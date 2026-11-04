---
id: read-specs-yourself
title: 仕様を自分で読み、AI に誤読を指摘させる
nav_title: 仕様を自分で読む
aliases: [誤読の検出, 仕様の読み違いを防ぐ, 要件定義書を読む, 問題文を読む]
type: recipe
field: recipes
chapter: 読んで理解する
order: 20
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [握る, 確かめる]
prevents: [見えていない, 確かめていない]
pitfalls: [預けすぎる, みんなの案になる]
scenes: [開発, コンテスト]
summary: 与えられた仕様は原文を自分で読んで要約を書き、AI には原文と突き合わせて誤読や落とした条件を指摘させる。理解は、採点や検証の処理を書いて公式の値と照らして確かめる。
signs:
  - {type: goal, text: 要件定義書や API の仕様の読み違いを防ぎたい}
  - {type: symptom, text: AI に要約させた仕様で実装したら、仕様の条件を取り違えていた}
  - {type: situation, text: 長い問題文や規約を読んでから取りかかる}
prerequisites: [summary-overgeneralization, fact-checking]
related: [think-before-asking, spec-first, explore-a-codebase, research-and-reports, tests-first, handing-long-documents, ai-ideas-are-everyones, practice-vs-contest-day, documents-in-japanese, checking-citations]
sources: []
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guard}
  - {title: 先に自分で読んで要約する, anchor: read-first}
  - {title: AI に誤読を指摘させる, anchor: misreading-detector}
  - {title: 採点の処理で理解を確かめる, anchor: check-by-scoring}
  - {title: 全体の確かめ方, anchor: overall-check}
  - {title: うまくいかないとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：与えられた仕様を先に自分で読んで要約し、AI に原文と突き合わせて誤読を指摘させ、採点の処理で理解を確かめられる。
    - **いつ引くか**：要件定義書や API の仕様の読み違いを防ぎたいとき、AI に要約させた仕様で実装したら条件を取り違えていたとき、長い問題文や規約を読んでから取りかかるとき。
    - **前提**：<!-- link:begin summary-overgeneralization -->[要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)<!-- link:end -->、<!-- link:begin fact-checking -->[事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)<!-- link:end -->

<!-- textlint-disable -->
別名：誤読の検出・仕様の読み違いを防ぐ・要件定義書を読む・問題文を読む
<!-- textlint-enable -->

仕様を自分で読んで AI に誤読を指摘させるとは、要件定義書・API の仕様・規約・問題文といった与えられた仕様を、人が原文で読み、AI を要約役ではなく点検役として使う進め方である。このページは、その順序と、理解を確かめる終わり方を書く。仕様を作る側の話は <!-- link:begin spec-first -->[仕様を先に固める（spec・インタビュー・モック先行）](spec-first.md)<!-- link:end --> が持つ。

## 先に整える守り {#guard}

仕様を読む作業で起きやすい失敗は 4 つある。Claude 側の「見えていない」は、要約から何が落ちたかが、要約だけを見ても分からないことだ。「確かめていない」は、要約を原文と照らさずに実装へ進むことだ。人の側の「預けすぎる」は、読む作業そのものを AI に任せることだ。「みんなの案になる」は、全員が AI の要約を読んで済ませ、落ちた条件ごと同じ解釈に揃うことだ。

- **要約を根拠にしない**：AI の要約は、原文の条件や限定を落として、主張を原文より広く言いがちである。「正確に」と頼んでも直らないことがある。理由は <!-- link:begin summary-overgeneralization#why -->[要約は原文より強く言いがち（過度な一般化） › なぜ起きるか](../basics/summary-overgeneralization.md#why)<!-- link:end --> にある。
- **原文を同じ会話に入れる**：突き合わせるには、AI の手元に原文が要る。要約だけを渡すと、AI は要約の言い換えしかできない。
- **指摘には原文の引用を付けさせる**：引用のない指摘は、AI の推測と区別できない。手順は <!-- link:begin fact-checking#quotes -->[事実を確かめる（引用・照合・best-of-N） › 主張ごとに引用させる](../verify/fact-checking.md#quotes)<!-- link:end --> と <!-- link:begin fact-checking#summaries -->[事実を確かめる（引用・照合・best-of-N） › 要約を原文と照らす](../verify/fact-checking.md#summaries)<!-- link:end --> にある。
- **人が先に読む**：先に自分の理解を書いておくと、AI の指摘と比べられる。順序の理由：<!-- link:begin think-before-asking#self-first -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI](../judgment/think-before-asking.md#self-first)<!-- link:end -->。

## 先に自分で読んで要約する {#read-first}

頼む前に、原文を自分で読み、自分の言葉で要約と疑問点を書く。この要約は、あとで AI が原文と突き合わせる対象になる。

読む対象は、実装や提出の結果を左右するものを全部入れる。

- 業務の仕様：要件の範囲、API の入出力・エラー・制限・版、契約や規約の期限・例外・責任の範囲。
- 競技の問題：問題文、スコア式、入力の生成法、評価指標、テスターのコード、提出環境（時間制限・メモリ・オフラインか・言語と版）。

要約は、条件・単位・範囲・例外ごとに書く。読んで引っかかった所は、要約と別に疑問点として残す。曖昧な点は、原文から一通りに決まる「決定事項」と、運営や依頼主に聞くべき「質問すべき事項」に分ける。分け方は雛形の読んだ記録に置いた。

<!-- gen:begin snippet read-specs-yourself/reading-memo -->
<!-- textlint-disable -->

??? example "雛形：読んだ記録のひな形"

    ```markdown
    ## 読んだ記録：（仕様の名前・版・読んだ日）

    ### 条件の要約（自分の言葉）
    | # | 条件（単位・範囲・例外を含める） | 原文の場所 |
    |---|---|---|
    | 1 | | |

    ### 決定事項（原文から一通りに決まること）
    - 

    ### 質問すべき事項（原文では決まらないこと。決まるまで仮定を置かない）
    | # | 疑問 | 読み方 A のとき | 読み方 B のとき | 質問先 | 答え |
    |---|---|---|---|---|---|
    | 1 | | | | | |

    ### AI の指摘への対応
    | # | AI の指摘 | 原文を開いた結果 | 扱い（自分の誤読・AI の誤り・質問へ） |
    |---|---|---|---|
    | 1 | | | |
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet read-specs-yourself/reading-memo -->

先に自分で要約する順序は、発想の場面で先に自分の案を書く考え方を、読解に当てはめたものである（類推）。読解でこの順序の効果を比べた研究は、この辞典では確認していない。理解と確認のために原文を見せることは、順序と関係なく要る。

!!! example "判断例：AI に要約させて読むか、先に自分で読むか"
    - **状況**：取引先の API の仕様が長い。今日中に実装へ着手したい。
    - **迷う候補**：AI に要約させて全体を早くつかむ。または、先に自分で原文を読んで要約を書く。
    - **選んだもの**：先に自分で原文を読み、要約と疑問点を書く。AI には、原文と要約の突き合わせだけを頼む。
    - **理由**：AI の要約を最初に読むと、落ちた条件に気づく手がかりが自分の側に残らない。自分の要約があれば、AI の指摘が自分の読みとどこで違うかを比べられる。急ぐ場面でも、読む時間を削ると、実装の後で条件の取り違えに気づくほうが高くつく。

**終わりの確かめ**：要約の各条件に、原文の場所を付けられること。付けられない条件は、自分の推測か、どこかから写したものである。

## AI に誤読を指摘させる {#misreading-detector}

AI には、自分の要約と原文を突き合わせて、食い違いを指摘させる。解き方や実装は聞かない。聞くと、AI の解釈に引きずられて、自分の読みを点検する役が果たせなくなる。

原文の渡し方は、面で違う。

=== "アプリ"

    原文を会話に貼るか、ファイルとして添付する。長い資料は、分ける・Markdown に直すなどの準備を先にする（<!-- link:begin handing-long-documents#split-and-convert -->[長い資料を渡すとき › 分ける・形を直す](../context/handing-long-documents.md#split-and-convert)<!-- link:end -->）。日本語の PDF は、読めているかを先に確かめる（<!-- link:begin documents-in-japanese#pdf -->[日本語の資料を読ませる・書かせる › 日本語の PDF を渡す前と後に確かめること](../japanese/documents-in-japanese.md#pdf)<!-- link:end -->）。

=== "Claude Code"

    原文をテキストか Markdown にして作業ディレクトリに置き、ファイルのパスで指す。Claude Code は WSL・Linux の CLI を基準に書いている。ほかの OS と IDE 拡張の動作は未確認である。

依頼の型を雛形に置いた。要約の条件の抜けと、原文より強い言い方と、読み方が分かれる所の 3 つを挙げさせ、指摘ごとに原文の引用を求める。

<!-- gen:begin snippet read-specs-yourself/compare-summary -->
<!-- textlint-disable -->

??? example "雛形：自分の要約と原文を突き合わせさせる依頼"

    ```text
    下の「原文」と「私の要約」を突き合わせて、食い違いを指摘してください。解き方や実装は答えないでください。

    - 原文にあって、私の要約に書かれていない条件（但し書き・例外・単位・範囲・順序）を挙げる
    - 私の要約にあって、原文からは言えないこと、または原文より強く言っていることを挙げる
    - 原文が曖昧で、読み方が 2 通り以上ある所を挙げ、読み方ごとに結果がどう変わるかを書く
    - 指摘は 1 件ごとに、原文の該当の文を一字も変えずに引用して根拠にする。引用できない指摘は「推測」と書く
    - 食い違いがないと判断した項目は、ないと書く。無理に探さない

    ## 原文
    （ここに貼る。Claude Code ではファイルのパスを書く）

    ## 私の要約と疑問点
    （先に自分で書いた要約と、読んで引っかかった点）
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet read-specs-yourself/compare-summary -->

返ってきた指摘は、そのまま信じず、指摘ごとに原文を開いて確かめる。AI の指摘も、原文を読み違えていることがある。確かめた結果は、次の 3 つに分ける。

- 自分の誤読だった：要約を直す。
- AI の誤りだった：原文の該当の文を、指摘への反証として記録する。
- 原文では決まらない：質問すべき事項へ移す。答えが来るまで、仮定を置く場合は仮定と書く。

質問すべき事項が多いときは、実装の前に仕様を詰める手順に移る（<!-- link:begin spec-first#interview -->[仕様を先に固める（spec・インタビュー・モック先行） › インタビューで仕様を詰める](spec-first.md#interview)<!-- link:end -->）。

**終わりの確かめ**：AI の指摘がすべて、自分の誤読・AI の誤り・原文では決まらない、のどれかに分かれていること。未処理の指摘が残っていない。

## 採点の処理で理解を確かめる {#check-by-scoring}

読んで分かったつもりでも、理解が合っているかは別に確かめる。確かめ方は、仕様が定めている計算や判定だけを処理として書き、公式の値と小さな例で一致させることだ。

仕様ごとの例は、次のとおりである。

- 競技：スコア計算や評価指標の処理を書き、公式のツールの出力と小さな入力で一致させる。
- API：料金・件数・境界の判定など、仕様が規則を定めている計算を関数にし、仕様書に載っている応答例と一致させる。
- 契約や規約：期限や金額の計算規則を、具体的な日付と金額の例で手計算し、読み方ごとに結果を並べる。

処理は自分で書いても、AI に書かせてもよい。AI に書かせるときの依頼の型を雛形に置いた。公式の例をすべてテストにし、落ちたときは期待値を変えずに原因の文を報告させる。

<!-- gen:begin snippet read-specs-yourself/scoring-code -->
<!-- textlint-disable -->

??? example "雛形：採点の処理を書かせ、公式の値と一致させる依頼"

    ```text
    下の「原文」が定めている計算（採点・料金・判定など）を、関数として実装してください。関数以外の実装は不要です。

    - 原文の規則を、1 文ずつ関数の処理に対応づけて書く。対応づけられない文は、そのまま挙げる
    - 原文にない前提（丸め方・境界の扱い・単位）を補ったときは、補った箇所にコメントで「補足」と書く
    - 原文に載っている公式の例（入力と、そのときの正しい値）を、すべてテストとして書く
    - 公式の例にない小さな入力も 3 件ほど選び、正しい値を原文の規則から手計算した過程つきで書く
    - テストが通らないときは、テストの期待値を変えずに、どの文の読み違いが原因かを報告する

    ## 原文
    （ここに貼る。Claude Code ではファイルのパスを書く）

    ## 公式の例
    （原文にある入力と値。公式の計算ツールの出力でもよい）
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet read-specs-yourself/scoring-code -->

値が一致しないときは、まず原文に戻って読み直す。AI に頼んで値を合わせ込むと、公式の例だけに合って、ほかの入力で外れる実装になりやすい。テストを書き換えた差分は特に読む（<!-- link:begin tests-first#review-test-changes -->[テストを先に書かせる › テストの変更は特に読む](../verify/tests-first.md#review-test-changes)<!-- link:end -->）。テストを先に書かせる手順そのものは、<!-- link:begin tests-first#steps -->[テストを先に書かせる › 手順](../verify/tests-first.md#steps)<!-- link:end --> にある。

AI を禁じる大会では、本番で使えるものが決まっている。読んで採点する力は本番でも自分で要るので、練習では AI を点検役にし、本番の条件で自力を確かめる（<!-- link:begin practice-vs-contest-day#test-under-contest-conditions -->[練習と本番の使い分け（AI を禁じる大会に向けた練習を含む） › 本番の条件で自力を確かめる](../contest/practice-vs-contest-day.md#test-under-contest-conditions)<!-- link:end -->）。競技の問題文の読み方そのものは kyopro-atlas に任せ、このページは AI への渡し方と確かめ方に絞る。ここまでの順序は、競技の実践者の報告が中心で、条件をそろえて比べた研究ではない（根拠：弱）。

**終わりの確かめ**：公式の値と一致した例の件数と、一致しなかった例の原因が、読んだ記録に残っていること。

## 全体の確かめ方 {#overall-check}

実装や提出へ進む前に、次の 4 つを見る。

1. 要約の各条件に、原文の場所が付いている。
2. AI の指摘が、自分の誤読・AI の誤り・質問すべき事項に分かれ、未処理がない。
3. 仕様が定める計算は、公式の値や応答例と一致している。
4. AI なしで、仕様の要点と曖昧な点を自分の言葉で説明できる。

4 つ目に答えられないときは、要約を自分で書き直すところへ戻る。AI の指摘を読んだだけでは、理解したことにならない。

## うまくいかないとき {#when-it-fails}

- **「問題ない」ばかりの指摘だったのに、後から条件の取り違えが見つかった**：原文が長く、途中まで読まれていない可能性がある。原文を分けて渡し、引用を先に抜かせる（<!-- link:begin handing-long-documents#quotes-first -->[長い資料を渡すとき › 引用を先に抜かせる](../context/handing-long-documents.md#quotes-first)<!-- link:end -->）。
- **指摘に引用がなく、一般論ばかり**：引用のない指摘は「推測」と書かせる依頼に直す。引用が原文にあるかは、<!-- link:begin checking-citations#steps -->[引用や出典の確かめ方 › 確かめる手順](../verify/checking-citations.md#steps)<!-- link:end --> の手順で見る。
- **すでに AI の要約で読み進めてしまった**：要約を根拠にした箇所を、原文と照らし直す。落ちやすい条件の型は <!-- link:begin summary-overgeneralization#what-happens -->[要約は原文より強く言いがち（過度な一般化） › 何が起きるか](../basics/summary-overgeneralization.md#what-happens)<!-- link:end --> にある。
- **全員が同じ読みに揃う、差が要る場面**：AI の読みを「ほかの人も得ている読み」として扱い、自分の疑問点を足す（<!-- link:begin ai-ideas-are-everyones#when-difference-matters -->[AI の案は「みんなの案」（均質化） › 差が要る場面と、底上げで足りる場面](../judgment/ai-ideas-are-everyones.md#when-difference-matters)<!-- link:end -->）。
- **仕様がコードベースの中にある**：説明をコードで確かめる手順は <!-- link:begin explore-a-codebase#check-against-code -->[知らないコードベースを読む › 説明をコードで確かめる](explore-a-codebase.md#check-against-code)<!-- link:end --> にある。出典つきの調べものなら <!-- link:begin research-and-reports#check-sources -->[調べものとレポート › 出典を原文で確かめる](research-and-reports.md#check-sources)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)

**関連**

- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](../judgment/think-before-asking.md)
- [仕様を先に固める（spec・インタビュー・モック先行）](spec-first.md)
- [知らないコードベースを読む](explore-a-codebase.md)
- [調べものとレポート](research-and-reports.md)
- [テストを先に書かせる](../verify/tests-first.md)
- [長い資料を渡すとき](../context/handing-long-documents.md)
- [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)
- [練習と本番の使い分け（AI を禁じる大会に向けた練習を含む）](../contest/practice-vs-contest-day.md)
- [日本語の資料を読ませる・書かせる](../japanese/documents-in-japanese.md)
- [引用や出典の確かめ方](../verify/checking-citations.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
