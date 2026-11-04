# write.md：checking-unattended-runs（recipe・verify）

## 書いたファイル
- `docs/verify/checking-unattended-runs.md`（stub から移して執筆。stage は draft）
- front matter で変えたキー：`sections`（guards-first と when-it-fails を足した。既存の 3 つの anchor はそのまま）・`stage`（draft）・`updated`（2026-11-05）・`sources`（cc-docs-best-practices・cc-docs-headless・cc-changelog・cc-issue-46940・cc-issue-64286。いずれも data/sources.yml にある id）
- `snippets/checking-unattended-runs/unattended-checklist.md` と `.expect.yaml`（目次の templates の点検表）
- `snippets/checking-unattended-runs/check-after-run.sh` と `.expect.yaml`（分かりやすさのために足した、実行の後に確かめるスクリプト）
- `data/sources.d/checking-unattended-runs.yml`（新しい出典なし。`sources: []`）

## 必ず持つものの対応
- 手順：`#records`（5 段。各段に「終わったとみなす条件」を付けた）
- 確かめるページへの道：front matter の `prerequisites`（verification-ladder）と本文の `#guards-first`（verification-ladder#choose-step）・`#beyond-exit-codes`（evidence-not-reports）・`#records`（diffs-humans-must-read）・`#final-decision`（independent-review・automated-pr-review）
- 縛るページへの道：`#guards-first`（headless-basics#limits・github-actions-with-claude#secrets-and-permissions・cloud-schedules#least-privilege）と `related` の what-auto-mode-stops
- 比例則（監督が少ないほど確かめを強める）：`#guards-first`（five-questions-before-delegating#proportional-guards）と `#final-decision`
- 構成の目安：要点（冒頭）→ 先に整える守り（`#guards-first`）→ 手順（`#records`）→ 確かめ方（`#beyond-exit-codes` の表と `#final-decision`）→ 失敗したとき（`#when-it-fails`）
- level：回す（stub のまま）

## メインに判断してほしいこと
- 目次の備考にある「注釈付きのセッション記録」（制作のワークフローの無人の実行を、報告・記録・始めと終わりの HEAD の比較で確かめた例。DR-08 の H3）は、制作の環境の記録を渡されていないため載せていない。載せるなら、記録の材料を別に渡してほしい
- `fact` の目印に使った 2 件（claude-code-p-startup-failure-exit-code-fix-version・auto-mode-no-verdict-display-fixed）は data/facts.yml で status が未確認（CHANGELOG の原文を開いていない）。確認済みになるまで、本文の版の記述も未確認のまま

## 提案
- front matter・用語集・data への提案はなし

## 検査の結果
- `check_page.py` を 2 回流した。1 回目はエラー 0・警告 6（助詞の重なり・文の長さ・読点）、直した後はエラー 0・警告 1（助詞「に」の重なり）。その警告の文を短くして直したが、直した後の再検査は 2 回の上限のため流していない

## 確かめていないこと
- 雛形の 2 つ（点検表・スクリプト）は動かしていない。スクリプトの `npm test` と grep の動きは未確認
- CHANGELOG（版 2.1.314・2.1.316・2.1.317）の原文は開いていない。束の research/22 と data の写しに基づく
- GitHub の 2 件の報告（#46940・#64286）は、束の research/05 の写しに基づき、原文を開いていない。モデルの名と日付も写しのまま
- 「ブランチの保護で main への直接の push を許さない」は、束の research/05 5-1（最終決定権はブランチ保護とマージを承認する人間に置く）に基づく。設定の手順は書いていない
- Claude Code 以外の OS・IDE 拡張の動作は未確認

## 使用量
- 道具の呼び出し：約 14 回（Read 2、Bash 7、Write 7、Edit 1）。Web の取得：0 回
