---
id: agent-sdk-basics
title: Agent SDK（Claude Code をライブラリとして使う）
nav_title: Agent SDK
aliases: [Claude Agent SDK, claude-agent-sdk]
type: feature
field: api
chapter: エージェントを組む
order: 100
level: 回す
priority: 推奨
surfaces: [api, claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない, 境界がない]
scenes: [開発]
summary: Claude Code と同じ道具とループを、自分のプログラムからライブラリとして使える。読み込む設定・権限・課金の経路を、対話の Claude Code との違いとして押さえられる。
signs:
  - {type: goal, text: Claude Code と同じ動きを自分のプログラムから使いたい}
  - {type: situation, text: 社内の仕組みに Claude Code を組み込む}
prerequisites: [sdk-comparison, permission-rules]
related: [headless-basics, bare-mode, hooks-basics, sandboxing, protecting-secrets, check-billing-path, checking-unattended-runs, github-actions-with-claude, long-running-agent-context]
tracks: [agent-sdk, headless]
sources: []
volatility: 高
sections:
  - {title: Claude Code と同じもの・違うもの, anchor: same-and-different}
  - {title: 読み込む設定を決める, anchor: setting-sources}
  - {title: 権限と承認, anchor: permissions}
  - {title: 課金の経路, anchor: billing}
stage: stub
updated: 2026-11-04
---

## Claude Code と同じもの・違うもの {#same-and-different}

## 読み込む設定を決める {#setting-sources}

## 権限と承認 {#permissions}

## 課金の経路 {#billing}
