---
id: how-attachments-are-read
title: 添付ファイルはどこまで読まれるか
aliases: [ファイルのアップロード, Upload files, Files API, PDF support, vision]
type: feature
field: app
chapter: 資料と長い会話
order: 60
level: 使う
priority: 必須
surfaces: [app, api]
principle: [見せる, 確かめる]
prevents: [見えていない]
scenes: [調べもの, データ分析]
summary: 添付した PDF や文書のどこまでが図も含めて読まれるかが分かり、大きな資料の分け方と、読まれたかの確かめ方を選べる。API で渡すときの違いも分かる。
signs:
  - {type: symptom, text: Word の資料に入れた図を読んでくれない}
  - {type: goal, text: 大きな資料を漏れなく読ませたい}
prerequisites: []
related: [skipped-later-pages, handing-long-documents, context-rot#lost-in-the-middle, long-context-first, images-and-voice, checking-citations, too-much-project-knowledge, files-and-code-execution, documents-in-japanese, feature-to-api-mapping]
tracks: [file-uploads, files-api]
sources: []
volatility: 中
sections:
  - {title: PDF とそれ以外の文書, anchor: pdf-and-others}
  - {title: 大きな資料の分け方, anchor: splitting}
  - {title: 読まれたかを確かめる（ページの番号と引用）, anchor: verify}
  - {title: API で渡すとき（Files API・PDF・画像）, anchor: api, level: 仕組みにする}
stage: stub
updated: 2026-11-04
---

## PDF とそれ以外の文書 {#pdf-and-others}

## 大きな資料の分け方 {#splitting}

## 読まれたかを確かめる（ページの番号と引用） {#verify}

## API で渡すとき（Files API・PDF・画像） {#api}
