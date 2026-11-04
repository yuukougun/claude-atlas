#!/usr/bin/env python3
"""schema/keys.yml（キーの台帳の、道具が読む形）と schema/site.yml（語彙）から、JSON Schema（Draft-07）を作る
（DR-16：page.schema.json は site.yml とキーの台帳から作る。語彙を二か所に持たない）。

作るもの（keys.yml の各節の output）:
  schema/page.schema.json            ページの front matter（docs/<field>/<id>.md）
  schema/facts.schema.json           data/facts.yml（facts・features・names）
  schema/sources.schema.json         data/sources.yml と data/sources.d/<id>.yml（domains・sources）
  schema/outdated-advice.schema.json data/outdated-advice.yml（advice）
  schema/inspection.schema.json      data/inspection.yml（last）

使い方:
  uv run python tools/make_schema.py            作り直して、中身の変わったファイルだけを書く
  uv run python tools/make_schema.py --check    作り直して比べるだけ（書かない。CI と commit の前）
  uv run python tools/make_schema.py --root DIR DIR を根にする（DIR/schema/keys.yml・DIR/schema/site.yml。試験用）
終了コード: 0＝最新（--check）か書き終えた、1＝--check で古い・ないファイルがある、または keys.yml の書き方の誤り、
           2＝読めない（keys.yml・site.yml がない・壊れている）
出力: 1行ずつ「書いた: 」「最新: 」「古い: 」とファイル。「注: 」は、site.yml にない語彙（その語彙は enum にせず、
      空でない文字列かだけを見る）と、planning/design.md §3.3 の台帳の表と keys.yml の page のキーの食い違い
      （終了コードは変えない）。

作ったファイルは生成物なので手で直さない（直すのは keys.yml か site.yml）。commit し、CI で --check を流す
（design §8.4）。毎回変わる値（日時・ハッシュ）は入れない。front matter と data に当てるのは検査の層
（lib/schema.py の検査器か jsonschema）。
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.base import Fatal  # noqa: E402
from lib.ledger import Built, Ledger, build_all, load_ledger  # noqa: E402
from lib.site import load_site  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DESIGN = "planning/design.md"
LEDGER_SECTION_RE = re.compile(r"^### 3\.3[^\n]*\n(.*?)(?=^#{2,3} )", re.M | re.S)
BACKTICK_RE = re.compile(r"`([^`]+)`")


def design_keys(text: str) -> list[str] | None:
    """design §3.3 のキーの台帳の表の1列目にある `キー`（表がなければ None）。"""
    m = LEDGER_SECTION_RE.search(text)
    if not m:
        return None
    keys: list[str] = []
    for line in m.group(1).splitlines():
        if line.startswith("| `"):
            first = line.strip().strip("|").split("|")[0]
            keys += [k for k in BACKTICK_RE.findall(first) if k not in keys]
    return keys or None


def design_notes(root: Path, ledger: Ledger) -> list[str]:
    """design §3.3 の表と keys.yml の page のキーの食い違い（design.md がなければ見ない）。"""
    path = root / DESIGN
    page = ledger.section("page")
    if not path.exists() or page is None:
        return []
    try:
        keys = design_keys(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError):
        return [f"{DESIGN} が読めない（§3.3 の台帳と照らさない）"]
    if keys is None:
        return [f"{DESIGN} に §3.3 のキーの台帳の表が見つからない（照らさない）"]
    notes = []
    only_design = [k for k in keys if k not in page.keys]
    only_ledger = [k for k in page.keys if k not in keys]
    if only_design:
        notes.append(f"{DESIGN} §3.3 の台帳にあるのに keys.yml の page にない: {'・'.join(only_design)}")
    if only_ledger:
        notes.append(f"keys.yml の page にあるのに {DESIGN} §3.3 の台帳にない: {'・'.join(only_ledger)}")
    return notes


def build(root: Path) -> tuple[list[Built], list[str]]:
    """(作ったもの, 注)。読めなければ Fatal、keys.yml の誤りは ValueError。"""
    site = load_site(root)
    ledger = load_ledger(root)
    if ledger.errors:
        raise ValueError("\n".join(ledger.errors))
    built = build_all(ledger, site)
    notes = [n for b in built for n in b.notes] + design_notes(root, ledger)
    return built, list(dict.fromkeys(notes))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="make_schema.py", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="作り直して比べるだけ（書かない）")
    parser.add_argument("--root", metavar="DIR", help="根（既定はこのリポジトリ）")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve() if args.root else ROOT
    try:
        built, notes = build(root)
    except Fatal as e:
        print(f"作れない: {e}", file=sys.stderr)
        return 2
    except ValueError as e:
        for line in str(e).splitlines():
            print(f"台帳の誤り: {line}", file=sys.stderr)
        return 1
    stale = 0
    for b in built:
        path = root / b.path
        try:
            now = path.read_text(encoding="utf-8") if path.exists() else None
        except (OSError, UnicodeDecodeError):
            now = None
        if now == b.text:
            print(f"最新: {b.path}")
        elif args.check:
            stale += 1
            print(f"古い: {b.path}（{'ない' if now is None else '作り直すと変わる'}。uv run python tools/make_schema.py で作る）")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(b.text, encoding="utf-8")
            print(f"書いた: {b.path}")
    for n in notes:
        print(f"注: {n}")
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main())
