---
id: agent-sdk-basics
title: Agent SDK（Claude Code をライブラリとして使う）
nav_title: Agent SDK
aliases: [Claude Agent SDK, claude-agent-sdk]
type: feature
field: api
chapter: エージェントを組む
order: 100
level: 回す
priority: 推奨
surfaces: [api, claude-code]
principle: [縛る, 確かめる]
prevents: [縛っていない, 境界がない]
scenes: [開発]
summary: Claude Code と同じ道具とループを、自分のプログラムからライブラリとして使える。読み込む設定・権限・課金の経路を、対話の Claude Code との違いとして押さえられる。
signs:
  - {type: goal, text: Claude Code と同じ動きを自分のプログラムから使いたい}
  - {type: situation, text: 社内の仕組みに Claude Code を組み込む}
prerequisites: [sdk-comparison, permission-rules]
related: [headless-basics, bare-mode, hooks-basics, sandboxing, protecting-secrets, check-billing-path, checking-unattended-runs, github-actions-with-claude, long-running-agent-context]
tracks: [agent-sdk, headless]
sources: [cc-docs-agent-sdk-overview, cc-docs-agent-sdk-migration, cc-docs-agent-sdk-claude-code-features, hc-agent-sdk-plan, hc-api-credits, cc-docs-headless, cc-docs-permission-modes]
volatility: 高
sections:
  - {title: Claude Code と同じもの・違うもの, anchor: same-and-different}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 読み込む設定を決める, anchor: setting-sources}
  - {title: 権限と承認, anchor: permissions}
  - {title: 課金の経路, anchor: billing}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：Claude Code と同じ道具とループを、Python か TypeScript のライブラリとして自分のプログラムから動かせる。
    - **いつ引くか**：Claude Code と同じ動きを自分のプログラムから使いたいとき。社内の仕組みに Claude Code を組み込むとき。
    - **前提**：<!-- link:begin sdk-comparison -->[Client SDK・Agent SDK・Managed Agents・CLI の比較](sdk-comparison.md)<!-- link:end -->・<!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Claude Agent SDK・claude-agent-sdk
<!-- textlint-enable -->

Agent SDK（現在の名前は <!-- name:begin code-sdk-to-agent-sdk -->Claude Agent SDK<!-- name:end -->）は、Claude Code の本体を自分のプログラムの中から動かすためのライブラリである。対話の Claude Code では人が画面の前にいて、確認に答え、設定を目で見ている。ライブラリで呼ぶと、その人がいない。だから、読み込ませるもの、許すもの、課金の経路を、コードの側で決めることになる。

## Claude Code と同じもの・違うもの {#same-and-different}

Agent SDK が Claude Code と共有するのは、組み込みの道具、エージェントのループ、文脈の管理である。フック・サブエージェント・MCP・権限・セッション・スキル・プラグインも、ライブラリの側から使える。`claude -p` は、この SDK を CLI の形で呼ぶものである。基本は <!-- link:begin headless-basics#minimal -->[非対話モード（claude -p）の基本 › 最小の使い方](../delegate/headless-basics.md#minimal)<!-- link:end --> に書いてある。

違うのは、動かす主体と、その場にいる人である。

| 観点 | 対話の Claude Code | Agent SDK |
| --- | --- | --- |
| 動かすもの | 人が端末で動かす | 自分のプログラムが呼ぶ |
| 承認の確認 | 画面で人が答える | 答える人がいない。コードで決める |
| 設定の読み込み | 自動で読む | 読み込む場所を、省略に頼らず指定で決める |
| 課金の経路 | ログインか API キーかを人が選ぶ | 環境の認証で決まる |

この違いが、このページの 3 つの節（設定・権限・課金）の元になっている。どれも、人が見ていないときに「縛っていない」「境界がない」状態で動き出す原因になる。原理は縛る（動ける範囲をコードと設定で決める）と、確かめる（結果を信じる前に記録で見る）である。確かめる側は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->[無人実行の結果を確かめる › 終了コードと要約だけで決めない](../verify/checking-unattended-runs.md#beyond-exit-codes)<!-- link:end --> が持ち主である。

Agent SDK を選ぶ場面は、自分のプロセスにエージェントを組み込みたいときである。ループを自分で書く形やホストさせる形との違いは <!-- link:begin sdk-comparison#comparison -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › 層ごとの比較（自分のプロセスに組み込む・Anthropic にホストさせる・CLI で動かす）](sdk-comparison.md#comparison)<!-- link:end --> で比べられる。

## 最小の使い方 {#minimal}

使い方は、面によって入口が違う。

=== "Claude Code"

    端末やスクリプトからは、`claude -p` で呼ぶ。1 回の依頼を渡して結果を受け取る形で、SDK のプログラムを書かずに済む。出力の形式と終了コードは <!-- link:begin headless-basics#output-and-exit-codes -->[非対話モード（claude -p）の基本 › 出力の形式と終了コード](../delegate/headless-basics.md#output-and-exit-codes)<!-- link:end --> を見る。

=== "API"

    Python は `claude-agent-sdk`、TypeScript は `@anthropic-ai/claude-agent-sdk` のパッケージを入れ、`query()` にプロンプトとオプションを渡す。返ってくるメッセージを順に読み、最後の結果のメッセージで成功かどうかを見る。読み込む設定・許す道具・権限モードは、省略に頼らずオプションで書く。書き方は[雛形](#templates)にある。

最小でも、最初から決めておくものが 3 つある。読み込む設定の置き場所、確認なしで許す道具、権限モードである。設定の置き場所は次の節、道具と権限モードは「権限と承認」の節で扱う。

## 読み込む設定を決める {#setting-sources}

Agent SDK が `.claude/` のどの設定を読むかは、`settingSources`（Python では `setting_sources`）で決まる。値は `user`・`project`・`local` の 3 つで、それぞれ次を読む。

- `project`：作業ディレクトリの `.claude/settings.json` とフック、CLAUDE.md と `.claude/rules/`、プロジェクトのスキル・commands・サブエージェント。
- `user`：`~/.claude/` の設定、CLAUDE.md、rules、スキル・commands・サブエージェント。
- `local`：`CLAUDE.local.md` と `.claude/settings.local.json`。

省いたときに何を読むかは、版で変わりうる。今の公式の文書が書く、省いたときの読み込みは次のとおりである。<!-- fact:begin agent-sdk-setting-sources-default -->user・project・local をすべて読む。managed policy・~/.claude.json・自動の記憶・claude.ai の MCP コネクタは settingSources と無関係に読まれる（2026-11-05 時点）<!-- fact:end -->。この挙動に頼らず、`settingSources` を毎回書く。手元で動いたものが CI やサーバーで違う動きをする原因の多くは、ここにある。ユーザー設定が本番の環境にはなく、プロジェクトのフックだけが動く、といった差である。

空の配列 `[]` を渡すと、user・project・local の設定を読まなくなる。ただし、次のものは `[]` でも読まれる。

- 管理者の設定（managed policy）。端末に置かれた管理設定と、組織の認証で取得するサーバー管理の設定がある。
- `~/.claude.json` のグローバルな設定。
- `~/.claude/projects/` の下の自動の記憶。
- claude.ai にログインしているときの、claude.ai の MCP コネクタ。

別の利用者の依頼を 1 つのプロセスで扱う仕組みでは、既定のオプションを隔離の手段にしてはいけない。利用者ごとにファイルシステムを分け、`settingSources: []` と自動の記憶を止める環境変数を併せて渡す。公式の文書もこの形を勧めている。形は[雛形](#templates)の TypeScript にある。

CLI 側で同じ目的に使うのは `--bare` である。読み込まないものは <!-- link:begin bare-mode#what-is-skipped -->[--bare と再現性 › 読み込まないもの](../delegate/bare-mode.md#what-is-skipped)<!-- link:end --> にある。

フックは 2 通りで入れられる。設定ファイルに書いたシェルのフックは、`settingSources` が読む場所にあるときだけ動く。プログラムのコールバックとして渡すフックは、自分のプロセスの中で動き、構造のある判断を返せる。どちらもサブエージェントの中で動く。止める規則のコールバックには、コールバック自体が失敗したときに素通りせず止める側へ倒す指定（`onFailure: "block"`）がある。Python でも使えるかと、入った版は、公式の文書で確かめる。イベントの選び方は <!-- link:begin hooks-basics#when -->[フックの考え方とイベント › 使いどころ](../enforce/hooks-basics.md#when)<!-- link:end --> が持つ。

## 権限と承認 {#permissions}

自律に任せる幅を広げる前に、守りを先に決める。無人の呼び出しには、承認に答える人がいないからである。次の順で整える。

1. 道具の許可と拒否を、ルールで決める。拒否は先に評価される。評価の順番は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end --> にある。
2. 子プロセスにはルールが効かないので、コマンドの読み書きと通信は OS の層で囲む。囲える範囲は <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> を見る。
3. 秘密は作業ディレクトリと会話に置かず、二重に守る。形は <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> にある。

そのうえで、SDK 側で決めるのは、承認の要る呼び出しをどう扱うかである。承認が要る呼び出しを認める手段は、allow ルール、フック、`canUseTool` のコールバック、`--permission-prompt-tool` のいずれかである。認めていないものは拒まれる。

権限モードを決めない実行の既定と、承認の要る呼び出しの扱いは、版で変わってきた。今の既定の開始モードは <!-- fact:begin permission-mode-default-noninteractive -->Manual（Claude Code 2.1.302 以降。承認の要る呼び出しは、allow ルール・フック・canUseTool・--permission-prompt-tool で認めない限り拒否）（2026-11-04 時点）<!-- fact:end --> である。この変化があるので、権限モードを毎回オプションで書く。今の挙動は <!-- link:begin headless-basics#permissions -->[非対話モード（claude -p）の基本 › 許可と権限モード](../delegate/headless-basics.md#permissions)<!-- link:end --> と公式の文書で確かめる。

`allowed_tools`（TypeScript は `allowedTools`）は、確認なしで使わせる道具の一覧である。使わせたくない道具を確実に止める手段は、deny ルールかフックである。フックのコールバックは、`permissionDecision` を `deny` にして理由を返すと止められ、理由は Claude に道具の結果として渡る。

!!! example "判断例：夜間に回すレポート生成"
    - **状況**：社内のリポジトリの変更をまとめるレポートを、夜間にプログラムから Agent SDK で生成させる。
    - **迷う候補**：権限モードを緩めて全部の道具を確認なしで許す案と、許す道具を読み取りに絞って書く場所を囲む案。
    - **選んだもの**：許す道具を読み取りの道具に絞り、書き込みが要る作業は別の実行に分ける。
    - **理由**：夜間は誰も見ておらず、緩めた権限で間違いが起きても止める人がいない。読み取りだけの実行なら、最悪でも結果が悪いだけで済む。結果は終了コードだけでなく、出力と記録で翌朝に確かめる。

## 課金の経路 {#billing}

Agent SDK の利用が何に課金されるかは、プログラムを動かす環境の認証で決まる。コードの書き方では決まらない。

- 環境に `ANTHROPIC_API_KEY` があれば、`claude -p` と同じく、その鍵が使われる。鍵の組織に API の従量の料金がかかり、プランの利用量は使われない。
- 鍵がなく、サブスクリプションでログインしていれば、プランの利用上限から引かれる。
- 経路が決まる順は <!-- link:begin check-billing-path#how-the-path-is-chosen -->[課金の経路を確かめる（API キーとサブスクリプション） › 経路が決まる順](../cost/check-billing-path.md#how-the-path-is-chosen)<!-- link:end -->、鍵があるときの落とし穴は <!-- link:begin check-billing-path#api-key-in-env -->[課金の経路を確かめる（API キーとサブスクリプション） › API キーの環境変数があるとき](../cost/check-billing-path.md#api-key-in-env)<!-- link:end -->、今の経路の確かめ方は <!-- link:begin check-billing-path#check-current-path -->[課金の経路を確かめる（API キーとサブスクリプション） › 今の経路を確かめる](../cost/check-billing-path.md#check-current-path)<!-- link:end --> が持つ。

シェルの設定ファイルに鍵を書いたまま忘れ、プランの範囲で使うつもりが従量課金になる、というのが典型である。無人で回す前に、経路を確かめる。

プランによっては、月ごとの API credits が付く。紐付けた組織の API キーで動かした Agent SDK の利用は対象で、対話の Claude Code は対象外である。額と条件は <!-- link:begin check-billing-path#monthly-api-credits -->[課金の経路を確かめる（API キーとサブスクリプション） › プランに付く API credits](../cost/check-billing-path.md#monthly-api-credits)<!-- link:end --> を見る。

製品として他の人に使わせるときは、制約がある。第三者の開発者が、自分の製品で claude.ai のログインやプランの利用枠を提供することは、承認がない限り認められていない（公式の文書）。他の人に使わせる仕組みでは、API キーで動かす形を前提にする。

## 雛形 {#templates}

Agent SDK を呼ぶ最小の形を 2 つ置く。どちらも認証は環境に任せ、コードに鍵を書かない。動作の確かめは自分の環境で行う。

最初は Python の例で、読み込む設定・許す道具・権限モードを明示する。

<!-- gen:begin snippet agent-sdk-basics/explicit-options -->
<!-- textlint-disable -->

??? example "雛形：読み込む設定と権限を明示して呼ぶ（Python）"

    ```python
    # Agent SDK を呼ぶとき、読み込む設定・許す道具・権限モードを省略に頼らず書く
    # 認証は環境に任せる。コードにも設定にも API キーを書かない
    import asyncio

    from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query


    async def main() -> None:
        options = ClaudeAgentOptions(
            cwd="/path/to/workdir",  # 作業ディレクトリ。project の設定はここから探す
            setting_sources=["project"],  # 読み込む設定の置き場を明示する（user・local は読まない）
            allowed_tools=["Read", "Grep", "Glob"],  # 確認なしで使わせる道具。読み取りだけ
            permission_mode="default",  # 権限モードも明示する
        )
        async for message in query(prompt="src/ の構成を要約して", options=options):
            if isinstance(message, ResultMessage):
                # subtype が success 以外のときは、結果を信じる前に原因を見る
                print(message.subtype)
                print(message.result)


    asyncio.run(main())
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet agent-sdk-basics/explicit-options -->

次は TypeScript の例で、手元の設定を読み込まない形である。別の利用者の依頼を扱う仕組みの出発点になる。

<!-- gen:begin snippet agent-sdk-basics/isolated-run -->
<!-- textlint-disable -->

??? example "雛形：手元の設定を読み込まずに呼ぶ（TypeScript）"

    ```typescript
    // 手元の設定を読み込まない形で Agent SDK を呼ぶ（別の利用者の依頼を処理する仕組みなどの出発点）
    // 認証は環境に任せる。コードにも設定にも API キーを書かない
    import { query } from "@anthropic-ai/claude-agent-sdk";

    for await (const message of query({
      prompt: "README.md を読んで、使い方を 3 行で要約して",
      options: {
        cwd: "/path/to/isolated-workdir",
        settingSources: [], // user・project・local の設定を読まない
        allowedTools: ["Read"], // 読み取りだけを確認なしで許す
        permissionMode: "default",
        env: {
          ...process.env,
          CLAUDE_CODE_DISABLE_AUTO_MEMORY: "1", // 自動の記憶は settingSources の外で読まれる
        },
      },
    })) {
      if (message.type === "result") {
        console.log(message.subtype);
        if (message.subtype === "success") console.log(message.result);
      }
    }
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet agent-sdk-basics/isolated-run -->

## 効かない場面・落とし穴 {#pitfalls}

- **設定の読み込みを省略に任せる**：実行する環境で読み込まれるものが変わる。毎回 `settingSources` を書く。
- **`settingSources: []` を完全な隔離だと思う**：管理者の設定、グローバルな設定、自動の記憶などは読まれる。完全な隔離には、ファイルシステムを分ける。
- **知らないフォルダで動かす**：`--bare` なしの `-p` は、知らないフォルダでも、そこの設定のフックを実行する。SDK で同じ動きになるかは未確認。扱いは <!-- link:begin headless-basics#untrusted-folders -->[非対話モード（claude -p）の基本 › 知らないフォルダで動かすとき](../delegate/headless-basics.md#untrusted-folders)<!-- link:end --> を見る。
- **スキルをコードで登録しようとする**：スキルはファイルとして置くものである。使うには `settingSources` で読む場所を指定する。
- **終了コードや「成功」の表示で済ませる**：結果は出力・記録・差分で確かめる。
- **長く動かして文脈が溢れる**：要約や外部の記憶の組み合わせは <!-- link:begin long-running-agent-context#three-tools -->[長時間エージェントのコンテキスト管理 › 三つの手段（compaction・context editing・memory tool）](long-running-agent-context.md#three-tools)<!-- link:end --> を見る。
- **Windows と IDE 拡張**：このページの動作は WSL・Linux の CLI を基準にしている。ほかの OS と IDE 拡張の動作は未確認である。

## 比べる相手 {#compare}

選ぶ基準は、ループを誰が回し、どこで動かすかである。自分のプロセスに組み込むなら Agent SDK、API を直接呼んで自分でループを書くなら Client SDK、Anthropic にホストさせるなら Managed Agents である。表は <!-- link:begin sdk-comparison#comparison -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › 層ごとの比較（自分のプロセスに組み込む・Anthropic にホストさせる・CLI で動かす）](sdk-comparison.md#comparison)<!-- link:end -->、ホストさせる形は <!-- link:begin sdk-comparison#managed-agents -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › Managed Agents（Anthropic がループと環境を持つ）](sdk-comparison.md#managed-agents)<!-- link:end -->、組み合わせ方は <!-- link:begin sdk-comparison#combine -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › 組み合わせ方](sdk-comparison.md#combine)<!-- link:end --> が持つ。

端末やスクリプトから 1 回だけ呼ぶなら、`claude -p` で足りる。その基本は <!-- link:begin headless-basics -->[非対話モード（claude -p）の基本](../delegate/headless-basics.md)<!-- link:end -->、GitHub のイベントから動かすなら <!-- link:begin github-actions-with-claude#modes -->[GitHub Actions と @claude › 呼ばれて動く形と、イベントで動く形](../delegate/github-actions-with-claude.md#modes)<!-- link:end --> を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)：Anthropic・英語・確認日 2026-11-04
- [Migrate to Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/migration-guide)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code features in the SDK](https://code.claude.com/docs/en/agent-sdk/claude-code-features)：Anthropic・英語・確認日 2026-11-04
- [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)：Anthropic・英語・確認日 2026-11-04
- [Monthly API credits for Max, Ultra, and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)：Anthropic・英語・確認日 2026-11-04
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [Client SDK・Agent SDK・Managed Agents・CLI の比較](sdk-comparison.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)

**関連**

- [非対話モード（claude -p）の基本](../delegate/headless-basics.md)
- [--bare と再現性](../delegate/bare-mode.md)
- [フックの考え方とイベント](../enforce/hooks-basics.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [課金の経路を確かめる（API キーとサブスクリプション）](../cost/check-billing-path.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [GitHub Actions と @claude](../delegate/github-actions-with-claude.md)
- [長時間エージェントのコンテキスト管理](long-running-agent-context.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
