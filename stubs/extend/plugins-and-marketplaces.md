---
id: plugins-and-marketplaces
title: プラグインとマーケットプレイス
aliases: [marketplace, /plugin, plugin.json, marketplace.json]
type: feature
field: extend
chapter: プラグイン
order: 210
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, app]
principle: [見せる]
prevents: [散らかっている, 境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: スキル・サブエージェント・フック・MCP などをプラグインに束ねて入れ、配れる。入れたものは使わないときも説明が常駐し、ユーザーの権限でコードを動かすことを踏まえて選ぶ。
signs:
  - {type: situation, text: 別のリポジトリにも同じ設定を作ろうとしている}
  - {type: goal, text: 作った手順や設定を、チームに配りたい}
  - {type: goal, text: チームで同じ設定を使いたい}
prerequisites: [extensions-at-a-glance]
related: [vetting-extensions, share-team-settings, code-intelligence-plugins, mods, pruning-extensions, plugins-in-the-app, writing-skills, connecting-mcp, org-managed-settings-and-mcp, always-on-costs, rolling-out-to-teams]
tracks: [plugins, marketplaces]
sources: []
volatility: 中
sections:
  - {title: 入れる前の確認, anchor: before-install}
  - {title: チームのマーケットプレイスを作る, anchor: team-marketplace}
stage: stub
updated: 2026-11-04
---

## 入れる前の確認 {#before-install}

## チームのマーケットプレイスを作る {#team-marketplace}
