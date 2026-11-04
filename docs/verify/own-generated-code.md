---
id: own-generated-code
title: 生成コードを自分のものにする
aliases: [AI が書いたコードの理解]
type: recipe
field: verify
chapter: レビューで確かめる
order: 140
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, 学習, コンテスト]
summary: 生成されたコードを採る前に、Claude に処理の流れと入力の端を説明させ、実際の動きと照らし、自分の言葉で言い直して理解を確かめられる。言い直せない所が、読み直す箇所になる。
signs:
  - {type: goal, text: 生成されたコードを理解したうえで採りたい}
  - {type: goal, text: マージする前に、生成されたコードのどこが分かっていないかを洗い出したい}
  - {type: situation, text: 大事な処理を書き換えたコードを、Claude から受け取った}
prerequisites: [how-much-understanding-to-keep]
related: [learning-with-ai, diffs-humans-must-read, evidence-not-reports, unfaithful-reasoning, explore-a-codebase, independent-review, over-reliance, looks-are-not-quality, create-and-review-prs, review-bottlenecks, experiment-log]
tracks: []
outdated_advice: []
sources: [anthropic-research-ai-assistance-coding-skills, rustc-dev-guide-llm-guidance-reviewing]
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 処理の流れと入力の端を説明させる, anchor: explain}
  - {title: 説明を実際の動きと照らす, anchor: check-explanation}
  - {title: 自分の言葉で言い直してから採る, anchor: gate}
  - {title: 理解できたかの確かめ方, anchor: overall-check}
  - {title: うまくいかないとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：Claude に処理の流れと入力の端を説明させ、実際の動きと照らし、自分の言葉で言い直してから採れる。
    - **いつ引くか**：大事な処理を書き換えたコードを Claude から受け取り、理解したうえで採りたいとき。マージ前に、どこが分かっていないかを洗い出したいとき。
    - **前提**：<!-- link:begin how-much-understanding-to-keep -->[どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)<!-- link:end -->

<!-- textlint-disable -->
別名：AI が書いたコードの理解
<!-- textlint-enable -->

生成コードを自分のものにするとは、Claude が書いたコードを、説明・実行・言い直しの 3 段で確かめてから採ることである。3 段を通った変更は採る。通らなかった所は、読み直す箇所として残る。どの変更にこの手順を当てるかは、中核と周辺の線引きで決まる。線引きは <!-- link:begin how-much-understanding-to-keep#core-and-periphery -->[どこまで理解を手放してよいか（中核と周辺） › 中核と周辺を分ける](../judgment/how-much-understanding-to-keep.md#core-and-periphery)<!-- link:end --> にある。

## 先に整える守り {#guards}

手順を始める前に、次の 4 つを整える。理解を確かめる手順は、Claude の説明を材料にする。材料がずれていても気づけない状態で始めると、確かめたつもりだけが残る。

- **当てる範囲を決める**。すべての変更にこの手順を当てると、確かめる側が詰まる。中核の変更に当て、周辺は任せる。詰まり方と流す量の決め方は <!-- link:begin review-bottlenecks#match-review-capacity -->[レビューのボトルネックと疲労 › 流す量をレビューに合わせる](../team/review-bottlenecks.md#match-review-capacity)<!-- link:end --> にある。
- **差分を自分でも開く**。説明だけを材料にしない。赤信号になる箇所は <!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](diffs-humans-must-read.md#red-flags)<!-- link:end --> で先に拾う。
- **実行できる環境を用意する**。入力を流せるテストランナーか実行コマンドが、作業ツリーの中で動くようにしておく。次の「照らす」段に要る。
- **この手順を独立したレビューの代わりにしない**。書いた本人の説明を聞く手順であり、変更を生んだ推論を見ていない者の目ではない。重い変更には <!-- link:begin independent-review#what-happens -->[書いた本人ではない者にレビューさせる › 同じ会話で確かめさせると何が起きるか](independent-review.md#what-happens)<!-- link:end --> を別に回す。

## 処理の流れと入力の端を説明させる {#explain}

最初の段は、採る前の変更について、Claude に処理の流れと入力の端を説明させる段である。要約ではなく、次の 4 つを出させる。

1. 入力から出力までの処理の流れ。分岐とループには、入る条件を添えさせる。流れが複雑なら、図で出させる。図は流れの抜けを見つけやすくするための手段で、必須ではない。
2. 想定する入力の端。端ごとに、コードのどの行がどう扱うかを行番号つきで出させる。
3. 説明のうち、コードを読んで確かめたことと、書いた意図から推測したことの区別。
4. 自分で試せる入力と、期待する出力。

<!-- gen:begin snippet own-generated-code/explain-before-adopting -->
<!-- textlint-disable -->

??? example "雛形：中核の変更を採る前に理解を確かめる依頼"

    ```markdown
    次の変更を、マージする前に自分が理解するために説明してほしい。コードは直さないこと。

    対象：<ファイルや関数。差分なら `git diff` の範囲>

    1. 処理の流れを、入力から出力まで順に説明する。分岐とループには、どの条件で入るかを添える。流れが複雑なら Mermaid の図で出す。
    2. この処理が想定している入力の端を挙げる。空、1 件だけ、上限ぎりぎり、範囲外、型が違う、重複、順序が逆のうち、この処理に関わるものを選ぶ。それぞれ、コードのどの行がどう扱うかを行番号つきで書く。
    3. 説明のうち、コードを読んで確かめたことと、書いた意図から推測したことを分けて書く。
    4. 私が自分で確かめられる入力を、期待する出力つきでいくつか挙げる。

    「なぜこう書いたか」ではなく、「このコードが何をするか」を説明すること。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet own-generated-code/explain-before-adopting -->

聞くのは「このコードが何をするか」にする。「なぜこう書いたか」への答えは、書いたときの計算をそのまま写したものとは限らない。理由は読み物として受け取り、理解の根拠にしない。理由が理解の根拠にならない仕組みは <!-- link:begin unfaithful-reasoning -->[表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)<!-- link:end --> にある。

この段が終わった印は、次の 3 つがそろうことである。

- 流れの各分岐に、入る条件が書かれている。
- 入力の端ごとに、行番号つきの扱いが書かれている。
- 読んでも分からない語と、飛ばされた分岐に、自分で印を付けた。

## 説明を実際の動きと照らす {#check-explanation}

説明を実際の動きと照らす段では、Claude の説明が実際の処理と合っているかを、実行で確かめる。説明が筋の通った文章になっていることと、コードがその通りに動くことは別である。説明と実際が食い違うときは、実行して見た事実を正とする（<!-- link:begin evidence-not-reports#facts-win -->[報告ではなく証拠を求める › 説明と事実が食い違ったら](evidence-not-reports.md#facts-win)<!-- link:end -->）。

手順は次のとおり。

1. 実行する前に、入力の端それぞれの出力を、自分で予想して書く。予想の外れた箇所は、分かっていない所である。
2. 説明に挙がった入力の端を、実際に流す。コマンドと生の出力を残させる。証拠の形は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](evidence-not-reports.md#what-counts)<!-- link:end --> にある。
3. 説明と出力が違った項目は、説明を直させる前に、コードを行で追って違いの原因を自分で探す。追い方は <!-- link:begin explore-a-codebase#check-against-code -->[知らないコードベースを読む › 説明をコードで確かめる](../recipes/explore-a-codebase.md#check-against-code)<!-- link:end --> と同じである。

<!-- gen:begin snippet own-generated-code/run-the-edges -->
<!-- textlint-disable -->

??? example "雛形：説明の入力の端を実行で照らす依頼"

    ```markdown
    さっきの説明の「入力の端」の各項目を、実際に実行して確かめてほしい。

    - 項目ごとに、実行したコマンドと生の出力をそのまま貼る。
    - 説明と出力が違った項目は、説明を直さずに、違いをそのまま報告する。
    - 実行できなかった項目は、理由を添えて「未実行」と書く。
    - 既存のコードとテストは変更しない。確認用のスクリプトは作業用の場所に置く。
    - 最後に、実行した項目の数と、説明が合っていた項目の数を書く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet own-generated-code/run-the-edges -->

テストが通ること、README が整っていること、説明が滑らかなことは、理解の証拠にならない。見た目で判断しない理由は <!-- link:begin looks-are-not-quality -->[見た目は品質の証拠ではない](looks-are-not-quality.md)<!-- link:end --> にある。

!!! example "判断例：テストが通っている変更を実行で照らすか"
    - **状況**：区間の重複を数える関数を書き換えたコードを、Claude から受け取った。説明は筋が通っていて、既存のテストも全部通っている。
    - **迷う候補**：既存のテストが端の入力を含んでいるので、追加の実行を省く。または、説明に挙がった入力の端を、自分で流して照らす。
    - **選んだもの**：既存のテストが端の入力を含むかを自分で確かめ、含まない端だけを流して照らす。
    - **理由**：テストの件数が変わっても「全部通過」と返ってくることがあり、通過は端を見た証拠とは限らない（<!-- link:begin evidence-not-reports#what-happens -->[報告ではなく証拠を求める › 件数が変わっても「全部通過」と返ってくる](evidence-not-reports.md#what-happens)<!-- link:end -->）。一方、端をすべて流し直すと手間が膨らむ。テストが覆う端は任せ、覆わない端だけを手元で確かめる。

## 自分の言葉で言い直してから採る {#gate}

最後の段は、Claude の説明を見ずに、処理の流れと入力の端の扱いを自分の言葉で書き直す段である。この段が採るかどうかのゲートになる。

- **自分で書く**。言い直しを Claude に書かせない。書かせると、確かめる対象が自分の理解から Claude の文章に変わる。
- **短く書く**。チームメイトに伝えられる長さにする。「3 行で」のような行数の目安は出典のない経験則なので、行数は決めない。
- **言い直せない所に印を付ける**。そこが読み直す箇所になる。該当の行だけを Claude に質問し、答えを読んだらもう一度、見ずに言い直す。
- **言い直せるまで採らない**。中核の変更は、言い直せるまでマージしない。この出荷の基準の置き方は <!-- link:begin how-much-understanding-to-keep#explain-or-reject -->[どこまで理解を手放してよいか（中核と周辺） › 説明できないものは採らない](../judgment/how-much-understanding-to-keep.md#explain-or-reject)<!-- link:end --> にある。確かめる手間を惜しんで説明を読んだだけで採る流れは、<!-- link:begin over-reliance -->[判断を預けすぎる（過度依存）](../judgment/over-reliance.md)<!-- link:end --> の落とし穴にあたる。

言い直した文は、PR の説明にそのまま使える。書き方は <!-- link:begin create-and-review-prs#pr-description -->PR を作り、レビューを受ける › PR の説明に書くこと（準備中）<!-- link:end --> にある。

この考え方は、実在の組織の規約にもある。Rust コンパイラの開発ガイドは、LLM が生成したコードを含む変更について、作者に自分の言葉での説明、バグの再現、エッジケースの列挙を求めるよう、レビュアーに指示している（2026-11-04 に確認。ガイドの版で変わりうる）。

実験や設定の改善にも当てはまる。「この改善はなぜ効いたのか」を説明できない採用は、保留にする。仮説を先に書く記録は <!-- link:begin experiment-log#hypothesis-first -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 仮説を先に書く](../eval/experiment-log.md#hypothesis-first)<!-- link:end --> にある。

## 理解できたかの確かめ方 {#overall-check}

3 段を終えたあとで、理解が残ったかを次の 3 つで確かめる。

- 新しい入力を 1 つ渡されて、実行する前に出力を当てられるか。
- 条件を 1 つ変える小さな変更を、自分の言葉で指示でき、結果を予想できるか。
- 後日その箇所を開いたとき、説明を見ずに流れを追えるか。

言い直せなかった箇所と、そこを採ったか保留にしたかを、記録に残す。同じ種類の箇所で言い直せないことが続くなら、その種類は Claude に任せる範囲から外すか、小さく分けて作らせる。理解が残ったかの確かめ方は、学習の文脈では <!-- link:begin learning-with-ai#how-to-check -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 理解が残ったかの確かめ方](../judgment/learning-with-ai.md#how-to-check)<!-- link:end --> にもある。

この手順で確かめられるのは、自分が理解したことである。コードが正しいことは確かめられない。正しさは、テストと実行の証拠、独立したレビューで確かめる。

## うまくいかないとき {#when-it-fails}

- **言い直せない**：言い直せない行を指して、Claude に質問する。それでも言い直せないなら、採らない。変更を小さく分けて作り直させる。
- **説明が実行と食い違う**：説明を捨て、実行の出力からコードを読み直す。1 か所の食い違いは、ほかの箇所の説明もずれている疑いになる。
- **同じ質問の説明が、聞くたびに変わる**：説明を理解の材料にしない。コードそのものを読む。
- **手順に時間がかかりすぎる**：当てる範囲が広すぎる。中核に絞り、周辺は任せる。範囲の決め方は、前提の <!-- link:begin how-much-understanding-to-keep -->[どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)<!-- link:end --> にある。
- **学習が目的なのに、デバッグまで Claude に任せている**：学習目的なら、デバッグは自分で行う。Anthropic の研究（2026 年）は、Python の Trio を学ぶ課題で、課題の直後のクイズが AI 群 50%、手書きの対照群 67% だったと報告した。参加者は 52 人で、AI 群のアシスタントは GPT-4o ベースである（根拠：中）。最も低かった類型は、AI に直させて検証もさせる反復デバッグだった。ただし類型は各 4 人ほどで、類型と結果の因果は主張されていない。また結果は課題の直後のもので、Claude Code のようなエージェントとは設定が違う。学習の使い方は <!-- link:begin learning-with-ai#patterns -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 理解が残る使い方・残らない使い方](../judgment/learning-with-ai.md#patterns)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How AI assistance impacts the formation of coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)：Anthropic・英語・確認日 2026-11-04
- [Reviewing code with LLMs](https://rustc-dev-guide.rust-lang.org/llm-guidance/reviewing.html)：Rust Project（rustc-dev-guide）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)

**次に読む**

- PR を作り、レビューを受ける（準備中）

**関連**

- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- [人間が読むべき差分の箇所](diffs-humans-must-read.md)
- [報告ではなく証拠を求める](evidence-not-reports.md)
- [表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)
- [知らないコードベースを読む](../recipes/explore-a-codebase.md)
- [書いた本人ではない者にレビューさせる](independent-review.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- [見た目は品質の証拠ではない](looks-are-not-quality.md)
- [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
