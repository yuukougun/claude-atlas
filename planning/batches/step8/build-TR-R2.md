# TR-R2 報告

- 直したページ：3ページ3件（model-based-grading：採点役の例の分け方の文に（推論・実践例なし）を付け、related に misses-broken-evaluation を追加。isolate-with-safe-mode：summary を本文に合わせて直した〔120字以内〕）。雛形 snippets/check-billing-path/check-no-api-key.sh：手順 3 で見つけたときも found=1 にした（check-billing-path のページ）。check_page は3ページともエラー0
- 直さなかったもの：数値の提案、強制力・用語集・出典の差し替え、図の要否、警告は先例どおり
- backlog.md に足した：「推奨R2」節（数値の提案15行、強制力の値の案11機能、用語集13語、道具・data の形ほか約10項）
- rec2-decisions.md：12行
- 4 の確かめ（template_keys.yml）：3行とも、行の形（`- キー名` を列に揃え、`#` の後ろに出典と確認日を書く）と注の書き方（公式の settings-reference の一覧・Scope・2026-11-05 にメインが確認）は既存の行に合う。enabledPlugins・extraKnownMarketplaces は settings 直下の列、allowUnsandboxedCommands は sandbox の列で、置き場所も正しい。気づき：既存の注は多くが「research/28 #n」形式で、新しい 3 行は文章の注。ほかの行（statusLine など）とは同じ形なので問題なし
- check_page.py：エラー0（3ページ。警告は既存の助詞の重なりなど）
- Web の取得：0回
- 道具の呼び出し：約16回
- 止められた操作：なし
