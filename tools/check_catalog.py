#!/usr/bin/env python3
"""目次（planning/catalog/ の registry.yaml と <field>.yaml）を検査する（工程3。設計書 §5.2 の3）。
形式と規則は planning/catalog/README.md の §2〜§6、語彙は schema/site.yml、上位の規則は planning/design.md の §3〜§5。

使い方:
  python3 tools/check_catalog.py                   全分野を検査して、エラーと警告を1件1行で出す
  python3 tools/check_catalog.py --field symptoms  その分野に関わる指摘だけを出す（読むのと参照の解決は全体で行う）
  python3 tools/check_catalog.py --stats           集計（分野ごとのページ数と内訳・第一波の数・必須の数）も出す
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
                                  entry_fields（入ってくる道を問わない分野。なければ fields の最初の分野＝start）
  planning/catalog/registry.yaml  候補（pages）と、古くなった助言の台帳の項目（ledger）
  planning/catalog/<field>.yaml   分野のページ。ファイル名が site.yml の fields の id のものだけを読む
  機能の id（tracks）             planning/catalog/features.yaml があればそこから、なければ catalog/README.md §5 の表から読み、
                                  どの分野のファイルの new_features の id も加える。features.yaml は、id の文字列のリスト、
                                  {id: …} のリスト、それらを面ごとの見出しの下に置いたマッピング（features: の下でもよい）を読む

参照（prerequisites・related・merged の into）の解決:
  ページの id                          解決する。related の id#anchor は、相手の sections の anchor も確かめる
  分野のファイルがまだない registry の候補  指摘しない（その分野のファイルができてから確かめる）
  分野のファイルはあるのに、その pages・merged・dropped のどこにもない registry の候補   警告（未処理の候補）
  merged・dropped にした候補、どこにもない id   エラー（参照）

構造（設計書 §8.3）: 読む層（load_catalog：YAML を読んでページのモデルにする）→ 検査（@check で登録した関数。
1検査1関数で、重さは登録のときに決める）→ 出力（format_issue・format_stats・summary_line）。検査の一覧は -h の末尾。
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
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
    "prerequisites": STRS, "related": STRS, "tracks": STRS, "outdated_advice": STRS, "volatility": STR,
    "sections": MAPS, "templates": MAPS, "visual": MAP, "materials": STRS, "notes": ANY,
}
PAGE_REQUIRED = ("id", "title", "type", "priority", "summary", "volatility")   # level は型による（§4.3-2）
PART_SHAPES = {   # ページの中の要素
    "signs": {"type": STR, "text": STR},
    "sections": {"title": STR, "anchor": STR, "level": STR},
    "templates": {"name": STR, "kind": STR, "safety": BOOL},
    "visual": {"kind": STR, "text": STR},
}
PART_REQUIRED = {"signs": ("type", "text"), "sections": ("title", "anchor"),
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
PART_VOCAB = {("signs", "type"): "sign_types", ("sections", "level"): "levels",
              ("templates", "kind"): "template_kinds", ("visual", "kind"): "visual_kinds"}
CANDIDATE_VOCAB = {"field": "fields", "type": "types", "priority": "priorities", "level": "levels"}

# 規則が名指しする語彙と数（catalog/README.md §4.1・§4.4・§4.5・§4.7）。
# 名指しする語彙が site.yml にあるかは、読むときに確かめる（なければ「設定」の警告）
SYMPTOM_TYPE = "symptom"        # 症状のページ：困りごとのサインを2つ以上、prevents を1つ以上
SYMPTOM_SIGN = "symptom"        # 困りごとのサインの種類
FEATURE_TYPE = "feature"        # 機能のページ：tracks が要る
MIN_SYMPTOM_SIGNS = 2
MAX_PREREQUISITES = 4           # 直接の前提は4つまで（5つ以上で警告）
MAX_RELATED = 20
MAX_SUMMARY_SENTENCES = 2
NEW_MARK = "新規"                # registry にないページの notes に書く印

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


# site.yml のリストの語彙：Vocab の属性 → (site.yml のキー, 使う検査)
VOCAB_LISTS = {
    "types": ("types", "type の語彙と level の要否"),
    "levels": ("levels", "level の語彙・レベルの逆転・比例則"),
    "priorities": ("priorities", "priority の語彙・必須の前提"),
    "surfaces": ("surfaces", "surfaces の語彙"),
    "principles": ("principles", "principle の語彙"),
    "prevents": ("prevents", "prevents の語彙"),
    "pitfalls": ("pitfalls", "pitfalls の語彙"),
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
    for value, pool, key, uses in ((SYMPTOM_TYPE, vocab.types, "types", "症状の signs・prevents"),
                                   (FEATURE_TYPE, vocab.types, "types", "機能の tracks"),
                                   (SYMPTOM_SIGN, vocab.sign_types, "sign_types", "症状の signs")):
        if pool is not None and value not in pool:
            note(f"道具の規則が名指しする「{value}」が site.yml の {key} にない（{uses}の検査が当たらない。"
                 "tools/check_catalog.py の規則の定数を直す）")
    if vocab.priorities == []:
        note("site.yml の priorities が空（必須の前提を検査しない）")
    return vocab


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
    各項目の id・field・title、merged の id・into、signs の type・text、sections の title・anchor など"""
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
    scenes、signs の type、sections の level、visual と templates の kind、registry の候補の field・type・priority・level"""
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
    """prerequisites・related・merged の into が解決しない：存在しない id、merged・dropped にした候補、
    related の id#anchor の anchor が相手の sections にない"""
    for p in cat.pages:
        for key, ref in page_refs(p):
            if not ref.target:
                yield at(p, f"{key} に空の id がある（{ref.raw!r}）")
                continue
            r = cat.resolve(ref.target)
            problem = bad_target(r)
            if problem:
                yield at(p, f"{key} の「{ref.raw}」{problem}")
            elif key == "related" and ref.anchor is not None and r.status == PAGE:
                anchors = r.page.anchors()
                if ref.anchor not in anchors:
                    have = f"あるのは {joined(anchors)}" if anchors else "sections がない"
                    yield at(p, f"related の「{ref.raw}」: {r.page.id} の sections に anchor「{ref.anchor}」がない（{have}）")
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
    """prerequisites・related・merged の into が指す registry の候補が、その分野のファイル（はある）の pages・merged・
    dropped のどこにもない（その分野が書きかけなら、後で解決する）"""
    def message(r: Resolution) -> str:
        f = r.entry.text("field")
        return f"は registry の候補だが、{f}.yaml の pages・merged・dropped のどこにもない（{f} が書きかけなら後で解決する）"

    for p in cat.pages:
        for key, ref in page_refs(p):
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
    """前提のページの level が、そのページの level より上の段（site.yml の levels の順）"""
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
    """必須（site.yml の priorities の最初）のページの前提が必須でない"""
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


@check("比例則", WARNING)
def check_proportional(cat: Catalog) -> Iterator[Finding]:
    """site.yml の proportional_rule の levels（任せる・仕組みにする・回す）のページが、guard_fields（verify・eval・enforce・
    safety）の分野のページを前提にも関連にも持たない（guard_fields の分野のページは除く。まだない分野の候補は registry
    の分野で数える）。任せる幅を広げる内容のページだけが対象なので、そうでないページは notes に理由を書いて残してよい"""
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
    """どのページの prerequisites・related にも出てこない（入ってくる道がない）。入口の分野（site.yml の entry_fields。
    なければ fields の最初の start）は除く"""
    incoming: set[str] = set()
    for p in cat.pages:
        for _, ref in page_refs(p):
            r = cat.resolve(ref.target) if ref.target else None
            if r is not None and r.status == PAGE and r.page.id != p.id:
                incoming.add(r.page.id)
    absent = [f for f in cat.vocab.fields if f not in cat.files]
    later = f"。まだファイルのない {len(absent)} 分野からの参照は数えていない" if absent else ""
    for pid, p in cat.by_id.items():
        if p.field not in cat.vocab.entry_fields and pid not in incoming:
            yield at(p, f"どのページの prerequisites・related にも出てこない（入ってくる道がない{later}）")


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


@check("症状の prevents", WARNING)
def check_symptom_prevents(cat: Catalog) -> Iterator[Finding]:
    """symptom のページの prevents が空"""
    for p in cat.pages:
        if p.text("type") == SYMPTOM_TYPE and not p.strings("prevents"):
            yield at(p, f"{SYMPTOM_TYPE} のページの prevents が空（防ぐ・診断する原因を1つ以上書く）")


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
    wave: 1 のページがない"""
    core = cat.vocab.first_wave_core_fields
    if not core:
        return
    for p in cat.pages:
        if p.is_wave and p.field not in core:
            yield at(p, f"wave: 1 は第一波の核の分野（{joined(core)}）のページにだけ付ける")
    for f in core:
        ff = cat.files.get(f)
        if ff is not None and ff.pages and not any(p.is_wave for p in ff.pages):
            yield Finding(ff.file, None, "-", "第一波の核の分野なのに wave: 1 のページがない（総論と、多くのページが前提にする"
                                              "ページに付ける）", frozenset({f}))


@check("設定", WARNING)
def check_config(cat: Catalog) -> Iterator[Finding]:
    """検査の材料が足りない（registry.yaml がない、site.yml に語彙がない、機能の id の表がない、など）。足りない分の
    検査はしない"""
    yield from loaded(cat, "設定")

# ============================================================================
# 集計（--stats）
# ============================================================================


def first_wave(cat: Catalog) -> tuple[list[Page], list[Page], list[str]]:
    """第一波：wave: 1 のページと、そこから prerequisites をたどって届くページ。
    (wave: 1 のページ, たどって届いたページ, たどれない前提＝分野のファイルにまだない候補の id)。"""
    core = [p for p in cat.by_id.values() if p.is_wave]
    seen = {p.id for p in core}
    reached: list[Page] = []
    unresolved: list[str] = []
    queue = collections.deque(core)
    while queue:
        p = queue.popleft()
        for ref in p.refs("prerequisites"):
            r = cat.resolve(ref.target)
            if r.status == PAGE:
                if r.page.id not in seen:
                    seen.add(r.page.id)
                    reached.append(r.page)
                    queue.append(r.page)
            elif r.status in (PENDING, UNPROCESSED) and ref.target not in unresolved:
                unresolved.append(ref.target)
    return core, reached, unresolved


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
    core, reached, unresolved = first_wave(cat)
    wave = core + reached
    if only is not None:
        mine = [p for p in wave if p.field == only]
        lines.append(f"第一波（{only} のページ）: {len(mine)} ページ（全体では {len(wave)} ページ）")
    else:
        per = collections.Counter(p.field for p in wave)
        lines.append(f"第一波: {len(wave)} ページ（wave: 1 が {len(core)}、前提でたどって届くもの {len(reached)}）｜"
                     f"{counts(per, v.fields)}")
    if unresolved:
        lines.append(f"  前提でたどれない候補（分野のファイルにまだない）: {joined(unresolved)}")
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
    parser.add_argument("--stats", action="store_true", help="集計（分野ごとのページ数と内訳・第一波の数・必須の数）も出す")
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
