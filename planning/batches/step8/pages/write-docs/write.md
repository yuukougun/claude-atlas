# write-docs 執筆の報告

## 書いたファイル
- docs/recipes/write-docs.md（stub から移し済みのものに本文を書いた。front matter で変えたキー：`sections`〔guards・steps・intent・overall-check・when-it-fails〕・`sources`〔cc-docs-common-workflows〕・`stage`〔draft〕・`updated`〔2026-11-05〕）
- snippets/write-docs/write-from-model.txt・.expect.yaml、doc-code-mismatch.txt・.expect.yaml

## 必ず持つものの対応
- 冒頭の要点：先頭の `!!! abstract`（前提は prerequisites の 3 ページを全部 link）
- 手順：#steps（手順 1〜5。各段に「終わりの確かめ」）
- 確かめる・縛るのページへの道（前提か関連。比例則）：#guards（show-examples・consistent-politeness・textlint-hook・fact-checking を先に示す）。#steps の手順 5 の判断例で「広げる前に確かめと検査を通す」を示した
- level：front matter の `level: 整える`
- 構成の目安（要点 → 先に整える守り → 手順 → 確かめ方 → 失敗したとき）：#guards → #steps（＋#intent）→ #overall-check → #when-it-fails。#intent は目次の「プロジェクトの標準に照らす」を補う節で、目安にない追加

## メインに判断してほしいこと
- なし（公開の約束・方針に関わる文は入れていない）

## 提案
- なし（front matter・用語集・数値の提案はない）

## 検査の結果
- `check_page.py write-docs`：1 回目はエラー 1（タブの並び）・警告 8（助詞の重複など）。直して 2 回目でエラー 0・警告 0

## 確かめていないこと
- 雛形 2 つは動作を試していない（expect は観察の記述）
- アプリでの手元のファイルの読み込みの細部は未確認とそのまま書いた
- Claude Code の挙動は公式 Common workflows の要約（束の写し）に基づく。原文は開いていない（Web の取得は 0 回）
- 直しの 2 回目は Python スクリプトで置換した（Edit の連発を避けるため）。ページの初稿は Write で書いた

## 使用量
- 道具の呼び出し 約 13 回、Web の取得 0 回
