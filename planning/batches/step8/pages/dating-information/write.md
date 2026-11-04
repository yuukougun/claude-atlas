# write.md：dating-information

## 書いたファイル
- docs/changes/dating-information.md（stubs から mv。stage を draft、updated を 2026-11-05 に）
- front matter で変えたキー：sections（`what-helps`・`misconceptions` を足した。既存の 3 つは変えず）、sources（既存の id：cc-docs-best-practices・cc-changelog）、stage、updated
- 雛形・図・data/sources.d は無し（目次に templates・visual なし）

## 必ず持つものの対応
- 冒頭の要点の最初が「何が分かるか」：冒頭の要点の囲み
- level（使う）を持つ：front matter
- どの原理に関わるか（principle：確かめる）を本文で名指す：#what-helps
- prevents・pitfalls：front matter に値なし。#what-helps で防ぐ失敗（古い手順の思い込み・食い違い・回避策の継続）を書いた
- 構成の目安（具体の場面→なぜ→何に効くか→誤解→関連）：#layers（食い違う記事の場面は #check-date-and-version の判断例）→ #workarounds → #what-helps → #misconceptions → 関連（テンプレート）

## メインに判断してほしいこと
- 「公式の Best practices が書き直された」の記述に日付・版を書いていない（変わりやすい値を避けるため）。日付入りで書くなら facts への登録が要る
- `claude --version` は束にない。記憶による記述（広く使われる確認手段）なので、別の担当が確かめてほしい

## 提案
- 無し（用語集は既存の語のみ。prh に従い フック・スキル・auto モード・サンドボックス と書いた）

## 検査の結果
- 1 回目：エラー 6（prh の表記：hooks・skills・auto mode・sandbox）、警告 3。表記を直した
- 2 回目：エラー 0、警告 2（no-doubled-joshi。104 行目「に」、120 行目「が」。読めるので残した）

## 確かめていないこと
- 面ごとのタブ（アプリの Help Center、API のリリースノートの在り処）は束と記憶による。URL は書いていない
- checking-for-updates は未公開で「準備中」と出る
- 例に挙げた置き換わりの 4 件は束の research による。台帳の行の id への link は、行の id が束にないため使っていない

## 使用量
- 道具の呼び出し 約 14 回、Web の取得 0 回
