---
id: writing-subagents
title: サブエージェントの作り方と使いどころ
aliases: [subagent, カスタムサブエージェント, .claude/agents, /agents]
type: feature
field: extend
chapter: サブエージェント
order: 150
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [散らかっている, 確かめていない]
pitfalls: []
scenes: [開発]
summary: 調査・レビュー・出力の多い作業を、別の文脈で動く担当として定義できる。工程ではなく文脈の独立で分け、道具とモデルを絞り、余分なトークンがかかることを踏まえて使う。
signs:
  - {type: goal, text: 調査やレビューを、本筋の会話とは別の担当に任せたい}
  - {type: goal, text: 決まった役割の担当を、毎回同じ設定で呼びたい}
  - {type: symptom, text: 工程ごとに担当を作ったら、受け渡しの調整に追われている}
  - {type: symptom, text: 昔の記事の手順でサブエージェントを作ろうとしたら、作成の画面が出てこない}
prerequisites: [subagent-isolation]
related: [what-subagents-dont-inherit, skill-vs-subagent, research-in-subagents, independent-review, instructing-reviewers, permission-rules, hook-recipes#subagent-only, hooks-basics, choosing-parallel-modes, agent-teams, what-not-to-delegate, parallel-and-loop-costs, split-models-by-role, effort-levels#subagents-and-org-limits, skill-descriptions, agreement-is-not-evidence#reviewer-agreement]
tracks: [subagents]
outdated_advice: [agents-command, subagent-per-step, tell-it-to-use-subagents, subagents-to-save-context]
sources: []
volatility: 中
sections:
  - {title: 定義の書き方（ファイルを書くか、Claude に作らせる）, anchor: define}
  - {title: 使いどころと、使わない場面, anchor: when-to-use}
  - {title: 道具・モデル・effort を絞る, anchor: tools-and-model}
stage: stub
updated: 2026-11-04
---

## 定義の書き方（ファイルを書くか、Claude に作らせる） {#define}

## 使いどころと、使わない場面 {#when-to-use}

## 道具・モデル・effort を絞る {#tools-and-model}
