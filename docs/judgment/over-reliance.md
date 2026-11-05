---
id: over-reliance
title: 判断を預けすぎる（過度依存）
aliases: [AI に頼りすぎる, 自動化バイアス, over-reliance]
type: judgment
field: judgment
chapter: 落とし穴ごとの対策
order: 20
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない]
pitfalls: [預けすぎる]
scenes: [開発, 調べもの, コンテスト]
summary: 判断まで AI に預けると、もっともらしい誤りをそのまま採ってしまう理由と、どの判断を手元に残し、確かめる手間をどう下げるかが分かる。
signs:
  - {type: symptom, text: もっともらしい答えを、確かめずにそのまま使ってしまう}
  - {type: symptom, text: AI の出力がおかしいと感じても、自分の判断で上書きできない}
  - {type: situation, text: 評価のしかたや方針の選び方まで AI に任せている}
wave: 1
prerequisites: [human-pitfalls]
related: [what-not-to-delegate, evidence-not-reports, verification-ladder, why-hallucinations, learning-with-ai, how-much-understanding-to-keep, agreement-is-not-evidence, independent-review, verifier-defines-problem, is-the-task-ai-suited, fact-checking]
tracks: []
outdated_advice: []
sources: [pmc-vaccaro-2024-human-ai-combinations, mollick-centaurs-cyborgs-jagged, lee-2025-genai-critical-thinking, arxiv-2603-21551, vasconcelos-2023-explanations-overreliance]
volatility: 低
sections:
  - {title: 判断の課題で損が出る, anchor: judgment-tasks}
  - {title: 能力の外の課題で、もっともらしい誤りを採る, anchor: outside-the-frontier}
  - {title: なぜ預けてしまうか, anchor: why-we-hand-over}
  - {title: 手元に残す判断, anchor: what-to-keep}
  - {title: 確かめる手間を下げる, anchor: cheap-verification}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：判断まで AI に預けると、もっともらしい誤りを採ってしまう理由と、手元に残す判断・確かめる手間の下げ方が分かる。
    - **いつ引くか**：Claude の答えを確かめずに使っている、おかしいと感じても自分で上書きできない、評価のしかたや方針の選び方まで任せているときに引く。
    - **前提**：<!-- link:begin human-pitfalls -->[人の側の五つの落とし穴（総論）](human-pitfalls.md)<!-- link:end -->

<!-- textlint-disable -->
別名：AI に頼りすぎる・自動化バイアス・over-reliance
<!-- textlint-enable -->

過度依存は、判断まで AI に預けた結果、AI の誤りを見抜けなくなる落とし穴である。人の側の 5 つの落とし穴のうち「預けすぎる」にあたる。実装は速くなっても、何を良しとして採るかを預けると、速さより先に損が出る。

## 判断の課題で損が出る {#judgment-tasks}

人と AI を組ませた成績は、人だけよりは良い。しかし、人と AI のうち良いほう単独には届かないことが多い（根拠：強）。

Vaccaro ほか（2024）は、2020 年 1 月から 2023 年 6 月までの 74 論文・106 実験を統合したメタ分析である。結果は次のとおり。

- 人＋AI は人単独より良い（g=0.64）。
- 人と AI のうち良いほう単独と比べると、平均で劣る（g=−0.23）。
- 損が大きいのは、判断の課題（g=−0.27）と、AI のほうが強い場面（g=−0.54）である。
- 説明や AI の確信度を画面に出しても、この損は改善しなかった。

読むときの注意が 3 つある。1 つ目は、結果のばらつきが非常に大きい（I²=97.7%）ことで、どの組み合わせでも損が出るわけではない。2 つ目は、測ったのは組み合わせの損で、過度依存はその原因の 1 つとしての解釈であること。3 つ目は、対象が 2023 年前半までの研究で、現行の Claude の傾向を直接測ったものではないことである。

コンテストや開発に当てはめると（類推）、実装は AI の得意な領域だが、「どの評価で良し悪しを決めるか」「どの戦略に賭けるか」は判断の課題である。ここで Claude の出力を上書きできなければ、損が出る。

## 能力の外の課題で、もっともらしい誤りを採る {#outside-the-frontier}

AI が苦手な課題ほど、AI を使った人の判断は悪くなる（根拠：強）。

Dell'Acqua ほか（2023）は、事前登録された実験である。BCG のコンサルタント 758 人が、GPT-4 を使って課題に取り組んだ。AI の能力の外にある課題では、AI を使った人は正しい解を出す確率が 19% 低かった。原因は、もっともらしい誤答をそのまま採ったことだった。

得意な課題では AI が成績を上げ、苦手な課題では下げる。得意と苦手の境目は外から見えにくく、研究者はこれを能力の凸凹と呼ぶ。境目の分からない作業ほど、出力を確かめずに採る損が大きくなると考えられる（推論）。

誤答がもっともらしくなる仕組みは <!-- link:begin why-hallucinations -->[ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)<!-- link:end --> にある。課題が AI に向くかどうかの見積もりは <!-- link:begin is-the-task-ai-suited#five-axes -->[そのタスクは AI に向いているか（五つの軸） › 五つの軸](../delegate/is-the-task-ai-suited.md#five-axes)<!-- link:end --> で見る。

## なぜ預けてしまうか {#why-we-hand-over}

預けてしまうのは、意志が弱いからではなく、確かめる手間と得を、人が無意識に比べているからだと考えられる。

Vasconcelos ほか（2023）は、シミュレーションした AI を使った迷路の課題の実験（5 つの研究、N=731）である。人は AI の説明を読むかどうかを、手間と得を比べて決めており、課題や説明の難しさ、報酬の大きさで過度依存が変わった（根拠：中・類推。LLM ではない模擬の AI と小さな課題）。AI の答えを確かめる手間が大きいままなら、説明を足しても依存は減らない、と著者らは考えている。

知識労働者 319 人の調査では、AI への信頼が高い人ほど、批判的思考の努力が少ないと答える関連があった（β=−0.69。根拠：中。相関と自己報告）。因果は言えない。

CSAW の LLM CTF 部門の分析では、人が主導するトラックの会話の 60% が、答えを求めるだけの「AI 依存型」だった（根拠：中。小標本の分析）。

この 3 つから言えるのは次の見立てである。確かめる手間が大きく、信頼が高いほど、人は確かめない。これは実験の結論ではなく、この辞典の読み方である（推論）。

## 手元に残す判断 {#what-to-keep}

手元に残す判断は、機械的に確かめられないものである。評価の定義、採否、撤退、中核の理解がそれにあたる。一覧と分け方の軸は <!-- link:begin what-not-to-delegate#what-humans-hold -->[任せないもの（評価・採否・撤退・中核の理解） › どの段階でも人が握るもの](../delegate/what-not-to-delegate.md#what-humans-hold)<!-- link:end --> と <!-- link:begin what-not-to-delegate#verifiable-axis -->[任せないもの（評価・採否・撤退・中核の理解） › 分ける軸：機械的に確かめられるか](../delegate/what-not-to-delegate.md#verifiable-axis)<!-- link:end --> が持つ。ここでは、預けてしまう場面での使い方だけを書く。

次の 3 つの問いに、1 つでも「いいえ」と答えるなら、その判断は預けすぎである。

- Claude の答えを、採る前に自分の言葉で説明できるか。説明できないなら <!-- link:begin how-much-understanding-to-keep#explain-or-reject -->[どこまで理解を手放してよいか（中核と周辺） › 説明できないものは採らない](how-much-understanding-to-keep.md#explain-or-reject)<!-- link:end --> に従い、採らない。
- Claude の答えが間違っていたら、どの事実を見れば分かるか。見る先がないなら、確かめようのない判断を預けている。
- Claude の答えに「おかしい」と思ったとき、自分の根拠で上書きできるか。根拠がないなら、評価の軸を自分が持っていない。

!!! example "判断例：解法の方針を Claude に選ばせる"
    - **状況**：コンテストの練習で、問題に 2 通りの解法の候補がある。Claude に聞くと、片方を「標準的で安全」と言って勧めた。
    - **迷う候補**：その勧めに従って実装を任せる。または、自分で小さい入力の手計算をして、方針の当たりをつけてから任せる。
    - **選んだもの**：先に自分で小さい入力を 2 つ作って手で解き、Claude が勧めた方針で同じ入力をたどった結果と突き合わせる。合ってから、実装を任せる。
    - **理由**：実装は任せてよいが、方針の採否は、預けた分だけ誤りを見抜けなくなる判断である。小さい入力の手計算なら、Claude の勧めの当たり外れを少ない手間で確かめられる。

## 確かめる手間を下げる {#cheap-verification}

預けすぎを防ぐ手は、「疑え」と意識することではなく、確かめる手間を小さくして、確かめるのを既定にすることである（Vasconcelos ほかの見立てに沿った推論）。

- **確かめる手段を先に決める**：テストや採点のような検証器を最初に置く。置いた検証器が問題を決めるので、検証器の中身は人が握る（<!-- link:begin verifier-defines-problem#verifier-first -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › 最初の成果物は検証器](../eval/verifier-defines-problem.md#verifier-first)<!-- link:end -->）。
- **証拠で受け取る**：完了の報告ではなく、実行したコマンドと生の出力で受け取る（<!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](../verify/evidence-not-reports.md#what-counts)<!-- link:end -->）。
- **根拠を引用させる**：事実の主張ごとに、渡した資料からの引用を付けさせると、照合の手間が減る（<!-- link:begin fact-checking#quotes -->[事実を確かめる（引用・照合・best-of-N） › 主張ごとに引用させる](../verify/fact-checking.md#quotes)<!-- link:end -->）。
- **任せる幅に合わせて段を選ぶ**：確かめる段の選び方は <!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](../verify/verification-ladder.md#choose-step)<!-- link:end --> にある。
- **書いた本人以外に見せる**：同じ推論を見ていない者にレビューさせる（<!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end -->）。AI 同士の一致は証拠に数えない（<!-- link:begin agreement-is-not-evidence#reviewer-agreement -->[同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](agreement-is-not-evidence.md#reviewer-agreement)<!-- link:end -->）。
- **採否を先に自分で決める**：判断の場面では、Claude の答えを見る前に自分の暫定の答えを書く。見た後に直したかどうかが分かり、そのまま採ったのかも分かる（推論・実践例なし）。

自分の依存は、記録を付けて測る。1 週間ほど、判断の場面ごとに「そのまま採った・直して採った・退けた」を 1 行ずつ残す。退けた記録が 1 件もないなら、確かめていない可能性が高い。やめどきも先に決める。「2 週続けて退けた記録が 0 件なら、検証器か自分の暫定の答えを見直す」と書いておく。この基準は目安で、根拠のある数字ではない（推論・実践例なし）。

効かない場面もある。確かめる手段そのものが誤っていると、確かめるほど安心して預けてしまう。検証器の誤りは <!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](../eval/verifier-defines-problem.md#loops-amplify)<!-- link:end --> にある。理解が残る使い方は <!-- link:begin learning-with-ai -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](learning-with-ai.md)<!-- link:end --> で扱う。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [When combinations of humans and AI are useful: A systematic review and meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC11659167/)：PubMed Central・英語・確認日 2026-11-04
- [Centaurs and Cyborgs on the Jagged Frontier](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged)：Ethan Mollick（One Useful Thing）・英語・確認日 2026-11-04
- [The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers](https://advait.org/files/lee_2025_ai_critical_thinking_survey.pdf)：Advait Sarkar（論文の写し）・英語・確認日 2026-11-04
- [AI In Cybersecurity Education -- Scalable Agentic CTF Design Principles and Educational Outcomes](https://arxiv.org/abs/2603.21551)：arXiv（Xi, Haoran ほか）・英語・確認日 2026-11-04
- [Explanations Can Reduce Overreliance on AI Systems During Decision-Making](https://cicl.stanford.edu/papers/vasconcelos2023explanations.pdf)：Stanford CICL・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [人の側の五つの落とし穴（総論）](human-pitfalls.md)

**次に読む**

- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](learning-with-ai.md)

**関連**

- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [検証の階段](../verify/verification-ladder.md)
- [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)
- [どこまで理解を手放してよいか（中核と周辺）](how-much-understanding-to-keep.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](agreement-is-not-evidence.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [そのタスクは AI に向いているか（五つの軸）](../delegate/is-the-task-ai-suited.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
