# write.md：model-based-grading（recipe・eval）

## 書いたファイル
- `docs/eval/model-based-grading.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources に 2 件、sections に 3 節を足した）
- `snippets/model-based-grading/grader-prompt.md`・`.expect.yaml`（採点の依頼）
- `snippets/model-based-grading/review-disagreements.md`・`.expect.yaml`（食い違いの読み直し）
- `data/sources.d/model-based-grading.yml` は作っていない（出典は既存の data/sources.yml の 2 件で足りた）
- front matter で変えたキー：`sections`（write-grader・keep-checking・when-it-fails を足した。既存の 3 つの anchor は変えず）・`sources`・`stage`・`updated`

## 必ず持つものの対応
- 用途ごとの進め方：#calibrate（手順 1〜5）と #write-grader
- 手順（各段に確かめ）：#calibrate の各段の「終わりの確認」
- 確かめる・縛るのページへの道：#prefer-code（verifier-three-conditions#tamper-proof、measure-changes#graders、textlint-hook）・#calibrate（measure-changes#small-eval・#how-many-runs）。前提の 2 ページは要点の囲みで指す
- level：front matter の「仕組みにする」（変えていない）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：要点 → #prefer-code → #write-grader・#calibrate → #what-the-judge-sees・#keep-checking → #when-it-fails

## メインに判断してほしいこと
- 手順の「人が先に採点した例を集める」の件数は書いていない。公式の評価の記事の「20〜50 個のタスク」は、数値の提案にせず、measure-changes#small-eval を指すにとどめた。必要なら数値の提案を別に起こしてほしい
- 「人の点を見せる前に採点役の点を人に見せない」「一致の線は結果を見る前に決める」「測る例は依頼の例と分ける」は、束の材料（hold-out は人が持つ、聞き方で迎合が増える）からの運用上の整理であり、出典付きの主張ではない。本文は断定の形にしたが、根拠の印は付けていない。弱いと判断するなら（推論・実践例なし）の印を足してほしい
- 失敗したときの節は、症状ページ（misses-broken-evaluation など）を束の指せる節に含まないので指していない。振り分けたければ、related への追加の提案が要る

## 提案
```yaml
frontmatter: []
```
- 用語集：「較正（calibrate）」「判定役／採点役」を、このページでは「採点役の点を人の点に近づけるために採点の依頼を直す作業」と短く定義して使った。用語集に無ければ追加の提案
- 数値の提案：なし（本文に変わりやすい値を書いていない）

## 検査の結果
- 1 回目：エラー 1（prh：Harness を「ハーネス」に）・警告 10
- 直した後の 2 回目：エラー 0・警告 5
- 残した警告（誤検出に近い）：助詞「に」「が」の重複 4 件（60・112・148・192 行。リンクの題名が入った文と、並列の文）、読点 4 つ以上 1 件（120 行）。検証の担当に任せる

## 確かめていないこと
- 2 つの雛形の動作（採点役が判定不能を返すか、など）は実行していない
- 公式の評価の記事とハーネス設計の記事の内容は、束の写しに基づく。原文は開いていない（Web の取得は 0 回）
- Harness design の報告の対象のモデル・世代は束にないので、本文は「特定のモデルの傾向として一般化しない」と書いた
- アプリ・Claude Code・API のタブは、一般的な分け方の記述であり、各面での挙動を確かめていない
- 本文のリンクの表示（準備中の相手）は gen_site の出力に従う

## 使用量
- 道具の呼び出し：約 17 回（Read 3・Bash 7・Write 5・Edit 9。うち Edit は検査後の直しを 1 回にまとめた分）、Web の取得：0 回
