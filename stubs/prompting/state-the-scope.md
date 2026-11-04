---
id: state-the-scope
title: 範囲を伝える（やらないこと）
aliases: [anti-goals, スコープを絞る, 頼んだ範囲で, やらないことを書く]
type: concept
field: prompting
chapter: 何をどこまで頼むか
order: 80
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる, 縛る]
prevents: [見えていない, 合っていない]
scenes: [開発]
summary: 依頼に、やること・やらないこと・触ってよい範囲を書くと、頼んでいない機能や変更が増えにくくなる。例外を許さない範囲は、言葉ではなく権限やフックで縛る。
signs:
  - {type: goal, text: 小さな修正は、小さいまま終わらせたい}
  - {type: goal, text: 触ってよいファイルを限りたい}
prerequisites: [four-specifics, request-vs-lock]
related: [does-more-than-asked, say-what-you-want, suggest-or-do, permission-rules, protected-paths, when-to-lock#spoken-rules-fade, model-quirks]
sources: []
volatility: 低
sections:
  - {title: やらないことを書く, anchor: anti-goals}
  - {title: いまの作業に要る最小限を求める, anchor: minimum}
  - {title: 例外を許さない範囲は仕組みで縛る（二層）, anchor: two-layers}
stage: stub
updated: 2026-11-04
---

## やらないことを書く {#anti-goals}

## いまの作業に要る最小限を求める {#minimum}

## 例外を許さない範囲は仕組みで縛る（二層） {#two-layers}
