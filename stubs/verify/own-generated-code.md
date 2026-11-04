---
id: own-generated-code
title: 生成コードを自分のものにする
aliases: [AI が書いたコードの理解]
type: recipe
field: verify
chapter: レビューで確かめる
order: 140
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, 学習, コンテスト]
summary: 生成されたコードを採る前に、Claude に処理の流れと入力の端を説明させ、実際の動きと照らし、自分の言葉で言い直して理解を確かめられる。言い直せない所が、読み直す箇所になる。
signs:
  - {type: goal, text: 生成されたコードを理解したうえで採りたい}
  - {type: goal, text: マージする前に、生成されたコードのどこが分かっていないかを洗い出したい}
  - {type: situation, text: 大事な処理を書き換えたコードを、Claude から受け取った}
prerequisites: [how-much-understanding-to-keep]
related: [learning-with-ai, diffs-humans-must-read, evidence-not-reports, unfaithful-reasoning, explore-a-codebase, independent-review, over-reliance, looks-are-not-quality, create-and-review-prs, review-bottlenecks, experiment-log]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: 処理の流れと入力の端を説明させる, anchor: explain}
  - {title: 説明を実際の動きと照らす, anchor: check-explanation}
  - {title: 自分の言葉で言い直してから採る, anchor: gate}
stage: stub
updated: 2026-11-04
---

## 処理の流れと入力の端を説明させる {#explain}

## 説明を実際の動きと照らす {#check-explanation}

## 自分の言葉で言い直してから採る {#gate}
