---
id: old-advice-doesnt-work
title: 記事や前のやり方が通じない
aliases: [古い記事が通じない, 前は効いたのに効かなくなった, 古い Tips, 記事の手順が動かない]
type: symptom
field: symptoms
chapter: 事実と出典
order: 100
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる]
prevents: [確かめていない, 合っていない]
pitfalls: []
scenes: [開発, 文章, 調べもの]
summary: 記事や本、前に覚えたやり方が通じないときに、その情報の日付と版を確かめ、撤回された助言か名前が変わっただけかを切り分けて、今のやり方に置き換えられる。
signs:
  - {type: symptom, text: 古い記事のやり方が通じない}
  - {type: symptom, text: 前は効いた書き方や設定が効かなくなった}
  - {type: symptom, text: 記事に出てくるコマンドや機能の名前が、手元に見当たらない}
  - {type: symptom, text: 記事によって書いてあることが食い違う}
wave: 1
prerequisites: []
related: [ask-claude-code#check-version, change-timeline-2026, writing-skills#from-commands, writing-subagents#define, thinking-keywords, emphasis-words, doesnt-know-latest, seems-less-capable, six-causes]
routes:
  - {cause: 確かめていない, to: [dating-information#check-date-and-version, checking-for-updates, outdated-advice-ledger#find-in-your-setup]}
  - {cause: 合っていない, to: [outdated-advice-ledger, term-index#old-names, command-cheatsheet]}
tracks: []
outdated_advice: [fork-to-branch, removed-commands, commands-directory, agents-command, routines-name, code-on-the-web-remote]
sources: [cc-docs-best-practices, cc-changelog, cc-docs-changelog, cc-docs-commands]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 記事の手順を Claude に突き合わせさせる, anchor: ask-claude}
  - {title: 判断例, anchor: example}
  - {title: 予防：古い書き方を残さない仕組み, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：記事や前のやり方が通じないとき、日付と版を確かめ、撤回か名前の変更かを切り分けて今のやり方に置き換えられる。
    - **いつ引くか**：古い記事の手順が動かない。前は効いた書き方が効かない。記事の機能名が手元にない。記事同士が食い違う。
    - **前提**：なし

<!-- textlint-disable -->
別名：古い記事が通じない・前は効いたのに効かなくなった・古い Tips・記事の手順が動かない
<!-- textlint-enable -->

記事や本、前に覚えたやり方が通じないのは、たいてい Claude の不調ではなく、情報の日付と手元の版がずれているときである。このページは、そのずれを安く確かめる順に並べ、撤回された助言か、名前が変わっただけかを切り分ける。

## よくある形 {#forms}

通じなくなり方は、大きく 4 つに分かれる。どれに当たるかで、次に見る場所が変わる。

- **名前が見当たらない**：記事のコマンドや機能の名前が、手元の画面や一覧に出てこない。名前が変わったか、消えたかのどちらかである。
- **打てるが、記事と違う動きをする**：名前は残っているのに、画面や結果が記事と違う。動きが変わったか、同じ名前が別の機能を指すようになった。
- **動くが、今は勧められない**：記事の書き方は今も動く。ただし、新しいやり方が別にできている。
- **記事同士が食い違う**：同じ機能の説明が、記事によって逆になる。書かれた時期か、指している面が違う。

頼み方の助言も同じ形で古くなる。「よく考えて」と書く、強調語を重ねるといった勧めは、書かれた時点の制御手段の不足を補う回避策だった。

## 原因を安く確かめる順 {#diagnosis}

安く確かめられるものから順に並べる。上の項目で原因が決まったら、下は読まなくてよい。

1. **記事の日付と版を見る（確かめていない）**。記事の公開日、更新日、記事が前提にしている版を探す。どれも書かれていなければ、通じない原因が古さかどうかを、この時点では決められない。日付と版の見分け方は <!-- link:begin dating-information#check-date-and-version -->いつの情報かを見分ける › 日付と版の確かめ方（準備中）<!-- link:end --> にある。
2. **手元の版と、記事の版を並べる（確かめていない）**。手元の版が記事の版より新しければ、変更が入っている可能性が高い。版や変更履歴の確かめ方は <!-- link:begin checking-for-updates -->最新を自分で確かめる方法（準備中）<!-- link:end --> にある。同じ版で通じないなら、古さではなく別の原因を疑う。
3. **公式の文書と変更履歴で、その名前を引く（合っていない）**。記事に出る機能やコマンドの名前を、公式の文書と変更履歴で検索する。出てくる結果は 3 通りである。結果は、古くなった助言を状態と今のやり方つきで並べた「台帳」（下の節でリンクする）の状態の名前でも呼ばれる。
    - **名前が変わっただけ**：中身は同じで、呼び方だけ変わっている。台帳では「置換」と書かれる。
    - **撤回された**：機能や画面が消えた。台帳では「撤回」と書かれ、代わりのやり方が添えられる。
    - **今も動くが条件が変わった**：台帳では「条件付き」と書かれる。
4. **同じ名前で、別の機能になっていないかを見る（合っていない）**。名前は残っていても、指す先の機能は変わりうる。記事の用語を、台帳の「今どうするか」と照らして読み替える。
5. **面が違っていないかを見る（合っていない）**。同じ名前でも、アプリ・Claude Code・API で別の機能を指すことがある。記事が、どの面の話かを確かめる。
6. **記事同士の食い違いは、日付の新しいほうと公式の文書に合わせる**。日付が近いなら、違いは面か版にあることが多い。

### 名前が変わっただけのとき

名前の変更は、読み替えれば手順がそのまま使える。台帳で扱う例を 3 つ挙げる。

- 記事の routines は、<!-- name:begin routines-to-scheduled-tasks -->クラウドの予定のタスク（cloud scheduled tasks）<!-- name:end --> のことである。手元で動く予定のタスクとは別の機能なので、どちらを指すかも確かめる。
- 記事の Claude Code on the web は、<!-- name:begin web-to-cloud-sessions -->クラウドセッション（cloud sessions）<!-- name:end --> のことである。端末から始めるときのフラグも、記事の `--remote` は `--cloud` に替える。`--remote-control` は別の機能なので替えない。
- 会話を分岐させる意味の `/fork` は、<!-- name:begin fork-renamed-branch -->/branch（今の /fork は、会話を新しい背景のセッションに写す別の機能）<!-- name:end --> に読み替える。

### 撤回や置き換えのとき

消えたコマンド、作成の画面がなくなった `/agents`、`.claude/commands/` からスキルへの移行といった例は、台帳に今どうするかが並んでいる。台帳の入口は <!-- link:begin outdated-advice-ledger -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md)<!-- link:end --> である。

- 自分の設定や記事に残る古い書き方を探すとき：<!-- link:begin outdated-advice-ledger#find-in-your-setup -->[古くなった助言の台帳 › 自分の設定や記事で見つける](../changes/outdated-advice-ledger.md#find-in-your-setup)<!-- link:end -->。
- サブエージェントの作り方：<!-- link:begin writing-subagents#define -->サブエージェントの作り方と使いどころ › 定義の書き方（ファイルを書くか、Claude に作らせる）（準備中）<!-- link:end -->。
- カスタムコマンドからスキルへの移り方：<!-- link:begin writing-skills#from-commands -->[スキルの作り方 › カスタムコマンドから移る](../extend/writing-skills.md#from-commands)<!-- link:end -->。

「よく考えて」や強調語のような頼み方の勧めは、台帳から <!-- link:begin thinking-keywords -->「考えて」と書くことの現在（ultrathink）（準備中）<!-- link:end --> と <!-- link:begin emphasis-words -->強調語（IMPORTANT・必ず）の現在（準備中）<!-- link:end --> へ進む。

### 人の側の落とし穴

記事の手順を写した設定が、自分の環境に昔のまま残っていることも多い。手元の設定のほうが古いままだと、記事の手順を今の版に読み替えても動かない。人の側の落とし穴の見方は <!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end --> にある。

通じない原因が、記事ではなく Claude の知識の古さにあるなら <!-- link:begin doesnt-know-latest -->[最新の情報を知らない](doesnt-know-latest.md)<!-- link:end --> へ、前は効いたという手応えが体感だけなら <!-- link:begin seems-less-capable -->[急に賢くなくなった気がする](seems-less-capable.md)<!-- link:end --> へ進む。

### 原因ごとの対処

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 確かめていない | いつの情報かを見分ける › 日付と版の確かめ方（準備中）<br>最新を自分で確かめる方法（準備中）<br>[古くなった助言の台帳 › 自分の設定や記事で見つける](../changes/outdated-advice-ledger.md#find-in-your-setup) |
| 合っていない | [古くなった助言の台帳](../changes/outdated-advice-ledger.md)<br>[用語索引と旧名の対応 › 旧名から引く](../start/term-index.md#old-names)<br>主要コマンド早見表（準備中） |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 記事の手順を Claude に突き合わせさせる {#ask-claude}

記事の手順に出てくる名前を、Claude に公式の資料と突き合わせさせると、手で引くより早い。ただし、Claude 自身の知識は古いことがあるので、見た資料の URL を必ず付けさせる。次の依頼は、結果を 4 つの区分に分け、確かめられなかったものを推測で埋めさせない。

<!-- gen:begin snippet old-advice-doesnt-work/check-article -->
<!-- textlint-disable -->

??? example "雛形：記事の手順を、今の公式の資料と突き合わせさせる依頼"

    ```markdown
    次の記事の手順（または自分の古いメモ）が、今も通じるかを確かめたい。

    - 記事の日付と、記事が前提にしている版：<日付と版。書かれていなければ「書かれていない」>
    - 手元の版と使っている面：<手元の版。アプリ・Claude Code・API のどれか>
    - 確かめたい手順：<記事から該当部分を貼る>

    やってほしいこと：手順に出てくるコマンド・機能・設定の名前を 1 つずつ挙げ、公式の文書と変更履歴で、今も同じ名前・同じ意味かを調べる。結果は次の 4 つに分け、見た資料の URL を付ける。

    1. そのまま通じる
    2. 名前が変わっただけ（今の名前を書く）
    3. 撤回された（代わりのやり方を書く）
    4. 確かめられなかった（理由を書く）

    確かめられなかったものは、推測で埋めず、そのまま 4 に入れる。まだ設定は変えない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet old-advice-doesnt-work/check-article -->

Claude Code に自分の使い方を聞く場合も、答えが手元の版より新しい機能を含みうる。使う前に版を確かめる方法は <!-- link:begin ask-claude-code#check-version -->Claude Code 自身に聞く › 答えの版を確かめる（準備中）<!-- link:end --> にある。

## 判断例 {#example}

!!! example "判断例：記事の `/agents` の画面が開かない"
    - **状況**：サブエージェントの作り方を書いた記事の手順どおりに `/agents` を打った。作成の画面が開かず、案内の文だけが出た。
    - **迷う候補**：記事に合わせて手元の版を下げる。または、記事のほうが古いと見て、今のやり方に読み替える。
    - **選んだもの**：記事の日付と版を確かめ、台帳で `/agents` の行を引いた。作成の画面は撤回されていたので、読み替える側を選んだ。
    - **理由**：版を下げると、ほかの機能も記事の時点に戻り、別の記事の手順が通じなくなる。台帳には今のやり方が載っており、Claude にサブエージェントを作らせるか、定義のファイルを直接書けばよい。

<!-- link:begin outdated-advice-ledger -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md)<!-- link:end --> の行は、この判断の根拠になる。

## 予防：古い書き方を残さない仕組み {#prevention}

通じなくなってから探すより、古くなっても気づける置き方にしておくほうが安い。

- 記事から写した設定や手順には、写した日と、記事の日付・版・URL を 1 行で残す。次に通じなくなったとき、記事の日付と版を探す手間と、手元の版と並べる手間が省ける。
- 手順書やスキルに書いたコマンドや機能の名前は、変更履歴を確かめるたびに台帳で引き直す。引き直しの入口は <!-- link:begin outdated-advice-ledger#find-in-your-setup -->[古くなった助言の台帳 › 自分の設定や記事で見つける](../changes/outdated-advice-ledger.md#find-in-your-setup)<!-- link:end --> である。
- 台帳は、回避策が正式な仕組みに置き換わる規則から、次に古くなりそうなものの見当も付ける。2026 年に何が変わったかの流れは <!-- link:begin change-timeline-2026 -->2026 年の主な変更の年表（準備中）<!-- link:end --> で見られる。
- 記事を読むときは、まず日付と版を見る。方向性を学び、個別の手順は書かれた時点のものと考える。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- いつの情報かを見分ける（準備中）
- 最新を自分で確かめる方法（準備中）
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- [用語索引と旧名の対応](../start/term-index.md)
- 主要コマンド早見表（準備中）

**関連**

- Claude Code 自身に聞く › 答えの版を確かめる（準備中）
- 2026 年の主な変更の年表（準備中）
- [スキルの作り方 › カスタムコマンドから移る](../extend/writing-skills.md#from-commands)
- サブエージェントの作り方と使いどころ › 定義の書き方（ファイルを書くか、Claude に作らせる）（準備中）
- 「考えて」と書くことの現在（ultrathink）（準備中）
- 強調語（IMPORTANT・必ず）の現在（準備中）
- [最新の情報を知らない](doesnt-know-latest.md)
- [急に賢くなくなった気がする](seems-less-capable.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
