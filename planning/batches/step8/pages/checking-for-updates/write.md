# write.md：checking-for-updates（執筆）

## 書いたファイル
- docs/changes/checking-for-updates.md（stubs から mv。front matter で変えたのは sections〔5 節〕・sources〔9 件〕・stage〔draft〕・updated〔2026-11-05〕）
- snippets/checking-for-updates/ に 3 つ：show-version（sh）・read-changes-since（prompt）・audit-outdated-writing（prompt）。各 expect.yaml 付き。目次の templates 案は audit-outdated-writing。ほか 2 つは手順の段 1・3 のために足した
- data/sources.d/checking-for-updates.yml（cc-docs-setup を新規。code.claude.com は既存ドメインなので check_noai は流していない）
- facts-proposal.yml（stable の遅れの日数）

## 必ず持つものの対応
- 手順：steps（6 段、各段に「確かめ」）
- 確かめる・縛るのページへの道：before-you-start（dating-information#check-date-and-version・ask-claude-code#check-version）、steps（after-switching-models#remove-one-at-a-time・outdated-advice-ledger#find-in-your-setup）、verify（suspected-degradation#measure）、when-it-fails（suspected-degradation・after-switching-models・outdated-advice-ledger・change-timeline-2026）
- level：整える（front matter）
- 構成の目安：要点 → before-you-start → where-records-live（面のタブ。記録の在り処は手順の前提なので手順の前に置いた）→ steps → verify → when-it-fails

## メインに判断してほしいこと
- stable の遅れの日数は、目次の備考どおり数値ファイルへ置く案を facts-proposal.yml に書いた。承認までは本文に日数を書かず、目印も置いていない
- 面のタブにある「`/release-notes` の動きは WSL・Linux の CLI 基準、ほかは未確認」の文は、基準の決まりに沿った書き方にした

## 提案
- facts-proposal.yml（上記）
- 用語集：prh が `skills` を `スキル` へ直すと指摘した。本文は「スキル」に直した。`/doctor` と `/release-notes` などのコマンド名は原文のまま

## 検査の結果
- 1 回目：エラー 2（skills の表記）・警告 4 → 直した。2 回目：エラー 0・警告 2
- 残した警告（no-doubled-joshi）：77 行目の「が」と 201 行目の「も」。どちらも文を分ける直しは可能だが、検査の回数の上限のため直していない。検証の担当が直せる

## 確かめていないこと
- `/release-notes`・`/doctor prompt-audit`・`claude doctor`・`claude update` の実際の動きを手元では動かしていない。公式の Commands・Skills・Advanced setup の文を 2026-11-05 に読んだ内容による
- show-version.sh と 2 つの依頼は動作確認をしていない。`npm view ... dist-tags` の出力の形は、調査資料 22 の記述〔latest・next・stable〕による
- `prompt-audit` が確認を取ってから直すかは、公式の文書が書いていない。本文もそう書いた
- Wayback の保存の日時（2026-10-26 19:44 UTC）と改稿の内容は、既存の出典 wb-cc-best-practices-2026-10-26 と調査資料 23 による。再取得していない
- 2.1.313 の欠番と 2.1.315 の項目なしは調査資料 22 の記述による（npm を再確認していない）
- アプリでのリリースノートの載り方（Help Center にだけ出る変更の例は本文で名前を出していない）

## 使用量
- 道具の呼び出し：約 25 回。Web の取得：3 回（commands・setup・skills）
