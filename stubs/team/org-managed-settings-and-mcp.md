---
id: org-managed-settings-and-mcp
title: 組織に設定と MCP サーバーを配る
aliases: [managedMcpServers, MDM で配る, 設定の配布]
type: feature
field: team
chapter: 管理と契約
order: 120
level: 仕組みにする
priority: 任意
surfaces: [claude-code, app]
principle: [縛る]
prevents: [縛っていない, 境界がない]
pitfalls: []
scenes: [チーム]
summary: 組織の全員に設定と MCP サーバーの許可を配る経路（管理コンソール・MDM など）を選び、グループごとに設定を分けるかを決められる。許す MCP サーバーは、入れる前の確認を通したものに絞る。
signs:
  - {type: situation, text: 全社に Claude Code を配り、設定をそろえる}
  - {type: goal, text: 社員が使える MCP サーバーを、組織で決めたい}
  - {type: goal, text: 部署ごとに違う設定を配りたい}
prerequisites: [managed-settings-enforcement, share-team-settings]
related: [vetting-extensions, choosing-mcp-servers, connectors-in-the-app, paved-roads, audit-logs-and-telemetry, via-cloud-providers, choosing-an-org-plan, shared-projects-and-org-skills]
tracks: [managed-settings, mcp]
sources: []
volatility: 中
sections:
  - {title: 配る経路, anchor: delivery}
  - {title: グループごとに設定を分ける, anchor: per-group-settings}
  - {title: MCP サーバーの許可, anchor: mcp-allowlist}
stage: stub
updated: 2026-11-04
---

## 配る経路 {#delivery}

## グループごとに設定を分ける {#per-group-settings}

## MCP サーバーの許可 {#mcp-allowlist}
