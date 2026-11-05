# XC10 整合性の確認（8ページ）

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 直したほうがよい | rate-limits-and-errors#reduce-pressure | message threads の成熟度「beta」を手書き（持ち主 stateless-messages-api は data の目印）。持ち主への link もなかった | 成熟度を `gen feature message-threads/maturity` の目印にし、持ち主へ link を付けた |
| 軽い | long-running-agent-context | prompt-caching-in-practice#invalidation は「履歴の要約・古い発言の削除で先頭の一致が崩れる」と書くが、compaction・context editing の節にキャッシュへの影響の言及がない（矛盾ではなく欠落） | 直さず（下記） |
| 軽い | tool-use-loop#forcing | strict を「必ず合う」と書く。structured-outputs-basics#not-guaranteed は refusal・max_tokens で崩れる場合を挙げる。同じ節に「縛られるのは形」の注意があり、矛盾とまでは言えない | 直さず |

そのほか、次は互いに合っていた：鍵（強制力）の扱い（structured-outputs は data の目印、tool-use-loop は tool_choice・strict を鍵側と説明）、tool_choice 強制がモデルで使えない件、キャッシュの順序（tools・system・messages）と無効範囲、effort 変更の影響、寿命・区切り数・最小長は fact の目印、message threads は送る量だけが減る点（stateless・rate-limits）、SDK の自動再試行。

## メインに決めてほしいこと
- long-running-agent-context に「compaction・context editing はキャッシュの先頭を崩す」旨を一文足すか（足すなら prompt-caching-in-practice#invalidation へ link）。

## check_page.py
- rate-limits-and-errors：エラー0・警告3（既存の textlint 警告）。ほかのページは直していないので未実行。

## 道具の呼び出し
約 16 回
