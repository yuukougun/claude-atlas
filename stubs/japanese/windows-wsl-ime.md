---
id: windows-wsl-ime
title: Windows・WSL・IME で困ったら
aliases: [IME の変換候補の位置, 全角の入力, Windows の文字化け, WSL2 で使う]
type: recipe
field: japanese
chapter: 資料と環境
order: 110
level: 整える
priority: 任意
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 合っていない]
scenes: [開発]
summary: 日本語の入力・表示・文字化けの不具合は版ごとに個別に直されてきたので、まず版を確かめ、変更の記録で既知の不具合かを探す。
signs:
  - {type: symptom, text: 日本語入力の変換候補が変な位置に出る}
  - {type: symptom, text: Windows で日本語の出力が文字化けする}
  - {type: situation, text: Windows で Claude Code を使っている}
prerequisites: []
related: [character-encodings, checking-for-updates, using-ides, sandboxing]
sources: []
volatility: 高
sections:
  - {title: まず版と既知の不具合を確かめる, anchor: version}
  - {title: IME と全角の入力, anchor: ime}
  - {title: Windows の文字化け, anchor: mojibake}
  - {title: WSL で使う, anchor: wsl}
stage: stub
updated: 2026-11-04
---

## まず版と既知の不具合を確かめる {#version}

## IME と全角の入力 {#ime}

## Windows の文字化け {#mojibake}

## WSL で使う {#wsl}
