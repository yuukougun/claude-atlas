# build-TR3：バッチ3の終わりの扱い

## 直したページ（17ページ）
- バッチ3：fix-a-bug・does-more-than-asked・goal-until-done（related 追加。does-more-than-asked は推論に印も）、learning-with-ai（題・要点の「速く進む」を弱めた）、human-pitfalls（Buçinca の要旨を arXiv で確認し日付を添えた）、secrets-exposed（GitHub の文書で確認。.gitignore の観点に印）、hits-limits-quickly（アプリの数え方に「辞典の推奨」の印）。deleted-something-important は git restore を git-scm で確認（直し不要）
- 持ち越し8件：product-map（直し不要。名前の目印は済み、手がかり4項目は束に基づく）／knowledge-map（3通りの見方に直した）／rereads-whole-history（URL を確認してリンクと source を足し、gen_site --page）／independent-review（引用を言い換え）／measure-changes（計算で確認、誤りなし）／selection-pressure（53件中16件を削除、「4〜5回」を数字なしに）／what-auto-mode-stops・protect-tests（data に強制力の属性がないので backlog へ。ページは直さない）／prompt-injection-in-practice（WhatsApp の確認画面の細部を削除）
- 先例で「何もしない」：destructive-commands（Opus 4.6 はすでに無い）ほか多数

## backlog に足した件数
約 40 行（数値の提案 10 行・用語集 6・道具と data の形 7・調べる担当 4 行・出典 4 件）。節「バッチ3の終わり（TR3）で足したもの」

## batch3-decisions.md
14 行

## check_page.py
直した全ページでエラー 0（警告は残るものあり）。1ページ2回までを守った

## 使用量
Web の取得 4 回（context-window・arXiv 2102.09692・git-scm の git-restore・GitHub 文書）。道具の呼び出し 約 50 回
