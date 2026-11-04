---
id: plausible-falsehoods
title: もっともらしい嘘・出典の誤り
aliases: [ハルシネーション, 存在しない出典, 嘘の引用, 答えが毎回違う]
type: symptom
field: symptoms
chapter: 事実と出典
order: 70
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる, 見せる]
prevents: [見えていない, 確かめていない]
pitfalls: []
scenes: [調べもの, 文章, 学習]
summary: もっともらしい嘘や存在しない出典を、見せた資料と確かめ方の不足から切り分け、引用・照合・「分からない」と言わせる手を選ぶ。
signs:
  - {type: symptom, text: もっともらしいが出典が怪しい}
  - {type: symptom, text: 存在しない論文や URL を挙げられる}
  - {type: symptom, text: 同じ質問をするたびに答えが変わり、どれが正しいか分からない}
  - {type: symptom, text: 確かめると数字や引用が原文と違っている}
wave: 1
prerequisites: [why-hallucinations]
related: [nondeterminism, using-research, knowledge-cutoff, citations-basics, second-opinion-from-another-model, agreement-is-not-evidence, summary-overstates-source, uses-nonexistent-apis, doesnt-know-latest, caves-when-pushed, six-causes]
routes:
  - {cause: 見えていない, to: [allow-i-dont-know, search-research-thinking]}
  - {cause: 確かめていない, to: [fact-checking, checking-citations]}
tracks: [web-search, research, citations]
outdated_advice: [lower-temperature]
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
