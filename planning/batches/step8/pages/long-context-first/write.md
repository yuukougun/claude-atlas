# write.md：long-context-first

## 書いたファイル
- docs/prompting/long-context-first.md（stub から移動。stage を draft、updated を 2026-11-05、sources に 4 件、sections に why・limits の 2 節を足した）
- snippets/long-context-first/docs-then-question.{txt,expect.yaml}、quote-first.{txt,expect.yaml}
- facts-proposal.yml（数値の提案 2 件）。data/sources.d は不要（出典 4 件は既存）

## 必ず持つものの対応
- 用途（技法：Before/After → 何が変わるか → なぜ効くか → 効かない場面）：Before/After と変更点は #order、引用は #quote-first、なぜは #why、効かない場面は #limits
- principle「見せる」の名指し：#why の冒頭と、「見えていない」の段落
- prevents「見えていない」「散らかっている」の名指し：#why（それぞれ 1 段落）
- pitfalls：front matter に無いので持たない（本文での名指しは対象外）
- level（整える）：front matter。要点の最初は「何が分かるか」

## メインに判断してほしいこと
- 図（目次 visual の Before/After）は SVG にせず、本文の Before/After とスニペットで代えた。SVG が要るなら次の波で
- 公式の「最大 30% 向上」は数値の提案にとどめ、本文には数字を書いていない（目印が使えないため）。承認後に fact の目印を足す

## 提案
- facts：facts-proposal.yml
- 用語集：新しい語の提案なし

## 検査の結果
- check_page.py：書いた直後 エラー 0・警告 6、直した後 エラー 0・警告 4（助詞「に」「が」「にも」の重複。意味を保つため残した）

## 確かめていないこと
- 公式の 2 文書は束の写しに基づく。原文は開いていない（Web の取得 0）
- 公式のテストの条件、アプリで添付が本文のどこに置かれるか、Claude Code で `@` が並びに与える影響は未確認（本文に「未確認」と書いた）
- 雛形は動作を確かめていない
- デザイン固定化の研究（arxiv-2403-11164）は束の写し（11 C-15）の記述のみで、原文を見ていない

## 使用量
- 道具の呼び出し 17 回、Web の取得 0 回
