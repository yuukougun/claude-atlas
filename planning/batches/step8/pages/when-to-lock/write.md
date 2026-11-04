# when-to-lock 執筆の報告

## 書いたファイル

- `docs/enforce/when-to-lock.md`（stub から移した。front matter の変更：`stage` を draft、`updated` を 2026-11-05、`sources` に既存の 7 件〔cc-docs-features-overview・cc-docs-permissions・cc-docs-permission-modes・cc-docs-best-practices・cc-docs-memory・cc-docs-hooks-guide・cc-docs-context-window〕、`sections` に where-to-move・effects・misconceptions を足した）
- `snippets/when-to-lock/deny-git-push.json`・`.expect.yaml`（settings。目次の templates の案）
- `snippets/when-to-lock/reason-for-push-in-claude-md.md`・`.expect.yaml`（claude-md。鍵に移した後の CLAUDE.md の行。分かりやすさのために足した）
- `data/sources.d/when-to-lock.yml` は作っていない（新しい出典なし）

## 必ず持つものの対応

- 冒頭の要点：abstract の「何が分かるか」が最初の項目。
- どの原理に関わるか（`principle`＝縛る）：`#effects` の冒頭で「縛る」と名指しした。
- どの原因に関わるか（`prevents`＝縛っていない・散らかっている）：`#effects` の 2 項目で名指しした。
- `pitfalls`：front matter が空なので、持たない。
- level（任せる）：front matter に持つ。
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解）：何が起きる＝`#signals`・`#spoken-rules-fade`（判断例付き）、なぜ＝`#spoken-rules-fade`、何に効くか＝`#effects`、誤解＝`#misconceptions`。図（流れ図）は `#signals`。

## メインに判断してほしいこと

- 面ごとのタブは置かなかった。材料に app・api の鍵の手段がなく、`#where-to-move` で `request-lock-table#by-surface` を指すだけにした。
- 判断例「小さな直しにとどめて」は、材料（design §10.5 の判断を含む規則の例）から一般化した例で、公式の事例ではない。不要なら外してよい。

## 提案

なし。

## 検査の結果

- 1 回目：エラー 1（prh：auto mode → auto モード）・警告 5。直した。
- 2 回目：エラー 0・警告 2。残した理由：`#spoken-rules-fade` の 78 行は、リンク先の題名「何が残り、何が消えるか」の「が」が重なるもの（題名は直せない）。125 行は助詞「に」の重なりで、誤検出に近いが、文の読みやすさは許容と判断した。

## 確かめていないこと

- 雛形の deny ルール `Bash(git push *)` の書き方と、止まる動作は、実機で試していない（束の材料と記憶による。公式の permissions の文書で書式の確認を要する）。
- 圧縮の後に deny ルールが効き続けることは、束の data の note（公式の記述）による。実機では未確認。
- アプリ・API の面で使える鍵は書いていない（`request-lock-table#by-surface` に任せた）。Windows など WSL・Linux 以外は未確認。
- 見出し・リンク先の節の本文は読んでいない（束の要約だけで指した）。

## 使用量

道具の呼び出し 11 回前後、Web の取得 0 回。
