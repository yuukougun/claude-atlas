"""本文（front matter の後）の検査：目印・sections と見出し・冒頭の要点と別名の行・手書きのリンク・link の目印・
ナビゲーション（nav.yml）。

本文の形は planning/guides/common.md §3（冒頭）・§4（見出しと節）・§10（ほかのページを指す）。本文を見るのは
骨格でないページ（draft 以上。docs/ にあるもの）だけ（骨格のページの本文は骨格の道具が作り、執筆で書き直す）。
手書きのリンクは、フェンス・行の中のコード・HTML のコメント・目印の中（道具が書く所）の外だけを見る。

未公開のページ（design §8.4）：骨格のページ（stubs/）と、公開から外した試作のページ（nav.yml の exclude_docs）。
手書きの Markdown のリンクでこれらを指すと、MkDocs 1.6.1 は exclude_docs で外したページへのリンクを INFO でしか
出さず、公開のサイトで 404 になる（design §8.5）。ここで止める。
"""
from __future__ import annotations

import posixpath
import re
from typing import Iterator

from lib.base import Ref
from lib.markdown import mask_code_spans

from .context import Context
from .core import ERROR, WARNING, Finding, check, joined
from .relations import at
from .rules import (ABSTRACT_FREE_TYPES, ABSTRACT_HEAD, ALIASES_LABEL, ALIASES_SEP, NONE_TEXT, PREREQUISITE_LABEL,
                    TEXTLINT_OFF, TEXTLINT_ON)

COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
INLINE_LINK_RE = re.compile(r"(!?)\[((?:[^\[\]\\]|\\.|\[[^\]]*\])*)\]\(\s*(<[^>]*>|[^)\s]+)"
                            r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)")
REF_DEF_RE = re.compile(r"^ {0,3}\[([^\]]+)\]:\s*(<[^>]*>|\S+)")
HREF_RE = re.compile(r"""\bhref\s*=\s*(["'])(.*?)\1""", re.I)
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
H2_RE = re.compile(r"^ {0,3}## ")
ITEM_RE = re.compile(r"^(?P<indent> {4})- (?P<rest>.*)$")
PREREQ_ITEM_RE = re.compile(r"^ {4}- \*\*" + re.escape(PREREQUISITE_LABEL) + r"\*\*[：:](?P<rest>.*)$")
HEADING_MARKS = ("`", "**", "](", "<", "{", "}")
TAB_RE = re.compile(r'^(?P<indent> *)===\+? "(?P<label>[^"]*)"\s*$')


# ---------------------------------------------------------------- 本文の見方


def written(ctx: Context):
    """本文を見るページ：docs/ にある、骨格でないページ（front matter の読めないページは「形」だけを出す）。"""
    return [p for p in ctx.pages if getattr(p, "in_docs", False) and not ctx.is_stub(p) and p.md.meta is not None]


def masked_lines(md, markers) -> list[str]:
    """本文の行（フェンスの中・行の中のコード・HTML のコメント・目印の begin から end までを、同じ長さの空白にしたもの）。"""
    lines = [(" " * len(x)) if md.fenced[i] else mask_code_spans(x) for i, x in enumerate(md.lines)]
    chars = list("\n".join(lines))

    def blank(a: int, b: int) -> None:
        for k in range(max(a, 0), min(b, len(chars))):
            if chars[k] != "\n":
                chars[k] = " "
    for m in markers:
        blank(m.start, m.stop if m.closed else m.inner_start)
    text = "".join(chars)
    for m in COMMENT_RE.finditer(text):
        blank(m.start(), m.end())
    return "".join(chars).split("\n")


def first_h2(p) -> int:
    """最初の ## の本文の中の行（0 から。なければ行数）。"""
    for h in p.headings:
        if h.level == 2:
            return h.line - p.body_line
    return len(p.lines)


def opening(p) -> tuple[int | None, int, int]:
    """冒頭の要点の囲み：(見出しの行, 囲みの終わりの次の行, 最初の ## の行)。行は本文の中の位置（0 から）。
    囲みがなければ最初の行が None。HTML のコメントだけの行と空行は飛ばす。"""
    lines = p.lines
    stop = first_h2(p)
    i = 0
    while i < stop and (not lines[i].strip() or COMMENT_RE.fullmatch(lines[i].strip())):
        i += 1
    if i >= stop or lines[i].rstrip() != ABSTRACT_HEAD:
        return None, i, stop
    j = i + 1
    while j < stop and (not lines[j].strip() or lines[j].startswith(("    ", "\t"))):
        j += 1
    return i, j, stop


# ---------------------------------------------------------------- 目印・節・見出し


@check("目印", ERROR)
def check_markers(ctx: Context) -> Iterator[Finding]:
    """目印（<!-- gen:begin … -->・<!-- fact:begin … -->・<!-- link:begin … -->）の対が合わない：閉じていない、begin の
    ない end、名前の違う end、名前のない begin と gen:end、同じ種類の入れ子（design §8.4）"""
    for pr in ctx.problems:
        if pr.kind == "目印":
            yield Finding(pr.file, pr.line, pr.id or "-", pr.message, frozenset({pr.id}) if pr.id != "-" else frozenset())


@check("sections", ERROR)
def check_sections(ctx: Context) -> Iterator[Finding]:
    """sections の anchor の見出し（## <title> {#<anchor>}）が本文にない。見出しの文字が sections の title と違うもの
    は警告（title を見出しに合わせて直してよい。common.md §2.2・§4）"""
    for p in written(ctx):
        heads = {}
        for h in p.headings:
            if h.anchor and h.anchor not in heads:
                heads[h.anchor] = h
        for sec in p.sections:
            a, t = str(sec.get("anchor") or "").strip(), str(sec.get("title") or "").strip()
            if not a:
                continue
            h = heads.get(a)
            if h is None:
                yield at(ctx, p, f"sections の anchor「{a}」の見出しが本文にない（## {t} {{#{a}}} の形で置く）", "sections")
            elif t and h.text != t:
                yield Finding(p.file, h.line, p.label, f"見出し「{h.text}」が sections の title「{t}」と違う（title を見出しに"
                                                       "合わせる）", severity=WARNING)


@check("見出し", ERROR)
def check_headings(ctx: Context) -> Iterator[Finding]:
    """本文に H1（# …）がある（題名は front matter の title からテンプレートが出す。見出しは ## から）。見出しに記法
    （` ** ]( < と波かっこ。末尾の {#anchor} は除く）がある（目次・節へのリンク・検索に記法のまま出る。common.md §4）"""
    for p in written(ctx):
        for h in p.headings:
            if h.level == 1:
                yield Finding(p.file, h.line, p.label, f"本文に H1「# {h.text}」がある（題名は title からテンプレートが出す。"
                                                       "見出しは ## から）")
                continue
            marks = [m for m in HEADING_MARKS if m in h.text]
            if marks:
                yield Finding(p.file, h.line, p.label, f"見出し「{h.text}」に記法（{' '.join(marks)}）がある（平文にする。"
                                                       "波かっこは末尾の {#anchor} だけ）")


# ---------------------------------------------------------------- 冒頭


@check("要点", ERROR)
def check_abstract(ctx: Context) -> Iterator[Finding]:
    """本文の最初（最初の ## より前）に要点の囲み（!!! abstract "要点"）がない。要点の後に導入（題名を主語にした1〜3文）
    がないものは警告（requirements §5.1「全ページで必ず置くのは front matter と冒頭の要点だけ」。common.md §3）"""
    for p in written(ctx):
        head, end, stop = opening(p)
        if head is None:
            line = p.body_line + min(end, max(len(p.lines) - 1, 0))
            yield Finding(p.file, line, p.label, f"本文の最初に要点の囲み（{ABSTRACT_HEAD}）がない（最初の ## より前に、"
                                                 "要点・別名の行・導入の順で置く）")
            continue
        rest = [x for x in p.lines[end:stop]
                if x.strip() and not COMMENT_RE.fullmatch(x.strip()) and not x.startswith(ALIASES_LABEL)]
        if not rest:
            yield Finding(p.file, p.body_line + head, p.label, "要点の後に導入（題名を主語にした1〜3文）がない",
                          severity=WARNING)


@check("要点の前提", ERROR)
def check_abstract_prerequisites(ctx: Context) -> Iterator[Finding]:
    """要点の囲みの「- **前提**：」の項目が、front matter の prerequisites と合わない（すべてを link の目印で並べる。
    ないときは「なし」。項目がない。guide と hub は項目を内容に合わせて変えてよいので、項目がなければ見ない）"""
    for p in written(ctx):
        head, end, _ = opening(p)
        if head is None:
            continue                     # 「要点」が出す
        lines = p.lines
        item = next((k for k in range(head + 1, end) if PREREQ_ITEM_RE.match(lines[k])), None)
        if item is None:
            if p.type not in ABSTRACT_FREE_TYPES:
                yield Finding(p.file, p.body_line + head, p.label, f"要点の囲みに「- **{PREREQUISITE_LABEL}**：」の項目がない"
                                                                   f"（prerequisites を link の目印で並べる。ないときは「{NONE_TEXT}」）")
            continue
        last = item + 1
        while last < end and lines[last].strip() and not ITEM_RE.match(lines[last]) and lines[last].startswith("      "):
            last += 1
        first_line, last_line = p.body_line + item, p.body_line + last - 1
        found = [Ref.parse(m.arg).target for m in p.markers
                 if m.kind == "link" and m.arg and first_line <= m.line <= last_line]
        want = [r.target for r in p.prerequisites if r.target]
        if not want:
            text = re.sub(r"<!--.*?-->", "", PREREQ_ITEM_RE.match(lines[item]).group("rest")).strip()
            if found or text != NONE_TEXT:
                yield Finding(p.file, first_line, p.label, f"prerequisites が空なので、前提の項目は「{NONE_TEXT}」と書く")
            continue
        for t in want:
            if t not in found:
                yield Finding(p.file, first_line, p.label, f"前提の項目に prerequisites の「{t}」がない（link の目印で並べる）",
                              frozenset({t}))
        for t in found:
            if t not in want:
                yield Finding(p.file, first_line, p.label, f"前提の項目の「{t}」が prerequisites にない", frozenset({t}))


@check("別名の行", ERROR)
def check_aliases_line(ctx: Context) -> Iterator[Finding]:
    """冒頭（最初の ## より前）の別名の行（別名：a・b）が aliases と合わない：aliases があるのに行がない・名前が欠けて
    いる・aliases が空なのに行がある、<!-- textlint-disable -->〜<!-- textlint-enable --> で囲んでいない。並びや
    余分な名前は警告（common.md §3）"""
    for p in written(ctx):
        stop = first_h2(p)
        lines = p.lines
        rows = [k for k in range(stop) if lines[k].startswith(ALIASES_LABEL)]
        aliases = p.aliases
        if not aliases:
            for k in rows:
                yield Finding(p.file, p.body_line + k, p.label, "aliases が空なのに別名の行がある（行を外すか、aliases を提案する）")
            continue
        if not rows:
            yield at(ctx, p, f"別名の行がない（要点の後に「{ALIASES_LABEL}{ALIASES_SEP.join(aliases)}」を置き、"
                             f"{TEXTLINT_OFF}〜{TEXTLINT_ON} で囲む）", "aliases")
            continue
        k = rows[0]
        line = p.body_line + k
        rest = lines[k][len(ALIASES_LABEL):].strip()
        before = next((lines[j].strip() for j in range(k - 1, -1, -1) if lines[j].strip()), "")
        after = next((lines[j].strip() for j in range(k + 1, len(lines)) if lines[j].strip()), "")
        if before != TEXTLINT_OFF or after != TEXTLINT_ON:
            yield Finding(p.file, line, p.label, f"別名の行を {TEXTLINT_OFF}〜{TEXTLINT_ON} で囲む（表記の揺れを書き方の検査から外す）")
        missing = [a for a in aliases if a not in rest]
        for a in missing:
            yield Finding(p.file, line, p.label, f"別名の行に aliases の「{a}」がない")
        expected = ALIASES_SEP.join(aliases)
        if not missing and rest != expected:
            yield Finding(p.file, line, p.label, f"別名の行を aliases の並びのとおり「{ALIASES_LABEL}{expected}」にする",
                          severity=WARNING)
        for extra in rows[1:]:
            yield Finding(p.file, p.body_line + extra, p.label, "別名の行が2つある（1つにする）")


def tab_sets(p) -> list[list[tuple[int, str]]]:
    """本文のタブ（=== "名前"）の組：[(本文の中の行, 名前), …] の並び。同じ字下げで続くものを1つの組にし、それより
    浅い字下げの行が来たら組を閉じる（フェンスの中は見ない）。"""
    sets: list[list[tuple[int, str]]] = []
    open_: dict[int, list[tuple[int, str]]] = {}
    for i, raw in enumerate(p.lines):
        if p.md.fenced[i]:
            continue
        m = TAB_RE.match(raw)
        if m:
            ind = len(m.group("indent"))
            for k in [k for k in open_ if k > ind]:
                del open_[k]
            if ind not in open_:
                open_[ind] = []
                sets.append(open_[ind])
            open_[ind].append((i, m.group("label")))
            continue
        if raw.strip():
            ind = len(raw) - len(raw.lstrip(" "))
            for k in [k for k in open_ if k >= ind]:
                del open_[k]
    return sets


@check("タブの面", ERROR)
def check_surface_tabs(ctx: Context) -> Iterator[Finding]:
    """面のタブ（名前が面の表示の名前の組。nav.yml の extra.ca.surfaces）が、front matter の surfaces にない面を持つ、
    site.yml の surfaces の並び（アプリ → Claude Code → API）でない。面のタブの組に面でないタブがあるものは警告
    （common.md §6）"""
    labels = ctx.nav.surface_labels if ctx.nav is not None else {}
    order = ctx.site.vocab("surfaces") or []
    by_label = {v: k for k, v in labels.items()}
    pages = [(p, tab_sets(p)) for p in written(ctx)]
    if not labels:
        if any(sets for _, sets in pages) and ctx.nav is not None and ctx.nav.present:
            yield Finding(ctx.nav.file, None, "-", "nav.yml の extra.ca.surfaces（面の表示の名前。作る層が書く）がないので、"
                                                   "面のタブを見ない", severity=WARNING)
        return
    rank = {s: i for i, s in enumerate(order)}
    for p, sets in pages:
        for tabs in sets:
            ids = [by_label.get(name) for _, name in tabs]
            if not any(ids):
                continue                       # 面のタブでない（Before と After など）
            line = p.body_line + tabs[0][0]
            for (_, name), sid in zip(tabs, ids):
                if sid is None:
                    yield Finding(p.file, line, p.label, f"面のタブの組に、面でないタブ「{name}」がある", severity=WARNING)
                elif sid not in p.surfaces:
                    yield Finding(p.file, line, p.label, f"タブ「{name}」の面（{sid}）が front matter の surfaces にない"
                                                         f"（surfaces：{joined(p.surfaces) or 'なし'}）")
            got = [sid for sid in ids if sid]
            if got != sorted(got, key=lambda s: rank.get(s, len(rank))):
                want = joined(labels[s] for s in sorted(got, key=lambda s: rank.get(s, len(rank))))
                yield Finding(p.file, line, p.label, f"面のタブの並びを {want} にする（site.yml の surfaces の順）")


# ---------------------------------------------------------------- リンク


def link_targets(lines: list[str]) -> Iterator[tuple[int, str]]:
    """本文の行（masked_lines）から、リンクの行き先 (行の位置, 行き先) を出す（画像は除く）。"""
    for i, line in enumerate(lines):
        for m in INLINE_LINK_RE.finditer(line):
            if not m.group(1):
                yield i, m.group(3).strip("<>")
        m = REF_DEF_RE.match(line)
        if m:
            yield i, m.group(2).strip("<>")
        for m in HREF_RE.finditer(line):
            yield i, m.group(2)


def resolve_link(page_dir: str, target: str, site_url: str) -> str | None:
    """行き先を docs/ からの相対の .md のパスにする（サイトの中のページへのリンクでなければ None）。"""
    t = target.strip()
    if site_url and t.startswith(site_url):
        path = t[len(site_url):].split("#")[0].split("?")[0].strip("/")
        return (path + ".md") if path else "index.md"
    if not t or t.startswith(("#", "/")) or SCHEME_RE.match(t):
        return None
    path = t.split("#")[0].split("?")[0]
    if not path.endswith(".md"):
        return None
    return posixpath.normpath(posixpath.join(page_dir, path))


def link_sources(ctx: Context):
    """手書きのリンクを見るもの：(表示のパス, ページの id, docs/ からの相対のフォルダ, Markdown, 目印)。"""
    for p in written(ctx):
        yield p.file, p.label, p.field, p.md, p.markers
    docs = ctx.atlas.docs
    for md in (docs.others if docs is not None else []):
        if md.shown == "docs/index.md":
            yield md.shown, "-", "", md, md.markers


@check("未公開のページへのリンク", ERROR)
def check_unpublished_links(ctx: Context) -> Iterator[Finding]:
    """目印の外の手書きの Markdown のリンクが、未公開のページ（骨格のページ・exclude_docs で公開から外したページ）か、
    ないページを指す（相手を公開したら道具が書き直せるよう、<!-- link:begin <id> --> の目印にする。design §8.4）"""
    pages = {p.rel: p for p in ctx.pages if getattr(p, "in_docs", False)}
    stubs = {p.rel: p for p in ctx.pages if not getattr(p, "in_docs", True)}
    site_url = _site_url(ctx)
    for shown, label, folder, md, markers in link_sources(ctx):
        lines = masked_lines(md, markers)
        for i, target in link_targets(lines):
            rel = resolve_link(folder, target, site_url)
            if rel is None:
                continue
            line = md.body_line + i
            q = pages.get(rel)
            if q is not None:
                if not ctx.published(q):
                    why = ("exclude_docs で公開から外したページ" if q.id in ctx.atlas.held_back
                           else f"stage が {q.stage or '（なし）'} のページ")
                    yield Finding(shown, line, label, f"手書きのリンク「{target}」が未公開のページ {q.id}（{why}）を指す"
                                                      f"（<!-- link:begin {q.id} --><!-- link:end --> にする）", frozenset({q.id}))
                continue
            stub_rel = rel[len("../stubs/"):] if rel.startswith("../stubs/") else rel
            s = stubs.get(stub_rel)
            if s is not None:
                yield Finding(shown, line, label, f"手書きのリンク「{target}」が未公開の骨格のページ {s.id}（stubs/{s.rel}）を指す"
                                                  f"（<!-- link:begin {s.id} --><!-- link:end --> にする）", frozenset({s.id}))
                continue
            if rel.startswith("../") or not (ctx.root / "docs" / rel).is_file():
                yield Finding(shown, line, label, f"手書きのリンク「{target}」の先のページがない")


def _site_url(ctx: Context) -> str:
    """mkdocs.yml の site_url（読めなければ空）。"""
    path = ctx.root / "mkdocs.yml"
    try:
        for line in path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^site_url:\s*['\"]?([^'\"\s#]+)", line)
            if m:
                return m.group(1)
    except OSError:
        pass
    return ""


@check("link の目印", ERROR)
def check_link_markers(ctx: Context) -> Iterator[Finding]:
    """本文の link の目印（<!-- link:begin <id>[#<anchor>] -->）の id のページがない。#anchor が相手の sections にない
    （道具が相手の題名とリンクを書けない。common.md §10）"""
    for p in ctx.pages:
        if not hasattr(p, "markers"):
            continue
        for m in p.markers:
            if m.kind != "link" or not m.arg:
                continue
            ref = Ref.parse(m.arg)
            q = ctx.page(ref.target)
            if q is None:
                yield Finding(p.file, m.line, p.label, f"link の目印の「{m.arg}」のページがない", frozenset({ref.target}))
            elif ref.anchor is not None and ref.anchor not in q.anchors():
                have = f"あるのは {joined(q.anchors())}" if q.anchors() else "sections がない"
                yield Finding(p.file, m.line, p.label, f"link の目印の「{m.arg}」: {q.id} の sections に anchor「{ref.anchor}」が"
                                                       f"ない（{have}）", frozenset({q.id}))


@check("ナビゲーション", ERROR)
def check_nav(ctx: Context) -> Iterator[Finding]:
    """nav.yml の nav に、exclude_docs で外したページがある（MkDocs はナビゲーションに 404 のリンクを残す。build-B1.md
    §2.3）。exclude_docs が、ページ（<分野>/<id>.md）でないファイルに当たる・どのファイルにも当たらないものは警告"""
    nav = ctx.nav
    if nav is None or not nav.present:
        return
    for rel in nav.entries:
        if nav.excluded(rel):
            yield Finding(nav.file, nav.nav_line, "-", f"nav に、exclude_docs で外した「{rel}」がある（公開から外したページは "
                                                       "nav に載せない）")
    if not nav.exclude:
        return
    docs_dir = ctx.root / "docs"
    files = sorted(x.relative_to(docs_dir).as_posix() for x in docs_dir.rglob("*") if x.is_file()) if docs_dir.is_dir() else []
    pages = {p.rel for p in ctx.pages if getattr(p, "in_docs", False)}
    from .config import ignored
    for rule in nav.exclude:
        hits = [f for f in files if ignored([rule], f)] if not rule.negate else None
        if hits is None:
            continue
        if not hits:
            yield Finding(nav.file, nav.exclude_line, "-", f"exclude_docs の「{rule.raw}」がどのファイルにも当たらない（外す"
                                                            "ページを docs/ から移したなら消す）", severity=WARNING)
        for f in hits:
            if f.endswith(".md") and f not in pages:
                yield Finding(nav.file, nav.exclude_line, "-", f"exclude_docs の「{rule.raw}」が、ページでない「docs/{f}」に"
                                                                "当たる（公開から外すのは試作のページだけ）", severity=WARNING)
