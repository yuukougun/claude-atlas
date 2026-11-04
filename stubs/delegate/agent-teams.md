---
id: agent-teams
title: エージェントチーム（複数の Claude に分担させる）
nav_title: エージェントチーム
aliases: [agent teams, teammate]
type: feature
field: delegate
chapter: 並べる
order: 150
level: 回す
priority: 任意
surfaces: [claude-code]
principle: [握る]
prevents: [合っていない]
pitfalls: []
scenes: [開発]
summary: リードの Claude にチームメイトへの割り当てと調整を任せ、互いに連絡しながら並行して進めさせられる。チームメイトの数だけトークンを使い、同じファイルを触ると衝突するので、小さく焦点を絞って試す。
signs:
  - {type: goal, text: 複数の Claude に分担させ、互いにやりとりさせたい}
  - {type: symptom, text: 複数の Claude に分担させたら、同じファイルを取り合った}
prerequisites: [choosing-parallel-modes, what-auto-mode-stops]
related: [dynamic-workflows, agent-view-and-background, subagent-isolation, parallel-and-loop-costs, permission-modes-overview, humans-set-the-parallel-limit, fix-a-bug]
tracks: [agent-teams]
outdated_advice: [tmux-agent-orgs]
sources: []
volatility: 高
stage: stub
updated: 2026-11-04
---
