# write.md：always-on-costs（concept・context）

## 書いたファイル
- docs/context/always-on-costs.md（stubs から mv）。front matter の変更：stage を draft、updated を 2026-11-05、sources に既存 id 8 件（features-overview・context-window・memory・skills・mcp・large-codebases・how-claude-code-works・best-practices）、sections に why-small・effect・misconceptions を足した（既存の anchor は不変）
- 雛形・図・data/sources.d は作っていない（目次の templates・visual が「なし」。新しい出典もなし）

## 必ず持つものの対応
- どの原理に関わるか（principle「見せる」）：#effect
- どの原因に関わるか（prevents「散らかっている」「合っていない」）：#effect
- pitfalls：front matter が空なので本文に名指しなし
- level（任せる）・要点の最初は「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#resident-vs-on-demand → #why-small → #effect → （#reduce は目次の指定の節）→ #misconceptions → 関連はテンプレート。比喩付きの図は置いていない（持たない理由：文章の比喩〔広い机〕で足りると判断。必要なら図の追加をメインが判断）

## メインに判断してほしいこと
- 図なし：型の目安にある「比喩付きの図」を置かなかった
- #why-small の「2026-11-03 に確かめた現行の Best practices が『コンテキストを最大の制約として管理する』をやめてよい表に挙げる」は、束の research/23 §3.1 の写しに基づく。一次資料は未確認なので、検証の担当に確認してほしい
- #reduce の順（測る→外す→CLI→スキル→paths→CLAUDE.md→フック）は「この辞典の推奨」と明記した（公式の順ではない）

## 提案
- 数値の提案なし（数値を本文に書いていない）。feature の目印で load_timing・context_cost を指した
- front matter の変更提案なし

## 検査の結果
- 1 回目：エラー 1（本文の「skill」→スキルに修正）・警告 4。2 回目：エラー 0・警告 3
- 残した警告：textlint の no-doubled-joshi が 2 件（49・59 行。文の構造上、直さず）。gen_site の警告 1 件は inspect-context#baseline の見出しがまだ本文にない（相手が stub のため。公開までに解消される見込み）

## 確かめていないこと
- 一次資料（公式文書）を開いていない。本文の事実は束の data（確認日 2026-11-04）と調査資料の写しによる
- ツール検索が使えない配置での MCP の挙動、Windows・macOS・IDE 拡張の挙動は未確認
- 「MCP より CLI」を多数とする点は束の 03 Q4 Takeaway（実務家の一致）による（根拠：中）
- 2 つの textlint 警告は検査の回数の制限のため再検査していない

## 使用量
- 道具の呼び出し 9 回ほど（Read 3・Bash 5・Write 2）、Web の取得 0 回
