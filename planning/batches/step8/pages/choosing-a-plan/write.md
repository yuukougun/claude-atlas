# write.md：choosing-a-plan（comparison・cost）

## 書いたファイル
- `docs/cost/choosing-a-plan.md`（stubs から移した。stage draft、updated 2026-11-05）
- front matter で変えたキー：`sections`（combining「組み合わせ方」を足した。既存 3 つは変えず）、`sources`（7 件、すべて sources.yml にある）、`stage`、`updated`
- `facts-proposal.yml`（数値の提案）。雛形・図・`data/sources.d/`：なし（目次の templates・visual が空。新しい出典もない）

## 必ず持つものの対応
- 冒頭の要点（「〜なら A、〜なら B」の基準を 1 文）：冒頭の囲みの「何ができるか」
- 比較の表（数値ファイルから道具が作る）：#plan-table（`fact-table usage-limit-types-by-plan`）。料金の表は fact がないため未配置（下の判断 1）
- 判断例：#examples（3 つ）
- level を持つ：front matter `level: 使う`
- 構成の目安（要点 → 比較の表 → 選び方 → 組み合わせ方）：冒頭 → #what-to-compare（観点）→ #plan-table → #examples → #combining
- 台帳の行（max-5x-or-20x）：#plan-table の末尾の段落で `outdated-advice-ledger#max-5x-or-20x` を指した

## メインに判断してほしいこと
1. 料金（月額・年払い）の表がない。facts にプランの料金の項目がなく、目印はない id を指すと止まるため置けなかった。他ページ（how-usage-limits-work・before-using-top-model）は「料金を含む表は choosing-a-plan にある」と指す。`facts-proposal.yml` の `plan-prices-individual` を facts に入れたら、#plan-table の fact-table の直後に `fact-table plan-prices-individual` の目印を足す。それまで、本文は料金のページへのリンクで代える
2. 表の Team の行の「—」は、facts 側で null のまま（束の材料に席ごとの値がない）。本文は「—は未確認で『ない』ではない」と書いた。Team の席ごとの上限を facts に足すかは任せる
3. 公式同士の食い違い（Fable の別の週の上限か、通常の週の上限の内側か）は before-using-top-model が持つ。このページは引かれ方を before-using-top-model#which-limit に任せ、表の「最上位のモデルの別の週の上限」列はそのまま出る。列の見直しが入れば、このページの表も変わる
4. Ultra の量が旧 Max 20x と同じかは断定していない（research/22 #44）。「ネットに同じだという説明がある」と匿名で書いた。この書き方でよいか

## 提案
`facts-proposal.yml` を参照。要点：`plan-prices-individual`（個人向けの月額・払い方。Pro と Free は料金のページ 2026-10-29 の記録のみ）、任意で `claude-code-in-free-plan`。front matter は related に saving-priorities を足す提案（本文からは指していない）。用語集・prh への提案はなし。

## 検査の結果
- `check_page.py` を 2 回流した。1 回目：エラー 0・警告 3（助詞「に」の重なり 3 件）。直した後の 2 回目：エラー 0・警告 2（助詞「に」「で」の重なり 2 件）。2 件を直したが、流し直す上限に達したため再検査していない。助詞の重なりが残る場合は、箇条 #combining の「超えた分は usage credits の担当」「プランに付く API credits は API キー経由の用途の分」の行を見る

## 確かめていないこと
- 本文の事実は束の写しによる。一次資料は今回開いていない（Web の取得 0 回）。特に Max のモバイル価格の注記、Claude Code が Pro・Max・Ultra で使える点はリンク先の記事の題名と束の写しによる
- 判断例 3 つは架空の状況で、動作確認はしていない。判断例 1 の「月に 1〜2 回なら usage credits で足りる」は経験則で、根拠の印は付けていない
- 「Settings > Usage に Current session の棒がなければ 5 時間の上限がない」は research/22 #32 の写しで、画面は見ていない
- 2 回目の検査の後の textlint の結果（上記の 2 件の修正が効いたか）

## 使用量
- 道具の呼び出し：約 16 回（Read 2・Bash 7・Write 4 ほか）。Web の取得：0 回
