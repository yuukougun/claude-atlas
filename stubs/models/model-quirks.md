---
id: model-quirks
title: モデル別の癖と、プロンプトの合わせ方
aliases: [モデルごとの傾向, モデル別のプロンプトの指針, モデルの性格]
type: concept
field: models
chapter: 替えたとき・劣化を疑うとき
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code, api, app]
principle: [確かめる]
prevents: [合っていない]
pitfalls: []
summary: 止まりすぎ・やりすぎ・冗長さなど、モデルごとに出やすい傾向を公式の指針から知り、自分の環境で観察してプロンプトを合わせられる。傾向は版で変わるので、暗記せず記録する。
signs:
  - {type: symptom, text: モデルを替えたら、確認ばかりで止まるようになった}
  - {type: goal, text: 使うモデルに合わせてプロンプトを直したい}
prerequisites: [choosing-a-model]
related: [after-switching-models, keeps-stopping, does-more-than-asked, output-shape, permission-to-stop, suggest-or-do, verification-ladder#verbal-checks, emphasis-words, felt-vs-measured, current-models]
tracks: []
outdated_advice: [add-double-check, tell-it-to-use-subagents, keep-going-dont-be-lazy]
sources: []
volatility: 高
sections:
  - {title: 公式の指針に出てくる傾向, anchor: official-guidance}
  - {title: 自分の環境で観察して記録する, anchor: observe-and-record}
stage: stub
updated: 2026-11-04
---

## 公式の指針に出てくる傾向 {#official-guidance}

## 自分の環境で観察して記録する {#observe-and-record}
