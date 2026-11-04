"""材料の束の道具（tools/make_packet.py。工程7）の試験。`uv run python -m unittest discover -s tests/tools` で動く。

fixtures/packet/ は、束の試験用の小さな置き場所：schema/site.yml（道具が読むキーだけ）・stubs/ のページ8と docs/ のページ1・
planning/catalog/・data/・planning/guides/・planning/batches/step6/data/wave1-sources.yml・調査資料 planning/research/ の
ひな形（00・01・03・05・10・11・11b・20・23・24・27 を、本物と同じ形の小さな文書で）と、planning/ の計画の資料（requirements・
design・decisions）。値はすべて試験用の作りもので、ドメインは example.*。試験は、それを一時フォルダに写して使う。

確かめること:
  - 項目の読み方（印への分け方・範囲・前の印の引き継ぎ・（…）の注・別の資料への移り）
  - 印のたどり方（§N・分野NN・Q/KQ・F-1・0-4・#N・p12#N・第N章・第N節・A-14・「…」・の4・付録A-N）と、見つからない・対象外・
    一部だけ見つかった項目の扱い、手前の所で代える語の印、注記の添え方
  - 上限で切るとき、印（【2026-11-03 注記】）の付いた所が残り、「…（略）」と全文の行の範囲が書かれること
  - 束の7つの節の中身（ページ・つながるページ・目次・data・出典・材料・書き方）と、--wave1・--all・--out・--stats・終了コード
  - 本物のリポジトリ（読むだけ）で、--wave1 が tools/check_catalog.py と同じ閉包になり、試作の10ページの束が節の形・大きさに収まること
"""
from __future__ import annotations

import contextlib
import io
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "packet"

import make_packet as mp  # noqa: E402

TEN_PAGES = ["instructions-ignored", "request-vs-lock", "four-specifics", "writing-skills", "claude-md-vs-rules-skills-styles",
             "keep-replies-in-japanese", "agreement-is-not-evidence", "competition-rules", "outdated-advice-ledger", "how-to-use"]


def piece_text(piece) -> str:
    return "\n".join(b.text for b in piece.blocks)


def item_text(item) -> str:
    return "\n".join(piece_text(p) for p in item.pieces)


def outside_fences(text: str) -> str:
    """写しの囲み（```` 〜 ````）の中を空にした束（写しの中の "## 1. …" を束の節と取り違えないため）。"""
    return re.sub(r"^(`{4,})\n.*?^\1$", lambda m: m.group(1) + "\n" + m.group(1), text, flags=re.M | re.S)


def section(text: str, heading: str) -> str:
    """束の "## 6. …" のような節の中身（次の束の節まで。写しの囲みの中は節に数えない）。"""
    lines = text.split("\n")
    fence = None
    start = end = None
    for i, ln in enumerate(lines):
        m = re.match(r"^(`{4,})$", ln)
        if fence is None and m:
            fence = m.group(1)
        elif fence is not None and ln == fence:
            fence = None
        elif fence is None and ln.startswith("## "):
            if start is not None:
                end = i
                break
            if ln.startswith("## " + heading):
                start = i
    if start is None:
        raise AssertionError(f"節 {heading} がない")
    return "\n".join(lines[start:end])


class FixtureCase(unittest.TestCase):
    """fixtures/packet を一時フォルダに写す。"""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "site"
        shutil.copytree(FIXTURE, self.root)
        self.store = mp.Store(self.root)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel: str, text: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.store = mp.Store(self.root)

    def read(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")

    def replace(self, rel: str, old: str, new: str) -> None:
        text = self.read(rel)
        self.assertIn(old, text, rel)
        self.write(rel, text.replace(old, new, 1))

    def resolve(self, raw: str) -> "mp.Item":
        return mp.resolve_item(self.store, 1, raw)

    def run_tool(self, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                code = mp.main(["--root", str(self.root), *args])
            except SystemExit as e:                   # argparse の使い方の誤り
                code = e.code
        return code, out.getvalue(), err.getvalue()

    def packet(self, pid: str, *args: str) -> str:
        code, out, err = self.run_tool(pid, *args)
        self.assertEqual(code, 0, out + err)
        return self.read(f"state/packets/{pid}.md")


# ---------------------------------------------------------------- 項目の読み方


class ParseTests(unittest.TestCase):
    def test_head_key(self):
        cases = {
            "3. 20分野・300ページ候補は活動で切る": "3", "3.1 版と日付": "3.1", "1-5. CLAUDE.md の指示が無視される": "1-5",
            "Q8. よくある不満": "q8", "Key Question 4: 変更点": "kq4", "分野18 症状辞典（20ページ）": "分野18",
            "第10章 正しさは": "第10章", "**F-1. Hooks**": "f-1", "P10（00 分野15 の表）：要点に足す": "p10",
            "A1★ 調査は誰がどうやったか": "a1", "新分野案X：判断と理解を守る": "新分野案x", "W7. TDD(テスト先行)": "w7",
            "C-1": "c-1", "45": "45", "２．全角の数": "2",
        }
        for text, key in cases.items():
            self.assertEqual(mp.head_key(text), key, text)

    def test_expand_range(self):
        self.assertEqual(mp.expand_range("c-1", "c-4"), ["c-1", "c-2", "c-3", "c-4"])
        self.assertEqual(mp.expand_range("p12#71", "p12#73"), ["p12#71", "p12#72", "p12#73"])
        self.assertEqual(mp.expand_range("9.2", "9.4"), ["9.2", "9.3", "9.4"])
        self.assertEqual(mp.expand_range("第3章", "第5章"), ["第3章", "第4章", "第5章"])
        self.assertEqual(mp.expand_range("c-1", "p-3"), [])            # 頭が違う
        self.assertEqual(mp.expand_range("c-5", "c-1"), [])            # 逆順
        self.assertEqual(mp.expand_range("a-1", "a-9999"), [])         # 多すぎる

    def test_split_sources_decides_the_file(self):
        def kinds(raw):
            return [(r.kind, r.key) for r in mp.split_sources(raw)]
        self.assertEqual(kinds("00 §3 分野18"), [("research", "00")])
        self.assertEqual(kinds("research/23 §3.1・§3.7（注）"), [("research", "23")])
        self.assertEqual(kinds("11b p34#56（未確認）"), [("research", "11b")])
        self.assertEqual(kinds("p34#59"), [("pbare", "11b")])
        self.assertEqual(kinds("p12#34"), [("pbare", "11a")])
        self.assertEqual(kinds("requirements §6.7 の4"), [("plan", "requirements")])
        self.assertEqual(kinds("design-review DR-01"), [("plan", "design-review")])
        self.assertEqual(kinds("design §6.13"), [("plan", "design")])
        self.assertEqual(kinds("catalog/README §4.5 の4"), [("plan", "catalog/README")])
        self.assertEqual(kinds("planning/batches/step3/open-issues.md の changes#3"), [("path", "planning/batches/step3/open-issues.md")])
        self.assertEqual(kinds("kyopro-atlas の docs/start/how-to-use.md（手本）"), [("unknown", "")])
        self.assertEqual(kinds("registry の ledger（37項目）"), [("unknown", "")])
        self.assertEqual(kinds("R1-12（工程4の見直し）"), [("unknown", "")])

    def test_split_sources_moves_to_another_file(self):
        def kinds(raw):
            return [(r.kind, r.key) for r in mp.split_sources(raw)]
        self.assertEqual(kinds("research/20 A4・I4、format-and-operations L15（約束）"),
                         [("research", "20"), ("plan", "format-and-operations")])
        self.assertEqual(kinds("11 第4節 #32・research/24 B-32（確認）"), [("research", "11"), ("research", "24")])
        self.assertEqual(kinds("00 §5 台帳（IMPORTANT）と research/22 §3.4"), [("research", "00"), ("research", "22")])
        # 資料の名前でない「・」では分けない
        self.assertEqual(kinds("research/27 #2・#3・§3.2"), [("research", "27")])

    def parse(self, raw: str, **kw):
        ref = mp.split_sources(raw)[0]
        return mp.parse_body(ref.body, ref.notes, ref.quotes, **kw)

    def test_paths_and_inherited_prefix(self):
        g = self.parse("11 第1節 分野01 p56#11")
        self.assertEqual([t.kind for t in g[0].prefix], ["setsu", "bunya"])
        self.assertEqual((g[0].leaf.kind, g[0].leaf.keys), ("pid", ("p56#11",)))
        g = self.parse("03 Q4 T1・T2")                       # T2 は前の組の Q4 を引き継ぐ
        self.assertEqual([[t.raw for t in x.prefix] for x in g], [["Q4"], ["Q4"]])
        self.assertEqual([x.leaf.raw for x in g], ["T1", "T2"])
        g = self.parse("research/23 §3.1・§3.7・#9")           # 節の印は引き継がない
        self.assertEqual([x.prefix for x in g], [[], [], []])
        g = self.parse("10 第3章 二つ目（迎合）・実践")
        self.assertEqual([x.leaf.kind for x in g], ["word", "word"])
        self.assertEqual([t.raw for t in g[1].prefix], ["第3章"])
        self.assertEqual(g[0].leaf.hint, mp.norm_text("迎合"))        # 直後の（…）は絞り込みの手がかり

    def test_ranges_and_ordinals(self):
        g = self.parse("11 第3節 C-1〜C-4")
        self.assertEqual(g[0].leaf.keys, ("c-1", "c-2", "c-3", "c-4"))
        g = self.parse("11 第4節 #1〜#3")
        self.assertEqual((g[0].leaf.kind, g[0].leaf.keys), ("row", ("1", "2", "3")))
        g = self.parse("11 第4節 #1〜3")
        self.assertEqual(g[0].leaf.keys, ("1", "2", "3"))
        g = self.parse("11 第2節 分野01 p12#71〜p12#73")
        self.assertEqual(g[0].leaf.keys, ("p12#71", "p12#72", "p12#73"))
        g = self.parse("11 第1節 分野12 p12#93〜#95")            # 右は # と数だけ
        self.assertEqual(g[0].leaf.keys, ("p12#93", "p12#94", "p12#95"))
        g = self.parse("design §9.2〜§9.4")
        self.assertEqual(g[0].leaf.keys, ("9.2", "9.3", "9.4"))
        g = self.parse("decisions 2026-11-03「書き方の方針（第三者・根拠・コンテスト）」の4と5")
        self.assertEqual([t.kind for t in g[0].prefix], ["date", "word"])
        self.assertEqual((g[0].leaf.kind, g[0].leaf.nums), ("ord", ("4", "5")))
        g = self.parse("decisions 書き方の方針の4と5")             # 語に続く「の4と5」
        self.assertEqual([t.kind for t in g[0].prefix], ["word"])
        self.assertEqual(g[0].leaf.nums, ("4", "5"))
        g = self.parse("10 付録A-9 の4")
        self.assertEqual((g[0].prefix[0].kind, g[0].prefix[0].keys), ("id", ("a-9",)))
        self.assertEqual(g[0].leaf.nums, ("4",))

    def test_words_and_separators(self):
        g = self.parse("05 §1「全体の構図」（公式の対応表）と §3 Inferences（お願いと鍵）")
        self.assertEqual(len(g), 2)                              # 「と §3」で分ける
        self.assertEqual([t.kind for t in g[0].prefix] + [g[0].leaf.kind], ["sec", "word"])
        self.assertEqual(g[1].leaf.text, "inferences")
        g = self.parse("05 §3-6（注）と注記")                      # 数字の後の「と」で分ける。注記は印ではないので残さない
        self.assertEqual([x.leaf.raw for x in g], ["§3-6"])
        g = self.parse("05 §3-6（注）と第2章")
        self.assertEqual([x.leaf.raw for x in g], ["§3-6", "第2章"])
        g = self.parse("00 §3 分野01「お願いと鍵（決定論的か、非決定論的か）」")        # 引用の中の記号では分けない
        self.assertEqual(g[0].leaf.text, mp.norm_text("お願いと鍵（決定論的か、非決定論的か）"))
        g = self.parse("11 第3節 3-2 #5 と、表の後の注記（skill の説明文）")
        self.assertEqual(len(g), 2)
        g = self.parse("00 §2 の五つ目の経路（古い助言を原理で解釈する）")
        self.assertEqual(g[0].leaf.raw, "五つ目の経路")
        self.assertEqual(g[0].leaf.hint, mp.norm_text("古い助言を原理で解釈する"))

    def test_comments_and_quotes_nest(self):
        flat, notes = mp.strip_comments("design-review DR-01（題名（準備中））・DR-10「引用（中）」")
        self.assertEqual(notes, ["題名（準備中）"])
        self.assertIn("DR-10「引用（中）」", flat)                  # 引用の中の（…）は注ではない
        flat, quotes = mp.extract_quotes("§1「公式は『お願い』と『鍵』を区別する」と §3")
        self.assertEqual(quotes, ["公式は『お願い』と『鍵』を区別する"])
        self.assertNotIn("お願い", flat)

    def test_pids_as_rows(self):
        g = self.parse("11b p34#56", pids_as_rows=True)
        self.assertEqual((g[0].leaf.kind, g[0].leaf.keys), ("row", ("56",)))
        g = mp.parse_body(*self.bare("p34#59"), pids_as_rows=True)
        self.assertEqual((g[0].leaf.kind, g[0].leaf.keys), ("row", ("59",)))

    def bare(self, raw):
        ref = mp.split_sources(raw)[0]
        return ref.body, ref.notes, ref.quotes

    def test_hint_terms(self):
        self.assertEqual(mp.hint_terms(["カスタムコマンドは skills に統合"]), ["カスタムコマンド", "skills", "統合"])
        self.assertEqual(mp.hint_terms(["研究の段落の訂正", "注記つき"]), ["研究"])       # 「訂正」「注記」「段落」は手がかりにしない
        self.assertIn("p12#35", mp.hint_terms(["p12#35・p12#40"]))
        self.assertEqual(mp.hint_terms([]), [])


# ---------------------------------------------------------------- 印をたどる


class ResolveTests(FixtureCase):
    def assertFound(self, item, *needles, absent=()):
        self.assertEqual(item.status, "ok", f"{item.raw}: {item.status} {item.missing} {item.reason}")
        text = item_text(item)
        for n in needles:
            self.assertIn(n, text, item.raw)
        for n in absent:
            self.assertNotIn(n, text, item.raw)

    def test_section_by_number_and_field_number(self):
        it = self.resolve("00 §3 分野18")
        self.assertFound(it, "### 分野18 症状辞典（20ページ）", "【2026-11-03 訂正】熟練度の差", "| 意図と違うものが出てくる |",
                         absent=("分野01", "指示と仕組みの困りごと"))
        self.assertRegex(it.pieces[0].lines_desc, r"^\d+〜\d+ 行$")
        self.assertEqual(it.pieces[0].kind, "heading")
        start, end = (int(x) for x in re.findall(r"\d+", it.pieces[0].lines_desc))
        lines = self.read("planning/research/00-content-report.md").split("\n")
        self.assertEqual(lines[start - 1], "### 分野18 症状辞典（20ページ）")      # 行の範囲は、写しの元の行
        self.assertTrue(lines[end - 1].startswith("| CLAUDE.md や指示が守られない"))

    def test_quoted_title_finds_the_table_row(self):
        it = self.resolve("00 §3 分野01「お願いと鍵（決定論的か、非決定論的か）」")
        self.assertFound(it, "| お願いと鍵（決定論的か、非決定論的か） | L2 | 必須 |", "| ページ候補 | Lv | 優先 |", absent=("トークンとは",))
        self.assertEqual(it.pieces[0].kind, "row")

    def test_quote_marks_do_not_matter(self):
        it = self.resolve("00 §1「公式は失敗を四つに分け、『お願い』と『鍵』を区別する」")
        self.assertFound(it, "公式は Claude Code を定義している", "【2026-11-03 訂正】この段落の定義", absent=("実践者の段落",))

    def test_heading_text_with_a_hint_note(self):
        it = self.resolve("00 §4 指示と仕組みの困りごと（守られない・skill が使われない）")
        self.assertFound(it, "- 守られない", "- skill が使われない")

    def test_bold_label_with_a_hint_stops_at_the_next_label(self):
        it = self.resolve("00 §2 の五つ目の経路（古い助言を原理で解釈する）")
        self.assertFound(it, "五つ目の説明。回避策が仕組みに置き換わる", absent=("一つ目の説明",))
        self.assertEqual(it.pieces[0].kind, "label")

    def test_label_by_id_with_its_note(self):
        it = self.resolve("01 D-2（frontmatter・置き換えと動的な注入）")
        self.assertFound(it, "**D-2. Skills", "- **配置**: 場所は五つある。", "【2026-11-03 注記】配置の優先", absent=("D-1", "F-1", "Hooks"))

    def test_key_question_and_numbered_heading(self):
        it = self.resolve("01 KQ4 4-2（廃止・削除・改名・非推奨）")
        self.assertFound(it, "カスタム slash commands は skills に統合", "メモリショートカット削除", absent=("Agent teams",))
        self.assertFound(self.resolve("01 4-2"), "#### 4-2.")

    def test_q_section_with_inherited_prefix(self):
        it = self.resolve("03 Q4 T1・T2")
        self.assertFound(it, "T1 の本文", "T2 の本文")
        self.assertEqual(len(it.pieces), 2)
        it = self.resolve("03 Q5 Takeaway・P1（訂正）")
        self.assertFound(it, "Q5 の要点", "P1 の本文")
        self.assertFound(self.resolve("research/03 Q8 F6（決めた道具を使わない）"), "F6 の本文")

    def test_prefix_that_does_not_hold_falls_back_to_the_whole_file(self):
        it = self.resolve("03 Q4 F6")                              # F6 は Q8 にある
        self.assertFound(it, "F6 の本文")

    def test_numbered_heading_and_two_groups(self):
        self.assertFound(self.resolve("05 §1-5"), "1-5 の本文。症状と原因")
        it = self.resolve("05 §1「全体の構図」（公式の対応表）と §3 Inferences（お願いと鍵）")
        self.assertFound(it, "構図の本文", "推論の本文")
        self.assertEqual(len(it.pieces), 2)

    def test_chapter_labels_with_notes(self):
        it = self.resolve("10 第1章 ルールの地図（注記つき）")
        self.assertFound(it, "地図の段落。規則は毎年書き換わる", "【2026-11-03 注記】この段落の規則", "注記の後の追加の段落",
                         absent=("核の段落", "柱の段落"))
        it = self.resolve("10 第3章 二つ目（迎合）・実践")
        self.assertFound(it, "迎合の段落", "実践の段落", absent=("過度依存の段落",))
        self.assertEqual([p.kind for p in it.pieces], ["label", "label"])

    def test_crosscheck_rows_by_original_id_in_a_section(self):
        it = self.resolve("11 第1節 分野01 p56#11（規範は保証にならない）")
        self.assertFound(it, "| 既存「迎合」に追加 | 規範は保証にならない。 | 強 | p56#11 |", "| 提案ページ |", absent=("p12#152", "迎合 | 例1"))
        it = self.resolve("11 第2節 分野04 p12#105・p34#74・p12#106")        # p12#105 と p34#74 は同じ行
        self.assertFound(it, "具体性の4点", "同上 | 競プロの誤り")
        self.assertEqual(len(it.pieces), 1)                                    # 同じ表の行は1つにまとめる
        it = self.resolve("11 第2節 分野01 p12#71〜p12#73")
        self.assertFound(it, "例1", "例2", "例3")

    def test_the_section_in_front_decides_which_row_is_meant(self):
        it = self.resolve("11 第2節 分野01 p12#72")                          # p12#72 は第1節にも出る
        self.assertFound(it, "| 同上 | 例2 |", absent=("第1節の側の行",))
        it = self.resolve("11 第1節 分野01 p12#72")
        self.assertFound(it, "第1節の側の行", absent=("例2",))
        it = self.resolve("11 第1節 分野04「具体性の4点」p12#106")           # 行の印の後ろの印は、その表の中で探す
        self.assertFound(it, "| 同上 | 競プロの誤り。 | 中 | p12#106 |")

    def test_crosscheck_notes_after_the_table_are_attached_when_they_mention_the_rows(self):
        it = self.resolve("11 第3節 C-1〜C-2")
        self.assertFound(it, "| C-1 | AtCoder の規則", "| C-2 | 短期 AHC の規則", "【2026-11-03 注記】C-1 の内容", absent=("C-3 | 長期", "C-9"))
        self.assertIn("表の後の注記を添えた", it.pieces[0].extra_note)
        it = self.resolve("11 第3節 C-3")                                      # C-3 に触れる注記はない
        self.assertFound(it, "C-3 | 長期 AHC", absent=("【2026-11-03 注記】",))
        it = self.resolve("11 第3節 C-3（注記つき）")                          # 注記を求めていて、注記が少ないので、触れていなくても添える
        self.assertFound(it, "C-3 | 長期 AHC", "【2026-11-03 注記】C-1 の内容", "【2026-11-03 注記】C-9 はこの表の外")
        text = self.read("planning/research/11-crosscheck.md")
        self.write("planning/research/11-crosscheck.md", text.replace("\n## 第4節", "\n> 【2026-11-03 注記】C-10 の注記。\n\n> 【2026-11-03 注記】C-11 の注記。\n\n## 第4節"))
        it = self.resolve("11 第3節 C-3（注記つき）")                          # 注記が多いと、行に触れているものだけ
        self.assertFound(it, "C-3 | 長期 AHC", absent=("【2026-11-03 注記】",))
        it = self.resolve("11 第3節 C-1〜C-2（注記つき）")
        self.assertFound(it, "【2026-11-03 注記】C-1 の内容", absent=("C-9", "C-10"))

    def test_crosscheck_numbered_rows(self):
        self.assertFound(self.resolve("11 第4節 #1〜#2（注記つき）"), "| 1 | 長期 AHC は2部門制", "| 2 | 短期 AHC", absent=("| 52 |",))
        self.assertFound(self.resolve("11 第4節 #52"), "| 52 | 数値の主張 | 未確認 |")

    def test_bare_original_id_reads_the_first_table_of_the_note(self):
        it = self.resolve("p34#59")
        self.assertFound(it, "| 59 | 8 | 採点のバグを直したら", absent=("別の表の59行目",))
        self.assertFound(self.resolve("11b p34#58"), "| 58 | 8 | ほかの論点 |")

    def test_result_table_rows_and_sections(self):
        self.assertFound(self.resolve("research/23 #2（組み込みの出力スタイル）"), "| 2 | output style の組み込みは4種", "| # | 主張 | 結果 |",
                         absent=("古い前提",))
        it = self.resolve("research/23 §3.1・§3.7（注）")
        self.assertFound(it, "本文 3.1。", "本文 3.7。")
        self.assertEqual(len(it.pieces), 2)

    def test_letter_number_rows_and_headings(self):
        it = self.resolve("research/24 §2.3 イ・A-14・B-44・P-4")
        self.assertEqual(it.status, "partial")                                  # B-44 は表にない
        text = item_text(it)
        for n in ("| イ 同意を根拠にする | 強 |", "| A-14 | 使い込むほど強まる | 誤り |", "P-4 の本文。"):
            self.assertIn(n, text)
        self.assertEqual(it.missing, ["B-44 が見つからない"])
        self.assertNotIn("預けすぎる", text)

    def test_bullets_by_leading_id(self):
        it = self.resolve("research/27 §4 P10・P12")
        self.assertFound(it, "- P10（00 分野15 の表）：要点に足す。", "- P12 英語への回帰の検証ノート。", absent=("P13",))
        self.assertEqual([p.kind for p in it.pieces], ["item", "item"])

    def test_two_sources_in_one_item(self):
        it = self.resolve("research/20 A4・I4、requirements §6.5（約束）")
        self.assertFound(it, "守れない約束を書かない", "一番伝えたいこと", "規則の要約は載せない")
        self.assertEqual({p.doc.rel.split("/")[-1] for p in it.pieces}, {"20-retro.md", "requirements.md"})

    def test_plan_documents(self):
        self.assertFound(self.resolve("design §6.13（大会の規則）"), "大会の規則の本文", absent=("見せ方の本文",))
        it = self.resolve("requirements §6.7 の4（禁止事項を CLAUDE.md に書くか：二層）")      # 表の4行目
        self.assertFound(it, "| 禁止事項を CLAUDE.md に書くか | 二層にする |", "| 論点 | 統合した書き方 |", absent=("成果で示す",))

    def test_ordinal_stays_inside_the_section_in_front(self):
        it = self.resolve("requirements §6.5 の4")                              # 6.5 には4番目がない
        self.assertEqual(it.status, "missing", item_text(it))
        self.assertFalse(it.pieces)

    def test_decisions_by_date_row_and_numbered_items(self):
        it = self.resolve("decisions 2026-11-03「大会の規則の版」・書き方の方針（第三者・根拠・コンテスト）の4と5")
        self.assertFound(it, "| 大会の規則の版 | 公式 X で確かめた版だけを入れる |", "4. **大会の規則**：版と類型だけを持つ",
                         "5. **kyopro-atlas との境界**：リンクする", absent=("AI 臭さ", "名指ししない"))

    def test_same_heading_start_is_told_apart_by_the_note_in_parentheses(self):
        it = self.resolve("decisions 書き方の方針（安全・面・表現）の4")
        self.assertFound(it, "4. **「AI 臭さ」**：読みやすさとして扱う", absent=("大会の規則：版と類型だけを持つ",))

    def test_appendix_ids_and_numbered_lines_inside_a_code_fence(self):
        self.assertFound(self.resolve("10 付録A-6"), "雛形 A-6 の本文。", absent=("愚直解",))
        it = self.resolve("10 付録A-9 の4（ddmin で縮める）")
        self.assertFound(it, "4. 不一致が出ても本解は直さないで。ddmin で縮めて。", absent=("2. 生成器",))

    def test_a_word_that_only_says_where_in_the_place_in_front_is_that_place(self):
        it = self.resolve("00 §3 分野18 本文（症状ページの書き方）")
        self.assertFound(it, "症状ページは、症状の確認から原因へ進む順に書く。", "【2026-11-03 訂正】熟練度の差")      # 見つからないのではない
        it = self.resolve("00 §3 分野01「お願いと鍵（決定論的か、非決定論的か）」の行とその注記")
        self.assertFound(it, "| お願いと鍵（決定論的か、非決定論的か） | L2 | 必須 |")

    def test_a_word_that_is_not_found_is_replaced_by_the_place_in_front_and_said(self):
        it = self.resolve("10 第3章 実践②③（注記つき）")
        self.assertEqual(it.status, "partial")
        self.assertIn("迎合の段落", item_text(it))
        self.assertEqual(it.missing, ["実践②③ が見つからないので、手前の「第3章」の所を写した"])

    def test_not_found_and_out_of_scope(self):
        it = self.resolve("00 §3 分野99")
        self.assertEqual((it.status, it.pieces), ("missing", []))
        self.assertIn("分野99", it.missing[0])
        it = self.resolve("research/99 §1")
        self.assertEqual(it.status, "missing")
        self.assertIn("99-*.md がない", it.reason)
        it = self.resolve("kyopro-atlas の docs/guide/x.md（手本。構成をまねない）")
        self.assertEqual((it.status, it.pieces, it.missing), ("skip", [], []))
        it = self.resolve("planning/batches/step3/none.md の M1")
        self.assertEqual(it.status, "missing")
        self.assertIn("がない", it.reason)

    def test_labels_and_numbered_items_under_them(self):
        it = self.resolve("research/27 §3.3 (b)2")                          # (b) の2番目
        self.assertFound(it, "2. 推論の全文を求める指示を外す。", absent=("3. 誤判定", "1. 引き金"))
        it = self.resolve("research/27 §3.3 (b)")
        self.assertFound(it, "1. 引き金より前に戻す。", "3. 誤判定を報告する。", absent=("面ごとの表示", "目的と文脈を足す"))

    def test_a_note_in_parentheses_that_is_the_title_of_a_row_finds_the_row(self):
        it = self.resolve("00 §3 の対立点の表（トークンとは）")
        self.assertFound(it, "| トークンとは | L1 | 必須 |", "| ページ候補 | Lv | 優先 |", absent=("お願いと鍵",))
        it = self.resolve("00 §3 の対立点の表（長い作業の続け方）")           # 注にも当たる行がなければ、手前の所で代える
        self.assertEqual(it.status, "partial")

    def test_text_that_is_nowhere_is_not_found_by_searching_raw_lines_in_the_whole_file(self):
        it = self.resolve("00 そのような語はどこにもない")
        self.assertEqual(it.status, "missing")
        it = self.resolve("research/23 §3.1 そのような語はどこにもない")
        self.assertEqual(it.status, "partial")                                  # §3.1 の中にないので、§3.1 で代えて、そう書く
        self.assertIn("本文 3.1。", item_text(it))
        self.assertIn("手前の「§3.1」の所を写した", it.missing[0])

    def test_a_word_that_only_says_which_part_is_not_searched_for_alone(self):
        it = self.resolve("research/23 §3.1と注記（Best practices）")            # 「注記」は §3.1 の中の注記のこと
        self.assertFound(it, "本文 3.1。", absent=("本文 3.7。",))
        self.assertEqual(len(it.pieces), 1)
        self.assertTrue(mp.is_descriptive("表の最後の行"))
        self.assertTrue(mp.is_descriptive("注記つき"))
        self.assertFalse(mp.is_descriptive("ルールの地図"))
        self.assertEqual(self.resolve("00 注記").status, "missing")                # それだけなら、探すものがない

    def test_a_file_without_any_locator_is_not_found(self):
        it = self.resolve("01（interactive-mode・common-workflows：画像の貼り付け）")     # 資料は分かるが、節の印がない
        self.assertEqual((it.status, it.pieces), ("missing", []))
        self.assertIn("資料の中の印がない", it.reason)

    def test_partial_when_one_of_several_is_missing(self):
        it = self.resolve("research/23 #2・#99")
        self.assertEqual(it.status, "partial")
        self.assertIn("| 2 | output style", item_text(it))
        self.assertEqual(it.missing, ["#99 が見つからない"])

    def test_a_row_with_a_mark_in_a_cell_keeps_the_mark(self):
        self.replace("planning/research/23-errata.md", "| 1 | 古い前提 | 正しい |", "| 1 | 古い前提 | 正しい。" + "あ" * 700 + "【2026-11-03 訂正】後ろの訂正 |")
        it = self.resolve("research/23 #1")
        text, cut = mp.clip_blocks(it.pieces[0].blocks, 600)
        self.assertTrue(cut)
        self.assertIn("【2026-11-03 訂正】後ろの訂正", text)


# ---------------------------------------------------------------- 切り方


class ClipTests(unittest.TestCase):
    def blocks(self, texts, **flags):
        return [mp.Block(t, mark=bool(mp.MARK_RE.search(t)), **flags) for t in texts]

    def test_short_text_is_kept_whole(self):
        text, cut = mp.clip_blocks(self.blocks(["あいう", "えお"]), 100)
        self.assertEqual((text, cut), ("あいう\nえお", False))

    def test_long_text_is_cut_from_the_head_and_says_so(self):
        paras = [f"段落{i}：" + "あ" * 200 for i in range(10)]
        text, cut = mp.clip_blocks(self.blocks(paras), 700)
        self.assertTrue(cut)
        self.assertIn("段落0：", text)
        self.assertNotIn("段落9：", text)
        self.assertTrue(text.rstrip().endswith("…（以降を略）"))
        self.assertLessEqual(len(text), 700 + 30)

    def test_mark_blocks_are_kept_even_when_they_are_late(self):
        paras = [f"段落{i}：" + "あ" * 200 for i in range(10)]
        paras[8] = "> 【2026-11-03 注記】ここは直した。" + "い" * 50
        text, cut = mp.clip_blocks(self.blocks(paras), 700)
        self.assertTrue(cut)
        self.assertIn("> 【2026-11-03 注記】ここは直した。", text)
        self.assertIn("…（略）", text)

    def test_hint_terms_pick_the_matching_blocks_first(self):
        paras = [f"段落{i}：" + "あ" * 200 for i in range(8)]
        paras[6] = "段落6：スキルの統合について" + "あ" * 200
        text, _ = mp.clip_blocks(self.blocks(paras), 600, ["スキル", "統合"])
        self.assertIn("段落6：スキルの統合", text)
        self.assertIn("段落0：", text)                                  # 残りは頭から
        text, _ = mp.clip_blocks(self.blocks(paras), 600)
        self.assertNotIn("段落6", text)

    def test_the_paragraph_a_matching_note_corrects_is_added(self):
        paras = [f"段落{i}：" + "あ" * 300 for i in range(8)]
        paras[3] = "段落3：研究の数値の段落" + "あ" * 300
        paras[4] = "> 【2026-11-03 訂正】研究の数値を直した。"
        text, _ = mp.clip_blocks(self.blocks(paras), 900, ["研究"])
        self.assertIn("段落3：研究の数値の段落", text)
        self.assertIn("【2026-11-03 訂正】研究の数値を直した。", text)

    def test_table_header_and_marked_rows_stay_and_a_table_without_rows_loses_its_header(self):
        head = [mp.Block("| a | b |", keep=True), mp.Block("|---|---|", keep=True)]
        rows = [mp.Block(f"| 行{i} | " + "あ" * 120 + " |", row=True, core=True) for i in range(6)]
        rows[5] = mp.Block("| 行5 | 注 【2026-11-03 注記】行5の注 |", mark=True, row=True, core=True)
        text, cut = mp.clip_blocks(head + rows, 400)
        self.assertTrue(cut)
        self.assertIn("| a | b |", text)
        self.assertIn("行5の注", text)
        # 次の表は、行が1つも残らなければ見出しだけを残さない
        second = [mp.Block("| c | d |", keep=True), mp.Block("|---|---|", keep=True)] + [mp.Block("| x | " + "う" * 300 + " |", row=True)]
        text, _ = mp.clip_blocks([mp.Block("あ" * 380)] + second, 400)
        self.assertNotIn("| c | d |", text)

    def test_notes_attached_to_a_table_do_not_push_out_the_rows(self):
        head = [mp.Block("| a | b |", keep=True), mp.Block("|---|---|", keep=True)]
        rows = [mp.Block(f"| 行{i} | " + "あ" * 100 + " |", row=True, core=True) for i in range(4)]
        notes = [mp.Block(f"> 【2026-11-03 注記】注{i}" + "い" * 400, mark=True, core=True) for i in range(3)]
        text, cut = mp.clip_blocks(head + rows + notes, 900)
        self.assertTrue(cut)
        for i in range(4):
            self.assertIn(f"| 行{i} |", text)
        self.assertEqual(text.count("【2026-11-03 注記】"), 1)             # 注記は割合の上限まで。最初の1つは必ず残る

    def test_clip_text_keeps_the_mark_that_comes_after_the_cut(self):
        text = "あ" * 300 + "【2026-11-03 注記】大事な注記" + "い" * 100
        out = mp.clip_text(text, 120)
        self.assertLessEqual(len(out), 125)
        self.assertIn("【2026-11-03 注記】大事な注記", out)
        self.assertEqual(mp.clip_text("みじかい", 120), "みじかい")

    def test_shrink_row_keeps_every_column(self):
        row = "| 左 | " + "あ" * 300 + " | 結果は正しい |"
        out = mp.shrink_row(row, 120)
        self.assertLessEqual(len(out), 130)
        self.assertEqual(out.count("|"), row.count("|"))
        self.assertIn("結果は正しい", out)

    def test_allocate_shares_the_item_limit(self):
        self.assertEqual(mp.allocate([100, 100], 3000), [100, 100])
        self.assertEqual(mp.allocate([5000, 100], 3000), [2900, 100])
        out = mp.allocate([5000, 5000, 5000], 3000)
        self.assertEqual(out, [1000, 1000, 1000])
        self.assertEqual(mp.allocate([], 3000), [])
        self.assertTrue(all(x >= mp.MIN_PIECE for x in mp.allocate([5000] * 30, 3000)))


# ---------------------------------------------------------------- 束


class PacketTests(FixtureCase):
    def test_the_head_says_to_read_only_the_packet_and_the_card(self):
        head = self.packet("sym-a").split("## 1. ")[0]
        self.assertIn("読むのはこの束と planning/guides/card.md だけ", head)

    def test_all_seven_sections_come_in_order(self):
        text = self.packet("sym-a")
        heads = re.findall(r"^## (\d)\. ", outside_fences(text), re.M)
        self.assertEqual(heads, ["1", "2", "3", "4", "5", "6", "7"])
        self.assertTrue(text.startswith("# 材料の束：sym-a（指示が守られない（試験用））"))

    def test_page_section_has_the_front_matter(self):
        sec = section(self.packet("sym-a"), "1. ページ")
        for want in ("- id：sym-a", "- 分野：symptoms（症状辞典）", "- 型：symptom", "- level：整える", "- 優先度：必須",
                     "- 題名：指示が守られない（試験用）", "- 要約：書いた規則が破られる原因を切り分け、どれを仕組みに移すかを決める。",
                     "- volatility：中", "- stage：stub　ファイル：stubs/symptoms/sym-a.md", "  - symptom：書いたのに守られない",
                     "  - 原因を安く確かめる順 {#diagnosis}", "- 別名（aliases）：指示を無視される・ルールを破られる", "- 面（surfaces）：claude-code",
                     "- 原理（principle）：縛る・見せる", "- Claude 側の原因（prevents）：散らかっている・縛っていない", "- 場面（scenes）：開発",
                     "- 機能（tracks）：claude-md", "- 古くなった助言（outdated_advice）：old-tip", "- wave：1（第一波の核）"):
            self.assertIn(want, sec)

    def test_a_type_without_level_says_so(self):
        sec = section(self.packet("guide-a"), "1. ページ")
        self.assertIn("- level：（なし。この型は level を持たない）", sec)

    def test_linked_pages_with_title_summary_type_and_sections(self):
        sec = section(self.packet("sym-a"), "2. つながるページ")
        self.assertIn("- concept-a（basics／concept）お願いと鍵（試験用）：指示は Claude が読んで判断するお願いで", sec)
        self.assertRegex(sec, r"- 散らかっている\n  - feat-a（extend／feature）規則を CLAUDE\.md に置く（試験用）：CLAUDE\.md に規則を置いて")
        self.assertIn("  - concept-b#lock（basics／concept）位置の考え方（試験用） ― 節「置き場所の節」：", sec)
        self.assertRegex(sec, r"- 縛っていない\n  - feat-c（extend／feature）フックで止める（試験用）：")
        self.assertIn("  - ghost-page（ページがない）", sec)
        self.assertIn("- concept-b#nope（basics／concept）位置の考え方（試験用） ― 節 nope は sections にない：", sec)
        self.assertIn("- feat-c#lock（extend／feature）フックで止める（試験用） ― 節「止め方」：", sec)
        none = section(self.packet("lonely"), "2. つながるページ")
        self.assertEqual(none.count("- （なし）"), 3)

    def test_linked_pages_list_the_anchors_that_can_be_pointed_at(self):
        sec = section(self.packet("sym-a"), "2. つながるページ")
        self.assertIn("### 指せる節（link の目印は `id#anchor`", sec)
        self.assertIn("concept-b#lock（置き場所の節）", sec)
        self.assertIn("feat-c#lock（止め方）", sec)
        self.assertEqual(sec.count("- feat-c：") + sec.count("- concept-b："), 2)   # ページごとに1行
        self.assertNotIn("### 指せる節", section(self.packet("lonely"), "2. つながるページ"))

    def test_catalog_section(self):
        sec = section(self.packet("sym-a"), "3. 目次の情報")
        for want in ("planning/catalog/symptoms.yaml", "- level の根拠（level_evidence）：規則を書き始めた段階で最初に出会う",
                     "  - 規則を hook に移す例（kind：hook、safety：False）", "  - 頼み方の例（kind：prompt、safety：True）",
                     "- 図の案（visual）：static：お願いと鍵の二層の図", "- 備考（notes）：\n  備考の一行目。\n  備考の二行目。",
                     "  1. 00 §3 分野18", "  2. research/23 §3.1・§3.99（注意）", "  4. research/99 §1"):
            self.assertIn(want, sec)
        self.assertIn("目次（planning/catalog/）に lonely の項目がない", section(self.packet("lonely"), "3. 目次の情報"))
        self.assertIn("- 材料（materials。写しは 6）：（なし）", section(self.packet("concept-a"), "3. 目次の情報"))

    def test_data_section_has_features_advice_and_names(self):
        sec = section(self.packet("sym-a"), "4. data")
        self.assertIn("- id: claude-md\n  title: CLAUDE.md", sec)
        self.assertIn("note: 試験用の機能の注。", sec)
        self.assertNotIn("  match_terms:", sec)                       # 道具だけが使うキーは省く
        self.assertNotIn("/init", sec)
        self.assertIn("- id: old-tip\n  title: 昔の小技", sec)
        self.assertIn("how_to_find: 記事で探す。", sec)
        self.assertIn("- id: old-to-new", sec)                        # tracks の機能の names
        self.assertIn("- id: via-advice-name", sec)                    # 台帳の行の name
        self.assertEqual(sec.count("- id: old-to-new"), 1)
        none = section(self.packet("lonely"), "4. data")
        self.assertIn("（tracks なし）", none)
        self.assertIn("（outdated_advice なし）", none)

    def test_a_ledger_page_gets_the_index_of_every_ledger_row(self):
        self.replace("stubs/extend/lonely.md", "type: feature", "type: ledger")
        sec = section(self.packet("lonely"), "4. data")
        self.assertIn("### 台帳の全行の一覧", sec)
        self.assertIn("- old-tip｜置換｜2026-01-09（2.1.3）｜昔の小技", sec)
        self.assertNotIn("### 台帳の全行の一覧", section(self.packet("sym-a"), "4. data"))        # ほかの型には付けない

    def test_data_section_says_when_the_data_item_is_missing(self):
        self.replace("stubs/extend/lonely.md", "prerequisites: []", "prerequisites: []\ntracks: [no-such-feature]\noutdated_advice: [no-such-advice]")
        sec = section(self.packet("lonely"), "4. data")
        self.assertIn("- no-such-feature：data/facts.yml の features にない", sec)
        self.assertIn("- no-such-advice：data/outdated-advice.yml の advice にない", sec)

    def test_sources_section(self):
        sec = section(self.packet("sym-a"), "5. 出典の一覧")
        self.assertIn("- src-memory｜公式文書｜メモリの文書｜https://docs.example.com/memory", sec)
        self.assertIn("- src-noai｜実践者｜断るサイトの記事｜https://noai.example.org/post｜AI の利用を断るドメイン。開かない", sec)
        self.assertIn("- src-missing｜（data/sources.yml にない）", sec)
        extra = sec.split("data の項目（4）が挙げている出典")[1]
        self.assertIn("src-blog", extra)
        self.assertIn("src-changelog", extra)
        self.assertNotIn("src-memory", extra)                         # 上の一覧にあるものは重ねない
        self.assertIn("一覧なし（planning/batches/step6/data/wave1-sources.yml にこのページがない）", section(self.packet("lonely"), "5. 出典の一覧"))
        self.assertIn("- （空）", section(self.packet("concept-a"), "5. 出典の一覧"))
        doc = section(self.packet("doc-page"), "5. 出典の一覧")
        self.assertIn("front matter の sources", doc)
        self.assertIn("- src-memory｜公式文書", doc)

    def test_materials_section_found_not_found_and_out_of_scope(self):
        sec = section(self.packet("sym-a"), "6. 材料の抜き出し")
        self.assertIn("### 6.1 00 §3 分野18", sec)
        self.assertRegex(sec, r"出典：planning/research/00-content-report\.md の \d+〜\d+ 行（分野18 症状辞典（20ページ））｜")
        self.assertIn("※ 全文（", sec)
        self.assertIn("【2026-11-03 訂正】熟練度の差の文を直した。", sec)
        self.assertIn("本文 3.1。", sec)
        self.assertIn("見つからない：research/23 §3.1・§3.99（注意）（§3.99 が見つからない）", sec)
        self.assertIn("対象外：kyopro-atlas の docs/guide/x.md（手本）（調査資料でも計画の資料でもない。束に写さない）", sec)
        self.assertIn("見つからない：research/99 §1（planning/research/99-*.md がない）", sec)
        self.assertEqual(len(re.findall(r"^見つからない：", sec, re.M)), 2)
        self.assertEqual(len(re.findall(r"^対象外：", sec, re.M)), 1)

    def test_a_page_without_materials_says_so(self):
        self.assertIn("目次の materials がない（写す材料なし）", section(self.packet("concept-a"), "6. 材料の抜き出し"))
        self.assertIn("目次の materials がない（写す材料なし）", section(self.packet("lonely"), "6. 材料の抜き出し"))

    def test_type_musts_section_copies_guide_sections(self):
        sec = section(self.packet("concept-a"), "1b. 型の必ず持つもの")
        guide = self.read("planning/guides/concept.md")
        for num in ("1", "2"):
            m = re.search(rf"^## {num}\. .*?(?=^## |\Z)", guide, flags=re.M | re.S)
            self.assertIsNotNone(m)
            self.assertIn("#" + m.group(0).rstrip(), sec)
        self.assertNotIn("## 3.", sec)

    def test_a_hosting_page_gets_its_gen_marks_and_others_do_not(self):
        sec = section(self.packet("concept-a"), "1. ページ")
        self.assertIn("`<!-- gen:begin causes -->`〜`<!-- gen:end causes -->` を置く。中身は道具が書くので、手で表を書かない", sec)
        self.assertIn("card §9：症状の原因別の表", sec)
        self.assertIn("gen:begin signs symptom -->`〜`<!-- gen:end signs symptom -->", sec)
        self.assertIn("card §9：逆引き・ロードマップ", sec)
        self.assertIn("gen:begin nowhere", sec)
        self.assertIn("に説明の行がない", sec)
        self.assertNotIn("gen:begin", section(self.packet("lonely"), "1. ページ"))

    def test_a_word_after_a_section_is_searched_in_the_enclosing_section_first(self):
        self.write("planning/research/05-failures.md", "# 05\n\n## 1. 一\n\n### Inferences\n- 一の推論\n\n"
                   "## 3. 三\n\n#### 3-5. 五\n本文五\n\n#### 3-6. 六\n本文六\n\n### Inferences\n- 三の推論\n")
        it = self.resolve("05 §3-5（五の話）と Inferences")
        self.assertEqual(it.status, "ok")
        text = item_text(it)
        self.assertIn("三の推論", text)
        self.assertNotIn("一の推論", text)

    def test_type_musts_section_for_a_type_without_guide(self):
        sec = section(self.packet("feat-a"), "1b. 型の必ず持つもの")
        self.assertEqual(sec.rstrip().split("\n")[2:], ["この型の手引きはない"])

    def test_guides_section_names_the_two_guides_and_the_report_place(self):
        sec = section(self.packet("sym-a"), "7. 書き方")
        self.assertIn("planning/guides/card.md", sec)
        self.assertIn("planning/guides/common.md", sec)
        self.assertIn("planning/guides/symptom.md", sec)
        self.assertIn("報告の置き場所：指示に従う", sec)
        self.assertNotIn("まだない", sec)
        self.assertIn("planning/guides/feature.md（まだない）", section(self.packet("feat-a"), "7. 書き方"))

    def test_a_page_in_docs_gets_a_packet(self):
        text = self.packet("doc-page")
        self.assertIn("- stage：draft　ファイル：docs/extend/doc-page.md", text)
        self.assertIn("- sources（front matter）：src-memory", text)

    def test_the_same_place_is_not_copied_twice(self):
        self.replace("planning/catalog/symptoms.yaml", '      - "research/99 §1"', '      - "research/23 §3.1（もう一度）"')
        sec = section(self.packet("sym-a"), "6. 材料の抜き出し")
        self.assertEqual(sec.count("本文 3.1。"), 1)
        self.assertIn("（6.2 に写したのと同じ所）", sec)

    def test_unchanged_packet_is_not_rewritten(self):
        self.packet("sym-a")
        path = self.root / "state/packets/sym-a.md"
        before = path.stat().st_mtime_ns
        self.packet("sym-a")
        self.assertEqual(path.stat().st_mtime_ns, before)

    def test_missing_catalog_data_and_research_do_not_stop_the_tool(self):
        shutil.rmtree(self.root / "planning" / "catalog")
        shutil.rmtree(self.root / "planning" / "research")
        shutil.rmtree(self.root / "data")
        text = self.packet("sym-a")
        self.assertIn("目次（planning/catalog/）に sym-a の項目がない", text)
        self.assertIn("- claude-md：data/facts.yml の features にない", text)
        self.assertIn("- old-tip：data/outdated-advice.yml の advice にない", text)

    def test_packets_are_deterministic(self):
        first = self.packet("sym-a")
        self.assertEqual(self.packet("sym-a"), first)

    # ---- 上限

    def long_research(self) -> None:
        paras = [f"段落{i}：" + "あ" * 240 for i in range(14)]
        paras[10] = "> 【2026-11-03 注記】この節の十一番目の段落は直した。" + "い" * 60
        self.write("planning/research/28-long.md", "# 長い資料\n\n## 1. 長い節\n\n" + "\n\n".join(paras) + "\n\n## 2. 次の節\n\n次の節の本文。\n")
        self.replace("planning/catalog/symptoms.yaml", '      - "research/99 §1"', '      - "28 §1（長い節）"')

    def test_a_long_section_is_cut_and_the_mark_stays(self):
        self.long_research()
        sec = section(self.packet("sym-a", "--item-limit", "900"), "6. 材料の抜き出し")
        piece = sec.split("### 6.4 ")[1]
        self.assertIn("※ 全 ", piece)
        self.assertIn("切った所は「…（略）」", piece)
        self.assertRegex(piece, r"出典：planning/research/28-long\.md の 3〜\d+ 行")
        self.assertIn("段落0：", piece)
        self.assertNotIn("段落13：", piece)
        self.assertIn("【2026-11-03 注記】この節の十一番目の段落は直した。", piece)
        self.assertIn("…（略）", piece)
        self.assertNotIn("次の節の本文", piece)
        body = re.search(r"````\n(.*?)\n````", piece, re.S).group(1)
        self.assertLessEqual(len(body), 900 + 120)

    def test_item_limit_changes_how_much_is_copied(self):
        self.long_research()
        small = section(self.packet("sym-a", "--item-limit", "600"), "6. 材料の抜き出し")
        large = section(self.packet("sym-a", "--item-limit", "6000"), "6. 材料の抜き出し")
        self.assertLess(len(small), len(large))
        self.assertIn("段落13：", large)
        self.assertIn("1項目あたり最大 600 字", small)

    def test_hint_in_the_note_chooses_the_paragraph_to_copy(self):
        self.long_research()
        self.write("planning/research/28-long.md", self.read("planning/research/28-long.md").replace("段落7：", "段落7：マーカー語の説明。"))
        self.replace("planning/catalog/symptoms.yaml", "28 §1（長い節）", "28 §1（マーカー語）")
        sec = section(self.packet("sym-a", "--item-limit", "900"), "6. 材料の抜き出し")
        self.assertIn("段落7：マーカー語の説明。", sec)

    def test_a_packet_over_the_limit_lowers_the_item_limit(self):
        self.long_research()
        code, out, err = self.run_tool("sym-a", "--stats", "--packet-limit", "100000")
        self.assertEqual(code, 0)
        self.assertNotIn("下げた", out)
        big = self.read("state/packets/sym-a.md")
        code, out, err = self.run_tool("sym-a", "--stats", "--packet-limit", str(len(big) - 400))
        self.assertEqual(code, 0, err)
        small = self.read("state/packets/sym-a.md")
        self.assertLess(len(small), len(big))
        self.assertRegex(out, r"上限を 3000 字から \d+ 字に下げた")
        self.assertIn("1項目あたり最大", small)
        # 下限まで下げても収まらないときは、超えていると書く
        code, out, _ = self.run_tool("sym-a", "--stats", "--packet-limit", "500")
        self.assertIn("500 字を超えている", out)
        self.assertIn(f"1項目 {mp.MIN_ITEM_LIMIT} 字", out)

    # ---- 呼び出し

    def test_stats_prints_the_size_and_the_counts(self):
        code, out, err = self.run_tool("sym-a", "lonely", "--stats")
        self.assertEqual(code, 0, err)
        size = len(self.read("state/packets/sym-a.md"))
        self.assertIn(f"sym-a: {size} 字（", out)
        self.assertRegex(out, r"sym-a: \d+ 字（\d+／\d+／\d+／\d+／\d+／\d+／\d+／\d+）｜材料 4 項目（見つかった 1・一部 1・見つからない 1・対象外 1・切った写し 0）｜1項目 3000 字")
        self.assertIn("lonely:", out)
        self.assertRegex(out, r"計 2 束：最小 \d+・最大 \d+・合計 \d+ 字｜見つからない 1・一部 1・対象外 1")
        code, out, _ = self.run_tool("sym-a")
        self.assertNotIn("字（", out)

    def test_unknown_id_is_reported_and_the_others_are_made(self):
        code, out, err = self.run_tool("sym-a", "no-such-page")
        self.assertEqual(code, 1)
        self.assertIn("ページがない: no-such-page", err)
        self.assertTrue((self.root / "state/packets/sym-a.md").is_file())
        self.assertFalse((self.root / "state/packets/no-such-page.md").exists())

    def test_no_argument_is_a_usage_error_and_a_missing_site_yml_cannot_be_read(self):
        code, out, err = self.run_tool()
        self.assertEqual(code, 2)
        self.assertIn("ページの id か --wave1 か --all", err)
        (self.root / "schema/site.yml").unlink()
        code, out, err = self.run_tool("sym-a")
        self.assertEqual(code, 2)
        self.assertIn("読めない", err)

    def test_out_dir(self):
        out_dir = Path(self._tmp.name) / "elsewhere"
        code, out, err = self.run_tool("sym-a", "--out", str(out_dir))
        self.assertEqual(code, 0, err)
        self.assertTrue((out_dir / "sym-a.md").is_file())
        self.assertFalse((self.root / "state").exists())

    def test_an_output_place_that_cannot_be_made_stops_with_2(self):
        blocker = Path(self._tmp.name) / "blocker"
        blocker.write_text("ファイル", encoding="utf-8")                       # フォルダにできない
        code, out, err = self.run_tool("sym-a", "--out", str(blocker / "packets"))
        self.assertEqual(code, 2)
        self.assertIn("書けない", err)

    def test_wave1_is_the_closure_of_the_core_the_routes_and_the_named(self):
        ids = mp.first_wave_ids(mp.Builder(self.root).atlas)
        # 核（wave: 1）の guide-a・concept-a・sym-a、sym-a の routes の最初の必須の先 feat-a、named の named-page、
        # その前提でたどって届く concept-b。feat-c（推奨）は routes の2つ目の cause の先だが必須でないので入らない
        self.assertEqual(ids, ["guide-a", "concept-a", "concept-b", "feat-a", "named-page", "sym-a"])      # ナビゲーションの順
        code, out, err = self.run_tool("--wave1")
        self.assertEqual(code, 0, err)
        self.assertEqual(sorted(p.name for p in (self.root / "state/packets").iterdir()), sorted(f"{i}.md" for i in ids))

    def test_wave1_counting_follows_site_yml(self):
        self.replace("schema/site.yml", "routes: first", "routes: all")
        ids = mp.first_wave_ids(mp.Builder(self.root).atlas)
        self.assertIn("feat-c", ids)
        self.assertNotIn("ghost-page", ids)
        self.replace("schema/site.yml", "routes: all", "routes: none")
        ids = mp.first_wave_ids(mp.Builder(self.root).atlas)
        self.assertNotIn("feat-a", ids)
        self.assertNotIn("feat-c", ids)
        self.assertIn("named-page", ids)

    def test_all_makes_every_page(self):
        code, out, err = self.run_tool("--all")
        self.assertEqual(code, 0, err)
        names = sorted(p.stem for p in (self.root / "state/packets").iterdir())
        self.assertEqual(names, ["concept-a", "concept-b", "doc-page", "feat-a", "feat-c", "guide-a", "lonely", "named-page", "sym-a"])

    def test_an_id_given_twice_or_with_wave1_is_made_once(self):
        code, out, err = self.run_tool("sym-a", "sym-a", "--wave1", "--stats")
        self.assertEqual(code, 0, err)
        self.assertEqual(out.count("  sym-a:"), 1)


# ---------------------------------------------------------------- 本物のリポジトリ（読むだけ）


class RealRepoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not (REPO / "planning" / "research").is_dir() or not (REPO / "planning" / "catalog").is_dir():
            raise unittest.SkipTest("本物の planning/ がない")
        cls.builder = mp.Builder(REPO)

    def test_wave1_is_the_same_closure_as_check_catalog(self):
        try:
            import check_catalog
        except ImportError:                       # check_catalog.py が退いたあとは、この比べ方をやめる
            self.skipTest("tools/check_catalog.py がない")
        cat = check_catalog.load_catalog(REPO)
        theirs = {p.id for p in check_catalog.first_wave(cat).pages}
        mine = mp.first_wave_ids(self.builder.atlas)
        self.assertEqual(set(mine), theirs)
        self.assertEqual(len(mine), len(set(mine)))

    def test_the_ten_prototype_pages_make_packets_within_the_limit(self):
        for pid in TEN_PAGES:
            if pid not in self.builder.atlas.by_id:
                self.skipTest(f"{pid} がない")
            pk = self.builder.packet(pid, mp.ITEM_LIMIT, mp.PACKET_LIMIT)
            self.assertIsNotNone(pk, pid)
            self.assertEqual(re.findall(r"^## (\d)\. ", outside_fences(pk.text), re.M), list("1234567"), pid)
            self.assertLessEqual(pk.chars, mp.PACKET_LIMIT, pid)
            self.assertIsNone(pk.lowered_from, pid)
            self.assertGreater(len(pk.items), 0, pid)
            self.assertGreater(sum(len(i.pieces) for i in pk.items), 0, pid)
            # 調査資料の印は、ほとんどがたどれる（たどれない項目は「見つからない：」に書かれる）
            self.assertLessEqual(pk.count("missing") + pk.count("partial"), 2, pid)
            self.assertEqual(len(re.findall(r"^見つからない：", pk.text, re.M)), pk.count("missing") + pk.count("partial"), pid)

    def test_a_note_in_the_research_keeps_its_mark_in_the_copy(self):
        pk = self.builder.packet("competition-rules", mp.ITEM_LIMIT, mp.PACKET_LIMIT)
        self.assertIn("【2026-11-03 注記】", pk.text)


if __name__ == "__main__":
    unittest.main()
