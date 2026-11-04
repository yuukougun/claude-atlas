# write.md：test-the-verifier

## 書いたファイル
- `docs/eval/test-the-verifier.md`（stub から mv。front matter で変えたキー：stage=draft、updated=2026-11-05、sources に既存 3 件、sections に `guard-first`（先頭）と `when-it-fails`（末尾）を足した）
- `snippets/test-the-verifier/red-green-prompt.md`・`red-green-prompt.expect.yaml`（目次の templates の案。proposed/frozen の運用と、壊したコピーで落ちる確認を足した）
- 出典は data/sources.yml の既存 id だけを使ったので、`data/sources.d/test-the-verifier.yml` は作っていない

## 必ず持つものの対応
- 手順：`#red-green`（確認の表と各段の終わりの確かめ）・`#hand-calculated`・`#broken-copy`（番号付きの手順）・`#freeze`
- 確かめる・縛るのページへの道：本文は `#guard-first`（verifier-three-conditions#correct、freeze-eval-assets）・`#freeze`（freeze-eval-assets の 3 節）・`#red-green`（tests-first#steps）・`#broken-copy`（pitfalls-of-ai-written-tests#test-strength）。front matter の prerequisites と related にも同じものがある
- level：front matter に「仕組みにする」（変更なし）
- 構成の目安（要点→守り→手順→確かめ方→失敗したとき）：`#guard-first` → `#red-green` ほか → `#freeze` 内のチェック → `#when-it-fails`

## メインに判断してほしいこと
- 研究の数値（CORE-Bench 42% → 95%、96.12 と 96.124991…）は、card §7 の「研究の結果は固定の記録」に従い、モデル名・日付・条件を添えて本文に書いた。目印にしていない
- `tests/proposed/`・`tests/frozen/` は例示のパスとして本文に書いた。A-4 の deny ルール（`Edit(/tests/frozen/**)`）の具体は freeze-eval-assets に任せ、本文では繰り返していない

## 提案
- 用語集：「検証器」「red/green」「凍結」が用語集にあるか未確認。なければ追加を提案する
- front matter の提案：なし

## 検査の結果
- 1 回目：エラー 0・警告 7。直した後の 2 回目：エラー 0・警告 4（2 回の上限なので再検査していない）
- 残した警告：max-ten（要点の 1 行目、43 行）、no-doubled-joshi（61・108・180 行）。いずれも文の分け方の好みの範囲で、意味は崩れていない。メインの検査で必要なら直す

## 確かめていないこと
- 雛形（red-green-prompt）は実際に Claude に出して動かしていない。expect は想定である
- 「ランダムな解は必ず負ける」は材料（11 の要約）の推論で、確率で当たる課題では成り立たない場合がある。本文は「強い解より低い点が返る」にとどめた
- 入力の生成器の節と採点の正本の節は、材料の 11（実践、章：強）に基づく。一次の資料は開いていない（Web の取得 0 回）
- 判断例 2 件（手計算との食い違い、壊したコピーでも通る）は書き手の例で、出典はない
- 用語集と prh への適合は検査の範囲でしか見ていない

## 使用量
- 道具の呼び出し：約 10 回。Web の取得：0 回
