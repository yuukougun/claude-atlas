---
id: browser-agent-cautions
title: ブラウザや画面の操作を任せるときの注意
aliases: [Claude in Chrome の注意, Computer use の注意, ブラウザ操作の安全, Chrome・computer use・ブラウザでの注意]
type: concept
field: safety
chapter: 悪意ある入力
order: 130
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, 調べもの]
summary: ブラウザや画面の操作を Claude に任せるとき、ログイン済みのサイトや開いているアプリまで届くことを踏まえて、任せる範囲を決められる。機微な情報に触れる作業には使わない。
signs:
  - {type: situation, text: Claude in Chrome で作業を任せようとしている}
  - {type: goal, text: 画面の操作を任せても大丈夫な作業を見分けたい}
prerequisites: [prompt-injection-in-practice]
related: [browser-control, lethal-trifecta, visual-checks, default-safety-settings]
tracks: [claude-in-chrome, computer-use]
sources: []
volatility: 高
sections:
  - {title: 届く範囲（ログイン済みのサイト・開いているアプリ）, anchor: reach}
  - {title: 任せない作業, anchor: what-not-to-do}
stage: stub
updated: 2026-11-04
---

## 届く範囲（ログイン済みのサイト・開いているアプリ） {#reach}

## 任せない作業 {#what-not-to-do}
