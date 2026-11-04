"""規則が名指しする語彙と数（tools/check_catalog.py の定数と同じ値）と、schema/site.yml の語彙の読み方。

語彙の値の一覧（分野・型・段階など）は site.yml から読み、コードに書かない。ここに置くのは、規則がどの値を名指しする
か（「症状のページは…」の symptom など）と、規則の数（前提は4つまで、など）だけ。名指しする値が site.yml にあるかは
「設定」の検査が確かめる（なければ、その規則が当たらないことを知らせる）。

出どころ:
  型と数        planning/catalog/README.md §4.1・§4.4・§4.5（check_catalog.py と同じ）
  本文の形      planning/guides/common.md §3（冒頭）・§4（見出しと節）
"""
from __future__ import annotations

from dataclasses import dataclass, field

from lib import Site

# ---- 型と数（check_catalog.py の SYMPTOM_TYPE などと同じ）
SYMPTOM_TYPE = "symptom"        # 症状のページ：困りごとのサインを2つ以上、prevents を1つ以上。routes を持てるのはこの型だけ
SYMPTOM_SIGN = "symptom"        # 困りごとのサインの種類
FEATURE_TYPE = "feature"        # 機能のページ：tracks が要る
SYMPTOM_PREREQUISITE_TYPES = ("concept", "guide", "hub")   # 症状のページの前提に置く型（catalog/README §4.4 の6）
MIN_SYMPTOM_SIGNS = 2
MAX_PREREQUISITES = 4           # 直接の前提は4つまで（5つ以上で警告）
MAX_RELATED = 20
MAX_ROUTE_TARGETS = 3           # routes の1つの cause の to は、中心の対処を3件まで（4件以上で警告）
MAX_SUMMARY_SENTENCES = 2

# ---- 本文の形（planning/guides/common.md §3・§4）
ABSTRACT_HEAD = '!!! abstract "要点"'        # 冒頭の要点の囲み（requirements §5.3）
PREREQUISITE_LABEL = "前提"                  # 要点の囲みの「- **前提**：…」の項目
NONE_TEXT = "なし"                           # 前提がないときの書き方
ABSTRACT_FREE_TYPES = ("guide", "hub")      # 要点の項目を内容に合わせて変えてよい型（前提の項目を問わない）
ALIASES_LABEL = "別名："                     # 別名の行の頭
ALIASES_SEP = "・"
TEXTLINT_OFF, TEXTLINT_ON = "<!-- textlint-disable -->", "<!-- textlint-enable -->"   # 別名の行を囲む印

NAMED_TYPES = {SYMPTOM_TYPE: "症状の signs・prevents・routes", FEATURE_TYPE: "機能の tracks",
               **{t: "症状の前提・要点の前提" for t in SYMPTOM_PREREQUISITE_TYPES + ABSTRACT_FREE_TYPES}}


@dataclass
class Rules:
    """site.yml の語彙（check_catalog.py の Vocab と同じ読み方。読めない語彙は None で、その検査をしない）。"""

    site: Site
    fields: list[str] = field(default_factory=list)
    types: list[str] | None = None
    types_without_level: list[str] = field(default_factory=list)
    fields_without_level: list[str] = field(default_factory=list)
    levels: list[str] | None = None
    priorities: list[str] | None = None
    prevents: list[str] | None = None
    pitfalls: list[str] | None = None
    sign_types: list[str] | None = None
    stages: list[str] = field(default_factory=list)
    entry_fields: list[str] = field(default_factory=list)
    first_wave_core_fields: list[str] = field(default_factory=list)
    summary_banned_words: list[str] = field(default_factory=list)
    summary_max_chars: int | None = None
    proportional_levels: list[str] = field(default_factory=list)
    guard_fields: list[str] = field(default_factory=list)

    @classmethod
    def from_site(cls, site: Site) -> Rules:
        v = site.vocab
        r = cls(site, list(site.fields))
        r.types = v("types")
        r.types_without_level = v("types_without_level") or []
        r.fields_without_level = v("fields_without_level") or []
        r.levels = v("levels")
        r.priorities = v("priorities")
        r.prevents = v("prevents")
        r.pitfalls = v("pitfalls")
        r.sign_types = v("sign_types")
        r.stages = site.stages
        r.entry_fields = v("entry_fields") or r.fields[:1]
        r.first_wave_core_fields = v("first_wave_core_fields") or []
        r.summary_banned_words = v("summary_banned_words") or []
        mc = site.raw.get("summary_max_chars")
        r.summary_max_chars = mc if isinstance(mc, int) and not isinstance(mc, bool) and mc > 0 else None
        r.proportional_levels = site.proportional_levels
        r.guard_fields = site.guard_fields
        return r

    @property
    def level_rank(self) -> dict[str, int]:
        return {lv: i for i, lv in enumerate(self.levels or [])}

    @property
    def top_priority(self) -> str | None:
        """必須（site.yml の priorities の最初）。"""
        return self.priorities[0] if self.priorities else None

    @property
    def causes(self) -> list[str] | None:
        """routes の cause の語彙（prevents と pitfalls。どちらかが読めなければ None）。"""
        if self.prevents is None or self.pitfalls is None:
            return None
        return self.prevents + self.pitfalls

    @property
    def skeleton_stage(self) -> str | None:
        """骨格の段階（site.yml の stages の最初。いまは stub）。"""
        return self.stages[0] if self.stages else None

    def needs_level(self, page) -> bool:
        """level が要るページか（型が語彙にないときは決めない）。"""
        t = page.type
        if self.types is None or t not in self.types:
            return False
        return t not in self.types_without_level and page.field not in self.fields_without_level

    def config_notes(self) -> list[str]:
        """規則が名指しする値が site.yml にない、などの注（「設定」の検査が出す）。"""
        notes = []
        for key, value in (("types", self.types), ("levels", self.levels), ("priorities", self.priorities),
                           ("prevents", self.prevents), ("pitfalls", self.pitfalls), ("sign_types", self.sign_types)):
            if value is None:
                notes.append(f"site.yml の {key} がない（その語彙を使う規則を当てない）")
        if self.types is not None:
            for value, uses in NAMED_TYPES.items():
                if value not in self.types:
                    notes.append(f"道具の規則が名指しする「{value}」が site.yml の types にない（{uses}の検査が当たらない。"
                                 "tools/checks/rules.py の定数を直す）")
        if self.sign_types is not None and SYMPTOM_SIGN not in self.sign_types:
            notes.append(f"道具の規則が名指しする「{SYMPTOM_SIGN}」が site.yml の sign_types にない（症状の signs の検査が当たらない）")
        if not self.stages:
            notes.append("site.yml の stages がない（置き場所と stage・公開を検査しない）")
        if not self.proportional_levels or not self.guard_fields:
            notes.append("site.yml の proportional_rule（levels・guard_fields）がない（比例則を検査しない）")
        if self.summary_max_chars is None:
            notes.append("site.yml の summary_max_chars がない（summary の長さを検査しない）")
        return notes
