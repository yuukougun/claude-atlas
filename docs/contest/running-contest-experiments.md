---
id: running-contest-experiments
title: 実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数）
nav_title: 実験の回し方
aliases: [ローカル評価の回し方, 勝率の判定, パラメータ調整]
type: recipe
field: contest
chapter: 評価と実験
order: 60
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: [体感を信じる]
scenes: [コンテスト]
summary: 結果のぶれを見込んでケース数と集計の方法を決め、パラメータの調整と勝率の判定を、誤差に負けない試合数で回す手順が分かる。
signs:
  - {type: symptom, text: 改善したはずの版が、ケースを増やすと負ける}
  - {type: goal, text: 勝率が本当に上がったのか、何試合やれば言えるか知りたい}
  - {type: goal, text: AI にパラメータの探索を回させたい}
prerequisites: [experiment-log, evaluators-by-format]
related: [selection-pressure, measure-changes#by-stratum, lockbox-and-holdout, open-ended-loop-trap, compare-hypotheses-in-parallel, parallel-and-loop-costs, decide-when-to-quit, suspect-too-good-results, progress-logs-for-long-jobs]
tracks: []
outdated_advice: []
sources: [terry-ahc040, kiri8128-relative-score-ahc, nvidia-winning-kaggle-competition-generative-ai]
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 手順の流れ, anchor: steps}
  - {title: ぶれるならケースを増やす, anchor: more-cases}
  - {title: 集計の方法を選ぶ（相対スコア）, anchor: aggregation}
  - {title: 勝率に要る試合数, anchor: games-for-win-rate}
  - {title: パラメータは入力の性質ごとに, anchor: parameters-by-input}
  - {title: 効かなかった実験も残す, anchor: keep-all-runs}
  - {title: 確かめ方, anchor: check}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：結果のぶれを見込んでケース数と集計の方法を決め、パラメータの調整と勝率の判定を、誤差に負けない試合数で回せる。
    - **いつ引くか**：改善したはずの版が、ケースを増やすと負けるとき。勝率が本当に上がったのか、何試合やれば言えるか知りたいとき。AI にパラメータの探索を回させたいとき。
    - **前提**：<!-- link:begin experiment-log -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)<!-- link:end -->、<!-- link:begin evaluators-by-format -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](evaluators-by-format.md)<!-- link:end -->

<!-- textlint-disable -->
別名：ローカル評価の回し方・勝率の判定・パラメータ調整
<!-- textlint-enable -->

実験の回し方は、手元の評価器で 2 つの版を比べるときの、ケースの数と集計と試合数の決め方をまとめた手順のページである。実験の一般の規律（台帳・選択圧・ロックボックス）は eval の分野のページが持つので、ここは大会での数え方に絞る。

## 先に整える守り {#guards}

実験を回す前に、比べる物差しと記録の置き場を整える。整えないまま数を増やしても、ぶれは減るが、物差しのずれは直らない。

- **評価器が公式の採点と合っている**：手元のスコアが公式とずれていると、ケースを増やしても、ずれた方向へ最適化する。
    - ヒューリスティックの評価器は <!-- link:begin evaluators-by-format#tester -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › ヒューリスティック：公式とスコアが一致するテスタ](evaluators-by-format.md#tester)<!-- link:end --> が持つ。
    - 対戦型の評価器は <!-- link:begin evaluators-by-format#arena -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › 対戦型：対戦場と基準のボット](evaluators-by-format.md#arena)<!-- link:end --> が持つ。
- **仮説と検証器の版を、実行の前に台帳へ書く**：結果を見てからの後付けを防ぐ。
    - 仮説の書き方は <!-- link:begin experiment-log#hypothesis-first -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 仮説を先に書く](../eval/experiment-log.md#hypothesis-first)<!-- link:end --> が持つ。
    - 検証器の版の残し方は <!-- link:begin experiment-log#verifier-version -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 検証器の版を残す](../eval/experiment-log.md#verifier-version)<!-- link:end --> が持つ。
- **選び続ける圧力を知っておく**：良かった版を選び続けるだけで、手元の入力に合わせ込んでしまう。
    - 防ぎ方は <!-- link:begin selection-pressure#defenses -->[選択圧：良かった版を選び続ける罠 › 防ぎ方](../eval/selection-pressure.md#defenses)<!-- link:end --> が持つ。
    - 節目の確認に使う入力を人が持つ分け方は <!-- link:begin lockbox-and-holdout#three-tiers -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 三層に分ける](../eval/lockbox-and-holdout.md#three-tiers)<!-- link:end --> が持つ。
- **AI に回させる範囲を縛る**：回させてよいのは、探す範囲・評価器・止める条件が決まった反復に限る。
    - 閉じた反復と開いたループの区別は <!-- link:begin open-ended-loop-trap#closed-vs-open -->[AI に改善を回させ続ける罠（開いたループ） › 閉じた反復と開いたループ](../delegate/open-ended-loop-trap.md#closed-vs-open)<!-- link:end --> が持つ。
    - 回数と本数が増えたときの費用の上限は、始める前に決める。決め方は <!-- link:begin parallel-and-loop-costs#decide-before-starting -->[並列・ループ・workflows のコスト › 始める前に決める三つ](../cost/parallel-and-loop-costs.md#decide-before-starting)<!-- link:end --> が持つ。

## 手順の流れ {#steps}

実験は、次の順に回す。各段に、何で終わったかの確かめを付けた。

1. **比べる 2 つの版と、入力の一覧（seed）を固定する**。終わりの確かめ：同じ版を 2 回走らせて、結果が一致するか、ぶれる幅が分かる。
2. **ぶれの大きさから、ケース数を決める**。終わりの確かめ：見たい差が、ぶれの幅より大きい。詳しくは「ぶれるならケースを増やす」の節。
3. **集計の方法を決める**。終わりの確かめ：本番の順位の点と、手元の集計が同じ向きに動く。詳しくは「集計の方法を選ぶ（相対スコア）」の節。
4. **対戦型は、試合数を始める前に決める**。終わりの確かめ：見分けたい勝率の差に対して、決めた試合数が足りている（目安は差の 2 乗の逆数。計算は節で示す）。詳しくは「勝率に要る試合数」の節。
5. **パラメータは、入力の性質ごとに調整する**。終わりの確かめ：調整に使っていない seed で、層ごとに差が残る。詳しくは「パラメータは入力の性質ごとに」の節。
6. **結果を、改善しなかった実験も含めて残す**。終わりの確かめ：後で別の集計に変えても、残した結果から再計算できる。詳しくは「効かなかった実験も残す」の節。

## ぶれるならケースを増やす {#more-cases}

結果がぶれるなら、ケースを増やす。ヒューリスティック系の上位者の経験則として、上達するにつれて 1 回の実行で 2,000〜5,000 ケースも珍しくなくなる（根拠：弱）。AHC040 の解説には、手法を 1,000 ケースで比べて、約 0.1% の差を判定したとある（根拠：弱。自己申告）。数字はどちらも、その人の問題と実行時間での経験で、そのまま自分の大会のケース数にはならない。

増やす理由は、ぶれの大きさがケース数の平方根に反比例して小さくなることにある。seed ごとのスコア差の標準偏差を `s`、ケース数を `n` とすると、平均の差の標準誤差は `s / √n` である。ケース数を 4 倍にすると、標準誤差は半分になる。見たい差を `d` とすると、95% 区間の半幅 1.96 × `s / √n` が `d` を下回る `n`（約 (1.96 × `s` / `d`)² 以上）が要る。`s` は、最初に走らせた数十ケースの差から測って見積もる。`s` と `d` は同じ単位（スコアそのもの、または相対値）でそろえる。

1 回の実行の時間が長いときは、ケースを並列で走らせる。費用は本数と回数と 1 回の文脈の大きさの掛け算で膨らむので、始める前に上限を決める。掛け算の中身は <!-- link:begin parallel-and-loop-costs#multiplication -->[並列・ループ・workflows のコスト › 費用が膨らむ掛け算](../cost/parallel-and-loop-costs.md#multiplication)<!-- link:end --> が持つ。

走らせる実行器と集計は、Claude Code に作らせられる。評価器を書き換えさせず、同じ seed で全部を走らせ、実行ごとに別の結果ファイルを作らせるのがこつである。依頼の例は次のとおり。

<!-- gen:begin snippet running-contest-experiments/runner-request -->
<!-- textlint-disable -->

??? example "雛形：同じ入力で 2 つの版を比べる走らせ方と集計を作らせる依頼"

    ```markdown
    手元の評価器で、2 つの版を同じ入力で比べる実験の走らせ方と集計のスクリプトを作ってほしい。今回は作るだけで、探索や改善はしない。

    前提：

    - 比べる版は、`./bots/base` と `./bots/candidate` の 2 つとする
    - 評価器（テスタ・対戦場）は `./tester/` にあるものを使う。このディレクトリの中身は読むだけで、書き換えない
    - 入力は seed の一覧ファイル `seeds.txt` から読む。seed の一覧は作ったあとで変えない

    作るもの：

    1. 2 つの版を、同じ seed で全部走らせるスクリプト。対戦型なら、同じ seed で先手と後手を入れ替えた 2 試合を 1 組にする
    2. 1 件ごとの結果（seed・版・スコアまたは勝敗・実行時間）を、実行ごとに別のファイル `results/<実行の ID>.csv` へ書く。既存のファイルには追記しない
    3. 集計のスクリプト。次を出す
        - 平均スコアの差と、seed ごとの差の標準誤差
        - 相対スコアの大会なら、その大会の式で出した順位の点
        - 対戦なら、勝率と 95% 区間（引き分けは除いて、除いた数も書く）
        - 差が最も悪かった seed を悪い順に 10 件

    終わったら、1 回の実行にかかる時間と、`seeds.txt` の件数で標準誤差がどのくらいになるかを書く。そこから、0.1% の差を見たいときに要る件数の見積りも出す。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet running-contest-experiments/runner-request -->

!!! example "判断例：50 ケースで勝った版を採るか"
    - **状況**：新しい版が、手元の 50 ケースで旧版より平均スコアが 0.5% 高かった。1 回の実行は短く、ケースは増やせる。
    - **迷う候補**：50 ケースの結果で採用する。1,000 ケースに増やしてから決める。
    - **選んだもの**：1,000 ケースに増やしてから決める。
    - **理由**：50 ケースの差は、seed ごとのぶれの範囲に収まりやすい。少ないケースで良かった版を選ぶと、運の良い上振れを拾う。増やした結果で差が消えたなら、「改善したはずの版が、ケースを増やすと負ける」という困りごとは、この上振れが原因だったと分かる。

## 集計の方法を選ぶ（相対スコア） {#aggregation}

相対スコアの大会では、集計の方法そのものを選ぶ必要がある。スコア式の形によって、ケースごとの改善の効率が大きく変わるからである（根拠：弱。実践者の解説）。平均スコアが上がっても、本番の順位の点が上がるとは限らない。

集計の方法は、見えるものと見えないものが違う。複数を並べて出し、食い違ったら本番の式に近い方を優先する。

| 集計の方法 | 見えるもの | 見落とすもの |
| --- | --- | --- |
| 絶対スコアの平均 | 全体の底上げ | 一部の大きいケースに引きずられること |
| ケースごとの勝ち負けの数 | 広いケースで効いているか | 差の大きさ |
| 大会の式で出した点 | 本番に近い評価 | 相手の出力が分からないときの代用の質 |

相対スコアは、本番では他の参加者の出力で決まる。手元には他の参加者の出力がないので、基準にした版などで代用する（この辞典の推奨）。大会ごとの式は公式の規則で確かめる。集計のスクリプトに式を実装させたら、数件のケースで公式の点と一致するかを見る。

合計だけで見ると、一部のケースの悪化が隠れる。層ごとと最悪のケースを見る考え方は <!-- link:begin measure-changes#by-stratum -->[変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)<!-- link:end --> が持つ。ここでは、悪い順に seed を 10 件出させて、改善が一部のケースに偏っていないかを確かめる。

## 勝率に要る試合数 {#games-for-win-rate}

対戦型で勝敗の二値だけを使うと、必要な試合数は直感より多い。勝率 55% の版を見分ける場合を数えると、勝率の標準誤差は `√(p(1−p)/n)` である。`p` = 0.55 のとき、100 試合で標準誤差は 0.0497 になり、95% 区間は約 ±9.8 ポイントで、50% と区別できない。400 試合では標準誤差が 0.0249 になり、半幅は約 4.9 ポイントで、区間の下限が約 50.1% とわずかに 50% を上回る。

この数は、引き分けのない独立な試合を前提にした概算である。引き分けが多い大会や、同じ入力を使い回す試合では、そのまま使えない。

目安は、`p` が 0.5 に近いとき、区間の半幅が約 1 / `√n` になることである。見分けたい差を `d` とすると、試合数は約 1 / `d²` 以上が要る。差が 5 ポイントなら約 400 試合、勝率が 52% なら約 2,400 試合になる。差を半分にしたければ、試合数は 4 倍である。計算は次のスクリプトで確かめられる。

<!-- gen:begin snippet running-contest-experiments/win-rate-interval -->
<!-- textlint-disable -->

??? example "雛形：勝率の 95% 区間と、見分けに要る試合数を出すスクリプト"

    ```python
    """勝敗だけから、勝率の 95% 区間と、見分けに要る試合数の目安を出す。

    前提：引き分けのない、独立な試合。引き分けは除くか、別に数える。
    使い方：python win-rate-interval.py 勝ち数 試合数
            python win-rate-interval.py --need 0.55   （真の勝率を 0.55 と見たときの目安）
    """
    import math
    import sys

    Z = 1.96  # 95% 区間（正規近似）


    def interval(wins: int, games: int) -> tuple[float, float, float]:
        p = wins / games
        half = Z * math.sqrt(p * (1 - p) / games)
        return p, p - half, p + half


    def games_needed(p: float) -> int:
        """区間の下限が 0.5 を上回るのに要る試合数（真の勝率が p のとき）。"""
        gap = p - 0.5
        return math.ceil(Z * Z * p * (1 - p) / (gap * gap))


    if __name__ == "__main__":
        if len(sys.argv) == 3 and sys.argv[1] == "--need":
            p = float(sys.argv[2])
            print(f"真の勝率 {p:.3f} を見分ける目安：約 {games_needed(p)} 試合")
        elif len(sys.argv) == 3:
            wins, games = int(sys.argv[1]), int(sys.argv[2])
            p, lo, hi = interval(wins, games)
            verdict = "50% と区別できる" if lo > 0.5 else "50% と区別できない"
            print(f"勝率 {p:.3f}　95% 区間 [{lo:.3f}, {hi:.3f}]　{verdict}")
        else:
            sys.exit(__doc__)
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet running-contest-experiments/win-rate-interval -->

試合数を減らす道は 2 つある。

- **対応のある比較にする**：同じ入力・同じ seed で、先後と開始位置を入れ替えて対にする。入力の違いによるぶれが消える。
- **得点差も記録する**：勝敗だけだと情報が 1 試合に 1 ビットしかない。得点差があれば、同じ試合数でも差を細かく見られる。

試合数は始める前に決める。途中で結果を見て、都合の良いところで止めると、偽の勝ちを拾う。途中で打ち切りたいときは、境界を事前に決めた逐次の検定を使う。

同じ版を何度も試すほど、運の良い結果が通りやすくなる。再挑戦に上限を置く考え方は <!-- link:begin selection-pressure#retry-cap -->[選択圧：良かった版を選び続ける罠 › 同じアイデアの再挑戦に上限を置く](../eval/selection-pressure.md#retry-cap)<!-- link:end --> が持つ。

## パラメータは入力の性質ごとに {#parameters-by-input}

最適なパラメータが入力の性質で変わる問題では、全入力で 1 つの値を探すと、どの入力にも中途半端な値になる。入力の性質で分けて調整する。

AHC040 の解説では、入力パラメータをサンプルして各点で最適化し、「入力パラメータから最適パラメータ」への写像をガウス過程回帰で学習させている（根拠：弱。単独の事例）。対戦型にも同じ考え方を当てはめられる（類推）。対戦人数や盤面の大きさで強い定数が違うなら、条件ごとに別々に調整し、条件ごとに勝率を測る。

進め方は次のとおり。

1. 入力から計算できる量（個数・大きさ・密度など）で、入力の性質を表す
2. その軸で入力を層に分け、層ごとにパラメータを探す
3. 全体の平均だけで決めず、層ごとの差を見る。層が多すぎるときは、回帰で写像を学習する

探索を AI に回させるのは、数値のパラメータに限る。探す範囲と評価器と止める条件が決まっていれば、Claude Code に反復させられる。戦略そのものを AI に改善させ続けるのは、手元の評価への過適合を自動で進めるので、回さない。理由は <!-- link:begin open-ended-loop-trap#why -->[AI に改善を回させ続ける罠（開いたループ） › なぜ手元の評価に合わせ込まれるのか](../delegate/open-ended-loop-trap.md#why)<!-- link:end --> が持つ。

探索で選んだ最良値は、使った seed では実力より上振れして見える。探索に使わない seed で測り直し、その結果を採否の根拠にする。

長時間の探索は、要約した指標を定期的に書き出させる。設計は <!-- link:begin progress-logs-for-long-jobs -->[長時間ジョブの進捗ログを設計する](../delegate/progress-logs-for-long-jobs.md)<!-- link:end --> が持つ。頭打ちになったら、続けるか方針を変えるかを決める。判断の考え方は <!-- link:begin decide-when-to-quit#plateau -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 頭打ちは方針を疑う合図](../judgment/decide-when-to-quit.md#plateau)<!-- link:end --> が持つ。

!!! example "判断例：温度パラメータの探索を Claude に任せる"
    - **状況**：焼きなましの温度を決める 3 つのパラメータを、Claude Code に自動で探索させたい。入力の大きさによって、最適な値が違いそうである。
    - **迷う候補**：全入力で 1 つの値の組を探す。入力の大きさの層ごとに、値の組を探す。
    - **選んだもの**：層ごとに探す。探索に使う seed と、採否に使う seed は分ける。
    - **理由**：大きさで最適値が違うなら、1 つの値の組は、どの層にも合わない。探索に使った seed の成績は上振れしているので、採否は別の seed で決める。

## 効かなかった実験も残す {#keep-all-runs}

改善しなかった実験も、結果を残す。残さないと、同じ失敗を繰り返し、集計の方法を変えたときに再計算できない。

Kaggle の金メダルの事例には、改善しなかった実験も含めて全実験の OOF 予測（交差検証で、学習に使っていない側の予測）とテスト予測を保存し、後で組み合わせたものがある（根拠：中。機械学習に固有で、AHC への当てはめは類推）。ヒューリスティックでは、予測の代わりに、版ごとのコードの位置と、seed ごとの出力とスコアを残す。

残すものは次のとおり。台帳の項目の全体は <!-- link:begin experiment-log#fields -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 台帳の項目](../eval/experiment-log.md#fields)<!-- link:end --> が持つ。

- **版**：コミットの ID と、変えた点を一言で
- **入力の一覧と集計の式**：seed の一覧ファイルと、使った集計の方法
- **1 件ごとの結果**：seed ごとのスコアまたは勝敗。合計だけにしない
- **採否と理由**：採らなかった版も書く

Claude が提案した実験と、人が提案した実験は、命名で分けておく。後で効いたものの出どころを調べられる。分け方は <!-- link:begin experiment-log#proposer -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 提案者を記録する](../eval/experiment-log.md#proposer)<!-- link:end --> が持つ。

## 確かめ方 {#check}

実験の回し方が正しいかは、次の点で確かめる。

- 同じ版同士を比べて、差が 0 の付近に収まり、ぶれの幅が決めた幅より小さい
- 採用の前に、調整に使っていない seed で測り直して、差が残る
- 手元のスコアが、数件のケースで公式の点と一致する
- 改善が一部のケースだけでなく、悪い順の seed 10 件でも悪化していない
- 急に大きく伸びた結果は、受け取る前に疑う。疑う点は <!-- link:begin suspect-too-good-results#what-to-suspect -->[良すぎる結果を疑う › まず疑うもの](../verify/suspect-too-good-results.md#what-to-suspect)<!-- link:end --> が持つ。

## 失敗したとき {#when-it-fails}

- **手元で勝つのに、本番で負ける**：評価器と本番がずれている。原因の振り分けは <!-- link:begin misses-broken-evaluation -->[手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)<!-- link:end --> が持つ。
- **増やしたケースで、改善が消える**：少ないケースで良かった版を選んでいた。ケース数を増やして測り直し、採否を決め直す。
- **同じ失敗を繰り返す**：台帳が書けていない。確かめ方は <!-- link:begin experiment-log#when-it-fails -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 台帳があっても繰り返すとき](../eval/experiment-log.md#when-it-fails)<!-- link:end --> が持つ。
- **仮説が多くて、比べ方が混ざる**：仮説ごとに版を分けて、同じ物差しで比べる。手順は <!-- link:begin compare-hypotheses-in-parallel#steps -->[仮説ごとに並べて、同じ物差しで比べる › 手順](../delegate/compare-hypotheses-in-parallel.md#steps)<!-- link:end --> が持つ。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [HACK TO THE FUTURE 2025 (AHC040) 解説](https://blog.terry-u16.net/entry/ahc040)：TERRY（terry\_u16）・確認日 2026-11-04
- [相対スコア AHC の立ち回り](https://kiri8128.hatenablog.com/entry/2024/05/06/032420)：Kiri8128・確認日 2026-11-04
- [Winning a Kaggle Competition with Generative AI–Assisted Coding](https://developer.nvidia.com/blog/winning-a-kaggle-competition-with-generative-ai-assisted-coding/)：NVIDIA Developer Blog・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](evaluators-by-format.md)

**関連**

- [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)
- [変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)
- [AI に改善を回させ続ける罠（開いたループ）](../delegate/open-ended-loop-trap.md)
- [仮説ごとに並べて、同じ物差しで比べる](../delegate/compare-hypotheses-in-parallel.md)
- [並列・ループ・workflows のコスト](../cost/parallel-and-loop-costs.md)
- [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- [良すぎる結果を疑う](../verify/suspect-too-good-results.md)
- [長時間ジョブの進捗ログを設計する](../delegate/progress-logs-for-long-jobs.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
