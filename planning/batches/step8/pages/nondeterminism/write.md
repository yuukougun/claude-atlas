# write.md：nondeterminism

## 書いたファイル
- docs/basics/nondeterminism.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に anthropic-research-infrastructure-noise を追加、sections を 5 節追加）
- 雛形・図・data/sources.d は置かない（理由は下）

## 必ず持つものの対応
- どの原理・原因に関わるか（principle「確かめる」・prevents「確かめていない」を名指す）：#what-helps
- pitfalls：front matter に pitfalls のキーがなく、束にもないため持たない
- 要点の最初は「何が分かるか」：冒頭の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：#what-happens → #why → #what-helps → #misconceptions（関連は page-links）。#temperature-advice は台帳の行 lower-temperature を指す節

## メインに判断してほしいこと
- 図（目次の visual 案「同じレシピでも味が違う料理人」）は文章の比喩だけにして、SVG は作っていない。要るなら別途
- 雛形は目次の templates が空なので置いていない

## 提案
- 用語集：「非決定性」を、同じ依頼を出し直すと答えが変わる性質として追加する案
- 数値の提案はなし

## 検査の結果
- 2 回流した。最終はエラー 0・警告 1
- 残した警告：43 行の textlint no-doubled-joshi（「が」の重なり）。直さない理由は、定義文と挙動の説明を 1 文に置いたためで、読みにくくはないと判断した（直すなら 2 文に分ける）

## 確かめていないこと
- 答えが変わる仕組み（トークンを選ぶ幅）の説明は一般的な説明で、一次資料で確かめていない。束にある GPU 計算の原因は二次情報なので使っていない
- Terminal-Bench 2.0 の 6 ポイントは束の注記（research/24 B-51 で確認済み）に基づく。原典は開いていない（アクセスの数は 0）
- 面ごとのタブ（アプリ・Claude Code・API）の手順は一般的な使い方で、各 UI の操作は確かめていない。IDE 拡張と WSL・Linux 以外は「未確認」と書いた
- temperature の撤回の詳細は台帳を指し、本文には版・日付を書いていない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0 回
