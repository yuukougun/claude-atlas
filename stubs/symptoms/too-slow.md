---
id: too-slow
title: 返事が遅い・時間がかかりすぎる
nav_title: 返事が遅い
aliases: [遅い, 重い, 考え込みすぎる, 待ち時間が長い]
type: symptom
field: symptoms
chapter: 上限と速さ
order: 330
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: 返事が遅い・時間がかかりすぎる原因を、effort とモデル、文脈の重さ、面の違いに分けて切り分け、速さと質のどちらを優先するかを決める。
signs:
  - {type: symptom, text: 返事が返ってくるまで時間がかかりすぎる}
  - {type: symptom, text: 簡単な質問なのに長く考え込む}
  - {type: symptom, text: 入れた拡張が多すぎて重い}
wave: 1
prerequisites: [rereads-whole-history]
related: [how-thinking-works, split-models-by-role, inspect-context, research-in-subagents, thinking-keywords, current-models, when-ai-is-unavailable, hits-limits-quickly, seems-less-capable, six-causes]
routes:
  - {cause: 散らかっている, to: [when-to-start-fresh, always-on-costs, pruning-extensions]}
  - {cause: 合っていない, to: [effort-levels, choosing-a-model, fast-mode-and-advisor]}
tracks: [effort, fast-mode, model-selection, mcp, plugins]
outdated_advice: []
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
