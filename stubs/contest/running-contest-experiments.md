---
id: running-contest-experiments
title: 実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数）
nav_title: 実験の回し方
aliases: [ローカル評価の回し方, 勝率の判定, パラメータ調整]
type: recipe
field: contest
chapter: 評価と実験
order: 60
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: [体感を信じる]
scenes: [コンテスト]
summary: 結果のぶれを見込んでケース数と集計の方法を決め、パラメータの調整と勝率の判定を、誤差に負けない試合数で回す手順が分かる。
signs:
  - {type: symptom, text: 改善したはずの版が、ケースを増やすと負ける}
  - {type: goal, text: 勝率が本当に上がったのか、何試合やれば言えるか知りたい}
  - {type: goal, text: AI にパラメータの探索を回させたい}
prerequisites: [experiment-log, evaluators-by-format]
related: [selection-pressure, measure-changes#by-stratum, lockbox-and-holdout, open-ended-loop-trap, compare-hypotheses-in-parallel, parallel-and-loop-costs, decide-when-to-quit, suspect-too-good-results, progress-logs-for-long-jobs]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: ぶれるならケースを増やす, anchor: more-cases}
  - {title: 集計の方法を選ぶ（相対スコア）, anchor: aggregation}
  - {title: 勝率に要る試合数, anchor: games-for-win-rate}
  - {title: パラメータは入力の性質ごとに, anchor: parameters-by-input}
  - {title: 効かなかった実験も残す, anchor: keep-all-runs}
stage: stub
updated: 2026-11-04
---

## ぶれるならケースを増やす {#more-cases}

## 集計の方法を選ぶ（相対スコア） {#aggregation}

## 勝率に要る試合数 {#games-for-win-rate}

## パラメータは入力の性質ごとに {#parameters-by-input}

## 効かなかった実験も残す {#keep-all-runs}
