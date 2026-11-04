# write.md：structured-outputs-basics

## 書いたファイル
- docs/api/structured-outputs-basics.md（stub から mv。stage を draft、updated を 2026-11-05 に）
- front matter で変えたキー：sections（使いどころ {#when}・最小の使い方 {#minimal}・比べる相手 {#compare}・古くなった助言 {#outdated} を足した。既存 4 つの anchor は変えず）、sources（既にある 4 つの id）、stage、updated
- snippets/structured-outputs-basics/ に json-output.json・strict-tool.json・claude-p-json-schema.sh と、それぞれの .expect.yaml
- data/sources.d/structured-outputs-basics.yml は作っていない（出典は既存の id で足りた）

## 必ず持つものの対応
- 冒頭の要点：冒頭の `!!! abstract`（何ができるか・いつ引くか・強制力・前提）
- 機能の属性のバッジ（強制力など）：バッジ列はテンプレートが出す。要点の「強制力」に `gen feature enforcement` の目印を置いた
- tracks：front matter の `tracks: [structured-outputs]`（変更なし）
- level：front matter の `level: 仕組みにする`（変更なし）
- 使いどころ（どの原因を防ぐか）：#when
- 最小の使い方（面のタブ）：#minimal（Claude Code・API のタブ）
- 雛形：#minimal（json-output・strict-tool）と #claude-code（claude-p-json-schema）
- 効かない場面・落とし穴：#not-guaranteed
- 比べる相手：#compare
- 古くなった助言：#from-prefill（移行先）と #outdated（台帳の link）

## メインに判断してほしいこと
- 台帳の link `outdated-advice-ledger#prefill-for-json` を使った。check は通った

## 提案
- なし（数値・用語集・data への提案はなし）。スキーマの複雑さの上限などは数値を書かず、公式への案内にとどめた

## 検査の結果
- 1 回目：エラー 0・警告 4（no-doubled-joshi）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- 雛形 3 つは実行していない（API の本文はキーが要るため。`claude -p` は未実行）
- `structured_output` が `--output-format json` の出力のどこに入るかの細部は、束の J-1 の記述に頼った。公式の headless は開いていない
- citations との併用不可（400）と、再帰スキーマ・数値範囲の非対応は束の 02 §5-4 に頼った。取得した公式の文書の前半では、未対応の書き方に最小・最大が含まれ、400 になることは確かめた。citations と prefill の節は取得の範囲外
- `-p` の `--json-schema` が API と同じ制約つきのデコードによる保証かは確かめていない（本文は断定していない）
- 「道具の強制（tool_choice）がモデルによって使えず、公式は structured outputs を勧める」は data の note に頼った
- Windows・macOS・IDE 拡張での `claude -p` の動作は未確認

## 使用量
- 道具の呼び出し：約 17 回、Web の取得：1 回
