"""tools/check_templates.py（雛形の静的な検査。検査は tools/checks/templates.py）の試験。
`uv run python -m unittest discover -s tests/tools` で動く。

fixtures/checks/ を一時フォルダに写し（本物の schema/ を足す）、snippets/ に試験用の雛形を置いて、出るはずの指摘だけが
出ることを確かめる。本物のリポジトリの .claude/settings.json が許す一覧に通ることも見る。
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
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "checks"
sys.path.insert(0, str(REPO / "tools"))

import check_templates  # noqa: E402
from checks import ERROR, TEMPLATES, WARNING, checks_for, load_context, run_checks  # noqa: E402
from checks.templates import load_keys, settings_problems  # noqa: E402

COVERED: set[str] = set()


def covers(*names: str):
    COVERED.update(names)
    return lambda func: func


GOOD_SETTINGS = {
    "$schema": "https://json.schemastore.org/claude-code-settings.json",
    "permissions": {"deny": ["Read(./.env)", "Bash(git push *)"], "defaultMode": "default"},
    "hooks": {"PreToolUse": [{"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 x.py", "timeout": 10,
                                                             "onFailure": "block"}]}]},
    "sandbox": {"enabled": True, "failIfUnavailable": True},
}


class TemplatesCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "repo"
        shutil.copytree(FIXTURE, self.root)
        shutil.copytree(REPO / "schema", self.root / "schema")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel: str, text) -> None:
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text if isinstance(text, str) else json.dumps(text, ensure_ascii=False, indent=2), encoding="utf-8")

    def issues(self):
        return [i for i in run_checks(load_context(self.root, TEMPLATES)) if i.check != "settings のスキーマ"]

    def assertFound(self, *expected: tuple[str, str]):
        issues = self.issues()
        got = sorted({(i.check, i.page) for i in issues})
        self.assertEqual(got, sorted(set(expected)), "\n" + "\n".join(f"{i.file}:{i.line} [{i.check}] {i.message}" for i in issues))
        return issues


class TestTemplates(TemplatesCase):
    def test_clean(self):
        self.write("snippets/hooks-basics/settings.json", GOOD_SETTINGS)
        self.write("snippets/hooks-basics/settings.expect.yaml", "place: project\n")
        self.write("snippets/hooks-basics/verified.yaml", "date: 2026-11-04\n")
        self.write("snippets/hooks-basics/review/SKILL.md", "---\nname: review\ndescription: 試験用のスキル\n---\n\n本文\n")
        self.write("snippets/hooks-basics/agents/checker.md", "---\nname: checker\ndescription: 試験用の担当\n---\n本文\n")
        self.write("snippets/hooks-basics/prompt.md", "試験用のプロンプトの型（front matter なし）\n")
        self.assertFound()

    def test_every_check_has_a_test(self):
        self.assertEqual(sorted({c.name for c in checks_for(TEMPLATES)} - COVERED), [])

    @covers("雛形の置き場所")
    def test_place(self):
        self.write("snippets/loose.json", "{}")
        self.write("snippets/no-such-page/a.json", "{}")
        self.assertFound(("雛形の置き場所", "-"), ("雛形の置き場所", "no-such-page"))

    @covers("雛形の形")
    def test_syntax(self):
        self.write("snippets/hooks-basics/a.json", "{ not json")
        self.write("snippets/hooks-basics/b.yaml", "a: [\n")
        self.write("snippets/hooks-basics/c.md", "---\nname: x\n")
        issues = self.assertFound(("雛形の形", "hooks-basics"))
        self.assertEqual(len(issues), 3)

    @covers("期待の形")
    def test_expectations(self):
        self.write("snippets/hooks-basics/settings.json", GOOD_SETTINGS)
        self.write("snippets/hooks-basics/orphan.expect.yaml", "place: project\n")
        self.write("snippets/hooks-basics/settings.expect.yaml", "- a list\n")
        issues = self.assertFound(("期待の形", "hooks-basics"))
        self.assertEqual(len(issues), 2)

    @covers("スキルの front matter")
    def test_skill_front_matter(self):
        self.write("snippets/hooks-basics/Bad_Name/SKILL.md", "---\nname: Bad_Name\n---\n本文\n")
        self.write("snippets/hooks-basics/other/SKILL.md", "---\nname: renamed\ndescription: 試験\n---\n")
        self.write("snippets/hooks-basics/SKILL.md", "本文だけ（front matter なし）\n")
        issues = self.assertFound(("スキルの front matter", "hooks-basics"))
        self.assertEqual(len(issues), 4)          # name の形・description なし・フォルダ名と違う・front matter なし

    @covers("サブエージェントの front matter")
    def test_subagent_front_matter(self):
        self.write("snippets/hooks-basics/agents/a.md", "---\nname: \"x:y\"\n---\n")
        self.write("snippets/hooks-basics/agents/b.md", "---\ndescription: 名前がない\n---\n")
        self.write("snippets/hooks-basics/notes.md", "---\ntitle: agents の外の文書は見ない\n---\n")
        issues = self.assertFound(("サブエージェントの front matter", "hooks-basics"))
        self.assertEqual(len(issues), 3)

    @covers("settings のキー")
    def test_settings_keys(self):
        bad = json.loads(json.dumps(GOOD_SETTINGS))
        bad["permisions"] = {}
        bad["hooks"]["PreToolUse"][0]["matcher"] = ["Bash"]
        bad["hooks"]["PreToolUse"][0]["hooks"][0].update(timeout=0, onFailure="stop", colour="red")
        bad["hooks"]["NoSuchEvent"] = []
        bad["permissions"]["deny"].append("Bash(git push")
        self.write("snippets/hooks-basics/local-settings.json", bad)
        issues = self.assertFound(("settings のキー", "hooks-basics"))
        msgs = " ".join(i.message for i in issues)
        for needle in ("permisions", "matcher", "timeout", "onFailure", "colour", "NoSuchEvent", "Bash(git push"):
            self.assertIn(needle, msgs)

    def test_own_settings_file_is_checked(self):
        self.write(".claude/settings.json", {"permissions": {"deny": []}, "hooks": {"PreToolUse": [{"hooks": []}]},
                                             "unknownTop": 1})
        self.assertFound(("settings のキー", "-"))
        self.write(".claude/settings.json", "{ broken")
        self.assertFound(("settings のキー", "-"))

    @covers("settings のスキーマ")
    def test_schema_copy(self):
        self.write("snippets/hooks-basics/settings.json", GOOD_SETTINGS)
        ctx = load_context(self.root, TEMPLATES)
        got = [i for i in run_checks(ctx) if i.check == "settings のスキーマ"]
        self.assertEqual([(i.severity, i.file) for i in got], [(WARNING, "schema/claude-code-settings.schema.json")])
        schema = {"$schema": "http://json-schema.org/draft-07/schema#", "type": "object",
                  "properties": {"permissions": {"type": "object", "additionalProperties": False,
                                                 "properties": {"deny": {"type": "array"}}}}}
        self.write("schema/claude-code-settings.schema.json", schema)
        got = [i for i in run_checks(load_context(self.root, TEMPLATES)) if i.check == "settings のスキーマ"]
        self.assertEqual({(i.severity, i.page) for i in got}, {(ERROR, "hooks-basics")})   # defaultMode を通さない写し
        self.assertTrue(all("permissions" in i.message for i in got))


class TestRealSettings(unittest.TestCase):
    def test_repository_settings_pass_the_allow_list(self):
        data = json.loads((REPO / ".claude" / "settings.json").read_text(encoding="utf-8"))
        self.assertEqual(list(settings_problems(data, load_keys())), [])

    def test_allow_list_shape(self):
        keys = load_keys()
        for k in ("top", "permissions", "sandbox", "hook_events", "hook_entry", "hook", "on_failure"):
            self.assertIsInstance(keys.get(k), list, k)
            self.assertEqual(len(keys[k]), len(set(keys[k])), k)

    def test_cli(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = check_templates.main([])
        self.assertEqual(code, 0, out.getvalue())
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(err):
            self.assertEqual(check_templates.main(["--page", "no-such-page"]), 2)
            self.assertEqual(check_templates.main(["--list"]), 0)


if __name__ == "__main__":
    unittest.main()
