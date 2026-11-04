---
id: sandboxing
title: サンドボックスで封じ込める
aliases: [sandbox, Sandboxing, /sandbox, bubblewrap, denyRead]
type: feature
field: enforce
chapter: 権限と封じ込め
order: 60
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: サンドボックスで、Claude が動かすコマンドの読み書きと通信を OS の層で囲える。既定では読み取りが広いので、秘密の場所は明示して塞ぐ。
signs:
  - {type: goal, text: 確認を減らしても、壊されたり外へ送られたりしないようにしたい}
  - {type: goal, text: auto モードに任せて大丈夫か}
  - {type: situation, text: スクリプトやテストを、確認なしで実行させたい}
  - {type: symptom, text: 拒否のルールを書いたのに、スクリプト経由で読まれた}
  - {type: goal, text: Docker や devcontainer の中で Claude Code を動かすべきか決めたい}
prerequisites: [permission-rules]
related: [protecting-secrets, where-bypass-is-ok, what-auto-mode-stops, approval-fatigue, protected-paths, lethal-trifecta, freeze-eval-assets, default-safety-settings#by-stage, before-opening-unknown-repos, writing-safe-hooks, dynamic-workflows]
tracks: [sandbox]
sources: []
volatility: 中
sections:
  - {title: 囲えるもの・囲えないもの, anchor: scope}
  - {title: 読み取りは既定で広い, anchor: default-reads}
  - {title: 起動できないときに通さない, anchor: fail-if-unavailable}
  - {title: Linux と WSL2 で使う, anchor: linux-wsl}
  - {title: コンテナ（Docker・devcontainer）との使い分け, anchor: containers}
stage: stub
updated: 2026-11-04
---

## 囲えるもの・囲えないもの {#scope}

## 読み取りは既定で広い {#default-reads}

## 起動できないときに通さない {#fail-if-unavailable}

## Linux と WSL2 で使う {#linux-wsl}

## コンテナ（Docker・devcontainer）との使い分け {#containers}
