# write.md：permission-modes-in-the-app

## 書いたファイル
- docs/app/permission-modes-in-the-app.md（stubs から mv。stage draft、updated 2026-11-05）
- front matter で変えたキー：`sections`（limits・compare を追加）、`sources`（hc-cowork-start・hc-cowork-and-chat・hc-cowork-safety・hc-computer-use。どれも data/sources.yml にある）、`stage`、`updated`
- snippets/permission-modes-in-the-app/first-low-risk-task.md と .expect.yaml（prompt・safety true）
- docs/img/permission-modes-in-the-app/two-conditions.svg（目次の図の案：二条件と外す手段）
- data/sources.d は新規なし（出典は既存の id だけ）

## 必ず持つものの対応
- 強制力のバッジと一言：冒頭の要点の「強制力」（feature の目印 app-permission-modes/enforcement）。鍵は Manual の許可確認と削除の確認、Auto は判断と {#modes} でも書く
- tracks：front matter の `app-permission-modes`（変更なし）
- 使いどころ（どの原因を防ぐか）：{#two-conditions}（境界がない・縛っていない。二条件と外し方）
- 最小の使い方（面のタブ）：タブなし。surfaces が app だけのため。手順は {#start-small}
- 雛形：{#start-small}（first-low-risk-task）
- 効かない場面・落とし穴：{#limits}（預けすぎる）
- 比べる相手：{#compare}
- 古くなった助言：持たない。束に台帳の行がない
- level：任せる（変更なし）

## メインに判断してほしいこと
- 本文はプラン名と既定を書かず、default-safety-settings#defaults-by-surface を指した。アプリの既定を数値ファイルに置くなら下の提案を採るか判断してほしい
- 「コネクタの許可は届く先を絞る」は、目次の図の案からの書き方で、束の公式の抜き出しに直接の記述がない。本文では穏やかに書いた

## 提案
```yaml
proposals:
  - fact: {id: app-permission-mode-defaults, title: アプリの新しい会話の権限モードの既定（プラン別）, value: "要確認（束の data には Pro・Max・Ultra・Team は Auto、Enterprise は Manual とある。調査資料 02 は Pro・Max・Team の Auto、Enterprise の Manual。Ultra の扱いが食い違う）", sources: [hc-cowork-start, hc-cowork-and-chat], checked: 2026-11-05, status: 要確認}
    used_in: [permission-modes-in-the-app#modes]
```
- 本文には目印を置いていない。採用されたら #modes の「新しい会話の既定の段」の文に fact の目印を足す

## 検査の結果
- 1 回目：エラー 5（prh の auto mode・sandbox・plugin）・警告 7。直した後：エラー 0・警告 4
- 残した警告：72 行（図の代替テキストの助詞「が」。図の内容を言うため）、82 行（文の長さ。リンクの記法が字数に入る誤検出と見る）、133 行（判断例の「に」）、143 行（「が」）。意味を変えずに直す案が見つからなかった

## 確かめていないこと
- Desktop と Web の権限モードの設定画面・既定・切り替え方（research/23 §5 のとおり未読）。本文にもそう書いた
- アプリの Auto と Claude Code の auto mode が同じ分類器か。本文は同じと書かず、確かめていないと書いた
- 外の URL は開いていない。本文の事実は束の写しだけに基づく
- 雛形・図の動作と見え方は確かめていない
- 「Skip」の段は名前だけ出し、旧名と使い方は書かなかった

## 使用量
- 道具の呼び出し 11 回、Web の取得 0 回、検査 2 回
