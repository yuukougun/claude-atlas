"""逆引き辞典（design §7・DR-15）。逆引きのページ（reverse-index）の手書きの節の中に置く。

  <!-- gen:begin signs <sign の type> -->   公開するページの signs のうち、その type のもの（site.yml の sign_types）

- 同じ文（NFKC・大文字小文字・空白をそろえて比べる）の sign は1行に束ね、行き先を並べる。行き先には面と型の短い印
  （「アプリ・Claude Code、考え方」）を付ける
- 節の分け方は作る層の設定の reverse.group（type ごと）：
    symptom_chapter  症状辞典の章で分ける。症状のページはそのページの章。対処のページの困りごとは、そのページへ振り分ける
                     症状のページ（ナビゲーションの順の最初）の章。どの症状のページの routes にもないページは、
                     reverse.field_to_symptom_chapter で分野から章を選ぶ（なければ「そのほか」）
    field            行の最初の行き先の分野で分ける
    （なし）          節に分けない
- 束ねた行は、最初の行き先（ナビゲーションの順）で節を決める。節の中は、最初の行き先のナビゲーションの順
"""
from __future__ import annotations

from .blocks import block
from .text import md_text, norm_key


def chapter_order(gen) -> list[str]:
    out = []
    for p in gen.pages:
        if p.type == gen.symptom_type and p.chapter and p.chapter not in out:
            out.append(p.chapter)
    for ch in gen.config.field_to_symptom_chapter().values():
        if ch not in out:
            out.append(ch)
    return out


def group_of(gen, page, mode: str, order: list[str]) -> tuple[int, str]:
    other = gen.text("other_group", "そのほか")
    if mode == "symptom_chapter":
        if page.type == gen.symptom_type:
            ch = page.chapter
        else:
            routed = gen.routed_from.get(page.id) or []
            ch = routed[0].chapter if routed else gen.config.field_to_symptom_chapter().get(page.field, "")
        return (order.index(ch), ch) if ch in order else (len(order), other)
    if mode == "field":
        fields = gen.site.fields
        return (fields.index(page.field) if page.field in fields else len(fields), gen.field_title(page.field))
    return (0, "")


@block("signs", param="<sign の type>", doc="逆引き：その type の signs（同じ文は1行に束ね、面と型の印を付ける）")
def b_signs(ctx) -> str:
    gen = ctx.gen
    st = ctx.param
    if st not in (gen.site.vocab("sign_types") or []):
        gen.note(f"{ctx.host}: 生成の部分「{ctx.name}」の「{st}」は site.yml の sign_types にない（空にした）")
        return ""
    mode = gen.config.reverse_group(st)
    order = chapter_order(gen) if mode == "symptom_chapter" else []
    bundles: dict[str, dict] = {}
    for p in gen.published:
        for t, text in p.signs:
            if t != st or not text:
                continue
            b = bundles.setdefault(norm_key(text), {"text": text, "pages": []})
            if p not in b["pages"]:
                b["pages"].append(p)
    if not bundles:
        return gen.text("empty", "（まだない）")
    groups: dict[tuple[int, str], list[dict]] = {}
    for b in bundles.values():
        groups.setdefault(group_of(gen, b["pages"][0], mode, order), []).append(b)
    out: list[str] = []
    for key in sorted(groups):
        lines = []
        for b in groups[key]:
            dests = "・".join(gen.page_link(ctx.host, p) + gen.kind_marks(p) for p in b["pages"])
            lines.append(f"- {md_text(b['text'])} → {dests}")
        if key[1]:
            out += [f"### {md_text(key[1])}", ""]
        out += lines + [""]
    return "\n".join(out).rstrip("\n")
