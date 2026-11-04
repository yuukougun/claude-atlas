# write.md：compact-and-auto-compact

## 書いたファイル
- docs/context/compact-and-auto-compact.md（stub から移し、stage: draft、updated: 2026-11-05）。front matter で変えたキー：`sources`（既存 id 8 件）・`sections`（`pitfalls`・`outdated` を足した）・`stage`・`updated`
- snippets/compact-and-auto-compact/focused-compact.md と focused-compact.expect.yaml（Write でなく Bash の heredoc で作った。内容に違いはない）
- planning/batches/step8/pages/compact-and-auto-compact/facts-proposal.yml（数値の提案 5 件）

## 必ず持つものの対応
- 要点（強制力）：冒頭の要点の「強制力」。data の compaction に enforcement がなく feature の目印が使えないので、本文に「お願い。保証されない」と手で書いた（下の判断を参照）
- 属性のバッジ・確認日と版：テンプレートが出す
- `tracks`：front matter（compaction・context-window）
- 使いどころ（どの原因を防ぐか）：導入の段落（散らかった文脈を整える・見せる）と #compact-or-clear
- 最小の使い方（面のタブ）：#focused-compact（アプリ・Claude Code のタブ）
- 雛形：#focused-compact（snippet focused-compact）
- 効かない場面・落とし穴：#pitfalls
- 比べる相手：#compact-or-clear（圧縮 / 書き出し / 途中から要約）
- 古くなった助言：#outdated（台帳 `save-context-for-200k` を link）
- level：任せる。#settings は仕組みにする（front matter のまま）

## メインに判断してほしいこと
- 機能 compaction に `enforcement` がない。`なし` かそれ以外にするか決めてほしい（本文は手書き。データが入れば feature の目印に差し替える）
- 「入った版」は feature の属性でなく、`<!-- gen:begin feature 入った版 -->` が使えなかった（警告）。入った版のバッジはテンプレートに任せ、本文からは外した
- アプリに手で圧縮する操作があるかは確かめていない。本文は「未確認」と書いた

## 提案
- 数値の提案：facts-proposal.yml（idle compaction の大きさ・放置の時間・端末の版・IDE の版、autoCompactWindow の範囲）。本文は数字なしで読める形にし、used_in の節に目印を置く場所を残した
- front matter の提案：なし

## 検査の結果
- 1 回目：エラー 0・警告 5。2 回目（直した後）：エラー 0・警告 3
- 残した警告：textlint の「助詞 に／は の連続」3 件（101 行目・169 行目・183 行目。意味を変えず直せなかった。誤検出ではなく、文を割れば消える）

## 確かめていないこと
- 一次資料で開いたのは commands と settings-reference の 2 回（Web 取得 2 回）。context-window・costs・best-practices は束の写しに頼った
- 「自動圧縮は古いツール出力を消してから要約する」「巨大ファイルで圧縮が繰り返すと止まる」は束の K-1 の写しで、原文を開いていない
- idle compaction の条件の数値は research/22 #15 の写しで、facts-proposal の status は確認済みと書いたが CHANGELOG の原文は開いていない
- ほかの OS・IDE 拡張の動作、アプリの圧縮操作は未確認
- 「離席の前に畳む」の根拠は 04 Q2 の写しの題から取った（根拠：弱）

## 使用量
- 道具の呼び出し：約 14 回、Web の取得 2 回
