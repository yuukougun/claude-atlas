---
id: does-more-than-asked
title: 頼んでいないことまでやる（過剰設計）
nav_title: 頼んでいないことまでやる
aliases: [過剰設計, スコープの膨張, over-engineering, 余計な変更, 死んだコードを残す, 作業フォルダが散らかる]
type: symptom
field: symptoms
chapter: 返答と品質
order: 20
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [見せる, 確かめる]
prevents: [見えていない, 確かめていない, 合っていない]
pitfalls: []
scenes: [開発]
summary: 頼んでいない機能・ファイル・抽象化が増える原因を、範囲の伝え方と effort・モデルの選び方に分けて切り分け、範囲の指定と差分の確かめ方を決める。
signs:
  - {type: symptom, text: 頼んでいない機能やファイルが増える}
  - {type: symptom, text: 小さな修正を頼んだのに周りまで書き換えられる}
  - {type: symptom, text: 使わない抽象化や設定項目を勝手に足される}
  - {type: symptom, text: 古いコードを消さずに新しい版を足していく}
  - {type: symptom, text: 作業フォルダに一時ファイルを残していく}
wave: 1
prerequisites: []
related: [suggest-or-do, ask-for-outcomes, what-to-put-in-claude-md, own-generated-code, independent-review, rewind-dont-correct, output-shape, not-what-i-meant, keeps-stopping, six-causes]
routes:
  - {cause: 見えていない, to: [state-the-scope, when-to-plan, spec-first]}
  - {cause: 確かめていない, to: [diffs-humans-must-read, working-with-git]}
  - {cause: 合っていない, to: [effort-levels, model-quirks]}
tracks: [effort, plan-mode]
outdated_advice: [keep-going-dont-be-lazy]
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
