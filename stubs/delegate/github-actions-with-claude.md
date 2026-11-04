---
id: github-actions-with-claude
title: GitHub Actions と @claude
aliases: [claude-code-action, /install-github-app]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 210
level: 回す
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: GitHub Actions から Claude Code を動かし、issue や PR で @claude と呼んだり、イベントや定時で作業させたりできる。鍵は secrets に置き、権限を最小にし、マージの前に人がレビューする。
signs:
  - {type: goal, text: issue や PR で、@claude と呼んで作業させたい}
  - {type: goal, text: スクリプトや CI から Claude Code を使いたい}
  - {type: symptom, text: 古い記事の書き方で、Claude の GitHub Action が動かない}
prerequisites: [headless-basics, protecting-secrets]
related: [lethal-trifecta, prompt-injection-in-practice, where-bypass-is-ok, permission-rules, automated-pr-review, risk-tiered-approval, create-and-review-prs, checking-unattended-runs, check-billing-path, bare-mode, choosing-automation, what-to-put-in-claude-md]
tracks: [github-actions]
outdated_advice: [action-beta-direct-prompt]
sources: []
volatility: 中
sections:
  - {title: 呼ばれて動く形と、イベントで動く形, anchor: modes}
  - {title: 鍵と権限, anchor: secrets-and-permissions}
  - {title: 外の人が書いた issue と PR, anchor: untrusted-input}
stage: stub
updated: 2026-11-04
---

## 呼ばれて動く形と、イベントで動く形 {#modes}

## 鍵と権限 {#secrets-and-permissions}

## 外の人が書いた issue と PR {#untrusted-input}
