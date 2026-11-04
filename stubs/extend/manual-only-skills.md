---
id: manual-only-skills
title: 副作用のあるスキルを勝手に動かさない
aliases: [disable-model-invocation, 手動専用のスキル, user-invocable]
type: feature
field: extend
chapter: スキル
order: 130
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発]
summary: デプロイのような副作用のある手順を、Claude が自分の判断で動かさないようにできる。人だけが呼べる設定と、それでも鍵が要る場面を見分ける。
signs:
  - {type: goal, text: デプロイ用の手順を、勝手に動かされたくない}
  - {type: symptom, text: デプロイのような手順を、頼んでいないのに始められた}
prerequisites: [writing-skills]
related: [skill-descriptions, permission-rules, destructive-commands, hook-vs-skill, when-to-lock, does-more-than-asked]
tracks: [skills]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
