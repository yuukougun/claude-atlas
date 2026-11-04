# write.md：unexpected-memories（執筆）

## 書いたファイル
- docs/symptoms/unexpected-memories.md（stubs から mv。stage を draft に、updated を 2026-11-05 に）
- front matter で変えたキー：sections（forms・to-fix・examples・prevention を足した。diagnosis は変えず）・sources（hc-memory・hc-incognito・hc-projects-what・cc-docs-memory。いずれも data/sources.yml にある id）・stage・updated
- 雛形・図・data/sources.d は無し（目次の templates が空のため）

## 必ず持つものの対応
- 診断のチェックリスト（安い順）：#diagnosis（共通の 2 項目→アプリのタブ 5 項目→Claude Code のタブ 4 項目。原因は「散らかっている」「境界がない」）
- 人の側の落とし穴：#diagnosis の項目 1（同じ会話の中の話）と、#prevention の最後（six-causes#human-side を指す）
- 原因ごとの振り分け先（routes）：#to-fix（`routes` の目印）
- 構成の目安の残り：よくある形 #forms／判断例 #examples（2 件）／予防 #prevention

## メインに判断してほしいこと
- 「メモリの項目（Topics）を設定で開く」は台帳 memory-daily-summary の now の文に基づく。設定画面の項目名の詳細は how-memory-works に任せ、本文では書いていない
- 「ほかのプロジェクトの記憶が混ざる」の項目 3 は、「プロジェクトはそれぞれのメモリを持つ」（data の note）の範囲に留めた。05 §2-4 の「プロジェクト内ではアカウント全体のメモリも併用される」は、data の note と書き方が違うため本文に入れていない（how-memory-works#scope の側で確定してほしい）

## 提案
- なし（用語集・prh・data への提案なし）

## 検査の結果
- 書き終えた後：エラー 0・警告 3（no-doubled-joshi）。1 回直して再実行：エラー 0・警告 3 のまま（行 51・110・131）
- 残した警告：助詞の連続の誤検出に近い。直し切れていない。メインか検証の担当で文を整える

## 確かめていないこと
- Claude Code で「別のプロジェクトの記憶」が混ざる経路を、実機では確かめていない。束の data（CLAUDE.md の読み込み階層・自動メモリの読み込み）の記述だけに基づく
- Claude Code の自動メモリが、リポジトリやディレクトリごとに分かれて保存されるかは束にないため、本文では書いていない（using-auto-memory に任せた）
- 「Claude に出どころを尋ねる」手がかりの信頼度は、一次資料では確かめていない（本文では証拠にならないと明記）
- 過去チャット検索が走ったときの表示（道具の呼び出し）は data の note に基づく。画面の見え方は未確認
- 圧縮のあとの CLAUDE.md の扱い（根は入れ直し、入れ子は読み直し）は data の note に基づく

## 使用量
- 道具の呼び出し 9 回前後、Web の取得 0 回
