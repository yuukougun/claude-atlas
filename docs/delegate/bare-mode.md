---
id: bare-mode
title: --bare と再現性
aliases: [bare mode, 自動の読み込みを止める]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 200
level: 回す
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 縛る]
prevents: [散らかっている, 境界がない]
pitfalls: []
scenes: [開発]
summary: --bare で CLAUDE.md・フック・MCP などの自動の読み込みを止め、どのマシンでも同じ条件で claude -p を動かせる。手元の設定や、知らないリポジトリのフックが自動の実行に混ざるのを防ぐ。
signs:
  - {type: symptom, text: 手元と CI で、同じ指示なのに結果が違う}
  - {type: symptom, text: 自動の実行に、自分の CLAUDE.md や hooks が混ざる}
prerequisites: [headless-basics]
related: [before-opening-unknown-repos, vetting-extensions, check-billing-path, settings-layers, isolate-with-safe-mode, checking-unattended-runs, github-actions-with-claude, batch-and-p-loops, choosing-automation]
tracks: [headless, settings, bare-mode]
sources: [cc-docs-headless, cc-docs-cli-reference, cc-changelog, cc-docs-changelog]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 読み込まないもの, anchor: what-is-skipped}
  - {title: 認証が変わる（サブスクリプションで使うとき）, anchor: authentication}
  - {title: 効いているかを確かめる, anchor: verify}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：`--bare` で CLAUDE.md・フック・MCP などの自動の読み込みを止め、どのマシンでも同じ条件で `claude -p` を動かせる。
    - **いつ引くか**：手元と CI で、同じ指示なのに結果が違うとき。自動の実行に、自分の CLAUDE.md やフックが混ざるとき。
    - **強制力**：読み込みそのものを起動時に止める。指示で頼むのではなく、起動の仕方で決まる。ただし道具の許可は絞らないので、許可と上限は別に渡す。
    - **いちばんの注意**：サブスクリプションのログインを使わない。`ANTHROPIC_API_KEY` などの API の認証が要り、API の従量課金になる。
    - **前提**：<!-- link:begin headless-basics -->[非対話モード（claude -p）の基本](headless-basics.md)<!-- link:end -->

<!-- textlint-disable -->
別名：bare mode・自動の読み込みを止める
<!-- textlint-enable -->

`--bare` は、`claude -p` が起動のときに設定やフックなどを自動で探して読む動きを止めるオプションである。成熟度は <!-- gen:begin feature bare-mode/maturity -->GA<!-- gen:end feature bare-mode/maturity --> で、公式は、スクリプトと SDK の呼び出し向けの起動の仕方として説明する。このページは、何を読まなくなるか、認証がどう変わるか、効いているかの確かめ方を扱う。

## 使いどころ {#when}

`--bare` は、自動の実行の前提を、読み込む場所の側から揃える手段である。手元と CI で結果が違う原因の多くは、指示の違いではなく、読み込まれたものの違いにある。手元には自分の CLAUDE.md・自分のフック・入れたプラグイン・自動メモリがあり、CI にはない。

防ぐ原因は 2 つある。

- 散らかっている：手元の設定や記憶が自動の実行に混ざり、マシンごとに前提が変わる（原理：見せる）。`--bare` なら、何を読ませたかを起動のコマンドだけで説明できる。
- 境界がない：`--bare` なしの `claude -p` は、知らないフォルダでも `.claude/settings.json` のフックを実行し、`.mcp.json` のサーバーを接続する。信頼の確認は出ない（原理：縛る）。`--bare` はこの 2 つを読まない。

任せる幅を広げる話なので、守りを先に決める。`--bare` が止めるのは読み込みであり、許す道具や止まる上限は決めない。許可と上限は <!-- link:begin headless-basics#permissions -->[非対話モード（claude -p）の基本 › 許可と権限モード](headless-basics.md#permissions)<!-- link:end --> と <!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](headless-basics.md#limits)<!-- link:end --> で先に決める。知らないリポジトリを無人で動かす場合は、`--bare` だけで足りるとは考えない。先に整える守りは <!-- link:begin before-opening-unknown-repos#headless -->[知らないリポジトリを開く前に › 非対話の実行では確認が出ない](../safety/before-opening-unknown-repos.md#headless)<!-- link:end --> にあり、隔離のしかたは <!-- link:begin before-opening-unknown-repos#isolate -->[知らないリポジトリを開く前に › 隔離して動かす](../safety/before-opening-unknown-repos.md#isolate)<!-- link:end --> にある。

## 最小の使い方 {#minimal}

=== "Claude Code"

    API キーを環境に置き、`--bare` と許す道具を足して起動する。

    ```bash
    export ANTHROPIC_API_KEY=...   # Console で作った API キー
    claude --bare -p "Summarize README.md" --allowedTools "Read"
    ```

    - 読ませたいものは、起動のオプションで明示して渡す。システムプロンプトへの追記は `--append-system-prompt`、設定は `--settings`、MCP サーバーは `--mcp-config`、サブエージェントは `--agents`、プラグインは `--plugin-dir` で渡す。
    - 手元の CLAUDE.md の内容を使いたいときも、勝手には読まれない。必要な指示はプロンプトか `--append-system-prompt` に書く。
    - 全オプションの一覧は、公式の [CLI reference](https://code.claude.com/docs/en/cli-reference) を見る。

## 読み込まないもの {#what-is-skipped}

`--bare` の起動では、次のものの自動の探索を飛ばす。公式の [Run Claude Code programmatically](https://code.claude.com/docs/en/headless) の説明に沿った一覧である。

- フック
- スキル
- カスタムコマンド
- サブエージェント
- 入れたプラグイン
- MCP サーバー
- 自動メモリ
- CLAUDE.md

置かれた場所は問わない。作業中のフォルダの `.claude/` や `.mcp.json` も、`~/.claude` も読まない。同僚の `~/.claude` のフックや、プロジェクトの `.mcp.json` のサーバーが動かない、というのがこの仕様の核心である。

読み込みが「飛ぶ」だけでなく、実行中の挙動にも差が出る。

- MCP サーバー：コマンドラインで渡したものだけが接続する。
- システムリマインダー（実行中に Claude へ差し込まれる、状態の変化の通知）：Claude には、プロンプトとツールの結果だけが渡る。たとえば、先に読んだファイルが後で書き換わっても、そのことは伝わらない。使えるスキルの一覧も渡らない。
- バックグラウンドの作業：バックグラウンドのコマンドやサブエージェントは使えない。時間切れのコマンドは、バックグラウンドへ移らずに止まる。

この 3 項目の制限が一部だけだった版もある（<!-- fact:begin bare-mode-partial-limits-before -->v2.1.286 より前は一部だけ（2026-11-05 時点）<!-- fact:end -->）。

読ませ直す手段にも例外がある。`--settings` で渡したフックは、`--bare` のもとでは動かない。フラグで読み込むプラグインの中のフックも動かない。フックを必ず動かしたい実行では、`--bare` を使わない。`--add-dir` で名指ししたフォルダは一部が例外で、その `.claude/skills/` のスキルは読み込まれるが、`.claude/commands/` と `.claude/agents/` は読まれない。

Claude には、Bash・ファイルの読み取り・ファイルの編集の道具が残る。

## 認証が変わる（サブスクリプションで使うとき） {#authentication}

`--bare` の起動は、OAuth の認証情報もシステムのキーチェーンも読まない。サブスクリプションのログインは、そのままでは使えない。`CLAUDE_CODE_OAUTH_TOKEN` も読まれない。

Anthropic の API には、次のどちらかで認証する。

- 環境変数 `ANTHROPIC_API_KEY`：Console で作った API キーを置く。
- `apiKeyHelper`：`--settings` に渡す JSON の中に書く。

Amazon Bedrock・Google Cloud・Microsoft Foundry は、それぞれの提供元の認証情報をふだんどおり読む。

サブスクリプションで使う読者にとって、これは設計の分かれ目になる。API キーを使うと、その Console の組織に API の従量の料金がかかり、プランの利用量は使われない。経路が変わる仕組みと確かめ方は <!-- link:begin check-billing-path#api-key-in-env -->[課金の経路を確かめる（API キーとサブスクリプション） › API キーの環境変数があるとき](../cost/check-billing-path.md#api-key-in-env)<!-- link:end --> と <!-- link:begin check-billing-path#check-current-path -->[課金の経路を確かめる（API キーとサブスクリプション） › 今の経路を確かめる](../cost/check-billing-path.md#check-current-path)<!-- link:end --> にある。`claude -p` が鍵を見つけたときの扱いは <!-- link:begin headless-basics#billing-path -->[非対話モード（claude -p）の基本 › 課金の経路（API キーがあるとき）](headless-basics.md#billing-path)<!-- link:end --> にもある。

!!! example "判断例：サブスクリプションで使う個人の、毎晩のスクリプト"
    - **状況**：自分のマシンで毎晩 `claude -p` を回す。ふだんの `~/.claude` の設定や自動メモリが、結果に混ざって困っている。API キーは契約していない。
    - **迷う候補**：A は API キーを取って `--bare` にする。B はサブスクリプションのまま、読む設定の層を `--setting-sources` で絞り、専用の `CLAUDE_CONFIG_DIR` を使う。
    - **選んだもの**：B。
    - **理由**：目的は自分の設定を切り離すことで、認証を変えることではない。A は従量課金を新しく始める。B は認証を変えずに混ざりを減らせる。CI のように、そもそも API キーで動かす実行なら、A が素直である。

読む設定を絞る選び方は、比べる相手の節にまとめる。

## 効いているかを確かめる {#verify}

`--bare` を付けたつもりで、実際には効いていない、あるいは別のものが混ざっている、ということがありうる。起動の記録で確かめる。

`--output-format stream-json` に `--verbose` を足すと、最初の `system/init` のイベントに、セッションのモデル・道具・MCP サーバー・読み込まれたプラグインが出る。

```bash
claude -p "ok" --output-format stream-json --verbose \
  | jq -c 'select(.type == "system" and .subtype == "init")'
```

`--bare` を付けない実行と付けた実行で、この行を比べる。読み込まないはずの MCP サーバーやプラグインが残っていないかを見る。MCP サーバーを `--mcp-config` で渡した実行では、設定の誤りで外された項目が `mcp_server_errors` に出る。CI では、そのキーが空でないときに落とす、という使い方ができる。

版と日付も記録に残す。同じ条件のつもりでも、Claude Code の版やモデルが違えば結果は変わる。`claude --version` の出力と、`--model` で固定したモデルの名前を、実行の記録と一緒に保存する。

## 雛形 {#templates}

サブスクリプションのまま、手元の設定を混ぜない起動の例を 1 つ載せる。API キーが要る `--bare` の起動は、条件と考え方を上の節に書き、雛形にはしない。

<!-- gen:begin snippet bare-mode/isolated-run -->
<!-- textlint-disable -->

??? example "雛形：自分の設定を混ぜない claude -p の起動例（サブスクリプションのまま）"

    ```bash
    #!/usr/bin/env bash
    # 手元の設定を混ぜずに claude -p を動かす例。サブスクリプションのまま使える形
    # 使い方: MODEL=<モデルの名前> ./isolated-run.sh "プロンプト"
    set -euo pipefail

    # 鍵の環境変数を外す。残っていると、-p は必ずその鍵を使い、API の従量課金になる
    unset ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN

    # 専用の置き場所。~/.claude の設定・CLAUDE.md・rules・skills・agents・plugins・自動メモリは読まれない
    # 初回だけ、この置き場所で claude を対話で起動して /login しておく
    export CLAUDE_CONFIG_DIR="${CLAUDE_CONFIG_DIR:-$HOME/.claude-isolated}"
    export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
    export ENABLE_CLAUDEAI_MCP_SERVERS=false

    # project と local の設定だけを読む。MCP は --mcp-config で渡したものだけにする
    # モデルは固定する。記録のために版も残す
    claude --version >&2
    claude -p "$1" \
      --setting-sources project,local \
      --strict-mcp-config \
      --model "${MODEL:?MODEL にモデルの名前を入れる}" \
      --output-format json
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet bare-mode/isolated-run -->

この例は、`--bare` ではなく、読む設定の層と置き場所を絞る組み合わせである。認証を変えない代わりに、効果の範囲は `--bare` より狭い。どの層が残るかは <!-- link:begin settings-layers#layers -->[設定ファイルの階層と優先順位 › 層と優先順位](../cli/settings-layers.md#layers)<!-- link:end --> で確かめる。

## 効かない場面・落とし穴 {#pitfalls}

- 自分の守りのフックも止まる：書式の自動修正や、危険なコマンドを止めるフックを使っていても、`--bare` では動かない。止めたいことは、許す道具の指定と権限モードで渡す。
- 必要な指示が消える：プロジェクトの CLAUDE.md に書いた規約は読まれない。CI で規約を効かせたいなら、プロンプトか `--append-system-prompt` で渡す。
- 同じ条件であって、同じ出力ではない：読み込みを揃えても、モデルの出力は毎回同じにはならない。モデルと版を固定して記録し、結果は<!-- link:begin checking-unattended-runs -->[無人実行の結果を確かめる](../verify/checking-unattended-runs.md)<!-- link:end -->のように確かめる。
- 鍵の置き忘れ：シェルの設定ファイルに `ANTHROPIC_API_KEY` を書いたまま、サブスクリプションのつもりで `claude -p` を動かすと、従量課金になる。`--bare` なしでも、`-p` は変数があれば必ずその鍵を使う。
- 知らないリポジトリの安全は別の話：`--bare` はリポジトリのフックと MCP の設定を読まないだけで、Bash の道具は残る。指示にだまされて危険なコマンドを実行する問題は残る。隔離や許可の絞り込みと組み合わせる。
- 外した設定が漏れる古い版：`--setting-sources` で外した設定ファイルの一部が、渡り続ける不具合が過去にあった（直った版：<!-- fact:begin setting-sources-leak-fix-version -->未確認<!-- fact:end -->）。Claude Code を更新して使い、版を記録する。
- `-p` の既定が変わる予定：<!-- fact:begin bare-mode-default-plan -->公式の headless の文書は、--bare を将来 -p の既定にすると書く（予定。入る版は未定）（2026-11-05 時点）<!-- fact:end -->。予定は変わりうるので、実行の挙動を前提にするときは `--bare` を毎回書く。
- 動作の確認は WSL・Linux の CLI が基準である。ほかの OS と IDE 拡張の動作は未確認である。

## 比べる相手 {#compare}

自動の読み込みを減らす方法は 3 つある。どれも、認証と効果の範囲が違う。

| 方法 | 止まるもの | 認証 |
| --- | --- | --- |
| `--bare` | フック・スキル・サブエージェント・プラグイン・MCP・自動メモリ・CLAUDE.md の自動の探索 | API キーか `apiKeyHelper` が要る |
| `--safe-mode` | 自分の設定と拡張（CLAUDE.md・スキル・プラグイン・フック・MCP など）。管理設定は効く | そのまま。OAuth も使える |
| `--setting-sources` | 指定しない層の設定ファイル | そのまま |

- 認証を変えずに壊れた設定の切り分けをしたいなら、<!-- link:begin isolate-with-safe-mode -->[設定を外して切り分ける（--safe-mode）](../cli/isolate-with-safe-mode.md)<!-- link:end --> を使う。プロジェクトのフックも止まるので、そのフックそのものの確認には使えない。
- 読む設定の層を選ぶなら `--setting-sources`。層の考え方は <!-- link:begin settings-layers -->[設定ファイルの階層と優先順位](../cli/settings-layers.md)<!-- link:end --> にある。
- 外の人が書いた拡張を入れる前の確認は <!-- link:begin vetting-extensions -->[MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)<!-- link:end --> にある。`--bare` は入れた後の読み込みを止めるだけで、中身の確認の代わりにならない。
- 同じ作業を多数のファイルに流すなら <!-- link:begin batch-and-p-loops -->多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）<!-- link:end -->。ループの 1 回ごとの呼び出しに `--bare` を付ければ、毎回同じ条件になる。GitHub Actions から動かす形は <!-- link:begin github-actions-with-claude -->[GitHub Actions と @claude](github-actions-with-claude.md)<!-- link:end -->、動かし方そのものの選び方は <!-- link:begin choosing-automation -->[自動化の選び方（定期タスク・非対話モード・SDK）](choosing-automation.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04
- [CLI reference](https://code.claude.com/docs/en/cli-reference)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [非対話モード（claude -p）の基本](headless-basics.md)

**関連**

- [知らないリポジトリを開く前に](../safety/before-opening-unknown-repos.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [課金の経路を確かめる（API キーとサブスクリプション）](../cost/check-billing-path.md)
- [設定ファイルの階層と優先順位](../cli/settings-layers.md)
- [設定を外して切り分ける（--safe-mode）](../cli/isolate-with-safe-mode.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [GitHub Actions と @claude](github-actions-with-claude.md)
- 多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）
- [自動化の選び方（定期タスク・非対話モード・SDK）](choosing-automation.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
