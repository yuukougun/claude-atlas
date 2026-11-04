---
id: bare-mode
title: --bare と再現性
aliases: [bare mode, 自動の読み込みを止める]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 200
level: 回す
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 縛る]
prevents: [散らかっている, 境界がない]
pitfalls: []
scenes: [開発]
summary: --bare で CLAUDE.md・フック・MCP などの自動の読み込みを止め、どのマシンでも同じ条件で claude -p を動かせる。手元の設定や、知らないリポジトリのフックが自動の実行に混ざるのを防ぐ。
signs:
  - {type: symptom, text: 手元と CI で、同じ指示なのに結果が違う}
  - {type: symptom, text: 自動の実行に、自分の CLAUDE.md や hooks が混ざる}
prerequisites: [headless-basics]
related: [before-opening-unknown-repos, vetting-extensions, check-billing-path, settings-layers, github-actions-with-claude, batch-and-p-loops, choosing-automation]
tracks: [headless, settings, bare-mode]
sources: []
volatility: 中
sections:
  - {title: 読み込まないもの, anchor: what-is-skipped}
  - {title: 認証が変わる（サブスクリプションで使うとき）, anchor: authentication}
stage: stub
updated: 2026-11-04
---

## 読み込まないもの {#what-is-skipped}

## 認証が変わる（サブスクリプションで使うとき） {#authentication}
