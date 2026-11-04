---
id: rate-limits-and-errors
title: rate limits とエラー（混雑と再試行）
nav_title: rate limits とエラー
aliases: [レート制限, API のエラー, '429', '529', overloaded, 再試行, リトライ]
type: concept
field: api
chapter: 上限とエラー
order: 80
level: 仕組みにする
priority: 推奨
surfaces: [api, claude-code]
principle: [確かめる, 握る]
prevents: []
scenes: [開発]
summary: API が返す上限のエラーと混雑のエラーを見分け、待って再試行するか、送る量や時期を変えるかを決められる。再試行には間隔と回数の上限を設ける。
signs:
  - {type: symptom, text: API が 429 や 529 のエラーを返す}
  - {type: goal, text: 混雑や上限で失敗した呼び出しを、安全に再試行したい}
  - {type: goal, text: 大量の呼び出しを流す前に、上限に当たらないかを確かめたい}
prerequisites: []
related: [when-ai-is-unavailable, how-usage-limits-work, batch-api-basics, prompt-caching-in-practice, checking-unattended-runs, structured-outputs-basics#not-guaranteed, when-requests-are-refused, reading-api-pricing, sdk-comparison, agent-sdk-basics]
tracks: [messages-api, api-rate-limits]
sources: []
volatility: 高
sections:
  - {title: エラーの見分け方（自分の上限・全体の混雑・要求の誤り）, anchor: kinds}
  - {title: 上限の種類と、今の値の確かめ方, anchor: limit-types}
  - {title: 再試行の考え方（間隔を広げ、回数に上限を設ける）, anchor: retry}
  - {title: 上限に当たりにくい送り方, anchor: reduce-pressure}
  - {title: エラーにならずに止まる応答（長さの上限・拒否）, anchor: non-error-stops}
  - {title: Claude Code で同じエラーを見たとき, anchor: in-claude-code}
stage: stub
updated: 2026-11-04
---

## エラーの見分け方（自分の上限・全体の混雑・要求の誤り） {#kinds}

## 上限の種類と、今の値の確かめ方 {#limit-types}

## 再試行の考え方（間隔を広げ、回数に上限を設ける） {#retry}

## 上限に当たりにくい送り方 {#reduce-pressure}

## エラーにならずに止まる応答（長さの上限・拒否） {#non-error-stops}

## Claude Code で同じエラーを見たとき {#in-claude-code}
