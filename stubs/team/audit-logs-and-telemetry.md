---
id: audit-logs-and-telemetry
title: 監査ログと可視化（OpenTelemetry など）
nav_title: 監査ログと可視化
aliases: [Compliance API, 利用状況の記録, Analytics API]
type: feature
field: team
chapter: 管理と契約
order: 130
level: 仕組みにする
priority: 任意
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない, 境界がない]
pitfalls: []
scenes: [チーム]
summary: 組織での Claude の使われ方を、監査ログ・OpenTelemetry・使用量の集計で記録して見られる。何が記録され、何が記録されないかを先に確かめる。
signs:
  - {type: goal, text: 社内で Claude がどう使われているか、記録して見たい}
  - {type: situation, text: 監査のために、AI の利用の記録を求められた}
prerequisites: [org-managed-settings-and-mcp]
related: [where-your-data-goes, disclosure-and-provenance, choosing-an-org-plan, what-uses-up-limits#find-what-uses-it, insights-and-usage-review, via-cloud-providers, managed-settings-enforcement]
tracks: [otel-telemetry, usage-analytics-api, plans]
sources: []
volatility: 中
sections:
  - {title: 記録されるもの、されないもの, anchor: what-is-recorded}
  - {title: 管理していない端末, anchor: unmanaged-devices}
stage: stub
updated: 2026-11-04
---

## 記録されるもの、されないもの {#what-is-recorded}

## 管理していない端末 {#unmanaged-devices}
