---
id: parallel-fatigue
title: 並列にしたら疲れた・レビューが追いつかない
nav_title: 並列にしたら疲れた
aliases: [並列疲れ, レビュー待ちがたまる, 並列にしても速くならない]
type: symptom
field: symptoms
chapter: 長い作業と方針
order: 270
level: 回す
priority: 必須
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない, 合っていない]
pitfalls: [預けすぎる, 体感を信じる]
scenes: [開発, チーム]
summary: 並列で任せたら疲れた・レビューが追いつかないときに、並べる数・確かめ方・体感のずれのどれが原因かを切り分け、並列の上限と人が読む範囲を決め直す。
signs:
  - {type: symptom, text: 並列にしたら疲れた}
  - {type: symptom, text: レビュー待ちの変更がたまっていく}
  - {type: symptom, text: 並べた分だけ速くなった気がしない}
wave: 1
prerequisites: []
related: [independent-review, over-reliance, parallel-with-worktrees, completion-notifications, parallel-and-loop-costs, wrong-amount-of-approvals, hits-limits-quickly, six-causes]
routes:
  - {cause: 確かめていない, to: [diffs-humans-must-read, review-bottlenecks, risk-tiered-approval]}
  - {cause: 合っていない, to: [choosing-parallel-modes, agent-view-and-background#what-fits]}
  - {cause: 預けすぎる, to: [humans-set-the-parallel-limit]}
  - {cause: 体感を信じる, to: [felt-vs-measured]}
tracks: [worktrees, agent-view]
outdated_advice: [tmux-agent-orgs]
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
