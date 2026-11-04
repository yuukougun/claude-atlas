---
id: path-scoped-rules
title: .claude/rules と paths で必要なときだけ読ませる
nav_title: .claude/rules と paths
aliases: [rules, パス別のルール, paths のフロントマター, ディレクトリごとの規約]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 60
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発]
summary: 特定のフォルダやファイル向けの規約を、そのファイルに触れたときだけ読み込ませられる。常駐を減らせるが、圧縮の後は引き金のファイルを読むまで戻らない。
signs:
  - {type: goal, text: 特定のディレクトリだけのルールを書きたい}
  - {type: symptom, text: 一部のフォルダ用の規約が、関係のない作業にも毎回読み込まれている}
  - {type: symptom, text: 圧縮の後、フォルダごとの規約が効かなくなった}
  - {type: situation, text: CLAUDE.md が長くなってきた}
prerequisites: [what-to-put-in-claude-md]
related: [claude-md-loading-order, claude-md-length, what-survives-compaction, promises-after-compaction, claude-md-vs-rules-skills-styles, how-skills-load, when-to-lock, always-on-costs, forgot-after-compaction]
tracks: [rules]
sources: []
volatility: 中
sections:
  - {title: 圧縮の後に戻る時期, anchor: after-compaction}
stage: stub
updated: 2026-11-04
---

## 圧縮の後に戻る時期 {#after-compaction}
