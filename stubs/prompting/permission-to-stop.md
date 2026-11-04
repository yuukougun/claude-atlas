---
id: permission-to-stop
title: 止まって報告する権利を渡す
aliases: [テストがおかしければ報告させる, 回避せずに止まる, 人に判断を仰がせる]
type: concept
field: prompting
chapter: 正直さと確かめ方
order: 190
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
scenes: [開発, データ分析, コンテスト]
summary: テストや評価がおかしいと判断したら回避せずに止まって報告してよい、と依頼に書く。言葉の許可だけでは防ぎきれないので、テストを書き換えられない仕組みと組み合わせる。
signs:
  - {type: goal, text: テストが間違っていそうなら、書き換えずに報告してほしい}
  - {type: goal, text: 仕様と食い違うときは、手を止めて知らせてほしい}
prerequisites: [allow-i-dont-know]
related: [rewrote-tests-to-pass, protect-tests, misses-broken-evaluation, reward-hacking, verifier-three-conditions, suggest-or-do]
sources: []
volatility: 中
sections:
  - {title: 止まって報告する条件を書く, anchor: conditions}
  - {title: 言葉の許可が効く範囲（モデルによる差）, anchor: limits}
  - {title: 書き換えられない仕組みと組み合わせる, anchor: with-structure}
stage: stub
updated: 2026-11-04
---

## 止まって報告する条件を書く {#conditions}

## 言葉の許可が効く範囲（モデルによる差） {#limits}

## 書き換えられない仕組みと組み合わせる {#with-structure}
