---
id: open-ended-loop-trap
title: AI に改善を回させ続ける罠（開いたループ）
nav_title: 開いた改善ループの罠
aliases: [開いた改善ループ, 自律改善ループ, 回し続ければ良くなる]
type: concept
field: delegate
chapter: 任せる前の判断
order: 50
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: [やめられない, 体感を信じる]
scenes: [開発, コンテスト, データ分析]
summary: 戦略そのものを AI に改善させ続ける開いたループが、手元の評価への過適合を自動で進めてしまう理由が分かる。反復させるのは、仕様が決まり停止条件のある実装の作業に限る。
signs:
  - {type: goal, text: AI に改善をずっと回させておきたい}
  - {type: situation, text: 方針や手法の改善まで、AI に自動で回させている}
  - {type: goal, text: AI に回させる反復を、どこまでに限るか決めたい}
prerequisites: [selection-pressure]
related: [verifier-defines-problem, goal-until-done, compare-hypotheses-in-parallel, lockbox-and-holdout, check-the-metric, suspect-too-good-results, reward-hacking, decide-when-to-quit, misses-broken-evaluation, stuck-in-a-check-loop, wont-rethink-approach, what-not-to-delegate, five-questions-before-delegating]
sources: []
volatility: 低
sections:
  - {title: 閉じた反復と開いたループ, anchor: closed-vs-open}
  - {title: 長く回せば良くなるとは限らない, anchor: longer-is-not-better}
  - {title: なぜ手元の評価に合わせ込まれるのか, anchor: why}
  - {title: 何に効くか, anchor: what-it-affects}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：戦略そのものを AI に改善させ続ける開いたループが、手元の評価への過適合を自動で進める理由が分かる。
    - **いつ引くか**：AI に改善をずっと回させておきたいとき。方針や手法の改善まで AI に自動で回させているとき。回させる反復をどこまでに限るか決めたいとき。
    - **前提**：<!-- link:begin selection-pressure -->[選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)<!-- link:end -->

<!-- textlint-disable -->
別名：開いた改善ループ・自律改善ループ・回し続ければ良くなる
<!-- textlint-enable -->

AI に改善を回させ続ける罠とは、実装だけでなく方針や手法の改善まで AI に任せ、手元の評価で良かった版を自動で選び続けることで、手元の評価にだけ合った成果物ができあがる現象である。反復させてよいのは、仕様が決まり、停止条件があり、採否を人が握る実装の作業に限る。

## 閉じた反復と開いたループ {#closed-vs-open}

閉じた反復は、仕様の決まった実装を、停止条件に着くまで繰り返す作業である。開いたループは、何を良しとするかの側、つまり方針・手法・戦略まで AI が変え続け、変えた結果を同じ手元の評価で選び続ける仕組みである。

違いは、人が握る点を残すかどうかである。

| 観点 | 閉じた反復 | 開いたループ |
| --- | --- | --- |
| AI が変えるもの | 仕様に沿った実装 | 方針・手法・戦略そのもの |
| 止まる条件 | 着手前に決めた停止条件 | 決まっていない。人が止めるまで続く |
| 採否 | 人が握る | 手元の評価の点数で自動に決まる |
| 手元の評価への過適合 | 反復の範囲が狭く、人が採否の前に確かめられる | 回すほど自動で進む |

開いたループの組み方は、このページでは扱わない。閉じた反復の組み方は <!-- link:begin goal-until-done#spec-tasks-only -->[/goal（完了するまで続けさせる） › 仕様の決まった実装に限る](goal-until-done.md#spec-tasks-only)<!-- link:end --> を見る。

!!! example "判断例：予測モデルの改善を一晩任せる"
    - **状況**：データ分析で、予測モデルの検証スコアを上げたい。Claude Code に一晩かけて改善を回させたい。
    - **迷う候補**：特徴量の選び方からモデルの種類まで、方針ごと任せてスコアが上がる版を採り続ける案。方針は人が決め、特徴量を 1 つ足す実装だけを、仕様と停止条件を付けて反復させる案。
    - **選んだもの**：後者。採否は、AI に見せていない検証用のデータで人が決める。
    - **理由**：前者は方針の変更と採否を同じ手元の評価が自動で決めるので、朝には評価の穴に合わせ込んだ版が残りやすい。後者は変えるものが狭く、採否の前に人が確かめる点を残せる。

## 長く回せば良くなるとは限らない {#longer-is-not-better}

開いたループを長く回しても、成果が伸び続けるとは限らない。伸びが止まった後の延長は、時間と金を使うだけに終わることがある。

- **頭打ちの事例**：Claude Code をループで回してエージェントを最適化する実験で、最良の構成を早い段階で見つけた後は頭打ちになり、延長しても時間と金の無駄だった（根拠：中。単独の実験で、対象のモデルと版は確かめていない）。
- **競技の事例**：CTF では AI の優位が序盤に集中し、ISUCON では数時間で頭打ちになったという報告がある。時間の効き方は競技の形式で違う（根拠：中。時点依存）。
- **逆の事例**：DrivenData の競技では、Codex の run を 9 日間に延ばしたところ、12 位から 7 位に上がった（根拠：弱。単独の事例）。

頭打ちの事例も逆の事例も、単独の報告である。延長が効くかどうかは、課題と評価によって違う。ここから引ける結論は、回す時間の長さを成果の根拠にしないことだけである。伸びが手元の評価の点数だけなのか、本番に近い評価でも出ているのかを、先に確かめる。

## なぜ手元の評価に合わせ込まれるのか {#why}

開いたループは、手元の評価で良かった版を選び続けるので、評価の穴（手元の評価では点が取れても、本番の目的とはずれている所）に合わせ込む力が働く。この力は AI が正直でも働く。仕組みの本体は <!-- link:begin selection-pressure#why -->[選択圧：良かった版を選び続ける罠 › なぜ正直でも外れるか](../eval/selection-pressure.md#why)<!-- link:end --> にある。

開いたループでは、方針や手法の変更も、その採否も、同じ手元の評価に任される。人が止める点がないので、次のことが重なりうる。

- 試行が増えるほど、評価の穴に合う版が残りやすくなる。
- 方針を変えても採否の物差しは同じなので、前の版で効いた穴への合わせ込みが残ったまま、点数だけが積み上がりうる（推論・実践例なし）。
- 評価そのものに誤りがあれば、ループはその誤りも同じ速さで増やす。詳しくは <!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](../eval/verifier-defines-problem.md#loops-amplify)<!-- link:end --> にある。
- 評価に抜け道があれば、目的でなく採点を満たす方向に解かれる。詳しくは <!-- link:begin reward-hacking -->[採点器を騙す（reward hacking）](../basics/reward-hacking.md)<!-- link:end --> にある。

## 何に効くか {#what-it-affects}

このページが関わる原理は「握る」「確かめる」、防ぐ Claude 側の原因は「確かめていない」、人の側の落とし穴は「やめられない」「体感を信じる」である。

- **握る**：評価の定義・採否・撤退は、反復の外で人が握る。何を人が握り何を任せるかは、<!-- link:begin what-not-to-delegate#verifiable-axis -->[任せないもの（評価・採否・撤退・中核の理解） › 分ける軸：機械的に確かめられるか](what-not-to-delegate.md#verifiable-axis)<!-- link:end --> の軸で分ける。
- **確かめる**：手元の点数の上昇は、本番での改善の証拠にならない。確かめには、AI に中身を見せない検証用のデータが要る。<!-- link:begin lockbox-and-holdout#scores-only -->[ロックボックスと hold-out（人だけが持つ検証用データ） › 点数だけを返す](../eval/lockbox-and-holdout.md#scores-only)<!-- link:end --> のとおり、AI には点数だけを返す。
- **確かめていない（Claude 側の原因）**：開いたループでは、手元の評価の上昇を、本番での改善として確かめる段が抜ける。急な伸びは、先に <!-- link:begin suspect-too-good-results#what-to-suspect -->[良すぎる結果を疑う › まず疑うもの](../verify/suspect-too-good-results.md#what-to-suspect)<!-- link:end --> で疑う。
- **やめられない（人の側の落とし穴）**：点数が少しずつ上がり続けると、回す理由が残り、止めどきを決めにくくなる。止める基準は着手前に書く。書き方は <!-- link:begin decide-when-to-quit#write-criteria-first -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 基準を着手前に書く](../judgment/decide-when-to-quit.md#write-criteria-first)<!-- link:end --> にある。
- **体感を信じる（人の側の落とし穴）**：点数が上がる画面を眺めていると、良くなっている感覚が先に立つ。感覚ではなく、見せていないデータでの結果で判断する。

任せる幅を広げるほど、確かめ方と封じ込めを強める。無人で回す前の問いと、段ごとの守りは <!-- link:begin five-questions-before-delegating#proportional-guards -->[任せ方の段階と、無人で走らせる前の五つの問い › 段ごとに強める確かめ方と封じ込め](five-questions-before-delegating.md#proportional-guards)<!-- link:end --> にある。この守りが整わないうちは、反復の範囲を閉じた反復に狭める。

## よくある誤解 {#misconceptions}

- **「長く回せば良くなる」**：頭打ちになる事例も、延長が効いた事例もあり、時間の長さは成果の根拠にならない。上の <!-- link:begin open-ended-loop-trap#longer-is-not-better -->[AI に改善を回させ続ける罠（開いたループ） › 長く回せば良くなるとは限らない](open-ended-loop-trap.md#longer-is-not-better)<!-- link:end --> のとおり、どちらも単独の報告である。
- **「AI が正直なら過適合は起きない」**：起きる。良かった版を選び続けるだけで、評価の穴への合わせ込みは進む。
- **「頭打ちは回し方が悪いからだ」**：頭打ちは、方針を疑う合図のことが多い。回し方を変える前に、<!-- link:begin decide-when-to-quit#plateau -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 頭打ちは方針を疑う合図](../judgment/decide-when-to-quit.md#plateau)<!-- link:end --> の見方で判断する。
- **「反復はすべて避けるべきだ」**：避けるのは開いたループである。仕様が決まり、停止条件があり、採否を人が握る反復は、任せてよい。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)

**関連**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [/goal（完了するまで続けさせる）](goal-until-done.md)
- [仮説ごとに並べて、同じ物差しで比べる](compare-hypotheses-in-parallel.md)
- [ロックボックスと hold-out（人だけが持つ検証用データ）](../eval/lockbox-and-holdout.md)
- [評価指標そのものを確かめる](../eval/check-the-metric.md)
- [良すぎる結果を疑う](../verify/suspect-too-good-results.md)
- [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)
- [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- [任せないもの（評価・採否・撤退・中核の理解）](what-not-to-delegate.md)
- [任せ方の段階と、無人で走らせる前の五つの問い](five-questions-before-delegating.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
