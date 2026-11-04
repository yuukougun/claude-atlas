# write.md：init-and-first-claude-md

## 書いたファイル

- docs/cli/init-and-first-claude-md.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を [cc-docs-memory] に。sections に example・limits・compare・outdated を足した）
- snippets/init-and-first-claude-md/pruned-claude-md.md・pruned-claude-md.expect.yaml
- data/sources.d/init-and-first-claude-md.yml（`sources: []`。新しい出典なし）

## 必ず持つものの対応

- 機能の属性のバッジ：テンプレートが出す。要点の「強制力」は `feature claude-md/enforcement` の目印（冒頭の要点）
- tracks：front matter の `tracks: [claude-md]`（変更なし）
- 1機能1ページ・level：level 整える（変更なし）
- 構成の目安：使いどころ・最小の使い方は #run-init、削る流れは #prune、手で書く流儀との比べは #by-hand、雛形は #example、効かない場面は #limits、比べる相手は #compare、古くなった助言は #outdated

## メインに判断してほしいこと

- 「実践者の幅」に個人・記事の名前を出さず、「ある実践者の記事」と書いた。出典（redreamality・Tembo など）を sources に足すかは未判断
- 要点に「強制力」の項を足した（feature 型の要件）。形が合わなければ直してほしい

## 提案

- なし

## 検査の結果

- エラー 0・警告 4（2 回流した）。残した警告：no-doubled-joshi 3 件（75・90・143 行。75 は link の展開後の題名、ほかは文を短くしたが再検査の回数が尽きて確認できていない）、sentence-length 1 件（77 行の判断例の一続き）。誤検出か本物かは未確認

## 確かめていないこと

- `/init` の挙動は公式 memory 文書（Web の取得 1 回）の記述による。手元で `/init` や `CLAUDE_CODE_NEW_INIT=1` の流れを試していない
- 雛形のコマンド・パスは架空の例。動作は未確認
- 01 2-1 の「CLAUDE.md を /init で作り育てる」は改稿前の版の要約。現行の Best practices は開いておらず、本文は memory 文書の文だけを根拠にした
- 実践者の両論は束の写し（03 Q2 C6・research/25 §3.2）による。原文は開いていない
- ほかの OS と IDE 拡張の `/init` は未確認と本文に書いた

## 使用量

- 道具の呼び出し 約 16 回、Web の取得 1 回
