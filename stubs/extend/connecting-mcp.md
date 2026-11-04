---
id: connecting-mcp
title: MCP をつなぐ
aliases: [MCP サーバー, Model Context Protocol, claude mcp add, .mcp.json, /mcp]
type: feature
field: extend
chapter: MCP
order: 180
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 境界がない]
pitfalls: []
scenes: [開発, データ分析]
summary: 外部のサービスやツールを MCP でつなぎ、共有の範囲と資格情報を決め、つながらないときは切り分けられる。誰と使うかでスコープを選び、信頼できるサーバーと読み取り専用の資格情報から始める。
signs:
  - {type: goal, text: ブラウザからコピーして貼っているデータを、直接取りに行かせたい}
  - {type: goal, text: 社内のツールや外部のサービスを、Claude から使いたい}
  - {type: situation, text: チームで同じ外部ツールへの接続を使いたい}
  - {type: symptom, text: MCP サーバーをつないだのに、ツールが出てこない・つながらない}
prerequisites: [agent-loop]
related: [vetting-extensions, mcp-or-cli, choosing-mcp-servers, lethal-trifecta, prompt-injection-in-practice, protecting-secrets, connectors-in-the-app, always-on-costs, inspect-context, settings-layers, isolate-with-safe-mode, org-managed-settings-and-mcp, plugins-and-marketplaces, share-team-settings]
tracks: [mcp]
outdated_advice: [mcp-sse-transport]
sources: []
volatility: 中
sections:
  - {title: スコープと共有, anchor: scopes}
  - {title: 資格情報と権限, anchor: credentials}
  - {title: つながらない・ツールが出てこないとき, anchor: troubleshooting}
  - {title: Desktop アプリの MCP との関係, anchor: desktop}
stage: stub
updated: 2026-11-04
---

## スコープと共有 {#scopes}

## 資格情報と権限 {#credentials}

## つながらない・ツールが出てこないとき {#troubleshooting}

## Desktop アプリの MCP との関係 {#desktop}
