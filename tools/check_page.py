#!/usr/bin/env python3
"""1ページ分の検査をまとめて流し、指摘だけを短く出す（担当が書き終えた後と直した後に1回ずつ流す。decisions 2026-11-05「使用量を抑える運用」）。

流すもの（この順）:
  1 生成    tools/gen_site.py --page <id>      目印の間を書く（--no-gen で飛ばす）。出力の「注意」は警告として拾う
  2 参照    tools/check_pages.py --page <id>   front matter・参照・目印・数値と出典
  3 書き方  textlint（tools/textlint_targets.py の対象のうち、そのページのファイルだけ）
            骨格（stub）のページは textlint の対象外なので、飛ばして「対象外」と書く

使い方:
  uv run python tools/check_page.py <id> [<id> …]
  uv run python tools/check_page.py <id> --no-gen        生成を飛ばす
  uv run python tools/check_page.py <id> --limit 30      出す指摘の上限（既定 25。超えた分は件数だけ書く。0 で無制限）
  uv run python tools/check_page.py <id> --root DIR      DIR を根にして読む（試験用）

出力: 1指摘1行（エラーを先に）。形は「エラー <場所> [<検査>] <内容>」（警告は「警告 」で始まる）。最後の1行は「エラー N・警告 M」。
終了コード: 0＝エラーがない、1＝エラーがある、2＝検査できない（id のページがない・道具が動かない など）
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

import textlint_targets as tt  # noqa: E402

DEFAULT_LIMIT = 25
MESSAGE_WIDTH = 140
PAGES_LINE_RE = re.compile(r"^(エラー|警告): (?P<where>[^:]+(?::\d+)?): (?P<id>\S+): (?P<rest>\[[^\]]+\] .*)$")


class CannotCheck(Exception):
    """検査できない（終了コード 2）。"""


class Issue:
    def __init__(self, severity: str, where: str, text: str):
        self.severity = severity      # "エラー" か "警告"
        self.where = where
        self.text = text

    def line(self) -> str:
        head = f"{self.severity} {self.where}" if self.where else self.severity
        return clip(f"{head} {self.text}".rstrip())

    @property
    def is_error(self) -> bool:
        return self.severity == "エラー"


def clip(s: str, n: int = MESSAGE_WIDTH) -> str:
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def page_file(root: Path, pid: str) -> Path | None:
    """docs/ か stubs/ の <分野>/<id>.md（root からの相対パス）。なければ None。"""
    for base in ("docs", "stubs"):
        found = sorted((root / base).glob(f"*/{pid}.md"))
        if found:
            return found[0].relative_to(root)
    return None


def run(cmd: list[str], root: Path) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(cmd, cwd=root, capture_output=True, text=True, encoding="utf-8")
    except OSError as e:
        raise CannotCheck(f"{cmd[0]} が動かない（{e}）") from None


def tool_args(script: str, root: Path) -> list[str]:
    cmd = [sys.executable, str(TOOLS / script)]
    if root != ROOT:
        cmd += ["--root", str(root)]
    return cmd


def run_gen(root: Path, pid: str) -> list[Issue]:
    done = run(tool_args("gen_site.py", root) + ["--page", pid], root)
    if done.returncode != 0:
        msg = (done.stderr or done.stdout).strip().splitlines()
        raise CannotCheck(f"gen_site.py --page {pid} が失敗した（終了コード {done.returncode}）：{msg[0] if msg else ''}")
    issues = []
    for ln in done.stdout.splitlines():
        if ln.startswith("注意:"):
            issues.append(Issue("警告", "", f"[gen_site] {ln[len('注意:'):].strip()}"))
    return issues


def run_check_pages(root: Path, ids: list[str]) -> list[Issue]:
    args: list[str] = []
    for pid in ids:
        args += ["--page", pid]
    done = run(tool_args("check_pages.py", root) + args, root)
    if done.returncode not in (0, 1):
        msg = (done.stderr or done.stdout).strip().splitlines()
        raise CannotCheck(f"check_pages.py が検査できない：{msg[0] if msg else ''}")
    issues = []
    for ln in done.stdout.splitlines():
        m = PAGES_LINE_RE.match(ln)
        if m:
            issues.append(Issue(ln.split(":", 1)[0], m["where"], m["rest"]))
        elif ln.startswith(("エラー:", "警告:")):
            issues.append(Issue(ln.split(":", 1)[0], "", ln.split(":", 1)[1].strip()))
    return issues


def run_textlint(root: Path, files: list[Path]) -> list[Issue]:
    if not files:
        return []
    exe = root / tt.TEXTLINT
    if not exe.exists():
        raise CannotCheck(f"textlint がない（{tt.TEXTLINT.as_posix()}）。リポジトリの根で npm ci を流す")
    # 生成の目印の間は、lint:text（textlint_targets.py --run）と同じく検査から外す（写しに textlint-disable を足して流す）
    tmp = Path(tempfile.mkdtemp(prefix=".textlint-mask-", dir=root))
    back: dict[str, str] = {}   # 写しの絶対パス → 元のページの相対パス
    args = []
    try:
        for f in files:
            src = f if f.is_absolute() else root / f
            try:
                text = src.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                args.append(src.as_posix())
                continue
            if not tt.has_generated_marker(text):
                args.append(src.as_posix())
                continue
            rel_src = src.resolve().relative_to(root.resolve())
            copy = tmp / rel_src
            copy.parent.mkdir(parents=True, exist_ok=True)
            copy.write_text(tt.mask_generated(text), encoding="utf-8")
            back[copy.resolve().as_posix()] = rel_src.as_posix()
            args.append(copy.as_posix())
        done = run([str(exe), "-f", "json", *args], root)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    try:
        results = json.loads(done.stdout)
    except json.JSONDecodeError:
        msg = (done.stderr or done.stdout).strip().splitlines()
        raise CannotCheck(f"textlint の出力が読めない（終了コード {done.returncode}）：{msg[0] if msg else ''}") from None
    issues = []
    for res in results:
        fp = Path(res["filePath"]).resolve().as_posix()
        if fp in back:
            rel = back[fp]
        else:
            try:
                rel = Path(res["filePath"]).resolve().relative_to(root.resolve()).as_posix()
            except ValueError:
                rel = res["filePath"]
        for m in res.get("messages", []):
            sev = "エラー" if m.get("severity") == 2 else "警告"
            issues.append(Issue(sev, f"{rel}:{m.get('line', 0)}:{m.get('column', 0)}", f"[textlint:{m.get('ruleId', '')}] {m.get('message', '')}"))
    return issues


def check(root: Path, ids: list[str], gen: bool = True) -> tuple[list[Issue], list[str]]:
    """指摘の一覧と、補足（飛ばしたものなど）を返す。"""
    notes: list[str] = []
    files: dict[str, Path] = {}
    for pid in ids:
        f = page_file(root, pid)
        if f is None:
            raise CannotCheck(f"「{pid}」のページが docs/ にも stubs/ にもない")
        files[pid] = f
    issues: list[Issue] = []
    if gen:
        for pid in ids:
            issues += run_gen(root, pid)
    issues += run_check_pages(root, ids)
    listed = set(tt.targets(root))
    lint_files = []
    for pid, f in files.items():
        if f in listed:
            lint_files.append(f)
        else:
            notes.append(f"textlint は対象外：{f.as_posix()}（骨格のページ）")
    issues += run_textlint(root, lint_files)
    return issues, notes


def render(issues: list[Issue], notes: list[str], limit: int) -> list[str]:
    ordered = [i for i in issues if i.is_error] + [i for i in issues if not i.is_error]
    shown = ordered if limit <= 0 else ordered[:limit]
    out = [i.line() for i in shown]
    if len(ordered) > len(shown):
        out.append(f"（ほか {len(ordered) - len(shown)} 件は上限 {limit} 件で省略。直してからもう一度流す）")
    out += notes
    errors = sum(1 for i in issues if i.is_error)
    out.append(f"エラー {errors}・警告 {len(issues) - errors}")
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="1ページ分の検査（生成・参照・書き方）をまとめて流し、指摘だけを短く出す")
    parser.add_argument("ids", nargs="+", metavar="id", help="ページの id")
    parser.add_argument("--no-gen", action="store_true", help="目印を書く gen_site.py を飛ばす")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help=f"出す指摘の上限（既定 {DEFAULT_LIMIT}。0 で無制限）")
    parser.add_argument("--root", type=Path, default=ROOT, help="リポジトリの根（試験用）")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    ids = list(dict.fromkeys(args.ids))
    try:
        issues, notes = check(root, ids, gen=not args.no_gen)
    except (CannotCheck, tt.CannotCheck) as e:
        print(f"検査できない: {e}", file=sys.stderr)
        return 2
    for ln in render(issues, notes, args.limit):
        print(ln)
    return 1 if any(i.is_error for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
