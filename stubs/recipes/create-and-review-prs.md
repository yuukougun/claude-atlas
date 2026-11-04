---
id: create-and-review-prs
title: PR を作り、レビューを受ける
aliases: [プルリクエストを作らせる, PR の説明文, pull request, コードレビューを受ける]
type: recipe
field: recipes
chapter: 作る・変える
order: 100
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる, 同意を根拠にする]
scenes: [開発, チーム]
summary: 変更から PR を作らせ、出す前にリスクと確かめた証拠を書き出させる。説明は自分の言葉で書けるまで読み、AI のレビューが通ったことを人の承認の代わりにしない。
signs:
  - {type: goal, text: PR の作成と説明文の下書きを任せたい}
  - {type: situation, text: AI が書いた変更を、チームのレビューに出す}
  - {type: symptom, text: AI のレビューで問題なしと出たのに、人のレビューで欠陥が見つかった}
prerequisites: [working-with-git, independent-review, own-generated-code, agreement-is-not-evidence]
related: [diffs-humans-must-read, automated-pr-review, github-actions-with-claude, risk-tiered-approval, grow-review-checklists, review-bottlenecks, separate-roles, disclosure-and-provenance, instructing-reviewers, commit-and-comment-language, resume-and-branch, refactor-and-migrate]
sources: []
volatility: 中
sections:
  - {title: 出す前にリスクを挙げさせる, anchor: risks-before-submitting}
  - {title: PR の説明に書くこと, anchor: pr-description}
  - {title: レビューの指摘を直させる, anchor: address-review}
stage: stub
updated: 2026-11-04
---

## 出す前にリスクを挙げさせる {#risks-before-submitting}

## PR の説明に書くこと {#pr-description}

## レビューの指摘を直させる {#address-review}
