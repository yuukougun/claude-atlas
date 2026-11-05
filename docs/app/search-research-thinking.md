---
id: search-research-thinking
title: web 検索・リサーチ・拡張思考の使い分け
aliases: [web search]
type: comparison
field: app
chapter: 調べる・作る
order: 80
level: 整える
priority: 必須
surfaces: [app]
principle: [見せる, 確かめる]
prevents: [見えていない, 合っていない]
scenes: [調べもの]
summary: web 検索・リサーチ・拡張思考を、最新の情報が要るか、どれだけ広く調べるかで使い分けられる。組み合わせたときに何が変わるかも分かる。
signs:
  - {type: goal, text: 最新の情報を踏まえて答えてほしい}
  - {type: goal, text: 検索より、じっくり考えて答えてほしい}
  - {type: goal, text: 調べものに、どこまで時間をかけさせるか決めたい}
prerequisites: [knowledge-cutoff]
related: [using-research, doesnt-know-latest, effort-levels#thinking-toggle, how-thinking-works, fact-checking, research-and-reports, what-uses-up-limits]
tracks: [web-search, research, effort]
outdated_advice: [cowork-separate-app]
sources: [hc-web-search-extended-thinking, hc-web-search, hc-research, hc-effort-settings, hc-cowork-and-chat]
volatility: 中
sections:
  - {title: 三つの使い分け, anchor: comparison}
  - {title: 選び方, anchor: choose}
  - {title: 組み合わせる, anchor: combine}
  - {title: 使えたかと合っているかの確かめ方, anchor: verify}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：最新の事実の確認なら web 検索、広く集めて出典付きでまとめるならリサーチ、最新の情報が要らない推論なら思考（thinking）と選べる。
    - **いつ引くか**：最新の情報を踏まえて答えてほしいとき、検索より考えて答えてほしいとき、調べものにかける時間を決めたいとき。
    - **前提**：<!-- link:begin knowledge-cutoff -->[知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)<!-- link:end -->

<!-- textlint-disable -->
別名：web search
<!-- textlint-enable -->

web 検索・リサーチ・思考は、どれも「答える前に何かをする」機能だが、していることが違う。このページは、アプリで 3 つのどれを使うかを決める基準と、組み合わせたときに変わることをまとめる。

## 三つの使い分け {#comparison}

web 検索は、役に立つときに検索して、答えに出典を付ける。リサーチは、前の検索結果をもとに次の検索を重ね、何を調べるかを Claude が自分で決めながら、web と接続済みのツールから集める。思考は、最新の情報を取りに行く機能ではなく、答える前に考える時間を取る設定である。古い呼び名は拡張思考（extended thinking）で、アプリでの切り替えは effort の側にある。

面・成熟度などの属性は、次の表にある。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 面 | 強制力 | 入った版 |
| --- | --- | --- | --- |
| [Web 検索（web search。アプリ）](search-research-thinking.md) | アプリ | — | 2025-03-20 |
| [リサーチ（Research）](using-research.md) | アプリ | お願い | 2025-04-15 |
| [effort](../models/effort-levels.md) | アプリ・Claude Code・API | なし | 2025-11-24 |

すべて共通：成熟度 GA、確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare -->

effort の行は Claude Code と API にも当たる。このページが扱うのはアプリでの使い分けで、effort の段階と既定は <!-- link:begin effort-levels#levels -->[effort の段階と使い分け › 段ごとの振る舞い](../models/effort-levels.md#levels)<!-- link:end --> と <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](../models/effort-levels.md#defaults-by-surface)<!-- link:end --> が持つ。

使い分けの分かれ目は 2 つである。

- **最新の情報が要るか**：要るなら web 検索とリサーチが候補で、要らないなら思考を選ぶ。モデルの知識は止まった時点までで、料金・規約・新しい版のような変わりうる事実は、検索で確かめるのが前提になる。検索を頼んでも古い答えが返るときの切り分けは <!-- link:begin doesnt-know-latest#diagnosis -->[最新の情報を知らない › 原因を安く確かめる順](../symptoms/doesnt-know-latest.md#diagnosis)<!-- link:end --> にある。
- **どれだけ広く調べるか**：1 つの事実を確かめるなら、少ない呼び出しで済む web 検索。複数の観点を集めて比べるなら、多くの呼び出しを数分かけて重ねるリサーチ。公式の使い分けの記事は、呼び出しの回数と所要時間の目安も挙げている。web 検索の目安は「<!-- fact:begin web-search-call-guide -->1〜2 回のツール呼び出しで答えられる単純な事実確認（2026-10-29 時点）<!-- fact:end -->」、リサーチの目安は「<!-- fact:begin research-call-guide -->5 回以上のツール呼び出しを 1〜3 分かけて行う包括的な情報収集（2026-10-29 時点）<!-- fact:end -->」である。数値は変わりうるので、参考に挙げた記事で確かめる。

広く調べるほど、時間と利用枠を使う。web 検索と、渡した URL を読む web fetch は枠を使い、長い記事を読み込むと大きく減る。何が枠を使っているかは <!-- link:begin what-uses-up-limits#causes -->[上限を早く使う要因 › 枠を早く減らす原因](../cost/what-uses-up-limits.md#causes)<!-- link:end --> で確かめる。

## 選び方 {#choose}

選ぶ前に、答えが「止まった時点より後の事実」に依存するか、1 つの事実で済むか複数の観点が要るかを見る。次の 3 つの判断例は、それぞれ別の分かれ目で決まる。

!!! example "判断例：今日時点の仕様を 1 つ確かめる"
    - **状況**：使っているツールの、今の設定項目が何かを 1 つだけ知りたい。
    - **迷う候補**：web 検索で確かめる。リサーチに頼んで出典付きで調べさせる。
    - **選んだもの**：web 検索。
    - **理由**：単純な事実確認は、少ない呼び出しで済む。リサーチは広く集める機能で、1 つの事実のために使うと時間と枠を余計に使う。

!!! example "判断例：設計案の比較を考えさせる"
    - **状況**：自分で用意した 3 つの設計案について、どれが後で破綻しにくいかを考えてほしい。最新の情報は要らない。
    - **迷う候補**：web 検索で類似の事例を探させる。思考を使って、案の中身を深く考えさせる。
    - **選んだもの**：思考。必要なら effort を上げる。
    - **理由**：公式の使い分けでは、最新情報が要らない複雑な推論は思考の役割である。考える深さの上げ下げと待ち時間の釣り合いは <!-- link:begin effort-levels#thinking-toggle -->[effort の段階と使い分け › thinking の切り替え](../models/effort-levels.md#thinking-toggle)<!-- link:end --> にある。

!!! example "判断例：競合の最近の動きをレポートにする"
    - **状況**：複数の競合の最近の動きを、出典付きの 1 本のレポートにまとめたい。
    - **迷う候補**：web 検索を何度も頼んで、自分でまとめる。リサーチに頼む。
    - **選んだもの**：リサーチ。観点の設計が結果を左右するなら、思考も足す。
    - **理由**：前の結果をもとに次の検索を重ねて集める作業は、リサーチの役割である。頼み方の型は <!-- link:begin using-research#requesting -->[リサーチを使いこなす › 頼み方（範囲・出典の条件・出力の形）](using-research.md#requesting)<!-- link:end --> にある。

## 組み合わせる {#combine}

3 つは排他ではなく、同じ会話で重ねられる。重ねたときの変わり方は、組によって違う。

- **思考とリサーチ**：公式の記事によると、計画を立ててから集めるので、より長く出典付きのレポートになる。変わるのは、集める前に計画が入ることと、レポートが長くなることである。長くなった分、読む手間と確かめる手間も増える。頼み方の雛形を次に置く。

<!-- gen:begin snippet search-research-thinking/research-with-plan -->
<!-- textlint-disable -->

??? example "雛形：リサーチに計画を先に出させ、事実と推測を分けさせる頼み方"

    ```markdown
    リサーチ機能を使って、次の問いを調べてください。

    問い：<知りたいこと。1 文で>
    範囲：<期間・地域・対象。範囲の外は含めない>

    調べる前に、どの観点で何を調べるかの計画を短く出してください。
    レポートでは、出典のある事実と、あなたの推測を分けて書いてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet search-research-thinking/research-with-plan -->

- **web 検索と思考**：検索で事実を集める段と、集めた事実から考える段を、別の依頼に分けると役割が見やすい。公式の記事にこの組の記述はなく、この辞典の提案である（推論・実践例なし）。
- **何をどちらに置くか**：事実の収集は web 検索かリサーチに、収集した事実の評価や選択は思考に置く。重要な結論の裏取りは、そのどちらにも任せず、<!-- link:begin fact-checking#overall-check -->[事実を確かめる（引用・照合・best-of-N） › 全体の確かめ方](../verify/fact-checking.md#overall-check)<!-- link:end --> で確かめる。

変わりうる事実を検索に任せたいときは、検索するよう頼みに書く。新しい体験では、検索するかどうかを Claude が自分で判断するので、頼みで背中を押すと、検索されやすくなる。

<!-- gen:begin snippet search-research-thinking/search-changeable-facts -->
<!-- textlint-disable -->

??? example "雛形：変わりうる事実を、検索で確かめてから答えさせる頼み方"

    ```markdown
    次の質問には、変わりうる事実（料金・規約・最新の版・最近の出来事）が含まれます。
    記憶で答えず、web 検索で確かめてから答えてください。

    質問：<知りたいこと>

    回答には、参照した出典の URL と、出典に書かれていた日付を付けてください。
    検索で確かめられなかった点は、確かめられなかったと書いてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet search-research-thinking/search-changeable-facts -->

!!! note "自分のアカウントがどちらの体験か"
    - **今の体験**：web 検索の切り替えはなく、要るときに Claude が検索する。リサーチは `/deep-research` か「+」から選ぶ。
    - **前の体験**：入力欄に「Chat」と「Cowork」の選択が残るアカウントは、まだ前のやり方のままである。web 検索を「+」のメニューから自分で有効にする。
    - **詳しくは**：<!-- link:begin outdated-advice-ledger#cowork-separate-app -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#cowork-separate-app)<!-- link:end --> に、変わった時期と見つけ方がある。

## 使えたかと合っているかの確かめ方 {#verify}

使い分けた後は、検索やリサーチが実際に使われたかと、結果が合っているかを見る。

- **検索したか**：web 検索を使った回答には出典が付く。最新の事実を述べているのに出典がない答えは、検索せずに記憶で答えた可能性がある（推論・実践例なし）。その場合は、検索するよう頼みに書いて聞き直す。
- **リサーチの結果**：レポートの出典は、原文を開いて確かめる。手順は <!-- link:begin using-research#checking-sources -->[リサーチを使いこなす › 出典の確かめ方](using-research.md#checking-sources)<!-- link:end --> と <!-- link:begin research-and-reports#check-sources -->[調べものとレポート › 出典を原文で確かめる](../recipes/research-and-reports.md#check-sources)<!-- link:end --> にある。
- **重要な結論**：<!-- link:begin fact-checking#sources-only -->[事実を確かめる（引用・照合・best-of-N） › 渡した資料の範囲で答えさせる](../verify/fact-checking.md#sources-only)<!-- link:end --> のように、渡した資料の範囲で答えさせる方法もある。重要な事実ほど、一次の資料で裏を取る。
- **使った量**：思い当たらないのに枠が減るときは、<!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> で内訳を見る。

思考の仕組みと、考えた分も出力として数えられる点は <!-- link:begin how-thinking-works -->[思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)<!-- link:end --> にある。調べもの全体の進め方は <!-- link:begin research-and-reports -->[調べものとレポート](../recipes/research-and-reports.md)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)

**次に読む**

- [リサーチを使いこなす](using-research.md)
- [調べものとレポート](../recipes/research-and-reports.md)

**関連**

- [最新の情報を知らない](../symptoms/doesnt-know-latest.md)
- [effort の段階と使い分け › thinking の切り替え](../models/effort-levels.md#thinking-toggle)
- [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [When should I use web search, extended thinking, and research?](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research)：Anthropic・英語・確認日 2026-11-04
- [Enable and use web search](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)：Anthropic・英語・確認日 2026-11-04
- [Use research on Claude](https://support.claude.com/en/articles/11088861-use-research-on-claude)：Anthropic・英語・確認日 2026-11-04
- [Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)：Anthropic・英語・確認日 2026-11-04
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
