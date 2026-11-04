---
id: cloud-sessions-and-teleport
title: クラウドセッションと teleport
aliases: [claude.ai/code, --cloud, /teleport, Claude Code on the Web, --remote]
type: feature
field: cli
chapter: ほかの面と離席
order: 160
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [握る, 縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: 作業をクラウドのセッションで走らせて手元を閉じても続けさせ、終わったら teleport で手元の端末に取り込む。クラウドは手元の設定の一部を読まないので、計画と縛りをリポジトリに置いてから送る。
signs:
  - {type: goal, text: 手元で計画した作業をクラウドに渡し、PC を閉じても進めさせたい}
  - {type: situation, text: クラウドで動かしたセッションを、手元で続けたい}
prerequisites: [when-to-plan, where-it-runs]
related: [control-from-phone, resume-and-branch, agent-view-and-background, choosing-parallel-modes, cloud-schedules, protecting-secrets, checking-unattended-runs, share-team-settings]
tracks: [cloud-sessions]
outdated_advice: [code-on-the-web-remote]
sources: []
volatility: 高
sections:
  - {title: クラウドに送ってよい作業, anchor: what-to-send}
  - {title: 手元の設定との違い, anchor: settings}
  - {title: teleport で取り込む, anchor: teleport}
stage: stub
updated: 2026-11-04
---

## クラウドに送ってよい作業 {#what-to-send}

## 手元の設定との違い {#settings}

## teleport で取り込む {#teleport}
