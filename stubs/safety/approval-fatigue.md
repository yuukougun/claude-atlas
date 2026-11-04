---
id: approval-fatigue
title: 承認疲れ
aliases: [approval fatigue, 確認を読まずに押す, 承認のしすぎ]
type: judgment
field: safety
chapter: 既定と承認
order: 20
level: 整える
priority: 推奨
surfaces: [claude-code, app]
principle: [握る, 縛る]
prevents: [境界がない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: 確認が多いと中身を読まずに承認するようになり、確認が安全の仕組みとして働かなくなる理由が分かる。確認を auto モード・allow ルール・サンドボックスで減らし、残す確認を絞れる。
signs:
  - {type: goal, text: どの確認を残し、どれを減らすかを決めたい}
  - {type: goal, text: 確認を減らしても、残した確認は中身を読んで判断したい}
prerequisites: [permission-modes-overview]
related: [what-auto-mode-stops, permission-rules, sandboxing, wrong-amount-of-approvals, keeps-stopping, over-reliance, review-bottlenecks, permission-modes-in-the-app, default-safety-settings]
tracks: [auto-mode, permission-modes]
outdated_advice: [approve-everything-first]
sources: []
volatility: 中
sections:
  - {title: なぜ読まなくなるか, anchor: why}
  - {title: 確認を減らす順番, anchor: reduce-prompts}
  - {title: 残す確認を選ぶ, anchor: keep-prompts}
stage: stub
updated: 2026-11-04
---

## なぜ読まなくなるか {#why}

## 確認を減らす順番 {#reduce-prompts}

## 残す確認を選ぶ {#keep-prompts}
