---
id: check-the-metric
title: 評価指標そのものを確かめる
aliases: [指標のずれ, 評価指標の選び方, 手元の指標と本番の指標]
type: concept
field: eval
chapter: 検証器を作る
order: 70
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [データ分析, コンテスト, 開発]
summary: 検証器が測る指標と本当の目的のずれを、最適化を始める前に確かめられる。指標が良いことは、正しいことを意味しない。
signs:
  - {type: symptom, text: 上げさせた指標が、本当に上げたかったものとずれていた}
  - {type: goal, text: 最適化させる指標が、本当に欲しいものと合っているか確かめたい}
prerequisites: [verifier-defines-problem]
related: [verifier-three-conditions, define-done, suspect-too-good-results, measure-changes, lockbox-and-holdout, data-analysis, read-specs-yourself, misses-broken-evaluation]
tracks: []
outdated_advice: []
sources: [lukyanenko-kaggle-antigravity-s6e7, openai-expanding-on-sycophancy, cvpr-2023-why-is-the-winner-the-best]
volatility: 低
sections:
  - {title: 指標と目的のずれ, anchor: mismatch}
  - {title: Claude は指標のずれを直さない, anchor: why}
  - {title: 最適化の前に指標を確かめる, anchor: check}
  - {title: 何に効くか, anchor: what-it-affects}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：最適化を任せる前に、検証器の指標と本当の目的の合い方を、人が確かめる見方。指標が良いことは、正しいことを意味しない。
    - **いつ引くか**：上げさせた指標が、本当に上げたかったものとずれていたとき。最適化させる指標が、本当に欲しいものと合っているかを確かめたいとき。
    - **前提**：<!-- link:begin verifier-defines-problem -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する）](verifier-defines-problem.md)<!-- link:end -->

<!-- textlint-disable -->
別名：指標のずれ・評価指標の選び方・手元の指標と本番の指標
<!-- textlint-enable -->

評価指標そのものを確かめるとは、検証器の返す数字が本当に欲しいものを測っているかを疑うことである。検証器の中身が正しくても、測るものが目的とずれていれば、Claude は数字を上げたまま目的から離れる。この確認は、最適化を始める前に、人が行う。

## 指標と目的のずれ {#mismatch}

指標は、検証器が返す数字である。目的は、その数字を上げた先で本当に欲しいものである。2 つが同じに見えるあいだは問題にならない。ずれは、最適化を進めてから表に出る。

事例を 3 つ挙げる。

- **手元の指標が競技の指標と違った例**：Kaggle のあるコンペの実践者の報告である。設定とデータの確認（EDA）は accuracy で行われ、競技の指標は balanced accuracy だった。交差検証（CV）は 0.967 で、公開リーダーボード（LB）は 0.874 だった（根拠：弱。単独の実践者の報告）。
- **数字が良いまま出して、戻した例**：2025 年 4 月、OpenAI は GPT-4o の迎合的な更新を出した。オフライン評価と A/B テストの数字が良かったため、専門のテスターの懸念を押し切って出し、後にロールバックした。OpenAI 自身が公表している（根拠：強。一次資料）。この例は他社のモデルの話であり、現行の Claude の傾向を示すものではない。示すのは、数字が良いという判断が、そのまま正しさの判断にはならないという点である。
- **指標を設計に入れた勝者の例**：IEEE ISBI 2021 と MICCAI 2021 の医用画像コンペ 80 件を、勝者の側から分析した研究（CVPR 2023）がある。上位チームに共通した戦略の 1 つは、評価指標を手法の設計に反映することだった（根拠：中。観察研究で、因果は主張されていない）。

3 つに共通するのは、数字を作る側が、数字の意味を最後まで確かめていなかったことである。1 つ目は、Claude に渡す完了の定義と本当の目的がずれる落とし穴と同じ形をしている（類推）。完了の定義の中身は <!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end --> を参照する。

## Claude は指標のずれを直さない {#why}

Claude は、渡された検証器に映るものを目標にして反復する。検証器が accuracy を返すなら、accuracy を上げる変更が残る。目的とのずれは、検証器に映らないので、反復の中では誰も気づかない。この仕組みの説明は <!-- link:begin verifier-defines-problem#why -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › 検証器に映ったものだけが目標になる](verifier-defines-problem.md#why)<!-- link:end --> を参照する。

反復が多いほど、指標を上げる変更だけが選ばれて積み重なる。指標が目的の近似にすぎないなら、近似の誤差もその分だけ大きくなる。人が最初に確かめなければ、ずれは最後の報告まで残る。

ここで握るのは、何を上げるかを決める権限である。Claude に指標の候補や弱点を挙げさせるのはよい。決めるのは、目的を知っている人である。

## 最適化の前に指標を確かめる {#check}

指標を確かめる順は次のとおり。どれも、反復を始める前に済む。

1. **目的を 1 文で書く**：数字ではなく、成功したときに何が起きるかを書く。書けなければ、まだ指標を選べない。
2. **指標を最大にする悪い答えを考える**：指標は満たし、目的は外す出力を考える。ほぼ全部を多数派のクラスと答えるだけで accuracy が高くなる、のような形である。
3. **指標の定義を原文で読む**：式・集計の単位・除外される入力を、評価の資料と評価のコードで確かめる。要約でなく原文を読む。方法は <!-- link:begin read-specs-yourself#read-first -->[仕様を自分で読み、AI に誤読を指摘させる › 先に自分で読んで要約する](../recipes/read-specs-yourself.md#read-first)<!-- link:end --> にある。
4. **指標が使われる場所を並べる**：設定・データの確認・開発中の検証・最終の評価が、同じ指標を使っているかを一覧にする。Kaggle の例では、ここが食い違っていた。
5. **手元の値と本番側の小さな実測を並べる**：本番に近いデータで数字を取り直す。生データでの裏取りは <!-- link:begin data-analysis#check-raw-data -->[データを分析する › 生データで裏を取る](../recipes/data-analysis.md#check-raw-data)<!-- link:end --> を参照する。見せない検証用のデータの分け方は <!-- link:begin lockbox-and-holdout#three-tiers -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 三層に分ける](lockbox-and-holdout.md#three-tiers)<!-- link:end --> を参照する。
6. **完了の定義に、指標と目的を両方書く**：指標が目標、目的が満たすべき条件、という分担にする。

2 と 4 は、Claude に一覧を出させると速い。次の依頼は、実装を始めさせずに、指標の確認だけを出させる。出てきた一覧は候補であり、正しいかどうかは人が原文で確かめる。

<!-- gen:begin snippet check-the-metric/metric-check-request -->
<!-- textlint-disable -->

??? example "雛形：最適化の前に指標を確かめさせる依頼"

    ```markdown
    最適化を始める前に、評価指標を確かめたい。実装や改善はまだ始めず、次を順に出してほしい。

    1. 指標の定義。式・集計の単位・除外される入力を、評価のコードと資料から書き出す。
    2. この指標を最大にするが、下の「本当の目的」を満たさない出力の例を 3 つ。
    3. 設定・データの確認・開発中の検証・最終の評価で、同じ指標を使っているかの一覧。違う所があれば、そこを先に報告する。
    4. 指標と目的がずれる点の候補。それぞれ、どう確かめるかの手順をつける。

    指標を変えてよいかは、私が決める。候補を出すだけにして、評価のコードと資料は書き換えない。

    本当の目的：<最終的に何がうまくいけば成功か>
    評価のコードと資料：<パスや URL>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet check-the-metric/metric-check-request -->

同じ依頼でも、「指標を上げて」とだけ頼むと、指標の定義は確かめられないまま反復が始まる。上の依頼は、実装の前に定義と使われ方の一覧を出させ、指標を変える権限を人に残す点が違う。

業務の想定の場面で考える。

!!! example "判断例：緊急の問い合わせを見つける分類器"
    - **状況**：問い合わせを「緊急」と「通常」に分ける分類器を、Claude に反復させて改善している。緊急は全体のごく一部で、検証器は accuracy を返す。
    - **迷う候補**：accuracy のまま反復させ、最後に別の指標を見る案。反復の前に、緊急の見逃しを測る指標を足す案。
    - **選んだもの**：反復の前に、緊急の見逃しを測る指標を足し、accuracy は副指標にする。
    - **理由**：緊急は少ないので、ほぼ全部を「通常」と答えても accuracy は高い。最後に気づくと、反復の結果を捨てることになる。一方、最初から目的を測る指標を足すのは安い。

## 何に効くか {#what-it-affects}

この確認は、原理の「握る」と「確かめる」に関わる。何を上げるかの決定は人が握り、その決定が目的と合うかを、最適化の前に人が確かめる。

防ぐ原因は「確かめていない」である。指標が目的と合っているかが未確認のまま、反復を回す状態を防ぐ。

効く範囲は狭い。隣のページと分担する。

- 検証器の全体の条件（正しい・書き換えられない・本番を代表する）は <!-- link:begin verifier-three-conditions#representative -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 本番を代表する](verifier-three-conditions.md#representative)<!-- link:end --> にある。このページは、そのうち測るものの側だけを扱う。
- 手元の評価は良いのに本番で通用しない、という症状から入るなら <!-- link:begin misses-broken-evaluation#diagnosis -->[手元の評価は良いのに本番で通用しない › 原因を安く確かめる順](../symptoms/misses-broken-evaluation.md#diagnosis)<!-- link:end --> から原因を切り分ける。
- 反復の結果が良すぎるときの疑い方は <!-- link:begin suspect-too-good-results#what-to-suspect -->[良すぎる結果を疑う › まず疑うもの](../verify/suspect-too-good-results.md#what-to-suspect)<!-- link:end --> にある。
- 変更が効いたかを前後で測る手順は <!-- link:begin measure-changes#by-stratum -->[変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](measure-changes.md#by-stratum)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- **指標が上がったのだから、良くなった**：上がったのは指標であり、目的ではない。2 つが一致するかは、別に確かめる。
- **指標を複数見れば安全**：複数の指標が同じずれを共有していれば、すべて外れる。たとえば、どれも全体の正解率の言い換えなら、少数派の見逃しはどの数字にも映らない。
- **一度確かめれば終わり**：目的や、本番の入力の傾向が変われば、前に確かめた指標も合わなくなる。目的を変えたときは、1 から見直す。
- **Claude に指標を選ばせればよい**：候補と弱点を挙げさせるのはよいが、本当の目的を知っているのは人である。選ぶのは人に残す。
- **指標を直せば、確認は終わる**：指標を直した後も、検証器が正しいか、書き換えられないかは別に残る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Starting and iterating on a Kaggle competition in Google Antigravity](https://andlukyane.com/blog/kaggle-antigravity-s6e7)：Andrey Lukyanenko・英語・確認日 2026-11-04
- [Expanding on what we missed with sycophancy](https://openai.com/index/expanding-on-sycophancy/)：OpenAI・英語・確認日 2026-11-05
- [Why Is the Winner the Best?](https://cvpr.thecvf.com/virtual/2023/poster/21260)：CVPR 2023・英語・確認日 2026-11-05

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](verifier-defines-problem.md)

**関連**

- [検証器の三条件（正しい・書き換えられない・本番を代表する）](verifier-three-conditions.md)
- [「完了」を定義して渡す](../verify/define-done.md)
- [良すぎる結果を疑う](../verify/suspect-too-good-results.md)
- [変更が効いたかを測る（小さな eval）](measure-changes.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](lockbox-and-holdout.md)
- [データを分析する](../recipes/data-analysis.md)
- [仕様を自分で読み、AI に誤読を指摘させる](../recipes/read-specs-yourself.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
