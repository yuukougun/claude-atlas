---
id: designing-agent-tools
title: エージェント用のツールを設計する原則
aliases: [ツールの設計, Writing effective tools for agents, MCP サーバーの設計]
type: concept
field: api
chapter: エージェントを組む
order: 120
level: 仕組みにする
priority: 任意
surfaces: [api, claude-code]
principle: [見せる, 確かめる]
prevents: [散らかっている, 見えていない]
scenes: [開発]
summary: エージェントに渡す道具を少なく統合し、返す情報を絞り、評価で直すという設計の原則が分かる。MCP サーバーや自作のツールを作るときに使える。
signs:
  - {type: goal, text: エージェント用の道具や MCP サーバーを作りたい}
  - {type: symptom, text: 道具を増やしたら、エージェントが道具を選び間違える}
prerequisites: [tool-use-loop]
related: [measure-changes, lethal-trifecta, mcp-or-cli, choosing-mcp-servers, move-judgment-into-scripts, always-on-costs, connecting-mcp]
tracks: [tool-use]
sources: []
volatility: 低
sections:
  - {title: 少なく、まとめて, anchor: fewer-tools}
  - {title: 返す情報を絞る, anchor: high-signal-output}
  - {title: 評価で直す, anchor: evaluate}
stage: stub
updated: 2026-11-04
---

## 少なく、まとめて {#fewer-tools}

## 返す情報を絞る {#high-signal-output}

## 評価で直す {#evaluate}
