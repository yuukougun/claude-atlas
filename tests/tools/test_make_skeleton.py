"""骨格の道具（tools/make_skeleton.py。工程6c）の試験。`uv run python -m unittest discover -s tests/tools` で動く。

- 試験用の小さな目次（fixtures/skeleton/。本物の schema/ を写して当てる）から作った骨格が、本物の page.schema.json に
  通り（読む層の検査器と jsonschema の両方）、目次のキーを写し、決めた本文（sections の見出しと routes の目印）を持つ
- すでに docs/ か stubs/ にあるページは上書きしない。--force は stubs/ のものだけを作り直し、updated のほかが同じなら書かない
- --check が目次と stubs/ の front matter の差（ない・値の違い・置き場所・読めない・重なり・目次にない）を見つけ、書かない
- --dry-run は書かない。作れないとき（schema・site.yml がない、目次が壊れている、schema に通らない）は1ページも書かずに 2
- 骨格だけのサイトで check_pages.py のエラーが0（data が空なので、tracks・outdated_advice の参照は骨格の警告になる）
- 本物の目次（planning/catalog/。読むだけ）の全ページの骨格が page.schema.json に通り、--check が差を出さない
"""
from __future__ import annotations

import contextlib
import datetime
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "skeleton"
DATE = "2026-11-04"

import check_pages  # noqa: E402
import make_skeleton  # noqa: E402
from lib.catalog import CATALOG_ONLY_KEYS, load_catalog  # noqa: E402
from lib.ledger import load_ledger  # noqa: E402
from lib.markdown import split_front_matter  # noqa: E402
from lib.pages import load_docs  # noqa: E402
from lib.schema import load_validator  # noqa: E402
from lib.site import load_site  # noqa: E402
from lib.yamlio import parse_yaml, to_jsonable  # noqa: E402

try:
    import jsonschema
except ImportError:          # 照らし合わせだけに使う（なければその部分を飛ばす）
    jsonschema = None

WRITER_ONLY = ("verified", "verified_with", "checked")


def run(root: Path, *args: str) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = make_skeleton.main(["--root", str(root), "--date", DATE, *args])
    return code, out.getvalue(), err.getvalue()


def json_validator(root: Path):
    schema = json.loads((root / "schema" / "page.schema.json").read_text(encoding="utf-8"))
    return jsonschema.Draft7Validator(schema, format_checker=jsonschema.FormatChecker())


def schema_errors(root: Path, pages) -> list[str]:
    """読む層の検査器と jsonschema（あれば）の誤り。"""
    v = load_validator(root / "schema" / "page.schema.json")
    jv = json_validator(root) if jsonschema else None
    bad = []
    for p in pages:
        fm = to_jsonable(p.raw)
        bad += [f"{p.id}: {e.format()}" for e in v.errors(fm)]
        if jv is not None:
            bad += [f"{p.id}: jsonschema: {e.message}" for e in jv.iter_errors(fm)]
    return bad


def body_of(text: str) -> str:
    return split_front_matter(text)[1]


class SkeletonCase(unittest.TestCase):
    """fixtures/skeleton と本物の schema/ を一時フォルダに写す。"""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "site"
        shutil.copytree(FIXTURE, self.root)
        shutil.copytree(REPO / "schema", self.root / "schema")

    def tearDown(self):
        self._tmp.cleanup()

    def tool(self, *args: str) -> tuple[int, str, str]:
        return run(self.root, *args)

    def made(self) -> tuple[int, str, str]:
        code, out, err = self.tool()
        self.assertEqual(code, 0, out + err)
        return code, out, err

    def path(self, rel: str) -> Path:
        return self.root / rel

    def read(self, rel: str) -> str:
        return self.path(rel).read_text(encoding="utf-8")

    def write(self, rel: str, text: str) -> None:
        self.path(rel).parent.mkdir(parents=True, exist_ok=True)
        self.path(rel).write_text(text, encoding="utf-8")

    def replace(self, rel: str, old: str, new: str) -> None:
        text = self.read(rel)
        self.assertIn(old, text, rel)
        self.write(rel, text.replace(old, new, 1))

    def edit_front_matter(self, rel: str, change) -> None:
        """骨格の front matter を読んで change(dict) で変え、同じ書き方で書き戻す（本文はそのまま）。"""
        text = self.read(rel)
        fm, body, _, err = split_front_matter(text)
        self.assertIsNone(err)
        meta = to_jsonable(parse_yaml(fm).data)
        change(meta)
        self.write(rel, "---\n" + make_skeleton.dump_front_matter(meta, {"updated"}) + "---\n" + body)

    def snapshot(self) -> dict[str, str]:
        out = {}
        for base in ("docs", "stubs"):
            d = self.root / base
            if d.is_dir():
                out.update({p.relative_to(self.root).as_posix(): p.read_text(encoding="utf-8") for p in sorted(d.rglob("*"))
                            if p.is_file()})
        return out

    def stub_pages(self):
        docs = load_docs(self.root, load_site(self.root))
        self.assertEqual([x.format() for x in docs.all_problems()], [])
        return {p.id: p for p in docs.pages if not p.in_docs}


# ---------------------------------------------------------------- 作るもの


class TestMake(SkeletonCase):
    def test_makes_every_catalog_page(self):
        _, out, err = self.made()
        catalog = load_catalog(self.root)
        want = sorted(f"{p.field}/{p.id}.md" for p in catalog.pages)
        got = sorted(p.relative_to(self.root / "stubs").as_posix() for p in (self.root / "stubs").rglob("*")
                     if p.is_file())
        self.assertEqual(got, want)                       # stubs/ には <field>/<id>.md だけ
        self.assertIn(f"目次 {len(want)} ページ（6 分野）：作った {len(want)}・書かない 0", out)
        self.assertIn("作った骨格の分野ごとの数：start 2・basics 1・enforce 3・judgment 1・symptoms 2・changes 1", out)
        self.assertNotIn("注意:", out)
        self.assertEqual(err, "")
        self.assertFalse((self.root / "docs").exists())   # docs/ には書かない

    def test_stubs_fit_the_page_schema(self):
        self.made()
        pages = self.stub_pages()
        self.assertEqual(len(pages), 10)
        self.assertEqual(schema_errors(self.root, pages.values()), [])

    def test_front_matter_copies_the_catalog(self):
        self.made()
        pages = self.stub_pages()
        ledger = load_ledger(self.root)
        keys = ledger.catalog_keys()
        order = list(ledger.sections["page"].keys)
        site = load_site(self.root)
        for ff in load_catalog(self.root).files.values():
            for i, p in enumerate(ff.pages):
                fm = to_jsonable(pages[p.id].raw)
                want = {k: to_jsonable(p.raw[k]) for k in keys if p.raw.get(k) is not None}
                self.assertEqual({k: fm.get(k) for k in want}, want, p.id)
                for k in keys:
                    if p.raw.get(k) is None:
                        self.assertNotIn(k, fm, f"{p.id}: 目次にないか null の {k} は書かない")
                self.assertEqual((fm["field"], fm["order"], fm["stage"], fm["updated"]),
                                 (ff.field, (i + 1) * 10, site.stages[0], DATE), p.id)
                self.assertEqual(list(fm), [k for k in order if k in fm], f"{p.id}: キーの並びは keys.yml の順")
                for k in CATALOG_ONLY_KEYS + WRITER_ONLY:
                    self.assertNotIn(k, fm, p.id)
                if p.type in ("guide", "hub"):        # keys.yml の sources の required（types_except: [guide, hub]）
                    self.assertNotIn("sources", fm, p.id)
                else:
                    self.assertEqual(fm["sources"], [], p.id)
        self.assertEqual(set(pages), {p.id for p in load_catalog(self.root).pages})
        self.assertNotIn("nav_title", to_jsonable(pages["how-to-use"].raw))           # 目次は nav_title: null
        self.assertEqual(pages["instructions-ignored"].raw["nav_title"], "指示が守られない")
        self.assertEqual(pages["hook-vs-skill"].raw["sections"], [])                    # 空のリストは目次のとおり

    def test_strings_stay_strings(self):
        """YAML で文字列でない値に読まれかねない語も、文字列のまま読める（読む層と、MkDocs と同じ PyYAML の SafeLoader）。
        updated は引用符なしの日付（design §3.3 の例の形）。"""
        self.made()
        text = self.read("stubs/basics/request-vs-lock.md")
        want = ["yes", "null", "2026-11-04", "1.0", "a: b", "#タグ", "CLAUDE.md, rules", "[角かっこ]"]
        self.assertEqual(self.stub_pages()["request-vs-lock"].raw["aliases"], want)
        fm = yaml.safe_load(split_front_matter(text)[0])
        self.assertEqual(fm["aliases"], want)
        self.assertEqual(fm["updated"], datetime.date(2026, 11, 4))
        self.assertIn("\nupdated: 2026-11-04\n", text)

    def test_layout_follows_the_design_example(self):
        self.made()
        text = self.read("stubs/symptoms/instructions-ignored.md")
        self.assertTrue(text.startswith("---\nid: instructions-ignored\ntitle: CLAUDE.md や指示が守られない\n"))
        for line in ("aliases: [指示を無視される]", "surfaces: [claude-code, app]", "pitfalls: []", "signs:",
                     "  - {type: symptom, text: CLAUDE.md に書いたのに守られない}", "wave: 1", "routes:",
                     "  - {cause: 散らかっている, to: [outdated-advice-ledger]}",
                     "  - {cause: 縛っていない, to: [hooks-basics#exit-codes, hook-recipes]}", "sources: []",
                     "  - {title: 原因を安く確かめる順, anchor: diagnosis}", "stage: stub", "updated: 2026-11-04"):
            self.assertIn("\n" + line + "\n", text)
        self.assertNotIn("materials", text)
        self.assertNotIn("visual", text)


class TestBody(SkeletonCase):
    def test_section_headings_and_routes_marker(self):
        self.made()
        pages = self.stub_pages()
        for p in load_catalog(self.root).pages:
            body = body_of(self.read(f"stubs/{p.field}/{p.id}.md"))
            lines = [x for x in body.split("\n") if x]
            heads = [x for x in lines if x.startswith("#")]
            self.assertEqual(heads, [f"## {s['title']} {{#{s['anchor']}}}" for s in p.sections], p.id)   # H1 は置かない
            self.assertEqual(pages[p.id].heading_anchors(), [s["anchor"] for s in p.sections], p.id)
            gen = [m for m in pages[p.id].markers if m.kind == "gen"]
            if p.routes:
                self.assertEqual([(m.name, m.closed) for m in gen], [("routes", True)], p.id)
                k = lines.index("## 原因を安く確かめる順 {#diagnosis}")
                self.assertEqual(lines[k + 1:k + 3], list(make_skeleton.ROUTES_MARKER), p.id)   # 診断の節の見出しの下
            else:
                self.assertEqual(gen, [], p.id)
            if not p.sections and not p.routes:
                self.assertEqual(body, "", p.id)
        body = body_of(self.read("stubs/symptoms/blocked-by-a-rule.md"))
        self.assertEqual(body, "\n## 何に止められたか {#what-stopped}\n\n## 原因を安く確かめる順 {#diagnosis}\n\n"
                               "<!-- gen:begin routes -->\n<!-- gen:end routes -->\n\n## 面ごとの違い {#by-surface}\n")
        self.assertEqual(self.read("stubs/start/knowledge-map.md").split("---\n")[-1], "")      # 節のないページは本文なし

    def test_routes_marker_without_diagnosis_section(self):
        self.replace("planning/catalog/symptoms.yaml", '      - {title: "原因を安く確かめる順", anchor: diagnosis}\n'
                                                       '      - {title: "面ごとの違い", anchor: by-surface}\n',
                     '      - {title: "面ごとの違い", anchor: by-surface}\n')
        _, out, _ = self.made()
        body = body_of(self.read("stubs/symptoms/blocked-by-a-rule.md"))
        self.assertTrue(body.endswith("## 面ごとの違い {#by-surface}\n\n<!-- gen:begin routes -->\n<!-- gen:end routes -->\n"))
        self.assertIn("注意: stubs/symptoms/blocked-by-a-rule.md: 診断の節（anchor が diagnosis）がないので、routes の目印を"
                      "本文の最後に置いた", out)

    def test_names_match_the_generator_and_the_real_catalog(self):
        """routes の目印の名前は作る層の生成の部分にあり、本物の目次の routes を持つページはすべて診断の節を持つ。"""
        import gen
        self.assertIn(make_skeleton.ROUTES_BLOCK, gen.REGISTRY)
        with_routes = [p for p in load_catalog(REPO).pages if p.routes]
        self.assertTrue(with_routes)
        for p in with_routes:
            self.assertIn(make_skeleton.ROUTES_SECTION, p.anchors(), p.id)


# ---------------------------------------------------------------- 上書きしない・--force


class TestOverwrite(SkeletonCase):
    DOCS_PAGE = "docs/symptoms/instructions-ignored.md"

    def place_docs_page(self) -> str:
        """骨格を作る前に、draft のページを docs/ に置く（目次と違う題名で）。"""
        text = ("---\nid: instructions-ignored\ntitle: 書きかけの題名\ntype: symptom\nfield: symptoms\nstage: draft\n---\n\n"
                "書きかけの本文。\n")
        self.write(self.DOCS_PAGE, text)
        return text

    def test_existing_pages_are_not_overwritten(self):
        docs_text = self.place_docs_page()
        _, out, _ = self.made()
        self.assertIn("作った 9・書かない 1（docs/ にある 1・stubs/ にある 0・ほかの分野にある 0）", out)
        self.assertFalse(self.path("stubs/symptoms/instructions-ignored.md").exists())
        self.replace("stubs/enforce/hooks-basics.md", "title: フック（hooks）の基本", "title: 手で直した題名")
        before = self.snapshot()
        _, out, _ = self.made()
        self.assertIn("作った 0・書かない 10（docs/ にある 1・stubs/ にある 9・ほかの分野にある 0）", out)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(self.read(self.DOCS_PAGE), docs_text)

    def test_force_rewrites_only_changed_stubs(self):
        docs_text = self.place_docs_page()
        self.made()
        self.replace("stubs/enforce/hooks-basics.md", "title: フック（hooks）の基本", "title: 手で直した題名")
        before = self.snapshot()
        code, out, _ = run(self.root, "--force", "--date", "2026-12-01")      # 後の --date が効く
        self.assertEqual(code, 0, out)
        self.assertIn("作った 0・作り直した 1・目次と同じ 8・書かない 1（docs/ にある 1", out)
        self.assertIn("  作り直した stubs/enforce/hooks-basics.md", out)
        after = self.snapshot()
        changed = sorted(k for k in after if after[k] != before.get(k))
        self.assertEqual(changed, ["stubs/enforce/hooks-basics.md"])
        text = after["stubs/enforce/hooks-basics.md"]
        self.assertIn("\ntitle: フック（hooks）の基本\n", text)
        self.assertIn("\nupdated: 2026-12-01\n", text)                 # 作り直したものは、その日
        self.assertIn("\nupdated: 2026-11-04\n", after["stubs/enforce/hook-vs-skill.md"])   # 同じものは書かない
        self.assertEqual(self.read(self.DOCS_PAGE), docs_text)          # docs/ には触れない
        self.assertFalse(self.path("stubs/symptoms/instructions-ignored.md").exists())
        code, out, _ = run(self.root, "--force", "--date", "2026-12-02")
        self.assertIn("作り直した 0・目次と同じ 9", out)
        self.assertEqual(self.snapshot(), after)

    def test_page_in_another_field_folder_is_not_duplicated(self):
        self.made()
        old, new = "stubs/judgment/agreement-is-not-evidence.md", "stubs/start/agreement-is-not-evidence.md"
        self.write(new, self.read(old))
        self.path(old).unlink()
        for args in ((), ("--force",)):
            _, out, _ = self.tool(*args)
            self.assertIn("ほかの分野にある 1", out)
            self.assertIn(f"注意: agreement-is-not-evidence: {new} にある（目次の分野は judgment。{old} へ移すか、目次を直す）", out)
            self.assertFalse(self.path(old).exists())

    def test_force_rewrites_an_unreadable_stub(self):
        self.made()
        self.write("stubs/start/knowledge-map.md", "---\nid: [\n---\n")
        _, out, _ = self.tool()
        self.assertIn("stubs/ にある 10", out)
        self.assertEqual(self.read("stubs/start/knowledge-map.md"), "---\nid: [\n---\n")
        _, out, _ = self.tool("--force")
        self.assertIn("作り直した 1", out)
        self.assertIn("\nid: knowledge-map\n", self.read("stubs/start/knowledge-map.md"))


# ---------------------------------------------------------------- --check・--dry-run


class TestCheck(SkeletonCase):
    def test_clean_after_making(self):
        self.made()
        before = self.snapshot()
        code, out, _ = self.tool("--check")
        self.assertEqual(code, 0, out)
        self.assertEqual(out, "目次と stubs/ の front matter は同じ（目次 10 ページ：stubs/ にある 10・docs/ にあり比べない 0）\n")
        self.assertEqual(self.snapshot(), before)

    def test_finds_differences(self):
        self.made()
        self.replace("stubs/enforce/hooks-basics.md", "title: フック（hooks）の基本", "title: 手で直した題名")
        self.edit_front_matter("stubs/start/knowledge-map.md", lambda m: m.pop("wave"))
        self.edit_front_matter("stubs/start/how-to-use.md",
                               lambda m: m.update(related=["knowledge-map", "agreement-is-not-evidence"]))
        self.edit_front_matter("stubs/symptoms/blocked-by-a-rule.md", lambda m: m["sections"].reverse())
        self.edit_front_matter("stubs/enforce/hook-recipes.md", lambda m: m.update(order=35, updated="2026-12-01",
                                                                                 sources=["some-source"]))
        self.path("stubs/changes/outdated-advice-ledger.md").unlink()
        self.write("stubs/start/agreement-is-not-evidence.md", self.read("stubs/judgment/agreement-is-not-evidence.md"))
        self.path("stubs/judgment/agreement-is-not-evidence.md").unlink()
        self.write("stubs/basics/extra-page.md", "---\nid: extra-page\ntitle: 目次にないページ\nstage: stub\n---\n")
        self.write("stubs/basics/request-vs-lock.md", "---\nid: [\n---\n")
        before = self.snapshot()
        code, out, _ = self.tool("--check")
        self.assertEqual(code, 1, out)
        for line in (
            "差: stubs/enforce/hooks-basics.md: title: 目次 フック（hooks）の基本・stub 手で直した題名",
            "差: stubs/start/knowledge-map.md: wave: 目次 1・stub （なし）",
            "差: stubs/start/how-to-use.md: related: 目次にだけ [request-vs-lock]・stub にだけ [agreement-is-not-evidence]",
            "差: stubs/symptoms/blocked-by-a-rule.md: sections: 並びか数が違う（目次 [{title: 何に止められたか, anchor: "
            "what-stopped}, {title: 原因を安く確かめる順, anchor: diagnosis}, {title: 面ごとの違い, anchor: by-surface}]・"
            "stub [{title: 面ごとの違い, anchor: by-surface}, {title: 原因を安く確かめる順, anchor: diagnosis}, "
            "{title: 何に止められたか, anchor: what-stopped}]）",
            "差: stubs/enforce/hook-recipes.md: order: 目次 30・stub 35",
            "ない: stubs/changes/outdated-advice-ledger.md（planning/catalog/changes.yaml の pages の 1 番目）",
            "置き場所: stubs/start/agreement-is-not-evidence.md: 目次の分野は judgment（stubs/judgment/agreement-is-not-evidence.md"
            " に置く）",
            "読めない: stubs/basics/request-vs-lock.md: front matter が読めない（check_pages.py で直すか、--force で作り直す）",
            "目次にない: stubs/basics/extra-page.md（目次の pages にない id。目次から外したなら消す）",
        ):
            self.assertIn(line + "\n", out)
        self.assertNotIn("updated", out)                 # 道具が足す日と執筆者のキーは比べない
        self.assertNotIn("sources", out)
        self.assertIn("差がある：ない 1・値の違う 5 ページ（5 キー）・置き場所 1・読めない 1・重なり 0・目次にない 1（目次 10 ページ："
                      "stubs/ にある 9・docs/ にあり比べない 0）", out)
        self.assertEqual(self.snapshot(), before)        # --check は書かない

    def test_docs_pages_are_not_compared(self):
        self.made()
        text = self.read("stubs/start/how-to-use.md").replace("stage: stub", "stage: draft").replace(
            "title: この辞典の引き方", "title: 書きかけで変えた題名")
        self.write("docs/start/how-to-use.md", text)
        code, out, _ = self.tool("--check")
        self.assertEqual(code, 1, out)
        self.assertIn("重なり: stubs/start/how-to-use.md: docs/ にも同じ id のページがある（docs/ へ移したなら stubs/ のほうを消す）\n",
                      out)
        self.assertNotIn("差:", out)
        self.path("stubs/start/how-to-use.md").unlink()
        code, out, _ = self.tool("--check")
        self.assertEqual(code, 0, out)
        self.assertIn("stubs/ にある 9・docs/ にあり比べない 1", out)

    def test_check_with_force_is_refused(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err), self.assertRaises(SystemExit) as cm:
            make_skeleton.main(["--root", str(self.root), "--check", "--force"])
        self.assertEqual(cm.exception.code, 2)
        self.assertIn("--check と --force は一緒に使えない", err.getvalue())


class TestDryRun(SkeletonCase):
    def test_writes_nothing(self):
        code, out, _ = self.tool("--dry-run")
        self.assertEqual(code, 0, out)
        self.assertIn("目次 10 ページ（6 分野）：作る 10・書かない 0", out)
        self.assertIn("--dry-run なので書いていない", out)
        self.assertFalse((self.root / "stubs").exists())

    def test_counts_rewrites_with_force(self):
        self.made()
        self.replace("stubs/enforce/hooks-basics.md", "title: フック（hooks）の基本", "title: 手で直した題名")
        before = self.snapshot()
        _, out, _ = self.tool("--dry-run", "--force")
        self.assertIn("作る 0・作り直す 1・目次と同じ 9", out)
        self.assertIn("  作り直す stubs/enforce/hooks-basics.md", out)
        self.assertEqual(self.snapshot(), before)


# ---------------------------------------------------------------- 作れないとき


class TestCannotMake(SkeletonCase):
    def assert_refused(self, *phrases: str) -> None:
        code, out, err = self.tool()
        self.assertEqual(code, 2, out + err)
        for ph in phrases:
            self.assertIn(ph, err)
        self.assertFalse((self.root / "stubs").exists())     # 1ページも書かない

    def test_without_page_schema(self):
        self.path("schema/page.schema.json").unlink()
        self.assert_refused("作れない: schema/page.schema.json がない（uv run python tools/make_schema.py で作る）")

    def test_without_site_yml(self):
        self.path("schema/site.yml").unlink()
        self.assert_refused("作れない: ", "site.yml")

    def test_broken_catalog(self):
        self.write("planning/catalog/judgment.yaml", "field: judgment\npages: [\n")
        self.assert_refused("作れない: 目次が読めない（tools/check_catalog.py で直す）", "planning/catalog/judgment.yaml")

    def test_same_id_twice_in_the_catalog(self):
        text = self.read("planning/catalog/judgment.yaml").replace("  - id: agreement-is-not-evidence",
                                                                   "  - id: hooks-basics")
        self.write("planning/catalog/judgment.yaml", text)
        self.assert_refused("planning/catalog/judgment.yaml: hooks-basics: 同じ id のページが planning/catalog/enforce.yaml にもある")

    def test_front_matter_that_does_not_fit_the_schema(self):
        self.replace("planning/catalog/enforce.yaml", "    tracks: [hooks]\n", "")
        self.replace("planning/catalog/start.yaml", "    priority: 推奨\n", "    priority: そのうち\n")
        self.assert_refused("page.schema.json に通らない（1ページも書かない）",
                            "planning/catalog/enforce.yaml: hooks-basics: ", "tracks",
                            "planning/catalog/start.yaml: knowledge-map: priority")


# ---------------------------------------------------------------- 検査の層と合わせる


class TestWithCheckPages(SkeletonCase):
    def test_skeleton_site_has_no_errors(self):
        """骨格だけのサイト（data は空）で check_pages.py のエラーが0。参照の警告（tracks・outdated_advice）は出てよい。"""
        self.made()
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = check_pages.main(["--root", str(self.root), "--today", DATE])
        self.assertEqual(code, 0, out.getvalue() + err.getvalue())
        self.assertNotIn("エラー:", out.getvalue())
        self.assertIn("エラー 0 件", out.getvalue())
        self.assertIn("stubs/ のページ 10", out.getvalue())


# ---------------------------------------------------------------- 本物の目次


class TestRealCatalog(unittest.TestCase):
    """本物の目次と schema/ を一時フォルダに写して骨格を作る（本物の stubs/ には書かない）。"""

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls._tmp.name) / "site"
        shutil.copytree(REPO / "schema", cls.root / "schema")
        shutil.copytree(REPO / "planning" / "catalog", cls.root / "planning" / "catalog")
        cls.code, cls.out, cls.err = run(cls.root)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_every_page_fits_the_schema(self):
        self.assertEqual(self.code, 0, self.out + self.err)
        self.assertNotIn("注意:", self.out)
        catalog = load_catalog(self.root)
        docs = load_docs(self.root, load_site(self.root))
        self.assertEqual([x.format() for x in docs.all_problems()], [])
        self.assertEqual(sorted(p.id for p in docs.pages), sorted(p.id for p in catalog.pages))
        self.assertEqual(schema_errors(self.root, docs.pages), [])
        self.assertTrue(len(docs.pages) > 300)

    def test_check_is_clean(self):
        code, out, _ = run(self.root, "--check")
        self.assertEqual(code, 0, out)
        self.assertEqual(out.count("\n"), 1)

    def test_symptom_pages_have_the_routes_marker_in_diagnosis(self):
        pages = [p for p in load_catalog(self.root).pages if p.routes]
        self.assertTrue(pages)
        for p in pages:
            lines = [x for x in body_of((self.root / "stubs" / p.field / f"{p.id}.md").read_text(encoding="utf-8")).split("\n") if x]
            k = next(i for i, x in enumerate(lines) if x.endswith("{#diagnosis}"))
            self.assertEqual(lines[k + 1:k + 3], list(make_skeleton.ROUTES_MARKER), p.id)


if __name__ == "__main__":
    unittest.main()
