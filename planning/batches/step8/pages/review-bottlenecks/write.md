# write.md：review-bottlenecks（concept・team）

## 書いたファイル
- docs/team/review-bottlenecks.md（stub を移す代わりに新規に Write し、stubs/team/review-bottlenecks.md を `rm` で消した。`mv` ではない）
- docs/img/review-bottlenecks/clog.svg（図：PR が増え、レビューと動作確認の口に待ちが積もる流れ）
- front matter で変えたキー：`sections`（末尾に principles-and-causes・misconceptions を足した。既存 3 つは不変）・`sources`（3 件）・`stage`（draft）・`updated`（2026-11-05）
- snippets と data/sources.d/review-bottlenecks.yml は作っていない（雛形の案なし。出典 3 件は data/sources.yml に既にある）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle`・`prevents`・`pitfalls` を本文で名指す）：#principles-and-causes（確かめる／確かめていない、握る／預けすぎる、体感を信じる）
- level（任せる）：front matter。要点の最初の項目は「何が分かるか」にした（冒頭の囲み）
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#where-it-clogs（何が起きるか・なぜ。図つき）／#reading-case-numbers／#match-review-capacity／#principles-and-causes（何に効くか）／#misconceptions（誤解）／関連はテンプレートが出す

## メインに判断してほしいこと
- 本文は、事例の社名（READYFOR・Rehab for JAPAN）を、各社が自社の数値を報告した形で出した。否定的な文脈ではないが、名指しの扱いが気になるなら社名を外してよい
- 「一次資料で確かめたこと」：asoview の記事を 1 回取得し、「1 件 10〜15 分が 2〜3 分」「承認の自動化はやりすぎ」の記述と、測定条件の記載がないことを確かめた。READYFOR・Rehab for JAPAN の数値は束の research/25 P7 の写しによる（元記事は取得していない）

## 提案
- なし（用語集・prh・data・front matter の他のキーの提案はない）

## 検査の結果
- 2 回流した。エラー 0。警告 5（no-doubled-joshi）が残った
  - 43 行・106 行・110 行：生成されるリンクの題名の中の助詞を数えた誤検出に近い（本文側は 1 回直した）
  - 79 行・97 行：自分の文の助詞の重なり。回数の上限のため直せていない。メインかレビューの担当で直す

## 確かめていないこと
- READYFOR・Rehab for JAPAN の元記事（束の写しだけに基づく）
- 「Claude が動かして確かめていない変更を完了として出すことがある」は、束の Q6（実践者の報告）に基づく一般的な言い方で、頻度は書いていない
- 他の OS・IDE 拡張の動作（本文は扱っていない）
- 図の描画（SVG は検査の対象に入るが、目では見ていない）

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：1 回（tech.asoview.co.jp）
