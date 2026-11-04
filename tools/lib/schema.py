"""小さな JSON Schema の検査器（Draft-07 の一部）。schema/page.schema.json と data の schema を当てる。

kyopro-atlas の tools/check_pages.py の Validator（同じ作者、MIT）を写して直したもの。jsonschema がなくても動き、
誤りを日本語で返す（schema に x-message があれば、それを出す）。足したもの：
- format（date・partial-date・regex）を確かめる（jsonschema は format を既定では確かめない。試験では
  FormatChecker を付けた jsonschema と結果を照らす）
- minProperties・maxProperties、required の誤りにも x-message を使うこと
- 誤りの場所を、キーと位置の並び（path）で返すこと（yamlio.line_at でファイルの行に直せる）
知らないキーワードのある schema は、読み込みで SchemaError にする（綴りの誤りで検査が素通りにならないように）。
"""
from __future__ import annotations

import collections
import datetime
import json
import re
from dataclasses import dataclass
from pathlib import Path

from .base import DATE_RE, PARTIAL_DATE_RE, partial_date_key


class SchemaError(Exception):
    """schema が読めない・この検査器が知らないキーワードがある。"""


@dataclass(frozen=True)
class SchemaIssue:
    path: tuple                # キーと位置の並び（("routes", 0, "cause") など。空なら全体）
    message: str

    @property
    def where(self) -> str:
        """「routes[0].cause」の形（全体なら「front matter」ではなく空の文字列）。"""
        out = ""
        for x in self.path:
            out += f"[{x}]" if isinstance(x, int) else (f".{x}" if out else str(x))
        return out

    def format(self) -> str:
        return f"{self.where}: {self.message}" if self.path else self.message


def _check_format(name: str, inst: str) -> bool:
    if name == "date":
        if not DATE_RE.match(inst):          # fromisoformat は 3.11 から 20261104 や 2026-W45-3 も読むので、形を先に見る
            return False
        try:
            datetime.date.fromisoformat(inst)
        except ValueError:
            return False
        return True
    if name == "partial-date":
        return PARTIAL_DATE_RE.match(inst) is not None and partial_date_key(inst) is not None
    if name == "regex":
        try:
            re.compile(inst)
        except re.error:
            return False
        return True
    return True                # 知らない format は確かめない（Draft-07 の既定と同じ）


FORMAT_HINT = {"date": "日付（2026-11-04 の形）でない", "partial-date": "日付（2026・2026-11・2026-11-04 の形）でない",
               "regex": "正規表現として読めない"}


def _show(v) -> str:
    return "null" if v is None else json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list, bool)) else repr(v)


class Validator:
    KEYWORDS = {"$schema", "$id", "$comment", "title", "description", "default", "examples", "x-message",
                "type", "enum", "const", "pattern", "format", "minLength", "maxLength", "minimum", "maximum",
                "multipleOf", "required", "properties", "additionalProperties", "minProperties", "maxProperties",
                "items", "minItems", "maxItems", "uniqueItems", "allOf", "anyOf", "not", "if", "then", "else",
                "$ref", "definitions"}
    TYPES = {"string": lambda v: isinstance(v, str), "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
             "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
             "boolean": lambda v: isinstance(v, bool), "null": lambda v: v is None,
             "array": lambda v: isinstance(v, list), "object": lambda v: isinstance(v, dict)}
    TYPE_JA = {"string": "文字列", "integer": "整数", "number": "数", "boolean": "真偽", "null": "null",
               "array": "リスト", "object": "マッピング"}

    def __init__(self, schema: dict) -> None:
        self.root = schema
        self._check(schema, "#")

    def _check(self, s, where: str) -> None:
        if isinstance(s, bool):
            return
        if not isinstance(s, dict):
            raise SchemaError(f"{where}: スキーマがオブジェクトでない")
        unknown = set(s) - self.KEYWORDS
        if unknown:
            raise SchemaError(f"{where}: 検査器が知らないキーワード {sorted(unknown)}（tools/lib/schema.py の Validator に足す）")
        for t in (s["type"] if isinstance(s.get("type"), list) else [s["type"]]) if "type" in s else []:
            if t not in self.TYPES:
                raise SchemaError(f"{where}: 知らない type「{t}」")
        if "$ref" in s:
            self.resolve(s["$ref"])
        for k in ("properties", "definitions"):
            for name, sub in (s.get(k) or {}).items():
                self._check(sub, f"{where}/{k}/{name}")
        for k in ("additionalProperties", "items", "not", "if", "then", "else"):
            if k in s:
                if k == "items" and isinstance(s[k], list):
                    raise SchemaError(f"{where}/items: 位置ごとの items（リスト）は扱わない")
                self._check(s[k], f"{where}/{k}")
        for k in ("allOf", "anyOf"):
            for i, sub in enumerate(s.get(k) or []):
                self._check(sub, f"{where}/{k}/{i}")

    def resolve(self, ref: str) -> dict:
        if not ref.startswith("#/"):
            raise SchemaError(f"$ref は文書の中だけ: {ref}")
        node = self.root
        try:
            for part in ref[2:].split("/"):
                node = node[part]
        except (KeyError, TypeError):
            raise SchemaError(f"$ref の先がない: {ref}") from None
        return node

    def errors(self, inst, s=None, path: tuple = ()) -> list[SchemaIssue]:
        s = self.root if s is None else s
        if s is True:
            return []
        if s is False:
            return [SchemaIssue(path, "この項目は持てない")]
        if "$ref" in s:
            s = {**self.resolve(s["$ref"]), **{k: v for k, v in s.items() if k != "$ref"}}
        errs: list[SchemaIssue] = []

        def add(msg: str) -> None:
            errs.append(SchemaIssue(path, s.get("x-message") or msg))

        if "type" in s:
            types = s["type"] if isinstance(s["type"], list) else [s["type"]]
            if not any(self.TYPES[t](inst) for t in types):
                add(f"{'・'.join(self.TYPE_JA[t] for t in types)}にする（いまは {_show(inst)}）")
                return errs
        if "enum" in s and not any(inst == e and type(inst) is type(e) for e in s["enum"]):
            add(f"「{_show(inst)}」は使えない（{'・'.join(_show(e) if not isinstance(e, str) else e for e in s['enum'])} のどれか）")
        if "const" in s and not (inst == s["const"] and type(inst) is type(s["const"])):
            add(f"{_show(s['const'])} にする（いまは {_show(inst)}）")
        if isinstance(inst, str):
            if "pattern" in s and not re.search(s["pattern"], inst):
                add(f"形が違う: {inst!r}")
            elif "format" in s and not _check_format(s["format"], inst):
                add(f"{FORMAT_HINT.get(s['format'], '形が違う')}: {inst!r}")
            if len(inst) < s.get("minLength", 0):
                add("空にしない")
            if "maxLength" in s and len(inst) > s["maxLength"]:
                add(f"長すぎる（{len(inst)} 字。{s['maxLength']} 字まで）")
        if isinstance(inst, (int, float)) and not isinstance(inst, bool):
            if "minimum" in s and inst < s["minimum"]:
                add(f"{inst} は小さすぎる（{s['minimum']} 以上）")
            if "maximum" in s and inst > s["maximum"]:
                add(f"{inst} は大きすぎる（{s['maximum']} 以下）")
            if "multipleOf" in s and inst % s["multipleOf"]:
                add(f"{inst} は {s['multipleOf']} の倍数でない")
        if isinstance(inst, dict):
            for k in s.get("required", []):
                if k not in inst:
                    errs.append(SchemaIssue(path + (k,), s.get("x-message") or "ない（必須）"))
            if len(inst) < s.get("minProperties", 0):
                add(f"項目が {len(inst)} 個（{s['minProperties']} 個以上にする）")
            if "maxProperties" in s and len(inst) > s["maxProperties"]:
                add(f"項目が {len(inst)} 個（{s['maxProperties']} 個まで）")
            props = s.get("properties", {})
            for k, v in inst.items():
                if k in props:
                    errs += self.errors(v, props[k], path + (k,))
                elif "additionalProperties" in s:
                    ap = s["additionalProperties"]
                    if ap is False:
                        errs.append(SchemaIssue(path + (k,), "知らない項目（綴りの誤りか。キーの台帳 schema/keys.yml にない）"))
                    elif isinstance(ap, dict):
                        errs += self.errors(v, ap, path + (k,))
        if isinstance(inst, list):
            lo, hi = s.get("minItems", 0), s.get("maxItems")
            if len(inst) < lo or (hi is not None and len(inst) > hi):
                rng = f"{lo}〜{hi} 個" if hi is not None else f"{lo} 個以上"
                add(f"要素が {len(inst)} 個（{rng}にする）")
            if s.get("uniqueItems"):
                keys = [json.dumps(x, sort_keys=True, ensure_ascii=False) for x in inst]
                dup = [k for k, c in collections.Counter(keys).items() if c > 1]
                if dup:
                    add(f"同じ要素が重なっている: {', '.join(dup)}")
            if "items" in s:
                for i, x in enumerate(inst):
                    errs += self.errors(x, s["items"], path + (i,))
        for sub in s.get("allOf", []):
            errs += self.errors(inst, sub, path)
        if "anyOf" in s and all(self.errors(inst, sub, path) for sub in s["anyOf"]):
            add("どの形にも合わない")
        if "not" in s and not self.errors(inst, s["not"], path):
            add("この形にはできない")
        if "if" in s:
            branch = s.get("then") if not self.errors(inst, s["if"], path) else s.get("else")
            if branch is not None:
                errs += self.errors(inst, branch, path)
        return errs

    def is_valid(self, inst) -> bool:
        return not self.errors(inst)


def load_validator(path: Path) -> Validator:
    """schema のファイルを読んで検査器にする（読めなければ SchemaError）。"""
    try:
        schema = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        raise SchemaError(f"{path} が読めない: {e}") from None
    return Validator(schema)
