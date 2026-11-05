# write.md：claude-code-surfaces

## 書いたファイル
- docs/surfaces/claude-code-surfaces.md（stub は前の作業で docs へ移し済み。stage を draft、updated を 2026-11-05、sources を data/sources.yml にある 7 件、sections に combine を足した）
- 雛形・図・data/sources.d は作っていない（目次の templates と visual が「なし」。出典は既存の id で足りた）

## 必ず持つものの対応
- 比較の表（compare の目印）：#comparison-table
- 判断例：#how-to-choose（3 件）
- 要点 → 表 → 選び方 → 組み合わせ方の順：same-loop → comparison-table → how-to-choose → combine
- level を持つ：front matter（整える）
- 比べるのは混同されやすい組だけ：面の窓口（Web・モバイルがクラウドか Remote Control か）を #same-loop に置いた

## メインに判断してほしいこと
- 表の「Desktop アプリの Claude Code」の行が、このページ自身へのリンクになる（data の page がこのページのため）。自己リンクのままでよいか
- 表の行は 4 機能で、ターミナルの行がない。ターミナルの CLI は基準として本文で触れた

## 提案
- なし（数値・front matter の提案はない）

## 検査の結果
- 1 回目：エラー 3（skills の表記）・警告 6。直した後 2 回目：エラー 0・警告 5
- 残した警告 5：助詞の重なり 4 件と読点 1 件。リンクの目印の間に道具が入れる題名が長く、文を短くしても出る（line 56 は目印の外だが誤検出と見て残した）

## 確かめていないこと
- IDE の拡張・Desktop・Remote Control の動作は、束の公式文書の写しによる。試していない。WSL・Linux 以外の OS は未確認と本文に書いた
- Linux の Desktop アプリが beta である点は、成熟度の値なので本文に書かず、表に任せた（表では全行共通の GA と出るため、読者に伝わらない恐れがある。data の note にしかない）
- 「手元のセッションをつなぎ続けるには手元の PC を動かし続ける」は、束の記述（実行は手元に残る）からの読みで、本文の組み合わせ方に書いた
- using-ides は未公開のため、link は「準備中」になる

## 使用量
- 道具の呼び出し：約 10 回。Web の取得：0 回
