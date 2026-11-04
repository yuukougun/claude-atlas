---
id: selection-pressure
title: 選択圧：良かった版を選び続ける罠
aliases: [勝者の呪い, 評価への過適合, 選んだ版の上振れ]
type: concept
field: eval
chapter: 実験を回す
order: 100
level: 仕組みにする
priority: 必須
surfaces: [claude-code, api]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: Claude が正直でも、良かった版を選び続けるだけで評価の穴に合わせ込んでしまう罠が分かる。試行を増やすほど強まり、一変更一評価・台帳・見せないデータで防ぐ。
signs:
  - {type: symptom, text: いちばん点の良かった版を選んだのに、新しい入力では平凡だった}
  - {type: situation, text: 何十通りも試させて、いちばん良かった版を採っている}
prerequisites: [verifier-defines-problem, measure-changes]
related: [experiment-log, lockbox-and-holdout, open-ended-loop-trap, compare-hypotheses-in-parallel, goal-until-done, dynamic-workflows, decide-when-to-quit, suspect-too-good-results, running-contest-experiments]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: なぜ正直でも外れるか, anchor: why}
  - {title: 防ぎ方, anchor: defenses}
  - {title: 同じアイデアの再挑戦に上限を置く, anchor: retry-cap}
stage: stub
updated: 2026-11-04
---

## なぜ正直でも外れるか {#why}

## 防ぎ方 {#defenses}

## 同じアイデアの再挑戦に上限を置く {#retry-cap}
