---
id: promises-after-compaction
title: 圧縮で消えない場所に約束を置く
aliases: [圧縮のあとに残る約束、消える約束, 圧縮の後も守らせたい, 会話で言ったことが圧縮で消える]
type: concept
field: context
chapter: 圧縮
order: 60
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [縛る, 見せる]
prevents: [散らかっている, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 圧縮のあとも守らせたい決めごとを、圧縮の後に読み直される CLAUDE.md や計画のファイルに書き、例外を許さないものはdeny ルールやフックに移す。会話の中だけで伝えた約束は要約に溶けうる。
signs:
  - {type: goal, text: 圧縮のあとも守らせたい約束を、どこに書けばよいか知りたい}
  - {type: goal, text: 長いセッションで、最初に決めた約束を最後まで守らせたい}
prerequisites: [what-survives-compaction]
related: [compact-and-auto-compact, when-to-lock#spoken-rules-fade, permission-rules, path-scoped-rules, what-to-put-in-claude-md, how-skills-load, handoff-documents, forgot-after-compaction, request-vs-lock]
tracks: [compaction, claude-md, rules]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 読み直される場所と、要約に溶ける約束, anchor: what-comes-back}
  - {title: 約束の種類ごとの置き場所, anchor: where-to-put}
  - {title: paths 付きの rules とスキルの本文の注意, anchor: caveats}
stage: stub
updated: 2026-11-04
---

## 読み直される場所と、要約に溶ける約束 {#what-comes-back}

## 約束の種類ごとの置き場所 {#where-to-put}

## paths 付きの rules とスキルの本文の注意 {#caveats}
