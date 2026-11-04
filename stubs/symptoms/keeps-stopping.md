---
id: keeps-stopping
title: 確認ばかりで進まない・途中で止まる
aliases: [途中で止まる, 提案だけで止まる, 毎回確認してくる]
type: symptom
field: symptoms
chapter: 返答と品質
order: 30
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 合っていない]
pitfalls: []
scenes: [開発]
summary: 確認ばかりで進まない・途中で止まる原因を、提案か実行かの伝え方、権限モード、モデルと effort の癖に分けて切り分け、最後まで進めさせる手を選ぶ。
signs:
  - {type: symptom, text: 提案だけで止まり、実行してくれない}
  - {type: symptom, text: 「続けますか」と毎回聞いてくる}
  - {type: symptom, text: 長い作業を途中でやめて報告してくる}
  - {type: symptom, text: 理由を言わずに止まっている}
wave: 1
prerequisites: [agent-loop]
related: [ask-for-outcomes, goal-until-done, permission-to-stop, what-auto-mode-stops#when-blocked, lock-side-effects, wrong-amount-of-approvals, does-more-than-asked, refused-or-blocked, six-causes]
routes:
  - {cause: 見えていない, to: [suggest-or-do, define-done]}
  - {cause: 合っていない, to: [effort-levels, model-quirks, permission-modes-overview]}
tracks: [effort, permission-modes, goal]
outdated_advice: [keep-going-dont-be-lazy]
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
