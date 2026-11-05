---
id: command-cheatsheet
title: 主要コマンド早見表
aliases: [スラッシュコマンド一覧, コマンド一覧, 旧コマンドとの対応]
type: ledger
field: cli
chapter: 早見表
order: 190
priority: 推奨
surfaces: [claude-code]
principle: []
prevents: []
pitfalls: []
summary: よく使うコマンドを、何に使うか・判断を書いたページ・旧名とあわせて引ける。全コマンドの網羅は公式の一覧に任せる。
signs:
  - {type: goal, text: コマンドの名前や、古い記事で見た旧名から、使い方のページを引きたい}
prerequisites: []
related: [input-symbols, must-know-operations, ask-claude-code, init-and-first-claude-md, term-index#old-names, outdated-advice-ledger]
tracks: []
outdated_advice: [slash-cost-and-stats, fork-to-branch, removed-commands, commands-directory, agents-command]
sources: [cc-docs-commands, cc-changelog, cc-docs-changelog]
volatility: 高
sections:
  - {title: 引き方, anchor: how-to-read}
  - {title: コマンドから引く, anchor: by-command}
  - {title: 旧名から今の名前を引く, anchor: by-old-name}
  - {title: 名前が変わるときの型, anchor: patterns}
  - {title: 自分の手順書や記事で見つける, anchor: find-in-your-setup}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：コマンドの名前や古い記事で見た旧名から、使い方と判断を書いたページを引ける。
    - **いつ引くか**：コマンドの名前や、古い記事で見た旧名から、使い方のページを引きたいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：スラッシュコマンド一覧・コマンド一覧・旧コマンドとの対応
<!-- textlint-enable -->

主要コマンド早見表は、Claude Code でよく使うコマンドを、どのページに判断が書いてあるかと一緒に引く表である。古い記事で見た旧名から、今の名前を引くこともできる。全コマンドの一覧は載せず、公式の [Commands](https://code.claude.com/docs/en/commands) に任せる。

## 引き方 {#how-to-read}

このページの表は、コマンドの名前から、判断を書いたページへ飛ぶための索引である。コマンドの使いどころ、使わないほうがよい場面、前後の手順は、行き先のページにある。表には書かない。

「コマンドから引く」の表は、次の 3 列でできている。

- **左の列は、コマンドの名前。** 打つ文字のまま書いてある。
- **真ん中の列は、判断を書いたページ。** 迷ったら、まずここへ飛ぶ。
- **右の列は、そのコマンドで何ができるかの一言。** 使い方の手順ではなく、探しているものかを見分ける印である。

コマンドは版が上がるたびに増え、名前も変わる。ここに載せていないコマンドも、手元の版にしかないコマンドもある。手元の版で何が打てるかは、<!-- link:begin ask-claude-code#check-version -->[Claude Code 自身に聞く › 答えの版を確かめる](ask-claude-code.md#check-version)<!-- link:end --> のとおり、答えの版を確かめながら Claude Code 自身に聞く。`/` から始まる入力の基本は <!-- link:begin input-symbols#slash -->[入力の記号（/ ! @）と Esc › / でコマンドとスキルを呼ぶ](input-symbols.md#slash)<!-- link:end --> にある。

この早見表は、WSL・Linux の端末の Claude Code を基準にしている。ほかの OS と IDE 拡張でのコマンドの動作は未確認である。

## コマンドから引く {#by-command}

主要なコマンドを、使いたい場面のまとまりごとに並べる。

**会話と文脈を整える**

| コマンド | 判断を書いたページ | 何ができるか |
| --- | --- | --- |
| `/clear` | <!-- link:begin when-to-start-fresh -->[新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<!-- link:end --> | 会話を空にして新しく始める |
| `/compact` | <!-- link:begin compact-and-auto-compact -->[/compact と自動圧縮](../context/compact-and-auto-compact.md)<!-- link:end --> | 残す焦点を指示して、会話を要約して続ける |
| `/context` | <!-- link:begin inspect-context -->[/context で中身を見る](../context/inspect-context.md)<!-- link:end --> | 文脈の内訳を見る |
| `/btw` | <!-- link:begin side-questions-btw -->[本筋を汚さずに聞く（/btw）](../context/side-questions-btw.md)<!-- link:end --> | 答えが会話の履歴に入らないサイド質問をする |
| `/rewind` | <!-- link:begin checkpoints-and-rewind -->[チェックポイントと /rewind（git との違い）](checkpoints-and-rewind.md)<!-- link:end --> | 以前の時点に、コード・会話・その両方を戻す |

**セッションを続ける・分ける**

| コマンド | 判断を書いたページ | 何ができるか |
| --- | --- | --- |
| `/resume` | <!-- link:begin resume-and-branch#resume -->[セッションに名前を付けて再開・分岐する › 再開する](resume-and-branch.md#resume)<!-- link:end --> | 前のセッションの続きから再開する |
| `/rename` | <!-- link:begin resume-and-branch#naming -->[セッションに名前を付けて再開・分岐する › 名前の付け方](resume-and-branch.md#naming)<!-- link:end --> | セッションに名前を付けて、戻る先を探しやすくする |
| `/branch` | <!-- link:begin resume-and-branch#branch -->[セッションに名前を付けて再開・分岐する › 分岐して別案を試す](resume-and-branch.md#branch)<!-- link:end --> | 会話を分岐して、別の案を試す |
| `/teleport` | <!-- link:begin cloud-sessions-and-teleport#teleport -->[クラウドセッションと teleport › teleport で取り込む](cloud-sessions-and-teleport.md#teleport)<!-- link:end --> | クラウドのセッションを手元の端末に取り込む |
| `/remote-control` | <!-- link:begin control-from-phone -->スマホから操作する（Remote Control）<!-- link:end --> | 手元のセッションをブラウザやスマホから操作する |

**状態を見る・設定する**

| コマンド | 判断を書いたページ | 何ができるか |
| --- | --- | --- |
| `/usage` | <!-- link:begin usage-context-statusline#instruments -->[/usage・/context・ステータスラインで状態を見る › 三つの道具で見えるもの](usage-context-statusline.md#instruments)<!-- link:end --> | 上限の使い方を見る |
| `/statusline` | <!-- link:begin usage-context-statusline#statusline -->[/usage・/context・ステータスラインで状態を見る › ステータスラインに出すもの](usage-context-statusline.md#statusline)<!-- link:end --> | ステータスラインに状態を出しておく |
| `/status` | <!-- link:begin settings-layers#verify -->[設定ファイルの階層と優先順位 › 効いているかを確かめる](settings-layers.md#verify)<!-- link:end --> | 読み込まれた設定の層を確かめる |
| `/permissions` | <!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end --> | 許可・確認・拒否のルールを見直す |
| `/output-style` | <!-- link:begin output-style-modes#built-in -->[出力スタイルで応答の仕方を切り替える › 組み込みのスタイル](output-style-modes.md#built-in)<!-- link:end --> | 応答の仕方を切り替える |
| `/ide` | <!-- link:begin using-ides -->IDE（VS Code・JetBrains）で使う<!-- link:end --> | IDE と連携して使う |

**進め方を決める**

| コマンド | 判断を書いたページ | 何ができるか |
| --- | --- | --- |
| `/plan` | <!-- link:begin when-to-plan -->[plan mode の使いどころ](when-to-plan.md)<!-- link:end --> | plan mode で、編集を止めたまま調べさせる |
| `/init` | <!-- link:begin init-and-first-claude-md#run-init -->[/init と最初の CLAUDE.md › /init で叩き台を作る](init-and-first-claude-md.md#run-init)<!-- link:end --> | リポジトリを調べさせて CLAUDE.md の叩き台を作る |
| `/memory` | <!-- link:begin using-auto-memory -->[自動メモリ](../extend/using-auto-memory.md)<!-- link:end --> | CLAUDE.md や自動メモリのファイルを開く |
| `/powerup`・`/insights` | <!-- link:begin ask-claude-code#what-to-ask -->[Claude Code 自身に聞く › 何を聞けるか](ask-claude-code.md#what-to-ask)<!-- link:end --> | 対話のレッスンで使い方を学ぶ。自分の使い方のレポートを出す |

**拡張を扱う**

| コマンド | 判断を書いたページ | 何ができるか |
| --- | --- | --- |
| `/skills` | <!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)<!-- link:end --> | スキルを扱う |
| `/agents` | <!-- link:begin writing-subagents -->[サブエージェントの作り方と使いどころ](../extend/writing-subagents.md)<!-- link:end --> | サブエージェントの作り方の案内を出す |
| `/hooks` | <!-- link:begin hooks-basics -->[フックの考え方とイベント](../enforce/hooks-basics.md)<!-- link:end --> | フックを扱う |
| `/mcp` | <!-- link:begin connecting-mcp -->[MCP をつなぐ](../extend/connecting-mcp.md)<!-- link:end --> | MCP の接続を扱う |
| `/plugin` | <!-- link:begin plugins-and-marketplaces -->[プラグインとマーケットプレイス](../extend/plugins-and-marketplaces.md)<!-- link:end --> | プラグインを扱う |

`/agents` の動きは版で変わった。画面で作る使い方は古く、今の動きは台帳の <!-- link:begin outdated-advice-ledger#agents-command -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#agents-command)<!-- link:end --> にある。

## 旧名から今の名前を引く {#by-old-name}

古い記事や手順書で見たコマンド名から、今の名前を引く。台帳とは、古くなった助言を、今どうするか・変わった時期と版とあわせて並べた別のページである。変わった時期と版、今どうするかの詳しい説明は、右の列の台帳の行にある。

| 旧名 | 今の名前 | 台帳の行 |
| --- | --- | --- |
| `/cost`・`/stats` | <!-- name:begin cost-stats-to-usage -->/usage<!-- name:end --> | <!-- link:begin outdated-advice-ledger#slash-cost-and-stats -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#slash-cost-and-stats)<!-- link:end --> |
| `/fork`（会話の分岐の意味） | <!-- name:begin fork-renamed-branch -->/branch（今の /fork は、会話を新しい背景のセッションに写す別の機能）<!-- name:end --> | <!-- link:begin outdated-advice-ledger#fork-to-branch -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#fork-to-branch)<!-- link:end --> |
| `/vim` | <!-- name:begin vim-to-editor-mode -->/config の Editor mode（Vim と Normal の切り替え）<!-- name:end --> | <!-- link:begin outdated-advice-ledger#removed-commands -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#removed-commands)<!-- link:end --> |
| `/project:<名前>`・`/user:<名前>` | <!-- name:begin project-prefix-removed -->/&lt;名前&gt;（サブディレクトリのファイルは /&lt;フォルダ&gt;:&lt;名前&gt;）<!-- name:end --> | <!-- link:begin outdated-advice-ledger#commands-directory -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#commands-directory)<!-- link:end --> |
| `/review` | <!-- name:begin review-to-code-review -->/code-review<!-- name:end --> | （台帳に行はない） |
| `/allowed-tools` | <!-- name:begin allowed-tools-to-permissions -->/permissions<!-- name:end --> | （台帳に行はない） |

消えたコマンドは、今の名前に当たるものがない。`/pr-comments`・`/tag`・`ultraplan`、それに `TaskOutput` ツールは消えた。それぞれの代わりは台帳の <!-- link:begin outdated-advice-ledger#removed-commands -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#removed-commands)<!-- link:end --> にある。

旧名はコマンドだけではない。`/permissions` のタブの名前も変わり、今は <!-- name:begin recently-denied-to-blocked -->Recently blocked（/permissions のタブ）<!-- name:end --> である。機能名や英語名を含む旧名の全体は、<!-- link:begin term-index#old-names -->[用語索引と旧名の対応 › 旧名から引く](../start/term-index.md#old-names)<!-- link:end --> から引く。

## 名前が変わるときの型 {#patterns}

コマンドの名前の変わり方には型がある。型が分かると、見たことのない旧名にも当たりを付けられる。

- **改名してまとまる。** `/cost` と `/stats` は `/usage` にまとまり、旧名は今も打てる別名として残った。旧名で書かれた手順は動くので、急いで直さなくてよい。新しく書く手順は今の名前で書く。
- **消えて、頼み方や設定に置き換わる。** `/vim` は `/config` の設定に、`/pr-comments` は Claude への直接の依頼に移った。旧名を打っても動かないので、行き先は台帳で確かめる。
- **同じ名前で別の機能になる。** 今の `/fork` は、会話を分岐する旧来の動きではなく、会話を新しい背景のセッションに写す別の機能である。`/agents` も、画面で作る動きから案内を出すだけの動きに変わった。名前が通じても、記事の説明が今の動きと同じとは限らない。
- **仕組みが正式な機能に置き換わる。** `.claude/commands/` に置いたカスタムコマンドは、スキルにまとめられた。既存のファイルは今も動く。新しく作るものはスキルにする。作り方は <!-- link:begin writing-skills#from-commands -->[スキルの作り方 › カスタムコマンドから移る](../extend/writing-skills.md#from-commands)<!-- link:end --> にある。

この規則性は、台帳全体にも通じる。回避策や独自の流儀だった操作が正式な仕組みに置き換わると、旧名は別名として残るか、動かなくなる。次に古くなりそうなものの見当は、<!-- link:begin outdated-advice-ledger#workarounds -->[古くなった助言の台帳 › 回避策は正式な仕組みに置き換わる](../changes/outdated-advice-ledger.md#workarounds)<!-- link:end --> から付けられる。

## 自分の手順書や記事で見つける {#find-in-your-setup}

古い名前は、自分の手順書やスキル、フックの設定にも残っている。見つけ方は、型によって違う。

- **打てば動くもの（`/cost`・`/stats`・`.claude/commands/`）。** 手順書の文字列を探し、新しく書く手順から今の名前にする。
- **動かないもの（`/vim`・`/tag`・`/pr-comments`・`/ultraplan`・`TaskOutput`）。** 手順書、スキル、フックの設定を探す。フックの matcher に `TaskOutput` を書いていれば、もう当たらない。
- **名前が通じるが意味が変わったもの（`/fork`・`/agents`）。** 名前だけで読み替えず、記事がどちらの動きを説明しているかを見る。

!!! example "判断例：記事の /fork をどう読むか"
    - **状況**：古い記事の手順に「`/fork` で会話を分けて、別の方向を試す」とある。手元で同じことをしたい。
    - **迷う候補**：記事のとおり `/fork` を打つ。または、分岐の意味なら `/branch` に読み替える。
    - **選んだもの**：`/branch` に読み替える。
    - **理由**：今の `/fork` は、会話を新しい背景のセッションに写して元の会話を続ける別の機能である。打つと何かは起きるが、記事が説明した分岐とは違う。名前が通じる分、気づきにくい。

手元で名前が通じるかどうかは、打って確かめるより先に、公式の [Commands](https://code.claude.com/docs/en/commands) と、<!-- link:begin ask-claude-code#check-version -->[Claude Code 自身に聞く › 答えの版を確かめる](ask-claude-code.md#check-version)<!-- link:end --> で版を確かめる。それぞれの行の詳しい経緯は <!-- link:begin outdated-advice-ledger#ledger -->[古くなった助言の台帳 › 台帳](../changes/outdated-advice-ledger.md#ledger)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [入力の記号（/ ! @）と Esc](input-symbols.md)
- [知らないと損をする操作](must-know-operations.md)
- [Claude Code 自身に聞く](ask-claude-code.md)
- [/init と最初の CLAUDE.md](init-and-first-claude-md.md)
- [用語索引と旧名の対応 › 旧名から引く](../start/term-index.md#old-names)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
