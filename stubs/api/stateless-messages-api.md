---
id: stateless-messages-api
title: Messages API と会話の正体
aliases: [stateless, message threads, system と messages]
type: concept
field: api
chapter: アプリと API の対応
order: 20
level: 任せる
priority: 推奨
surfaces: [api]
principle: [見せる]
prevents: [散らかっている]
scenes: [開発]
summary: Messages API の基本の形は状態を持たず、呼び出し側が system と messages で毎回それまでの全体を渡すことが分かる。message threads で送る量を減らしても、モデルが読む量は変わらないことも分かる。
signs:
  - {type: symptom, text: API で呼ぶと、前の発言を覚えていない}
  - {type: goal, text: API で会話を続けるには、毎回何を送ればよいか知りたい}
prerequisites: [rereads-whole-history]
related: [feature-to-api-mapping, prompt-caching-in-practice, long-running-agent-context, where-instructions-sit, attention-budget, where-your-data-goes, what-uses-up-limits]
tracks: [messages-api, message-threads]
sources: []
volatility: 中
sections:
  - {title: 毎回、全体を渡す, anchor: stateless}
  - {title: system と messages, anchor: system-and-messages}
  - {title: message threads（送る量だけを減らす）, anchor: message-threads}
stage: stub
updated: 2026-11-04
---

## 毎回、全体を渡す {#stateless}

## system と messages {#system-and-messages}

## message threads（送る量だけを減らす） {#message-threads}
