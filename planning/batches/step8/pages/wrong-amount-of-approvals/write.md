# write.md：wrong-amount-of-approvals（執筆）

## 書いたファイル
- docs/symptoms/wrong-amount-of-approvals.md（stubs から mv。stage を draft、updated を 2026-11-05、sections に forms・routes・example・prevent を足し、sources に既存の 5 件を入れた）
- 雛形・図・data/sources.d は作っていない（目次の templates・visual が「なし」。新しい出典もない）

## 必ず持つものの対応
- 診断のチェックリスト（安く確かめる順。人の側の落とし穴を後に）：#diagnosis（手順 1〜4 が合っていない・境界がない、手順 5 が預けすぎる）
- 原因ごとの振り分け先（routes）：#routes（`gen:begin routes`）
- 構成の目安のうち、要点・よくある形：冒頭の囲み・#forms／判断例：#example／予防：#prevent

## メインに判断してほしいこと
- なし（約束・方針の文は書いていない）

## 提案
- なし（数値は本文に書いていない。承認率などは approval-fatigue に任せた）

## 検査の結果
- 2 回流した。エラー 0・警告 2
- 残した警告：51 行「に」の重複（導入の文）、94 行「で」の重複（生成された長いリンク題名を含む文）。意味を変えずに直せる形が見つからなかった

## 確かめていないこと
- 手順 3 の「会話の頼みや CLAUDE.md は許すことを変えない」は、束の data（permissions の note）にだけ基づく。公式の文書は開いていない
- `claude -p` と Agent SDK の確認の挙動は、束の research/23 F2-b（2026-11-03 確認）にだけ基づく。版は書いていない
- アプリの面の記述は、束の permission-modes-in-the-app の要約にだけ基づく。アプリの画面は確かめていない
- 生成後のリンク（準備中のページ）の表示と、リンク先の節が公開後に残るかは確かめていない

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：0 回（束とカード以外に、同種の症状ページ keeps-stopping と stubs・sources の形を確認するため、docs と snippets を少し読んだ）
