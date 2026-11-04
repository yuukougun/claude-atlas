# write.md：how-usage-limits-work（執筆）

## 書いたファイル
- docs/cost/how-usage-limits-work.md（stub から移動。stage を draft、updated を 2026-11-05、sources を 8 件に。sections に cause・misconceptions を足した。ほかのキーは変えていない）
- docs/img/how-usage-limits-work/shared-limit.svg（3 つの面が 1 つの枠へ向かう図）
- facts-proposal.yml（数値の提案 4 件）
- 雛形・data/sources.d は無し（目次の templates が空。出典は data/sources.yml の既存の id だけ）

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の囲み。level は front matter（使う）
- どの原理・原因に関わるか：#cause（prevents「合っていない」を名指し。principle と pitfalls は空なので名指すものがない）
- 型の構成の目安：何が起きるか＝#shared-limit、なぜ＝#shared-limit・#limit-types（図）、何に効くか＝#cause、誤解＝#misconceptions、関連＝page-links の目印

## メインに判断してほしいこと
- 節 limit-types の題は「（プランごとの表）」だが、表にする数値が facts にないため表の目印を置いていない（置くと検査が止まる）。facts-proposal.yml の usage-limit-types-by-plan を採るなら、節に `<!-- gen:begin fact-table usage-limit-types-by-plan -->` の組を足す。採らないなら題から「（プランごとの表）」を外すか、choosing-a-plan の表への link のままにする（今はそうしている）。Team の席ごとの値は束に材料がなく null にした
- auto-continue-max-times・wrap-up-allowance-frequency・wrap-up-allowance-min-version を採ったら、#when-you-hit-the-limit の「続ける回数には上限がある」「回数はプランで違う」「新しい版が要る」の所に fact の目印を足す（今は数字なしで読める形）
- 用語集に「利用上限」の項があるか確かめていない。本文は題名どおり「利用上限」、別名の行に「利用制限」「使用制限」

## 提案
- 数値：facts-proposal.yml（used_in つき）
- front matter：なし

## 検査の結果
- check_page.py を 2 回。1 回目は警告 3（文の長さ 1・読点 1・算用数字 1）、直して 2 回目はエラー 0・警告 0

## 確かめていないこと
- 一次資料を開いていない（Web の取得 0 回）。束の写しだけに基づく。Settings > Usage に戻る時刻が出るか、Claude Code の上限の知らせに戻る時刻が出るかは未確認なので書いていない
- 「アプリは別の枠だから響かない」「新しい会話で新しい枠」の誤解の項は、共有の仕組みと 02 §2-2 から導いた。公式の文にその形の誤解が書かれているわけではない
- 上げたプランの新しい上限がすぐ適用される点は、research/02 §2-2 の写し（2026-10-29 確認）による。Ultra 改名より前の確認なので、現状の確認が要る
- Desktop の面の固有の動作（タブは app と claude-code の 2 面だけ）。Windows・macOS の Claude Code は未確認（CLI の動作は WSL・Linux を基準）

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
