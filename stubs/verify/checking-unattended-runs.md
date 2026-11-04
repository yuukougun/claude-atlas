---
id: checking-unattended-runs
title: 無人実行の結果を確かめる
aliases: [無人実行の検証, headless の結果を確かめる, 夜間の実行の確認]
type: recipe
field: verify
chapter: 完了を確かめる
order: 50
level: 回す
priority: 推奨
surfaces: [app, claude-code, api]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, チーム]
summary: 人が見ていない実行の結果を、終了コードや要約だけでなく、出力・記録・差分で確かめられる。監督が少ないほど確かめを強め、最後の判断は人とブランチの保護に置く。
signs:
  - {type: situation, text: 夜間や CI で、人が見ていない間に Claude を動かしている}
  - {type: symptom, text: 無人で回した結果は成功だったのに、中身が壊れていた}
  - {type: symptom, text: 止まった理由が分からないまま、無人の実行が終わっている}
  - {type: goal, text: 無人の実行の結果を、毎回全部読まずに信頼したい}
prerequisites: [verification-ladder]
related: [headless-basics, five-questions-before-delegating, progress-logs-for-long-jobs, github-actions-with-claude, cloud-schedules, tasks-and-schedules-in-the-app, automated-pr-review, choosing-automation, what-auto-mode-stops, evidence-not-reports, independent-review, diffs-humans-must-read]
tracks: [headless, github-actions, scheduled-tasks]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 終了コードと要約だけで決めない, anchor: beyond-exit-codes}
  - {title: 記録と差分で確かめる, anchor: records}
  - {title: 最後の判断を人に置く, anchor: final-decision}
stage: stub
updated: 2026-11-04
---

## 終了コードと要約だけで決めない {#beyond-exit-codes}

## 記録と差分で確かめる {#records}

## 最後の判断を人に置く {#final-decision}
