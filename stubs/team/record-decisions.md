---
id: record-decisions
title: 決定を文書に残す（ADR と週次アップデート）
nav_title: 決定を文書に残す
aliases: [ADR, Architecture Decision Record, 週次アップデート]
type: recipe
field: team
chapter: レビューと判断
order: 100
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [見せる, 握る]
prevents: [見えていない]
pitfalls: []
scenes: [チーム, 開発]
summary: 決めたことと理由を ADR に残し、週ごとに決めたこと・AI に任せたこと・見てほしい点を書面で共有できる。新しい人が文書だけで作業を始められるかで、書けているかを確かめる。
signs:
  - {type: symptom, text: なぜそう決めたかが、後から分からない}
  - {type: goal, text: AI に任せたことと決めたことを、チームに書面で伝えたい}
prerequisites: [handoff-documents]
related: [keep-failure-lessons, postmortems, experiment-log, disclosure-and-provenance, what-to-put-in-claude-md, agents-md, separate-roles, rolling-out-to-teams, compare-hypotheses-in-parallel]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
