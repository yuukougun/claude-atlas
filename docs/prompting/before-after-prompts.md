---
id: before-after-prompts
title: Before/After プロンプト集
aliases: [プロンプトの書き換え例, Instead of / Try, 頼み方の例文集]
type: recipe
field: prompting
chapter: 型と例文
order: 210
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる, 確かめる]
prevents: [見えていない]
scenes: [開発, 文章, 調べもの, データ分析]
summary: よくある依頼の書き換え前と後を比べて、自分の依頼に足りないもの（具体性・理由・範囲と完了・確かめる手段）を見つけられる。同じ書き換えを、アプリ・Claude Code・API のタブで比べられる。
signs:
  - {type: goal, text: 良い頼み方の具体例を見たい}
  - {type: goal, text: 自分の依頼のどこが足りないか、例と比べて知りたい}
prerequisites: [four-specifics]
related: [brief-a-new-colleague, give-reasons, show-examples, say-what-you-want, suggest-or-do, state-the-scope, long-context-first, verification-ladder#verbal-checks, prompt-patterns, fix-a-bug, measure-changes]
sources: [cc-docs-best-practices, api-docs-prompting-best-practices]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 書き換えの手順, anchor: procedure}
  - {title: 具体性を足す, anchor: specifics}
  - {title: 理由を足す, anchor: reasons}
  - {title: 範囲と完了を足す, anchor: scope-and-done}
  - {title: 確かめる手段を足す, anchor: verification}
  - {title: 面ごとの書き換え, anchor: by-surface}
  - {title: 書き換えの効きを確かめる, anchor: check}
  - {title: 書き換えても直らないとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：よくある依頼の書き換え前と後を比べて、自分の依頼に足りないもの（具体性・理由・範囲と完了・確かめる手段）を見つけられる。
    - **いつ引くか**：良い頼み方の具体例を見たいとき。自分の依頼のどこが足りないかを、例と比べて知りたいとき。
    - **前提**：<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end -->

<!-- textlint-disable -->
別名：プロンプトの書き換え例・Instead of / Try・頼み方の例文集
<!-- textlint-enable -->

Before/After プロンプト集は、同じ依頼を書き換え前と書き換え後で並べ、何を足したかと、足すと防げるずれを注記した例文集である。依頼に書かれていない情報は Claude に見えないので、足りないものを見つける手がかりは、書き換え前と後の差になる。公式の Claude Code の [Best practices](https://code.claude.com/docs/en/best-practices) にも、曖昧な依頼を具体的な依頼に書き換える「Instead of / Try」の対比表がある。このページは、足すものを 4 種類（具体性・理由・範囲と完了・確かめる手段）に分けて、開発・文章・調べもの・データ分析の例で見せる。

## 先に整える守り {#guards}

先に整える守りとは、書き換えを始める前の準備として、書き換えで防げることと防げないことを分けておくことである。書き換えた依頼は、Claude が読んで判断する「お願い」の質を上げるだけで、必ず守らせる鍵にはならない。

- 例外を許さない禁止は、依頼に言葉を重ねず、権限やフックで止める。分け方は <!-- link:begin say-what-you-want#two-layers -->[否定形ではなく、望む形で書く › 例外のない禁止は仕組みへ（二層）](say-what-you-want.md#two-layers)<!-- link:end --> と <!-- link:begin state-the-scope#two-layers -->[範囲を伝える（やらないこと） › 例外を許さない範囲は仕組みで縛る（二層）](state-the-scope.md#two-layers)<!-- link:end --> にある。
- 任せる幅を広げる書き換え（範囲を広く取る、完了まで一人で進めさせる）は、確かめる手段を先に渡す。手段の選び方は <!-- link:begin verification-ladder#verbal-checks -->[検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)<!-- link:end --> にある。確かめる手段のない広い依頼は、間違いに気づく場所がない。
- 依頼が Claude に通じるかは、書いた本人には分かりにくい。文脈を知らない同僚に読ませる確かめ方は <!-- link:begin brief-a-new-colleague#colleague-test -->[新人の同僚に頼むつもりで › 文脈のない同僚に見せて確かめる](brief-a-new-colleague.md#colleague-test)<!-- link:end --> にある。

## 書き換えの手順 {#procedure}

書き換えの手順とは、自分の依頼を Before として取っておき、4 種類の足しものを順に問い、足した結果を比べる流れである。各段に、終わったと言える印を付けた。

1. 送る前（または、ずれた返答を受け取った後）の依頼を、そのまま残す。印：書き換え前の依頼が手元にある。
2. 下の表の 4 種類を順に問い、書かれていないものを書き出す。印：足りないものが 1 行ずつ並ぶ。<!-- link:begin four-specifics#which-to-add -->[具体性の 4 点（対象・状況・完了・手本） › ずれ方から、次に足す点を探す](four-specifics.md#which-to-add)<!-- link:end --> は、返答のずれ方から次に足す点を探す。
3. 足した依頼を新しいセッションで送り、元の依頼の結果と並べる。印：どの足しものがどのずれを減らしたかを、1 つずつ言える。
4. 効いた足しものは、自分の雛形か CLAUDE.md に移す。印：次の依頼で最初から書いてある。

<!-- gen:begin snippet before-after-prompts/audit-my-request -->
<!-- textlint-disable -->

??? example "雛形：送る前の依頼文を 4 つの観点で点検させる依頼"

    ```markdown
    次の依頼文を、送る前に点検してほしい。書き直さずに、足りないものを指摘するだけにする。

    点検の観点は 4 つ：
    1. 具体性：対象（どのファイル・どの資料）、状況（症状・読む人・背景）、完了の形、倣う手本のうち、書かれていないもの
    2. 理由：規則や制約のうち、理由が書かれていないために、書いていない場面へ応用できないもの
    3. 範囲と完了：やらないこと、触ってよい範囲、終わったと言える条件のうち、書かれていないもの
    4. 確かめる手段：「確認して」とだけ書かれていて、実際に確かめる手段（流すコマンド・照合する元データ・引用する原文）が渡されていないもの

    観点ごとに「足りないもの」と「足すと防げるずれ」を 1 行ずつ書く。足りないものがない観点は「なし」と書く。
    私に聞かないと分からないことは、推測で埋めずに、最後に質問として並べる。

    --- 点検する依頼文 ---
    <ここに、送る前の依頼文を貼る>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet before-after-prompts/audit-my-request -->

2 の書き出しは、Claude に頼んでもよい。点検だけを頼み、書き直しは頼まない。書き直しまで頼むと、足りない所を Claude の推測で埋めた依頼になり、元の意図とずれる。

| 足すもの | 防ぐこと | 詳しくは |
|---|---|---|
| 具体性 | 対象・状況・完了・手本が見えず、Claude が推測で埋める | <!-- link:begin four-specifics#before-after -->[具体性の 4 点（対象・状況・完了・手本） › 同じ依頼を 4 点で書き直す](four-specifics.md#before-after)<!-- link:end --> |
| 理由 | 書いていない場面へ、規則を応用できない | <!-- link:begin give-reasons#what-changes -->[理由を添える › 理由を添えると何が変わるか](give-reasons.md#what-changes)<!-- link:end --> |
| 範囲と完了 | 頼んでいない変更が増える。どこで終わりか分からない | <!-- link:begin state-the-scope#anti-goals -->[範囲を伝える（やらないこと） › やらないことを書く](state-the-scope.md#anti-goals)<!-- link:end --> |
| 確かめる手段 | 「念のため確認した」と言葉だけで終わる | <!-- link:begin verification-ladder#verbal-checks -->[検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)<!-- link:end --> |

!!! example "判断例：理由を足すか、範囲を足すか"
    - **状況**：「ログイン周りを直して」と頼んだら、直したい箇所に加えて、無関係なファイルの整形が差分に混ざった。
    - **迷う候補**：なぜ差分を小さくしたいかの理由を足す。触ってよいファイルと、触らないものを足す。
    - **選んだもの**：先に範囲を足し、触らない理由は 1 文だけ添えた。
    - **理由**：ずれの形が「頼んでいない変更が増えた」なので、足りないのは境目である。理由は、境目の近くで判断が分かれる場面に効くので、範囲を書いた後に 1 文足せば足りる。

## 具体性を足す {#specifics}

具体性を足すとは、依頼に対象・状況・完了の形・倣う手本のうち、書かれていないものを足すことである。Claude は会話の外にあるコードや読む人を知らないので、書かれていない点は推測で埋める。防ぐ原因は、Claude に見えていないことである。

開発の例を見る。

```text
Before
ログインのバグを直して。

After
しばらく放置してセッションが切れたあとにログインすると、「トークンが無効です」と出て失敗する。
`src/auth/` のトークン更新の処理を見てほしい。
先に、この症状を再現する失敗テストを書き、そのテストが通るように直す。
テストの書き方は、既存の `tests/auth/login.test.ts` に合わせる。
```

After で足したものは 4 つある。状況（放置後に失敗する症状）、対象（`src/auth/` のトークン更新）、完了の形（失敗テストが通る）、手本（既存のテスト）である。Before の「バグ」は、Claude から見ると、どのバグかが決まらない。

文章の例を見る。

```text
Before
この障害報告を要約して。

After
添付の障害報告を、経営会議で読む 1 段落に要約してほしい。読む人は技術に詳しくない。
原因は専門用語を使わずに書き、影響の範囲と再発防止の担当を落とさない。
長さと口調は、前回の月次報告の要約（下に貼る）に合わせる。
```

足したものは、読む人（状況）、落とさない項目（完了の形）、前回の要約（手本）である。手本の選び方は <!-- link:begin show-examples#choose -->[例を見せる › 典型的で多様な例を選ぶ](show-examples.md#choose)<!-- link:end --> にある。

## 理由を足す {#reasons}

理由を足すとは、規則や制約に、なぜそうしたいかを 1 文で添えることである。理由があると、Claude は書いていない近い場面にも、同じ意図を当てはめられる。防ぐ原因は、規則の背後の意図が見えていないことである。

データ分析の例を見る。

```text
Before
外れ値は除いて集計して。

After
外れ値は除いて集計して。ここでの外れ値は、計測器の故障で入った 0 や極端に大きい値のことである。
実際に起きた大口の注文は、売上の実態を表すので除かない。
除くかどうか迷う行は、除かずに一覧にして最後に見せてほしい。
```

After で足したものは、外れ値の定義、大口の注文を残す理由、迷う行の扱いである。「外れ値」の一語は、統計の慣習どおりに読まれることがある。理由を書くと、書いていない種類の行にも判断が応用できる。

文章の例を見る。

```text
Before
専門用語を使わないで書いて。

After
読む人は営業部の担当者で、製品の仕様書を読んだことがない。
そのため、専門用語は使わずに書き、どうしても必要な語には、初めて出るときに一言の説明を添えてほしい。
```

禁止だけを書いた Before は、どの語が専門用語かの判断を Claude に任せている。After は読む人を書いたので、書いていない語の扱いも決められる。理由の書き方と効かない場面は <!-- link:begin give-reasons#limits -->[理由を添える › 効かない場面とやりすぎ](give-reasons.md#limits)<!-- link:end --> にある。

## 範囲と完了を足す {#scope-and-done}

範囲と完了を足すとは、やらないこと、触ってよい範囲、終わったと言える条件を依頼に書くことである。防ぐ原因は、境目と終わりが Claude に見えていないことである。範囲を広げる書き換えほど、確かめる手段（このページの「確かめる手段を足す」の節）とセットで足す。

開発の例を見る。

```text
Before
この関数をリファクタして。

After
`src/billing/invoice.ts` の `calcTotal` だけを整理してほしい。条件分岐が深いので、読みやすく分けたい。
やらないこと：戻り値の形を変えない。他のファイルを触らない。新しい依存を足さない。
気づいたことは直さずに、返答の最後へ書く。
終わりの条件：既存のテストがすべて通り、`calcTotal` を呼ぶ側の変更が要らないこと。
```

After で足したものは、範囲（1 つの関数）、やらないこと、気づいたことの置き場所、完了の条件である。書き方の詳細は <!-- link:begin state-the-scope#anti-goals -->[範囲を伝える（やらないこと） › やらないことを書く](state-the-scope.md#anti-goals)<!-- link:end --> にある。

調べものの例を見る。

```text
Before
このライブラリの移行について調べて。

After
公式の移行ガイドと変更履歴だけを根拠に、v2 から v3 へ上げるときに壊れる可能性のある箇所を一覧にしてほしい。
コードは書き換えない。
各項目に、根拠にした記述の原文を引用する。原文から言えないことは「不明」と書く。
```

足したものは、根拠にする資料の範囲、やらないこと（書き換え）、完了の形（引用つきの一覧）、不明のときの扱いである。提案で止めるか実行までさせるかは動詞で分ける（<!-- link:begin suggest-or-do#verbs -->[提案してほしいのか、実行してほしいのか › 提案と実行を動詞で分ける](suggest-or-do.md#verbs)<!-- link:end -->）。

## 確かめる手段を足す {#verification}

確かめる手段を足すとは、「確認して」と書く代わりに、流すコマンド、照合する元データ、引用する原文のような、確かめの方法そのものを渡すことである。言葉で確認を求めても、確認の中身は Claude の判断に任される。防ぐ原因は、結果が正しいかどうかを確かめる手段が Claude に見えていないことである。

開発の例を見る。

```text
Before
修正したら、念のため確認しておいて。

After
修正したら、`npm test -- tests/auth` を流して、結果をそのまま貼ってほしい。
失敗が残る間は、完了と書かない。失敗したテストの名前と、原因の仮説を書く。
流せなかったときは、流せなかったと書く。
```

After で足したものは、流すコマンド、結果をそのまま貼ること、完了と言える条件、確かめられなかったときの書き方である。「念のため」の言葉を足すより、手段を渡すほうが効く、という整理は <!-- link:begin verification-ladder#verbal-checks -->[検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)<!-- link:end --> にある。

データ分析の例を見る。

```text
Before
集計が合っているか確認して。

After
集計したあと、元の CSV の行数と、集計後の各グループの行数の合計を、別のコードで数えて並べてほしい。
一致しないときは、差になった行を 5 件示す。
```

足したものは、照合する相手（元の CSV）、照合の方法（行数の突き合わせ）、不一致のときの出し方である。集計した同じ方法で確かめ直すと、同じ見落としを繰り返すことがあるので、別の数え方を渡す。

## 面ごとの書き換え {#by-surface}

面ごとの書き換えとは、同じ「確かめる手段を足す」書き換えを、アプリ・Claude Code・API のそれぞれで、どこに何を書くかの違いとして比べることである。依頼の中身は同じで、手段の置き場所が面で変わる。面に固有の詳しい手順は、各面の分野のページに譲る。

=== "アプリ"

    Claude は、手元のリポジトリを読めるとは限らない。対象のコードと、失敗の出力を、依頼に貼る。確かめる手段は、あなたが流して結果を貼り直す形で書く。

    ```text
    下のコードと失敗の出力を貼る。直したコードを返すとき、直したことで通るはずのテストの名前も書いてほしい。
    私が `npm test` を流して結果を貼る。失敗が残っていたら、その出力から原因を絞り直してほしい。
    ```

    アプリで Claude が自分でコードを実行できるかは、このページでは確かめていない。

=== "Claude Code"

    Claude がリポジトリを読み、コマンドも流せる。対象はパスで書き、確かめる手段は流すコマンドで書く。

    ```text
    `src/auth/` のトークン更新を直してほしい。
    直したら `npm test -- tests/auth` を流して、結果をそのまま貼る。失敗が残る間は完了と書かない。
    ```

    例外を許さない確認（たとえば、テストが通るまで終了させない）は、依頼ではなくフックで止める。

=== "API"

    Claude が見るのは、リクエストに入れたものだけである。長い資料は先頭に置き、質問と指示は最後に置く（<!-- link:begin long-context-first#order -->[長い資料は先、質問は最後 › 資料を先、質問を最後に置く](long-context-first.md#order)<!-- link:end -->）。確かめる手段は、呼び出し側のコードに置く。

    ```text
    <documents> … 資料 … </documents>
    上の資料だけを根拠に答える。各主張に、根拠にした箇所の原文を引用する。
    引用できない主張は、answer ではなく unknown の欄に入れる。
    出力は、キー answer と unknown を持つ JSON だけにする。
    ```

    呼び出し側のコードで、JSON が読めること、引用が資料に実在することを検査する。検査に落ちた回答は使わない。

## 書き換えの効きを確かめる {#check}

書き換えの効きを確かめるとは、足した依頼が実際にずれを減らしたかを、元の依頼と比べて見ることである。1 回の返答の良し悪しでは決めない。

- 足したものを 1 つずつ戻して、どれが効いたかを言えるか。全部まとめて足した場合、効いていない足しものが混ざる。
- 同じ依頼を数回送って、返答のばらつきを見る。数回の観察は傾向を言うには足りないので、「そう見えた」と書き留める。
- 依頼を CLAUDE.md やスキルに移すときは、小さな eval で前後を比べる。方法は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> にある。
- 足しすぎていないか。4 つ全部を足しても、依頼が長くなるだけで効かないことがある。やりすぎは <!-- link:begin four-specifics#limits -->[具体性の 4 点（対象・状況・完了・手本） › 効かない場面とやりすぎ](four-specifics.md#limits)<!-- link:end --> にある。

雛形は、4 種類の足しものを欄にした枠である。要る欄だけ埋め、要らない欄は消す。

<!-- gen:begin snippet before-after-prompts/rewrite-frame -->
<!-- textlint-disable -->

??? example "雛形：4 つの足しものを欄にした書き換えの枠"

    ```markdown
    【やりたいこと】<目的を 1 文で。何のために、誰が使うのか>

    【対象】<ファイルのパス・資料の名前・画面の名前>
    【状況】<症状と再現の手順、または読む人と背景>
    【手本】<倣う既存のコード・文章。なければ「なし」>

    【理由】<制約や好みには、なぜそうしたいかを 1 文で添える>

    【やること】
    - <やることを動詞で。調べるだけか、直すところまでかを分ける>

    【やらないこと・触ってよい範囲】
    - <触ってよいファイルや範囲>
    - <触らないもの・足さないもの。気づいたことは直さずに最後へ書く、と頼む>

    【完了】<何が起きれば終わりか。例：このテストが通る>
    【確かめる手段】<流すコマンド、照合する元データ、引用する原文>
    【終わったら】<結果をそのまま貼る。確かめられなかった所は、確かめていないと書く>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet before-after-prompts/rewrite-frame -->

## 書き換えても直らないとき {#when-it-fails}

書き換えても直らないときは、返答のずれ方から、次に足すものか、別のページの方法を選ぶ。

- 何を足せばよいか分からない：<!-- link:begin four-specifics#which-to-add -->[具体性の 4 点（対象・状況・完了・手本） › ずれ方から、次に足す点を探す](four-specifics.md#which-to-add)<!-- link:end --> で、ずれ方から探す。
- 禁止を並べても守られない：禁止を望む形へ直す。それでも例外が出て困るなら、仕組みで止める（<!-- link:begin say-what-you-want#rewrite -->[否定形ではなく、望む形で書く › 禁止を望む形に書き換える](say-what-you-want.md#rewrite)<!-- link:end -->）。
- 提案だけで止まる、または頼んでいない書き換えが起きる：動詞を書き分ける（<!-- link:begin suggest-or-do#verbs -->[提案してほしいのか、実行してほしいのか › 提案と実行を動詞で分ける](suggest-or-do.md#verbs)<!-- link:end -->）。
- 長い資料の読み違いが多い：資料を先頭に置き、引用を抜かせる（<!-- link:begin long-context-first#quote-first -->[長い資料は先、質問は最後 › 答えの前に引用を抜かせる](long-context-first.md#quote-first)<!-- link:end -->）。
- バグが直らない：再現と完了を渡して仮説から進める（<!-- link:begin fix-a-bug#flow -->[バグを直す › 進める順番と、各段の終わりの印](../recipes/fix-a-bug.md#flow)<!-- link:end -->）。
- 同じ種類の依頼を毎回書く：項目を型にして使い回す（<!-- link:begin prompt-patterns#research -->用途別プロンプトの型 › 調査と要約の型（準備中）<!-- link:end -->）。

関連する原理は、<!-- link:begin brief-a-new-colleague -->[新人の同僚に頼むつもりで](brief-a-new-colleague.md)<!-- link:end -->、<!-- link:begin give-reasons -->[理由を添える](give-reasons.md)<!-- link:end -->、<!-- link:begin show-examples -->[例を見せる](show-examples.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)

**関連**

- [新人の同僚に頼むつもりで](brief-a-new-colleague.md)
- [理由を添える](give-reasons.md)
- [例を見せる](show-examples.md)
- [否定形ではなく、望む形で書く](say-what-you-want.md)
- [提案してほしいのか、実行してほしいのか](suggest-or-do.md)
- [範囲を伝える（やらないこと）](state-the-scope.md)
- [長い資料は先、質問は最後](long-context-first.md)
- [検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)
- 用途別プロンプトの型（準備中）
- [バグを直す](../recipes/fix-a-bug.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
