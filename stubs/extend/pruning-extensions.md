---
id: pruning-extensions
title: 拡張の棚卸しと剪定
aliases: [/skill-doctor, 拡張が多すぎる, skillOverrides, 使っていないスキル]
type: recipe
field: extend
chapter: 見直し
order: 240
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている, 合っていない]
pitfalls: [体感を信じる]
scenes: [開発, チーム]
summary: 入れた CLAUDE.md・スキル・MCP・プラグインを定期的に見直し、使っていないものを外せる。常駐のコストを測ってから切り、共有するものは複数の人が使うものに絞る。
signs:
  - {type: symptom, text: 使っていないはずの設定が、毎回トークンを使っている}
  - {type: situation, text: 設定を作り込んで、しばらくたった}
prerequisites: [extensions-at-a-glance, always-on-costs]
related: [inspect-context, claude-md-length, skill-descriptions, plugins-and-marketplaces, vetting-extensions, insights-and-usage-review, felt-vs-measured, what-uses-up-limits#find-what-uses-it, hits-limits-quickly, share-team-settings, when-to-add-what]
tracks: [claude-md, skills, mcp, plugins]
sources: []
volatility: 中
sections:
  - {title: 測る, anchor: measure}
  - {title: 切る基準, anchor: criteria}
stage: stub
updated: 2026-11-04
---

## 測る {#measure}

## 切る基準 {#criteria}
