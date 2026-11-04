"""症状のページの routes から書くもの（design §8.3・§8.4・DR-02）。

  <!-- gen:begin routes -->  症状のページの診断の節：原因ごとの振り分け先の表（原因は site.yml の prevents・pitfalls の
                            並び＝安く確かめられる順。振り分け先は routes の to の順＝近い順で、セルの中で1つずつ改行（<br>）。
                            未公開は「題名（準備中）」）
  <!-- gen:begin causes -->  失敗の二つの軸のページ（six-causes）：原因ごとに、その原因へ振り分ける公開の症状のページ
"""
from __future__ import annotations

from .blocks import block
from .text import md_text, table

AXES = ("prevents", "pitfalls")     # site.yml のキー（routes の cause の語彙。lib.site.Site.causes と同じ）


def cause_rank(gen) -> dict[str, int]:
    return {c: i for i, c in enumerate(gen.site.causes)}


@block("routes", doc="症状のページの診断の節：原因ごとの振り分け先の表（front matter の routes から）")
def b_routes(ctx) -> str:
    gen, page = ctx.gen, ctx.page
    if page is None:
        return ""
    routes = page.routes
    if not routes:
        if page.type != gen.symptom_type:
            gen.note(f"{ctx.host}: 生成の部分 routes は症状のページ（type: {gen.symptom_type}）に置く")
        return ""
    rank = cause_rank(gen)
    ordered = sorted(routes, key=lambda r: (rank.get(r.cause, len(rank)), r.index))
    cfg = gen.config
    rows = []
    for r in ordered:
        links = [gen.ref_link(ctx.host, ref, table=True) for ref in r.to]
        rows.append([md_text(r.cause, True), "<br>".join(links) or "—"])   # 行き先は1つずつセルの中で改行する
    return table([md_text(cfg.text("routes", "cause", "原因"), True), md_text(cfg.text("routes", "to", "対処のページ（近い順）"), True)],
                 rows)


@block("causes", doc="症状の原因別の表：原因ごとに、その原因へ振り分ける公開の症状のページ（症状のページの routes から）")
def b_causes(ctx) -> str:
    gen = ctx.gen
    cfg = gen.config
    by_cause: dict[str, list] = {}
    for p in gen.published:
        if p.type != gen.symptom_type:
            continue
        for c in dict.fromkeys(r.cause for r in p.routes):
            by_cause.setdefault(c, []).append(p)
    rows = []
    for axis in AXES:
        for c in gen.site.vocab(axis) or []:
            pages = by_cause.get(c, [])
            links = "・".join(gen.page_link(ctx.host, p, table=True) for p in pages) or "—"
            rows.append([md_text(gen.label("cause_axes", axis), True), md_text(c, True), links])
    if not rows:
        return gen.text("empty", "（まだない）")
    head = [cfg.text("routes", "axis", "軸"), cfg.text("routes", "cause", "原因"), cfg.text("routes", "symptoms", "症状のページ")]
    return table([md_text(h, True) for h in head], rows)
