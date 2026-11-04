---
id: fact-checking
title: 事実を確かめる（引用・照合・best-of-N）
nav_title: 事実を確かめる
aliases: [ファクトチェック, 裏取り, ハルシネーション対策]
type: recipe
field: verify
chapter: 事実を確かめる
order: 60
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない, 見えていない]
pitfalls: []
scenes: [調べもの, 文章, 学習]
summary: 答えの中の事実を、根拠の引用・資料との照合・同じ質問の繰り返しで確かめられる。重要な事実ほど、一次の資料で裏を取る。
signs:
  - {type: goal, text: 答えの中の事実が正しいか確かめたい}
  - {type: goal, text: 渡した資料に書いてあることだけで答えさせたい}
  - {type: goal, text: 要約が原文に書いてあるとおりかを照らしたい}
prerequisites: [why-hallucinations]
related: [learning-with-ai, evidence-not-reports, claims-done-but-isnt, checking-citations, plausible-falsehoods, allow-i-dont-know, doesnt-know-latest, knowledge-cutoff, nondeterminism, search-research-thinking, using-research, summary-overgeneralization, summary-overstates-source, handing-long-documents, research-and-reports, read-specs-yourself, citations-basics]
tracks: [web-search, research, citations]
outdated_advice: []
sources: [api-docs-reduce-hallucinations, cc-changelog]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guard}
  - {title: 主張ごとに引用させる, anchor: quotes}
  - {title: 渡した資料の範囲で答えさせる, anchor: sources-only}
  - {title: 何度か聞いて比べる（best-of-N）, anchor: best-of-n}
  - {title: 要約を原文と照らす, anchor: summaries}
  - {title: 全体の確かめ方, anchor: overall-check}
  - {title: うまくいかないとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：答えの中の事実を、根拠の引用・資料との照合・同じ質問の繰り返しで確かめられる。重要な事実ほど、一次の資料で裏を取る。
    - **いつ引くか**：答えの中の事実が正しいか確かめたいとき。渡した資料に書いてあることだけで答えさせたいとき。要約が原文に書いてあるとおりかを照らしたいとき。
    - **前提**：<!-- link:begin why-hallucinations -->[ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)<!-- link:end -->

<!-- textlint-disable -->
別名：ファクトチェック・裏取り・ハルシネーション対策
<!-- textlint-enable -->

事実を確かめるとは、Claude の答えの中の事実を、そのまま信じず、根拠・資料・繰り返しの 3 つで照らすことである。事実の誤りは、返答を読んで使い始めた最初から起こりうる。このページは、依頼の中で頼める 4 つの確かめ方を、用途ごとに並べる。

## 先に整える守り {#guard}

手順の前に、誤りを減らす土台を 3 つ置く。どれも誤りを減らすだけで、無くしはしない。公式は、これらの技法でハルシネーションが大きく減るとしている。ただし無くなりはしないので、重大な判断に関わる情報は検証せよと求める（[Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)）。

- **分からないと言ってよいと伝える**：分からないまま答えを作らせないための逃げ道になる。書き方は <!-- link:begin allow-i-dont-know#escape-hatch -->[「分からない」と言ってよいと伝える › 分からないと言える逃げ道を作る](../prompting/allow-i-dont-know.md#escape-hatch)<!-- link:end --> に任せる。
- **確かめる材料を渡す**：最近の出来事や新しい版は、モデルの知識の外にある。検索の結果や公式の資料を渡す。切り分けは <!-- link:begin doesnt-know-latest#diagnosis -->[最新の情報を知らない › 原因を安く確かめる順](../symptoms/doesnt-know-latest.md#diagnosis)<!-- link:end --> にある。
- **長い資料は形と量を整える**：読まれていない部分があると、確かめる元がずれる。分け方は <!-- link:begin handing-long-documents#split-and-convert -->[長い資料を渡すとき › 分ける・形を直す](../context/handing-long-documents.md#split-and-convert)<!-- link:end --> にある。

「正確に書いて」と頼むだけでは、確かめたことにならない。要約は、頼んでも原文の条件を落とすことがある。理由は <!-- link:begin summary-overgeneralization -->[要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)<!-- link:end --> にある。確かめるには、照らす先（引用・資料・繰り返しの結果）を作る。

## 主張ごとに引用させる {#quotes}

答えの主張ごとに、根拠になる原文の引用を付けさせ、引用できない主張を外させる。引用を付けさせると、答えが「どこに書いてあるか」で照らせる形になる。

1. 資料のうち質問に関係する箇所を、原文のまま先に抜き出させる。長い資料では特に効く。詳しい頼み方は <!-- link:begin handing-long-documents#quotes-first -->[長い資料を渡すとき › 引用を先に抜かせる](../context/handing-long-documents.md#quotes-first)<!-- link:end --> にある。
2. 答えの主張に、引用の番号を付けさせる。
3. 書き終えた後に、主張を 1 つずつ見直させ、引用で裏づけられない主張を外させる。外した所には印を付けさせる。

各段の確かめは、次のとおりである。

- 段 1 の終わり：抜き出された引用を、資料の中で文字列検索する。見つからない引用が 1 つでもあれば、その引用は作られている。
- 段 3 の終わり：外された主張の数を見る。0 件のときは、見直しが形だけだった疑いがある。外された主張の一覧を出させる。

依頼の雛形は次のとおりである。

<!-- gen:begin snippet fact-checking/quote-each-claim -->
<!-- textlint-disable -->

??? example "雛形：主張ごとに引用を付けさせ、引用できない主張を外させる依頼"

    ```markdown
    下の資料だけを根拠に、【質問】に答えてほしい。

    【質問】
    （ここに質問を書く）

    【資料】
    （ここに資料を貼る。ファイルなら、そのパスを書く）

    進め方：
    1. 先に、質問に関係する箇所を、資料から一字も変えずに抜き出す。番号を付ける。関係する箇所がなければ「該当する箇所なし」と書く。
    2. 答えは、抜き出した引用だけを根拠に書く。答えの主張の後ろに、根拠にした引用の番号を付ける。
    3. 書き終えたら、答えの主張を 1 つずつ見直す。引用で裏づけられない主張は、答えから外す。外した所には【削除】と書き、外した主張は最後に一覧にする。
    4. 資料に書いていないことは、推測だと分かる形で別にまとめる。推測は答えの本文に混ぜない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet fact-checking/quote-each-claim -->

API では、指示で引用させる代わりに、根拠の箇所を返させる機能がある。違いは <!-- link:begin citations-basics#vs-prompting -->citations（根拠の箇所を返させる） › 引用させる指示との違い（準備中）<!-- link:end --> にある。

## 渡した資料の範囲で答えさせる {#sources-only}

渡した資料に書いてあることだけで答えさせる。資料の外の知識を混ぜさせないと、答えの根拠が資料に絞られ、照らす先が 1 つに決まる。公式は、この制限を、資料以外の一般知識を使わせない指示として挙げている（[Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)）。

資料を渡す手段は、面で違う。

=== "アプリ"

    資料を添付するか貼り、依頼に「この資料だけを根拠にする」と書く。資料に書いていないときは答えを作らず、その旨を書かせる。

=== "Claude Code"

    資料をファイルとして置き、そのパスを依頼に書く。根拠は、ファイルの文言をそのまま引かせる。

=== "API"

    資料を依頼の本文に入れる。根拠の箇所まで返させるなら、<!-- link:begin citations-basics#limits -->citations（根拠の箇所を返させる） › 一緒に使えない機能（準備中）<!-- link:end --> の制約を先に確かめる。

依頼の雛形は次のとおりである。

<!-- gen:begin snippet fact-checking/sources-only -->
<!-- textlint-disable -->

??? example "雛形：渡した資料の範囲だけで答えさせる依頼"

    ```markdown
    【質問】に、下の【資料】に書いてあることだけで答えてほしい。

    【質問】
    （ここに質問を書く）

    【資料】
    （ここに資料を貼る。ファイルなら、そのパスを書く）

    - 資料の外の知識や、検索で調べたことは使わない。
    - 資料に書いていないときは、答えを作らず「資料には書かれていない」と書く。
    - 答えの根拠にした箇所を、資料の文言のまま添える。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet fact-checking/sources-only -->

確かめは、資料に書いていない質問を 1 つ混ぜて出すことである。「書かれていない」と返れば、制限が効いている。答えが返ったら、制限が効いていない疑いがある。書き方は <!-- link:begin allow-i-dont-know#source-only -->[「分からない」と言ってよいと伝える › 渡した資料だけを根拠にさせる](../prompting/allow-i-dont-know.md#source-only)<!-- link:end --> にもある。

## 何度か聞いて比べる（best-of-N） {#best-of-n}

同じ依頼を何度か出し、答えを比べる。答えの食い違いは、ハルシネーションの疑いの合図になる（[Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)）。同じ依頼でも答えが毎回少し変わる理由は <!-- link:begin nondeterminism -->[同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)<!-- link:end --> にある。

1. 同じ依頼を、会話を分けて数回出す。同じ会話の続きで聞くと、前の答えに引きずられやすい（推論・実践例なし）。
2. 文面ではなく、事実の主張（数値・日付・名前・有無）を並べて比べる。
3. 食い違った主張だけを、一次の資料で確かめる。

=== "アプリ"

    新しいチャットを開き、同じ依頼を貼る。これを数回繰り返す。

=== "Claude Code"

    新しいセッションを開き、同じ依頼を出す。履歴を引き継がない。

=== "API"

    同じリクエストを数回送る。会話の履歴は含めない。

一致は、正しさの保証にならない。同じ誤りを何度も返すことがある（推論・実践例なし）。比べるのは、疑う箇所を絞るためである。

!!! example "判断例：3 回聞いて 2 回一致したとき"
    - **状況**：ある機能の導入日を同じ依頼で 3 回聞いた。2 回は同じ日付、1 回は別の日付だった。
    - **迷う候補**：多数決で 2 回出た日付を採る。3 つとも一次の資料で確かめる。
    - **選んだもの**：一次の資料で確かめる。
    - **理由**：食い違いは、この日付が不確かな合図である。多数決は、同じ誤りが 2 回出た場合に誤りを選ぶ。機能の日付は、公式の文書で確かめられる。

## 要約を原文と照らす {#summaries}

要約が原文に書いてあるとおりかを、主張ごとに原文の引用を付けさせて照らす。AI の要約は、原文の条件や限定を落として主張の範囲を広げがちである。症状と診断は <!-- link:begin summary-overstates-source#diagnosis -->[要約が原文より断定的になる › 原因を安く確かめる順](../symptoms/summary-overstates-source.md#diagnosis)<!-- link:end --> にある。

1. 要約を、主張・原文の短い引用・条件や限定の 3 列の表にさせる。
2. 数値は原文のとおりに写させる。丸めさせない。
3. 原文に書かれていることと、推測を分けさせる。原文にない一般化を禁じるだけでは、お願いで終わる。引用の列があると、照合できる形になる。
4. 引用を原文で文字列検索する。見つからない引用は、作られている。
5. 一番重要な主張は、原文を自分で読む。読み方は <!-- link:begin read-specs-yourself#read-first -->仕様を自分で読み、AI に誤読を指摘させる › 先に自分で読んで要約する（準備中）<!-- link:end --> にある。

依頼の雛形は次のとおりである。

<!-- gen:begin snippet fact-checking/summary-with-quotes -->
<!-- textlint-disable -->

??? example "雛形：要約の主張ごとに原文の引用を付けさせ、書かれていることと推測を分けさせる依頼"

    ```markdown
    下の【原文】を要約してほしい。主張ごとに、原文の根拠を付ける。

    【原文】
    （ここに原文を貼る。ファイルなら、そのパスを書く）

    要約の書き方：
    - 表にする。列は「主張」「原文の短い引用」「条件・限定」の 3 つ。
    - 引用は原文から一字も変えずに抜き出す。引用できない主張は、表に入れない。
    - 「条件・限定」の列に、原文がその主張に付けている条件、範囲、例外を書く。原文にそれがなければ「なし」と書く。
    - 数値は原文のとおりに写す。丸めたり、言い換えたりしない。
    - 原文にない一般化はしない。原文に書かれていることと、あなたの推測は、表を分けて書く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet fact-checking/summary-with-quotes -->

上位の解法を、手法・それを正当化した性質・原文の引用の表で要約させる使い方は、<!-- link:begin learning-with-ai -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)<!-- link:end --> にある。このページでは、調べもの一般の要約の照らし方だけを扱う。

## 全体の確かめ方 {#overall-check}

引用・資料の限定・繰り返し・要約の照合のどれを使った後でも、最後に答え全体を確かめる。

- **引用の実在**：引用が原文にそのまま見つかるか。文字列検索で確かめる。Claude Code では、原文のファイルを検索して照らせる。
- **主張の重さ**：重要な事実（金額・日付・法律・安全・他人に出す文書）は、一次の資料を開いて確かめる。出典のある報告は、<!-- link:begin research-and-reports#check-sources -->[調べものとレポート › 出典を原文で確かめる](../recipes/research-and-reports.md#check-sources)<!-- link:end --> と <!-- link:begin using-research#checking-sources -->リサーチを使いこなす › 出典の確かめ方（準備中）<!-- link:end --> で原文に照らす。
- **出典そのもの**：挙げられた文献や引用が、実在し、題名・著者・年まで合うか。実在しても細部が違う誤りは、<!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](checking-citations.md#steps)<!-- link:end --> で確かめる。
- **決める人**：結論を決めるのは人である。Claude の要約や自己申告に決定を渡さない。

確かめた主張と確かめていない主張は、分けて記録する。そうすると、未確認の主張が最終の文書に混ざらない。

## うまくいかないとき {#when-it-fails}

確かめても誤りが残るときは、困りごとの形から次のページへ進む。

- **引用が原文にない、または言い換えられている**：指示で引用させても、引用は作られうる。API なら、<!-- link:begin citations-basics#vs-prompting -->citations（根拠の箇所を返させる） › 引用させる指示との違い（準備中）<!-- link:end --> の方法を検討する。
- **実在する文献だが、細部が違う**：<!-- link:begin checking-citations#error-types -->[引用や出典の確かめ方 › よくある誤りの形](checking-citations.md#error-types)<!-- link:end --> で誤りの形を調べる。
- **もっともらしい嘘が出る**：<!-- link:begin plausible-falsehoods#diagnosis -->[もっともらしい嘘・出典の誤り › 原因を安く確かめる順](../symptoms/plausible-falsehoods.md#diagnosis)<!-- link:end --> で原因を切り分ける。
- **最近の話で間違う**：<!-- link:begin knowledge-cutoff -->[知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)<!-- link:end --> を確かめ、検索の結果か最新の資料を渡す。調べ方の選択は <!-- link:begin search-research-thinking#comparison -->[web 検索・リサーチ・拡張思考の使い分け › 三つの使い分け](../app/search-research-thinking.md#comparison)<!-- link:end --> にある。
- **要約が原文より断定的**：<!-- link:begin summary-overstates-source#diagnosis -->[要約が原文より断定的になる › 原因を安く確かめる順](../symptoms/summary-overstates-source.md#diagnosis)<!-- link:end --> で、落ちた条件を見つける。
- **「ない」と言い切られた**：検索が途中で打ち切られていないかを疑う。Claude Code では、過去の版で、Grep と Glob の検索が時間切れで途中までの結果しか返さないのに、Claude がそれを全部の結果とみなす不具合があった。直った版は [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) にある。「ない」と言われたときは、検索のコマンドと出力を見せさせて、自分でも確かめる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)

**次に読む**

- [引用や出典の確かめ方](checking-citations.md)
- [知らないコードベースを読む](../recipes/explore-a-codebase.md)
- 仕様を自分で読み、AI に誤読を指摘させる（準備中）
- ドキュメント・技術文書を書く（準備中）
- 資料・スライドを作る（準備中）

**関連**

- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- [報告ではなく証拠を求める](evidence-not-reports.md)
- [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)
- [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)
- [最新の情報を知らない](../symptoms/doesnt-know-latest.md)
- [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)
- [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- リサーチを使いこなす（準備中）
- [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)
- [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)
- [長い資料を渡すとき](../context/handing-long-documents.md)
- [調べものとレポート](../recipes/research-and-reports.md)
- citations（根拠の箇所を返させる）（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
