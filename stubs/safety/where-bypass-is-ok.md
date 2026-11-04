---
id: where-bypass-is-ok
title: bypassPermissions と無人の実行はどこで動かすか
aliases: [--dangerously-skip-permissions, YOLO モード, 全許可モード, 使い捨ての環境, bypassPermissions はどこで使ってよいか, devcontainer, Docker, コンテナ]
type: concept
field: safety
chapter: 既定と承認
order: 30
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: 確認をすべて外すモードや無人の実行を、隔離した使い捨ての環境だけで動かす理由と、その環境の条件が分かる。確認を減らすだけなら、先に auto モードとサンドボックスを使う。
signs:
  - {type: goal, text: --dangerously-skip-permissions で、確認なしに走らせたい}
  - {type: goal, text: コンテナの中で Claude Code を無人で動かしたい}
  - {type: situation, text: 夜間や CI で、人が見ていない間に Claude を動かしている}
prerequisites: [what-auto-mode-stops, sandboxing]
related: [headless-basics, five-questions-before-delegating, default-safety-settings#by-stage, permission-modes-overview, managed-settings-enforcement, protected-paths, before-opening-unknown-repos, github-actions-with-claude, cloud-sessions-and-teleport, checking-unattended-runs, destructive-commands, cloud-schedules]
tracks: [permission-modes, headless, cloud-sessions]
outdated_advice: [yolo-skip-permissions]
sources: []
volatility: 中
sections:
  - {title: なぜ隔離した環境だけか, anchor: why-isolate}
  - {title: 使い捨ての環境の条件, anchor: requirements}
  - {title: 書き込みを作業ディレクトリに閉じても代わりにならない, anchor: not-a-substitute}
stage: stub
updated: 2026-11-04
---

## なぜ隔離した環境だけか {#why-isolate}

## 使い捨ての環境の条件 {#requirements}

## 書き込みを作業ディレクトリに閉じても代わりにならない {#not-a-substitute}
