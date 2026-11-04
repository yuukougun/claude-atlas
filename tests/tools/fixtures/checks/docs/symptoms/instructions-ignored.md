---
id: instructions-ignored
title: CLAUDE.md や指示が守られない
type: symptom
field: symptoms
chapter: 指示と仕組み
order: 10
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
summary: 試験用の要約。
signs:
  - {type: symptom, text: 試験用の困りごと1}
  - {type: symptom, text: 試験用の困りごと2}
wave: 1
prerequisites: [request-vs-lock]
routes:
  - {cause: 縛っていない, to: [hooks-basics#exit-codes]}
outdated_advice: [sample-caps]
sources: [sample-doc, sample-note]
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: draft
updated: 2026-11-04
---

!!! abstract "要点"
    - **何ができるか**：試験用の項目。
    - **いつ引くか**：試験用の項目。
    - **前提**：<!-- link:begin request-vs-lock --><!-- link:end -->

CLAUDE.md や指示が守られないのは、試験用の導入である。

## 原因を安く確かめる順 {#diagnosis}

まず[お願いと鍵](../basics/request-vs-lock.md#two-layers)を読む。

<!-- gen:begin routes -->
- 縛っていない：<!-- link:begin hooks-basics#exit-codes -->フック（準備中）<!-- link:end -->
<!-- gen:end routes -->

<!-- gen:begin references -->
- 試験用の出典
<!-- gen:end references -->
