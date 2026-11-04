---
id: character-encodings
title: 文字コード（Shift_JIS の CSV など）
aliases: [Shift_JIS, CP932, 文字化け, UTF-8 に変換する]
type: recipe
field: japanese
chapter: 資料と環境
order: 100
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [見せる]
prevents: [見えていない]
scenes: [データ分析, 開発]
summary: Shift_JIS などで保存されたファイルは文字化けや集計の空欄の元になるので、UTF-8 に変えてから渡すか、文字コードを伝えて読ませる。Claude Code の編集の道具がそうしたファイルを拒むこともある。
signs:
  - {type: symptom, text: CSV を集計させたら、日本語の列が空欄や文字化けになった}
  - {type: symptom, text: Shift_JIS のファイルを編集させようとしたら断られた}
  - {type: situation, text: Excel や古い業務システムが書き出したファイルを渡す}
prerequisites: []
related: [files-and-code-execution, how-attachments-are-read, data-analysis, office-paperwork, documents-in-japanese, windows-wsl-ime]
sources: []
volatility: 中
sections:
  - {title: 渡す前に文字コードを確かめる, anchor: check}
  - {title: UTF-8 に変えてから渡す, anchor: convert}
  - {title: Claude Code の編集の道具と文字コード, anchor: claude-code}
stage: stub
updated: 2026-11-04
---

## 渡す前に文字コードを確かめる {#check}

## UTF-8 に変えてから渡す {#convert}

## Claude Code の編集の道具と文字コード {#claude-code}
