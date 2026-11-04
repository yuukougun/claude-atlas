---
id: lockbox-and-holdout
title: ロックボックスと hold-out（人だけが持つ検証用データ）
nav_title: ロックボックスと hold-out
aliases: [ホールドアウト, 隠しテスト, 見せない検証データ, lockbox]
type: concept
field: eval
chapter: 実験を回す
order: 120
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 握る]
prevents: [縛っていない, 確かめていない]
pitfalls: []
scenes: [データ分析, コンテスト, 開発]
summary: 入力を開発用・検証用・人だけが持つロックボックスに分け、節目にだけ見る運用ができる。エージェントには点数だけを返し、中身を見せない。
signs:
  - {type: goal, text: Claude に見せない検証用のデータを持ちたい}
  - {type: symptom, text: 見えているテストは通るのに、隠れたテストで大きく落ちる}
prerequisites: [verifier-three-conditions, selection-pressure]
related: [protect-tests, freeze-eval-assets, sandboxing, permission-rules, suspect-too-good-results, experiment-log, check-the-metric, misses-broken-evaluation, data-analysis, evaluators-by-format]
tracks: [permissions, sandbox]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 三層に分ける, anchor: three-tiers}
  - {title: 点数だけを返す, anchor: scores-only}
  - {title: 読めない所に置く, anchor: keep-out-of-reach}
stage: stub
updated: 2026-11-04
---

## 三層に分ける {#three-tiers}

## 点数だけを返す {#scores-only}

## 読めない所に置く {#keep-out-of-reach}
