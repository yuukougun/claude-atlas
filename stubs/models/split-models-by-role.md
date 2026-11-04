---
id: split-models-by-role
title: 計画・実装・サブエージェントでモデルを分ける
nav_title: 役割でモデルを分ける
aliases: [opusplan, 計画は Opus・実装は Sonnet, サブエージェントのモデル, subagent のモデル, Haiku の使いどころ, 軽いモデルの使いどころ, CLAUDE_CODE_SUBAGENT_MODEL]
type: concept
field: models
chapter: 役割で使い分ける
order: 100
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [見せる]
prevents: [合っていない]
pitfalls: []
summary: 計画と実装、本体とサブエージェントでモデルを分けるかを、仕事の重さの差と費用で決められる。分けた側で動く effort と、引き継がれる文脈も確かめる。
signs:
  - {type: goal, text: 計画は賢いモデル、実装は安いモデルに分けたい}
  - {type: goal, text: サブエージェントだけ軽いモデルで動かして、使用量を抑えたい}
  - {type: situation, text: 「計画は上位のモデル、実装は安いモデル」というコツが今も得か分からない}
prerequisites: [choosing-a-model, subagent-isolation]
related: [effort-levels#subagents-and-org-limits, when-to-plan, writing-subagents, fast-mode-and-advisor, current-models, saving-priorities, independent-review]
tracks: [model-selection, subagents]
outdated_advice: [avoid-opus-as-expensive]
sources: []
volatility: 高
sections:
  - {title: 分ける形（計画と実装・本体とサブエージェント）, anchor: patterns}
  - {title: 分ける価値があるとき, anchor: when-to-split}
  - {title: 軽いモデルの使いどころ, anchor: lighter-models}
stage: stub
updated: 2026-11-04
---

## 分ける形（計画と実装・本体とサブエージェント） {#patterns}

## 分ける価値があるとき {#when-to-split}

## 軽いモデルの使いどころ {#lighter-models}
