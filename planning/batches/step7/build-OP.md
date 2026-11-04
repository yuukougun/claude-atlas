# 報告：OP（使用量を抑える運用の道具と文書。2026-11-05）

## 1. 書いたファイル
- `tools/check_page.py`：`<id> […]` について gen_site.py --page（`--no-gen` で飛ばす）→ check_pages.py --page → textlint（textlint_targets.targets の対象のうちそのファイルだけ。骨格は「対象外」と書く）。1指摘1行（エラーが先）、上限 25 件（`--limit`、0 で無制限）、最後に「エラー N・警告 M」。終了コード 0＝エラーなし・1＝エラーあり・2＝検査できない
- `tests/tools/test_check_page.py`（14 件。偽の textlint と fixtures/checks を使う）
- `planning/guides/card.md`（199 行）。各節の見出しに（common §N）か（型の手引き）を添えた
- `tools/make_packet.py`：2 節の最後に「指せる節」（つながるページの sections の `id#anchor`・題名）を足した。束の冒頭に「読むのはこの束と planning/guides/card.md だけ」を足し、7 節をカード中心に直した。`tests/tools/test_make_packet.py` に 2 件足し 1 件直した
- `planning/batches/step7/brief-page.md`（v3）、`.claude/workflows/step7-prototype.js`（v3。執筆 sonnet・high → 検証と直し sonnet・medium の pipeline）
- `tests/guides/test_guides.py`：card.md を、型の手引きの一対一・README の一覧・「元：」の行から外し、代わりに「見出しに元を添える」「common §N の先がある」「200 行以内」「全型の行がある」を見る。「common §N」を節の参照として解く

## 2. メインに判断してほしいこと
- card.md を `planning/guides/README.md` の一覧に載せていない（書いてよい範囲の外のため）。試験の側で除いてある。載せるなら README の表に 1 行足し、試験の除外を外す
- 束は `state/packets/` に作り直していない。新しい束（指せる節つき）が要るなら `uv run python tools/make_packet.py <id> …` を流す。instructions-ignored の束は約 49 KB から約 57 KB に増える（上限の目安 60000 字に近い。ページによっては材料の抜き出しの上限が下がる）
- `tests/tools` の失敗 2 件は、ほかの担当が直している途中のページによる。test_check_templates の TestRealSettings.test_cli は snippets/keep-replies-in-japanese/user-settings.json の `language` キー、test_gen_catalog の test_generated_files_are_fresh は competition-rules の数値 `contest-ai-rules`（data/facts.yml にない）と nav.yml が古いこと。この変更とは関係がない

## 3. 検査の結果
- `uv run python -m unittest discover -s tests/guides`：17 件 OK
- `uv run python -m unittest discover -s tests/tools`：585 件、失敗 2 件（上の件。ほかは OK）。test_check_page 14 件・test_make_packet 90 件は OK
- `uv run python tools/check_page.py instructions-ignored`（約 3.4 秒）の出力は次の 1 行だけだった：
  `エラー 0・警告 0`

## 4. 確かめていないこと
- 新しいワークフローの実際の流し（JS の構文は、先頭の return の形を除いて確かめただけ）
- card.md を読んだ担当が書いたページの質
