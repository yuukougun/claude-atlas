---
id: agent-loop
title: エージェントループと tool use
aliases: [エージェントループ, agentic loop, ツールの呼び出し, 文脈を集める・行動する・確かめる]
type: concept
field: basics
chapter: エージェントと思考
order: 80
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [確かめる]
prevents: [確かめていない]
scenes: [開発, コンテスト]
summary: Claude は道具を使って文脈を集め、行動し、結果を確かめる輪を回し、確かめる手段がないと終わったように見えたところで止まることが分かる。合否を返すテストなどを渡すと、輪を自分で閉じられる。
signs:
  - {type: goal, text: エージェントが裏で何を繰り返して作業を進めているのか知りたい}
  - {type: goal, text: 動くか確かめないまま終わったことにする理由を知りたい}
prerequisites: []
related: [claims-done-but-isnt, define-done, verification-ladder, evidence-not-reports, reward-hacking, tool-use-loop, harness-over-model, subagent-isolation, goal-until-done]
outdated_advice: [keep-going-dont-be-lazy, add-double-check]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
