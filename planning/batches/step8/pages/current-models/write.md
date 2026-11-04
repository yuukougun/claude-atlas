# write.md：current-models（執筆）

## 書いたファイル
- docs/models/current-models.md（stub から移した。stub の原本 stubs/models/current-models.md は削除。stage を draft、updated を 2026-11-05、sources を 8 件に、sections を 5 節に変えた）
- sections の追加：how-to-choose（系統の選び方）・combine（系統の組み合わせ方）。既存の 3 節の anchor は変えていない
- 雛形・図・data/sources.d は作っていない（目次の templates・visual がなく、出典は既存の id だけで足りた）
- facts-proposal.yml（数値の提案）

## 必ず持つものの対応
- 要点：冒頭の囲み（「何ができるか」に「〜なら A、〜なら B」の基準）
- 比較の表：#lineup（系統 × 向く仕事 × 速さと料金の位置の表）。属性の生成表ではなく手書きの定性の表（下の判断 1）
- 判断例：#how-to-choose（2 つ）
- 組み合わせ方：#combine
- level：front matter の「使う」のまま

## メインに判断してほしいこと
1. データに現行モデルの一覧表（型番・API ID・料金・窓）がなく、tracks の機能が model-selection の 1 つだけで `compare` の目印が表にならない。そこで #lineup は、型番・料金の数値を使わない定性の表にした（系統名だけ、世代は書かない）。facts-proposal.yml の current-models-lineup を facts に足したら、#lineup の表の後に `fact-table current-models-lineup` を置いてほしい
2. #fable-and-mythos は、提供範囲を本文に書かず「公式の発表で確かめる」にした。mythos-availability を足したら fact の目印で置ける。透かしは catalog の notes に従い、2 つの違いとして書かず、日付も本文に書かなかった
3. 自動の切り替え（分類器が止めた依頼を別のモデルで答え直す）は、仕組みの説明 1 段落だけにした。safety の持ち主のページ（when-requests-are-refused）を link で指していない（束の「指せる節」にないため）。足してよければ指したい
4. 「確認日 2026-10-29」を #lineup の表の下に手書きした（束の 3-1 の確認日）。目印の外の日付で、fact-table を足したら表の下の出典の行に置き換えてよい

## 提案
- 数値の提案：facts-proposal.yml（current-models-lineup・haiku-4-5-removed-from-app-selector・sonnet-4-5-retirement・mythos-availability）
- front matter の提案はなし

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 3（助詞の重複 2、1 文の長さ 1。生成された link の題名で文が長くなったもの）。直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 表の速さ・料金・得意な仕事は、束の写し（research/02 §3-1・3-4・3-5、確認日 2026-10-29）のとおり。一次資料を開いていない（Web の取得 0 回）。束の写しは「…（略）」で切れており、Haiku の項の末尾と Haiku の始め方の「能力優先」の項は読んでいない
- 「窓の広さや知識の期限は 4 系統で大きく変わらない」は 3-1 の表（1M・2026年6月）に基づく。数値は本文に書いていない
- 「旧世代はアプリの選択肢から先に外れ、Claude Code と API に残る例」は research/22 #23 に基づく一般化。日付は書いていない
- `availableModels`・`/model` で `s` を押すとそのセッションだけ、は data の model-selection の note に基づく。WSL・Linux 以外と IDE 拡張の動作は未確認
- 公式の「同じモデルで安全装置の水準が違う」は、引用でなく言い換えにした

## 使用量
- 道具の呼び出し 14 回前後、Web の取得 0 回
