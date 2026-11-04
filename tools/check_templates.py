#!/usr/bin/env python3
"""雛形の静的な検査（設計書 §8.6 の「雛形（静的）」の行・§8.7・DR-07。検査は tools/checks/templates.py）。

使い方:
  uv run python tools/check_templates.py                 snippets/ の雛形と .claude/settings.json を検査する
  uv run python tools/check_templates.py --page <id>     そのページの雛形（snippets/<id>/）に関わる指摘だけ（くり返し・
                                                         カンマ区切り可）
  uv run python tools/check_templates.py -q              警告を出さない
  uv run python tools/check_templates.py --list          検査の一覧を出す
  uv run python tools/check_templates.py --root DIR      DIR を根にして読む（試験用）
終了コード: 0＝エラーがない（警告だけなら 0）、1＝エラーがある、2＝検査できない（site.yml が読めない、--page の id の
           ページがない）
出力は tools/check_pages.py と同じ形（1件1行と、最後の行に件数）。

見るもの：JSON・YAML・front matter が読めるか、スキル（SKILL.md）とサブエージェント（agents/ の .md）の front matter の
必須の項目、settings の雛形（名前が settings.json で終わる JSON）と .claude/settings.json のキー（許す一覧
tools/checks/template_keys.yml と、あれば schema/claude-code-settings.schema.json）、期待（<名前>.expect.yaml）と結果
（verified.yaml）の形。実機の確認（使い捨てのフォルダで claude -p を動かす。design §8.7）はまだない（build-C.md §5）。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import Fatal  # noqa: E402
from checks import ERROR, TEMPLATES, WARNING, checks_epilog, format_issue, load_context, run_checks, summary_line  # noqa: E402
from checks.templates import settings_targets, snippet_files  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="check_templates.py", description=__doc__, epilog=checks_epilog(TEMPLATES),
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", metavar="DIR", help="置き場所の根（既定はこのリポジトリ）")
    parser.add_argument("--page", action="append", default=[], metavar="ID", help="そのページの雛形だけ（くり返し・カンマ区切り可）")
    parser.add_argument("-q", "--quiet", action="store_true", help="警告を出さない（件数だけを最後の行に出す）")
    parser.add_argument("--list", action="store_true", help="検査の一覧を出して終わる")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.list:
        print(checks_epilog(TEMPLATES))
        return 0
    root = Path(args.root).resolve() if args.root else ROOT
    try:
        ctx = load_context(root, TEMPLATES)
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
    read = f"雛形のファイル {len(snippet_files(ctx))}・settings {len(settings_targets(ctx))} を読んだ"
    scope = f"{'・'.join(wanted)} に関わる指摘：" if wanted else ""
    print(summary_line(errors, warnings, read, scope, args.quiet))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
