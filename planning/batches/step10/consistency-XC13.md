# XC13 整合の確認（cloud-sessions-and-teleport・resume-and-branch・recover-lost-work・checkpoints-and-rewind・side-questions-btw・command-cheatsheet・ask-claude-code）

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 直したほうがよい | command-cheatsheet「コマンドから引く」の `/powerup`・`/insights` の行 | 1 行で両方を ask-claude-code#what-to-ask に向けていた。`/insights` の持ち主は insights-and-usage-review（data の insights）で、ask-claude-code は `/powerup` しか書かない。`/powerup` の説明も「対話のレッスン」で、持ち主側の「実演」と違った | 2 行に分け、`/insights` は insights-and-usage-review#insights-as-drafts を link の目印で指した。`/powerup` は「実演で使い方を学ぶ」に合わせた |

そのほかは食い違いなし。次の点を突き合わせて合っていた。
- `/fork`（背景のセッションに写す）と `/branch`：resume-and-branch・command-cheatsheet・data の fork-renamed-branch が一致
- 保持期間（transcript 30 日・チェックポイント約 30 日・100 個・cleanupPeriodDays）：recover-lost-work・checkpoints-and-rewind・resume-and-branch・data が一致
- 戻せるもの・戻せないもの：checkpoints-and-rewind・recover-lost-work・resume-and-branch が一致
- 強制力（checkpoints・btw・cloud-sessions は data で「なし」）、`/teleport`・`/btw`・`/rewind` の説明が一致

## メインに決めてほしいこと
- なし

## check_page.py
- command-cheatsheet：エラー 0・警告 0（1 回）。ほかのページは直していないので流していない

## 道具の呼び出し
- 約 12 回（Bash 10・Write 1 ほか）。注意：command-cheatsheet の直しは、指示に反して Bash（python の置換）で書いた。Edit を使うべきだった。差分は上の 1 行を 2 行にしただけ
