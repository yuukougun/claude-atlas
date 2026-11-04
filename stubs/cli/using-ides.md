---
id: using-ides
title: IDE（VS Code・JetBrains）で使う
aliases: [VS Code の拡張, JetBrains のプラグイン, IDE 連携, /ide]
type: feature
field: cli
chapter: ほかの面と離席
order: 150
level: 整える
priority: 任意
surfaces: [claude-code]
principle: [確かめる, 見せる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: IDE の拡張では、計画を文書として読んでコメントで返し、差分を一つずつ受け入れ、選んだ範囲を自動で渡せる。ターミナルの CLI とできることが一部違い、IDE が自動で実行する設定ファイルの書き換えには注意する。
signs:
  - {type: goal, text: VS Code の中で差分を見ながら Claude Code を使いたい}
  - {type: situation, text: WSL の CLI から IDE につながらない}
prerequisites: [claude-code-surfaces]
related: [when-to-plan, checkpoints-and-rewind, permission-modes-overview, diffs-humans-must-read, protecting-secrets, windows-wsl-ime]
tracks: [ide-extensions]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: IDE で得られるもの, anchor: what-you-get}
  - {title: CLI との違い, anchor: vs-cli}
  - {title: 安全の注意, anchor: safety}
stage: stub
updated: 2026-11-04
---

## IDE で得られるもの {#what-you-get}

## CLI との違い {#vs-cli}

## 安全の注意 {#safety}
