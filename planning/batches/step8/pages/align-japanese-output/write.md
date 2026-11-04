# write.md：align-japanese-output（執筆）

## 書いたファイル
- docs/japanese/align-japanese-output.md（stubs から mv。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（what-happens・effects・misconceptions の 3 節を足した。既存 5 節の anchor は変えず）、`sources`（既存の id 17 件）、`stage`、`updated`
- 雛形・図・data/sources.d は作っていない（目次の templates は「なし」。図の案は二軸の表にして、本文の表 2 つで足りると判断）

## 必ず持つものの対応
- 用途（なぜそうなるか・原理）：`#what-happens`（揃わない 3 つの形と手段の分け方）・`#request-layer`（指示は読んで従うかが決まる）
- 原理・原因への名指し：`#effects`（principle「縛る」「確かめる」、prevents「縛っていない」「確かめていない」を名指し）
- pitfalls：front matter に `pitfalls` のキーがないので、名指す対象がない
- level を持つ：front matter の level は「整える」、`#lock-layer` は「仕組みにする」。要点の最初は「何が分かるか」
- 構成（要点→例→なぜ→何に効くか→誤解→関連）：要点／`#what-happens`／`#request-layer`・`#lock-layer`・`#reach`／`#effects`／`#misconceptions`／page-links（関連）

## メインに判断してほしいこと
- 「確認日と版を付けて」書く挙動（強制できる場所・アプリに機械の仕組みがないこと）に、確認日 2026-11-03 は付けたが、Claude Code の版は付けていない（束に版がなく、版は入った版に当たるため手で書かない）。版を付けるなら数値の提案が要る
- 判断例を 2 つ置いた（`#app`、`#keep-few`）

## 提案
- なし（用語集・prh・data・front matter の直しの提案はない）

## 検査の結果
- 1 回目：エラー 0・警告 4。直した後の 2 回目：エラー 0・警告 2（no-doubled-joshi が 2 件）
- 2 回目の後に、その 2 件の文を言い換えた。規則の2回の上限があるため、3 回目は流していない

## 確かめていないこと
- 2 回目の後に言い換えた 2 文の textlint の警告が消えたこと
- 表の「書かれていない」の行（`language` の設定のサブエージェントと圧縮の後、出力スタイルのクラウド）は、束の写しに基づく。公式の文書は開いていない
- link の `outdated-advice-ledger#styles-for-tone` と各 `id#anchor` は check_page の通過で確認したが、リンク先の文の読みやすさは見ていない
- 「アプリには機械で確かめる仕組みがない」「API では自分のコードで判定できる」は束と推論による。アプリの最新の画面は確かめていない
- Claude Code の WSL・Linux 以外の動作は書いていない（未確認）

## 使用量
- 道具の呼び出し：約 11 回。Web の取得：0 回
