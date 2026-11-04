---
id: uses-nonexistent-apis
title: 存在しない関数やパッケージを使う
aliases: [存在しない API, 架空のパッケージ, package hallucination]
type: symptom
field: symptoms
chapter: 事実と出典
order: 80
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [見せる, 確かめる]
prevents: [見えていない, 確かめていない, 境界がない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 存在しない関数・引数・パッケージを使われる原因を、読ませた資料と知識の古さから切り分け、読んでから書かせる手と、導入前の確かめ方を決める。
signs:
  - {type: symptom, text: 存在しない関数や引数を自信満々に使う}
  - {type: symptom, text: インストールできないパッケージ名を書かれる}
  - {type: symptom, text: 実行する環境で使えないライブラリを足される}
wave: 1
prerequisites: [why-hallucinations, knowledge-cutoff]
related: [fact-checking, connecting-mcp, read-specs-yourself, doesnt-know-latest, plausible-falsehoods, six-causes]
routes:
  - {cause: 見えていない, to: [choose-what-to-read, code-intelligence-plugins]}
  - {cause: 確かめていない, to: [tests-first, evidence-not-reports]}
  - {cause: 境界がない, to: [vetting-extensions#dependencies]}
tracks: [plugins]
outdated_advice: []
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
