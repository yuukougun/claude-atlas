---
id: managed-settings-enforcement
title: 管理設定と組織の強制
aliases: [managed settings, managed-settings.json, server-managed settings, 組織の設定で強制する]
type: feature
field: enforce
chapter: 権限と封じ込め
order: 80
level: 仕組みにする
priority: 任意
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない, 境界がない]
pitfalls: []
scenes: [チーム]
summary: 管理設定で、利用者の設定では外せない規則を組織として強制できる。優先の順番と、bypassPermissions や auto モードを使えなくする設定が分かる。
signs:
  - {type: situation, text: チームの全員に、同じ禁止を必ず守らせたい}
  - {type: goal, text: --dangerously-skip-permissions を組織で使えなくしたい}
prerequisites: [permission-rules, settings-layers]
related: [org-managed-settings-and-mcp#delivery, share-team-settings, where-bypass-is-ok, what-auto-mode-stops, permission-modes-overview, ai-usage-guidelines, paved-roads, audit-logs-and-telemetry, choosing-an-org-plan]
tracks: [managed-settings, settings, permission-modes]
sources: []
volatility: 中
sections:
  - {title: 優先の順番, anchor: precedence}
  - {title: モードを使えなくする設定, anchor: disable-modes}
  - {title: 利用者の側から外せない範囲, anchor: cannot-override}
stage: stub
updated: 2026-11-04
---

## 優先の順番 {#precedence}

## モードを使えなくする設定 {#disable-modes}

## 利用者の側から外せない範囲 {#cannot-override}
