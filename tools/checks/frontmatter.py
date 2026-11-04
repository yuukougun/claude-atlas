"""front matter のページだけに当てる検査：読めること・形（page.schema.json）・ファイルの名前と置き場所・stage・章・設定。

形（型・書式・語彙・必須・台帳にないキー）は schema/page.schema.json（tools/make_schema.py がキーの台帳と site.yml
から作る）で見る。schema にしない規則（ファイル名との一致・置き場所と stage・章）はここの関数が見る（keys.yml の note）。
置き場所（design §8.5。2026-11-04 の決定）：骨格のページ（stage が site.yml の stages の最初）は stubs/<field>/<id>.md、
draft 以上は docs/<field>/<id>.md。
"""
from __future__ import annotations

from typing import Iterator

from lib.yamlio import line_at, to_jsonable

from .context import Context
from .core import ERROR, WARNING, Finding, check, joined
from .relations import at

def loaded(ctx: Context, kind: str, files: tuple[str, ...] | None = None) -> Iterator[Finding]:
    """読む層の指摘のうち、その種類のもの（files を渡すと、その頭のファイルだけ）。"""
    for pr in ctx.problems:
        if pr.kind != kind:
            continue
        if files is not None and not pr.file.startswith(files):
            continue
        pages = frozenset({pr.id}) if pr.id and pr.id != "-" else frozenset()
        yield Finding(pr.file, pr.line, pr.id or "-", pr.message, pages)


@check("YAML", ERROR)
def check_yaml(ctx: Context) -> Iterator[Finding]:
    """YAML が読めない（構文の誤り）。同じキーが2回ある（後のものだけが読まれる）：front matter・data/・nav.yml"""
    yield from loaded(ctx, "YAML")


@check("形", ERROR)
def check_shape(ctx: Context) -> Iterator[Finding]:
    """front matter がない・閉じていない・マッピングでない。front matter が schema/page.schema.json に合わない（型・
    書式・語彙・必須・キーの台帳にないキー。キーの台帳は design §3.3 と schema/keys.yml）"""
    yield from loaded(ctx, "front matter")
    v, why = ctx.validator("page")
    if v is None:
        yield Finding("schema/page.schema.json", None, "-", why or "page.schema.json が読めない", severity=WARNING)
        return
    for p in ctx.pages:
        if p.md.meta is None:
            continue
        for issue in v.errors(to_jsonable(p.raw)):
            yield Finding(p.file, line_at(p.raw, issue.path), p.label, issue.format())


@check("id とファイル名", ERROR)
def check_id_matches_file(ctx: Context) -> Iterator[Finding]:
    """front matter の id がファイル名（<id>.md）と違う（id は URL とすべての生成物に使う。design §3.3）"""
    for p in ctx.pages:
        declared = p.declared_id
        if declared is not None and declared != p.stem:
            yield at(ctx, p, f"id「{declared}」がファイル名「{p.stem}.md」と違う（ファイル名を id にそろえる）", "id")


@check("分野とフォルダ", ERROR)
def check_field_matches_folder(ctx: Context) -> Iterator[Finding]:
    """front matter の field がページのフォルダ（<field>/<id>.md の <field>）と違う"""
    for p in ctx.pages:
        declared = p.meta_field
        if declared and declared != p.field:
            yield at(ctx, p, f"field「{declared}」がフォルダの分野「{p.field}」と違う", "field")


@check("置き場所", ERROR)
def check_placement(ctx: Context) -> Iterator[Finding]:
    """ページの置き場所が <分野>/<id>.md でない。骨格のページ（stage が site.yml の stages の最初）が docs/ にある、
    draft 以上のページが stubs/ にある（design §8.5：骨格のページは stubs/ に置き、draft にするときに docs/ へ移す）"""
    yield from loaded(ctx, "置き場所")
    skeleton = ctx.rules.skeleton_stage
    if skeleton is None:
        return
    for p in ctx.pages:
        st = p.stage
        if not st or st not in ctx.rules.stages:
            continue                    # stage のない・語彙にないページは「形」が出す
        if p.in_docs and st == skeleton:
            yield at(ctx, p, f"stage が {skeleton} のページが docs/ にある（骨格のページは stubs/{p.rel} に置く）", "stage")
        elif not p.in_docs and st != skeleton:
            yield at(ctx, p, f"stage が {st} のページが stubs/ にある（{skeleton} でなくなったら docs/{p.rel} へ移す）", "stage")


@check("章", WARNING)
def check_chapter(ctx: Context) -> Iterator[Finding]:
    """ページの chapter が、目次（planning/catalog/<field>.yaml）の chapters にない（目次は骨格の後も、章の正本として
    読む。目次がないか、その分野のファイルに chapters がなければ見ない）"""
    cat = ctx.catalog
    if cat is None:
        return
    for p in ctx.pages:
        c = p.chapter
        if not c:
            continue
        ff = cat.files.get(p.field)
        if ff is None or not ff.readable or not isinstance(ff.raw.get("chapters"), list):
            continue
        if c not in ff.chapters:
            yield at(ctx, p, f"chapter「{c}」が {ff.file} の chapters（{joined(ff.chapters)}）にない", "chapter")


@check("設定", WARNING)
def check_config(ctx: Context) -> Iterator[Finding]:
    """検査の材料が足りない（site.yml に語彙がない、data/ のファイルがない、nav.yml・.claude/settings.json が読めない、
    など）。足りない分の検査はしない"""
    yield from loaded(ctx, "設定")
    for note in ctx.rules.config_notes():
        yield Finding("schema/site.yml", None, "-", note)
