---
id: choose-what-to-read
title: '@参照と、何を読ませるかの絞り込み'
aliases: ['@ でファイルを指定する', 読ませるファイルを絞る, 長いコマンド出力を絞る]
type: concept
field: context
chapter: 見る・絞る
order: 120
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発, データ分析]
summary: 読むべきファイルを @ で直接指し、テストやログの長い出力は要点の数行に絞ってから会話に入れる。探させる手間と、関係のない読み込みが答えをぼかすことの両方を減らせる。
signs:
  - {type: goal, text: 読ませるファイルを自分で指定したい}
  - {type: situation, text: 大きなコードベースで作業している}
prerequisites: [context-rot]
related: [input-symbols, handing-long-documents, research-in-subagents, inspect-context, hook-recipes, explore-a-codebase, code-intelligence-plugins, four-specifics, mcp-or-cli, protecting-secrets]
tracks: [context-window]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 直接指すか、探させるか, anchor: point-or-search}
  - {title: 出力を絞る, anchor: trim-output}
  - {title: '@ 参照の注意', anchor: caveats}
stage: stub
updated: 2026-11-04
---

## 直接指すか、探させるか {#point-or-search}

## 出力を絞る {#trim-output}

## @ 参照の注意 {#caveats}
