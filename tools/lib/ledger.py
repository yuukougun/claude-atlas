"""キーの台帳（schema/keys.yml）を読み、JSON Schema（Draft-07）を作る。入口は tools/make_schema.py。

設計書 §3.3 の台帳（キーごとに、誰が書くか・どこに写るか・書式）を道具が読める形にしたものが schema/keys.yml で、
語彙は schema/site.yml から読む（DR-16：page.schema.json は site.yml とキーの台帳から作る。語彙を二か所に持たない）。
data の schema（facts・sources・outdated-advice・inspection）も同じ書き方で作る。keys.yml の書き方は keys.yml の冒頭。

schema にする規則:
  required: all → required。optional → なし。{types|types_except|stages|stages_except|with|without: …} → allOf の
            if/then（then に required。non_empty なら minItems 1 も）
  forbidden: 同じ条件 → allOf の if/then（then でそのキーを書けなくする。null も書かない）
  format:   FORMATS の名前か、{vocab: site.yml のキー}（enum）・{vocab_list: …}・{object: {キー: …}}・{list: {キー: …}}
            site.yml にない語彙は、空でない文字列だけを見る形にして「注」に出す（site.yml に足せば、作り直すと enum になる）
  nullable: null も許す。min_items・min_keys：リストの要素・マッピングの項目の最少の数
  writer・shows・note・catalog：description に入れる（キーの台帳の「書く人」「写る先」「書式・検査」の説明）
入れ子のマッピングもすべて additionalProperties: false にする（台帳にないキーは誤り。kyopro-atlas の反省 B2）。
毎回変わる値（日時・ハッシュ）は入れない（design §8.4）。
"""
from __future__ import annotations

import copy
import json
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from .base import ID_PATTERN, REF_PATTERN, Fatal, as_strings, as_text
from .site import Site
from .yamlio import read_yaml

KEYS_FILE = "schema/keys.yml"
SCHEMA_DIR = "schema"
DRAFT = "http://json-schema.org/draft-07/schema#"
COMMENT = ("tools/make_schema.py が schema/keys.yml（キーの台帳）と schema/site.yml（語彙）から作る。"
           "手で直さない（直すのは keys.yml か site.yml。直したら作り直す）")

MONTH, DAY = r"(0[1-9]|1[0-2])", r"(0[1-9]|[12][0-9]|3[01])"     # 2月30日のような日は format で見る
DATE_PATTERN = rf"^[0-9]{{4}}-{MONTH}-{DAY}$"
PARTIAL_DATE_PATTERN = rf"^[0-9]{{4}}(-{MONTH}(-{DAY})?)?$"
VERSION_PATTERN = r"^[0-9]+\.[0-9]+\.[0-9]+$"
DOMAIN_PATTERN = r"^([a-z0-9]([a-z0-9-]*[a-z0-9])?\.)+[a-z]{2,}$"
LANG_PATTERN = r"^[a-z]{2,3}(-[A-Za-z0-9]{2,8})*$"
URL_PATTERN = r"^https?://[^\s]+$"

TEXT = {"type": "string", "minLength": 1, "x-message": "空でない文字列（平文）にする"}
ID = {"type": "string", "pattern": ID_PATTERN, "x-message": "id（英小文字・数字・ハイフン）にする"}
REF = {"type": "string", "pattern": REF_PATTERN, "x-message": "ページの id か id#anchor にする"}
SCALAR = {"type": ["string", "number", "boolean", "null"], "x-message": "文字列・数・真偽・null のどれかにする"}


def _array_of(item: dict) -> dict:
    return {"type": "array", "uniqueItems": True, "items": item}


FORMATS: dict[str, dict] = {
    "text": TEXT,
    "texts": _array_of(TEXT),
    "id": ID,
    "ids": _array_of(ID),
    "page_ref": REF,
    "page_refs": _array_of(REF),
    "date": {"type": "string", "pattern": DATE_PATTERN, "format": "date", "x-message": "日付（2026-11-04 の形）にする"},
    "partial_date": {"type": ["string", "integer"], "pattern": PARTIAL_DATE_PATTERN, "format": "partial-date",
                     "minimum": 1000, "maximum": 9999,       # 年だけ（date: 2026）は YAML では整数になる
                     "x-message": "日付（2026・2026-11・2026-11-04 の形）にする"},
    "order": {"type": "integer", "minimum": 0, "x-message": "0 以上の整数にする"},
    "wave": {"const": 1, "x-message": "1 にする（第一波の核でなければ書かない）"},
    "boolean": {"type": "boolean", "x-message": "true か false にする"},
    "url": {"type": "string", "pattern": URL_PATTERN, "x-message": "URL（https://… の形）にする"},
    "domain": {"type": "string", "pattern": DOMAIN_PATTERN, "x-message": "ドメイン（code.claude.com の形。英小文字）にする"},
    "version": {"type": "string", "pattern": VERSION_PATTERN, "x-message": "版（2.1.317 の形の文字列）にする"},
    "lang": {"type": "string", "pattern": LANG_PATTERN, "x-message": "言語（ja・en の形）にする"},
    "regex": {"type": "string", "minLength": 1, "format": "regex", "x-message": "正規表現（Python の re の書き方）にする"},
    "scalar": SCALAR,
    "value": {"$ref": "#/definitions/value"},
    "table": {"$ref": "#/definitions/table"},
}
ARRAY_FORMATS = {"texts", "ids", "page_refs"}          # 名前の書式のうちリストのもの（ほかに vocab_list・list）

DEFINITIONS: dict[str, dict] = {
    "value": {
        "description": "数値ファイルの1つの値：文字列・数・真偽か、そのリスト",
        "type": ["string", "number", "boolean", "array"], "minItems": 1,
        "items": {"type": ["string", "number", "boolean"], "x-message": "リストの値は文字列・数・真偽にする"},
        "x-message": "値は文字列・数・真偽か、そのリストにする",
    },
    "cell": {
        "description": "表の1つの値：文字列・数・真偽・null（値を書いた文書がない）か、{value, note, sources}",
        "type": ["string", "number", "boolean", "null", "object"], "additionalProperties": False, "required": ["value"],
        "properties": {"value": SCALAR, "note": TEXT, "sources": _array_of(ID)},
        "x-message": "表の値は、値か {value, note, sources} にする",
    },
    "table": {
        "description": ("面やモデルで違う値の表。rows は行が何か（表の左上の見出し）、columns は列の id か {id, title}、"
                        "cells は行ごとの値（row に行の名前、列の id をキーに値）。列の id と cells のキーの対応は検査の層が見る"),
        "type": "object", "additionalProperties": False, "required": ["rows", "columns", "cells"],
        "properties": {
            "rows": TEXT,
            "columns": {"type": "array", "minItems": 1, "items": {
                "type": ["string", "object"], "pattern": ID_PATTERN, "required": ["id"], "additionalProperties": False,
                "properties": {"id": ID, "title": TEXT}, "x-message": "列は id か {id, title} にする"}},
            "cells": {"type": "array", "minItems": 1, "items": {
                "type": "object", "required": ["row"], "properties": {"row": TEXT},
                "additionalProperties": {"$ref": "#/definitions/cell"},
                "x-message": "行は {row: 行の名前, <列の id>: 値, …} にする"}},
        },
    },
}
NEEDS = {"value": ("value",), "table": ("table", "cell")}   # 書式が使う definitions

SPEC_KEYS = ("required", "forbidden", "format", "nullable", "non_empty", "min_items", "min_keys",
             "writer", "shows", "catalog", "note")
SECTION_KEYS = ("output", "file", "title", "description", "keys")
LEDGER_KEYS = ("id_base", "sections")
CONDITIONS = ("types", "types_except", "stages", "stages_except", "with", "without")
CONDITION_KEY = {"types": "type", "types_except": "type", "stages": "stage", "stages_except": "stage"}
CONDITION_POOL = {"type": "types", "stage": "stages"}       # 条件のキー → site.yml の語彙


@dataclass(frozen=True)
class Condition:
    kind: str                          # all・optional・types・types_except・stages・stages_except・with・without
    value: object = None               # 値の組・site.yml のキー（文字列）・同じマッピングのキーの名前


@dataclass
class KeySpec:
    name: str
    required: Condition
    forbidden: Condition | None
    format: object                     # 名前（文字列）か {vocab|vocab_list|object|list: …}
    nested: dict[str, KeySpec] | None = None
    nullable: bool = False
    non_empty: bool = False
    min_items: int | None = None
    min_keys: int | None = None
    writer: str = ""
    shows: str = ""
    catalog: bool = False
    note: str = ""

    @property
    def format_kind(self) -> str:
        return self.format if isinstance(self.format, str) else next(iter(self.format))

    @property
    def is_array(self) -> bool:
        return self.format_kind in ARRAY_FORMATS or self.format_kind in ("vocab_list", "list")


@dataclass
class Section:
    name: str
    output: str                        # schema/ の中のファイル名（page.schema.json など）
    files: list[str]                   # 当てるファイル（説明）
    title: str
    description: str
    keys: dict[str, KeySpec]


@dataclass
class Ledger:
    file: str
    id_base: str
    sections: dict[str, Section]
    errors: list[str]                  # 台帳そのものの誤り（あれば schema を作らない）

    def section(self, name: str) -> Section | None:
        return self.sections.get(name)

    def catalog_keys(self) -> list[str]:
        """骨格で目次から写すページのキー（catalog: true。design §5.2 の5）。"""
        page = self.sections.get("page")
        return [k for k, s in page.keys.items() if s.catalog] if page else []


# ---------------------------------------------------------------- 読む


def _condition(raw, where: str, errors: list[str], simple: tuple[str, ...]) -> Condition:
    if isinstance(raw, str) and raw in simple:
        return Condition(raw)
    if isinstance(raw, dict) and len(raw) == 1:
        (kind, value), = raw.items()
        if kind in CONDITION_KEY:
            if isinstance(value, str) and value:
                return Condition(kind, value)
            if isinstance(value, list) and value and all(isinstance(x, str) and x for x in value):
                return Condition(kind, tuple(value))
        if kind in ("with", "without") and isinstance(value, str) and value:
            return Condition(kind, value)
    forms = "・".join(simple + ("{types|types_except|stages|stages_except: […] か site.yml のキー}",
                                "{with|without: 同じマッピングのキー}"))
    errors.append(f"{where}: 条件が読めない（{raw!r}。{forms}）")
    return Condition("optional")


def _spec(name: str, raw, where: str, errors: list[str]) -> KeySpec:
    if not isinstance(raw, dict):
        errors.append(f"{where}: キーの書き方をマッピングにする（いまは {raw!r}）")
        raw = {}
    for k in raw:
        if k not in SPEC_KEYS:
            errors.append(f"{where}: 知らない項目「{k}」（使えるのは {'・'.join(SPEC_KEYS)}）")
    required = _condition(raw.get("required", "optional"), f"{where}.required", errors, ("all", "optional"))
    forbidden = _condition(raw["forbidden"], f"{where}.forbidden", errors, ()) if raw.get("forbidden") is not None else None
    fmt, nested = raw.get("format"), None
    if isinstance(fmt, str):
        if fmt not in FORMATS:
            errors.append(f"{where}.format: 知らない書式「{fmt}」（{'・'.join(FORMATS)}）")
            fmt = "text"
    elif isinstance(fmt, dict) and len(fmt) == 1 and next(iter(fmt)) in ("vocab", "vocab_list", "object", "list"):
        kind, arg = next(iter(fmt.items()))
        if kind in ("vocab", "vocab_list"):
            ok = (isinstance(arg, str) and arg) or (isinstance(arg, list) and arg and all(isinstance(x, str) for x in arg))
            if not ok:
                errors.append(f"{where}.format: {kind} には site.yml のキー（かそのリスト）を書く")
                fmt = "text"
        elif isinstance(arg, dict) and arg:
            nested = _keys(arg, f"{where}.{kind}", errors)
        else:
            errors.append(f"{where}.format: {kind} にはキーの書き方のマッピングを書く")
            fmt = "text"
    else:
        errors.append(f"{where}.format: 書式がない・読めない（名前か {{vocab|vocab_list|object|list: …}}。いまは {fmt!r}）")
        fmt = "text"

    def flag(key: str) -> bool:
        v = raw.get(key, False)
        if not isinstance(v, bool):
            errors.append(f"{where}.{key}: true か false にする")
            return False
        return v

    def count(key: str) -> int | None:
        v = raw.get(key)
        if v is None:
            return None
        if not isinstance(v, int) or isinstance(v, bool) or v < 1:
            errors.append(f"{where}.{key}: 1 以上の整数にする")
            return None
        return v

    spec = KeySpec(name, required, forbidden, fmt, nested, flag("nullable"), flag("non_empty"), count("min_items"),
                   count("min_keys"), as_text(raw.get("writer")), as_text(raw.get("shows")), flag("catalog"),
                   as_text(raw.get("note")))
    if (spec.non_empty or spec.min_items) and not spec.is_array:
        errors.append(f"{where}: non_empty・min_items はリストの書式（{'・'.join(sorted(ARRAY_FORMATS))}・vocab_list・list）だけ")
    if spec.non_empty and required.kind == "optional":
        errors.append(f"{where}: non_empty は required の条件と組にする（任意のキーは min_items を使う）")
    if spec.min_keys and spec.format_kind != "object":
        errors.append(f"{where}: min_keys は object の書式だけ")
    for k in ("writer", "shows", "note"):
        if raw.get(k) is not None and not isinstance(raw.get(k), str):
            errors.append(f"{where}.{k}: 文字列にする")
    return spec


def _keys(raw: dict, where: str, errors: list[str]) -> dict[str, KeySpec]:
    specs = {}
    for name, sraw in raw.items():
        if not isinstance(name, str) or not name:
            errors.append(f"{where}: キーの名前を文字列にする（{name!r}）")
            continue
        specs[name] = _spec(name, sraw, f"{where}.{name}", errors)
    for name, spec in specs.items():          # 条件が同じマッピングのキーを指しているか
        for cond in (spec.required, spec.forbidden):
            if cond is None:
                continue
            if cond.kind in CONDITION_KEY and CONDITION_KEY[cond.kind] not in specs:
                errors.append(f"{where}.{name}: {cond.kind} の条件は、同じマッピングに {CONDITION_KEY[cond.kind]} があるときだけ")
            if cond.kind in ("with", "without") and (cond.value not in specs or cond.value == name):
                errors.append(f"{where}.{name}: {cond.kind} の「{cond.value}」が、同じマッピングのほかのキーでない")
    return specs


def load_ledger(root: Path) -> Ledger:
    """schema/keys.yml を読む。読めなければ Fatal。書き方の誤りは Ledger.errors に入れる。"""
    doc = read_yaml(Path(root) / KEYS_FILE)
    if doc.error is not None:
        raise Fatal(f"{KEYS_FILE} が読めない: {doc.error}")
    if not isinstance(doc.data, dict):
        raise Fatal(f"{KEYS_FILE} の最上位がマッピングでない")
    errors = [p.format() for p in doc.problems(KEYS_FILE)]
    raw = doc.data
    for k in raw:
        if k not in LEDGER_KEYS:
            errors.append(f"知らない項目「{k}」（使えるのは {'・'.join(LEDGER_KEYS)}）")
    id_base = as_text(raw.get("id_base"))
    if not id_base.endswith("/"):
        errors.append("id_base（schema の $id の頭。/ で終わる URL）がない")
    sections: dict[str, Section] = {}
    outputs: dict[str, str] = {}
    sraw_all = raw.get("sections")
    if not isinstance(sraw_all, dict) or not sraw_all:
        errors.append("sections（節の名前 → 節）がない")
        sraw_all = {}
    for name, sraw in sraw_all.items():
        where = f"sections.{name}"
        if not isinstance(sraw, dict):
            errors.append(f"{where}: マッピングにする")
            continue
        for k in sraw:
            if k not in SECTION_KEYS:
                errors.append(f"{where}: 知らない項目「{k}」（使えるのは {'・'.join(SECTION_KEYS)}）")
        output = as_text(sraw.get("output"))
        if not output.endswith(".schema.json") or "/" in output:
            errors.append(f"{where}.output: schema/ の中のファイル名（<名前>.schema.json）にする")
        elif output in outputs:
            errors.append(f"{where}.output: 「{output}」は {outputs[output]} と同じ")
        outputs[output] = name
        if not as_text(sraw.get("title")):
            errors.append(f"{where}.title がない")
        keys = sraw.get("keys")
        if not isinstance(keys, dict) or not keys:
            errors.append(f"{where}.keys（キーの書き方）がない")
            keys = {}
        sections[name] = Section(str(name), output, as_strings(sraw.get("file")), as_text(sraw.get("title")),
                                 as_text(sraw.get("description")), _keys(keys, f"{where}.keys", errors))
    return Ledger(KEYS_FILE, id_base, sections, errors)


# ---------------------------------------------------------------- 作る


def _nullable(s: dict) -> None:
    if "$ref" in s:
        s["anyOf"] = [{"$ref": s.pop("$ref")}, {"type": "null"}]
    elif "enum" in s:
        if None not in s["enum"]:
            s["enum"] = s["enum"] + [None]
    elif "const" in s:
        s["anyOf"] = [{"const": s.pop("const")}, {"type": "null"}]
    elif "type" in s:
        types = s["type"] if isinstance(s["type"], list) else [s["type"]]
        if "null" not in types:
            s["type"] = types + ["null"]


class Builder:
    """1つの節（Section）を JSON Schema にする。notes に、site.yml にない語彙などの注をためる。"""

    def __init__(self, site: Site, ledger: Ledger, section: Section):
        self.site, self.ledger, self.section = site, ledger, section
        self.notes: list[str] = []
        self.needs: list[str] = []
        self.missing: dict[str, list[str]] = {}     # site.yml にない語彙 → それを使う場所（注は語彙ごとに1行）

    def note(self, message: str) -> None:
        if message not in self.notes:
            self.notes.append(message)

    def build(self) -> dict:
        body = self.object(self.section.keys, "")
        schema = {"$schema": DRAFT, "$id": self.ledger.id_base + self.section.output, "$comment": COMMENT,
                  "title": self.section.title}
        files = "・".join(self.section.files)
        desc = "。".join(x for x in (f"当てるファイル：{files}" if files else "", self.section.description.rstrip("。")) if x)
        if desc:
            schema["description"] = desc
        schema.update(body)
        if self.needs:
            schema["definitions"] = {k: copy.deepcopy(DEFINITIONS[k]) for k in DEFINITIONS if k in self.needs}
        for label, paths in self.missing.items():
            self.note(f"site.yml に {label} がない（{self.section.name} の {'・'.join(paths)} を語彙で検査せず、"
                      "空でない文字列かだけを見る）")
        return schema

    def where(self, path: str) -> str:
        return f"{self.section.name} の {path}" if path else self.section.name

    def vocab(self, names, path: str) -> dict:
        values = self.site.vocab(names)
        label = names if isinstance(names, str) else "・".join(names)
        if values is None:
            self.missing.setdefault(label, []).append(path)
            return {"type": "string", "minLength": 1}
        return {"enum": values}

    def condition(self, cond: Condition, path: str) -> tuple[dict | None, str]:
        """(if の schema, 文の言い方)。条件に当たる値がなければ (None, …)（その規則は作らない）。"""
        if cond.kind in ("with", "without"):
            text = f"{cond.value} が{'ある' if cond.kind == 'with' else 'ない'}とき"
            req = {"required": [cond.value]}
            return (req if cond.kind == "with" else {"not": req}), text
        key = CONDITION_KEY[cond.kind]
        pool_name = CONDITION_POOL[key]
        pool = self.site.vocab(pool_name)
        if pool is None:
            self.note(f"site.yml に {pool_name} がない（{self.where(path)} の {cond.kind} の規則を作らない）")
            return None, ""
        if isinstance(cond.value, str):
            listed = self.site.vocab(cond.value)
            if listed is None:
                self.note(f"site.yml に {cond.value} がない（{self.where(path)} の {cond.kind} の規則を作らない）")
                return None, ""
            label = f"{'・'.join(listed)}（site.yml の {cond.value}）"
        else:
            listed = list(cond.value)
            label = "・".join(listed)
            for v in listed:
                if v not in pool:
                    self.note(f"{self.where(path)} の {cond.kind} の「{v}」が site.yml の {pool_name} にない")
        gap = " " if label[-1:].isascii() else ""          # 「symptom のページ」「…）のページ」
        if cond.kind.endswith("_except"):
            values, text = [v for v in pool if v not in listed], f"{key} が {label}{gap}のほかのページ"
        else:
            values, text = [v for v in listed if v in pool], f"{key} が {label}{gap}のページ"
        if not values:
            self.note(f"{self.where(path)} の {cond.kind} の条件に当たる {key} がない（この規則を作らない）")
            return None, text
        return {"required": [key], "properties": {key: {"enum": values}}}, text

    def describe(self, spec: KeySpec) -> str:
        parts = []
        if spec.writer:
            parts.append(f"書く人：{spec.writer}")
        if spec.shows:
            parts.append(f"写る先：{spec.shows}")
        if spec.note:
            parts.append(spec.note)
        if spec.format_kind in ("vocab", "vocab_list"):
            names = next(iter(spec.format.values()))
            parts.append(f"語彙は site.yml の {names if isinstance(names, str) else '・'.join(names)}")
        if spec.catalog:
            parts.append("骨格で目次から写す")
        return "。".join(p.rstrip("。") for p in parts)

    def property(self, spec: KeySpec, path: str) -> dict:
        s: dict = {}
        desc = self.describe(spec)
        if desc:
            s["description"] = desc
        kind = spec.format_kind
        if isinstance(spec.format, str):
            body = copy.deepcopy(FORMATS[spec.format])
            for d in NEEDS.get(spec.format, ()):
                if d not in self.needs:
                    self.needs.append(d)
        elif kind == "vocab":
            body = self.vocab(spec.format["vocab"], path)
        elif kind == "vocab_list":
            body = {"type": "array", "uniqueItems": True, "items": self.vocab(spec.format["vocab_list"], path)}
        elif kind == "object":
            body = self.object(spec.nested or {}, path)
        else:
            body = {"type": "array", "items": self.object(spec.nested or {}, path + "[]")}
        s.update(body)
        if spec.nullable:
            _nullable(s)
        least = max(spec.min_items or 0, 1 if spec.non_empty and spec.required.kind == "all" else 0)
        if least:
            s["minItems"] = least
        if spec.min_keys:
            s["minProperties"] = spec.min_keys
        return s

    def object(self, specs: dict[str, KeySpec], path: str) -> dict:
        props: dict[str, dict] = {}
        required: list[str] = []
        all_of: list[dict] = []
        for name, spec in specs.items():
            sub = f"{path}.{name}" if path else name
            props[name] = self.property(spec, sub)
            req = spec.required
            if req.kind == "all":
                required.append(name)
            elif req.kind != "optional":
                cond, text = self.condition(req, sub)
                if cond is not None:
                    then: dict = {"required": [name], "x-message": f"{name} がない（{text}は書く）"}
                    if spec.non_empty:
                        then["properties"] = {name: {"minItems": 1, "x-message": f"{name} を空にしない（{text}）"}}
                    all_of.append({"if": cond, "then": then})
            if spec.forbidden is not None:
                cond, text = self.condition(spec.forbidden, sub)
                if cond is not None:
                    all_of.append({"if": cond, "then": {"properties": {name: {
                        "not": {}, "x-message": f"{text}は {name} を書かない（null も書かない）"}}}})
        s: dict = {"type": "object", "additionalProperties": False}
        if required:
            s["required"] = required
        s["properties"] = props
        if all_of:
            s["allOf"] = all_of
        return s


@dataclass
class Built:
    section: Section
    path: str                          # 根からの相対パス（schema/page.schema.json）
    schema: dict
    text: str                          # 書くときの文字列（dumps）
    notes: list[str] = field(default_factory=list)


def build_all(ledger: Ledger, site: Site) -> list[Built]:
    """台帳のすべての節の schema を作る（台帳に誤りがあれば ValueError）。"""
    if ledger.errors:
        raise ValueError("キーの台帳に誤りがある: " + " / ".join(ledger.errors))
    out = []
    for sec in ledger.sections.values():
        b = Builder(site, ledger, sec)
        schema = b.build()
        out.append(Built(sec, f"{SCHEMA_DIR}/{sec.output}", schema, dumps(schema), b.notes))
    return out


def _width(s: str) -> int:
    """表示の幅（全角は2）。"""
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in s)


def _depth(o) -> int:
    if isinstance(o, dict):
        return 1 + max((_depth(v) for v in o.values()), default=0)
    if isinstance(o, list):
        return 1 + max((_depth(v) for v in o), default=0)
    return 0


def dumps(obj, width: int = 120) -> str:
    """JSON を、表示の幅に入る入れ物は1行に、入らないものは2字下げで書く。値だけのリストは幅まで詰めて折り返す。
    同じ入力からいつも同じ文字列になる。"""
    def one(o) -> str:
        return json.dumps(o, ensure_ascii=False, separators=(", ", ": "))

    def fmt(o, indent: int, used: int) -> str:
        line = one(o)
        if not isinstance(o, (dict, list)) or not o or used + _width(line) <= width:
            return line
        pad, close = " " * (indent + 2), " " * indent
        if isinstance(o, list) and _depth(o) == 1:
            rows, row = [], ""
            for item in (one(v) for v in o):
                if row and len(pad) + _width(row) + 2 + _width(item) > width:
                    rows.append(row + ",")
                    row = item
                else:
                    row = f"{row}, {item}" if row else item
            rows.append(row)
            return "[\n" + "\n".join(pad + r for r in rows) + "\n" + close + "]"
        if isinstance(o, dict):
            parts = []
            for k, v in o.items():
                key = json.dumps(k, ensure_ascii=False) + ": "
                parts.append(pad + key + fmt(v, indent + 2, indent + 2 + _width(key)))
            return "{\n" + ",\n".join(parts) + "\n" + close + "}"
        return "[\n" + ",\n".join(pad + fmt(v, indent + 2, indent + 2) for v in o) + "\n" + close + "]"

    return fmt(obj, 0, 0) + "\n"
