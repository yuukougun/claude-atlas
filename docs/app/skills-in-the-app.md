---
id: skills-in-the-app
title: アプリでスキルを使う
aliases: [Skills, Agent Skills, スキルのアップロード]
type: feature
field: app
chapter: つなぐ・足す
order: 140
level: 任せる
priority: 推奨
surfaces: [app]
principle: [見せる]
prevents: [見えていない, 散らかっている]
scenes: [文章, チーム]
summary: 決まった手順や書式をスキルとしてアプリに持たせ、必要な場面だけ読ませられる。使われないときに確かめることも分かる。
signs:
  - {type: goal, text: 長い手順を、必要なときだけ読ませたい}
  - {type: goal, text: 決まった書式の文書を、いつも同じ手順で作らせたい}
  - {type: symptom, text: 以前使っていた文体の設定が見当たらない}
prerequisites: [how-skills-load]
related: [where-to-put-instructions, skill-descriptions, writing-skills, plugins-in-the-app, shared-projects-and-org-skills, vetting-extensions, files-and-code-execution]
tracks: [app-skills, styles]
outdated_advice: [customize-tabs, styles-for-tone]
sources: [hc-skills-what, hc-skills-use, api-docs-agent-skills, hc-plugins-page, hc-styles-to-skills, hc-personalization]
volatility: 高
sections:
  - {title: 使いどころ, anchor: purpose}
  - {title: 組み込みのスキルと自作のスキル, anchor: built-in-and-custom}
  - {title: 使われないとき, anchor: not-triggered}
  - {title: 移された Styles, anchor: migrated-styles}
  - {title: 自作のスキルを入れる, anchor: upload, level: 仕組みにする}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: old-advice}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：決まった手順や書式をスキルとしてアプリに持たせ、必要な場面だけ読ませられる。使われないときの確かめ方も分かる。
    - **いつ引くか**：長い手順を必要なときだけ読ませたいとき。決まった書式の文書を、いつも同じ手順で作らせたいとき。以前使っていた文体の設定（Styles）が見当たらないとき。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。スキルは Claude が読んで従う手順で、使われることも、手順どおりに進むことも保証されない。毎回必ず起きてほしい処理は、スキルでは止められない。
    - **前提**：<!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Skills・Agent Skills・スキルのアップロード
<!-- textlint-enable -->

アプリでスキルを使うとは、手順や書式をフォルダにまとめたスキルとして、claude.ai や Desktop のアプリに持たせることである。Claude は説明文だけを常に見ていて、依頼に関わると判断したときに本文を読む。このページは、アプリでの使い方、使われないときの確かめ方、移された Styles の扱い、自作のスキルの入れ方を扱う。

## 使いどころ {#purpose}

スキルが防ぐ原因は 2 つある。1 つは、必要な手順が Claude に見えていないこと。同じ手順書を会話のたびに貼っているなら、その手順はスキルの候補である。もう 1 つは、常に効く指示に長い手順を詰めて、指示が散らかることである。手順をスキルに出せば、使わない会話で場所を取るのは名前と説明だけになる。仕組みは「<!-- link:begin how-skills-load#what-happens -->[スキルの考え方（手順を必要なときだけ読む） › 何が起きるか](../extend/how-skills-load.md#what-happens)<!-- link:end -->」にある。

スキルに向くのは、繰り返す手順と、決まった書式の作り方である。毎回の会話で必ず守らせたい短い前提は、スキルではなく指示の置き場所に書く。どこに置くかの比べ方は「<!-- link:begin where-to-put-instructions#comparison -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 置き場所ごとの効く範囲と読まれる時期](where-to-put-instructions.md#comparison)<!-- link:end -->」にある。

!!! example "判断例：週報の書式をどこに置くか"
    - **状況**：毎週、メモを貼って決まった見出しの週報を作らせている。見出しの指定と書き方の注意が 20 行ほどある。
    - **迷う候補**：Claude への指示／プロジェクトの指示／スキル
    - **選んだもの**：スキルを選ぶ。
    - **理由**：週報を頼まない会話にも、20 行が毎回入る必要はない。スキルなら、週報の依頼のときだけ本文が読まれる。週報以外の会話は、同じ設定のまま短く保てる。

## 組み込みのスキルと自作のスキル {#built-in-and-custom}

アプリのスキルには、Anthropic が用意した組み込みのものと、自分で入れるものがある。組み込みには、Excel・Word・PowerPoint・PDF のファイルを作るためのスキルがあり、関連する場面では自動的に使われる。自作のスキルは、フォルダを ZIP にして入れる。入れ方は、後ろの「自作のスキルを入れる」の節にある。

スキルが動くには、コード実行とファイル作成の設定が有効になっている必要がある。この設定とファイルの受け取り方は、「<!-- link:begin files-and-code-execution#when -->[ファイル作成とコード実行 › 使いどころ](files-and-code-execution.md#when)<!-- link:end -->」にある。

スキルの管理は、<!-- name:begin customize-to-plugins -->「Plugins」（サイドバー・チャットのメニュー・設定の名前と、1 つの「Plugins」のページ）<!-- name:end -->の画面で行う。スキルはここで有効と無効を切り替える。チャットの入力欄では、「+」か「/」から選んで使える。画面の名前は変わる途中で、口座によって前の画面のことがある。違いは「古くなった助言」の節にある。

スキルは、Claude の判断で使われる場合と、自分が名前を挙げて呼ぶ場合がある。自分で呼べば、使うかどうかを Claude の判断だけで決めなくてよい。

## 使われないとき {#not-triggered}

スキルを入れたのに使われないときは、次の順に確かめる。

1. スキルのトグルがオンになっているかを見る。入れただけでは有効にならない場合がある。以前の Styles から移されたスキルも、既定で無効である（「移された Styles」の節）。
2. コード実行とファイル作成が有効かを見る。無効だと、スキルは動かない。
3. 依頼の文に、スキルの名前を挙げて頼み直す。これで動けば、スキル自体は壊れておらず、説明文が依頼と合っていない。
4. 説明文を直す。いつ使うスキルかを先頭に具体的に書き、ほかのスキルと重ならないようにする。書き方は「<!-- link:begin skill-descriptions#front-load -->[スキルの description の書き方 › いつ使うかを先頭に具体的に書く](../extend/skill-descriptions.md#front-load)<!-- link:end -->」と「<!-- link:begin skill-descriptions#overlap -->[スキルの description の書き方 › ほかのスキルと重ならないようにする](../extend/skill-descriptions.md#overlap)<!-- link:end -->」にある。
5. 組織で使っているときは、組織の設定でスキルが切られていないかを管理者に聞く。配布の仕組みは「<!-- link:begin shared-projects-and-org-skills#org-skills -->アプリをチームで使う（共有プロジェクト・組織のスキル） › 組織のスキルと配布（準備中）<!-- link:end -->」にある。

直した後は、新しい会話で、同じ依頼をもう一度出して確かめる。確かめ方の全体は「<!-- link:begin skill-descriptions#check -->[スキルの description の書き方 › 起動を確かめる](../extend/skill-descriptions.md#check)<!-- link:end -->」にある。

## 移された Styles {#migrated-styles}

Styles は、応答の調子と形式を選ぶ機能だった。2026 年 6 月に、スキルへの移行が告知された（確認日は 2026-11-04）。この節は、以前使っていた文体の設定が見当たらないときの読み方である。

告知の内容は次のとおりである。

- 自分で作った style は、自動でスキルに移される。移されたスキルは既定で無効なので、使うものを有効にする。
- 既定の Concise・Explanatory・Formal は、移行の後は使えない。Learning は、スキルとして残る。
- 移された style は、名前から作られるスラッシュコマンド `/<名前>-style` で呼ぶ。名前は小文字にして、空白はハイフンにする。
- 移行が終わると、Styles のメニューは表示されなくなる。

告知の記事は、2026-11-04 には取り下げられている。移行が終わったか、画面にメニューが残るかは、公式の資料では確かめられなかった（未確認）。自分のアカウントで、スキルの一覧に `-style` で終わる名前があるかを見るのが早い。

今どうするかは、目的で分ける。いつも同じ調子にするなら、全会話に効く Claude への指示に書く。場面ごとに切り替えるなら、スキルにする。置き場所の考え方は「<!-- link:begin where-to-put-instructions#styles -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 調子と形式を揃えたいとき（Styles を使っていた場合）](where-to-put-instructions.md#styles)<!-- link:end -->」にある。Claude Code の出力スタイルは別の機能で、この移行とは関係がない。

## 自作のスキルを入れる {#upload}

自作のスキルは、`SKILL.md` を入れたフォルダを ZIP にして、アプリにアップロードする。入れたスキルは、自分の判断で使うのか、チームに配るのかで扱いが違う。

先に整える守りがある。他人が作ったスキルは、あなたの権限で動き、スクリプトを含むこともある。入れる前に、出所と中身を確かめる。手順は「<!-- link:begin vetting-extensions#provenance -->[MCP・プラグイン・スキルを入れる前の確認 › 出所を確かめる](../safety/vetting-extensions.md#provenance)<!-- link:end -->」と「<!-- link:begin vetting-extensions#read-contents -->[MCP・プラグイン・スキルを入れる前の確認 › 中身を読む（道具の説明・フック・スクリプト）](../safety/vetting-extensions.md#read-contents)<!-- link:end -->」にある。自分で作ったスキルでも、スクリプトを持たせるなら、実行環境のネットワークの設定を先に見る（「<!-- link:begin files-and-code-execution#network -->[ファイル作成とコード実行 › 実行環境とネットワークの設定](files-and-code-execution.md#network)<!-- link:end -->」）。

入れる手順は次のとおりである。

1. `SKILL.md` を書き、フォルダに入れる。`name` と `description` を持つフロントマターと、呼ばれたときに従う本文でできている。
2. フォルダごと ZIP にする。
3. アプリのスキルの画面から、ZIP をアップロードする。画面は、<!-- name:begin customize-to-plugins -->「Plugins」（サイドバー・チャットのメニュー・設定の名前と、1 つの「Plugins」のページ）<!-- name:end -->のページか、前の画面の「Customize」の「Skills」である。
4. 入れたスキルを有効にする。
5. 新しい会話で、スキルの名前を挙げて頼み、本文のとおりに動くかを見る。

<!-- gen:begin snippet skills-in-the-app/SKILL -->
<!-- textlint-disable -->

??? example "雛形：アプリに入れる最小のスキル（週報の書式）"

    ```markdown
    ---
    name: weekly-report
    description: 週報の下書きを頼まれたとき（「週報にして」「今週のまとめを書いて」など）に使う。貼られたメモを、決まった見出しの週報にそろえる。
    ---

    貼られたメモを、次の見出しの順で週報にまとめる。

    1. 「今週やったこと」は、成果が分かる形で 1 項目 1 行にする。
    2. 「来週やること」は、期限が分かるものを先に並べる。
    3. 「困っていること」は、メモに書かれているものだけを書く。なければ「なし」と書く。
    4. メモにない事実は足さない。足りない情報は、最後に質問として並べる。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet skills-in-the-app/SKILL -->

スキルの中身の書き方は、「<!-- link:begin writing-skills#minimal -->[スキルの作り方 › 最小のスキルを作る](../extend/writing-skills.md#minimal)<!-- link:end -->」にある。本文を短く保ち、詳しい資料は補助ファイルに分ける（「<!-- link:begin writing-skills#supporting-files -->[スキルの作り方 › 補助ファイルとスクリプトに分ける](../extend/writing-skills.md#supporting-files)<!-- link:end -->」）。

組織に配る場合は、権限と配布の仕組みが別にある。Team と Enterprise で共有や配布ができると Help Center は書く。一方、Platform の Agent Skills の文書は、claude.ai のカスタムスキルを各人だけのもので、面をまたいで同期しないと書く。公式同士で食い違っているので、組織で使えるかどうかは、自分の画面と管理者の設定で確かめる。配布は「<!-- link:begin shared-projects-and-org-skills#org-skills -->アプリをチームで使う（共有プロジェクト・組織のスキル） › 組織のスキルと配布（準備中）<!-- link:end -->」を見る。

Claude の設定で有効にしたスキルは、同じアカウントでログインした Claude Code にも読み込まれる（片方向）。同期の条件は「<!-- link:begin plugins-in-the-app#sync -->アプリでプラグインを使う › Claude Code との同期（準備中）<!-- link:end -->」にある。

## 効かない場面と落とし穴 {#limits}

- **使われる保証はない**。スキルはお願いである。名前を挙げて頼むと使われやすくなるが、手順どおりに進むことまでは保証されない。必ず従わせたい処理は、スキルに書かず、別の仕組みで強制する。
- **説明文が起動を決める**。説明文が曖昧なスキルは、使われない、または余計な場面で使われる。直し方は「<!-- link:begin skill-descriptions#purpose -->[スキルの description の書き方 › 使いどころ：説明文が起動を決める](../extend/skill-descriptions.md#purpose)<!-- link:end -->」にある。
- **入れすぎると残るコストがある**。使わないスキルでも、名前と説明は常に載る。数が増えると、説明どうしが重なって起動も乱れる。詳しくは「<!-- link:begin how-skills-load#residual-cost -->[スキルの考え方（手順を必要なときだけ読む） › 入れすぎたときに残るコスト](../extend/how-skills-load.md#residual-cost)<!-- link:end -->」にある。
- **画面と対応は変わりやすい**。画面の名前、使えるプラン、組織での配布は、展開の途中である。この辞典の記述は確認日の時点のものなので、画面と食い違うときは公式の記事を優先する。
- **Styles の現状は未確認**。移行が終わったかは、公式の資料では確かめられていない。

## 比べる相手 {#compare}

- **Claude への指示・プロジェクトの指示・メモリ**：常に、または特定のプロジェクトで効く前提を置く場所である。スキルは、必要なときだけ読まれる手順を置く場所である。比較は「<!-- link:begin where-to-put-instructions -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](where-to-put-instructions.md)<!-- link:end -->」にある。
- **プラグイン**：スキルのほか、コネクタやサブエージェントなどをまとめた束である。職種ごとの道具一式を入れたいときは「<!-- link:begin plugins-in-the-app -->アプリでプラグインを使う（準備中）<!-- link:end -->」を見る。
- **Claude Code のスキル**：同じ仕組みだが、置く場所と作り方が違う。作り方は「<!-- link:begin writing-skills -->[スキルの作り方](../extend/writing-skills.md)<!-- link:end -->」にある。

## 古くなった助言 {#old-advice}

- 「Customize の『Skills』タブで管理する」という手順は、画面の名前が変わる途中にあり、口座によっては今も前の画面である。台帳は「<!-- link:begin outdated-advice-ledger#customize-tabs -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#customize-tabs)<!-- link:end -->」。今どうするかは、自分のサイドバーに「Customize」と「Plugins」のどちらが出るかで読み替える。
- 「Styles で調子と形式を切り替える」という助言は、スキルへの移行で置き換わった。台帳は「<!-- link:begin outdated-advice-ledger#styles-for-tone -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#styles-for-tone)<!-- link:end -->」。今どうするかは、「移された Styles」の節のとおり、常に同じなら Claude への指示、場面ごとならスキルである。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)：Anthropic・英語・確認日 2026-11-04
- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)：Anthropic・英語・確認日 2026-11-04
- [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)：Anthropic・英語・確認日 2026-11-04
- [Manage plugins, skills, and connectors from one Plugins page](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)：Anthropic・英語・確認日 2026-11-04
- [Styles are moving to skills](https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills)：Anthropic（写し）・英語・確認日 2026-11-04
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)

**次に読む**

- アプリでプラグインを使う（準備中）
- アプリをチームで使う（共有プロジェクト・組織のスキル）（準備中）

**関連**

- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](where-to-put-instructions.md)
- [スキルの description の書き方](../extend/skill-descriptions.md)
- [スキルの作り方](../extend/writing-skills.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [ファイル作成とコード実行](files-and-code-execution.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
