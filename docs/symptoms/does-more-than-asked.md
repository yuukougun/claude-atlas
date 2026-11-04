---
id: does-more-than-asked
title: 頼んでいないことまでやる（過剰設計）
nav_title: 頼んでいないことまでやる
aliases: [過剰設計, スコープの膨張, over-engineering, 余計な変更, 死んだコードを残す, 作業フォルダが散らかる]
type: symptom
field: symptoms
chapter: 返答と品質
order: 20
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [見せる, 確かめる]
prevents: [見えていない, 確かめていない, 合っていない]
pitfalls: []
scenes: [開発]
summary: 頼んでいない機能・ファイル・抽象化が増える原因を、範囲の伝え方と effort・モデルの選び方に分けて切り分け、範囲の指定と差分の確かめ方を決める。
signs:
  - {type: symptom, text: 頼んでいない機能やファイルが増える}
  - {type: symptom, text: 小さな修正を頼んだのに周りまで書き換えられる}
  - {type: symptom, text: 使わない抽象化や設定項目を勝手に足される}
  - {type: symptom, text: 古いコードを消さずに新しい版を足していく}
  - {type: symptom, text: 作業フォルダに一時ファイルを残していく}
wave: 1
prerequisites: []
related: [suggest-or-do, ask-for-outcomes, what-to-put-in-claude-md, own-generated-code, independent-review, rewind-dont-correct, output-shape, not-what-i-meant, keeps-stopping, six-causes, outdated-advice-ledger]
routes:
  - {cause: 見えていない, to: [state-the-scope, when-to-plan, spec-first]}
  - {cause: 確かめていない, to: [diffs-humans-must-read, working-with-git]}
  - {cause: 合っていない, to: [effort-levels, model-quirks]}
tracks: [effort, plan-mode]
outdated_advice: [keep-going-dont-be-lazy]
sources: [api-docs-prompting-best-practices, api-docs-prompting-opus-5, cc-docs-best-practices, arxiv-2403-08937, arxiv-2603-00539, dolthub-claude-code-gotchas, marmelab-code-tips-wish-id-had]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: examples}
  - {title: 予防：範囲を先に決め、差分を毎回見る, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：頼んでいない機能・ファイル・抽象化が増える原因を、見えていない・確かめていない・合っていないの順に安く切り分けられる。範囲の指定と差分の確かめ方も決められる。
    - **いつ引くか**：頼んでいない機能やファイルが増えたとき。小さな修正を頼んだのに周りまで書き換えられたとき。使わない抽象化や設定項目を足されたとき。古いコードを消さずに新しい版を足されたとき。作業フォルダに一時ファイルを残されたとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：過剰設計・スコープの膨張・over-engineering・余計な変更・死んだコードを残す・作業フォルダが散らかる
<!-- textlint-enable -->

頼んでいないことまでやるとは、依頼にない機能・ファイル・抽象化・周辺の書き換えが、成果物に混ざることである。原因は 3 つに分けられる。依頼の範囲が Claude に伝わっていない（見えていない）、出てきた差分を人が確かめていない（確かめていない）、モデルや effort の癖が作業に合っていない（合っていない）である。このページは、安く確かめられる順に原因を切り分け、行き先のページを決める。診断は Claude Code を基準にする。アプリでの動きは、この教材ではまだ確かめていない（未確認）。

## よくある形 {#forms}

困りごとの言い方ごとに、先に疑う原因を添える。確かめ方は、下の診断にある。

- **頼んでいない機能やファイルが増える**：1 つの機能を頼んだのに、設定ファイルや補助の関数、説明用の文書まで作られる。依頼の範囲が書かれていたかを、先に見る。
- **小さな修正を頼んだのに周りまで書き換えられる**：バグを 1 つ直すだけの頼みで、周辺の関数の整理や名前の変更まで入る。先に「見えていない」を疑い、次に差分を読んだかを見る。
- **使わない抽象化や設定項目を勝手に足される**：呼び出しが一箇所しかない処理に、汎用の仕組みやオプションが付く。範囲の伝え方に加えて、モデルの癖も疑う。
- **古いコードを消さずに新しい版を足していく**：古い関数の隣に、名前に New を付けた関数が並び、古い側が死んだコードとして残る。範囲の伝え方と、差分の確かめ方の両方を見る。
- **作業フォルダに一時ファイルを残していく**：確かめ用のスクリプト、テスト用のデータベース、ビルドの成果物が残る。差分の確かめ方を先に見る（根拠：弱）。

## 原因を安く確かめる順 {#diagnosis}

困った一件の依頼文と、その後の差分（`git status` と `git diff`）を手元に出す。上から順に確かめる。上の原因ほど、確かめる手間が小さい。各項目で原因を直したら、同じ依頼をやり直し、増える物が減ったかを見る。

1. **見えていない**：依頼に、やること・やらないこと・触ってよい範囲が書かれていなかった。LLM が書いたコードのバグを分類した 2024 年の研究では、最大の類型が仕様の誤解釈で、頼まれていない処理の追加も類型に入っている（根拠：中。対象は当時のモデル）。次を、依頼文と手元の設定から探す。
    - 依頼文に完了の条件と触らない範囲があるか。なければ原因の第一候補である。書き方は <!-- link:begin state-the-scope#anti-goals -->[範囲を伝える（やらないこと） › やらないことを書く](../prompting/state-the-scope.md#anti-goals)<!-- link:end --> にある。
    - 好みの方式があるのに伝えていないか。2 つの妥当な方式があって好みがあるなら、最初に伝える。コードからは読み取れない（公式の Best practices の勧め）。
    - CLAUDE.md や繰り返す頼み方に、「最後までやり切れ」「keep going」「don't be lazy」の類の一言がないか。こうした一言は、停滞を解く代わりに過剰な作業を招きやすい。今どうするかは <!-- link:begin outdated-advice-ledger#keep-going-dont-be-lazy -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#keep-going-dont-be-lazy)<!-- link:end --> にある。
    - 方針や範囲に迷いがある作業を、いきなり実装させていないか。迷う作業は、plan mode で編集を止めたまま計画を出させ、計画の段階で範囲のずれを見つける。使い方は <!-- link:begin when-to-plan#when -->plan mode の使いどころ › 計画が効く作業、省いてよい作業（準備中）<!-- link:end --> にある。大きな機能なら、実装の前に範囲外まで仕様に書く手もある（<!-- link:begin spec-first#interview -->仕様を先に固める（spec・インタビュー・モック先行） › インタビューで仕様を詰める（準備中）<!-- link:end -->）。
    - 提案で止めてほしい頼みを、実行まで頼む書き方にしていないか。動詞の書き分けは <!-- link:begin suggest-or-do#verbs -->[提案してほしいのか、実行してほしいのか › 提案と実行を動詞で分ける](../prompting/suggest-or-do.md#verbs)<!-- link:end --> にある。
2. **確かめていない**：増えた物が、差分に出ていたのに、読まずに採ってしまった。範囲を書いても、差分を読まなければ、漏れた変更は残る。
    - `git status` で、追跡されていない新しいファイルと、頼んでいないファイルの変更を見る。`git diff --stat` で、変更が頼みの大きさに見合うかを見る。作業フォルダの一時ファイルは、ここで見つかる。
    - 古い関数の隣に、名前だけ違う新しい版が並んでいないかを見る。死んだコードが残るのは、公式の文書ではなく実践者の記事にある報告である（根拠：弱）。
    - 洗い出しを Claude に頼むなら、この項目の後ろにある雛形のように、直さずに一覧だけ出させる。同じ会話の Claude は、自分の変更を甘く見やすい（推論・実践例なし）。差分が大きいときは、変更を作っていない新しいセッションか別の担当に見せる（<!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end -->）。
    - 洗い出しで、判定・理由・修正案まで求めすぎない。コードを要件に照らして判定させる 2026 年の研究がある。この研究では、判定・理由・修正案まで求めると、正しいコードを要件不適合と判定する率が上がった（根拠：中・類推。旧世代のモデルを含む 5 つのモデルの結果なので、現行の Claude の傾向とは言えない）。事実の一覧だけを出させ、判断は人が行う。
    - 人が読むべき差分の箇所は <!-- link:begin diffs-humans-must-read#red-flags -->人間が読むべき差分の箇所 › 赤信号の一覧（準備中）<!-- link:end --> にある。変更を小さく区切るほど、増えた物は見つけやすい（<!-- link:begin working-with-git#granularity -->[git との付き合い方 › どこで区切るか](../cli/working-with-git.md#granularity)<!-- link:end -->）。

<!-- gen:begin snippet does-more-than-asked/scope-audit -->
<!-- textlint-disable -->

??? example "雛形：頼んだ範囲を外れた変更を洗い出す依頼の雛形"

    ```markdown
    直した内容を、私の依頼の範囲と照らして洗い出してほしい。ここでは何も直さず、一覧だけを出す。`git status` と `git diff` の出力を根拠にする。

    1. 私の依頼の文のどこにも書いていない変更。新しいファイル・関数・設定項目・抽象化・周辺の書き換えを、ファイルごとに挙げる
    2. 作業のために作って、まだ残している一時ファイルやスクリプト
    3. 古い版を残したまま、新しい版を足したもの

    それぞれに、依頼のどの文に基づくかを添える。基づく文がなければ「なし」と書く。判定や直し方の提案は書かず、事実だけを並べる。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet does-more-than-asked/scope-audit -->

3. **合っていない**：範囲を書き、差分も読んでいるのに、同じ種類の余計な物が出る。モデルや effort の癖が、作業に合っていない可能性がある。公式のモデル別の指針には、過剰設計や範囲の拡大が出やすいと書かれたものがある（Prompting best practices と Prompting Claude Opus 5。確認日 2026-11-05）。傾向はモデルの版で変わるので、暗記せず、使っているモデルの最新の指針を見る。
    - 同じ依頼を、別のモデルか別の段の effort で出し、差分の大きさを比べる。現在の既定の段は、面とモデルで違う（<!-- link:begin effort-levels#defaults-by-surface -->[effort の段階と使い分け › 既定の段（モデル × 面の表）](../models/effort-levels.md#defaults-by-surface)<!-- link:end -->）。effort の段と過剰設計の関係は、公式の文書では確かめていない（未確認）ので、比べた結果を記録して判断する。
    - 傾向の見方と記録のしかたは <!-- link:begin model-quirks#observe-and-record -->モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する（準備中）<!-- link:end --> にある。
    - 公式は、範囲の拡大が出るモデルに対して、頼んだ範囲を守らせる一文を指示に足す手を示している。書き方は <!-- link:begin state-the-scope#anti-goals -->[範囲を伝える（やらないこと） › やらないことを書く](../prompting/state-the-scope.md#anti-goals)<!-- link:end --> にある。

原因が分かったら、次の表の先へ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)<br>plan mode の使いどころ（準備中）<br>仕様を先に固める（spec・インタビュー・モック先行）（準備中） |
| 確かめていない | 人間が読むべき差分の箇所（準備中）<br>[git との付き合い方](../cli/working-with-git.md) |
| 合っていない | [effort の段階と使い分け](../models/effort-levels.md)<br>モデル別の癖と、プロンプトの合わせ方（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：バグを 1 つ直すだけの頼みで、周辺まで整理された"
    - **状況**：関数の境界条件のバグを直す頼みで、その関数を呼ぶ 4 つのファイルの変数名と、隣の関数の構造まで変わった。
    - **迷う候補**：差分から余計な部分だけを手で戻す。「余計な変更は戻して」と返して直させる。巻き戻して、範囲を書き足した依頼をやり直す。
    - **選んだもの**：巻き戻して、「この関数の境界条件だけを直す。名前の変更と周辺の整理はしない」を足した依頼をやり直す。
    - **理由**：間違った試みが会話に残ると、次の答えがそれに引きずられる（<!-- link:begin rewind-dont-correct#why -->[違うと返すより、巻き戻す・編集する › なぜ訂正より巻き戻しか](../context/rewind-dont-correct.md#why)<!-- link:end -->）。範囲の欠けが原因なら、直すのは依頼の側である。やり直した後の差分は、`git diff --stat` で見る。

!!! example "判断例：古い関数の隣に新しい版が増え、一時ファイルも残った"
    - **状況**：処理の置き換えを頼んだら、古い関数が残ったまま `New` 付きの関数が並び、作業用のスクリプトがフォルダに残った。
    - **迷う候補**：その場で削除を頼む。新しいセッションで、ファイルを 1 つに限って死んだコードの削除を頼む。規則を CLAUDE.md に書く。
    - **選んだもの**：削除は新しいセッションで、ファイルを 1 つに限って頼み、置き換えの規則は CLAUDE.md に理由と一緒に書く。
    - **理由**：実践者の記事は、ファイルを限り、新しいセッションで削除を頼む手を勧める（根拠：弱）。削除のたびに範囲を狭めれば、差分を読み切れる。CLAUDE.md には、「置き換えるときは古い版を消す」と理由を書く。守られないなら、<!-- link:begin state-the-scope#two-layers -->[範囲を伝える（やらないこと） › 例外を許さない範囲は仕組みで縛る（二層）](../prompting/state-the-scope.md#two-layers)<!-- link:end --> の鍵に移す。

## 予防：範囲を先に決め、差分を毎回見る {#prevention}

予防は、範囲を先に決めることと、差分を毎回見ることの 2 つである。

- **範囲を先に書く**：やること・やらないこと・触ってよい範囲を、依頼文の中で示す。最小限で足りるなら、その旨を書く（<!-- link:begin state-the-scope#minimum -->[範囲を伝える（やらないこと） › いまの作業に要る最小限を求める](../prompting/state-the-scope.md#minimum)<!-- link:end -->）。目的と完了の条件は成果で渡し、どこを触るかは具体的に書く（<!-- link:begin ask-for-outcomes#specifics -->細かく指図するか、成果で頼むか › 具体的に書くもの：対象と測り方（準備中）<!-- link:end -->）。
- **迷う作業は計画を読む**：範囲に迷う作業は、plan mode で計画を出させ、読んでから実装に入る。
- **例外を許さない範囲は鍵に移す**：触らせないファイルや作らせない物は、権限やフックで縛る。CLAUDE.md には理由と相談の基準を書く（<!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end -->）。
- **変更を小さく区切り、毎回差分を見る**：1 つの変更を 1 つの確かめと 1 つのコミットに対応させると、余計な物が混ざった時点で戻せる。コミットの前に `git status` と `git diff` を見る習慣は、実践者の報告にもある（根拠：弱）。
- **強い言葉で続けさせない**：「最後までやり切れ」の類の一言は消し、通すべきテストのような確かめる手段を渡す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Bugs in Large Language Models Generated Code: An Empirical Study](https://arxiv.org/abs/2403.08937)：arXiv（Tambon, Florian ほか）・英語・確認日 2026-11-04
- [Are LLMs Reliable Code Reviewers? Systematic Overcorrection in Requirement Conformance Judgement](https://arxiv.org/abs/2603.00539)：arXiv（Jin, Haolin ほか）・英語・確認日 2026-11-04
- [Claude Code Gotchas](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)：DoltHub・英語・確認日 2026-11-04
- [Claude Code Tips I Wish I’d Had From Day One](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)：marmelab・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)
- plan mode の使いどころ（準備中）
- 仕様を先に固める（spec・インタビュー・モック先行）（準備中）
- 人間が読むべき差分の箇所（準備中）
- [git との付き合い方](../cli/working-with-git.md)
- [effort の段階と使い分け](../models/effort-levels.md)
- モデル別の癖と、プロンプトの合わせ方（準備中）

**関連**

- [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)
- 細かく指図するか、成果で頼むか（準備中）
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- 生成コードを自分のものにする（準備中）
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- 出力の形と分量を指定する（準備中）
- [意図と違うものが出てくる](not-what-i-meant.md)
- [確認ばかりで進まない・途中で止まる](keeps-stopping.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
