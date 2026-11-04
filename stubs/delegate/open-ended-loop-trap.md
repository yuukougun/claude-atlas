---
id: open-ended-loop-trap
title: AI に改善を回させ続ける罠（開いたループ）
nav_title: 開いた改善ループの罠
aliases: [開いた改善ループ, 自律改善ループ, 回し続ければ良くなる]
type: concept
field: delegate
chapter: 任せる前の判断
order: 50
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: [やめられない, 体感を信じる]
scenes: [開発, コンテスト, データ分析]
summary: 戦略そのものを AI に改善させ続ける開いたループが、手元の評価への過適合を自動で進めてしまう理由が分かる。反復させるのは、仕様が決まり停止条件のある実装の作業に限る。
signs:
  - {type: goal, text: AI に改善をずっと回させておきたい}
  - {type: situation, text: 方針や手法の改善まで、AI に自動で回させている}
  - {type: goal, text: AI に回させる反復を、どこまでに限るか決めたい}
prerequisites: [selection-pressure]
related: [verifier-defines-problem, goal-until-done, compare-hypotheses-in-parallel, lockbox-and-holdout, check-the-metric, suspect-too-good-results, reward-hacking, decide-when-to-quit, misses-broken-evaluation, stuck-in-a-check-loop, wont-rethink-approach, what-not-to-delegate, five-questions-before-delegating]
sources: []
volatility: 低
sections:
  - {title: 閉じた反復と開いたループ, anchor: closed-vs-open}
  - {title: 長く回せば良くなるとは限らない, anchor: longer-is-not-better}
stage: stub
updated: 2026-11-04
---

## 閉じた反復と開いたループ {#closed-vs-open}

## 長く回せば良くなるとは限らない {#longer-is-not-better}
