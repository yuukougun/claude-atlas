"""どのページにも置く生成の部分：参考の節（references）とページ下部（page-links）。design §8.4・§8.5・DR-01。

  <!-- gen:begin references -->  見出し「参考」{#references}（手で書いた同じ anchor の見出しがあれば書かない）と、
                                 front matter の sources の出典（data の sources）
  <!-- gen:begin page-links -->  前提・次に読む・関連（未公開のページは「題名（準備中）」の平文。書かないページは載せない）

どちらも、ページに目印がなければ gen_site.py が本文の末尾に足す（markers.py）。参考の節は sources があるときだけ。
ページ下部は <div class="ca-page-links" markdown> で囲む（見た目は V のテンプレートと CSS が付ける）。
  前提     prerequisites の順
  次に読む  症状のページは routes の先（原因の並び＝診断の順。routes の表と同じ）、続けてこのページを前提にするページ（公開しているものを先に、
           ナビゲーションの順）。page_links.next_max まで（超えた分は「ほか N ページ」）
  関連     related の順。前提と次に読むに出したページは重ねない（節を指す関連は出す）
"""
from __future__ import annotations

from lib.base import Ref

from .blocks import block
from .facts import sources_line
from .text import md_text


def _ref_anchor_text(gen, host: str, refs: list[Ref]) -> list[str]:
    return [gen.ref_link(host, r) for r in refs if not gen.is_unplanned_ref(r)]


def _references_anchors(gen, page, param):
    return {gen.config.text("references", "anchor", "references")} if page.sources else set()


@block("references", doc="参考の節：見出しと、front matter の sources の出典（data/sources.yml と sources.d/）",
       anchors=_references_anchors)
def b_references(ctx) -> str:
    gen, page = ctx.gen, ctx.page
    if page is None or not page.sources:
        return ""
    data = gen.atlas.data
    cfg = gen.config
    heading = cfg.text("references", "heading", "参考")
    anchor = cfg.text("references", "anchor", "references")
    checked_word = cfg.text("references", "checked", "確認日")
    archive_word = cfg.text("references", "archive", "写し")
    langs = cfg.labels("langs")
    # 見出しを手で書いたページ（目印の前に「## 参考 {#references}」がある）では、見出しを重ねない
    lines = [] if anchor in gen.hand_anchors(page) else [f"## {md_text(heading)} {{#{anchor}}}", ""]
    for sid in dict.fromkeys(page.sources):
        src = data.sources.get(sid) if data is not None else None
        if src is None:
            gen.note(f"{ctx.host}: 出典「{sid}」が data/sources.yml・data/sources.d/ にない（id のまま書いた）")
            lines.append(f"- {md_text(sid)}")
            continue
        parts = [md_text(src.text("publisher"))]
        lang = src.text("lang")
        if lang and lang != "ja":
            parts.append(md_text(langs.get(lang, lang)))
        if src.text("checked"):
            parts.append(f"{md_text(checked_word)} {src.text('checked')}")
        if src.text("archive"):
            parts.append(f"[{md_text(archive_word)}]({src.text('archive')})")
        meta = "・".join(x for x in parts if x)
        lines.append(f"- [{md_text(src.text('title') or sid)}]({src.text('url')})" + (f"：{meta}" if meta else ""))
    return "\n".join(lines)


def next_pages(gen, page) -> list:
    """次に読むページ（症状のページは routes の先を先に）。重ねない。"""
    out: list = []
    seen = {page.id, *(r.target for r in page.prerequisites)}
    if page.type == gen.symptom_type:
        rank = {c: i for i, c in enumerate(gen.site.causes)}
        for route in sorted(page.routes, key=lambda r: (rank.get(r.cause, len(rank)), r.index)):
            for r in route.to:
                p = gen.resolve(r)
                if p is not None and p.id not in seen and not gen.is_unplanned(p):
                    out.append(p)
                    seen.add(p.id)
    deps = [p for p in gen.dependents.get(page.id, []) if p.id not in seen and not gen.is_unplanned(p)]
    deps.sort(key=lambda p: (not gen.is_pub(p), gen.rank.get(p.id, 0)))
    out += deps
    return out


@block("page-links", doc="ページ下部：前提・次に読む・関連（未公開のページは「題名（準備中）」）")
def b_page_links(ctx) -> str:
    gen, page = ctx.gen, ctx.page
    if page is None:
        return ""
    cfg = gen.config
    host = ctx.host
    rows = []
    pre = _ref_anchor_text(gen, host, page.prerequisites)
    rows.append((cfg.text("page_links", "prerequisites", "前提"), pre or [gen.text("none", "なし")]))
    nxt = next_pages(gen, page)
    cap = cfg.number("page_links", "next_max", 8)
    items = [gen.page_link(host, p) for p in nxt[:cap]]
    if len(nxt) > cap:
        items.append(gen.text("more", "ほか {n} ページ").replace("{n}", str(len(nxt) - cap)))
    if items:
        rows.append((cfg.text("page_links", "next", "次に読む"), items))
    shown = {r.target for r in page.prerequisites} | {p.id for p in nxt[:cap]}
    rel, seen = [], set()
    for r in page.related:
        key = r.raw.strip()
        if key in seen or (r.anchor is None and r.target in shown) or gen.is_unplanned_ref(r):
            continue
        seen.add(key)
        rel.append(gen.ref_link(host, r))
    if rel:
        rows.append((cfg.text("page_links", "related", "関連"), rel))
    out = ['<div class="ca-page-links" markdown>', ""]
    for label, links in rows:
        out += [f"**{md_text(label)}**", ""] + [f"- {x}" for x in links] + [""]
    out.append("</div>")
    return "\n".join(out)


@block("graph", doc="知識マップの図を描く場所（JS が data-graph の graph.json を読む。knowledge-map のページ）")
def b_graph(ctx) -> str:
    from .text import url_prefix
    return f'<div class="ca-graph" data-graph="{url_prefix(ctx.url)}assets/data/graph.json"></div>'


__all__ = ["next_pages", "sources_line"]
