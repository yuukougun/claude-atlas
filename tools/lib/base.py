"""読む層の共通の部品：指摘（Problem）・値の読み方・参照（Ref）・YAML の1項目（Record）・ページの読み方（PageRecord）。

PageRecord は、front matter のページ（pages.Page）と目次のページ（catalog.CatalogPage）に共通の読み方である。
作る層と検査の層がこの読み方だけで規則を書けば、目次と front matter の両方のモデルに同じ規則を当てられる
（設計書 §8.3「前提と関連の規則は、catalog と front matter の両方のモデルに当てる」）。

読む層は値を直さず、止まらずに読む。値の形が台帳と違っても（リストのところが数など）空として読み、形の誤りは
schema の検査（tools/lib/schema.py と schema/*.schema.json）が出す。tools/check_catalog.py の読む層の部品
（as_text・as_strings・as_maps・Ref・Page の読み方）を写して、front matter にも使える形にしたもの。
"""
from __future__ import annotations

import datetime
import re
from dataclasses import dataclass

ID_PATTERN = r"^[a-z0-9]+(-[a-z0-9]+)*$"          # ページ・節の anchor・data の項目の id（catalog/README §2）
REF_PATTERN = r"^[a-z0-9]+(-[a-z0-9]+)*(#[a-z0-9]+(-[a-z0-9]+)*)?$"   # id か id#anchor
ID_RE = re.compile(ID_PATTERN)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PARTIAL_DATE_RE = re.compile(r"^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$")


class Fatal(Exception):
    """読めない（schema/site.yml がない・壊れている、など）。道具は終了コード 2 で止まる。"""


@dataclass(frozen=True)
class Problem:
    """読む層が見つけた指摘（YAML の誤り・front matter が閉じていない・目印の対が合わない、など）。
    重さと検査の名前は検査の層が決める。kind はその手がかり（YAML・形・front matter・目印・置き場所・設定）。"""

    file: str                 # 根からの相対パス（表示用）
    line: int | None          # ファイルの行（1 から）
    message: str
    kind: str
    id: str = "-"             # 関わるページや項目の id（なければ「-」）

    def format(self) -> str:
        loc = f"{self.file}:{self.line}" if self.line else self.file
        return f"{loc}: {self.id}: [{self.kind}] {self.message}"


# ---------------------------------------------------------------- 値の読み方


def as_text(v) -> str:
    """文字列として読む（前後の空白を除く。文字列でなければ空）。"""
    return v.strip() if isinstance(v, str) else ""


def as_strings(v) -> list[str]:
    """文字列のリストとして読む（1つの文字列は1要素のリスト。文字列でない要素は飛ばす）。"""
    if isinstance(v, str):
        return [v]
    if isinstance(v, list):
        return [x for x in v if isinstance(x, str)]
    return []


def as_maps(v) -> list[dict]:
    """マッピングのリストとして読む（1つのマッピングは1要素のリスト）。"""
    if isinstance(v, dict):
        return [v]
    if isinstance(v, list):
        return [x for x in v if isinstance(x, dict)]
    return []


def as_list(v) -> list:
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def parse_date(v) -> datetime.date | None:
    """日付（2026-11-04 の文字列か date）を date にする。日付として正しくなければ None。"""
    if isinstance(v, datetime.datetime):
        return v.date()
    if isinstance(v, datetime.date):
        return v
    if isinstance(v, str) and DATE_RE.match(v.strip()):
        try:
            return datetime.date.fromisoformat(v.strip())
        except ValueError:
            return None
    return None


def partial_date_key(v) -> tuple[int, ...] | None:
    """「2026」「2026-10」「2026-10-27」（変わった時期など。年だけの整数も）を並べられる組にする。正しくなければ None。"""
    if isinstance(v, datetime.date):
        return (v.year, v.month, v.day)
    if isinstance(v, int) and not isinstance(v, bool):        # 年だけ（YAML の 2026 は整数）
        return (v,) if 1000 <= v <= 9999 else None
    m = PARTIAL_DATE_RE.match(v.strip()) if isinstance(v, str) else None
    if not m:
        return None
    parts = tuple(int(x) for x in m.groups() if x is not None)
    try:
        datetime.date(parts[0], parts[1] if len(parts) > 1 else 1, parts[2] if len(parts) > 2 else 1)
    except ValueError:
        return None
    return parts


# ---------------------------------------------------------------- 参照

FIELD_PREFIX = "field:"      # link の目印で分野の入口を指す形（field:<分野の id>）。ページの id は英小文字・数字・ハイフンなので重ならない


@dataclass(frozen=True)
class Ref:
    """prerequisites・related・routes の to・本文の link の目印の1件（id か id#anchor）。"""

    raw: str
    target: str
    anchor: str | None

    @classmethod
    def parse(cls, raw: str) -> Ref:
        target, sharp, anchor = raw.strip().partition("#")
        return cls(raw, target.strip(), anchor.strip() if sharp else None)


@dataclass(frozen=True)
class Route:
    """症状のページの routes の1件（原因と、その振り分け先）。"""

    cause: str
    to: tuple[Ref, ...]
    index: int                # routes の中の位置（0 から）
    raw: dict


# ---------------------------------------------------------------- YAML の1項目


class Record:
    """YAML の1項目（ページの front matter・目次のページ・data の項目）。raw は YAML のまま（yamlio.LineDict）。"""

    def __init__(self, raw: dict, file: str, key: str = "id"):
        self.raw = raw
        self.file = file           # 根からの相対パス（表示用）
        self._key = key            # 項目の名前のキー（ふつうは id。data の domains は domain）

    def __repr__(self) -> str:
        return f"<{type(self).__name__} {self.id or '?'} {self.file}>"

    @property
    def line(self) -> int | None:
        return getattr(self.raw, "line", None)

    def key_line(self, key: str) -> int | None:
        """そのキーの行（なければ項目の始まりの行）。"""
        lines = getattr(self.raw, "key_lines", None) or {}
        return lines.get(str(key), self.line)

    @property
    def id(self) -> str | None:
        v = self.raw.get(self._key)
        return v if isinstance(v, str) and v.strip() else None

    @property
    def label(self) -> str:
        return self.id or "(id なし)"

    def get(self, key: str, default=None):
        return self.raw.get(key, default)

    def has(self, key: str) -> bool:
        """キーがあり、値が null でない。"""
        return self.raw.get(key) is not None

    def text(self, key: str) -> str:
        return as_text(self.raw.get(key))

    def strings(self, key: str) -> list[str]:
        return as_strings(self.raw.get(key))

    def parts(self, key: str) -> list[dict]:
        return as_maps(self.raw.get(key))

    def refs(self, key: str) -> list[Ref]:
        return [Ref.parse(s) for s in self.strings(key)]

    def date(self, key: str) -> datetime.date | None:
        return parse_date(self.raw.get(key))


class PageRecord(Record):
    """ページの読み方（front matter と目次に共通）。field は、front matter のページならフォルダの分野、目次の
    ページならファイルの分野（どちらも、ページが実際に置かれた分野）。"""

    kind = "page"                 # 子が「front matter」「catalog」にする
    field: str = ""

    # 1つの値
    @property
    def title(self) -> str:
        return self.text("title")

    @property
    def nav_label(self) -> str:
        """ナビゲーションの名前（nav_title がなければ title）。"""
        return self.text("nav_title") or self.title

    @property
    def type(self) -> str:
        return self.text("type")

    @property
    def level(self) -> str:
        return self.text("level")

    @property
    def priority(self) -> str:
        return self.text("priority")

    @property
    def chapter(self) -> str:
        return self.text("chapter")

    @property
    def summary(self) -> str:
        return self.text("summary")

    @property
    def volatility(self) -> str:
        return self.text("volatility")

    @property
    def stage(self) -> str:
        return self.text("stage")

    @property
    def is_wave(self) -> bool:
        """第一波の核か（wave: 1。true は 1 と数えない）。"""
        w = self.raw.get("wave")
        return w == 1 and not isinstance(w, bool)

    # リスト
    @property
    def aliases(self) -> list[str]:
        return self.strings("aliases")

    @property
    def prerequisites(self) -> list[Ref]:
        return self.refs("prerequisites")

    @property
    def related(self) -> list[Ref]:
        return self.refs("related")

    @property
    def routes(self) -> list[Route]:
        out = []
        for i, r in enumerate(self.parts("routes")):
            out.append(Route(as_text(r.get("cause")), tuple(Ref.parse(s) for s in as_strings(r.get("to"))), i, r))
        return out

    def route_targets(self) -> list[Ref]:
        """routes の to を、すべての原因について順に並べたもの。"""
        return [ref for r in self.routes for ref in r.to]

    @property
    def sections(self) -> list[dict]:
        return self.parts("sections")

    def anchors(self) -> list[str]:
        return [a for a in (as_text(s.get("anchor")) for s in self.sections) if a]

    @property
    def signs(self) -> list[tuple[str, str]]:
        """(type, text) の組（どちらかが文字列でない要素は飛ばす）。"""
        return [(as_text(s.get("type")), as_text(s.get("text"))) for s in self.parts("signs")
                if isinstance(s.get("type"), str) and isinstance(s.get("text"), str)]

    @property
    def sign_items(self) -> list[tuple[str, str, str]]:
        """(type, text, anchor) の組（anchor は任意で、なければ空。type・text が文字列でない要素は飛ばす）。"""
        return [(as_text(s.get("type")), as_text(s.get("text")), as_text(s.get("anchor")))
                for s in self.parts("signs") if isinstance(s.get("type"), str) and isinstance(s.get("text"), str)]

    @property
    def surfaces(self) -> list[str]:
        return self.strings("surfaces")

    @property
    def principle(self) -> list[str]:
        return self.strings("principle")

    @property
    def prevents(self) -> list[str]:
        return self.strings("prevents")

    @property
    def pitfalls(self) -> list[str]:
        return self.strings("pitfalls")

    @property
    def scenes(self) -> list[str]:
        return self.strings("scenes")

    @property
    def tracks(self) -> list[str]:
        return self.strings("tracks")

    @property
    def outdated_advice(self) -> list[str]:
        return self.strings("outdated_advice")

    @property
    def sources(self) -> list[str]:
        return self.strings("sources")
