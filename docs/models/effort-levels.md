---
id: effort-levels
title: effort の段階と使い分け
aliases: [努力レベル, /effort, 推論の量, thinking のオンとオフ]
type: feature
field: models
chapter: effort・思考・コンテキスト
order: 40
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [合っていない]
pitfalls: []
summary: effort で、考える深さとツールの使い方・待ち時間・使用量の釣り合いを変えられる。既定の段を確かめてから、作業に合わせて上げ下げする。
signs:
  - {type: goal, text: 返答をもっと深く考えさせたい}
  - {type: goal, text: 簡単な作業では、深く考えさせずに速く済ませたい}
  - {type: situation, text: アプリと Claude Code と API で、同じモデルなのに振る舞いが違う気がする}
prerequisites: [how-thinking-works]
related: [choosing-a-model, thinking-keywords, suspected-degradation, too-slow, after-switching-models, split-models-by-role, fast-mode-and-advisor, what-uses-up-limits, search-research-thinking, measure-changes]
tracks: [effort, adaptive-thinking]
outdated_advice: [budget-tokens]
sources: [api-docs-effort, hc-effort-settings, cc-docs-model-config, cc-docs-settings-reference, cc-docs-sub-agents, api-docs-thinking, cc-changelog]
volatility: 高
sections:
  - {title: 段ごとの振る舞い, anchor: levels}
  - {title: 既定の段（モデル × 面の表）, anchor: defaults-by-surface}
  - {title: 面ごとの変え方, anchor: how-to-set}
  - {title: サブエージェントと組織の上限, anchor: subagents-and-org-limits}
  - {title: thinking の切り替え, anchor: thinking-toggle}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated-advice}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：effort で、考える深さとツールの使い方・待ち時間・使用量の釣り合いを変えられる。
    - **いつ引くか**：返答をもっと深く考えさせたいとき。簡単な作業を深く考えさせずに速く済ませたいとき。アプリと Claude Code と API で、同じモデルなのに振る舞いの違いを感じるとき。
    - **成熟度**：<!-- gen:begin feature maturity -->GA<!-- gen:end feature maturity -->。
    - **強制力**：<!-- gen:begin feature enforcement -->なし<!-- gen:end feature enforcement -->。何も止めない。考え方の傾向を変える設定であり、禁止や上限の仕組みではない。
    - **前提**：<!-- link:begin how-thinking-works -->[思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)<!-- link:end -->

<!-- textlint-disable -->
別名：努力レベル・/effort・推論の量・thinking のオンとオフ
<!-- textlint-enable -->

effort は、Claude が 1 回の依頼にどれだけ力を使うかを段で決める設定である。防ぐ原因は、作業の重さと段が合っていないことだ。重い作業が浅く済まされることも、軽い作業が深く考えられて遅く高くつくことも、この設定で直せる。まず今の段を確かめ、次に作業に合わせて 1 段ずつ動かす。

## 段ごとの振る舞い {#levels}

effort の段は、トークンの厳密な予算ではなく、振る舞いの合図である。段を上げると、考える量だけでなく、ツールを呼ぶ回数、行動の前に計画を説明するかどうか、最後のまとめの詳しさも変わる。その分、待ち時間と使用量が増える。

低い段では、ツール呼び出しが減り、前置きなしで動く。高い段では、計画を説明してから動き、詳しくまとめる。簡単な依頼なら、高い段でも考える量は少ないままのことがある。段は目標の高さを伝えるもので、毎回その量を使うという約束ではない。

| 段 | 向く作業 | 傾向 |
| --- | --- | --- |
| low | すぐ確認する短いやり取り。サブエージェント。速さと費用を優先する作業 | 速く安い。ツール呼び出しが少なく、前置きなしで動く |
| medium | 範囲の明確な日常の作業 | 速さと深さの釣り合い |
| high | バグ修正のように、検証が重要な作業。複雑な推論や難しいコーディング | 計画を説明し、確かめながら進める |
| xhigh | より深い推論が要る作業。長時間の agentic な作業 | 深いが、待ち時間と使用量が大きい |
| max | 難問。正確さが最優先の作業 | 過剰に考えたり、効果が頭打ちになったりする場合がある。試してから採用する |

選べる段の種類はモデルで違う。モデルが対応していない段を指定すると、Claude Code は、そのモデルで使える段のうち、指定より下で最も高いものを使う（2026-11-05 に Model configuration で確認）。

最初の目安は、日常の作業を既定で始め、難所だけを上げることだ。上げた効果は、体感でなく、自分の作業で確かめる。確かめ方は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> を使う。劣化かどうか疑っているときは <!-- link:begin suspected-degradation#measure -->[劣化を疑ったら測って確かめる › 版と effort を記録して、同じ課題で比べる](suspected-degradation.md#measure)<!-- link:end --> のとおり、版と effort を記録して同じ課題で比べる。

!!! example "判断例：バグの修正と、ログの読み取り"
    - **状況**：Claude Code で、再現しにくいバグの修正を頼む。同じセッションで、長いテスト出力から失敗の行だけを拾う作業も頼む。
    - **迷う候補**：全部を同じ高い段で通す。作業ごとに段を変える。
    - **選んだもの**：バグの修正は high から始め、足りなければ xhigh を試す。ログの読み取りは low のサブエージェントに任せる。
    - **理由**：バグの修正は検証が要るので、考える量とツール呼び出しの多さが結果に効く。ログの拾い出しは判断が少なく、待ち時間のほうが費用になる。どちらも筋が通る選択だが、作業の重さの差に段を合わせたほうが、遅さと使用量を抑えられる。

## 既定の段（モデル × 面の表） {#defaults-by-surface}

既定の段は、モデルごとに違い、面ごとにも違う。同じモデルでも、API とアプリと Claude Code で、何も選ばずに使ったときの段は異なる場合がある。振る舞いの違いを感じたら、モデルを疑う前に、まず面ごとの既定を確かめる。

面で違う理由は、既定を決める場所が別だからである。API は、リクエストに段を書かなければ、モデルの既定が効く。Claude Code とアプリは、製品の側が選んだ段をリクエストに入れて送る。Claude Code を、段を送らない設定にすると、API の既定が効く。

Claude Code の段は、最初に当てはまったものが採られる。順は次のとおりだ（2026-11-05 に Model configuration で確認）。

1. 環境変数 `CLAUDE_CODE_EFFORT_LEVEL`
2. セッションの中で `/effort` か `/model` のメニューで選んだ段
3. 起動時の `--effort`
4. 設定に保存した、モデルごとの段か、`effortLevel`
5. モデルの既定

組織が既定のモデルの段を決めていれば、それが既定になる。ユーザー設定の一番上の `effortLevel` は、モデルごとに段を保存する新しいモデルには効かない。そのモデルには `modelSettings` で書く。環境変数を `auto` か `unset` にすると、Claude Code は段を送らず、API の既定が効く。

各モデルの既定の値は、変わりやすいので、下の表のとおり。公式の Models overview（API）、Model configuration（Claude Code）、各モデルの発表（アプリ）で確かめる。公式の Help Center は、アプリのメニューで各モデルの推奨の段に「Default」と表示するとだけ書き、値の一覧は載せていない。

<!-- gen:begin fact-table effort-default-by-model-surface -->
<!-- textlint-disable -->

| モデル | API | Claude Code | アプリ |
| --- | --- | --- | --- |
| Fable 5.1 | high | high | medium（claude.ai と Cowork。Fable 5.1 の発表） |
| Opus 5.5 | medium | medium | —（文書に面ごとの値はない。発表は「既定（medium）」とだけ書く） |
| Sonnet 5.5 | high | medium | medium（Sonnet 5.5 の発表。Claude Code とアプリは medium、Claude Platform は high） |
| Haiku 5.5 | medium | medium | —（値を書いた文書は見つけていない） |
| Sonnet 5 | high | high | —（値を書いた文書は見つけていない） |
| Opus 4.7 | high | xhigh | —（値を書いた文書は見つけていない） |
| Fable 5・Opus 5・Opus 4.8・Opus 4.6・Sonnet 4.6 | high | high | —（値を書いた文書は見つけていない） |

確認日 2026-11-03。出典：[Models overview](https://platform.claude.com/docs/en/models/overview)、[Effort](https://platform.claude.com/docs/en/build-with-claude/effort)、[Model configuration](https://code.claude.com/docs/en/model-config)、[Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)、[Introducing Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)、[Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)、[Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)。

<!-- textlint-enable -->
<!-- gen:end fact-table effort-default-by-model-surface -->

!!! example "判断例：同じモデルなのに、返答の深さが違う"
    - **状況**：同じモデルで同じ依頼をしたのに、アプリでは浅く、API では深く考えているように見える。
    - **迷う候補**：モデルの版が違うと考える。面ごとの既定の段が違うと考える。
    - **選んだもの**：先に、双方の段を確かめる。アプリは送信ボタンの横のメニュー、Claude Code は `/effort`、API はリクエストの `output_config.effort` を見る。
    - **理由**：段は面ごとに別の場所で決まるので、モデルが同じでも既定は揃わない。段をそろえてから比べないと、モデルの差と段の差を見分けられない。

## 面ごとの変え方 {#how-to-set}

段を変える手段は面ごとに違う。どの面でも、変えたら新しいやり取りで効果を確かめる。

=== "アプリ"

    送信ボタンの横のモデルのメニューから、段を選ぶ。段は Low・Medium・High・Extra high・Max で、モデルが対応する段だけが出る。各モデルの推奨の段には「Default」と表示される。変更は次の応答から効く。

    日常の用途は既定で足りる。複雑な作業は段を上げるか、thinking をオンにする。Max は、最も難しく、正確さが重要な作業だけにする。高い段ほど、時間もトークンも多く使う。

    Enterprise の管理者は、役割ごとに使えるモデルや段を制限でき、新しいチャットの最初のモデルと段も決められる。自分のメニューに出ない段があるときは、まず管理者の設定を疑う。

=== "Claude Code"

    - `/effort` を引数なしで実行すると、スライダーが開く。`/effort high` のように段の名前を付けると直接設定する。`/effort status` で今の段を見る。
    - `/effort auto` は、今のモデルに保存した段を消し、モデルの既定に戻す。
    - `--effort` で、起動した 1 回のセッションだけ段を決める。
    - 設定の `effortLevel` は、個別の保存がないモデルの既定の段になる。モデルごとの段は `modelSettings` に書く。設定には `max` を書けない。
    - スキルとサブエージェントは、`effort` をフロントマターに書ける。実行中は、起動時や保存や選択の段より優先される。

=== "API"

    リクエストの `output_config.effort` に段を書く。ベータ用のヘッダーは要らない。書かなければ、モデルの既定が効く。

    ```python
    response = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": "..."}],
        output_config={"effort": "medium"},
    )
    ```

    高い段では、考える分も含めて出力が長くなるので、`max_tokens` を大きく取る。新しいモデルに替えたときは、古い設定を持ち越さず、自分の評価で段を振って確かめる。

Claude Code の設定の例を次に示す。モデルの名前は、自分が使うモデルに替える。モデルごとの保存には、<!-- fact:begin effort-model-settings-min-version -->Claude Code 2.1.251 以降（2026-11-05 時点）<!-- fact:end -->が要る。

<!-- gen:begin snippet effort-levels/model-effort-settings -->
<!-- textlint-disable -->

??? example "雛形：モデルごとの effort を設定に書く例"

    ```json
    {
      "modelSettings": {
        "claude-opus-5-5": {
          "effortLevel": "high"
        }
      }
    }
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet effort-levels/model-effort-settings -->

## サブエージェントと組織の上限 {#subagents-and-org-limits}

サブエージェントの段は、本体の段をそのまま引き継ぐとは限らない。サブエージェントの `effort` のフロントマターがあれば、それが動いている間は優先される。`CLAUDE_CODE_SUBAGENT_EFFORT` は、ほかに指定がないときにサブエージェントが動く段を決める環境変数である。

本体と別のモデルで動くサブエージェントやチームメイトは、セッションの段を受け継がない。そのモデルに保存した段か、そのモデルの既定の段で動く。この挙動は <!-- fact:begin subagent-own-model-effort-min-version -->未確認<!-- fact:end --> で入った。これは Claude Code の CHANGELOG による（2026-11-03 に確認）。サブエージェントの文書には、この記述がまだない。チームの文書には「リーダーの段を引き継ぐ」と読める記述があり、合わない場合がある。挙動を確かめるまで、別のモデルを割り当てたサブエージェントの段は、既定だと見ておく。

軽いモデルをサブエージェントに割り当てると、そのサブエージェントはそのモデルの既定の段で動く。軽くて速い作業で段をさらに `low` に固定したいときは、次の雛形のように `effort` を書く。モデルを分ける判断は <!-- link:begin split-models-by-role#patterns -->[計画・実装・サブエージェントでモデルを分ける › 分ける形（計画と実装・本体とサブエージェント）](split-models-by-role.md#patterns)<!-- link:end --> にある。

<!-- gen:begin snippet effort-levels/low-effort-subagent -->
<!-- textlint-disable -->

??? example "雛形：軽い作業のサブエージェントに低い effort を付ける例"

    ```markdown
    ---
    name: log-summarizer
    description: ログやテスト出力を読み、失敗した行と直近の変更だけを短くまとめる。長い出力を本体の会話に持ち込みたくないときに使う
    effort: low
    ---

    渡されたログやテスト出力を読み、次の 3 点だけを返す。

    - 失敗した項目の名前
    - その失敗に関係する行（原文のまま、最大 10 行）
    - 直前に変えたファイルとの関係が分かれば、その 1 行

    原因の推測や修正案は書かない。判断は呼び出した側が行う。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet effort-levels/low-effort-subagent -->

組織は、段に上限をかけられる。Claude Code では 2 つの手段がある。

- Enterprise の管理者が、役割ごと、モデルごとに最大の段を決める。上限より上の段は `/effort` に出ず、それより高い要求は上限の段で動く。
- 管理設定の `maxEffortLevel` は、プランやプロバイダーを問わず、クライアントで段を制限する。

両方が効くときは、低いほうの上限が使われる。上限はモデルごとなので、モデルを替えると選べる段が変わる。自分が選んだはずの段で動いていないときは、上限を疑い、`/effort status` で実際の段を見る。上限より高い段を設定に書いていると、以前の版では "Invalid effort level" で失敗し続けることがあった。新しい版では、段を下げて再試行し、使った段を知らせる。

## thinking の切り替え {#thinking-toggle}

thinking は、答える前にどれだけ考えるかの仕組みで、effort はその深さを変える主な操作である。仕組みは <!-- link:begin how-thinking-works -->[思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)<!-- link:end --> にある。考えた分は画面に出なくても出力として数えられ、費用と上限に入る。画面に出る要約は、考えた過程の全文とは限らない。

新しいモデルの多くは、Claude が必要に応じて考える量を決める adaptive thinking だけを持つ。この種のモデルには、thinking を切れないものがある。切れるかどうかはモデルごとに違うので、切り替えを試す前に確かめる。

=== "アプリ"

    モデルのメニューに、thinking の切り替えが出るモデルがある。effort を持つモデルでは「Thinking」、それ以外では「Extended」と表示される。thinking を切れないモデルでは、アプリからオフにできない。

=== "Claude Code"

    - `Option+T`（Windows と Linux は `Alt+T`）で、そのセッションだけ切り替える。
    - `/config` の thinking mode が、全体の既定を決める。設定には `alwaysThinkingEnabled` として保存される。
    - `MAX_THINKING_TOKENS=0` で、Anthropic の API を使うときに thinking を切れる。
    - thinking を切れないモデルでは、`alwaysThinkingEnabled: false` も `MAX_THINKING_TOKENS=0` も効かない。

=== "API"

    adaptive thinking を使い、深さは effort で決める。一部のモデルでは、`thinking` を `disabled` にした要求が、どの段でも 400 エラーになる。手動の予算 `budget_tokens` は、新しい世代では使えない。

## 効かない場面・落とし穴 {#pitfalls}

効かない場面は、依頼そのものが合っていないときである。目的や完了条件が曖昧な依頼を、段を上げて直そうとしても、深く考えた末に曖昧な結果が返るだけになる。段を上げる前に、依頼を具体にする。

落とし穴は次のとおりだ。

- **段は厳密な予算ではない。** 同じ段でも、依頼しだいで使う量は大きく変わる。使用量を確実に抑える手段としては使えない。上限を早く使う要因は <!-- link:begin what-uses-up-limits#causes -->[上限を早く使う要因 › 枠を早く減らす原因](../cost/what-uses-up-limits.md#causes)<!-- link:end --> で、自分の場合は <!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> で確かめる。
- **max の常用。** 最高の段は、過剰に考えて逆効果になる場合がある。待ち時間も費用になる。先に低い段で試し、足りないときだけ上げる。
- **段の持ち越し。** モデルを替えたら、前のモデルで決めた段をそのまま使わない。新しいモデルの既定から始める。見直す順は <!-- link:begin after-switching-models#checklist -->[新しいモデルに替えたら見直すこと › 見直す順](after-switching-models.md#checklist)<!-- link:end --> にある。
- **体感で判断する。** 「浅くなった」「遅くなった」と感じたときは、版と段を記録して、同じ課題で比べる。
- **遅さの原因を段だけに見る。** 遅いときの原因は段のほかに、文脈の重さや面の違いもある。切り分けは <!-- link:begin too-slow#diagnosis -->[返事が遅い・時間がかかりすぎる › 原因を安く確かめる順](../symptoms/too-slow.md#diagnosis)<!-- link:end --> にある。
- **言葉で段を上げようとする。** 「よく考えて」と書いても、段は上がらない。段は設定で決める。

## 比べる相手 {#compare}

effort と並べて考える手段は、効く場所が違う。

- **モデルを替える。** 選ぶ順は、既定で試し、足りなければ effort を上げ、それでも足りないときだけ上位のモデルにする。理由は <!-- link:begin choosing-a-model#effort-first -->[モデルの選び方（三段階） › モデルより effort を先に動かす理由](choosing-a-model.md#effort-first)<!-- link:end --> にある。
- **プロンプトに考えさせる言葉を書く。** 普通の文として渡るだけで、effort は上がらない。1 回だけ深く考えさせる手段もある。使い分けは <!-- link:begin thinking-keywords#plain-text-phrases -->[「考えて」と書くことの現在（ultrathink） › 普通の文として渡る言い回し](thinking-keywords.md#plain-text-phrases)<!-- link:end --> と <!-- link:begin thinking-keywords#ultrathink -->[「考えて」と書くことの現在（ultrathink） › ultrathink の使いどころ](thinking-keywords.md#ultrathink)<!-- link:end --> にある。
- **fast mode と advisor。** 速さを料金と引き換えに得る手段と、要所だけ別のモデルに助言させる手段である。既定と effort で足りないときに足す。<!-- link:begin fast-mode-and-advisor#fast-mode -->fast mode と advisor › fast mode（準備中）<!-- link:end --> を見る。
- **軽いモデルをサブエージェントに使う。** 仕事の重さの差が大きいときは、段でなくモデルで分ける。<!-- link:begin split-models-by-role#lighter-models -->[計画・実装・サブエージェントでモデルを分ける › 軽いモデルの使いどころ](split-models-by-role.md#lighter-models)<!-- link:end --> を見る。
- **web 検索やリサーチ。** 考える深さでなく、調べる範囲や最新の情報が要るかで選ぶ。<!-- link:begin search-research-thinking#comparison -->[web 検索・リサーチ・拡張思考の使い分け › 三つの使い分け](../app/search-research-thinking.md#comparison)<!-- link:end --> を見る。

## 古くなった助言 {#outdated-advice}

「`budget_tokens` で思考量を指定する」は、新しい世代のモデルでは通らない助言になった。今は thinking の種類を adaptive にして、深さを effort で決める。新しい世代のモデルは、`budget_tokens` を使う要求を 400 エラーで断る。台帳の行は <!-- link:begin outdated-advice-ledger#budget-tokens -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#budget-tokens)<!-- link:end --> にある。

自分の API を呼ぶコードで、`budget_tokens` と、`thinking` の種類が `enabled` の要求を探す。手動の思考しか持たない古いモデルは、そのままで構わない。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)：Anthropic・英語・確認日 2026-11-04
- [Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)：Anthropic・英語・確認日 2026-11-04
- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)

**次に読む**

- [「考えて」と書くことの現在（ultrathink）](thinking-keywords.md)
- [劣化を疑ったら測って確かめる](suspected-degradation.md)
- [新しいモデルに替えたら見直すこと](after-switching-models.md)
- fast mode と advisor（準備中）

**関連**

- [モデルの選び方（三段階）](choosing-a-model.md)
- [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)
- [計画・実装・サブエージェントでモデルを分ける](split-models-by-role.md)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)
- [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
