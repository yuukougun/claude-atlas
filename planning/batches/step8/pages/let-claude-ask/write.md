# write.md：let-claude-ask

## 書いたファイル
- docs/prompting/let-claude-ask.md（stub から移動。stage draft、updated 2026-11-05）
- front matter で変えたキー：sections（`why`・`limits` の 2 節を足した）、sources（cc-docs-best-practices・cc-docs-tools-reference・cc-docs-hooks）、stage、updated
- snippets/let-claude-ask/interview-feature.{txt,expect.yaml}、interview-evaluator.{txt,expect.yaml}
- planning/batches/step8/pages/let-claude-ask/facts-proposal.yml
- data/sources.d/let-claude-ask.yml は書いていない（使った出典は 3 つとも data/sources.yml にある）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle「見せる」・prevents「見えていない」を本文で名指す）：`why`
- level（整える）と、要点の最初が「何が分かるか」：冒頭の囲み
- 技法の構成（Before/After → 何が変わるか → なぜ効くか → 効かない場面）：`how`（Before/After と足したもの）→ `why` → `spec-then-fresh`・`decided-vs-open` → `limits`
- pitfalls：front matter に値がないので、本文で名指す対象なし

## メインに判断してほしいこと
- A-6 の雛形は `snippets/let-claude-ask/` に置いた。目次の notes は「spec-first と取り込みで共有する」と書くので、spec-first のページの担当が同じものを別に置くと重複する。共有の置き場所を決めてほしい
- A-6 の元の文はツール名 AskUserQuestion を出すが、notes と research/26 #17 に従い「インタビューして」の形に直した
- 数値（1 回の問数と選択肢の数、timeout の値）は本文に書かず、下の提案にした。数値ファイルに入った後、`how`・`limits` の「上限がある」の所へ目印を置きたい

## 提案
- 数値の提案：facts-proposal.yml（ask-user-question-limits・ask-user-question-timeout）。Agent SDK の文書（Handle approvals and user input）は sources に id がなく、research/26 §3.9 の写しに基づく
- 用語集：「インタビューして仕様を作る」の用語は追加不要と見た

## 検査の結果
- 1 回目：エラー 0・警告 1（no-doubled-joshi、冒頭の導入文の「に」の重なり）
- 導入文を直したが警告が残ったので、もう一度「作業を始める前に」に直した。この 2 回目の直しは検査を流していない（検査は 2 回までの決め）。残っていれば、検証の担当が見てほしい

## 確かめていないこと
- 一次資料を開いていない（Web の取得 0 回）。束の写し（research/26 §3.9・03・10・11）をそのまま信頼した
- 「仕様に範囲外・関わるファイル・確かめる手順を書かせる」は 11 第2節の補完の写しに基づき、「この辞典の推奨」と書いた
- アプリでの選択式の質問の出方、サブエージェント不可・`-p` の制限が現行版で変わっていないか
- 雛形 2 つの動作（動作を確かめていない旨は道具が書く）

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
