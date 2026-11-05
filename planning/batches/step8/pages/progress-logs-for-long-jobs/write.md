# write.md：progress-logs-for-long-jobs

## 書いたファイル
- docs/delegate/progress-logs-for-long-jobs.md（stage draft。front matter は sections・sources・stage・updated のみ変更。sources は既存の 4 件）
- snippets/progress-logs-for-long-jobs/progress-writer.py・.expect.yaml、watch-request.txt・.expect.yaml
- planning/batches/step8/pages/progress-logs-for-long-jobs/facts-proposal.yml
- data/sources.d は新しい出典がないので作っていない

## 必ず持つものの対応
- 冒頭の要点：冒頭の `!!! abstract`
- 手順：#steps（各段に「終わり」の確かめを付けた）
- 確かめる・縛るのページへの道：#guards（checking-unattended-runs#guards-first・goal-until-done#writing-conditions・agent-view-and-background#guards-first）と、#check（checking-unattended-runs#records）。前提は progress-files
- level：仕組みにする（front matter のまま）
- 構成の目安（要点→守り→手順→確かめ方→失敗したとき）：#guards → #steps → #templates → #check → #vs-progress-files（足した）→ #troubleshoot

## メインに判断してほしいこと
- 「ログが大きすぎて監視できなかった例」の（根拠：中）は、目次の materials（11 の p34#168）の評価に拠る。公開の出典がなく、sources に載せていない。出典を足すか、印を（根拠：弱）にするか
- hook-monitor-min-version（facts、status 未確認）を目印で使った。確認済みにするか、本文を直すか

## 提案
- 数値の提案：facts-proposal.yml（Monitor の見張りの期限 3 件と、制限環境での最低の版）。本文は数字を書かず、目印も置いていない。取り込んだら #steps の「見張りには期限があり」の所に目印を置く
- 用語集：Monitor（道具）の定義が本文に短くあるだけ。用語の追加はしていない

## 検査の結果
- check_page.py を 2 回流した。エラー 0、警告 1
- 残した警告：要点の囲みの「Claude にも人にも」の助詞の重複（front matter の summary と同じ文にそろえたため）

## 確かめていないこと
- 雛形の Python を実際に流していない（読んで確かめただけ）
- Monitor の挙動は tools-reference（2026-11-05 に取得）に拠る。ほかの OS と IDE 拡張、Windows の Git Bash の条件は書いていない
- 「grep で絞ってから Monitor に流す」形の具体的なコマンドは載せていない（依頼の文で指示する形にした）

## 使用量
- 道具の呼び出し：約 20 回、Web の取得：1 回（tools-reference）
