---
id: agent-view-and-background
title: agent view と背景セッション
aliases: [claude agents, background sessions, claude --bg, /background, cross-session messaging]
type: feature
field: delegate
chapter: 並べる
order: 120
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: 見張らなくてよい独立した作業を背景のセッションに投入し、一覧で状態を見て、要るときだけ返事をできる。セッションごとに利用枠を使うので、同時に動かす数を決めてから投入する。
signs:
  - {type: goal, text: いくつかの作業を投げておいて、後でまとめて確かめたい}
  - {type: symptom, text: 背景で動かしたセッションがどうなったか分からない}
prerequisites: [choosing-parallel-modes, what-auto-mode-stops]
related: [parallel-with-worktrees, humans-set-the-parallel-limit, pairing-and-delegating, progress-logs-for-long-jobs, checking-unattended-runs, completion-notifications, control-from-phone, cloud-sessions-and-teleport, parallel-and-loop-costs]
tracks: [agent-view, cross-session-messaging]
outdated_advice: [tmux-agent-orgs]
sources: []
volatility: 高
sections:
  - {title: 向く作業と向かない作業, anchor: what-fits}
  - {title: ほかのセッションに知らせる（cross-session messaging）, anchor: cross-session-messaging}
stage: stub
updated: 2026-11-04
---

## 向く作業と向かない作業 {#what-fits}

## ほかのセッションに知らせる（cross-session messaging） {#cross-session-messaging}
