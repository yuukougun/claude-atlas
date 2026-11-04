---
id: followed-injected-instructions
title: 読ませたページやファイルの指示に従ってしまった
nav_title: 読ませたものの指示に従った
aliases: [prompt injection にかかった, 資料の中の指示に従う, 勝手に送信しようとした]
type: symptom
field: symptoms
chapter: 安全と承認
order: 300
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る, 握る]
prevents: [縛っていない, 境界がない]
pitfalls: []
scenes: [開発, 調べもの]
summary: 読ませた Web ページやファイルに書かれた指示に従ってしまったときに、何を読ませ何を許していたかを切り分け、読ませ方と許す操作の組み合わせを決め直す。
signs:
  - {type: symptom, text: 読ませた Web ページに書かれた指示どおりに動いた}
  - {type: symptom, text: 頼んでいない送信や操作をしようとした}
  - {type: symptom, text: 資料を読ませたら答えが不自然な方向に誘導された}
wave: 1
prerequisites: [data-vs-instructions]
related: [browser-agent-cautions, before-opening-unknown-repos, vetting-extensions, connectors-in-the-app, sandboxing, secrets-exposed, refused-or-blocked, six-causes]
routes:
  - {cause: 縛っていない, to: [permission-rules, what-auto-mode-stops#limits]}
  - {cause: 境界がない, to: [lethal-trifecta, prompt-injection-in-practice, instructions-hidden-in-materials]}
tracks: [connectors, mcp, web-search, claude-in-chrome, auto-mode]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
