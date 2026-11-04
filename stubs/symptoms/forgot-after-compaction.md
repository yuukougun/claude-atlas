---
id: forgot-after-compaction
title: 圧縮の後に約束を忘れた
aliases: [compaction の後に忘れる, 自動圧縮で指示が消えた, /compact の後に忘れる]
type: symptom
field: symptoms
chapter: 会話と文脈
order: 150
level: 任せる
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る, 見せる]
prevents: [散らかっている, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 圧縮の後に、会話で決めた約束や禁止を忘れる原因を切り分け、圧縮で残る場所に移すか、仕組みで縛るかを決める。
signs:
  - {type: symptom, text: 圧縮されたら前に決めたことを忘れた}
  - {type: symptom, text: 会話で禁止したことを圧縮の後にやられた}
  - {type: symptom, text: 自動圧縮の後から作業の進め方が変わった}
wave: 1
prerequisites: [what-survives-compaction]
related: [progress-files, what-to-put-in-claude-md, path-scoped-rules#after-compaction, block-with-exit-2, instructions-ignored, replies-in-english, forgets-in-long-chats, six-causes]
routes:
  - {cause: 散らかっている, to: [promises-after-compaction, compact-and-auto-compact, handoff-documents]}
  - {cause: 縛っていない, to: [when-to-lock#spoken-rules-fade, permission-rules, hook-recipes]}
tracks: [compaction, claude-md, permissions, hooks]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
