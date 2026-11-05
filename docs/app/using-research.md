---
id: using-research
title: リサーチを使いこなす
aliases: [Research, Deep Research, /deep-research]
type: feature
field: app
chapter: 調べる・作る
order: 90
level: 整える
priority: 推奨
surfaces: [app]
principle: [確かめる, 見せる]
prevents: [見えていない, 確かめていない]
pitfalls: [預けすぎる]
scenes: [調べもの]
summary: リサーチに広く調べさせ、出典付きのレポートを受け取れる。起動しないときの頼み方と、出典を自分で確かめる手順が分かる。
signs:
  - {type: goal, text: 調査結果の出典を確かめたい}
  - {type: goal, text: 出典付きの調査レポートを作らせたい}
  - {type: symptom, text: 調べてと頼んでも、深く調べずに答えが返る}
prerequisites: [search-research-thinking]
related: [checking-citations, fact-checking, connectors-in-the-app, research-and-reports, plausible-falsehoods, over-reliance]
tracks: [research, connectors]
sources: [hc-research, claude-blog-research, claude-blog-integrations, hc-cowork-and-chat, hc-web-search-extended-thinking]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when-to-use}
  - {title: 頼み方（範囲・出典の条件・出力の形）, anchor: requesting}
  - {title: 出典の確かめ方, anchor: checking-sources}
  - {title: コネクタと組み合わせる, anchor: with-connectors}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
stage: reviewed
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：リサーチに広く調べさせ、出典付きのレポートを受け取れる。起動しないときの頼み方と、出典を確かめる手順もある。
    - **いつ引くか**：調査結果の出典を確かめたいとき。出典付きの調査レポートを作らせたいとき。調べてと頼んでも、深く調べずに答えが返るとき。
    - **強制力**：リサーチは調べる機能で、範囲や出典の条件は依頼に書く<!-- gen:begin feature research/enforcement -->お願い<!-- gen:end feature research/enforcement -->である。条件が守られたかは、受け取ったレポートで自分が確かめる。
    - **前提**：<!-- link:begin search-research-thinking -->[web 検索・リサーチ・拡張思考の使い分け](search-research-thinking.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Research・Deep Research・/deep-research
<!-- textlint-enable -->

リサーチ（Research）とは、前の検索結果をもとに次の検索を重ね、web と接続済みのツールから集めて、出典付きのレポートにする機能である。Help Center の日本語版は「調査機能」と訳す。広く任せる機能なので、頼む段階で範囲と出典の条件を決め、受け取った後で出典を自分で確かめる。この 2 つを一続きにして使うのが、このページの主題である。

## 使いどころ {#when-to-use}

使いどころとは、リサーチを選ぶ場面と、リサーチが防ぐ原因のことである。

防ぐ原因は 2 つある。1 つは、答えに要る資料が会話に見えていないこと。リサーチは web と、Gmail・Calendar・Google Docs などの接続済みのツールから資料を集め、会話に持ち込む。もう 1 つは、Claude が確かめていないこと。レポートに出典が付くので、主張を原文と照らす入口ができる。ただし、出典が付いただけでは、確かめたことにならない。照らす作業は人の側に残る。

選ぶ基準は、どれだけ広く調べるかである。公式の使い分けでは、リサーチの目安は「<!-- fact:begin research-call-guide -->5 回以上のツール呼び出しを 1〜3 分かけて行う包括的な情報収集（2026-10-29 時点）<!-- fact:end -->」である。1 つの事実の確認には重すぎる。数値は変わりうるので、参考に挙げた記事で確かめる。web 検索・思考との選び分けは <!-- link:begin search-research-thinking#choose -->[web 検索・リサーチ・拡張思考の使い分け › 選び方](search-research-thinking.md#choose)<!-- link:end --> にある。

リサーチに使われるモデルは、会話で選んでいるモデルとは別である。使うモデルの名前は変わるので、公式の記事で見る。

## 頼み方（範囲・出典の条件・出力の形） {#requesting}

頼み方とは、リサーチに渡す依頼の書き方である。広く任せるぶん、依頼の段階で守りを先に置く。範囲で調べる幅を絞り、出典の条件で後から確かめやすい形にし、出力の形でレポートを読みやすくする。

- **範囲**：問いを 1 文で書き、期間・地域・対象を決める。範囲の外は含めないと書く。
- **出典の条件**：優先する出典の種類（公式の文書、一次資料）、使わない種類、使ってよい言語を書く。主張ごとに出典の URL を付けさせ、見つからなかった点は見つからなかったと書かせる。
- **出力の形**：結論を先頭に置く。観点ごとに見出しを分ける。長さの上限を決める。出典のある事実と、Claude の推測を分けて書かせる。

3 つを埋める型は次の雛形にある。

<!-- gen:begin snippet using-research/research-request -->
<!-- textlint-disable -->

??? example "雛形：リサーチを頼む文の型（範囲・出典の条件・出力の形）"

    ```markdown
    リサーチのツールを使って、次の問いを調べてください。

    問い：<知りたいこと。1 文で>
    範囲：<期間・地域・対象。範囲の外は含めない>
    出典の条件：<公式の文書と一次資料を優先する。使わない種類の出典があれば書く。使ってよい言語も書く>
    出力の形：<結論を先頭に置く。観点ごとに見出しを分ける。長さの上限を書く>

    調べる前に、どの観点で何を調べるかの計画を短く出してください。
    レポートでは、すべての主張に出典の URL を付け、出典のある事実と、あなたの推測を分けて書いてください。
    出典が見つからなかった点は、見つからなかったと書いてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet using-research/research-request -->

計画を先に出させると、調べる観点がずれていないかを、集め始める前に直せる。思考と組み合わせたときに何が変わるかは <!-- link:begin search-research-thinking#combine -->[web 検索・リサーチ・拡張思考の使い分け › 組み合わせる](search-research-thinking.md#combine)<!-- link:end --> にある。

### 起動しないとき

調べてと頼んでも深く調べずに答えが返るのは、リサーチが起動せず、通常の返答や web 検索で答えているときに起きる。公式のコツは、リサーチを使うことを依頼に明示することである。英語の原文は次の形である。

> Claude, please use the research tool to…

日本語でも、「リサーチのツールを使って」と書けばよい。画面から選ぶ手もある。新しい Claude の体験では、`/deep-research` か「+」から選ぶ。

それでも起動しないときは、安い順に次を確かめる。

1. 画面でリサーチを選べているか。使えるプランと面は変わるので、公式の記事で確かめる。
2. web 検索を有効にしてあるか。リサーチには要る。Team と Enterprise では owner が組織で有効にする。
3. 問いが 1 つの事実の確認になっていないか。そうなら web 検索で足りる。

!!! example "判断例：「調べて」と頼んだのに数秒で答えが返った"
    - **状況**：業界の動向を複数の観点で比べたいと「調べて」と頼んだ。数秒で短い答えが返り、出典は付いていない。
    - **迷う候補**：質問を長く詳しく書き直して、もう一度頼む。または、リサーチのツールを使うことを明示して頼み直す。
    - **選んだもの**：リサーチを使うことを明示して頼み直し、範囲・出典の条件・出力の形を足す。
    - **理由**：長く書いても、リサーチが起動する保証にはならない。公式のコツは明示である。範囲などを足すのは、起動した後のレポートを確かめやすくするためである。

## 出典の確かめ方 {#checking-sources}

出典の確かめ方とは、レポートの主張が、挙げられた出典の原文に本当にあるかを、自分で確かめる手順である。リサーチのレポートも、AI が挙げる出典の 1 種である。実在しない出典や、実在しても細部の違う出典が混ざりうる点は、ほかの場合と変わらない。誤りの形は <!-- link:begin plausible-falsehoods#forms -->[もっともらしい嘘・出典の誤り › よくある形](../symptoms/plausible-falsehoods.md#forms)<!-- link:end --> と <!-- link:begin checking-citations#error-types -->[引用や出典の確かめ方 › よくある誤りの形](../verify/checking-citations.md#error-types)<!-- link:end --> にある。

確かめる手順は、安い順に並べる。

1. **主張と出典の対応表を作らせる**。出典のない主張を洗い出す。表の引用も Claude が書いたものなので、次の段で原文と照らす。依頼の型は次の雛形にある。
2. **出典を開く**。URL が開くか、題名・発行元・日付が表と合うかを見る。
3. **重要な主張だけ、原文の該当箇所を照らす**。数値・日付・固有名詞と、「すべて」「必ず」のような範囲の言い方が、原文のとおりかを見る。
4. **出典の種類を見る**。結論に効く主張は、公式の文書や一次資料で裏を取る。二次の解説だけが出典なら、その解説の出典へさかのぼる。
5. **出典のない主張は推測として扱う**。採るなら、別に調べさせるか、自分で調べる。

<!-- gen:begin snippet using-research/claims-table-request -->
<!-- textlint-disable -->

??? example "雛形：レポートの主張と出典の対応表を作らせる依頼"

    ```markdown
    上のレポートの主張を、1 つずつ表にしてください。

    列は次の 4 つにします。
    - 主張
    - 出典の URL
    - その出典の該当箇所の引用（原文のまま）
    - 出典の種類（公式の文書・一次資料・二次の解説・不明のどれか）

    出典のない主張と、原文を引用できない主張は、出典の列に「出典なし」と書いてください。
    引用は作り直さず、原文にあるものだけを書いてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet using-research/claims-table-request -->

手順の本体は <!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end --> にある。重要な結論の裏取りは <!-- link:begin fact-checking#overall-check -->[事実を確かめる（引用・照合・best-of-N） › 全体の確かめ方](../verify/fact-checking.md#overall-check)<!-- link:end -->、調べものの全体の進め方は <!-- link:begin research-and-reports#check-sources -->[調べものとレポート › 出典を原文で確かめる](../recipes/research-and-reports.md#check-sources)<!-- link:end --> を見る。ここでは繰り返さない。

日本語で頼んだときに、日本語の資料と英語の資料をどう拾うか、引用の質がどうかを検証した資料は、この辞典では見つけていない。出典の条件に使ってよい言語を書き、レポートの出典の言語を見て、偏りがないかを確かめる。

!!! example "判断例：出典付きのレポートを、どこまで原文で確かめるか"
    - **状況**：出典が 15 件付いたレポートを、社内の提案資料に使いたい。全部を原文で確かめる時間はない。
    - **迷う候補**：全部の出典を開いて、引用まで照らす。または、結論に効く主張だけを原文まで確かめる。
    - **選んだもの**：結論に効く主張と、数値や固有名詞を含む主張だけを原文まで照らす。残りは、出典が実在し、題名が合うところまでを見る。
    - **理由**：全部を照らす運用は続かない。ただし、提案資料に引用として載せる主張は、範囲を広げて原文まで照らす。手間を下げる考え方は <!-- link:begin over-reliance#cheap-verification -->[判断を預けすぎる（過度依存） › 確かめる手間を下げる](../judgment/over-reliance.md#cheap-verification)<!-- link:end --> にある。

## コネクタと組み合わせる {#with-connectors}

コネクタと組み合わせるとは、リサーチの調べる先に、メールやカレンダー、Google Docs などの接続済みのツールを加えることである。web に出ていない自分の資料を踏まえたレポートを作らせられる。

使うには、先にコネクタをつなぎ、そのチャットでオンにしておく。つなぎ方とチャットごとのオンは <!-- link:begin connectors-in-the-app#types -->[コネクタ（MCP）をアプリで使う › コネクタの種類](connectors-in-the-app.md#types)<!-- link:end --> にある。モバイルで始めたリサーチは、web だけを使い、コネクタを使わない。

依頼には、調べる先を書く。web だけか、社内の資料も含めるか、社内の資料だけかを決める。出典の条件には、社内の資料は資料名と場所を、web は URL を書かせると、確かめる場所が分かる。

社内の資料が出典に混ざると、確かめ方が少し変わる。社内の資料は、自分が原文を開ける。web の記事と社内の資料が食い違うときは、どちらを採るかを自分で決める。

!!! example "判断例：コネクタを全部つないだまま、リサーチを頼む"
    - **状況**：競合の動向を、自社の過去の提案資料も踏まえて整理させたい。コネクタはメール・カレンダー・ファイル置き場など、多くをつないである。
    - **迷う候補**：全部のコネクタをオンのまま頼む。または、使うファイル置き場のコネクタだけをオンにして頼む。
    - **選んだもの**：使うコネクタだけをオンにし、依頼に調べる先を書く。
    - **理由**：関係のないメールやカレンダーまで調べる先に入ると、レポートの焦点がぼやけ、私的な内容が混ざる余地も広がる。多くつないだときの読ませ方は <!-- link:begin connectors-in-the-app#on-demand -->[コネクタ（MCP）をアプリで使う › 使うときだけ読ませる（On demand）](connectors-in-the-app.md#on-demand)<!-- link:end --> にある。

つなぎ先の信頼の判断は、リサーチでも同じく必要である。メールや資料には外の人の文が入る。判断の考え方は <!-- link:begin connectors-in-the-app#trust -->[コネクタ（MCP）をアプリで使う › 信頼してよいか](connectors-in-the-app.md#trust)<!-- link:end --> にある。

## 効かない場面と落とし穴 {#limits}

効かない場面と落とし穴は、次のとおりである。

- **出典が付いていても、正しいとは限らない**。出典は確かめる入口である。確かめずに使うと、もっともらしい誤りをそのまま採ることになる。
- **預けすぎる**。レポートが整っているほど、そのまま使いたくなる。残す判断の選び方は <!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](../judgment/over-reliance.md#what-to-keep)<!-- link:end --> を見る。
- **1 つの事実の確認には重い**。数分かかる調べ方なので、単発の確認は web 検索で足りる。
- **条件は依頼に書くお願い**。出典の条件や範囲が守られたかは、レポートを見て確かめる。
- **日本語の質は確かめていない**。日本語の資料の拾い方と引用の質を検証した資料は、見つけていない。
- **面とプランで使える範囲が違う**。モバイルでは web だけを使い、ローカルの MCP は使えない。使えるプランは公式の記事で確かめる。

## 比べる相手 {#compare}

比べる相手は、同じ目的を別の手段で満たすものである。

- **web 検索**：1 つの事実の確認なら、web 検索のほうが少ない呼び出しで済む。違いは <!-- link:begin search-research-thinking#comparison -->[web 検索・リサーチ・拡張思考の使い分け › 三つの使い分け](search-research-thinking.md#comparison)<!-- link:end --> にある。
- **資料を自分で渡して答えさせる**：調べる範囲を自分で決めたいなら、集める作業を人が済ませ、渡した資料の範囲で答えさせる。やり方は <!-- link:begin fact-checking#sources-only -->[事実を確かめる（引用・照合・best-of-N） › 渡した資料の範囲で答えさせる](../verify/fact-checking.md#sources-only)<!-- link:end --> にある。
- **調べものの進め方全体**：問いと範囲の決め方から、レポートの確かめ方までは <!-- link:begin research-and-reports#steps -->[調べものとレポート › 調べものの進め方](../recipes/research-and-reports.md#steps)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use research on Claude](https://support.claude.com/en/articles/11088861-use-research-on-claude)：Anthropic・英語・確認日 2026-11-04
- [Claude takes research to new places](https://claude.com/resources/articles/research)：Anthropic・英語・確認日 2026-11-04
- [Claude can now connect to your world](https://claude.com/resources/articles/integrations)：Anthropic・英語・確認日 2026-11-04
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04
- [When should I use web search, extended thinking, and research?](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [web 検索・リサーチ・拡張思考の使い分け](search-research-thinking.md)

**関連**

- [引用や出典の確かめ方](../verify/checking-citations.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [コネクタ（MCP）をアプリで使う](connectors-in-the-app.md)
- [調べものとレポート](../recipes/research-and-reports.md)
- [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
