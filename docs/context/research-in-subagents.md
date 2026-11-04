---
id: research-in-subagents
title: 出力の多い調査はサブエージェントに任せて要約だけ受け取る
nav_title: 調査をサブエージェントに任せる
aliases: [調査は subagent に任せて要約だけ受け取る, サブエージェントに調べさせる, Explore subagent]
type: concept
field: context
chapter: 脇道を分ける
order: 140
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発, 調べもの]
summary: ログや多数のファイルを読む調査を別の文脈で行わせ、本筋には結論と根拠の場所だけを戻させる。トークンは余分にかかるので、出力が多く本筋から独立した調査に限る。
signs:
  - {type: goal, text: 調べものの途中経過で、本筋の会話を埋めたくない}
  - {type: situation, text: 「subagent を使え」と書き足すべきか迷っている}
prerequisites: [subagent-isolation]
related: [writing-subagents, skill-vs-subagent, what-subagents-dont-inherit, independent-review, choose-what-to-read, side-questions-btw, parallel-and-loop-costs, explore-a-codebase, tidy-the-desk]
tracks: [subagents]
outdated_advice: [subagents-to-save-context, tell-it-to-use-subagents, subagent-per-step]
sources: [cc-docs-sub-agents, cc-docs-best-practices, wb-cc-best-practices-2026-10-27, api-docs-prompting-opus-5, cc-docs-costs, anthropic-eng-effective-context-engineering-ai]
volatility: 中
sections:
  - {title: 任せてよい調査、本筋で読むべきもの, anchor: when}
  - {title: 頼み方と戻させる形, anchor: how}
  - {title: 何に効くか, anchor: effects}
  - {title: 費用と使いすぎ, anchor: cost}
  - {title: 誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：出力の多い調査を別の文脈に任せ、結論と根拠の場所だけを本筋に戻させる頼み方と、任せてよい調査の見分け方が分かる。
    - **いつ引くか**：調べものの途中経過で本筋の会話を埋めたくないとき。「subagent を使え」と書き足すか迷うとき。
    - **前提**：<!-- link:begin subagent-isolation -->[サブエージェントは別室の部下](../basics/subagent-isolation.md)<!-- link:end -->

<!-- textlint-disable -->
別名：調査は subagent に任せて要約だけ受け取る・サブエージェントに調べさせる・Explore subagent
<!-- textlint-enable -->

出力の多い調査をサブエージェントに任せるとは、ログや多数のファイルを読む調べものを別の文脈で行わせ、本筋の会話には結論と根拠の場所だけを戻させることである。任せる価値があるのは、途中経過が本筋に要らず、出力が多い調査だけだ。トークンは余分にかかり、答えが賢くなるわけでもない。

## 任せてよい調査、本筋で読むべきもの {#when}

任せてよいかどうかは、調査の途中経過が本筋の判断に要るかで決まる。たとえば失敗したテストの原因を探すと、実行結果や読んだファイルの中身が会話に並ぶ。結論に使うのはその一部だけで、残りは本筋の机を散らかす。この途中経過を別の文脈（別室の部下）に閉じ込め、報告書だけを机に置かせるのが、調査を任せる技法である。

| 調査の様子 | 置き場 |
| --- | --- |
| テスト全体の実行、ログの解析、文書の取得など、出力が多く、使うのはごく一部 | サブエージェントに任せる |
| 広い検索で、本筋の作業と独立して進められる | サブエージェントに任せる |
| 読んだ中身を見ながら次の手を決める調査 | 本筋で読む |
| 数ファイルを見れば済む小さな調査 | 本筋で読む |
| 修正まで続く作業 | 本筋で行う |
| 出力は長いが、コマンドで絞れる | 絞って本筋で読む |
| 用語や仕様を 1 つ確かめるだけ | 本筋を汚さずに聞く |

- 小さな調査を任せると、新しいサブエージェントは本筋がすでに持っていた文脈を集め直すので、かえって遅くなることがある
- サブエージェントは本筋の会話の履歴を見ない。会話で決めた経緯に頼る調査は、依頼に書き込むか本筋で行う（引き継がれるものは <!-- link:begin what-subagents-dont-inherit -->[サブエージェントに引き継がれないもの](../extend/what-subagents-dont-inherit.md)<!-- link:end --> にある）
- 出力を絞る手は <!-- link:begin choose-what-to-read#trim-output -->[@参照と、何を読ませるかの絞り込み › 出力を絞る](choose-what-to-read.md#trim-output)<!-- link:end --> にある。ちょっとした質問なら <!-- link:begin side-questions-btw#which -->本筋を汚さずに聞く（/btw） › /btw・新しい会話・サブエージェントの使い分け（準備中）<!-- link:end --> に使い分けがある
- 知らないコードの全体像をつかむ流れは <!-- link:begin explore-a-codebase -->[知らないコードベースを読む](../recipes/explore-a-codebase.md)<!-- link:end --> で扱う

!!! example "判断例：長い失敗ログの原因を探す"
    - **状況**：CI が落ち、ログが長い。原因を突き止めて修正したい。
    - **迷う候補**：ログを本筋に貼って読む。原因の調査だけをサブエージェントに任せる。
    - **選んだもの**：原因の調査を任せ、修正は本筋で行う。
    - **理由**：ログの全文は、結論が出れば本筋に要らない。修正の判断は、本筋の会話で決めた方針に沿って行う必要がある。失敗が 1 件で、ログの該当部分が数行なら、任せずに本筋で読むほうが速い。

## 頼み方と戻させる形 {#how}

頼み方の要は、何を戻させるかを依頼に書くことである。「サブエージェントで調べて」とだけ頼むと、戻る報告の長さと形が決まらず、報告そのものが本筋を埋めうる。報告が多ければ、本筋の文脈もやはり埋まる。

次の Before/After は、同じ調査の頼み方である。

```text
Before
セッションの有効期限を決めている箇所を調べて、影響範囲を教えて。

After
セッションの有効期限を決めている箇所の調査をサブエージェントに任せて。
読み取りだけで調べ、戻すのは「結論」「根拠の場所（パスと行番号）」
「分からなかったこと」だけにして。コードの全文は戻さないで。
```

After で足したのは 4 つある。

- 任せる範囲と目的。サブエージェントは会話を見ないので、依頼の文だけが手がかりになる
- 戻す形。結論と、結論ごとの根拠の場所と、分からなかったこと
- 読み取りだけという制限。調査が修正に広がらない
- 全文を戻さないという指定。本筋に入る量を縛る

下の雛形は、この 4 つを空欄にした依頼である。

<!-- gen:begin snippet research-in-subagents/delegate-research -->
<!-- textlint-disable -->

??? example "雛形：調査を任せる依頼と、戻させる要約の形"

    ```markdown
    次の調査をサブエージェントに任せてください。

    調べること：<例：セッションの有効期限を決めている箇所をすべて探す>
    調べる範囲：<例：src/auth/ と tests/auth/ だけ>
    目的：<例：期限の長さを変える修正で、どこに影響が出るかを知りたい>

    調査は読み取りだけで行い、ファイルは変更しないでください。

    本筋に戻すのは次の 3 つだけにしてください。
    - 結論（3 文まで）
    - 結論ごとの根拠の場所（ファイルのパスと行番号を 1 つ以上）
    - 分からなかったことと、確かめていないこと

    ログやコードの全文は戻さないでください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet research-in-subagents/delegate-research -->

コードを探して読むだけの調査なら、組み込みの Explore を使える。読み取り専用で、詳しい出力はサブエージェント側に留まり、徹底度を指定できる。繰り返し使う調査の担当は、自分で定義できる。作り方は <!-- link:begin writing-subagents#define -->[サブエージェントの作り方と使いどころ › 定義の書き方（ファイルを書くか、Claude に作らせる）](../extend/writing-subagents.md#define)<!-- link:end --> を見る。

戻ってきた要約は、調査を読んだ担当を通した二次の情報である。結論が修正や判断の土台になるなら、戻された根拠の場所を本筋で開いて確かめる。場所を指して読ませる手は <!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](choose-what-to-read.md#point-or-search)<!-- link:end --> にある。別の担当に確かめさせる考え方は <!-- link:begin independent-review -->[書いた本人ではない者にレビューさせる](../verify/independent-review.md)<!-- link:end --> を見る。

## 何に効くか {#effects}

調査を任せる技法が効くのは、原理「見せる」と、原因「散らかっている」である。Claude に見せるものを選び、本筋の机には結論と根拠の場所だけを置く。調査の途中経過が本筋に残らないので、焦点がぼけにくい。Anthropic のエンジニアリング記事も、サブエージェントがきれいな文脈で探索して要約を返す構成を、長い作業の手法の 1 つに挙げている。

効く先は、溢れの防止ではない。公式の Best practices の改稿は、コンテキストを守るためにサブエージェントを使う助言を、もうやめてよいものに入れた。溢れることがまれになったからで、今も向くのは、並べる作業、うるさい出力を本筋から離すこと、独立したレビューである。整頓の位置づけは <!-- link:begin tidy-the-desk#why-now -->[机を整える：新鮮さ・巻き戻し・書き出し・委任 › 溢れの心配から、質と費用へ](tidy-the-desk.md#why-now)<!-- link:end --> にある。

任せても、答えが賢くなるわけではない。同じ作業をサブエージェントに渡しても、答えはよくならない。仕組みは <!-- link:begin subagent-isolation#cost -->[サブエージェントは別室の部下 › 賢くはならず、費用がかかる](../basics/subagent-isolation.md#cost)<!-- link:end --> に書いてある。

## 費用と使いすぎ {#cost}

サブエージェントは自分の request を送るので、同じ使用量枠を消費する。出力の多い調査を任せるのは、本筋の文脈を軽くする代わりに、余分なトークンを払う取引である。

- 任せる数が増えると、費用は本数と回数と 1 回の文脈の大きさの掛け算で膨らむ。仕組みは <!-- link:begin parallel-and-loop-costs#multiplication -->[並列・ループ・workflows のコスト › 費用が膨らむ掛け算](../cost/parallel-and-loop-costs.md#multiplication)<!-- link:end -->、始める前に決めることは <!-- link:begin parallel-and-loop-costs#decide-before-starting -->[並列・ループ・workflows のコスト › 始める前に決める三つ](../cost/parallel-and-loop-costs.md#decide-before-starting)<!-- link:end --> にある
- 委任の多いモデルでは、小さな作業まで任せて費用が膨らむ。公式の頼み方の手引き（[Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)）は、独立して並べられる大きな作業だけを任せるよう指示することと、数の上限を設けることを勧める
- Claude Code は、同時に動かす数を環境変数 `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` で、入れ子の深さを `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` で縛れる
- 元が取れているかは、`/usage` でサブエージェントの種類ごとの使用量を見て確かめる

!!! example "判断例：調査を毎回任せるか"
    - **状況**：同じリポジトリで、小さな調べものを 1 日に何度も頼む。
    - **迷う候補**：すべてサブエージェントに任せる。出力の多いものだけ任せる。
    - **選んだもの**：出力が多く、本筋と独立したものだけを任せる。
    - **理由**：小さな調べものは、任せるたびに文脈を集め直すので、本筋で読むより遅く、トークンも余分にかかる。任せた回数でなく、出力の多さで線を引く。

## 誤解 {#misconceptions}

- 「任せれば賢くなる」。サブエージェントは作業を本筋から隔てるだけで、答えの質を上げない。多用すると、遅くなり、トークンも増えうる
- 「コンテキストを守るために、調べものは一律にサブエージェントへ」。この助言は条件付きになった。CLAUDE.md や頼み方の型で一律に決めていないかを見る。台帳の行は <!-- link:begin outdated-advice-ledger#subagents-to-save-context -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#subagents-to-save-context)<!-- link:end --> にある
- 「`subagent を使え` と書き足せば、よく調べる」。書き足しても戻す形は決まらず、委任が増えるだけになりうる。台帳の行は <!-- link:begin outdated-advice-ledger#tell-it-to-use-subagents -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#tell-it-to-use-subagents)<!-- link:end --> にある
- 「工程ごとにサブエージェントを作れば散らからない」。文脈を分ける意味のある作業にだけ使う。台帳の行は <!-- link:begin outdated-advice-ledger#subagent-per-step -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#subagent-per-step)<!-- link:end --> にある

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code（改稿後。Internet Archive の写し、2026-10-27 08:15 UTC）](https://web.archive.org/web/20261027081520/https://code.claude.com/docs/en/best-practices)：Anthropic（写し）・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [サブエージェントは別室の部下](../basics/subagent-isolation.md)

**関連**

- [サブエージェントの作り方と使いどころ](../extend/writing-subagents.md)
- [スキルとサブエージェントの違い](../extend/skill-vs-subagent.md)
- [サブエージェントに引き継がれないもの](../extend/what-subagents-dont-inherit.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [@参照と、何を読ませるかの絞り込み](choose-what-to-read.md)
- 本筋を汚さずに聞く（/btw）（準備中）
- [並列・ループ・workflows のコスト](../cost/parallel-and-loop-costs.md)
- [知らないコードベースを読む](../recipes/explore-a-codebase.md)
- [机を整える：新鮮さ・巻き戻し・書き出し・委任](tidy-the-desk.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
