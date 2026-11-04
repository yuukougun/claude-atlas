"""読む層（tools/lib/）の、読む部品の試験：yamlio・site・markdown・pages・catalog・data。
`uv run python -m unittest discover -s tests/tools` で動く。

fixtures/lib/ は、指摘の出ない小さな置き場所（schema/site.yml は本物の写しに、工程6a の B2 の提案の語彙を足したもの。
docs/ のページ3つ・stubs/ の骨格のページ1つ・生成物・サイトのトップ、data/ の各ファイル。値はすべて試験用の作りもので、ドメインは example.*）。
試験は、それを一時フォルダに写して1か所だけ変える。目次の読み方は、tools/check_catalog.py（目次の検査）と同じ結果に
なることを、check_catalog の試験の目次（fixtures/small/。読むだけ）と本物の目次で確かめる。
"""
from __future__ import annotations

import datetime
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "lib"
SMALL = Path(__file__).resolve().parent / "fixtures" / "small"

from lib import Fatal, load_catalog, load_data, load_docs, load_site  # noqa: E402
from lib.base import Ref, partial_date_key, parse_date  # noqa: E402
from lib.data import DATA_FILES, SOURCES_D_SECTIONS, host_of, url_key  # noqa: E402
from lib.ledger import load_ledger  # noqa: E402
from lib.markdown import find_headings, find_markers, fenced_mask, split_front_matter  # noqa: E402
from lib.yamlio import LineDict, line_at, parse_yaml, read_yaml, to_jsonable  # noqa: E402


class FixtureCase(unittest.TestCase):
    """fixtures/lib を一時フォルダに写す。"""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "lib"
        shutil.copytree(FIXTURE, self.root)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel: str, text: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")

    def replace(self, rel: str, old: str, new: str) -> None:
        text = self.read(rel)
        self.assertIn(old, text)
        self.write(rel, text.replace(old, new, 1))

    def docs(self):
        return load_docs(self.root, load_site(self.root))


# ---------------------------------------------------------------- yamlio


class TestYaml(unittest.TestCase):
    def test_lines_and_key_lines(self):
        doc = parse_yaml("a: 1\nb:\n  c: 2\n  d: [x, y]\n", line_offset=1)
        self.assertIsNone(doc.error)
        self.assertIsInstance(doc.data, LineDict)
        self.assertEqual(doc.data.line, 2)
        self.assertEqual(doc.data.key_lines, {"a": 2, "b": 3})
        self.assertEqual(doc.data["b"].line, 4)
        self.assertEqual(doc.data["b"].key_lines, {"c": 4, "d": 5})

    def test_duplicate_keys_are_recorded(self):
        doc = parse_yaml("a: 1\nb: 2\na: 3\n")
        self.assertEqual(doc.data["a"], 3)
        self.assertEqual(doc.duplicates, [("a", 3, 1)])
        self.assertEqual([p.kind for p in doc.problems("x.yml")], ["YAML"])
        self.assertEqual(doc.problems("x.yml")[0].line, 3)

    def test_dates_stay_strings(self):
        doc = parse_yaml("d: 2026-11-04\ne: 2026-13-45\nf: 2026\ng: 2026-10\n")
        self.assertEqual(doc.data, {"d": "2026-11-04", "e": "2026-13-45", "f": 2026, "g": "2026-10"})
        self.assertEqual(parse_date(doc.data["d"]), datetime.date(2026, 11, 4))
        self.assertIsNone(parse_date(doc.data["e"]))
        self.assertIsNone(parse_date("2026-11-4"))
        self.assertEqual(parse_date(datetime.date(2026, 1, 2)), datetime.date(2026, 1, 2))

    def test_partial_dates(self):
        self.assertEqual(partial_date_key("2026"), (2026,))
        self.assertEqual(partial_date_key(2026), (2026,))
        self.assertEqual(partial_date_key("2026-10"), (2026, 10))
        self.assertEqual(partial_date_key("2026-10-27"), (2026, 10, 27))
        for bad in ("2026-13", "2026-02-30", "26-10", "2026/10", True, 12, None):
            self.assertIsNone(partial_date_key(bad), bad)
        self.assertLess(partial_date_key("2026-09"), partial_date_key("2026-10-01"))

    def test_broken_yaml_has_the_file_line(self):
        doc = parse_yaml("a: 1\nb: [x\n", line_offset=1)
        self.assertIsNotNone(doc.error)
        self.assertIsNone(doc.data)
        self.assertEqual(doc.error_line, 4)
        self.assertIn("4 行", doc.error)

    def test_explicit_timestamp_error_does_not_stop(self):
        doc = parse_yaml("d: !!timestamp 2026-13-45\n")
        self.assertIsNotNone(doc.error)

    def test_line_at(self):
        doc = parse_yaml("a: 1\nroutes:\n  - cause: x\n    to: [p, q]\n  - cause: y\n")
        self.assertEqual(line_at(doc.data, ("routes", 1, "cause")), 5)
        self.assertEqual(line_at(doc.data, ("routes", 0, "to", 1)), 4)
        self.assertEqual(line_at(doc.data, ("missing",)), 1)
        self.assertEqual(line_at(doc.data, ()), 1)

    def test_to_jsonable(self):
        self.assertEqual(to_jsonable({1: datetime.date(2026, 1, 2), "s": {3, 1}, "t": (1,)}),
                         {"1": "2026-01-02", "s": [1, 3], "t": [1]})

    def test_read_yaml_missing_file(self):
        doc = read_yaml(Path(tempfile.gettempdir()) / "no-such-file-for-lib-test.yml")
        self.assertIn("ファイルが読めない", doc.error)


# ---------------------------------------------------------------- site


class TestSite(FixtureCase):
    def test_real_site_yml(self):
        site = load_site(REPO)
        self.assertEqual(len(site.fields), 23)
        self.assertEqual(site.fields[0], "start")
        self.assertEqual(site.vocab("fields"), site.fields)
        self.assertEqual(site.field_titles["symptoms"], "症状辞典")
        self.assertEqual(site.vocab("volatility_days"), ["低", "中", "高"])
        self.assertEqual(site.volatility_days, {"低": 365, "中": 90, "高": 30})
        self.assertEqual(site.vocab(["prevents", "pitfalls"]), site.causes)
        self.assertEqual(len(site.causes), 11)
        self.assertIsNone(site.vocab("no-such-key"))
        self.assertIsNone(site.vocab(["prevents", "no-such-key"]))
        self.assertEqual(site.rank("levels")["使う"], 0)
        self.assertEqual(site.default_fact_volatility, "高")       # site.yml にないので、期限のいちばん短いもの
        self.assertEqual(site.published_stages, ["draft", "reviewed", "done"])   # stages の最初のほか
        self.assertEqual(site.guard_fields, ["verify", "eval", "enforce", "safety"])
        self.assertEqual(site.problems, [])

    def test_explicit_values(self):
        self.replace("schema/site.yml", "default_fact_volatility: 高", "default_fact_volatility: 中")
        self.replace("schema/site.yml", "published_stages: [draft, reviewed, done]", "published_stages: [reviewed, done]")
        site = load_site(self.root)
        self.assertEqual(site.default_fact_volatility, "中")
        self.assertEqual(site.published_stages, ["reviewed", "done"])

    def test_missing_or_broken_site_yml_is_fatal(self):
        (self.root / "schema" / "site.yml").unlink()
        with self.assertRaises(Fatal):
            load_site(self.root)
        self.write("schema/site.yml", "fields: [\n")
        with self.assertRaises(Fatal):
            load_site(self.root)
        self.write("schema/site.yml", "types: [concept]\n")
        with self.assertRaises(Fatal):
            load_site(self.root)

    def test_field_without_id_is_a_problem(self):
        self.replace("schema/site.yml", "  - {id: start, title: 入口と地図}", "  - {title: 入口と地図}")
        site = load_site(self.root)
        self.assertNotIn("start", site.fields)
        self.assertEqual([p.kind for p in site.problems], ["設定"])


# ---------------------------------------------------------------- markdown


class TestMarkdown(unittest.TestCase):
    def test_split_front_matter(self):
        self.assertEqual(split_front_matter("# t\n"), (None, "# t\n", 1, None))
        self.assertEqual(split_front_matter("---\na: 1\n---\nbody\n"), ("a: 1", "body\n", 4, None))
        self.assertEqual(split_front_matter("---\na: 1\n...\nbody"), ("a: 1", "body", 4, None))
        self.assertEqual(split_front_matter("---  \na: 1\n---\n"), ("a: 1", "", 4, None))
        fm, body, line, err = split_front_matter("---\na: 1\n")
        self.assertIsNone(fm)
        self.assertIn("閉じていない", err)

    def lines(self, text: str):
        lines = text.split("\n")
        return text, lines, fenced_mask(lines)

    def test_headings(self):
        text, lines, mask = self.lines("# 題\n\n## 節 {#sec-a}\n\n```\n## コードの中\n```\n### 閉じ ###\n####### 7つ\n#タグ\n")
        hs = find_headings(lines, mask, 10)
        self.assertEqual([(h.level, h.text, h.anchor, h.line) for h in hs],
                         [(1, "題", None, 10), (2, "節", "sec-a", 12), (3, "閉じ", None, 17)])

    def markers(self, text: str):
        text, lines, mask = self.lines(text)
        return find_markers(text, lines, mask, 5, "docs/x/y.md", "y")

    def test_markers_pairs_and_offsets(self):
        text = ("前 <!-- fact:begin limit -->100<!-- fact:end --> 後\n"
                "<!-- gen:begin snippet hooks/block -->\n中身\n<!-- gen:end snippet hooks/block -->\n"
                "<!--link:begin hooks-basics#exit-codes-->フック<!--   link:end   -->\n")
        ms, problems = self.markers(text)
        self.assertEqual(problems, [])
        self.assertEqual([(m.kind, m.arg, m.line, m.end_line) for m in ms],
                         [("fact", "limit", 5, 5), ("gen", "snippet hooks/block", 6, 8),
                          ("link", "hooks-basics#exit-codes", 9, 9)])
        self.assertEqual(ms[0].content(text), "100")
        self.assertEqual(ms[1].content(text), "\n中身\n")
        self.assertEqual(text[ms[1].start:ms[1].inner_start], "<!-- gen:begin snippet hooks/block -->")
        self.assertEqual(text[ms[1].inner_end:ms[1].stop], "<!-- gen:end snippet hooks/block -->")
        self.assertEqual(ms[2].content(text), "フック")

    def test_different_kinds_can_nest(self):
        ms, problems = self.markers("<!-- gen:begin table -->\n| <!-- fact:begin a -->1<!-- fact:end --> |\n"
                                    "<!-- gen:end table -->\n")
        self.assertEqual(problems, [])
        self.assertEqual([m.kind for m in ms], ["gen", "fact"])

    def test_markers_in_code_are_not_read(self):
        ms, problems = self.markers("`<!-- fact:begin a -->`\n```\n<!-- gen:begin x -->\n```\n~~~\n<!-- link:end -->\n~~~\n")
        self.assertEqual((ms, problems), ([], []))

    def test_marker_problems(self):
        cases = {
            "<!-- fact:begin a -->x": "閉じていない",
            "<!-- fact:end -->": "begin のない",
            "<!-- gen:begin a -->\n<!-- gen:end b -->": "違う",
            "<!-- gen:begin a -->\n<!-- gen:end -->": "gen:end に名前がない",
            "<!-- fact:begin -->x<!-- fact:end -->": "名前",
            "<!-- fact:begin a -->x<!-- fact:begin b -->y<!-- fact:end -->": "入れ子",
        }
        for text, words in cases.items():
            with self.subTest(text=text):
                ms, problems = self.markers(text)
                self.assertTrue(problems)
                self.assertIn(words, " ".join(p.message for p in problems))
                self.assertTrue(all(p.kind == "目印" and p.id == "y" and p.file == "docs/x/y.md" for p in problems))

    def test_fact_end_may_repeat_the_id(self):
        ms, problems = self.markers("<!-- fact:begin a -->1<!-- fact:end a -->")
        self.assertEqual((len(ms), problems), (1, []))


# ---------------------------------------------------------------- pages


class TestDocs(FixtureCase):
    def test_fixture_is_clean(self):
        docs = self.docs()
        self.assertEqual(docs.all_problems(), [])
        self.assertEqual([p.id for p in docs.pages], ["request-vs-lock", "how-to-use", "instructions-ignored", "hooks-basics"])
        self.assertEqual([p.base for p in docs.pages], ["docs", "docs", "docs", "stubs"])   # docs/ を先に、stubs/ を後に
        self.assertEqual(sorted(docs.generated), ["docs/lists/by-level.md", "docs/start/index.md"])
        self.assertEqual([o.shown for o in docs.others], ["docs/index.md"])
        self.assertEqual(docs.duplicate_ids(), {})

    def test_page_model(self):
        p = {p.id: p for p in self.docs().pages}["instructions-ignored"]
        self.assertEqual((p.field, p.meta_field, p.stem, p.rel), ("symptoms", "symptoms", "instructions-ignored",
                                                                  "symptoms/instructions-ignored.md"))
        self.assertEqual(p.file, "docs/symptoms/instructions-ignored.md")
        self.assertEqual(p.url, "symptoms/instructions-ignored/")
        self.assertEqual((p.type, p.level, p.stage, p.volatility), ("symptom", "整える", "draft", "中"))
        self.assertTrue(p.is_wave)
        self.assertEqual(p.prerequisites, [Ref("request-vs-lock", "request-vs-lock", None)])
        self.assertEqual([(r.cause, [t.raw for t in r.to]) for r in p.routes], [("縛っていない", ["hooks-basics#exit-codes"])])
        self.assertEqual(p.route_targets()[0].anchor, "exit-codes")
        self.assertEqual(p.signs, [("symptom", "試験用の困りごと1"), ("symptom", "試験用の困りごと2")])
        self.assertEqual(p.anchors(), ["diagnosis"])
        self.assertEqual(p.heading_anchors(), ["diagnosis", "references"])
        self.assertEqual(p.fact_ids(), ["sample-limit", "sample-default-effort"])
        self.assertEqual([r.raw for r in p.link_refs()], ["hooks-basics#exit-codes"])
        self.assertEqual(p.gen_names(), ["routes", "references"])
        self.assertEqual(p.date("updated"), datetime.date(2026, 11, 4))
        self.assertEqual(p.key_line("routes"), p.key_line("prerequisites") + 1)
        self.assertEqual(p.body_line, 32)
        self.assertEqual(p.markers[0].line, 37)

    def test_id_falls_back_to_the_file_name(self):
        self.replace("docs/start/how-to-use.md", "id: how-to-use\n", "")
        p = {p.stem: p for p in self.docs().pages}["how-to-use"]
        self.assertIsNone(p.declared_id)
        self.assertEqual(p.id, "how-to-use")

    def test_front_matter_problems(self):
        self.write("docs/start/no-front-matter.md", "# 題\n")
        self.write("docs/start/unclosed.md", "---\nid: unclosed\n")
        self.write("docs/start/broken.md", "---\nid: broken\ntitle: [x\n---\n")
        self.write("docs/start/not-a-mapping.md", "---\n- a\n---\n")
        self.write("docs/start/empty.md", "---\n\n---\n")
        self.write("docs/start/duplicate.md", "---\nid: a\nid: b\n---\n")
        got = {p.stem: [(x.kind, x.line) for x in p.problems] for p in self.docs().pages if p.problems}
        self.assertEqual(got, {"no-front-matter": [("front matter", 1)], "unclosed": [("front matter", 1)],
                               "broken": [("YAML", 3)], "not-a-mapping": [("front matter", 1)],
                               "empty": [("front matter", 1)], "duplicate": [("YAML", 3)]})

    def test_misplaced_markdown(self):
        self.write("docs/notes.md", "# メモ\n")
        self.write("docs/start/sub/deep.md", "---\nid: deep\n---\n")
        self.write("docs/unknown-field/x.md", "---\nid: x\n---\n")
        self.write("stubs/index.md", "# stubs にトップは置かない\n")              # トップと生成物は docs/ だけ
        self.write("stubs/lists/by-field.md", "# stubs に一覧は置かない\n")
        self.write("stubs/start/index.md", "---\nid: index\n---\n")
        docs = self.docs()
        self.assertEqual(sorted(p.file for p in docs.problems if p.kind == "置き場所"),
                         ["docs/notes.md", "docs/start/sub/deep.md", "docs/unknown-field/x.md", "stubs/index.md",
                          "stubs/lists/by-field.md", "stubs/start/index.md"])
        self.assertNotIn("deep", [p.id for p in docs.pages])
        self.assertNotIn("index", [p.id for p in docs.pages])
        self.assertNotIn("stubs/lists/by-field.md", docs.generated)

    def test_marker_problems_belong_to_the_page(self):
        self.replace("docs/symptoms/instructions-ignored.md", "<!-- gen:end routes -->", "")
        p = {p.id: p for p in self.docs().pages}["instructions-ignored"]
        self.assertEqual([(x.kind, x.id) for x in p.problems], [("目印", "instructions-ignored")])

    def test_stubs_are_read(self):
        p = {p.id: p for p in self.docs().pages}["hooks-basics"]
        self.assertEqual((p.base, p.in_docs, p.file, p.rel, p.url, p.stage),
                         ("stubs", False, "stubs/enforce/hooks-basics.md", "enforce/hooks-basics.md", "enforce/hooks-basics/",
                          "stub"))
        only_docs = load_docs(self.root, load_site(self.root), dirs=("docs",))
        self.assertNotIn("hooks-basics", [p.id for p in only_docs.pages])

    def test_same_id_in_docs_and_stubs(self):
        """stub を draft にして docs/ へ移したのに stubs/ に残した、など。読む層は両方を残して duplicate_ids に出す。"""
        self.write("stubs/start/how-to-use.md", "---\nid: how-to-use\nstage: stub\n---\n")
        self.write("stubs/basics/moved.md", "---\nid: instructions-ignored\nstage: stub\n---\n")   # 分野もファイル名も違う
        dups = self.docs().duplicate_ids()
        self.assertEqual({pid: [p.file for p in ps] for pid, ps in dups.items()},
                         {"how-to-use": ["docs/start/how-to-use.md", "stubs/start/how-to-use.md"],
                          "instructions-ignored": ["docs/symptoms/instructions-ignored.md", "stubs/basics/moved.md"]})

    def test_bom_and_crlf(self):
        text = self.read("docs/start/how-to-use.md").replace("\n", "\r\n")
        (self.root / "docs/start/how-to-use.md").write_bytes(b"\xef\xbb\xbf" + text.encode("utf-8"))
        p = {p.id: p for p in self.docs().pages}["how-to-use"]
        self.assertEqual((p.problems, p.title, p.stage), ([], "この辞典の引き方", "draft"))


# ---------------------------------------------------------------- catalog


def check_catalog_module():
    import check_catalog
    return check_catalog


class TestCatalog(unittest.TestCase):
    """lib の目次の読み方が、tools/check_catalog.py の読む層と同じページ・同じ値を返す。"""

    def assertSameAsCheckCatalog(self, root: Path):
        cc = check_catalog_module()
        theirs = cc.load_catalog(root)
        ours = load_catalog(root)
        self.assertEqual(list(ours.files), list(theirs.files))
        self.assertEqual([(p.id, p.field, p.index) for p in ours.pages], [(p.id, p.field, p.index) for p in theirs.pages])
        self.assertEqual([p.raw for p in ours.pages], [p.raw for p in theirs.pages])
        for kind in ("merged", "dropped"):
            self.assertEqual(ours.ids_of(kind), [e.id for ff in theirs.files.values() for e in getattr(ff, kind) if e.id])
        self.assertEqual(ours.ids_of("pages"), [e.id for e in theirs.registry.candidates if e.id])
        self.assertEqual(ours.ids_of("ledger"), [e.id for e in theirs.registry.ledger if e.id])
        self.assertEqual(ours.stray, theirs.stray)
        for f, ff in ours.files.items():
            self.assertEqual(ff.chapters, cc.as_strings(theirs.files[f].raw.get("chapters")))
        for ours_p, theirs_p in zip(ours.pages, theirs.pages):
            self.assertEqual(ours_p.anchors(), theirs_p.anchors())
            self.assertEqual([r.raw for r in ours_p.prerequisites], [r.raw for r in theirs_p.refs("prerequisites")])
            self.assertEqual(ours_p.is_wave, theirs_p.is_wave)
            self.assertEqual(ours_p.line, theirs_p.line)
        return ours

    def test_same_as_check_catalog_on_its_fixture(self):
        cat = self.assertSameAsCheckCatalog(SMALL)
        self.assertEqual(cat.problems, [])
        self.assertIn("eval", cat.site.fields)
        self.assertNotIn("eval", cat.files)          # まだ分野のファイルがない分野

    def test_same_as_check_catalog_on_the_real_catalog(self):
        cat = self.assertSameAsCheckCatalog(REPO)
        self.assertEqual(cat.problems, [])
        self.assertEqual(len(cat.pages), len(cat.by_id))
        page = cat.by_id["instructions-ignored"]
        self.assertEqual(page.kind, "catalog")
        self.assertEqual(page.field, "symptoms")
        self.assertTrue(page.materials)
        self.assertEqual(cat.chapters("symptoms")[0], "返答と品質")

    def test_problems_match_check_catalog_findings(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "small"
            shutil.copytree(SMALL, root)
            p = root / "planning" / "catalog" / "basics.yaml"
            p.write_text(p.read_text(encoding="utf-8") + "\n  - id: [broken\n", encoding="utf-8")
            (root / "planning" / "catalog" / "stray.yaml").write_text("pages: []\n", encoding="utf-8")
            cc = check_catalog_module()
            theirs = [(f.file, f.line) for f in cc.load_catalog(root).findings if f.check == "YAML"]
            ours = load_catalog(root)
            self.assertEqual([(x.file, x.line) for x in ours.problems if x.kind == "YAML"], theirs)
            self.assertEqual(ours.stray, ["planning/catalog/stray.yaml"])
            self.assertNotIn("basics", [f for f, ff in ours.files.items() if ff.readable])


# ---------------------------------------------------------------- data


class TestData(FixtureCase):
    def test_fixture(self):
        data = load_data(self.root)
        self.assertEqual(data.problems, [])
        self.assertEqual(list(data.facts), ["sample-limit", "sample-default-effort"])
        self.assertEqual(list(data.features), ["sample-hooks"])
        self.assertEqual(list(data.names), ["sample-rename"])
        self.assertEqual(list(data.sources), ["sample-doc", "sample-blog", "sample-note"])   # sources.d を後に足す
        self.assertEqual(data.sources["sample-note"].file, "data/sources.d/instructions-ignored.yml")
        self.assertEqual(list(data.domains), ["example.com", "example.org", "example.net"])
        self.assertEqual(list(data.advice), ["sample-caps", "sample-renamed"])
        self.assertEqual(data.facts["sample-limit"].checked, datetime.date(2026, 10, 15))
        self.assertEqual(data.facts["sample-limit"].volatility, "中")
        self.assertEqual(data.facts["sample-limit"].key_line("checked"), 10)
        self.assertEqual(data.last_inspection()["claude_code"], "2.1.317")
        self.assertEqual(data.noai_domains(), ["example.org"])

    def test_domain_lookup(self):
        data = load_data(self.root)
        self.assertEqual(data.domain_entry("https://blog.example.com/post").id, "example.com")
        self.assertEqual(data.domain_entry("EXAMPLE.org").id, "example.org")
        self.assertIsNone(data.domain_entry("https://example.co.jp/"))
        self.assertIsNone(data.domain_entry("localhost"))

    def test_duplicates_are_kept_in_entries(self):
        self.write("data/sources.d/how-to-use.yml",
                   "sources:\n  - {id: sample-doc, url: https://example.com/other, title: t, kind: 研究, publisher: p,"
                   " lang: ja, checked: 2026-11-01}\n")
        data = load_data(self.root)
        self.assertEqual([s.file for s in data.entries("sources") if s.id == "sample-doc"],
                         ["data/sources.yml", "data/sources.d/how-to-use.yml"])
        self.assertEqual(data.sources["sample-doc"].file, "data/sources.yml")   # index は最初のもの

    def test_missing_and_broken_files(self):
        (self.root / "data" / "outdated-advice.yml").unlink()
        self.write("data/facts.yml", "facts: [\n")
        self.write("data/sources.d/x.yaml", "sources: []\n")
        self.write("data/inspection.yml", "")
        data = load_data(self.root)
        got = sorted((p.file, p.kind) for p in data.problems)
        self.assertEqual(got, [("data/facts.yml", "YAML"), ("data/inspection.yml", "形"),
                               ("data/outdated-advice.yml", "設定"), ("data/sources.d/x.yaml", "置き場所")])
        self.assertEqual(data.facts, {})
        self.assertEqual(data.last_inspection(), {})

    def test_url_helpers(self):
        self.assertEqual(url_key("HTTPS://Example.COM:443/docs/Limit/#top"), "https://example.com/docs/Limit")
        self.assertEqual(url_key("https://example.com/"), url_key("https://example.com"))
        self.assertEqual(url_key("http://example.com:8080/a?b=1"), "http://example.com:8080/a?b=1")
        self.assertEqual(host_of("https://Sub.Example.com/x"), "sub.example.com")
        self.assertEqual(host_of("example.com/x"), "example.com")

    def test_sections_match_the_ledger(self):
        """data.py の DATA_FILES・SOURCES_D_SECTIONS が、schema/keys.yml の各節の最上位のキーと同じ。"""
        ledger = load_ledger(REPO)
        by_file = {f: sec for sec in ledger.sections.values() for f in sec.files}
        for shown, sections in DATA_FILES.items():
            self.assertEqual(tuple(by_file[shown].keys), sections, shown)
        self.assertEqual(tuple(by_file["data/sources.d/<id>.yml"].keys), SOURCES_D_SECTIONS)
        self.assertEqual(tuple(by_file["data/inspection.yml"].keys), ("last",))

    def test_real_data_reads_without_problems(self):
        """本物の data/ が、読む層の指摘なしに読める（中身は 6b から増えるので数は見ない。形は test_lib_schema）。"""
        data = load_data(REPO)
        self.assertEqual(data.problems, [])
        self.assertLessEqual(set(DATA_FILES) | {"data/inspection.yml"}, set(data.files))
        self.assertEqual(set(data.last_inspection()), {"date", "claude_code", "release_notes", "news"})


if __name__ == "__main__":
    unittest.main()
