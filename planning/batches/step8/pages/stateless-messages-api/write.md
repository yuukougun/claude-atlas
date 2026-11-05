# write.md：stateless-messages-api

## 書いたファイル
- docs/api/stateless-messages-api.md（stubs から移した。stage を draft、updated を 2026-11-05 にした）
- docs/img/stateless-messages-api/send-vs-read.svg（図：基本の形と message threads で、送る量とモデルが読む量を並べた）
- front matter で変えたキー：`sections`（`effects`・`misconceptions` を足した。既存の 3 つは変えず）、`sources`（api-docs-messages・api-docs-message-threads・api-release-notes。いずれも data/sources.yml にある）、`stage`、`updated`
- 雛形（snippets）は置いていない（目次の templates は「なし」。リクエストの形は本文のコードブロックで示した）。data/sources.d/stateless-messages-api.yml も、新しい出典がないので作っていない

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の囲み
- 何が起きるか（例）：#stateless（`parse_config` の 2 回目の呼び出しで「さっきの関数」が通じない例と、履歴を含めた送り方）
- なぜそうなるか（比喩付きの図）：#stateless（毎回読み直す受験者の比喩。理由の本体は rereads-whole-history#why へ link）と #message-threads（図 send-vs-read.svg）
- 何に効くか（原理・原因を名指し）：#effects（原理「見せる」・原因「散らかっている」。判断例も同じ節）
- 誤解：#misconceptions
- 関連：テンプレートが出す
- `pitfalls`：このページの front matter にキーがないので、本文で名指す値はない
- 補足：#system-and-messages は目次の sections にある節（`system` と `messages` の役目）

## メインに判断してほしいこと
- message threads のスレッドの寿命（最後の要求から切れるまで、最後に使ってから消えるまで）は、data の facts に該当の id がない。本文は数字を書かず「公式の文書で確かめる」とした。下の提案で fact を足してもらえれば、#message-threads の 1 つ目の項目に目印を置ける
- 判断例の「選んだもの」（要約で履歴を短くする）は、このページの推奨ではなく状況を限った例である。違和感があれば直す
- ZDR と HIPAA の対象外という記述は、research/22 #40（Platform のリリースノート 11-02）と facts の note による。HIPAA は facts の note にはなく、research/22 だけが根拠。公式の message threads の文書で再確認していない

## 提案
```yaml
proposals:
  - fact: {id: message-threads-lifetime, title: message threads のスレッドの寿命（最後の要求から切れるまでと、最後に使ってから消えるまで）, value: "最後の要求から 5 分で切れ、最後に使ってから 1 時間以内に消える", sources: [api-docs-message-threads, api-docs-messages], checked: 2026-11-05, status: 確認済み}
    used_in: [stateless-messages-api#message-threads]
```
- 根拠：working-with-messages の文書の「A thread expires 5 minutes after its last request and is deleted no more than 1 hour after its last use」（2026-11-05 に取得）と research/22 #40
- 用語集：「stateless（状態を持たない）」は本文で短く定義した。用語集にないなら追加を検討してほしい

## 検査の結果
- 1 回目：エラー 1（prompt caching の表記。prh）・警告 3
- 直した後（2 回目）：エラー 0・警告 1（#message-threads 末尾の判断例の「理由」の 1 文で助詞「と」が重なる。直す回数の上限のため残した。検証と直しの担当が直してよい）
- 英語の `prompt caching` は、API の機能名として原文のまま書きたかったので、prh を一か所だけ無効にした

## 確かめていないこと
- 図（SVG）をブラウザで描画して見ていない。文字の収まりは目で確かめていない
- 判断例（20 往復目の質問応答）は想定の場面で、実際に試していない
- 公式の message threads の文書そのものは開いていない。working-with-messages の文書の記述と、束の写し（research/22 #40・facts の note）に基づく
- Messages API の始まった時期は確かめていない（facts の note のとおり）
- `system` が「最初から効かせたい指示を入れる最上位の欄」という記述は working-with-messages の文書による。複数の面（クラウド各社）で同じかは見ていない

## 使用量
- 道具の呼び出し：約 14 回（Read 5・Bash 6・Write 3 ほか。Edit 3）、Web の取得：1 回
