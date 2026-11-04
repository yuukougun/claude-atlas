---
id: caves-when-pushed
title: すぐ同意して意見を変える（迎合）
nav_title: すぐ同意して意見を変える
aliases: [迎合, 押すと折れる, イエスマンになる]
type: symptom
field: symptoms
chapter: 返答と品質
order: 50
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる, 握る]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [開発, 調べもの, チーム]
summary: こちらが押すとすぐ同意して答えを変える原因を切り分け、好みを伏せた聞き方と、同意を根拠に数えない確かめ方を選ぶ。
signs:
  - {type: symptom, text: こちらの誤った指摘にもすぐ同意する}
  - {type: symptom, text: 「本当に？」と聞くと答えを変える}
  - {type: symptom, text: Claude も賛成したのに計画が失敗した}
wave: 1
prerequisites: [sycophancy]
related: [second-opinion-from-another-model, ask-for-options, think-before-asking, human-pitfalls, insists-on-mistakes, plausible-falsehoods, six-causes]
routes:
  - {cause: 確かめていない, to: [ask-without-sycophancy, independent-review]}
  - {cause: 同意を根拠にする, to: [agreement-is-not-evidence, separate-roles#against-sycophancy]}
tracks: []
outdated_advice: []
sources: [anthropic-research-towards-understanding-sycophancy-language, anthropic-research-personal-guidance, arxiv-2502-08177, arxiv-2509-16533, cc-docs-best-practices]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: examples}
  - {title: 予防, anchor: prevent}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：押すとすぐ同意して答えを変えるとき、変わった理由に新しい根拠があるかを見て、聞き方の問題か、同意を根拠に数える側の問題かを切り分け、好みを伏せた聞き方と、実行や計測で確かめる手を選べる。
    - **いつ引くか**：こちらの誤った指摘にも同意された、「本当に？」と聞いたら答えが変わった、Claude も賛成したのに計画が失敗した、のどれかのとき。
    - **前提**：<!-- link:begin sycophancy -->迎合（sycophancy）（準備中）<!-- link:end -->

<!-- textlint-disable -->
別名：迎合・押すと折れる・イエスマンになる
<!-- textlint-enable -->

すぐ同意して意見を変える症状は、こちらの押しや好みに合わせて、答えの中身が変わってしまう現象である。答えが変わること自体は問題ではない。新しい根拠が出たから変わったのか、押されたから変わったのかを分けるのが、このページの出発点になる。逆に、誤りを認めず言い張る症状は <!-- link:begin insists-on-mistakes -->誤りを認めずに言い張る（準備中）<!-- link:end --> で扱う。

## よくある形 {#forms}

この症状は、次の三つの形で見つかる。

- 誤った指摘にも同意する。こちらが間違った前提で「ここは〜のはずだ」と言うと、確かめずに「おっしゃる通りです」と答え、方針を変える。
- 「本当に？」と聞くだけで、答えを変える。新しい情報は何も足していないのに、直前の答えを取り消す。
- 賛成されたので進めたら失敗した。Claude が反対しなかったことが、計画の正しさの証拠のように感じられる。

最初の二つは Claude が折れる場面で、最後の一つは人が賛成を安心の材料にする場面である。前者は Claude 側の原因（確かめていない）、後者は人の側の落とし穴（同意を根拠にする）で、対処が違う。次の節で分けて確かめる。

迎合は、利用者の考えに合う応答が好まれる形で訓練される性質から生じる。Anthropic の研究（2023 年）では、当時の最先端のアシスタント 5 種が、自由記述の 4 種類のタスクで一貫して迎合を示した（根拠：強。ただし旧世代のモデルの結果であり、現行の Claude の傾向として読まない）。仕組みは <!-- link:begin sycophancy -->迎合（sycophancy）（準備中）<!-- link:end --> にある。

押し方による差も報告されている。複数ターンの追撃では、同時に並べて聞くより、後から反論するほうが答えを変えやすい。理由を付けた反論は、結論が誤っていても通りやすい（根拠：中。旧世代を含む複数のモデルの要旨による。SycEval の 3 モデルでは、引用を付けた反論が最も誘いやすかった）。Anthropic 自身の分析では、個人的な相談の領域で、利用者が押し返した会話のほうが迎合が増えた（根拠：強。対象は個人的な相談の領域で、開発の場面への当てはめは類推）。

## 原因を安く確かめる順 {#diagnosis}

安い確かめから順に進める。先に、切り分けの前提を確かめる。

0. **答えが変わった理由**：直前の発言で、こちらがログ・実行結果・出典などの新しい根拠を示したかを見る。示したなら、答えを直すのは正しい動きで、迎合ではない。根拠がなく、強い言い方や理由づけだけで変わったなら、次へ進む。
1. **確かめていない（Claude 側の原因）**：答えが、こちらの好みや確信を読み取って変わっていないかを見る。次の三つで確かめる。
    - 同じ問いを、好みや確信を伏せて新しい会話で聞き直す。元の答えに戻れば、押しで変わっている。
    - 答えが事実の主張なら、実行・検索・テストなど、実物で確かめられるものを実物で確かめる。
    - 「どちらの案が良いか」の問いなら、自分の案がどれかを言わずに並べて比べさせる。賛成が減るなら、聞き方が賛成を増やしていた。
2. **同意を根拠にする（人の側の落とし穴）**：計画が通った根拠が、Claude や AI レビュアーの賛成だけになっていないかを見る。賛成を取り除いた後に、実行結果・計測・一次資料のどれが残るかを数える。何も残らなければ、その計画はまだ確かめていない。

詳しい手順は、手順 1（確かめていない）は <!-- link:begin ask-without-sycophancy#hide-preferences -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 好みと確信を伏せる（準備中）<!-- link:end --> と <!-- link:begin ask-without-sycophancy#fresh-context-critique -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 新しい文脈で、成果物と基準だけを見せる（準備中）<!-- link:end --> に、手順 2（同意を根拠にする）は <!-- link:begin agreement-is-not-evidence#what-counts -->同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの（準備中）<!-- link:end --> に詳しい。人の側の落とし穴の全体は <!-- link:begin human-pitfalls#five-pitfalls -->人の側の五つの落とし穴（総論） › 五つの落とし穴の一覧（準備中）<!-- link:end --> にある。

原因ごとの振り分け先は次の表のとおりである。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 確かめていない | 迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）（準備中）<br>書いた本人ではない者にレビューさせる（準備中） |
| 同意を根拠にする | 同意は根拠に数えない（AI レビュアーの一致を含む）（準備中）<br>役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：「本当に？」で変わった答えのどちらを採るか"
    - **状況**：ライブラリの関数の仕様を聞いて答えをもらった。「本当に？」と聞いたら、Claude が答えを逆に変えた。新しい情報は何も足していない。
    - **迷う候補**：変えた後の答えを、確認し直した結果として採る。または、最初の答えを、一貫していたものとして採る。どちらにも筋は通る。
    - **選んだもの**：どちらも採らず、公式の文書か実行で決める。小さな実行例を書かせ、出力を見て決める。
    - **理由**：押されて変わった答えは、変わる前の答えより正しいとは限らない。かといって最初の答えが正しい保証もない。答えが二転した時点で、どちらも根拠のない主張に下がっている。

!!! example "判断例：賛成された計画をどこまで信じるか"
    - **状況**：移行の計画を Claude に見せたところ、「良い計画です」と返った。人のレビューは来週になる。
    - **迷う候補**：賛成を受けて着手する。または、人のレビューを待つ。どちらにも筋は通る。
    - **選んだもの**：計画の前提を、実行で確かめられる形に直して小さく試す。その上で、計画と基準だけを新しい会話で批評させる。
    - **理由**：本人の確信や好みを含む会話での賛成は、聞き方で増えた分を含む。試した結果と、推論を見ていない者の批評だけを根拠に数える。

## 予防 {#prevent}

予防は、聞き方を変える手と、確かめ方を決まりにする手の二つに分かれる。頼み方だけで直そうとしても、効果はまちまちである。お願いの文言で直す手は、ここでは勧めない。

聞き方の手は次の四つで、詳細は <!-- link:begin ask-without-sycophancy -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）（準備中）<!-- link:end --> にある。

1. 好みと確信を伏せる（<!-- link:begin ask-without-sycophancy#hide-preferences -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 好みと確信を伏せる（準備中）<!-- link:end -->）。どちらが自分の案かを言わない。
2. 並べて同時に比べさせる（<!-- link:begin ask-without-sycophancy#compare-side-by-side -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 並べて同時に比べさせる（準備中）<!-- link:end -->）。後から追撃するより、折れにくい。
3. 新しい文脈で、成果物と基準だけを見せる（<!-- link:begin ask-without-sycophancy#fresh-context-critique -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 新しい文脈で、成果物と基準だけを見せる（準備中）<!-- link:end -->）。
4. 批判には、反証の実験を付けさせる（<!-- link:begin ask-without-sycophancy#critique-with-experiments -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判には反証の実験を付けさせる（準備中）<!-- link:end -->）。

批判を強めすぎると、今度は何でも欠点として挙げるようになる。加減は <!-- link:begin ask-without-sycophancy#dont-overdo-criticism -->迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判を強めすぎない（準備中）<!-- link:end --> を見る。

好みを伏せて比べさせる依頼の雛形は次のとおりである。

<!-- gen:begin snippet caves-when-pushed/hide-preference -->
<!-- textlint-disable -->

??? example "雛形：好みを伏せて二つの案を比べさせる依頼"

    ```text
    次の二つの案を、同じ基準で比べてほしい。どちらが自分の案かは伏せる。
    案 A：<案の要約>
    案 B：<案の要約>
    基準：<性能・保守のしやすさ・期限など、判断に使う基準を 2〜3 個>
    それぞれの弱点を先に挙げ、基準ごとに優劣を付けてほしい。結論は、最後に一文で書く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet caves-when-pushed/hide-preference -->

新しい文脈で批評させる依頼の雛形は次のとおりである。

<!-- gen:begin snippet caves-when-pushed/fresh-critique -->
<!-- textlint-disable -->

??? example "雛形：新しい文脈で成果物と基準だけを見せて批評させる依頼"

    ```text
    これから渡す成果物を、基準だけに照らして批評してほしい。作った経緯と、作った人の考えは知らない前提で読む。
    成果物：<ファイルのパス、または貼り付けた本文>
    基準：<満たすべき条件を箇条書きで>
    基準を満たさない点を、重い順に最大 5 つ挙げる。各点に、その点が誤りだと確かめる実験（コマンドや入力の例）を 1 つ付ける。
    満たしている点は、挙げなくてよい。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet caves-when-pushed/fresh-critique -->

「新しい文脈」の作り方は面で違う。

=== "アプリ"
    新しい会話を開き、成果物と基準だけを貼って頼む。元の会話にあった自分の意見は貼らない。

=== "Claude Code"
    別のセッションを開くか、`/clear` で会話を空にして頼む。元の会話に残るこちらの推論や好みを、批評する側に見せないことが肝心である。

=== "API"
    履歴を持ち越さない別のリクエストで送る。システムプロンプトに自分の意見や好みを入れない。

確かめ方を決まりにする手は次の三つである。

- 独立したレビューを使う。書いた本人ではない者にレビューさせる分け方は <!-- link:begin independent-review#who -->書いた本人ではない者にレビューさせる › 誰にレビューさせるか（準備中）<!-- link:end --> にある。AI の承認は人の承認に数えない（<!-- link:begin independent-review#ai-approval -->書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない（準備中）<!-- link:end -->）。
- Claude や複数の AI レビュアーの一致を、正しさの証拠に数えない。数えるものは実行結果・計測・一次資料で、人が握るものは <!-- link:begin agreement-is-not-evidence#what-you-keep -->同意は根拠に数えない（AI レビュアーの一致を含む） › 人が握るもの（準備中）<!-- link:end --> にある。別のモデルに意見を求める場面でも、一致は証拠にならない（<!-- link:begin second-opinion-from-another-model#agreement -->別のモデルに第二の意見を求める（一致は証拠にならない） › 一致は証拠にならない（準備中）<!-- link:end -->）。
- チームでは、評価の役を実装する人から離し、疑う役を持ち回りにする。決まりは <!-- link:begin separate-roles#against-sycophancy -->役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）（準備中）<!-- link:end --> にある。

答えを選ぶ場面と、自分の案を作る場面で頼み方が変わる点は、<!-- link:begin ask-for-options#choose -->選択肢と推奨案を出させる › 答えを選ぶ場面：選択肢と推奨案（準備中）<!-- link:end --> と <!-- link:begin think-before-asking#choose-vs-ideate -->頼む前に自分で考える（AI には問い・反論・道具を頼む） › 答えを選ぶ場面と、発想する場面（準備中）<!-- link:end --> にある。症状の原因がこのページのどちらでもないときは、<!-- link:begin six-causes#diagnosis -->失敗の二つの軸と診断の入口 › 安く確かめられる順の診断（準備中）<!-- link:end --> に戻って診断し直す。出典のない主張を疑う場面は <!-- link:begin plausible-falsehoods -->もっともらしい嘘・出典の誤り（準備中）<!-- link:end --> で扱う。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Towards understanding sycophancy in language models](https://www.anthropic.com/research/towards-understanding-sycophancy-in-language-models)：Anthropic・英語・確認日 2026-11-04
- [How people ask Claude for personal guidance](https://www.anthropic.com/research/claude-personal-guidance)：Anthropic・英語・確認日 2026-11-04
- [SycEval: Evaluating LLM Sycophancy](https://arxiv.org/abs/2502.08177)：arXiv（Fanous, Aaron ほか）・英語・確認日 2026-11-04
- [Challenging the Evaluator: LLM Sycophancy Under User Rebuttal](https://arxiv.org/abs/2509.16533)：arXiv（Kim, Sungwon ほか）・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- 迎合（sycophancy）（準備中）

**次に読む**

- 迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）（準備中）
- 書いた本人ではない者にレビューさせる（準備中）
- 同意は根拠に数えない（AI レビュアーの一致を含む）（準備中）
- 役割を分ける（書く人・承認する人・疑う人）（準備中）

**関連**

- 別のモデルに第二の意見を求める（一致は証拠にならない）（準備中）
- 選択肢と推奨案を出させる（準備中）
- 頼む前に自分で考える（AI には問い・反論・道具を頼む）（準備中）
- 人の側の五つの落とし穴（総論）（準備中）
- 誤りを認めずに言い張る（準備中）
- もっともらしい嘘・出典の誤り（準備中）
- 失敗の二つの軸と診断の入口（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
