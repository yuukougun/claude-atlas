---
id: going-in-circles
title: 同じ失敗を繰り返す（堂々巡り）
nav_title: 同じ失敗を繰り返す
aliases: [堂々巡り, 同じ修正の失敗, going in circles, 直してもまた壊れる]
type: symptom
field: symptoms
chapter: 会話と文脈
order: 140
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 散らかっている, 確かめていない]
pitfalls: [やめられない]
scenes: [開発]
summary: 同じ失敗を何度も繰り返す原因を、会話に残った失敗の跡から切り分け、訂正を重ねるか、巻き戻すか、学んだことを書いて新しく始めるかを決める。
signs:
  - {type: symptom, text: 同じバグの修正を何度も失敗する}
  - {type: symptom, text: 直してと言うたびに同じ間違いが戻ってくる}
  - {type: symptom, text: 訂正しても別の形で同じ誤りが出る}
wave: 1
prerequisites: [context-rot]
related: [checkpoints-and-rewind, tidy-the-desk, build-on-results, let-claude-ask, stuck-in-a-check-loop, wont-rethink-approach, insists-on-mistakes, forgets-in-long-chats, six-causes]
routes:
  - {cause: 見えていない, to: [keep-failure-lessons, handoff-documents]}
  - {cause: 散らかっている, to: [rewind-dont-correct, when-to-start-fresh, fix-a-bug#when-stuck]}
  - {cause: 確かめていない, to: [fix-a-bug#reproduce-and-define-done, define-done]}
  - {cause: やめられない, to: [decide-when-to-quit]}
tracks: [checkpoints, clear]
outdated_advice: []
sources: [cc-docs-best-practices]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 訂正・巻き戻し・新しく始めるの選び方, anchor: choose}
  - {title: 原因ごとの振り分け先, anchor: routes}
  - {title: 判断例, anchor: examples}
  - {title: 予防, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：同じ失敗の原因を、会話に残った失敗の跡などから切り分け、訂正・巻き戻し・新しく始めるのどれにするかを決められる。
    - **いつ引くか**：同じバグの修正を何度も失敗する、直してと言うたびに同じ間違いが戻る、訂正しても別の形で同じ誤りが出るとき。
    - **前提**：<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end -->

<!-- textlint-disable -->
別名：堂々巡り・同じ修正の失敗・going in circles・直してもまた壊れる
<!-- textlint-enable -->

同じ失敗を繰り返す（堂々巡り）は、同じ点を何度頼み直しても直らず、会話だけが伸びていく症状である。多くの場合、原因は Claude の能力だけでなく、会話に残った失敗の跡と、足りない情報と、確かめの欠落にある。

## よくある形 {#forms}

同じ失敗の繰り返しは、次の 3 つの形で現れる。

- 同じバグの修正を何度も頼むが、そのたびに直らない。
- 直してと言うたびに、前に捨てたはずの間違った案が戻ってくる。
- 訂正すると、その箇所は直るが、別の形で同じ誤りが出る。

似ているが、別のページが扱う症状もある。実行と確認を繰り返すだけで進まないときは <!-- link:begin stuck-in-a-check-loop#diagnosis -->[同じ確認のループにはまる › 原因を安く確かめる順](stuck-in-a-check-loop.md#diagnosis)<!-- link:end --> を引く。方針そのものが誤りなのに直し続けているときは <!-- link:begin wont-rethink-approach#diagnosis -->[直し続けて方針を疑わない（またはすぐ撤退を勧める） › 原因を安く確かめる順](wont-rethink-approach.md#diagnosis)<!-- link:end --> を引く。誤りを指摘しても言い張るときは <!-- link:begin insists-on-mistakes#diagnosis -->[誤りを認めずに言い張る › 原因を安く確かめる順](insists-on-mistakes.md#diagnosis)<!-- link:end --> を引く。会話が長くなって前提を忘れるときは <!-- link:begin forgets-in-long-chats#diagnosis -->[長い会話で前提を忘れる・雑になる › 原因を安く確かめる順](forgets-in-long-chats.md#diagnosis)<!-- link:end --> を引く。

## 原因を安く確かめる順 {#diagnosis}

同じ失敗が続くときは、次の順に確かめる。上ほど安く確かめられる。1 つ当たったら、その項目の振り分け先へ進む。

1. **見えていない（情報不足）**
    - **見るもの**：同じ前提が毎回抜けていないか。ファイル名、症状、再現の手順、期待する挙動を、Claude に渡したか。
    - **確かめ方**：Claude に、いま分かっていることと分かっていないこと、試した修正とそれが駄目だった理由を、一覧で書かせる。一覧に事実の取り違えや抜けがあれば、見えていない。
    - **当たったとき**：足りない情報を渡す。会話を新しくしても同じ抜けが出るなら、書き残して引き継ぐ。振り分け先は後の表にある。
    - **参考**：「直して」を繰り返して長く失ったが、処理の流れを説明させたら短い時間で原因に着いた、という日本語の経験談がある（根拠：弱。単独の経験談）。
2. **散らかっている（失敗の残骸）**
    - **見るもの**：会話に、失敗した修正の試みが何度も残っていないか。同じ点への訂正が重なっていないか。直したはずの案が戻ってくるのは、この形の典型である。
    - **確かめ方**：会話を見返し、失敗した試みの数を数える。タイトルだけでなく、Claude が直前の誤った案を踏まえて答えているかを見る。
    - **当たったとき**：失敗した試みが入った会話を読み続けるだけになるので、訂正を重ねない。前のメッセージを直して送り直すか、巻き戻すか、新しく始める。選び方は次の節にある。
3. **確かめていない（完了と原因の検証がない）**
    - **見るもの**：「直った」の定義と再現の手順を渡したか。Claude が、実行せずに直ったと言っていないか。原因の仮説を確かめる前に、コードを変えていないか。
    - **確かめ方**：再現のコマンドかテストを、自分で 1 回実行する。失敗が再現しないまま直しているなら、確かめていない。
    - **当たったとき**：失敗するテストで再現させてから直させる。症状を隠すだけの修正は認めない。
4. **やめられない（人の側の落とし穴）**
    - **見るもの**：同じ方針に費やした時間が増え、やめる基準を決めないまま続けていないか。
    - **確かめ方**：同じ方針で何度目かを数え、やめる基準が着手前に書いてあるかを見る。
    - **当たったとき**：続けるかやめるかを、先に決めた基準で判断する。

1 から 3 は、どれも会話のなかの記録で確かめられる。4 は自分の状態の確認であり、1 から 3 のどれかに当たっても同時に疑う。

## 訂正・巻き戻し・新しく始めるの選び方 {#choose}

同じ失敗が続くとき、取れる手は 3 つある。公式の Best practices（2026-11-05 に確認）は、同じ点の訂正が重なっても直らないときは、さらに訂正を足さないよう勧める（切り替えの目安は <!-- fact:begin clear-after-failed-corrections -->2 回（2026-11-03 時点）<!-- fact:end -->）。代わりに、会話を新しくして、学んだことを織り込んだ依頼を 1 つ書き直す。訂正を足すほど、失敗した試みが入った会話を Claude が読み直すだけになるからである。この目安は版で変わりうるので、公式の最新も見る。

- **訂正する**：直前の 1 回だけが外れていて、会話のほかの部分は健全なとき。まだ失敗の跡が少ないので、足りない情報を 1 つ足して頼み直す。
- **巻き戻す**：失敗した試みが複数残り、その前の時点には戻れるとき。コード、会話、その両方のどれを戻すかを選ぶ。戻せないものがあるので、先に <!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](../cli/checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> を見る。面ごとの戻し方は <!-- link:begin rewind-dont-correct#how -->[違うと返すより、巻き戻す・編集する › 面ごとの戻し方](../context/rewind-dont-correct.md#how)<!-- link:end --> にある。
- **学んだことを書いて新しく始める**：会話がすでに汚れ、分かったこともある（駄目だった方法、確かめた事実）とき。駄目だったことと分かったことだけを短く書き出し、会話を新しくして、その文書から再開する。何を残すかは <!-- link:begin keep-failure-lessons#what-to-keep -->失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか（準備中）<!-- link:end --> を見る。新しくする前に残すものは <!-- link:begin when-to-start-fresh#before-clearing -->[新しい会話を始めるタイミング › 新しくする前に残すもの](../context/when-to-start-fresh.md#before-clearing)<!-- link:end --> を見る。

巻き戻しと書き出しは両立する。巻き戻して会話を軽くし、分かったことだけをファイルに残せば、同じ失敗の再提案を防げる。詳しくは <!-- link:begin keep-failure-lessons#both -->失敗の教訓は捨てずに書き残す › 巻き戻しと記録の両立（準備中）<!-- link:end --> を見る。

学んだことを織り込んだ頼み直しの雛形を次に示す。新しい会話で出す。

<!-- gen:begin snippet going-in-circles/restart-prompt -->
<!-- textlint-disable -->

??? example "雛形：学んだことを織り込んだ頼み直し"

    ```markdown
    前の会話で、次の修正を試したが直らなかった。その結果を踏まえて、新しく取り組み直したい。

    - 症状：<何が起きるか。再現のコマンドか手順>
    - 試して駄目だったこと：<試した修正と、そのあとに起きたこと>
    - 分かったこと：<原因について確かめられたこと。推測は推測と分けて書く>
    - 直ったと言える条件：<実行するコマンドと、期待する結果>

    試した修正をそのまま繰り返さないでほしい。まず原因の仮説を複数挙げ、それぞれの確かめ方を示すこと。確かめが終わるまでは、コードを変えないこと。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.0。

<!-- textlint-enable -->
<!-- gen:end snippet going-in-circles/restart-prompt -->

## 原因ごとの振り分け先 {#routes}

原因ごとの対処の本体は、各分野のページに任せる。次の表から、当たった原因の行き先へ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | 失敗の教訓は捨てずに書き残す（準備中）<br>[handoff 文書と document-and-clear](../context/handoff-documents.md) |
| 散らかっている | [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)<br>[新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<br>[バグを直す › 直らないときは巻き戻して頼み直す](../recipes/fix-a-bug.md#when-stuck) |
| 確かめていない | [バグを直す › 再現と「直った」の定義を渡す](../recipes/fix-a-bug.md#reproduce-and-define-done)<br>[「完了」を定義して渡す](../verify/define-done.md) |
| やめられない | [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：直らないテストの修正を、どう続けるか"
    - **状況**：失敗するテストの修正を何度か頼んだが、そのたびに別の箇所を直され、同じテストが落ち続ける。会話には、失敗した修正が複数残っている。
    - **迷う候補**：同じ会話で、さらに具体的に訂正する。または、失敗した修正の前まで巻き戻して頼み直す。
    - **選んだもの**：巻き戻して頼み直す。頼み直しには、再現のコマンドと「直った」の定義、これまでに分かった原因の手がかりを足す。
    - **理由**：失敗した試みが残ると、次の答えはそれに引きずられやすい。同じ会話で訂正を足すより、期待と違う返答の前に戻るほうが筋が通る。ただし Bash で変えたファイルは戻らないので、戻す前に変更の範囲を確かめる。

!!! example "判断例：新しい会話でも同じ詰まりに戻るとき"
    - **状況**：会話を新しくして頼み直したが、同じ設計の修正でまた詰まる。同じ方針に、すでに長く時間を使っている。
    - **迷う候補**：もう一度新しい会話で、別の言い方で頼む。または、続けるかやめるかを、先に決めた基準で判断する。
    - **選んだもの**：やめる基準に照らして判断する。基準がなければ、いまから書く。判定は Claude の勧めに任せない。
    - **理由**：会話を新しくしても直らないなら、原因は文脈の汚れではなく、方針か、費やした分だけ続けてしまう人の側にある。詳しくは <!-- link:begin decide-when-to-quit#plateau -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 頭打ちは方針を疑う合図](../judgment/decide-when-to-quit.md#plateau)<!-- link:end --> を見る。

## 予防 {#prevention}

同じ失敗の繰り返しは、起きてから直すより、起きにくい進め方に移すほうが安い。

- 最初の依頼で、ファイル名、症状、「直った」の定義を渡す。バグの修正では、再現と完了の定義を先に渡す。渡し方は <!-- link:begin fix-a-bug#reproduce-and-define-done -->[バグを直す › 再現と「直った」の定義を渡す](../recipes/fix-a-bug.md#reproduce-and-define-done)<!-- link:end --> と <!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end --> を見る。
- 最初の 1 分を見て、ずれたらすぐ止める。ずれた答えの上に訂正を重ねない。
- 巻き戻しや `/clear` で捨てる試みから、分かったことだけを残す習慣をつける。書き残しすぎると別の問題が出るので、残す量は <!-- link:begin keep-failure-lessons#too-much -->失敗の教訓は捨てずに書き残す › 書き残しすぎの副作用（準備中）<!-- link:end --> を見て決める。
- 出力を良くしたいときは、毎回作り直させず、前回の結果と測った値を見せて直させる。進め方は <!-- link:begin build-on-results#regenerate-or-refine -->やり直させるより、結果を踏まえて直させる › 作り直しと直しの違い（準備中）<!-- link:end --> にある。
- 自分でも要件が固まっていないときは、先に Claude に質問させる。質問の頼み方は <!-- link:begin let-claude-ask#how -->質問させる・インタビューさせる › 質問させる頼み方（準備中）<!-- link:end --> を見る。
- 続けるかやめるかを、着手前に書いた基準で判断する。基準の書き方は <!-- link:begin decide-when-to-quit#write-criteria-first -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する） › 基準を着手前に書く](../judgment/decide-when-to-quit.md#write-criteria-first)<!-- link:end --> を見る。

会話を整える動作の全体は <!-- link:begin tidy-the-desk#four-actions -->机を整える：新鮮さ・巻き戻し・書き出し・委任 › 四つの動作（準備中）<!-- link:end --> にまとめてある。診断の入口は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [context rot と紛らわしい情報](../basics/context-rot.md)

**次に読む**

- 失敗の教訓は捨てずに書き残す（準備中）
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [バグを直す](../recipes/fix-a-bug.md)
- [「完了」を定義して渡す](../verify/define-done.md)
- [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)

**関連**

- [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- 机を整える：新鮮さ・巻き戻し・書き出し・委任（準備中）
- やり直させるより、結果を踏まえて直させる（準備中）
- 質問させる・インタビューさせる（準備中）
- [同じ確認のループにはまる](stuck-in-a-check-loop.md)
- [直し続けて方針を疑わない（またはすぐ撤退を勧める）](wont-rethink-approach.md)
- [誤りを認めずに言い張る](insists-on-mistakes.md)
- [長い会話で前提を忘れる・雑になる](forgets-in-long-chats.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
