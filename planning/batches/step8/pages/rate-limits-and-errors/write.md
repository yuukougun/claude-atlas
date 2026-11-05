# write.md：rate-limits-and-errors（執筆）

## 書いたファイル
- `docs/api/rate-limits-and-errors.md`（stubs から mv。stage を draft、updated を 2026-11-05。sections に `cause`・`misconceptions` を足した。sources に api-docs-rate-limits・api-docs-errors・cc-docs-errors・api-docs-refusals・api-release-notes を入れた）
- `data/sources.d/rate-limits-and-errors.yml`（`sources: []`。新しい出典はない）
- `planning/batches/step8/pages/rate-limits-and-errors/facts-proposal.yml`（数値の提案 2 件）
- 雛形・図ファイルはなし。図は本文の Mermaid（流れ図）。目次の templates が「なし」で、コード例とパラメータの一覧は公式へ任せる notes に従った

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle を名指す）：`#cause`（確かめる・握る）。prevents は空なので原因は名指さず、容量と上限の問題で設定の誤りとは別の層、と書いた
- level（仕組みにする）：front matter。要点の最初は「何が分かるか」
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：何が起きるか＝`#kinds`・`#limit-types`、なぜ・設計＝`#retry`・`#reduce-pressure`、振り分け＝`#non-error-stops`・`#in-claude-code`、何に効くか＝`#cause`、誤解＝`#misconceptions`、関連＝テンプレート

## メインに判断してほしいこと
- 追加した節 `cause`・`misconceptions` を sections に入れたのでよいか。prevents が空のため、原因は名指さなかった
- 再試行の「間隔にばらつきを足す」は公式にない定石で、「この辞典の推奨」と明記した。残してよいか
- 「再試行の層を重ねない（回数が掛け合わさる）」は（推論・実践例なし）の印を付けた

## 提案
- 数値の提案は `facts-proposal.yml`（SDK の自動の再試行の既定、Claude Code の自動の再試行の既定）。本文は数字なしで読める形にしてあり、承認後に目印を `#retry`・`#in-claude-code` へ置ける
- front matter の提案：なし

## 検査の結果
- 1 回目：エラー 0・警告 8。直した後の 2 回目：エラー 0・警告 3
- 残した警告 3：111 行（ヘッダー名のコードが長く、文の長さが超える）、114 行と 128 行（助詞の重なり。読みにくくないと判断）

## 確かめていないこと
- Claude Code の errors のページは 1 回の取得で先頭 10 万字だけを読んだ。利用枠の節（usage limit）は読めていない
- Platform の文書は 2026-11-05 の取得で確かめた。message threads の記述は束の research/22 #40 の写しによる（原文は未取得）
- 拒否の fallback の公式の文書（api-docs-refusals）は本文の中でリンクを付けず、言及だけにした。stop_reason の値 `refusal`・`max_tokens` は束の写し（02 §5-4・research/26）による
- Claude Code のほかの OS・IDE 拡張の動作は未確認

## 使用量
- 道具の呼び出し 約 20 回、Web の取得 3 回
