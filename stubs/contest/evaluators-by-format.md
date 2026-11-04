---
id: evaluators-by-format
title: 形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）
nav_title: 形式別の評価器
aliases: [ローカルテスタ, ローカル評価]
type: concept
field: contest
chapter: 評価と実験
order: 50
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [コンテスト]
summary: 形式ごとに検証器が何に当たるか（テスタ・ベンチマーカー・CV・flag の検証・対戦場など）と、公式や本番とのずれをどう確かめるかが分かる。
signs:
  - {type: goal, text: AHC のローカルテスタを AI に作らせたい}
  - {type: symptom, text: 手元の評価器のスコアが、公式の採点と合わない}
  - {type: goal, text: 対戦型の大会で、ボットの強さを手元で比べたい}
prerequisites: [verifier-three-conditions]
related: [test-the-verifier, verifier-defines-problem, differential-testing, lockbox-and-holdout, check-the-metric, build-test-harness, build-observation-tools, running-contest-experiments, competition-day-operations, format-cheatsheet, freeze-eval-assets, protect-tests, misses-broken-evaluation, suspect-too-good-results]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: どの形式でも、最初の成果物は評価器, anchor: evaluator-first}
  - {title: 短時間のアルゴリズム：愚直解との比較, anchor: stress-test}
  - {title: ヒューリスティック：公式とスコアが一致するテスタ, anchor: tester}
  - {title: 性能改善：ベンチマーカーと計装, anchor: benchmarker}
  - {title: CTF：提出の前の flag の検証, anchor: flag}
  - {title: データ分析：分布の差を確かめた CV, anchor: cv}
  - {title: ハッカソン：機械の評価器がないとき, anchor: no-mechanical-evaluator}
  - {title: 対戦型：対戦場と基準のボット, anchor: arena}
stage: stub
updated: 2026-11-04
---

## どの形式でも、最初の成果物は評価器 {#evaluator-first}

## 短時間のアルゴリズム：愚直解との比較 {#stress-test}

## ヒューリスティック：公式とスコアが一致するテスタ {#tester}

## 性能改善：ベンチマーカーと計装 {#benchmarker}

## CTF：提出の前の flag の検証 {#flag}

## データ分析：分布の差を確かめた CV {#cv}

## ハッカソン：機械の評価器がないとき {#no-mechanical-evaluator}

## 対戦型：対戦場と基準のボット {#arena}
