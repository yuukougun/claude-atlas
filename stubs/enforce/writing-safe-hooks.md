---
id: writing-safe-hooks
title: フックを安全に書く
aliases: [onFailure, fail-open, フックの exec 形式, 他人のフックを確かめる]
type: feature
field: enforce
chapter: フック
order: 110
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない, 境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: フックは失敗すると操作を通してしまう既定を知り、止める用途で失敗を止めに倒す書き方ができる。他人のフックは、コードとして確かめてから使う。
signs:
  - {type: symptom, text: 止めるはずのフックが、エラーのときは何も止めていなかった}
  - {type: situation, text: 他人のリポジトリやプラグインのフックを使おうとしている}
  - {type: symptom, text: 関係のない道具の呼び出しまでフックに止められる}
prerequisites: [hooks-basics]
related: [block-with-exit-2, hook-recipes, lock-side-effects, before-opening-unknown-repos, vetting-extensions, sandboxing]
tracks: [hooks]
sources: []
volatility: 中
sections:
  - {title: 既定は失敗すると通す（fail-open）, anchor: fail-open}
  - {title: matcher で止めすぎない, anchor: matcher}
  - {title: シェルを通さずに起動する（args）, anchor: exec-form}
  - {title: フックは利用者の権限で動く, anchor: runs-as-you}
stage: stub
updated: 2026-11-04
---

## 既定は失敗すると通す（fail-open） {#fail-open}

## matcher で止めすぎない {#matcher}

## シェルを通さずに起動する（args） {#exec-form}

## フックは利用者の権限で動く {#runs-as-you}
