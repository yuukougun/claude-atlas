---
id: loop-and-scheduling
title: /loop と定期実行の方式
aliases: [Desktop scheduled tasks, 定期タスク, Desktop の定期タスク, 予定のタスク]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 170
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, 調べもの]
summary: 開いているセッションの中で依頼を繰り返す /loop と、手元やクラウドで決まった時刻に走らせる方式を使い分けられる。途中で質問できないので、成功の定義と結果の置き場所を依頼に書く。
signs:
  - {type: goal, text: 毎朝決まった調査をさせたい}
  - {type: goal, text: 数分おきにビルドやデプロイの状態を見張らせたい}
prerequisites: [five-questions-before-delegating, what-auto-mode-stops]
related: [cloud-schedules, tasks-and-schedules-in-the-app, choosing-automation, goal-until-done, checking-unattended-runs, completion-notifications, parallel-and-loop-costs, headless-basics]
tracks: [loop, scheduled-tasks]
sources: []
volatility: 中
sections:
  - {title: セッションの中で繰り返す（/loop）, anchor: loop}
  - {title: どこで走らせるか（セッション・手元・クラウド）, anchor: where-to-run}
  - {title: 成功の定義と結果の置き場所, anchor: success-and-results}
stage: stub
updated: 2026-11-04
---

## セッションの中で繰り返す（/loop） {#loop}

## どこで走らせるか（セッション・手元・クラウド） {#where-to-run}

## 成功の定義と結果の置き場所 {#success-and-results}
