---
id: separate-roles
title: 役割を分ける（書く人・承認する人・疑う人）
nav_title: 役割を分ける
aliases: [役割分担, 評価担当, 批評担当, チームで迎合と過信を防ぐ]
type: concept
field: team
chapter: レビューと判断
order: 70
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: [同意を根拠にする, やめられない, 預けすぎる]
scenes: [チーム, 開発, コンテスト]
summary: AI と進めるチームの役割を、書く人・承認する人・疑う人に分け、評価と撤退の判断を実装する人から離せる。AI の同意を根拠に数えない決まりも、持ち回りの疑う役で守る。
signs:
  - {type: situation, text: AI と進めるチームで、誰が何を決めるかを決める}
  - {type: symptom, text: 実装した人が自分で評価して、撤退の判断もしている}
  - {type: symptom, text: チームの議論で「AI も賛成した」が決め手になっている}
prerequisites: [independent-review, decide-when-to-quit]
related: [risk-tiered-approval, agreement-is-not-evidence, over-reliance, review-bottlenecks, ask-without-sycophancy, caves-when-pushed, retros-without-ai-verdicts, lockbox-and-holdout, verifier-three-conditions, what-not-to-delegate, ideate-independently, record-decisions, long-team-competitions]
sources: []
volatility: 低
sections:
  - {title: 迎合と過信に備える（AI の同意を根拠に数えない）, anchor: against-sycophancy}
stage: stub
updated: 2026-11-04
---

## 迎合と過信に備える（AI の同意を根拠に数えない） {#against-sycophancy}
