---
id: explore-a-codebase
title: 知らないコードベースを読む
aliases: [コードベースの理解, オンボーディング, 既存のコードを把握する, コードの地図を作る]
type: recipe
field: recipes
chapter: 読んで理解する
order: 10
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [見えていない, 確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, 学習]
summary: 知らないコードベースの全体像を、広い質問から始めて具体的な箇所へ絞りながらつかむ。説明は該当のファイルと行で確かめ、分かったことは地図や用語集にして残す。
signs:
  - {type: situation, text: 引き継いだリポジトリで、どこに何があるか分からない}
  - {type: goal, text: ある処理が入口からどこを通って動くのかを追いたい}
  - {type: symptom, text: コードの説明がもっともらしいが、本当にそう動くのか分からない}
prerequisites: [choose-what-to-read, fact-checking]
related: [read-specs-yourself, research-in-subagents, code-intelligence-plugins, own-generated-code, how-much-understanding-to-keep, learning-with-ai, before-opening-unknown-repos, vetting-extensions#dependencies, what-to-put-in-claude-md, init-and-first-claude-md, uses-nonexistent-apis, fix-a-bug]
tracks: [subagents, plugins]
outdated_advice: [architecture-in-claude-md]
sources: []
volatility: 中
sections:
  - {title: 広い質問から絞る, anchor: broad-to-narrow}
  - {title: 説明をコードで確かめる, anchor: check-against-code}
  - {title: 地図と用語集を残す, anchor: keep-a-map}
  - {title: 他人のリポジトリを開くとき, anchor: unknown-repos}
stage: stub
updated: 2026-11-04
---

## 広い質問から絞る {#broad-to-narrow}

## 説明をコードで確かめる {#check-against-code}

## 地図と用語集を残す {#keep-a-map}

## 他人のリポジトリを開くとき {#unknown-repos}
