---
id: knowledge-cutoff
title: 知識カットオフと「今」を知らない問題
aliases: [knowledge cutoff, 学習データの期限, 今日の日付を知らない]
type: concept
field: basics
chapter: 答えの確かさ
order: 120
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない]
scenes: [調べもの, 開発]
summary: モデルの知識はある時点で止まり、今日の日付も知らないので、最近の出来事や新しい版について誤ることが分かる。日付と検索結果と最新の資料を渡す理由になる。
signs:
  - {type: goal, text: Claude が最近の出来事や今日の日付を知らない理由を知りたい}
prerequisites: []
related: [doesnt-know-latest, why-hallucinations, search-research-thinking, uses-nonexistent-apis, dating-information, current-models]
tracks: [web-search]
sources: [hc-up-date-training-data, api-docs-models-overview, hc-web-search-extended-thinking, api-docs-prompting-claude-haiku-5-5, api-docs-prompting-claude-fable-5-1, api-docs-prompting-claude-sonnet-5-5]
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: なぜ知らないのか, anchor: why}
  - {title: 何に効くか, anchor: what-helps}
  - {title: よくある誤解, anchor: misconceptions}
volatility: 中
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：モデルの知識は学習データのある時点で止まり、今日の日付も会話で渡されない限り分からない。だから最近の出来事や新しい版については、知らないか古い内容で答える。
    - **いつ引くか**：Claude が最近の出来事や今日の日付を知らない理由を知りたいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：knowledge cutoff・学習データの期限・今日の日付を知らない
<!-- textlint-enable -->

知識カットオフとは、モデルが学習に使ったデータの終わりの時点のことである。モデルはそれより後に起きたことを、学習では見ていない。このページは、その止まった知識と「今日がいつか」の 2 つが、答えにどう響くかを説明する。

## 何が起きるか {#what-happens}

知識が止まった時点より後のことを聞くと、答えは次の 3 つのどれかになる。

- 知らないと言う。
- 止まった時点の古い内容を、今のこととして答える。
- 名前だけ知っているものについて、中身を推測で埋める。

たとえば、あるライブラリの最新の版について聞くとする。モデルが知っているのは、学習データにあった版までである。それより新しい版が出ていても、モデルの側には何も見えていない。古い版の使い方を、そのまま今の方法として返すことがある。

日付も同じである。「今日は何日か」「あと何日で期限か」と聞くと、モデルは自分の知識から日付を推し量るしかない。会話の中に日付がなければ、止まった時点の近くを「今」だと思い込んだ計算になる。

!!! example "判断例：期限までの日数を聞く"
    - **状況**：「来月末のリリースまであと何日か」を Claude に数えさせたい。
    - **迷う候補**：そのまま聞く。または、今日の日付を添えて聞く。
    - **選んだもの**：今日の日付を添えて聞く。
    - **理由**：モデルは今日の日付を持っていない。日付がなければ、数え方が正しくても、起点が違う答えになる。

最近の出来事や新しい版で間違えたときの切り分けと対処は、<!-- link:begin doesnt-know-latest#diagnosis -->[最新の情報を知らない › 原因を安く確かめる順](../symptoms/doesnt-know-latest.md#diagnosis)<!-- link:end --> にある。

## なぜ知らないのか {#why}

理由は 2 つある。

1. **学習には終わりの時点がある。** モデルは、ある時点までに集めたデータで学習し、その後は知識が増えない。モデルを使い始めた後で世の中が動いても、モデルの中身は変わらない。
2. **日付はモデルの外にある情報である。** 今日が何日かは、学習データのどこにも書かれていない。会話に日付が入っていなければ、モデルには見えない。

公式は、知識の終わりを 2 種類に分けて案内している。

| 種類 | 意味 |
| --- | --- |
| reliable knowledge cutoff | 知識がいちばん広く確かな時点。当てにできる範囲の目安になる |
| training data cutoff | 学習に使ったデータの終わりの時点 |

古いモデルでは、この 2 つの日付がずれることがあり、reliable のほうが前の日付になる。Help Center の一覧に並ぶ日付は training data cutoff に当たる。「どこまで当てにしてよいか」は reliable のほうで見るのが安全である。

日付の値は、モデルが替わるたびに変わる。このページには書かない。各モデルの日付は公式の Models overview に載っていて、モデルの選び方は <!-- link:begin current-models#lineup -->現行モデルの一覧と位置づけ › 系統ごとの位置づけ（表）（準備中）<!-- link:end --> にある。

知識が止まっていることと、止まった時点より前のことを正しく覚えていることは別である。止まった時点の手前でも、情報が少なかった話題は怪しい。この性質の背景は、別のページが説明している。分からなくても答えるほうが得になる訓練の話は <!-- link:begin why-hallucinations#guess-pays -->[ハルシネーションはなぜ起きるか › 分からなくても答えるほうが得になる訓練](why-hallucinations.md#guess-pays)<!-- link:end --> にある。

## 何に効くか {#what-helps}

使う原理は「見せる」で、防ぐ原因は「見えていない」（モデルに必要な情報が見えていない状態）である。モデルの知識は後から増やせないので、知らないことは会話の側で見せる。見せれば、モデルが推測で埋める余地が減る。見せるものは 3 つある。

| 見せるもの | 防ぐこと | 使う場面 |
| --- | --- | --- |
| 今日の日付 | 日付の計算や「最近」の判断が、止まった時点を起点にすること | 期限・経過日数・「最新の」を含む依頼 |
| 検索の結果 | 最近の出来事や変わりうる事実を、古い記憶で答えること | 料金・規約・新しい版・時事 |
| 最新の資料 | 新しい仕様や版の中身を、推測で埋めること | 新しいライブラリ・API の使い方 |

検索や調査の使い分けは <!-- link:begin search-research-thinking#comparison -->[web 検索・リサーチ・拡張思考の使い分け › 三つの使い分け](../app/search-research-thinking.md#comparison)<!-- link:end --> にある。公式の案内では、単純な事実の確認は web 検索、広い調べものは調査機能が向く。

面ごとの手段は次のとおりである。

=== "アプリ"

    web 検索を有効にしておくと、最新の情報が要る質問のときに Claude が検索して答える。最新の情報が要る依頼では、検索を使うよう頼むと確実である。日付が効く依頼は、日付を書いて頼む。

=== "Claude Code"

    新しい版の API や設定を扱うときは、公式の資料や変更履歴の該当部分を読ませてから書かせる。日付が効く作業は、依頼の中に日付を書く。この辞典では、Claude Code が日付を会話に渡しているかは確かめていない。

=== "API"

    公式のモデル別の指針には、次の勧めがある。どのモデルがどれを勧めているかは、指針の原文で確かめる。

    - 現在の日付をプロンプトで渡す。
    - 変わりうる詳細（料金・許可されていること）は、検索で確かめるよう指示する。
    - 名前を知っているだけでは現状を知っているとは限らないので、検索させる。

存在しない関数やパッケージを出されたときは、知識の古さが原因のことがある。切り分けは <!-- link:begin uses-nonexistent-apis#diagnosis -->[存在しない関数やパッケージを使う › 原因を安く確かめる順](../symptoms/uses-nonexistent-apis.md#diagnosis)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- **「新しいモデルなら最新のことも知っている」**：モデルが新しくても、知識は学習データの終わりで止まる。モデルを使う時点との間には、必ず空白がある。
- **「聞けば自分の期限を正確に答えられる」**：モデル自身の答えは推測を含む。正確な日付は、公式の一覧で確かめる。
- **「検索を有効にすれば、日付も分かる」**：検索の結果に日付が入るとは限らない。日付が効く依頼では、日付を書く。
- **「止まった時点より前のことなら、すべて正しい」**：情報が少なかった話題は、止まった時点より前でも怪しい。重要な結論は、出典で確かめる。
- **「ネットの記事のとおりに動かないのは、知識が古いせいだ」**：読んだ記事や設定のほうが古いこともある。助言の古さの見分け方は <!-- link:begin dating-information#layers -->いつの情報かを見分ける › 古くなる速さの三つの層（準備中）<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)：Anthropic・英語・確認日 2026-11-04
- [Models overview](https://platform.claude.com/docs/en/models/overview)：Anthropic・英語・確認日 2026-11-04
- [When should I use web search, extended thinking, and research?](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)
- [最新の情報を知らない](../symptoms/doesnt-know-latest.md)

**関連**

- [ハルシネーションはなぜ起きるか](why-hallucinations.md)
- いつの情報かを見分ける（準備中）
- 現行モデルの一覧と位置づけ（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
