---
id: input-symbols
title: 入力の記号（/ ! @）と Esc
aliases: [入力の4記号, スラッシュコマンド, '! でシェルを実行する', '@ でファイルを参照する', Esc で止める, 割り込んで指示する]
type: feature
field: cli
chapter: 入力と基本の操作
order: 10
level: 使う
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: / でコマンドとスキルを呼び、! で自分でシェルを実行して結果を会話に入れ、@ でファイルを直接指し、Esc で作業を止めて方向を直す。ずれに気づいたら早く止めるほど手戻りが小さい。
signs:
  - {type: goal, text: Claude Code の入力欄でできることを最初に知りたい}
  - {type: symptom, text: 間違った方向に進み始めたのに、止め方が分からない, anchor: esc}
prerequisites: []
related: [must-know-operations, choose-what-to-read, checkpoints-and-rewind, ask-claude-code, command-cheatsheet, images-and-voice]
tracks: [interactive-mode]
outdated_advice: [hash-to-memorize]
sources: [cc-docs-interactive-mode, cc-docs-commands, cc-docs-how-claude-code-works, cc-changelog]
volatility: 中
sections:
  - {title: 入力の記号の使い分け, anchor: which}
  - {title: / でコマンドとスキルを呼ぶ, anchor: slash}
  - {title: '! シェルを自分で走らせる', anchor: bang}
  - {title: '@ ファイルを直接指す', anchor: at}
  - {title: Esc で止める・割り込む, anchor: esc}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: つながる操作, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：`/` でコマンドとスキルを呼び、`!` でシェルを自分で走らせ、`@` でファイルを指し、`Esc` で作業を止めて方向を直す。
    - **いつ引くか**：Claude Code の入力欄でできることを最初に知りたいとき。間違った方向に進み始めたのに、止め方が分からないとき。
    - **強制力**：<!-- gen:begin feature enforcement -->なし<!-- gen:end feature enforcement -->。入力の操作であり、禁止や上限の仕組みではない。
    - **止められること**：`Esc` は今の応答と道具の呼び出しを止める。すでに起きたファイルの変更は戻さない。
    - **前提**：なし

<!-- textlint-disable -->
別名：入力の4記号・スラッシュコマンド・! でシェルを実行する・@ でファイルを参照する・Esc で止める・割り込んで指示する
<!-- textlint-enable -->

入力の記号は、Claude Code の入力欄の先頭などに打つ短い印で、普通の依頼とは別の動きを起こす。`/`・`!`・`@` と `Esc`（コマンド、シェル、ファイル指定、中断）を覚えれば、最初の日の操作はほぼ足りる。記号の数や割り当ては版で変わるので、手元の表は `?` で確かめる。

## 入力の記号の使い分け {#which}

入力の記号は、Claude に見えていないものを見せ、進む方向を直すための道具である。Claude は、あなたが別の窓で見ている端末の出力や、まだ指していないファイルを知らない。`!` と `@` はそうしたものを Claude の前に出し、`/` は決まった手順を呼び、`Esc` は進む方向を直す入口になる。

| 記号 | 打つ場所 | 何が起きるか | 使う場面 |
| --- | --- | --- | --- |
| `/` | メッセージの先頭 | コマンドかスキルを呼ぶ | 設定を変える、決まった手順を呼ぶ |
| `!` | メッセージの先頭 | シェルのコマンドを自分で走らせ、出力を会話に入れる | 結果を Claude にも見せたい確認 |
| `@` | 文中のどこでも | ファイルのパスの候補を出して指す | 読むファイルが分かっている依頼 |
| `Esc` | 作業中 | 今の応答や道具の呼び出しを止める | 方向のずれに気づいた |

使い分けの基準は、誰が何を決めるかである。呼ぶコマンド、走らせるシェル、指すファイルを自分で決めるなら、記号で直接渡す。何をするかを Claude に決めさせるなら、普通の依頼として頼む。

## / でコマンドとスキルを呼ぶ {#slash}

`/` は、メッセージの先頭に打つと、コマンドかスキルを呼ぶ記号である。`/` に続けて文字を打つと、メニューの候補が絞られる。引数は、コマンド名の後ろに続けて書く。

メニューには、組み込みのコマンドのほか、自作や同梱のスキル、プラグインや MCP サーバーが足したコマンドも並ぶ。プランや面によって見えないコマンドもある。名前を忘れたら、`/` だけを打って一覧から探す。

`/` が働くのは、メッセージの先頭にあるときだけである。文の途中の `/` は、コマンド名の補完が出ることはあっても、コマンドとしては走らない。`/tmp/notes.md` のようなパスを文中に書いても、コマンドとは見なされない。

コマンドの全部は覚えなくてよい。よく使うものは <!-- link:begin command-cheatsheet -->[主要コマンド早見表](command-cheatsheet.md)<!-- link:end --> で引く。公式の一覧は [Commands](https://code.claude.com/docs/en/commands) にある。使い方が分からないコマンドは、<!-- link:begin ask-claude-code#what-to-ask -->[Claude Code 自身に聞く › 何を聞けるか](ask-claude-code.md#what-to-ask)<!-- link:end --> のとおり Claude Code 自身に聞く。

## ! シェルを自分で走らせる {#bang}

`!` は、メッセージの先頭に打つと、続くシェルのコマンドを自分で走らせ、その出力を会話に入れる記号である。`! npm test` と打てば、テストが走り、結果が Claude の前に出る。

仕組みの要点は 4 つある。

- あなたの打ったコマンドが、Claude の解釈や許可を挟まずそのまま走る。
- 進み具合と出力は、実行中にその場で見える。
- 長く走るコマンドは、`Ctrl+B` で背景に回せる。
- 先頭が `!` の入力欄では、過去の `!` のコマンドを `Tab` で補完できる。

出力が会話に入ると、Claude はそれを受けて自動で応答する。`! npm test` だけで、失敗の説明まで進む。応答は普通の依頼を送るのと同じだけ使用量を使う。出力を入れるだけで応答させたくないときは、設定の `respondToBashCommands` を `false` にする。

`!` を使うのは、Claude にも見せたい確認を、自分の手で走らせたいときである。Claude に「テストを走らせて」と頼むと、どのコマンドで走らせるかは Claude が選び、許可の確認も通る。自分でコマンドを決めたい、許可の確認を挟まずに走らせたい、と思うときに `!` を使う。

!!! example "判断例：テストの失敗を調べる"
    - **状況**：手元のテストが落ちている。原因は分からないが、どのコマンドで落ちるかは自分が知っている。
    - **迷う候補**：`! npm test` で自分で走らせる。または「テストを走らせて原因を調べて」と頼む。
    - **選んだもの**：まず `! npm test` で走らせ、出力を会話に入れる。
    - **理由**：コマンドが決まっているので、Claude に選ばせる意味が薄い。出力が会話に入れば、Claude はそのまま原因の説明に進める。原因が複数のファイルにまたがるなら、そこから先は普通の依頼で調べさせる。

## @ ファイルを直接指す {#at}

`@` は、依頼の中でファイルのパスを指す記号である。`@` に続けてパスの先頭を打つと、ファイルの候補が出る。候補から選べば、パスを打ち間違えずに指せる。

指す効用は、探させる手間を省くことにある。読むべきファイルが分かっているなら、`@` で指したほうが、Claude が検索を繰り返すより速く、関係のないファイルを読む場面も減る。反対に、どこにあるか分からないものは、指さずに探させる。この分け方は <!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](../context/choose-what-to-read.md#point-or-search)<!-- link:end --> に詳しい。

`@` で指しても、指したファイルの中の大きな出力や関係のない部分まで読ませる危険は残る。<!-- link:begin choose-what-to-read#caveats -->[@参照と、何を読ませるかの絞り込み › @ 参照の注意](../context/choose-what-to-read.md#caveats)<!-- link:end --> を読んでから使う。

## Esc で止める・割り込む {#esc}

`Esc` は、作業の途中の応答や道具の呼び出しを止めて、方向を直すための操作である。止めても、そこまでの作業は会話に残る。

ずれに気づいたら、早く止めるほど手戻りが小さい。間違った方向に進んだ作業の上に直しを重ねると、直す範囲が広がるためである。止めた後は、止めた理由と進めたい方向を書いて送る。書き方の雛形は後の節にある。

作業中に別のメッセージを打って `Enter` を押すと、割り込みにはならず、メッセージが待ち行列に入る。Claude は、今の道具の呼び出しが終わった後に、同じ応答の流れの中でそれを受け取る。待たずに止めたいときは `Esc` を使う。待ち行列にメッセージがあるときに `Esc` を押すと、作業が止まり、待っていたメッセージがすぐ送られる。

`Esc` を 2 回押すと、動きが入力欄の状態で変わる。

- 入力欄に文字があるときは、下書きを消す。下書きは履歴に残り、上矢印で呼び戻せる。
- 入力欄が空のときは、巻き戻しのメニューが開く。コードと会話を、前の時点に戻せる。

巻き戻しで戻るものと戻らないものは、<!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> にある。`Ctrl+C` も実行中の処理を止めるが、何も走っていないときの 1 回目は入力欄を消す動きになる。迷ったら、作業を止めるときは `Esc` を使う。

!!! example "判断例：ずれに気づいたとき"
    - **状況**：Claude が、頼んだのとは別のモジュールを書き換え始めた。まだ 1 つ目のファイルの途中である。
    - **迷う候補**：`Esc` で止めて方向を直す。または「そのモジュールは触らないで」と打って `Enter` で待ち行列に入れる。
    - **選んだもの**：`Esc` で止める。
    - **理由**：待ち行列のメッセージは、今の道具の呼び出しが終わるまで届かない。書き換えが進んでから届くと、戻す範囲が広がる。小さな補足なら、待ち行列に入れるほうが作業の流れを切らない。

Vim のモードを使っているときは、`Esc` の動きが変わる。入力欄では NORMAL モードへ入る操作になるので、作業を止める操作とは分けて考える。旧名のコマンド `/vim` は、今は <!-- name:begin vim-to-editor-mode -->/config の Editor mode（Vim と Normal の切り替え）<!-- name:end --> である。

## 雛形 {#templates}

`@` で指して頼む型と、`Esc` で止めた後に方向を直す型を、雛形にした。どちらも依頼の本文に使う。

<!-- gen:begin snippet input-symbols/point-with-at -->
<!-- textlint-disable -->

??? example "雛形：@ でファイルを指して頼む雛形"

    ```text
    @<ファイルのパス> の <関数や節の名前> を読んで、<してほしいこと>。
    変えるのは <範囲> だけで、<触れないもの> は変えない。
    終わったら <確かめる方法> で確かめて、結果を見せて。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet input-symbols/point-with-at -->

<!-- gen:begin snippet input-symbols/redirect-after-esc -->
<!-- textlint-disable -->

??? example "雛形：Esc で止めた後に方向を直す雛形"

    ```text
    止めたのは、<止めた理由。例：想定と違うファイルを変え始めたため>。
    ここまでの変更のうち、<残すもの> は残して、<戻すもの> は戻して。
    そのうえで、次は <進めたい方向> で進めて。始める前に、何をするかを 3 行で教えて。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet input-symbols/redirect-after-esc -->

## 効かない場面・落とし穴 {#pitfalls}

- **`!` は、あなたの権限でそのまま走る。** Claude の許可の確認を通らない。サンドボックスを有効にしていても、`!` で打ったコマンドはその外で走るのが基本である（例外は公式の文書にある）。自分で責任を持てるコマンドだけを打つ。
- **`!` の出力は全部会話に入る。** 長いログを出すコマンドを打つと、会話が長くなり、答えがぼやける。出力は要点の数行に絞ってから入れる。方法は <!-- link:begin choose-what-to-read#trim-output -->[@参照と、何を読ませるかの絞り込み › 出力を絞る](../context/choose-what-to-read.md#trim-output)<!-- link:end --> にある。
- **`/` は先頭でしか働かない。** 文の途中に書いたコマンド名は、Claude への文章として読まれる。
- **`Esc` は変更を元に戻さない。** 止めた時点までの変更はファイルに残りうる。止めた後は差分を確かめ、必要なら巻き戻すか、git と組み合わせる。組み合わせ方は <!-- link:begin checkpoints-and-rewind#with-git -->[チェックポイントと /rewind（git との違い） › git と組み合わせる](checkpoints-and-rewind.md#with-git)<!-- link:end --> にある。
- **キーの割り当ては端末と面で違う。** ここに書いたのは、WSL・Linux の端末の Claude Code を基準にした話である。ほかの OS と IDE 拡張での動作は未確認。端末ごとの違いは <!-- link:begin must-know-operations#terminals -->[知らないと損をする操作 › 端末と WSL での違い](must-know-operations.md#terminals)<!-- link:end --> にある。

## つながる操作 {#compare}

入力の記号は最初の入口で、ほかの操作と組み合わせて使う。

- モードの切り替えや、長い指示・画像の渡し方、背景に回す操作は、<!-- link:begin must-know-operations -->[知らないと損をする操作](must-know-operations.md)<!-- link:end --> にまとまっている。
- 画像や音声で渡すと速いものは、<!-- link:begin images-and-voice -->[画像・スクリーンショット・音声で渡す](../prompting/images-and-voice.md)<!-- link:end --> にある。
- 止めた後の巻き戻しと要約は、<!-- link:begin checkpoints-and-rewind -->[チェックポイントと /rewind（git との違い）](checkpoints-and-rewind.md)<!-- link:end --> にある。
- 機能の使い方を迷ったら、<!-- link:begin ask-claude-code -->[Claude Code 自身に聞く](ask-claude-code.md)<!-- link:end --> のとおり、Claude Code 自身に聞く。

## 古くなった助言 {#outdated}

古い記事には、入力の先頭に `#` を付けて、その行を CLAUDE.md に覚えさせる近道が出てくる。今の入力の記号の表に `#` はなく、この近道は使えない。CLAUDE.md に足したいことは、Claude に CLAUDE.md の編集を頼むか、`/memory` でファイルを開いて自分で書く。詳しい経緯は <!-- link:begin outdated-advice-ledger#hash-to-memorize -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#hash-to-memorize)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Interactive mode](https://code.claude.com/docs/en/interactive-mode)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [知らないと損をする操作](must-know-operations.md)
- [Claude Code 自身に聞く](ask-claude-code.md)
- [チェックポイントと /rewind（git との違い）](checkpoints-and-rewind.md)

**関連**

- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- [主要コマンド早見表](command-cheatsheet.md)
- [画像・スクリーンショット・音声で渡す](../prompting/images-and-voice.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
