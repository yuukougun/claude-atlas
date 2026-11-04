---
id: say-what-you-want
title: 否定形ではなく、望む形で書く
aliases: [「するな」より「こうして」, 正の例で示す, Tell Claude what to do instead]
type: concept
field: prompting
chapter: 頼み方の原則
order: 50
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
scenes: [文章, 開発]
summary: 「〜するな」より「〜で書け」と望む形を示すほうが守られやすい。例外を許さない禁止は言葉を重ねず、フックや権限のルールなどの仕組みに移す。
signs:
  - {type: symptom, text: 「使うな」と書いたのに、かえってそれが出てくる}
  - {type: symptom, text: 禁止事項を足すほど、出力がぎこちなくなる}
prerequisites: [give-reasons, request-vs-lock]
related: [emphasis-words, state-the-scope, output-shape, show-examples, when-to-lock, permission-rules]
sources: []
volatility: 低
sections:
  - {title: 禁止を望む形に書き換える, anchor: rewrite}
  - {title: 例外のない禁止は仕組みへ（二層）, anchor: two-layers}
stage: stub
updated: 2026-11-04
---

## 禁止を望む形に書き換える {#rewrite}

## 例外のない禁止は仕組みへ（二層） {#two-layers}
