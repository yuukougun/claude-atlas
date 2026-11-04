# write.md：less-ai-sounding-japanese

## 書いたファイル

- docs/japanese/less-ai-sounding-japanese.md（stubs から mv。stage を draft、updated を 2026-11-05。sections に guards・verify・failure を足し、patterns 以降の既存の anchor と level は変えていない。sources に cc-docs-skills・hc-skills-what を入れた）
- snippets/less-ai-sounding-japanese/revise-request.md と .expect.yaml（目次の templates の案：推敲の観点を書いた依頼、prompt）
- snippets/less-ai-sounding-japanese/proofread-ja.md と .expect.yaml（足した雛形：SKILL.md の例、skill）
- data/sources.d/<id>.yml は作っていない（新しい出典なし）

## 必ず持つものの対応

- 用途ごとの進め方（手順）：#revise-step（各段に「終わりの確かめ」あり）。スキル化の手順は #proofreading-skill
- 確かめる・縛るのページへの道：front matter の prerequisites（requesting-prose）と related。本文は #guards（requesting-prose#reader、consistent-politeness#guards、disclosure-and-provenance#four-points）、#lint-vs-judgment（textlint-hook など）
- level：front matter の level 整える。#proofreading-skill は 仕組みにする
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：#guards → #patterns・#own-writing・#revise-step・#proofreading-skill・#lint-vs-judgment → #verify → #failure

## メインに判断してほしいこと

- 第三者の推敲スキルは、名前を出さず「方針が 2 つに分かれる」とだけ書いた（目次の notes の、考え方の例として名前を出す案より控えめ）。名前と成熟度・確認日を付けて出すなら、材料の再確認が要る
- 「AI 臭さ」は読みやすさの品質と書き、AI の利用を隠さない旨を #guards の 1 項目に書いた。公開の方針に当たる文なら承認を（カード §13）。約束の文ではなく、手順の目的の説明のつもり

## 提案

なし（front matter・用語集・data への提案なし）。用語集に「lint」「推敲」があるかは未確認。

## 検査の結果

- 1 回目：エラー 0・警告 2（no-doubled-joshi）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと

- 雛形 2 つは動かしていない（expect は期待の記録）
- 型の表（前置き・「単なる A ではなく B」など）は書き手の整理した例で、Claude の出力の癖を測ったものではない。本文にもそう書いた
- アプリでのスキルの設定場所の名前は変わりつつあるため、画面の名前は書かず link 先に任せた
- `/proofread-ja` で呼べることは、data の names（project-prefix-removed）と手引きの記述からの推定で、実機では確かめていない
- `!!!` と `===` の中の字下げした段落は textlint の対象外なので、目で読んだが、機械では見ていない

## 使用量

- 道具の呼び出し：約 12 回（Read 2、Bash 5、Write 6 を含む）。Web の取得：0 回
