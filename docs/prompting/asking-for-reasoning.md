---
id: asking-for-reasoning
title: 推論を見せてほしいとき
aliases: [思考の過程を見たい, thinking の要約, 根拠を短く説明させる, thinking タグに書かせる]
type: concept
field: prompting
chapter: 正直さと確かめ方
order: 200
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない]
scenes: [開発, 学習]
summary: 答えの理由を知りたいときは、短い根拠の説明を頼むか、表示される思考の要約を読む。推論の全文を本文に書かせる指示は断られることがあり、書かれた推論が実際の計算と一致する保証もない。
signs:
  - {type: goal, text: なぜその答えになったのか、過程を全部見せてほしい}
  - {type: symptom, text: 推論を書き出すよう頼んだら断られた}
prerequisites: [unfaithful-reasoning]
related: [when-requests-are-refused, refused-or-blocked, how-thinking-works, thinking-keywords, evidence-not-reports, effort-levels]
tracks: [adaptive-thinking]
outdated_advice: [thinking-tags]
sources: [api-docs-prompting-opus-5-5, api-docs-prompting-best-practices, api-docs-thinking, api-docs-adaptive-thinking, api-docs-refusals, anthropic-research-tracing-thoughts-language-model]
volatility: 中
sections:
  - {title: 頼み方の例, anchor: example}
  - {title: 全文を求める指示が断られる理由, anchor: refusal}
  - {title: 短い根拠と思考の要約で読む, anchor: alternatives}
  - {title: 何に効くか, anchor: effects}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：答えの理由は、短い根拠の説明を頼むか、表示される思考の要約を読むと確かめられる。
    - **いつ引くか**：なぜその答えになったのか、過程を全部見せてほしいとき。推論を書き出すよう頼んだら断られたとき。
    - **前提**：<!-- link:begin unfaithful-reasoning -->[表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)<!-- link:end -->

<!-- textlint-disable -->
別名：思考の過程を見たい・thinking の要約・根拠を短く説明させる・thinking タグに書かせる
<!-- textlint-enable -->

推論を見せてほしいとは、答えの理由を知りたいという頼みである。内部の推論を本文に全部書かせる頼み方は、断られることがある。理由を知る目的には、短い根拠の説明と、表示される思考の要約という 2 つの手がある。

## 頼み方の例 {#example}

同じ「この設計を選んだ理由を知りたい」という依頼を、推論の全文を求める形と、根拠を求める形で並べる。

**Before（全文を求める）**

```text
この設計を選んだ理由を、頭の中で考えた過程を省かずに <thinking> タグへ書き出してから答えてください。
```

**After（短い根拠を求める）**

```text
この設計を選んだ理由を、決め手になった点 3 つと、検討して選ばなかった案 1 つ、各 2 文以内で説明してください。
```

After で足したのは、説明の中身の指定である。決め手の数、選ばなかった案、文の長さを決めている。書き出させる対象を「考えた過程の再現」から「判断の根拠という成果物」に変えている。Before は、新しいモデルでは断られることがある。

次の雛形は After を一般化したものである。確かめ方も 1 つ添えさせるので、受け取った説明をそのまま信じずに済む。

<!-- gen:begin snippet asking-for-reasoning/short-basis-request -->
<!-- textlint-disable -->

??? example "雛形：短い根拠を頼む依頼の雛形"

    ```text
    {判断や回答の対象}について、次の形で根拠を説明してください。
    - 決め手になった点を 3 つまで、各 2 文以内で書く
    - 検討して選ばなかった案を 1 つ、選ばなかった理由とともに書く
    - 確かめられていない前提があれば、そう書く
    - 答えが正しいかを自分で確かめる方法（実行するコマンドや見る箇所）を 1 つ添える
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet asking-for-reasoning/short-basis-request -->

## 全文を求める指示が断られる理由 {#refusal}

推論の全文や決まった形（`<thinking>` の欄、JSON の `reasoning` の欄など）を本文に書かせる指示は、`reasoning_extraction` という拒否の分類に当たることがある。新しいモデルの世代で、この分類が足された（足された日：<!-- fact:begin reasoning-extraction-since -->2026-06-09（Claude Fable 5 の公開の日）（2026-11-06 時点）<!-- fact:end -->。対象のモデルは台帳の行にある）。断られると、API の応答は `stop_reason` が `refusal` になり、`stop_details.category` に分類が入る。

この種の指示は、頼んだ本人が書いていなくても入り込む。CLAUDE.md・スキル・サブエージェント・出力スタイル・MCP のツールの説明に、推論の全文や決まった形の欄を求める文が入っていることがある。`claude --safe-mode` で設定を外すと、どこから来たかを切り分けられる。止められた原因の見分け方は <!-- link:begin refused-or-blocked#diagnosis -->[断られた・止められた › 原因を安く確かめる順](../symptoms/refused-or-blocked.md#diagnosis)<!-- link:end --> にまとめてある。

出力の前に止まった拒否でも、課金される分類がある（課金の扱い：<!-- fact:begin refusals-billing-by-category -->出力の前に止まった拒否でも課金される分類は bio・frontier\_llm・reasoning\_extraction。ほかの分類は課金されない。途中で止まれば、それまでの入出力は課金される（2026-09 時点。2026 年に何度か変わった）（2026-11-06 時点）<!-- fact:end -->）。断られても費用は発生しうるので、どの分類が課金されるかは、公式の Refusals の文書（参考の節に出典を載せる）で確かめる。

「`<thinking>` タグに推論を書かせる」は、<!-- link:begin outdated-advice-ledger#thinking-tags -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#thinking-tags)<!-- link:end -->に載る助言で、かつては有効だった。思考の機能を使わないころは、答えの前に考えを書かせると答えがよくなり、その過程を読んで確かめられた。今は、推論を見たいときは本文に書かせず、思考のブロックを読む。

断られたときに、分類を避ける言い換えや分割を試してはいけない。公式が案内する手段と、避けてはいけない理由は、<!-- link:begin when-requests-are-refused#official-steps -->[正当な依頼が断られたとき › 公式が案内する手段](../safety/when-requests-are-refused.md#official-steps)<!-- link:end --> と <!-- link:begin when-requests-are-refused#why-not-evade -->[正当な依頼が断られたとき › 分類器を避ける頼み方をしない理由（利用ポリシー）](../safety/when-requests-are-refused.md#why-not-evade)<!-- link:end --> にある。

## 短い根拠と思考の要約で読む {#alternatives}

理由を知りたいときの手は 2 つある。どちらも、推論の全文を本文に書かせない。

1. **短い根拠を頼む**：説明、根拠、行ったことの要約を頼む。決め手の数や文の長さを決めて頼むと、読んで確かめやすい形で返る。
2. **思考の要約を読む**：thinking のブロックを、要約された形で受け取って読む。

面ごとに手が違う。

=== "アプリ"

    本文で、短い根拠を頼む。画面に出る思考の見え方はモデルと設定による。アプリでの設定の細部は未確認である。

=== "Claude Code"

    設定の `showThinkingSummaries` で、思考の要約を表示できる。表示されない場合は、短い根拠を本文で頼む。

=== "API"

    thinking の `display` を `"summarized"` にして要約を受け取る。要約は全文ではない。考えた分も出力として数えられる点は <!-- link:begin how-thinking-works#what-happens -->[思考（thinking）と effort の仕組み › 何が起きるか](../basics/how-thinking-works.md#what-happens)<!-- link:end --> にある。

考える深さそのものを変えたいときは、「よく考えて」と書くのではなく effort を使う。段階は <!-- link:begin effort-levels#levels -->[effort の段階と使い分け › 段ごとの振る舞い](../models/effort-levels.md#levels)<!-- link:end --> と <!-- link:begin thinking-keywords#plain-text-phrases -->[「考えて」と書くことの現在（ultrathink） › 普通の文として渡る言い回し](../models/thinking-keywords.md#plain-text-phrases)<!-- link:end --> で確かめる。

## 何に効くか {#effects}

関わる原理は「確かめる」、防ぐ原因は「確かめていない」である。理由が分からないまま答えを使うと、確かめていない答えを受け入れることになる。短い根拠は、決め手と未確認の前提を先に出させるので、確かめる場所が見える。

判断例を 1 つ示す。

!!! example "判断例：移行方針の理由を知りたい"
    - **状況**：データベースの移行方針を Claude が提案した。なぜその方針なのかを、レビューの前に把握したい。
    - **迷う候補**：推論の全文を書き出させる頼み方と、短い根拠を頼む頼み方。どちらも、理由を知りたいという目的は同じである。
    - **選んだもの**：短い根拠を頼み、決め手・選ばなかった案・確かめ方を書かせる。
    - **理由**：全文を求める指示は断られることがある。根拠なら、レビューで確かめる対象がそのまま手に入る。

## 効かない場面とやりすぎ {#limits}

書かれた根拠は、内部の計算と一致するとは限らない。大きな数の計算で「計算した」と書かれていても、内部にその痕跡は見つからなかった。そうした例が研究で報告されている（根拠：中。Anthropic の解釈可能性研究、2025-03-27）。仕組みは <!-- link:begin unfaithful-reasoning#why -->[表示された思考は内部の計算と一致するとは限らない › なぜそうなるか](../basics/unfaithful-reasoning.md#why)<!-- link:end --> にある。思考の要約も同じで、読んで納得しても、それは確かめたことにならない。

- **説明を結果の代わりにしない**：根拠が筋道立っていても、答えは独立に確かめる。実行・grep・git で見た事実を正とする考え方は <!-- link:begin evidence-not-reports#facts-win -->[報告ではなく証拠を求める › 説明と事実が食い違ったら](../verify/evidence-not-reports.md#facts-win)<!-- link:end --> にある。
- **何度も根拠を求めない**：根拠を重ねても、確かめたことにはならない。確かめ方を 1 つ添えさせて実行するほうが早い。
- **思考を切ったときの手動の段階踏み**：思考を切れるモデルで切ったときは、今も手で段階を踏ませ、答えを `<answer>` タグに書かせる手が使える。ただし、内部の推論を本文に書かせる形は断られることがある。
- **新しいモデルでは確認する**：断られるかどうかは、モデルと時期で変わる。台帳の行の確認日を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)：Anthropic・英語・確認日 2026-11-04
- [Steering thinking](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)：Anthropic・英語・確認日 2026-11-04
- [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)：Anthropic・英語・確認日 2026-11-04
- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)

**関連**

- [正当な依頼が断られたとき](../safety/when-requests-are-refused.md)
- [断られた・止められた](../symptoms/refused-or-blocked.md)
- [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- [「考えて」と書くことの現在（ultrathink）](../models/thinking-keywords.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [effort の段階と使い分け](../models/effort-levels.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
