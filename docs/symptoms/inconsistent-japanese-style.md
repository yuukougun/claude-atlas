---
id: inconsistent-japanese-style
title: 文体や表記が揃わない
aliases: [です・ますが混ざる, 表記ゆれ, 文体の揺れ]
type: symptom
field: symptoms
chapter: 日本語の出力
order: 200
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る, 見せる]
prevents: [見えていない, 散らかっている, 縛っていない]
pitfalls: []
scenes: [文章, 開発]
summary: です・ますの混在や表記ゆれの原因を、指定の不足・資料の影響・縛りの有無に分けて切り分け、例示で足りるか lint で縛るかを決める。
signs:
  - {type: symptom, text: です・ますとだ・であるが混ざる}
  - {type: symptom, text: 「サーバー」と「サーバ」が混在する}
  - {type: symptom, text: 指定した文体が長い文章の途中で崩れる}
wave: 1
prerequisites: [request-vs-lock]
related: [less-ai-sounding-japanese, documents-in-japanese, requesting-prose, hook-recipes, replies-in-english, not-what-i-meant, instructions-ignored, six-causes]
routes:
  - {cause: 見えていない, to: [consistent-politeness, consistent-notation, show-examples]}
  - {cause: 散らかっている, to: [output-shape#mirror, consistent-politeness#example]}
  - {cause: 縛っていない, to: [textlint-hook, align-japanese-output#lock-layer]}
tracks: [hooks, skills]
outdated_advice: [styles-for-tone]
sources: [cc-docs-hooks, cc-docs-hooks-guide, cc-docs-best-practices, cc-docs-features-overview, cc-docs-skills, hc-styles-to-skills, hc-personalization]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: examples}
  - {title: 予防：繰り返す揺れは仕組みに移す, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：です・ますの混在や表記ゆれの原因を、指定の不足・資料の影響・縛りの有無に分けて切り分け、例示で足りるか lint で縛るかを決められる。
    - **いつ引くか**：です・ますとだ・であるが混ざるとき。同じ語の表記が混在するとき。指定した文体が長い文章の途中で崩れるとき。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：です・ますが混ざる・表記ゆれ・文体の揺れ
<!-- textlint-enable -->

この症状の原因は、指定が Claude の手元にない場合だけではない。指定は届いていても読んだ資料に引かれる場合や、お願いのままでは揺れが残る場合もある。このページは、確かめる手間が小さい順に原因を切り分ける。文体と表記を揃える手順の本体は、持ち主のページに任せる。

## よくある形 {#forms}

読者の言葉ごとに、先に疑う原因を添える。確かめ方は、下の診断にある。

**です・ますとだ・であるが混ざる**：同じ文書の中で、段落や文によって「です・ます」と「だ・である」が入れ替わる。文体の指定を書いたかを疑う（見えていない）。貼った資料の文体に引かれていないかも疑う（散らかっている）。

<!-- textlint-disable prh -->
**同じ語の表記が混在する**：「サーバー」と「サーバ」のように、同じ語が長音の有無や漢字とひらがなの違いで混ざる。どちらも誤りではないので、揃える基準が Claude に渡っていないことが多い（見えていない）。基準を渡しても残るなら、お願いの限界を疑う（縛っていない）。
<!-- textlint-enable prh -->

**指定した文体が長い文章の途中で崩れる**：始めは指定どおりなのに、長く書かせると途中から崩れる。崩れる位置と、その直前に読んだものを控える（散らかっている）。それでも崩れるなら、指示が読まれたうえで外れている（縛っていない）。

## 原因を安く確かめる順 {#diagnosis}

揺れた箇所を 1 つ選び、揺れ方を控える。控えるのは、どの文体とどの文体が混ざったか、同じ語がどんな形で割れたか、揺れが出た位置である。引用・コード・固有名詞の中の揺れは、元の表記のままで正しいので、数えない。上から順に確かめる。上の原因ほど、確かめる手間が小さい。

各項目で原因を直したら、新しい会話で同じ依頼を出し、揃うかを見る。直らなければ、次の項目に進む。

指示で足りるか、lint で縛るかの判断には、プロンプトや CLAUDE.md のような指示は Claude が読んで判断するお願いで、フックのような仕組みは範囲の中で毎回効く鍵だという区別を使う。区別の中身は「<!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end -->」にある。

1. **見えていない**：揃えたい文体や表記が、Claude の手元に入っていない。依頼文にも、毎回読まれる場所にも書いていなければ、揃える基準がそもそもない。

    - 文体の指定を、依頼文や毎回読まれる場所に書いたかを見る。書き方は「<!-- link:begin consistent-politeness#specify -->[です・ます／だ・であるを揃える › 文体は一行で、理由と一緒に指定する](../japanese/consistent-politeness.md#specify)<!-- link:end -->」にある。
    - 表記は、揃えたい語の一覧を渡したかを見る。一覧がなければ、Claude にとっては、どの形も同じく正しい。一覧の作り方は「<!-- link:begin consistent-notation#glossary -->[表記ゆれと漢字の開き › 表記の一覧（用語集）を作る](../japanese/consistent-notation.md#glossary)<!-- link:end -->」にある。
    - 一覧を渡したくても、正本そのものが決まっていないことがある。決まっていない基準は、指示に書けず、検査に使うこともできない。まず正本を決める。
    - 言葉で説明しにくい文体は、手本を見せるほうが揃う。選び方は「<!-- link:begin show-examples#choose -->[例を見せる › 典型的で多様な例を選ぶ](../prompting/show-examples.md#choose)<!-- link:end -->」にある。
    - 書いた場所が、揺れた作業に届いているかも見る。サブエージェントや圧縮の後に指示が届くかは「<!-- link:begin align-japanese-output#reach -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 届く範囲（サブエージェント・圧縮の後・クラウドのセッション）](../japanese/align-japanese-output.md#reach)<!-- link:end -->」にある。
    - アプリで、旧い手順書にあった Styles のメニューを探しても見つからないときは、手順が古い。調子を揃える手段は、Claude への指示に書くか、スキルにする。経緯は「<!-- link:begin outdated-advice-ledger#styles-for-tone -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#styles-for-tone)<!-- link:end -->」にある。

2. **散らかっている**：指定は届いているが、ほかの文体や表記が優勢になっている。貼った資料、読み込んだファイル、過去の出力、頼む文そのものの文体が、出力に映る。

    - 揺れた位置の直前に読んだものを控える。だ・である調の資料や、揺れた表記の多いログを読んだ直後に崩れているなら、この原因が濃い。
    - 頼む文の文体も見る。頼む文の書き方は出力の形に映る。映り方は「<!-- link:begin output-shape#mirror -->[出力の形と分量を指定する › 頼む文の書き方が出力に映る](../prompting/output-shape.md#mirror)<!-- link:end -->」にある。
    - 手本の文章で上書きする手がある。手本の置き方は「<!-- link:begin consistent-politeness#example -->[です・ます／だ・であるを揃える › 手本の文章を見せる](../japanese/consistent-politeness.md#example)<!-- link:end -->」にある。
    - 長い文章の途中で崩れるときは、崩れる位置を控えて、分けて書かせて比べる。長さの原因を切り分けた資料は、いまのところ見つかっていない。

3. **縛っていない**：1 と 2 を直しても揺れが残るなら、指定は届いていて、埋もれてもいない。指定はお願いで、読まれたうえで外れることがある。外れた量を数えてから、仕組みにするかを決める。

    - まず、出力を機械で数える。たとえば `grep -nE "(です|ます)。"` と `grep -nE "(だ|である)。"` の両方に行が出れば、混在している。数えられる揺れは、機械で見つけて直させられる。
    - 例外を許さないか、直さなくても困らないかを決める。許さないなら、仕組みに移す。判断の土台は、お願い（指示）と鍵（仕組み）の区別である。

    === "アプリ"

        - アプリには指示しかなく、出力を機械で確かめて差し戻す仕組みは、この教材では確かめられていない（未確認）。出力を人が読み直し、揺れた箇所を示して直させる運用になる。
        - 指示の層の整理は「<!-- link:begin align-japanese-output#app -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › アプリには指示しかない](../japanese/align-japanese-output.md#app)<!-- link:end -->」にある。

    === "Claude Code"

        - フック（<!-- gen:begin feature hooks/enforcement -->鍵<!-- gen:end feature hooks/enforcement -->）は、決めた規則を毎回確かめて差し戻せる。ファイルを書いた直後に textlint を走らせ、違反を Claude に返す作りが基本である。作り方は「<!-- link:begin textlint-hook#post-tool-use -->[textlint をフックで回す › 書いた後に走らせて差し戻す](../japanese/textlint-hook.md#post-tool-use)<!-- link:end -->」にある。
        - スキル（<!-- gen:begin feature skills/enforcement -->お願い<!-- gen:end feature skills/enforcement -->）に文体の手引きを置く手もある。ただし、これも指示と同じで、揺れは残る。
        - 機械で拾える範囲は、辞書で見つけられる表記と、文末の型に限られる。どの規則を任せるかは「<!-- link:begin textlint-hook#rules -->[textlint をフックで回す › どのルールを機械に任せるか](../japanese/textlint-hook.md#rules)<!-- link:end -->」にある。
        - シェルで書いたファイルには、書いた直後に走るフックが届かない。拾えない書き込みは「<!-- link:begin textlint-hook#gaps -->[textlint をフックで回す › 拾えない書き込み（シェルで書いたファイル）](../japanese/textlint-hook.md#gaps)<!-- link:end -->」にある。
        - 日本語の出力を揃える手段全体は「<!-- link:begin align-japanese-output#lock-layer -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 確かめて差し戻す層：フックと lint](../japanese/align-japanese-output.md#lock-layer)<!-- link:end -->」にある。

    === "API"

        - API では、Claude Code のフックに当たる仕組みを、この教材では確かめていない（未確認）。返答を受け取った側のプログラムで文体と表記を検査し、揺れたら頼み直す組み方が考えられるが、効くかは試していない。

原因が分かったら、次の表の先へ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)<br>[表記ゆれと漢字の開き](../japanese/consistent-notation.md)<br>[例を見せる](../prompting/show-examples.md) |
| 散らかっている | [出力の形と分量を指定する › 頼む文の書き方が出力に映る](../prompting/output-shape.md#mirror)<br>[です・ます／だ・であるを揃える › 手本の文章を見せる](../japanese/consistent-politeness.md#example) |
| 縛っていない | [textlint をフックで回す](../japanese/textlint-hook.md)<br>[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 確かめて差し戻す層：フックと lint](../japanese/align-japanese-output.md#lock-layer) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：技術文書の表記が割れる"
    - **状況**：Claude Code でリポジトリの設計文書を書かせている。同じ文書の中で、同じ語の表記が章によって割れる。文体は指定どおりに揃っている。
    - **迷う候補**：指示に「表記を揃える」と一行足す。揃えたい語の一覧を渡す。一覧から作った lint をフックで回す。
    - **選んだもの**：揃えたい語の一覧を渡し、新しい会話で同じ依頼を出す。残る割れを数えて、毎回出るなら、同じ一覧から lint を作ってフックで回す。
    - **理由**：「揃える」と書いても、どの形を正とするかが Claude にない。一覧を渡すのが最も安い。表記の割れは、辞書で機械が見つけられるので、お願いで残ったときの移し先として lint が筋に合う。一覧を指示と lint の両方に使うと、片方だけ古くなることがない。使い方は「<!-- link:begin consistent-notation#single-source -->[表記ゆれと漢字の開き › 一覧を指示と lint の両方に使う](../japanese/consistent-notation.md#single-source)<!-- link:end -->」にある。

!!! example "判断例：アプリで文体が途中から崩れる"
    - **状況**：アプリで、長い報告書を書かせている。始めはです・ます調だが、終わりのほうでだ・である調が混ざる。
    - **迷う候補**：アプリの指示に文体を足す。自分の過去の文章を手本として貼る。章ごとに分けて書かせ、最後に人が読み直す。
    - **選んだもの**：文体を指示に書き、手本の段落を貼る。それでも崩れるなら、章ごとに分けて書かせ、最後に人が読み直す。
    - **理由**：アプリで使える、出力を機械で確かめて差し戻す仕組みは、この教材では確かめられていない。指示と手本はお願いなので、完全には防げない。崩れが出る長さの手前で分けるのは、確実に取れる手である。

## 予防：繰り返す揺れは仕組みに移す {#prevention}

揺れは、指示を足すだけでは減らないことがある。次の順で備える。

- 文体は一行で指定し、毎回読まれる場所に置く。指定が 1 か所にあれば、食い違いで古い指定が残らない。置き場所は「<!-- link:begin consistent-politeness#where -->[です・ます／だ・であるを揃える › 置き場所（アプリの指示・スキル・CLAUDE.md・出力スタイル）](../japanese/consistent-politeness.md#where)<!-- link:end -->」にある。
- 表記の一覧は、人が持つ正本から作る。指示と検査に同じ一覧を使う。使い方は「<!-- link:begin consistent-notation#single-source -->[表記ゆれと漢字の開き › 一覧を指示と lint の両方に使う](../japanese/consistent-notation.md#single-source)<!-- link:end -->」にある。
- 例外を許さない揺れだけを、フックと lint に移す。移す規則は少なく保つ。保ち方は「<!-- link:begin align-japanese-output#keep-few -->[日本語の出力を揃える：お願いで足りること、仕組みが要ること › 縛る規則は少なく保つ](../japanese/align-japanese-output.md#keep-few)<!-- link:end -->」と「<!-- link:begin textlint-hook#failure-and-few -->[textlint をフックで回す › フックが落ちたときと、規則を増やしすぎないこと](../japanese/textlint-hook.md#failure-and-few)<!-- link:end -->」にある。
- 揃ったかは、直した後に出力を機械で数えて確かめる。確かめ方は「<!-- link:begin consistent-politeness#check -->[です・ます／だ・であるを揃える › 揃ったかを確かめる](../japanese/consistent-politeness.md#check)<!-- link:end -->」にある。
- 文章の癖が気になるときは、文体の揺れと分けて直す。読みにくさの型は「<!-- link:begin less-ai-sounding-japanese#patterns -->[日本語の「AI 臭さ」を減らす › 読みにくさの型を具体的に挙げる](../japanese/less-ai-sounding-japanese.md#patterns)<!-- link:end -->」にある。ほかの規則も守られないなら、「<!-- link:begin instructions-ignored -->[CLAUDE.md や指示が守られない](instructions-ignored.md)<!-- link:end -->」を見る。日本語で頼んだのに英語で返るなら、「<!-- link:begin replies-in-english -->[英語で返ってくる](replies-in-english.md)<!-- link:end -->」を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Styles are moving to skills](https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills)：Anthropic（写し）・英語・確認日 2026-11-04
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**次に読む**

- [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)
- [表記ゆれと漢字の開き](../japanese/consistent-notation.md)
- [例を見せる](../prompting/show-examples.md)
- [出力の形と分量を指定する](../prompting/output-shape.md)
- [textlint をフックで回す](../japanese/textlint-hook.md)
- [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)

**関連**

- [日本語の「AI 臭さ」を減らす](../japanese/less-ai-sounding-japanese.md)
- [日本語の資料を読ませる・書かせる](../japanese/documents-in-japanese.md)
- [文章を頼むとき（読み手・目的・手本を渡す）](../prompting/requesting-prose.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [英語で返ってくる](replies-in-english.md)
- [意図と違うものが出てくる](not-what-i-meant.md)
- [CLAUDE.md や指示が守られない](instructions-ignored.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
