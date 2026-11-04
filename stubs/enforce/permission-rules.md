---
id: permission-rules
title: 権限ルール（allow・ask・deny）
aliases: [permissions, permission rules, 許可ルール, 確認ルール, 拒否ルール, allow ルール, ask ルール, deny ルール, /permissions]
type: feature
field: enforce
chapter: 権限と封じ込め
order: 40
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない, 境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: 許可・確認・拒否のルールで、Claude が使える道具とファイルを決められる。拒否は先に評価されるが、当たらないパスのルールと、効かない子プロセスがある。
signs:
  - {type: goal, text: '`.env` や migrations を絶対に触らせたくない'}
  - {type: goal, text: よく使う安全なコマンドは、毎回確認させたくない}
  - {type: symptom, text: 拒否のルールに書いたのに、下のフォルダにある同じ名前のファイルは読まれた}
prerequisites: [permission-modes-overview]
related: [what-auto-mode-stops, sandboxing, protected-paths, protecting-secrets, when-to-lock, settings-layers, freeze-eval-assets, managed-settings-enforcement, lock-side-effects, before-opening-unknown-repos, share-team-settings, hook-vs-skill]
tracks: [permissions, settings]
sources: []
volatility: 中
sections:
  - {title: 評価の順番（deny → ask → allow）, anchor: evaluation-order}
  - {title: パスの書き方と、何にも当たらないルール, anchor: path-rules}
  - {title: 子プロセスには効かない, anchor: child-processes}
  - {title: 信頼の前に効くもの・後に効くもの, anchor: workspace-trust}
stage: stub
updated: 2026-11-04
---

## 評価の順番（deny → ask → allow） {#evaluation-order}

## パスの書き方と、何にも当たらないルール {#path-rules}

## 子プロセスには効かない {#child-processes}

## 信頼の前に効くもの・後に効くもの {#workspace-trust}
