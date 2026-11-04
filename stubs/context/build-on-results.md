---
id: build-on-results
title: やり直させるより、結果を踏まえて直させる
aliases: [逐次改善, 結果を見せて直させる, 一から作り直させない]
type: concept
field: context
chapter: 新しくする・巻き戻す
order: 40
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [見せる, 確かめる]
prevents: [見えていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 出力を良くしたいとき、毎回一から作り直させず、前回の結果と測った値を見せて直させる進め方が分かる。会話の失敗は巻き戻し、分かったことはファイルに残して両立させる。
signs:
  - {type: goal, text: 出力を少しずつ良くしていきたい}
  - {type: symptom, text: 何度作り直させても同じくらいの出来にしかならない}
prerequisites: [rewind-dont-correct]
related: [keep-failure-lessons, evidence-not-reports, define-done, measure-changes, handoff-documents, when-to-start-fresh, refine-in-conversation, wont-rethink-approach, performance-tuning]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 作り直しと直しの違い, anchor: regenerate-or-refine}
  - {title: /clear・巻き戻しとの両立, anchor: with-clear}
stage: stub
updated: 2026-11-04
---

## 作り直しと直しの違い {#regenerate-or-refine}

## /clear・巻き戻しとの両立 {#with-clear}
