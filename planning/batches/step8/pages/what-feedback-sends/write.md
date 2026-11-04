# write.md：what-feedback-sends

## 書いたファイル
- docs/safety/what-feedback-sends.md（stubs から移した）。front matter で変えたキー：sections（`before-sending` を足した。既存の 3 つの anchor は変えず）・sources（cc-docs-data-usage・cc-docs-commands・privacy-long-store-data）・stage（draft）・updated（2026-11-05）
- snippets/what-feedback-sends/disable-reporting.json と .expect.yaml（settings の env 3 つ）
- data/sources.d/what-feedback-sends.yml（新しい出典なしで `sources: []`）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・読み込みの時期など）：テンプレートが出す。本文には置いていない。下の「メインに判断してほしいこと」1 を参照
- `tracks`（feedback）：front matter に `tracks: [feedback]` がある。節は {#what-is-sent}（保持の期間）・{#share-is-bug}・{#telemetry}
- level：整える（front matter）
- 構成の目安：使いどころ（何を送るか・防ぐ原因）={#what-is-sent}・{#before-sending}／最小の使い方（面のタブ）={#what-is-sent} のタブ／雛形={#telemetry}／効かない場面・落とし穴={#before-sending}・{#share-is-bug}／比べる相手＝{#share-is-bug}（claude.ai のチャット共有を link）／古くなった助言＝台帳の行がなく置かない

## メインに判断してほしいこと
1. feedback の機能に `enforcement` がない。/feedback は強制の仕組みではないので、要点に「強制力」を置かなかった。必要なら data 側で値（なし）を足すか、feature 型でこの項目を外すかを決める
2. 目次の templates は「なし」。分かりやすさのために、テレメトリを止める env の雛形を 1 つ足した（safety: true）

## 提案
```yaml
proposals:
  - fact: {id: feedback-transcript-share-retention-months, title: セッション評価の後の記録の共有（Yes を選んだとき）の最長の保持期間, value: 6, unit: か月, sources: [cc-docs-data-usage], checked: 2026-11-05, status: 確認済み}
    used_in: [what-feedback-sends#what-is-sent]
```
- 束の research/05 4-6 の写し（Data usage より）に「最大6か月」とある。数値の目印が置けないので、本文は数字なしにしてある。fact が入ったら what-is-sent の該当文（「別の上限が付く」）に目印を置く
- 用語集・prh・front matter の提案はなし

## 検査の結果
- check_page.py 1 回目：エラー 1（タブの並び）・警告 2（助詞の連続）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- 一次資料を開いていない。束の写し（Data usage・Commands の引用）に基づく。同意の画面の文言と、履歴の範囲の選び方の細部は未確認
- アプリでの送り方（画面・選べる範囲）は材料にない。アプリのタブは 👍👎・バグの報告が同じ期間で残るとだけ書いた
- 「送った後に手元から取り消す手順は公式の文書に見当たらない」は、束の材料に取り消しの記述がないことからの書き方で、公式を全部探した結果ではない
- 個人のプランと商用のプランで、/feedback の保持が変わるかは材料にない（where-your-data-goes に任せ、本文では触れていない）
- `DISABLE_FEEDBACK_COMMAND` を置いたときの /feedback の表示と、雛形の動作は試していない
- Windows・macOS・IDE 拡張の動作は未確認（本文では OS に触れていない）

## 使用量
- 道具の呼び出し：12 回ほど（Read 2、Bash 5、Write 5）。Web の取得：0
