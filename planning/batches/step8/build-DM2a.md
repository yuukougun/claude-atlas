# DM2a 報告（数値の目印）

11ページすべて check_page.py は1回、エラー 0（警告は文長・助詞の重なりのみ）。

置いた：fact の目印 30 個、fact-table 2 組（usage-limit-types-by-plan、wrap-up-allowance-frequency）。置かなかった：0 個の行（表の 34 行中、model-knowledge-cutoffs だけ下記）。

- 未確認の項目（出力が「未確認」の一語になる）は、括弧・「は、〜」の形に置いて、文として読めるようにした。確認済みになれば値の文に替わる。
  at-reference-read-limit、search-truncation / p-startup の版、sandbox-default-state、app-default-permission-mode、incognito-retention-period、hook-event-count、hook-handler-types、hook-monitor-min-version、hook-agent-id-min-version、compaction-bugfix-version
- doesnt-know-latest：行「現行のモデル」・列 training の1セルだけを置いた（reliable のセルは note が長く文に入らない）。reliable は置かず、文で公式の文書に任せた。
- how-memory-works #chat-search：chat-search-plans の値が「customer-managed … 使えない」まで含むので、手書きの同じ文を削った。
- how-usage-limits-work #limit-types：表の直後に、手書きの箇条（Pro/Max/Ultra…）が残る。表と重なるので、箇条を削るかは作者・メインの判断。
- evidence-not-reports：「直った版は CHANGELOG で確かめる」を「各項目に書く」に直した。
- going-in-circles：目印を「切り替えの目安」として括弧に置いた（「重なっても」の文には埋めていない）。
- 提案：default-safety-settings の permission-mode-default-* の出力が長い（括弧入り）。文長の警告が出た。
