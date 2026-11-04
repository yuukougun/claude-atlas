---
id: differential-testing
title: 答えの分かる遅い解と比べる（差分テスト・オラクル）
nav_title: 答えの分かる遅い解と比べる
aliases: [オラクル, ストレステスト, 参照実装との比較, 愚直解との比較]
type: recipe
field: eval
chapter: 検証器を作る
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 遅くても明らかに正しい解（愚直解・旧実装・公式の道具）と突き合わせる差分テストを、Claude に作らせて回させられる。正解の側を本解に合わせて直させない。
signs:
  - {type: goal, text: 正解の分かる遅い実装と突き合わせて、正しさを確かめたい}
  - {type: symptom, text: テストでは見つからない間違いが、本番の入力で出る}
  - {type: situation, text: 古い実装を新しく書き直している}
prerequisites: [verifier-three-conditions]
related: [pitfalls-of-ai-written-tests, test-the-verifier, shrink-failing-inputs, property-based-tests, bisect-regressions, refactor-and-migrate, performance-tuning, fix-a-bug, build-test-harness, search-code-checklist]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 手順, anchor: steps}
  - {title: 正解の側を守る, anchor: protect-the-oracle}
stage: stub
updated: 2026-11-04
---

## 手順 {#steps}

## 正解の側を守る {#protect-the-oracle}
