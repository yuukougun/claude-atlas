---
id: misses-broken-evaluation
title: 手元の評価は良いのに本番で通用しない
aliases: [評価のおかしさに自分からは気づかない, 評価の誤りを放置する, リークに気づかない, スコアだけ上がる]
type: symptom
field: symptoms
chapter: 完了と検証
order: 230
level: 任せる
priority: 必須
surfaces: [claude-code, api]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [データ分析, 開発, コンテスト]
summary: 手元の評価は良いのに本番で通用しないときに、評価の仕組みが正しいか・書き換えられないか・本番を代表するかを切り分ける。Claude は評価の誤りを自分からは直さないので、評価そのものを人が確かめる。
signs:
  - {type: symptom, text: 評価のやり方の誤りを指摘してくれない}
  - {type: symptom, text: 手元のスコアは上がるのに本番で通用しない}
  - {type: symptom, text: おかしな評価のまま実験を続けている}
wave: 1
prerequisites: [verifier-defines-problem]
related: [selection-pressure, open-ended-loop-trap, lockbox-and-holdout, suspect-too-good-results, measure-changes#by-stratum, reward-hacking, over-reliance, audit-ml-pipelines, data-analysis, evaluators-by-format, rewrote-tests-to-pass, claims-done-but-isnt, stuck-in-a-check-loop, six-causes]
routes:
  - {cause: 確かめていない, to: [verifier-three-conditions, test-the-verifier, check-the-metric]}
  - {cause: 預けすぎる, to: [what-not-to-delegate#what-humans-hold]}
tracks: []
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
