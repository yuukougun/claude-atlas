---
id: build-test-harness
title: 検証環境・テスト基盤を作らせる
aliases: [テストハーネス, 評価環境, 入力の生成器, 並列のテストランナー, フィクスチャを作らせる]
type: recipe
field: recipes
chapter: 確かめる道具を作らせる
order: 120
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない]
scenes: [開発, コンテスト]
summary: 入力の生成・並列の実行・集計・比べる基準など、確かめるための環境を Claude に作らせる。できた環境は判定に使う前に既知の答えで確かめ、作業する側が書き換えられない場所に置く。
signs:
  - {type: goal, text: テストデータの生成器や、たくさんのケースを一度に回す仕組みを作らせたい}
  - {type: situation, text: 変更が良くなったかを、毎回同じ物差しで測る環境がない}
prerequisites: [verifier-three-conditions]
related: [verifier-defines-problem, test-the-verifier, freeze-eval-assets, lockbox-and-holdout, differential-testing, measure-changes, experiment-log, evaluators-by-format, misses-broken-evaluation, build-observation-tools, pitfalls-of-ai-written-tests]
sources: []
volatility: 低
sections:
  - {title: 何を作らせるか, anchor: what-to-build}
  - {title: 作った環境を確かめる, anchor: check-the-harness}
  - {title: 検証の資産を分けて置く, anchor: separate-eval-assets}
stage: stub
updated: 2026-11-04
---

## 何を作らせるか {#what-to-build}

## 作った環境を確かめる {#check-the-harness}

## 検証の資産を分けて置く {#separate-eval-assets}
