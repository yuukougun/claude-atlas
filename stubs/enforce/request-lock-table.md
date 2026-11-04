---
id: request-lock-table
title: お願いと鍵の対応表
aliases: [お願いと鍵の早見表, 非決定論的な指示と決定論的な制御の対応表, 指示と強制の対応表]
type: comparison
field: enforce
chapter: 何を縛るか
order: 20
level: 任せる
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発, 文章, チーム]
summary: 完了の判定・禁止・出力の形式・文体などの用途ごとに、お願いの書き方と鍵の手段を並べて選べる。同じ用途でも、面によって使える鍵が違う。
signs:
  - {type: goal, text: この規則をどの仕組みで強制すればよいか知りたい}
  - {type: goal, text: 出力の形式や文体を毎回そろえたい}
prerequisites: [when-to-lock]
related: [request-vs-lock, permission-rules, hooks-basics, stop-hooks, sandboxing, hook-vs-skill, claude-md-vs-rules-skills-styles, structured-outputs-basics, textlint-hook, keep-replies-in-japanese, protect-tests, move-judgment-into-scripts]
tracks: [hooks, permissions, sandbox, claude-md, output-styles, structured-outputs]
outdated_advice: [important-caps, prefill-for-json, styles-for-tone]
sources: []
volatility: 中
sections:
  - {title: 用途ごとの対応表, anchor: table}
  - {title: 鍵にできるのはどこか（ターンの終わりと道具の前後）, anchor: where-locks-act}
  - {title: 面ごとの鍵の手段, anchor: by-surface}
stage: stub
updated: 2026-11-04
---

## 用途ごとの対応表 {#table}

## 鍵にできるのはどこか（ターンの終わりと道具の前後） {#where-locks-act}

## 面ごとの鍵の手段 {#by-surface}
