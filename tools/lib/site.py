"""schema/site.yml（語彙）を読む。道具は語彙をコードに書かず、ここから読む（設計書 §3.2。kyopro-atlas の反省）。

Site.vocab(名前) は、site.yml のそのキーを語彙のリストとして読む：文字列のリストはそのまま、{id, title} のリスト
（fields）は id の並び、マッピング（volatility_days）はキーの並び。名前のリストを渡すと、それぞれをつないだもの
（routes の cause は prevents と pitfalls）。ないか形が違えば None（その語彙の検査をしない、と呼ぶ側が決める）。
"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .base import Fatal, Problem, as_list
from .yamlio import line_of, read_yaml

SITE_YML = "schema/site.yml"


class Site:
    """site.yml の中身。raw は YAML のまま。"""

    def __init__(self, raw: dict, file: str = SITE_YML, problems: Iterable[Problem] = ()):
        self.raw = raw
        self.file = file
        self.problems: list[Problem] = list(problems)
        self.fields: list[str] = []                 # 分野の id（並び順がナビゲーションの順）
        self.field_titles: dict[str, str] = {}
        for x in as_list(raw.get("fields")):
            fid = x.get("id") if isinstance(x, dict) else x
            if isinstance(fid, str) and fid.strip():
                self.fields.append(fid)
                self.field_titles[fid] = str(x.get("title") or "") if isinstance(x, dict) else ""
            else:
                self.problems.append(Problem(file, line_of(x), f"fields の項目に id がない（{x!r}）", "設定"))

    # ---- 語彙

    def vocab(self, name: str | Iterable[str]) -> list[str] | None:
        """site.yml の name を語彙のリストとして読む（ないか形が違えば None）。"""
        if not isinstance(name, str):
            out: list[str] = []
            for n in name:
                part = self.vocab(n)
                if part is None:
                    return None
                out += [x for x in part if x not in out]
            return out
        v = self.raw.get(name)
        if isinstance(v, list) and v and all(isinstance(x, str) for x in v):
            return list(v)
        if isinstance(v, list) and v and all(isinstance(x, dict) and isinstance(x.get("id"), str) for x in v):
            return [x["id"] for x in v]
        if isinstance(v, list) and not v:
            return []
        if isinstance(v, dict) and v:
            return [str(k) for k in v]
        return None

    def has(self, name: str) -> bool:
        return self.vocab(name) is not None

    def rank(self, name: str) -> dict[str, int]:
        """語彙の並びの順（levels・stages など。低い順）。"""
        return {x: i for i, x in enumerate(self.vocab(name) or [])}

    @property
    def types(self) -> list[str]:
        return self.vocab("types") or []

    @property
    def types_without_level(self) -> list[str]:
        return self.vocab("types_without_level") or []

    @property
    def levels(self) -> list[str]:
        return self.vocab("levels") or []

    @property
    def priorities(self) -> list[str]:
        return self.vocab("priorities") or []

    @property
    def stages(self) -> list[str]:
        return self.vocab("stages") or []

    @property
    def causes(self) -> list[str]:
        """routes の cause の語彙（prevents と pitfalls）。"""
        return self.vocab(["prevents", "pitfalls"]) or []

    @property
    def volatility_days(self) -> dict[str, int]:
        """変わりやすさごとの点検の期限（日。design §9.2）。整数でない値は飛ばす。"""
        v = self.raw.get("volatility_days")
        if not isinstance(v, dict):
            return {}
        return {str(k): d for k, d in v.items() if isinstance(d, int) and not isinstance(d, bool) and d > 0}

    @property
    def default_fact_volatility(self) -> str | None:
        """数値（data の facts・features）の volatility の既定（design §9.2「既定は高」）。site.yml の
        default_fact_volatility があればそれ、なければ期限のいちばん短いもの。"""
        days = self.volatility_days
        v = self.raw.get("default_fact_volatility")
        if isinstance(v, str) and v in days:
            return v
        return min(days, key=days.get) if days else None

    @property
    def published_stages(self) -> list[str]:
        """公開する段階（design §8.4：stub は公開しない）。site.yml の published_stages があればそれ、なければ
        stages の最初（stub）のほか。"""
        v = self.vocab("published_stages")
        stages = self.stages
        if v is not None and all(x in stages for x in v):
            return v
        return stages[1:]

    @property
    def guard_fields(self) -> list[str]:
        """比例則の守りの分野（proportional_rule の guard_fields）。"""
        pr = self.raw.get("proportional_rule")
        return [x for x in as_list(pr.get("guard_fields")) if isinstance(x, str)] if isinstance(pr, dict) else []

    @property
    def proportional_levels(self) -> list[str]:
        pr = self.raw.get("proportional_rule")
        return [x for x in as_list(pr.get("levels")) if isinstance(x, str)] if isinstance(pr, dict) else []


def load_site(root: Path) -> Site:
    """schema/site.yml を読む。読めない・最上位がマッピングでない・fields がないときは Fatal。"""
    doc = read_yaml(Path(root) / SITE_YML)
    if doc.error is not None:
        raise Fatal(f"{SITE_YML} が読めない: {doc.error}")
    if not isinstance(doc.data, dict):
        raise Fatal(f"{SITE_YML} の最上位がマッピングでない")
    site = Site(doc.data, SITE_YML, doc.problems(SITE_YML))
    if not site.fields:
        raise Fatal(f"{SITE_YML} に fields（分野の id）がない")
    return site
