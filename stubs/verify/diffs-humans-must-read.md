---
id: diffs-humans-must-read
title: 人間が読むべき差分の箇所
aliases: [差分レビューの優先順位, 赤信号の差分, diff の読み方]
type: concept
field: verify
chapter: レビューで確かめる
order: 130
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, チーム]
summary: 差分を全部は読めないとき、人が必ず読む箇所（テストと採点の変更・特例の分岐・例外の握りつぶし・件数の変化など）を見分けられる。
signs:
  - {type: situation, text: 差分が大きすぎて、全部は読めない}
  - {type: situation, text: 自分の目で全部レビューする時間がない}
  - {type: goal, text: 人が必ず目を通すべき変更を見分けたい}
prerequisites: [evidence-not-reports]
related: [independent-review, protect-tests, suspect-too-good-results, own-generated-code, reward-hacking, review-bottlenecks, grow-review-checklists, risk-tiered-approval, create-and-review-prs, working-with-git]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 赤信号の一覧, anchor: red-flags}
  - {title: 要の処理と周辺の読み分け, anchor: core-vs-periphery}
stage: stub
updated: 2026-11-04
---

## 赤信号の一覧 {#red-flags}

## 要の処理と周辺の読み分け {#core-vs-periphery}
