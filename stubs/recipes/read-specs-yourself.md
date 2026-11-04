---
id: read-specs-yourself
title: 仕様を自分で読み、AI に誤読を指摘させる
nav_title: 仕様を自分で読む
aliases: [誤読の検出, 仕様の読み違いを防ぐ, 要件定義書を読む, 問題文を読む]
type: recipe
field: recipes
chapter: 読んで理解する
order: 20
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [握る, 確かめる]
prevents: [見えていない, 確かめていない]
pitfalls: [預けすぎる, みんなの案になる]
scenes: [開発, コンテスト]
summary: 与えられた仕様は原文を自分で読んで要約を書き、AI には原文と突き合わせて誤読や落とした条件を指摘させる。理解は、採点や検証の処理を書いて公式の値と照らして確かめる。
signs:
  - {type: goal, text: 要件定義書や API の仕様の読み違いを防ぎたい}
  - {type: symptom, text: AI に要約させた仕様で実装したら、仕様の条件を取り違えていた}
  - {type: situation, text: 長い問題文や規約を読んでから取りかかる}
prerequisites: [summary-overgeneralization, fact-checking]
related: [think-before-asking, spec-first, explore-a-codebase, research-and-reports, tests-first, handing-long-documents, ai-ideas-are-everyones, practice-vs-contest-day, documents-in-japanese, checking-citations]
sources: []
volatility: 低
sections:
  - {title: 先に自分で読んで要約する, anchor: read-first}
  - {title: AI に誤読を指摘させる, anchor: misreading-detector}
  - {title: 採点の処理で理解を確かめる, anchor: check-by-scoring}
stage: stub
updated: 2026-11-04
---

## 先に自分で読んで要約する {#read-first}

## AI に誤読を指摘させる {#misreading-detector}

## 採点の処理で理解を確かめる {#check-by-scoring}
