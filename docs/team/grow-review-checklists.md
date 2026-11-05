---
id: grow-review-checklists
title: レビューの観点を育てる
aliases: [レビューの観点, レビューチェックリスト]
type: recipe
field: team
chapter: レビューと判断
order: 80
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [チーム, 開発]
summary: 見落としを直した PR から見落とした理由を抜き出し、人の承認を経てレビューの観点に足していける。AI のレビュアーへの指示も同じ観点で育てる。
signs:
  - {type: symptom, text: 同じ種類の見落としが、レビューをすり抜ける}
  - {type: goal, text: 見落としから、レビューの観点を増やしていきたい}
prerequisites: [instructing-reviewers]
related: [independent-review, automated-pr-review, create-and-review-prs#pr-description, risk-tiered-approval, review-bottlenecks, postmortems, keep-failure-lessons, writing-skills]
sections:
  - {anchor: guards, title: 先に整える守り}
  - {anchor: steps, title: 手順}
  - {anchor: template, title: 雛形：見落とした理由を抜き出す依頼文}
  - {anchor: check, title: 確かめ方}
  - {anchor: when-failing, title: 失敗したとき}
sources: []
volatility: 低
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：見落としを直した PR から理由を抜き出し、人が承認した分だけレビューの観点に足して、AI への指示にも反映できる。
    - **いつ引くか**：同じ種類の見落としがレビューをすり抜けるとき。見落としから、レビューの観点を増やしていきたいとき。
    - **前提**：<!-- link:begin instructing-reviewers -->[レビュアーへの指示の書き方](../verify/instructing-reviewers.md)<!-- link:end -->

<!-- textlint-disable -->
別名：レビューの観点・レビューチェックリスト
<!-- textlint-enable -->

レビューの観点を育てるとは、見落としが見つかるたびに、その理由を観点として書き戻していくことである。やることは次の循環である。見落としを直した PR から理由を抜き出す。人が採否を決める。採ったものを、レビューの観点と AI のレビュアーへの指示の両方へ足す。ミスのたびに指示へ書き戻す考え方のレビュー版にあたる。この進め方は企業ブログで紹介された考え方に基づく（根拠：中）。効果を数で示した研究はないので、効いたかどうかは自分たちのレビューで確かめる。

## 先に整える守り {#guards}

観点を増やす前に、次の 3 つを決めておく。増やした観点が誤っていても、レビューの質を下げないための守りである。

- **観点を足す権限は人に置く**：Claude が出すのは観点の「案」までにする。AI の承認は人の承認に数えない。理由は <!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](../verify/independent-review.md#ai-approval)<!-- link:end --> と <!-- link:begin risk-tiered-approval#ai-approval-doesnt-count -->[リスク段階別の承認（AI の承認を人の承認に数えない） › AI の承認を数えない](risk-tiered-approval.md#ai-approval-doesnt-count)<!-- link:end --> にある。観点は以後すべての PR のレビューに効くので、足す判断は人が持つ。
- **理由を抜き出す役は、見落とした変更を書いたセッションとは別にする**：変更を生んだ推論を見た者は、同じ見落としを繰り返しやすい。分け方は <!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end --> を使う。
- **観点の数に上限を持つ**：観点が増えるほど、レビューする側の負担も増える。上限は、レビューで一度に読める量を目安に、チームで決める。流す量をレビューの容量へ合わせる考え方は <!-- link:begin review-bottlenecks#match-review-capacity -->[レビューのボトルネックと疲労 › 流す量をレビューに合わせる](review-bottlenecks.md#match-review-capacity)<!-- link:end --> にある。

もう 1 つの前提は、レビュアーへの指示がすでに常設になっていることである。観点を足す先がなければ、抜き出した理由は読まれないまま残る。指示の書き方は <!-- link:begin instructing-reviewers -->[レビュアーへの指示の書き方](../verify/instructing-reviewers.md)<!-- link:end --> に任せる。

## 手順 {#steps}

各段の終わりに、何で終わったと言えるかを置く。

1. **材料を選ぶ**：レビューをすり抜けて後から直した PR を、元の PR とセットで集める。誰のミスかを探すためではなく、レビューの仕組みの隙間を探すために使う（考え方は <!-- link:begin postmortems#which-gap -->[失敗を仕組みに戻す（ポストモーテム） › 誰がではなく、どの隙間が](../judgment/postmortems.md#which-gap)<!-- link:end -->）。
    - 終わりの確かめ：見落とされた内容を 1 文で言える。言えないものは材料にしない。
2. **理由を抜き出させる**：新しいセッションに、元の PR と修正の PR を渡す。依頼文は次の節の雛形を使う。出させるのは、見落とした変更の型・見落とした理由・次に確かめる観点の案の 3 つである。
    - 終わりの確かめ：各件が、元の PR を見なくても読める。この PR だけの名前に依存していない。
3. **人が採否を決める**：案ごとに、採る・直して採る・採らないを決める。採らない案も理由を 1 行残すと、同じ案が何度も出てきても判断し直さずに済む（残し方は <!-- link:begin keep-failure-lessons#what-to-keep -->[失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか](../context/keep-failure-lessons.md#what-to-keep)<!-- link:end -->）。
    - 終わりの確かめ：すべての案に、人の決定が付いている。
4. **観点に足す**：採った案を、観点の置き場に足す。置き場は AI のレビュアーへの指示・CLAUDE.md・スキルなどから、読まれる場面で選ぶ（選び方は <!-- link:begin postmortems#where-to-put-fixes -->[失敗を仕組みに戻す（ポストモーテム） › 再発防止をどこに入れるか](../judgment/postmortems.md#where-to-put-fixes)<!-- link:end -->、スキルにするなら <!-- link:begin writing-skills#when-to-use -->[スキルの作り方 › どんなときにスキルにするか](../extend/writing-skills.md#when-to-use)<!-- link:end -->）。観点には、確かめ方を 1 つ付ける。指摘ごとに確かめ方を付けさせる頼み方は <!-- link:begin instructing-reviewers#per-finding -->[レビュアーへの指示の書き方 › 指摘ごとに確かめ方を付けさせる](../verify/instructing-reviewers.md#per-finding)<!-- link:end --> にある。
    - 終わりの確かめ：観点が「どの変更で・何を・どう確かめるか」の形で読める。
5. **次のレビューで効いたかを見る**：足した観点が、実際のレビューの指摘に出てきたかを見る。
    - 終わりの確かめ：足した観点ごとに、使われた・使われなかったの記録が残っている。見方は次の「確かめ方」の節にある。

観点の形の例を示す。型を限り、確かめ方を付けた書き方にする。

```text
設定値を足す変更では、その値を読む側の既定値の扱いも変わっているか。
確かめ方：値の名前を grep し、読む箇所すべてに既定値の分岐があるかを見る。
```

!!! example "判断例：この見落としを観点に足すか"
    - **状況**：ある PR で、特定のライブラリの癖が原因の不具合が、レビューをすり抜けて後から直された。
    - **迷う候補**：その癖を全 PR 共通の観点に足す。足さずに、回帰テストを足すだけにする。
    - **選んだもの**：観点には足さず、回帰テストを足す。
    - **理由**：観点はすべての PR のレビューで読まれ、読む量が増える。そのライブラリを使う変更が少ないなら、観点より回帰テストのほうが、見落としを確実に止められる。使う変更が増えてきたら、観点へ足す判断に変えてよい。

## 雛形：見落とした理由を抜き出す依頼文 {#template}

修正の PR から、見落とした理由を抜き出させる依頼文である。観点は書き足させず、案を出させるだけにしてある。採否を人に残すためである。

<!-- gen:begin snippet grow-review-checklists/extract-miss-reasons -->
<!-- textlint-disable -->

??? example "雛形：修正の PR から見落とした理由を抜き出す依頼文"

    ```markdown
    次の 2 つを読み、レビューが見落とした理由を抜き出してください。

    - 元の PR：<PR の番号か差分>
    - 見落としを直した PR：<PR の番号か差分>

    出す形（1 件につき次の 3 行）：

    - 見落とした変更の型：どんな種類の変更だったか。この PR だけの名前（関数名・チケット番号）を使わずに書く
    - 見落とした理由：レビューで何を見ていなかったか。誰の誤りかではなく、観点の何が足りなかったかで書く
    - 観点の案：次のレビューで確かめる 1 文と、その確かめ方（コマンド・見るファイル・テスト）

    守ること：

    - 観点は書き足さない。案として出すだけにする。採るかどうかは人が決める
    - 理由を推測で補わない。差分と PR の議論から読み取れないときは「不明」と書く
    - 案は 3 件までにする。同じ型の案は 1 件にまとめる
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet grow-review-checklists/extract-miss-reasons -->

## 確かめ方 {#check}

観点が育っているかは、次の 2 つで確かめる。

- **過去の見落としで試す**：観点を足した後、その観点のきっかけになった見落としを含む元の PR を、新しいセッションにレビューさせる。その見落としが指摘に出れば、観点が働いている。出ないときは、観点の書き方が曖昧だと見る。
- **観点ごとの使われ方を見る**：一定の期間のレビューで、一度も指摘を出さなかった観点と、毎回のように指摘を出す観点を分けて見る。指摘が出ない観点は、狭めるか外す候補になる。毎回出る観点は、変更の側で防げないかを考える（防げるなら <!-- link:begin risk-tiered-approval#principles-and-causes -->[リスク段階別の承認（AI の承認を人の承認に数えない） › どの原理・どの原因に関わるか](risk-tiered-approval.md#principles-and-causes)<!-- link:end --> の原理で守りに移す）。

数を増やすこと自体を成果にしない。同種の見落としがレビューを抜けなくなったかで測る。

## 失敗したとき {#when-failing}

- **観点が増えすぎて、レビューが重くなった**：観点を型ごとにまとめ直し、指摘が出ないものを外す。詰まりの見方は <!-- link:begin review-bottlenecks#where-it-clogs -->[レビューのボトルネックと疲労 › 詰まる場所はレビューと動作確認](review-bottlenecks.md#where-it-clogs)<!-- link:end --> にある。
- **足した観点が広すぎて、的外れな指摘が増えた**：観点を「どの変更で」の条件で絞る。指摘の網羅と選別を分ける頼み方は <!-- link:begin instructing-reviewers#exhaustive-then-filter -->[レビュアーへの指示の書き方 › 網羅と選別を分ける](../verify/instructing-reviewers.md#exhaustive-then-filter)<!-- link:end --> にある。
- **同じ見落としが、観点を足した後も再発する**：観点が読まれていないか、確かめ方が曖昧である。足した先が読み込まれる場面かを見直す。レビューを AI に任せているなら、AI のレビューで通ったことを理由に人の確認を省いていないかも見る（<!-- link:begin automated-pr-review -->自動 PR レビュー（Code Review・/ultrareview）<!-- link:end -->）。
- **失敗の記録そのものが残っていない**：<!-- link:begin keep-failure-lessons -->[失敗の教訓は捨てずに書き残す](../context/keep-failure-lessons.md)<!-- link:end --> の書き残し方から始める。

PR の説明で、リスクと確かめた証拠を先に書かせる方法は <!-- link:begin create-and-review-prs#pr-description -->[PR を作り、レビューを受ける › PR の説明に書くこと](../recipes/create-and-review-prs.md#pr-description)<!-- link:end --> にある。観点を増やす前に、説明の側で見落としを減らせることもある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [レビュアーへの指示の書き方](../verify/instructing-reviewers.md)

**関連**

- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [PR を作り、レビューを受ける › PR の説明に書くこと](../recipes/create-and-review-prs.md#pr-description)
- [リスク段階別の承認（AI の承認を人の承認に数えない）](risk-tiered-approval.md)
- [レビューのボトルネックと疲労](review-bottlenecks.md)
- [失敗を仕組みに戻す（ポストモーテム）](../judgment/postmortems.md)
- [失敗の教訓は捨てずに書き残す](../context/keep-failure-lessons.md)
- [スキルの作り方](../extend/writing-skills.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
