---
id: ask-for-outcomes
title: 細かく指図するか、成果で頼むか
aliases: [細かく指図せず、成果で頼む, 'Delegate, don''t dictate', 成果ベースで頼む, 狙いを指定して頼む]
type: concept
field: prompting
chapter: 何をどこまで頼むか
order: 90
level: 任せる
priority: 推奨
surfaces: [claude-code, app, api]
principle: [見せる, 確かめる]
prevents: [見えていない, 確かめていない]
scenes: [開発, コンテスト]
summary: 目的と完了の条件は測れる成果として渡し、どこを攻めるか・何で測るかは具体的に書く。成果だけを渡すと、指標だけを満たす変更や迷走が起きうる。
signs:
  - {type: goal, text: やり方まで指示せずに任せたい}
  - {type: symptom, text: 「スコアを上げて」と頼んだら、関係のない所をいじり続ける}
  - {type: symptom, text: 細かく指示したら、指示の外の問題を見落とした}
prerequisites: [four-specifics, define-done]
related: [share-targets-and-bounds, verifier-defines-problem, state-the-scope, evidence-not-reports, goal-until-done, performance-tuning, wont-rethink-approach]
sources: [cc-docs-best-practices, api-docs-prompting-best-practices, prussianblue-ahc054-claude-code, jitendrazaa-tips-code-tips-creator-boris]
volatility: 低
sections:
  - {title: 成果だけの依頼と指図だけの依頼を、同じ依頼で比べる, anchor: before-after}
  - {title: 成果で示すもの：目的と完了の条件, anchor: outcomes}
  - {title: 具体的に書くもの：対象と測り方, anchor: specifics}
  - {title: どこが詰まっているかは人か計測が決める, anchor: bottleneck}
  - {title: なぜ効くか、何に効くか, anchor: why}
  - {title: 効かない場面とやりすぎ, anchor: limits}
  - {title: 成果と対象を分けて書く雛形, anchor: templates}
stage: reviewed
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：目的と完了の条件は測れる成果として渡し、どこを攻めるか・何で測るかは具体的に書く。やり方は任せつつ、迷走を防げる
    - **いつ引くか**：やり方まで指示せずに任せたいとき。「スコアを上げて」と頼んだら関係のない所をいじり続けたとき。細かく指示したら指示の外の問題を見落としたとき
    - **まず足すもの**：成果だけの依頼なら、対象と測り方を足す。指図だけの依頼なら、完了の条件を足して、手順の指定を減らす。書き写せる型は[成果と対象を分けて書く雛形](#templates)にある
    - **関わる原理と原因**：原理は、対象と測り方を「見せる」ことと、完了を測って「確かめる」こと。防ぐ原因は、Claude 側の 6 つの原因のうち「見えていない」と「確かめていない」である
    - **前提**：<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end -->、<!-- link:begin define-done -->[「完了」を定義して渡す](../verify/define-done.md)<!-- link:end -->

<!-- textlint-disable -->
別名：細かく指図せず、成果で頼む・Delegate, don't dictate・成果ベースで頼む・狙いを指定して頼む
<!-- textlint-enable -->

細かく指図するか、成果で頼むかは、依頼のどこまでを手順で縛り、どこからを Claude に任せるかの決め方である。目的と完了の条件は成果として測れる形で渡し、どこを攻めるかの対象と、何で測るかは具体的に書く。成果だけを渡すと、指標だけを満たす変更や迷走が起きうる。

## 成果だけの依頼と指図だけの依頼を、同じ依頼で比べる {#before-after}

同じ性能改善の依頼を、手順で指図するだけの形、成果だけの形、成果と対象を分けた形で並べる。次は説明のために作った依頼の例で、Claude に試した結果ではない。

**Before（指図だけ）**

```text
src/report.py の build_rows の for ループをリスト内包表記に書き換えて、
行ごとの検索は dict に置き換えて、最後に整形の関数を 1 つにまとめて
```

**Before（成果だけ）**

```text
レポートの生成を速くして
```

**After（成果と対象を分ける）**

```text
目的：月次レポートの生成を速くしたい
完了：`pytest tests/report` が通り、`python bench/report_bench.py` の中央値が変更前より下がる
変えないもの：出力ファイルの内容（変更前と一致すること）
対象：計測では build_rows が最も遅い。まずそこを見る
やり方：任せる。手を入れる前に、変更前の計測値を報告する
```

After で足したものは 4 つある。1 つ目は、終わりを決める完了の条件。2 つ目は、変えてはならないもの。3 つ目は、攻める対象。4 つ目は、計測値を先に出す手順である。逆に、書き換え方の指定は外して、やり方を任せた。

指図だけの依頼は、指示した書き換えが的外れでも、そのまま実行されやすい。成果だけの依頼は、どこを触ってよいかが見えず、何をもって速くなったとするかも決まらない。公式の Best practices にも、"fix the login bug" のような曖昧な依頼を、症状・場所・確かめ方つきの依頼に書き換える対比表がある（[Best practices](https://code.claude.com/docs/en/best-practices)）。

## 成果で示すもの：目的と完了の条件 {#outcomes}

成果で示すものは、何のためにやるかという目的と、どうなれば終わりかという完了の条件である。手順は含まない。完了の条件は、コマンドと結果の形で書き、人が読み返さなくても合否が分かるようにする。完了の定義に入れるものの一覧は、<!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end -->が詳しい。

成果で頼む価値は、Claude が手順を選べることにある。手順を指図すると、指示した部分だけは正確に実行されるが、指示の外にある問題は見落とされやすい。実践者の紹介では、失敗している CI のテストを直すとき、変更内容を細かく指示せず、結果を指して頼む例が挙がっている（根拠：弱。単独の実践者の紹介で、前提として文脈の提供が要る）。

達成できる値や理論上の上界が分かっているなら、成果に目標値として書く。書かないと、少し良くなったところで止まりやすい。値の伝え方と、分からないときの測り方は<!-- link:begin share-targets-and-bounds#targets -->[目標値・上界を伝える › 目標値を書く](share-targets-and-bounds.md#targets)<!-- link:end -->にある。

任せる幅を広げる頼み方なので、見合う守りを先に決める。完了を測れること、報告ではなく証拠を受け取ることが、その守りである。証拠の形は<!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](../verify/evidence-not-reports.md#what-counts)<!-- link:end -->、完了するまでターンを続けさせる条件の書き方は<!-- link:begin goal-until-done#writing-conditions -->[/goal（完了するまで続けさせる） › 条件の書き方（終わりの状態・証明・変えないもの・上限）](../delegate/goal-until-done.md#writing-conditions)<!-- link:end -->にある。

## 具体的に書くもの：対象と測り方 {#specifics}

具体的に書くものは、どこを攻めるかという対象と、何で測るかという測り方である。成果だけを渡すと、Claude は「良くなった」と言える所を自分で探す。測り方が曖昧なら、関係のない所をいじり続けたり、指標だけを満たす変更に流れたりする。

対象は、ファイルや関数の名前、または処理の名前で書く。「スコアを上げて」ではなく、「この関数を高速化して」「この仕様のステップ 3 を実装して」のように、局所化した作業にして頼む。対象の書き方は<!-- link:begin four-specifics#target -->[具体性の 4 点（対象・状況・完了・手本） › 対象：どのファイル・どの画面か](four-specifics.md#target)<!-- link:end -->、完了の書き方は<!-- link:begin four-specifics#done -->[具体性の 4 点（対象・状況・完了・手本） › 完了：何が起きれば終わりか](four-specifics.md#done)<!-- link:end -->にある。やってはならない変更や触れてはならない範囲は<!-- link:begin state-the-scope#anti-goals -->[範囲を伝える（やらないこと） › やらないことを書く](state-the-scope.md#anti-goals)<!-- link:end -->に書く。

測り方は、測るコマンド、比べる条件、比べる回数まで書く。指標は、書いたとおりに最適化される。指標だけを満たす変更が出る仕組みは、<!-- link:begin verifier-defines-problem#why -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › 検証器に映ったものだけが目標になる](../eval/verifier-defines-problem.md#why)<!-- link:end -->が詳しい。

最適化コンテストの 1 つ（AHC054）を Claude Code で戦った参加者の体験記には、次のことが書かれている。参加者は、方針を自分で考えて 7 ステップの仕様書に落とした。「スコアを改善して」という依頼は効果が限られ、「この処理を高速化して」「多様性を持たせて」のように狙いの明確な依頼が効いた（根拠：弱。単独の体験記で、2025 年のモデルでのもの）。いまのモデルで同じになるとは限らないので、傾向の一例として読む。

## どこが詰まっているかは人か計測が決める {#bottleneck}

どこが詰まっているか、つまりボトルネックの特定は、人か計測が担う。Claude に「どこを直すべきか」から任せると、見やすい所や直しやすい所に手が伸び、本当に詰まっている所とは別の所に時間が使われやすい。

計測で分かっていない段階では、対象を決める前の仕事として計測を頼む。性能改善なら、プロファイルを先に取り、上位の候補を報告させ、その中から人が対象を選んで次の依頼に書く。手順は<!-- link:begin performance-tuning#profile-first -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › プロファイルを先に取る](../recipes/performance-tuning.md#profile-first)<!-- link:end -->にある。コンテストの解法なら、工程ごとの時間やスコアの内訳を測らせ、どこに余地があるかを人が決める。

!!! example "判断例：スコアが伸びない最適化コンテストの解法"
    - **状況**：練習の最適化問題で、自分の解法のスコアが伸びない。Claude Code に任せて時間を節約したい。
    - **迷う候補**：「スコアを改善して」と成果だけを渡す。または、「温度の設定を変えて、近傍を 1 つ足して」と手法まで指図する。どちらも筋が通る。
    - **選んだもの**：成果は「手元の入力の集合での合計スコアが、変更前より上がること」と書く。着手点は、まず工程ごとの内訳を測らせて報告させ、その結果を見て自分で選び、「この処理を高速化して」と局所化して頼む。
    - **理由**：成果だけでは、測り方に映る所を手当たり次第にいじる。手法の指図だけでは、指示の外にある詰まりを見落とす。内訳の計測が、どちらの失敗も防ぐ。コンテストでの AI の利用は、大会ごとの規則に従う。

## なぜ効くか、何に効くか {#why}

成果と対象を分けて書くと効くのは、依頼に書かれていないことが Claude に見えないからである。対象と測り方を書くのは、必要な情報を「見せる」ことにあたる。完了の条件を測れる形にするのは、結果を「確かめる」ことにあたる。

防ぐ原因は 2 つある。1 つ目は「見えていない」である。どこを攻めるか、何で測るかが依頼にないと、Claude は推測で埋める。2 つ目は「確かめていない」である。完了が曖昧だと、終わったように見えた所で止まるか、指標だけを満たして終わる。終わったように見えた所で止まる理由は<!-- link:begin define-done#why-it-stops -->[「完了」を定義して渡す › 終わったように見えた所で止まる](../verify/define-done.md#why-it-stops)<!-- link:end -->にある。

手順を書かないのは、手順を選ぶ力を使うためである。ただし、成果を渡すことは文脈を省くことではない。何のための作業か、守るべきものは何かといった文脈は、依頼に書く。

## 効かない場面とやりすぎ {#limits}

効かない場面とやりすぎには、次のものがある。

- **測れない成果**：完了を測るコマンドや採点がない場合、成果で頼んでも、人が見て確かめるしかない。先に測る手段を整える。検証器が誤っていれば、誤りも同じ速さで増える。これは<!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](../eval/verifier-defines-problem.md#loops-amplify)<!-- link:end -->で扱う
- **手順そのものが成果の場面**：規約で手順が決まっている作業や、順序を間違えると壊れる操作では、手順を指図する。成果で頼むのは、手順を選ぶ余地を任せてよい場面に限る
- **例外を許さない範囲**：触れてはならないものを依頼の言葉だけで守らせない。強制が要るものは、権限やフックで縛る。二層の考え方は<!-- link:begin state-the-scope#two-layers -->[範囲を伝える（やらないこと） › 例外を許さない範囲は仕組みで縛る（二層）](state-the-scope.md#two-layers)<!-- link:end -->にある
- **対象を絞りすぎ**：指定した対象が実は原因でないと、そこを直しても症状は残る。計測で外れと分かったら、対象を取り下げて測り直す
- **迷走が続くとき**：成果で任せたのに直し続けて進まないときは、続けるかやめるかを、先に決めた基準と測った上界で決める。判断は<!-- link:begin wont-rethink-approach#routes -->[直し続けて方針を疑わない（またはすぐ撤退を勧める） › 原因ごとの対処](../symptoms/wont-rethink-approach.md#routes)<!-- link:end -->にある

## 成果と対象を分けて書く雛形 {#templates}

次の雛形は、目的・完了・変えないもの・対象・測り方・やり方・止まる条件を欄に分けた依頼である。対象が分かっていないときは、欄の注に従い、まず計測を頼む。

<!-- gen:begin snippet ask-for-outcomes/outcome-request -->
<!-- textlint-disable -->

??? example "雛形：成果と対象を分けて書く依頼"

    ```text
    目的：<何を良くしたいか。1 文>
    完了：<実行するコマンドと、通るべき結果。目標値が分かっているなら値も書く>
    変えないもの：<出力の一致、公開しているインタフェース、既存のテストなど>
    対象：<計測や調査で分かっている着手点のパスと関数名。分かっていなければ「まず計測して、候補を報告して」と書く>
    測り方：<測るコマンドと、比べる条件と回数>
    やり方：任せる。ただし、対象が決まる前は編集せず、計測の結果（上位の候補）を報告する
    止まる条件：<完了に届かないとき、または測り方がおかしいと判断したときは、回避せず報告して止まる>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet ask-for-outcomes/outcome-request -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [AHC054参加記録 with Claude Code](https://prussianblue.hatenadiary.jp/entry/2025/09/29/223244)：PrussianBlue・確認日 2026-11-04
- [10 Claude Code Tips from the Creator Boris Cherny](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)：Jitendra Zaa・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)
- [「完了」を定義して渡す](../verify/define-done.md)

**次に読む**

- [目標値・上界を伝える](share-targets-and-bounds.md)

**関連**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [範囲を伝える（やらないこと）](state-the-scope.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- [性能改善を頼む（プロファイルが先・出力の一致と実測）](../recipes/performance-tuning.md)
- [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
