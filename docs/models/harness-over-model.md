---
id: harness-over-model
title: モデルの差よりハーネスの差
aliases: [harness, ハーネスエンジニアリング, モデルを替える前に, ツールを乗り換える前に]
type: concept
field: models
chapter: モデルを選ぶ
order: 30
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [確かめる, 見せる]
prevents: [合っていない, 確かめていない]
pitfalls: [体感を信じる]
scenes: [開発, データ分析, コンテスト]
summary: 結果の差がモデルではなく、検証の手段・渡す文脈・指示といったハーネスから来る場合があることが分かる。モデルを替える前にハーネスを直し、自分の評価で比べる。
signs:
  - {type: symptom, text: モデルを替えても結果があまり変わらない}
  - {type: goal, text: 別の AI ツールのほうが良いと聞き、乗り換えるか迷う}
  - {type: situation, text: 同じ課題でも、AI ツールの順位が条件によって入れ替わる話を見た}
prerequisites: [choosing-a-model]
related: [verifier-defines-problem, measure-changes, felt-vs-measured, verification-ladder, extensions-at-a-glance, after-switching-models, compare-hypotheses-in-parallel]
tracks: []
outdated_advice: []
sources: [drivendata-ai-agents-data-science-competitions, anthropic-eng-harness-design-long-running, api-docs-choosing-a-model, mitchellh-writing-ai-adoption-journey]
volatility: 中
sections:
  - {title: ハーネスとは何か, anchor: what-is-harness}
  - {title: 差がハーネスから来るとき, anchor: when-harness-matters}
  - {title: 比べるときは自分の評価で, anchor: compare-with-your-eval}
  - {title: 何に効くか（原理と防ぐ原因）, anchor: what-it-prevents}
  - {title: 誤解しやすい点, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：結果の差がモデルではなく、検証の手段・渡す文脈・指示といったハーネスから来る場合があることが分かる。
    - **いつ引くか**：モデルを替えても結果があまり変わらないとき。別の AI ツールのほうが良いと聞き、乗り換えるか迷うとき。同じ課題でも、AI ツールの順位が条件によって入れ替わる話を見たとき。
    - **確かめ方**：ハーネスを直す前と後で、同じ課題・同じ検証器で比べる。体感で決めない。
    - **前提**：<!-- link:begin choosing-a-model -->[モデルの選び方（三段階）](choosing-a-model.md)<!-- link:end -->

<!-- textlint-disable -->
別名：harness・ハーネスエンジニアリング・モデルを替える前に・ツールを乗り換える前に
<!-- textlint-enable -->

モデルの差よりハーネスの差は、結果が悪いときにモデルを疑う前に、モデルのまわりの仕組みを疑う考え方である。同じモデルでも、何を見せ、何で確かめ、どう頼むかで結果は変わる。モデルを替えるのは、ハーネスを直して自分の課題で比べた後でよい。

## ハーネスとは何か {#what-is-harness}

ハーネスとは、モデルのまわりでツールを動かし、モデルが見る文脈を管理する層である。Claude Code 本体がこれにあたる。API では、自分で組んだ呼び出しのループと、そこに渡すシステムプロンプト・ツール・検証の処理がこれにあたる。

モデルは入力を受け取って出力を返すだけである。何を入力として見せるか、出力をどう実行するか、終わったと誰が判断するかは、ハーネスが決める。

| 部品 | 決めること | 例 |
| --- | --- | --- |
| 文脈 | モデルが何を見るか | `CLAUDE.md`・読ませるファイル・会話の履歴 |
| 指示 | 何をどう頼むか | プロンプト・システムプロンプト・スキル |
| 道具 | 何を実行できるか | ファイル編集・シェル・検索・MCP |
| 検証の手段 | 終わったと言えるかを誰が決めるか | テスト・採点の処理・フック |
| ループの制御 | いつ止め、いつやり直すか | 停止条件・ターン数の上限・サブエージェント |

面によって、部品を置く場所が違う。

=== "Claude Code"

    文脈は `CLAUDE.md` やルール、指示はスキル、検証の手段はフックやテストの実行手順として置く。部品ごとの強制力と読み込みの時期は<!-- link:begin extensions-at-a-glance#table -->[拡張機能の全体図と使い分け早見表 › 比較の表](../extend/extensions-at-a-glance.md#table)<!-- link:end -->にある。

=== "API"

    文脈と指示は、リクエストに入れるシステムプロンプトとメッセージで決める。道具の定義、結果の検証、やり直しの条件は、呼び出し側のコードで書く。

Anthropic の記事は、ハーネスの各部品を「モデルが単独ではできないこと」についての仮定だと述べる。モデルが変わったら、その仮定がまだ要るかを確かめ、部品を 1 つずつ外して効果を測る方針である（根拠：中。企業の一次の報告で、Claude Opus 4.5 の時期の事例）。外し方は<!-- link:begin after-switching-models#remove-one-at-a-time -->[新しいモデルに替えたら見直すこと › ハーネスの部品を一つずつ外して測る](after-switching-models.md#remove-one-at-a-time)<!-- link:end -->にある。

## 差がハーネスから来るとき {#when-harness-matters}

差がハーネスから来る場合とは、同じモデルでも、見せる文脈・検証の手段・指示を変えると結果が変わる場合である。次の 2 つの報告が手がかりになる。

**同じ課題をハーネスだけ変えて走らせた例**：Anthropic の記事は、レトロなゲームを作る課題を、単体の実行と、計画・生成・評価を分けたフルハーネスの実行で比べた。単体の実行は見た目こそそれらしいが、中核の機能が動かなかった。フルハーネスの実行は、遊べる状態まで届いた。フルハーネスの実行は時間も費用も大きかった。モデルは同じ Claude Opus 4.5 である（根拠：中。1 つの課題の報告）。

**ツールの順位が競技ごとに入れ替わった例**：DrivenData は、データ分析コンテスト 3 つで、Claude Code（Opus 4.5）と Codex（GPT 5.2 Codex）を同じ条件で走らせて比べた。順位は競技によって入れ替わり、どちらも全部で先ではなかった。著者は、成績は素のモデルの賢さだけで決まらず、多くの力はエージェントの組み方で引き出されると書いている（根拠：中。版依存。2026 年 2 月の報告で、3 競技の標本）。

2 つ目の報告の読み方に注意がある。著者が示す根拠は、組み方が未熟な別のツールの成績が大きく下がったことである。Claude Code と Codex の差のうち、どれだけがモデルでどれだけがハーネスかは、この報告では切り分けていない。順位が入れ替わったことは、「どちらのモデルが上か」を一般に決められないことの手がかりにとどまる。

ミスのたびにハーネスへ書き戻す実践も、同じ見方に立つ。Claude が間違えたら、その場で直すだけでなく、`CLAUDE.md`・スクリプト・フックに再発防止の策を加える。この実践は「ハーネスエンジニアリング」と呼ばれ、複数の実務家が報告している（根拠：弱。経験談の一致）。肥大化すると守られなくなるので、古い記述を定期的に削る手間とセットで扱う。

!!! example "判断例：別のツールのほうが良いと聞いた"
    - **状況**：Claude Code でリポジトリの修正を頼んでいる。別の AI ツールのほうが良いという話を見て、乗り換えを考えた。いまは、テストの実行手順を `CLAUDE.md` に書いておらず、Claude がテストを走らせずに完了と報告することがときどきある。
    - **迷う候補**：すぐ乗り換える。または、テストの実行手順と完了の条件を足してから、同じ課題で前後を比べる。
    - **選んだもの**：先にハーネスを直し、前後を比べる。
    - **理由**：テストを走らせない欠けは、乗り換えた先でも残りうる。モデルとハーネスのどちらが原因か分からないまま替えると、効果も測れない。直した後も足りない課題が残るなら、乗り換えは筋が通る。

## 比べるときは自分の評価で {#compare-with-your-eval}

モデルやツールを比べるときは、他人の順位ではなく、自分の課題と自分の検証器（結果の合否を決めるテストや採点の処理）で比べる。公式のモデル選択ガイドも、よい評価セットを持つことを選ぶ過程で最も大事な段階としている。

手順は次のとおりである。

1. 自分の作業から代表的な課題を選ぶ。1 回の試行で決めず、同じ課題を複数回走らせる。回数と差の大きさの見方は<!-- link:begin measure-changes#how-many-runs -->[変更が効いたかを測る（小さな eval） › 試行の数と差の大きさ](../eval/measure-changes.md#how-many-runs)<!-- link:end -->にある。
2. 検証器を先に決めて固定する。比べている間に検証器を変えると、差が何から来たのか分からなくなる。検証器の置き方は<!-- link:begin verifier-defines-problem#verifier-first -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › 最初の成果物は検証器](../eval/verifier-defines-problem.md#verifier-first)<!-- link:end -->にある。
3. 変えるのは 1 つだけにする。モデルを比べるなら、ハーネスを固定してモデルだけ替える。ハーネスを比べるなら、モデルを固定して部品を 1 つ足すか外す。
4. 合計の数字だけで見ず、層ごとの結果と最悪の場合を見て、結果の記録（transcript）を読む。見方は<!-- link:begin measure-changes#by-stratum -->[変更が効いたかを測る（小さな eval） › 合計ではなく、層別と最悪ケースで見る](../eval/measure-changes.md#by-stratum)<!-- link:end -->と<!-- link:begin measure-changes#read-transcripts -->[変更が効いたかを測る（小さな eval） › transcript を読む](../eval/measure-changes.md#read-transcripts)<!-- link:end -->にある。

手順全体の小さな版は<!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end -->にまとめてある。体感で決めると、その日の調子や最近の出来事に引っ張られる。理由は<!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end -->にある。

ほかの会社の製品と比べた話を引くときは、評価の言葉ではなく条件で書く。ツールの版、使ったモデル、設定、課題、日付を添える。「その条件のその課題では、こうなった」までを言い、製品の一般の優劣にしない。自分で比べるときも、同じ形で記録を残す。

モデルを替える前に動かすものには順がある。まず effort を動かし、次にハーネスを見て、最後にモデルを替える。理由は<!-- link:begin choosing-a-model#effort-first -->[モデルの選び方（三段階） › モデルより effort を先に動かす理由](choosing-a-model.md#effort-first)<!-- link:end -->にある。

!!! example "判断例：モデルを替えても結果が変わらない"
    - **状況**：データ分析の作業を 1 つ上のモデルに替えたが、出力の誤りの数がほとんど変わらない。誤りの多くは、元のデータの列の意味を取り違えたものである。
    - **迷う候補**：さらに上のモデルに替える。または、列の意味の説明を文脈として渡し、集計の結果を既知の値と突き合わせる検証を足す。
    - **選んだもの**：文脈と検証を足し、同じ課題で前後を比べる。
    - **理由**：誤りの原因がデータの意味の取り違えなら、渡していない情報は上のモデルでも補えない。モデルを替えても変わらないのは、ボトルネックがモデルの外にあるという手がかりである。

## 何に効くか（原理と防ぐ原因） {#what-it-prevents}

この考え方は、原理の「確かめる」と「見せる」に関わる。確かめるは、結果の差を自分の課題と検証器で測ることである。見せるは、モデルが判断に要る文脈を、ハーネスを通して渡すことである。

防ぐ原因は 2 つある。

- **合っていない**：課題に要る文脈や指示が渡っていないために、出力が目的に合わない。モデルを替えても、渡していないものは補えない。
- **確かめていない**：終わったかどうかを確かめる手段がないために、誤りがそのまま完了として返る。検証の手段を足すと、この原因が減る。手段の選び方は<!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](../verify/verification-ladder.md#choose-step)<!-- link:end -->にある。

人の側の落とし穴は、体感を信じることである。「あのツールは賢い気がする」という印象は、ハーネスの差をモデルの差と取り違えやすい。測らずに乗り換えると、直せたはずの欠けを持ち越す。

任せる幅を広げるときは、守りを先に置く。ハーネスを作り込んで長い作業を任せるほど、検証器が誤っていれば、誤りも同じ速さで増える。仕組みは<!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](../eval/verifier-defines-problem.md#loops-amplify)<!-- link:end -->に、確かめる手段の段は<!-- link:begin verification-ladder#four-steps -->[検証の階段 › 四つの段](../verify/verification-ladder.md#four-steps)<!-- link:end -->にある。

## 誤解しやすい点 {#misconceptions}

- **「モデルの差はない」わけではない**：この考え方は、モデルの差が無視できると言うのではない。原因を切り分けずにモデルだけを替えると、効果が測れないと言う。ハーネスを直しても足りない課題は、モデルを替える段階である。手順は<!-- link:begin choosing-a-model#three-steps -->[モデルの選び方（三段階） › 三段階：既定 → effort → 上位のモデル](choosing-a-model.md#three-steps)<!-- link:end -->にある。
- **「ハーネスは作り込むほどよい」わけではない**：部品は「モデルが単独ではできないこと」の仮定なので、モデルが変われば不要になる。複雑さは必要になってから足し、足した部品は 1 つずつ外して測る。
- **「順位が入れ替わったから、どちらも同じ」わけではない**：入れ替わりは、課題や条件に依存することを示す。ツールの優劣がないという結論は、その報告からは出ない。
- **「別系統のモデルは使わない」わけではない**：行き詰まったときの別解や、重要な変更のレビューに、別系統のモデルを使う方法はある。レビューの結果は、実行や検索で必ず確かめる。複数の仮説を並べて比べる手順は<!-- link:begin compare-hypotheses-in-parallel -->[仮説ごとに並べて、同じ物差しで比べる](../delegate/compare-hypotheses-in-parallel.md)<!-- link:end -->にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [AI Agents in Data Science Competitions: Lessons from the Leaderboard](https://blog.drivendata.org/blog/ai-agents-data-science-competitions)：DrivenData・英語・確認日 2026-11-04
- [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)：Anthropic・英語・確認日 2026-11-04
- [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)：Anthropic・英語・確認日 2026-11-04
- [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)：Mitchell Hashimoto・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [モデルの選び方（三段階）](choosing-a-model.md)

**関連**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [検証の階段](../verify/verification-ladder.md)
- [拡張機能の全体図と使い分け早見表](../extend/extensions-at-a-glance.md)
- [新しいモデルに替えたら見直すこと](after-switching-models.md)
- [仮説ごとに並べて、同じ物差しで比べる](../delegate/compare-hypotheses-in-parallel.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
