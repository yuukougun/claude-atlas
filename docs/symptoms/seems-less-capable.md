---
id: seems-less-capable
title: 急に賢くなくなった気がする
aliases: [劣化した, 性能が落ちた, 前よりバカになった, 調子が悪い]
type: symptom
field: symptoms
chapter: 上限と速さ
order: 340
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる, 見せる]
prevents: [散らかっている, 合っていない]
pitfalls: [体感を信じる]
scenes: [開発, 文章]
summary: 急に賢くなくなった気がするときに、版・effort・モデル・会話の量の順に確かめ、体感ではなく同じ課題で比べて判断する。
signs:
  - {type: symptom, text: 急に性能が落ちた気がする}
  - {type: symptom, text: 前は一度でできたことができなくなった}
  - {type: symptom, text: 更新の後から答えが雑になった気がする}
wave: 1
prerequisites: [nondeterminism]
related: [current-models, choosing-a-model, context-rot, always-on-costs, harness-over-model, insights-and-usage-review, change-timeline-2026, checking-for-updates, human-pitfalls, forgets-in-long-chats, too-slow, six-causes]
routes:
  - {cause: 散らかっている, to: [when-to-start-fresh, inspect-context, isolate-with-safe-mode]}
  - {cause: 合っていない, to: [suspected-degradation#official-sources, effort-levels, after-switching-models]}
  - {cause: 体感を信じる, to: [suspected-degradation#measure, felt-vs-measured, measure-changes]}
tracks: [model-selection, effort, context-window]
outdated_advice: [think-hard-keywords]
sources: [api-docs-effort, cc-docs-model-config, cc-docs-commands, hc-effort-settings, cc-docs-context-window, anthropic-research-april-23-postmortem]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: routes-to-fixes}
  - {title: 判断例, anchor: example}
  - {title: 古い助言に引きずられない, anchor: outdated}
  - {title: 予防：記録を残して差を測れるようにする, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：版・effort・モデル・会話の量の順に確かめ、体感ではなく同じ課題で比べて、落ちたのか、何が変わったのかを切り分けられる。
    - **いつ引くか**：性能が落ちた、前は一度でできたことができない、更新の後から雑になった、と感じたときに引く。
    - **前提**：<!-- link:begin nondeterminism -->[同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)<!-- link:end -->

<!-- textlint-disable -->
別名：劣化した・性能が落ちた・前よりバカになった・調子が悪い
<!-- textlint-enable -->

急に賢くなくなった気がするとは、同じような依頼なのに、前より答えが浅い、または雑だと感じる状態である。原因は Claude の能力そのものとは限らない。条件が変わっている場合も、感じ方がずれている場合もある。このページは、確かめるのが安い順に原因を並べ、どこへ進むかを決める。

## よくある形 {#forms}

読者の言葉では、次の 3 つの形で現れる。どれも、最初に確かめることは同じである。

- 急に性能が落ちた気がする：昨日までと同じ作業なのに、質が違うと感じる。まず、版・effort・モデルのどれかが変わっていないかを見る。
- 前は一度でできたことができなくなった：以前の成功は 1 回の結果だったことが多い。同じ頼み方でも答えが毎回少し変わるので、1 回ずつの成否では差が言えない。理由は <!-- link:begin nondeterminism#what-happens -->[同じ質問でも答えが変わる（非決定性） › 何が起きるか](../basics/nondeterminism.md#what-happens)<!-- link:end --> にある。
- 更新の後から答えが雑になった気がする：更新で既定の値や設定の効き方が変わったのかもしれない。版の変更履歴と、effort の既定を見る。

長い会話の途中で雑になるなら、<!-- link:begin forgets-in-long-chats#diagnosis -->[長い会話で前提を忘れる・雑になる › 原因を安く確かめる順](forgets-in-long-chats.md#diagnosis)<!-- link:end --> を先に当たる。返事が遅いだけなら、<!-- link:begin too-slow#diagnosis -->[返事が遅い・時間がかかりすぎる › 原因を安く確かめる順](too-slow.md#diagnosis)<!-- link:end --> に進む。症状が決まらないときの入口は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> にある。

## 原因を安く確かめる順 {#diagnosis}

診断は、手間の少ない確認から順に進める。順は、版、effort、モデル、会話の量、最後に判断のしかたである。最初に、前にうまくいった作業と、今うまくいかない作業を 1 つずつ決める。決めないと、以下の確認を当てられない。

1. **版が変わった**（合っていない）
    - 見るもの：前にうまくいった時から、Claude Code・アプリ・モデルの版が変わっていないか。製品の側で既定が変わっていないか。
    - 確かめ方：今の版を控え、変更履歴の該当の期間を読む。公式の報告・変更履歴・稼働状況の確かめ先は <!-- link:begin suspected-degradation#official-sources -->[劣化を疑ったら測って確かめる › 製品の側の変更を確かめる先（公式の報告・変更履歴・稼働状況）](../models/suspected-degradation.md#official-sources)<!-- link:end --> にある。変更履歴の読み方と古い書き方の点検は <!-- link:begin checking-for-updates -->最新を自分で確かめる方法（準備中）<!-- link:end --> に、主な変更の時系列は <!-- link:begin change-timeline-2026#timeline -->2026 年の主な変更の年表 › 年表（準備中）<!-- link:end --> にある。既定の effort が製品の側で下げられ、品質の不満の後に戻された例は <!-- link:begin suspected-degradation#postmortem-example -->[劣化を疑ったら測って確かめる › 製品の側の変更だった例](../models/suspected-degradation.md#postmortem-example)<!-- link:end --> にある。
2. **effort が違う**（合っていない）
    - 見るもの：今の effort の段と、前に使っていた段。モデルを替えたあとに、前のモデル向けの段を持ち越していないか。
    - 確かめ方：今の段を見て、前の記録と並べる。既定の段は面とモデルで違い、時期によっても変わってきた。値は <!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](../models/effort-levels.md#defaults-by-surface)<!-- link:end --> にある。環境変数や設定で段を決めている場合は、既定よりそちらが優先される。変える場所は <!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](../models/effort-levels.md#how-to-set)<!-- link:end --> にある。モデルを替えたあとの見直しの順は <!-- link:begin after-switching-models#checklist -->[新しいモデルに替えたら見直すこと › 見直す順](../models/after-switching-models.md#checklist)<!-- link:end --> にある。
3. **モデルが違う**（合っていない）
    - 見るもの：今のモデルと、前に使っていたモデル。既定のモデルが変わっていないか。
    - 確かめ方：今のモデルを見て、可能なら前のモデルで同じ課題を流す。替える順は、既定で試し、足りなければ effort を上げ、それでも足りないときだけ上位のモデルに替える。理由は <!-- link:begin choosing-a-model#effort-first -->[モデルの選び方（三段階） › モデルより effort を先に動かす理由](../models/choosing-a-model.md#effort-first)<!-- link:end --> にある。いま選べるモデルは <!-- link:begin current-models#lineup -->[現行モデルの一覧と位置づけ › 系統ごとの位置づけ（表）](../models/current-models.md#lineup)<!-- link:end --> に、既定の変化や退役への気づき方は <!-- link:begin after-switching-models#retirements-and-default-changes -->[新しいモデルに替えたら見直すこと › 退役と既定の変化に気づく](../models/after-switching-models.md#retirements-and-default-changes)<!-- link:end --> にある。差がモデルでなく、検証の手段・渡す文脈・指示から来る場合もある。見分け方は <!-- link:begin harness-over-model#when-harness-matters -->モデルの差よりハーネスの差 › 差がハーネスから来るとき（準備中）<!-- link:end --> にある。
4. **会話が散らかっている**（散らかっている）
    - 見るもの：会話の長さ、話題の混在、失敗した試みの跡、毎回読み込まれる常駐のもの（CLAUDE.md・スキル・MCP など）。
    - 確かめ方：今の依頼に要る前提と資料だけを書き出して新しい会話に入れ、同じ依頼を出す。答えがよくなるなら、散らかりが原因である。新しい会話にする合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。紛らわしい情報が答えの質を下げる理由は <!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end --> にある。自分の設定（CLAUDE.md・スキル・MCP など）が原因かを、設定を外して同じ依頼で比べる手は、<!-- link:begin isolate-with-safe-mode#compare -->設定を外して切り分ける（--safe-mode） › 比べ方（準備中）<!-- link:end --> にある。
5. **体感だけで判断している**（人の側の落とし穴：体感を信じる）
    - 見るもの：「前は良かった」の根拠が、記憶だけになっていないか。前の課題と今の課題が同じ難しさか。
    - 確かめ方：同じ課題を、条件を揃えて何度か流して比べる。体感が実測とずれる理由は <!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end --> に、記録の取り方は <!-- link:begin suspected-degradation#measure -->[劣化を疑ったら測って確かめる › 版と effort を記録して、同じ課題で比べる](../models/suspected-degradation.md#measure)<!-- link:end --> にある。人の側の落とし穴の全体は <!-- link:begin human-pitfalls#five-pitfalls -->[人の側の五つの落とし穴（総論） › 五つの落とし穴の一覧](../judgment/human-pitfalls.md#five-pitfalls)<!-- link:end --> にある。

版・モデル・effort・会話の量は、面によって見る場所が違う。

=== "アプリ"

    モデルと effort は、送信ボタンの横のモデルのメニューで見る。アプリ自体の版の見方と、更新が入った日は未確認である。会話が長いときは、新しい会話で同じ依頼を出して比べる。

=== "Claude Code"

    `claude --version` で版を、`/model` でモデルを、`/effort` で effort を見る。`/context` で、会話・読み込んだファイル・常駐するもののどれが場所を取っているかを見分ける。見方は <!-- link:begin inspect-context#reading -->[/context で中身を見る › 内訳の読み方](../context/inspect-context.md#reading)<!-- link:end --> にある。WSL・Linux の CLI を基準にした説明で、ほかの OS と IDE 拡張の画面は未確認である。

=== "API"

    呼び出しの設定に書いた model と effort の値を、結果と一緒にログに残す。指定していない項目は既定が効くので、既定が変わると結果が変わりうる。会話の履歴は呼び出す側のコードが組み立てるので、送った内容そのものを確かめる。

前と今を並べて違う項目を見つけるための記録票を、次に置く。

<!-- gen:begin snippet seems-less-capable/compare-record -->
<!-- textlint-disable -->

??? example "雛形：劣化の疑いを並べて記録する票"

    ```text
    劣化の疑いの記録（前にうまくいった時と、今を並べる）

    [前にうまくいった時]
    日付：
    面（app / claude-code / api）：
    版（Claude Code の版、アプリの更新日など）：
    モデル：
    effort：
    会話の状態（新しい会話か、続きか。長さ）：
    常駐するもの（CLAUDE.md・MCP・スキルなど）：

    [今]
    日付：
    面：
    版：
    モデル：
    effort：
    会話の状態：
    常駐するもの：

    課題（入力を固定する）：
    成功の基準（通る・通らないで言えるように）：
    試行の回数と結果（前の条件／今の条件）：
    違う項目（1 つに絞って、もう一方に合わせて流し直す）：
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet seems-less-capable/compare-record -->

違う項目が見つかったら、1 つだけ前に合わせて、同じ課題を流し直す。結果が戻れば、その項目が差の原因である。戻らなければ、次の項目に移る。

## 原因ごとの対処 {#routes-to-fixes}

診断で当たった原因に対応する対処は、次の表のページにある。このページは切り分けまでを受け持ち、対処の本体は書かない。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 散らかっている | [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<br>[/context で中身を見る](../context/inspect-context.md)<br>設定を外して切り分ける（--safe-mode）（準備中） |
| 合っていない | [劣化を疑ったら測って確かめる › 製品の側の変更を確かめる先（公式の報告・変更履歴・稼働状況）](../models/suspected-degradation.md#official-sources)<br>[effort の段階と使い分け](../models/effort-levels.md)<br>[新しいモデルに替えたら見直すこと](../models/after-switching-models.md) |
| 体感を信じる | [劣化を疑ったら測って確かめる › 版と effort を記録して、同じ課題で比べる](../models/suspected-degradation.md#measure)<br>[体感と実測](../eval/felt-vs-measured.md)<br>[変更が効いたかを測る（小さな eval）](../eval/measure-changes.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

どの原因にも当たらないときは、<!-- link:begin insights-and-usage-review#usage-breakdown -->/insights と /usage で振り返る › /usage の内訳から削るものを選ぶ（準備中）<!-- link:end --> で使い方の内訳を見直す手もある。出てきた提案は、判断ではなく下書きとして読む。

## 判断例 {#example}

!!! example "判断例：更新の後に、リファクタの依頼が浅くなった"
    - **状況**：Claude Code を更新した翌日から、以前は 1 回で通っていた中規模のリファクタの依頼が、浅い変更で終わるようになった。
    - **迷う候補**：A は、上位のモデルに替えてそのまま作業を続ける。B は、前にうまくいった時の版・モデル・effort を思い出して今と並べ、違う項目を 1 つ戻して同じ依頼を数回流す。
    - **選んだもの**：B。
    - **理由**：記録票に並べると、モデルは同じで、effort の段だけが前と違っていた。段を戻して同じ依頼を数回流すと、結果が前の水準に近づいたので、原因は能力の低下ではなく設定の違いだった。A は、原因を確かめないまま費用だけを上げ、差の理由も残らない。段を戻しても変わらなければ、次に会話の量とモデルを見る。

## 古い助言に引きずられない {#outdated}

深く考えさせたくて、`think hard` や「熟考」「よく考えて」と書き足す古い頼み方が、記事や自分の CLAUDE.md に残っていることがある。これらは effort を上げる言葉としては働かない。考える深さは effort で決める。今の扱いは <!-- link:begin outdated-advice-ledger#think-hard-keywords -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#think-hard-keywords)<!-- link:end --> にある。

昔その言葉で深く考えていた覚えがあるなら、「性能が落ちた」という感じの一部は、そこから来ているかもしれない。保存した頼み方に残っていないかを探し、深く考えさせたい場面は effort で頼む。

## 予防：記録を残して差を測れるようにする {#prevention}

予防の考え方は、感覚に頼らず、前の状態を後から比べられる形で残すことである。

- うまくいった作業は、版・モデル・effort と課題を、記録票の形で残す。悪くなったと感じたとき、前の状態を思い出す手間が要らなくなる。
- 大事な課題は、失敗した作業を何度か流す小さな eval にしておく。手順は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end --> にある。
- 更新やモデルの切り替えの後は、変更履歴を見て、古い書き方が残っていないかを点検する。点検の手段は <!-- link:begin checking-for-updates -->最新を自分で確かめる方法（準備中）<!-- link:end --> にある。
- 話題が変わったら会話を新しくし、常駐するものを小さく保つ。減らす順は <!-- link:begin always-on-costs#reduce -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 減らす順](../context/always-on-costs.md#reduce)<!-- link:end --> にある。
- 「落ちた」という判断を、自分の記録で裏づけてから他人に伝える。裏づけがなければ、気がするという言い方にとどめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)：Anthropic・英語・確認日 2026-11-04
- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [An update on recent Claude Code quality reports](https://www.anthropic.com/research/april-23-postmortem)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)

**次に読む**

- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [/context で中身を見る](../context/inspect-context.md)
- 設定を外して切り分ける（--safe-mode）（準備中）
- [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)
- [effort の段階と使い分け](../models/effort-levels.md)
- [新しいモデルに替えたら見直すこと](../models/after-switching-models.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)

**関連**

- [現行モデルの一覧と位置づけ](../models/current-models.md)
- [モデルの選び方（三段階）](../models/choosing-a-model.md)
- [context rot と紛らわしい情報](../basics/context-rot.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- モデルの差よりハーネスの差（準備中）
- /insights と /usage で振り返る（準備中）
- 2026 年の主な変更の年表（準備中）
- 最新を自分で確かめる方法（準備中）
- [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)
- [長い会話で前提を忘れる・雑になる](forgets-in-long-chats.md)
- [返事が遅い・時間がかかりすぎる](too-slow.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
