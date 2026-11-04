"""鮮度の検査：確認日の期限（design §9.2・§9.3。日によって結果が変わるので警告）と、目印の外の数値（design §6.7・
DR-16。照合の型を持つ数値だけを照らす警告）。

期限の日は読む層（lib.model.Atlas.expiry）が数える：「ページの確認日（verified と checked の新しいほう）＋ページの
期限」と「各数値の確認日＋数値の期限」のうち早いもの。draft は verified がないので数値の分だけ。

目印の外の数値：data/facts.yml の facts のうち、match（照合の型）を持つ項目の value を、本文（フェンス・HTML の
コメント・目印の中を除く）と、front matter の title・summary・signs の文から探す。値の前後は match の
units（値の後の単位）・before（値の前の語）・after（値の後の語）・pattern（正規表現。{value} を値に置き換える）で
照らす。表（table）の値は照らさない。全角の数字と記号は NFKC で半角にしてから照らし、3桁ごとの「,」も許す。
"""
from __future__ import annotations

import re
import unicodedata
from typing import Iterator

from lib.base import as_strings

from .body import masked_lines, written
from .context import Context
from .core import WARNING, Finding, check
from .relations import at

DUE_NAMES = {"page": "ページの確認日", "fact": "数値", "feature": "機能"}


def describe_due(due) -> str:
    kind, _, name = due.what.partition(":")
    what = DUE_NAMES.get(kind, kind) + (f"「{name}」の確認日" if name else "")
    return f"{what} {due.checked.isoformat()}＋{due.volatility} {due.days} 日"


@check("確認日", WARNING)
def check_expiry(ctx: Context) -> Iterator[Finding]:
    """ページの期限の日（design §9.2）が今日より前（点検で確かめ直す。日によって結果が変わるので警告）。tracks で機能を
    指すのに、verified_with に版（claude_code か app）がない（版に依存する記述の確認日。design §8.6）"""
    for p in ctx.pages:
        if ctx.is_stub(p):
            continue
        e = ctx.atlas.expiry(p)
        if e.date is not None and e.date < ctx.today:
            yield at(ctx, p, f"期限の日 {e.date.isoformat()} を過ぎた（{describe_due(e.by)}。今日は {ctx.today.isoformat()}）",
                     "verified" if e.by.what == "page" else None)
        vw = p.raw.get("verified_with")
        if p.tracks and isinstance(vw, dict) and not (vw.get("claude_code") or vw.get("app")):
            yield at(ctx, p, "tracks で機能を指すのに、verified_with に確かめた版（claude_code か app）がない", "verified_with")


# ---------------------------------------------------------------- 目印の外の数値


def value_pattern(v) -> str | None:
    """値を照らす正規表現（数は前後に数字が続かないもの。整数は3桁ごとの , も許す）。"""
    if isinstance(v, bool) or v is None:
        return None
    if isinstance(v, int):
        digits = str(abs(v))
        groups = []
        while len(digits) > 3:
            groups.insert(0, digits[-3:])
            digits = digits[:-3]
        groups.insert(0, digits)
        body = ",?".join(groups)
        return rf"(?<![0-9.,]){'-' if v < 0 else ''}{body}(?![0-9]|[.,][0-9])"
    if isinstance(v, float):
        return rf"(?<![0-9.,]){re.escape(repr(v))}(?![0-9])"
    if isinstance(v, str):
        s = unicodedata.normalize("NFKC", v.strip())
        if not s:
            return None
        head = r"(?<![A-Za-z0-9])" if s[0].isascii() and s[0].isalnum() else ""
        tail = r"(?![A-Za-z0-9])" if s[-1].isascii() and s[-1].isalnum() else ""
        return head + re.escape(s) + tail
    return None


def fact_patterns(item) -> list[tuple[str, re.Pattern]]:
    """facts の1項目の照らし方 (見せる値, 正規表現) の並び（match がなければ空）。"""
    match = item.raw.get("match")
    if not isinstance(match, dict):
        return []
    values = item.raw.get("value")
    values = values if isinstance(values, list) else [values]
    out = []
    for v in values:
        vp = value_pattern(v)
        if vp is None:
            continue
        shown = str(v)
        pats = []
        for u in as_strings(match.get("units")):
            pats.append(vp + r"\s*" + re.escape(unicodedata.normalize("NFKC", u)))
        for b in as_strings(match.get("before")):
            pats.append(re.escape(unicodedata.normalize("NFKC", b)) + r"\s*" + vp)
        for a in as_strings(match.get("after")):
            pats.append(vp + r"\s*" + re.escape(unicodedata.normalize("NFKC", a)))
        pattern = match.get("pattern")
        if isinstance(pattern, str) and pattern:
            pats.append(pattern.replace("{value}", vp))
        for pat in pats:
            try:
                out.append((shown, re.compile(pat)))
            except re.error:
                continue
    return out


def search_text(text: str, patterns) -> str | None:
    norm = unicodedata.normalize("NFKC", text)
    for shown, rx in patterns:
        m = rx.search(norm)
        if m:
            return m.group(0)
    return None


@check("目印の外の数値", WARNING)
def check_values_outside_markers(ctx: Context) -> Iterator[Finding]:
    """数値ファイルの値（照合の型 match を持つ facts の value）と同じ値を、目印の外に手で書いている（本文と、front matter
    の title・summary・signs。変わりやすい値は fact の目印の間に道具が書く。design §6.7）"""
    data = ctx.data
    if data is None:
        return
    facts = [(it, fact_patterns(it)) for it in data.entries("facts")]
    facts = [(it, pats) for it, pats in facts if pats]
    if not facts:
        return
    for p in ctx.pages:
        fields = [("title", p.text("title")), ("summary", p.text("summary"))]
        fields += [("signs", str(s.get("text") or "")) for s in p.parts("signs")]
        for key, text in fields:
            for it, pats in facts:
                hit = search_text(text, pats)
                if hit:
                    yield at(ctx, p, f"{key} に数値ファイルの値「{hit}」（{it.label}）がある（題名・要約・サインに変わりやすい値を"
                                     "書かない）", key)
    for p in written(ctx):
        lines = masked_lines(p.md, p.markers)
        for i, line in enumerate(lines):
            if not line.strip():
                continue
            for it, pats in facts:
                hit = search_text(line, pats)
                if hit:
                    yield Finding(p.file, p.body_line + i, p.label, f"数値ファイルの値「{hit}」（{it.label}）を目印の外に書いている"
                                                                    f"（<!-- fact:begin {it.label} --><!-- fact:end --> にする）")
