---
id: doesnt-know-latest
title: 最新の情報を知らない
aliases: [知識カットオフ, 古い情報で答える, 新しい版を知らない]
type: symptom
field: symptoms
chapter: 事実と出典
order: 90
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [調べもの, 開発]
summary: 最近の出来事や新しい版について間違える原因を知識の締め切りから切り分け、検索・公式の資料・日付の確かめ方のどれを使うかを決める。
signs:
  - {type: symptom, text: 最近の出来事や新しい版について間違える}
  - {type: symptom, text: Claude Code の新しい機能について聞くと古い答えが返る}
  - {type: symptom, text: 古い書き方のコードや設定を出してくる}
wave: 1
prerequisites: [knowledge-cutoff]
related: [using-research, connectors-in-the-app, old-advice-doesnt-work, dating-information, plausible-falsehoods, uses-nonexistent-apis, six-causes]
routes:
  - {cause: 見えていない, to: [search-research-thinking, choose-what-to-read, ask-claude-code]}
tracks: [web-search, research]
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
