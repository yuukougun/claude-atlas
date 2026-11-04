"""見た目の部品の試験（overrides/。planning/design.md §6.4・§8.5・§9.2・§9.3、DR-10・DR-11・DR-14。工程6a の2段目の担当 V）。

`uv run python -m unittest discover -s tests/site` で流す（B1 の test_site_config.py と同じ置き場所）。

- テンプレート：tests/site/fixtures/parts/ の試験用のページを一時のフォルダに写し、本物の overrides/ と mkdocs.yml の設定
  （site_url だけを替える）でビルドして、ページ上部（題の直後の下書きの帯・期限切れの注意書きの枠・バッジ）とページ下部
  （知識マップへのリンク・段階と更新日・誤りの報告）を確かめる。nav.yml は作る層（tools/gen/pages_out.py）の出力の形を
  まねたもの（extra.ca あり）と、extra のないもの（作る層が書く前でもビルドが止まらず、表示名のないバッジを出さない）の2つ
- Zensical の組（uv sync --group zensical）があれば、同じページを Zensical でもビルドし、部品が MkDocs と同じになるかを見る
- CSS と JS：外のサイトから読まない、端末に保存しない（進捗の部品を持ち込まない。D17）、テンプレートで Python の
  メソッドを呼ばない（Zensical の MiniJinja で読めるように）
- 色：レベルの段・下書きの帯・期限切れの注意書き・振り分けの辺の、背景と字の読みやすさ（WCAG のコントラスト比）
- 写し（assets/vendor/ の Cytoscape.js と dagre）：SOURCES.txt の sha256 と一致し、map.js が読む版がある
- JS の中身（Node.js があるとき。tests/site/js/parts_harness.cjs）：期限の比べ方、照合の規則、graph.json の読み方
ブラウザでの動き（注意書きが出るか・地図が描かれるか・絞り込み・幅 390px のライトとダーク）は test_site_parts_browser.py。

試験の置き場所 tests/site/fixtures/parts/（値はすべて試験用の作りもの）：
- docs/：front matter は design §3.3 の形。サイト用のデータ（docs/assets/data/pages.json・graph.json）と一覧（docs/lists/）は、
  作る層の出力（tools/gen/pages_out.py。2026-11-04 の形）をまねて手で書いた
- nav.yml：作る層の出力の形をまねた nav と extra.ca（表示の言葉・レベルの順・一覧・データの置き場所・ページごとの期限の日と
  機能のバッジ）。試験のために report_template も足した。nav-plain.yml：extra のない nav
- 期限の日：what-to-put-in-claude-md は過去（2000-01-31。注意書きが出る）、context-window と instructions-ignored は先
  （2999 年）、ほかは値なし。glossary は辺のないページ（知識マップの関連の囲みに出る）
"""

from __future__ import annotations

import hashlib
import html.parser
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "parts"
OVERRIDES = ROOT / "overrides"
JS_FILES = ["expiry.js", "filter.js", "map.js"]
SITE_URL = "https://example.invalid/claude-atlas/"
REPO = "https://github.com/yuukougun/claude-atlas"

# DR-10 の帯の文と、決定の最小の文（冒頭。B1 の試験と同じ）
DRAFT_BAND = "下書き・未検証"
HEAD_TEXT = "この辞典は Anthropic の公式の教材ではない。"


# ---------------------------------------------------------------- HTML を木にして読む


class Node:
    def __init__(self, tag: str, attrs: dict, parent: "Node | None"):
        self.tag = tag
        self.attrs = attrs
        self.parent = parent
        self.children: list = []

    def classes(self) -> list[str]:
        return (self.attrs.get("class") or "").split()

    def has_class(self, name: str) -> bool:
        return name in self.classes()

    def elements(self) -> list["Node"]:
        return [c for c in self.children if isinstance(c, Node)]

    def iter(self):
        for c in self.children:
            if isinstance(c, Node):
                yield c
                yield from c.iter()

    def find_all(self, tag: str | None = None, cls: str | None = None) -> list["Node"]:
        return [n for n in self.iter() if (tag is None or n.tag == tag) and (cls is None or n.has_class(cls))]

    def find(self, tag: str | None = None, cls: str | None = None) -> "Node | None":
        found = self.find_all(tag, cls)
        return found[0] if found else None

    def text(self) -> str:
        out = []
        for c in self.children:
            if isinstance(c, Node):
                if c.tag not in ("svg", "script", "style"):
                    out.append(c.text())
            else:
                out.append(c)
        return "".join(out)

    def plain(self) -> str:
        return " ".join(self.text().split())


class _Tree(html.parser.HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr", "path"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", {}, None)
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        node = Node(tag, {k: (v or "") for k, v in attrs}, self.cur)
        self.cur.children.append(node)
        if tag not in self.VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, {k: (v or "") for k, v in attrs}, self.cur))

    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag:
            n = n.parent
        if n is not None and n.parent is not None:
            self.cur = n.parent

    def handle_data(self, data):
        self.cur.children.append(data)


def parse(text: str) -> Node:
    tree = _Tree()
    tree.feed(text)
    tree.close()
    return tree.root


def article(path: Path) -> Node:
    node = parse(path.read_text(encoding="utf-8")).find("article")
    if node is None:
        raise AssertionError(f"{path} に article がない")
    return node


def badges(head: Node) -> dict[str, list[Node]]:
    """バッジの列：dt の言葉 → dd の中のバッジ（.ca-badge）。"""
    out = {}
    dl = head.find("dl", "ca-badges")
    for item in (dl.elements() if dl else []):
        dt = item.find("dt")
        dd = item.find("dd")
        if dt is not None and dd is not None:
            out[dt.plain()] = dd.find_all(cls="ca-badge")
    return out


def parts(path: Path, url: str) -> dict:
    """ページの部品を、MkDocs と Zensical で比べられる形にまとめる（属性の書き方・空白・相対の URL の書き方の違いを除く。
    Zensical はページ自身への相対の URL を ././ と書き、MkDocs は ./ と書く）。"""
    def r(href):
        return None if href is None else resolve(url, href)

    art = article(path)
    head = art.find("div", "ca-page-head")
    info = art.find("div", "ca-page-info")
    report = info.find("a", "ca-page-info__report") if info else None
    maplink = art.find("p", "ca-map-link")
    return {
        "h1": [h.plain() for h in art.find_all("h1")],
        "head": None if head is None else {
            "page": head.attrs.get("data-ca-page"),
            "pages_json": r(head.attrs.get("data-ca-pages-json")),
            "draft": [x.plain() for x in head.find_all("p", "ca-draft")],
            "draft_help": [r(a.attrs.get("href")) for a in head.find_all("a", "ca-draft__help")],
            "expiry_hidden": [("hidden" in p.attrs) for p in head.find_all("p", "ca-expiry")],
            "expiry_help": [r(a.attrs.get("href")) for a in head.find_all("a", "ca-expiry__help")],
            "badges": {k: [(b.tag, b.plain(), r(b.attrs.get("href")), sorted(b.classes())) for b in v]
                       for k, v in badges(head).items()},
        },
        "map": None if maplink is None else r(maplink.find("a").attrs.get("href")),
        "info": None if info is None else {
            "meta": [d.plain() for d in info.find_all("div") if d.parent and d.parent.has_class("ca-page-info__meta")],
            "stage_link": [r(a.attrs.get("href")) for a in info.find_all("a") if a.has_class("ca-stage")],
            "report": None if report is None else report.attrs.get("href"),
        },
    }


# ---------------------------------------------------------------- 試験用のサイトを作る


def make_project(tmp: Path, nav: str = "nav.yml", site_url: str = SITE_URL, extra_js: dict[str, str] | None = None,
                 site_dir: str | None = None) -> Path:
    """一時のフォルダに試験用のサイトを置く（docs/ は写し、overrides/ は本物へのリンク、mkdocs.yml は site_url だけを替える）。"""
    project = tmp / "project"
    shutil.copytree(FIXTURE / "docs", project / "docs")
    os.symlink(OVERRIDES, project / "overrides")
    shutil.copy(FIXTURE / nav, project / "nav.yml")
    config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    config = re.sub(r"(?m)^site_url: .*$", f"site_url: {site_url}", config)
    if site_dir:
        config += f"\nsite_dir: {site_dir}\n"
    for name, code in (extra_js or {}).items():
        (project / "docs/assets/js").mkdir(parents=True, exist_ok=True)
        (project / "docs/assets/js" / name).write_text(code, encoding="utf-8")
        config = config.rstrip("\n") + f"\n  - assets/js/{name}\n"
    (project / "mkdocs.yml").write_text(config, encoding="utf-8")
    return project


def build_mkdocs(project: Path, out: Path) -> tuple[int, str]:
    env = dict(os.environ, NO_MKDOCS_2_WARNING="1")
    proc = subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(project / "mkdocs.yml"),
                           "-d", str(out)], cwd=project, env=env, capture_output=True, text=True, timeout=600)
    return proc.returncode, proc.stdout + proc.stderr


def zensical_available() -> bool:
    return importlib.util.find_spec("zensical") is not None


# 試験用のページ：URL（サイトの根から）→ 期待
PAGES = {
    "symptoms/instructions-ignored/": {"title": "CLAUDE.md や指示が守られない", "stage": "draft", "map": True},
    "extend/what-to-put-in-claude-md/": {"title": "CLAUDE.md に何を書くか（推測できないことだけ）", "stage": "reviewed",
                                         "map": True},
    "basics/context-window/": {"title": "コンテキストウィンドウ", "stage": "done", "map": True},
    "enforce/when-to-lock/": {"title": "縛るときの判断 & 鍵の選び方", "stage": "draft", "map": True},
    "start/how-to-use/": {"title": "この辞典の引き方", "stage": "draft", "map": False},
    "start/knowledge-map/": {"title": "知識マップ", "stage": "draft", "map": False},
    "start/reverse-index/": {"title": "逆引き辞典", "stage": "draft", "map": False},
    "start/glossary/": {"title": "用語集", "stage": "draft", "map": False},
}
PLAIN_PAGES = ["", "lists/by-level/", "lists/by-surface/"]   # front matter に id のないページ


def html_of(site: Path, url: str) -> Path:
    return site / url / "index.html"


def query_of(href: str) -> dict[str, str]:
    q = urllib.parse.urlsplit(href).query
    return {k: v[0] for k, v in urllib.parse.parse_qs(q, keep_blank_values=True).items()}


def resolve(page_url: str, href: str) -> str:
    """ページの URL（サイトの根から）と相対のリンクから、サイトの根からのパス（#・? を含む）。"""
    return urllib.parse.urljoin(SITE_URL + page_url, href)[len(SITE_URL):]


# ---------------------------------------------------------------- 作る層の extra.ca があるとき（MkDocs）


class TemplateFullTest(unittest.TestCase):
    """作る層が nav.yml の extra.ca を書いた形（表示名・レベルの順・一覧・データの置き場所）でのテンプレート。"""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.project = make_project(Path(cls.tmp.name))
        cls.site = Path(cls.tmp.name) / "site"
        cls.returncode, cls.log = build_mkdocs(cls.project, cls.site)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def setUp(self):
        self.assertEqual(self.returncode, 0, self.log)

    def head(self, url: str) -> Node:
        head = article(html_of(self.site, url)).find("div", "ca-page-head")
        self.assertIsNotNone(head, url)
        return head

    def test_build_is_strict_clean(self):
        self.assertEqual(self.returncode, 0, self.log)

    def test_head_comes_right_after_the_title(self):
        for url, want in PAGES.items():
            art = article(html_of(self.site, url))
            elems = art.elements()
            h1 = [i for i, e in enumerate(elems) if e.tag == "h1"]
            self.assertEqual(len(h1), 1, url)
            # 見出しは front matter の title（nav の短い名前ではない。& もそのまま）
            self.assertEqual(elems[h1[0]].plain(), want["title"], url)
            nxt = elems[h1[0] + 1]
            self.assertTrue(nxt.has_class("ca-page-head"), f"{url}: h1 の次が {nxt.tag}.{nxt.classes()}")
            self.assertEqual(nxt.attrs.get("data-ca-page"), url.strip("/").split("/")[-1])
            # 冒頭の要点は、ページ上部の後
            self.assertTrue(elems[h1[0] + 2].has_class("abstract"), url)

    def test_pages_without_id_have_no_head_but_the_report_link(self):
        for url in PLAIN_PAGES:
            art = article(html_of(self.site, url))
            self.assertIsNone(art.find("div", "ca-page-head"), url)
            self.assertIsNone(art.find("p", "ca-map-link"), url)
            info = art.find("div", "ca-page-info")
            if url == "":
                # サイトのトップは決定にある最小の文だけにする（brief-build §3）ので、報告のリンクも出さない
                self.assertIsNone(info)
                continue
            self.assertIsNotNone(info, url)
            self.assertIsNone(info.find("dl"), url)   # 段階と更新日は id を持つページだけ
            self.assertIsNotNone(info.find("a", "ca-page-info__report"), url)

    def test_draft_band_only_on_draft_pages(self):
        for url, want in PAGES.items():
            head = self.head(url)
            bands = head.find_all("p", "ca-draft")
            if want["stage"] == "draft":
                self.assertEqual(len(bands), 1, url)
                self.assertEqual(bands[0].find("span", "ca-draft__label").plain(), DRAFT_BAND)
                self.assertEqual(bands[0].attrs.get("role"), "note")
                help_link = bands[0].find("a", "ca-draft__help")
                self.assertEqual(resolve(url, help_link.attrs["href"]), "start/how-to-use/#stage")
                self.assertEqual(help_link.plain(), "段階・下書きの帯・「準備中」の題名")   # how-to-use の sections の題
            else:
                self.assertEqual(bands, [], url)
            self.assertNotIn(DRAFT_BAND, " ".join(n.plain() for n in head.find_all("dd")), url)

    def test_expiry_notice_is_a_hidden_frame_filled_by_js(self):
        for url in PAGES:
            head = self.head(url)
            notes = head.find_all("p", "ca-expiry")
            self.assertEqual(len(notes), 1, url)
            self.assertIn("hidden", notes[0].attrs, url)
            self.assertIn("data-ca-expiry", notes[0].attrs, url)
            self.assertIsNotNone(notes[0].find("time"), url)
            self.assertIn("data-ca-expiry-date", notes[0].find("time").attrs)
            self.assertEqual(resolve(url, notes[0].find("a", "ca-expiry__help").attrs["href"]), "start/how-to-use/#freshness")
            # pages.json の置き場所（nav.yml の extra.ca.pages_json）を、このページからの相対で渡す
            self.assertEqual(resolve(url, head.attrs["data-ca-pages-json"]), "assets/data/pages.json")
            # 期限の日（extra.ca.expires。作る層が数えた値）を data 属性に出す。値のないページは空
            want = {"basics/context-window/": "2999-12-31", "extend/what-to-put-in-claude-md/": "2000-01-31",
                    "symptoms/instructions-ignored/": "2999-01-01"}.get(url, "")
            self.assertEqual(head.attrs.get("data-ca-expires"), want, url)

    def test_badges_of_a_draft_symptom_page(self):
        b = badges(self.head("symptoms/instructions-ignored/"))
        # 機能のバッジは extra.ca.badges のこのページの値（作る層が選ぶ）だけを出す。この試験では成熟度だけ
        self.assertEqual(list(b), ["レベル", "型", "面", "原理", "成熟度", "変わりやすさ", "確認日"])
        level = b["レベル"][0]
        self.assertEqual((level.tag, level.plain()), ("a", "整える"))
        self.assertIn("ca-lv-2", level.classes())   # levels の2番目
        self.assertEqual(resolve("symptoms/instructions-ignored/", level.attrs["href"]), "lists/by-level/#整える")
        self.assertEqual([x.plain() for x in b["型"]], ["症状"])
        self.assertEqual([x.plain() for x in b["面"]], ["Claude Code", "アプリ"])   # front matter の順
        self.assertEqual([resolve("symptoms/instructions-ignored/", x.attrs["href"]) for x in b["面"]],
                         ["lists/by-surface/#claude-code", "lists/by-surface/#app"])
        self.assertEqual([x.plain() for x in b["原理"]], ["縛る", "見せる"])
        self.assertEqual([x.plain() for x in b["変わりやすさ"]], ["中"])
        self.assertEqual([(x.plain(), x.has_class("ca-badge--unverified")) for x in b["確認日"]], [("未検証", True)])

    def test_badges_of_a_reviewed_feature_page(self):
        b = badges(self.head("extend/what-to-put-in-claude-md/"))
        self.assertEqual(list(b), ["レベル", "型", "面", "原理", "成熟度", "強制力", "変わりやすさ", "確認日", "段階"])
        self.assertEqual([x.plain() for x in b["型"]], ["機能"])
        self.assertEqual([x.plain() for x in b["成熟度"]], ["GA"])     # extra.ca.badges のこのページの値
        self.assertEqual([x.plain() for x in b["強制力"]], ["お願い"])
        verified = b["確認日"][0]
        self.assertEqual(verified.plain(), "2026-11-03・Claude Code 2.1.317（stable）")
        self.assertEqual(verified.find("time").attrs.get("datetime"), "2026-11-03")
        self.assertEqual(verified.attrs.get("title"), "モデル：claude-opus-5-5、claude-sonnet-5-5。点検：2026-11-04")
        self.assertEqual([x.plain() for x in b["段階"]], ["検証済み"])

    def test_badges_of_a_done_concept_page_and_a_guide(self):
        b = badges(self.head("basics/context-window/"))
        self.assertIn("ca-lv-1", b["レベル"][0].classes())
        self.assertEqual([x.plain() for x in b["面"]], ["アプリ", "Claude Code", "API"])
        self.assertEqual(b["確認日"][0].plain(), "2026-11-04・Claude Code 2.1.317（latest）")
        self.assertEqual([x.plain() for x in b["段階"]], ["完成"])
        b = badges(self.head("enforce/when-to-lock/"))
        self.assertIn("ca-lv-4", b["レベル"][0].classes())
        # guide はレベルを持たない（design §3.1 の2）
        b = badges(self.head("start/how-to-use/"))
        self.assertEqual(list(b), ["型", "変わりやすさ", "確認日"])
        self.assertEqual([x.plain() for x in b["型"]], ["案内"])

    def test_map_link_only_where_the_page_has_edges(self):
        for url, want in PAGES.items():
            link = article(html_of(self.site, url)).find("p", "ca-map-link")
            if want["map"]:
                self.assertIsNotNone(link, url)
                pid = url.strip("/").split("/")[-1]
                self.assertEqual(resolve(url, link.find("a").attrs["href"]), f"start/knowledge-map/?focus={pid}")
            else:
                self.assertIsNone(link, url)

    def test_bottom_line_and_report_link(self):
        cases = {
            "symptoms/instructions-ignored/": ("下書き", "2026-11-04", "未検証"),
            "extend/what-to-put-in-claude-md/": ("検証済み", "2026-11-03", "2026-11-03"),
            "basics/context-window/": ("完成", "2026-11-04", "2026-11-04"),
        }
        for url, (stage, updated, verified) in cases.items():
            art = article(html_of(self.site, url))
            info = art.find("div", "ca-page-info")
            meta = {d.find("dt").plain(): d.find("dd").plain() for d in info.find("dl").elements()}
            self.assertEqual(meta, {"段階": stage, "更新日": updated}, url)
            stage_link = info.find("dl").find("a")
            self.assertEqual(resolve(url, stage_link.attrs["href"]), "start/how-to-use/#stage")
            report = info.find("a", "ca-page-info__report")
            href = report.attrs["href"]
            self.assertTrue(href.startswith(REPO + "/issues/new?"), href)
            title = PAGES[url]["title"]
            self.assertEqual(query_of(href), {
                "title": "誤りの報告：" + title, "template": "page-error.yml", "page-title": title,
                "page-url": SITE_URL + url, "page-verified": verified, "page-updated": updated,
            })
            self.assertEqual(report.attrs.get("target"), "_blank")
            self.assertIn("noopener", report.attrs.get("rel", ""))
            self.assertEqual(report.plain(), "このページの誤りを報告する")
            # 最後の行は、作る層のページ下部（前提・次に読む・関連）より後
            elems = art.elements()
            if url == "symptoms/instructions-ignored/":
                links = [i for i, e in enumerate(elems) if e.has_class("ca-page-links")]
                self.assertEqual(len(links), 1)
                self.assertLess(links[0], elems.index(info))

    def test_css_and_js_are_loaded_on_every_page(self):
        for url in list(PAGES) + PLAIN_PAGES:
            text = html_of(self.site, url).read_text(encoding="utf-8")
            root = parse(text)
            css = [resolve(url, n.attrs["href"]) for n in root.find_all("link") if "stylesheet" in n.attrs.get("rel", "")]
            self.assertIn("assets/css/ca.css", css, url)
            scripts = [resolve(url, n.attrs["src"]) for n in root.find_all("script") if n.attrs.get("src")]
            ours = [s for s in scripts if s.startswith("assets/js/")]
            # mermaid-local.js（extra_javascript）の後に、期限・絞り込み（照合の規則）・地図の順
            self.assertEqual(ours, ["assets/js/mermaid-local.js", "assets/js/expiry.js", "assets/js/filter.js",
                                    "assets/js/map.js"], url)
            self.assertIn(HEAD_TEXT, text, url)
        for rel in ["assets/css/ca.css"] + [f"assets/js/{n}" for n in JS_FILES] + [
                "assets/vendor/cytoscape-3.34.4/cytoscape.min.js", "assets/vendor/cytoscape-dagre-4.0.1/cytoscape-dagre.min.js"]:
            self.assertTrue((self.site / rel).is_file(), rel)

    def test_page_links_block_and_graph_mount_from_the_generator(self):
        # 作る層の出力（div.ca-page-links・div.ca-graph）を md_in_html がそのまま通す
        art = article(html_of(self.site, "symptoms/instructions-ignored/"))
        block = art.find("div", "ca-page-links")
        self.assertEqual([p.plain() for p in block.elements() if p.tag == "p"], ["前提", "次に読む", "関連"])
        self.assertEqual([u.tag for u in block.elements()], ["p", "ul", "p", "ul", "p", "ul"])
        graph = article(html_of(self.site, "start/knowledge-map/")).find("div", "ca-graph")
        self.assertEqual(resolve("start/knowledge-map/", graph.attrs["data-graph"]), "assets/data/graph.json")


# ---------------------------------------------------------------- extra のない nav（作る層が書く前）


class TemplatePlainTest(unittest.TestCase):
    """nav.yml に extra.ca がないとき：ビルドは止まらず、表示名のないバッジ（型・面・段階）と一覧へのリンクを出さない。"""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.project = make_project(Path(cls.tmp.name), nav="nav-plain.yml")
        cls.site = Path(cls.tmp.name) / "site"
        cls.returncode, cls.log = build_mkdocs(cls.project, cls.site)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_build_is_strict_clean(self):
        self.assertEqual(self.returncode, 0, self.log)

    def test_badges_without_labels(self):
        head = article(html_of(self.site, "symptoms/instructions-ignored/")).find("div", "ca-page-head")
        b = badges(head)
        self.assertEqual(list(b), ["レベル", "原理", "変わりやすさ", "確認日"])
        level = b["レベル"][0]
        self.assertEqual(level.tag, "span")              # 一覧の置き場所がないのでリンクにしない
        self.assertIn("ca-lv-0", level.classes())       # レベルの順がないので色の段を付けない
        self.assertEqual(len(head.find_all("p", "ca-draft")), 1)   # 帯は表示名に頼らない
        self.assertNotIn("data-ca-expires", head.attrs)             # 期限の日がなければ、expiry.js が pages.json から引く
        # 段階の表示名がないので、reviewed のページにも段階のバッジを出さない
        self.assertNotIn("段階", badges(article(html_of(self.site, "extend/what-to-put-in-claude-md/")).find("div", "ca-page-head")))

    def test_title_and_bottom_without_labels(self):
        art = article(html_of(self.site, "extend/what-to-put-in-claude-md/"))
        # nav の短い名前（CLAUDE.md の書き方）ではなく、front matter の title
        self.assertEqual([h.plain() for h in art.find_all("h1")], ["CLAUDE.md に何を書くか（推測できないことだけ）"])
        info = art.find("div", "ca-page-info")
        meta = {d.find("dt").plain(): d.find("dd").plain() for d in info.find("dl").elements()}
        self.assertEqual(meta, {"更新日": "2026-11-03"})
        href = info.find("a", "ca-page-info__report").attrs["href"]
        q = query_of(href)
        self.assertNotIn("template", q)                  # テンプレートの名前がなければ、本文に書く
        self.assertEqual(q["title"], "誤りの報告：CLAUDE.md に何を書くか（推測できないことだけ）")
        self.assertEqual(q["body"].split("\n")[:4], [
            "ページ：CLAUDE.md に何を書くか（推測できないことだけ）",
            "URL：" + SITE_URL + "extend/what-to-put-in-claude-md/", "確認日：2026-11-03", "更新日：2026-11-03"])


# ---------------------------------------------------------------- Zensical（試験ビルド。組があるときだけ）


@unittest.skipUnless(zensical_available(), "zensical の組が入っていない（uv sync --group zensical）")
class ZensicalTest(unittest.TestCase):
    """Zensical（MiniJinja）でも同じ部品が出る（design §8.1 の評価の基準「overrides が動く」）。"""

    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        tmp = Path(cls.tmp.name)
        cls.project = make_project(tmp, site_dir="zsite")
        proc = subprocess.run([sys.executable, "-m", "zensical", "build", "--strict", "--clean", "-f",
                               str(cls.project / "mkdocs.yml")], cwd=cls.project, capture_output=True, text=True,
                              timeout=600)
        cls.z_code, cls.z_log = proc.returncode, proc.stdout + proc.stderr
        cls.zsite = cls.project / "zsite"
        cls.m_site = tmp / "msite"
        cls.m_code, cls.m_log = build_mkdocs(cls.project, cls.m_site)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_build_is_strict_clean(self):
        self.assertEqual(self.z_code, 0, self.z_log)
        self.assertNotIn("issue", self.z_log.replace("No issues found", "").lower(), self.z_log)

    def test_parts_are_the_same_as_mkdocs(self):
        self.assertEqual(self.m_code, 0, self.m_log)
        for url in list(PAGES) + PLAIN_PAGES:
            self.assertEqual(parts(html_of(self.zsite, url), url), parts(html_of(self.m_site, url), url), url)


# ---------------------------------------------------------------- CSS と JS の中身（読むだけ）


def overrides_texts() -> dict[str, str]:
    """overrides/ の、写し（assets/vendor/）のほかのファイル。"""
    out = {}
    for path in sorted(OVERRIDES.rglob("*")):
        if path.is_file() and "vendor" not in path.relative_to(OVERRIDES).parts:
            out[str(path.relative_to(OVERRIDES))] = path.read_text(encoding="utf-8")
    return out


class StaticTest(unittest.TestCase):
    def test_no_outside_urls_in_css_and_js(self):
        for name in ["assets/css/ca.css"] + [f"assets/js/{n}" for n in JS_FILES]:
            text = (OVERRIDES / name).read_text(encoding="utf-8")
            self.assertIsNone(re.search(r"https?://|url\(\s*['\"]?//", text), f"{name} に外の URL がある")

    def test_no_storage_or_progress_parts(self):
        # 読者の情報を端末に残さない・集めない（decisions 2026-11-03「アクセスの解析」）。進捗の部品は持ち込まない（D17）
        banned = ["localStorage", "sessionStorage", "document.cookie", "indexedDB", "sendBeacon", "理解した", "解いた",
                  "勉強したい", "kp-", "KPProgress", "KPMatch"]
        for name, text in overrides_texts().items():
            for word in banned:
                self.assertNotIn(word, text, f"{name} に {word}")

    def test_template_calls_no_python_methods(self):
        # Zensical（MiniJinja）でも読めるよう、テンプレートの式で Python のメソッドを呼ばない（.items() など）
        text = (OVERRIDES / "main.html").read_text(encoding="utf-8")
        for expr in re.findall(r"{[{%](.*?)[}%]}", text, re.S):
            self.assertIsNone(re.search(r"\.\s*[A-Za-z_]\w*\s*\(", expr), f"メソッドの呼び出し：{expr.strip()[:80]}")

    def test_template_keeps_the_minimal_head_text_and_loads_parts(self):
        text = (OVERRIDES / "main.html").read_text(encoding="utf-8")
        m = re.search(r"{% block announce %}(.*?){% endblock %}", text, re.S)
        self.assertEqual(m.group(1).strip(), HEAD_TEXT)
        self.assertIn("'assets/css/ca.css' | url", text)
        for name in JS_FILES:
            self.assertIn(f"'assets/js/{name}' | url", text)
        self.assertIn(DRAFT_BAND, text)

    def test_vendor_copies_match_sources(self):
        sources = (OVERRIDES / "assets/vendor/SOURCES.txt").read_text(encoding="utf-8")
        map_js = (OVERRIDES / "assets/js/map.js").read_text(encoding="utf-8")
        libs = re.search(r"var LIBS = \[([^\]]+)\]", map_js).group(1)
        rels = re.findall(r'"(vendor/[^"]+)"', libs)
        self.assertEqual(len(rels), 2)
        for rel in rels:
            path = OVERRIDES / "assets" / rel
            self.assertTrue(path.is_file(), rel)
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertIn(digest, sources, f"SOURCES.txt の sha256 と {rel} が一致しない")
            self.assertTrue((path.parent / "LICENSE").is_file(), rel)
            self.assertIn(path.parent.name + "/", sources)
        self.assertTrue((OVERRIDES / "assets/vendor/cytoscape-dagre-4.0.1/LICENSE.dagre").is_file())
        self.assertTrue((OVERRIDES / "assets/vendor/cytoscape-dagre-4.0.1/LICENSE.graphlib").is_file())
        # 古い版の写しを残さない
        for prefix in ("cytoscape-3.", "cytoscape-dagre-"):
            dirs = [p.name for p in (OVERRIDES / "assets/vendor").glob(prefix + "*")]
            self.assertEqual(len(dirs), 1, dirs)


# ---------------------------------------------------------------- 色（WCAG のコントラスト比）


def _lum(rgb: tuple[float, float, float]) -> float:
    def ch(c: float) -> float:
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _rgb(value: str, bg: tuple[float, float, float] | None = None) -> tuple[float, float, float]:
    value = value.strip()
    m = re.fullmatch(r"#([0-9a-fA-F]{6})", value)
    if m:
        h = m.group(1)
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    m = re.fullmatch(r"rgba\((\d+),\s*(\d+),\s*(\d+),\s*([\d.]+)\)", value)
    if m and bg is not None:
        a = float(m.group(4))
        return tuple(int(m.group(i + 1)) * a + bg[i] * (1 - a) for i in range(3))
    raise AssertionError(f"色を読めない：{value}")


def contrast(a, b) -> float:
    la, lb = sorted([_lum(a), _lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def css_vars(css: str, selector: str) -> dict[str, str]:
    m = re.search(re.escape(selector) + r"\s*{([^}]*)}", css)
    if not m:
        raise AssertionError(f"{selector} の規則がない")
    return {k: v.strip() for k, v in re.findall(r"(--ca-[\w-]+)\s*:\s*([^;]+);", m.group(1))}


LIGHT_BG = (255, 255, 255)        # Material の --md-default-bg-color（default）
DARK_BG = (30, 33, 41)            # slate：hsl(225 15% 14%)


class PaletteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        css = (OVERRIDES / "assets/css/ca.css").read_text(encoding="utf-8")
        cls.light = css_vars(css, ":root")
        cls.dark = css_vars(css, '[data-md-color-scheme="slate"]')

    def check_levels(self, v: dict[str, str], bg, darker_up: bool):
        fills = [_rgb(v[f"--ca-lv-{i}"]) for i in range(1, 6)]
        lums = [_lum(c) for c in fills]
        # 1つの色相の明るさの段：ライトは上の段ほど暗く、ダークは上の段ほど明るい（低い段ほど背景に近い）
        self.assertEqual(lums, sorted(lums, reverse=darker_up), lums)
        # 背景に近い端の段も、背景から 2:1 以上
        self.assertGreaterEqual(min(contrast(c, bg) for c in fills), 2.0)
        # 段の中の字（バッジの文字）は 4.4:1 以上（いちばん低いのは #2a78d6 の白・黒の 4.42〜4.46）
        for i, c in enumerate(fills, 1):
            self.assertGreaterEqual(contrast(_rgb(v[f"--ca-lv-{i}-fg"]), c), 4.4, f"--ca-lv-{i}")

    def test_level_ramp_light(self):
        self.check_levels(self.light, LIGHT_BG, darker_up=True)

    def test_level_ramp_dark(self):
        self.check_levels(self.dark, DARK_BG, darker_up=False)

    def test_band_and_notice_text(self):
        for v, bg in ((self.light, LIGHT_BG), (self.dark, DARK_BG)):
            for name in ("draft", "expiry"):
                fill = _rgb(v[f"--ca-{name}-bg"], bg)
                self.assertGreaterEqual(contrast(_rgb(v[f"--ca-{name}-color"]), fill), 4.5, name)
            self.assertGreaterEqual(contrast(_rgb(v["--ca-route-color"]), bg), 3.0)


# ---------------------------------------------------------------- JS の中身（Node.js があるとき）


@unittest.skipUnless(shutil.which("node"), "Node.js がない")
class ScriptLogicTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        proc = subprocess.run(["node", str(HERE / "js/parts_harness.cjs"), str(OVERRIDES),
                               str(FIXTURE / "docs/assets/data/graph.json")], capture_output=True, text=True, timeout=120)
        if proc.returncode != 0:
            raise AssertionError("parts_harness.cjs が止まった:\n" + proc.stderr)
        cls.out = json.loads(proc.stdout)

    def test_expiry_compares_dates_strictly_before_today(self):
        self.assertEqual(self.out["expired"], [True, False, False, True, False, False, False, False])
        self.assertRegex(self.out["today"], r"^\d{4}-\d{2}-\d{2}$")

    def test_match_rules(self):
        n = self.out["norm"]
        self.assertEqual(n[0:3], ["planmode"] * 3)            # 大文字・小文字・全角・空白とハイフン
        self.assertEqual(n[3], n[4])                          # カタカナとひらがな
        self.assertEqual(n[5:7], ["claude.md"] * 2)
        self.assertEqual(n[7], "ふっくhooks")                  # ・を除く
        s = self.out["synonym"]
        self.assertEqual(s["terms"][0][:2], [n[3], "planmode"])
        self.assertTrue(s["hit"])
        self.assertFalse(s["miss"])
        self.assertTrue(s["plain"])
        self.assertEqual(s["count"], 2)                       # 同じ組を二度足しても重ならない
        self.assertIn(["削除", "取り除いた", "削除"], s["okurigana"])   # 送り仮名ごと置き換える
        self.assertEqual(s["words"], ["hooks", "permissions"])

    def test_graph_from_the_generator(self):
        g = self.out["graph"]
        self.assertEqual(g["pages"], ["glossary", "context-window", "what-to-put-in-claude-md", "when-to-lock",
                                      "instructions-ignored"])
        self.assertIn(["instructions-ignored", "when-to-lock", "route"], g["edges"])
        self.assertIn(["context-window", "instructions-ignored", "prerequisite"], g["edges"])
        self.assertEqual(len(g["edges"]), 5)
        self.assertEqual(g["parents"]["when-to-lock"], ["what-to-put-in-claude-md", "instructions-ignored"])
        self.assertEqual(g["related"]["instructions-ignored"], ["when-to-lock", "context-window"])
        self.assertEqual(g["related"]["when-to-lock"], ["glossary"])
        self.assertEqual(g["rank"]["仕組みにする"], 4)
        self.assertEqual([f[0] for f in g["fields"]], ["start", "basics", "extend", "enforce", "symptoms"])

    def test_graph_from_page_fields(self):
        g = self.out["graphPages"]
        self.assertEqual(g["pages"], ["a", "b", "s"])         # id のないページと、同じ id の2つ目は捨てる
        self.assertEqual(g["edges"], [["a", "b", "prerequisite"], ["s", "b", "route"], ["s", "a", "route"]])
        self.assertEqual(g["related"]["s"], ["a", "b"])       # ないページ・自分・重なり・#anchor をまとめる
        self.assertEqual(g["rank"]["六つ目"], 5)                # 色の段は5まで
        self.assertEqual(g["fields"], [["x", "x"], ["y", "y"]])
        self.assertEqual(self.out["graphEmpty"]["pages"], [])


if __name__ == "__main__":
    unittest.main()
