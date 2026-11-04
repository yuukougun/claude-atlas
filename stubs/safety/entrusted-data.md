---
id: entrusted-data
title: 預かったデータ・規約付きのデータを AI に渡してよいか
aliases: [機密のデータを AI に渡す, NDA のデータ, 顧客のデータ, コンペのデータの規約, 社外秘の資料]
type: concept
field: safety
chapter: データの扱い
order: 70
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [握る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, データ分析, チーム, コンテスト]
summary: 顧客のデータや、NDA・規約の付いたデータを、どの面なら渡してよいかを判断できる。預かったデータは、契約で扱いが決まっている面だけで使う。
signs:
  - {type: situation, text: 顧客から預かったデータを分析させたい}
  - {type: situation, text: コンペのデータを、クラウドで動くエージェントに読ませようとしている}
  - {type: goal, text: 社外秘の資料を AI に渡してよいか確かめたい}
prerequisites: [where-your-data-goes]
related: [checking-ai-rules, default-safety-settings#by-stage, protecting-secrets, where-it-runs, ai-usage-guidelines, via-cloud-providers, choosing-an-org-plan, data-analysis, office-paperwork, cloud-sessions-and-teleport]
sources: []
volatility: 中
sections:
  - {title: 誰のデータで、何が決まっているか, anchor: whose-data}
  - {title: 契約のある面だけで使う, anchor: contracted-surfaces}
  - {title: クラウドで動く作業に気をつける, anchor: cloud-runs}
stage: stub
updated: 2026-11-04
---

## 誰のデータで、何が決まっているか {#whose-data}

## 契約のある面だけで使う {#contracted-surfaces}

## クラウドで動く作業に気をつける {#cloud-runs}
