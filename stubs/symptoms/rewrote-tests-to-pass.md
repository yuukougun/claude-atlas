---
id: rewrote-tests-to-pass
title: テストを書き換えて通した
aliases: [テストの改ざん, ハードコードで通す, 特例の分岐で通す]
type: symptom
field: symptoms
chapter: 完了と検証
order: 220
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: テストの書き換えや特例の分岐で通されたときに、何が書き換えられる状態だったかを切り分け、テストの保護と一般解の求め方を決める。
signs:
  - {type: symptom, text: テストのほうを書き換えて通された}
  - {type: symptom, text: 特定の入力だけ通るように分岐を足された}
  - {type: symptom, text: 例外を握りつぶしたり型を緩めたりしてエラーを消された}
wave: 1
prerequisites: [reward-hacking]
related: [verifier-three-conditions#tamper-proof, when-to-lock, hook-recipes, pitfalls-of-ai-written-tests, independent-review, test-the-verifier, suspect-too-good-results, verification-ladder, claims-done-but-isnt, misses-broken-evaluation, six-causes]
routes:
  - {cause: 確かめていない, to: [protect-tests, diffs-humans-must-read#red-flags, fix-a-bug#no-symptom-patches]}
  - {cause: 縛っていない, to: [freeze-eval-assets, permission-rules, block-with-exit-2]}
tracks: [permissions, hooks]
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
