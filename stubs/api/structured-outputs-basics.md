---
id: structured-outputs-basics
title: structured outputs（形式を保証する）
aliases: [構造化出力, JSON outputs, strict tool use, --json-schema]
type: feature
field: api
chapter: API の主な機能
order: 40
level: 仕組みにする
priority: 推奨
surfaces: [api, claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない]
scenes: [開発, データ分析]
summary: 出力やツールの呼び出しを、指定したスキーマどおりの形で受け取れる。それでも形が崩れる場合と、形が正しくても中身は別に確かめる理由が分かる。
signs:
  - {type: symptom, text: JSON で返すよう頼んでも形が崩れる}
  - {type: goal, text: 出力を必ず決まった形で受け取りたい}
prerequisites: [request-vs-lock]
related: [output-shape, looks-are-not-quality, tool-use-loop, citations-basics, headless-basics]
tracks: [structured-outputs]
outdated_advice: [prefill-for-json]
sources: []
volatility: 中
sections:
  - {title: JSON outputs と strict tool use, anchor: two-modes}
  - {title: 形が保証されない場合, anchor: not-guaranteed}
  - {title: prefill からの移行, anchor: from-prefill}
  - {title: Claude Code の -p で形を指定する, anchor: claude-code}
stage: stub
updated: 2026-11-04
---

## JSON outputs と strict tool use {#two-modes}

## 形が保証されない場合 {#not-guaranteed}

## prefill からの移行 {#from-prefill}

## Claude Code の -p で形を指定する {#claude-code}
