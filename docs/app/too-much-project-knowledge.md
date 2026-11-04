---
id: too-much-project-knowledge
title: プロジェクトのナレッジが多すぎるとき
aliases: [RAG モード, RAG mode, ナレッジの容量]
type: feature
field: app
chapter: 指示と記憶
order: 30
level: 整える
priority: 推奨
surfaces: [app]
principle: [見せる]
prevents: [散らかっている, 見えていない]
scenes: [調べもの, 文章]
summary: プロジェクトのナレッジが容量に近づいたときに読み方がどう変わるかが分かり、資料を絞って入れ直す判断ができる。
signs:
  - {type: situation, text: プロジェクトに資料をたくさん入れている}
  - {type: symptom, text: 資料を足すほど、答えが資料を踏まえなくなった気がする}
prerequisites: [using-projects]
related: [how-attachments-are-read, handing-long-documents, context-rot, choose-what-to-read]
tracks: [projects]
sources: [hc-projects-manage, hc-usage-limits, jinrai-claude-projects-guide]
volatility: 中
sections:
  - {title: 容量に近づくと何が変わるか, anchor: rag-mode}
  - {title: 資料の絞り方と入れ直し方, anchor: curate}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：ナレッジが容量へ近づくと読み方がどう変わるかが分かり、資料を絞って入れ直す判断ができる。
    - **いつ引くか**：プロジェクトに資料をたくさん入れているとき。資料を足すほど、答えが資料を踏まえなくなった気がするとき。
    - **前提**：<!-- link:begin using-projects -->[プロジェクトの使いどころ](using-projects.md)<!-- link:end -->

<!-- textlint-disable -->
別名：RAG モード・RAG mode・ナレッジの容量
<!-- textlint-enable -->

プロジェクトのナレッジは、容量に近づくと、読み方の切り替わる場合がある。切り替わった後の細部は、公式の説明が薄い。そこで、このページは確かめられたことと確かめられていないことを分ける。そのうえで、資料を絞って入れ直す手順と、読まれたかの確かめ方を示す。プロジェクト機能の成熟度は <!-- gen:begin feature projects/maturity -->GA<!-- gen:end feature projects/maturity --> である。

## 容量に近づくと何が変わるか {#rag-mode}

プロジェクトのナレッジが、会話で扱える長さの上限に近づくと、有料プランでは RAG mode が自動で有効になり、扱える量が広がる。公式の説明が書いているのはここまでである（[How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)）。

RAG は、一般には「資料の全体を毎回渡すのではなく、質問に関係する部分を検索で取り出して渡す方式」を指す言葉である。ただし Claude のアプリ内の仕組みが、この一般の意味どおりかは、公式の説明からは確かめられない。調べた範囲では、次のことは確かめていない。

- どの時点で切り替わるか、画面にどう表示されるか。
- 切り替わった後に、資料のどの部分がどのくらい読まれるか。
- 切り替わったプロジェクトの答えの質が、切り替わる前と比べてどう変わるか。

そのため、このページは「容量に近づくと資料の一部しか読まれない」とは書かない。確かなのは、容量が広がること、そして資料が多いほど、答えがどの資料を使ったかを人が見失いやすいことである。

資料を足すほど答えが資料を踏まえなくなったと感じるとき、原因の候補は 3 つある。

- ナレッジの読み方が切り替わり、質問に必要な部分が取り出されていない。（推論・実践例なし。一般の RAG の性質からの推測で、Claude の実装では確かめていない）
- 似ているが違う資料や古い版が混ざり、紛らわしい情報になっている。仕組みは <!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end --> にあり、長い入力の中ほどの情報が使われにくい傾向は <!-- link:begin context-rot#lost-in-the-middle -->[context rot と紛らわしい情報 › 中ほどの情報は使われにくいか（lost in the middle）](../basics/context-rot.md#lost-in-the-middle)<!-- link:end --> にある。
- プロジェクトの指示が、資料の使い方を決めていない。指示はお願いであり、資料を読ませる仕組みではない。

どれが当たりかは、見た目では決められない。資料を絞る前に、答えが資料のどこを根拠にしているかを出させ、人が資料と照らす。引用とページの番号で確かめる方法は <!-- link:begin how-attachments-are-read#verify -->[添付ファイルはどこまで読まれるか › 読まれたかを確かめる（ページの番号と引用）](how-attachments-are-read.md#verify)<!-- link:end --> にあり、プロジェクト向けの依頼の雛形は次に示す。

<!-- gen:begin snippet too-much-project-knowledge/check-knowledge-use -->
<!-- textlint-disable -->

??? example "雛形：ナレッジが使われたかを確かめる依頼（引用とファイル名を先に出させる）"

    ```text
    次の質問に、プロジェクトのナレッジの資料だけを根拠にして答えてください。

    質問：<自分の質問。例：経費精算で、タクシー代を精算できる条件は何か>

    答え方：
    1. 先に、根拠にした資料のファイル名と、該当する箇所の引用を示す。引用は原文のまま、1 か所につき 1〜2 文にする。
    2. その後で、引用だけを使って答えを書く。
    3. ナレッジに根拠が見つからないときは、推測で埋めず「ナレッジにない」と答える。
    4. 最後に、この質問のために見たファイルの名前を挙げ、見ていない資料があれば、そう書く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet too-much-project-knowledge/check-knowledge-use -->

山かっこの所は、ナレッジの資料にだけ答えがある、自分の質問に書き換える。返ってきた引用が、実際に資料にあるかは、人がファイルを開いて確かめる。引用が資料と合わないときや、見たはずのファイルの名前が挙がらないときは、その資料が答えに使われていない疑いがある。Claude の「読みました」という自己申告は、読まれた証拠にならない。

会話そのものが長くなって上限に近づく問題は、ナレッジの容量とは別である。会話の側の上限と対処は <!-- link:begin long-chat-limits -->[長い会話の自動のコンテキスト管理と長さの上限](long-chat-limits.md)<!-- link:end --> にある。

## 資料の絞り方と入れ直し方 {#curate}

資料を絞る目的は、必要な資料が Claude に見えていて、不要な資料で机が散らかっていない状態に戻すことである。公式も、長さの上限に当たったときの対処の 1 つに、プロジェクトのファイルを減らすことを挙げている（[How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)）。

手順は次の順で進める。各段の終わりに、確かめることを添える。

1. プロジェクトの目的を 1 つ書き出す。目的に関係しない資料を、別のプロジェクトに移す。切る単位は <!-- link:begin using-projects#scope -->[プロジェクトの使いどころ › プロジェクトを切る単位（1つに1つの目的）](using-projects.md#scope)<!-- link:end --> にある。確かめること：残った資料のすべてについて、目的との関係を 1 文で言える。
2. 古い版と、1 回きりの資料を消す。実践者の解説は、最初は少数のファイルにし、古い版は削除するよう勧める（根拠：弱）。確かめること：同じ内容の版が 2 つ残っていない。
3. 長い資料は、分ける・テキストに直すなど、形と量を整えてから入れ直す。方法は <!-- link:begin handing-long-documents#split-and-convert -->[長い資料を渡すとき › 分ける・形を直す](../context/handing-long-documents.md#split-and-convert)<!-- link:end --> にある。PDF やそれ以外の文書の読まれ方の違いと、分け方は <!-- link:begin how-attachments-are-read#splitting -->[添付ファイルはどこまで読まれるか › 大きな資料の分け方](how-attachments-are-read.md#splitting)<!-- link:end --> にある。確かめること：1 つの資料が 1 つの話題に収まっている。
4. 入れ直したら、新しい会話を始め、「容量に近づくと何が変わるか」の節の雛形で同じ質問を出す。確かめること：引用が資料にあり、絞る前より答えが資料を踏まえている。

!!! example "判断例：旧版や回答集が混ざったプロジェクトの絞り方"
    - **状況**：社内の経費規程を扱うプロジェクトである。ナレッジに、規程の現行版、旧版、過去の回答集、取引先からの一度きりのメールが入っている。最近、答えが条文を踏まえなくなった気がする。
    - **迷う候補**：旧版とメールだけを外して続ける。規程用と回答集用の 2 つに分ける。
    - **選んだもの**：まず旧版とメールだけを外し、引用つきの質問で確かめる。条文を踏まえるなら、分けない。
    - **理由**：外す手間は小さく、効いたかを同じ質問で比べられる。分けるのは、目的の混在が分かったときでよい。回答集が旧規程の時代のものなら、食い違う答えが紛れる。そのときは回答集を別のプロジェクトへ移す。

資料を差し替えるときは、古い版を消してから新しい版を入れる。古い版を残したまま新しい版を足すと、どちらの版が使われたかが会話ごとにぶれる。

## 効かない場面・落とし穴 {#pitfalls}

- 資料を絞っても直らない症状がある。指示が資料の使い方を決めていないと、資料が少なくても答えは資料を踏まえない。資料の使い方（資料にないときの扱いなど）は、プロジェクトの指示に書く（<!-- link:begin using-projects#instructions -->[プロジェクトの使いどころ › プロジェクトの指示に書くこと](using-projects.md#instructions)<!-- link:end -->）。
- 「RAG mode に切り替わったから質が下がった」と決めつけない。切り替わりの有無を画面で確かめる方法は、調べた範囲では確認できていない。原因が切り替わりか、混在か、指示かは、引用つきの質問で切り分ける。
- 有料プラン以外での扱いを、このページは確かめていない。RAG mode の自動の切り替えを書いた公式の説明は、有料プランについてだけである。自分のプランでの上限と挙動は、公式の説明と画面で確かめる。
- 資料を全部残したまま指示を強めても、資料の量による問題は直らない。指示はお願いなので、守られたかは出力で確かめる。
- 容量の目安の数値は、変わりやすいのでここに書かない。使える長さはモデルとプランで違うので、公式の説明を見る。
- 読み方が切り替わる仕組みを、他の機能に当てはめない。Claude Code で資料を読ませる場合は別の仕組みで、このページの対象外である。

## 比べる相手 {#compare}

プロジェクトのナレッジに置き続けるか、会話に添付するかで迷うときは、繰り返し使う資料をナレッジ、1 回きりの資料を添付にする。置く資料の選び方は <!-- link:begin using-projects#knowledge -->[プロジェクトの使いどころ › ナレッジを置くと何が変わるか](using-projects.md#knowledge)<!-- link:end --> にある。

添付ファイルの読まれ方（PDF の図まで読まれる範囲など）は、プロジェクトのナレッジとは別に決まる。内容は <!-- link:begin how-attachments-are-read#pdf-and-others -->[添付ファイルはどこまで読まれるか › PDF とそれ以外の文書](how-attachments-are-read.md#pdf-and-others)<!-- link:end --> で確かめる。長い資料を丸ごと渡さず、先に引用を抜かせる方法もある。手順は <!-- link:begin handing-long-documents#quotes-first -->[長い資料を渡すとき › 引用を先に抜かせる](../context/handing-long-documents.md#quotes-first)<!-- link:end --> で読める。

Claude Code では、読ませるファイルを @ で直接指し、長い出力を要点に絞る。アプリのナレッジとは仕組みが違うが、読ませる量を絞るという考え方は同じである（<!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](../context/choose-what-to-read.md#point-or-search)<!-- link:end -->）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)：Anthropic・英語・確認日 2026-11-04
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)：Anthropic・英語・確認日 2026-11-04
- [Claude Projects の解説記事（仁頼のブログ）](https://jinrai.co.jp/blog/2026/04/03/claude-projects-guide/)：仁頼・確認日 2026-11-05

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [プロジェクトの使いどころ](using-projects.md)

**関連**

- [添付ファイルはどこまで読まれるか](how-attachments-are-read.md)
- [長い資料を渡すとき](../context/handing-long-documents.md)
- [context rot と紛らわしい情報](../basics/context-rot.md)
- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
