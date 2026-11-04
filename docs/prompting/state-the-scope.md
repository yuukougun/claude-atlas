---
id: state-the-scope
title: 範囲を伝える（やらないこと）
aliases: [anti-goals, スコープを絞る, 頼んだ範囲で, やらないことを書く]
type: concept
field: prompting
chapter: 何をどこまで頼むか
order: 80
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる, 縛る]
prevents: [見えていない, 合っていない]
scenes: [開発]
summary: 依頼に、やること・やらないこと・触ってよい範囲を書くと、頼んでいない機能や変更が増えにくくなる。例外を許さない範囲は、言葉ではなく権限やフックで縛る。
signs:
  - {type: goal, text: 小さな修正は、小さいまま終わらせたい}
  - {type: goal, text: 触ってよいファイルを限りたい}
prerequisites: [four-specifics, request-vs-lock]
related: [does-more-than-asked, say-what-you-want, suggest-or-do, give-reasons, permission-rules, protected-paths, when-to-lock#spoken-rules-fade, model-quirks]
sources: [cc-docs-best-practices, api-docs-prompting-best-practices, api-docs-prompting-opus-5, api-docs-prompting-claude-sonnet-5-5, velvetshark-stop-prompting-code-let-interview, thorstenball-talks-prompt]
volatility: 低
sections:
  - {title: やらないことを書く, anchor: anti-goals}
  - {title: いまの作業に要る最小限を求める, anchor: minimum}
  - {title: 範囲を書く雛形, anchor: templates}
  - {title: 例外を許さない範囲は仕組みで縛る（二層）, anchor: two-layers}
  - {title: 何に効くか, anchor: effects}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：依頼にやること・やらないこと・触ってよい範囲を書くと、頼んでいない変更が増えにくくなる理由と書き方が分かる。
    - **いつ引くか**：小さな修正を小さいまま終わらせたいとき、触ってよいファイルを限りたいとき。
    - **前提**：<!-- link:begin four-specifics -->[具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)<!-- link:end -->・<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：anti-goals・スコープを絞る・頼んだ範囲で・やらないことを書く
<!-- textlint-enable -->

範囲を伝えるとは、依頼に「やること」のほかに「やらないこと」と「触ってよい範囲」を書くことである。Claude は頼まれていない機能やファイルを足すことがあるので、境目を先に見せておく。言葉で頼んでも守られない範囲は、権限やフックで縛る。

## やらないことを書く {#anti-goals}

やらないことを書くとは、依頼の中に、手を付けない対象と、足さないものを名指しで置くことである。やることだけを書いた依頼では、Claude は境目を推測で埋める。

同じ依頼を、範囲を書かない形と書く形で並べる。

```text
Before
ログイン後のリダイレクトを直して。

After
ログイン後の戻り先が `/` に固定されている。ログイン前に開いていたページへ戻るように直してほしい。
やること：`src/auth/redirect.ts` の戻り先の決め方を直す。
やらないこと：`src/auth/` の外のファイルを変えない。新しい依存を足さない。周りの整形や名前の付け替えをしない。
触ってよい範囲：`src/auth/redirect.ts` と `tests/auth/redirect.test.ts` だけ。
```

After で足したものは 3 つある。やること（直す場所と症状）、やらないこと（外のファイル・依存・ついでの整理）、触ってよい範囲（ファイル名で限る）である。症状・対象・完了を書く部分は <!-- link:begin four-specifics#before-after -->[具体性の 4 点（対象・状況・完了・手本） › 同じ依頼を 4 点で書き直す](four-specifics.md#before-after)<!-- link:end --> と同じ考え方で、ここでは境目を足している。

効く理由は、境目が Claude の側から見えないことにある。Claude は、どこまでが今回の依頼で、どこからが別の人の持ち物かを、依頼文とコードから推測する。公式の Claude Code の Best practices にも、曖昧な依頼に対象と条件を足して書き直す対比がある。実践者の報告には、仕様に anti-goals を書く習慣や、守るべき制約は書かなければモデルには分からないという指摘もある。これらは単独の経験談で根拠は弱い。ただ、境目を書く手間は小さいので、この辞典は「境目は書く」ことを勧める。

「やらないこと」には理由を添える。理由があると、Claude は書かれていない近い場面にも判断を応用できる。理由の書き方は <!-- link:begin give-reasons -->[理由を添える](give-reasons.md)<!-- link:end --> の持ち分である。

「やらないこと」を禁止形だけで並べると、望む形で書いたほうが守られやすい、という別の問題に当たる。書き換え方は <!-- link:begin say-what-you-want#rewrite -->否定形ではなく、望む形で書く › 禁止を望む形に書き換える（準備中）<!-- link:end --> にある。

## いまの作業に要る最小限を求める {#minimum}

最小限を求めるとは、禁止を並べる代わりに、今回の作業に要るだけを望む形で頼むことである。公式の Prompting best practices には、作り込みすぎを抑える方針として、次の趣旨の一文がある（2026-10-29 に確認）。

> The right amount of complexity is the minimum needed for the current task.

モデル別の指針にも、範囲を守らせる一文が載っている（どちらも 2026-10-29 に確認）。

- Prompting Claude Opus 5：`Deliver what was asked, at the scope intended.`
- Prompting Claude Sonnet 5.5：`Don't add features, tests, files, docs or refactors that weren't asked for.`

Sonnet 5.5 の指針は、effort を上げると頼まれていないことまでやりがちになる、とも述べている。モデルや effort による傾向の違いは <!-- link:begin model-quirks#official-guidance -->モデル別の癖と、プロンプトの合わせ方 › 公式の指針に出てくる傾向（準備中）<!-- link:end --> で見る。傾向は版で変わるので、文面を暗記せず、自分の環境で観察する。

「最小限」は、気づいたことの置き場所とセットで頼む。ついでの直しを禁じるだけだと、気づいた問題が消える。「直さずに、返答の最後に書く」と頼めば、差分は小さいまま、気づきも残る。提案で止めるか実行までさせるかは、動詞で書き分ける（<!-- link:begin suggest-or-do#verbs -->[提案してほしいのか、実行してほしいのか › 提案と実行を動詞で分ける](suggest-or-do.md#verbs)<!-- link:end -->）。

範囲の外に出ないと終わらないときは、黙って広げるのではなく止まって相談する、と先に決めておく。止まる条件の書き方は <!-- link:begin suggest-or-do#stop-and-discuss -->[提案してほしいのか、実行してほしいのか › 懸念があれば止まって相談させる](suggest-or-do.md#stop-and-discuss)<!-- link:end --> にある。

## 範囲を書く雛形 {#templates}

依頼の本文に置く雛形は、やること・やらないこと・触ってよい範囲・範囲の外に出るときの扱いを、1 つの依頼にまとめて並べたものである。かっこの中の理由は、自分の事情に置き換える。

<!-- gen:begin snippet state-the-scope/scope-request -->
<!-- textlint-disable -->

??? example "雛形：やること・やらないこと・触ってよい範囲を足した依頼"

    ```markdown
    ログイン後の戻り先が `/` に固定されている。ログイン前に開いていたページへ戻るように直してほしい。

    やること：
    - `src/auth/redirect.ts` の、戻り先の決め方を直す
    - 戻り先が外部サイトのときは `/` に戻す（既存の `isSafeRedirect` を使う）

    やらないこと：
    - `src/auth/` の外のファイルを変えない（別のチームの持ち物で、レビューの宛先が変わるため）
    - 新しい依存を足さない
    - 周りの整形・名前の付け替え・ついでの整理をしない。気づいたことは、直さずに返答の最後へ書く

    触ってよい範囲：`src/auth/redirect.ts` と `tests/auth/redirect.test.ts` だけ。
    この範囲の外を変えないと終わらないと分かったら、変えずに止めて、理由と案を書いて相談する。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet state-the-scope/scope-request -->

毎回の依頼に同じ内容を書くなら、理由と相談の基準だけを CLAUDE.md へ移す。例外を許さない禁止は、ここに書かず、次の節の仕組みへ移す。

<!-- gen:begin snippet state-the-scope/scope-claude-md -->
<!-- textlint-disable -->

??? example "雛形：理由と相談の基準だけを書く CLAUDE.md の節"

    ```markdown
    ## 変更の範囲

    - 頼まれた変更だけを行う。ついでの整理・名前の付け替え・機能の追加はしない。気づいたことは返答の最後に書く（理由：差分が大きいと、レビューで本来の変更を見落とすため）
    - 次のときは、直す前に止めて相談する：頼まれた範囲の外のファイルを変えないと終わらないとき、公開されている関数の形を変えるとき、新しい依存を足すとき
    - `migrations/` は、変える必要があると思っても案を書くだけにする（理由：適用済みの移行を変えると、環境ごとに結果が分かれるため）。この規則は権限のルールでも別に止めている
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet state-the-scope/scope-claude-md -->

## 例外を許さない範囲は仕組みで縛る（二層） {#two-layers}

二層とは、範囲の指定を、Claude に読んで判断させる層と、仕組みで必ず止める層に分けることである。依頼文や CLAUDE.md に書いた範囲は、Claude が読んで判断する「お願い」にとどまる（<!-- link:begin request-vs-lock#why -->[お願いと鍵（決定論的か、非決定論的か） › なぜそうなるか](../basics/request-vs-lock.md#why)<!-- link:end -->）。例外が 1 つもない範囲は、お願いのままにしない。

分け方は次のとおりである。

- 例外を許さない禁止（このディレクトリは書き換えない、このコマンドは実行しない）は、deny ルールかフックで強制する。書き方は <!-- link:begin permission-rules#minimal -->[権限ルール（allow・ask・deny） › 最小の使い方](../enforce/permission-rules.md#minimal)<!-- link:end --> にある
- CLAUDE.md には、その禁止の理由と、止まって相談する基準だけを書く。判断を含む規則は、お願いのままにする
- 依頼文には、今回の作業の範囲を書く。作業ごとに変わる範囲は、仕組みに移さない

仕組みにも穴がある。当たらないパスのルールや、子プロセスに効かないものがあるので、<!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end --> と <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end --> を確かめる。作業ディレクトリの外への書き込みを閉じる設定は <!-- link:begin protected-paths#outside-working-directory -->消せない場所・触れない場所（protected paths） › 作業ディレクトリの外への読み書きを閉じる（準備中）<!-- link:end --> にある。

会話の途中で言った禁止は、長いセッションで圧縮されると消えることがある。同じ注意を 2 回した、強調しても破られた、というときが仕組みに移す合図である（<!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<!-- link:end -->）。

面ごとに、縛る手段は違う。

=== "アプリ"
    依頼の本文と、プロジェクトの指示に、範囲と理由を書く。アプリで依頼の範囲を仕組みで縛る手段は、この辞典では未確認である。

=== "Claude Code"
    依頼の本文に今回の範囲を書き、CLAUDE.md に理由と相談の基準を書く。例外を許さない範囲は、deny ルールかフックで縛る。

=== "API"
    システムプロンプトと各依頼に範囲を書く。ツールを実行するのは自分のコードなので、範囲の外の操作を拒否する処理は、そのコードの側に置く（推論・実践例なし）。

!!! example "判断例：「migrations/ に触るな」をどこに書くか"
    - **状況**：小さな修正の依頼が多いリポジトリで、適用済みの `migrations/` を書き換える変更が一度混ざった。
    - **迷う候補**：依頼文と CLAUDE.md に「触るな」と強く書く。あるいは、`migrations/` への書き込みを deny ルールにして、CLAUDE.md には理由だけを書く。
    - **選んだもの**：後者。`migrations/` を deny ルールで止め、CLAUDE.md には「適用済みの移行を変えると環境ごとに結果が分かれる。変える必要があるときは案を書く」と理由と相談の基準を書く。
    - **理由**：例外がなく、機械で判定できる規則だからである。言葉を重ねても、読んで判断するお願いのままで、必ず効く保証にならない。ただし、新しい移行を足す作業は `migrations/` に書く必要がある。その作業のときだけ、ルールの側を外す手順を決めておく。

## 何に効くか {#effects}

範囲を伝えることは、原理の「見せる」と「縛る」に関わり、防ぐ原因は「見えていない」と「合っていない」である。

- **見せる**：境目は Claude の側から見えない。やらないこと・触ってよい範囲・相談の基準を書くのは、見えていないものを見せる手である。原因の「見えていない」を防ぐ。
- **縛る**：例外を許さない範囲は、書いて見せるだけでは足りない。deny ルールやフックは、効く範囲と条件の中で毎回必ず効く。原因の「合っていない」、つまりモデルや effort による「頼まれていないことまでやる」傾向と頼み方のずれが、頼み方を合わせても残る分を、仕組みで受け止める。傾向そのものは観察して記録し、毎回の差分の確認で補う。

症状の側から原因を切り分ける順序は <!-- link:begin does-more-than-asked#diagnosis -->[頼んでいないことまでやる（過剰設計） › 原因を安く確かめる順](../symptoms/does-more-than-asked.md#diagnosis)<!-- link:end --> にある。

## 効かない場面とやりすぎ {#limits}

範囲を書くことには、効かない場面と、やりすぎの形がある。

- **禁止を並べすぎる**：長い禁止の列は、重要な 1 行を埋もれさせる。禁止ごとに理由を添えられないなら、数を絞る。
- **範囲を狭くしすぎる**：原因が範囲の外にあるバグで、範囲を 1 ファイルに限ると、直せないまま止まる。範囲の外に出るときの扱い（止まって相談する）を、範囲と一緒に書く。
- **言葉だけで守らせる**：範囲を書いても、お願いは守られないことがある。差分で範囲の外の変更がないかを確かめる。例外のない範囲は仕組みへ移す。
- **判断を含む規則を鍵にする**：「小さく直す」のような程度の規則は、機械で判定できない。仕組みで縛るのは、例外がなく判定できるものだけにする（<!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](../enforce/when-to-lock.md#what-not-to-lock)<!-- link:end -->）。
- **長いセッションで薄れる**：会話で言った範囲は、圧縮で消えうる。続けて作業するなら、CLAUDE.md か仕組みへ移す。

効いているかは、変更したファイルの一覧を見て確かめる。依頼の範囲より広がった変更が出たら、その範囲を依頼文に足すか、仕組みへ移す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)：Anthropic・英語・確認日 2026-11-04
- [Stop prompting Claude Code - let it interview you](https://velvetshark.com/stop-prompting-claude-code-let-it-interview-you)：VelvetShark・英語・確認日 2026-11-04
- [Think Harder: How I Prompt — Thorsten Ball, Laracon US 2026](https://thorstenball.com/talks/how-i-prompt/)：Thorsten Ball・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [具体性の 4 点（対象・状況・完了・手本）](four-specifics.md)
- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**関連**

- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- 否定形ではなく、望む形で書く（準備中）
- [提案してほしいのか、実行してほしいのか](suggest-or-do.md)
- [理由を添える](give-reasons.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 消せない場所・触れない場所（protected paths）（準備中）
- [お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)
- モデル別の癖と、プロンプトの合わせ方（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
