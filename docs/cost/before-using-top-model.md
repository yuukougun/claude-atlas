---
id: before-using-top-model
title: 最上位のモデルを使う前に
aliases: [Fable を使う前に, 最上位のモデルの料金, Fable の上限, Fable の使用量]
type: concept
field: cost
chapter: プランと支払い
order: 50
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [合っていない]
pitfalls: []
summary: 最上位のモデルは、プランの枠との関係がほかのモデルと違い、使用量の減りも速いことが分かる。使う前に、どの枠や支払いから引かれるかと、本当に要る仕事かを確かめる。
signs:
  - {type: goal, text: いちばん高性能なモデルを使ってみたい}
  - {type: symptom, text: 上位のモデルを少し使っただけで、残りの枠が大きく減った}
prerequisites: [how-usage-limits-work, choosing-a-model]
related: [usage-credits-basics, choosing-a-plan, current-models#fable-and-mythos, what-uses-up-limits, harness-over-model]
tracks: [plans, usage-limits, usage-credits]
outdated_advice: []
sources: [hc-fable-models-plan, claude-pricing, hc-max-plan, hc-ultra-plan, hc-pro-plan, hc-usage-credits, hc-usage-limits]
volatility: 高
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: どの枠から引かれるか（プランごとの表）, anchor: which-limit}
  - {title: 使う価値がある仕事, anchor: when-worth-it}
  - {title: 何に効くか（原理と防ぐ原因）, anchor: what-it-prevents}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：最上位のモデルは、プランによって枠に含まれるか usage credits から引かれるかが違い、使用量も速く減る。
    - **いつ引くか**：いちばん高性能なモデルを使ってみたいとき。上位のモデルを少し使っただけで、残りの枠が大きく減ったとき。
    - **前提**：<!-- link:begin how-usage-limits-work -->[利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)<!-- link:end -->・<!-- link:begin choosing-a-model -->[モデルの選び方（三段階）](../models/choosing-a-model.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Fable を使う前に・最上位のモデルの料金・Fable の上限・Fable の使用量
<!-- textlint-enable -->

最上位のモデルを使う前に確かめることは 2 つある。どの枠や支払いから引かれるかと、その仕事に本当に要るかである。最上位のモデルは入れ替わるので、このページはモデルの名前で呼ばず、今どれにあたるかは <!-- link:begin current-models#fable-and-mythos -->[現行モデルの一覧と位置づけ › Fable と Mythos](../models/current-models.md#fable-and-mythos)<!-- link:end --> で確かめる。

## 何が起きるか {#what-happens}

最上位のモデルを、ほかのモデルと同じ感覚で使うと、予想より早く枠が減るか、思わぬ支払いが出る。プランによって、起きることが分かれる。

- **枠に含まれるプラン**：使った分は、ほかのモデルと同じ通常の週の上限から引かれる。ほかのモデルより速く減る。含まれるのは上限の一部までなので、数日試しただけで、ほかのモデルで使える残りも細る。
- **枠に含まれないプラン**：最初から usage credits で使う。1 回目の依頼から従量課金が始まる。
- **API**：プランの枠とは関係なく、標準の API 料金で請求される。

どれも「少し試しただけ」で効く。公式は「ほかのモデルより速く減る」とだけ書き、倍率は公表していない（[Claude Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)）。速く減る理由も、公式は説明していない。だから、減り方は自分の口座で見て確かめる。

## どの枠から引かれるか（プランごとの表） {#which-limit}

引かれる先は、プランで 4 通りに分かれる。Team と Enterprise では、席の種類（premium seat と standard seat）で分かれる。次の分け方は、公式の記事で 2026-11-05 に確かめた。

- **プランの枠に含まれる**：Max、<!-- name:begin max-20x-to-ultra -->Ultra<!-- name:end -->、Team と席ごとの Enterprise の premium seat。通常の週の上限の内側で、一部まで使える。上限の一部まで使い終えたら、usage credits で続けるか、別のモデルに替える。
- **usage credits から引かれる**：Pro、Team と席ごとの Enterprise の standard seat。席ごとの Enterprise では、組織が usage credits を有効にしている必要がある。
- **標準の API 料金**：使用量に基づく Enterprise と API。
- **使えない**：Free。

プランに含まれる最上位のモデルの割合は、通常の週の上限のうち <!-- fact:begin top-model-weekly-share -->50%（料金のページは「半分まで」）（2026-11-05 時点）<!-- fact:end --> である。各プランの上限の大きさは、このページに書かない。プランの比べ方は <!-- link:begin choosing-a-plan#plan-table -->[プランの選び方 › プランの表（確認日つき）](choosing-a-plan.md#plan-table)<!-- link:end --> で確かめる。

!!! warning "公式の書き方が食い違っている"
    - 料金のページは「週上限の半分まで」と書く。
    - Max と Ultra の記事は「別の週の上限がある」と書く。
    - 最上位のモデルの記事は「別の週の上限はなく、通常の週の上限の内側」と書く。
    - このページは、最上位のモデルの記事に合わせて「通常の週の上限の内側」と書く。含まれる分は追加の枠ではない。別枠かどうかは、残りの表示で自分の口座を見て確かめる。

残りと減り方を見る場所は、面で違う。

=== "アプリ"

    Settings > Usage の進捗バーで、残りを見る。見る場所の一覧は <!-- link:begin how-usage-limits-work#where-to-check -->[利用上限の仕組み（面をまたいで共有する枠） › 残りを見る場所](how-usage-limits-work.md#where-to-check)<!-- link:end --> にある。

    usage credits から引かれるプランでは、使う前に Settings > Usage で usage credits を有効にし、月の上限額と通知を決める。決め方は <!-- link:begin usage-credits-basics#set-a-cap -->[usage credits（上限を超えた分の従量課金） › 上限額と通知を決める](usage-credits-basics.md#set-a-cap)<!-- link:end --> にある。

=== "Claude Code"

    `/usage` で、使用量の内訳を見る。読み方は <!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> にある。

    アプリと Claude Code は同じ枠を分け合う。アプリで試した分も、Claude Code の残りから減っている。最上位のモデルを Claude Code で選ぶには、最低の版が要る。要る版は、<!-- fact:begin top-model-claude-code-min-version -->モデル 5 は 2.1.170、モデル 5.1 は 2.1.255（モデルの世代ごと）（2026-11-05 時点）<!-- fact:end --> である。古い版では選べないことがある。

=== "API"

    プランの枠とは別に、使ったトークンの量に応じて標準の API 料金で請求される。API の rate limits はプランの枠とは別の仕組みで、違いは <!-- link:begin how-usage-limits-work#shared-limit -->[利用上限の仕組み（面をまたいで共有する枠） › 面をまたいで一つの枠](how-usage-limits-work.md#shared-limit)<!-- link:end --> にある。

## 使う価値がある仕事 {#when-worth-it}

最上位のモデルに替えるのは、既定のモデルで足りず、effort を上げても足りなかった仕事に限る。順番は <!-- link:begin choosing-a-model#three-steps -->[モデルの選び方（三段階） › 三段階：既定 → effort → 上位のモデル](../models/choosing-a-model.md#three-steps)<!-- link:end --> の 3 段階に従う。公式の推奨も、迷ったら下位のモデルから始め、モデルを替える前に effort を調整するというものである（公式の立場）。

この辞典の推奨は、替える前に次の 4 つを確かめることである。

1. **引かれ先**：自分のプランで、どの枠か usage credits かを、「どの枠から引かれるか」の節で確かめる。
2. **残り**：枠から引かれるなら、週の残りと、ほかの作業に要る量を見る。usage credits から引かれるなら、月の上限額を先に決める。
3. **効果**：同じ仕事を、既定のモデルと最上位のモデルで、自分の評価で比べる。比べ方は <!-- link:begin choosing-a-model#verify -->[モデルの選び方（三段階） › 替えた効果の確かめ方](../models/choosing-a-model.md#verify)<!-- link:end --> にある。
4. **原因の切り分け**：差が出ないときや、出ても小さいときは、モデルではなく検証の手段・渡す文脈・指示が原因のことがある。モデルの差より先に、<!-- link:begin harness-over-model#when-harness-matters -->[モデルの差よりハーネスの差 › 差がハーネスから来るとき](../models/harness-over-model.md#when-harness-matters)<!-- link:end --> を見る。

!!! example "判断例：Pro で最上位のモデルを試す"
    - **状況**：Pro のプランで、大きなリファクタリングを最上位のモデルに任せたい。
    - **迷う候補**：最初から大きな仕事をまるごと任せる。小さな 1 か所で試して、効果と減り方を見てから広げる。
    - **選んだもの**：小さな 1 か所で試す。
    - **理由**：Pro では最初から usage credits の支払いになる。大きな仕事をまるごと任せると、効果が分からないまま費用だけが先に出る。小さな 1 か所なら、同じ仕事を既定のモデルでも試せるので、差が出るかを見て続けるかを決められる。月の上限額も、試す前に決めておく。

!!! example "判断例：Max の週の途中で最上位のモデルを使う"
    - **状況**：Max のプランで、週の半ばに、長い調査と難しい修正を続けて頼みたい。
    - **迷う候補**：どちらの作業も最上位のモデルで通す。難しい修正の段だけ最上位のモデルにし、調査は既定のモデルで行う。
    - **選んだもの**：難しい修正の段だけ最上位のモデルにする。
    - **理由**：最上位のモデルは通常の週の上限から速く引かれ、含まれる分は一部までである。調査にも使うと、週の後半にほかのモデルの分まで足りなくなる。モデルの組み合わせ方は <!-- link:begin current-models#combine -->[現行モデルの一覧と位置づけ › 系統の組み合わせ方](../models/current-models.md#combine)<!-- link:end --> にある。

軽い作業に最上位のモデルを使うのは、仕事に対してモデルが重すぎる使い方である。効果は変わらないのに、使用量だけが増える。

## 何に効くか（原理と防ぐ原因） {#what-it-prevents}

このページの考え方は、原理「確かめる」と、原因「合っていない」に結び付く。原因は 6 つの原因（<!-- link:begin six-causes -->[失敗の二つの軸と診断の入口](../start/six-causes.md)<!-- link:end -->）の 1 つである。

原因「合っていない」とは、選んだモデルや枠が、その仕事と自分の使い方に合っていないことである。最上位のモデルでは、次の形で出る。

- **枠が合っていない**：プランの枠に含まれると思って使ったら、usage credits から引かれていた。または、含まれる分を使い切って、ほかのモデルの残りまで細った。
- **仕事が合っていない**：既定のモデルで足りる仕事に、最上位のモデルを使い、使用量だけが増えた。

どちらも、原理「確かめる」で防ぐ。使う前に引かれ先を確かめ、使った後に減り方と効果を確かめる。大きな減り方の原因が最上位のモデルとは限らない。全体の要因は <!-- link:begin what-uses-up-limits#causes -->[上限を早く使う要因 › 枠を早く減らす原因](what-uses-up-limits.md#causes)<!-- link:end --> で見る。

## よくある誤解 {#misconceptions}

- **プランに含まれるなら、使い放題である**：違う。通常の週の上限の内側で、一部までである。ほかのモデルより速く減る。
- **含まれる分は、週の上限に足される追加の枠である**：違う。公式は、追加の枠ではないと書く。ほかのモデルと同じ上限を分け合うので、合計は上限を超えない。
- **有料のプランなら、どれでも枠の中で使える**：違う。Pro と standard seat は、枠に含まれず、最初から usage credits の支払いになる。Free では使えない。
- **減る倍率は調べれば分かる**：公式は倍率を公開していない。自分の口座の減り方で見る。
- **いちばん高性能なら、いつも最上位のモデルがよい**：決まらない。仕事の重さに合わせる。差は自分の仕事で比べて決める。
- **モデルの名前を覚えれば、いつまでも通じる**：通じない。最上位のモデルは入れ替わり、引かれ先の決まりも変わる。今の扱いは、公式の記事の確認日で見直す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Claude Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)：Anthropic・英語・確認日 2026-11-04
- [Plans & pricing](https://claude.com/pricing)：Anthropic・英語・確認日 2026-11-04
- [What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)：Anthropic・英語・確認日 2026-11-04
- [What is the Ultra plan?](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan)：Anthropic・英語・確認日 2026-11-04
- [What is the Pro plan?](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)：Anthropic・英語・確認日 2026-11-04
- [Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)：Anthropic・英語・確認日 2026-11-04
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)
- [モデルの選び方（三段階）](../models/choosing-a-model.md)

**関連**

- [usage credits（上限を超えた分の従量課金）](usage-credits-basics.md)
- [プランの選び方](choosing-a-plan.md)
- [現行モデルの一覧と位置づけ › Fable と Mythos](../models/current-models.md#fable-and-mythos)
- [上限を早く使う要因](what-uses-up-limits.md)
- [モデルの差よりハーネスの差](../models/harness-over-model.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
