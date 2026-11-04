---
id: instructions-hidden-in-materials
title: 課題資料・問題文に仕込まれた指示
aliases: [AI 向けの隠し指示, 問題文のプロンプトインジェクション, 資料に埋め込まれた指示]
type: concept
field: safety
chapter: 悪意ある入力
order: 90
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [握る, 縛る]
prevents: [境界がない]
pitfalls: []
scenes: [学習, コンテスト, 文章, チーム]
summary: 課題の資料や問題文、受け取った文書に AI 向けの指示が仕込まれていたときに、何が起きているかと扱い方を判断できる。AI の利用を禁じる合図なら、規則に従う。
signs:
  - {type: symptom, text: 課題の資料や問題文を読ませたら、頼んでいない指示に従った答えが返ってきた}
  - {type: situation, text: 課題や問題文の PDF を、AI に読ませようとしている}
prerequisites: [prompt-injection-in-practice]
related: [checking-ai-rules, followed-injected-instructions, disclosure-and-provenance, practice-vs-contest-day, competition-rules, data-vs-instructions, lethal-trifecta]
sources: []
volatility: 中
sections:
  - {title: 仕込まれる指示の二つの型（攻撃と、利用の規則の合図）, anchor: two-kinds}
  - {title: 規則を先に確かめる, anchor: check-rules}
  - {title: 資料をデータとして扱う, anchor: treat-as-data}
stage: stub
updated: 2026-11-04
---

## 仕込まれる指示の二つの型（攻撃と、利用の規則の合図） {#two-kinds}

## 規則を先に確かめる {#check-rules}

## 資料をデータとして扱う {#treat-as-data}
