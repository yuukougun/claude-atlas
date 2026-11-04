---
id: must-know-operations
title: 知らないと損をする操作
aliases: [知らないと損をする操作20, キーボードショートカット, Shift+Tab, 外部エディタで書く, 画像を貼り付ける, トランスクリプトを見る]
type: feature
field: cli
chapter: 入力と基本の操作
order: 20
level: 整える
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: 権限モードの切り替え、長い指示を外部エディタで書く、画像を貼る、作業の様子を見る、実行中の処理を背景に回すなど、知っていると手戻りが減る操作を場面ごとに引ける。
signs:
  - {type: goal, text: Claude Code の操作をもっと速くしたい}
  - {type: situation, text: スクリーンショットや長い指示を渡したい}
prerequisites: [input-symbols]
related: [command-cheatsheet, permission-modes-overview, checkpoints-and-rewind, resume-and-branch, side-questions-btw, images-and-voice, agent-view-and-background, windows-wsl-ime]
tracks: [interactive-mode, permission-modes]
outdated_advice: [removed-commands]
sources: [cc-docs-interactive-mode, cc-docs-commands, cc-docs-permission-modes]
volatility: 高
sections:
  - {title: 場面から引く, anchor: when}
  - {title: モードを切り替える, anchor: modes}
  - {title: 長い指示と画像を渡す, anchor: input}
  - {title: 様子を見る・背景に回す, anchor: watch-and-background}
  - {title: 端末と WSL での違い, anchor: terminals}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：権限モードの切り替え・外部エディタでの入力・画像の貼り付け・作業の確認・背景化を、場面から引ける。
    - **いつ引くか**：Claude Code の操作をもっと速くしたいとき、スクリーンショットや長い指示を渡したいとき。
    - **強制力**：キー操作は「<!-- gen:begin feature interactive-mode/enforcement -->なし<!-- gen:end feature interactive-mode/enforcement -->」である。入力と表示の近道にすぎない。
    - **切り替え先のモード**：権限モードは「<!-- gen:begin feature permission-modes/enforcement -->鍵<!-- gen:end feature permission-modes/enforcement -->」である。確認なしで進む範囲を決める。
    - **前提**：<!-- link:begin input-symbols -->[入力の記号（/ ! @）と Esc](input-symbols.md)<!-- link:end -->

<!-- textlint-disable -->
別名：知らないと損をする操作20・キーボードショートカット・Shift+Tab・外部エディタで書く・画像を貼り付ける・トランスクリプトを見る
<!-- textlint-enable -->

知らないと損をする操作は、Claude Code の対話画面で、知っていると手戻りが減るキー操作とコマンドを、場面から引くページである。キーの割り当ては、公式の文書 [Interactive mode](https://code.claude.com/docs/en/interactive-mode) を読んだ調査資料（確認日 2026-10-29）による。実機では試しておらず、WSL・Linux の CLI を基準に書く。全キーの網羅は公式に任せる。

## 場面から引く {#when}

操作を覚える目的は、Claude の作業が見えないまま任せて、ずれに気づくのが遅れることを防ぐことである。防ぐ原因は「見えていない」で、原理は「見せる」である。Claude に画面や長い背景を見せ、人は Claude の作業を見る。渡す操作と見る操作を、次の表で場面から引く。

| 場面 | 操作 | 詳しく |
| --- | --- | --- |
| 確認の出方を作業に合わせたい | `Shift+Tab` | [モードを切り替える](#modes) |
| 長い指示を落ち着いて書きたい | `Ctrl+G` | [長い指示と画像を渡す](#input) |
| 画面の不具合を見せたい | 画像の貼り付け | [長い指示と画像を渡す](#input) |
| Claude が何をしたかを確かめたい | `Ctrl+O` | [様子を見る・背景に回す](#watch-and-background) |
| 長い処理を待たずに次を頼みたい | `Ctrl+B` | [様子を見る・背景に回す](#watch-and-background) |
| 作業が違う方向に進んだ | `Esc` | <!-- link:begin input-symbols#esc -->[入力の記号（/ ! @）と Esc › Esc で止める・割り込む](input-symbols.md#esc)<!-- link:end --> |

## モードを切り替える {#modes}

権限モードを切り替えるキーは `Shift+Tab` である。押すたびに権限モードが替わるので、押した後は、表示されたモードの名前を目で確かめる。どのモードで何が確認なしに進むかは、<!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](permission-modes-overview.md#modes)<!-- link:end --> が持つ。コマンドや起動時の指定を含む切り替え方は、<!-- link:begin permission-modes-overview#switch -->[権限モードの選び方 › 切り替え方](permission-modes-overview.md#switch)<!-- link:end --> が持つ。本ページは、キーで切り替える場面の判断だけを持つ。

確認を減らす向きへ切り替える前に、戻る手段を用意する。確認が減るほど、止めてもらえる機会も減るからである。Bash だけが変えたファイルは `/rewind` で戻らないので、変更を commit 済みにしてから切り替える。戻せるものと戻せないものは <!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> に、git との組み合わせ方は <!-- link:begin checkpoints-and-rewind#with-git -->[チェックポイントと /rewind（git との違い） › git と組み合わせる](checkpoints-and-rewind.md#with-git)<!-- link:end --> にある。

起動したときのモードは、版で変わってきた。手元の既定は <!-- link:begin permission-modes-overview#defaults -->[権限モードの選び方 › 既定のモードと版](permission-modes-overview.md#defaults)<!-- link:end --> の確かめ方で見る。表示の名前も変わっていて、いまの呼び方は <!-- name:begin default-to-manual-mode -->Manual（権限モード。設定の値は default のまま）<!-- name:end --> である。

!!! example "判断例：小さな修正を続けて頼む"
    - **状況**：1 つのファイルの小さな修正を 10 回ほど続けて頼む。変更は commit 済みで、ほかのファイルには触れない。
    - **迷う候補**：確認を見ながら今のモードのまま進める。または `Shift+Tab` で確認を減らす向きに切り替える。
    - **選んだもの**：commit 済みなのを確かめてから、確認を減らす向きに切り替える。
    - **理由**：戻る先があり、範囲も 1 つのファイルに限られるので、確認の手間を減らす価値が上回る。範囲が広がる依頼に移ったら、`Shift+Tab` で確認の出る側に戻す。

## 長い指示と画像を渡す {#input}

長い指示は、入力欄に直接打たず、`Ctrl+G` で外部エディタに出して書く。入力を外部エディタで編集でき、目的・完了の条件・着手点・触らないものを見直しながら書ける。書き足りない依頼で手戻りするのを防ぐ。どのエディタが開くかの設定は、公式の文書で確かめる（本ページでは未確認）。

書く中身は、目的と完了を成果で、着手点を具体的に書く。迷う場面は、選択肢と推奨案を出させる。この骨組みを雛形にした。

<!-- gen:begin snippet must-know-operations/long-instruction -->
<!-- textlint-disable -->

??? example "雛形：長い指示の骨組み（Ctrl+G で開いた外部エディタに書く）"

    ```markdown
    # 依頼：<一言で>

    ## 目的
    <何のためか。直したい困りごと、または作りたいもの>

    ## 完了の条件
    - <成果で書く。例：`pytest tests/foo` が通る>

    ## 着手点
    - <最初に見てほしいファイルのパス>
    - <関連しそうなコマンドや画面>

    ## 触らないもの
    - <範囲外のファイルや挙動>

    ## 判断に迷ったら
    - <選択肢と推奨案を出して、私の返事を待つ>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet must-know-operations/long-instruction -->

複数行を書くだけなら、`/terminal-setup` を実行して `Shift+Enter` で改行する方法もある。書きかけを退避して戻すのは `Ctrl+S`、過去の入力を探すのは `Ctrl+R` である。

画面の不具合・図・エラーの見た目は、画像で貼る。貼るキーは `Ctrl+V`（Windows と WSL では `Alt+V`）で、入力欄に `[Image #N]` の形で入る。画像の読み取りには誤りが残るので、エラーの文面などの要点は文字でも貼る。

<!-- gen:begin snippet must-know-operations/screenshot-request -->
<!-- textlint-disable -->

??? example "雛形：画像で渡すときの依頼文"

    ```markdown
    添付の画像は、<画面の名前>で<操作>をしたときの表示です。

    - 期待していた表示：<…>
    - 実際の表示：<…>（画像の<場所>の部分）
    - 再現の手順：<1〜3 行>
    - エラーの文面は、画像の読み違いを防ぐために文字でも貼ります：
      <エラーの文面>

    まず画像から読み取れたことを短く言い直してください。そのうえで、原因の候補を挙げてください。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet must-know-operations/screenshot-request -->

画像の使い分けは <!-- link:begin images-and-voice#images -->[画像・スクリーンショット・音声で渡す › 画像で渡すと速いもの](../prompting/images-and-voice.md#images)<!-- link:end --> に、音声でまとめて話して渡す方法は <!-- link:begin images-and-voice#voice -->[画像・スクリーンショット・音声で渡す › 音声でまとめて話して渡す](../prompting/images-and-voice.md#voice)<!-- link:end --> にある。ファイルそのものを渡すなら、画像ではなく <!-- link:begin input-symbols#at -->[入力の記号（/ ! @）と Esc › @ ファイルを直接指す](input-symbols.md#at)<!-- link:end --> を使う。

## 様子を見る・背景に回す {#watch-and-background}

作業の様子を見る操作は、見たいものによって選ぶ。任せた作業が見えないと、ずれに気づくのが遅れる。見る手段を先に決めてから任せる。

| 見たいもの | 操作 |
| --- | --- |
| Claude が行った作業の経過（トランスクリプト） | `Ctrl+O` |
| Claude の To-do（作業の予定） | `Ctrl+T` |
| 変更の差分 | `/diff` |
| 最後のプロンプトと要約だけ | `/focus` |
| ちらつきのない全画面の表示 | `/tui fullscreen` |

作業が違う方向に進んだと見えたら、早く止めるほど手戻りが小さい。止め方は <!-- link:begin input-symbols#esc -->[入力の記号（/ ! @）と Esc › Esc で止める・割り込む](input-symbols.md#esc)<!-- link:end --> にある。`Esc` を 2 回押す操作は、入力のクリアか rewind のどちらかに働くので、押した後の表示を確かめる。戻し方は <!-- link:begin checkpoints-and-rewind#how-to -->[チェックポイントと /rewind（git との違い） › 最小の使い方](checkpoints-and-rewind.md#how-to)<!-- link:end --> にある。

実行中のタスクは、`Ctrl+B` で背景に回せる。長い処理を待つ間に、次の依頼を出したいときに使う。処理ではなく、セッションごと背景に回す方法もある。向く作業と向かない作業は <!-- link:begin agent-view-and-background#what-fits -->agent view と背景セッション › 向く作業と向かない作業（準備中）<!-- link:end --> に、同時に動かす数の決め方も同じページにある。本筋を汚さずに短く聞きたいだけなら、<!-- link:begin side-questions-btw#which -->本筋を汚さずに聞く（/btw） › /btw・新しい会話・サブエージェントの使い分け（準備中）<!-- link:end --> の使い分けを見る。

離れる前の作業は、セッションに名前を付けておくと戻りやすい。再開は <!-- link:begin resume-and-branch#resume -->セッションに名前を付けて再開・分岐する › 再開する（準備中）<!-- link:end --> にある。

## 端末と WSL での違い {#terminals}

キーの割り当ては、端末と面で違う。本文は WSL・Linux の CLI を基準にしたが、ここに挙げる違いは、公式の文書による記述で、実機では試していない。

- **画像の貼り付け**：`Ctrl+V` が基本である。iTerm2 では `Cmd+V`、Windows 側の端末と WSL では `Alt+V` と書かれている。
- **Option を使うキー**：`Option+P`（モデル切替）・`Option+T`（thinking 切替）・`Option+O`（fast mode）は Mac の表記である。WSL・Linux での対応は未確認。
- **一覧**：どのキーが使えるかは、入力欄で `?` を押すと出るショートカットの一覧で確かめる。
- **IDE 拡張**：VS Code などの拡張には、`!` のシェルの近道とタブ補完がない。選択範囲の参照は `Option+K`（Mac）か `Alt+K` で入れる。公式の文書による（確認日 2026-11-03）。動作は試していない。
- **日本語の入力と表示**：IME の不具合や文字化けは、版ごとに個別に直されてきた。まず <!-- link:begin windows-wsl-ime#version -->Windows・WSL・IME で困ったら › まず版と既知の不具合を確かめる（準備中）<!-- link:end --> を見る。WSL については <!-- link:begin windows-wsl-ime#wsl -->Windows・WSL・IME で困ったら › WSL で使う（準備中）<!-- link:end --> がある。

## 効かない場面・落とし穴 {#pitfalls}

- **モードの切り替えは、権限の鍵ではない**：`Shift+Tab` は確認の出方を替える操作である。モードの上に権限ルールが重なるので、止めたい操作はルールで止める。
- **`@` の参照は、フックを通らない**：`@` で渡したファイルはツール呼び出しを伴わず、PreToolUse フックが走らない。読ませたくないパスは、`Read` の deny ルールで守る。
- **画像の読み取りは外れる**：画像だけを貼って「直して」と頼むと、読み違いに気づかないまま進む。要点は文字でも貼り、最初に読み取った内容を言い直させる。
- **Esc の 2 回押しは、1 つの動きに決まらない**：入力のクリアか rewind に働く。連打せず、押した後の表示を確かめる。
- **背景に回しても、結果は自動では読まれない**：背景のタスクの出力は、Claude に頼んで読ませる。

## 比べる相手 {#compare}

- **入力の記号**：`/`・`!`・`@`・`Esc` は、入力欄の先頭や途中で意味を持つ記号である。キー操作との分担は <!-- link:begin input-symbols#which -->[入力の記号（/ ! @）と Esc › 入力の記号の使い分け](input-symbols.md#which)<!-- link:end --> にある。
- **コマンドの早見表**：コマンド全般を引くなら <!-- link:begin command-cheatsheet -->主要コマンド早見表（準備中）<!-- link:end --> を見る。本ページは、キーと場面の判断に絞る。
- **権限モードの選び方**：切り替え先の選び方は <!-- link:begin permission-modes-overview#examples -->[権限モードの選び方 › 選び方の判断例](permission-modes-overview.md#examples)<!-- link:end --> にある。本ページは、切り替えるキーを持つ。
- **背景セッション**：処理でなく作業を丸ごと背景に回すなら <!-- link:begin agent-view-and-background -->agent view と背景セッション（準備中）<!-- link:end --> を使う。

## 古くなった助言 {#outdated}

古い記事には、消えたコマンドを使う手順が出てくる。台帳の行は <!-- link:begin outdated-advice-ledger#removed-commands -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#removed-commands)<!-- link:end --> にある。この操作に関わるのは次である。

- **Vim の操作の切り替え**：`/vim` は消えた。今は <!-- name:begin vim-to-editor-mode -->/config の Editor mode（Vim と Normal の切り替え）<!-- name:end --> で行う。
- **背景の出力を読むツール**：TaskOutput ツールは消えた。背景のタスクの出力は、Claude に頼んで読ませる。
- **`#` で CLAUDE.md に書き足す近道**：入力の記号の側の古い助言で、<!-- link:begin input-symbols#outdated -->[入力の記号（/ ! @）と Esc › 古くなった助言](input-symbols.md#outdated)<!-- link:end --> にまとめている。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [入力の記号（/ ! @）と Esc](input-symbols.md)

**関連**

- 主要コマンド早見表（準備中）
- [権限モードの選び方](permission-modes-overview.md)
- [チェックポイントと /rewind（git との違い）](checkpoints-and-rewind.md)
- セッションに名前を付けて再開・分岐する（準備中）
- 本筋を汚さずに聞く（/btw）（準備中）
- [画像・スクリーンショット・音声で渡す](../prompting/images-and-voice.md)
- agent view と背景セッション（準備中）
- Windows・WSL・IME で困ったら（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Interactive mode](https://code.claude.com/docs/en/interactive-mode)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
