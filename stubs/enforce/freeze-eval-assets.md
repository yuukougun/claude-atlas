---
id: freeze-eval-assets
title: 評価資産を凍結し、触れる範囲を絞る
aliases: [評価用のファイルを凍結する, 採点器を書き換えさせない, テストを書き換えさせない設定]
type: recipe
field: enforce
chapter: 縛りの運用
order: 140
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: テストや採点のスクリプト、検証用のデータを Claude が書き換えられないようにし、触れてよいファイルを絞れる。deny ルールだけでは子プロセスを止められないので、サンドボックスと組み合わせる。
signs:
  - {type: goal, text: テストや採点のスクリプトを、Claude に書き換えさせたくない}
  - {type: situation, text: スコアを上げる改善を、長い時間 Claude に任せる}
prerequisites: [verifier-three-conditions, sandboxing]
related: [protect-tests, permission-rules, lockbox-and-holdout, rewrote-tests-to-pass, reward-hacking, test-the-verifier, build-test-harness, protected-paths, hook-recipes, misses-broken-evaluation, selection-pressure]
tracks: [permissions, sandbox, hooks]
sources: []
volatility: 中
sections:
  - {title: 凍結するものと触らせるもの, anchor: what-to-freeze}
  - {title: 設定で止める（権限ルール・サンドボックス・ファイルの権限）, anchor: how-to-freeze}
  - {title: 凍結が効いているかを確かめる, anchor: check}
stage: stub
updated: 2026-11-04
---

## 凍結するものと触らせるもの {#what-to-freeze}

## 設定で止める（権限ルール・サンドボックス・ファイルの権限） {#how-to-freeze}

## 凍結が効いているかを確かめる {#check}
