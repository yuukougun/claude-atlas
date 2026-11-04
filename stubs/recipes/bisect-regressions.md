---
id: bisect-regressions
title: 退行の原因を git bisect で探させる
nav_title: 退行の原因を探させる
aliases: [git bisect run, リグレッションの原因探し, どのコミットで壊れたか, 退行の調査]
type: recipe
field: recipes
chapter: 直す
order: 50
level: 任せる
priority: 任意
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない]
scenes: [開発]
summary: 前は動いていたものが壊れたとき、良し悪しを判定するスクリプトを書かせ、git bisect run で原因のコミットを機械的に絞り込ませる。判定は Claude の推測でなく、スクリプトの終了コードで決める。
signs:
  - {type: symptom, text: 前は動いていたのに、いつの間にか壊れていた}
  - {type: goal, text: どの変更から遅くなったのかを突き止めたい}
prerequisites: [fix-a-bug, working-with-git, verifier-three-conditions]
related: [move-judgment-into-scripts, differential-testing, evidence-not-reports, shrink-failing-inputs, performance-tuning, build-test-harness]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
