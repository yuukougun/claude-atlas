---
id: replies-in-english
title: 英語で返ってくる
aliases: [英語に戻る, 返事が英語になる, 日本語で返してくれない]
type: symptom
field: symptoms
chapter: 日本語の出力
order: 190
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る, 見せる]
prevents: [見えていない, 散らかっている, 縛っていない, 合っていない]
pitfalls: []
scenes: [開発, 文章]
summary: 日本語で頼んでいるのに英語で返る原因を、設定・読み込んだ英語の出力・モデル・面の順に切り分け、指示で足りるか仕組みで止めるかを決める。
signs:
  - {type: symptom, text: 返事が英語になる}
  - {type: symptom, text: 途中から英語に切り替わって戻らない}
  - {type: symptom, text: ツールの結果を読んだ後の一言だけ英語になる}
wave: 1
prerequisites: [request-vs-lock]
related: [can-i-prompt-in-japanese, commit-and-comment-language, hook-recipes, output-style-modes, forgot-after-compaction, instructions-ignored, inconsistent-japanese-style, isolate-with-safe-mode, six-causes]
routes:
  - {cause: 見えていない, to: [keep-replies-in-japanese#language-setting, settings-layers, what-subagents-dont-inherit]}
  - {cause: 散らかっている, to: [keep-replies-in-japanese#when]}
  - {cause: 縛っていない, to: [keep-replies-in-japanese#stop-hook, align-japanese-output#lock-layer, stop-hooks]}
  - {cause: 合っていない, to: [model-quirks, keep-replies-in-japanese#app-and-api, cloud-sessions-and-teleport#settings]}
tracks: [language-setting, settings, output-styles, claude-md, hooks]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
