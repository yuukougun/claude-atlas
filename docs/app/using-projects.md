---
id: using-projects
title: プロジェクトの使いどころ
aliases: [Projects, Claude Projects, Project knowledge, プロジェクトナレッジ]
type: feature
field: app
chapter: 指示と記憶
order: 20
level: 整える
priority: 必須
surfaces: [app]
principle: [見せる]
prevents: [見えていない, 散らかっている]
scenes: [文章, 調べもの]
summary: 同じ資料と指示で繰り返す作業を、プロジェクトに入れる単位と中身で整えられる。資料を置くと使用量が抑えられる理由と、目的を混ぜない理由も分かる。
signs:
  - {type: situation, text: 同じ資料を使う作業を何度も繰り返す}
  - {type: goal, text: 同じ資料を、会話のたびに添付し直さずに使いたい}
  - {type: goal, text: 案件ごとに指示と資料を分けて持ちたい}
prerequisites: [attention-budget]
related: [where-to-put-instructions, too-much-project-knowledge, how-memory-works, shared-projects-and-org-skills, feature-to-api-mapping, why-prompt-caching, tidy-the-desk#in-the-app, what-uses-up-limits, handing-long-documents]
tracks: [projects, project-instructions]
sources: [hc-projects-manage, hc-projects-what, hc-personalization, hc-usage-limit-best-practices, jinrai-claude-projects-guide]
volatility: 中
sections:
  - {title: プロジェクトを切る単位（1つに1つの目的）, anchor: scope}
  - {title: ナレッジを置くと何が変わるか, anchor: knowledge}
  - {title: プロジェクトの指示に書くこと, anchor: instructions}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：同じ資料と指示で繰り返す作業を、プロジェクトに入れる単位と中身で整えられる。
    - **強制力**：プロジェクトの指示は <!-- gen:begin feature project-instructions/enforcement -->お願い<!-- gen:end feature project-instructions/enforcement -->である。全部の会話で Claude が使う指示になるが、守らせる仕組みではない。ナレッジは、置いた資料を使える状態にするだけで、読ませる仕組みではない。
    - **いつ引くか**：同じ資料を使う作業を何度も繰り返すとき。会話のたびに資料を添付し直したくないとき。案件ごとに指示と資料を分けて持ちたいとき。
    - **前提**：<!-- link:begin attention-budget -->[コンテキストウィンドウと注意の予算](../basics/attention-budget.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Projects・Claude Projects・Project knowledge・プロジェクトナレッジ
<!-- textlint-enable -->

プロジェクトは、アプリで会話をまとめる作業場所である。資料（ナレッジ）と指示を 1 か所に置き、その中で始めた会話のすべてに使わせる。成熟度は <!-- gen:begin feature projects/maturity -->GA<!-- gen:end feature projects/maturity --> である。毎回の資料の添付と説明は減るが、目的を混ぜたり資料を詰め込んだりすると、かえって答えが散らかる。このページは、何を 1 つのプロジェクトに入れ、何を置き、何を指示に書くかを決めるために引く。

## プロジェクトを切る単位（1つに1つの目的） {#scope}

プロジェクトは、1 つに 1 つの目的を持たせて切る。目的は「月次の売上レポートの下書き」「社内規程への問い合わせ対応」のように、同じ資料と同じ指示で繰り返す作業の単位である。

1 つのプロジェクトには、ナレッジ（資料）・指示・その中の会話が入る。ナレッジと指示は、そのプロジェクトのすべての会話に使われる（[How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)）。プロジェクトごとに独立したメモリもあり、範囲の詳細は <!-- link:begin how-memory-works#scope -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › アカウントのメモリとプロジェクトのメモリ](how-memory-works.md#scope)<!-- link:end --> にある。

目的を混ぜない理由は 2 つある。

- 指示が衝突する。たとえば「結論から短く」と「根拠を詳しく」を同じ指示に書くと、どちらに従うかが会話ごとにぶれる。実践者の解説も、目的を混ぜると指示とナレッジが衝突する、と書く（根拠：弱）。
- 無関係な資料が混ざる。すべての会話でナレッジが材料の候補になるので、目的に関係のない資料が多いほど、肝心の資料への注意が薄くなる。仕組みは <!-- link:begin attention-budget#effects -->[コンテキストウィンドウと注意の予算 › 何に効くか：見せることと、散らかっていること](../basics/attention-budget.md#effects)<!-- link:end --> にある（原理は「見せる」）。

「1 プロジェクト 1 目的」は公式の規則ではなく、実践者の勧めである。根拠は単独の企業の解説記事で、強くない。ただ、混ぜたときの不具合は、上の 2 つの理由から筋が通る。

切る基準は、同じ資料と指示を使い回すかである。1 回きりの作業は、プロジェクトを作らず、通常の会話に資料を添付すればよい。すべての案件に共通する好み（口調・言語など）は、プロジェクトごとに書き写さず、置き場所を選ぶ（<!-- link:begin where-to-put-instructions#how-to-choose -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › どこに置くかの選び方](where-to-put-instructions.md#how-to-choose)<!-- link:end -->）。

!!! example "判断例：月次レポートと採用の資料を同じプロジェクトにするか"
    - **状況**：月次の売上レポートの下書きを毎月作る。同じ人が、採用の面接メモの整理も毎週している。どちらも文章の作業で、使う画面も同じである。
    - **迷う候補**：「仕事全般」の 1 つのプロジェクトにまとめる。目的ごとに 2 つのプロジェクトに分ける。
    - **選んだもの**：2 つに分ける。
    - **理由**：売上レポートに採用の資料は要らず、面接メモに売上の資料は要らない。まとめると、指示にも 2 つの用途の書き方が並び、どちらの作業でも要らない資料が候補に入る。分ければ、各プロジェクトの指示と資料が短くなり、何が効いているかも確かめやすい。口調など両方で同じものは、プロジェクトの外の置き場所に書く。

## ナレッジを置くと何が変わるか {#knowledge}

ナレッジは、プロジェクトに置く資料である。置いた資料は、そのプロジェクトのすべての会話で使われるので、会話のたびに添付し直さなくてよい。必要な資料が Claude に見えていない状態と、無関係な資料で机が散らかっている状態を、置く資料を選ぶことで防ぐ。変わるのは次の 3 点である。

- 添付と説明の手間が減る。「この資料を見て」と毎回頼まなくても、資料が使える状態から会話が始まる。
- 使用量が抑えられる。公式の節約の勧めは、繰り返し参照する主要な資料を最初にプロジェクトへアップロードすることである。キャッシュが効き、再利用のときの消費が少なくなる。ただし、一定の時間使わないとキャッシュが切れ、全量が数えられる状態に戻る（[Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)）。
- 会話をまたいで同じ資料を前提にできる。資料の版が会話ごとにそろい、「どの版を見たか」がずれにくい。

使用量が抑えられるのは、先頭が変わらなければ読み直しが安く済む、という仕組みに乗るからである。積み木の下の段が変わらない限り、そこは積み直さずに済む。仕組みは <!-- link:begin why-prompt-caching -->[プロンプトキャッシング（先頭が変わらないことの価値）](../basics/why-prompt-caching.md)<!-- link:end --> にあり、何が上限を早く使うかは <!-- link:begin what-uses-up-limits#causes -->[上限を早く使う要因 › 枠を早く減らす原因](../cost/what-uses-up-limits.md#causes)<!-- link:end --> で確かめられる。ただし、使わずに時間が空くとキャッシュは切れるので、「毎回安い」とは限らない。

置けば読まれる、ではない。ナレッジは、会話の材料にできる状態になるだけである。実際にどこが使われるかは、資料の量と指示の書き方で決まる。資料が多すぎて容量に近づくと、読み方が変わる。その場合は <!-- link:begin too-much-project-knowledge#rag-mode -->[プロジェクトのナレッジが多すぎるとき › 容量に近づくと何が変わるか](too-much-project-knowledge.md#rag-mode)<!-- link:end --> と <!-- link:begin too-much-project-knowledge#curate -->[プロジェクトのナレッジが多すぎるとき › 資料の絞り方と入れ直し方](too-much-project-knowledge.md#curate)<!-- link:end --> を見る。

入れる資料は、少数から始める。実践者の解説は、最初は少数のファイルにし、古い版は削除するよう勧める（根拠：弱）。長い資料は、分ける・テキストに直すなど、形と量を整えてから置く（<!-- link:begin handing-long-documents#split-and-convert -->[長い資料を渡すとき › 分ける・形を直す](../context/handing-long-documents.md#split-and-convert)<!-- link:end -->）。

!!! example "判断例：この資料はナレッジに置くか、会話に添付するか"
    - **状況**：社内の経費精算の規程（月に 1 回ほど改訂される）と、今日だけ見る取引先からのメールがある。経費に関する問い合わせへの回答の下書きを、毎週何件も作る。
    - **迷う候補**：両方をナレッジに置く。規程だけをナレッジに置き、メールは会話に添付する。
    - **選んだもの**：規程だけをナレッジに置く。メールは、その会話に添付する。
    - **理由**：規程は、繰り返す作業のすべての会話で使うので、置く価値がある。メールは 1 回きりで、置くと次回以降の会話で無関係な資料になる。規程を改訂したら、古い版をナレッジから消して入れ直す。古い版が残ると、どちらの版を読むかが会話ごとにぶれる。

## プロジェクトの指示に書くこと {#instructions}

プロジェクトの指示は、そのプロジェクトのすべての会話に使われる指示である。公式は Claude が使う指示として説明し、強制の仕組みとしては扱っていない（[How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)）。強制力は <!-- gen:begin feature project-instructions/enforcement -->お願い<!-- gen:end feature project-instructions/enforcement --> である。

書くことは 3 つに絞る。

- 目的：このプロジェクトで何を作るか。1 つの目的を 1〜2 文で書く。
- 資料の使い方：どの事実をナレッジから取るか。資料にないときの扱い、資料どうしが食い違うときの扱い、出どころの添え方を書く。
- 出力の形：見出しの構成・文字数・読み手・口調を書く。「いい感じに」ではなく、数値や形式で書く（根拠：弱。実践者の勧め）。

書かないものもある。

- 資料の中身そのもの。長い規程や表はナレッジに置き、指示には使い方だけを書く。
- 全案件に共通する好み。プロジェクトごとに写さず、置き場所を選ぶ（<!-- link:begin where-to-put-instructions#comparison -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 置き場所ごとの効く範囲と読まれる時期](where-to-put-instructions.md#comparison)<!-- link:end -->）。
- 例外を許さない禁止。指示はお願いなので、守らせたい規則は、守られたかを出力で確かめる。

<!-- gen:begin snippet using-projects/project-instructions -->
<!-- textlint-disable -->

??? example "雛形：プロジェクトの指示の雛形（目的・資料の使い方・出力の形）"

    ```markdown
    このプロジェクトの目的：<1 つだけ書く。例：月次の売上レポートの下書きを作る>

    資料の使い方：
    - 事実は、ナレッジに置いた資料から取る。資料にないことは「資料にない」と書き、推測で埋めない。
    - 資料どうしが食い違うときは、日付の新しいほうを採り、食い違いを知らせる。
    - 数値や固有名詞を書くときは、どの資料のどこから取ったかを添える。

    出力の形：
    - <形式を具体的に書く。例：見出し 3 つ（概要・数値の動き・次の確認）で、全体を 600 字以内>
    - <口調や読み手を書く。例：社内の管理職向け。だ・である調>

    迷ったとき：
    - 依頼が上の目的から外れているときは、作業する前に、このプロジェクトで扱うか別に分けるかを聞く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet using-projects/project-instructions -->

雛形の山かっこは、自分の目的と形式に書き換えて使う。貼った後は、新しい会話を始めて目的に沿った依頼を 1 つ出し、出力の形と出どころの添え方が指示どおりかを見る。外れていれば、外れた点を指示の 1 行に直す。

## 効かない場面・落とし穴 {#pitfalls}

- 指示を使えるプランに食い違いがある。個人設定の記事は、プロジェクトの指示を有料プランだけとする所がある。一方、同じ記事とプロジェクトの記事は、Free でもプロジェクトを作れると書き、指示の設定にプランの制限を書いていない（[Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)）。2026-11-03 の確認でも食い違いは続いていた。自分のプランで指示の欄が使えるかは、画面で確かめる。
- ナレッジの差し替えを忘れる。資料を改訂しても、ナレッジの古い版が残っていると、古い内容が使われる。改訂したら、古い版を消して入れ直す。
- 他のプロジェクトのメモリは使われない。プロジェクトの中では、そのプロジェクトのメモリと、プロジェクトの外のアカウントのメモリが使われる。完全に分けたいときの設定は <!-- link:begin how-memory-works#scope -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › アカウントのメモリとプロジェクトのメモリ](how-memory-works.md#scope)<!-- link:end --> にある。
- 共有すると、見える範囲が広がる。チームで使うときの権限と配る前の確認は <!-- link:begin shared-projects-and-org-skills#shared-projects -->アプリをチームで使う（共有プロジェクト・組織のスキル）<!-- link:end --> にある。
- 同じ名前の別の機能がある。Claude Code 側から順に広がっている新しい版（beta。1 つの会話を並列の threads に分ける）は、アプリのプロジェクトとは別の機能で、このページの対象にしない。
- 会話そのものが長くなる問題は、プロジェクトでは解決しない。会話を新しくする・書き出すなどの整え方は <!-- link:begin tidy-the-desk#in-the-app -->[机を整える：新鮮さ・巻き戻し・書き出し・委任 › アプリでの整え方](../context/tidy-the-desk.md#in-the-app)<!-- link:end --> にある。

## 比べる相手 {#compare}

プロジェクトの指示は、Claude への指示・メモリ・スキルと効く範囲と読まれる時期が違う。どこに何を置くかは <!-- link:begin where-to-put-instructions#comparison -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 置き場所ごとの効く範囲と読まれる時期](where-to-put-instructions.md#comparison)<!-- link:end --> の表で決める。アプリのプロジェクトのキャッシュが API のどの概念に当たるかは <!-- link:begin feature-to-api-mapping#table -->[アプリの機能と API の概念の対応表 › 対応表](../api/feature-to-api-mapping.md#table)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)：Anthropic・英語・確認日 2026-11-04
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)：Anthropic・英語・確認日 2026-11-04
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)：Anthropic・英語・確認日 2026-11-04
- [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Claude Projects の解説記事（仁頼のブログ）](https://jinrai.co.jp/blog/2026/04/03/claude-projects-guide/)：仁頼・確認日 2026-11-05

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)

**次に読む**

- [プロジェクトのナレッジが多すぎるとき](too-much-project-knowledge.md)
- [アプリの機能と API の概念の対応表](../api/feature-to-api-mapping.md)

**関連**

- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](where-to-put-instructions.md)
- [アプリのメモリ（仕組み・範囲・消し方と止め方）](how-memory-works.md)
- [プロンプトキャッシング（先頭が変わらないことの価値）](../basics/why-prompt-caching.md)
- [机を整える：新鮮さ・巻き戻し・書き出し・委任 › アプリでの整え方](../context/tidy-the-desk.md#in-the-app)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)
- [長い資料を渡すとき](../context/handing-long-documents.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
