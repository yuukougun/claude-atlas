---
id: parallel-and-loop-costs
title: 並列・ループ・workflows のコスト
aliases: [並列の費用, 自動ループの費用, サブエージェントの費用, agent teams の費用, ultracode の費用]
type: concept
field: cost
chapter: 任せて回すとき
order: 100
level: 仕組みにする
priority: 必須
surfaces: [claude-code, api]
principle: [握る, 縛る]
prevents: [合っていない]
pitfalls: [やめられない]
summary: 並列・ループ・workflows の費用が、本数と回数と1回の文脈の大きさの掛け算で膨らむ理由が分かる。始める前に、同時に動かす数と止める条件と費用の上限を決める。
signs:
  - {type: goal, text: 並列やループで回す前に、費用の見当をつけたい}
  - {type: symptom, text: 夜通しループを回したら、上限や請求が一気に増えた}
  - {type: situation, text: agent teams や workflows を試したいが、どれだけ使うか分からない}
prerequisites: [what-uses-up-limits]
related: [humans-set-the-parallel-limit, choosing-parallel-modes, goal-until-done, loop-and-scheduling, dynamic-workflows, agent-teams, research-in-subagents, checking-unattended-runs, decide-when-to-quit, open-ended-loop-trap, usage-credits-basics]
tracks: [workflows, agent-teams, loop, goal, subagents]
outdated_advice: [ralph-loops, workflow-keyword-extra-usage, subagents-to-save-context]
sources: []
volatility: 高
sections:
  - {title: 費用が膨らむ掛け算, anchor: multiplication}
  - {title: 始める前に決める三つ, anchor: decide-before-starting}
  - {title: 実例の読み方（自己申告と時点）, anchor: reading-examples}
stage: stub
updated: 2026-11-04
---

## 費用が膨らむ掛け算 {#multiplication}

## 始める前に決める三つ {#decide-before-starting}

## 実例の読み方（自己申告と時点） {#reading-examples}
