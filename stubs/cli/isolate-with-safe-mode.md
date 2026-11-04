---
id: isolate-with-safe-mode
title: 設定を外して切り分ける（--safe-mode）
aliases: [--safe-mode, 拡張なしで起動する, 自分の設定のせいか確かめる, Debug your configuration]
type: feature
field: cli
chapter: 見る・切り分ける
order: 110
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: CLAUDE.md・スキル・プラグイン・フック・MCP などを読まずに起動し、同じ依頼で挙動を比べて、不調が自分の設定から来るかを切り分ける。権限と管理の設定は効いたままで、安全の設定を外す道具ではない。
signs:
  - {type: goal, text: おかしな挙動が、自分の設定や拡張のせいか確かめたい}
  - {type: situation, text: 拡張を入れてから急に挙動が変わった}
prerequisites: [settings-layers]
related: [seems-less-capable, instructions-ignored, replies-in-english, blames-the-tools, suspected-degradation, pruning-extensions, felt-vs-measured, usage-context-statusline]
tracks: [safe-mode]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 外れるもの・残るもの, anchor: what-is-disabled}
  - {title: 比べ方, anchor: compare}
stage: stub
updated: 2026-11-04
---

## 外れるもの・残るもの {#what-is-disabled}

## 比べ方 {#compare}
