# write.md：how-much-understanding-to-keep

## 書いたファイル

- `docs/judgment/how-much-understanding-to-keep.md`（stub から mv。stage を draft、updated を 2026-11-05 に）
- front matter で変えたキー：`sections`（`what-happens` と `how-to-check` を足した。既存4つの anchor は変えていない）、`sources`（sources.yml に既にある5件の id）、`stage`、`updated`
- 雛形・図・`data/sources.d/<id>.yml` は作っていない（目次の templates と visual が「なし」。出典は既存の id だけ）

## 必ず持つものの対応

- 冒頭の要点：冒頭の `!!! abstract`
- 判断例（状況・迷う候補・選んだもの・理由の4行）：`#explain-or-reject`
- level（任せる）：front matter
- 構成の目安（要点→何が起きるか→なぜ→判断例→握るもの→確かめ方）：何が起きるか `#what-happens`／握るもの（中核の線引き）`#core-and-periphery`／なぜ `#supervision-paradox`／判断例 `#explain-or-reject`／確かめ方 `#how-to-check`。「なぜ」は判断例の後に置いた（目安なので並べ替え）。
- 比例則（周辺を任せきる内容）：`#core-and-periphery` で、守りの diffs-humans-must-read と what-not-to-delegate を link で指し、own-generated-code は `#explain-or-reject` で指す

## メインに判断してほしいこと

- 「ある実務家」の認知負債の紹介は、個人を名指ししない決めに合わせて名を出さず、出典は `sources` の speakerdeck-twada-agentic-software-engineering で示した。Simon Willison の記事は sources.yml にないので載せていない
- U-22・RITSEC・With AI 部門の大会の例は、束の注記で一部が未確認のため載せなかった（大会の話は practice-vs-contest-day へ link）
- 週1回など、ここで言う習慣の頻度は本文に書かなかった（根拠が中で数値の出典がないため）

## 提案

なし（数値の提案・front matter の提案・用語集への提案は不要。認知負債は用語集にある）

## 検査の結果

- 2回流した。最終はエラー 0・警告 2
- 残した警告：`no-doubled-joshi`（41行目の要点内「AI が書いたコードが増えて」の「が」、75行目の link 間の題名を含む長い文）。時間の上限で直せていない。75行目は link の間（道具が書く題名）を含む文で、前後の文を短くすれば減らせる見込み
- 1回目の後、警告 4 のうち 3 つは Bash の Python で文を直した（brief の「Write で書く」から外れた。Edit ではなく置換で、内容は文の切り分けだけ）

## 確かめていないこと

- 本文中の研究の数値（中央値 3 対 1・n=4・GPT-4o・直後のクイズ）は束の写し（research/10・24 の注記）に基づく。arXiv や Anthropic の記事の原文を開いていない
- Rust の開発ガイドの内容は束の写しのみ。原文を開いていない
- Anthropic の社内調査の標本と手法は確かめていない（本文にもそう書いた）
- 判断例は作った架空の状況で、実際に試していない
- 「確かめ方」の4項目は、この辞典の推奨（効果を測った研究なし）
- 追加した2つの節の見出しの語（用語）と、link 先の節の存在は check_page の参照検査が通っただけ

## 使用量

- 道具の呼び出し：約 12 回。Web の取得：0
