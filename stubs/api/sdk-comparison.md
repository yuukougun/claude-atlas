---
id: sdk-comparison
title: Client SDK・Agent SDK・Managed Agents・CLI の比較
nav_title: SDK と CLI の比較
aliases: [Claude Managed Agents, Agent SDK と Managed Agents の位置づけ, どの SDK を使うか, Anthropic SDK]
type: comparison
field: api
chapter: エージェントを組む
order: 90
level: 仕組みにする
priority: 必須
surfaces: [api, claude-code]
principle: [握る, 縛る]
prevents: [合っていない]
scenes: [開発]
summary: Client SDK・Agent SDK・Managed Agents・CLI を、ループを誰が回すか、どこで動くかで比べ、自分の用途に合う層を選べる。
signs:
  - {type: goal, text: 自分のアプリに Claude を組み込みたい}
  - {type: goal, text: エージェントのループを自分で書くか、任せるかを決めたい}
prerequisites: [choosing-a-surface, agent-loop]
related: [agent-sdk-basics, tool-use-loop, headless-basics, choosing-automation, where-your-data-goes, sandboxing, long-running-agent-context, feature-to-api-mapping]
tracks: [messages-api, agent-sdk, managed-agents, headless]
sources: []
volatility: 中
sections:
  - {title: 層ごとの比較（自分のプロセスに組み込む・Anthropic にホストさせる・CLI で動かす）, anchor: comparison}
  - {title: Managed Agents（Anthropic がループと環境を持つ）, anchor: managed-agents}
  - {title: 選び方の判断例, anchor: examples}
stage: stub
updated: 2026-11-04
---

## 層ごとの比較（自分のプロセスに組み込む・Anthropic にホストさせる・CLI で動かす） {#comparison}

## Managed Agents（Anthropic がループと環境を持つ） {#managed-agents}

## 選び方の判断例 {#examples}
