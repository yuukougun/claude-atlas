---
id: long-context-first
title: 長い資料は先、質問は最後
aliases: [Long context prompting, 資料を先頭に置く, 先に引用を抜かせる]
type: concept
field: prompting
chapter: 資料と入力の渡し方
order: 120
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない, 散らかっている]
scenes: [調べもの, 文章, 学習]
summary: 長い資料は依頼の先頭に置き、質問と指示を最後に書くと答えの質が上がる。答えの前に関係する箇所を原文から引用させると、誤読と取りこぼしを確かめやすい。
signs:
  - {type: symptom, text: 長い資料を渡すと、質問の肝心な所を外す}
  - {type: goal, text: 複数の文書を読ませて比べたい}
  - {type: goal, text: 資料のどこを根拠にしたのか示してほしい}
prerequisites: [attention-budget]
related: [handing-long-documents, context-rot#lost-in-the-middle, xml-tags, checking-citations, skipped-later-pages, documents-in-japanese, think-before-asking, allow-i-dont-know]
sources: [api-docs-prompting-best-practices, api-docs-reduce-hallucinations, cc-docs-best-practices, arxiv-2403-11164]
volatility: 低
sections:
  - {title: 資料を先、質問を最後に置く, anchor: order}
  - {title: 答えの前に引用を抜かせる, anchor: quote-first}
  - {title: 原文を見せるか、自分の要約を渡すか, anchor: source-or-summary}
  - {title: なぜ効くか、何に効くか, anchor: why}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：長い資料は依頼の先頭、質問と指示は最後に置き、答えの前に原文の引用を抜かせると、読み違いに気づきやすい。
    - **いつ引くか**：長い資料を渡すと質問の肝心な所を外すとき。複数の文書を読ませて比べたいとき。資料のどこを根拠にしたのか示してほしいとき。
    - **どこまで効くか**：並べ方は答えの質を上げるが、読み違いを無くさない。引用は根拠の目印であり、引用が原文と合うかは自分で確かめる。
    - **前提**：<!-- link:begin attention-budget -->[コンテキストウィンドウと注意の予算](../basics/attention-budget.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Long context prompting・資料を先頭に置く・先に引用を抜かせる
<!-- textlint-enable -->

「長い資料は先、質問は最後」とは、1 回の依頼の中で、資料を先頭に、質問と指示を末尾に置く頼み方である。ここで扱うのは依頼の中の並べ方と、答えの前に引用を抜かせる使い方だけである。資料の形や量を整える方法は <!-- link:begin handing-long-documents#split-and-convert -->[長い資料を渡すとき › 分ける・形を直す](../context/handing-long-documents.md#split-and-convert)<!-- link:end --> が持つ。

## 資料を先、質問を最後に置く {#order}

長い資料を渡すときは、資料を依頼の先頭に置き、質問と指示を末尾に書く。次は説明のために作った依頼の例で、Claude に試した結果ではない。

**Before**（質問が先頭にあり、資料が後ろにある）

```text
2 つの契約書の、解約の条件の違いを表にまとめて。

契約書 A：
（本文を貼る）

契約書 B：
（本文を貼る）
```

**After**（資料が先で、質問と指示が最後にある）

<!-- gen:begin snippet long-context-first/docs-then-question -->
<!-- textlint-disable -->

??? example "雛形：資料を先、質問を最後に置く依頼の雛形"

    ```text
    <documents>
      <document>
        <source>契約書A.pdf</source>
        <document_content>
        （契約書 A の本文をここに貼る）
        </document_content>
      </document>
      <document>
        <source>契約書B.pdf</source>
        <document_content>
        （契約書 B の本文をここに貼る）
        </document_content>
      </document>
    </documents>

    上の 2 つの契約書の、解約の条件（予告期間・違約金・手続き）の違いを表にまとめて。
    読み手は契約を結ぶ事業部の担当者で、法務の専門家ではない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet long-context-first/docs-then-question -->

After は、Before と同じ依頼に 3 つを足している。資料を質問より前に移した。資料ごとに、名前を `<source>`、本文を `<document_content>` に入れ、`<document>` で包んだ。質問に、何を比べるか（予告期間・違約金・手続き）と、読み手を足した。

公式の Prompting best practices は、長い文書を先頭に置き、質問と指示を最後に置くよう勧める。複数の文書を渡すときは、各文書を `<document>` で包み、名前を `<source>`、本文を `<document_content>` に入れる形も挙げる。公式は、この並べ方で自社のテストの品質が<!-- fact:begin long-context-order-quality-gain -->最大 30%（2026-10-29 時点）<!-- fact:end -->上がり、複数の文書を渡す場合に特に効いたと述べる。テストの中身はこの辞典では確かめていないので、効き目の大きさは自分の資料で試して確かめる。

資料を包むタグの考え方は <!-- link:begin xml-tags#nesting -->XML タグで区切る › 文書を入れ子にする（準備中）<!-- link:end --> が、指示と資料を分ける理由は <!-- link:begin xml-tags#separate -->XML タグで区切る › 指示・資料・例を分ける（準備中）<!-- link:end --> が扱う。

資料を渡す手段は、面で違う。

=== "アプリ"

    資料を本文に貼るときは、先に貼り、質問は貼った後に書く。ファイルを添付するときは、添付が本文のどこに置かれるかを自分では決められない。この辞典は、添付と本文の並びの扱いを確かめていない（未確認）。本文の側で、質問と指示を最後に書く。どの添付を指すかは、ファイル名で書く。

=== "Claude Code"

    長い資料は、貼るより、ファイルのまま読ませることが多い。`@` とパスで指したファイルの中身は依頼に入る。このとき並べ方で決められるのは、依頼の本文のどこで指すかである。資料を依頼の本文に貼るなら、先に貼り、質問は最後に書く。引用を抜かせる使い方（次の節）は、どちらの渡し方でも同じに使える。

=== "API"

    `messages` の `user` の本文に、資料を先に、質問を最後に入れる。複数の文書は、上の雛形のように文書ごとにタグで包む。画像や PDF を渡すブロックと質問のテキストを同じメッセージに入れるときも、資料のブロックを先に置き、質問のテキストを後ろに置く。

後半が読まれていないと感じるときは、並べ方の前に読み込みの範囲を疑う。切り分けの順は <!-- link:begin skipped-later-pages#diagnosis -->[添付した資料の後半を読んでいない › 原因を安く確かめる順](../symptoms/skipped-later-pages.md#diagnosis)<!-- link:end --> にある。

## 答えの前に引用を抜かせる {#quote-first}

引用を先に抜かせるとは、質問に答える前に、関係する箇所を資料から原文のまま書き出させ、答えをその引用に基づかせる頼み方である。公式の Prompting best practices は、回答の前に関係する部分を引用させ、根拠を固めるよう勧める。

雛形は、資料の後ろの質問の位置に、引用の指示を足した形である。

<!-- gen:begin snippet long-context-first/quote-first -->
<!-- textlint-disable -->

??? example "雛形：答えの前に引用を抜かせる依頼の雛形"

    ```text
    （資料は、<documents> で包んで、質問より先に置く）

    質問：2 つの契約書の、解約の条件（予告期間・違約金・手続き）の違いは何か。

    答える前に、質問に関係する箇所を、どの資料のものかを付けて、原文のまま <quotes> に抜き出して。
    関係する箇所が見つからない資料は、「該当なし」と書いて。
    そのあとで、<quotes> に抜き出した内容だけに基づいて、違いを <answer> に書いて。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet long-context-first/quote-first -->

引用の指示は、答えの前の段が 1 つ増えるだけである。そのため次の 3 つを確かめやすくなる。

- 取りこぼしを見つける。質問に関係するはずの箇所が引用に並んでいなければ、そこが読まれていない
- 誤読を見つける。引用と答えを見比べて、答えが引用から言える範囲を超えていないかを見る
- 根拠を示す。答えのどの文が、資料のどこに基づくかが分かる。複数の資料では、引用に資料の名前を付けさせると、どの資料の話かも分かる

公式の Reduce hallucinations は、とくに長い文書（目安は<!-- fact:begin long-context-quote-first-length-threshold -->約 20000 トークン超（2026-10-29 時点）<!-- fact:end -->）では、先に逐語の引用を抜き出させ、その引用だけに基づいて分析させる対策を挙げる。同じ文書は、「分からない」と言ってよいと明示することや、資料だけを使わせることも、対策に挙げる。これらは作り話を大きく減らすが、無くさない。重要な情報、特に重大な判断に関わるものは検証するよう、公式も書く。

引用が原文と合っているかは、自分で原文を開いて確かめる。確かめ方は <!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end --> にある。誤りの形は <!-- link:begin checking-citations#error-types -->[引用や出典の確かめ方 › よくある誤りの形](../verify/checking-citations.md#error-types)<!-- link:end --> にある。「分からない」と言ってよい、資料だけを根拠にする、という添え方は <!-- link:begin allow-i-dont-know#escape-hatch -->[「分からない」と言ってよいと伝える › 分からないと言える逃げ道を作る](allow-i-dont-know.md#escape-hatch)<!-- link:end --> と <!-- link:begin allow-i-dont-know#source-only -->[「分からない」と言ってよいと伝える › 渡した資料だけを根拠にさせる](allow-i-dont-know.md#source-only)<!-- link:end --> が扱う。

## 原文を見せるか、自分の要約を渡すか {#source-or-summary}

理解と確認のために資料を読ませるときは、自分の要約ではなく原文を渡す。要約は、要約した人の読み違いを含み、その読み違いは Claude には見えないまま引き継がれる。原文があれば、引用の抜き出しで読み違いを見つけられる。

要約を渡すほうが筋の通る場面もある。独自の発想が要る場面では、課題文や先行事例をそのまま貼ると、その言葉づかいに考えが引きずられることがある。そこでは、自分の言葉で抽象化した構造を先に作り、それを渡す助言がある。ただしこれは、画像生成でのデザイン固定化の研究から当てはめた考えで、Claude への依頼では確かめられていない（根拠：弱・類推）。この助言を使うのは、発想を広げたい場面に限る。

!!! example "判断例：複数の仕様書を読ませて差分を調べる"
    - **状況**：旧版と新版の仕様書（どちらも長い）を渡し、互換性を壊す変更を洗い出したい。
    - **迷う候補**：自分で両方を要約して渡す案と、原文を 2 つとも渡す案。要約のほうが短く、安く済む。
    - **選んだもの**：原文を 2 つとも渡し、引用を先に抜かせる。
    - **理由**：目的は差分の見落としを減らすことであり、要約で落ちた変更は Claude にも自分にも見えなくなる。原文なら、引用に出ない変更を見て、取りこぼしに気づける。

発想の段階の使い分けは <!-- link:begin think-before-asking#self-first -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI](../judgment/think-before-asking.md#self-first)<!-- link:end --> が扱う。この辞典の推奨は、理解と確認なら原文を見せ、発想を広げたいときに限って、自分の言葉の要約を先に作ることである。

## なぜ効くか、何に効くか {#why}

資料を先、質問を最後に置き、答えの前に引用を抜かせる頼み方は、原理の「見せる」を、散らかっていない形で実行するものである。防ぐ原因は、Claude 側の原因のうち「見えていない」と「散らかっている」である。

「見えていない」に効くのは、原文を渡すことと、引用で読めた所を確かめられることである。要約や記憶に頼らず、判断の材料を原文のまま依頼へ入れる。引用は、読まれた所を見える形にする。

「散らかっている」に効くのは、資料・質問・指示の区別をはっきりさせることである。コンテキストウィンドウに入ることと、中身をよく使えることは別で、情報が増えるほど個々の情報への注意は薄くなる。広い机に資料を何枚も広げたまま質問を挟むと、どれが資料でどれが頼みごとか分かりにくい。資料を先にまとめ、質問を最後に置き、タグで区切ると、机の上の並びが整う（<!-- link:begin attention-budget -->[コンテキストウィンドウと注意の予算](../basics/attention-budget.md)<!-- link:end -->）。

資料を先に置く並べ方がなぜ効くのかを、公式は説明していない。長い入力の途中の情報が使われにくいことは知られている（<!-- link:begin context-rot#lost-in-the-middle -->[context rot と紛らわしい情報 › 中ほどの情報は使われにくいか（lost in the middle）](../basics/context-rot.md#lost-in-the-middle)<!-- link:end -->）。質問が最後にあれば、資料を読み終えた直後に問いが目に入る、という見方はできる。ただし内部の動きまでは断定できない（推論・実践例なし）。

## 効かない場面とやりすぎ {#limits}

この並べ方と引用の抜き出しは、効かない場面がある。

- 短い資料では差が小さい。公式が勧めるのは長い資料の場合で、数行の貼り付けなら、並べ方にこだわらなくてよい
- 引用の指示は、出力を長くする。要点だけでよい質問や、1 行で答えられる質問には重い
- 引用は、原文と合っているとは限らない。引用の体裁でも細部が違うことがある。大事な箇所は原文を開いて確かめる
- 質問に関係する箇所が資料に無いと、引用が空になるか、近い箇所を無理に探す。「該当なし」と書いてよいと添える
- 資料が読み込めていないと、並べ方では直らない。PDF の図や、面ごとの読み込みの限界は <!-- link:begin handing-long-documents#limits -->[長い資料を渡すとき › 面ごとの読み込みの限界](../context/handing-long-documents.md#limits)<!-- link:end --> が、日本語の PDF は <!-- link:begin documents-in-japanese#pdf -->[日本語の資料を読ませる・書かせる › 日本語の PDF を渡す前と後に確かめること](../japanese/documents-in-japanese.md#pdf)<!-- link:end --> が扱う

やりすぎの例は、すべての依頼に引用の段と何重ものタグを足すことである。長い資料を読ませて根拠を確かめたいときに使い、短い質問には足さない。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [The Effects of Generative AI on Design Fixation and Divergent Thinking](https://arxiv.org/abs/2403.11164)：arXiv（Wadinambiarachchi, Samangi ほか）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)

**次に読む**

- [日本語の資料を読ませる・書かせる](../japanese/documents-in-japanese.md)

**関連**

- [長い資料を渡すとき](../context/handing-long-documents.md)
- [context rot と紛らわしい情報 › 中ほどの情報は使われにくいか（lost in the middle）](../basics/context-rot.md#lost-in-the-middle)
- XML タグで区切る（準備中）
- [引用や出典の確かめ方](../verify/checking-citations.md)
- [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)
- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](../judgment/think-before-asking.md)
- [「分からない」と言ってよいと伝える](allow-i-dont-know.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
