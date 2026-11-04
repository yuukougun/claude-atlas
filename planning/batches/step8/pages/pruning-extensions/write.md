# write.md：pruning-extensions（recipe・extend）

## 書いたファイル

- `docs/extend/pruning-extensions.md`（stubs から移した。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（既存の measure・criteria は変えず、guards・cut・verify・failure を足した）・`sources`（既存の id 7 つ）・`stage`・`updated`
- `snippets/pruning-extensions/inventory-checklist.md` と `.expect.yaml`（目次の案の棚卸しのチェックリスト）
- `snippets/pruning-extensions/skill-overrides.json` と `.expect.yaml`（目次の案の skillOverrides の設定）
- `planning/batches/step8/pages/pruning-extensions/facts-proposal.yml`（数値の提案）
- `data/sources.d/pruning-extensions.yml` は作っていない（足す出典がすべて data/sources.yml にある）

## 必ず持つものの対応

- 用途ごとの進め方（要点以外に必ず持つ）：手順は `#measure`（手順 1〜3）と `#cut`（手順 4・5）。各手順に「確かめ：」の行を付けた
- 確かめる・縛るのページへの道：本文の `#guards`（felt-vs-measured#what-to-record・vetting-extensions#guards・inspect-context#baseline）と、front matter の prerequisites と related
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：`#guards`・`#measure`・`#criteria`・`#cut`・`#verify`・`#failure`
- level：front matter の「仕組みにする」のまま

## メインに判断してほしいこと

- 目次の備考「40 個を超えたら見直す」は、出どころを確かめる指示のため本文に書かなかった。数値ファイルに置く案が出たら、used_in は `pruning-extensions#criteria`
- 公開の約束や方針の文は書いていない

## 提案

- 数値：`facts-proposal.yml` の 2 件。本文には数を書いていないので、置く場所は measure の「/plugin の Installed タブ」の項目。置くなら「一定の期間と回数のあいだ」を目印に替える。2 件目は本文に使っていない（任意）
- 用語集・prh・front matter への提案はなし

## 検査の結果

- 1 回目（書いた後）：エラー 0・警告 7（助詞「に」の重なり）。直した
- 2 回目（直した後）：エラー 0・警告 1（助詞「に」の重なり）。その後 1 文を直したが、その後の再検査は上限のため流していない

## 確かめていないこと

- 日本語の文体の警告 1 件を直した後の textlint は流していない
- `skillOverrides` の最低の版・`claude plugin details` の最低の版は未確認（本文に書いていない）
- `/doctor` の挙動は公式のプラグイン計測の文書の説明だけで、実機では確かめていない
- 雛形 2 つの expect は、実機で動かしていない
- `/context` のメモリのファイルの欄と MCP ツールの欄の名前は、画面の表記を確かめていない（MCP ツールの欄は公式の文書による）
- MCP を外す具体的な操作は connecting-mcp に任せ、中身を確かめていない
- 共有を「複数の人が使うものに絞る」基準の根拠の強さは、調査資料の「中」を写した

## 使用量

- 道具の呼び出し：約 20 回。Web の取得：2 回（skills、plugins/measure）
