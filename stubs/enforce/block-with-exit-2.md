---
id: block-with-exit-2
title: フックで止めて理由を返す（exit 2 と JSON）
nav_title: フックで止めて理由を返す
aliases: [exit 2 でブロックする, permissionDecision, PreToolUse でブロックする, フックで拒否する]
type: feature
field: enforce
chapter: フック
order: 100
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発]
summary: PreToolUse のフックで操作を止め、理由と代わりの手段を Claude に返せる。exit 2 と JSON の返し方の違いと、止めた後に回り込ませない書き方が分かる。
signs:
  - {type: goal, text: 特定のコマンドを、理由を伝えて止めたい}
  - {type: goal, text: '`.env` や migrations を絶対に触らせたくない'}
  - {type: symptom, text: フックで止めても、Claude が理由を分からずに同じ操作を繰り返す}
prerequisites: [hooks-basics]
related: [writing-safe-hooks, hook-recipes, lock-side-effects, permission-rules, stop-hooks, protecting-secrets, destructive-commands]
tracks: [hooks]
sources: []
volatility: 中
sections:
  - {title: exit 2 と JSON の違い, anchor: exit-2-vs-json}
  - {title: 理由と代わりの手段の書き方, anchor: reason}
  - {title: 権限ルールとの順番, anchor: precedence}
stage: stub
updated: 2026-11-04
---

## exit 2 と JSON の違い {#exit-2-vs-json}

## 理由と代わりの手段の書き方 {#reason}

## 権限ルールとの順番 {#precedence}
