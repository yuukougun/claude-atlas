---
id: lethal-trifecta
title: 三つを同時に持たせない（lethal trifecta と Rule of Two）
nav_title: 三つを同時に持たせない
aliases: [lethal trifecta, Rule of Two, Agents Rule of Two, 最小権限]
type: concept
field: safety
chapter: 悪意ある入力
order: 100
level: 任せる
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, 調べもの, チーム]
summary: 信頼できない入力・秘密や私的なデータ・外への送信や変更の三つを一つの構成に同時に持たせないことで、仕込まれた指示が被害につながる経路を断てる。三つとも要る作業には人の承認を挟む。
signs:
  - {type: goal, text: メールや Web を読ませつつ、社内のデータにもつなぎたい}
  - {type: situation, text: コネクタや MCP を増やして、何でもできる構成になっている}
  - {type: situation, text: Web ページやメールを読ませるのが不安}
prerequisites: [prompt-injection-in-practice]
related: [vetting-extensions, browser-agent-cautions, sandboxing, protecting-secrets, secrets-exposed, what-auto-mode-stops, default-safety-settings, permission-modes-in-the-app, connectors-in-the-app, connecting-mcp, five-questions-before-delegating, tasks-and-schedules-in-the-app]
sources: []
volatility: 低
sections:
  - {title: 三つの能力, anchor: three-capabilities}
  - {title: 面ごとの当てはめ, anchor: by-surface}
  - {title: 三つとも要るとき, anchor: when-all-three}
stage: stub
updated: 2026-11-04
---

## 三つの能力 {#three-capabilities}

## 面ごとの当てはめ {#by-surface}

## 三つとも要るとき {#when-all-three}
