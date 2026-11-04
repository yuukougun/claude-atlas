---
id: parallel-with-worktrees
title: git worktree で並列にする
aliases: [claude -w, --worktree, .worktreeinclude, 並列開発]
type: feature
field: delegate
chapter: 並べる
order: 100
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [散らかっている]
pitfalls: []
scenes: [開発]
summary: git worktree で作業ごとに別のチェックアウトを作り、複数のセッションが互いのファイルを上書きせずに並行して進められる。依存の導入や秘密のファイルの写し方は worktree ごとに決める。
signs:
  - {type: goal, text: 同じリポジトリで、複数のセッションを同時に動かしたい}
  - {type: symptom, text: 並列のセッションが、互いのファイルを書き換えてしまう}
prerequisites: [working-with-git]
related: [choosing-parallel-modes, humans-set-the-parallel-limit, compare-hypotheses-in-parallel, agent-view-and-background, batch-and-p-loops, protecting-secrets, sandboxing, checkpoints-and-rewind, resume-and-branch, writing-subagents]
tracks: [worktrees]
sources: []
volatility: 中
sections:
  - {title: worktree ごとの準備（依存・秘密・データベース）, anchor: per-worktree-setup}
  - {title: 片付けと残すもの, anchor: cleanup}
stage: stub
updated: 2026-11-04
---

## worktree ごとの準備（依存・秘密・データベース） {#per-worktree-setup}

## 片付けと残すもの {#cleanup}
