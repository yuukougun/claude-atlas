# DM2b 報告（数値の目印）

置いた：12ページ・目印 約28（check_page エラー 0）。keeps-stopping は置かず。
- knowledge-cutoff：fact-table model-knowledge-cutoffs（段落を表への案内に直した）
- long-context-first：order-quality-gain・quote-first-length-threshold
- permission-modes-overview：default-interactive・noninteractive
- sandboxing：default-reads・fail-open-default
- search-research-thinking：web-search-call-guide・research-call-guide
- skipped-later-pages：app-pdf-visual-pages・text-only-pages
- textlint-hook：hook-on-failure-block-min-version
- tokens：tokenizer-token-increase-opus-4-7・chars-per-token-earlier-models
- what-survives-compaction：hook-output-max-chars・auto-memory-startup-load・reread-files-max・reread-file-tokens-max
- when-to-start-fresh：clear-after-failed-corrections
- where-your-data-goes：deleted-chat-backend-days・training-opt-in-retention-years・violation-retention・feedback-retention-years・local-transcript-cleanup-days。節 retention の「「30 日」のような」の手書きを外した

置かなかった（status 未確認で、出力が「未確認」だけになり文として読めない）：
- keeps-stopping：auto-mode-no-verdict-display-fixed
- selection-pressure：fishtest-retry-cap（ページ無変更）
- tokens：tokenizer-token-range-opus-5-5
- where-your-data-goes：incognito-retention-period（任意）

注意：skipped-later-pages と search-research-thinking の旧文に残る値の言及は直した。手書きの数字は残していない。警告は既存の助詞・文長のみ。
