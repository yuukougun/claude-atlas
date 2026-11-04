---
id: automated-pr-review
title: 自動 PR レビュー（Code Review・/ultrareview）
nav_title: 自動 PR レビュー
aliases: [AI による PR レビュー, 自動レビュー]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 220
level: 仕組みにする
priority: 任意
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [開発, チーム]
summary: PR ごとに AI のレビューを自動で付け、人が見る前に指摘を出させられる。AI のレビューは人の承認の代わりに数えず、指摘の採否と承認は人が決める。
signs:
  - {type: goal, text: PR ごとに AI のレビューを自動で付けたい}
  - {type: situation, text: 人のレビューの代わりに、AI のレビューで済ませたくなっている}
prerequisites: [independent-review]
related: [risk-tiered-approval, instructing-reviewers, review-bottlenecks, grow-review-checklists, separate-roles#against-sycophancy, agreement-is-not-evidence, second-opinion-from-another-model, github-actions-with-claude, create-and-review-prs, parallel-and-loop-costs]
tracks: [github-actions, managed-code-review, ultrareview]
sources: []
volatility: 高
stage: stub
updated: 2026-11-04
---
