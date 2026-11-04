---
id: hook-recipes
title: 代表的なフックのレシピ
aliases: [フックの例, hooks の例, フォーマッタのフック, 危ないコマンドを止めるフック]
type: recipe
field: enforce
chapter: フック
order: 120
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない, 散らかっている]
pitfalls: []
scenes: [開発, チーム]
summary: 編集後の整形・危ない操作の遮断・決めたコマンドへの誘導・テスト出力の絞り込み・終わりの通知・担当にだけ禁じる操作を、フックで組める。どの型も、当てる範囲を狭くし、効いたかを確かめてから常設する。
signs:
  - {type: goal, text: 編集のたびにフォーマッタをかけさせたい}
  - {type: goal, text: pip ではなく uv のように、決めたコマンドを必ず使わせたい}
  - {type: goal, text: テストやログの出力で会話が埋まるのを防ぎたい}
  - {type: goal, text: サブエージェントにだけ commit を禁じたい}
prerequisites: [block-with-exit-2, writing-safe-hooks]
related: [hooks-basics, stop-hooks, textlint-hook, protecting-secrets, destructive-commands, what-to-put-in-claude-md#what-to-write, freeze-eval-assets, lock-side-effects, writing-subagents, what-subagents-dont-inherit, completion-notifications]
tracks: [hooks]
sources: []
volatility: 中
sections:
  - {title: 編集の後に整形する, anchor: format-after-edit}
  - {title: 危ない操作を止める, anchor: block-dangerous}
  - {title: 決めたコマンドへ誘導する（pip の代わりに uv など）, anchor: redirect-commands}
  - {title: テストの出力を絞る, anchor: filter-test-output}
  - {title: 終わったら知らせる, anchor: notify}
  - {title: 担当にだけ禁じる（agent_id）, anchor: subagent-only}
stage: stub
updated: 2026-11-04
---

## 編集の後に整形する {#format-after-edit}

## 危ない操作を止める {#block-dangerous}

## 決めたコマンドへ誘導する（pip の代わりに uv など） {#redirect-commands}

## テストの出力を絞る {#filter-test-output}

## 終わったら知らせる {#notify}

## 担当にだけ禁じる（agent_id） {#subagent-only}
