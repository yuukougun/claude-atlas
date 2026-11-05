---
id: research-and-reports
title: 調べものとレポート
aliases: [調査を頼む, リサーチ, 文献の整理, 出典つきのレポート]
type: recipe
field: recipes
chapter: 調べものと文書
order: 160
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [確かめる, 見せる]
prevents: [確かめていない, 見えていない]
pitfalls: [預けすぎる]
scenes: [調べもの, 文章]
summary: 調べものは、問いと範囲を決めてから頼み、出典つきのレポートを書かせる。結論は出典の原文と照らして確かめ、書かれていることと推測を分けさせる。
signs:
  - {type: goal, text: ある技術や製品について、出典つきで調べてほしい}
  - {type: symptom, text: レポートの出典を開くと、書かれていないことが書いてある}
  - {type: goal, text: いくつかの記事や論文を読み比べて、違いを整理したい}
prerequisites: [search-research-thinking, checking-citations]
related: [using-research, artifacts-overview, using-projects, fact-checking, plausible-falsehoods, summary-overgeneralization, doesnt-know-latest, knowledge-cutoff, research-in-subagents, read-specs-yourself, write-docs, make-slides, documents-in-japanese, second-opinion-from-another-model]
tracks: [research, web-search, projects, artifacts]
outdated_advice: [cowork-separate-app]
sources: [hc-research, hc-web-search, hc-projects-what, hc-artifacts, hc-cowork-and-chat]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guard}
  - {title: 調べものの進め方, anchor: steps}
  - {title: 問いと範囲を先に決める, anchor: define-the-question}
  - {title: アプリと Claude Code の使い分け（リサーチ・プロジェクト・アーティファクト）, anchor: app-or-claude-code}
  - {title: 出典を原文で確かめる, anchor: check-sources}
  - {title: うまくいかないとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：問い・範囲・出典の条件を決めて頼み、出典つきのレポートを受け取って、結論を原文と照らしてから使える。
    - **いつ引くか**：ある技術や製品を出典つきで調べてほしいとき、レポートの出典を開くと書かれていないことが書いてあったとき、いくつかの記事や論文を読み比べたいとき。
    - **前提**：<!-- link:begin search-research-thinking -->[web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)<!-- link:end -->、<!-- link:begin checking-citations -->[引用や出典の確かめ方](../verify/checking-citations.md)<!-- link:end -->

<!-- textlint-disable -->
別名：調査を頼む・リサーチ・文献の整理・出典つきのレポート
<!-- textlint-enable -->

調べものとレポートは、Claude に調べさせて、出典つきの文書を受け取る作業である。レポートは体裁が整っているほど、そのまま信じやすい。このページは、頼む前に問いと範囲を決め、受け取った後に原文で確かめる進め方を書く。

## 先に整える守り {#guard}

レポートを受け取る前に、確かめる前提と、確かめられる形を整える。この作業で起きやすい失敗は 3 つある。Claude 側の「確かめていない」は、記憶で補い、読んでいない資料を読んだように書くことだ。「見えていない」は、どこまで調べたかがレポートから分からないことだ。人の側の「預けすぎる」は、体裁が整ったレポートを、原文に当たらずに使うことだ。

- **使う前に原文で確かめる前提で頼む**：出典の題名・著者・年と、引用の文言が実在の資料と合っているかを、人が原文を開いて見る。実在する文献でも、細部の違う誤りは起きる。手順は <!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end --> にある。
- **書かれていることと推測を分けさせる**：原文にあることと補ったことが混ざると、読み手は見分けにくい。分けて書かせ、原文の短い引用を添えさせる。雛形は「出典を原文で確かめる」の節に置いた。
- **最新の情報は、日付と検索結果で支える**：モデルの知識は、ある時点で止まっている。最近の出来事や新しい版は、検索結果と日付を根拠にさせる。理由は <!-- link:begin knowledge-cutoff#why -->[知識カットオフと「今」を知らない問題 › なぜ知らないのか](../basics/knowledge-cutoff.md#why)<!-- link:end --> にある。

確かめ方の全体像は、<!-- link:begin fact-checking#guard -->[事実を確かめる（引用・照合・best-of-N） › 先に整える守り](../verify/fact-checking.md#guard)<!-- link:end --> が持っている。このページは、調べもの向けの運び方だけを足す。

## 調べものの進め方 {#steps}

調べものは、次の 5 段で進める。各段に、終わったかを確かめる目安を付けた。

1. 問いと範囲を決める。目安：問いが 1 文で言え、範囲外にするものも決まっている。
2. 道具を選ぶ。目安：資料がどこにあるか（web・渡す資料・手元のファイル）で選んだ。
3. 頼む。目安：返答の主張ごとに、出典と原文の引用が付き、推測が分けてある。
4. 原文で確かめる。目安：使う主張ごとに、原文の該当箇所を自分で開いた。
5. 直させて仕上げる。目安：確かめられなかった主張が、本文に残っていない。

5 では、確かめられなかった主張と引用のない主張を、Claude に指して消させるか「未確認」と書かせる。消えたかは、返ってきた文書を自分で読み直して見る。

5 の後に、レポートを文書や資料の形に整えるなら、<!-- link:begin write-docs -->[ドキュメント・技術文書を書く](write-docs.md)<!-- link:end -->、<!-- link:begin make-slides -->[資料・スライドを作る](make-slides.md)<!-- link:end --> が持ち主である。日本語の資料を読ませるときは、<!-- link:begin documents-in-japanese#pdf -->[日本語の資料を読ませる・書かせる › 日本語の PDF を渡す前と後に確かめること](../japanese/documents-in-japanese.md#pdf)<!-- link:end --> を先に見る。

## 問いと範囲を先に決める {#define-the-question}

問いと範囲を決めてから頼む。決めずに頼むと、Claude が問いの解釈と調べる範囲を決めてしまい、何を調べなかったかがレポートから見えなくなる。

頼む前に、次の 4 つを決める。

- **使い道**：この結果で何を決めるか。使い道が違えば、必要な深さと資料の種類が変わる。
- **範囲と範囲外**：対象・期間・言語と、調べないもの。
- **出典の条件**：公式や一次の資料を優先するか。二次の資料を使うときは区別させるか。
- **出力の形**：結論・根拠・分からなかったこと、の順に書かせる。

いくつかの記事や論文を読み比べたいときは、これに加えて、比べる軸（対象・条件・前提・結論）を先に決める。軸を決めると、資料ごとに違いが同じ欄に並び、違いが見つけやすくなる。資料は、自分で選んで渡すか、URL を指定する。

頼み方の詳細（範囲・出典の条件・出力の形）は、<!-- link:begin using-research#requesting -->[リサーチを使いこなす › 頼み方（範囲・出典の条件・出力の形）](../app/using-research.md#requesting)<!-- link:end --> が持ち主である。次の雛形は、4 つを埋めて出す依頼の形である。

<!-- gen:begin snippet research-and-reports/research-request -->
<!-- textlint-disable -->

??? example "雛形：問い・範囲・出典の条件を決めた調べものの依頼"

    ```text
    次の問いについて、出典つきで調べてレポートにしてください。

    問い：（1 文で書く。例：A と B の違いは何か）
    使い道：（この結果で何を決めるか）
    範囲：（対象・期間・言語。例：公式の文書と、直近 1 年の論文）
    範囲外：（調べないもの）
    出典の条件：（公式・一次の資料を優先する。二次の資料を使うときは、そう書く）

    出力の形：
    - 結論を先に、3 行以内で書く
    - 結論の根拠を、主張ごとに「出典の題名・URL・原文からの短い引用」で付ける
    - 原文に書かれていないこと（推測や一般論）は、「推測」と書いて分ける
    - 調べられなかったこと、資料が見つからなかったことは、黙らずに最後に書く
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet research-and-reports/research-request -->

## アプリと Claude Code の使い分け（リサーチ・プロジェクト・アーティファクト） {#app-or-claude-code}

調べものの道具は、資料がどこにあるか、どれだけ広く調べるか、結果をどう残すかで選ぶ。アプリで使う 4 つの機能は、次のとおりである。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 面 | 強制力 | 入った版 |
| --- | --- | --- | --- |
| [リサーチ（Research）](../app/using-research.md) | アプリ | お願い | 2025-04-15 |
| [Web 検索（web search。アプリ）](../app/search-research-thinking.md) | アプリ | — | 2025-03-20 |
| [プロジェクト（Projects）](../app/using-projects.md) | アプリ | なし | 2024-06-25 |
| [アーティファクト（artifacts）](../app/artifacts-overview.md) | アプリ・Claude Code | なし | 2024-06-20 |

すべて共通：成熟度 GA、確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare -->

面ごとの使い分けは、次のとおりである。

=== "アプリ"
    - **リサーチ**：広く web を調べて、出典つきのレポートを受け取りたいとき。起動しないときの頼み方と、使える条件は <!-- link:begin using-research#requesting -->[リサーチを使いこなす › 頼み方（範囲・出典の条件・出力の形）](../app/using-research.md#requesting)<!-- link:end --> にある。
    - **web 検索と拡張思考との使い分け**：最新の情報が要るか、どれだけ広く調べるかで選ぶ。基準は <!-- link:begin search-research-thinking#choose -->[web 検索・リサーチ・拡張思考の使い分け › 選び方](../app/search-research-thinking.md#choose)<!-- link:end --> にある。
    - **プロジェクト**：同じ資料を固定して、繰り返し調べるとき。資料は置いたまま、問いだけを変えられる。目的を混ぜない単位は <!-- link:begin using-projects#scope -->[プロジェクトの使いどころ › プロジェクトを切る単位（1つに1つの目的）](../app/using-projects.md#scope)<!-- link:end --> にある。
    - **アーティファクト**：レポートを文書として残し、直し、共有するとき。直し方は <!-- link:begin artifacts-overview#editing -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › 直し方（頼む・直接直す・範囲を選ぶ）](../app/artifacts-overview.md#editing)<!-- link:end -->、公開するときの注意は <!-- link:begin artifacts-overview#sharing -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › 公開と共有](../app/artifacts-overview.md#sharing)<!-- link:end --> にある。

=== "Claude Code"
    - **手元の資料に基づく調べもの**：コードベース・ローカルのファイル・ログを読んで答えさせるとき。根拠が手元のファイルになるので、ファイルの場所を出典として挙げさせる。
    - **出力の多い調査**：多数のファイルを読む調査は、別の文脈で行わせて、結論と根拠の場所だけを受け取る。使いどころは <!-- link:begin research-in-subagents#when -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 任せてよい調査、本筋で読むべきもの](../context/research-in-subagents.md#when)<!-- link:end --> にある。
    - **web の資料**：Claude Code で web を調べさせるときの設定と権限は、この辞典では確かめていない（未確認）。広く web を調べるレポートは、アプリのリサーチのほうが手順を確かめやすい。

!!! example "判断例：3 つの技術記事を読み比べたい"
    - **状況**：同じ題材について書かれた技術記事が 3 本あり、前提と結論の違いを整理したい。
    - **迷う候補**：リサーチに「この題材を広く調べて」と頼む。または、3 本を自分で選んで会話に渡し、比べる軸を決めて表にさせる。
    - **選んだもの**：3 本を渡して表にさせる。
    - **理由**：比べる対象が決まっていて、範囲を自分で決められる。出典が渡した原文に限られるので、確かめる先も 3 本に決まる。対象が決まっていない調べものなら、リサーチのほうが向く。

新しい Claude の体験では、Web 検索の切り替えはなく、Claude が要るときに自分で検索する。入力欄に「Chat」と「Cowork」の選択が残るアカウントは、前のやり方のままである。古くなった助言の台帳は <!-- link:begin outdated-advice-ledger#cowork-separate-app -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#cowork-separate-app)<!-- link:end --> にある。手順書に「Web 検索をオンにする」とあっても、自分のアカウントの体験に合うかを先に見る。

## 出典を原文で確かめる {#check-sources}

レポートの出典は、使う主張の分だけ原文で確かめる。確かめる順は、実在、書誌、引用、主張の裏づけの 4 つである。誤りの形は <!-- link:begin checking-citations#error-types -->[引用や出典の確かめ方 › よくある誤りの形](../verify/checking-citations.md#error-types)<!-- link:end -->、リサーチのレポートでの確かめ方は <!-- link:begin using-research#checking-sources -->[リサーチを使いこなす › 出典の確かめ方](../app/using-research.md#checking-sources)<!-- link:end --> にある。調べものの場面では、次を足す。

- **主張ごとに原文の引用を付けさせる**：言い換えでなく、原文の文を一字も変えずに写させる。引用があれば、原文を検索して照合できる。頼み方は <!-- link:begin fact-checking#quotes -->[事実を確かめる（引用・照合・best-of-N） › 主張ごとに引用させる](../verify/fact-checking.md#quotes)<!-- link:end --> にある。
- **書かれていることと推測を、表の列で分ける**：「禁じる」と頼むだけではお願いにとどまる。引用の列があれば、照合できる形になる。次の雛形で、条件・限定の列と数値の写し方も指定する。
- **要約は原文より強い言い方になりやすい**：条件や限定が落ちて、主張の範囲が広がる。「正確に」と頼んでも直らないことがあるので、条件の列で原文と照らす。理由は <!-- link:begin summary-overgeneralization#what-happens -->[要約は原文より強く言いがち（過度な一般化） › 何が起きるか](../basics/summary-overgeneralization.md#what-happens)<!-- link:end --> にある。
- **最重要の主張は、原文を自分で読む**：結論を左右する 1〜2 件は、表を信じずに原文を読む。読んだ内容は自分で要約し、Claude には誤読の指摘を頼む方法がある（<!-- link:begin read-specs-yourself#misreading-detector -->[仕様を自分で読み、AI に誤読を指摘させる › AI に誤読を指摘させる](read-specs-yourself.md#misreading-detector)<!-- link:end -->）。
- **一致を証拠にしない**：別のモデルや同じモデルの再実行が同じ結論を出しても、原文の確認にはならない。<!-- link:begin second-opinion-from-another-model#agreement -->別のモデルに第二の意見を求める（一致は証拠にならない） › 一致は証拠にならない（準備中）<!-- link:end --> を参照する。

<!-- gen:begin snippet research-and-reports/facts-vs-inference -->
<!-- textlint-disable -->

??? example "雛形：書かれていることと推測を分け、原文の引用を添えて表にさせる依頼"

    ```text
    渡した資料（または、いま挙げた出典）の内容を、次の列の表にしてください。

    | 資料 | 主張 | 原文に書かれていること / 推測 | 主張が成り立つ条件・限定 | 原文の該当箇所（そのままの引用） |

    - 「原文に書かれていること / 推測」の列には、原文にあるなら「原文」、あなたが補ったなら「推測」と書く
    - 条件・限定の列には、原文が主張に付けている条件（対象・期間・前提）を書く。原文に条件がなければ「記載なし」と書く
    - 原文にない一般化はしない。複数の資料をまとめるときも、資料ごとの行を残す
    - 数値は原文どおりに写す。丸めたり単位を変えたりしない
    - 引用は原文の一字も変えずに写す。言い換えたものは引用の列に入れず、「言い換え」と書く
    - 該当箇所が見つからない主張は、行を消さずに「引用なし」と書く
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet research-and-reports/facts-vs-inference -->

雛形の表が返ってきたら、「推測」の行と「引用なし」の行を先に見る。そこが、レポートの中で原文の裏がない部分である。重要な事実ほど、一次の資料で裏を取る。全体の確かめ方は <!-- link:begin fact-checking#overall-check -->[事実を確かめる（引用・照合・best-of-N） › 全体の確かめ方](../verify/fact-checking.md#overall-check)<!-- link:end --> にある。

## うまくいかないとき {#when-it-fails}

症状ごとに、持ち主のページへ進む。

- **出典を開くと、書かれていないことが書いてある**：存在しない出典か、実在する文献の細部の誤りかを切り分ける。<!-- link:begin plausible-falsehoods#diagnosis -->[もっともらしい嘘・出典の誤り › 原因を安く確かめる順](../symptoms/plausible-falsehoods.md#diagnosis)<!-- link:end --> に原因を安く確かめる順がある。引用・照合の手は <!-- link:begin fact-checking#when-it-fails -->[事実を確かめる（引用・照合・best-of-N） › うまくいかないとき](../verify/fact-checking.md#when-it-fails)<!-- link:end --> にある。
- **古い情報が混ざっている**：最近の出来事や新しい版を間違えている。<!-- link:begin doesnt-know-latest#diagnosis -->[最新の情報を知らない › 原因を安く確かめる順](../symptoms/doesnt-know-latest.md#diagnosis)<!-- link:end --> で、検索・公式の資料・日付のどれで補うかを決める。
- **要約が原文より断定的になっている**：<!-- link:begin summary-overgeneralization#what-helps -->[要約は原文より強く言いがち（過度な一般化） › 何に効くか](../basics/summary-overgeneralization.md#what-helps)<!-- link:end --> の手に戻り、条件の列で照らし直す。
- **リサーチが起動しない、範囲が広すぎる**：<!-- link:begin using-research#requesting -->[リサーチを使いこなす › 頼み方（範囲・出典の条件・出力の形）](../app/using-research.md#requesting)<!-- link:end --> で頼み方を見直し、問いと範囲を絞って出し直す。
- **調査で本筋の会話が埋まる**：出力の多い調査は、別の文脈に任せる。費用の注意は <!-- link:begin research-in-subagents#cost -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 費用と使いすぎ](../context/research-in-subagents.md#cost)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- [引用や出典の確かめ方](../verify/checking-citations.md)

**関連**

- [リサーチを使いこなす](../app/using-research.md)
- [アーティファクト（会話の中で作る文書・スライド・デザイン）](../app/artifacts-overview.md)
- [プロジェクトの使いどころ](../app/using-projects.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)
- [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)
- [最新の情報を知らない](../symptoms/doesnt-know-latest.md)
- [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)
- [仕様を自分で読み、AI に誤読を指摘させる](read-specs-yourself.md)
- [ドキュメント・技術文書を書く](write-docs.md)
- [資料・スライドを作る](make-slides.md)
- [日本語の資料を読ませる・書かせる](../japanese/documents-in-japanese.md)
- 別のモデルに第二の意見を求める（一致は証拠にならない）（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use research on Claude](https://support.claude.com/en/articles/11088861-use-research-on-claude)：Anthropic・英語・確認日 2026-11-04
- [Enable and use web search](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)：Anthropic・英語・確認日 2026-11-04
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)：Anthropic・英語・確認日 2026-11-04
- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)：Anthropic・英語・確認日 2026-11-04
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
