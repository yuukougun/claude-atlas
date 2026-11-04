---
id: how-skills-load
title: スキルの考え方（手順を必要なときだけ読む）
nav_title: スキルの考え方
aliases: [progressive disclosure, 段階的な開示]
type: concept
field: extend
chapter: スキル
order: 100
level: 任せる
priority: 必須
surfaces: [claude-code, app, api]
principle: [見せる]
prevents: [散らかっている, 見えていない]
pitfalls: []
scenes: [開発, 文章]
summary: スキルが説明文だけを常駐させ、本文と補助ファイルを必要なときにだけ読む仕組みが分かる。長い手順を常駐の指示から外せる理由と、入れすぎたときに残るコストも分かる。
signs:
  - {type: goal, text: 長い手順を、必要なときだけ読ませたい}
  - {type: symptom, text: 手順を書き足すたびに CLAUDE.md が長くなる}
prerequisites: [attention-budget]
related: [writing-skills, skill-descriptions, skill-vs-subagent, hook-vs-skill, claude-md-vs-rules-skills-styles, always-on-costs, what-survives-compaction, skills-in-the-app, pruning-extensions, when-to-add-what, repeating-the-same-explanation, vetting-extensions]
tracks: [skills]
sources: []
volatility: 中
sections:
  - {title: 圧縮の後に戻るもの, anchor: after-compaction}
stage: stub
updated: 2026-11-04
---

## 圧縮の後に戻るもの {#after-compaction}
