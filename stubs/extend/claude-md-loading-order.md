---
id: claude-md-loading-order
title: CLAUDE.md の階層と読み込み順
aliases: [CLAUDE.local.md, '@import', claudeMdExcludes, ユーザーの CLAUDE.md, サブフォルダの CLAUDE.md]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 50
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発, チーム]
summary: どの CLAUDE.md がいつ読まれ、どう重なるかを確かめられる。上書きではなく連結され、サブフォルダの分は後から読まれ、取り込みではコンテキストが減らないことが分かる。
signs:
  - {type: symptom, text: 個人の指示とプロジェクトの指示の、どちらが効いているか分からない}
  - {type: situation, text: モノレポで、フォルダごとに違う規約がある}
  - {type: symptom, text: ほかのチームのフォルダの指示まで読み込まれている}
prerequisites: [what-to-put-in-claude-md]
related: [path-scoped-rules, what-survives-compaction, agents-md, settings-layers, using-auto-memory, managed-settings-enforcement, share-team-settings, inspect-context, claude-md-length, forgot-after-compaction]
tracks: [claude-md, rules]
sources: []
volatility: 中
sections:
  - {title: モノレポとほかのチームの指示, anchor: monorepo}
  - {title: 圧縮の後と、クラウドのセッション, anchor: after-compaction}
stage: stub
updated: 2026-11-04
---

## モノレポとほかのチームの指示 {#monorepo}

## 圧縮の後と、クラウドのセッション {#after-compaction}
