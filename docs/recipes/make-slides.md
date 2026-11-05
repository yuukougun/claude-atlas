---
id: make-slides
title: 資料・スライドを作る
aliases: [プレゼン資料, 発表資料, スライドのたたき台, Marp]
type: recipe
field: recipes
chapter: 調べものと文書
order: 180
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [見せる, 握る]
prevents: [見えていない]
scenes: [文章, チーム]
summary: 発表資料やスライドを、伝えたい筋と聞き手を先に決めてから作らせる。たたき台は Claude に任せ、主張と数字の確認と最後の仕上げは人が行う。
signs:
  - {type: goal, text: 説明用のスライドのたたき台を早く作りたい}
  - {type: goal, text: Markdown の原稿からスライドを作りたい}
  - {type: symptom, text: 作らせたスライドは見栄えがよいが、中身が薄い}
prerequisites: [artifacts-overview, fact-checking]
related: [looks-are-not-quality, peripheral-products#office-add-ins, files-and-code-execution, write-docs, research-and-reports, frontend-design, less-ai-sounding-japanese, ai-ideas-are-everyones]
tracks: [artifacts, office-add-ins, file-creation]
sources: [hc-artifacts, claude-docs-m365-powerpoint, hc-files]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guard}
  - {title: 手順, anchor: steps}
  - {title: 作る手段の選び方, anchor: tools}
  - {title: 確かめ方, anchor: verify}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：筋と聞き手を先に渡してスライドのたたき台を作らせ、主張と数字の確認と最後の仕上げを人が握れる。
    - **いつ引くか**：説明用のスライドのたたき台を早く作りたいとき。Markdown の原稿からスライドを作りたいとき。作らせたスライドが見栄えはよいのに中身が薄いとき。
    - **前提**：<!-- link:begin artifacts-overview -->[アーティファクト（会話の中で作る文書・スライド・デザイン）](../app/artifacts-overview.md)<!-- link:end -->・<!-- link:begin fact-checking -->[事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)<!-- link:end -->

<!-- textlint-disable -->
別名：プレゼン資料・発表資料・スライドのたたき台・Marp
<!-- textlint-enable -->

資料・スライドを作らせるとは、発表の筋と聞き手を人が決め、枚数分の下書きと体裁を Claude に任せることである。「スライドを作って」とだけ頼むと、見栄えのよい一般論が返りやすい。Claude には聞き手も発表の場も見えておらず、何を持ち帰らせたいのかも分からないからである。筋と聞き手を渡し、主張と数字は人が確かめ、最後は人が仕上げる。この順で進める。

## 先に整える守り {#guard}

スライドを作らせる前に、人が決めておくことが 3 つある。任せる幅は、この守りに見合う範囲までにする。

1. 聞き手に持ち帰ってほしいこと。聞き手が誰で、何を知っていて、発表の後に何をしてほしいか。これが決まらないと、1 枚ごとの主張も決まらない。この辞典の原理でいう「見せる」（Claude に見えていない条件を見せる）に当たる。Claude に見えていない条件は、依頼に書いて見せる。
2. 1 枚ごとの主張。発表の判断や主張が自分のものなら、筋は自分で書く。Claude に任せてよいのは、筋の穴の指摘、順序の案、言い換えである。AI の案を起点にすると発想が似通う理由と、差が要る場面の扱いは <!-- link:begin ai-ideas-are-everyones#when-difference-matters -->[AI の案は「みんなの案」（均質化） › 差が要る場面と、底上げで足りる場面](../judgment/ai-ideas-are-everyones.md#when-difference-matters)<!-- link:end --> が持つ。
3. 確かめる担当は人であること。主張と数字の最終の判断は人が握る。これが原理でいう「握る」（判断を人の手に残す）に当たる。Claude の出した数字は、資料の原文と照らして確かめる。照らし方は <!-- link:begin fact-checking#quotes -->[事実を確かめる（引用・照合・best-of-N） › 主張ごとに引用させる](../verify/fact-checking.md#quotes)<!-- link:end --> が持つ。

整った見た目は、中身が正しい証拠にならない。見栄えのよいスライドほど、薄い中身が目に入りにくい。見た目の代わりに何を見るかは <!-- link:begin looks-are-not-quality#what-to-check -->[見た目は品質の証拠ではない › 見た目の代わりに見るもの](../verify/looks-are-not-quality.md#what-to-check)<!-- link:end --> が持つ。

## 手順 {#steps}

各段に、何で終わったかの確かめを付ける。確かめが通らなければ、次の段へ進まず、その段に戻る。

1. 聞き手と持ち帰ってほしいことを書く。確かめ：持ち帰ってほしいことを 1〜2 文で言える。言えないなら、発表の目的がまだ決まっていない。
2. 1 枚ごとの主張を並べる。タイトルだけの一覧でよい。確かめ：タイトルだけを順に読んで、筋が通る。話が飛ぶ所は、枚を足すか並べ替える。調べものを元にする発表では、先に <!-- link:begin research-and-reports#define-the-question -->[調べものとレポート › 問いと範囲を先に決める](research-and-reports.md#define-the-question)<!-- link:end --> で問いと範囲を決めておく。
3. 筋・聞き手・主張・使ってよい資料を渡して、たたき台を作らせる。依頼は下の雛形を使う。確かめ：資料にない数字には〔要確認〕の印が付く。主張と資料の箇所の対応表が返る。
4. 数字と主張を資料と照らす。確かめ：数字・固有名・日付のすべてに、資料の引用か「根拠なし」が付く。「根拠なし」は人が資料に当たって消すか、スライドから外す。
5. 見た目を整える。確かめ：実際に表示して、人の目で見る。手段ごとの違いは次の節にある。
6. 人が仕上げる。確かめ：話す順で通読し、聞き手の立場で分からない所を直す。足す・削るの判断は人が行う。

たたき台の依頼は、聞き手・持ち帰ってほしいこと・長さ・1 枚ごとの主張・資料をまとめて渡す型である。作る前に足りない条件を質問させると、Claude が条件を補って埋めてしまうことが減る。

<!-- gen:begin snippet make-slides/draft-request -->
<!-- textlint-disable -->

???+ example "雛形：筋・聞き手・1 枚ごとの主張を先に渡して、たたき台を作らせる依頼"

    ```text
    〔発表の名前〕のスライドのたたき台を作って。作る前に、次の条件を読んで、足りない点があれば先に聞いて。
    - 聞き手：〔誰が聞くか。立場と前提知識〕
    - 聞き手に持ち帰ってほしいこと：〔1〜2 文〕
    - 長さ：〔発表の分数〕、〔枚数の上限〕
    - 1 枚ごとの主張：
      1. 〔1 枚目の主張を 1 文で〕
      2. 〔2 枚目の主張を 1 文で〕
      3. 〔以下同じ〕
    - 使ってよい資料：〔添付やファイルの名前〕。資料にない数字や事実は書かず、〔要確認〕と印を付ける。

    作り方：
    - 各枚のタイトルは、その枚の主張を 1 文で書く。本文は、その主張の根拠だけにする。
    - 図や表にしたほうが伝わる枚は、どう見せたいかを一言添えて提案する。作らなくてよい。
    - 最後に、各枚の主張と、使った資料の箇所の対応表を出す。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet make-slides/draft-request -->

手順 4 の照合は、直す前に、見つかった点の一覧だけを返させる。直しも同時に頼むと、何が変わったのかが追えない。

<!-- gen:begin snippet make-slides/check-request -->
<!-- textlint-disable -->

??? example "雛形：作ったスライドを資料と照らして確かめさせる依頼"

    ```text
    作ったスライドを、渡した資料と照らして確かめて。直す前に、見つかった点の一覧だけを返す。
    1. 各枚の数字・固有名・日付を一覧にし、資料のどの箇所から取ったかを、原文の引用で横に書く。引用できないものは「根拠なし」と書く。
    2. 各枚の主張が、前の枚の主張から続いているかを見て、話が飛んでいる所を挙げる。
    3. 主張とタイトルが食い違っている枚があれば挙げる。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet make-slides/check-request -->

!!! example "判断例：筋が固まっていない発表の頼み方"
    - **状況**：社内の勉強会で、自分の調査の結果を発表する。手元に調査メモはあるが、何を結論にするかはまだ固まっていない。
    - **迷う候補**：メモを渡し、Claude に筋の案を複数出させてからスライドにする。あるいは、自分で筋と 1 枚ごとの主張を書いてから渡す。
    - **選んだもの**：自分で筋と主張を書き、Claude には筋の穴と順序の案だけを出させる。
    - **理由**：結論は発表者が責任を持つ判断であり、Claude が決めると、自分の調査から離れた一般的な結論が出やすい。決めかねているだけなら、案を複数出させ、人が採るものを選ぶ使い方も筋が通る。その場合も、選んだ後の主張は自分の言葉で書き直す。

## 作る手段の選び方 {#tools}

スライドを作る手段は 3 つある。会話の中のアーティファクト、Microsoft 365 の PowerPoint のアドイン、ファイルの作成と編集である。使える面と成熟度は次の表のとおりで、選ぶ基準は表の下のタブに書く。

<!-- gen:begin compare 面 成熟度 -->
<!-- textlint-disable -->

| 機能 | 面 |
| --- | --- |
| [アーティファクト（artifacts）](../app/artifacts-overview.md) | アプリ・Claude Code |
| Claude for Microsoft 365 のアドイン（Excel・PowerPoint・Word・Outlook） | アプリ |
| [ファイルの作成と編集（create and edit files）](../app/files-and-code-execution.md) | アプリ |

すべて共通：成熟度 GA。

<!-- textlint-enable -->
<!-- gen:end compare 面 成熟度 -->

=== "アプリ"
    アプリでは 3 つの手段のどれも使える。

    - アーティファクトは、会話の中でスライドを作り、直し、共有できる。会話で直しながら筋を詰めたいときに向く。テンプレートの選び方は <!-- link:begin artifacts-overview#templates -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › テンプレートの選び方](../app/artifacts-overview.md#templates)<!-- link:end -->、直し方は <!-- link:begin artifacts-overview#editing -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › 直し方（頼む・直接直す・範囲を選ぶ）](../app/artifacts-overview.md#editing)<!-- link:end -->、公開の注意は <!-- link:begin artifacts-overview#sharing -->[アーティファクト（会話の中で作る文書・スライド・デザイン） › 公開と共有](../app/artifacts-overview.md#sharing)<!-- link:end --> が持つ。
    - PowerPoint のアドインは、既存のテンプレートでスライドを作り、特定のスライドだけを直し、箇条書きを図やグラフにできる。会社のテンプレートに載せたいときに向く。位置づけと確認日つきの一覧は <!-- link:begin peripheral-products#office-add-ins -->周辺製品の一覧<!-- link:end --> が持つ。
    - ファイルの作成は、スライドのファイルを作らせて受け取る。受け取り方と実行環境の注意は <!-- link:begin files-and-code-execution#outputs -->[ファイル作成とコード実行 › 作ったファイルの受け取り方](../app/files-and-code-execution.md#outputs)<!-- link:end --> が持つ。

    どの手段でも、手順 1〜4 は同じである。変わるのは手順 5 の見た目の整え方だけである。

=== "Claude Code"
    Claude Code では、Markdown の原稿を書かせ、スライドへの変換は別の道具に任せる形が基本になる。変換の道具には Marp などがある。ここでは考え方の例として名前を出すだけで、その成熟度と使い方は確かめていない。

    - 原稿はリポジトリのファイルとして置く。差分で変更が見え、1 枚ごとの主張の並べ替えも追いやすい。
    - 手順 3 の依頼で、出力を Markdown の原稿にするよう指定する。1 枚の区切りは、使う変換の道具の書き方に合わせる。
    - 見た目の確認は、変換した結果を人が開いて行う。仕上がりを画像で見せて直させる進め方は <!-- link:begin frontend-design -->フロントエンドのデザイン<!-- link:end --> が持つ。

    Claude Code で、PowerPoint などのファイルを直接作らせる手順は、この辞典では確かめていない。

文章の読みやすさを整える作業は、スライドの本文にも当てはまる。定型の言い回しや装飾が気になるときは <!-- link:begin less-ai-sounding-japanese#patterns -->[日本語の「AI 臭さ」を減らす › 読みにくさの型を具体的に挙げる](../japanese/less-ai-sounding-japanese.md#patterns)<!-- link:end --> を使う。スライドの元になる文書を先に書く場合は <!-- link:begin write-docs -->[ドキュメント・技術文書を書く](write-docs.md)<!-- link:end --> が近い。

## 確かめ方 {#verify}

仕上げる前に、全体を 4 つの点で確かめる。

1. 主張ごとの根拠：各枚の主張に、資料の箇所を 1 つ指せる。指せない主張は、削るか、自分の意見だと分かる書き方にする。
2. 数字：数字・固有名・日付が、資料の原文と一致する。要約された数字は、必ず原文に戻る。要約を原文と照らす方法は <!-- link:begin fact-checking#summaries -->[事実を確かめる（引用・照合・best-of-N） › 要約を原文と照らす](../verify/fact-checking.md#summaries)<!-- link:end --> が持つ。
3. 筋：タイトルだけを順に読んで、持ち帰ってほしいことに届く。
4. 聞き手：発表の場にいない人が、スライド単体を読んで主張を取れるかを、別の人に見てもらう。自分では、作った筋に慣れて穴が見えない。

確かめ全体の進め方は <!-- link:begin fact-checking#overall-check -->[事実を確かめる（引用・照合・best-of-N） › 全体の確かめ方](../verify/fact-checking.md#overall-check)<!-- link:end --> が持つ。作らせた本人に採点させず、別の目で見る点は、ここでも同じである。

## 失敗したとき {#when-it-fails}

作らせたスライドが見栄えはよいのに中身が薄いときは、次の順で原因を探す。

- 1 枚ごとの主張を渡していなかった。手順 2 に戻り、タイトルだけの一覧を自分で書いてから、作り直させる。
- 使ってよい資料を渡していなかった。資料にない事実を、もっともらしく補っている。資料を渡し、資料にない内容は〔要確認〕と書かせる。うまくいかないときの切り分けは <!-- link:begin fact-checking#when-it-fails -->[事実を確かめる（引用・照合・best-of-N） › うまくいかないとき](../verify/fact-checking.md#when-it-fails)<!-- link:end --> にある。
- ほかの人のスライドと似た並びになる。AI の案は、ほかの人も得ている案である。差が要る発表では、上積みを自分で考える。判断は <!-- link:begin ai-ideas-are-everyones#check -->[AI の案は「みんなの案」（均質化） › 案が似ていないかの確かめ方](../judgment/ai-ideas-are-everyones.md#check)<!-- link:end --> が持つ。
- 見た目は整っているが、主張が弱い。体裁を直しても中身は直らない。手順 4 の照合をやり直し、根拠のない枚を外す。
- 文章が硬い、または定型に寄っている。<!-- link:begin less-ai-sounding-japanese#patterns -->[日本語の「AI 臭さ」を減らす › 読みにくさの型を具体的に挙げる](../japanese/less-ai-sounding-japanese.md#patterns)<!-- link:end --> の型で直させる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [アーティファクト（会話の中で作る文書・スライド・デザイン）](../app/artifacts-overview.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)

**関連**

- [見た目は品質の証拠ではない](../verify/looks-are-not-quality.md)
- [ファイル作成とコード実行](../app/files-and-code-execution.md)
- [ドキュメント・技術文書を書く](write-docs.md)
- [調べものとレポート](research-and-reports.md)
- [日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)
- [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)：Anthropic・英語・確認日 2026-11-04
- [Use Claude for PowerPoint](https://claude.com/docs/office-agents/powerpoint)：Anthropic・英語・確認日 2026-11-04
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
