---
id: protected-paths
title: 消せない場所・触れない場所（protected paths）
aliases: [protected paths, 保護されたパス, critical paths, 作業ディレクトリの外への書き込み]
type: feature
field: enforce
chapter: 権限と封じ込め
order: 70
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: どの権限モードでも確認なしには書かせない場所と、消させない場所を知り、足りない境界を設定で足せる。作業ディレクトリの外への書き込みを道具の側で止める設定もある。
signs:
  - {type: symptom, text: '.claude や .git を書き換えるたびに確認が出る'}
  - {type: goal, text: 作業ディレクトリの外のファイルは書き換えさせたくない}
prerequisites: [permission-rules]
related: [destructive-commands, permission-modes-overview, sandboxing, what-auto-mode-stops, deleted-something-important, before-opening-unknown-repos, freeze-eval-assets]
tracks: [permissions, permission-modes]
sources: []
volatility: 中
sections:
  - {title: 保護される場所と、モードごとの扱い, anchor: protected}
  - {title: どのモードでも止まる削除, anchor: critical-rm}
  - {title: 作業ディレクトリの外への読み書きを閉じる, anchor: outside-working-directory}
stage: stub
updated: 2026-11-04
---

## 保護される場所と、モードごとの扱い {#protected}

## どのモードでも止まる削除 {#critical-rm}

## 作業ディレクトリの外への読み書きを閉じる {#outside-working-directory}
