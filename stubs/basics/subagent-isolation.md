---
id: subagent-isolation
title: サブエージェントは別室の部下
aliases: [文脈の隔離, 別のコンテキストで調べさせる, 別室の部下]
type: concept
field: basics
chapter: コンテキストと注意
order: 70
level: 任せる
priority: 必須
surfaces: [claude-code, api]
principle: [見せる]
prevents: [散らかっている]
summary: サブエージェントは別のコンテキストで作業して要約だけを返すので本筋を散らかさずに済むが、賢くはならずトークンは余分にかかることが分かる。向くのは並列の作業・うるさい出力の切り離し・独立したレビューである。
signs:
  - {type: goal, text: 調べものを別の担当に任せると、何が得で何が損か知りたい}
prerequisites: [attention-budget]
related: [research-in-subagents, writing-subagents, what-subagents-dont-inherit, skill-vs-subagent, independent-review, choosing-parallel-modes, agent-loop]
tracks: [subagents]
outdated_advice: [subagents-to-save-context, tell-it-to-use-subagents, subagent-per-step]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
