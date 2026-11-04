"""手引きとチェックリスト（planning/guides/・planning/checklists/）の形の試験。
planning/guides/README.md §3 の直し方のうち、機械で確かめられるものを見る。

動かし方:
  uv run python -m unittest discover -s tests/guides
  （pyproject.toml がまだないときは uv run --no-project --python 3.12 --with pyyaml python -m unittest discover -s tests/guides）

見るもの:
  型の手引き    planning/guides/<型>.md が schema/site.yml の types と一対一にそろう。題名の行が型の名前を持つ。
                README の見本の表に、すべての型の行がある
  一覧          planning/guides/ と planning/checklists/ のファイルが、すべて planning/guides/README.md から指されている
  リンク        相対リンクの先のファイルがある
  中の参照      「共通の手引き §N」「共通の決まり §N」と、共通の手引きの中の「§N」の先の節がある
  元            各「## 」の節に「元：」の行がある。設計書・要件・catalog/README の節、design-review の DR、
                research の番号、元の行に書いた決定の日付・「項目」・方針の番号が、その文書にある
  検査の印      「（検査：X）」「（作る予定：X）」の X の形がそろう。検査：の道具（と検査の名前）がある。
                作る予定：の道具（と検査の名前）ができていたら、書き換えを求めて落ちる
  版            冒頭に「- 版：YYYY-MM-DD 第N版」の行がある
  末尾に足す形  見出しに「決めたこと」がなく、本文に「こちらを優先」がない（今有効な規則だけを置く）
"""
from __future__ import annotations

import os
import re
import unittest
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
PLANNING = REPO / "planning"
GUIDES = PLANNING / "guides"
CHECKLISTS = PLANNING / "checklists"
INDEX = GUIDES / "README.md"
COMMON_GUIDE = GUIDES / "common.md"
COMMON_CHECKLIST = CHECKLISTS / "common.md"
SITE_YML = REPO / "schema" / "site.yml"
DECISIONS = PLANNING / "decisions.md"
DESIGN_REVIEW = PLANNING / "design-review.md"
RESEARCH = PLANNING / "research"
NOT_TYPE_GUIDES = {"README.md", "common.md"}

# 節の番号で指す文書（指すときの語 → ファイル）
SECTION_DOCS = {
    "design": PLANNING / "design.md",
    "requirements": PLANNING / "requirements.md",
    "catalog/README": PLANNING / "catalog" / "README.md",
    "共通の手引き": COMMON_GUIDE,
    "共通の決まり": COMMON_CHECKLIST,
}
# 決定の方針の番号（design の「方針 A3」の読み方）：記号 → decisions.md の見出し
POLICY_HEADINGS = {
    "A": "### 書き方の方針（第三者・根拠・コンテスト）",
    "B": "### 書き方の方針（安全・面・表現）",
}

_SEC = r"§\d+(?:\.\d+)?(?: の\d+)?"
PREFIXED_RE = re.compile(r"(" + "|".join(re.escape(k) for k in SECTION_DOCS) + r") (" + _SEC + r"(?:・" + _SEC + r")*)")
SECTION_NUM_RE = re.compile(r"§(\d+(?:\.\d+)?)")
DR_RE = re.compile(r"design-review ((?:DR-\d+)(?:・DR-\d+)*)")
RESEARCH_RE = re.compile(r"research/(\d{2})(?!〜)")
POLICY_RE = re.compile(r"方針 ((?:[AB]\d(?:〜[AB]?\d)?)(?:・[AB]\d(?:〜[AB]?\d)?)*)")
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
QUOTE_RE = re.compile(r"「([^」]+)」")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
MARK_RE = re.compile(r"（(検査|作る予定)：([^（）]*)）")
MARK_BODY_RE = re.compile(r"^(?P<tool>[A-Za-z0-9_.-]+)(?P<args>(?: [^\s「」（）]+)*)(?:「(?P<label>[^「」]+)」)?$")
VERSION_RE = re.compile(r"^- 版：\d{4}-\d{2}-\d{2} 第\d+版")


def files() -> list[Path]:
    return sorted(GUIDES.glob("*.md")) + sorted(CHECKLISTS.glob("*.md"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def lines_outside_code(text: str) -> list[tuple[int, str]]:
    """コードの囲み（```）の外の行を (行番号, 行) で返す。囲みの中の例を規則として読まないため"""
    out, fenced = [], False
    for n, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append((n, line))
    return out


def has_section(doc: Path, number: str) -> bool:
    """doc に節 number（"6" なら「## 6. 」、"6.4" なら「### 6.4 」）の見出しがあるか"""
    head = f"### {number} " if "." in number else f"## {number}. "
    return any(line.startswith(head) for line in read(doc).splitlines())


def policy_count(letter: str) -> int:
    """decisions.md の方針の見出しの下にある、番号付きの項目の数"""
    text, heading = read(DECISIONS), POLICY_HEADINGS[letter]
    start = text.index(heading)
    body = text[start + len(heading):]
    end = re.search(r"^#", body, re.M)
    body = body[: end.start()] if end else body
    return len(re.findall(r"^\d+\. ", body, re.M))


def tool_sources() -> list[str]:
    return [read(p) for p in sorted((REPO / "tools").rglob("*.py"))] if (REPO / "tools").exists() else []


def tool_ready(tool: str, args: list[str], label: str | None) -> bool | None:
    """印の道具（と検査の名前）ができているか。True：できている、False：まだ、None：この試験が知らない道具"""
    if tool.endswith(".py"):
        path = REPO / "tools" / tool
        if not path.exists():
            return False
        src = read(path)
        if any(a.startswith("--") and a not in src for a in args):
            return False
        if label is None:
            return True
        registered = re.compile(r"check\(\s*[\"']" + re.escape(label) + r"[\"']")
        return any(registered.search(s) for s in tool_sources())
    if tool == "textlint":
        return any(REPO.glob(".textlintrc*"))
    if tool == "mkdocs":
        return (REPO / "mkdocs.yml").exists()
    if tool == "lychee":
        workflows = REPO / ".github" / "workflows"
        return workflows.exists() and any("lychee" in read(p) for p in workflows.glob("*.y*ml"))
    if re.fullmatch(r"H[1-4]", tool):   # design §10.5 の縛り（.claude/settings.json の deny と hooks）
        return (REPO / ".claude" / "settings.json").exists()
    return None


class TypeGuides(unittest.TestCase):
    def test_type_guides_match_site_types(self):
        types = yaml.safe_load(read(SITE_YML))["types"]
        found = {p.stem for p in GUIDES.glob("*.md") if p.name not in NOT_TYPE_GUIDES}
        self.assertEqual(set(types), found, "planning/guides/<型>.md は site.yml の types と一対一にする")

    def test_type_guide_title_names_the_type(self):
        for t in yaml.safe_load(read(SITE_YML))["types"]:
            first = read(GUIDES / f"{t}.md").splitlines()[0]
            self.assertEqual(first, f"# 型の手引き：{t}", f"planning/guides/{t}.md の1行目")

    def test_sample_table_has_every_type(self):
        text = read(INDEX)
        for t in yaml.safe_load(read(SITE_YML))["types"]:
            self.assertRegex(text, rf"(?m)^\| {re.escape(t)}[ （]", f"README §4 の見本の表に {t} の行がない")


class Index(unittest.TestCase):
    def test_every_file_is_listed_in_index(self):
        index = read(INDEX)
        for path in files():
            if path == INDEX:
                continue
            target = os.path.relpath(path, GUIDES)
            self.assertIn(f"]({target})", index, f"{rel(path)} が planning/guides/README.md から指されていない")


class References(unittest.TestCase):
    def test_relative_links_resolve(self):
        for path in files():
            for n, line in lines_outside_code(read(path)):
                for target in LINK_RE.findall(line):
                    if target.startswith(("http://", "https://", "mailto:", "#")):
                        continue
                    dest = (path.parent / target.split("#", 1)[0]).resolve()
                    self.assertTrue(dest.exists(), f"{rel(path)}:{n}: リンクの先 {target} がない")

    def test_section_refs_resolve(self):
        for path in files():
            for n, line in lines_outside_code(read(path)):
                for doc, chain in PREFIXED_RE.findall(line):
                    for number in SECTION_NUM_RE.findall(chain):
                        self.assertTrue(has_section(SECTION_DOCS[doc], number),
                                        f"{rel(path)}:{n}: {doc} §{number} の節がない")

    def test_bare_section_refs_in_common_guide_resolve(self):
        for n, line in lines_outside_code(read(COMMON_GUIDE)):
            rest = PREFIXED_RE.sub("", line)
            rest = re.sub(r"research/\d{2}[^、。）]*", "", rest)   # 調査資料の中の節は、ほかの試験が見る
            for number in SECTION_NUM_RE.findall(rest):
                self.assertTrue(has_section(COMMON_GUIDE, number), f"planning/guides/common.md:{n}: §{number} の節がない")

    def test_design_review_and_research_refs_resolve(self):
        review = read(DESIGN_REVIEW)
        for path in files():
            for n, line in lines_outside_code(read(path)):
                for chain in DR_RE.findall(line):
                    for dr in chain.split("・"):
                        self.assertRegex(review, rf"(?m)^### {dr} ", f"{rel(path)}:{n}: design-review の {dr} がない")
                for number in RESEARCH_RE.findall(line):
                    self.assertTrue(any(RESEARCH.glob(f"{number}-*.md")), f"{rel(path)}:{n}: research/{number} がない")


class Sources(unittest.TestCase):
    def test_every_section_cites_source(self):
        for path in files():
            sections: dict[str, bool] = {}   # 「## 」の節の題 → 「元：」の行があるか（コードの囲みの中の見出しは数えない）
            title = None
            for _, line in lines_outside_code(read(path)):
                if line.startswith("## "):
                    title = line[3:]
                    sections[title] = False
                elif title is not None and line.startswith("元："):
                    sections[title] = True
            for title, cited in sections.items():
                self.assertTrue(cited, f"{rel(path)}: 節「{title}」に「元：」の行がない")

    def test_decision_refs_in_source_lines_resolve(self):
        decisions = read(DECISIONS)
        dates = set(re.findall(r"(?m)^## (\d{4}-\d{2}-\d{2}) ", decisions))
        counts = {letter: policy_count(letter) for letter in POLICY_HEADINGS}
        for path in files():
            for n, line in lines_outside_code(read(path)):
                if not line.startswith("元：") or "decisions" not in line:
                    continue
                where = f"{rel(path)}:{n}"
                for date in DATE_RE.findall(line):
                    self.assertIn(date, dates, f"{where}: decisions.md に {date} の節がない")
                for item in QUOTE_RE.findall(line):
                    self.assertIn(item, decisions, f"{where}: decisions.md に「{item}」がない")
                for chain in POLICY_RE.findall(line):
                    for ref in re.split(r"[・〜]", chain):
                        letter = ref[0] if ref[0] in POLICY_HEADINGS else chain[0]
                        number = int(ref[-1])
                        self.assertTrue(1 <= number <= counts[letter], f"{where}: 方針 {letter}{number} がない")


class CheckMarks(unittest.TestCase):
    def marks(self):
        for path in files():
            for n, line in lines_outside_code(read(path)):
                for kind, body in MARK_RE.findall(line):
                    if body.startswith("<"):   # README の書き方の説明（<名前>）
                        continue
                    yield f"{rel(path)}:{n}", kind, body

    def test_marks_are_well_formed(self):
        for where, kind, body in self.marks():
            self.assertRegex(body, MARK_BODY_RE, f"{where}: 印の中は「道具 引数「検査の名前」」だけにする：（{kind}：{body}）")

    def test_existing_checks_exist_and_planned_checks_are_not_ready(self):
        for where, kind, body in self.marks():
            m = MARK_BODY_RE.match(body)
            if not m:
                continue   # 形は test_marks_are_well_formed が見る
            ready = tool_ready(m["tool"], m["args"].split(), m["label"])
            self.assertIsNotNone(ready, f"{where}: この試験が知らない道具：{m['tool']}（tool_ready に見方を足す）")
            if kind == "検査":
                self.assertTrue(ready, f"{where}: 道具か検査がない：（検査：{body}）")
            else:
                self.assertFalse(ready, f"{where}: 道具ができたので「検査：」に書き換える：（作る予定：{body}）")


class Form(unittest.TestCase):
    def test_version_line(self):
        for path in files():
            head = read(path).splitlines()[:6]
            self.assertTrue(any(VERSION_RE.match(line) for line in head), f"{rel(path)}: 冒頭に「- 版：…」の行がない")

    def test_no_appended_decision_sections(self):
        for path in files():
            for n, line in lines_outside_code(read(path)):
                if line.startswith("#"):
                    self.assertNotIn("決めたこと", line, f"{rel(path)}:{n}: 決定を末尾に足す形の見出し（今有効な規則の所を書き換える）")
                self.assertNotIn("こちらを優先", line, f"{rel(path)}:{n}: 「後の節が優先」の形にしない")


if __name__ == "__main__":
    unittest.main()
