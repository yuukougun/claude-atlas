---
id: consistent-politeness
title: です・ます／だ・であるを揃える
aliases: [敬体と常体を揃える, 文体の統一, 文末が揺れる]
type: recipe
field: japanese
chapter: 文体と表記
order: 50
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる, 縛る]
prevents: [縛っていない, 見えていない]
scenes: [文章, 開発, チーム]
summary: 文体を一行で指定し、手本の文章を見せ、毎回読まれる場所に置くと揺れが減る。それでも揺れは残るので、混在は lint で見つけて直させる。
signs:
  - {type: goal, text: 文書を、です・ますか、だ・であるのどちらかに揃えたい}
  - {type: goal, text: チームの文書を、いつも同じ文体で書かせたい}
wave: 1
prerequisites: [align-japanese-output]
related: [inconsistent-japanese-style, consistent-notation, textlint-hook, show-examples, where-to-put-instructions, skills-in-the-app#migrated-styles, output-style-modes, less-ai-sounding-japanese, write-docs, requesting-prose, measure-changes]
tracks: [personal-instructions, project-instructions, app-skills, styles, claude-md, output-styles]
outdated_advice: [styles-for-tone]
sources: []
volatility: 中
sections:
  - {title: 文体は一行で、理由と一緒に指定する, anchor: specify}
  - {title: 手本の文章を見せる, anchor: example}
  - {title: 置き場所（アプリの指示・スキル・CLAUDE.md・出力スタイル）, anchor: where}
  - {title: 混在を lint で見つける, anchor: lint}
  - {title: 揃ったかを確かめる, anchor: check}
stage: stub
updated: 2026-11-04
---

## 文体は一行で、理由と一緒に指定する {#specify}

## 手本の文章を見せる {#example}

## 置き場所（アプリの指示・スキル・CLAUDE.md・出力スタイル） {#where}

## 混在を lint で見つける {#lint}

## 揃ったかを確かめる {#check}
