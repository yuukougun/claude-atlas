---
id: protected-paths
title: 消せない場所・触れない場所（protected paths）
aliases: [protected paths, 保護されたパス, critical paths, 作業ディレクトリの外への書き込み]
type: feature
field: enforce
chapter: 権限と封じ込め
order: 70
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: どの権限モードでも確認なしには書かせない場所と、消させない場所を知り、足りない境界を設定で足せる。作業ディレクトリの外への書き込みを道具の側で止める設定もある。
signs:
  - {type: symptom, text: '.claude や .git を書き換えるたびに確認が出る'}
  - {type: goal, text: 作業ディレクトリの外のファイルは書き換えさせたくない}
prerequisites: [permission-rules]
related: [destructive-commands, permission-modes-overview, sandboxing, what-auto-mode-stops, deleted-something-important, before-opening-unknown-repos, freeze-eval-assets]
tracks: [permissions, permission-modes]
sources: [cc-docs-permissions, cc-docs-permission-modes, cc-docs-settings-reference, cc-changelog]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 保護される場所と、モードごとの扱い, anchor: protected}
  - {title: どのモードでも止まる削除, anchor: critical-rm}
  - {title: 作業ディレクトリの外への読み書きを閉じる, anchor: outside-working-directory}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：どのモードでも確認なしには書かせない場所と、消させない場所が分かり、作業ディレクトリの外への書き込みは設定で閉じられる
    - **いつ引くか**：`.claude` や `.git` を書き換えるたびに確認が出るとき。作業ディレクトリの外のファイルは書き換えさせたくないとき
    - **強制力**：<!-- gen:begin feature enforcement -->鍵<!-- gen:end feature enforcement -->。保護された場所は、モードによっては止まらない。外を閉じる設定が止めるのは、ファイルの道具だけ
    - **前提**：<!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](permission-rules.md)<!-- link:end -->

<!-- textlint-disable -->
別名：protected paths・保護されたパス・critical paths・作業ディレクトリの外への書き込み
<!-- textlint-enable -->

Claude Code には、allow ルールを書いても事前承認されない場所と、どのルールでも通せない削除の対象が、あらかじめ決まっている。このページは、その場所と削除の対象、モードごとの扱い、足りない境界を設定で足す方法を扱う。

## 使いどころ {#when}

任せる幅を広げる前に、何が既に守られていて、何が守られていないかを知るために引く。このページが防ぐのは、原因の「境界がない」である。原理は「縛る」で、お願いではなく Claude Code が止める。

- `.claude` や `.git` を書き換えるたびに確認が出る。不具合ではなく保護された場所の動きで、allow ルールを足しても消えない。理由と例外は「保護される場所と、モードごとの扱い」の節にある
- acceptEdits や auto モードで任せ始めた。確認なしで書ける範囲と残る範囲を先に知る。モードごとの全体は <!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](../cli/permission-modes-overview.md#modes)<!-- link:end --> にある
- 作業ディレクトリの外のファイルは書き換えさせたくない。保護された場所の一覧には入らないので、設定で足す。足し方は「作業ディレクトリの外への読み書きを閉じる」の節にある
- 消したくないものがある。取り返しのつかない削除の全体は <!-- link:begin destructive-commands#how-it-happens -->[消されたくないもの（破壊的コマンド） › 消える経路](../safety/destructive-commands.md#how-it-happens)<!-- link:end --> にある。このページが扱うのは、そのうち `rm` と `rmdir` が止まる対象である

任せる幅を広げるなら、守りを先に置く。権限ルールは <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](permission-rules.md#evaluation-order)<!-- link:end -->、シェルの先まで囲うなら <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](sandboxing.md#scope)<!-- link:end --> を先に決める。このページの機能は、その上に重ねる層である。

## 保護される場所と、モードごとの扱い {#protected}

保護された場所とは、書き込みが事前承認されない、Claude Code が決めた場所の集まりである。目的は、リポジトリの状態と、Claude 自身の設定が、うっかり壊れるのを避けることにある。確認が出る理由は、安全の確認がモードより先に働くからで、公式はこの確認が allow ルールの評価より前に走ると書く。

代表的な場所は次のとおり。一覧は版で増えるので、全部は公式で確かめる。

- ディレクトリ：`.git`・`.vscode`・`.idea`・`.husky`・`.devcontainer`・`.claude` など。`.claude` には例外があり、Claude の git worktree、そのセッションの計画のファイル、メモリのファイルなどは含まれない
- ファイル：`.gitconfig`・`.bashrc`・`.zshrc`・`.profile` などのシェルや git の設定、`.npmrc` などのパッケージの設定、`.mcp.json`・`.claude.json` などの Claude と MCP の設定
- `--settings`・`--mcp-config`・`--agents` で渡したファイルも含まれる

フックのスクリプトも、`.claude/hooks/` に置けば同じ保護がかかる。つまり、縛りの設定そのものを、Claude が黙って書き換えにくくなる。

モードごとの扱いは次のとおり。`default` モードの今の呼び方は <!-- name:begin default-to-manual-mode -->Manual（権限モード。設定の値は default のまま）<!-- name:end --> である。

| モード | 保護された場所への書き込み |
| --- | --- |
| `default` | 確認が出る |
| `acceptEdits` | 確認が出る |
| `auto` | 分類器が判断する |
| `dontAsk` | 拒否される |
| `bypassPermissions` | 許可される |

`plan` は、対話の端末で bypass が使える状態なら許可され、そうでなければ分類器か確認に回る。ほかのモードの全体は <!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](../cli/permission-modes-overview.md#modes)<!-- link:end --> を見る。

この表から分かる境界は 2 つある。

- 確認が出るのは `default` と `acceptEdits` だけである。ここでは、人が見ていることが前提になる。見ていない運用では確認が溜まって通される（承認疲れ）。保護された場所は、鍵ではなく確認にとどまる
- 止まるのは `dontAsk` の拒否だけである。`auto` では分類器の判断、`bypassPermissions` では許可になる。縛りの設定ファイルを確実に守りたいなら、deny ルールで足す

!!! example "判断例：`.claude` の確認を allow ルールで消したい"
    - **状況**：acceptEdits で作業している。Claude が `.claude` の下のファイルを書くたびに確認が出て、手が止まる。
    - **迷う候補**：`Edit(.claude/**)` の allow ルールを足して確認を消す。確認を残したまま、書く場面を減らす。
    - **選んだもの**：確認を残す。
    - **理由**：allow ルールは保護された場所の確認を消さないので、足しても効かない。消せたとしても、縛りの設定が見えないうちに書き換わる経路を開けることになる。確認の数が問題なら、書いてほしい場所を `.claude` の外へ移す。

## どのモードでも止まる削除 {#critical-rm}

重要な場所への `rm` と `rmdir` は、どのルールでも通せない。公式はこの対象を critical paths と呼ぶ。allow ルールでも、allow を返すフックでも、承認できない。deny ルールは、これまでどおり止める。

Claude Code が重要な場所と見分ける対象は、代表的には次のとおり。

- ファイルシステムのルートと、`/usr` や `/etc` のような最上位のディレクトリ
- 自分のホームディレクトリと、Windows のドライブのルート
- 作業ディレクトリと、その親
- 追加した作業ディレクトリの下に対する glob
- 値が空になりうる変数が付いた形：`rm -rf "$DIR"/*` や `rm -rf "$(pwd)"` など

変数が付いた形が入っているのは、変数が空のまま展開されて、意図しない広い範囲を消す事故を防ぐためである。

モードとの関係は、次の 2 点だけを押さえる。

- acceptEdits は、作業ディレクトリの中の `rm` を確認なしに通すが、見分けた重要な場所への削除には確認が出る
- auto モードの分類器は、既定では、見分けた重要な場所への `rm` と `rmdir` を審査の対象にしない。この節の検査が先に働くからである

見分けられない形は、特別扱いされない。公式は、この検査が見逃した命令には特別な扱いがないと書く。たとえばスクリプトの中で消すもの、子プロセスが消すものは、この仕組みの外にある。完全に守りたいなら、サンドボックスで囲い、消されたくないものは別のコピーに置く。消されたときの戻し方は <!-- link:begin deleted-something-important#recover -->[消してはいけないものを消された › まず戻す（復旧の手順）](../symptoms/deleted-something-important.md#recover)<!-- link:end --> にある。

## 作業ディレクトリの外への読み書きを閉じる {#outside-working-directory}

保護された場所の一覧は、作業ディレクトリの外のファイルを守らない。外のファイルを守るには、設定のキー `permissions.blockWritesOutsideWorkingDirectories` を true にする。Write・Edit・NotebookEdit が、どの権限モードでも、作業ディレクトリの外のパスを拒否するようになる。bypassPermissions でも拒否される。読み取り側には `permissions.blockReadsOutsideWorkingDirectories` があり、ファイルの道具の読み取りを同じように閉じる。

=== "Claude Code"

    設定ファイルの `permissions` に、書き込み側のキーを true にして置く。どの設定ファイルに書いても効く。リポジトリが自分の設定に書くことはできるが、利用者の設定を外すことはできない。キーが入ったのは比較的新しい版なので、手元の版が古いと効かない。手元の版で使えるかは、公式の変更履歴で確かめる。置き方の例は「雛形」の節にある。

    作業ディレクトリの外に置いたコードを、Claude に直させたい場面では、このキーを入れると書けなくなる。直させたい場所は、作業ディレクトリに加える。

    入れると、EnterWorktree と ExitWorktree の道具が使えなくなる。worktree を使う作業と同時には入れられない。

このキーが縛るのは、ファイルの道具の 3 つだけである。シェルのコマンド、MCP の道具、フックが動かすプログラムは縛らない。公式は、シェルの書き込みの範囲を絞るには、サンドボックスを使うよう勧める。同じ限界は、権限ルールの deny にもある。ルール側の限界は <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](permission-rules.md#child-processes)<!-- link:end --> にある。つまり、外への書き込みをほぼ確実に止めたいなら、このキーでファイルの道具を閉じ、サンドボックスでシェルを囲う。囲い方は <!-- link:begin sandboxing#minimal -->[サンドボックスで封じ込める › 最小の使い方](sandboxing.md#minimal)<!-- link:end --> にある。

!!! example "判断例：隣のプロジェクトを書き換えさせたくない"
    - **状況**：auto モードで任せている。同じ親ディレクトリの下に、別のプロジェクトがある。Claude が、そちらを書き換えないようにしたい。
    - **迷う候補**：隣のプロジェクトのパスへの deny ルールを書く。`blockWritesOutsideWorkingDirectories` を true にする。
    - **選んだもの**：キーを true にし、シェルはサンドボックスで囲う。
    - **理由**：deny ルールは、パスの書き方を 1 つずつ足す。隣のプロジェクトが増えると、書き漏らす。キーは、作業ディレクトリの外を丸ごと閉じるので、書き漏らしがない。ただしシェルは縛らないので、サンドボックスが要る。

## 雛形 {#templates}

作業ディレクトリの外への書き込みと読み取りを、ファイルの道具の側で閉じる設定の例である。自分の環境で確かめてから使う。

<!-- gen:begin snippet protected-paths/block-writes-outside -->
<!-- textlint-disable -->

??? example "雛形：作業ディレクトリの外への書き込みと読み取りを、道具の側で閉じる設定"

    ```json
    {
      "permissions": {
        "blockWritesOutsideWorkingDirectories": true,
        "blockReadsOutsideWorkingDirectories": true
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet protected-paths/block-writes-outside -->

この設定は、シェル・MCP・フックを縛らない。サンドボックスとの組み合わせは <!-- link:begin sandboxing#templates -->[サンドボックスで封じ込める › 雛形](sandboxing.md#templates)<!-- link:end --> にある。

## 効かない場面・落とし穴 {#pitfalls}

- 保護された場所は、鍵ではなく確認である。`auto` では分類器の判断に、`bypassPermissions` では許可になる。縛りの設定を確実に守るには、deny ルールを足す
- allow ルールは、保護された場所の確認を消さない。`Edit(.claude/**)` を書いても、結果は変わらない
- 一覧にない場所は保護されない。たとえば自分で作った `secrets/` や、`.env` は一覧の保護の対象ではない。守りたい場所は、deny ルールかサンドボックスで足す。秘密の守り方は、別のページが扱う
- 外への書き込みを閉じるキーは、シェルを縛らない。`cp` や `echo` のリダイレクトで、外のファイルは書き換わる。サンドボックスと併用する
- 外を閉じると、EnterWorktree と ExitWorktree が使えなくなる。worktree を使う運用とは両立しない
- 重要な場所への削除を止める検査は、見逃す形がある。スクリプトの中の削除や、子プロセスの削除は、検査の外にある
- 評価の順番と、当たらないパスのルールの落とし穴は <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](permission-rules.md#path-rules)<!-- link:end --> にある。auto モードの分類器がすり抜けさせうるものは <!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](what-auto-mode-stops.md#limits)<!-- link:end --> にある

## 比べる相手 {#compare}

守りたい対象に合わせて、手段を選ぶ。

| 手段 | 止めるもの | 止められないもの |
| --- | --- | --- |
| 保護された場所と重要な場所（このページ） | 決まった場所への書き込みの事前承認と、決まった対象への `rm` | 一覧にない場所。分類器や bypass での書き込み |
| 外への書き込みを閉じるキー | ファイルの道具の、作業ディレクトリの外への書き込みと読み取り | シェル・MCP・フック |
| deny ルール | 指定したパスへの、ファイルの道具の呼び出し | 当たらないパスの書き方。子プロセス |
| サンドボックス | シェルのコマンドと子プロセスの、ファイルと通信 | ファイルの道具・フック・ローカルの MCP サーバー |

どの手段も、単独では穴がある。ファイルの道具は deny ルールか外を閉じるキーで、シェルはサンドボックスで止め、層を重ねる。

deny ルールの書き方は <!-- link:begin permission-rules#minimal -->[権限ルール（allow・ask・deny） › 最小の使い方](permission-rules.md#minimal)<!-- link:end -->、サンドボックスは <!-- link:begin sandboxing#compare -->[サンドボックスで封じ込める › 比べる相手](sandboxing.md#compare)<!-- link:end -->、評価資産を凍結する組み方は <!-- link:begin freeze-eval-assets#how-to-freeze -->[評価資産を凍結し、触れる範囲を絞る › 設定で止める（権限ルール・サンドボックス・ファイルの権限）](freeze-eval-assets.md#how-to-freeze)<!-- link:end --> にある。知らないリポジトリを開く前に見るものは <!-- link:begin before-opening-unknown-repos#guards -->[知らないリポジトリを開く前に › 先に整える守り](../safety/before-opening-unknown-repos.md#guards)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [権限ルール（allow・ask・deny）](permission-rules.md)

**関連**

- [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- [権限モードの選び方](../cli/permission-modes-overview.md)
- [サンドボックスで封じ込める](sandboxing.md)
- [auto モードは何を止め、何を止めないか](what-auto-mode-stops.md)
- [消してはいけないものを消された](../symptoms/deleted-something-important.md)
- [知らないリポジトリを開く前に](../safety/before-opening-unknown-repos.md)
- [評価資産を凍結し、触れる範囲を絞る](freeze-eval-assets.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
