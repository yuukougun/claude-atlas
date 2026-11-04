---
id: instructions-ignored
title: CLAUDE.md や指示が守られない
aliases: [指示を無視される, CLAUDE.md が効かない, skill が使われない, ルールを破られる, 決めたコマンドを使わない]
type: symptom
field: symptoms
chapter: 指示と仕組み
order: 170
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 見せる]
prevents: [見えていない, 散らかっている, 縛っていない]
pitfalls: []
scenes: [開発]
summary: CLAUDE.md や指示に書いた規則が破られる原因を切り分け、書き方を直すか、どれを仕組みに移すかを決める。
signs:
  - {type: symptom, text: CLAUDE.md に書いたのに守られない}
  - {type: symptom, text: 長い会話の途中から規則を無視し始める}
  - {type: symptom, text: 作った skill が使われない}
  - {type: symptom, text: CLAUDE.md を書き足すほど守られなくなった}
  - {type: symptom, text: 決めたコマンド（uv・pnpm など）を使わず別の方法で実行する}
wave: 1
prerequisites: [request-vs-lock, where-instructions-sit]
related: [emphasis-words, hook-vs-skill, request-lock-table, hooks-basics, block-with-exit-2, where-to-put-instructions, init-and-first-claude-md, forgot-after-compaction, replies-in-english, repeating-the-same-explanation, inconsistent-japanese-style, isolate-with-safe-mode, lock-side-effects, six-causes]
routes:
  - {cause: 見えていない, to: [inspect-context, claude-md-loading-order, skill-descriptions]}
  - {cause: 散らかっている, to: [claude-md-length, what-to-put-in-claude-md, path-scoped-rules]}
  - {cause: 縛っていない, to: [when-to-lock, permission-rules, hook-recipes#redirect-commands]}
tracks: [claude-md, rules, skills, hooks, permissions]
outdated_advice: [important-caps]
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
