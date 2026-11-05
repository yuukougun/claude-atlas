---
id: write-docs
title: ドキュメント・技術文書を書く
aliases: [README を書かせる, 設計書を書かせる, API の説明を書かせる, コメントや docstring の生成]
type: recipe
field: recipes
chapter: 調べものと文書
order: 170
level: 整える
priority: 推奨
surfaces: [claude-code, app]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
scenes: [文章, 開発]
summary: README や設計文書などの技術文書を、プロジェクトの既存の文書と規約を手本に見せて書かせる。内容はコードと照らして確かめ、文体と表記は検査の道具でそろえる。
signs:
  - {type: goal, text: コードに合った README や設計書を書かせたい}
  - {type: symptom, text: 書かせた文書が、コードの実際の動きと合っていない}
  - {type: goal, text: プロジェクトの文書の文体と用語を、既存の文書にそろえたい}
prerequisites: [show-examples, consistent-politeness, fact-checking]
related: [requesting-prose, less-ai-sounding-japanese, consistent-notation, textlint-hook, documents-in-japanese, artifacts-overview, commit-and-comment-language, research-and-reports, make-slides, record-decisions, explore-a-codebase, notes-and-pkm]
sources: [cc-docs-common-workflows]
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 手順, anchor: steps}
  - {title: 理由と意図はコードにない, anchor: intent}
  - {title: 全体の確かめ方, anchor: overall-check}
  - {title: うまくいかないとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：既存の文書と規約を手本に見せて書かせ、内容をコードと照らして確かめ、文体と表記は検査の道具でそろえる。
    - **いつ引くか**：コードに合った README や設計書を書かせたいとき。書かせた文書が、コードの実際の動きと合っていないとき。文書の文体と用語を、既存の文書にそろえたいとき。
    - **前提**：<!-- link:begin show-examples -->[例を見せる](../prompting/show-examples.md)<!-- link:end -->・<!-- link:begin consistent-politeness -->[です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)<!-- link:end -->・<!-- link:begin fact-checking -->[事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)<!-- link:end -->

<!-- textlint-disable -->
別名：README を書かせる・設計書を書かせる・API の説明を書かせる・コメントや docstring の生成
<!-- textlint-enable -->

ドキュメント・技術文書を書かせる作業は、README や設計書、API の説明、コメントや docstring を Claude に書かせる場面を扱う。Claude は文書をそれらしく書けるが、頼まなければ、プロジェクトの文体も、コードの実際の動きも見ていない。このページは、手本を見せて書かせ、書かれた内容をコードで確かめ、文体の揺れを検査の道具で拾うまでの進め方を示す。日本語の文体や表記そのものの直し方は、関連のページに任せる。

## 先に整える守り {#guards}

文書を書かせる前に、守りを 3 つ置く。1 つ目は手本と規約を Claude から見える形にすること、2 つ目は機械で見つけられる揺れを検査へ回すこと、3 つ目は内容の正しさをコードで確かめる前提に立つことである。

- **見えていない（原理は見せる）**：Claude は、頼まれなければ、既存の文書の文体も用語の使い方もコードの動きも読まない。「プロジェクトの文体で」と言葉で頼むより、手本の文書を実際に開かせるほうが揃う。プロジェクトの既存の文書は、自分の過去の文章という手本に当たる。手本の選び方は <!-- link:begin show-examples#own-writing -->[例を見せる › 自分の文章を手本にする](../prompting/show-examples.md#own-writing)<!-- link:end --> を見る。
- **縛っていない（原理は縛る）**：文体と用語の指示は、書いている途中で揺れる。揺れは指示を増やして直さず、検査の道具で見つけて直させる。文体は一行で指定し、毎回読まれる場所に置く。置き場所は <!-- link:begin consistent-politeness#where -->[です・ます／だ・であるを揃える › 置き場所（アプリの指示・スキル・CLAUDE.md・出力スタイル）](../japanese/consistent-politeness.md#where)<!-- link:end --> にある。書いた直後に検査を走らせる仕組みは <!-- link:begin textlint-hook#post-tool-use -->[textlint をフックで回す › 書いた後に走らせて差し戻す](../japanese/textlint-hook.md#post-tool-use)<!-- link:end --> にある。
- **内容は検査の道具では拾えない**：文体の検査が通っても、コードにない既定値やコマンドが書かれた文書は通る。内容の正しさは、コードと照らして確かめる。根拠を主張ごとに引かせる方法は <!-- link:begin fact-checking#quotes -->[事実を確かめる（引用・照合・best-of-N） › 主張ごとに引用させる](../verify/fact-checking.md#quotes)<!-- link:end --> を見る。

一括で大量の文書を書かせるほど、この 3 つが先に要る。任せる幅を広げる前に、手本と照合と検査を 1 本の文書で動かしておく。

## 手順 {#steps}

公式の [Common workflows](https://code.claude.com/docs/en/common-workflows) は、文書化の流れを、文書のない関数を見つける・docstring などを生成する・例を足す・プロジェクトの標準と照らす、の順で示している。ここでは、その「標準と照らす」を、手本の文書とコードを使う手順へ広げる。各段の終わりに、次へ進む前の確かめを置く。

**手順 1：書く文書と読み手を決める。**　何の文書か（README・設計書・API の説明・docstring）、誰が読むか、どこまで書くかを、1〜2 文で決める。読み手と目的を渡す頼み方は <!-- link:begin requesting-prose#reader -->[文章を頼むとき（読み手・目的・手本を渡す） › 読み手と目的を渡す](../prompting/requesting-prose.md#reader)<!-- link:end --> にある。終わりの確かめ：この文書を読んだ人が何をできるようになるかを、1 文で言える。

**手順 2：手本・規約・コードを見せて書かせる。**　手本の既存文書、規約（文体と用語集）、照らすコードの 3 つを依頼に書く。面によって、渡し方が違う。

=== "アプリ"

    手元のリポジトリを Claude が自動で読む前提にせず、手本の文書と照らすコードを会話に貼るか、添付して渡す。渡していないコードは照合できないので、渡した範囲を依頼に書き、範囲の外の記述は「要確認」にさせる。アプリでのファイルの読み込みの細部は、この辞典では未確認である。会話の中で文書を作り、直す方法は <!-- link:begin artifacts-overview -->[アーティファクト（会話の中で作る文書・スライド・デザイン）](../app/artifacts-overview.md)<!-- link:end --> にある。

=== "Claude Code"

    リポジトリのルートで起動し、手本と規約とコードのパスを依頼に書く。書かれたパスのファイルは、Claude Code が自分で開いて読む。文体の規約は `CLAUDE.md` に一行で置くと、依頼のたびに書かなくてよい。コメントや docstring の言語は、チームの決まりとして共有の指示に置く。分け方は <!-- link:begin commit-and-comment-language#team-vs-personal -->[コミットメッセージ・コメントの言語 › チームの決まりと個人の好みを分ける](../japanese/commit-and-comment-language.md#team-vs-personal)<!-- link:end --> にある。

依頼の型は次のとおりである。括弧の例を、自分の文書とコードに書き換えて使う。

<!-- gen:begin snippet write-docs/write-from-model -->
<!-- textlint-disable -->

??? example "雛形：既存の文書を手本に渡して、技術文書を書かせる依頼"

    ```text
    【書いてほしい文書】
    （例：このリポジトリの README の「使い方」の節。対象は、初めてこのリポジトリを触る開発者）

    【手本にする既存の文書】
    （例：docs/setup.md と docs/architecture.md。文体・見出しの付け方・用語はこれに合わせる）

    【規約】
    （例：CONTRIBUTING.md の「文書の書き方」の節。用語集は docs/glossary.md）

    【照らすコード】
    （例：src/cli/ と pyproject.toml。コマンド名・引数・既定値は、ここにあるものだけを書く）

    進め方：
    1. 手本の文書の文体・見出しの粒度・用語の使い方を、先に 5 行以内でまとめる。
    2. 文書を書く。コードにない動作や設定は書かない。コードから読み取れなかった所は、推測で埋めず「要確認」と書く。
    3. 書いた後に、文書の記述ごとに、それを裏づけるコードのファイルと行を並べる。裏づけのない記述は別に挙げる。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet write-docs/write-from-model -->

終わりの確かめ：返答の最初にある手本の文体のまとめが、手本の文書と合っている。合っていなければ、書かせる前に手本を選び直す。

**手順 3：記述ごとの根拠を、コードで開いて確かめる。**　手順 2 の依頼の型にある「進め方」の 3 で、記述ごとに裏づけのファイルと行が並ぶ。この一覧は Claude の自己申告なので、数か所を実際に開いて確かめる。書いた会話の中で「合っているか」と聞き直しても、同じ思い込みが返りやすい。確かめは新しい会話に分け、書いた文書とコードだけを渡して食い違いを挙げさせる。

<!-- gen:begin snippet write-docs/doc-code-mismatch -->
<!-- textlint-disable -->

??? example "雛形：書いた文書とコードの食い違いを挙げさせる依頼"

    ```text
    次の文書を、コードと照らして確かめてほしい。文書は直さず、食い違いの一覧だけを返す。

    【確かめる文書】
    （例：README.md の「使い方」と「設定」の節）

    【照らすコード】
    （例：src/ 全体と pyproject.toml）

    【手本にする既存の文書】
    （例：docs/architecture.md。文体・用語がこれと違う所も挙げる）

    一覧の形（表）：
    | 文書の記述（節と該当の文） | 種類 | コードの実際（ファイルと行） | 直し方の案 |

    種類は次の 4 つから選ぶ。
    - コードと違う：コマンド名・引数・既定値・手順が、コードと合わない
    - コードにない：コードに見つからない機能や設定が書かれている
    - 書かれていない：コードにあるのに、文書に出てこない引数や手順
    - 手本と違う：文体・見出し・用語が、手本の文書と揃っていない

    コードを開いて確かめられなかった記述は、表に入れず、最後に「確かめられなかった記述」として別に挙げる。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet write-docs/doc-code-mismatch -->

終わりの確かめ：表の指摘を 1 件ずつ開いて、採否を決めた。「確かめられなかった記述」は、自分でコードを開いて確かめるか、文書から外した。

**手順 4：文体と表記を、検査の道具でそろえる。**　文体の混在と表記の揺れは、辞書つきの lint で見つけて直させる。用語の一覧は人が持つ正本から作り、指示と検査に同じものを使う。方法は <!-- link:begin consistent-notation#single-source -->[表記ゆれと漢字の開き › 一覧を指示と lint の両方に使う](../japanese/consistent-notation.md#single-source)<!-- link:end --> と <!-- link:begin consistent-politeness#lint -->[です・ます／だ・であるを揃える › 混在を lint で見つける](../japanese/consistent-politeness.md#lint)<!-- link:end --> にある。終わりの確かめ：検査の指摘が 0 件になった。ただし、通っても内容が正しい証拠にはならない。

**手順 5：範囲を広げる。**　1 本の文書で手順 1〜4 が通ってから、同じ型で対象を広げる。広げ方の例を次に示す。

!!! example "判断例：docstring を付ける範囲"
    - **状況**：公開している関数が多いパッケージで、docstring のない関数に、まとめて docstring を付けたい。
    - **迷う候補**：全関数を一度に書かせて、あとで通して読む。公開の関数のうち数個だけ先に書かせ、手本と照合してから広げる。
    - **選んだもの**：数個だけ先に書かせて、手順 3 と手順 4 を通してから広げる。
    - **理由**：一度に書かせると、コードと食い違う記述が混ざっても、量が多くて見落としやすい。先に数個で型が通れば、同じ依頼と同じ検査で広げられる。全関数を一度に書かせても筋は通るが、そのときは確かめに使う時間を先に見積もる。

## 理由と意図はコードにない {#intent}

設計書の「なぜそうしたか」と「何を採らなかったか」は、コードを読んでも分からない。コードから読み取れるのは、何をしているかである。Claude に理由まで書かせると、コードに合う、もっともらしい理由が付く。それが実際の判断の理由かどうかは、コードからは確かめられない。

理由の材料は、commit のメッセージ・PR の説明・既存の決定の記録・議論の記録に残っている。これらを依頼に渡して、書かれていることだけを使わせる。材料がない理由は、推測で埋めず「要確認」と書かせ、人が書く。決定を文書に残す側の進め方は <!-- link:begin record-decisions -->[決定を文書に残す（ADR と週次アップデート）](../team/record-decisions.md)<!-- link:end --> にある。

!!! example "判断例：設計書の「採用しなかった案」の欄"
    - **状況**：既存のモジュールの設計書を、コードから書かせている。「採用しなかった案」の欄が空いている。
    - **迷う候補**：コードから推測して Claude に埋めさせる。材料がある分だけ渡して埋めさせ、残りは「要確認」にして人が書く。
    - **選んだもの**：材料がある分だけ埋めさせ、残りは人が書く。
    - **理由**：推測で埋めた欄は、読み手が実際の判断と区別できない。「要確認」と残した欄は、読み手と書き手の両方に、まだ分かっていないことが見える。

## 全体の確かめ方 {#overall-check}

手順ごとの確かめのあとで、文書全体を確かめる。Claude の根拠の一覧が整っていることと、文書が使えることは別だからである。

- 手順が書かれた文書（README の使い方など）は、書かれた順に実行する。壊れても困らない環境か、新しいクローンで行う。動かない手順は、文書が間違っている印である。
- 文書に出てくるコマンド名・引数・既定値・ファイル名を、コードで検索して実在を確かめる。検索で見つからない名前は、書き間違いか、コードにない機能である。
- 文書だけを読んだ人が、コードを開かずに作業を始められるかを確かめる。確かめ方の考え方は、決定の文書での確かめと同じである（<!-- link:begin record-decisions -->[決定を文書に残す（ADR と週次アップデート）](../team/record-decisions.md)<!-- link:end -->）。
- 文体と用語は、手順 4 の検査が 0 件であることを確かめる。検査が拾わない箇所（囲みの中の長い段落など）は、自分で読む。

コードが変わると、文書は古くなる。コードの差分を渡して、古くなる記述を挙げさせる方法もある。ただし、挙がらなくても古くなっていない証拠にはならないので、文書の持ち主が節ごとに見直す日を決めておく。

## うまくいかないとき {#when-it-fails}

症状ごとに、見るページが違う。

- コードと合わない記述が、直しても残る：範囲を狭め、記述ごとに根拠の引用を取り直す。進め方は <!-- link:begin fact-checking#when-it-fails -->[事実を確かめる（引用・照合・best-of-N） › うまくいかないとき](../verify/fact-checking.md#when-it-fails)<!-- link:end --> にある。
- 文書ごとに文体がばらばらになる：手本を 1〜2 本に絞り、文体の指定を毎回読まれる場所に置いたかを見る。<!-- link:begin consistent-politeness#failure -->[です・ます／だ・であるを揃える › 揺れが残ったとき](../japanese/consistent-politeness.md#failure)<!-- link:end --> に原因別の見方がある。
- 検査の道具では拾えない揺れが残る：機械で見つけられる範囲と判断の要る範囲を分ける。<!-- link:begin consistent-notation#failure -->[表記ゆれと漢字の開き › 失敗したとき](../japanese/consistent-notation.md#failure)<!-- link:end --> と <!-- link:begin textlint-hook#failure-and-few -->[textlint をフックで回す › フックが落ちたときと、規則を増やしすぎないこと](../japanese/textlint-hook.md#failure-and-few)<!-- link:end --> を見る。
- 定型の言い回しが多く、読みにくい：読みにくさの型を挙げて直させる。<!-- link:begin less-ai-sounding-japanese#patterns -->[日本語の「AI 臭さ」を減らす › 読みにくさの型を具体的に挙げる](../japanese/less-ai-sounding-japanese.md#patterns)<!-- link:end --> を見る。
- 日本語の PDF や社内文書を、材料として渡している：読めたかを先に確かめる。<!-- link:begin documents-in-japanese#pdf -->[日本語の資料を読ませる・書かせる › 日本語の PDF を渡す前と後に確かめること](../japanese/documents-in-japanese.md#pdf)<!-- link:end --> を見る。
- 上のどれにも当たらない、または原因が分からない：<!-- link:begin field:symptoms -->[症状辞典](../symptoms/index.md)<!-- link:end --> から、症状で引く。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Common workflows](https://code.claude.com/docs/en/common-workflows)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [例を見せる](../prompting/show-examples.md)
- [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)

**関連**

- [文章を頼むとき（読み手・目的・手本を渡す）](../prompting/requesting-prose.md)
- [日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)
- [表記ゆれと漢字の開き](../japanese/consistent-notation.md)
- [textlint をフックで回す](../japanese/textlint-hook.md)
- [日本語の資料を読ませる・書かせる](../japanese/documents-in-japanese.md)
- [アーティファクト（会話の中で作る文書・スライド・デザイン）](../app/artifacts-overview.md)
- [コミットメッセージ・コメントの言語](../japanese/commit-and-comment-language.md)
- [調べものとレポート](research-and-reports.md)
- [資料・スライドを作る](make-slides.md)
- [決定を文書に残す（ADR と週次アップデート）](../team/record-decisions.md)
- [知らないコードベースを読む](explore-a-codebase.md)
- ノート・PKM（Obsidian など）（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
