---
id: deleted-something-important
title: 消してはいけないものを消された
aliases: [ファイルを消された, rm -rf された, 履歴を消された]
type: symptom
field: symptoms
chapter: 安全と承認
order: 280
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 握る]
prevents: [縛っていない, 境界がない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: 消してはいけないファイルや履歴を消されたときに、戻せる手段を先に確かめて復旧し、何が止められなかったかを切り分けて再発を防ぐ。
signs:
  - {type: symptom, text: ファイルを消された・消されそうで怖い}
  - {type: symptom, text: git の履歴やブランチを巻き戻された}
  - {type: symptom, text: データベースのデータを消された}
wave: 1
prerequisites: [request-vs-lock]
related: [checkpoints-and-rewind, working-with-git, recover-lost-work, block-with-exit-2, hook-recipes, postmortems, notes-and-pkm, wrong-amount-of-approvals, secrets-exposed, six-causes]
routes:
  - {cause: 縛っていない, to: [destructive-commands, permission-rules, protected-paths]}
  - {cause: 境界がない, to: [sandboxing, where-bypass-is-ok]}
  - {cause: 預けすぎる, to: [default-safety-settings#by-stage, what-auto-mode-stops#limits]}
tracks: [checkpoints, permissions, permission-modes, sandbox, hooks]
outdated_advice: [yolo-skip-permissions]
sources: []
volatility: 中
sections:
  - {title: まず戻す（復旧の手順）, anchor: recover}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## まず戻す（復旧の手順） {#recover}

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
