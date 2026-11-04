---
id: connecting-mcp
title: MCP をつなぐ
aliases: [MCP サーバー, Model Context Protocol, claude mcp add, .mcp.json, /mcp]
type: feature
field: extend
chapter: MCP
order: 180
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 境界がない]
pitfalls: []
scenes: [開発, データ分析]
summary: 外部のサービスやツールを MCP でつなぎ、共有の範囲と資格情報を決め、つながらないときは切り分けられる。誰と使うかでスコープを選び、信頼できるサーバーと読み取り専用の資格情報から始める。
signs:
  - {type: goal, text: ブラウザからコピーして貼っているデータを、直接取りに行かせたい}
  - {type: goal, text: 社内のツールや外部のサービスを、Claude から使いたい}
  - {type: situation, text: チームで同じ外部ツールへの接続を使いたい}
  - {type: symptom, text: MCP サーバーをつないだのに、ツールが出てこない・つながらない}
prerequisites: [agent-loop]
related: [vetting-extensions, mcp-or-cli, choosing-mcp-servers, lethal-trifecta, prompt-injection-in-practice, protecting-secrets, connectors-in-the-app, always-on-costs, inspect-context, settings-layers, isolate-with-safe-mode, org-managed-settings-and-mcp, plugins-and-marketplaces, share-team-settings]
tracks: [mcp]
outdated_advice: [mcp-sse-transport]
sources: [cc-docs-mcp, cc-docs-security, cc-docs-sandboxing, cc-docs-desktop, hc-getting-started-local-mcp, cc-docs-features-overview]
volatility: 中
sections:
  - {title: 何を任せて、何を先に決めるか, anchor: use}
  - {title: 最小のつなぎ方, anchor: minimal}
  - {title: スコープと共有, anchor: scopes}
  - {title: 資格情報と権限, anchor: credentials}
  - {title: つながらない・ツールが出てこないとき, anchor: troubleshooting}
  - {title: Desktop アプリの MCP との関係, anchor: desktop}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：外部のサービスやツールを MCP でつなぎ、Claude に直接読ませられる。共有の範囲と資格情報を先に決めれば、つながらないときも切り分けられる。
    - **いつ引くか**：ブラウザからコピーして貼っているデータを、直接取りに行かせたいとき。社内のツールや外部のサービスを使いたいとき。チームで同じ接続を使いたいとき。つないだのにツールが出てこないとき。
    - **強制力**：<!-- gen:begin feature enforcement -->なし<!-- gen:end feature enforcement -->。道具を足す仕組みで、何も止めない。サーバーは利用者の権限で動くので、止めるのは資格情報の権限・権限ルール・管理設定の側である。成熟度は <!-- gen:begin feature maturity -->GA<!-- gen:end feature maturity -->、読み込みの時期は <!-- gen:begin feature load_timing -->セッション開始<!-- gen:end feature load_timing -->である。
    - **前提**：<!-- link:begin agent-loop -->[エージェントループと tool use](../basics/agent-loop.md)<!-- link:end -->

<!-- textlint-disable -->
別名：MCP サーバー・Model Context Protocol・claude mcp add・.mcp.json・/mcp
<!-- textlint-enable -->

MCP をつなぐとは、Claude Code に外部のサービスやツールを道具として足し、会話の中から呼べるようにすることである。決めることは 3 つある。誰と共有するか（スコープ）、どの資格情報と権限で動かすか、つながらないときにどこから見るかである。

## 何を任せて、何を先に決めるか {#use}

MCP が防ぐのは、Claude から外のデータが見えていないことである。チケット、データベース、監視の画面の内容をブラウザからコピーして貼っているなら、その作業を MCP に任せられる。Claude は必要なデータを自分で取りに行き、結果を見て次の一手を決める。

一方で、任せる範囲が広がるほど、境界の曖昧さが危険になる。つないだサーバーは利用者の権限で動き、読んだ内容は Claude の入力になる。そのため、つなぐ前に次の 3 つを先に決める。

- **信頼できるサーバーだけにする**。入れる前に出所と中身を確かめる。手順は「<!-- link:begin vetting-extensions#provenance -->[MCP・プラグイン・スキルを入れる前の確認 › 出所を確かめる](../safety/vetting-extensions.md#provenance)<!-- link:end -->」にある。
- **資格情報は読み取り専用から始める**。書き込みが要る理由が出たら、そのとき広げる。詳しくは[資格情報と権限](#credentials)の節にある。
- **信頼できない入力・秘密のデータ・外への送信を、1 つの構成に同時に置かない**。3 つとも要る作業には人の承認を挟む。
  考え方は「<!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](../safety/lethal-trifecta.md#three-capabilities)<!-- link:end -->」にある。
  読ませた内容に指示が仕込まれる経路は「<!-- link:begin prompt-injection-in-practice#channels -->[プロンプトインジェクションの実際 › 指示が入ってくる経路](../safety/prompt-injection-in-practice.md#channels)<!-- link:end -->」にある。

MCP で取ってきたデータも、道具の出力の 1 つである。取れたことと、正しいことは別なので、重要な数字は元のデータと突き合わせる。考え方は「<!-- link:begin agent-loop#tool-output -->[エージェントループと tool use › 道具の出力も確かめる](../basics/agent-loop.md#tool-output)<!-- link:end -->」にある。

## 最小のつなぎ方 {#minimal}

最小のつなぎ方は、サーバーを 1 つ追加して、接続と認証を確かめるところまでである。面で入口が違う。

=== "アプリ"

    アプリでは、コネクタとして追加する。メールやカレンダー、社内の資料、自分の MCP サーバーをつなぐ手順と、信頼してよいかの判断は「<!-- link:begin connectors-in-the-app#types -->[コネクタ（MCP）をアプリで使う › コネクタの種類](../app/connectors-in-the-app.md#types)<!-- link:end -->」に任せる。この辞典の Desktop の話は[Desktop アプリの MCP との関係](#desktop)の節だけである。

=== "Claude Code"

    リモートのサーバーは HTTP でつなぐ。

    ```bash
    claude mcp add --transport http notion https://mcp.notion.com/mcp
    ```

    ローカルのプロセスとして動かすサーバー（stdio）は、`--` の後ろにサーバーを起動するコマンドを書く。

    ```bash
    claude mcp add --env KEY=value --transport stdio myserver -- npx -y some-package
    ```

    Claude Code 自身のオプション（`--transport`・`--env`・`--scope`）は、サーバー名より前に置く。`--` の後ろは、そのままサーバーに渡される。

    追加したら、セッションの中で `/mcp` を開く。サーバーの接続の状態が見え、認証が要るサーバーはここから進める。端末からは `claude mcp list` と `claude mcp get <名前>` で同じ状態を見られる。外すときは `claude mcp remove <名前>` である。

つないだ後の MCP のツールは、ツール名の一覧だけが毎回の文脈に入り、定義の中身は使うときに読まれる。コンテキストのコストは<!-- gen:begin feature context_cost -->使うまで小さい<!-- gen:end feature context_cost -->。それでもサーバーを足すほど一覧は増えるので、使っていないサーバーは外す。常駐するものの費用の見方は「<!-- link:begin always-on-costs#resident-vs-on-demand -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 常駐するものと、使うときだけ読むもの](../context/always-on-costs.md#resident-vs-on-demand)<!-- link:end -->」にある。

ツールのほかに、サーバーが出すリソースとプロンプトも使える。リソースは `@サーバー名:リソース` の形で会話に参照させ、プロンプトは `/mcp__サーバー名__プロンプト名` の形のコマンドとして呼ぶ。出すかどうかはサーバー次第なので、使えるものは `/mcp` と `/` のメニューで確かめる。

## スコープと共有 {#scopes}

スコープとは、そのサーバーの定義を誰に効かせ、どのファイルに書くかの区別である。誰と使うかで選ぶ。`claude mcp add` に `--scope` を付けて選び、付けなければ local になる。

![MCP の 3 つのスコープの図。local と project はこのプロジェクト、user はすべてのプロジェクトに効く。同じ名前は local、project、user の順に勝つ。](../img/connecting-mcp/scopes.svg)

| スコープ | 効く範囲 | 書かれる場所 |
| --- | --- | --- |
| local（既定） | このプロジェクトの、自分だけ | `~/.claude.json` |
| project | このプロジェクトの、チーム全員 | リポジトリ直下の `.mcp.json` |
| user | すべてのプロジェクトの、自分だけ | `~/.claude.json` |

チームで同じ接続を使うなら project にして、`.mcp.json` を commit する。共有の設定の考え方は「<!-- link:begin share-team-settings#shared-vs-personal -->[チームで設定を共有する › 共有するものと個人に残すもの](../team/share-team-settings.md#shared-vs-personal)<!-- link:end -->」にある。`.mcp.json` に書くのは、サーバーの種類と URL と、秘密を差し込む環境変数の名前までにする。次の雛形は、HTTP でつなぎ、トークンを環境変数から渡す形である。

<!-- gen:begin snippet connecting-mcp/team-mcp -->
<!-- textlint-disable -->

??? example "雛形：チームで共有する .mcp.json（HTTP でつなぎ、秘密は環境変数から渡す）"

    ```json
    {
      "mcpServers": {
        "issue-tracker": {
          "type": "http",
          "url": "https://mcp.example.com/mcp",
          "headers": {
            "Authorization": "Bearer ${ISSUE_TRACKER_TOKEN}"
          }
        }
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet connecting-mcp/team-mcp -->

project スコープには、安全のための仕組みが 2 つある。

- 対話のセッションでは、`.mcp.json` のサーバーを初めて使う前に承認を求められる。リポジトリを clone しただけで、見知らぬサーバーが動き出すことはない。承認の記録を消したいときは `claude mcp reset-project-choices` を使う。
- `claude -p` のように承認を聞けない実行では、`.mcp.json` のサーバーは承認なしにつながる。CI や自動実行に載せるリポジトリでは、`.mcp.json` に入れるものを、その前提で選ぶ。外したいサーバーは `disabledMcpjsonServers` に書くか、`--strict-mcp-config` で起動する。

同じ名前のサーバーが複数の場所にあると、一番優先の高い場所の定義が 1 つだけ使われる。優先順は local、project、user、プラグイン、claude.ai のコネクタの順で、組織が管理設定で配るサーバーはこれらより上になる。定義はキーごとに合わさらず、丸ごと入れ替わる。そのため、project の定義に自分用の変更を足したいときは、local に同じ名前で全体を書く。設定の層の優先は「<!-- link:begin settings-layers#layers -->[設定ファイルの階層と優先順位 › 層と優先順位](../cli/settings-layers.md#layers)<!-- link:end -->」を参照する。組織で配るサーバーの許可は「<!-- link:begin org-managed-settings-and-mcp#mcp-allowlist -->組織に設定と MCP サーバーを配る › MCP サーバーの許可（準備中）<!-- link:end -->」に任せる。

!!! example "判断例：チケット管理のサーバーをどのスコープに置くか"
    - **状況**：チーム 5 人が同じチケット管理のサービスを使う。サーバーの URL は全員同じで、トークンは一人ずつ違う。
    - **迷う候補**：各自が user スコープに追加する／project スコープの `.mcp.json` を commit する。
    - **選んだもの**：project スコープで `.mcp.json` に URL を書き、トークンは各自の環境変数から渡す。
    - **理由**：URL とサーバーの種類は全員で同じなので、共有すると設定のずれが出ない。トークンは個人のものなので、ファイルに書かず、環境変数の名前だけを共有する。新しい人は、リポジトリを開いて承認し、環境変数を設定すれば使える。

## 資格情報と権限 {#credentials}

資格情報とは、サーバーが外のサービスに入るときに使う、トークン・パスワード・接続文字列のことである。サーバーは利用者の権限で動くので、資格情報の権限が、Claude がそのサービスにできることの上限になる。最初にこの上限を低く決めることが、境界を作る一番確実な方法である。

- **読み取り専用から始める**。データベースには読み取り専用のユーザーを使う。公式の文書も、Claude が実行するクエリでデータを変えられないようにするため、これを勧めている。書き込みが要る作業が出たら、そのときに別の資格情報を足す。
- **本番ではなく、複製か分析用の環境につなぐ**。読み取りだけでも、個人情報や秘密が会話に入りうる。
- **秘密はファイルに書かない**。`.mcp.json` では `${変数名}` で環境変数から差し込める。差し込めるのは、サーバーの `command`・`args`・`env`・`url`・`headers` の値である。環境変数が未設定のまま起動すると、警告が出て、`${変数名}` の文字のまま使われる。この状態では認証が通らないので、つながらないときの確認項目の 1 つになる。秘密を置かない・読ませない設定は「<!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end -->」にある。
- **信頼できるサーバーだけをつなぐ**。Anthropic はどの MCP サーバーのセキュリティも監査していない。自分で書いたサーバーか、信頼できる提供元のサーバーを使う。外のコンテンツを取ってくるサーバーは、プロンプトインジェクションの入り口になりうる。

次の雛形は、読み取り専用のユーザーでデータベースの MCP をつなぐ例である。サーバーの名前は、データベースの MCP の一例であり、推薦ではない。

<!-- gen:begin snippet connecting-mcp/readonly-db -->
<!-- textlint-disable -->

??? example "雛形：読み取り専用の資格情報でデータベースの MCP をつなぐ例"

    ```json
    {
      "mcpServers": {
        "analytics-db": {
          "type": "stdio",
          "command": "npx",
          "args": [
            "-y",
            "@bytebase/dbhub",
            "--dsn",
            "postgresql://${ANALYTICS_RO_USER}:${ANALYTICS_RO_PASSWORD}@db.example.com:5432/analytics"
          ]
        }
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet connecting-mcp/readonly-db -->

!!! example "判断例：分析用のデータベースに Claude をつなぐ"
    - **状況**：売上の集計を、毎回クエリを手で実行して結果を貼る形から、Claude に直接やらせたい。手元には、更新もできる管理用の接続文字列がある。
    - **迷う候補**：手元の接続文字列をそのまま渡す／SELECT だけを許す読み取り専用のユーザーを作って渡す。
    - **選んだもの**：読み取り専用のユーザーを作り、その接続文字列を環境変数から渡す。
    - **理由**：集計に要るのは SELECT だけである。更新できる接続を渡すと、仕込まれた指示や Claude の取り違えで、データが変わる経路が開く。権限をデータベース側で絞れば、Claude が間違っても変更は通らない。

権限の線引きは、MCP の設定だけでは足りない。Bash などのシェルコマンドを囲うサンドボックスは、MCP サーバーには及ばない（<!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end -->も参照）。ツールごとに許す・確認する・止めるを決めるのは、権限ルールの役目である。書き方は公式の権限の文書で確かめる。

## つながらない・ツールが出てこないとき {#troubleshooting}

MCP のサーバーをつないだのにツールが出ないときは、状態、設定の層、自分の設定の順に見る。上から順に確かめると、切り分けが早い。

1. **状態を見る**。セッションの中の `/mcp` か、端末の `claude mcp list` を使う。見るのは、サーバーが一覧に出るか、接続済みか、認証待ちかである。承認を待つ `.mcp.json` のサーバーは、承認待ちとして出る。認証は `/mcp` から進める。失敗した接続は、`/mcp` の各サーバーのメニューにある再接続で試せる。全部を試す `/mcp reconnect all` は新しい版の機能である。表示の細部と対応する版は、公式の文書で確かめる。
2. **追加のコマンドを見る**。stdio のサーバーが一覧に出ないときや起動に失敗するときは、書き方の誤りを疑う。オプションをサーバー名より前に置いたか、起動コマンドの前に `--` を置いたかを確かめる。`--env` の直後にサーバー名を置くと、名前が環境変数の 1 つとして読まれる。
3. **設定の層とスコープを見る**。次の 3 つが原因になる。
    - project スコープの `.mcp.json` は、初めに承認が要る。承認していないと、サーバーは使われない。
    - 同じ名前のサーバーが別の場所にあると、優先の高い定義が使われ、自分が書いたほうは使われない。
    - 組織の管理設定が、許すサーバーを絞っていることがある。

    どの層が読み込まれているかの確かめ方は「<!-- link:begin settings-layers#verify -->[設定ファイルの階層と優先順位 › 効いているかを確かめる](../cli/settings-layers.md#verify)<!-- link:end -->」にある。
4. **環境変数を見る**。`.mcp.json` で `${変数名}` を使っているなら、起動した端末にその変数があるかを確かめる。未設定だと、文字のまま送られて認証が通らない。
5. **自分の設定のせいかを切り分ける**。`--safe-mode` で起動し、同じ依頼を比べる。ただし `--safe-mode` は MCP も読まない。この方法で分かるのは、MCP そのものの不調ではなく、CLAUDE.md・フック・プラグインなど、ほかの設定や拡張との干渉があるかどうかである。比べ方は「<!-- link:begin isolate-with-safe-mode#compare -->[設定を外して切り分ける（--safe-mode） › 比べ方](../cli/isolate-with-safe-mode.md#compare)<!-- link:end -->」にある。

ツールが `/context` に並ばないことは、不調とは限らない。ツールの検索（tool search。必要なツールの定義だけを使うときに読む仕組み）が既定で働くので、起動直後は名前と指示だけが入る。ツールが見えないから失敗とは決めず、1 の `/mcp` で接続を確かめる。`/context` の見方は「<!-- link:begin inspect-context#reading -->[/context で中身を見る › 内訳の読み方](../context/inspect-context.md#reading)<!-- link:end -->」にある。

## Desktop アプリの MCP との関係 {#desktop}

Desktop アプリのローカルの MCP サーバーと、Claude Code の MCP の設定は、別のファイルに書かれ、一部だけがつながっている。

=== "アプリ"

    Desktop のローカルの MCP サーバーは、`claude_desktop_config.json` の `mcpServers` に書く。書き換えた後は、Desktop を完全に終了して起動し直す。この辞典では、アプリのコネクタの操作には立ち入らない。Desktop のローカル MCP の手順と、信頼してよいかの判断は「<!-- link:begin connectors-in-the-app#desktop-local-mcp -->[コネクタ（MCP）をアプリで使う › Desktop のローカル MCP](../app/connectors-in-the-app.md#desktop-local-mcp)<!-- link:end -->」に任せる。

=== "Claude Code"

    - Desktop の Code タブのローカルのセッションは、`claude_desktop_config.json` のサーバーも、`~/.claude.json` と `.mcp.json` のものと並べて読む。同じ名前なら Desktop の設定が勝つ。
    - 単独の CLI は、`claude_desktop_config.json` を読まない。
    - Desktop に設定済みのサーバーを CLI でも使うには、`claude mcp add-from-claude-desktop` で `~/.claude.json` に写す。macOS と WSL だけで動く。名前に英数字・ハイフン・下線以外を含むサーバーは写せない。

Desktop に設定したサーバーが CLI に出ないときは、まず「Claude Code」のタブの 3 点（単独の CLI は読まない・同名は Desktop が勝つ・写すには `add-from-claude-desktop`）を確かめる。Windows のネイティブや IDE 拡張での動きは未確認である。

## 効かない場面と落とし穴 {#limits}

MCP をつなぐと、次の場面で想定とずれる。

- **サンドボックスの外で動く**。Bash のコマンドを囲うサンドボックスは、MCP サーバーのプロセスには効かない。サーバーの権限は、資格情報とサーバー自身の作りで決まる。
- **入れた後に中身が変わりうる**。承認したときの定義と、後から読まれる定義が同じとは限らない。ツールの説明に指示が隠れている場合もある。入れる前の確認と、入れた後の変化の見方は「<!-- link:begin vetting-extensions#changes-after-install -->[MCP・プラグイン・スキルを入れる前の確認 › 入れた後に変わる（rug pull）](../safety/vetting-extensions.md#changes-after-install)<!-- link:end -->」にある。この辞典は、脅威の型の説明を safety のページに任せる。
- **`.mcp.json` だけでは、読み込まれるサーバーの全体は分からない**。ほかのスコープ、claude.ai のコネクタ、プラグインもサーバーを足す。全体は `/mcp` で見る。
- **出力が大きいと扱いにくい**。ツールの出力が大きいと警告が出て、さらに大きいと上限で扱いきれなくなる。値は、<!-- fact:begin mcp-output-token-limits -->未確認<!-- fact:end -->。大量のデータは、サーバー側で絞るか、必要な範囲だけを取らせる。
- **入れすぎると場所を取る**。サーバーを足すたびに、ツールの一覧が文脈に増える。判断を良くする分より増えるなら外す。選ぶ基準は「<!-- link:begin choosing-mcp-servers -->MCP サーバーの選び方（準備中）<!-- link:end -->」にある。

## 比べる相手 {#compare}

外部ツールの道は、MCP のほかに、CLI とスキルで済ませる方法がある。成熟した CLI があって、決まった作業なら、CLI のほうが文脈の効率がよい。CLI がないときや、認証つきの生きたデータが要るとき、シェル全体より狭い権限にしたいときは、MCP が生きる。選び方は「<!-- link:begin mcp-or-cli -->[MCP か CLI か](mcp-or-cli.md)<!-- link:end -->」にまとめてある。公式の文書は、つなぐ MCP と、使い方の知識を渡すスキルを組み合わせる形も勧めている。

組織の全員に MCP サーバーを配るなら、「<!-- link:begin org-managed-settings-and-mcp -->組織に設定と MCP サーバーを配る（準備中）<!-- link:end -->」を見る。サーバーを束にして配るなら、「<!-- link:begin plugins-and-marketplaces#before-install -->[プラグインとマーケットプレイス › 入れる前の確認](plugins-and-marketplaces.md#before-install)<!-- link:end -->」の確認を先に通す。

## 古くなった助言 {#outdated}

MCP を SSE の転送でつなぐ、という古い説明が残っている。今は、リモートのサーバーは HTTP でつなぐ（`claude mcp add --transport http`）。新しい版は、SSE しか出さないサーバーにも先に HTTP を試し、受け付けないときだけ SSE に切り替える。SSE を直接指定するのは、古い版か、HTTP を受け付けないサーバーのときだけである。`.mcp.json` に `"type": "sse"` が残っているサーバーは、HTTP に変えられないかを確かめる。経緯と時期は「<!-- link:begin outdated-advice-ledger#mcp-sse-transport -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#mcp-sse-transport)<!-- link:end -->」にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [エージェントループと tool use](../basics/agent-loop.md)

**次に読む**

- [MCP か CLI か](mcp-or-cli.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- MCP サーバーの選び方（準備中）

**関連**

- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [コネクタ（MCP）をアプリで使う](../app/connectors-in-the-app.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [/context で中身を見る](../context/inspect-context.md)
- [設定ファイルの階層と優先順位](../cli/settings-layers.md)
- [設定を外して切り分ける（--safe-mode）](../cli/isolate-with-safe-mode.md)
- 組織に設定と MCP サーバーを配る（準備中）
- [プラグインとマーケットプレイス](plugins-and-marketplaces.md)
- [チームで設定を共有する](../team/share-team-settings.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)：Anthropic・英語・確認日 2026-11-04
- [Security](https://code.claude.com/docs/en/security)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Desktop application](https://code.claude.com/docs/en/desktop)：Anthropic・英語・確認日 2026-11-04
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
