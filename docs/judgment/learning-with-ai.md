---
id: learning-with-ai
title: AI で新しい技術を学ぶ（生成させた後に理解を確かめる）
nav_title: AI で新しい技術を学ぶ
aliases: [AI で学ぶと身につかない, 技能形成, AI を使った学習]
type: judgment
field: judgment
chapter: 理解を手放さない
order: 80
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [握る, 確かめる]
prevents: []
pitfalls: [預けすぎる, 体感を信じる]
scenes: [学習, 開発, コンテスト]
summary: AI に書かせても速さの得は確かめられず、理解が残りにくいことと、生成の後に理解を確かめる、エラーは自分で直す、といった理解が残る使い方が分かる。
signs:
  - {type: symptom, text: AI と一緒だと分かった気になるが、AI なしでは解けない}
  - {type: situation, text: 新しいライブラリや手法を、AI と一緒に覚えたい}
  - {type: goal, text: コンテストの上位解法や解説を AI に要約させて学びたい}
wave: 1
prerequisites: [over-reliance]
related: [how-much-understanding-to-keep, own-generated-code, output-style-modes, felt-vs-measured, summary-overstates-source, checking-citations, practice-vs-contest-day, think-before-asking, explore-a-codebase, fix-a-bug, retros-without-ai-verdicts]
tracks: [output-styles]
outdated_advice: []
sources: [anthropic-research-ai-assistance-coding-skills, arxiv-2601-20245, pnas-bastani-2025-genai-learning, pmc-kestin-2025-ai-tutoring, arxiv-2607-03303, arxiv-2607-05068, cc-docs-output-styles, qiita-kmat67916008-d7586a]
volatility: 低
sections:
  - {title: 速さの得は確かめられず、理解は残りにくい, anchor: faster-but-shallower}
  - {title: 理解が残る使い方・残らない使い方, anchor: patterns}
  - {title: なぜ理解が残らないのか, anchor: why}
  - {title: 新しい技法を学ぶ手順, anchor: learning-steps}
  - {title: 答えではなくヒントを返させる, anchor: hints-not-answers}
  - {title: 上位解法や解説を AI に要約させるとき, anchor: summaries-of-solutions}
  - {title: 人が握るもの, anchor: what-you-keep}
  - {title: 理解が残ったかの確かめ方, anchor: how-to-check}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：AI に書かせると進みは速いが理解は残りにくい。理解の残る使い方が分かる。
    - **いつ引くか**：AI と一緒だと分かった気になるが、AI なしでは解けないとき。新しい手法を覚えたいとき。上位解法を AI に要約させたいとき。
    - **前提**：<!-- link:begin over-reliance -->[判断を預けすぎる（過度依存）](over-reliance.md)<!-- link:end -->

<!-- textlint-disable -->
別名：AI で学ぶと身につかない・技能形成・AI を使った学習
<!-- textlint-enable -->

AI で新しい技術を学ぶときの判断を扱うページである。AI に実装させれば動くものはすぐできるが、動くことと、自分が分かっていることは別である。理解を残す使い方を選び、残ったかを自分で確かめる。

## 速さの得は確かめられず、理解は残りにくい {#faster-but-shallower}

AI に実装を任せると、新しい技術でも動くコードがすぐ手に入る。その一方で、自分の理解は残りにくい。

Anthropic が 2026 年に公表した研究（論文は arXiv 2601.20245）が、この差を測っている。52 人の開発者が、知らない Python の非同期ライブラリ Trio を学ぶ課題に取り組んだ。課題の直後の理解度クイズは、AI を使った群が 50%、手で書いた群が 67% だった（Cohen's d=0.738）。差が最も大きかったのはデバッグの問題である。完了時間の差は有意でなかった（根拠：強）。

つまりこの課題では、速さの得は確かめられず、理解の差だけが出た。作業が進んでいる感覚と、理解が残る度合いは別に動く。

この結果には限りがある。当てはめるときは次の点を覚えておく。

- 小規模な実験である。52 人で、各群は 26 人である。
- AI 群のアシスタントは GPT-4o をもとにしたものである。Claude 固有の結果ではない。
- クイズは課題の直後に行われた。長期の技能が残るかは分からない。
- アルゴリズムの学習やコンテストに固有のデータはない。ここへの当てはめは類推である。

## 理解が残る使い方・残らない使い方 {#patterns}

同じ研究の使い方の分析では、AI の使い方で理解度クイズの成績が大きく分かれた。

| 使い方 | 保った成績（約） |
| --- | --- |
| 生成させた後に、理解を確かめる質問をする | 86% |
| コードと説明を同時に求める | 68% |
| 概念だけを聞き、エラーは自分で解く | 65% |
| 丸投げする | 39% |
| 少しずつ依存していく | 35% |
| デバッグを AI に任せ、反復させる | 24% |

表の上の 3 行が理解の残った型で、下の 3 行が残らなかった型である（根拠：中）。ただし、各型は n=2〜7 の小さな群で、40% に届かない 3 型は各 n=4 である。この分類は傾向であり、使い方と結果の因果を研究は主張していない。理解したい人が、もともと理解を確かめる質問をする型を選んだ可能性も残る。

著者らは、Claude Code のようなエージェント型のツールでは影響がさらに大きくなりうると注記している。これは著者の推測であり、確かめられた結果ではない。

型の名前を覚えるより、差が出た場所を覚えるほうが使える。理解が残った型は、どれも自分で考える作業を手元に残している。残らなかった型は、考える作業を AI に渡している。渡しすぎの一般的な仕組みは、前提のページが扱う。<!-- link:begin over-reliance#why-we-hand-over -->[判断を預けすぎる（過度依存） › なぜ預けてしまうか](over-reliance.md#why-we-hand-over)<!-- link:end -->

## なぜ理解が残らないのか {#why}

理解が残らない理由は、自分で考える機会が減ることと、残っていないことに自分で気づきにくいことの 2 つに分けて考えられる。

1 つめは、エラーに自分で当たる機会である。Trio を学ぶ課題の研究では、手で書いた対照群のほうがエラーに多く遭遇していた。著者らは、自力でエラーを解いた経験がデバッグ能力の形成に寄与した可能性があると述べている（根拠：中）。エラーは、仕組みの理解のずれが表に出る場所である。AI に直させるとその場は進むが、ずれに気づく機会を渡すことになる。

2 つめは、体感が実際より楽観的になることである。トルコの高校生約 1,000 人が数学を学んだ実験（Bastani ほか、PNAS 2025、GPT-4 を使用）では、素の GPT-4 を使った群の練習中の成績が 48% 上がった。ところが AI を外した試験では、対照群より 17% 低かった。本人の自己評価も楽観的すぎた（根拠：強・類推。数学の学習で、コンテストではない）。分かった気になる感覚は、理解の証拠にならない。体感と実測のずれの仕組みは、別のページが扱う。<!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end -->

## 新しい技法を学ぶ手順 {#learning-steps}

焼きなまし・ビームサーチ・MCTS・新しいライブラリといった未知の技法を、AI と学ぶときの手順を示す。理解が残った使い方の型（生成後に質問する、概念だけ聞いてエラーは自分で解く）を手順に直したもので、この手順そのものの効果を調べた研究はない（類推）。

1. **概念を質問する**。実装の前に、その技法が何を解く道具で、どんな部品でできているかを聞く。
2. **AI に実装させたら、自分に質問を出させる**。温度・近傍・評価関数などの役割について 3 問出題させ、答えるまで次に進ませない。
3. **エラーは、まず自分で仮説を立てる**。AI には、仮説の確かめ方や概念だけを聞く。直すのは自分である。
4. **結果を先に予測してから、実験で確かめる**。たとえば「温度を 10 倍にしたら何が起きるか」を先に書き、AI に作らせた実験のスクリプトで確かめる。

2 の質問を出させる雛形を示す。

<!-- gen:begin snippet learning-with-ai/quiz-after-generate -->
<!-- textlint-disable -->

???+ example "雛形：生成の後に、役割について自分に質問を出させる"

    ```markdown
    いま実装してもらった <手法名> のコードについて、次の順で進めてください。

    1. 温度・近傍・評価関数など、このコードの主な部品の役割について、私に 3 問出題してください。
    2. 1 問ずつ出してください。私が答えるまで、正解も解説も言わないでください。
    3. 私の答えをコードに照らして採点し、間違いの理由だけを短く伝えてください。
    4. 3 問に答え終えるまで、次の実装や改善に進まないでください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.81。

<!-- textlint-enable -->
<!-- gen:end snippet learning-with-ai/quiz-after-generate -->

質問に答えるのは自分である。答えを AI に考えさせたり、正解を先に聞いたりすると、確かめる意味がなくなる。

手順 3 でエラーの直しを自分に残すのは、学ぶ場面での線引きである。本番のコードのバグを直す依頼は、別のページが扱う。<!-- link:begin fix-a-bug#hypotheses-before-fixes -->[バグを直す › 直す前に仮説を確かめさせる](../recipes/fix-a-bug.md#hypotheses-before-fixes)<!-- link:end -->

!!! example "判断例：明後日の長期コンテストまでに、焼きなましを使えるようにする"
    - **状況**：焼きなましを初めて使う。AI に実装させたところ、コードは動いた。ただし、近傍の取り方と温度の下げ方は説明できない。コンテストは明後日で、時間は限られている。
    - **迷う候補**：コードをそのまま使い、スコアが悪ければ AI に直させて進める。または、時間を削ってでも、役割の質問と予測の実験を挟んでから使う。
    - **選んだもの**：先に役割の質問 3 問へ答える。答えられなかった部分は、予測を立てて実験で確かめてから使う。
    - **理由**：近傍と温度は、スコアを上げる調整の中心になる。説明できないまま使うと、悪くなったときに何を疑うか分からず、結局は AI の反復デバッグに戻る。質問と予測には時間がかかるが、調整の見当が付けば、本番で迷う時間が減ると見込める。

この判断例で、どちらの候補にも筋は通る。時間が本当に足りず、まず動くものが要るなら前者もありうる。その場合は、本番の後に残った分を同じ手順で埋める。

## 答えではなくヒントを返させる {#hints-not-answers}

AI に答えを返させると理解が落ちる場面でも、返し方を変えれば落ち方を抑えられる。

- 高校生の数学の学習の実験（Bastani ほか、PNAS 2025）で、答えではなくヒントを返すように設計したチューターを使った群は、AI を外した試験の成績の低下をほぼ打ち消した（根拠：強・類推）。
- 段階的な模範解答を事前にプロンプトへ入れ、誤答を防いだ物理の AI チューターは、教室での能動学習より学習の伸びが大きかった（Kestin ほか、Scientific Reports 2025。根拠：中・類推）。
- ソクラテス式に問うチューターで 6 週間学んだ群は、その後に制約のない LLM を使わせても、理解を志向するプロンプトを多く使った。ただし学習者からは「効率が悪い」と評価された（Brender ほか。根拠：中・類推）。
- CS1 の受講生 917 人の研究では、ほぼ正しい AI の解に現実的なバグを注入すると、学生はコードを直接読んで直す傾向が増え、次の試行の成功率も高かった（根拠：中・類推）。

どれも、コンテストに向けた個人の独学を対象にした実験ではない。数学・物理・大学の入門課程の結果で、現行の Claude の傾向でもない。ただ、答えを出さずにヒントを返す設計や、正しい資料を先に見せる設計が学習に効く、という向きは一致している。同時に、効く設計ほど学習者に嫌われやすい。楽な設計が理解の残る設計とは限らない。

頼み方は面で違う。

=== "アプリ"

    会話の最初の依頼で、ヒントだけを返す約束を頼む。下の雛形を使える。お願いなので、途中で守られなくなることがあれば、会話の途中でも言い直す。

=== "Claude Code"

    会話での頼み方は、アプリと同じである。セッション全体の答え方を切り替えるには、出力スタイルが使える。Learning という組み込みのスタイルは、設計判断を含む数行を `TODO(human)` として利用者に書かせる設計である。ただし、この学習効果を示す実証データは見つかっていない。設計上の意図として紹介する。スタイルの種類と使い方は、機能のページが扱う。<!-- link:begin output-style-modes#built-in -->[出力スタイルで応答の仕方を切り替える › 組み込みのスタイル](../cli/output-style-modes.md#built-in)<!-- link:end -->

<!-- gen:begin snippet learning-with-ai/hints-only -->
<!-- textlint-disable -->

??? example "雛形：答えではなくヒントを返させる"

    ```markdown
    この会話では、私の学習の相手をしてください。次の決まりで答えてください。

    - 完成したコードや最終的な答えを、先に書かないでください。
    - 私の質問には、まずヒントを 1 つだけ返してください。足りなければ私が「次のヒント」と頼みます。
    - ヒントは、考える方向（着目する量、試す小さな例、思い出す概念）を示すものにしてください。
    - エラーの原因を、先に言い当てないでください。何を確かめるとよいかだけを聞いてください。
    - 私が自分の答えを書いたら、その答えの誤りと、誤りの理由を指摘してください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.81。

<!-- textlint-enable -->
<!-- gen:end snippet learning-with-ai/hints-only -->

## 上位解法や解説を AI に要約させるとき {#summaries-of-solutions}

コンテストの後に上位解法や解説を読むのは、よい学び方である。AI に要約させると読む時間は減るが、要約は手法を正当化した条件を落としやすい。

実践者の記事（Kaggle のコンペの経験談。根拠：弱）は、上位解法の前提が性能を縛ることがあるので、手法だけでなく、なぜその問題でそれが効いたかを読む必要があると指摘している。要約でこの「なぜ」が落ちると、手法だけが別の問題へ持ち込まれ、効かない理由が分からなくなる。

対策は、要約の形を先に決めることである。手法・その手法を正当化した問題の性質・原文の短い引用の 3 列の表にさせ、原文にない一般化を禁じる。

<!-- gen:begin snippet learning-with-ai/summarize-solutions -->
<!-- textlint-disable -->

??? example "雛形：上位解法を、手法・性質・引用の 3 列で要約させる"

    ```markdown
    次に貼る上位解法の文章（または解説）を、次の 3 列の表に要約してください。

    | 手法 | その手法を正当化した問題の性質 | 原文の該当箇所の引用 |
    | --- | --- | --- |

    決まりは次のとおりです。

    - 原文に書かれていないことを足さないでください。他の問題に当てはまる、といった一般化も禁じます。
    - 「問題の性質」の列は、原文がその手法を選んだ理由として挙げた条件だけを書いてください。原文に理由がなければ「原文に記載なし」と書いてください。
    - 引用は原文の短い抜き出しにし、言い換えないでください。

    <ここに上位解法の文章を貼る>
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.81。

<!-- textlint-enable -->
<!-- gen:end snippet learning-with-ai/summarize-solutions -->

表は読む入口にすぎない。次の 2 つを守る。

- 引用が原文にあるかを、原文で確かめる。要約が原文より断定的になっていないかは、別のページの手順で確かめられる。<!-- link:begin summary-overstates-source#diagnosis -->[要約が原文より断定的になる › 原因を安く確かめる順](../symptoms/summary-overstates-source.md#diagnosis)<!-- link:end -->
- 最も重要な 1 つの解法は、要約に頼らず原文を自分で読む。

コンテストの後に、自分の AI の使い方（モデル・効いた指示・効かなかった指示）を書き残すと、次の練習に戻せる。書き残し方は別のページが扱う。<!-- link:begin retros-without-ai-verdicts#record-ai-usage -->振り返りで AI に評価させない（集計係にとどめる） › 作業の後に AI の使い方を書き残す（準備中）<!-- link:end -->

## 人が握るもの {#what-you-keep}

学ぶ場面で人が握るのは、次の 4 つである。

- **質問に答えること**。理解の確かめは自分がやる。AI は問題を出し、採点する側に置く。
- **エラーの仮説**。AI へ聞く前の段階で、自分の原因の見当を書く。
- **予測**。実験の前に結果を書き、外れた理由を考える。
- **原文を読むこと**。要約は入口にとどめ、重要な箇所は原文で確かめる。

独創性の要る考察では、答えそのものを AI に頼らず、先に自分の案を書く順序が要る。<!-- link:begin think-before-asking#self-first -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 先に自分、その後で AI](think-before-asking.md#self-first)<!-- link:end -->

どこまで理解を求めるかは、コードの重要度で変わる。周辺のコードは任せきりでよく、中核は説明できるまで確かめる。その線引きは、別のページが扱う。<!-- link:begin how-much-understanding-to-keep#core-and-periphery -->[どこまで理解を手放してよいか（中核と周辺） › 中核と周辺を分ける](how-much-understanding-to-keep.md#core-and-periphery)<!-- link:end -->

## 理解が残ったかの確かめ方 {#how-to-check}

分かった気になる感覚は当てにならないので、記録で測る。

- **AI なしで書き直せるか**。数日後に、AI を使わず、手法の核になる部分を一から書く。書けた所と詰まった所を記録する。
- **予測の当たり外れ**。実験の前に書いた予測と、実測の結果を並べて残す。外れが続くなら、仕組みの理解がずれている。
- **言い直せなかった質問**。AI が出した質問のうち、自分の言葉で答えられなかったものを控える。次の学習の入口にする。

記録の取り方は、体感を実測で置き換える別のページが扱う。<!-- link:begin felt-vs-measured#what-to-record -->[体感と実測 › 記録で測るもの](../eval/felt-vs-measured.md#what-to-record)<!-- link:end -->

やめどきも先に決めておく。たとえば、同じ質問に 2 回続けて答えられなかったら、AI を閉じて原文か公式の文書を読む。AI を使わない時間を残す考え方は、別のページが扱う。<!-- link:begin how-much-understanding-to-keep#ai-free-time -->[どこまで理解を手放してよいか（中核と周辺） › AI を使わない時間を残す](how-much-understanding-to-keep.md#ai-free-time)<!-- link:end -->

大会に向けては、本番の条件で自力を確かめる段階も要る。<!-- link:begin practice-vs-contest-day#test-under-contest-conditions -->[練習と本番の使い分け（AI を禁じる大会に向けた練習を含む） › 本番の条件で自力を確かめる](../contest/practice-vs-contest-day.md#test-under-contest-conditions)<!-- link:end -->

生成されたコードを採る前に、処理の流れを説明させて確かめる手順は、学ぶ場面ではなく出荷の基準として、別のページが持つ。<!-- link:begin own-generated-code#explain -->[生成コードを自分のものにする › 処理の流れと入力の端を説明させる](../verify/own-generated-code.md#explain)<!-- link:end -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)：Anthropic・英語・確認日 2026-11-04
- [How AI Impacts Skill Formation](https://arxiv.org/abs/2601.20245)：arXiv（Shen, Judy Hanwen ほか）・英語・確認日 2026-11-04
- [Generative AI without guardrails can harm learning: Evidence](https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html)：RePEc IDEAS（PNAS の論文の書誌）・英語・確認日 2026-11-04
- [AI tutoring outperforms in-class active learning: an RCT introducing a novel research-based design in an authentic educational setting](https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/)：PubMed Central・英語・確認日 2026-11-04
- [Reflective Dialogue or Prompt Refinement? Effects of Tutor Scaffolding on Students' Independent LLM Use for Programming](https://arxiv.org/abs/2607.03303)：arXiv（Brender, Jerome ほか）・英語・確認日 2026-11-04
- [When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code](https://arxiv.org/abs/2607.05068)：arXiv（Pădurean, Victor-Alexandru ほか）・英語・確認日 2026-11-04
- [Output styles](https://code.claude.com/docs/en/output-styles)：Anthropic・英語・確認日 2026-11-04
- [Kaggle画像コンペでやっていること④](https://qiita.com/Kmat67916008/items/d7586a28e6ec8595d579)：Qiita（Kmat67916008）・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [判断を預けすぎる（過度依存）](over-reliance.md)

**次に読む**

- [どこまで理解を手放してよいか（中核と周辺）](how-much-understanding-to-keep.md)
- [練習と本番の使い分け（AI を禁じる大会に向けた練習を含む）](../contest/practice-vs-contest-day.md)

**関連**

- [生成コードを自分のものにする](../verify/own-generated-code.md)
- [出力スタイルで応答の仕方を切り替える](../cli/output-style-modes.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)
- [引用や出典の確かめ方](../verify/checking-citations.md)
- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](think-before-asking.md)
- [知らないコードベースを読む](../recipes/explore-a-codebase.md)
- [バグを直す](../recipes/fix-a-bug.md)
- 振り返りで AI に評価させない（集計係にとどめる）（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
