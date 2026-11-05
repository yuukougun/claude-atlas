---
id: wont-rethink-approach
title: 直し続けて方針を疑わない（またはすぐ撤退を勧める）
nav_title: 方針を疑わない・すぐ撤退を勧める
aliases: [方針を見直さない, すぐ諦めを勧める, 限界ですと言われる]
type: symptom
field: symptoms
chapter: 長い作業と方針
order: 250
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [握る, 確かめる]
prevents: [散らかっている, 確かめていない]
pitfalls: [やめられない, 預けすぎる]
scenes: [開発, コンテスト, データ分析]
summary: エラーを直し続けて方針を疑わない、または早々に撤退を勧めるときに、続けるかやめるかを AI の勧めでなく、先に決めた基準と測った上界で決める。
signs:
  - {type: symptom, text: エラーを直し続けるだけで、やり方そのものを見直さない}
  - {type: symptom, text: 少し試しただけで「これ以上は無理です」と言われる}
  - {type: symptom, text: 会話が長くなると撤退を勧めてくる}
wave: 1
prerequisites: []
related: [experiment-log, compare-hypotheses-in-parallel, ask-for-options, when-to-plan, spec-first, open-ended-loop-trap, goal-until-done, felt-vs-measured, agreement-is-not-evidence, human-pitfalls, going-in-circles, stuck-in-a-check-loop, insists-on-mistakes, six-causes]
routes:
  - {cause: 散らかっている, to: [when-to-start-fresh, handoff-documents]}
  - {cause: 確かめていない, to: [decide-when-to-quit#ai-advice-on-quitting, measure-the-upper-bound, share-targets-and-bounds]}
  - {cause: やめられない, to: [decide-when-to-quit]}
  - {cause: 預けすぎる, to: [what-not-to-delegate, over-reliance]}
tracks: [plan-mode]
outdated_advice: []
sources: [sleesman-2012-escalation-commitment, qiita-ktdatascience-cad6d1, speakerdeck-chihironakayama-agentshi-dai-nokagglede, lukyanenko-rogii-geosteering-kaggle, schulman-opinionated-guide-ml-research, speakerdeck-shun-duan-qi-ahcdesheng, kiri8128-ahc-without-annealing]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: routes}
  - {title: 判断例と予防, anchor: examples}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：エラーを直し続けるときも、すぐ撤退を勧められたときも、続けるかやめるかは先に決めた基準と測った上界で決める。Claude の勧めは根拠にしない。
    - **いつ引くか**：エラーを直し続けるだけでやり方そのものを見直さないとき。少し試しただけで「これ以上は無理です」と言われたとき。会話が長くなると撤退を勧めてくるとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：方針を見直さない・すぐ諦めを勧める・限界ですと言われる
<!-- textlint-enable -->

直し続けて方針を疑わない（またはすぐ撤退を勧める）症状は、方針そのものの妥当性が問われないまま、作業が続くか打ち切られる状態である。逆向きに見えて、どちらも続行か撤退かの判断を Claude の出力に預けている点が同じだ。このページは原因を安く確かめる順に切り分け、対処の本体は各分野のページに振り分ける。

## よくある形 {#forms}

この症状は、次の 3 つの形で現れる。

- **直し続ける**：エラーが出るたびに目の前の修正を重ねるが、そもそもこのやり方で届くのかは問わない。実践者の報告に、Claude がエラーを直し続けても方針の妥当性は疑わなかった、というものがある（根拠：弱。単独の経験談）。
- **早々に撤退を勧める**：安い試行を数回しただけで「限界です」「打ち手がありません」と結論する。本番と似ていない安い試行でアイデアを棄却し、スコアが頭打ちだと早く宣言した、という報告がある（根拠：弱。単独の経験談）。
- **長い会話で撤退を勧める**：会話が長くなるほど、撤退を勧める回答が増える。これも実践者の報告にとどまる（根拠：弱。版にも依存しうる）。

どれも個別の報告は弱いが、扱いは同じにできる。Claude の撤退の勧めにも続行の勧めにも、そのまま従わない。撤退すべきだという判断は、本番の条件で再検証するまで採らない。

## 原因を安く確かめる順 {#diagnosis}

次の 4 つを、手間の小さい順に確かめる。前の 2 つは Claude 側の原因、後の 2 つは人の側の落とし穴である。

1. **散らかっている**（会話の側）
    - 何を見るか：会話が長いか。失敗した試行や直しの跡が大量に残っていないか。撤退の勧めが出たのは、その長い会話の後半ではないか。
    - どう確かめるか：目的と現在の状態だけを書いた新しい会話で、同じ問い（続けるか、別のやり方があるか）を出す。新しい会話で撤退を勧めなくなる、または別のやり方が出るなら、元の会話に溜まった跡が効いている。新しくする判断は<!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end -->、引き継ぎの書き方は<!-- link:begin handoff-documents#four-items -->[handoff 文書と document-and-clear › 書かせる四項目](../context/handoff-documents.md#four-items)<!-- link:end -->を読む。

2. **確かめていない**（結論の根拠の側）
    - 何を見るか：「限界です」「直しました」の根拠が、どの条件の試行か。本番と同じ入力・同じ評価・同じ制約で試した結果か。上界（条件を緩めたときの点数など）を測ったか。
    - どう確かめるか：Claude に、その結論を支える試行の条件と回数を挙げさせ、本番の条件との違いを人が読む。安い試行だけが根拠なら、結論は採らない。直し続ける側では、直した後に何が良くなったかの数値の記録を見る。記録がなければ、その場の修正が進歩なのかが分からない。

3. **やめられない**（人の側の落とし穴）
    - 何を見るか：これまでに費やした時間と回数が、続ける理由になっていないか。「もう少しで直る」という見込みを、数値や期日なしで保っていないか。やめる条件を着手前に書いたか。
    - どう確かめるか：着手前に書いた撤退基準を探す。なければ、今それを書いたとして、費やした分を除いて続けると判断するか、自分に問う。費やした分だけ固執が強まる現象は、組織の意思決定を調べた 2012 年のメタ分析（166 標本）で確かめられている（根拠：強）。AI の速さや同意がこれをさらに強めるという筋は推論で、この点に研究と実践例はない（推論・実践例なし）。

4. **預けすぎる**（人の側の落とし穴）
    - 何を見るか：続行と撤退の決定に、Claude の提案をそのまま採っていないか。評価の定義・採否・撤退は、本来人が握るものである。
    - どう確かめるか：直近の「続ける」「やめる」の決定が、誰のどの根拠によるかを書き出す。根拠が Claude の言い分だけなら、預けている。

疑いすぎにも注意する。方針の変えすぎのほうが、粘りすぎより多い失敗だという実践者の指摘がある（根拠：弱。単独の経験談）。方針を疑うのは、頭打ちや同じ種類の修正の連続といった合図が出たときと、着手前に書いた撤退基準へ達したときにする。頭打ちの見方は<!-- link:begin decide-when-to-quit#plateau -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 頭打ちは方針を疑う合図](../judgment/decide-when-to-quit.md#plateau)<!-- link:end -->、変えすぎの戒めは<!-- link:begin decide-when-to-quit#dont-switch-too-often -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 変えすぎも失敗](../judgment/decide-when-to-quit.md#dont-switch-too-often)<!-- link:end -->を読む。

## 原因ごとの対処 {#routes}

原因が分かったら、次の表から対処のページへ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 散らかっている | [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<br>[handoff 文書と document-and-clear](../context/handoff-documents.md) |
| 確かめていない | [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › AI の「やめよう」「続けよう」を再検証する](../judgment/decide-when-to-quit.md#ai-advice-on-quitting)<br>上界を測って「限界です」を反証する（準備中）<br>[目標値・上界を伝える](../prompting/share-targets-and-bounds.md) |
| 預けすぎる | [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)<br>[判断を預けすぎる（過度依存）](../judgment/over-reliance.md) |
| やめられない | [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例と予防 {#examples}

!!! example "判断例：安い試行の後に「頭打ちです」と言われた"
    - **状況**：スコアを上げる作業で、Claude が小さな入力による数回の試行の後に「この方針は頭打ちで、打ち手がありません」と答えた。期日の判定はまだ先にある。
    - **迷う候補**：Claude の判断を採って撤退する。まだ試していない手があるはずだと、そのまま続ける。
    - **選んだもの**：どちらも採らない。まず試行の条件と本番の条件の違いを確かめ、条件を緩めたときの点数で上界を測ってから、先に書いてあった撤退基準で決める。
    - **理由**：撤退を採ると、本番では届く方針を捨てうる。続けるを採ると、本当に届かない方針に時間を費やしうる。どちらも根拠が Claude の言い分だけである。上界と基準なら、人が判定できる。

!!! example "判断例：同じ種類の修正が続いている"
    - **状況**：テストの失敗を直すたびに別の失敗が出て、修正が数回続いている。Claude は毎回、目の前の失敗の修正を提案する。
    - **迷う候補**：もう一度直させる。やり方そのものを見直させる。
    - **選んだもの**：修正をいったん止め、下の依頼で、試した修正の一覧と別の選択肢を出させる。
    - **理由**：同じ種類の修正の連続は、やり方の側に原因がある合図になりうる。選択肢が出れば、続けるか変えるかを人が決められる。

方針の見直しを頼むときは、次の依頼が使える。コードを直させずに、一覧と選択肢と、やめる条件だけを出させる。

<!-- gen:begin snippet wont-rethink-approach/recheck-approach -->
<!-- textlint-disable -->

??? example "雛形：方針を見直させる依頼"

    ```markdown
    いまのやり方を続ける前に、次に答えてください。コードはまだ直さないでください。

    1. これまでに試した修正を、結果つきで一覧にしてください。
    2. 同じ種類の修正が続いていますか。続いているなら、やり方そのものに別の選択肢はありますか。
    3. 続けるなら、何が起きたらやめると判断しますか。やめるなら、本番と同じ条件で確かめた根拠は何ですか。
    4. 選択肢と推奨案と理由を出してください。続けるかやめるかは私が決めます。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet wont-rethink-approach/recheck-approach -->

予防は、判断を仕組みに移すことである。

- 着手前に撤退基準を書き、判定を作った本人から離す。書き方は<!-- link:begin decide-when-to-quit#write-criteria-first -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 基準を着手前に書く](../judgment/decide-when-to-quit.md#write-criteria-first)<!-- link:end -->を読む。
- 達成できる値や上界が分かるなら、依頼に書く。分からないなら先に測る。<!-- link:begin share-targets-and-bounds#measure -->[目標値・上界を伝える › 上界が分からないときは測る](../prompting/share-targets-and-bounds.md#measure)<!-- link:end -->を読む。
- 実装の前に方針を確かめる。plan mode で編集を止めたまま調べさせ、計画を読んで直してから実装に入る。<!-- link:begin when-to-plan -->[plan mode の使いどころ](../cli/when-to-plan.md)<!-- link:end -->を読む。
- 試した方針と結果は、仮説を先に書く台帳へ残す。<!-- link:begin experiment-log#hypothesis-first -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 仮説を先に書く](../eval/experiment-log.md#hypothesis-first)<!-- link:end -->を読む。
- 方針そのものを長く回し続けて直そうとしない。<!-- link:begin open-ended-loop-trap#longer-is-not-better -->[AI に改善を回させ続ける罠（開いたループ） › 長く回せば良くなるとは限らない](../delegate/open-ended-loop-trap.md#longer-is-not-better)<!-- link:end -->を読む。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Cleaning Up the Big Muddy: A Meta-Analytic Review of the Determinants of Escalation of Commitment](https://gwern.net/doc/psychology/cognitive-bias/sunk-cost/2012-sleesman.pdf)：gwern.net（論文の写し）・英語・確認日 2026-11-04
- [【kaggle】Claude CodeだけでKaggleコンペに挑んで惨敗した話](https://qiita.com/ktdatascience/items/cad6d18c080aa6ca812c)：Qiita（ktdatascience）・確認日 2026-11-04
- [Agent時代のKaggleで、人間は何を見るべきか (関西kaggler会 2026.5.22)](https://speakerdeck.com/chihironakayama/agentshi-dai-nokagglede-ren-jian-hahe-wojian-rubekika-guan-xi-kagglerhui-2026-dot-5-22)：Speaker Deck（chihironakayama）・確認日 2026-11-04
- [How AI agents helped me win a Kaggle silver medal — and how they failed me](https://andlukyane.com/blog/rogii-geosteering-kaggle)：Andrey Lukyanenko・英語・確認日 2026-11-04
- [An Opinionated Guide to ML Research](http://joschu.net/blog/opinionated-guide-ml-research.html)：John Schulman（個人のブログ）・英語・確認日 2026-11-04
- [短期AHCで勝つためのテクニック](https://speakerdeck.com/shun_pi/duan-qi-ahcdesheng-tutamenotekunituku)：Speaker Deck（shun\_pi）・確認日 2026-11-04
- [焼きなまし法が使えなくても AHC 橙になれたよ](https://kiri8128.hatenablog.com/entry/2023/11/29/024335)：Kiri8128・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- 上界を測って「限界です」を反証する（準備中）
- [目標値・上界を伝える](../prompting/share-targets-and-bounds.md)
- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)

**関連**

- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [仮説ごとに並べて、同じ物差しで比べる](../delegate/compare-hypotheses-in-parallel.md)
- [選択肢と推奨案を出させる](../prompting/ask-for-options.md)
- [plan mode の使いどころ](../cli/when-to-plan.md)
- [仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)
- [AI に改善を回させ続ける罠（開いたループ）](../delegate/open-ended-loop-trap.md)
- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)
- [同じ失敗を繰り返す（堂々巡り）](going-in-circles.md)
- [同じ確認のループにはまる](stuck-in-a-check-loop.md)
- [誤りを認めずに言い張る](insists-on-mistakes.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
