---
id: fact-checking
title: 事実を確かめる（引用・照合・best-of-N）
nav_title: 事実を確かめる
aliases: [ファクトチェック, 裏取り, ハルシネーション対策]
type: recipe
field: verify
chapter: 事実を確かめる
order: 60
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない, 見えていない]
pitfalls: []
scenes: [調べもの, 文章, 学習]
summary: 答えの中の事実を、根拠の引用・資料との照合・同じ質問の繰り返しで確かめられる。重要な事実ほど、一次の資料で裏を取る。
signs:
  - {type: goal, text: 答えの中の事実が正しいか確かめたい}
  - {type: goal, text: 渡した資料に書いてあることだけで答えさせたい}
  - {type: goal, text: 要約が原文に書いてあるとおりかを照らしたい}
prerequisites: [why-hallucinations]
related: [checking-citations, plausible-falsehoods, allow-i-dont-know, doesnt-know-latest, knowledge-cutoff, nondeterminism, search-research-thinking, using-research, summary-overgeneralization, summary-overstates-source, handing-long-documents, research-and-reports, read-specs-yourself, citations-basics]
tracks: [web-search, research, citations]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 主張ごとに引用させる, anchor: quotes}
  - {title: 渡した資料の範囲で答えさせる, anchor: sources-only}
  - {title: 何度か聞いて比べる（best-of-N）, anchor: best-of-n}
  - {title: 要約を原文と照らす, anchor: summaries}
stage: stub
updated: 2026-11-04
---

## 主張ごとに引用させる {#quotes}

## 渡した資料の範囲で答えさせる {#sources-only}

## 何度か聞いて比べる（best-of-N） {#best-of-n}

## 要約を原文と照らす {#summaries}
