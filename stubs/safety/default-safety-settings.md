---
id: default-safety-settings
title: 安全の早見表（面ごとの既定と、段階ごとに足すもの）
nav_title: 安全の早見表
aliases: [安全の既定, 安全の設定の早見表, 最低限の安全の設定]
type: comparison
field: safety
chapter: 既定と承認
order: 10
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る, 握る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: アプリ・Claude Code・API の、権限・通信・データ・記録の既定を並べて比べられる。公式の既定を基準に、任せる段階ごとに足す設定が分かる。
signs:
  - {type: goal, text: 安全のために、最低限どこまで設定すればよいか知りたい}
  - {type: goal, text: アプリと Claude Code で、既定の安全の設定がどう違うか知りたい}
  - {type: situation, text: Claude に任せる範囲を広げようとしている}
prerequisites: [where-your-data-goes, permission-modes-overview]
related: [what-auto-mode-stops, sandboxing, protecting-secrets, where-bypass-is-ok, entrusted-data, lethal-trifecta, approval-fatigue, permission-modes-in-the-app, four-principles, five-questions-before-delegating, headless-basics, incognito-chats]
tracks: [permission-modes, auto-mode, sandbox, incognito, app-memory]
sources: []
volatility: 高
sections:
  - {title: 面ごとの既定（生成の表）, anchor: defaults-by-surface}
  - {title: 段階ごとに足すもの, anchor: by-stage}
  - {title: 公式の既定の限界, anchor: limits}
stage: stub
updated: 2026-11-04
---

## 面ごとの既定（生成の表） {#defaults-by-surface}

## 段階ごとに足すもの {#by-stage}

## 公式の既定の限界 {#limits}
