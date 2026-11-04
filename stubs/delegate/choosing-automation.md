---
id: choosing-automation
title: 自動化の選び方（定期タスク・非対話モード・SDK）
aliases: [自動化の比較, cron で動かす]
type: comparison
field: delegate
chapter: 定期と無人の実行
order: 160
level: 回す
priority: 推奨
surfaces: [claude-code, app, api]
principle: [縛る, 確かめる]
prevents: [合っていない, 境界がない]
pitfalls: []
scenes: [開発]
summary: 決まった時刻・イベント・スクリプトから Claude を動かす方法を、どこで動くか・何に触れられるか・どの課金になるかで選べる。
signs:
  - {type: goal, text: 決まった時刻やイベントで、Claude を自動で動かしたい}
  - {type: symptom, text: 自分の作業を自動で回したいが、どの仕組みで動かすか決められない}
prerequisites: [headless-basics, loop-and-scheduling]
related: [cloud-schedules, github-actions-with-claude, bare-mode, tasks-and-schedules-in-the-app, sdk-comparison, agent-sdk-basics, where-it-runs, check-billing-path, checking-unattended-runs, default-safety-settings]
tracks: [loop, scheduled-tasks, headless, github-actions, agent-sdk, managed-agents]
outdated_advice: [routines-name]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
