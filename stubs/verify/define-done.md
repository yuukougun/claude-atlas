---
id: define-done
title: 「完了」を定義して渡す
aliases: [完了条件, 完了の定義, Definition of Done, 終わりの条件を渡す]
type: concept
field: verify
chapter: 完了を確かめる
order: 10
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる, 見せる]
prevents: [確かめていない, 見えていない]
pitfalls: []
scenes: [開発, 文章]
summary: どのコマンドがどう返れば終わりか・変えてはならないもの・止まって報告する条件を決め、「完了」を測れる形で Claude に渡せる。終わったように見えた所で止まる理由も分かる。
signs:
  - {type: goal, text: どこまでやったら終わりかを、はっきり伝えたい}
  - {type: goal, text: どのコマンドがどう返れば完了かを、依頼に書いて渡したい}
  - {type: goal, text: 席を外す前に、終わりの条件を決めて渡したい}
prerequisites: [agent-loop]
related: [evidence-not-reports, verification-ladder, four-specifics, ask-for-outcomes, state-the-scope, permission-to-stop, claims-done-but-isnt, does-more-than-asked, tests-first, spec-first, goal-until-done, measure-changes, check-the-metric]
tracks: []
outdated_advice: [keep-going-dont-be-lazy]
sources: []
volatility: 低
sections:
  - {title: 終わったように見えた所で止まる, anchor: why-it-stops}
  - {title: 完了の定義に入れるもの, anchor: what-to-include}
  - {title: 止まって報告する条件, anchor: stop-and-report}
stage: stub
updated: 2026-11-04
---

## 終わったように見えた所で止まる {#why-it-stops}

## 完了の定義に入れるもの {#what-to-include}

## 止まって報告する条件 {#stop-and-report}
