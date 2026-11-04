---
id: using-auto-memory
title: 自動メモリ
aliases: [auto memory, MEMORY.md, /memory, Claude が書き溜める記録]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 70
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [散らかっている, 見えていない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: Claude が自分で書き溜める記録を確かめ、直し、止められる。人が書く CLAUDE.md との分担と、誤った結論が残って後の作業を汚さないための見直し方が分かる。
signs:
  - {type: goal, text: Claude Code が書き溜めた記録の場所を知り、見て直したい}
  - {type: symptom, text: 一度の誤った結論を覚えられ、後の作業でも前提にされる}
prerequisites: [what-to-put-in-claude-md]
related: [how-memory-works, unexpected-memories, experiment-log, over-reliance, claude-md-length, what-survives-compaction, keep-failure-lessons, progress-files, claude-md-loading-order, pruning-extensions]
tracks: [auto-memory]
sources: []
volatility: 中
sections:
  - {title: 誤った記録の見直し, anchor: review}
stage: stub
updated: 2026-11-04
---

## 誤った記録の見直し {#review}
