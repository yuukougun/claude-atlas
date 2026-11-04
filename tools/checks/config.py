"""検査が読む設定のファイル：nav.yml（ナビゲーションと exclude_docs）と .claude/settings.json（deny ルール）。

nav.yml（mkdocs.yml が INHERIT で読む。2段目から tools/gen_site.py が生成する）:
  nav            ナビゲーション。文字列・{題: パス}・{題: [入れ子]} の形を読み、.md のパスを集める
  extra.ca.surfaces  面の id → 表示の名前（作る層が tools/gen/config.yml の labels から書く。面のタブの名前に使う）
  exclude_docs   ビルドから外すファイル（gitignore の形。MkDocs は docs/ からの相対パスに当てる）。公開から外した
                 試作のページ（design §8.4 の未公開のページ）は、ここで外す。検査の層は、ここに当たる docs/ のページを
                 公開しないページ（Atlas の held_back）として数える
gitignore の形の当て方は git の決まりの近似：/ で始まるか途中に / があるものは根から、ないものはどの深さの名前にも
当てる。* は / をまたがず、** はまたぐ。末尾の / はフォルダだけ。! は外したものを戻す。フォルダに当たれば中の
ファイルにも当たる。

.claude/settings.json：permissions.deny の文字列のリスト。WebFetch(domain:…) が AI の利用を断るドメイン（H1）、
Edit(/…) が生成物のパス（H2）。.claude/hooks/pre_tool_use.py と同じ読み方。
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from lib import Problem
from lib.yamlio import read_yaml

NAV_FILE = "nav.yml"
SETTINGS_FILE = ".claude/settings.json"


# ---------------------------------------------------------------- gitignore の形


def _glob_part(pattern: str) -> str:
    out, i = [], 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out.append("(?:[^/]+/)*")
            i += 3
        elif pattern.startswith("**", i):
            out.append(".*")
            i += 2
        elif pattern[i] == "*":
            out.append("[^/]*")
            i += 1
        elif pattern[i] == "?":
            out.append("[^/]")
            i += 1
        elif pattern[i] == "[":
            j = pattern.find("]", i + 1)
            if j < 0:
                out.append(re.escape(pattern[i]))
                i += 1
            else:
                body = pattern[i + 1:j]
                if body.startswith("!"):
                    body = "^" + body[1:]
                out.append("[" + body.replace("\\", "\\\\") + "]")
                i = j + 1
        elif pattern[i] == "\\" and i + 1 < len(pattern):
            out.append(re.escape(pattern[i + 1]))
            i += 2
        else:
            out.append(re.escape(pattern[i]))
            i += 1
    return "".join(out)


@dataclass(frozen=True)
class IgnoreRule:
    raw: str
    negate: bool
    dir_only: bool
    regex: re.Pattern


def parse_ignore(lines) -> list[IgnoreRule]:
    """gitignore の形の行（空行と # の行は飛ばす）を規則にする。"""
    rules = []
    for raw in lines:
        s = raw.rstrip("\n").rstrip()
        if not s or s.startswith("#"):
            continue
        negate = s.startswith("!")
        if negate:
            s = s[1:]
        dir_only = s.endswith("/")
        s = s.rstrip("/")
        if not s:
            continue
        anchored = "/" in s
        s = s.lstrip("/")
        body = _glob_part(s)
        regex = re.compile(("^" if anchored else "^(?:.*/)?") + body + "$")
        rules.append(IgnoreRule(raw.strip(), negate, dir_only, regex))
    return rules


def ignored(rules: list[IgnoreRule], path: str) -> bool:
    """path（/ 区切りの相対パス。ファイル）が規則に当たるか（後の規則が勝つ。フォルダに当たれば中も当たる）。"""
    parts = path.strip("/").split("/")
    result = False
    for rule in rules:
        hit = False
        for k in range(1, len(parts) + 1):
            if k == len(parts) and rule.dir_only:
                break
            if rule.regex.match("/".join(parts[:k])):
                hit = True
                break
        if hit:
            result = not rule.negate
    return result


# ---------------------------------------------------------------- nav.yml


@dataclass
class Nav:
    file: str
    present: bool
    entries: list[str] = field(default_factory=list)          # nav の .md（docs/ からの相対）
    exclude: list[IgnoreRule] = field(default_factory=list)
    exclude_line: int | None = None
    nav_line: int | None = None
    surface_labels: dict[str, str] = field(default_factory=dict)   # extra.ca.surfaces（面の id → 表示の名前。作る層が書く）
    problems: list[Problem] = field(default_factory=list)

    def excluded(self, rel: str) -> bool:
        """docs/ からの相対パスが exclude_docs に当たるか。"""
        return ignored(self.exclude, rel)


def _nav_paths(node, out: list[str]) -> None:
    if isinstance(node, str):
        s = node.strip()
        if s.endswith(".md") and "://" not in s:
            out.append(s.lstrip("/"))
    elif isinstance(node, list):
        for x in node:
            _nav_paths(x, out)
    elif isinstance(node, dict):
        for v in node.values():
            _nav_paths(v, out)


def load_nav(root: Path) -> Nav:
    path = Path(root) / NAV_FILE
    nav = Nav(NAV_FILE, path.exists())
    if not nav.present:
        nav.problems.append(Problem(NAV_FILE, None, "nav.yml がない（ナビゲーションと exclude_docs を検査しない）", "設定"))
        return nav
    doc = read_yaml(path)
    nav.problems += doc.problems(NAV_FILE)
    if doc.error is not None:
        return nav
    if not isinstance(doc.data, dict):
        nav.problems.append(Problem(NAV_FILE, None, "最上位をマッピング（nav・exclude_docs）にする", "形"))
        return nav
    lines = getattr(doc.data, "key_lines", None) or {}
    nav.nav_line = lines.get("nav")
    nav.exclude_line = lines.get("exclude_docs")
    _nav_paths(doc.data.get("nav"), nav.entries)
    extra = doc.data.get("extra")
    ca = extra.get("ca") if isinstance(extra, dict) else None
    labels = ca.get("surfaces") if isinstance(ca, dict) else None
    if isinstance(labels, dict):
        nav.surface_labels = {str(k): str(v) for k, v in labels.items() if isinstance(v, str) and v.strip()}
    ex = doc.data.get("exclude_docs")
    if isinstance(ex, str):
        nav.exclude = parse_ignore(ex.splitlines())
    elif ex is not None:
        nav.problems.append(Problem(NAV_FILE, nav.exclude_line, "exclude_docs を文字列（1行に1つのパターン。| の形）にする", "形"))
    return nav


# ---------------------------------------------------------------- .claude/settings.json


@dataclass
class Settings:
    file: str
    present: bool
    deny: list[str] | None = None            # 読めなければ None
    problems: list[Problem] = field(default_factory=list)

    def noai_domains(self) -> list[str]:
        """deny の WebFetch(domain:…) のドメイン（*. を外す。.claude/hooks/pre_tool_use.py の noai_domains と同じ）。"""
        out: list[str] = []
        for rule in self.deny or []:
            m = re.match(r"^WebFetch\(domain:([^)]+)\)$", rule)
            if not m:
                continue
            d = m.group(1).strip().lower().rstrip(".")
            if d.startswith("*."):
                d = d[2:]
            if d and "*" not in d and d not in out:
                out.append(d)
        return out

    def generated_patterns(self) -> list[str]:
        """deny の Edit(/…) のパス（根からの相対。先頭の / を外したもの）。"""
        out = []
        for rule in self.deny or []:
            m = re.match(r"^Edit\(/([^/][^)]*)\)$", rule)
            if m:
                out.append(m.group(1))
        return out


def load_settings(root: Path) -> Settings:
    path = Path(root) / SETTINGS_FILE
    s = Settings(SETTINGS_FILE, path.exists())
    if not s.present:
        s.problems.append(Problem(SETTINGS_FILE, None, ".claude/settings.json がない（断るドメインと deny を検査しない）", "設定"))
        return s
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        s.problems.append(Problem(SETTINGS_FILE, getattr(e, "lineno", None), f"JSON が読めない: {e}", "設定"))
        return s
    deny = data.get("permissions", {}).get("deny") if isinstance(data, dict) and isinstance(data.get("permissions"), dict) else None
    if isinstance(deny, list) and all(isinstance(x, str) for x in deny):
        s.deny = deny
    else:
        s.deny = []
        if deny is not None:
            s.problems.append(Problem(SETTINGS_FILE, None, "permissions.deny が文字列のリストでない", "設定"))
    return s
