---
id: permission-modes-overview
title: 権限モードの選び方
aliases: [権限モードの全体像, permission modes, Manual・acceptEdits・plan・auto・dontAsk・bypassPermissions, Shift+Tab でモードを切り替える, auto モード]
type: feature
field: cli
chapter: 権限モードと計画
order: 40
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [境界がない, 合っていない]
pitfalls: []
scenes: [開発]
summary: 権限モードごとに何が確認なしで進むかを知り、作業の危うさと見ていられる度合いに合わせて選ぶ。既定は版で変わってきたので、手元の既定と確認の出方を確かめてから任せる。
signs:
  - {type: goal, text: 確認を減らしたいが、どのモードにすればよいか分からない}
  - {type: goal, text: 既定の権限モードで、何が確認なしで実行されるのか知りたい}
prerequisites: [agent-loop]
related: [what-auto-mode-stops, permission-rules, sandboxing, where-bypass-is-ok, default-safety-settings, approval-fatigue, protected-paths, destructive-commands, when-to-plan, settings-layers, wrong-amount-of-approvals, permission-modes-in-the-app, headless-basics#permissions, agent-teams]
tracks: [permission-modes, auto-mode]
outdated_advice: [approve-everything-first, yolo-skip-permissions]
sources: []
volatility: 中
sections:
  - {title: モードごとに確認なしで進むもの, anchor: modes}
  - {title: 既定のモードと版, anchor: defaults}
  - {title: 選び方の判断例, anchor: examples}
stage: stub
updated: 2026-11-04
---

## モードごとに確認なしで進むもの {#modes}

## 既定のモードと版 {#defaults}

## 選び方の判断例 {#examples}
