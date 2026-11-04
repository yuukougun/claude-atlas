# write.md：search-research-thinking

## 書いたファイル
- docs/app/search-research-thinking.md（stub から移動。stage は draft、updated は 2026-11-05。sections に `choose`（選び方）と `verify`（使えたかと合っているかの確かめ方）を足した。sources に既存の 5 件を入れた）
- snippets/search-research-thinking/research-with-plan.md と .expect.yaml、search-changeable-facts.md と .expect.yaml（目次の templates は「なし」。分かりやすさのために 2 つ足した）
- planning/batches/step8/pages/search-research-thinking/facts-proposal.yml

## 必ず持つものの対応
- 比較の表（compare の目印）：#comparison
- 判断例：#choose（3 つ）
- 要点の「何ができるか」が「〜なら A、〜なら B」の基準：冒頭の要点の囲み
- 組み合わせ方：#combine
- 確かめ方（任意の節）：#verify
- level：front matter の「整える」

## メインに判断してほしいこと
- 呼び出しの回数と時間の目安は、数値ファイルに該当の項目がなかった。本文は数字なしで書き、提案（facts-proposal.yml）に置いた。反映されたら #comparison の「どれだけ広く調べるか」の項に fact の目印を足す。
- compare の表に、リサーチ（using-research 未公開）が「準備中」と出る。web 検索の行は自分のページへ向く（機能の page が自ページ）。生成の仕様なら問題ない。
- 「web 検索と思考」の組み合わせは公式の記事に記述がなく、（推論・実践例なし）を付けた提案として短く書いた。不要なら削る。

## 提案
- 数値：facts-proposal.yml のとおり（2 件）。

## 検査の結果
- 1 回目：エラー 0・警告 2（no-doubled-joshi：「か」「も」）。2 回目：エラー 0・警告 2（同じ 2 件）。その後、文を直した（再実行はしていない。2 回の上限のため）。

## 確かめていないこと
- 直した 2 文の警告が消えたか（再実行していない）。
- 雛形 2 つの動作（Claude で試していない）。
- 新しい体験の記述は、束の台帳の行と材料の写しに基づく。実画面は見ていない。
- Web の取得はしていない。

## 使用量
- 道具の呼び出しは約 12 回。Web の取得は 0 回。
