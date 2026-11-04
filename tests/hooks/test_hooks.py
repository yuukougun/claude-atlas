"""hooks（.claude/hooks/）と .claude/settings.json の試験（planning/design.md §10.5、design-review.md の DR-08）。

Claude Code は起動しない。一時フォルダに .claude/settings.json と .claude/hooks/ を写し、その写しの hook のスクリプトに
入力の JSON（Claude Code が標準入力に渡す形。research/28 #1 と、手元の 2.1.317 の入力の型）を与えて、出力の JSON と
終了コードを確かめる。制作の印（state/production）は一時フォルダの中にだけ置く（本物の state/ には触れない）。

動かし方（標準のライブラリだけ。hooks は読者の python3 で動くので、両方で流す）：
  python3 -m unittest discover -s tests/hooks
  uv run python -m unittest discover -s tests/hooks
環境変数：
  HOOK_PYTHON           hook を動かす Python（既定は試験を動かしている Python）
  HOOKS_TEST_SETTINGS   写す settings.json（既定は .claude/settings.json。入れる前の案を試すとき）
"""
from __future__ import annotations

import ast
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HOOKS = REPO / ".claude" / "hooks"
SETTINGS = Path(os.environ.get("HOOKS_TEST_SETTINGS") or REPO / ".claude" / "settings.json")
PYTHON = os.environ.get("HOOK_PYTHON") or sys.executable
PRE = "pre_tool_use.py"
START = "session_start.py"


def load_module(path: Path, name: str):
    """フックのスクリプトを試験の中で読む（.claude/hooks/ に __pycache__ を作らない）。"""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    keep, sys.dont_write_bytecode = sys.dont_write_bytecode, True
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.dont_write_bytecode = keep
    return mod


HOOK = load_module(HOOKS / PRE, "claude_atlas_pre_tool_use")


def clean_env(**extra: str) -> dict:
    """試験の外の値が混ざらない環境（API キーの変数・CLAUDE_PROJECT_DIR を外す）。"""
    env = {k: v for k, v in os.environ.items()
           if not k.startswith(("ANTHROPIC_", "CLAUDE_CODE_USE_")) and k != "CLAUDE_PROJECT_DIR"}
    env.update(extra)
    return env


class Project:
    """一時フォルダに作った、リポジトリの写し（.claude/ と、必要なら state/）。"""

    def __init__(self, production: bool = False, state: bool = True, trace: bool = False, settings: bool = True):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(os.path.realpath(self._tmp.name)) / "repo"
        hooks = self.root / ".claude" / "hooks"
        hooks.mkdir(parents=True)
        if settings:
            shutil.copy(SETTINGS, self.root / ".claude" / "settings.json")
        for p in HOOKS.glob("*.py"):
            shutil.copy(p, hooks / p.name)
        if state or production or trace:
            (self.root / "state").mkdir()
        if production:
            (self.root / "state" / "production").write_text("", encoding="utf-8")
        if trace:
            (self.root / "state" / "hook-trace").write_text("", encoding="utf-8")

    def close(self) -> None:
        self._tmp.cleanup()

    def script(self, name: str) -> Path:
        return self.root / ".claude" / "hooks" / name

    def run(self, name: str, payload, env: dict | None = None, python: str = PYTHON):
        stdin = payload if isinstance(payload, str) else json.dumps(payload, ensure_ascii=False)
        r = subprocess.run([python, str(self.script(name))], input=stdin.encode("utf-8"), capture_output=True,
                           env=env or clean_env(CLAUDE_PROJECT_DIR=str(self.root)), cwd=str(self.root), timeout=30)
        return r

    def call(self, tool: str, tool_input: dict, agent: bool = False, cwd: Path | None = None, **extra):
        return self.run(PRE, tool_call(self.root, tool, tool_input, agent=agent, cwd=cwd, **extra))

    def log_lines(self, name: str = "blocks.log") -> list[str]:
        p = self.root / "state" / name
        return p.read_text(encoding="utf-8").splitlines() if p.exists() else []


def tool_call(root: Path, tool: str, tool_input: dict, agent: bool = False, cwd: Path | None = None, **extra) -> dict:
    """PreToolUse の入力（共通の項目 + tool_name・tool_input。担当なら agent_id と agent_type）。"""
    d = {"session_id": "test-session", "transcript_path": "/tmp/test.jsonl", "cwd": str(cwd or root),
         "permission_mode": "default", "hook_event_name": "PreToolUse", "tool_name": tool,
         "tool_input": tool_input, "tool_use_id": "toolu_test"}
    if agent:
        d.update(agent_id="a0b1c2d3e4", agent_type="general-purpose")
    d.update(extra)
    return d


class HookCase(unittest.TestCase):
    production = False

    def setUp(self):
        self.p = Project(production=self.production)
        self.addCleanup(self.p.close)

    def assertDeny(self, r, rule: str, *needles: str) -> str:
        self.assertEqual(r.returncode, 0, r.stderr.decode())
        self.assertEqual(r.stderr.decode(), "")
        self.assertTrue(r.stdout.strip(), "止めるはずが、何も出さなかった")
        out = json.loads(r.stdout)
        hso = out["hookSpecificOutput"]
        self.assertEqual(hso["hookEventName"], "PreToolUse")
        self.assertEqual(hso["permissionDecision"], "deny")
        reason = hso["permissionDecisionReason"]
        self.assertIn(rule, reason)
        self.assertIn("回り込まず", reason)                     # 決まり2：回避策を探させない
        for n in needles:
            self.assertIn(n, reason)
        self.assertLessEqual(len(reason), 2000)                 # Claude Code が切り詰める長さ（2.1.317）
        self.assertLessEqual(len(reason.splitlines()), 20)
        return reason

    def assertAllow(self, r) -> None:
        self.assertEqual(r.returncode, 0, r.stderr.decode())
        self.assertEqual(r.stdout.decode(), "", "止めないはずが、出力があった")
        self.assertEqual(r.stderr.decode(), "")

    def bash(self, command: str, agent: bool = False, cwd: Path | None = None):
        return self.p.call("Bash", {"command": command, "description": "test"}, agent=agent, cwd=cwd)


# ---------------------------------------------------------------------------------------------------------------
class SettingsTest(unittest.TestCase):
    """.claude/settings.json の形（いまの作業を止めない範囲になっているか）。"""

    @classmethod
    def setUpClass(cls):
        cls.s = json.loads(SETTINGS.read_text(encoding="utf-8"))
        cls.deny = cls.s["permissions"]["deny"]

    def test_top_level_keys(self):
        self.assertLessEqual(set(self.s), {"$schema", "permissions", "hooks"})

    def test_noai_domains_have_both_forms(self):
        domains = HOOK.noai_domains(self.deny)
        self.assertLessEqual({"atcoder.jp", "codeforces.com"}, set(domains))
        for d in domains:
            self.assertIn(f"WebFetch(domain:{d})", self.deny)
            self.assertIn(f"WebFetch(domain:*.{d})", self.deny)

    def test_no_rule_stops_main_work(self):
        # Bash・Read の deny と、道具ごと消す deny（素の WebFetch など）を置かない。メインの git・uv・npm・python3 を止めない
        for rule in self.deny:
            self.assertFalse(rule.startswith(("Bash", "Read")), rule)
            self.assertIn("(", rule, rule)
        self.assertNotIn("WebFetch(domain:*)", self.deny)

    def test_edit_rules_are_root_relative(self):
        edits = [r for r in self.deny if r.startswith("Edit")]
        self.assertTrue(edits)
        for r in edits:
            self.assertRegex(r, r"^Edit\(/[^/~][^)]*\)$")
        self.assertEqual(len(HOOK.generated_patterns(self.deny)), len(edits))

    def test_edit_rules_match_generated_and_spare_handwritten(self):
        pats = [rx for _, rx in HOOK.generated_patterns(self.deny)]
        generated = ["docs/llms.txt", "docs/lists/levels.md", "docs/lists/by-scene/contest.md",
                     "docs/start/index.md", "docs/symptoms/index.md"]
        handwritten = ["docs/index.md", "docs/start/how-to-use.md", "docs/start/glossary.md",
                       "docs/symptoms/instructions-ignored.md", "docs/img/x/a.svg", "mkdocs.yml", "CLAUDE.md",
                       "README.md", "planning/design.md", "data/facts.yml", "snippets/x/a.json", "overrides/main.html",
                       "tests/tools/fixtures/small/docs/lists/a.md", "docs/llms.txt.bak", "docs/lists"]
        for g in generated:
            self.assertTrue(any(rx.match(g) for rx in pats), g)
        for h in handwritten:
            self.assertFalse(any(rx.match(h) for rx in pats), h)

    def test_hook_entries(self):
        hooks = self.s["hooks"]
        self.assertEqual(set(hooks), {"PreToolUse", "SessionStart"})
        pre = hooks["PreToolUse"]
        self.assertEqual(len(pre), 1)
        self.assertRegex(pre[0]["matcher"], r"^[A-Za-z|]+$")   # 完全一致の形（正規表現にしない。research/28 #5）
        self.assertEqual(set(pre[0]["matcher"].split("|")), {"Bash", "Edit", "Write", "NotebookEdit", "WebFetch"})
        self.assertNotIn("matcher", hooks["SessionStart"][0])
        scripts = {"PreToolUse": PRE, "SessionStart": START}
        for event, entries in hooks.items():
            for entry in entries:
                for h in entry["hooks"]:
                    self.assertEqual(h["type"], "command")
                    self.assertEqual(h["command"], f'python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/{scripts[event]}"')
                    self.assertTrue((HOOKS / scripts[event]).is_file())
                    self.assertGreater(h.get("timeout", 0), 0)
                    self.assertNotIn("onFailure", h)               # 止める側に倒すのはスクリプトの中だけ（README）

    @unittest.skipUnless(shutil.which("bash"), "bash がない")
    def test_commands_run_through_the_shell(self):
        # settings.json の command の文字列を、そのまま bash で動かす（引用と $CLAUDE_PROJECT_DIR の展開）
        p = Project(production=True)
        self.addCleanup(p.close)
        env = clean_env(CLAUDE_PROJECT_DIR=str(p.root), ANTHROPIC_API_KEY="sk-ant-test")
        for event, entries in self.s["hooks"].items():
            payload = (tool_call(p.root, "WebFetch", {"url": "https://atcoder.jp/", "prompt": "x"})
                       if event == "PreToolUse" else {"session_id": "s", "transcript_path": "/tmp/t", "cwd": str(p.root),
                                                     "hook_event_name": "SessionStart", "source": "startup"})
            for entry in entries:
                for h in entry["hooks"]:
                    r = subprocess.run(["bash", "-c", h["command"]], input=json.dumps(payload).encode(),
                                       capture_output=True, env=env, cwd=str(p.root), timeout=30)
                    self.assertEqual(r.returncode, 0, r.stderr.decode())
                    self.assertTrue(r.stdout.strip(), event)
                    json.loads(r.stdout)


# ---------------------------------------------------------------------------------------------------------------
class NoaiWebFetchTest(HookCase):
    """H1：WebFetch。deny が強制し、hook は理由と記録を受け持つ（メインにも担当にも、印がなくても働く）。"""

    def fetch(self, url: str, agent: bool = False):
        return self.p.call("WebFetch", {"url": url, "prompt": "要約して"}, agent=agent)

    def test_denies_noai_hosts(self):
        for url, host in [("https://atcoder.jp/contests/abc300", "atcoder.jp"),
                          ("https://img.atcoder.jp/a.png", "img.atcoder.jp"),
                          ("http://ATCODER.JP./", "atcoder.jp"),
                          ("https://codeforces.com/problemset", "codeforces.com"),
                          ("https://m1.codeforces.com/", "m1.codeforces.com")]:
            with self.subTest(url=url):
                self.assertDeny(self.fetch(url), "H1", host, "別の一次資料")
        self.assertDeny(self.fetch("https://atcoder.jp/", agent=True), "H1")

    def test_allows_other_hosts(self):
        # ドメインの文字列では照らさない（パスや別のドメインの一部に含まれるだけなら止めない）
        for url in ["https://code.claude.com/docs/en/hooks", "https://example.com/?q=atcoder.jp",
                    "https://notatcoder.jp/", "https://atcoder.jp.example.com/",
                    "https://web.archive.org/web/2026/https://atcoder.jp/", "not a url", ""]:
            with self.subTest(url=url):
                self.assertAllow(self.fetch(url))


class NoaiBashTest(HookCase):
    """H1：Bash は取得の道具の URL の引数だけを照らす（grep や check_noai.py を止めない）。"""

    def test_denies_fetch_tools(self):
        for cmd in ["curl -sL https://atcoder.jp/contests/abc300/tasks",
                    "wget -q -O - codeforces.com/problemset",
                    'cd /tmp && curl "https://atcoder.jp"',
                    "timeout 20 curl atcoder.jp",
                    "sudo -u nobody curl https://atcoder.jp/",
                    "bash -lc 'curl -s https://atcoder.jp/'",
                    "x=$(curl -s https://img.atcoder.jp/)",
                    "curl --url=https://atcoder.jp/",
                    "http GET atcoder.jp/contests",
                    "/usr/bin/curl https://atcoder.jp",
                    "curl -s https://example.com | grep a; wget https://codeforces.com/",
                    "FOO=1 env BAR=2 curl -H 'X: y' https://atcoder.jp"]:
            with self.subTest(cmd=cmd):
                self.assertDeny(self.bash(cmd), "H1", "別の一次資料")

    def test_allows_non_fetch_mentions(self):
        for cmd in ["curl -sI https://example.com",
                    "grep -rn atcoder.jp planning/",
                    "python3 tools/check_noai.py https://atcoder.jp/",
                    "uv run python tools/check_noai.py --robots https://codeforces.com/",
                    "echo https://atcoder.jp",
                    "git log --grep atcoder.jp",
                    "rg 'curl https://atcoder.jp' docs",
                    "cat <<'EOF' > /tmp/x\ncurl https://atcoder.jp\nEOF",
                    "curl -o atcoder.jp.html https://example.com",
                    "# curl https://atcoder.jp",
                    "echo 'wget atcoder.jp' | wc -c"]:
            with self.subTest(cmd=cmd):
                self.assertAllow(self.bash(cmd))


# ---------------------------------------------------------------------------------------------------------------
class GeneratedFileTest(HookCase):
    """H2：生成物のパス（settings.json の deny の Edit(/…)）への Edit・Write・NotebookEdit。"""

    def test_denies_generated_paths(self):
        r = self.p.root
        cases = [("Write", {"file_path": str(r / "docs/llms.txt"), "content": "x"}, "docs/llms.txt"),
                 ("Edit", {"file_path": str(r / "docs/lists/levels.md"), "old_string": "a", "new_string": "b"},
                  "docs/lists/levels.md"),
                 ("Write", {"file_path": str(r / "docs/lists/by-scene/contest.md"), "content": "x"},
                  "docs/lists/by-scene/contest.md"),
                 ("Edit", {"file_path": str(r / "docs/start/index.md"), "old_string": "a", "new_string": "b"},
                  "docs/start/index.md"),
                 ("NotebookEdit", {"notebook_path": str(r / "docs/lists/a.ipynb"), "new_source": "x"},
                  "docs/lists/a.ipynb"),
                 ("Write", {"file_path": "docs/llms.txt", "content": "x"}, "docs/llms.txt")]   # 相対は cwd から
        for tool, tin, rel in cases:
            for agent in (False, True):
                with self.subTest(tool=tool, rel=rel, agent=agent):
                    self.assertDeny(self.p.call(tool, tin, agent=agent), "H2", rel, "gen_site.py")

    def test_allows_handwritten_and_outside(self):
        r = self.p.root
        for path in [r / "docs/index.md", r / "docs/start/how-to-use.md", r / "nav.yml", r / "CLAUDE.md",
                     r / "tests/tools/fixtures/small/docs/lists/a.md", Path("/tmp/elsewhere/docs/llms.txt"),
                     r.parent / "docs/llms.txt"]:
            with self.subTest(path=path):
                self.assertAllow(self.p.call("Write", {"file_path": str(path), "content": "x"}))
                self.assertAllow(self.p.call("Edit", {"file_path": str(path), "old_string": "a", "new_string": "b"}))

    def test_read_is_not_affected(self):
        self.assertAllow(self.p.call("Read", {"file_path": str(self.p.root / "docs/llms.txt")}))


class GeneratedFileBashTest(HookCase):
    """H2：Bash は、Claude Code が書き込みと見分ける形（リダイレクト・tee・sed -i）の書き先だけを見る。"""

    def test_denies_shell_writes(self):
        root = self.p.root
        for cmd in ["echo x > docs/llms.txt",
                    "printf a >> docs/lists/levels.md",
                    "cat > docs/lists/new.md <<'EOF'\nbody\nEOF",
                    "sed -i 's/a/b/' docs/start/index.md",
                    "sed -Ei.bak 's/a/b/' docs/start/index.md",
                    "uv run python tools/x.py | tee docs/lists/a.md",
                    "cd docs && echo x > llms.txt",
                    "echo x >| docs/llms.txt",
                    "make 2>&1 &> docs/llms.txt",
                    f"echo x > {root}/docs/llms.txt",
                    "echo x>docs/llms.txt"]:
            with self.subTest(cmd=cmd):
                self.assertDeny(self.bash(cmd), "H2", "gen_site.py")

    def test_allows_reads_and_other_targets(self):
        for cmd in ["cat docs/llms.txt",
                    "sed -n 1,5p docs/start/index.md",
                    "uv run python tools/gen_site.py",
                    "uv run python tools/gen_site.py --page how-to-use",
                    "echo x > /tmp/a.txt",
                    "echo x 2>&1 | tee /tmp/log",
                    "cat > /tmp/x <<'EOF'\n> docs/llms.txt\nEOF",
                    "cat > /tmp/x <<-EOF\n\techo y > docs/llms.txt\n\tEOF",
                    'echo "> docs/llms.txt"',
                    "git diff > /tmp/d.patch",
                    "diff <(cat docs/llms.txt) /tmp/x",
                    "echo x >> state/now.md",
                    "wc -l < docs/llms.txt",
                    "echo x > docs/index.md",
                    MAIN_COMMIT]:
            with self.subTest(cmd=cmd):
                self.assertAllow(self.bash(cmd))


# ---------------------------------------------------------------------------------------------------------------
# メインがふだん使う commit の形（本文の ' と ( と、> で始まる行を含む）
MAIN_COMMIT = ("git add -A && git commit -m \"$(cat <<'EOF'\nFix the hooks' tests (don't block)\n\n"
               "> docs/llms.txt is generated\nCo-Authored-By: Claude <noreply@anthropic.com>\nEOF\n)\" && git push")
GIT_READ_CMDS = ["git status", "git status --porcelain", "git diff --stat", "git log --oneline -5",
                 "git show HEAD:README.md", "git -C ../kyopro-atlas log -3", "git --no-pager diff HEAD~1",
                 "git rev-parse HEAD", "git ls-files docs", "git blame CLAUDE.md", "git grep -n foo",
                 "git --version", "git help commit", "git", "git log | head -5", "echo git commit",
                 'grep -rn "git commit" planning', "cat .git/HEAD", "uv run python tools/check_catalog.py",
                 "echo $(git rev-parse --short HEAD)", "gh pr view 3", "gh issue list --state all", "gh pr",
                 "gh api repos/yuukougun/claude-atlas", "gh api -X GET search/issues -f q=x", "gh --version",
                 "gh run view 123 --log", "gh -R yuukougun/claude-atlas pr list", "gh search repos claude"]
GIT_WRITE_CMDS = ["git commit -m x", "git add .", "git push origin main", "git checkout -- docs/x.md",
                  "git reset --hard HEAD", "git stash", "git stash list", "git restore docs/x.md", "git clean -fd",
                  "git switch -c b", "git -C . commit -m x", "git -c user.name=x commit -m y",
                  "git --git-dir=.git --work-tree=. commit -m y", "git diff --output=/tmp/x",
                  "git status; git add -A", "cd docs && git commit -am x", 'bash -c "git commit -m x"',
                  "sh -c 'git push'", 'eval "git reset --hard"', "/usr/bin/git commit -m x", "\\git commit -m x",
                  "sudo git commit -m x", "xargs git add < /tmp/list", "echo $(git commit -m x)",
                  "git ci -m x", "git branch -D x", "git tag v1", "git config user.email x",
                  "git log --oneline && git push", "gh pr create --fill", "gh pr merge 3", "gh issue comment 3 -b x",
                  "gh api -X POST repos/x/y/issues", "gh api repos/x/y/issues -f title=x", "gh api --method=PATCH x",
                  "gh repo clone yuukougun/claude-atlas", "gh release create v1", "gh auth login"]


class AgentGitWithoutMarkTest(HookCase):
    """H3：制作の印がなければ働かない（読者の環境と、印を作る前の制作）。"""

    def test_agent_git_is_allowed_without_mark(self):
        for cmd in ["git commit -m x", "git push", "gh pr create"]:
            with self.subTest(cmd=cmd):
                self.assertAllow(self.bash(cmd, agent=True))
        self.assertFalse((self.p.root / "state" / "blocks.log").exists())


class AgentGitTest(HookCase):
    """H3：印があるとき、担当（agent_id がある呼び出し）の git と gh は読むだけ。メインは止めない。"""
    production = True

    def test_main_is_never_stopped(self):
        for cmd in ["git add -A && git commit -m x && git push", "gh pr create --fill", "git reset --hard", MAIN_COMMIT]:
            with self.subTest(cmd=cmd):
                self.assertAllow(self.bash(cmd))
        # agent_id が空の文字列なら、メインとして扱う
        self.assertAllow(self.p.run(PRE, tool_call(self.p.root, "Bash", {"command": "git commit -m x"}, agent_id="")))

    def test_agent_read_only_git_and_gh(self):
        for cmd in GIT_READ_CMDS:
            with self.subTest(cmd=cmd):
                self.assertAllow(self.bash(cmd, agent=True))

    def test_agent_write_git_and_gh(self):
        for cmd in GIT_WRITE_CMDS + [MAIN_COMMIT]:
            with self.subTest(cmd=cmd):
                self.assertDeny(self.bash(cmd, agent=True), "H3", "報告に書いて")

    def test_command_after_heredoc_in_substitution_is_seen(self):
        head = "x=\"$(cat <<'EOF'\nit's (a) test\nEOF\n)\"; "
        self.assertAllow(self.bash(head + "git status", agent=True))
        self.assertDeny(self.bash(head + "git push", agent=True), "H3", "git push")

    def test_other_tools_of_agents_are_not_affected(self):
        self.assertAllow(self.p.call("Write", {"file_path": str(self.p.root / "planning/x.md"), "content": "git commit"},
                                     agent=True))
        self.assertAllow(self.bash("uv run python -m unittest discover -s tests/hooks", agent=True))


# ---------------------------------------------------------------------------------------------------------------
class BlocksLogTest(unittest.TestCase):
    """止めた操作の記録（state/blocks.log）と、hook の呼ばれ方の記録（state/hook-trace.log）。"""

    def project(self, **kw) -> Project:
        p = Project(**kw)
        self.addCleanup(p.close)
        return p

    def test_logs_one_line_per_block_with_mark(self):
        p = self.project(production=True)
        p.call("Bash", {"command": "git push https://x:sk-ant-abc123@github.com/x/y main"}, agent=True)
        p.call("WebFetch", {"url": "https://atcoder.jp/", "prompt": "x"})
        p.call("Bash", {"command": "git status"}, agent=True)                       # 止めないものは書かない
        lines = p.log_lines()
        self.assertEqual(len(lines), 2, lines)
        f1, f2 = lines[0].split("\t"), lines[1].split("\t")
        self.assertEqual(len(f1), 5)
        self.assertEqual((f1[1], f1[2], f1[3]), ("H3", "agent:general-purpose:a0b1c2d3e4", "Bash"))
        self.assertNotIn("sk-ant-abc123", lines[0])                                # 秘密らしい値は伏せる
        self.assertEqual((f2[1], f2[2], f2[3], f2[4]), ("H1", "main", "WebFetch", "atcoder.jp"))

    def test_no_log_without_mark(self):
        p = self.project(production=False)
        r = p.call("WebFetch", {"url": "https://atcoder.jp/", "prompt": "x"})
        self.assertIn(b"deny", r.stdout)
        self.assertEqual(p.log_lines(), [])

    def test_does_not_create_state(self):
        p = self.project(state=False)
        r = p.call("Write", {"file_path": str(p.root / "docs/llms.txt"), "content": "x"})
        self.assertIn(b"deny", r.stdout)
        self.assertFalse((p.root / "state").exists())

    def test_trace(self):
        p = self.project(trace=True)
        p.call("Bash", {"command": "ls"}, agent=True)
        p.call("WebFetch", {"url": "https://atcoder.jp/", "prompt": "x"})
        lines = p.log_lines("hook-trace.log")
        self.assertEqual([x.split("\t")[1:] for x in lines],
                         [["PreToolUse", "Bash", "a0b1c2d3e4", "general-purpose", "-"],
                          ["PreToolUse", "WebFetch", "-", "-", "deny"]])
        self.assertEqual(p.log_lines(), [])                                         # 印がないので blocks.log はない


class RobustnessTest(unittest.TestCase):
    """壊れた入力・設定でも、止めずに静かに終わる（担当の git・gh だけは印があると止める側に倒す）。"""

    def project(self, **kw) -> Project:
        p = Project(**kw)
        self.addCleanup(p.close)
        return p

    def assertQuiet(self, r):
        self.assertEqual((r.returncode, r.stdout, r.stderr), (0, b"", b""))

    def test_bad_input(self):
        p = self.project(production=True)
        for payload in ["", "not json", "[1, 2]", "null", '{"tool_name": "Bash"}',
                        '{"tool_name": "Bash", "tool_input": "git commit"}',
                        '{"tool_name": "Bash", "tool_input": {"command": ""}}',
                        '{"tool_name": "Bash", "tool_input": {"command": 3}}',
                        '{"tool_name": "Glob", "tool_input": {"pattern": "docs/lists/**"}}',
                        '{"tool_name": "Edit", "tool_input": {}}']:
            with self.subTest(payload=payload):
                self.assertQuiet(p.run(PRE, payload))

    def test_unbalanced_quotes_do_not_crash(self):
        p = self.project(production=True)
        for cmd in ["echo 'unterminated", 'echo "a $(b', "echo `x", "cat <<EOF\nno end", "a && && b", "))((",
                    "echo ${x", "\\"]:
            with self.subTest(cmd=cmd):
                self.assertQuiet(p.call("Bash", {"command": cmd}, agent=True))

    def test_missing_or_broken_settings(self):
        p = self.project(settings=False)
        self.assertQuiet(p.call("WebFetch", {"url": "https://atcoder.jp/", "prompt": "x"}))
        (p.root / ".claude" / "settings.json").write_text("{ broken", encoding="utf-8")
        self.assertQuiet(p.call("Write", {"file_path": str(p.root / "docs/llms.txt"), "content": "x"}))

    def test_internal_error_fails_safe_only_for_agent_git(self):
        # evaluate が誤りで終わったとき：印があり担当の Bash に git・gh が出るときだけ止め、ほかは止めない
        wrapper = ("import importlib.util, sys\n"
                   "spec = importlib.util.spec_from_file_location('h', sys.argv[1])\n"
                   "m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)\n"
                   "def boom(data):\n    raise RuntimeError('boom')\n"
                   "m.evaluate = boom\nsys.exit(m.main())\n")
        cases = [(True, True, "git status", True), (True, True, "ls -la", False), (True, False, "git commit", False),
                 (False, True, "git commit", False), (True, True, "cat github.md", False)]
        for production, agent, cmd, stops in cases:
            with self.subTest(production=production, agent=agent, cmd=cmd):
                p = self.project(production=production)
                payload = json.dumps(tool_call(p.root, "Bash", {"command": cmd}, agent=agent))
                r = subprocess.run([PYTHON, "-c", wrapper, str(p.script(PRE))], input=payload.encode(),
                                   capture_output=True, env=clean_env(), timeout=30)
                self.assertEqual(r.returncode, 0, r.stderr.decode())
                if stops:
                    out = json.loads(r.stdout)["hookSpecificOutput"]
                    self.assertEqual(out["permissionDecision"], "deny")
                    self.assertIn("H3", out["permissionDecisionReason"])
                else:
                    self.assertEqual(r.stdout, b"")

    def test_long_reason_is_bounded(self):
        p = self.project(production=True)
        cmd = " ; ".join(["git commit -m " + "x" * 500, "curl https://atcoder.jp/" + "y" * 500,
                          "echo z > docs/lists/" + "w" * 300 + ".md"] * 20)
        r = p.call("Bash", {"command": cmd}, agent=True)
        reason = json.loads(r.stdout)["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertLessEqual(len(reason), 2000)
        self.assertLessEqual(len(reason.splitlines()), 20)
        for rule in ("H1", "H2", "H3"):
            self.assertIn(rule, reason)

    @unittest.skipUnless(shutil.which("python3"), "python3 がない")
    def test_runs_with_python3_on_path(self):
        # 読者の環境と同じく、PATH の python3 で動く（settings.json の command と同じ）
        p = self.project()
        r = p.run(PRE, tool_call(p.root, "WebFetch", {"url": "https://codeforces.com/", "prompt": "x"}),
                  python=shutil.which("python3"))
        self.assertEqual(r.returncode, 0, r.stderr.decode())
        self.assertEqual(json.loads(r.stdout)["hookSpecificOutput"]["permissionDecision"], "deny")


# ---------------------------------------------------------------------------------------------------------------
class SessionStartTest(unittest.TestCase):
    """H4：印があり、API キーなどの変数があるときだけ知らせる（止めない。値は出さない）。"""

    PAYLOAD = {"session_id": "s", "transcript_path": "/tmp/t.jsonl", "cwd": "/tmp", "hook_event_name": "SessionStart",
               "source": "startup", "model": "claude-opus-5-5"}

    def start(self, production: bool, **env: str):
        p = Project(production=production)
        self.addCleanup(p.close)
        return p.run(START, self.PAYLOAD, env=clean_env(CLAUDE_PROJECT_DIR=str(p.root), **env))

    def assertSilent(self, r):
        self.assertEqual((r.returncode, r.stdout, r.stderr), (0, b"", b""))

    def test_silent_without_mark(self):
        self.assertSilent(self.start(False, ANTHROPIC_API_KEY="sk-ant-secret"))

    def test_silent_without_keys(self):
        self.assertSilent(self.start(True))
        self.assertSilent(self.start(True, ANTHROPIC_API_KEY=""))
        self.assertSilent(self.start(True, CLAUDE_CODE_USE_BEDROCK="0", CLAUDE_CODE_USE_VERTEX="false"))
        self.assertSilent(self.start(True, ANTHROPIC_MODEL="claude-opus-5-5", ANTHROPIC_BASE_URL="http://x"))

    def test_notices_keys_by_name_only(self):
        for env, names in [({"ANTHROPIC_API_KEY": "sk-ant-secret"}, ["ANTHROPIC_API_KEY"]),
                           ({"ANTHROPIC_AUTH_TOKEN": "t0ken", "ANTHROPIC_FOUNDRY_API_KEY": "k3y"},
                            ["ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_FOUNDRY_API_KEY"]),
                           ({"CLAUDE_CODE_USE_BEDROCK": "1"}, ["CLAUDE_CODE_USE_BEDROCK"])]:
            with self.subTest(env=env):
                r = self.start(True, **env)
                self.assertEqual(r.returncode, 0, r.stderr.decode())
                out = json.loads(r.stdout)
                self.assertEqual(out["hookSpecificOutput"]["hookEventName"], "SessionStart")
                for text in (out["systemMessage"], out["hookSpecificOutput"]["additionalContext"]):
                    self.assertIn("H4", text)
                    self.assertIn("従量の課金", text)
                    for n in names:
                        self.assertIn(n, text)
                    for value in env.values():
                        if value != "1":
                            self.assertNotIn(value, text)

    def test_bad_input_is_ignored(self):
        p = Project(production=True)
        self.addCleanup(p.close)
        r = p.run(START, "not json", env=clean_env(ANTHROPIC_API_KEY="x"))
        self.assertEqual(r.returncode, 0)
        self.assertIn(b"ANTHROPIC_API_KEY", r.stdout)


# ---------------------------------------------------------------------------------------------------------------
class ParserTest(unittest.TestCase):
    """シェルの字句の近似（pre_tool_use.py の parse_shell と effective_argv）。"""

    def words(self, src: str) -> list[list[str]]:
        return [c.words for c in HOOK.parse_shell(src)]

    def test_operators_split_commands(self):
        self.assertEqual(self.words("a && b || c; d | e & f\ng"), [["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"]])
        self.assertEqual(self.words("(cd x; ls) |& tee y"), [["cd", "x"], ["ls"], ["tee", "y"]])

    def test_quotes_and_escapes(self):
        self.assertEqual(self.words("echo \"a b\" 'c d' e\\ f g\"h\"i ''"), [["echo", "a b", "c d", "e f", "ghi", ""]])
        self.assertEqual(self.words('echo "x \\" y"'), [["echo", 'x " y']])
        self.assertEqual(self.words("echo a \\\n b"), [["echo", "a", "b"]])

    def test_redirects(self):
        cmd = HOOK.parse_shell("cmd 2>/dev/null >out 2>&1 &>both >>app <in <<<str")[0]
        self.assertEqual(cmd.words, ["cmd"])
        self.assertEqual(cmd.redirects, [(">", "/dev/null"), (">", "out"), (">&", "1"), ("&>", "both"),
                                         (">>", "app"), ("<", "in"), ("<<<", "str")])

    def test_heredoc_body_is_skipped(self):
        cmds = HOOK.parse_shell("cat <<'EOF' > f\nrm -rf / > g\nEOF\necho done")
        self.assertEqual([c.words for c in cmds], [["cat"], ["echo", "done"]])
        self.assertEqual(cmds[0].redirects, [(">", "f")])

    def test_heredoc_inside_substitution(self):
        cmds = list(HOOK.iter_commands("x=\"$(cat <<'EOF'\nIt's a (test\n> docs/llms.txt\nEOF\n)\"; git push"))
        self.assertIn(["git", "push"], [argv for _c, argv in cmds])
        self.assertEqual([r for c, _a in cmds for r in c.redirects], [])

    def test_comments(self):
        self.assertEqual(self.words("echo a#b # c d\n# e\nf"), [["echo", "a#b"], ["f"]])

    def test_substitutions_are_parsed(self):
        got = self.words('echo $(git status) `git log` "$(git diff)" <(git show)')
        for inner in (["git", "status"], ["git", "log"], ["git", "diff"], ["git", "show"]):
            self.assertIn(inner, got)
        # 算術の展開と ${…} は1語のまま（中をコマンドとして読まない）
        self.assertEqual(self.words("echo $((1+2)) ${x:-a b} z"), [["echo", "$((1+2))", "${x:-a b}", "z"]])

    def test_effective_argv(self):
        cases = [("FOO=1 sudo -u x timeout -s KILL 5 git commit", ["git", "commit"]),
                 ("env -u A B=2 nice -n 5 nohup /usr/bin/git push", ["git", "push"]),
                 ("xargs -I {} -n 1 git add {}", ["git", "add", "{}"]),
                 ("if git diff --quiet", ["git", "diff", "--quiet"]),
                 ("time -p git log", ["git", "log"]),
                 ("command -v git", ["git"]),
                 ("A=1", [])]
        for src, argv in cases:
            with self.subTest(src=src):
                self.assertEqual(HOOK.effective_argv(HOOK.parse_shell(src)[0].words), argv)

    def test_nested_script(self):
        self.assertEqual(HOOK.nested_script(["bash", "-o", "pipefail", "-c", "git push"]), "git push")
        self.assertEqual(HOOK.nested_script(["sh", "-ec", "x"]), "x")
        self.assertEqual(HOOK.nested_script(["bash", "script.sh"]), None)
        self.assertEqual(HOOK.nested_script(["eval", "git", "push"]), "git push")

    def test_git_and_gh_tables(self):
        for src in GIT_READ_CMDS:
            for _cmd, argv in HOOK.iter_commands(src):
                if argv and argv[0] == "git":
                    self.assertTrue(HOOK.git_is_read(argv), src)
                if argv and argv[0] == "gh":
                    self.assertTrue(HOOK.gh_is_read(argv), src)
        self.assertFalse(HOOK.gh_api_is_get(["repos/x", "--input", "f.json"]))
        self.assertTrue(HOOK.gh_api_is_get(["repos/x", "--paginate", "-H", "Accept: x"]))
        self.assertFalse(HOOK.gh_api_is_get(["-XDELETE", "repos/x"]))


class StdlibOnlyTest(unittest.TestCase):
    """hooks は標準のライブラリだけで動く（design §8.1・§10.5 の決まり5）。"""

    def test_imports_are_stdlib(self):
        allowed = getattr(sys, "stdlib_module_names", None) or {
            "__future__", "json", "os", "re", "sys", "time", "urllib"}
        for path in HOOKS.glob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                names = []
                if isinstance(node, ast.Import):
                    names = [a.name for a in node.names]
                elif isinstance(node, ast.ImportFrom):
                    names = [node.module or ""]
                for n in names:
                    with self.subTest(path=path.name, module=n):
                        self.assertIn(n.split(".")[0], allowed)


if __name__ == "__main__":
    unittest.main()
