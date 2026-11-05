# VF：未確認の数値の確認（2026-11-06）

対象：data/facts.yml で status が 未確認 かつ docs/ に目印のある 46 件。結果は、確認済み 44（うち値を直したもの 5）・確かめられず本文を直した 2。
`uv run python tools/check_pages.py` はエラー 0（警告 4 は以前からのもの）。gen_site.py は流していない（確認済みにした値の目印の中身は、メインがバッチの終わりの gen_site.py で埋める）。

## 取得と道具

- Web の取得：WebFetch 25 回（うち 1 回は agent-sdk の user-input がリダイレクトされて読めなかった）。CHANGELOG は check_noai.py で断る指定がないことを確かめ、1 回だけ curl で取得して scratchpad に置き、手元で grep した。
- 道具の呼び出し：約 60 回（一覧のスクリプト、CHANGELOG の版を引くスクリプト、Edit、check_page、check_pages など）。

## 結果の表

CHANGELOG は https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md（出典 id は cc-changelog）。

| fact の id | 前の値 | 確かめた値 | 結果 | 出典 |
|---|---|---|---|---|
| claude-code-search-truncation-fix-version | 2.1.317 | 2.1.317 | 確認済み | cc-changelog |
| claude-code-p-startup-failure-exit-code-fix-version | 2.1.314 | 2.1.314 | 確認済み | cc-changelog |
| compaction-bugfix-version | 2.1.317 | 2.1.317 | 確認済み | cc-changelog |
| hook-event-count | 33 | 33 | 確認済み | cc-docs-hooks |
| hook-handler-types | 5 | 5 | 確認済み | cc-docs-hooks |
| hook-monitor-min-version | 2.1.314 | 2.1.314 | 確認済み | cc-changelog |
| hook-agent-id-min-version | 2.1.69 | 2.1.69 | 確認済み | cc-changelog |
| subagent-own-model-effort-min-version | 2.1.317 | 2.1.317 | 確認済み | cc-changelog |
| auto-mode-no-verdict-display-fixed | 2.1.314〜2.1.317 | 2.1.314〜2.1.317 | 確認済み | cc-changelog |
| app-default-permission-mode | Auto（個人向けの有料プランと Team）、Manual（Enterprise）。管理者が既定を決められる | Auto（Pro・Max・Ultra・Team）、Manual（Enterprise） | 直した（管理者の部分は記事に書かれず外した） | hc-cowork-and-chat |
| sandbox-default-state | 既定は無効（macOS・Linux・WSL2 で動く） | 同じ | 確認済み | cc-docs-sandboxing |
| at-reference-read-limit | 25,000 トークン以内・256KB 超は含めない | 同じ | 確認済み | cc-docs-common-workflows |
| mcp-output-token-limits | 警告 10,000・上限 25,000 | 同じ | 確認済み | cc-docs-mcp |
| auto-mode-block-pause-thresholds | 連続 3 回または合計 20 回 | 同じ | 確認済み | cc-docs-permission-modes |
| sonnet-4-5-retirement-date | 2026-11-30 | 2026-11-30 | 確認済み | api-docs-model-deprecations |
| mythos-availability | CVP と LSVP 経由のみ。米国の組織に限る | 信頼されたアクセスの制度を通した、米国の一部の組織に限る。LSVP では使える。CVP は今は Opus・Sonnet 級で、Mythos 級は今後 | 直した | anthropic-fable-mythos-5-1 |
| ultrathink-raise-min-version-vscode | 2.1.316 | 2.1.316 | 確認済み | cc-changelog |
| ultrathink-raise-target-and-models | xhigh。Opus 5.5・Sonnet 5.5・Haiku 5.5・Fable 5.1（API） | 同じ（2.1.311） | 確認済み | cc-changelog |
| ultrathink-disable-env-min-version | 2.1.316 | 2.1.316 | 確認済み | cc-changelog |
| ask-user-question-limits | 1〜4 問、選択肢 2〜4、header 12 文字 | 確かめられず | 確かめられず本文を直した | （Tools reference に記載なし。Agent SDK の文書は取得の上限で読めず） |
| ask-user-question-timeout | 60s・5m・10m | 同じ | 確認済み | cc-docs-tools-reference |
| idle-compaction-min-tokens | 200,000 | 200,000（200K） | 確認済み | cc-changelog |
| idle-compaction-wait | 約 1 時間 | 約 54 分 | 直した | cc-changelog |
| idle-compaction-terminal-version | 2.1.299 | 2.1.299 | 確認済み | cc-changelog |
| idle-compaction-ide-version | 2.1.314 | 2.1.314 | 確認済み | cc-changelog |
| key-transcript-and-background | Ctrl+O・Ctrl+B | 同じ | 確認済み | cc-docs-interactive-mode |
| skill-description-rebuild-min-version | 2.1.304 | 2.1.304 | 確認済み | cc-changelog |
| managed-agents-session-hour-price | $0.08 | $0.08 / session-hour（running の間） | 確認済み | api-docs-pricing（出典を managed-agents の overview から変えた） |
| chat-sharing-invite-expiry | 30 日 | 30 日 | 確認済み | hc-share-people |
| top-model-by-plan | プランごとの引かれ先 | 確かめられず | 確かめられず本文を直した | （4 つの出典を読む取得の上限で読めず） |
| computer-use-requirements | macOS・Windows の Desktop。Pro・Max・Ultra。Team・Enterprise は対象外（beta）。投資・取引・暗号資産は既定でブロック | 同じ | 確認済み | hc-computer-use |
| scheduled-tasks-schedule-warning-version | 2.1.317 | 2.1.317 | 確認済み | cc-changelog |
| setting-sources-leak-fix-version | 2.1.314 | 2.1.314 | 確認済み | cc-changelog |
| prompt-cache-min-length | 512 から 4,096 トークン | 同じ | 確認済み | api-docs-prompt-caching |
| prompt-cache-max-breakpoints | 4 つ | 4 つ | 確認済み | api-docs-prompt-caching |
| feedback-transcript-share-retention-months | 6 か月 | 6 か月 | 確認済み | cc-docs-data-usage |
| refusals-auto-switch-default | アプリ・Claude Code 有効。API は fallbacks（beta） | 同じ | 確認済み | hc-switched-models・cc-docs-model-config・api-docs-refusals |
| refusals-cc-per-category-switch-min-version | 2.1.219 | 2.1.219 | 確認済み | cc-docs-model-config |
| refusals-api-categories | cyber・bio・frontier_llm・reasoning_extraction・general_harms（または null） | 同じ | 確認済み | api-docs-refusals |
| refusals-billing-by-category | 課金される分類は bio・frontier_llm・reasoning_extraction（アプリの記事では distillation）… | 「アプリの記事では distillation」を外した以外は同じ（2026-09-24 に再開。2026 年に何度か変わった） | 直した | api-docs-refusals・api-release-notes |
| refusals-cvp-tiers | 3 段階。個人は Defense だけ | 同じ | 確認済み | hc-cyber-verification-program |
| reasoning-extraction-since | 2026-06-09 | 2026-06-09 | 確認済み | api-release-notes |
| usage-credits-expiry-japan | 購入から 6 か月（2026-09-10 以降の購入分） | 購入から 6 か月（2026-09-10 から。日本などの地域） | 直した（「購入分」は記事に書かれず外した） | hc-usage-credits |
| message-threads-lifetime | 最後の要求から 5 分で切れ、最後に使ってから 1 時間以内に消える | 同じ | 確認済み | api-docs-message-threads |
| edit-refuses-non-utf8-since | 2.1.296 | 2.1.296 | 確認済み | cc-changelog |
| write-refuses-non-utf8-since | 2.1.299 | 2.1.299 | 確認済み | cc-changelog |

## 確かめられなかった 2 件と、直した本文

- ask-user-question-limits：docs/prompting/let-claude-ask.md の 72 行目。目印を外し、「上限の値は、この辞書では確かめていないので、公式の文書で見る」とした。
- top-model-by-plan：docs/models/choosing-a-model.md の 120 行目。目印を外し、プランごとの扱いの中身を書かない形にした。
- どちらも check_page.py はエラー 0・警告 0。facts.yml の項目は 未確認 のまま、note に今回の経過を書いた。次に確かめるなら、前者は https://code.claude.com/docs/en/agent-sdk/user-input（sources に足す）、後者は hc-fable-models-plan・claude-pricing・hc-max-plan・hc-ultra-plan の 4 つ。

## メインへの提案・気づき

- gen_site.py：確認済みにした 44 件の目印の中身（まだ「未確認」と見える）は、バッチの終わりの gen_site.py で埋まる。値を直した 5 件（app-default-permission-mode・mythos-availability・idle-compaction-wait・refusals-billing-by-category・usage-credits-expiry-japan）は、その文が自然に読めるか、再生成の後に見てほしい。
- data/sources.yml（共有のため触れていない）：今回読んだ出典の checked を 2026-11-06 に上げてよい。managed-agents-session-hour-price は出典を api-docs-pricing（sources.yml に既にある）に変えた。
- default-safety-settings の本文にある「既定はプランと管理者の設定で変わりうる」の「管理者」は、今回の出典（Cowork and Chat の記事）が書いていない。ほかの出典で裏づけるか、「プラン」だけにするかの判断が要る（このページには触れていない）。
- 研究資料にあった「idle compaction は約 1 時間」は誤りで、CHANGELOG は約 54 分（1 時間のキャッシュが切れる前）と書く。
- cc-docs-hooks は 28 万字あり、前半 10 万字しか読めていない（今回の項目は前半で確かめられた）。
- 止められた操作はなかった。
