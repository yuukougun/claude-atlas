---
id: compact-and-auto-compact
title: /compact と自動圧縮
aliases: [コンテキスト圧縮, 自動圧縮, auto-compact, idle compaction, /autocompact, 休憩と cache 切れ, 1M 時代の圧縮設定]
type: feature
field: context
chapter: 圧縮
order: 50
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発]
summary: /compact に残す焦点を指示して会話を要約させ、自動圧縮や放置したときの圧縮で何が消えうるかを見越して備える。要約で失いたくない作業は、書き出してから /clear する。
signs:
  - {type: goal, text: 長い作業を同じセッションのまま続けたい}
  - {type: symptom, text: 席を外して戻ったら、会話が要約されていた}
  - {type: situation, text: 自動圧縮のタイミングを変えるべきか迷っている}
prerequisites: [what-survives-compaction]
related: [promises-after-compaction, handoff-documents, when-to-start-fresh, checkpoints-and-rewind#summarize, inspect-context, forgot-after-compaction, when-to-lock#spoken-rules-fade, long-chat-limits, large-context-window, why-prompt-caching, what-uses-up-limits, keep-replies-in-japanese]
tracks: [compaction, context-window]
outdated_advice: [save-context-for-200k]
sources: []
volatility: 中
sections:
  - {title: /compact に焦点を指示する, anchor: focused-compact}
  - {title: 自動圧縮で起きること, anchor: auto-compact}
  - {title: 席を外すとき（idle compaction と cache 切れ）, anchor: idle-compaction}
  - {title: 圧縮か、書き出して /clear か, anchor: compact-or-clear}
  - {title: 圧縮の設定, anchor: settings, level: 仕組みにする}
stage: stub
updated: 2026-11-04
---

## /compact に焦点を指示する {#focused-compact}

## 自動圧縮で起きること {#auto-compact}

## 席を外すとき（idle compaction と cache 切れ） {#idle-compaction}

## 圧縮か、書き出して /clear か {#compact-or-clear}

## 圧縮の設定 {#settings}
