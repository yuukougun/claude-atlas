"""外のリンクを確かめる道具（tools/check_links.py。設計書 §9.4 の手順6）の試験。`uv run python -m unittest discover -s tests/tools` で動く。

問い合わせは試験の中で偽物（fetch の差し替え）にする。実際のネットには出ない。値はすべて作りもの。
確かめること:
  - 対象の集め方：公開するページ（draft 以上・docs/）の本文と出典の url、コードの中の URL を除く、# 以降と末尾の / の違いの重なり、
    stub のページと stubs/ のページを除く、使っている所の記録
  - 問い合わせない：deny のドメイン（*. 付きも）・data の noai のドメイン・check_noai の既知の一覧・例の URL。問い合わせが 0 回
  - 転送：転送先を出す（恒久・一時の別）・多段・確かめないホストへの転送で止まる・転送の先が切れている・転送が多すぎる
  - 状態：正常・切れ・要確認（403・429）・接続できない・HEAD を断られたときの GET
  - 作法：同じホストへの間隔（偽の時計）・User-Agent に個人の情報がない
  - CLI：--dry-run は問い合わせない・表の出力・--json・--only-problems・終了コード
"""
from __future__ import annotations

import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))
SITE = Path(__file__).resolve().parent / "fixtures" / "gen" / "schema" / "site.yml"

import check_links as cl  # noqa: E402

PAGE = """---
id: {id}
title: {title}
type: feature
field: extend
chapter: 試験
order: 10
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る]
summary: 試験用の要約。
signs:
  - {{type: goal, text: 試験}}
volatility: 中
stage: {stage}
updated: 2026-11-01
---

本文
{body}
"""

SETTINGS = {"permissions": {"deny": ["WebFetch(domain:blocked.test.org)", "WebFetch(domain:*.blocked.test.org)"]}}

SOURCES = """domains:
  - {domain: noai.test.org, checked: '2026-11-01', noai: true, url: 'https://noai.test.org/'}
  - {domain: ok.test.org, checked: '2026-11-01', noai: false, url: 'https://ok.test.org/'}
sources:
  - {id: s-ok, url: 'https://ok.test.org/doc', title: 試験, kind: 公式文書, publisher: 試験, lang: en, checked: '2026-11-01'}
  - {id: s-noai, url: 'https://noai.test.org/page', title: 試験, kind: 公式文書, publisher: 試験, lang: en, checked: '2026-11-01'}
"""


class FakeNet:
    """URL → [(状態, Location)] か例外。呼ばれた (URL, method) を残す。"""

    def __init__(self, table: dict):
        self.table = table
        self.calls: list[tuple[str, str]] = []

    def __call__(self, url: str, method: str, timeout: float):
        self.calls.append((url, method))
        entry = self.table.get((url, method), self.table.get(url, (404, None)))
        if isinstance(entry, Exception):
            raise entry
        return entry


class LinksCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "site"
        (self.root / "schema").mkdir(parents=True)
        shutil.copy(SITE, self.root / "schema" / "site.yml")
        self.write("data/facts.yml", "facts: []\nfeatures: []\nnames: []\n")
        self.write("data/sources.yml", SOURCES)
        self.write("data/outdated-advice.yml", "advice: []\n")
        self.write("data/inspection.yml", "last:\n  date: null\n")
        self.write(".claude/settings.json", json.dumps(SETTINGS))

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel: str, text: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def page(self, pid: str, body: str, stage: str = "draft", base: str = "docs") -> None:
        self.write(f"{base}/extend/{pid}.md", PAGE.format(id=pid, title=pid, stage=stage, body=body))

    def targets(self) -> dict[str, cl.Target]:
        targets, _ = cl.collect_targets(self.root)
        return {t.url: t for t in targets}

    def run_cli(self, net: FakeNet, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = cl.main(["--root", str(self.root), "--interval", "0", *args], fetch=net)
        return code, out.getvalue(), err.getvalue()


class CollectTests(LinksCase):
    def test_pages_and_sources_are_collected_with_users(self):
        self.page("a", "[公式](https://ok.test.org/doc) と <https://ok.test.org/x>。\n(https://ok.test.org/p).")
        ts = self.targets()
        self.assertEqual(ts["https://ok.test.org/doc"].used_by, ["ページ a", "出典 s-ok"])
        self.assertIn("https://ok.test.org/x", ts)
        self.assertIn("https://ok.test.org/p", ts)       # 括弧と句点は URL に入らない

    def test_code_is_excluded_and_duplicates_are_merged(self):
        self.page("a", "`https://code.test.org/inline`\n\n```\nhttps://code.test.org/fence\n```\n\n"
                       "[x](https://ok.test.org/d#top) [y](https://ok.test.org/d/)")
        ts = self.targets()
        self.assertNotIn("https://code.test.org/inline", ts)
        self.assertNotIn("https://code.test.org/fence", ts)
        self.assertEqual([u for u in ts if u.startswith("https://ok.test.org/d") and u != "https://ok.test.org/doc"], ["https://ok.test.org/d"])

    def test_stub_pages_are_not_collected(self):
        self.page("s", "[x](https://only-stub.test.org/a)", stage="stub")
        self.page("t", "[x](https://in-stubs.test.org/a)", stage="draft", base="stubs")
        ts = self.targets()
        self.assertNotIn("https://only-stub.test.org/a", ts)
        self.assertNotIn("https://in-stubs.test.org/a", ts)


class SkipTests(LinksCase):
    def test_deny_noai_known_and_example_hosts_are_not_queried(self):
        self.page("a", "https://blocked.test.org/a https://sub.blocked.test.org/b https://noai.test.org/c "
                       "https://atcoder.jp/x https://www.codeforces.com/y https://example.com/z https://ok.test.org/fine")
        ts = self.targets()
        for u in ("https://blocked.test.org/a", "https://sub.blocked.test.org/b", "https://noai.test.org/c",
                  "https://atcoder.jp/x", "https://www.codeforces.com/y", "https://example.com/z", "https://noai.test.org/page"):
            self.assertIsNotNone(ts[u].skip, u)
        self.assertIsNone(ts["https://ok.test.org/fine"].skip)
        self.assertIn("deny", ts["https://blocked.test.org/a"].skip)
        net = FakeNet({"https://ok.test.org/fine": (200, None), "https://ok.test.org/doc": (200, None)})
        code, out, _ = self.run_cli(net)
        self.assertEqual(code, 0)
        self.assertEqual(sorted(u for u, _ in net.calls), ["https://ok.test.org/doc", "https://ok.test.org/fine"])
        self.assertIn("確かめない", out)
        self.assertNotIn("blocked.test.org/a | 200", out)

    def test_redirect_into_known_noai_host_is_not_followed(self):
        self.page("a", "https://ok.test.org/jump")
        net = FakeNet({"https://ok.test.org/jump": (302, "https://atcoder.jp/contests"), "https://ok.test.org/doc": (200, None)})
        code, out, _ = self.run_cli(net, "--json")
        self.assertEqual(code, 0)
        self.assertNotIn("https://atcoder.jp/contests", [u for u, _ in net.calls])
        row = [r for r in json.loads(out) if r["url"] == "https://ok.test.org/jump"][0]
        self.assertEqual((row["status"], row["final_url"]), (cl.SKIPPED, "https://atcoder.jp/contests"))

    def test_dry_run_makes_no_request_and_lists_targets(self):
        self.page("a", "https://blocked.test.org/a https://ok.test.org/fine")
        net = FakeNet({})
        code, out, _ = self.run_cli(net, "--dry-run")
        self.assertEqual(code, 0)
        self.assertEqual(net.calls, [])
        self.assertIn("問い合わせていない", out)
        row = [l for l in out.splitlines() if "https://blocked.test.org/a" in l][0]
        self.assertIn("確かめない", row)
        row = [l for l in out.splitlines() if "https://ok.test.org/fine" in l][0]
        self.assertIn("問い合わせる", row)
        self.assertIn("ページ a", row)

    def test_dry_run_json(self):
        self.page("a", "https://ok.test.org/fine")
        code, out, _ = self.run_cli(FakeNet({}), "--dry-run", "--json")
        self.assertEqual(code, 0)
        rows = {r["url"]: r for r in json.loads(out)}
        self.assertIsNone(rows["https://ok.test.org/fine"]["skip"])
        self.assertIsNotNone(rows["https://noai.test.org/page"]["skip"])


class ProbeTests(LinksCase):
    def probe(self, table: dict, url: str = "https://ok.test.org/a", blocked: dict | None = None):
        net = FakeNet(table)
        t = cl.Target(url, ["ページ a"])
        r = cl.probe(t, net, cl.HostGate(0), 5, blocked or {"blocked.test.org": "deny"})
        return r, net

    def test_ok_broken_and_manual(self):
        self.assertEqual(self.probe({"https://ok.test.org/a": (200, None)})[0].status, cl.OK)
        r, _ = self.probe({"https://ok.test.org/a": (404, None)})
        self.assertEqual((r.status, r.http), (cl.BROKEN, 404))
        self.assertEqual(self.probe({"https://ok.test.org/a": (500, None)})[0].status, cl.BROKEN)
        self.assertEqual(self.probe({"https://ok.test.org/a": (429, None)})[0].status, cl.MANUAL)
        self.assertEqual(self.probe({"https://ok.test.org/a": (403, None)})[0].status, cl.MANUAL)

    def test_head_refused_retries_with_get_only(self):
        r, net = self.probe({("https://ok.test.org/a", "HEAD"): (405, None), ("https://ok.test.org/a", "GET"): (200, None)})
        self.assertEqual(r.status, cl.OK)
        self.assertEqual([m for _, m in net.calls], ["HEAD", "GET"])
        r, net = self.probe({"https://ok.test.org/a": (404, None)})
        self.assertEqual([m for _, m in net.calls], ["HEAD"])         # 404 は GET でやり直さない

    def test_connection_error_is_broken(self):
        r, _ = self.probe({"https://ok.test.org/a": TimeoutError("timed out")})
        self.assertEqual(r.status, cl.BROKEN)
        self.assertIn("timed out", r.note)

    def test_permanent_redirect_shows_destination(self):
        r, net = self.probe({"https://ok.test.org/a": (308, "/b"), "https://ok.test.org/b": (200, None)})
        self.assertEqual((r.status, r.http, r.final_url, r.first_code), (cl.MOVED, 200, "https://ok.test.org/b", 308))
        self.assertEqual([u for u, _ in net.calls], ["https://ok.test.org/a", "https://ok.test.org/b"])

    def test_multi_hop_redirect_reports_final_url_and_first_code(self):
        r, _ = self.probe({"https://ok.test.org/a": (302, "https://other.test.org/m"),
                           "https://other.test.org/m": (301, "https://other.test.org/z"),
                           "https://other.test.org/z": (200, None)})
        self.assertEqual((r.status, r.final_url, r.first_code), (cl.MOVED, "https://other.test.org/z", 302))

    def test_redirect_to_unchecked_host_stops_without_request(self):
        r, net = self.probe({"https://ok.test.org/a": (301, "https://blocked.test.org/x")})
        self.assertEqual(r.status, cl.SKIPPED)
        self.assertEqual(r.final_url, "https://blocked.test.org/x")
        self.assertIn("転送先は確かめない", r.note)
        self.assertEqual([u for u, _ in net.calls], ["https://ok.test.org/a"])

    def test_redirect_to_broken_page_is_broken(self):
        r, _ = self.probe({"https://ok.test.org/a": (301, "/gone"), "https://ok.test.org/gone": (404, None)})
        self.assertEqual((r.status, r.final_url), (cl.BROKEN, "https://ok.test.org/gone"))
        self.assertIn("転送の先が切れている", r.note)

    def test_too_many_redirects_is_broken(self):
        r, _ = self.probe({"https://ok.test.org/a": (302, "/a")})
        self.assertEqual(r.status, cl.BROKEN)
        self.assertIn("転送が", r.note)


class MannerTests(unittest.TestCase):
    def test_same_host_requests_are_spaced_and_other_hosts_are_not(self):
        now = [0.0]
        slept: list[float] = []
        def sleep(d: float) -> None:
            slept.append(d)
            now[0] += d
        gate = cl.HostGate(2.0, clock=lambda: now[0], sleep=sleep)
        delays = [gate.wait("a.test.org"), gate.wait("a.test.org"), gate.wait("b.test.org"), gate.wait("a.test.org")]
        self.assertEqual(delays, [0, 2.0, 0, 2.0])

    def test_user_agent_has_no_personal_information(self):
        self.assertEqual(cl.USER_AGENT, "claude-atlas-link-check")
        self.assertNotRegex(cl.USER_AGENT, r"[@/]|https?:")

    def test_interleave_alternates_hosts(self):
        ts = [cl.Target(f"https://{h}.test.org/{i}") for h in "ab" for i in range(2)]
        self.assertEqual([t.url for t in cl.interleave(ts)],
                         ["https://a.test.org/0", "https://b.test.org/0", "https://a.test.org/1", "https://b.test.org/1"])


class CliTests(LinksCase):
    def test_table_json_and_exit_code(self):
        self.page("a", "[m](https://ok.test.org/moved) [b](https://ok.test.org/broken) [g](https://ok.test.org/good)")
        net = FakeNet({"https://ok.test.org/moved": (301, "https://ok.test.org/new"), "https://ok.test.org/new": (200, None),
                       "https://ok.test.org/broken": (404, None), "https://ok.test.org/good": (200, None),
                       "https://ok.test.org/doc": (200, None)})
        code, out, _ = self.run_cli(net)
        self.assertEqual(code, 1)                                     # 切れがあれば 1
        lines = out.splitlines()
        self.assertTrue(lines[0].startswith("5 件："), lines[0])
        self.assertIn("| 状態 | URL | HTTP | 転送先 | メモ | 使っている所 |", out)
        moved = [l for l in lines if "ok.test.org/moved" in l][0]
        self.assertIn("転送", moved)
        self.assertIn("https://ok.test.org/new（301）", moved)
        # 切れが先に並ぶ
        self.assertLess(out.index("ok.test.org/broken"), out.index("ok.test.org/good"))
        code, out, _ = self.run_cli(net, "--only-problems")
        self.assertNotIn("ok.test.org/good", out)
        code, out, _ = self.run_cli(net, "--json")
        rows = {r["url"]: r for r in json.loads(out)}
        self.assertEqual(rows["https://ok.test.org/moved"]["final_url"], "https://ok.test.org/new")
        self.assertEqual(rows["https://noai.test.org/page"]["status"], cl.SKIPPED)

    def test_exit_zero_without_broken_and_files_unchanged(self):
        self.page("a", "[g](https://ok.test.org/good)")
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        net = FakeNet({"https://ok.test.org/good": (200, None), "https://ok.test.org/doc": (429, None)})
        code, _, _ = self.run_cli(net)
        self.assertEqual(code, 0)                                     # 要確認だけなら 0
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_bad_arguments_and_unreadable_site(self):
        self.assertEqual(self.run_cli(FakeNet({}), "--workers", "0")[0], 2)
        empty = Path(self._tmp.name) / "empty"
        empty.mkdir()
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = cl.main(["--root", str(empty), "--dry-run"])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
