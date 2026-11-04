---
id: shrink-failing-inputs
title: 失敗する入力を縮めるスクリプトを書かせる
nav_title: 失敗する入力を縮める
aliases: [入力の縮小, 最小の再現例, デルタデバッギング, ddmin, minimal reproducible example]
type: recipe
field: recipes
chapter: 直す
order: 40
level: 任せる
priority: 任意
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [見えていない, 散らかっている]
scenes: [開発, コンテスト]
summary: 大きな失敗入力は、直させる前に最小の再現例へ縮める。縮める処理は何度でも同じ結果を出せるスクリプトとして書かせ、縮めた入力を修正の依頼に渡す。
signs:
  - {type: symptom, text: 大きな入力でしか起きないバグで、どこが悪いのか分からない}
  - {type: goal, text: バグを再現する一番小さな入力を作りたい}
prerequisites: [fix-a-bug, differential-testing]
related: [property-based-tests, bisect-regressions, build-test-harness, move-judgment-into-scripts, research-in-subagents, going-in-circles]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
