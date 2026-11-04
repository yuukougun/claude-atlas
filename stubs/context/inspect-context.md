---
id: inspect-context
title: /context で中身を見る
aliases: [/context, コンテキストの内訳, 何がコンテキストを占めているか, 起動直後の基準値]
type: feature
field: context
chapter: 見る・絞る
order: 100
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発]
summary: /context の内訳から、会話・読み込んだファイル・常駐するもののどれが場所を取っているかを見分け、片付け方を選ぶ。起動直後の値を控えておくと、増えた分が分かる。
signs:
  - {type: goal, text: 何がコンテキストを占めているか知りたい}
  - {type: goal, text: 拡張を足した後、起動直後にどれだけ場所を取っているか確かめたい}
prerequisites: [attention-budget]
related: [usage-context-statusline, always-on-costs, choose-what-to-read, compact-and-auto-compact, research-in-subagents, pruning-extensions, felt-vs-measured, what-uses-up-limits#find-what-uses-it]
tracks: [context-window]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 内訳の読み方, anchor: reading}
  - {title: 起動直後の基準値, anchor: baseline}
  - {title: どの片付け方を選ぶか, anchor: what-to-do}
stage: stub
updated: 2026-11-04
---

## 内訳の読み方 {#reading}

## 起動直後の基準値 {#baseline}

## どの片付け方を選ぶか {#what-to-do}
