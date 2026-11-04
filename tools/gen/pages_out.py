"""生成するファイル（design §7・§8.2・§8.5）：nav.yml・分野の入口（docs/<field>/index.md）・一覧（docs/lists/）・
llms.txt・サイト用のデータ（docs/assets/data/pages.json と graph.json）。

nav.yml（mkdocs.yml が INHERIT で読む）
  nav           サイトのトップ（docs/index.md）→ 公開するページのある分野（site.yml の fields の順）ごとに、分野の入口、
                chapter のないページ、chapter ごとのページ（ナビゲーションの順。題名は nav_title か title）→ 一覧
  exclude_docs  docs/ にあって公開しないページ（held_back の試作のページ・stage が公開の段階でないページ）。nav にも
                載せない（MkDocs は外したページを nav に載せると 404 のリンクを残す。build-B1.md §2.3）
  extra.ca      テンプレート（overrides/。担当 V）が config.extra.ca で引く表示の言葉・サイト用のデータの置き場所・
                ページごとの期限の日（expires）と機能のバッジ（badges。tracks の最初の確認済みの機能の成熟度と強制力）
分野の入口    公開するページのある分野だけ。chapter ごとの箇条書き（題名・レベル・下書きの印・要約の1文目）と、
              作る層の設定の entrance.extra の節（contest の入口の、コンテストの場面を持つほかの分野のページ）
一覧          作る層の設定の lists.pages のファイルごとに、語彙の値の節（値のあるページがあるものだけ）。検索から外す
llms.txt      1ページ1行（題名・URL・id・型・レベル・段階・確認日・要約）。分野ごとの節
pages.json    公開するページごとの、テンプレートと JS が使う値（期限の日を含む。今日と比べるのはブラウザ）
graph.json    知識マップ：ノードは公開するページ、辺は前提（prerequisite）と症状の振り分け（route）。from → to は読む向き
"""
from __future__ import annotations

from lib.base import as_strings

from .text import dumps, first_sentence, front, json_document, md_text, rel_md, yaml_scalar

NAV_HEAD = ["# tools/gen_site.py が生成する。手で直さない（mkdocs.yml が INHERIT: nav.yml で読む。design §8.4・§8.5）。",
            "# 並び：トップ → 公開するページのある分野（site.yml の fields の順）ごとに、分野の入口・chapter のないページ・",
            "# chapter ごとのページ（front matter の order の順）→ 一覧。exclude_docs は docs/ にあって公開しないページ。"]
PAGES_JSON = "assets/data/pages.json"
GRAPH_JSON = "assets/data/graph.json"


def field_pages(gen, field: str) -> list:
    return [p for p in gen.published if p.field == field]


def fields_with_pages(gen) -> list[str]:
    return [f for f in gen.site.fields if field_pages(gen, f)]


def chapters_of(pages: list) -> list[str]:
    return list(dict.fromkeys(p.chapter for p in pages if p.chapter))


def unpublished_docs(gen) -> list:
    """docs/ にあって公開しないページ（exclude_docs に書くもの）。同じ id の2つ目のページも含む。"""
    pub = {id(p) for p in gen.published}
    docs = gen.atlas.docs
    return [p for p in (docs.pages if docs is not None else []) if p.in_docs and id(p) not in pub]


# ---------------------------------------------------------------- nav.yml


def nav_yml(gen, lists: list[tuple[str, str]]) -> str:
    lines = NAV_HEAD + ["nav:"]
    if (gen.root / "docs" / "index.md").exists():
        lines.append("  - index.md")
    for f in fields_with_pages(gen):
        ps = field_pages(gen, f)
        lines.append(f"  - {yaml_scalar(gen.field_title(f))}:")
        lines.append(f"      - {f}/index.md")
        for p in ps:
            if not p.chapter:
                lines.append(f"      - {yaml_scalar(p.nav_label or p.id)}: {gen.doc_rel(p)}")
        for ch in chapters_of(ps):
            lines.append(f"      - {yaml_scalar(ch)}:")
            lines += [f"          - {yaml_scalar(p.nav_label or p.id)}: {gen.doc_rel(p)}" for p in ps if p.chapter == ch]
    if lists:
        lines.append(f"  - {yaml_scalar(gen.config.text('lists', 'index_title', '一覧'))}:")
        lines.append("      - lists/index.md")
        lines += [f"      - {yaml_scalar(title)}: lists/{file}" for title, file in lists]
    excluded = sorted(f"/{p.rel}" for p in unpublished_docs(gen))
    if excluded:
        lines.append("exclude_docs: |")
        lines += [f"  {x}" for x in excluded]
    lines += extra_lines(gen, lists)
    return "\n".join(lines) + "\n"


def extra_lines(gen, lists: list[tuple[str, str]]) -> list[str]:
    """extra.ca：テンプレートが引く表示の言葉（作る層の設定の labels）と、サイト用のデータと一覧の置き場所。"""
    def mapping(name: str, items: dict[str, str]) -> list[str]:
        if not items:
            return [f"    {name}: {{}}"]
        return [f"    {name}:"] + [f"      {yaml_scalar(k)}: {yaml_scalar(v)}" for k, v in items.items()]

    site = gen.site
    out = ["extra:", "  ca:"]
    out += mapping("fields", {f: gen.field_title(f) for f in site.fields})
    out += mapping("types", {t: gen.config.labels("types").get(t, t) for t in site.types})
    out += mapping("stages", {s: gen.config.labels("stages").get(s, s) for s in site.stages})
    out += mapping("surfaces", {s: gen.config.labels("surfaces").get(s, s) for s in (site.vocab("surfaces") or [])})
    out.append(f"    levels: [{', '.join(yaml_scalar(x) for x in site.levels)}]")
    out.append(f"    published_stages: [{', '.join(yaml_scalar(x) for x in site.published_stages)}]")
    out.append(f"    pages_json: {PAGES_JSON}")
    out.append(f"    graph_json: {GRAPH_JSON}")
    report = gen.config.raw.get("report_template")   # 誤りの報告の Issue のテンプレート（作る層の設定。overrides/main.html が欄に入れて開く）
    if report:
        out.append(f"    report_template: {yaml_scalar(str(report))}")
    keys = {cfg["key"]: f"lists/{cfg['file']}" for cfg in gen.config.list_pages() if (cfg["title"], cfg["file"]) in lists}
    out += mapping("lists", keys)
    # ページごとの、テンプレートが data 属性とバッジに出す値（design §8.5：期限の日は道具が数え、比べるのはブラウザ）。
    # 値のあるページだけ。pages.json と同じ値
    expires = {p.id: gen.expiry_of(p).date.isoformat() for p in gen.published if gen.expiry_of(p).date}
    out += mapping("expires", expires)
    badges = {}
    for p in gen.published:
        b = next((x for x in feature_badges(gen, p) if "maturity" in x or "enforcement" in x), None)
        if b is not None:
            badges[p.id] = "{" + ", ".join(f"{k}: {yaml_scalar(str(b[k]))}" for k in ("maturity", "enforcement") if b.get(k)) + "}"
    if badges:
        out.append("    badges:")
        out += [f"      {yaml_scalar(k)}: {v}" for k, v in badges.items()]
    else:
        out.append("    badges: {}")
    return out


# ---------------------------------------------------------------- 分野の入口と一覧


def page_items(gen, host: str, pages: list, with_field: bool = False) -> str:
    out = []
    for p in pages:
        s = first_sentence(p.summary)
        out.append(f"- {gen.page_link(host, p)}{gen.list_marks(p, with_field)}" + (f"：{md_text(s)}" if s else ""))
    return "\n".join(out)


def entrance(gen, field: str) -> str:
    ps = field_pages(gen, field)
    host = f"{field}/index.md"
    title = gen.field_title(field)
    out = front(title) + f"# {md_text(title)}\n"
    top = [p for p in ps if not p.chapter]
    if top:
        out += "\n" + page_items(gen, host, top) + "\n"
    for ch in chapters_of(ps):
        out += f"\n## {md_text(ch)}\n\n" + page_items(gen, host, [p for p in ps if p.chapter == ch]) + "\n"
    for x in gen.config.entrance_extra():
        if x["field"] != field:
            continue
        key, value = str(x["key"]), str(x["value"])
        others = [p for p in gen.published if p.field != field and value in as_strings(p.raw.get(key))]
        if others:
            out += f"\n## {md_text(str(x.get('title') or value))}\n\n" + page_items(gen, host, others, with_field=True) + "\n"
    return out


def list_anchor(value: str) -> str:
    return "-".join(value.lower().split())


def list_page(gen, cfg: dict) -> str | None:
    """一覧のページ（値のあるページがなければ None）。"""
    host = f"lists/{cfg['file']}"
    values = gen.site.vocab(str(cfg["vocab"]))
    if values is None:
        gen.note(f"tools/gen/config.yml の lists の vocab「{cfg['vocab']}」が site.yml にない（{host} を作らない）")
        return None
    key = str(cfg["key"])
    labels = str(cfg.get("labels") or "")
    body = ""
    for v in values:
        ps = [p for p in gen.published if v in as_strings(p.raw.get(key))]
        if not ps:
            continue
        label = gen.label(labels, v) if labels else v
        body += f"\n## {md_text(label)} {{#{list_anchor(v)}}}\n\n" + page_items(gen, host, ps, with_field=True) + "\n"
    if not body:
        return None
    title = str(cfg.get("title") or cfg["file"])
    return front(title, search_exclude=True) + f"# {md_text(title)}\n" + body


def list_counts(gen, cfg: dict) -> list[tuple[str, int]]:
    key = str(cfg["key"])
    labels = str(cfg.get("labels") or "")
    out = []
    for v in gen.site.vocab(str(cfg["vocab"])) or []:
        n = sum(1 for p in gen.published if v in as_strings(p.raw.get(key)))
        if n:
            out.append((gen.label(labels, v) if labels else v, list_anchor(v), n))
    return out


def lists_index(gen, made: list[dict]) -> str:
    title = gen.config.text("lists", "index_title", "一覧")
    host = "lists/index.md"
    out = front(title, search_exclude=True) + f"# {md_text(title)}\n\n"
    for cfg in made:
        counts = "・".join(f"[{md_text(label)}]({rel_md(host, 'lists/' + cfg['file'])}#{anchor})（{n}）"
                           for label, anchor, n in list_counts(gen, cfg))
        out += f"- [{md_text(cfg.get('title') or cfg['file'])}]({rel_md(host, 'lists/' + cfg['file'])})：{counts}\n"
    return out


# ---------------------------------------------------------------- llms.txt


def page_confirmed(page) -> str:
    """ページの確認日（verified と checked の新しいほう。verified がなければ空。design §9.2）。"""
    v, c = page.text("verified"), page.text("checked")
    if not page.date("verified"):
        return ""
    return max(v, c) if page.date("checked") else v


def llms_txt(gen) -> str:
    info, site = gen.info, gen.site
    stages = site.stages
    out = [f"# {info.name or 'claude-atlas'}", ""]
    if info.description:
        out += [f"> {info.description}", ""]
    notice = gen.config.text("llms", "notice", "")
    if notice:
        out += [notice, ""]
    level_less = "—"
    unverified = gen.text("unverified", "未検証")
    draft = f"（{stages[1]} は{gen.text('draft_band', '下書き・未検証')}）" if len(stages) > 1 else ""
    out += [
        "- 1行が1ページ：「- [題名](URL)（id・型・レベル・段階・確認日）：要約」",
        f"- 型：{'・'.join(site.types)}。レベル（低い順）：{'・'.join(site.levels)}。レベルを持たない型（"
        f"{'・'.join(site.types_without_level)}）は「{level_less}」",
        f"- 段階：{'・'.join(site.published_stages)}{draft}。確認日のないページは「{unverified}」",
        f"- ページ数：{len(gen.published)}",
    ]
    for f in fields_with_pages(gen):
        out += ["", f"## {gen.field_title(f)}", ""]
        for p in field_pages(gen, f):
            url = info.url + p.url
            meta = "・".join([p.id, p.type or "—", gen.level_text(p) or level_less, p.stage, page_confirmed(p) or unverified])
            out.append(f"- [{md_text(gen.title(p))}]({url})（{meta}）：{' '.join(p.summary.split())}")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- サイト用のデータ


def vocab_head(gen) -> dict:
    site, cfg = gen.site, gen.config
    return {
        "fields": [{"id": f, "title": gen.field_title(f)} for f in site.fields],
        "types": [{"id": t, "label": cfg.labels("types").get(t, t)} for t in site.types],
        "levels": site.levels,
        "stages": [{"id": s, "label": cfg.labels("stages").get(s, s)} for s in site.stages],
        "surfaces": [{"id": s, "label": cfg.labels("surfaces").get(s, s)} for s in (site.vocab("surfaces") or [])],
    }


def feature_badges(gen, page) -> list[dict]:
    out = []
    for fid in page.tracks:
        f = gen.feature(fid)
        if f is None:
            continue
        item = {"id": fid, "title": f.text("title"), "status": f.text("status"), "checked": f.text("checked") or None}
        if gen.is_confirmed(f):
            for k in ("maturity", "enforcement", "load_timing", "context_cost", "survives_compaction"):
                if k in f.raw:
                    item[k] = f.raw.get(k)
        out.append(item)
    return out


def pages_json(gen) -> str:
    rows = []
    for p in gen.published:
        exp = gen.expiry_of(p)
        vw = p.raw.get("verified_with")
        rows.append({
            "id": p.id, "url": p.url, "title": gen.title(p), "nav_title": p.text("nav_title") or None,
            "field": p.field, "chapter": p.chapter or None, "type": p.type or None, "level": gen.level_text(p) or None,
            "stage": p.stage, "surfaces": p.surfaces, "principle": p.principle, "volatility": p.volatility or None,
            "summary": " ".join(p.summary.split()), "updated": p.text("updated") or None,
            "verified": p.text("verified") or None, "checked": p.text("checked") or None,
            "confirmed": page_confirmed(p) or None,
            "verified_with": vw if isinstance(vw, dict) else None,
            "expires": exp.date.isoformat() if exp.date else None,
            "expires_by": exp.by.what if exp.by else None,
            "features": feature_badges(gen, p),
        })
    head = {"about": "tools/gen_site.py が生成する（手で直さない）。公開するページだけ。expires は期限の日（design §9.2）で、"
                     "今日と比べるのはブラウザ",
            **vocab_head(gen)}
    return json_document(head, {"pages": rows})


def graph_json(gen) -> str:
    pub = gen.pub_ids
    nodes, edges, seen = [], [], set()
    for p in gen.published:
        pre = [r.target for r in p.prerequisites if r.target in pub and r.target != p.id]
        pre = list(dict.fromkeys(pre))
        routes = []
        for r in p.routes if p.type == gen.symptom_type else []:
            to = list(dict.fromkeys(ref.target for ref in r.to if ref.target in pub and ref.target != p.id))
            if to:
                routes.append({"cause": r.cause, "to": to})
        rel = list(dict.fromkeys(r.target for r in p.related if r.target in pub and r.target != p.id))
        nodes.append({"id": p.id, "title": gen.title(p), "nav_title": p.text("nav_title") or None, "aliases": p.aliases,
                      "url": p.url,
                      "field": p.field, "chapter": p.chapter or None, "type": p.type or None,
                      "level": gen.level_text(p) or None, "stage": p.stage, "summary": " ".join(p.summary.split()),
                      "prerequisites": pre, "routes": routes, "related": rel})
        for t in pre:
            if (t, p.id, "prerequisite") not in seen:
                seen.add((t, p.id, "prerequisite"))
                edges.append({"from": t, "to": p.id, "kind": "prerequisite"})
        for r in routes:
            for t in r["to"]:
                if (p.id, t, "route") not in seen:
                    seen.add((p.id, t, "route"))
                    edges.append({"from": p.id, "to": t, "kind": "route", "cause": r["cause"]})
    head = {"about": "tools/gen_site.py が生成する（手で直さない）。ノードは公開するページ、辺は前提（prerequisite：前提 → "
                     "ページ）と症状の振り分け（route：症状 → 振り分け先）",
            "fields": [{"id": f, "title": gen.field_title(f)} for f in gen.site.fields], "levels": gen.site.levels}
    return json_document(head, {"nodes": nodes, "edges": edges})


__all__ = ["GRAPH_JSON", "PAGES_JSON", "dumps", "entrance", "fields_with_pages", "graph_json", "list_page", "lists_index",
           "llms_txt", "nav_yml", "pages_json", "unpublished_docs"]
