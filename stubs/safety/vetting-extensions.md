---
id: vetting-extensions
title: MCP・プラグイン・スキルを入れる前の確認
aliases: [MCP サーバーの安全, rug pull, プラグインの確認, スキルの確認, MCP・plugins・skills を入れる前の確認, 依存のパッケージの確認, slopsquatting]
type: recipe
field: safety
chapter: 悪意ある入力
order: 120
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: MCP サーバー・プラグイン・スキルや依存のパッケージを入れる前に、出所・持つ権限・中身（道具の説明やスクリプト）を確かめられる。入れたものは利用者の権限で動き、後から中身が変わることもある。
signs:
  - {type: situation, text: 便利そうな MCP やプラグインを見つけた}
  - {type: goal, text: 入れた拡張が安全かを確かめたい}
  - {type: goal, text: Claude が足そうとしているパッケージが、本物か確かめたい}
prerequisites: [prompt-injection-in-practice, connecting-mcp]
related: [lethal-trifecta, plugins-and-marketplaces, choosing-mcp-servers, mods, connectors-in-the-app, plugins-in-the-app, skills-in-the-app, writing-safe-hooks, looks-are-not-quality, uses-nonexistent-apis, pruning-extensions, org-managed-settings-and-mcp]
tracks: [mcp, plugins, marketplaces, skills, connectors, mods]
sources: []
volatility: 中
sections:
  - {title: 出所を確かめる, anchor: provenance}
  - {title: 中身を読む（道具の説明・フック・スクリプト）, anchor: read-contents}
  - {title: 入れた後に変わる（rug pull）, anchor: changes-after-install}
  - {title: 依存のパッケージを入れる前に（存在しない名前・後から登録された名前）, anchor: dependencies}
stage: stub
updated: 2026-11-04
---

## 出所を確かめる {#provenance}

## 中身を読む（道具の説明・フック・スクリプト） {#read-contents}

## 入れた後に変わる（rug pull） {#changes-after-install}

## 依存のパッケージを入れる前に（存在しない名前・後から登録された名前） {#dependencies}
