"""台帳の生成（tools/gen/ledger.py）の試験：一覧表（ledger-index）・行の見出しの下の1行・時期の注・原理の欄の見出し・同じ話題の行。
`uv run python -m unittest discover -s tests/tools` で動く。置き場所は fixtures/gen（gen_helpers.py）。
"""
from __future__ import annotations

import unittest

from gen_helpers import GenCase, block_content

PAGE = "docs/changes/outdated-advice-ledger.md"

ADVICE = """advice:
  - id: sample-caps
    title: 大文字で強調すれば守られる
    now: 守らせたい規則はフックに移す
    changed: {date: 2026-03, until: 2026-05, label: "始まり：改稿の日。終わり：廃止の日"}
    status: 置換
    surfaces: [claude-code, api]
    principle: [縛る]
    see_also: [sample-renamed, sample-missing]
    sources: [sample-doc]
    checked: 2026-10-01
  - id: sample-renamed
    title: 古いフック | で止める
    now: フックで止める
    name: sample-rename
    status: 撤回
    surfaces: [app]
    principle: [縛る]
    see_also: [sample-caps]
    sources: [sample-blog]
    checked: 2026-10-01
  - id: sample-screen
    title: 画面の名前
    now: 新しい画面を使う
    changed: {date: 2026-04}
    status: 置換
    surfaces: [app]
    principle: [見せる]
    principle_kind: feature
    sources: [sample-blog]
    checked: 2026-10-01
"""


class TestLedger(GenCase):
    def setUp(self):
        super().setUp()
        self.write("data/outdated-advice.yml", ADVICE)
        text = self.read(PAGE).replace("<!-- gen:begin ledger -->",
                                       "<!-- gen:begin ledger-index -->\n<!-- gen:end ledger-index -->\n\n<!-- gen:begin ledger -->")
        self.write(PAGE, text)
        self.generate()
        self.page = self.read(PAGE)

    def test_index_table(self):
        rows = [x for x in block_content(self.page, "ledger-index").split("\n") if x.startswith("|")]
        self.assertEqual(rows[0], "| 古い助言 | 状態 | 変わった時期 | 面 |")
        self.assertEqual(rows[2], "| [大文字で強調すれば守られる](#sample-caps) | 置換 | 2026-03〜2026-05 | Claude Code・API |")
        self.assertIn("| [古いフック \\| で止める](#sample-renamed) | 撤回 | 2026-10 ごろ・Claude Code 2.1.300 | アプリ |", rows)
        self.assertEqual(len(rows), 5)

    def test_row_under_heading_says_it_is_stale(self):
        ledger = block_content(self.page, "ledger")
        self.assertIn("### 大文字で強調すれば守られる {#sample-caps}\n\n古い助言（状態：置換）\n\n- **今どうするか**", ledger)
        self.assertIn("### 古いフック | で止める {#sample-renamed}\n\n古い助言（状態：撤回）", ledger)

    def test_label_follows_the_period(self):
        ledger = block_content(self.page, "ledger")
        self.assertIn("- **変わった時期**：2026-03〜2026-05（始まり：改稿の日。終わり：廃止の日）", ledger)
        self.assertIn("- **変わった時期**：2026-04\n", ledger)      # label がなければ付かない

    def test_principle_heading_for_renamed_and_feature_rows(self):
        ledger = block_content(self.page, "ledger")
        self.assertEqual(ledger.count("- **どの原理の回避策だったか**：縛る"), 1)      # sample-caps だけ
        self.assertEqual(ledger.count("- **この機能が受け持つ原理**："), 2)            # name の行と principle_kind: feature の行
        self.assertIn("- **この機能が受け持つ原理**：見せる", ledger)

    def test_see_also_links_and_missing_target(self):
        ledger = block_content(self.page, "ledger")
        self.assertIn("- **同じ話題の行**：[古いフック | で止める](#sample-renamed)\n", ledger)
        self.assertIn("- **同じ話題の行**：[大文字で強調すれば守られる](#sample-caps)\n", ledger)
        code, out, err = self.cli("--check")
        self.assertIn("sample-missing", out + err)

    def test_timeline_keeps_the_short_period(self):
        timeline = block_content(self.read("docs/changes/change-timeline-2026.md"), "timeline")
        self.assertNotIn("始まり：", timeline)


class TestRenameWithoutDate(GenCase):
    """names の changed.date を省いた項目（改名の時期が分からない）。"""
    NAME = ("  - id: sample-undated\n    current: 新しい学習所\n    old: [古い学習所]\n"
            "    changed: {note: 改名の時期は不明}\n    sources: [sample-blog]\n    checked: 2026-11-05\n    status: 確認済み\n")

    def setUp(self):
        super().setUp()
        text = self.read("data/facts.yml")
        self.write("data/facts.yml", text.replace("\nnames:\n", "\nnames:\n" + self.NAME, 1))
        self.generate()

    def test_the_old_name_list_says_the_period_is_unknown(self):
        old = block_content(self.read("docs/start/term-index.md"), "terms old")
        self.assertIn("- 古い学習所 → 新しい学習所（不明）\n", old)
        self.assertIn("- 古いフック → フック（2026-10 ごろ・Claude Code 2.1.300）", old)     # 時期のある名前はそのまま

    def test_the_timeline_leaves_it_out(self):
        timeline = block_content(self.read("docs/changes/change-timeline-2026.md"), "timeline")
        self.assertNotIn("古い学習所", timeline)
        self.assertIn("古いフック", timeline)


if __name__ == "__main__":
    unittest.main()
