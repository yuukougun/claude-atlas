---
id: ask-for-options
title: 選択肢と推奨案を出させる
aliases: [複数案と推奨を出させる, 比べてから選ぶ, 自分の案を批評させる, 設計の壁打ち]
type: concept
field: prompting
chapter: 詰め方と頼み直し
order: 170
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [握る, 見せる]
prevents: [見えていない]
pitfalls: [同意を根拠にする, みんなの案になる]
scenes: [開発, 文章, 学習, コンテスト]
summary: 答えを選ぶ場面では、選択肢と推奨案と理由を出させてから人が決める。独自性が要る発想の場面では、先に自分の案を書き、AI には問いと反論を求める。
signs:
  - {type: goal, text: どの方針がよいか、比べてから決めたい}
  - {type: goal, text: 設計や技術の選び方を壁打ちしたい}
  - {type: symptom, text: 一つの案しか出てこず、ほかと比べられない}
prerequisites: [suggest-or-do]
related: [think-before-asking, ai-ideas-are-everyones, ask-without-sycophancy, agreement-is-not-evidence, sycophancy, let-claude-ask]
sources: []
volatility: 低
sections:
  - {title: 答えを選ぶ場面：選択肢と推奨案, anchor: choose}
  - {title: 発想の場面：先に自分の案、AI には問いと反論, anchor: ideate}
  - {title: 自分の案を批評させる, anchor: critique}
  - {title: なぜ効くか、何に効くか, anchor: why}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：答えを選ぶ場面で選択肢と推奨案と理由を出させる頼み方と、発想の場面で先に自分の案を書く順序が分かる。
    - **いつ引くか**：どの方針がよいか、比べてから決めたいとき。設計や技術の選び方を壁打ちしたいとき。案が 1 つしか出てこず、ほかと比べられないとき。
    - **前提**：<!-- link:begin suggest-or-do -->[提案してほしいのか、実行してほしいのか](suggest-or-do.md)<!-- link:end -->

<!-- textlint-disable -->
別名：複数案と推奨を出させる・比べてから選ぶ・自分の案を批評させる・設計の壁打ち
<!-- textlint-enable -->

選択肢と推奨案を出させるとは、答えを 1 つ返させる代わりに、数案と推奨と理由を並べさせ、決めるのは人のままにする頼み方である。場面で使い分ける。選ぶ場面では選択肢を出させ、独自性が要る発想の場面では先に自分の案を書く。

## 答えを選ぶ場面：選択肢と推奨案 {#choose}

答えを選ぶ場面とは、認証の方式や保存先の技術のように、候補の中から方針を決める場面である。ここでは Claude に、前提の違う数案と、推奨案と、その理由を出させる。決めるのは人である。

次の頼み方は、案が 1 つしか返らない。

```text
認証の方式を決めたい。どうすればいい？
```

この頼み方では、Claude が候補を絞った理由も、捨てた案も見えない。同じ依頼を、選択肢と推奨案を出させる形に書き直す。

<!-- gen:begin snippet ask-for-options/options-recommend -->
<!-- textlint-disable -->

???+ example "雛形：選択肢と推奨案を出させる依頼の雛形"

    ```text
    〔決めたいこと〕を決めたい。まだ実装はせず、提案だけしてください。
    前提：〔規模・期限・既存の構成・守りたい制約〕

    1. 実現できる案を 2〜4 つ挙げてください。似た案を言い換えて増やさず、前提が違う案を選んでください。
    2. 各案に、利点・欠点・向く条件を書いてください。
    3. 推奨は 1 つだけにしてください。理由と、推奨が外れる条件（この前提が違えば別の案がよい、という点）を書いてください。
    4. 私の前提のうち、確かめないと推奨が変わるものがあれば、最後に挙げてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet ask-for-options/options-recommend -->

Before から足したものは 5 つある。

- **提案だけで止める指定**：「まだ実装はせず、提案だけ」と動詞で書き分ける。理由は <!-- link:begin suggest-or-do#verbs -->[提案してほしいのか、実行してほしいのか › 提案と実行を動詞で分ける](suggest-or-do.md#verbs)<!-- link:end --> にある。
- **前提**：規模・期限・既存の構成・制約を渡す。案の良し悪しは前提で決まるからである。
- **前提の違う案**：言い換えで数を増やさせず、考え方の違う案を求める。
- **推奨は 1 つと、外れる条件**：推奨を 1 つに絞らせ、その推奨が成り立たなくなる前提を書かせる。
- **確かめるべき前提**：Claude が仮定した点のうち、違えば推奨が変わるものを最後に挙げさせる。

返答を読むときは、推奨そのものより、理由と「外れる条件」を見る。外れる条件が自分の事情に当てはまるなら、推奨を採らない判断ができる。不確かなタスクで、選択肢と既定の推奨案を 1 つ出させる型は、実務家の間で紹介されている（根拠：弱）。

面による違いは、依頼を出す場所だけである。依頼文はアプリ・Claude Code・API のどれでも同じに書ける。Claude Code では、計画の段階で、再利用できる既存の関数を探させてから案を出させる使い方も紹介されている（根拠：弱）。

## 発想の場面：先に自分の案、AI には問いと反論 {#ideate}

発想の場面とは、考察や企画のように、ほかの人と差がつく案そのものに価値がある場面である。この場面で選択肢を先に出させると、最初に見た案へ考えが引っ張られる。そこで、先に自分の案を書き、AI へは案ではなく問いと反論を頼む。

先に自分で考える順序の本体は <!-- link:begin think-before-asking#self-first -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI](../judgment/think-before-asking.md#self-first)<!-- link:end --> にある。選ぶ場面と発想の場面の見分け方は <!-- link:begin think-before-asking#choose-vs-ideate -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 答えを選ぶ場面と、発想する場面](../judgment/think-before-asking.md#choose-vs-ideate)<!-- link:end --> にある。差が要る場面の見分け方は <!-- link:begin ai-ideas-are-everyones#when-difference-matters -->[AI の案は「みんなの案」（均質化） › 差が要る場面と、底上げで足りる場面](../judgment/ai-ideas-are-everyones.md#when-difference-matters)<!-- link:end --> が扱う。

AI に頼むものは、答えではなく、確かめるべき問いである。解法や設計の案を出させずに、資料を読んで問いを挙げさせる。

<!-- gen:begin snippet ask-for-options/question-role -->
<!-- textlint-disable -->

??? example "雛形：確かめるべき問いを挙げさせる依頼の雛形（問い役）"

    ```text
    解法や設計の案は出さないでください。添付の〔問題文・要件書・仕様〕を読み、私が先に確かめるべき問いを 10 個挙げてください。
    各問いには、根拠となる原文の箇所を短く引用してください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet ask-for-options/question-role -->

反論は、書いた自分の案を見せて頼む。頼み方は次の節にある。

根本的に前提の異なる案を AI に出させるのは、自分の案が行き詰まった中盤に限る（類推）。最初から出させると、自分の案を作る前に、AI の案が基準になってしまう。

## 自分の案を批評させる {#critique}

自分の案を批評させるとは、書いた案を AI に見せ、代案を出させずに弱点だけを指摘させる頼み方である。選択肢を出させる頼み方の裏返しになる。自分の案を持ったまま、見えていない前提を外から洗い出せる。

指摘させるのは 3 点に絞る。誤っている可能性のある前提、見落としている条件、方針が崩れそうな入力や相手や状況である。「新しい解法は提案しない」と書くのは、代案に流れて、自分の案への指摘が薄くなるのを防ぐためである。

<!-- gen:begin snippet ask-for-options/critique-own-idea -->
<!-- textlint-disable -->

??? example "雛形：自分の案の批評を頼む依頼の雛形（批評役）"

    ```text
    以下は私の〔考察メモ・設計案〕です。新しい解法や代案は提案せず、次の 3 点だけを指摘してください。
    (1) 誤っている可能性のある前提
    (2) 見落としている条件（〔問題文・要件書〕のどこに書かれているかを、短く引用してください）
    (3) この方針が崩れそうな入力・相手・状況の具体像（業務なら、想定外の利用者の操作、負荷、ほかのシステムの挙動）
    指摘ごとに、確かめる方法を 1 行添えてください。根拠のない指摘には「推測」と付けてください。

    〔メモや案を貼る〕
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet ask-for-options/critique-own-idea -->

3 点目の「崩れそうな状況」は、競技では負けやすい入力や相手の特徴、業務では想定外の利用者の操作や負荷に言い換えて使える。

批評を頼むときは、次の 3 つに気を付ける。

- **新しい文脈で頼む**：議論の途中でなく、成果物と基準だけを新しい会話に貼ると、迎合が減る。手順は <!-- link:begin ask-without-sycophancy#fresh-context-critique -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 新しい文脈で、成果物と基準だけを見せる](../judgment/ask-without-sycophancy.md#fresh-context-critique)<!-- link:end --> にある。
- **案を並べるときは誰の案かを伏せる**：自分の案と Claude の案を並べて比べさせるなら、どれが自分の案かを書かない。理由は <!-- link:begin ask-without-sycophancy#hide-preferences -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 好みと確信を伏せる](../judgment/ask-without-sycophancy.md#hide-preferences)<!-- link:end --> と <!-- link:begin ask-without-sycophancy#compare-side-by-side -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 並べて同時に比べさせる](../judgment/ask-without-sycophancy.md#compare-side-by-side)<!-- link:end --> にある。
- **指摘に実験を付けさせる**：指摘を鵜呑みにせず、確かめる実験を添えさせる。見方は <!-- link:begin ask-without-sycophancy#critique-with-experiments -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判には反証の実験を付けさせる](../judgment/ask-without-sycophancy.md#critique-with-experiments)<!-- link:end --> にある。

## なぜ効くか、何に効くか {#why}

この頼み方が関わる原理は「握る」と「見せる」である。防ぐ Claude 側の原因は「見えていない」、人の側の落とし穴は「同意を根拠にする」と「みんなの案になる」である。

- **握る**：案を並べさせ、選ぶ前に止めることで、決める役を人に残す。答えを 1 つだけ受け取ると、決めたのは Claude になり、人は採るか捨てるかしか選べない。
- **見せる**：数案と理由と、推奨が成り立たなくなる前提（外れる条件）を書かせると、Claude が置いた前提と、捨てた案が見える。
- **見えていない**：Claude は、こちらの事情や評価の軸を全部は見ていない。1 つの答えでは、その見えていない部分が隠れたままになる。外れる条件と確かめるべき前提を書かせると、足りない前提を人が補える。
- **同意を根拠にする**：推奨に Claude が賛成していることは、正しさの証拠ではない。理由と外れる条件を読んで、自分の事情と合うかで判断する。考え方は <!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](../judgment/agreement-is-not-evidence.md#what-counts)<!-- link:end --> にある。自分の案を先に見せると賛成へ傾きやすい理由は <!-- link:begin sycophancy#why -->[迎合（sycophancy） › なぜそうなるか](../basics/sycophancy.md#why)<!-- link:end --> にある。
- **みんなの案になる**：AI が出す案は、ほかの人が得る案と似やすい。発想の場面で先に自分の案を書くのは、この均質化を避けるためである。理由は <!-- link:begin ai-ideas-are-everyones#outputs-converge -->[AI の案は「みんなの案」（均質化） › AI を使った成果どうしは似る](../judgment/ai-ideas-are-everyones.md#outputs-converge)<!-- link:end --> にある。

## 効かない場面とやりすぎ {#limits}

選択肢を出させる頼み方には、効かない場面とやりすぎがある。

- **決めるほどでない小さな選択**：変数名や細かい書き方のように、間違えても直せるものに案を出させると、読む手間のほうが大きい。
- **要件が固まっていないとき**：選ぶ前に、何を満たしたいかが決まっていない。先に質問させる。手順は <!-- link:begin let-claude-ask#how -->[質問させる・インタビューさせる › 質問させる頼み方](let-claude-ask.md#how)<!-- link:end --> にある。
- **案の水増し**：数を多く求めると、名前だけ違う似た案が並ぶ。前提の違う案を数案に絞って求める。
- **推奨をそのまま採る**：推奨は理由を読むための入口である。採るかどうかは、外れる条件と自分の事情を突き合わせて決める。
- **事実の誤り**：案に書かれたライブラリの機能や制限は、Claude の記憶に基づいていることがある。決める前に、公式の文書などの一次資料で確かめる。
- **批判の強めすぎ**：批評を頼みすぎると、必要のない弱点まで挙がる。加減は <!-- link:begin ask-without-sycophancy#dont-overdo-criticism -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判を強めすぎない](../judgment/ask-without-sycophancy.md#dont-overdo-criticism)<!-- link:end --> にある。

!!! example "判断例：頼み方をどちらにするか"
    - **状況**：新しい社内ツールの保存先を決める。同じ週に、コンテストの考察で解法の方針も立てる。
    - **迷う候補**：どちらにも選択肢と推奨案を出させる。または、保存先は選択肢を出させ、考察は先に自分の案を書く。
    - **選んだもの**：保存先は選択肢と推奨案を出させ、考察は先に自分の案を書いて、AI には問いと反論を頼む。
    - **理由**：保存先は、既知の候補から条件に合うものを選ぶ場面で、案の比較が価値になる。考察は、他の人と差がつく案こそ価値であり、AI の案を先に見ると似た案に寄るからである。

関連するページは、下にまとめて示す。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [提案してほしいのか、実行してほしいのか](suggest-or-do.md)

**関連**

- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](../judgment/think-before-asking.md)
- [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)
- [迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [迎合（sycophancy）](../basics/sycophancy.md)
- [質問させる・インタビューさせる](let-claude-ask.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
