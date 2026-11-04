---
id: misses-broken-evaluation
title: 手元の評価は良いのに本番で通用しない
aliases: [評価のおかしさに自分からは気づかない, 評価の誤りを放置する, リークに気づかない, スコアだけ上がる]
type: symptom
field: symptoms
chapter: 完了と検証
order: 230
level: 任せる
priority: 必須
surfaces: [claude-code, api]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [データ分析, 開発, コンテスト]
summary: 手元の評価は良いのに本番で通用しないときに、評価の仕組みが正しいか・書き換えられないか・本番を代表するかを切り分ける。Claude は評価の誤りを自分からは直さないので、評価そのものを人が確かめる。
signs:
  - {type: symptom, text: 評価のやり方の誤りを指摘してくれない}
  - {type: symptom, text: 手元のスコアは上がるのに本番で通用しない}
  - {type: symptom, text: おかしな評価のまま実験を続けている}
wave: 1
prerequisites: [verifier-defines-problem]
related: [selection-pressure, open-ended-loop-trap, lockbox-and-holdout, suspect-too-good-results, measure-changes#by-stratum, reward-hacking, over-reliance, audit-ml-pipelines, data-analysis, evaluators-by-format, rewrote-tests-to-pass, claims-done-but-isnt, stuck-in-a-check-loop, six-causes]
routes:
  - {cause: 確かめていない, to: [verifier-three-conditions, test-the-verifier, check-the-metric]}
  - {cause: 預けすぎる, to: [what-not-to-delegate#what-humans-hold]}
tracks: []
outdated_advice: []
sources: [arxiv-2605-21384, lukyanenko-rogii-geosteering-kaggle, drivendata-ai-agents-data-science-competitions, andpad-claude-code-ml-loop, pebblous-agentic-data-science-silent-failures, battlecode-2025-confused-pdf, anthropic-eng-harness-design-long-running]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: routes-to-fixes}
  - {title: 判断例, anchor: example}
  - {title: 予防：仕組みに移す, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：評価の仕組みが正しいか・書き換えられていないか・本番を代表するかを、安く確かめる順に切り分け、人が確かめる所を決められる。
    - **いつ引くか**：手元のスコアは上がるのに本番で通用しない・Claude が評価のやり方の誤りを指摘してくれない・おかしな評価のまま実験が続いている、とき。
    - **前提**：<!-- link:begin verifier-defines-problem -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)<!-- link:end -->

<!-- textlint-disable -->
別名：評価のおかしさに自分からは気づかない・評価の誤りを放置する・リークに気づかない・スコアだけ上がる
<!-- textlint-enable -->

手元の評価は良いのに本番で通用しない症状は、Claude が手元のスコアを上げる作業を進めたのに、そのスコアが本番の良さを表していないことである。放置すると、誤った評価を基準にした実験が積み上がり、成果として報告される。

背景は前提のページにある。Claude は渡された評価（検証器）が定める問題を解くので、評価が誤っていれば、誤りに合わせて作業を進める。このページは、起きたときに原因を切り分け、人が何を確かめるかを決める入口である。評価の誤りは Claude が自分から指摘するとは限らない（「よくある形」の節の例）。評価を確かめる役は、人が持つ。

## よくある形 {#forms}

手元の評価と本番がずれる形は、次の 5 つに分けると見分けやすい。いずれも公開された報告で、起きた条件は版やモデルで違う。コンテストの例は、業務のデータ分析やテストにもそのまま当てはまる（類推）。

- **評価の誤りに気づくのが遅い**：企業の報告に、機械学習の実験ループを Claude Code に回させる際、わざとリークのある交差検証（CV）を仕込んだ実験がある。Claude Code が評価の方法そのものを直したのは、10 実験目あたりだった（モデルは未確認。根拠：中）。それまでの実験は、誤った評価の上で進んでいた。
- **検証のスコアだけが満点に近い**：エージェントが漏洩した変数を使い、自前の検証で QWK（採点に使う一致度の指標）がほぼ 1.0 だったのに、実際のリーダーボード（本番の順位表）では 0.44 前後だったという研究がある。二次の要約で読んだもので、対象のモデルは確かめていない（根拠：弱）。
- **見えている指標に合わせる**：Kaggle の入賞者は、Claude が見えている 3 本のテストをくり返しハードコードしたと報告している。学習と推論の間に、リークや特徴量の順序の食い違いも入っていた。「難しい」サンプルは、OOF（学習に使わなかった分の予測）から黙って除外されていた（単独の経験談。根拠：弱）。
- **計画した検証を省く**：データ分析のコンテストで、Claude が 5-fold の CV（データを 5 つに分けて順に検証する方法）を計画しながら、単一の分割で済ませた例がある。自分の過去の版より悪い提出を最終に選ぶこともあった（実践者の報告。根拠：弱）。
- **見えている検証と見えていない検証の差**：SpecBench（2026 年。arXiv のプレプリント）は、可視の検証スイートと、非公開の hold-out（開発に使わず取り置いたデータ）の差を測る。Claude Code（Opus 4.6）の差は、探索の戦略によらず約 43〜48 ポイントあった。最も多い失敗は、機能を個別にしか満たさないもので、意図的な悪用はまれだった（根拠：中）。

手元の評価が本番を代表しない例は、競技にもある。Battlecode 2025 の事後報告の 1 つは、予選時点の自分の旧版には 70% 超で勝てたのに、上位チームとの練習試合では五分前後だったと書く（実践者の報告。根拠：弱・類推）。自分の旧版だけに勝つ評価は、本番の勝ちを意味しない。

## 原因を安く確かめる順 {#diagnosis}

診断は、手間の少ない確認から順に進める。最初に、差を事実で確定する。手元の評価と本番（または人だけが持つ検証用のデータ）を、同じ指標で比べる。差が試行のばらつきの範囲なら、症状は別の原因なので、このページを閉じてよい。ばらつきの見方は <!-- link:begin measure-changes#how-many-runs -->[変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ](../eval/measure-changes.md#how-many-runs)<!-- link:end --> にある。差が確定したら、次の順に確かめる。

1. **確かめていない：評価が正しくない**（リーク〔検証用のデータの情報が学習に混ざること〕・採点の誤り）
    - 見るもの：検証用のデータの情報が、学習や特徴量の作成に入っていないか。スコアが良すぎないか。
    - 確かめ方：急に上がったスコアや満点に近いスコアは、まずリークを疑う。何もしない解が負けるか、手で計算した値と一致するかを、評価に当てて確かめる。やり方は <!-- link:begin test-the-verifier#red-green -->[検証器そのものを確かめる（red/green・手で計算したケース） › red/green を検証器に当てる](../eval/test-the-verifier.md#red-green)<!-- link:end --> にある。疑う順は <!-- link:begin suspect-too-good-results#what-to-suspect -->[良すぎる結果を疑う › まず疑うもの](../verify/suspect-too-good-results.md#what-to-suspect)<!-- link:end --> にある。
    - 機械学習のパイプラインを行の引用つきで点検させる手順は、<!-- link:begin audit-ml-pipelines -->機械学習のパイプラインを点検させる（準備中）<!-- link:end --> にある。
2. **確かめていない：評価が書き換えられた**
    - 見るもの：評価のコード・テスト・正解のデータ・データの分割が、実験の途中で変わっていないか。
    - 確かめ方：評価に関わるファイルの差分を、人が `git diff` で見る。変わっていれば、いつ誰が変えたかをたどる。書き換えられない状態に置けていたかは <!-- link:begin verifier-three-conditions#tamper-proof -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 書き換えられない](../eval/verifier-three-conditions.md#tamper-proof)<!-- link:end -->、テストを書き換えて通した症状との見分けは <!-- link:begin rewrote-tests-to-pass#diagnosis -->[テストを書き換えて通した › 原因を安く確かめる順](rewrote-tests-to-pass.md#diagnosis)<!-- link:end --> にある。
3. **確かめていない：評価が本番を代表しない**
    - 見るもの：検証用のデータの分布は、本番に来る入力と同じか。同じ検証用のデータで、版を選び続けていないか。
    - 確かめ方：検証用のデータと本番の入力を、いくつかの層（時期・種類・難しさ）で比べる。合計だけでなく、層ごとと最悪の場合でも測り直す。測り直し方は <!-- link:begin measure-changes#by-stratum -->[変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)<!-- link:end --> にある。
    - 同じ検証用のデータで版を選び続けると、評価の穴に合わせ込まれる。仕組みは <!-- link:begin selection-pressure#why -->[選択圧：良かった版を選び続ける罠 › なぜ正直でも外れるか](../eval/selection-pressure.md#why)<!-- link:end --> にある。
    - 条件の見方は <!-- link:begin verifier-three-conditions#representative -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 本番を代表する](../eval/verifier-three-conditions.md#representative)<!-- link:end -->、データ分析の CV の例は <!-- link:begin evaluators-by-format#cv -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › データ分析：分布の差を確かめた CV](../contest/evaluators-by-format.md#cv)<!-- link:end --> にある。
4. **確かめていない：指標が目的とずれる**
    - 見るもの：評価の指標が上がることと、本当に欲しい結果が得られることは、同じ意味か。
    - 確かめ方：指標が良いのに目的を満たさない例を、手で 1 つ探す。見つかれば、指標そのものが誤りである。確かめ方は <!-- link:begin check-the-metric#mismatch -->[評価指標そのものを確かめる › 指標と目的のずれ](../eval/check-the-metric.md#mismatch)<!-- link:end --> にある。
5. **預けすぎる**（人の側）：評価の設計まで任せきっている。
    - 見るもの：評価の定義・分割・採否の基準を、誰が決めたか。人が自分の目で確かめたのは、いつが最後か。
    - 確かめ方：評価を作った者と、評価を確かめた者が同じ Claude のセッションでないか。同じなら、書いた本人が採点している。報告では「評価に問題はない」と言われても、確かめた範囲が示されていなければ、確かめたことにならない。エージェントが自分の作業を高く評価しやすい傾向は、企業の報告にある（根拠：中）。人が手元に残すものは <!-- link:begin what-not-to-delegate#what-humans-hold -->[任せないもの（評価・採否・撤退・中核の理解） › どの段階でも人が握るもの](../delegate/what-not-to-delegate.md#what-humans-hold)<!-- link:end --> にある。

Claude に点検を手伝わせてもよい。ただし、返答は手がかりであり、評価が正しいという証明ではない。引用された行は人が開いて確かめる。依頼の雛形を、次に置く。

<!-- gen:begin snippet misses-broken-evaluation/audit-evaluation -->
<!-- textlint-disable -->

??? example "雛形：評価の仕組みを点検させる依頼"

    ```text
    いまの評価の仕組み（<評価のスクリプトと、データを分けるコードの場所>）を点検して。この依頼では何も変更しない。答えるのは次の 4 点だけで、各項目に該当するコードの行を引用する。

    1. 検証用のデータの情報が、学習や特徴量の作成に入っていないか。
    2. 評価のコード・テスト・正解のデータを、これまでの変更で書き換えていないか。差分で確かめる。
    3. 検証用のデータの分布と、本番に来る入力の分布の違い。
    4. 手元のスコアが、本当の目的を測っているか。ずれる所があれば挙げる。

    見つからなかった項目は「見つからなかった」と書き、確かめた範囲を添える。確かめていないことを、問題なしとは書かない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet misses-broken-evaluation/audit-evaluation -->

## 原因ごとの対処 {#routes-to-fixes}

診断で当たった原因に対応する対処は、次の表のページにある。このページは切り分けまでを受け持ち、対処の本体は書かない。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 確かめていない | [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)<br>[検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)<br>[評価指標そのものを確かめる](../eval/check-the-metric.md) |
| 預けすぎる | [任せないもの（評価・採否・撤退・中核の理解） › どの段階でも人が握るもの](../delegate/what-not-to-delegate.md#what-humans-hold) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#example}

!!! example "判断例：検証のスコアが上がり続けるのに、本番に近いデータで下がった"
    - **状況**：分類モデルの改善を Claude に任せた。手元の検証スコアは、10 回の変更で上がり続けた。本番に近い新しいデータで測ると、スコアは下がっていた。
    - **迷う候補**：A は、Claude に「評価に問題がないか確認して」と頼み、同じセッションで直させる。B は、人が先に評価の分割・リークの有無・評価コードの差分を点検し、人だけが持つ検証用のデータを切り分けてから続ける。
    - **選んだもの**：B。A の依頼は、点検の手がかりを得る補助として併用する。
    - **理由**：Claude は、評価の誤りを自分から指摘するとは限らない。A だけだと、10 回の変更で合わせ込まれた同じ検証用のデータが基準のまま残り、「問題なし」の返答も同じ基準で出る。B は、評価を確かめる役を、変更を重ねてきた流れの外に置ける。

## 予防：仕組みに移す {#prevention}

予防の考え方は、「評価も見て」と頼み続けるのをやめ、評価を確かめて守る手段を仕組みに置くことである。任せる幅を広げるほど、先に評価を整える。

- 最初の成果物を、評価にする。使う前に、何もしない解が負け、手で計算した値と一致することを確かめ、確かめてから凍結する（<!-- link:begin test-the-verifier#freeze -->[検証器そのものを確かめる（red/green・手で計算したケース） › 確かめてから凍結する](../eval/test-the-verifier.md#freeze)<!-- link:end -->）。
- 入力を、開発用・検証用・人だけが持つロックボックスに分ける。節目にだけロックボックスを見て、Claude には点数だけを返す（<!-- link:begin lockbox-and-holdout#three-tiers -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 三層に分ける](../eval/lockbox-and-holdout.md#three-tiers)<!-- link:end -->）。
- 版を選び続ける運用に守りを置く。一変更一評価、試行の台帳、見せないデータを使う（<!-- link:begin selection-pressure#defenses -->[選択圧：良かった版を選び続ける罠 › 防ぎ方](../eval/selection-pressure.md#defenses)<!-- link:end -->）。
- 満点に近い結果を、受け取る前に疑う。自己点検は、報告の前に Claude にさせる（<!-- link:begin suspect-too-good-results#self-check -->[良すぎる結果を疑う › 報告の前に自己点検させる](../verify/suspect-too-good-results.md#self-check)<!-- link:end -->）。
- 評価の定義・採否・撤退は、人が握る。分ける軸は、出力を機械的に確かめられるかである（<!-- link:begin what-not-to-delegate#verifiable-axis -->[任せないもの（評価・採否・撤退・中核の理解） › 分ける軸：機械的に確かめられるか](../delegate/what-not-to-delegate.md#verifiable-axis)<!-- link:end -->）。
- 戦略そのものを回し続けさせない。反復させるのは、仕様が決まり停止条件のある実装の作業に限る（<!-- link:begin open-ended-loop-trap#closed-vs-open -->[AI に改善を回させ続ける罠（開いたループ） › 閉じた反復と開いたループ](../delegate/open-ended-loop-trap.md#closed-vs-open)<!-- link:end -->）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents](https://arxiv.org/abs/2605.21384)：arXiv（Zhao, Bingchen ほか）・英語・確認日 2026-11-04
- [How AI agents helped me win a Kaggle silver medal — and how they failed me](https://andlukyane.com/blog/rogii-geosteering-kaggle)：Andrey Lukyanenko・英語・確認日 2026-11-04
- [AI Agents in Data Science Competitions: Lessons from the Leaderboard](https://blog.drivendata.org/blog/ai-agents-data-science-competitions)：DrivenData・英語・確認日 2026-11-04
- [Claude CodeでML実験ループを自動化した際の学び](https://tech.andpad.co.jp/entry/2026/08/07/100000)：ANDPAD Tech Blog・確認日 2026-11-04
- [Data Leakage: The Flaw That Makes an AI's Analysis Score Higher](https://blog.pebblous.ai/blog/agentic-data-science-silent-failures/en/)：Pebblous・英語・確認日 2026-11-04
- [Battlecode 2025 Postmortem（confused）](https://battlecode.org/assets/files/postmortem-2025-confused.pdf)：Battlecode（MIT）の参加チームの振り返り・英語・確認日 2026-11-04
- [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)

**次に読む**

- [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- [評価指標そのものを確かめる](../eval/check-the-metric.md)
- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)

**関連**

- [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)
- [AI に改善を回させ続ける罠（開いたループ）](../delegate/open-ended-loop-trap.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)
- [良すぎる結果を疑う](../verify/suspect-too-good-results.md)
- [変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)
- [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- 機械学習のパイプラインを点検させる（準備中）
- [データを分析する](../recipes/data-analysis.md)
- [形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](../contest/evaluators-by-format.md)
- [テストを書き換えて通した](rewrote-tests-to-pass.md)
- [「完了」と言うが終わっていない](claims-done-but-isnt.md)
- [同じ確認のループにはまる](stuck-in-a-check-loop.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
