"""検査に渡すもの（Context）と、その読み方（load_context）。

  load_context(root)                     front matter（docs/ と stubs/ のページ・data/・nav.yml・.claude/settings.json）
  load_context(root, CATALOG)            目次（planning/catalog/）。前提と関連の規則を当てるとき（骨格まで）

公開しないページ（Atlas の held_back）は、nav.yml の exclude_docs に当たる docs/ のページ（公開から外した試作のページ）。
目次のモデルの参照の解決は tools/check_catalog.py と同じにする：まとめた（merged）・採らない（dropped）候補を指すのは
誤り、分野のファイルにまだない registry の候補は指摘しない（その分野が書かれてから確かめる）。
"""
from __future__ import annotations

import datetime
import functools
from dataclasses import dataclass, field
from pathlib import Path

from lib import Atlas, Catalog, PageRecord, Problem, Site, load_catalog, load_data, load_docs, load_site
from lib.catalog import CATALOG_DIR
from lib.schema import SchemaError, Validator, load_validator

from .config import Nav, Settings, load_nav, load_settings
from .core import CATALOG, FRONT_MATTER, TEMPLATES
from .rules import Rules

SCHEMA_DIR = "schema"


def where(x) -> str:
    return f"{x.file}:{x.line}" if getattr(x, "line", None) else x.file


@dataclass
class Context:
    root: Path
    target: str
    site: Site
    atlas: Atlas
    rules: Rules
    today: datetime.date
    nav: Nav | None = None
    settings: Settings | None = None
    problems: list[Problem] = field(default_factory=list)   # 読む層の指摘（atlas・nav・settings）
    _catalog: Catalog | None = None
    _catalog_read: bool = False
    _validators: dict = field(default_factory=dict)

    # ---- 読む

    @property
    def pages(self) -> list[PageRecord]:
        return self.atlas.pages

    @property
    def data(self):
        return self.atlas.data

    @property
    def catalog(self) -> Catalog | None:
        """目次（目次のモデルなら atlas の目次。front matter のときは要るときに読む。なければ None）。"""
        if self.atlas.catalog is not None:
            return self.atlas.catalog
        if not self._catalog_read:
            self._catalog_read = True
            if (self.root / CATALOG_DIR).is_dir():
                self._catalog = load_catalog(self.root, self.site)
        return self._catalog

    def validator(self, name: str) -> tuple[Validator | None, str | None]:
        """schema/<name>.schema.json の検査器（読めなければ None と理由）。"""
        if name not in self._validators:
            path = self.root / SCHEMA_DIR / f"{name}.schema.json"
            if not path.exists():
                self._validators[name] = (None, f"{SCHEMA_DIR}/{name}.schema.json がない（uv run python tools/make_schema.py で作る）")
            else:
                try:
                    self._validators[name] = (load_validator(path), None)
                except SchemaError as e:
                    self._validators[name] = (None, f"{SCHEMA_DIR}/{name}.schema.json が読めない: {e}")
        return self._validators[name]

    # ---- 参照の解決（目次と front matter で同じ検査の関数が使う）

    def page(self, target: str) -> PageRecord | None:
        return self.atlas.by_id.get(target)

    @functools.cached_property
    def _catalog_index(self) -> dict:
        """目次のモデルの、まとめた・採らない・registry の候補（id → Entry）。front matter のときは空。"""
        out: dict = {"merged": {}, "dropped": {}, "candidates": {}}
        if self.target != CATALOG or self.atlas.catalog is None:
            return out
        cat = self.atlas.catalog
        for ff in cat.files.values():
            for e in ff.merged:
                if e.id is not None:
                    out["merged"].setdefault(e.id, e)
            for e in ff.dropped:
                if e.id is not None:
                    out["dropped"].setdefault(e.id, e)
        for e in cat.registry.candidates:
            if e.id is not None:
                out["candidates"].setdefault(e.id, e)
        return out

    def bad_target(self, target: str) -> str | None:
        """解決しない参照の説明（解決するか、まだ確かめられないなら None）。文は check_catalog.py と同じ。"""
        if target in self.atlas.by_id:
            return None
        if self.target == CATALOG:
            idx = self._catalog_index
            if target in idx["merged"]:
                e = idx["merged"][target]
                return f"は {where(e)} で「{e.text('into')}」にまとめた（まとめた先を指す）"
            if target in idx["dropped"]:
                return f"は {where(idx['dropped'][target])} で採らないことにした（dropped）"
            if target in idx["candidates"]:
                return None
            return "が存在しない id（どの分野のページにも、registry の候補にもない）"
        return "が存在しない id（docs/ にも stubs/ にもページがない）"

    def target_field(self, target: str) -> str | None:
        """参照の先の分野（ページならその分野、目次のまだない分野の候補なら registry の分野）。"""
        p = self.page(target)
        if p is not None:
            return p.field
        if self.target == CATALOG:
            idx = self._catalog_index
            if target not in idx["merged"] and target not in idx["dropped"] and target in idx["candidates"]:
                return idx["candidates"][target].text("field") or None
        return None

    def absent_fields(self) -> list[str]:
        """目次のモデルで、分野のファイルがまだない分野（front matter のときは空）。"""
        if self.target != CATALOG or self.atlas.catalog is None:
            return []
        return [f for f in self.site.fields if f not in self.atlas.catalog.files]

    def field_file(self, f: str) -> str:
        """分野の置き場所の呼び名（目次は planning/catalog/<f>.yaml、front matter は docs/<f>/）。"""
        if self.target == CATALOG and self.atlas.catalog is not None and f in self.atlas.catalog.files:
            return self.atlas.catalog.files[f].file
        return f"docs/{f}/"

    # ---- 公開

    def is_stub(self, p: PageRecord) -> bool:
        """骨格のページ（stage が site.yml の stages の最初）か。目次のページは False。"""
        return self.target == FRONT_MATTER and p.stage == self.rules.skeleton_stage

    def published(self, p: PageRecord) -> bool:
        return self.atlas.is_published(p)


def held_back_ids(docs, nav: Nav | None) -> set[str]:
    """nav.yml の exclude_docs に当たる docs/ のページの id。"""
    if nav is None or not nav.exclude:
        return set()
    return {p.id for p in docs.pages if p.in_docs and nav.excluded(p.rel)}


def load_context(root: Path, target: str = FRONT_MATTER, today: datetime.date | None = None) -> Context:
    """検査に渡すものを読む。site.yml が読めなければ lib.Fatal。"""
    root = Path(root)
    site = load_site(root)
    rules = Rules.from_site(site)
    today = today or datetime.date.today()
    if target == CATALOG:
        catalog = load_catalog(root, site)
        atlas = Atlas(site, catalog.pages, None, catalog=catalog)
        return Context(root, target, site, atlas, rules, today, problems=atlas.problems())
    docs = load_docs(root, site)
    nav = load_nav(root)
    settings = load_settings(root)
    atlas = Atlas(site, docs.pages, load_data(root), held_back_ids(docs, nav), docs=docs)
    problems = atlas.problems() + nav.problems + settings.problems
    return Context(root, target if target in (FRONT_MATTER, TEMPLATES) else FRONT_MATTER, site, atlas, rules, today,
                   nav, settings, problems)
