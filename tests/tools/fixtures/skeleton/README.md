# 骨格の道具の試験用の置き場所

`tests/tools/test_make_skeleton.py` が一時フォルダに写して使う、小さな目次（`planning/catalog/`）と空の data（`data/`）。
`schema/` は置かない（試験が本物の `schema/` を写し、本物の site.yml・keys.yml・page.schema.json に当てる）。
値はすべて試験用の作りもので、本物の目次とは関係がない。

- 型：guide・hub（level と sources を持たない）・concept・feature・comparison・recipe・symptom・judgment・ledger
- symptom の1つは、診断の節（diagnosis）の前と後にほかの節を持つ（routes の目印を置く節を確かめる）
- concept の aliases に、YAML で文字列でない値に読まれかねない語（yes・null・日付・`a: b` など）を置く
- 目次だけの項目（materials・templates・visual・level_evidence・notes）と `nav_title: null` を持つページがある
- 参照（prerequisites・related・routes の to）は、この目次の中で解決する（骨格だけのサイトで check_pages.py のエラーが0になる）
