---
id: refactor-and-migrate
title: リファクタリングと大規模な移行
aliases: [コードの移行, ライブラリの置き換え, 大規模な書き換え, 非推奨 API の置き換え, migration]
type: recipe
field: recipes
chapter: 作る・変える
order: 70
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
scenes: [開発]
summary: 挙動を変えないリファクタリングや大規模な移行を、小さく確かめられる単位に分けて任せる。挙動が保たれたことは、変更前後のテストの結果と出力を比べて確かめる。
signs:
  - {type: goal, text: 古いライブラリや API からの移行を、たくさんのファイルにわたって進めたい}
  - {type: goal, text: 動きを変えずにコードを整理したい}
  - {type: symptom, text: 大きな変更を一度に頼んだら、どこで壊れたのか分からなくなった}
prerequisites: [working-with-git, differential-testing]
related: [verification-ladder, protect-tests, freeze-eval-assets, rewrote-tests-to-pass, pitfalls-of-ai-written-tests, goal-until-done, dynamic-workflows, batch-and-p-loops, parallel-with-worktrees, checkpoints-and-rewind, progress-files, diffs-humans-must-read, create-and-review-prs, performance-tuning, spec-first]
tracks: [goal, workflows, worktrees]
outdated_advice: [keep-going-dont-be-lazy, ralph-loops]
sources: []
volatility: 中
sections:
  - {title: 小さく分けて一つずつ確かめる, anchor: small-steps}
  - {title: 挙動が変わっていないことを確かめる, anchor: behavior-preserved}
  - {title: 多数のファイルに同じ変更を流す, anchor: bulk-changes, level: 回す}
  - {title: /goal で回すときの停止条件, anchor: goal-stop-conditions, level: 仕組みにする}
stage: stub
updated: 2026-11-04
---

## 小さく分けて一つずつ確かめる {#small-steps}

## 挙動が変わっていないことを確かめる {#behavior-preserved}

## 多数のファイルに同じ変更を流す {#bulk-changes}

## /goal で回すときの停止条件 {#goal-stop-conditions}
