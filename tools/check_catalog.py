#!/usr/bin/env python3
"""目次（planning/catalog/ の registry.yaml と <field>.yaml）を検査する（工程3。設計書 §5.2 の3）。
形式と規則は planning/catalog/README.md の §2〜§6、語彙は schema/site.yml、上位の規則は planning/design.md の §3〜§5。

使い方:
  python3 tools/check_catalog.py                   全分野を検査して、エラーと警告を1件1行で出す
  python3 tools/check_catalog.py --field symptoms  その分野に関わる指摘だけを出す（読むのと参照の解決は全体で行う）
  python3 tools/check_catalog.py --stats           集計（分野ごとのページ数と内訳・第一波の数と内訳・必須の数）も出す
  python3 tools/check_catalog.py -q                警告を出さない（件数だけを最後の行に出す）
  python3 tools/check_catalog.py --root DIR        DIR を根にして読む（DIR/schema/site.yml と DIR/planning/catalog/。試験用）
終了コード: 0＝エラーがない（警告だけなら 0）、1＝エラーがある（--field のときは、その分野に関わるエラーで決める）、
           2＝検査できない（site.yml が読めない、--field の分野が site.yml の fields にない）

出力: 1件1行で「エラー: <ファイル>:<行>: <ページの id>: [<検査>] <内容>」（警告は「警告: 」で始まる）。
      ページに関わらない指摘は id を「-」、id のないページは「(pages の N 番目)」にする。最後の行に件数を出す。

読むもの:
  schema/site.yml                 語彙（道具に語彙を直書きしない）。visual と templates の kind は、site.yml に
                                  visual_kinds・template_kinds があればそれを、なければ catalog/README.md の §3・§4.7 の
                                  書き方から読む。あれば読むもの：fields_without_level（level を持たない分野）、
                                  entry_fields（入ってくる道を問わない分野。なければ fields の最初の分野＝start）。
                                  第一波の数え方は first_wave（routes：none・first・all、named：名指しの正本の id）
  planning/catalog/registry.yaml  候補（pages）と、古くなった助言の台帳の項目（ledger）
  planning/catalog/<field>.yaml   分野のページ。ファイル名が site.yml の fields の id のものだけを読む
  機能の id（tracks）             planning/catalog/features.yaml があればそこから、なければ catalog/README.md §5 の表から読み、
                                  どの分野のファイルの new_features の id も加える。features.yaml は、id の文字列のリスト、
                                  {id: …} のリスト、それらを面ごとの見出しの下に置いたマッピング（features: の下でもよい）を読む

参照（prerequisites・related・症状のページの routes の to・merged の into）の解決:
  ページの id                          解決する。related と routes の id#anchor は、相手の sections の anchor も確かめる
  分野のファイルがまだない registry の候補  指摘しない（その分野のファイルができてから確かめる）
  分野のファイルはあるのに、その pages・merged・dropped のどこにもない registry の候補   警告（未処理の候補）
  merged・dropped にした候補、どこにもない id   エラー（参照）

第一波（--stats。catalog/README §4.6 の3）: 閉包。wave: 1 のページ（核）と、核の症状のページの routes の先と、site.yml の
  first_wave の named を種にし、そこから prerequisites でたどって届くページをすべて入れる。routes の先は first_wave の
  routes で決める（none：入れない、first：各 cause の to のうち最初の必須の先。必須の先がない cause からは入れない、
  all：優先度を問わず全部）。内訳は、核 → 前提でたどって届くもの → routes から → named から の順に足したときに新しく
  増えるページの数。routes を none・first・all にしたときの数と、必須の先がない cause の数も出す

構造（設計書 §8.3）: 読む層（load_catalog：YAML を読んでページのモデルにする）→ 検査（@check で登録した関数。
1検査1関数で、重さは登録のときに決める）→ 出力（format_issue・format_stats・summary_line）。検査の一覧は -h の末尾。
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
import unicodedata
from dataclasses import dataclass, field as dc_field
from pathlib import Path
from typing import Callable, Iterable, Iterator

import yaml

ROOT = Path(__file__).resolve().parent.parent
SITE_YML = "schema/site.yml"
CATALOG_DIR = "planning/catalog"
REGISTRY_FILE = "registry.yaml"
FEATURES_FILE = "features.yaml"
README_FILE = "README.md"

ERROR, WARNING = "エラー", "警告"
ALWAYS = frozenset({"*"})          # --field のときも出す指摘（設定の不足、registry が読めない、など）
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")   # ページの id と節の anchor（catalog/README.md §2）

# ============================================================================
# 目次の形（catalog/README.md §2・§3・§5）。読む層と、形・必須・知らない項目の検査が使う
# ============================================================================

STR, STRS, MAP, MAPS, BOOL, WAVE, ANY = "str", "strs", "map", "maps", "bool", "wave", "any"
SHAPE_HINT = {STR: "文字列にする", MAP: "マッピング（{…}）にする", BOOL: "true か false にする",
              WAVE: "1 にする（第一波の核でなければ書かない）"}

PAGE_SHAPE = {
    "id": STR, "chapter": STR, "title": STR, "nav_title": STR, "aliases": STRS, "type": STR, "level": STR,
    "level_evidence": STR, "priority": STR, "wave": WAVE, "surfaces": STRS, "principle": STRS,
    "prevents": STRS, "pitfalls": STRS, "scenes": STRS, "summary": STR, "signs": MAPS,
    "prerequisites": STRS, "routes": MAPS, "related": STRS, "tracks": STRS, "outdated_advice": STRS,
    "volatility": STR, "sections": MAPS, "templates": MAPS, "visual": MAP, "materials": STRS, "notes": ANY,
}
PAGE_REQUIRED = ("id", "title", "type", "priority", "summary", "volatility")   # level は型による（§4.3-2）
PART_SHAPES = {   # ページの中の要素
    "signs": {"type": STR, "text": STR},
    "routes": {"cause": STR, "to": STRS},     # 症状のページの、原因ごとの振り分け先（§4.4 の6）
    "sections": {"title": STR, "anchor": STR, "level": STR},
    "templates": {"name": STR, "kind": STR, "safety": BOOL},
    "visual": {"kind": STR, "text": STR},
}
PART_REQUIRED = {"signs": ("type", "text"), "routes": ("cause", "to"), "sections": ("title", "anchor"),
                 "templates": ("name", "kind"), "visual": ("kind", "text")}
FILE_SHAPE = {"field": STR, "chapters": STRS, "pages": MAPS, "merged": MAPS, "dropped": MAPS,
              "open_issues": ANY, "new_features": MAPS, "notes": ANY}
FILE_REQUIRED = ("field", "pages")
ENTRY_SHAPES = {"merged": {"id": STR, "into": STR, "reason": ANY},
                "dropped": {"id": STR, "reason": ANY},
                "new_features": {"id": STR, "title": STR, "note": ANY}}
ENTRY_REQUIRED = {"merged": ("id", "into"), "dropped": ("id",), "new_features": ("id",)}
REGISTRY_SHAPE = {"pages": MAPS, "ledger": MAPS, "notes": ANY}
REGISTRY_REQUIRED = ("pages", "ledger")
CANDIDATE_SHAPE = {"id": STR, "field": STR, "title": STR, "type": STR, "priority": STR, "level": STR,
                   "origin": ANY, "wave_core": BOOL}
CANDIDATE_REQUIRED = ("id", "field", "title")
LEDGER_SHAPE = {"id": STR, "title": STR, "origin": ANY}
LEDGER_REQUIRED = ("id", "title")

# 語彙で確かめるキーと、その語彙（Vocab の属性。値は site.yml から読む）
PAGE_VOCAB = {"type": "types", "level": "levels", "priority": "priorities", "volatility": "volatility",
              "surfaces": "surfaces", "principle": "principles", "prevents": "prevents",
              "pitfalls": "pitfalls", "scenes": "scenes"}
PART_VOCAB = {("signs", "type"): "sign_types", ("routes", "cause"): "causes", ("sections", "level"): "levels",
              ("templates", "kind"): "template_kinds", ("visual", "kind"): "visual_kinds"}
CANDIDATE_VOCAB = {"field": "fields", "type": "types", "priority": "priorities", "level": "levels"}

# 規則が名指しする語彙と数（catalog/README.md §4.1・§4.4・§4.5・§4.6・§4.7）。
# 名指しする語彙が site.yml にあるかは、読むときに確かめる（なければ「設定」の警告）
SYMPTOM_TYPE = "symptom"        # 症状のページ：困りごとのサインを2つ以上、prevents を1つ以上。routes を持てるのはこの型だけ
SYMPTOM_SIGN = "symptom"        # 困りごとのサインの種類
FEATURE_TYPE = "feature"        # 機能のページ：tracks が要る
SYMPTOM_PREREQUISITE_TYPES = ("concept", "guide", "hub")   # 症状のページの前提に置く型（診断を読むのに要る概念。§4.4 の6）
MIN_SYMPTOM_SIGNS = 2
MAX_PREREQUISITES = 4           # 直接の前提は4つまで（5つ以上で警告）
MAX_RELATED = 20
MAX_ROUTE_TARGETS = 3           # routes の1つの cause の to は、中心の対処を3件まで（4件以上で警告）
MAX_SUMMARY_SENTENCES = 2
NEW_MARK = "新規"                # registry にないページの notes に書く印

# site.yml の first_wave（第一波の数え方。§4.6 の3）。routes の値は道具の数え方の名前（語彙ではない）
FIRST_WAVE_ROUTES = ("none", "first", "all")   # 症状のページの routes の先を：入れない・各 cause の最初の必須の先・全部
FIRST_WAVE_KEYS = ("routes", "named")

# catalog/README.md から読むもの（site.yml にないとき）
VISUAL_KINDS_RE = re.compile(r"visual[^\n]*?kind\s*は\s*([^）)。\n]+)")
TEMPLATE_KINDS_RE = re.compile(r"`templates`[^\n]*?`kind`\s*は\s*([^）)。\n]+)")
FEATURES_SECTION_RE = re.compile(r"^## 5\.[^\n]*\n(.*?)(?=^## |\Z)", re.M | re.S)
BACKTICK_RE = re.compile(r"`([^`]+)`")

# ============================================================================
# 読む層：YAML を読んで、ページのモデルにする
# ============================================================================


class Fatal(Exception):
    """検査できない（site.yml が読めない、など）。"""


class LineDict(dict):
    """行番号（1 から）を持つ dict。読む層は YAML のマッピングをこれにする。"""

    line: int | None = None


def line_of(x) -> int | None:
    return getattr(x, "line", None)


class _Loader(yaml.SafeLoader):
    """SafeLoader に、マッピングの行番号と、同じキーが2回あること（後のものだけが残る）の記録を足したもの。"""

    def __init__(self, stream):
        super().__init__(stream)
        self.duplicate_keys: list[tuple[str, int, int]] = []   # (キー, 行, 先にあった行)

    def construct_mapping(self, node, deep=False):
        if isinstance(node, yaml.MappingNode):
            seen: dict[str, int] = {}
            for key_node, _ in node.value:
                if isinstance(key_node, yaml.ScalarNode) and key_node.tag != "tag:yaml.org,2002:merge":
                    line = key_node.start_mark.line + 1
                    if key_node.value in seen:
                        self.duplicate_keys.append((key_node.value, line, seen[key_node.value]))
                    else:
                        seen[key_node.value] = line
        return super().construct_mapping(node, deep=deep)


def _construct_map(loader: _Loader, node):
    data = LineDict()
    data.line = node.start_mark.line + 1
    yield data
    data.update(loader.construct_mapping(node))


_Loader.add_constructor("tag:yaml.org,2002:map", _construct_map)


@dataclass
class YamlDoc:
    data: object = None
    error: str | None = None
    error_line: int | None = None
    duplicates: list[tuple[str, int, int]] = dc_field(default_factory=list)


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def read_yaml(path: Path) -> YamlDoc:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return YamlDoc(error=f"ファイルが読めない（{e}）")
    loader = _Loader(text)
    try:
        return YamlDoc(data=loader.get_single_data(), duplicates=loader.duplicate_keys)
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None) or getattr(e, "context_mark", None)
        problem = " ".join(str(getattr(e, "problem", None) or e).split())
        context = getattr(e, "context", None)
        where = f"{mark.line + 1} 行 {mark.column + 1} 列" if mark else "位置は不明"
        return YamlDoc(error=f"YAML が読めない（{where}）: {problem}" + (f"（{context}）" if context else ""),
                       error_line=mark.line + 1 if mark else None)
    finally:
        loader.dispose()


def as_text(v) -> str:
    return v.strip() if isinstance(v, str) else ""


def as_strings(v) -> list[str]:
    """文字列のリストとして読む（1つの文字列は1要素のリストにする。形の誤りは「形」の検査が出す）。"""
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        return [x for x in v if isinstance(x, str)]
    return []


def as_maps(v) -> list[dict]:
    """マッピングのリストとして読む（1つのマッピングは1要素のリストにする）。"""
    if isinstance(v, dict):
        return [v]
    if isinstance(v, list):
        return [x for x in v if isinstance(x, dict)]
    return []


@dataclass(frozen=True)
class Ref:
    """prerequisites・related の1件（id か id#anchor）。"""

    raw: str
    target: str
    anchor: str | None

    @classmethod
    def parse(cls, raw: str) -> Ref:
        target, sharp, anchor = raw.strip().partition("#")
        return cls(raw, target.strip(), anchor.strip() if sharp else None)


@dataclass
class Page:
    """分野のファイルの pages の1件（読む層のモデル。raw は YAML のまま）。"""

    raw: dict
    field: str          # ファイル名の分野
    file: str           # 表示用のパス
    index: int          # pages の中の位置（0 から）

    @property
    def line(self) -> int | None:
        return line_of(self.raw)

    @property
    def id(self) -> str | None:
        v = self.raw.get("id")
        return v if isinstance(v, str) and v.strip() else None

    @property
    def label(self) -> str:
        return self.id or f"(pages の {self.index + 1} 番目)"

    @property
    def is_wave(self) -> bool:
        w = self.raw.get("wave")
        return w == 1 and not isinstance(w, bool)

    def text(self, key: str) -> str:
        return as_text(self.raw.get(key))

    def strings(self, key: str) -> list[str]:
        return as_strings(self.raw.get(key))

    def parts(self, key: str) -> list[dict]:
        return as_maps(self.raw.get(key))

    def refs(self, key: str) -> list[Ref]:
        return [Ref.parse(s) for s in self.strings(key)]

    def anchors(self) -> list[str]:
        return [a for a in (as_text(s.get("anchor")) for s in self.parts("sections")) if a]


@dataclass
class Entry:
    """registry の pages・ledger の1件、または分野のファイルの merged・dropped・new_features の1件。"""

    raw: dict
    file: str
    index: int
    kind: str                   # pages・ledger・merged・dropped・new_features
    owner: str | None = None    # 分野のファイルの分野（registry の項目は None）

    @property
    def line(self) -> int | None:
        return line_of(self.raw)

    @property
    def id(self) -> str | None:
        v = self.raw.get("id")
        return v if isinstance(v, str) and v.strip() else None

    @property
    def label(self) -> str:
        return self.id or f"({self.kind} の {self.index + 1} 番目)"

    def text(self, key: str) -> str:
        return as_text(self.raw.get(key))


@dataclass
class FieldFile:
    field: str                  # ファイル名の分野
    file: str                   # 表示用のパス
    raw: dict | None            # 読めなければ None
    pages: list[Page] = dc_field(default_factory=list)
    merged: list[Entry] = dc_field(default_factory=list)
    dropped: list[Entry] = dc_field(default_factory=list)
    new_features: list[Entry] = dc_field(default_factory=list)

    @property
    def readable(self) -> bool:
        return self.raw is not None

    def entries(self) -> list[Entry]:
        return self.merged + self.dropped + self.new_features


@dataclass
class Registry:
    file: str
    present: bool
    raw: dict | None
    candidates: list[Entry] = dc_field(default_factory=list)
    ledger: list[Entry] = dc_field(default_factory=list)

    @property
    def readable(self) -> bool:
        return self.raw is not None

    @property
    def by_id(self) -> dict[str, Entry]:
        out: dict[str, Entry] = {}
        for e in self.candidates:
            if e.id is not None:
                out.setdefault(e.id, e)
        return out

    @property
    def ledger_ids(self) -> set[str]:
        return {e.id for e in self.ledger if e.id is not None}

    def notes(self) -> list[str]:
        return [str(x) for x in as_list(self.raw.get("notes"))] if self.raw else []


def as_list(v) -> list:
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


@dataclass(frozen=True)
class Finding:
    """検査の関数が返す1件。重さと検査の名前は、登録した検査から付く。"""

    file: str
    line: int | None
    page: str
    message: str
    fields: frozenset[str] = frozenset()   # 関わる分野（--field で選ぶ）。ALWAYS はいつも出す
    check: str | None = None               # 読む層が見つけたものだけ：出す検査の名前


@dataclass
class Vocab:
    """schema/site.yml の語彙。語彙が読めないものは None（その検査をしない）。"""

    fields: list[str]
    field_titles: dict[str, str]
    types: list[str] | None = None
    types_without_level: list[str] = dc_field(default_factory=list)
    fields_without_level: list[str] = dc_field(default_factory=list)
    levels: list[str] | None = None
    priorities: list[str] | None = None
    surfaces: list[str] | None = None
    principles: list[str] | None = None
    prevents: list[str] | None = None
    pitfalls: list[str] | None = None
    scenes: list[str] | None = None
    sign_types: list[str] | None = None
    volatility: list[str] | None = None
    visual_kinds: list[str] | None = None
    template_kinds: list[str] | None = None
    proportional_levels: list[str] = dc_field(default_factory=list)
    guard_fields: list[str] = dc_field(default_factory=list)
    first_wave_core_fields: list[str] = dc_field(default_factory=list)
    first_wave_routes: str = "none"      # site.yml の first_wave の routes（FIRST_WAVE_ROUTES のどれか）
    first_wave_named: list[str] = dc_field(default_factory=list)   # site.yml の first_wave の named
    entry_fields: list[str] = dc_field(default_factory=list)
    summary_banned_words: list[str] = dc_field(default_factory=list)
    summary_max_chars: int | None = None

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


# site.yml のリストの語彙：Vocab の属性 → (site.yml のキー, 使う検査)
VOCAB_LISTS = {
    "types": ("types", "type の語彙と level の要否"),
    "levels": ("levels", "level の語彙・レベルの逆転・比例則"),
    "priorities": ("priorities", "priority の語彙・必須の前提"),
    "surfaces": ("surfaces", "surfaces の語彙"),
    "principles": ("principles", "principle の語彙"),
    "prevents": ("prevents", "prevents と routes の cause の語彙"),
    "pitfalls": ("pitfalls", "pitfalls と routes の cause の語彙"),
    "scenes": ("scenes", "scenes の語彙"),
    "sign_types": ("sign_types", "signs の type の語彙"),
}


def load_vocab(root: Path, findings: list[Finding]) -> Vocab:
    """schema/site.yml を読む。読めない・fields がないときは Fatal。足りない語彙は「設定」の警告にする。"""
    doc = read_yaml(root / SITE_YML)
    if doc.error is not None:
        raise Fatal(f"{SITE_YML} が読めない: {doc.error}")
    data = doc.data
    if not isinstance(data, dict):
        raise Fatal(f"{SITE_YML} の最上位がマッピングでない")
    fields: list[str] = []
    titles: dict[str, str] = {}
    for x in as_list(data.get("fields")):
        fid = x.get("id") if isinstance(x, dict) else x
        if isinstance(fid, str) and fid:
            fields.append(fid)
            titles[fid] = str(x.get("title") or "") if isinstance(x, dict) else ""
    if not fields:
        raise Fatal(f"{SITE_YML} に fields（分野の id）がない")

    def note(msg: str) -> None:
        findings.append(Finding(SITE_YML, None, "-", msg, ALWAYS, "設定"))

    def str_list(key: str, uses: str, required: bool = True) -> list[str] | None:
        v = data.get(key)
        if isinstance(v, list) and all(isinstance(x, str) for x in v):
            return list(v)
        if v is None and not required:
            return None
        note(f"site.yml の {key} が{'ない' if v is None else '文字列のリストでない'}（{uses}を検査しない）")
        return None

    vocab = Vocab(fields, titles)
    for attr, (key, uses) in VOCAB_LISTS.items():
        setattr(vocab, attr, str_list(key, uses))
    vd = data.get("volatility_days")
    if isinstance(vd, dict) and vd:
        vocab.volatility = [str(k) for k in vd]
    else:
        note("site.yml の volatility_days がない（volatility の語彙を検査しない）")
    vocab.types_without_level = str_list("types_without_level", "level を持たない型") or []
    pr = data.get("proportional_rule")
    if isinstance(pr, dict):
        vocab.proportional_levels = [x for x in as_list(pr.get("levels")) if isinstance(x, str)]
        vocab.guard_fields = [x for x in as_list(pr.get("guard_fields")) if isinstance(x, str)]
    if not vocab.proportional_levels or not vocab.guard_fields:
        note("site.yml の proportional_rule（levels・guard_fields）がない（比例則を検査しない）")
    vocab.first_wave_core_fields = str_list("first_wave_core_fields", "wave の付け方") or []
    read_first_wave(data.get("first_wave"), vocab, note)
    vocab.summary_banned_words = str_list("summary_banned_words", "summary の使わない語") or []
    mc = data.get("summary_max_chars")
    if isinstance(mc, int) and not isinstance(mc, bool) and mc > 0:
        vocab.summary_max_chars = mc
    else:
        note("site.yml の summary_max_chars がない（summary の長さを検査しない）")
    # あれば読むもの（なければ README から読むか、既定にする）
    vocab.visual_kinds = str_list("visual_kinds", "visual の kind", required=False)
    vocab.template_kinds = str_list("template_kinds", "templates の kind", required=False)
    vocab.fields_without_level = str_list("fields_without_level", "level を持たない分野", required=False) or []
    vocab.entry_fields = str_list("entry_fields", "入ってくる道を問わない分野", required=False) or fields[:1]

    for values, pool, what, pool_key in (
            (vocab.types_without_level, vocab.types, "types_without_level", "types"),
            (vocab.proportional_levels, vocab.levels, "proportional_rule の levels", "levels"),
            (vocab.guard_fields, fields, "proportional_rule の guard_fields", "fields"),
            (vocab.first_wave_core_fields, fields, "first_wave_core_fields", "fields"),
            (vocab.fields_without_level, fields, "fields_without_level", "fields"),
            (vocab.entry_fields, fields, "entry_fields", "fields")):
        for x in values:
            if pool is not None and x not in pool:
                note(f"site.yml の {what} の「{x}」が {pool_key} にない")
    named_values = [(SYMPTOM_TYPE, vocab.types, "types", "症状の signs・prevents・routes"),
                    (FEATURE_TYPE, vocab.types, "types", "機能の tracks"),
                    (SYMPTOM_SIGN, vocab.sign_types, "sign_types", "症状の signs")]
    named_values += [(t, vocab.types, "types", "症状の前提") for t in SYMPTOM_PREREQUISITE_TYPES]
    for value, pool, key, uses in named_values:
        if pool is not None and value not in pool:
            note(f"道具の規則が名指しする「{value}」が site.yml の {key} にない（{uses}の検査が当たらない。"
                 "tools/check_catalog.py の規則の定数を直す）")
    if vocab.priorities == []:
        note("site.yml の priorities が空（必須の前提を検査しない）")
    return vocab


def read_first_wave(fw, vocab: Vocab, note: Callable[[str], None]) -> None:
    """site.yml の first_wave（第一波の数え方。catalog/README §4.6 の3）を読む。読めない分は、routes を none、
    named を空として数え、「設定」の警告にする。"""
    fallback = "第一波を wave: 1 と前提だけで数える"
    if fw is None:
        note(f"site.yml の first_wave がない（{fallback}）")
        return
    if not isinstance(fw, dict):
        note(f"site.yml の first_wave がマッピング（routes・named）でない（{fallback}）")
        return
    for k in fw:
        if k not in FIRST_WAVE_KEYS:
            note(f"site.yml の first_wave の知らない項目「{k}」")
    mode = fw.get("routes")
    if isinstance(mode, str) and mode in FIRST_WAVE_ROUTES:
        vocab.first_wave_routes = mode
    else:
        now = "がない" if mode is None else f"の「{mode}」が {joined(FIRST_WAVE_ROUTES)} のどれでもない"
        note(f"site.yml の first_wave の routes {now}（routes の先を入れずに数える）")
    named = fw.get("named")
    if isinstance(named, list) and all(isinstance(x, str) for x in named):
        vocab.first_wave_named = list(dict.fromkeys(x.strip() for x in named if x.strip()))
    elif named is not None:
        note("site.yml の first_wave の named が文字列のリストでない（named を数えない）")


def parse_kinds(text: str | None, pattern: re.Pattern) -> list[str]:
    """README の「kind は a・b・c」の書き方から語彙を読む。"""
    m = pattern.search(text or "")
    if not m:
        return []
    return [w.strip("` ") for w in re.split(r"[・、,]", m.group(1)) if w.strip("` ")]


def parse_feature_table(text: str | None) -> list[str]:
    """README §5 の表から機能の id（2列目より後の `id`）を読む。"""
    m = FEATURES_SECTION_RE.search(text or "")
    ids: list[str] = []
    for line in (m.group(1).splitlines() if m else []):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        for cell in cells[1:]:
            ids += [x for x in BACKTICK_RE.findall(cell) if x not in ids]
    return ids


def fill_kinds(vocab: Vocab, readme: str | None, findings: list[Finding]) -> None:
    """visual と templates の kind が site.yml になければ、catalog/README.md（§3・§4.7）から読む。"""
    for attr, key, pattern, what in (("visual_kinds", "visual_kinds", VISUAL_KINDS_RE, "visual の kind"),
                                     ("template_kinds", "template_kinds", TEMPLATE_KINDS_RE, "templates の kind")):
        if getattr(vocab, attr) is not None:
            continue
        kinds = parse_kinds(readme, pattern)
        if kinds:
            setattr(vocab, attr, kinds)
        else:
            findings.append(Finding(SITE_YML, None, "-", f"{what}の語彙が site.yml（{key}）にも {CATALOG_DIR}/{README_FILE} "
                                    f"にもない（{what}を検査しない）", ALWAYS, "設定"))


def feature_ids_from(doc) -> tuple[list[str], list]:
    """features.yaml から機能の id を読む。(id, 読めなかった要素)。"""
    node = doc.get("features", doc) if isinstance(doc, dict) else doc
    ids: list[str] = []
    bad: list = []

    def from_list(items: list) -> None:
        for x in items:
            if isinstance(x, str):
                ids.append(x)
            elif isinstance(x, dict) and isinstance(x.get("id"), str):
                ids.append(x["id"])
            else:
                bad.append(x)

    if isinstance(node, list):
        from_list(node)
    elif isinstance(node, dict):
        for k, v in node.items():
            if isinstance(v, list):          # 面ごとの見出し → id のリスト
                from_list(v)
            elif v is None or isinstance(v, dict):   # id → 属性
                ids.append(str(k))
            else:
                bad.append({k: v})
    return ids, bad


def load_features(root: Path, readme: str | None, findings: list[Finding]) -> tuple[set[str] | None, str]:
    """機能の id の表を読む。(id の集合か None, 出どころ)。"""
    path = root / CATALOG_DIR / FEATURES_FILE
    shown = f"{CATALOG_DIR}/{FEATURES_FILE}"
    if path.exists():
        doc = read_yaml(path)
        if doc.error is not None:
            findings.append(Finding(shown, doc.error_line, "-", f"{doc.error}（README §5 の表を使う）", ALWAYS, "YAML"))
        else:
            ids, bad = feature_ids_from(doc.data)
            for x in bad:
                findings.append(Finding(shown, line_of(x), "-", f"機能の id として読めない要素: {brief(x)}", ALWAYS, "形"))
            for x in ids:
                if not ID_RE.match(x):
                    findings.append(Finding(shown, None, x, f"機能の id「{x}」が書式に合わない", ALWAYS, "id の書式"))
            if ids:
                return set(ids), shown
            findings.append(Finding(shown, None, "-", "機能の id が1つも読めない（README §5 の表を使う）", ALWAYS, "設定"))
    ids = parse_feature_table(readme)
    if ids:
        return set(ids), f"{CATALOG_DIR}/{README_FILE} §5"
    findings.append(Finding(f"{CATALOG_DIR}/{README_FILE}", None, "-",
                            f"機能の id の表（{FEATURES_FILE} か README §5）がない（tracks の id を検査しない）", ALWAYS, "設定"))
    return None, ""


def load_registry(root: Path, findings: list[Finding]) -> Registry:
    path = root / CATALOG_DIR / REGISTRY_FILE
    shown = f"{CATALOG_DIR}/{REGISTRY_FILE}"
    reg = Registry(shown, path.exists(), None)
    if not reg.present:
        findings.append(Finding(shown, None, "-", "registry.yaml がない（registry との対応・outdated_advice の id を検査せず、"
                                "まだない分野のページへの参照も解決できない）", ALWAYS, "設定"))
        return reg
    doc = read_yaml(path)
    if doc.error is not None:
        findings.append(Finding(shown, doc.error_line, "-", doc.error, ALWAYS, "YAML"))
        return reg
    for key, line, first in doc.duplicates:
        findings.append(Finding(shown, line, "-", f"同じキー「{key}」が2回ある（{first} 行にもある。後のものだけが読まれる）",
                                ALWAYS, "YAML"))
    if not isinstance(doc.data, dict):
        findings.append(Finding(shown, None, "-", "最上位をマッピング（pages・ledger・notes）にする", ALWAYS, "形"))
        return reg
    reg.raw = doc.data
    for kind, store in (("pages", reg.candidates), ("ledger", reg.ledger)):
        items = doc.data.get(kind)
        if isinstance(items, list):
            store += [Entry(x, shown, i, kind) for i, x in enumerate(items) if isinstance(x, dict)]
    return reg


def load_field_file(root: Path, field: str, findings: list[Finding]) -> FieldFile:
    shown = f"{CATALOG_DIR}/{field}.yaml"
    ff = FieldFile(field, shown, None)
    scope = frozenset({field})
    doc = read_yaml(root / shown)
    if doc.error is not None:
        findings.append(Finding(shown, doc.error_line, "-", doc.error, scope, "YAML"))
        return ff
    for key, line, first in doc.duplicates:
        findings.append(Finding(shown, line, "-", f"同じキー「{key}」が2回ある（{first} 行にもある。後のものだけが読まれる）",
                                scope, "YAML"))
    if not isinstance(doc.data, dict):
        empty = "（空のファイル）" if doc.data is None else ""
        findings.append(Finding(shown, None, "-", f"最上位をマッピング（field・chapters・pages …）にする{empty}", scope, "形"))
        return ff
    ff.raw = doc.data
    pages = doc.data.get("pages")
    if isinstance(pages, list):
        ff.pages = [Page(x, field, shown, i) for i, x in enumerate(pages) if isinstance(x, dict)]
    for kind in ("merged", "dropped", "new_features"):
        items = doc.data.get(kind)
        if isinstance(items, list):
            getattr(ff, kind).extend(Entry(x, shown, i, kind, field) for i, x in enumerate(items) if isinstance(x, dict))
    return ff


@dataclass(frozen=True)
class Resolution:
    """参照の解決の結果。"""

    status: str                       # PAGE・PENDING・UNPROCESSED・MERGED・DROPPED・MISSING
    page: Page | None = None
    entry: Entry | None = None        # registry の候補、または merged・dropped の項目

    @property
    def field(self) -> str | None:
        """相手の分野（ページならその分野、まだない候補なら registry の分野）。"""
        if self.page is not None:
            return self.page.field
        if self.status in (PENDING, UNPROCESSED) and self.entry is not None:
            return self.entry.text("field") or None
        return None


PAGE, PENDING, UNPROCESSED, MERGED, DROPPED, MISSING = "page", "pending", "unprocessed", "merged", "dropped", "missing"


class Catalog:
    """目次の全体（読む層の出力）。検査と集計はこれだけを見る。"""

    def __init__(self, root: Path, vocab: Vocab, registry: Registry, files: dict[str, FieldFile], stray: list[str],
                 feature_ids: set[str] | None, feature_source: str, findings: list[Finding]):
        self.root, self.vocab, self.registry, self.files, self.stray = root, vocab, registry, files, stray
        self.feature_ids, self.feature_source, self.findings = feature_ids, feature_source, findings
        self.pages: list[Page] = [p for ff in files.values() for p in ff.pages]
        self.by_id: dict[str, Page] = {}
        for p in self.pages:
            if p.id is not None:
                self.by_id.setdefault(p.id, p)
        self.merged_ids: dict[str, Entry] = {}
        self.dropped_ids: dict[str, Entry] = {}
        for ff in files.values():
            for e in ff.merged:
                if e.id is not None:
                    self.merged_ids.setdefault(e.id, e)
            for e in ff.dropped:
                if e.id is not None:
                    self.dropped_ids.setdefault(e.id, e)
        self.new_feature_ids = {e.id for ff in files.values() for e in ff.new_features if e.id is not None}
        self.candidates = registry.by_id

    def resolve(self, target: str) -> Resolution:
        if target in self.by_id:
            return Resolution(PAGE, page=self.by_id[target])
        if target in self.merged_ids:
            return Resolution(MERGED, entry=self.merged_ids[target])
        if target in self.dropped_ids:
            return Resolution(DROPPED, entry=self.dropped_ids[target])
        cand = self.candidates.get(target)
        if cand is not None:
            ff = self.files.get(cand.text("field"))
            return Resolution(UNPROCESSED if ff is not None and ff.readable else PENDING, entry=cand)
        return Resolution(MISSING)

    def registry_fields(self, entry: Entry) -> frozenset[str]:
        f = entry.text("field")
        return frozenset({f}) if f in self.vocab.fields else frozenset()

    def file_rank(self, file: str) -> int:
        if file == SITE_YML:
            return -1
        if file == self.registry.file:
            return 0
        for i, f in enumerate(self.vocab.fields):
            if file == f"{CATALOG_DIR}/{f}.yaml":
                return i + 1
        return len(self.vocab.fields) + 1


def load_catalog(root: Path) -> Catalog:
    """目次を読んでモデルにする（読む層の入口）。site.yml が読めなければ Fatal。"""
    root = Path(root)
    findings: list[Finding] = []
    vocab = load_vocab(root, findings)
    cdir = root / CATALOG_DIR
    readme = read_text(cdir / README_FILE)
    fill_kinds(vocab, readme, findings)
    registry = load_registry(root, findings)
    files = {f: load_field_file(root, f, findings) for f in vocab.fields if (cdir / f"{f}.yaml").exists()}
    stray = sorted(f"{CATALOG_DIR}/{p.name}" for p in cdir.glob("*.yaml")
                   if p.name not in (REGISTRY_FILE, FEATURES_FILE) and p.stem not in vocab.fields)
    feature_ids, source = load_features(root, readme, findings)
    return Catalog(root, vocab, registry, files, stray, feature_ids, source, findings)

# ============================================================================
# 検査の層：1検査1関数。@check(名前, 重さ) で登録し、Finding を返す
# ============================================================================


@dataclass(frozen=True)
class Check:
    name: str
    severity: str
    func: Callable[[Catalog], Iterable[Finding]]

    @property
    def summary(self) -> str:
        """docstring の最初の段落を1行にする（折り返しの両側が英数字のときだけ空白を入れる）。"""
        out = ""
        for line in (x.strip() for x in (self.func.__doc__ or "").strip().split("\n\n")[0].splitlines()):
            if out and line and out[-1].isascii() and out[-1].isalnum() and line[0].isascii() and line[0].isalnum():
                out += " "
            out += line
        return out


CHECKS: list[Check] = []


def check(name: str, severity: str):
    def register(func):
        CHECKS.append(Check(name, severity, func))
        return func
    return register


@dataclass(frozen=True)
class Issue:
    severity: str
    check: str
    file: str
    line: int | None
    page: str
    message: str
    fields: frozenset[str]


def run_checks(cat: Catalog, checks: Iterable[Check] | None = None) -> list[Issue]:
    """検査を流して、指摘を（重さ・ファイル・行・検査の順に）並べて返す。"""
    order = {c.name: i for i, c in enumerate(CHECKS)}
    issues = [Issue(c.severity, c.name, f.file, f.line, f.page, f.message, f.fields)
              for c in (CHECKS if checks is None else checks) for f in c.func(cat)]
    issues.sort(key=lambda i: (i.severity != ERROR, cat.file_rank(i.file), i.file, i.line or 0, order.get(i.check, 0)))
    return issues


def brief(v, limit: int = 40) -> str:
    r = repr(v)
    return r if len(r) <= limit else r[:limit - 1] + "…"


def where(x) -> str:
    return f"{x.file}:{x.line}" if x.line else x.file


def at(page: Page, message: str, *also: str | None) -> Finding:
    """ページについての指摘。also は、ほかに関わる分野（--field でその分野にも出す）。"""
    return Finding(page.file, page.line, page.label, message, frozenset([page.field, *[f for f in also if f]]))


def at_entry(entry: Entry, message: str, fields: Iterable[str] = ()) -> Finding:
    return Finding(entry.file, entry.line, entry.label, message, frozenset(fields))


def loaded(cat: Catalog, name: str) -> Iterator[Finding]:
    """読む層が見つけた指摘のうち、その検査が出すもの。"""
    return (f for f in cat.findings if f.check == name)


def is_missing(data: dict, key: str) -> bool:
    v = data.get(key)
    return v is None or (isinstance(v, str) and not v.strip())


def needs_level(vocab: Vocab, page: Page) -> bool:
    """level が要るページか（型が語彙にないときは決めない）。"""
    t = page.text("type")
    if vocab.types is None or t not in vocab.types:
        return False
    return t not in vocab.types_without_level and page.field not in vocab.fields_without_level


def shape_ok(value, kind: str) -> bool:
    if value is None or kind == ANY:
        return True
    if kind == STR:
        return isinstance(value, str)
    if kind == BOOL:
        return isinstance(value, bool)
    if kind == WAVE:
        return value == 1 and not isinstance(value, bool)
    if kind == MAP:
        return isinstance(value, dict)
    return True


def shape_problems(data: dict, shape: dict[str, str], prefix: str = "") -> Iterator[str]:
    for key, kind in shape.items():
        v = data.get(key)
        if v is None or kind == ANY:
            continue
        if kind in (STRS, MAPS):
            if not isinstance(v, list):
                yield f"{prefix}{key} をリスト（[…]）にする（いまは {brief(v)}）"
                continue
            want, name = (str, "文字列") if kind == STRS else (dict, "マッピング（{…}）")
            for i, x in enumerate(v):
                if not isinstance(x, want):
                    yield f"{prefix}{key} の {i + 1} 番目を{name}にする（いまは {brief(x)}）"
        elif not shape_ok(v, kind):
            yield f"{prefix}{key} を{SHAPE_HINT[kind]}（いまは {brief(v)}）"


def unknown_keys(data: dict, shape: dict[str, str]) -> list[str]:
    return [str(k) for k in data if k not in shape]


def page_refs(p: Page) -> Iterator[tuple[str, Ref]]:
    for key in ("prerequisites", "related"):
        for ref in p.refs(key):
            yield key, ref


def route_label(route: dict, index: int) -> str:
    """routes の1件の呼び名（「routes（縛っていない）」。cause がなければ「routes の N 番目」）。"""
    cause = as_text(route.get("cause"))
    return f"routes（{cause}）" if cause else f"routes の {index + 1} 番目"


def route_refs(p: Page) -> Iterator[tuple[str, Ref]]:
    """routes の to の1件ずつ（呼び名「routes（cause）の to」, 参照）。"""
    for i, route in enumerate(p.parts("routes")):
        label = f"{route_label(route, i)}の to"
        for s in as_strings(route.get("to")):
            yield label, Ref.parse(s)


def bad_target(r: Resolution) -> str | None:
    """解決しない参照の説明（解決するか、まだ確かめられないなら None）。"""
    if r.status == MISSING:
        return "が存在しない id（どの分野のページにも、registry の候補にもない）"
    if r.status == MERGED:
        return f"は {where(r.entry)} で「{r.entry.text('into')}」にまとめた（まとめた先を指す）"
    if r.status == DROPPED:
        return f"は {where(r.entry)} で採らないことにした（dropped）"
    return None


def joined(values: Iterable[str]) -> str:
    return "・".join(values)


# ---- エラー（終了コードを 1 にする）


@check("YAML", ERROR)
def check_yaml(cat: Catalog) -> Iterator[Finding]:
    """YAML が読めない（構文の誤り）。同じキーが2回ある（後のものだけが読まれる）"""
    yield from loaded(cat, "YAML")


@check("形", ERROR)
def check_shape(cat: Catalog) -> Iterator[Finding]:
    """値の形が README §2・§3 と違う（リストのところが文字列、マッピングでない、wave が 1 でない、など）"""
    yield from loaded(cat, "形")
    reg = cat.registry
    if reg.raw is not None:
        for msg in shape_problems(reg.raw, REGISTRY_SHAPE):
            yield Finding(reg.file, line_of(reg.raw), "-", msg, ALWAYS)
        for e in reg.candidates:
            for msg in shape_problems(e.raw, CANDIDATE_SHAPE):
                yield at_entry(e, msg, cat.registry_fields(e))
        for e in reg.ledger:
            for msg in shape_problems(e.raw, LEDGER_SHAPE, "ledger の "):
                yield at_entry(e, msg)
    for ff in cat.files.values():
        if ff.raw is None:
            continue
        for msg in shape_problems(ff.raw, FILE_SHAPE):
            yield Finding(ff.file, line_of(ff.raw), "-", msg, frozenset({ff.field}))
        for e in ff.entries():
            for msg in shape_problems(e.raw, ENTRY_SHAPES[e.kind], f"{e.kind} の "):
                yield at_entry(e, msg, {ff.field})
    for p in cat.pages:
        for msg in shape_problems(p.raw, PAGE_SHAPE):
            yield at(p, msg)
        for key, shape in PART_SHAPES.items():
            for part in p.parts(key):
                for msg in shape_problems(part, shape, f"{key} の要素の "):
                    yield at(p, msg)


@check("必須", ERROR)
def check_required(cat: Catalog) -> Iterator[Finding]:
    """必須の項目がない：ページの id・title・type・priority・summary・volatility と、型による level
    （site.yml の types_without_level の型は書かない）。分野のファイルの field・pages、registry の pages・ledger と
    各項目の id・field・title、merged の id・into、signs の type・text、routes の cause・to、sections の title・anchor など"""
    reg = cat.registry
    if reg.raw is not None:
        for key in REGISTRY_REQUIRED:
            if is_missing(reg.raw, key):
                yield Finding(reg.file, None, "-", f"{key} がない", ALWAYS)
        for e in reg.candidates:
            for key in CANDIDATE_REQUIRED:
                if is_missing(e.raw, key):
                    yield at_entry(e, f"pages の項目に {key} がない", cat.registry_fields(e))
        for e in reg.ledger:
            for key in LEDGER_REQUIRED:
                if is_missing(e.raw, key):
                    yield at_entry(e, f"ledger の項目に {key} がない")
    for ff in cat.files.values():
        if ff.raw is None:
            continue
        for key in FILE_REQUIRED:
            if is_missing(ff.raw, key):
                yield Finding(ff.file, line_of(ff.raw), "-", f"{key} がない", frozenset({ff.field}))
        for e in ff.entries():
            for key in ENTRY_REQUIRED[e.kind]:
                if is_missing(e.raw, key):
                    yield at_entry(e, f"{e.kind} の項目に {key} がない", {ff.field})
    for p in cat.pages:
        for key in PAGE_REQUIRED:
            if is_missing(p.raw, key):
                yield at(p, f"{key} がない")
        if needs_level(cat.vocab, p) and is_missing(p.raw, "level"):
            yield at(p, f"level がない（type が {p.text('type')} のページは level を書く）")
        for key, required in PART_REQUIRED.items():
            for part in p.parts(key):
                for k in required:
                    if is_missing(part, k):
                        yield at(p, f"{key} の要素に {k} がない（{brief(part)}）")


@check("語彙", ERROR)
def check_vocab(cat: Catalog) -> Iterator[Finding]:
    """値が語彙（schema/site.yml）にない：type・level・priority・volatility・surfaces・principle・prevents・pitfalls・
    scenes、signs の type、routes の cause（prevents か pitfalls の値）、sections の level、visual と templates の kind、
    registry の候補の field・type・priority・level"""
    v = cat.vocab
    for p in cat.pages:
        for key, attr in PAGE_VOCAB.items():
            allowed = getattr(v, attr)
            if allowed is None:
                continue
            for x in p.strings(key):
                if x not in allowed:
                    yield at(p, f"{key} の「{x}」が語彙にない（{joined(allowed)}）")
        for (key, sub), attr in PART_VOCAB.items():
            allowed = getattr(v, attr)
            if allowed is None:
                continue
            for part in p.parts(key):
                x = part.get(sub)
                if isinstance(x, str) and x not in allowed:
                    yield at(p, f"{key} の {sub} の「{x}」が語彙にない（{joined(allowed)}）")
    for e in cat.registry.candidates:
        for key, attr in CANDIDATE_VOCAB.items():
            allowed, x = getattr(v, attr), e.raw.get(key)
            if allowed is not None and isinstance(x, str) and x not in allowed:
                yield at_entry(e, f"registry の {key} の「{x}」が語彙にない（{joined(allowed)}）", cat.registry_fields(e))


@check("id の書式", ERROR)
def check_id_format(cat: Catalog) -> Iterator[Finding]:
    """id が書式（英小文字・数字・ハイフン。^[a-z0-9]+(-[a-z0-9]+)*$）に合わない：ページ・registry の候補・ledger・
    merged・dropped・new_features・features.yaml の id と、sections の anchor"""
    for p in cat.pages:
        if p.id is not None and not ID_RE.match(p.id):
            yield at(p, f"id「{p.id}」が書式に合わない（英小文字・数字・ハイフン）")
        for sec in p.parts("sections"):
            a = sec.get("anchor")
            if isinstance(a, str) and a.strip() and not ID_RE.match(a):
                yield at(p, f"sections の anchor「{a}」が書式に合わない（英小文字・数字・ハイフン）")
    for e in cat.registry.candidates + cat.registry.ledger:
        if e.id is not None and not ID_RE.match(e.id):
            yield at_entry(e, f"registry の {e.kind} の id「{e.id}」が書式に合わない", cat.registry_fields(e))
    for ff in cat.files.values():
        for e in ff.entries():
            if e.id is not None and not ID_RE.match(e.id):
                yield at_entry(e, f"{e.kind} の id「{e.id}」が書式に合わない", {ff.field})
    yield from loaded(cat, "id の書式")


@check("id の重複", ERROR)
def check_duplicates(cat: Catalog) -> Iterator[Finding]:
    """同じ id が2つ以上ある：ページの id（分野をまたいで）、registry の候補と ledger の id、ページと merged・dropped の
    間（同じ候補を採り、かつまとめた、など）、ページの中の sections の anchor"""
    first: dict[str, Page] = {}
    for p in cat.pages:
        if p.id is None:
            continue
        q = first.setdefault(p.id, p)
        if q is not p:
            yield at(p, f"id「{p.id}」が {where(q)} にもある", q.field)
    places: dict[str, list[tuple[str, str, Entry | None]]] = collections.defaultdict(list)
    for p in cat.pages:
        if p.id is not None:
            places[p.id].append((f"pages（{where(p)}）", p.field, None))
    for ff in cat.files.values():
        for e in ff.merged + ff.dropped:
            if e.id is not None:
                places[e.id].append((f"{e.kind}（{where(e)}）", ff.field, e))
    for cid, pl in places.items():
        entries = [e for _, _, e in pl if e is not None]
        if entries and len(pl) > 1:
            yield at_entry(entries[0], f"「{cid}」が {joined(d for d, _, _ in pl)} にある（1か所にする）",
                           {f for _, f, _ in pl})
    for kind, items in (("pages", cat.registry.candidates), ("ledger", cat.registry.ledger)):
        seen: dict[str, Entry] = {}
        for e in items:
            if e.id is None:
                continue
            q = seen.setdefault(e.id, e)
            if q is not e:
                yield at_entry(e, f"registry の {kind} の id「{e.id}」が {where(q)} にもある", cat.registry_fields(e))
    for p in cat.pages:
        anchors = collections.Counter(p.anchors())
        for a, n in anchors.items():
            if n > 1:
                yield at(p, f"sections の anchor「{a}」が {n} つある")


@check("分野とファイル名", ERROR)
def check_field_names(cat: Catalog) -> Iterator[Finding]:
    """分野のファイルの field がファイル名と違う。planning/catalog/ に、分野の id（site.yml の fields）でない名前の
    .yaml がある（分野のファイルとして読まない）"""
    for path in cat.stray:
        yield Finding(path, None, "-", "ファイル名が分野の id（site.yml の fields）でないので、分野のファイルとして読んでいない",
                      ALWAYS)
    for ff in cat.files.values():
        if ff.raw is None:
            continue
        declared = ff.raw.get("field")
        if isinstance(declared, str) and declared.strip() and declared != ff.field:
            yield Finding(ff.file, line_of(ff.raw), "-", f"field「{declared}」がファイル名の分野（{ff.field}）と違う",
                          frozenset({ff.field}))


@check("参照", ERROR)
def check_refs(cat: Catalog) -> Iterator[Finding]:
    """prerequisites・related・routes の to・merged の into が解決しない：存在しない id、merged・dropped にした候補、
    related と routes の id#anchor の anchor が相手の sections にない"""
    for p in cat.pages:
        for key, ref in [*page_refs(p), *route_refs(p)]:
            if not ref.target:
                yield at(p, f"{key} に空の id がある（{ref.raw!r}）")
                continue
            r = cat.resolve(ref.target)
            problem = bad_target(r)
            if problem:
                yield at(p, f"{key} の「{ref.raw}」{problem}")
            elif key != "prerequisites" and ref.anchor is not None and r.status == PAGE:
                anchors = r.page.anchors()
                if ref.anchor not in anchors:
                    have = f"あるのは {joined(anchors)}" if anchors else "sections がない"
                    yield at(p, f"{key} の「{ref.raw}」: {r.page.id} の sections に anchor「{ref.anchor}」がない（{have}）")
    for ff in cat.files.values():
        for e in ff.merged:
            into = Ref.parse(e.text("into")).target
            if not into:
                continue
            if into == e.id:
                yield at_entry(e, f"merged の「{e.id}」を自分自身にまとめている", {ff.field})
                continue
            problem = bad_target(cat.resolve(into))
            if problem:
                yield at_entry(e, f"merged の into「{into}」{problem}", {ff.field})


def prerequisite_graph(cat: Catalog) -> dict[str, list[str]]:
    """前提のグラフ（ページの id → 前提のページの id。解決したものだけ）。"""
    graph: dict[str, list[str]] = {}
    for pid, p in cat.by_id.items():
        targets = [r.page.id for r in (cat.resolve(ref.target) for ref in p.refs("prerequisites")) if r.status == PAGE]
        graph[pid] = list(dict.fromkeys(targets))
    return graph


def strongly_connected(graph: dict[str, list[str]]) -> list[list[str]]:
    """強連結成分（Tarjan。再帰しない）。"""
    index: dict[str, int] = {}
    low: dict[str, int] = {}
    stack: list[str] = []
    on_stack: set[str] = set()
    result: list[list[str]] = []
    counter = 0
    for root in graph:
        if root in index:
            continue
        index[root] = low[root] = counter
        counter += 1
        stack.append(root)
        on_stack.add(root)
        work = [(root, iter(graph.get(root, ())))]
        while work:
            node, it = work[-1]
            pushed = False
            for nxt in it:
                if nxt not in index:
                    index[nxt] = low[nxt] = counter
                    counter += 1
                    stack.append(nxt)
                    on_stack.add(nxt)
                    work.append((nxt, iter(graph.get(nxt, ()))))
                    pushed = True
                    break
                if nxt in on_stack:
                    low[node] = min(low[node], index[nxt])
            if pushed:
                continue
            work.pop()
            if work:
                parent = work[-1][0]
                low[parent] = min(low[parent], low[node])
            if low[node] == index[node]:
                comp = []
                while True:
                    w = stack.pop()
                    on_stack.discard(w)
                    comp.append(w)
                    if w == node:
                        break
                result.append(comp)
    return result


def cycle_through(graph: dict[str, list[str]], start: str, members: set[str]) -> list[str]:
    """start を通る最短の循環（members の中だけをたどる）。"""
    parent: dict[str, str] = {}
    queue = collections.deque([start])
    seen = {start}
    while queue:
        u = queue.popleft()
        for v in graph.get(u, ()):
            if v == start:
                path = [u]
                while path[-1] != start:
                    path.append(parent[path[-1]])
                return list(reversed(path))
            if v in members and v not in seen:
                seen.add(v)
                parent[v] = u
                queue.append(v)
    return [start]


def prerequisite_targets(p: Page) -> list[str]:
    """前提の指す先のページの id（id#anchor はページの id にする。空と重複を除き、書いた順）。"""
    return list(dict.fromkeys(r.target for r in p.refs("prerequisites") if r.target))


def reached_from(graph: dict[str, list[str]], start: str, avoid: str | None = None) -> dict[str, str | None]:
    """start から前提をたどって届く id → その道でひとつ手前の id（start 自身は None）。幅優先なので最短の道になる。
    avoid は通らず、届いたことにもしない。一度見た id は二度たどらないので、循環があっても止まる。"""
    parent: dict[str, str | None] = {start: None}
    queue = collections.deque([start])
    while queue:
        u = queue.popleft()
        for v in graph.get(u, ()):
            if v != avoid and v not in parent:
                parent[v] = u
                queue.append(v)
    return parent


def path_to(parent: dict[str, str | None], end: str) -> list[str]:
    """reached_from の結果から、start から end までの道。"""
    path = [end]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return path[::-1]


@check("循環", ERROR)
def check_cycles(cat: Catalog) -> Iterator[Finding]:
    """前提（prerequisites）が循環している（自分自身を前提にするものも）"""
    graph = prerequisite_graph(cat)
    order = {pid: i for i, pid in enumerate(cat.by_id)}
    for comp in strongly_connected(graph):
        if len(comp) == 1 and comp[0] not in graph[comp[0]]:
            continue
        start = min(comp, key=order.__getitem__)
        cycle = cycle_through(graph, start, set(comp))
        rest = len(comp) - len(cycle)
        more = f"（ほかに {rest} ページが同じ循環に入る）" if rest > 0 else ""
        p = cat.by_id[start]
        yield Finding(p.file, p.line, p.label, "前提が循環している: " + " → ".join(cycle + [start]) + more,
                      frozenset(cat.by_id[x].field for x in comp))


@check("前提と関連の重複", ERROR)
def check_overlap(cat: Catalog) -> Iterator[Finding]:
    """同じページが prerequisites と related の両方にある。同じ id が同じリストに2回ある"""
    for p in cat.pages:
        pre = [r.target for r in p.refs("prerequisites")]
        for key, items in (("prerequisites", pre), ("related", [r.raw.strip() for r in p.refs("related")])):
            for x, n in collections.Counter(items).items():
                if x and n > 1:
                    yield at(p, f"{key} に「{x}」が {n} 回ある")
        for t in dict.fromkeys(r.target for r in p.refs("related")):
            if t and t in pre:
                yield at(p, f"「{t}」が prerequisites と related の両方にある（related から外す）")


@check("routes", ERROR)
def check_routes(cat: Catalog) -> Iterator[Finding]:
    """routes（症状のページの、原因ごとの振り分け先）を symptom でないページが持っている。routes の to が空
    （cause の語彙は「語彙」、to の解決は「参照」、cause・to がないものは「必須」が出す）"""
    types = cat.vocab.types
    for p in cat.pages:
        if p.raw.get("routes") is None:
            continue
        t = p.text("type")
        if t != SYMPTOM_TYPE and types is not None and t in types:   # type がない・語彙にないときは、ほかのエラーが出る
            yield at(p, f"routes は type が {SYMPTOM_TYPE} のページだけが持つ（このページは {t}。ほかのページへの道は related に書く）")
        for i, route in enumerate(p.parts("routes")):
            if route.get("to") == []:
                yield at(p, f"{route_label(route, i)}の to が空（振り分け先のページを1件以上書く）")


# ---- 警告（終了コードは変えない）


@check("参照の書き方", WARNING)
def check_ref_style(cat: Catalog) -> Iterator[Finding]:
    """prerequisites に id#anchor がある（前提はページの id で書く。節を指すのは related）。related に自分自身がある"""
    for p in cat.pages:
        for ref in p.refs("prerequisites"):
            if ref.anchor is not None:
                yield at(p, f"prerequisites の「{ref.raw}」に #anchor がある（前提はページの id で書く）")
        for ref in p.refs("related"):
            if p.id is not None and ref.target == p.id:
                yield at(p, f"related に自分自身「{ref.raw}」がある")


@check("未処理の候補", WARNING)
def check_unprocessed(cat: Catalog) -> Iterator[Finding]:
    """prerequisites・related・routes の to・merged の into が指す registry の候補が、その分野のファイル（はある）の
    pages・merged・dropped のどこにもない（その分野が書きかけなら、後で解決する）"""
    def message(r: Resolution) -> str:
        f = r.entry.text("field")
        return f"は registry の候補だが、{f}.yaml の pages・merged・dropped のどこにもない（{f} が書きかけなら後で解決する）"

    for p in cat.pages:
        for key, ref in [*page_refs(p), *route_refs(p)]:
            r = cat.resolve(ref.target) if ref.target else None
            if r is not None and r.status == UNPROCESSED:
                yield at(p, f"{key} の「{ref.raw}」{message(r)}", r.field)
    for ff in cat.files.values():
        for e in ff.merged:
            into = Ref.parse(e.text("into")).target
            r = cat.resolve(into) if into else None
            if r is not None and r.status == UNPROCESSED:
                yield at_entry(e, f"merged の into「{into}」{message(r)}", {ff.field, r.field or ff.field})


@check("レベルの逆転", WARNING)
def check_level_inversion(cat: Catalog) -> Iterator[Finding]:
    """前提のページの level が、そのページの level より上の段（site.yml の levels の順）。routes の先は見ない
    （上の段の対処も振り分け先に置ける。catalog/README §4.4 の6）"""
    rank = cat.vocab.level_rank
    for p in cat.pages:
        lv = p.text("level")
        if lv not in rank:
            continue
        for ref in p.refs("prerequisites"):
            r = cat.resolve(ref.target)
            if r.status != PAGE:
                continue
            q = r.page.text("level")
            if q in rank and rank[q] > rank[lv]:
                yield at(p, f"前提「{r.page.id}」の level（{q}）がこのページ（{lv}）より上の段")


@check("必須の前提", WARNING)
def check_required_prerequisites(cat: Catalog) -> Iterator[Finding]:
    """必須（site.yml の priorities の最初）のページの前提が必須でない。routes の先は見ない（推奨の対処も振り分け先に
    置ける）"""
    v = cat.vocab
    top = v.top_priority
    if top is None:
        return
    for p in cat.pages:
        if p.text("priority") != top:
            continue
        for ref in p.refs("prerequisites"):
            r = cat.resolve(ref.target)
            q = r.page.text("priority") if r.status == PAGE else ""
            if q and q != top and q in (v.priorities or []):
                yield at(p, f"前提「{r.page.id}」の priority が {q}（{top}のページの前提は{top}にする）", r.page.field)


@check("推移的な前提", WARNING)
def check_transitive_prerequisites(cat: Catalog) -> Iterator[Finding]:
    """prerequisites に、同じページのほかの前提から前提をたどって届くものがある（README §4.4 の1「推移的に届くものは
    書かない」）。どの前提から届くかを道筋で出す。id#anchor はページの id で比べ、そのページ自身を通る道は数えない

    たどるのは分野のファイルにあるページの prerequisites だけ。ファイルのまだない分野の候補などは、ほかのページの
    前提に書いてあれば届いたことにするが、その先はたどらない。前提が循環していても止まる（循環そのものは「循環」の
    エラーが出す。自分を通る道を数えないのは、循環のせいでほかの前提がすべて届くように見えるのを避けるため）。"""
    graph = {pid: prerequisite_targets(p) for pid, p in cat.by_id.items()}
    for p in cat.pages:
        pre = [t for t in prerequisite_targets(p) if t != p.id]
        if len(pre) < 2:
            continue
        reach = {y: reached_from(graph, y, avoid=p.id) for y in pre}
        for x in pre:
            via = [y for y in pre if y != x and x in reach[y]]
            if via:
                paths = "、".join(" → ".join(path_to(reach[y], x)) for y in via)
                yield at(p, f"前提「{x}」は、ほかの前提「{'」「'.join(via)}」からたどって届く: {paths}"
                            "（推移的に届く前提は書かない。要るなら related に移す）")


@check("比例則", WARNING)
def check_proportional(cat: Catalog) -> Iterator[Finding]:
    """site.yml の proportional_rule の levels（任せる・仕組みにする・回す）のページが、guard_fields（verify・eval・enforce・
    safety）の分野のページを前提にも関連にも持たない（guard_fields の分野のページは除く。まだない分野の候補は registry
    の分野で数える。routes の先は数えない）。任せる幅を広げる内容のページだけが対象なので、そうでないページは notes に
    理由を書いて残してよい"""
    v = cat.vocab
    levels, guards = set(v.proportional_levels), set(v.guard_fields)
    if not levels or not guards:
        return
    for p in cat.pages:
        lv = p.text("level")
        if lv not in levels or p.field in guards:
            continue
        targets = {cat.resolve(ref.target).field for _, ref in page_refs(p) if ref.target}
        if not targets & guards:
            yield at(p, f"level が {lv} だが、{joined(v.guard_fields)} の分野のページを前提にも関連にも持たない"
                        "（任せる幅を広げる内容なら足す）")


@check("入ってくる道", WARNING)
def check_incoming(cat: Catalog) -> Iterator[Finding]:
    """どのページの prerequisites・related・routes にも出てこない（入ってくる道がない）。入口の分野（site.yml の
    entry_fields。なければ fields の最初の start）は除く。症状のページの routes の先は、診断の節から道があるので数える"""
    incoming: set[str] = set()
    for p in cat.pages:
        for _, ref in [*page_refs(p), *route_refs(p)]:
            r = cat.resolve(ref.target) if ref.target else None
            if r is not None and r.status == PAGE and r.page.id != p.id:
                incoming.add(r.page.id)
    absent = [f for f in cat.vocab.fields if f not in cat.files]
    later = f"。まだファイルのない {len(absent)} 分野からの参照は数えていない" if absent else ""
    for pid, p in cat.by_id.items():
        if p.field not in cat.vocab.entry_fields and pid not in incoming:
            yield at(p, f"どのページの prerequisites・related・routes にも出てこない（入ってくる道がない{later}）")


def count_sentences(s: str) -> int:
    """かっこの外の「。」で文を数える（最後の「。」の後に文字が残れば、それも1文）。"""
    depth, n, tail = 0, 0, False
    for ch in s:
        if ch in "（(「『":
            depth += 1
        elif ch in "）)」』":
            depth = max(0, depth - 1)
        if ch == "。" and depth == 0:
            n += 1
            tail = False
        elif not ch.isspace():
            tail = True
    return n + (1 if tail else 0)


@check("summary", WARNING)
def check_summary(cat: Catalog) -> Iterator[Finding]:
    """summary が site.yml の summary_max_chars より長い、3文以上ある、site.yml の summary_banned_words の語を使っている"""
    v = cat.vocab
    for p in cat.pages:
        s = p.text("summary")
        if not s:
            continue
        if v.summary_max_chars is not None and len(s) > v.summary_max_chars:
            yield at(p, f"summary が {len(s)} 字（{v.summary_max_chars} 字まで）")
        n = count_sentences(s)
        if n > MAX_SUMMARY_SENTENCES:
            yield at(p, f"summary が {n} 文（{MAX_SUMMARY_SENTENCES} 文まで）")
        bad = [w for w in v.summary_banned_words if w in s]
        if bad:
            yield at(p, f"summary に使わない語がある: 「{'」「'.join(bad)}」")


@check("症状の signs", WARNING)
def check_symptom_signs(cat: Catalog) -> Iterator[Finding]:
    """symptom のページの signs に、type が symptom のサインが2つ以上ない"""
    for p in cat.pages:
        if p.text("type") != SYMPTOM_TYPE:
            continue
        n = sum(1 for s in p.parts("signs") if s.get("type") == SYMPTOM_SIGN)
        if n < MIN_SYMPTOM_SIGNS:
            yield at(p, f"signs のうち type が {SYMPTOM_SIGN} のものが {n} つ（{MIN_SYMPTOM_SIGNS} つ以上にする）")


def sign_key(text: str) -> str:
    """signs の文を比べる形：NFKC で全角と半角をそろえ、空白と記号を除く。記号は Unicode の分類が句読点（P）・記号（S）・
    区切り（Z）・制御など（C）の文字（「」『』、。・,.!?！？（）() など）。長音「ー」や「々」は文字なので残す。"""
    return "".join(ch for ch in unicodedata.normalize("NFKC", text) if unicodedata.category(ch)[0] not in "PSZC")


@check("逆引きの重複", WARNING)
def check_reverse_index_overlap(cat: Catalog) -> Iterator[Finding]:
    """症状（symptom）のページの signs の文と、空白と記号を除いて同じ文が、ほかのページの signs にある（README §4.5 の4。
    逆引きで同じ困りごとが二か所に出る）。ほかのページの側に、どの症状のページのどの文と同じかを出す

    signs の type は問わない。症状のページでないページどうしの同じ文は指摘しない（逆引きで並べるために、そろえて
    よい）。症状のページどうしで同じ文があれば、両方のページに出す。"""
    owners: dict[str, list[tuple[Page, str]]] = collections.defaultdict(list)   # 比べる形 → (症状のページ, 文)
    for s in cat.pages:
        if s.text("type") != SYMPTOM_TYPE:
            continue
        for sign in s.parts("signs"):
            text = as_text(sign.get("text"))
            key = sign_key(text)
            if key and all(q is not s for q, _ in owners[key]):
                owners[key].append((s, text))
    for p in cat.pages:
        for sign in p.parts("signs"):
            text = as_text(sign.get("text"))
            key = sign_key(text)
            hits = [(s, t) for s, t in owners.get(key, ()) if s is not p] if key else []
            if not hits:
                continue
            relation = "と同じ" if all(t == text for _, t in hits) else "と、空白と記号を除くと同じ"
            if p.text("type") == SYMPTOM_TYPE:
                hint = "症状のページどうしで重なっている。どちらの症状のページで受けるかを決める"
            else:
                hint = "逆引きで同じ困りごとが二か所に出る。対処のページには、より狭い場面の困りごとか、やりたいことの形で置く"
            hit_text = "、".join(f"{s.label} の sign「{t}」" for s, t in hits)
            yield at(p, f"signs の「{text}」が、症状のページ {hit_text}{relation}（{hint}）", *(s.field for s, _ in hits))


@check("症状の prevents", WARNING)
def check_symptom_prevents(cat: Catalog) -> Iterator[Finding]:
    """symptom のページの prevents が空"""
    for p in cat.pages:
        if p.text("type") == SYMPTOM_TYPE and not p.strings("prevents"):
            yield at(p, f"{SYMPTOM_TYPE} のページの prevents が空（防ぐ・診断する原因を1つ以上書く）")


@check("症状の前提", WARNING)
def check_symptom_prerequisites(cat: Catalog) -> Iterator[Finding]:
    """symptom のページの前提の type が concept・guide・hub でない（症状のページの前提は、診断を読むのに要る概念の
    ページだけにする。対処のページは routes に置く。catalog/README §4.4 の6）

    見るのは分野のファイルにある前提のページだけ。type がない・語彙にない前提は、そのページのエラーが出るので見ない。"""
    types = cat.vocab.types
    allowed = joined(SYMPTOM_PREREQUISITE_TYPES)
    for p in cat.pages:
        if p.text("type") != SYMPTOM_TYPE:
            continue
        for t in prerequisite_targets(p):
            r = cat.resolve(t)
            q = r.page.text("type") if r.status == PAGE else ""
            if q and q not in SYMPTOM_PREREQUISITE_TYPES and (types is None or q in types):
                yield at(p, f"前提「{t}」の type が {q}（症状のページの前提は、診断を読むのに要る {allowed} のページだけに"
                            "する。対処のページは routes に置く）")


@check("症状の routes", WARNING)
def check_symptom_routes(cat: Catalog) -> Iterator[Finding]:
    """symptom のページに routes（原因ごとの振り分け先）がない"""
    for p in cat.pages:
        if p.text("type") == SYMPTOM_TYPE and not p.parts("routes"):
            yield at(p, f"{SYMPTOM_TYPE} のページに routes がない（原因ごとに、中心の対処のページを1〜{MAX_ROUTE_TARGETS} 件、"
                        "近い順に書く）")


@check("routes と原因", WARNING)
def check_route_causes(cat: Catalog) -> Iterator[Finding]:
    """routes の cause が、そのページの prevents・pitfalls にない。そのページの prevents・pitfalls の原因に routes がない
    （routes と prevents の両方を書いた symptom のページだけを見る）

    語彙にない cause は「語彙」のエラーが出るので見ない（site.yml の prevents か pitfalls が読めなければ、この検査を
    しない）。対処のページがない原因は、notes に理由を書いて残してよい。"""
    causes = cat.vocab.causes
    if causes is None:
        return
    for p in cat.pages:
        routes = p.parts("routes")
        prevents, pitfalls = p.strings("prevents"), p.strings("pitfalls")
        if p.text("type") != SYMPTOM_TYPE or not routes or not prevents:
            continue
        routed = list(dict.fromkeys(c for c in (as_text(r.get("cause")) for r in routes) if c in causes))
        for c in routed:
            if c not in prevents and c not in pitfalls:
                yield at(p, f"routes の cause「{c}」が、このページの prevents・pitfalls にない（診断で問う原因に足すか、"
                            "routes から外す）")
        for key, values in (("prevents", prevents), ("pitfalls", pitfalls)):
            for c in dict.fromkeys(values):
                if c not in routed and c in causes:
                    yield at(p, f"{key} の「{c}」に routes がない（その原因の中心の対処を routes に書く。対処のページが"
                                "ない原因なら、notes に書く）")


@check("routes の重なり", WARNING)
def check_route_overlap(cat: Catalog) -> Iterator[Finding]:
    """routes に同じ cause が2回ある。1つの cause の to に同じ id が2回ある。routes の先のページが、同じページの
    prerequisites か related にもある（ページの id で比べる。related には routes にない近いページだけを置く）"""
    for p in cat.pages:
        routes = p.parts("routes")
        if not routes:
            continue
        for c, n in collections.Counter(as_text(r.get("cause")) for r in routes).items():
            if c and n > 1:
                yield at(p, f"routes の cause「{c}」が {n} 回ある（1つにまとめる）")
        for i, route in enumerate(routes):
            for x, n in collections.Counter(s.strip() for s in as_strings(route.get("to"))).items():
                if x and n > 1:
                    yield at(p, f"{route_label(route, i)}の to に「{x}」が {n} 回ある")
        pre = set(prerequisite_targets(p))
        rel = {r.target for r in p.refs("related") if r.target}
        for t in dict.fromkeys(ref.target for _, ref in route_refs(p) if ref.target):
            if t in pre:
                yield at(p, f"routes の先「{t}」が prerequisites にもある（どちらか一方にする。前提は、診断を読むのに要る概念の"
                            "ページだけ）")
            if t in rel:
                yield at(p, f"routes の先「{t}」が related にもある（related から外す。related には、routes にない近いページ"
                            "だけを置く）")


@check("routes の数", WARNING)
def check_route_counts(cat: Catalog) -> Iterator[Finding]:
    """routes の1つの cause の to が4件以上（原因ごとに、中心の対処を3件まで）"""
    for p in cat.pages:
        for i, route in enumerate(p.parts("routes")):
            n = len(as_strings(route.get("to")))
            if n > MAX_ROUTE_TARGETS:
                yield at(p, f"{route_label(route, i)}の to が {n} 件（中心の対処を {MAX_ROUTE_TARGETS} 件までにする。"
                            "ほかは related に置く）")


@check("機能の tracks", WARNING)
def check_feature_tracks(cat: Catalog) -> Iterator[Finding]:
    """feature のページの tracks が空"""
    for p in cat.pages:
        if p.text("type") == FEATURE_TYPE and not p.strings("tracks"):
            yield at(p, f"{FEATURE_TYPE} のページの tracks が空（README §5 の機能の id を書く）")


@check("tracks の id", WARNING)
def check_track_ids(cat: Catalog) -> Iterator[Finding]:
    """tracks の id が、機能の id の表（features.yaml か README §5）にも、どの分野のファイルの new_features にもない"""
    if cat.feature_ids is None:
        return
    known = cat.feature_ids | cat.new_feature_ids
    for p in cat.pages:
        for t in p.strings("tracks"):
            if t not in known:
                yield at(p, f"tracks の「{t}」が機能の id の表（{cat.feature_source}）にも new_features にもない"
                            "（足すなら new_features に書く）")


@check("outdated_advice の id", WARNING)
def check_outdated_advice(cat: Catalog) -> Iterator[Finding]:
    """outdated_advice の id が registry の ledger にない"""
    reg = cat.registry
    if reg.raw is None or not isinstance(reg.raw.get("ledger"), list):
        return
    ledger = reg.ledger_ids
    for p in cat.pages:
        for a in p.strings("outdated_advice"):
            if a not in ledger:
                yield at(p, f"outdated_advice の「{a}」が registry の ledger にない")


@check("registry の候補", WARNING)
def check_registry_coverage(cat: Catalog) -> Iterator[Finding]:
    """registry の候補が、その分野のファイルの pages・merged・dropped のどこにもない（分野のファイルがあるときだけ）。
    registry の分野と違う分野のファイルにある。merged・dropped の id が registry の候補にない"""
    reg = cat.registry
    if reg.raw is None:
        return
    placed: dict[str, list[str]] = collections.defaultdict(list)    # id → 置いた分野
    for ff in cat.files.values():
        for x in [p.id for p in ff.pages] + [e.id for e in ff.merged + ff.dropped]:
            if x is not None and ff.field not in placed[x]:
                placed[x].append(ff.field)
    for cid, e in reg.by_id.items():
        f = e.text("field")
        ff = cat.files.get(f)
        if ff is None or not ff.readable or f in placed.get(cid, []):
            continue
        title = f"「{e.text('title')}」" if e.text("title") else ""
        if placed.get(cid):
            others = placed[cid]
            yield Finding(ff.file, None, cid, f"registry では {f} の候補{title}だが、{joined(o + '.yaml' for o in others)} "
                                              "にある（registry を直すか、open_issues の提案にする）", frozenset([f, *others]))
        else:
            yield Finding(ff.file, None, cid, f"registry の候補{title}が pages・merged・dropped のどこにもない",
                          frozenset({f}))
    known = reg.by_id
    for ff in cat.files.values():
        for e in ff.merged + ff.dropped:
            if e.id is not None and e.id not in known:
                yield at_entry(e, f"{e.kind} の「{e.id}」が registry の候補にない", {ff.field})


def marked_new(cat: Catalog, p: Page) -> bool:
    """registry にないページに「新規」の印があるか（ページの notes、またはファイル・registry の notes にその id と一緒に）。"""
    if any(NEW_MARK in str(x) for x in as_list(p.raw.get("notes"))):
        return True
    ff = cat.files.get(p.field)
    notes = [str(x) for x in as_list(ff.raw.get("notes"))] if ff is not None and ff.raw else []
    return any(NEW_MARK in x and p.id in x for x in notes + cat.registry.notes())


@check("registry にない id", WARNING)
def check_new_ids(cat: Catalog) -> Iterator[Finding]:
    """分野のファイルのページの id が registry の候補になく、notes に「新規」の印もない"""
    if cat.registry.raw is None:
        return
    for p in cat.pages:
        if p.id is not None and p.id not in cat.candidates and not marked_new(cat, p):
            yield at(p, f"registry の候補にない id（新しいページなら、notes に「{NEW_MARK}：理由」と書く）")


@check("前提と関連の数", WARNING)
def check_counts(cat: Catalog) -> Iterator[Finding]:
    """prerequisites が5つ以上（直接の前提だけを4つまで）。related が21件以上（20件まで）"""
    for p in cat.pages:
        n = len(dict.fromkeys(r.target for r in p.refs("prerequisites")))
        if n > MAX_PREREQUISITES:
            yield at(p, f"prerequisites が {n} 個（直接の前提だけを {MAX_PREREQUISITES} つまで）")
        m = len(p.refs("related"))
        if m > MAX_RELATED:
            yield at(p, f"related が {m} 件（{MAX_RELATED} 件まで）")


@check("id の分野名", WARNING)
def check_field_prefix(cat: Catalog) -> Iterator[Finding]:
    """ページと registry の候補の id が、自分の分野の名前で始まる（README §2「分野の名前を頭に付けない」。
    ほかの分野の名前で始まる id は見ない。basics の context-rot は用語そのもの）"""
    def prefixed(pid: str | None, field: str) -> bool:
        return bool(pid and field) and (pid == field or pid.startswith(field + "-"))

    for p in cat.pages:
        if prefixed(p.id, p.field):
            yield at(p, f"id「{p.id}」が分野の名前「{p.field}」で始まる（分野の名前を頭に付けない）")
    for e in cat.registry.candidates:
        if prefixed(e.id, e.text("field")):
            yield at_entry(e, f"registry の id「{e.id}」が分野の名前「{e.text('field')}」で始まる", cat.registry_fields(e))


@check("知らない項目", WARNING)
def check_unknown_keys(cat: Catalog) -> Iterator[Finding]:
    """README §2・§3 の形にない項目がある（綴りの誤りだと、その項目の検査が素通りになる）"""
    reg = cat.registry
    if reg.raw is not None:
        for k in unknown_keys(reg.raw, REGISTRY_SHAPE):
            yield Finding(reg.file, line_of(reg.raw), "-", f"知らない項目「{k}」")
    for ff in cat.files.values():
        if ff.raw is None:
            continue
        for k in unknown_keys(ff.raw, FILE_SHAPE):
            yield Finding(ff.file, line_of(ff.raw), "-", f"知らない項目「{k}」", frozenset({ff.field}))
        for e in ff.entries():
            for k in unknown_keys(e.raw, ENTRY_SHAPES[e.kind]):
                yield at_entry(e, f"{e.kind} の知らない項目「{k}」", {ff.field})
    for p in cat.pages:
        for k in unknown_keys(p.raw, PAGE_SHAPE):
            yield at(p, f"知らない項目「{k}」")
        for key, shape in PART_SHAPES.items():
            for part in p.parts(key):
                for k in unknown_keys(part, shape):
                    yield at(p, f"{key} の要素の知らない項目「{k}」")


@check("章", WARNING)
def check_chapters(cat: Catalog) -> Iterator[Finding]:
    """ページの chapter がファイルの chapters にない。chapters の章にページがない"""
    for ff in cat.files.values():
        chapters = ff.raw.get("chapters") if ff.raw is not None else None
        if not isinstance(chapters, list):
            continue
        names = [c for c in chapters if isinstance(c, str)]
        used: set[str] = set()
        for p in ff.pages:
            c = p.text("chapter")
            if c:
                used.add(c)
                if c not in names:
                    yield at(p, f"chapter「{c}」が chapters（{joined(names)}）にない")
        for c in names:
            if c not in used:
                yield Finding(ff.file, line_of(ff.raw), "-", f"chapters の「{c}」の章にページがない", frozenset({ff.field}))


@check("level の付け方", WARNING)
def check_level_usage(cat: Catalog) -> Iterator[Finding]:
    """level を持たない型（site.yml の types_without_level）や分野（fields_without_level）のページに level がある。
    sections の level がページの level より下の段"""
    v = cat.vocab
    rank = v.level_rank
    for p in cat.pages:
        t, lv = p.text("type"), p.text("level")
        if lv and (t in v.types_without_level or p.field in v.fields_without_level):
            why = f"type が {t} の" if t in v.types_without_level else f"{p.field} の分野の"
            yield at(p, f"{why}ページは level を書かない（いまは {lv}）")
        if lv in rank:
            for sec in p.parts("sections"):
                s = sec.get("level")
                if isinstance(s, str) and s in rank and rank[s] < rank[lv]:
                    yield at(p, f"sections の「{as_text(sec.get('title'))}」の level（{s}）がページ（{lv}）より下の段")


@check("wave", WARNING)
def check_wave(cat: Catalog) -> Iterator[Finding]:
    """第一波の核の分野（site.yml の first_wave_core_fields）でないページに wave: 1 がある。核の分野のファイルに
    wave: 1 のページがない。入口の分野（entry_fields）のページと症状（symptom）のページに wave: 1 がない（核の分野の
    ものは全ページに付ける。catalog/README §4.6 の2）"""
    core = cat.vocab.first_wave_core_fields
    if not core:
        return
    for p in cat.pages:
        if p.is_wave and p.field not in core:
            yield at(p, f"wave: 1 は第一波の核の分野（{joined(core)}）のページにだけ付ける")
        elif (not p.is_wave and p.field in core
              and (p.field in cat.vocab.entry_fields or p.text("type") == SYMPTOM_TYPE)):
            yield at(p, "wave: 1 がない（入口の分野のページと症状のページは、全ページに付ける）")
    for f in core:
        ff = cat.files.get(f)
        if ff is not None and ff.pages and not any(p.is_wave for p in ff.pages):
            yield Finding(ff.file, None, "-", "第一波の核の分野なのに wave: 1 のページがない（総論と、多くのページが前提にする"
                                              "ページに付ける）", frozenset({f}))


@check("設定", WARNING)
def check_config(cat: Catalog) -> Iterator[Finding]:
    """検査の材料が足りない（registry.yaml がない、site.yml に語彙がない、機能の id の表がない、など）。足りない分の
    検査はしない。site.yml の first_wave が読めない、first_wave の named がページを指していない"""
    yield from loaded(cat, "設定")
    for x in cat.vocab.first_wave_named:
        ref = Ref.parse(x)
        r = cat.resolve(ref.target)
        problem = bad_target(r)
        if problem:
            yield Finding(SITE_YML, None, "-", f"site.yml の first_wave の named の「{x}」{problem}（第一波に数えない）", ALWAYS)
        elif ref.anchor is not None and r.status == PAGE and ref.anchor not in r.page.anchors():
            yield Finding(SITE_YML, None, "-", f"site.yml の first_wave の named の「{x}」: {r.page.id} の sections に "
                                               f"anchor「{ref.anchor}」がない（ページは第一波に数える）", ALWAYS)

# ============================================================================
# 集計（--stats）
# ============================================================================


@dataclass(frozen=True)
class Lacking:
    """核の症状のページの routes のうち、to に必須の先がない cause（first では、そこから何も入れない）。"""

    page: Page
    cause: str                 # cause の値（なければ「N 番目」）
    targets: tuple[str, ...]   # to の先のページの id


@dataclass
class FirstWave:
    """第一波の数（catalog/README §4.6 の3）。内訳は、核 → 前提 → routes → named の順に足したときに新しく増えるページ。"""

    mode: str                  # routes の数え方（FIRST_WAVE_ROUTES のどれか）
    core: list[Page]           # wave: 1 のページ
    prerequisites: list[Page]  # 核から前提でたどって届くもの
    routes: list[Page]         # routes から：核の症状のページの routes の先と、その前提でたどって新しく届くもの
    named: list[Page]          # named から：site.yml の first_wave の named と、その前提でたどって新しく届くもの
    unresolved: list[str]      # たどれない候補（分野のファイルにまだない候補の id）
    lacking: list[Lacking]     # 必須の先がない cause（数え方によらず、核の症状のページの routes を見る）

    @property
    def pages(self) -> list[Page]:
        return self.core + self.prerequisites + self.routes + self.named


def target_priority(cat: Catalog, target: str) -> str:
    """参照の先の priority（ページならページの、分野のファイルにまだない候補なら registry の見当）。"""
    r = cat.resolve(target)
    if r.status == PAGE:
        return r.page.text("priority")
    if r.status in (PENDING, UNPROCESSED) and r.entry is not None:
        return r.entry.text("priority")
    return ""


def route_seeds(cat: Catalog, p: Page, mode: str) -> tuple[list[str], list[Lacking]]:
    """症状のページの routes から第一波の種にする先のページの id と、必須の先がない cause。first は各 cause の to のうち
    最初の必須（site.yml の priorities の最初）の先、all は全部、none は無し。id#anchor はページの id にする。"""
    if p.text("type") != SYMPTOM_TYPE:
        return [], []
    top = cat.vocab.top_priority
    seeds: list[str] = []
    lacking: list[Lacking] = []
    for i, route in enumerate(p.parts("routes")):
        targets = list(dict.fromkeys(t for t in (Ref.parse(s).target for s in as_strings(route.get("to"))) if t))
        required = [t for t in targets if top is None or target_priority(cat, t) == top]
        if not required:
            lacking.append(Lacking(p, as_text(route.get("cause")) or f"{i + 1} 番目", tuple(targets)))
        seeds += targets if mode == "all" else required[:1] if mode == "first" else []
    return list(dict.fromkeys(seeds)), lacking


def first_wave(cat: Catalog, mode: str | None = None) -> FirstWave:
    """第一波（閉包）：wave: 1 のページ（核）と、核の症状のページの routes の先（mode。省くと site.yml の first_wave の
    routes）と、site.yml の first_wave の named を種にし、そこから prerequisites でたどって届くページをすべて入れる。"""
    mode = cat.vocab.first_wave_routes if mode is None else mode
    core = [p for p in cat.by_id.values() if p.is_wave]
    seen = {p.id for p in core}
    unresolved: list[str] = []

    def grow(seeds: Iterable[str], expand: Iterable[Page] = ()) -> list[Page]:
        """seeds と、そこ（と expand のページ）から前提でたどって新しく届くページ。"""
        added: list[Page] = []
        queue = collections.deque(expand)

        def visit(target: str) -> None:
            r = cat.resolve(target)
            if r.status == PAGE:
                if r.page.id not in seen:
                    seen.add(r.page.id)
                    added.append(r.page)
                    queue.append(r.page)
            elif r.status in (PENDING, UNPROCESSED) and target not in unresolved:
                unresolved.append(target)

        for t in seeds:
            visit(t)
        while queue:
            for t in prerequisite_targets(queue.popleft()):
                visit(t)
        return added

    picks = [route_seeds(cat, p, mode) for p in core]
    reached = grow((), expand=core)
    routed = grow(t for seeds, _ in picks for t in seeds)
    named = grow(Ref.parse(x).target for x in cat.vocab.first_wave_named)
    return FirstWave(mode, core, reached, routed, named, unresolved, [x for _, lack in picks for x in lack])


COVERAGE = ("採る", "まとめた", "採らない", "ほかの分野", "未処理")


@dataclass
class FieldStats:
    pages: int = 0
    priority: collections.Counter = dc_field(default_factory=collections.Counter)
    level: collections.Counter = dc_field(default_factory=collections.Counter)
    type: collections.Counter = dc_field(default_factory=collections.Counter)
    candidates: int = 0
    coverage: collections.Counter = dc_field(default_factory=collections.Counter)

    def add(self, other: FieldStats) -> None:
        self.pages += other.pages
        self.candidates += other.candidates
        for name in ("priority", "level", "type", "coverage"):
            getattr(self, name).update(getattr(other, name))


def field_stats(cat: Catalog, field: str) -> FieldStats:
    st = FieldStats()
    ff = cat.files.get(field)
    for p in ff.pages if ff is not None else []:
        st.pages += 1
        st.priority[p.text("priority") or "なし"] += 1
        st.level[p.text("level") or "なし"] += 1
        st.type[p.text("type") or "なし"] += 1
    own = {p.id for p in ff.pages} if ff is not None else set()
    for cid, e in cat.candidates.items():
        if e.text("field") != field:
            continue
        st.candidates += 1
        if ff is None or not ff.readable:
            continue
        if cid in own:
            st.coverage["採る"] += 1
        elif cid in cat.merged_ids:
            st.coverage["まとめた"] += 1
        elif cid in cat.dropped_ids:
            st.coverage["採らない"] += 1
        elif cid in cat.by_id:
            st.coverage["ほかの分野"] += 1
        else:
            st.coverage["未処理"] += 1
    return st


def counts(counter: collections.Counter, order: Iterable[str] = ()) -> str:
    order = list(order)
    keys = [k for k in order if counter.get(k)] + sorted(k for k in counter if k not in order and counter[k])
    return joined(f"{k} {counter[k]}" for k in keys) or "なし"


def format_field_stats(cat: Catalog, st: FieldStats, has_file: bool = True) -> str:
    v = cat.vocab
    cand = f"registry の候補 {st.candidates}" + (f"（{counts(st.coverage, COVERAGE)}）" if st.coverage else "")
    if not has_file:
        return f"ファイルなし｜{cand}"
    return (f"{st.pages} ページ｜優先度 {counts(st.priority, v.priorities or [])}｜"
            f"レベル {counts(st.level, (v.levels or []) + ['なし'])}｜型 {counts(st.type, v.types or [])}｜{cand}")


def format_first_wave(cat: Catalog, only: str | None = None) -> list[str]:
    """第一波の行：数と内訳（wave: 1・前提でたどって届くもの・routes から・named から）、routes の数え方ごとの数、
    必須の先がない cause、たどれない候補。only のときは、全体でたどってから、その分野のページを数える（cause は全体）。"""
    fw = first_wave(cat)
    alt = {m: first_wave(cat, m).pages for m in FIRST_WAVE_ROUTES}

    def n(pages: list[Page]) -> int:
        return sum(1 for p in pages if only is None or p.field == only)

    parts = (f"wave: 1 が {n(fw.core)}、前提でたどって届くもの {n(fw.prerequisites)}、routes から {n(fw.routes)}、"
             f"named から {n(fw.named)}")
    by_mode = joined(f"{m} {n(alt[m])}" for m in FIRST_WAVE_ROUTES)
    head = f"  routes の数え方ごとの第一波（site.yml の first_wave の routes。いまは {fw.mode}）: "
    if only is None:
        per = collections.Counter(p.field for p in fw.pages)
        lines = [f"第一波: {n(fw.pages)} ページ（{parts}）｜{counts(per, cat.vocab.fields)}", head + by_mode]
    else:
        whole = joined(f"{m} {len(alt[m])}" for m in FIRST_WAVE_ROUTES)
        lines = [f"第一波（{only} のページ）: {n(fw.pages)} ページ（{parts}。全体では {len(fw.pages)} ページ）",
                 f"{head}{by_mode}（全体では {whole}）"]
    first_ids = {p.id for p in alt["first"]}
    outside = sum(1 for x in fw.lacking if not first_ids.intersection(x.targets))
    by_page: dict[str, list[str]] = collections.defaultdict(list)
    for x in fw.lacking:
        by_page[x.page.label].append(x.cause)
    listed = "、".join(f"{pid}（{joined(cs)}）" for pid, cs in by_page.items())
    lines.append(f"  必須の先がない cause（first ではそこから入れない）: {len(fw.lacking)}"
                 + (f"（うち、first で先がどれも第一波に入らないもの {outside}）｜{listed}" if fw.lacking else ""))
    if fw.unresolved:
        lines.append(f"  たどれない候補（分野のファイルにまだない）: {joined(fw.unresolved)}")
    return lines


def format_stats(cat: Catalog, only: str | None = None) -> list[str]:
    """集計の行（--stats）。only のときはその分野だけ（第一波は全体でたどってから、その分野のページを数える）。"""
    v = cat.vocab
    lines = [f"集計（{only} の分野）:" if only else "集計（分野ごと。ページは分野のファイルの pages を数える）:"]
    total = FieldStats()
    for f in v.fields:
        if only is not None and f != only:
            continue
        st = field_stats(cat, f)
        has_file = f in cat.files
        if not has_file and not st.candidates and only is None:
            continue
        title = v.field_titles.get(f)
        lines.append(f"  {f}{f'（{title}）' if title else ''}: {format_field_stats(cat, st, has_file)}")
        total.add(st)
    if only is None:
        lines.append(f"  計: {format_field_stats(cat, total)}")
    lines += format_first_wave(cat, only)
    top = v.top_priority
    if top is not None:
        n = sum(1 for p in cat.pages if p.text("priority") == top and (only is None or p.field == only))
        lines.append(f"{top}: {n} ページ")
    return lines

# ============================================================================
# 出力と CLI
# ============================================================================


def select(issues: list[Issue], field: str | None) -> list[Issue]:
    """--field のときは、その分野に関わる指摘と、いつも出す指摘だけにする。"""
    if field is None:
        return issues
    return [i for i in issues if field in i.fields or i.fields == ALWAYS]


def format_issue(i: Issue) -> str:
    loc = f"{i.file}:{i.line}" if i.line else i.file
    message = i.message.replace("\r", " ").replace("\n", " ")
    return f"{i.severity}: {loc}: {i.page}: [{i.check}] {message}"


def summary_line(cat: Catalog, errors: list[Issue], warnings: list[Issue], field: str | None, quiet: bool) -> str:
    order = {c.name: i for i, c in enumerate(CHECKS)}

    def part(label: str, items: list[Issue]) -> str:
        c = collections.Counter(i.check for i in items)
        detail = joined(f"{k} {c[k]}" for k in sorted(c, key=order.get))
        return f"{label} {len(items)} 件" + (f"（{detail}）" if detail else "")

    scope = f"{field} に関わる指摘：" if field else ""
    hidden = "。-q で出していない" if quiet and warnings else ""
    return (f"{scope}{part(ERROR, errors)}、{part(WARNING, warnings)}{hidden}"
            f"（分野のファイル {len(cat.files)}・ページ {len(cat.pages)} を読んだ）")


def checks_epilog() -> str:
    out = []
    for sev, effect in ((ERROR, "終了コードを 1 にする"), (WARNING, "終了コードは変えない")):
        out.append(f"検査（{sev}。{effect}）:")
        out += [f"  [{c.name}] {c.summary}" for c in CHECKS if c.severity == sev]
    return "\n".join(out)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="check_catalog.py", description=__doc__, epilog=checks_epilog(),
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", metavar="DIR",
                        help="置き場所の根（既定はこのリポジトリ。DIR/schema/site.yml と DIR/planning/catalog/ を読む）")
    parser.add_argument("--field", metavar="ID", help="その分野に関わる指摘だけを出す（読むのと参照の解決は全体で行う）")
    parser.add_argument("--stats", action="store_true", help="集計（分野ごとのページ数と内訳・第一波の数と内訳・必須の数）も出す")
    parser.add_argument("-q", "--quiet", action="store_true", help="警告を出さない（件数だけを最後の行に出す）")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(args.root).resolve() if args.root else ROOT
    try:
        cat = load_catalog(root)
    except Fatal as e:
        print(f"検査できない: {e}", file=sys.stderr)
        return 2
    if args.field is not None and args.field not in cat.vocab.fields:
        print(f"検査できない: --field の「{args.field}」が分野の id（site.yml の fields）にない", file=sys.stderr)
        return 2
    issues = select(run_checks(cat), args.field)
    errors = [i for i in issues if i.severity == ERROR]
    warnings = [i for i in issues if i.severity == WARNING]
    for i in errors + ([] if args.quiet else warnings):
        print(format_issue(i))
    if args.field is not None and args.field not in cat.files:
        print(f"注: {CATALOG_DIR}/{args.field}.yaml はまだない")
    if args.stats:
        for line in format_stats(cat, args.field):
            print(line)
    print(summary_line(cat, errors, warnings, args.field, args.quiet))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
