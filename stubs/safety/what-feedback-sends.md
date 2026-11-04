---
id: what-feedback-sends
title: /feedback・トランスクリプトの共有で送られるもの
aliases: [/feedback, /bug, /share, transcript の共有, フィードバックで送られるもの, テレメトリ]
type: feature
field: safety
chapter: データの扱い
order: 50
level: 整える
priority: 推奨
surfaces: [claude-code, app]
principle: [握る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: /feedback やトランスクリプトの共有に応じると、会話とコードが送られて長く残ることを知り、送る前に中身を選べる。/share は共有のリンクを作る機能ではない。
signs:
  - {type: situation, text: 不具合を /feedback で報告しようとしている}
  - {type: situation, text: セッションの評価の後に、トランスクリプトを共有するか聞かれた}
prerequisites: [where-your-data-goes]
related: [protecting-secrets, shared-artifacts-and-files, entrusted-data, default-safety-settings, audit-logs-and-telemetry]
tracks: [feedback]
sources: []
volatility: 中
sections:
  - {title: 送られるものと残る期間, anchor: what-is-sent}
  - {title: /share は共有のリンクではない, anchor: share-is-bug}
  - {title: テレメトリと報告の機能を止める, anchor: telemetry}
stage: stub
updated: 2026-11-04
---

## 送られるものと残る期間 {#what-is-sent}

## /share は共有のリンクではない {#share-is-bug}

## テレメトリと報告の機能を止める {#telemetry}
