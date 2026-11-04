# write.md：keeps-stopping（執筆）

## 書いたファイル
- docs/symptoms/keeps-stopping.md（stub から移して draft。front matter で変えたキー：sections に forms・routes・example・prevent を足した、sources に 7 件〔api-docs-prompting-claude-sonnet-5-5・cc-docs-best-practices・cc-docs-goal・cc-docs-permission-modes・api-docs-effort・cc-docs-model-config・cc-changelog〕、stage、updated）
- snippets/keeps-stopping/carry-through.txt と carry-through.expect.yaml（最後まで進めさせる依頼の型。目次の templates は「なし」だったが、モデルの癖の手順で要るので足した）
- planning/batches/step8/pages/keeps-stopping/facts-proposal.yml

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめる順。関われば人の側の落とし穴）：#diagnosis（6 手順。末尾に人の側の落とし穴の箇条）
- 原因ごとの振り分け先（routes）：#routes（`gen:begin routes`）
- 構成の目安の残り：よくある形 #forms／判断例 #example／予防 #prevent
- 六つの原因のうち prevents にあるのは 見えていない・合っていない の 2 つ。手順 2・3 が前者、4・5・6 が後者

## メインに判断してほしいこと
- 手順 1 に「古い版の不具合」を数値なしで書いた（版は facts-proposal.yml に提案）。本文に版を出さない形でよいか。
- 手順 6 で Sonnet の low・medium の癖を、公式の指針へのリンクと確認日（2026-11-05）つきで書いた。モデルの名前はリンクの題名にだけ出た（本文の地の文には出さない）。
- 手順 4 の権限モードは「Claude Code の機能」と書いた（data の surfaces が claude-code のみ）。アプリ側の確認の出方は書いていない。

## 提案
- facts-proposal.yml：auto-mode-no-verdict-display-fixed（used_in：keeps-stopping#diagnosis。本文に目印はまだ置いていない。採用されたら、手順 1 の「現在は修正されている」の前後に目印を足せる）

## 検査の結果
- 1 回目：エラー 2・警告 6。2 回目（直した後）：エラー 0・警告 4
- 残した警告 4 件は no-doubled-joshi（70 行の「が」2 件、80 行の「に」、131 行の「か」）。意味が変わらず、直すと文が固くなるので残した

## 確かめていないこと
- 手順 1 の不具合の修正の版と内容は、束の research/22 #11 の写しに基づく。CHANGELOG で再確認していない
- Sonnet の指針の記述は、公式の Prompting Claude Sonnet 5.5 を 1 回取得して確かめた（2026-11-05）。ほかのモデルの傾向は書いていない
- アプリの effort の見方（モデルのメニュー）は data の feature の note に基づく。画面は未確認
- `/effort` で段を選べることは data の note に基づく。引数なしの動作は未確認
- 雛形 carry-through の動作は試していない
- リンクの節（agent-loop#why-stops など）は束の「指せる節」から選んだ。outdated-advice-ledger#keep-going-dont-be-lazy は check_page で解決された

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：1 回
