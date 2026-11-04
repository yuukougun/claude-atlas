---
id: sym-a
title: 指示が守られない（試験用）
aliases: [指示を無視される, ルールを破られる]
type: symptom
field: symptoms
chapter: 指示と仕組み
order: 10
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [縛る, 見せる]
prevents: [散らかっている, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 書いた規則が破られる原因を切り分け、どれを仕組みに移すかを決める。
signs:
  - {type: symptom, text: 書いたのに守られない}
  - {type: symptom, text: 長い会話の途中から無視される}
wave: 1
prerequisites: [concept-a]
related: [guide-a, concept-b#nope, feat-c#lock]
routes:
  - {cause: 散らかっている, to: [feat-a, concept-b#lock]}
  - {cause: 縛っていない, to: [feat-c, ghost-page]}
tracks: [claude-md]
outdated_advice: [old-tip]
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}
