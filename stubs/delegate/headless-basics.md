---
id: headless-basics
title: 非対話モード（claude -p）の基本
aliases: [headless, ヘッドレス, non-interactive mode, print モード]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 190
level: 回す
priority: 必須
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [境界がない, 確かめていない]
pitfalls: []
scenes: [開発]
summary: claude -p でスクリプトや CI から Claude Code を動かし、結果を決まった形式で受け取れる。無人では確認に答える人がいないので、許す道具と止まる上限を明示して渡す。
signs:
  - {type: goal, text: スクリプトや CI から Claude Code を使いたい}
  - {type: symptom, text: スクリプトから動かすと、ファイルの編集やコマンドをせずに終わる}
  - {type: symptom, text: CI では成功と出たのに、実際は何もしていなかった}
  - {type: symptom, text: サブスクリプションで使っているつもりが、API の請求が来た}
prerequisites: [five-questions-before-delegating]
related: [permission-rules, bare-mode, checking-unattended-runs, what-auto-mode-stops, where-bypass-is-ok, sandboxing, before-opening-unknown-repos, protecting-secrets, check-billing-path, what-uses-up-limits#find-what-uses-it, structured-outputs-basics, batch-and-p-loops, github-actions-with-claude, choosing-automation, sdk-comparison, agent-sdk-basics]
tracks: [headless, permission-modes]
outdated_advice: [yolo-skip-permissions]
sources: []
volatility: 中
sections:
  - {title: 出力の形式と終了コード, anchor: output-and-exit-codes}
  - {title: 許可と権限モード, anchor: permissions}
  - {title: 止まる上限（ターンと費用）, anchor: limits}
  - {title: 知らないフォルダで動かすとき, anchor: untrusted-folders}
  - {title: 課金の経路（API キーがあるとき）, anchor: billing-path}
stage: stub
updated: 2026-11-04
---

## 出力の形式と終了コード {#output-and-exit-codes}

## 許可と権限モード {#permissions}

## 止まる上限（ターンと費用） {#limits}

## 知らないフォルダで動かすとき {#untrusted-folders}

## 課金の経路（API キーがあるとき） {#billing-path}
