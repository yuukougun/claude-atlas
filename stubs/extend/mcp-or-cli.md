---
id: mcp-or-cli
title: MCP か CLI か
aliases: [MCP と CLI の使い分け, MCP より CLI]
type: comparison
field: extend
chapter: MCP
order: 190
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: 外部ツールを MCP でつなぐか、CLI とスキルで済ませるかを選べる。成熟した CLI があればコンテキストの効率がよく、CLI がないときや権限を狭く絞りたいときに MCP が生きる。
signs:
  - {type: goal, text: 外部ツールをつなぐか、コマンドで済ませるかを決めたい}
  - {type: symptom, text: つないだツールの定義や出力で、コンテキストが埋まる}
prerequisites: [connecting-mcp]
related: [move-judgment-into-scripts, how-skills-load, always-on-costs, choosing-mcp-servers, permission-rules, lethal-trifecta, writing-skills]
tracks: [mcp]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
