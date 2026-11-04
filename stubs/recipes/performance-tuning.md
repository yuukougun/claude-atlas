---
id: performance-tuning
title: 性能改善を頼む（プロファイルが先・出力の一致と実測）
nav_title: 性能改善を頼む
aliases: [高速化, 最適化, プロファイリング, パフォーマンスチューニング, 遅い処理を速くする]
type: recipe
field: recipes
chapter: 作る・変える
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 見せる]
prevents: [見えていない, 確かめていない]
pitfalls: [体感を信じる]
scenes: [開発, コンテスト]
summary: 性能改善は、プロファイルで遅い箇所を確かめてから対象を指定して頼む。速くなったという報告は信じず、変更前後の出力の一致と、複数回の実測の比較を証拠として求める。
signs:
  - {type: goal, text: 遅い処理を Claude に速くしてもらいたい}
  - {type: symptom, text: 桁違いに速くなったと報告されたが、本当か怪しい}
  - {type: symptom, text: 速くしてと頼んだら、遅くない所ばかり書き換えられた}
prerequisites: [suspect-too-good-results, differential-testing]
related: [evidence-not-reports, build-observation-tools, bisect-regressions, refactor-and-migrate, measure-changes#by-stratum, felt-vs-measured, measure-the-upper-bound, freeze-eval-assets, rewrote-tests-to-pass, uses-nonexistent-apis, search-code-checklist, experiment-log]
sources: []
volatility: 低
sections:
  - {title: プロファイルを先に取る, anchor: profile-first}
  - {title: 出力の一致と実測を証拠にする, anchor: same-output-and-timing}
  - {title: 出力が変わる最適化は分ける, anchor: output-changing-changes}
  - {title: 良すぎる速度向上を疑う, anchor: too-good-speedups}
stage: stub
updated: 2026-11-04
---

## プロファイルを先に取る {#profile-first}

## 出力の一致と実測を証拠にする {#same-output-and-timing}

## 出力が変わる最適化は分ける {#output-changing-changes}

## 良すぎる速度向上を疑う {#too-good-speedups}
