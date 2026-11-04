---
id: suspected-degradation
title: 劣化を疑ったら測って確かめる
aliases: [品質の低下, nerf, 劣化の確かめ方]
type: recipe
field: models
chapter: 替えたとき・劣化を疑うとき
order: 70
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [確かめる]
prevents: [合っていない]
pitfalls: [体感を信じる]
summary: 劣化を疑ったとき、版と effort を記録して同じ課題を何度か流して比べ、体感でなく結果で確かめられる。製品の側の変更が原因だった例から、公式の報告と変更履歴の確かめ方も分かる。
signs:
  - {type: goal, text: 「劣化した」と感じたのが本当かを、測って確かめたい}
  - {type: goal, text: 更新の前と後で、同じ課題の結果を比べたい}
  - {type: situation, text: 「性能が落とされた」という話を見かけ、自分の環境でも起きているか確かめたい}
prerequisites: [effort-levels, felt-vs-measured]
related: [seems-less-capable, measure-changes, nondeterminism, checking-for-updates, change-timeline-2026, after-switching-models]
tracks: [effort, model-selection]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 版と effort を記録して、同じ課題で比べる, anchor: measure}
  - {title: 製品の側の変更を確かめる先（公式の報告・変更履歴・稼働状況）, anchor: official-sources}
  - {title: 製品の側だったときの手当て（更新の通り道・報告）, anchor: if-product-side}
  - {title: 製品の側の変更だった例, anchor: postmortem-example}
stage: stub
updated: 2026-11-04
---

## 版と effort を記録して、同じ課題で比べる {#measure}

## 製品の側の変更を確かめる先（公式の報告・変更履歴・稼働状況） {#official-sources}

## 製品の側だったときの手当て（更新の通り道・報告） {#if-product-side}

## 製品の側の変更だった例 {#postmortem-example}
