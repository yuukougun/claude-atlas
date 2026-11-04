---
id: destructive-commands
title: 消されたくないもの（破壊的コマンド）
aliases: [rm -rf, git reset --hard, force push, 破壊的な操作, 取り返しのつかない操作]
type: concept
field: safety
chapter: 秘密と壊す操作
order: 150
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 握る]
prevents: [境界がない, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 取り返しのつかない削除や書き換えが起きる経路と、巻き戻しで戻らないものが分かり、消されたくないものを権限ルール・サンドボックス・バックアップで守れる。
signs:
  - {type: goal, text: 本番のデータベースやリモートのブランチに触らせたくない}
  - {type: goal, text: 取り返しのつかない操作の前には、必ず止めてほしい}
prerequisites: [checkpoints-and-rewind, permission-rules]
related: [deleted-something-important, protected-paths, sandboxing, what-auto-mode-stops, block-with-exit-2, hook-recipes, working-with-git, where-bypass-is-ok]
tracks: [checkpoints, auto-mode, sandbox, permissions]
sources: []
volatility: 中
sections:
  - {title: 消える経路, anchor: how-it-happens}
  - {title: 巻き戻しで戻らないもの, anchor: not-recoverable}
  - {title: 確認を求めさせる頼み方と、鍵, anchor: guard}
stage: stub
updated: 2026-11-04
---

## 消える経路 {#how-it-happens}

## 巻き戻しで戻らないもの {#not-recoverable}

## 確認を求めさせる頼み方と、鍵 {#guard}
