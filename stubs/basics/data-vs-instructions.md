---
id: data-vs-instructions
title: データと命令を区別できない（prompt injection の原理）
nav_title: データと命令を区別できない
aliases: [prompt injection, プロンプトインジェクション, 間接プロンプトインジェクション, 読ませた文書の指示に従う]
type: concept
field: basics
chapter: 指示と仕組み
order: 190
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る]
prevents: [境界がない]
scenes: [開発, 調べもの]
summary: 読ませた Web ページやファイルの中の文も頼んだ指示と同じ文脈に並ぶので、Claude はデータと命令を確実には分けられないことが分かる。バグではなく性質なので、権限と経路で守る理由になる。
signs:
  - {type: situation, text: Web ページやメールを読ませるのが不安}
  - {type: goal, text: 読ませた資料の中の指示に、なぜ従ってしまうのか知りたい}
prerequisites: []
related: [prompt-injection-in-practice, lethal-trifecta, instructions-hidden-in-materials, before-opening-unknown-repos, vetting-extensions, browser-agent-cautions, sandboxing]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
