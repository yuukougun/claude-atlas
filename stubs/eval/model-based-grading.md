---
id: model-based-grading
title: Claude に採点させる（人の判定で較正する）
aliases: [LLM as a judge, モデルによる採点, model-based grader, AI の採点の較正]
type: recipe
field: eval
chapter: 検証器を作る
order: 90
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, api, app]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [文章, 開発]
summary: 機械で判定しにくい出力を Claude に採点させるとき、人の判定と比べて採点の基準を較正できる。較正していない AI の採点は、合否の根拠にしない。
signs:
  - {type: goal, text: 文章の質のような、機械で判定しにくいものを Claude に採点させたい}
  - {type: symptom, text: AI の採点は高いのに、読んでみると良くない}
prerequisites: [verifier-three-conditions, measure-changes]
related: [test-the-verifier, agreement-is-not-evidence, ask-without-sycophancy, sycophancy, independent-review, instructing-reviewers, goal-until-done, textlint-hook]
tracks: []
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: コードで判定できるものはコードで, anchor: prefer-code}
  - {title: 人の判定と比べて較正する, anchor: calibrate}
  - {title: 判定役が見ているもの, anchor: what-the-judge-sees}
stage: stub
updated: 2026-11-04
---

## コードで判定できるものはコードで {#prefer-code}

## 人の判定と比べて較正する {#calibrate}

## 判定役が見ているもの {#what-the-judge-sees}
