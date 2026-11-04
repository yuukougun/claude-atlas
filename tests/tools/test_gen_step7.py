"""工程7の道具の直し（planning/batches/step7/decisions-main.md の「道具」の表）の試験。

compare の列の指定・共通の列・条件による（#22）、fact-table の行ごとの出典（#28）、雛形の open と min_version_fact（#34）、
link の目印で分野の入口を指す（#43a）、routes のセルの改行（#45。test_gen_site.py）、検査の側（#26・#28）、
text・markdown の折り返しの CSS（#41a）。GenCase（一時フォルダに fixtures/gen を写す）と、check_pages の PagesCase を使う。
"""
from __future__ import annotations

import sys
import unittest

from gen_helpers import REPO, GenCase, block_content

sys.path.insert(0, str(REPO / "tools"))

from checks import ERROR  # noqa: E402
from test_check_pages import II, RVL, PagesCase  # noqa: E402

HVS = "docs/extend/hook-vs-skill.md"
TWO = "tracks: [sample-hooks, sample-skills, sample-beta, missing-feature]"


def compare_with(case: GenCase, args: str, tracks: str = "tracks: [sample-hooks, sample-skills]") -> str:
    case.replace(HVS, TWO, tracks)
    name = "compare" + (" " + args if args else "")
    case.replace(HVS, "<!-- gen:begin compare -->\n<!-- gen:end compare -->", f"<!-- gen:begin {name} -->\n<!-- gen:end {name} -->")
    case.generate()
    return block_content(case.read(HVS), name)


class TestCompareColumns(GenCase):
    def test_columns_by_label_by_id_and_checked(self):
        block = compare_with(self, "強制力 survives_compaction 確認日")
        self.assertIn("| 機能 | 強制力 | 圧縮で残るか | 確認日 |", block)
        self.assertIn("| [フック](../enforce/hooks-basics.md) | 鍵 | 残る | 2026-10-12 |", block)
        self.assertIn("| スキル（準備中） | お願い | 残らない | 2026-10-05 |", block)
        self.assertNotIn("成熟度", block)
        self.assertNotIn("すべて共通", block)

    def test_default_columns_omit_same_value_columns(self):
        block = compare_with(self, "")
        self.assertIn("| 機能 | 面 | 強制力 | 圧縮で残るか | 入った版 | 確認日 |", block)    # 成熟度（GA）は全行が同じ
        self.assertNotIn("| 成熟度 |", block)
        self.assertIn("\n\nすべて共通：成熟度 GA。\n", block)

    def test_specified_common_column_goes_to_the_line_below(self):
        block = compare_with(self, "成熟度 強制力")
        self.assertIn("| 機能 | 強制力 |", block)
        self.assertIn("すべて共通：成熟度 GA。", block)

    def test_all_common_columns_stay_in_the_table(self):
        block = compare_with(self, "成熟度")
        self.assertIn("| 機能 | 成熟度 |", block)
        self.assertNotIn("すべて共通", block)

    def test_one_row_has_no_common_line(self):
        block = compare_with(self, "", tracks="tracks: [sample-hooks]")
        self.assertIn("成熟度", block)
        self.assertNotIn("すべて共通", block)

    def test_unknown_column_is_noted(self):
        self.replace(HVS, TWO, "tracks: [sample-hooks, sample-skills]")
        self.replace(HVS, "<!-- gen:begin compare -->\n<!-- gen:end compare -->",
                     "<!-- gen:begin compare 強制力 ない列 -->\n<!-- gen:end compare 強制力 ない列 -->")
        out = self.generate()
        self.assertIn("比較の表の列「ない列」は機能の属性でも確認日でもない", out)
        self.assertIn("| 機能 | 強制力 |", block_content(self.read(HVS), "compare 強制力 ない列"))

    def test_null_is_unchecked_and_conditional_is_split(self):
        self.replace("data/facts.yml", "    survives_compaction: false\n",
                     "    survives_compaction: null\n    conditional: [survives_compaction]\n")
        self.replace("data/facts.yml", "    survives_compaction: true\n    since: {claude_code: 2.1.0, date: 2026-01}",
                     "    survives_compaction: null\n    since: {claude_code: 2.1.0, date: 2026-01}")
        block = compare_with(self, "強制力 圧縮で残るか")
        self.assertIn("| [フック](../enforce/hooks-basics.md) | 鍵 | 未確認 |", block)     # 書かない null は「確かめていない」
        self.assertIn("| スキル（準備中） | お願い | 条件による |", block)                # conditional に挙げた null
        feature = self.read("docs/enforce/hooks-basics.md")
        self.assertNotIn("条件による", feature)

    def test_conditional_attribute_only_column_is_shown_by_default(self):
        self.replace("data/facts.yml", "    survives_compaction: false\n",
                     "    survives_compaction: null\n    conditional: [survives_compaction]\n")
        self.replace("data/facts.yml", "    survives_compaction: true\n    since: {claude_code: 2.1.0, date: 2026-01}",
                     "    survives_compaction: null\n    since: {claude_code: 2.1.0, date: 2026-01}")
        block = compare_with(self, "")
        self.assertIn("圧縮で残るか", block)
        self.assertIn("条件による", block)


class TestFactTableRowSources(GenCase):
    def test_cell_sources_are_listed_per_row(self):
        self.replace("data/facts.yml", "app: {value: null, note: 値を書いた文書がない}}",
                     "app: {value: null, note: 値を書いた文書がない, sources: [sample-blog]}}")
        self.replace("data/facts.yml", "claude-code: medium, app: low}",
                     "claude-code: {value: medium, sources: [sample-blog]}, app: {value: low, sources: [sample-blog]}}")
        self.generate()
        table = block_content(self.read(HVS), "fact-table sample-effort")
        blog = "[Sample blog post \\[draft\\]](https://blog.example.org/post)"
        self.assertIn("出典（行ごと）：\n\n- model-a：" + blog, table)
        self.assertIn("- model-b：" + blog, table)
        self.assertNotIn("\n出典：", table)
        self.assertNotIn("。出典：", table)                     # 表の下の1段落にまとめない
        self.assertIn("そのほかの出典：[", table)                # 行に出なかった sample-doc
        self.assertIn("確認日 2026-10-10。食い違い：low", table)

    def test_different_sources_in_a_row_name_the_column(self):
        self.replace("data/facts.yml", "api: high, claude-code: medium, app: {value: null, note: 値を書いた文書がない}}",
                     "api: {value: high, sources: [sample-doc]}, claude-code: {value: medium, sources: [sample-blog]}, "
                     "app: {value: null, note: 値を書いた文書がない}}")
        self.generate()
        table = block_content(self.read(HVS), "fact-table sample-effort")
        self.assertRegex(table, r"- model-a：API \[[^\n]*\]\(https://docs\.example\.com[^\n]*\)；Claude Code \[Sample blog")

    def test_no_cell_sources_keeps_one_line(self):
        self.generate()
        table = block_content(self.read(HVS), "fact-table sample-effort")
        self.assertIn("。出典：[", table)
        self.assertNotIn("行ごと", table)


class TestSnippetOpenAndMinVersionFact(GenCase):
    PATH = "snippets/hooks-basics/block-rm.expect.yaml"
    PAGE = "docs/enforce/hooks-basics.md"
    FACT = ("  - {id: min-ver, title: 試験用の最低の版, value: 2.1.99, sources: [sample-doc], checked: 2026-10-01,"
            " status: 確認済み}\nfeatures:\n")

    def snippet(self) -> str:
        self.generate()
        return block_content(self.read(self.PAGE), "snippet hooks-basics/block-rm")

    def test_default_is_closed(self):
        self.assertIn('\n??? example "雛形：危ない削除を止める"\n', self.snippet())

    def test_open_true_opens_the_fold(self):
        self.replace(self.PATH, "place: project\n", "place: project\nopen: true\n")
        snip = self.snippet()
        self.assertIn('\n???+ example "雛形：危ない削除を止める"\n', snip)
        self.assertNotIn('\n??? example', snip)

    def test_open_false_stays_closed(self):
        self.replace(self.PATH, "place: project\n", "place: project\nopen: false\n")
        self.assertIn('\n??? example "雛形：', self.snippet())

    def test_min_version_fact_beats_feature_since(self):
        self.replace("data/facts.yml", "features:\n", self.FACT)
        self.replace(self.PATH, "place: project\n", "place: project\nmin_version_fact: min-ver\n")
        snip = self.snippet()
        self.assertIn("要る最低の版：Claude Code 2.1.99。", snip)
        self.assertNotIn("2.1.50", snip)

    def test_unknown_or_unchecked_fact_falls_back_to_features(self):
        self.replace(self.PATH, "place: project\n", "place: project\nmin_version_fact: no-such-fact\n")
        out = self.generate()
        self.assertIn("min_version_fact「no-such-fact」が data/facts.yml の facts にない", out)
        self.assertIn("要る最低の版：Claude Code 2.1.50。", block_content(self.read(self.PAGE), "snippet hooks-basics/block-rm"))
        self.replace("data/facts.yml", "features:\n", self.FACT.replace("status: 確認済み", "status: 未確認"))
        self.replace(self.PATH, "no-such-fact", "min-ver")
        out = self.generate()
        self.assertIn("要る最低の版：Claude Code 2.1.50。", block_content(self.read(self.PAGE), "snippet hooks-basics/block-rm"))
        self.assertIn("min_version_fact「min-ver」は確認済みでない", out)


class TestFieldLink(GenCase):
    def add(self, text: str) -> None:
        self.replace(HVS, "## 比較の表 {#table}", text + "\n\n## 比較の表 {#table}")

    def test_field_link_shows_the_field_name(self):
        self.add("入口は <!-- link:begin field:extend --><!-- link:end --> から。")
        self.generate()
        self.assertIn("<!-- link:begin field:extend -->[使い分け・仕組み](index.md)<!-- link:end -->".replace("使い分け・仕組み", self.field_name()),
                      self.read(HVS))

    def field_name(self) -> str:
        import yaml
        site = yaml.safe_load((self.root / "schema" / "site.yml").read_text(encoding="utf-8"))
        return next(f["title"] for f in site["fields"] if f["id"] == "extend")

    def test_field_in_another_folder_has_a_relative_path(self):
        self.replace("docs/symptoms/instructions-ignored.md", "## ", "<!-- link:begin field:extend --><!-- link:end -->\n\n## ")
        self.generate()
        self.assertIn(f"[{self.field_name()}](../extend/index.md)", self.read("docs/symptoms/instructions-ignored.md"))

    def test_unknown_field_is_noted_and_left_as_text(self):
        self.add("<!-- link:begin field:no-such --><!-- link:end -->")
        out = self.generate()
        self.assertIn("<!-- link:begin field:no-such -->field:no-such<!-- link:end -->", self.read(HVS))
        self.assertIn("「field:no-such」の分野が schema/site.yml の fields にない", out)


class TestChecks(PagesCase):
    def test_link_to_ledger_row_id_passes_when_the_row_exists(self):
        self.append(RVL, "\n<!-- gen:begin ledger -->\n<!-- gen:end ledger -->\n")
        self.append(II, "\n<!-- link:begin request-vs-lock#sample-caps --><!-- link:end -->\n")
        self.assertFalse([i for i in self.issues() if i.check == "link の目印"])

    def test_link_to_unknown_ledger_row_id_is_still_an_error(self):
        self.append(RVL, "\n<!-- gen:begin ledger -->\n<!-- gen:end ledger -->\n")
        self.append(II, "\n<!-- link:begin request-vs-lock#no-such-row --><!-- link:end -->\n")
        self.assertTrue([i for i in self.issues() if i.check == "link の目印" and "no-such-row" in i.message])

    def test_ledger_row_id_is_not_allowed_on_a_page_without_the_ledger(self):
        self.append(II, "\n<!-- link:begin request-vs-lock#sample-caps --><!-- link:end -->\n")
        self.assertTrue([i for i in self.issues() if i.check == "link の目印"])

    def test_field_link_marker(self):
        self.append(RVL, "\n<!-- link:begin field:symptoms --><!-- link:end -->\n")
        self.assertFalse([i for i in self.issues() if i.check == "link の目印"])
        self.append(RVL, "\n<!-- link:begin field:no-such --><!-- link:end -->\n")
        found = [i for i in self.issues() if i.check == "link の目印"]
        self.assertEqual(len(found), 1)
        self.assertIn("no-such", found[0].message)

    def test_unregistered_fact_table_id_is_an_error(self):
        self.append(RVL, "\n<!-- gen:begin fact-table no-such-table -->\n<!-- gen:end fact-table no-such-table -->\n")
        found = [i for i in self.issues() if i.check == "facts の id"]
        self.assertEqual(len(found), 1)
        self.assertIn("fact-table の目印の「no-such-table」", found[0].message)
        self.assertEqual(found[0].severity, ERROR)

    def test_registered_fact_table_id_passes(self):
        fid = next(iter(self._fact_ids()))
        self.append(RVL, f"\n<!-- gen:begin fact-table {fid} -->\n<!-- gen:end fact-table {fid} -->\n")
        self.assertFalse([i for i in self.issues() if i.check == "facts の id"])

    def _fact_ids(self):
        import yaml
        return [f["id"] for f in yaml.safe_load(self.read("data/facts.yml"))["facts"]]


class TestCss(unittest.TestCase):
    def test_text_and_markdown_blocks_wrap(self):
        css = (REPO / "overrides" / "assets" / "css" / "ca.css").read_text(encoding="utf-8")
        for lang in ("text", "markdown"):
            self.assertIn(f".highlight.language-{lang} pre", css)
        self.assertIn("white-space: pre-wrap", css)
        self.assertNotIn("language-bash", css)                  # プログラムのコードは横に送ったまま


if __name__ == "__main__":
    unittest.main()
