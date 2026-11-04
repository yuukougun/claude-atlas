# write.md：ask-for-outcomes（執筆）

## 書いたファイル
- docs/prompting/ask-for-outcomes.md（stubs から mv。stage は draft）
- snippets/ask-for-outcomes/outcome-request.txt・outcome-request.expect.yaml
- front matter で変えたキー：sections（節を 4 つ足した。既存 3 つの anchor は不変）・sources（既存 id 4 つ）・stage（draft）・updated（2026-11-05）

## 必ず持つものの対応
- どの原理に関わるか（principle：見せる・確かめる）：#why（対象と測り方を「見せる」、完了を測って「確かめる」）
- どの原因を防ぐか（prevents：見えていない・確かめていない）：#why（2 つの原因を名指し）。冒頭の要点にも同じ
- pitfalls：front matter に pitfalls のキーがないため持たない
- level（任せる）・要点の最初は「何が分かるか」：冒頭の要点の 1 項目目
- 技法の構成（Before/After → 何が変わる → なぜ効く → 効かない場面）：#before-after → #outcomes・#specifics・#bottleneck → #why → #limits
- 比例則（任せる幅を広げるので守りを先に）：#outcomes の第 4 段落（define-done・evidence-not-reports・goal-until-done を指す）

## メインに判断してほしいこと
- sections に 4 つ足した（before-after・why・limits・templates）。技法の構成に合わせるため
- 題名「細かく指図するか、成果で頼むか」の「か」が 2 つ続く問いの形は、catalog の決定どおりで変えていない

## 提案
- 出典の一覧が束になく、data/sources.yml の既存 id（cc-docs-best-practices・api-docs-prompting-best-practices・prussianblue-ahc054-claude-code・jitendrazaa-tips-code-tips-creator-boris）を sources に入れた。新しい出典の追加はない
- 数値の提案なし。用語集・prh・front matter の提案なし

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 3（助詞の重なり。リンクの題名が入った文）。文を直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 雛形の動作（Claude に試していない）。例の依頼も説明用で、試した結果ではない
- 「公式の Best practices に対比表がある」は束の調査資料の記述によるもので、現行の文書で再確認していない
- 体験記（AHC054）と実践者の紹介の内容は束の写しによるもので、原文を開いていない
- 判断例の「コンテストでの AI の利用は大会ごとの規則に従う」は一般的な注意で、個別の大会の規則は見ていない

## 使用量
- 道具の呼び出し：約 14 回（Read 4・Bash 6・Write 4 ほか）。Web の取得：0
