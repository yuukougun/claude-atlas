---
id: working-with-git
title: git との付き合い方
aliases: [コミットを任せるか, 小さくコミットする, draft PR, git を Claude に任せる]
type: concept
field: cli
chapter: 巻き戻しとセッション
order: 70
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない, 境界がない]
pitfalls: [預けすぎる]
scenes: [開発, チーム]
summary: 変更を小さく区切ってコミットし、コミットと push を人が握るか任せるかを段階で決める。一つの変更を一つの評価と一つのコミットに対応させると、悪くなったときにすぐ戻せる。
signs:
  - {type: goal, text: コミットや PR の作成をどこまで任せてよいか決めたい}
  - {type: situation, text: Claude の変更が大きくなり、どこで区切ればよいか分からない}
prerequisites: [checkpoints-and-rewind]
related: [create-and-review-prs, diffs-humans-must-read, destructive-commands, measure-changes, parallel-with-worktrees, bisect-regressions, own-generated-code, commit-and-comment-language, resume-and-branch]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: どこで区切るか, anchor: granularity}
  - {title: 誰がコミットするか, anchor: who-commits}
  - {title: 1変更1評価1コミット, anchor: one-change-one-eval}
stage: stub
updated: 2026-11-04
---

## どこで区切るか {#granularity}

## 誰がコミットするか {#who-commits}

## 1変更1評価1コミット {#one-change-one-eval}
