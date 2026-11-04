---
id: suspect-too-good-results
title: 良すぎる結果を疑う
aliases: [うますぎる結果, リークを疑う, 偽の高速化, 結果の偽装]
type: concept
field: verify
chapter: 結果を疑う
order: 170
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: 急な高速化や満点に近いスコアのような良すぎる結果を、リーク・退化・採点の省略を疑って確かめてから受け取れる。報告の前に Claude に自己点検させる。
signs:
  - {type: symptom, text: 桁違いに速くなったと報告されたが、本当か怪しい}
  - {type: symptom, text: 精度がほぼ満点になって、かえって怪しい}
  - {type: goal, text: うますぎる結果を、受け取る前に確かめたい}
prerequisites: [evidence-not-reports]
related: [lockbox-and-holdout, check-the-metric, verifier-three-conditions, selection-pressure, differential-testing, protect-tests, performance-tuning, data-analysis, audit-ml-pipelines, misses-broken-evaluation, looks-are-not-quality]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: まず疑うもの, anchor: what-to-suspect}
  - {title: 報告の前に自己点検させる, anchor: self-check}
stage: stub
updated: 2026-11-04
---

## まず疑うもの {#what-to-suspect}

## 報告の前に自己点検させる {#self-check}
