---
id: checkpoints-and-rewind
title: チェックポイントと /rewind（git との違い）
aliases: [checkpoint, rewind, Esc を2回, /undo, /checkpoint, 巻き戻し]
type: feature
field: cli
chapter: 巻き戻しとセッション
order: 60
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発]
summary: プロンプトごとの時点に、コード・会話・その両方を戻し、途中から要約もできる。Bash で変えたファイルや外での変更は戻らないので、git の代わりにはしない。
signs:
  - {type: goal, text: 試しにやらせて、駄目なら元に戻したい}
  - {type: symptom, text: 巻き戻したのに、一部のファイルが元に戻らない}
prerequisites: [input-symbols]
related: [rewind-dont-correct, working-with-git, recover-lost-work, resume-and-branch, compact-and-auto-compact, deleted-something-important, destructive-commands, using-ides]
tracks: [checkpoints]
outdated_advice: []
sources: []
volatility: 中
sections:
  - {title: 戻せるもの・戻せないもの, anchor: what-is-restored}
  - {title: 途中から要約する, anchor: summarize}
  - {title: git と組み合わせる, anchor: with-git}
stage: stub
updated: 2026-11-04
---

## 戻せるもの・戻せないもの {#what-is-restored}

## 途中から要約する {#summarize}

## git と組み合わせる {#with-git}
