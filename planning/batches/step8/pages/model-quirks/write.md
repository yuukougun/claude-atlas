# model-quirks 執筆の報告

## 書いたファイル
- docs/models/model-quirks.md（stubs から移動。stage を draft、updated を 2026-11-05、sources を既存の 6 件〔api-docs-prompting-best-practices・opus-5・opus-5-5・claude-sonnet-5-5・claude-fable-5-1・claude-haiku-5-5〕、sections に what-it-prevents と misconceptions を追加）
- snippets/model-quirks/observation-log.md と observation-log.expect.yaml（観察の記録の表。目次の templates は「なし」だが、観察の節に要るので足した）
- planning/batches/step8/pages/model-quirks/facts-proposal.yml（モデル別の偏りの数値の提案）

## 必ず持つものの対応
- どの原理に関わるか（principle＝確かめる）：#what-it-prevents（冒頭の文で名指し。#observe-and-record の判断例も記録で確かめる流れ）
- どの原因に関わるか（prevents＝合っていない）：#what-it-prevents（「モデル・effort・頼み方が作業に合っていない」と名指し）
- pitfalls：空のため、持たない
- level を持つ・要点の最初が「何が分かるか」：冒頭の囲み
- 構成（原理型：要点→何が起きるか→なぜ→何に効くか→誤解→関連）：#official-guidance が「何が起きるか」、#observe-and-record が観察の手順と判断例、#what-it-prevents、#misconceptions。比喩付きの図は、薄くなるので置かなかった

## メインに判断してほしいこと
- 本文の表に、モデルの系統名（Opus・Sonnet・Fable・Haiku）を 2026-10-29 の確認の時点つきで手書きした。版の数字は書いていない。系統名も「変わりやすい名称」と見るなら、names への追加か、数値の提案（facts-proposal.yml）の fact-table への置き換えが要る
- 表の「合わせ方の向き」の列は、調査資料 02 §4-13 を要約した私の言い換えで、公式の文は写していない

## 提案
- facts-proposal.yml を参照（used_in は #official-guidance。fact 化されたら、表を fact-table か fact の目印に替える）
- related に outdated-advice-ledger を足す提案はしない（台帳の行への link は本文にある）

## 検査の結果
- 1 回目：エラー 0・警告 6。直した後：エラー 0・警告 1
- 残した警告：no-doubled-joshi（助詞「に」）。link の目印の間に道具が書く題名（「新しいモデルに替えたら見直すこと › 見直す順」）に含まれる「に」が原因で、手では直せない誤検出

## 確かめていないこと
- 一次資料（各モデルの公式の指針）を開いていない。表の内容は束の調査資料 02 §4-13（確認日 2026-10-29）の写しで、現在の指針と合うかは未確認
- 参照先 outdated-advice-ledger の行と anchor は check_page が通ったことだけ確認した
- 観察の雛形は動作を確かめていない（記録の表の形だけ）
- 手順の「数件」は経験則で、根拠のある数ではない
- Web の取得なし

## 使用量
- 道具の呼び出し：約 12 回、Web の取得 0
