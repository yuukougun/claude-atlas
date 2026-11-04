"""Markdown のページを読む部品：front matter と本文の分け方・フェンスのコード・見出し・目印（設計書 §8.4）。

目印は1行の HTML のコメントで、段落の中にも置ける:
  <!-- gen:begin 名前 --> … <!-- gen:end 名前 -->        生成の部分（名前は references・snippet <id>/<名前> など）
  <!-- fact:begin <id> --> … <!-- fact:end -->          変わりやすい値（data/facts.yml の facts の id）
  <!-- link:begin <id>[#<anchor>] --> … <!-- link:end -->  まだ公開していないかもしれないページへのリンク
  <!-- name:begin <id> --> … <!-- name:end -->          名前の今の呼び方（data/facts.yml の names の id）
フェンスのコードと、行の中のコード（`…`）の中の目印は読まない（目印の書き方を説明するページのため）。
対の合わないもの（閉じていない・begin のない end・名前の違う end・名前のない begin と gen:end）は Problem にする。
種類が違う目印は入れ子にしてよい（gen の中の fact など）。同じ種類の入れ子は誤りにする。

fence_spans は kyopro-atlas の tools/check_pages.py（同じ作者、MIT）から写した。
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from .base import Problem

FENCE_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})(?P<info>.*)$")
FENCE_CLOSE_RE = re.compile(r"^[ \t]*(`{3,}|~{3,})\s*$")
HEADING_RE = re.compile(r"^[ ]{0,3}(?P<hashes>#{1,6})(?:[ \t]+(?P<text>.*?))?[ \t]*$")
CLOSING_HASHES_RE = re.compile(r"(?:^|[ \t]+)#+[ \t]*$")
ATTR_ID_RE = re.compile(r"[ \t]*\{[^{}]*?#(?P<id>[A-Za-z0-9_:.-]+)[^{}]*\}[ \t]*$")
CODE_SPAN_RE = re.compile(r"(`+)(?:(?!\1).)+?\1")
MARKER_RE = re.compile(r"<!--[ \t]*(?P<kind>gen|fact|link|name):(?P<edge>begin|end)(?:[ \t]+(?P<arg>.*?))?[ \t]*-->")
MARKER_KINDS = ("gen", "fact", "link", "name")
FRONT_MATTER_OPEN = "---"
FRONT_MATTER_CLOSE = ("---", "...")


def split_front_matter(text: str) -> tuple[str | None, str, int, str | None]:
    """(front matter の YAML か None, 本文, 本文の1行目のファイルの行, 閉じていないときの理由)。
    front matter は1行目の --- から、次の --- か ... の行まで（MkDocs と同じ）。"""
    lines = text.split("\n")
    if not lines or lines[0].rstrip() != FRONT_MATTER_OPEN:
        return None, text, 1, None
    for i in range(1, len(lines)):
        if lines[i].rstrip() in FRONT_MATTER_CLOSE:
            return "\n".join(lines[1:i]), "\n".join(lines[i + 1:]), i + 2, None
    return None, text, 1, "front matter が閉じていない（--- の行がない）"


def parse_lang(info: str) -> str:
    s = info.strip()
    if s.startswith("{"):
        s = s.strip("{} ")
    tok = s.split()[0] if s.split() else ""
    return tok.lstrip(".").rstrip("}").lower()


def fence_spans(lines: list[str]) -> list[tuple[int, int, str, str]]:
    """フェンスのコードの範囲 (開始行, 終了行, 言語, 字下げ)（0 始まり、終了行を含む。閉じていなければ最後まで）。"""
    spans = []
    i = 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i])
        if not m or (m.group("fence")[0] == "`" and "`" in m.group("info")):
            i += 1
            continue
        ch, n = m.group("fence")[0], len(m.group("fence"))
        j = i + 1
        while j < len(lines):
            c = FENCE_CLOSE_RE.match(lines[j])
            if c and c.group(1)[0] == ch and len(c.group(1)) >= n:
                break
            j += 1
        spans.append((i, min(j, len(lines) - 1), parse_lang(m.group("info")), m.group("indent")))
        i = j + 1
    return spans


def fenced_mask(lines: list[str], spans=None) -> list[bool]:
    """行ごとに、フェンスのコード（開きと閉じの行を含む）の中か。"""
    mask = [False] * len(lines)
    for a, b, _, _ in (fence_spans(lines) if spans is None else spans):
        for k in range(a, b + 1):
            mask[k] = True
    return mask


def mask_code_spans(line: str) -> str:
    """行の中のコード（`…`）を、同じ長さの空白にする（位置は変えない）。"""
    return CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), line)


@dataclass(frozen=True)
class Heading:
    level: int                # # の数
    text: str                 # 見出しの文字（{#anchor} と閉じの # は除く）
    anchor: str | None        # {#anchor} で書いた anchor（なければ None）
    line: int                 # ファイルの行


def find_headings(lines: list[str], mask: list[bool], first_line: int) -> list[Heading]:
    """ATX の見出し（フェンスの外。字下げは3つまで）。"""
    out = []
    for i, raw in enumerate(lines):
        if mask[i]:
            continue
        m = HEADING_RE.match(raw.rstrip("\r"))
        if not m:
            continue
        text = CLOSING_HASHES_RE.sub("", m.group("text") or "")
        anchor = None
        a = ATTR_ID_RE.search(text)
        if a:
            anchor = a.group("id")
            text = text[:a.start()]
        out.append(Heading(len(m.group("hashes")), text.strip(), anchor, first_line + i))
    return out


@dataclass
class Marker:
    """本文の目印の1組。位置（start など）は本文（front matter の後）の中の文字の位置で、作る層が中身を
    書き換えるときに使う：body[start:inner_start] が begin、body[inner_start:inner_end] が中身、
    body[inner_end:stop] が end。閉じていなければ end の側は None。"""

    kind: str                 # gen・fact・link・name
    arg: str                  # gen は名前、fact は数値の id、link は id か id#anchor、name は names の id
    line: int                 # begin のファイルの行
    start: int
    inner_start: int
    end_line: int | None = None
    inner_end: int | None = None
    stop: int | None = None

    @property
    def closed(self) -> bool:
        return self.stop is not None

    @property
    def name(self) -> str:
        """gen の名前・fact の id・link の参照（arg のこと）。"""
        return self.arg

    def content(self, body: str) -> str | None:
        return body[self.inner_start:self.inner_end] if self.closed else None


def find_markers(body: str, lines: list[str], mask: list[bool], first_line: int,
                 file: str = "", page: str = "-") -> tuple[list[Marker], list[Problem]]:
    """本文の目印を読む。lines は body を \\n で分けたもの、mask はフェンスの中か、first_line は本文の1行目の行。"""
    offsets = []
    pos = 0
    for raw in lines:
        offsets.append(pos)
        pos += len(raw) + 1
    markers: list[Marker] = []
    problems: list[Problem] = []
    open_: dict[str, Marker] = {}

    def problem(line: int, message: str) -> None:
        problems.append(Problem(file, line, message, "目印", page))

    for i, raw in enumerate(lines):
        if mask[i] or "<!--" not in raw:
            continue
        line = first_line + i
        for m in MARKER_RE.finditer(mask_code_spans(raw)):
            kind, edge = m.group("kind"), m.group("edge")
            arg = raw[m.start("arg"):m.end("arg")].strip() if m.group("arg") is not None else ""
            start, stop = offsets[i] + m.start(), offsets[i] + m.end()
            if edge == "begin":
                prev = open_.pop(kind, None)
                if prev is not None:
                    problem(prev.line, f"{kind}:begin「{prev.arg}」が閉じる前に、{line} 行に次の {kind}:begin がある"
                                       f"（同じ種類の目印は入れ子にしない）")
                    markers.append(prev)
                if not arg:
                    problem(line, f"{kind}:begin に名前（{'id' if kind != 'gen' else '生成の名前'}）がない")
                open_[kind] = Marker(kind, arg, line, start, stop)
                continue
            mk = open_.pop(kind, None)
            if mk is None:
                problem(line, f"対になる {kind}:begin のない {kind}:end")
                continue
            if arg and arg != mk.arg:
                problem(line, f"{kind}:end の名前「{arg}」が、{mk.line} 行の {kind}:begin の「{mk.arg}」と違う")
            elif kind == "gen" and not arg:
                problem(line, f"gen:end に名前がない（{mk.line} 行の gen:begin と同じ「{mk.arg}」を書く）")
            mk.end_line, mk.inner_end, mk.stop = line, start, stop
            markers.append(mk)
    for mk in open_.values():
        problem(mk.line, f"{mk.kind}:begin「{mk.arg}」が閉じていない（{mk.kind}:end がない）")
        markers.append(mk)
    markers.sort(key=lambda x: x.start)
    return markers, problems
