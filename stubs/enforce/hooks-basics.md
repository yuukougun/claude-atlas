---
id: hooks-basics
title: フックの考え方とイベント
aliases: [hooks, フックイベント, hook events]
type: feature
field: enforce
chapter: フック
order: 90
level: 仕組みにする
priority: 必須
surfaces: [claude-code, api]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発]
summary: フックで、決まったきっかけに必ずスクリプトを走らせ、規則を確実に守らせる仕組みが分かる。止める・整える・知らせるのそれぞれに、どのイベントを使うかを選べる。
signs:
  - {type: goal, text: ファイルを編集するたびに、必ず何かを実行したい}
  - {type: goal, text: Claude に頼まずに、規則を毎回確実に守らせたい}
  - {type: symptom, text: 設定したフックが動いていないように見える}
prerequisites: [when-to-lock, agent-loop]
related: [block-with-exit-2, hook-recipes, writing-safe-hooks, stop-hooks, hook-vs-skill, request-lock-table, extensions-at-a-glance, settings-layers, writing-subagents, textlint-hook]
tracks: [hooks]
sources: []
volatility: 中
sections:
  - {title: 代表的なイベント, anchor: events}
  - {title: 置き場所と効く範囲（サブエージェントと信頼の確認）, anchor: locations}
  - {title: 決定的なフックと、モデルが判断するフック, anchor: deterministic}
stage: stub
updated: 2026-11-04
---

## 代表的なイベント {#events}

## 置き場所と効く範囲（サブエージェントと信頼の確認） {#locations}

## 決定的なフックと、モデルが判断するフック {#deterministic}
