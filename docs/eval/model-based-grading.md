---
id: model-based-grading
title: Claude に採点させる（人の判定で較正する）
aliases: [LLM as a judge, モデルによる採点, model-based grader, AI の採点の較正]
type: recipe
field: eval
chapter: 検証器を作る
order: 90
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, api, app]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [文章, 開発]
summary: 機械で判定しにくい出力を Claude に採点させるとき、人の判定と比べて採点の基準を較正できる。較正していない AI の採点は、合否の根拠にしない。
signs:
  - {type: goal, text: 文章の質のような、機械で判定しにくいものを Claude に採点させたい}
  - {type: symptom, text: AI の採点は高いのに、読んでみると良くない}
prerequisites: [verifier-three-conditions, measure-changes]
related: [misses-broken-evaluation, test-the-verifier, agreement-is-not-evidence, ask-without-sycophancy, sycophancy, independent-review, instructing-reviewers, goal-until-done, textlint-hook]
tracks: []
outdated_advice: []
sources: [anthropic-eng-demystifying-evals-ai-agents, anthropic-eng-harness-design-long-running]
volatility: 中
sections:
  - {title: コードで判定できるものはコードで, anchor: prefer-code}
  - {title: 採点の依頼を書く, anchor: write-grader}
  - {title: 人の判定と比べて較正する, anchor: calibrate}
  - {title: 判定役が見ているもの, anchor: what-the-judge-sees}
  - {title: 使い続けるときの確かめ方, anchor: keep-checking}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：機械で判定しにくい出力を、人の判定と突き合わせて較正した Claude の採点で、合否の材料にできる。
    - **いつ引くか**：文章の質のように機械で判定しにくいものを Claude に採点させたいとき。AI の採点は高いのに、読んでみると良くないとき。
    - **前提**：<!-- link:begin verifier-three-conditions -->[検証器の三条件（正しい・書き換えられない・本番を代表する）](verifier-three-conditions.md)<!-- link:end -->・<!-- link:begin measure-changes -->[変更が効いたかを測る（小さな eval）](measure-changes.md)<!-- link:end -->

<!-- textlint-disable -->
別名：LLM as a judge・モデルによる採点・model-based grader・AI の採点の較正
<!-- textlint-enable -->

Claude に採点させるとは、出力の良し悪しを Claude に点として返させ、その点を評価の仕組みの合否や比較に使うことである。点を付ける側の Claude を、このページでは採点役と呼ぶ。採点役の点を人の点に近づけるために採点の依頼を直す作業を、較正と呼ぶ。このページは、その採点を使ってよい状態にするまでの手順を扱う。核は 2 つある。コードで判定できるものはコードに任せること。残りは、人が付けた点と比べて採点の基準を直し続けることである。

## コードで判定できるものはコードで {#prefer-code}

採点の手段は、コード・モデル・人の 3 種類に分かれる。公式の評価の記事は、この 3 種類を次のように整理している。コードによる採点は、速く安く再現できるが、融通が利かない。モデルによる採点は、柔軟だが非決定的で、人間との較正が必要になる。人間による採点は、最も信頼できるが、高く遅い（[Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)）。使い分けの全体は <!-- link:begin measure-changes#graders -->[変更が効いたかを測る（小さな eval） › 採点の種類（コード・モデル・人）](measure-changes.md#graders)<!-- link:end --> にある。

この整理から、採点の順番が決まる。

- テストが通るか、形式が合っているか、必須の項目があるか、禁止の語が出ていないか。これらはコードで決められるので、コードで採点する。機械で見つけられる表記の揺れも、決まった規則の検査に任せる（<!-- link:begin textlint-hook -->[textlint をフックで回す](../japanese/textlint-hook.md)<!-- link:end -->）。
- 「読みやすいか」「論旨が通っているか」のように、基準を言葉にできても機械では数えにくいものだけを、Claude の採点に回す。
- 採点役の判断が最後まで当てにならないものは、人が読む。

モデルによる採点は、コードの採点を置き換えるものではなく、コードの採点が届かない部分を足すものである。コードで決まる部分まで AI に採点させると、同じ入力で点が揺れ、原因の切り分けもしにくくなる。

AI の採点を評価の仕組みに入れる前に、その仕組みが <!-- link:begin verifier-three-conditions#tamper-proof -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 書き換えられない](verifier-three-conditions.md#tamper-proof)<!-- link:end --> を満たすかを点検する。採点される側のエージェントが採点の依頼や較正用の例を書き換えられるなら、点は意味を失う。採点の依頼と人の点付きの例は、エージェントの手が届かない場所に置く。

## 採点の依頼を書く {#write-grader}

採点の依頼は、基準・点の付け方・例・判定不能の扱いを、依頼の本文に書く。素の Claude に「この文章を採点して」とだけ頼むと、基準が回ごとに変わり、点が高めに寄りやすい。エージェントは凡庸な出来でも自分の作業を自信満々に褒める。素の Claude を QA 役にすると、問題を見つけても、承認するよう自分を説得してしまう。次の記事に、この報告がある（[Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)。根拠：中。ハーネス設計者の報告で、特定のモデルの傾向として一般化しない）。この傾向の背景は <!-- link:begin sycophancy -->[迎合（sycophancy）](../basics/sycophancy.md)<!-- link:end --> にある。

依頼に入れるものは次のとおりである。

- **基準は観察できる言葉で書く**。「良い文章」ではなく、「結論が最初の 2 文に出ている」「主張ごとに根拠が付いている」のように、成果物を見て確かめられる形にする。
- **基準ごとに別々に採点させる**。総合点を 1 つ出させると、どの基準で点が動いたかが分からない。
- **点の段階を書く**。各段階の状態を基準ごとに書き、中間の点が何を意味するかを決めておく。
- **人が採点した例を入れる**。点の理由が付いた例を入れると、基準の読み方が揃う。ただし、依頼に入れた例は、後で一致を測る例に使わない。
- **点が下がる箇所を先に探させる**。良い点を並べさせる前に、各基準で点が下がる箇所を成果物から引かせる。見つからなかったときだけ満点にさせる。
- **決められないときは「判定不能」と書かせる**。基準で決められない成果物に無理に点を付けさせると、作り話の根拠が出る。

次の雛形は、この 6 点を入れた採点の依頼である。波かっこの部分を、自分の基準と例に置き換える。

<!-- gen:begin snippet model-based-grading/grader-prompt -->
<!-- textlint-disable -->

??? example "雛形：採点の基準を書いた採点の依頼の雛形"

    ```markdown
    あなたは採点役だ。次の成果物を、下の基準だけで採点する。成果物を書き直したり、改善案を出したりしない。

    # 採点の対象
    {ここに成果物を貼る。何を頼まれて書かれたものかも 1 行添える}

    # 基準（各項目を 0 点・1 点・2 点で採点する）
    1. {基準 1 の名前}：{2 点の状態を、観察できる言葉で書く}／{1 点の状態}／{0 点の状態}
    2. {基準 2 の名前}：{同じ形で書く}
    3. {基準 3 の名前}：{同じ形で書く}

    # 基準の例（人が先に採点した成果物）
    - 例 A（{基準 1} が 2 点、{基準 2} が 0 点）：{成果物の抜粋}。理由：{人が付けた理由}
    - 例 B（{基準 1} が 0 点、{基準 2} が 2 点）：{成果物の抜粋}。理由：{人が付けた理由}

    # 守ること
    - 基準にない好みで点を動かさない。基準で決められないときは「判定不能」とし、何が分かれば決められるかを書く。
    - 良い点を並べる前に、各基準で点が下がる箇所を成果物から引いて探す。見つからなかったときだけ満点にする。
    - 出力は次の形だけにする。
      - 基準ごとに：点、根拠として成果物から引いた 1〜2 行
      - 最後に：判定不能にした項目とその理由
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet model-based-grading/grader-prompt -->

## 人の判定と比べて較正する {#calibrate}

較正とは、採点役の点を人の点に近づけるために、採点の依頼を直す作業である。人の点が正しいと決まっているのではなく、人が握る基準に採点役を合わせるのである。小さな eval の考え方（<!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](measure-changes.md#small-eval)<!-- link:end -->）と同じく、実際に出た失敗から集めた少数の例で足りる。

1. **人が先に採点した例を集める**。実際に出た、良い出力と悪い出力と、判断が割れそうな出力を混ぜる。人は、採点役の点を見る前に、基準にそって点と理由を付ける。AI の点を見てから付けると、人の点が AI の点に引きずられる（<!-- link:begin ask-without-sycophancy#hide-preferences -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 好みと確信を伏せる](../judgment/ask-without-sycophancy.md#hide-preferences)<!-- link:end -->）。終わりの確認：例ごとに、人の点と理由が表に残っている。
2. **例を 2 つに分ける**。片方は採点の依頼に入れる例、もう片方は一致を測る例にする。後者は依頼に入れず、人が持つ。採点役とエージェントには中身を見せない。（推論・実践例なし）終わりの確認：測るための例が、依頼のどこにも出てこない。
3. **新しいセッションで採点させる**。成果物と基準だけを見せ、書いた側の説明や推論は見せない（見せるものは次の節）。同じ例を何度か採点させ、点が揺れるかも見る（<!-- link:begin measure-changes#how-many-runs -->[変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ](measure-changes.md#how-many-runs)<!-- link:end -->）。終わりの確認：例ごとに、採点役の点が複数回分ある。
4. **食い違いを表にして読む**。点の差がある行について、成果物と人の理由と採点役の根拠を読み、原因を分ける。主な原因は 4 つある。基準があいまいで別の意味に読まれた。基準にない好み（長さや語調）で点が動いた。人の点のほうが誤りだった。成果物だけでは決められなかった。終わりの確認：食い違いの行ごとに原因が 1 つ付いている。
5. **採点の依頼を直して、もう一度測る**。原因が基準のあいまいさなら基準の文を直し、好みで動いているなら「基準にない好みで点を動かさない」を足し、決められないものは判定不能の条件を足す。人の点が誤りだったときだけ、人が確かめて人の点を直す。採点役に合わせて人の点を直さない。終わりの確認：直した後の依頼で、測るための例の食い違いが減ったかを同じ表で比べている。

前の節で挙げたハーネス設計の記事には、設計者が評価役のログを読み、自分の判断とずれた箇所を見つけ、QA のプロンプトを数回改訂した、という記述がある（根拠：中）。食い違いを読んで依頼を直す、4 と 5 の流れと同じ形である。

食い違いを読むための依頼の雛形を、下に置く。人の点と採点の依頼は書き換えさせず、直す案だけを出させる。

<!-- gen:begin snippet model-based-grading/review-disagreements -->
<!-- textlint-disable -->

??? example "雛形：人の判定と食い違った例を読み直させる依頼の雛形"

    ```markdown
    採点役の点と人の点が食い違った例を読み直して、採点の依頼を直す案を出してほしい。採点の依頼そのものは、案が承認されるまで書き換えない。

    - 材料：`eval/calibration/pairs.md`（成果物の ID、人の点、採点役の点、人が付けた理由の表）。食い違いは、点の差が 1 以上の行とする。
    - 読み方：食い違いの行ごとに、成果物と人の理由と採点役の根拠を読み、原因を次の 4 つから選ぶ。
      1. 基準の書き方があいまいで、採点役が別の意味に読んだ
      2. 基準にない好み（長さ・語調など）で採点役の点が動いた
      3. 人の点のほうが誤りだった（人の理由が基準に合わない）
      4. 成果物だけでは決められない（判定不能にすべきだった）
    - 出す案：原因 1・2 については、採点の依頼のどの行をどう直すか、直す前後の文を並べる。原因 3 は人に確認する質問として出す。原因 4 は「判定不能」の条件の書き足しとして出す。
    - 変えないもの：`eval/calibration/pairs.md` の人の点。人の点を採点役に合わせて直さない。
    - 最後の報告：食い違いの数、原因ごとの件数、直す案を採点の依頼に当てたときに一致が増えると見込む行の ID を表にする。見込みは推測と明記する。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet model-based-grading/review-disagreements -->

人が握るものは、基準そのもの、人が採点した例、合格の線、そして較正をやり直す時期である。AI が出すのは、その基準にそった点と根拠までにする。一致がどこまで上がれば合否の根拠に使ってよいか。その線は、結果を見る前に人が決めておく。結果を見てから決めると、採点役に合わせた線になりやすい。

!!! example "判断例：記事の推敲ループの採点を決める"
    - **状況**：Claude に技術記事を推敲させるループを回している。毎回の版を点数で比べて、良い版を残したい。
    - **迷う候補**：採点役に総合点を付けさせて、一定の点を超えたら採用する案。人が毎回読んで選ぶ案。
    - **選んだもの**：表記・文字数・必須の見出しの有無はコード（textlint など）で採点する。論旨と読みやすさだけを、基準ごとの採点役に任せる。採点役は、人が採点した例で一致を確かめてから使い、使い始めた後も人が一部を抜き取って読む。
    - **理由**：総合点を超えたら採用する案は、点が高いのに読むと良くない版を通しやすい。人が毎回読む案は確実だが、ループの速さを失う。コードで決まる部分を外し、残りに較正済みの採点役を当てると、人が読む量を抑えながら、点の根拠を残せる。

## 判定役が見ているもの {#what-the-judge-sees}

判定役とは採点役のことである。採点役は、渡された文章しか見ない。成果物に何が書いてあるか、採点の依頼に何が書いてあるか、会話に何が出ているか。それ以外は、判定の材料にならない。

この性質は、組み込みの判定役でも同じである。`/goal` の判定役は、会話に出た証拠しか読まない。証拠が会話に出ていなければ、実際に仕事が済んでいても、済んだと判定できない（<!-- link:begin goal-until-done#evaluator-reads-conversation -->[/goal（完了するまで続けさせる） › 判定役は会話しか読まない](../delegate/goal-until-done.md#evaluator-reads-conversation)<!-- link:end -->）。採点役を自分で作るときも、何を見せて何を見せないかを決めるのは書き手である。

見せ方で気をつけることは次の 3 つである。

- **成果物と基準だけを見せる**。書いた側の説明や、書くまでの推論は見せない。それを読んだ採点役は、書き手の言い分に引っ張られる（<!-- link:begin independent-review#hide-reasoning -->[書いた本人ではない者にレビューさせる › 推論を見せない](../verify/independent-review.md#hide-reasoning)<!-- link:end -->、<!-- link:begin ask-without-sycophancy#fresh-context-critique -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 新しい文脈で、成果物と基準だけを見せる](../judgment/ask-without-sycophancy.md#fresh-context-critique)<!-- link:end -->）。
- **自分の見立てや好みを書き添えない**。「これは良い出来だと思う」と添えると、採点役はそれに合わせやすい（<!-- link:begin instructing-reviewers#hide-your-view -->[レビュアーへの指示の書き方 › 自分の見立てを書き添えない](../verify/instructing-reviewers.md#hide-your-view)<!-- link:end -->）。
- **経路ではなく結果を見せて採点させる**。公式の評価の記事は、経路ではなく結果で採点し、各試行をきれいな環境から始めることを勧めている（[Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)）。途中のやり取りまで見せるかは、基準が途中の振る舞いを問うかどうかで決める。

採点役をどこで走らせるかは、面ごとに違う。

=== "アプリ"
    新しい会話を開き、成果物と基準だけを貼って採点させる。書いた会話の続きで頼まない。件数が多いと貼る手間が増えるので、人の点との突き合わせは、少数の例に絞って行う。

=== "Claude Code"
    新しいセッションか、サブエージェントに、成果物のファイルと基準のファイルだけを渡して採点させる。書かせたセッションの続きで採点させない。サブエージェントの分け方は <!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end --> にある。

=== "API"
    採点用の呼び出しを別に作り、メッセージには成果物と基準だけを入れる。書いた側の呼び出しの履歴を引き継がない。同じ入力を何度か送り、点が揺れる幅を人の点との比較の前に見ておく。

AI の採点が高いことを、そのまま合意として数えない。採点役が高く採点したのは、採点の依頼とのずれがなかったことを示すだけで、良さの証拠ではない（<!-- link:begin agreement-is-not-evidence#reviewer-agreement -->[同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](../judgment/agreement-is-not-evidence.md#reviewer-agreement)<!-- link:end -->）。

## 使い続けるときの確かめ方 {#keep-checking}

較正は 1 回で終わらない。採点の依頼を直したとき、採点役のモデルを替えたとき、採点する成果物の種類が変わったときは、人が持っている例で一致を測り直す。

- **抜き取って人が読む**。採点役が通した成果物の一部を、人が抜き取って読む。点が高いのに読むと良くないものが出たら、その成果物を人の点付きの例に足して、較正の手順に戻る。
- **合否の線に近い成果物を重く見る**。合格の線の近くで食い違うと、合否が逆になる。線から遠い食い違いより、線の近くの食い違いを先に読む。
- **採点役の点を、人の点の代わりに記録しない**。記録には、人が付けた点と、採点役が付けた点を別の列で残す。後で較正をやり直すときの材料になる。
- **較正していない間は、合否の根拠にしない**。較正の前の AI の点は、傾向を見る参考にとどめる。採用や完了の判断は、人の判定か、コードの採点に置く。

## 失敗したとき {#when-it-fails}

- **人の点との一致が上がらない**。基準があいまいな可能性が高い。食い違いの行を読み直し、基準を観察できる言葉に書き直す（食い違いを表にして原因を分け、依頼を直す手順は、人の判定と比べて較正する節にある）。それでも一致しないなら、人の側の点が割れていないかを確かめる。人同士で点が割れる基準は、採点役にも決められない。
- **採点役が成果物を褒めすぎる**。素の Claude が凡庸な出来を褒めやすい傾向に当たる。点が下がる箇所を先に探させる指示と、点の低い例を依頼に足す。聞き方で迎合を減らす方法は <!-- link:begin ask-without-sycophancy -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)<!-- link:end --> にある。
- **同じ成果物の点が回ごとに揺れる**。複数回の点を取り、揺れの幅を見る。幅が合否の線をまたぐ基準は、基準を絞るか、コードで決められる形に変える。
- **点は一致するのに、読むと良くない**。測るための例が、実際に出る成果物を代表していない可能性がある。例を、最近の本番の成果物から取り直す（<!-- link:begin verifier-three-conditions#representative -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 本番を代表する](verifier-three-conditions.md#representative)<!-- link:end -->）。
- **採点役の評価を作る手間が大きすぎる**。コードで判定できる部分を増やして AI に任せる範囲を狭めるか、人が読む量を増やす。評価の仕組みそのものの確かめ方は <!-- link:begin test-the-verifier -->[検証器そのものを確かめる（red/green・手で計算したケース）](test-the-verifier.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)：Anthropic・英語・確認日 2026-11-04
- [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [検証器の三条件（正しい・書き換えられない・本番を代表する）](verifier-three-conditions.md)
- [変更が効いたかを測る（小さな eval）](measure-changes.md)

**関連**

- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [検証器そのものを確かめる（red/green・手で計算したケース）](test-the-verifier.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)
- [迎合（sycophancy）](../basics/sycophancy.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [レビュアーへの指示の書き方](../verify/instructing-reviewers.md)
- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- [textlint をフックで回す](../japanese/textlint-hook.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
