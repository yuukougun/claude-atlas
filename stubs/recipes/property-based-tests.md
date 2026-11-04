---
id: property-based-tests
title: プロパティテストを書かせる
aliases: [プロパティベーステスト, property-based testing, Hypothesis, 性質のテスト]
type: recipe
field: recipes
chapter: 確かめる道具を作らせる
order: 110
level: 任せる
priority: 任意
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
scenes: [開発]
summary: 入力を自動で作って性質が成り立つかを確かめるテストを書かせ、例を並べたテストでは見つからない誤りを探させる。報告された失敗には誤報も混ざるので、人が再現して本物かを確かめる。
signs:
  - {type: goal, text: 例を並べたテストでは見つからない境界の誤りを探したい}
  - {type: goal, text: いろいろな入力を自動で作って、たくさん試すテストを書かせたい}
prerequisites: [pitfalls-of-ai-written-tests]
related: [shrink-failing-inputs, differential-testing, test-the-verifier, build-test-harness, suspect-too-good-results]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
