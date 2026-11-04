---
id: move-judgment-into-scripts
title: 判断を決定論的なスクリプトに移す
aliases: [LLM にスクリプトを書かせる, 決定論的な道具に置き換える]
type: concept
field: enforce
chapter: 何を縛るか
order: 30
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, api]
principle: [縛る, 確かめる]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: 毎回 Claude に判断させている作業を、Claude に書かせたスクリプトに移せる。結果が毎回同じになり、確かめやすくなる。
signs:
  - {type: goal, text: 同じ集計や変換を、毎回 Claude にやらせている}
  - {type: symptom, text: 同じ集計なのに、頼むたびに数字が少しずつ違う}
prerequisites: [request-vs-lock, nondeterminism]
related: [when-to-lock, request-lock-table, mcp-or-cli, shrink-failing-inputs, bisect-regressions, build-observation-tools, hook-recipes, writing-skills, designing-agent-tools]
tracks: [skills, hooks]
sources: []
volatility: 低
sections:
  - {title: 移す作業の見分け方, anchor: what-to-move}
  - {title: 書かせたスクリプトを確かめる, anchor: check-the-script}
stage: stub
updated: 2026-11-04
---

## 移す作業の見分け方 {#what-to-move}

## 書かせたスクリプトを確かめる {#check-the-script}
