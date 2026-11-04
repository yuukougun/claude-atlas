---
id: independent-review
title: 書いた本人ではない者にレビューさせる
aliases: [独立したレビュー, 新しいセッションでレビュー, Writer/Reviewer パターン, /code-review, /security-review]
type: concept
field: verify
chapter: レビューで確かめる
order: 110
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [開発, 文章, チーム]
summary: 変更を生んだ推論を見ていない者（新しいセッション・サブエージェント・別の人）にレビューさせる理由と分け方が分かる。AI の承認は人の承認に数えない。
signs:
  - {type: situation, text: 自分の目で全部レビューする時間がない}
  - {type: symptom, text: Claude に自分の作業を確認させると、いつも問題なしと言う}
  - {type: goal, text: 書いた本人ではない目でレビューさせたい}
  - {type: goal, text: AI が書いたコードに脆弱性がないか見させたい}
prerequisites: [verification-ladder, subagent-isolation]
related: [instructing-reviewers, agreement-is-not-evidence, diffs-humans-must-read, second-opinion-from-another-model, own-generated-code, writing-subagents, risk-tiered-approval, separate-roles, sycophancy, ask-without-sycophancy, automated-pr-review, create-and-review-prs, review-bottlenecks]
tracks: [code-review, subagents, security-review]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 誰にレビューさせるか, anchor: who}
  - {title: 推論を見せない, anchor: hide-reasoning}
  - {title: AI の承認を人の承認に数えない, anchor: ai-approval}
  - {title: セキュリティのレビューを頼む（脆弱性を探させる）, anchor: security-review}
stage: stub
updated: 2026-11-04
---

## 誰にレビューさせるか {#who}

## 推論を見せない {#hide-reasoning}

## AI の承認を人の承認に数えない {#ai-approval}

## セキュリティのレビューを頼む（脆弱性を探させる） {#security-review}
