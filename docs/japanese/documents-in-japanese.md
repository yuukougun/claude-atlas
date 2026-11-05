---
id: documents-in-japanese
title: 日本語の資料を読ませる・書かせる
aliases: [日本語の PDF を読ませる, 縦書きの資料, 敬語のメールを書かせる, 社内用語を使わせる]
type: recipe
field: japanese
chapter: 資料と環境
order: 90
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [見せる, 確かめる]
prevents: [見えていない]
scenes: [文章, 調べもの, チーム]
summary: 日本語の PDF や社内文書は、読めたかを引用で確かめてから使う。敬語や社内用語を使わせるときは、読み手・相手との関係・用語の一覧を添えて頼む。
signs:
  - {type: goal, text: 日本語の PDF（縦書きやスキャン）を読ませたい}
  - {type: goal, text: 取引先に送る敬語のメールを書かせたい}
  - {type: symptom, text: 社内の言い方と違う用語で書かれる}
prerequisites: [long-context-first]
related: [handing-long-documents, how-attachments-are-read, consistent-notation, consistent-politeness, skipped-later-pages, can-i-prompt-in-japanese, character-encodings, write-docs, research-and-reports]
sources: []
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guard}
  - {title: 日本語の PDF を渡す前と後に確かめること, anchor: pdf}
  - {title: 敬語は読み手と関係を渡す, anchor: keigo}
  - {title: 社内用語は一覧で渡す, anchor: glossary}
  - {title: 全体の確かめ方, anchor: verify}
  - {title: うまくいかないとき, anchor: failure}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：日本語の PDF は引用で読めたかを確かめてから使い、敬語と社内用語は読み手・関係・一覧を渡して書かせる。
    - **いつ引くか**：縦書きやスキャンの PDF を読ませたいとき、取引先向けの敬語のメールを頼むとき、社内の言い方と違う用語で書かれるとき。
    - **前提**：<!-- link:begin long-context-first -->[長い資料は先、質問は最後](../prompting/long-context-first.md)<!-- link:end -->

<!-- textlint-disable -->
別名：日本語の PDF を読ませる・縦書きの資料・敬語のメールを書かせる・社内用語を使わせる
<!-- textlint-enable -->

日本語の資料を読ませる・書かせる仕事は、読む側と書く側の 2 つに分かれる。読む側では、PDF が本当に読めたかを人が確かめる。書く側では、敬語の相手と社内の用語という、Claude の手元にない情報を依頼に添える。このページは、その手順と確かめ方をまとめる。

## 先に整える守り {#guard}

日本語の資料の仕事で最初に守るのは、「読めたはず」「通じたはず」で進めないことである。見えていない部分は、答えの質が悪いのではなく、答えの材料に入っていない。入っていないことは答えの見た目では分からないので、確かめる仕掛けを依頼に入れる。

- **原文を見せる**：PDF は要約させる前に、原文の引用を先に出させる。引用の仕組みは <!-- link:begin long-context-first#quote-first -->[長い資料は先、質問は最後 › 答えの前に引用を抜かせる](../prompting/long-context-first.md#quote-first)<!-- link:end --> にある。
- **渡す形を整える**：文字化けしやすいファイルや大きな資料は、読ませる前に形と量を整える。方法は <!-- link:begin handing-long-documents#split-and-convert -->[長い資料を渡すとき › 分ける・形を直す](../context/handing-long-documents.md#split-and-convert)<!-- link:end --> と <!-- link:begin character-encodings#check -->[文字コード（Shift\_JIS の CSV など） › 渡す前に文字コードを確かめる](character-encodings.md#check)<!-- link:end --> にある。
- **人が最後に読む**：敬語のメールは、送る前に人が全文を読む。相手との関係は、依頼に書かない限り Claude には見えない。
- **揺れは検査に任せる**：敬体と常体の混在や用語の揺れは、依頼の文面で防ぎきれない。検査の道具で見つける考え方は <!-- link:begin consistent-politeness#lint -->[です・ます／だ・であるを揃える › 混在を lint で見つける](consistent-politeness.md#lint)<!-- link:end --> と <!-- link:begin consistent-notation#guard -->[表記ゆれと漢字の開き › 先に整える守り：指示だけに頼らない](consistent-notation.md#guard)<!-- link:end --> にある。

## 日本語の PDF を渡す前と後に確かめること {#pdf}

日本語の PDF は、渡す前に形を見て、渡した後に引用で読めたかを確かめる。縦書きの資料やスキャンした PDF が実際にどう読まれるかは、この辞典では試していない。読めるはずと断定せず、手元の資料で毎回確かめる。

**渡す前に見るもの**

- 文字を選択してコピーできるか。コピーできなければ、画像だけの PDF の可能性が高い。
- 縦書きの箇所があるか。あるなら、後の確かめで縦書きの箇所を必ず引用させる。
- 表や図が答えに要るか。要るなら、図表まで読まれる範囲に収まっているかを <!-- link:begin how-attachments-are-read#pdf-and-others -->[添付ファイルはどこまで読まれるか › PDF とそれ以外の文書](../app/how-attachments-are-read.md#pdf-and-others)<!-- link:end --> で見る。
- 大きな資料か。大きいなら、分け方を <!-- link:begin how-attachments-are-read#splitting -->[添付ファイルはどこまで読まれるか › 大きな資料の分け方](../app/how-attachments-are-read.md#splitting)<!-- link:end --> で選ぶ。

**渡した後にさせること**

1. 要約や分析の前に、最初と最後のページ、縦書きの箇所から原文のまま引用させる。
2. 読めなかった箇所を、ページ番号付きで挙げさせる。
3. 引用を元の PDF と見比べる。文字が欠けている、読み順が入れ替わっている、数字が違うといった食い違いがあれば、読めていない。

この 3 つを 1 つの依頼にまとめた雛形を次に置く。

<!-- gen:begin snippet documents-in-japanese/pdf-read-check -->
<!-- textlint-disable -->

??? example "雛形：PDF が読めたかを先に確かめる依頼"

    ```markdown
    添付した PDF「（ファイル名）」を、要約する前に読めているかだけ確かめてください。

    1. 最初のページと最後のページから、それぞれ 3 行ずつ、原文のまま引用してください。縦書きの箇所があれば、その箇所からも 1 つ引用してください。
    2. 文字として読めなかった箇所、画像として見えているだけの箇所、読み順に自信のない箇所を、ページ番号付きで挙げてください。
    3. 表と図が何点あるかを数え、数えたページ番号を並べてください。

    読めたと判断できるまで、要約や分析は始めないでください。読めなかった箇所は、推測で埋めずに「読めない」と書いてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet documents-in-japanese/pdf-read-check -->

引用が原文と合っていても、後半のページが読まれたことまでは分からない。後半の取りこぼしは別に確かめる。切り分けは <!-- link:begin skipped-later-pages#diagnosis -->[添付した資料の後半を読んでいない › 原因を安く確かめる順](../symptoms/skipped-later-pages.md#diagnosis)<!-- link:end --> にある。

Claude Code で PDF を扱うときは、ファイルを読ませる前に、テキストへ変換して中身を目で確かめる手もある。変換の道具と手順はこの辞典では扱わない。変換した後のテキストにも、同じ引用の確かめを使う。

## 敬語は読み手と関係を渡す {#keigo}

敬語のメールを頼むときは、誰が誰に送るのかと、2 人の関係を依頼に書く。「敬語で書いて」だけでは、尊敬語で高める相手と、謙譲語で下げる自分の側の範囲が決まらない。

渡す情報は 4 つである。

- **宛先**：会社名・部署・役職。面識の有無。
- **送り手**：自分の立場。取引先に送るなら、社外に対して自社の人を高めない。
- **関係**：初めての連絡か、やり取りが続いているか。距離が近い相手に硬すぎる文を送ると、かえって不自然になる。
- **目的と事実**：お詫び・依頼・日程の調整といった目的と、伝える事実の箇条書き。事実を渡さないと、Claude の推測した内容が混じる。

次の判断例は、頼み方を決める場面である。

!!! example "判断例：敬語の段階を、指示するか、手本で見せるか"
    - **状況**：初めて連絡する取引先の担当者に、納期の遅れを詫びるメールを送る。
    - **迷う候補**：宛先と関係を書いて「尊敬語と謙譲語を使い分ける」と指示する。過去に送った似たメールを手本として貼る。
    - **選んだもの**：宛先と関係を書いて指示し、手本は社内で定めた書き出しと結びだけを貼る。
    - **理由**：過去のメールは、相手との関係が今回と違うことが多い。丸ごと貼ると、その関係の距離感まで写される。書き出しと結びだけなら、社内の決まりは守られ、本文の敬語の段階は今回の関係に合わせられる。

依頼の雛形を次に置く。迷った文を挙げさせる最後の行は、人が読むときの目印になる。

<!-- gen:begin snippet documents-in-japanese/keigo-request -->
<!-- textlint-disable -->

??? example "雛形：読み手と関係を渡して敬語のメールを頼む依頼"

    ```markdown
    取引先に送るメールの下書きを書いてください。

    - 宛先：（会社名・部署・役職・名前）。面識は（ある／ない）。
    - 送り手：私（自社の立場と役職）。宛先とは（初めての連絡／何度かやり取りがある／長い付き合いがある）。
    - 目的：（遅れのお詫び／日程の調整／見積もりの依頼 など）
    - 伝えること：（事実を箇条書きで）
    - 文体：丁寧語を基本に、宛先の動作には尊敬語、自社と自分の動作には謙譲語を使う。過剰な敬語にしない。
    - 長さ：本文は（200）字ほど。件名もつける。

    宛先の動作と自社の動作の区別に迷った文は、本文の後に「迷った文」として挙げてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet documents-in-japanese/keigo-request -->

敬語の使い分けは、Claude が正しく書けたと見なして送らない。宛先の名前・役職・社名の誤りは、敬語の誤りより重い。人が全文を読み、宛先の情報を名刺や連絡先の記録と照らす。

文体の揺れ（です・ます調と、だ・である調の混在）は、敬語とは別の問題である。文体の指定と lint の方法は、<!-- link:begin consistent-politeness#specify -->[です・ます／だ・であるを揃える › 文体は一行で、理由と一緒に指定する](consistent-politeness.md#specify)<!-- link:end --> にある。

## 社内用語は一覧で渡す {#glossary}

社内の言い方と違う用語で書かれるのは、Claude が社内の言い方を知らないからである。一般的な言い方で書くのが自然な動きであり、気を利かせても当たらない。使う言い方を一覧にして渡せば、見えていない原因が消える。

一覧には 3 つの欄を持たせる。

- **使わない言い方**：一般的な言い方や、組織の中で避けている言い方。
- **使う言い方**：社内の言い方。
- **意味・使う場面**：同じ語が場面で変わるときの条件。

一覧にない語を勝手に直させない指示も入れておく。直させると、社内では正しい語を一般的な言い方に戻されることがある。「一覧にない語」として後から挙げさせ、人が一覧に足すかを決める。

<!-- gen:begin snippet documents-in-japanese/internal-terms -->
<!-- textlint-disable -->

??? example "雛形：社内用語の一覧を添えて文書を頼む依頼"

    ```markdown
    以下の「社内用語の一覧」を正として、文書を書いてください。

    - 左の欄の言い方は使わず、右の欄の言い方に直す。
    - 一覧にある語は、そのまま使う。言い換えや略しなおしをしない。
    - 一覧にない社内の言い方が文書に出てきたら、勝手に直さず、書いた後に「一覧にない語」として挙げる。

    | 使わない言い方 | 社内の言い方 | 意味・使う場面 |
    | --- | --- | --- |
    | 顧客 | お客様 | 外部向けの文書では必ずこれにする |
    | 申請書 | 稟議書 | 金額の決裁を求める文書 |
    | 会議 | 定例 | 毎週の定例の会議だけ。臨時の会議は「打ち合わせ」 |
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet documents-in-japanese/internal-terms -->

一覧は、依頼の本文に毎回貼るか、毎回読まれる場所に置く。置き場所の選び方は、<!-- link:begin consistent-politeness#where -->[です・ます／だ・であるを揃える › 置き場所（アプリの指示・スキル・CLAUDE.md・出力スタイル）](consistent-politeness.md#where)<!-- link:end --> と同じ考え方である。一覧を人が持つ正本から作り、指示と検査の両方に使う方法は <!-- link:begin consistent-notation#single-source -->[表記ゆれと漢字の開き › 一覧を指示と lint の両方に使う](consistent-notation.md#single-source)<!-- link:end --> にある。表記の一覧と社内用語の一覧は、同じ一覧にまとめてよい。

一覧が長いと、依頼の本文が一覧に押される。長い資料の置き方は <!-- link:begin long-context-first#order -->[長い資料は先、質問は最後 › 資料を先、質問を最後に置く](../prompting/long-context-first.md#order)<!-- link:end --> に従い、一覧を先、依頼を最後に置く。

## 全体の確かめ方 {#verify}

3 つの仕事は、確かめ方が違う。どれも、Claude に「できたか」と聞くのではなく、外から見て確かめる。

| 仕事 | 確かめるもの | 確かめ方 |
| --- | --- | --- |
| PDF を読ませる | 読めたか | 原文の引用を元の PDF と見比べる |
| 敬語で書かせる | 関係に合った段階か | 人が全文を読み、迷った文の挙げ方を見る |
| 社内用語で書かせる | 一覧どおりか | 使わない言い方を検索し、一覧にない語の報告を見る |

使わない言い方の検索は、手で行うほか、表記の検査の道具に登録して自動化できる。登録の方法は <!-- link:begin consistent-notation#verify -->[表記ゆれと漢字の開き › 確かめ方](consistent-notation.md#verify)<!-- link:end --> にある。文書を書かせる仕事の全般は <!-- link:begin write-docs -->[ドキュメント・技術文書を書く](../recipes/write-docs.md)<!-- link:end -->、調べた内容を報告にまとめる仕事は <!-- link:begin research-and-reports -->[調べものとレポート](../recipes/research-and-reports.md)<!-- link:end --> を見る。

## うまくいかないとき {#failure}

うまくいかない形ごとに、先に切り分けるものと、行き先を挙げる。

- **PDF の後半が答えに出ない**：読み込みの範囲か、注意の偏りかを切り分ける。<!-- link:begin skipped-later-pages -->[添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)<!-- link:end --> へ進む。
- **引用が出ない、または原文と合わない**：画像だけの PDF や、読み順の崩れが疑われる。ページの画像を見せて確かめるか、テキストに変換してから渡す。変換した後も同じ引用の確かめを使う。
- **文字化けや空欄が出る**：ファイルの文字コードが合っていない可能性がある。<!-- link:begin character-encodings -->[文字コード（Shift\_JIS の CSV など）](character-encodings.md)<!-- link:end --> を見る。
- **敬語の段階が合わない**：宛先と関係の書き方が足りない。判断例の理由を見て、書き出しと結びの手本を足す。
- **社内用語が守られない**：一覧を毎回読まれる場所に置いたかを見る。長い会話の途中なら、一覧を依頼の最後にもう一度付ける。
- **日本語で頼むこと自体が不安**：<!-- link:begin can-i-prompt-in-japanese -->[日本語で指示して大丈夫か](can-i-prompt-in-japanese.md)<!-- link:end --> を見る。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [長い資料は先、質問は最後](../prompting/long-context-first.md)

**関連**

- [長い資料を渡すとき](../context/handing-long-documents.md)
- [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- [表記ゆれと漢字の開き](consistent-notation.md)
- [です・ます／だ・であるを揃える](consistent-politeness.md)
- [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)
- [日本語で指示して大丈夫か](can-i-prompt-in-japanese.md)
- [文字コード（Shift\_JIS の CSV など）](character-encodings.md)
- [ドキュメント・技術文書を書く](../recipes/write-docs.md)
- [調べものとレポート](../recipes/research-and-reports.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
