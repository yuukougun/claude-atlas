---
id: tool-use-loop
title: tool use のループ
aliases: [function calling, client tools, server tools, tool_choice]
type: concept
field: api
chapter: API の主な機能
order: 30
level: 仕組みにする
priority: 推奨
surfaces: [api]
principle: [縛る, 見せる]
prevents: [縛っていない, 境界がない]
scenes: [開発]
summary: Claude が道具の呼び出しを頼み、呼び出し側が実行して結果を返すループの形が分かる。必ず呼ばせたい・形を守らせたいときに、指示でなく設定で縛る理由も分かる。
signs:
  - {type: goal, text: 自分の関数を Claude に呼ばせたい}
  - {type: symptom, text: 道具を呼んでほしい場面で、呼ばずに答えてしまう}
prerequisites: [agent-loop]
related: [designing-agent-tools, structured-outputs-basics, sdk-comparison, lethal-trifecta, data-vs-instructions, request-vs-lock, connecting-mcp]
tracks: [tool-use, server-tools]
sources: []
volatility: 中
sections:
  - {title: client tools と server tools, anchor: client-and-server}
  - {title: 呼ばせ方を縛る（tool_choice・strict）, anchor: forcing}
  - {title: ループを誰が回すか, anchor: who-runs-the-loop}
stage: stub
updated: 2026-11-04
---

## client tools と server tools {#client-and-server}

## 呼ばせ方を縛る（tool_choice・strict） {#forcing}

## ループを誰が回すか {#who-runs-the-loop}
