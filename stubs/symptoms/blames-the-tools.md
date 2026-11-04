---
id: blames-the-tools
title: 環境や道具が壊れたと言い出す
aliases: [環境のせいにする, ツールが壊れたと言う, 道具への不満が増える]
type: symptom
field: symptoms
chapter: 長い作業と方針
order: 260
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [確かめる, 見せる]
prevents: [見えていない, 散らかっている, 確かめていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 「環境や道具が壊れた」と言い出したときに、本当に壊れたのか、長い作業の劣化の兆しなのかを自分で確かめて切り分け、続けるか新しく始めるかを決める。
signs:
  - {type: symptom, text: 「環境が壊れている」と言って作業をやめる}
  - {type: symptom, text: ツールが動かないと言うが、自分で実行すると動く}
  - {type: symptom, text: 長く動かすうちに道具への不満が増えていく}
wave: 1
prerequisites: [agent-loop, context-rot]
related: [progress-logs-for-long-jobs, inspect-context, stuck-in-a-check-loop, insists-on-mistakes, claims-done-but-isnt, forgets-in-long-chats, lock-side-effects, six-causes]
routes:
  - {cause: 見えていない, to: [sandboxing, isolate-with-safe-mode]}
  - {cause: 散らかっている, to: [handoff-documents, when-to-start-fresh]}
  - {cause: 確かめていない, to: [evidence-not-reports#tool-output, checking-unattended-runs]}
tracks: [sandbox]
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
