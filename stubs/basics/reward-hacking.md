---
id: reward-hacking
title: 採点器を騙す（reward hacking）
aliases: [reward hacking, 報酬ハッキング, specification gaming, 採点の抜け道]
type: concept
field: basics
chapter: 答えの確かさ
order: 160
level: 任せる
priority: 必須
surfaces: [claude-code, api]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
scenes: [開発, コンテスト]
summary: 採点の仕組みに抜け道があると、目的ではなく採点を満たす方向に解かれることがあると分かる。テストの書き換えや特別扱いを防ぐには、書き換えられない独立した検証が要る理由になる。
signs:
  - {type: goal, text: 採点やテストの抜け道を突かれる理由を知りたい}
  - {type: goal, text: 検証を書き換えられない形にすべき理由を知りたい}
prerequisites: [agent-loop]
related: [rewrote-tests-to-pass, protect-tests, verifier-three-conditions, verifier-defines-problem, freeze-eval-assets, misses-broken-evaluation, suspect-too-good-results, pitfalls-of-ai-written-tests]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
