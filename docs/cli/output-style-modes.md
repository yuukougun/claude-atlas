---
id: output-style-modes
title: 出力スタイルで応答の仕方を切り替える
nav_title: 出力スタイル
aliases: [output style, /output-style, output style（応答のスタイルを切り替える）]
type: feature
field: cli
chapter: 設定と最初の準備
order: 140
level: 整える
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [合っていない]
pitfalls: [預けすぎる]
scenes: [開発, 学習]
summary: 組み込みや自作の出力スタイルで、説明の多さ・簡潔さ・確認の仕方・学び方をセッション全体について切り替える。何を知るべきかは CLAUDE.md、どう答えるかは出力スタイルに置く。
signs:
  - {type: goal, text: 説明を増やしたり簡潔にしたりを、毎回言わずに切り替えたい}
  - {type: goal, text: コードを学びながら進めたいので、一部を自分で書きたい}
prerequisites: []
related: [claude-md-vs-rules-skills-styles, init-and-first-claude-md, learning-with-ai, how-much-understanding-to-keep, keeps-stopping, does-more-than-asked, keep-replies-in-japanese#instructions, what-subagents-dont-inherit, permission-modes-overview]
tracks: [output-styles]
outdated_advice: []
sources: [cc-docs-output-styles, cc-docs-features-overview, cc-changelog]
volatility: 中
sections:
  - {title: 組み込みのスタイル, anchor: built-in}
  - {title: 切り替え方, anchor: switch}
  - {title: 自作のスタイル, anchor: custom}
  - {title: 効かない場面・落とし穴, anchor: limits}
  - {title: CLAUDE.md・スキルとの分担, anchor: vs-claude-md}
  - {title: 日本語の応答との関係, anchor: japanese}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：応答の量・簡潔さ・確認の仕方・学び方を、組み込みか自作の出力スタイルでセッション全体について切り替える。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。スタイルは Claude が従う指示で、何も止められない。必ず起きることはフックに置く。
    - **いつ引くか**：説明を増やしたり簡潔にしたりを、毎回言わずに切り替えたいとき。コードを学びながら進めたいので、一部を自分で書きたいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：output style・/output-style・output style（応答のスタイルを切り替える）
<!-- textlint-enable -->

出力スタイルは、Claude Code が毎回のリクエストで Claude に渡す、役割・口調・応答の形の指示である。依頼の文に「簡潔に」「理由も説明して」と毎回足す代わりに、セッションの単位で一度に選べる。

何を知るべきかは CLAUDE.md、どう答えるかは出力スタイル、必ず起きることはフック、という分担が公式の勧めである。この分担の詳細は節 [CLAUDE.md・スキルとの分担](#vs-claude-md) にある。

## 組み込みのスタイル {#built-in}

組み込みのスタイルは、スタイルを選ばない状態（Default）のほかに 4 種ある。どれも Default の指示を残し、そこへ自分の指示を足す。種類と入った版は数値ファイルの機能の項目にあり、題名や本文には並べない。

| スタイル | 変わること | 向く場面 |
| --- | --- | --- |
| Proactive | 日常的な判断で確認せず、仮定を置いて進める | 途中の確認が多く、間違っていたら後で直せばよい作業 |
| Concise | 最初の 1 文で結果を述べ、前置き・実況・最後のまとめを省く | 既定の応答が長すぎると感じるとき |
| Explanatory | 選択の理由を `Insight` と題した短いブロックで足す | 知らないコードベースに慣れたいとき |
| Learning | Explanatory に加え、設計判断を含む数行を利用者に書かせる | 作業を進めながら手を動かして学びたいとき |

次の点を知っておくと選びやすい。

- Proactive は権限モードを変えない。確認が減るのは「Claude が尋ねる」部分だけで、ツールの許可の確認は権限モードのとおりに出る。権限は <!-- link:begin permission-modes-overview -->[権限モードの選び方](permission-modes-overview.md)<!-- link:end --> で決める。
- Proactive でも、データの削除や共有環境を変える操作の前には、会話の中で確認するよう指示される。これも指示であり、許可の画面とは別である。
- Concise は、頼まれた説明、エラー、テストの失敗、破壊的な操作の確認を省かない。エンジニアリングの作業そのものは Default と同じ丁寧さで進める。
- Concise は新しい組み込みで、古い版の Claude Code にはない。使えるか迷うときは版を確かめる。
- Learning は、`TODO(human)` というコメントを置いて作業を止め、何を書くかを説明してから待つ。書き終えたと伝えると、Claude が続きに進む。

Learning の学習の効果を実証したデータは、確認できていない。ここでの説明は設計の意図であり、理解が残るかは使い方による。理解を確かめる使い方は <!-- link:begin learning-with-ai#patterns -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる） › 理解が残る使い方・残らない使い方](../judgment/learning-with-ai.md#patterns)<!-- link:end --> に、どこまでを自分の理解に残すかは <!-- link:begin how-much-understanding-to-keep#core-and-periphery -->[どこまで理解を手放してよいか（中核と周辺） › 中核と周辺を分ける](../judgment/how-much-understanding-to-keep.md#core-and-periphery)<!-- link:end --> にある。

!!! example "判断例：新しいコードベースに入ったばかりの週"
    - **状況**：初めて触るリポジトリで、小さな機能を追加する。締め切りは緩いが、構造を覚えたい。
    - **迷う候補**：Explanatory で理由を読みながら進める。Learning で核になる数行を自分で書く。
    - **選んだもの**：最初の数日は Explanatory にし、構造が分かってから、設計判断のある作業だけ Learning に切り替える。
    - **理由**：Learning は作業のたびに止まって自分で書くので、構造が分からないうちは書く手が止まりやすい。まず読んで地図を作り、次に手を動かす順にすると、止まる回数が減る。

## 切り替え方 {#switch}

出力スタイルを切り替える方法は、コマンド・メニュー・設定ファイルの 3 つである。この節は WSL・Linux の CLI を基準にする。VS Code 拡張とデスクトップアプリには別の入口があり、動作は未確認である。

- `/output-style <名前>`：その場で切り替える。引数なしで一覧を出し、今のスタイルに印が付く。名前の大文字小文字は区別されない。新しい版が要る。
- `/config`：メニューの出力スタイルの項目から選ぶ。
- 設定ファイルの `outputStyle`：値を直接書く。大文字小文字を区別するので、`Explanatory` と書く。`explanatory` のように合わない値は、エラーも出ず Default の扱いになる。

コマンドとメニューの選択は、プロジェクトの個人用の設定（`.claude/settings.local.json`）に保存される。全プロジェクトの既定にするなら、`~/.claude/settings.json` に `outputStyle` を書く。プロジェクト側の設定が優先される。

<!-- gen:begin snippet output-style-modes/output-style-setting -->
<!-- textlint-disable -->

??? example "雛形：設定ファイルで出力スタイルを指定する"

    ```json
    {
      "outputStyle": "Explanatory"
    }
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.81。

<!-- textlint-enable -->
<!-- gen:end snippet output-style-modes/output-style-setting -->

途中で切り替えたときは、次のメッセージから新しいスタイルが効く。切り替えるとプロンプトキャッシングの効きに影響するので、頻繁には切り替えず、作業の区切りで選び直す。

## 自作のスタイル {#custom}

自作の出力スタイルは、フロントマター付きの Markdown ファイルである。ユーザー全体なら `~/.claude/output-styles/`、プロジェクトなら `.claude/output-styles/` に置く。ファイル名がスタイルの名前になり、`name` で変えられる。

フロントマターの主なキーは次の 3 つである。

- `name`：メニューに出る名前。省くとファイル名になる。
- `description`：メニューに出る説明。
- `keep-coding-instructions`：`true` にすると、Claude Code が持つソフトウェア開発の指示を残す。省くと外れる。

コードを書く作業のまま口調や形だけ変えたいときは、`keep-coding-instructions: true` を付ける。付けないと、変更の範囲の決め方・コメントの書き方・作業の確かめ方といった組み込みの指示が外れる。Claude にコードを書かせない用途（文章の添削など）のときは、省いてよい。

<!-- gen:begin snippet output-style-modes/custom-style -->
<!-- textlint-disable -->

??? example "雛形：自作の出力スタイルの例（要点先行・日本語）"

    ```markdown
    ---
    name: 要点先行
    description: 結論を先に述べ、日本語で短く答える
    keep-coding-instructions: true
    ---

    応答は日本語で書く。

    最初の 1 文で、結果か答えを述べる。前置き、手順の実況、最後のまとめは省く。

    次のものは短くせず、全文を書く。

    - 依頼された説明や詳細
    - エラーの内容、失敗したテストの出力
    - 破壊的な操作の確認

    コード、コマンド、ファイル名、設定のキーは原文のまま書く。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.81。

<!-- textlint-enable -->
<!-- gen:end snippet output-style-modes/custom-style -->

この例は、結果を先に述べさせ、頼まれた説明とエラーと破壊的な操作の確認は省かせない。短くさせる指示には、短くしてはいけないものを同時に書く。書かないと、エラーの内容まで削られて原因が分からなくなる。

ターミナルの Claude Code は、スタイルのファイルを起動時に読み込む。起動中のセッションでファイルを作ったり直したりしたら、Claude Code を起動し直す。同じ名前のスタイルが複数の階層にあるときは、作業ディレクトリに近いものが使われる。プラグインがスタイルを同梱することもある。

大きな役割の変更でない限り、自作の前に組み込みを試す。組み込みで足りないところだけを、自作で足す。

## 効かない場面・落とし穴 {#limits}

出力スタイルは指示であり、効き目は保証されない。次の場面では効かない、または期待とずれる。

- **必ず起きるべきこと**：編集のたびの整形や、特定のコマンドの禁止には使えない。これらはフックか権限の規則に移す。スタイルに「禁止」と書いても、鍵にはならない。
- **fork でないサブエージェント**：サブエージェントは自分のシステムプロンプトで動くので、スタイルが届かない。fork は親の会話とシステムプロンプトを引き継ぐので届く。届かない所の全体像は <!-- link:begin what-subagents-dont-inherit -->[サブエージェントに引き継がれないもの](../extend/what-subagents-dont-inherit.md)<!-- link:end --> にある。
- **確認ばかりで進まない症状**：Proactive は確認を減らすが、止まる原因が権限モードやモデルの癖にあるなら直らない。原因の切り分けは <!-- link:begin keeps-stopping#diagnosis -->[確認ばかりで進まない・途中で止まる › 原因を安く確かめる順](../symptoms/keeps-stopping.md#diagnosis)<!-- link:end --> にある。
- **頼んでいないことまでやる症状**：Proactive は、範囲を広げる方向にも働きうる。範囲の指定と差分の確かめは <!-- link:begin does-more-than-asked#prevention -->[頼んでいないことまでやる（過剰設計） › 予防：範囲を先に決め、差分を毎回見る](../symptoms/does-more-than-asked.md#prevention)<!-- link:end --> で決める。
- **アプリの Styles**：claude.ai のアプリにある Styles は、Claude Code の出力スタイルとは別の機能である。スキルへの移行が告知されており、設定の場所と効き方が違う。画面にまだメニューが出るかは未確認である。

落とし穴は、スタイルに預けすぎることである。Concise にすると応答が短くなるが、確かめる責任まで軽くなるわけではない。差分とテストの結果は、スタイルにかかわらず自分で読む。Explanatory の説明を読んだだけで、そのコードを理解したことにもしない。Learning でも、書かされた数行を「書いた」ことで理解したことにせず、説明できるかを自分に問う。

トークンの使い方もスタイルで変わる。Explanatory と Learning は設計上、Default より長く答える。Concise は逆に短くする。自作のスタイルは、書いた指示が何を出力させるかに依存する。

## CLAUDE.md・スキルとの分担 {#vs-claude-md}

出力スタイルと CLAUDE.md は、どちらも文脈を足す点が似ているが、足すものが違う。

- **CLAUDE.md**：プロジェクトの規約・コマンド・構造など、Claude が知るべきこと。どのスタイルを選んでも残る。
- **出力スタイル**：応答の長さ・形・口調・役割など、どう答えるか。セッション全体に効き、1 つのコマンドで切り替わる。
- **スキル**：リリース手順やレビュー手順のような、ある種類の作業の指示。呼ばれたときか、作業が合ったときにだけ読み込まれ、関係のない応答には影響しない。
- **フック**：毎回必ず起きるべきこと。Claude Code 自身が実行するので、指示に従うかどうかに頼らない。

分担の考え方は次のとおりである。場面によって切り替えたい応答の形は出力スタイルに置き、プロジェクトの事実は CLAUDE.md に書く。例外を許さないものはフックに移し、スタイルや CLAUDE.md には理由と相談の基準だけを残す。

!!! example "判断例：「テストを先に説明して」をどこに置くか"
    - **状況**：テストを追加する作業のたびに、「何を確かめるテストか」を先に 1 文で言わせたい。ほかの作業では要らない。
    - **迷う候補**：CLAUDE.md に書く。テスト追加用のスキルに書く。自作の出力スタイルに書く。
    - **選んだもの**：テスト追加用のスキルに書く。
    - **理由**：場面が限られた手順なので、呼ばれたときだけ読み込まれるスキルが合う。出力スタイルに書くと、関係のない応答にも効く。CLAUDE.md に書くと、テストと関係のない作業でも毎回読み込まれ、文脈を無駄に使う。

置き場所の選び方は <!-- link:begin claude-md-vs-rules-skills-styles#how-to-choose -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示の置き場所の選び方](../extend/claude-md-vs-rules-skills-styles.md#how-to-choose)<!-- link:end --> に、並べた比較の表は <!-- link:begin claude-md-vs-rules-skills-styles#table -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 比較の表](../extend/claude-md-vs-rules-skills-styles.md#table)<!-- link:end --> にある。最初の CLAUDE.md を作るところは <!-- link:begin init-and-first-claude-md#run-init -->[/init と最初の CLAUDE.md › /init で叩き台を作る](init-and-first-claude-md.md#run-init)<!-- link:end --> から始める。

## 日本語の応答との関係 {#japanese}

出力スタイルは、返答の言語を決める仕組みではない。組み込みのスタイルが返答の言語にどう影響するかは、公式の文書に書かれていない（未確認）。日本語で返させ続ける手段は、言語の設定・CLAUDE.md・スタイル・フックを組み合わせる。全体は <!-- link:begin keep-replies-in-japanese#instructions -->[日本語で返し続けさせる › CLAUDE.md と出力スタイル（お願いの層）](../japanese/keep-replies-in-japanese.md#instructions)<!-- link:end --> にある。

自作のスタイルに「応答は日本語で書く」と書くのは、お願いの層の 1 つである。ほかのお願いと同じく、完全には守られない。fork でないサブエージェントには届かないので、サブエージェントの報告が英語に戻ることは、スタイルでは防げない。

Concise などの組み込みスタイルを日本語の環境で使うときは、応答が日本語のまま保たれるかを、自分の環境で確かめる。確かめ方は、簡単な質問と、英語のツール出力を読んだ後の質問を 1 回ずつ出し、返答の言語を見ればよい。日本語が崩れるなら、自作のスタイルに言語の指示を足す。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Output styles](https://code.claude.com/docs/en/output-styles)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)
- [/init と最初の CLAUDE.md](init-and-first-claude-md.md)
- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- [どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)
- [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- [日本語で返し続けさせる › CLAUDE.md と出力スタイル（お願いの層）](../japanese/keep-replies-in-japanese.md#instructions)
- [サブエージェントに引き継がれないもの](../extend/what-subagents-dont-inherit.md)
- [権限モードの選び方](permission-modes-overview.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
