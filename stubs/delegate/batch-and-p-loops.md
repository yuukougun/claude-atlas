---
id: batch-and-p-loops
title: 多数のファイルに同じ作業を流す（/batch と -p のループ）
nav_title: /batch と -p のループ
aliases: [fan-out（旧い語）, 一括の変更, 大量のファイルの変更]
type: feature
field: delegate
chapter: 並べる
order: 140
level: 回す
priority: 任意
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: /batch や claude -p のループで、多数のファイルに同じ作業を分けて流せる。まず数件で試してプロンプトと許可を直し、結果を確かめてから全件に広げる。
signs:
  - {type: goal, text: 数百のファイルに同じ変更を入れたい}
  - {type: symptom, text: 一括で流したら、壊れた結果がどれか分からなくなった}
prerequisites: [headless-basics, parallel-with-worktrees]
related: [dynamic-workflows, goal-until-done, permission-rules, sandboxing, checking-unattended-runs, bare-mode, refactor-and-migrate, parallel-and-loop-costs, batch-api-basics]
tracks: [headless, worktrees, batch-command]
sources: []
volatility: 中
sections:
  - {title: API の Message Batches API とは別のもの, anchor: not-the-batch-api}
stage: stub
updated: 2026-11-04
---

## API の Message Batches API とは別のもの {#not-the-batch-api}
