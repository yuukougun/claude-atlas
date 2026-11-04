---
id: test-the-verifier
title: 検証器そのものを確かめる（red/green・手で計算したケース）
nav_title: 検証器そのものを確かめる
aliases: [検証器のテスト, 採点スクリプトの検証, 評価器の red/green]
type: recipe
field: eval
chapter: 検証器を作る
order: 60
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 検証器を使う前に、何もしない解が負け、強い解が勝ち、手で計算した値と一致し、わざと壊した検証器では落ちることを確かめてから凍結できる。
signs:
  - {type: symptom, text: 採点のスクリプト自体にバグがあった}
  - {type: symptom, text: どの方法を試しても点が出ず、何かがおかしい}
  - {type: goal, text: 評価の仕組みが正しく採点しているか確かめてから使いたい}
wave: 1
prerequisites: [verifier-three-conditions]
related: [differential-testing, model-based-grading, freeze-eval-assets, misses-broken-evaluation, build-test-harness, evaluators-by-format, tests-first, pitfalls-of-ai-written-tests]
tracks: []
outdated_advice: []
sources: [anthropic-eng-demystifying-evals-ai-agents, anthropic-eng-building-c-compiler, simonwillison-guides-agentic-engineering-patterns-red]
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guard-first}
  - {title: red/green を検証器に当てる, anchor: red-green}
  - {title: 手で計算したケース, anchor: hand-calculated}
  - {title: わざと壊した検証器で落ちるか, anchor: broken-copy}
  - {title: 入力の生成器の分布を人が見る, anchor: input-distribution}
  - {title: 採点の正本は一か所に, anchor: single-scorer}
  - {title: 確かめてから凍結する, anchor: freeze}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：検証器を凍結する前に、何もしない解が負け、強い解が勝ち、手計算の値と一致し、わざと壊した検証器では落ちることを確かめられる。
    - **いつ引くか**：採点のスクリプト自体にバグがあったとき。どの方法を試しても点が出ず、何かがおかしいとき。評価の仕組みが正しく採点しているかを、使う前に確かめたいとき。
    - **前提**：<!-- link:begin verifier-three-conditions -->[検証器の三条件（正しい・書き換えられない・本番を代表する）](verifier-three-conditions.md)<!-- link:end -->

<!-- textlint-disable -->
別名：検証器のテスト・採点スクリプトの検証・評価器の red/green
<!-- textlint-enable -->

検証器そのものを確かめるとは、解を採点する側のスクリプトに、既知の答えを当ててみることである。検証器が間違っていると、Claude はその間違いを正解として最適化する。確かめる作業は、使い始める前と、検証器を直すたびに行う。

## 先に整える守り {#guard-first}

検証器を確かめる前に、何を確かめるのかを決める。検証器が満たすべき 3 条件のうち、このページが確かめるのは「正しい」である。<!-- link:begin verifier-three-conditions#correct -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 正しい](verifier-three-conditions.md#correct)<!-- link:end --> に条件の中身がある。

- 書き換えられないことは、確かめた後に凍結して守る。ここでは「確かめてから凍結する」の節で扱い、設定の詳細は <!-- link:begin freeze-eval-assets -->[評価資産を凍結し、触れる範囲を絞る](../enforce/freeze-eval-assets.md)<!-- link:end --> が持つ。
- 本番を代表することは、このページでは入力の分布を人が見るところまでを扱う。残りは <!-- link:begin verifier-three-conditions#representative -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 本番を代表する](verifier-three-conditions.md#representative)<!-- link:end --> を見る。
- 検証器のテストは、Claude に書かせてよい。ただし検証器自体と凍結済みのテストは、書かせる作業の中で変えさせない。テストを通すために検証器を曲げる道を、先に塞ぐためである。新しいテストは提案用の場所に書かせ、人が読んでから凍結する場所へ移す。

Claude 側の原因は「確かめていない」である。並列の Claude 群で C コンパイラを作った Anthropic の報告は、エージェントは与えられた問題を解く、と指摘している。だから検証器はほぼ完璧でなければならない、と結論する（根拠：中）。完璧にするには、検証器を人が確かめる手が要る。

## red/green を検証器に当てる {#red-green}

red/green とは、テストが先に失敗する（red）ことを確かめてから、通る（green）状態にする進め方である。Simon Willison がコーディングエージェント向けに勧めている。これを検証器に当てはめると、凍結する前に、次の表の確認を通すことになる（類推）。実装のテストを先に書く進め方の一般形は <!-- link:begin tests-first#steps -->[テストを先に書かせる › 手順](../verify/tests-first.md#steps)<!-- link:end --> にある。

| 当てるもの | 期待 | 期待と違ったとき疑うこと |
| --- | --- | --- |
| 何もしない解（空の出力・初期のまま） | 最低点か不正解になる | 出力の有無を見ずに点を付けている |
| ランダムな解 | 低い点で、強い解より必ず下になる | 採点が入力に依らない。点の計算が入力を読んでいない |
| 明らかに強い解 | 満点か、ほかの解より必ず上になる | 採点の式の向きが逆。出力の形式を読み違えている |
| 手で計算したケース | 手計算の値と一致する | 採点の式、丸め、許容誤差 |
| わざと壊した検証器 | テストが落ちる | テストが弱い |

表の上 3 行は、検証器を使うたびに安く回せる。「明らかに強い解」は、手で書いた単純だが確実に高得点になる解や、過去の良い提出を使う。手計算とわざと壊したコピーは、この後の 2 つの節で扱う。対戦型は、先後を入れ替えた同一ボット同士の勝率が 0.5 からずれないことも確かめる（推論）。この確認は対戦型に固有なので、<!-- link:begin evaluators-by-format#arena -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場） › 対戦型：対戦場と基準のボット](../contest/evaluators-by-format.md#arena)<!-- link:end --> に譲る。

各段の終わりの確かめは、次のとおりである。

1. 何もしない解を当てる。終わりの確かめ：最低点か不正解が返り、満点が出ていない。
2. ランダムな解を当てる。終わりの確かめ：強い解より低い点が返る。
3. 明らかに強い解を当てる。終わりの確かめ：満点か、ほかより上の点が返る。

この 3 つと、後の 2 つの確認を Claude に書かせる依頼の雛形が次である。実行の前に期待を書かせること、手計算の根拠を残させること、検証器を変えさせないことを足してある。

<!-- gen:begin snippet test-the-verifier/red-green-prompt -->
<!-- textlint-disable -->

??? example "雛形：検証器の red/green テストを書かせる依頼"

    ```markdown
    検証器 `eval/score.py`（解の出力を読んで点を返すスクリプト）が正しく採点するかを確かめるテストを書いてほしい。検証器そのものは直さない。

    - 書く場所：`tests/proposed/test_score.py`。`tests/frozen/` には書かない。人が読んでから移す。
    - 当てるもの：何もしない解（空の出力）、ランダムな解、明らかに強い解（`baseline/strong.py`）、手で計算できる小さなケース。それぞれの期待を、実行する前にテストの冒頭のコメントへ書く。
    - 手で計算したケース：期待の値は、検証器を実行して得た値ではなく、入力から手で計算した値を書く。計算の過程もコメントに残す。
    - わざと壊した検証器：`eval/score.py` のコピーを `tests/proposed/broken/` に置き、採点の符号を逆にする・端のケースを数え落とすなど、1 か所ずつ壊す。壊したコピーに当てると、テストが落ちることを確かめる。
    - 変えないもの：`eval/score.py` と既存のテスト。テストを通すために検証器を変えない。
    - 最後の報告：テストごとに、本物の検証器に当てた結果（通った・落ちた）と、壊したコピーに当てた結果を表で貼る。壊したコピーで落ちなかったものは、その理由の推測を添える。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet test-the-verifier/red-green-prompt -->

## 手で計算したケース {#hand-calculated}

手で計算したケースとは、入力が小さく、正しい点を人が手で出せる例である。期待の値は、入力から手で計算して決める。検証器を実行して出た値を期待に写すと、検証器のバグを正解に固めることになる（<!-- link:begin pitfalls-of-ai-written-tests#pinning-bugs -->[AI に書かせたテストの落とし穴 › 今の挙動を正解として固める](../verify/pitfalls-of-ai-written-tests.md#pinning-bugs)<!-- link:end --> を参照）。

- 小さなケースを数件選ぶ。点が自明なもの、端にあたるもの（空の入力・最小の入力・同点）を入れる。
- 計算の過程をテストのコメントに残す。後から食い違ったとき、どちらが間違いかを追える。
- 端数の出るケースを 1 件入れる。Anthropic の記事には、正しい答えの 96.12 を、検証器が 96.124991… と一致しないとして落としていた例がある（根拠：中）。許容誤差が意図どおりに働くかは、手計算のケースで見える。

!!! example "判断例：手計算の値と検証器の出力が食い違った"
    - **状況**：手で計算した点は 18 だが、検証器は 17 を返した。
    - **迷う候補**：検証器のバグとして直す。手計算の誤りとして期待の値を直す。
    - **選んだもの**：まず手計算を別の方法でやり直し、それでも 18 なら検証器を調べる。
    - **理由**：どちらも間違いうる。検証器を先に直すと、手計算の誤りに合わせて正しい検証器を壊すことがある。大きな入力で食い違うなら、答えの分かる遅い解と比べる <!-- link:begin differential-testing#steps -->[答えの分かる遅い解と比べる（差分テスト・オラクル） › 手順](differential-testing.md#steps)<!-- link:end --> が使える。

## わざと壊した検証器で落ちるか {#broken-copy}

わざと壊した検証器とは、本物の検証器のコピーに誤りを 1 か所だけ入れたものである。このコピーに検証器のテストを当てて、落ちることを確かめる。落ちなければ、そのテストは検証器の誤りを見つけられない。

1. 検証器をコピーして別の場所に置く。凍結するファイルとは混ぜない。
2. 誤りを 1 か所だけ入れる。例：点の符号を逆にする。端のケースを数え落とす。許容誤差を広げる。出力を読まずに満点を返す。
3. 壊したコピーにテストを当てる。終わりの確かめ：誤りごとに、少なくとも 1 件のテストが落ちる。
4. 落ちなかった誤りは、テストを足してから、もう一度壊したコピーに当てる。

通るだけのテストの見つけ方は <!-- link:begin pitfalls-of-ai-written-tests#test-strength -->[AI に書かせたテストの落とし穴 › テストの強さを確かめる](../verify/pitfalls-of-ai-written-tests.md#test-strength)<!-- link:end --> が持つ。

!!! example "判断例：壊したコピーでもテストが通った"
    - **状況**：許容誤差を広げたコピーに当てても、検証器のテストが全部通った。
    - **迷う候補**：許容誤差の端を突くテストを足す。許容誤差は使い道が狭いので、検証器から外す。
    - **選んだもの**：端を突くテストを足す。
    - **理由**：許容誤差を外すと、浮動小数の採点が不安定になる。テストの穴は、足せば閉じる。ただし、その許容誤差を使う課題が 1 つもないと分かっているなら、外す選択も筋が通る。

## 入力の生成器の分布を人が見る {#input-distribution}

入力の生成器とは、検証器に流すテスト入力を作るスクリプトである。競技の課題では、規約の範囲を均等に、かつ端を重点的にサンプルするのが基本になる。生成した入力のパラメータの分布をヒストグラムにして、人が規約と突き合わせる（実践の報告に基づく）。

- 多数の入力を生成し、規約にあるパラメータ（大きさ・値の範囲・個数）ごとにヒストグラムを描く。
- 規約の範囲の外に出ていないか、端の値が出ているか、特定の範囲に偏っていないかを人が見る。
- 一般化すると、テストデータの分布を人が確かめる、ということになる（類推）。分布が偏った入力で高得点でも、本番での勝ちは意味しない。本番を代表するかどうかは <!-- link:begin verifier-three-conditions#representative -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 本番を代表する](verifier-three-conditions.md#representative)<!-- link:end --> で問う。

ヒストグラムを描くスクリプトは Claude に書かせてよい。ヒストグラムを見て、規約と合うかを判断するのは人である。

## 採点の正本は一か所に {#single-scorer}

採点の正本とは、点を計算する唯一の場所である。ビジュアライザや集計のスクリプトは、点を独自に再計算せず、検証器の出力を読むだけにする。採点のロジックが二重になると、食い違ったときにどちらが正しいか分からなくなる。確かめる対象も増える（実践の報告に基づく）。

- 検証器は、点と内訳（ケースごとの点など）をファイルに出力する。
- 周辺のツールは、そのファイルを読んで表示と集計だけを行う。
- Claude に周辺のツールを作らせるときは、依頼に「点の計算を再実装しない。検証器の出力を読む」と書く。

## 確かめてから凍結する {#freeze}

検証器は、red/green の表・手計算のケース・壊したコピーの確認をすべて通してから凍結する。凍結とは、検証器とそのテストを、作業する側が書き換えられない状態にすることである。

1. 新しいテストを `tests/proposed/` に書かせる。
2. 人が読む。期待の値の根拠、壊したコピーで落ちるか、分布のヒストグラムを見る。
3. 通ったテストを `tests/frozen/` へ移す。移すのは人である。
4. 凍結済みの場所への書き込みを、設定で止める。

凍結の対象と止め方は、<!-- link:begin freeze-eval-assets#what-to-freeze -->[評価資産を凍結し、触れる範囲を絞る › 凍結するものと触らせるもの](../enforce/freeze-eval-assets.md#what-to-freeze)<!-- link:end --> と <!-- link:begin freeze-eval-assets#how-to-freeze -->[評価資産を凍結し、触れる範囲を絞る › 設定で止める（権限ルール・サンドボックス・ファイルの権限）](../enforce/freeze-eval-assets.md#how-to-freeze)<!-- link:end --> にある。止めた後に効いているかの確認は <!-- link:begin freeze-eval-assets#check -->[評価資産を凍結し、触れる範囲を絞る › 凍結が効いているかを確かめる](../enforce/freeze-eval-assets.md#check)<!-- link:end --> で行う。

全体の確かめ方は、次のチェックである。

- 何もしない解・ランダムな解が負け、強い解が勝つ。
- 手計算のケースで点が一致している。期待の値は手計算で決めた。
- わざと壊したコピーを、テストが誤りごとに落としている。
- 入力の分布のヒストグラムを、人が規約と突き合わせた。
- 点の計算は検証器の 1 か所にだけある。

検証器を直したら、凍結を外し、この確認を最初からやり直す。直した検証器で前の確認が通るとは限らない。

## 失敗したとき {#when-it-fails}

確認が通らないとき、まず検証器を疑う。Claude の解や課題を疑うのは、その後である。

- 壊したコピーでテストが落ちない：テストが弱い。壊したコピーの節に戻って、テストを足す。
- 多数の試行で 0% のまま：たいてい課題か検証器が壊れている。Anthropic の記事に出る経験則である。同じ記事では、Opus 4.5 の CORE-Bench が最初 42% だった。厳しすぎる採点、あいまいな課題の仕様、厳密には再現できない確率的な課題を直し、さらに制約の少ない scaffold に替えて 95% になった。それぞれの寄与は書かれていない（根拠：中）。
- 手元の評価は良いのに本番で通用しない：<!-- link:begin misses-broken-evaluation#diagnosis -->[手元の評価は良いのに本番で通用しない › 原因を安く確かめる順](../symptoms/misses-broken-evaluation.md#diagnosis)<!-- link:end --> で、原因を安く確かめる順に切り分ける。
- 検証の環境ごと Claude に作らせた：作った環境の確かめは <!-- link:begin build-test-harness#check-the-harness -->[検証環境・テスト基盤を作らせる › 作った環境を確かめる](../recipes/build-test-harness.md#check-the-harness)<!-- link:end --> にある。形式ごとの違いは <!-- link:begin evaluators-by-format -->[形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](../contest/evaluators-by-format.md)<!-- link:end --> を見る。
- 採点を Claude に任せている：人の判定との較正が先である。<!-- link:begin model-based-grading#calibrate -->[Claude に採点させる（人の判定で較正する） › 人の判定と比べて較正する](model-based-grading.md#calibrate)<!-- link:end --> を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)：Anthropic・英語・確認日 2026-11-04
- [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/research/building-c-compiler)：Anthropic・英語・確認日 2026-11-04
- [Red/green TDD - Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)：Simon Willison・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器の三条件（正しい・書き換えられない・本番を代表する）](verifier-three-conditions.md)

**関連**

- [答えの分かる遅い解と比べる（差分テスト・オラクル）](differential-testing.md)
- [Claude に採点させる（人の判定で較正する）](model-based-grading.md)
- [評価資産を凍結し、触れる範囲を絞る](../enforce/freeze-eval-assets.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [検証環境・テスト基盤を作らせる](../recipes/build-test-harness.md)
- [形式別の評価器（テスタ・ベンチマーカー・CV・flag・対戦場）](../contest/evaluators-by-format.md)
- [テストを先に書かせる](../verify/tests-first.md)
- [AI に書かせたテストの落とし穴](../verify/pitfalls-of-ai-written-tests.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
