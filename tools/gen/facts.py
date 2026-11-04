"""数値ファイル（data/facts.yml）から書くもの（design §6.7・§8.4・§9.1）。

  <!-- fact:begin <id> --><!-- fact:end -->                 値・決まった文・確認日（facts の value）
  <!-- fact:begin <id> <行> <列> --><!-- fact:end -->       面やモデルで違う値（facts の table）の1つのセル
  <!-- gen:begin fact-table <id> -->                         facts の table の全体を表にする
  <!-- gen:begin feature <属性> -->（文の中）               ページの tracks の最初の機能の属性（強制力など）
  <!-- gen:begin feature <機能の id>/<属性> -->（文の中）    指定した機能の属性
  <!-- gen:begin compare [<列> …] -->                        ページの tracks の機能の比較の表。列は属性の id（enforcement）か
                                                            表示の名前（強制力）か 確認日。省くと値のある属性だけ（並びは作る層の
                                                            設定の labels.feature_keys）。全行が同じ値の列は表から省き、表の下に
                                                            「すべて共通：…」の1行で出す

決まった文（sentence）は {value}・{unit}・{checked} を埋める。sentence がなければ「{value} {unit}」、どちらも確認日を
含まなければ「（{checked} 時点）」を足す（design §6.7：数値と決まった文と確認日を道具が書く）。
status が確認済み（作る層の設定の roles.fact_confirmed）でない項目は、値を書かずに「未確認」とだけ書く
（一次資料で確かめていない値を出さない）。
"""
from __future__ import annotations

import re

from lib.base import as_strings, as_text

from .blocks import block
from .text import md_text, table

TEMPLATE_RE = re.compile(r"\{(value|unit|checked)\}")
FEATURE_KEYS_DEFAULT = ("surfaces", "maturity", "enforcement", "load_timing", "context_cost", "survives_compaction", "since")


def value_text(gen, v, key: str | None = None, table_cell: bool = False) -> str:
    """data の値を表示の文字にする（真偽と null は作る層の設定の言葉。リストは「・」でつなぐ）。"""
    if isinstance(v, dict):
        out = value_text(gen, v.get("value"), key, table_cell)
        note = as_text(v.get("note"))
        return out + (f"（{md_text(note, table_cell)}）" if note else "")
    if isinstance(v, list):
        return "・".join(value_text(gen, x, key, table_cell) for x in v)
    if v is None or isinstance(v, bool):
        own = gen.config.labels(key) if key else {}
        if v is None:
            return own.get("null", "—")        # 値を書いた文書がない（属性ごとの言葉があればそれ）
        labels = own or gen.config.labels("boolean")
        word = "true" if v else "false"
        return labels.get(word, word)
    return md_text(v, table_cell)


def _fill(template: str, values: dict[str, str]) -> str:
    return TEMPLATE_RE.sub(lambda m: values.get(m.group(1), ""), template)


def unchecked(gen) -> str:
    return gen.text("unchecked", "未確認")


def table_cell(item, row: str, col: str):
    """facts の table の (見つかったか, 値)。"""
    t = item.raw.get("table")
    if not isinstance(t, dict):
        return False, None
    cols = [c.get("id") if isinstance(c, dict) else c for c in t.get("columns") or []]
    if col not in cols:
        return False, None
    for cell in t.get("cells") or []:
        if isinstance(cell, dict) and str(cell.get("row")) == row:
            return True, cell.get(col)
    return False, None


def fact_text(gen, host: str, arg: str) -> str:
    """fact の目印の中身（文の中の1行）。"""
    fid, *rest = arg.split()
    data = gen.atlas.data
    item = data.facts.get(fid) if data is not None else None
    if item is None:
        gen.note(f"{host}: 数値「{fid}」が data/facts.yml の facts にない（空にした）")
        return ""
    if not gen.is_confirmed(item):
        return unchecked(gen)
    if item.has("table"):
        if len(rest) != 2:
            gen.note(f"{host}: 数値「{fid}」は表なので、目印に行と列を書く（fact:begin {fid} <行> <列>。空にした）")
            return ""
        found, value = table_cell(item, rest[0], rest[1])
        if not found:
            gen.note(f"{host}: 数値「{fid}」の表に、行「{rest[0]}」と列「{rest[1]}」のセルがない（空にした）")
            return ""
    else:
        if rest:
            gen.note(f"{host}: 数値「{fid}」は表でないので、行と列（{' '.join(rest)}）は読まない")
        value = item.raw.get("value")
    unit = item.text("unit")
    checked = item.text("checked")
    sentence = item.text("sentence") or ("{value} {unit}" if unit else "{value}")
    if "{checked}" not in sentence and checked:
        sentence += "（{checked} " + gen.text("as_of", "時点") + "）"
    return _fill(sentence, {"value": value_text(gen, value), "unit": md_text(unit), "checked": checked})


def sources_line(gen, host: str, ids: list[str]) -> str:
    """出典の id のリスト → 「[題名](URL)、…」（ない id は文字のまま）。"""
    data = gen.atlas.data
    out = []
    for sid in ids:
        src = data.sources.get(sid) if data is not None else None
        if src is None:
            gen.note(f"{host}: 出典「{sid}」が data の sources にない（文字のまま書いた）")
            out.append(md_text(sid))
        else:
            out.append(f"[{md_text(src.text('title') or sid)}]({src.text('url')})")
    return "、".join(out)


@block("fact-table", param="<数値の id>", doc="数値ファイルの表（facts の table）の全体と、確認日・出典・食い違い")
def b_fact_table(ctx) -> str:
    gen = ctx.gen
    data = gen.atlas.data
    item = data.facts.get(ctx.param) if data is not None else None
    if item is None:
        gen.note(f"{ctx.host}: 数値「{ctx.param}」が data/facts.yml の facts にない（空にした）")
        return ""
    if not gen.is_confirmed(item):
        return unchecked(gen)
    t = item.raw.get("table")
    if not isinstance(t, dict):
        gen.note(f"{ctx.host}: 数値「{ctx.param}」は表でない（fact-table は table の項目に使う。空にした）")
        return ""
    surfaces = gen.config.labels("surfaces")
    cols = []
    for c in t.get("columns") or []:
        cid = c.get("id") if isinstance(c, dict) else c
        title = as_text(c.get("title")) if isinstance(c, dict) else ""
        cols.append((str(cid), title or surfaces.get(str(cid), str(cid))))
    rows = []
    row_sources: list[tuple[str, list[tuple[str, list[str]]]]] = []      # (行の名前, [(列の題, セルの出典の id)])
    for cell in t.get("cells") or []:
        if isinstance(cell, dict):
            rows.append([md_text(cell.get("row"), True)] + [value_text(gen, cell.get(c), table_cell=True) for c, _ in cols])
            per = [(title, as_strings(cell[c].get("sources"))) for c, title in cols
                   if isinstance(cell.get(c), dict) and as_strings(cell[c].get("sources"))]
            if per:
                row_sources.append((md_text(cell.get("row")), per))
    out = table([md_text(as_text(t.get("rows")), True)] + [md_text(title, True) for _, title in cols], rows)
    tail = [f"{gen.config.text('references', 'checked', '確認日')} {item.text('checked')}"]
    if item.strings("sources") and not row_sources:
        tail.append(f"{gen.text('sources', '出典')}：" + sources_line(gen, ctx.host, item.strings("sources")))
    for c in item.parts("conflict"):
        tail.append(f"{gen.text('conflict', '食い違い')}：" + value_text(gen, c.get("value")) + "（" + sources_line(gen, ctx.host, as_strings(c.get("sources")))
                    + (f"。{md_text(as_text(c.get('note')))}" if as_text(c.get("note")) else "") + "）")
    out += "\n\n" + "。".join(tail) + "。"
    if row_sources:
        out += "\n\n" + gen.text("sources", "出典") + "（" + gen.text("per_row", "行ごと") + "）：\n\n" + \
            "\n".join(_row_sources_line(gen, ctx.host, name, per) for name, per in row_sources)
        used = {s for _, per in row_sources for _, ids in per for s in ids}
        rest = [s for s in item.strings("sources") if s not in used]
        if rest:
            out += f"\n\n{gen.text('other_sources', 'そのほかの出典')}：" + sources_line(gen, ctx.host, rest) + "。"
    return out


def _row_sources_line(gen, host: str, name: str, per: list[tuple[str, list[str]]]) -> str:
    """行ごとの出典の1行。その行のセルの出典がすべて同じなら「行：出典」、違えば「行：列の題 出典；列の題 出典」。"""
    if all(ids == per[0][1] for _, ids in per):
        return f"- {name}：" + sources_line(gen, host, per[0][1])
    return f"- {name}：" + "；".join(f"{md_text(title)} " + sources_line(gen, host, ids) for title, ids in per)


def feature_value(gen, key: str, v, table_cell: bool = False, feat=None) -> str:
    """機能の属性の値を表示の文字にする。値が null で、機能の conditional にその属性があれば「条件による」
    （条件で値が変わる）、conditional になければ「未確認」など（確かめていない。属性ごとの言葉は labels.<属性>.null）。"""
    if v is None and feat is not None and key in feat.strings("conditional"):
        return gen.text("conditional", "条件による")
    if key == "surfaces":
        return "・".join(gen.label("surfaces", s) for s in as_strings(v)) or "—"
    if key == "since" and isinstance(v, dict):
        ver, date = as_text(v.get("claude_code")), as_text(str(v.get("date") or ""))
        text = ver + (f"（{date}）" if ver and date else date)
        return md_text(text, table_cell) or "—"
    if isinstance(v, bool) or v is None:
        return value_text(gen, v, key if gen.config.labels(key) else None, table_cell)
    return value_text(gen, v, None, table_cell)


@block("feature", kind="inline", param="<属性> か <機能の id>/<属性>",
       doc="機能の属性（強制力・成熟度など。data/facts.yml の features）。機能を省くとページの tracks の最初")
def b_feature(ctx) -> str:
    gen = ctx.gen
    fid, _, key = ctx.param.rpartition("/")
    if not fid:
        fid = ctx.page.tracks[0] if ctx.page is not None and ctx.page.tracks else ""
    feat = gen.feature(fid) if fid else None
    if feat is None:
        gen.note(f"{ctx.host}: 生成の部分「{ctx.name}」の機能「{fid or '（tracks がない）'}」が data/facts.yml の features にない（空にした）")
        return ""
    if not gen.is_confirmed(feat):
        return unchecked(gen)
    if key not in gen.config.labels("feature_keys") and key not in FEATURE_KEYS_DEFAULT:
        gen.note(f"{ctx.host}: 生成の部分「{ctx.name}」の属性「{key}」は機能の属性でない（空にした）")
        return ""
    return feature_value(gen, key, feat.raw.get(key), feat=feat)


CHECKED_KEY = "checked"      # compare の列の指定で確認日を指す id（表示の名前は references.checked の「確認日」）


def _compare_columns(ctx, names: dict[str, str], feats: list) -> list[str]:
    """compare の列（属性の id と CHECKED_KEY の並び）。目印の引数があればそれ（属性の id か表示の名前か確認日）、
    なければ値のある属性（または conditional で挙げた属性）と確認日。"""
    gen = ctx.gen
    checked_word = gen.config.text("references", "checked", "確認日")
    if not ctx.param.strip():
        confirmed = [f for f in feats if gen.is_confirmed(f)]
        keys = [k for k in names if any(f.raw.get(k) is not None or k in f.strings("conditional") for f in confirmed)]
        return keys + [CHECKED_KEY]
    by_label = {v: k for k, v in names.items()}
    cols: list[str] = []
    for tok in ctx.param.split():
        key = tok if tok in names else by_label.get(tok)
        if key is None and tok in (CHECKED_KEY, checked_word):
            key = CHECKED_KEY
        if key is None:
            gen.note(f"{ctx.host}: 比較の表の列「{tok}」は機能の属性でも確認日でもない（列にしない。"
                     f"使えるのは {'・'.join(names.values())}・{checked_word}）")
        elif key not in cols:
            cols.append(key)
    return cols


@block("compare", param="[<列> …]", param_optional=True,
       doc="比較の表：ページの tracks の機能の属性（data/facts.yml の features）。列は属性の id か表示の名前か確認日で指す"
           "（省くと値のある属性と確認日）。全行が同じ値の列は表から省き、表の下に「すべて共通：…」の1行で出す")
def b_compare(ctx) -> str:
    gen = ctx.gen
    page = ctx.page
    names = gen.config.labels("feature_keys") or {k: k for k in FEATURE_KEYS_DEFAULT}
    feats = []
    for fid in (page.tracks if page is not None else []):
        f = gen.feature(fid)
        if f is None:
            gen.note(f"{ctx.host}: 比較の表の機能「{fid}」が data/facts.yml の features にない（表に入れない）")
        else:
            feats.append(f)
    if not feats:
        return gen.text("empty", "（まだない）")
    keys = _compare_columns(ctx, names, feats)
    if not keys:
        return gen.text("empty", "（まだない）")
    heads = {k: md_text(gen.config.text("references", "checked", "確認日") if k == CHECKED_KEY else names[k], True) for k in keys}
    rows = []                                   # 行ごとの {列: 表示の文字}
    for f in feats:
        if gen.is_confirmed(f):
            cell = {k: (f.text("checked") or "—") if k == CHECKED_KEY else feature_value(gen, k, f.raw.get(k), True, f) for k in keys}
        else:
            cell = {k: (f.text("checked") or "—") if k == CHECKED_KEY else unchecked(gen) for k in keys}
        rows.append(cell)
    common = [k for k in keys if len(rows) > 1 and len({r[k] for r in rows}) == 1]
    if len(common) == len(keys):
        common = []                             # 全部が共通なら、表の中身がなくなるので省かない
    shown = [k for k in keys if k not in common]
    out_rows = []
    for f, cell in zip(feats, rows):
        main = gen.atlas.by_id.get(f.text("page"))
        name = gen.page_link(ctx.host, main, table=True, text=md_text(f.text("title") or f.id, True)) if main else \
            md_text(f.text("title") or f.id, True)
        out_rows.append([name] + [cell[k] for k in shown])
    out = table([md_text(gen.text("feature_column", "機能"), True)] + [heads[k] for k in shown], out_rows)
    if common:
        out += "\n\n" + gen.text("common", "すべて共通") + "：" + "、".join(f"{heads[k]} {rows[0][k]}" for k in common) + "。"
    return out
