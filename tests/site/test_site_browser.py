"""ブラウザで、サイトが外のサイトから読まないことと、Mermaid の写しが働くことを確かめる試験
（planning/design.md §8.5「外から読まない」。工程6a の担当 B1）。

環境変数 CA_CHROME に Chrome（headless shell でもよい）の実行ファイルを指定したときだけ動く。ないときは飛ばす。
2026-11-04 に Chrome for Testing 146 の chrome-headless-shell で通した。

    CA_CHROME=/path/to/chrome-headless-shell uv run python -m unittest discover -s tests/site

一時のフォルダに試験用のページ（図のないページ・図のページ2つ）を作り、本物の overrides/ と mkdocs.yml の設定で
ビルドして、127.0.0.1 で配る。Chrome は 127.0.0.1 のほかの名前を引けないようにして開き（外へは実際には出ない）、
NetLog に残った URL を見る。試験用の JS が instant navigation で「図のないページ → 図のページ → もう一つの図の
ページ」と移り、各ページで図が描かれたか（div.mermaid）と、本物の Mermaid が読まれたかを html の属性に書く。

- 図のないページから移っても、外のサイト（unpkg.com・api.github.com・フォントなど）へ問い合わせない
- 図のあるページでは写しが読まれて図が描かれ、図のないページだけを開いたときは写しを読まない
"""

from __future__ import annotations

import functools
import http.server
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHROME = os.environ.get("CA_CHROME", "")

AUTOCLICK_JS = r"""
// 試験だけの JS：instant navigation で移りながら、各ページの結果を html の data-ca-result に書く
(function () {
  var log = [];
  var count = 0;
  function record(s) {
    log.push(s);
    document.documentElement.setAttribute("data-ca-result", JSON.stringify(log));
  }
  document$.subscribe(function () {
    count++;
    var path = location.pathname;
    var tries = 0;
    var timer = setInterval(function () {
      tries++;
      var hasDiagram = !!document.querySelector("article .mermaid");
      var drawn = document.querySelectorAll("article div.mermaid").length;
      if (!hasDiagram || drawn > 0 || tries > 100) {
        clearInterval(timer);
        record({doc: count, path: path, drawn: drawn,
                real: !!(window.mermaid && typeof window.mermaid.parse === "function")});
        var go = document.getElementById("go");
        if (go) go.click();
      }
    }, 100);
  });
})();
"""

PAGES = {
    "index.md": "# トップ\n\n[図のないページ](a/plain.md)\n",
    "a/plain.md": "# 図のないページ\n\n[図のページへ](diagram.md){#go}\n",
    "a/diagram.md": "# 図のページ\n\n```mermaid\ngraph LR\n  A[見せる] --> B[確かめる]\n```\n\n"
                    "[もう一つの図のページへ](../b/diagram2.md){#go}\n",
    "b/diagram2.md": "# もう一つの図のページ\n\n```mermaid\nsequenceDiagram\n  人->>Claude: 頼む\n"
                     "  Claude-->>人: 返す\n```\n",
}


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@unittest.skipUnless(CHROME and Path(CHROME).is_file(), "CA_CHROME に Chrome の実行ファイルを指定したときだけ動く")
class BrowserTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        tmp = Path(cls.tmp.name)
        cls.tmp_path = tmp
        srv = tmp / "srv"
        srv.mkdir()
        handler = functools.partial(_QuietHandler, directory=str(srv))
        cls.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        cls.port = cls.server.server_port
        cls.base = f"http://127.0.0.1:{cls.port}/claude-atlas/"
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()

        project = tmp / "project"
        (project / "docs/assets/js").mkdir(parents=True)
        os.symlink(ROOT / "overrides", project / "overrides")
        for rel, text in PAGES.items():
            path = project / "docs" / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        (project / "docs/assets/js/autoclick.js").write_text(AUTOCLICK_JS, encoding="utf-8")
        (project / "nav.yml").write_text(
            "nav:\n  - index.md\n  - a/plain.md\n  - a/diagram.md\n  - b/diagram2.md\n", encoding="utf-8")
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        # instant navigation は sitemap の URL と配る所が合うときに働くので、site_url を手元にする
        config = re.sub(r"(?m)^site_url: .*$", f"site_url: {cls.base}", config)
        config = config.rstrip("\n") + "\n  - assets/js/autoclick.js\n"
        (project / "mkdocs.yml").write_text(config, encoding="utf-8")

        env = dict(os.environ, NO_MKDOCS_2_WARNING="1")
        proc = subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(project / "mkdocs.yml"),
             "-d", str(srv / "claude-atlas")],
            cwd=project, env=env, capture_output=True, text=True, timeout=600,
        )
        if proc.returncode != 0:
            raise AssertionError("試験用のサイトを作れなかった:\n" + proc.stdout + proc.stderr)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.tmp.cleanup()

    def open_in_chrome(self, name: str, path: str):
        prof = self.tmp_path / f"prof-{name}"
        netlog = self.tmp_path / f"net-{name}.json"
        proc = subprocess.run(
            [CHROME, "--headless", "--no-first-run", "--no-default-browser-check", "--disable-gpu",
             f"--user-data-dir={prof}",
             "--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE 127.0.0.1",
             "--virtual-time-budget=60000", f"--log-net-log={netlog}", "--dump-dom", self.base + path],
            capture_output=True, text=True, timeout=180,
        )
        shutil.rmtree(prof, ignore_errors=True)
        m = re.search(r'data-ca-result="([^"]*)"', proc.stdout)
        self.assertIsNotNone(m, f"試験用の JS の結果がない（Chrome の終了コード {proc.returncode}）:\n{proc.stderr[-2000:]}")
        result = json.loads(m.group(1).replace("&quot;", '"'))
        raw = netlog.read_text(encoding="utf-8", errors="replace")
        urls = set(re.findall(r'"url":"([^"]+)"', raw))
        own = f"http://127.0.0.1:{self.port}/"
        outside = sorted(u for u in urls if not u.startswith(own) and not u.startswith(("data:", "chrome", "about:", "blob:")))
        mermaid_loaded = any(u.startswith(own) and u.endswith("/mermaid.min.js") for u in urls)
        return result, outside, mermaid_loaded

    def test_instant_navigation_into_diagram_pages(self):
        result, outside, mermaid_loaded = self.open_in_chrome("instant", "a/plain/")
        self.assertEqual(outside, [], "外のサイトへ問い合わせた")
        self.assertEqual([r["path"] for r in result],
                         ["/claude-atlas/a/plain/", "/claude-atlas/a/diagram/", "/claude-atlas/b/diagram2/"])
        self.assertEqual([r["doc"] for r in result], [1, 2, 3], "instant navigation で移っていない")
        self.assertEqual([r["drawn"] for r in result], [0, 1, 1], "図が描かれていない")
        self.assertEqual([r["real"] for r in result], [False, True, True])
        self.assertTrue(mermaid_loaded)

    def test_page_without_diagram_does_not_load_mermaid(self):
        result, outside, mermaid_loaded = self.open_in_chrome("top", "")
        self.assertEqual(outside, [], "外のサイトへ問い合わせた")
        self.assertEqual(len(result), 1)
        self.assertFalse(result[0]["real"])
        self.assertFalse(mermaid_loaded, "図のないページで Mermaid の写しを読んだ")


if __name__ == "__main__":
    unittest.main()
