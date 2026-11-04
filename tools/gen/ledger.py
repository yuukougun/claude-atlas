"""古くなった助言の台帳と、変更の記録（年表）。design §7・§9.1・DR-18、README の判断「台帳の行を指す形」。

  <!-- gen:begin ledger -->     台帳の行（data/outdated-advice.yml の advice。ファイルの順）。行ごとに見出し
                               「### 古い助言 {#<台帳の id>}」を置き、ほかのページは outdated-advice-ledger#<台帳の id> で指す
  <!-- gen:begin timeline -->   年表：data の names（名前の変更）と advice（変わった時期のある行）を、時期の順に

名前と画面の変更の行（advice の name）は、data/facts.yml の names の時期を引く（二か所に持たない。DR-18）。
status が確認済みでない names は年表に載せない。
"""
from __future__ import annotations

from lib.base import as_strings, partial_date_key

from .blocks import block
from .facts import sources_line
from .terms import period_text
from .text import md_text


def advice_changed(gen, item) -> dict | None:
    """台帳の行の変わった時期（name を指す行は names の changed）。"""
    if item.has("name"):
        data = gen.atlas.data
        n = data.names.get(item.text("name")) if data is not None else None
        return n.raw.get("changed") if n is not None else None
    ch = item.raw.get("changed")
    return ch if isinstance(ch, dict) else None


def _ledger_anchors(gen, page, param):
    data = gen.atlas.data
    return {a.id for a in data.entries("advice") if a.id} if data is not None else set()


@block("ledger", doc="古くなった助言の台帳：行ごとの見出し（anchor は台帳の id）と、今どうするか・時期・状態・原理・出典",
       anchors=_ledger_anchors)
def b_ledger(ctx) -> str:
    gen = ctx.gen
    data = gen.atlas.data
    items = data.entries("advice") if data is not None else []
    if not items:
        return gen.text("empty", "（まだない）")
    cfg = gen.config
    word = lambda key, default: cfg.text("ledger", key, default)   # noqa: E731
    out: list[str] = []
    for a in items:
        if not a.id:
            continue
        if a.text("name") and data.names.get(a.text("name")) is None:
            gen.note(f"{ctx.host}: 台帳の行「{a.id}」の name「{a.text('name')}」が data/facts.yml の names にない")
        out += [f"### {md_text(a.text('title') or a.id)} {{#{a.id}}}", ""]
        rows = [(word("now", "今どうするか"), md_text(a.text("now")))]
        period = period_text(gen, advice_changed(gen, a))
        if period:
            rows.append((word("changed", "変わった時期"), period))
        rows.append((word("status", "状態"), md_text(a.text("status"))))
        if a.strings("principle"):
            rows.append((word("principle", "どの原理の回避策だったか"), "・".join(md_text(x) for x in a.strings("principle"))))
        if a.text("why_then"):
            rows.append((word("why_then", "かつてなぜ正しかったか"), md_text(a.text("why_then"))))
        if a.text("how_to_find"):
            rows.append((word("how_to_find", "自分の設定や記事で見つける方法"), md_text(a.text("how_to_find"))))
        pages = gen.advice_pages.get(a.id, [])
        if pages:
            rows.append((word("pages", "関わるページ"), "・".join(gen.page_link(ctx.host, p) for p in pages)))
        if a.strings("sources"):
            rows.append((word("sources", "出典"), sources_line(gen, ctx.host, a.strings("sources"))))
        out += [f"- **{md_text(k)}**：{v}" for k, v in rows if v] + [""]
    return "\n".join(out).rstrip("\n")


@block("timeline", doc="変更の記録（年表）：名前の変更（names）と台帳の行（advice）を、変わった時期の順に")
def b_timeline(ctx) -> str:
    gen = ctx.gen
    data = gen.atlas.data
    if data is None:
        return gen.text("empty", "（まだない）")
    rows = []
    for n in data.entries("names"):
        ch = n.raw.get("changed")
        key = partial_date_key(ch.get("date")) if isinstance(ch, dict) else None
        if key is None or not gen.is_confirmed(n):
            continue
        olds = "・".join(md_text(x) for x in as_strings(n.raw.get("old")))
        text = f"{olds} → {md_text(n.text('current'))}"
        feat = gen.feature(n.text("feature")) if n.text("feature") else None
        main = gen.atlas.by_id.get(feat.text("page")) if feat is not None else None
        if main is not None:
            text += "（" + gen.page_link(ctx.host, main) + "）"
        rows.append((key, 0, n.id or "", period_text(gen, ch), text))
    ledger_page = next((pid for pid, names in gen.config.hosts().items() if "ledger" in names), "")
    host_page = gen.atlas.by_id.get(ledger_page)
    for a in data.entries("advice"):
        ch = advice_changed(gen, a)
        key = partial_date_key(ch.get("date")) if isinstance(ch, dict) else None
        if key is None or not a.id:
            continue
        text = md_text(a.text("title") or a.id)
        if host_page is not None:
            text = gen.page_link(ctx.host, host_page, anchor=a.id, text=text)
        rows.append((key, 1, a.id, period_text(gen, ch), text + f" → {md_text(a.text('now'))}"))
    if not rows:
        return gen.text("empty", "（まだない）")
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    return "\n".join(f"- {period}：{text}" for _, _, _, period, text in rows)
