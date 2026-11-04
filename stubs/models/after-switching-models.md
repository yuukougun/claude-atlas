---
id: after-switching-models
title: 新しいモデルに替えたら見直すこと
aliases: [モデルの移行, 既定のモデルが変わったとき, 旧モデルの退役, モデルの非推奨]
type: recipe
field: models
chapter: 替えたとき・劣化を疑うとき
order: 90
level: 任せる
priority: 必須
surfaces: [claude-code, api, app]
principle: [確かめる]
prevents: [合っていない]
pitfalls: []
summary: モデルを替えたときや既定が変わったときに、effort の持ち越し・古い強調や検証の指示・使えなくなった API の引数を見直せる。外すものは一つずつ外し、効果を測る。
signs:
  - {type: situation, text: 既定のモデルが新しくなったと知った}
  - {type: symptom, text: モデルを替えてから、API がエラーを返すようになった}
  - {type: goal, text: 旧いモデルが使えなくなる前に、移行を済ませたい}
prerequisites: [choosing-a-model, effort-levels, measure-changes]
related: [model-quirks, harness-over-model, emphasis-words, verification-ladder#verbal-checks, structured-outputs-basics, claude-md-length, outdated-advice-ledger, change-timeline-2026]
tracks: [model-selection, effort, adaptive-thinking]
outdated_advice: [budget-tokens, prefill-for-json, lower-temperature, important-caps, add-double-check]
sources: []
volatility: 高
sections:
  - {title: 見直す順, anchor: checklist}
  - {title: API の引数とモデルの世代, anchor: api-parameters}
  - {title: ハーネスの部品を一つずつ外して測る, anchor: remove-one-at-a-time}
  - {title: 退役と既定の変化に気づく, anchor: retirements-and-default-changes}
stage: stub
updated: 2026-11-04
---

## 見直す順 {#checklist}

## API の引数とモデルの世代 {#api-parameters}

## ハーネスの部品を一つずつ外して測る {#remove-one-at-a-time}

## 退役と既定の変化に気づく {#retirements-and-default-changes}
