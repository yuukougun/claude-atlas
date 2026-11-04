---
id: wrong-amount-of-approvals
title: 承認の確認が多すぎる・少なすぎる
aliases: [許可を何度も求められる, 確認なしで実行される]
type: symptom
field: symptoms
chapter: 安全と承認
order: 310
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 握る]
prevents: [合っていない, 境界がない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: 承認の確認が多すぎて読まずに押す、または少なすぎて怖いときに、権限モード・権限ルール・サンドボックスのどれを調整するかを、任せる段階に合わせて決める。
signs:
  - {type: symptom, text: 確認ボタンを読まずに押している}
  - {type: symptom, text: 許可を求められる回数が多すぎて作業にならない}
  - {type: symptom, text: 確認なしで実行されて怖い}
wave: 1
prerequisites: []
related: [where-bypass-is-ok, protected-paths, settings-layers, keeps-stopping, deleted-something-important, parallel-fatigue, lock-side-effects, six-causes]
routes:
  - {cause: 合っていない, to: [permission-modes-overview, permission-rules, permission-modes-in-the-app]}
  - {cause: 境界がない, to: [sandboxing, what-auto-mode-stops]}
  - {cause: 預けすぎる, to: [approval-fatigue, default-safety-settings#by-stage]}
tracks: [permission-modes, auto-mode, permissions, sandbox]
outdated_advice: [yolo-skip-permissions, approve-everything-first]
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
