# write.md：dynamic-workflows（feature・delegate）

## 書いたファイル
- docs/delegate/dynamic-workflows.md（stubs から移動。stage を draft、updated を 2026-11-05、sources に cc-docs-workflows・cc-docs-agents・cc-docs-sub-agents・cc-docs-permissions・cc-docs-sandboxing・cc-docs-costs・cc-changelog。sections に minimal・templates・pitfalls・compare・outdated を足した。既存の 2 つの anchor は変えていない）
- snippets/dynamic-workflows/scoped-trial.md と .expect.yaml（目次の案の「範囲を絞って試す依頼」）
- snippets/dynamic-workflows/scoped-migration.md と .expect.yaml（足した雛形。隔離したコピーでの移行の依頼）
- planning/batches/step8/pages/dynamic-workflows/facts-proposal.yml（数値の提案 4 件）
- data/sources.d/dynamic-workflows.yml は作っていない（新しい出典なし。既存の id だけを使った）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。本文には成熟度と入った版を `gen:begin feature workflows/...` で冒頭の導入に置いた（強制力は下の「メインに判断してほしいこと」）
- tracks（workflows・effort）：front matter のまま。`workflows` の属性を導入で使った
- 要点（強制力・確認日と版のバッジ）：冒頭の「要点」と導入（強制力の代わりに「止められるもの」を置いた）
- 使いどころ（どの原因を防ぐか）：#when-and-start-small
- 最小の使い方（面のタブ）：#minimal（面は claude-code だけなので、タブは 1 つ）
- 雛形：#templates
- 効かない場面・落とし穴：#pitfalls（縛りの効く・効かないは #guards-for-workers）
- 比べる相手：#compare
- 古くなった助言：#outdated（台帳の行 workflow-keyword-extra-usage を link で指した）
- level：回す（front matter のまま）

## メインに判断してほしいこと
- 強制力：data の features の `workflows` に `enforcement` がないので、`feature workflows/enforcement` の目印を使えなかった。ワークフロー自体は何も強制しない機能なので、要点に「止められるもの」を手書きで足した（「担当の道具には権限ルールと サンドボックス が効く」）。型の「強制力」の項目をどう扱うか（`enforcement: なし` を足すか、この形でよいか）を決めてほしい
- 本文の数値：担当の数・同時の上限・警告のしきい値・規模の目安の段は、数値ファイルに項目がないので本文に書いていない。facts-proposal.yml の 4 件を data/facts.yml に入れてもらえば、`fact-table` や `fact` の目印で足せる

## 提案
- data/facts.yml：facts-proposal.yml の 4 件（workflow-concurrent-agents・workflow-agent-caps・workflow-large-warning・workflow-size-guideline）。出典は cc-docs-workflows、確認日 2026-11-05
- 用語集・prh：なし（check_page で prh が hook・sandbox を指摘したので、本文は「フック」「サンドボックス」に統一した）

## 検査の結果
- check_page.py は 3 回流した（指定は 2 回まで。2 回目で link の目印を perl の置換で壊したのを直したため、3 回目を足した）。最後の結果：エラー 0・警告 2
- 残した警告 2 件：no-doubled-joshi の「に」（68 行、link の目印の間に道具が書く節の題の中）と「が」（81 行）。後者は直さなかった

## 確かめていないこと
- 雛形 2 つは動かしていない（動作確認は別の担当）。expect の then は、公式の文書の記述から書いた見込み
- 「担当ごとに範囲が分かれるので指示のずれが減る」は推論で、本文でも（推論・実践例なし）と書いた
- /goal と workflows の使い分け（#compare）は二次の記事の分け方で、根拠は弱と付けた。ページ goal-until-done は id だけで指した
- 使用上限に当たったときの待ちの条件、再開の細部は公式の文書に任せ、本文に書いていない
- 設定の hooks がワークフローの担当で走るかは、research/28 #4 のとおり確かめていない。本文はそのまま「確かめていない」と書いた
- Windows・macOS・IDE 拡張・アプリでの動作は確かめていない（面は claude-code のみ）

## 使用量
- 道具の呼び出し：約 25 回、Web の取得：1 回（code.claude.com/docs/en/workflows。公式のため check_noai は流していない）
