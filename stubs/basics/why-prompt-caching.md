---
id: why-prompt-caching
title: プロンプトキャッシング（先頭が変わらないことの価値）
nav_title: プロンプトキャッシングの仕組み
aliases: [cache, キャッシュが切れる, 先頭部分の一致]
type: concept
field: basics
chapter: コンテキストと注意
order: 50
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [合っていない]
summary: 会話の先頭（ツールの定義・システムプロンプト・前の発言）が変わらなければ読み直しが安く済み、途中で変えるとそこから後のキャッシュが外れることが分かる。途中で何を変えないかと、よく使う資料をどこに置くかを決める土台になる。
signs:
  - {type: goal, text: セッションの途中でモデルや設定を変えると費用が増える理由を知りたい}
prerequisites: [rereads-whole-history]
related: [prompt-caching-in-practice, using-projects, compact-and-auto-compact, always-on-costs, what-uses-up-limits, how-thinking-works]
tracks: [prompt-caching]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
