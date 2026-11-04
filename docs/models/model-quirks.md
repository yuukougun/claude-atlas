---
id: model-quirks
title: モデル別の癖と、プロンプトの合わせ方
aliases: [モデルごとの傾向, モデル別のプロンプトの指針, モデルの性格]
type: concept
field: models
chapter: 替えたとき・劣化を疑うとき
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code, api, app]
principle: [確かめる]
prevents: [合っていない]
pitfalls: []
summary: 止まりすぎ・やりすぎ・冗長さなど、モデルごとに出やすい傾向を公式の指針から知り、自分の環境で観察してプロンプトを合わせられる。傾向は版で変わるので、暗記せず記録する。
signs:
  - {type: symptom, text: モデルを替えたら、確認ばかりで止まるようになった}
  - {type: goal, text: 使うモデルに合わせてプロンプトを直したい}
prerequisites: [choosing-a-model]
related: [after-switching-models, keeps-stopping, does-more-than-asked, output-shape, permission-to-stop, suggest-or-do, verification-ladder#verbal-checks, emphasis-words, felt-vs-measured, current-models]
tracks: []
outdated_advice: [add-double-check, tell-it-to-use-subagents, keep-going-dont-be-lazy]
sources: [api-docs-prompting-best-practices, api-docs-prompting-opus-5, api-docs-prompting-opus-5-5, api-docs-prompting-claude-sonnet-5-5, api-docs-prompting-claude-fable-5-1, api-docs-prompting-claude-haiku-5-5]
volatility: 高
sections:
  - {title: 公式の指針に出てくる傾向, anchor: official-guidance}
  - {title: 自分の環境で観察して記録する, anchor: observe-and-record}
  - {title: 何に効くか, anchor: what-it-prevents}
  - {title: 誤解しやすい点, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：止まりすぎ・やりすぎ・冗長さの出方は、モデルと版で違う。公式の指針で当たりを付け、自分の環境で記録して合わせる。
    - **いつ引くか**：モデルを替えたら確認ばかりで止まるようになったとき。使うモデルに合わせてプロンプトを直したいとき。
    - **前提**：<!-- link:begin choosing-a-model -->[モデルの選び方（三段階）](choosing-a-model.md)<!-- link:end -->

<!-- textlint-disable -->
別名：モデルごとの傾向・モデル別のプロンプトの指針・モデルの性格
<!-- textlint-enable -->

モデル別の癖とは、モデルと effort の組ごとに出やすい振る舞いの偏りのことである。このページは、公式の指針が挙げる偏りの種類を知るところから始める。固定の性格として覚えずに、自分の環境で観察して記録し、プロンプトと effort を合わせるところまでを扱う。

## 公式の指針に出てくる傾向 {#official-guidance}

公式はモデルごとのプロンプトの指針を出しており、モデルと effort の組ごとに出やすい偏りを挙げている。2026-10-29 に調査資料へ写した時点の内容を、偏りの種類で並べると次のようになる。どの版にどの偏りが出るかは、下に挙げる公式の各指針で確かめる。

| 偏りの種類 | 公式の指針が挙げる出方 | 合わせ方の向き |
| --- | --- | --- |
| 止まりすぎ | Sonnet は effort が low や medium のとき、確認のために止まりすぎる。Haiku は low で早く止まりがちで、effort を上げると減ったという。 | 最後まで任せる範囲を依頼に書く。それで足りなければ effort を上げる。 |
| やりすぎ | Sonnet は effort が high 以上のとき、頼まれていない機能・テスト・ファイル・文書・リファクタを足しがちである。 | 作る範囲を依頼に書く。案や計画を求めるときは、出したら止まるよう書く。 |
| 冗長 | Opus は既定で答えが長めになる。 | 望む長さと形を、出力の指定として書く。 |
| 確認と委任の重ね | Opus は自分の作業を言われなくても確かめ、進んで委任もする。確かめ直しや確かめ役の委任を促す一言は、過剰になる。 | その一言を消して、結果を比べる。 |
| 報告が約束で終わる | Fable は、ターンの最後の段落が計画や約束で終わることがあるため、終える前にそうなっていないかを確かめさせるよう公式が勧めている。 | 完了の報告に入れるものを依頼に書く。 |
| 調べ方の偏り | Fable は low で検索を減らし、記憶で答えがちである。Haiku は「何でも検索」と一律に書くと調べすぎる。 | 調べる対象と、記憶で答えてよい対象を分けて書く。 |

- 公式の指針の入口（英語）：[Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 系統ごとの指針（英語）：
    - [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
    - [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
    - [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
    - [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)
    - [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)

この表は、固定の性格の一覧ではない。偏りは版が替わると変わり、前の世代で効いた一言が次の世代で害になることもある。たとえば、続けるよう促す一言は、かつて長い作業の途中の停止を防いだ。今は <!-- link:begin outdated-advice-ledger#keep-going-dont-be-lazy -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#keep-going-dont-be-lazy)<!-- link:end --> として扱われ、やりすぎの原因になりやすい。

モデルの性格の差を体系的に測ったデータはない。実践者の報告には、長い会話で Claude が区切りや撤退を促しがちだという例もあるが、単独の経験談で、版でも変わる（根拠：弱）。だから、このページでは偏りを暗記する対象にせず、次の節のように観察して記録する対象として扱う。どのモデルがいま選べるかは <!-- link:begin current-models#lineup -->[現行モデルの一覧と位置づけ › 系統ごとの位置づけ（表）](current-models.md#lineup)<!-- link:end --> で確かめる。

## 自分の環境で観察して記録する {#observe-and-record}

観察して記録するとは、同じ依頼を条件だけ変えて流し、起きたことを数えて残すことである。公式の指針は当たりを付けるための仮説で、自分の依頼で同じ偏りが出るかは流してみないと分からない。体感が実測とずれる理由と、記録で測る項目は <!-- link:begin felt-vs-measured#what-to-record -->[体感と実測 › 記録で測るもの](../eval/felt-vs-measured.md#what-to-record)<!-- link:end --> にある。ここではモデルの癖に絞って手順を示す。

1. 代表的な依頼を数件選んで、文面を固定する。小さな修正・数ファイルにまたがる変更・調べて案を出す依頼のように、癖が出やすい種類を混ぜる。
2. 変える条件は、1 回の比べで 1 つだけにする。候補はモデル・effort・依頼の文面である。複数を同時に変えると、効いたものが分からない。
3. 数えるものを先に決める。確認で止まった回数、頼んでいない変更のファイル数と行数、返答の長さ、完了の報告の有無が基本である。
4. 直しは 1 つずつ入れ、入れるたびに固定した依頼を流し直す。ほかの依頼が悪くなっていないかも見る。

記録の表の雛形を次に示す。

<!-- gen:begin snippet model-quirks/observation-log -->
<!-- textlint-disable -->

???+ example "雛形：モデルの癖の観察記録の表"

    ```markdown
    # モデルの癖の記録

    ## 固定する依頼（条件を変えても文面を変えない）

    | 名前 | 依頼の文面（または置き場所） | 何で終わりとするか |
    | --- | --- | --- |
    | A | （小さな修正の依頼） | 指定のテストが通る |
    | B | （数ファイルにまたがる変更の依頼） | 指定のテストが通り、差分が依頼の範囲に収まる |
    | C | （調べて案を出す依頼） | 案を出した時点で止まる |

    ## 記録

    | 日付 | モデル（セッション内の表示） | effort | 面 | 依頼 | 変えた条件（1 つだけ） | 確認で止まった回数 | 頼んでいない変更（ファイル数・行数） | 返答の長さ（おおよそ） | 完了の報告の有無 | 気づいたこと |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | （例）2026-11-05 | （表示のまま） | （表示のまま） | Claude Code | A | なし（基準） | 0 | 0 | 短い | あり | |
    | | | | | A | effort を 1 段下げた | | | | | |
    | | | | | A | 依頼に「最後まで進めてよい範囲」を足した | | | | | |

    ## 読み方

    - 変えた条件が 1 行に 2 つ以上あるときは、どちらが効いたか分からないので、その行は結論に使わない
    - 1 回の差は偶然のことがある。同じ条件で数回繰り返し、傾向として読む
    - 直した後は、固定した依頼をすべて流し直し、ほかの依頼が悪くなっていないかを見る
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet model-quirks/observation-log -->

!!! example "判断例：モデルを替えたら確認ばかりで止まるようになった"
    - **状況**：使うモデルを替えた直後から、Claude Code が作業の途中で何度も確認を求めて止まる。
    - **迷う候補**：公式の指針に倣って「最後まで進めてよい」と依頼に書き足す。または、依頼は変えずに、同じ依頼で effort だけを変えて止まる回数を記録する。
    - **選んだもの**：先に、固定した依頼で effort だけを 1 段ずつ変えて、止まる回数を数える。
    - **理由**：公式の指針は止まりすぎの出やすい組み合わせを挙げるだけで、いまの停止がその癖によるとは限らない。提案か実行かの伝え方や権限モードが原因のこともあるため、切り分けは <!-- link:begin keeps-stopping#diagnosis -->[確認ばかりで進まない・途中で止まる › 原因を安く確かめる順](../symptoms/keeps-stopping.md#diagnosis)<!-- link:end --> の順で進める。effort を上げて止まる回数が減るなら、依頼の文面を触らずに済み、替えた効果の確かめ方は <!-- link:begin choosing-a-model#verify -->[モデルの選び方（三段階） › 替えた効果の確かめ方](choosing-a-model.md#verify)<!-- link:end --> と同じ形になる。

依頼に足す文は、強調で押し切らず、範囲と完了の条件を具体的に書く。提案と実行の書き分けは <!-- link:begin suggest-or-do#verbs -->[提案してほしいのか、実行してほしいのか › 提案と実行を動詞で分ける](../prompting/suggest-or-do.md#verbs)<!-- link:end --> が、長さの指定は <!-- link:begin output-shape#length -->[出力の形と分量を指定する › 長さと要約の有無](../prompting/output-shape.md#length)<!-- link:end --> が持っている。モデルを替えた直後に見直す部品の全体は <!-- link:begin after-switching-models#checklist -->[新しいモデルに替えたら見直すこと › 見直す順](after-switching-models.md#checklist)<!-- link:end --> にある。

## 何に効くか {#what-it-prevents}

このページの原理は「確かめる」で、防ぐ原因は、モデル・effort・頼み方が作業に合っていないことである。公式の指針の癖をそのまま当てはめて直すと、直しは外れやすい。記録で確かめてから直すと、合っていない部分を 1 つずつ特定できる。

- 止まりすぎ：原因の切り分けは <!-- link:begin keeps-stopping#diagnosis -->[確認ばかりで進まない・途中で止まる › 原因を安く確かめる順](../symptoms/keeps-stopping.md#diagnosis)<!-- link:end --> へ。このページは、モデルと effort の癖の可能性を確かめる側を受け持つ。
- やりすぎ：範囲の指定と差分の確かめ方は <!-- link:begin does-more-than-asked#prevention -->[頼んでいないことまでやる（過剰設計） › 予防：範囲を先に決め、差分を毎回見る](../symptoms/does-more-than-asked.md#prevention)<!-- link:end --> へ。
- 冗長さや形：長さと形の指定は <!-- link:begin output-shape#length -->[出力の形と分量を指定する › 長さと要約の有無](../prompting/output-shape.md#length)<!-- link:end --> へ。
- 確認の重ねすぎ：「念のため確認して」と書き足すより、確かめる手段を渡すほうがよい。段の選び方は <!-- link:begin verification-ladder#verbal-checks -->[検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)<!-- link:end --> へ。

効かない場面もある。例外を許さない禁止は、依頼に書いても守られきらないので、仕組みに移す。止まって報告する権利を渡す書き方と、その限界は <!-- link:begin permission-to-stop#limits -->[止まって報告する権利を渡す › 言葉の許可が効く範囲（モデルによる差）](../prompting/permission-to-stop.md#limits)<!-- link:end --> にある。

長い作業を任せるほど、癖の出方が結果に響く。任せる前に、止まりすぎとやりすぎの両方を確かめる手段を先に決めておく。

## 誤解しやすい点 {#misconceptions}

- 「このモデルはこういう性格」と覚えれば足りる。性格の差を測ったデータはなく、版で変わる。覚えるのは偏りの種類と、観察の手順である。
- 強い言い方を足せば直る。強調語は指示の効きを上げず、かえって過剰に当てはまることがある。直し方は <!-- link:begin emphasis-words#rewrite -->[強調語（IMPORTANT・必ず）の現在 › 強調を外した書き直しの例](../prompting/emphasis-words.md#rewrite)<!-- link:end --> にある。
- 前のモデルで効いた一言は、今も効く。確かめ直しを促す一言は <!-- link:begin outdated-advice-ledger#add-double-check -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#add-double-check)<!-- link:end --> に、委任を促す一言は <!-- link:begin outdated-advice-ledger#tell-it-to-use-subagents -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#tell-it-to-use-subagents)<!-- link:end --> にある。効くかどうかはモデルによるので、消して比べる。
- 公式の指針の文をそのまま写せば直る。指針は出発点で、自分の依頼で効いたかは記録で確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [モデルの選び方（三段階）](choosing-a-model.md)

**関連**

- [新しいモデルに替えたら見直すこと](after-switching-models.md)
- [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- [出力の形と分量を指定する](../prompting/output-shape.md)
- [止まって報告する権利を渡す](../prompting/permission-to-stop.md)
- [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)
- [検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](../verify/verification-ladder.md#verbal-checks)
- [強調語（IMPORTANT・必ず）の現在](../prompting/emphasis-words.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [現行モデルの一覧と位置づけ](current-models.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
