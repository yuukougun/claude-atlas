---
id: check-the-metric
title: 評価指標そのものを確かめる
aliases: [指標のずれ, 評価指標の選び方, 手元の指標と本番の指標]
type: concept
field: eval
chapter: 検証器を作る
order: 70
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [データ分析, コンテスト, 開発]
summary: 検証器が測る指標と本当の目的のずれを、最適化を始める前に確かめられる。指標が良いことは、正しいことを意味しない。
signs:
  - {type: symptom, text: 上げさせた指標が、本当に上げたかったものとずれていた}
  - {type: goal, text: 最適化させる指標が、本当に欲しいものと合っているか確かめたい}
prerequisites: [verifier-defines-problem]
related: [verifier-three-conditions, define-done, suspect-too-good-results, measure-changes, lockbox-and-holdout, data-analysis, read-specs-yourself, misses-broken-evaluation]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 指標と目的のずれ, anchor: mismatch}
stage: stub
updated: 2026-11-04
---

## 指標と目的のずれ {#mismatch}
