"""tools/textlint_targets.py（textlint の対象の一覧と、--run の受け渡し）の試験。
uv run python -m unittest discover -s tests/tools で動く（Node と textlint は要らない）。

一時フォルダに schema/site.yml と docs/ を作り、一覧に入るもの・除くものを確かめる。
--run の試験は、node_modules/.bin/textlint の場所に、受け取った引数を書き出すだけの偽の textlint を置く。
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TOOL = REPO / "tools" / "textlint_targets.py"
sys.path.insert(0, str(REPO / "tools"))
import textlint_targets as tt  # noqa: E402

SITE_YML = """\
fields:
  - {id: start, title: 入口と地図}
  - {id: symptoms, title: 症状辞典}
stages: [stub, draft, reviewed, done]
"""

FAKE_TEXTLINT = """\
#!/bin/sh
printf '%s\\n' "$@" > "$(dirname "$0")/args.txt"
exit "${FAKE_TEXTLINT_EXIT:-0}"
"""


def page(stage: str | None) -> str:
    lines = ["---", "id: sample", "title: 試しのページ"]
    if stage is not None:
        lines.append(f"stage: {stage}")
    return "\n".join(lines + ["---", "", "本文である。", ""])


class TargetsCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write("schema/site.yml", SITE_YML)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, rel: str, text: str) -> Path:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def listed(self) -> list[str]:
        return [p.as_posix() for p in tt.targets(self.root)]

    def cli(self, *args: str, env: dict | None = None) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(TOOL), "--root", str(self.root), *args],
                              capture_output=True, text=True, env=env)


class TestTargets(TargetsCase):
    def test_handwritten_pages_are_listed_and_stub_and_generated_files_are_not(self):
        self.write("docs/index.md", "# トップ\n\n手書きのトップである。\n")          # front matter なし
        self.write("docs/start/how-to-use.md", page("draft"))
        self.write("docs/start/glossary.md", page("stub"))                       # 骨格
        self.write("docs/symptoms/instructions-ignored.md", page("reviewed"))
        self.write("docs/symptoms/done-but-not-done.md", page("done"))
        self.write("docs/start/index.md", "# 入口と地図\n")                     # 分野の入口（生成）
        self.write("docs/lists/by-level.md", "# レベル別\n")                     # 生成した一覧
        self.write("docs/lists/sub/by-scene.md", "# 場面別\n")
        self.assertEqual(self.listed(), [
            "docs/index.md",
            "docs/start/how-to-use.md",
            "docs/symptoms/done-but-not-done.md",
            "docs/symptoms/instructions-ignored.md",
        ])

    def test_skeleton_stage_is_the_first_of_site_yml_stages(self):
        # 段の名前を直書きしていないことを、名前を変えた site.yml で確かめる
        self.write("schema/site.yml", SITE_YML.replace("[stub, draft", "[skeleton, draft"))
        self.write("docs/start/a.md", page("skeleton"))
        self.write("docs/start/b.md", page("stub"))
        self.assertEqual(self.listed(), ["docs/start/b.md"])

    def test_field_entry_is_decided_by_site_yml_fields(self):
        self.write("docs/start/index.md", "# 生成\n")
        self.write("docs/notafield/index.md", "# 分野でないフォルダの index.md は手書きとみなす\n")
        self.write("docs/start/deeper/index.md", "# 2段より深い index.md も手書きとみなす\n")
        self.write("docs/lists.md", "# lists というファイル名は生成物のフォルダではない\n")
        self.assertEqual(self.listed(), ["docs/lists.md", "docs/notafield/index.md", "docs/start/deeper/index.md"])

    def test_pages_without_stage_or_with_broken_front_matter_are_listed(self):
        self.write("docs/start/no-stage.md", page(None))
        self.write("docs/start/empty.md", "---\n---\n\n本文である。\n")
        self.write("docs/start/broken.md", "---\nid: [broken\n---\n\n本文である。\n")
        self.write("docs/start/list.md", "---\n- a\n---\n\n本文である。\n")
        warnings: list[str] = []
        files = [p.as_posix() for p in tt.targets(self.root, warnings.append)]
        self.assertEqual(files, ["docs/start/broken.md", "docs/start/empty.md", "docs/start/list.md",
                                 "docs/start/no-stage.md"])
        self.assertEqual(len(warnings), 2)
        self.assertTrue(all(w.startswith("警告: docs/start/") for w in warnings), warnings)

    def test_no_docs_dir_gives_empty_list(self):
        self.assertEqual(self.listed(), [])


class TestCli(TargetsCase):
    def test_prints_one_relative_path_per_line(self):
        self.write("docs/start/b.md", page("draft"))
        self.write("docs/start/a.md", page("draft"))
        done = self.cli()
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(done.stdout.splitlines(), ["docs/start/a.md", "docs/start/b.md"])

    def test_cannot_check_without_site_yml(self):
        (self.root / "schema/site.yml").unlink()
        done = self.cli()
        self.assertEqual(done.returncode, 2)
        self.assertIn("検査できない", done.stderr)
        self.assertEqual(done.stdout, "")

    def test_cannot_check_without_stages_or_fields(self):
        for text in ("fields:\n  - {id: start, title: 入口}\n", "stages: [stub, draft]\n", "- a\n", "fields: [\n"):
            with self.subTest(site_yml=text):
                self.write("schema/site.yml", text)
                self.assertEqual(self.cli().returncode, 2)

    def test_extra_arguments_need_run(self):
        done = self.cli("--", "--fix")
        self.assertEqual(done.returncode, 2)


class TestRun(TargetsCase):
    def setUp(self) -> None:
        super().setUp()
        fake = self.write("node_modules/.bin/textlint", FAKE_TEXTLINT)
        fake.chmod(0o755)
        self.args_file = fake.parent / "args.txt"

    def test_passes_extra_arguments_and_targets_and_returns_textlint_exit_code(self):
        self.write("docs/index.md", "# トップ\n")
        self.write("docs/start/a.md", page("draft"))
        self.write("docs/start/b.md", page("stub"))
        env = dict(os.environ, FAKE_TEXTLINT_EXIT="1")
        done = self.cli("--run", "--", "--fix", "--format", "json", env=env)
        self.assertEqual(done.returncode, 1, done.stderr)
        self.assertEqual(self.args_file.read_text(encoding="utf-8").splitlines(),
                         ["--fix", "--format", "json", "docs/index.md", "docs/start/a.md"])

    def test_does_not_call_textlint_without_targets(self):
        self.write("docs/start/a.md", page("stub"))
        done = self.cli("--run")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn("対象がない", done.stderr)
        self.assertFalse(self.args_file.exists())

    def test_cannot_check_without_textlint(self):
        shutil.rmtree(self.root / "node_modules")
        self.write("docs/index.md", "# トップ\n")
        done = self.cli("--run")
        self.assertEqual(done.returncode, 2)
        self.assertIn("npm ci", done.stderr)


class TestMaskGenerated(unittest.TestCase):
    def test_marker_pairs_are_wrapped_in_textlint_disable_and_enable(self):
        text = ("前。<!-- link:begin a#b -->五つの題名<!-- link:end -->後。\n"
                "<!-- gen:begin table x -->\n| 表 |\n<!-- gen:end table x -->\n"
                "<!-- fact:begin f --> 値 <!-- fact:end -->\n")
        out = tt.mask_generated(text)
        self.assertEqual(out.count("<!-- textlint-disable -->"), 3)
        self.assertEqual(out.count("<!-- textlint-enable -->"), 3)
        self.assertIn("<!-- link:begin a#b --><!-- textlint-disable -->五つの題名<!-- textlint-enable --><!-- link:end -->", out)
        self.assertEqual(out.count("\n"), text.count("\n"))   # 行番号は変わらない
        self.assertTrue(tt.has_generated_marker(text))
        self.assertFalse(tt.has_generated_marker("普通の本文である。\n"))


class TestRunMasked(TargetsCase):
    """目印のあるページは、目印を足した写しで検査し、パスを元に戻す。"""

    def setUp(self) -> None:
        super().setUp()
        fake = self.write("node_modules/.bin/textlint", (
            "#!/bin/sh\n"
            'for a in "$@"; do case "$a" in docs/*|.textlint-mask-*) printf \'%s\\n\' "$a" >> "$(dirname "$0")/args.txt";'
            ' cp "$a" "$(dirname "$0")/seen-$(basename "$a")";; esac; done\n'
            'echo "$(pwd)/$(ls -d .textlint-mask-*/docs/start/a.md 2>/dev/null | head -1)  警告"\n'
            "exit 0\n"))
        fake.chmod(0o755)
        self.bin = fake.parent

    def test_page_with_markers_goes_through_masked_copy_and_is_removed_after(self):
        self.write("docs/start/a.md", "---\nid: a\ntitle: A\nstage: draft\n---\n\n"
                   "<!-- link:begin x -->五つ<!-- link:end -->\n")
        self.write("docs/start/b.md", page("draft"))
        done = self.cli("--run")
        self.assertEqual(done.returncode, 0, done.stderr)
        args = (self.bin / "args.txt").read_text(encoding="utf-8").splitlines()
        self.assertTrue(args[0].startswith(".textlint-mask-") and args[0].endswith("/docs/start/a.md"), args)
        self.assertEqual(args[1], "docs/start/b.md")
        seen = (self.bin / "seen-a.md").read_text(encoding="utf-8")
        self.assertIn("<!-- link:begin x --><!-- textlint-disable -->五つ<!-- textlint-enable --><!-- link:end -->", seen)
        self.assertIn(str(self.root / "docs/start/a.md"), done.stdout)   # 出力のパスは元のページ
        self.assertNotIn(".textlint-mask-", done.stdout)
        self.assertEqual([p.name for p in self.root.iterdir() if p.name.startswith(".textlint-mask-")], [])

    def test_fix_uses_original_files(self):
        self.write("docs/start/a.md", "---\nid: a\ntitle: A\nstage: draft\n---\n<!-- link:begin x -->y<!-- link:end -->\n")
        self.cli("--run", "--", "--fix")
        self.assertEqual((self.bin / "args.txt").read_text(encoding="utf-8").splitlines(), ["docs/start/a.md"])


class TestRealRepository(unittest.TestCase):
    def test_lists_existing_markdown_under_docs(self):
        done = subprocess.run([sys.executable, str(TOOL)], capture_output=True, text=True, cwd=REPO)
        self.assertEqual(done.returncode, 0, done.stderr)
        for line in done.stdout.splitlines():
            self.assertTrue(line.startswith("docs/") and line.endswith(".md"), line)
            self.assertTrue((REPO / line).is_file(), line)


if __name__ == "__main__":
    unittest.main()
