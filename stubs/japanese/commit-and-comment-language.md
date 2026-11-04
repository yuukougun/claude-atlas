---
id: commit-and-comment-language
title: コミットメッセージ・コメントの言語
aliases: [コミットを日本語で書かせる, コードのコメントの言語, CLAUDE.local.md に置く]
type: concept
field: japanese
chapter: 返答とコミットの言語
order: 40
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
scenes: [開発, チーム]
summary: コミットメッセージとコメントの言語はチームの決まりとして共有の指示に書き、個人の好みは個人の設定に分けて置く。返答の言語の設定がそこまで効くかは公式に書かれていない。
signs:
  - {type: goal, text: コミットメッセージは日本語、コードのコメントは英語にしたい}
  - {type: situation, text: OSS で、自分だけ日本語で返事をもらいたい}
  - {type: symptom, text: 返事は日本語なのに、コミットメッセージだけ英語になる}
prerequisites: [keep-replies-in-japanese]
related: [settings-layers, claude-md-loading-order, what-to-put-in-claude-md, working-with-git, share-team-settings, cloud-sessions-and-teleport, hook-recipes]
tracks: [language-setting, claude-md, settings]
sources: []
volatility: 中
sections:
  - {title: チームの決まりと個人の好みを分ける, anchor: team-vs-personal}
  - {title: 共有の設定の言語は個人の設定を上書きする, anchor: override}
  - {title: クラウドのセッションに届く指示, anchor: cloud}
  - {title: 設定がどこまで効くかは確かめる（検証ノート）, anchor: verify-note}
stage: stub
updated: 2026-11-04
---

## チームの決まりと個人の好みを分ける {#team-vs-personal}

## 共有の設定の言語は個人の設定を上書きする {#override}

## クラウドのセッションに届く指示 {#cloud}

## 設定がどこまで効くかは確かめる（検証ノート） {#verify-note}
