---
id: can-i-prompt-in-japanese
title: 日本語で指示して大丈夫か
aliases: [日本語のプロンプト, 英語で書くべきか, 日本語と英語の精度, CLAUDE.md は英語で書くべきか]
type: concept
field: japanese
chapter: 考え方
order: 10
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない]
scenes: [開発, 文章]
summary: 日本語で頼んでよく、作業の指示を日本語と英語で比べたデータはない。言語を替えるより、具体性と構造を整え、コマンド・パス・識別子を原文のまま書くほうが先である。
signs:
  - {type: symptom, text: 日本語で頼むと精度が落ちる気がする}
  - {type: goal, text: 英語で書いたほうがよいのか知りたい}
  - {type: symptom, text: 日本語だとトークンや上限を早く使う気がする}
  - {type: goal, text: CLAUDE.md を日本語で書いてよいか知りたい}
prerequisites: [tokens]
related: [four-specifics, felt-vs-measured, keep-replies-in-japanese, what-uses-up-limits, saving-priorities, thinking-keywords, init-and-first-claude-md, documents-in-japanese]
tracks: [token-counting]
outdated_advice: [think-hard-keywords]
sources: []
volatility: 中
sections:
  - {title: 日本語と英語を比べた公式の評価と、その限り, anchor: evaluation}
  - {title: 原文のまま書くもの（コマンド・パス・識別子）, anchor: keep-original}
  - {title: CLAUDE.md を日本語で書くか, anchor: claude-md}
  - {title: 日本語のトークン数と、上限への効き方, anchor: tokens}
  - {title: 「熟考」と書けば深く考えるか, anchor: thinking-words}
stage: stub
updated: 2026-11-04
---

## 日本語と英語を比べた公式の評価と、その限り {#evaluation}

## 原文のまま書くもの（コマンド・パス・識別子） {#keep-original}

## CLAUDE.md を日本語で書くか {#claude-md}

## 日本語のトークン数と、上限への効き方 {#tokens}

## 「熟考」と書けば深く考えるか {#thinking-words}
