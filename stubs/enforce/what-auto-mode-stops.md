---
id: what-auto-mode-stops
title: auto モードは何を止め、何を止めないか
aliases: [auto mode, オートモード, auto モードの分類器, 権限の分類器]
type: feature
field: enforce
chapter: 権限と封じ込め
order: 50
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [縛る]
prevents: [境界がない, 縛っていない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: auto モードの分類器が既定で止める操作と、すり抜けうる操作を知り、権限ルールやサンドボックスで補うものを決められる。auto モードは確認を減らす仕組みで、安全を保証しない。
signs:
  - {type: goal, text: auto モードに任せて大丈夫か}
  - {type: symptom, text: auto モードに操作を止められて、作業が進まない}
  - {type: goal, text: 確認なしで進めつつ、危ない操作だけは止めたい}
prerequisites: [permission-modes-overview]
related: [permission-rules, sandboxing, approval-fatigue, default-safety-settings, destructive-commands, protecting-secrets, where-bypass-is-ok, lethal-trifecta, permission-modes-in-the-app, wrong-amount-of-approvals, five-questions-before-delegating, headless-basics, when-to-lock, lock-side-effects]
tracks: [auto-mode, permission-modes]
outdated_advice: [approve-everything-first, yolo-skip-permissions]
sources: []
volatility: 中
sections:
  - {title: 既定で止めるもの・通すもの, anchor: defaults}
  - {title: すり抜けと限界, anchor: limits}
  - {title: 止められたときの見直し方, anchor: when-blocked}
  - {title: 面ごとの違い, anchor: by-surface}
stage: stub
updated: 2026-11-04
---

## 既定で止めるもの・通すもの {#defaults}

## すり抜けと限界 {#limits}

## 止められたときの見直し方 {#when-blocked}

## 面ごとの違い {#by-surface}
