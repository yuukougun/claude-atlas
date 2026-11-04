---
id: show-examples
title: 例を見せる
aliases: [few-shot, multishot, 例示, 手本を見せる]
type: concept
field: prompting
chapter: 頼み方の原則
order: 40
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない]
scenes: [文章, 開発, データ分析]
summary: 形や文体は言葉で説明するより、典型的で多様な例を見せるほうが揃う。自分の過去の文章やコードを手本にすると、言葉にしにくい好みまで伝わる。
signs:
  - {type: symptom, text: 説明しても、欲しい形式や文体にならない}
  - {type: goal, text: 自分の文体に近い文章を書かせたい}
prerequisites: [brief-a-new-colleague]
related: [four-specifics, consistent-politeness, requesting-prose, output-shape, xml-tags, less-ai-sounding-japanese, prompt-patterns]
sources: [api-docs-prompting-best-practices, arxiv-2403-08937, jinrai-claude-japanese]
volatility: 低
sections:
  - {title: 言葉の説明を例に替える, anchor: before-after}
  - {title: なぜ例が効くのか, anchor: why}
  - {title: 典型的で多様な例を選ぶ, anchor: choose}
  - {title: 何個見せるか, anchor: how-many}
  - {title: 自分の文章を手本にする, anchor: own-writing}
  - {title: 例にだけ合う出力に気をつける, anchor: overfit}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：形や文体は、言葉で説明するより、典型的で多様な例を見せるほうが揃う。
    - **いつ引くか**：説明しても、欲しい形式や文体にならないとき。自分の文体に近い文章を書かせたいとき。
    - **前提**：<!-- link:begin brief-a-new-colleague -->[新人の同僚に頼むつもりで](brief-a-new-colleague.md)<!-- link:end -->

<!-- textlint-disable -->
別名：few-shot・multishot・例示・手本を見せる
<!-- textlint-enable -->

例を見せるとは、依頼の中に「この入力にはこの出力」という実物を添えることである。形式・文体・分類の基準のように、言葉にすると長くなる好みを伝えるときに効く。このページでは、例の選び方と数の考え方、自分の文章を手本にする使い方、例に引きずられる失敗を扱う。

## 言葉の説明を例に替える {#before-after}

形や文体の注文を、形容詞で書く代わりに、できあがりの実物で見せる。同じリリースノートの依頼で比べる。

Before は、形式を形容詞で説明した依頼である。

```text
次のコミットの一覧から、リリースノートを、簡潔で読みやすい形式で書いてほしい。
```

「簡潔」と「読みやすい」が指す形は、書き手ごとに違う。見出しを付けるか、文末を「した」で終えるか、1 項目を何行にするかは、依頼から読み取れない。Claude は、それを推測で埋める。

After は、同じ依頼に典型的で種類の違う例を 2 件添えたものである。

<!-- gen:begin snippet show-examples/release-notes -->
<!-- textlint-disable -->

??? example "雛形：典型的で多様な例を添えた、リリースノートの依頼"

    ```text
    次のコミットの一覧から、リリースノートを書いてほしい。形式は <examples> の例に合わせる。

    <examples>
    <example>
    <commits>
    fix: 日付の読み取りで 2 月 29 日が 28 日になる
    feat: CSV の出力に BOM 付きの選択肢を追加
    </commits>
    <release_note>
    ### 修正
    - 日付の読み取りで、うるう年の 2 月 29 日が 28 日になる問題を直した。

    ### 追加
    - CSV の出力で、BOM 付きを選べるようにした。
    </release_note>
    </example>
    <example>
    <commits>
    revert: 検索の並べ替えの変更を取り消す
    docs: README のインストール手順を更新
    </commits>
    <release_note>
    ### 変更
    - 検索の並べ替えを、前の動作に戻した。

    ### ドキュメント
    - README のインストール手順を更新した。
    </release_note>
    </example>
    </examples>

    <commits>
    ここに今回のコミットの一覧を貼る
    </commits>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet show-examples/release-notes -->

After で足したものは次の 3 つである。

- 出力の形を、例の `<examples>` に合わせると書いた。
- 例を、通常の修正・追加と、取り消し・文書の更新という種類の違うコミットから選んだ。
- 例を `<example>` で 1 件ずつ囲み、入力と出力の組を取り違えにくくした。囲み方は <!-- link:begin xml-tags#separate -->XML タグで区切る › 指示・資料・例を分ける（準備中）<!-- link:end --> にある。

何が変わるかを一言で言うと、形式の説明が要らなくなる。見出しの数、文末、箇条書きの粒度は、例が持っている。形容詞で頼んだときのずれを、例を足すことで減らせる。

## なぜ例が効くのか {#why}

このページが扱う原理は「見せる」で、防ぐ原因は「見えていない」である。

Claude には、依頼の外にあるあなたの好みが見えていない。リリースノートの書き方も、文体の癖も、頭の中にあるだけでは届かない。言葉で説明すると、書き手が好みを残らず言語化する必要がある。「簡潔」のような形容詞は、言語化したつもりでも、程度や形を決めない。

例は、形・長さ・語調・粒度をまとめて見せる。言葉にできない好みも、例の中に入っている。文脈を知らない新人の同僚に過去の資料を渡して「こう書いてほしい」と頼むのと同じである。この見方は <!-- link:begin brief-a-new-colleague#colleague-test -->[新人の同僚に頼むつもりで › 文脈のない同僚に見せて確かめる](brief-a-new-colleague.md#colleague-test)<!-- link:end --> にある。

公式の文書も、例を示すと精度と一貫性が上がるとする。勧めるのは、関連性があり、多様で、構造化された例である（[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)）。

例の中身を Claude がどう処理するかという内部の動きは、この頁では断定しない。確かめられるのは、例を足した前後で出力がどう変わるかである。

## 典型的で多様な例を選ぶ {#choose}

例は、実際の入力に似ていて、種類にばらつきがあり、同じ形で区切られたものを選ぶ。公式の文書の 3 つの条件（関連性・多様性・構造）は、次の 3 項目に当たる。

- **典型的であること**：本番でいちばん多い入力に近い例を中心にする。珍しい入力ばかりを見せると、それが標準の形だと受け取られやすい（推論・実践例なし）。
- **多様であること**：種類・長さ・難しさをばらつかせる。1 種類の入力だけを見せると、どの入力にも同じ形の出力を返しやすい。分類の依頼なら、ラベルごとに 1 件は入れ、境界に近い入力も混ぜる。
- **構造をそろえること**：入力と出力の組を同じ形で並べ、区切りを付ける。区切りの付け方は <!-- link:begin xml-tags#separate -->XML タグで区切る › 指示・資料・例を分ける（準備中）<!-- link:end --> を使う。
- **出力を、欲しい形そのものにすること**：例の出力にある誤りや癖も、写されうる。見せる前に、直したものに替える。

データ分析の例では、集計結果の見せ方（表の列、数値の丸め、1 行の所見）を例にするとそろえやすい。開発の例では、既存のコードの書き方を手本にする。後者は <!-- link:begin four-specifics#model -->[具体性の 4 点（対象・状況・完了・手本） › 手本：倣う既存のコードや文章](four-specifics.md#model)<!-- link:end --> にある。

!!! example "判断例：問い合わせの分類に添える例"
    - **状況**：届いた問い合わせを、ラベルに分けさせたい。実際の問い合わせは、ほとんどが 2 つの種類に集中し、残りのラベルはまれである。
    - **迷う候補**：実際の入力から、似た種類の例を多く選ぶ。または、ラベルごとに 1 件ずつ、まれなラベルまで入れる。
    - **選んだもの**：多い種類の例を中心にして、まれなラベルを 1 件ずつ足す。
    - **理由**：多い種類で外すと、誤りの件数が全体でいちばん増えるからである。一方で、まれなラベルの例が 1 件もないと、その種類は説明なしで当てることになる。

## 何個見せるか {#how-many}

例の数は、少数で足りることが多い。公式の文書は勧める個数を示している（個数は上の参考の公式の文書で確かめる）。個数そのものより、実際の入力の種類を覆えているかで決める。

- 1 件だけだと、その例の言い回しや構成をそのまま写しやすい。種類の違う例を足すと、共通する形だけが残る。
- 出力が例の 1 件に似すぎるときは、例を差し替えるか、種類を足す。
- まだ形がずれるときは、ずれる種類の入力と、その正しい出力を 1 組足す。例を増やす前に、ずれた出力と欲しい出力の差を見る。
- 例をむやみに増やすと、依頼が長くなり、本題の指示が埋もれる。足すのは、ずれを直す例だけにする。

手持ちの例が足りているかは、Claude に点検させてもよい。公式の文書も、例が適切かの評価と、追加の例の作成を Claude にさせてよいとしている。点検の依頼の雛形を置く。

<!-- gen:begin snippet show-examples/review-examples -->
<!-- textlint-disable -->

??? example "雛形：用意した例を Claude に点検させ、足りない例を作らせる依頼"

    ```text
    これから、<task> の作業を頼むために使う例を <examples> に貼る。例として適切か点検してほしい。

    見てほしい点：
    - 実際の入力に似ているか（典型的か）。
    - 種類・長さ・難しさがばらついているか。足りない種類があれば挙げる。
    - 例どうしで、出力の形や判断の基準が食い違っていないか。

    そのうえで、足りない種類の例を、同じ形式で追加で作ってほしい。作った例は私が確かめてから採用するので、<proposed_examples> に分けて出す。

    <task>
    ここに、例を使って頼むつもりの作業を一文で書く
    </task>

    <examples>
    ここに、用意した例を貼る
    </examples>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet show-examples/review-examples -->

Claude が作った例は、そのまま採用しない。自分で読んで、欲しい形そのものになっているものだけを使う。

## 自分の文章を手本にする {#own-writing}

文体の好みは、規則にすると長くなる。語尾、漢字の開き方、段落の長さ、言い切りの強さは、自分が満足した過去の文章を貼るのが早い。

日本語では、Claude の返答は漢字の比率が高くなりがちで、です・ます調を明示しないと途中で揺れるという実践者の報告がある。対策は、表記ルールを書くことと、自分の文章を Few-shot で見せることである（根拠：弱。単独の実践者の報告）。表記ルールの書き方は <!-- link:begin consistent-politeness#specify -->[です・ます／だ・であるを揃える › 文体は一行で、理由と一緒に指定する](../japanese/consistent-politeness.md#specify)<!-- link:end --> が扱う。

手本を渡す手順は次のとおりである。

1. 自分で書いて満足した文章を選ぶ。読み手と用途は、今回の文章と近いものにする。
2. 手本を区切って貼る。依頼の指示と、手本の中の文を取り違えさせないためである。
3. 何を真似るかを一言で書く。「文体と段落の作りを真似る。内容は写さない」のように、写してほしいものと写さないものを分ける。
4. 手本から読み取りにくい決まり（です・ます調の統一など）は、手本とは別に一行で書く。

雛形を置く。

<!-- gen:begin snippet show-examples/own-writing -->
<!-- textlint-disable -->

??? example "雛形：自分の過去の文章を手本にする依頼"

    ```text
    社内向けの週報の下書きを書いてほしい。文体と段落の作りは、<sample> の文章に合わせる。内容は <sample> から写さない。

    <sample>
    ここに、自分が書いて満足した過去の週報を貼る
    </sample>

    <notes>
    ここに今週の出来事をメモのまま貼る
    </notes>

    書き終えたら、<sample> と違う点（語尾・段落の長さ・漢字の開き方）があれば、箇条書きで挙げてほしい。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet show-examples/own-writing -->

手本の渡し方は、面で変わる。

=== "アプリ"

    依頼の本文に手本を貼る。手本が長いときは、ファイルとして添える。続けて使う手本は、Projects の資料に置く方法もある（面ごとの置き方は未確認）。

=== "Claude Code"

    手本になる文章やコードのファイルを、パスで指して読ませる。「`docs/guide.md` の書き方に合わせて」のように、倣う対象を名指しする。

=== "API"

    プロンプトの中に、`<examples>` で囲んだ手本を入れる。手本をいつも使うなら、システムプロンプトの側に固定で置く。

日本語の文体をそろえる使い方は <!-- link:begin less-ai-sounding-japanese#own-writing -->[日本語の「AI 臭さ」を減らす › 自分の文章を手本にする](../japanese/less-ai-sounding-japanese.md#own-writing)<!-- link:end --> が持つ。嫌な言い回しを例で示す方法は <!-- link:begin requesting-prose#concrete-dislikes -->[文章を頼むとき（読み手・目的・手本を渡す） › 嫌な点は例で示す](requesting-prose.md#concrete-dislikes)<!-- link:end --> にある。手本の文章は、書いた本人の癖や誤りも含む。気に入らない癖は、手本から外すか、別に直す指示を書く。社外に出せない文章を貼る前には、使っている面での扱いを確かめる。

## 例にだけ合う出力に気をつける {#overfit}

例を見せると、その例にだけ合う出力が返りうる。例は形を伝えるための道具で、答えの範囲を決めるものではない。

Tambon らの研究（2024 年、arXiv）は、LLM が書いたコードのバグ 333 件を分類した。その類型の 1 つに、プロンプトの例にしか合わないコードがある（根拠：中）。研究時点のモデルの結果で、現行の Claude に当てはまるかは確かめていない。コードに限らず、文章でも、例の固有名や言い回しがそのまま出力に混ざる形で現れうる。

防ぎ方は次の 3 つである。

- 例を多様にする。1 種類だけの例は、その種類だけが正解だと見せることになる（推論・実践例なし）。
- 「例は形を示すもので、内容は入力から作る」と一行で書く（推論・実践例なし）。
- 例に使わなかった入力で試す。空の入力、極端に長い入力、境界の入力を選ぶ。例に使った入力で試しても、例に合っていることしか分からない。

## 効かない場面とやりすぎ {#limits}

例を見せても効きにくい場面は、次のとおりである。

- **規則が一文で言えるとき**：「箇条書きにしない」のような単純な指定は、言葉で書くほうが短い。例を付けると、望まない部分まで写される。
- **形式を必ず守らせたいとき**：例は強制ではなく、お願いにとどまる。機械が読む出力で形を保証したいときは、<!-- link:begin output-shape#guaranteed -->[出力の形と分量を指定する › 必ず守らせたい形式は仕組みで](output-shape.md#guaranteed)<!-- link:end --> の仕組みを使う。
- **例と指示が食い違うとき**：どちらに従うか分からなくなる。例を作った後で指示を変えたら、例も直す。
- **例が長すぎるとき**：本題の指示が埋もれる。例は短くし、長い資料は別に区切って渡す。

例を見せても形が揃わないときは、まず例が典型的か、多様か、出力の形がそろっているかを見直す。それでもずれるなら、ずれる箇所を言葉で足す。呪文のように例を増やし続けない。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Bugs in Large Language Models Generated Code: An Empirical Study](https://arxiv.org/abs/2403.08937)：arXiv（Tambon, Florian ほか）・英語・確認日 2026-11-04
- [Claude日本語精度｜ChatGPT・Gemini比較と自然な出力のコツ](https://jinrai.co.jp/blog/2026/03/26/claude-japanese/)：仁頼・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [新人の同僚に頼むつもりで](brief-a-new-colleague.md)

**次に読む**

- [文章を頼むとき（読み手・目的・手本を渡す）](requesting-prose.md)
- フロントエンドのデザイン（準備中）
- ドキュメント・技術文書を書く（準備中）

**関連**

- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)
- [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)
- [出力の形と分量を指定する](output-shape.md)
- XML タグで区切る（準備中）
- [日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)
- 用途別プロンプトの型（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
