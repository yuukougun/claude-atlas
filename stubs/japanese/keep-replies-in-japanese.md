---
id: keep-replies-in-japanese
title: 日本語で返し続けさせる
aliases: [英語への回帰, 返答の言語を固定する, language 設定]
type: recipe
field: japanese
chapter: 返答とコミットの言語
order: 30
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [縛る, 確かめる]
prevents: [縛っていない]
scenes: [開発]
summary: 英語のツール出力やサブエージェントの報告を読んだ後に英語へ戻る返答を、設定・指示・フックの組み合わせで減らす。どれも完全には防げず、ツールの合間の短い一言が画面に出る前に止める仕組みはない。
signs:
  - {type: symptom, text: 言語を日本語に設定しても、英語の返事が混ざる}
  - {type: goal, text: Claude Code の返事を、いつも日本語にしたい}
  - {type: goal, text: 最後の返事が英語のときは、自動で日本語に直させたい}
wave: 1
prerequisites: [align-japanese-output]
related: [replies-in-english, where-to-put-instructions, stop-hooks, output-style-modes, settings-layers, what-subagents-dont-inherit, what-survives-compaction, cloud-sessions-and-teleport, agent-loop, where-instructions-sit, hook-recipes, commit-and-comment-language, measure-changes]
tracks: [language-setting, claude-md, output-styles, hooks, subagents, cloud-sessions]
sources: []
volatility: 高
sections:
  - {title: 英語に戻りやすい場面, anchor: when}
  - {title: 言語の設定と、効かないときに確かめること, anchor: language-setting}
  - {title: CLAUDE.md と出力スタイル（お願いの層）, anchor: instructions}
  - {title: Stop フックで最後の返事を確かめる, anchor: stop-hook, level: 仕組みにする}
  - {title: 届かない所（サブエージェント・圧縮の要約・クラウドのセッション）, anchor: reach}
  - {title: アプリと API の場合, anchor: app-and-api}
  - {title: どこまで減ったかを測る（検証ノート）, anchor: measure}
stage: stub
updated: 2026-11-04
---

## 英語に戻りやすい場面 {#when}

## 言語の設定と、効かないときに確かめること {#language-setting}

## CLAUDE.md と出力スタイル（お願いの層） {#instructions}

## Stop フックで最後の返事を確かめる {#stop-hook}

## 届かない所（サブエージェント・圧縮の要約・クラウドのセッション） {#reach}

## アプリと API の場合 {#app-and-api}

## どこまで減ったかを測る（検証ノート） {#measure}
