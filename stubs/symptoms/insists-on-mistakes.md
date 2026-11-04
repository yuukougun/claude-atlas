---
id: insists-on-mistakes
title: 誤りを認めずに言い張る
aliases: [間違いを認めない, 存在しないものをあると言い張る, 言い訳が続く]
type: symptom
field: symptoms
chapter: 返答と品質
order: 60
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [見えていない, 散らかっている, 確かめていない]
pitfalls: []
scenes: [開発]
summary: 誤りを指摘しても認めずに言い張るときに、言い争う代わりに実物（履歴・検索・実行結果）を見せて確かめ、会話を巻き戻すかを決める。
signs:
  - {type: symptom, text: 間違いを指摘しても認めずに言い張る}
  - {type: symptom, text: 存在しないバグや変更をあったことにして譲らない}
  - {type: symptom, text: 説明と実際の履歴が食い違っている}
wave: 1
prerequisites: [context-rot]
related: [why-hallucinations, unfaithful-reasoning, caves-when-pushed, going-in-circles, blames-the-tools, plausible-falsehoods, six-causes]
routes:
  - {cause: 見えていない, to: [choose-what-to-read, working-with-git]}
  - {cause: 散らかっている, to: [rewind-dont-correct, when-to-start-fresh]}
  - {cause: 確かめていない, to: [evidence-not-reports#facts-win]}
tracks: []
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
