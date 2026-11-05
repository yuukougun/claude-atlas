# write.md：refactor-and-migrate（執筆）

## 書いたファイル

- `docs/recipes/refactor-and-migrate.md`（`stubs/recipes/` から mv。stage は draft）
- front matter で変えたキー：`sections`（先頭に `guards-first`、末尾に `when-it-fails` を足した。既存4節の anchor は変えず）・`sources`（cc-docs-common-workflows・cc-docs-best-practices・cc-docs-goal・cc-docs-workflows・cc-docs-worktrees。いずれも既存の id）・`stage`（draft）・`updated`（2026-11-05）
- `snippets/refactor-and-migrate/migration-request.{txt,expect.yaml}`（挙動を保つ移行の依頼）
- `snippets/refactor-and-migrate/goal-stop-conditions.{txt,expect.yaml}`（/goal の停止条件。A-14 を直し、git status の出力を会話に出させる）
- `data/sources.d/` は作っていない（新しい出典なし）

## 必ず持つものの対応

- 手順：`#small-steps`（計画→基準→1 単位の変更→比較→コミット。段ごとの終わった印の表と図、依頼の雛形）。多数への展開の手順は `#bulk-changes`、無人の回し方は `#goal-stop-conditions`
- 確かめる・縛るのページへの道（比例則）：`#guards-first`（working-with-git・pitfalls-of-ai-written-tests・differential-testing・verification-ladder・protect-tests・freeze-eval-assets を先に指す）。front matter の prerequisites と related は束のまま
- 構成の目安（要点→先に整える守り→手順→確かめ方→失敗したとき）：`#guards-first`→`#small-steps`→`#behavior-preserved`→`#bulk-changes`・`#goal-stop-conditions`→`#when-it-fails`
- level：front matter に「任せる」。回す・仕組みにするは節の level で保った

## メインに判断してほしいこと

- 雛形 `goal-stop-conditions` の末尾 `or stop after <上限のターン数> turns` は束の 11 §4 #23 の構文を写した。構文と判定の仕様は版依存なので、確認日と版は本文の compare 表（goal の入った版・確認日）と goal-until-done への誘導で担保した。構文自体の fact を数値ファイルに置くか、判断を願う
- compare 表は成熟度が全行共通で表から外れ、「すべて共通」の行に出る。recipe に compare の目印を置くのが型の方針に合うかを確認してほしい（tracks の3機能の版と確認日を出すために使った）

## 提案

```yaml
frontmatter: []
```

- 用語集・prh・data への提案はなし
- 補足：`#goal-stop-conditions` は「止まる条件と上限を先に決める」「`-p` で回すときはターン数と費用の上限を指定する」と書いた。値は書いていない（束の ralph-loops の how_to_find が根拠）

## 検査の結果

- 1 回目：エラー 0・警告 9（max-ten・no-doubled-joshi・sentence-length）。直した後の2回目：エラー 0・警告 1
- 残した警告：127 行目（判断例「理由」の「が」の重複）。文を変えると判断例の流れが崩れるため、検証と直しの担当に委ねる
- 目印の間は gen_site.py が埋めた（link・snippet・compare・feature・page-links・references）

## 確かめていないこと

- 雛形2つの動作は確かめていない（道具が「確かめていない」旨を書く）。/goal の構文は束の写しによる
- 公式のブログ「how Anthropic runs large-scale code migrations」は URL を持たず、読んでもいない。本文は「公式のブログへの案内にとどまる」とだけ書いた
- Common workflows の挙動は、束の調査資料の写し（01 KQ3）に基づく。一次資料は開いていない
- 判断例（単位の切り方・落ちたテスト）と「単位ごとの終わった印」の表は、束の材料から組んだ筆者の提案で、実践例による裏づけはない
- 「ターン数と費用の上限を指定する」の具体的なオプション名は書いていない（公式の cli-reference を開いていない）

## 使用量

- 道具の呼び出し：約 17 回（Read 4・Bash 6・Write 6・Edit 6 の概数）。Web の取得：0 回
