---
id: request-vs-lock
title: お願いと鍵（決定論的か、非決定論的か）
nav_title: お願いと鍵
aliases: [決定論的な制御, 非決定論的な指示, deterministic, 指示と強制]
type: concept
field: basics
chapter: 指示と仕組み
order: 180
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る]
prevents: [縛っていない]
summary: プロンプト・CLAUDE.md・スキルのような指示は Claude が読んで判断するお願いで、フック・deny ルール・管理設定は毎回必ず効く鍵だと分かる。例外を許さない規則を鍵に移す判断の土台になる。
signs:
  - {type: goal, text: 「必ず」と書いた規則でも破られる理由を知りたい}
  - {type: goal, text: どの規則を仕組みで強制すべきか見分けたい}
prerequisites: []
related: [when-to-lock, request-lock-table, hook-vs-skill, instructions-ignored, where-instructions-sit, data-vs-instructions, emphasis-words, hooks-basics, permission-rules, four-principles#lock]
outdated_advice: [important-caps]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
