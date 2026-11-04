#!/usr/bin/env python3
"""外のリンクの切れと転送を確かめる道具（設計書 §9.4 の手順6。鮮度の点検の skill の「リンクの切れと転送」）。

確かめる URL は、次の2つから集める。
  - docs/ の公開するページ（stage が draft 以上で docs/ にあるもの）の本文の URL（コードの中は除く）
  - data/sources.yml と data/sources.d/ の出典の url
同じ URL（# 以降と末尾の / の違いを除く）は1回だけ問い合わせ、使っている所（ページの id・出典の id）を添える。
問い合わせの結果は、状態で分ける。
  正常        HTTP 2xx（転送なし）
  転送        転送をたどった先が 2xx。転送先の URL を出す（出典の記録は転送先を持つ。common §11・research/28）
  切れ        HTTP 4xx・5xx（401・403・429 を除く）、接続できない・時間切れ、転送が多すぎる・転送の先が切れている
  要確認      401・403・429（サイトが機械の問い合わせを断っただけのことが多い。手で開いて見る）
  確かめない  .claude/settings.json の deny の WebFetch(domain:…)・data/sources.yml で noai が true のドメイン・
              tools/check_noai.py の既知の一覧（atcoder.jp・codeforces.com など）のホスト。問い合わせない
              （転送の先がそのホストなら、そこで止めて「転送先は確かめない」と出す）。例の URL（example.com・localhost など）も同じ

使い方:
  uv run python tools/check_links.py --dry-run      問い合わせず、対象の一覧（問い合わせる・確かめない）だけを出す
  uv run python tools/check_links.py                全部問い合わせて、結果を表で標準出力へ出す（ファイルは書き換えない）
  uv run python tools/check_links.py --only-problems 正常を表から外す（数は最後に出る）
  uv run python tools/check_links.py --json          結果を JSON で出す
  uv run python tools/check_links.py --root DIR       根を替える（試験用。DIR/schema/site.yml・DIR/docs・DIR/data・DIR/.claude/settings.json）
問い合わせの作法（相手のサイトに負担をかけない）:
  - 同じホストへの問い合わせの間を --interval 秒（既定 1.0）あける
  - 同時に --workers 本（既定 4）まで。別のホストの問い合わせは並べて進める
  - 1回の問い合わせは --timeout 秒（既定 15）で切る。転送は最大 5 回までたどる
  - HEAD で問い合わせ、HEAD を断られたとき（400・403・405・501）だけ GET で1回やり直す（本文は読まない）
  - User-Agent は一般の名前（claude-atlas-link-check）。メールアドレスなどの個人の情報は入れない
終了コード: 0＝切れがない、1＝切れがある、2＝読めない・引数の誤り
標準ライブラリと tools/lib だけで動く。本物のネットに出るのは、--dry-run を付けない実行だけ（工程10で流す）。
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import Fatal, load_atlas  # noqa: E402
from lib.data import host_of, url_key  # noqa: E402
from check_noai import KNOWN_NOAI  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
USER_AGENT = "claude-atlas-link-check"
DEFAULT_INTERVAL = 1.0
DEFAULT_WORKERS = 4
DEFAULT_TIMEOUT = 15.0
MAX_HOPS = 5
HEAD_REFUSED = (400, 403, 405, 501)       # HEAD を断られたときだけ GET でやり直す
CHECK_BY_HAND = (401, 403, 429)
EXAMPLE_HOSTS = ("example.com", "example.org", "example.net", "localhost", "127.0.0.1", "0.0.0.0")
EXAMPLE_SUFFIXES = (".example.com", ".example", ".invalid", ".test", ".localhost", ".local")

# 状態（表に出す名前と並べる順）
OK, MOVED, BROKEN, MANUAL, SKIPPED = "正常", "転送", "切れ", "要確認", "確かめない"
ORDER = {BROKEN: 0, MANUAL: 1, MOVED: 2, SKIPPED: 3, OK: 4}

URL_RE = re.compile(r"https?://[A-Za-z0-9\-._~:/?#@!$&*+,;=%()]+")      # ASCII の URL の文字だけ（日本語の句読点・括弧で止まる）
FENCE_RE = re.compile(r"^(`{3,}|~{3,}).*?^\1[ \t]*$", re.S | re.M)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


# ---- 対象を集める ---------------------------------------------------------------------------------------------------

@dataclass
class Target:
    url: str                                   # 問い合わせる URL（# 以降を除く）
    used_by: list[str] = field(default_factory=list)      # 「ページ <id>」「出典 <id>」
    skip: str | None = None                    # 問い合わせない理由

    @property
    def host(self) -> str:
        return host_of(self.url)


def clean_url(raw: str) -> str:
    """本文から拾った URL の後ろの記号（括弧・句読点）を落とし、# 以降を除く。"""
    u = raw
    while u:
        c = u[-1]
        if c in ".,;:!?*_'\"、。）」』】":
            u = u[:-1]
        elif c == ")" and u.count(")") > u.count("("):
            u = u[:-1]
        else:
            break
    return u.split("#", 1)[0]


def urls_in_markdown(body: str) -> list[str]:
    """本文の http(s) の URL（コードブロックとインラインのコードの中は除く）。"""
    text = INLINE_CODE_RE.sub(" ", FENCE_RE.sub(" ", body))
    out = []
    for m in URL_RE.finditer(text):
        u = clean_url(m.group(0))
        if re.match(r"https?://[^/]", u):
            out.append(u)
    return out


def deny_domains(root: Path) -> dict[str, str]:
    """.claude/settings.json の deny の WebFetch(domain:…)（*. を外す）→ 理由。読めなければ空。"""
    path = root / ".claude" / "settings.json"
    try:
        deny = json.loads(path.read_text(encoding="utf-8")).get("permissions", {}).get("deny", [])
    except Exception:  # noqa: BLE001
        return {}
    out: dict[str, str] = {}
    for rule in deny if isinstance(deny, list) else []:
        m = re.fullmatch(r"WebFetch\(domain:([^)]+)\)", str(rule).strip())
        if m:
            d = m.group(1).strip().lower().rstrip(".")
            if d.startswith("*."):
                d = d[2:]
            if d and "*" not in d:
                out.setdefault(d, ".claude/settings.json の deny にある")
    return out


def no_query_domains(root: Path, noai: list[str]) -> dict[str, str]:
    """問い合わせないドメイン→理由。deny・data の noai・check_noai の既知の一覧。"""
    out = dict(deny_domains(root))
    for d in noai:
        out.setdefault(d, "data/sources.yml で AI の利用を断るドメイン")
    for d in KNOWN_NOAI:
        out.setdefault(d, "tools/check_noai.py の既知の noai")
    return out


def skip_reason(url: str, blocked: dict[str, str]) -> str | None:
    host = host_of(url)
    if not host:
        return "ホストがない"
    for d, why in blocked.items():
        if host == d or host.endswith("." + d):
            return f"{d}：{why}"
    if host in EXAMPLE_HOSTS or host.endswith(EXAMPLE_SUFFIXES):
        return "例の URL（実在しない）"
    return None


def collect_targets(root: Path) -> tuple[list[Target], dict[str, str]]:
    """公開するページの本文と、出典の url から URL を集める。(対象, 問い合わせないドメイン→理由) を返す。"""
    atlas = load_atlas(root)
    found: dict[str, Target] = {}

    def add(url: str, label: str) -> None:
        try:
            key = url_key(url)
        except ValueError:                      # 壊れた URL は、そのまま問い合わせて「切れ」に出す
            key = url
        t = found.setdefault(key, Target(url))
        if label not in t.used_by:
            t.used_by.append(label)

    for page in atlas.published():
        body = getattr(page, "body", "")
        for u in urls_in_markdown(body):
            add(u, f"ページ {page.id}")
    for item in atlas.data.entries("sources"):
        u = item.raw.get("url")
        if isinstance(u, str) and re.match(r"https?://[^/]", u.strip()):
            add(clean_url(u.strip()), f"出典 {item.id or '(id なし)'}")
    blocked = no_query_domains(root, atlas.data.noai_domains())
    targets = list(found.values())
    for t in targets:
        t.skip = skip_reason(t.url, blocked)
    return sorted(targets, key=lambda t: (t.host, t.url)), blocked


def interleave(targets: list[Target]) -> list[Target]:
    """ホストを順に回る並びにする（同じホストの待ちで、ほかのホストが遅れないように）。"""
    by_host: dict[str, list[Target]] = defaultdict(list)
    for t in targets:
        by_host[t.host].append(t)
    queues = list(by_host.values())
    out: list[Target] = []
    while any(queues):
        for q in queues:
            if q:
                out.append(q.pop(0))
    return out


# ---- 問い合わせ -----------------------------------------------------------------------------------------------------

class HostGate:
    """同じホストへの問い合わせの間をあける（順番に時刻を予約する。時計と待ちは試験で差し替える）。"""

    def __init__(self, interval: float, clock: Callable[[], float] = time.monotonic,
                 sleep: Callable[[float], None] = time.sleep):
        self.interval = interval
        self._clock, self._sleep = clock, sleep
        self._next: dict[str, float] = {}
        self._lock = threading.Lock()

    def wait(self, host: str) -> float:
        with self._lock:
            now = self._clock()
            at = max(now, self._next.get(host, now))
            self._next[host] = at + self.interval
        delay = at - now
        if delay > 0:
            self._sleep(delay)
        return delay


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None       # 転送は自分でたどる（どの URL を経たかを残し、確かめないホストへは行かないため）


_OPENER = urllib.request.build_opener(_NoRedirect)


def fetch_once(url: str, method: str, timeout: float) -> tuple[int, str | None]:
    """1回だけ問い合わせて (HTTP の状態, Location) を返す。接続できない・時間切れは OSError を投げる。"""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        res = _OPENER.open(req, timeout=timeout)
    except urllib.error.HTTPError as e:         # 3xx（転送を断った）・4xx・5xx
        try:
            return e.code, e.headers.get("Location")
        finally:
            e.close()
    except urllib.error.URLError as e:
        raise OSError(str(e.reason)) from e
    with res:
        return res.status, res.headers.get("Location")


Fetch = Callable[[str, str, float], "tuple[int, str | None]"]


@dataclass
class Result:
    url: str
    status: str                                 # OK・MOVED・BROKEN・MANUAL・SKIPPED
    http: int | None = None                     # 最後の HTTP の状態
    final_url: str | None = None                # 転送された先（転送がなければ None）
    first_code: int | None = None               # 最初の転送の状態（301・308 は恒久、302・307 は一時）
    note: str = ""
    used_by: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {"url": self.url, "status": self.status, "http": self.http, "final_url": self.final_url,
                "first_redirect": self.first_code, "note": self.note, "used_by": self.used_by}


def probe(target: Target, fetch: Fetch, gate: HostGate, timeout: float, blocked: dict[str, str]) -> Result:
    """URL を問い合わせ、転送をたどって結果にする。"""
    res = Result(target.url, OK, used_by=list(target.used_by))
    if target.skip:
        res.status, res.note = SKIPPED, target.skip
        return res
    url, hops, first = target.url, 0, None
    while True:
        gate.wait(host_of(url))
        try:
            code, loc = fetch(url, "HEAD", timeout)
            if code in HEAD_REFUSED:
                gate.wait(host_of(url))
                code, loc = fetch(url, "GET", timeout)
        except Exception as e:  # noqa: BLE001  接続できない・時間切れ・証明書の誤りなど
            res.status, res.note = BROKEN, f"接続できない：{e}"
            res.final_url = url if url != target.url else None
            res.first_code = first
            return res
        res.http = code
        if code in (301, 302, 303, 307, 308) and loc:
            nxt = urllib.parse.urljoin(url, loc)
            first = first if first is not None else code
            res.final_url, res.first_code = nxt, first
            why = skip_reason(nxt, blocked)
            if why:
                res.status, res.note = SKIPPED, f"転送先は確かめない（{why}）"
                return res
            hops += 1
            if hops > MAX_HOPS:
                res.status, res.note = BROKEN, f"転送が {MAX_HOPS} 回を超える"
                return res
            url = nxt
            continue
        break
    if 200 <= code < 300:
        res.status = MOVED if res.final_url else OK
    elif code in CHECK_BY_HAND:
        res.status, res.note = MANUAL, "サイトが機械の問い合わせを断った可能性（手で開いて見る）"
    else:
        res.status = BROKEN
        res.note = "転送の先が切れている" if res.final_url else ""
    return res


def run(targets: list[Target], fetch: Fetch = fetch_once, interval: float = DEFAULT_INTERVAL,
        workers: int = DEFAULT_WORKERS, timeout: float = DEFAULT_TIMEOUT, blocked: dict[str, str] | None = None,
        gate: HostGate | None = None) -> list[Result]:
    gate = gate or HostGate(interval)
    blocked = blocked or {}
    todo = interleave(targets)
    with ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        results = list(pool.map(lambda t: probe(t, fetch, gate, timeout, blocked), todo))
    return sorted(results, key=lambda r: (ORDER[r.status], host_of(r.url), r.url))


# ---- 出力 -----------------------------------------------------------------------------------------------------------

def cell(s: object) -> str:
    return str(s).replace("|", "\\|").replace("\n", " ")


def used_text(used: list[str], limit: int = 3) -> str:
    shown = "、".join(used[:limit])
    return shown + (f" ほか{len(used) - limit}" if len(used) > limit else "")


def table(header: list[str], rows: list[list[object]]) -> str:
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    lines += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def show_dry_run(targets: list[Target]) -> str:
    rows = [["確かめない" if t.skip else "問い合わせる", t.url, used_text(t.used_by), t.skip or ""] for t in targets]
    skipped = sum(1 for t in targets if t.skip)
    hosts = len({t.host for t in targets if not t.skip})
    head = f"対象 {len(targets)} 件（問い合わせる {len(targets) - skipped} 件・{hosts} ホスト／確かめない {skipped} 件）。問い合わせていない（--dry-run）。"
    return head + "\n\n" + table(["予定", "URL", "使っている所", "理由"], rows)


def show_results(results: list[Result], only_problems: bool) -> str:
    count = {s: sum(1 for r in results if r.status == s) for s in ORDER}
    rows = []
    for r in results:
        if only_problems and r.status == OK:
            continue
        where = r.final_url or ""
        if r.final_url and r.first_code:
            where = f"{r.final_url}（{r.first_code}）"
        rows.append([r.status, r.url, r.http if r.http is not None else "-", where, r.note, used_text(r.used_by)])
    summary = "、".join(f"{s} {count[s]}" for s in sorted(ORDER, key=ORDER.get))
    head = f"{len(results)} 件：{summary}"
    if not rows:
        return head
    return head + "\n\n" + table(["状態", "URL", "HTTP", "転送先", "メモ", "使っている所"], rows)


def main(argv: list[str] | None = None, fetch: Fetch = fetch_once) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT, help="根（既定はこのリポジトリ）")
    parser.add_argument("--dry-run", action="store_true", help="問い合わせず、対象の一覧だけを出す")
    parser.add_argument("--json", action="store_true", help="JSON で出す")
    parser.add_argument("--only-problems", action="store_true", help="正常を表から外す")
    parser.add_argument("--interval", type=float, default=DEFAULT_INTERVAL, help="同じホストへの問い合わせの間（秒）")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS, help="同時に問い合わせる本数")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT, help="1回の問い合わせの時間切れ（秒）")
    args = parser.parse_args(argv)
    if args.interval < 0 or args.workers < 1 or args.timeout <= 0:
        print("--interval は 0 以上、--workers は 1 以上、--timeout は正の数にする", file=sys.stderr)
        return 2
    try:
        targets, blocked = collect_targets(args.root)
    except Fatal as e:
        print(f"読めない：{e}", file=sys.stderr)
        return 2
    if args.dry_run:
        if args.json:
            print(json.dumps([{"url": t.url, "used_by": t.used_by, "skip": t.skip} for t in targets],
                             ensure_ascii=False, indent=1))
        else:
            print(show_dry_run(targets))
        return 0
    results = run(targets, fetch, args.interval, args.workers, args.timeout, blocked)
    if args.json:
        print(json.dumps([r.as_dict() for r in results], ensure_ascii=False, indent=1))
    else:
        print(show_results(results, args.only_problems))
    return 1 if any(r.status == BROKEN for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
