# write.md：move-judgment-into-scripts

## 書いたファイル
- `docs/enforce/move-judgment-into-scripts.md`（`stubs/enforce/` から `mv`）。front matter で変えたキー：`sections`（既存の 2 節の anchor は保ち、`what-happens`・`why`・`where-to-put`・`effects`・`misconceptions` を足して、ページの順に並べた）・`stage`（stub を draft）・`updated`（2026-11-05）・`sources`（`cc-docs-hooks-guide`・`cc-docs-skills`。どちらも data の features が挙げる既存の id）
- `snippets/move-judgment-into-scripts/ask-for-script.txt`・`.expect.yaml`（集計をスクリプトにさせる依頼）
- `snippets/move-judgment-into-scripts/review-the-script.txt`・`.expect.yaml`（書かせたスクリプトを流して確かめさせる依頼）
- 目印の組：snippet 2・compare 1・link 多数。`data/sources.d/move-judgment-into-scripts.yml` は新しい出典がないので書かない

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の `!!! abstract`
- level（仕組みにする）：front matter。要点の最初の項目も「何が分かるか」
- どの原理・どの原因に関わるか（`principle`・`prevents`・`pitfalls` を本文で名指す）：`#effects`（原理「縛る」「確かめる」、原因「縛っていない」「確かめていない」を名指す）。`pitfalls` は空なので名指す対象がない
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`#what-happens`・`#why`・`#effects`・`#misconceptions`。関連はテンプレートが下部に出す。間に目次どおりの `#what-to-move`・`#check-the-script` と、置き場所の `#where-to-put` を入れた

## メインに判断してほしいこと
- 「なぜそうなるか」の図は置かなかった（比喩が「お願いと鍵」だけで、文章で足りると判断した）。図が要るなら別の担当に頼む
- 1 件の研究の根拠（入力の縮小）は、束に研究の名・年・対象モデルがないため、「調査資料が拾った 1 件の研究」と書き、（根拠：中・類推）を付けた。名・年・対象は入れていない

## 提案
- 数値の提案・front matter の提案・用語集などへの提案：なし

## 検査の結果
- 1 回目：エラー 2・警告 7（半角と全角の間の空白 1 件、助詞の重複、「手続きを実行」の冗長表現）。直して 2 回目：エラー 0・警告 2
- 残した警告：`:74` の助詞「に」の重複（文を分けきれていない）。`:192` の助詞「に」の重複は、道具が書くリンクの題名（「補助ファイルとスクリプトに分ける」）と周りの文が 1 文と数えられた誤検出

## 確かめていないこと
- 雛形 2 つの動作は試していない
- 「API」タブの内容は一般論で、公式の文書で具体の手段を確かめていない。そのため具体の書き方は載せず、公式へ回した
- 研究の出典（名・年・対象）は束の材料にない。調査資料 11 の元 ID（p34#68）の先は開いていない
- 判断例・Before/After の作例の数や状況は作例で、実測ではない
- 囲み・タブの中の字下げした段落は textlint が検査しないため、目で読んだだけ
- `link` の目印の中のタイトルが入った文の読みやすさは、生成後に目で確かめた範囲に限る

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：0 回
