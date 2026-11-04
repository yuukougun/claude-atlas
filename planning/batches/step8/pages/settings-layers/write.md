# settings-layers 執筆の報告

## 書いたファイル
- docs/cli/settings-layers.md（stubs から移動。stage: draft、updated: 2026-11-05）
- front matter で変えたキー：`sections`（使いどころ {#when}・雛形 {#templates}・効かない場面・落とし穴 {#limits}・比べる相手 {#compare} を足した。既存の 3 つの anchor は変えていない）、`sources`（4 件。すべて data/sources.yml にある id）、`stage`、`updated`
- snippets/settings-layers/team-shared.json と .expect.yaml、personal-local.json と .expect.yaml
- data/sources.d/settings-layers.yml は作っていない（新しい出典がないため）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力）：冒頭の要点「強制力」の行。tracks の最初の settings は強制力を持たないので、`feature managed-settings/enforcement`（鍵）を管理の層について置き、ほかの 3 つの層は本人が書き換えられると書いた
- tracks：front matter（settings・managed-settings）。本文では #layers が両方を扱う
- 要点（強制力・確認日と版のバッジ）：冒頭の要点の囲み。確認日と版はテンプレート
- 使いどころ（どの原因を防ぐか）：#when（縛っていない）
- 最小の使い方（面のタブ）：持たない。surfaces が claude-code だけで、タブにする面の違いがない。最小の使い方は #layers の表と #merge の表
- 雛形：#templates（2 つ）
- 効かない場面・落とし穴：#limits と #verify
- 比べる相手：#compare
- 古くなった助言：持たない。outdated_advice が空で、台帳の行がない
- level：front matter（任せる）。比例則は #when で deny を先に置き、管理の層へ link

## メインに判断してほしいこと
- 要点の「強制力」は、tracks の最初の settings に enforcement の値がないため、管理の機能の値を使った。feature 型の「強制力」の行が settings に要るなら、data の settings に enforcement を足すか、置き方の決めが要る

## 提案
- 用語集：「層」（scope）を設定の文脈で定義するか確認。本文は「層」で統一した（公式は scope）
- front matter の変更はなし

## 検査の結果
- 1 回目：エラー 0、警告 4。直した後の 2 回目：エラー 0、警告 3
- 残した警告：no-doubled-joshi の 2 件（84 行の `1. 管理…` の項目は「も」を 1 つ減らしたが残った。190 行は生成されたリンクの題名「（準備中）」を含む行の「に」）、sentence-length の 1 件（131 行付近。位置が生成された部分に当たり、本文のどの文か特定できなかった）。誤検出の疑い
- 2 回目の直しは、Write でなく Bash の python で文字列を置換した（細かい 5 か所の置換のため）。brief の「Bash で書かない」から外れたので記す

## 確かめていないこと
- 雛形 2 つの動作（偽の .env での拒否、手元の層の上書き）は試していない
- `--setting-sources` と IDE 拡張・デスクトップアプリの動作は、調査資料と公式の文書の記述による。手元では未確認
- 内容は公式の Settings files and precedence を 1 回取得して突き合わせた（2026-11-05）。settings-reference と managed-settings は開いていない
- 3 つの警告の位置の特定

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：1 回（code.claude.com/docs/en/settings）
