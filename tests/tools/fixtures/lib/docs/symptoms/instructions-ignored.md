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
related: [how-to-use]
tracks: [sample-hooks]
outdated_advice: [sample-caps, sample-renamed]
sources: [sample-doc, sample-note]
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: draft
updated: 2026-11-04
---

# CLAUDE.md や指示が守られない

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
- 縛っていない：<!-- link:begin hooks-basics#exit-codes -->フック（準備中）<!-- link:end -->
<!-- gen:end routes -->

上限は <!-- fact:begin sample-limit -->100 回<!-- fact:end --> で、既定は <!-- fact:begin sample-default-effort -->試験用の表<!-- fact:end --> にある。

目印の書き方は `<!-- fact:begin <id> -->` の形（行の中のコードの目印は読まない）。

```text
<!-- gen:begin not-a-marker -->
```

## 参考 {#references}

<!-- gen:begin references -->
- 試験用の出典
<!-- gen:end references -->
