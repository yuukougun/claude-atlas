---
id: verification-ladder
title: 検証の階段
aliases: [確かめ方の段階, 検証の強さ, Give Claude a check to run, 「念のため確認して」は効くか, double-check して]
type: concept
field: verify
chapter: 完了を確かめる
order: 30
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 完了の確かめを、依頼に書く・判定役に見張らせる・フックで終了を止める・書いていない者に確かめさせる、の段から任せる幅に応じて選べる。「確かめて」と書き足すより、手段を渡すほうが効く。
signs:
  - {type: goal, text: テストが通るまで終わらせたくない}
  - {type: symptom, text: 「確かめて」と書いても、確かめずに終わる}
  - {type: goal, text: 任せる範囲に合わせて、確かめ方の強さを選びたい}
  - {type: situation, text: 長い作業を任せて、途中は見ないつもりでいる}
prerequisites: [evidence-not-reports, request-vs-lock]
related: [goal-until-done, stop-hooks, independent-review, protect-tests, verifier-defines-problem, model-quirks, when-to-lock, five-questions-before-delegating, claims-done-but-isnt, checking-unattended-runs, visual-checks, four-principles]
tracks: [goal, hooks, code-review]
outdated_advice: [add-double-check]
sources: []
volatility: 中
sections:
  - {title: 四つの段, anchor: four-steps}
  - {title: 「念のため確認して」と書き足すより、確かめる手段を渡す, anchor: verbal-checks}
  - {title: 任せる幅に合わせて段を選ぶ, anchor: choose-step}
stage: stub
updated: 2026-11-04
---

## 四つの段 {#four-steps}

## 「念のため確認して」と書き足すより、確かめる手段を渡す {#verbal-checks}

## 任せる幅に合わせて段を選ぶ {#choose-step}
