---
id: before-opening-unknown-repos
title: 知らないリポジトリを開く前に
aliases: [clone したリポジトリの確認, workspace trust, 信頼のダイアログ, 設定ファイルもコードとして扱う]
type: recipe
field: safety
chapter: 悪意ある入力
order: 110
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 知らないリポジトリを Claude Code で開く前に、設定・フック・MCP の定義など、開くだけで動きうるものを確かめられる。信頼の確認が出ない非対話の実行は、隔離した環境で動かす。
signs:
  - {type: goal, text: 知らない人のリポジトリを開きたい}
  - {type: situation, text: 配られたコードや README の手順を、Claude に実行させたい}
prerequisites: [prompt-injection-in-practice, permission-rules]
related: [vetting-extensions, writing-safe-hooks, hooks-basics, sandboxing, where-bypass-is-ok, protecting-secrets, explore-a-codebase, headless-basics, cloud-sessions-and-teleport]
tracks: [settings, hooks, mcp]
sources: [cc-docs-security, cc-docs-permissions, cc-docs-settings, cc-docs-headless, cc-docs-mcp, checkpoint-rce-api-token-exfiltration-through]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 開く前に見るファイル, anchor: files-to-check}
  - {title: 信頼の前と後で効くもの, anchor: trust}
  - {title: 非対話の実行では確認が出ない, anchor: headless}
  - {title: 隔離して動かす, anchor: isolate}
  - {title: 手順, anchor: steps}
  - {title: 確かめ方, anchor: verify}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：知らないリポジトリを Claude Code で開く前に、設定・フック・MCP の定義など、開くだけで動きうるものを確かめられる。
    - **いつ引くか**：知らない人のリポジトリを開きたいとき。配られたコードや README の手順を、Claude に実行させたいとき。
    - **前提**：<!-- link:begin prompt-injection-in-practice -->[プロンプトインジェクションの実際](prompt-injection-in-practice.md)<!-- link:end -->・<!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end -->

<!-- textlint-disable -->
別名：clone したリポジトリの確認・workspace trust・信頼のダイアログ・設定ファイルもコードとして扱う
<!-- textlint-enable -->

知らないリポジトリの `.claude/` や `.mcp.json` は、Claude が読む文章であるだけでなく、開いた人の権限で動きうるコードでもある。このレシピは、設定ファイルをコードとして扱い、中身を読んでから開く手順をまとめる。信頼の確認が出ない非対話の実行は、隔離した環境で動かす。

## 先に整える守り {#guards}

開く前に、手元の側で次の 3 つを整える。リポジトリの側は、読むまで信用できない。

1. **最新版で開く**。clone しただけで成り立つ攻撃が Check Point Research から報告され、公表の時点で、報告された問題はすべて修正済みだった（2026 年 2 月に公表。根拠：中）。報告の内容は 3 種類で、設定のフックの実行と、MCP サーバーの自動承認と、接続先の付け替えによる API キーの送出である。後の 2 つは信頼の確認より前に起きた。更新してから開く。
2. **自分の側の deny を先に置く**。プロジェクトの `permissions.allow` は信頼の後でだけ使われる。deny と ask は信頼と関係なく効く。秘密を読ませない deny の作り方は <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](protecting-secrets.md#two-layers)<!-- link:end --> にある。評価の順は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end --> を見る。
3. **隔離できる場所を用意する**。説明できない設定が見つかったときに、移る先を先に決めておく。条件は <!-- link:begin where-bypass-is-ok#requirements -->[bypassPermissions と無人の実行はどこで動かすか › 使い捨ての環境の条件](where-bypass-is-ok.md#requirements)<!-- link:end --> にある。

## 開く前に見るファイル {#files-to-check}

開く前に、Claude Code を起動せずに、次のファイルを読む。設定ファイルの変更は、ソースコードの変更と同じ厳しさでレビューする。Check Point Research の推奨も同じ内容である。

| 場所 | 見るもの | なぜ見るか |
| --- | --- | --- |
| `.claude/settings.json` | `hooks`・`env`・コマンドを呼ぶ設定・`enableAllProjectMcpServers` | フックはシェルのコマンドを実行する。`env` は接続先を変えられる |
| `.mcp.json` | 各サーバーの起動コマンドと接続先 | サーバーは自分のマシンで動くプロセスで、道具の説明は Claude が読む |
| `.claude/` の下のスキルとサブエージェント | フックと許可する道具の指定 | 非対話の実行では、プロジェクトのスキルのフックと許可する道具の指定が使われる |
| `.vscode/` | 設定とタスク | Check Point Research の推奨が、`.claude/` と並べて挙げている。Claude Code 以外の動作は未確認である |
| `CLAUDE.md`・README | Claude への指示と、実行させたいコマンド | 実行させる前に、自分で読む |

フックが何をするかの考え方は <!-- link:begin hooks-basics#locations -->[フックの考え方とイベント › 置き場所と効く範囲（サブエージェントと信頼の確認）](../enforce/hooks-basics.md#locations)<!-- link:end --> に、他人のフックを使う前の見方は <!-- link:begin writing-safe-hooks#runs-as-you -->[フックを安全に書く › フックは利用者の権限で動く](../enforce/writing-safe-hooks.md#runs-as-you)<!-- link:end --> にある。MCP サーバーとプラグインの確かめ方は、このページでは繰り返さず <!-- link:begin vetting-extensions#read-contents -->[MCP・プラグイン・スキルを入れる前の確認 › 中身を読む（道具の説明・フック・スクリプト）](vetting-extensions.md#read-contents)<!-- link:end --> に任せる。

一覧と確認表は、次の雛形を使う。一覧のスクリプトは読むだけで、何も実行しない。

<!-- gen:begin snippet before-opening-unknown-repos/list-auto-run-files -->
<!-- textlint-disable -->

??? example "雛形：開くだけで動きうる設定を探す一覧"

    ```bash
    #!/usr/bin/env bash
    # clone したリポジトリで、開くだけで動きうる設定を探す。読むだけで、何も実行せず、書き換えない。
    # 使い方：bash list-auto-run-files.sh <clone したディレクトリ>
    # Claude Code は起動しない。出力は、自分の目で読む。
    set -u

    cd "${1:?clone したディレクトリを渡す}" || exit 1

    echo "== 設定・MCP・エディタの設定のファイル =="
    find . -path ./.git -prune -o \
      \( -path './.claude/*' -o -name '.mcp.json' -o -path './.vscode/*' \
         -o -name 'CLAUDE.md' -o -name 'CLAUDE.local.md' \) -type f -print 2>/dev/null

    echo
    echo "== 自動で動きうるキー（フック・環境変数・MCP・コマンドを呼ぶ設定）=="
    grep -rnE 'hooks|"env"|enableAllProjectMcpServers|ANTHROPIC_BASE_URL|mcpServers|[Hh]elper|"command"' \
      .claude .mcp.json .vscode 2>/dev/null || true
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet before-opening-unknown-repos/list-auto-run-files -->

<!-- gen:begin snippet before-opening-unknown-repos/open-checklist -->
<!-- textlint-disable -->

???+ example "雛形：知らないリポジトリを開く前の確認表"

    ```markdown
    # 知らないリポジトリを開く前の確認表

    リポジトリ：＿＿＿＿＿＿（clone した元の URL と、誰から渡されたか）
    開く場所：＿＿＿＿＿＿（手元・使い捨てのコンテナや VM・クラウドのセッションのどれか）

    ## 出所

    - [ ] 渡してくれた人と clone した元の URL は、自分で確かめられる
    - [ ] Claude Code は最新版で、更新してから開く

    ## 開くだけで動きうるもの（Claude Code を起動する前に読む）

    - [ ] `.claude/settings.json` に `hooks` がある。ある場合は、走るコマンドを 1 つずつ読んで説明できる
    - [ ] `.claude/settings.json` に `env` や、コマンドを呼ぶ設定がある。ある場合は、接続先と呼ぶコマンドを説明できる
    - [ ] `.claude/settings.json` に `enableAllProjectMcpServers` がある。ある場合は、理由を説明できる
    - [ ] `.mcp.json` がある。ある場合は、各サーバーの起動コマンドと接続先を説明できる
    - [ ] `.claude/` の下のスキルやサブエージェントの定義に、フックや許可する道具の指定がある。ある場合は、中身を読んだ
    - [ ] `.vscode/` の設定とタスクを読んだ

    ## 読み込まれる指示

    - [ ] `CLAUDE.md` と README に、Claude への指示や実行させたいコマンドがある。ある場合は、自分で読んで、実行してよいと判断した

    ## 開き方

    - [ ] 説明できないものが 1 つでもあれば、手元では開かず、隔離した環境で開く
    - [ ] `claude -p` は、読み終えたものか、隔離した環境のものにだけ使う
    - [ ] 信頼の確認が出たら、読み終えたフォルダだけ受け入れる
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet before-opening-unknown-repos/open-checklist -->

## 信頼の前と後で効くもの {#trust}

対話のセッションでは、初めて開くフォルダに、信頼の確認（workspace trust のダイアログ）が出る。受け入れる前と後で、効くものが違う。

- **受け入れるまで走らない**：どの設定ファイルのフックも走らない。自分の `~/.claude/settings.json` のフックも含む。
- **受け入れた後に使われる**：プロジェクトの `permissions.allow` と `additionalDirectories`。
- **受け入れと関係なく効く**：deny と ask。
- **別の承認が要る**：`.mcp.json` のサーバー。

確認を受け入れるとは、そのフォルダの設定ファイルのフックを走らせてよいと答えることである。読み終えたフォルダだけ受け入れる。仕組みの詳細は <!-- link:begin permission-rules#workspace-trust -->[権限ルール（allow・ask・deny） › 信頼の前に効くもの・後に効くもの](../enforce/permission-rules.md#workspace-trust)<!-- link:end --> にある。

過去には、この順序が守られなかった報告がある。修正は、フックが 2025 年 8 月、MCP サーバーの自動承認が 2025 年 9 月、接続先の付け替えが 2025 年 12 月だった（根拠：中）。確認が出るとしても、古い版で開いてよいことにはならない。

## 非対話の実行では確認が出ない {#headless}

`claude -p` は、信頼の確認を出さない。標準出力が端末でないときも同じである。確認の代わりに、次のものが承認なしに使われる。

- **使われる**：設定ファイルのフック・`env`・コマンドを呼ぶ設定。プロジェクトのスキルのフックと許可する道具の指定。`.mcp.json` のサーバー（承認なしでつながる）。
- **使われない**：プロジェクトの `permissions.allow` と `additionalDirectories`（標準エラーに警告が出る）。プロジェクトのサブエージェントの先頭部のフック。

つまり、`-p` は「確認なしで信頼した」状態で動く。対話なら止まる場面が、止まらない。外から来たブランチをそのまま checkout して `claude -p` を走らせる構成では、そのブランチの設定が確認なしに動く。知らないフォルダで動かす条件は <!-- link:begin headless-basics#untrusted-folders -->[非対話モード（claude -p）の基本 › 知らないフォルダで動かすとき](../delegate/headless-basics.md#untrusted-folders)<!-- link:end --> に、許可の渡し方は <!-- link:begin headless-basics#permissions -->[非対話モード（claude -p）の基本 › 許可と権限モード](../delegate/headless-basics.md#permissions)<!-- link:end --> にある。

## 隔離して動かす {#isolate}

読んでも説明できないものが残るとき、読みきれないほど大きいとき、配られたコードや README の手順を動かすときは、手元で動かさない。公式の Security は、信頼できない content について、スクリプトや tool 呼び出しを VM で動かすことを勧めている。コンテナ・VM・クラウドのセッションのどれかを使う。

- **条件を確かめる**：使い捨てで、手元の認証情報を持ち込まない環境にする。条件の一覧は <!-- link:begin where-bypass-is-ok#requirements -->[bypassPermissions と無人の実行はどこで動かすか › 使い捨ての環境の条件](where-bypass-is-ok.md#requirements)<!-- link:end --> にある。
- **書き込みの制限は代わりにならない**：書き込みを作業ディレクトリに閉じても、隔離の代わりにはならない。理由は <!-- link:begin where-bypass-is-ok#not-a-substitute -->[bypassPermissions と無人の実行はどこで動かすか › 書き込みを作業ディレクトリに閉じても代わりにならない](where-bypass-is-ok.md#not-a-substitute)<!-- link:end --> を見る。
- **サンドボックスとの使い分け**：サンドボックスの対象は Claude が動かすコマンドである。フックや MCP サーバーまで含むかは、<!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> で確かめる。コンテナとの使い分けは <!-- link:begin sandboxing#containers -->[サンドボックスで封じ込める › コンテナ（Docker・devcontainer）との使い分け](../enforce/sandboxing.md#containers)<!-- link:end --> にある。
- **クラウドに送る**：送ってよい作業の見分けは <!-- link:begin cloud-sessions-and-teleport#what-to-send -->クラウドセッションと teleport › クラウドに送ってよい作業（準備中）<!-- link:end --> に、手元の設定との違いは <!-- link:begin cloud-sessions-and-teleport#settings -->クラウドセッションと teleport › 手元の設定との違い（準備中）<!-- link:end --> にある。

## 手順 {#steps}

各段の最後に、何で終わったかの確かめを置く。

1. **渡してくれた人と元の URL を確かめる**。clone しただけで Claude Code は起動しない。確かめ：出所を 1 行で言える。
2. **ファイルを読む**。「開く前に見るファイル」の節の一覧のスクリプトと確認表で、`.claude/`・`.mcp.json`・`.vscode/` を読む。確かめ：フック・`env`・MCP サーバーのどれについても、何をするかを説明できる。
3. **開く場所を決める**。すべて説明できて、読むだけの作業なら、手元の対話で開いてよい。説明できないものが 1 つでもあるとき、配られたコードや README の手順を動かすときは、隔離した環境に移す。確かめ：隔離する場合は、その環境から手元のホームと認証情報が見えない。
4. **開く**。対話なら、信頼の確認は読み終えたフォルダだけ受け入れる。確かめ：起動後に動いているフックと MCP サーバーが、手順 2 で読んだものと一致する。
5. **`claude -p` は、読み終えたものか、隔離した環境のものにだけ使う**。確かめ：`-p` を走らせる場所が、手順 2 で読み終えたフォルダか、手順 3 で決めた隔離した環境である。
6. **README の手順は、Claude に任せる前に自分で読む**。提案されたコマンドは、承認の前に確かめる。信頼できない content を、Claude に直接パイプしない。確かめ：実行するコマンドを自分の言葉で説明できる。README から指示が入る経路は <!-- link:begin prompt-injection-in-practice#channels -->[プロンプトインジェクションの実際 › 指示が入ってくる経路](prompt-injection-in-practice.md#channels)<!-- link:end --> を見る。

!!! example "判断例：OSS のリポジトリでビルドの不具合を調べる"
    - **状況**：初めて見る OSS のリポジトリを clone した。README のとおりにビルドして、不具合の原因を Claude に調べさせたい。
    - **迷う候補**：手元でそのまま開く。隔離した環境で開く。
    - **選んだもの**：手順 2 で `.claude/` と `.mcp.json` がないことを確かめたうえで、読むだけの調査は手元の対話で行う。README のビルド手順の実行は、使い捨てのコンテナで行う。
    - **理由**：設定ファイルがなければ、開くだけで動くものは見当たらない。ただし、README のコマンドと依存の取得は、リポジトリの外のものを動かす。こちらは設定ファイルの確認では防げないので、隔離する。

## 確かめ方 {#verify}

信頼の前後の挙動は、無害なフックで確かめられる。隔離した環境の空のフォルダに、次の設定を `.claude/settings.json` として置く。フックは、フォルダに空のファイルを 1 つ作るだけである。

<!-- gen:begin snippet before-opening-unknown-repos/trust-probe -->
<!-- textlint-disable -->

??? example "雛形：信頼の前後でフックが走るかを確かめる無害なフック"

    ```json
    {
      "hooks": {
        "SessionStart": [
          {
            "hooks": [
              {
                "type": "command",
                "command": "touch hook-ran.txt"
              }
            ]
          }
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet before-opening-unknown-repos/trust-probe -->

信頼の確認を受け入れずに閉じたときは、ファイルができない。受け入れたときと、`claude -p` で実行したときは、ファイルができる。この結果が出れば、このページの「信頼の前と後で効くもの」と「非対話の実行では確認が出ない」の通りに動いている。ファイルができなかったはずの場面でできたら、手元の版か設定が想定と違う。その環境では、リポジトリを開かずに調べ直す。この雛形は、この辞典ではまだ動かして確かめていない。

## 失敗したとき {#when-it-fails}

- **信頼してから不審な設定に気づいた**：そのフォルダでの作業を止め、設定を読み直す。入れてしまったものへの対処は <!-- link:begin vetting-extensions#after-install -->[MCP・プラグイン・スキルを入れる前の確認 › 入れてしまったとき](vetting-extensions.md#after-install)<!-- link:end --> にある。
- **手元で動かしてしまった**：そのリポジトリのフック・`env`・MCP サーバーが何をするかを読み直す。触れたかもしれない認証情報は、無効にして作り直す。
- **秘密が読まれたかもしれない**：初動は <!-- link:begin protecting-secrets#when-it-fails -->[秘密情報（.env・API キー）を守る › 効かなかったとき](protecting-secrets.md#when-it-fails)<!-- link:end --> にある。
- **コードベースを読むだけでよい**：他人のコードを調べる別の進め方は <!-- link:begin explore-a-codebase#unknown-repos -->[知らないコードベースを読む › 他人のリポジトリを開くとき](../recipes/explore-a-codebase.md#unknown-repos)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [プロンプトインジェクションの実際](prompt-injection-in-practice.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)

**関連**

- [MCP・プラグイン・スキルを入れる前の確認](vetting-extensions.md)
- [フックを安全に書く](../enforce/writing-safe-hooks.md)
- [フックの考え方とイベント](../enforce/hooks-basics.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [bypassPermissions と無人の実行はどこで動かすか](where-bypass-is-ok.md)
- [秘密情報（.env・API キー）を守る](protecting-secrets.md)
- [知らないコードベースを読む](../recipes/explore-a-codebase.md)
- [非対話モード（claude -p）の基本](../delegate/headless-basics.md)
- クラウドセッションと teleport（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Security](https://code.claude.com/docs/en/security)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Settings files and precedence](https://code.claude.com/docs/en/settings)：Anthropic・英語・確認日 2026-11-04
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04
- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)：Anthropic・英語・確認日 2026-11-04
- [Caught in the Hook: RCE and API Token Exfiltration Through Claude Code Project Files](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/)：Check Point Research・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
