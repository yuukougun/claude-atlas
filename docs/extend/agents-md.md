---
id: agents-md
title: AGENTS.md とほかのツールとの共有
aliases: ['@AGENTS.md', /import, ほかのエージェントの指示ファイル]
type: feature
field: extend
chapter: CLAUDE.md・rules・自動メモリ
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発, チーム]
summary: AGENTS.md を読ませて、ほかのエージェントツールと同じ指示を共有できる。読み込みの設定に任せるか、CLAUDE.md から取り込むかを、Claude だけに向けた指示があるかで選ぶ。
signs:
  - {type: goal, text: ほかのエージェントツールと指示を共有したい}
  - {type: situation, text: チームで Claude Code とほかの AI ツールを併用している}
prerequisites: [claude-md-loading-order]
related: [what-to-put-in-claude-md, share-team-settings, claude-md-length]
tracks: [claude-md]
sources: [cc-docs-memory, cc-docs-commands]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 読み方の選び方, anchor: choose}
  - {title: 最小の使い方, anchor: usage}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：AGENTS.md を Claude Code に読ませ、ほかのエージェントツールと同じ指示を 1 つのファイルで共有できる。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。AGENTS.md の中身も CLAUDE.md と同じく、Claude が読んで従うだけの文脈で、何も止められない。例外を許さない禁止は鍵に移す。
    - **いつ引くか**：ほかのエージェントツールと指示を共有したいとき、チームで Claude Code とほかの AI ツールを併用しているとき。
    - **前提**：<!-- link:begin claude-md-loading-order -->[CLAUDE.md の階層と読み込み順](claude-md-loading-order.md)<!-- link:end -->

<!-- textlint-disable -->
別名：@AGENTS.md・/import・ほかのエージェントの指示ファイル
<!-- textlint-enable -->

AGENTS.md とほかのツールとの共有は、複数のエージェントツールが読む 1 つの指示ファイルを、Claude Code にも読ませる使い方である。選ぶのは 2 つの道で、Claude Code の読み込みの設定に任せるか、CLAUDE.md から `@AGENTS.md` で取り込むかである。決め手は、Claude だけに向けた指示があるかどうかだ。

## 使いどころ {#when}

リポジトリに AGENTS.md があるのに、Claude が読んでいるかが分からない。あるいは、ツールごとに指示ファイルを別々に書いて、内容が食い違っていく。このページが防ぐ原因は「見えていない」である。効かせる原理は「見せる」で、指示ファイルを Claude の文脈に確実に入れることを指す。

引くのは、次のような場面だ。

- チームで Claude Code とほかの AI ツールを併用していて、指示を 1 か所に保ちたい。
- すでに AGENTS.md を整えたリポジトリに、Claude Code を足したい。
- AGENTS.md を置いたのに、Claude がその内容に従わない。

この機能は指示ファイルの読み方を決めるだけで、Claude に任せる幅は広げない。AGENTS.md は CLAUDE.md と同じ「お願い」であり、強制したい禁止は<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->で選ぶ鍵（フックや deny ルール）に置く。

## 読み方の選び方 {#choose}

AGENTS.md を Claude Code に読ませる方法は 2 つある。読み込みの設定（`/config` の設定画面で選ぶ）に任せる方法と、CLAUDE.md に `@AGENTS.md` を書いて取り込む方法である。

読み込みの設定の初期の値は、<!-- fact:begin agents-md-instruction-files-default -->claude-md-or-agents-md（CLAUDE.md を読み、作業ディレクトリかその上に CLAUDE.md・CLAUDE.local.md がないときだけ AGENTS.md を読む）（2026-11-05 時点）<!-- fact:end -->である。この値のときの動きは、次のとおりだ。Claude Code は、作業ディレクトリかその上に CLAUDE.md、`.claude/CLAUDE.md`、`CLAUDE.local.md` のどれもないときだけ、AGENTS.md を読む。1 つでもあれば、CLAUDE.md の系統だけが読まれ、AGENTS.md は読まれない。なお、ホームの `~/.claude/CLAUDE.md`、組織の管理用 CLAUDE.md、`.claude/rules/` のファイルは、この判定に数えない。

選び方は、Claude だけに向けた指示があるかで決まる。

- **Claude だけへの指示がない**：CLAUDE.md を置かない。AGENTS.md がそのまま読まれる。
- **Claude だけへの指示がある**：CLAUDE.md の先頭に `@AGENTS.md` を書き、その下に Claude 向けの指示を足す。共通の指示は AGENTS.md に、Claude だけの指示は CLAUDE.md に分かれる。
- **個人用の `CLAUDE.local.md` も使いたい**：`CLAUDE.local.md` も CLAUDE.md として数えられるので、置くと AGENTS.md が読まれなくなる。対処は 2 つある。読み込みの設定を「CLAUDE.md と AGENTS.md の両方」に変えるか、CLAUDE.md から取り込む。

!!! example "判断例：Claude だけに向けた指示がある"
    - **状況**：チームは Codex 系のツールと Claude Code を併用している。AGENTS.md に共通の規約があり、Claude Code では課金まわりの変更に plan mode を使わせたい。
    - **迷う候補**：AGENTS.md の末尾に Claude 向けの行を足す。または、CLAUDE.md を作って `@AGENTS.md` で取り込み、Claude 向けの行を CLAUDE.md に書く。
    - **選んだもの**：CLAUDE.md を作って取り込む。
    - **理由**：plan mode は Claude Code の機能で、ほかのツールには意味がない。AGENTS.md に書くと、ほかのツールの利用者に無関係な行を読ませる。CLAUDE.md なら共通部分は 1 か所のまま、Claude の行だけを分けられる。

取り込みは、AGENTS.md を CLAUDE.md の一部として文脈に入れる。同じファイルが二重に読まれることはなく、読み込みの設定を「両方」にしても変わらない。ただし、取り込みでコンテキストが減るわけではない。仕組みは<!-- link:begin claude-md-loading-order#import -->[CLAUDE.md の階層と読み込み順 › 取り込みでは減らない](claude-md-loading-order.md#import)<!-- link:end -->にある。

## 最小の使い方 {#usage}

最小の手順は、`@AGENTS.md` の 1 行だけを書いた CLAUDE.md を AGENTS.md の隣に置くことだ。Claude Code は CLAUDE.md を読み、その中の取り込みで AGENTS.md を展開する。

=== "Claude Code"

    1. AGENTS.md と同じ階層に CLAUDE.md を作り、先頭に `@AGENTS.md` を書く。Claude だけへの指示があれば、その下に足す。雛形は下の「雛形」にある。
    2. 新しいセッションを始め、`/context all` を実行する。確かめ：Memory files の一覧に CLAUDE.md が出て、AGENTS.md の内容が文脈に入っている。
    3. CLAUDE.md を置かずに AGENTS.md だけを読ませる場合は、新しいセッションの冒頭に「CLAUDE.md が見つからず AGENTS.md を読み込んだ」旨の 1 行が出る。確かめ：この行が出るか、`/context all` に AGENTS.md が載る。

Claude だけへの指示が要らず、Windows の利用者もいないなら、シンボリックリンクでも足りる。

```bash
ln -s AGENTS.md CLAUDE.md
```

Windows の利用者がいるときは、取り込みを選ぶ。Windows ではシンボリックリンクの作成に管理者権限か開発者モードが要り、リポジトリを取得した側で通常のテキストファイルになることがある。また、Claude の Edit や Write のツールは、リンクを通した書き込みを断り、リンク先の AGENTS.md を直すよう案内する。Windows と IDE 拡張での動作は、この辞典では未確認である。

2 つ目の使い方は、ほかのツールの設定を移すときだ。`/import` は、対応するツールの設定を Claude Code に取り込む。AGENTS.md のような指示ファイルは、対応する CLAUDE.md に 1 回だけ複写される。複写なので、取り込み後に AGENTS.md を直しても CLAUDE.md には反映されない。共有を続けたいなら、`/import` ではなく `@AGENTS.md` の取り込みを使う。`/init` も、ほかのツールの指示ファイルを見つけ、関係する部分を新しい CLAUDE.md に含める。`/init` の使い方は<!-- link:begin init-and-first-claude-md -->[/init と最初の CLAUDE.md](../cli/init-and-first-claude-md.md)<!-- link:end -->を引く。

## 雛形 {#templates}

1 つ目は、AGENTS.md を取り込み、Claude だけへの指示を足す CLAUDE.md である。下の 2 項目は、自分のプロジェクトの規約に書き換える。

<!-- gen:begin snippet agents-md/import-agents-md -->
<!-- textlint-disable -->

??? example "雛形：AGENTS.md を取り込み、Claude だけへの指示を足す CLAUDE.md"

    ```markdown
    @AGENTS.md

    ## Claude Code

    - 課金まわり（`src/billing/`）の変更は、実装の前に plan mode で方針を出す。
    - 変更後は `npm test` を流し、結果を貼ってから完了と報告する。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet agents-md/import-agents-md -->

AGENTS.md を読む組み込みプラグインの ID は、<!-- fact:begin agents-md-plugin-id-rename -->agents-md@builtin から cc-plugin-agents-md@builtin へ。後者の項目を読むのは 2.1.285 以降（前者も同じ版以降は読む）（2026-11-05 時点）<!-- fact:end -->。下の設定の雛形は、新しい ID で書いてある。

2 つ目は、CLAUDE.md と AGENTS.md を両方読ませる設定である。CLAUDE.md を置いたまま、取り込みではなく設定で AGENTS.md も読ませたいときに使う。`/config` の設定画面で同じ値を選んでもよい。

<!-- gen:begin snippet agents-md/read-both-files -->
<!-- textlint-disable -->

??? example "雛形：CLAUDE.md と AGENTS.md を両方読ませる設定"

    ```json
    {
      "pluginConfigs": {
        "cc-plugin-agents-md@builtin": {
          "options": {
            "instructionFiles": "claude-md-and-agents-md"
          }
        }
      }
    }
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet agents-md/read-both-files -->

## 効かない場面と落とし穴 {#limits}

AGENTS.md が読まれない、または読まれ方が CLAUDE.md と違う場面が、次のようにある。

- **CLAUDE.md が 1 つでもある**：初期の設定では、作業ディレクトリかその上に CLAUDE.md か `CLAUDE.local.md` があると AGENTS.md は読まれない。個人用の `CLAUDE.local.md` を足しただけで、それまで読まれていた AGENTS.md が読まれなくなる。確かめ：`/context all` の Memory files に AGENTS.md が載っているかを見る。
- **読み込みの設定が使えないセッション**：読み込みの設定で AGENTS.md を読む機能は、<!-- fact:begin agents-md-direct-read-min-version -->Claude Code 2.1.277 以降（2026-11-05 時点）<!-- fact:end -->のものである。それより前の版、組み込みのプラグインを無効にした環境、アップグレード直後の最初のセッションなどでは、CLAUDE.md だけが読まれ、`/config` に読み込みの設定の欄が出ない。クラウドの基盤や、利用状況の送信を止めた環境で読まれない版もあった。こうした環境でも共有するには、CLAUDE.md から取り込む。
- **フックと追加ディレクトリで差が出る**：読み込みの設定で読まれた AGENTS.md は、`InstructionsLoaded` フックを呼ばない。取り込まれた AGENTS.md は呼ぶ。`--add-dir` で足したディレクトリの AGENTS.md も、読み込みの設定では読まれない。
- **サブエージェントの扱い**：プロジェクトの指示を持たずに始まるサブエージェントは、AGENTS.md も持たずに始まる。
- **シンボリックリンクの書き込み**：リンクにした CLAUDE.md には、Claude が直接書き込めない。直すときはリンク先の AGENTS.md を直す。
- **指示の強制ではない**：AGENTS.md は CLAUDE.md と同じ文脈であり、書いても止められない。行の増えすぎは<!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](claude-md-length.md#deletion-test)<!-- link:end -->で見直す。

読み込みの設定には、ほかに「CLAUDE.md だけ」と「組織の管理用の指示だけ」の値もある。値の一覧は公式の文書で確かめる。モノレポの階層と読み込み順は、前提のページにある。

## 比べる相手 {#compare}

AGENTS.md を Claude に見せる方法は 4 つある。どれも、同じファイルを複数のツールで使うか、いったん複写するかの違いである。

| 方法 | 向く場面 | 注意 |
| --- | --- | --- |
| 読み込みの設定に任せる（CLAUDE.md を置かない） | Claude だけへの指示がない | CLAUDE.md か `CLAUDE.local.md` を足すと読まれなくなる |
| CLAUDE.md から `@AGENTS.md` で取り込む | Claude だけへの指示がある。設定が使えない環境もある | 取り込みでコンテキストは減らない |
| シンボリックリンク | Claude だけへの指示がなく、Windows の利用者もいない | Claude はリンク越しに書けない。Windows では壊れやすい |
| `/import` で複写する | ほかのツールから Claude Code へ移るとき | 1 回だけの複写で、その後は共有されない |

チーム全体への設定の入れ方は<!-- link:begin share-team-settings#shared-vs-personal -->[チームで設定を共有する › 共有するものと個人に残すもの](../team/share-team-settings.md#shared-vs-personal)<!-- link:end -->にある。CLAUDE.md に何を残し、何を AGENTS.md に移すかは<!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end -->で決める。

## 古くなった助言 {#outdated}

Claude が AGENTS.md を直接読めなかった時期に、次の回避策が広まった。直接読める環境では、不要になるか、逆効果になる。

- **CLAUDE.md に「AGENTS.md を読め」と文で書く**：Claude が自分でファイルを開くと決めたときだけ読まれる。CLAUDE.md を消して直接読ませるか、取り込みの `@AGENTS.md` へ書き換える。
- **`@AGENTS.md` だけの CLAUDE.md**：そのままでよい。二重には読まれない。ほかに何も書かないなら消してよい。ただし、読み込みの設定が使えない環境があるなら残す。
- **シンボリックリンクの CLAUDE.md**：そのままでも、消してもよい。内容は 1 回しか読まれない。
- **AGENTS.md を出力する `SessionStart` フック**：外す。直接読まれるようになると、同じ内容が文脈に 2 回入る。

読み込みの設定で AGENTS.md を直接読めるのは、<!-- fact:begin agents-md-direct-read-min-version -->Claude Code 2.1.277 以降（2026-11-05 時点）<!-- fact:end -->である。自分の環境の版で、`/context all` を使って確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [CLAUDE.md の階層と読み込み順](claude-md-loading-order.md)

**関連**

- [CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)
- [チームで設定を共有する](../team/share-team-settings.md)
- [CLAUDE.md の長さと剪定](claude-md-length.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
