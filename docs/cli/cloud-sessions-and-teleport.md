---
id: cloud-sessions-and-teleport
title: クラウドセッションと teleport
aliases: [claude.ai/code, --cloud, /teleport, Claude Code on the Web, --remote]
type: feature
field: cli
chapter: ほかの面と離席
order: 160
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [握る, 縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発]
summary: 作業をクラウドのセッションで走らせて手元を閉じても続けさせ、終わったら teleport で手元の端末に取り込む。クラウドは手元の設定の一部を読まないので、計画と縛りをリポジトリに置いてから送る。
signs:
  - {type: goal, text: 手元で計画した作業をクラウドに渡し、PC を閉じても進めさせたい}
  - {type: situation, text: クラウドで動かしたセッションを、手元で続けたい}
prerequisites: [when-to-plan, where-it-runs]
related: [control-from-phone, resume-and-branch, agent-view-and-background, choosing-parallel-modes, cloud-schedules, protecting-secrets, checking-unattended-runs, share-team-settings]
tracks: [cloud-sessions]
outdated_advice: [code-on-the-web-remote]
sources: [cc-docs-claude-code-on-the-web, cc-docs-settings, cc-docs-cloud-environments, cc-docs-cli-reference, cc-changelog]
volatility: 高
sections:
  - {title: クラウドに送ってよい作業, anchor: what-to-send}
  - {title: 手元の設定との違い, anchor: settings}
  - {title: teleport で取り込む, anchor: teleport}
  - {title: 効かない場面・落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：手元で計画した作業をクラウドで走らせて PC を閉じても続けさせ、終わったら teleport で手元の端末に取り込める。
    - **成熟度**：<!-- gen:begin feature maturity -->GA<!-- gen:end feature maturity -->。クラウドのセッションは、手元の `~/.claude/settings.json` と `.claude/settings.local.json` を読まない。縛りはリポジトリに入れて送る。
    - **いつ引くか**：手元で計画した作業をクラウドに渡し、PC を閉じても進めさせたいとき。クラウドで動かしたセッションを、手元で続けたいとき。
    - **前提**：<!-- link:begin when-to-plan -->[plan mode の使いどころ](when-to-plan.md)<!-- link:end -->、<!-- link:begin where-it-runs -->[実行場所の違い（クラウド・自分の PC・リモート操作）](../surfaces/where-it-runs.md)<!-- link:end -->

<!-- textlint-disable -->
別名：claude.ai/code・--cloud・/teleport・Claude Code on the Web・--remote
<!-- textlint-enable -->

クラウドセッションは、Claude Code のセッションを自分の PC ではなく、Anthropic が管理するクラウドの環境で動かす機能である。手元のノート PC を閉じても作業は続き、終わったら `--teleport` で手元の端末に取り込める。この辞典では、任せる幅が広がる分だけ、渡す前の計画と縛りを重く見る。

## クラウドに送ってよい作業 {#what-to-send}

クラウドに送ってよいのは、リポジトリの中だけで完結し、完了を機械で確かめられる作業である。クラウドのセッションは、GitHub のリモートをクローンした新しい環境で動く。手元にしかないファイル、手元で起動したサービス、手元のブラウザには届かない。実行場所ごとの違いは <!-- link:begin where-it-runs#three-locations -->[実行場所の違い（クラウド・自分の PC・リモート操作） › 三つの実行場所](../surfaces/where-it-runs.md#three-locations)<!-- link:end --> に、届かないものの一覧は <!-- link:begin where-it-runs#what-cloud-cannot-reach -->[実行場所の違い（クラウド・自分の PC・リモート操作） › クラウドで動くときに届かないもの](../surfaces/where-it-runs.md#what-cloud-cannot-reach)<!-- link:end --> にある。

向く作業は次のとおりである。

- 計画が文書になっていて、手順と完了の条件が書いてある（例：移行の計画に沿った機械的な書き換え）
- テストやビルドで、済んだかどうかを機械で確かめられる
- 互いに独立していて、途中で人に聞き返す必要がほとんどない
- 失敗しても、ブランチを捨てれば元に戻せる

向かない作業は、方針が固まっていない作業、手元の DB や秘密を使う作業、途中で何度も判断を挟みたい作業である。方針が固まっていないなら、先に手元で <!-- link:begin when-to-plan#how-to -->[plan mode の使いどころ › 最小の使い方](when-to-plan.md#how-to)<!-- link:end --> から計画を作る。手元で動かしたまま席を離れたいだけなら、実行を手元に残す <!-- link:begin control-from-phone -->スマホから操作する（Remote Control）（準備中）<!-- link:end --> のほうが合う。

### 先に整えるもの

クラウドのセッションは、見張られないまま長く動く。しかも手元の縛りが届かないので、何も整えずに送ると、Claude の動く範囲に境界がない状態になる。この機能が防ぐ原因はこの「境界がない」で、作業を計画で握り、縛りをリポジトリに置いて縛ることで防ぐ。送る前に、次の 3 つを先に整える。

1. **計画をリポジトリに置く**：計画ファイルを保存し、commit して push する。クラウドの環境は、手元のチェックアウトではなく、GitHub 上の現在のブランチをクローンする。push していない commit は届かない
2. **縛りをリポジトリに置く**：機械で判定できる禁止は、リポジトリの `.claude/settings.json` に deny ルールとして入れる。手元だけにある設定は、次の節のとおり届かない。置き方は <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> を参照する
3. **結果の確かめ方を決める**：終了したという知らせだけで済ませず、差分と記録を読む。方法は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->[無人実行の結果を確かめる › 終了コードと要約だけで決めない](../verify/checking-unattended-runs.md#beyond-exit-codes)<!-- link:end --> にある

計画の書き方は、plan mode で作った計画を、目的・範囲・手順ごとの確かめ・完了の条件・止まって報告する条件に整える形が使いやすい。次の雛形は、計画ファイルの一例である。

<!-- gen:begin snippet cloud-sessions-and-teleport/cloud-task-plan -->
<!-- textlint-disable -->

??? example "雛形：クラウドに渡す作業の計画ファイル"

    ```markdown
    # クラウドに渡す作業：<題>

    ## 目的
    <何を達成したいか。一文で>

    ## 範囲
    - 触ってよい：<ディレクトリやファイル>
    - 触らない：<範囲外のもの>

    ## 手順
    1. <段の内容>。済んだ確かめ：<実行するコマンドか見るもの>
    2. <段の内容>。済んだ確かめ：<実行するコマンドか見るもの>

    ## 完了の条件
    - <テストやビルドが通る、など機械で確かめられるもの>
    - 変更はブランチ <ブランチ名> に push し、main には入れない

    ## 止まって報告する条件
    - 範囲外のファイルを変えないと進めないとき
    - 手順の確かめが 2 回続けて通らないとき
    - 計画にない依存を足す必要が出たとき
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet cloud-sessions-and-teleport/cloud-task-plan -->

### 最小の使い方

ターミナルから送るには、push 済みのブランチで `claude --cloud` に頼む内容を付けて始める。公式の文書の例（確認日 2026-11-05）は、手元の plan mode で計画を作り、計画ファイルを commit して push してから、次のように頼む流れである。

```bash
claude --cloud "Execute the migration plan in docs/migration-plan.md"
```

このコマンドは新しいクラウドのセッションを作り、手元の作業は続けられる。進み具合はブラウザの claude.ai/code か、Claude のモバイルアプリで見て、途中で指示を足せる。計画を承認する流れは <!-- link:begin when-to-plan#after-approval -->[plan mode の使いどころ › 計画を承認した後](when-to-plan.md#after-approval)<!-- link:end --> にある。

`--cloud` は一度に 1 つのリポジトリを対象にする。独立した作業は、`--cloud` を作業の数だけ並べれば、別々のセッションが同時に動く。ただし利用枠は手元の使用と共有で、並べた数に応じて減る。同時に動かす数の決め方は <!-- link:begin choosing-parallel-modes#compare -->[並列の方式の選び方 › 方式の比較](../delegate/choosing-parallel-modes.md#compare)<!-- link:end --> と <!-- link:begin agent-view-and-background#what-fits -->[agent view と背景セッション › 向く作業と向かない作業](../delegate/agent-view-and-background.md#what-fits)<!-- link:end --> を参照する。

使えるプランと、Claude のサブスクリプションの認証が要ることは、公式の [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web) で確かめる。API キーや Amazon Bedrock などの別の提供元の設定では使えない。この辞典は WSL・Linux の CLI を基準としている。ほかの OS での動作は未確認である。

!!! example "判断例：移行の書き換えを夜のうちに進める"
    - **状況**：50 ほどのファイルで、古い API の呼び出しを新しい書き方へ機械的に直したい。テストはあり、夜のうちに終わらせたい。
    - **迷う候補**：手元で Claude Code を動かしたまま PC を開けておく。計画を push してクラウドに送る。
    - **選んだもの**：手元の plan mode で計画を作り、deny ルールと計画ファイルを push してから、クラウドに送る。
    - **理由**：機械的な書き換えで、済んだかどうかをテストで確かめられる。クラウドなら PC を閉じても続き、失敗してもブランチを捨てれば戻る。翌朝は、差分とテストの記録を読んでから PR にする。

!!! example "判断例：手元の DB を使う調査"
    - **状況**：手元で起動したデータベースに繋ぎ、遅いクエリの原因を調べたい。途中で何度も結果を見て方針を変える。
    - **迷う候補**：クラウドに送る。手元のセッションを Remote Control で外から見る。
    - **選んだもの**：手元で動かし、席を離れる間は Remote Control で見る。
    - **理由**：クラウドの環境に手元の DB はなく、途中の判断も多い。実行を手元に残すほうが筋が通る。

## 手元の設定との違い {#settings}

クラウドのセッションは、リポジトリのクローンの中にあるものだけを読み、手元にしかないものは読まない。公式の文書（確認日 2026-11-05）による、単一のリポジトリのセッションでの違いは次のとおりである。

| 置き場所 | クラウドで | 理由 |
| --- | --- | --- |
| リポジトリの `CLAUDE.md` と `.claude/rules/` | 読む | クローンに含まれる |
| リポジトリの `.claude/settings.json` のフックと権限ルール | 読む | クローンに含まれる |
| リポジトリの `.mcp.json` | 読む | クローンに含まれる |
| リポジトリの `.claude/skills/`・`agents/`・`commands/` | 読む | クローンに含まれる |
| リポジトリの `.claude/settings.json` で宣言したプラグイン | 入らない | クラウドでは、リポジトリが有効にしたプラグインを入れない |
| 手元の `~/.claude/settings.json`・`~/.claude/CLAUDE.md` | 読まない | 手元の PC にある |
| 手元の `.claude/settings.local.json` | 読まない | クローンに入らない |
| `claude mcp add` で local か user の範囲に足した MCP | 読まない | 手元の `~/.claude.json` に書かれる |
| 手元の MDM や管理設定のファイル | 届かない | クラウドは別のマシンで動く。組織のサーバー管理の設定は別経路で届く |

読む・読まないの境目は、リポジトリに commit されているかどうかである。複数のリポジトリを同じセッションで開く場合や、claude.ai の Projects（作業ごとに資料と指示をまとめる機能）の中のクラウドのスレッドでは、読むものがさらに減る。該当するときは、公式の [Settings files and precedence](https://code.claude.com/docs/en/settings) の「Settings in cloud sessions」で確かめる。

### 縛りを置き直す

手元の `~/.claude/settings.json` や `.claude/settings.local.json` に deny ルールを置いている人は、同じ縛りがクラウドのセッションには届かないことに注意する。手元で効いていた縛りが、クラウドでは何も働かない。これが、手元の設定との違いで起きる最も痛い取り違えである。

共有してよい縛りは、リポジトリの `.claude/settings.json` に移す。次の設定は、`.env` の読み取りと強制 push を止める deny ルールの一例である。

<!-- gen:begin snippet cloud-sessions-and-teleport/cloud-repo-settings -->
<!-- textlint-disable -->

??? example "雛形：クラウドのセッションにも届く縛りをリポジトリに置く設定"

    ```json
    {
      "permissions": {
        "deny": [
          "Read(./.env)",
          "Read(./.env.*)",
          "Read(./secrets/**)",
          "Bash(git push --force *)"
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet cloud-sessions-and-teleport/cloud-repo-settings -->

deny ルールが効くか、送る前に確かめる。偽の秘密だけを入れた `.env` を置いた作業用のリポジトリで試す手順は、<!-- link:begin protecting-secrets#verify -->[秘密情報（.env・API キー）を守る › 偽の秘密で確かめる](../safety/protecting-secrets.md#verify)<!-- link:end --> にある。何を共有し、何を個人に残すかは <!-- link:begin share-team-settings#shared-vs-personal -->[チームで設定を共有する › 共有するものと個人に残すもの](../team/share-team-settings.md#shared-vs-personal)<!-- link:end --> を参照する。

秘密は、リポジトリに commit せず、会話にも貼らない。置き方の考え方は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> にある。API キーをクラウドのセッションで使う設定は、公式の [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments) で確かめる。

クラウドの環境は、ネットワークの接続先も設定で決まる。公式の文書によると、Anthropic が管理する環境では接続先が既定で制限され、無効にもできる。接続先と権限を最小にする考え方は <!-- link:begin cloud-schedules#least-privilege -->[クラウドの定期タスク › 接続先と権限を最小にする](../delegate/cloud-schedules.md#least-privilege)<!-- link:end --> にある。

なお、リモートのないリポジトリや、Claude の GitHub アプリが入っていない GitHub のリポジトリから送ると、ローカルのリポジトリをまとめて直接アップロードする経路になることがある。この経路でコミット前の変更が含まれるかは、この辞典では確かめていない。手元の変更を送りたくないときは、先に stash するか戻してから送る。

## teleport で取り込む {#teleport}

teleport は、クラウドで動いたセッションを、手元の端末に取り込む操作である。取り込むと、クラウドのセッションのブランチを取得して checkout し、会話を手元の端末に読み込む。取り込んだ後の作業は手元で続けられる。

取り込み方は次のとおりである（確認日 2026-11-05）。

- `claude --teleport`：セッションの一覧から選ぶ。`claude --teleport <セッション ID>` なら直接開く
- `/teleport`（短縮は `/tp`）：すでに手元で動かしているセッションの中から、同じ一覧を開く
- claude.ai/code のセッションのメニューで **Open in > Terminal** を選ぶと、貼り付けるコマンドが得られる

取り込むには、次の条件が要る。

| 条件 | 内容 |
| --- | --- |
| 作業ツリーがきれい | 未 commit の変更があると、stash するよう求められる |
| 同じリポジトリ | フォークではなく、同じリポジトリのチェックアウトで実行する |
| ブランチが push 済み | クラウドのセッションのブランチがリモートにある |
| 同じアカウント | クラウドのセッションと同じ claude.ai のアカウントで認証している |

CLI からの引き渡しは、クラウドから手元への一方向である。手元の端末のセッションを、そのままクラウドへ送ることはできない。Desktop アプリには、手元のセッションをクラウドへ送る操作がある。

取り込んだ後の扱いには、3 つの注意がある。

- **手元の作業はクラウドに戻らない**：取り込んだセッションは手元の別の写しになる。以降の作業は、claude.ai やモバイルアプリのクラウドのセッションには現れない
- **圧縮された部分は届かない**：クラウドのセッションが長くなって圧縮されていると、要約される前のやり取りは手元に写されない。Claude は要約から続ける。元のやり取りは claude.ai で読む
- **スマホから見続けるなら別に始める**：取り込んだ手元のセッションで `/remote-control` を始める。仕組みは <!-- link:begin control-from-phone -->スマホから操作する（Remote Control）（準備中）<!-- link:end --> を参照する

手元の端末の会話そのものを再開・分岐するには、クラウドとは別に <!-- link:begin resume-and-branch#resume -->[セッションに名前を付けて再開・分岐する › 再開する](resume-and-branch.md#resume)<!-- link:end --> を使う。`--resume` は手元の履歴を開くので、クラウドのセッションは一覧に出ない。

### 結果を確かめる

取り込む前に、クラウドで何が起きたかを確かめる。終了した、という知らせだけで済ませない。claude.ai/code の **Changes** で差分を読み、行ごとにコメントを付けて返せる。テストの記録と差分を突き合わせる方法は <!-- link:begin checking-unattended-runs#records -->[無人実行の結果を確かめる › 記録と差分で確かめる](../verify/checking-unattended-runs.md#records)<!-- link:end --> にある。最後の判断は人とブランチの保護に置く。置き方は <!-- link:begin checking-unattended-runs#final-decision -->[無人実行の結果を確かめる › 最後の判断を人に置く](../verify/checking-unattended-runs.md#final-decision)<!-- link:end --> を参照する。

実行中のセッションには、別の端末から追加の指示を送れる。`claude -p "指示" --cloud <セッション ID>` は、1 通を送って終わる。返事は待たない。

## 効かない場面・落とし穴 {#limits}

- **手元の縛りは届かない**：`~/.claude/settings.json` と `.claude/settings.local.json` の deny ルールは、クラウドで働かない。リポジトリの `.claude/settings.json` に置き直し、送る前に確かめる
- **push していない作業は届かない**：クラウドは GitHub 上のブランチをクローンする。手元だけの commit と、未 commit の変更は入らない。ブランチが GitHub になければ `Branch <名前> is not on GitHub` の行が出て、別の起点から始まる
- **利用枠は共有で、並べるほど減る**：クラウドのセッションの使用量は、手元の Claude の使用量と同じ上限で数える。並列の数に比例して消費が増える。数の決め方は <!-- link:begin choosing-parallel-modes#same-files -->[並列の方式の選び方 › 同じファイルを触るか](../delegate/choosing-parallel-modes.md#same-files)<!-- link:end --> を参照する
- **GitHub が前提**：リポジトリのクローンと PR の作成は GitHub が前提である。ほかのホストのリポジトリは手元からアップロードして送れるが、結果をそのリモートへ push できない
- **環境は期限で切れる**：しばらく使わないと VM が回収される。会話の履歴は戻るが、動いていたシェルのコマンドとサブエージェント、セッション内で組んだ定期の予定は戻らない。再開してから頼み直す
- **入れ子の `claude -p` で、セッションの記録が混ざったことがある**：クラウドのセッションの中で `claude -p` を動かすと、外側の ID と記録を共有する不具合があった。CHANGELOG に直した旨がある。環境変数 `CLAUDE_CODE_DISABLE_NESTED_SESSION_ID=1` で以前の動きに戻せる。扱う版は CHANGELOG で確かめる
- **PR の自動対応は、コメントで動く自動化を起こしうる**：Auto-fix では、Claude があなたの GitHub アカウントで返信を投稿する。コメントで動く自動化を持つリポジトリでは、有効にする前に確かめる

## 比べる相手 {#compare}

| 手段 | 向く場面 | 詳しい説明 |
| --- | --- | --- |
| Remote Control | 実行とファイルを手元に残し、席を離れて見る | <!-- link:begin control-from-phone -->スマホから操作する（Remote Control）（準備中）<!-- link:end --> |
| クラウドの定期タスク | 決まった時刻や GitHub のイベントで、人なしで動かす | <!-- link:begin cloud-schedules -->[クラウドの定期タスク](../delegate/cloud-schedules.md)<!-- link:end --> |
| 背景セッション | 手元の PC で、見張らなくてよい作業を投入する | <!-- link:begin agent-view-and-background -->[agent view と背景セッション](../delegate/agent-view-and-background.md)<!-- link:end --> |
| 並列の方式 | 並列の数と、誰が調整するかを決める | <!-- link:begin choosing-parallel-modes -->[並列の方式の選び方](../delegate/choosing-parallel-modes.md)<!-- link:end --> |
| 実行場所の違い | クラウド・自分の PC・リモート操作を選ぶ | <!-- link:begin where-it-runs -->[実行場所の違い（クラウド・自分の PC・リモート操作）](../surfaces/where-it-runs.md)<!-- link:end --> |

## 古くなった助言 {#outdated}

「Claude Code on the Web と `--remote` を使う」という助言は、今は言い方が変わっている。機能の名前は <!-- name:begin web-to-cloud-sessions -->クラウドセッション（cloud sessions）<!-- name:end --> で、ターミナルから始めるフラグは <!-- name:begin remote-to-cloud-flag -->--cloud<!-- name:end --> である。`--remote` は非推奨の別名として今も動く。ブラウザの claude.ai/code は、今も Claude Code on the web とも呼ばれる。台帳の行は <!-- link:begin outdated-advice-ledger#code-on-the-web-remote -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#code-on-the-web-remote)<!-- link:end --> にある。

自分のスクリプトや手順書に `claude --remote` があれば、`--cloud` に替える。`--remote-control` は別の機能なので、替えない。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)：Anthropic・英語・確認日 2026-11-04
- [Settings files and precedence](https://code.claude.com/docs/en/settings)：Anthropic・英語・確認日 2026-11-04
- [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments)：Anthropic・英語・確認日 2026-11-04
- [CLI reference](https://code.claude.com/docs/en/cli-reference)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [plan mode の使いどころ](when-to-plan.md)
- [実行場所の違い（クラウド・自分の PC・リモート操作）](../surfaces/where-it-runs.md)

**関連**

- スマホから操作する（Remote Control）（準備中）
- [セッションに名前を付けて再開・分岐する](resume-and-branch.md)
- [agent view と背景セッション](../delegate/agent-view-and-background.md)
- [並列の方式の選び方](../delegate/choosing-parallel-modes.md)
- [クラウドの定期タスク](../delegate/cloud-schedules.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [チームで設定を共有する](../team/share-team-settings.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
