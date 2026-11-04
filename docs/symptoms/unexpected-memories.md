---
id: unexpected-memories
title: 別の会話やプロジェクトの内容が混ざる
nav_title: 別の会話の内容が混ざる
aliases: [記憶が混ざる, 消した会話を覚えている, メモリの混乱]
type: symptom
field: symptoms
chapter: 会話と文脈
order: 160
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる]
prevents: [散らかっている, 境界がない]
pitfalls: []
scenes: [開発, 文章]
summary: 別の会話やプロジェクトの内容が混ざる・消したはずの内容を覚えている原因を、どの記憶の仕組みかから切り分け、範囲の分け方と消し方を決める。
signs:
  - {type: symptom, text: 別のプロジェクトの記憶が混ざる}
  - {type: symptom, text: 会話を消したのに覚えている}
  - {type: symptom, text: 前の会話で話した内容を勝手に持ち出される}
wave: 1
prerequisites: [where-instructions-sit]
related: [where-to-put-instructions, where-your-data-goes, forgets-in-long-chats, repeating-the-same-explanation, six-causes]
routes:
  - {cause: 散らかっている, to: [how-memory-works#manage, using-auto-memory#review, claude-md-loading-order]}
  - {cause: 境界がない, to: [how-memory-works, using-projects#scope, incognito-chats]}
tracks: [app-memory, chat-search, incognito, projects, auto-memory, claude-md]
outdated_advice: [memory-daily-summary]
sources: [hc-memory, hc-incognito, hc-projects-what, cc-docs-memory]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: to-fix}
  - {title: 判断例, anchor: examples}
  - {title: 予防, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：混ざった内容がどの記憶の仕組みから来たかを、安い順の確認で切り分け、範囲の分け方と消し方を決められる。
    - **いつ引くか**：別のプロジェクトの内容が出てきたとき、消した会話の内容を覚えていたとき、前の会話の話を勝手に持ち出されたとき。
    - **前提**：<!-- link:begin where-instructions-sit -->[システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)<!-- link:end -->

<!-- textlint-disable -->
別名：記憶が混ざる・消した会話を覚えている・メモリの混乱
<!-- textlint-enable -->

別の会話やプロジェクトの内容が混ざるのは、Claude が文脈とは別の場所に残った情報を、いまの会話に持ち込んでいる状態である。持ち込み元は 1 つではない。アプリではメモリ、過去の会話の検索、プロジェクトの資料と指示が、Claude Code では CLAUDE.md と自動メモリが、それぞれ別の範囲で働く。このページでは、持ち込んだ仕組みを切り分けて、直す先のページへ振り分ける。

## よくある形 {#forms}

読者の言葉で見ると、症状は 3 つの形で現れる。

- **別のプロジェクトの記憶が混ざる**：仕事の相談に、個人の用事の話が出てくる。別の案件の前提が、いまの案件の回答に入る。
- **会話を消したのに覚えている**：消した会話の内容を、新しい会話で Claude が口にする。
- **前の会話で話した内容を勝手に持ち出される**：頼んでいないのに、以前の好みや事情を前提にして答える。

3 つとも、持ち込み元を特定して初めて直せる。内容を消す前に、まず出どころを見る。

## 原因を安く確かめる順 {#diagnosis}

安く確かめられる順に並べた。上の項目で出どころが見つかれば、下は見なくてよい。原因の名前は、Claude 側の 6 つの原因のうち、この症状に関わる 2 つを使う。全体の診断は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

最初に、面を問わず 2 つを確かめる。

1. **同じ会話の中の話ではないか**（人の側の落とし穴）：混ざったと感じた内容が、実はいまの会話の前のほうで自分が書いたものだった、ということがある。会話の中を検索して確かめる。見つかれば記憶の問題ではなく、長い会話の問題である。<!-- link:begin forgets-in-long-chats#diagnosis -->[長い会話で前提を忘れる・雑になる › 原因を安く確かめる順](forgets-in-long-chats.md#diagnosis)<!-- link:end --> に進む。
2. **出たのはどの面か**：アプリ（claude.ai・Desktop・Mobile）と Claude Code では、持ち込み元が別である。アプリのメモリは Claude Code の記録とは別の仕組みなので、出た面のほうだけを見る。

次に、出た面のタブで確かめる。

=== "アプリ"

    1. **過去の会話の検索が走っていないか**（境界がない）：プランによっては、Claude が過去の会話を検索して答えに使うことがある。この検索は会話の中に道具の呼び出しとして表示される。呼び出しが出ていれば、持ち込み元は検索である。検索はメモリとは別の機能で、別の場所でオフにする。見る場所は <!-- link:begin how-memory-works#chat-search -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 過去チャットの検索との違い](../app/how-memory-works.md#chat-search)<!-- link:end --> にある。
    2. **メモリの項目に、混ざった内容があるか**（散らかっている）：設定でメモリの項目（Topics）を開き、混ざった内容と同じ話題の項目を探す。あれば持ち込み元はメモリである。古い内容や誤った内容が項目に溜まっている。直し方と消し方は <!-- link:begin how-memory-works#manage -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 覚えた内容を見る・直す（棚卸し）](../app/how-memory-works.md#manage)<!-- link:end --> にある。
    3. **症状が出たのは、プロジェクトの中か外か**（境界がない）：プロジェクトはそれぞれのメモリを持つ。プロジェクトの外の会話と中の会話で、見える記憶の範囲が違う。出た場所と、混ざった内容が生まれた場所を並べて、範囲をまたいでいないかを見る。範囲の仕組みは <!-- link:begin how-memory-works#scope -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › アカウントのメモリとプロジェクトのメモリ](../app/how-memory-works.md#scope)<!-- link:end --> にある。
    4. **プロジェクトのナレッジや指示に、その内容が入っていないか**（境界がない）：プロジェクトの中で混ざるなら、メモリではなく、プロジェクトに置いた資料や指示が出どころのこともある。目的の違う資料を同じプロジェクトに入れていると起きる。切る単位は <!-- link:begin using-projects#scope -->[プロジェクトの使いどころ › プロジェクトを切る単位（1つに1つの目的）](../app/using-projects.md#scope)<!-- link:end --> にある。
    5. **消したはずの内容なら、消したのは会話だけではないか**（散らかっている）：会話を消しても、その会話から作られたメモリの項目は残る。メモリの項目は別に消す必要がある。残るものの全体は <!-- link:begin how-memory-works#deleted-chats -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 会話を消しても残るもの](../app/how-memory-works.md#deleted-chats)<!-- link:end --> にある。

=== "Claude Code"

    1. **作業ディレクトリの上の階層に、別のプロジェクトの CLAUDE.md がないか**（境界がない）：CLAUDE.md は、作業ディレクトリから上の階層の分がセッション開始で読み込まれる。リポジトリを入れ子やモノレポで置いていると、隣の案件の指示が一緒に入る。読み込み元を確かめる。重なり方は <!-- link:begin claude-md-loading-order#monorepo -->CLAUDE.md の階層と読み込み順 › モノレポとほかのチームの指示（準備中）<!-- link:end --> にある。
    2. **サブディレクトリの CLAUDE.md が、あとから読み込まれていないか**（境界がない）：サブディレクトリの CLAUDE.md は、Claude がそのディレクトリのファイルを読み書きしたときに読み込まれる。作業の途中で別の領域に入ると、その領域の指示が加わり、回答の前提が変わる。
    3. **自動メモリに、誤った記録や古い記録が残っていないか**（散らかっている）：自動メモリは、セッション開始に MEMORY.md の頭の部分を読み込み、話題ごとのファイルは Claude が必要なときに読む。誤った結論が記録に残ると、後の作業に混ざる。記録を開いて、混ざった内容と同じ話題がないかを見る。見直し方は <!-- link:begin using-auto-memory#review -->自動メモリ › 誤った記録の見直し（準備中）<!-- link:end --> にある。
    4. **圧縮のあとに、指示の効き方が変わっていないか**（散らかっている）：圧縮のあと、プロジェクトの根の CLAUDE.md はディスクから入れ直される。入れ子の CLAUDE.md は要約に消え、必要になったときに読み直される。圧縮の前後で、出てくる指示の内容が変わったように見えるときは、この動きを疑う。

原因が見つからないときは、混ざった内容について Claude に尋ねる。たとえば「いまの内容は、この会話の発言・メモリ・過去の会話の検索・指示ファイルのどれから得たか」と聞く。答えは手がかりであって、証拠ではない。上の確認で裏を取る。

古い助言にも注意が要る。「メモリには翌日に反映される」という説明は、前の方式のものである。待たずに、項目を直接見て確かめる。行の詳細は <!-- link:begin outdated-advice-ledger#memory-daily-summary -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#memory-daily-summary)<!-- link:end --> にある。

## 原因ごとの対処 {#to-fix}

対処の本体は、各分野のページに任せる。見つけた原因に合わせて、次の表の行き先へ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 散らかっている | [アプリのメモリ（仕組み・範囲・消し方と止め方） › 覚えた内容を見る・直す（棚卸し）](../app/how-memory-works.md#manage)<br>自動メモリ › 誤った記録の見直し（準備中）<br>CLAUDE.md の階層と読み込み順（準備中） |
| 境界がない | [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)<br>[プロジェクトの使いどころ › プロジェクトを切る単位（1つに1つの目的）](../app/using-projects.md#scope)<br>シークレットチャット（記録を残さない会話）（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

表の読み方は次のとおりである。「散らかっている」は、残っている記録の中身を見て、直すか消す。「境界がない」は、記憶の範囲を分けて、混ざらないようにする。

アプリで消しても直らないときは、消した場所が違うことが多い。会話を消しても、メモリの項目は消えない。項目を消したら、新しい会話で同じ質問を試して確かめる。

## 判断例 {#examples}

!!! example "判断例：仕事の相談に個人の話が混ざる"
    - **状況**：アプリで仕事の文書の相談をすると、以前に個人の用事で話した内容が前提として出てくる。
    - **迷う候補**：メモリをすべて消す。該当の項目だけを消す。
    - **選んだもの**：先にメモリの項目を開き、該当の話題の項目だけを消す。そのうえで、個人の用事の相談は、記録を残さない会話か別のプロジェクトでする。
    - **理由**：すべて消すと、役に立っている記録まで失う。混ざった原因は、範囲が分かれていないことなので、項目を消すだけでは同じ混ざり方がまた起きる。消す作業と、今後の置き場所の見直しをセットにする。

!!! example "判断例：隣の案件の指示が Claude Code に入る"
    - **状況**：ある案件のリポジトリで作業していると、別の案件の規約に沿った提案が出る。
    - **迷う候補**：その案件の CLAUDE.md に「別の案件の規約は無視する」と書く。上の階層に置いた CLAUDE.md を見直す。
    - **選んだもの**：読み込まれている CLAUDE.md を階層ごとに確かめ、上の階層にある別の案件の分を、その案件の置き場所へ移す。
    - **理由**：CLAUDE.md は強制ではなく文脈なので、「無視する」と書いても効きが保証されない。出どころの置き場所を直すほうが確実で、文脈も減る。

## 予防 {#prevention}

混ざる症状は、置き場所と範囲を最初に決めておくと減る。注意に頼らず、仕組みに移す。

- **プロジェクトは、1 つに 1 つの目的で切る**：目的の違う資料や指示を混ぜない。切る単位は <!-- link:begin using-projects#scope -->[プロジェクトの使いどころ › プロジェクトを切る単位（1つに1つの目的）](../app/using-projects.md#scope)<!-- link:end --> にある。
- **残したくない相談は、記録を残さない会話にする**：履歴にもメモリにも残らない。一部は残るので、見分け方は <!-- link:begin incognito-chats#retention -->シークレットチャット（記録を残さない会話） › 残らないもの・残るもの（準備中）<!-- link:end --> にある。保持の考え方は <!-- link:begin where-your-data-goes#retention -->[送ったデータの行方（学習・保持期間） › 残る期間](../safety/where-your-data-goes.md#retention)<!-- link:end --> にある。
- **会話ごとにメモリを止めたいときは、最初のメッセージを送る前に切る**：後からは切り替えられない。手順は <!-- link:begin how-memory-works#turning-off -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 消し方と止め方（Pause・Reset・会話ごとのオフ・シークレットチャット）](../app/how-memory-works.md#turning-off)<!-- link:end --> にある。
- **メモリの項目と自動メモリの記録を、ときどき見る**：誤った記録や古い記録を早めに消せば、後の作業を汚さない。見る場所は <!-- link:begin how-memory-works#manage -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 覚えた内容を見る・直す（棚卸し）](../app/how-memory-works.md#manage)<!-- link:end --> と <!-- link:begin using-auto-memory#review -->自動メモリ › 誤った記録の見直し（準備中）<!-- link:end --> にある。
- **繰り返し頼む前提は、持ち主の置き場所へ移す**：毎回の説明を記憶に頼らず、置き場所に書く。選び方は <!-- link:begin where-to-put-instructions#how-to-choose -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › どこに置くかの選び方](../app/where-to-put-instructions.md#how-to-choose)<!-- link:end --> にある。説明の繰り返しが症状の本体なら <!-- link:begin repeating-the-same-explanation#diagnosis -->[毎回同じ説明をしている › 原因を安く確かめる順](repeating-the-same-explanation.md#diagnosis)<!-- link:end --> に進む。
- **人の側の落とし穴も疑う**：思い込みや目的の混在など、人の側の落とし穴は <!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end --> にまとまっている。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use Claude’s chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)：Anthropic・英語・確認日 2026-11-04
- [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)：Anthropic・英語・確認日 2026-11-04
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)

**次に読む**

- [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- 自動メモリ（準備中）
- CLAUDE.md の階層と読み込み順（準備中）
- [プロジェクトの使いどころ](../app/using-projects.md)
- シークレットチャット（記録を残さない会話）（準備中）

**関連**

- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- [長い会話で前提を忘れる・雑になる](forgets-in-long-chats.md)
- [毎回同じ説明をしている](repeating-the-same-explanation.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
