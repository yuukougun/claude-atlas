---
id: write-docs
title: ドキュメント・技術文書を書く
aliases: [README を書かせる, 設計書を書かせる, API の説明を書かせる, コメントや docstring の生成]
type: recipe
field: recipes
chapter: 調べものと文書
order: 170
level: 整える
priority: 推奨
surfaces: [claude-code, app]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
scenes: [文章, 開発]
summary: README や設計文書などの技術文書を、プロジェクトの既存の文書と規約を手本に見せて書かせる。内容はコードと照らして確かめ、文体と表記は検査の道具でそろえる。
signs:
  - {type: goal, text: コードに合った README や設計書を書かせたい}
  - {type: symptom, text: 書かせた文書が、コードの実際の動きと合っていない}
  - {type: goal, text: プロジェクトの文書の文体と用語を、既存の文書にそろえたい}
prerequisites: [show-examples, consistent-politeness, fact-checking]
related: [requesting-prose, less-ai-sounding-japanese, consistent-notation, textlint-hook, documents-in-japanese, artifacts-overview, commit-and-comment-language, research-and-reports, make-slides, record-decisions, explore-a-codebase, notes-and-pkm]
sources: []
volatility: 低
stage: stub
updated: 2026-11-04
---
