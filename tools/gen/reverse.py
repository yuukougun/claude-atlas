"""逆引き辞典（design §7・DR-15）。逆引きのページ（reverse-index）の手書きの節の中に置く。

  <!-- gen:begin signs <sign の type> -->   公開するページの signs のうち、その type のもの（site.yml の sign_types）

- 同じ文（NFKC・大文字小文字・空白をそろえて比べる）の sign は1つにし、行き先を並べる。行き先は ページ か ページ#anchor
  （sign の任意の anchor。そのページの見出しにあるとき。ないときはページへのリンクにして注意に出す）。行き先には面と型の
  短い印（「アプリ・Claude Code、考え方」）を付ける
- 行き先の並びが同じ文は1行に束ね、文を改行（<br>）で並べ、最後の改行の後に「→ 行き先」を置く（文の並びは、ページの
  signs の並び＝最初に出た順）。anchor が違う行き先は別の行
- 節の分け方は作る層の設定の reverse.group（type ごと）：
    symptom_chapter  症状辞典の章で分ける。症状のページはそのページの章。対処のページの困りごとは、そのページへ振り分ける
                     症状のページ（ナビゲーションの順の最初）の章。どの症状のページの routes にもないページは、
                     reverse.field_to_symptom_chapter で分野から章を選ぶ（なければ「そのほか」）
    field            行の最初の行き先の分野で分ける
    （なし）          節に分けない
- 束ねた行は、最初の行き先（ナビゲーションの順）で節を決める。節の中は、最初の行き先のナビゲーションの順
  （同じページの行は続け、その中は文が最初に出た順）
"""
from __future__ import annotations

from .blocks import block
from .text import md_text, norm_key

SEPARATOR = "<br>"      # 束ねた行で読者の言葉を分ける区切り（改行）


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
    index = {p.id: i for i, p in enumerate(gen.published)}
    # 読者の言葉ごとに行き先（ページ, anchor）を集める。同じ言葉は1つにし、行き先を並べる
    words: dict[str, dict] = {}
    for p in gen.published:
        for t, text, anchor in p.sign_items:
            if t != st or not text:
                continue
            w = words.setdefault(norm_key(text), {"text": text, "seq": len(words), "dests": []})
            if (p, anchor) not in w["dests"]:
                w["dests"].append((p, anchor))
    if not words:
        return gen.text("empty", "（まだない）")
    # 行き先の並びが同じ言葉を1行に束ねる
    rows: dict[tuple, dict] = {}
    for w in words.values():
        key = tuple((p.id, a) for p, a in w["dests"])
        r = rows.setdefault(key, {"texts": [], "dests": w["dests"], "seq": w["seq"]})
        r["texts"].append(w["text"])
    groups: dict[tuple[int, str], list[dict]] = {}
    for r in rows.values():
        groups.setdefault(group_of(gen, r["dests"][0][0], mode, order), []).append(r)
    out: list[str] = []
    for key in sorted(groups):
        lines = []
        for r in sorted(groups[key], key=lambda r: (index[r["dests"][0][0].id], r["seq"])):
            dests = "・".join(gen.page_link(ctx.host, p, a or None) + gen.kind_marks(p) for p, a in r["dests"])
            texts = SEPARATOR.join(md_text(t) for t in r["texts"])
            # 2つ以上の言葉を束ねた行は、矢印を最後の言葉の続きでなく、行き先の頭に置く（全部の言葉の行き先と読める）
            lines.append(f"- {texts}{SEPARATOR if len(r['texts']) > 1 else ' '}→ {dests}")
        if key[1]:
            out += [f"### {md_text(key[1])}", ""]
        out += lines + [""]
    return "\n".join(out).rstrip("\n")
