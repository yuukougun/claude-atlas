"""作る層を本物の目次と本物のリポジトリで確かめる試験。`uv run python -m unittest discover -s tests/tools` で動く。

- 本物の目次（planning/catalog/。読むだけ）から骨格の形のサイトを一時フォルダに作り（B2 の報告 §4.6 の形：キーの台帳の
  catalog のキー＋field・order・stage・updated・sources: []）、wave: 1 のページを draft で docs/ に、ほかを stubs/ に置いて
  生成する：注意が出ない・公開するのは第一波の核だけ・生成物のリンクは公開するページだけを指す・--check が通る・
  MkDocs の --strict のビルドが通る。全ページを draft にしても注意が出ず、作り直しても同じ
- 本物の作る層の設定（tools/gen/config.yml）：site.yml の語彙にすべて表示の言葉がある・逆引きの分野から章への対応表と
  hosts が目次に合う
- 本物のリポジトリの生成物が最新（gen_site.py --check。生成物を commit する決まり。design §8.4）
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

from gen_helpers import FIXTURE, REPO, run_cli
from lib.catalog import load_catalog
from lib.ledger import load_ledger
from lib.site import load_site
from lib.yamlio import to_jsonable

LINK_RE = re.compile(r"\]\(([^)\s]+\.md)(#[^)]*)?\)")


def make_catalog_site(root: Path, draft: str) -> list[str]:
    """本物の目次から骨格の形のサイトを作る。draft は all（全ページを docs/ に draft）か wave（wave: 1 だけ）。
    docs/ に置いたページの本文には、sections の見出し・症状の診断の節の routes・本体を生成するページの目印を置く。
    docs/ に置いたページの id を返す。"""
    (root / "schema").mkdir(parents=True)
    shutil.copy(REPO / "schema" / "site.yml", root / "schema" / "site.yml")
    shutil.copytree(REPO / "data", root / "data")
    mk = (FIXTURE / "mkdocs.yml").read_text(encoding="utf-8").replace("https://example.com/atlas/",
                                                                       "https://yuukougun.github.io/claude-atlas/")
    (root / "mkdocs.yml").write_text(mk, encoding="utf-8")
    (root / "docs").mkdir()
    (root / "docs" / "index.md").write_text("# トップ\n\n<!-- link:begin reverse-index --><!-- link:end -->\n", encoding="utf-8")
    hosts = (yaml.safe_load((REPO / "tools/gen/config.yml").read_text(encoding="utf-8")) or {}).get("hosts") or {}
    keys = load_ledger(REPO).catalog_keys()
    catalog = load_catalog(REPO)
    placed = []
    for ff in catalog.files.values():
        for i, p in enumerate(ff.pages):
            fm = {k: p.raw[k] for k in keys if k in p.raw}
            in_docs = draft == "all" or (draft == "wave" and p.is_wave)
            fm.update(field=ff.field, order=(i + 1) * 10, stage="draft" if in_docs else "stub", updated="2026-11-04")
            if p.type not in ("guide", "hub"):
                fm["sources"] = []
            text = "---\n" + yaml.safe_dump(to_jsonable(fm), allow_unicode=True, sort_keys=False, width=1000) + "---\n"
            if in_docs:
                pre = "・".join(f"<!-- link:begin {r.raw} --><!-- link:end -->" for r in p.prerequisites)
                body = ["", f"試しの本文。前提は {pre}。" if pre else "試しの本文。", ""]
                for s in p.sections:
                    body += [f"## {s.get('title')} {{#{s.get('anchor')}}}", "", "試しの本文。", ""]
                    if s.get("anchor") == "diagnosis" and p.type == "symptom":
                        body += ["<!-- gen:begin routes -->", "<!-- gen:end routes -->", ""]
                for name in hosts.get(p.id, []):
                    body += [f"<!-- gen:begin {name} -->", f"<!-- gen:end {name} -->", ""]
                text += "\n".join(body)
                placed.append(p.id)
            path = root / ("docs" if in_docs else "stubs") / ff.field / f"{p.id}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    return placed


class CatalogSiteCase(unittest.TestCase):
    draft = "wave"

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls._tmp.name) / "site"
        cls.placed = make_catalog_site(cls.root, cls.draft)
        cls.code, cls.out, cls.err = run_cli("--root", str(cls.root))

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()


class TestWaveSite(CatalogSiteCase):
    def test_generates_without_notes(self):
        self.assertEqual(self.code, 0, self.out + self.err)
        self.assertNotIn("注意:", self.out)
        self.assertIn(f"公開するページ {len(self.placed)}（", self.out)
        self.assertTrue(len(self.placed) > 30)

    def test_nav_has_only_the_wave(self):
        nav = (self.root / "nav.yml").read_text(encoding="utf-8")
        pages = re.findall(r": ([a-z]+/[a-z0-9-]+\.md)$", nav, re.M)
        self.assertEqual(sorted(p.split("/")[1][:-3] for p in pages if not p.startswith("lists/")), sorted(self.placed))
        self.assertNotIn("\nexclude_docs:", nav)            # docs/ に公開しないページがない

    def test_links_point_only_to_published_pages(self):
        docs = self.root / "docs"
        for path in docs.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for m in LINK_RE.finditer(text):
                target = (path.parent / m.group(1)).resolve()
                self.assertTrue(target.exists(), f"{path.relative_to(self.root)} → {m.group(1)}")
                self.assertTrue(str(target).startswith(str(docs.resolve())), m.group(1))

    def test_check_is_clean(self):
        code, out, _ = run_cli("--root", str(self.root), "--check")
        self.assertEqual(code, 0, out)

    def test_mkdocs_strict(self):
        try:
            import mkdocs  # noqa: F401
        except ImportError:
            self.skipTest("mkdocs がない")
        env = dict(os.environ, NO_MKDOCS_2_WARNING="1")
        r = subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-d", str(self.root / "site")],
                           cwd=self.root, capture_output=True, text=True, env=env, timeout=600)
        self.assertEqual(r.returncode, 0, r.stdout[-3000:] + r.stderr[-3000:])


class TestAllDraftSite(CatalogSiteCase):
    draft = "all"

    def test_generates_without_notes_and_is_stable(self):
        self.assertEqual(self.code, 0, self.out + self.err)
        self.assertNotIn("注意:", self.out)
        self.assertEqual(len(self.placed), len(load_catalog(REPO).pages))
        code, out, _ = run_cli("--root", str(self.root), "--check")
        self.assertEqual(code, 0, out)

    def test_every_symptom_page_has_its_routes_table(self):
        for path in (self.root / "docs" / "symptoms").glob("*.md"):
            if path.name == "index.md":
                continue
            text = path.read_text(encoding="utf-8")
            self.assertRegex(text, r"<!-- gen:begin routes -->\n<!-- textlint-disable -->\n\n\| 原因 \|", path.name)


class TestRealConfig(unittest.TestCase):
    def setUp(self):
        self.cfg = yaml.safe_load((REPO / "tools/gen/config.yml").read_text(encoding="utf-8"))
        self.site = load_site(REPO)

    def test_labels_cover_the_vocabulary(self):
        labels = self.cfg["labels"]
        for kind, vocab in [("types", "types"), ("stages", "stages"), ("surfaces", "surfaces"), ("sign_types", "sign_types")]:
            self.assertEqual(set(labels[kind]), set(self.site.vocab(vocab)), kind)
        self.assertEqual(set(labels["cause_axes"]), {"prevents", "pitfalls"})
        for item in self.cfg["lists"]["pages"]:
            self.assertIsNotNone(self.site.vocab(item["vocab"]), item)
        roles = self.cfg["roles"]
        self.assertIn(roles["symptom_type"], self.site.types)
        self.assertIn(roles["feature_type"], self.site.types)
        self.assertIn(roles["symptom_field"], self.site.fields)
        self.assertIn(roles["fact_confirmed"], self.site.vocab("fact_statuses"))
        self.assertIsInstance(self.cfg["held_back"], list)

    def test_reverse_and_hosts_fit_the_catalog(self):
        catalog = load_catalog(REPO)
        symptoms = catalog.chapters(self.cfg["roles"]["symptom_field"])
        mapping = self.cfg["reverse"]["field_to_symptom_chapter"]
        self.assertTrue(set(mapping) <= set(self.site.fields))
        self.assertTrue(set(mapping.values()) <= set(symptoms), set(mapping.values()) - set(symptoms))
        ids = {p.id for p in catalog.pages}
        self.assertTrue(set(self.cfg["hosts"]) <= ids, set(self.cfg["hosts"]) - ids)
        self.assertEqual(set(self.cfg["reverse"]["group"]), set(self.site.vocab("sign_types")))


class TestRealRepository(unittest.TestCase):
    def test_generated_files_are_fresh(self):
        """本物のリポジトリの生成物（nav.yml・llms.txt・サイト用のデータなど）が、作り直したものと同じ。"""
        code, out, err = run_cli("--root", str(REPO), "--check")
        self.assertEqual(code, 0, out + err)


if __name__ == "__main__":
    unittest.main()
