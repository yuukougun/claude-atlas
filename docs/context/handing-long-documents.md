---
id: handing-long-documents
title: 長い資料を渡すとき
aliases: [PDF を渡す, 長文を読ませる, 資料を分けて渡す]
type: concept
field: context
chapter: 見る・絞る
order: 130
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる, 確かめる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [調べもの, 文章, データ分析]
summary: 長い資料は、分けたり、テキストや Markdown に直したりして、形と量を整えてから渡す。面ごとの読み込みの限界を知っておくと、読まれていない部分に気づける。
signs:
  - {type: goal, text: 長い PDF や仕様書をもとに答えさせたい}
  - {type: goal, text: 長い資料を、読み落とされにくい形にしてから渡したい}
prerequisites: [attention-budget]
related: [how-attachments-are-read, long-context-first, skipped-later-pages, context-rot#lost-in-the-middle, checking-citations, summary-overstates-source, choose-what-to-read, too-much-project-knowledge, documents-in-japanese, research-and-reports]
tracks: []
outdated_advice: []
sources: [hc-upload-files, api-docs-files, stulberg-code-everything-code-tips-tricks]
volatility: 中
sections:
  - {title: 長い資料を丸ごと渡したとき, anchor: what-happens}
  - {title: 引用を先に抜かせる, anchor: quotes-first}
  - {title: 分ける・形を直す, anchor: split-and-convert}
  - {title: 面ごとの読み込みの限界, anchor: limits}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：長い資料は、分ける・テキストや Markdown に直すなどして形と量を整えてから渡すと、読み落としが減る理由とやり方。
    - **いつ引くか**：長い PDF や仕様書をもとに答えさせたいとき。長い資料を、読み落とされにくい形にしてから渡したいとき。
    - **前提**：<!-- link:begin attention-budget -->[コンテキストウィンドウと注意の予算](../basics/attention-budget.md)<!-- link:end -->

<!-- textlint-disable -->
別名：PDF を渡す・長文を読ませる・資料を分けて渡す
<!-- textlint-enable -->

長い資料を渡すときは、何をどの形でどれだけ見せるかを、渡す側が先に決める。資料の形と量を整えることが、答えの質を左右する。

## 長い資料を丸ごと渡したとき {#what-happens}

長い資料を丸ごと添付して質問しても、答えが資料の一部にしか触れないことがある。

たとえば 200 ページの仕様書 PDF を添付して、「この仕様で、この操作は許されるか」と聞く。返ってきた答えは本文の説明だけで、後ろの付録の例外規定は扱われていない。読めなかったのか、読んだのに使わなかったのか、見ただけでは分からない。

原因は複数ある。

- 読み込みの範囲の外にある。面ごとに、読まれるページ数や、図まで読まれるかどうかに限りがある。
- 範囲の中にあっても、注意が薄い。入力が長いほど、中ほどの情報は使われにくくなる傾向がある。詳しくは <!-- link:begin context-rot#lost-in-the-middle -->[context rot と紛らわしい情報 › 中ほどの情報は使われにくいか（lost in the middle）](../basics/context-rot.md#lost-in-the-middle)<!-- link:end --> にある。
- 資料の形が読み取りに向いていない。文字が画像になっている、段組や表が崩れる、といった形である。
- 質問に関係のない部分が多すぎて、肝心の箇所が埋もれる。

読まれていないと疑う症状の側から入るなら、<!-- link:begin skipped-later-pages -->[添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)<!-- link:end --> が原因の切り分けを持つ。このページは、渡す前に資料をどう用意するかを扱う。

## 引用を先に抜かせる {#quotes-first}

答えの前に、関係する箇所を原文から引用させると、どこを根拠にしたかが見え、取りこぼしに気づきやすい。依頼の中の並べ方と引用のさせ方は、<!-- link:begin long-context-first#quote-first -->[長い資料は先、質問は最後 › 答えの前に引用を抜かせる](../prompting/long-context-first.md#quote-first)<!-- link:end --> が持つ。

このページで足すのは、資料を分けて渡したときの使い方だけである。分けた部品ごとに引用を出させると、どの部品が答えに使われ、どの部品が使われていないかが分かる。引用が原文と合っているかは、<!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end --> の手順で原文を開いて確かめる。

## 分ける・形を直す {#split-and-convert}

資料を渡す前にすることは 2 つある。質問に関係する範囲へ絞る（量を整える）ことと、読み取りやすい形に直す（形を整える）ことである。

量を整えるには、章や節の単位で分ける。

- 質問に関係する章だけを渡す。目次と、用語や定義の章は、章をまたいで参照されやすいので一緒に付ける。
- 分けた部品には、章の番号や題を含む名前を付ける。答えの根拠を指すときに、どの部品か分かる。
- 質問が変わったら、渡す部品も変える。全部を毎回渡さない。

絞る理由は、広い机の比喩で説明できる。机の広さに限りがなくても、載せた資料が多いほど、1 枚ごとへの目配りは薄くなる。仕組みは <!-- link:begin attention-budget#why -->[コンテキストウィンドウと注意の予算 › 広い机でも一枚ごとの目配りは薄くなる](../basics/attention-budget.md#why)<!-- link:end --> にある。

形を整えるには、PDF や Office の文書を、テキストや Markdown に直してから渡す。実践者の記事は、PDF・Word・Excel・PowerPoint を Markdown に直す変換ツール（たとえば markitdown）で、元資料をきれいにしてから渡す使い方を挙げている（根拠：弱）。直した結果は、次の点を元の資料と見比べる。

- 表の行や列が崩れていないか。
- 数式や脚注が抜けていないか。
- 図が落ちていないか。図が答えに必要なら、図の部分は元の PDF のまま渡すか、図の説明を文章で足す。

日本語の PDF は、読めたかを引用で確かめてから使う。手順は <!-- link:begin documents-in-japanese#pdf -->日本語の資料を読ませる・書かせる › 日本語の PDF を渡す前と後に確かめること（準備中）<!-- link:end --> にある。

渡し方は面で違う。

=== "アプリ"

    会話に添付するか、プロジェクトのファイルに入れる。繰り返し使う資料はプロジェクトに入れてよいが、入れすぎると読まれ方が変わる。絞り方は <!-- link:begin too-much-project-knowledge#curate -->プロジェクトのナレッジが多すぎるとき › 資料の絞り方と入れ直し方（準備中）<!-- link:end --> にある。PDF とそれ以外の文書の読まれ方の違いは <!-- link:begin how-attachments-are-read#pdf-and-others -->[添付ファイルはどこまで読まれるか › PDF とそれ以外の文書](../app/how-attachments-are-read.md#pdf-and-others)<!-- link:end --> が、分け方の目安は <!-- link:begin how-attachments-are-read#splitting -->[添付ファイルはどこまで読まれるか › 大きな資料の分け方](../app/how-attachments-are-read.md#splitting)<!-- link:end --> が持つ。

=== "Claude Code"

    資料をファイルとして作業ディレクトリに置き、読ませるファイルを @ で直接指す。長い資料は、先に分けるか Markdown にしてから置く。指し方と、大きなファイルの扱いの注意は <!-- link:begin choose-what-to-read#caveats -->[@参照と、何を読ませるかの絞り込み › @ 参照の注意](choose-what-to-read.md#caveats)<!-- link:end --> にある。PDF を Claude Code がどこまで読むかは、このページでは確かめていない（未確認）。

=== "API"

    一度上げたファイルを、後の要求から ID で指せる Files API がある。上げ方と、PDF・画像の渡し方は <!-- link:begin how-attachments-are-read#api -->[添付ファイルはどこまで読まれるか › API で渡すとき（Files API・PDF・画像）](../app/how-attachments-are-read.md#api)<!-- link:end --> にある。

!!! example "判断例：150 ページの仕様書で、認証の仕様だけ知りたい"
    - **状況**：150 ページの仕様書 PDF がある。知りたいのは、認証の章の仕様だけである。
    - **迷う候補**：資料を丸ごと渡す。認証の章だけを抜いて渡す。
    - **選んだもの**：認証の章に、目次と用語の章を付けて渡す。
    - **理由**：関係のない章が減るほど、肝心の箇所が埋もれにくく、読み込みの範囲の外に出る心配も減る。丸ごとのほうが安全に見えるが、読まれなかった所に気づきにくい。

    - **例外**：認証の仕様が他の章の定義に依存するなら、その章も足す。章をまたぐ質問なら、丸ごと渡して引用で確かめる。

## 面ごとの読み込みの限界 {#limits}

添付した資料が、どこまで読まれるかには、面ごとの限りがある。限りを知っておくと、答えに使われていない部分を、読み込みの範囲の外にあったためと疑える。

アプリで PDF を添付したときの範囲は、<!-- fact:begin app-pdf-visual-pages -->100 ページまで（文字と視覚要素）（2026-11-04 時点）<!-- fact:end -->。さらに、<!-- fact:begin app-pdf-text-only-pages -->101〜1000 ページは文字だけが読まれ、1000 ページを超えると拒否される（2026-11-04 時点）<!-- fact:end -->。つまり、範囲を超えた後ろのページにある図や表の見た目は、答えに反映されない。PDF 以外の文書は、図や画像が読まれない前提で考える。詳しい仕様は <!-- link:begin how-attachments-are-read#pdf-and-others -->[添付ファイルはどこまで読まれるか › PDF とそれ以外の文書](../app/how-attachments-are-read.md#pdf-and-others)<!-- link:end --> が持つ。

Claude Code と API の限りは、このページでは数えない。API で渡すときの違いは <!-- link:begin how-attachments-are-read#api -->[添付ファイルはどこまで読まれるか › API で渡すとき（Files API・PDF・画像）](../app/how-attachments-are-read.md#api)<!-- link:end --> を引く。

限りの内側にあっても、読まれたとは限らない。渡した直後に、資料の最初・中ほど・最後から引用させると、読まれたかを安く確かめられる。質問は資料の後に置く。

<!-- gen:begin snippet handing-long-documents/read-check -->
<!-- textlint-disable -->

??? example "雛形：読まれたかを引用で確かめてから答えさせる依頼"

    ```text
    添付した <資料名> を、次の順で扱って。

    1. 質問に答える前に、資料の最初・中ほど・最後から、それぞれ 1 か所ずつ原文を引用して。引用にはページ番号か見出しを付ける。
    2. 引用できなかった部分があれば、その部分は読めていないと書く。推測で補わない。
    3. そのあとで、下の質問に答える。答えの根拠にした箇所は、ページ番号付きの引用で示す。

    質問：<質問>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet handing-long-documents/read-check -->

確かめ方の全体は <!-- link:begin how-attachments-are-read#verify -->[添付ファイルはどこまで読まれるか › 読まれたかを確かめる（ページの番号と引用）](../app/how-attachments-are-read.md#verify)<!-- link:end --> に、毎回確かめる予防は <!-- link:begin skipped-later-pages#prevention -->[添付した資料の後半を読んでいない › 予防：読まれたかを毎回確かめる](../symptoms/skipped-later-pages.md#prevention)<!-- link:end --> にある。

## 何に効くか {#effects}

資料の形と量を整えることは、原理「見せる」と「確かめる」に効き、原因「見えていない」と「散らかっている」を防ぐ。

- **見えていない（原理：見せる）**：読み込みの範囲の外にあるものや、読み取れない形の資料は、Claude に見えていない。範囲の内に収め、読める形に直すことで、見える状態にする。
- **散らかっている（原理：見せる）**：関係のない部分が多いと、肝心の箇所の注意が薄くなる。関係する範囲に絞ることで、机の上を片付ける。<!-- link:begin attention-budget#effects -->[コンテキストウィンドウと注意の予算 › 何に効くか：見せることと、散らかっていること](../basics/attention-budget.md#effects)<!-- link:end --> が、この効き方を持つ。
- **確かめる（原理：確かめる）**：引用を先に抜かせ、ページ番号付きで原文と照らすと、読まれたかと、読み違いがないかを確かめられる。

資料を渡す量の判断例は、<!-- link:begin attention-budget#examples -->[コンテキストウィンドウと注意の予算 › 資料を渡す量の判断例](../basics/attention-budget.md#examples)<!-- link:end --> にもある。

## 誤解 {#misconceptions}

**「コンテキストウィンドウに入る量なら、全部読まれる」**：入ることと、よく使われることは別である。入力が長いほど、中ほどの情報は使われにくくなる傾向がある。ウィンドウの広さと注意の関係は <!-- link:begin attention-budget#misconceptions -->[コンテキストウィンドウと注意の予算 › 誤解](../basics/attention-budget.md#misconceptions)<!-- link:end --> にある。

**「要約を渡せば、原文と同じに使える」**：要約は、条件や但し書きが落ちて、原文より断定的になりやすい。原文か自分の要約かの選び方は <!-- link:begin long-context-first#source-or-summary -->[長い資料は先、質問は最後 › 原文を見せるか、自分の要約を渡すか](../prompting/long-context-first.md#source-or-summary)<!-- link:end --> が、落ちた条件の見つけ方は <!-- link:begin summary-overstates-source -->[要約が原文より断定的になる](../symptoms/summary-overstates-source.md)<!-- link:end --> が持つ。

**「Markdown に直せば、完全に読める」**：変換で表や図の一部が欠けても、気づきにくい。直した後は、元の資料と見比べる。

**「細かく分けるほどよい」**：章をまたぐ定義や参照は、分けると切れる。分けた後も、依存する章は一緒に渡す。

調べものの全体の進め方は <!-- link:begin research-and-reports -->[調べものとレポート](../recipes/research-and-reports.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude)：Anthropic・英語・確認日 2026-11-04
- [Files API](https://platform.claude.com/docs/en/build-with-claude/files)：Anthropic・英語・確認日 2026-11-04
- [Claude Code for Everything: Keeping Up with the Claude Code Treadmill (30 Claude Code Tips & Tricks)](https://hannahstulberg.substack.com/p/claude-code-for-everything-30-claude-code-tips-and-tricks)：Hannah Stulberg・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)

**関連**

- [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- [長い資料は先、質問は最後](../prompting/long-context-first.md)
- [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)
- [context rot と紛らわしい情報 › 中ほどの情報は使われにくいか（lost in the middle）](../basics/context-rot.md#lost-in-the-middle)
- [引用や出典の確かめ方](../verify/checking-citations.md)
- [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)
- [@参照と、何を読ませるかの絞り込み](choose-what-to-read.md)
- プロジェクトのナレッジが多すぎるとき（準備中）
- 日本語の資料を読ませる・書かせる（準備中）
- [調べものとレポート](../recipes/research-and-reports.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
