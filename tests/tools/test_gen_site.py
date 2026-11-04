"""作る層（tools/gen/ と tools/gen_site.py）の試験：試験用の置き場所（fixtures/gen/）で生成物の全体を作り、中身を見る。
`uv run python -m unittest discover -s tests/tools` で動く。置き場所の中身は gen_helpers.py の冒頭。

見るもの：nav.yml（公開するページだけ・exclude_docs・extra.ca）・分野の入口・一覧・llms.txt・pages.json・graph.json・
目印の間（link・fact・gen の各部分）・目印の外が変わらないこと・参考の節とページ下部を末尾に足すこと・--check・--page・
古い生成物を消すこと・同じ入力から同じ出力・MkDocs と Zensical の --strict のビルド（入っていれば）。
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import unittest

import yaml

from gen_helpers import HELD, REPO, GenCase, block_content, outside_markers

PUBLISHED = ["how-to-use", "six-causes", "reverse-index", "term-index", "roadmap", "knowledge-map", "request-vs-lock",
             "long-tasks", "hook-vs-skill", "verification-ladder", "checking-long-tasks", "hooks-basics", "contest-rules",
             "instructions-ignored", "claims-done-but-isnt", "outdated-advice-ledger", "change-timeline-2026"]


def nav_paths(items) -> list[str]:
    out = []
    for x in items:
        if isinstance(x, str):
            out.append(x)
        elif isinstance(x, dict):
            for v in x.values():
                out += nav_paths(v) if isinstance(v, list) else [v]
    return out


class TestNav(GenCase):
    def setUp(self):
        super().setUp()
        self.out = self.generate()
        self.nav = yaml.safe_load(self.read("nav.yml"))

    def test_only_published_pages_and_generated_pages(self):
        paths = nav_paths(self.nav["nav"])
        pages = [p for p in paths if p.rsplit("/", 1)[-1] != "index.md" and not p.startswith("lists/")]
        self.assertEqual([p.rsplit("/", 1)[1][:-3] for p in pages], PUBLISHED)       # ナビゲーションの順
        self.assertEqual(paths[0], "index.md")
        self.assertNotIn("enforce/writing-safe-hooks.md", paths)
        self.assertNotIn("symptoms/stub-in-docs.md", paths)
        entrances = [p for p in paths if p.rsplit("/", 1)[-1] == "index.md" and "/" in p and not p.startswith("lists/")]
        self.assertEqual(entrances, ["start/index.md", "basics/index.md", "context/index.md", "extend/index.md",
                                     "verify/index.md", "enforce/index.md", "contest/index.md", "symptoms/index.md",
                                     "changes/index.md"])
        self.assertEqual([p for p in paths if p.startswith("lists/")],
                         ["lists/index.md", "lists/by-level.md", "lists/by-surface.md", "lists/by-principle.md",
                          "lists/by-scene.md"])

    def test_sections_chapters_and_nav_title(self):
        start = self.nav["nav"][1]["入口と地図"]
        self.assertEqual(start[0], "start/index.md")
        self.assertEqual(list(start[1]), ["使い方"])
        self.assertEqual(start[3]["辞書として引く"][0], {"逆引き辞典": "start/reverse-index.md"})   # nav_title

    def test_exclude_docs_lists_unpublished_docs_pages(self):
        self.assertEqual(self.nav["exclude_docs"].split(), ["/enforce/writing-safe-hooks.md", "/symptoms/stub-in-docs.md"])

    def test_extra_for_templates(self):
        ca = self.nav["extra"]["ca"]
        self.assertEqual(ca["fields"]["start"], "入口と地図")
        self.assertEqual(ca["types"]["concept"], "考え方")
        self.assertEqual(ca["stages"], {"stub": "準備中", "draft": "下書き", "reviewed": "分かりやすさ確認済み", "done": "完成"})
        self.assertEqual(ca["surfaces"]["claude-code"], "Claude Code")
        self.assertEqual(ca["levels"], ["使う", "整える", "任せる", "仕組みにする", "回す"])
        self.assertEqual(ca["pages_json"], "assets/data/pages.json")
        self.assertEqual(ca["lists"]["level"], "lists/by-level.md")
        # 期限の日（手で数えた値。request-vs-lock は未確認の数値 sample-unchecked の 2026-10-01 + 高 30 日）
        self.assertEqual(ca["expires"]["request-vs-lock"], "2026-10-31")
        self.assertEqual(ca["expires"]["instructions-ignored"], "2027-01-10")          # tracks の sample-hooks
        self.assertNotIn("how-to-use", ca["expires"])                                   # draft で数値がない
        self.assertEqual(ca["badges"]["hooks-basics"], {"maturity": "GA", "enforcement": "鍵"})

    def test_empty_site_has_only_the_top(self):
        shutil.rmtree(self.root / "docs")
        (self.root / "docs").mkdir()
        (self.root / "docs" / "index.md").write_text("# トップ\n", encoding="utf-8")
        self.generate()
        nav = yaml.safe_load(self.read("nav.yml"))
        self.assertEqual(nav["nav"], ["index.md"])
        self.assertNotIn("exclude_docs", nav)
        self.assertFalse((self.root / "docs" / "lists").exists())
        self.assertIn("ページ数：0", self.read("docs/llms.txt"))
        self.assertEqual(json.loads(self.read("docs/assets/data/pages.json"))["pages"], [])


class TestGeneratedPages(GenCase):
    def setUp(self):
        super().setUp()
        self.generate()

    def test_entrance(self):
        text = self.read("docs/start/index.md")
        self.assertTrue(text.startswith("---\ntitle: 入口と地図\n---\n\n<!-- tools/gen_site.py が生成する。手で直さない -->\n"))
        self.assertIn("## 辞書として引く\n\n- [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)（下書き）：試験用の要約。", text)
        self.assertFalse((self.root / "docs" / "surfaces" / "index.md").exists())          # 公開するページのない分野
        contest = self.read("docs/contest/index.md")
        self.assertIn("## コンテストの場面を持つ、ほかの分野のページ\n\n- [お願いと鍵](../basics/request-vs-lock.md)"
                      "（基礎：なぜそうなるか・使う）：指示と仕組みの違いが分かる。", contest)
        self.assertNotIn("writing-safe-hooks", self.read("docs/enforce/index.md"))

    def test_lists(self):
        text = self.read("docs/lists/by-level.md")
        self.assertIn("search:\n  exclude: true\n", text)
        self.assertEqual(re.findall(r"^## (.+)$", text, re.M), ["使う {#使う}", "整える {#整える}", "任せる {#任せる}",
                                                                "仕組みにする {#仕組みにする}"])
        self.assertIn("- [お願いと鍵](../basics/request-vs-lock.md)（基礎：なぜそうなるか・使う）", text)
        surface = self.read("docs/lists/by-surface.md")
        self.assertIn("## Claude Code {#claude-code}", surface)
        self.assertNotIn("## API", surface)
        index = self.read("docs/lists/index.md")
        self.assertIn("[レベル別の一覧](by-level.md)：[使う](by-level.md#使う)（1）・[整える](by-level.md#整える)（3）", index)

    def test_llms_txt(self):
        text = self.read("docs/llms.txt")
        lines = [x for x in text.split("\n") if x.startswith("- [")]
        self.assertEqual(len(lines), len(PUBLISHED))
        self.assertIn("- [お願いと鍵](https://example.com/atlas/basics/request-vs-lock/)（request-vs-lock・concept・使う・"
                      "reviewed・2026-10-20）：指示と仕組みの違いが分かる。二つ目の文。", lines)
        self.assertIn("（how-to-use・guide・—・draft・未検証）", text)
        self.assertTrue(text.startswith("# claude-atlas\n\n> 試験用の教材の説明\n\nこの辞典は Anthropic の公式の教材ではない。\n"))
        self.assertNotIn(HELD, text)
        self.assertNotIn("stub-in-docs", text)

    def test_pages_json(self):
        data = json.loads(self.read("docs/assets/data/pages.json"))
        self.assertEqual([p["id"] for p in data["pages"]], PUBLISHED)
        by = {p["id"]: p for p in data["pages"]}
        p = by["request-vs-lock"]
        self.assertEqual((p["url"], p["stage"], p["level"], p["confirmed"], p["expires"], p["expires_by"]),
                         ("basics/request-vs-lock/", "reviewed", "使う", "2026-10-20", "2026-10-31", "fact:sample-unchecked"))
        self.assertEqual(p["verified_with"]["claude_code"], "2.1.317")
        self.assertIsNone(by["how-to-use"]["expires"])
        self.assertEqual(by["hook-vs-skill"]["expires"], "2026-10-01")         # 未確認の機能 sample-beta の確認日 + 高 30 日
        self.assertEqual(by["hooks-basics"]["features"][0]["enforcement"], "鍵")
        self.assertNotIn("maturity", by["hook-vs-skill"]["features"][2])        # 未確認の機能の値は出さない
        self.assertEqual([t["label"] for t in data["types"]][:2], ["考え方", "機能"])
        # 各行は1行の JSON
        self.assertEqual(sum(1 for line in self.read("docs/assets/data/pages.json").split("\n") if line.startswith('{"id":')),
                         len(PUBLISHED))

    def test_graph_json(self):
        g = json.loads(self.read("docs/assets/data/graph.json"))
        self.assertEqual([n["id"] for n in g["nodes"]], PUBLISHED)
        ids = set(PUBLISHED)
        for e in g["edges"]:
            self.assertIn(e["from"], ids)
            self.assertIn(e["to"], ids)
        self.assertIn({"from": "request-vs-lock", "to": "instructions-ignored", "kind": "prerequisite"}, g["edges"])
        self.assertIn({"from": "instructions-ignored", "to": "hooks-basics", "kind": "route", "cause": "縛っていない"}, g["edges"])
        node = next(n for n in g["nodes"] if n["id"] == "instructions-ignored")
        self.assertEqual(node["routes"], [{"cause": "縛っていない", "to": ["hooks-basics"]}])   # 未公開の先は入れない
        self.assertNotIn(HELD, json.dumps(g, ensure_ascii=False))


class TestMarkers(GenCase):
    def setUp(self):
        super().setUp()
        self.before = {p.relative_to(self.root).as_posix(): p.read_text(encoding="utf-8")
                       for p in (self.root / "docs").rglob("*.md")}
        self.out = self.generate()

    def test_outside_of_markers_is_unchanged(self):
        for rel, old in self.before.items():
            new, was = outside_markers(self.read(rel)), outside_markers(old)
            if "<!-- gen:begin page-links -->" not in old and rel != "docs/index.md":
                # 末尾に目印を足しただけ（足した部分は目印の組だけ）
                self.assertTrue(new.startswith(was.rstrip("\n") + "\n\n<!-- gen:begin "), rel)
                tail = new[len(was.rstrip("\n")):]
                self.assertEqual(re.sub(r"<!-- gen:(begin|end) (references|page-links) -->", "", tail).strip(), "", rel)
                continue
            self.assertEqual(new, was, rel)

    def test_link_markers(self):
        top = self.read("docs/index.md")
        self.assertIn("<!-- link:begin reverse-index -->[逆引き辞典（症状・やりたいこと・状況）](start/reverse-index.md)"
                      "<!-- link:end -->", top)
        self.assertIn("<!-- link:begin outdated-advice-ledger#sample-caps -->[古くなった助言の台帳]"
                      "(changes/outdated-advice-ledger.md#sample-caps)<!-- link:end -->", top)     # 台帳の行の anchor
        self.assertIn(f"<!-- link:begin {HELD} -->安全なフックの書き方（準備中）<!-- link:end -->", top)
        use = self.read("docs/start/how-to-use.md")
        self.assertIn("[逆引き辞典（症状・やりたいこと・状況） › 困りごとから引く](reverse-index.md#by-symptom)", use)

    def test_fact_markers(self):
        text = self.read("docs/basics/request-vs-lock.md")
        self.assertIn("<!-- fact:begin sample-limit -->100 回（2026-10-15 時点）<!-- fact:end -->", text)
        self.assertIn("<!-- fact:begin sample-sentence -->5 時間ごとに戻る（2026-10-20 の確認）<!-- fact:end -->", text)
        self.assertIn("<!-- fact:begin sample-effort model-a claude-code -->medium（2026-10-10 時点）<!-- fact:end -->", text)
        self.assertIn("<!-- fact:begin sample-unchecked -->未確認<!-- fact:end -->", text)     # 未確認の値は書かない
        self.assertIn("`<!-- fact:begin sample-limit -->` の形", text)                          # コードの中は読まない
        self.assertIn("```text\n<!-- gen:begin references -->\n```", text)

    def test_routes_table(self):
        block = block_content(self.read("docs/symptoms/instructions-ignored.md"), "routes")
        self.assertTrue(block.startswith("\n<!-- textlint-disable -->\n\n| 原因 | 対処のページ（近い順） |"))
        rows = [x for x in block.split("\n") if x.startswith("| ") and "---" not in x][1:]
        self.assertEqual(rows, ["| 散らかっている | CLAUDE.md に何を書くか（準備中） |",               # site.yml の原因の順
                                "| 縛っていない | [フック（hooks）の基本 › 終了コード](../enforce/hooks-basics.md#exit-codes)<br>"
                                "安全なフックの書き方（準備中） |"])    # 行き先は1つずつセルの中で改行（<br>）

    def test_page_bottom_and_references_are_added(self):
        text = self.read("docs/symptoms/instructions-ignored.md")
        refs, links = text.index("<!-- gen:begin references -->"), text.index("<!-- gen:begin page-links -->")
        self.assertLess(text.index("<!-- gen:end routes -->"), refs)
        self.assertLess(refs, links)
        self.assertTrue(text.endswith("<!-- gen:end page-links -->\n"))
        ref = block_content(text, "references")
        self.assertIn("## 参考 {#references}", ref)
        self.assertIn("- [Sample blog post \\[draft\\]](https://blog.example.org/post)：Example・英語・確認日 2026-10-02・"
                      "[写し](https://web.example.org/2026/post)", ref)
        bottom = block_content(text, "page-links")
        self.assertIn('<div class="ca-page-links" markdown>', bottom)
        self.assertIn("**前提**\n\n- [お願いと鍵](../basics/request-vs-lock.md)", bottom)
        # 次に読む：routes の先（原因の順）
        self.assertIn("**次に読む**\n\n- CLAUDE.md に何を書くか（準備中）\n- [フック（hooks）の基本](../enforce/hooks-basics.md)\n"
                      "- 安全なフックの書き方（準備中）", bottom)
        self.assertIn("**関連**\n\n- [失敗の二つの軸と診断の入口](../start/six-causes.md)", bottom)
        # 手書きの段落の後にあった目印はそのまま。sources がないので参考の節は足さない
        claims = self.read("docs/symptoms/claims-done-but-isnt.md")
        self.assertNotIn("gen:begin references", claims)
        self.assertLess(claims.index("ページ下部の前に書いた手書きの段落。"), claims.index("<!-- gen:begin page-links -->"))

    def test_references_inserted_before_existing_page_links(self):
        self.replace("docs/symptoms/claims-done-but-isnt.md", "sources: []", "sources: [sample-doc]")
        self.generate()
        text = self.read("docs/symptoms/claims-done-but-isnt.md")
        hand = text.index("ページ下部の前に書いた手書きの段落。")
        self.assertLess(hand, text.index("<!-- gen:begin references -->"))
        self.assertLess(text.index("<!-- gen:end references -->"), text.index("<!-- gen:begin page-links -->"))
        self.assertEqual(text.count("<!-- gen:begin page-links -->"), 1)

    def test_next_to_read_cap(self):
        self.write_config({"  next_max: 8 ": "  next_max: 2 "})
        self.generate()
        bottom = block_content(self.read("docs/basics/request-vs-lock.md"), "page-links")
        self.assertIn("**次に読む**\n\n- [長い作業を任せる](../context/long-tasks.md)\n- [確かめ方のはしご]"
                      "(../verify/verification-ladder.md)\n- ほか 5 ページ", bottom)
        # 次に読むで切った分のうち、related にあるページは関連に出る
        self.assertIn("**関連**\n\n- [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)", bottom)

    def test_blocks_are_wrapped_for_textlint(self):
        for rel in ["docs/start/reverse-index.md", "docs/enforce/hooks-basics.md", "docs/changes/outdated-advice-ledger.md"]:
            text = self.read(rel)
            for m in re.finditer(r"<!-- gen:begin ([^>]+?) -->\n(.*?)<!-- gen:end \1 -->", text, re.S):
                self.assertTrue(m.group(2).startswith("<!-- textlint-disable -->\n\n"), (rel, m.group(1)))
                self.assertTrue(m.group(2).endswith("\n\n<!-- textlint-enable -->\n"), (rel, m.group(1)))

    def test_notes(self):
        self.assertIn("注意: extend/hook-vs-skill.md: 比較の表の機能「missing-feature」が data/facts.yml の features にない", self.out)


class TestIndexBlocks(GenCase):
    def setUp(self):
        super().setUp()
        self.generate()

    def test_reverse_index(self):
        text = self.read("docs/start/reverse-index.md")
        sym = block_content(text, "signs symptom")
        self.assertEqual(re.findall(r"^### (.+)$", sym, re.M), ["指示と仕組み", "完了と検証", "返答と品質"])
        # 同じ文は1行に束ね、行き先に面と型の印を付ける（最初の行き先のナビゲーションの順。対処のページは振り分け元の章）
        self.assertIn("- スキルに書いた手順を飛ばされる → [フックとスキルの使い分け](../extend/hook-vs-skill.md)（Claude Code、比較）"
                      "・[CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)（Claude Code、症状）", sym)
        # どの症状のページの routes にもない対処のページは、分野から章を選ぶ（start → 返答と品質）
        self.assertIn("### 返答と品質\n\n- うまくいかないが、何が悪いのか見当がつかない → [失敗の二つの軸と診断の入口](six-causes.md)（案内）",
                      sym)
        goal = block_content(text, "signs goal")
        self.assertIn("### 確かめる\n\n- テストが通るまで終わらせたくない → [確かめ方のはしご](../verify/verification-ladder.md)"
                      "（Claude Code、考え方）・[長い作業の確かめ方](../verify/checking-long-tasks.md)（Claude Code、手順）", goal)
        self.assertNotIn("外した試作のやりたいこと", goal)
        self.assertNotIn("公開しない骨格のページの困りごと", sym)
        self.assertNotIn("手順をスキルにしたい", goal)                 # stubs/ のページ

    def test_term_index(self):
        text = self.read("docs/start/term-index.md")
        kana = block_content(text, "terms kana")
        self.assertIn("### は行 {#terms-ha}\n\n- フック → [フック（hooks）の基本](../enforce/hooks-basics.md)\n", kana)  # 機能の名前
        self.assertIn("- 逆引き → [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)", kana)
        self.assertIn("- [お願いと鍵](../basics/request-vs-lock.md)\n", kana)
        self.assertNotIn("試験用の未確認の機能", kana)                   # 未確認の機能の名前は載せない
        self.assertIn("### 漢字・記号で始まる語（最初の字の順。読みの順ではない） {#terms-other}", kana)
        latin = block_content(text, "terms latin")
        self.assertIn("[C](#terms-latin-c)・[H](#terms-latin-h)・[R](#terms-latin-r)", latin)
        self.assertIn("- hooks → [フック（hooks）の基本](../enforce/hooks-basics.md)", latin)
        old = block_content(text, "terms old")
        self.assertIn("- 古いフック → フック（2026-10 ごろ・Claude Code 2.1.300）：[フック（hooks）の基本](../enforce/hooks-basics.md)",
                      old)
        self.assertNotIn("古い何か", old)                               # 未確認の名前の変更は載せない

    def test_alias_equal_to_another_title_is_dropped(self):
        self.replace("docs/start/how-to-use.md", "aliases: [使い方]", "aliases: [使い方, お願いと鍵]")
        self.generate()
        kana = block_content(self.read("docs/start/term-index.md"), "terms kana")
        self.assertIn("- [お願いと鍵](../basics/request-vs-lock.md)\n", kana)
        self.assertNotIn("お願いと鍵 → ", kana)

    def test_roadmap_orders_guards_first(self):
        block = block_content(self.read("docs/start/roadmap.md"), "roadmap")
        part = block[block.index("### 任せる"):block.index("### 仕組みにする")]
        self.assertEqual(re.findall(r"^\d+\. \[([^\]]+)\]", part, re.M),
                         ["確かめ方のはしご", "長い作業を任せる", "長い作業の確かめ方"])  # 守りを手前に。前提の順は優先
        self.assertNotIn("この辞典の引き方", block)                      # level を持たない型

    def test_causes_table(self):
        block = block_content(self.read("docs/start/six-causes.md"), "causes")
        self.assertIn("| Claude 側 | 縛っていない | [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md) |", block)
        self.assertIn("| 人の側 | 体感を信じる | [完了と言うのに終わっていない](../symptoms/claims-done-but-isnt.md) |", block)
        self.assertIn("| Claude 側 | 見えていない | — |", block)

    def test_ledger_and_timeline(self):
        ledger = block_content(self.read("docs/changes/outdated-advice-ledger.md"), "ledger")
        self.assertIn("### 大文字で強調すれば守られる {#sample-caps}", ledger)
        self.assertIn("- **変わった時期**：2026-10 ごろ・Claude Code 2.1.300", ledger)   # name の行は names の時期
        self.assertIn("- **関わるページ**：[CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)", ledger)
        timeline = block_content(self.read("docs/changes/change-timeline-2026.md"), "timeline")
        rows = [x for x in timeline.split("\n") if x.startswith("- ")]
        self.assertEqual(rows[0], "- 2026-03 ごろ：[大文字で強調すれば守られる](outdated-advice-ledger.md#sample-caps) → "
                                  "守らせたい規則はフックに移す")
        self.assertEqual(len(rows), 3)

    def test_compare_fact_table_feature_and_snippets(self):
        text = self.read("docs/extend/hook-vs-skill.md")
        cmp_ = block_content(text, "compare")
        self.assertIn("| 機能 | 面 | 成熟度 | 強制力 | 圧縮で残るか | 入った版 | 確認日 |", cmp_)
        self.assertIn("| [フック](../enforce/hooks-basics.md) | Claude Code | GA | 鍵 | 残る | 2.1.0（2026-01） | 2026-10-12 |", cmp_)
        self.assertIn("| スキル（準備中） | Claude Code・アプリ | GA | お願い | 残らない | 2.1.50 | 2026-10-05 |", cmp_)
        self.assertIn("| 未確認 | 未確認 | 未確認 | 未確認 | 未確認 | 2026-09-01 |", cmp_)
        table = block_content(text, "fact-table sample-effort")
        self.assertIn("| モデル | API | Claude Code | アプリの面 |", table)
        self.assertIn("| model-a | high | medium | —（値を書いた文書がない） |", table)
        self.assertIn("食い違い：low（[Sample blog post \\[draft\\]](https://blog.example.org/post)。試験用の食い違い）", table)
        hooks = self.read("docs/enforce/hooks-basics.md")
        self.assertIn("<!-- gen:begin feature enforcement -->鍵<!-- gen:end feature enforcement -->。", hooks)
        self.assertIn("<!-- gen:begin feature sample-hooks/since -->2.1.0（2026-01）<!-- gen:end feature sample-hooks/since -->",
                      hooks)
        snip = block_content(hooks, "snippet hooks-basics/block-rm")
        self.assertIn('??? example "雛形：危ない削除を止める"\n\n    ````json\n    {\n', snip)   # 中の ``` より長い囲み
        self.assertIn("確かめた環境：Claude Code 2.1.317（latest）・claude-opus-5-5・WSL2 Ubuntu 24.04・2026-11-20。"
                      "要る最低の版：Claude Code 2.1.50。", snip)
        pending = block_content(hooks, "snippet hooks-basics/pending-one")
        self.assertIn("動作を確かめていない雛形", pending)   # 確認が fail でも写す（decisions 2026-11-04）
        self.assertNotIn("確かめた環境", pending)

    def test_graph_container(self):
        block = block_content(self.read("docs/start/knowledge-map.md"), "graph")
        self.assertIn('<div class="ca-graph" data-graph="../../assets/data/graph.json"></div>', block)


class TestCheckAndPage(GenCase):
    def test_check_after_write_is_clean(self):
        code, out, _ = self.cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("作られる: nav.yml", out)
        self.assertFalse((self.root / "nav.yml").exists())                  # --check は書かない
        self.generate()
        code, out, _ = self.cli("--check")
        self.assertEqual(code, 0, out)
        self.assertIn("生成物は最新", out)

    def test_check_finds_hand_edits_inside_markers(self):
        self.generate()
        self.replace("docs/symptoms/instructions-ignored.md", "| 散らかっている | CLAUDE.md に何を書くか（準備中） |",
                     "| 散らかっている | 手で書き換えた |")
        code, out, _ = self.cli("--check", "--diff")
        self.assertEqual(code, 1)
        self.assertIn("古い: docs/symptoms/instructions-ignored.md", out)
        self.assertIn("-| 散らかっている | 手で書き換えた |", out)

    def test_publishing_a_page_rewrites_links_elsewhere(self):
        self.generate()
        self.held_back = ()
        self.write_config()
        self.generate()
        top = self.read("docs/index.md")
        self.assertIn(f"<!-- link:begin {HELD} -->[安全なフックの書き方](enforce/writing-safe-hooks.md)<!-- link:end -->", top)
        self.assertNotIn("/enforce/writing-safe-hooks.md", self.read("nav.yml").split("exclude_docs")[-1])

    def test_stale_generated_files_are_removed(self):
        self.generate()
        self.write("docs/lists/old.md", "古い一覧\n")
        self.write("docs/surfaces/index.md", "---\ntitle: x\n---\n\n<!-- tools/gen_site.py が生成する。手で直さない -->\n")
        code, out, _ = self.cli("--check")
        self.assertEqual(code, 1)
        self.assertIn("消える: docs/lists/old.md", out)
        self.assertIn("消える: docs/surfaces/index.md", out)
        self.generate()
        self.assertFalse((self.root / "docs/lists/old.md").exists())
        self.assertFalse((self.root / "docs/surfaces/index.md").exists())

    def test_handwritten_entrance_is_not_overwritten(self):
        self.write("docs/start/index.md", "# 手で書いた入口\n")
        out = self.generate()
        self.assertEqual(self.read("docs/start/index.md"), "# 手で書いた入口\n")
        self.assertIn("docs/start/index.md に生成の印がないので上書きしない", out)
        code, _, _ = self.cli("--force")
        self.assertEqual(code, 0)
        self.assertIn("<!-- tools/gen_site.py が生成する。手で直さない -->", self.read("docs/start/index.md"))

    def test_page_option_writes_only_that_page(self):
        code, out, _ = self.cli("--page", "instructions-ignored")
        self.assertEqual(code, 0, out)
        self.assertFalse((self.root / "nav.yml").exists())
        self.assertFalse((self.root / "docs/llms.txt").exists())
        self.assertIn("<!-- gen:begin page-links -->", self.read("docs/symptoms/instructions-ignored.md"))
        self.assertNotIn("textlint-disable", self.read("docs/start/reverse-index.md"))
        code, out, _ = self.cli("--page", "instructions-ignored", "--check")
        self.assertEqual(code, 0, out)

    def test_page_option_on_a_stub(self):
        code, out, _ = self.cli("--page", "what-to-put-in-claude-md")
        self.assertEqual(code, 0, out)
        bottom = block_content(self.read("stubs/extend/what-to-put-in-claude-md.md"), "page-links")
        self.assertIn("- [お願いと鍵](../basics/request-vs-lock.md)", bottom)     # docs/ へ移したときの相対リンク

    def test_full_run_does_not_touch_stubs(self):
        before = self.read("stubs/extend/what-to-put-in-claude-md.md")
        self.generate()
        self.assertEqual(self.read("stubs/extend/what-to-put-in-claude-md.md"), before)

    def test_unknown_page_and_unreadable_root(self):
        code, _, err = self.cli("--page", "no-such-page")
        self.assertEqual(code, 2)
        self.assertIn("no-such-page", err)
        (self.root / "mkdocs.yml").unlink()
        code, _, err = self.cli("--check")
        self.assertEqual(code, 2)
        self.assertIn("mkdocs.yml", err)

    def test_same_input_same_output(self):
        self.generate()
        first = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.tearDown()
        self.setUp()
        self.generate()
        second = {p.relative_to(self.root).as_posix(): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(first, second)
        code, out, _ = self.cli("--check")
        self.assertEqual(code, 0, out)


@unittest.skipUnless(shutil.which("mkdocs") or (REPO / ".venv").exists(), "mkdocs がない")
class TestBuild(GenCase):
    """生成した試験用のサイトが、MkDocs（と Zensical。入っていれば）の --strict のビルドを通る（リンク・anchor・nav・
    exclude_docs の確かめ）。"""

    def build(self, *cmd: str) -> subprocess.CompletedProcess:
        env = dict(os.environ, NO_MKDOCS_2_WARNING="1")
        return subprocess.run(list(cmd), cwd=self.root, capture_output=True, text=True, env=env, timeout=300)

    def test_mkdocs_strict(self):
        try:
            import mkdocs  # noqa: F401
        except ImportError:
            self.skipTest("mkdocs がない")
        self.generate()
        r = self.build(sys.executable, "-m", "mkdocs", "build", "--strict", "-d", str(self.root / "site"))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        site = self.root / "site"
        self.assertFalse((site / "enforce" / "writing-safe-hooks").exists())
        self.assertFalse((site / "symptoms" / "stub-in-docs").exists())
        html = (site / "symptoms" / "instructions-ignored" / "index.html").read_text(encoding="utf-8")
        self.assertIn('<div class="ca-page-links">', html)
        self.assertIn('href="../../enforce/hooks-basics/#exit-codes"', html)
        self.assertTrue((site / "llms.txt").exists())
        self.assertTrue((site / "assets" / "data" / "graph.json").exists())

    def test_zensical_strict(self):
        exe = shutil.which("zensical") or (str(REPO / ".venv/bin/zensical") if (REPO / ".venv/bin/zensical").exists() else None)
        if exe is None:
            self.skipTest("zensical がない（uv sync --group zensical で入る）")
        self.generate()
        r = self.build(exe, "build", "--strict", "-f", "mkdocs.yml")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertFalse((self.root / "site" / "enforce" / "writing-safe-hooks").exists())


if __name__ == "__main__":
    unittest.main()
