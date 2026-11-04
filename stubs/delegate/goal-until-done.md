---
id: goal-until-done
title: /goal（完了するまで続けさせる）
aliases: [完了条件で続けさせる, 自作ループ（Ralph など）, Ralph のループ]
type: feature
field: delegate
chapter: 続けさせる
order: 60
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: 完了の条件を満たすまで Claude にターンを続けさせ、席を外している間も作業を進められる。判定役は会話に出た証拠しか読まないので、証拠を会話に出させる条件を書く。
signs:
  - {type: goal, text: テストが通るまで終わらせたくない}
  - {type: goal, text: 条件を満たすまで、自分で作業を続けさせたい}
  - {type: goal, text: 席を外している間も進めてほしい}
  - {type: symptom, text: 条件に入れた「テストを変えない」が守られたか判定されない}
prerequisites: [five-questions-before-delegating]
related: [evidence-not-reports, verification-ladder, stop-hooks, protect-tests, what-auto-mode-stops, sandboxing, spec-first#goal-with-stop-conditions, refactor-and-migrate#goal-stop-conditions, open-ended-loop-trap, progress-logs-for-long-jobs, completion-notifications, loop-and-scheduling, batch-and-p-loops, permission-to-stop, parallel-and-loop-costs, when-ai-is-unavailable, claims-done-but-isnt, keeps-stopping, stuck-in-a-check-loop]
tracks: [goal]
outdated_advice: [keep-going-dont-be-lazy, ralph-loops]
sources: []
volatility: 中
sections:
  - {title: 判定役は会話しか読まない, anchor: evaluator-reads-conversation}
  - {title: 条件の書き方（終わりの状態・証明・変えないもの・上限）, anchor: writing-conditions}
  - {title: 仕様の決まった実装に限る, anchor: spec-tasks-only}
  - {title: 自作ループ（Ralph など）から移る, anchor: from-homemade-loops}
  - {title: 利用上限で止まったとき, anchor: at-usage-limits}
stage: stub
updated: 2026-11-04
---

## 判定役は会話しか読まない {#evaluator-reads-conversation}

## 条件の書き方（終わりの状態・証明・変えないもの・上限） {#writing-conditions}

## 仕様の決まった実装に限る {#spec-tasks-only}

## 自作ループ（Ralph など）から移る {#from-homemade-loops}

## 利用上限で止まったとき {#at-usage-limits}
