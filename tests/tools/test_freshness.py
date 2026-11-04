"""鮮度の点検の道具（tools/freshness.py。設計書 §9.4 の手順の1・2・5）の試験。`uv run python -m unittest discover -s tests/tools` で動く。

一時フォルダに小さなサイト（schema/site.yml は fixtures/gen の写し・ページ5・data/）を作って確かめる。値はすべて作りもの。
確かめること:
  - match：features の照合の語・id、ページの tracks と aliases、facts の id、names の旧名と今の名前での当たりと、影響のあるページ
    （tracks のページ・主のページ・fact と name の目印を持つページ）と数値の一覧。大文字小文字・複数形・「-」「_」空白の揺れの吸収、
    英数字の続く語への当たらなさ、設定の exclude と --exclude、最短の長さ、行番号、--json、標準入力
  - last と stamp：記録の読み書き（注の残り方・古い版や日付を断る・--force・不正な値）
  - checked：front matter の checked を足す・進める・新しければ変えない・verified を触らない・ページがないとき
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

import freshness as fr  # noqa: E402

PAGE = """---
id: {id}
title: {title}
type: feature
field: extend
chapter: 試験
order: {order}
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る]
summary: 試験用の要約。
{extra}signs:
  - {{type: goal, text: 試験}}
volatility: 中
stage: draft
updated: 2026-11-01
{tail}---

本文{body}
"""

FACTS = """facts:
  - id: widget-limit
    title: 試験用の上限
    value: 10
    sources: [s1]
    checked: 2026-10-01
    status: 確認済み
  - id: alpha-flag
    title: 試験用のフラグ
    value: 1
    sources: [s1]
    checked: 2026-10-01
    status: 確認済み
features:
  - id: widget-hooks
    title: 試験のフック
    page: hooks-main
    match_terms: [PreWidgetUse, widget hook, Goal, ab]
    sources: [s1]
    checked: 2026-10-01
    status: 確認済み
  - id: sample-skills
    title: 試験のスキル
    page: skills-main
    match_terms: [SKILL.md, sub-agent]
    sources: [s1]
    checked: 2026-10-01
    status: 確認済み
names:
  - id: max-to-ultra
    current: Ultra（新しい名前）
    old: [Max 20x]
    changed: {date: 2026-10-30}
    feature: sample-skills
    sources: [s1]
    checked: 2026-10-01
    status: 確認済み
"""

INSPECTION = """# 試験用
last:
  date: null            # 前回の点検の日
  claude_code: null     # 版
  release_notes: null   # リリースノート
  news: null            # ニュース
"""


class FreshCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "site"
        (self.root / "schema").mkdir(parents=True)
        shutil.copy(SITE, self.root / "schema" / "site.yml")
        self.write("data/facts.yml", FACTS)
        self.write("data/sources.yml", "domains: []\nsources: []\n")
        self.write("data/outdated-advice.yml", "advice: []\n")
        self.write("data/inspection.yml", INSPECTION)
        self.page("extend", "hooks-main", "フックの基本", aliases="[フック入門, Widget Basics]", tracks="[widget-hooks]")
        self.page("extend", "skills-main", "スキルの基本")
        self.page("extend", "hook-vs-skill", "使い分け", tracks="[widget-hooks, sample-skills, only-tracked]")
        self.page("extend", "limits-page", "上限の話", body="\n\n<!-- fact:begin widget-limit -->10<!-- fact:end -->\n"
                                                           "<!-- name:begin max-to-ultra -->Ultra<!-- name:end -->")
        self.page("extend", "plain-page", "関係のないページ")
        self.config = Path(self._tmp.name) / "freshness.yml"
        self.config.write_text("exclude: [goal, forks]\nmin_length: 3\n", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel: str, text: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")

    def page(self, field: str, pid: str, title: str, aliases: str | None = None, tracks: str | None = None, body: str = "",
             tail: str = "") -> None:
        extra = (f"aliases: {aliases}\n" if aliases else "") + (f"tracks: {tracks}\n" if tracks else "")
        self.write(f"docs/{field}/{pid}.md", PAGE.format(id=pid, title=title, order=10, extra=extra, body=body, tail=tail))

    def cli(self, *args: str, stdin: str | None = None) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        old_in = sys.stdin
        if stdin is not None:
            sys.stdin = io.StringIO(stdin)
        try:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = fr.main(["--root", str(self.root), *args])
        finally:
            sys.stdin = old_in
        return code, out.getvalue(), err.getvalue()

    def match(self, text: str, *extra: str) -> dict:
        code, out, err = self.cli("match", text, "--config", str(self.config), "--json", *extra)
        self.assertEqual(code, 0, err)
        return json.loads(out)

    @staticmethod
    def page_ids(res: dict) -> list[str]:
        return [r["id"] for r in res["pages"]]

    @staticmethod
    def number_ids(res: dict) -> list[str]:
        return [r["id"] for r in res["numbers"]]


class MatchTests(FreshCase):
    def test_feature_term_hits_main_and_tracking_pages(self):
        res = self.match("Added PreWidgetUse event for plugins")
        self.assertEqual(set(self.page_ids(res)), {"hooks-main", "hook-vs-skill"})
        self.assertEqual(self.number_ids(res), ["features/widget-hooks"])
        hit = res["pages"][0]["hits"][0]
        self.assertEqual((hit["term"], hit["source"], hit["line"]), ("PreWidgetUse", "features:widget-hooks の照合の語", 1))

    def test_case_plural_and_separator_variants(self):
        for text in ("widget hooks now run", "WIDGET-HOOK fixed", "widget_hook", "Widget  Hooks"):
            self.assertIn("hooks-main", self.page_ids(self.match(text)), text)
        self.assertIn("skills-main", self.page_ids(self.match("the skill.md file is read")))
        self.assertIn("skills-main", self.page_ids(self.match("subagent and Sub Agents")))

    def test_no_hit_inside_longer_words(self):
        self.assertEqual(self.page_ids(self.match("widget hooked and xPreWidgetUse2 and Ultraviolet")), [])

    def test_line_number_is_first_hit(self):
        res = self.match("line one\nline two\nfixed widget hook\nwidget hook again")
        self.assertEqual(res["pages"][0]["hits"][0]["line"], 3)

    def test_tracks_only_id_hits_its_own_page(self):
        res = self.match("fixed only-tracked behaviour")
        self.assertEqual(self.page_ids(res), ["hook-vs-skill"])
        self.assertEqual(res["pages"][0]["hits"][0]["source"], "ページの tracks")
        self.assertEqual(res["numbers"], [])

    def test_alias_hits_its_page(self):
        res = self.match("Widget Basics page")
        self.assertEqual(self.page_ids(res), ["hooks-main"])
        self.assertEqual(res["pages"][0]["hits"][0]["source"], "ページの aliases")
        self.assertEqual(self.page_ids(self.match("フック入門を読む")), ["hooks-main"])

    def test_fact_id_hits_fact_and_pages_with_marker(self):
        res = self.match("changed the widget-limit to 20")
        self.assertEqual(self.number_ids(res), ["facts/widget-limit"])
        self.assertEqual(self.page_ids(res), ["limits-page"])
        self.assertEqual(self.page_ids(self.match("alpha flag renamed")), [])
        self.assertEqual(self.number_ids(self.match("alpha flag renamed")), ["facts/alpha-flag"])

    def test_name_hits_marker_pages_and_feature_pages(self):
        res = self.match("Max 20x is now Ultra")
        self.assertIn("names/max-to-ultra", self.number_ids(res))
        self.assertTrue({"limits-page", "skills-main", "hook-vs-skill"} <= set(self.page_ids(res)))
        self.assertNotIn("features/sample-skills", self.number_ids(res))
        by = {r["id"]: r for r in res["numbers"]}["names/max-to-ultra"]
        self.assertEqual({h["term"] for h in by["hits"]}, {"Max 20x", "Ultra"})

    def test_excluded_terms_are_dropped_and_reported(self):
        res = self.match("A new goal and the Goals feature")
        self.assertEqual(res["pages"], [])
        self.assertEqual([r["term"] for r in res["excluded"]], ["Goal"])
        res2 = self.match("A new goal", "--config", str(self.root / "no-such.yml"))
        self.assertEqual(set(self.page_ids(res2)), {"hooks-main", "hook-vs-skill"})

    def test_exclude_option_adds_terms(self):
        self.assertTrue(self.page_ids(self.match("PreWidgetUse")))
        res = self.match("PreWidgetUse", "--exclude", "prewidgetuse")
        self.assertEqual(res["pages"], [])

    def test_short_terms_are_skipped(self):
        res = self.match("the ab flag and AB")
        self.assertEqual(res["pages"], [])
        self.assertIn("ab", res["skipped_short"])

    def test_text_output_shape(self):
        code, out, _ = self.cli("match", "Max 20x renamed", "--config", str(self.config))
        self.assertEqual(code, 0)
        self.assertIn("## 影響のあるページ（", out)
        self.assertIn("- limits-page「上限の話」 [draft]", out)
        self.assertIn("names:max-to-ultra", out)
        self.assertIn("## 影響のある数値（1）", out)
        self.assertIn("- names/max-to-ultra", out)
        self.assertIn("関わるページ：", out)

    def test_stdin_and_file_input(self):
        code, out, _ = self.cli("match", "-", "--config", str(self.config), "--json", stdin="x\nPreWidgetUse")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out)["pages"][0]["hits"][0]["line"], 2)
        f = Path(self._tmp.name) / "log.txt"
        f.write_text("widget hook", encoding="utf-8")
        code, out, _ = self.cli("match", "-f", str(f), "--config", str(self.config), "--json")
        self.assertEqual(code, 0)
        self.assertIn("hooks-main", self.page_ids(json.loads(out)))

    def test_no_hits(self):
        code, out, _ = self.cli("match", "nothing relevant here", "--config", str(self.config))
        self.assertEqual(code, 0)
        self.assertIn("影響のあるページ（0）", out)
        self.assertIn("影響のある数値（0）", out)

    def test_real_config_loads_and_excludes_general_words(self):
        st = fr.load_settings(None, [])
        self.assertIn("goal", st.exclude)
        self.assertEqual(st.min_length, 3)


class LastStampTests(FreshCase):
    def test_last_before_first_inspection(self):
        code, out, _ = self.cli("last")
        self.assertEqual(code, 0)
        self.assertIn("まだない", out)
        code, out, _ = self.cli("last", "--json")
        self.assertEqual(json.loads(out), {"date": None, "claude_code": None, "release_notes": None, "news": None})

    def test_stamp_writes_and_last_reads_back(self):
        code, out, err = self.cli("stamp", "--version", "2.1.320", "--date", "2026-11-10")
        self.assertEqual(code, 0, err)
        text = self.read("data/inspection.yml")
        self.assertIn("claude_code: 2.1.320", text)
        self.assertIn("date: '2026-11-10'", text)
        self.assertIn("# 前回の点検の日", text)             # 注は残る
        self.assertTrue(text.startswith("# 試験用\n"))
        code, out, _ = self.cli("last", "--json")
        self.assertEqual(json.loads(out), {"date": "2026-11-10", "claude_code": "2.1.320",
                                           "release_notes": "2026-11-10", "news": "2026-11-10"})

    def test_stamp_separate_dates_and_note(self):
        code, _, err = self.cli("stamp", "--version", "2.1.320", "--date", "2026-11-10", "--release-notes-date", "2026-11-08",
                                "--news-date", "2026-11-09", "--note", "ニュースは「x」まで")
        self.assertEqual(code, 0, err)
        code, out, _ = self.cli("last", "--json")
        got = json.loads(out)
        self.assertEqual((got["release_notes"], got["news"], got["note"]), ("2026-11-08", "2026-11-09", "ニュースは「x」まで"))
        self.cli("stamp", "--version", "2.1.321", "--date", "2026-11-11", "--note", "二度目")
        self.assertEqual(self.read("data/inspection.yml").count("note:"), 1)

    def test_stamp_refuses_older_unless_forced(self):
        self.assertEqual(self.cli("stamp", "--version", "2.1.320", "--date", "2026-11-10")[0], 0)
        before = self.read("data/inspection.yml")
        code, _, err = self.cli("stamp", "--version", "2.1.99", "--date", "2026-11-11")
        self.assertEqual(code, 1)
        self.assertIn("古い版", err)
        code, _, err = self.cli("stamp", "--version", "2.1.321", "--date", "2026-11-01")
        self.assertEqual(code, 1)
        self.assertEqual(self.read("data/inspection.yml"), before)
        self.assertEqual(self.cli("stamp", "--version", "2.1.99", "--date", "2026-11-01", "--force")[0], 0)
        self.assertIn("claude_code: 2.1.99", self.read("data/inspection.yml"))

    def test_stamp_rejects_bad_values(self):
        before = self.read("data/inspection.yml")
        self.assertEqual(self.cli("stamp", "--version", "v2.1", "--date", "2026-11-10")[0], 2)
        self.assertEqual(self.cli("stamp", "--version", "2.1.1", "--date", "2026-13-10")[0], 2)
        self.assertEqual(self.cli("stamp", "--version", "2.1.1", "--date", "2026-11-10", "--news-date", "x")[0], 2)
        self.assertEqual(self.read("data/inspection.yml"), before)

    def test_stamp_output_passes_the_schema(self):
        from lib.schema import load_validator
        from lib.yamlio import read_yaml, to_jsonable
        self.cli("stamp", "--version", "2.1.320", "--date", "2026-11-10", "--note", "試験")
        v = load_validator(REPO / "schema" / "inspection.schema.json")
        doc = read_yaml(self.root / "data" / "inspection.yml")
        self.assertEqual(list(v.errors(to_jsonable(doc.data))), [])


class CheckedTests(FreshCase):
    def test_adds_checked_before_closing_marker(self):
        code, out, err = self.cli("checked", "plain-page", "skills-main", "--date", "2026-11-10")
        self.assertEqual(code, 0, err)
        for pid in ("plain-page", "skills-main"):
            text = self.read(f"docs/extend/{pid}.md")
            self.assertIn("updated: 2026-11-01\nchecked: 2026-11-10\n---\n\n本文", text)
        self.assertIn("plain-page：checked: なし → 2026-11-10", out)
        self.assertNotIn("checked", self.read("docs/extend/hooks-main.md"))

    def test_advances_existing_and_keeps_verified(self):
        self.page("extend", "plain-page", "関係のないページ",
                  tail="verified: 2026-10-20\nverified_with: {claude_code: 2.1.300, channel: latest}\nchecked: 2026-10-25\n")
        code, _, err = self.cli("checked", "plain-page", "--date", "2026-11-10")
        self.assertEqual(code, 0, err)
        text = self.read("docs/extend/plain-page.md")
        self.assertIn("checked: 2026-11-10\n---", text)
        self.assertEqual(text.count("checked:"), 1)
        self.assertIn("verified: 2026-10-20\nverified_with: {claude_code: 2.1.300, channel: latest}\n", text)
        self.assertEqual(text.split("---")[2].strip(), "本文")

    def test_same_or_newer_is_kept(self):
        self.page("extend", "plain-page", "関係のないページ", tail="checked: 2026-11-20\n")
        before = self.read("docs/extend/plain-page.md")
        code, out, _ = self.cli("checked", "plain-page", "--date", "2026-11-10")
        self.assertEqual(code, 0)
        self.assertIn("のまま", out)
        self.assertEqual(self.read("docs/extend/plain-page.md"), before)

    def test_missing_page_exits_1_and_others_are_written(self):
        code, out, _ = self.cli("checked", "no-such-page", "plain-page", "--date", "2026-11-10")
        self.assertEqual(code, 1)
        self.assertIn("no-such-page：ページがない", out)
        self.assertIn("checked: 2026-11-10", self.read("docs/extend/plain-page.md"))

    def test_bad_date_is_refused(self):
        before = self.read("docs/extend/plain-page.md")
        self.assertEqual(self.cli("checked", "plain-page", "--date", "11/10")[0], 2)
        self.assertEqual(self.read("docs/extend/plain-page.md"), before)

    def test_checked_moves_the_expiry_date(self):
        from lib import load_atlas
        self.page("extend", "plain-page", "関係のないページ", tail="verified: 2026-10-01\n")
        atlas = load_atlas(self.root)
        page = next(p for p in atlas.pages if p.id == "plain-page")
        before = atlas.expiry(page)
        self.cli("checked", "plain-page", "--date", "2026-11-10")
        atlas = load_atlas(self.root)
        after = atlas.expiry(next(p for p in atlas.pages if p.id == "plain-page"))
        self.assertEqual(before.date.isoformat(), "2026-12-30")           # volatility 中＝90日。verified 2026-10-01 + 90日
        self.assertGreater(after.date, before.date)


if __name__ == "__main__":
    unittest.main()
