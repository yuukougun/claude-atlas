---
id: prompt-injection-in-practice
title: プロンプトインジェクションの実際
aliases: [tool poisoning, 仕込まれた指示]
type: concept
field: safety
chapter: 悪意ある入力
order: 80
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, 調べもの]
summary: 読ませた Web ページ・ファイル・issue・道具の説明に仕込まれた指示に、Claude が従ってしまう経路と型が分かる。防ぐ手立ては、モデルの賢さではなく、持たせる権限と通信の組み合わせの側にある。
signs:
  - {type: situation, text: Web ページやメールを読ませるのが不安}
  - {type: goal, text: 外部の資料を、安全に読ませたい}
prerequisites: [data-vs-instructions]
related: [lethal-trifecta, instructions-hidden-in-materials, followed-injected-instructions, vetting-extensions, before-opening-unknown-repos, browser-agent-cautions, what-auto-mode-stops, sandboxing, connectors-in-the-app, connecting-mcp]
tracks: [mcp, connectors, web-search]
sources: []
volatility: 中
sections:
  - {title: 指示が入ってくる経路, anchor: channels}
  - {title: よくある型（無害な再現）, anchor: patterns}
  - {title: 検出に頼れない理由, anchor: why-detection-fails}
stage: stub
updated: 2026-11-04
---

## 指示が入ってくる経路 {#channels}

## よくある型（無害な再現） {#patterns}

## 検出に頼れない理由 {#why-detection-fails}
