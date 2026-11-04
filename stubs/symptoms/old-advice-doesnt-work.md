---
id: old-advice-doesnt-work
title: 記事や前のやり方が通じない
aliases: [古い記事が通じない, 前は効いたのに効かなくなった, 古い Tips, 記事の手順が動かない]
type: symptom
field: symptoms
chapter: 事実と出典
order: 100
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない, 合っていない]
pitfalls: []
scenes: [開発, 文章, 調べもの]
summary: 記事や本、前に覚えたやり方が通じないときに、その情報の日付と版を確かめ、撤回された助言か名前が変わっただけかを切り分けて、今のやり方に置き換えられる。
signs:
  - {type: symptom, text: 古い記事のやり方が通じない}
  - {type: symptom, text: 前は効いた書き方や設定が効かなくなった}
  - {type: symptom, text: 記事に出てくるコマンドや機能の名前が、手元に見当たらない}
  - {type: symptom, text: 記事によって書いてあることが食い違う}
wave: 1
prerequisites: []
related: [ask-claude-code#check-version, change-timeline-2026, writing-skills#from-commands, writing-subagents#define, thinking-keywords, emphasis-words, doesnt-know-latest, seems-less-capable, six-causes]
routes:
  - {cause: 確かめていない, to: [dating-information#check-date-and-version, checking-for-updates, outdated-advice-ledger#find-in-your-setup]}
  - {cause: 合っていない, to: [outdated-advice-ledger, term-index#old-names, command-cheatsheet]}
tracks: []
outdated_advice: [fork-to-branch, removed-commands, commands-directory, agents-command, routines-name, code-on-the-web-remote]
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
