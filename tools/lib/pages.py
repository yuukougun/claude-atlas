"""ページ（front matter と本文）を、docs/ と stubs/ から読む。

置き場所（設計書 §8.2。stub の置き場所は 2026-11-04 のメインの決定：骨格のページは docs/ の外の stubs/ に置き、
draft にするときに docs/ へ移す。MkDocs のビルドに入るのは docs/ だけ）:
  docs/<field>/<id>.md     ページ（Page）。field は site.yml の fields の id。公開するページ
  stubs/<field>/<id>.md    骨格のページ（Page。base が stubs）。公開しない
  docs/<field>/index.md    分野の入口（生成物。読まない）
  docs/lists/              生成した一覧（読まない）
  docs/index.md            サイトのトップ（手書き。型を持たない。others に入れる）
  それ以外の Markdown       others に入れ、「置き場所」の Problem にする（stubs/ には <field>/<id>.md のほかを置かない）
同じ id のページが docs/ と stubs/ の両方（や二つの分野）にあれば、Docs.duplicate_ids と Atlas.duplicates に出る
（読む層は両方を残す。誤りとして出すのは検査の層。by_id は先に読んだ docs/ のほうを引く）。
stage と置き場所の食い違い（stubs/ に draft 以上、docs/ に stub）も、検査の層が見る。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from .base import PageRecord, Problem, Record, Ref
from .markdown import Heading, Marker, fence_spans, fenced_mask, find_headings, find_markers, split_front_matter
from .site import Site
from .yamlio import LineDict, parse_yaml

DOCS_DIR = "docs"
STUBS_DIR = "stubs"            # 骨格のページ（公開しない。draft にするときに docs/ へ移す）
PAGE_DIRS = (DOCS_DIR, STUBS_DIR)   # ページを読む置き場所（この順に読む）
LISTS_DIR = "lists"            # docs/lists/：生成した一覧
INDEX_NAME = "index.md"        # docs/<field>/index.md は分野の入口（生成）、docs/index.md はサイトのトップ（手書き）


@dataclass
class Markdown:
    """Markdown のファイル1つを読んだもの。"""

    shown: str                         # 根からの相対パス（表示用。docs/symptoms/x.md）
    text: str
    meta: LineDict | None              # front matter（マッピングとして読めたときだけ）
    has_front_matter: bool
    body: str
    body_line: int                     # 本文の1行目のファイルの行
    lines: list[str]                   # 本文の行
    fenced: list[bool]                 # 行ごとに、フェンスのコードの中か
    markers: list[Marker]
    headings: list[Heading]
    problems: list[Problem]


def read_markdown(path: Path, shown: str, page: str = "-") -> Markdown:
    """Markdown を読み、front matter・本文・フェンス・見出し・目印に分ける。読めない所は Problem にする。"""
    problems: list[Problem] = []
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except (OSError, UnicodeDecodeError) as e:
        text = ""
        problems.append(Problem(shown, None, f"ファイルが読めない（{e}）", "front matter", page))
    fm, body, body_line, err = split_front_matter(text)
    meta = None
    if err:
        problems.append(Problem(shown, 1, err, "front matter", page))
    elif fm is not None:
        doc = parse_yaml(fm, line_offset=1)
        problems += doc.problems(shown, page)
        if doc.error is None:
            if isinstance(doc.data, dict):
                meta = doc.data
            else:
                what = "空" if doc.data is None else "マッピングでない"
                problems.append(Problem(shown, 1, f"front matter が{what}", "front matter", page))
    lines = body.split("\n")
    fenced = fenced_mask(lines, fence_spans(lines))
    markers, mproblems = find_markers(body, lines, fenced, body_line, shown, page)
    return Markdown(shown, text, meta, fm is not None, body, body_line, lines, fenced, markers,
                    find_headings(lines, fenced, body_line), problems + mproblems)


class Page(PageRecord):
    """docs/<field>/<id>.md か stubs/<field>/<id>.md のページ（front matter のモデル）。raw は front matter（読めなければ空）。"""

    kind = "front matter"

    def __init__(self, md: Markdown, field: str, stem: str, rel: str, base: str = DOCS_DIR):
        super().__init__(md.meta if md.meta is not None else LineDict(), md.shown)
        self.md = md
        self.field = field             # フォルダの分野（front matter の field は meta_field）
        self.stem = stem               # ファイル名（.md を除く）
        self.rel = rel                 # 置き場所の中の相対パス（<field>/<id>.md）
        self.base = base               # 置き場所（docs か stubs）

    @property
    def declared_id(self) -> str | None:
        """front matter に書いた id（なければ None）。"""
        return Record.id.fget(self)

    @property
    def id(self) -> str:
        """front matter の id（なければファイル名）。ファイル名との一致は検査の層が見る。"""
        return self.declared_id or self.stem

    @property
    def label(self) -> str:
        return self.id

    @property
    def meta_field(self) -> str:
        return self.text("field")

    @property
    def in_docs(self) -> bool:
        """docs/ にある（MkDocs のビルドに入る）。stubs/ の骨格のページは False。"""
        return self.base == DOCS_DIR

    @property
    def url(self) -> str:
        """サイトの根からの URL（use_directory_urls。<field>/<id>/。stubs/ のページは docs/ へ移したときの URL）。"""
        return f"{self.field}/{self.stem}/"

    @property
    def body(self) -> str:
        return self.md.body

    @property
    def body_line(self) -> int:
        return self.md.body_line

    @property
    def lines(self) -> list[str]:
        return self.md.lines

    @property
    def markers(self) -> list[Marker]:
        return self.md.markers

    @property
    def headings(self) -> list[Heading]:
        return self.md.headings

    @property
    def problems(self) -> list[Problem]:
        return self.md.problems

    def markers_of(self, kind: str) -> list[Marker]:
        return [m for m in self.markers if m.kind == kind]

    def fact_ids(self) -> list[str]:
        """本文の fact の目印が指す数値の id（重ねない。出てくる順）。"""
        return list(dict.fromkeys(m.arg.split()[0] for m in self.markers_of("fact") if m.arg))

    def link_refs(self) -> list[Ref]:
        """本文の link の目印が指すページ（id か id#anchor）。"""
        return [Ref.parse(m.arg) for m in self.markers_of("link") if m.arg]

    def gen_names(self) -> list[str]:
        return [m.arg for m in self.markers_of("gen") if m.arg]

    def heading_anchors(self) -> list[str]:
        """本文の見出しに {#anchor} で書いた anchor（sections の anchor が本文にあるかを見るため）。"""
        return [h.anchor for h in self.headings if h.anchor]


@dataclass
class Docs:
    """docs/ と stubs/ を読んだもの。"""

    root: Path
    pages: list[Page] = field(default_factory=list)          # <field>/<id>.md（置き場所の順、その中はパスの順）
    others: list[Markdown] = field(default_factory=list)     # docs/index.md と、置き場所の違う Markdown
    generated: list[str] = field(default_factory=list)       # 読まなかった生成物（docs/<field>/index.md・docs/lists/）
    problems: list[Problem] = field(default_factory=list)    # 置き場所など（ページの中の指摘は Page.problems）

    def all_problems(self) -> list[Problem]:
        return self.problems + [x for p in self.pages for x in p.problems] + [x for o in self.others for x in o.problems]

    def duplicate_ids(self) -> dict[str, list[Page]]:
        """同じ id のページが2つ以上あるもの（docs/ と stubs/ の両方、二つの分野など）。読んだ順に並べる。"""
        seen: dict[str, list[Page]] = {}
        for p in self.pages:
            seen.setdefault(p.id, []).append(p)
        return {pid: ps for pid, ps in seen.items() if len(ps) > 1}


def load_docs(root: Path, site: Site, dirs: Iterable[str] = PAGE_DIRS) -> Docs:
    """ページを読む。dirs は置き場所（根からの相対。既定は docs と stubs の順）。ない置き場所は飛ばす。
    生成物（分野の入口・lists/）とサイトのトップを置くのは docs/ だけ。"""
    root = Path(root)
    docs = Docs(root)
    fields = set(site.fields)
    for base in dirs:
        bdir = root / base
        if not bdir.is_dir():
            continue
        site_dir = base == DOCS_DIR
        for path in sorted(bdir.rglob("*.md")):
            rel = path.relative_to(bdir).as_posix()
            shown = f"{base}/{rel}"
            parts = rel.split("/")
            if site_dir and parts[0] == LISTS_DIR and len(parts) > 1:
                docs.generated.append(shown)
                continue
            if len(parts) == 2 and parts[0] in fields and parts[1] == INDEX_NAME and site_dir:
                docs.generated.append(shown)          # 分野の入口（stubs/ の index.md は下で置き場所の誤りにする）
                continue
            if len(parts) == 2 and parts[0] in fields and parts[1] != INDEX_NAME:
                stem = parts[1][:-len(".md")]
                md = read_markdown(path, shown, stem)
                if not md.has_front_matter and not md.problems:
                    md.problems.append(Problem(shown, 1, "front matter がない（ページは --- で始まる front matter を持つ）",
                                               "front matter", stem))
                docs.pages.append(Page(md, parts[0], stem, rel, base))
                continue
            md = read_markdown(path, shown)
            docs.others.append(md)
            if not (site_dir and rel == INDEX_NAME):
                docs.problems.append(Problem(shown, None, "置き場所が <分野>/<id>.md でない（分野は site.yml の fields の id。"
                                                          f"手書きのページで型を持たないのは {DOCS_DIR}/{INDEX_NAME} だけ）",
                                             "置き場所"))
    return docs
