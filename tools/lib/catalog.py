"""目次（planning/catalog/）を、front matter と同じページのモデル（PageRecord）として読む。

tools/check_catalog.py の読む層（load_registry・load_field_file・load_catalog）を写して、ページを CatalogPage
（PageRecord）にしたもの。check_catalog.py は骨格（工程6c）まで目次の検査に使い、その後に退く（設計書 §8.3）。
このモジュールは、骨格の道具（目次から front matter を作る）と、目次と front matter に同じ規則を当てる検査の層が使う。
読むもの：registry.yaml（候補と古くなった助言の台帳の id）と、site.yml の fields の id を名前にした <field>.yaml。
ほかの名前の .yaml は読まずに stray に入れる（features.yaml は機能の id の一覧で、6b で data/facts.yml に移す）。
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .base import PageRecord, Problem, Record, as_strings
from .site import Site, load_site
from .yamlio import read_yaml

CATALOG_DIR = "planning/catalog"
REGISTRY_FILE = "registry.yaml"
FEATURES_FILE = "features.yaml"
CATALOG_ONLY_KEYS = ("level_evidence", "templates", "visual", "materials", "notes")   # 執筆の指示（front matter に写さない）


class CatalogPage(PageRecord):
    """分野のファイルの pages の1件。field はファイルの分野。"""

    kind = "catalog"

    def __init__(self, raw: dict, field: str, file: str, index: int):
        super().__init__(raw, file)
        self.field = field
        self.index = index             # pages の中の位置（0 から）。ナビゲーションの順

    @property
    def label(self) -> str:
        return self.id or f"(pages の {self.index + 1} 番目)"

    # 執筆の指示（catalog/README §3）
    @property
    def materials(self) -> list[str]:
        return self.strings("materials")

    @property
    def templates(self) -> list[dict]:
        return self.parts("templates")

    @property
    def visual(self) -> dict | None:
        v = self.raw.get("visual")
        return v if isinstance(v, dict) else None

    @property
    def notes(self):
        return self.raw.get("notes")

    @property
    def level_evidence(self) -> str:
        return self.text("level_evidence")


class Entry(Record):
    """registry の pages・ledger の1件、または分野のファイルの merged・dropped の1件。"""

    def __init__(self, raw: dict, file: str, kind: str, index: int, owner: str | None = None):
        super().__init__(raw, file)
        self.kind = kind               # pages・ledger・merged・dropped
        self.index = index
        self.owner = owner             # 分野のファイルの分野（registry の項目は None）

    @property
    def label(self) -> str:
        return self.id or f"({self.kind} の {self.index + 1} 番目)"


@dataclass
class FieldFile:
    field: str
    file: str
    raw: dict | None                   # 読めなければ None
    pages: list[CatalogPage] = field(default_factory=list)
    merged: list[Entry] = field(default_factory=list)
    dropped: list[Entry] = field(default_factory=list)

    @property
    def readable(self) -> bool:
        return self.raw is not None

    @property
    def chapters(self) -> list[str]:
        return as_strings(self.raw.get("chapters")) if self.raw else []


@dataclass
class Registry:
    file: str
    present: bool
    raw: dict | None = None
    candidates: list[Entry] = field(default_factory=list)
    ledger: list[Entry] = field(default_factory=list)


@dataclass
class Catalog:
    root: Path
    site: Site
    registry: Registry
    files: dict[str, FieldFile]         # 分野 → ファイル（site.yml の fields の順。ファイルのある分野だけ）
    stray: list[str]                    # 分野のファイルとして読まなかった .yaml
    problems: list[Problem]

    @property
    def pages(self) -> list[CatalogPage]:
        """全ページ（分野の順、ファイルの中の順）。"""
        return [p for ff in self.files.values() for p in ff.pages]

    @property
    def by_id(self) -> dict[str, CatalogPage]:
        out: dict[str, CatalogPage] = {}
        for p in self.pages:
            if p.id is not None:
                out.setdefault(p.id, p)
        return out

    def ids_of(self, kind: str) -> list[str]:
        """merged・dropped（分野のファイルの）、pages・ledger（registry の）の id。"""
        if kind in ("pages", "ledger"):
            items = self.registry.candidates if kind == "pages" else self.registry.ledger
        else:
            items = [e for ff in self.files.values() for e in getattr(ff, kind)]
        return [e.id for e in items if e.id is not None]

    def chapters(self, field: str) -> list[str]:
        ff = self.files.get(field)
        return ff.chapters if ff else []


def _mapping_doc(path: Path, shown: str, problems: list[Problem], what: str):
    doc = read_yaml(path)
    problems += doc.problems(shown)
    if doc.error is not None:
        return None
    if not isinstance(doc.data, dict):
        empty = "（空のファイル）" if doc.data is None else ""
        problems.append(Problem(shown, None, f"最上位をマッピング（{what}）にする{empty}", "形"))
        return None
    return doc.data


def load_registry(root: Path, problems: list[Problem]) -> Registry:
    path = Path(root) / CATALOG_DIR / REGISTRY_FILE
    shown = f"{CATALOG_DIR}/{REGISTRY_FILE}"
    reg = Registry(shown, path.exists())
    if not reg.present:
        problems.append(Problem(shown, None, "registry.yaml がない", "設定"))
        return reg
    reg.raw = _mapping_doc(path, shown, problems, "pages・ledger・notes")
    if reg.raw is not None:
        for kind, store in (("pages", reg.candidates), ("ledger", reg.ledger)):
            items = reg.raw.get(kind)
            if isinstance(items, list):
                store += [Entry(x, shown, kind, i) for i, x in enumerate(items) if isinstance(x, dict)]
    return reg


def load_field_file(root: Path, fid: str, problems: list[Problem]) -> FieldFile:
    shown = f"{CATALOG_DIR}/{fid}.yaml"
    ff = FieldFile(fid, shown, _mapping_doc(Path(root) / shown, shown, problems, "field・chapters・pages …"))
    if ff.raw is None:
        return ff
    pages = ff.raw.get("pages")
    if isinstance(pages, list):
        ff.pages = [CatalogPage(x, fid, shown, i) for i, x in enumerate(pages) if isinstance(x, dict)]
    for kind in ("merged", "dropped"):
        items = ff.raw.get(kind)
        if isinstance(items, list):
            getattr(ff, kind).extend(Entry(x, shown, kind, i, fid) for i, x in enumerate(items) if isinstance(x, dict))
    return ff


def load_catalog(root: Path, site: Site | None = None) -> Catalog:
    """目次を読む。site を渡さなければ schema/site.yml を読む（読めなければ Fatal）。"""
    root = Path(root)
    site = site or load_site(root)
    problems: list[Problem] = []
    cdir = root / CATALOG_DIR
    registry = load_registry(root, problems)
    files = {f: load_field_file(root, f, problems) for f in site.fields if (cdir / f"{f}.yaml").exists()}
    stray = sorted(f"{CATALOG_DIR}/{p.name}" for p in cdir.glob("*.yaml")
                   if p.name not in (REGISTRY_FILE, FEATURES_FILE) and p.stem not in site.fields) if cdir.is_dir() else []
    return Catalog(root, site, registry, files, stray, problems)
