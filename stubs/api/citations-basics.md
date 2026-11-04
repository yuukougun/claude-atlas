---
id: citations-basics
title: citations（根拠の箇所を返させる）
aliases: [Citations, 引用機能, cited_text]
type: feature
field: api
chapter: API の主な機能
order: 50
level: 仕組みにする
priority: 任意
surfaces: [api]
principle: [確かめる, 縛る]
prevents: [確かめていない]
scenes: [調べもの, 開発]
summary: 答えの各主張について、渡した資料のどの箇所が根拠かを API に返させられる。引用させる指示より確かな理由と、一緒に使えない機能が分かる。
signs:
  - {type: goal, text: 答えの根拠を、資料のどこかまで示させたい}
  - {type: symptom, text: API で資料を渡して引用させても、資料にない文が引用に混ざる}
prerequisites: [checking-citations]
related: [fact-checking, structured-outputs-basics, plausible-falsehoods, how-attachments-are-read, using-research]
tracks: [citations]
sources: []
volatility: 中
sections:
  - {title: 引用させる指示との違い, anchor: vs-prompting}
  - {title: 一緒に使えない機能, anchor: limits}
stage: stub
updated: 2026-11-04
---

## 引用させる指示との違い {#vs-prompting}

## 一緒に使えない機能 {#limits}
