---
id: settings-layers
title: 設定ファイルの階層と優先順位
aliases: [設定ファイルの階層（最小限）, settings.json, settings.local.json, user・project・local・managed, /status, /config]
type: feature
field: cli
chapter: 設定と最初の準備
order: 120
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [縛る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発, チーム]
summary: 設定を、誰に効かせたいかでユーザー・プロジェクト・手元だけ・管理の層に書き分け、効かないときは /status で読み込まれた層を確かめて直せる。同じキーは優先順の高い層が勝つが、権限ルールは層をまたいで合わさる。
signs:
  - {type: symptom, text: settings.json に書いた設定が効いていない}
  - {type: goal, text: 自分だけの設定と、チームで共有する設定を分けたい}
prerequisites: []
related: [permission-rules, share-team-settings, managed-settings-enforcement, permission-modes-overview, isolate-with-safe-mode, output-style-modes, claude-md-loading-order, protecting-secrets, keep-replies-in-japanese#language-setting, commit-and-comment-language#override]
tracks: [settings, managed-settings]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 層と優先順位, anchor: layers}
  - {title: 合わさる設定、上書きされる設定, anchor: merge}
  - {title: 効いているかを確かめる, anchor: verify}
stage: stub
updated: 2026-11-04
---

## 層と優先順位 {#layers}

## 合わさる設定、上書きされる設定 {#merge}

## 効いているかを確かめる {#verify}
