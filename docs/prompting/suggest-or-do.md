---
id: suggest-or-do
title: 提案してほしいのか、実行してほしいのか
aliases: [動詞をはっきりさせる, default_to_action]
type: concept
field: prompting
chapter: 何をどこまで頼むか
order: 70
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない, 合っていない]
scenes: [開発]
summary: 提案だけか、実行までか、懸念があれば止まって相談するのかを動詞で書き分けると、勝手に書き換えられることも提案で止まることも減る。既定でどちらに寄せるかも、指示に書いておける。
signs:
  - {type: symptom, text: 相談のつもりだったのに、ファイルを書き換えられた}
  - {type: goal, text: 大事な方針の変更では、手を止めて相談してほしい}
prerequisites: [four-specifics]
related: [keeps-stopping, does-more-than-asked, state-the-scope, when-to-plan, ask-for-options, permission-to-stop, model-quirks]
sources: [api-docs-prompting-best-practices, api-docs-prompting-opus-5, api-docs-prompting-claude-sonnet-5-5, cc-docs-best-practices]
volatility: 中
sections:
  - {title: 提案と実行を動詞で分ける, anchor: verbs}
  - {title: 既定の振る舞いを決める（すぐ実行するか、指示を待つか）, anchor: default}
  - {title: 懸念があれば止まって相談させる, anchor: stop-and-discuss}
  - {title: なぜ効くか、何に効くか, anchor: why}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：提案だけか、実行までか、止まって相談するのかを動詞で書き分けると、勝手に書き換えられることも提案で止まることも減る。
    - **いつ引くか**：相談のつもりだったのに、ファイルを書き換えられたとき。大事な方針の変更では、手を止めて相談してほしいとき。
    - **前提**：<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end -->
    - **関わる原理と原因**：原理は、望む動きを依頼に「見せる」こと。防ぐ原因は、6 つの原因のうち、望む動きが Claude に「見えていない」ことと、既定の動きが望む動きに「合っていない」ことである。

<!-- textlint-disable -->
別名：動詞をはっきりさせる・default_to_action
<!-- textlint-enable -->

Claude への依頼は、案を求めるものにも、実行を求めるものにも読める。どちらに読まれるかは、依頼に使う動詞と、指示に書いた既定で変わる。このページは、その書き分け方と、止まって相談させる書き方を扱う。

## 提案と実行を動詞で分ける {#verbs}

提案だけを頼むのか、実行まで頼むのかは、依頼に使う動詞で伝える。公式の指針は、「提案してもらえるか」と聞くと提案だけで終わることがある、と注意している。実行してほしいなら「この関数を書き換えて」のように明示する。逆に、相談のつもりで「〜するのはどうか」と書くと、実行の指示に読まれて、ファイルが書き換わることがある。モデル別の指針には、案や計画を求めたときは、出したら止めて着手しないよう指示する勧めもある。

同じ依頼を、2 通りに書き分けた例を示す。

```text
# Before：実行してほしいのに、提案で止まる
リトライ処理を指数バックオフにする案を出してもらえますか。

# After：実行まで頼む
src/client/retry.py の retry() を指数バックオフに書き換えて、
tests/test_retry.py を流して通ることを確かめて。
```

```text
# Before：相談のつもりなのに、書き換えられる
ログ出力を JSON にするのはどうだろう。

# After：提案だけを頼む
ログ出力を JSON にする案と、影響を受けるファイルを教えて。
ファイルは変更しないで。実装は、私が案を選んでから頼む。
```

1 組目の After では、動詞を「書き換えて」にし、対象のファイルと関数、終わりの確かめ方を足した。2 組目の After では、動詞を「教えて」にし、「変更しないで」と「実装は私が選んでから」を足した。対象と完了の書き方は <!-- link:begin four-specifics#done -->[具体性の 4 点（対象・状況・完了・手本） › 完了：何が起きれば終わりか](four-specifics.md#done)<!-- link:end --> が扱う。

動詞と、足す一言の組み合わせを表にまとめる。

| 頼みたいこと | 使う動詞の例 | 足す一言 |
| --- | --- | --- |
| 提案だけ | 案を出して・比べて・影響を教えて | 「ファイルは変更しないで」 |
| 実行まで | 書き換えて・実装して・直して | 終わりの確かめ方（「テストを流して」） |
| 案を見てから実行 | まず案を出して。私が選んだら実装して | 「選ぶまで着手しないで」 |
| 懸念があれば止まる | 実装の前に懸念を述べて、返事を待って | 止まる条件（「懸念があれば止まって相談させる」の節の雛形に例がある） |

提案と実行を 1 つの依頼に混ぜるときは、順序を書く。「案を出す、私が選ぶ、実装する」の 3 段で頼めば、勝手に先へ進むことも案の後で止まることも減る。選択肢を出させる頼み方は <!-- link:begin ask-for-options#choose -->選択肢と推奨案を出させる › 答えを選ぶ場面：選択肢と推奨案（準備中）<!-- link:end --> が扱う。

## 既定の振る舞いを決める（すぐ実行するか、指示を待つか） {#default}

毎回の依頼で動詞を書き分ける代わりに、既定の振る舞いを指示に一度だけ書いておける。公式の指針（確認日 2026-10-29）は、システムプロンプトに 2 つのタグを置く書き方を挙げている。1 つは、積極的に実行させる `<default_to_action>`。もう 1 つは、指示があるまで慎重に待たせる `<do_not_act_before_instructions>` である。

どちらに寄せるかは、作業の性質で決める。

!!! example "判断例：既定を実行に寄せるか、指示を待たせるか"
    - **状況**：小さな修正を次々に頼む日と、設計の相談を続ける日がある。どちらも同じリポジトリで Claude Code を使う。
    - **迷う候補**：既定を実行に寄せる。既定を指示待ちに寄せる。
    - **選んだもの**：修正が中心の日は実行に寄せ、相談が中心の日は指示待ちに寄せる。設計の相談では、毎回「変更しないで」と書く代わりに、既定を待ちにした。
    - **理由**：実行に寄せると、修正のたびに「進めて」と返す手間が減る。指示待ちに寄せると、相談の途中で書き換えられることが減る。どちらの既定にも、外れる場面がある。外れた場面は、その依頼の動詞で上書きする。

実行に寄せるほど、任せる幅が広がる。幅を広げる前に、戻せる仕組みと、止める仕組みを先に用意する。書き換えを git の差分で確かめられる状態にし、削除や push のように戻しにくい操作は、確認を求めるか、権限で止める。止める仕組みは <!-- link:begin state-the-scope#two-layers -->[範囲を伝える（やらないこと） › 例外を許さない範囲は仕組みで縛る（二層）](state-the-scope.md#two-layers)<!-- link:end --> が扱う。編集を止めたまま調べさせる手は <!-- link:begin when-to-plan#when -->[plan mode の使いどころ › 計画が効く作業、省いてよい作業](../cli/when-to-plan.md#when)<!-- link:end --> が扱う。

既定を書く場所は、面で違う。

=== "アプリ"

    会話の最初の依頼に、既定を 1 文で書く。指示を保存して使い回す場所の手順は、このページでは確かめていない。

=== "Claude Code"

    CLAUDE.md か、セッションの最初の依頼に書く。CLAUDE.md の文章は、守らせる鍵ではなく、依頼の一部として読まれる。例外を許さない操作は、権限やフックで止める。

=== "API"

    システムプロンプトに書く。`<default_to_action>` と `<do_not_act_before_instructions>` は、システムプロンプトに置く前提で公式の指針に載っている。

既定の書き方の雛形を 2 つ示す。実行に寄せる雛形には、確認を求める操作の欄がある。ここを空にしないことが、寄せすぎを防ぐ。

<!-- gen:begin snippet suggest-or-do/default-to-action -->
<!-- textlint-disable -->

??? example "雛形：既定を「実行」に寄せる指示"

    ```text
    <default_to_action>
    変更を勧められる場面では、案を述べるだけで終えず、変更そのものを行う。
    意図がはっきりしないときは、最も役に立つと考えられる行動を推測して進める。
    ファイルの読み取りと検索は、確認なしで行ってよい。
    次の操作は、実行の前に私へ確認する：<確認してほしい操作。例：ファイルの削除、git push、外部への送信>
    </default_to_action>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet suggest-or-do/default-to-action -->

<!-- gen:begin snippet suggest-or-do/wait-for-instructions -->
<!-- textlint-disable -->

??? example "雛形：既定を「指示を待つ」に寄せる指示"

    ```text
    <do_not_act_before_instructions>
    私が明示的に指示するまで、ファイルの変更と、読み取り以外のコマンドの実行をしない。
    意図がはっきりしないときは、実行せず、調べた内容と案と質問を返す。
    「〜はどうか」「〜を考えて」「〜を比べて」は、案を求める言葉であり、実行の指示ではない。
    実行を頼むときは、私が「書き換えて」「実装して」のように動詞で書く。
    </do_not_act_before_instructions>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet suggest-or-do/wait-for-instructions -->

モデルや版によって、指示がないときの既定は違う。確認のために止まりすぎる設定もあれば、頼まれていないことまで進める設定もある。傾向の見方は <!-- link:begin model-quirks#official-guidance -->モデル別の癖と、プロンプトの合わせ方 › 公式の指針に出てくる傾向（準備中）<!-- link:end --> が扱う。

## 懸念があれば止まって相談させる {#stop-and-discuss}

懸念を見つけたときの動きも、依頼で書き分けられる。書き方は 2 通りある。

- **述べて続ける**：依頼が誤っていそうなら一文でそう言い、依頼どおりに続ける。公式のモデル別の指針に、この書き方の推奨がある。小さな変更で止まりすぎるのを防ぐ。
- **止まって議論する**：懸念があれば、一文で済ませずに手を止めて議論する。方針と評価の方法、評価の指標、入力範囲の解釈に関わる変更に向く。

後者は、前者と逆向きの指示を明示する書き方である。この辞典の推奨であり、公式の最新のモデル別の指針に同じ記述があるかは、確かめていない（推論・実践例なし）。方針や評価の変更は、後から直すと、それまでの作業の結果ごとやり直しになりやすい。そのため、止めて議論させる価値が大きい。

2 つの書き方は、変更の種類で使い分ける。

!!! example "判断例：述べて続けるか、止まって議論するか"
    - **状況**：評価用のスクリプトを直す作業を頼んだ。Claude が、入力の範囲を「直近 7 日」と読む解釈は仕様と違うかもしれない、と気づいた。
    - **迷う候補**：懸念を一文で述べて、依頼どおり続ける。手を止めて、解釈を私に確かめる。
    - **選んだもの**：手を止めて、解釈を確かめる。
    - **理由**：入力範囲の解釈は、評価の結果すべてに効く。誤ったまま続けると、出てきた数字を全部読み直すことになる。変数名の修正のような小さな変更なら、述べて続けるほうが速い。

雛形を示す。止めたい変更の種類の欄は、自分の作業に合わせて書き換える。

<!-- gen:begin snippet suggest-or-do/stop-and-discuss -->
<!-- textlint-disable -->

??? example "雛形：懸念があれば止まって相談させる指示"

    ```text
    次の種類の変更では、懸念があるとき、一文で述べて続けない。そこで手を止めて、私と議論する。
    - <止めたい変更の種類。例：方針・戦略の変更>
    - <例：評価の方法や指標の変更>
    - <例：入力の範囲や仕様の解釈に関わる変更>

    止まるときは、次の 3 つを書いて、私の返事を待つ。
    1. 気になる点
    2. 選択肢（それぞれの影響を一言で）
    3. 推奨とその理由
    返事が来るまで、その変更はしない。

    上の種類に当たらない変更では、懸念を一文で述べたうえで、依頼どおりに続けてよい。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet suggest-or-do/stop-and-discuss -->

止まる条件の書き方と、モデルによる差は <!-- link:begin permission-to-stop#conditions -->止まって報告する権利を渡す › 止まって報告する条件を書く（準備中）<!-- link:end --> が扱う。

## なぜ効くか、何に効くか {#why}

提案か実行かは、依頼の中身だけでは決まらないことが多い。依頼にも会話にも書かれていない望みは、Claude に見えない。見えないところは、Claude が推測で埋める。その推測は、モデルや設定の既定しだいで、提案の側にも実行の側にも傾く。

このページの技法は、原理の「見せる」にあたる。案だけがほしいのか、実行までほしいのか、どこで止まってほしいのかという望みを、動詞と一言で依頼に見せる。防ぐ原因は 2 つある。

- **見えていない**：望む動きを書いていないために、Claude が推測で埋める。動詞を書き分ければ埋まる。
- **合っていない**：モデルや設定の既定の動きが、頼みたい動きと合っていない。既定を指示に書けば合わせられる。

「見えていない」を埋める点で、このページは前提の <!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end --> の続きにあたる。4 点が依頼の中身を見せるのに対し、このページは依頼の動きを見せる。

## 効かない場面とやりすぎ {#limits}

動詞や既定を書いても効かない場面がある。

- **言葉は鍵ではない**：「変更しないで」と書いても、権限が許していれば、書き換えが起きる可能性は残る。例外を許さない範囲は、言葉ではなく権限やフックで縛る。縛り方は <!-- link:begin state-the-scope#two-layers -->[範囲を伝える（やらないこと） › 例外を許さない範囲は仕組みで縛る（二層）](state-the-scope.md#two-layers)<!-- link:end --> と <!-- link:begin permission-to-stop#with-structure -->止まって報告する権利を渡す › 書き換えられない仕組みと組み合わせる（準備中）<!-- link:end --> が扱う。
- **強すぎる書き方**：「必ず」「絶対に」を重ねると、指示に強く反応するモデルでは、効きすぎることがある。公式の指針は、「必ず使え」のような強い書き方を、「〜のときに使う」という条件の書き方に和らげるよう勧めている。
- **既定の書きすぎ**：実行に寄せる指示と、待たせる指示を両方置くと、どちらに従うかが読めなくなる。既定は 1 つにして、例外は依頼の動詞で上書きする。
- **止まりすぎ・やりすぎが続くとき**：動詞を直しても止まり続けるときの原因の切り分けは <!-- link:begin keeps-stopping#diagnosis -->[確認ばかりで進まない・途中で止まる › 原因を安く確かめる順](../symptoms/keeps-stopping.md#diagnosis)<!-- link:end --> が扱う。頼んでいないことまで進むときの切り分けは <!-- link:begin does-more-than-asked#diagnosis -->[頼んでいないことまでやる（過剰設計） › 原因を安く確かめる順](../symptoms/does-more-than-asked.md#diagnosis)<!-- link:end --> が扱う。範囲を伝える書き方は <!-- link:begin state-the-scope#anti-goals -->[範囲を伝える（やらないこと） › やらないことを書く](state-the-scope.md#anti-goals)<!-- link:end --> が扱う。
- **版で変わる**：既定の傾向は、版が変わると変わる。雛形の効き方は、新しいセッションで試して記録する。記録の付け方は <!-- link:begin model-quirks#observe-and-record -->モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する（準備中）<!-- link:end --> が扱う。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)

**次に読む**

- 選択肢と推奨案を出させる（準備中）

**関連**

- [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- [範囲を伝える（やらないこと）](state-the-scope.md)
- [plan mode の使いどころ](../cli/when-to-plan.md)
- 止まって報告する権利を渡す（準備中）
- モデル別の癖と、プロンプトの合わせ方（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
