---
id: spec-first
title: 仕様を先に固める（spec・インタビュー・モック先行）
nav_title: 仕様を先に固める
aliases: [仕様駆動開発, spec 駆動, SPEC.md, インタビューで仕様を詰める, spec-driven development]
type: recipe
field: recipes
chapter: 作る・変える
order: 60
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [見せる, 確かめる]
prevents: [見えていない, 確かめていない]
scenes: [開発]
summary: 大きな機能は実装の前に Claude にインタビューさせて仕様を書かせ、範囲外と確かめ方まで決める。画面はモックで先に合意し、実装は仕様を渡した新しいセッションで行う。
signs:
  - {type: goal, text: 大きな機能を作る前に、要件の抜けをなくしたい}
  - {type: goal, text: 作り始める前に、画面の見た目と動きをモックで合意したい}
  - {type: goal, text: 何を作るのかを、質問に答えながら詰めていきたい}
prerequisites: [let-claude-ask, define-done, when-to-plan]
related: [read-specs-yourself, frontend-design, handoff-documents, state-the-scope, ask-for-outcomes, tests-first, goal-until-done, not-what-i-meant, does-more-than-asked, progress-files, record-decisions, refactor-and-migrate]
tracks: [ask-user-question, plan-mode, goal]
sources: []
volatility: 中
sections:
  - {title: インタビューで仕様を詰める, anchor: interview}
  - {title: 仕様に書くこと, anchor: what-goes-in-the-spec}
  - {title: モックで先に合意する, anchor: mock-first}
  - {title: 新しいセッションで実装する, anchor: implement-fresh}
  - {title: 決まった仕様の実装を停止条件つきで回す, anchor: goal-with-stop-conditions, level: 仕組みにする}
stage: stub
updated: 2026-11-04
---

## インタビューで仕様を詰める {#interview}

## 仕様に書くこと {#what-goes-in-the-spec}

## モックで先に合意する {#mock-first}

## 新しいセッションで実装する {#implement-fresh}

## 決まった仕様の実装を停止条件つきで回す {#goal-with-stop-conditions}
