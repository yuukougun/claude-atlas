# write.md：suggest-or-do（提案してほしいのか、実行してほしいのか）

## 書いたファイル

- docs/prompting/suggest-or-do.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 4 件に。sections に `why`・`limits` を足した。既存の 3 つの anchor は変えていない）
- snippets/suggest-or-do/default-to-action.txt・wait-for-instructions.txt・stop-and-discuss.txt と、それぞれの .expect.yaml
- data/sources.d/suggest-or-do.yml は作っていない（使った 4 件の出典は data/sources.yml にある）

## 必ず持つものの対応

- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の囲み
- 技法の構成（Before/After → 何が変わるか → なぜ効くか → 効かない場面・やりすぎ）：`verbs`（Before/After と、After の注記・動詞の表）→ `why` → `limits`
- 原理 `principle: 見せる` を本文で名指す：`why`（および冒頭の囲みの 4 つ目の項目）
- 原因 `prevents: 見えていない・合っていない` を本文で名指す：`why`（2 つの箇条）
- `pitfalls`：front matter にキーがないので持たない
- level（整える）：front matter のとおり

## メインに判断してほしいこと

- 本文にモデル名を書かなかった（モデル名は目印で書く決まりのため）。「公式のモデル別の指針」と言い、出典の一覧に頼った。読者に具体名が要るなら、names の目印を使う案を決めてほしい
- 「止まって議論する」書き方は、束の 11 第2節のとおり（推論・実践例なし）の印で書いた。最新のモデル別の指針に同じ記述があるかは未確認と本文にも書いた

## 提案

- 用語集：「system prompt」は prh でエラーになるので、本文は「システムプロンプト」にした。`default_to_action` などのタグ名は用語集に載せなくてよい
- 前提のページ four-specifics の「完了」へ link を張った（four-specifics#done）

## 検査の結果

- 1 回目：エラー 1（system prompt の表記）・警告 8。直した後：エラー 0・警告 4
- 残した警告 4：no-doubled-joshi（47 行の「と」「が」、157 行の「に」、200 行の「にも」）。引用の「」や並列で、文を割ると読みにくくなるため残した

## 確かめていないこと

- アプリで既定の指示を保存して使い回す場所の手順（本文に「確かめていない」と書いた）
- Claude Code の CLAUDE.md に `<default_to_action>` を書いたときの効き方（公式の指針は system prompt 向け）。雛形の expect は未実行
- Opus 5 の推奨スコープ指示の原文と、最新版の指針との差（束の写しだけに基づく）
- 「相談のつもりで書くと書き換えられる」ことの頻度は測っていない。本文は「ことがある」にとどめた

## 使用量

- 道具の呼び出し 15 回ほど。Web の取得 0 回
