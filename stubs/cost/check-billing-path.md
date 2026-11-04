---
id: check-billing-path
title: 課金の経路を確かめる（API キーとサブスクリプション）
nav_title: 課金の経路を確かめる
aliases: [ANTHROPIC_API_KEY, API キーの課金, サブスクリプションで使う, 認証の優先順位, API credits]
type: concept
field: cost
chapter: 課金の経路と API
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [確かめる]
prevents: [合っていない]
pitfalls: []
summary: Claude Code がプランと API キーのどちらで課金されているかを確かめ、思わぬ従量課金を防げる。環境変数・起動の仕方・面で経路が変わるので、無人で回す前に確かめる。
signs:
  - {type: symptom, text: サブスクリプションで使っているつもりが、API の請求が来た}
  - {type: goal, text: スクリプトから動かすとき、どの支払いで動くのか確かめたい}
  - {type: situation, text: プランに付く API credits を Claude Code で使えるのか分からない}
prerequisites: [how-usage-limits-work]
related: [headless-basics#billing-path, bare-mode#authentication, agent-sdk-basics#billing, protecting-secrets, usage-credits-basics#vs-api-credits, reading-api-pricing, settings-layers, sdk-comparison, github-actions-with-claude, via-cloud-providers]
tracks: [headless, agent-sdk, api-credits]
outdated_advice: []
sources: []
volatility: 高
sections:
  - {title: 経路が決まる順, anchor: how-the-path-is-chosen}
  - {title: API キーの環境変数があるとき, anchor: api-key-in-env}
  - {title: 今の経路を確かめる, anchor: check-current-path}
  - {title: プランに付く API credits, anchor: monthly-api-credits}
stage: stub
updated: 2026-11-04
---

## 経路が決まる順 {#how-the-path-is-chosen}

## API キーの環境変数があるとき {#api-key-in-env}

## 今の経路を確かめる {#check-current-path}

## プランに付く API credits {#monthly-api-credits}
