---
id: stop-hooks
title: Stop フックで「終わらせない」
aliases: [Stop hook, SubagentStop, 終わらせないフック, stop_hook_active]
type: feature
field: enforce
chapter: フック
order: 130
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: Stop フックで、確かめる処理が通るまでターンを終えさせない仕組みを作れる。続けて止められる回数には上限があり、止め続けるループを避ける書き方が要る。
signs:
  - {type: goal, text: テストが通るまで終わらせたくない}
  - {type: symptom, text: Stop フックを入れたら、同じ確認を延々と繰り返す}
prerequisites: [block-with-exit-2, verification-ladder]
related: [goal-until-done, claims-done-but-isnt, stuck-in-a-check-loop, define-done, evidence-not-reports, hook-recipes, writing-safe-hooks, keep-replies-in-japanese#stop-hook, test-the-verifier, protect-tests]
tracks: [hooks, goal]
sources: []
volatility: 中
sections:
  - {title: 続けて止められる回数の上限, anchor: block-cap}
  - {title: 止め続けるループを避ける, anchor: avoid-loops}
  - {title: /goal との使い分け, anchor: vs-goal}
stage: stub
updated: 2026-11-04
---

## 続けて止められる回数の上限 {#block-cap}

## 止め続けるループを避ける {#avoid-loops}

## /goal との使い分け {#vs-goal}
