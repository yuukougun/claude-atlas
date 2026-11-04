# write：evidence-not-reports

## 書いたファイル
- docs/verify/evidence-not-reports.md（stub から移した。stage draft、updated 2026-11-05。sections に what-happens・what-it-prevents・misconceptions を足し、sources に 5 件〔cc-docs-best-practices・cc-issue-46940・cc-issue-64286・cc-changelog・cc-docs-changelog、いずれも data/sources.yml にある〕を入れた）
- snippets/evidence-not-reports/report-with-evidence.md と .expect.yaml（目次の案の「改善を報告させる形式」）
- planning/batches/step8/pages/evidence-not-reports/facts-proposal.yml
- data/sources.d/evidence-not-reports.yml は作っていない（出典はすべて既存の id）

## 必ず持つものの対応
- 原理・原因の名指し（principle＝確かめる、prevents＝確かめていない、pitfalls は空）：#what-it-prevents（冒頭の導入にも「確かめる」）
- level（整える）と、要点の最初が「何が分かるか」：front matter と冒頭の要点の囲み
- 構成の目安「何が起きるか（例）」：#what-happens
- 同「なぜそうなるか（比喩付きの図）」：#what-happens の末尾に仕組みの説明を置いた。比喩付きの図は置いていない（一覧に合う比喩がなく、代わりに #what-counts の表で対比を示した）
- 同「何に効くか」：#what-it-prevents
- 同「誤解」：#misconceptions
- 同「関連」：末尾の page-links の目印（テンプレートが出す）

## メインに判断してほしいこと
- 目次の visual の案（「全部通りました」と、コマンド・生の出力・分母を並べた対比の図）は、図を作らず #what-counts の表で代えた。図が要るなら別の担当に
- 研究資料 11 p12#114（ALE-Agent が計算量を見誤り TLE を繰り返す）は入れていない。第三者のエージェントを失敗の文脈で名指しするのを避け、一次資料も開いていないため

## 提案
- 数値：facts-proposal.yml（2 件。直った版 v2.1.317 と v2.1.314）。本文は版を書かず「直った版は CHANGELOG で確かめる」としてあるので、facts に入ったら #tool-output に fact の目印を置く
- front matter の変更の提案：なし

## 検査の結果
- check_page.py を 2 回。1 回目 エラー 0・警告 5（冗長な表現・助詞の連続・読点の数）。直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 事例 1・2 の数字（4992/4992 など）と日付・モデル名は、束の写し（research/05）のまま。GitHub の原典は開いていない
- CHANGELOG の 2 件の不具合の記述は research/22 の写し。原文と版は未確認
- 「出力を読むほうが再実行より速い」「見ていなかったセッションでは唯一の証拠」は research/05 の Best practices の写し。現行の原文は未確認
- 「Claude 自身が後から述べた」の言い回しは #64286 の写しによる。原文は未確認
- 判断例 2 件と表・箇条の `grep`／`git diff`／`git status` の例は、この辞典の推奨としての書き下ろしで、実際の動作は試していない
- 雛形は動作を試していない

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
