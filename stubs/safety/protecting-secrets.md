---
id: protecting-secrets
title: 秘密情報（.env・API キー）を守る
aliases: [.env を読ませない, API キーの漏洩, 認証情報を守る, 秘密の読み取りの禁止]
type: recipe
field: safety
chapter: 秘密と壊す操作
order: 140
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [縛る]
prevents: [境界がない, 縛っていない]
pitfalls: []
scenes: [開発]
summary: .env や API キー、認証情報を Claude に読ませない設定を、権限ルールとサンドボックスの二重にして作れる。会話に貼った秘密は、手元の記録に平文で残る。
signs:
  - {type: goal, text: .env や API キーを、絶対に読ませたくない}
  - {type: situation, text: 認証情報のあるマシンで、Claude Code に作業を任せる}
prerequisites: [sandboxing]
related: [secrets-exposed#first-response, permission-rules, lethal-trifecta, what-feedback-sends, where-your-data-goes, what-auto-mode-stops, hook-recipes, before-opening-unknown-repos, check-billing-path, default-safety-settings#by-stage]
tracks: [permissions, sandbox]
sources: []
volatility: 中
sections:
  - {title: 秘密を作業ディレクトリと会話に置かない, anchor: keep-out}
  - {title: 権限ルールとサンドボックスの二重にする, anchor: two-layers}
stage: stub
updated: 2026-11-04
---

## 秘密を作業ディレクトリと会話に置かない {#keep-out}

## 権限ルールとサンドボックスの二重にする {#two-layers}
