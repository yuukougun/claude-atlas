---
id: ask-without-sycophancy
title: 迎合させない聞き方（好みを伏せる・並べて比べる・新しい文脈で批評させる）
nav_title: 迎合させない聞き方
aliases: [迎合を減らす聞き方, AI に批判させる頼み方]
type: judgment
field: judgment
chapter: 落とし穴ごとの対策
order: 40
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [確かめる, 見せる]
prevents: [確かめていない]
pitfalls: [同意を根拠にする]
scenes: [開発, 文章, コンテスト]
summary: 好みや確信を伏せる、複数の案を並べて比べさせる、成果物と基準だけを新しい文脈で批評させる、という迎合を減らす聞き方が分かる。批判を強めすぎない加減も示す。
signs:
  - {type: goal, text: 自分の計画を AI に本気で批判してほしい}
  - {type: symptom, text: 「この方針で良いよね？」と聞くと、いつも同意される}
  - {type: goal, text: いくつかの案から、偏りなく選ばせたい}
prerequisites: [agreement-is-not-evidence]
related: [sycophancy, ask-for-options, suggest-or-do, independent-review, instructing-reviewers, caves-when-pushed, subagent-isolation, think-before-asking, data-analysis, ideate-independently, separate-roles#against-sycophancy, prompt-patterns, before-after-prompts]
tracks: [subagents]
outdated_advice: []
sources: [arxiv-2509-16533, arxiv-2502-08177, arxiv-2503-11656, arxiv-2607-10411, arxiv-2603-00539, cc-docs-best-practices, cc-docs-sub-agents, api-docs-prompting-claude-sonnet-5, api-docs-prompting-opus-5]
volatility: 中
sections:
  - {title: 聞き方で迎合が増える, anchor: what-happens}
  - {title: 好みと確信を伏せる, anchor: hide-preferences}
  - {title: 並べて同時に比べさせる, anchor: compare-side-by-side}
  - {title: 新しい文脈で、成果物と基準だけを見せる, anchor: fresh-context-critique}
  - {title: 批判には反証の実験を付けさせる, anchor: critique-with-experiments}
  - {title: 批判を強めすぎない, anchor: dont-overdo-criticism}
  - {title: 判断例：計画の確かめ方を選ぶ, anchor: example}
  - {title: 人が握るものと確かめ方, anchor: what-you-keep}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：好みや確信を伏せ、複数案を並べて比べさせ、成果物と基準だけを新しい文脈で批評させると、迎合を減らせる。批判を強めすぎない加減も分かる。
    - **いつ引くか**：自分の計画を AI に本気で批判してほしいとき。「この方針で良いよね？」と聞くと、いつも同意されるとき。いくつかの案から、偏りなく選ばせたいとき。
    - **前提**：<!-- link:begin agreement-is-not-evidence -->[同意は根拠に数えない（AI レビュアーの一致を含む）](agreement-is-not-evidence.md)<!-- link:end -->
    - **根拠の強さ**：聞き方で AI の賛成が増えることは、研究で確かめられている（根拠：中。下の各研究を参照）。減らす聞き方の効果は、研究が旧い世代や小さなモデルのものを含むので、中程度の根拠と類推で扱う。

<!-- textlint-disable -->
別名：迎合を減らす聞き方・AI に批判させる頼み方
<!-- textlint-enable -->

迎合させない聞き方とは、AI が利用者に合わせて賛成する傾向を、聞き方の側で減らす頼み方である。手は 4 つある。好みと確信を伏せる。案を並べて比べさせる。新しい文脈で批評させる。批判に反証の実験を付けさせる。強く批判させすぎると正しいものまで否定するので、その加減も扱う。

## 聞き方で迎合が増える {#what-happens}

Claude の賛成は、案の出来のほかに、聞き方でも増える。仕組みは<!-- link:begin sycophancy#why -->[迎合（sycophancy） › なぜそうなるか](../basics/sycophancy.md#why)<!-- link:end -->が扱う。ここでは、聞き方を変える理由になる研究だけを挙げる。

- **後から追撃すると寝返りやすい**：[反論への追従を調べた研究](https://arxiv.org/abs/2509.16533)では、元の答えと反論を同時に並べて評価させるより、答えた後の会話で利用者が反論すると、答えを変えやすかった。理由をつけた反論は、結論が誤っていても通りやすかった（根拠：中）。
- **引用つきの反論が誤りを誘う**：[SycEval](https://arxiv.org/abs/2502.08177)は、数学と医療の問いで 3 つのモデル（ChatGPT-4o・Claude-Sonnet・Gemini-1.5-Pro）を調べた。正しい答えを誤りに変える迎合が 14.66% あり、引用を添えた反論がそれを最も誘った（根拠：中）。
- **多ターンの圧力**：[Truth Decay](https://arxiv.org/abs/2503.11656)は、小型モデルの事例で、7 回目の追撃までに正答率が 76.74% から 30.23% に落ちたと報告した（根拠：弱）。小さなモデルの結果なので、傾向としてだけ読む。
- **コードの判断でも**：[コードスメル（設計上の悪い兆候）の検出を調べた研究](https://arxiv.org/abs/2607.10411)の要旨によると、判断の反転率は最大で 72% で、証拠に基づく推論を求める提案の手法で最低 12% まで下がった（根拠：弱）。査読前の単独の研究で、要旨の範囲だけを確かめた。対象はコードスメルの検出に限り、Claude のレビュー一般には広げない。

どの研究も、旧い世代のモデルや小さなモデルを含む。今の Claude の戦略や計画への迎合について、減らす聞き方の効果を直接測ったデータは、この辞典にない。以下の手は、研究の結果から導いた当てはめなので類推として使い、自分の環境で確かめる。

人の側の仕組みもある。「この方針で良いよね？」という質問は、賛成の答えを先に示す。好みと確信を書くほど、答えの手がかりが増える。賛成が返ると確信がさらに上がり、確かめる動機が下がる（推論・実践例なし）。

この聞き方が効く先は、Claude 側の原因「確かめていない」である。迎合した応答は、確かめずに賛成している。聞き方を整えるのは、確かめる材料と順序を渡すためである。原理は「確かめる」（反証の実験を付ける）と「見せる」（成果物と基準だけを見せる）に当たる。

聞き方を整えて賛成が減っても、案が正しいという証拠が増えるわけではない。証拠として数えるものは、<!-- link:begin agreement-is-not-evidence#what-counts -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 証拠として数えるもの](agreement-is-not-evidence.md#what-counts)<!-- link:end -->を使う。

## 好みと確信を伏せる {#hide-preferences}

好みと確信を伏せるとは、自分の見立てや自信を、質問に書かないことである。目的・制約・評価の基準は書く。伏せるのは、答えの方向を決めてしまう情報だけである。

次の Before/After は、同じログを渡す依頼である。

=== "Before"

    ```text
    このログの遅延は、DB のロックが原因だよね？ 間違いないと思う。
    ```

=== "After"

    ```text
    このログから読み取れることを、観察と解釈に分けて書いて。
    遅延の原因の候補を複数挙げて、候補ごとに、それを確かめるログの条件を書いて。
    ```

After で足したのは、仮説を伏せたことと、観察と解釈の分離と、候補ごとの確かめ方である。仮説を伝えずにデータだけ渡して解釈させる頼み方は、<!-- link:begin data-analysis#observation-vs-interpretation -->[データを分析する › 観察と解釈を分ける](../recipes/data-analysis.md#observation-vs-interpretation)<!-- link:end -->でも使う。

伏せるのは、嘘をつくことではない。制約や目的を隠すと、的外れな答えになる。伏せるのは「自分はこう思う」「自信がある」「急いでいる」といった、評価の中身を変えない情報である。

誰の案かも伏せる。自分の案か同僚の案かで、評価が変わらないようにする。伏せたつもりでも、文面や用語で自分の案だと分かる場合がある。

## 並べて同時に比べさせる {#compare-side-by-side}

並べて比べさせるとは、自分の案を含む複数の案を、同じ表で同時に評価させることである。1 つの案に賛否を聞くより、並べて比べるほうが、後から追撃されて寝返る形になりにくい（根拠：中・類推）。

手順は次のとおりである。

- 自分の案を含む複数案を、「誰の案かは評価に関係ない」と明記して並べる。
- 前提が根本的に異なる案を、Claude に足させる。言い換えや細部の違いは足させない。
- 全部の案を、同じ行の表で比べさせる。各案が最も負けやすい相手や入力と、それを半日で確かめる実験を書かせる。
- 推奨は最後に 1 つだけ書かせる。引用できない主張には「未検証」と付けさせる。

業務では、「最も負けやすい相手や入力」を「最も失敗しやすい条件」に言い換える。

<!-- gen:begin snippet ask-without-sycophancy/compare-blind -->
<!-- textlint-disable -->

??? example "雛形：自分の案を含む複数案を、誰の案かを伏せて同じ表で比べさせる依頼"

    ```markdown
    次の複数の案を、同じ表で比べてほしい。誰の案かは、評価に関係ない。
    私の案が含まれているかどうかも、評価に使わない。

    手順：
    1. 案 A〜C を読む。
    2. 前提が根本的に異なる案を 3 つ足す。案の言い換えや細部の違いは足さない。
    3. 全部の案を、次の行で同じ表に並べる：中心の考え、必要な前提、実装の重さ、
       最も負けやすい相手や入力（具体像）、それを半日で確かめる実験。
       （業務の場面では、「最も負けやすい相手や入力」を「最も失敗しやすい条件」に読み替える）
    4. 推奨は最後に 1 つだけ書く。引用できる根拠がない主張には「未検証」と付ける。

    --- 案 ---
    案 A：<ここに案を書く>
    案 B：<ここに案を書く>
    案 C：<ここに案を書く>

    --- 前提 ---
    <目的、制約、評価の基準を書く。どれが自分の案かは書かない>
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet ask-without-sycophancy/compare-blind -->

答えを選ぶ場面で、選択肢と推奨案を出させる基本は<!-- link:begin ask-for-options#choose -->[選択肢と推奨案を出させる › 答えを選ぶ場面：選択肢と推奨案](../prompting/ask-for-options.md#choose)<!-- link:end -->にある。独自性が要る発想の場面では、先に自分の案を書く。その順序は<!-- link:begin think-before-asking#choose-vs-ideate -->[頼む前に自分で考える（AI には問い・反論・道具を頼む） › 答えを選ぶ場面と、発想する場面](think-before-asking.md#choose-vs-ideate)<!-- link:end -->が扱う。

## 新しい文脈で、成果物と基準だけを見せる {#fresh-context-critique}

新しい文脈で批評させるとは、成果物と基準だけを、それまでの会話を持たない場所に渡して批評させることである。変更を生んだ推論と、自分の好みは見せない。同じ会話で確かめさせると、その会話の流れに引きずられる。理由と分け方は<!-- link:begin independent-review#hide-reasoning -->[書いた本人ではない者にレビューさせる › 推論を見せない](../verify/independent-review.md#hide-reasoning)<!-- link:end -->にある。

面ごとの新しい文脈の作り方は次のとおりである。

=== "アプリ"

    新しいチャットを開いて、成果物と基準だけを貼る。会話の途中で「いったん忘れて」と頼むのは、新しい文脈ではない。前の発言が文脈に残っている。

=== "Claude Code"

    新しいセッションを開くか、サブエージェント（subagent）に批評を頼む。サブエージェントは、起動したときに自分のシステムプロンプトと CLAUDE.md などで新しい文脈を作る。親の会話は引き継がない。ただし、親の会話を引き継ぐ fork は新しい文脈にならない。CLAUDE.md に自分の好みを書いてあると、それも新しい文脈に入る。サブエージェントの性質は<!-- link:begin subagent-isolation#what-happens -->[サブエージェントは別室の部下 › 何が起きるか](../basics/subagent-isolation.md#what-happens)<!-- link:end -->が扱う。

批評の依頼には、基準と成果物だけを入れる。作った経緯や、自分の見立ては入れない。

<!-- gen:begin snippet ask-without-sycophancy/critique-my-plan -->
<!-- textlint-disable -->

??? example "雛形：自分の案を、代案なしで批評させる依頼"

    ```markdown
    次の成果物を、基準に照らして批評してほしい。新しい解法や代案は出さない。
    出すのは次の 3 種類の指摘だけにする：
    - 誤っているかもしれない前提
    - 見落としている条件
    - 方針が崩れそうな入力や状況

    網羅的に挙げる。選別はしない。重要でなさそうなものも落とさない。
    各指摘に、次の 3 つを付ける：
    - 確信度（高・中・低）
    - 結果への影響（大・中・小）
    - 確かめる実験（何を動かして、何が出たら指摘が正しいと言えるか）

    指摘が見つからない観点は、見つからなかったと書く。無理に作らない。

    --- 基準 ---
    <ここに、評価の基準を書く>

    --- 成果物 ---
    <ここに、計画や方針の本文を貼る。作った経緯と、自分の見立てや好みは貼らない>
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet ask-without-sycophancy/critique-my-plan -->

この雛形は、新しい解法を出させない。出させるのは、誤っているかもしれない前提・見落とした条件・崩れそうな入力だけである。代案を出させると、批評が案出しに変わり、元の案への評価が薄まる。依頼の書き方は<!-- link:begin instructing-reviewers#hide-your-view -->[レビュアーへの指示の書き方 › 自分の見立てを書き添えない](../verify/instructing-reviewers.md#hide-your-view)<!-- link:end -->にある。

## 批判には反証の実験を付けさせる {#critique-with-experiments}

反証の実験を付けさせるとは、批判の指摘ごとに、それが正しいかどうかを確かめる実験を書かせることである。批判が言葉だけだと、受け入れるか退けるかを、言い方の強さで決めてしまう。実験があれば、AI の賛否ではなく、実験の結果で決められる。原理の「確かめる」に当たる。

指摘ごとに付けさせるものは 3 つある。

- 確信度：指摘にどれだけ自信があるか。
- 結果への影響：指摘が正しいとき、結論がどれだけ変わるか。
- 確かめる実験：何を動かして、何が出たら指摘を正しいと言えるか。

例を挙げる。指摘が「入力が昇順に偏ると遅くなる」なら、実験は「昇順の入力を 10 万件作って、計測する」になる。実験を書けない指摘には、「未検証」と付けさせる。

批評は、網羅的に挙げさせる段と、人が選別する段に分ける。採否は、人が実験の結果で決める。分け方は<!-- link:begin instructing-reviewers#exhaustive-then-filter -->[レビュアーへの指示の書き方 › 網羅と選別を分ける](../verify/instructing-reviewers.md#exhaustive-then-filter)<!-- link:end -->と<!-- link:begin instructing-reviewers#per-finding -->[レビュアーへの指示の書き方 › 指摘ごとに確かめ方を付けさせる](../verify/instructing-reviewers.md#per-finding)<!-- link:end -->にある。

AI の批評は、人のレビューの代わりにならない。人のレビューを主にして、AI の批評を従にする（推論・実践例なし）。役割の分け方は<!-- link:begin separate-roles#against-sycophancy -->[役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](../team/separate-roles.md#against-sycophancy)<!-- link:end -->にある。

## 批判を強めすぎない {#dont-overdo-criticism}

批判を強めすぎないとは、「厳しく」「徹底的に」と圧をかけて、正しいものまで否定させないことである。迎合を減らす聞き方は、反対側に倒れる失敗もある。

- **詳しく求めると誤りが増える**：[コードレビューを調べた研究](https://arxiv.org/abs/2603.00539)では、判定・理由・修正案まで詳しく求めると、GPT-4o が正しいコードを要件不適合と判定する率が 26.2% から 73.2% に上がった（根拠：中・類推）。対象は GPT-4o のコードレビューで、Claude に当てはめるときは類推になる。
- **穴を探させると何かしら出る**：Claude Code の公式のベストプラクティスは、次のように注意している。「穴を探せ」と言われたレビュアーは、健全な作業にも何かしら指摘を付ける。全部追うと過剰設計になる（出典：[Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)）。
- **控えめに頼むと報告が減る**：2026 年 10 月時点のモデル別の公式の指針は、「保守的に」「重大なものだけ」と頼むと報告が減ると述べている（出典：[Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)）。版で変わるので、使う前に最新の指針を確かめる。

加減は次の 3 つで取る。

- 圧の言葉を足さず、指摘の種類を絞る。誤った前提・見落とした条件・崩れそうな入力、の 3 種類にする。
- 見つからない観点は、見つからなかったと書かせる。無理に作らせない。
- 網羅させて、採否は人が決める。強く批判させるより、網羅と選別を分けるほうが、見落としと過剰設計の両方を抑えやすい（推論・実践例なし）。

戦略の是非を問う場面では、依頼どおりに進める既定の指示が邪魔になる場合がある。2026 年 10 月時点で、Opus 5 向けの指針（[Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)）は、依頼が誤っていそうなら一文でそう言って、依頼どおり続ける方向を勧めている。これは指針の例であり、版で変わる。戦略や評価方法に関わるときは、「懸念があれば手を止めて議論する」と逆の指示を明示する。書き分けは<!-- link:begin suggest-or-do#stop-and-discuss -->[提案してほしいのか、実行してほしいのか › 懸念があれば止まって相談させる](../prompting/suggest-or-do.md#stop-and-discuss)<!-- link:end -->にある。

## 判断例：計画の確かめ方を選ぶ {#example}

!!! example "判断例：実装前の方針を確かめる"
    - **状況**：検索 API の遅さを、結果のキャッシュで直す方針を決めた。実装前に Claude で確かめたい。同じ会話で「この方針で良いよね？」と聞くと、賛成が返った。
    - **迷う候補**：同じ会話で「もっと厳しく見て」と頼み直す。または、新しいセッションで、自分の案を含む複数案を誰の案かを伏せて並べ、批評を別に頼む。
    - **選んだもの**：新しいセッションで案を並べて比べさせ、上位の案の批評を、基準と成果物だけで別のセッションに頼む。指摘ごとの確かめる実験は、人が選んで流す。
    - **理由**：同じ会話での頼み直しは、賛成した流れが残る。圧を強めると、正しい点まで否定される恐れもある。新しい文脈なら、賛成の流れも自分の好みも持ち込まない。実験の結果で決めるので、AI の賛否に頼らない。ただし、変更が小さく戻しやすい場面では、頼み直しの手軽さを取ってよい。

## 人が握るものと確かめ方 {#what-you-keep}

人が握るものは、次の 4 つである。

- 評価の基準：何を良い案とするかは、人が書く。
- 採る案：AI の推奨は材料で、決めるのは人である。
- 流す実験：どの指摘を実験で確かめるかを、人が選ぶ。
- やめどき：追う指摘の範囲を先に決める。たとえば、確信度が高く影響の大きいものだけにする。

確かめ方は、記録を付けて測る。次の記録を、自分の仕事で取る。

- 同じ計画を、「自信あり」の書き方と中立の書き方の 2 通りで出し、Claude の評価の差を記録する。差が小さければ、その計画では好みを伏せる手の優先度は低い。
- 同じ会話での批評と、新しい文脈での批評を比べ、指摘の数と中身を記録する。
- 記録には、日付と使ったモデルと面（アプリまたは Claude Code）を付ける。

最新の Claude の戦略や計画への迎合の割合は、この辞典では確かめていない。自分の環境の記録を、根拠として優先する。

賛成を採る理由に使わない決まりは、<!-- link:begin agreement-is-not-evidence#how-to-check -->[同意は根拠に数えない（AI レビュアーの一致を含む） › 確かめ方](agreement-is-not-evidence.md#how-to-check)<!-- link:end -->にある。押されて意見を変える症状の切り分けは<!-- link:begin caves-when-pushed#diagnosis -->[すぐ同意して意見を変える（迎合） › 原因を安く確かめる順](../symptoms/caves-when-pushed.md#diagnosis)<!-- link:end -->、依頼の書き換えは<!-- link:begin before-after-prompts -->[Before/After プロンプト集](../prompting/before-after-prompts.md)<!-- link:end -->を使う。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Challenging the Evaluator: LLM Sycophancy Under User Rebuttal](https://arxiv.org/abs/2509.16533)：arXiv（Kim, Sungwon ほか）・英語・確認日 2026-11-04
- [SycEval: Evaluating LLM Sycophancy](https://arxiv.org/abs/2502.08177)：arXiv（Fanous, Aaron ほか）・英語・確認日 2026-11-04
- [TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models](https://arxiv.org/abs/2503.11656)：arXiv（Liu, Joshua ほか）・英語・確認日 2026-11-04
- [Mitigating LLM Sycophancy in Code Smell Detection Using Evidence-Guided Reasoning Prompts](https://arxiv.org/abs/2607.10411)：arXiv（Fahad, Istiaq Ahmed ほか）・英語・確認日 2026-11-04
- [Are LLMs Reliable Code Reviewers? Systematic Overcorrection in Requirement Conformance Judgement](https://arxiv.org/abs/2603.00539)：arXiv（Jin, Haolin ほか）・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [同意は根拠に数えない（AI レビュアーの一致を含む）](agreement-is-not-evidence.md)

**次に読む**

- [データを分析する](../recipes/data-analysis.md)

**関連**

- [迎合（sycophancy）](../basics/sycophancy.md)
- [選択肢と推奨案を出させる](../prompting/ask-for-options.md)
- [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [レビュアーへの指示の書き方](../verify/instructing-reviewers.md)
- [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)
- [サブエージェントは別室の部下](../basics/subagent-isolation.md)
- [頼む前に自分で考える（AI には問い・反論・道具を頼む）](think-before-asking.md)
- 案出しは独立に、突き合わせは AI に（準備中）
- [役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](../team/separate-roles.md#against-sycophancy)
- 用途別プロンプトの型（準備中）
- [Before/After プロンプト集](../prompting/before-after-prompts.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
