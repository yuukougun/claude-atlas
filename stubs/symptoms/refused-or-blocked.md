---
id: refused-or-blocked
title: 断られた・止められた
aliases: [利用ポリシーで止められた, 拒否された, 分類器に止められた, refusal]
type: symptom
field: symptoms
chapter: 返答と品質
order: 40
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない, 散らかっている, 合っていない]
pitfalls: []
scenes: [開発, 調べもの]
summary: 正当な依頼が断られた・止められたときに、利用ポリシーの判定か、auto モード・フック・権限ルールの停止かを先に見分け、引き金と依頼の文脈のどちらが効いたかを切り分けて進め直す。
signs:
  - {type: symptom, text: 正当な依頼なのに断られる}
  - {type: symptom, text: 「新しい会話を始めて」と言われて続けられない}
  - {type: symptom, text: 途中で別のモデルの返事に切り替わった}
  - {type: symptom, text: 操作を止められたが、何に止められたのか分からない}
wave: 1
prerequisites: []
related: [checkpoints-and-rewind, what-feedback-sends, isolate-with-safe-mode, current-models, block-with-exit-2, keeps-stopping, followed-injected-instructions, wrong-amount-of-approvals, six-causes]
routes:
  - {cause: 見えていない, to: [when-requests-are-refused#official-steps, give-reasons]}
  - {cause: 散らかっている, to: [rewind-dont-correct, when-to-start-fresh, asking-for-reasoning#refusal]}
  - {cause: 合っていない, to: [what-auto-mode-stops#when-blocked, lock-side-effects, permission-rules]}
tracks: [checkpoints, refusals, auto-mode]
outdated_advice: []
sources: []
volatility: 高
sections:
  - {title: 何に止められたかを見分ける（利用ポリシーか、auto モード・フック・権限ルールか）, anchor: what-stopped}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 面ごとの表示（本体は when-requests-are-refused の節 by-surface）, anchor: by-surface}
stage: stub
updated: 2026-11-04
---

## 何に止められたかを見分ける（利用ポリシーか、auto モード・フック・権限ルールか） {#what-stopped}

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->

## 面ごとの表示（本体は when-requests-are-refused の節 by-surface） {#by-surface}
