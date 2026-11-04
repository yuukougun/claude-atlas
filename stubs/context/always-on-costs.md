---
id: always-on-costs
title: 常駐するもののコスト（CLAUDE.md・MCP・スキル）
aliases: [常駐するもののコスト（CLAUDE.md・MCP・skills）, listing tax, 常駐するコンテキスト, 起動時に読み込まれるもの, MCP を入れすぎると重い]
type: concept
field: context
chapter: 見る・絞る
order: 110
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: CLAUDE.md の全文・スキルの説明・MCP のツールの一覧など、毎回のリクエストに乗るものの費用が分かり、必要なときだけ読ませる形に移せる。溢れの心配より、焦点と費用のために常駐を小さく保つ。
signs:
  - {type: goal, text: MCP や skill をどこまで入れてよいか知りたい}
prerequisites: [rereads-whole-history]
related: [inspect-context, pruning-extensions, too-slow, extensions-at-a-glance, claude-md-length, path-scoped-rules, how-skills-load, connecting-mcp, mcp-or-cli, vetting-extensions, why-prompt-caching, what-uses-up-limits, choose-what-to-read]
tracks: [claude-md, skills, mcp, context-window]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 常駐するものと、使うときだけ読むもの, anchor: resident-vs-on-demand}
  - {title: 減らす順, anchor: reduce}
stage: stub
updated: 2026-11-04
---

## 常駐するものと、使うときだけ読むもの {#resident-vs-on-demand}

## 減らす順 {#reduce}
