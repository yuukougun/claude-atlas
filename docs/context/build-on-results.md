---
id: build-on-results
title: やり直させるより、結果を踏まえて直させる
aliases: [逐次改善, 結果を見せて直させる, 一から作り直させない]
type: concept
field: context
chapter: 新しくする・巻き戻す
order: 40
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [見せる, 確かめる]
prevents: [見えていない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 出力を良くしたいとき、毎回一から作り直させず、前回の結果と測った値を見せて直させる進め方が分かる。会話の失敗は巻き戻し、分かったことはファイルに残して両立させる。
signs:
  - {type: goal, text: 出力を少しずつ良くしていきたい}
  - {type: symptom, text: 何度作り直させても同じくらいの出来にしかならない}
prerequisites: [rewind-dont-correct]
related: [keep-failure-lessons, evidence-not-reports, define-done, measure-changes, handoff-documents, when-to-start-fresh, refine-in-conversation, wont-rethink-approach, performance-tuning]
tracks: []
outdated_advice: []
sources: [arxiv-2506-09050]
volatility: 低
sections:
  - {title: 作り直しと直しの違い, anchor: regenerate-or-refine}
  - {title: 直させるときに見せるもの, anchor: what-to-show}
  - {title: /clear・巻き戻しとの両立, anchor: with-clear}
  - {title: 何に効くか、効かない場面, anchor: effect}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：出力を良くしたいとき、毎回作り直させず、前回の結果と測った値を見せて直させる進め方。
    - **いつ引くか**：出力を少しずつ良くしていきたいとき。何度作り直させても同じくらいの出来にしかならないとき。
    - **前提**：<!-- link:begin rewind-dont-correct -->[違うと返すより、巻き戻す・編集する](rewind-dont-correct.md)<!-- link:end -->

<!-- textlint-disable -->
別名：逐次改善・結果を見せて直させる・一から作り直させない
<!-- textlint-enable -->

「やり直させるより、結果を踏まえて直させる」は、出来の足りない出力に対する進め方である。一から作り直させずに、前回の結果と測った値を Claude に見せて直させる。会話に残った失敗は巻き戻して捨て、分かったことはファイルに残す。この 2 つは両立する。

## 作り直しと直しの違い {#regenerate-or-refine}

作り直しと直しは、前回の結果を入力に使うかどうかで分かれる。作り直しは「最初から書き直して」「もう一度やって」と頼み、前回の出力を使わない。直しは、前回の出力と、それを測った値を見せ、悪かった所だけを変えさせる。

作り直しを繰り返すと、毎回が独立した試行になる。前回に分かったこと（どのケースで落ちたか、どこが遅いか）は次に渡らない。うまくいった部分も、書き直しのたびに失われうる。何度頼んでも同じくらいの出来に落ち着くのは、この形で頼んでいるときに起きやすい。

同じ依頼を 2 通りで並べる。

Before（作り直させる）：

```text
この解法はスコアが低い。最初から書き直して、もっと良くして。
```

After（結果を見せて直させる）：

```text
`best/solution.py` を直してほしい。前回は平均が <前回の平均>、ケース 7 と 12 が時間切れだった。時間切れの 2 ケースを速くする点を 1 つだけ直し、同じ採点を流して前回の値と並べて。
```

After で足したのは 5 つある。直す対象の版、測った値、落ちた場所、直す点の絞り込み、同じ採点で比べる指示である。「もっと良くして」という感想の代わりに、次の判断に使える材料を渡している。

この進め方に近い結果が、ALE-Bench の論文にある。ALE-Bench は、AtCoder Heuristic Contest の過去問 40 問で、AI が長い時間をかけて解を磨く力を測る評価で、2025 年に論文が出た。論文は、採点の結果を見ながら 4 時間ほど直していく逐次の改善を許すと、評価した全モデルが 400 点以上伸びたと報告した。さらに、一部の問題（6 問）では、独立に 150 回生成して選ぶより、結果を見て直すほうが強かった（根拠：中）。

この結果の読み方には 3 つの条件がある。評価されたのは当時の o3 や Gemini 2.5 Pro などで、現行の Claude の傾向を示すものではない。採点が機械で数値として返る課題の結果である。ほかの作業への当てはめは類推にとどまる（類推）。

## 直させるときに見せるもの {#what-to-show}

直させるとき、Claude に見せるものは 3 つある。

- **前回の結果そのもの**：直す対象の版。ファイルで渡すか、出力を貼る。
- **測った値**：同じ採点で出た数値と、落ちたケースの一覧。感想ではなく、実行して出た出力を渡す。
- **変えてよい範囲と、壊してはいけないもの**：直す点は 1 つに絞り、最悪ケースや既存のテストなど、悪くしてはいけない値を言う。1 回で変える点が多いと、値が動いても原因が分からない。

直して測るループを Claude に回させるほど、任せる幅は広がる。先に、終わりの条件と、止まって報告する条件を渡す。渡し方は <!-- link:begin define-done#stop-and-report -->[「完了」を定義して渡す › 止まって報告する条件](../verify/define-done.md#stop-and-report)<!-- link:end --> にある。値は Claude の「良くなった」という報告で受け取らず、実行した出力と、前後で分母のそろった数で受け取る。見方は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](../verify/evidence-not-reports.md#what-counts)<!-- link:end --> にある。

測る手段そのものの作り方と、効いたかの比べ方は、<!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> が扱う。性能改善のように測る対象がはっきりしている例は、<!-- link:begin performance-tuning#same-output-and-timing -->[性能改善を頼む（プロファイルが先・出力の一致と実測） › 出力の一致と実測を証拠にする](../recipes/performance-tuning.md#same-output-and-timing)<!-- link:end --> にある。

面によって、前回の結果と値の渡し方が変わる。

=== "アプリ"

    前回の出力と測った値を、会話に貼るか添付する。同じ会話で続けるなら、前回の出力は文脈に残っているので、値と直す点だけを足す。会話が長くなったら、最良の版と値を貼って新しい会話を始める。

=== "Claude Code"

    前回の版をファイルで持たせ、採点のスクリプトを Claude に実行させて、その出力を読ませる。値は説明ではなく、実行した出力で受け取る。最良の版と試した版を別のファイルに分けておくと、下がったときに戻せる。

=== "API"

    API は会話の状態を持たない。前回の出力と測った値を、次のリクエストの `messages` に自分で入れて送る。入れ忘れると、そのリクエストでは前回の結果が Claude に見えない。

依頼の雛形を置く。前回の値と採点の手順を埋めて使う。

<!-- gen:begin snippet build-on-results/refine-from-result -->
<!-- textlint-disable -->

??? example "雛形：前回の結果を見せて直させる依頼"

    ```markdown
    `best/solution.py` を、作り直さずに直してほしい。前回の結果は次のとおりだ。

    - 採点の入力と手順：`scripts/score.sh`（全ケースの平均と、最悪ケースを出す）
    - 前回の値：平均 <前回の平均>、最悪ケース <前回の最悪値>
    - 前回の出力の様子：<例：ケース 7 と 12 で時間切れ。大きい入力で遅い>

    進め方は次のとおりにする。

    1. 直す点を 1 つに絞り、先にその点と理由を 2 行で書く。
    2. 直したら、同じ `scripts/score.sh` を同じ入力で流し、前回の値と並べた表を出す。
    3. 平均も最悪ケースも前回以上なら、その版を `best/solution.py` に上書きする。どちらかが下がったら上書きせず、直した版は `attempts/` に別名で置く。
    4. 下がったときは、何を試して何が起きたかを `notes/lessons.md` に 1〜2 行で足す。

    手順 2 の値は、実行して出た出力をそのまま貼る。実行していない値は書かない。直す余地が見えなくなったら、続けずに止まって報告する。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet build-on-results/refine-from-result -->

## /clear・巻き戻しとの両立 {#with-clear}

結果を踏まえて直させることと、会話を巻き戻したり `/clear` で新しくしたりすることは、一見ぶつかる。訂正を重ねても直らないときは、新しい会話にするほうがよい。一方で、直すには前回の結果が要る。会話を捨てれば、前回の結果も消える。

両立の鍵は、捨てるものと残すものを分けることである。広い机にたとえると、机の上から片付けるのは、失敗した試みと訂正のやりとりだ。残すのは最良の版、その値、分かったことである。これらは机の外のファイルに置き、新しい机の最初に広げる。

- **会話から捨てる**：失敗した試み、訂正の往復、悪化した版の長い出力。巻き戻しの理由は <!-- link:begin rewind-dont-correct#why -->[違うと返すより、巻き戻す・編集する › なぜ訂正より巻き戻しか](rewind-dont-correct.md#why)<!-- link:end --> にある。
- **ファイルに残す**：最良の版と測った値、試して駄目だったことの短い記録。何を残し何を捨てるかは <!-- link:begin keep-failure-lessons#what-to-keep -->[失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか](keep-failure-lessons.md#what-to-keep)<!-- link:end -->、巻き戻しと記録の両立は <!-- link:begin keep-failure-lessons#both -->[失敗の教訓は捨てずに書き残す › 巻き戻しと記録の両立](keep-failure-lessons.md#both)<!-- link:end --> にある。
- **新しい会話の最初に見せる**：残したファイルを読ませ、そこから直させる。置き場所と再開の仕方は <!-- link:begin handoff-documents#where -->[handoff 文書と document-and-clear › 置き場所（圧縮で消えない所）](handoff-documents.md#where)<!-- link:end --> と <!-- link:begin handoff-documents#resume -->[handoff 文書と document-and-clear › 新しい会話での再開の仕方](handoff-documents.md#resume)<!-- link:end --> にある。

新しくする前に残すものの一覧は <!-- link:begin when-to-start-fresh#before-clearing -->[新しい会話を始めるタイミング › 新しくする前に残すもの](when-to-start-fresh.md#before-clearing)<!-- link:end --> にもある。

!!! example "判断例：悪化が続いた長い作業の再開"
    - **状況**：スコアを競う最適化の解を、Claude Code で 1 時間ほど直してきた。最良の版は `best/solution.py`、採点の結果は `scores.csv` にある。直近の数回は悪化が続き、会話には失敗した試みと訂正が並んでいる。
    - **迷う候補**：最良の版まで巻き戻し、同じ会話で別の直しを頼む。新しい会話を始め、最良の版と値を見せて直させる。
    - **選んだもの**：新しい会話を始め、次の 3 つを読ませてから（`best/solution.py`・`scores.csv`・`notes/lessons.md`）、直す点を 1 つ決めて頼む。
    - **理由**：失敗が直近の 1〜2 回に収まるなら、巻き戻しで足りる。ここでは悪化が数回続き、会話全体も長く、失敗した試みと訂正が広く残っている。最良の版と値が手元のファイルにあるので、新しい会話に移しても前回の結果は失われない。一から作り直させる案は、最良の版と値を捨てるので選ばない。

## 何に効くか、効かない場面 {#effect}

この進め方は、原理の「見せる」と「確かめる」に関わる。前回の結果と測った値を見せ、直した後に同じ採点で前後を比べて確かめる。防ぐ Claude 側の原因は「見えていない」である。作り直しでは、前回の結果が Claude に見えていないので、毎回が手探りになる。

効かない場面と、やりすぎの形は次のとおりである。

- **測る手段がない**：良くなったかを判断できず、直しが好みの往復になる。先に測る手段と終わりの条件を決める。
- **値が伸びなくなった**：直しは、いまの方針の中の改善である。同じ所を直し続けて伸びないなら、方針を疑う。判断の順は <!-- link:begin wont-rethink-approach#diagnosis -->[直し続けて方針を疑わない（またはすぐ撤退を勧める） › 原因を安く確かめる順](../symptoms/wont-rethink-approach.md#diagnosis)<!-- link:end --> にある。
- **依頼の言い方がずれている**：出力を直すより、依頼を直したほうが速いことがある。<!-- link:begin refine-in-conversation#edit-the-request -->[頼み方は一回で決めない（会話で詰める） › 訂正を重ねるより依頼を直す](../prompting/refine-in-conversation.md#edit-the-request)<!-- link:end --> を見る。
- **1 回で済む小さな頼み**：結果と値を整える手間のほうが大きい。普通に頼み直せばよい。

## よくある誤解 {#misconceptions}

- **作り直しは悪く、直しは善いという誤解**：方針そのものが合っていないときは、作り直しのほうが正しい。直しを重ねて値が良くなる方向に動くかで決める。動かないなら、方針を見直す。
- **直させるとは、訂正を重ねることだという誤解**：訂正は「違う」「もっと良く」と言い返すことで、結果の値を渡さない。直しは、前回の版と測った値を渡す。会話に誤りが残る形で訂正を重ねるなら、巻き戻す。
- **結果を見せれば、Claude が自分で正しく評価するという誤解**：値は、自分で測った出力か、実行した記録で渡す。Claude の評価だけを根拠にして次の直しへ進めない。

この辞典の推奨は、測れる課題では前回の結果と値を見せて直させ、会話は巻き戻しや `/clear` で軽く保ち、残すものはファイルに置くことである。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [ALE-Bench: A Benchmark for Long-Horizon Objective-Driven Algorithm Engineering](https://arxiv.org/abs/2506.09050)：arXiv（Imajuku, Yuki ほか）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [違うと返すより、巻き戻す・編集する](rewind-dont-correct.md)

**関連**

- [失敗の教訓は捨てずに書き残す](keep-failure-lessons.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [「完了」を定義して渡す](../verify/define-done.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [handoff 文書と document-and-clear](handoff-documents.md)
- [新しい会話を始めるタイミング](when-to-start-fresh.md)
- [頼み方は一回で決めない（会話で詰める）](../prompting/refine-in-conversation.md)
- [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- [性能改善を頼む（プロファイルが先・出力の一致と実測）](../recipes/performance-tuning.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
