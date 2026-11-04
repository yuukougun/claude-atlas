#!/usr/bin/env python3
"""ページごとの「材料の束」を state/packets/<id>.md に作る（decisions 2026-11-04「執筆の担当が開く一次資料」。工程7）。
執筆の担当が、手引き・目次・調査資料・data を小分けに読む道具の呼び出しを減らし、束と手引き2つ（共通と型）だけを読んで
書けるようにする。state/ は git で追跡しない。束は道具が作る（手で直さない。作り直すと上書きする）。

使い方:
  uv run python tools/make_packet.py <id> [<id> …]   そのページの束を作る
  uv run python tools/make_packet.py --wave1         第一波の全ページ（site.yml の first_wave と front matter から閉包を出す。
                                                     数え方は tools/check_catalog.py と同じ）
  uv run python tools/make_packet.py --all           全ページ（stubs/ と docs/ のページ）
  uv run python tools/make_packet.py … --out DIR     束を書く先（既定は state/packets）
  uv run python tools/make_packet.py … --stats       束の大きさ（文字数）を、節ごとと材料の抜き出しの内訳つきで出す
  uv run python tools/make_packet.py … --item-limit N     材料の抜き出し1項目の上限（字。既定 3000）
  uv run python tools/make_packet.py … --packet-limit N   1つの束の大きさの目安（字。既定 60000）。超えるときは
                                                     材料の抜き出しの上限を下げて作り直す（--stats に出す）
  uv run python tools/make_packet.py … --root DIR    DIR を根にする（試験用。DIR/schema・DIR/stubs・DIR/docs・DIR/data・
                                                     DIR/planning）
終了コード: 0＝作り終えた、1＝id のページがない（ほかのページの束は作る）、2＝読めない（site.yml がない・引数がない など）

束の中身（Markdown。節の番号は固定）:
  1 ページ              front matter（stubs/ か docs/）の id・分野・型・level・優先度・題名・要約・signs・sections・volatility
                        と、本文を結び付ける aliases・面・原理・原因・場面
  2 つながるページ      prerequisites・related・routes（cause ごと）の先の id・題名・要約・型（id#anchor は節も）
  3 目次の情報          planning/catalog/<field>.yaml の同じ id の templates・visual・notes・level_evidence と materials の一覧
  4 data               tracks の機能（data/facts.yml の features）・outdated_advice の台帳の行（data/outdated-advice.yml）・
                        それに関わる names
  5 出典の一覧          planning/batches/step6/data/wave1-sources.yml のそのページの sources を、data/sources.yml の
                        題名・URL・種類で（なければ「一覧なし」）。data の項目が挙げる出典も添える
  6 材料の抜き出し      materials の各項目を planning/research/ の節・表の行・箇条にたどって写す（下の規則）
  7 書き方              読む手引きの場所と、報告の置き場所（指示に従う）

材料の抜き出し（6）の規則:
  - 頭の数字（00・01・…・11・11a〜11c・20〜28。research/ が付いてもよい）で planning/research/ のファイルを決める。
    requirements・design・decisions・design-review・format-and-operations・catalog/README は planning/ の同名のファイル、
    p12#N・p34#N・p56#N は 11a・11b・11c の論点の一覧の行。それ以外の頭（kyopro-atlas の手本・registry など）は
    「対象外：<項目>」と書いて写さない
  - 項目の中の印をたどる：§3・§3.1・§1-5（見出しの番号）、分野08・第10章・第1節・付録A-6（見出し）、Q8・KQ4・F6・T1・E・
    D-2・0-4・A-14・C-1〜C-12・(b)（見出し・太字の見出し・表の1列目・箇条の頭の印）、#45・p56#11（表の行）、「…」や語
    （見出し・太字の見出し・表の1列目の文字）、の4（番号つきの箇条。なければ表の4行目）。「・」「、」で印を分け、空白で
    前の印から絞る（第1節 分野01 p56#11。単独の印は前の組の絞り込みを引き継ぐ：Q4 T1・T2）。絞った所になければファイル全体を探す
  - （…）の注は印に数えない。同じ語の見出しが複数あるときの絞り込み、印が語で見つからないときに注が行の題そのものなら
    その行、切るときに残す段落を選ぶ手がかりの語、注に「注記」「訂正」があれば表の後の注記を添える、にだけ使う
  - 見つけたら、その見出しの節（次の同じ深さの見出しまで）・太字の見出しの段落（次の太字の見出しまで）・表の行（表の見出しつき。
    同じ表の行は1つにまとめる）・箇条を写す。表の後の【2026-11-03 注記】は、写した行に触れているものを添える。
    【2026-11-03 訂正】【2026-11-03 注記】はその印ごと写す
  - 1項目あたりの上限（--item-limit）を超えるときは切り、「…（略）」と全文の行の範囲を書く。切るときも、表の見出し・見出し・
    印の付いた所は残し、注の手がかりの語を含む段落や行を先に残す
  - 印が語で、手前で絞れた所があるのに語が見つからないときは、その所を写して「見つからない：<項目>（…）」と書く。
    見つからなければ「見つからない：<項目>（理由）」と書く
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib import Fatal, load_atlas, load_catalog  # noqa: E402
from lib.base import Ref  # noqa: E402
from lib.markdown import fence_spans, fenced_mask, find_headings  # noqa: E402
from lib.yamlio import read_yaml, to_jsonable  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
RESEARCH_DIR = "planning/research"
GUIDES_DIR = "planning/guides"
WAVE1_SOURCES = "planning/batches/step6/data/wave1-sources.yml"
DEFAULT_OUT = "state/packets"
ITEM_LIMIT = 3000            # 材料の抜き出し1項目の上限（字）
MIN_ITEM_LIMIT = 600         # 束が大きいときに上限を下げる下限
PACKET_LIMIT = 60000         # 1つの束の大きさの目安（字）
LIMIT_STEP = 0.7             # 束が大きいときの上限の下げ方（掛ける数）
MIN_PIECE = 240              # 1項目の中の1つの写しに配る字の下限
MARK_CAP = 520               # 印（【2026-11-03 訂正】【2026-11-03 注記】）の付いた1まとまりを残す字の上限
MARK_SHARE = 0.65            # 切るとき、印の付いたまとまりに使う字の割合の上限
PRE_CAP = 360                # 印の付いた注記が直す直前の段落を添える字の上限
SHORT_MARK = (110, 300)      # 手がかりの語に当たらない印のまとまりを残す字の下限と上限
NOTES_SHARE = 0.35           # 表の後に添えた注記に使う字の割合の上限（写した行を押しのけない）
NOTES_FEW = 3                # 「注記つき」のとき、表の後の注記がこれ以下なら、行に触れていなくても全部添える
MAX_SCOPES = 8               # 前の印で絞る所の数の上限
MAX_RANGE = 200              # C-1〜C-12 のような範囲の数の上限
HEAD_KINDS = ("heading", "label")
MARK_RE = re.compile(r"【\d{4}-\d{2}-\d{2}\s*(?:訂正|注記)】")
DROP_KEYS = {"features": ("match_terms",)}   # data の写しから省く、道具だけが使うキー

# planning/ の計画の資料（頭の名前 → ファイル）
PLAN_DOCS = {
    "requirements": "planning/requirements.md",
    "design-review": "planning/design-review.md",
    "design": "planning/design.md",
    "decisions": "planning/decisions.md",
    "format-and-operations": "planning/format-and-operations.md",
    "catalog/README": "planning/catalog/README.md",
    "progress": "planning/progress.md",
}
_PLAN_NAMES = "|".join(re.escape(k) for k in PLAN_DOCS)
PLAN_HEAD_RE = re.compile(r"^(" + _PLAN_NAMES + r")(?![\w-])")
RESEARCH_HEAD_RE = re.compile(r"^(?:research/)?(\d{2}[a-c]?)(?=[\s　§「\x01]|$)")
PBARE_HEAD_RE = re.compile(r"^p(12|34|56)#(\d+)")
PATH_HEAD_RE = re.compile(r"^(planning/[\w./-]+\.md)")
P_FILES = {"12": "11a", "34": "11b", "56": "11c"}   # p12#N は 11a の #N
# 「、」「・」で別の資料に移る所（research/20 A4・I4、format-and-operations L15。11 第4節 #32・research/24 B-32）
SOURCE_BOUNDARY_RE = re.compile(r"(?:[、,，・]|と)\s*(?=(?:research/\d{2}[a-c]?\b|" + _PLAN_NAMES + r")(?![\w-]))")


# ---------------------------------------------------------------- 正規化


def nfkc(s: str) -> str:
    return unicodedata.normalize("NFKC", s)


def norm_text(s: str) -> str:
    """文字の照合用：全角を半角に、空白・記号・引用符を除き、小文字にする。"""
    return re.sub(r"[\W_]+", "", nfkc(s)).casefold()


def squash(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def plain(s: str) -> str:
    """Markdown の強調とコードの印を除く。"""
    return s.replace("**", "").replace("`", "").strip()


KQ_RE = re.compile(r"^Key Question\s+(\d+)", re.I)


def head_key(text: str) -> str:
    """見出し・太字の見出し・表の1列目・箇条の頭の「印」（"3.1"・"1-5"・"q8"・"w7"・"分野18"・"第10章"・"kq4"）。"""
    s = nfkc(plain(text))
    m = KQ_RE.match(s)
    if m:
        return "kq" + m.group(1)
    if m := re.match(r"^(\d+(?:[.\-]\d+)*)\.(?=\D)", s):          # "2.見出し"（空白のない番号）
        return m.group(1)
    tok = re.split(r"[\s:、，,(]", s, maxsplit=1)[0]
    if not tok:
        tok = s.split()[0] if s.split() else ""
    return tok.rstrip(".。★☆").casefold()


TERM_RE = re.compile(r"p\d{2}#\d+|[一-龥々〆ヵヶァ-ヴー]{2,}|[A-Za-z][A-Za-z0-9_.\-]{2,}|\d{2,}")
STOP_TERMS = {"注記つき", "注記", "訂正", "段落", "本文", "冒頭", "末尾", "つき", "ページ", "項目", "中身"}


def hint_terms(notes: list[str]) -> list[str]:
    """項目の（…）の注から、どの段落・どの行が要るかの手がかりの語を取る（漢字・カタカナの2字以上の連なり、英数字の3字以上）。"""
    terms: list[str] = []
    for n in notes:
        for m in TERM_RE.finditer(nfkc(n)):
            t = m.group(0).casefold()
            if t not in STOP_TERMS and t not in terms:
                terms.append(t)
    return terms


def clip_text(text: str, n: int) -> str:
    """n 字以内にする。印（【2026-11-03 訂正】など）が切る所より後にあるときは、印のある所を残す。"""
    if len(text) <= n:
        return text
    m = MARK_RE.search(text)
    if m and m.start() >= n - 20 and n >= 80:
        head = max(n // 3, 40)
        tail = n - head - 2
        piece = text[m.start():m.start() + tail]
        return text[:head].rstrip() + "…" + piece + ("…" if m.start() + tail < len(text) else "")
    return text[:max(n - 1, 1)].rstrip() + "…"


# ---------------------------------------------------------------- 資料の読み方（見出し・太字の見出し・表の行・箇条）


@dataclass
class Table:
    start: int
    end: int
    header: int | None
    sep: int | None


@dataclass
class Anchor:
    """資料の中の、印で引ける1か所。start と end は行（0 から。end は含まない）。"""

    kind: str                  # heading・label（太字の見出し）・row（表の行）・item（箇条）
    start: int
    end: int
    key: str = ""
    extra: tuple[str, ...] = ()
    raw: str = ""
    level: int = 0
    table: Table | None = None
    _norm: str | None = None

    @property
    def norm(self) -> str:
        if self._norm is None:
            self._norm = norm_text(self.raw)
        return self._norm

    def has_key(self, k: str) -> bool:
        return bool(k) and (k == self.key or k in self.extra)


TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)*\|?\s*$")
HR_RE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
LABEL_RE = re.compile(r"^\*\*([^*\n]+?)\*\*")
ITEM_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(\S.*)$")
FENCE_LINE_RE = re.compile(r"^\s*(?:`{3,}|~{3,})")
PID_RE = re.compile(r"p\d{2}#\d+")
KIND_ORDER = ("heading", "label", "row", "item")


def split_cells(line: str) -> list[str]:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" \t"))


class Doc:
    """Markdown の資料1つ。見出し・太字の見出し・表の行・箇条を Anchor にして持つ。"""

    def __init__(self, rel: str, text: str):
        self.rel = rel
        self.lines = text.replace("\r\n", "\n").split("\n")
        self.n = len(self.lines)
        self.headings: list[Anchor] = []
        self.tables: list[Table] = []
        self.anchors: list[Anchor] = []
        self._build()

    def _build(self) -> None:
        lines = self.lines
        mask = fenced_mask(lines, fence_spans(lines))
        for h in find_headings(lines, mask, 1):
            self.headings.append(Anchor("heading", h.line - 1, self.n, key=head_key(h.text), raw=plain(h.text), level=h.level))
        for i, a in enumerate(self.headings):                       # 見出しの節は、次の同じ深さ以上の見出しまで
            end = next((b.start for b in self.headings[i + 1:] if b.level <= a.level), self.n)
            a.end = self._trim(a.start, end)
        labels = [Anchor("label", i, self.n, key=head_key(m.group(1)), raw=plain(m.group(1)))
                  for i, ln in enumerate(lines) if not mask[i] and (m := LABEL_RE.match(ln))]
        hrs = {i for i, ln in enumerate(lines) if not mask[i] and HR_RE.match(ln)}
        bounds = sorted({h.start for h in self.headings} | {a.start for a in labels} | hrs)
        for a in labels:                                            # 太字の見出しは、次の太字の見出し・見出し・水平線まで
            a.end = self._trim(a.start, next((b for b in bounds if b > a.start), self.n))
        self.anchors = sorted(self.headings + labels + self._tables(mask) + self._items(mask),
                              key=lambda a: (a.start, KIND_ORDER.index(a.kind)))

    def _trim(self, start: int, end: int) -> int:
        while end > start + 1 and (not self.lines[end - 1].strip() or HR_RE.match(self.lines[end - 1])):
            end -= 1
        return end

    def _tables(self, mask: list[bool]) -> list[Anchor]:
        out: list[Anchor] = []
        lines = self.lines
        i = 0
        while i < self.n:
            if mask[i] or not lines[i].lstrip().startswith("|"):
                i += 1
                continue
            j = i
            while j < self.n and not mask[j] and lines[j].lstrip().startswith("|"):
                j += 1
            table = Table(i, j, None, None)
            body = i
            if j - i >= 2 and TABLE_SEP_RE.match(lines[i + 1]):
                table.header, table.sep, body = i, i + 1, i + 2
            for k in range(body, j):
                if TABLE_SEP_RE.match(lines[k]):
                    continue
                cells = split_cells(lines[k])
                first = plain(cells[0]) if cells else ""
                extra = tuple(x.casefold() for x in PID_RE.findall(cells[-1])) if len(cells) > 1 else ()
                out.append(Anchor("row", k, k + 1, key=head_key(first), extra=extra, raw=first, table=table))
            self.tables.append(table)
            i = j
        return out

    def _items(self, mask: list[bool]) -> list[Anchor]:
        out: list[Anchor] = []
        lines = self.lines
        for i, ln in enumerate(lines):
            if mask[i] or ln.lstrip().startswith("|"):
                continue
            m = ITEM_RE.match(ln)
            if not m:
                continue
            ind = len(m.group(1))
            marker, text = m.group(2), m.group(3)
            j = i + 1
            while j < self.n:
                nxt = lines[j]
                if not nxt.strip():
                    k = j + 1
                    while k < self.n and not lines[k].strip():
                        k += 1
                    if k < self.n and indent_of(lines[k]) > ind:
                        j = k + 1
                        continue
                    break
                if indent_of(nxt) > ind:
                    j += 1
                    continue
                break
            numbered = marker[0].isdigit()
            out.append(Anchor("item", i, self._trim(i, j), key=marker.rstrip(".)") if numbered else head_key(text),
                              extra=(head_key(text),) if numbered else (), raw=plain(text)[:160]))
        return out

    def breadcrumb(self, line: int, own: Anchor | None = None) -> str:
        """その行を囲む見出し（外側から3つまで）。own が見出しなら、その見出し自身は含めない。"""
        chain = [h for h in self.headings if h.level > 1 and h.start <= line < h.end and h is not own]
        return " > ".join(short(h.raw, 30) for h in chain[-3:])

    def numbered_line(self, i: int) -> Anchor:
        """コードの囲みの中の番号つきの行 i と、その続きの行（次の番号つきの行・空行・囲みの終わりまで）。"""
        j = i + 1
        while j < self.n and self.lines[j].strip() and not re.match(r"^\s*\d+[.)]\s", self.lines[j]) and not FENCE_LINE_RE.match(self.lines[j]):
            j += 1
        return Anchor("item", i, j, raw=plain(self.lines[i])[:80])

    def paragraph_at(self, i: int) -> Anchor:
        """i 行目を含む段落（表の行ならその行）。"""
        if self.lines[i].lstrip().startswith("|"):
            table = next((t for t in self.tables if t.start <= i < t.end), None)
            return Anchor("row", i, i + 1, raw=self.lines[i].strip()[:80], table=table)
        a = i
        while a > 0 and self.lines[a - 1].strip():
            a -= 1
        b = i + 1
        while b < self.n and self.lines[b].strip():
            b += 1
        return Anchor("item", a, b, raw=plain(self.lines[a])[:80])


# ---------------------------------------------------------------- 項目（materials の1行）を印に分ける


@dataclass
class Tok:
    """項目の中の1つの印。kind は sec・chap・part・setsu・bunya・kq・date・id・numid・letter・row・pid・word・ord。"""

    kind: str
    raw: str
    keys: tuple[str, ...] = ()
    text: str = ""                     # word：照合用の字
    hint: str = ""                     # word：直後の（…）の照合用の字（同じ語の見出しが複数あるときの絞り込み）
    nums: tuple[str, ...] = ()         # ord：番号つきの箇条の番号

    @property
    def inheritable(self) -> bool:
        """「Q4 T1・T2」の T2 のように、前の組の絞り込みを引き継げる印か。"""
        return self.kind in ("id", "numid", "letter", "row", "pid", "word", "ord")


@dataclass
class Group:
    prefix: list[Tok]                  # 絞り込みの印（外側から）
    leaf: Tok                          # 探す印
    shown: str                         # 見つからないときに見せる字


@dataclass
class SourceRef:
    kind: str                          # research・plan・path・pbare・unknown
    key: str                           # research：00 など。plan：requirements など。path：相対パス。pbare：11b など
    body: str
    notes: list[str]
    quotes: list[str]


def strip_comments(s: str) -> tuple[str, list[str]]:
    """（…）の注を取り除く（「…」の中は触らない）。注のあった所に \\x01n\\x01 を残す（直前の語の絞り込みに使う）。"""
    out: list[str] = []
    notes: list[str] = []
    buf: list[str] = []
    quote = depth = 0
    for ch in s:
        if depth:
            if ch == "（":
                depth += 1
            elif ch == "）":
                depth -= 1
                if depth == 0:
                    notes.append("".join(buf))
                    out.append(f"\x01{len(notes) - 1}\x01")
                    buf = []
                    continue
            buf.append(ch)
            continue
        if ch in "「『":
            quote += 1
        elif ch in "」』" and quote:
            quote -= 1
        if ch == "（" and not quote:
            depth = 1
            buf = []
            continue
        out.append(ch)
    if depth:
        notes.append("".join(buf))
        out.append(f"\x01{len(notes) - 1}\x01")
    return "".join(out), notes


def extract_quotes(s: str) -> tuple[str, list[str]]:
    """「…」を取り出し、 \\x02n\\x02 に置き換える（中の「」『』は外側の1つが閉じるまで含める）。"""
    out: list[str] = []
    quotes: list[str] = []
    buf: list[str] = []
    depth = 0
    for ch in s:
        if ch in "「『":
            if depth == 0 and ch == "「":
                depth = 1
                buf = []
                continue
            if depth:
                depth += 1
        elif ch in "」』" and depth:
            depth -= 1
            if depth == 0:
                quotes.append("".join(buf))
                out.append(f" \x02{len(quotes) - 1}\x02 ")
                continue
        (buf if depth else out).append(ch)
    if depth:
        out.append("「" + "".join(buf))
    return "".join(out), quotes


def split_sources(item: str) -> list[SourceRef]:
    """1項目を、資料ごとに分ける（ふつうは1つ）。頭が資料の名前でなければ unknown。"""
    flat, notes = strip_comments(squash(item))
    flat, quotes = extract_quotes(flat)
    cuts = [0] + [m.end() for m in SOURCE_BOUNDARY_RE.finditer(flat)] + [len(flat)]
    out: list[SourceRef] = []
    for a, b in zip(cuts, cuts[1:]):
        part = re.sub(r"^[、,，\s]+", "", flat[a:b])
        if m := RESEARCH_HEAD_RE.match(part):
            out.append(SourceRef("research", m.group(1), part[m.end():].strip(), notes, quotes))
        elif m := PBARE_HEAD_RE.match(part):
            out.append(SourceRef("pbare", P_FILES[m.group(1)], part, notes, quotes))
        elif m := PLAN_HEAD_RE.match(part):
            out.append(SourceRef("plan", m.group(1), part[m.end():].strip(), notes, quotes))
        elif (m := PATH_HEAD_RE.match(part)) and ".." not in m.group(1).split("/"):
            out.append(SourceRef("path", m.group(1), part[m.end():].strip(), notes, quotes))
        else:
            out.append(SourceRef("unknown", "", part, notes, quotes))
    return out


SEP_RE = re.compile(r"[・、,，;；]|と(?=\s*(?:§|第\d|#\d|p\d{2}#|\x02))|(?<=[\d\x01])と(?=[^\d\s])|(?<=\s)と(?=\s|[、,，]|$)")
KIND_RES = [
    ("pid", re.compile(r"^(p\d{2}#\d+)$")),
    ("sec", re.compile(r"^§\s*(\d+(?:[.\-]\d+)*)$")),
    ("bunya", re.compile(r"^(分野\s*\d+)$")),
    ("chap", re.compile(r"^(第\s*\d+\s*章)$")),
    ("part", re.compile(r"^(第\s*\d+\s*部)$")),
    ("setsu", re.compile(r"^(第\s*\d+\s*節)$")),
    ("kq", re.compile(r"^(KQ\s*\d+)$", re.I)),
    ("row", re.compile(r"^#\s*(\d+)$")),
    ("date", re.compile(r"^(\d{4}-\d{2}-\d{2})$")),
    ("id", re.compile(r"^([A-Za-z]{1,3}-?\d+(?:-[A-Za-z0-9]+)?)$")),
    ("numid", re.compile(r"^(\d+(?:-\d+)+)$")),
    ("letter", re.compile(r"^([A-Z])$")),
]
RANGE_KINDS = ("sec", "chap", "part", "setsu", "bunya", "row", "pid", "id")
RANGE_RE = re.compile(r"^(.+?)[〜～](.+)$")
TAIL_RE = re.compile(r"^(.*?)(\d+)(\D*)$")


def norm_key(kind: str, raw: str) -> str:
    s = nfkc(raw).strip()
    if kind in ("bunya", "chap", "part", "setsu", "kq"):
        return re.sub(r"\s+", "", s).casefold()
    return s.casefold()


def expand_range(a: str, b: str) -> list[str]:
    """"c-1" と "c-12"、"p12#71" と "p12#74"、"9.2" と "9.5"、"第3章" と "第5章" を、間を埋めた印の並びにする（できなければ空）。"""
    ma, mb = TAIL_RE.match(a), TAIL_RE.match(b)
    if not ma or not mb:
        return []
    if (ma.group(1), ma.group(3)) != (mb.group(1), mb.group(3)):
        return []
    lo, hi = int(ma.group(2)), int(mb.group(2))
    if hi < lo or hi - lo > MAX_RANGE:
        return []
    width = len(ma.group(2)) if ma.group(2).startswith("0") else 0
    return [f"{ma.group(1)}{str(i).zfill(width)}{ma.group(3)}" for i in range(lo, hi + 1)]


def classify(piece: str, hint: str = "") -> Tok:
    p = piece.strip()
    if re.fullmatch(r"\d+(?:と\d+)*", p):
        return Tok("ord", p, nums=tuple(re.findall(r"\d+", p)))
    if m := re.fullmatch(r"付録([A-Z]-?\d+)", p):                 # 付録A-6 は 10 の見出し A-6
        return Tok("id", p, keys=(norm_key("id", m.group(1)),))
    if m := RANGE_RE.match(p):
        left = classify(m.group(1))
        right = m.group(2).strip()
        if left.kind in RANGE_KINDS and left.keys:
            if bare := re.fullmatch(r"#?\s*(\d+)", right):         # #1〜8・p12#18〜#21：右は数だけ
                tail = TAIL_RE.match(left.keys[0])
                right_key = f"{tail.group(1)}{bare.group(1)}{tail.group(3)}" if tail else ""
            else:
                rt = classify(right)
                right_key = rt.keys[0] if rt.kind == left.kind and rt.keys else ""
            keys = expand_range(left.keys[0], right_key) if right_key else []
            if keys:
                return Tok(left.kind, p, keys=tuple(keys))
    for kind, rx in KIND_RES:
        if m := rx.match(p):
            return Tok(kind, p, keys=(norm_key(kind, m.group(1)),))
    return Tok("word", p, text=norm_text(p), hint=norm_text(hint))


DESCRIPTIVE_RE = re.compile(r"(?:注記つき|注記|訂正|注|本文|冒頭|末尾|段落|表|行|全体|その|最後|後|の|と|つき|含む|ほか|など)+")


def is_descriptive(raw: str) -> bool:
    """「注記」「本文」「表の最後の行」のように、印ではなく、手前の所のどこを指すかだけを言う語か。"""
    return bool(DESCRIPTIVE_RE.fullmatch(norm_text(raw)))


def as_row(t: Tok) -> Tok:
    return Tok("row", t.raw, keys=tuple(k.split("#", 1)[1] for k in t.keys)) if t.kind == "pid" else t


def piece_toks(piece: str, quotes: list[str], hint: str) -> list[Tok]:
    """空白で分けた1つの字を、印にする（引用・「…の4」・ふつうの印）。"""
    if q := re.fullmatch(r"\x02(\d+)\x02", piece):
        text = quotes[int(q.group(1))]
        return [Tok("word", text, text=norm_text(text), hint=norm_text(hint))]
    piece = re.sub(r"^の(?=\S)", "", piece)
    if m := re.match(r"^(\([A-Za-z0-9]\))(\d+)$", piece):                          # (b)2 は (b) の2番目
        return [classify(m.group(1), hint), classify(m.group(2))]
    if (m := re.match(r"^(.+?)の(\d+(?:と\d+)*)$", piece)) and not re.match(r"^[A-Za-z0-9]", piece):
        return [classify(m.group(1), hint), classify(m.group(2))]                 # 書き方の方針の4と5
    return [classify(piece, hint)]


def parse_body(body: str, notes: list[str], quotes: list[str], *, pids_as_rows: bool = False) -> list[Group]:
    """資料の名前の後の字を、印の組（Group）にする。「・」「、」で組を分け、空白で組の中の印を分ける。
    組が1つの印だけのときは、前の組の絞り込み（「Q4 T1・T2」の Q4）を引き継ぐ（見つからなければ全体を探す）。"""
    body = re.sub(r"^[\s　]*の(?=\S)", "", body)
    groups: list[list[Tok]] = []
    for chunk in SEP_RE.split(body):
        toks: list[Tok] = []
        for raw_piece in chunk.split():
            # 注の印（\x01n\x01）で語を分け、注は直前の語の手がかりにする（「方針（第三者…）4」の 4 は別の印）
            parts = re.split(r"\x01(\d+)\x01", raw_piece)
            for k, part in enumerate(parts):
                if k % 2:
                    if toks and toks[-1].kind == "word" and int(part) < len(notes):
                        toks[-1].hint = norm_text(notes[int(part)])
                    continue
                if part:
                    toks += piece_toks(part, quotes, "")
        if toks:
            groups.append(toks)
    out: list[Group] = []
    prefix: list[Tok] = []
    for toks in groups:
        leaf = toks[-1]
        if len(toks) > 1:
            prefix = toks[:-1]
            use = prefix
        else:
            use = prefix if leaf.inheritable else []
        if pids_as_rows:                                  # 11a〜11c の中や頭の p34#59 は、その論点の一覧の 59 行
            use = [as_row(t) for t in use]
            leaf = as_row(leaf)
        out.append(Group(list(use), leaf, " ".join(t.raw for t in toks)))
    kept = [g for g in out if not (g.leaf.kind == "word" and not g.prefix and is_descriptive(g.leaf.raw))]     # 「…と注記」の注記
    return kept or out


# ---------------------------------------------------------------- 印をたどる


def text_rank(req: str, norm: str) -> int | None:
    if not req or not norm:
        return None
    if norm == req:
        return 0
    if norm.startswith(req):
        return 1
    if len(req) >= 2 and req in norm:
        return 2
    return None


def inscope(a: Anchor, scope: list[tuple[int, int]]) -> bool:
    return any(s <= a.start < e for s, e in scope)


def locate(doc: Doc, scope: list[tuple[int, int]], tok: Tok, *, needle: bool = True) -> list[Anchor]:
    """scope の中で tok に当たる所（ふつうは1つ。日付の見出しや範囲は複数）。"""
    anchors = [a for a in doc.anchors if inscope(a, scope)]
    k = tok.kind
    out: list[Anchor] = []
    if k in ("sec", "chap", "part", "setsu", "bunya", "kq", "date"):
        for key in tok.keys:
            hits = [a for a in anchors if a.kind in HEAD_KINDS and a.has_key(key)]
            out += hits if k == "date" else hits[:1]
    elif k in ("id", "numid", "letter"):
        for key in tok.keys:
            picked: list[Anchor] = []
            for kind in KIND_ORDER:                       # 見出しと表の行の両方にある印（P9 など）は2つとも写す
                hit = next((a for a in anchors if a.kind == kind and a.has_key(key)), None)
                if hit is not None:
                    picked.append(hit)
            order = ("heading", "row", "label", "item")
            out += sorted(picked, key=lambda a: order.index(a.kind))[:2]
    elif k in ("row", "pid"):
        for key in tok.keys:
            hit = next((a for a in anchors if a.kind == "row" and a.has_key(key)), None)
            if hit is not None:
                out.append(hit)
    elif k == "ord":
        for n in tok.nums:
            hit = next((a for a in anchors if a.kind == "item" and a.has_key(n)), None)
            if hit is None:                              # 表の n 行目（見出し行は数えない）
                rows = [a for a in anchors if a.kind == "row"]
                first = rows[0].table if rows else None
                same = [a for a in rows if a.table is first]
                hit = same[int(n) - 1] if first is not None and 0 < int(n) <= len(same) else None
            if hit is None:                              # コードの囲みの中の番号つきの行
                rx = re.compile(r"^\s*" + re.escape(n) + r"[.)]\s")
                line = next((i for s, e in scope for i in range(s, min(e, doc.n)) if rx.match(doc.lines[i])), None)
                hit = doc.numbered_line(line) if line is not None else None
            if hit is not None:
                out.append(hit)
    else:
        out = locate_word(doc, scope, anchors, tok, needle)
    return out


def locate_word(doc: Doc, scope: list[tuple[int, int]], anchors: list[Anchor], tok: Tok, needle: bool = True) -> list[Anchor]:
    def search(req: str) -> Anchor | None:
        ranked = []
        for a in anchors:
            r = text_rank(req, a.norm)
            if r is not None:
                miss = 0 if (tok.hint and tok.hint in a.norm) else 1
                ranked.append((r, miss, KIND_ORDER.index(a.kind), a.start, a))
        if not ranked:
            return None
        ranked.sort(key=lambda x: x[:4])
        return ranked[0][4]

    hit = search(tok.text)
    if hit is None and "の" in tok.raw:                       # 五つ目の経路 → 五つ目、経路の三つ目 → 三つ目
        for part in (tok.raw.split("の", 1)[0], tok.raw.rsplit("の", 1)[1]):
            if hit is None and len(norm_text(part)) >= 2:
                hit = search(norm_text(part))
    if hit is None and len(tok.hint) >= 4:                    # 「対立点の表（長い作業の続け方）」：注が行の題そのもののとき
        hit = search(tok.hint)
    if hit is not None:
        return [hit]
    text = squash(tok.raw)                                     # 最後の手：その字を含む行のある段落（絞った所の中だけ）
    if needle and len(text) >= 3:
        for s, e in scope:
            for i in range(s, min(e, doc.n)):
                if text in doc.lines[i]:
                    return [doc.paragraph_at(i)]
    return []


def resolve_group(doc: Doc, group: Group) -> tuple[list[Anchor], str]:
    """(見つけた所, 手前の印の所で代えたときの、その印の字)。語の印が見つからないときだけ、手前で絞れた所（いちばん奥）を
    代わりに返す。「本文」「注記」のように手前の所のどこかを言うだけの語なら、代えたことは書かない（空の字を返す）。"""
    whole = [(0, doc.n)]
    scope = whole
    narrowed: tuple[Tok, list[Anchor]] | None = None
    for tok in group.prefix:
        cands = locate(doc, scope, tok)
        if cands:
            narrowed = (tok, cands[:MAX_SCOPES])
            inner = [(a.start + 1, a.end) for a in cands if a.end - a.start > 1]          # 中身のある所だけ、探す範囲を絞る
            if inner:
                scope = inner[:MAX_SCOPES]
    found = locate(doc, scope, group.leaf)
    if not found and scope is not whole and group.leaf.kind != "ord":      # 番号は手前の所の中でだけ数える
        found = locate(doc, whole, group.leaf, needle=False)
    if not found and group.leaf.kind == "word" and narrowed is not None:
        return narrowed[1][:1], ("" if is_descriptive(group.leaf.raw) else narrowed[0].raw)      # 「本文」「注記」などは手前の所のこと
    return found, ""


# ---------------------------------------------------------------- 写す所（Piece）と、切り方


@dataclass
class Block:
    text: str
    keep: bool = False             # 切るときも残す（表の見出し・見出し）
    mark: bool = False             # 印（【2026-11-03 訂正】【2026-11-03 注記】）がある
    row: bool = False              # 表の行
    core: bool = False             # 印で指された行と、それに添えた表の後の注記（印があれば MARK_CAP 字まで必ず残す）


@dataclass
class Piece:
    doc: Doc
    start: int
    end: int
    kind: str
    title: str
    blocks: list[Block]
    lines_desc: str
    crumb: str
    extra_note: str = ""
    terms: list[str] = field(default_factory=list)

    @property
    def full_len(self) -> int:
        return sum(len(b.text) + 1 for b in self.blocks)


def blocks_of(lines: list[str]) -> list[Block]:
    """行を、段落・表の行・箇条（続きの行を含む）・見出しの塊にする。"""
    blocks: list[Block] = []
    cur: list[str] = []

    def flush() -> None:
        if cur:
            text = "\n".join(cur)
            blocks.append(Block(text, mark=bool(MARK_RE.search(text))))
            cur.clear()

    for k, ln in enumerate(lines):
        if not ln.strip():
            flush()
        elif ln.lstrip().startswith("|"):
            flush()
            head = bool(TABLE_SEP_RE.match(ln)) or (k + 1 < len(lines) and bool(TABLE_SEP_RE.match(lines[k + 1])))
            blocks.append(Block(ln, keep=head, mark=bool(MARK_RE.search(ln)), row=not head))
        elif re.match(r"^#{1,6}\s", ln):
            flush()
            blocks.append(Block(ln, keep=True))
        else:
            m = ITEM_RE.match(ln)
            if m and len(m.group(1)) <= 1:
                flush()
            cur.append(ln)
    flush()
    return blocks


def shrink_row(line: str, n: int) -> str:
    """表の行を n 字以内に、どの列も残して縮める（印のある列は印から残す）。"""
    if len(line) <= n:
        return line
    cells = split_cells(line)
    if len(cells) < 2:
        return clip_text(line, n)
    budget = max(n - (3 * len(cells) + 1), len(cells) * 8)
    lo, hi = 8, max(len(c) for c in cells)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if sum(min(len(c), mid) for c in cells) <= budget:
            lo = mid
        else:
            hi = mid - 1
    return "| " + " | ".join(clip_text(c, lo) for c in cells) + " |"


def clip_blocks(blocks: list[Block], limit: int, terms: list[str] | None = None) -> tuple[str, bool]:
    """ブロックを limit 字ほどにする（本文, 切ったか）。
    - keep（表の見出し・見出し）と、印で指された行の印の付いたまとまり（core）は必ず残す（印のあるものは MARK_CAP 字まで）
    - 節の中にある印の付いた注記は、項目の注の語（terms）に当たるものを先に、直前の段落（注記が直すもの）を添えて残し、
      当たらないものは短く残す（合わせて limit の MARK_SHARE まで）
    - 残りは、terms を多く含むブロックを先に、次に頭から詰める"""
    if sum(len(b.text) + 1 for b in blocks) <= limit:
        return "\n".join(b.text for b in blocks), False
    norm = [nfkc(b.text).casefold() for b in blocks]

    def score(i: int) -> int:
        return sum(len(t) for t in (terms or []) if t in norm[i]) if 0 <= i < len(blocks) else 0

    def fit(b: Block, n: int) -> str:
        return shrink_row(b.text, n) if b.row else clip_text(b.text, n)

    chosen: dict[int, str] = {}
    used = 0
    for i, b in enumerate(blocks):
        if b.keep:
            chosen[i] = b.text
            used += len(b.text) + 1
        elif b.core and b.mark and b.row:                  # 印で指された行の中の印
            chosen[i] = fit(b, MARK_CAP)
            used += len(chosen[i]) + 1
    attached = 0
    for i, b in enumerate(blocks):                         # 表の後に添えた注記は、写した行を押しのけない範囲で
        if b.core and b.mark and not b.row:
            text = clip_text(b.text, MARK_CAP)
            if attached + len(text) + 1 <= int(limit * NOTES_SHARE) or not attached:
                chosen[i] = text
                attached += len(text) + 1
    used += attached
    marks = [i for i, b in enumerate(blocks) if b.mark and not b.keep and not b.core]
    prev = {i: i - 1 for i in marks if i > 0 and not (blocks[i - 1].keep or blocks[i - 1].mark or blocks[i - 1].row)}
    unit = {i: score(i) + (score(prev[i]) if i in prev else 0) for i in marks}
    share = max(int(limit * MARK_SHARE) - used, 0)
    spent = 0
    for i in sorted((i for i in marks if unit[i] > 0), key=lambda i: (-unit[i], i)):
        text = fit(blocks[i], MARK_CAP)
        pre = clip_text(blocks[prev[i]].text, PRE_CAP) if i in prev and score(prev[i]) > 0 else ""
        cost = len(text) + 1 + (len(pre) + 1 if pre else 0)
        if spent + cost <= share or not spent:
            chosen[i] = text
            if pre:
                chosen[prev[i]] = pre
            spent += cost
    lows = [i for i in marks if i not in chosen and unit[i] == 0]
    if lows:
        cap = max(SHORT_MARK[0], min(SHORT_MARK[1], (share - spent) // len(lows)))
        for i in lows:
            text = fit(blocks[i], cap)
            if spent + len(text) + 1 <= share or not spent:
                chosen[i] = text
                spent += len(text) + 1
    used += spent
    free = max(limit - used, 0)
    rest = [i for i, b in enumerate(blocks) if i not in chosen and not b.keep and not b.mark]
    first = [i for i in sorted(rest, key=lambda i: (-score(i), i)) if score(i) > 0]            # 手がかりの語を含むものを先に
    taken = 0
    for pass_ in (first, [i for i in rest if i not in first]):
        for i in pass_:
            b = blocks[i]
            if taken + len(b.text) + 1 <= free:
                chosen[i] = b.text
                taken += len(b.text) + 1
            elif free - taken >= 120:
                chosen[i] = fit(b, free - taken)
                taken = free
            if taken >= free:
                break
    for i, b in enumerate(blocks):                       # 行が1つも残らなかった表の見出しは残さない
        if b.keep and b.text.lstrip().startswith("|") and i in chosen:
            nxt = next((j for j in range(i + 1, len(blocks)) if not (blocks[j].keep and blocks[j].text.lstrip().startswith("|"))), None)
            if nxt is None or nxt not in chosen or not blocks[nxt].text.lstrip().startswith("|"):
                del chosen[i]
    out: list[str] = []
    skipped = False
    for i in range(len(blocks)):
        if i in chosen:
            if skipped:
                out.append("…（略）")
                skipped = False
            out.append(chosen[i])
        else:
            skipped = True
    if skipped:
        out.append("…（以降を略）")
    return "\n".join(out), True


def allocate(sizes: list[int], limit: int) -> list[int]:
    """1項目の上限を、写しの長さに応じて配る（短いものはそのまま、残りを長いものに等分）。"""
    out = [0] * len(sizes)
    remaining = limit
    left = len(sizes)
    for i in sorted(range(len(sizes)), key=lambda i: sizes[i]):
        out[i] = min(sizes[i], max(remaining // left, MIN_PIECE))
        remaining -= out[i]
        left -= 1
    return out


def fmt_lines(start: int, end: int) -> str:
    return f"{start + 1} 行" if end - start <= 1 else f"{start + 1}〜{end} 行"


def short(s: str, n: int) -> str:
    return s if len(s) <= n else s[:n - 1] + "…"


def pieces_for(doc: Doc, anchors: list[Anchor], terms: list[str], all_notes: bool = False) -> list[Piece]:
    """見つけた Anchor を、写す所にする（同じ表の行は1つにまとめ、表の見出しをつける）。all_notes は、項目の注が「注記つき」など
    注記を求めているとき（表の後の注記を、行に触れていなくても全部添える）。"""
    pieces: list[Piece] = []
    tables: dict[int, list[Anchor]] = {}
    order: list[tuple[str, object]] = []
    for a in anchors:
        if a.kind == "row" and a.table is not None:
            rows = tables.setdefault(a.table.start, [])
            if not rows:
                order.append(("table", a.table))
            rows.append(a)
        else:
            order.append(("anchor", a))
    for what, obj in order:
        if what == "anchor":
            a = obj
            pieces.append(Piece(doc, a.start, a.end, a.kind, short(a.raw, 60), blocks_of(doc.lines[a.start:a.end]),
                                fmt_lines(a.start, a.end), doc.breadcrumb(a.start, a if a.kind == "heading" else None),
                                terms=terms))
            continue
        table = obj
        rows = sorted(tables[table.start], key=lambda r: r.start)
        blocks: list[Block] = []
        if table.header is not None and table.sep is not None:
            blocks += [Block(doc.lines[table.header], keep=True), Block(doc.lines[table.sep], keep=True)]
        blocks += [Block(doc.lines[r.start], mark=bool(MARK_RE.search(doc.lines[r.start])), row=True, core=True) for r in rows]
        notes = notes_after(doc, table, rows, all_notes)
        blocks += [Block(t, mark=True, core=True) for t in notes]
        nums = "・".join(str(r.start + 1) for r in rows[:6]) + ("…" if len(rows) > 6 else "")
        desc = f"表の {nums} 行" if rows else "表"
        shown = "・".join(short(r.raw, 24) for r in rows[:4]) + ("…" if len(rows) > 4 else "")
        pieces.append(Piece(doc, rows[0].start, rows[-1].end, "row", shown, blocks, desc, doc.breadcrumb(rows[0].start),
                            "（表の後の注記を添えた）" if notes else "", terms))
    return pieces


def notes_after(doc: Doc, table: Table, rows: list[Anchor], everything: bool = False) -> list[str]:
    """表の直後の引用（> 【2026-11-03 注記】…）のうち、写した行の印に触れているもの。everything（項目の注が注記を求めている）の
    ときは、注記が少なくて（NOTES_FEW 以下）表全体への注記と読めるなら、触れていなくても全部。"""
    keys = [x for r in rows for x in (r.raw, r.key) if x]
    found: list[str] = []
    i = table.end
    while i < doc.n and not doc.lines[i].strip():
        i += 1
    while i < doc.n and doc.lines[i].lstrip().startswith(">"):
        j = i
        while j < doc.n and doc.lines[j].lstrip().startswith(">"):
            j += 1
        text = "\n".join(doc.lines[i:j])
        if MARK_RE.search(text):
            found.append(text)
        i = j
        while i < doc.n and not doc.lines[i].strip():
            i += 1
    if everything and len(found) <= NOTES_FEW:
        return found
    return [t for t in found if mentions(t, keys)]


def mentions(text: str, keys: list[str]) -> bool:
    for k in keys:
        k = k.strip()
        if not k:
            continue
        if k.isdigit():
            if re.search(r"#\s*" + re.escape(k) + r"(?!\d)", text):
                return True
        elif re.search(r"(?<![\w-])" + re.escape(k) + r"(?![\w-])", text, re.I):
            return True
    return False


# ---------------------------------------------------------------- 資料の置き場と、項目の解決


class Store:
    """資料のファイルを読んで持つ（根から相対）。"""

    def __init__(self, root: Path):
        self.root = Path(root)
        self._docs: dict[str, Doc | None] = {}

    def doc(self, rel: str) -> Doc | None:
        if rel not in self._docs:
            try:
                self._docs[rel] = Doc(rel, (self.root / rel).read_text(encoding="utf-8-sig"))
            except (OSError, UnicodeDecodeError):
                self._docs[rel] = None
        return self._docs[rel]

    def research(self, key: str) -> str | None:
        base = self.root / RESEARCH_DIR
        found = sorted(base.glob(f"{key}-*.md")) if base.is_dir() else []
        return f"{RESEARCH_DIR}/{found[0].name}" if found else None


@dataclass
class Item:
    index: int
    raw: str
    status: str = "ok"                 # ok・partial・missing・skip
    pieces: list[Piece] = field(default_factory=list)
    missing: list[str] = field(default_factory=list)
    reason: str = ""


def resolve_item(store: Store, index: int, raw: str) -> Item:
    item = Item(index, raw)
    reasons: list[str] = []
    attempted = 0
    for ref in split_sources(raw):
        if ref.kind == "unknown":
            reasons.append("調査資料でも計画の資料でもない")
            continue
        attempted += 1
        if ref.kind == "research" or ref.kind == "pbare":
            rel = store.research(ref.key)
            if rel is None:
                item.missing.append(f"{RESEARCH_DIR}/{ref.key}-*.md がない")
                reasons.append(f"{RESEARCH_DIR}/{ref.key}-*.md がない")
                continue
        else:
            rel = PLAN_DOCS[ref.key] if ref.kind == "plan" else ref.key
        doc = store.doc(rel)
        if doc is None:
            item.missing.append(f"{rel} がない")
            reasons.append(f"{rel} がない")
            continue
        groups = parse_body(ref.body, ref.notes, ref.quotes, pids_as_rows=ref.kind == "pbare" or ref.key in ("11a", "11b", "11c"))
        if not groups:
            item.missing.append(f"{ref.key} の中の印がない")
            reasons.append("資料の中の印がない")
            continue
        anchors: list[Anchor] = []
        for g in groups:
            found, fallback = resolve_group(doc, g)
            anchors += found
            if not found:
                item.missing.append(f"{g.shown} が見つからない")
            elif fallback:
                item.missing.append(f"{g.leaf.raw} が見つからないので、手前の「{fallback}」の所を写した")
        item.pieces += pieces_for(doc, dedupe_anchors(anchors), hint_terms(ref.notes),
                                  any("注記" in n or "訂正" in n for n in ref.notes))
    if attempted == 0:
        item.status, item.reason = "skip", (reasons[0] if reasons else "調査資料でも計画の資料でもない")
    elif item.missing and not item.pieces:
        item.status = "missing"
        item.reason = "；".join(reasons) if reasons else "資料の中に、その印の見出し・表の行・箇条がない"
    elif item.missing:
        item.status = "partial"
    return item


def dedupe_anchors(anchors: list[Anchor]) -> list[Anchor]:
    seen: set[tuple[str, int, int]] = set()
    out: list[Anchor] = []
    for a in anchors:
        if (a.kind, a.start, a.end) not in seen:
            seen.add((a.kind, a.start, a.end))
            out.append(a)
    return out


# ---------------------------------------------------------------- 第一波


def first_wave_ids(atlas) -> list[str]:
    """第一波のページの id（ナビゲーションの順）。site.yml の first_wave と front matter から、check_catalog.py と同じ閉包を出す：
    wave: 1 のページ（核）と、核の症状のページの routes の先（routes：none・first〔各 cause の to のうち最初の必須の先〕・all）と、
    named を種にして、prerequisites でたどって届くページをすべて入れる。"""
    site = atlas.site
    cfg = site.raw.get("first_wave")
    cfg = cfg if isinstance(cfg, dict) else {}
    mode = cfg.get("routes") if cfg.get("routes") in ("none", "first", "all") else "none"
    named = [x for x in (cfg.get("named") if isinstance(cfg.get("named"), list) else []) if isinstance(x, str)]
    top = site.priorities[0] if site.priorities else None
    by_id = atlas.by_id
    core = [p for p in by_id.values() if p.is_wave]
    seeds: list[str] = []
    for p in core:
        if p.type != "symptom":
            continue
        for route in p.routes:
            targets = list(dict.fromkeys(r.target for r in route.to if r.target))
            required = [t for t in targets if top is None or (t in by_id and by_id[t].priority == top)]
            seeds += targets if mode == "all" else required[:1] if mode == "first" else []
    seeds += [Ref.parse(x).target for x in named]
    seen = {p.id for p in core}
    queue = deque(core)
    for t in seeds:
        if t in by_id and t not in seen:
            seen.add(t)
            queue.append(by_id[t])
    while queue:
        for ref in queue.popleft().prerequisites:
            if ref.target in by_id and ref.target not in seen:
                seen.add(ref.target)
                queue.append(by_id[ref.target])
    return [p.id for p in atlas.ordered() if p.id in seen and by_id.get(p.id) is p]


# ---------------------------------------------------------------- 束を組む


@dataclass
class Packet:
    id: str
    text: str
    sections: dict[str, int]
    limit: int
    items: list[Item]
    truncated: int
    lowered_from: int | None = None
    over: bool = False

    @property
    def chars(self) -> int:
        return len(self.text)

    def count(self, status: str) -> int:
        return sum(1 for i in self.items if i.status == status)


def fence_for(text: str) -> str:
    runs = [len(m.group(0)) for m in re.finditer(r"`+", text)]
    return "`" * max(4, (max(runs) + 1) if runs else 4)


def yaml_of(item) -> str:
    data = to_jsonable(item.raw)
    for k in DROP_KEYS.get(item.section, ()):
        data.pop(k, None)
    return yaml.safe_dump([data], allow_unicode=True, sort_keys=False, width=10 ** 9).rstrip("\n")


class Builder:
    """束を組むのに要るもの（読む層・資料・出典の一覧）。"""

    def __init__(self, root: Path):
        self.root = Path(root)
        self.atlas = load_atlas(self.root)
        self.catalog = load_catalog(self.root, self.atlas.site)
        self.cat_by_id = self.catalog.by_id
        self.store = Store(self.root)
        self.wave_sources = self._load_wave_sources()
        self._items: dict[str, list[Item]] = {}

    def _load_wave_sources(self) -> dict[str, list[str]]:
        path = self.root / WAVE1_SOURCES
        if not path.is_file():
            return {}
        doc = read_yaml(path)
        pages = doc.data.get("pages") if isinstance(doc.data, dict) else None
        out: dict[str, list[str]] = {}
        for p in pages if isinstance(pages, list) else []:
            if isinstance(p, dict) and isinstance(p.get("id"), str):
                src = p.get("sources")
                out[p["id"]] = [s for s in src if isinstance(s, str)] if isinstance(src, list) else []
        return out

    # ---- 節

    def sec_page(self, page) -> list[str]:
        title = self.atlas.site.field_titles.get(page.field, "")
        out = [
            "## 1. ページ",
            "",
            f"- id：{page.id}",
            f"- 分野：{page.field}" + (f"（{title}）" if title else ""),
            f"- 型：{page.type or '（なし）'}",
            f"- level：{page.level or '（なし。この型は level を持たない）'}",
            f"- 優先度：{page.priority or '（なし）'}",
            f"- 題名：{page.title}",
            f"- 要約：{page.summary}",
            f"- volatility：{page.volatility or '（なし）'}",
            f"- stage：{page.stage or '（なし）'}　ファイル：{page.base}/{page.rel}",
        ]
        if page.text("nav_title"):
            out.append(f"- nav_title：{page.text('nav_title')}")
        if page.chapter:
            out.append(f"- 章（chapter）：{page.chapter}")
        out.append("- signs：" + ("" if page.signs else "（なし）"))
        out += [f"  - {t}：{x}" for t, x in page.signs]
        out.append("- sections：" + ("" if page.sections else "（なし）"))
        for s in page.sections:
            lv = f"（level：{s['level']}）" if s.get("level") else ""
            out.append(f"  - {s.get('title', '')} {{#{s.get('anchor', '')}}}{lv}")
        for label, value in (("別名（aliases）", page.aliases), ("面（surfaces）", page.surfaces),
                             ("原理（principle）", page.principle), ("Claude 側の原因（prevents）", page.prevents),
                             ("人の側の落とし穴（pitfalls）", page.pitfalls), ("場面（scenes）", page.scenes),
                             ("機能（tracks）", page.tracks), ("古くなった助言（outdated_advice）", page.outdated_advice),
                             ("sources（front matter）", page.sources)):
            if value:
                out.append(f"- {label}：{'・'.join(value)}")
        if page.is_wave:
            out.append("- wave：1（第一波の核）")
        return out

    def link_line(self, ref: Ref) -> str:
        target = self.atlas.resolve(ref)
        if target is None:
            return f"- {ref.raw}（ページがない）"
        head = f"- {ref.raw}（{target.field}／{target.type or '型なし'}）{target.title}"
        if ref.anchor is not None:
            sec = next((s for s in target.sections if s.get("anchor") == ref.anchor), None)
            head += f" ― 節「{sec.get('title', '')}」" if sec else f" ― 節 {ref.anchor} は sections にない"
        return f"{head}：{target.summary or '（要約なし）'}"

    def sec_links(self, page) -> list[str]:
        out = ["## 2. つながるページ", "", "### 前提（prerequisites）"]
        out += [self.link_line(r) for r in page.prerequisites] or ["- （なし）"]
        out += ["", "### 振り分け先（routes。cause ごと）"]
        if page.routes:
            for route in page.routes:
                out.append(f"- {route.cause or '（cause なし）'}")
                out += ["  " + self.link_line(r) for r in route.to]
        else:
            out.append("- （なし）")
        out += ["", "### 関連（related。近い順）"]
        out += [self.link_line(r) for r in page.related] or ["- （なし）"]
        out += self.anchor_lines(page)
        return out

    def anchor_lines(self, page) -> list[str]:
        """つながるページの sections の anchor（`<!-- link:begin id#anchor -->` で指せるもの）を、ページごとに1行で。"""
        refs = list(page.prerequisites) + [r for route in page.routes for r in route.to] + list(page.related)
        seen: set[str] = set()
        lines: list[str] = []
        for ref in refs:
            target = self.atlas.resolve(ref)
            if target is None or target.id in seen:
                continue
            seen.add(target.id)
            anchors = [s for s in target.sections if s.get("anchor")]
            if anchors:
                lines.append(f"- {target.id}：" + "・".join(f"{target.id}#{s['anchor']}（{s.get('title', '')}）" for s in anchors))
        if not lines:
            return []
        return ["", "### 指せる節（link の目印は `id#anchor`。つながるページの sections にあるものだけ指せる）"] + lines

    def sec_catalog(self, page, cat) -> list[str]:
        if cat is None:
            return ["## 3. 目次の情報", "", f"- 目次（planning/catalog/）に {page.id} の項目がない"]
        out = [f"## 3. 目次の情報（{cat.file}）", ""]
        if cat.level_evidence:
            out.append(f"- level の根拠（level_evidence）：{cat.level_evidence}")
        out.append("- 雛形（templates）：" + ("" if cat.templates else "（なし）"))
        for t in cat.templates:
            extra = "、".join(f"{k}：{v}" for k, v in t.items() if k != "name")
            out.append(f"  - {t.get('name', '')}" + (f"（{extra}）" if extra else ""))
        v = cat.visual
        out.append("- 図の案（visual）：" + (f"{v.get('kind', '')}：{v.get('text', '')}" if v else "（なし）"))
        notes = cat.notes
        if isinstance(notes, str) and notes.strip():
            out += ["- 備考（notes）："] + ["  " + ln for ln in notes.strip().split("\n")]
        elif isinstance(notes, list) and notes:
            out += ["- 備考（notes）："] + [f"  - {n}" for n in notes]
        else:
            out.append("- 備考（notes）：（なし）")
        out.append("- 材料（materials。写しは 6）：" + ("" if cat.materials else "（なし）"))
        out += [f"  {i}. {m}" for i, m in enumerate(cat.materials, 1)]
        return out

    def sec_data(self, page) -> list[str]:
        data = self.atlas.data
        names: dict[str, object] = {}

        def dump(item) -> list[str]:
            return ["", "```yaml", yaml_of(item), "```"]

        out = ["## 4. data", "", "### tracks の機能（data/facts.yml の features。match_terms は省いた）"]
        if page.tracks:
            for fid in page.tracks:
                item = data.features.get(fid)
                if item is None:
                    out.append(f"- {fid}：data/facts.yml の features にない")
                    continue
                out += dump(item)
                for n in data.entries("names"):
                    if n.raw.get("feature") == fid and n.id:
                        names.setdefault(n.id, n)
        else:
            out.append("- （tracks なし）")
        out += ["", "### outdated_advice の台帳の行（data/outdated-advice.yml）"]
        if page.outdated_advice:
            for aid in page.outdated_advice:
                item = data.advice.get(aid)
                if item is None:
                    out.append(f"- {aid}：data/outdated-advice.yml の advice にない")
                    continue
                out += dump(item)
                nm = item.raw.get("name")
                if isinstance(nm, str) and nm in data.names:
                    names.setdefault(nm, data.names[nm])
        else:
            out.append("- （outdated_advice なし）")
        out += ["", "### それに関わる names（data/facts.yml。tracks の機能の feature と、台帳の行の name）"]
        if names:
            for n in names.values():
                out += dump(n)
        else:
            out.append("- （なし）")
        if page.type == "ledger" and data.entries("advice"):
            out += ["", "### 台帳の全行の一覧（ledger 型のページに添える。data/outdated-advice.yml の advice。id｜状態｜変わった時期｜題名）"]
            out += [self.advice_line(a) for a in data.entries("advice")]
        return out

    def advice_line(self, a) -> str:
        """台帳の1行の見出し：id｜状態｜変わった時期（版）｜題名。時期は changed か、name の names の changed。"""
        changed = a.raw.get("changed")
        nm = a.raw.get("name")
        if not isinstance(changed, dict) and isinstance(nm, str) and nm in self.atlas.data.names:
            changed = self.atlas.data.names[nm].raw.get("changed")
        when = ""
        if isinstance(changed, dict):
            when = str(changed.get("date", "")) + (f"（{changed['version']}）" if changed.get("version") else "")
        return f"- {a.id}｜{a.text('status')}｜{when or '時期なし'}｜{a.text('title')}"

    def source_line(self, sid: str) -> str:
        data = self.atlas.data
        s = data.sources.get(sid)
        if s is None:
            return f"- {sid}｜（data/sources.yml にない）"
        url = s.text("url")
        entry = data.domain_entry(url) if url else None
        mark = "｜AI の利用を断るドメイン。開かない" if entry is not None and entry.raw.get("noai") is True else ""
        return f"- {sid}｜{s.text('kind')}｜{s.text('title')}｜{url}{mark}"

    def data_source_ids(self, page) -> list[str]:
        data = self.atlas.data
        ids: list[str] = []
        for fid in page.tracks:
            if (f := data.features.get(fid)) is not None:
                ids += f.strings("sources")
        for aid in page.outdated_advice:
            if (f := data.advice.get(aid)) is not None:
                ids += f.strings("sources")
                nm = f.raw.get("name")
                if isinstance(nm, str) and nm in data.names:
                    ids += data.names[nm].strings("sources")
        ids += [s for n in data.entries("names") if n.raw.get("feature") in page.tracks for s in n.strings("sources")]
        return list(dict.fromkeys(ids))

    def sec_sources(self, page) -> list[str]:
        out = ["## 5. 出典の一覧", ""]
        listed = self.wave_sources.get(page.id)
        shown: set[str] = set()
        if listed is None:
            out.append(f"一覧なし（{WAVE1_SOURCES} にこのページがない）")
        else:
            out.append(f"{WAVE1_SOURCES} のこのページの sources（{len(listed)} 件。id｜種類｜題名｜URL。"
                       "materials がたどる節にある出典で、本文に全部を使うという意味ではない）")
            out += ["", *[self.source_line(s) for s in listed]] if listed else ["", "- （空）"]
            shown = set(listed)
        if page.sources:
            out += ["", "front matter の sources（このページが挙げている出典）", *[self.source_line(s) for s in page.sources]]
            shown |= set(page.sources)
        extra = [s for s in self.data_source_ids(page) if s not in shown]
        if extra:
            out += ["", "data の項目（4）が挙げている出典（上の一覧にないもの）", *[self.source_line(s) for s in extra]]
        return out

    def items_of(self, pid: str, cat) -> list[Item]:
        if pid not in self._items:
            self._items[pid] = [resolve_item(self.store, i, m) for i, m in enumerate(cat.materials if cat else [], 1)]
        return self._items[pid]

    def sec_materials(self, items: list[Item], limit: int) -> tuple[list[str], int]:
        out = ["## 6. 材料の抜き出し", ""]
        if not items:
            return out + ["目次の materials がない（写す材料なし）"], 0
        out += [f"目次の materials を planning/research/ などの節・表の行・箇条にたどった写し（1項目あたり最大 {limit} 字。"
                "超えるときは「…（略）」で切り、出典の行の範囲に全文がある。【2026-11-03 訂正】【2026-11-03 注記】は印ごと写す。"
                "写しはバッククォート4つ以上の囲みに入れ、中の見出しは調査資料のもので、この束の節ではない）", ""]
        seen: list[tuple[str, int, int, str]] = []
        truncated = 0
        for it in items:
            out += [f"### 6.{it.index} {it.raw}", ""]
            if it.status == "skip":
                out += [f"対象外：{it.raw}（{it.reason}。束に写さない）", ""]
                continue
            fresh: list[Piece] = []
            for p in it.pieces:
                dup = next((s for s in seen if s[0] == p.doc.rel and s[1] <= p.start and p.end <= s[2]), None)
                if dup is None:
                    fresh.append(p)
                else:
                    out += [f"出典：{p.doc.rel} の {p.lines_desc}（{p.title}）", f"（{dup[3]} に写したのと同じ所）", ""]
            for p, cap in zip(fresh, allocate([p.full_len for p in fresh], limit)):
                text, cut = clip_blocks(p.blocks, cap, p.terms)
                crumb = f"｜{p.crumb}" if p.crumb else ""
                out.append(f"出典：{p.doc.rel} の {p.lines_desc}（{p.title}）{crumb}{p.extra_note}")
                if cut:
                    truncated += 1
                    out.append(f"※ 全 {p.full_len} 字のうち {len(text)} 字を写した（上限 {cap} 字。切った所は「…（略）」）")
                else:
                    out.append(f"※ 全文（{p.full_len} 字）")
                fence = fence_for(text)
                out += [fence, text, fence, ""]
                if not cut:
                    seen.append((p.doc.rel, p.start, p.end, f"6.{it.index}"))
            if it.status in ("missing", "partial"):
                what = it.reason if it.status == "missing" else "、".join(it.missing)
                out += [f"見つからない：{it.raw}（{what}）", ""]
        return out, truncated

    def sec_guides(self, page) -> list[str]:
        out = ["## 7. 書き方", "", f"- 執筆カード：{GUIDES_DIR}/card.md（書く規則の要点はこれで足りる。全部読む）",
               f"- 共通の手引き：{GUIDES_DIR}/common.md（迷ったときだけ、カードの（common §N）の節を引く。全部は読まない）"]
        if page.type:
            guide = f"{GUIDES_DIR}/{page.type}.md"
            out.append(f"- 型の手引き：{guide}" + ("（迷ったときだけ引く）" if (self.root / guide).is_file() else "（まだない）"))
        else:
            out.append("- 型の手引き：（型が未設定）")
        out.append("- 報告の置き場所：指示に従う（担当への指示に書いてある）")
        return out

    # ---- 束

    def packet(self, pid: str, item_limit: int, packet_limit: int) -> Packet | None:
        page = self.atlas.by_id.get(pid)
        if page is None:
            return None
        cat = self.cat_by_id.get(pid)
        items = self.items_of(pid, cat)
        limit = item_limit
        while True:
            pk = self.render(page, cat, items, limit)
            pk.over = pk.chars > packet_limit
            if pk.over and limit > MIN_ITEM_LIMIT:
                limit = max(MIN_ITEM_LIMIT, int(limit * LIMIT_STEP))
                continue
            pk.lowered_from = item_limit if limit != item_limit else None
            return pk

    def render(self, page, cat, items: list[Item], limit: int) -> Packet:
        mats, truncated = self.sec_materials(items, limit)
        sections = {
            "1 ページ": self.sec_page(page), "2 つながるページ": self.sec_links(page), "3 目次の情報": self.sec_catalog(page, cat),
            "4 data": self.sec_data(page), "5 出典の一覧": self.sec_sources(page), "6 材料の抜き出し": mats,
            "7 書き方": self.sec_guides(page),
        }
        head = "\n".join([
            f"# 材料の束：{page.id}（{page.title}）",
            "",
            "**読むのはこの束と planning/guides/card.md だけ**。ほかのファイルを探して小分けに読まない（呼び出しの数がそのまま使用量になる）。",
            "",
            "道具 tools/make_packet.py が作った（手で直さない。作り直すと上書きされる）。束にないことが要るときだけ、ほかの資料を開く"
            "（decisions 2026-11-04「執筆の担当が開く一次資料」、2026-11-05「使用量を抑える運用」）。",
            "",
            f"- 構成：1 ページ／2 つながるページ／3 目次の情報／4 data／5 出典の一覧／6 材料の抜き出し（1項目 {limit} 字まで）／7 書き方",
        ])
        parts, sizes = [head], {}
        for name, lines in sections.items():
            text = "\n".join(lines).rstrip("\n")
            sizes[name] = len(text)
            parts.append(text)
        return Packet(page.id, "\n\n".join(parts) + "\n", sizes, limit, items, truncated)


# ---------------------------------------------------------------- CLI


def write_if_changed(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")


def format_stats(packets: list[Packet], packet_limit: int) -> list[str]:
    lines = ["束の大きさ（文字数）。内訳は 1 ページ／2 つながるページ／3 目次／4 data／5 出典／6 材料／7 書き方"]
    for pk in packets:
        parts = "／".join(str(n) for n in pk.sections.values())
        mats = (f"材料 {len(pk.items)} 項目（見つかった {pk.count('ok')}・一部 {pk.count('partial')}・見つからない {pk.count('missing')}"
                f"・対象外 {pk.count('skip')}・切った写し {pk.truncated}）")
        low = f"。上限を {pk.lowered_from} 字から {pk.limit} 字に下げた" if pk.lowered_from else ""
        over = f"。{packet_limit} 字を超えている" if pk.over else ""
        lines.append(f"  {pk.id}: {pk.chars} 字（{parts}）｜{mats}｜1項目 {pk.limit} 字{low}{over}")
    if packets:
        sizes = [pk.chars for pk in packets]
        lines.append(f"  計 {len(packets)} 束：最小 {min(sizes)}・最大 {max(sizes)}・合計 {sum(sizes)} 字"
                     f"｜見つからない {sum(pk.count('missing') for pk in packets)}・一部 {sum(pk.count('partial') for pk in packets)}"
                     f"・対象外 {sum(pk.count('skip') for pk in packets)}")
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("ids", nargs="*", metavar="ID", help="束を作るページの id")
    parser.add_argument("--wave1", action="store_true", help="第一波の全ページ")
    parser.add_argument("--all", action="store_true", help="全ページ")
    parser.add_argument("--out", metavar="DIR", help=f"束を書く先（既定は根の {DEFAULT_OUT}）")
    parser.add_argument("--root", type=Path, default=ROOT, help="根（既定はこのリポジトリ。試験用）")
    parser.add_argument("--stats", action="store_true", help="束の大きさ（文字数）を出す")
    parser.add_argument("--item-limit", type=int, default=ITEM_LIMIT, metavar="N",
                        help=f"材料の抜き出し1項目の上限（字。既定 {ITEM_LIMIT}）")
    parser.add_argument("--packet-limit", type=int, default=PACKET_LIMIT, metavar="N",
                        help=f"1つの束の大きさの目安（字。既定 {PACKET_LIMIT}）。超えるときは 1項目の上限を下げる")
    args = parser.parse_args(argv)
    if not (args.ids or args.wave1 or args.all):
        parser.error("ページの id か --wave1 か --all を指定する")
    root = args.root.resolve()
    try:
        builder = Builder(root)
    except Fatal as e:
        print(f"読めない: {e}", file=sys.stderr)
        return 2
    out_dir = Path(args.out) if args.out else root / DEFAULT_OUT
    ids = list(args.ids)
    if args.wave1:
        ids += first_wave_ids(builder.atlas)
    if args.all:
        ids += [p.id for p in builder.atlas.ordered() if builder.atlas.by_id.get(p.id) is p]
    packets: list[Packet] = []
    missing: list[str] = []
    for pid in dict.fromkeys(ids):
        pk = builder.packet(pid, max(args.item_limit, 1), max(args.packet_limit, 1))
        if pk is None:
            missing.append(pid)
            print(f"ページがない: {pid}（stubs/ にも docs/ にもない）", file=sys.stderr)
            continue
        try:
            write_if_changed(out_dir / f"{pid}.md", pk.text)
        except OSError as e:
            print(f"書けない: {out_dir / (pid + '.md')}（{e}）", file=sys.stderr)
            return 2
        packets.append(pk)
    try:
        shown = out_dir.resolve().relative_to(root)
    except ValueError:
        shown = out_dir
    print(f"束を作った: {len(packets)} 件（{shown}）")
    if args.stats:
        for line in format_stats(packets, args.packet_limit):
            print(line)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
