# write.md：asking-for-reasoning

## 書いたファイル
- docs/prompting/asking-for-reasoning.md（stubs から移した。stage は draft、updated は 2026-11-05）
- snippets/asking-for-reasoning/short-basis-request.txt と .expect.yaml
- planning/batches/step8/pages/asking-for-reasoning/facts-proposal.yml
- front matter で変えたキー：sections（example・effects・limits を足した。既存の refusal・alternatives は不変）、stage、updated、sources（既存の id 6 つ）
- stubs/prompting/asking-for-reasoning.md は mv の代わりに新規 Write のあと rm した
- data/sources.d/asking-for-reasoning.yml は書いていない（新しい出典なし。sources は data/sources.yml の既存 id）

## 必ず持つものの対応
- どの原理・原因に関わるか（principle 確かめる・prevents 確かめていない を名指す）：#effects
- level 整える・要点の最初が「何が分かるか」：冒頭の要点の囲み
- 技法の構成（Before/After → 何が変わるか → なぜ → 効かない場面）：#example（Before/After と変わったこと）、#refusal（なぜ）、#alternatives、#limits（効かない場面・やりすぎ）
- pitfalls：front matter に pitfalls なし。#limits で効かない場面を扱った

## メインに判断してほしいこと
- 課金の扱い（出力の前に止まっても課金される分類）と、reasoning_extraction が足された日・対象モデルは、本文に手で書かず facts-proposal.yml に提案した。承認後に fact の目印へ差し替えたい（今の本文は課金の中身に触れず「Refusals の文書で確かめる」）
- アプリでの思考の要約の表示方法は束に材料がなく、「未確認」と書いた

## 提案
- facts-proposal.yml（2 件）：reasoning-extraction-billing、reasoning-extraction-since。used_in は asking-for-reasoning#refusal

## 検査の結果
- check_page.py：1 回目 エラー 3・警告 1（prh の skill・subagent・output style と助詞の重複）。直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 用語集に「スキル」「サブエージェント」「出力スタイル」の表記があることは prh の指摘で知っただけで、用語集の全文は読んでいない
- `showThinkingSummaries`・`display: "summarized"`・`claude --safe-mode`・`stop_reason` の細部は束（research/26・台帳）の写しのままで、一次資料を開いていない
- 解釈可能性研究の根拠の印（中）は束の写し（05 §2-3）に基づく。論文の原文は未確認
- 雛形の動作は試していない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得 0 回
