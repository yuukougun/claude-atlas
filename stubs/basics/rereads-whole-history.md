---
id: rereads-whole-history
title: 毎ターン全履歴を読み直す
aliases: [会話全体の再送, ステートレス, 長い会話が重い理由, 読み直す受験者]
type: concept
field: basics
chapter: コンテキストと注意
order: 30
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [散らかっている, 合っていない]
summary: Claude は毎回、会話の最初からすべてを読み直して返事をするので、長い会話ほど遅く重く、上限も早く使うことが分かる。同じ前置きが続くとキャッシュで安くなる理由にもつながる。
signs:
  - {type: goal, text: 長い会話ほど返事が遅く、上限の減りも早くなる理由を知りたい}
prerequisites: [tokens]
related: [attention-budget, why-prompt-caching, what-survives-compaction, when-to-start-fresh, stateless-messages-api, what-uses-up-limits, hits-limits-quickly]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
