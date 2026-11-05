---
id: artifacts-overview
title: アーティファクト（会話の中で作る文書・スライド・デザイン）
nav_title: アーティファクト
aliases: [Artifacts, Docs, Slides, Design, Dashboards]
type: feature
field: app
chapter: 調べる・作る
order: 110
level: 整える
priority: 必須
surfaces: [app]
principle: [確かめる]
prevents: [確かめていない]
scenes: [文章, 開発]
summary: 会話の中で文書・スライド・デザインなどを作り、直し、共有できる。テンプレートの選び方と、公開するときの注意が分かる。
signs:
  - {type: goal, text: 会話の中で文書やスライドを作って直したい}
  - {type: goal, text: 画面のモックや試作をすぐ見たい}
  - {type: goal, text: 作ったものを人に見せられる形で渡したい}
prerequisites: []
related: [artifacts-as-apps, files-and-code-execution, shared-artifacts-and-files, make-slides, write-docs, looks-are-not-quality, rewind-dont-correct, peripheral-products]
tracks: [artifacts, code-execution]
sources: [hc-artifacts, hc-cowork-and-chat, hc-release-notes, hc-files, claude-pricing, anthropic-news-design-anthropic-labs]
volatility: 高
sections:
  - {title: 使いどころ, anchor: when}
  - {title: テンプレートの選び方, anchor: templates}
  - {title: 直し方（頼む・直接直す・範囲を選ぶ）, anchor: editing}
  - {title: 公開と共有, anchor: sharing}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: Claude Design（周辺製品）との違い, anchor: claude-design}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：会話の横に文書・スライド・デザインなどを作り、直し、共有できる。用途でテンプレートを選ぶ。
    - **いつ引くか**：会話の中で文書やスライドを作って直したいとき、画面のモックや試作をすぐ見たいとき、作ったものを人に見せられる形で渡したいとき。
    - **強制力**：<!-- gen:begin feature artifacts/enforcement -->なし<!-- gen:end feature artifacts/enforcement -->。作る・直す・共有するための機能で、何も止めない。
    - **前提**：なし

<!-- textlint-disable -->
別名：Artifacts・Docs・Slides・Design・Dashboards
<!-- textlint-enable -->

アーティファクトは、Claude が人へ見せる目的で作るものを、会話の横に開いて扱う機能である。開いたまま直し、後から開き直し、共有できる。見た目が整って出るので、中身を確かめずに渡す失敗が起きやすい。このページは、テンプレートの選び方と直し方、渡し方、確かめる習慣を扱う。

## 使いどころ {#when}

アーティファクトが作られるのは、分量があり、単体で完結し、後で使い回されそうな内容のときである。短い答えは、ふつうの返答のままになる。

使いどころは次の 3 つである。

- 文書やスライドを会話の中で下書きし、同じ画面で直したい。
- 画面のモックや試作を、コードを動かす前に目で見たい。
- 作ったものを、会話のログのままにせず、人へ渡せる形にしたい。

防ぐ原因は「確かめていない」である。アーティファクトは整った見た目で出るため、書かれた数字や主張を読み手が確かめたように見えてしまう。見た目と中身の関係は <!-- link:begin looks-are-not-quality -->[見た目は品質の証拠ではない](../verify/looks-are-not-quality.md)<!-- link:end --> が扱う。対策は、渡す前に自分で中身を確かめることで、手順は直し方と公開と共有の節に書く。

最初に整えておく設定もある。アーティファクトは、アプリの設定でファイル作成とコード実行を有効にしておく必要がある。設定の名前と画面は変わりやすいので、現在の名前は公式の記事で確かめる。この設定が持つ危険と範囲は <!-- link:begin files-and-code-execution#network -->[ファイル作成とコード実行 › 実行環境とネットワークの設定](files-and-code-execution.md#network)<!-- link:end --> にある。以前の形で作ったものは legacy artifacts として動き続けるが、新しくは作れない。

## テンプレートの選び方 {#templates}

テンプレートは、何を渡すかで選ぶ。迷ったら、渡す相手が最終的に何を開くかを考える。

| 渡すもの | テンプレート | 書き出し先（公式の記事、確認日 2026-10-29） |
| --- | --- | --- |
| 文章（報告・仕様・議事録） | Docs | Word・PDF・Markdown・Google Docs |
| 発表資料 | Slides | PowerPoint・PDF・Google Slides |
| 画面のモック・試作・ランディングページ | Design | zip・PDF・PPTX・HTML |
| 数字を見せる画面 | Dashboards | 各チャートにクエリと最終更新時刻が出る |
| 動画 | Motion | MP4 |

Docs は、チームで同時に編集できる。Dashboards と Motion は、成熟度と使えるプランが Docs・Slides・Design と別に定められている。プランごとの可否と成熟度は変わりやすいので、本文には書かず、公式の記事と料金のページで確かめる。公式の記事は、スプレッドシート型のテンプレートを挙げていない。表計算が要るときは、ファイル作成で xlsx を作らせるか、Dashboards を使う。ファイルの受け取り方は <!-- link:begin files-and-code-execution#outputs -->[ファイル作成とコード実行 › 作ったファイルの受け取り方](files-and-code-execution.md#outputs)<!-- link:end --> にある。

アーティファクトの中から Claude を呼ぶ、接続したアプリを読み書きする、データを残す、という使い方は別の機能として扱う。繰り返し使う小さな道具にしたいときは <!-- link:begin artifacts-as-apps#runtime -->[アーティファクトを小さなアプリにする › Claude を呼ぶ・アプリにつなぐ・データを残す](artifacts-as-apps.md#runtime)<!-- link:end --> へ進む。

最初の頼み方は、種類、目的、読み手、分量、資料の範囲を書く形が確実である。次の雛形は、資料にない数字を空欄にさせ、推測した箇所を会話の側に報告させる。

<!-- gen:begin snippet artifacts-overview/create-request -->
<!-- textlint-disable -->

???+ example "雛形：目的と読み手を決めてアーティファクトを作らせる依頼の雛形"

    ```text
    次の条件で、アーティファクトとして「＜文書・スライド・画面のモックのどれか＞」を作ってください。

    - 目的：＜何のために使うか。例：金曜の定例で、リリース延期の判断を仰ぐ＞
    - 読み手：＜誰が見るか。例：前提知識のない他部署の管理職＞
    - 分量：＜例：スライド 5 枚、または文書 1 ページ＞
    - 入れる内容：＜貼った資料の範囲、または箇条書き＞

    作るときの決まり：
    - 数字・日付・固有名詞は、私が渡した資料にあるものだけを使ってください。資料にないものは、空欄にして「要確認」と書いてください。
    - 最後に、あなたが推測で補った箇所の一覧を、アーティファクトの外（会話の返答）に書いてください。

    理由：作ったものをそのまま人に見せるので、見た目が整っていても、出どころの分からない数字が混ざると困ります。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet artifacts-overview/create-request -->

!!! example "判断例：打ち合わせで見せる画面案のテンプレート"
    - **状況**：新機能の画面案を、今日の打ち合わせで見せたい。文章の説明も数行ほど付けたい。
    - **迷う候補**：Docs に画面の説明を文章で書く。Design で、見て触れるモックを作る。
    - **選んだもの**：Design で作り、説明の数行はモックの中に置く。
    - **理由**：画面案の良し悪しは、文章よりも見て触って判断するほうが早い。打ち合わせの議論も、文章の解釈ではなくモックの修正に集まる。文章中心の仕様書が必要になったら、そのとき Docs に作り直す。

資料やスライドを作る手順は、<!-- link:begin make-slides -->[資料・スライドを作る](../recipes/make-slides.md)<!-- link:end --> と <!-- link:begin write-docs -->[ドキュメント・技術文書を書く](../recipes/write-docs.md)<!-- link:end --> にある。

## 直し方（頼む・直接直す・範囲を選ぶ） {#editing}

直し方は 3 つある。

- **頼む**：会話で、直したい点を伝える。
- **直接直す**：アーティファクトの本文を、自分の手で書き換える。
- **範囲を選ぶ**：Docs や Markdown では、範囲を選び、その範囲だけを Claude に直させる。

3 つの使い分けは、直す量で決める。語句の修正は直接直すほうが早い。節をまるごと書き直すなら、頼む。1 つの段落だけ言い回しを変えたいなら、範囲を選ぶ。範囲を選ぶと直す対象が限られるため、ほかの部分は変わりにくい。

会話で頼むときも、直す範囲を言葉で限ると同じ効果がある。次の雛形は、指定した部分の外を変えさせず、変えた箇所を一覧で返させる。

<!-- gen:begin snippet artifacts-overview/scoped-edit-request -->
<!-- textlint-disable -->

??? example "雛形：直す範囲を限って直させる依頼の雛形"

    ```text
    アーティファクトの「＜直したい節・スライド・要素の名前＞」だけを直してください。

    直す内容：＜例：結論を 1 文にまとめ、理由を 3 つの箇条書きにする＞

    守ること：
    - 指定した部分の外は、1 文字も変えないでください。
    - 直したあとに、変えた箇所を一覧にして返答に書いてください。変えていない部分を変えていないと確かめた旨も 1 行で書いてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet artifacts-overview/scoped-edit-request -->

過去のメッセージを編集して送り直すと、会話が別のブランチになり、元のアーティファクトは残る。これは、違う方向を試したいときに使える。訂正を重ねるよりも、前のメッセージを直して送り直すほうが良い理由は <!-- link:begin rewind-dont-correct#why -->[違うと返すより、巻き戻す・編集する › なぜ訂正より巻き戻しか](../context/rewind-dont-correct.md#why)<!-- link:end --> にあり、面ごとの戻し方は <!-- link:begin rewind-dont-correct#how -->[違うと返すより、巻き戻す・編集する › 面ごとの戻し方](../context/rewind-dont-correct.md#how)<!-- link:end --> にある。

アーティファクトの表示に不具合が出たときは、「Try fixing with Claude」のボタンで直せることがある。ただし、直る保証はない。直らないときは、同じボタンを繰り返さず、不具合の内容を言葉で伝えるか、前のメッセージに戻って頼み直す。

直した後は、読み手の立場で全文を読み直す。数字、日付、固有名詞、リンクを、元の資料と 1 つずつ照らす。直す前の版と見比べることで、頼んでいない部分が変わっていないかも確かめられる。

## 公開と共有 {#sharing}

アーティファクトは、作った直後は本人だけが見られる。共有するかどうかは、自分で決める。

共有の方法と見られる人、取り消せるものと取り消せないものは、持ち主のページが扱う。このページでは、渡す前に決めることだけを書く。

- **共有のしかた**：特定の人への招待、公開リンク、組織の中だけの共有がある。違いは <!-- link:begin shared-artifacts-and-files#how-to-share -->[共有リンクと公開アーティファクトの扱い › 共有のしかた（特定の人への招待・公開リンク・組織の中だけの共有）](../safety/shared-artifacts-and-files.md#how-to-share)<!-- link:end --> にある。
- **渡るもの**：共有で渡るのは、その時点の写しである。更新のしかたは <!-- link:begin shared-artifacts-and-files#snapshot -->[共有リンクと公開アーティファクトの扱い › 共有されるもの（その時点の写しと、更新のしかた）](../safety/shared-artifacts-and-files.md#snapshot)<!-- link:end --> にある。
- **見られる人**：プランによって違う。<!-- link:begin shared-artifacts-and-files#who-can-see -->[共有リンクと公開アーティファクトの扱い › 見られる人と、プランによる違い](../safety/shared-artifacts-and-files.md#who-can-see)<!-- link:end --> で確かめる。
- **取り消し**：取り消して消えるものと、消えないものがある。共有する前に <!-- link:begin shared-artifacts-and-files#revoke -->[共有リンクと公開アーティファクトの扱い › 取り消せるもの・取り消せないもの](../safety/shared-artifacts-and-files.md#revoke)<!-- link:end --> を読む。

渡す前の順序は、自分で中身を確かめてから、いちばん狭い範囲で共有する、である。公開した後で誤りに気づいても、すでに見られたものは取り消せないことがある。

他人が公開したアーティファクトを開くときは、知らない送り主から届いたファイルと同じに扱う。公式がこの注意を出している。開く前の確かめ方は <!-- link:begin shared-artifacts-and-files#opening-others -->[共有リンクと公開アーティファクトの扱い › 他人が公開したものを開くとき](../safety/shared-artifacts-and-files.md#opening-others)<!-- link:end --> にある。

アーティファクトに Claude の呼び出しやアプリの接続を持たせると、共有したときに誰の権限と枠で動くかが問題になる。公式の記事は、閲覧者が自分のアプリを接続し、利用分も各ユーザーのプランから引かれる、と説明している。詳しくは <!-- link:begin artifacts-as-apps#whose-account -->[アーティファクトを小さなアプリにする › 共有したときに誰の権限と枠で動くか](artifacts-as-apps.md#whose-account)<!-- link:end --> にある。

!!! example "判断例：試作を社外の人に見せる"
    - **状況**：作ったデモの画面を、社外の取引先に見せたい。
    - **迷う候補**：公開リンクを作って送る。特定の人だけを招待する。
    - **選んだもの**：先に自分で全文を確かめ、特定の人への招待で渡す。
    - **理由**：公開リンクは、リンクを知った人なら誰でも開ける形になる。見せたい相手が決まっているなら、狭い形で十分である。誤りに気づいたときも、影響を受ける人が少なくて済む。

## 効かない場面・落とし穴 {#pitfalls}

- **整った見た目を、確かめた印と読む**：スライドや文書は、中身が誤っていても整って出る。数字と主張は、元の資料で自分が照らす。見た目が品質の証拠でなくなった理由は <!-- link:begin looks-are-not-quality -->[見た目は品質の証拠ではない](../verify/looks-are-not-quality.md)<!-- link:end --> にある。
- **短い答えがアーティファクトにならない**：分量が少ない内容は、返答のままになる。アーティファクトにしたいときは、種類を名指しして頼む。
- **新しい設定が前提になる**：ファイル作成とコード実行の設定をオフにしていると、作れないことがある。設定の画面は変わりやすい。
- **昔のものは legacy**：<!-- fact:begin artifacts-rebuilt-date -->2026-09-16 から今の形になった。それより前に作ったものは legacy artifacts で、動き続けるが新しくは作れない（2026-10-29 時点）<!-- fact:end -->。作り直したいときは、新しい形でもう一度頼む。
- **テンプレートごとに状況が違う**：公式の記事と料金のページとリリースノートで、成熟度の書き方の食い違う項目がある。使う前に、自分のプランで選べるかを画面で確かめる。

## Claude Design（周辺製品）との違い {#claude-design}

名前の似たものが 2 つある。1 つ目は、アーティファクトのテンプレートである Design で、本体のアプリの会話の中で使う。2 つ目は、Anthropic Labs が出している Claude Design という別の製品である。

- **会話の中の Design**：アーティファクトの一種として、会話の横にモックや試作を作る。このページが扱う。
- **Claude Design**：デザイン、プロトタイプ、スライドなどを作る別の製品で、コードベースやデザインファイルからデザインシステムを作ったり、Claude Code へ引き渡したりできる、と発表されている。位置づけと確認日つきの一覧は <!-- link:begin peripheral-products#list -->周辺製品の一覧<!-- link:end --> にある。

読者がふつうに触れるのは、会話の中のほうである。Claude Design の操作の手順は、このページでは扱わない。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)：Anthropic・英語・確認日 2026-11-04
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)：Anthropic・英語・確認日 2026-11-04
- [Plans & pricing](https://claude.com/pricing)：Anthropic・英語・確認日 2026-11-04
- [Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/claude-design-anthropic-labs)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [アーティファクトを小さなアプリにする](artifacts-as-apps.md)
- [共有リンクと公開アーティファクトの扱い](../safety/shared-artifacts-and-files.md)
- [資料・スライドを作る](../recipes/make-slides.md)

**関連**

- [ファイル作成とコード実行](files-and-code-execution.md)
- [ドキュメント・技術文書を書く](../recipes/write-docs.md)
- [見た目は品質の証拠ではない](../verify/looks-are-not-quality.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
