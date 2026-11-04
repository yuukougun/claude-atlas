---
id: research-in-subagents
title: 出力の多い調査はサブエージェントに任せて要約だけ受け取る
nav_title: 調査をサブエージェントに任せる
aliases: [調査は subagent に任せて要約だけ受け取る, サブエージェントに調べさせる, Explore subagent]
type: concept
field: context
chapter: 脇道を分ける
order: 140
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発, 調べもの]
summary: ログや多数のファイルを読む調査を別の文脈で行わせ、本筋には結論と根拠の場所だけを戻させる。トークンは余分にかかるので、出力が多く本筋から独立した調査に限る。
signs:
  - {type: goal, text: 調べものの途中経過で、本筋の会話を埋めたくない}
  - {type: situation, text: 「subagent を使え」と書き足すべきか迷っている}
prerequisites: [subagent-isolation]
related: [writing-subagents, skill-vs-subagent, what-subagents-dont-inherit, independent-review, choose-what-to-read, side-questions-btw, parallel-and-loop-costs, explore-a-codebase, tidy-the-desk]
tracks: [subagents]
outdated_advice: [subagents-to-save-context, tell-it-to-use-subagents, subagent-per-step]
sources: []
volatility: 中
sections:
  - {title: 任せてよい調査、本筋で読むべきもの, anchor: when}
  - {title: 頼み方と戻させる形, anchor: how}
  - {title: 費用と使いすぎ, anchor: cost}
stage: stub
updated: 2026-11-04
---

## 任せてよい調査、本筋で読むべきもの {#when}

## 頼み方と戻させる形 {#how}

## 費用と使いすぎ {#cost}
