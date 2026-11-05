---
id: share-targets-and-bounds
title: 目標値・上界を伝える
aliases: [目標スコアを書く, 理論上の上界を伝える, 達成できる値を伝える]
type: concept
field: prompting
chapter: 何をどこまで頼むか
order: 100
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [見せる, 確かめる]
prevents: [見えていない]
scenes: [開発, データ分析, コンテスト]
summary: 達成できる値や理論上の上界が分かっていれば依頼に書くと、早く打ち切ったり「限界です」と言ったりしにくくなる。分からないときは、先に上界を測る。
signs:
  - {type: goal, text: 最適化を、目標の値に届くまで粘らせたい}
  - {type: symptom, text: 最適化を頼むと、早々に打ち切る}
  - {type: situation, text: 性能改善やスコアを競う課題を任せている}
prerequisites: [ask-for-outcomes]
related: [measure-the-upper-bound, performance-tuning, wont-rethink-approach, blames-the-tools, measure-changes, format-cheatsheet]
sources: [anthropic-research-ai-resistant-technical-evaluations, drivendata-ai-agents-data-science-competitions]
volatility: 低
sections:
  - {title: 目標値を書く, anchor: targets}
  - {title: 上界が分からないときは測る, anchor: measure}
  - {title: 目標値と上界を書く雛形, anchor: templates}
  - {title: なぜ効くか、何に効くか, anchor: why}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：達成できる値や理論上の上界が分かっていれば依頼に書くと、早く打ち切ったり「限界」と言い出したりしにくくなる。分からないときは、先に上界を測る。
    - **いつ引くか**：最適化を、目標の値に届くまで粘らせたいとき。最適化を頼むと、早々に打ち切るとき。性能改善やスコアを競う課題を任せているとき。
    - **根拠の強さ**：中〜弱である。事例が 1 件と、別分野の単独の実験が 1 件で、どちらも目標値の有無を同じ条件で比べた実験ではない。
    - **関わる原理と原因**：原理は、到達点を「見せる」ことと、届いたかを「確かめる」こと。防ぐ原因は、Claude 側の 6 つの原因のうち「見えていない」である。
    - **前提**：<!-- link:begin ask-for-outcomes -->[細かく指図するか、成果で頼むか](ask-for-outcomes.md)<!-- link:end -->

<!-- textlint-disable -->
別名：目標スコアを書く・理論上の上界を伝える・達成できる値を伝える
<!-- textlint-enable -->

目標値・上界を伝えるとは、最適化の依頼に、どこまで届けば終わりなのかを値で書くことである。目標値は届かせたい値を指し、上界は理論上どこまで届くかの限界の値を指す（時間のように小さいほどよい指標では、下限がそれに当たる）。どちらも Claude からは見えないので、分かっているなら書き、分からないなら先に測る。

## 目標値を書く {#targets}

目標値を書くとは、最適化を頼むときに、いまの値と届かせたい値と、その値の出どころを依頼に入れることである。次は説明のために作った依頼の例で、Claude に試した結果ではない。

**Before（目標がない）**

```text
recommend_items の処理が遅いので、速くして
```

**After（目標と出どころを足した）**

```text
recommend_items の処理時間を短くしてほしい。
測り方は `python bench.py` の中央値で、いまは <現在の値>、目標は <目標の値> だ。
目標の値は、同じ入力で参照実装が出している値である。
届くまで続け、難しいと判断したときは、試したことと理由を添えて報告して
```

After で足したのは、次の 4 つである。

- **目標の値**：打ち切る基準が「少し良くなった」から「届いたか」に変わる。
- **出どころ**：参照実装の実測、別の手法で出ている値、計算した上限や下限のどれかを書く。届くと分かる値だと伝わる。
- **測り方**：何で測るかは、<!-- link:begin ask-for-outcomes#specifics -->[細かく指図するか、成果で頼むか › 具体的に書くもの：対象と測り方](ask-for-outcomes.md#specifics)<!-- link:end -->に沿って具体的に書く。
- **難しいと判断したときの報告**：黙って止まらず、試したことと理由を返させる。

届くまで続けさせる依頼は、任せる幅を広げる。守りとして、届いたという報告だけで受け取らず、変更前後の出力の一致と実測を求める。やり方は<!-- link:begin performance-tuning#same-output-and-timing -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › 出力の一致と実測を証拠にする](../recipes/performance-tuning.md#same-output-and-timing)<!-- link:end -->にある。

根拠は 2 つある。1 つ目は、DrivenData のデータサイエンス競技でのエージェントの実験（2026 年の記事）である。目標スコアを書かないと、エージェントは少し学習しただけで止まりがちだった（根拠：中・類推）。単独の実験で、使われたモデルはこの辞典では確かめていない。最適化の依頼への当てはめは類推である。

2 つ目は、Anthropic が 2026 年 1 月に公開した性能エンジニアリングの採用課題の記事である。公開前の Claude Opus 4.5 を Claude Code で動かしたところ、合格の基準に届いた後、メモリ帯域の壁を越えられないと判断して止まった。書き手が達成できるサイクル数を伝えると、しばらく考えて回避の工夫を見つけた（根拠：中。1 件の事例）。目標値の有無を比べた実験ではなく、旧世代や別の課題の傾向とも言えない。

## 上界が分からないときは測る {#measure}

上界が分からないときは、推測で書かずに、先に測る。推測の値を書くと、実際より低い値で止まったり、届かない値を追わせたりする（推論）。

測り方の骨子は次の 3 つである。手順の全体は<!-- link:begin measure-the-upper-bound -->上界を測って「限界です」を反証する（準備中）<!-- link:end -->にある。

1. 条件を緩めた版を決める。たとえば、相手が何もしない場合、時間が無制限の場合、情報がすべて分かる場合である。
2. 緩めた版を、本番と同じ評価器で測る。
3. 出た値を「上界の目安」として依頼に書く。実現できる値とは限らないと添える。

この測り方は、制限時間を延ばして高速化の価値を測るコンテストの実践を一般化した推論で、直接の出典はない（推論・実践例なし）。上界の目安は保証ではなく、Claude の「限界です」を確かめる材料として使う。

性能改善では、緩めた版の前に、遅い箇所を確かめるのが先である。<!-- link:begin performance-tuning#profile-first -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › プロファイルを先に取る](../recipes/performance-tuning.md#profile-first)<!-- link:end -->を先に行い、ボトルネックと見える箇所が本当にそうかを測る。

!!! example "判断例：スコアの最適化を任せたら、数回で「これ以上は難しい」と返ってきた"
    - **状況**：スコアを競う課題の改善を任せたところ、数回の改善の後に「これ以上は難しい」と報告された。参照になる値はまだない。
    - **迷う候補**：いまの最良の値より少し高い値を、手元の感覚で目標値として書く。または、先に緩めた版を測って上界の目安を出す。
    - **選んだもの**：先に緩めた版を測り、その値を上界の目安として添えたうえで、目標の値を決める。
    - **理由**：根拠のない目標は、届かない値を追わせるか、低すぎて早く止まる原因になる。測った値があれば、「難しい」が上界の近くで出た判断かどうかを、その場で比べられる。

## 目標値と上界を書く雛形 {#templates}

目標の値、出どころ、測り方、難しいと判断したときの報告の 4 点を、書き写せる形にしたものが次の雛形である。山かっこの所を埋めて使う。

<!-- gen:begin snippet share-targets-and-bounds/target-and-bound-request -->
<!-- textlint-disable -->

??? example "雛形：目標値と上界を添えて最適化を頼む依頼"

    ```markdown
    <対象> の <指標> を改善してほしい。

    測り方：<測るコマンド>。同じ入力で <回数> 回走らせた中央値を見る。
    いまの値：<現在の値>
    目標の値：<目標の値>
    目標の出どころ：<参照実装の実測・別の手法で出ている値・計算した理論上の下限や上限 のどれか>
    出力は変更前と一致させる。

    目標の値に届くまで続けてほしい。「これ以上は難しい」と判断したときは、次の 3 点を添えて報告する。

    1. 何を試し、それぞれ測ると何が変わったか
    2. 難しいと考える理由（ボトルネックと見ている箇所と、その確かめ方）
    3. 目標の値との差が、その理由で説明できるか

    目標の値に届いたら、測った結果と、変更前後の出力が一致した確認を出して終える。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet share-targets-and-bounds/target-and-bound-request -->

## なぜ効くか、何に効くか {#why}

効く理由は、Claude の側から見ると、到達点が見えていないことにある。「速くして」という依頼では、どこまで進めば終わりかが依頼から分からない。改善が出た時点で終わりに見える（推論）。

関わる原理と原因は、次の 2 点である。

- **見せる（原理）**：目標の値と出どころを依頼に書くと、到達点が Claude に見える。防ぐ原因は、6 つの原因のうち「見えていない」である。
- **確かめる（原理）**：測り方と目標の値を揃えると、届いたかを機械的に確かめられる。「限界です」と返ってきたときも、上界の目安と比べて確かめられる。

「限界です」と言い出したときの切り分けは、<!-- link:begin wont-rethink-approach#diagnosis -->[直し続けて方針を疑わない（またはすぐ撤退を勧める） › 原因を安く確かめる順](../symptoms/wont-rethink-approach.md#diagnosis)<!-- link:end -->にある。目標値は、その診断の前に依頼へ入れておける予防である。

## 効かない場面とやりすぎ {#limits}

目標値と上界は、書けば必ず粘るというものではない。効かない場面とやりすぎは、次のとおりである。

- **目標の値に根拠がない**：出どころのない高い値は、届かない値を追わせる。出どころを書けない値は、目標でなく上界の目安として添える。
- **届かない目標で指標だけが動く**：目標に届かせたい圧力は、指標だけを満たす変更を呼びうる。<!-- link:begin performance-tuning#same-output-and-timing -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › 出力の一致と実測を証拠にする](../recipes/performance-tuning.md#same-output-and-timing)<!-- link:end -->を証拠に求め、極端に良い結果は<!-- link:begin performance-tuning#too-good-speedups -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › 良すぎる速度向上を疑う](../recipes/performance-tuning.md#too-good-speedups)<!-- link:end -->で疑う。
- **打ち切りの原因が目標値でない**：同じ直し方を続けて方針を疑わないときは、目標値を足しても変わらない。<!-- link:begin wont-rethink-approach -->[直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)<!-- link:end -->の診断に回す。
- **上界の目安を事実として扱う**：緩めた版の値は実現できるとは限らない。目安として書き、実現できるかは測って決める。
- **効果の大きさを約束する**：根拠は中〜弱で、事例が 1 件と別分野の単独の実験にとどまる。変更が効いたかは、<!-- link:begin measure-changes -->[変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)<!-- link:end -->で自分の課題について確かめる。

形式ごとの効き方の違いは、<!-- link:begin format-cheatsheet#performance-tuning -->[コンテストの形式別の早見表（AI の効き方と人が握るところ） › 性能改善](../contest/format-cheatsheet.md#performance-tuning)<!-- link:end -->にまとまっている。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Designing AI resistant technical evaluations](https://www.anthropic.com/research/AI-resistant-technical-evaluations)：Anthropic・英語・確認日 2026-11-04
- [AI Agents in Data Science Competitions: Lessons from the Leaderboard](https://blog.drivendata.org/blog/ai-agents-data-science-competitions)：DrivenData・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [細かく指図するか、成果で頼むか](ask-for-outcomes.md)

**関連**

- 上界を測って「限界です」を反証する（準備中）
- [性能改善を頼む（プロファイルが先・出力の一致と実測）](../recipes/performance-tuning.md)
- [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [コンテストの形式別の早見表（AI の効き方と人が握るところ）](../contest/format-cheatsheet.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
