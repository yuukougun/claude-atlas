---
id: data-analysis
title: データを分析する
aliases: [データ分析, SQL を書かせる, ログや CSV の集計, 分析の結果を確かめる]
type: recipe
field: recipes
chapter: データと分析
order: 140
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる, 同意を根拠にする]
scenes: [データ分析, 開発]
summary: データの集計や分析を、あとで再実行できるクエリやスクリプトの形で Claude に任せる。数字は生データで裏を取り、観察した事実と原因の解釈を分けて出させる。
signs:
  - {type: goal, text: ログや CSV を集計して傾向をつかみたい}
  - {type: symptom, text: 分析の結論はもっともらしいが、数字の出どころが分からない}
  - {type: symptom, text: 自分の仮説に合う分析ばかり返ってくる}
prerequisites: [evidence-not-reports, files-and-code-execution, ask-without-sycophancy]
related: [build-observation-tools, audit-ml-pipelines, entrusted-data, where-your-data-goes, character-encodings, measure-changes#by-stratum, check-the-metric, lockbox-and-holdout, suspect-too-good-results, agreement-is-not-evidence, mcp-or-cli, office-paperwork]
tracks: [code-execution]
sources: []
volatility: 中
sections:
  - {title: 再実行できる形で集計させる, anchor: reproducible-queries}
  - {title: 生データで裏を取る, anchor: check-raw-data}
  - {title: 観察と解釈を分ける, anchor: observation-vs-interpretation}
stage: stub
updated: 2026-11-04
---

## 再実行できる形で集計させる {#reproducible-queries}

## 生データで裏を取る {#check-raw-data}

## 観察と解釈を分ける {#observation-vs-interpretation}
