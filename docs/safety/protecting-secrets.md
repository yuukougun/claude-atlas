---
id: protecting-secrets
title: 秘密情報（.env・API キー）を守る
aliases: [.env を読ませない, API キーの漏洩, 認証情報を守る, 秘密の読み取りの禁止]
type: recipe
field: safety
chapter: 秘密と壊す操作
order: 140
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [縛る]
prevents: [境界がない, 縛っていない]
pitfalls: []
scenes: [開発]
summary: .env や API キー、認証情報を Claude に読ませない設定を、権限ルールとサンドボックスの二重にして作れる。会話に貼った秘密は、手元の記録に平文で残る。
signs:
  - {type: goal, text: .env や API キーを、絶対に読ませたくない}
  - {type: situation, text: 認証情報のあるマシンで、Claude Code に作業を任せる}
prerequisites: [sandboxing]
related: [secrets-exposed#first-response, permission-rules, lethal-trifecta, what-feedback-sends, where-your-data-goes, what-auto-mode-stops, hook-recipes, before-opening-unknown-repos, check-billing-path, default-safety-settings#by-stage]
tracks: [permissions, sandbox]
sources: [cc-docs-permissions, cc-docs-sandboxing, cc-docs-best-practices, cc-docs-data-usage, cc-docs-security]
volatility: 中
sections:
  - {title: 秘密を作業ディレクトリと会話に置かない, anchor: keep-out}
  - {title: 権限ルールとサンドボックスの二重にする, anchor: two-layers}
  - {title: 偽の秘密で確かめる, anchor: verify}
  - {title: 効かなかったとき, anchor: when-it-fails}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：.env や API キー、認証情報を Claude に読ませない設定を、権限ルールとサンドボックスの二重にして作れる。
    - **いつ引くか**：.env や API キーを、絶対に読ませたくないとき。認証情報のあるマシンで、Claude Code に作業を任せるとき。
    - **前提**：<!-- link:begin sandboxing -->[サンドボックスで封じ込める](../enforce/sandboxing.md)<!-- link:end -->

<!-- textlint-disable -->
別名：.env を読ませない・API キーの漏洩・認証情報を守る・秘密の読み取りの禁止
<!-- textlint-enable -->

秘密情報を守るレシピである。秘密を置かない・貼らない場所を決め、それでも手元に残る秘密を権限ルールとサンドボックスの二重で読ませなくし、偽の秘密で効いたかを確かめる。CLAUDE.md に「.env を読まない」と書く方法は、公式もほぼ守られると説明するが、「ほぼ」では足りないときは deny ルールなど、設定の側の仕組みへ移すよう勧めている。このページはその移し方である。

## 秘密を作業ディレクトリと会話に置かない {#keep-out}

秘密を守る最初の手は、Claude の手が届く場所に置かないことである。置かないものは、読ませない設定を作る前に決めておく。

- **作業ディレクトリ**：.env やトークンのファイルは、作業ディレクトリの外へ移せるなら移す。リポジトリの中に置くしかないものだけが、次の節の対象になる。
- **会話**：API キーやパスワードを会話に貼らない。貼った秘密は、手元の `~/.claude/projects/` にセッションの記録として平文で残る。残る期間と、記録がどこまで送られるかは <!-- link:begin where-your-data-goes#local-transcripts -->[送ったデータの行方（学習・保持期間） › 手元に残る記録](where-your-data-goes.md#local-transcripts)<!-- link:end --> を引く。
- **報告や共有**：`/feedback` やトランスクリプトの共有に応じると、会話とコードが送られる。秘密が会話に入った後で送る前に、<!-- link:begin what-feedback-sends#what-is-sent -->[/feedback・トランスクリプトの共有で送られるもの › 送られるものと残る期間](what-feedback-sends.md#what-is-sent)<!-- link:end --> で送られるものを確かめる。
- **環境変数とシェルの設定**：`ANTHROPIC_API_KEY` のような変数をシェルの設定ファイルに書いて忘れると、課金の経路まで変わる。詳しくは <!-- link:begin check-billing-path#api-key-in-env -->[課金の経路を確かめる（API キーとサブスクリプション） › API キーの環境変数があるとき](../cost/check-billing-path.md#api-key-in-env)<!-- link:end --> を引く。

置かないだけで足りない理由が 2 つある。作業に要る .env はリポジトリの中にあることが多い。サンドボックスの読み取りは既定でマシンのほぼ全体に及ぶので、作業ディレクトリの外に置いたホームの秘密も、明示して塞がない限り読める（<!-- link:begin sandboxing#default-reads -->[サンドボックスで封じ込める › 読み取りは既定で広い](../enforce/sandboxing.md#default-reads)<!-- link:end -->）。すでに会話へ貼ってしまった場合や、鍵を読まれたかもしれない場合は、設定を直す前に <!-- link:begin secrets-exposed#first-response -->[秘密の情報を読まれた・外に出された › まず鍵を無効にする](../symptoms/secrets-exposed.md#first-response)<!-- link:end --> へ進む。

## 権限ルールとサンドボックスの二重にする {#two-layers}

読ませない縛りを、権限ルールの deny ルールとサンドボックスの `denyRead` の二重にして作る節である。どちらか片方では、止められない読み方が残る。

- **権限ルール（Read の deny ルール）**：Claude のファイルの道具と、`cat`・`head`・`tail`・`sed`・`tee` のように Claude Code が見分けられるコマンド、リダイレクトの先に効く。`grep -r パターン .` のように名前を出さずに読むコマンドや、Python・Node のスクリプトが自分で開くファイルには効かない（<!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end -->）。
- **サンドボックス**：OS の層で、Bash のコマンドとその子プロセスの読み書きを囲う。ただし Claude のファイルの道具、MCP サーバー、フックはサンドボックスの外で動く。`denyRead` は Read の道具を止めない。
- **合わさり方**：Read の deny ルールは、サンドボックスの設定にも合わさる。プロジェクトの .env は deny ルールを 1 回書けば、道具の側とサンドボックスの側の両方で拒否される。ホームの秘密は、`denyRead` として明示して列挙する。

!!! example "判断例：deny ルールだけで足りるか"
    - **状況**：リポジトリの .env を読ませたくない。Read の deny ルールは 1 行で書ける。
    - **迷う候補**：Read の deny ルールだけにする。サンドボックスも有効にして二重にする。
    - **選んだもの**：二重にする。
    - **理由**：deny ルールだけだと、Claude が書いたスクリプトや `grep -r` が .env を開くのを止められない。サンドボックスを足せば、子プロセスの読み取りも OS の層で止まる。サンドボックスだけにしても、Read の道具は止まらない。

手順は次の 4 段である。

1. **サンドボックスを使える状態にする**。使える環境は macOS・Linux・WSL2 で、Windows のネイティブではサンドボックスなしで動く。有効にする最小の手順は <!-- link:begin sandboxing#minimal -->[サンドボックスで封じ込める › 最小の使い方](../enforce/sandboxing.md#minimal)<!-- link:end -->、WSL2 では <!-- link:begin sandboxing#linux-wsl -->[サンドボックスで封じ込める › Linux と WSL2 で使う](../enforce/sandboxing.md#linux-wsl)<!-- link:end --> を引く。終わりの確認：サンドボックスを有効にしたセッションが、エラーなしで始まる。
2. **プロジェクトの設定に deny ルールを置く**。手順の後ろに載せた 1 つ目の雛形（プロジェクト用）を `.claude/settings.json`（共有しない自分だけの設定なら `.claude/settings.local.json`）へ書く。`failIfUnavailable` は、サンドボックスを起動できないときにコマンドを通さずに止める設定である（<!-- link:begin sandboxing#fail-if-unavailable -->[サンドボックスで封じ込める › 起動できないときに通さない](../enforce/sandboxing.md#fail-if-unavailable)<!-- link:end -->）。終わりの確認：新しいセッションで、`.env` を読ませる依頼が拒否される。
3. **ユーザーの設定にホームの秘密を置く**。2 つ目の雛形（ユーザー用）を `~/.claude/settings.json` へ書く。設定の配列はスコープをまたいで合わさるので、プロジェクトの deny ルールと両方が効く。終わりの確認：拒否したディレクトリの偽のファイルを、シェルからも読めない。
4. **偽の秘密で確かめる**。次の節で、偽の秘密を使って効き方を見る。

<!-- gen:begin snippet protecting-secrets/deny-secrets-project -->
<!-- textlint-disable -->

??? example "雛形：プロジェクトの .env と secrets を、権限ルールとサンドボックスで読ませない設定"

    ```json
    {
      "permissions": {
        "deny": [
          "Read(./.env)",
          "Read(./.env.*)",
          "Read(./secrets/**)"
        ]
      },
      "sandbox": {
        "enabled": true,
        "failIfUnavailable": true
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.24。

<!-- textlint-enable -->
<!-- gen:end snippet protecting-secrets/deny-secrets-project -->

<!-- gen:begin snippet protecting-secrets/deny-secrets-user -->
<!-- textlint-disable -->

??? example "雛形：ホームの認証情報とトークンの環境変数を、全プロジェクトで読ませない設定"

    ```json
    {
      "permissions": {
        "deny": [
          "Read(~/.ssh/**)",
          "Read(~/.aws/**)"
        ]
      },
      "sandbox": {
        "enabled": true,
        "filesystem": {
          "denyRead": ["~/.ssh", "~/.aws"]
        },
        "credentials": {
          "envVars": [
            { "name": "GITHUB_TOKEN", "mode": "deny" },
            { "name": "NPM_TOKEN", "mode": "deny" }
          ]
        }
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.24。

<!-- textlint-enable -->
<!-- gen:end snippet protecting-secrets/deny-secrets-user -->

書き方に 2 つ注意する。サンドボックスのパスは `/tmp/build` が絶対パス、`~/.kube` がホームからの相対で、権限ルールの `//path`（絶対）・`/path`（プロジェクト基準）とは書き方が違う。2 つ目に、`sandbox.credentials` の `envVars` は、サンドボックスの中で動かすコマンドから、その環境変数を消す。Claude Code 自身の認証には影響しない。

権限ルールの書き方と、何にも当たらないルールの見分け方は <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end --> を引く。評価の順番は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end --> にある。deny は先に評価される。

## 偽の秘密で確かめる {#verify}

設定が効いたかを、偽の秘密だけで確かめる節である。確かめのために、本物の `.env` や `~/.ssh` を Claude へ読ませない。結果は自分の環境で確かめる必要がある。

1. 壊れても困らない作業用のリポジトリに、前の節のプロジェクトの雛形を置く。`printf 'FAKE_API_KEY=not-a-real-key\n' > .env` で、偽の .env を作る。
2. 新しいセッションを始め、「.env を読んで中身を見せて」と頼む。終わりの確認：Read の拒否で止まり、`not-a-real-key` が返らない。
3. 「シェルで `grep -r FAKE_API_KEY .` を実行して」と頼む。終わりの確認：サンドボックスの中で拒否されるか、偽の秘密の文字列が返らない。
4. 「Python で `.env` を開いて表示して」と頼む。終わりの確認：サンドボックスの中で拒否されるか、偽の秘密の文字列が返らない。
5. ホームの設定は、本物のディレクトリを使わず、作業用の偽のディレクトリ名（例：`~/fake-secrets`）に書き換えた設定で、同じ頼み方を試す。確かめ終わったら、偽のファイルと書き換えた設定を戻す。

手順 3 と 4 で中身が返るときは、サンドボックスが動いていない可能性が高い。次の節へ進む。

## 効かなかったとき {#when-it-fails}

効かない場面は、次のどれかであることが多い。

- **シェルや Python では読めてしまう**：サンドボックスが有効になっていない。`failIfUnavailable` を入れていれば、起動できない環境ではコマンドが止まるので気づける。環境の確認は <!-- link:begin sandboxing#pitfalls -->[サンドボックスで封じ込める › 効かない場面・落とし穴](../enforce/sandboxing.md#pitfalls)<!-- link:end --> を引く。Windows のネイティブでは、サンドボックスなしで動く。
- **何も拒否されない**：パスが当たっていない可能性がある。サブディレクトリの .env に当たるかは、偽の秘密で確かめる。書き方は <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end --> を引く。IDE 拡張や、WSL・Linux 以外の OS での動作は未確認である。
- **サンドボックスの外に出る道**：サンドボックスの外で動くフックや MCP サーバー、サンドボックスから外したコマンドは、秘密に届きうる。囲える範囲は <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> を引く。コマンドの文字列で止めたいときは <!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](../enforce/hook-recipes.md#block-dangerous)<!-- link:end --> が使える。
- **auto モードに任せている**：auto モードの分類器は確認を減らす仕組みで、安全を保証しない。秘密の読み取りは、分類器でなく deny ルールとサンドボックスで縛る（<!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end -->）。
- **知らないリポジトリを開いた**：リポジトリの設定ファイルが、API キーなどを外へ送る経路になった脆弱性が公表されている（修正済み）。開く前に見るものは <!-- link:begin before-opening-unknown-repos#files-to-check -->[知らないリポジトリを開く前に › 開く前に見るファイル](before-opening-unknown-repos.md#files-to-check)<!-- link:end --> を引く。
- **読まれたと疑う**：読まれた・会話に出たときは、鍵を無効にする手順が先である。<!-- link:begin secrets-exposed#first-response -->[秘密の情報を読まれた・外に出された › まず鍵を無効にする](../symptoms/secrets-exposed.md#first-response)<!-- link:end --> を引く。

読ませない縛りが効いていても、秘密と外への送信と信頼できない入力が 1 つの構成に揃うと、被害の経路は残る。揃えない考え方は <!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](lethal-trifecta.md#three-capabilities)<!-- link:end --> にある。任せる段階ごとの既定の全体は <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](default-safety-settings.md#by-stage)<!-- link:end --> が正本である。アプリの既定は <!-- link:begin default-safety-settings#defaults-by-surface -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 面ごとの既定（生成の表）](default-safety-settings.md#defaults-by-surface)<!-- link:end --> を引く。このページの設定は、Claude Code の権限ルールとサンドボックスを使うものである。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Data usage](https://code.claude.com/docs/en/data-usage)：Anthropic・英語・確認日 2026-11-04
- [Security](https://code.claude.com/docs/en/security)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [サンドボックスで封じ込める](../enforce/sandboxing.md)

**次に読む**

- GitHub Actions と @claude（準備中）

**関連**

- [秘密の情報を読まれた・外に出された › まず鍵を無効にする](../symptoms/secrets-exposed.md#first-response)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](lethal-trifecta.md)
- [/feedback・トランスクリプトの共有で送られるもの](what-feedback-sends.md)
- [送ったデータの行方（学習・保持期間）](where-your-data-goes.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [知らないリポジトリを開く前に](before-opening-unknown-repos.md)
- [課金の経路を確かめる（API キーとサブスクリプション）](../cost/check-billing-path.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](default-safety-settings.md#by-stage)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
