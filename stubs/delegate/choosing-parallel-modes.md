---
id: choosing-parallel-modes
title: 並列の方式の選び方
aliases: [並列実行, Run agents in parallel, マルチエージェント]
type: comparison
field: delegate
chapter: 並べる
order: 90
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [見せる, 握る]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: 並列の方式を、誰が調整するか・同じファイルを触るか・互いに連絡が要るかで選べる。どの方式でも、結果を確かめる人の手間は本数に応じて増える。
signs:
  - {type: goal, text: 複数の作業を同時に進めたい}
  - {type: symptom, text: 並列の方法が多すぎて、どれを使えばいいか分からない}
prerequisites: [subagent-isolation]
related: [humans-set-the-parallel-limit, parallel-with-worktrees, agent-view-and-background, agent-teams, dynamic-workflows, batch-and-p-loops, compare-hypotheses-in-parallel, writing-subagents, skill-vs-subagent, research-in-subagents, independent-review, sandboxing, parallel-and-loop-costs, cloud-sessions-and-teleport]
tracks: [subagents, agent-view, agent-teams, workflows, worktrees, code-projects]
outdated_advice: [subagent-per-step, subagents-to-save-context]
sources: []
volatility: 中
sections:
  - {title: 誰が調整するか, anchor: who-coordinates}
  - {title: 同じファイルを触るか, anchor: same-files}
  - {title: 一部は捨てる前提で回す, anchor: expect-to-discard}
stage: stub
updated: 2026-11-04
---

## 誰が調整するか {#who-coordinates}

## 同じファイルを触るか {#same-files}

## 一部は捨てる前提で回す {#expect-to-discard}
