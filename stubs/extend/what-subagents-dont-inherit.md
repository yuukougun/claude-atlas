---
id: what-subagents-dont-inherit
title: サブエージェントに引き継がれないもの
aliases: [サブエージェントが規則を守らない, omitClaudeMd, 委任のプロンプト]
type: feature
field: extend
chapter: サブエージェント
order: 160
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: サブエージェントに届かない会話・スキル・出力スタイルなどを知り、要る規則を確実に渡せる。委任の文と定義に書き直し、例外を許さない規則はフックで縛る。
signs:
  - {type: symptom, text: サブエージェントが、会話で決めた前提や規則を知らない}
  - {type: goal, text: サブエージェントにも、日本語で報告させたい}
prerequisites: [writing-subagents]
related: [subagent-isolation, hooks-basics, hook-recipes#subagent-only, keep-replies-in-japanese, replies-in-english, how-skills-load, what-to-put-in-claude-md, research-in-subagents]
tracks: [subagents]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
