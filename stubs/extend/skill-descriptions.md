---
id: skill-descriptions
title: スキルの description の書き方
aliases: [スキルの説明文, when_to_use, スキルが使われない]
type: feature
field: extend
chapter: スキル
order: 120
level: 仕組みにする
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: スキルが使われない・余計に使われるときに、説明文を直して起動を合わせられる。いつ使うかを先頭に具体的に書き、ほかのスキルと重ならないようにする。
signs:
  - {type: goal, text: 作ったスキルを、使ってほしい場面で確実に使わせたい}
  - {type: symptom, text: 関係のない場面で、別の手順が勝手に読み込まれる}
prerequisites: [writing-skills]
related: [how-skills-load, manual-only-skills, measure-changes, pruning-extensions, writing-subagents]
tracks: [skills]
sources: []
volatility: 中
stage: stub
updated: 2026-11-04
---
