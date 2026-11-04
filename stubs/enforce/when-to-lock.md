---
id: when-to-lock
title: お願いを鍵に移す判断
aliases: [お願いから鍵へ, 指示を仕組みに移す, 決定論的な制御に移す, 会話で言った禁止事項は圧縮で消える]
type: concept
field: enforce
chapter: 何を縛るか
order: 10
level: 任せる
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る]
prevents: [縛っていない, 散らかっている]
pitfalls: []
scenes: [開発, チーム]
summary: 頼んだ規則のうち、どれを権限ルールやフックに移すかを判断できる。同じ注意を二回した、強調しても破られた、会話で言った禁止が圧縮で消えた、が移す合図になる。
signs:
  - {type: symptom, text: CLAUDE.md に「〜しない」と書いたのに破られる}
  - {type: symptom, text: 「push しないで」と言ったのに、しばらくすると push された}
  - {type: goal, text: 例外なく守らせたい規則がある}
prerequisites: [request-vs-lock, what-survives-compaction]
related: [request-lock-table, permission-rules, hooks-basics, lock-side-effects, move-judgment-into-scripts, instructions-ignored, forgot-after-compaction, promises-after-compaction, what-to-put-in-claude-md#what-to-leave-out, emphasis-words, hook-vs-skill]
tracks: [claude-md, hooks, permissions, compaction]
outdated_advice: [important-caps]
sources: []
volatility: 中
sections:
  - {title: 鍵に移す合図, anchor: signals}
  - {title: 会話で言った禁止は圧縮で消える, anchor: spoken-rules-fade}
  - {title: 鍵にしない規則（判断を含むもの）, anchor: what-not-to-lock}
stage: stub
updated: 2026-11-04
---

## 鍵に移す合図 {#signals}

## 会話で言った禁止は圧縮で消える {#spoken-rules-fade}

## 鍵にしない規則（判断を含むもの） {#what-not-to-lock}
