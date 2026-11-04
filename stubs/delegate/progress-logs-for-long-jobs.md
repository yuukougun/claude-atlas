---
id: progress-logs-for-long-jobs
title: 長時間ジョブの進捗ログを設計する
aliases: [進捗ログ, 長時間のジョブの監視]
type: recipe
field: delegate
chapter: 続けさせる
order: 70
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [散らかっている, 確かめていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: 長時間の作業に、要約した指標を定期的に書き出す進捗ログを用意し、Claude にも人にも状況が見えるようにできる。生のログを大量に出すと、Claude 自身が状況を追えなくなる。
signs:
  - {type: goal, text: 長時間の実験やジョブの途中経過を見えるようにしたい}
  - {type: symptom, text: 長いジョブのログが大きすぎて、Claude が状況を追えない}
prerequisites: [progress-files]
related: [checking-unattended-runs, experiment-log, build-observation-tools, goal-until-done, agent-view-and-background, handoff-documents, long-running-agent-context, compact-and-auto-compact, completion-notifications, blames-the-tools]
tracks: [monitor-tool]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
