"""生成物の全体を作る（書かない）：ファイル → 中身の表と、消す古い生成物の一覧。gen_site.py が比べて書く。

作るもの：nav.yml・docs/<field>/index.md・docs/lists/*.md・docs/llms.txt・docs/assets/data/pages.json と graph.json・
docs/ のページ（docs/<field>/<id>.md と docs/index.md）の目印の中身。stubs/ の骨格のページは、--page で名指ししたときだけ
書く（公開しないので、全体の生成では触らない。draft にするときに docs/ へ移してから書く）。
消すもの：作らなくなった docs/lists/ の Markdown と、生成の印のある分野の入口（ページのなくなった分野）。
生成の印のない docs/<field>/index.md（手で書いたもの）は上書きせずに注意に出す（force のときは上書きする）。
"""
from __future__ import annotations

from pathlib import Path

from . import pages_out as out_
from .markers import apply_markers
from .text import GEN_MARK

DOCS = "docs"


def page_text(gen, page) -> str:
    """ページの目印の間を書き直した、ファイルの全体の文字。"""
    md = page.md
    return apply_markers(gen, md.text, md.body, md.markers, page, gen.doc_rel(page), page.url,
                         page.md.shown, page.body_line)


def top_text(gen):
    """docs/index.md（サイトのトップ。型を持たない手書きのページ）の目印の間を書き直したもの（なければ None）。"""
    docs = gen.atlas.docs
    for md in (docs.others if docs is not None else []):
        if md.shown == f"{DOCS}/index.md":
            return md, apply_markers(gen, md.text, md.body, md.markers, None, "index.md", "", md.shown, md.body_line)
    return None, None


def host_notes(gen) -> None:
    """作る層の設定の hosts（本体を生成するページ）に、目印がないもの（docs/ にあるページだけ見る）。"""
    missing = []
    for pid, names in gen.config.hosts().items():
        page = gen.atlas.by_id.get(pid)
        if page is None or not page.in_docs:
            continue
        have = {" ".join(m.arg.split()) for m in page.markers_of("gen")}
        missing += [f"{name}（{page.md.shown}）" for name in names if name not in have]
    if missing:
        gen.note(f"本体を生成するページに目印のない生成の部分 {len(missing)}: " + "、".join(missing))


def outputs(gen, force: bool = False) -> tuple[dict[Path, str], list[Path]]:
    root = gen.root
    docs = root / DOCS
    outs: dict[Path, str] = {}
    # 一覧
    made, lists = [], []
    for cfg in gen.config.list_pages():
        text = out_.list_page(gen, cfg)
        if text is not None:
            outs[docs / "lists" / cfg["file"]] = text
            made.append(cfg)
            lists.append((str(cfg.get("title") or cfg["file"]), cfg["file"]))
    if made:
        outs[docs / "lists" / "index.md"] = out_.lists_index(gen, made)
    outs[root / "nav.yml"] = out_.nav_yml(gen, lists)
    fields = out_.fields_with_pages(gen)
    for f in fields:
        outs[docs / f / "index.md"] = out_.entrance(gen, f)
    outs[docs / "llms.txt"] = out_.llms_txt(gen)
    outs[docs / out_.PAGES_JSON] = out_.pages_json(gen)
    outs[docs / out_.GRAPH_JSON] = out_.graph_json(gen)
    # 手書きのページの目印
    for p in (gen.atlas.docs.pages if gen.atlas.docs is not None else []):
        if p.in_docs:
            text = page_text(gen, p)
            if text != p.md.text:
                outs[root / p.md.shown] = text
    md, text = top_text(gen)
    if md is not None and text != md.text:
        outs[root / md.shown] = text
    host_notes(gen)
    # 手で書いた分野の入口は上書きしない
    for f in fields:
        path = docs / f / "index.md"
        if path.exists() and GEN_MARK not in path.read_text(encoding="utf-8") and not force:
            gen.note(f"{path.relative_to(root)} に生成の印がないので上書きしない（手で書いたものなら別の名前に移す。上書きは --force）")
            del outs[path]
    # 消す古い生成物
    stale: list[Path] = []
    lists_dir = docs / "lists"
    if lists_dir.is_dir():
        stale += [x for x in sorted(lists_dir.rglob("*.md")) if x not in outs]
    for f in gen.site.fields:
        path = docs / f / "index.md"
        if f not in fields and path.exists() and GEN_MARK in path.read_text(encoding="utf-8"):
            stale.append(path)
    return outs, stale


def page_outputs(gen, pid: str) -> dict[Path, str]:
    """--page：そのページ（docs/ か stubs/）の目印の間だけを書いたもの。"""
    page = gen.atlas.by_id.get(pid)
    text = page_text(gen, page)
    return {gen.root / page.md.shown: text} if text != page.md.text else {}
