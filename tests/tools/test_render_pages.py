"""tools/render_pages.py（描画の検査。kyopro-atlas から写して直したもの）の試験。
`uv run python -m unittest discover -s tests/tools` で動く。

- いつも動く：Chrome を使わない部品（ページの一覧・絞り込み・変えたページの選び方・指摘のまとめ方・外への問い合わせの
  拾い方・WebSocket のフレーム・Chrome の探し方）
- 環境変数 CA_CHROME に Chrome（headless shell でもよい）の実行ファイルを指定したときだけ動く：本物の overrides/ と
  mkdocs.yml の設定で試験用のページを一時フォルダにビルドし、render_pages.py で描いて、崩れ（外の画像・横ずれ・地の文に
  残った記法・広い表）を捕まえ、Mermaid の図が写しで描かれることを確かめる（tests/site/test_site_browser.py と同じ名前の
  変数。2026-11-04 に Chrome for Testing 146 の chrome-headless-shell で通した）

    CA_CHROME=/path/to/chrome-headless-shell uv run python -m unittest tests/tools/test_render_pages.py
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

import render_pages as rp  # noqa: E402

CHROME = os.environ.get("CA_CHROME", "")

PAGES = {
    "index.md": "# 試験のトップ\n\n[ページ](a/clean.md)\n",
    "a/clean.md": "# 崩れのないページ\n\n本文。\n\n| 列 | 列 |\n| --- | --- |\n| a | b |\n",
    "a/outside.md": "# 外の画像\n\n![外の図](https://example.com/a.png)\n",
    "a/leak.md": "# 残った記法\n\nこれは **太字の失敗。\n\n![区間 [1, 5)](a.svg)\n",
    "a/overflow.md": '# 横ずれ\n\n<div style="width: 1200px">はみ出す箱</div>\n',
    "a/wide.md": "# 広い表\n\n| " + " | ".join(f"とても長い見出しの列{i}" for i in range(12)) + " |\n| "
                 + " | ".join("---" for _ in range(12)) + " |\n| " + " | ".join("あいうえおかきくけこ" for _ in range(12)) + " |\n",
    "a/diagram.md": "# 図\n\n```mermaid\ngraph LR\n  A[見せる] --> B[確かめる]\n```\n",
}


class TestParts(unittest.TestCase):
    def test_pages_and_selection(self):
        with tempfile.TemporaryDirectory() as tmp:
            site, docs = Path(tmp) / "site", Path(tmp) / "docs"
            for rel in ("index.html", "start/how-to-use/index.html", "start/index.html", "assets/x/index.html",
                        "search/index.html", "404.html"):
                (site / rel).parent.mkdir(parents=True, exist_ok=True)
                (site / rel).write_text("x", encoding="utf-8")
            (site / "sitemap.xml").write_text('<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                                              "<url><loc>https://yuukougun.github.io/claude-atlas/</loc></url>"
                                              "<url><loc>https://yuukougun.github.io/claude-atlas/start/</loc></url></urlset>",
                                              encoding="utf-8")
            (docs / "start").mkdir(parents=True)
            (docs / "start/how-to-use.md").write_text("x", encoding="utf-8")
            (docs / "index.md").write_text("x", encoding="utf-8")
            self.assertEqual(rp.site_prefix(site), "/claude-atlas/")
            pages = rp.list_pages(site, docs)
            self.assertEqual([p.path for p in pages], ["", "start/", "start/how-to-use/", "404.html"])
            self.assertEqual(pages[2].source, "docs/start/how-to-use.md")
            self.assertEqual([p.path for p in rp.select_pages(pages, ["how-to-use"], [])], ["start/how-to-use/"])
            self.assertEqual([p.path for p in rp.select_pages(pages, [], ["start"])], ["start/", "start/how-to-use/"])
            with self.assertRaises(SystemExit):
                rp.select_pages(pages, ["nope"], [])

    def test_changed_pages(self):
        pages = [rp.SitePage("", "docs/index.md"), rp.SitePage("symptoms/instructions-ignored/", "docs/symptoms/instructions-ignored.md"),
                 rp.SitePage("enforce/hooks-basics/", "docs/enforce/hooks-basics.md"), rp.SitePage("404.html")]
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            (docs / "enforce").mkdir()
            (docs / "enforce/hooks-basics.md").write_text("<!-- gen:begin snippet hooks-basics/deny -->", encoding="utf-8")
            paths, shared = rp.changed_pages(["docs/symptoms/instructions-ignored.md", "tools/x.py", "data/facts.yml",
                                              "docs/llms.txt", "stubs/a/b.md"], pages, docs)
            self.assertEqual((paths, shared), (["symptoms/instructions-ignored/"], []))
            paths, _ = rp.changed_pages(["snippets/hooks-basics/deny.json", "overrides/404.html"], pages, docs)
            self.assertEqual(paths, ["enforce/hooks-basics/", "404.html"])
            paths, shared = rp.changed_pages(["overrides/main.html", "docs/assets/data/pages.json"], pages, docs)
            self.assertEqual((len(paths), shared), (4, ["overrides/main.html", "docs/assets/data/pages.json"]))
            paths, _ = rp.changed_pages(["docs/img/hooks-basics/flow.svg"], pages, docs)
            self.assertEqual(paths, ["enforce/hooks-basics/"])

    def test_outside_requests_and_console(self):
        base = "http://127.0.0.1:8000/claude-atlas/"
        events = [
            {"method": "Network.requestWillBeSent", "params": {"request": {"url": base + "assets/x.js"}}},
            {"method": "Network.requestWillBeSent", "params": {"request": {"url": "https://unpkg.com/mermaid@11"}}},
            {"method": "Network.requestWillBeSent", "params": {"request": {"url": "https://unpkg.com/mermaid@11"}}},
            {"method": "Network.requestWillBeSent", "params": {"request": {"url": "data:image/png;base64,AAAA"}}},
            {"method": "Log.entryAdded", "params": {"entry": {"level": "error", "text": "外の失敗", "url": "https://unpkg.com/x"}}},
            {"method": "Log.entryAdded", "params": {"entry": {"level": "error", "text": "読めない", "url": base + "a.js"}}},
            {"method": "Runtime.exceptionThrown", "params": {"exceptionDetails": {"text": "x", "exception": {"description": "TypeError: y"}}}},
        ]
        self.assertEqual(rp.outside_requests(events, base), ["https://unpkg.com/mermaid@11"])
        self.assertEqual(rp.console_errors(events, base), ["読めない（/a.js）", "例外: TypeError: y"])

    def test_collect_merges_variants(self):
        page = rp.SitePage("a/", "docs/a.md")
        light, dark = rp.Variant(390, "light"), rp.Variant(390, "dark")
        res = {"items": {"wide-table": [{"h": "x", "where": "", "head": "h", "width": 500, "box": 300, "hidden": 200, "cols": 3}]},
               "outside": ["https://example.com/a.png"], "console": [], "scheme": "default"}
        dark_res = dict(res, scheme="slate")
        findings, notes = rp.collect([page], {"a/": [(light, res), (dark, dark_res)]})
        self.assertEqual(notes, [])
        self.assertEqual([(f.kind, f.variants) for f in findings],
                         [("outside-request", ["390 ライト", "390 ダーク"]), ("wide-table", ["390 ライト", "390 ダーク"])])
        self.assertEqual(rp.summarize(findings)["outside-request"]["findings"], 1)
        failed, _ = rp.collect([page], {"a/": [(light, {"failed": "開けない"})]})
        self.assertEqual([f.kind for f in failed], ["load-failed"])

    def test_websocket_frame(self):
        frame = rp.encode_frame(0x1, b"hello", mask=b"\x01\x02\x03\x04")
        self.assertEqual(frame[0], 0x81)
        self.assertEqual(frame[1], 0x80 | 5)
        self.assertEqual(rp._xor(frame[6:], b"\x01\x02\x03\x04"), b"hello")
        self.assertEqual(len(rp.encode_frame(0x1, b"x" * 70000)), 2 + 8 + 4 + 70000)

    def test_leak_pattern(self):
        rx = re.compile(rp.LEAK_RE)
        for s in ("図は ![図](a b.png)", "**太字の失敗", "段落 {#anchor}", '!!! note "x"', '=== "アプリ"', "<!-- x"):
            self.assertTrue(rx.search(s), s)
        for s in ("ふつうの文。", "a = b", "2 * 3"):
            self.assertFalse(rx.search(s), s)

    def test_find_chrome_from_environment(self):
        with tempfile.TemporaryDirectory() as tmp:
            exe = Path(tmp) / "chrome"
            exe.write_text("#!/bin/sh\n", encoding="utf-8")
            exe.chmod(exe.stat().st_mode | stat.S_IEXEC)
            keep = {k: os.environ.get(k) for k in ("CA_CHROME", "CHROME")}
            try:
                os.environ["CA_CHROME"] = str(exe)
                os.environ.pop("CHROME", None)
                self.assertEqual(rp.find_chrome(None), exe)
                self.assertEqual(rp.find_chrome(str(exe)), exe)
            finally:
                for k, v in keep.items():
                    if v is None:
                        os.environ.pop(k, None)
                    else:
                        os.environ[k] = v

    def test_no_site(self):
        err = io.StringIO()
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(rp.main([tmp]), 2)
        self.assertIn("ビルドしたサイトがない", err.getvalue())


@unittest.skipUnless(CHROME and Path(CHROME).is_file(), "CA_CHROME に Chrome の実行ファイルを指定したときだけ動く")
class TestRender(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        tmp = Path(cls.tmp.name)
        project = tmp / "project"
        (project / "docs").mkdir(parents=True)
        os.symlink(REPO / "overrides", project / "overrides")
        for rel, text in PAGES.items():
            p = project / "docs" / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8")
        (project / "nav.yml").write_text("nav:\n" + "".join(f"  - {rel}\n" for rel in PAGES), encoding="utf-8")
        (project / "mkdocs.yml").write_text((REPO / "mkdocs.yml").read_text(encoding="utf-8"), encoding="utf-8")
        cls.site = tmp / "site"
        env = dict(os.environ, NO_MKDOCS_2_WARNING="1")
        r = subprocess.run([sys.executable, "-m", "mkdocs", "build", "-q", "-f", str(project / "mkdocs.yml"), "-d", str(cls.site)],
                           cwd=project, env=env, capture_output=True, text=True, timeout=600)
        if r.returncode != 0:
            raise AssertionError("試験用のサイトを作れなかった:\n" + r.stdout + r.stderr)
        cls.json = tmp / "render.json"
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            cls.code = rp.main([str(cls.site), "--docs", str(project / "docs"), "--json", str(cls.json),
                                "--chrome", CHROME, "-j", "3"])
        cls.out = out.getvalue()
        cls.data = json.loads(cls.json.read_text(encoding="utf-8"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def kinds(self, page: str) -> set[str]:
        return {f["kind"] for f in self.data["findings"] if f["page"] == page}

    def test_exit_code_and_report(self):
        self.assertEqual(self.code, 1, self.out)
        self.assertIn("まとめ（件数・ページ数）", self.out)
        self.assertEqual(self.data["pages"], len(PAGES) + 1)          # 404.html も描く

    def test_clean_pages(self):
        for page in ("", "a/clean/", "a/diagram/", "404.html"):
            self.assertEqual(self.kinds(page), set(), page)

    def test_outside_request_is_caught(self):
        kinds = self.kinds("a/outside/")
        self.assertIn("outside-request", kinds)
        urls = [f["detail"] for f in self.data["findings"] if f["kind"] == "outside-request"]
        self.assertEqual(urls, ["https://example.com/a.png"])

    def test_breakage_is_caught(self):
        self.assertIn("leaked-markup", self.kinds("a/leak/"))
        self.assertIn("page-overflow", self.kinds("a/overflow/"))
        self.assertEqual(self.kinds("a/wide/"), {"wide-table"})

    def test_mermaid_is_drawn_from_the_local_copy(self):
        res = [r for r in self.data["results"] if r["page"] == "a/diagram/"]
        self.assertEqual(len(res), 2)
        self.assertTrue(all(r["counts"]["mermaid"] >= 1 and r["waited"]["mermaid"] for r in res))
        self.assertTrue(all(r["outside"] == 0 for r in res))


if __name__ == "__main__":
    unittest.main()
