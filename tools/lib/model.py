"""ページのモデルの全体（Atlas）：site.yml・ページ（front matter か目次）・data を合わせ、参照の解決・前提のグラフ・
公開・期限の日を引けるようにする。作る層と検査の層はこれを読む。

  load_atlas(root)          site.yml・docs/ と stubs/ の front matter・data/ を読む（骨格の後の正本。design §5.2 の5）
  load_catalog_atlas(root)  site.yml・planning/catalog/ を、同じモデルで読む（目次に同じ規則を当てるとき）

公開（design §8.4）：docs/ にあり（stubs/ の骨格のページは MkDocs のビルドに入らない。2026-11-04 のメインの決定）、
stage が site.yml の published_stages（なければ stub のほか）で、held_back（公開から外した試作のページ。波が来るまで）
にないページ。置き場所と stage の食い違い（stubs/ に draft、docs/ に stub）は検査の層が見る。
同じ id のページが二つ以上（docs/ と stubs/ の両方など）あれば duplicates に入れ、by_id は先に読んだほう（docs/）を引く。
期限の日（design §9.2）：「ページの確認日＋ページの期限」と「各数値の確認日＋数値の期限」のうち早いもの。ページの
確認日は verified と checked の新しいほうで、verified のないページ（draft など）は数値の分だけで数える。数値は、本文の
fact の目印が指す data の facts と、tracks が指す features（機能の属性のバッジに出るもの）。数値の期限は項目の
volatility（なければ site.yml の default_fact_volatility）。
"""
from __future__ import annotations

import datetime
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from .base import PageRecord, Problem, Ref
from .catalog import Catalog, load_catalog
from .data import Data, load_data
from .graph import topological_order
from .pages import PAGE_DIRS, Docs, load_docs
from .site import Site, load_site


@dataclass(frozen=True)
class Due:
    """期限の日の1つの元。"""

    date: datetime.date               # 期限の日
    what: str                         # page・fact:<id>・feature:<id>
    checked: datetime.date            # 確認日
    volatility: str
    days: int


@dataclass(frozen=True)
class Expiry:
    dues: tuple[Due, ...]             # 期限の元（早い順）
    missing: tuple[str, ...] = ()     # 数えられなかったもの（data にない id、確認日や volatility の読めない項目）

    @property
    def date(self) -> datetime.date | None:
        return self.dues[0].date if self.dues else None

    @property
    def by(self) -> Due | None:
        """いちばん早い期限の元。"""
        return self.dues[0] if self.dues else None

    def expired(self, today: datetime.date) -> bool:
        return self.date is not None and self.date < today


class Atlas:
    """ページのモデルの全体。pages は front matter の pages.Page か、目次の catalog.CatalogPage。"""

    def __init__(self, site: Site, pages: Sequence[PageRecord], data: Data | None = None,
                 held_back: Iterable[str] = (), docs: Docs | None = None, catalog: Catalog | None = None):
        self.site = site
        self.pages = list(pages)
        self.data = data
        self.held_back = set(held_back)
        self.docs = docs
        self.catalog = catalog
        self.by_id: dict[str, PageRecord] = {}
        self.duplicates: dict[str, list[PageRecord]] = {}
        for p in self.pages:
            pid = p.id
            if pid is None:
                continue
            if pid in self.by_id:
                self.duplicates.setdefault(pid, [self.by_id[pid]]).append(p)
            else:
                self.by_id[pid] = p

    # ---- 引く

    def page(self, pid: str) -> PageRecord | None:
        return self.by_id.get(pid)

    def resolve(self, ref: Ref | str) -> PageRecord | None:
        """参照（id か id#anchor）の相手のページ（なければ None。anchor は見ない）。"""
        target = Ref.parse(ref).target if isinstance(ref, str) else ref.target
        return self.by_id.get(target)

    def anchor_ok(self, ref: Ref | str) -> bool | None:
        """id#anchor の anchor が相手の sections にあるか（相手がない・anchor がないときは None）。"""
        ref = Ref.parse(ref) if isinstance(ref, str) else ref
        page = self.resolve(ref)
        if page is None or ref.anchor is None:
            return None
        return ref.anchor in page.anchors()

    def problems(self) -> list[Problem]:
        """読む層の指摘の全部（site.yml・docs か目次・data）。"""
        out = list(self.site.problems)
        if self.docs is not None:
            out += self.docs.all_problems()
        if self.catalog is not None:
            out += self.catalog.problems
        if self.data is not None:
            out += self.data.problems
        return out

    # ---- 並べる

    def ordered(self) -> list[PageRecord]:
        """ナビゲーションの順：site.yml の fields の順、分野の中は front matter の order（目次は pages の並び）、id。"""
        rank = {f: i for i, f in enumerate(self.site.fields)}

        def key(p: PageRecord):
            order = p.raw.get("order")
            pos = getattr(p, "index", None)
            n = order if isinstance(order, int) and not isinstance(order, bool) else pos if pos is not None else 10 ** 9
            return (rank.get(p.field, len(rank)), n, p.id or "")
        return sorted(self.pages, key=key)

    def prerequisite_graph(self) -> dict[str, list[str]]:
        """前提のグラフ（ページの id → 前提のページの id。解決したものだけ、重ねない）。"""
        return {pid: list(dict.fromkeys(r.target for r in p.prerequisites if r.target in self.by_id))
                for pid, p in self.by_id.items()}

    def route_graph(self) -> dict[str, list[str]]:
        """症状のページの routes の先（ページの id → 先のページの id。解決したものだけ）。知識マップの辺に使う。"""
        return {pid: list(dict.fromkeys(r.target for r in p.route_targets() if r.target in self.by_id))
                for pid, p in self.by_id.items() if p.parts("routes")}

    def prerequisite_order(self) -> list[str]:
        """前提が先に来る並び（同じ段ではナビゲーションの順）。"""
        return topological_order(self.prerequisite_graph(), [p.id for p in self.ordered() if p.id in self.by_id])

    # ---- 公開と期限

    def is_published(self, page: PageRecord) -> bool:
        """公開するか：docs/ にあり、stage が公開する段階で、held_back にない（目次のページは stage がないので False）。"""
        in_docs = getattr(page, "in_docs", True)
        return in_docs and page.stage in self.site.published_stages and page.id not in self.held_back

    def published(self) -> list[PageRecord]:
        return [p for p in self.pages if self.is_published(p)]

    def fact_ids(self, page: PageRecord) -> list[str]:
        """ページの本文が fact の目印で使う数値の id（目次のページは空）。"""
        f = getattr(page, "fact_ids", None)
        return f() if callable(f) else []

    def expiry(self, page: PageRecord, extra_facts: Iterable[str] = ()) -> Expiry:
        """期限の日（design §9.2）。extra_facts は、目印のほかに作る層がページに書く数値の id（比較表など）。"""
        days = self.site.volatility_days
        default = self.site.default_fact_volatility
        dues: list[Due] = []
        missing: list[str] = []
        verified = page.date("verified")
        if verified is not None:
            checked = page.date("checked")
            base = max(verified, checked) if checked else verified
            vol = page.volatility
            if vol in days:
                dues.append(Due(base + datetime.timedelta(days=days[vol]), "page", base, vol, days[vol]))
            else:
                missing.append("page")
        items = []
        if self.data is not None:
            facts, features = self.data.facts, self.data.features
            items += [(f"fact:{x}", facts.get(x)) for x in dict.fromkeys([*self.fact_ids(page), *extra_facts])]
            items += [(f"feature:{x}", features.get(x)) for x in dict.fromkeys(page.tracks)]
        for what, item in items:
            checked = item.checked if item is not None else None
            vol = (item.volatility or default) if item is not None else None
            if checked is None or vol not in days:
                missing.append(what)
                continue
            dues.append(Due(checked + datetime.timedelta(days=days[vol]), what, checked, vol, days[vol]))
        dues.sort(key=lambda d: (d.date, d.what))
        return Expiry(tuple(dues), tuple(missing))


def load_atlas(root: Path, held_back: Iterable[str] = (), dirs: Iterable[str] = PAGE_DIRS) -> Atlas:
    """site.yml・ページ（dirs の置き場所。既定は docs/ と stubs/）・data/ を読む。site.yml が読めなければ Fatal。"""
    root = Path(root)
    site = load_site(root)
    docs = load_docs(root, site, dirs)
    return Atlas(site, docs.pages, load_data(root), held_back, docs=docs)


def load_catalog_atlas(root: Path, with_data: bool = False) -> Atlas:
    """site.yml と目次を読む（data/ は with_data のときだけ）。"""
    root = Path(root)
    site = load_site(root)
    catalog = load_catalog(root, site)
    return Atlas(site, catalog.pages, load_data(root) if with_data else None, catalog=catalog)


__all__ = ["Atlas", "Due", "Expiry", "load_atlas", "load_catalog_atlas"]
