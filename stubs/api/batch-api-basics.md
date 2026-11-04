---
id: batch-api-basics
title: Message Batches API（急がない大量の処理）
nav_title: Message Batches API
aliases: [Batch API, バッチ処理]
type: feature
field: api
chapter: API の主な機能
order: 70
level: 回す
priority: 任意
surfaces: [api]
principle: [確かめる]
prevents: [合っていない]
scenes: [開発, データ分析]
summary: 急がない大量の要求を一括で非同期に処理させ、費用を抑えられる。評価や一括の生成に向き、対話や待てない処理に向かない理由が分かる。
signs:
  - {type: goal, text: 急がない大量の処理を安く流したい}
  - {type: goal, text: 評価用の大量のプロンプトをまとめて実行したい}
prerequisites: [stateless-messages-api]
related: [checking-unattended-runs, measure-changes, reading-api-pricing, prompt-caching-in-practice, rate-limits-and-errors, choosing-automation, batch-and-p-loops]
tracks: [batch-api]
sources: []
volatility: 中
sections:
  - {title: 向く仕事・向かない仕事, anchor: fit}
stage: stub
updated: 2026-11-04
---

## 向く仕事・向かない仕事 {#fit}
