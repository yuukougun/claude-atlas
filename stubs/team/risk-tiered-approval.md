---
id: risk-tiered-approval
title: リスク段階別の承認（AI の承認を人の承認に数えない）
nav_title: リスク段階別の承認
aliases: [リスク別の承認, 承認の段階, AI のお墨付き]
type: concept
field: team
chapter: レビューと判断
order: 60
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [チーム, 開発]
summary: 変更をリスクの段に分け、段ごとに人の承認の数を決められる。AI の承認は人の承認に数えず、危ない場所は常に人が見る。
signs:
  - {type: goal, text: AI が書いた変更の承認の仕方を、危なさで分けたい}
  - {type: situation, text: AI のレビューが通ったら、人の承認は要らないか迷っている}
  - {type: symptom, text: AI のレビューが通った PR を、人がよく見ずに承認している}
prerequisites: [independent-review, agreement-is-not-evidence]
related: [review-bottlenecks, automated-pr-review, separate-roles, protected-paths, freeze-eval-assets, diffs-humans-must-read, ai-usage-guidelines, create-and-review-prs, github-actions-with-claude]
sources: []
volatility: 中
sections:
  - {title: 三つの段と承認の数, anchor: three-tiers}
  - {title: AI の承認を数えない, anchor: ai-approval-doesnt-count}
  - {title: 段を決めるのは中身、常に人が見る場所, anchor: always-human}
stage: stub
updated: 2026-11-04
---

## 三つの段と承認の数 {#three-tiers}

## AI の承認を数えない {#ai-approval-doesnt-count}

## 段を決めるのは中身、常に人が見る場所 {#always-human}
