---
id: protect-tests
title: テストを守る（改ざんを防ぐ）
aliases: [テストの改ざんを防ぐ, テストを書き換えさせない, 評価資産を守る, reward hacking への備え]
type: concept
field: verify
chapter: テストで確かめる
order: 100
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: Claude がテストや採点を書き換えて通すのを、依頼・差分のレビュー・ファイルの鍵・見せないデータの層で防げる。テストは正しさを確かめるもので、解を決めるものではない。
signs:
  - {type: goal, text: テストや採点のスクリプトを、Claude に書き換えさせたくない}
  - {type: goal, text: テストを書き換えずに直すよう、依頼の段階で伝えたい}
prerequisites: [verification-ladder, reward-hacking]
related: [rewrote-tests-to-pass, freeze-eval-assets, verifier-three-conditions, lockbox-and-holdout, permission-rules, hook-recipes, block-with-exit-2, sandboxing, permission-to-stop, diffs-humans-must-read, pitfalls-of-ai-written-tests, tests-first, request-lock-table]
tracks: [permissions, hooks, sandbox]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: なぜテストが書き換えられるか, anchor: why}
  - {title: 守りの層, anchor: layers}
  - {title: 依頼に書くこと, anchor: in-the-request}
stage: stub
updated: 2026-11-04
---

## なぜテストが書き換えられるか {#why}

## 守りの層 {#layers}

## 依頼に書くこと {#in-the-request}
