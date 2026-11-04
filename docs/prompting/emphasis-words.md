---
id: emphasis-words
title: 強調語（IMPORTANT・必ず）の現在
aliases: [IMPORTANT, YOU MUST, CRITICAL, 全大文字で強調する, 「絶対に」と書く]
type: concept
field: prompting
chapter: 頼み方の原則
order: 60
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [縛る]
prevents: [縛っていない, 散らかっている]
scenes: [開発]
summary: 強調語を重ねても指示は守られるようにならず、強い言い方はかえって過剰に当てはめられることがある。守られないなら、指示を短くするか、例外のない規則は仕組みに移す。
signs:
  - {type: symptom, text: IMPORTANT や「必ず」を付けても守られない}
  - {type: symptom, text: 強く書いた指示を、関係のない場面にまで当てはめる}
  - {type: goal, text: 強調に頼らずに、大事な指示を守らせたい}
prerequisites: [request-vs-lock]
related: [instructions-ignored, when-to-lock, say-what-you-want, claude-md-length, give-reasons, request-lock-table, after-switching-models, model-quirks, outdated-advice-ledger]
tracks: [claude-md]
outdated_advice: [important-caps, keep-going-dont-be-lazy]
sources: [cc-docs-best-practices, wb-cc-best-practices-2026-10-26, wb-cc-best-practices-2026-10-27, cc-docs-goal, api-docs-prompting-best-practices, api-docs-prompting-opus-5, hyperdev-tired-toddler-problem, shareuhack-code-setup-guide]
volatility: 中
sections:
  - {title: 強調で直らない二つの理由（長すぎる・例外がない）, anchor: why-not}
  - {title: 強調を外した書き直しの例, anchor: rewrite}
  - {title: 強い言い方が過剰に効く, anchor: overreaction}
  - {title: 「手を抜くな」「続けて」と書く代わりに, anchor: keep-going}
  - {title: かつて強調が効いた理由, anchor: history}
  - {title: 強調をめぐる三つの立場, anchor: stances}
  - {title: 何に効くか, anchor: effects}
  - {title: 効かない場面とやりすぎ, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：強調語を足しても指示が守られるようにならない理由と、守られないときに直すものが分かる。
    - **いつ引くか**：IMPORTANT や「必ず」を付けても守られないとき、強く書いた指示が関係のない場面にまで効くとき。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：IMPORTANT・YOU MUST・CRITICAL・全大文字で強調する・「絶対に」と書く
<!-- textlint-enable -->

強調語とは、IMPORTANT、YOU MUST、CRITICAL、全部が大文字の行、「絶対に」「必ず」のように、指示を強く見せる書き方である。守られない指示へ足したくなる書き方だが、効かないことが多く、効きすぎる害もある。このページは、強調に頼る代わりに何を直すかを順に示す。

## 強調で直らない二つの理由（長すぎる・例外がない） {#why-not}

強調を足しても守られない指示には、2 つの原因がある。公式の Best practices の現行の版は、IMPORTANT を足しても直らないなら、ファイルが長すぎるか、例外のない規則であるかのどちらかだとする。

- **長すぎる**：行が多いと、指示は周りの行に埋もれる。1 行を強く書いても、全体の量は減らない。直すのは強さではなく量で、ファイルを短くする。削る基準は <!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](../extend/claude-md-length.md#deletion-test)<!-- link:end --> にある。
- **例外がない**：例外を許さず、機械で判定できる規則は、言葉で頼む対象ではない。プロンプトや CLAUDE.md は Claude が読んで判断するお願いなので、どれだけ強く書いても「読んだうえで従わない」余地が残る。こうした規則は、フックか deny ルールへ移す。分け方は <!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end -->、移す合図は <!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end --> にある。

自分の指示がどちらかを確かめるには、2 つの問いを使う。

1. 周りの行を減らしたら、守られるようになるか。なるなら、長すぎるのが原因である。
2. 例外が 1 つでもあるか。例外がなく、守ったかどうかを機械で判定できるなら、鍵に移す候補である。

禁止を望む形に書き換える方法と、例外のない禁止を仕組みに移す 2 層の書き方は、<!-- link:begin say-what-you-want#two-layers -->[否定形ではなく、望む形で書く › 例外のない禁止は仕組みへ（二層）](say-what-you-want.md#two-layers)<!-- link:end --> にある。

!!! example "判断例：読まれたくないファイルを守りたい"
    - **状況**：CLAUDE.md に「IMPORTANT: .env は絶対に読むな」と書いたが、作業の途中で読まれた。
    - **迷う候補**：強調をさらに重ねる。CLAUDE.md を短くして埋もれを防ぐ。deny ルールに移す。
    - **選んだもの**：deny ルールに移し、CLAUDE.md には理由と、読む必要が出たときの相談の基準だけを書く。
    - **理由**：この規則は例外がなく、読むか読まないかを機械で判定できる。強調を重ねても、読むかどうかを Claude が判断する点は変わらない。短くする手も筋は通るが、埋もれが原因でなければ直らない。

## 強調を外した書き直しの例 {#rewrite}

強調を外すとは、強さの代わりに、手段・理由・条件を足すことである。同じ依頼で並べる。

**Before**

```text
IMPORTANT: テストは必ず実行すること。YOU MUST run the tests. 絶対に忘れるな。
```

**After**

```text
コードを変えたら、変えた範囲のテストを実行し、失敗が残っていれば報告してほしい。
CI で落ちると直しに戻る手間が大きいので、先に気づきたいからである。
```

After で足したものは 3 つある。

- **確かめる手段**：何を実行するかを、範囲まで書いた。
- **理由**：なぜ必要かを 1 文で書いた。理由があると、書いていない場面にも意図を当てはめられる。詳しくは <!-- link:begin give-reasons#what-changes -->[理由を添える › 理由を添えると何が変わるか](give-reasons.md#what-changes)<!-- link:end --> にある。
- **条件**：「コードを変えたら」と、効かせたい場面を絞った。

強調を外した行は、2 層の書き方の上の層になる。それでも守られなければ、次に疑うのは行の量と、例外のなさである。

自分の設定にある強調の行を一度に洗い出すには、次の依頼を使える。

<!-- gen:begin snippet emphasis-words/audit-emphasis -->
<!-- textlint-disable -->

??? example "雛形：強調で書かれた行を洗い出して分ける"

    ```markdown
    CLAUDE.md と .claude/rules/ の各ファイルから、強調で書かれた行を洗い出して。
    強調とは、IMPORTANT・YOU MUST・NEVER・CRITICAL・全部が大文字の行・「絶対に」「必ず」を指す。

    編集はせず、行ごとに次の 3 つのどれかに分けた表で見せて。

    1. 例外がなく、機械で判定できる規則（deny ルールかフックに移す候補）
    2. 判断を含む規則（強調を外し、理由と条件を添えた書き直しの案も付ける）
    3. 周りの行に埋もれているだけの行（周りの行を減らして残す候補）

    表の列は、ファイルと行・元の文・分類・分類の理由にして。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet emphasis-words/audit-emphasis -->

## 強い言い方が過剰に効く {#overreaction}

強い言い方は、守らせたい場面だけでなく、関係のない場面にも当てはまる。公式のプロンプト指針は、システムプロンプトに強く反応するモデルがあると指摘する。そのうえで、「CRITICAL: You MUST use this tool」のような表現を、「Use this tool when…」という条件つきの言い方へ和らげるよう勧める。現行の Best practices も、強調を重ねると Claude が規則を当てはめすぎる原因になりうるとする。

たとえば、CLAUDE.md に「必ず全テストを実行する」と強く書くと、README の誤字を直すだけの作業でも全テストを回すことがある。書いた側の意図は「コードを変えたとき」だけだったが、強さが条件を押しのけた形である。

直し方は、強さを下げて条件を足すことである。

- 「必ず」「絶対に」を外し、ふつうの言葉にする。
- 効かせたい場面を、「〜のとき」と書く。
- やってほしいことだけでなく、やらなくてよい場面も 1 つ書く。

どのモデルがどの程度強く反応するかは、版で変わる。傾向は <!-- link:begin model-quirks#official-guidance -->[モデル別の癖と、プロンプトの合わせ方 › 公式の指針に出てくる傾向](../models/model-quirks.md#official-guidance)<!-- link:end --> で公式の指針から引き、自分の環境での観察は <!-- link:begin model-quirks#observe-and-record -->[モデル別の癖と、プロンプトの合わせ方 › 自分の環境で観察して記録する](../models/model-quirks.md#observe-and-record)<!-- link:end --> の手順で記録する。

## 「手を抜くな」「続けて」と書く代わりに {#keep-going}

「keep going」「don't be lazy」のような一言も、強調語の仲間である。台帳では <!-- link:begin outdated-advice-ledger#keep-going-dont-be-lazy -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#keep-going-dont-be-lazy)<!-- link:end --> の行が、この助言を撤回として扱う。

以前のモデルは長い作業の途中で止まりやすく、続けるよう促す一言が効いた。公式の Best practices によると、いまのモデルは合意した作業を言われなくても続け、この手の文はかえってやりすぎの原因になりやすい。代わりに次のものを渡す。

- **確かめる手段**：通すべきテストのように、終わったと言える条件を渡す。「最後までやり切れ」と書くより、何をもって終わりとするかが明確になる。
- **止まったとき**：途中で止まったら、`continue` と言って続けさせる。
- **誰も見ていない実行**：`/goal` か Stop フックで続けさせる。`/goal` の公式の説明は、Best practices とは別の文書（Keep Claude working toward a goal）にある。

「続けて」の一言を消しても、終わりの条件は消えない。条件を言葉の強さではなく、確かめられる形で書く。

## かつて強調が効いた理由 {#history}

強調語が定番の助言だったのは、以前のモデルが、強調しないと指示を落とすことがあったからである。改稿前の Best practices も、守られない 1 行にだけ IMPORTANT などの強調を付けるよう勧めていた。同時に、多くの行を強調するとどれも目立たなくなるとも書いていた。

Best practices は 2026-10-27 ごろに大きく書き直され、「What you can stop doing」という表が加わった。この表に「IMPORTANT や全大文字で強調する」の行が入り、強調は、もうやめてよい助言の側になった。公式は、この表の助言の多くを、モデルがまだ確実にできなかったことの回避策だったとする。

強調は、原理でいう「縛る」の回避策だった。言葉で縛るしかなかった頃の手であり、いまは例外のない規則を縛る正式な仕組みがある。回避策が仕組みに置き換わる流れは <!-- link:begin outdated-advice-ledger#workarounds -->[古くなった助言の台帳 › 回避策は正式な仕組みに置き換わる](../changes/outdated-advice-ledger.md#workarounds)<!-- link:end --> に、台帳の読み方は <!-- link:begin outdated-advice-ledger#how-to-read -->[古くなった助言の台帳 › 台帳の読み方（状態と、どの原理の回避策だったか）](../changes/outdated-advice-ledger.md#how-to-read)<!-- link:end --> にまとまっている。この助言の台帳の行は <!-- link:begin outdated-advice-ledger#important-caps -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#important-caps)<!-- link:end --> にある。

自分の設定に古い強調が残っているかは、CLAUDE.md・rules・スキルで、IMPORTANT・YOU MUST・NEVER・全部が大文字の行を探せば分かる。探し方は <!-- link:begin outdated-advice-ledger#find-in-your-setup -->[古くなった助言の台帳 › 自分の設定や記事で見つける](../changes/outdated-advice-ledger.md#find-in-your-setup)<!-- link:end --> にある。

## 強調をめぐる三つの立場 {#stances}

強調の効き目は、実践者の間で見方が割れる。公式の立場、実践者の幅、この辞典の推奨に分けて示す。

- **公式の立場**：現行の Best practices は、IMPORTANT を足しても守られないのは、ファイルが長すぎるか、例外のない規則だからだとする。対処は、ファイルを短くするか、フックにすることである。公式のプロンプト指針も、強すぎる表現を和らげるよう勧める。
- **実践者の幅**：強調だけに頼らず、フックや権限のルールで強制するのが現在の主流だという見方がある（根拠：弱）。CRITICAL と書いても守られなかったという報告もある（根拠：弱。単独の経験談）。一方、かつては強調で守られる率が上がるという助言がよく見られた。
- **この辞典の推奨**：強調せず、ふつうの言葉で理由と条件を添えて書く。それでも守られないなら、ファイルを短くする。例外がなく機械で判定できる規則は、フックか deny ルールに移す。

「強調は 1 行だけにする」は、改稿前の Best practices の勧めである。いまの版の軸は「守られないなら、ファイルを短くするか、フックにする」であり、この辞典もそちらに従う。

## 何に効くか {#effects}

強調語の見直しは、原理の「縛る」と、原因の「縛っていない」「散らかっている」に効く。

- **縛る**：言葉の強さで縛るのをやめ、縛りたい規則は鍵に移す。移す先の選び方は <!-- link:begin when-to-lock#where-to-move -->[お願いを鍵に移す判断 › 移し先の選び方](../enforce/when-to-lock.md#where-to-move)<!-- link:end --> にある。用途ごとの鍵の手段は <!-- link:begin request-lock-table#table -->[お願いと鍵の対応表 › 用途ごとの対応表](../enforce/request-lock-table.md#table)<!-- link:end --> で引ける。
- **縛っていない**：例外のない規則が、お願いの文として置かれているだけの状態を直す。強調を足すのは、お願いの強さを上げるだけで、縛ったことにはならない。
- **散らかっている**：指示が長い、強調だらけで優先がつかない、といった状態を直す。強調を外して短くすると、残した行が読まれやすくなる。

守られない症状の原因を安い順に切り分けるなら、<!-- link:begin instructions-ignored#diagnosis -->[CLAUDE.md や指示が守られない › 原因を安く確かめる順](../symptoms/instructions-ignored.md#diagnosis)<!-- link:end --> から入る。

## 効かない場面とやりすぎ {#limits}

強調を外す見直しにも、効かない場面ややりすぎがある。

- **全部を外す前に測る**：強調の行を一度に全部外すと、効いていた行が混ざっていても見分けられない。外すものは 1 つずつ外し、守られ方を見る。手順は <!-- link:begin after-switching-models#remove-one-at-a-time -->[新しいモデルに替えたら見直すこと › ハーネスの部品を一つずつ外して測る](../models/after-switching-models.md#remove-one-at-a-time)<!-- link:end --> にある。
- **判断を含む規則は鍵にしない**：例外を許さない禁止だけを鍵に移す。「状況を見て決める」規則を鍵にすると、必要な作業まで止まる。境目は <!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](../enforce/when-to-lock.md#what-not-to-lock)<!-- link:end --> にある。
- **面で使える鍵が違う**：アプリ・Claude Code・API で、使える鍵の手段は違う。移す前に <!-- link:begin request-lock-table#by-surface -->[お願いと鍵の対応表 › 面ごとの鍵の手段](../enforce/request-lock-table.md#by-surface)<!-- link:end --> で、自分の面にある手段を確かめる。
- **公式の版が変わる**：この助言は、Best practices の改稿で入れ替わった。次の改稿でまた変わりうるので、本文の判断は台帳の確認日とあわせて読む。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code（改稿前。Internet Archive の写し、2026-10-26 19:44 UTC）](https://web.archive.org/web/20261026194435/https://code.claude.com/docs/en/best-practices)：Anthropic（写し）・英語・確認日 2026-11-04
- [Best practices for Claude Code（改稿後。Internet Archive の写し、2026-10-27 08:15 UTC）](https://web.archive.org/web/20261027081520/https://code.claude.com/docs/en/best-practices)：Anthropic（写し）・英語・確認日 2026-11-04
- [Keep Claude working toward a goal](https://code.claude.com/docs/en/goal)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04
- [The Tired Toddler Problem](https://hyperdev.matsuoka.com/p/the-tired-toddler-problem)：Matsuoka（HyperDev）・英語・確認日 2026-11-04
- [Claude Code Ignores Your CLAUDE.md? It's the Delivery Mechanism, Not a Bug (2026 Fix)](https://www.shareuhack.com/en/posts/claude-code-claude-md-setup-guide-2026)：Shareuhack・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**関連**

- [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [否定形ではなく、望む形で書く](say-what-you-want.md)
- [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- [理由を添える](give-reasons.md)
- [お願いと鍵の対応表](../enforce/request-lock-table.md)
- [新しいモデルに替えたら見直すこと](../models/after-switching-models.md)
- [モデル別の癖と、プロンプトの合わせ方](../models/model-quirks.md)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
