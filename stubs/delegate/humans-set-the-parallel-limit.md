---
id: humans-set-the-parallel-limit
title: 並列の上限は人間が決める
aliases: [並列の本数, レビューの帯域]
type: concept
field: delegate
chapter: 並べる
order: 80
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [握る]
prevents: [確かめていない]
pitfalls: [預けすぎる, 体感を信じる]
scenes: [開発]
summary: 並列の本数を決めるのはマシンや予算ではなく、結果をレビューする人の帯域だと分かる。レビューの要る本流は少なく、調査や使い捨ての試作は多めに並べる。
signs:
  - {type: goal, text: 何本まで並べてよいか決めたい}
  - {type: situation, text: マシンや予算に余裕があるので、並べる本数を増やそうとしている}
prerequisites: []
related: [parallel-fatigue, review-bottlenecks, choosing-parallel-modes, five-questions-before-delegating, pairing-and-delegating, independent-review, diffs-humans-must-read, approval-fatigue, felt-vs-measured, parallel-and-loop-costs, parallel-with-worktrees, agent-view-and-background, compare-hypotheses-in-parallel]
sources: []
volatility: 低
sections:
  - {title: 本流と偵察で本数を分ける, anchor: mainline-vs-scouting}
  - {title: 疲れの兆し, anchor: signs-of-fatigue}
stage: stub
updated: 2026-11-04
---

## 本流と偵察で本数を分ける {#mainline-vs-scouting}

## 疲れの兆し {#signs-of-fatigue}
