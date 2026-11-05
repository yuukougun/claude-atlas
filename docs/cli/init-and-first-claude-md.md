---
id: init-and-first-claude-md
title: /init と最初の CLAUDE.md
aliases: [/init, CLAUDE.md を作る, 最初の CLAUDE.md の作り方]
type: feature
field: cli
chapter: 設定と最初の準備
order: 130
level: 整える
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: /init でリポジトリを調べさせて CLAUDE.md の叩き台を作り、読んで削ってから使い始められる。手で一行ずつ書く流儀もあり、どちらで始めても書いた後に削る。
signs:
  - {type: goal, text: 最初の CLAUDE.md を手早く作りたい}
  - {type: situation, text: /init が作った CLAUDE.md を、そのまま使ってよいか迷っている}
prerequisites: [where-instructions-sit]
related: [claude-md-length#init-draft, what-to-put-in-claude-md, when-to-add-what, repeating-the-same-explanation, agents-md, output-style-modes]
tracks: [claude-md]
outdated_advice: [architecture-in-claude-md, hash-to-memorize]
sources: [cc-docs-memory]
volatility: 中
sections:
  - {title: /init で叩き台を作る, anchor: run-init}
  - {title: 叩き台を削ってから使う（削り方は claude-md-length）, anchor: prune}
  - {title: 手で書く流儀との違い, anchor: by-hand}
  - {title: 削った後の例, anchor: example}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：`/init` でリポジトリを調べさせて CLAUDE.md の叩き台を作り、読んで削ってから使い始められる。
    - **強制力**：<!-- gen:begin feature claude-md/enforcement -->お願い<!-- gen:end feature claude-md/enforcement -->。書いた行は文脈として読まれるだけで、行為を止める鍵にはならない。
    - **いつ引くか**：最初の CLAUDE.md を手早く作りたいとき。`/init` が作った CLAUDE.md をそのまま使ってよいか迷うとき。
    - **前提**：<!-- link:begin where-instructions-sit -->[システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)<!-- link:end -->

<!-- textlint-disable -->
別名：/init・CLAUDE.md を作る・最初の CLAUDE.md の作り方
<!-- textlint-enable -->

`/init` は、Claude Code がリポジトリを調べて CLAUDE.md の叩き台を作るコマンドである。叩き台は完成品ではなく、読んで削ってから使う下書きとして扱う。

## /init で叩き台を作る {#run-init}

`/init` は、Claude がコードベースを調べ、見つけたビルドの手順・テストの手順・プロジェクトの慣習を CLAUDE.md にまとめる（[How Claude remembers your project](https://code.claude.com/docs/en/memory)）。CLAUDE.md が既にあるときは、上書きせずに改善案を出す。ほかのツールの指示ファイルがあれば、関係する部分を取り込む。

=== "Claude Code"

    1. 作業したいリポジトリの根で `claude` を起動する。
    2. `/init` を実行し、生成が終わるのを待つ。
    3. できた CLAUDE.md を開いて、全行を読む。この読む作業を飛ばさない。
    4. 読んで分かることを削る（判断は次の節が指す先にある）。残した行のコマンドが実際に動くか確かめる。

公式は、対話的に複数の段階で進める別の流れも案内している。環境変数 `CLAUDE_CODE_NEW_INIT` を `1` にしてから `/init` を実行すると、作るものを選ぶ質問、サブエージェントによる調査、書く前の提案の確認が入る。この別の流れは手元で試していない（未確認）。

CLAUDE.md はセッションの開始で読まれる文脈であり、強制される設定ではない。そのため、`/init` で作った行も、書いただけでは守られる保証がない。位置づけは <!-- link:begin where-instructions-sit#why -->[システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置 › なぜ強制ではなく文脈になるか](../basics/where-instructions-sit.md#why)<!-- link:end --> にある。

## 叩き台を削ってから使う（削り方は claude-md-length） {#prune}

`/init` の叩き台は、「作る → 読んで削る → 使いながら足す」の 3 歩の最初の 1 歩である。削る歩の判断は <!-- link:begin claude-md-length#init-draft -->[CLAUDE.md の長さと剪定 › /init の叩き台を削る](../extend/claude-md-length.md#init-draft)<!-- link:end --> が持つので、ここでは繰り返さない。

流れの要点だけを書く。

- 作る：`/init` を 1 回流す。完成を期待しない。
- 読んで削る：Claude がリポジトリを読めば分かることは削る。残すのは、読んでも分からない約束・理由・落とし穴である。判断の問いは <!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](../extend/claude-md-length.md#deletion-test)<!-- link:end --> にある。
- 使いながら足す：同じ説明を繰り返し始めてから行を足す。最初から作り込まない。足す基準は <!-- link:begin repeating-the-same-explanation#prevention -->[毎回同じ説明をしている › 予防：移した後に削り、足すのは繰り返しが見えてから](../symptoms/repeating-the-same-explanation.md#prevention)<!-- link:end --> と <!-- link:begin when-to-add-what#why -->[拡張を足すタイミング › 繰り返しが見えてから足す理由](../extend/when-to-add-what.md#why)<!-- link:end --> にある。

残す行と外す行の基準そのものは <!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> にある。

!!! example "判断例：/init が作った CLAUDE.md をそのまま使うか"
    - **状況**：初めて `/init` を流したら、ディレクトリの木・使っているフレームワークの説明・コマンドの一覧を含む長い CLAUDE.md ができた。
    - **迷う候補**：手間を省いてそのまま使う。または、読んで推測できる説明を削ってから使う。
    - **選んだもの**：読んで削ってから使う。
    - **理由**：木やフレームワークの説明は、Claude がリポジトリを読めば分かる。残しても行が増えるだけである。コマンドは動くものだけを残し、読んでも分からない落とし穴を足す。

## 手で書く流儀との違い {#by-hand}

`/init` を使うかどうかは、実践者の間で意見が割れる。公式の立場・実践者の幅・この辞典の推奨に分けて書く。

- 公式の立場：`/init` で叩き台を作り、そこから「Claude が自分では見つけられない指示」で磨くという流れを案内している（[How Claude remembers your project](https://code.claude.com/docs/en/memory)）。
- 実践者の幅（叩き台に使う派）：`/init` で叩き台を作り、そこから直す。複数の実践者がこの使い方を勧めている（根拠：弱）。
- 実践者の幅（手で書く派）：CLAUDE.md は全作業に効く重要なファイルなので、1 行ずつよく考えて手で書く。ある実践者の記事は、`/init` や自動生成を避けるよう勧めている（根拠：弱）。別の記事は、自動生成の CLAUDE.md は長くなりやすく、肝心の理由が抜けると述べている（根拠：弱）。
- この辞典の推奨：どちらで始めてもよい。ただし `/init` を使うなら、必ず削って手で直す。手で書く派の懸念は、長さと理由の欠落である。読んで削る歩と、理由を自分で足す歩で、どちらも抑えられる。

手で書く場合も、書いた後に削る点は変わらない。始め方の違いは、最初の下書きを Claude に作らせるか、自分で作るかだけである。

## 削った後の例 {#example}

叩き台を削った後の CLAUDE.md の例を示す。推測できる説明を落とし、コマンドと落とし穴と決まりだけを残している。コマンドと生成物のパスは、自分のリポジトリのものに置き換える。

<!-- gen:begin snippet init-and-first-claude-md/pruned-claude-md -->
<!-- textlint-disable -->

??? example "雛形：/init の叩き台を削った後の CLAUDE.md の例"

    ```markdown
    # 開発の約束

    ## コマンド

    - テスト：`npm test`（単体のファイルだけなら `npm test -- path/to/file.test.ts`）
    - 型検査：`npm run typecheck`。テストの前に通す

    ## 落とし穴

    - `src/generated/` は `npm run codegen` が作る。手で直さない（次の生成で消える）
    - 結合テストは `.env.test` がないと黙って成功扱いになる。新しい環境ではまず `.env.test` の有無を確かめる

    ## 決まり

    - 公開 API の変更は、先に `docs/api-changes.md` へ理由を書く。理由は、後から経緯を追えるようにするため
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet init-and-first-claude-md/pruned-claude-md -->

## 効かない場面と落とし穴 {#limits}

- 削らずに使う：叩き台のまま常駐させると、読んでも分かる説明で行が増える。守らせたい行が埋もれる。
- 理由が抜ける：`/init` は調べて分かる事実を拾うが、「なぜそうするか」は拾えない。理由は自分で足す。
- 禁止を書けば止まると思う：CLAUDE.md の行は文脈であり、強制ではない。例外を許さない禁止は、鍵の仕組みに移し、CLAUDE.md には理由だけを書く。分け方は <!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](../extend/what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end --> にある。
- 一度作って放置する：リポジトリが変わると、叩き台のコマンドが古くなる。動かないコマンドは、書いていないより悪い。
- 他の OS と IDE 拡張：動作は WSL・Linux の CLI を基準に書いている。ほかの OS と IDE 拡張での `/init` の動作は未確認である。

## 比べる相手 {#compare}

- ほかのツールと指示を共有したいとき：AGENTS.md を読ませる方法がある。選び方は <!-- link:begin agents-md -->[AGENTS.md とほかのツールとの共有](../extend/agents-md.md)<!-- link:end --> にある。
- 答え方（説明の多さ・簡潔さ）を変えたいとき：CLAUDE.md ではなく出力スタイルに置く。分担は <!-- link:begin output-style-modes#vs-claude-md -->[出力スタイルで応答の仕方を切り替える › CLAUDE.md・スキルとの分担](output-style-modes.md#vs-claude-md)<!-- link:end --> にある。
- 削った後の運用：長さを保つ判断は <!-- link:begin claude-md-length -->[CLAUDE.md の長さと剪定](../extend/claude-md-length.md)<!-- link:end --> が持つ。

## 古くなった助言 {#outdated}

- 「アーキテクチャやファイル構成を CLAUDE.md に書く」：今は書かない。Claude がリポジトリを自分で読むので、書くのは読んでも分からないことだけにする。台帳は <!-- link:begin outdated-advice-ledger#architecture-in-claude-md -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#architecture-in-claude-md)<!-- link:end --> にある。
- 「入力の先頭に # を付けると CLAUDE.md に記憶される」：この近道は今はない。足したい内容は、Claude に編集を頼む。または `/memory` でファイルを開いて自分で書く。台帳は <!-- link:begin outdated-advice-ledger#hash-to-memorize -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#hash-to-memorize)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)

**関連**

- [CLAUDE.md の長さと剪定 › /init の叩き台を削る](../extend/claude-md-length.md#init-draft)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [拡張を足すタイミング](../extend/when-to-add-what.md)
- [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- [AGENTS.md とほかのツールとの共有](../extend/agents-md.md)
- [出力スタイルで応答の仕方を切り替える](output-style-modes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
