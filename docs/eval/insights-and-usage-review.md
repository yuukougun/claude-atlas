---
id: insights-and-usage-review
title: /insights と /usage で振り返る
aliases: [使い方の振り返り, 摩擦の分析]
type: feature
field: eval
chapter: 変化を測る
order: 40
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: []
pitfalls: []
scenes: [開発]
summary: /insights と /usage で、摩擦の起きた所と使い方の内訳を振り返り、仕組みに移すものや削るものを選べる。出てきた提案は、判断ではなく下書きとして読む。
signs:
  - {type: goal, text: 自分の使い方のどこに無駄や引っかかりがあるか知りたい}
  - {type: goal, text: どの拡張がどれだけ使われているかを見たい}
prerequisites: [felt-vs-measured]
related: [usage-context-statusline, what-uses-up-limits#find-what-uses-it, always-on-costs, pruning-extensions, when-to-add-what, repeating-the-same-explanation, postmortems, measure-changes]
tracks: [insights, usage]
outdated_advice: [slash-cost-and-stats]
sources: [cc-docs-costs, cc-docs-commands]
volatility: 中
sections:
  - {title: どんな無駄と引っかかりを見つけるか, anchor: when}
  - {title: 最小の使い方, anchor: minimal}
  - {title: /insights の提案を下書きとして読む, anchor: insights-as-drafts}
  - {title: /usage の内訳から削るものを選ぶ, anchor: usage-breakdown}
  - {title: 効かない場面と落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：`/insights` で摩擦の起きた所を、`/usage` で使い方の内訳を見て、仕組みに移すものと削るものを選べる。
    - **いつ引くか**：自分の使い方のどこに無駄や引っかかりがあるか知りたいとき。どの拡張がどれだけ使われているかを見たいとき。
    - **強制力**：<!-- gen:begin feature insights/enforcement -->なし<!-- gen:end feature insights/enforcement -->。報告と内訳を見せるだけで、見ても設定と動作は変わらない。設定を変えるのは自分で、`/usage` の推奨の自動適用を使うときだけ例外になる。
    - **前提**：<!-- link:begin felt-vs-measured -->[体感と実測](felt-vs-measured.md)<!-- link:end -->

<!-- textlint-disable -->
別名：使い方の振り返り・摩擦の分析
<!-- textlint-enable -->

`/insights` と `/usage` は、Claude Code で自分の使い方を振り返る 2 つの道具である。前者は最近のセッションから摩擦の起きた所と改善の提案を HTML の報告にし、後者は使用量を拡張ごとの内訳で見せる。どちらも材料を出すだけで、何を仕組みに移し、何を削るかは自分で決める。

## どんな無駄と引っかかりを見つけるか {#when}

`/insights` と `/usage` が防ぐのは、体感だけで使い方を直すことである。「なんとなく遅い」「毎回同じところで詰まる」という印象は、記録と照らすとずれることがある。ずれる理由は <!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](felt-vs-measured.md#why)<!-- link:end --> にある。振り返りの道具は、その印象を記録に戻すための入口になる。

2 つの道具が答える問いは別である。

- `/insights`：最近のセッションで、どんな作業をして、どこで引っかかったか。引っかかりの例は、依頼の取り違えと、バグのあるコードである。
- `/usage`：使用量が、スキル・サブエージェント・プラグイン・MCP サーバーのどれに、どれだけ向いているか。

見る頻度は、毎日ではなく、セッションがまとまった量たまってからでよい。月に 1 回ほどという目安がある（根拠：弱。版に依存する実践者の目安で、規則ではない）。

## 最小の使い方 {#minimal}

使い方は、Claude Code の中でコマンドを打つだけである。この 2 つは Claude Code の機能で、アプリと API には同じものがない。ほかの OS と IDE 拡張での動作は未確認である。

1. `/insights` を打つ。この機械の最近のセッションが分析され、HTML の報告ができる。報告には、取り組んでいた作業・うまくいかなかった所・試せる機能が入る。
2. `/usage` を打つ。使用量の内訳が出る。プランによっては、何が上限に数えられたかの内訳と、改善の推奨も出る。

`/insights` の分析にもトークンを使い、使用量に数えられる。クラウドのセッションでは使えない。この機械のセッションだけが対象で、ほかの機械と claude.ai のセッションは入らない。

## /insights の提案を下書きとして読む {#insights-as-drafts}

`/insights` が出す改善の提案は、判断ではなく下書きとして読む。報告は、セッションの記録を分析した結果であり、記録そのものではない。分析が見落とした摩擦も、実際より目立たせた摩擦もありうる（推論・実践例なし）。

提案を仕組みへ移す前に、次の 3 つを自分で確かめる。

1. **繰り返しが見えるか**：同じ摩擦が複数のセッションで起きているか。1 回きりの摩擦を規則にすると、指示が増えるだけである。足す時期の考え方は <!-- link:begin when-to-add-what#why -->[拡張を足すタイミング › 繰り返しが見えてから足す理由](../extend/when-to-add-what.md#why)<!-- link:end --> にある。
2. **原因は何の隙間か**：指示の不足か、仕組みの隙間か。誰の誤りかではなく、どの隙間が許したかで見る。見方は <!-- link:begin postmortems#which-gap -->[失敗を仕組みに戻す（ポストモーテム） › 誰がではなく、どの隙間が](../judgment/postmortems.md#which-gap)<!-- link:end --> にある。
3. **移した後の効果を確かめられるか**：確かめ方がない提案は、反映した後に効果が分からない。確かめ方は <!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](measure-changes.md#small-eval)<!-- link:end --> にある。

移す先は、繰り返しの種類で決まる。毎回同じ説明をしているなら <!-- link:begin repeating-the-same-explanation#causes -->[毎回同じ説明をしている › 原因ごとの対処](../symptoms/repeating-the-same-explanation.md#causes)<!-- link:end --> を、置き場所の選び方なら <!-- link:begin when-to-add-what#triggers -->[拡張を足すタイミング › 繰り返しの種類と移す先](../extend/when-to-add-what.md#triggers)<!-- link:end --> を引く。

!!! example "判断例：報告の提案を CLAUDE.md に足すか"
    - **状況**：`/insights` の報告が、3 つのセッションで、テストの実行コマンドの取り違えを指摘している。提案は、テストの実行方法を CLAUDE.md に足すことである。
    - **迷う候補**：提案のとおり CLAUDE.md に足す。足さずに、次の数回のセッションで同じ摩擦が起きるかを見る。
    - **選んだもの**：足す前に、3 つのセッションの記録を自分で開き、同じ原因かを確かめる。
    - **理由**：2 つは同じ原因（古いコマンドを Claude が推測した）で、1 つは依頼の曖昧さだった。前者は 1 行を足す価値があり、後者は CLAUDE.md の問題ではない。報告の提案は、仕分け前の下書きである。

下書きの仕分けは、Claude に手伝わせてもよい。ただし、仕分けを頼むときも、根拠の確認と最終の判断は自分が握る。AI は集計係であり、移すかどうかを決める側ではない。

<!-- gen:begin snippet insights-and-usage-review/triage-insights-report -->
<!-- textlint-disable -->

??? example "雛形：/insights の提案を下書きとして仕分けさせる依頼"

    ```markdown
    次は `/insights` が出した報告の、提案の部分である。

    <ここに、報告の提案の部分を貼る>

    この提案を、決める前の下書きとして仕分けてほしい。ファイルは変更しない。

    各提案について、次の 4 つを表にする。
    1. 報告のどの摩擦の記述が根拠か（報告の文をそのまま引く）
    2. その摩擦が複数のセッションで繰り返されているかを、私が自分で確かめる方法
    3. 移す先の候補（指示・CLAUDE.md・スキル・フック・deny ルール・何もしない）と、その候補を選ぶ理由
    4. 移した後に、効いたかを確かめる方法

    根拠が報告の中に見つからない提案は、表の最後に「根拠が見えない提案」として分ける。
    私が答えないと決められない点は、表を作る前に質問する。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet insights-and-usage-review/triage-insights-report -->

## /usage の内訳から削るものを選ぶ {#usage-breakdown}

内訳の読み方そのものは <!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> が持ち主である。ここでは、内訳を読んだ後に、削るものを選ぶ判断だけを書く。

内訳の割合は、使った量であって、役に立った量ではない。割合が大きいことは、削る理由にならない。「割合の大きさ」と「最近使った頻度」の 2 つを並べて決める。

| 割合 | 使う頻度 | 方針 |
| --- | --- | --- |
| 大きい | 低い | 削るか、使うときだけ読ませる形にする |
| 大きい | 高い | 残す。中身を小さくできないか見る |
| 小さい | 低い | 急がない。棚卸しのときにまとめて見る |
| 小さい | 高い | 触らない |

毎回のリクエストに乗るものほど、割合が大きいときの効果が大きい。常駐するものの費用は <!-- link:begin always-on-costs#reduce -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 減らす順](../context/always-on-costs.md#reduce)<!-- link:end --> にある。実際に切る手順と、切った後の確かめ方は <!-- link:begin pruning-extensions -->[拡張の棚卸しと剪定](../extend/pruning-extensions.md)<!-- link:end --> に任せる。

`/usage` が推奨を出す場合は、それも下書きとして読む。推奨は自動で適用する操作が用意されている版もあるが、適用の前に、何が変わるかを読む。

!!! example "判断例：割合の大きい MCP サーバーを外すか"
    - **状況**：`/usage` の内訳で、ある MCP サーバーの割合が大きい。そのサーバーは、月末の集計作業にしか使わない。
    - **迷う候補**：外して、必要なときに入れ直す。入れたままにして、割合を許容する。
    - **選んだもの**：普段は無効にして、月末の作業の前だけ有効にする。
    - **理由**：使う頻度が低いのに割合が大きいので、常駐させる利点が小さく、費用だけが毎回かかる。外すと月末に入れ直す手間が出るので、削除ではなく無効にした。切った後は、同じ作業が前と同じ品質で終わるかを見る。

<!-- gen:begin snippet insights-and-usage-review/list-cut-candidates -->
<!-- textlint-disable -->

??? example "雛形：/usage の内訳から削る候補を仕分けさせる依頼"

    ```markdown
    次は `/usage` の内訳を写したものである。

    <ここに、/usage の内訳を貼る>

    内訳の項目を、削る・小さくする・残す の 3 つに仕分ける案を出してほしい。ファイルと設定は変更しない。

    手順は次のとおりにする。
    1. 項目を、毎回のリクエストに乗るもの（CLAUDE.md・スキルの説明・MCP のツールの一覧など）と、使うときだけ読まれるものに分ける。
    2. 割合の大きい順に並べる。
    3. 各項目について、私が最近いつ使ったかを私に質問する。私の答えを聞く前に、削る案を確定しない。
    4. 答えを聞いた後で、各項目に 3 つのどれかを付け、理由を 1 行で書く。

    割合は使った量であり、役に立った量ではない。割合の大きさだけを理由に「削る」を選ばないこと。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.0。

<!-- textlint-enable -->
<!-- gen:end snippet insights-and-usage-review/list-cut-candidates -->

## 効かない場面と落とし穴 {#pitfalls}

- **対象の範囲**：`/insights` が見るのは、この機械の最近のセッションだけである。ほかの機械・claude.ai・クラウドのセッションで起きた摩擦は入らない。
- **セッションが少ないと偏る**：件数が少ないうちは、1 回の事故が報告の大半を占める。たまってから見る。
- **記録に出ない摩擦は見えない**：途中で諦めて手作業に切り替えた場面は、記録に残りにくい（推論）。体感との突き合わせに使う記録の選び方は <!-- link:begin felt-vs-measured#what-to-record -->[体感と実測 › 記録で測るもの](felt-vs-measured.md#what-to-record)<!-- link:end --> にある。
- **提案をそのまま足す**：報告の提案を全部 CLAUDE.md に足すと、常駐するものが増える。増えた分は毎回のリクエストに乗る。理由は <!-- link:begin always-on-costs#why-small -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › なぜ常駐を小さく保つのか](../context/always-on-costs.md#why-small)<!-- link:end --> にある。
- **分析自体が使用量を使う**：`/insights` の分析にもトークンを使う。上限が厳しいときは、実行する時期を選ぶ。
- **費用の数字は推定値**：`/usage` のセッションの費用は、API を使う人向けの推定値である。請求の額ではない。
- **内訳の出ないプラン**：上限に数えられた分の内訳は、一部のプランだけで出る。出ないときは、<!-- link:begin usage-context-statusline#instruments -->[/usage・/context・ステータスラインで状態を見る › 三つの道具で見えるもの](../cli/usage-context-statusline.md#instruments)<!-- link:end --> の道具で代わりに見る。
- **報告の共有**：報告は作業の内容を含む。人へ見せる前に、中身を読む。

## 比べる相手 {#compare}

2 つの道具の属性の比較を、次の表に示す。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 入った版 |
| --- | --- |
| [/insights](insights-and-usage-review.md) | — |
| [/usage](../cli/usage-context-statusline.md) | 2.0.0（2025-09-29） |

すべて共通：面 Claude Code、成熟度 GA、強制力 なし、確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare -->

文脈の内訳を見るなら `/context` を使う。`/context` とステータスラインは <!-- link:begin usage-context-statusline -->[/usage・/context・ステータスラインで状態を見る](../cli/usage-context-statusline.md)<!-- link:end --> で扱う。変更が効いたかを測るなら <!-- link:begin measure-changes -->[変更が効いたかを測る（小さな eval）](measure-changes.md)<!-- link:end --> の小さな eval を使う。振り返りは「どこを直すか」を選ぶ道具で、直した結果が効いたかは、別に測る。

## 古くなった助言 {#outdated}

「使用量は `/cost`、使い方の統計は `/stats` で見る」という手順は古い。今の呼び方は <!-- name:begin cost-stats-to-usage -->/usage<!-- name:end --> である。旧名は今も打てる別名で、`/usage` の該当のタブを開く。急いで直す必要はないが、新しく書く手順は `/usage` で書く。台帳の行は <!-- link:begin outdated-advice-ledger#slash-cost-and-stats -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#slash-cost-and-stats)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [体感と実測](felt-vs-measured.md)

**関連**

- [/usage・/context・ステータスラインで状態を見る](../cli/usage-context-statusline.md)
- [上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [拡張の棚卸しと剪定](../extend/pruning-extensions.md)
- [拡張を足すタイミング](../extend/when-to-add-what.md)
- [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- [失敗を仕組みに戻す（ポストモーテム）](../judgment/postmortems.md)
- [変更が効いたかを測る（小さな eval）](measure-changes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
