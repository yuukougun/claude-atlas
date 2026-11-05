---
id: measure-changes
title: 変更が効いたかを測る（小さな eval）
aliases: [小さな eval, プロンプトの評価（eval）入門, 前後で比べる, 変更の効果の測り方, pass^k]
type: recipe
field: eval
chapter: 変化を測る
order: 30
level: 任せる
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: [体感を信じる]
scenes: [開発, 文章]
summary: CLAUDE.md・プロンプト・スキルの変更が効いたかを、失敗したタスクを前後で何度か走らせて比べる小さな eval で確かめられる。一度の試行では判断しない。
signs:
  - {type: goal, text: CLAUDE.md を変えて良くなったか知りたい}
  - {type: goal, text: プロンプトや手順書を直した効果を比べたい}
  - {type: symptom, text: 一度試して良かった変更が、次には効かなかった}
  - {type: symptom, text: 平均は良くなったのに、一部のケースで悪くなっていた}
wave: 1
prerequisites: [felt-vs-measured, nondeterminism, define-done]
related: [model-based-grading, experiment-log, selection-pressure, after-switching-models, claude-md-length, writing-skills#evaluate, pruning-extensions, before-after-prompts, prompt-patterns, keep-replies-in-japanese#measure, check-the-metric, test-the-verifier, insights-and-usage-review, headless-basics, batch-api-basics, measure-the-upper-bound, verifier-defines-problem]
tracks: [plugin-eval]
outdated_advice: [console-prompt-generator]
sources: [anthropic-eng-demystifying-evals-ai-agents, anthropic-research-infrastructure-noise, api-docs-prompt-engineering-overview, cc-docs-skills, cc-docs-plugin-evals]
volatility: 低
sections:
  - {title: 成功の基準を先に決める（task・trial・grader・transcript・outcome）, anchor: terms}
  - {title: 小さな eval の手順, anchor: small-eval}
  - {title: スキルの有り無しを新しいセッションで比べる（skill-creator・claude plugin eval）, anchor: compare-skills, level: 仕組みにする}
  - {title: 採点の種類（コード・モデル・人）, anchor: graders}
  - {title: 試行の数と差の大きさ, anchor: how-many-runs}
  - {title: 合計ではなく、層別と最悪ケースで見る, anchor: by-stratum, level: 仕組みにする}
  - {title: transcript を読む, anchor: read-transcripts}
  - {title: 手順が回っているかの確かめと、失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：CLAUDE.md・プロンプト・スキルの変更が効いたかを、失敗したタスクを前後で何度か走らせて比べる小さな eval で確かめられる。
    - **いつ引くか**：CLAUDE.md を変えて良くなったか知りたいとき。一度試して良かった変更が次には効かなかったとき。平均は上がったのに、一部のケースが悪くなっていたとき。
    - **前提**：<!-- link:begin felt-vs-measured -->[体感と実測](felt-vs-measured.md)<!-- link:end -->・<!-- link:begin nondeterminism -->[同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)<!-- link:end -->・<!-- link:begin define-done -->[「完了」を定義して渡す](../verify/define-done.md)<!-- link:end -->

<!-- textlint-disable -->
別名：小さな eval・プロンプトの評価（eval）入門・前後で比べる・変更の効果の測り方・pass^k
<!-- textlint-enable -->

変更が効いたかを測る小さな eval は、失敗したタスクを集め、変更の前と後で同じ条件のまま何度かずつ走らせ、あらかじめ決めた基準で採点して比べる手順である。Claude の答えは毎回少し変わるので、一度の試行で良し悪しは決められない。体感に頼らず、記録を付けた回数で判断する。

## 成功の基準を先に決める（task・trial・grader・transcript・outcome） {#terms}

小さな eval を始める前に、何が成功かを決める。基準が後から決まると、結果を見てから都合のよい基準を選ぶことになる。公式の Prompt engineering overview も、プロンプトを改善する前に、成功の基準を定義して、経験的に測る方法を用意するよう勧めている（[Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)）。基準の置き方は<!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end -->と同じ考え方である。

eval の語は、Anthropic の記事の定義で揃える（[Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)、2026-01-09）。

| 語 | 意味 | CLAUDE.md の変更を測るときの例 |
| --- | --- | --- |
| task | 入力と成功の基準を持つ 1 つの課題 | 「この関数にテストを足す」と、「テストが通り、既存のテストを書き換えていない」 |
| trial | 1 つの task を 1 回走らせること | 同じ task を新しいセッションで 3 回走らせれば、3 つの trial |
| grader | trial を採点するロジック | テストコマンドの終了コード、差分の検査、採点役の Claude、人の目 |
| transcript | trial の全記録 | 指示、ツールの呼び出し、出力、最後の報告 |
| outcome | trial の後の環境の最終状態 | テストの結果、変わったファイル |

採点は、Claude が「やった」と言った内容でなく、outcome で行う。たとえば予約の処理なら、予約が本当に DB にあるかを見る。報告の文は、結果と食い違うことがある。

結果のまとめ方にも 2 つの語がある。pass@k は、k 回のうち 1 回でも成功する確率である。pass^k は、k 回すべてが成功する確率である。1 回あたりの成功率が 75% なら、3 回続けて成功する確率は約 42% になる（0.75 の 3 乗。Anthropic の同じ記事の例）。CLAUDE.md の規則や手順のように、毎回守られてほしい変更は、pass^k で見る。

測る前に整える守りが 2 つある。1 つ目は、採点そのものが正しいかである。壊れた grader で測った結果は、変更の効果を表さない。その確かめ方は<!-- link:begin test-the-verifier#red-green -->[検証器そのものを確かめる（red/green・手で計算したケース） › red/green を検証器に当てる](test-the-verifier.md#red-green)<!-- link:end -->に書く。2 つ目は、指標が本当の目的とずれていないかである。このずれは<!-- link:begin check-the-metric#mismatch -->[評価指標そのものを確かめる › 指標と目的のずれ](check-the-metric.md#mismatch)<!-- link:end -->で確かめる。

古い手順にも注意する。Console の prompt generator や improver にプロンプトを直させる手順は、すでに使えない（<!-- link:begin outdated-advice-ledger#console-prompt-generator -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#console-prompt-generator)<!-- link:end -->）。今は、成功の基準と評価を決めて、変えた効果を測りながら直す。

## 小さな eval の手順 {#small-eval}

小さな eval は、1 つの変更について、失敗したタスクを前後で数回ずつ走らせる手順である。各段に、終わったかの確かめを付ける。

1. **変えるものを 1 つに絞る**。CLAUDE.md の 1 か所、プロンプトの 1 文、スキルの 1 つのように、1 回の eval で変えるのは 1 つにする。確かめ：変更前の版を残してあり、差分を見て何を変えたか 1 文で言える。複数を一度に変えた結果は、どれが効いたか分からない。良かった版を選び続ける罠は<!-- link:begin selection-pressure#defenses -->[選択圧：良かった版を選び続ける罠 › 防ぎ方](selection-pressure.md#defenses)<!-- link:end -->で防ぐ。
2. **失敗したタスクを集める**。実際に Claude が失敗した、または不満が残った作業から取る。Anthropic の記事は、実際の失敗から取った 20〜50 個の単純なタスクで始められるとする（公式の立場）。個人の変更を測る小さな版では、数個から 20 個ほどを目安にする（推論・実践例なし。この辞典の提案）。層（小さな修正と大きな変更など、変更の影響が違いそうな task の分け方）も、結果を見る前のここで決めておく。確かめ：各 task に、入力と、成功の基準と、層が書いてある。
3. **起きるべき場合と起きるべきでない場合の両方を入れる**。「テストを実行する」規則を足すなら、テストのある作業のほかに、テストのない作業も入れる。確かめ：変更が出しゃばる側のケースが、1 つ以上ある。
4. **採点を決める**。コードで採点できるものはコードで採点する（Claude に採点させる場合は<!-- link:begin model-based-grading#prefer-code -->[Claude に採点させる（人の判定で較正する） › コードで判定できるものはコードで](model-based-grading.md#prefer-code)<!-- link:end -->を参照）。確かめ：1 つの trial を見て、人が合否を同じ答えに決められる。
5. **変更前を測る**。同じ task を、変更前の版で、1 つにつき数回ずつ走らせる。各 trial は、きれいな環境から始める。確かめ：前の trial の作業ファイルや会話が、次の trial に残っていない。
6. **変更後を測る**。変更だけを入れ替え、モデルと effort、使える道具、開始時のファイルを同じにして、同じ回数を走らせる。確かめ：前後で変わっているのが、変えたもの 1 つだけである。
7. **記録表に書いて比べる**。trial ごとの合否と、失敗の様子を表に残す。合計、層別、前より悪くなった task の順に見て、最後に失敗の transcript を読む。確かめ：採否の理由を、表の数字と transcript の引用で言える。

記録表の雛形を次に置く。値は例であり、自分の課題に合わせて決め直す。

<!-- gen:begin snippet measure-changes/eval-record -->
<!-- textlint-disable -->

??? example "雛形：小さな eval の記録表（タスク・変更の前後・試行ごとの合否と失敗の様子）"

    ```markdown
    # 小さな eval の記録：<変更の名前>

    ## 条件（前後で揃えるもの）

    - モデルと effort：<例：同じモデル、effort は既定のまま>
    - 試行の数：<タスクごとに N 回（例：3 回）>
    - 開始状態：<例：同じコミットを新しく checkout し、新しいセッションで始める>
    - 変えたもの（1 つだけ）：<例：CLAUDE.md の 12〜15 行目を追加>
    - 採点：<例：`npm test` が通り、変更ファイルが 3 つ以下なら合格（コードで採点）>

    ## 記録表

    | タスク | 層（種類） | 版 | 1 回目 | 2 回目 | 3 回目 | 失敗の様子（transcript で確かめた原因） |
    | --- | --- | --- | --- | --- | --- | --- |
    | A：<失敗したタスクの名前> | <例：小さな修正> | 前 | ○ | × | × | <例：テストを実行せずに終えた（Claude の誤り）> |
    | A：<同じタスク> | <同じ層> | 後 | ○ | ○ | × | <例：3 回目は採点の条件が曖昧だった（課題の曖昧さ）> |
    | B：<…> | <…> | 前 |  |  |  |  |
    | B：<…> | <…> | 後 |  |  |  |  |

    ## 集計（合計と、層別と、最悪のタスク）

    - 試行の合格数：前 <  > / <  >、後 <  > / <  >
    - 毎回合格したタスク（pass^k）：前 <  >、後 <  >
    - 1 回でも合格したタスク（pass@k）：前 <  >、後 <  >
    - 層ごとの合格数：<層ごとに前後を書く>
    - 前より悪くなったタスク：<名前と、transcript で見た理由>

    ## 判断

    - 採否：<採る・採らない・試行を増やす>
    - 理由と、残る疑い：<例：差が 1 ケース分で、試行が少ない>
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.269。

<!-- textlint-enable -->
<!-- gen:end snippet measure-changes/eval-record -->

trial を走らせる手段は、面ごとに違う。

=== "アプリ"
    task ごとに新しい会話を開き、同じ依頼を前後で同じ回数ずつ出す。変更するのは、プロジェクトの指示やスタイルのうち 1 つにする。結果は手で記録表に写すので、task の数を少なく絞る。

=== "Claude Code"
    task ごとに新しいセッションを開く。作業ディレクトリは、同じコミットを新しく取り出したものにする。非対話モードの `claude -p` を使うと、スクリプトから回せる。無人で回すときは、許す道具と止まる上限を明示する（<!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](../delegate/headless-basics.md#limits)<!-- link:end -->）。

=== "API"
    変更前と変更後のシステムプロンプトを用意し、task の入力を、同じモデルと同じ設定で何度か送る。試行が多いときは、急がない処理を一括で流す手段が使える（<!-- link:begin batch-api-basics#fit -->Message Batches API（急がない大量の処理）<!-- link:end -->）。

## スキルの有り無しを新しいセッションで比べる（skill-creator・claude plugin eval） {#compare-skills}

スキルを足した効果は、スキルを入れた状態と入れない状態を、新しいセッションで比べて確かめる。公式のスキルの文書は、この比べ方を作成の推奨に挙げ、skill-creator のプラグインと `claude plugin eval` の 2 つの道具を案内している（[Extend Claude with skills](https://code.claude.com/docs/en/skills)）。

`claude plugin eval` は、シェルのコマンドで、プラグインを入れた場合と入れない場合（no-plugin baseline）を同じ task で走らせて採点し、結果を比べる道具である（[Test plugins with evals](https://code.claude.com/docs/en/plugin-evals)）。この機能の成熟度は <!-- gen:begin feature plugin-eval/maturity -->GA<!-- gen:end feature plugin-eval/maturity --> である。

使う前に、次の点を知っておく。

- 実行と採点は、どれも実際のモデルの呼び出しである。プランの使用量か、API の請求に数える。回数を増やすと、費用がそのまま増える。
- git のある環境では、git 2.31 以降が要る。
- マニフェストの `experimental.evals` のキーは、形が変わりうる。書き方は公式の文書で、そのときの版を確かめる。

手動で比べるときも、考え方は同じである。スキルを入れた版と入れない版で、task、モデル、開始時のファイルを揃え、新しいセッションで同じ回数ずつ走らせる。スキルが読み込まれたか、読み込まれたうえで手順どおりに使われたかは、transcript で確かめる。スキルの作り方と、効いているかの確かめの入口は<!-- link:begin writing-skills#evaluate -->[スキルの作り方 › 効いているかを確かめる](../extend/writing-skills.md#evaluate)<!-- link:end -->にある。不要になったスキルを外すときも、外す前後を同じ方法で比べる（<!-- link:begin pruning-extensions#measure -->[拡張の棚卸しと剪定 › 測る](../extend/pruning-extensions.md#measure)<!-- link:end -->）。

## 採点の種類（コード・モデル・人） {#graders}

採点の種類は 3 つあり、task ごとに選ぶ。Anthropic の記事は、それぞれの性質を次のように整理している。

| 採点 | 強み | 弱み |
| --- | --- | --- |
| コード | 速く、安く、同じ結果が再現できる | 融通が利かない |
| モデル（Claude など） | 柔軟で、機械で判定しにくい出力も扱える | 結果がぶれる。人の判定との較正が要る |
| 人 | 最も信頼できる | 高く、遅い |

コードで判定できるものは、コードで判定する。たとえば「テストが通る」「指定したファイルが変わっていない」「出力に禁止の語がない」は、コードで書ける。経路でなく結果で採点するので、Claude が通った道筋を細かく縛らない。

コードの採点にも落とし穴がある。Anthropic の記事によれば、Opus 4.5 の CORE-Bench の点が最初は 42% だった理由の 1 つは、厳しすぎる採点だった。96.12 という答えを、96.124991… と違うとして落としていた。ほかに、あいまいな課題の仕様と、厳密には再現できない確率的な課題があった。これらを直し、制約の少ない scaffold に替えると、点は 95% になった。それぞれの寄与は、記事に書かれていない（根拠：中）。

モデルによる採点は、人の判定と比べて較正してから使う。手順は<!-- link:begin model-based-grading#calibrate -->[Claude に採点させる（人の判定で較正する） › 人の判定と比べて較正する](model-based-grading.md#calibrate)<!-- link:end -->に書く。人による採点は、モデルの採点を較正するために、少数の trial に使う。

## 試行の数と差の大きさ {#how-many-runs}

試行の数が少ないと、大きな差しか見分けられない。数回ずつの小さな eval の結果は、傾向として読む。

次の表は、5 つの task を前後で 3 回ずつ走らせた、架空の結果である（○は成功、×は失敗）。

| task | 変更前（3 回） | 変更後（3 回） |
| --- | --- | --- |
| A | ○ / ○ / ○ | ○ / ○ / ○ |
| B | ○ / × / × | ○ / ○ / ○ |
| C | × / × / × | ○ / × / × |
| D | ○ / ○ / × | ○ / ○ / × |
| E | × / ○ / × | × / × / × |

この表を、3 通りに数える。

- 成功した trial の数は、15 回中、前が 7 回、後が 9 回である。
- 1 回でも成功した task（pass@3）は、前後とも 5 つ中 4 つで、同じである。
- 3 回とも成功した task（pass^3）は、前が 5 つ中 1 つ（A）、後が 5 つ中 2 つ（A と B）である。

数え方で見え方が変わる。毎回守られてほしい変更なら、pass^3 の増加に意味がある。一方で、task E は 1 回成功から 0 回成功へ減り、前より悪くなっている。

差の大きさの目安を、計算で示す。成功率の 95% 区間の半幅は、独立な試行を仮定した概算で、n 回のとき 1.96 × √(p(1−p)/n) になる。勝率 55% の版を、勝率 50% の版と見分ける対戦の例では、n = 100 で約 9.75 ポイント、n = 400 で約 4.88 ポイントになる。400 回でようやく、区間の下限が 50% をわずかに上回る（計算。引き分けのない独立な試合を前提にした概算）。この計算を当てはめると、15 回や 30 回の eval は、十数ポイントの差でも偶然と区別できない。小さな eval で見分けられるのは、大きな差だけである。

実行環境のぶれも差を作る。Anthropic の研究（2026-02-05）では、Terminal-Bench 2.0 で資源の最も多い設定と最も少ない設定の間に 6 ポイントの差が出た（p<0.01）。測ったのは Claude のモデルで、ほかのモデルは厳密には試していない。資源の設定が文書化されて揃うまでは、3 ポイント未満の差を疑うべきだとしている（根拠：中）。前後の測定は、同じ環境で、できれば近い時間帯に走らせる。

!!! example "判断例：差は出たが、小さい"
    - **状況**：CLAUDE.md に 1 規則を足した。失敗した task 5 つ（A〜E）を 3 回ずつ走らせたところ、成功が 15 回中 7 回から 9 回に増えた。ただし task E は、1 回成功から 0 回成功に減った。
    - **迷う候補**：増えたのだから採る。または、試行を増やすか、差の出た task を絞って確かめてから決める。
    - **選んだもの**：すぐには採らず、task を足して回数を 2 倍にし、E の transcript を読んでから決める。
    - **理由**：差は 2 回分で、試行が少ないので偶然の範囲に入る。E の悪化が規則の副作用なら、増えた分を打ち消すかもしれない。

## 合計ではなく、層別と最悪ケースで見る {#by-stratum}

合計の成功率は、一部の task が悪くなったことを隠す。結果は合計だけで見ず、task の種類や入力の条件ごとに集計して、最も悪い層を追う。

層は、変更の影響が違いそうな軸で切る。たとえば、小さな修正と大きな変更、テストのある作業とない作業、日本語の作業と英語の作業である。層ごとに前後の成功数を並べ、悪くなった層と、前より悪くなった task を別に書く。前節の架空の表の task E がその例で、合計が 7 回から 9 回へ増えていても、E は 1 回から 0 回へ減っている。

層別は、結果が出た後に層の切り方を選ぶと、都合のよい切り方を選べてしまう。層は、手順の 2 段目で task を集めたときに決めておく。また、層が細かくなるほど 1 層の試行は減り、偶然に動きやすくなる。層別の数字は、悪化の見張りとして使い、効果の証明には使わない（根拠：中・類推。入力の条件ごとに集計して最悪の層を追う実践は、ほかの分野の実験の運用に由来する）。

変更の目的が、守られていた振る舞いを壊さないことなら、回帰の eval に分ける。Anthropic の記事は、低い通過率から始める能力評価と、ほぼ 100% を保つ回帰評価を分けている。回帰評価のケースが 1 つ落ちたら、合計が良くても調べる。

## transcript を読む {#read-transcripts}

採点の数字を受け取る前に、失敗した trial の transcript を読む。失敗が、Claude の誤りなのか、採点の誤りなのかは、数字からは分からない。Anthropic の記事は、スコアを鵜呑みにせず transcript を読み、エージェントの誤りか採点のバグかを見分けるよう勧める。

多数の試行で 1 回も成功しない task は、たいてい、課題か採点が壊れている。最先端のモデルで 100 回走らせても成功が 0 なら、モデルの限界と決める前に、課題の仕様と採点を疑う（根拠：中。Anthropic の同じ記事）。採点の節で述べた、厳しすぎる採点で点が 42% に留まった CORE-Bench の例が、その実例である。

読む対象は、失敗した trial と、前より悪くなった task を優先する。成功した trial も、数件は読む。採点を通っても、禁止の近道（テストの書き換えなど）を通っていることがある。

失敗の原因は、Claude の誤り、採点の誤り、課題の曖昧さ、環境のぶれの 4 つに分けると整理しやすい。分類を Claude に下書きさせる依頼の雛形を、次に置く。

<!-- gen:begin snippet measure-changes/classify-failures -->
<!-- textlint-disable -->

??? example "雛形：失敗した試行の原因を transcript から分類させる依頼の雛形"

    ```text
    添付した試行の記録（transcript）を読み、採点で失敗とされた試行ごとに、原因を次の 4 つのどれかに分類してください。

    - Claude の誤り：指示や課題は明確で、採点も妥当だが、Claude が守らなかった、または間違えた。
    - 採点の誤り：Claude の結果は課題の趣旨を満たすのに、採点の条件が厳しすぎる、または間違っている。
    - 課題の曖昧さ：課題の仕様が曖昧で、複数の読み方があり、採点がその 1 つだけを正としている。
    - 環境のぶれ：時間切れ・資源の不足・外部のサービスの失敗など、Claude の出力に関係しない原因。

    出力の形：試行ごとに 1 行で、「試行の名前｜分類｜根拠として記録から引いた 1〜2 行」の順に書いてください。
    判断できないときは、分類を「不明」にして、何が分かれば決められるかを書いてください。
    課題・採点・CLAUDE.md を直す案は、この段では書かないでください。分類だけを返してください。

    ＜試行の記録をここに貼る、またはファイルの場所を書く＞
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.269。

<!-- textlint-enable -->
<!-- gen:end snippet measure-changes/classify-failures -->

Claude の分類は下書きとして読み、少なくとも数件は、自分で transcript を読んで確かめる。採点役の Claude の較正は<!-- link:begin model-based-grading#calibrate -->[Claude に採点させる（人の判定で較正する） › 人の判定と比べて較正する](model-based-grading.md#calibrate)<!-- link:end -->の方法による。

## 手順が回っているかの確かめと、失敗したとき {#when-it-fails}

eval 全体が回っているかは、次の 3 点で確かめる。

- 変更前の測定を 2 回行ったとき、結果が近い。近くなければ、変更の効果より、測定のぶれが大きい。
- 失敗した trial の transcript に、原因として挙げた失敗が実際に出ている。
- 採否の理由が、表の数字と transcript の引用で書かれている。

うまくいかないときは、症状で引き先を選ぶ。

- **一度試して良かった変更が、次には効かなかった**：試行が少なく、偶然で動いている。回数を増やし、変更前も複数回測る。答えのばらつきの仕組みは<!-- link:begin nondeterminism -->[同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)<!-- link:end -->にある。
- **平均は良くなったのに、一部が悪くなっていた**：層別と、前より悪くなった task を先に見る。原因は transcript で確かめる。
- **良かった版を選び続けて、本番では効かない**：測っている task に合わせ込んでいる。防ぎ方は<!-- link:begin selection-pressure#defenses -->[選択圧：良かった版を選び続ける罠 › 防ぎ方](selection-pressure.md#defenses)<!-- link:end -->に書く。
- **採点がおかしい、または指標が目的とずれている**：<!-- link:begin test-the-verifier#hand-calculated -->[検証器そのものを確かめる（red/green・手で計算したケース） › 手で計算したケース](test-the-verifier.md#hand-calculated)<!-- link:end -->と<!-- link:begin check-the-metric#mismatch -->[評価指標そのものを確かめる › 指標と目的のずれ](check-the-metric.md#mismatch)<!-- link:end -->で確かめる。
- **結果を残したい、同じ失敗を繰り返す**：仮説を先に書き、採否と判定者を残す。<!-- link:begin experiment-log#hypothesis-first -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 仮説を先に書く](experiment-log.md#hypothesis-first)<!-- link:end -->を使う。
- **モデルを替えた後の見直し**：外すものを 1 つずつ外して測る（<!-- link:begin after-switching-models#remove-one-at-a-time -->[新しいモデルに替えたら見直すこと › ハーネスの部品を一つずつ外して測る](../models/after-switching-models.md#remove-one-at-a-time)<!-- link:end -->）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)：Anthropic・英語・確認日 2026-11-04
- [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/research/infrastructure-noise)：Anthropic・英語・確認日 2026-11-04
- [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Test plugins with evals](https://code.claude.com/docs/en/plugin-evals)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [体感と実測](felt-vs-measured.md)
- [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- [「完了」を定義して渡す](../verify/define-done.md)

**次に読む**

- [新しいモデルに替えたら見直すこと](../models/after-switching-models.md)
- [Claude に採点させる（人の判定で較正する）](model-based-grading.md)
- [選択圧：良かった版を選び続ける罠](selection-pressure.md)

**関連**

- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](experiment-log.md)
- [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- [スキルの作り方 › 効いているかを確かめる](../extend/writing-skills.md#evaluate)
- [拡張の棚卸しと剪定](../extend/pruning-extensions.md)
- [Before/After プロンプト集](../prompting/before-after-prompts.md)
- [用途別プロンプトの型](../prompting/prompt-patterns.md)
- [日本語で返し続けさせる › 検証の方法](../japanese/keep-replies-in-japanese.md#measure)
- [評価指標そのものを確かめる](check-the-metric.md)
- [検証器そのものを確かめる（red/green・手で計算したケース）](test-the-verifier.md)
- [/insights と /usage で振り返る](insights-and-usage-review.md)
- [非対話モード（claude -p）の基本](../delegate/headless-basics.md)
- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](verifier-defines-problem.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
