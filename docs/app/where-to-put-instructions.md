---
id: where-to-put-instructions
title: アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）
nav_title: 指示の置き場所（アプリ）
aliases: [Instructions for Claude, 全会話の指示, Project instructions, プロジェクトの指示, カスタム指示, Styles]
type: comparison
field: app
chapter: 指示と記憶
order: 10
level: 整える
priority: 必須
surfaces: [app]
principle: [見せる]
prevents: [見えていない, 散らかっている]
scenes: [文章, 開発]
summary: Claude への指示・プロジェクトの指示・メモリ・スキルを、効く範囲と読まれる時期で比べ、繰り返す前提や形式の指定をどこに置くかを決められる。
signs:
  - {type: goal, text: 返答の口調や形式をいつも揃えたい}
  - {type: symptom, text: 設定した指示が、関係のない会話にまで効いてしまう}
prerequisites: [attention-budget, where-instructions-sit]
related: [using-projects, how-memory-works, skills-in-the-app, shared-projects-and-org-skills#org-instructions, repeating-the-same-explanation, claude-md-vs-rules-skills-styles, output-style-modes, keep-replies-in-japanese, tidy-the-desk#in-the-app, always-on-costs]
tracks: [personal-instructions, project-instructions, app-memory, app-skills, styles]
outdated_advice: [styles-for-tone]
sources: [cc-docs-memory, hc-personalization, hc-styles-to-skills, hc-set-organization-instructions, hc-projects-manage, hc-memory, hc-skills-what]
volatility: 中
sections:
  - {title: 置き場所ごとの効く範囲と読まれる時期, anchor: comparison}
  - {title: どこに置くかの選び方, anchor: how-to-choose}
  - {title: 置き場所の組み合わせ方, anchor: combine}
  - {title: 調子と形式を揃えたいとき（Styles を使っていた場合）, anchor: styles}
  - {title: 組織の指示があるとき, anchor: org-instructions}
  - {title: Claude Code の置き場所との対応, anchor: claude-code}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：いつも同じ前提・口調なら Claude への指示、1 つの案件ならプロジェクトの指示、場面限りの手順や書式ならスキルに置く。会話から覚えさせるのはメモリ。
    - **いつ引くか**：返答の口調や形式をいつも揃えたいとき。設定した指示が関係のない会話にまで効いてしまうとき。
    - **前提**：<!-- link:begin attention-budget -->[コンテキストウィンドウと注意の予算](../basics/attention-budget.md)<!-- link:end -->・<!-- link:begin where-instructions-sit -->[システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Instructions for Claude・全会話の指示・Project instructions・プロジェクトの指示・カスタム指示・Styles
<!-- textlint-enable -->

アプリの指示の置き場所は、同じ前提や書式を毎回頼まずに済ませるための置き場の選び方である。Claude への指示・プロジェクトの指示・メモリ・スキルは、どれも「あとの会話で Claude に見せるもの」だが、効く範囲と読まれる時期が違う。広く置きすぎると関係のない会話に混ざり、狭く置きすぎると同じ説明を繰り返すことになる。

## 置き場所ごとの効く範囲と読まれる時期 {#comparison}

アプリで繰り返す前提や形式を持たせる場所は、4 つに絞れる。次の表は、機能の属性を数値ファイルから道具が作ったものである。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 面 | 成熟度 | 強制力 | 入った版 |
| --- | --- | --- | --- | --- |
| [Claude への指示（Instructions for Claude）](where-to-put-instructions.md) | アプリ | GA | お願い | 2024-12-20 |
| [プロジェクトの指示（project instructions）](using-projects.md) | アプリ | GA | お願い | — |
| [メモリ（アプリ。memory）](how-memory-works.md) | アプリ | GA | — | 2025-09-11 |
| スキル（アプリ。skills）（準備中） | アプリ | GA | お願い | 2025-10-16 |
| スタイル（Styles。スキルへ移行）（準備中） | 未確認 | 未確認 | 未確認 | 未確認 |

すべて共通：確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare -->

属性の表にない、効く範囲と読まれる時期は次のとおりである。

| 置き場所 | 効く範囲 | 読まれる時期 |
| --- | --- | --- |
| Claude への指示 | アカウントの全部の会話 | その範囲の会話では毎回、Claude が考慮する指示として効く |
| プロジェクトの指示 | そのプロジェクトの中の会話だけ | そのプロジェクトで会話するたびに効く |
| メモリ | アカウントのメモリと、プロジェクトごとのメモリ | 保存された内容が、あとの会話に持ち越される |
| スキル | 有効にしたスキル | 名前と説明を先に見て、関わるときだけ本体を読む |

読み方は 3 つある。

- **指示は書いた人が中身を決める**：Claude への指示とプロジェクトの指示は、自分で書いた文がそのまま使われる。どちらも、強制の仕組みではなくお願いである（表の強制力の列）。
- **メモリは Claude が保存する**：書いて置く場所ではなく、会話から保存されるものである。何がどう保存されるかは <!-- link:begin how-memory-works#what-is-saved -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 何が、いつ保存されるか](how-memory-works.md#what-is-saved)<!-- link:end --> を見る。範囲の分かれ方は <!-- link:begin how-memory-works#scope -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › アカウントのメモリとプロジェクトのメモリ](how-memory-works.md#scope)<!-- link:end --> にある。
- **スキルだけが必要なときに読まれる**：指示とメモリは範囲の中で常に効くが、スキルは説明を手がかりに、関わる場面だけ本体を読む。常に載せる量を抑えられる理由は <!-- link:begin always-on-costs#resident-vs-on-demand -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 常駐するものと、使うときだけ読むもの](../context/always-on-costs.md#resident-vs-on-demand)<!-- link:end --> に書いてある。

プロジェクトの指示の書き方と、プロジェクトを切る単位は <!-- link:begin using-projects#instructions -->[プロジェクトの使いどころ › プロジェクトの指示に書くこと](using-projects.md#instructions)<!-- link:end --> と <!-- link:begin using-projects#scope -->[プロジェクトの使いどころ › プロジェクトを切る単位（1つに1つの目的）](using-projects.md#scope)<!-- link:end --> へ。スキルの入れ方は <!-- link:begin skills-in-the-app#built-in-and-custom -->アプリでスキルを使う › 組み込みのスキルと自作のスキル（準備中）<!-- link:end --> へ。

## どこに置くかの選び方 {#how-to-choose}

置き場所は、その内容が「どの会話に要るか」で決める。公式の使い分けも、アカウント全体に効かせたいなら Claude への指示、特定のプロジェクト向けならプロジェクトの指示、応答の形式や届け方ならスキルである。

!!! example "判断例：毎回の前提を、全会話の指示にするかプロジェクトにするか"
    - **状況**：毎回「社内の API 設計の資料を前提に、です・ます調で」と書いている。ほかの会話では、この前提は要らない。
    - **迷う候補**：Claude への指示に書く。または、その案件のプロジェクトの指示に書く。
    - **選んだもの**：プロジェクトの指示に書く。
    - **理由**：Claude への指示に書くと、関係のない会話にも前提が混ざる。症状は「設定した指示が関係のない会話にまで効く」になる。その案件の会話だけに効かせたいので、範囲が合うのはプロジェクトである。

!!! example "判断例：どの会話でも使う短い方針"
    - **状況**：全部の会話で日本語で返してほしい。自分は開発者なので、git の基本の説明は要らない。
    - **迷う候補**：プロジェクトごとに同じ文を書く。または、Claude への指示に 1 回だけ書く。
    - **選んだもの**：Claude への指示に 1 回だけ書く。
    - **理由**：全部の会話に要る内容は、プロジェクトごとに複製すると、直すときに食い違いが出る。ただし、短くしておく。長い指示は常に載るので、大事な指示への注意が薄くなる（<!-- link:begin attention-budget -->[コンテキストウィンドウと注意の予算](../basics/attention-budget.md)<!-- link:end -->）。

!!! example "判断例：週次レポートの書式"
    - **状況**：週に 1 度だけ、決まった章立てと表のレポートを頼む。ほかの会話では要らない。
    - **迷う候補**：Claude への指示に書式を書く。または、スキルにする。
    - **選んだもの**：スキルにする。
    - **理由**：書式の指定は、使う場面が限られる。指示に書くと毎回載るが、スキルなら説明だけが常にあり、本体は頼んだときに読まれる。使われないときは <!-- link:begin skills-in-the-app#not-triggered -->アプリでスキルを使う › 使われないとき（準備中）<!-- link:end --> で確かめる。

!!! example "判断例：好みを覚えさせるか、書くか"
    - **状況**：説明は結論から書いてほしい、という好みを毎回伝えている。
    - **迷う候補**：会話の中で頼み続けてメモリに保存させる。または、Claude への指示に書く。
    - **選んだもの**：Claude への指示に書く。
    - **理由**：メモリの中身は Claude が保存するので、自分が文面を決められない。確実に同じ文を渡したいなら、自分で書ける指示が向く。メモリに入った内容は、<!-- link:begin how-memory-works#manage -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 覚えた内容を見る・直す（棚卸し）](how-memory-works.md#manage)<!-- link:end --> で見て直せる。

新しい置き場所を作る前に、毎回同じ説明を繰り返している原因そのものを確かめたいときは、<!-- link:begin repeating-the-same-explanation#diagnosis -->[毎回同じ説明をしている › 原因を安く確かめる順](../symptoms/repeating-the-same-explanation.md#diagnosis)<!-- link:end --> へ。

## 置き場所の組み合わせ方 {#combine}

置き場所は 1 つに絞らず、範囲の広い順に役割を分ける。この辞典の推奨は次のとおりである（根拠：弱。公式の使い分けを並べた整理で、効果を測った結果ではない）。

- **Claude への指示**：言語・文体・自分の立場のような、どの会話でも変わらない短い方針。
- **プロジェクトの指示**：その案件の前提・用語・出力の書式。
- **スキル**：場面ごとの手順や書式。
- **メモリ**：書くほどではない、会話から分かる好み。見直せることが前提になる。

同じ内容を複数の場所に置かない。メモリと指示の両方に同じ好みがあると、直すとき片方だけが残る。個人の指示とプロジェクトの指示で矛盾する文を置いた場合に、どちらが優先されるかは確かめていない。矛盾を置かないのが安全である。

### 効いているかの確かめ方

指示を置いたら、新しい会話で、関係のある質問と関係のない質問の両方を出す。関係のある質問で効き、関係のない質問で効かなければ、範囲は合っている。関係のない質問にまで効くなら、置き場所が広すぎるので、プロジェクトかスキルへ移す。

雛形として、Claude への指示に書く短い方針の例を載せる。動作は確かめていない。

<!-- gen:begin snippet where-to-put-instructions/personal-instruction-example -->
<!-- textlint-disable -->

???+ example "雛形：Claude への指示に書く短い方針の例（言語・文体・前提）"

    ```markdown
    返答は日本語で、です・ます調で書く。
    私はソフトウェアエンジニアで、git とターミナルの基本は説明しなくてよい。
    コードは言語名付きのコードブロックで示し、説明は先に結論を書く。
    分からないことは推測で補わず、確かめる方法を先に示す。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet where-to-put-instructions/personal-instruction-example -->

返答の言語を固定する設定は、アプリにはない。指示で頼むしかなく、守られやすさも公式には書かれていない。日本語に寄せ続ける方法は <!-- link:begin keep-replies-in-japanese#app-and-api -->[日本語で返し続けさせる › アプリと API の場合](../japanese/keep-replies-in-japanese.md#app-and-api)<!-- link:end --> へ。

## 調子と形式を揃えたいとき（Styles を使っていた場合） {#styles}

Styles で応答の調子と形式を切り替えていた場合は、いまの置き場所に移す。この助言は古くなったものとして台帳に載っている（<!-- link:begin outdated-advice-ledger#styles-for-tone -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#styles-for-tone)<!-- link:end -->）。

- **いつも同じ調子にしたい**：Claude への指示に書く。
- **場面を見て切り替えたい**：スキルにする。自分で作ったスタイルは移行でスキルになる。呼ぶときは、名前から作られる `/<名前>-style` を使う。移されたスキルは既定で無効なので、有効にしたかを確かめる。
- **既定のスタイル**：Concise・Explanatory・Formal はなくなり、Learning はスキルとして残った。

公式のスタイル移行の記事は、2026-11-04 の時点で取り下げられている（Internet Archive の写しで読んだ）。画面にスタイルのメニューがまだ出るかは、確かめていない。出ていても、新しく Styles に頼らず、Claude への指示かスキルに書く。Claude Code の出力スタイルは別の機能である（<!-- link:begin output-style-modes -->出力スタイルで応答の仕方を切り替える（準備中）<!-- link:end -->）。移されたスキルの扱いは <!-- link:begin skills-in-the-app#migrated-styles -->アプリでスキルを使う › 移された Styles（準備中）<!-- link:end --> へ。

## 組織の指示があるとき {#org-instructions}

組織の指示がある環境では、個人とプロジェクトの指示に、組織の指示も重なる。個人の指示と組織の指示が矛盾するときは、組織の指示が優先される、と公式は書く。

ただし、この優先は強制の仕組みではなく、プロンプトの層の指示に頼る。まれに挙動が変わる、と公式も明記している。個人の指示を書くときは、組織の指示と食い違う文を置かない。

組織の指示を誰が、どう設定し、どう配るかは、このページでは扱わない。<!-- link:begin shared-projects-and-org-skills#org-instructions -->アプリをチームで使う（共有プロジェクト・組織のスキル） › 組織の指示（準備中）<!-- link:end --> を見る。

## Claude Code の置き場所との対応 {#claude-code}

Claude Code では、同じ役割の置き場所が別の名前で存在する。分け方の対応は近いが、機能は別で、設定も別である。対応は Claude Code の公式の文書（How Claude remembers your project。参考に出典を置いた）で確かめた。

| アプリ | Claude Code |
| --- | --- |
| Claude への指示（全会話） | ユーザー単位の CLAUDE.md |
| プロジェクトの指示 | プロジェクトの CLAUDE.md |
| スキル | スキル |

アプリで書いた指示が Claude Code に届くとは限らない。逆も同じである。両方で同じ口調にしたいなら、それぞれに置く。

Claude Code 側の置き場所の選び方は <!-- link:begin claude-md-vs-rules-skills-styles#how-to-choose -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示の置き場所の選び方](../extend/claude-md-vs-rules-skills-styles.md#how-to-choose)<!-- link:end -->。届く範囲は <!-- link:begin claude-md-vs-rules-skills-styles#reach -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示が届く範囲の違い](../extend/claude-md-vs-rules-skills-styles.md#reach)<!-- link:end --> へ。アプリで有効にしたスキルが Claude Code に読み込まれる条件は、公式同士で記述が食い違う。アプリ側の説明は <!-- link:begin skills-in-the-app -->アプリでスキルを使う（準備中）<!-- link:end --> に任せる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)：Anthropic・英語・確認日 2026-11-04
- [Styles are moving to skills](https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills)：Anthropic（写し）・英語・確認日 2026-11-04
- [Set organization instructions](https://support.claude.com/en/articles/14546867-set-organization-instructions)：Anthropic・英語・確認日 2026-11-04
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)：Anthropic・英語・確認日 2026-11-04
- [Use Claude’s chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)：Anthropic・英語・確認日 2026-11-04
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)
- [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)

**関連**

- [プロジェクトの使いどころ](using-projects.md)
- [アプリのメモリ（仕組み・範囲・消し方と止め方）](how-memory-works.md)
- アプリでスキルを使う（準備中）
- アプリをチームで使う（共有プロジェクト・組織のスキル） › 組織の指示（準備中）
- [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)
- 出力スタイルで応答の仕方を切り替える（準備中）
- [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- [机を整える：新鮮さ・巻き戻し・書き出し・委任 › アプリでの整え方](../context/tidy-the-desk.md#in-the-app)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
