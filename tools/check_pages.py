#!/usr/bin/env python3
"""ページ（docs/ と stubs/ の front matter と本文）と data/ を検査する（設計書 §8.6 の front matter・参照・数値と出典・
確認日の行。§8.3 の検査の層 tools/checks/ の入口）。

使い方:
  uv run python tools/check_pages.py                  全ページと data/ を検査して、エラーと警告を1件1行で出す
  uv run python tools/check_pages.py --page <id>      そのページに関わる指摘だけを出す（くり返し・カンマ区切り可。読むのと
                                                      参照の解決は全体で行う。担当が自分のページを確かめるとき）
  uv run python tools/check_pages.py --catalog        目次（planning/catalog/）に、前提と関連の規則を当てる（同じ規則の
                                                      関数。目次だけの規則は tools/check_catalog.py。骨格の後は使わない）
  uv run python tools/check_pages.py --today 2026-12-01   確認日の期限を数える日（既定は今日）
  uv run python tools/check_pages.py -q               警告を出さない（件数だけを最後の行に出す）
  uv run python tools/check_pages.py --list           検査の一覧を出す
  uv run python tools/check_pages.py --root DIR       DIR を根にして読む（試験用）
終了コード: 0＝エラーがない（警告だけなら 0）、1＝エラーがある（--page のときは、そのページに関わるエラーで決める）、
           2＝検査できない（site.yml が読めない、--page の id のページがない）

出力: 1件1行で「エラー: <ファイル>:<行>: <ページの id>: [<検査>] <内容>」（警告は「警告: 」で始まる）。
      ページに関わらない指摘は id を「-」にする。最後の行に件数を出す。

読むもの（読む層 tools/lib/ を通す）:
  schema/site.yml・schema/*.schema.json   語彙と形（schema は tools/make_schema.py の生成物）
  docs/<field>/<id>.md・stubs/<field>/<id>.md   ページ（stub は stubs/、draft 以上は docs/。design §8.5）
  docs/index.md                           サイトのトップ（手書きのリンクだけを見る）
  data/                                   facts・sources（と sources.d/）・outdated-advice・inspection
  nav.yml                                 nav と exclude_docs（exclude_docs に当たる docs/ のページを未公開に数える）
  .claude/settings.json                   deny（AI の利用を断るドメインが入っているか）
  planning/catalog/                       章の正本（chapters）と、--catalog のときのページ
生成物（docs/<field>/index.md・docs/lists/・docs/llms.txt・docs/assets/data/）は見ない（tools/gen_site.py --check が見る）。
"""
from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import Fatal  # noqa: E402
from checks import (CATALOG, ERROR, FRONT_MATTER, WARNING, checks_epilog, checks_for, format_issue,  # noqa: E402
                    load_context, run_checks, summary_line)

ROOT = Path(__file__).resolve().parent.parent


def build_parser() -> argparse.ArgumentParser:
    epilog = checks_epilog(FRONT_MATTER) + "\n\n--catalog のとき（前提と関連の規則）:\n" + "\n".join(
        f"  [{c.name}]" for c in checks_for(CATALOG))
    parser = argparse.ArgumentParser(prog="check_pages.py", description=__doc__, epilog=epilog,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", metavar="DIR", help="置き場所の根（既定はこのリポジトリ）")
    parser.add_argument("--page", action="append", default=[], metavar="ID",
                        help="そのページに関わる指摘だけを出す（くり返し・カンマ区切り可）")
    parser.add_argument("--catalog", action="store_true", help="目次に、前提と関連の規則を当てる")
    parser.add_argument("--today", type=datetime.date.fromisoformat, metavar="YYYY-MM-DD",
                        help="確認日の期限を数える日（既定は今日）")
    parser.add_argument("-q", "--quiet", action="store_true", help="警告を出さない（件数だけを最後の行に出す）")
    parser.add_argument("--list", action="store_true", help="検査の一覧を出して終わる")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    target = CATALOG if args.catalog else FRONT_MATTER
    if args.list:
        print(checks_epilog(target))
        return 0
    root = Path(args.root).resolve() if args.root else ROOT
    try:
        ctx = load_context(root, target, today=args.today)
    except Fatal as e:
        print(f"検査できない: {e}", file=sys.stderr)
        return 2
    wanted = [x.strip() for v in args.page for x in v.split(",") if x.strip()]
    unknown = [x for x in wanted if x not in ctx.atlas.by_id]
    if unknown:
        print(f"検査できない: --page の「{'」「'.join(unknown)}」のページがない", file=sys.stderr)
        return 2
    issues = run_checks(ctx)
    if wanted:
        issues = [i for i in issues if set(wanted) & i.pages]
    errors = [i for i in issues if i.severity == ERROR]
    warnings = [i for i in issues if i.severity == WARNING]
    for i in errors + ([] if args.quiet else warnings):
        print(format_issue(i))
    if target == CATALOG:
        read = f"目次のページ {len(ctx.pages)} を読んだ"
    else:
        n_docs = sum(1 for p in ctx.pages if p.in_docs)
        n_data = sum(len(v) for v in ctx.data.items.values()) if ctx.data is not None else 0
        read = f"docs/ のページ {n_docs}・stubs/ のページ {len(ctx.pages) - n_docs}・data の項目 {n_data} を読んだ"
    scope = f"{'・'.join(wanted)} に関わる指摘：" if wanted else ""
    print(summary_line(errors, warnings, read, scope, args.quiet))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
