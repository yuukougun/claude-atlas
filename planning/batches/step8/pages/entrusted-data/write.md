# write.md：entrusted-data

## 書いたファイル
- docs/safety/entrusted-data.md（stubs から移した。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：sections（`what-it-prevents`・`misconceptions` の 2 節を足した）、sources（既存の id 6 つ）、stage、updated
- 雛形・図・data/sources.d/entrusted-data.yml は置いていない（目次の templates と visual が「なし」。出典は data/sources.yml の既存 id だけで足りた）

## 必ず持つものの対応
- 原理・原因（principle「握る」・prevents「境界がない」）の名指し：`#what-it-prevents`
- pitfalls：空のため持たない
- level（整える）と要点の最初の項目「何が分かるか」：冒頭の囲み
- 構成の目安（場面 → 仕組み → 何に効くか → 誤解 → 関連）：`#whose-data`（場面と 2 つの契約）→ `#contracted-surfaces`・`#cloud-runs`（判断例 2 つ）→ `#what-it-prevents` → `#misconceptions` → 関連はテンプレート

## メインに判断してほしいこと
- `#misconceptions` の「オプトアウトしても、すでに学習に使われたデータは残る」は research/05 4-7 と research/26 §3.12 の写しに基づく。本文に日数・年数は書いていない
- コンペのデータの記述は、束の材料（research/11、類推・版依存）だけが根拠。印は（根拠：中・類推）にした。大会の規約は読んでいない

## 提案
- front matter・用語集・data への提案はなし

## 検査の結果
- check_page.py：1 回目 エラー 1（`front matter` の表記、prh）・警告 7、2 回目 エラー 0・警告 3
- 残した警告：no-doubled-joshi（助詞の重なり）3 件。読みにくくなく、直すと文が不自然になるため残した（55 行・62 行・123 行付近）

## 確かめていないこと
- 具体的な契約の条項、NDA・業務委託契約の実際の書き方（観点だけを書いた）
- 法令の解釈（書かない決めのため触れていない）
- Claude Code の認証方式と契約の側の対応（個人のアカウント＝個人向け、組織の契約や API の認証＝商用）は束の材料から組んだ。Claude Code の公式文書では照合していない
- アプリのタスクがクラウドで動くこと、クラウドセッションが隔離環境で動くことは束の材料（research/02・05）による。公式の原文では再確認していない
- Web の取得は 0 回

## 使用量
- 道具の呼び出し：約 12 回（Read 3、Bash 6、Write 2、Edit 7 を含めて概算）、Web の取得 0
