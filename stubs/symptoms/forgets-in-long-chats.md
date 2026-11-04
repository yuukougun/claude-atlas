---
id: forgets-in-long-chats
title: 長い会話で前提を忘れる・雑になる
aliases: [会話が長いと精度が落ちる, 前提を忘れる, context rot]
type: symptom
field: symptoms
chapter: 会話と文脈
order: 130
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発, 文章, 調べもの]
summary: 長い会話で前提を忘れ、答えが雑になる原因を、会話に溜まった無関係な情報から切り分け、新しい会話・引き継ぎ・委任のどれで片付けるかを決める。
signs:
  - {type: symptom, text: 会話が長くなると精度が落ちる}
  - {type: symptom, text: 最初に伝えた前提を途中から忘れる}
  - {type: symptom, text: 大量のログやテスト出力で会話が埋まっていく}
wave: 1
prerequisites: [context-rot]
related: [rereads-whole-history, attention-budget, rewind-dont-correct, research-in-subagents, hook-recipes#filter-test-output, inspect-context, large-context-window, compact-and-auto-compact, going-in-circles, forgot-after-compaction, unexpected-memories, seems-less-capable, skipped-later-pages, six-causes]
routes:
  - {cause: 見えていない, to: [handoff-documents, long-chat-limits]}
  - {cause: 散らかっている, to: [when-to-start-fresh, tidy-the-desk, choose-what-to-read#trim-output]}
tracks: [context-window, compaction, clear]
outdated_advice: [save-context-for-200k, subagents-to-save-context]
sources: []
volatility: 中
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
