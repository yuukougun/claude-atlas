---
id: share-team-settings
title: チームで設定を共有する
aliases: [.claude/settings.json, 共有の設定]
type: recipe
field: team
chapter: 導入と決まり
order: 30
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
pitfalls: []
scenes: [チーム, 開発]
summary: CLAUDE.md・共有の設定・MCP の設定・プラグインをリポジトリに入れ、チームで同じ前提と縛りで Claude Code を使える。個人の好みと秘密は共有のファイルに入れない。
signs:
  - {type: goal, text: チームで同じ設定を使いたい}
  - {type: symptom, text: 人によって Claude Code の振る舞いが違う}
prerequisites: [settings-layers, permission-rules]
related: [what-to-put-in-claude-md, claude-md-length#team, agents-md, connecting-mcp, plugins-and-marketplaces, protected-paths, protecting-secrets, vetting-extensions, before-opening-unknown-repos, managed-settings-enforcement, org-managed-settings-and-mcp, rolling-out-to-teams]
tracks: [settings, claude-md, mcp, plugins, permissions]
sources: []
volatility: 中
sections:
  - {title: 共有するものと個人に残すもの, anchor: shared-vs-personal}
  - {title: 信頼してから効く設定, anchor: after-trust}
stage: stub
updated: 2026-11-04
---

## 共有するものと個人に残すもの {#shared-vs-personal}

## 信頼してから効く設定 {#after-trust}
