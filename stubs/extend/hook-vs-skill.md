---
id: hook-vs-skill
title: フックとスキルの違い
aliases: [hook と skill の使い分け, hooks と skills]
type: comparison
field: extend
chapter: スキル
order: 140
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [縛る, 見せる]
prevents: [縛っていない]
pitfalls: []
scenes: [開発]
summary: 決まった手順をスキルにするか、フックで必ず走らせるかを選べる。スキルは Claude が判断して使うお願いで、フックは決まったときに必ず動く鍵である。
signs:
  - {type: symptom, text: スキルに書いた手順の、必ずやってほしい一歩を飛ばされる}
  - {type: goal, text: 手順として読ませるか、自動で必ず走らせるかを決めたい}
prerequisites: [request-vs-lock, how-skills-load]
related: [hooks-basics, when-to-lock, request-lock-table, hook-recipes, writing-skills, manual-only-skills, extensions-at-a-glance, textlint-hook, less-ai-sounding-japanese#lint-vs-judgment]
tracks: [hooks, skills]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
