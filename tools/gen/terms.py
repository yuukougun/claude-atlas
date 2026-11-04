"""用語索引と旧名の対応（design §7・DR-15・DR-18）。用語索引のページ（term-index）の手書きの節の中に置く。

  <!-- gen:begin terms kana -->    かなで始まる語（五十音の行ごと）と、漢字・記号で始まる語（最初の字の順）
  <!-- gen:begin terms latin -->   英数字で始まる語（先頭に跳び先の行、0〜9 と A〜Z ごと）
  <!-- gen:begin terms old -->     旧名 → 今の名前（data/facts.yml の names。変わった時期と、機能の主のページ）

語は、公開するページの title・nav_title・aliases と、data の features の title（その機能の主のページ＝page へ。status が
確認済みの機能だけ）。
同じ語（NFKC・大文字小文字・空白をそろえて比べる）は1行にまとめ、機能の主のページを先に、続けて題名のページ、
ほかのページをナビゲーションの順に、短い印（型）付きで並べる。ほかのページの題名と同じ別名は外す（DR-15）。
かなの行の分け方と並べ方は、カタカナをひらがなにし長音を除いた字の順（読みの辞書は持たないので、漢字で始まる語は
最初の字の順に並べる）。
"""
from __future__ import annotations

import unicodedata

from lib.base import as_strings

from .blocks import block
from .text import md_text, norm_key

KANA_ROWS = [("a", "あ行", 0x3041, 0x304A), ("ka", "か行", 0x304B, 0x3054), ("sa", "さ行", 0x3055, 0x305E),
             ("ta", "た行", 0x305F, 0x3069), ("na", "な行", 0x306A, 0x306E), ("ha", "は行", 0x306F, 0x307D),
             ("ma", "ま行", 0x307E, 0x3082), ("ya", "や行", 0x3083, 0x3088), ("ra", "ら行", 0x3089, 0x308D),
             ("wa", "わ行", 0x308E, 0x309F)]


def kana_key(s: str) -> str:
    """並べ替えの鍵：NFKC、カタカナをひらがなに、長音を除く。"""
    out = []
    for ch in unicodedata.normalize("NFKC", s):
        o = ord(ch)
        if 0x30A1 <= o <= 0x30F6:
            ch = chr(o - 0x60)
        if ch != "ー":
            out.append(ch)
    return "".join(out)


def term_class(s: str) -> str:
    c = unicodedata.normalize("NFKC", s.strip())[:1]
    if c.isascii() and c.isalnum():
        return "latin"
    k = kana_key(c)[:1] if c else ""
    if k and 0x3041 <= ord(k) <= 0x309F:
        return "kana"
    return "other"


def collect_terms(gen) -> list[dict]:
    """語の一覧：{display, key, pages: [(page, how)]}。how は main（機能の主のページ）・title・alias。"""
    entries: dict[str, dict] = {}

    def add(word: str, page, how: str) -> None:
        key = norm_key(word)
        if not key:
            return
        e = entries.setdefault(key, {"display": " ".join(word.split()), "key": key, "pages": []})
        for i, (p, h) in enumerate(e["pages"]):
            if p is page:
                if RANK[how] < RANK[h]:
                    e["pages"][i] = (p, how)
                return
        e["pages"].append((page, how))

    for p in gen.published:
        add(p.title, p, "title")
        if p.text("nav_title"):
            add(p.text("nav_title"), p, "title")
        for a in p.aliases:
            add(a, p, "alias")
    data = gen.atlas.data
    for f in data.entries("features") if data is not None else []:
        main = gen.atlas.by_id.get(f.text("page"))
        if main is not None and gen.is_pub(main) and f.text("title") and gen.is_confirmed(f):
            add(f.text("title"), main, "main")
    out = []
    for e in entries.values():
        if any(h == "title" for _, h in e["pages"]):
            e["pages"] = [(p, h) for p, h in e["pages"] if h != "alias"]    # ほかのページの題名と同じ別名は外す
        e["pages"].sort(key=lambda x: (RANK[x[1]], gen.rank.get(x[0].id, 0)))
        title_display = next((w for w in [x[0].title for x in e["pages"] if x[1] == "title"] if norm_key(w) == e["key"]), None)
        if title_display:
            e["display"] = title_display
        out.append(e)
    return out


RANK = {"main": 0, "title": 1, "alias": 2}


def term_line(gen, host: str, e: dict) -> str:
    pages = e["pages"]
    if len(pages) == 1 and pages[0][1] == "title" and norm_key(pages[0][0].title) == e["key"]:
        return f"- {gen.page_link(host, pages[0][0])}"
    links = []
    for i, (p, how) in enumerate(pages):
        mark = "" if i == 0 else (f"（{gen.label('types', p.type)}）" if p.type else "")
        links.append(gen.page_link(host, p) + mark)
    return f"- {md_text(e['display'])} → " + "、".join(links)


@block("terms", param="kana・latin・old のどれか", doc="用語索引：かな（と漢字・記号）・英数字で始まる語、旧名と今の名前")
def b_terms(ctx) -> str:
    gen = ctx.gen
    part = ctx.param
    if part == "old":
        return old_names(ctx)
    if part not in ("kana", "latin"):
        gen.note(f"{ctx.host}: 生成の部分「{ctx.name}」の引数は kana・latin・old のどれか（空にした）")
        return ""
    terms = [e for e in collect_terms(gen) if (term_class(e["display"]) == "latin") == (part == "latin")]
    if not terms:
        return gen.text("empty", "（まだない）")
    out: list[str] = []
    if part == "latin":
        terms.sort(key=lambda e: (e["key"], e["display"]))
        groups: dict[str, list] = {}
        for e in terms:
            c = e["key"][:1]
            groups.setdefault("digits" if c.isdigit() else c, []).append(e)
        label = {k: "0〜9" if k == "digits" else k.upper() for k in groups}
        out.append("・".join(f"[{label[k]}](#terms-latin-{k})" for k in groups))
        for k, es in groups.items():
            out += ["", f"### {label[k]} {{#terms-latin-{k}}}", ""] + [term_line(gen, ctx.host, e) for e in es]
        return "\n".join(out)
    kana = sorted((e for e in terms if term_class(e["display"]) == "kana"), key=lambda e: (kana_key(e["display"]), e["display"]))
    other = sorted((e for e in terms if term_class(e["display"]) == "other"),
                   key=lambda e: (unicodedata.normalize("NFKC", e["display"]), e["display"]))
    rows: dict[str, list] = {}
    names = {}
    for e in kana:
        o = ord(kana_key(e["display"])[:1])
        key, label = next(((k, lab) for k, lab, lo, hi in KANA_ROWS if lo <= o <= hi), ("wa", "わ行"))
        rows.setdefault(key, []).append(e)
        names[key] = label
    for key, *_ in KANA_ROWS:
        if key in rows:
            out += [f"### {names[key]} {{#terms-{key}}}", ""] + [term_line(gen, ctx.host, e) for e in rows[key]] + [""]
    if other:
        heading = gen.config.text("terms", "other_heading", "漢字・記号で始まる語")
        out += [f"### {md_text(heading)} {{#terms-other}}", ""] + [term_line(gen, ctx.host, e) for e in other] + [""]
    return "\n".join(out).rstrip("\n")


def period_text(gen, changed: dict) -> str:
    """変わった時期（date・until・approx・version）を文字にする：「2026-10 ごろ・Claude Code 2.1.300」「2026-09〜2026-10」。"""
    if not isinstance(changed, dict):
        return ""
    date = str(changed.get("date") or "")
    until = str(changed.get("until") or "")
    text = date + (f"〜{until}" if until else "")
    if changed.get("approx") is True and text:
        text += " " + gen.text("approx", "ごろ")
    ver = str(changed.get("version") or "")
    if ver:
        text += ("・" if text else "") + f"Claude Code {ver}"
    return md_text(text)


def old_names(ctx) -> str:
    gen = ctx.gen
    data = gen.atlas.data
    items = []
    for n in data.entries("names") if data is not None else []:
        for old in as_strings(n.raw.get("old")):
            items.append((norm_key(old), old, n))
    if not items:
        return gen.text("empty", "（まだない）")
    out = []
    for _, old, n in sorted(items, key=lambda x: (x[0], x[1])):
        if not gen.is_confirmed(n):
            continue
        line = f"- {md_text(old)} → {md_text(n.text('current'))}"
        period = period_text(gen, n.raw.get("changed")) or gen.text("period_unknown", "不明")   # changed.date を省いた名前（時期が分からない）
        line += f"（{period}）"
        feat = gen.feature(n.text("feature")) if n.text("feature") else None
        main = gen.atlas.by_id.get(feat.text("page")) if feat is not None else None
        if main is not None:
            line += "：" + gen.page_link(ctx.host, main)
        out.append(line)
    return "\n".join(out) or gen.text("empty", "（まだない）")
