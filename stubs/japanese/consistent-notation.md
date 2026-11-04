---
id: consistent-notation
title: 表記ゆれと漢字の開き
aliases: [表記の統一, 「サーバー」と「サーバ」, 用語集を渡す, 漢字をひらく, prh]
type: recipe
field: japanese
chapter: 文体と表記
order: 60
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる, 縛る]
prevents: [縛っていない, 見えていない]
scenes: [文章, 開発, チーム]
summary: 用語の表記と漢字を開く語を一覧にして渡し、機械で見つけられる揺れは辞書つきの lint で直させる。一覧は人が持つ正本から作り、指示と検査に同じものを使う。
signs:
  - {type: symptom, text: 漢字が多くて硬い文章になる}
  - {type: goal, text: 社内の用語集どおりの表記で書かせたい}
wave: 1
prerequisites: [align-japanese-output]
related: [inconsistent-japanese-style, consistent-politeness, textlint-hook, documents-in-japanese, less-ai-sounding-japanese, where-to-put-instructions, path-scoped-rules]
tracks: [project-instructions, claude-md]
sources: []
volatility: 中
sections:
  - {title: 表記の一覧（用語集）を作る, anchor: glossary}
  - {title: 漢字を開く語を決める, anchor: open-kanji}
  - {title: 一覧を指示と lint の両方に使う, anchor: single-source}
stage: stub
updated: 2026-11-04
---

## 表記の一覧（用語集）を作る {#glossary}

## 漢字を開く語を決める {#open-kanji}

## 一覧を指示と lint の両方に使う {#single-source}
