# write.md：research-in-subagents（執筆）

## 書いたファイル
- docs/context/research-in-subagents.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 6 件）
- front matter で変えたキー：`sections`（`effects` 何に効くか・`misconceptions` 誤解 を足した。when・how・cost は変えていない）・`stage`・`updated`・`sources`
- snippets/research-in-subagents/delegate-research.md と delegate-research.expect.yaml（目次の templates の案どおり）
- data/sources.d/research-in-subagents.yml は書いていない（出典は既存の id だけ：cc-docs-sub-agents・cc-docs-best-practices・wb-cc-best-practices-2026-10-27・api-docs-prompting-opus-5・cc-docs-costs・anthropic-eng-effective-context-engineering-ai）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle` 見せる・`prevents` 散らかっている を本文で名指す）：`#effects`
- `pitfalls` は空なので名指すものはない（`#misconceptions` で台帳の 3 行を指した）
- level（任せる）：front matter。要点の最初の項目は「何が分かるか」
- 構成（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：何が起きるか・なぜ（別室の部下の比喩）は `#when`、頼み方の Before/After は `#how`、何に効くかは `#effects`、費用は `#cost`、誤解は `#misconceptions`。関連はテンプレートが出す。なぜの節と図は、薄くなるので独立させず `#when` の導入に入れた（図なし）

## メインに判断してほしいこと
- `sections` に 2 節を足した。不要なら外すが、`#effects` は concept の必須（原理・原因の名指し）を置く節
- `#cost` で、公式の頼み方の手引きの題名（Prompting Claude Opus 5）にモデル名が入る。本文でモデル名を目印なしに書くのは避けたので、題名のリンクとして 1 回だけ出した
- `outdated-advice-ledger#<行の id>` の link が未公開の相手を指す場合の表示は道具に任せた（検査は通った）

## 提案
- 数値の提案なし（本文に数値・既定値を書いていない。環境変数の名前だけを書いた：data の台帳 tell-it-to-use-subagents の now と同じ）
- 用語集・prh・front matter への提案なし

## 検査の結果
- 1 回目：エラー 0・警告 3（文の長さ 1・助詞の重複 2）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- 事実は束の材料（台帳・調査資料の写し）に基づく。一次資料は開いていない（Web の取得 0 回）。Explore が読み取り専用であることと徹底度を指定できること、`/usage` でサブエージェントの種類ごとに見られること、環境変数の名前は、束の写し（03 X6・台帳）に頼っている
- 「新しいサブエージェントは文脈を集め直すので、かえって遅くなることがある」「同じ作業を渡しても答えはよくならない」は 05 1-13 の写しから
- 本文の判断例 2 つと Before/After は書き手の例で、実機で動かしていない。雛形も動作を確かめていない
- 実機の Explore の挙動、WSL・Linux 以外の動作は未確認

## 使用量
- 道具の呼び出し：約 12 回（Read 2・Bash 7・Write 4 ほか）。Web の取得：0 回
