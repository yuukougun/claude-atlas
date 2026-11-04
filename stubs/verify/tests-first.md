---
id: tests-first
title: テストを先に書かせる
aliases: [TDD, テスト駆動開発, テストファースト, red/green]
type: recipe
field: verify
chapter: テストで確かめる
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: 仕様からテストを先に書かせ、落ちることを確かめてから実装させられる。テストが実装の後追いになり、今の挙動をそのまま正解にするのを防ぐ。
signs:
  - {type: goal, text: テストを先に書かせてから実装させたい}
  - {type: symptom, text: 実装に合わせてテストまで書かれ、何を確かめたのか分からない}
  - {type: symptom, text: テストと実装がかみ合わず、直しの往復が続く}
prerequisites: [define-done]
related: [pitfalls-of-ai-written-tests, protect-tests, spec-first, fix-a-bug, verification-ladder, test-the-verifier]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 手順, anchor: steps}
  - {title: テストの変更は特に読む, anchor: review-test-changes}
stage: stub
updated: 2026-11-04
---

## 手順 {#steps}

## テストの変更は特に読む {#review-test-changes}
