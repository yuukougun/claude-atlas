---
id: request-vs-lock
title: お願いと鍵
aliases: [試験用の別名, もう一つの別名]
type: concept
field: basics
order: 10
level: 使う
priority: 必須
surfaces: [claude-code, app]
principle: [縛る]
prevents: [縛っていない]
summary: 試験用の要約。
signs:
  - {type: goal, text: 試験用のやりたいこと2}
prerequisites: []
related: [completion-check]
sources: [sample-doc]
volatility: 低
sections:
  - {title: 二つの層, anchor: two-layers}
stage: reviewed
updated: 2026-10-01
verified: 2026-10-01
verified_with: {claude_code: 2.1.317, channel: latest, models: [claude-opus-5-5]}
checked: 2026-10-20
---

!!! abstract "要点"
    - **何ができるか**：試験用の項目。
    - **いつ引くか**：試験用の項目。
    - **前提**：なし

<!-- textlint-disable -->
別名：試験用の別名・もう一つの別名
<!-- textlint-enable -->

お願いと鍵は、試験用の導入である。

## 二つの層 {#two-layers}

上限は <!-- fact:begin sample-limit -->100 回（2026-10-15 時点）<!-- fact:end --> である。

目印の書き方は `<!-- fact:begin <id> -->` の形で、`100 回` のような行の中のコードは数えない。

```text
上限は 100 回と書いたフェンスの中は数えない
```

=== "アプリ"

    アプリの手段。

=== "Claude Code"

    Claude Code の手段。

面のタブでない組は見ない。

=== "Before"

    前。

=== "After"

    後。
