#!/usr/bin/env python3
"""ページの front matter・本文の目印・data/ から、サイトの生成物と目印の中身を作る（設計書 §7・§8.3・§8.4）。

使い方:
  uv run python tools/gen_site.py                 作り直して、中身の変わったファイルだけを書く（古い生成物は消す）
  uv run python tools/gen_site.py --check         作り直して比べるだけ（書かない。差があれば終了コード 1。CI と commit の前）
  uv run python tools/gen_site.py --check --diff  差の中身も出す
  uv run python tools/gen_site.py --page <id>     そのページの目印の間だけを書く（執筆の担当が自分のページで使う。
                                                  docs/ か stubs/ のページ。ほかの生成物は書かない）
  uv run python tools/gen_site.py --page <id> --check   そのページだけを比べる
  uv run python tools/gen_site.py --list-blocks   手書きのページに置ける生成の部分の名前の一覧
  uv run python tools/gen_site.py --root DIR      DIR を根にする（試験用。DIR/docs・DIR/stubs・DIR/data・DIR/schema/site.yml・
                                                  DIR/mkdocs.yml、作る層の設定は DIR/tools/gen/config.yml かこの道具の隣）
  uv run python tools/gen_site.py --force         生成の印のない docs/<field>/index.md も上書きする

書くもの（tools/gen/__init__.py と各部品の冒頭に詳しく書いた）:
  nav.yml                         ナビゲーション（公開するページだけ）・exclude_docs（docs/ にあって公開しないページ）・extra.ca
  docs/<field>/index.md           分野の入口（公開するページのある分野だけ）
  docs/lists/                     一覧（レベル別・面別・原理別・場面別。作る層の設定の lists）
  docs/llms.txt                   1ページ1行
  docs/assets/data/pages.json     公開するページの値（期限の日を含む）
  docs/assets/data/graph.json     知識マップ（前提と症状の振り分け）
  docs/ のページの目印の間         gen・fact・link の目印（参考の節とページ下部は、目印がなければ末尾に足す）
終了コード: 0＝最新（--check）か書き終えた、1＝--check で古い・ないファイルがある、2＝読めない（site.yml・mkdocs.yml・
           作る層の設定がない・壊れている、--page の id のページがない）
出力の「注意」は、生成のときに分かった誤り（ない id・閉じていない目印・知らない生成の部分など）で、終了コードは変えない
（誤りとして止めるのは検査の層の check_pages.py）。毎回変わる値（日時・ハッシュ）は生成物に入れない。
生成物は手で直さない（.claude/settings.json の deny が Edit と Write を止める。道具が書くのはよい）。
"""
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gen import REGISTRY, load_gen, outputs, page_outputs  # noqa: E402
from lib.base import Fatal  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def rel(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def list_blocks() -> None:
    print("手書きのページに <!-- gen:begin 名前 --> と <!-- gen:end 名前 --> を置くと、その間を gen_site.py が書く。")
    print("種類の block は目印をそれぞれ1行に、inline は文の中に置く。本体を生成するページは tools/gen/config.yml の hosts。")
    for name, b in sorted(REGISTRY.items()):
        shown = f"{name} {b.param}" if b.param else name
        print(f"  {shown:40s} {b.kind:6s} {b.doc}")
    print("ほかの目印：<!-- fact:begin <数値の id> -->（表は <id> <行> <列>）と <!-- link:begin <id>[#<anchor>] -->。"
          "どちらも <!-- fact:end --> と <!-- link:end --> で閉じる")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="作り直して比べるだけ（書かない）")
    parser.add_argument("--diff", action="store_true", help="--check で差の中身も出す")
    parser.add_argument("--page", metavar="ID", help="そのページの目印の間だけを書く")
    parser.add_argument("--root", type=Path, default=ROOT, help="根（既定はこのリポジトリ）")
    parser.add_argument("--force", action="store_true", help="生成の印のない docs/<field>/index.md も上書きする")
    parser.add_argument("--list-blocks", action="store_true", help="生成の部分の名前の一覧")
    args = parser.parse_args(argv)
    if args.list_blocks:
        list_blocks()
        return 0
    root = args.root.resolve()
    try:
        gen = load_gen(root)
        if args.page:
            if gen.atlas.by_id.get(args.page) is None:
                raise Fatal(f"--page の「{args.page}」のページが docs/ にも stubs/ にもない")
            outs, stale = page_outputs(gen, args.page), []
        else:
            outs, stale = outputs(gen, args.force)
    except Fatal as e:
        print(f"読めない: {e}", file=sys.stderr)
        return 2
    changed = []
    for path, text in outs.items():
        old = path.read_text(encoding="utf-8") if path.exists() else None
        if old != text:
            changed.append((path, old, text))
    n_docs = sum(1 for p in gen.pages if p.in_docs)
    print(f"公開するページ {len(gen.published)}（docs/ のページ {n_docs}・stubs/ のページ {len(gen.pages) - n_docs}・"
          f"公開から外した試作のページ {len(gen.config.held_back)}）")
    for n in gen.notes:
        print(f"注意: {n}")
    if args.check:
        for path, old, text in changed:
            print(("作られる: " if old is None else "古い: ") + rel(root, path))
            if args.diff and old is not None:
                d = difflib.unified_diff(old.split("\n"), text.split("\n"), rel(root, path), rel(root, path) + "（作り直し）",
                                         lineterm="", n=1)
                for k, line in enumerate(d):
                    if k >= 80:
                        print("    …")
                        break
                    print("    " + line)
        for path in stale:
            print("消える: " + rel(root, path))
        if changed or stale:
            print(f"生成物が古い：{len(changed) + len(stale)} ファイル。uv run python tools/gen_site.py で作り直して commit する")
            return 1
        print("生成物は最新")
        return 0
    for path, _, text in changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    for path in stale:
        path.unlink()
    print(f"書いた: {len(changed)} ファイル・消した: {len(stale)} ファイル")
    for path, old, _ in changed:
        print(("  作った " if old is None else "  変えた ") + rel(root, path))
    for path in stale:
        print("  消した " + rel(root, path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
