---
id: xml-tags
title: XML タグで区切る
aliases: [XML tags, タグで構造化する, <document> で包む, 区切りを付ける]
type: concept
field: prompting
chapter: 資料と入力の渡し方
order: 130
level: 整える
priority: 推奨
surfaces: [api, claude-code, app]
principle: [見せる]
prevents: [散らかっている]
scenes: [開発, 調べもの]
summary: 指示・資料・例を説明的なタグで区切ると、どれが何かを Claude が取り違えにくくなる。タグの名前に決まりはなく、一貫していればよい。
signs:
  - {type: symptom, text: 指示・資料・例を一つの依頼に詰め込むと、どれがどれか混ざる}
  - {type: goal, text: 長い依頼を、読み違えられない形に整えたい}
prerequisites: []
related: [long-context-first, show-examples, data-vs-instructions, prompt-injection-in-practice, output-shape, prompt-patterns]
sources: []
volatility: 低
sections:
  - {title: 指示・資料・例を分ける, anchor: separate}
  - {title: 文書を入れ子にする, anchor: nesting}
  - {title: 外から貼った文章を包む, anchor: wrap-untrusted}
stage: stub
updated: 2026-11-04
---

## 指示・資料・例を分ける {#separate}

## 文書を入れ子にする {#nesting}

## 外から貼った文章を包む {#wrap-untrusted}
