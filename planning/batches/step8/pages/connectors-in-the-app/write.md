# write：connectors-in-the-app

## 書いたファイル
- docs/app/connectors-in-the-app.md（stub から移した。front matter：stage を draft、updated を 2026-11-05、sources に既存の 8 件、sections に limits・compare・outdated を足した）
- snippets/connectors-in-the-app/connector-request.md と .expect.yaml（prompt）、desktop-config.json と .expect.yaml（settings）
- data/sources.d は作っていない（出典はすべて data/sources.yml にある既存の id）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが tracks（connectors・mcp）から出す。本文には書かない。要点の「強制力」は文で書き、feature の目印は置いていない（下の判断を参照）
- tracks：front matter の `tracks: [connectors, mcp]`（そのまま）
- 使いどころ（どの原因を防ぐか）：#types（冒頭と種類）・#on-demand（見せすぎ）・#trust（境界）
- 最小の使い方：#types の「最小の使い方」の小見出し（面は app だけなのでタブなし）
- 雛形：#types（connector-request）・#desktop-local-mcp（desktop-config）
- 効かない場面・落とし穴：#limits
- 比べる相手：#compare
- 古くなった助言：#outdated（台帳 customize-tabs を link で指した）
- level：front matter に level 整える、#desktop-local-mcp は任せる（元のまま）

## メインに判断してほしいこと
- 要点の「強制力」：data の connectors に enforcement がなく、feature の目印では「未確認」になる。値を目印で出さず、文で「鍵ではない。止められるのは道具ごとの許可で締めた操作だけ」と書いた。data に enforcement を足すか判断してほしい
- 雛形 connector-request の control（読み取りだけの行がないと下書きまで作ろうとすることがある）は未検証の記録

## 提案
```yaml
proposals:
  - fact: {id: custom-connector-free-limit, title: 個人の Free プランの Custom connectors の上限, value: 1 件, sources: [hc-connectors], checked: 2026-11-05, status: 確認済み}
    used_in: [connectors-in-the-app#types]
  - fact: {id: connectors-on-demand-recommend-threshold, title: On demand を勧める有効なコネクタの数の目安, value: 10 個以上, sources: [hc-connectors], checked: 2026-11-05, status: 確認済み}
    used_in: [connectors-in-the-app#on-demand]
```
- 上の 2 件は、本文では数字を書かず公式を見る旨にしてある。目印を置く場合の位置が used_in。値は束の 02 §1-11（確認日 2026-10-29）による。Free の上限は data の connectors の note と一致

## 検査の結果
- 1 回目：エラー 1（前提は「なし」）・警告 9。直した後の 2 回目：エラー 0・警告 5
- その後、警告 5 のうち 4 行（助詞の重複）を言い換えたが、検査は流していない（回数の決まりのため）。残りの警告は、link の目印の間に入る相手の題名による誤検出の可能性がある

## 確かめていないこと
- 雛形の動作（Gmail・カレンダーのコネクタでの挙動、filesystem サーバーの起動）。desktop-config.json の `@modelcontextprotocol/server-filesystem` は記憶に基づく一般的な例で、一次資料を開いていない
- 設定画面の入口の名前（束の注記どおり未確認）。Web 取得は 0 回
- On demand の読み込みの細部（依頼に名前を書くと確実になるかは推論と明記した）
- #types の「Directory のコネクタは何を読み書きできるかを自分で確かめる」は一般的な注意で、公式の記述ではない

## 使用量
- 道具の呼び出し 13 回ほど、Web の取得 0 回
