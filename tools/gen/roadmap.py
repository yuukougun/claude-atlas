"""ロードマップ（委任の段階別。design §7・§3.1 の4）。ロードマップのページ（roadmap）の手書きの節の中に置く。

  <!-- gen:begin roadmap -->   site.yml の levels の段ごとに、公開するページを前提の順で並べる

段の中の並び：同じ段の前提を先に（前提が先に来る並び。同じ並びの位置ではナビゲーションの順）。比例則（site.yml の
proportional_rule）の段で、守りの分野（guard_fields）でないページは、それが前提・関連（症状のページは routes の先も）に
持つ同じ段の守りの分野のページを手前に置く（前提の順とぶつかるときは前提を優先する）。level を持たない型は載せない。
"""
from __future__ import annotations

from lib.graph import reachable, topological_order

from .blocks import block
from .text import first_sentence, md_text


def level_order(gen, level: str) -> list:
    pages = [p for p in gen.published if p.level == level and p.type not in gen.site.types_without_level]
    ids = [p.id for p in pages]
    inside = set(ids)
    graph = {p.id: [r.target for r in p.prerequisites if r.target in inside and r.target != p.id] for p in pages}
    guards = set(gen.site.guard_fields)
    if level in gen.site.proportional_levels and guards:
        for p in pages:
            if p.field in guards:
                continue
            refs = [*p.prerequisites, *p.related, *(p.route_targets() if p.type == gen.symptom_type else [])]
            for ref in refs:
                g = gen.resolve(ref)
                if g is None or g.id not in inside or g.id == p.id or g.field not in guards or g.id in graph[p.id]:
                    continue
                if p.id in reachable(graph, [g.id]):       # 守りのページが、このページを前提にたどる（前提を優先）
                    continue
                graph[p.id].append(g.id)
    by_id = {p.id: p for p in pages}
    return [by_id[i] for i in topological_order(graph, ids)]


@block("roadmap", doc="ロードマップ：段（level）ごとに、公開するページを前提の順に（比例則の守りのページを手前に）")
def b_roadmap(ctx) -> str:
    gen = ctx.gen
    out: list[str] = []
    for i, level in enumerate(gen.site.levels):
        pages = level_order(gen, level)
        if not pages:
            continue
        out += [f"### {md_text(level)} {{#reading-order-{i + 1}}}", ""]
        for n, p in enumerate(pages, 1):
            s = first_sentence(p.summary)
            out.append(f"{n}. {gen.page_link(ctx.host, p)}（{md_text(gen.field_title(p.field))}）" + (f"：{md_text(s)}" if s else ""))
        out.append("")
    return "\n".join(out).rstrip("\n") or gen.text("empty", "（まだない）")

