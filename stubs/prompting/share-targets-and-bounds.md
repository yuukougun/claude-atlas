---
id: share-targets-and-bounds
title: 目標値・上界を伝える
aliases: [目標スコアを書く, 理論上の上界を伝える, 達成できる値を伝える]
type: concept
field: prompting
chapter: 何をどこまで頼むか
order: 100
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [見せる, 確かめる]
prevents: [見えていない]
scenes: [開発, データ分析, コンテスト]
summary: 達成できる値や理論上の上界が分かっていれば依頼に書くと、早く打ち切ったり「限界です」と言ったりしにくくなる。分からないときは、先に上界を測る。
signs:
  - {type: goal, text: 最適化を、目標の値に届くまで粘らせたい}
  - {type: symptom, text: 最適化を頼むと、早々に打ち切る}
  - {type: situation, text: 性能改善やスコアを競う課題を任せている}
prerequisites: [ask-for-outcomes]
related: [measure-the-upper-bound, performance-tuning, wont-rethink-approach, blames-the-tools, measure-changes, format-cheatsheet]
sources: []
volatility: 低
sections:
  - {title: 目標値を書く, anchor: targets}
  - {title: 上界が分からないときは測る, anchor: measure}
stage: stub
updated: 2026-11-04
---

## 目標値を書く {#targets}

## 上界が分からないときは測る {#measure}
