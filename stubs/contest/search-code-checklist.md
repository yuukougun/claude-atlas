---
id: search-code-checklist
title: 探索コードと高速化の点検表（AI に書かせたとき）
nav_title: 探索コードと高速化の点検表
aliases: [焼きなましのバグの点検, 差分更新の検証, 高速化の確かめ方]
type: recipe
field: contest
chapter: 評価と実験
order: 70
level: 任せる
priority: 任意
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [コンテスト]
summary: AI に書かせた探索コードと高速化を、差分更新と全再計算の一致・取り消し漏れ・時間の確認・乱数の種などの観点で点検し、速さを実測で確かめる手順が分かる。
signs:
  - {type: symptom, text: AI に書かせた焼きなましのスコアが、ときどきおかしい}
  - {type: goal, text: AI に高速化させた探索コードが、壊れていないか確かめたい}
prerequisites: [evaluators-by-format]
related: [performance-tuning, differential-testing, suspect-too-good-results, show-examples, running-contest-experiments, pitfalls-of-ai-written-tests, fix-a-bug, shrink-failing-inputs]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 探索コードの点検の観点, anchor: search-code}
  - {title: 高速化は計測が先, anchor: measure-first}
  - {title: 人の知見を点検表として渡す, anchor: checklist-as-context}
stage: stub
updated: 2026-11-04
---

## 探索コードの点検の観点 {#search-code}

## 高速化は計測が先 {#measure-first}

## 人の知見を点検表として渡す {#checklist-as-context}
