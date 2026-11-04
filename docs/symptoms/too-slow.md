---
id: too-slow
title: 返事が遅い・時間がかかりすぎる
nav_title: 返事が遅い
aliases: [遅い, 重い, 考え込みすぎる, 待ち時間が長い]
type: symptom
field: symptoms
chapter: 上限と速さ
order: 330
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: 返事が遅い・時間がかかりすぎる原因を、effort とモデル、文脈の重さ、面の違いに分けて切り分け、速さと質のどちらを優先するかを決める。
signs:
  - {type: symptom, text: 返事が返ってくるまで時間がかかりすぎる}
  - {type: symptom, text: 簡単な質問なのに長く考え込む}
  - {type: symptom, text: 入れた拡張が多すぎて重い}
wave: 1
prerequisites: [rereads-whole-history]
related: [how-thinking-works, split-models-by-role, inspect-context, research-in-subagents, thinking-keywords, current-models, when-ai-is-unavailable, hits-limits-quickly, seems-less-capable, six-causes]
routes:
  - {cause: 散らかっている, to: [when-to-start-fresh, always-on-costs, pruning-extensions]}
  - {cause: 合っていない, to: [effort-levels, choosing-a-model, fast-mode-and-advisor]}
tracks: [effort, fast-mode, model-selection, mcp, plugins]
outdated_advice: []
sources: [cc-docs-model-config, api-docs-effort, cc-docs-features-overview, cc-changelog]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 面ごとに見る場所, anchor: by-surface}
  - {title: 原因ごとの対処, anchor: routes}
  - {title: 判断例, anchor: examples}
  - {title: 予防, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：遅さの原因を、会話や常駐物の重さと、effort・モデル・面の合わなさに分けて安い順に調べ、速さと質のどちらを取るか決められる。
    - **いつ引くか**：返事が返ってくるまで時間がかかる、簡単な質問なのに長く考え込む、入れた拡張が多すぎて重い、と感じたとき。
    - **前提**：<!-- link:begin rereads-whole-history -->[毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)<!-- link:end -->

<!-- textlint-disable -->
別名：遅い・重い・考え込みすぎる・待ち時間が長い
<!-- textlint-enable -->

返事が遅いときの原因は、大きく 2 つに分かれる。1 つは文脈が重いこと（散らかっている）で、もう 1 つは effort・モデル・面が作業に合っていないことである。このページでは、2 つを安い順に確かめ、直す先のページへ振り分ける。

## よくある形 {#forms}

遅さの訴えには、読者の言葉で 3 つの形がある。形によって、先に疑う原因が変わる。

- **返事が返ってくるまで時間がかかりすぎる**：会話が長いか、常駐するものが多いと、文脈が重くなる。作業に対して effort が高すぎる場合もある。
- **簡単な質問なのに長く考え込む**：考える深さを決める effort が、作業より高い可能性が高い。直前に重い作業のため上げて、戻し忘れた場合が典型である。
- **入れた拡張が多すぎて重い**：CLAUDE.md・スキル・MCP・プラグインの名前や説明が毎回の入力に乗り、文脈が重くなる。拡張を足していくほど出やすい。

## 原因を安く確かめる順 {#diagnosis}

遅さの原因を、確かめる手間の小さい順に並べた診断である。上から順に、1 つずつ確かめる。人の側の落とし穴は最後に置く。

1. **止まっているだけではないか**：何を見るか。ほかの人や別の面でも同じ依頼が遅いか。どう確かめるか。別の面や別の会話で短い依頼を出す。全体が遅いなら、自分の設定ではなく障害や混雑の可能性がある。止まり方の種類は <!-- link:begin when-ai-is-unavailable#kinds -->AI が使えないときの備え（障害・上限） › 止まり方の種類（障害・上限・規則）（準備中）<!-- link:end --> にある。
2. **散らかっている（会話が長い）**：何を見るか。同じ会話を長く続けていないか。どう確かめるか。同じ依頼を新しい会話で出して、速さが変わるかを見る。Claude は毎回会話の最初から読み直すので、長い会話ほど重くなる。新しくする合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。
3. **散らかっている（常駐するものが多い）**：何を見るか。入れた CLAUDE.md・スキル・MCP・プラグインが、毎回の入力に乗っていないか。どう確かめるか。Claude Code で、新しい会話の直後の内訳を `/context` で見て、常駐するものの占める量を読む。見方は <!-- link:begin inspect-context#baseline -->[/context で中身を見る › 起動直後の基準値](../context/inspect-context.md#baseline)<!-- link:end --> にある。
4. **合っていない（effort が作業より高い）**：何を見るか。いまの effort と、直前に変えたかどうか。どう確かめるか。effort を 1 段下げて、同じ依頼で待ち時間と質を比べる。既定の段はモデルと面で違うので、先に <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](../models/effort-levels.md#defaults-by-surface)<!-- link:end --> で自分の組み合わせの既定を確かめる。「よく考えて」と書き足しても effort は上がらない。書き方による違いは <!-- link:begin thinking-keywords#plain-text-phrases -->[「考えて」と書くことの現在（ultrathink） › 普通の文として渡る言い回し](../models/thinking-keywords.md#plain-text-phrases)<!-- link:end --> にある。
5. **合っていない（モデルが作業に重い）**：何を見るか。上位のモデルへ替えた直後から遅くなっていないか。どう確かめるか。既定のモデルに戻して同じ依頼を試す。選ぶ順は、既定で試し、足りなければ effort を上げ、それでも足りないときだけ上位のモデルである（<!-- link:begin choosing-a-model#three-steps -->[モデルの選び方（三段階） › 三段階：既定 → effort → 上位のモデル](../models/choosing-a-model.md#three-steps)<!-- link:end -->）。
6. **合っていない（サブエージェントの effort が想定と違う）**：何を見るか。本体と違うモデルで動くサブエージェントがないか。どう確かめるか。2026-11 時点の CHANGELOG では、そのようなサブエージェントは、セッションの effort を受け継がず、そのモデルに保存した値か既定の値で動く。本体の effort を下げても、サブエージェント側の待ち時間は変わらないことがある。分け方は <!-- link:begin split-models-by-role#patterns -->計画・実装・サブエージェントでモデルを分ける › 分ける形（計画と実装・本体とサブエージェント）（準備中）<!-- link:end --> にある。
7. **人の側：体感を信じる**：何を見るか。遅いという感覚が、実測と合っているか。どう確かめるか。同じ依頼を、条件を変える前と後で 1 回ずつ流し、待った時間を控える。感覚だけで effort やモデルを動かすと、質を落としたのに速くならない結果もありうる。

## 面ごとに見る場所 {#by-surface}

effort とモデルを確かめる場所は面で違う。固有の詳しい手順は effort の持ち主のページ（<!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](../models/effort-levels.md#how-to-set)<!-- link:end -->）に任せる。

=== "アプリ"

    送信ボタンの横のモデルのメニューで、モデルと effort を選ぶ。選べる段はモデルで違う。

=== "Claude Code"

    `/model` と `/effort` で切り替える。起動時は `--effort` でも決められる。環境変数や設定ファイルにも値があるため、切り替えても効かないときは、どこで決まっているかを確かめる。

=== "API"

    effort はリクエストのパラメーターで決める。指定がなければモデルの既定が使われる。面ごとの既定は <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](../models/effort-levels.md#defaults-by-surface)<!-- link:end --> の表にある。

## 原因ごとの対処 {#routes}

診断で当たった原因ごとに、直す先のページへ進む。散らかっているなら文脈の整理、合っていないなら選び方の見直しである。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 散らかっている | [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<br>[常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)<br>[拡張の棚卸しと剪定](../extend/pruning-extensions.md) |
| 合っていない | [effort の段階と使い分け](../models/effort-levels.md)<br>[モデルの選び方（三段階）](../models/choosing-a-model.md)<br>fast mode と advisor（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

速さが要るが質も落としたくないときは、fast mode と advisor が選択肢になる。どちらも、既定と effort で足りないときに足すものである。

## 判断例 {#examples}

!!! example "判断例：簡単な質問に毎回長く考え込む"
    - **状況**：Claude Code で、ファイル名の確認のような簡単な質問にも毎回長く考え込む。難しい設計の相談をした日に effort を上げたまま、戻していなかった。
    - **迷う候補**：小さなモデルに替える。または、effort を下げる。
    - **選んだもの**：effort を下げる。
    - **理由**：先に動かすのは effort で、モデルの交換は最後である。モデルを替えると質の差まで一緒に動く。effort だけなら、待ち時間と質への効きを同じ依頼で比べやすい。理由は <!-- link:begin choosing-a-model#effort-first -->[モデルの選び方（三段階） › モデルより effort を先に動かす理由](../models/choosing-a-model.md#effort-first)<!-- link:end --> にある。

## 予防 {#prevention}

遅さは、直したあとに戻りやすい。戻らないよう、確認と片付けの習慣に移す。

- **既定を決めておく**：作業の重さごとに effort を決め、重い作業の後は戻す。重い調査は、別の文脈で行わせて要約だけ受け取る（<!-- link:begin research-in-subagents#when -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 任せてよい調査、本筋で読むべきもの](../context/research-in-subagents.md#when)<!-- link:end -->）。
- **常駐するものを定期的に棚卸しする**：測ってから切る。測り方と切る基準は <!-- link:begin pruning-extensions#measure -->[拡張の棚卸しと剪定 › 測る](../extend/pruning-extensions.md#measure)<!-- link:end --> にある。
- **長い会話を続けない**：話題が変わったら新しくする。常駐を小さく保つ理由は <!-- link:begin always-on-costs#why-small -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › なぜ常駐を小さく保つのか](../context/always-on-costs.md#why-small)<!-- link:end --> にある。
- **質が落ちたと感じたら別症状として切り分ける**：速さを優先して設定を下げた後の質の低下は <!-- link:begin seems-less-capable -->[急に賢くなくなった気がする](seems-less-capable.md)<!-- link:end --> で確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)

**次に読む**

- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [拡張の棚卸しと剪定](../extend/pruning-extensions.md)
- [effort の段階と使い分け](../models/effort-levels.md)
- [モデルの選び方（三段階）](../models/choosing-a-model.md)
- fast mode と advisor（準備中）

**関連**

- [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- 計画・実装・サブエージェントでモデルを分ける（準備中）
- [/context で中身を見る](../context/inspect-context.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)
- [「考えて」と書くことの現在（ultrathink）](../models/thinking-keywords.md)
- [現行モデルの一覧と位置づけ](../models/current-models.md)
- AI が使えないときの備え（障害・上限）（準備中）
- [すぐ上限に当たる](hits-limits-quickly.md)
- [急に賢くなくなった気がする](seems-less-capable.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
