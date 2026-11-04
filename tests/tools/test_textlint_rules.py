"""書き方の検査の設定（.textlintrc.json・prh.yml・package.json・package-lock.json）の試験。
uv run python -m unittest discover -s tests/tools で動く。

- 静的な試験（Node は要らない）：設定が design §6.2 の決まりを持つこと、依存の版が固定で lock と合うこと、prh.yml の形
- textlint を動かす試験：node_modules/.bin/textlint があるときだけ動く（リポジトリの根で npm ci を流しておく）。
  ないときは飛ばす。環境変数 REQUIRE_TEXTLINT=1 のときは、飛ばさずに失敗にする（CI で Node を入れた job が使う）。
  リポジトリの .textlintrc.json と prh.yml で、一時フォルダの Markdown を検査する
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
CONFIG = REPO / ".textlintrc.json"
PRH = REPO / "prh.yml"
PACKAGE = REPO / "package.json"
LOCK = REPO / "package-lock.json"
TEXTLINT = REPO / "node_modules" / ".bin" / "textlint"

# 正規表現（prh は u の旗を付ける）で使ってよいエスケープの文字。ほかの文字のエスケープ（\# \: \@ など）は u では誤り
ALLOWED_ESCAPES = set("^$\\.*+?()[]{}|/-dDsSwWbBfnrtv0123456789cxupPk")


def is_regexp(pattern: str) -> bool:
    return len(pattern) >= 2 and pattern.startswith("/") and re.search(r"/[gimy]*$", pattern[1:]) is not None


def rule_patterns(rule: dict) -> list:
    value = rule.get("pattern", rule.get("patterns"))
    return value if isinstance(value, list) else [value]


# ---- 静的な試験 ----

class TestTextlintConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.config = json.loads(CONFIG.read_text(encoding="utf-8"))
        self.rules = self.config["rules"]

    def test_disable_comments_are_enabled(self):
        # 別名の行と表記の例を <!-- textlint-disable --> で外すため
        self.assertIs(self.config["filters"]["comments"], True)

    def test_prh_reads_prh_yml_and_runs_before_spacing(self):
        # textlint --fix は規則を順に当てる。prh で英語の名前に直した後に、空白の規則が空白を足す
        self.assertEqual(self.rules["prh"]["rulePaths"], ["./prh.yml"])
        names = list(self.rules)
        self.assertLess(names.index("prh"), names.index("ja-space-between-half-and-full-width"))

    def test_design_writing_rules(self):
        # design §6.2：半角英数字と全角文字の間に空白、だ・である調
        self.assertEqual(self.rules["ja-space-between-half-and-full-width"]["space"], "always")
        self.assertEqual(self.rules["ja-space-around-code"], {"before": True, "after": True})
        style = self.rules["preset-ja-technical-writing"]["no-mix-dearu-desumasu"]
        self.assertEqual((style["preferInBody"], style["preferInList"]), ("である", "である"))


class TestPackage(unittest.TestCase):
    def setUp(self) -> None:
        self.package = json.loads(PACKAGE.read_text(encoding="utf-8"))
        self.lock = json.loads(LOCK.read_text(encoding="utf-8"))

    def test_versions_are_pinned_and_match_the_lock(self):
        deps = self.package["devDependencies"]
        self.assertIn("textlint", deps)
        self.assertIn("textlint-rule-prh", deps)
        for name, version in deps.items():
            with self.subTest(name=name):
                self.assertRegex(version, r"^\d+\.\d+\.\d+$")   # ^ や ~ を付けない
                self.assertEqual(self.lock["packages"][f"node_modules/{name}"]["version"], version)
        self.assertEqual(self.lock["packages"][""]["devDependencies"], deps)
        self.assertEqual(self.lock["packages"][""].get("engines"), self.package.get("engines"))

    def test_scripts_use_the_target_list(self):
        scripts = self.package["scripts"]
        self.assertIn("tools/textlint_targets.py --run", scripts["lint:text"])
        self.assertIn("tools/textlint_targets.py --run -- --fix", scripts["lint:text:fix"])


class TestPrhYaml(unittest.TestCase):
    def setUp(self) -> None:
        self.prh = yaml.safe_load(PRH.read_text(encoding="utf-8"))
        self.rules = self.prh["rules"]

    def test_shape(self):
        self.assertEqual(self.prh["version"], 1)
        self.assertGreater(len(self.rules), 0)
        for i, rule in enumerate(self.rules):
            with self.subTest(rule=i, expected=rule.get("expected")):
                self.assertIsInstance(rule.get("expected"), str)
                self.assertEqual(sum(k in rule for k in ("pattern", "patterns")), 1)
                for pattern in rule_patterns(rule):
                    self.assertIsInstance(pattern, str)
                    self.assertNotEqual(pattern, "")
                for spec in rule.get("specs", []):
                    self.assertEqual(set(spec), {"from", "to"})
                    self.assertTrue(isinstance(spec["from"], str) and isinstance(spec["to"], str))

    def test_regexp_rules_have_specs(self):
        for rule in self.rules:
            if any(is_regexp(p) for p in rule_patterns(rule)):
                with self.subTest(expected=rule["expected"]):
                    self.assertTrue(rule.get("specs"), "正規表現の規則には specs を付ける")

    def test_regexp_escapes_are_valid_with_the_u_flag(self):
        for rule in self.rules:
            for pattern in rule_patterns(rule):
                if not is_regexp(pattern):
                    continue
                for m in re.finditer(r"\\(.)", pattern):
                    with self.subTest(expected=rule["expected"], escape=m.group(0)):
                        self.assertIn(m.group(1), ALLOWED_ESCAPES)

    def test_no_pattern_is_in_two_rules(self):
        seen: dict[str, str] = {}
        for rule in self.rules:
            for pattern in rule_patterns(rule):
                with self.subTest(pattern=pattern):
                    self.assertNotIn(pattern, seen, f"{seen.get(pattern)} と {rule['expected']} の両方にある")
                seen[pattern] = rule["expected"]


# ---- textlint を動かす試験 ----

class TextlintCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not TEXTLINT.exists():
            message = f"textlint がない（{TEXTLINT}。リポジトリの根で npm ci を流す）"
            if os.environ.get("REQUIRE_TEXTLINT") == "1":
                raise AssertionError(message)
            raise unittest.SkipTest(message)

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, text: str, name: str = "page.md") -> Path:
        path = self.dir / name
        path.write_text(text, encoding="utf-8")
        return path

    def textlint(self, *args: str, config: Path = CONFIG) -> subprocess.CompletedProcess:
        return subprocess.run([str(TEXTLINT), "--config", str(config), *args], cwd=REPO,
                              capture_output=True, text=True)

    def lint(self, text: str) -> tuple[int, list[dict]]:
        done = self.textlint("--format", "json", str(self.write(text)))
        self.assertIn(done.returncode, (0, 1), done.stderr or done.stdout)
        messages = [m for result in json.loads(done.stdout) for m in result["messages"]]
        return done.returncode, messages


def prh_fixes(messages: list[dict], line: int | None = None) -> list[str]:
    return [m["fix"]["text"] for m in messages if m["ruleId"] == "prh" and (line is None or m["line"] == line)]


class TestPrhThroughTextlint(TextlintCase):
    # 1段落ずつ並べて1回で検査し、行ごとの prh の直しを比べる
    FLAGGED = [
        ("プランモードで計画させる。", ["plan mode"]),
        ("plan モードとプランモード。", ["plan mode", "plan mode"]),
        ("努力レベルを上げる。", ["effort"]),
        ("許可ルールと確認ルールと拒否ルールを足す。", ["allow ルール", "ask ルール", "deny ルール"]),
        ("Claude Code の subagent に調べさせる。", ["サブエージェント"]),
        ("PreToolUse の hook で止める。hook event の一覧を見る。", ["フック", "フックイベント"]),
        ("skill を作り、plugin で配り、marketplace に足す。", ["スキル", "プラグイン", "マーケットプレイス"]),
        ("plugin marketplace を作る。", ["プラグインマーケットプレイス"]),
        ("permission mode を選び、permissions の deny ルールに足す。", ["権限モード", "権限"]),
        ("sandbox で閉じ込め、auto mode で動かす。オートモードの分類器。", ["サンドボックス", "auto モード", "auto モード"]),
        ("context window が埋まる。output style を切り替える。", ["コンテキストウィンドウ", "出力スタイル"]),
        ("auto memory に残る。メモリーに残る。ワークツリーで分ける。", ["自動メモリ", "メモリ", "worktree"]),
        ("claude code の Claude.md に書く。", ["Claude Code", "CLAUDE.md"]),
        ("全てを確かめる。但し、例外がある。出来ない。", ["すべて", "ただし", "できな"]),
    ]
    CLEAN = [
        "plan mode で計画させ、effort を上げる。effort レベルを上げる。",
        "allow ルール・ask ルール・deny ルールを足す。",
        "サブエージェント（subagent）に調べさせる。「hooks」という英語の名前。",
        "`subagent_type` を渡し、SubagentStop で止める。",
        "プラグインの hooks module を読み、Agent Skills の標準に沿う。Skills API に上げる。",
        "/plugin marketplace add で足す。",
        "claude plugin validate を流す。bypassPermissions で動かす。",
        "API の memory tool と compaction を使う。Claude Code の Projects を開く。",
        "research preview の機能である。アプリの権限モードの Auto を選ぶ。",
        "条件や但し書きが要約から落ちる。出来事を記録する。",
        ".claude/hooks/ と /sandbox と sandbox-runtime を使う。",
    ]

    def test_flagged_and_clean_lines(self):
        lines = ["# 試し", ""]
        where = []
        for text in [t for t, _ in self.FLAGGED] + self.CLEAN:
            lines += [text, ""]
            where.append(len(lines) - 1)
        _, messages = self.lint("\n".join(lines))
        for (text, expected), line in zip(self.FLAGGED, where):
            with self.subTest(text=text):
                self.assertEqual(prh_fixes(messages, line), expected)
        for text, line in zip(self.CLEAN, where[len(self.FLAGGED):]):
            with self.subTest(text=text):
                self.assertEqual([m["message"] for m in messages if m["line"] == line and m["severity"] == 2], [])

    def test_front_matter_alias_line_code_links_and_disabled_parts_are_not_checked(self):
        text = "\n".join([
            "---",
            "aliases: [プランモード, 努力レベル, subagent]",
            "stage: draft",
            "---",
            "",
            "<!-- textlint-disable -->",
            "別名：プランモード・plan モード・subagent・Claudeの指示",
            "<!-- textlint-enable -->",
            "",
            "`プランモード` と書かない。[プランモードの記事](https://example.com/plan-mode) を読む。",
            "",
            "```text",
            "プランモード",
            "subagent",
            "```",
            "",
            "<!-- textlint-disable prh -->",
            "| 直す表記 | 正規形 |",
            "| --- | --- |",
            "| プランモード | plan mode |",
            "<!-- textlint-enable prh -->",
            "",
        ])
        code, messages = self.lint(text)
        self.assertEqual([(m["line"], m["ruleId"], m["message"]) for m in messages], [])
        self.assertEqual(code, 0)

    def test_headings_tables_bold_and_italic_are_checked(self):
        text = "\n".join([
            "## プランモードの使いどころ",
            "",
            "| 面 | 手段 |",
            "| --- | --- |",
            "| Claude Code | subagent に任せる |",
            "",
            "**プランモード** で計画させる。*プランモード* で計画させる。",
            "",
        ])
        _, messages = self.lint(text)
        self.assertEqual([(m["line"], m["fix"]["text"]) for m in messages if m["ruleId"] == "prh"],
                         [(1, "plan mode"), (5, "サブエージェント"), (7, "plan mode"), (7, "plan mode")])

    def test_fix_applies_prh_and_then_spacing(self):
        path = self.write("# 試し\n\nのプランモードで計画させる。Claude Code の subagent に調べさせる。hooks と permissions で縛る。\n")
        done = self.textlint("--fix", str(path))
        self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
        self.assertEqual(path.read_text(encoding="utf-8"),
                         "# 試し\n\nの plan mode で計画させる。Claude Code のサブエージェントに調べさせる。フックと権限で縛る。\n")
        self.assertEqual(self.textlint(str(path)).returncode, 0)


class TestOtherRulesThroughTextlint(TextlintCase):
    def test_desumasu_in_body_is_an_error(self):
        code, messages = self.lint("これは試しである。これは試しです。\n")
        self.assertEqual(code, 1)
        self.assertTrue(any(m["ruleId"].endswith("no-mix-dearu-desumasu") and m["severity"] == 2 for m in messages))

    def test_missing_spaces_are_errors(self):
        code, messages = self.lint("Claude Codeで動かす。`uv run`で動かす。\n")
        self.assertEqual(code, 1)
        rules = {m["ruleId"] for m in messages if m["severity"] == 2}
        self.assertEqual(rules, {"ja-space-between-half-and-full-width", "ja-space-around-code"})

    def test_warnings_do_not_fail(self):
        long_sentence = "あいうえおかきくけこ" * 13 + "。\n"   # 131字。sentence-length（120）は警告
        code, messages = self.lint(long_sentence)
        self.assertEqual(code, 0)
        self.assertEqual({(m["ruleId"], m["severity"]) for m in messages},
                         {("ja-technical-writing/sentence-length", 1)})

    def test_broken_prh_spec_stops_textlint(self):
        # specs は読み込むときに prh が確かめる。外れると、検査の全体が止まる（黙って通らない）
        shutil.copy(CONFIG, self.dir / ".textlintrc.json")
        (self.dir / "prh.yml").write_text(
            "version: 1\nrules:\n  - expected: plan mode\n    pattern: プランモード\n"
            "    specs:\n      - {from: プランモード, to: プラン モード}\n", encoding="utf-8")
        done = self.textlint(str(self.write("本文である。\n")), config=self.dir / ".textlintrc.json")
        self.assertNotEqual(done.returncode, 0)
        self.assertIn("spec failed", done.stdout + done.stderr)

    def test_known_gap_indented_bodies_after_a_blank_line_are_not_checked(self):
        # いまの限界：タブ（=== "…"）・囲み（!!! …）・折りたたみ（??? …）の中で、空行の後の字下げした段落は、
        # Markdown の字下げのコードとして読まれ、検査されない（手本の kyopro-atlas と同じ。build-B3.md の提案）。
        # この試験が落ちたら、限界が直ったので、試験と手引きを直す
        text = "\n".join([
            '=== "Claude Code"',
            "",
            "    プランモードで計画させる。",
            "",
            '!!! note "注意"',
            "",
            "    subagent に頼む。",
            "",
            "本文のプランモード。",
            "",
        ])
        _, messages = self.lint(text)
        self.assertEqual([(m["line"], m["fix"]["text"]) for m in messages if m["ruleId"] == "prh"], [(9, "plan mode")])


if __name__ == "__main__":
    unittest.main()
