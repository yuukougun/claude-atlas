# write.md：choosing-a-model

## 書いたファイル
- docs/models/choosing-a-model.md（stubs から mv。front matter は sections・stage・updated・sources だけ変更）
- docs/img/choosing-a-model/three-steps.svg（三段の階段の図）
- 雛形・data/sources.d は無し（出典は既存の id だけ使用）。front matter の変更：sections に what-it-prevents・verify・misconceptions を追加（既存 4 節の anchor は不変）、stage を draft、updated を 2026-11-05、sources に api-docs-choosing-a-model・api-docs-models-overview・api-docs-effort・cc-docs-model-config・hc-effort-settings

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle「確かめる」・prevents「合っていない」）：#what-it-prevents（本文で名指し。#verify も「確かめる」に当たる）
- pitfalls：front matter が空のため無し
- level「使う」・要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成：要点 → 何が起きるか（例）#examples → なぜ #effort-first → 何に効くか #what-it-prevents → 誤解 #misconceptions → 関連（テンプレート）。三段階の本体は #three-steps

## メインに判断してほしいこと
- 原因「合っていない」の定義を、束にある情報だけから「選んだモデルや effort が作業の重さに合っていない」と書いた。site.yml の定義と合うか確認してほしい
- 具体的なモデル名・料金・既定値は、names/facts の id が束になかったので本文に書かず、current-models と effort-levels の節を指した。数値の目印は 0 個

## 提案
- なし（数値・用語集・front matter の提案なし）

## 検査の結果
- 1 回目：エラー 0・警告 3（一つ・も 重複・が 重複）→ 語句を直した
- 2 回目：エラー 0・警告 2（判断例 3 の状況の行の「が」重複）→ 回数の上限のため再検査せず、当該の行だけを sed で直した（「気がするが」→「気はする。」）。再検査は未実施

## 確かめていないこと
- 2 回目の警告を直した後の check_page.py の結果（検査は 2 回までの決めのため流していない）
- 判断例 1 の「数段上げても変わらないとき」など、effort の段の数に関する書き方が各モデルの選べる段と合うか
- 能力優先・効率優先の公式の記述は束の写しだけで、一次資料を開いていない
- API タブの「model を替える」「effort のパラメーター」の言い回し（束の data に基づく）

## 使用量
- 道具の呼び出し 11 回、Web の取得 0 回
