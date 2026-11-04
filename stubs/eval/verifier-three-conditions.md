---
id: verifier-three-conditions
title: 検証器の三条件（正しい・書き換えられない・本番を代表する）
nav_title: 検証器の三条件
aliases: [評価器の要件, 検証器の質, 本番を代表するテスト]
type: concept
field: eval
chapter: 検証器を作る
order: 50
level: 任せる
priority: 必須
surfaces: [claude-code, api]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: 検証器が満たすべき三つの条件（正しい・書き換えられない・本番を代表する）で、評価の仕組みを使う前に点検できる。手元の勝ちが本番の勝ちを意味するかを問う。
signs:
  - {type: goal, text: Claude に回させる前に、評価の仕組みが信用できるか確かめたい}
  - {type: symptom, text: 手元で試した入力と、本番の入力の傾向が違っていた}
wave: 1
prerequisites: [verifier-defines-problem, reward-hacking]
related: [test-the-verifier, protect-tests, lockbox-and-holdout, check-the-metric, differential-testing, model-based-grading, freeze-eval-assets, misses-broken-evaluation, rewrote-tests-to-pass, build-test-harness, evaluators-by-format]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 正しい, anchor: correct}
  - {title: 書き換えられない, anchor: tamper-proof}
  - {title: 本番を代表する, anchor: representative}
stage: stub
updated: 2026-11-04
---

## 正しい {#correct}

## 書き換えられない {#tamper-proof}

## 本番を代表する {#representative}
