---
id: via-cloud-providers
title: Bedrock・Vertex AI・Foundry 経由で使う
nav_title: クラウドの提供元経由で使う
aliases: [Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry, クラウドの提供元]
type: feature
field: team
chapter: 管理と契約
order: 140
level: 任せる
priority: 任意
surfaces: [claude-code, api]
principle: [縛る]
prevents: [合っていない]
pitfalls: []
scenes: [チーム, 開発]
summary: Bedrock・Vertex AI・Foundry 経由で Claude Code を使い、組織のクラウドの契約と統制の中で動かせる。claude.ai の管理コンソールが使えないので、設定の配り方と使える機能の違いを先に確かめる。
signs:
  - {type: situation, text: 会社の AWS や Google Cloud の契約の中で Claude を使う}
  - {type: symptom, text: Bedrock 経由だと、使えない機能がある}
prerequisites: [check-billing-path]
related: [org-managed-settings-and-mcp, choosing-an-org-plan, audit-logs-and-telemetry, what-each-surface-cannot-do, where-your-data-goes, managed-settings-enforcement, github-actions-with-claude]
tracks: [cloud-providers, managed-settings]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
