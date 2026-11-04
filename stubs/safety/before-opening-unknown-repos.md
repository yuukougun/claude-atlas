---
id: before-opening-unknown-repos
title: 知らないリポジトリを開く前に
aliases: [clone したリポジトリの確認, workspace trust, 信頼のダイアログ, 設定ファイルもコードとして扱う]
type: recipe
field: safety
chapter: 悪意ある入力
order: 110
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 知らないリポジトリを Claude Code で開く前に、設定・フック・MCP の定義など、開くだけで動きうるものを確かめられる。信頼の確認が出ない非対話の実行は、隔離した環境で動かす。
signs:
  - {type: goal, text: 知らない人のリポジトリを開きたい}
  - {type: situation, text: 配られたコードや README の手順を、Claude に実行させたい}
prerequisites: [prompt-injection-in-practice, permission-rules]
related: [vetting-extensions, writing-safe-hooks, hooks-basics, sandboxing, where-bypass-is-ok, protecting-secrets, explore-a-codebase, headless-basics, cloud-sessions-and-teleport]
tracks: [settings, hooks, mcp]
sources: []
volatility: 中
sections:
  - {title: 開く前に見るファイル, anchor: files-to-check}
  - {title: 信頼の前と後で効くもの, anchor: trust}
  - {title: 非対話の実行では確認が出ない, anchor: headless}
  - {title: 隔離して動かす, anchor: isolate}
stage: stub
updated: 2026-11-04
---

## 開く前に見るファイル {#files-to-check}

## 信頼の前と後で効くもの {#trust}

## 非対話の実行では確認が出ない {#headless}

## 隔離して動かす {#isolate}
