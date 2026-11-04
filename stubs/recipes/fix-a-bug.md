---
id: fix-a-bug
title: バグを直す
aliases: [デバッグ, 不具合の修正, エラーを直させる, バグ修正]
type: recipe
field: recipes
chapter: 直す
order: 30
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [確かめる, 見せる]
prevents: [見えていない, 確かめていない]
scenes: [開発, コンテスト]
summary: バグは、再現の手順と「直った」の定義を渡し、失敗するテストで再現させてから直させる。原因の仮説を確かめる前にコードを変えさせず、症状を隠すだけの修正を認めない。
signs:
  - {type: goal, text: エラーの原因を突き止めて直させたい}
  - {type: symptom, text: 直したと言われたのに、条件を変えると同じバグが出る}
  - {type: symptom, text: 修正を頼むたびに、的外れな場所が書き換えられる}
prerequisites: [evidence-not-reports]
related: [define-done, shrink-failing-inputs, bisect-regressions, build-observation-tools, going-in-circles, claims-done-but-isnt, rewrote-tests-to-pass, rewind-dont-correct, tests-first, protect-tests, differential-testing, wont-rethink-approach, uses-nonexistent-apis, vetting-extensions#dependencies, agent-teams, before-after-prompts]
tracks: [checkpoints]
outdated_advice: [add-double-check]
sources: []
volatility: 中
sections:
  - {title: 再現と「直った」の定義を渡す, anchor: reproduce-and-define-done}
  - {title: 直す前に仮説を確かめさせる, anchor: hypotheses-before-fixes}
  - {title: 症状を隠す修正を認めない, anchor: no-symptom-patches}
  - {title: 直らないときは巻き戻して頼み直す, anchor: when-stuck}
stage: stub
updated: 2026-11-04
---

## 再現と「直った」の定義を渡す {#reproduce-and-define-done}

## 直す前に仮説を確かめさせる {#hypotheses-before-fixes}

## 症状を隠す修正を認めない {#no-symptom-patches}

## 直らないときは巻き戻して頼み直す {#when-stuck}
