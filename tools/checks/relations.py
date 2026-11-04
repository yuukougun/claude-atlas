"""前提と関連の規則：front matter と目次（catalog）の両方に当てる検査（設計書 §8.3・DR-16）。

tools/check_catalog.py の同じ名前の検査と同じ中身・同じ文（目次のモデルに当てると同じ指摘になる。試験が照らす）。
check_catalog.py は骨格（工程6c）の後に退くので、これらの規則はここが正になる。違うのは次の点だけ：
- 行：front matter はそのキーの行、目次はページの始まりの行（check_catalog.py と同じ）
- 指摘に添える「関わるもの」：check_catalog.py は分野（--field 用）、ここはページの id（check_pages.py --page 用）
- 目次だけにある規則（registry の候補・merged・dropped・chapters・features.yaml・ledger）は check_catalog.py に残す
ページは lib の PageRecord（front matter の Page と目次の CatalogPage に共通の読み方）だけで読む。
"""
from __future__ import annotations

import collections
import unicodedata
from typing import Iterator

from lib.base import Ref, as_strings, as_text
from lib.graph import strongly_connected

from .context import Context, where
from .core import CATALOG, ERROR, FRONT_MATTER, WARNING, Finding, check, joined
from .rules import (FEATURE_TYPE, MAX_PREREQUISITES, MAX_RELATED, MAX_ROUTE_TARGETS, MAX_SUMMARY_SENTENCES,
                    MIN_SYMPTOM_SIGNS, SYMPTOM_PREREQUISITE_TYPES, SYMPTOM_SIGN, SYMPTOM_TYPE)

BOTH = (FRONT_MATTER, CATALOG)


def at(ctx: Context, p, message: str, key: str | None = None, *also: str | None) -> Finding:
    """ページについての指摘。front matter ならそのキーの行、目次ならページの始まりの行。also は関わるほかのページ。"""
    line = p.key_line(key) if key and ctx.target == FRONT_MATTER else p.line
    return Finding(p.file, line, p.label, message, frozenset(x for x in also if x))


def page_refs(p) -> Iterator[tuple[str, Ref]]:
    for key in ("prerequisites", "related"):
        for ref in p.refs(key):
            yield key, ref


def route_label(route: dict, index: int) -> str:
    """routes の1件の呼び名（「routes（縛っていない）」。cause がなければ「routes の N 番目」）。"""
    cause = as_text(route.get("cause"))
    return f"routes（{cause}）" if cause else f"routes の {index + 1} 番目"


def route_refs(p) -> Iterator[tuple[str, Ref]]:
    """routes の to の1件ずつ（呼び名「routes（cause）の to」, 参照）。"""
    for i, route in enumerate(p.parts("routes")):
        label = f"{route_label(route, i)}の to"
        for s in as_strings(route.get("to")):
            yield label, Ref.parse(s)


def key_of(label: str) -> str:
    """呼び名から front matter のキー（行を引くため）。"""
    return "routes" if label.startswith("routes") else label


def prerequisite_targets(p) -> list[str]:
    """前提の指す先のページの id（id#anchor はページの id にする。空と重複を除き、書いた順）。"""
    return list(dict.fromkeys(r.target for r in p.refs("prerequisites") if r.target))


def by_id(ctx: Context) -> dict:
    return ctx.atlas.by_id


# ================================================================ エラー


@check("参照", ERROR, *BOTH)
def check_refs(ctx: Context) -> Iterator[Finding]:
    """prerequisites・related・routes の to が解決しない：存在しない id（目次では merged・dropped にした候補も）、
    related と routes の id#anchor の anchor が相手の sections にない"""
    for p in ctx.pages:
        for key, ref in [*page_refs(p), *route_refs(p)]:
            if not ref.target:
                yield at(ctx, p, f"{key} に空の id がある（{ref.raw!r}）", key_of(key))
                continue
            problem = ctx.bad_target(ref.target)
            if problem:
                yield at(ctx, p, f"{key} の「{ref.raw}」{problem}", key_of(key))
                continue
            q = ctx.page(ref.target)
            if key != "prerequisites" and ref.anchor is not None and q is not None:
                anchors = q.anchors()
                if ref.anchor not in anchors:
                    have = f"あるのは {joined(anchors)}" if anchors else "sections がない"
                    yield at(ctx, p, f"{key} の「{ref.raw}」: {q.id} の sections に anchor「{ref.anchor}」がない（{have}）",
                             key_of(key), q.id)


def cycle_through(graph: dict[str, list[str]], start: str, members: set[str]) -> list[str]:
    """start を通る最短の循環（members の中だけをたどる）。"""
    parent: dict[str, str] = {}
    queue = collections.deque([start])
    seen = {start}
    while queue:
        u = queue.popleft()
        for v in graph.get(u, ()):
            if v == start:
                path = [u]
                while path[-1] != start:
                    path.append(parent[path[-1]])
                return list(reversed(path))
            if v in members and v not in seen:
                seen.add(v)
                parent[v] = u
                queue.append(v)
    return [start]


@check("循環", ERROR, *BOTH)
def check_cycles(ctx: Context) -> Iterator[Finding]:
    """前提（prerequisites）が循環している（自分自身を前提にするものも）"""
    graph = ctx.atlas.prerequisite_graph()
    order = {pid: i for i, pid in enumerate(by_id(ctx))}
    for comp in strongly_connected(graph):
        if len(comp) == 1 and comp[0] not in graph[comp[0]]:
            continue
        start = min(comp, key=order.__getitem__)
        cycle = cycle_through(graph, start, set(comp))
        rest = len(comp) - len(cycle)
        more = f"（ほかに {rest} ページが同じ循環に入る）" if rest > 0 else ""
        p = by_id(ctx)[start]
        yield Finding(p.file, at(ctx, p, "", "prerequisites").line, p.label,
                      "前提が循環している: " + " → ".join(cycle + [start]) + more, frozenset(comp))


@check("前提と関連の重複", ERROR, *BOTH)
def check_overlap(ctx: Context) -> Iterator[Finding]:
    """同じページが prerequisites と related の両方にある。同じ id が同じリストに2回ある"""
    for p in ctx.pages:
        pre = [r.target for r in p.refs("prerequisites")]
        for key, items in (("prerequisites", pre), ("related", [r.raw.strip() for r in p.refs("related")])):
            for x, n in collections.Counter(items).items():
                if x and n > 1:
                    yield at(ctx, p, f"{key} に「{x}」が {n} 回ある", key)
        for t in dict.fromkeys(r.target for r in p.refs("related")):
            if t and t in pre:
                yield at(ctx, p, f"「{t}」が prerequisites と related の両方にある（related から外す）", "related")


@check("routes", ERROR, *BOTH)
def check_routes(ctx: Context) -> Iterator[Finding]:
    """routes（症状のページの、原因ごとの振り分け先）を symptom でないページが持っている。routes の to が空
    （cause の語彙と to の形は front matter では「形」、目次では check_catalog.py の「語彙」「必須」が出す）"""
    types = ctx.rules.types
    for p in ctx.pages:
        if p.raw.get("routes") is None:
            continue
        t = p.text("type")
        if t != SYMPTOM_TYPE and types is not None and t in types:   # type がない・語彙にないときは、ほかのエラーが出る
            yield at(ctx, p, f"routes は type が {SYMPTOM_TYPE} のページだけが持つ（このページは {t}。ほかのページへの道は "
                             "related に書く）", "routes")
        for i, route in enumerate(p.parts("routes")):
            if route.get("to") == []:
                yield at(ctx, p, f"{route_label(route, i)}の to が空（振り分け先のページを1件以上書く）", "routes")


@check("id の重複", ERROR, *BOTH)
def check_duplicates(ctx: Context) -> Iterator[Finding]:
    """同じ id のページが2つ以上ある（front matter では docs/ と stubs/ の両方・二つの分野など）。ページの中の sections
    の anchor が重なっている（目次の registry・merged・dropped の重なりは check_catalog.py が見る）"""
    first: dict[str, object] = {}
    for p in ctx.pages:
        if p.id is None:
            continue
        q = first.setdefault(p.id, p)
        if q is not p:
            yield at(ctx, p, f"id「{p.id}」が {where(q)} にもある", "id")
    for p in ctx.pages:
        anchors = collections.Counter(p.anchors())
        for a, n in anchors.items():
            if n > 1:
                yield at(ctx, p, f"sections の anchor「{a}」が {n} つある", "sections")


# ================================================================ 警告


@check("参照の書き方", WARNING, *BOTH)
def check_ref_style(ctx: Context) -> Iterator[Finding]:
    """prerequisites に id#anchor がある（前提はページの id で書く。節を指すのは related）。related に自分自身がある"""
    for p in ctx.pages:
        for ref in p.refs("prerequisites"):
            if ref.anchor is not None:
                yield at(ctx, p, f"prerequisites の「{ref.raw}」に #anchor がある（前提はページの id で書く）", "prerequisites")
        for ref in p.refs("related"):
            if p.id is not None and ref.target == p.id:
                yield at(ctx, p, f"related に自分自身「{ref.raw}」がある", "related")


@check("レベルの逆転", WARNING, *BOTH)
def check_level_inversion(ctx: Context) -> Iterator[Finding]:
    """前提のページの level が、そのページの level より上の段（site.yml の levels の順）。routes の先は見ない
    （上の段の対処も振り分け先に置ける。catalog/README §4.4 の6）"""
    rank = ctx.rules.level_rank
    for p in ctx.pages:
        lv = p.text("level")
        if lv not in rank:
            continue
        for ref in p.refs("prerequisites"):
            q = ctx.page(ref.target)
            if q is None:
                continue
            ql = q.text("level")
            if ql in rank and rank[ql] > rank[lv]:
                yield at(ctx, p, f"前提「{q.id}」の level（{ql}）がこのページ（{lv}）より上の段", "prerequisites", q.id)


@check("必須の前提", WARNING, *BOTH)
def check_required_prerequisites(ctx: Context) -> Iterator[Finding]:
    """必須（site.yml の priorities の最初）のページの前提が必須でない。routes の先は見ない（推奨の対処も振り分け先に
    置ける）"""
    r = ctx.rules
    top = r.top_priority
    if top is None:
        return
    for p in ctx.pages:
        if p.text("priority") != top:
            continue
        for ref in p.refs("prerequisites"):
            q = ctx.page(ref.target)
            qp = q.text("priority") if q is not None else ""
            if qp and qp != top and qp in (r.priorities or []):
                yield at(ctx, p, f"前提「{q.id}」の priority が {qp}（{top}のページの前提は{top}にする）", "prerequisites", q.id)


def reached_from(graph: dict[str, list[str]], start: str, avoid: str | None = None) -> dict[str, str | None]:
    """start から前提をたどって届く id → その道でひとつ手前の id（start 自身は None）。幅優先なので最短の道になる。
    avoid は通らず、届いたことにもしない。一度見た id は二度たどらないので、循環があっても止まる。"""
    parent: dict[str, str | None] = {start: None}
    queue = collections.deque([start])
    while queue:
        u = queue.popleft()
        for v in graph.get(u, ()):
            if v != avoid and v not in parent:
                parent[v] = u
                queue.append(v)
    return parent


def path_to(parent: dict[str, str | None], end: str) -> list[str]:
    path = [end]
    while parent[path[-1]] is not None:
        path.append(parent[path[-1]])
    return path[::-1]


@check("推移的な前提", WARNING, *BOTH)
def check_transitive_prerequisites(ctx: Context) -> Iterator[Finding]:
    """prerequisites に、同じページのほかの前提から前提をたどって届くものがある（catalog/README §4.4 の1「推移的に
    届くものは書かない」）。どの前提から届くかを道筋で出す。id#anchor はページの id で比べ、そのページ自身を通る道は
    数えない

    たどるのはページの prerequisites だけ。目次でファイルのまだない分野の候補などは、ほかのページの前提に書いてあれば
    届いたことにするが、その先はたどらない。前提が循環していても止まる（循環そのものは「循環」のエラーが出す）。"""
    graph = {pid: prerequisite_targets(p) for pid, p in by_id(ctx).items()}
    for p in ctx.pages:
        pre = [t for t in prerequisite_targets(p) if t != p.id]
        if len(pre) < 2:
            continue
        reach = {y: reached_from(graph, y, avoid=p.id) for y in pre}
        for x in pre:
            via = [y for y in pre if y != x and x in reach[y]]
            if via:
                paths = "、".join(" → ".join(path_to(reach[y], x)) for y in via)
                yield at(ctx, p, f"前提「{x}」は、ほかの前提「{'」「'.join(via)}」からたどって届く: {paths}"
                                 "（推移的に届く前提は書かない。要るなら related に移す）", "prerequisites")


@check("比例則", WARNING, *BOTH)
def check_proportional(ctx: Context) -> Iterator[Finding]:
    """site.yml の proportional_rule の levels（任せる・仕組みにする・回す）のページが、guard_fields（verify・eval・
    enforce・safety）の分野のページを前提にも関連にも持たない（症状のページは routes の先も数える。guard_fields の
    分野のページは除く）。任せる幅を広げる内容のページだけが対象なので、そうでないページは理由を残して置いてよい"""
    r = ctx.rules
    levels, guards = set(r.proportional_levels), set(r.guard_fields)
    if not levels or not guards:
        return
    for p in ctx.pages:
        lv = p.text("level")
        if lv not in levels or p.field in guards:
            continue
        symptom = p.text("type") == SYMPTOM_TYPE
        refs = [*page_refs(p), *(route_refs(p) if symptom else ())]
        targets = {ctx.target_field(ref.target) for _, ref in refs if ref.target}
        if not targets & guards:
            place = "前提にも関連にも routes にも" if symptom else "前提にも関連にも"
            yield at(ctx, p, f"level が {lv} だが、{joined(r.guard_fields)} の分野のページを{place}持たない"
                             "（任せる幅を広げる内容なら足す）", "level")


@check("入ってくる道", WARNING, *BOTH)
def check_incoming(ctx: Context) -> Iterator[Finding]:
    """どのページの prerequisites・related・routes にも出てこない（入ってくる道がない）。入口の分野（site.yml の
    entry_fields。なければ fields の最初の start）は除く。症状のページの routes の先は、診断の節から道があるので数える"""
    incoming: set[str] = set()
    for p in ctx.pages:
        for _, ref in [*page_refs(p), *route_refs(p)]:
            q = ctx.page(ref.target) if ref.target else None
            if q is not None and q.id != p.id:
                incoming.add(q.id)
    absent = ctx.absent_fields()
    later = f"。まだファイルのない {len(absent)} 分野からの参照は数えていない" if absent else ""
    for pid, p in by_id(ctx).items():
        if p.field not in ctx.rules.entry_fields and pid not in incoming:
            yield at(ctx, p, f"どのページの prerequisites・related・routes にも出てこない（入ってくる道がない{later}）")


def count_sentences(s: str) -> int:
    """かっこの外の「。」で文を数える（最後の「。」の後に文字が残れば、それも1文）。"""
    depth, n, tail = 0, 0, False
    for ch in s:
        if ch in "（(「『":
            depth += 1
        elif ch in "）)」』":
            depth = max(0, depth - 1)
        if ch == "。" and depth == 0:
            n += 1
            tail = False
        elif not ch.isspace():
            tail = True
    return n + (1 if tail else 0)


@check("summary", WARNING, *BOTH)
def check_summary(ctx: Context) -> Iterator[Finding]:
    """summary が site.yml の summary_max_chars より長い、3文以上ある、site.yml の summary_banned_words の語を使っている"""
    r = ctx.rules
    for p in ctx.pages:
        s = p.text("summary")
        if not s:
            continue
        if r.summary_max_chars is not None and len(s) > r.summary_max_chars:
            yield at(ctx, p, f"summary が {len(s)} 字（{r.summary_max_chars} 字まで）", "summary")
        n = count_sentences(s)
        if n > MAX_SUMMARY_SENTENCES:
            yield at(ctx, p, f"summary が {n} 文（{MAX_SUMMARY_SENTENCES} 文まで）", "summary")
        bad = [w for w in r.summary_banned_words if w in s]
        if bad:
            yield at(ctx, p, f"summary に使わない語がある: 「{'」「'.join(bad)}」", "summary")


@check("症状の signs", WARNING, *BOTH)
def check_symptom_signs(ctx: Context) -> Iterator[Finding]:
    """symptom のページの signs に、type が symptom のサインが2つ以上ない"""
    for p in ctx.pages:
        if p.text("type") != SYMPTOM_TYPE:
            continue
        n = sum(1 for s in p.parts("signs") if s.get("type") == SYMPTOM_SIGN)
        if n < MIN_SYMPTOM_SIGNS:
            yield at(ctx, p, f"signs のうち type が {SYMPTOM_SIGN} のものが {n} つ（{MIN_SYMPTOM_SIGNS} つ以上にする）", "signs")


def sign_key(text: str) -> str:
    """signs の文を比べる形：NFKC で全角と半角をそろえ、空白と記号（Unicode の分類の P・S・Z・C）を除く。"""
    return "".join(ch for ch in unicodedata.normalize("NFKC", text) if unicodedata.category(ch)[0] not in "PSZC")


@check("逆引きの重複", WARNING, *BOTH)
def check_reverse_index_overlap(ctx: Context) -> Iterator[Finding]:
    """症状（symptom）のページの signs の文と、空白と記号を除いて同じ文が、ほかのページの signs にある（catalog/README
    §4.5 の4。逆引きで同じ困りごとが二か所に出る）。ほかのページの側に、どの症状のページのどの文と同じかを出す

    signs の type は問わない。症状のページでないページどうしの同じ文は指摘しない（逆引きで並べるために、そろえて
    よい）。症状のページどうしで同じ文があれば、両方のページに出す。"""
    owners: dict[str, list[tuple[object, str]]] = collections.defaultdict(list)
    for s in ctx.pages:
        if s.text("type") != SYMPTOM_TYPE:
            continue
        for sign in s.parts("signs"):
            text = as_text(sign.get("text"))
            key = sign_key(text)
            if key and all(q is not s for q, _ in owners[key]):
                owners[key].append((s, text))
    for p in ctx.pages:
        for sign in p.parts("signs"):
            text = as_text(sign.get("text"))
            key = sign_key(text)
            hits = [(s, t) for s, t in owners.get(key, ()) if s is not p] if key else []
            if not hits:
                continue
            relation = "と同じ" if all(t == text for _, t in hits) else "と、空白と記号を除くと同じ"
            if p.text("type") == SYMPTOM_TYPE:
                hint = "症状のページどうしで重なっている。どちらの症状のページで受けるかを決める"
            else:
                hint = "逆引きで同じ困りごとが二か所に出る。対処のページには、より狭い場面の困りごとか、やりたいことの形で置く"
            hit_text = "、".join(f"{s.label} の sign「{t}」" for s, t in hits)
            yield at(ctx, p, f"signs の「{text}」が、症状のページ {hit_text}{relation}（{hint}）", "signs",
                     *(s.id for s, _ in hits))


@check("症状の prevents", WARNING, *BOTH)
def check_symptom_prevents(ctx: Context) -> Iterator[Finding]:
    """symptom のページの prevents が空"""
    for p in ctx.pages:
        if p.text("type") == SYMPTOM_TYPE and not p.strings("prevents"):
            yield at(ctx, p, f"{SYMPTOM_TYPE} のページの prevents が空（防ぐ・診断する原因を1つ以上書く）", "prevents")


@check("症状の前提", WARNING, *BOTH)
def check_symptom_prerequisites(ctx: Context) -> Iterator[Finding]:
    """symptom のページの前提の type が concept・guide・hub でない（症状のページの前提は、診断を読むのに要る概念の
    ページだけにする。対処のページは routes に置く。catalog/README §4.4 の6）

    見るのは解決した前提のページだけ。type がない・語彙にない前提は、そのページのエラーが出るので見ない。"""
    types = ctx.rules.types
    allowed = joined(SYMPTOM_PREREQUISITE_TYPES)
    for p in ctx.pages:
        if p.text("type") != SYMPTOM_TYPE:
            continue
        for t in prerequisite_targets(p):
            q = ctx.page(t)
            qt = q.text("type") if q is not None else ""
            if qt and qt not in SYMPTOM_PREREQUISITE_TYPES and (types is None or qt in types):
                yield at(ctx, p, f"前提「{t}」の type が {qt}（症状のページの前提は、診断を読むのに要る {allowed} のページだけに"
                                 "する。対処のページは routes に置く）", "prerequisites", t)


@check("症状の routes", WARNING, *BOTH)
def check_symptom_routes(ctx: Context) -> Iterator[Finding]:
    """symptom のページに routes（原因ごとの振り分け先）がない"""
    for p in ctx.pages:
        if p.text("type") == SYMPTOM_TYPE and not p.parts("routes"):
            yield at(ctx, p, f"{SYMPTOM_TYPE} のページに routes がない（原因ごとに、中心の対処のページを1〜{MAX_ROUTE_TARGETS} 件、"
                             "近い順に書く）", "routes")


@check("routes と原因", WARNING, *BOTH)
def check_route_causes(ctx: Context) -> Iterator[Finding]:
    """routes の cause が、そのページの prevents・pitfalls にない。そのページの prevents・pitfalls の原因に routes がない
    （routes と prevents の両方を書いた symptom のページだけを見る）

    語彙にない cause は「語彙」か「形」のエラーが出るので見ない（site.yml の prevents か pitfalls が読めなければ、
    この検査をしない）。対処のページがない原因は、理由を残して置いてよい。"""
    causes = ctx.rules.causes
    if causes is None:
        return
    for p in ctx.pages:
        routes = p.parts("routes")
        prevents, pitfalls = p.strings("prevents"), p.strings("pitfalls")
        if p.text("type") != SYMPTOM_TYPE or not routes or not prevents:
            continue
        routed = list(dict.fromkeys(c for c in (as_text(r.get("cause")) for r in routes) if c in causes))
        for c in routed:
            if c not in prevents and c not in pitfalls:
                yield at(ctx, p, f"routes の cause「{c}」が、このページの prevents・pitfalls にない（診断で問う原因に足すか、"
                                 "routes から外す）", "routes")
        for key, values in (("prevents", prevents), ("pitfalls", pitfalls)):
            for c in dict.fromkeys(values):
                if c not in routed and c in causes:
                    yield at(ctx, p, f"{key} の「{c}」に routes がない（その原因の中心の対処を routes に書く。対処のページが"
                                     "ない原因なら、notes に書く）", key)


@check("routes の重なり", WARNING, *BOTH)
def check_route_overlap(ctx: Context) -> Iterator[Finding]:
    """routes に同じ cause が2回ある。1つの cause の to に同じ id が2回ある。routes の先のページが、同じページの
    prerequisites か related にもある（ページの id で比べる。related には routes にない近いページだけを置く）"""
    for p in ctx.pages:
        routes = p.parts("routes")
        if not routes:
            continue
        for c, n in collections.Counter(as_text(r.get("cause")) for r in routes).items():
            if c and n > 1:
                yield at(ctx, p, f"routes の cause「{c}」が {n} 回ある（1つにまとめる）", "routes")
        for i, route in enumerate(routes):
            for x, n in collections.Counter(s.strip() for s in as_strings(route.get("to"))).items():
                if x and n > 1:
                    yield at(ctx, p, f"{route_label(route, i)}の to に「{x}」が {n} 回ある", "routes")
        pre = set(prerequisite_targets(p))
        rel = {r.target for r in p.refs("related") if r.target}
        for t in dict.fromkeys(ref.target for _, ref in route_refs(p) if ref.target):
            if t in pre:
                yield at(ctx, p, f"routes の先「{t}」が prerequisites にもある（どちらか一方にする。前提は、診断を読むのに要る概念の"
                                 "ページだけ）", "routes")
            if t in rel:
                yield at(ctx, p, f"routes の先「{t}」が related にもある（related から外す。related には、routes にない近いページ"
                                 "だけを置く）", "routes")


@check("routes の数", WARNING, *BOTH)
def check_route_counts(ctx: Context) -> Iterator[Finding]:
    """routes の1つの cause の to が4件以上（原因ごとに、中心の対処を3件まで）"""
    for p in ctx.pages:
        for i, route in enumerate(p.parts("routes")):
            n = len(as_strings(route.get("to")))
            if n > MAX_ROUTE_TARGETS:
                yield at(ctx, p, f"{route_label(route, i)}の to が {n} 件（中心の対処を {MAX_ROUTE_TARGETS} 件までにする。"
                                 "ほかは related に置く）", "routes")


@check("機能の tracks", WARNING, *BOTH)
def check_feature_tracks(ctx: Context) -> Iterator[Finding]:
    """feature のページの tracks が空"""
    where_ids = "README §5 の機能の id" if ctx.target == CATALOG else "data/facts.yml の features の id"
    for p in ctx.pages:
        if p.text("type") == FEATURE_TYPE and not p.strings("tracks"):
            yield at(ctx, p, f"{FEATURE_TYPE} のページの tracks が空（{where_ids} を書く）", "tracks")


@check("前提と関連の数", WARNING, *BOTH)
def check_counts(ctx: Context) -> Iterator[Finding]:
    """prerequisites が5つ以上（直接の前提だけを4つまで）。related が21件以上（20件まで）"""
    for p in ctx.pages:
        n = len(dict.fromkeys(r.target for r in p.refs("prerequisites")))
        if n > MAX_PREREQUISITES:
            yield at(ctx, p, f"prerequisites が {n} 個（直接の前提だけを {MAX_PREREQUISITES} つまで）", "prerequisites")
        m = len(p.refs("related"))
        if m > MAX_RELATED:
            yield at(ctx, p, f"related が {m} 件（{MAX_RELATED} 件まで）", "related")


@check("id の分野名", WARNING, *BOTH)
def check_field_prefix(ctx: Context) -> Iterator[Finding]:
    """ページの id が、自分の分野の名前で始まる（catalog/README §2「分野の名前を頭に付けない」。ほかの分野の名前で
    始まる id は見ない）"""
    for p in ctx.pages:
        pid, f = p.id, p.field
        if pid and f and (pid == f or pid.startswith(f + "-")):
            yield at(ctx, p, f"id「{pid}」が分野の名前「{f}」で始まる（分野の名前を頭に付けない）", "id")


@check("level の付け方", WARNING, *BOTH)
def check_level_usage(ctx: Context) -> Iterator[Finding]:
    """level を持たない型（site.yml の types_without_level）や分野（fields_without_level）のページに level がある。
    sections の level がページの level より下の段"""
    r = ctx.rules
    rank = r.level_rank
    for p in ctx.pages:
        t, lv = p.text("type"), p.text("level")
        if lv and (t in r.types_without_level or p.field in r.fields_without_level):
            why = f"type が {t} の" if t in r.types_without_level else f"{p.field} の分野の"
            yield at(ctx, p, f"{why}ページは level を書かない（いまは {lv}）", "level")
        if lv in rank:
            for sec in p.parts("sections"):
                s = sec.get("level")
                if isinstance(s, str) and s in rank and rank[s] < rank[lv]:
                    yield at(ctx, p, f"sections の「{as_text(sec.get('title'))}」の level（{s}）がページ（{lv}）より下の段",
                             "sections")


@check("wave", WARNING, *BOTH)
def check_wave(ctx: Context) -> Iterator[Finding]:
    """第一波の核の分野（site.yml の first_wave_core_fields）でないページに wave: 1 がある。核の分野に wave: 1 の
    ページがない。入口の分野（entry_fields）のページと症状（symptom）のページに wave: 1 がない（核の分野のものは
    全ページに付ける。catalog/README §4.6 の2）"""
    core = ctx.rules.first_wave_core_fields
    if not core:
        return
    for p in ctx.pages:
        if p.is_wave and p.field not in core:
            yield at(ctx, p, f"wave: 1 は第一波の核の分野（{joined(core)}）のページにだけ付ける", "wave")
        elif (not p.is_wave and p.field in core
              and (p.field in ctx.rules.entry_fields or p.text("type") == SYMPTOM_TYPE)):
            yield at(ctx, p, "wave: 1 がない（入口の分野のページと症状のページは、全ページに付ける）")
    for f in core:
        pages = [p for p in ctx.pages if p.field == f]
        if pages and not any(p.is_wave for p in pages):
            yield Finding(ctx.field_file(f), None, "-", "第一波の核の分野なのに wave: 1 のページがない（総論と、多くのページが"
                                                         "前提にするページに付ける）")


PLAIN_MARKS = ("`", "**", "](", "<", "$", "{#")


@check("平文の欄", WARNING, *BOTH)
def check_plain_fields(ctx: Context) -> Iterator[Finding]:
    """平文の欄（title・nav_title・aliases・summary・signs の text・sections の title）に Markdown や HTML の記法
    （` ** ]( < $ {#）がある（キーの台帳の「平文」。一覧・索引・検索・llms.txt に記法のまま出る）"""
    for p in ctx.pages:
        values: list[tuple[str, str]] = [(k, p.text(k)) for k in ("title", "nav_title", "summary")]
        values += [("aliases", a) for a in p.strings("aliases")]
        values += [("signs", as_text(s.get("text"))) for s in p.parts("signs")]
        values += [("sections", as_text(s.get("title"))) for s in p.parts("sections")]
        for key, text in values:
            marks = [m for m in PLAIN_MARKS if m in text]
            if marks:
                yield at(ctx, p, f"{key} の「{text}」に記法（{' '.join(marks)}）がある（平文で書く）", key)
