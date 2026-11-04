---
id: claims-done-but-isnt
title: 「完了」と言うが終わっていない
nav_title: 完了と言うが終わっていない
aliases: [偽の完了, 全部通ったと言うのに動かない, 完了の報告が信用できない]
type: symptom
field: symptoms
chapter: 完了と検証
order: 210
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [確かめる]
prevents: [見えていない, 確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, データ分析]
summary: 「完了」「全部通った」という報告が事実と違う原因を切り分け、完了の定義と証拠を渡す・別の者に確かめさせる、のどこから足すかを決める。
signs:
  - {type: symptom, text: 「全部通りました」と言うが信用できない}
  - {type: symptom, text: 完了と報告されたのに動かない}
  - {type: symptom, text: 計画したはずの確認を実際にはやっていない}
  - {type: symptom, text: 「ほかに該当する箇所はない」と言い切られたが残っていた}
wave: 1
prerequisites: [agent-loop]
related: [tests-first, fix-a-bug#no-symptom-patches, visual-checks, goal-until-done, stop-hooks, rewrote-tests-to-pass, misses-broken-evaluation, blames-the-tools, six-causes]
routes:
  - {cause: 見えていない, to: [define-done]}
  - {cause: 確かめていない, to: [evidence-not-reports, verification-ladder, independent-review]}
  - {cause: 預けすぎる, to: [over-reliance#cheap-verification, checking-unattended-runs]}
tracks: [goal, hooks]
outdated_advice: [add-double-check]
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
