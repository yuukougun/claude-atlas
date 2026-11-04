---
id: evidence-not-reports
title: 報告ではなく証拠を求める
aliases: [自己申告ではなく証拠, 実行結果で確かめる, 生の出力を出させる]
type: concept
field: verify
chapter: 完了を確かめる
order: 20
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, データ分析]
summary: 完了の報告を、実行したコマンドと生の出力と分母のそろった証拠で受け取れる。説明と事実が食い違えば、実行・grep・git で見た事実を正とする。
signs:
  - {type: symptom, text: テストの件数が、報告のたびに変わっている}
  - {type: symptom, text: うまくいった場合だけを並べた報告が返ってくる}
  - {type: goal, text: 見ていなかった作業が本当に済んだかを、短い時間で確かめたい}
prerequisites: [define-done]
related: [verification-ladder, claims-done-but-isnt, blames-the-tools, visual-checks, diffs-humans-must-read, looks-are-not-quality, suspect-too-good-results, checking-unattended-runs, insists-on-mistakes, unfaithful-reasoning, experiment-log]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 証拠の形（コマンド・生の出力・分母）, anchor: what-counts}
  - {title: 説明と事実が食い違ったら, anchor: facts-win}
  - {title: 道具の出力も確かめる（途中で切れた検索・失敗を成功として返す起動）, anchor: tool-output}
stage: stub
updated: 2026-11-04
---

## 証拠の形（コマンド・生の出力・分母） {#what-counts}

## 説明と事実が食い違ったら {#facts-win}

## 道具の出力も確かめる（途中で切れた検索・失敗を成功として返す起動） {#tool-output}
