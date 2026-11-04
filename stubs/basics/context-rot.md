---
id: context-rot
title: context rot と紛らわしい情報
aliases: [コンテキストの劣化, 長い会話の劣化, distractor, 失敗の残骸, lost in the middle, 中ほどの情報は使われにくい, 位置の効果, U 字型の性能]
type: concept
field: basics
chapter: コンテキストと注意
order: 40
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [散らかっている]
summary: 入力が長くなるほど、また似ているが違う情報が混ざるほど、答えの質が下がりやすいことが分かる。失敗した試みが会話に残ると紛らわしい情報になるので、片付けや巻き戻しが効く。
signs:
  - {type: goal, text: 長い会話で答えの質が落ちていく理由を知りたい}
  - {type: goal, text: 失敗した試みが会話に残ると、同じ誤りに戻りやすくなる理由を知りたい}
  - {type: goal, text: 長い資料の真ん中の情報は使われにくい、というのは本当か知りたい}
prerequisites: [attention-budget]
related: [forgets-in-long-chats, going-in-circles, when-to-start-fresh, rewind-dont-correct, tidy-the-desk, handoff-documents, large-context-window, long-context-first, handing-long-documents, skipped-later-pages]
outdated_advice: [save-context-for-200k]
sources: []
volatility: 低
sections:
  - {title: 中ほどの情報は使われにくいか（lost in the middle）, anchor: lost-in-the-middle, level: 整える}
stage: stub
updated: 2026-11-04
---

## 中ほどの情報は使われにくいか（lost in the middle） {#lost-in-the-middle}
