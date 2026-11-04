---
id: code-intelligence-plugins
title: code intelligence プラグイン（LSP）
aliases: [LSP, 言語サーバー, コードインテリジェンス]
type: feature
field: extend
chapter: プラグイン
order: 220
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発]
summary: 型のある言語で、定義へのジャンプや型エラーの報告を Claude に使わせられる。ファイルを総当たりで読む代わりに言語サーバーに尋ねるので、探索で読む量が減る。
signs:
  - {type: symptom, text: 関数の定義を探すたびに、多くのファイルを読ませている}
  - {type: goal, text: 編集の後の型エラーに、Claude 自身に気づかせたい}
prerequisites: [plugins-and-marketplaces]
related: [choose-what-to-read, explore-a-codebase, using-ides, vetting-extensions, when-to-add-what]
tracks: [code-intelligence, plugins]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
