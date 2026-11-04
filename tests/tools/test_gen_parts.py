"""作る層の部品の試験：文字の部品（tools/gen/text.py）・かなの分け方・時期の書き方と、目印の端の場合（知らない名前・
閉じていない目印・置き方の誤り・入れ子・ない id・ない anchor・字下げ）。`uv run python -m unittest discover -s tests/tools`。
"""
from __future__ import annotations

import json
import unittest

import yaml

from gen_helpers import GenCase, block_content
from gen.terms import KANA_ROWS, kana_key, period_text, term_class
from gen.text import first_sentence, json_document, md_text, rel_md, url_prefix, yaml_scalar

PAGE = "docs/enforce/hooks-basics.md"


class TestText(unittest.TestCase):
    def test_md_text(self):
        self.assertEqual(md_text("a*b_[c]`d`{e}"), r"a\*b\_\[c\]\`d\`\{e\}")
        self.assertEqual(md_text("<x> & y"), "&lt;x&gt; & y")
        self.assertEqual(md_text("a|b"), "a|b")
        self.assertEqual(md_text("a|b", table=True), r"a\|b")
        self.assertEqual(md_text("一行目\n  二行目"), "一行目 二行目")
        self.assertEqual(md_text(42), "42")

    def test_first_sentence(self):
        self.assertEqual(first_sentence("一文目（かっこ。の中）。二文目。"), "一文目（かっこ。の中）。")
        self.assertEqual(first_sentence("「引用。」の後。次。"), "「引用。」の後。")
        self.assertEqual(first_sentence("句点がない"), "句点がない")
        self.assertEqual(first_sentence(""), "")

    def test_rel_md_and_url_prefix(self):
        self.assertEqual(rel_md("symptoms/a.md", "enforce/b.md"), "../enforce/b.md")
        self.assertEqual(rel_md("symptoms/a.md", "symptoms/c.md"), "c.md")
        self.assertEqual(rel_md("index.md", "start/how-to-use.md"), "start/how-to-use.md")
        self.assertEqual(rel_md("lists/by-level.md", "basics/x.md"), "../basics/x.md")
        self.assertEqual(rel_md("start/index.md", "start/x.md"), "x.md")
        self.assertEqual(url_prefix("start/knowledge-map/"), "../../")
        self.assertEqual(url_prefix(""), "")

    def test_yaml_scalar(self):
        for s in ["入口と地図", "Claude Code", "使う"]:
            self.assertEqual(yaml_scalar(s), s)
        for s in ["yes", "2026", "a: b", "# x", " x", "null", "[x]"]:
            q = yaml_scalar(s)
            self.assertNotEqual(q, s)
            self.assertEqual(yaml.safe_load(f"k: {q}"), {"k": s})

    def test_json_document(self):
        text = json_document({"a": 1, "b": ["x"]}, {"rows": [{"id": "p"}, {"id": "q"}], "none": []})
        self.assertEqual(json.loads(text), {"a": 1, "b": ["x"], "rows": [{"id": "p"}, {"id": "q"}], "none": []})
        self.assertIn('\n{"id":"p"},\n{"id":"q"}\n', text)
        self.assertTrue(text.endswith("}\n"))


class TestKanaAndPeriods(unittest.TestCase):
    def test_kana_key_and_class(self):
        self.assertEqual(kana_key("フック"), "ふっく")
        self.assertEqual(kana_key("ルーター"), "るた")
        self.assertEqual(term_class("フック"), "kana")
        self.assertEqual(term_class("ﾌｯｸ"), "kana")             # 半角カナは NFKC で読む
        self.assertEqual(term_class("hooks"), "latin")
        self.assertEqual(term_class("２０２６年"), "latin")        # 全角の数字は NFKC で英数字
        self.assertEqual(term_class("用語"), "other")
        self.assertEqual(term_class("「括弧」"), "other")
        rows = [r for r in KANA_ROWS if r[2] <= ord("ん") <= r[3]]
        self.assertEqual(rows[0][1], "わ行")

    def test_period_text(self):
        class G:
            @staticmethod
            def text(key, default):
                return default
        self.assertEqual(period_text(G, {"date": "2026-10", "approx": True, "version": "2.1.300"}),
                         "2026-10 ごろ・Claude Code 2.1.300")
        self.assertEqual(period_text(G, {"date": "2026-09", "until": "2026-10"}), "2026-09〜2026-10")
        self.assertEqual(period_text(G, {"date": 2026}), "2026")
        self.assertEqual(period_text(G, None), "")


class TestMarkerEdgeCases(GenCase):
    def add(self, text: str, rel: str = PAGE) -> None:
        self.write(rel, self.read(rel) + "\n" + text + "\n")

    def test_unknown_block_is_kept(self):
        self.add("<!-- gen:begin no-such -->\n手で書いた中身\n<!-- gen:end no-such -->")
        out = self.generate()
        self.assertIn("<!-- gen:begin no-such -->\n手で書いた中身\n<!-- gen:end no-such -->", self.read(PAGE))
        self.assertIn("知らない生成の部分「no-such」", out)

    def test_unclosed_marker_is_kept(self):
        self.add("<!-- gen:begin roadmap -->\n中身")
        out = self.generate()
        self.assertIn("<!-- gen:begin roadmap -->\n中身", self.read(PAGE))
        self.assertIn("gen:begin「roadmap」が閉じていない", out)

    def test_block_inside_a_sentence_is_kept(self):
        self.add("文の中の <!-- gen:begin roadmap --><!-- gen:end roadmap --> は書かない。")
        out = self.generate()
        self.assertIn("文の中の <!-- gen:begin roadmap --><!-- gen:end roadmap --> は書かない。", self.read(PAGE))
        self.assertIn("目印をそれぞれ1行に置く", out)

    def test_parameters(self):
        self.add("<!-- gen:begin signs -->\n<!-- gen:end signs -->\n\n<!-- gen:begin roadmap x -->\n<!-- gen:end roadmap x -->\n\n"
                 "<!-- gen:begin signs nothing -->\n<!-- gen:end signs nothing -->\n\n"
                 "<!-- gen:begin terms nothing -->\n<!-- gen:end terms nothing -->\n\n"
                 "<!-- gen:begin snippet Bad Param -->\n<!-- gen:end snippet Bad Param -->")
        out = self.generate()
        self.assertIn("生成の部分「signs」に引数（<sign の type>）がない", out)
        self.assertIn("生成の部分「roadmap」は引数を取らない", out)
        self.assertIn("「nothing」は site.yml の sign_types にない", out)
        self.assertIn("生成の部分「terms nothing」の引数は kana・latin・old のどれか", out)
        self.assertIn("引数は <ページの id>/<名前> にする", out)

    def test_nested_markers_are_rewritten_by_the_outer(self):
        rel = "docs/symptoms/instructions-ignored.md"
        self.replace(rel, "<!-- gen:begin routes -->\n<!-- gen:end routes -->",
                     "<!-- gen:begin routes -->\n- 縛っていない：<!-- link:begin hooks-basics -->古い<!-- link:end -->\n"
                     "<!-- gen:end routes -->")
        self.generate()
        block = block_content(self.read(rel), "routes")
        self.assertNotIn("link:begin", block)
        self.assertIn("| 縛っていない |", block)

    def test_missing_anchor_and_unknown_page(self):
        self.add("<!-- link:begin how-to-use#no-such -->x<!-- link:end --> と <!-- link:begin no-such-page --><!-- link:end -->")
        out = self.generate()
        text = self.read(PAGE)
        self.assertIn("<!-- link:begin how-to-use#no-such -->[この辞典の引き方](../start/how-to-use.md)<!-- link:end -->", text)
        self.assertIn("<!-- link:begin no-such-page -->no-such-page<!-- link:end -->", text)
        self.assertIn("how-to-use#no-such の見出しが how-to-use の本文にない", out)
        self.assertIn("「no-such-page」のページがない", out)

    def test_anchor_listed_in_sections_but_not_in_body(self):
        self.replace("docs/enforce/hooks-basics.md", "## 終了コード {#exit-codes}", "## 終了コード")
        out = self.generate()
        block = block_content(self.read("docs/symptoms/instructions-ignored.md"), "routes")
        self.assertIn("[フック（hooks）の基本 › 終了コード](../enforce/hooks-basics.md)・", block)   # ページへのリンクにした
        self.assertIn("hooks-basics#exit-codes の見出しが hooks-basics の本文にない", out)

    def test_facts_errors(self):
        self.add("<!-- fact:begin sample-effort --><!-- fact:end -->・<!-- fact:begin no-such -->x<!-- fact:end -->・"
                 "<!-- fact:begin sample-effort model-z api --><!-- fact:end -->・"
                 "<!-- fact:begin sample-limit a b --><!-- fact:end -->")
        out = self.generate()
        text = self.read(PAGE)
        self.assertIn("<!-- fact:begin sample-effort --><!-- fact:end -->・<!-- fact:begin no-such --><!-- fact:end -->", text)
        self.assertIn("<!-- fact:begin sample-limit a b -->100 回（2026-10-15 時点）<!-- fact:end -->", text)
        self.assertIn("数値「sample-effort」は表なので、目印に行と列を書く", out)
        self.assertIn("数値「no-such」が data/facts.yml の facts にない", out)
        self.assertIn("行「model-z」と列「api」のセルがない", out)
        self.assertIn("表でないので、行と列（a b）は読まない", out)

    def test_feature_and_snippet_errors(self):
        self.add("<!-- gen:begin feature nothing --><!-- gen:end feature nothing -->・"
                 "<!-- gen:begin feature no-such/maturity --><!-- gen:end feature no-such/maturity -->\n\n"
                 "<!-- gen:begin snippet hooks-basics/no-file -->\n<!-- gen:end snippet hooks-basics/no-file -->")
        out = self.generate()
        self.assertIn("属性「nothing」は機能の属性でない", out)
        self.assertIn("機能「no-such」が data/facts.yml の features にない", out)
        self.assertIn("雛形 snippets/hooks-basics/no-file.* がない", out)
        self.assertIn("雛形「no-file」は準備中。", block_content(self.read(PAGE), "snippet hooks-basics/no-file"))

    def test_unverified_snippet_without_verified_file(self):
        # 動作確認の記録がなくても写し、確かめていないことを書く（decisions 2026-11-04「雛形の動作確認」）
        (self.root / "snippets/hooks-basics/verified.yaml").unlink()
        self.generate()
        block = block_content(self.read(PAGE), "snippet hooks-basics/block-rm")
        self.assertIn("PreToolUse", block)
        self.assertIn("動作を確かめていない雛形", block)
        self.assertNotIn("確かめた環境", block)

    def test_indented_block_keeps_the_indent(self):
        self.add('!!! note "試験"\n\n    <!-- gen:begin causes -->\n    <!-- gen:end causes -->')
        self.generate()
        text = self.read(PAGE)
        block = block_content(text, "causes")
        lines = [x for x in block.split("\n") if x]
        self.assertTrue(all(x.startswith("    ") for x in lines), lines[:3])
        self.assertIn("    <!-- gen:end causes -->", text)

    def test_markers_in_fenced_code_are_not_read(self):
        self.add("```markdown\n<!-- gen:begin roadmap -->\n<!-- gen:end roadmap -->\n```")
        self.generate()
        self.assertIn("```markdown\n<!-- gen:begin roadmap -->\n<!-- gen:end roadmap -->\n```", self.read(PAGE))

    def test_handwritten_references_heading_is_not_repeated(self):
        self.replace("docs/basics/request-vs-lock.md", "<!-- gen:begin references -->\n<!-- gen:end references -->",
                     "## 参考 {#references}\n\n<!-- gen:begin references -->\n<!-- gen:end references -->")
        self.generate()
        text = self.read("docs/basics/request-vs-lock.md")
        self.assertEqual(text.count("{#references}"), 1)
        self.assertIn("- [試験用の公式の文書](https://docs.example.com/hooks)", block_content(text, "references"))

    def test_host_page_without_its_markers_is_noted(self):
        self.replace("docs/start/roadmap.md", "<!-- gen:begin roadmap -->\n<!-- gen:end roadmap -->", "目印を外した。")
        out = self.generate()
        self.assertIn("本体を生成するページに目印のない生成の部分 1: roadmap（docs/start/roadmap.md）", out)

    def test_missing_labels_are_noted(self):
        self.write_config({"  surfaces: {app: アプリ, claude-code: Claude Code, api: API}":
                           "  surfaces: {app: アプリ, api: API}"})
        out = self.generate()
        self.assertIn("tools/gen/config.yml の labels.surfaces に「claude-code」がない", out)
        self.assertIn("（claude-code、症状）", self.read("docs/start/reverse-index.md"))


if __name__ == "__main__":
    unittest.main()
