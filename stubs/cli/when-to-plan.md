---
id: when-to-plan
title: plan mode の使いどころ
aliases: [plan モード, plan mode, プランモード, 計画モード, /plan, 計画させてから実装する]
type: feature
field: cli
chapter: 権限モードと計画
order: 50
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [握る, 見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: plan mode で編集を止めたまま調べさせ、出てきた計画を読んで直してから実装に入る。誤解は計画の段階で見つけるほど安く直せるので、方針や範囲に迷いがある作業で使う。
signs:
  - {type: goal, text: いきなり実装させず、先に方針を確かめたい}
  - {type: symptom, text: 大きな変更を、実装が済んでから方針ごと作り直すことが多い}
prerequisites: [permission-modes-overview]
related: [spec-first, let-claude-ask, define-done, split-models-by-role, not-what-i-meant, does-more-than-asked, handoff-documents, using-ides, cloud-sessions-and-teleport]
tracks: [plan-mode]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 計画が効く作業、省いてよい作業, anchor: when}
  - {title: 計画の読み方と直し方, anchor: review}
  - {title: 計画を承認した後, anchor: after-approval}
stage: stub
updated: 2026-11-04
---

## 計画が効く作業、省いてよい作業 {#when}

## 計画の読み方と直し方 {#review}

## 計画を承認した後 {#after-approval}
