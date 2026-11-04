---
id: measure-changes
title: 変更が効いたかを測る（小さな eval）
aliases: [小さな eval, プロンプトの評価（eval）入門, 前後で比べる, 変更の効果の測り方, pass^k]
type: recipe
field: eval
chapter: 変化を測る
order: 30
level: 任せる
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: [体感を信じる]
scenes: [開発, 文章]
summary: CLAUDE.md・プロンプト・スキルの変更が効いたかを、失敗したタスクを前後で何度か走らせて比べる小さな eval で確かめられる。一度の試行では判断しない。
signs:
  - {type: goal, text: CLAUDE.md を変えて良くなったか知りたい}
  - {type: goal, text: プロンプトや手順書を直した効果を比べたい}
  - {type: symptom, text: 一度試して良かった変更が、次には効かなかった}
  - {type: symptom, text: 平均は良くなったのに、一部のケースで悪くなっていた}
wave: 1
prerequisites: [felt-vs-measured, nondeterminism, define-done]
related: [model-based-grading, experiment-log, selection-pressure, after-switching-models, claude-md-length, writing-skills#evaluate, pruning-extensions, before-after-prompts, prompt-patterns, keep-replies-in-japanese#measure, check-the-metric, test-the-verifier, insights-and-usage-review, headless-basics, batch-api-basics, measure-the-upper-bound, verifier-defines-problem]
tracks: [plugin-eval]
outdated_advice: [console-prompt-generator]
sources: []
volatility: 低
sections:
  - {title: 成功の基準を先に決める（task・trial・grader・transcript・outcome）, anchor: terms}
  - {title: 小さな eval の手順, anchor: small-eval}
  - {title: スキルの有り無しを新しいセッションで比べる（skill-creator・claude plugin eval）, anchor: compare-skills, level: 仕組みにする}
  - {title: 採点の種類（コード・モデル・人）, anchor: graders}
  - {title: 試行の数と差の大きさ, anchor: how-many-runs}
  - {title: 合計ではなく、層別と最悪ケースで見る, anchor: by-stratum, level: 仕組みにする}
  - {title: transcript を読む, anchor: read-transcripts}
stage: stub
updated: 2026-11-04
---

## 成功の基準を先に決める（task・trial・grader・transcript・outcome） {#terms}

## 小さな eval の手順 {#small-eval}

## スキルの有り無しを新しいセッションで比べる（skill-creator・claude plugin eval） {#compare-skills}

## 採点の種類（コード・モデル・人） {#graders}

## 試行の数と差の大きさ {#how-many-runs}

## 合計ではなく、層別と最悪ケースで見る {#by-stratum}

## transcript を読む {#read-transcripts}
