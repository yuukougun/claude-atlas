---
id: seems-less-capable
title: 急に賢くなくなった気がする
aliases: [劣化した, 性能が落ちた, 前よりバカになった, 調子が悪い]
type: symptom
field: symptoms
chapter: 上限と速さ
order: 340
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる, 見せる]
prevents: [散らかっている, 合っていない]
pitfalls: [体感を信じる]
scenes: [開発, 文章]
summary: 急に賢くなくなった気がするときに、版・effort・モデル・会話の量の順に確かめ、体感ではなく同じ課題で比べて判断する。
signs:
  - {type: symptom, text: 急に性能が落ちた気がする}
  - {type: symptom, text: 前は一度でできたことができなくなった}
  - {type: symptom, text: 更新の後から答えが雑になった気がする}
wave: 1
prerequisites: [nondeterminism]
related: [current-models, choosing-a-model, context-rot, always-on-costs, harness-over-model, insights-and-usage-review, change-timeline-2026, checking-for-updates, human-pitfalls, forgets-in-long-chats, too-slow, six-causes]
routes:
  - {cause: 散らかっている, to: [when-to-start-fresh, inspect-context, isolate-with-safe-mode]}
  - {cause: 合っていない, to: [suspected-degradation#official-sources, effort-levels, after-switching-models]}
  - {cause: 体感を信じる, to: [suspected-degradation#measure, felt-vs-measured, measure-changes]}
tracks: [model-selection, effort, context-window]
outdated_advice: [think-hard-keywords]
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
