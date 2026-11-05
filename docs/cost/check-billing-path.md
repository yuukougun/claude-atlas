---
id: check-billing-path
title: 課金の経路を確かめる（API キーとサブスクリプション）
nav_title: 課金の経路を確かめる
aliases: [ANTHROPIC_API_KEY, API キーの課金, サブスクリプションで使う, 認証の優先順位, API credits]
type: concept
field: cost
chapter: 課金の経路と API
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code, api]
principle: [確かめる]
prevents: [合っていない]
pitfalls: []
summary: Claude Code がプランと API キーのどちらで課金されているかを確かめ、思わぬ従量課金を防げる。環境変数・起動の仕方・面で経路が変わるので、無人で回す前に確かめる。
signs:
  - {type: symptom, text: サブスクリプションで使っているつもりが、API の請求が来た}
  - {type: goal, text: スクリプトから動かすとき、どの支払いで動くのか確かめたい}
  - {type: situation, text: プランに付く API credits を Claude Code で使えるのか分からない}
prerequisites: [how-usage-limits-work]
related: [headless-basics#billing-path, bare-mode#authentication, agent-sdk-basics#billing, protecting-secrets, usage-credits-basics#vs-api-credits, reading-api-pricing, settings-layers, sdk-comparison, github-actions-with-claude, via-cloud-providers]
tracks: [headless, agent-sdk, api-credits]
outdated_advice: []
sources: [cc-docs-authentication, hc-claude-code-plan, hc-agent-sdk-plan, hc-api-credits, cc-docs-headless, cc-docs-cli-reference, cc-docs-agent-sdk-overview]
volatility: 高
sections:
  - {title: 経路が決まる順, anchor: how-the-path-is-chosen}
  - {title: API キーの環境変数があるとき, anchor: api-key-in-env}
  - {title: 今の経路を確かめる, anchor: check-current-path}
  - {title: プランに付く API credits, anchor: monthly-api-credits}
  - {title: どの原因に関わるか, anchor: cause}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：Claude Code の課金先がプランか API キーかは、環境変数・起動の仕方・面で決まり、`/status` と起動前の確認で確かめられる。
    - **いつ引くか**：サブスクリプションで使っているつもりが API の請求が来たとき。スクリプトから動かす前に、どの支払いで動くのか確かめたいとき。プランに付く API credits を Claude Code で使えるのか分からないとき。
    - **前提**：<!-- link:begin how-usage-limits-work -->[利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)<!-- link:end -->

<!-- textlint-disable -->
別名：ANTHROPIC_API_KEY・API キーの課金・サブスクリプションで使う・認証の優先順位・API credits
<!-- textlint-enable -->

課金の経路とは、Claude Code の 1 回の利用を、どこに請求するかを決める認証の道筋である。行き先は 2 つあり、プランの利用枠か、API キーを持つ Console の組織への従量課金である。プランで `/login` していても、環境変数に API キーが残っていれば、経路は API の側へ移る。

## 経路が決まる順 {#how-the-path-is-chosen}

Claude Code は、使える認証が複数あるとき、決まった順で 1 つを選ぶ。順は公式文書の Authentication にあり、2026-11-04 に確かめた（[Authentication](https://code.claude.com/docs/en/authentication)）。上にあるものが勝つ。

1. クラウドの提供元の指定（`CLAUDE_CODE_USE_BEDROCK` など）
2. `ANTHROPIC_AUTH_TOKEN`
3. `ANTHROPIC_API_KEY`
4. `apiKeyHelper`
5. `CLAUDE_CODE_OAUTH_TOKEN`（`claude setup-token` で作る長期の token。サブスクリプションで認証する）
6. Anthropic の profile と federation
7. `/login` で入ったサブスクリプション

プランで `/login` した状態は、いちばん下にある。つまり「ログインしているから、プランから引かれる」とは言えない。上の 6 つのどれかが生きていれば、そちらが選ばれる。社内の gateway にサインインしたセッションは、この順の外で最も強い。

課金先は、選ばれた認証で決まる。

- 3 は、その鍵を持つ Console の組織への API の従量課金になる
- 5 と 7 は、サブスクリプションの側になる
- 1 は提供元のクラウドの契約の側になる。扱いは <!-- link:begin via-cloud-providers -->Bedrock・Vertex AI・Foundry 経由で使う<!-- link:end --> にある
- 2 と 4 の課金先は、この辞典では確かめていない。鍵や token を出す側の仕組みで決まるので、使う前にその仕組みの持ち主に確かめる

## API キーの環境変数があるとき {#api-key-in-env}

`ANTHROPIC_API_KEY` が環境にあると、Claude Code はプランではなくその鍵で認証し、API の料金で課金される。サブスクリプションでログインしていても同じで、プランの利用量は使われない（[Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)）。

起動の仕方で、鍵の扱いは変わる。

| 起動の仕方 | 鍵が環境にあるとき |
| --- | --- |
| 対話の `claude` | 最初に一度だけ、その鍵を使うかを聞かれ、答えは記憶される。後から変えるには `/config` の「Use custom API key」を使う（変数があるときだけ出る） |
| `claude -p` | 変数があれば、確認なしで必ずその鍵を使う |
| `claude -p --bare` | サブスクリプションの OAuth も keychain も読まない。API の側の認証（`ANTHROPIC_API_KEY` か `apiKeyHelper`）が前提になる |
| Agent SDK を鍵で動かす | API の課金になる |
| VS Code の拡張・GitHub Actions | CLI を包む面なので、`ANTHROPIC_API_KEY` などの環境の認証情報が効く |
| Claude Desktop・クラウドのセッション | 環境の鍵を読まず、OAuth を使う。環境に鍵を置いても、サブスクリプションの認証が使われる |

この表は WSL・Linux の CLI を基準に、公式文書で確かめた挙動をまとめたものである（[Authentication](https://code.claude.com/docs/en/authentication)）。VS Code の拡張など、ほかの面の細かい動作は未確認である。`--bare` の詳しい挙動は <!-- link:begin bare-mode#authentication -->[--bare と再現性 › 認証が変わる（サブスクリプションで使うとき）](../delegate/bare-mode.md#authentication)<!-- link:end --> が扱う。

落とし穴は、鍵をシェルの設定ファイルに書いたまま忘れることである。対話では最初の確認で気づけても、`-p` には確認がない。cron や CI から動かすスクリプトは、人が画面を見ていない。気づく機会がないまま、従量課金が積み上がる。任せる幅を広げる話なので、次の節の確認を先に済ませる。

管理者が `forceLoginOrgUUID` や `forceLoginMethod` を設定している組織では、環境の鍵で始まるセッションが起動の時点で止められる。止められたときは、鍵を外す側を直す。

!!! example "判断例：夜間のスクリプトを、鍵を残したまま回すか"
    - **状況**：手元の WSL で、シェルの設定ファイルに `ANTHROPIC_API_KEY` を置いたまま、夜間に `claude -p` のスクリプトを回したい。普段の対話はプランで使っている。
    - **迷う候補**：A は鍵を残し、API の従量で回す。B は鍵を外し、プランの利用枠で回す。
    - **選んだもの**：B。その実行だけ `env -u ANTHROPIC_API_KEY claude -p "..."` で鍵を外して動かし、今の経路を確かめてから回す。
    - **理由**：A も筋は通るが、使った量がそのまま請求に変わり、止まる場所が上限ではなく予算になる。B は上限に当たれば止まる。ただし B は、日中の対話と同じ利用枠を使う（枠の共有は <!-- link:begin how-usage-limits-work#shared-limit -->[利用上限の仕組み（面をまたいで共有する枠） › 面をまたいで一つの枠](how-usage-limits-work.md#shared-limit)<!-- link:end --> を見る）。A を選ぶなら、先に費用の見当と止まる上限を決める（<!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](../delegate/headless-basics.md#limits)<!-- link:end --> と <!-- link:begin reading-api-pricing#claude-code-on-api -->API 料金の読み方<!-- link:end --> を使う）。

## 今の経路を確かめる {#check-current-path}

確かめる場所は 3 つある。起動の前、起動した直後、無人で回す直前である。

1. **起動の前に、環境を見る**：`ANTHROPIC_API_KEY` などの変数が設定されているか、`apiKeyHelper` を書いた設定ファイルがないかを見る。見るのは有無だけで、値は出さない。後述の雛形がこれをやる。
2. **起動した直後に、対話で `/status` を打つ**：今の認証の方式が出る。両方が有効なときは、使っていない方に印が付く。起動のときに鍵が見つかれば確認が出て、両方が有効ならログインの後に通知も出る。
3. **無人で回す直前に、手順 1 の環境の点検を毎回通す**：`-p` には確認がないので、スクリプトの先頭で環境を点検し、API 側の設定が見つかったら止める。

変数の値を `echo` や `env` で画面に出して確かめない。鍵の値が画面とログに残る。会話に貼れば、手元の記録にも平文で残る。守り方は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> にある。層をまたいで設定が効いているかは、<!-- link:begin settings-layers#verify -->[設定ファイルの階層と優先順位 › 効いているかを確かめる](../cli/settings-layers.md#verify)<!-- link:end --> の手順で確かめる。

<!-- gen:begin snippet check-billing-path/check-no-api-key -->
<!-- textlint-disable -->

??? example "雛形：claude -p の前に、API キーの設定が残っていないか確かめるスクリプト"

    ```bash
    #!/usr/bin/env bash
    # claude -p を動かす前に、API 側の課金になりうる設定が残っていないかを確かめる。
    # 変数の値は画面にもログにも出さない（有無と、見つかったファイル名だけを出す）。
    # 使い方：./check-no-api-key.sh && claude -p "..."
    set -u

    found=0

    # 1. 環境変数（値は読まず、設定されているかだけを見る）
    for name in ANTHROPIC_API_KEY ANTHROPIC_AUTH_TOKEN CLAUDE_CODE_USE_BEDROCK; do
      if [ -n "${!name:-}" ]; then
        echo "設定あり：$name（値は表示しない）"
        found=1
      fi
    done

    # 2. apiKeyHelper を書いた設定ファイル（-l でファイル名だけを出す）
    for f in "$HOME/.claude/settings.json" .claude/settings.json .claude/settings.local.json; do
      if [ -f "$f" ] && grep -q 'apiKeyHelper' "$f"; then
        echo "apiKeyHelper あり：$f"
        found=1
      fi
    done

    # 3. シェルの設定ファイルに書いたままになっていないか（-l でファイル名だけを出す）
    for f in "$HOME/.bashrc" "$HOME/.zshrc" "$HOME/.profile"; do
      if [ -f "$f" ] && grep -q 'ANTHROPIC_API_KEY' "$f"; then
        echo "シェルの設定に記述あり：$f"
        found=1
      fi
    done

    if [ "$found" -eq 1 ]; then
      echo "API 側の課金になりうる設定がある。意図したものでなければ外してから動かす。"
      exit 1
    fi
    echo "環境変数と設定ファイルに、API 側の認証は見つからなかった。"
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet check-billing-path/check-no-api-key -->

この雛形は、API 側の課金になりうる設定を見つけると終了コード 1 で止まる。`./check-no-api-key.sh && claude -p "..."` のようにつなげば、見つかった実行は始まらない。偽の値で試し、本物の鍵では試さない。

意図して鍵を使うなら、見つかって止まるのは正しい動きである。そのときは、止めるのではなく、請求先の Console の組織と、止まる上限を決めてから回す。

## プランに付く API credits {#monthly-api-credits}

プランによっては、月ごとに Claude Platform のクレジット（API credits）が付く。これは Claude Code の対話の利用には使えない。

使えるのは、次の 4 つである（[Monthly API credits](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)）。

- Claude API（Messages と Message Batches）
- Console の Playground
- Claude Managed Agents
- Agent SDK

対象のプランと月の額は、時期で変わるので本文に書かない。今の対象は上の記事で確かめる。受け取るには、claude.ai で Console の組織を 1 つ結ぶ。結んだ組織は自分では変えられない。

`claude -p` と Agent SDK は、どの認証で動かすかで扱いが分かれる。

| 動かし方 | 引かれるもの |
| --- | --- |
| 結んだ組織の API キーで、自分で動かす | Agent SDK の利用として、API credits が使われる |
| プランでログインして動かす | プランの利用上限から引かれる。API credits は使われない |
| GitHub Action・IDE 拡張・Desktop から起動する | `-p` でも Claude Code の利用として扱われ、API credits の対象外 |

プランでログインした場合の扱いは、公式の記事にもある（[Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)）。

使える範囲の外が、次のとおり混ざりやすい。

- 対話の Claude Code（端末・IDE・Desktop・web）には使えない
- プランの上限を超えた分を従量で続ける usage credits とは別物である。そちらは <!-- link:begin usage-credits-basics#vs-api-credits -->[usage credits（上限を超えた分の従量課金） › API credits との違い](usage-credits-basics.md#vs-api-credits)<!-- link:end --> にある
- Bedrock・Vertex AI・Foundry 経由の Claude には使えない
- 繰り越されない。期末に失効する
- 使い切って他に credits がなければ API は止まる。プランに請求が回ることはない

API credits で検証や自動化を動かすには、API キーが要る。つまり、API credits を使う経路と、思わぬ従量課金の経路は、同じ `ANTHROPIC_API_KEY` を通る。キーを置くのは、どの組織のどの予算で動かすかを決めた実行に限る。API の料金の読み方は <!-- link:begin reading-api-pricing#price-components -->API 料金の読み方<!-- link:end --> にある。

## どの原因に関わるか {#cause}

このページの仕組みは、6 つの原因（<!-- link:begin six-causes -->[失敗の二つの軸と診断の入口](../start/six-causes.md)<!-- link:end -->）のうち「合っていない」に関わる。想定した課金先と、実際に選ばれた経路が合っていないと、思わぬ請求が出る。

4 つの原理（<!-- link:begin four-principles -->[四つの原理と比例則（見せる・確かめる・縛る・握る）](../start/four-principles.md)<!-- link:end -->）では「確かめる」に当たる。無人で回す前に経路を確かめるのは、任せる幅を広げる前に置く守りである。確かめずに任せると、ずれは請求書で初めて見える。

## よくある誤解 {#misconceptions}

- **プランで `/login` しているから、プランから引かれる**：引かれない場合がある。順の上位に鍵や提供元の指定があれば、そちらが選ばれる。順は節「経路が決まる順」にある。
- **対話では確認が出たのだから、`-p` でも確認が出る**：出ない。`-p` は変数があれば確認なしにその鍵を使う。
- **API credits があるので、対話の Claude Code の分も払われる**：払われない。使える範囲は節「プランに付く API credits」の一覧にある。
- **プランでログインした `-p` や Agent SDK は、API credits を使う**：使わない。プランの利用上限から引かれる。
- **Desktop やクラウドのセッションに鍵を置けば、API で課金される**：置いても読まれない。OAuth のサブスクリプションが使われる。
- **自作のツールで、利用者に claude.ai のログインを使わせてよい**：許可がなければ認められていない。第三者の開発者が自分の製品で claude.ai のログインや利用枠を提供することは、Agent SDK の公式文書が許可なしには認めていない（[Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)）。Agent SDK 側の整理は <!-- link:begin agent-sdk-basics#billing -->[Agent SDK（Claude Code をライブラリとして使う） › 課金の経路](../api/agent-sdk-basics.md#billing)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Authentication](https://code.claude.com/docs/en/authentication)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)：Anthropic・英語・確認日 2026-11-04
- [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)：Anthropic・英語・確認日 2026-11-04
- [Monthly API credits for Max, Ultra, and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)：Anthropic・英語・確認日 2026-11-04
- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04
- [CLI reference](https://code.claude.com/docs/en/cli-reference)：Anthropic・英語・確認日 2026-11-04
- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)

**関連**

- [非対話モード（claude -p）の基本 › 課金の経路（API キーがあるとき）](../delegate/headless-basics.md#billing-path)
- [--bare と再現性 › 認証が変わる（サブスクリプションで使うとき）](../delegate/bare-mode.md#authentication)
- [Agent SDK（Claude Code をライブラリとして使う） › 課金の経路](../api/agent-sdk-basics.md#billing)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [usage credits（上限を超えた分の従量課金） › API credits との違い](usage-credits-basics.md#vs-api-credits)
- [設定ファイルの階層と優先順位](../cli/settings-layers.md)
- [Client SDK・Agent SDK・Managed Agents・CLI の比較](../api/sdk-comparison.md)
- [GitHub Actions と @claude](../delegate/github-actions-with-claude.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
