---
id: going-in-circles
title: 同じ失敗を繰り返す（堂々巡り）
nav_title: 同じ失敗を繰り返す
aliases: [堂々巡り, 同じ修正の失敗, going in circles, 直してもまた壊れる]
type: symptom
field: symptoms
chapter: 会話と文脈
order: 140
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 散らかっている, 確かめていない]
pitfalls: [やめられない]
scenes: [開発]
summary: 同じ失敗を何度も繰り返す原因を、会話に残った失敗の跡から切り分け、訂正を重ねるか、巻き戻すか、学んだことを書いて新しく始めるかを決める。
signs:
  - {type: symptom, text: 同じバグの修正を何度も失敗する}
  - {type: symptom, text: 直してと言うたびに同じ間違いが戻ってくる}
  - {type: symptom, text: 訂正しても別の形で同じ誤りが出る}
wave: 1
prerequisites: [context-rot]
related: [checkpoints-and-rewind, tidy-the-desk, build-on-results, let-claude-ask, stuck-in-a-check-loop, wont-rethink-approach, insists-on-mistakes, forgets-in-long-chats, six-causes]
routes:
  - {cause: 見えていない, to: [keep-failure-lessons, handoff-documents]}
  - {cause: 散らかっている, to: [rewind-dont-correct, when-to-start-fresh, fix-a-bug#when-stuck]}
  - {cause: 確かめていない, to: [fix-a-bug#reproduce-and-define-done, define-done]}
  - {cause: やめられない, to: [decide-when-to-quit]}
tracks: [checkpoints, clear]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
