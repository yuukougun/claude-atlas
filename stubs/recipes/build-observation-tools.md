---
id: build-observation-tools
title: 観察の道具を作らせる（可視化・集計・ログ）
nav_title: 観察の道具を作らせる
aliases: [ビジュアライザを作らせる, ダッシュボードを作らせる, 集計スクリプト, デバッグ用の表示]
type: recipe
field: recipes
chapter: 確かめる道具を作らせる
order: 130
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [握る, 見せる]
prevents: [見えていない]
pitfalls: [預けすぎる]
scenes: [開発, データ分析, コンテスト]
summary: 結論を出させる代わりに、可視化・集計・ログなど観察のための道具を作らせ、浮いた時間を自分の観察に回す。道具の出す値は、小さな例で手計算と合うかを先に確かめる。
signs:
  - {type: goal, text: 結果やログを見やすくする道具を手早く作りたい}
  - {type: goal, text: 原因を AI に推測させるより、自分で見て考えたい}
prerequisites: [think-before-asking]
related: [data-analysis, fix-a-bug, performance-tuning, build-test-harness, artifacts-as-apps, test-the-verifier, over-reliance, how-much-understanding-to-keep]
tracks: [artifacts]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
