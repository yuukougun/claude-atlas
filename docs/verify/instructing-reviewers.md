---
id: instructing-reviewers
title: レビュアーへの指示の書き方
aliases: [レビューの頼み方, レビュー用のプロンプト, 指摘の出させ方]
type: concept
field: verify
chapter: レビューで確かめる
order: 120
level: 仕組みにする
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, 文章]
summary: レビュー役に、何を基準に何を出させるかを決めて頼める。網羅と選別を分け、自分の見立てを書き添えず、指摘ごとに確かめ方を付けさせる。
signs:
  - {type: symptom, text: レビューを頼むと、細かい好みの指摘ばかり出てくる}
  - {type: symptom, text: 「重大なものだけ」と頼んだら、大事な指摘まで減った}
  - {type: goal, text: レビュー役に、何をどこまで出させるかを決めたい}
prerequisites: [independent-review]
related: [ask-without-sycophancy, sycophancy, model-quirks, does-more-than-asked, grow-review-checklists, writing-subagents, second-opinion-from-another-model, automated-pr-review, agreement-is-not-evidence]
tracks: [subagents, code-review]
outdated_advice: []
sources: [api-docs-prompting-opus-5, arxiv-2607-10411, cc-docs-sub-agents, cc-docs-code-review-local]
volatility: 中
sections:
  - {title: 頼み方の例, anchor: example}
  - {title: 網羅と選別を分ける, anchor: exhaustive-then-filter}
  - {title: 自分の見立てを書き添えない, anchor: hide-your-view}
  - {title: 指摘ごとに確かめ方を付けさせる, anchor: per-finding}
  - {title: 何に効くか, anchor: effects}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：レビュー役への頼み方は、全部出させてから別の依頼で絞ること、見立てを書き添えないこと、指摘ごとに確かめ方を付けさせることの 3 つで決まると分かる。
    - **いつ引くか**：レビューを頼むと好みの指摘ばかり出るとき。「重大なものだけ」と頼んで、大事な指摘まで減ったとき。レビュー役に何をどこまで出させるかを決めたいとき。
    - **前提**：<!-- link:begin independent-review -->[書いた本人ではない者にレビューさせる](independent-review.md)<!-- link:end -->

<!-- textlint-disable -->
別名：レビューの頼み方・レビュー用のプロンプト・指摘の出させ方
<!-- textlint-enable -->

レビュアーへの指示の書き方は、レビュー役の Claude に、何を基準に何をどんな形で出させるかを決めて頼む技法である。誰にレビューさせるかは <!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](independent-review.md#who)<!-- link:end --> が扱い、このページは頼む文面を扱う。

## 頼み方の例 {#example}

同じレビューの依頼を、指示を足す前と後で並べる。レビュー役は、Claude Code ではサブエージェントや <!-- name:begin review-to-code-review -->/code-review<!-- name:end --> の実行で、アプリでは新しい会話である。

Before は、自分の見立てと絞り込みを 1 つの依頼に混ぜている。

```text
この PR をレビューして。自分ではたぶん大丈夫だと思う。重大なものだけ教えて。
```

After は、見立てを消し、先に全部出させ、指摘ごとに確かめ方を付けさせている。

<!-- gen:begin snippet instructing-reviewers/review-request-exhaustive -->
<!-- textlint-disable -->

??? example "雛形：網羅させてから選別するレビューの依頼"

    ```markdown
    次の変更をレビューしてほしい。対象は `git diff main...HEAD` の差分と、その差分が触れるテスト。

    - 見るもの：正しさ（仕様や要件と食い違う動き）、テストの抜け、壊れうる呼び出し元。書式や命名の好みは対象外。
    - 出し方：重大度で絞らず、気になったものを全部挙げる。迷うものも挙げ、確信度を低にして書く。絞るのは別の工程でやるので、ここでは落とさない。
    - 指摘ごとに、次の 5 つを付ける。
      1. 場所（ファイルと行）
      2. 何が起きうるか
      3. 確信度（高・中・低）と、その理由
      4. 影響の大きさ（壊れる範囲：大・中・小）
      5. 確かめる最小の実験（実行するコマンド、または足すテスト 1 件）。思いつかないときは「実験なし」と書く。
    - 書かないもの：直し方の実装と、この変更全体への評価（「問題なさそう」など）。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.147。

<!-- textlint-enable -->
<!-- gen:end snippet instructing-reviewers/review-request-exhaustive -->

After で足したものは 3 つある。「重大なものだけ」を「絞らず全部」に変えた。「たぶん大丈夫」を消し、見る範囲と基準に置き換えた。指摘に確信度・影響の大きさ・確かめる最小の実験を付けさせた。それぞれの理由を、次の 3 節で述べる。

## 網羅と選別を分ける {#exhaustive-then-filter}

網羅と選別を分けるとは、指摘を全部出させる工程と、そこから絞る工程を別の依頼にすることである。

「保守的に」「重大なものだけ」と書くと報告が減る。公式のモデル別の指針が、新しい世代のモデルについてそう述べている。指示を文字どおりに守るので、基準を厳しく書くと、その分だけ報告が減るという。大事な指摘まで減るのは、「見つける」判断と「重大か決める」判断が 1 つになるからである。重大か迷うものは、報告に載る前に落とされる。

逆に、「穴を探せ」とだけ頼むと、健全な作業にも指摘が付きやすい。全部を追うと、頼んでいない直しが増える（<!-- link:begin does-more-than-asked#forms -->[頼んでいないことまでやる（過剰設計） › よくある形](../symptoms/does-more-than-asked.md#forms)<!-- link:end -->）。

分け方は次のとおりである。

1. 1 段目：基準（正しさ、仕様との食い違い、テストの抜けなど）を決め、迷うものも確信度を低にして全部挙げさせる。
2. 2 段目：別の依頼で絞る。絞る基準は 2 段目に書く。指摘は消さず、保留に回して理由を残す。
3. 採否：人が決める。AI の絞り込みは、読む順を決める手伝いにとどまる。

絞る依頼の雛形を示す。1 段目の指摘の一覧だけを渡し、変更の意図や 1 段目の推論は渡さない。

<!-- gen:begin snippet instructing-reviewers/review-filter-pass -->
<!-- textlint-disable -->

??? example "雛形：指摘の一覧を、消さずに並べ替える選別の依頼"

    ```markdown
    次に貼るのは、先のレビューが出した指摘の一覧である。変更の意図の説明や、先のレビューの途中の推論は渡さない。この一覧だけを見て、人が読む順を決めてほしい。

    - 各指摘にある「確かめる最小の実験」のうち、実行できるものは実行し、結果（再現した・しない）を書く。
    - 並べ方は次の順にする。
      1. 実験で再現したもの
      2. 確信度が高く、影響の大きさが大きいもの
      3. それ以外は「保留」
    - 指摘を消さない。保留も一覧に残し、保留にした理由を 1 行で付ける。
    - 採否は決めない。決めるのは人である。

    一覧：
    （ここに、先のレビューの指摘を貼る）
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.147。

<!-- textlint-enable -->
<!-- gen:end snippet instructing-reviewers/review-filter-pass -->

「重大なものだけ」で報告が減る度合いは、モデルの世代で変わる。自分の環境では、同じ差分に「重大なものだけ」の依頼と「全部挙げる」の依頼を流し、件数と、後で実際に直した指摘が残ったかを比べるとよい（<!-- link:begin model-quirks#observe-and-record -->[モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する](../models/model-quirks.md#observe-and-record)<!-- link:end -->）。絞る担当を別のサブエージェントにする作り方は <!-- link:begin writing-subagents#define -->[サブエージェントの作り方と使いどころ › 定義の書き方（ファイルを書くか、Claude に作らせる）](../extend/writing-subagents.md#define)<!-- link:end --> にある。

## 自分の見立てを書き添えない {#hide-your-view}

自分の見立てを書き添えないとは、「たぶん大丈夫」「クリーンなはず」といった自分の評価や期待を、レビューの依頼に入れないことである。

レビュー役は、依頼に書かれた見立てに合わせやすい。<!-- link:begin sycophancy -->[迎合（sycophancy）](../basics/sycophancy.md)<!-- link:end --> は、利用者の考えに合う応答が好まれる形で訓練された結果、Claude が同意しやすくなる現象を指す。

見立てが判断を動かす例として、2026 年の査読前の論文（arXiv 2607.10411）がある。対象はコードスメルの検出で、利用者が前提を示すと判断が反転し、反転率は最大 72% だった。証拠に基づく推論を強いる手法を入れると、最低 12% まで下がった（根拠：中）。要旨だけを確かめたもので、モデルの大きさは要旨から分からない。Claude のレビュー一般に広げず、「見立てが判断を動かしうる」例として読む。

書かないものと、書くものを分ける。

- 書かない：「たぶん大丈夫」などの評価、結果への期待、「重大なものだけ」という先取りの絞り込み。
- 書く：見る範囲、基準、出力の形。変更の理由が要るなら、要件や仕様を事実として書く。

好みや確信を伏せる聞き方は <!-- link:begin ask-without-sycophancy#hide-preferences -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 好みと確信を伏せる](../judgment/ask-without-sycophancy.md#hide-preferences)<!-- link:end -->、変更を生んだ推論を見せない理由は <!-- link:begin independent-review#hide-reasoning -->[書いた本人ではない者にレビューさせる › 推論を見せない](independent-review.md#hide-reasoning)<!-- link:end --> にある。

## 指摘ごとに確かめ方を付けさせる {#per-finding}

指摘ごとに確かめ方を付けさせるとは、1 件ずつ、確信度・影響の大きさ・確かめる最小の実験を書かせることである。

実験は、実行するコマンドか、足すテスト 1 件の大きさにする。実験が思いつかない指摘は、「実験なし」と書かせる。そうすると、指摘が次の 2 つに分かれる。

- 実験で再現した指摘：人が結果を見て、直すかどうかを決められる。
- 実験なしの指摘：人が読んで決める。件数が多いときは、読む順を後ろにできる。

確信度と影響の大きさは、並べ替えの手がかりにする。確信度は Claude の自己申告で、実際の当たりやすさと合っている保証はないからである。採否の根拠にするのは、実験の結果である。批判に反証の実験を付けさせる考え方は <!-- link:begin ask-without-sycophancy#critique-with-experiments -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判には反証の実験を付けさせる](../judgment/ask-without-sycophancy.md#critique-with-experiments)<!-- link:end --> と同じである。複数の AI レビュアーが同じ指摘を出しても、それは正しさの証拠に数えない（<!-- link:begin agreement-is-not-evidence#reviewer-agreement -->[同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](../judgment/agreement-is-not-evidence.md#reviewer-agreement)<!-- link:end -->）。

## 何に効くか {#effects}

このページの 3 つの頼み方は、原理「確かめる」に当たる。防ぐ原因は「確かめていない」である。

「確かめていない」は、実行や根拠のないまま Claude が「大丈夫」と答える原因である。網羅させれば、迷う指摘が最初に落ちるのを防げる。見立てを伏せれば、見立てに合わせた「問題なし」を減らせる。確かめ方を付けさせれば、指摘が実行で確かめられる形になる。どれも、レビューの出力を「読んで納得する」ものから「実行で確かめる」ものへ寄せる。

## 効かない場面とやりすぎ {#limits}

指示の文面だけでは、レビューの質は決まらない。変更を書いた会話の中で頼むと、書いた推論を引きずる。文脈を分けることが先で、指示の書き方はその上に乗る（<!-- link:begin independent-review#what-happens -->[書いた本人ではない者にレビューさせる › 同じ会話で確かめさせると何が起きるか](independent-review.md#what-happens)<!-- link:end -->）。

網羅させすぎると、指摘が多すぎて人が読み切れない。1 段目は、見る観点を絞るか、差分を分けて頼む。2 段目の絞りで、読む順を付ける。

「批判せよ」を強めすぎると、正しいものまで否定される。加減は <!-- link:begin ask-without-sycophancy#dont-overdo-criticism -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判を強めすぎない](../judgment/ask-without-sycophancy.md#dont-overdo-criticism)<!-- link:end --> にある。

AI のレビューは、人の承認に数えない（<!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](independent-review.md#ai-approval)<!-- link:end -->）。見落としを直した PR から観点を足していく方法は <!-- link:begin grow-review-checklists -->[レビューの観点を育てる](../team/grow-review-checklists.md)<!-- link:end -->、別の系統のモデルに第二の意見を求める場面は <!-- link:begin second-opinion-from-another-model#when -->別のモデルに第二の意見を求める（一致は証拠にならない） › 使いどころ（準備中）<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [Mitigating LLM Sycophancy in Code Smell Detection Using Evidence-Guided Reasoning Prompts](https://arxiv.org/abs/2607.10411)：arXiv（Fahad, Istiaq Ahmed ほか）・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Review locally with /code-review](https://code.claude.com/docs/en/code-review-local)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [書いた本人ではない者にレビューさせる](independent-review.md)

**次に読む**

- [レビューの観点を育てる](../team/grow-review-checklists.md)

**関連**

- [迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](../judgment/ask-without-sycophancy.md)
- [迎合（sycophancy）](../basics/sycophancy.md)
- [モデル別の癖と、プロンプトの合わせ方](../models/model-quirks.md)
- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- [サブエージェントの作り方と使いどころ](../extend/writing-subagents.md)
- 別のモデルに第二の意見を求める（一致は証拠にならない）（準備中）
- 自動 PR レビュー（Code Review・/ultrareview）（準備中）
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
