# write.md：how-thinking-works

## 書いたファイル
- docs/basics/how-thinking-works.md（stub から移し、stage を draft、updated を 2026-11-05 に）
- front matter で変えたキー：sections（what-happens・why・effects・misconceptions を足した）・sources（既存の 9 件）・stage・updated
- 雛形・図ファイル・data/sources.d は無し（目次の templates なし。図は本文の Mermaid。新しい出典なし）

## 必ず持つものの対応
- どの原理・原因に関わるか：`prevents`（合っていない）を #effects で名指し。`principle` は front matter に無い（目次の備考どおり）ので、その旨を #effects に書いた。`pitfalls` は無し
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 構成：#what-happens（例）→ #why（図）→ #effects → #misconceptions → 関連（page-links の目印）

## メインに判断してほしいこと
- 本文で「新しいモデルの中には thinking を切れないものがある」とだけ書き、どのモデルかは書いていない（束の未確認 11 3-2 #11 に従う）

## 提案
- facts-proposal.yml：effort の既定の段の「モデル × 面」の表（effort-levels#defaults-by-surface が使う想定。このページの本文では使っていない）

## 検査の結果
- check_page.py：エラー 0・警告 4（no-doubled-joshi。囲みの中の判断例と、図の説明・台帳の説明の文。意味が通るので残した）

## 確かめていないこと
- 一次資料を開いていない。束の写し（05 §3-8 ほか）だけに基づく
- 「プランの利用上限も出力の分を使う」は、要約の「費用と上限に数えられる」と tokens の要約に基づく。上限の仕組みの細部は未確認
- 「effort を変えるとキャッシュが外れる」は 05 §3-8 の一文のみ。範囲（どの変更で外れるか）は未確認
- Claude Code の WSL・Linux 以外と IDE 拡張の動作は未確認

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：0 回
