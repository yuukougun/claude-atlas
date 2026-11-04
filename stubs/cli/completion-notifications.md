---
id: completion-notifications
title: 終わったら知らせてもらう
aliases: [通知, Notification hook, 完了通知, 入力待ちの通知]
type: feature
field: cli
chapter: ほかの面と離席
order: 180
level: 任せる
priority: 任意
surfaces: [claude-code]
principle: [握る]
prevents: []
pitfalls: []
scenes: [開発]
summary: 作業の終わりや承認待ちをフックなどで通知させ、画面に張りつかずに任せる。知らせが多すぎると作業が細切れになるので、確認するタイミングを自分で決める流儀もある。
signs:
  - {type: goal, text: 任せている間に別の作業をしたいので、終わったら知らせてほしい}
  - {type: symptom, text: 承認待ちで止まっていたことに、後から気づく}
prerequisites: []
related: [hook-recipes#notify, hooks-basics, control-from-phone, agent-view-and-background, humans-set-the-parallel-limit]
tracks: [hooks]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 知らせるか、時刻を決めて見るか, anchor: when-to-notify}
  - {title: 知らせる手段（端末の設定とフック）, anchor: channels}
stage: stub
updated: 2026-11-04
---

## 知らせるか、時刻を決めて見るか {#when-to-notify}

## 知らせる手段（端末の設定とフック） {#channels}
