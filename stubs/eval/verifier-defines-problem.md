---
id: verifier-defines-problem
title: 検証器が問題を定義する（Claude は置かれたループを何でも加速する）
nav_title: 検証器が問題を定義する
aliases: [評価器が問題を定義する, 評価を握る, 最初の成果物は検証器]
type: concept
field: eval
chapter: 総論
order: 10
level: 任せる
priority: 必須
surfaces: [claude-code, api]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, データ分析, コンテスト]
summary: Claude は渡された検証器（テスト・採点・ベンチマーク）が定める問題を解き、置かれたループを何でも速めることが分かる。検証器が誤れば、誤りも同じ速さで増える。
signs:
  - {type: goal, text: Claude に長く改善を回させても、方向を誤らせたくない}
  - {type: symptom, text: テストに書いた条件だけが満たされ、書かなかった意図は抜けていた}
  - {type: situation, text: スコアやテストを目標に、Claude に試行を繰り返させている}
wave: 1
prerequisites: [verification-ladder]
related: [verifier-three-conditions, selection-pressure, measure-changes, reward-hacking, four-principles, protect-tests, what-not-to-delegate, misses-broken-evaluation, build-test-harness, evaluators-by-format, open-ended-loop-trap, goal-until-done]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: ループは何でも速める, anchor: loops-amplify}
  - {title: 最初の成果物は検証器, anchor: verifier-first}
  - {title: 評価と実験の地図, anchor: map}
stage: stub
updated: 2026-11-04
---

## ループは何でも速める {#loops-amplify}

## 最初の成果物は検証器 {#verifier-first}

## 評価と実験の地図 {#map}
