---
id: think-before-asking
title: 頼む前に自分で考える（AI には問い・反論・道具を頼む）
nav_title: 頼む前に自分で考える
aliases: [先に自分で考える, AI を問い役にする, 考察の型]
type: judgment
field: judgment
chapter: 落とし穴ごとの対策
order: 70
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [握る, 見せる]
prevents: []
pitfalls: [みんなの案になる, 預けすぎる]
scenes: [開発, 文章, コンテスト]
summary: 独自性が要る考察では先に自分の案と疑問を書き、AI には答えではなく問い・反論・観察の道具を頼む、という順序と使い分けが分かる。
signs:
  - {type: goal, text: AI に答えを聞く前に、自分の考えを固めたい}
  - {type: symptom, text: 最初に AI の案を見ると、それ以外が思いつかなくなる}
  - {type: situation, text: コンテストの考察で、AI をどこまで使うか迷っている}
prerequisites: [ai-ideas-are-everyones]
related: [ask-for-options, ask-without-sycophancy, read-specs-yourself, build-observation-tools, ideate-independently, learning-with-ai, prompt-patterns, long-context-first, format-cheatsheet#heuristic, decide-when-to-quit, competition-rules]
tracks: []
outdated_advice: []
sources: [arxiv-2502-06197, ijcai-2025-creative-momentum, wong-post-think-first-chatgpt-later, arxiv-2410-03703, kellogg-article-comes-creativity-ai-doesnt, arxiv-2403-11164, speakerdeck-terryu16-atcoder-heuristic-first, terry-ahc001]
volatility: 低
sections:
  - {title: 先に自分、その後で AI, anchor: self-first}
  - {title: 答えを選ぶ場面と、発想する場面, anchor: choose-vs-ideate}
  - {title: AI に頼むもの：問い・反論・観察の道具, anchor: questions-rebuttals-tools}
  - {title: 汎用の発想の型に頼りきらない, anchor: generic-frameworks}
  - {title: 考察の五つの問い（コンテストの例）, anchor: five-questions}
  - {title: 人が握るもの, anchor: what-you-keep}
  - {title: 守れたかの確かめ方, anchor: how-to-check}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：独自性が要る考察では先に自分の案と疑問を書き、AI には答えではなく問い・反論・観察の道具を頼む、という順序と使い分けが分かる。
    - **いつ引くか**：AI に答えを聞く前に、自分の考えを固めたいとき。最初に AI の案を見ると、それ以外が思いつかなくなるとき。コンテストの考察で、AI をどこまで使うか迷っているとき。
    - **前提**：<!-- link:begin ai-ideas-are-everyones -->[AI の案は「みんなの案」（均質化）](ai-ideas-are-everyones.md)<!-- link:end -->

<!-- textlint-disable -->
別名：先に自分で考える・AI を問い役にする・考察の型
<!-- textlint-enable -->

頼む前に自分で考えるとは、独自性が要る考察で、先に自分の案と疑問を書き、AI には答えではなく問い・反論・観察の道具を頼む順序のことである。根拠にした研究はどれも創作や発想の課題で、コンテストの考察や業務の分析を対象にした実験は見つからなかった。このページの推奨は、仮説としての推奨（類推）である。

## 先に自分、その後で AI {#self-first}

発想が要る場面では、AI の案を見る前に、自分の案と疑問を書いておく。最初に AI の案を見ると、その案が基準になって、ほかの案が出にくくなるからである。

何が起きるかは、発想課題の研究で測られている。

- 先に 3 案以上を自力で出してから LLM を使った群は、最初から使った群より、自分の案と LLM の案の類似度が低かった（0.648 対 0.899）（根拠：中・類推。LLM を使う文章の発想課題）。
- AI の案を最初に見せるとアンカリング（最初に見た案への固着）が強まった。途中で見せると、方針転換が起きた（根拠：中・類推。AI の提案を使う反復的な発想課題）。
- 大学生 196 人の研究では、「まず自分で考え、その後 ChatGPT で改良・評価する」群が、AI なしの次の課題で最も高い独創性を示した（根拠：弱・類推。著者個人のサイトの紹介ページ経由で、原論文は確かめていない）。

人の側の仕組みは、次のように説明できる（推論。上の結果からの説明で、コンテストでは測られていない）。最初に見た案は、比べる基準になる。基準があると、自分の粗い案は見劣りして、書く前に捨てられる。AI の案を見るのが先だと、この捨てる動きが最初の一歩から働く。同じ AI を使う人たちの案が似通う仕組みは、<!-- link:begin ai-ideas-are-everyones#outputs-converge -->[AI の案は「みんなの案」（均質化） › AI を使った成果どうしは似る](ai-ideas-are-everyones.md#outputs-converge)<!-- link:end --> にある。

先に書くものは、問題や課題の自分の言葉での要約、疑問点、今ある仮説である。コンテストなら、最初の 15〜30 分は AI を使わずに、問題文・スコア式・入力の作られ方・テスター・提出環境を読み、要約と疑問点を書く。時間は目安で、根拠は実践者の経験則である（根拠：弱）。規則で AI を使えない大会があるので、この手順は AI なしで考察する練習にもなる。大会ごとの規則は <!-- link:begin competition-rules -->[大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)<!-- link:end --> で確かめる。

## 答えを選ぶ場面と、発想する場面 {#choose-vs-ideate}

AI への最初の頼みは、場面で変わる。答えを選ぶ場面では選択肢を出させ、発想する場面では先に自分の案を書く。

| 場面 | 先に出すもの | AI に頼むこと |
| --- | --- | --- |
| 答えを選ぶ（作業の進め方、設定の選び方） | 目的と制約 | 選択肢と推奨案と理由 |
| 発想する（独自性に価値がある考察、企画） | 自分の案と疑問 | 問い・反論・観察の道具 |

選ぶ場面の頼み方は <!-- link:begin ask-for-options#choose -->[選択肢と推奨案を出させる › 答えを選ぶ場面：選択肢と推奨案](../prompting/ask-for-options.md#choose)<!-- link:end --> に、発想する場面の頼み方は <!-- link:begin ask-for-options#ideate -->[選択肢と推奨案を出させる › 発想の場面：先に自分の案、AI には問いと反論](../prompting/ask-for-options.md#ideate)<!-- link:end --> にある。分かれ目は、他者との差が結果を決めるかどうかである。差が結果を決めない場面では、AI の案をそのまま使ってよい。この分かれ目は <!-- link:begin ai-ideas-are-everyones#when-difference-matters -->[AI の案は「みんなの案」（均質化） › 差が要る場面と、底上げで足りる場面](ai-ideas-are-everyones.md#when-difference-matters)<!-- link:end --> で整理されている。

!!! example "判断例：最適化コンテストの開始直後に、AI をいつ開くか"
    - **状況**：数時間の最適化コンテストが始まった直後で、問題文を読み終えた。この大会は AI の利用が許されていて、順位は他の参加者との相対で決まる。
    - **迷う候補**：問題文を貼って AI に方針を 3 つ出させ、そこから選ぶ。AI を開く前に決めた時間だけ、自分の言葉で要約と仮説を書く。
    - **選んだもの**：先に要約と疑問を書き、その後で AI に確かめるべき問いを挙げさせる。
    - **理由**：方針を AI から先にもらうと早く動き出せる。ただ、順位を競う場では、他の参加者も同じ方針を得ている前提で考えたい。自分の案を先に書いておけば、AI の案との差と上積みの余地が見える。完走が目的の練習や、時間が極端に短い場面では、最初から AI に方針を出させる選択も筋が通る。

## AI に頼むもの：問い・反論・観察の道具 {#questions-rebuttals-tools}

自分の案を書いた後で AI に頼むのは、答えそのものではなく、3 つの役割である。

- 問い役：解法や方針の名前を出させず、確かめるべき問いを挙げさせる。下の雛形が、その依頼である。
- 反論役：自分のメモの誤った前提と、見落とした条件を指摘させる。好みや確信を伏せて、成果物と基準だけを新しい文脈で見せる聞き方は <!-- link:begin ask-without-sycophancy#fresh-context-critique -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 新しい文脈で、成果物と基準だけを見せる](ask-without-sycophancy.md#fresh-context-critique)<!-- link:end --> にある。批判を強めすぎない加減は <!-- link:begin ask-without-sycophancy#dont-overdo-criticism -->[迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる） › 批判を強めすぎない](ask-without-sycophancy.md#dont-overdo-criticism)<!-- link:end --> にある。
- 道具の作り手：可視化・集計・ログなど、観察のための道具を作らせる。AI を使う中で、最も安全で効果が大きいと見られる使いどころである（根拠：弱。実践者の整理で、効果を測った研究はない）。作らせ方と、出た値の確かめ方は <!-- link:begin build-observation-tools -->観察の道具を作らせる（可視化・集計・ログ）（準備中）<!-- link:end --> にある。

根本的に異なる方針を AI に出させるのは、行き詰まった中盤に限る。序盤から出させると、先に見た方針が基準になるからである。AI の案を途中で見せると方針転換が起きた、という発想課題の研究の結果（根拠：中・類推）が、この使い方の根拠である。

<!-- gen:begin snippet think-before-asking/question-role -->
<!-- textlint-disable -->

??? example "雛形：解法の名前を出させず、確かめるべき問いを原文の引用つきで挙げさせる依頼"

    ```markdown
    次の問題について、解法や方針の名前は出さずに、確かめるべき問いだけを挙げてほしい。
    答え、解法の概略、コードは書かない。

    問いは次の 5 つの観点に分けて挙げる：
    - 仕様の問い（スコアの式、入力の作られ方、テスターの挙動）
    - 理想形の問い（上界、緩和した問題、最適解の形）
    - 制約要因の問い（今の解は何に阻まれているか）
    - 意外性の問い（予想と違った結果は、なぜ違ったか）
    - 前例の問い（過去のどの問題と同じ構造か）

    各問いに、問題文の該当箇所を原文のまま引用して付ける。
    引用できない問いは、問題文にない推測として、その旨を書く。
    観点に当てはまる問いがなければ、ないと書く。無理に作らない。

    --- 問題文（原文のまま） ---
    <ここに、問題文を貼る>

    --- 自分のメモ（あれば） ---
    <ここに、自分で書いた要約・疑問点・考察のメモを貼る。メモにすでにある問いは繰り返さない>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet think-before-asking/question-role -->

問題文は、原文のまま渡す。要約だけを渡すと、AI は要約の誤りに沿って答える。原文と自分の要約を突き合わせて誤読を指摘させる方法は <!-- link:begin read-specs-yourself#misreading-detector -->[仕様を自分で読み、AI に誤読を指摘させる › AI に誤読を指摘させる](../recipes/read-specs-yourself.md#misreading-detector)<!-- link:end --> にある。

例外として、発想を広げたい場面では、自分の言葉で抽象化した構造を渡す手がある。問題文をそのまま渡すと、AI の出力が問題文の言葉を再利用して、発想が固定化しやすいという見方による（根拠：弱・類推）。元の研究は画像生成 AI を使ったデザイン作業を対象にしていて、文章の問題への当てはめは飛躍が大きい。この例外は仮説であり、理解を確かめたい場面では使わない。

## 汎用の発想の型に頼りきらない {#generic-frameworks}

「汎用の発想フレームを AI に出させれば安全」とは考えない。SCAMPER（代用・結合・応用などの観点で案を広げる、汎用の発想の型）のような汎用の発想戦略を示された群は、支援を外した後の独創性がむしろ下がった（根拠：中・類推。発散的思考と収束的思考のランダム化実験）。型に沿って案を出すことに慣れると、型のない場面では出せる案が減りうる、と読める。

型を使うなら、その問題に固有の問いにする。問題の仕様、今の解を阻んでいるもの、予想と違った結果のように、その場の対象に結びつく問いである。「いつもやること」と「その場だからやること」の区別は <!-- link:begin ai-ideas-are-everyones#routine-vs-specific -->[AI の案は「みんなの案」（均質化） › 「いつもやること」と「その場だからやること」](ai-ideas-are-everyones.md#routine-vs-specific)<!-- link:end --> にある。前者は AI に任せやすく、差が出るのは後者である。

ボットに「何を考えるか」ではなく「どう考えるか」を聞くと成績が大きく伸びた、という授業での試行も報じられている。標本の大きさは不明で、逸話として扱う（根拠：弱）。

## 考察の五つの問い（コンテストの例） {#five-questions}

コンテストの考察は、次の 5 つの問いで型にできる。上位者の考察の手順そのものは競技の技術なので、姉妹の教材 kyopro-atlas に任せる。ここでは AI への頼み方に絞る。

| 問い | 確かめること |
| --- | --- |
| 仕様 | スコアの式、入力の作られ方、テスターの挙動 |
| 理想形 | 上界、緩和した問題、最適解の形 |
| 制約要因 | 今の解は何に阻まれているか |
| 意外性 | 予想と違った結果は、なぜ違ったか |
| 前例 | 過去のどの問題と同じ構造か |

最初の 15〜30 分で、この 5 つの観点のメモを自分で書く。その後で AI に、メモにない問いを挙げさせ、メモの誤った前提を指摘させる。確かめるべき問いを挙げさせる依頼の雛形（問い役。上の節にある）は、この 5 つの観点をそのまま使っている。

この型の背景には、観察と実験を回す実践者の整理がある。5 分で書ける単純な解から始め、計画・実装・実行・気づきのサイクルを何回回せるかが鍵だという講義資料がある（根拠：中。複数の実践者の整理が一致している。競技固有）。AtCoder Heuristic Contest 001（AHC001）の解説では、ビジュアライザを改造して各要素のスコアを表示し、「周囲に阻まれて拡大できない」という制約要因を見つけて、新しい操作を加えている（根拠：弱。単独の解説）。制約要因の問いが、観察の道具につながる例である。

最後の 4 つの問いは、業務の問題分析にも使える（推論。業務での実践例は見つかっていない）。形式ごとの AI の効き方と人が握るところは <!-- link:begin format-cheatsheet#heuristic -->コンテストの形式別の早見表（AI の効き方と人が握るところ） › ヒューリスティック（短期・長期）（準備中）<!-- link:end --> にある。

## 人が握るもの {#what-you-keep}

AI に頼んでも手放さないものは、次の 4 つである。

- どの問いを採って、どの仮説を試すか。AI が挙げた問いは候補であり、採るのは自分である。
- 問題の読み。仕様の理解は、原文を自分で読んで書いた要約が土台になる。
- 方針を捨てるかどうか。やめどきを先に決めておく。判断の型は <!-- link:begin decide-when-to-quit -->[やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](decide-when-to-quit.md)<!-- link:end --> にある。
- AI の案を採るときの上積み。他の参加者も同じ案を得ている前提で、差になる部分を自分で考える。

## 守れたかの確かめ方 {#how-to-check}

順序を守れたかは、記録で確かめる。効果の証明ではなく、順序を守ったかの確認である。1 人の少ない回数の結果では、順序が成績に効いたかは分からない。

- AI を開く前のメモを、日時付きで残す。後で AI の案と並べて、AI の案にだけあった観点と、自分のメモにだけあった観点を分ける。案が似ていないかの確かめ方は <!-- link:begin ai-ideas-are-everyones#check -->[AI の案は「みんなの案」（均質化） › 案が似ていないかの確かめ方](ai-ideas-are-everyones.md#check)<!-- link:end --> にある。
- 自力で考える時間の上限を、始める前に決める。時間が来たら、問い役として AI を開く。自力に固執して行き詰まりが長引くのも損である。
- 終わった後に、次の点を振り返る。
    - 最初に開いたのは、AI だったか、自分のメモだったか。
    - AI に頼んだのは、問い・反論・道具だったか、答えだったか。
    - AI の案を採った箇所に、自分の上積みはあったか。

答えを聞いて分かった気になる使い方の問題は <!-- link:begin learning-with-ai#hints-not-answers -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 答えではなくヒントを返させる](learning-with-ai.md#hints-not-answers)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Timing Matters: How Using LLMs at Different Timings Influences Writers' Perceptions and Ideation Outcomes in AI-Assisted Ideation](https://arxiv.org/abs/2502.06197)：arXiv（Qin, Peinuan ほか）・英語・確認日 2026-11-04
- [Creative Momentum Transfer: How Timing and Labeling of AI Suggestions Shape Iterative Human Ideation | IJCAI](https://ijcai.org/proceedings/2025/1142)：IJCAI・英語・確認日 2026-11-04
- [Think First, ChatGPT Later (Wong & Qiu, 2026, Educational Psychology Review)](https://www.sarahshihuiwong.com/post/think-first-chatgpt-later-wong-qiu-2026-educational-psychology-review)：Sarah Shi Hui Wong・英語・確認日 2026-11-04
- [Human Creativity in the Age of LLMs: Randomized Experiments on Divergent and Convergent Thinking](https://arxiv.org/abs/2410.03703)：arXiv（Kumar, Harsh ほか）・英語・確認日 2026-11-04
- [When It Comes to Creativity, AI Doesn’t Always Have the Answer](https://insight.kellogg.northwestern.edu/article/when-it-comes-to-creativity-ai-doesnt-always-have-the-answer)：Kellogg Insight・英語・確認日 2026-11-04
- [The Effects of Generative AI on Design Fixation and Divergent Thinking](https://arxiv.org/abs/2403.11164)：arXiv（Wadinambiarachchi, Samangi ほか）・英語・確認日 2026-11-04
- [AtCoder Heuristic First-step Vol.1 講義スライド](https://speakerdeck.com/terryu16/atcoder-heuristic-first-step-vol-dot-1-jiang-yi-suraido)：Speaker Deck（terryu16）・確認日 2026-11-04
- [AtCoder Heuristic Contest 001 (AHC001) 初心者向け解説](https://blog.terry-u16.net/entry/ahc001-how-to)：TERRY（terry\_u16）・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [AI の案は「みんなの案」（均質化）](ai-ideas-are-everyones.md)

**次に読む**

- 観察の道具を作らせる（可視化・集計・ログ）（準備中）

**関連**

- [選択肢と推奨案を出させる](../prompting/ask-for-options.md)
- [迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）](ask-without-sycophancy.md)
- [仕様を自分で読み、AI に誤読を指摘させる](../recipes/read-specs-yourself.md)
- 案出しは独立に、突き合わせは AI に（準備中）
- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](learning-with-ai.md)
- 用途別プロンプトの型（準備中）
- [長い資料は先、質問は最後](../prompting/long-context-first.md)
- コンテストの形式別の早見表（AI の効き方と人が握るところ） › ヒューリスティック（短期・長期）（準備中）
- [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](decide-when-to-quit.md)
- [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
