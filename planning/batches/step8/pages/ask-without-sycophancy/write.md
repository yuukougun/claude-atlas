# write.md：ask-without-sycophancy

## 書いたファイル
- docs/judgment/ask-without-sycophancy.md（stub から移動。stage を draft、updated を 2026-11-05、sources を既存の id 9 件、sections に what-happens・example・what-you-keep の 3 節を足した。既存 5 節の anchor は変えていない）
- snippets/ask-without-sycophancy/compare-blind.md と .expect.yaml（並べて比べる。業務向けの言い換えを同じ雛形に入れた）
- snippets/ask-without-sycophancy/critique-my-plan.md と .expect.yaml（自分の案の批評）
- data/sources.d/ask-without-sycophancy.yml は作っていない（出典は data/sources.yml の既存の id だけで足りた）

## 必ず持つものの対応
- 判断例（状況・迷う候補・選んだもの・理由の 4 行）：#example
- 要点以外の構成の目安（何が起きるか→なぜ→判断例→握るもの→確かめ方）：何が起きるか #what-happens／なぜ（人の側の仕組み）#what-happens の後半と #hide-preferences／判断例 #example／握るもの・確かめ方 #what-you-keep
- level：front matter（整える）

## メインに判断してほしいこと
- Truth Decay（arxiv-2503-11656、7 回目の追撃で 76.74% → 30.23%）を（根拠：弱）で #what-happens に載せた。research/24 B-44 の確認の範囲に入っていないので、載せるか判断してほしい
- Jin & Chen（arxiv-2603-00539、26.2% → 73.2%）は 10 第19章の数値のまま載せた。B-40 のような訂正はないが、一次資料では確かめていない

## 提案
- front matter・用語集・data への提案はなし

## 検査の結果
- check_page.py を 2 回流した。1 回目はエラー 0・警告 9（読点・助詞・文の長さ・「一つ」）、直した後はエラー 0・警告 0

## 確かめていないこと
- 研究の数値は束の写しに基づく。SycEval・Kim & Khashabi・コードスメルの研究は B-44・B-40 の範囲、それ以外は一次資料を開いていない
- 公式のベストプラクティスと、モデル別の指針（Opus 5・Sonnet 5）の記述は、束の写しのとおりに書いた。原文を開いていない（Web の取得は 0 回）
- サブエージェントの新しい文脈（親の会話を引き継がない・fork は引き継ぐ・CLAUDE.md が入る）は data の features の note による。動作を試していない
- 2 つの雛形は動作を確かめていない。Chiang・Drosos の研究は束のとおり確かめていないので、本文に書いていない
- 最新の Claude の迎合の割合は測っていない。#what-you-keep に、自分で測る手順として書いた

## 使用量
- 道具の呼び出し：約 20 回、Web の取得：0 回
