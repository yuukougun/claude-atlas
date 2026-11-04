"""tools/check_all.py（CI と同じ検査の組を流す入口）と .github/workflows/check.yml の試験。
`uv run python -m unittest discover -s tests/tools` で動く。段の中身は流さない（一時フォルダに偽の道具を置いて、
段の選び方・飛ばし方・終了コード・まとめを見る）。
"""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "tools"))

import check_all  # noqa: E402

DESIGN_STEPS = ["make_schema", "gen_site", "check_pages", "check_catalog", "check_templates", "check_svg", "textlint",
                "mkdocs", "tests-tools", "tests-site", "tests-hooks-python3", "tests-hooks", "tests-guides"]


class TestCheckAll(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "tools").mkdir()
        (self.root / "tools/make_schema.py").write_text("print('最新')\n", encoding="utf-8")
        (self.root / "tools/check_pages.py").write_text("import sys\nprint('エラー: x')\nsys.exit(1)\n", encoding="utf-8")
        (self.root / "tools/check_svg.py").write_text("print('図 0 枚')\n", encoding="utf-8")

    def tearDown(self):
        self._tmp.cleanup()

    def run_cli(self, *args: str) -> tuple[int, str]:
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = check_all.main(["--root", str(self.root), *args])
        return code, out.getvalue()

    def test_steps_are_the_ci_set(self):
        steps = check_all.steps(self.root)
        self.assertEqual([s.name for s in steps if not s.optional], DESIGN_STEPS)
        self.assertEqual([s.name for s in steps if s.optional], ["render"])
        for s in steps:
            if s.command[0] == check_all.PY and s.command[1].startswith("tools/"):
                self.assertTrue((REPO / s.command[1]).is_file(), s.command[1])

    def test_selection(self):
        steps = check_all.steps(self.root)
        names = lambda chosen: [s.name for s in chosen]           # noqa: E731
        self.assertEqual(names(check_all.select_steps(steps, [], [], False)), DESIGN_STEPS)
        self.assertEqual(names(check_all.select_steps(steps, ["render"], [], False)), ["mkdocs", "render"])
        self.assertEqual(names(check_all.select_steps(steps, [], ["tests-site", "mkdocs"], True))[-1], "render")
        self.assertNotIn("mkdocs", names(check_all.select_steps(steps, [], ["mkdocs"], False)))

    def test_results_and_exit_codes(self):
        code, out = self.run_cli("--only", "make_schema,gen_site,check_pages,check_svg")
        self.assertEqual(code, 1)
        self.assertIn("通った  make_schema", out)
        self.assertIn("飛ばした  gen_site（tools/gen_site.py がない）", out)
        self.assertIn("落ちた  check_pages（終了コード 1）", out)
        self.assertIn("通った 2・落ちた 1・飛ばした 1", out)
        code, out = self.run_cli("--only", "make_schema,check_svg")
        self.assertEqual(code, 0)

    def test_fail_fast_and_names(self):
        code, out = self.run_cli("--only", "check_pages,check_svg", "-x")
        self.assertEqual(code, 1)
        self.assertNotIn("通った  check_svg", out)
        self.assertIn("流さなかった 1", out)
        self.assertEqual(self.run_cli("--only", "no-such-step")[0], 2)
        code, out = self.run_cli("--list")
        self.assertEqual(code, 0)
        for name in DESIGN_STEPS + ["render"]:
            self.assertIn(name, out)


class TestWorkflow(unittest.TestCase):
    def test_check_yml_runs_check_all(self):
        data = yaml.safe_load((REPO / ".github/workflows/check.yml").read_text(encoding="utf-8"))
        on = data.get("on", data.get(True))
        self.assertIn("workflow_call", on)               # ci.yml から呼んで、デプロイをこの後に置けるように
        self.assertIn("workflow_dispatch", on)
        steps = data["jobs"]["all"]["steps"]
        runs = [s.get("run", "") for s in steps]
        self.assertTrue(any("uv sync --locked" in r and "npm ci" in r for r in runs))
        last = steps[-1]
        self.assertEqual(last["run"], "uv run python tools/check_all.py")
        self.assertEqual(last["env"]["REQUIRE_TEXTLINT"], "1")
        uses = [s.get("uses", "") for s in steps]
        self.assertTrue(any(u.startswith("actions/setup-node@v") for u in uses))
        node = next(s for s in steps if s.get("uses", "").startswith("actions/setup-node@"))
        self.assertGreaterEqual(int(node["with"]["node-version"]), 22)   # prh 6.1.0 の要件
        self.assertEqual(data["permissions"], {"contents": "read"})


if __name__ == "__main__":
    unittest.main()
