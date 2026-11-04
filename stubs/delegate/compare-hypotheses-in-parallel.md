---
id: compare-hypotheses-in-parallel
title: 仮説ごとに並べて、同じ物差しで比べる
aliases: [設計案を並べて実装する, A と B を作って比べる]
type: recipe
field: delegate
chapter: 並べる
order: 110
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [体感を信じる, やめられない]
scenes: [開発, コンテスト]
summary: 仮説ごとに worktree かブランチを分けて別々に実装させ、同じ評価器で比べて、勝った方だけを取り込める。仮説と物差しと採否は人が決める。
signs:
  - {type: goal, text: 二つの設計案を実際に作らせて比べたい}
  - {type: symptom, text: 案を順に試すと、前の案と同じ条件で比べられなくなる}
prerequisites: [parallel-with-worktrees, experiment-log]
related: [measure-changes, selection-pressure, decide-when-to-quit, open-ended-loop-trap, humans-set-the-parallel-limit, ai-ideas-are-everyones, felt-vs-measured, record-decisions, running-contest-experiments]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
