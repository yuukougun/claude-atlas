"""作る層の文字の部品：Markdown の書き方（エスケープ・表・相対リンク・最初の文）・YAML と JSON の書き方。

生成物は同じ入力からいつも同じ文字列になるように書く（design §8.4。日時・ハッシュを入れない）。
"""
from __future__ import annotations

import json
import posixpath
import unicodedata

import yaml

GEN_MARK = "<!-- tools/gen_site.py が生成する。手で直さない -->"
TEXTLINT_OFF = "<!-- textlint-disable -->"     # 生成の部分は目次の題名・別名・サインを写すので、書き方の検査から外す
TEXTLINT_ON = "<!-- textlint-enable -->"       # （B3 の報告の P2。手本の gen_site.py と同じ）

# Python-Markdown の \ で外せる字（ESCAPED_CHARS のうち、文の中で働きうるもの）。< と > は文字参照にする
_BACKSLASH = set("\\`*_[]{}")


def plain(s) -> str:
    """改行と続く空白を1つの空白にした文字列（平文の欄を1行に書くため）。"""
    return " ".join(str(s).split())


def md_text(s, table: bool = False) -> str:
    """平文を Markdown の文の中に置ける形にする（記法の字を外す。表のセルなら | も）。"""
    out = []
    for ch in plain(s):
        if ch in _BACKSLASH:
            out.append("\\" + ch)
        elif ch == "<":
            out.append("&lt;")
        elif ch == ">":
            out.append("&gt;")
        elif ch == "|" and table:
            out.append("\\|")
        else:
            out.append(ch)
    return "".join(out)


def table(header: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join("---" for _ in header) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def first_sentence(s: str) -> str:
    """かっこの外の最初の「。」までの文（なければ全部）。"""
    s = plain(s)
    depth = 0
    for i, ch in enumerate(s):
        if ch in "（(「『【":
            depth += 1
        elif ch in "）)」』】":
            depth = max(0, depth - 1)
        elif ch == "。" and depth == 0:
            return s[:i + 1]
    return s


def rel_md(host: str, target: str) -> str:
    """docs/ の中の Markdown（host）から、docs/ の中のファイル（target）への相対リンク（MkDocs が検査する形）。"""
    base = posixpath.dirname(host) or "."
    return posixpath.relpath(target, base)


def url_prefix(url: str) -> str:
    """ページの URL（サイトの根から。start/how-to-use/）から、サイトの根への相対の前置き（../../）。"""
    depth = len([x for x in url.split("/") if x])
    return "../" * depth


def yaml_scalar(s: str) -> str:
    """YAML のキーか値として安全なら素のまま、そうでなければ二重引用符で書く（手本の gen_site.py と同じ）。"""
    try:
        if s and s == s.strip() and "#" not in s and yaml.safe_load(f"{s}: x") == {s: "x"}:
            return s
    except yaml.YAMLError:
        pass
    return json.dumps(s, ensure_ascii=False)


def dumps(v) -> str:
    """JSON の1行（キーの並びは作った順。ASCII でない字もそのまま）。"""
    return json.dumps(v, ensure_ascii=False, separators=(",", ":"))


def json_document(head: dict, lists: dict[str, list]) -> str:
    """JSON のファイル：head の項目を1行ずつ、lists の各リストは1要素1行（差分を読みやすく、並列の直しで衝突しにくく）。"""
    parts = [f"{dumps(k)}:{dumps(v)}" for k, v in head.items()]
    for k, items in lists.items():
        if not items:
            parts.append(f"{dumps(k)}:[]")
            continue
        body = ",\n".join(dumps(x) for x in items)
        parts.append(f"{dumps(k)}:[\n{body}\n]")
    return "{\n" + ",\n".join(parts) + "\n}\n"


def front(title: str, search_exclude: bool = False) -> str:
    """生成するページの front matter と、手で直さない印。"""
    fm = f"---\ntitle: {yaml_scalar(title)}\n"
    if search_exclude:
        fm += "search:\n  exclude: true\n"
    return fm + "---\n\n" + GEN_MARK + "\n\n"


def norm_key(s: str) -> str:
    """語を比べる形（NFKC・小文字・空白を1つ）。"""
    return " ".join(unicodedata.normalize("NFKC", str(s)).casefold().split())


def join_marks(parts: list[str]) -> str:
    parts = [p for p in parts if p]
    return f"（{'・'.join(parts)}）" if parts else ""
