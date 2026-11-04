---
id: long-running-agent-context
title: 長時間エージェントのコンテキスト管理
aliases: [compaction（API）, context editing, memory tool, コンテキスト編集]
type: concept
field: api
chapter: エージェントを組む
order: 110
level: 回す
priority: 推奨
surfaces: [api]
principle: [見せる]
prevents: [散らかっている]
scenes: [開発]
summary: 長く動くエージェントで文脈が溢れないよう、要約・古い結果の削除・外部の記憶をどう組み合わせるかが分かる。何を文脈に残し、何をファイルに出すかも判断できる。
signs:
  - {type: goal, text: 何時間も動くエージェントの文脈が溢れないようにしたい}
  - {type: symptom, text: API で組んだエージェントを長く動かすと、前に決めたことを忘れる}
prerequisites: [what-survives-compaction, stateless-messages-api]
related: [checking-unattended-runs, progress-logs-for-long-jobs, progress-files, handoff-documents, compact-and-auto-compact, feature-to-api-mapping, agent-sdk-basics, using-auto-memory]
tracks: [api-compaction, context-editing, memory-tool]
sources: []
volatility: 高
sections:
  - {title: 三つの手段（compaction・context editing・memory tool）, anchor: three-tools}
  - {title: 状態をファイルに持たせる, anchor: external-state}
stage: stub
updated: 2026-11-04
---

## 三つの手段（compaction・context editing・memory tool） {#three-tools}

## 状態をファイルに持たせる {#external-state}
