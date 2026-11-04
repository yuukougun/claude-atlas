---
id: define-done
title: 「完了」を定義して渡す
aliases: [完了条件, 完了の定義, Definition of Done, 終わりの条件を渡す]
type: concept
field: verify
chapter: 完了を確かめる
order: 10
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる, 見せる]
prevents: [確かめていない, 見えていない]
pitfalls: []
scenes: [開発, 文章]
summary: どのコマンドがどう返れば終わりか・変えてはならないもの・止まって報告する条件を決め、「完了」を測れる形で Claude に渡せる。終わったように見えた所で止まる理由も分かる。
signs:
  - {type: goal, text: どこまでやったら終わりかを、はっきり伝えたい}
  - {type: goal, text: どのコマンドがどう返れば完了かを、依頼に書いて渡したい}
  - {type: goal, text: 席を外す前に、終わりの条件を決めて渡したい}
prerequisites: [agent-loop]
related: [evidence-not-reports, verification-ladder, four-specifics, ask-for-outcomes, state-the-scope, permission-to-stop, claims-done-but-isnt, does-more-than-asked, tests-first, spec-first, goal-until-done, measure-changes, check-the-metric]
tracks: []
outdated_advice: [keep-going-dont-be-lazy]
sources: [cc-docs-best-practices, cc-docs-goal, api-docs-prompting-opus-5, cc-issue-46940, cc-issue-64286, anthropic-eng-building-c-compiler]
volatility: 低
sections:
  - {title: 終わったように見えた所で止まる, anchor: why-it-stops}
  - {title: 同じ依頼に完了の定義を足す, anchor: before-after}
  - {title: 完了の定義に入れるもの, anchor: what-to-include}
  - {title: 止まって報告する条件, anchor: stop-and-report}
  - {title: 面ごとの渡し方, anchor: by-surface}
  - {title: 完了の定義を含む依頼の雛形, anchor: templates}
  - {title: 何に効くか, anchor: what-it-helps}
  - {title: 誤解と、効かない場面, anchor: misreadings}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：実行するコマンドとその結果・変えないもの・止まって報告する条件を決めて渡すと、終わったように見えた所での停止を防げる
    - **いつ引くか**：どこまでやったら終わりかを伝えたいとき。どのコマンドがどう返れば完了かを書きたいとき。席を外す前に終わりを決めたいとき
    - **関わる原理と原因**：原理は、結果を「確かめる」ことと、確かめ方を Claude に「見せる」こと。防ぐ原因は「確かめていない」と「見えていない」である
    - **前提**：<!-- link:begin agent-loop -->[エージェントループと tool use](../basics/agent-loop.md)<!-- link:end -->

<!-- textlint-disable -->
別名：完了条件・完了の定義・Definition of Done・終わりの条件を渡す
<!-- textlint-enable -->

「完了」を定義して渡すとは、どこまでやれば終わりかを、測れる形で依頼に書くことである。測れる形とは、実行するコマンドとその結果、変えてはならないもの、止まって報告する条件の 3 つを指す。

## 終わったように見えた所で止まる {#why-it-stops}

Claude は、作業が終わったように見えた時点で止まる。本当に終わったかを判定するものを実行できなければ、「終わったように見える」ことしか判断材料がない。これは公式の [Best practices](https://code.claude.com/docs/en/best-practices) の説明である。

この止まり方が実害になった例が、Claude Code の Issue に報告されている（根拠：弱。単独の経験談）。

- [Issue #46940](https://github.com/anthropics/claude-code/issues/46940)（2026-04-12、Opus 4.6）：回帰テストが 4992 件中 4985 件の通過に落ちたのに、件数を書き換えて「ALL PASSED」と報告し、壊れたコードを commit した。
- [Issue #64286](https://github.com/anthropics/claude-code/issues/64286)（2026-05-31、Opus 4.8・effort High）：「162 tests green」と報告したが、実際は 3 件のテストが失敗していた。ユーザーの準備ができていない状態で、main へのマージと push まで進んだ。

どちらも、合否を返すものが完了の定義に入っておらず、報告が事実と離れても気づく手段がなかった。報告が事実と違うときの原因の切り分けは<!-- link:begin claims-done-but-isnt#diagnosis -->[「完了」と言うが終わっていない › 原因を安く確かめる順](../symptoms/claims-done-but-isnt.md#diagnosis)<!-- link:end -->に任せる。止まる仕組みそのものは<!-- link:begin agent-loop#why-stops -->[エージェントループと tool use › 確かめる手段がないと、終わったように見えたところで止まる](../basics/agent-loop.md#why-stops)<!-- link:end -->で扱っている。

## 同じ依頼に完了の定義を足す {#before-after}

同じバグ修正の依頼を、完了の定義のない形と、ある形で並べる。次は説明のために作った例で、Claude に試した結果ではない。

**Before**

```text
カートの合計がおかしいので直して
```

**After**

```text
カートの合計が、割引クーポンを使った注文で 1 円ずれる。src/cart/total.ts の合計の計算を直して。

完了の定義：
- npm test -- cart を実行し、失敗 0 件で終わること
- 実行したコマンドと出力をそのまま貼ること。件数は「通った数 / 全体の数」で書くこと

変えないもの：
- tests/cart 以下のテストファイル
- calculateTotal の名前と引数

止まって報告する条件：
- 完了のコマンドが実行できないとき
- テストを変えないと通らないとき
```

After で足したものは 3 つある。1 つ目は、完了のコマンドと、期待する結果である。2 つ目は、変えてはならないファイルと関数である。3 つ目は、回避せずに止まる条件である。症状と対象の書き方は<!-- link:begin four-specifics#done -->[具体性の 4 点（対象・状況・完了・手本） › 完了：何が起きれば終わりか](../prompting/four-specifics.md#done)<!-- link:end -->が持つ。ここでは、完了の部分だけを詳しく見る。

## 完了の定義に入れるもの {#what-to-include}

依頼には、完了の定義、変えてはならないもの、止まって報告する条件の 3 つを含める。止まる条件は「止まって報告する条件」の節で述べ、この節では完了の定義と変えてはならないものを見る。

**完了の定義：どのコマンドがどの出力を返せば完了か。** 合否が機械的に返るものを選ぶ。公式の Best practices が挙げるのは、テストファイル、ビルドの終了コード、linter、期待する出力との diff を取るスクリプト、モックとブラウザのスクリーンショットの比較などである。リポジトリにすでにあるなら、それを実行するコマンドが、CLAUDE.md の中で最も役立つ 1 行になる。

**証拠の形：** 完了を「通った」の一言ではなく、実行したコマンドと出力で受け取れるようにする。「All tests pass」だけでは情報がほとんどない。見ていなかったセッションでは、実行したコマンドとその出力が唯一の証拠になる。証拠の形は<!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](evidence-not-reports.md#what-counts)<!-- link:end -->で扱う。

**変えてはならないもの：** 完了の条件を満たす近道として、テストや設定を書き換えられることがある。完了のコマンドが指すテストファイル、公開している関数の名前と引数、設定などを書く。言葉で書いても守られないものは、<!-- link:begin state-the-scope#two-layers -->[範囲を伝える（やらないこと） › 例外を許さない範囲は仕組みで縛る（二層）](../prompting/state-the-scope.md#two-layers)<!-- link:end -->のとおり、権限やフックで縛る。テストの書き換えを読むときの注意は<!-- link:begin tests-first#review-test-changes -->テストを先に書かせる › テストの変更は特に読む（準備中）<!-- link:end -->にある。

!!! example "判断例：完了のコマンドを何にするか"
    - **状況**：ライブラリの更新に伴う修正を、夜のうちに Claude へ任せる。リポジトリには、数秒で終わる単体テストと、数十分かかる結合テストがある。
    - **迷う候補**：単体テストだけを完了のコマンドにする。結合テストまで含める。
    - **選んだもの**：単体テストを完了のコマンドにし、結合テストは、朝に自分が実行する確認として別に残す。
    - **理由**：完了のコマンドは、Claude が何度も実行できる軽さが要る。重すぎると、実行が後回しにされたり、途中で切れたりしやすい。結合テストの範囲に変更が及ぶなら、それも完了に含める。軽さと確かさのどちらを取るかは、直す範囲が決める。

## 止まって報告する条件 {#stop-and-report}

止まって報告する条件とは、完了を目指す途中で、先に進まず状況を報告してほしい場合を、依頼に書いておくものである。完了の定義だけを渡すと、完了のコマンドが通らないとき、Claude はコマンドを通すこと自体を目標にしてしまうことがある。止まる条件は、その逃げ道を塞ぐ。（推論・実践例なし）

条件の例は次のとおりである。

- 完了のコマンドが、環境の問題で実行できないとき。
- 結果が空、または途中で切れているとき。
- 完了のために、変えてはならないものを変える必要が出たとき。
- テストや検証の側が間違っていると判断したとき。回避せず、根拠を添えて報告させる。
- 触ってよい範囲の外に手を出さないと進めないとき。

席を外す前には、5 つの問いに答えておく。完了の定義は何か。自分で確かめられるか。触ってよい範囲はどこか。何で止まるか（`--max-turns` や `--max-budget-usd` のような上限）。結果を誰が承認するか。これは公式の Best practices にある。

「止まってよい」と書くだけで、どれほど止まるようになるかには、モデルによる差がある。その範囲は<!-- link:begin permission-to-stop#limits -->止まって報告する権利を渡す › 言葉の許可が効く範囲（モデルによる差）（準備中）<!-- link:end -->に、書き換えられない仕組みとの組み合わせは<!-- link:begin permission-to-stop#with-structure -->止まって報告する権利を渡す › 書き換えられない仕組みと組み合わせる（準備中）<!-- link:end -->にある。この辞典では、止まる条件を完了の定義の一部として書く。止まる権利そのものの効き方は、そちらに任せる。

## 面ごとの渡し方 {#by-surface}

渡す手段は面で違う。完了の定義の 3 つの要素は同じで、確かめる手段が変わる。

=== "アプリ"

    コードを実行して合否を返す場面は限られるので、完了を形式・分量・合格の基準として書く。見出しの構成、字数の範囲、含めるべき項目の一覧を渡し、最後に項目ごとに満たしたかを一覧で示させる。書き写せる型は[雛形](#templates)の文章向けのものにある。

=== "Claude Code"

    完了のコマンドを依頼に書く。繰り返し使うコマンドは CLAUDE.md の 1 行にしておくと、毎回書かずに済む。席を外す間も続けさせたいなら、完了の条件を満たすまでターンを続ける `/goal` がある。条件の書き方は<!-- link:begin goal-until-done#writing-conditions -->[/goal（完了するまで続けさせる） › 条件の書き方（終わりの状態・証明・変えないもの・上限）](../delegate/goal-until-done.md#writing-conditions)<!-- link:end -->を見る。終わりを止める強い仕組みまで含めた段の選び方は<!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](verification-ladder.md#choose-step)<!-- link:end -->にある。

=== "API"

    呼び出しの指示（プロンプト）に、完了を形式・分量・合格の基準として書く。コマンドを実行する道具を Claude に渡していない呼び出しでは、完了のコマンドは実行できない。合否を返す道具を渡せるなら、輪を閉じられる。その渡し方は<!-- link:begin agent-loop#close-the-loop -->[エージェントループと tool use › 合否を返すものを渡してループを閉じる](../basics/agent-loop.md#close-the-loop)<!-- link:end -->で扱う。

## 完了の定義を含む依頼の雛形 {#templates}

次の 2 つは、完了のコマンドと期待する出力・変えないもの・止まって報告する条件を含む依頼の型である。欄を自分の作業に置き換えて使う。

<!-- gen:begin snippet define-done/request -->
<!-- textlint-disable -->

??? example "雛形：完了の定義を含む依頼（開発）"

    ```text
    <やってほしいこと。対象のファイルと、いまの症状>

    完了の定義：
    - <完了のコマンド> を実行し、<期待する結果。例：終了コード 0、失敗 0 件> が返ること
    - 実行したコマンドと出力をそのまま返答に貼ること。件数は「通った数 / 全体の数」の形で書くこと
    - 出力が空、または途中で切れていたら、完了とは書かず、そのことを報告すること

    変えないもの：
    - <変えてはならないファイルや設定。例：既存のテスト、公開している関数の名前と引数>

    止まって報告する条件：
    - 完了のコマンドが実行できないとき
    - 完了のために「変えないもの」を変える必要が出たとき
    - テストや検証の側が間違っていると思うとき（回避せず、根拠を添えて報告すること）
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet define-done/request -->

文章を頼むときは、コマンドの代わりに、形式・分量・合格の基準で完了を書く。

<!-- gen:begin snippet define-done/request-writing -->
<!-- textlint-disable -->

??? example "雛形：完了の定義を含む依頼（文章）"

    ```text
    <書いてほしい文章。読み手と用途>

    完了の定義：
    - 形式：<見出しの構成、表を使うか、箇条にするか>
    - 分量：<字数の範囲>
    - 合格の基準：次の項目をすべて含むこと
      1. <含める項目。例：結論>
      2. <含める項目。例：根拠 3 点>
      3. <含める項目。例：次にとる行動>
    - 最後に、項目ごとに「含めた・含めていない」を一覧で示すこと

    変えないもの：
    - <元の文章のうち、言い換えてはならない部分。例：引用、数値、固有名詞>

    止まって報告する条件：
    - 資料に書かれていない数値や事実が要るときは、推測で埋めずに、足りない点を書き出して確認すること
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet define-done/request-writing -->

## 何に効くか {#what-it-helps}

完了の定義が防ぐのは、Claude 側の原因のうち、「確かめていない」と「見えていない」の 2 つである。

- **確かめていない**（原理：確かめる）。完了のコマンドが、終わったかどうかを判定する手段になる。手段がなければ、Claude は「終わったように見える」所で止まる。コマンドを渡すと、合否が返るまで作業を続ける理由が生まれる。
- **見えていない**（原理：見せる）。どこまでやれば終わりか、何を変えてはならないかは、依頼や会話に書かれていなければ Claude に見えない。完了の定義は、頭の中にある終わりの基準を、Claude が読める形に出す。

関連する近い頼み方との分担は次のとおりである。対象・状況・完了の形・手本の 4 点を依頼に書く頼み方は<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)<!-- link:end -->で、完了はその 1 点にあたる。目的と完了を成果で渡す考え方は<!-- link:begin ask-for-outcomes -->細かく指図するか、成果で頼むか（準備中）<!-- link:end -->にある。

## 誤解と、効かない場面 {#misreadings}

**「確かめて」と書き足せば、完了の定義になる。** ならない。言葉で「double-check して」と書き足すことは、公式の [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) が、外すよう勧める書き足しに挙げている。確かめる手段を渡すことと、言葉で命じることは区別する。手段の渡し方は<!-- link:begin verification-ladder#verbal-checks -->[検証の階段 › 「念のため確認して」と書き足すより、確かめる手段を渡す](verification-ladder.md#verbal-checks)<!-- link:end -->にある。

**「keep going」と書けば、最後までやり切る。** 以前のモデルは長い作業の途中で止まりやすく、続けるよう促す一言が効いた。いまは、こうした一言を消し、通すべきテストのような確かめる手段を渡すのが公式の勧めである。途中で止まったら続けるよう伝え、誰も見ていない実行は、完了の条件を満たすまで続けさせる機能で続けさせる。行の詳細は<!-- link:begin outdated-advice-ledger#keep-going-dont-be-lazy -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#keep-going-dont-be-lazy)<!-- link:end -->にある。

**完了のコマンドが通れば、本当に終わっている。** 完了の定義の効き目は、検証器の質で決まる。並列の Claude 群で C コンパイラを作った事例の記事は、エージェントが与えられた問題を解くので検証器はほぼ完璧でなければならない、と述べる（[Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/research/building-c-compiler)）。指標だけを満たし、本当の目的を外れる変更も起きうる。指標と目的のずれは<!-- link:begin check-the-metric#mismatch -->評価指標そのものを確かめる › 指標と目的のずれ（準備中）<!-- link:end -->で確かめる。

**完了の定義を細かく書くほど、よい。** 目的と完了は成果で渡し、攻める場所と測り方は具体的に書く。成果の条件だけを渡して中身を任せすぎると、迷走や指標だけを満たす変更が起きうる。分け方は<!-- link:begin ask-for-outcomes#outcomes -->細かく指図するか、成果で頼むか › 成果で示すもの：目的と完了の条件（準備中）<!-- link:end -->にある。

効かない場面もある。完了の定義が機械的に測れない作業では、合否を返すコマンドを置けない。その場合は、含めるべき項目の一覧のような合格の基準を渡し、別の者に確かめさせる段へ移る。仕様が固まっていない大きな機能は、完了を決める前に、<!-- link:begin spec-first -->[仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)<!-- link:end -->の手順で仕様を詰める。変更が効いたかを、複数回の試行で比べて測るのは<!-- link:begin measure-changes -->[変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)<!-- link:end -->の役割である。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Keep Claude working toward a goal](https://code.claude.com/docs/en/goal)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [Claude fabricates test results - reports ALL PASSED when tests are FAILING（Issue #46940）](https://github.com/anthropics/claude-code/issues/46940)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [\[Bug\] Claude Code fabricated test results and pushed untested code to main branch (Opus 4.8 @ Effort = High)（Issue #64286）](https://github.com/anthropics/claude-code/issues/64286)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/research/building-c-compiler)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [エージェントループと tool use](../basics/agent-loop.md)

**次に読む**

- [タスクと定期タスク（Cowork）](../app/tasks-and-schedules-in-the-app.md)
- [報告ではなく証拠を求める](evidence-not-reports.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)
- 細かく指図するか、成果で頼むか（準備中）
- テストを先に書かせる（準備中）
- AI に書かせたテストの落とし穴（準備中）

**関連**

- [検証の階段](verification-ladder.md)
- [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)
- [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)
- 止まって報告する権利を渡す（準備中）
- [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- 評価指標そのものを確かめる（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
