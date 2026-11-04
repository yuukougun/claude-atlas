---
id: cloud-schedules
title: クラウドの定期タスク
aliases: [routines, cloud scheduled tasks, /schedule, ルーティン]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 180
level: 回す
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [境界がない, 確かめていない]
pitfalls: []
scenes: [開発, 調べもの]
summary: 手元の PC を閉じていても、決まった時刻や GitHub のイベントでクラウドの Claude Code に作業させられる。接続先と権限を最小にし、成功の定義と結果の確かめ方を先に決める。
signs:
  - {type: goal, text: 決まった時刻の作業を、手元の PC なしで走らせたい}
  - {type: goal, text: PR が開いたら、自動で Claude に作業させたい}
prerequisites: [loop-and-scheduling, lethal-trifecta]
related: [checking-unattended-runs, where-bypass-is-ok, prompt-injection-in-practice, vetting-extensions, choosing-automation, github-actions-with-claude, cloud-sessions-and-teleport, where-it-runs, connectors-in-the-app, tasks-and-schedules-in-the-app, parallel-and-loop-costs]
tracks: [scheduled-tasks, cloud-sessions]
outdated_advice: [routines-name]
sources: []
volatility: 高
sections:
  - {title: きっかけ（時刻・API・GitHub のイベント）, anchor: triggers}
  - {title: 接続先と権限を最小にする, anchor: least-privilege}
stage: stub
updated: 2026-11-04
---

## きっかけ（時刻・API・GitHub のイベント） {#triggers}

## 接続先と権限を最小にする {#least-privilege}
