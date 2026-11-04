---
id: visual-checks
title: 画面で確かめる（ブラウザ・スクリーンショット・/verify）
nav_title: 画面で確かめる
aliases: [スクリーンショットで確かめる, ブラウザで動作確認, E2E で確かめる]
type: feature
field: verify
chapter: 完了を確かめる
order: 40
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: 画面を持つ成果物を、ブラウザの操作やスクリーンショットの比較で、人が使うのと同じように確かめさせられる。単体テストや応答の確認だけで完了とみなすのを防ぐ。
signs:
  - {type: goal, text: 見た目の崩れを確かめさせたい}
  - {type: symptom, text: テストは通るのに、画面を開くと動かない}
  - {type: goal, text: モックと出来上がりの画面の違いを挙げさせたい}
prerequisites: [evidence-not-reports]
related: [browser-control, images-and-voice, verification-ladder, browser-agent-cautions, looks-are-not-quality, frontend-design, make-slides, claims-done-but-isnt]
tracks: [claude-in-chrome, verify-skill]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 人のユーザーとして確かめさせる, anchor: as-a-user}
  - {title: スクリーンショットで比べる, anchor: screenshots}
stage: stub
updated: 2026-11-04
---

## 人のユーザーとして確かめさせる {#as-a-user}

## スクリーンショットで比べる {#screenshots}
