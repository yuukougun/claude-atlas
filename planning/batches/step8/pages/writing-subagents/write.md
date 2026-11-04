# write.md：writing-subagents（feature・extend）

## 書いたファイル
- `docs/extend/writing-subagents.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources に cc-docs-sub-agents・cc-docs-best-practices・cc-docs-commands・cc-docs-hooks・cc-changelog・api-docs-prompting-opus-5 を足した。sections に pitfalls・compare・outdated を足した。既存の anchor は変えていない）
- `snippets/writing-subagents/`：ask-claude-to-define（prompt）・reviewer（subagent）・test-runner（subagent）と、それぞれの `.expect.yaml`
- 新しい出典のファイル `data/sources.d/writing-subagents.yml` は置いていない（使った出典の id はすべて既存）

## 必ず持つものの対応
- 機能の属性のバッジ：冒頭の要点の「強制力」の項目（成熟度・読み込みの時期・コンテキストのコストは feature の目印）。強制力は data が「書かない」としているので、目印を使わず、お願いと鍵が混ざることを手で書いた
- `tracks`：front matter の `tracks: [subagents]`（変更なし）
- level：front matter の `level: 仕組みにする`（変更なし）
- 使いどころ（どの原因を防ぐか）：#when-to-use
- 最小の使い方（面のタブ）：#define（タブ「Claude Code」。surfaces は claude-code だけ）
- 雛形：#define（ask-claude-to-define）・#tools-and-model（reviewer・test-runner）
- 効かない場面・落とし穴：#pitfalls
- 比べる相手：#compare
- 古くなった助言：#outdated（台帳の 4 行を link で指した）

## メインに判断してほしいこと
- 台帳への link `outdated-advice-ledger#<行の id>` が、4 行とも check_page で通った。ページの id と anchor はこの形で合っていた（確認のみ）

## 提案
- 数値の提案：なし。同時実行数・ネストの深さ・skills の上限・入った版は本文に書いていない（環境変数の名前だけ書いた）
- 用語集・prh：「フロントマター」の表記が prh で要求された（front matter は不可）。用語集にあるので、変更の提案はない

```yaml
frontmatter: []
```

## 検査の結果
- 書き終えた後：エラー 2（prh：front matter・hooks）、警告 1（一つ）。直した後：エラー 0・警告 0

## 確かめていないこと
- 事実は束の材料（01 E-1・4-2・23 §3.1・§3.7・22 #21・28 #1・#2・#14・05 1-13）からだけ書いた。一次資料（公式の文書）は開いていない（Web の取得 0 回）
- 「`tools` を書かないと本体と同じ道具を引き継ぐ」（reviewer.expect.yaml の control）は束にない。公式の文書の記憶に基づくので、検証側で出典に当ててほしい
- 「Bash を許した担当はシェルから書き込める」は一般的な理解に基づく推論で、束に直接の記述はない
- `effort` の挙動（別のモデルの担当は effort を受け継がない・`CLAUDE_CODE_SUBAGENT_EFFORT`）は更新履歴の記述（research/22 #21）で、公式の担当の文書には記述がない旨を本文に書いた
- `@"X (agent)"` の書き方・`claude --agent X`・`--agents` の JSON・プラグインでの配り方は research/01 E-1 の記述で、動作は試していない
- 雛形 3 つの動作（呼ばれること・編集できないこと・件数の報告）は試していない。test-runner の `model: haiku` は例
- WSL・Linux 以外の OS と IDE 拡張の動作は確かめていない

## 使用量
- 道具の呼び出し：約 14 回（Read 3・Bash 5・Write 8 ほか）、Web の取得 0 回、check_page 2 回
