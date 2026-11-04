"""tools/check_page.py（1ページ分の検査をまとめて流し、指摘だけを短く出す）の試験。
`uv run python -m unittest discover -s tests/tools` で動く（Node と textlint は要らない）。

fixtures/checks/（エラーも警告も出ない置き場所）を一時フォルダに写し、本物の schema/ を足す。textlint は、決めた JSON を
返すだけの偽物を node_modules/.bin/textlint に置く。生成（gen_site.py）は、置き場所に mkdocs.yml がないので、
subprocess の受け渡しを差し替えて確かめる。
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
from unittest import mock

REPO = Path(__file__).resolve().parents[2]
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "checks"
sys.path.insert(0, str(REPO / "tools"))

import check_page  # noqa: E402
import textlint_targets as tt  # noqa: E402

II = "docs/symptoms/instructions-ignored.md"
HB = "stubs/enforce/hooks-basics.md"

FAKE_TEXTLINT = """\
#!/bin/sh
# 受け取った引数と、最初のファイルの中身（そのとき渡された写し）を書き出し、決めた JSON を返す。
# JSON の中の __FIRST__ は、最初のファイルのパス（写しのパス）に置き換える
d="$(dirname "$0")"
printf '%s\\n' "$@" > "$d/args.txt"
cp "$3" "$d/seen.md"
sed "s#__FIRST__#$3#" "$d/result.json"
exit 1
"""


class PageCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "repo"
        shutil.copytree(FIXTURE, self.root)
        shutil.copytree(REPO / "schema", self.root / "schema")
        self.bin = self.root / "node_modules" / ".bin"
        self.bin.mkdir(parents=True)
        exe = self.bin / "textlint"
        exe.write_text(FAKE_TEXTLINT, encoding="utf-8")
        exe.chmod(0o755)
        self.lint([])

    def tearDown(self):
        self._tmp.cleanup()

    def lint(self, messages: list[dict], rel: str = II):
        result = [{"filePath": str(self.root / rel), "messages": messages}]
        (self.bin / "result.json").write_text(json.dumps(result), encoding="utf-8")

    def lint_args(self) -> list[str]:
        return (self.bin / "args.txt").read_text(encoding="utf-8").split()

    def replace(self, rel: str, old: str, new: str):
        p = self.root / rel
        text = p.read_text(encoding="utf-8")
        self.assertIn(old, text)
        p.write_text(text.replace(old, new, 1), encoding="utf-8")

    def run_cli(self, *args: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = check_page.main(["--root", str(self.root), "--no-gen", *args])
        return code, out.getvalue(), err.getvalue()


class TestRun(PageCase):
    def test_a_clean_page_says_only_the_count(self):
        code, out, _ = self.run_cli("instructions-ignored")
        self.assertEqual((code, out), (0, "エラー 0・警告 0\n"))

    def test_textlint_runs_on_that_page_file_only(self):
        self.run_cli("instructions-ignored")
        args = self.lint_args()
        self.assertEqual(args[:2], ["-f", "json"])
        self.assertEqual(len(args), 3)
        self.assertTrue(args[2].endswith("/" + II))      # 目印のあるページは写し（下の試験）を渡す

    def test_textlint_findings_are_one_line_each(self):
        self.lint([{"line": 12, "column": 3, "ruleId": "prh", "severity": 2, "message": "表記が違う\n直す"},
                   {"line": 20, "column": 1, "ruleId": "ja-technical-writing/sentence-length", "severity": 1, "message": "長い"}])
        code, out, _ = self.run_cli("instructions-ignored")
        lines = out.splitlines()
        self.assertEqual(code, 1)
        self.assertEqual(lines[0], f"エラー {II}:12:3 [textlint:prh] 表記が違う 直す")
        self.assertEqual(lines[1], f"警告 {II}:20:1 [textlint:ja-technical-writing/sentence-length] 長い")
        self.assertEqual(lines[-1], "エラー 1・警告 1")
        self.assertEqual(len(lines), 3)

    def test_check_pages_findings_are_listed_and_decide_the_exit_code(self):
        self.replace(II, "prerequisites: [request-vs-lock]", "prerequisites: [no-such-page]")     # ない id を指させる
        code, out, _ = self.run_cli("instructions-ignored")
        lines = out.splitlines()
        self.assertEqual(code, 1)
        self.assertRegex(lines[0], r"^エラー docs/symptoms/instructions-ignored\.md(:\d+)? \[[^\]]+\] ")
        self.assertRegex(lines[-1], r"^エラー [1-9]\d*・警告 \d+$")

    def test_errors_come_before_warnings_and_the_limit_cuts_the_rest(self):
        msgs = [{"line": n, "column": 1, "ruleId": "r", "severity": 1, "message": f"警告{n}"} for n in range(1, 6)]
        msgs.append({"line": 99, "column": 1, "ruleId": "r", "severity": 2, "message": "誤り"})
        self.lint(msgs)
        code, out, _ = self.run_cli("instructions-ignored", "--limit", "3")
        lines = out.splitlines()
        self.assertEqual(code, 1)
        self.assertIn("誤り", lines[0])
        self.assertTrue(lines[1].startswith("警告 ") and lines[2].startswith("警告 "))     # 誤り1 + 警告2
        self.assertIn("ほか 3 件は上限 3 件で省略", lines[3])
        self.assertEqual(lines[-1], "エラー 1・警告 5")

    def test_zero_limit_shows_everything(self):
        self.lint([{"line": n, "column": 1, "ruleId": "r", "severity": 1, "message": "x"} for n in range(1, 40)])
        _, out, _ = self.run_cli("instructions-ignored", "--limit", "0")
        self.assertEqual(len(out.splitlines()), 40)
        self.assertNotIn("省略", out)

    def test_a_long_message_is_cut(self):
        self.lint([{"line": 1, "column": 1, "ruleId": "r", "severity": 1, "message": "あ" * 400}])
        _, out, _ = self.run_cli("instructions-ignored")
        self.assertLessEqual(len(out.splitlines()[0]), check_page.MESSAGE_WIDTH + 1)
        self.assertIn("…", out.splitlines()[0])

    def test_a_stub_page_is_not_given_to_textlint(self):
        code, out, _ = self.run_cli("hooks-basics")
        self.assertEqual(code, 0)
        self.assertIn("textlint は対象外：stubs/enforce/hooks-basics.md", out)
        self.assertFalse((self.bin / "args.txt").exists())     # 対象がなければ textlint を呼ばない

    def test_several_pages_are_checked_in_one_run(self):
        self.run_cli("instructions-ignored", "request-vs-lock")
        self.assertEqual(self.lint_args()[:2], ["-f", "json"])
        self.assertTrue(any(a.endswith("/" + II) for a in self.lint_args()))
        self.assertTrue(any(a.endswith("/docs/basics/request-vs-lock.md") for a in self.lint_args()))

    def test_unknown_page_cannot_be_checked(self):
        code, out, err = self.run_cli("no-such-page")
        self.assertEqual(code, 2)
        self.assertIn("「no-such-page」のページが docs/ にも stubs/ にもない", err)
        self.assertEqual(out, "")

    def test_missing_textlint_cannot_be_checked(self):
        (self.bin / "textlint").unlink()
        code, _, err = self.run_cli("instructions-ignored")
        self.assertEqual(code, 2)
        self.assertIn("textlint がない", err)


class TestMask(PageCase):
    """生成の目印の間は、textlint_targets.py --run と同じく、写しに textlint-disable を足して検査から外す。"""

    def test_textlint_gets_a_copy_with_the_marker_spans_disabled(self):
        self.run_cli("instructions-ignored")
        seen = (self.bin / "seen.md").read_text(encoding="utf-8")
        original = (self.root / II).read_text(encoding="utf-8")
        self.assertEqual(seen, tt.mask_generated(original))
        self.assertIn("<!-- textlint-disable -->", seen)
        self.assertEqual(seen.count("\n"), original.count("\n"))     # 行番号は変わらない

    def test_the_original_page_is_untouched_and_the_copy_is_removed(self):
        before = (self.root / II).read_text(encoding="utf-8")
        self.run_cli("instructions-ignored")
        self.assertEqual((self.root / II).read_text(encoding="utf-8"), before)
        self.assertEqual([p.name for p in self.root.iterdir() if p.name.startswith(".textlint-mask-")], [])

    def test_the_copy_is_removed_even_when_textlint_output_is_unreadable(self):
        (self.bin / "result.json").write_text("not json", encoding="utf-8")
        code, _, err = self.run_cli("instructions-ignored")
        self.assertEqual(code, 2)
        self.assertEqual([p.name for p in self.root.iterdir() if p.name.startswith(".textlint-mask-")], [])

    def test_findings_in_the_copy_are_reported_at_the_original_page(self):
        result = [{"filePath": "__FIRST__", "messages": [{"line": 7, "column": 2, "ruleId": "r", "severity": 1, "message": "指摘"}]}]
        (self.bin / "result.json").write_text(json.dumps(result), encoding="utf-8")
        _, out, _ = self.run_cli("instructions-ignored")
        self.assertEqual(out.splitlines()[0], f"警告 {II}:7:2 [textlint:r] 指摘")
        self.assertNotIn(".textlint-mask-", out)

    def test_a_page_without_markers_is_given_as_is(self):
        plain = self.root / "docs" / "plain.md"
        plain.write_text("# 題\n\n本文である。\n", encoding="utf-8")
        (self.bin / "result.json").write_text(json.dumps(
            [{"filePath": str(plain), "messages": [{"line": 3, "column": 1, "ruleId": "r", "severity": 2, "message": "誤り"}]}]), encoding="utf-8")
        issues = check_page.run_textlint(self.root, [Path("docs/plain.md")])
        self.assertEqual(self.lint_args(), ["-f", "json", plain.as_posix()])     # 写さない
        self.assertEqual([(i.severity, i.where) for i in issues], [("エラー", "docs/plain.md:3:1")])


REAL_TEXTLINT = REPO / "node_modules" / ".bin" / "textlint"


@unittest.skipUnless(REAL_TEXTLINT.exists(), "textlint がない（npm ci を流すと動く）")
class TestMaskWithRealTextlint(unittest.TestCase):
    """本物の textlint で、目印の間の「四つ」は指摘されず、目印の外の「四つ」は指摘される。"""

    def test_marker_spans_are_exempt_and_outside_is_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            (root / "docs").mkdir(parents=True)
            for name in (".textlintrc.json", "prh.yml"):
                shutil.copy(REPO / name, root / name)
            (root / "node_modules").symlink_to(REPO / "node_modules", target_is_directory=True)
            (root / "docs" / "x.md").write_text(
                "# 題\n\n<!-- gen:begin foo -->\n## 四つの具体性\n<!-- gen:end foo -->\n\n"
                "四つの点を書く。\n\n名は <!-- name:begin n1 -->四つ目<!-- name:end --> である。\n", encoding="utf-8")
            issues = check_page.run_textlint(root, [Path("docs/x.md")])
        arabic = [i for i in issues if "arabic-kanji-numbers" in i.text]
        self.assertEqual([i.where for i in arabic], ["docs/x.md:7:1"])         # 目印の外の1件だけ（4 行目と 9 行目は外れる）


class TestGen(PageCase):
    def done(self, code: int, out: str = "", err: str = ""):
        return mock.Mock(returncode=code, stdout=out, stderr=err)

    def test_gen_runs_first_with_the_page_flag_and_notices_become_warnings(self):
        calls = []
        real = check_page.run

        def fake(cmd, root):
            if cmd[1].endswith("gen_site.py"):
                calls.append(cmd)
                return self.done(0, "注意: 知らない生成の部分 foo\n書いた: 0 ファイル\n")
            return real(cmd, root)

        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(check_page, "run", fake), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = check_page.main(["--root", str(self.root), "instructions-ignored"])
        self.assertEqual(code, 0)
        self.assertEqual(calls[0][-2:], ["--page", "instructions-ignored"])
        self.assertEqual(out.getvalue().splitlines(), ["警告 [gen_site] 知らない生成の部分 foo", "エラー 0・警告 1"])

    def test_no_gen_skips_it(self):
        with mock.patch.object(check_page, "run_gen", side_effect=AssertionError("流さない")):
            code, _, _ = self.run_cli("instructions-ignored")
        self.assertEqual(code, 0)

    def test_a_failing_gen_cannot_be_checked(self):
        def fake(cmd, root):
            return self.done(2, "", "読めない: 壊れている\n")

        err = io.StringIO()
        with mock.patch.object(check_page, "run", fake), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            code = check_page.main(["--root", str(self.root), "instructions-ignored"])
        self.assertEqual(code, 2)
        self.assertIn("gen_site.py --page instructions-ignored が失敗した", err.getvalue())


if __name__ == "__main__":
    unittest.main()
