---
id: consistent-politeness
title: です・ます／だ・であるを揃える
aliases: [敬体と常体を揃える, 文体の統一, 文末が揺れる]
type: recipe
field: japanese
chapter: 文体と表記
order: 50
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる, 縛る]
prevents: [縛っていない, 見えていない]
scenes: [文章, 開発, チーム]
summary: 文体を一行で指定し、手本の文章を見せ、毎回読まれる場所に置くと揺れが減る。それでも揺れは残るので、混在は lint で見つけて直させる。
signs:
  - {type: goal, text: 文書を、です・ますか、だ・であるのどちらかに揃えたい}
  - {type: goal, text: チームの文書を、いつも同じ文体で書かせたい}
wave: 1
prerequisites: [align-japanese-output]
related: [inconsistent-japanese-style, consistent-notation, textlint-hook, show-examples, where-to-put-instructions, skills-in-the-app#migrated-styles, output-style-modes, less-ai-sounding-japanese, write-docs, requesting-prose, measure-changes]
tracks: [personal-instructions, project-instructions, app-skills, styles, claude-md, output-styles]
outdated_advice: [styles-for-tone]
sources: [cc-docs-memory, cc-docs-output-styles, hc-personalization, hc-skills-what, hc-styles-to-skills, zenn-yuki-a01e472d, jinrai-claude-japanese]
volatility: 中
sections:
  - {title: 先に決めておくこと, anchor: guards}
  - {title: 文体は一行で、理由と一緒に指定する, anchor: specify}
  - {title: 手本の文章を見せる, anchor: example}
  - {title: 置き場所（アプリの指示・スキル・CLAUDE.md・出力スタイル）, anchor: where}
  - {title: 混在を lint で見つける, anchor: lint}
  - {title: 揃ったかを確かめる, anchor: check}
  - {title: 揺れが残ったとき, anchor: failure}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：文体を一行で指定して手本を見せ、毎回読まれる場所に置くと揺れが減り、残った混在は lint で見つけて直させられる。
    - **いつ引くか**：文書を、です・ますか、だ・であるのどちらかに揃えたいとき。チームの文書を、いつも同じ文体で書かせたいとき。
    - **前提**：<!-- link:begin align-japanese-output -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること](align-japanese-output.md)<!-- link:end -->

<!-- textlint-disable -->
別名：敬体と常体を揃える・文体の統一・文末が揺れる
<!-- textlint-enable -->

文体を揃える手順を、用途の順に並べる。文体の指定は Claude への「お願い」であり、揺れをなくす保証にはならない。そこで、指定・手本・置き場所で揺れを減らし、残った混在は lint で拾う二段で組む。

## 先に決めておくこと {#guards}

文体の指定はお願いの層にある。お願いの層と、確かめて差し戻す層の分け方は <!-- link:begin align-japanese-output#request-layer -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › お願いの層：設定・CLAUDE.md・出力スタイル・アプリの指示](align-japanese-output.md#request-layer)<!-- link:end --> にある。この手順では、お願いを使って減らし、仕組みを使って拾う。始める前に、次の 3 つを決める。

- **どの文体か**：新しく決めるより、既存の文書に合わせる。既存の文書の文末を数える依頼は、「揃ったかを確かめる」の節の雛形にある。
- **どこまでが対象か**：書かせる文書だけか、コードのコメントとコミットメッセージも含むか。チャットの返答の調子を含めるかも決める。
- **何を lint に任せるか**：文体の混在は機械で見つけられる。どのルールを機械に任せるかは <!-- link:begin textlint-hook#rules -->[textlint をフックで回す › どのルールを機械に任せるか](textlint-hook.md#rules)<!-- link:end --> で決める。規則は増やしすぎない（<!-- link:begin textlint-hook#failure-and-few -->[textlint をフックで回す › フックが落ちたときと、規則を増やしすぎないこと](textlint-hook.md#failure-and-few)<!-- link:end -->）。

表記ゆれ（「サーバー」と「サーバ」など）は別の手順になる。用語の一覧を人が持ち、指示と lint に同じものを使う流れは <!-- link:begin consistent-notation#single-source -->[表記ゆれと漢字の開き › 一覧を指示と lint の両方に使う](consistent-notation.md#single-source)<!-- link:end --> にある。

## 文体は一行で、理由と一緒に指定する {#specify}

文体の指定は、対象・文体・理由の 3 つを一行に入れる。型は「<対象>は<文体>で書く。理由：…。対象外：…」である。

実践者の報告では、です・ます調を明示しないと長い文章の途中で揺れる（根拠：弱。単独の記事）。「文体を統一して」のように、どちらに揃えるかを書かない指定は、手がかりにならない。

!!! example "Before / After：同じ依頼の指定"
    - **Before**：「文体を統一してください」と頼む。
    - **After**：「README と設計メモは、だ・である調で書く。理由：既存の文書がすべてその調で、混ざると校正で読み直す手間が出るため。返答は対象外」と頼む。
    - **足したもの**：対象（README と設計メモ）・文体（だ・である調）・理由・対象外（返答）を足した。

理由を添える効果は、境目で判断する手がかりになることである。見出し・箇条書き・コメント・引用のどれに同じ規則を当てるかは、理由があると読み取りやすい。これはこの辞典の推奨で、手段として比べた記録はない。

境目の例を 1 つ挙げる。実践者の設定には、本文はです・ます、箇条書きはである、と部位で分けたものがある（根拠：弱。単独の実践例）。部位で分けるなら、その境目も指示と lint に書く。

!!! example "判断例：文体を節ごとに分けるか"
    - **状況**：既存の README が、本文はだ・である調で、利用者向けの手順の節だけです・ます調になっている。新しい文書を Claude に書かせたい。
    - **迷う候補**：全部を、だ・である調に揃える。本文はだ・である調、手順の節はです・ます調と、節ごとに分ける。
    - **選んだもの**：全部を、だ・である調に揃える。
    - **理由**：節ごとの境目を指示に書くと、規則と lint の設定が増え、境目で揺れる。利用者向けの手順にです・ますが要るなら、文書を分けて、文書ごとに一行で指定するほうが保ちやすい。

指定の例は、「置き場所」の節の雛形にまとめて載せた。一行の指定が書けたら、次の手本の節に進む。

確かめ：新しいセッションで短い文書を 1 本書かせ、文末が指定どおりかを目で見る。ここで揃わないなら、次の手本の前に、指定の対象と文体の書き方を見直す。

## 手本の文章を見せる {#example}

指定の次に、その文体で書かれた手本の文章を見せる。言葉で説明するより、典型的で多様な例を見せるほうが形や文体は揃う。選び方は <!-- link:begin show-examples#choose -->[例を見せる › 典型的で多様な例を選ぶ](../prompting/show-examples.md#choose)<!-- link:end --> にあり、数は <!-- link:begin show-examples#how-many -->[例を見せる › 何個見せるか](../prompting/show-examples.md#how-many)<!-- link:end --> で決める。

手本は、自分が書いた既存の文書から取るのがよい。言葉にしにくい好みまで伝わる（<!-- link:begin show-examples#own-writing -->[例を見せる › 自分の文章を手本にする](../prompting/show-examples.md#own-writing)<!-- link:end -->）。

- **短くする**：本文・見出し・箇条書きが入った数段落で足りる。長い手本は、毎回読まれる場所を圧迫する。
- **指定と同じ文体のものを選ぶ**：手本の文体が指定と違うと、手本に引かれる恐れがある（推論・実践例なし）。
- **混在のない文書を選ぶ**：手本に混在があると、そこが揺れの元になる。lint か文末を数える依頼で、手本を先に通しておく。
- **手本の写しすぎ**：手本の話題や構成まで写されることがある（<!-- link:begin show-examples#overfit -->[例を見せる › 例にだけ合う出力に気をつける](../prompting/show-examples.md#overfit)<!-- link:end -->）。

手本が長くなるなら、スキルに置いて、文書を書くときだけ読ませる。スキルは名前と説明を先に見て、関わるときだけ本体を読む。使われないときの確かめ方は <!-- link:begin skills-in-the-app#not-triggered -->[アプリでスキルを使う › 使われないとき](../app/skills-in-the-app.md#not-triggered)<!-- link:end --> にある。

技術文書を書かせる場面では、プロジェクトの既存の文書を手本にする流れが <!-- link:begin write-docs -->[ドキュメント・技術文書を書く](../recipes/write-docs.md)<!-- link:end --> にある。文章を頼むときの渡し方は <!-- link:begin requesting-prose -->[文章を頼むとき（読み手・目的・手本を渡す）](../prompting/requesting-prose.md)<!-- link:end --> にある。

確かめ：手本を入れたセッションで、手本と同じ種類の文書を新しく書かせ、文末が手本と揃うかを見る。

## 置き場所（アプリの指示・スキル・CLAUDE.md・出力スタイル） {#where}

一行の指定と手本は、毎回読まれる場所に置く。置き場所は面で違う。次の表は、置き場所の候補の強制力と読み込みの時期である。

<!-- gen:begin compare 面 強制力 読み込みの時期 -->
<!-- textlint-disable -->

| 機能 | 面 | 強制力 | 読み込みの時期 |
| --- | --- | --- | --- |
| [Claude への指示（Instructions for Claude）](../app/where-to-put-instructions.md) | アプリ | お願い | — |
| [プロジェクトの指示（project instructions）](../app/using-projects.md) | アプリ | お願い | — |
| [スキル（アプリ。skills）](../app/skills-in-the-app.md) | アプリ | お願い | — |
| [スタイル（Styles。スキルへ移行）](../app/skills-in-the-app.md) | 未確認 | 未確認 | 未確認 |
| [CLAUDE.md](../extend/what-to-put-in-claude-md.md) | Claude Code | お願い | セッション開始 |
| [出力スタイル（output styles）](../cli/output-style-modes.md) | Claude Code | お願い | セッション開始と切り替えたとき |

<!-- textlint-enable -->
<!-- gen:end compare 面 強制力 読み込みの時期 -->

どの置き場所も、強制ではなくお願いである。強制力の列がそれを示す。置き場所の選び方は <!-- link:begin where-to-put-instructions#how-to-choose -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › どこに置くかの選び方](../app/where-to-put-instructions.md#how-to-choose)<!-- link:end --> にある。組み合わせ方は <!-- link:begin where-to-put-instructions#combine -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 置き場所の組み合わせ方](../app/where-to-put-instructions.md#combine)<!-- link:end --> にある。

=== "アプリ"

    全部の会話で同じ文体にするなら、Claude への指示（設定の Instructions）に書く。特定のプロジェクトの文書だけなら、プロジェクトの指示に書く。場面ごとに切り替えるなら、スキルにする。

    チームで揃えるなら、プロジェクトの指示に雛形を置き、同じプロジェクトを使う人に共有する。文体の指定だけを個人の設定に置くと、人によって揃わない。

    Styles（スタイル）で調子と形式を切り替える助言は、スキルへの移行が告知されて古くなった。Styles を頼りにせず、上の置き場所を使う。移された Styles の書き方は <!-- link:begin where-to-put-instructions#styles -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 調子と形式を揃えたいとき（Styles を使っていた場合）](../app/where-to-put-instructions.md#styles)<!-- link:end --> と <!-- link:begin skills-in-the-app#migrated-styles -->[アプリでスキルを使う › 移された Styles](../app/skills-in-the-app.md#migrated-styles)<!-- link:end --> にある。台帳の行は <!-- link:begin outdated-advice-ledger#styles-for-tone -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#styles-for-tone)<!-- link:end --> で読める。

    アプリにはフックがなく、指示しかない（<!-- link:begin align-japanese-output#app -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › アプリには指示しかない](align-japanese-output.md#app)<!-- link:end -->）。次の lint の節の機械の検査は、書かせた文書を手元に持ち出して流す形になる。

=== "Claude Code"

    リポジトリの根の `CLAUDE.md` に書く。公式は、`CLAUDE.md` を強制する設定ではなく文脈として扱うと書く。チームで揃えるなら、リポジトリに入れて共有する。

    出力スタイルは、応答の仕方をセッション全体で切り替える機能で、これも指示であり何も強制しない。ファイルに書く文書の規約は `CLAUDE.md` に、応答の調子は出力スタイルに置く分担が筋である（この辞典の推奨）。分担の詳細は <!-- link:begin output-style-modes#vs-claude-md -->[出力スタイルで応答の仕方を切り替える › CLAUDE.md・スキルとの分担](../cli/output-style-modes.md#vs-claude-md)<!-- link:end --> と <!-- link:begin output-style-modes#japanese -->[出力スタイルで応答の仕方を切り替える › 日本語の応答との関係](../cli/output-style-modes.md#japanese)<!-- link:end --> にある。

    届かない場所がある。`CLAUDE.md` は組み込みの Explore と Plan のサブエージェントに届かず、出力スタイルは fork でないサブエージェントに届かない。サブエージェントに文書を書かせるなら、委任の文に文体の指定を書き直す。クラウドのセッションは、ユーザーの `~/.claude/CLAUDE.md` を読まない。届く範囲は <!-- link:begin align-japanese-output#reach -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 届く範囲（サブエージェント・圧縮の後・クラウドのセッション）](align-japanese-output.md#reach)<!-- link:end --> にまとめてある。

雛形は、プロジェクトの指示か `CLAUDE.md` へそのまま置ける。手本の文書名は、自分のものと入れ替える。

<!-- gen:begin snippet consistent-politeness/style-instruction -->
<!-- textlint-disable -->

??? example "雛形：文体の指定の例（CLAUDE.md とアプリの指示）"

    ```markdown
    ## 文体

    - README・設計メモ・コード内のコメントは、だ・である調で書く。理由：既存の文書がすべてその調で、混ざると校正のたびに全体を読み直す手間が出るため。
    - 見出し・本文・箇条書きの全部を同じ調にする。です・ますは使わない。他の文書からの引用と、コードの中の文字列は直さない。
    - この規則は、書かせる文書とコメントが対象である。チャットの返答の調子は対象外とする。
    - 手本は docs/overview.md の冒頭の 3 段落とする。迷ったら、まずそれに寄せる。

    手本（docs/overview.md の冒頭）：

    > 本ツールは、設定ファイルから docs の目次を生成する。生成は手元で行い、結果をそのままコミットする。
    >
    > 目次の順は、各ページの `order` で決まる。同じ値のページは、題名の順に並ぶ。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.81。

<!-- textlint-enable -->
<!-- gen:end snippet consistent-politeness/style-instruction -->

確かめ：置いた後に新しいセッションを開き、短い文書を書かせて、文末が揃うかを見る。サブエージェントや別の面でも書かせるなら、その面でも見る。

## 混在を lint で見つける {#lint}

指定と手本で揺れは減るが、なくならない。残った混在は、お願いを重ねるより、機械で見つけて Claude に直させる。指示と lint の役割の分け方は <!-- link:begin align-japanese-output#lock-layer -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 確かめて差し戻す層：フックと lint](align-japanese-output.md#lock-layer)<!-- link:end --> にある。

実践者の例がある。`Write|Edit|MultiEdit` の後に textlint を走らせ、ルール `no-mix-dearu-desumasu` で混在を見つける。残った違反は exit 2 で Claude に返し、直させている（根拠：弱。単独の実践例）。

設定は <!-- link:begin textlint-hook#post-tool-use -->[textlint をフックで回す › 書いた後に走らせて差し戻す](textlint-hook.md#post-tool-use)<!-- link:end --> に置いてある。この手順では、文体の混在に関する次の点だけを決める。

- **ルールは文体に絞る**：最初から多くのルールを入れない。まず文体の混在だけを入れる。
- **直させる指示は狭く書く**：「違反の行だけを直す。内容は変えない」と書く。
- **揃える向きは lint が決めない**：lint は混ざっていることを見つけるだけで、どちらに揃えるかは指定が決める。
- **拾えない書き込みがある**：シェルで書いたファイルは、フックの matcher に掛からない（<!-- link:begin textlint-hook#gaps -->[textlint をフックで回す › 拾えない書き込み（シェルで書いたファイル）](textlint-hook.md#gaps)<!-- link:end -->）。

確かめ：壊れてよいファイルに、わざと逆の文体の文を 1 文混ぜて書かせる。lint が止めて、Claude が直した後に混在が消えるかを見る。

## 揃ったかを確かめる {#check}

仕上げに、書かれた文書の文末を数える。数える作業は、コマンドを実行できる面なら grep などに任せる。Claude に目で数えさせると、数え間違いが混ざる（推論・実践例なし）。次の雛形は、数える依頼の例である。

<!-- gen:begin snippet consistent-politeness/count-endings -->
<!-- textlint-disable -->

??? example "雛形：文末の文体を数えさせる依頼"

    ```markdown
    docs/ の下の Markdown について、文末の文体を調べてほしい。

    - 数えるのは grep などのコマンドで行う。目で数えない。
    - 各ファイルで、文末が「です・ます」の文と「だ・である」の文を数える。
    - 両方が出るファイルは、少ないほうの文末の行番号を挙げる。
    - コードブロック・引用・表の中は数えない。
    - ファイルは直さない。一覧だけを報告する。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.81。

<!-- textlint-enable -->
<!-- gen:end snippet consistent-politeness/count-endings -->

この依頼は、手順の最初にも使える。始める前に既存の文書へ流せば、現状の文体が分かる。

効いたかは、一度の試行で判断しない。同じ依頼を新しいセッションで何度か走らせ、指定を足す前と後で混在した文書の数を比べる。小さな eval の手順は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> にある。

文体を守らせる手段を比べた記事は、調べた範囲では見つからなかった。`CLAUDE.md`・スキル・フックのどれが効くかは、自分の環境で測るしかない。スキルの有り無しを比べる手順は <!-- link:begin measure-changes#compare-skills -->[変更が効いたかを測る（小さな eval） › スキルの有り無しを新しいセッションで比べる（skill-creator・claude plugin eval）](../eval/measure-changes.md#compare-skills)<!-- link:end --> にある。

## 揺れが残ったとき {#failure}

lint まで入れても揺れが残るときは、症状から原因を切り分ける。

- **長い文章の途中から崩れる**：原因を安く確かめる順を <!-- link:begin inconsistent-japanese-style#diagnosis -->[文体や表記が揃わない › 原因を安く確かめる順](../symptoms/inconsistent-japanese-style.md#diagnosis)<!-- link:end --> に置いてある。指定が見えていないのか、縛っていないのかを分ける。
- **サブエージェントの報告だけが混ざる**：指定が届いていない。委任の文に書き直す。
- **推敲のスキルを通すと文体が変わる**：推敲の手順を書く手順と分ける。スキルの選び方は <!-- link:begin less-ai-sounding-japanese#proofreading-skill -->[日本語の「AI 臭さ」を減らす › 推敲をスキルにする（文体を保つか、構成から直すか）](less-ai-sounding-japanese.md#proofreading-skill)<!-- link:end --> にある。
- **lint を入れたのに止まらない**：書き込みの経路が matcher に掛かっていない。<!-- link:begin textlint-hook#gaps -->[textlint をフックで回す › 拾えない書き込み（シェルで書いたファイル）](textlint-hook.md#gaps)<!-- link:end --> で確かめる。
- **語尾は揃うが言い回しが定型になる**：文体の問題ではなく、読みにくさの型の問題である。<!-- link:begin less-ai-sounding-japanese#patterns -->[日本語の「AI 臭さ」を減らす › 読みにくさの型を具体的に挙げる](less-ai-sounding-japanese.md#patterns)<!-- link:end --> に分けて直す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Output styles](https://code.claude.com/docs/en/output-styles)：Anthropic・英語・確認日 2026-11-04
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)：Anthropic・英語・確認日 2026-11-04
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)：Anthropic・英語・確認日 2026-11-04
- [Styles are moving to skills](https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills)：Anthropic（写し）・英語・確認日 2026-11-04
- [\[進化版\] VSCode + Claude Code Hooksでマークダウンの文書作成を爆速化する環境構築方法](https://zenn.dev/yuki_fujisawa/articles/a01e472dc190cf)：Zenn（yuki\_fujisawa）・確認日 2026-11-04
- [Claude日本語精度｜ChatGPT・Gemini比較と自然な出力のコツ](https://jinrai.co.jp/blog/2026/03/26/claude-japanese/)：仁頼・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [日本語の出力を揃える：お願いで足りること、仕組みが要ること](align-japanese-output.md)

**次に読む**

- [ドキュメント・技術文書を書く](../recipes/write-docs.md)

**関連**

- [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)
- [表記ゆれと漢字の開き](consistent-notation.md)
- [textlint をフックで回す](textlint-hook.md)
- [例を見せる](../prompting/show-examples.md)
- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- [アプリでスキルを使う › 移された Styles](../app/skills-in-the-app.md#migrated-styles)
- [出力スタイルで応答の仕方を切り替える](../cli/output-style-modes.md)
- [日本語の「AI 臭さ」を減らす](less-ai-sounding-japanese.md)
- [文章を頼むとき（読み手・目的・手本を渡す）](../prompting/requesting-prose.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
