---
id: allow-i-dont-know
title: 「分からない」と言ってよいと伝える
aliases: [推測で埋めさせない, I don't know を許す, ハルシネーションを減らす頼み方]
type: concept
field: prompting
chapter: 正直さと確かめ方
order: 180
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない, 見えていない]
scenes: [調べもの, 学習, コンテスト]
summary: 分からなければ分からないと答えてよい、根拠のない所は推測と書け、と添えると、もっともらしい作り話が減る。減るだけで無くならないので、大事な事実は確かめる。
signs:
  - {type: goal, text: 分からないときは、分からないと答えてほしい}
  - {type: goal, text: 根拠のない部分は、推測だと分かるように書いてほしい}
prerequisites: [why-hallucinations]
related: [plausible-falsehoods, fact-checking, checking-citations, permission-to-stop, verification-ladder#verbal-checks, long-context-first, uses-nonexistent-apis]
sources: [api-docs-reduce-hallucinations, api-docs-prompting-best-practices, arxiv-2509-04664, anthropic-research-tracing-thoughts-language-model, chokudai-competitive-programming-genai-2025]
volatility: 低
sections:
  - {title: 分からないと言える逃げ道を作る, anchor: escape-hatch}
  - {title: 渡した資料だけを根拠にさせる, anchor: source-only}
  - {title: 答えを迫ると作り話が増える, anchor: pressure}
  - {title: 何に効くか, anchor: what-it-targets}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：分からなければ分からないと答えてよい、と依頼に添えると作り話が減るが、無くならないので大事な事実は確かめる。
    - **いつ引くか**：分からないときは分からないと答えてほしいとき。根拠のない部分は、推測だと分かるように書いてほしいとき。
    - **前提**：<!-- link:begin why-hallucinations -->[ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)<!-- link:end -->

<!-- textlint-disable -->
別名：推測で埋めさせない・I don't know を許す・ハルシネーションを減らす頼み方
<!-- textlint-enable -->

「分からない」と言ってよいと伝えるとは、答えに自信がない部分を、推測で埋めずに「分からない」と書いてよい、と依頼で先に許すことである。Claude は尋ねられると、根拠が薄くても答えの形を作りやすい。この許可は、その場の答えに「分からない」という選択肢を足す。事実を尋ね始める最初の段階から使える、作り話を減らす第一手である。

## 分からないと言える逃げ道を作る {#escape-hatch}

分からないと言える逃げ道を作るとは、依頼に「分からなければ分からないと答えてよい」と書き、推測を書くときは推測と分けて書かせることである。公式の hallucination 対策の文書も、手の 1 つとして「分からない」と言ってよいと明示することを挙げている。

!!! example "Before / After：実在が怪しい本の要旨を尋ねる"
    - **Before**：「2019 年刊の『分散システムの設計作法』という本の、第 7 章の要旨を教えて」とだけ頼む。この題は例のための架空のもので、答えは本の存在を前提にした章の要旨になりやすい。
    - **After**：同じ依頼に「この本について確かな知識がなければ、知らないと答えてよい。推測で補う部分は、文頭に『推測：』と付けて分けて書いて」と足す。
    - **足したもの**：「知らない」と答えてよいという許可と、推測を確かな部分と分ける書き方の指定。許可だけでなく、分けて書く形まで頼むと、読む側が確かめる場所を絞れる。

足す要素は 3 つある。許可（分からなければそう答えてよい）、分け方（推測には「推測：」を付ける）、理由（答えをどう使うか）である。理由を添えると、何を避けたいかが伝わり、書いていない場面にも応用が利く。たとえば「この答えを資料に使うので、誤りを確かなものとして読むより、分からないと分かるほうが困らない」と書く。

「分からない部分は、何が分かれば答えられるかも書いて」と足すと、行き止まりで終わらず、次に確かめる手が返りやすい。これは公式が勧める手ではなく、この辞典の提案である（推論・実践例なし）。

雛形を置く。質問の所だけ差し替えて使う。

<!-- gen:begin snippet allow-i-dont-know/escape-hatch -->
<!-- textlint-disable -->

???+ example "雛形：分からないと言える逃げ道を作る依頼の雛形"

    ```text
    以下の質問に答えてください。

    ＜質問をここに書く＞

    答えの扱いについて：
    - 確かな根拠がある部分は、そのまま答えてください。
    - 確かな根拠がない部分は、推測で補わずに「分からない」と書いてください。
    - 推測を書くときは、文頭に「推測：」と付けて、確かな部分と分けてください。
    - 分からない部分については、何が分かれば答えられるかも書いてください。

    理由：この答えをそのまま資料に使うので、誤った内容を確かなものとして読むより、分からないと分かるほうが困りません。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet allow-i-dont-know/escape-hatch -->

書く場所は面によって違うが、書く中身は同じである。

=== "アプリ"

    依頼の本文に書く。何度も使う文言は、会話の最初の依頼に置く。

=== "Claude Code"

    依頼の本文に書く。毎回の作業に効かせたい方針は、`CLAUDE.md` に理由とともに短く書く。ただし言葉だけで止められるわけではない。

=== "API"

    システムプロンプトに書く。出力を機械で読むときは、「分からない」を表す値（空欄や専用の語）を先に決めておく。

## 渡した資料だけを根拠にさせる {#source-only}

渡した資料だけを根拠にさせるとは、答えの材料を貼った資料だけに絞り、書かれていないことは一般知識で補わず「資料には書かれていない」と答えさせることである。公式の hallucination 対策も、提供した資料だけを使わせ、一般知識を使わせない手を挙げている。

逃げ道を作るだけでは、Claude が「知っているつもり」で答える場面を止めにくい。資料だけに絞ると、根拠が目に見える範囲に収まり、「資料に答えがない」という判断が具体的になる。資料に載っていない部分は、そのまま「分からない」の対象になる。

!!! example "判断例：資料に書かれていない質問が来たとき"
    - **状況**：社内の手順書を貼り、手順書に載っていない細部を尋ねる。
    - **迷う候補**：一般知識でも答えさせる。資料だけで答えさせ、なければ「書かれていない」と返させる。
    - **選んだもの**：資料だけで答えさせる。
    - **理由**：社内の決まりは、一般知識で補うと実際の運用と食い違う。補った部分が資料の内容に見えると、読む側が区別できない。一般的な技術の質問なら、一般知識を使わせたうえで、資料にある部分と分けて書かせる候補も筋が通る。

長い資料では、答える前に関係する箇所を原文から引用させると、根拠のない主張に気づきやすい。引用の手順と主張ごとの照合は、持ち主のページに任せる。

- 長い資料の置き方：<!-- link:begin long-context-first#quote-first -->[長い資料は先、質問は最後 › 答えの前に引用を抜かせる](long-context-first.md#quote-first)<!-- link:end -->
- 引用での確かめ方：<!-- link:begin fact-checking#quotes -->[事実を確かめる（引用・照合・best-of-N） › 主張ごとに引用させる](../verify/fact-checking.md#quotes)<!-- link:end -->
- 資料の範囲で答えさせる手順：<!-- link:begin fact-checking#sources-only -->[事実を確かめる（引用・照合・best-of-N） › 渡した資料の範囲で答えさせる](../verify/fact-checking.md#sources-only)<!-- link:end -->

<!-- gen:begin snippet allow-i-dont-know/source-only -->
<!-- textlint-disable -->

??? example "雛形：渡した資料だけを根拠にさせる依頼の雛形"

    ```text
    ＜資料＞
    ＜資料の全文をここに貼る＞
    ＜/資料＞

    ＜質問＞
    ＜質問をここに書く＞
    ＜/質問＞

    上の資料だけを根拠に答えてください。資料に書かれていないことは、あなたの一般的な知識で補わず、「資料には書かれていない」と答えてください。
    答えには、根拠にした資料の箇所を原文のまま引用して添えてください。引用が見つからない主張は、答えから外してください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet allow-i-dont-know/source-only -->

## 答えを迫ると作り話が増える {#pressure}

答えを迫ると作り話が増えるとは、「必ず答えて」「諦めるな」のように成果を強く迫ると、逃げ道が消えて、根拠のない答えが出やすくなることである。迫る言い方は、逃げ道を作る言い方と逆向きに働く。

競技プログラミングの実践者は、AI は常に何かを出力してしまい、自分の答えが誤りだと判断して提出を控えることができない、と指摘している（根拠：弱。立場の表明）。誤答に減点や失格がある場では、作り話の提出がそのまま損失になる。競技の規則の細部と練習の進め方は、kyopro-atlas にある。

迫る代わりに、成果の形を「分かったこと・分からないこと・次に確かめる手」にする。答えを出さないことを失敗にしない形である。

!!! example "判断例：行き詰まった調べものを続けさせる"
    - **状況**：資料が見つからない事実を、期限が近いので何としても答えさせたい。
    - **迷う候補**：「必ず答えを出して」と迫る。見つかった範囲と見つからなかった範囲を報告させる。
    - **選んだもの**：見つかった範囲と見つからなかった範囲を報告させる。
    - **理由**：迫ると、見つからなかった部分が推測で埋まり、確かな部分と区別できなくなる。報告なら、足りない部分だけを自分で確かめに行ける。

エージェントに作業を任せる場面で、テストや評価がおかしいと判断したら止まって報告してよいと伝える手は、<!-- link:begin permission-to-stop -->[止まって報告する権利を渡す](permission-to-stop.md)<!-- link:end --> が持つ。

## 何に効くか {#what-it-targets}

「分からなくてよい」と依頼に添える手が効く先は、原理では「確かめる」、Claude 側の原因では「確かめていない」と「見えていない」である。

「確かめていない」とは、Claude が答える前に、その内容に根拠があるかを自分で確かめないまま答えを出すことである。分からないと言ってよい、推測は推測と書け、と頼むと、根拠の有無が答えの表に出る。読む側は、推測と書かれた所だけを優先して確かめればよい。これは確かめる作業を減らすのではなく、確かめる場所を絞る手である。

「見えていない」とは、答えに要る資料が Claude の手元にない、または古い知識のままであることである。資料を渡し、その範囲に答えを限れば、見えていないものを「見えていない」と言わせやすくなる。

効く理由の 1 つは、モデルが山を張る受験生に似た傾向を持つことである。OpenAI らの論文（2025 年）は、多くのベンチマークが正解だけを 1 点とし、不正解も無回答も 0 点とすると述べる。この採点では、分からないと言うより推測したほうが得になる（根拠：中。研究の主張）。分からなくても答えるほうが得になる訓練の話は <!-- link:begin why-hallucinations#guess-pays -->[ハルシネーションはなぜ起きるか › 分からなくても答えるほうが得になる訓練](../basics/why-hallucinations.md#guess-pays)<!-- link:end --> にある。

もう 1 つは、名前を知っているだけで、断る既定が外れる仕組みである。Anthropic の解釈可能性研究（2025 年 3 月）は、Claude の既定は「十分な情報がない」と答える回路で、知っている実体を認識するとこの既定が抑制される、と報告している。名前は聞き覚えがあるが中身を知らないとき、「既知」の特徴が誤って働き、もっともらしい誤りが出る（根拠：中。企業の一次の報告で、対象はその研究のモデル）。くわしくは <!-- link:begin why-hallucinations#known-name -->[ハルシネーションはなぜ起きるか › 名前を知っているだけで断る既定が外れる](../basics/why-hallucinations.md#known-name)<!-- link:end --> にある。

依頼で「分からなくてよい」と許しても、訓練の傾きは直らない。依頼でできるのは、この会話の中で「分からない」も受け入れられる答えだと示すところまでで、性質はお願いである。仕組みで強制する鍵ではないので、効き目は確実ではない。公式も、これらの手は hallucination を大きく減らすが無くしはしないと書き、重要な情報、特に重大な判断に関わるものは検証せよとしている。

## 効かない場面とやりすぎ {#limits}

効かない場面は 3 つある。

- **Claude が知っているつもりのとき**：中身を知らないのに知っていると認識している場合、「分からない」と言う場面がそもそも来ない。許可を書いても、確かなものとして誤りが返る。この場合は、答えの外で確かめる。
- **推測と書かれていない部分が正しいとは限らないとき**：「推測：」の印は、書き手の自己申告である。印のない部分も、重要なものは確かめる。引用や出典は <!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end -->、事実の照合は <!-- link:begin fact-checking#overall-check -->[事実を確かめる（引用・照合・best-of-N） › 全体の確かめ方](../verify/fact-checking.md#overall-check)<!-- link:end --> に手順がある。
- **言葉の許可だけを頼りにしたとき**：成果を迫る力が強いと、許可は守られないことがある。守らせたいことは、答えの外の照合や仕組みと組み合わせる。「念のため確認して」と書き足すより、確かめる手段を渡すほうが効く。選び方は <!-- link:begin verification-ladder#verbal-checks -->[検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)<!-- link:end --> にある。

やりすぎにも注意する。「少しでも自信がなければ分からないと答えて」と強く書くと、答えられることまで「分からない」と返すことがある（推論・実践例なし）。「確かな根拠がある部分は、そのまま答えて」と対にして書く。

原因を切り分けたいときは、<!-- link:begin plausible-falsehoods#diagnosis -->[もっともらしい嘘・出典の誤り › 原因を安く確かめる順](../symptoms/plausible-falsehoods.md#diagnosis)<!-- link:end --> と <!-- link:begin uses-nonexistent-apis#diagnosis -->[存在しない関数やパッケージを使う › 原因を安く確かめる順](../symptoms/uses-nonexistent-apis.md#diagnosis)<!-- link:end --> の診断が先である。許可を足す前に、資料が見えていないだけではないかを確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664)：arXiv（Kalai, Adam Tauman ほか）・英語・確認日 2026-11-04
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)：Anthropic・英語・確認日 2026-11-04
- [競技プログラミングと生成AIの今 2025/07/02版](https://chokudai.hatenablog.com/entry/2025/07/02/151841)：chokudai・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)

**次に読む**

- [止まって報告する権利を渡す](permission-to-stop.md)

**関連**

- [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [引用や出典の確かめ方](../verify/checking-citations.md)
- [検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)
- [長い資料は先、質問は最後](long-context-first.md)
- [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
