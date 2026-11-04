---
id: dynamic-workflows
title: dynamic workflows（スクリプトで多数のサブエージェントを動かす）
nav_title: dynamic workflows
aliases: [ultracode, workflows, /workflows, ワークフロー, /deep-research]
type: feature
field: delegate
chapter: 並べる
order: 130
level: 回す
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [合っていない, 確かめていない]
pitfalls: []
scenes: [開発, 調べもの]
summary: Claude が書いたスクリプトで多数のサブエージェントを動かし、コードベース全体の監査や大量のファイルの移行を背景で進められる。費用が大きくなりやすいので、小さな範囲で試してから広げる。
signs:
  - {type: goal, text: コードベース全体の監査や大規模な移行を、一度に進めたい}
  - {type: symptom, text: ワークフローで動かしたら、思ったより利用枠を使った}
prerequisites: [choosing-parallel-modes, permission-rules]
related: [parallel-and-loop-costs, sandboxing, hooks-basics, independent-review, checking-unattended-runs, batch-and-p-loops, agent-teams, research-in-subagents, humans-set-the-parallel-limit, refactor-and-migrate, effort-levels]
tracks: [workflows, effort]
outdated_advice: [workflow-keyword-extra-usage]
sources: []
volatility: 中
sections:
  - {title: 向く規模と、小さく試す, anchor: when-and-start-small}
  - {title: 担当にも効く縛り、確かめていない縛り, anchor: guards-for-workers}
stage: stub
updated: 2026-11-04
---

## 向く規模と、小さく試す {#when-and-start-small}

## 担当にも効く縛り、確かめていない縛り {#guards-for-workers}
