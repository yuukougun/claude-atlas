#!/usr/bin/env python3
"""鮮度の点検の道具（設計書 §9.4 の手順の1・2・5。skill は .claude/skills/freshness-check/SKILL.md）。

点検の流れ：前回の点検の版と日付（`last`）より後の Claude Code の CHANGELOG・リリースノート・ニュースを読み、写した項目を
`match` にかけて影響のあるページと数値の一覧を出し、直した（確かめた）後に `checked` と `stamp` で記録を進める。
この道具は Web を使わず、記録を読む・書くだけである。`verified`（出典を読み直した日）と数値の確認日は、読み直した担当が書く
（この道具は書かない）。

使い方:
  uv run python tools/freshness.py last [--json]
      前回の点検の版と日付（data/inspection.yml）を出す。null は「まだ点検していない」。
  uv run python tools/freshness.py match [TEXT | -f FILE | -] [--json]
      変更の記録のテキスト（前回より後の項目）を、次に照らして、影響のあるページと数値の一覧を出す。
        features の match_terms と id（主のページと、tracks でその機能を指すページ）／ページの tracks と aliases／
        facts の id（本文の fact の目印を持つページ）／names の旧名・今の名前・id（本文の name の目印を持つページ）
      英語の大文字小文字・複数形（-s・-es）・「-」「_」「空白」の違いは吸収する。当たりすぎる一般の語は、設定
      tools/freshness.yml の exclude で外す（外した語で当たったものは、参考として最後に出す）。--exclude TERM で足せる。
      TEXT を省いて標準入力が端末でなければ標準入力を読む。--config FILE で設定を替える。
  uv run python tools/freshness.py stamp --version X.Y.Z --date YYYY-MM-DD [--release-notes-date D] [--news-date D] [--note 文]
      前回の点検の版と日付を data/inspection.yml に書く。date と release_notes と news は --date が既定
      （release_notes・news は読んだ最後の日なので、違うときは指定する）。記録より古い版・日付は --force がないと断る。
  uv run python tools/freshness.py checked <ページの id> [<id> …] --date YYYY-MM-DD
      影響がないと確かめたページの front matter の checked を進める（schema/keys.yml の checked：日付）。すでに同じか新しい
      日付なら変えない。verified は書かない。
共通: --root DIR で根を替える（試験用。DIR/schema/site.yml・DIR/docs・DIR/stubs・DIR/data）。
終了コード: 0＝済んだ、1＝id のページがない・古い版や日付を断った（ほかは処理する）、2＝読めない・引数の誤り
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import Fatal, load_atlas, load_data, parse_date  # noqa: E402
from lib.data import INSPECTION_FILE  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONFIG = Path(__file__).resolve().parent / "freshness.yml"
DEFAULT_MIN_LENGTH = 3
VERSION_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")       # schema/keys.yml の version の形
LAST_KEYS = ("date", "claude_code", "release_notes", "news")
SEP_RE = re.compile(r"(?<=[A-Za-z0-9])[-_\s]+(?=[A-Za-z0-9])")


# ---- 語の正規化と照合 -----------------------------------------------------------------------------------------------

def norm(s: str) -> str:
    """比べるための形：NFKC・小文字・空白をひとつに。"""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", s)).strip().casefold()


def clean_term(raw: str) -> str:
    """names の「今の名前」などに付いた注を外す（「…」の括弧と、（… 以降）。"""
    s = str(raw).replace("「", "").replace("」", "")
    s = re.split(r"[（(]", s, maxsplit=1)[0]
    return s.strip().strip("`")


def is_ascii(s: str) -> bool:
    return all(ord(c) < 128 for c in s)


def term_regex(term: str) -> re.Pattern:
    """語の正規表現。英語は大文字小文字・複数形・「-」「_」空白の違いを吸収し、前後が英数字なら当てない。日本語は部分一致。"""
    t = unicodedata.normalize("NFKC", term).strip()
    if not is_ascii(t):
        return re.compile(re.escape(t), re.I)
    parts = SEP_RE.split(t)
    body = r"[-_\s]*".join(re.escape(p) for p in parts)
    tail = r"(?:e?s)?" if t[-1:].isalpha() else ""
    return re.compile(r"(?<![A-Za-z0-9])" + body + tail + r"(?![A-Za-z0-9])", re.I)


@dataclass
class Settings:
    exclude: set[str] = field(default_factory=set)       # norm した語
    min_length: int = DEFAULT_MIN_LENGTH


def load_settings(path: Path | None, extra_exclude: list[str]) -> Settings:
    st = Settings()
    path = path if path is not None else CONFIG
    if path.exists():
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if not isinstance(doc, dict):
            raise Fatal(f"{path} の最上位をマッピングにする")
        ex = doc.get("exclude") or []
        if not isinstance(ex, list):
            raise Fatal(f"{path} の exclude をリストにする")
        st.exclude = {norm(str(x)) for x in ex}
        ml = doc.get("min_length")
        if isinstance(ml, int) and not isinstance(ml, bool) and ml >= 1:
            st.min_length = ml
    st.exclude |= {norm(x) for x in extra_exclude}
    return st


# ---- 照合の先（索引） -----------------------------------------------------------------------------------------------

@dataclass
class Entry:
    term: str                 # 元の語
    source: str               # どの照合の先か（人が読む形）
    pages: set[str]           # 当たったときに影響のあるページ
    numbers: set[str]         # 当たったときに影響のある数値（"features/<id>" など）


def build_entries(atlas) -> list[Entry]:
    data = atlas.data
    pages = [p for p in atlas.pages if p.id]
    tracking: dict[str, set[str]] = defaultdict(set)      # 機能の id → tracks で指すページ
    with_fact: dict[str, set[str]] = defaultdict(set)     # facts の id → 目印を持つページ
    with_name: dict[str, set[str]] = defaultdict(set)     # names の id → 目印を持つページ
    for p in pages:
        for t in p.tracks:
            tracking[t].add(p.id)
        for f in p.fact_ids():
            with_fact[f].add(p.id)
        for n in p.name_ids():
            with_name[n].add(p.id)
    out: list[Entry] = []
    features = data.features
    for fid, f in features.items():
        affected = set(tracking.get(fid, ()))
        main = f.text("page")
        if main:
            affected.add(main)
        num = {f"features/{fid}"}
        for t in f.strings("match_terms"):
            out.append(Entry(t, f"features:{fid} の照合の語", set(affected), set(num)))
        out.append(Entry(fid, f"features:{fid} の id", set(affected), set(num)))
    for p in pages:
        for t in p.tracks:
            if t not in features:
                out.append(Entry(t, "ページの tracks", {p.id}, set()))
        for a in p.aliases:
            out.append(Entry(a, "ページの aliases", {p.id}, set()))
    for fid in data.facts:
        out.append(Entry(fid, f"facts:{fid} の id", set(with_fact.get(fid, ())), {f"facts/{fid}"}))
    for nid, n in data.names.items():
        affected = set(with_name.get(nid, ()))
        feat = n.text("feature")
        if feat:
            affected |= tracking.get(feat, set())
            if feat in features and features[feat].text("page"):
                affected.add(features[feat].text("page"))
        num = {f"names/{nid}"}
        for t in n.strings("old"):
            out.append(Entry(clean_term(t), f"names:{nid} の旧名", set(affected), set(num)))
        out.append(Entry(clean_term(n.text("current")), f"names:{nid} の今の名前", set(affected), set(num)))
        out.append(Entry(nid, f"names:{nid} の id", set(affected), set(num)))
    return out


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def run_match(atlas, text: str, st: Settings) -> dict:
    text = unicodedata.normalize("NFKC", text)
    groups: dict[str, list[Entry]] = defaultdict(list)
    skipped: set[str] = set()
    for e in build_entries(atlas):
        t = e.term.strip()
        key = norm(t)
        if not key:
            continue
        floor = st.min_length if is_ascii(key) else 2
        if len(key) < floor and key not in st.exclude:
            skipped.add(t)
            continue
        groups[key].append(e)
    page_hits: dict[str, list[dict]] = defaultdict(list)
    num_hits: dict[str, dict] = {}
    excluded: list[dict] = []
    for key, entries in groups.items():
        m = term_regex(entries[0].term).search(text)
        if m is None:
            continue
        line = line_of(text, m.start())
        if key in st.exclude:
            excluded.append({"term": entries[0].term, "line": line})
            continue
        for e in entries:
            hit = {"term": e.term, "source": e.source, "line": line}
            for pid in e.pages:
                if hit not in page_hits[pid]:
                    page_hits[pid].append(hit)
            for nid in e.numbers:
                rec = num_hits.setdefault(nid, {"hits": [], "pages": set()})
                if hit not in rec["hits"]:
                    rec["hits"].append(hit)
                rec["pages"] |= e.pages
    by_id = {p.id: p for p in atlas.pages if p.id}
    pages_out = []
    for pid, hits in page_hits.items():
        p = by_id.get(pid)
        pages_out.append({"id": pid, "title": p.text("title") if p else "（このページはない）", "stage": p.stage if p else "",
                          "hits": sorted(hits, key=lambda h: (h["line"], h["term"]))})
    pages_out.sort(key=lambda r: (-len({owner_of(h) for h in r["hits"]}), r["id"]))
    nums_out = [{"id": nid, "hits": sorted(r["hits"], key=lambda h: (h["line"], h["term"])), "pages": sorted(r["pages"])}
                for nid, r in num_hits.items()]
    nums_out.sort(key=lambda r: (-len(r["hits"]), r["id"]))
    excluded.sort(key=lambda r: (r["line"], r["term"]))
    return {"lines": text.count("\n") + 1, "terms": len(groups), "pages": pages_out, "numbers": nums_out,
            "excluded": excluded, "skipped_short": sorted(skipped)}


def owner_of(hit: dict) -> str:
    """当たりの持ち主（features:hooks・ページの aliases など。同じ持ち主の複数の語を1行にまとめるため）。"""
    return hit["source"].split(" の", 1)[0]


def render_hits(hits: list[dict]) -> list[str]:
    """持ち主ごとに、語（hook と hooks のような複数形の違いは1つ）と最初の行をまとめる。"""
    groups: dict[str, dict] = {}
    for h in hits:
        g = groups.setdefault(owner_of(h), {"terms": {}, "line": h["line"]})
        g["terms"].setdefault(norm(h["term"]).rstrip("s"), h["term"])
        g["line"] = min(g["line"], h["line"])
    return [f"    - {o} ← {'・'.join(g['terms'].values())}（{g['line']} 行目）" for o, g in groups.items()]


def render_match(res: dict) -> str:
    out = [f"# 照合の結果（入力 {res['lines']} 行・照らした語 {res['terms']} 個）", ""]
    out.append(f"## 影響のあるページ（{len(res['pages'])}）")
    for r in res["pages"]:
        stage = f" [{r['stage']}]" if r["stage"] else ""
        out.append(f"- {r['id']}「{r['title']}」{stage}")
        out += render_hits(r["hits"])
    if not res["pages"]:
        out.append("- なし")
    out += ["", f"## 影響のある数値（{len(res['numbers'])}）"]
    for r in res["numbers"]:
        out.append(f"- {r['id']}")
        out += render_hits(r["hits"])
        if r["pages"]:
            out.append(f"    - 関わるページ：{'・'.join(r['pages'])}")
    if not res["numbers"]:
        out.append("- なし")
    if res["excluded"]:
        out += ["", f"## 参考：除外した語で当たったもの（{len(res['excluded'])}）。一般の語なので影響の判断に使わない"]
        out.append("- " + "・".join(f"{r['term']}（{r['line']} 行目）" for r in res["excluded"]))
    return "\n".join(out) + "\n"


# ---- 前回の点検の記録 ----------------------------------------------------------------------------------------------

def read_last(root: Path) -> dict:
    data = load_data(root)
    last = data.last_inspection()
    return {k: last.get(k) for k in LAST_KEYS} | ({"note": last["note"]} if last.get("note") else {})


def render_last(last: dict) -> str:
    if all(last.get(k) is None for k in LAST_KEYS):
        return "前回の点検：まだない（初回。CHANGELOG・リリースノート・ニュースの読める範囲を新しいほうから読む）\n"
    lines = [
        f"前回の点検の日：{last.get('date')}",
        f"Claude Code の版（CHANGELOG を読んだ最後）：{last.get('claude_code')}",
        f"リリースノート（Help Center と Claude Platform）を読んだ最後の日：{last.get('release_notes')}",
        f"Anthropic のニュースを読んだ最後の日：{last.get('news')}",
    ]
    if last.get("note"):
        lines.append(f"注：{last['note']}")
    return "\n".join(lines) + "\n"


def version_tuple(v: str) -> tuple[int, ...]:
    return tuple(int(x) for x in v.split("."))


def set_scalar(text: str, key: str, value: str) -> str | None:
    """`last:` の下の `  key: 値  # 注` の値を替える（注と、注の位置はできるだけ残す）。ない行は None。"""
    pat = re.compile(rf"^(  {re.escape(key)}:[ \t]*)([^#\n]*?)([ \t]*)(#[^\n]*)?$", re.M)
    m = pat.search(text)
    if m is None:
        return None
    pad = m.group(3)
    if m.group(4):
        width = len(m.group(2)) + len(pad)
        pad = " " * max(1, width - len(value))
    else:
        pad = ""
    return text[:m.start()] + m.group(1) + value + pad + (m.group(4) or "") + text[m.end():]


def yq(s: str) -> str:
    return "'" + s + "'"


def run_stamp(root: Path, version: str, date: str, rn_date: str, news_date: str, note: str | None, force: bool) -> tuple[int, str]:
    for label, v in (("--date", date), ("--release-notes-date", rn_date), ("--news-date", news_date)):
        if parse_date(v) is None:
            return 2, f"{label} は日付（2026-11-04 の形）にする：{v}"
    if not VERSION_RE.match(version):
        return 2, f"--version は版（2.1.317 の形）にする：{version}"
    path = root / INSPECTION_FILE
    if not path.exists():
        return 2, f"{INSPECTION_FILE} がない"
    text = path.read_text(encoding="utf-8")
    old = read_last(root)
    if not force:
        if old.get("claude_code") and version_tuple(version) < version_tuple(old["claude_code"]):
            return 1, f"記録の版 {old['claude_code']} より古い版 {version} は書かない（直すなら --force）"
        for key, new in (("date", date), ("release_notes", rn_date), ("news", news_date)):
            if old.get(key) and new < old[key]:
                return 1, f"記録の {key}（{old[key]}）より古い日付 {new} は書かない（直すなら --force）"
    values = {"date": yq(date), "claude_code": version, "release_notes": yq(rn_date), "news": yq(news_date)}
    for key, val in values.items():
        new_text = set_scalar(text, key, val)
        if new_text is None:
            return 2, f"{INSPECTION_FILE} に「  {key}:」の行がない（last の下の4つのキーを残す）"
        text = new_text
    if note is not None:
        new_text = set_scalar(text, "note", json.dumps(note, ensure_ascii=False))
        if new_text is None:
            text = text.rstrip("\n") + "\n  note: " + json.dumps(note, ensure_ascii=False) + "\n"
        else:
            text = new_text
    path.write_text(text, encoding="utf-8")
    return 0, render_last(read_last(root))


# ---- ページの checked ---------------------------------------------------------------------------------------------

def set_front_matter_key(text: str, key: str, value: str) -> tuple[str, str | None]:
    """front matter の最上位のキーを替える（なければ閉じる --- の前に足す）。(新しい文、前の値か None) を返す。"""
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip() != "---":
        raise ValueError("front matter がない")
    end = next((i for i in range(1, len(lines)) if lines[i].rstrip() in ("---", "...")), None)
    if end is None:
        raise ValueError("front matter が閉じていない")
    eol = "\r\n" if lines[0].endswith("\r\n") else "\n"
    pat = re.compile(rf"^{re.escape(key)}:[ \t]*(.*?)[ \t]*$")
    for i in range(1, end):
        m = pat.match(lines[i].rstrip("\r\n"))
        if m:
            lines[i] = f"{key}: {value}{eol}"
            return "".join(lines), m.group(1)
    lines.insert(end, f"{key}: {value}{eol}")
    return "".join(lines), None


def run_checked(root: Path, ids: list[str], date: str) -> tuple[int, list[str]]:
    if parse_date(date) is None:
        return 2, [f"--date は日付（2026-11-04 の形）にする：{date}"]
    atlas = load_atlas(root)
    by_id: dict[str, list] = defaultdict(list)
    for p in atlas.pages:
        by_id[p.id].append(p)
    msgs, code = [], 0
    for pid in dict.fromkeys(ids):
        found = by_id.get(pid)
        if not found:
            msgs.append(f"{pid}：ページがない")
            code = 1
            continue
        for page in found:
            path = root / page.base / page.rel
            text = path.read_text(encoding="utf-8")
            try:
                new, prev = set_front_matter_key(text, "checked", date)
            except ValueError as e:
                msgs.append(f"{pid}：{page.base}/{page.rel} を書けない（{e}）")
                code = 1
                continue
            prev_date = parse_date(prev.strip("'\"")) if prev else None
            if prev_date is not None and prev_date >= parse_date(date):
                msgs.append(f"{pid}：checked は {prev} のまま（{date} と同じか新しい）")
                continue
            path.write_text(new, encoding="utf-8")
            msgs.append(f"{pid}：checked: {prev or 'なし'} → {date}（{page.base}/{page.rel}）")
    return code, msgs


# ---- コマンド行 ----------------------------------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="freshness.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT, help="根（既定はこのリポジトリ）")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_last = sub.add_parser("last", help="前回の点検の版と日付を出す")
    p_last.add_argument("--json", action="store_true")
    p_match = sub.add_parser("match", help="変更の記録のテキストを照合の先に照らす")
    p_match.add_argument("text", nargs="?", help="テキスト（省くと標準入力。- も標準入力）")
    p_match.add_argument("-f", "--file", type=Path, help="テキストのファイル")
    p_match.add_argument("--exclude", action="append", default=[], metavar="TERM", help="外す語を足す（繰り返せる）")
    p_match.add_argument("--config", type=Path, help="設定（既定は tools/freshness.yml）")
    p_match.add_argument("--json", action="store_true")
    p_stamp = sub.add_parser("stamp", help="前回の点検の版と日付を書く")
    p_stamp.add_argument("--version", required=True, help="CHANGELOG を読んだ最後の Claude Code の版（x.y.z）")
    p_stamp.add_argument("--date", required=True, help="点検の日")
    p_stamp.add_argument("--release-notes-date", help="リリースノートを読んだ最後の日（既定は --date）")
    p_stamp.add_argument("--news-date", help="ニュースを読んだ最後の日（既定は --date）")
    p_stamp.add_argument("--note", help="注（平文）")
    p_stamp.add_argument("--force", action="store_true", help="記録より古い版・日付も書く")
    p_checked = sub.add_parser("checked", help="影響がないと確かめたページの checked を進める")
    p_checked.add_argument("ids", nargs="+", metavar="ページの id")
    p_checked.add_argument("--date", required=True, help="確かめた日")
    args = parser.parse_args(argv)
    root = args.root
    try:
        if args.cmd == "last":
            last = read_last(root)
            print(json.dumps(last, ensure_ascii=False, indent=2) if args.json else render_last(last), end="" if not args.json else "\n")
            return 0
        if args.cmd == "match":
            if args.file is not None:
                text = args.file.read_text(encoding="utf-8")
            elif args.text is not None and args.text != "-":
                text = args.text
            elif args.text == "-" or not sys.stdin.isatty():
                text = sys.stdin.read()
            else:
                print("テキストを渡す（引数・-f FILE・標準入力）", file=sys.stderr)
                return 2
            res = run_match(load_atlas(root), text, load_settings(args.config, args.exclude))
            print(json.dumps(res, ensure_ascii=False, indent=2) if args.json else render_match(res), end="" if not args.json else "\n")
            return 0
        if args.cmd == "stamp":
            code, msg = run_stamp(root, args.version, args.date, args.release_notes_date or args.date, args.news_date or args.date,
                                  args.note, args.force)
            print(msg, file=sys.stderr if code else sys.stdout)
            return code
        code, msgs = run_checked(root, args.ids, args.date)
        for m in msgs:
            print(m, file=sys.stderr if code == 2 else sys.stdout)
        return code
    except (Fatal, OSError) as e:
        print(f"読めない：{e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
