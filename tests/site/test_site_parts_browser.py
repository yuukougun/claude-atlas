"""ブラウザで、見た目の部品の動きを確かめる試験（planning/design.md §8.5・§9.3。工程6a の2段目の担当 V）。

環境変数 CA_CHROME に Chrome（headless shell でもよい）の実行ファイルを指定したときだけ動く（B1 の
test_site_browser.py と同じ）。ないときは飛ばす。2026-11-04 に Chrome for Testing 146 の chrome-headless-shell で通した。

    CA_CHROME=/path/to/chrome-headless-shell uv run python -m unittest discover -s tests/site

tests/site/fixtures/parts/ の試験用のページを、本物の overrides/ と mkdocs.yml の設定でビルドし、127.0.0.1 で配る。
Chrome は 127.0.0.1 のほかの名前を引けないようにして開き（外へは実際には出ない）、NetLog に残った URL を見る。
試験用の JS（下の PROBE。?probe=<場面> で場面を選ぶ）が部品を動かし、結果を html の data-ca-probe に書く。

- 期限切れの注意書き：期限の日が過ぎたページにだけ出る（日付を入れる）。pages.json が読めなくても止まらない
- 知識マップ：分野ごと・焦点（?focus=）・全体の表示、振り分けの辺の見た目、関連の囲み、instant navigation で移った先でも描く
- 絞り込みの欄：言い換え（data-ca-synonyms）・全角と半角・当たらない語・語を消したとき
- 幅 390px のライトとダーク：横にはみ出さない、レベルのバッジの色が配色に合う
- 外のサイトへ問い合わせない。Cytoscape.js の写しは地図のページでだけ読む。JS のエラーがない
"""

from __future__ import annotations

import functools
import html
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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_site_parts import build_mkdocs, make_project  # noqa: E402

CHROME = os.environ.get("CA_CHROME", "")

PROBE = r"""
// 試験だけの JS：?probe=<場面> の場面を動かし、結果を html の data-ca-probe に書く（done が真になったら終わり）
(function () {
  var scenario = new URLSearchParams(location.search).get("probe") || "";
  var res = { scenario: scenario, docs: [], errors: [], warnings: [], done: false };
  function write() { document.documentElement.setAttribute("data-ca-probe", JSON.stringify(res)); }
  window.addEventListener("error", function (e) { res.errors.push(String(e.message || e)); write(); });
  window.addEventListener("unhandledrejection", function (e) { res.errors.push("rejection: " + String(e.reason)); write(); });
  var origError = console.error, origWarn = console.warn;
  console.error = function () { res.errors.push(Array.prototype.join.call(arguments, " ")); write(); origError.apply(console, arguments); };
  console.warn = function () { res.warnings.push(Array.prototype.join.call(arguments, " ")); write(); origWarn.apply(console, arguments); };
  function finish() { res.done = true; write(); }
  function waitFor(test, then, limit) {
    var n = 0;
    var t = setInterval(function () {
      n++;
      var v = null;
      try { v = test(); } catch (e) { v = null; }
      if (v || n > (limit || 150)) { clearInterval(t); then(v); }
    }, 100);
  }
  function mapState(map) {
    var cy = map.cy;
    return {
      view: map.state.view, field: map.state.field, focus: map.state.focus,
      nodes: cy.nodes(".page").map(function (n) { return n.id(); }).sort(),
      ext: cy.nodes(".ext").map(function (n) { return n.id(); }).sort(),
      next: cy.nodes(".next").map(function (n) { return n.id(); }).sort(),
      fields: cy.nodes(".field").map(function (n) { return n.id(); }).sort(),
      related: cy.nodes(".rel").map(function (n) { return n.id(); }).sort(),
      relbox: cy.getElementById("__related").nonempty(),
      edges: cy.edges().map(function (e) { return [e.source().id(), e.target().id(), e.classes().filter(function (c) { return c !== "hl"; }).join(" ")]; })
        .sort(),
      status: document.querySelector(".ca-map__status").textContent,
      query: location.search,
    };
  }
  function layout() {
    var badge = document.querySelector(".ca-badge--level");
    return {
      scheme: document.body.getAttribute("data-md-color-scheme"),
      scrollWidth: document.documentElement.scrollWidth, innerWidth: window.innerWidth,
      levelBg: badge ? getComputedStyle(badge).backgroundColor : null,
      levelFg: badge ? getComputedStyle(badge).color : null,
    };
  }
  var docCount = 0;
  document$.subscribe(function () {
    docCount++;
    res.docs.push(location.pathname);
    write();
    if (scenario === "expiry-auto") {
      // ページを開いたときの注意書き（expiry.js が document$ で比べた後）
      setTimeout(function () {
        var head = document.querySelector("[data-ca-page]");
        var box = head.querySelector("[data-ca-expiry]");
        res.auto = { attr: head.getAttribute("data-ca-expires"), shown: !box.hidden, date: box.querySelector("time").textContent };
        finish();
      }, 500);
    } else if (scenario === "expiry") {
      waitFor(function () { return window.CAExpiry; }, function () {
        var head = document.querySelector("[data-ca-page]");
        var box = head.querySelector("[data-ca-expiry]");
        setTimeout(function () {
          // 1. 開いたとき：作る層が data-ca-expires に書いた期限の日と比べる
          res.auto = { attr: head.getAttribute("data-ca-expires"), shown: !box.hidden, date: box.querySelector("time").textContent,
                       datetime: box.querySelector("time").getAttribute("datetime"), visible: box.getClientRects().length > 0 };
          // 2. data-ca-expires がないとき：pages.json から引く
          head.removeAttribute("data-ca-expires");
          CAExpiry.check(document).then(function (exp) {
            res.fromJson = { expires: exp, shown: !box.hidden, date: box.querySelector("time").textContent };
            // 3. pages.json が読めないとき：止まらず、出さない
            head.setAttribute("data-ca-pages-json", "missing/pages.json");
            return CAExpiry.check(document);
          }).then(function (exp) {
            res.missing = { expires: exp, shown: !box.hidden };
            // 4. 期限の日を data 属性で渡す：pages.json を読まずに比べる
            head.setAttribute("data-ca-expires", "2001-02-03");
            return CAExpiry.check(document);
          }).then(function (exp) {
            res.direct = { expires: exp, shown: !box.hidden, date: box.querySelector("time").textContent };
            finish();
          });
        }, 500);
      });
    } else if (scenario === "map") {
      waitFor(function () { var r = document.querySelector(".ca-graph"); return r && r.caMap; }, function (map) {
        if (!map) { res.mapStatus = (document.querySelector(".ca-map__status") || {}).textContent; finish(); return; }
        res.first = mapState(map);
        res.legend = Array.prototype.map.call(document.querySelectorAll(".ca-map__legend li"), function (li) { return li.textContent; });
        map.setState({ view: "focus", focus: "when-to-lock" });
        res.focus = mapState(map);
        map.setState({ view: "all" });
        res.all = mapState(map);
        res.find = map.findPages("ＣＬＡＵＤＥ．ｍｄ の書き方");
        finish();
      });
    } else if (scenario === "nav") {
      if (docCount === 1) {
        // Material が instant navigation の受け口を付けた後に押す（最初の document$ の中ですぐ押すと、ふつうの移動になる）
        setTimeout(function () {
          var go = document.getElementById("go");
          if (go) go.click();
        }, 300);
      } else {
        waitFor(function () { var r = document.querySelector(".ca-graph"); return r && r.caMap; }, function (map) {
          res.navMap = map ? mapState(map) : null;
          finish();
        });
      }
    } else if (scenario === "filter") {
      waitFor(function () { var b = document.querySelector(".ca-filter"); return b && b.caFilter; }, function (api) {
        var article = document.querySelector("article");
        function visible() {
          return Array.prototype.filter.call(article.querySelectorAll("tbody tr"), function (tr) {
            return tr.getClientRects().length > 0;
          }).map(function (tr) { return tr.cells[0].textContent.trim(); });
        }
        function run(q) {
          api.input.value = q;
          api.apply();
          return { rows: visible(), status: document.querySelector(".ca-filter__status").textContent,
                   filtering: article.classList.contains("ca-filtering"), query: location.search,
                   h2: Array.prototype.filter.call(article.querySelectorAll("h2"), function (h) { return h.getClientRects().length > 0; })
                     .map(function (h) { return h.id; }),
                   abstractVisible: !!article.querySelector(".admonition.abstract") && article.querySelector(".admonition.abstract").getClientRects().length > 0,
                   infoVisible: article.querySelector(".ca-page-info").getClientRects().length > 0 };
        }
        var box = document.querySelector(".ca-filter");
        var abstract = article.querySelector(".admonition.abstract");
        res.beforeAbstract = !!(abstract && (box.compareDocumentPosition(abstract) & Node.DOCUMENT_POSITION_FOLLOWING));
        res.placeholder = api.input.getAttribute("placeholder");
        res.initial = run("");
        res.synonym = run("プランモード");
        res.fullwidth = run("ｈｏｏｋｓ");
        res.two = run("CLAUDE.md 守られない");
        res.none = run("存在しない語");
        res.reset = run("");
        finish();
      });
    } else if (scenario === "layout") {
      setTimeout(function () { res.layout = layout(); finish(); }, 300);
    } else {
      finish();
    }
  });
})();
"""


class _QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


@unittest.skipUnless(CHROME and Path(CHROME).is_file(), "CA_CHROME に Chrome の実行ファイルを指定したときだけ動く")
class PartsBrowserTest(unittest.TestCase):
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
        # instant navigation は sitemap の URL と配る所が合うときに働くので、site_url を手元にする
        cls.base = f"http://127.0.0.1:{cls.port}/claude-atlas/"
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        project = make_project(tmp, site_url=cls.base, extra_js={"probe.js": PROBE})
        code, log = build_mkdocs(project, srv / "claude-atlas")
        if code != 0:
            raise AssertionError("試験用のサイトを作れなかった:\n" + log)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.tmp.cleanup()

    def open(self, name: str, path: str, dark: bool = False) -> tuple[dict, list[str], set[str]]:
        prof = self.tmp_path / f"prof-{name}"
        netlog = self.tmp_path / f"net-{name}.json"
        args = [CHROME, "--headless", "--no-first-run", "--no-default-browser-check", "--disable-gpu", "--hide-scrollbars",
                f"--user-data-dir={prof}", "--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE 127.0.0.1",
                "--window-size=390,900", f"--blink-settings=preferredColorScheme={0 if dark else 1}",
                "--virtual-time-budget=60000", f"--log-net-log={netlog}", "--dump-dom", self.base + path]
        proc = subprocess.run(args, capture_output=True, text=True, timeout=180)
        shutil.rmtree(prof, ignore_errors=True)
        m = re.search(r'data-ca-probe="([^"]*)"', proc.stdout)
        self.assertIsNotNone(m, f"試験用の JS の結果がない（Chrome の終了コード {proc.returncode}）:\n{proc.stderr[-2000:]}")
        result = json.loads(html.unescape(m.group(1)))
        self.assertTrue(result["done"], f"{path}: 終わらなかった: {result}")
        raw = netlog.read_text(encoding="utf-8", errors="replace")
        urls = set(re.findall(r'"url":"([^"]+)"', raw))
        own = f"http://127.0.0.1:{self.port}/"
        outside = sorted(u for u in urls if not u.startswith(own) and not u.startswith(("data:", "chrome", "about:", "blob:")))
        mine = {u[len(own):].split("?")[0] for u in urls if u.startswith(own)}
        return result, outside, mine

    def assert_clean(self, result: dict, outside: list[str]):
        self.assertEqual(outside, [], "外のサイトへ問い合わせた")
        self.assertEqual(result["errors"], [], "JS のエラー")

    # ---- 期限切れの注意書き

    def test_expiry_notice_after_the_deadline(self):
        result, outside, mine = self.open("exp-past", "extend/what-to-put-in-claude-md/?probe=expiry")
        self.assert_clean(result, outside)
        auto = result["auto"]
        self.assertEqual((auto["attr"], auto["shown"], auto["visible"]), ("2000-01-31", True, True))
        self.assertEqual((auto["date"], auto["datetime"]), ("2000-01-31", "2000-01-31"))
        # data 属性がなければ pages.json から引く（作る層が extra.ca.expires を書く前の形）
        self.assertEqual(result["fromJson"], {"expires": "2000-01-31", "shown": True, "date": "2000-01-31"})
        self.assertIn("claude-atlas/assets/data/pages.json", mine)
        # pages.json が読めないとき：出さず、警告だけを書く
        self.assertEqual(result["missing"], {"expires": None, "shown": False})
        self.assertTrue(any("期限切れの注意書き" in w for w in result["warnings"]), result["warnings"])
        self.assertEqual(result["direct"], {"expires": "2001-02-03", "shown": True, "date": "2001-02-03"})

    def test_no_expiry_notice_before_the_deadline_or_without_dates(self):
        for name, path, attr in [("exp-future", "basics/context-window/?probe=expiry-auto", "2999-12-31"),
                                 ("exp-none", "start/how-to-use/?probe=expiry-auto", "")]:
            result, outside, mine = self.open(name, path)
            self.assert_clean(result, outside)
            self.assertEqual(result["auto"], {"attr": attr, "shown": False, "date": ""}, path)
            # 期限の日が data 属性にあるので、pages.json は読まない
            self.assertNotIn("claude-atlas/assets/data/pages.json", mine, path)

    # ---- 知識マップ

    def test_map_views(self):
        result, outside, mine = self.open("map", "start/knowledge-map/?probe=map")
        self.assert_clean(result, outside)
        self.assertIn("claude-atlas/assets/vendor/cytoscape-3.34.4/cytoscape.min.js", mine)
        self.assertIn("claude-atlas/assets/vendor/cytoscape-dagre-4.0.1/cytoscape-dagre.min.js", mine)
        self.assertIn("claude-atlas/assets/data/graph.json", mine)
        first = result["first"]
        # data-field="symptoms" の分野ごとの表示：症状のページ、ほかの分野の前（破線の枠）、振り分けの先の分野（→ の点）
        self.assertEqual((first["view"], first["field"]), ("field", "symptoms"))
        self.assertEqual(first["nodes"], ["context-window", "instructions-ignored"])
        self.assertEqual(first["ext"], ["context-window"])
        self.assertEqual(first["next"], ["next:enforce", "next:extend"])
        self.assertEqual(first["edges"], [["context-window", "instructions-ignored", ""]])
        self.assertIn("field=symptoms", first["query"])
        self.assertEqual(result["legend"][:5], ["使う", "整える", "任せる", "仕組みにする", "回す"])
        self.assertTrue(any("破線の矢印" in x for x in result["legend"]))
        # 焦点の表示：祖先（前提と振り分けの元）と子孫、振り分けの辺は route、関連の囲み（用語集）
        focus = result["focus"]
        self.assertEqual(focus["nodes"], ["context-window", "glossary", "instructions-ignored", "what-to-put-in-claude-md",
                                          "when-to-lock"])
        self.assertEqual(focus["related"], ["glossary"])
        self.assertTrue(focus["relbox"])
        self.assertIn(["instructions-ignored", "when-to-lock", "route"], focus["edges"])
        self.assertIn(["what-to-put-in-claude-md", "when-to-lock", ""], focus["edges"])
        self.assertIn(["when-to-lock", "glossary", "rel"], focus["edges"])
        self.assertIn("focus=when-to-lock", focus["query"])
        # 全体の表示：ページのある分野（入口と地図の用語集を含む）
        self.assertEqual(result["all"]["fields"], ["field:basics", "field:enforce", "field:extend", "field:start",
                                                   "field:symptoms"])
        self.assertEqual(result["find"][0], "what-to-put-in-claude-md")   # 短い題名に、全角の語でも当たる

    def test_map_opens_on_focus_from_the_page_link(self):
        result, outside, _ = self.open("map-focus", "start/knowledge-map/?probe=map&focus=instructions-ignored")
        self.assert_clean(result, outside)
        first = result["first"]
        self.assertEqual((first["view"], first["focus"]), ("focus", "instructions-ignored"))
        self.assertEqual(first["nodes"], ["context-window", "instructions-ignored", "what-to-put-in-claude-md", "when-to-lock"])
        self.assertFalse(first["relbox"])   # 関連（when-to-lock・context-window）は図にあるので、囲みは要らない
        self.assertEqual(sorted(e for e in first["edges"] if e[2] == "rel"),
                         [["instructions-ignored", "context-window", "rel"], ["instructions-ignored", "when-to-lock", "rel"]])

    def test_map_after_instant_navigation(self):
        result, outside, mine = self.open("nav", "start/how-to-use/?probe=nav")
        self.assert_clean(result, outside)
        self.assertEqual(result["docs"], ["/claude-atlas/start/how-to-use/", "/claude-atlas/start/knowledge-map/"])
        self.assertIsNotNone(result["navMap"], "移った先で地図が描かれない")
        self.assertEqual(result["navMap"]["view"], "field")
        self.assertIn("claude-atlas/assets/vendor/cytoscape-3.34.4/cytoscape.min.js", mine)

    def test_pages_without_map_do_not_load_cytoscape(self):
        result, outside, mine = self.open("plain", "basics/context-window/?probe=none")
        self.assert_clean(result, outside)
        self.assertFalse(any("cytoscape" in u for u in mine), mine)
        self.assertFalse(any("graph.json" in u for u in mine), mine)

    # ---- 絞り込みの欄

    def test_filter(self):
        result, outside, _ = self.open("filter", "start/reverse-index/?probe=filter")
        self.assert_clean(result, outside)
        self.assertTrue(result["beforeAbstract"], "欄が要点の前に移っていない")
        self.assertEqual(result["placeholder"], "語で行を絞り込む（例：hooks）")
        all_rows = ["CLAUDE.md に書いたのに守られない", "plan mode で立てた計画が雑", "ＨＯＯＫＳ で止めたい", "長い会話で前の話を忘れる"]
        self.assertEqual(result["initial"]["rows"], all_rows)
        self.assertTrue(result["initial"]["status"].startswith("4 行。"), result["initial"]["status"])
        syn = result["synonym"]
        self.assertEqual(syn["rows"], ["plan mode で立てた計画が雑"])
        self.assertIn("言い換え", syn["status"])
        self.assertEqual(syn["h2"], ["instructions"])
        self.assertFalse(syn["abstractVisible"])
        self.assertTrue(syn["infoVisible"])          # ページの最後の行は隠さない
        self.assertIn("filter=", syn["query"])
        self.assertEqual(result["fullwidth"]["rows"], ["ＨＯＯＫＳ で止めたい"])
        self.assertEqual(result["two"]["rows"], ["CLAUDE.md に書いたのに守られない"])
        self.assertEqual(result["none"]["rows"], [])
        self.assertIn("当たる行がない", result["none"]["status"])
        reset = result["reset"]
        self.assertEqual((reset["rows"], reset["filtering"], reset["abstractVisible"]), (all_rows, False, True))
        self.assertNotIn("filter=", reset["query"])

    # ---- 幅 390px のライトとダーク

    def test_layout_light_and_dark(self):
        expected = {False: ("default", "rgb(85, 152, 231)", "rgb(11, 11, 11)"),     # ライトの2段目 #5598e7・黒の字
                    True: ("slate", "rgb(42, 120, 214)", "rgb(255, 255, 255)")}     # ダークの2段目 #2a78d6・白の字
        for dark in (False, True):
            for path in ["symptoms/instructions-ignored/", "extend/what-to-put-in-claude-md/", "start/knowledge-map/",
                         "start/reverse-index/", ""]:
                name = f"layout-{'dark' if dark else 'light'}-{path.replace('/', '_') or 'top'}"
                result, outside, _ = self.open(name, path + "?probe=layout", dark=dark)
                self.assert_clean(result, outside)
                lay = result["layout"]
                self.assertEqual(lay["scheme"], expected[dark][0], path)
                self.assertLessEqual(lay["scrollWidth"], lay["innerWidth"], f"{path}（{'ダーク' if dark else 'ライト'}）が横にはみ出す")
                if path in ("symptoms/instructions-ignored/", "extend/what-to-put-in-claude-md/"):
                    self.assertEqual((lay["levelBg"], lay["levelFg"]), expected[dark][1:], path)


if __name__ == "__main__":
    unittest.main()
