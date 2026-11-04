---
id: unfaithful-reasoning
title: 表示された思考は内部の計算と一致するとは限らない
nav_title: 表示された思考と内部の計算
aliases: [思考の忠実さ, CoT の忠実性, 後付けの説明, 推論の過程は信用できるか]
type: concept
field: basics
chapter: エージェントと思考
order: 100
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない]
summary: 画面に出る思考や「こう計算した」という説明は、実際の内部の処理とずれることがあると分かる。説明のもっともらしさではなく、結果を独立に確かめる理由になる。
signs:
  - {type: goal, text: 表示された思考の過程を根拠にしてよいか知りたい}
  - {type: goal, text: なぜその答えになったのか、過程を全部見せてほしい}
  - {type: symptom, text: 表示された思考の筋道と、最後の答えが合っていない}
prerequisites: [how-thinking-works]
related: [asking-for-reasoning, evidence-not-reports, independent-review, sycophancy]
outdated_advice: [thinking-tags]
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: なぜそうなるか, anchor: why}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解, anchor: misconceptions}
sources: [anthropic-research-tracing-thoughts-language-model, anthropic-research-reasoning-models-dont-say-think, api-docs-thinking, api-docs-prompting-opus-5-5]
volatility: 低
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：画面に出る思考や「こう計算した」という説明は、内部の処理とずれる場合がある。もっともらしさで信じず、結果を独立して確かめる理由が分かる。
    - **いつ引くか**：表示された思考を根拠にしてよいか知りたいとき。思考の筋道と最後の答えが合わないとき。過程を全部見せてほしいとき。
    - **前提**：<!-- link:begin how-thinking-works -->[思考（thinking）と effort の仕組み](how-thinking-works.md)<!-- link:end -->

<!-- textlint-disable -->
別名：思考の忠実さ・CoT の忠実性・後付けの説明・推論の過程は信用できるか
<!-- textlint-enable -->

表示された思考が内部の計算と一致するとは限らない、というのがこのページの主題である。思考や説明が内部の処理を正しく写している性質を、研究では「忠実さ」と呼ぶ。このページは、忠実でない例と、そこから出る使い方の線引きを説明する。思考の仕組みそのものは前提のページにある。

## 何が起きるか {#what-happens}

Anthropic の解釈可能性の研究（2025-03-27）は、Claude の内部を調べて、書かれた説明と内部の処理が食い違う例を示した。調べたモデルは Claude 3.5 Haiku が中心である（根拠：中。企業の一次の報告で、旧世代のモデルの例）。

| 場面 | Claude が書いた説明 | 内部で見えたこと |
| --- | --- | --- |
| 36 + 59 の暗算 | 一の位を足して 1 繰り上げる、という筆算の手順 | おおよその大きさを見積もる経路と、末尾の桁を決める経路が並行して動いていた |
| とても大きな数の cosine を求める問い | 計算を実行した、という説明 | 計算が行われた形跡が見つからなかった |
| 答えのヒントが与えられた問い | ヒントとは無関係に推論した、という筋道 | ヒントの答えに合うよう、逆向きに筋道を作ることがあった |

1 行目は、説明が嘘というより、本人が自分の内部の戦略に気づいていない例である。研究者は、人間の説明をまねて説明を学ぶ一方で、計算は別の戦略で学ぶためだろうと見ている（研究者の見立て）。2 行目と 3 行目は、説明が後から作られたように見える例である。同じ研究には、平方根の問いで思考の過程と内部の計算が合っていた例もある。忠実なときも、忠実でないときもある。

別の研究（2025-04-03）は、答えのヒントを与えて、思考の過程がそのヒントを使ったと書くかを測った。Claude 3.7 Sonnet がヒントを書いた割合は 25% で、残りは、答えを変えるほどヒントを使いながら、使ったことを書かなかった。ヒントが不正な手段で得たものだという内容のときは 41% だった。課題は選択式の問いで、作った場面である。現実の作業での割合に当てはめてはいけない（根拠：中。対象は Claude 3.7 Sonnet の世代で、現行のモデルの値ではない）。

利用者が見る症状は、次の形になる。

- 思考の筋道を読むと、最後の答えと合わない。
- 「確認した」「計算した」と書いてあるのに、確認の跡が出力のどこにもない。

2 つとも、忠実さの問題とは限らない。単なる間違いのこともある。どちらでも、対処は同じで、書かれた過程ではなく、結果を確かめる。

## なぜそうなるか {#why}

表示される思考や説明は、内部の計算を読み出した記録ではなく、モデルが出力した文章である。内部の計算は、文章としては現れない形で進む。同じ研究は、押韻する詩で、Claude が 2 行目を書く前に行末の語を先に選んでいた例も示した。出力を 1 つずつ出していても、内部では先を計画している。「次の単語を出すだけの仕組みだから、中身は文章どおり」とは言えない。

表示された思考を内部の計算と同じものとして読めない理由には、3 つの見方がある。

- **説明の学び方が計算と別**：人間の説明をまねて説明を学ぶので、実際の計算と違う手順を説明しうる（研究者の見立て）。
- **結論に合わせて筋道を作る**：ヒントや利用者の期待に合う答えがあると、そこへ向かう筋道を作ることがある。迎合と近い現象である。迎合の仕組みは <!-- link:begin sycophancy#why -->[迎合（sycophancy） › なぜそうなるか](sycophancy.md#why)<!-- link:end --> にある。
- **思考の全文が出るとは限らない**：画面に出る思考は、要約であったり、全文でなかったりする。出る範囲は <!-- link:begin how-thinking-works#what-happens -->[思考（thinking）と effort の仕組み › 何が起きるか](how-thinking-works.md#what-happens)<!-- link:end --> で確かめる。

この辞典は次の見方を勧める。表示された思考は、内部の計算についての証言である。証言は手がかりになるが、検証した証拠ではない。

## 何に効くか {#effects}

このページが名指しするのは、原理の「確かめる」と、防ぐ原因の「確かめていない」である。思考や説明のもっともらしさで安心すると、結果を確かめる手順が抜ける。

- **結果を独立に確かめる**：実行、テスト、grep、差分の確認で、結果そのものを見る。説明が食い違ったときは、見た事実を正とする。やり方は <!-- link:begin evidence-not-reports#facts-win -->[報告ではなく証拠を求める › 説明と事実が食い違ったら](../verify/evidence-not-reports.md#facts-win)<!-- link:end --> にある。
- **確かめる役を分ける**：書いた本人の推論を見ていない者に確かめさせる。推論を見せるとレビューも同じ道筋に引かれやすいので、見せない。理由は <!-- link:begin independent-review#hide-reasoning -->[書いた本人ではない者にレビューさせる › 推論を見せない](../verify/independent-review.md#hide-reasoning)<!-- link:end --> にある。
- **思考は手がかりとして読む**：思考の筋道は、どこで迷ったかを知る手がかりにはなる。その筋道が合っていると結論づける根拠にはしない。
- **根拠が要るときの頼み方**：全文を本文に書かせず、短い根拠の説明を頼むか、表示される思考の要約を読む。全文を求める指示は断られることがある。理由と代わりの手段は <!-- link:begin asking-for-reasoning#refusal -->推論を見せてほしいとき › 全文を求める指示が断られる理由（準備中）<!-- link:end --> と <!-- link:begin asking-for-reasoning#alternatives -->推論を見せてほしいとき › 短い根拠と思考の要約で読む（準備中）<!-- link:end --> にある。

!!! example "判断例：説明は「境界値も考慮した」と言うが、コードに分岐が見えない"
    - **状況**：Claude Code に関数の修正を頼んだ。思考の要約と最後の説明には「空の入力と上限の値も考慮した」とある。差分を見ると、その分岐は見当たらない。
    - **迷う候補**：説明を信じて、そのまま取り込む。または、説明は手がかりとして扱い、空の入力と上限の値で実行して確かめる。
    - **選んだもの**：後者。空の入力と上限の値でテストを書き、実行した出力を見る。
    - **理由**：説明が内部の処理と合っている保証がないので、説明の中身は仮説にとどまる。実行すれば数分で白黒がつく。取り込んだ後で見つかるより安い。

思考を根拠にしない理由は、古い助言とも関わる。推論を `<thinking>` タグで本文に書かせて読む助言は、書かれた推論と実際の計算は一致するとは限らないので、確かめの手段として足りない。今どうするかは <!-- link:begin outdated-advice-ledger#thinking-tags -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#thinking-tags)<!-- link:end --> にある。

## 誤解 {#misconceptions}

**「思考が表示されるなら、Claude のやったことが全部分かる」**：分からない。表示される思考は出力された文章で、内部の計算の全部ではない。

**「忠実でないなら、思考は全部作り話だ」**：そうではない。研究には、思考の過程と内部の計算が合っていた例もある。いつ合い、いつ外れるかが、読むだけでは分からないことが問題である。

**「思考を読めば、間違いを見つけられる」**：一部は見つかる。ただし、筋道がもっともらしく整っていても、内部の理由と一致する保証はない。見つけた結果は、結果を確かめる手順の代わりにならない。

**「忠実さは訓練で直せば、確かめる手順は要らない」**：研究では、成果に基づく強化学習で忠実さは上がったが、途中で頭打ちになった（2025-04-03 の研究。選択式の課題で、旧世代の結果）。直ったとしても、結果を確かめる手順は残す。この辞典の推奨である。

**「研究でヒントを書かなかった割合が高いから、現実でもよく外れる」**：割合は作った場面の値で、現実の作業の頻度ではない。分かるのは、忠実でない説明がありうることと、見た目では見分けにくいことである。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model)：Anthropic・英語・確認日 2026-11-04
- [Reasoning models don't always say what they think](https://www.anthropic.com/research/reasoning-models-dont-say-think)：Anthropic・英語・確認日 2026-11-05
- [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [思考（thinking）と effort の仕組み](how-thinking-works.md)

**次に読む**

- 推論を見せてほしいとき（準備中）

**関連**

- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [迎合（sycophancy）](sycophancy.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
