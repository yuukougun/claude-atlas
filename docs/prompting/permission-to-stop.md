---
id: permission-to-stop
title: 止まって報告する権利を渡す
aliases: [テストがおかしければ報告させる, 回避せずに止まる, 人に判断を仰がせる]
type: concept
field: prompting
chapter: 正直さと確かめ方
order: 190
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
scenes: [開発, データ分析, コンテスト]
summary: テストや評価がおかしいと判断したら回避せずに止まって報告してよい、と依頼に書く。言葉の許可だけでは防ぎきれないので、テストを書き換えられない仕組みと組み合わせる。
signs:
  - {type: goal, text: テストが間違っていそうなら、書き換えずに報告してほしい}
  - {type: goal, text: 仕様と食い違うときは、手を止めて知らせてほしい}
prerequisites: [allow-i-dont-know]
related: [rewrote-tests-to-pass, protect-tests, misses-broken-evaluation, reward-hacking, verifier-three-conditions, suggest-or-do]
sources: [api-docs-prompting-best-practices, arxiv-2510-20270]
volatility: 中
sections:
  - {title: 止まって報告する条件を書く, anchor: conditions}
  - {title: 言葉の許可が効く範囲（モデルによる差）, anchor: limits}
  - {title: 書き換えられない仕組みと組み合わせる, anchor: with-structure}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：テストや評価がおかしいと判断したら、回避せずに止まって報告してよい、と依頼に書く。ただし効き方はモデルで違い、言葉の許可だけでは足りないので、書き換えられない仕組みと組み合わせる。
    - **いつ引くか**：テストが間違っていそうなら、書き換えずに報告してほしいとき。仕様と食い違うときに、手を止めて知らせてほしいとき。
    - **前提**：<!-- link:begin allow-i-dont-know -->[「分からない」と言ってよいと伝える](allow-i-dont-know.md)<!-- link:end -->

<!-- textlint-disable -->
別名：テストがおかしければ報告させる・回避せずに止まる・人に判断を仰がせる
<!-- textlint-enable -->

止まって報告する権利を渡すとは、テストや評価がおかしいと判断したら、回避せずに止まって報告してよい、と依頼に明示することである。「分からないと言ってよい」と伝える技法の、検証の場面での版にあたる。ただし、これは頼み方の一行にすぎない。書き換えそのものを止める鍵（権限やファイルの保護）ではないので、守りの本体にはならない。

## 止まって報告する条件を書く {#conditions}

止まって報告する条件とは、どういうときに作業を止め、何を報告するかを、依頼に具体的に書いた数行である。完了の条件を「テストが通ること」とだけ書くと、テストが誤っていても、通すことが目的になる。次の Before/After は、同じ依頼に止まる条件を足したものである。

Before：

```text
tests/test_price.py が通るように、calc_price を直して。
```

After：

```text
tests/test_price.py が通るように、calc_price を直して。
テストは正しさを確かめるためのもので、解を決めるものではない。
テストの期待値が仕様と食い違うと判断したら、テストを変えず、特定の入力だけを通す分岐も書かず、手を止めて報告して。
報告には、食い違う期待値と、合わない仕様の記述を書くこと。
```

After で足したのは 3 つである。1 つ目はテストの位置づけ、2 つ目は止まる条件、3 つ目は報告に書く中身である。公式のプロンプトガイドも、テストが誤っていれば回避せずに報告させる書き方を勧めている（[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)）。

この数行が変えるのは、出口の数である。条件がないと、テストが通らないときの出口は、通すように直すことだけに見える。条件があると、「おかしいと伝えて止まる」という出口が増える。報告の中身も決めておくと、人は食い違いをすぐ確かめて、テストを直すか、仕様を直すかを選べる。

面ごとに、条件を置く場所が違う。

=== "Claude Code"
    - 毎回守らせたい条件は、`CLAUDE.md` に数行で置く。下の雛形がその例である。
    - その回だけの条件は、依頼の本文に書く。

=== "API"
    - 毎回守らせたい条件は、システムプロンプトに書く。
    - その回だけの条件は、ユーザーのターンに書く。

<!-- gen:begin snippet permission-to-stop/stop-conditions -->
<!-- textlint-disable -->

??? example "雛形：止まって報告する条件を書いた CLAUDE.md の数行"

    ```markdown
    ## 止まって報告する条件
    - テスト・評価器・仕様のどれかが誤っていそうだと判断したら、回避せずに、その場で手を止めて報告する。
    - 報告には、食い違っている期待値と、合わない仕様の記述を書く。直す案があれば添える。
    - テストは正しさを確かめるためのもので、解を決めるものではない。通すためにテストを書き換えない。
    - 特定の入力だけを通す分岐や、定数の埋め込みで通さない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet permission-to-stop/stop-conditions -->

条件は、読んだ Claude が「いまがそのときか」を判断できる具体さで書く。「問題があれば報告して」では広すぎる。「期待値が仕様の記述と食い違うとき」「評価の入力が本番と違う形のとき」のように、見分けられる形にする。止まったあとに提案で済ませるか、実行まで進めるかは、<!-- link:begin suggest-or-do#stop-and-discuss -->[提案してほしいのか、実行してほしいのか › 懸念があれば止まって相談させる](suggest-or-do.md#stop-and-discuss)<!-- link:end --> で決める。

## 言葉の許可が効く範囲（モデルによる差） {#limits}

言葉で止まる権利を渡す効果は、モデルによって大きく違う。ImpossibleBench という研究（arXiv、2025 年）は、仕様と矛盾するテストを使う Conflicting-SWEbench で、「人間に判断を仰ぐ」逃げ道を与えた効果を測った。GPT-5 の不正率は 54% から 9% に、o3 は 49% から 12% に下がった（根拠：中）。

一方で、同じ論文は、Claude Opus 4.1 では効果が「ずっと小さい」と書いている。この結果には数値が付いていない（[ImpossibleBench](https://arxiv.org/abs/2510.20270)）。この辞典は、次のように扱う。

- 「止まる権利の効果は確かめられている」とは書かない。GPT-5 と o3 の数値を、Claude の傾向として読まない。
- 「ほぼ消える」とも書かない。Claude で小さいと言えるのは、Opus 4.1 での結果だけである。
- 現行の Claude モデルで、言葉の許可がどれだけ効くかは未確認である。

そのため、Claude 向けの頼み方としては、言葉の許可を添える一行として使う。守りの本体にはしない。

やりすぎにも注意する。止まる条件を広げすぎると、細かい点のたびに作業が止まり、任せた意味が薄れる（推論・実践例なし）。止めたい場面だけを、条件に具体的に書く。また、言葉の許可は鍵ではない。許可を書いても、テストが書き換えられる状態なら、書き換えは起こりうる。

## 書き換えられない仕組みと組み合わせる {#with-structure}

言葉の許可と組み合わせる仕組みとは、テストや評価器を Claude の手が届かない状態にすることである。この辞典の原理でいうと、2 つに分かれる。

- **縛る**：テストや採点のファイルを読み取り専用にする、変更を差分のレビューで止める、といった仕組みで、書き換えること自体をできなくする。「縛っていない」状態、つまり書き換えられる状態を防ぐ。
- **確かめる**：止まって報告された食い違いを、人が確かめる。テストが誤っているのか、仕様が誤っているのかを、人が決める。報告がなければ、テストや評価の誤りを誰も確かめていない状態が続く。「確かめていない」状態を防ぐのは、この手順である。

役割を分けると、こうなる。言葉の許可は、Claude が書き換えずに報告する道を開く。仕組みは、その道を通らなかった場合に、書き換えを防ぐ。仕組みの層は <!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](../verify/protect-tests.md#layers)<!-- link:end --> に、書き換えられない検証器の条件は <!-- link:begin verifier-three-conditions#tamper-proof -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 書き換えられない](../eval/verifier-three-conditions.md#tamper-proof)<!-- link:end --> にある。採点の抜け道が生まれる理由は <!-- link:begin reward-hacking#what-it-helps -->[採点器を騙す（reward hacking） › 何に効くか（原理「確かめる」「縛る」と原因「確かめていない」「縛っていない」）](../basics/reward-hacking.md#what-it-helps)<!-- link:end --> にある。

例外を許さない禁止は、Claude Code では deny ルールかフックで強制する。`CLAUDE.md` には、止まる条件と、その理由だけを書く。依頼の書き方の全体は <!-- link:begin protect-tests#in-the-request -->[テストを守る（改ざんを防ぐ） › 依頼に書くこと](../verify/protect-tests.md#in-the-request)<!-- link:end --> を見る。

すでにテストを書き換えて通された場合は、<!-- link:begin rewrote-tests-to-pass -->[テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)<!-- link:end --> で原因を切り分ける。手元の評価は良いのに本番で通用しない場合は、<!-- link:begin misses-broken-evaluation -->[手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)<!-- link:end --> を見る。

!!! example "判断例：止まる条件を書いた後に、tests/ を守るか"
    - **状況**：Claude Code に、失敗しているテストを通す修正を任せる。`CLAUDE.md` には止まる条件を書いた。
    - **迷う候補**：言葉の許可だけで任せる。または、`tests/` を読み取り専用にする仕組みも加える。
    - **選んだもの**：仕組みも加える。
    - **理由**：Claude で言葉の許可が効く程度は、確かめられていない。書き換えられる状態が残っていると、許可を無視された場合の被害が大きい。仕組みなら、許可が効かなかった場合も、書き換えを止められる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases](https://arxiv.org/abs/2510.20270)：arXiv（Zhong, Ziqian ほか）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [「分からない」と言ってよいと伝える](allow-i-dont-know.md)

**関連**

- [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)
- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- [提案してほしいのか、実行してほしいのか](suggest-or-do.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
