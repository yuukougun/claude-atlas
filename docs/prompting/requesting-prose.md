---
id: requesting-prose
title: 文章を頼むとき（読み手・目的・手本を渡す）
nav_title: 文章を頼むとき
aliases: [文章作成の頼み方, 型どおりの文章を避ける, AI っぽい文章, mannered prose]
type: recipe
field: prompting
chapter: 型と例文
order: 230
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [見せる]
prevents: [見えていない]
scenes: [文章]
summary: 文章を頼むときは、読み手・目的・分量・手本と、避けたい言い回しを具体的に渡す。「もっと自然に」と形容詞で頼むより、嫌な箇所を例で示すほうが直る。
signs:
  - {type: symptom, text: 「もっと自然に」と頼んでも、文章が良くならない}
  - {type: goal, text: 読み手と目的に合った文章を書かせたい}
  - {type: goal, text: 自分の文体に近い文章を書かせたい}
prerequisites: [show-examples]
related: [less-ai-sounding-japanese, output-shape, write-docs, consistent-politeness, disclosure-and-provenance]
sources: [ruben-hours, api-docs-prompting-best-practices, api-docs-prompting-claude-fable-5-1]
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 読み手と目的を渡す, anchor: reader}
  - {title: 嫌な点は例で示す, anchor: concrete-dislikes}
  - {title: 推敲を別の手順に分ける, anchor: revise}
  - {title: 確かめ方, anchor: check}
  - {title: 失敗したとき, anchor: failure}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：文章を頼むときに、読み手・目的・分量・手本と避けたい言い回しを渡し、嫌な点は形容詞ではなく例で示せる。
    - **いつ引くか**：「もっと自然に」と頼んでも文章が良くならないとき。読み手と目的に合った文章を書かせたいとき。自分の文体に近い文章を書かせたいとき。
    - **前提**：<!-- link:begin show-examples -->[例を見せる](show-examples.md)<!-- link:end -->

<!-- textlint-disable -->
別名：文章作成の頼み方・型どおりの文章を避ける・AI っぽい文章・mannered prose
<!-- textlint-enable -->

文章を頼むとは、説明文・記事・メールなどの下書きを Claude に書かせ、直させることである。Claude には、誰に向けた文章か、何のための文章か、書き手がどんな文体を好むかが見えていない。見えていないものは、渡すしかない。このページは、渡すものの順序と、嫌な点の伝え方と、推敲の手順を扱う。

## 先に整える守り {#guards}

文章の依頼で先に決めておく守りは、3 つある。

- **事実は材料から**：Claude が書く数字・固有名詞・日付は、材料にあるものか、自分で確かめたものだけを残す。材料にない事実を足させないために、依頼に「材料にないことは書かず、足りなければ質問する」と書く。
- **手本に貼るものを選ぶ**：自分の過去の文章を手本にするときは、外に出してよいものだけを貼る。顧客名や社内の数字が入ったものは、伏せてから貼る。
- **出す前に人が読む**：下書きは、読み手になったつもりで最後まで読んでから出す。AI をどこにどう使ったかを開示する場かどうかは、その場の規則で確かめる。考え方は <!-- link:begin disclosure-and-provenance#four-points -->[AI 利用の開示と出所の記録 › 開示・相談・出所・意図の四つの観点](../safety/disclosure-and-provenance.md#four-points)<!-- link:end --> にある。

## 読み手と目的を渡す {#reader}

読み手と目的を渡すとは、誰が読み、読んだ後に何をしてほしいかを依頼に書くことである。文章の良し悪しは、読み手と目的で決まる。同じ内容でも、上司への報告と、顧客へのお知らせでは、よい文章が違う。

次の頼み方では、Claude は、読み手と目的を知らないまま、無難な文章を返すしかない。

```text
先週の作業について、週報を書いて。
```

同じ依頼を、読み手・目的・分量・手本・避けたい言い回しを渡す形に書き直す。

<!-- gen:begin snippet requesting-prose/write-brief -->
<!-- textlint-disable -->

???+ example "雛形：読み手・目的・手本を渡して下書きを頼む依頼の雛形"

    ```text
    〔文章の種類（例：チームへの週報、顧客へのお知らせメール）〕の下書きを書いてください。

    読み手：〔誰が読むか。何を知っていて、何を知らないか〕
    目的：〔読んだ後に、読み手に何をしてほしいか、何が分かってほしいか〕
    分量：〔字数か段落数〕
    材料：〔書いてよい事実。ここにないことは書かず、足りなければ質問してください〕
    手本：〔自分の過去の文章を 1〜3 本貼る。外に出してよいものだけ〕
    避けたい言い回し：〔あれば、直したい言い回しと、代わりにしたい言い方の対〕

    まず下書きだけを出してください。推敲は、読んでから別に頼みます。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet requesting-prose/write-brief -->

Before から足したものは 5 つある。

- **読み手**：誰が読み、何を知っていて、何を知らないか。知らないことは説明を足し、知っていることは省く判断の材料になる。
- **目的**：読んだ後に、読み手に何をしてほしいか。報告なのか、判断を求めるのかで、結論を置く場所が変わる。
- **分量**：字数か段落数。長さの指定の考え方は <!-- link:begin output-shape#length -->[出力の形と分量を指定する › 長さと要約の有無](output-shape.md#length)<!-- link:end --> にある。
- **手本**：自分の過去の文章。言葉にしにくい文体の好みが、手本で伝わる。選び方は <!-- link:begin show-examples#own-writing -->[例を見せる › 自分の文章を手本にする](show-examples.md#own-writing)<!-- link:end --> を見る。
- **避けたい言い回し**：次の節のとおり、例で渡す。

材料の欄に「ここにないことは書かず、足りなければ質問する」と入れたのは、先に整える守りの「事実は材料から」のためである。技術文書を書かせるなら、プロジェクトの既存の文書を手本にするのが筋である。その手順は <!-- link:begin write-docs -->[ドキュメント・技術文書を書く](../recipes/write-docs.md)<!-- link:end --> にある。

## 嫌な点は例で示す {#concrete-dislikes}

嫌な点を例で示すとは、直したい箇所を、実際の文を挙げて伝えることである。「もっと自然に」「もっとパンチを」のような形容詞は、Claude がどの箇所をどう変えればよいかを決められない。形容詞で頼んでも直らない理由はここにある。実践者の報告にも、形容詞ではなく具体例で嫌な点を伝えるほうがよい、という助言がある（根拠：弱。単独の実践者の経験談）。

形容詞の頼み方と、例で示す頼み方を並べる。

```text
Before：もっと自然な文章にして。
```

<!-- gen:begin snippet requesting-prose/dislike-examples -->
<!-- textlint-disable -->

???+ example "雛形：嫌な点を例で示して直させる依頼の雛形"

    ```text
    下の文章を直してください。直す前と後を並べ、変えた箇所に一言の理由を付けてください。

    嫌な点（実際の文で示します）：
    - 〔例：「〜という点が挙げられます」が硬い。→「〜です」のように短くしたい〕
    - 〔例：段落の終わりが毎回「非常に重要です」になる。→ 何が重要かを一言で書きたい〕
    - 〔例：3 つ目の嫌な点があれば。直す前と後の対で〕

    上の例に当たらない箇所は変えないでください。内容と事実は変えません。

    【文章】
    〔直したい文章を貼る〕
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet requesting-prose/dislike-examples -->

上の雛形が After である。Before から足したものは 3 つある。

- **嫌な箇所の実例**：「〜という点が挙げられます」のように、実際の文を引く。形容詞の「硬い」より、どの文がどう硬いかが分かる。
- **直した後の形**：嫌な点だけでなく、代わりにしたい言い方を対にする。避けたい形だけを渡すと、別の型どおりの形が出やすい。
- **範囲の限定**：例に当たらない箇所は変えない。直さなくてよい箇所を守れる。

文章が「AI っぽい」と感じたときも、同じ手順で扱う。判断の基準は、読み手にとって読みにくいかどうかである。AI らしさそのものは基準にしない。型どおりの言い回しが続く、飾りが多くて中身が薄い、といった読みにくさは、実際の文を挙げて直せる。公式のモデル別の手引きにも、文章が密すぎるときに、装飾的な文体を外すよう一文で頼む例がある。日本語に固有の癖は、<!-- link:begin less-ai-sounding-japanese#patterns -->[日本語の「AI 臭さ」を減らす › 読みにくさの型を具体的に挙げる](../japanese/less-ai-sounding-japanese.md#patterns)<!-- link:end --> に型として挙がっている。

!!! example "判断例：手本を見せるか、嫌な言い回しを挙げるか"
    - **状況**：週報の下書きを頼む。返ってきた文章は、どの段落も「〜という点が挙げられます」「非常に重要です」で終わっていて、自分の文体と違う。
    - **迷う候補**：自分の過去の週報を手本として貼る。または、嫌な言い回しを 3 つ挙げて、代わりの言い方と対にして渡す。
    - **選んだもの**：手元に気に入った過去の週報があれば手本を貼り、なければ嫌な言い回しを挙げる。手本があっても、直らない言い回しが残れば、その分だけ例を足す。
    - **理由**：手本は、挙げ切れない好みまで一度に伝える。一方、手本がない人や、手本に直したい癖が混ざっている人には、嫌な言い回しの例のほうが確実に効く。どちらも、形容詞より具体的である。

## 推敲を別の手順に分ける {#revise}

推敲を別の手順に分けるとは、下書きを書かせる依頼と、直させる依頼を分けることである。1 回の依頼で「書いて、読みやすくして」と頼むと、書くことと直すことが混ざり、どちらの観点も浅くなる。手順は次のとおり。

1. **下書きを書かせる**。読み手・目的・分量・手本を渡す。確かめ：下書きが目的に合う構成か。文体の細かい直しは、この段では見ない。
2. **観点を 1 つに絞って直させる**。重複する文を削る、1 文を短くする、嫌な言い回しを置き換える、のどれか 1 つにする。確かめ：直す前と後が並んで返り、変えた箇所に一言の理由が付いているか。
3. **観点を替えて繰り返す**。次の観点へ進む前に、前の直しで内容が変わっていないかを読む。確かめ：事実と数字が材料と一致しているか。

直させる依頼の雛形を置く。

<!-- gen:begin snippet requesting-prose/revise-pass -->
<!-- textlint-disable -->

??? example "雛形：観点を 1 つに絞って推敲させる依頼の雛形"

    ```text
    下の下書きを推敲してください。内容と事実は変えません。

    この回の観点は〔1 つだけ。例：重複している文を削る／1 文を 60 字以内に短くする〕です。
    ほかの観点は、今回は見ないでください。
    直した箇所は、直す前と後を並べて示し、変えた理由を一言ずつ付けてください。

    【下書き】
    〔下書きを貼る〕
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet requesting-prose/revise-pass -->

観点を絞るのは、1 回の依頼に直しを詰めると、直す箇所が増えて差分を読み切れなくなるからである。推敲を書く手順と分ける考え方は、<!-- link:begin less-ai-sounding-japanese#revise-step -->[日本語の「AI 臭さ」を減らす › 推敲を書く手順と分ける](../japanese/less-ai-sounding-japanese.md#revise-step)<!-- link:end --> にある。

## 確かめ方 {#check}

文章全体の確かめは、読み手の側から行う。次の 3 つを順に見る。

1. **目的に答えているか**：依頼に書いた「読んだ後に何をしてほしいか」が、最初の段落で分かるかを読む。
2. **事実が材料と合うか**：数字・固有名詞・日付を、材料と 1 つずつ照らす。材料にない記述は削るか、出所を確かめる。
3. **文体が揃っているか**：です・ます調とだ・である調の混在のような機械で見つかるものは、道具に任せる。方法は <!-- link:begin consistent-politeness#lint -->[です・ます／だ・であるを揃える › 混在を lint で見つける](../japanese/consistent-politeness.md#lint)<!-- link:end --> にある。

好みの合否は、機械では決まらない。声に出して読み、自分が書いたものとして出せるかを自分で判断する。

## 失敗したとき {#failure}

直らないときは、症状から次のように振り分ける。

- **手本の内容まで似てしまう**：手本の言い回しや構成がそのまま写る。手本を複数にして、共通する文体だけを真似るよう頼む。詳しくは <!-- link:begin show-examples#overfit -->[例を見せる › 例にだけ合う出力に気をつける](show-examples.md#overfit)<!-- link:end --> にある。
- **直すたびに別の癖が出る**：嫌な点を足し続けるより、観点を 1 つだけにした推敲へ戻す。それでも直らなければ、新しいセッションで下書きからやり直す。
- **長さが合わない**：分量の指定の書き方を見直す。考え方は <!-- link:begin output-shape#length -->[出力の形と分量を指定する › 長さと要約の有無](output-shape.md#length)<!-- link:end --> にある。
- **文体が揺れる**：文体を一行で指定し、置き場所を見直す。手順は <!-- link:begin consistent-politeness#failure -->[です・ます／だ・であるを揃える › 揺れが残ったとき](../japanese/consistent-politeness.md#failure)<!-- link:end --> にある。
- **日本語の型が残る**：定型の言い回しや漢字の多さは、日本語の型として挙げて直させる。手順は <!-- link:begin less-ai-sounding-japanese#failure -->[日本語の「AI 臭さ」を減らす › 失敗したとき](../japanese/less-ai-sounding-japanese.md#failure)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [27 Claude tips after 1,800 hours.](https://ruben.substack.com/p/1800-hours-of-claude)：Ruben Hassid・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [例を見せる](show-examples.md)

**次に読む**

- [日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)

**関連**

- [出力の形と分量を指定する](output-shape.md)
- [ドキュメント・技術文書を書く](../recipes/write-docs.md)
- [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)
- [AI 利用の開示と出所の記録](../safety/disclosure-and-provenance.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
