---
id: instructions-ignored
title: CLAUDE.md や指示が守られない
aliases: [指示を無視される]
type: symptom
field: symptoms
chapter: 指示と仕組み
order: 10
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [散らかっている, 縛っていない]
pitfalls: []
summary: 規則が破られる原因を切り分ける。二つ目の文。
signs:
  - {type: symptom, text: CLAUDE.md に書いたのに守られない}
  - {type: symptom, text: スキルに書いた手順を飛ばされる}
wave: 1
prerequisites: [request-vs-lock]
routes:
  - {cause: 縛っていない, to: [hooks-basics#exit-codes, writing-safe-hooks]}
  - {cause: 散らかっている, to: [what-to-put-in-claude-md]}
related: [six-causes]
tracks: [sample-hooks]
outdated_advice: [sample-caps, sample-renamed]
sources: [sample-doc, sample-blog]
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: draft
updated: 2026-11-04
---

!!! abstract "要点"
    - **何ができるか**：試験用の文。
    - **前提**：<!-- link:begin request-vs-lock --><!-- link:end -->

## 原因を安く確かめる順 {#diagnosis}

1. **散らかっている**：試験用の確かめ方
2. **縛っていない**：試験用の確かめ方

<!-- gen:begin routes -->
<!-- gen:end routes -->
