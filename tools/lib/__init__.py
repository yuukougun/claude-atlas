"""読む層（設計書 §8.3）：front matter・目次（catalog）・data・schema/site.yml を読み、ページのモデルを作る。

作る層（tools/gen/）と検査の層（tools/checks/）は、ファイルを直に読まずにここを通す。読む層は値を直さず、止まらずに
読む（形の誤りは空として読み、YAML の誤りなどは Problem に記録する）。誤りとして出すのは検査の層である。
依存は PyYAML だけ（pyproject.toml。`uv run` で動かす）。

使い方（tools/ を sys.path に置いて `from lib import …`。tools/<道具>.py からは、そのまま import できる）:

    from lib import load_atlas
    atlas = load_atlas(ROOT)                  # site.yml・docs/ と stubs/ の front matter・data/ を読む
    for page in atlas.ordered():              # pages.Page（PageRecord）。ナビゲーションの順
        page.id, page.field, page.type, page.level, page.stage, page.url
        page.prerequisites, page.related      # [Ref]（id か id#anchor）
        page.routes                           # [Route(cause, to=(Ref, …))]（症状のページ）
        atlas.resolve(page.prerequisites[0])  # 相手のページか None
        page.markers                          # 本文の目印（gen・fact・link。markdown.Marker）
        atlas.expiry(page).date               # 期限の日（design §9.2）
        atlas.is_published(page)              # 公開するか（docs/ にあり draft 以上。design §8.4）
    atlas.duplicates                          # 同じ id のページ（docs/ と stubs/ の両方など）
    atlas.data.facts["<id>"].checked          # data/facts.yml の項目（data.Item）
    atlas.problems()                          # 読む層の指摘（YAML の誤り・目印の対など）
    catalog_atlas = load_catalog_atlas(ROOT)  # 目次（planning/catalog/）を同じモデルで読む

    from lib.schema import load_validator     # front matter と data を schema で検査する
    from lib.yamlio import to_jsonable, line_at
    v = load_validator(ROOT / "schema/page.schema.json")
    for issue in v.errors(to_jsonable(page.raw)):
        line = line_at(page.raw, issue.path)

部品:
  base.py      指摘（Problem）・値の読み方・参照（Ref）・PageRecord（front matter と目次に共通の読み方）
  yamlio.py    YAML を行番号つきで読む（日付は文字列のまま）
  site.py      schema/site.yml（語彙）
  markdown.py  front matter と本文の分け方・フェンス・見出し・目印
  pages.py     docs/<field>/<id>.md と stubs/<field>/<id>.md（骨格のページ）
  catalog.py   planning/catalog/（tools/check_catalog.py の読む層を写したもの）
  data.py      data/（facts・features・names・domains・sources と sources.d・advice・inspection）
  ledger.py    キーの台帳（schema/keys.yml）と JSON Schema の生成（入口は tools/make_schema.py）
  schema.py    小さな JSON Schema（Draft-07 の一部）の検査器
  graph.py     前提のグラフ（強連結成分・到達・前提が先に来る並び）
  model.py     Atlas（全体のモデル・参照の解決・公開・期限の日）
"""
from .base import Fatal, PageRecord, Problem, Record, Ref, Route, parse_date
from .catalog import Catalog, CatalogPage, load_catalog
from .data import Data, Item, load_data
from .model import Atlas, Due, Expiry, load_atlas, load_catalog_atlas
from .pages import Docs, Page, load_docs, read_markdown
from .site import Site, load_site

__all__ = [
    "Atlas", "Catalog", "CatalogPage", "Data", "Docs", "Due", "Expiry", "Fatal", "Item", "Page", "PageRecord", "Problem",
    "Record", "Ref", "Route", "Site", "load_atlas", "load_catalog", "load_catalog_atlas", "load_data", "load_docs",
    "load_site", "parse_date", "read_markdown",
]
