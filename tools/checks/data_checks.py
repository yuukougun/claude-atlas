"""数値と出典の検査（設計書 §8.6 の「数値と出典」の行・§6.8・§9.1・§10.5 の H1）。

  data/facts.yml            facts・features・names        → schema/facts.schema.json
  data/sources.yml          domains・sources              → schema/sources.schema.json
  data/sources.d/<id>.yml   ページごとの domains・sources → schema/sources.schema.json（<id> はページの id）
  data/outdated-advice.yml  advice                        → schema/outdated-advice.schema.json
  data/inspection.yml       last                          → schema/inspection.schema.json

ページが指す id（fact の目印・tracks・outdated_advice・sources）がないものは誤り。ただし骨格のページ（stub）だけが指す
ものは警告にする（data の初版（6b）は第一波のページが指す id だけをそろえる。design §10.1）。
AI の利用を断るドメイン（domains の noai: true）は、.claude/settings.json の deny に2つの形（WebFetch(domain:<d>) と
WebFetch(domain:*.<d>)）で入れる（H1）。deny のドメインは、tools/check_noai.py の KNOWN_NOAI と、外部リンクの検査
（.github/workflows/links.yml の lychee の --exclude）にも入れる（どちらも取得しないため）。
"""
from __future__ import annotations

import ast
import re
from typing import Iterator

import yaml

from lib.data import host_of, page_of_sources_file, url_key
from lib.yamlio import line_at, to_jsonable

from .context import Context, where
from .core import ERROR, WARNING, Finding, check, joined

SCHEMA_OF = {"data/facts.yml": "facts", "data/sources.yml": "sources", "data/outdated-advice.yml": "outdated-advice",
             "data/inspection.yml": "inspection"}
SOURCES_D = "data/sources.d/"
LINKS_WORKFLOW = ".github/workflows/links.yml"
NOAI_TOOL = "tools/check_noai.py"


def schema_name(file: str) -> str | None:
    if file in SCHEMA_OF:
        return SCHEMA_OF[file]
    if file.startswith(SOURCES_D) and file.endswith(".yml"):
        return "sources"
    return None


def file_pages(file: str) -> frozenset[str]:
    """data/sources.d/<id>.yml なら、そのページ（--page で選ぶため）。"""
    pid = page_of_sources_file(file)
    return frozenset({pid}) if pid else frozenset()


def item_at(it, message: str, key: str | None = None, severity: str | None = None) -> Finding:
    return Finding(it.file, it.key_line(key) if key else it.line, it.label, message, file_pages(it.file), severity)


def demote(ctx: Context, p) -> str | None:
    """骨格のページだけが指すものは警告にする。"""
    return WARNING if ctx.is_stub(p) else None


@check("data の形", ERROR)
def check_data_shape(ctx: Context) -> Iterator[Finding]:
    """data/ のファイルが schema（schema/facts.schema.json など。キーの台帳 schema/keys.yml から作る）に合わない。
    最上位がマッピングでない"""
    data = ctx.data
    if data is None:
        return
    for pr in ctx.problems:
        if pr.kind == "形" and pr.file.startswith("data/"):
            yield Finding(pr.file, pr.line, pr.id or "-", pr.message, file_pages(pr.file))
    for f, df in data.files.items():
        name = schema_name(f)
        if name is None or df.raw is None:
            continue
        v, why = ctx.validator(name)
        if v is None:
            yield Finding(f"schema/{name}.schema.json", None, "-", why or "schema が読めない", severity=WARNING)
            continue
        for issue in v.errors(to_jsonable(df.raw)):
            label = "-"
            if len(issue.path) >= 2 and isinstance(issue.path[1], int):
                items = df.raw.get(issue.path[0])
                if isinstance(items, list) and issue.path[1] < len(items) and isinstance(items[issue.path[1]], dict):
                    x = items[issue.path[1]].get("domain" if issue.path[0] == "domains" else "id")
                    label = x if isinstance(x, str) and x else "-"
            yield Finding(f, line_at(df.raw, issue.path), label, issue.format(), file_pages(f))


@check("data の id の重複", ERROR)
def check_data_duplicates(ctx: Context) -> Iterator[Finding]:
    """data の同じ節に同じ id が2つ以上ある（facts・features・names・sources〔sources.yml と sources.d/ をまとめて〕・
    advice・domains〔大文字と小文字を区別しない〕）"""
    data = ctx.data
    if data is None:
        return
    for section in ("facts", "features", "names", "sources", "advice", "domains"):
        first: dict[str, object] = {}
        for it in data.entries(section):
            key = it.id.lower() if (it.id and section == "domains") else it.id
            if key is None:
                continue
            q = first.setdefault(key, it)
            if q is not it:
                yield item_at(it, f"{section} の「{it.id}」が {where(q)} にもある（1つにする）", "domain" if section == "domains" else "id")


@check("facts の id", ERROR)
def check_fact_ids(ctx: Context) -> Iterator[Finding]:
    """本文の fact の目印（<!-- fact:begin <id> -->）と fact-table の目印（<!-- gen:begin fact-table <id> -->）の id が
    data/facts.yml の facts にない"""
    data = ctx.data
    if data is None:
        return
    facts = data.facts
    for p in ctx.pages:
        for m in getattr(p, "markers", []):
            gen_name = m.arg.split() if m.kind == "gen" else []
            if m.kind == "fact" and m.arg:
                fid, what = m.arg.split()[0], "fact の目印"
            elif gen_name[:1] == ["fact-table"] and len(gen_name) > 1:
                fid, what = gen_name[1], "fact-table の目印"
            else:
                continue
            if fid not in facts:
                yield Finding(p.file, m.line, p.label, f"{what}の「{fid}」が data/facts.yml の facts にない"
                                                       "（数値の提案のファイルに書いて、メインに足してもらう）",
                              severity=demote(ctx, p))


@check("tracks の id", ERROR)
def check_track_ids(ctx: Context) -> Iterator[Finding]:
    """ページの tracks の id が data/facts.yml の features にない（骨格のページだけなら警告）"""
    data = ctx.data
    if data is None:
        return
    features = data.features
    for p in ctx.pages:
        for t in p.tracks:
            if t not in features:
                yield Finding(p.file, p.key_line("tracks"), p.label, f"tracks の「{t}」が data/facts.yml の features にない",
                              severity=demote(ctx, p))


@check("outdated_advice の id", ERROR)
def check_advice_ids(ctx: Context) -> Iterator[Finding]:
    """ページの outdated_advice の id が data/outdated-advice.yml の advice にない（骨格のページだけなら警告）"""
    data = ctx.data
    if data is None:
        return
    advice = data.advice
    for p in ctx.pages:
        for a in p.outdated_advice:
            if a not in advice:
                yield Finding(p.file, p.key_line("outdated_advice"), p.label,
                              f"outdated_advice の「{a}」が data/outdated-advice.yml の advice にない", severity=demote(ctx, p))


@check("sources の id", ERROR)
def check_source_ids(ctx: Context) -> Iterator[Finding]:
    """ページの sources と、data の項目（facts・features・names・advice と、facts の conflict）の sources の id が、
    data/sources.yml と data/sources.d/ の sources にない（骨格のページだけなら警告）"""
    data = ctx.data
    if data is None:
        return
    known = data.sources
    for p in ctx.pages:
        for s in p.sources:
            if s not in known:
                yield Finding(p.file, p.key_line("sources"), p.label,
                              f"sources の「{s}」が data/sources.yml にも data/sources.d/ にもない（新しい出典は "
                              f"data/sources.d/{p.id}.yml に足す）", severity=demote(ctx, p))
    for section in ("facts", "features", "names", "advice"):
        for it in data.entries(section):
            refs = list(it.strings("sources"))
            for c in it.parts("conflict"):
                refs += [x for x in c.get("sources") or [] if isinstance(x, str)]
            for s in dict.fromkeys(refs):
                if s not in known:
                    yield item_at(it, f"{section} の「{it.label}」の sources の「{s}」が出典にない", "sources")


@check("data の参照", ERROR)
def check_data_refs(ctx: Context) -> Iterator[Finding]:
    """data の中の参照が解決しない：features の page（主のページ）がない、names の feature が features にない、advice の
    name が names にない。data/sources.d/<id>.yml の <id> がページの id でない"""
    data = ctx.data
    if data is None:
        return
    for it in data.entries("features"):
        pg = it.text("page")
        if pg and ctx.page(pg) is None:
            yield item_at(it, f"features の「{it.label}」の page「{pg}」のページがない", "page")
    for it in data.entries("names"):
        ft = it.text("feature")
        if ft and ft not in data.features:
            yield item_at(it, f"names の「{it.label}」の feature「{ft}」が features にない", "feature")
    for it in data.entries("advice"):
        nm = it.text("name")
        if nm and nm not in data.names:
            yield item_at(it, f"advice の「{it.label}」の name「{nm}」が facts.yml の names にない", "name")
    for f in data.files:
        pid = page_of_sources_file(f)
        if pid and ctx.page(pid) is None:
            yield Finding(f, None, "-", f"data/sources.d/ のファイル名「{pid}」がページの id でない（<ページの id>.yml にする）")


@check("出典の URL の重なり", ERROR)
def check_source_urls(ctx: Context) -> Iterator[Finding]:
    """同じ URL（scheme とホストの大文字と小文字・既定のポート・#… と末尾の / を除いて比べる）の出典が2つ以上ある
    （同じ URL の出典を二つ作らない。common.md §11）"""
    data = ctx.data
    if data is None:
        return
    first: dict[str, object] = {}
    for it in data.entries("sources"):
        url = it.text("url")
        if not url:
            continue
        q = first.setdefault(url_key(url), it)
        if q is not it:
            yield item_at(it, f"出典「{it.label}」の URL が {where(q)} の「{q.label}」と同じ（同じ URL の出典を二つ作らない）",
                          "url")


@check("AI の利用の指定", ERROR)
def check_noai_recorded(ctx: Context) -> Iterator[Finding]:
    """出典の URL のドメインの AI の利用の指定（data の domains）が記録されていない、断る指定のあるドメイン（noai: true）
    の出典がある。確かめられなかったドメイン（noai: null）は警告（未確認。design §6.8）"""
    data = ctx.data
    if data is None:
        return
    for it in data.entries("sources"):
        url = it.text("url")
        if not url:
            continue
        host = host_of(url)
        d = data.domain_entry(url)
        if d is None:
            yield item_at(it, f"出典「{it.label}」のドメイン「{host}」の AI の利用の指定が domains にない（tools/check_noai.py で"
                              "確かめて、同じファイルの domains に書く）", "url")
        elif d.raw.get("noai") is True:
            yield item_at(it, f"出典「{it.label}」のドメイン「{host}」は AI の利用を断っている（{where(d)}。資料にしない）", "url")
        elif d.raw.get("noai") is None:
            yield item_at(it, f"出典「{it.label}」のドメイン「{host}」の AI の利用の指定が未確認（{where(d)} の noai が null）",
                          "url", WARNING)


def known_noai(root) -> list[str] | None:
    """tools/check_noai.py の KNOWN_NOAI のドメイン（読めなければ None）。import せずに字句で読む。"""
    path = root / NOAI_TOOL
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError, UnicodeDecodeError):
        return None
    # check_noai.py が .claude/settings.json の deny を自分で読む形（_deny_domains）なら、一覧は食い違わない（比べない）
    if any(isinstance(node, ast.FunctionDef) and node.name == "_deny_domains" for node in tree.body):
        return None
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "KNOWN_NOAI" for t in node.targets):
            try:
                value = ast.literal_eval(node.value)
            except ValueError:
                return None
            return [str(k).lower() for k in value] if isinstance(value, dict) else None
    return None


def lychee_excludes(root) -> list[str] | None:
    """links.yml の lychee の --exclude の正規表現（ファイルがなければ None）。"""
    path = root / LINKS_WORKFLOW
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError, UnicodeDecodeError):
        return None
    out: list[str] = []
    jobs = data.get("jobs") if isinstance(data, dict) else None
    for job in (jobs or {}).values():
        for step in (job or {}).get("steps") or []:
            args = ((step or {}).get("with") or {}).get("args")
            if isinstance(args, str):
                out += re.findall(r"--exclude\s+'([^']+)'", args) + re.findall(r'--exclude\s+"([^"]+)"', args)
    return out


@check("断るドメインと deny", ERROR)
def check_noai_deny(ctx: Context) -> Iterator[Finding]:
    """AI の利用を断るドメイン（data の domains の noai: true）が、.claude/settings.json の deny に2つの形
    （WebFetch(domain:<d>) と WebFetch(domain:*.<d>)）でない（H1）。deny のドメインが tools/check_noai.py の KNOWN_NOAI
    と links.yml の lychee の --exclude にないものは警告（取得しないための一覧が食い違う）"""
    s = ctx.settings
    if s is None or s.deny is None:
        return
    deny = set(s.deny)
    noai = ctx.data.noai_domains() if ctx.data is not None else []
    for d in noai:
        lack = [r for r in (f"WebFetch(domain:{d})", f"WebFetch(domain:*.{d})") if r not in deny]
        if lack:
            it = ctx.data.domains.get(d)
            yield Finding(it.file if it else s.file, it.line if it else None, "-",
                          f"AI の利用を断るドメイン「{d}」が {s.file} の deny にない（{joined(lack)} を足す）")
    domains = s.noai_domains()
    known = known_noai(ctx.root)
    if known is not None:
        for d in domains:
            if d not in known:
                yield Finding(NOAI_TOOL, None, "-", f"deny のドメイン「{d}」が KNOWN_NOAI にない（check_noai.py が取得してしまう）",
                              severity=WARNING)
    excludes = lychee_excludes(ctx.root)
    if excludes is not None:
        for d in domains:
            urls = [f"https://{d}/", f"https://sub.{d}/x", f"https://{d.upper()}/"]
            bad = [u for u in urls if not any(_search(p, u) for p in excludes)]
            if bad:
                yield Finding(LINKS_WORKFLOW, None, "-", f"deny のドメイン「{d}」を、外部リンクの検査の --exclude が除かない"
                                                         f"（{bad[0]} を取得する）", severity=WARNING)


def _search(pattern: str, url: str) -> bool:
    try:
        return re.search(pattern, url) is not None
    except re.error:
        return False
