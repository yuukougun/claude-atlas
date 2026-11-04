---
id: summary-overstates-source
title: 要約が原文より断定的になる
aliases: [要約の言い過ぎ, 条件が落ちる要約]
type: symptom
field: symptoms
chapter: 事実と出典
order: 120
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [見えていない, 確かめていない]
pitfalls: []
scenes: [調べもの, 学習, 文章]
summary: 要約が原文より断定的になったときに、落ちた条件や但し書きを原文と照らして見つけ、要約を信じてよい範囲を決める。
signs:
  - {type: symptom, text: 要約すると「場合がある」が「必ず」になる}
  - {type: symptom, text: 論文の要約が原文の結論より強い}
  - {type: symptom, text: 条件や但し書きが要約から落ちる}
wave: 1
prerequisites: [summary-overgeneralization]
related: [research-and-reports, using-research, learning-with-ai, handing-long-documents, plausible-falsehoods, skipped-later-pages, six-causes]
routes:
  - {cause: 見えていない, to: [long-context-first#quote-first]}
  - {cause: 確かめていない, to: [fact-checking#summaries, checking-citations, read-specs-yourself]}
tracks: [research]
outdated_advice: []
sources: []
volatility: 低
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: example}
  - {title: 予防：要約の形で縛る, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：要約から落ちた条件や但し書きを原文と照らして見つけ、要約を信じてよい範囲を決められる。
    - **いつ引くか**：要約すると「場合がある」が「必ず」になる、論文の要約が原文の結論より強い、条件や但し書きが要約から落ちる、と感じたとき。
    - **前提**：<!-- link:begin summary-overgeneralization -->[要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)<!-- link:end -->

<!-- textlint-disable -->
別名：要約の言い過ぎ・条件が落ちる要約
<!-- textlint-enable -->

Claude に資料を要約させたところ、原文が慎重に書いていたことを、要約が言い切っていることがある。このページは、その症状を原文との照合で見つけ、原因を安く確かめる順に切り分けて、対処のページへ振り分ける。要約が強くなりやすい理由は前提のページに任せ、ここでは見つけ方と確かめ方だけを扱う。

## よくある形 {#forms}

要約が原文より断定的になるときは、次のような形で現れる。どれも、原文は実在し、中身の大半は合っている。そこが存在しない出典を作る嘘とは違う（そちらは <!-- link:begin plausible-falsehoods -->[もっともらしい嘘・出典の誤り](plausible-falsehoods.md)<!-- link:end --> を見る）。

- 「場合がある」「傾向がある」が、「必ず」「常に」「すべて」になる。
- 対象・期間・環境・規模の限られた結果が、条件のない一般論になる。
- 「相関がある」「示唆される」が、「原因である」「示された」になる。
- 論文の要約が、本文の結論や著者が書いた限界より強い。
- 著者が書いた「この結果は限られた場合のものである」という但し書きが、丸ごと落ちる。
- 競技の学習で、上位解法の要約から、その手法が効いた問題の性質（前提）が落ちる。詳しい例は <!-- link:begin summary-overgeneralization#contest -->[要約は原文より強く言いがち（過度な一般化） › 競技の例：上位解法の前提が落ちる](../basics/summary-overgeneralization.md#contest)<!-- link:end --> を見る。

読み落としやすいのは、要約が自然な文で書かれていて、落ちた条件の跡が見えないことだ。要約だけを読んでいても、断定になったことには気づけない。気づくには、原文の側から要約の強い言葉を照らすしかない。

## 原因を安く確かめる順 {#diagnosis}

症状が出たら、次の順に確かめる。上ほど安く、1 回の依頼か 1 回の目視で終わる。各項目の最後に、そこで見つかったときに進む先を書く。

1. **見えていない：要約の材料が原文そのものではなかった**
    - 何を見る：要約の材料が、原文の全体だったか。検索結果の断片、他人が書いた要約、貼り付けの一部、長い資料の前半だけ、のどれかではなかったか。
    - どう確かめる：要約の強い主張を 3 つほど選び、それぞれの根拠になる原文の箇所を、そのまま引用させる。引用が出せない、または引用した文が主張ほど強くないなら、この原因が疑わしい。
    - 見つかったとき：資料の渡し方を直す。長い資料は先に置いて、答えの前に引用を抜かせる（<!-- link:begin long-context-first#quote-first -->[長い資料は先、質問は最後 › 答えの前に引用を抜かせる](../prompting/long-context-first.md#quote-first)<!-- link:end -->）。面ごとの読み込みの限界は <!-- link:begin handing-long-documents#limits -->[長い資料を渡すとき › 面ごとの読み込みの限界](../context/handing-long-documents.md#limits)<!-- link:end --> を見る。後半だけが使われていないなら <!-- link:begin skipped-later-pages -->[添付した資料の後半を読んでいない](skipped-later-pages.md)<!-- link:end --> へ進む。
2. **確かめていない：要約が原文と照らされないまま使われた**
    - 何を見る：要約の中の強い言葉。「必ず」「常に」「すべて」「証明した」のような言い切りと、数や範囲を表す言葉を拾う。
    - どう確かめる：拾った言葉ごとに、原文の同じ主張の前後を探す。その近くに、限定の語（「場合がある」「〜の範囲では」「〜に限り」）、対象や標本や期間の記述、著者が書いた限界があるかを見る。あるのに要約になければ、落ちた条件である。照合は Claude にさせてもよい（依頼の雛形はこの節の終わりにある）。ただし、結果の引用は、原文を開いて自分の目で 1 か所は確かめる。
    - 見つかったとき：要約を根拠に使う前に、原文と照らす手順を入れる（<!-- link:begin fact-checking#summaries -->[事実を確かめる（引用・照合・best-of-N） › 要約を原文と照らす](../verify/fact-checking.md#summaries)<!-- link:end -->）。引用や出典の細部の確かめ方は <!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end --> を見る。与えられた仕様や読み物は、自分で要約を書いてから Claude に誤読を指摘させる（<!-- link:begin read-specs-yourself#misreading-detector -->仕様を自分で読み、AI に誤読を指摘させる › AI に誤読を指摘させる（準備中）<!-- link:end -->）。
3. **人の側：要約の言葉をそのまま次の文章に使う**
    - 何を見る：「正確に要約して」と頼んだだけで済んだと考えていないか。要約を一次の資料として別の文書や次の依頼に貼り直していないか。
    - どう確かめる：要約から取った数や結論が、いまの文書に原文の条件なしで入っていないかを見る。
    - 見つかったとき：人の側の落とし穴の全体は <!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end --> を見る。「正確に」と頼むだけでは直らないことがあるので、このページの「予防：要約の形で縛る」の節のように、要約の形で縛る。

どれにも当たらないときは、<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> に戻って、別の原因を疑う。

原因ごとの振り分け先は次の表である。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [長い資料は先、質問は最後 › 答えの前に引用を抜かせる](../prompting/long-context-first.md#quote-first) |
| 確かめていない | [事実を確かめる（引用・照合・best-of-N） › 要約を原文と照らす](../verify/fact-checking.md#summaries)<br>[引用や出典の確かめ方](../verify/checking-citations.md)<br>仕様を自分で読み、AI に誤読を指摘させる（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

照合の依頼は、次の形で出せる。原文を渡して、要約の主張を 1 つずつ原文の引用に結びつけさせ、落ちた限定を列に出させる。

<!-- gen:begin snippet summary-overstates-source/check-against-source -->
<!-- textlint-disable -->

??? example "雛形：要約を原文と照らさせる依頼"

    ```text
    次の「原文」と「要約」を照らして、要約が原文より強く言っている所を探してください。

    原文：
    <原文を貼る。または添付したファイルの名前を書く>

    要約：
    <確かめたい要約を貼る>

    要約の主張を 1 つずつ、次の列の表にしてください。
    要約の主張 | 原文の該当箇所の引用 | 原文にある条件・但し書き・限定 | 要約で落ちたもの

    - 引用は原文の文言のままにして、言い換えない
    - 該当する箇所が原文に見つからない主張は、引用の列に「見つからない」と書く
    - 最後に、原文の範囲を超えている主張だけを一覧にする。超えていなければ「なし」と書く
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet summary-overstates-source/check-against-source -->

この雛形は、Claude の答えを信じるためのものではなく、自分が原文のどこを開けばよいかを絞るためのものである。表の引用が原文にあるかは、自分で検索して確かめる。

## 判断例 {#example}

!!! example "判断例：論文の要約を、レポートの根拠に使う前"
    - **状況**：Claude に論文を要約させたところ、「この手法は有効である」と言い切る文が返った。論文の要旨は「一部の条件で効果が見られた」と書いているように思える。その要約をレポートの根拠に使いたい。
    - **迷う候補**：要約が自然で、ほかの記述も合っているので、そのまま使う。または、論文を最初から全部読み直す。どちらも筋は通る。
    - **選んだもの**：言い切りの文だけを抜き出し、Claude に原文の該当箇所を引用させて、前後の限定を自分で読む。限定が落ちていれば、レポートには限定つきの言い方で書く。結論の核になる 1 件だけは、原文を最初から自分で読む。
    - **理由**：全部読み直すのは費用が大きく、要約だけで使うと条件が落ちたまま広がる。強い言葉だけを照合すれば、安い費用で、いちばん危ない所に届く。核になる 1 件は、落ちた条件が結論を変えるので、省かない。

## 予防：要約の形で縛る {#prevention}

要約を頼む時点で、条件が残りやすい形にしておく。「正確に」と頼むだけでは直らないことがある（理由は <!-- link:begin summary-overgeneralization#what-helps -->[要約は原文より強く言いがち（過度な一般化） › 何に効くか](../basics/summary-overgeneralization.md#what-helps)<!-- link:end --> を見る）ので、形のほうを決める。

- 主張ごとに、原文の短い引用を付けさせる。
- 限定・対象・条件・著者の書いた限界を、主張の中に残させる。
- 原文から言えないことは「原文からは分からない」と書かせる。

次の依頼は、この 3 つをまとめたものだ。効果は、自分の資料で試して確かめる。

<!-- gen:begin snippet summary-overstates-source/summary-keeps-conditions -->
<!-- textlint-disable -->

??? example "雛形：条件を残して要約させる依頼"

    ```text
    次の資料を要約してください。

    - 主張ごとに、原文の該当箇所の短い引用を付ける
    - 「場合がある」「〜の範囲では」「〜に限り」のような限定、対象、条件、著者が書いた限界は、落とさずに主張の中へ残す
    - 原文にない一般化をしない。原文が一部の場合しか示していないことを、一般の事実のように書かない
    - 原文から言えないことは「原文からは分からない」と書く

    資料：
    <資料を貼る。または添付したファイルの名前を書く>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet summary-overstates-source/summary-keeps-conditions -->

調べものでは、出典の原文を開いて確かめる手順が、リサーチの使い方にも調べもののレポートにも書いてある（<!-- link:begin using-research#checking-sources -->リサーチを使いこなす › 出典の確かめ方（準備中）<!-- link:end -->、<!-- link:begin research-and-reports#check-sources -->[調べものとレポート › 出典を原文で確かめる](../recipes/research-and-reports.md#check-sources)<!-- link:end -->）。学習で上位解法を要約させるときは、手法・その手法を正当化した問題の性質・原文の短い引用の 3 列の表にさせるとよい（<!-- link:begin learning-with-ai#summaries-of-solutions -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 上位解法や解説を AI に要約させるとき](../judgment/learning-with-ai.md#summaries-of-solutions)<!-- link:end -->）。どの場合も、結論の核になる 1 件は、要約でなく原文を自分で読む。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)

**次に読む**

- [長い資料は先、質問は最後](../prompting/long-context-first.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [引用や出典の確かめ方](../verify/checking-citations.md)
- 仕様を自分で読み、AI に誤読を指摘させる（準備中）

**関連**

- [調べものとレポート](../recipes/research-and-reports.md)
- リサーチを使いこなす（準備中）
- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- [長い資料を渡すとき](../context/handing-long-documents.md)
- [もっともらしい嘘・出典の誤り](plausible-falsehoods.md)
- [添付した資料の後半を読んでいない](skipped-later-pages.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
