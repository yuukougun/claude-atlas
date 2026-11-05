---
id: build-test-harness
title: 検証環境・テスト基盤を作らせる
aliases: [テストハーネス, 評価環境, 入力の生成器, 並列のテストランナー, フィクスチャを作らせる]
type: recipe
field: recipes
chapter: 確かめる道具を作らせる
order: 120
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない]
scenes: [開発, コンテスト]
summary: 入力の生成・並列の実行・集計・比べる基準など、確かめるための環境を Claude に作らせる。できた環境は判定に使う前に既知の答えで確かめ、作業する側が書き換えられない場所に置く。
signs:
  - {type: goal, text: テストデータの生成器や、たくさんのケースを一度に回す仕組みを作らせたい}
  - {type: situation, text: 変更が良くなったかを、毎回同じ物差しで測る環境がない}
prerequisites: [verifier-three-conditions]
related: [verifier-defines-problem, test-the-verifier, freeze-eval-assets, lockbox-and-holdout, differential-testing, measure-changes, experiment-log, evaluators-by-format, misses-broken-evaluation, build-observation-tools, pitfalls-of-ai-written-tests]
sources: []
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guard-first}
  - {title: 何を作らせるか, anchor: what-to-build}
  - {title: 作った環境を確かめる, anchor: check-the-harness}
  - {title: 検証の資産を分けて置く, anchor: separate-eval-assets}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：入力の生成・並列の実行・集計・基準との比較など、確かめる環境を Claude に作らせ、既知の答えで確かめてから使える。
    - **いつ引くか**：テストデータの生成器や、たくさんのケースを一度に回す仕組みを作らせたいとき。変更が良くなったかを毎回同じ物差しで測る環境がないとき。
    - **前提**：<!-- link:begin verifier-three-conditions -->[検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)<!-- link:end -->

<!-- textlint-disable -->
別名：テストハーネス・評価環境・入力の生成器・並列のテストランナー・フィクスチャを作らせる
<!-- textlint-enable -->

検証環境・テスト基盤を作らせるとは、確かめるための道具一式（入力の生成器、並列の実行、集計、比べる基準）を Claude に書かせることである。こうした道具は量が多く手で書くと遅いが、Claude は速く作れる。一方で、できた環境が誤っていれば、以降の判定がすべて誤る。作らせる前に守りを決め、作らせた後に確かめ、置き場所で縛る。この順で進める。

## 先に整える守り {#guard-first}

環境を作らせる前に、3 つを人が決める。Claude は渡された検証の仕組みが定める問題を解くので、仕組みに映らないものは目標にならない。この性質は <!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](../eval/verifier-defines-problem.md#loops-amplify)<!-- link:end --> が持つ。

1. 何を勝ちとみなすか。採点の定義と、公式の道具に当たる部分は人が決める。Claude に作らせるのは、それを回す道具である。
2. 入力が本番を代表しているか。手元の勝ちが本番の勝ちを意味するかは、<!-- link:begin verifier-three-conditions#representative -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 本番を代表する](../eval/verifier-three-conditions.md#representative)<!-- link:end --> で点検する。
3. 環境のどこを Claude が書き換えてよいか。環境の誤りは、気づかれないまま大量の判定に混ざる。点検の仕方は <!-- link:begin verifier-three-conditions#audit -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 三条件を点検する](../eval/verifier-three-conditions.md#audit)<!-- link:end --> にある。

この 3 つが決まらないまま環境を作らせると、動く環境はできても、何を測っているかが分からない。凍結の前に整えることの全体は、<!-- link:begin freeze-eval-assets#before-freezing -->[評価資産を凍結し、触れる範囲を絞る › 凍結の前に整えること](../enforce/freeze-eval-assets.md#before-freezing)<!-- link:end --> が持つ。

## 何を作らせるか {#what-to-build}

Claude に作らせる環境の部品は 5 つある。コンテストでは評価器（ローカルのテスタ）、業務ではテスト基盤やフィクスチャに当たる。コンテストのリポジトリの分け方を業務へ当てはめる点は類推である（類推）。

| 部品 | 役目 |
| --- | --- |
| 入力の生成器 | 種を引数に取り、同じ種で同じ入力を出す |
| 基準 | 何もしない解、愚直解、旧実装、基準のボットなど、比べる相手 |
| 並列の実行 | たくさんのケースを一度に回し、失敗も記録する |
| 集計 | 結果を合計・最悪ケース・失敗の一覧にまとめる |
| 補助 | 可視化、模擬サーバ、異常系のテストなど |

手順は次のとおりである。各段に、何で終わったかの確かめを付ける。

1. 入力の生成器を作らせる。種を引数に取らせ、小さい値・境界・同値だらけ・最大付近を一定の割合で混ぜさせる。確かめ：同じ種で 2 回出して入力が一致するか。小さい種の入力は人が眺めて偏りを見る。分布の見方については、<!-- link:begin test-the-verifier#input-distribution -->[検証器そのものを確かめる（red/green・手で計算したケース） › 入力の生成器の分布を人が見る](../eval/test-the-verifier.md#input-distribution)<!-- link:end --> が持つ。
2. 基準を作らせる。何もしない解と、愚直解か旧実装を、本解と同じ仕組みで回せるようにする。確かめ：基準の出力が、同じ入力で毎回同じになる。突き合わせの作り方は <!-- link:begin differential-testing#steps -->[答えの分かる遅い解と比べる（差分テスト・オラクル） › 手順](../eval/differential-testing.md#steps)<!-- link:end --> が持つ。
3. 並列の実行を作らせる。実行ごとに出力先を分けさせ、失敗した件は止めずに記録させる。並列で動かすと、一時ファイルや出力先が衝突しやすい。確かめ：回した件数と結果の件数が一致する。同じ種の再実行が同じ結果になる。
4. 集計を作らせる。合計だけでなく、最悪ケースと失敗した件の一覧を出させる。合計だけでは、一部の層の悪化が隠れる（見方は <!-- link:begin measure-changes#by-stratum -->[変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)<!-- link:end --> が持つ）。確かめ：手で計算した小さいケースと集計が一致する。
5. 実験ごとの記録の置き場を作らせる。仮説・設定・結果・採否を残す形は <!-- link:begin experiment-log#flow -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 実験 1 件の流れ](../eval/experiment-log.md#flow)<!-- link:end --> が持つ。確かめ：1 件の実験が、記録だけから再現できる。

形式ごとに、環境が何に当たるかは違う。テスタ・ベンチマーカー・交差検証・対戦場の違いは <!-- link:begin evaluators-by-format -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](../contest/evaluators-by-format.md)<!-- link:end --> が持つ。結論を出させる代わりに、可視化や集計の道具を作らせる使い方は <!-- link:begin build-observation-tools -->[観察の道具を作らせる（可視化・集計・ログ）](build-observation-tools.md)<!-- link:end --> にある。

次の依頼は、手順の 1 から 4 と、完成後の確かめまでをまとめて頼む型である。確かめの 3 点を依頼に入れておくと、環境が動いたというだけの報告で終わりにくい。

<!-- gen:begin snippet build-test-harness/build-harness-request -->
<!-- textlint-disable -->

???+ example "雛形：検証環境を作らせる依頼の雛形（既知の答えで確かめるところまで頼む）"

    ```text
    〔対象〕の変更が良くなったかを測る検証環境を作って。次の順で進め、各段の終わりに何で確かめたかを示して。
    1. 〔入力の仕様〕を満たす入力の生成器 harness/gen.py を作る。種を引数に取り、同じ種なら同じ入力になること。小さい値・境界・同値だらけ・最大付近を一定の割合で混ぜる。
    2. 基準を作る。何もしない解と、〔愚直解か旧実装〕を同じ仕組みで回せるようにする。
    3. 〔N〕件を並列で回す harness/run_parallel.sh を作る。実行ごとに出力先を分け、失敗した件は止めずに記録する。
    4. 結果を集める harness/aggregate.py を作る。合計だけでなく、最悪ケースと失敗した件の一覧も出す。

    作った環境は、判定に使う前に次を確かめて。
    - 何もしない解は負け、明らかに強い解は勝つこと
    - 手で計算した小さいケース 5 つで、集計が cases/hand/ の期待値と一致すること
    - わざとバグを入れた環境のコピーでは、確かめが落ちること。その出力を見せて

    禁止: tools/official/ と cases/hand/ と brute/ を書き換えること。環境の側を本解に合わせて直すこと。確かめが通らないときは直さず、原因の仮説を報告して。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet build-test-harness/build-harness-request -->

## 作った環境を確かめる {#check-the-harness}

作らせた環境は、判定を始める前に、答えの分かっている入力を使って確かめる。確かめる作業は Claude に作らせてよい。ただし出力は、自分で実行して見る。確かめる点は 3 つである。

1. 何もしない解とランダムな解は負け、明らかに強い解は勝つ。環境が弱い解を勝たせるなら、集計か比べ方が壊れている。手順は <!-- link:begin test-the-verifier#red-green -->[検証器そのものを確かめる（red/green・手で計算したケース） › red/green を検証器に当てる](../eval/test-the-verifier.md#red-green)<!-- link:end --> が持つ。
2. 手で計算できる小さい入力を与えたとき、環境の出す値が人の計算と一致する。期待値は人が書く。Claude に書かせると、環境の癖が期待値に写る。<!-- link:begin test-the-verifier#hand-calculated -->[検証器そのものを確かめる（red/green・手で計算したケース） › 手で計算したケース](../eval/test-the-verifier.md#hand-calculated)<!-- link:end --> を参照する。
3. わざとバグを入れた環境のコピーで、確かめが落ちる。落ちないなら、その確かめは環境の誤りを見つけられない。<!-- link:begin test-the-verifier#broken-copy -->[検証器そのものを確かめる（red/green・手で計算したケース） › わざと壊した検証器で落ちるか](../eval/test-the-verifier.md#broken-copy)<!-- link:end --> を参照する。

対戦型なら、先後を入れ替えた同じボット同士の勝率が 0.5 からずれないことも見る。

確かめが通っても、テストの強さが足りないことはある。通るだけのテストの見分け方は <!-- link:begin pitfalls-of-ai-written-tests#test-strength -->[AI に書かせたテストの落とし穴 › テストの強さを確かめる](../verify/pitfalls-of-ai-written-tests.md#test-strength)<!-- link:end --> が持つ。

!!! example "判断例：全件通った並列ランナー"
    - **状況**：Claude に並列のテストランナーを作らせた。回すと全件が通り、報告も「問題なし」である。
    - **迷う候補**：そのまま凍結して以降の判定に使う。あるいは、わざと壊した本解を回し、落ちるかを先に見る。
    - **選んだもの**：壊した本解を回して、落ちるかを先に見る。
    - **理由**：全件が通る結果は、本解が正しいときだけでなく、ランナーが失敗を拾えていないときにも出る。落ちる場面を一度見ておけば、通った結果に意味が付く。

## 検証の資産を分けて置く {#separate-eval-assets}

確かめた環境は、作業する Claude が書き換えられない場所に置く。解を直す作業の最中に、テストや採点の側も書き換えられると、通ることが正しさを意味しなくなる。そこで、リポジトリを「Claude が書いてよいもの」と「読むだけのもの」に分ける。

<!-- gen:begin snippet build-test-harness/repo-layout -->
<!-- textlint-disable -->

??? example "雛形：検証の資産を分けたリポジトリの構成例"

    ```text
    eval-repo/
      CLAUDE.md                    # 触れてよい範囲、回し方、採否と理由の記録の場所
      solution/                    # 解（書き換えてよい。パラメータは引数か設定で渡す）
      tools/official/              # 公式の道具（読み取り専用）
      brute/                       # 愚直解（遅くても明らかに正しい。読み取り専用）
      cases/hand/                  # 手で計算したケースと期待値（人が書く。読み取り専用）
      harness/                     # 環境の本体（確かめてから凍結する）
        gen.py                     #   入力の生成器（種を引数に取る）
        run_parallel.sh            #   並列の実行
        aggregate.py               #   集計（最悪ケースと失敗の一覧を含む）
      tests/proposed/              # Claude が新しく書いたテスト（人が見るまで凍結の外）
      tests/frozen/                # 人が見て移したテスト（読み取り専用）
      experiments/
        〔日付〕-〔名前〕/            # 実験ごと：仮説・設定・結果・採否（Claude が書いてよい）
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet build-test-harness/repo-layout -->

分け方の考え方は次のとおりである。

- 書いてよいのは、解と、実験ごとの記録である。
- 読むだけにするのは、公式の道具、愚直解、手で計算したケース、確かめて凍結した環境である。
- 新しく書かせたテストは、凍結の外の置き場に作らせる。人が見てから、凍結側へ移す。
- 開発用・検証用・人だけが持つ検証用データの三層に入力を分ける考え方は、<!-- link:begin lockbox-and-holdout#three-tiers -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 三層に分ける](../eval/lockbox-and-holdout.md#three-tiers)<!-- link:end --> が持つ。

読むだけにする方法は、このページでは書かない。例外を許さない規則は、CLAUDE.md の文ではなく設定の仕組みで止める。凍結の対象は <!-- link:begin freeze-eval-assets#what-to-freeze -->[評価資産を凍結し、触れる範囲を絞る › 凍結するものと触らせるもの](../enforce/freeze-eval-assets.md#what-to-freeze)<!-- link:end --> が、設定で止める方法は <!-- link:begin freeze-eval-assets#how-to-freeze -->[評価資産を凍結し、触れる範囲を絞る › 設定で止める（権限ルール・サンドボックス・ファイルの権限）](../enforce/freeze-eval-assets.md#how-to-freeze)<!-- link:end --> が持つ。止めた後に効いているかは <!-- link:begin freeze-eval-assets#check -->[評価資産を凍結し、触れる範囲を絞る › 凍結が効いているかを確かめる](../enforce/freeze-eval-assets.md#check)<!-- link:end --> で確かめる。

## 失敗したとき {#when-it-fails}

- 確かめが通らない：環境の側を直すか、期待値を人が見直す。環境を本解に合わせて直させない。原因が分からないときは、仮説を Claude に報告させる。確かめ方の全体は <!-- link:begin test-the-verifier#when-it-fails -->[検証器そのものを確かめる（red/green・手で計算したケース） › 失敗したとき](../eval/test-the-verifier.md#when-it-fails)<!-- link:end --> にある。
- 手元の評価は良いのに本番で通用しない：<!-- link:begin misses-broken-evaluation -->[手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)<!-- link:end --> で、正しさ・書き換え・代表性のどれが崩れているかを切り分ける。
- 環境を Claude が書き換えていた：<!-- link:begin freeze-eval-assets#when-it-fails -->[評価資産を凍結し、触れる範囲を絞る › 失敗したとき](../enforce/freeze-eval-assets.md#when-it-fails)<!-- link:end --> で、止める設定を見直す。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)

**関連**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- [評価資産を凍結し、触れる範囲を絞る](../enforce/freeze-eval-assets.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)
- [答えの分かる遅い解と比べる（差分テスト・オラクル）](../eval/differential-testing.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](../contest/evaluators-by-format.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [観察の道具を作らせる（可視化・集計・ログ）](build-observation-tools.md)
- [AI に書かせたテストの落とし穴](../verify/pitfalls-of-ai-written-tests.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
