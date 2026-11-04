---
id: split-models-by-role
title: 計画・実装・サブエージェントでモデルを分ける
nav_title: 役割でモデルを分ける
aliases: [opusplan, 計画は Opus・実装は Sonnet, サブエージェントのモデル, subagent のモデル, Haiku の使いどころ, 軽いモデルの使いどころ, CLAUDE_CODE_SUBAGENT_MODEL]
type: concept
field: models
chapter: 役割で使い分ける
order: 100
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [見せる]
prevents: [合っていない]
pitfalls: []
summary: 計画と実装、本体とサブエージェントでモデルを分けるかを、仕事の重さの差と費用で決められる。分けた側で動く effort と、引き継がれる文脈も確かめる。
signs:
  - {type: goal, text: 計画は賢いモデル、実装は安いモデルに分けたい}
  - {type: goal, text: サブエージェントだけ軽いモデルで動かして、使用量を抑えたい}
  - {type: situation, text: 「計画は上位のモデル、実装は安いモデル」というコツが今も得か分からない}
prerequisites: [choosing-a-model, subagent-isolation]
related: [effort-levels#subagents-and-org-limits, when-to-plan, writing-subagents, fast-mode-and-advisor, current-models, saving-priorities, independent-review]
tracks: [model-selection, subagents]
outdated_advice: [avoid-opus-as-expensive]
sources: [api-docs-choosing-a-model, cc-docs-model-config, cc-docs-sub-agents, cc-docs-costs, cc-changelog]
volatility: 高
sections:
  - {title: 分ける形（計画と実装・本体とサブエージェント）, anchor: patterns}
  - {title: 分ける価値があるとき, anchor: when-to-split}
  - {title: 軽いモデルの使いどころ, anchor: lighter-models}
  - {title: 何に効くか（原理「見せる」と原因「合っていない」）, anchor: what-it-helps}
  - {title: 誤解しやすい点, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：計画と実装、本体とサブエージェントでモデルを分けるかを、仕事の重さの差と費用で決められる。分けた側で動く effort と、引き継がれる文脈も確かめる。
    - **いつ引くか**：計画は賢いモデル、実装は安いモデルに分けたいとき。サブエージェントだけ軽いモデルで動かして使用量を抑えたいとき。「計画は上位のモデル、実装は安いモデル」というコツが今も得か分からないとき。
    - **前提**：<!-- link:begin choosing-a-model -->[モデルの選び方（三段階）](choosing-a-model.md)<!-- link:end -->と<!-- link:begin subagent-isolation -->[サブエージェントは別室の部下](../basics/subagent-isolation.md)<!-- link:end -->。

<!-- textlint-disable -->
別名：opusplan・計画は Opus・実装は Sonnet・サブエージェントのモデル・subagent のモデル・Haiku の使いどころ・軽いモデルの使いどころ・CLAUDE_CODE_SUBAGENT_MODEL
<!-- textlint-enable -->

計画と実装でモデルを分けるとは、考える量の多い工程に上位のモデルを使い、方針が固まった後の工程に安いモデルを使うことである。同じ考え方で、本体の会話とサブエージェントにも別のモデルを割り当てられる。

先に <!-- link:begin choosing-a-model#three-steps -->[モデルの選び方（三段階） › 三段階：既定 → effort → 上位のモデル](choosing-a-model.md#three-steps)<!-- link:end --> の順（既定 → effort → 上位のモデル）で足りるかを見る。モデルを分けるのは、その後に残る選択肢の 1 つである。

## 分ける形（計画と実装・本体とサブエージェント） {#patterns}

モデルを分ける形は 2 つある。仕事を時間で分けるか、会話で分けるかが違う。

| 形 | 分ける境目 | 上位のモデルに任せる側 | 安いモデルに任せる側 |
| --- | --- | --- | --- |
| 計画と実装 | 同じ会話の中の工程 | 計画（調べて方針を決める） | 実装（決まった方針を形にする） |
| 本体とサブエージェント | 別の文脈で動く担当 | 本体の会話（判断と統合） | 件数の多い調査・分類・要約 |

**計画と実装を分ける**。plan mode で調べさせて計画を作り、承認してから実装に入る流れ（<!-- link:begin when-to-plan#when -->[plan mode の使いどころ › 計画が効く作業、省いてよい作業](../cli/when-to-plan.md#when)<!-- link:end -->）で、工程ごとにモデルを替える。Claude Code には `opusplan` というエイリアスがある。plan mode では上位の系統、実行では日常の系統のモデルで動き、工程の切り替えで自動的に替わる（公式の model-config、2026-10-29 に確認）。手で替えるなら `/model` を使う。どの系統が上位で、どれが日常向けかは <!-- link:begin current-models#lineup -->[現行モデルの一覧と位置づけ › 系統ごとの位置づけ（表）](current-models.md#lineup)<!-- link:end --> で確かめる。

**本体とサブエージェントを分ける**。サブエージェントの定義の `model` で、そのサブエージェントだけ別のモデルにできる。公式の費用の文書も、使用量を抑える手段として「サブエージェントに軽いモデルを指定する」を挙げている（`model: haiku` の例、2026-10-29 に確認）。環境変数 `CLAUDE_CODE_SUBAGENT_MODEL` でサブエージェントのモデルをまとめて決める方法も、コミュニティの解説にある（根拠：弱）。この変数と定義の `model` のどちらが優先されるかは、公式の model-config に書かれていない。使う前に自分の環境で確かめる。

本体のモデルを `/model` で替えると、本体のモデルを受け継ぐ設定のサブエージェントも同じモデルで動く。軽いモデルに固定したいサブエージェントは、定義に `model` を書く。サブエージェントそのものの作り方は <!-- link:begin writing-subagents#tools-and-model -->[サブエージェントの作り方と使いどころ › 道具・モデル・effort を絞る](../extend/writing-subagents.md#tools-and-model)<!-- link:end --> にある。

=== "Claude Code"

    `opusplan` か `/model` で計画と実装を分ける。サブエージェントは定義の `model` で分ける。サブエージェントを呼ぶたびに別の文脈ができる点は、<!-- link:begin subagent-isolation#cost -->[サブエージェントは別室の部下 › 賢くはならず、費用がかかる](../basics/subagent-isolation.md#cost)<!-- link:end --> にある。

=== "API"

    API はリクエストごとに `model` を指定する。計画を作る呼び出しと実装の呼び出しで、別のモデルを自分のコードで指定すればよい。公式のモデル選択の文書は、上位のモデルが難しい判断を受け持ち、安いモデルに作業を割り振る組み合わせ方を 2 つ挙げている（上位のモデルに難しい判断だけを相談する形と、上位のモデルが安いモデルへ作業を割り振る形）。前者の形は <!-- link:begin fast-mode-and-advisor#advisor -->fast mode と advisor › advisor（準備中）<!-- link:end --> にある。

### 分けた側で動く effort と文脈

分けるときは、分けた側で何が引き継がれるかを確かめる。

- **effort**：本体と別のモデルで動くサブエージェントは、セッションの effort を受け継がない。そのモデルに保存した effort か、そのモデルの既定で動く。この挙動が入った Claude Code の版は <!-- fact:begin subagent-own-model-effort-min-version -->未確認<!-- fact:end --> である。軽いモデルを割り当てた時点で、effort は既定になると見ておく。固定のしかたは <!-- link:begin effort-levels#subagents-and-org-limits -->[effort の段階と使い分け › サブエージェントと組織の上限](effort-levels.md#subagents-and-org-limits)<!-- link:end --> にある。
- **文脈**：サブエージェントは、自分のシステムプロンプト・指定したスキル・`CLAUDE.md` と git の状態で、新しい文脈を作って動く。本体の会話は見えない（親の会話を引き継ぐ fork は別）。したがって、安いモデルに渡す依頼は、前提・対象のファイル・返してほしい形を依頼の本文に書く。
- **計画の引き継ぎ**：計画と実装は同じ会話の中の工程なので、承認した計画は会話に残る。計画を別のセッションで実装するなら、計画をファイルに書き出して渡す。

## 分ける価値があるとき {#when-to-split}

モデルを分けるのは、仕事の重さが工程や担当で大きく違うときである。差が小さいなら、切り替えの手間と確認の手間のほうが大きい。

分ける価値が出やすいのは、次の 3 つのときである。

1. **計画が重く、実装が定型のとき**：方針が固まれば、実装は決まった手順の繰り返しになる。例は、規約が決まった置き換えの一括適用である。
2. **件数が多く、1 件が軽いサブエージェントがあるとき**：例は、ログの分類とファイルごとの要約である。1 件ごとの費用が小さくても、件数の分だけ使用量に響く。
3. **使用量の上限に実際に近づいているとき**：公式の費用の文書は、日常のコーディングは日常の系統に任せ、上位の系統は複雑な設計判断に使うことで使用量を抑えられるとしている。上限に当たる原因が重い工程の集中なら、そこだけを残して他を下げる。

分けないほうがよいのは、次のときである。

- **実装に判断が多いとき**：安いモデルの実装が計画から外れると、手戻りで計画の節約を失う。手戻りを減らすほうが先だという順は <!-- link:begin saving-priorities#order -->[節約の優先順位（手戻りを減らすのが先） › 優先順位](../cost/saving-priorities.md#order)<!-- link:end --> にある。
- **作業が小さいとき**：数ファイルの修正なら、分けずに 1 つのモデルで済ませたほうが速い。
- **費用だけを理由に、上位のモデルを避けてきたとき**：分ける前に、自分の作業で上位のモデルと比べ直す。固定の理由が費用だけなら、分けなくても足りることがある。今どうするかは <!-- link:begin outdated-advice-ledger#avoid-opus-as-expensive -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#avoid-opus-as-expensive)<!-- link:end --> にある。

この論点は、実践者の間でも意見が割れている。

- **公式の立場**：日常のコーディングは日常の系統を基本にし、上位の系統は複雑な設計判断に使う。サブエージェントには軽いモデルを指定できる（費用の文書）。ただし、モデルを替えるより effort の調整が効く場合が多いとも述べている（モデル選択の文書）。
- **実践者の幅**：「上位のモデルで計画し、安いモデルで実装する」を上限に収めるコツとして挙げる人がいる一方で、全作業で上位のモデルを使う人もいる（いずれも根拠：弱。経験談である）。後者は、トークン単価ではなく、信頼できる変更 1 件あたりの費用で比べるという考えである。
- **この辞典の推奨**：まず <!-- link:begin choosing-a-model#three-steps -->[モデルの選び方（三段階） › 三段階：既定 → effort → 上位のモデル](choosing-a-model.md#three-steps)<!-- link:end --> で足りるかを見る。分けるなら、自分の作業で分ける前後を比べ、変更 1 件あたりの費用と手戻りで決める。

!!! example "判断例：大規模な置き換えの計画と実装"
    - **状況**：数十のファイルに同じ規約の変更を入れる。どこをどう直すかの判断が最初に要り、その後は定型の作業である。
    - **迷う候補**：全工程を上位の系統で通す。計画だけ上位の系統にして、実装は日常の系統にする。
    - **選んだもの**：計画だけ上位の系統にして、実装は日常の系統にする。
    - **理由**：計画に判断が集中していて、実装は計画に沿う作業だからである。ただし、実装の結果が計画から外れていたら全工程を上位の系統に戻す。比べる単位は、変更 1 件あたりの費用と手戻りの回数である。

分けた結果は、替えた効果を確かめるときと同じやり方で測る。同じ作業を分ける前後で比べる方法は <!-- link:begin choosing-a-model#verify -->[モデルの選び方（三段階） › 替えた効果の確かめ方](choosing-a-model.md#verify)<!-- link:end --> にある。プランの使用量は、選ぶモデルで減り方が変わるので、`/usage` で確かめる。

## 軽いモデルの使いどころ {#lighter-models}

軽い系統のモデルは、件数が多く、1 件が単純で、結果を後から確かめやすい仕事に向く。公式の発表は、要約・compaction・データベースのクエリ・分類・サブエージェントといった大量処理を挙げている（2026-10-29 に確認）。系統ごとの位置づけは <!-- link:begin current-models#lineup -->[現行モデルの一覧と位置づけ › 系統ごとの位置づけ（表）](current-models.md#lineup)<!-- link:end --> にある。

向く仕事と向かない仕事は、次のように分ける。

- **向く**：ログやファイルの分類、ファイルごとの要約、決まった形式への抽出、単純な検索と集計。
- **向かない**：複雑で長い自律的なコーディング、方針の判断が要る設計、結果の確かめ方がない仕事。公式の発表も、複雑なエージェントのコーディングは上位の系統が上だとしている。

始め方にも 2 通りある。公式のモデル選択の文書は、効率優先なら軽いモデルから始めて足りない部分だけ上に替える、能力優先なら上位のモデルから始めて下げて最適化する、と説明している。件数の多い作業は前者が合う。対話で頼み始める読者には、<!-- link:begin choosing-a-model#three-steps -->[モデルの選び方（三段階） › 三段階：既定 → effort → 上位のモデル](choosing-a-model.md#three-steps)<!-- link:end --> の順を勧める（この辞典の推奨）。

軽いモデルに任せる前に、結果を確かめる手段を先に決める。任せる幅を広げるほど、確かめる側の備えも要る。軽いモデルの結果は、抜き取りで原文と照らす。または別の担当に見直させる（<!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end -->）。確かめる手段がない仕事は、軽いモデルに渡さない。

次の雛形は、ログの分類を軽いモデルのサブエージェントに任せる例である。返す形を表に絞り、原因の推測を禁じているのは、軽いモデルに判断を持たせないためである。

<!-- gen:begin snippet split-models-by-role/log-triage-subagent -->
<!-- textlint-disable -->

??? example "雛形：ログの分類を軽いモデルのサブエージェントに任せる例"

    ```markdown
    ---
    name: log-triage
    description: ビルドやテストのログを読み、失敗の種類ごとに件数と代表の行をまとめる。件数の多いログの分類に使う
    tools: Read, Grep, Glob
    model: haiku
    ---

    あなたはログの分類担当である。渡されたログのファイルを読み、失敗の種類（例：型エラー、タイムアウト、依存の解決失敗）ごとに、件数と代表の行（ファイル名と行番号つき）を表にして返す。

    - 原因の推測と修正案は書かない。分類だけを返す
    - 分類できない行は「未分類」にまとめ、件数だけ返す
    - 返す表は 20 行以内にする。長いログの全文は返さない
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet split-models-by-role/log-triage-subagent -->

!!! example "判断例：ログの分類を軽いモデルに任せる"
    - **状況**：毎晩のテストのログが数千行になる。失敗の種類ごとの件数を朝に知りたい。
    - **迷う候補**：本体の会話でそのまま読ませる。軽いモデルのサブエージェントに分類だけ任せる。
    - **選んだもの**：軽いモデルのサブエージェントに分類だけ任せる。
    - **理由**：1 件が単純で件数が多く、結果は grep で抜き取って確かめられる。本体にはうるさい出力が入らない。原因の調査は、分類の結果を見て本体の会話で行う。

## 何に効くか（原理「見せる」と原因「合っていない」） {#what-it-helps}

この分け方は、原因「合っていない」に効く。仕事の重さに対してモデルが過剰でも不足でも、結果か費用が合わなくなる。役割ごとにモデルを合わせると、重い判断に上位のモデルを、軽い作業に軽いモデルを割り当てられる。

原理「見せる」との関係は、分けた側に何を見せるかである。サブエージェントは別の文脈で動くので、見せたものしか知らない（<!-- link:begin subagent-isolation#what-it-helps -->[サブエージェントは別室の部下 › 何に効くか（原理「見せる」と原因「散らかっている」）](../basics/subagent-isolation.md#what-it-helps)<!-- link:end -->）。安いモデルほど、前提を依頼の本文に書いて見せないと、足りない前提を推測で埋めやすい。計画と実装を分けるときも、承認した計画が実装の側に見えている必要がある。

## 誤解しやすい点 {#misconceptions}

- **「分ければ必ず安くなる」**：安くならないことがある。サブエージェントは別の文脈を作るので、トークンは余分にかかる（<!-- link:begin subagent-isolation#cost -->[サブエージェントは別室の部下 › 賢くはならず、費用がかかる](../basics/subagent-isolation.md#cost)<!-- link:end -->）。軽いモデルの手戻りも費用に入る。
- **「サブエージェントは本体と同じ effort で動く」**：別のモデルで動くサブエージェントは、そのモデルの保存した effort か既定で動く。軽いモデルを割り当てたら、effort が本体と違う前提で結果を見る。
- **「上位のモデルは高いので、常に避ける」**：古くなった助言である。一律に避けず、自分の作業で比べて選ぶ。
- **「計画と実装の分業は公式の推奨だ」**：公式の推奨は、効率優先と能力優先の 2 通りの始め方と、モデルより effort を先に調整することである。計画と実装の分業は、公式の `opusplan` が用意する選択肢であり、必ず従う推奨ではない。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)：Anthropic・英語・確認日 2026-11-04
- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [モデルの選び方（三段階）](choosing-a-model.md)
- [サブエージェントは別室の部下](../basics/subagent-isolation.md)

**関連**

- [effort の段階と使い分け › サブエージェントと組織の上限](effort-levels.md#subagents-and-org-limits)
- [plan mode の使いどころ](../cli/when-to-plan.md)
- [サブエージェントの作り方と使いどころ](../extend/writing-subagents.md)
- fast mode と advisor（準備中）
- [現行モデルの一覧と位置づけ](current-models.md)
- [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
