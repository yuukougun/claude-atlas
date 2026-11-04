---
id: current-models
title: 現行モデルの一覧と位置づけ
aliases: [モデルの比較, モデルのラインナップ, Opus と Sonnet の違い, Haiku とは, Fable とは, Mythos とは]
type: comparison
field: models
chapter: モデルを選ぶ
order: 10
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: []
prevents: [合っていない]
pitfalls: []
summary: いま選べるモデルを系統ごとに、得意な仕事・速さ・料金の位置で比べられる。名前や世代より、どの仕事に向くかで覚える。
signs:
  - {type: goal, text: モデルの選択肢が多くて、それぞれ何が違うのか知りたい}
  - {type: situation, text: 新しいモデルの名前を聞いたが、今使っているものとの関係が分からない}
prerequisites: []
related: [choosing-a-model, effort-levels, before-using-top-model, split-models-by-role, model-quirks, large-context-window, after-switching-models, knowledge-cutoff, term-index, change-timeline-2026]
tracks: [model-selection]
outdated_advice: []
sources: [api-docs-models-overview, api-docs-choosing-a-model, api-docs-model-deprecations, anthropic-fable-mythos-5-1, anthropic-opus-5-5, anthropic-sonnet-5-5, anthropic-haiku-5-5, cc-docs-model-config]
volatility: 高
sections:
  - {title: 系統ごとの位置づけ（表）, anchor: lineup}
  - {title: 系統の選び方（判断例）, anchor: how-to-choose}
  - {title: 系統の組み合わせ方, anchor: combine}
  - {title: Fable と Mythos, anchor: fable-and-mythos}
  - {title: 面とプランごとに選べるモデル, anchor: by-surface}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：難しく長い仕事は Fable と Opus、日常の仕事は Sonnet、大量の定型処理は Haiku と、系統の位置で選べる。
    - **いつ引くか**：モデルの選択肢が多くて違いが分からないとき。新しいモデルの名前を聞いたが、今使っているものとの関係が分からないとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：モデルの比較・モデルのラインナップ・Opus と Sonnet の違い・Haiku とは・Fable とは・Mythos とは
<!-- textlint-enable -->

現行モデルの一覧と位置づけは、Claude のモデルを Fable・Opus・Sonnet・Haiku の 4 系統に分け、得意な仕事と、速さ・料金の位置を並べて比べるページである。防ぐ原因は、仕事の重さとモデルが合っていないことだ。名前や世代の数字を覚えるより、どの仕事に向く系統かで覚えるほうが、新しいモデルが出ても迷いにくい。

## 系統ごとの位置づけ（表） {#lineup}

モデルの名前は、系統と世代でできている。系統（Fable・Opus・Sonnet・Haiku）は仕事の位置を示し、数字は世代を示す。新しい名前を聞いたら、まず系統を見て、下の表のどこに当たるかを決める。同じ系統の新しい世代は、おおむね同じ位置を引き継ぐ。世代ごとの違いは公式の発表で確かめる。

| 系統 | 向く仕事 | 速さと料金の位置 |
| --- | --- | --- |
| Fable | 何時間も続く agent、多段の deep research、文書や表やスライドまで仕上げる分析 | 4 系統で最も遅く、最も高い |
| Opus | 何時間も自律で動くコーディング、大規模なリファクタリング、画像が中心の作業、computer use | 中位 |
| Sonnet | 日常的なコーディング、データ分析、コンテンツ作成、ツールを使う agent の作業 | 速く、Opus より安い |
| Haiku | リアルタイム処理、大量処理、サブエージェント、分類・抽出・要約 | 4 系統で最も速く、最も安い |

確認日 2026-10-29（公式の Models overview と、各モデルの発表）。

表の読み方は 3 つある。

- 上の行ほど能力は高いが、遅く、高い。ただし Opus は、公式の発表で、多くの仕事で Fable に近い水準と書かれている。Fable が要る仕事は、Opus で足りなかった仕事に絞られる。
- Sonnet は、範囲が明確な日常の仕事に強い。判断の難しい複雑な仕事は Opus 向けと、公式の発表は分けている。
- Haiku は、複雑な agentic coding では Sonnet や Opus に劣る。大量の定型処理とサブエージェントに置くモデルだ。

型番、API の ID、料金の数値は、公式の [Models overview](https://platform.claude.com/docs/en/models/overview) の表で確かめる。コンテキストウィンドウの広さや知識の期限は、現行の 4 系統で大きく変わらないので、選ぶ決め手にしない。窓の使い方は <!-- link:begin large-context-window#cost-of-long-context -->広いコンテキストウィンドウとの付き合い方 › 長い文脈の費用（準備中）<!-- link:end -->、知識の期限は <!-- link:begin knowledge-cutoff#why -->[知識カットオフと「今」を知らない問題 › なぜ知らないのか](../basics/knowledge-cutoff.md#why)<!-- link:end --> で扱う。

選ぶ順は、このページでなく <!-- link:begin choosing-a-model#three-steps -->[モデルの選び方（三段階） › 三段階：既定 → effort → 上位のモデル](choosing-a-model.md#three-steps)<!-- link:end --> が持つ。既定のモデルで試し、足りなければ <!-- link:begin choosing-a-model#effort-first -->[モデルの選び方（三段階） › モデルより effort を先に動かす理由](choosing-a-model.md#effort-first)<!-- link:end --> のとおり effort を上げ、それでも足りないときだけ上位の系統に替える。モデルを替えた後の見直しは <!-- link:begin after-switching-models#checklist -->[新しいモデルに替えたら見直すこと › 見直す順](after-switching-models.md#checklist)<!-- link:end --> にある。

## 系統の選び方（判断例） {#how-to-choose}

系統は、仕事の重さと量で選ぶ。重い仕事に軽い系統を当てると手戻りが増え、軽い仕事に重い系統を当てると、待ち時間と使用量が増える。迷う組は次のとおり。

!!! example "判断例：大規模なリファクタリングと、小さな修正"
    - **状況**：Claude Code で、数時間かかる大規模なリファクタリングを任せる。同じ日に、文言の直しや小さなバグ修正も数件頼む。
    - **迷う候補**：どちらも最上位の Fable で通す。仕事の重さで系統を分ける。
    - **選んだもの**：リファクタリングは Opus で始め、足りなければ effort を上げてから Fable を試す。小さな修正は Sonnet に任せる。
    - **理由**：Opus は長時間の自律コーディングと大規模なリファクタリング向け、Sonnet は日常のコーディング向けと位置づけられている。最上位の系統は、プランの枠との関係もほかと違い、使用量の減りも速い。使う前の確認は <!-- link:begin before-using-top-model#which-limit -->最上位のモデルを使う前に › どの枠から引かれるか（プランごとの表）（準備中）<!-- link:end --> にある。どちらも筋が通る選び方だが、仕事の重さの差に合わせたほうが、待ち時間と枠を節約できる。

!!! example "判断例：大量の問い合わせの分類"
    - **状況**：問い合わせの文章を数千件、種類ごとに分類したい。判定の基準は決まっていて、1 件ずつの答えは短い。
    - **迷う候補**：精度を見込んで Sonnet から始める。速さと費用を見込んで Haiku から始める。
    - **選んだもの**：Haiku で始め、少数の見本で精度を見る。足りない種類だけを Sonnet に回す。
    - **理由**：公式は、効率を優先するなら Haiku から始め、足りない部分だけ上位に替える始め方を挙げている。判定の基準が決まった大量処理は Haiku の得意な形だ。能力を優先する始め方も筋が通るので、最初の数十件で両方の結果を比べると、決め手が自分の仕事の数字になる。

選んだ後は、体感でなく、自分の作業の結果で確かめる。判断の枠は <!-- link:begin choosing-a-model#examples -->[モデルの選び方（三段階） › 判断例](choosing-a-model.md#examples)<!-- link:end --> にもある。

## 系統の組み合わせ方 {#combine}

1 つの作業の中で、系統を分けて置く方法がある。置き方の目安は次のとおり。

- 計画や難所の判断は、上位の系統（Opus、必要なときだけ Fable）に置く。
- 実装や日常の編集は、Sonnet に置く。
- 大量の読み取り、分類、要約は、Haiku のサブエージェントに置く。

分ける形、分ける価値の判断、軽い系統の使いどころは、別のページが持つ。

- 分ける形：<!-- link:begin split-models-by-role#patterns -->計画・実装・サブエージェントでモデルを分ける › 分ける形（計画と実装・本体とサブエージェント）（準備中）<!-- link:end -->
- 分ける価値があるとき：<!-- link:begin split-models-by-role#when-to-split -->計画・実装・サブエージェントでモデルを分ける › 分ける価値があるとき（準備中）<!-- link:end -->
- 軽い系統の使いどころ：<!-- link:begin split-models-by-role#lighter-models -->計画・実装・サブエージェントでモデルを分ける › 軽いモデルの使いどころ（準備中）<!-- link:end -->

分けた側で動く effort と、引き継がれる文脈は、分けた後に確かめる。effort の既定と段の意味は <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](effort-levels.md#defaults-by-surface)<!-- link:end --> で引く。

系統ごとに出やすい傾向（止まりすぎ、やりすぎ、冗長さなど）は、世代で変わる。プロンプトの合わせ方は <!-- link:begin model-quirks#official-guidance -->モデル別の癖と、プロンプトの合わせ方 › 公式の指針に出てくる傾向（準備中）<!-- link:end --> を見て、自分の環境で観察して記録する。

## Fable と Mythos {#fable-and-mythos}

Fable と Mythos は、同じモデルを、安全装置の強さだけ変えて提供するものである。公式は、同じモデルで安全装置の水準が違うと説明している。

- Fable は一般に提供される。ふつうの利用ではこちらを使う。
- Mythos は、検証の制度を通した組織だけに提供される。提供される範囲は、<!-- fact:begin mythos-availability -->未確認<!-- fact:end -->（公式の発表で確かめる）。

この 2 つは、読者が選び分ける組ではない。ふつうに使えるのは Fable で、Mythos は提供の条件を満たした組織の側の話だ。そのため、このページの系統の表では Fable だけを置き、Mythos は行にしていない。

出力の不可視の透かしは、この 2 つの違いではない。透かしは Fable と Mythos に限らず、対象は、定められた日より後に出たモデルの出力である。透かしの範囲と経緯は Anthropic の説明による。

アプリと Claude Code には、分類器が旗を立てた依頼を別のモデルで答え直す、自動の切り替えがある。これは安全のための仕組みで、モデルの選び方の話ではない。モデルを替えて依頼を通す手段としては扱わない。

## 面とプランごとに選べるモデル {#by-surface}

選べるモデルの一覧は、面とプランで違う。一覧を本文に手で書くと古くなるので、ここでは選び方と、確かめる場所を書く。

=== "アプリ"

    送信ボタンの横のモデルのメニューで選ぶ。メニューに並ぶモデルは、プランで違うことがある。旧世代のモデルは、アプリの選択肢から先に外れ、Claude Code や API にはしばらく残る例がある。外れる前に始めた会話は、後継のモデルが続きを答える場合がある。

    Enterprise の管理者は、役割ごとに使えるモデルを制限できる。メニューに出ないモデルがあるときは、プランと、管理者の設定を先に疑う。最上位の Fable が、プランの枠のどこから引かれるかは <!-- link:begin before-using-top-model#which-limit -->最上位のモデルを使う前に › どの枠から引かれるか（プランごとの表）（準備中）<!-- link:end --> で確かめる。

=== "Claude Code"

    `/model` で切り替え、新しいセッションの既定として保存する。選択画面で `s` を押すと、そのセッションだけに効く。起動時は `--model` で指定する。組織は `availableModels` で、選べるモデルを絞れる。

    各モデルの既定の effort は、面ごとに違う。値は <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](effort-levels.md#defaults-by-surface)<!-- link:end --> の表で引く。

=== "API"

    リクエストにモデルの ID を書いて選ぶ。ID の形と、退役の予定は、公式の [Models overview](https://platform.claude.com/docs/en/models/overview) と [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) で確かめる。たとえば Sonnet 4.5 の退役の予定日は、<!-- fact:begin sonnet-4-5-retirement-date -->未確認<!-- fact:end -->である。退役の日を過ぎたモデルは使えなくなるので、退役の予定があるモデルを固定して使っている場合は、先に後継へ替える。

面やプランの変更は、日付つきで <!-- link:begin change-timeline-2026#timeline -->2026 年の主な変更の年表 › 年表（準備中）<!-- link:end --> に記録される。モデルの名前や旧名から引くときは <!-- link:begin term-index#how-to-read -->[用語索引と旧名の対応 › 引き方](../start/term-index.md#how-to-read)<!-- link:end --> を使う。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [モデルの選び方（三段階）](choosing-a-model.md)

**関連**

- [effort の段階と使い分け](effort-levels.md)
- 最上位のモデルを使う前に（準備中）
- 計画・実装・サブエージェントでモデルを分ける（準備中）
- モデル別の癖と、プロンプトの合わせ方（準備中）
- 広いコンテキストウィンドウとの付き合い方（準備中）
- [新しいモデルに替えたら見直すこと](after-switching-models.md)
- [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)
- [用語索引と旧名の対応](../start/term-index.md)
- 2026 年の主な変更の年表（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Models overview](https://platform.claude.com/docs/en/models/overview)：Anthropic・英語・確認日 2026-11-04
- [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)：Anthropic・英語・確認日 2026-11-04
- [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)：Anthropic・英語・確認日 2026-11-04
- [Introducing Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)：Anthropic・英語・確認日 2026-11-04
- [Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)：Anthropic・英語・確認日 2026-11-04
- [Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)：Anthropic・英語・確認日 2026-11-04
- [Introducing Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)：Anthropic・英語・確認日 2026-11-04
- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
