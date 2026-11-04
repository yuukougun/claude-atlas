---
id: summary-overstates-source
title: 要約が原文より断定的になる
aliases: [要約の言い過ぎ, 条件が落ちる要約]
type: symptom
field: symptoms
chapter: 事実と出典
order: 120
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [見えていない, 確かめていない]
pitfalls: []
scenes: [調べもの, 学習, 文章]
summary: 要約が原文より断定的になったときに、落ちた条件や但し書きを原文と照らして見つけ、要約を信じてよい範囲を決める。
signs:
  - {type: symptom, text: 要約すると「場合がある」が「必ず」になる}
  - {type: symptom, text: 論文の要約が原文の結論より強い}
  - {type: symptom, text: 条件や但し書きが要約から落ちる}
wave: 1
prerequisites: [summary-overgeneralization]
related: [research-and-reports, using-research, learning-with-ai, handing-long-documents, plausible-falsehoods, skipped-later-pages, six-causes]
routes:
  - {cause: 見えていない, to: [long-context-first#quote-first]}
  - {cause: 確かめていない, to: [fact-checking#summaries, checking-citations, read-specs-yourself]}
tracks: [research]
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
