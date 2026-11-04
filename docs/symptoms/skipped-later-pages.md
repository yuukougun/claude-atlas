---
id: skipped-later-pages
title: 添付した資料の後半を読んでいない
aliases: [PDF の後半を読まない, 添付が全部読まれていない, 図を読んでいない]
type: symptom
field: symptoms
chapter: 事実と出典
order: 110
level: 使う
priority: 必須
surfaces: [app, api]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [調べもの, 学習]
summary: 添付した長い資料の後半や図が答えに使われない原因を、読み込みの範囲と注意の偏りから切り分け、分け方と、ページ番号付きの引用での確かめ方を決める。
signs:
  - {type: symptom, text: 長い PDF の後半の図について答えられない}
  - {type: symptom, text: 資料の途中から内容を取り違える}
  - {type: symptom, text: 添付したのに読んでいないような答えが返る}
wave: 1
prerequisites: [context-rot]
related: [documents-in-japanese, checking-citations, summary-overstates-source, forgets-in-long-chats, six-causes]
routes:
  - {cause: 見えていない, to: [how-attachments-are-read, handing-long-documents]}
  - {cause: 散らかっている, to: [long-context-first, too-much-project-knowledge]}
tracks: [file-creation, projects, files-api]
outdated_advice: []
sources: [hc-upload-files, arxiv-2307-03172, api-docs-reduce-hallucinations]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: routes-to-fixes}
  - {title: 似た症状との見分け, anchor: lookalikes}
  - {title: 判断例, anchor: example}
  - {title: 予防：読まれたかを毎回確かめる, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：添付した資料の後半や図が答えに使われない原因を、読み込みの範囲と注意の偏りに切り分け、分け方と引用での確かめ方を決められる。
    - **いつ引くか**：長い PDF の後半の図について答えられない・資料の途中から内容を取り違える・添付したのに読んでいないような答えが返る、とき。
    - **前提**：<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end -->

<!-- textlint-disable -->
別名：PDF の後半を読まない・添付が全部読まれていない・図を読んでいない
<!-- textlint-enable -->

添付した資料の後半を読んでいない症状は、資料の一部が答えの材料になっていないことである。Claude が一部を読めていない場合と、読めているのに使われていない場合の 2 通りがある。前者は読み込みの範囲の問題で、後者は注意の偏りの問題である。

どちらも、返答の文面だけでは区別できない。読んでいないページについても、それらしい答えは返ってくる。このページは、原因を切り分けて、読まれたかを引用で確かめるまでを受け持つ。

## よくある形 {#forms}

読まれていない形は、次の 4 つに分けると見分けやすい。

- **後半の図だけ答えられない**：本文の内容には答えるのに、長い PDF の後半にある図表について聞くと、答えられないか間違える。
- **途中から内容が混ざる**：資料の中ほどの記述が、前後の記述と取り違えられる。
- **画像が無視される**：Word などの文書に埋め込んだ画像が、答えに出てこない。
- **読んだふりの答え**：添付したのに、資料に書かれていないことを一般論で答える。資料の言葉が 1 つも引かれない。

## 原因を安く確かめる順 {#diagnosis}

診断は、手間の少ない確認から順に進める。最初に、資料の中の「答えに使われていない箇所」を特定する。どのページの何が使われていないかが分からないと、以下の確認が当てられない。

1. **見えていない**：その箇所が、そもそも Claude に渡る範囲の外にある。
    - 見るもの：資料の形式とページ数。図が根拠の箇所は、PDF のどのページにあるか。Word などの文書か、PDF か。
    - 確かめ方：添付した資料の長さを数え、読み込みの範囲と照らす。PDF は先頭から一定のページまでは文字と図表の両方が読まれ、その先は文字だけになる。PDF 以外の文書は、文字だけが取り出され、埋め込みの画像は読まれない。範囲の外にある図について聞いていたなら、これが原因である。範囲の値は <!-- link:begin how-attachments-are-read#pdf-and-others -->[添付ファイルはどこまで読まれるか › PDF とそれ以外の文書](../app/how-attachments-are-read.md#pdf-and-others)<!-- link:end --> にあり、API で渡すときの違いは <!-- link:begin how-attachments-are-read#api -->[添付ファイルはどこまで読まれるか › API で渡すとき（Files API・PDF・画像）](../app/how-attachments-are-read.md#api)<!-- link:end --> にある。
    - 日本語の PDF では、文字として読めているかも別に確かめる。確かめ方は <!-- link:begin documents-in-japanese#pdf -->日本語の資料を読ませる・書かせる › 日本語の PDF を渡す前と後に確かめること（準備中）<!-- link:end --> にある。
2. **見えていない（範囲の中で読まれたかの確認）**：範囲の中にあるはずなのに、読まれたか分からない。
    - 見るもの：答えに、資料の言葉やページの記述が引かれているか。
    - 確かめ方：答えに対応するページ番号と、そのページの原文の引用を出させ、原本を開いて文言を照らす。引用が出せない、または原本と合わないなら、その箇所は読まれていないか、使われていない。1 で範囲の外と言えないときは、次の 3 に進む。出させる依頼の雛形はこの節の末尾にある。引用を先に抜き出させる手法の考え方は <!-- link:begin handing-long-documents#quotes-first -->長い資料を渡すとき › 引用を先に抜かせる（準備中）<!-- link:end --> にあり、読まれたかの確かめ方の全体は <!-- link:begin how-attachments-are-read#verify -->[添付ファイルはどこまで読まれるか › 読まれたかを確かめる（ページの番号と引用）](../app/how-attachments-are-read.md#verify)<!-- link:end --> にある。
3. **散らかっている**：資料は読まれているが、長さや並びのせいで、その箇所が使われにくい。
    - 見るもの：依頼の中で、資料と質問をどの順に置いたか。長い入力の中ほどにある箇所を聞いていないか。
    - 確かめ方：資料を先頭に、質問を最後に置き直して、同じ質問をもう一度出す。中ほどの情報は使われにくい傾向がある（根拠：中。公刊は 2023 年で、対象は当時の言語モデルである。今の Claude にそのまま当てはまるとは限らない）。傾向の説明は前提の <!-- link:begin context-rot#lost-in-the-middle -->[context rot と紛らわしい情報 › 中ほどの情報は使われにくいか（lost in the middle）](../basics/context-rot.md#lost-in-the-middle)<!-- link:end --> にある。置き方は <!-- link:begin long-context-first#order -->[長い資料は先、質問は最後 › 資料を先、質問を最後に置く](../prompting/long-context-first.md#order)<!-- link:end --> にある。
4. **散らかっている**：資料を何点も添付している、またはプロジェクトのナレッジに資料を溜めている。
    - 見るもの：同じ会話やプロジェクトに入れた資料の数と、今回の質問に関係しない資料の量。
    - 確かめ方：質問に要る資料だけを新しい会話に入れ直して、同じ質問を出す。答えが改善するなら、余分な資料が邪魔をしていた。プロジェクトのナレッジが容量に近づくと読み方が変わる点は <!-- link:begin too-much-project-knowledge#rag-mode -->プロジェクトのナレッジが多すぎるとき › 容量に近づくと何が変わるか（準備中）<!-- link:end --> にある。

引用で確かめる依頼の雛形を、次に置く。資料を添付した後の、質問の部分に使う。この確かめ方は、公式が幻覚を減らす手法として挙げる「先に引用を抜き出させる」ことの応用である。

<!-- gen:begin snippet skipped-later-pages/quote-with-pages -->
<!-- textlint-disable -->

??? example "雛形：ページ番号付きの引用を先に出させる依頼"

    ```text
    添付した資料について答える前に、根拠を先に出して。

    1. 質問に関係する箇所を、ページ番号を付けて原文のまま引用する。要約や言い換えにしない。
    2. 図や表が根拠になるときは、図表の番号と題、軸や凡例の文字を書く。
    3. 該当する箇所が見つからないとき、または読めなかったときは、推測で埋めずに「読めていない」と書く。
    4. 答えは、1 から 3 で挙げた引用だけを根拠にして書く。

    質問：（ここに質問を書く）
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet skipped-later-pages/quote-with-pages -->

## 原因ごとの対処 {#routes-to-fixes}

診断で当たった原因に対応する対処は、次の表のページにある。このページは切り分けまでを受け持ち、対処の本体は書かない。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)<br>長い資料を渡すとき（準備中） |
| 散らかっている | [長い資料は先、質問は最後](../prompting/long-context-first.md)<br>プロジェクトのナレッジが多すぎるとき（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 似た症状との見分け {#lookalikes}

資料の読まれ方に見える症状は、ほかにも出る。次のように見分ける。

- 資料は読まれているのに、要約が原文より断定的になる：<!-- link:begin summary-overstates-source#diagnosis -->[要約が原文より断定的になる › 原因を安く確かめる順](summary-overstates-source.md#diagnosis)<!-- link:end --> で、落ちた条件や但し書きを原文と照らす。
- 長い会話の途中から、前の指示や前提を忘れる：<!-- link:begin forgets-in-long-chats#diagnosis -->[長い会話で前提を忘れる・雑になる › 原因を安く確かめる順](forgets-in-long-chats.md#diagnosis)<!-- link:end --> で、会話に溜まった情報を切り分ける。
- 引用や出典の文言が原文と違う：<!-- link:begin checking-citations#steps -->引用や出典の確かめ方 › 確かめる手順（準備中）<!-- link:end --> で、原文を開いて照らす。
- どの原因から疑うか迷う：<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> が、Claude 側の 6 つの原因を安く確かめる順に並べている。

## 判断例 {#example}

!!! example "判断例：長い PDF の後半の図について答えられない"
    - **状況**：図表の多い長い PDF を添付して、後半の章の図の内容を尋ねた。返答は本文の説明に終始し、図の中身には触れない。
    - **迷う候補**：A は、PDF の全体を添付し直して、「後半の図もちゃんと読んで」と依頼に足す。B は、図が必要な章を、図まで読まれる範囲に収まるように分けて添付し、ページ番号付きの引用を先に出させる。
    - **選んだもの**：B。
    - **理由**：A は、図まで読まれる範囲を超えているなら、足した一言では何も変わらない。範囲の外の図は、読まれずにそれらしい説明で埋められやすい。B は、図の載るページを範囲の中に入れ、引用で読まれたかを確かめられる。引用が出せなければ、その図は読まれていないと分かり、その時点で分け方を見直せる。

## 予防：読まれたかを毎回確かめる {#prevention}

予防の考え方は、読まれたと信じて進まず、確かめる手段を依頼に組み込むことである。

- 図が根拠になる資料は、渡す前に分ける。分け方は <!-- link:begin how-attachments-are-read#splitting -->[添付ファイルはどこまで読まれるか › 大きな資料の分け方](../app/how-attachments-are-read.md#splitting)<!-- link:end --> にある。形や量の整え方は <!-- link:begin handing-long-documents#split-and-convert -->長い資料を渡すとき › 分ける・形を直す（準備中）<!-- link:end --> にある。
- 答えを求める依頼に、ページ番号付きの引用を先に出させる指示を含める。引用が資料の中にあるかを、原本で照らす。
- 資料は依頼の先頭、質問は最後に置く。引用を答えの前に抜かせる使い方は <!-- link:begin long-context-first#quote-first -->[長い資料は先、質問は最後 › 答えの前に引用を抜かせる](../prompting/long-context-first.md#quote-first)<!-- link:end --> にある。
- プロジェクトのナレッジには、使う資料だけを入れ、不要になった資料は外す。絞り方は <!-- link:begin too-much-project-knowledge#curate -->プロジェクトのナレッジが多すぎるとき › 資料の絞り方と入れ直し方（準備中）<!-- link:end --> にある。
- 読み込みの範囲は面や時期で変わる。値は本文に頼らず、<!-- link:begin how-attachments-are-read#pitfalls -->[添付ファイルはどこまで読まれるか › 効かない場面・落とし穴](../app/how-attachments-are-read.md#pitfalls)<!-- link:end --> と公式の文書で、使う面について確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude)：Anthropic・英語・確認日 2026-11-04
- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)：arXiv（Liu, Nelson F. ほか）・英語・確認日 2026-11-04
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [context rot と紛らわしい情報](../basics/context-rot.md)

**次に読む**

- [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- 長い資料を渡すとき（準備中）
- [長い資料は先、質問は最後](../prompting/long-context-first.md)
- プロジェクトのナレッジが多すぎるとき（準備中）

**関連**

- 日本語の資料を読ませる・書かせる（準備中）
- 引用や出典の確かめ方（準備中）
- [要約が原文より断定的になる](summary-overstates-source.md)
- [長い会話で前提を忘れる・雑になる](forgets-in-long-chats.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
