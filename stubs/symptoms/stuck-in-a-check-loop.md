---
id: stuck-in-a-check-loop
title: 同じ確認のループにはまる
aliases: [無限検証ループ, 実行と確認の繰り返し, ベンチを回すだけになる]
type: symptom
field: symptoms
chapter: 長い作業と方針
order: 240
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる, 握る]
prevents: [見えていない, 散らかっている, 合っていない]
pitfalls: [預けすぎる]
scenes: [開発, コンテスト]
summary: 実行と確認を繰り返すだけで進まないループを見分け、新しい仮説や情報を入れるか、止める条件を決めるか、新しい会話に移すかを選ぶ。
signs:
  - {type: symptom, text: ベンチを回してスコアを見るだけの繰り返しになる}
  - {type: symptom, text: 同じ修正と確認を利用上限まで繰り返す}
  - {type: symptom, text: 何時間も回したのに途中から進んでいない}
wave: 1
prerequisites: [agent-loop]
related: [performance-tuning, permission-to-stop, parallel-and-loop-costs, going-in-circles, wont-rethink-approach, blames-the-tools, misses-broken-evaluation, hits-limits-quickly, six-causes]
routes:
  - {cause: 見えていない, to: [share-targets-and-bounds, keep-failure-lessons, experiment-log]}
  - {cause: 散らかっている, to: [when-to-start-fresh, handoff-documents]}
  - {cause: 合っていない, to: [goal-until-done#writing-conditions, stop-hooks#avoid-loops, open-ended-loop-trap]}
  - {cause: 預けすぎる, to: [decide-when-to-quit, progress-logs-for-long-jobs, checking-unattended-runs]}
tracks: [goal, loop]
outdated_advice: [ralph-loops]
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
