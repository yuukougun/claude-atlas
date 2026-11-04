---
id: share-team-settings
title: チームで設定を共有する
aliases: [.claude/settings.json, 共有の設定]
type: recipe
field: team
chapter: 導入と決まり
order: 30
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
pitfalls: []
scenes: [チーム, 開発]
summary: CLAUDE.md・共有の設定・MCP の設定・プラグインをリポジトリに入れ、チームで同じ前提と縛りで Claude Code を使える。個人の好みと秘密は共有のファイルに入れない。
signs:
  - {type: goal, text: チームで同じ設定を使いたい}
  - {type: symptom, text: 人によって Claude Code の振る舞いが違う}
prerequisites: [settings-layers, permission-rules]
related: [what-to-put-in-claude-md, claude-md-length#team, agents-md, connecting-mcp, plugins-and-marketplaces, protected-paths, protecting-secrets, vetting-extensions, before-opening-unknown-repos, managed-settings-enforcement, org-managed-settings-and-mcp, rolling-out-to-teams]
tracks: [settings, claude-md, mcp, plugins, permissions]
sources: [cc-docs-settings, cc-docs-memory, cc-docs-mcp, cc-docs-permissions, cc-docs-plugins-overview]
volatility: 中
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: 共有するものと個人に残すもの, anchor: shared-vs-personal}
  - {title: 手順, anchor: steps}
  - {title: 信頼してから効く設定, anchor: after-trust}
  - {title: 全体の確かめ方, anchor: verify}
  - {title: 失敗したとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：CLAUDE.md・共有の設定・MCP の設定・プラグインをリポジトリに入れ、チームで同じ前提と縛りで Claude Code を使える。個人の好みと秘密は共有のファイルに入れない。
    - **いつ引くか**：チームで同じ設定を使いたいとき。人によって Claude Code の振る舞いが違うとき。
    - **前提**：<!-- link:begin settings-layers -->[設定ファイルの階層と優先順位](../cli/settings-layers.md)<!-- link:end -->・<!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end -->

<!-- textlint-disable -->
別名：.claude/settings.json・共有の設定
<!-- textlint-enable -->

チームで設定を共有するレシピである。リポジトリにコミットした CLAUDE.md・`.claude/settings.json`・`.mcp.json` は、そのリポジトリを開いた全員に同じ前提と縛りを配る。個人の好みと秘密は、共有のファイルから外して手元に残す。共有は便利だが、間違いも全員に同時に届く。そのため、配る前に守りを整える順で進める。

## 先に整える守り {#guards}

共有のファイルは、リポジトリを開いた全員に効く。手順へ進む前の守りとして、次の 4 つを決めておく。

- **許可の幅を最小にする**：共有の設定に入れた allow ルールは、信頼したワークスペースで全員に効く。入れるのは、全員の作業に毎回要る読み取り系とテスト系のコマンドに絞る。評価の順番とパスの書き方は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end --> と <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end --> を引く。
- **秘密を共有のファイルに入れない**：MCP の資格情報は `.mcp.json` に直接書かず、環境変数で渡す。`.env` や認証情報を読ませない二重の設定は <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> を引く。資格情報の持たせ方は <!-- link:begin connecting-mcp#credentials -->[MCP をつなぐ › 資格情報と権限](../extend/connecting-mcp.md#credentials)<!-- link:end --> にある。
- **縛りを書き換えられる場面を知る**：`.claude/` は保護されたパスで、Claude がそこへ書くときの扱いは権限モードで変わる。allow ルールでは事前に許せないが、モードによっては確認なしに通る。どのモードでどう扱われるかは <!-- link:begin protected-paths#protected -->[消せない場所・触れない場所（protected paths） › 保護される場所と、モードごとの扱い](../enforce/protected-paths.md#protected)<!-- link:end --> を引く。共有の縛りの変更は、PR で別の人が承認する運用にする。
- **入れるものの出所を確かめる**：共有する MCP サーバーとプラグインは、全員の権限で動く。入れる前の確認は <!-- link:begin vetting-extensions#guards -->[MCP・プラグイン・スキルを入れる前の確認 › 先に整える守り](../safety/vetting-extensions.md#guards)<!-- link:end --> を引く。受け取る側にとって、共有された設定やフックは「開くだけで動きうるもの」でもある。その見方は <!-- link:begin before-opening-unknown-repos#files-to-check -->[知らないリポジトリを開く前に › 開く前に見るファイル](../safety/before-opening-unknown-repos.md#files-to-check)<!-- link:end --> にある。

## 共有するものと個人に残すもの {#shared-vs-personal}

共有するのは、誰が使っても同じであるべき前提と縛りである。個人に残すのは、人によって違ってよい好みと、自分の手元だけの許可である。分けるときの基準は「そのリポジトリを開いた全員に効いてよいか」の 1 つで足りる。

| 置き場所 | 効く範囲 | 入れるもの |
| --- | --- | --- |
| `.claude/settings.json`（コミットする） | リポジトリを開いた全員 | チームの allow ルール・ask ルール・deny ルール |
| `.claude/settings.local.json`（git に入れない） | 自分だけ、そのリポジトリ | 自分だけの許可、手元の都合 |
| `~/.claude/settings.json` | 自分の全リポジトリ | 個人の好み |
| `.mcp.json`（コミットする） | リポジトリを開いた全員（初回に承認が出る） | チームで使う MCP サーバーの定義。資格情報は環境変数 |
| CLAUDE.md | リポジトリを開いた全員 | 推測できないコマンド・理由・落とし穴 |

層の優先順位と、同じキーが重なったときの扱いは <!-- link:begin settings-layers#layers -->[設定ファイルの階層と優先順位 › 層と優先順位](../cli/settings-layers.md#layers)<!-- link:end --> と <!-- link:begin settings-layers#merge -->[設定ファイルの階層と優先順位 › 合わさる設定、上書きされる設定](../cli/settings-layers.md#merge)<!-- link:end --> が持つ。この recipe で押さえるのは次の 2 点である。

- 同じキーでは、手元の `.claude/settings.local.json` が共有の `.claude/settings.json` に勝つ。
- `permissions.allow` のようなリストは層をまたいで足し合わされ、deny ルールは先に評価される。個人の allow ルールで、共有の deny ルールは外れない。

共有に入れたもののうち、強制力が違うものを並べると次のとおりである。

<!-- gen:begin compare 強制力 読み込みの時期 -->
<!-- textlint-disable -->

| 機能 | 強制力 | 読み込みの時期 |
| --- | --- | --- |
| [設定（settings.json）](../cli/settings-layers.md) | — | — |
| [CLAUDE.md](../extend/what-to-put-in-claude-md.md) | お願い | セッション開始 |
| [MCP](../extend/connecting-mcp.md) | なし | セッション開始 |
| [プラグイン（plugins）](../extend/plugins-and-marketplaces.md) | — | セッション開始と使うとき |
| [権限（permissions）](../enforce/permission-rules.md) | 鍵 | — |

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 -->

CLAUDE.md は Claude が文脈として読むお願いで、守らせる力は持たない。例外を許さない禁止は、共有の deny ルールのような鍵に移し、CLAUDE.md には理由と相談の基準だけを残す。CLAUDE.md に書く行の選び方は <!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> を引く。

!!! example "判断例：新しく要るコマンドの許可を、共有に入れるか手元に残すか"
    - **状況**：メンバーの 1 人が、ローカルの開発環境のログを見るために `docker compose logs` を毎回許可するのが面倒になった。ほかのメンバーは、まだそのコマンドを使っていない。
    - **迷う候補**：共有の `.claude/settings.json` の allow ルールに入れて全員に配る。自分の `.claude/settings.local.json` にだけ入れる。
    - **選んだもの**：自分の `.claude/settings.local.json` にだけ入れる。
    - **理由**：共有の allow ルールは、リポジトリを開いた全員に効く。全員の作業に毎回要るとまだ言えないので、全員に配る理由がない。ほかの人も使うと分かったら、PR で出して別の人が承認してから共有に移す。

## 手順 {#steps}

既に個人の設定で動いている状態から、共有の設定へ移す手順である。各段に、終わりの確かめを付ける。

1. **いまの層を見る**：セッションで `/status` を開き、`Setting sources` で読み込まれているファイルを見る。個人の `~/.claude/settings.json` にある設定のうち、チームに要るものを書き出す。確かめ：読み込まれた層の一覧が出る。
2. **チームの縛りを共有に書く**：手順の下にある共有用の雛形を `.claude/settings.json` に置く。許可は最小にし、`git push` は ask ルールに、秘密のファイルは deny ルールにする。確かめ：新しいセッションで、許可したコマンドが通り、deny の対象が止まる。
3. **個人の分を手元に残す**：自分だけの許可は、手順の下にある手元用の雛形のように、`.claude/settings.local.json` へ置く。確かめ：`git status` に出ない。出るなら `.gitignore` に足す。
4. **MCP の定義を `.mcp.json` に置く**：チームで使うサーバーだけを、環境変数で資格情報を渡す形で書く。スコープの選び方と共有の範囲は <!-- link:begin connecting-mcp#scopes -->[MCP をつなぐ › スコープと共有](../extend/connecting-mcp.md#scopes)<!-- link:end --> を引く。確かめ：別の人が開くと、初回に承認が出る。
5. **CLAUDE.md に前提を書く**：ビルドとテストのコマンド、守る理由、落とし穴を書く。育て方と見直しは <!-- link:begin claude-md-length#team -->[CLAUDE.md の長さと剪定 › チームで育てる](../extend/claude-md-length.md#team)<!-- link:end --> を引く。ほかのエージェントツールも使うチームは <!-- link:begin agents-md -->AGENTS.md とほかのツールとの共有（準備中）<!-- link:end --> で指示を共有する。確かめ：新しいセッションで、Claude がコマンドを聞かずに実行できる。
6. **プラグインを共有する**：チーム専用のマーケットプレイスを作るかは <!-- link:begin plugins-and-marketplaces#team-marketplace -->[プラグインとマーケットプレイス › チームのマーケットプレイスを作る](../extend/plugins-and-marketplaces.md#team-marketplace)<!-- link:end --> を引く。入れたものは使わないときも説明が常駐するので、全員に要るものだけに絞る。入れる前の確認は <!-- link:begin plugins-and-marketplaces#before-install -->[プラグインとマーケットプレイス › 入れる前の確認](../extend/plugins-and-marketplaces.md#before-install)<!-- link:end --> にある。確かめ：別の人の環境で、有効になったものの一覧が自分と合う。
7. **PR で入れる**：共有のファイルの追加は、別の人がレビューして承認する。確かめ：新しく clone した環境で、次の確かめ方を一通り流す。

共有の `.claude/settings.json` の雛形である。

<!-- gen:begin snippet share-team-settings/shared-settings -->
<!-- textlint-disable -->

??? example "雛形：チームで共有する .claude/settings.json（許可は最小、読ませないものは deny）"

    ```json
    {
      "$schema": "https://json.schemastore.org/claude-code-settings.json",
      "permissions": {
        "allow": [
          "Bash(npm run test *)",
          "Bash(npm run lint *)",
          "Bash(git status)",
          "Bash(git diff *)"
        ],
        "ask": [
          "Bash(git push *)"
        ],
        "deny": [
          "Read(**/.env)",
          "Read(**/.env.*)"
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet share-team-settings/shared-settings -->

自分だけの許可を置く、手元の `.claude/settings.local.json` の雛形である。

<!-- gen:begin snippet share-team-settings/local-settings -->
<!-- textlint-disable -->

??? example "雛形：自分だけの許可を置く .claude/settings.local.json"

    ```json
    {
      "permissions": {
        "allow": [
          "Bash(docker compose logs *)",
          "Bash(make dev *)"
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet share-team-settings/local-settings -->

## 信頼してから効く設定 {#after-trust}

共有の `.claude/settings.json` の設定は、すべてが開いた直後から効くわけではない。効く時期は種類で違う。

- **deny ルールと ask ルール**：すぐ効く。
- **allow ルールと `env`**：ワークスペースを信頼した後に効く。信頼する前のセッションでは、共有の allow ルールがあっても確認が出る。
- **`permissions.defaultMode` の `auto` と `bypassPermissions`**：project の層でも local の層でも無効である。共有のファイルで、全員の権限モードを緩めることはできない。設定できるのは user の層か managed の層だけである。

信頼の前後で何が効くかの詳細は <!-- link:begin permission-rules#workspace-trust -->[権限ルール（allow・ask・deny） › 信頼の前に効くもの・後に効くもの](../enforce/permission-rules.md#workspace-trust)<!-- link:end --> を引く。新しく clone した人が「共有の許可が効かない」と言うときは、まず信頼の確認を通したかを聞く。

もう 1 つ、層の読み込みにも限りがある。クラウドセッションは user と local の設定を読まない。手元の `.claude/settings.local.json` にだけ置いた許可は、クラウドでは効かない。クラウドでも要る設定は、共有の `.claude/settings.json` へ置く。

## 全体の確かめ方 {#verify}

共有を終えたら、設定を書いた本人の環境ではなく、新しく clone した環境か別の人の環境で確かめる。書いた本人の環境には個人の設定が混ざっていて、共有だけで動くかが分からないためである。

1. **層を見る**：`/status` の `Setting sources` に、共有の `.claude/settings.json` が出る。手元の層が不意に上書きしていないかも、ここで見る。見方は <!-- link:begin settings-layers#verify -->[設定ファイルの階層と優先順位 › 効いているかを確かめる](../cli/settings-layers.md#verify)<!-- link:end --> にある。
2. **拒否されたエントリを見る**：シェルで `claude doctor` を流し、拒否された設定がないかを見る。
3. **縛りを偽の秘密で試す**：壊れても困らないリポジトリで偽の `.env` を置き、読ませる依頼を出して止まるかを見る。手順は <!-- link:begin protecting-secrets#verify -->[秘密情報（.env・API キー）を守る › 偽の秘密で確かめる](../safety/protecting-secrets.md#verify)<!-- link:end --> にある。
4. **MCP を見る**：初回の承認が出て、サーバーのツールが使える。

## 失敗したとき {#when-it-fails}

人によって振る舞いが違うときは、どの層の差かを `/status` で切り分ける。

- **同じキーの値が人によって違う**：手元の `.claude/settings.local.json` か `~/.claude/settings.json` が上書きしている。優先順位は <!-- link:begin settings-layers#layers -->[設定ファイルの階層と優先順位 › 層と優先順位](../cli/settings-layers.md#layers)<!-- link:end --> を引く。
- **共有の allow ルールが効かず、確認が出る**：ワークスペースの信頼を通していない。または、パスの書き方が何にも当たっていない。<!-- link:begin permission-rules#workspace-trust -->[権限ルール（allow・ask・deny） › 信頼の前に効くもの・後に効くもの](../enforce/permission-rules.md#workspace-trust)<!-- link:end --> と <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end --> を引く。
- **MCP のツールが出てこない**：<!-- link:begin connecting-mcp#troubleshooting -->[MCP をつなぐ › つながらない・ツールが出てこないとき](../extend/connecting-mcp.md#troubleshooting)<!-- link:end --> で切り分ける。
- **組織の管理設定に負ける、または外せない規則を作りたい**：managed の層は最上位で、利用者の設定では外せない。優先の順番は <!-- link:begin managed-settings-enforcement#precedence -->管理設定と組織の強制 › 優先の順番（準備中）<!-- link:end -->、全員に配る経路は <!-- link:begin org-managed-settings-and-mcp#delivery -->組織に設定と MCP サーバーを配る › 配る経路（準備中）<!-- link:end --> を引く。
- **CLAUDE.md の行が守られない**：お願いを鍵に移す。移し先の決め方は <!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](../extend/what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end --> を引く。
- **広め方そのものを決めたい**：<!-- link:begin rolling-out-to-teams#onboarding-guide -->チームに広める（/team-onboarding など） › 立ち上げの手引きを作る（準備中）<!-- link:end --> へ進む。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Settings files and precedence](https://code.claude.com/docs/en/settings)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Plugins overview](https://code.claude.com/docs/en/plugins/overview)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [設定ファイルの階層と優先順位](../cli/settings-layers.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)

**次に読む**

- チームに広める（/team-onboarding など）（準備中）
- 組織に設定と MCP サーバーを配る（準備中）

**関連**

- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [CLAUDE.md の長さと剪定 › チームで育てる](../extend/claude-md-length.md#team)
- AGENTS.md とほかのツールとの共有（準備中）
- [MCP をつなぐ](../extend/connecting-mcp.md)
- [プラグインとマーケットプレイス](../extend/plugins-and-marketplaces.md)
- [消せない場所・触れない場所（protected paths）](../enforce/protected-paths.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [知らないリポジトリを開く前に](../safety/before-opening-unknown-repos.md)
- 管理設定と組織の強制（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
