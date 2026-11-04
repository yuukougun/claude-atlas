"""schema の試験：小さな検査器（tools/lib/schema.py）・キーの台帳（schema/keys.yml と tools/lib/ledger.py）・
作った schema の当てはまり・道具の入口（tools/make_schema.py）。`uv run python -m unittest discover -s tests/tools` で動く。

- 作った schema を、試験の置き場所（fixtures/lib）の front matter と data に当てて誤り0、1か所ずつ変えると、決めた場所
  だけが誤りになることを確かめる（MUTATIONS）。jsonschema があれば、同じ入力で jsonschema（Draft-07・format も
  確かめる）と、通るか通らないかが一致することも確かめる
- 本物の schema/*.schema.json が、本物の keys.yml と site.yml から作り直したものと同じ（作り直し忘れがない）
- 本物の目次の全ページを骨格の形（キーの台帳の catalog のキー＋field・order・stage・updated・sources）にすると、
  page.schema.json に通る（骨格の道具が作る front matter と schema が食い違わない）
"""
from __future__ import annotations

import contextlib
import copy
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "lib"

import make_schema  # noqa: E402
from lib import load_catalog, load_docs, load_site  # noqa: E402
from lib.ledger import build_all, dumps, load_ledger  # noqa: E402
from lib.schema import SchemaError, SchemaIssue, Validator, load_validator  # noqa: E402
from lib.yamlio import read_yaml, to_jsonable  # noqa: E402

try:
    import jsonschema
except ImportError:          # jsonschema がなければ、照らし合わせの試験だけを飛ばす
    jsonschema = None

DELETE = object()
DATA_SCHEMAS = {"data/facts.yml": "facts", "data/sources.yml": "sources",
                "data/sources.d/instructions-ignored.yml": "sources", "data/outdated-advice.yml": "outdated-advice",
                "data/inspection.yml": "inspection"}


def json_validator(schema: dict):
    """format（date・regex と、この教材の partial-date）も確かめる jsonschema の検査器。"""
    from lib.schema import _check_format
    base = getattr(jsonschema.Draft7Validator, "FORMAT_CHECKER", None) or jsonschema.draft7_format_checker   # 4 より前の名前
    checker = copy.deepcopy(base)
    checker.checks("partial-date")(lambda v: not isinstance(v, str) or _check_format("partial-date", v))
    return jsonschema.Draft7Validator(schema, format_checker=checker)


def change(data: dict, path: tuple, value) -> None:
    """data の path（キーと位置）を value にする（DELETE なら消す）。"""
    node = data
    for part in path[:-1]:
        node = node[part]
    if value is DELETE:
        del node[path[-1]]
    else:
        node[path[-1]] = value


# ---------------------------------------------------------------- 検査器


class TestValidator(unittest.TestCase):
    def errors(self, schema: dict, inst) -> list[tuple[str, str]]:
        return [(i.where, i.message) for i in Validator(schema).errors(inst)]

    def test_unknown_keyword_and_bad_ref_stop_loading(self):
        with self.assertRaises(SchemaError):
            Validator({"type": "string", "patern": "x"})
        with self.assertRaises(SchemaError):
            Validator({"$ref": "#/definitions/none"})
        with self.assertRaises(SchemaError):
            Validator({"type": "text"})
        with self.assertRaises(SchemaError):
            Validator({"items": [{"type": "string"}]})

    def test_types_enum_const(self):
        self.assertEqual(self.errors({"type": ["string", "null"]}, 1)[0][1], "文字列・nullにする（いまは 1）")
        self.assertEqual(self.errors({"type": "integer"}, True), [("", "整数にする（いまは true）")])
        self.assertTrue(self.errors({"enum": [1]}, True))
        self.assertEqual(self.errors({"enum": ["a", None]}, None), [])
        self.assertTrue(self.errors({"const": 1}, True))
        self.assertEqual(self.errors({"const": 1}, 1), [])

    def test_strings(self):
        self.assertEqual(self.errors({"type": "string", "pattern": "^a"}, "ba"), [("", "形が違う: 'ba'")])
        self.assertEqual(self.errors({"type": "string", "format": "date"}, "2026-02-30")[0][1],
                         "日付（2026-11-04 の形）でない: '2026-02-30'")
        for ok in ("2026-02-28", "2024-02-29"):
            self.assertEqual(self.errors({"format": "date"}, ok), [])
        for bad in ("20261104", "2026-W45-3", "2026-11-4"):
            self.assertTrue(self.errors({"format": "date"}, bad), bad)
        self.assertEqual(self.errors({"format": "partial-date"}, "2026-10"), [])
        self.assertTrue(self.errors({"format": "partial-date"}, "2026-02-30"))
        self.assertTrue(self.errors({"format": "regex"}, "("))
        self.assertEqual(self.errors({"format": "unknown-format"}, "x"), [])
        self.assertEqual(self.errors({"minLength": 1}, ""), [("", "空にしない")])
        self.assertEqual(self.errors({"minLength": 1, "x-message": "平文"}, ""), [("", "平文")])

    def test_objects(self):
        s = {"type": "object", "additionalProperties": False, "required": ["a"], "minProperties": 2,
             "properties": {"a": {"type": "string"}, "b": {"type": "object", "properties": {"c": {"type": "integer"}}}}}
        self.assertEqual(self.errors(s, {"b": {"c": "x"}, "z": 1}),
                         [("a", "ない（必須）"), ("b.c", "整数にする（いまは 'x'）"),
                          ("z", "知らない項目（綴りの誤りか。キーの台帳 schema/keys.yml にない）")])
        self.assertEqual(self.errors(s, {"a": "x"}), [("", "項目が 1 個（2 個以上にする）")])
        self.assertEqual(self.errors({"required": ["a"], "x-message": "a を書く"}, {}), [("a", "a を書く")])
        self.assertEqual(self.errors({"minProperties": 1}, {}), [("", "項目が 0 個（1 個以上にする）")])

    def test_arrays(self):
        s = {"type": "array", "minItems": 1, "maxItems": 2, "uniqueItems": True, "items": {"type": "string"}}
        self.assertEqual(self.errors(s, []), [("", "要素が 0 個（1〜2 個にする）")])
        self.assertEqual(self.errors(s, ["a", "a", 3])[:1], [("", "要素が 3 個（1〜2 個にする）")])
        self.assertIn(("[2]", "文字列にする（いまは 3）"), self.errors(s, ["a", "a", 3]))
        self.assertEqual(self.errors({"minItems": 1}, []), [("", "要素が 0 個（1 個以上にする）")])

    def test_combinators(self):
        s = {"allOf": [{"if": {"required": ["k"]}, "then": {"required": ["v"], "x-message": "k があるときは v"},
                        "else": {"properties": {"v": {"type": "null"}}}}]}
        self.assertEqual(self.errors(s, {"k": 1}), [("v", "k があるときは v")])
        self.assertEqual(self.errors(s, {"v": 1}), [("v", "nullにする（いまは 1）")])
        self.assertEqual(self.errors(s, {"k": 1, "v": 1}), [])
        self.assertEqual(self.errors({"anyOf": [{"type": "string"}, {"type": "null"}]}, 1), [("", "どの形にも合わない")])
        self.assertEqual(self.errors({"not": {"required": ["a"]}}, {"a": 1}), [("", "この形にはできない")])
        self.assertEqual(self.errors({"definitions": {"d": {"type": "string"}}, "properties": {"a": {"$ref": "#/definitions/d"}}},
                                     {"a": 1}), [("a", "文字列にする（いまは 1）")])

    def test_issue_where(self):
        self.assertEqual(SchemaIssue(("routes", 0, "to", 1), "m").where, "routes[0].to[1]")
        self.assertEqual(SchemaIssue((), "m").format(), "m")
        self.assertEqual(SchemaIssue(("a",), "m").format(), "a: m")

    def test_load_validator(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "s.json"
            p.write_text("{", encoding="utf-8")
            with self.assertRaises(SchemaError):
                load_validator(p)
            p.write_text('{"type": "string"}', encoding="utf-8")
            self.assertTrue(load_validator(p).is_valid("x"))


# ---------------------------------------------------------------- 台帳と生成


class LedgerCase(unittest.TestCase):
    """試験の置き場所を一時フォルダに写し、本物の schema/keys.yml を置く。"""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "lib"
        shutil.copytree(FIXTURE, self.root)
        shutil.copy(REPO / "schema" / "keys.yml", self.root / "schema" / "keys.yml")

    def tearDown(self):
        self._tmp.cleanup()

    def built(self, root: Path | None = None) -> dict[str, object]:
        root = root or self.root
        return {b.section.name: b for b in build_all(load_ledger(root), load_site(root))}

    def schema(self, name: str) -> dict:
        return self.built()[name].schema

    def replace(self, rel: str, old: str, new: str) -> None:
        p = self.root / rel
        text = p.read_text(encoding="utf-8")
        self.assertIn(old, text)
        p.write_text(text.replace(old, new, 1), encoding="utf-8")

    def ledger_errors(self, old: str, new: str) -> list[str]:
        self.replace("schema/keys.yml", old, new)
        return load_ledger(self.root).errors


class TestLedger(LedgerCase):
    def test_real_ledger(self):
        ledger = load_ledger(REPO)
        self.assertEqual(ledger.errors, [])
        self.assertEqual(list(ledger.sections), ["page", "facts", "sources", "outdated-advice", "inspection"])
        self.assertEqual(ledger.catalog_keys(),
                         ["id", "title", "nav_title", "aliases", "type", "chapter", "level", "priority", "surfaces",
                          "principle", "prevents", "pitfalls", "scenes", "summary", "signs", "wave", "prerequisites",
                          "related", "routes", "tracks", "outdated_advice", "volatility", "sections"])

    def test_page_keys_match_design(self):
        """keys.yml の page のキーが、design §3.3 のキーの台帳の表のキーと同じ（並びも）。"""
        keys = make_schema.design_keys((REPO / "planning" / "design.md").read_text(encoding="utf-8"))
        self.assertEqual(keys, list(load_ledger(REPO).sections["page"].keys))
        self.assertEqual(make_schema.design_notes(REPO, load_ledger(REPO)), [])

    def test_design_keys_parsing(self):
        text = ("## 3. x\n### 3.3 台帳\n| キー | 必須 |\n| --- | --- |\n| `id` | 全 |\n| `type`・`field` | 全 |\n"
                "| 書式 `text` | |\n\n### 3.4 次\n| `other` | |\n")
        self.assertEqual(make_schema.design_keys(text), ["id", "type", "field"])
        self.assertIsNone(make_schema.design_keys("## 1. なし\n"))

    def test_ledger_errors(self):
        cases = [
            ("      title:\n        required: all\n        format: text\n",
             "      title:\n        required: always\n        format: txt\n        colour: red\n",
             ["条件が読めない", "知らない書式", "知らない項目「colour」"]),
            ("        required: {types: [symptom]}\n        forbidden: {types_except: [symptom]}\n",
             "        required: {kinds: [symptom]}\n        forbidden: optional\n", ["条件が読めない", "条件が読めない"]),
            ("              required: {without: table}", "              required: {without: tabel}", ["ほかのキーでない"]),
            ("      aliases:\n        format: texts\n", "      aliases:\n        format: texts\n        non_empty: true\n",
             ["required の条件と組にする"]),
            ("      summary:\n        required: all\n        format: text\n",
             "      summary:\n        required: all\n        format: text\n        min_items: 1\n        min_keys: 1\n",
             ["リストの書式", "object の書式"]),
            ("    output: inspection.schema.json", "    output: page.schema.json", ["同じ"]),
            ("id_base: https://raw.githubusercontent.com/yuukougun/claude-atlas/main/schema/", "id_base: x", ["id_base"]),
        ]
        for old, new, words in cases:
            with self.subTest(new=new):
                shutil.copy(REPO / "schema" / "keys.yml", self.root / "schema" / "keys.yml")
                errors = self.ledger_errors(old, new)
                for w in words:
                    self.assertTrue(any(w in e for e in errors), (w, errors))
                with self.assertRaises(ValueError):
                    build_all(load_ledger(self.root), load_site(self.root))

    def test_stage_condition_needs_stage_key(self):
        errors = self.ledger_errors("            id: {required: all, format: id, note: 目次の registry",
                                    "            id: {required: {stages: [done]}, format: id, note: 目次の registry")
        self.assertTrue(any("stage があるときだけ" in e for e in errors), errors)


class TestBuild(LedgerCase):
    def test_fixture_site_has_every_vocab(self):
        self.assertEqual([n for b in self.built().values() for n in b.notes], [])

    def test_missing_vocab_is_noted_and_left_as_text(self):
        # 本物の keys.yml と、channels を除いた site.yml で作る（本物の site.yml の語彙の有無に頼らない）
        import shutil, tempfile
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            (tmp / "schema").mkdir()
            shutil.copy(REPO / "schema" / "keys.yml", tmp / "schema" / "keys.yml")
            lines = (REPO / "schema" / "site.yml").read_text(encoding="utf-8").splitlines(keepends=True)
            (tmp / "schema" / "site.yml").write_text("".join(l for l in lines if not l.startswith("channels:")), encoding="utf-8")
            built = {b.section.name: b for b in build_all(load_ledger(tmp), load_site(tmp))}
        notes = [n for b in built.values() for n in b.notes]
        self.assertTrue(any("channels" in n for n in notes))
        channel = built["page"].schema["properties"]["verified_with"]["properties"]["channel"]
        self.assertEqual(channel["type"], "string")
        self.assertNotIn("enum", channel)
        fixture_channel = self.schema("page")["properties"]["verified_with"]["properties"]["channel"]
        self.assertEqual(fixture_channel["enum"], ["latest", "stable"])

    def test_vocab_comes_from_site_yml(self):
        self.replace("schema/site.yml", "levels: [使う, 整える, 任せる, 仕組みにする, 回す]",
                     "levels: [使う, 整える, 任せる, 仕組みにする, 回す, 試す]")
        self.replace("schema/site.yml", "types_without_level: [ledger, guide, hub]", "types_without_level: [ledger, guide]")
        page = self.schema("page")
        self.assertEqual(page["properties"]["level"]["enum"][-1], "試す")
        forbid = [x for x in page["allOf"] if "level" in x["then"].get("properties", {})][0]
        self.assertEqual(forbid["if"]["properties"]["type"]["enum"], ["ledger", "guide"])
        require = [x for x in page["allOf"] if x["then"].get("required") == ["level"]][0]
        self.assertIn("hub", require["if"]["properties"]["type"]["enum"])

    def test_deterministic_output(self):
        a = [b.text for b in self.built().values()]
        b = [b.text for b in self.built().values()]
        self.assertEqual(a, b)
        for text in a:
            self.assertEqual(json.loads(text), json.loads(text))
            self.assertTrue(text.endswith("}\n"))

    def test_dumps(self):
        self.assertEqual(dumps({"a": [1, 2]}), '{"a": [1, 2]}\n')
        wrapped = dumps({"k": ["あいうえお"] * 20}, width=60)
        lines = wrapped.splitlines()
        self.assertEqual(lines[0], "{")
        self.assertTrue(all(len(line.encode("utf-8")) < 200 for line in lines))
        self.assertEqual(json.loads(wrapped), {"k": ["あいうえお"] * 20})
        nested = {"a": {"b": {"c": list(range(40))}}}
        self.assertEqual(json.loads(dumps(nested, width=40)), nested)

    def test_schemas_are_valid_draft_07(self):
        if jsonschema is None:
            self.skipTest("jsonschema がない")
        for root in (self.root, REPO):
            for b in self.built(root).values():
                jsonschema.Draft7Validator.check_schema(b.schema)
                Validator(b.schema)                  # 小さな検査器も読める（知らないキーワードがない）


# ---------------------------------------------------------------- 作った schema の当てはまり

# (ファイル, 変える場所, 新しい値, 誤りになる場所)。場所は SchemaIssue.where の形。誤りの場所が空なら通る
PAGE_MUTATIONS = [
    ("how-to-use", ("id",), "How_To", {"id"}),
    ("how-to-use", ("title",), DELETE, {"title"}),
    ("how-to-use", ("type",), "page", {"type"}),
    ("how-to-use", ("type",), DELETE, {"type"}),                       # level の必須は重ねて出さない
    ("how-to-use", ("level",), "使う", {"level"}),                      # guide は level を持たない
    ("how-to-use", ("level",), None, {"level"}),                       # 持たないキーは null も書かない
    ("request-vs-lock", ("level",), DELETE, {"level"}),                # concept は level を持つ
    ("request-vs-lock", ("stage",), "draft", {"verified", "verified_with"}),   # draft は verified を持たない
    ("request-vs-lock", ("verified",), DELETE, set()),               # reviewed でも verified は任意（decisions 2026-11-05「段階 reviewed の付け方」）
    ("request-vs-lock", ("verified",), "2026-02-30", {"verified"}),
    ("request-vs-lock", ("verified_with",), {}, {"verified_with"}),
    ("request-vs-lock", ("verified_with",), {"claude_code": "2.1", "channel": "beta"},
     {"verified_with.claude_code", "verified_with.channel"}),
    ("request-vs-lock", ("checked",), "2026-10-32", {"checked"}),
    ("request-vs-lock", ("surfaces",), ["web"], {"surfaces[0]"}),
    ("request-vs-lock", ("sources",), DELETE, {"sources"}),            # concept は sources を持つ
    ("request-vs-lock", ("routes",), [{"cause": "縛っていない", "to": ["x"]}], {"routes"}),   # symptom だけ
    ("instructions-ignored", ("routes",), DELETE, {"routes"}),
    ("instructions-ignored", ("routes",), [], {"routes"}),
    ("instructions-ignored", ("routes",), [{"cause": "謎", "to": []}], {"routes[0].cause", "routes[0].to"}),
    ("instructions-ignored", ("routes", 0, "to", 0), "Hooks#x", {"routes[0].to[0]"}),
    ("hooks-basics", ("tracks",), [], {"tracks"}),
    ("hooks-basics", ("tracks",), DELETE, {"tracks"}),
    ("how-to-use", ("sources",), [], set()),                           # guide は sources を持たなくてよい
    ("how-to-use", ("wave",), True, {"wave"}),
    ("how-to-use", ("order",), -1, {"order"}),
    ("how-to-use", ("order",), "10", {"order"}),
    ("how-to-use", ("unknown_key",), 1, {"unknown_key"}),
    ("how-to-use", ("prerequisites",), ["request-vs-lock#two-layers"], {"prerequisites[0]"}),
    ("how-to-use", ("related",), ["a", "a"], {"related"}),
    ("how-to-use", ("signs",), [{"type": "wish", "text": "x", "extra": 1}], {"signs[0].type", "signs[0].extra"}),
    ("how-to-use", ("sections",), [{"title": "t", "anchor": "Bad Anchor", "level": "上級"}],
     {"sections[0].anchor", "sections[0].level"}),
    ("how-to-use", ("nav_title",), None, set()),
    ("how-to-use", ("nav_title",), "", {"nav_title"}),
    ("how-to-use", ("updated",), "2026/11/04", {"updated"}),
    ("how-to-use", ("field",), "nowhere", {"field"}),
    ("how-to-use", ("volatility",), "最高", {"volatility"}),
    ("how-to-use", ("aliases",), "単独の文字列", {"aliases"}),
    ("how-to-use", ("stage",), "published", {"stage"}),
]
DATA_MUTATIONS = [
    ("data/facts.yml", ("facts", 0, "value"), DELETE, {"facts[0].value"}),       # value か table のどちらか
    ("data/facts.yml", ("facts", 1, "value"), 1, {"facts[1].value"}),            # table と value の両方は持たない
    ("data/facts.yml", ("facts", 0, "value"), [1, [2]], {"facts[0].value[1]"}),
    ("data/facts.yml", ("facts", 0, "value"), [], {"facts[0].value"}),
    ("data/facts.yml", ("facts", 0, "sources"), [], {"facts[0].sources"}),
    ("data/facts.yml", ("facts", 0, "status"), "たぶん", {"facts[0].status"}),
    ("data/facts.yml", ("facts", 0, "checked"), 20261015, {"facts[0].checked"}),
    ("data/facts.yml", ("facts", 0, "match"), {}, {"facts[0].match"}),
    ("data/facts.yml", ("facts", 0, "match"), {"pattern": "("}, {"facts[0].match.pattern"}),
    ("data/facts.yml", ("facts", 1, "table", "columns"), [], {"facts[1].table.columns"}),
    ("data/facts.yml", ("facts", 1, "table", "columns", 0), "API", {"facts[1].table.columns[0]"}),
    ("data/facts.yml", ("facts", 1, "table", "cells", 0, "app"), {"note": "x"}, {"facts[1].table.cells[0].app.value"}),
    ("data/facts.yml", ("facts", 1, "table", "cells", 0, "api"), ["high"], {"facts[1].table.cells[0].api"}),
    ("data/facts.yml", ("facts", 1, "conflict"), [], {"facts[1].conflict"}),
    ("data/facts.yml", ("features", 0, "page"), DELETE, {"features[0].page"}),
    ("data/facts.yml", ("features", 0, "maturity"), "安定", {"features[0].maturity"}),
    ("data/facts.yml", ("features", 0, "since"), {"claude_code": "v2"}, {"features[0].since.claude_code"}),
    ("data/facts.yml", ("features", 0, "survives_compaction"), None, set()),
    ("data/facts.yml", ("names", 0, "old"), [], {"names[0].old"}),
    ("data/facts.yml", ("names", 0, "changed"), {"date": "2026-13"}, {"names[0].changed.date"}),
    ("data/facts.yml", ("names", 0, "changed"), {"date": "2026-02-30"}, {"names[0].changed.date"}),
    ("data/facts.yml", ("names", 0, "changed"), {"date": 2026}, set()),          # 年だけ（YAML の整数）
    ("data/facts.yml", ("names", 0, "changed"), {"date": 26}, {"names[0].changed.date"}),
    ("data/facts.yml", ("extra",), [], {"extra"}),
    ("data/sources.yml", ("domains", 0, "domain"), "Example.com", {"domains[0].domain"}),
    ("data/sources.yml", ("domains", 0, "noai"), DELETE, {"domains[0].noai"}),
    ("data/sources.yml", ("domains", 0, "noai"), None, set()),
    ("data/sources.yml", ("sources", 0, "kind"), "噂", {"sources[0].kind"}),
    ("data/sources.yml", ("sources", 0, "url"), "example.com/x", {"sources[0].url"}),
    ("data/sources.yml", ("sources", 0, "lang"), "日本語", {"sources[0].lang"}),
    ("data/sources.yml", ("sources", 1, "published"), "2026-9", {"sources[1].published"}),
    ("data/outdated-advice.yml", ("advice", 0, "changed"), DELETE, {"advice[0].changed"}),
    ("data/outdated-advice.yml", ("advice", 1, "changed"), {"date": "2026-10"}, {"advice[1].changed"}),
    ("data/outdated-advice.yml", ("advice", 0, "principle"), [], {"advice[0].principle"}),
    ("data/outdated-advice.yml", ("advice", 0, "status"), "廃止", {"advice[0].status"}),
    ("data/inspection.yml", ("last", "date"), DELETE, {"last.date"}),
    ("data/inspection.yml", ("last", "claude_code"), "latest", {"last.claude_code"}),
    ("data/inspection.yml", ("last",), None, {"last"}),
]


class TestGeneratedSchemas(LedgerCase):
    def setUp(self):
        super().setUp()
        built = self.built()
        self.schemas = {name: b.schema for name, b in built.items()}
        self.pages = {p.id: to_jsonable(p.raw) for p in load_docs(self.root, load_site(self.root)).pages}
        self.data = {f: to_jsonable(read_yaml(self.root / f).data) for f in DATA_SCHEMAS}

    def check(self, schema: dict, inst, expected: set[str], label: str) -> None:
        got = {i.where for i in Validator(schema).errors(inst)}
        self.assertEqual(got, expected, label)
        if jsonschema is not None:
            jerrors = list(json_validator(schema).iter_errors(inst))
            self.assertEqual(bool(jerrors), bool(expected), f"{label}: jsonschema と食い違う {[e.message for e in jerrors]}")

    def test_fixture_is_valid(self):
        for pid, fm in self.pages.items():
            self.check(self.schemas["page"], fm, set(), pid)
        for f, name in DATA_SCHEMAS.items():
            self.check(self.schemas[name], self.data[f], set(), f)

    def test_page_mutations(self):
        for pid, path, value, expected in PAGE_MUTATIONS:
            with self.subTest(page=pid, path=path, value=value):
                fm = copy.deepcopy(self.pages[pid])
                change(fm, path, value)
                self.check(self.schemas["page"], fm, expected, f"{pid} {path}")

    def test_data_mutations(self):
        for f, path, value, expected in DATA_MUTATIONS:
            with self.subTest(file=f, path=path, value=value):
                data = copy.deepcopy(self.data[f])
                change(data, path, value)
                self.check(self.schemas[DATA_SCHEMAS[f]], data, expected, f"{f} {path}")

    def test_messages_explain_the_rule(self):
        fm = copy.deepcopy(self.pages["how-to-use"])
        fm["level"] = "使う"
        msg = Validator(self.schemas["page"]).errors(fm)[0].message
        self.assertIn("ledger・guide・hub", msg)
        self.assertIn("level を書かない", msg)
        fm = copy.deepcopy(self.pages["instructions-ignored"])
        del fm["routes"]
        self.assertEqual(Validator(self.schemas["page"]).errors(fm)[0].message, "routes がない（type が symptom のページは書く）")

    def test_real_data_templates_are_valid(self):
        for f, name in DATA_SCHEMAS.items():
            if not (REPO / f).exists():
                continue
            v = load_validator(REPO / "schema" / f"{name}.schema.json")
            self.assertEqual(v.errors(to_jsonable(read_yaml(REPO / f).data)), [], f)


class TestSkeletonShape(unittest.TestCase):
    def test_catalog_pages_fit_the_page_schema(self):
        """本物の目次の全ページを骨格の形にすると、本物の page.schema.json に通る。"""
        ledger = load_ledger(REPO)
        keys = ledger.catalog_keys()
        catalog = load_catalog(REPO)
        v = load_validator(REPO / "schema" / "page.schema.json")
        jv = json_validator(json.loads((REPO / "schema" / "page.schema.json").read_text(encoding="utf-8"))) if jsonschema else None
        bad = []
        for ff in catalog.files.values():
            for i, p in enumerate(ff.pages):
                fm = {k: p.raw[k] for k in keys if k in p.raw}
                fm.update(field=ff.field, order=(i + 1) * 10, stage="stub", updated="2026-11-04")
                if p.type not in ("guide", "hub"):
                    fm["sources"] = []
                fm = to_jsonable(fm)
                bad += [f"{p.id}: {e.format()}" for e in v.errors(fm)]
                if jv is not None:
                    bad += [f"{p.id}: jsonschema: {e.message}" for e in jv.iter_errors(fm)]
        self.assertEqual(bad, [])
        self.assertTrue(catalog.pages)


# ---------------------------------------------------------------- 道具の入口


class TestMakeSchemaCli(LedgerCase):
    def run_cli(self, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = make_schema.main(["--root", str(self.root), *args])
        return code, out.getvalue(), err.getvalue()

    def test_write_then_check(self):
        code, out, _ = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertEqual(out.count("古い: "), 5)
        self.assertFalse((self.root / "schema" / "page.schema.json").exists())     # --check は書かない
        code, out, _ = self.run_cli()
        self.assertEqual((code, out.count("書いた: ")), (0, 5))
        code, out, _ = self.run_cli("--check")
        self.assertEqual((code, out.count("最新: ")), (0, 5))
        self.assertNotIn("注: ", out)
        self.replace("schema/site.yml", "channels: [latest, stable]", "channels: [latest, stable, nightly]")
        code, out, _ = self.run_cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("古い: schema/page.schema.json", out)
        self.assertIn("最新: schema/facts.schema.json", out)
        code, out, _ = self.run_cli()
        self.assertEqual((code, out.count("書いた: ")), (0, 1))

    def test_notes_do_not_change_the_exit_code(self):
        self.replace("schema/site.yml", "channels: [latest, stable]", "unused_channels: [latest, stable]")
        self.run_cli()
        code, out, _ = self.run_cli("--check")
        self.assertEqual(code, 0)
        self.assertIn("注: site.yml に channels がない", out)

    def test_errors(self):
        self.replace("schema/keys.yml", "        format: {vocab: types}", "        format: {vocab: types, x: 1}")
        code, _, err = self.run_cli()
        self.assertEqual(code, 1)
        self.assertIn("台帳の誤り: ", err)
        (self.root / "schema" / "keys.yml").write_text("sections: [\n", encoding="utf-8")
        self.assertEqual(self.run_cli()[0], 2)
        (self.root / "schema" / "keys.yml").unlink()
        self.assertEqual(self.run_cli()[0], 2)

    def test_real_repo_schemas_are_up_to_date(self):
        """本物の schema/*.schema.json が、keys.yml と site.yml から作り直したものと同じ（作り直し忘れがない）。"""
        built, notes = make_schema.build(REPO)
        for b in built:
            self.assertEqual((REPO / b.path).read_text(encoding="utf-8"), b.text,
                             f"{b.path} が古い（uv run python tools/make_schema.py で作り直す）")
        self.assertFalse([n for n in notes if "design.md" in n], notes)
        self.assertFalse([n for n in notes if "が site.yml の" in n], notes)   # 台帳が名指しする型・段階は site.yml にある


if __name__ == "__main__":
    unittest.main()
