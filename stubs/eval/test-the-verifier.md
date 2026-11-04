---
id: test-the-verifier
title: 検証器そのものを確かめる（red/green・手で計算したケース）
nav_title: 検証器そのものを確かめる
aliases: [検証器のテスト, 採点スクリプトの検証, 評価器の red/green]
type: recipe
field: eval
chapter: 検証器を作る
order: 60
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 検証器を使う前に、何もしない解が負け、強い解が勝ち、手で計算した値と一致し、わざと壊した検証器では落ちることを確かめてから凍結できる。
signs:
  - {type: symptom, text: 採点のスクリプト自体にバグがあった}
  - {type: symptom, text: どの方法を試しても点が出ず、何かがおかしい}
  - {type: goal, text: 評価の仕組みが正しく採点しているか確かめてから使いたい}
wave: 1
prerequisites: [verifier-three-conditions]
related: [differential-testing, model-based-grading, freeze-eval-assets, misses-broken-evaluation, build-test-harness, evaluators-by-format, tests-first, pitfalls-of-ai-written-tests]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: red/green を検証器に当てる, anchor: red-green}
  - {title: 手で計算したケース, anchor: hand-calculated}
  - {title: わざと壊した検証器で落ちるか, anchor: broken-copy}
  - {title: 入力の生成器の分布を人が見る, anchor: input-distribution}
  - {title: 採点の正本は一か所に, anchor: single-scorer}
  - {title: 確かめてから凍結する, anchor: freeze}
stage: stub
updated: 2026-11-04
---

## red/green を検証器に当てる {#red-green}

## 手で計算したケース {#hand-calculated}

## わざと壊した検証器で落ちるか {#broken-copy}

## 入力の生成器の分布を人が見る {#input-distribution}

## 採点の正本は一か所に {#single-scorer}

## 確かめてから凍結する {#freeze}
