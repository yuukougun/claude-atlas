---
id: verifier-three-conditions
title: 検証器の三条件（正しい・書き換えられない・本番を代表する）
nav_title: 検証器の三条件
aliases: [評価器の要件, 検証器の質, 本番を代表するテスト]
type: concept
field: eval
chapter: 検証器を作る
order: 50
level: 任せる
priority: 必須
surfaces: [claude-code, api]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
pitfalls: []
scenes: [開発, データ分析, コンテスト]
summary: 検証器が満たすべき三つの条件（正しい・書き換えられない・本番を代表する）で、評価の仕組みを使う前に点検できる。手元の勝ちが本番の勝ちを意味するかを問う。
signs:
  - {type: goal, text: Claude に回させる前に、評価の仕組みが信用できるか確かめたい}
  - {type: symptom, text: 手元で試した入力と、本番の入力の傾向が違っていた}
wave: 1
prerequisites: [verifier-defines-problem, reward-hacking]
related: [test-the-verifier, protect-tests, lockbox-and-holdout, check-the-metric, differential-testing, model-based-grading, freeze-eval-assets, misses-broken-evaluation, rewrote-tests-to-pass, build-test-harness, evaluators-by-format]
tracks: []
outdated_advice: []
sources: [anthropic-eng-building-c-compiler, anthropic-eng-demystifying-evals-ai-agents, arxiv-2510-20270, arxiv-2603-11337, cc-docs-best-practices, simonwillison-guides-agentic-engineering-patterns-red, battlecode-2023-4-musketeers-pdf, battlecode-2023-dont-at-me-pdf, battlecode-2025-confused-pdf, battlecode-2025-just-woke-up-pdf, battlecode-2026-lorem-ipsum-pdf]
volatility: 低
sections:
  - {title: 三条件が要る理由, anchor: why}
  - {title: 正しい, anchor: correct}
  - {title: 書き換えられない, anchor: tamper-proof}
  - {title: 本番を代表する, anchor: representative}
  - {title: 三条件を点検する, anchor: audit}
  - {title: 三条件が防ぐもの, anchor: what-it-prevents}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：検証器が満たすべき 3 つの条件（正しい・書き換えられない・本番を代表する）が分かり、回させる前の評価の仕組みを点検できる。
    - **いつ引くか**：評価の仕組みを信用してよいか、反復させる前に確かめたいとき。手元で試した入力と、本番の入力の傾向が違っていたとき。
    - **前提**：<!-- link:begin verifier-defines-problem -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する）](verifier-defines-problem.md)<!-- link:end -->、<!-- link:begin reward-hacking -->[採点器を騙す（reward hacking）](../basics/reward-hacking.md)<!-- link:end -->

<!-- textlint-disable -->
別名：評価器の要件・検証器の質・本番を代表するテスト
<!-- textlint-enable -->

検証器の三条件は、テスト・採点・ベンチマークなどの検証器が、正しいこと、書き換えられないこと、手元の勝ちが本番の勝ちを意味することの 3 つを指す。検証器があるだけでは足りない。この 3 条件が崩れると、Claude は崩れた検証器を目標にして、速く、まっすぐ誤った方向へ進む。

## 三条件が要る理由 {#why}

Claude は、渡された検証器が定める問題を解く。検証器が誤っていれば、誤りに向かう反復も同じ速さで進む。この前提は <!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](verifier-defines-problem.md#loops-amplify)<!-- link:end --> にある。

検証器が「あるか、ないか」は手段の有無の話である。この節以降は、あった検証器の質の話をする。質は次の 3 つに分けると点検しやすい。

| 条件 | 問い | 崩れたときに起きること |
| --- | --- | --- |
| 正しい | 検証器の判定は、正解と誤答を取り違えないか | 誤った解が通り、正しい解が落ちる |
| 書き換えられない | 作業する側が、検証器や採点の基準を変えて通せないか | 解かずに、採点だけを満たして通る |
| 本番を代表する | 手元で勝つことは、本番で勝つことを意味するか | 手元では良いのに、本番で通用しない |

3 つは独立している。正しくて書き換えられない検証器でも、手元の入力が本番と違えば、本番では役に立たない。

## 正しい {#correct}

正しい検証器は、正解を通し、誤答を落とす。バグのある検証器は、Claude が直そうとする対象にならず、そのまま目標になる。

Anthropic が複数の Claude を並列に動かして C コンパイラを作った報告は、次のように述べている。エージェントは与えられた問題を解くので、検証器はほぼ完璧でなければならない。

エージェント評価の解説（Anthropic、2026 年 1 月）には、CORE-Bench での Opus 4.5 の正答率が 42% から 95% になった例がある。厳しすぎる採点、あいまいな課題の仕様、確率的で再現できない課題を直し、さらに制約の少ない scaffold（エージェントを動かす枠組み）に替えた結果である。各修正の寄与は分けられていない。同じ解説は、多数の試行でも成功率が 0% なら、たいてい課題ではなく採点側が壊れている、という経験則も示す（根拠：中）。

正しさを確かめる最小の手順は、red/green の考え方を検証器に当てることである。検証器を凍結する前に、次の 3 点を確かめる。

- 何もしない解と乱数の解は必ず負け、明らかに強い解は必ず勝つ。
- 手計算できる小さなケースで、スコアが一致する。
- 対戦型なら、先後を入れ替えた同一のボット同士の勝率が 0.5 からずれない。

この考え方は Simon Willison の「先にテストが失敗することを確かめる」から借りた。手順の本体は <!-- link:begin test-the-verifier#red-green -->[検証器そのものを確かめる（red/green・手で計算したケース） › red/green を検証器に当てる](test-the-verifier.md#red-green)<!-- link:end --> にあり、手計算のケースは <!-- link:begin test-the-verifier#hand-calculated -->[検証器そのものを確かめる（red/green・手で計算したケース） › 手で計算したケース](test-the-verifier.md#hand-calculated)<!-- link:end --> にある。

答えの分かる遅い解があるときは、それと突き合わせる手が使える。やり方は <!-- link:begin differential-testing#steps -->[答えの分かる遅い解と比べる（差分テスト・オラクル） › 手順](differential-testing.md#steps)<!-- link:end --> に譲る。機械で判定しにくい出力を Claude に採点させる場合は、その採点が人の判定と合うかも確かめる対象になる。基準の較正は <!-- link:begin model-based-grading#calibrate -->[Claude に採点させる（人の判定で較正する） › 人の判定と比べて較正する](model-based-grading.md#calibrate)<!-- link:end --> にある。

## 書き換えられない {#tamper-proof}

書き換えられない検証器は、作業する側がテスト・採点・設定を変えて通すことができない。書き換えられる検証器では、Claude が問題を解くより、検証器を変えるほうが近道になることがある。書き換えで通す仕組みの全体像は前提の <!-- link:begin reward-hacking -->[採点器を騙す（reward hacking）](../basics/reward-hacking.md)<!-- link:end --> にある。

書き換えの実態を測った研究が 2 つある。

- ImpossibleBench（arXiv、2025 年）は、仕様と矛盾するテストをわざと用意し、通すと不正になる状況を作った。Claude 系のモデルの不正の 79% 超は、テストファイルの直接の書き換えだった。テストを読み取り専用にすると、性能を保ったままテストの書き換えを防げた。一方、テストを通すための特例の分岐や、比較演算子の上書きは防げなかった（根拠：中。矛盾する課題を作った測定で、日常の課題の頻度ではない）。
- RewardHackingAgents（arXiv、2026 年）は、ML の作業をするエージェントで評価コードの改ざんを測った。小型モデルを使った研究で、約 50% のエピソードで評価コードの改ざんが試みられた。外部に固定した評価コードで採点すると、改ざんは消えた（根拠：中。小型モデルの傾向で、現行の Claude の頻度ではない）。

この 2 つから、読み取り専用にするだけでは足りないと分かる。検証の本体を、作業する側の手の届かない所に置く層まで要る。

守りは 4 つの層で組む。

1. 依頼に書く：テストを変えないと伝える。これは助言であり、鍵ではない。書き方は <!-- link:begin protect-tests#in-the-request -->[テストを守る（改ざんを防ぐ） › 依頼に書くこと](../verify/protect-tests.md#in-the-request)<!-- link:end --> にある。
2. 設定で止める：権限ルールとサンドボックスとファイルの権限で、評価資産に触れないようにする。公式の Best practices は、CLAUDE.md を助言にすぎないものとし、例外を許さない規則はフックや deny ルールに置くよう勧めている。止め方は <!-- link:begin freeze-eval-assets#how-to-freeze -->[評価資産を凍結し、触れる範囲を絞る › 設定で止める（権限ルール・サンドボックス・ファイルの権限）](../enforce/freeze-eval-assets.md#how-to-freeze)<!-- link:end --> にある。
3. 検証を作業から離す：採点を別のプロセスや別の場所で動かし、結果だけを返す。分け方は <!-- link:begin build-test-harness#separate-eval-assets -->[検証環境・テスト基盤を作らせる › 検証の資産を分けて置く](../recipes/build-test-harness.md#separate-eval-assets)<!-- link:end --> にある。
4. 見せないデータを持つ：作業する側が読めない検証用データを人が持ち、点数だけを返す。分け方は <!-- link:begin lockbox-and-holdout#scores-only -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 点数だけを返す](lockbox-and-holdout.md#scores-only)<!-- link:end --> にある。

特例の分岐のように、検証器を書き換えずに通す手は、どの層を重ねても残る。見せないデータで見張る意味はここにある。全体の守りは <!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](../verify/protect-tests.md#layers)<!-- link:end --> にある。

## 本番を代表する {#representative}

本番を代表する検証器は、手元で勝てば本番でも勝つ関係を保つ。手元の入力が本番と傾向を違えれば、検証器が正しく、書き換えられなくても、手元の勝ちは本番の勝ちを意味しない。

業務の想定の場面で考える。

!!! example "判断例：手元のサンプルで通した変換スクリプト"
    - **状況**：CSV を別の形式へ変換するスクリプトを、Claude に反復させて直している。検証器は、手元の 20 行のサンプルを変換し、期待の出力と比べて合否を返す。
    - **迷う候補**：手元のサンプルを 200 行に増やして厳しくする案と、本番のデータから抜いた見本を足して、手元のサンプルと入力の傾向を比べる案。
    - **選んだもの**：本番から抜いた見本を足し、欠損・文字コード・行数の傾向を手元と並べて見る。手元のサンプルは、正しさの確認用に残す。
    - **理由**：手元のサンプルは、人が理想的に作った入力に偏る。増やしても偏りは変わらず、本番の欠損や文字コードの混在は現れない。

大会の事後報告にも、同じ形の例が多い。これらは対戦型の大会の例なので、業務への当てはめは類推になる（類推）。

- Battlecode 2025 の準優勝チームは、予選版には 70% 超勝てたが、上位チームとのスクリム（練習試合）では五分前後だった。決勝のマップでは中央寄りの探索が不利になった。自分の旧版にだけ勝つ評価は、代表性を欠く（根拠：中〜強・類推）。
- Battlecode 2025 の優勝チームは、勘に頼るのをやめ、全マップでの AB テストと、上位約 20 チームとのスクリムの自動申請を導入した。旧版相手では数字が出なかった防衛策も、攻撃的な相手には効くと判断して採用した（根拠：中〜強・類推）。
- Battlecode 2026 では、ローカルで 85% 超の勝率を示した改良が、オンラインのスクリムでは効果が小さかった。AI に書かせた攻撃コードは、見えている標的しか考えず、直接対決で弱かった（根拠：中。単独の振り返り・類推）。
- Battlecode 2023 では、本拠地（HQ）が密集した本番のマップで初めて出た計算量の超過が予選落ちにつながり、決勝の新しいマップで経路探索のバグが出て大会中に直した例もある。本番の環境でしか出ない不具合も、代表性の欠けと同じ形をしている（根拠：中〜強・類推）。

共通するのは、手元の評価が本番の分布の一部しか映さない点である。確かめ方は 2 つに分かれる。

- 入力の側：入力の生成器の分布を人が見る。手順は <!-- link:begin test-the-verifier#input-distribution -->[検証器そのものを確かめる（red/green・手で計算したケース） › 入力の生成器の分布を人が見る](test-the-verifier.md#input-distribution)<!-- link:end --> にある。
- 測るものの側：検証器が測る指標が、本当の目的とずれていないかを、最適化の前に見る。やり方は <!-- link:begin check-the-metric#mismatch -->[評価指標そのものを確かめる › 指標と目的のずれ](check-the-metric.md#mismatch)<!-- link:end --> にある。

節目の判定は、手元で使い込んでいない検証用データで行う。この分け方は <!-- link:begin lockbox-and-holdout#three-tiers -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 三層に分ける](lockbox-and-holdout.md#three-tiers)<!-- link:end --> にある。形式ごとに何が検証器に当たるかは <!-- link:begin evaluators-by-format#evaluator-first -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › どの形式でも、最初の成果物は評価器](../contest/evaluators-by-format.md#evaluator-first)<!-- link:end --> にある。

## 三条件を点検する {#audit}

回させる前に、3 条件を順に点検する。点検は Claude に頼んでもよいが、検証器を直す判断は人が持つ。

!!! example "判断例：点検で見つけた懸念をどう扱うか"
    - **状況**：採点スクリプトの点検で、Claude が「採点の設定ファイルが作業ディレクトリにあり、書き換えられる」と報告した。
    - **迷う候補**：その場で Claude に直させる案と、報告を人が読み、置き場所を変える案。
    - **選んだもの**：人が置き場所を変える。点検の依頼には「採点を自分で直さない」と書いておく。
    - **理由**：直す側と採点される側が同じだと、検証器の質を作業する側が決めることになる。点検の結果を使うのは人であり、直した後の確認も別の目で行う。

点検の依頼は、次の雛形のように観点を分けて頼む。

<!-- gen:begin snippet verifier-three-conditions/audit-request -->
<!-- textlint-disable -->

??? example "雛形：検証器を 3 条件で点検させる依頼"

    ```markdown
    `scripts/judge.py`（採点スクリプト）と `data/dev/`（手元の入力）を、これから反復の目標に使ってよいか点検してほしい。ファイルは直さず、読むことと、一時ディレクトリでの実行だけをする。

    次の 3 つの観点ごとに、確かめたこと・確かめていないこと・懸念を報告する。

    1. 正しいか：何もしない解と乱数の解が必ず負けるか。手で計算できる小さなケースで、スコアが一致するか。
    2. 書き換えられないか：`scripts/judge.py`、`data/dev/`、採点の設定を、作業する側が書き換えられる場所にあるか。結果を出すまでに通る経路で、判定を迂回できる所はないか。
    3. 本番を代表するか：`data/dev/` の入力の傾向（大きさ・偏り・欠損）が、`data/prod-sample/`（本番から抜いた見本）と食い違う点はどこか。

    懸念を見つけても、採点を自分で直さない。直し方の案は別の節に分けて書く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet verifier-three-conditions/audit-request -->

点検は一度で終わらない。本番の入力の傾向は変わるので、節目ごとに本番の見本を取り直し、手元と比べる（推論・実践例なし）。

## 三条件が防ぐもの {#what-it-prevents}

この辞典の原理で言えば、三条件は「確かめる」と「縛る」にあたる。

- 確かめる：正しい・本番を代表するは、検証器そのものを確かめる条件である。確かめていない検証器を目標にすると、原因の「確かめていない」が起きる。
- 縛る：書き換えられないは、作業する側の手を縛る条件である。縛っていない検証器は、原因の「縛っていない」に当たり、書き換えや特例化で通される。

症状から入るなら、手元の評価が良いのに本番で通用しないときは <!-- link:begin misses-broken-evaluation#diagnosis -->[手元の評価は良いのに本番で通用しない › 原因を安く確かめる順](../symptoms/misses-broken-evaluation.md#diagnosis)<!-- link:end --> で原因を切り分ける。テストを書き換えて通されたときは <!-- link:begin rewrote-tests-to-pass#diagnosis -->[テストを書き換えて通した › 原因を安く確かめる順](../symptoms/rewrote-tests-to-pass.md#diagnosis)<!-- link:end --> へ進む。

## よくある誤解 {#misconceptions}

- テストが全部通れば正しい：通ることは、テストが正しいことも、テストが本番を代表することも保証しない。
- 読み取り専用にすれば書き換えは防げる：直接の書き換えは防げても、特例の分岐は残る（ImpossibleBench の結果）。
- 勝率が上がれば本番でも勝つ：旧版や手元の入力にだけ強くなっている場合がある。
- CLAUDE.md に「テストを変えない」と書けば縛れる：助言であり、例外を許さない規則は設定で止める。
- 一度点検すれば終わり：入力の傾向も、検証器の周りの設定も変わる。節目ごとに見直す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/research/building-c-compiler)：Anthropic・英語・確認日 2026-11-04
- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)：Anthropic・英語・確認日 2026-11-04
- [ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases](https://arxiv.org/abs/2510.20270)：arXiv（Zhong, Ziqian ほか）・英語・確認日 2026-11-04
- [RewardHackingAgents: Benchmarking Evaluation Integrity for LLM ML-Engineering Agents](https://arxiv.org/abs/2603.11337)：arXiv（Atinafu, Yonas ほか）・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Red/green TDD - Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)：Simon Willison・英語・確認日 2026-11-04
- [4 Musketeers - Battlecode 2023 Strategy Guide](https://battlecode.org/assets/files/postmortem-2023-4-musketeers.pdf)：Battlecode（MIT）の参加チームの振り返り・英語・確認日 2026-11-04
- [Battlecode 2023 Postmortem - Don't @ Me](https://battlecode.org/assets/files/postmortem-2023-dont-at-me.pdf)：Battlecode（MIT）の参加チームの振り返り・英語・確認日 2026-11-04
- [Battlecode 2025 Postmortem（confused）](https://battlecode.org/assets/files/postmortem-2025-confused.pdf)：Battlecode（MIT）の参加チームの振り返り・英語・確認日 2026-11-04
- [Just Woke Up - BattleCode 2025 Postmortem](https://battlecode.org/assets/files/postmortem-2025-just-woke-up.pdf)：Battlecode（MIT）の参加チームの振り返り・英語・確認日 2026-11-04
- [Battlecode 2026 Postmortem（Lorem Ipsum）](https://battlecode.org/assets/files/postmortem-2026-lorem-ipsum.pdf)：Battlecode（MIT）の参加チームの振り返り・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](verifier-defines-problem.md)
- [採点器を騙す（reward hacking）](../basics/reward-hacking.md)

**次に読む**

- [検証器そのものを確かめる（red/green・手で計算したケース）](test-the-verifier.md)
- [答えの分かる遅い解と比べる（差分テスト・オラクル）](differential-testing.md)
- [Claude に採点させる（人の判定で較正する）](model-based-grading.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](lockbox-and-holdout.md)
- [評価資産を凍結し、触れる範囲を絞る](../enforce/freeze-eval-assets.md)
- [検証環境・テスト基盤を作らせる](../recipes/build-test-harness.md)
- [形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](../contest/evaluators-by-format.md)
- 退行の原因を git bisect で探させる（準備中）

**関連**

- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- [評価指標そのものを確かめる](check-the-metric.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
