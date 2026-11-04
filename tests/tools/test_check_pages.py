"""tools/check_pages.py と検査の層（tools/checks/）の front matter の検査の試験。
`uv run python -m unittest discover -s tests/tools` で動く。

fixtures/checks/ は、エラーも警告も出ない小さな置き場所（README.md に中身）。各試験はそれを一時フォルダに写し、本物の
schema/（site.yml・keys.yml・*.schema.json）を足してから1か所だけ変え、出るはずの指摘（検査の名前とページの id の組）
だけが出ることを確かめる。今日は 2026-11-04 に固定する（確認日の期限のため）。試験は検査ごとに書き、@covers で
記録する（test_every_check_has_a_test が、front matter に当てるすべての検査に試験があることを確かめる。前提と関連の
規則は test_checks_relations.py が check_catalog.py と照らして確かめる）。
"""
from __future__ import annotations

import contextlib
import datetime
import io
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "checks"
SMALL = Path(__file__).resolve().parent / "fixtures" / "small"
sys.path.insert(0, str(REPO / "tools"))

import check_catalog as cc  # noqa: E402
import check_pages  # noqa: E402
from checks import ERROR, FRONT_MATTER, WARNING, checks_for, load_context, run_checks  # noqa: E402
from checks.config import ignored, parse_ignore  # noqa: E402

TODAY = datetime.date(2026, 11, 4)
COVERED: set[str] = set()
SHARED = {c.name for c in cc.CHECKS}
LINE_RE = re.compile(r"^(エラー|警告): [^:]+(:\d+)?: \S+: \[[^\]]+\] \S.*$")

RVL = "docs/basics/request-vs-lock.md"
II = "docs/symptoms/instructions-ignored.md"
HTU = "docs/start/how-to-use.md"
CC = "docs/verify/completion-check.md"
HB = "stubs/enforce/hooks-basics.md"


def covers(*names: str):
    COVERED.update(names)
    return lambda func: func


class PagesCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "repo"
        shutil.copytree(FIXTURE, self.root)
        shutil.copytree(REPO / "schema", self.root / "schema")

    def tearDown(self):
        self._tmp.cleanup()

    # ---- 変える

    def path(self, rel: str) -> Path:
        return self.root / rel

    def read(self, rel: str) -> str:
        return self.path(rel).read_text(encoding="utf-8")

    def write(self, rel: str, text: str) -> None:
        p = self.path(rel)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def replace(self, rel: str, old: str, new: str) -> None:
        text = self.read(rel)
        self.assertIn(old, text, rel)
        self.write(rel, text.replace(old, new, 1))

    def append(self, rel: str, text: str) -> None:
        self.write(rel, self.read(rel) + text)

    # ---- 検査する

    def issues(self, today: datetime.date = TODAY):
        return run_checks(load_context(self.root, today=today))

    def assertFound(self, *expected: tuple[str, str], today: datetime.date = TODAY):
        """指摘の（検査の名前, ページの id）の組が、expected とちょうど同じであることを確かめる。"""
        issues = self.issues(today)
        got = sorted({(i.check, i.page) for i in issues})
        self.assertEqual(got, sorted(set(expected)), "\n" + "\n".join(
            f"{i.severity} {i.file}:{i.line} {i.page} [{i.check}] {i.message}" for i in issues))
        return issues

    def severity_of(self, issues, check: str) -> set[str]:
        return {i.severity for i in issues if i.check == check}

    def run_cli(self, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = check_pages.main(["--root", str(self.root), "--today", TODAY.isoformat(), *args])
        return code, out.getvalue(), err.getvalue()


# ================================================================ 置き場所と形


class TestClean(PagesCase):
    def test_fixture_is_clean(self):
        self.assertFound()

    def test_every_check_has_a_test(self):
        names = {c.name for c in checks_for(FRONT_MATTER)}
        self.assertEqual(sorted(names - COVERED - SHARED), [])


class TestShape(PagesCase):
    @covers("YAML")
    def test_duplicate_key(self):
        self.replace(RVL, "volatility: 低\n", "volatility: 低\nvolatility: 中\n")
        issues = self.assertFound(("YAML", "request-vs-lock"))
        self.assertEqual(issues[0].line, 20)

    @covers("YAML")
    def test_broken_data_yaml(self):
        self.write("data/outdated-advice.yml", "advice: [\n")
        self.assertFound(("YAML", "-"), ("outdated_advice の id", "instructions-ignored"))

    @covers("形")
    def test_unknown_key_and_vocab(self):
        self.replace(CC, "volatility: 中\n", "volatility: 中\ncolour: blue\n")
        self.replace(HTU, "priority: 必須", "priority: 大事")
        issues = self.assertFound(("形", "completion-check"), ("形", "how-to-use"))
        msgs = {i.page: i.message for i in issues}
        self.assertIn("colour", msgs["completion-check"])
        self.assertIn("大事", msgs["how-to-use"])
        self.assertEqual({i.line for i in issues if i.page == "how-to-use"}, {7})

    @covers("形")
    def test_no_front_matter(self):
        self.write("docs/verify/plain.md", "# ただの文書\n")
        self.assertFound(("形", "plain"), ("入ってくる道", "plain"))     # 本文の検査は front matter の読めるページだけ

    @covers("形")
    def test_verified_on_draft(self):
        self.replace(II, "stage: draft\n", "stage: draft\nverified: 2026-11-01\n")
        self.assertFound(("形", "instructions-ignored"))

    @covers("id とファイル名")
    def test_id_differs_from_file(self):
        self.replace(CC, "id: completion-check", "id: completion-checks")
        self.assertFound(("id とファイル名", "completion-checks"), ("参照", "request-vs-lock"),
                         ("入ってくる道", "completion-checks"))

    @covers("分野とフォルダ")
    def test_field_differs_from_folder(self):
        self.replace(CC, "field: verify", "field: eval")
        self.assertFound(("分野とフォルダ", "completion-check"))

    @covers("置き場所")
    def test_stub_in_docs(self):
        text = self.read(HB)
        self.path(HB).unlink()
        self.write("docs/enforce/hooks-basics.md", text)
        self.assertFound(("置き場所", "hooks-basics"))

    @covers("置き場所")
    def test_draft_in_stubs_and_stray_files(self):
        self.replace(HB, "stage: stub", "stage: draft")
        self.write("docs/misc.md", "# 置き場所の違う文書\n")
        self.write("stubs/enforce/index.md", "# 分野の入口は stubs/ に置かない\n")
        issues = self.assertFound(("置き場所", "hooks-basics"), ("置き場所", "-"))
        self.assertEqual(len([i for i in issues if i.page == "-"]), 2)

    @covers("id の重複")
    def test_same_id_in_docs_and_stubs(self):
        text = self.read(CC).replace("stage: draft", "stage: stub")
        self.write("stubs/verify/completion-check.md", text)
        issues = self.assertFound(("id の重複", "completion-check"))
        self.assertIn("docs/verify/completion-check.md", issues[0].message)

    @covers("章")
    def test_chapter_must_be_in_catalog(self):
        self.write("planning/catalog/symptoms.yaml", "field: symptoms\nchapters: [別の章]\npages: []\n")
        issues = self.assertFound(("章", "instructions-ignored"))
        self.assertEqual(issues[0].severity, WARNING)
        self.write("planning/catalog/symptoms.yaml", "field: symptoms\nchapters: [指示と仕組み]\npages: []\n")
        self.assertFound()

    @covers("設定")
    def test_missing_config_files(self):
        self.path("nav.yml").unlink()
        self.path(".claude/settings.json").unlink()
        issues = self.assertFound(("設定", "-"))
        self.assertEqual(len(issues), 2)

    @covers("設定")
    def test_site_without_rule_vocab(self):
        text = self.read("schema/site.yml")
        text = re.sub(r"(?ms)^proportional_rule:.*?(?=^\S)", "", text)
        self.write("schema/site.yml", text)
        issues = self.assertFound(("設定", "-"))
        self.assertIn("proportional_rule", issues[0].message)

    @covers("平文の欄")
    def test_markup_in_plain_fields(self):
        self.replace(CC, "title: 完了を確かめる", "title: \"`done` を確かめる\"")
        issues = self.assertFound(("平文の欄", "completion-check"))
        self.assertEqual(issues[0].severity, WARNING)


# ================================================================ 本文


class TestBody(PagesCase):
    @covers("目印")
    def test_unclosed_marker(self):
        self.append(RVL, "\n<!-- gen:begin oops -->\n")
        self.assertFound(("目印", "request-vs-lock"))

    @covers("sections")
    def test_section_heading_missing_or_renamed(self):
        self.replace(RVL, "## 二つの層 {#two-layers}", "## 二つの層")
        self.assertFound(("sections", "request-vs-lock"))

    def test_renamed_heading_is_a_warning(self):
        self.replace(RVL, "## 二つの層 {#two-layers}", "## 二つの層の違い {#two-layers}")
        issues = self.assertFound(("sections", "request-vs-lock"))
        self.assertEqual(issues[0].severity, WARNING)

    @covers("見出し")
    def test_h1_and_markup_in_headings(self):
        self.append(CC, "\n# 大見出し\n\n## `done` の印 {#done-mark}\n\n## 波かっこ {x} の節\n")
        issues = self.assertFound(("見出し", "completion-check"))
        self.assertEqual(len(issues), 3)

    @covers("要点")
    def test_abstract_missing(self):
        self.replace(CC, '!!! abstract "要点"', '!!! note "メモ"')
        self.assertFound(("要点", "completion-check"))

    def test_intro_missing_is_a_warning(self):
        self.replace(CC, "完了を確かめるのは、試験用の導入である。\n", "")
        issues = self.assertFound(("要点", "completion-check"))
        self.assertEqual(issues[0].severity, WARNING)

    @covers("要点の前提")
    def test_prerequisite_item_must_match(self):
        self.replace(II, "- **前提**：<!-- link:begin request-vs-lock --><!-- link:end -->", "- **前提**：なし")
        self.replace(RVL, "- **前提**：なし", "- **前提**：<!-- link:begin how-to-use --><!-- link:end -->")
        self.assertFound(("要点の前提", "instructions-ignored"), ("要点の前提", "request-vs-lock"))

    def test_prerequisite_item_missing(self):
        self.replace(CC, "    - **前提**：<!-- link:begin request-vs-lock --><!-- link:end -->\n", "")
        self.assertFound(("要点の前提", "completion-check"))

    def test_prerequisite_extra_and_continuation(self):
        self.replace(II, "- **前提**：<!-- link:begin request-vs-lock --><!-- link:end -->",
                     "- **前提**：<!-- link:begin request-vs-lock --><!-- link:end -->\n"
                     "      と <!-- link:begin how-to-use --><!-- link:end -->")
        issues = self.assertFound(("要点の前提", "instructions-ignored"))
        self.assertIn("how-to-use", issues[0].message)

    @covers("別名の行")
    def test_aliases_line(self):
        self.replace(RVL, "<!-- textlint-disable -->\n", "")
        self.replace(RVL, "別名：試験用の別名・もう一つの別名", "別名：試験用の別名")
        issues = self.assertFound(("別名の行", "request-vs-lock"))
        self.assertEqual(len(issues), 2)                 # 囲みの印がない・名前が欠けている

    def test_aliases_order_is_a_warning(self):
        self.replace(RVL, "別名：試験用の別名・もう一つの別名", "別名：もう一つの別名・試験用の別名")
        issues = self.assertFound(("別名の行", "request-vs-lock"))
        self.assertEqual(issues[0].severity, WARNING)

    def test_aliases_without_line(self):
        self.replace(HTU, "summary: 試験用の要約。三つの入口から引く。", "summary: 試験用の要約。三つの入口から引く。\naliases: [引き方]")
        self.assertFound(("別名の行", "how-to-use"))

    @covers("未公開のページへのリンク")
    def test_handwritten_links_to_unpublished_pages(self):
        self.append(HTU, "\n[フック](../enforce/hooks-basics.md)・[完了](../verify/completion-check.md#steps)・"
                         "[ない](../x/none.md)・[よい](../basics/request-vs-lock.md)・![図](../img/a.svg)\n"
                         "\n`[コード](../enforce/hooks-basics.md)` と <!-- [注釈](../enforce/hooks-basics.md) -->\n"
                         "\n[参照の形]: ../enforce/hooks-basics.md\n")
        self.append("docs/index.md", "\n[試作](verify/completion-check.md)\n")
        issues = self.assertFound(("未公開のページへのリンク", "how-to-use"), ("未公開のページへのリンク", "-"))
        msgs = sorted(i.message for i in issues if i.page == "how-to-use")
        self.assertEqual(len(msgs), 4)
        self.assertTrue(any("骨格のページ hooks-basics" in m for m in msgs))
        self.assertTrue(any("exclude_docs" in m for m in msgs))
        self.assertTrue(any("先のページがない" in m for m in msgs))

    def test_links_inside_markers_are_left_to_the_generator(self):
        self.append(HTU, "\n<!-- gen:begin x -->\n[フック](../enforce/hooks-basics.md)\n<!-- gen:end x -->\n")
        self.assertFound()

    def test_site_url_links(self):
        self.write("mkdocs.yml", "site_name: x\nsite_url: https://example.github.io/atlas/\n")
        self.append(HTU, "\n[フック](https://example.github.io/atlas/enforce/hooks-basics/)\n")
        self.assertFound(("未公開のページへのリンク", "how-to-use"))

    @covers("タブの面")
    def test_surface_tabs(self):
        self.replace(RVL, '=== "アプリ"', '=== "API"')
        issues = self.assertFound(("タブの面", "request-vs-lock"))
        self.assertEqual(len(issues), 2)                 # surfaces にない面・並び（API → Claude Code）
        self.replace(RVL, '=== "API"', '=== "その他"')
        issues = self.assertFound(("タブの面", "request-vs-lock"))
        self.assertEqual(self.severity_of(issues, "タブの面"), {WARNING})

    def test_surface_tabs_need_labels(self):
        self.replace("nav.yml", "    surfaces: {app: アプリ, claude-code: Claude Code, api: API}\n", "    other: 1\n")
        issues = self.assertFound(("タブの面", "-"))
        self.assertEqual(issues[0].severity, WARNING)

    @covers("link の目印")
    def test_link_markers(self):
        self.append(HTU, "\n<!-- link:begin no-page --><!-- link:end --> と "
                         "<!-- link:begin hooks-basics#nope --><!-- link:end -->\n")
        issues = self.assertFound(("link の目印", "how-to-use"))
        self.assertEqual(len(issues), 2)

    @covers("ナビゲーション")
    def test_nav_and_exclude_docs(self):
        self.replace("nav.yml", "  - basics/request-vs-lock.md\n", "  - basics/request-vs-lock.md\n  - verify/completion-check.md\n")
        self.replace("nav.yml", "  /verify/completion-check.md\n", "  /verify/completion-check.md\n  /index.md\n  /old/gone.md\n")
        issues = self.assertFound(("ナビゲーション", "-"))
        self.assertEqual(self.severity_of(issues, "ナビゲーション"), {ERROR, WARNING})
        # nav にある外したページ（verify/completion-check.md と index.md）・ページでないファイル・当たらないパターン
        self.assertEqual(len(issues), 4)


# ================================================================ 数値と出典


class TestData(PagesCase):
    @covers("data の形")
    def test_data_schema(self):
        self.replace("data/facts.yml", "    volatility: 中\n    status: 確認済み\n  - id: sample-default-effort",
                     "    volatility: 中\n  - id: sample-default-effort")
        self.write("data/sources.d/how-to-use.yml", "- not a mapping\n")
        issues = self.assertFound(("data の形", "sample-limit"), ("data の形", "-"))
        self.assertTrue(any(i.file == "data/sources.d/how-to-use.yml" and "how-to-use" in i.pages for i in issues))

    @covers("data の id の重複", "出典の URL の重なり")
    def test_duplicate_source(self):
        self.append("data/sources.d/instructions-ignored.yml",
                    "  - id: sample-doc\n    url: https://EXAMPLE.com/docs/limit/\n    title: 同じ\n    kind: 公式文書\n"
                    "    publisher: 試験\n    lang: ja\n    checked: 2026-11-02\n")
        self.assertFound(("data の id の重複", "sample-doc"), ("出典の URL の重なり", "sample-doc"))

    @covers("facts の id")
    def test_fact_marker_ids(self):
        self.append(RVL, "\n値は <!-- fact:begin no-fact --><!-- fact:end --> である。\n")
        self.append(HB, "\n<!-- fact:begin no-fact-2 --><!-- fact:end -->\n")
        issues = self.assertFound(("facts の id", "request-vs-lock"), ("facts の id", "hooks-basics"))
        sev = {i.page: i.severity for i in issues}
        self.assertEqual(sev, {"request-vs-lock": ERROR, "hooks-basics": WARNING})

    @covers("tracks の id")
    def test_track_ids(self):
        self.replace(HB, "tracks: [sample-hooks]", "tracks: [no-feature]")
        self.replace(CC, "sources: []", "sources: []\ntracks: [no-feature-2]")
        issues = self.assertFound(("tracks の id", "hooks-basics"), ("tracks の id", "completion-check"))
        sev = {i.page: i.severity for i in issues if i.check == "tracks の id"}
        self.assertEqual(sev, {"hooks-basics": WARNING, "completion-check": ERROR})

    @covers("outdated_advice の id")
    def test_advice_ids(self):
        self.replace(II, "outdated_advice: [sample-caps]", "outdated_advice: [sample-caps, no-advice]")
        self.assertFound(("outdated_advice の id", "instructions-ignored"))

    @covers("sources の id")
    def test_source_ids(self):
        self.replace(RVL, "sources: [sample-doc]", "sources: [sample-doc, no-source]")
        self.replace("data/outdated-advice.yml", "    sources: [sample-doc]\n    checked: 2026-10-28",
                     "    sources: [sample-doc, gone]\n    checked: 2026-10-28")
        self.assertFound(("sources の id", "request-vs-lock"), ("sources の id", "sample-caps"))

    @covers("data の参照")
    def test_data_refs(self):
        self.replace("data/facts.yml", "    page: hooks-basics", "    page: no-page")
        self.replace("data/facts.yml", "    feature: sample-hooks", "    feature: no-feature")
        self.replace("data/outdated-advice.yml", "    name: sample-rename", "    name: no-name")
        self.write("data/sources.d/no-such-page.yml", "sources: []\n")
        issues = self.assertFound(("data の参照", "sample-hooks"), ("data の参照", "sample-rename"),
                                  ("data の参照", "sample-renamed"), ("data の参照", "-"))
        self.assertEqual(len(issues), 4)

    @covers("AI の利用の指定")
    def test_noai_designation(self):
        self.append("data/sources.d/instructions-ignored.yml",
                    "  - id: sample-unknown\n    url: https://example.edu/a\n    title: a\n    kind: 研究\n"
                    "    publisher: a\n    lang: en\n    checked: 2026-11-02\n"
                    "  - id: sample-refused\n    url: https://www.example.org/b\n    title: b\n    kind: 研究\n"
                    "    publisher: b\n    lang: en\n    checked: 2026-11-02\n"
                    "  - id: sample-unchecked\n    url: https://example.info/c\n    title: c\n    kind: 研究\n"
                    "    publisher: c\n    lang: en\n    checked: 2026-11-02\n")
        self.replace("data/sources.d/instructions-ignored.yml", "domains:\n",
                     "domains:\n  - {domain: example.info, checked: 2026-11-02, noai: null}\n")
        issues = self.assertFound(("AI の利用の指定", "sample-unknown"), ("AI の利用の指定", "sample-refused"),
                                  ("AI の利用の指定", "sample-unchecked"))
        sev = {i.page: i.severity for i in issues}
        self.assertEqual(sev, {"sample-unknown": ERROR, "sample-refused": ERROR, "sample-unchecked": WARNING})

    @covers("断るドメインと deny")
    def test_noai_domains_in_deny(self):
        self.replace(".claude/settings.json", '      "WebFetch(domain:*.example.org)",\n', "")
        self.write("tools/check_noai.py", 'KNOWN_NOAI = {"atcoder.jp": "x", "example.org": "y"}\n')
        self.write(".github/workflows/links.yml",
                   "jobs:\n  lychee:\n    steps:\n      - with:\n          args: >-\n"
                   "            --exclude '(?i)^https?://([a-z0-9-]+\\.)*atcoder\\.jp([:/?#]|$)'\n")
        issues = self.assertFound(("断るドメインと deny", "-"))
        by_file = {i.file: i.severity for i in issues}
        self.assertEqual(by_file, {"data/sources.yml": ERROR, ".github/workflows/links.yml": WARNING})
        self.write("tools/check_noai.py", 'KNOWN_NOAI = {"example.org": "y"}\n')
        issues = self.assertFound(("断るドメインと deny", "-"))
        self.assertIn("tools/check_noai.py", {i.file for i in issues})


# ================================================================ 鮮度


class TestFreshness(PagesCase):
    @covers("確認日")
    def test_expired_page(self):
        issues = self.assertFound(("確認日", "request-vs-lock"), today=datetime.date(2027, 2, 1))
        self.assertIn("2027-01-13", issues[0].message)
        self.assertIn("sample-limit", issues[0].message)
        self.assertEqual(issues[0].severity, WARNING)
        self.assertFound(today=datetime.date(2027, 1, 13))        # 期限の日の当日は過ぎていない

    def test_tracks_without_version(self):
        self.replace(RVL, "verified_with: {claude_code: 2.1.317, channel: latest, models: [claude-opus-5-5]}",
                     "verified_with: {models: [claude-opus-5-5]}\ntracks: [sample-hooks]")
        self.assertFound(("確認日", "request-vs-lock"))

    @covers("目印の外の数値")
    def test_values_outside_markers(self):
        self.append(RVL, "\n上限は １００回 で、1,000 回ではない。値 `100 回` はコードの中。\n")
        self.replace(HTU, "summary: 試験用の要約。三つの入口から引く。", "summary: 試験用の要約。100 回まで引ける。")
        issues = self.assertFound(("目印の外の数値", "request-vs-lock"), ("目印の外の数値", "how-to-use"))
        self.assertEqual(len(issues), 2)
        self.assertEqual(self.severity_of(issues, "目印の外の数値"), {WARNING})

    def test_patterns_before_after(self):
        self.replace("data/facts.yml", "    match: {units: [回]}", "    match: {before: [上限は], pattern: '{value} 件'}")
        self.append(CC, "\n上限は 100 で、100 件まで。上限 100 回。\n")
        issues = self.assertFound(("目印の外の数値", "completion-check"))
        self.assertEqual(len(issues), 1)                          # 同じ行は1件


# ================================================================ 入口


class TestCli(PagesCase):
    def test_exit_codes_and_format(self):
        code, out, _ = self.run_cli()
        self.assertEqual(code, 0)
        self.assertIn("エラー 0 件、警告 0 件", out)
        self.append(HTU, "\n[フック](../enforce/hooks-basics.md)\n")
        self.replace(CC, "title: 完了を確かめる", "title: \"`x`\"")
        code, out, _ = self.run_cli()
        self.assertEqual(code, 1)
        lines = out.strip().splitlines()
        for line in lines[:-1]:
            self.assertRegex(line, LINE_RE)
        self.assertIn("エラー 1 件（未公開のページへのリンク 1）、警告 1 件（平文の欄 1）", lines[-1])
        code, out, _ = self.run_cli("-q")
        self.assertNotIn("警告: ", out)

    def test_page_filter(self):
        self.append(HTU, "\n[フック](../enforce/hooks-basics.md)\n")
        self.replace(CC, "title: 完了を確かめる", "title: \"`x`\"")
        code, out, _ = self.run_cli("--page", "completion-check")
        self.assertEqual(code, 0)
        self.assertIn("completion-check に関わる指摘", out)
        self.assertNotIn("how-to-use", out.replace("completion-check に関わる指摘", ""))
        code, out, _ = self.run_cli("--page", "hooks-basics,how-to-use")   # リンクの先のページにも出る
        self.assertEqual(code, 1)
        code, _, err = self.run_cli("--page", "no-such-page")
        self.assertEqual(code, 2)
        self.assertIn("no-such-page", err)

    def test_list_and_cannot_check(self):
        code, out, _ = self.run_cli("--list")
        self.assertEqual(code, 0)
        for c in checks_for(FRONT_MATTER):
            self.assertIn(f"[{c.name}]", out)
        (self.root / "schema" / "site.yml").unlink()
        code, _, err = self.run_cli()
        self.assertEqual(code, 2)
        self.assertIn("検査できない", err)

    def test_catalog_mode(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = check_pages.main(["--root", str(SMALL), "--catalog"])
        self.assertEqual(code, 0, out.getvalue())
        self.assertIn("目次のページ", out.getvalue())

    def test_script_runs(self):
        r = subprocess.run([sys.executable, str(REPO / "tools" / "check_pages.py"), "--root", str(self.root),
                            "--today", TODAY.isoformat()], capture_output=True, text=True, timeout=120)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_real_repository(self):
        # 本物のリポジトリ（中身は工程とともに変わるので、検査できることだけを見る）と、本物の目次
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertIn(check_pages.main([]), (0, 1))
            self.assertEqual(check_pages.main(["--catalog", "-q"]), 0)


class TestIgnorePatterns(unittest.TestCase):
    def test_gitignore_like_patterns(self):
        rules = parse_ignore(["/verify/a.md", "drafts/", "*.tmp", "!keep.tmp", "start/**/x.md", "# 注釈", ""])
        cases = {"verify/a.md": True, "x/verify/a.md": False, "drafts/b.md": True, "a/drafts/c.md": True,
                 "drafts": False, "z.tmp": True, "d/z.tmp": True, "keep.tmp": False, "start/x.md": True,
                 "start/a/b/x.md": True, "start/y.md": False, "verify/b.md": False}
        for path, want in cases.items():
            self.assertEqual(ignored(rules, path), want, path)


if __name__ == "__main__":
    unittest.main()
