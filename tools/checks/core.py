"""検査の層の登録の仕組み（設計書 §8.3「検査1つを関数1つにして登録する」）。

検査は `@check(名前, 重さ, 当てるもの…)` で登録した関数で、Context（tools/checks/context.py）を受け取り、Finding を
返す。重さは登録のときに決め、Finding の severity で1件ごとに変えられる（骨格のページだけが指すものを警告に下げる、
など）。当てるものは FRONT_MATTER（docs/ と stubs/ のページと data/）・CATALOG（目次 planning/catalog/）・TEMPLATES
（雛形 snippets/ と .claude/settings.json）。前提と関連の規則は FRONT_MATTER と CATALOG の両方に当てる（同じ関数）。

出力は tools/check_catalog.py と同じ形の1件1行：「エラー: <ファイル>:<行>: <ページの id>: [<検査>] <内容>」。
ページに関わらない指摘は id を「-」にする。
"""
from __future__ import annotations

import collections
from dataclasses import dataclass
from typing import Callable, Iterable

ERROR, WARNING = "エラー", "警告"
FRONT_MATTER, CATALOG, TEMPLATES = "front matter", "catalog", "templates"
TARGETS = (FRONT_MATTER, CATALOG, TEMPLATES)


@dataclass(frozen=True)
class Finding:
    """検査の関数が返す1件。pages は関わるページの id（--page で選ぶ。page の id は数えなくても入る）。"""

    file: str
    line: int | None
    page: str
    message: str
    pages: frozenset[str] = frozenset()
    severity: str | None = None            # None なら登録の重さ


@dataclass(frozen=True)
class Check:
    name: str
    severity: str
    func: Callable
    targets: frozenset[str]

    @property
    def summary(self) -> str:
        """docstring の最初の段落を1行にする（折り返しの両側が英数字のときだけ空白を入れる）。"""
        out = ""
        for line in (x.strip() for x in (self.func.__doc__ or "").strip().split("\n\n")[0].splitlines()):
            if out and line and out[-1].isascii() and out[-1].isalnum() and line[0].isascii() and line[0].isalnum():
                out += " "
            out += line
        return out


CHECKS: list[Check] = []


def check(name: str, severity: str, *targets: str):
    """検査を登録する。targets を省くと FRONT_MATTER。同じ名前を同じものに二度は登録しない。"""
    targets = targets or (FRONT_MATTER,)
    for t in targets:
        if t not in TARGETS:
            raise ValueError(f"知らない当てるもの: {t}")

    def register(func):
        for c in CHECKS:
            if c.name == name and c.targets & set(targets):
                raise ValueError(f"検査「{name}」を二度登録した")
        CHECKS.append(Check(name, severity, func, frozenset(targets)))
        return func
    return register


def checks_for(target: str) -> list[Check]:
    return [c for c in CHECKS if target in c.targets]


@dataclass(frozen=True)
class Issue:
    severity: str
    check: str
    file: str
    line: int | None
    page: str
    message: str
    pages: frozenset[str]


def run_checks(ctx, checks: Iterable[Check] | None = None) -> list[Issue]:
    """検査を流して、指摘を（重さ・ファイル・行・検査の順に）並べて返す。同じ指摘は1件にする。"""
    selected = checks_for(ctx.target) if checks is None else list(checks)
    order = {c.name: i for i, c in enumerate(CHECKS)}
    issues: list[Issue] = []
    seen: set[tuple] = set()
    for c in selected:
        for f in c.func(ctx):
            pages = set(f.pages)
            if f.page and f.page != "-":
                pages.add(f.page)
            issue = Issue(f.severity or c.severity, c.name, f.file, f.line, f.page, f.message, frozenset(pages))
            key = (issue.severity, issue.check, issue.file, issue.line, issue.page, issue.message)
            if key not in seen:
                seen.add(key)
                issues.append(issue)
    issues.sort(key=lambda i: (i.severity != ERROR, i.file, i.line or 0, order.get(i.check, 0)))
    return issues


def format_issue(i: Issue) -> str:
    loc = f"{i.file}:{i.line}" if i.line else i.file
    message = i.message.replace("\r", " ").replace("\n", " ")
    return f"{i.severity}: {loc}: {i.page}: [{i.check}] {message}"


def joined(values: Iterable[str]) -> str:
    return "・".join(values)


def summary_line(errors: list[Issue], warnings: list[Issue], read: str, scope: str = "", quiet: bool = False) -> str:
    """最後の行：「エラー N 件（検査 n …）、警告 M 件（…）（read）」。"""
    order = {c.name: i for i, c in enumerate(CHECKS)}

    def part(label: str, items: list[Issue]) -> str:
        c = collections.Counter(i.check for i in items)
        detail = joined(f"{k} {c[k]}" for k in sorted(c, key=lambda k: order.get(k, 0)))
        return f"{label} {len(items)} 件" + (f"（{detail}）" if detail else "")

    hidden = "。-q で出していない" if quiet and warnings else ""
    return f"{scope}{part(ERROR, errors)}、{part(WARNING, warnings)}{hidden}（{read}）"


def checks_epilog(target: str) -> str:
    """-h の末尾に出す検査の一覧。"""
    out = []
    for sev, effect in ((ERROR, "終了コードを 1 にする"), (WARNING, "終了コードは変えない")):
        items = [c for c in checks_for(target) if c.severity == sev]
        if items:
            out.append(f"検査（{sev}。{effect}）:")
            out += [f"  [{c.name}] {c.summary}" for c in items]
    return "\n".join(out)
