---
id: inconsistent-japanese-style
title: 文体や表記が揃わない
aliases: [です・ますが混ざる, 表記ゆれ, 文体の揺れ]
type: symptom
field: symptoms
chapter: 日本語の出力
order: 200
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る, 見せる]
prevents: [見えていない, 散らかっている, 縛っていない]
pitfalls: []
scenes: [文章, 開発]
summary: です・ますの混在や表記ゆれの原因を、指定の不足・資料の影響・縛りの有無に分けて切り分け、例示で足りるか lint で縛るかを決める。
signs:
  - {type: symptom, text: です・ますとだ・であるが混ざる}
  - {type: symptom, text: 「サーバー」と「サーバ」が混在する}
  - {type: symptom, text: 指定した文体が長い文章の途中で崩れる}
wave: 1
prerequisites: [request-vs-lock]
related: [less-ai-sounding-japanese, documents-in-japanese, requesting-prose, hook-recipes, replies-in-english, not-what-i-meant, instructions-ignored, six-causes]
routes:
  - {cause: 見えていない, to: [consistent-politeness, consistent-notation, show-examples]}
  - {cause: 散らかっている, to: [output-shape#mirror, consistent-politeness#example]}
  - {cause: 縛っていない, to: [textlint-hook, align-japanese-output#lock-layer]}
tracks: [hooks, skills]
outdated_advice: [styles-for-tone]
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
