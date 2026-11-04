---
id: summary-overgeneralization
title: 要約は原文より強く言いがち（過度な一般化）
nav_title: 要約は原文より強く言いがち
aliases: [過度な一般化, overgeneralization]
type: concept
field: basics
chapter: 答えの確かさ
order: 140
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない]
scenes: [調べもの, 文章, コンテスト]
summary: AI の要約は、原文の条件や限定を落として主張の範囲を広げがちだと分かる。「正確に」と頼んでも直らないことがあるので、要約を根拠に使う前に原文と照らす理由になる。
signs:
  - {type: goal, text: AI の要約をそのまま根拠に使ってよいか判断したい}
prerequisites: []
related: [summary-overstates-source, fact-checking, checking-citations, research-and-reports, read-specs-yourself, learning-with-ai, why-hallucinations]
sources: [arxiv-2504-00025, qiita-kmat67916008-d7586a]
volatility: 低
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: 研究が示したこと, anchor: study}
  - {title: なぜ起きるか, anchor: why}
  - {title: 競技の例：上位解法の前提が落ちる, anchor: contest}
  - {title: 何に効くか, anchor: what-helps}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：AI の要約は、原文の条件や限定を落として主張の範囲を広げがちだと分かる。
    - **いつ引くか**：AI の要約をそのまま根拠に使ってよいか、判断したいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：過度な一般化・overgeneralization
<!-- textlint-enable -->

要約は原文より強く言いがち（過度な一般化）は、AI が要約するときに、原文にあった条件や限定を落として、主張を広く言い切ってしまう傾向を指す。書かれた一文ずつは間違っていなくても、要約全体が原文より強い主張になる。このページは、その傾向の中身と、根拠に使う前に原文と照らす理由を説明する。

## 何が起きるか {#what-happens}

要約の中で、原文の「条件つきの結果」が「一般的な事実」に変わる。次の例は、この辞典が説明のために作った仮の例である。

!!! example "例：限定が落ちる要約"
    - **原文**：「小規模なデータセットで、この手法は精度を 3 ポイント改善した。大規模なデータでは検証していない。」
    - **要約**：「この手法は精度を改善する。」
    - **落ちたもの**：小規模なデータセットという条件と、大規模なデータでは未検証という限定。

要約の文は、原文のどの一文とも矛盾しない。だから読み流すと気づけない。変わったのは、主張が成り立つ範囲である。

## 研究が示したこと {#study}

この傾向は、科学論文の要約を使った研究で測られている。以下は 2025 年の arXiv の論文（査読前）の結果で、対象は当時のモデルである（以下、この研究と呼ぶ）。

- 10 の LLM が書いた科学論文の要約 4,900 件を、それぞれ原文と比べた。
- DeepSeek・ChatGPT-4o・LLaMA 3.3 70B は、26〜73% の割合で原文より広く一般化した。
- LLM の要約は、人が書いた要約より、一般化しすぎる確率が約 4.85 倍だった。
- 「正確に」と頼んでも、広い一般化は直らず、悪化したと報告されている。
- 新しいモデルの一般化の正確さは、古いモデルより低い傾向があった。

（根拠：中。大規模な実験だが、査読前の 1 本の研究で、領域は科学論文の要約に限られる）

この結果を、現行の Claude の傾向として読んではならない。この研究の対象は 2025 年当時の 10 のモデルで、いまのモデルが同じ割合で起こすかは、この辞典では確かめていない。確かめられるのは、自分の資料と自分のモデルで、要約を原文と照らした結果だけである。

## なぜ起きるか {#why}

要約は、短くするために情報を捨てる作業である。捨てる候補のうち、「ただし小規模の場合に限る」「この条件のときのみ」のような限定は、文の中心の主張より先に削れやすい。主張の骨格だけが残ると、結果は一般論に見える。

（推論・実践例なし：この研究は一般化が起きる割合を測ったもので、モデルの内部で何が起きているかは示していない。ここは、要約の性質からの説明である）

原文を書いた人は、限定をわざわざ書くことで自分の主張を守っている。要約者は限定を「重要だ」と判断しないと残せない。短くまとめるほど、残す余地は減る。人の要約者にも同じ傾向はあるが、この研究では LLM のほうが約 4.85 倍起こしやすかった。

## 競技の例：上位解法の前提が落ちる {#contest}

要約の一般化は、競技プログラミングの解説や上位解法の記事でも起きうる。コンペの実践者の記事に、次の指摘がある。上位解法の手法は問題の前提にも縛られるので、手法だけでなく「なぜその問題で効いたか」まで読む必要がある（根拠：弱。単独の実践者の記事）。AI の要約は、この前提を落とした「手法の一覧」にしやすい（類推：科学論文の要約の研究の結果を、解説の要約に当てはめた推論）。

落ちた前提に気づかずに別の問題へ手法を移すと、効かない手法を試すことになる。上位解法を要約させる場面の注意は <!-- link:begin learning-with-ai#summaries-of-solutions -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 上位解法や解説を AI に要約させるとき](../judgment/learning-with-ai.md#summaries-of-solutions)<!-- link:end --> が持つ。

## 何に効くか {#what-helps}

このページの知識が働く先は、原理の「確かめる」と、原因の「確かめていない」である。

原因の「確かめていない」とは、要約を読んで納得し、原文に戻らないまま、その内容を根拠にしてしまうことを指す。要約が一般化している分だけ、根拠が実際より強く見える。だから、要約は「原文のどこを読むかの目次」として使い、根拠にするのは原文の記述にする。

- 要約を根拠にする前に、結論の文ごとに、原文でその文が成り立つ条件を探す。照らし方は <!-- link:begin fact-checking#summaries -->[事実を確かめる（引用・照合・best-of-N） › 要約を原文と照らす](../verify/fact-checking.md#summaries)<!-- link:end --> にある。
- 要約が原文より断定的になったと気づいたとき、落ちた条件を見つける順は <!-- link:begin summary-overstates-source#diagnosis -->[要約が原文より断定的になる › 原因を安く確かめる順](../symptoms/summary-overstates-source.md#diagnosis)<!-- link:end --> にある。
- 引用や出典の細部を確かめる手順は <!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end --> にある。
- 調べものの結論を出典の原文で確かめる流れは <!-- link:begin research-and-reports#check-sources -->[調べものとレポート › 出典を原文で確かめる](../recipes/research-and-reports.md#check-sources)<!-- link:end --> にある。
- 仕様のように誤読が高くつく原文は、先に自分で読んで要約する。方法は <!-- link:begin read-specs-yourself#read-first -->仕様を自分で読み、AI に誤読を指摘させる › 先に自分で読んで要約する（準備中）<!-- link:end --> にある。

!!! example "判断例：要約をどこまで根拠にするか"
    - **状況**：論文を AI に要約させ、「この手法は精度を改善する」と読めた。自分の課題にこの手法を入れるか決めたい。
    - **迷う候補**：要約のまま採用を決める。または、原文で実験の条件を確かめてから決める。どちらも筋が通る。要約を読むほうが速く、手法が合わなければ後で外せる。
    - **選んだもの**：原文の実験の条件（データの規模・対象・比較相手）だけを読み、自分の課題と合うかを確かめてから決める。
    - **理由**：外すのが安い試しなら要約でもよい。しかし採用が他の作業の前提になるなら、落ちた条件の見落としが後で高くつく。原文全体でなく、条件の部分だけを読めば、確かめる手間は小さい。

## よくある誤解 {#misconceptions}

「正確に要約して」と頼めば直る、は誤解である。この研究では、正確さを頼んでも広い一般化は直らず、悪化したと報告されている。頼み方の工夫より、原文と照らす確かめを仕組みに入れる。

人が書いた要約なら安全、も誤解である。人の要約にも一般化はある。ただし LLM の要約のほうが起こしやすいと報告されている。

一文ずつ事実を確かめれば足りる、も誤解である。要約の各文が原文と矛盾しなくても、主張の範囲は広がりうる。範囲の確かめは、文の真偽の確かめとは別の作業になる。

作り話のハルシネーションと同じ現象、も違う。ハルシネーションは原文にない内容を作る問題である。ここで扱うのは、原文にある内容の範囲が広がる問題で、原因も確かめ方も違う。ハルシネーションの仕組みは <!-- link:begin why-hallucinations#what-happens -->[ハルシネーションはなぜ起きるか › 何が起きるか](why-hallucinations.md#what-happens)<!-- link:end --> を見る。

新しいモデルに替えれば直る、とも言えない。この研究では、新しいモデルの正確さのほうが低い傾向があった。これは当時のモデルの結果で、いまのモデルは確かめていない。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Generalization Bias in Large Language Model Summarization of Scientific Research](https://arxiv.org/abs/2504.00025)：arXiv（Peters, Uwe ほか）・英語・確認日 2026-11-04
- [Kaggle画像コンペでやっていること④](https://qiita.com/Kmat67916008/items/d7586a28e6ec8595d579)：Qiita（Kmat67916008）・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)
- 仕様を自分で読み、AI に誤読を指摘させる（準備中）

**関連**

- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [引用や出典の確かめ方](../verify/checking-citations.md)
- [調べものとレポート](../recipes/research-and-reports.md)
- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- [ハルシネーションはなぜ起きるか](why-hallucinations.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
