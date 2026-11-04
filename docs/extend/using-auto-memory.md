---
id: using-auto-memory
title: 自動メモリ
aliases: [auto memory, MEMORY.md, /memory, Claude が書き溜める記録]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 70
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [散らかっている, 見えていない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: Claude が自分で書き溜める記録を確かめ、直し、止められる。人が書く CLAUDE.md との分担と、誤った結論が残って後の作業を汚さないための見直し方が分かる。
signs:
  - {type: goal, text: Claude Code が書き溜めた記録の場所を知り、見て直したい}
  - {type: symptom, text: 一度の誤った結論を覚えられ、後の作業でも前提にされる}
prerequisites: [what-to-put-in-claude-md]
related: [how-memory-works, unexpected-memories, experiment-log, over-reliance, claude-md-length, what-survives-compaction, keep-failure-lessons, progress-files, claude-md-loading-order, pruning-extensions]
tracks: [auto-memory]
sources: [cc-docs-memory, cc-docs-context-window]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 最小の使い方, anchor: usage}
  - {title: 誤った記録の見直し, anchor: review}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：Claude が自分で書き溜める記録の場所を知り、`/memory` で見て、直し、止められる。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。記録は文脈として読まれるだけで、中身の正しさを確かめる仕組みも、行動を止める仕組みもない。
    - **いつ引くか**：Claude Code が書き溜めた記録の場所を知って、見て直したいとき。一度の誤った結論を覚えられ、後の作業でも前提にされるとき。
    - **前提**：<!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)<!-- link:end -->

<!-- textlint-disable -->
別名：auto memory・MEMORY.md・/memory・Claude が書き溜める記録
<!-- textlint-enable -->

自動メモリは、Claude Code が作業中に受けた訂正や好みを、Claude 自身がメモとして残し、次のセッションから読む仕組みである。人が書く CLAUDE.md と違い、何を残すかは Claude が決める。アプリ（claude.ai）の Memory とは別の機能で、アプリの側は<!-- link:begin how-memory-works -->[アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)<!-- link:end -->にある。

## 使いどころ {#when}

自動メモリは、Claude が自分で残す 4 種類のメモからなる。公式の文書では、メモの種類を `type` という項目で区別する。

- `user`：使う人の役割や得意分野、作業の好み。
- `feedback`：Claude への訂正と、うまくいったと確認したやり方。
- `project`：コードや git の履歴から分からない、進行中の作業・期限・決定。
- `reference`：課題管理や監視の画面など、プロジェクトの外にある情報の場所。

Claude は、コードから分かること（構成・ファイルの場所・デバッグの直し方）と、CLAUDE.md にすでに書いてあることは残さない。毎回何かを残すわけでもなく、後の会話で役立つかどうかで決める。

このページが防ぐ原因は 2 つある。

- **見えていない。** Claude が何を覚えているかが、人から見えない。記録の場所と見方を知れば解ける。
- **散らかっている。** 古い記録や誤った記録が増え、文脈に混ざる。見直しで解く。

効かせる原理は「見せる」と「確かめる」である。記録を人の目に出し、今のコードと突き合わせて確かめる。人の側の落とし穴は「預けすぎる」で、Claude が書いた記録をそのまま正としてしまうことだ。判断を預けすぎる理由は<!-- link:begin over-reliance#why-we-hand-over -->[判断を預けすぎる（過度依存） › なぜ預けてしまうか](../judgment/over-reliance.md#why-we-hand-over)<!-- link:end -->が持つ。

読み込みの仕組みは、次のとおりである。

- 起動時に読まれるのは `MEMORY.md` の先頭だけで、読み込みの上限は<!-- fact:begin auto-memory-startup-load -->200 行または 25KBの早いほうまで（2026-11-05 時点）<!-- fact:end -->である。超えた分は、起動時には読まれない。
- `MEMORY.md` は索引で、1 件につき 1 行にする。詳しい内容は、話題ごとのファイルに分けて置かれ、Claude が必要なときに読む。
- 記録はマシンの中に置かれ、同じリポジトリの worktree とサブフォルダで共有される。マシンをまたいだり、クラウドの環境と共有されたりはしない。
- 圧縮の後は、ディスクから入れ直される。会話の中だけで伝えた指示とは違い、圧縮では消えない。残るものの全体は<!-- link:begin what-survives-compaction#reloaded -->[圧縮（compaction）で何が残り、何が消えるか › 入れ直されるもの](../basics/what-survives-compaction.md#reloaded)<!-- link:end -->にある。

CLAUDE.md を書く側の方針は<!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)<!-- link:end -->、CLAUDE.md の読み込みの順序は<!-- link:begin claude-md-loading-order -->[CLAUDE.md の階層と読み込み順](claude-md-loading-order.md)<!-- link:end -->に任せる。

## 最小の使い方 {#usage}

自動メモリを見る・直す・止める手順は、Claude Code の中で行う。公式の文書（2026-11-05 に確かめた）に基づく。

=== "Claude Code"

    1. セッションの中で `/memory` を開く。CLAUDE.md の場所の一覧、自動メモリのオンとオフの切り替え、自動メモリのフォルダを開く選択肢が出る。
    2. 自動メモリのフォルダを開く。場所は `~/.claude/projects/<project>/memory/` で、`<project>` は git リポジトリから決まる。中に `MEMORY.md` の索引と、記録ごとのファイルがある。
    3. 中身は平文の markdown で、エディタで読み、直し、消せる。記録のファイルに `modified` の時刻があれば、いつ書かれたかの手がかりになる。
    4. 覚えさせたいことは、頼めば自動メモリに保存される。CLAUDE.md に入れたいときは「CLAUDE.md に足して」と頼むか、`/memory` から自分で編集する。
    5. 止めるには、`/memory` のトグルを使う。ユーザー設定の `autoMemoryEnabled` に保存される。1 つのプロジェクトだけ止めるなら、そのプロジェクトの設定に `autoMemoryEnabled: false` を書く。環境変数なら `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` である。今オンかどうかは、自分の環境で `/memory` のトグルを見て確かめる。

保存先を変えたいときは、設定の `autoMemoryDirectory` で指定できる。バックグラウンドのセッションと、Claude が Bash で起動したセッションでは、トグルでオフにはできても、オンには戻せない。オンに戻すには、ターミナルで直接 `claude` を起動して `/memory` を使う。

セッションの画面に「Saved 2 memories」や「Recalled 2 memories」のような表示が出たら、Claude が記録を書いたことや読んだことを示す。表示が出たら一度、中身を見るとよい。

ほかの OS と IDE 拡張で、保存先や `/memory` の見え方が同じかは未確認である。

## 誤った記録の見直し {#review}

誤った記録の見直しは、Claude が書き溜めた記録を人が読み、誤り・古くなった記録・一度の出来事を一般の決まりにした記録を、直すか消す作業である。

なぜ要るか。自動メモリは、人が承認する前に書かれ、次のセッションの始めから文脈に入る。一度の試行でたまたま出た誤った結論が書かれると、後のセッションはそれを前提にして作業する。実験で誤った結論が自動メモリに書かれ、後続の実験を汚し、手で消すしかなかった、という報告がある（根拠：弱。単独の経験談）。誤りは、Claude が間違えたときだけでなく、正しかった記録が古くなったときにも起きる。

見直しの原則は 2 つだ。Claude が書いた記録を、そのまま正としない。人が見直した記録を、正にする。人が見直した台帳を正にする考え方は<!-- link:begin experiment-log#hypothesis-first -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 仮説を先に書く](../eval/experiment-log.md#hypothesis-first)<!-- link:end -->と同じである。

手順は次のとおり。

1. `/memory` から自動メモリのフォルダを開き、`MEMORY.md` を頭から読む。1 行ずつ、覚えさせた覚えがあるかを見る。覚えのない行は、まず疑う。
2. 下の雛形で、Claude に記録を一覧させ、誤りと古い記録を挙げさせる。記録を書いたのは Claude 自身なので、判定は下書きとして使う。決めるのは、人が今のコードや設定と突き合わせた結果である。
3. 誤りを直すか消す。直すときは、結論だけでなく、誤った結論の元になった原因（環境の不調、手順の誤りなど）まで確かめて書く。同じ場面でまた同じ記録が書かれるなら、記録を消す前に、元の原因を直す。
4. 今後ずっと守らせたいことは、自動メモリに頼らず、人が CLAUDE.md に書く。何を書くかは<!-- link:begin what-to-put-in-claude-md#adding-lines -->[CLAUDE.md に書くこと・書かないこと › 足すときの手順](what-to-put-in-claude-md.md#adding-lines)<!-- link:end -->、CLAUDE.md が長くなったときの整え方は<!-- link:begin claude-md-length -->[CLAUDE.md の長さと剪定](claude-md-length.md)<!-- link:end -->にある。
5. 新しいセッションを開き、覚えていることを Claude に尋ねる。消したはずの内容が出ないこと、直した内容に変わっていることを見る。

<!-- gen:begin snippet using-auto-memory/review-prompt -->
<!-- textlint-disable -->

??? example "雛形：自動メモリの記録を一覧させ、誤りと古い記録を挙げさせるプロンプト"

    ```markdown
    このリポジトリの自動メモリに溜まった記録を見直したい。まだ何も書き換えず、先に一覧と判定だけを出してほしい。

    手順は次のとおり。

    1. 自動メモリのフォルダにある `MEMORY.md` と、そこから指されている話題ごとのファイルをすべて読む。
    2. 記録を 1 件ずつ、表にする。列は「ファイル名」「記録の要旨（1 行）」「種類（user・feedback・project・reference）」「書かれた時期（`modified` があればそれ）」「根拠」「判定」「理由」。
    3. 「根拠」には、その記録が正しいと言える材料を書く。今のリポジトリのコード・設定・ドキュメントを実際に読んで確かめたことだけを書き、記憶や推測で埋めない。確かめられなかった記録は「確かめられない」と書く。
    4. 「判定」は次の 4 つに分ける。
       - 残す：今のリポジトリと合っていて、後の作業に役立つ
       - 直す：方向は合っているが、古い・言い過ぎ・原因が違う
       - 消す：今のリポジトリと合わない、またはコードを読めば分かる
       - 判断できない：私に聞かないと分からない
    5. 次の記録は、別の表にして必ず挙げる。
       - 一度の失敗や一度の観察から、一般の決まりのように書かれた記録
       - 実験や計測の結論として書かれ、後の作業の前提になりうる記録
       - ほかの記録や CLAUDE.md と食い違う記録

    私が表を見て承認するまで、記録のファイルを書き換えたり消したりしないこと。自分が書いた記録であっても、正しいものとして扱わないこと。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.59。

<!-- textlint-enable -->
<!-- gen:end snippet using-auto-memory/review-prompt -->

試すときは、先に自動メモリのフォルダをほかの場所に写しておく。表の判定は Claude の推測を含むので、「消す」の行は自分の目でも確かめる。

見直す時期に決まりはない。実験や計測の途中で結論が出た後、大きな調べものが済んだ後、モデルを替えた後は、見直す機会になる。結論が後の作業の前提になる仕事ほど、細かく見る。Claude に覚えるのを任せる幅を広げるほど（長く使う・無人で回すなど）、見直しの時期を先に決めておく。実験の結果を扱うなら、記録の仕方は<!-- link:begin experiment-log -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)<!-- link:end -->が持つ。

!!! example "判断例：一度の失敗から書かれた「並列実行は遅い」の記録"
    - **状況**：ベンチマークを並列で流したら遅かった。数日後に見ると、自動メモリに「このベンチは並列実行すると遅いので、並列にしない」と書かれていた。当時はネットワークが一時的に不調だった。
    - **迷う候補**：記録を消す。記録を正しい原因に直す。この記録に限らず、プロジェクトの自動メモリをオフにする。
    - **選んだもの**：記録を、確かめた原因（そのときのネットワークの不調）に直す。ベンチの流し方で守らせたい決まりがあるなら、人が CLAUDE.md に書く。
    - **理由**：消すだけでは、次に遅くなったときに同じ記録が書かれる。オフにすると、ほかの有用な記録まで失う。記録を原因まで確かめて直すほうが、後の作業を汚す前提を取り除ける。

## 効かない場面と落とし穴 {#limits}

- **お願いであって、鍵ではない。** 自動メモリも CLAUDE.md も、文脈として読まれるだけで、厳密に守られる保証はない。例外を許さない禁止は、記録ではなく、deny ルールやフックで止める。
- **記録を確かめずに正とする。** 落とし穴は「預けすぎる」ことだ。「Saved memories」の表示があっても中身を読まずに使い続けると、誤った記録が前提として積み上がる。判断を手元に残す考え方は<!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](../judgment/over-reliance.md#what-to-keep)<!-- link:end -->にある。
- **索引が長すぎて後ろが読まれない。** `MEMORY.md` が上限を超えると、超えた分は次の起動で読まれない。上限を超えたまま放っておくと、索引の後ろにある記録を Claude は知らない状態で始まる。
- **チームでは共有されない。** 記録はそのマシンの中にあり、ほかの人やほかのマシンには届かない。全員に効かせたい規則は、リポジトリの CLAUDE.md に書く。
- **サブエージェントには渡らない。** メインの会話の自動メモリは、サブエージェントへ読み込まれない（会話を複製する fork は例外）。引き継がれないものの全体は<!-- link:begin what-subagents-dont-inherit -->[サブエージェントに引き継がれないもの](what-subagents-dont-inherit.md)<!-- link:end -->にある。
- **消さない限り残る。** 自動メモリの記録は、期間が過ぎても自動では消えず、人か Claude が直すか消すまで残る。古くなった記録は、見直さない限り前提として読まれ続ける。
- **環境によって既定が違う。** クラウドや自己ホストの環境は、自動メモリの既定の状態が違うことがある。使う環境ごとに、公式の文書と `/memory` のトグルで確かめる。
- **別の会話の内容が混ざって見えるとき。** 原因が自動メモリとは限らない。アプリと Claude Code の記憶のどちらかを切り分けるには、<!-- link:begin unexpected-memories#diagnosis -->[別の会話やプロジェクトの内容が混ざる › 原因を安く確かめる順](../symptoms/unexpected-memories.md#diagnosis)<!-- link:end -->を使う。

## 比べる相手 {#compare}

自動メモリと CLAUDE.md は、補い合う別々の仕組みである。どちらも、毎回のセッションの始めに読まれ、文脈として扱われる。

| 比べるもの | CLAUDE.md | 自動メモリ |
| --- | --- | --- |
| 書く人 | 人 | Claude |
| 中身 | 指示と規則 | 学んだことと癖 |
| 範囲 | プロジェクト・ユーザー・組織 | リポジトリごと（worktree で共有） |
| 見直す人 | チームで、PR などで合意する | 記録のフォルダを開いた人 |

- 人が決めたことと、Claude が学んだことの分け方は、進捗ファイルの考え方と近い。<!-- link:begin progress-files#decided-vs-open -->[進捗ファイルで、途中から再開できるようにする › 決めたことと、聞くべきことを分ける](../context/progress-files.md#decided-vs-open)<!-- link:end -->を見る。
- 失敗の教訓を、会話を捨てた後も残す方法は<!-- link:begin keep-failure-lessons#both -->[失敗の教訓は捨てずに書き残す › 巻き戻しと記録の両立](../context/keep-failure-lessons.md#both)<!-- link:end -->が持つ。
- 拡張全体の棚卸しは<!-- link:begin pruning-extensions -->[拡張の棚卸しと剪定](pruning-extensions.md)<!-- link:end -->が持つ。
- アプリのメモリは別の機能で、見る・直す・消す・止める手段が違う。<!-- link:begin how-memory-works#manage -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 覚えた内容を見る・直す（棚卸し）](../app/how-memory-works.md#manage)<!-- link:end -->を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)

**関連**

- [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- [CLAUDE.md の長さと剪定](claude-md-length.md)
- [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- [失敗の教訓は捨てずに書き残す](../context/keep-failure-lessons.md)
- [進捗ファイルで、途中から再開できるようにする](../context/progress-files.md)
- [CLAUDE.md の階層と読み込み順](claude-md-loading-order.md)
- [拡張の棚卸しと剪定](pruning-extensions.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
