# write.md：grow-review-checklists

## 書いたファイル
- docs/team/grow-review-checklists.md（stubs から mv。stage を draft、updated を 2026-11-05 に。sections を足した：guards・steps・template・check・when-failing）
- snippets/grow-review-checklists/extract-miss-reasons.md と .expect.yaml（kind：prompt、safety：false）
- data/sources.d/ は書いていない（下の「確かめていないこと」）

## 必ず持つものの対応
- 手順：steps
- 確かめる・縛るのページへの道：前提 instructing-reviewers（冒頭の要点と guards）。guards で independent-review#ai-approval・risk-tiered-approval#ai-approval-doesnt-count・independent-review#who へ。steps・check・when-failing でも review-bottlenecks・postmortems を指す
- level：front matter（仕組みにする）のまま
- 構成の目安（守り→手順→確かめ方→失敗したとき）：guards → steps → template → check → when-failing

## メインに判断してほしいこと
- 材料が目次の 1 行（企業ブログ、根拠：中）だけで、ブログの URL・題名が束にない。本文は「企業ブログで紹介された考え方に基づく（根拠：中）」とだけ書き、出典（sources）は空のまま。出典の URL が分かれば sources に足す
- 失敗したときの節は、束に症状ページの id がなく、症状への振り分けではなく関連ページへの link にした

## 提案
- front matter・用語集・data への提案なし。数値の提案なし

## 検査の結果
- 2 回流した：エラー 0、警告 2（残し方：両方とも道具が差し込んだ link の題名「…を…に合わせる」「PR の説明に書くこと」が文中の「にある」と重なって出る no-doubled-joshi の誤検出。本文は直せない。51 行目 review-bottlenecks#match-review-capacity、131 行目 create-and-review-prs#pr-description）

## 確かめていないこと
- 手順の進め方（過去の PR で試す、観点ごとの使われ方を見る）は、束の材料に具体の記述がなく、独自の組み立て。実践例の確認はしていない
- 雛形の動作は未確認（実際の PR で試していない）
- risk-tiered-approval#principles-and-causes を「守りに移す」の文脈で指したが、節の中身を束の要約でしか知らない。検証の担当が文脈の合いを見てほしい

## 使用量
- 道具の呼び出し：約 11 回。Web の取得：0 回
