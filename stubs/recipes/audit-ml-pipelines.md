---
id: audit-ml-pipelines
title: 機械学習のパイプラインを点検させる
aliases: [データリークの点検, リーク監査, 前処理の漏れ, 再現性の点検]
type: recipe
field: recipes
chapter: データと分析
order: 150
level: 任せる
priority: 任意
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
scenes: [データ分析, 開発, コンテスト]
summary: 機械学習のパイプラインを、検証用のデータの漏れと再現性の観点で Claude に点検させる。答えは該当するコードの行の引用つきで出させ、検証の成績が良すぎるときはまず漏れを疑う。
signs:
  - {type: symptom, text: 機械学習の検証の成績が良すぎて、データの漏れがないか不安}
  - {type: goal, text: 前処理や分割の順番に漏れがないかを点検させたい}
prerequisites: [data-analysis, suspect-too-good-results]
related: [lockbox-and-holdout, check-the-metric, measure-changes#by-stratum, checking-citations, evaluators-by-format]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
