# write.md：diffs-humans-must-read（執筆）

## 書いたファイル
- docs/verify/diffs-humans-must-read.md（stubs から移動。stage を draft、updated を 2026-11-05 に。sections に what-happens・why・what-it-helps・misconceptions を足した。既存の red-flags・core-vs-periphery は変えていない）
- snippets/diffs-humans-must-read/ に 3 つ：red-flag-checklist（.md・kind other）、list-red-flags（.txt・kind prompt）、scan-diff（.sh・kind other）。それぞれ .expect.yaml 付き
- sources と data/sources.d は作っていない（front matter の sources は空のまま）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle 確かめる・握る／prevents 確かめていない／pitfalls 預けすぎる）：#what-it-helps で 4 つとも名指し。#why でも「確かめていない」「預けすぎる」を名指し
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#what-happens → #why → #red-flags → #core-vs-periphery → #what-it-helps → #misconceptions。関連はテンプレートが出す
- 比喩付きの図：持たない。図の案が目次にない。比喩を無理に足さなかった
- level（任せる）：front matter に持つ。要点の最初は「何が分かるか」

## メインに判断してほしいこと
- 材料の p56#61（AI が生成した PR は約 1.7 倍の指摘、分析元は AI レビュー製品の販売元）は、出典を立てていないため本文に使わなかった。使うなら sources 追加と利害の併記が要る
- 「要の処理は厳しく、周辺は緩く」の出どころ（実践者の講演）は、個人を名指さず、（根拠：弱）の経験則として書いた。出典を立てて名指すかは判断を求める
- 赤信号の一覧は（根拠：中）とした（材料では「強〜中」）。強さの扱いを確認してほしい

## 提案
なし（用語集・prh・data への提案はない。数値の提案もない）

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 2（リンクの題名と助詞「に」が重なる no-doubled-joshi）。文を「が持つ」に直し、2 回目 エラー 0・警告 0

## 確かめていないこと
- scan-diff.sh と 2 つの依頼の雛形、点検表は実行していない（expect.yaml は期待の記録）
- 冒頭の差分例は説明のために作った例で、実際のセッションの記録ではない
- 赤信号の一覧の出どころ（11 第2節の補完）の個々の項目を一次資料で確かめていない。束の写しに基づく
- 判断例の「30 分」「40 ファイル」は例示のための数字
- WSL・Linux 以外の OS と IDE 拡張では確かめていない

## 使用量
- 道具の呼び出し：約 12 回（Read 3、Bash 4、Write 8 を含む）、Web の取得 0 回
