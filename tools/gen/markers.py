"""手書きのページの目印の間を書く（design §8.4）。

  <!-- gen:begin 名前 --> … <!-- gen:end 名前 -->     生成の部分（名前は blocks.py の登録。--list-blocks で一覧）
  <!-- fact:begin <id> --> … <!-- fact:end -->       数値（data/facts.yml の facts。表の値は <id> <行> <列>）
  <!-- name:begin <id> --> … <!-- name:end -->       名前の今の呼び方（data/facts.yml の names の id）
  <!-- link:begin <id>[#<anchor>] --> … <!-- link:end -->  ページへのリンク（未公開なら「題名（準備中）」）

目印の読み方は読む層（lib.markdown.find_markers）のもの。目印の外は1字も変えない。ただし、ページ（docs/<field>/<id>.md）の
本文に参考の節（gen:begin references。sources があるとき）とページ下部（gen:begin page-links）の目印がなければ、本文の
末尾に目印を足して書く（どのページにも要る部分なので、執筆者が置き忘れても出るようにする。参考はページ下部の前）。
入れ子の目印は外側だけを書く（外側の中身は作り直すので、内側は消える）。閉じていない目印・名前の分からない生成の部分・
置き方の合わない目印（1行に置く生成の部分を文の中に置いた、など）は書かずに残し、注意に出す。
生成の部分の中身は、書き方の検査（textlint）から外す印で囲む（目次の題名・別名・サインを写すため。B3 の報告の P2）。
"""
from __future__ import annotations

from lib.markdown import fence_spans, fenced_mask, find_markers

from . import blocks as B
from .text import TEXTLINT_OFF, TEXTLINT_ON

AUTO_BLOCKS = ("references", "page-links")       # ページに目印がなければ末尾に足す部分（この順に並べる）


def implicit_blocks(gen, page) -> list[str]:
    """ページに目印がなく、末尾に足す生成の部分の名前（参考の節は sources があるときだけ）。"""
    have = {B.split_name(m.arg)[0] for m in page.markers_of("gen")}
    out = []
    if "references" not in have and page.sources:
        out.append("references")
    if "page-links" not in have:
        out.append("page-links")
    return out


def empty_pair(name: str) -> str:
    return f"<!-- gen:begin {name} -->\n<!-- gen:end {name} -->"


def insert_missing(gen, page, body: str) -> str:
    """足す目印の組（中身は空）を本文に入れた文字。参考の節は、ページ下部の目印があればその前の行に入れる。"""
    missing = implicit_blocks(gen, page)
    if not missing:
        return body
    if missing == ["references"]:
        mk = next(m for m in page.markers_of("gen") if B.split_name(m.arg)[0] == "page-links")
        line_start = body.rfind("\n", 0, mk.start) + 1
        return body[:line_start] + empty_pair("references") + "\n\n" + body[line_start:]
    added = "\n\n".join(empty_pair(n) for n in missing)
    if not body.strip():
        return "\n" + added + "\n"
    return body.rstrip("\n") + "\n\n" + added + "\n"


def _line_bounds(body: str, start: int, stop: int) -> tuple[str, str]:
    """目印の前の、行の頭からの字と、目印の後の、行の終わりまでの字。"""
    head = body[body.rfind("\n", 0, start) + 1:start]
    eol = body.find("\n", stop)
    tail = body[stop:eol if eol >= 0 else len(body)]
    return head, tail


def wrap_block(content: str, indent: str) -> str:
    """1行に置く生成の部分の、目印の間に置く文字（中身があれば textlint の印で囲み、前後に空行を置く）。"""
    if not content.strip():
        return "\n" + indent
    lines = [indent + TEXTLINT_OFF, ""]
    lines += [(indent + x) if x.strip() else "" for x in content.strip("\n").split("\n")]
    lines += ["", indent + TEXTLINT_ON]
    return "\n" + "\n".join(lines) + "\n" + indent


def render_marker(gen, base: dict, mk, body: str, where: str) -> str | None:
    """目印1つの間に置く文字（書かないときは None）。"""
    if mk.kind == "link":
        return gen.ref_link(base["host"], mk.arg) if mk.arg else None   # field:<分野の id> は gen.ref_link が分野の入口にする
    if mk.kind == "fact":
        from .facts import fact_text            # 循環を避ける
        return fact_text(gen, base["host"], mk.arg) if mk.arg else None
    if mk.kind == "name":
        from .facts import name_text            # 循環を避ける
        return name_text(gen, base["host"], mk.arg) if mk.arg else None
    blk, param = B.lookup(mk.arg)
    if blk is None:
        gen.note(f"{where}:{mk.line}: 知らない生成の部分「{mk.arg}」（--list-blocks で一覧。書かずに残した）")
        return None
    if param and not blk.param:
        gen.note(f"{where}:{mk.line}: 生成の部分「{blk.name}」は引数を取らない（「{mk.arg}」。書かずに残した）")
        return None
    if blk.param and not param and not blk.param_optional:
        gen.note(f"{where}:{mk.line}: 生成の部分「{blk.name}」に引数（{blk.param}）がない（書かずに残した）")
        return None
    head, tail = _line_bounds(body, mk.start, mk.inner_start)
    alone = not head.strip() and not tail.strip()
    if blk.kind == "block" and not alone:
        gen.note(f"{where}:{mk.line}: 生成の部分「{mk.arg}」は、目印をそれぞれ1行に置く（文の中に置かない。書かずに残した）")
        return None
    content = blk.render(B.Ctx(gen, base["page"], base["host"], base["url"], param, mk.arg))
    if blk.kind == "inline":
        return " ".join(content.split("\n"))
    return wrap_block(content, head)


def apply_markers(gen, text: str, body: str, markers: list, page, host: str, url: str, where: str,
                  first_line: int = 1) -> str:
    """本文の目印の間を書き直した、ファイルの全体の文字。text はファイルの全体、body は front matter の後、
    first_line は本文の1行目のファイルの行。page はページ（docs/index.md のときは None）。"""
    prefix = text[:len(text) - len(body)] if text.endswith(body) else ""
    if page is not None:
        added = insert_missing(gen, page, body)
        if added != body:
            body = added
            lines = body.split("\n")
            markers, _ = find_markers(body, lines, fenced_mask(lines, fence_spans(lines)), first_line, where, page.id)
    base = {"page": page, "host": host, "url": url}
    pieces: list[str] = []
    pos = 0
    covered = -1                                      # 書き直した外側の目印の終わり
    for mk in sorted(markers, key=lambda m: m.start):
        if mk.start < covered:
            continue                                  # 外側の目印の中（外側を作り直すので書かない）
        if not mk.closed:
            gen.note(f"{where}:{mk.line}: {mk.kind}:begin「{mk.arg}」が閉じていない（書かずに残した）")
            continue
        content = render_marker(gen, base, mk, body, where)
        if content is None:
            continue
        pieces.append(body[pos:mk.inner_start])
        pieces.append(content)
        pos = mk.inner_end
        covered = mk.stop
    pieces.append(body[pos:])
    return prefix + "".join(pieces)
