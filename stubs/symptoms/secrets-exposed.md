---
id: secrets-exposed
title: 秘密の情報を読まれた・外に出された
nav_title: 秘密を読まれた・出された
aliases: [.env を読まれた, API キーの流出, 秘密をコミットされた]
type: symptom
field: symptoms
chapter: 安全と承認
order: 290
level: 使う
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 握る]
prevents: [縛っていない, 境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: 秘密（.env・API キー）を読まれた・会話や履歴に出たときに、まず鍵を無効にし、どの境界が欠けていたかを切り分けて、読ませない縛りを決める。
signs:
  - {type: symptom, text: .env の中身を読まれて会話に出された}
  - {type: symptom, text: API キーを含むファイルをコミットされた}
  - {type: symptom, text: 秘密の値がログや出力に残っている}
  - {type: symptom, text: 会話に API キーを貼ってしまった}
wave: 1
prerequisites: [where-your-data-goes]
related: [what-feedback-sends, shared-artifacts-and-files, block-with-exit-2, hook-recipes, what-auto-mode-stops, vetting-extensions, before-opening-unknown-repos, postmortems, followed-injected-instructions, deleted-something-important, six-causes]
routes:
  - {cause: 縛っていない, to: [protecting-secrets, permission-rules]}
  - {cause: 境界がない, to: [sandboxing, lethal-trifecta]}
tracks: [permissions, sandbox, hooks]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: まず鍵を無効にする, anchor: first-response}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## まず鍵を無効にする {#first-response}

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
