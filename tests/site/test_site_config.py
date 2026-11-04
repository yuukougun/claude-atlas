"""サイトの設定と CI の試験（planning/design.md §8.1・§8.5・§8.6・§8.8。工程6a の担当 B1）。

`uv run python -m unittest discover -s tests/site` で流す。設計で決めた約束が、設定の書き換えや
テーマの版の上げで崩れていないかを見る。

- 実際の設定（mkdocs.yml に INHERIT の nav.yml を合わせたもの）：プラグインは search だけ、theme.font は false、
  数式と取り込みの記法を入れない、外のサイトの JS・CSS を読まない、冒頭とフッターの文
- mkdocs.yml が nav と exclude_docs を持たない（持つと nav.yml の値を丸ごと上書きする）
- Mermaid の写し：版の文字列・置き場所・sha256・ライセンスの文書がそろう。テーマの bundle が Mermaid に呼ぶ関数が、
  overrides/assets/js/mermaid-local.js の受けるもの（initialize と render）だけである
- ヘッダーのリポジトリのリンク：テーマの部品の写しから data-md-component="source" だけを外した形である
- 依存の版の固定（pyproject.toml と uv.lock）と、ワークフローの形（デプロイは必須の検査の後など）
- ビルドしたサイトの HTML と CSS が、外のサイトの資源（JS・CSS・フォント・画像）を読まない
"""

from __future__ import annotations

import glob
import hashlib
import html.parser
import os
import re
import subprocess
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]

# decisions 2026-11-04「決定の一覧の承認」の最小の文（冒頭とフッター）
HEAD_TEXT = "この辞典は Anthropic の公式の教材ではない。"
FOOT_PARTS = ["© 2026 yuukougun", "本文と図：", "CC BY 4.0", "コードと雛形：", "MIT", "Anthropic の公式の教材ではない"]
SITE_URL = "https://yuukougun.github.io/claude-atlas/"

# テーマの bundle が Mermaid に呼んでよい関数（overrides/assets/js/mermaid-local.js の代わりが受けるもの）
STAND_IN_METHODS = {"initialize", "render"}


def load_effective_config():
    """mkdocs.yml に INHERIT の nav.yml を合わせた、MkDocs が実際に使う設定。"""
    from mkdocs.config import load_config

    cwd = os.getcwd()
    try:
        os.chdir(ROOT)
        return load_config(str(ROOT / "mkdocs.yml"))
    finally:
        os.chdir(cwd)


class _TagTolerantLoader(yaml.SafeLoader):
    """mkdocs.yml の !!python/… の印を None として読む（生の mkdocs.yml のキーを見るため）。"""


_TagTolerantLoader.add_multi_constructor("tag:yaml.org,2002:python/", lambda loader, suffix, node: None)


def read_raw_mkdocs_yml() -> dict:
    with open(ROOT / "mkdocs.yml", encoding="utf-8") as f:
        return yaml.load(f, Loader=_TagTolerantLoader)


def read_workflow(name: str) -> dict:
    with open(ROOT / ".github" / "workflows" / name, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if True in data:  # YAML 1.1 では on が真偽値として読まれる
        data["on"] = data.pop(True)
    return data


def mermaid_local_version() -> str:
    text = (ROOT / "overrides/assets/js/mermaid-local.js").read_text(encoding="utf-8")
    m = re.search(r'var VERSION = "([0-9.]+)";', text)
    if not m:
        raise AssertionError("mermaid-local.js に VERSION がない")
    return m.group(1)


def theme_bundle(package: str) -> str:
    """テーマの bundle（Material か zensical_ui）の中身。"""
    mod = __import__(package)
    base = Path(mod.__file__).parent / "templates" / "assets" / "javascripts"
    found = sorted(base.glob("bundle.*.min.js"))
    if len(found) != 1:
        raise AssertionError(f"{package} の bundle が1つに決まらない: {found}")
    return found[0].read_text(encoding="utf-8")


class EffectiveConfigTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg = load_effective_config()

    def test_plugins_are_search_only(self):
        names = {key.split("/")[-1] for key in self.cfg["plugins"].keys()}
        self.assertEqual(names, {"search"})
        self.assertEqual(dict(self.cfg["hooks"]), {})

    def test_search_is_japanese(self):
        search = [p for k, p in self.cfg["plugins"].items() if k.split("/")[-1] == "search"][0]
        self.assertEqual(search.config["lang"], ["ja"])
        self.assertTrue(search.config["separator"])

    def test_theme_does_not_load_fonts_from_outside(self):
        self.assertIs(self.cfg["theme"]["font"], False)
        self.assertEqual(self.cfg["theme"].name, "material")
        self.assertEqual(self.cfg["theme"]["language"], "ja")
        self.assertNotIn("announce.dismiss", self.cfg["theme"]["features"])

    def test_site_url_and_repo(self):
        self.assertEqual(self.cfg["site_url"], SITE_URL)
        self.assertEqual(self.cfg["repo_url"], "https://github.com/yuukougun/claude-atlas")

    def test_footer_text(self):
        copyright_text = self.cfg["copyright"]
        plain = re.sub(r"<[^>]+>", "", copyright_text)
        self.assertEqual(plain, "© 2026 yuukougun｜本文と図：CC BY 4.0｜コードと雛形：MIT｜Anthropic の公式の教材ではない")
        for part in FOOT_PARTS:
            self.assertIn(part, plain)

    def test_markdown_extensions(self):
        exts = set(self.cfg["markdown_extensions"])
        # 数式（KaTeX）・取り込みの記法（design §6.9）・日本語の強調を壊すもの（kyopro-atlas の記録）は入れない
        for banned in ("pymdownx.arithmatex", "pymdownx.snippets", "pymdownx.betterem"):
            self.assertNotIn(banned, exts)
        for needed in ("attr_list", "pymdownx.superfences", "pymdownx.tabbed", "toc"):
            self.assertIn(needed, exts)
        fences = self.cfg["mdx_configs"]["pymdownx.superfences"]["custom_fences"]
        mermaid = [f for f in fences if f["name"] == "mermaid"]
        self.assertEqual(len(mermaid), 1)
        # テーマは pre.mermaid を図として描く
        self.assertEqual(mermaid[0]["class"], "mermaid")

    def test_no_outside_js_or_css(self):
        for item in list(self.cfg["extra_javascript"]) + list(self.cfg["extra_css"]):
            self.assertNotRegex(str(item), r"^(https?:)?//", "外のサイトの JS・CSS を読まない（design §8.5）")
        self.assertIn("assets/js/mermaid-local.js", [str(x) for x in self.cfg["extra_javascript"]])

    def test_validation_is_strict_friendly(self):
        validation = self.cfg["validation"]
        self.assertEqual(validation["links"]["unrecognized_links"], 30)  # logging.WARNING
        self.assertEqual(validation["links"]["anchors"], 30)
        self.assertEqual(validation["nav"]["omitted_files"], 30)


class RawConfigTest(unittest.TestCase):
    def test_nav_and_exclude_docs_live_in_nav_yml(self):
        raw = read_raw_mkdocs_yml()
        self.assertEqual(raw.get("INHERIT"), "nav.yml")
        # mkdocs.yml の同じキーは nav.yml を丸ごと上書きする（exclude_docs は合わさらない。build-B1.md）
        self.assertNotIn("nav", raw)
        self.assertNotIn("exclude_docs", raw)
        self.assertNotIn("not_in_nav", raw)
        with open(ROOT / "nav.yml", encoding="utf-8") as f:
            nav = yaml.safe_load(f)
        self.assertIn("nav", nav)


class OverridesTest(unittest.TestCase):
    def test_announce_has_the_minimal_sentence(self):
        text = (ROOT / "overrides/main.html").read_text(encoding="utf-8")
        m = re.search(r"{% block announce %}(.*?){% endblock %}", text, re.S)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1).strip(), HEAD_TEXT)

    def test_source_partial_is_theme_copy_without_component(self):
        import material

        def body(t: str) -> str:
            t = re.sub(r"{#-.*?-#}", "", t, flags=re.S)  # Jinja の注釈を除く
            return re.sub(r"\s+", " ", t).strip()

        ours = body((ROOT / "overrides/partials/source.html").read_text(encoding="utf-8"))
        theirs = body((Path(material.__file__).parent / "templates/partials/source.html").read_text(encoding="utf-8"))
        self.assertNotIn("data-md-component", ours)
        self.assertIn('data-md-component="source"', theirs)
        # テーマの部品が変わったら、写しを取り直す（テーマの版を上げたときに気づくため）
        self.assertEqual(ours, theirs.replace(' data-md-component="source"', ""))


class MermaidCopyTest(unittest.TestCase):
    def test_version_dir_hash_and_license(self):
        version = mermaid_local_version()
        vendor = ROOT / "overrides/assets/vendor" / f"mermaid-{version}"
        self.assertTrue((vendor / "mermaid.min.js").is_file())
        self.assertTrue((vendor / "LICENSE").is_file())
        sources = (ROOT / "overrides/assets/vendor/SOURCES.txt").read_text(encoding="utf-8")
        self.assertIn(f"mermaid-{version}/", sources)
        digest = hashlib.sha256((vendor / "mermaid.min.js").read_bytes()).hexdigest()
        self.assertIn(digest, sources, "SOURCES.txt の sha256 と写しが一致しない")
        others = [p.name for p in (ROOT / "overrides/assets/vendor").glob("mermaid-*") if p.name != f"mermaid-{version}"]
        self.assertEqual(others, [], "古い版の写しが残っている")

    def test_copy_is_the_series_material_requests(self):
        bundle = theme_bundle("material")
        m = re.search(r"https://unpkg\.com/mermaid@(\d+)/dist/mermaid\.min\.js", bundle)
        self.assertIsNotNone(m, "Material の Mermaid の読み方が変わった。mermaid-local.js を見直す")
        self.assertEqual(mermaid_local_version().split(".")[0], m.group(1))

    def assert_bundle_contract(self, bundle: str):
        # テーマは window.mermaid がないときだけ外から読む。あれば、それの initialize と render だけを呼ぶ
        self.assertIn('typeof mermaid=="undefined"', bundle)
        called = set(re.findall(r"(?<![\w.$])mermaid\.(\w+)\(", bundle))
        self.assertTrue(called, "bundle に mermaid の呼び出しが見つからない")
        self.assertLessEqual(called, STAND_IN_METHODS, f"mermaid-local.js が受けない関数を呼ぶ: {called - STAND_IN_METHODS}")

    def test_material_bundle_calls_only_what_the_stand_in_takes(self):
        self.assert_bundle_contract(theme_bundle("material"))

    def test_zensical_bundle_calls_only_what_the_stand_in_takes(self):
        try:
            bundle = theme_bundle("zensical_ui")
        except ImportError:
            self.skipTest("zensical の組が入っていない（uv sync --group zensical）")
        self.assert_bundle_contract(bundle)


class PinsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(ROOT / "pyproject.toml", "rb") as f:
            cls.pyproject = tomllib.load(f)
        with open(ROOT / "uv.lock", "rb") as f:
            lock = tomllib.load(f)
        cls.locked = {p["name"]: p["version"] for p in lock["package"] if "version" in p}

    def test_python_is_312(self):
        self.assertEqual((ROOT / ".python-version").read_text(encoding="utf-8").strip(), "3.12")
        self.assertEqual(self.pyproject["project"]["requires-python"], "==3.12.*")
        self.assertEqual(sys.version_info[:2], (3, 12), "道具は uv run（Python 3.12）で動かす")

    def test_site_dependencies_are_pinned(self):
        deps = self.pyproject["project"]["dependencies"]
        self.assertIn("mkdocs==1.6.1", deps)
        material = [d for d in deps if d.startswith("mkdocs-material==")]
        self.assertEqual(len(material), 1)
        self.assertRegex(material[0], r"^mkdocs-material==9\.8\.\d+$")
        self.assertEqual(self.locked["mkdocs"], "1.6.1")
        self.assertEqual(self.locked["mkdocs-material"], material[0].split("==")[1])

    def test_zensical_is_pinned_exactly(self):
        group = self.pyproject["dependency-groups"]["zensical"]
        self.assertEqual(len(group), 1)
        self.assertRegex(group[0], r"^zensical==\d+\.\d+\.\d+$")
        self.assertEqual(self.locked["zensical"], group[0].split("==")[1])


class WorkflowsTest(unittest.TestCase):
    def test_deploy_waits_for_required_checks_on_main(self):
        ci = read_workflow("ci.yml")
        jobs = ci["jobs"]
        self.assertEqual(set(jobs["deploy"]["needs"]), {"site", "tools"})
        self.assertIn("refs/heads/main", jobs["deploy"]["if"])
        self.assertEqual(jobs["deploy"]["environment"]["name"], "github-pages")
        runs = [s.get("run", "") for s in jobs["site"]["steps"]]
        self.assertIn("uv sync --locked", runs)
        self.assertTrue(any("mkdocs build --strict" in r for r in runs))
        uses = [s.get("uses", "") for job in jobs.values() for s in job.get("steps", [])]
        for action in ("actions/upload-pages-artifact@", "actions/configure-pages@", "actions/deploy-pages@"):
            self.assertTrue(any(u.startswith(action) for u in uses), action)

    def test_zensical_never_blocks(self):
        z = read_workflow("zensical.yml")
        steps = z["jobs"]["build"]["steps"]
        build = [s for s in steps if "zensical build" in s.get("run", "")]
        self.assertEqual(len(build), 1)
        self.assertIs(build[0].get("continue-on-error"), True)
        self.assertIn("--strict", build[0]["run"])
        self.assertTrue(any("--group zensical" in s.get("run", "") for s in steps))

    def test_links_weekly_and_skip_ai_refusing_sites(self):
        links = read_workflow("links.yml")
        self.assertIn("schedule", links["on"])
        args = links["jobs"]["lychee"]["steps"][-1]["with"]["args"]
        patterns = re.findall(r"--exclude '([^']+)'", args)
        for url in ("https://atcoder.jp/contests/abc001", "https://img.atcoder.jp/a.png", "https://CODEFORCES.com/blog",
                    "https://m1.codeforces.com/"):
            self.assertTrue(any(re.search(p, url) for p in patterns), url)
        for url in ("https://code.claude.com/docs/ja/hooks", "https://notatcoder.jp/"):
            self.assertFalse(any(re.search(p, url) for p in patterns), url)
        self.assertIn("--verbose", args)  # 転送を出す

    def test_third_party_actions_are_pinned_by_sha(self):
        for path in glob.glob(str(ROOT / ".github/workflows/*.yml")):
            data = read_workflow(Path(path).name)
            for job in data["jobs"].values():
                for step in job.get("steps", []):
                    uses = step.get("uses")
                    if uses and not uses.startswith("actions/"):
                        self.assertRegex(uses, r"@[0-9a-f]{40}$", f"{Path(path).name}: {uses}")


class _ResourceParser(html.parser.HTMLParser):
    """ブラウザが読みに行く資源の URL（script・link の資源・img など）を集める。a の href は数えない。"""

    LOADING_RELS = {"stylesheet", "preload", "prefetch", "preconnect", "dns-prefetch", "icon", "apple-touch-icon",
                    "manifest", "modulepreload"}

    def __init__(self):
        super().__init__()
        self.urls: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "img", "iframe", "source", "audio", "video", "embed") and a.get("src"):
            self.urls.append(a["src"])
        if tag == "link" and a.get("href"):
            rels = set((a.get("rel") or "").lower().split())
            if rels & self.LOADING_RELS:
                self.urls.append(a["href"])


class BuiltSiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.site = Path(cls.tmp.name) / "site"
        env = dict(os.environ, NO_MKDOCS_2_WARNING="1")
        proc = subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(ROOT / "mkdocs.yml"), "-d", str(cls.site)],
            cwd=ROOT, env=env, capture_output=True, text=True, timeout=600,
        )
        cls.log = proc.stdout + proc.stderr
        cls.returncode = proc.returncode

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_build_is_strict_clean(self):
        self.assertEqual(self.returncode, 0, self.log)

    def html_files(self):
        files = sorted(self.site.rglob("*.html"))
        self.assertTrue(files)
        return files

    def test_every_page_has_head_and_foot_text(self):
        for path in self.html_files():
            text = path.read_text(encoding="utf-8")
            self.assertIn(HEAD_TEXT, text, path.name)
            plain = re.sub(r"<[^>]+>", "", text)
            self.assertIn("© 2026 yuukougun｜本文と図：CC BY 4.0｜コードと雛形：MIT｜Anthropic の公式の教材ではない", plain, path.name)
            self.assertNotIn('data-md-component="source"', text, path.name)

    def test_no_outside_resources_in_html(self):
        for path in self.html_files():
            parser = _ResourceParser()
            parser.feed(path.read_text(encoding="utf-8"))
            outside = [u for u in parser.urls if re.match(r"^(https?:)?//", u)]
            self.assertEqual(outside, [], f"{path.relative_to(self.site)} が外の資源を読む")

    def test_no_outside_resources_in_css(self):
        for path in sorted(self.site.rglob("*.css")):
            text = path.read_text(encoding="utf-8", errors="replace")
            self.assertIsNone(re.search(r"@import\s+(url\()?['\"]?(https?:)?//", text), path.name)
            self.assertIsNone(re.search(r"url\(\s*['\"]?(https?:)?//", text), path.name)

    def test_mermaid_copy_is_in_the_site(self):
        version = mermaid_local_version()
        self.assertTrue((self.site / "assets/js/mermaid-local.js").is_file())
        self.assertTrue((self.site / f"assets/vendor/mermaid-{version}/mermaid.min.js").is_file())


if __name__ == "__main__":
    unittest.main()
