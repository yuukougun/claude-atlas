---
id: align-japanese-output
title: 日本語の出力を揃える：お願いで足りること、仕組みが要ること
nav_title: 日本語の出力を揃える仕組み
aliases: [日本語の出力品質, 返答の言語と文体を固定する, お願いと鍵（日本語の場合）]
type: concept
field: japanese
chapter: 考え方
order: 20
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る, 確かめる]
prevents: [縛っていない, 確かめていない]
scenes: [開発, 文章, チーム]
summary: 返答の言語・文体・表記を揃える手段を、届く範囲と強制力で選び分けられる。指示はどれも保証にならず、仕組みで止められる場所にも限りがあることを前提に組む。
signs:
  - {type: situation, text: 日本語の指示を足しても揃わず、仕組みにすべきか迷っている}
  - {type: goal, text: 日本語の出力を、いつも同じ文体と表記にしたい}
  - {type: situation, text: チームで日本語の文書を Claude に書かせる}
wave: 1
prerequisites: [request-vs-lock]
related: [keep-replies-in-japanese, consistent-politeness, consistent-notation, textlint-hook, replies-in-english, inconsistent-japanese-style, where-to-put-instructions, claude-md-vs-rules-skills-styles, request-lock-table, when-to-lock, output-style-modes]
tracks: [language-setting, claude-md, output-styles, hooks, personal-instructions, project-instructions, app-skills]
outdated_advice: [styles-for-tone]
sources: []
volatility: 中
sections:
  - {title: お願いの層：設定・CLAUDE.md・出力スタイル・アプリの指示, anchor: request-layer}
  - {title: 確かめて差し戻す層：フックと lint, anchor: lock-layer, level: 仕組みにする}
  - {title: 届く範囲（サブエージェント・圧縮の後・クラウドのセッション）, anchor: reach}
  - {title: アプリには指示しかない, anchor: app}
  - {title: 縛る規則は少なく保つ, anchor: keep-few}
stage: stub
updated: 2026-11-04
---

## お願いの層：設定・CLAUDE.md・出力スタイル・アプリの指示 {#request-layer}

## 確かめて差し戻す層：フックと lint {#lock-layer}

## 届く範囲（サブエージェント・圧縮の後・クラウドのセッション） {#reach}

## アプリには指示しかない {#app}

## 縛る規則は少なく保つ {#keep-few}
