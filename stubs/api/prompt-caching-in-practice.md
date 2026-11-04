---
id: prompt-caching-in-practice
title: プロンプトキャッシングの実務
aliases: [prompt caching, cache_control, キャッシュのブレークポイント]
type: feature
field: api
chapter: API の主な機能
order: 60
level: 仕組みにする
priority: 推奨
surfaces: [api]
principle: [見せる]
prevents: [合っていない]
scenes: [開発]
summary: 毎回同じ先頭部分をキャッシュして、API の費用と待ち時間を抑えられる。区切りをどこに置くか、何を変えるとキャッシュが無効になるかが分かる。
signs:
  - {type: goal, text: 長いシステムプロンプトや資料を毎回送る費用を抑えたい}
  - {type: symptom, text: キャッシュを指定したのに効いていない}
prerequisites: [why-prompt-caching, stateless-messages-api]
related: [reading-api-pricing, feature-to-api-mapping, using-projects, batch-api-basics, effort-levels, saving-priorities]
tracks: [prompt-caching]
sources: []
volatility: 中
sections:
  - {title: どこまでがキャッシュされるか（tools・system・messages の順）, anchor: prefix}
  - {title: キャッシュを無効にする変更, anchor: invalidation}
  - {title: 区切りの置き方, anchor: breakpoints}
stage: stub
updated: 2026-11-04
---

## どこまでがキャッシュされるか（tools・system・messages の順） {#prefix}

## キャッシュを無効にする変更 {#invalidation}

## 区切りの置き方 {#breakpoints}
