---
id: lock-side-effects
title: 縛りすぎの害と見直し（止めすぎ・回り込み）
nav_title: 縛りすぎの害と見直し
aliases: [縛りの副作用, 止めすぎ, フックの回り込み, 縛りを外す判断]
type: concept
field: enforce
chapter: 縛りの運用
order: 150
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 握る]
prevents: []
pitfalls: []
scenes: [開発, チーム]
summary: 縛りを足しすぎたときに起きる止めすぎと回り込みを見分け、縛る規則を絞り直せる。止めるときは理由と代わりの手段を返し、止めた記録を見直す。
signs:
  - {type: symptom, text: フックで止めたら、別のコマンドで同じことをしようとする}
  - {type: symptom, text: 縛りを増やしたら、作業が進まなくなった}
  - {type: goal, text: 入れた縛りが役に立っているか見直したい}
prerequisites: [block-with-exit-2]
related: [when-to-lock#what-not-to-lock, writing-safe-hooks, permission-rules, hook-recipes, what-auto-mode-stops, stuck-in-a-check-loop, keeps-stopping, blames-the-tools, postmortems, paved-roads]
tracks: [hooks, permissions]
sources: []
volatility: 中
sections:
  - {title: 縛る規則の選び方（機械的に判定でき、害の大きいものだけ）, anchor: what-to-lock}
  - {title: 止めるときに返すこと, anchor: reason-and-alternative}
  - {title: 止めた記録の見直し, anchor: review-blocks}
stage: stub
updated: 2026-11-04
---

## 縛る規則の選び方（機械的に判定でき、害の大きいものだけ） {#what-to-lock}

## 止めるときに返すこと {#reason-and-alternative}

## 止めた記録の見直し {#review-blocks}
