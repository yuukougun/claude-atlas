---
id: postmortems
title: 失敗を仕組みに戻す（ポストモーテム）
aliases: [postmortem, 再発防止, ブレームレスな振り返り]
type: judgment
field: judgment
chapter: 振り返りと再発防止
order: 110
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 握る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発, チーム]
summary: AI と組んだ作業の失敗を、誰の誤りかではなくどの仕組みの隙間が許したかで書き、再発防止を CLAUDE.md・フック・レビューの観点のどこに入れるかを決められる。
signs:
  - {type: situation, text: AI に任せた作業で事故が起きたので、再発を防ぎたい}
  - {type: symptom, text: 注意したのに、同じ種類の失敗が別の作業でまた起きた}
prerequisites: [when-to-lock]
related: [retros-without-ai-verdicts, hook-recipes, what-to-put-in-claude-md, grow-review-checklists, keep-failure-lessons, recover-lost-work, record-decisions, deleted-something-important, instructions-ignored, request-lock-table, decide-when-to-quit]
tracks: [claude-md, hooks]
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 誰がではなく、どの隙間が, anchor: which-gap}
  - {title: 人と AI の操作の時間線, anchor: timeline}
  - {title: 再発防止をどこに入れるか, anchor: where-to-put-fixes}
  - {title: プレモーテムの扱い, anchor: premortem}
stage: stub
updated: 2026-11-04
---

## 誰がではなく、どの隙間が {#which-gap}

## 人と AI の操作の時間線 {#timeline}

## 再発防止をどこに入れるか {#where-to-put-fixes}

## プレモーテムの扱い {#premortem}
