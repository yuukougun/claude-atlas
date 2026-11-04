---
id: thinking-keywords
title: 「考えて」と書くことの現在（ultrathink）
aliases: [think hard, 熟考, よく考えて, 考えさせるキーワード]
type: feature
field: models
chapter: effort・思考・コンテキスト
order: 50
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: []
prevents: [合っていない]
pitfalls: []
summary: 「よく考えて」「think hard」と書いても effort は上がらず、普通の文として渡ることが分かる。深く考えさせたいときは effort を上げ、その依頼だけ深く考えさせる手段もある。
signs:
  - {type: goal, text: 「think hard」や「よく考えて」が効くのか知りたい}
  - {type: situation, text: 古い記事の「段階的に深く考えさせるキーワード」が今も効くか分からない}
  - {type: goal, text: この質問だけ、深く考えさせたい}
prerequisites: [effort-levels]
related: [how-thinking-works, emphasis-words, unfaithful-reasoning, outdated-advice-ledger]
tracks: [ultrathink, effort]
outdated_advice: [think-hard-keywords]
sources: [cc-docs-model-config, cc-changelog, cc-docs-best-practices, hc-effort-settings]
volatility: 高
sections:
  - {title: 普通の文として渡る言い回し, anchor: plain-text-phrases}
  - {title: ultrathink の使いどころ, anchor: ultrathink}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: なぜ変わったか（キーワードしかなかった時代の回避策）, anchor: history}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：「よく考えて」「think hard」と書いても effort は上がらず、普通の文として渡ることが分かる。深く考えさせたいときは effort を上げるか、その依頼だけ ultrathink を付ける。
    - **いつ引くか**：「think hard」や「よく考えて」が効くのか知りたいとき。古い記事の「段階的に深く考えさせるキーワード」が今も効くか分からないとき。この質問だけ、深く考えさせたいとき。
    - **成熟度**：<!-- gen:begin feature maturity -->GA<!-- gen:end feature maturity -->（ultrathink）。
    - **強制力**：<!-- gen:begin feature ultrathink/enforcement -->お願い<!-- gen:end feature ultrathink/enforcement -->（ultrathink）。何も止めない。深く考えるよう頼む言葉であり、禁止や上限の仕組みではない。
    - **前提**：<!-- link:begin effort-levels -->[effort の段階と使い分け](effort-levels.md)<!-- link:end -->

<!-- textlint-disable -->
別名：think hard・熟考・よく考えて・考えさせるキーワード
<!-- textlint-enable -->

「考えて」と書くことの現在（ultrathink）は、考えさせる言葉が今どう扱われるかを整理する項目である。深さを決める主な手段は effort で、言葉で頼むときに名前を持つのは ultrathink だけだ。防ぐ原因は、頼み方の選び方が依頼の重さと合っていないことである。

## 普通の文として渡る言い回し {#plain-text-phrases}

「think」「think hard」「think more」「think harder」「熟考」「よく考えて」と書いても、effort を上げるキーワードとしては働かない。これらは普通の文としてモデルに渡り、effort の範囲の中で軽く後押しするだけである。公式の文書（2026-11-04 に Model configuration と Best practices で確認）がそう書いている。

「ただの文字列で何も起きない」わけでも、「認識されない」と言い切れるわけでもない。文として読まれるので、考えてほしい中身を書けば、その中身は読まれる。ただし、書いた言葉で考える深さは決まらない。

| 書いた言葉 | 渡り方 | 深く考えさせたいとき |
| --- | --- | --- |
| think・think hard・think more・think harder・熟考・よく考えて | 普通の文として渡る | effort を上げる |
| ultrathink | そのターンだけ深く考えるよう頼む言葉として認識される | effort を上げるか、その依頼だけなら ultrathink（次の「ultrathink の使いどころ」の節） |

強い言い方を重ねても、効きが強まるとは限らない。かえって過剰に当てはめられることがある。その話は <!-- link:begin emphasis-words#overreaction -->[強調語（IMPORTANT・必ず）の現在 › 強い言い方が過剰に効く](../prompting/emphasis-words.md#overreaction)<!-- link:end --> にまとめてある。深さを変えたいときの設定は <!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](effort-levels.md#how-to-set)<!-- link:end --> を引く。

## ultrathink の使いどころ {#ultrathink}

ultrathink は、プロンプトに書くと、その 1 ターンだけ深く考えるよう頼む言葉として認識される。セッションの effort は変えない。使いどころは、ふだんは既定の effort で足りるが、この 1 回の依頼だけ慎重に考えさせたい場面である。effort を全体で上げると、以降のすべてのターンの待ち時間と使用量が増える。

Claude Code の対話の端末では、条件がそろうと、そのターンの effort を引き上げて動かす場合がある。引き上がるときは、入力欄の ultrathink が虹色で表示される。引き上がる段と、対応するモデル・面は、<!-- fact:begin ultrathink-raise-target-and-models -->未確認<!-- fact:end -->である。対応する版は、対話のターミナルが <!-- fact:begin ultrathink-raise-min-version-terminal -->Claude Code 2.1.311 以降（2026-11-04 時点）<!-- fact:end -->、VS Code が <!-- fact:begin ultrathink-raise-min-version-vscode -->未確認<!-- fact:end --> である。次の場合は、引き上がらない。


- `CLAUDE_CODE_EFFORT_LEVEL` で、引き上げる先より低い段に固定しているとき。
- 組織の上限が設定されているとき。
- Bedrock など、Anthropic の API 以外で動かしているとき。

`CLAUDE_CODE_DISABLE_ULTRATHINK` を設定すると、この動きを止められる（使える版：<!-- fact:begin ultrathink-disable-env-min-version -->未確認<!-- fact:end -->）。引き上がらない場合でも、ultrathink の語は頼みとして文脈に渡る。

=== "アプリ"

    アプリでの ultrathink の扱いは未確認である。その依頼を深く考えさせたいときは、送信ボタンの横のモデルのメニューで effort を選ぶ。選び方の詳細は <!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](effort-levels.md#how-to-set)<!-- link:end --> にある。

=== "Claude Code"

    依頼に ultrathink と書く。次の依頼からは、書かなければ元の段に戻る。段そのものを変えるときは `/effort` か `--effort` を使う。

<!-- gen:begin snippet thinking-keywords/ultrathink-one-turn -->
<!-- textlint-disable -->

??? example "雛形：この 1 回の依頼だけ深く考えさせる例"

    ```markdown
    ultrathink
    認証のセッション管理について、Cookie のまま CSRF 対策を足す案と、トークン方式に移す案を比べてほしい。
    各案で壊れやすい点と、移行で影響が出る既存のコードを挙げる。
    最後に、推奨する案とその理由を 3 行で書く。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 0.2.44。

<!-- textlint-enable -->
<!-- gen:end snippet thinking-keywords/ultrathink-one-turn -->

!!! example "判断例：設計の選択を 1 回だけ慎重に考えさせたい"
    - **状況**：ふだんは既定の effort で実装を進めている。今日は認証の方式を決める依頼が 1 回だけあり、ここだけは見落としを減らしたい。
    - **迷う候補**：セッション全体の effort を上げる。依頼に ultrathink を付ける。「慎重に考えて」と普通の文で書く。
    - **選んだもの**：その依頼に ultrathink を付け、比べる観点も文で書く。
    - **理由**：ultrathink は、その 1 ターンだけを対象にする。全体の effort を上げると、残りの軽い作業も遅く、使用量が多くなる。「慎重に」は effort を上げないので、深さを変える手段にはならない。比べる観点は普通の文として読まれるので、そこは書いて渡す。

## 効かない場面・落とし穴 {#pitfalls}

ultrathink を付けても、深さが上がったと確かめられない場面がある。表示が虹色にならないときは、頼みの文としては渡っていても、effort は上がっていない可能性がある。そのときは、設定と環境を見る。引き上がらない条件は 3 つある。`CLAUDE_CODE_EFFORT_LEVEL` で低い段に固定している。組織の上限がある。Bedrock など Anthropic の API 以外で動かしている。

毎回の依頼の頭に付けるのは、勧めない。常用すると、effort を上げたのと同じ重さになり、待ち時間と使用量が増える。その増え方は <!-- link:begin effort-levels#levels -->[effort の段階と使い分け › 段ごとの振る舞い](effort-levels.md#levels)<!-- link:end --> にある。

深く考えさせても、答えが正しくなる保証はない。画面に出る思考や「こう計算した」という説明は、実際の内部の処理とずれることがある。結果は独立に確かめる。理由は <!-- link:begin unfaithful-reasoning -->[表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)<!-- link:end --> にある。考える仕組みと、何に効くかは <!-- link:begin how-thinking-works#effects -->[思考（thinking）と effort の仕組み › 何に効くか](../basics/how-thinking-works.md#effects)<!-- link:end --> にある。

古い記事の「think → think hard → ultrathink」と段が上がる書き方をそのまま写しても、段は上がらない。think hard などは普通の文として読まれるだけなので、深さを変えたいなら effort を使う。

## 比べる相手 {#compare}

考えさせる深さを決める手段には、全体の既定を変える effort と、その依頼だけの ultrathink がある。対象と成熟度の違いは次の表で見る。

<!-- gen:begin compare 面 成熟度 入った版 -->
<!-- textlint-disable -->

| 機能 | 面 | 入った版 |
| --- | --- | --- |
| [ultrathink](thinking-keywords.md) | Claude Code | 0.2.44 |
| [effort](effort-levels.md) | アプリ・Claude Code・API | 2025-11-24 |

すべて共通：成熟度 GA。

<!-- textlint-enable -->
<!-- gen:end compare 面 成熟度 入った版 -->

使い分けは、対象の広さで決める。今後の依頼すべてを深くしたいなら effort を替える。この依頼だけなら ultrathink を使う。think hard のような普通の文は、どちらの代わりにもならない。

## なぜ変わったか（キーワードしかなかった時代の回避策） {#history}

かつては、考える量を言葉で頼むのが公式のやり方だった。effort の段を選ぶ手段がまだなかったからである。古い版の CHANGELOG には、think・think harder・ultrathink で考える量を頼めると書かれている。その後、英語以外の言語でも思考を起動できるようになった。日本語の「熟考」のような語は、この流れで段階を表す語として使われた。ただし、どの語がどの段に当たったかは、一次資料で確かめていない。

effort で段を選べるようになると、段階のキーワードは外れた。外れた時期は、一次資料に版の記述がなく、確かめられていない。上の表の版は、ultrathink が最初に入った版である。ultrathink は後に外れ、次のターンの effort を上げる言葉として戻り、いまの動きに至っている（戻った版は <!-- link:begin outdated-advice-ledger#think-hard-keywords -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#think-hard-keywords)<!-- link:end --> にある）。特定の月に廃止されたという記述も見かけるが、CHANGELOG では確かめられなかった。

この移り変わりは、台帳にある「言葉で回避していた弱点が、正式な仕組みに置き換わる」規則の例である。規則は <!-- link:begin outdated-advice-ledger#workarounds -->[古くなった助言の台帳 › 回避策は正式な仕組みに置き換わる](../changes/outdated-advice-ledger.md#workarounds)<!-- link:end --> で読める。このページの助言の行は <!-- link:begin outdated-advice-ledger#think-hard-keywords -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#think-hard-keywords)<!-- link:end --> にある。今どうするかを一言で言うと、考える深さは effort で決め、その依頼だけなら ultrathink を使う。

自分の設定や保存した頼み方に古い書き方が残っていないか探すには、次のコマンドが使える。読むだけで、何も書き換えない。

<!-- gen:begin snippet thinking-keywords/find-old-keywords -->
<!-- textlint-disable -->

??? example "雛形：古いキーワードの書き残しを探すコマンド"

    ```bash
    #!/bin/sh
    # CLAUDE.md・スキル・保存した頼み方から、段階のキーワードの書き残しを探す。読むだけで、何も書き換えない
    grep -rnIE "think (hard|harder|more)|ultrathink|熟考|よく考えて" \
      CLAUDE.md "$HOME/.claude/CLAUDE.md" .claude/ 2>/dev/null
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 0.2.44。

<!-- textlint-enable -->
<!-- gen:end snippet thinking-keywords/find-old-keywords -->

古いモデル向けに書いた指示を洗い出すには、`/doctor prompt-audit` も使える。対応する版は CHANGELOG で確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [effort の段階と使い分け](effort-levels.md)

**関連**

- [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- [強調語（IMPORTANT・必ず）の現在](../prompting/emphasis-words.md)
- [表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
