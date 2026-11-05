# write.md：agent-sdk-basics（feature・api）

## 書いたファイル
- `docs/api/agent-sdk-basics.md`（stubs から移動。stage を draft、updated を 2026-11-05、sections に minimal・templates・pitfalls・compare を足した。既存 4 つの anchor は変えず）
- front matter の `sources`：既存の id を 7 つ（cc-docs-agent-sdk-overview・cc-docs-agent-sdk-migration・cc-docs-agent-sdk-claude-code-features・hc-agent-sdk-plan・hc-api-credits・cc-docs-headless・cc-docs-permission-modes）
- `snippets/agent-sdk-basics/explicit-options.py`・`.expect.yaml`、`isolated-run.ts`・`.expect.yaml`
- `planning/batches/step8/pages/agent-sdk-basics/facts-proposal.yml`
- `data/sources.d/agent-sdk-basics.yml` は書いていない（出典は全部 data/sources.yml にある）

## 必ず持つものの対応
- 機能の属性のバッジ：本文には書かない。テンプレートが tracks（agent-sdk・headless）から出す。ただし data の agent-sdk に `enforcement` がないため、強制力が出るかは未確認（提案を参照）
- `tracks`：front matter に agent-sdk・headless（変更なし）
- 1機能1ページ・節に分ける：#same-and-different・#minimal・#setting-sources・#permissions・#billing・#templates・#pitfalls・#compare
- level：回す（front matter、変更なし）
- 構成の目安：要点（冒頭）→ 使いどころ（#same-and-different。防ぐ原因は縛っていない・境界がない）→ 最小の使い方（#minimal。面のタブ Claude Code・API）→ 雛形（#templates）→ 効かない場面・落とし穴（#pitfalls）→ 比べる相手（#compare）
- 古くなった助言：台帳の行がない（束に outdated_advice なし）ので節を置いていない

## メインに判断してほしいこと
- Web の取得 1 回（claude-code-features）：settingSources の既定は「省くと user・project・local をすべて読む」と文書にある。本文では既定を断定せず「毎回書く」にし、現在の記述は提案の fact にした
- 権限モードの既定と承認の扱いは本文に書かず、headless-basics#permissions を指した。持ち主の側で数値・版なしに現在の挙動を書いてあるかの確認が要る

## 提案
```yaml
frontmatter: []
data:
  - {feature: agent-sdk, key: enforcement, after: "なし（または適切な値）", reason: "feature 型の強制力のバッジのため。Agent SDK は機能全体としては強制力の値が決めにくく、メインが判断する"}
```
- 数値・既定値の提案は facts-proposal.yml
- 用語集：`settingSources` は用語集になく、本文で短く説明した。追加の要否はメインの判断

## 検査の結果
- 1 回目：エラー 11（prh：hooks・subagents・skills・plugins の表記）・警告 6（snippet の expect.yaml の YAML の `@`、ほか textlint）
- 2 回目（直した後）：エラー 0・警告 4。残した警告はすべて link の目印の展開後に出る長い節題の文（sentence-length 3 件、no-doubled-joshi 1 件）による誤検出で、手書きの文に起因しない

## 確かめていないこと
- 雛形 2 つの動作（API の認証が要るので実行していない）。`ClaudeAgentOptions` の引数名と `ResultMessage` の使い方は、公式の文書の例と記憶に基づく
- SDK で `-p` と同じく知らないフォルダのフックが動くか（本文は「未確認」と書いた）
- `allowed_tools` が「確認なしで許す一覧」であり絞り込みではないという書き方の細部
- `onFailure` の指定が Python のコールバックでも使えるか
- 隣のページ（headless-basics・check-billing-path など）の指せる節の中身は、題だけで参照した
- Windows・IDE 拡張の動作

## 使用量
- 道具の呼び出し：約 14 回、Web の取得 1 回
