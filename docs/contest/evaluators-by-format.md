---
id: evaluators-by-format
title: 形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）
nav_title: 形式別の評価器
aliases: [ローカルテスタ, ローカル評価]
type: concept
field: contest
chapter: 評価と実験
order: 50
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [コンテスト]
summary: 形式ごとに検証器が何に当たるか（テスタ・ベンチマーカー・CV・flag の検証・対戦場など）と、公式や本番とのずれをどう確かめるかが分かる。
signs:
  - {type: goal, text: AHC のローカルテスタを AI に作らせたい}
  - {type: symptom, text: 手元の評価器のスコアが、公式の採点と合わない}
  - {type: goal, text: 対戦型の大会で、ボットの強さを手元で比べたい}
prerequisites: [verifier-three-conditions]
related: [test-the-verifier, verifier-defines-problem, differential-testing, lockbox-and-holdout, check-the-metric, build-test-harness, build-observation-tools, running-contest-experiments, competition-day-operations, format-cheatsheet, freeze-eval-assets, protect-tests, misses-broken-evaluation, suspect-too-good-results]
tracks: []
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: どの形式でも、最初の成果物は評価器, anchor: evaluator-first}
  - {title: 短時間のアルゴリズム：愚直解との比較, anchor: stress-test}
  - {title: ヒューリスティック：公式とスコアが一致するテスタ, anchor: tester}
  - {title: 性能改善：ベンチマーカーと計装, anchor: benchmarker}
  - {title: CTF：提出の前の flag の検証, anchor: flag}
  - {title: データ分析：分布の差を確かめた CV, anchor: cv}
  - {title: ハッカソン：機械の評価器がないとき, anchor: no-mechanical-evaluator}
  - {title: 対戦型：対戦場と基準のボット, anchor: arena}
  - {title: 何に効くか, anchor: what-it-prevents}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：コンテストの形式ごとに、検証器に当たるもの（テスタ・ベンチマーカー・CV・flag の検証・対戦場）と、公式や本番とのずれの確かめ方が分かる。
    - **いつ引くか**：AHC のローカルテスタを AI に作らせるとき。手元の評価器のスコアが公式の採点と合わないとき。対戦型の大会で、ボットの強さを手元で比べたいとき。
    - **前提**：<!-- link:begin verifier-three-conditions -->[検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)<!-- link:end -->

<!-- textlint-disable -->
別名：ローカルテスタ・ローカル評価
<!-- textlint-enable -->

形式別の評価器は、コンテストの形式ごとに違う姿をした検証器の、当てはめ方を並べたページである。検証器の一般の原理は eval の分野のページが持つので、ここでは形式ごとの違いと、確かめどころに絞る。

## どの形式でも、最初の成果物は評価器 {#evaluator-first}

ローカルテスタ、ベンチ環境、CV、対戦場、flag の検証は、形式が違っても、すべて検証器である。Claude は置かれた検証器が定める問題を解くので、人が最初にやる仕事は解法ではなく検証器づくりになる。この考え方の本体は <!-- link:begin verifier-defines-problem#verifier-first -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › 最初の成果物は検証器](../eval/verifier-defines-problem.md#verifier-first)<!-- link:end --> にある。

検証器には、正しい・書き換えられない・本番を代表する、の 3 つの条件がある。条件の中身は <!-- link:begin verifier-three-conditions#why -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 三条件が要る理由](../eval/verifier-three-conditions.md#why)<!-- link:end --> が持つ。形式が変わると、この 3 つのうちで先に崩れる条件が変わる。下の表は、形式ごとの評価器の実体と、ずれが出やすい所である。

| 形式 | 評価器の実体 | ずれが出やすい所 |
| --- | --- | --- |
| 短時間のアルゴリズム | 愚直解との比較 | 愚直解や入力の生成器の誤り |
| ヒューリスティック | 公式と一致するテスタ | スコアの定義の読み違い |
| 性能改善 | ベンチマーカーと計装 | 点数だけで原因が見えないこと |
| CTF | 提出前の flag の検証 | 誤答のペナルティの見落とし |
| データ分析 | 分布の差を確かめた CV | リークと、train と test の分布差 |
| ハッカソン | 機械の評価器がない | 測れる部分だけを最適化すること |
| 対戦型 | 対戦場と基準のボット | 相手の幅の狭さ |

評価器を作らせたら、判定に使う前に、既知の答えで確かめてから凍結する。確かめ方は <!-- link:begin test-the-verifier#red-green -->[検証器そのものを確かめる（red/green・手で計算したケース） › red/green を検証器に当てる](../eval/test-the-verifier.md#red-green)<!-- link:end --> に、凍結のやり方は <!-- link:begin freeze-eval-assets#how-to-freeze -->[評価資産を凍結し、触れる範囲を絞る › 設定で止める（権限ルール・サンドボックス・ファイルの権限）](../enforce/freeze-eval-assets.md#how-to-freeze)<!-- link:end --> にある。以下の節は、形式ごとの確かめどころだけを書く。

## 短時間のアルゴリズム：愚直解との比較 {#stress-test}

短時間のアルゴリズムの大会では、評価器は愚直解との比較になる。遅くても明らかに正しい解を用意し、小さな入力を大量に生成して、本解の出力と突き合わせる。手順は <!-- link:begin differential-testing#steps -->[答えの分かる遅い解と比べる（差分テスト・オラクル） › 手順](../eval/differential-testing.md#steps)<!-- link:end --> が持つ。

形式に固有の確かめどころは 2 つある。

- 入力の生成器が問題文の制約を守っているか。制約の外の入力で「落ちた」と報告されても、本解の誤りとは限らない。生成器の分布は人が見る（<!-- link:begin test-the-verifier#input-distribution -->[検証器そのものを確かめる（red/green・手で計算したケース） › 入力の生成器の分布を人が見る](../eval/test-the-verifier.md#input-distribution)<!-- link:end -->）
- 愚直解そのものが正しいか。小さなケースを手で計算して、愚直解の答えと合うかを先に見る（<!-- link:begin test-the-verifier#hand-calculated -->[検証器そのものを確かめる（red/green・手で計算したケース） › 手で計算したケース](../eval/test-the-verifier.md#hand-calculated)<!-- link:end -->）

食い違いが出たときに、愚直解の側を本解に合わせて直させない。正解の側を守る依頼の書き方は <!-- link:begin differential-testing#protect-the-oracle -->[答えの分かる遅い解と比べる（差分テスト・オラクル） › 正解の側を守る](../eval/differential-testing.md#protect-the-oracle)<!-- link:end --> にある。

## ヒューリスティック：公式とスコアが一致するテスタ {#tester}

ヒューリスティックの大会では、評価器は公式のテスタとスコアが完全に一致するローカルテスタになる。ほかに要るのは、シードを変えた並列の実行、相対スコアでの集計、実行ごとのソースの保存である（根拠：強・類推。大会の実践の整理に基づく）。ソースを保存しておくと、あのスコアがどの版の解から出たかを後から辿れる。

テスタの作らせ方で、いちばん効くのは公式のテスタを書き直させないことである。公式が配るテスタを呼び出す側だけを作らせれば、スコアの定義を Claude が読み違える余地が減る。自前の採点を書かせるなら、公式のサンプルの入出力でスコアが一致することを、完了の条件にする。

<!-- gen:begin snippet evaluators-by-format/tester-request -->
<!-- textlint-disable -->

??? example "雛形：ローカルのテスタを先に作らせる依頼"

    ```markdown
    ヒューリスティック系の大会に向けて、ローカルで使うテスタを作ってほしい。解法はまだ書かない。先に作るのは評価器だけだ。

    材料は、`problem/` にある問題文と、公式が配った入力の生成器・テスタ・サンプルの入出力だ。`problem/` と `tools/official/` の中のファイルは書き換えない。

    作るもの：

    1. 公式のテスタを呼んでスコアを出す実行スクリプト。公式のテスタをこちらで書き直さない
    2. シードの範囲を渡して、複数の入力を並列に流す仕組み。結果は 1 行ずつ「シード・スコア・実行時間・異常の有無」で `runs/` に残す
    3. 実行ごとに、そのときの解のソースを `runs/` に保存する仕組み
    4. 相対スコアで順位を付ける集計。基準の解は、こちらが渡す

    終わる前に、公式のサンプルの入出力を流し、公式の採点と同じスコアが出ることを示してほしい。合わなければ、どこが違うかを調べて報告する。テスタ側を直して合わせるのではなく、まず違いの原因を報告すること。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet evaluators-by-format/tester-request -->

手元のスコアが公式の採点と合わないときは、次の順で安く確かめる。

1. 入力の形式と乱数のシード。同じ入力を流しているか
2. スコアの定義。最大化と最小化の向き、絶対スコアと相対スコアの別
3. 不正な出力や制限超過の扱い。公式は 0 点にするのか、失格にするのか
4. 実行環境の差。時間制限に近い解は、手元の機械と本番で結果が変わる

原因が分からないうちは、テスタ側を公式に合わせて直させず、違いの原因を先に報告させる。合わないまま最適化を回すと、間違った目標に向かって速く進む。症状としての切り分けは <!-- link:begin misses-broken-evaluation#diagnosis -->[手元の評価は良いのに本番で通用しない › 原因を安く確かめる順](../symptoms/misses-broken-evaluation.md#diagnosis)<!-- link:end --> にある。相対スコアでの集計は <!-- link:begin running-contest-experiments#aggregation -->[実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数） › 集計の方法を選ぶ（相対スコア）](running-contest-experiments.md#aggregation)<!-- link:end --> が持つ。

## 性能改善：ベンチマーカーと計装 {#benchmarker}

性能改善の大会では、評価器はベンチマーカーである。ただし点数だけでは、遅い原因が見えない。ベンチマーカーに加えて、コードを読むだけでは見えない待ちを見せる計装が要る。

ISUCON14 の再挑戦の事後報告では、遅い原因は SQL ではなくコネクションプールの待ちで、横断的な計測データを見て初めて分かった（根拠：中。1 つの大会の参加報告）。一般化すると、推測より計測になる。Claude に「遅そうな所」を推測で直させるより、計測の道具を作らせて、値を見てから直す箇所を決める。

計装を作らせる方法は <!-- link:begin build-observation-tools -->[観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)<!-- link:end --> が持つ。道具の出す値は、小さな例で手計算と合うかを先に確かめる。計装そのものが処理を遅くすることもあるので、計装を入れた版と外した版で、ベンチマーカーの点数を見比べる。

## CTF：提出の前の flag の検証 {#flag}

CTF では、評価器に当たるのは、提出前に人が flag を検証する手順である。flag の正誤は、提出して初めて分かる形式が多く、手元に採点器がない。そこで、手順そのものを評価器として設計する。

- 総当たりで flag を推測させない。エージェントに試行を任せると、提出の回数が増える
- 誤答のペナルティを、規則で先に確かめる。誤答の回数で提出が止まる大会がある。条件は大会と版で変わるので、数字は書かず、規則の確認に回す
- flag の形式と出所を、人が見る。取った値が、問題の指す場所から出たものかを確かめる

提出の段の運用は <!-- link:begin competition-day-operations#submission -->[本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態） › 提出：人が確かめる](competition-day-operations.md#submission)<!-- link:end --> が持つ。形式としての CTF の効き方は <!-- link:begin format-cheatsheet#ctf -->[コンテストの形式別の早見表（AI の効き方と人が握るところ） › CTF](format-cheatsheet.md#ctf)<!-- link:end --> で引ける。

## データ分析：分布の差を確かめた CV {#cv}

データ分析型の大会では、評価器は train と test の分布の差と時間変化を確かめたうえで設計した CV（交差検証）になる（根拠：強・類推）。分割の仕方が本番の分布を代表していなければ、CV の値は良くても、公開順位や最終順位には効かない。

人が先に決めるのは、分割の方法である。時間で並ぶデータなら、未来を過去で予測する形に分ける。train と test の特徴量の分布を比べ、違いが大きければ、test に近い分布の部分で検証するなど、その違いを分割の設計に反映する。この決定を Claude に任せると、リークのある CV でも高い値が出て、そのまま最適化が進む。

わざとリークのある CV を仕込んだ実験では、エージェントが評価方法を直したのは 10 実験目あたりだった（根拠：弱。国内の企業ブログ 1 件の報告）。エージェントは評価の誤りを自分からは直さない、と見積もるのが安全である。CV の値が急に跳ねたら、リークと退化を疑う（<!-- link:begin suspect-too-good-results#what-to-suspect -->[良すぎる結果を疑う › まず疑うもの](../verify/suspect-too-good-results.md#what-to-suspect)<!-- link:end -->）。

## ハッカソン：機械の評価器がないとき {#no-mechanical-evaluator}

ハッカソンや作品の部門では、機械の評価器がないことが多い。審査は人が行う。それでも、評価器を持たないまま進める必要はない。

機械で確かめられる部分と、人が判断する部分を分ける。機械で確かめられるのは、提出の要件を満たすこと、ビルドが通ること、デモの手順を通しで動かせること、などである。これらは、チェックリストと簡単な通しのテストにして、評価器として置ける（推論・実践例なし）。

人が判断する部分、つまり審査員が高く評価するかどうかは、機械で測れない。機械で測れる部分だけを最適化させると、指標と目的がずれる。このずれは <!-- link:begin check-the-metric#mismatch -->[評価指標そのものを確かめる › 指標と目的のずれ](../eval/check-the-metric.md#mismatch)<!-- link:end --> で確かめる。審査の観点は、人が読み取って文章にし、Claude には観点を満たす案を作らせるのでなく、案を観点に照らして指摘させる使い方が安全である。

## 対戦型：対戦場と基準のボット {#arena}

対戦型の大会では、評価器は公式の審判をラップしたローカルの対戦場になる。ローカルのリーグに、試合の結果から強さのレートを付ける仕組みを載せる例がある（根拠：強・類推）。

手元で勝てることが、本番で勝てることを意味するには、相手の幅が要る。ローカルの相手が自分の旧版だけだと、旧版にだけ勝つ評価になる。Battlecode の事後報告には、予選用の版には高い勝率でも、上位チームとの練習試合では五分前後だった例がある。旧版にだけ勝つ危うさは、大会の毎年の記録に出てくる（根拠：中）。

手元の相手の幅を確保するための対策と注意が、合わせて 3 つある。

- 性質の異なる基準のボット（ランダム、貪欲、攻撃型、守備型、複数の旧版）を用意する。戦略の仕様は人が書き分ける
- 他チームとのスクリムを併用する。手元の相手に含まれない戦略が出る
- 勝敗は二値で、差の大きさの情報を捨てている。勝率の判定には、誤差に負けない試合数が要る（<!-- link:begin running-contest-experiments#games-for-win-rate -->[実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数） › 勝率に要る試合数](running-contest-experiments.md#games-for-win-rate)<!-- link:end -->）

同じモデルに基準のボットをすべて書かせると、戦略が似通うのではないかと考えられる。これは仮説で、確かめられていない。仮説でも、戦略の仕様を人が書き分けておけば、この害を避けられる。

<!-- gen:begin snippet evaluators-by-format/arena-bots-request -->
<!-- textlint-disable -->

??? example "雛形：基準のボットを仕様どおりに作らせる依頼"

    ```markdown
    対戦型の大会に向けて、ローカルの対戦場に置く基準のボットを作ってほしい。ボットの戦略は、こちらが `bots/spec/` に 1 つずつ書いた仕様のとおりに実装する。仕様にない工夫は足さない。

    1. `bots/spec/random.md`・`greedy.md`・`aggressive.md`・`defensive.md` を、それぞれ別のボットとして実装する
    2. 公式の対戦の審判を呼んで、ボット同士を総当たりで戦わせる実行スクリプトを作る。審判をこちらで書き直さない
    3. 結果は 1 試合ごとに「対戦の組・先手後手・勝敗・試合の乱数」を `arena/results.csv` に残す。先手後手は入れ替えて同じ回数だけ戦わせる

    終わる前に、ボット同士の勝敗の表を出してほしい。どのボットにも勝てるボットや、どのボットにも負けるボットがいたら、仕様の読み違いを疑って報告する。仕様を勝手に直して勝敗を整えない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet evaluators-by-format/arena-bots-request -->

!!! example "判断例：新版が旧版に勝ち越したとき"
    - **状況**：自分の新版が、旧版に 7 割近く勝つ。ローカルの相手は、旧版と、旧版の別の設定だけである。
    - **迷う候補**：新版をそのまま提出する。基準のボットを増やして、勝率を取り直す。
    - **選んだもの**：基準のボットを増やして取り直す。
    - **理由**：旧版に勝つことは、旧版と似た相手に強いことしか示さない。性質の違う相手に対しても勝てるかを見ないと、手元の勝ちが本番の勝ちを意味するかは分からない。取り直しの費用は小さく、外れたときの損失は大きい。

## 何に効くか {#what-it-prevents}

このページの内容は、原理の「確かめる」に当たり、防ぐ原因は「確かめていない」である。Claude は渡された評価器が定める問題を解く。評価器の誤りは、そのまま速い誤りになる。形式ごとの評価器は、確かめる対象を決めて、確かめない状態で最適化が走るのを防ぐ。

形式ごとの確かめどころは、検証器の 3 つの条件に対応する。公式との一致やリークの有無は「正しい」に、本番の分布や相手の幅は「本番を代表する」に当たる。「書き換えられない」は、どの形式でも共通で、<!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](../verify/protect-tests.md#layers)<!-- link:end --> と <!-- link:begin freeze-eval-assets -->[評価資産を凍結し、触れる範囲を絞る](../enforce/freeze-eval-assets.md)<!-- link:end --> の守りが担う。

手元の評価は良いのに本番で通用しないときの切り分けは、<!-- link:begin misses-broken-evaluation -->[手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)<!-- link:end --> に任せる。ロックボックスの分け方は <!-- link:begin lockbox-and-holdout#three-tiers -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 三層に分ける](../eval/lockbox-and-holdout.md#three-tiers)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- **公式のテスタがあれば、評価器は確かめなくてよい**。公式のテスタはスコアの計算だけを持つ。入力の生成、相対スコアの集計、並列実行、結果の保存は自前で作るので、そこで誤りが入る
- **手元で勝てれば、本番でも勝てる**。手元の相手や入力が本番の幅を代表しないと、手元の勝ちは本番の勝ちを意味しない。形式を問わず、本番を代表するかを人が確かめる
- **機械の評価器がなければ、評価器は要らない**。機械で確かめられる部分は、ハッカソンでも切り出せる。測れる部分だけを最適化する危険は、指標と目的のずれとして別に確かめる

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)

**次に読む**

- [実験の回し方（ケース数・集計・パラメータ・勝率に要る試合数）](running-contest-experiments.md)
- [本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態）](competition-day-operations.md)

**関連**

- [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [答えの分かる遅い解と比べる（差分テスト・オラクル）](../eval/differential-testing.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)
- [評価指標そのものを確かめる](../eval/check-the-metric.md)
- [検証環境・テスト基盤を作らせる](../recipes/build-test-harness.md)
- [観察の道具を作らせる（可視化・集計・ログ）](../recipes/build-observation-tools.md)
- [コンテストの形式別の早見表（AI の効き方と人が握るところ）](format-cheatsheet.md)
- [評価資産を凍結し、触れる範囲を絞る](../enforce/freeze-eval-assets.md)
- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [良すぎる結果を疑う](../verify/suspect-too-good-results.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
