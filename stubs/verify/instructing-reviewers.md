---
id: instructing-reviewers
title: レビュアーへの指示の書き方
aliases: [レビューの頼み方, レビュー用のプロンプト, 指摘の出させ方]
type: concept
field: verify
chapter: レビューで確かめる
order: 120
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, 文章]
summary: レビュー役に、何を基準に何を出させるかを決めて頼める。網羅と選別を分け、自分の見立てを書き添えず、指摘ごとに確かめ方を付けさせる。
signs:
  - {type: symptom, text: レビューを頼むと、細かい好みの指摘ばかり出てくる}
  - {type: symptom, text: 「重大なものだけ」と頼んだら、大事な指摘まで減った}
  - {type: goal, text: レビュー役に、何をどこまで出させるかを決めたい}
prerequisites: [independent-review]
related: [ask-without-sycophancy, sycophancy, model-quirks, does-more-than-asked, grow-review-checklists, writing-subagents, second-opinion-from-another-model, automated-pr-review, agreement-is-not-evidence]
tracks: [subagents, code-review]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 網羅と選別を分ける, anchor: exhaustive-then-filter}
  - {title: 自分の見立てを書き添えない, anchor: hide-your-view}
  - {title: 指摘ごとに確かめ方を付けさせる, anchor: per-finding}
stage: stub
updated: 2026-11-04
---

## 網羅と選別を分ける {#exhaustive-then-filter}

## 自分の見立てを書き添えない {#hide-your-view}

## 指摘ごとに確かめ方を付けさせる {#per-finding}
