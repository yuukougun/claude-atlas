---
id: textlint-hook
title: textlint をフックで回す
aliases: [textlint の hook, textlint, 文章の lint, 書いた後に検査して差し戻す, 日本語の文章を機械で検査する]
type: recipe
field: japanese
chapter: 文体と表記
order: 80
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない]
scenes: [文章, 開発, チーム]
summary: ファイルを書いた直後に textlint を走らせ、残った違反を Claude に返して直させる。指示では揺れる文体と表記を、機械で見つけられる範囲だけ仕組みで揃える。
signs:
  - {type: goal, text: 文体や表記の決まりを、毎回自動で守らせたい}
  - {type: symptom, text: 用語集を渡して頼んでも、表記の揺れが残る}
  - {type: situation, text: 日本語のドキュメントを Claude Code で大量に書かせている}
wave: 1
prerequisites: [align-japanese-output, block-with-exit-2]
related: [consistent-politeness, consistent-notation, inconsistent-japanese-style, hook-recipes, hooks-basics, writing-safe-hooks, share-team-settings, less-ai-sounding-japanese, keep-replies-in-japanese]
tracks: [hooks]
sources: []
volatility: 中
sections:
  - {title: どのルールを機械に任せるか, anchor: rules}
  - {title: 書いた後に走らせて差し戻す, anchor: post-tool-use}
  - {title: 拾えない書き込み（シェルで書いたファイル）, anchor: gaps}
  - {title: フックが落ちたときと、規則を増やしすぎないこと, anchor: failure-and-few}
  - {title: チームで共有する, anchor: share}
stage: stub
updated: 2026-11-04
---

## どのルールを機械に任せるか {#rules}

## 書いた後に走らせて差し戻す {#post-tool-use}

## 拾えない書き込み（シェルで書いたファイル） {#gaps}

## フックが落ちたときと、規則を増やしすぎないこと {#failure-and-few}

## チームで共有する {#share}
