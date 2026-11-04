---
id: headless-basics
title: 非対話モード（claude -p）の基本
aliases: [headless, ヘッドレス, non-interactive mode, print モード]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 190
level: 回す
priority: 必須
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [境界がない, 確かめていない]
pitfalls: []
scenes: [開発]
summary: claude -p でスクリプトや CI から Claude Code を動かし、結果を決まった形式で受け取れる。無人では確認に答える人がいないので、許す道具と止まる上限を明示して渡す。
signs:
  - {type: goal, text: スクリプトや CI から Claude Code を使いたい}
  - {type: symptom, text: スクリプトから動かすと、ファイルの編集やコマンドをせずに終わる}
  - {type: symptom, text: CI では成功と出たのに、実際は何もしていなかった}
  - {type: symptom, text: サブスクリプションで使っているつもりが、API の請求が来た}
prerequisites: [five-questions-before-delegating]
related: [permission-rules, bare-mode, checking-unattended-runs, what-auto-mode-stops, where-bypass-is-ok, sandboxing, before-opening-unknown-repos, protecting-secrets, check-billing-path, what-uses-up-limits#find-what-uses-it, structured-outputs-basics, batch-and-p-loops, github-actions-with-claude, choosing-automation, sdk-comparison, agent-sdk-basics]
tracks: [headless, permission-modes]
outdated_advice: [yolo-skip-permissions]
sources: [cc-docs-headless, cc-docs-cli-reference, cc-docs-permission-modes, cc-docs-permissions, cc-changelog, hc-claude-code-plan, hc-agent-sdk-plan]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 出力の形式と終了コード, anchor: output-and-exit-codes}
  - {title: 許可と権限モード, anchor: permissions}
  - {title: 止まる上限（ターンと費用）, anchor: limits}
  - {title: 知らないフォルダで動かすとき, anchor: untrusted-folders}
  - {title: 課金の経路（API キーがあるとき）, anchor: billing-path}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：`claude -p` でスクリプトや CI から Claude Code を動かし、結果を決まった形式で受け取れる。
    - **いつ引くか**：スクリプトや CI から Claude Code を使いたいとき。動かしたのにファイルの編集やコマンドをせずに終わるとき。CI では成功と出たのに何もしていなかったとき。サブスクリプションのつもりが API の請求になったとき。
    - **強制力**：権限モードは<!-- gen:begin feature permission-modes/enforcement -->鍵<!-- gen:end feature permission-modes/enforcement -->。許す道具の列挙と権限モードは、確認に答える人がいない無人の実行でも効く。`claude -p` という起動の仕方そのものは、安全を作らない。
    - **いちばんの注意**：無人では確認に答える人がいない。許す道具と、止まる上限（ターンと費用）を、起動のたびに明示して渡す。
    - **前提**：<!-- link:begin five-questions-before-delegating -->[任せ方の段階と、無人で走らせる前の五つの問い](five-questions-before-delegating.md)<!-- link:end -->

<!-- textlint-disable -->
別名：headless・ヘッドレス・non-interactive mode・print モード
<!-- textlint-enable -->

非対話モード（`claude -p`）は、プロンプトを 1 つ渡して Claude Code を動かし、結果を標準出力に受け取る起動の仕方である。成熟度は <!-- gen:begin feature headless/maturity -->GA<!-- gen:end feature headless/maturity --> で、公式は Agent SDK の CLI として説明する。このページは、出力と終了コードの扱い、許可、止まる上限、知らないフォルダでの注意、課金の経路を扱う。

## 使いどころ {#when}

`claude -p` は、人が画面の前にいない場所から Claude Code を呼ぶ手段である。スクリプトの一部、ビルドの検査、CI のジョブ、別のプログラムからの呼び出しに向く。席を外す分だけ任せる幅が広がるので、先に守りを決める。任せ方の段階と、無人で走らせる前に答える問いは <!-- link:begin five-questions-before-delegating#five-questions -->[任せ方の段階と、無人で走らせる前の五つの問い › 無人で走らせる前の五つの問い](five-questions-before-delegating.md#five-questions)<!-- link:end --> にある。

防ぐ原因は 2 つある。

- 境界がない：確認に答える人がいないので、許す道具と止まる上限を決めて渡さないと、実行の範囲と費用が決まらない（原理：縛る）。
- 確かめていない：成功と出ても何が起きたかは別である。出力・記録・差分で確かめる（原理：確かめる）。確かめ方は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->無人実行の結果を確かめる › 終了コードと要約だけで決めない（準備中）<!-- link:end --> にある。

自分のプログラムに組み込むなら Agent SDK、決まった時刻や GitHub のイベントで動かすなら別の手段が合う。選び方は「比べる相手」の節にある。

## 最小の使い方 {#minimal}

=== "Claude Code"

    プロンプトを `-p` に渡し、許す道具と出力の形式を足す。

    ```bash
    claude -p "Find and fix the bug in auth.py" --allowedTools "Read,Edit" --output-format json
    ```

    - 標準入力のパイプも読める。ログを渡して原因を説明させる、といった使い方ができる。パイプの上限を超えると、エラーを出して 0 以外の終了コードで終わる。
    - `--continue` や `--resume <セッション ID>` で、前の会話を続けられる。セッション ID は `--output-format json` の出力から取れる。
    - ユーザーが起動する skill（`/skill-name`）は、プロンプトに書けば展開される。`/login` のような、ターミナルの画面専用のコマンドは使えない。

    許す道具・上限・出力形式をそろえた実行の例は、下の「雛形」の節にある。

## 出力の形式と終了コード {#output-and-exit-codes}

出力の形式は `--output-format` で選ぶ。

- `text`（既定）：最後の返答の文章だけが出る。長い作業では、終わるまで何も出ず、止まって見える。
- `json`：結果の文章を `result` に、セッション ID と費用の見積もりなどを別の欄に入れた JSON が、最後に 1 つ出る。スクリプトで読むならこれが基本である。
- `stream-json`：1 行 1 イベントの JSON で、進みが流れる。`--verbose` を併用する。トークンを逐次受け取るなら `--include-partial-messages` も付ける。最後の行が最終の結果である。

形を決めた値を受け取りたいときは、`--output-format json` に `--json-schema` を足す。結果は `structured_output` の欄に入る。有効な値を得られずに終わると、この欄は出ない。使う前に、欄があるかを確かめる。形が合っていても中身が正しいとは限らない。この仕組みの考え方は <!-- link:begin structured-outputs-basics#claude-code -->structured outputs（形式を保証する） › Claude Code の -p で形を指定する（準備中）<!-- link:end --> にある。

終了コードは、成功で 0、失敗で 0 以外になる。ただし、これだけで成功とは決められない。

- 実行の中で起きた失敗（認証がないなど）は、結果として標準出力に出る。終了コードを見る前に、出力の中身を読む。
- 古い版には、起動に失敗しても何も出さず終了コード 0 で終わる不具合や、記録の書き込みに失敗しても 0 で終わる不具合があった。いまは直っているが、固定した古い版で動かす CI では、終了コードだけの判定が失敗を見逃す。入った版は更新履歴で確かめる。
- 終了コード 0 でも、許可が足りず何もせずに終わることがある。原因と見分け方は、この下の「許可と権限モード」の節で扱う。

終了コードと要約だけで決めず、記録と差分で確かめる手順は <!-- link:begin checking-unattended-runs#records -->無人実行の結果を確かめる › 記録と差分で確かめる（準備中）<!-- link:end --> にある。最後の判断は人とブランチの保護に置く（<!-- link:begin checking-unattended-runs#final-decision -->無人実行の結果を確かめる › 最後の判断を人に置く（準備中）<!-- link:end -->）。

## 許可と権限モード {#permissions}

`claude -p` には、確認に答える人がいない。確認が要る呼び出しは、許す手段がなければ拒まれる。だから、許可を渡さない `-p` は、ファイルの編集やコマンドの実行をせずに終わることがある。

許す手段は次のとおりである。

- `--allowedTools`：許す道具を列挙する。`Read`・`Edit`・`Bash` のほか、`Bash(git diff *)` のように範囲を絞れる。` *` の前の空白が要る。空白がないと、`git diff-index` にも当たる。書き方の本体は <!-- link:begin permission-rules#minimal -->[権限ルール（allow・ask・deny） › 最小の使い方](../enforce/permission-rules.md#minimal)<!-- link:end --> にある。
- `settings.json` の allow ルール、`PermissionRequest` のフック、`--permission-prompt-tool`。
- `--permission-mode`：セッション全体の基準を決める。

権限モードの選びどころは次のとおりである。

- `dontAsk`：確認が要る呼び出しをすべて拒む。許したものだけが動くので、閉じた CI に向く。
- `acceptEdits`：作業ディレクトリ内の編集と、`mkdir`・`mv` などの一般的なファイル操作を、確認なしで通す。ほかのシェルのコマンドと通信は、列挙か allow ルールが要る。
- `auto`：分類器が行動を審査する。`--permission-mode auto` を渡せば `-p` でも使える。分類器が止める操作とすり抜ける操作は <!-- link:begin what-auto-mode-stops#defaults -->[auto モードは何を止め、何を止めないか › 既定で止めるもの・通すもの](../enforce/what-auto-mode-stops.md#defaults)<!-- link:end --> と <!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end --> にある。`auto` で起動したときは、`Bash` だけの広い allow は外され、コマンドごとに審査される。

モードを指定しない `-p` は <!-- name:begin default-to-manual-mode -->Manual（権限モード。設定の値は default のまま）<!-- name:end --> で始まる。この既定は 2026 年に何度か変わった。現在の扱いは、<!-- fact:begin permission-mode-default-noninteractive -->Manual（Claude Code 2.1.302 以降。承認の要る呼び出しは、allow ルール・フック・canUseTool・--permission-prompt-tool で認めない限り拒否）（2026-11-04 時点）<!-- fact:end -->。モードを指定すれば、既定の変更の影響を受けない。

席に誰もいないときは、`--permission-prompts none` を足せる。確認が要る呼び出しを拒み、Claude に「承認する人はいない。再び試すな」と伝える。使える版は <!-- fact:begin headless-permission-prompts-min-version -->Claude Code 2.1.259 以降（2026-11-05 時点）<!-- fact:end --> である。拒まれた呼び出しは `stream-json` の `permission_denied` のメッセージと、最終の結果の `permission_denials` に残るので、「何もせず終わった」ときの原因を見分けられる。

`auto` の分類器は、連続してブロックしたり、合計のブロックが多くなったりすると止まって確認に戻る。確認の経路がない `-p` では、その操作を拒むだけで、実行そのものは止まらない。止まらないので、ブロックされた呼び出しの記録を後で読む。

許可を広げるほど、守りを同じ流れで足す。

- コマンドの読み書きと通信を囲むのは <!-- link:begin sandboxing#minimal -->[サンドボックスで封じ込める › 最小の使い方](../enforce/sandboxing.md#minimal)<!-- link:end -->。
- 許可を二重にする考え方は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end -->。
- 確認をすべて外すモードは <!-- link:begin where-bypass-is-ok#why-isolate -->[bypassPermissions と無人の実行はどこで動かすか › なぜ隔離した環境だけか](../safety/where-bypass-is-ok.md#why-isolate)<!-- link:end --> にある。

!!! example "判断例：CI でテストの失敗を直させる"
    - **状況**：CI のジョブで、失敗したテストを Claude に直させたい。使うのは専用のブランチだけで、人が差分を見てからマージする。
    - **迷う候補**：`--permission-mode auto` で分類器に任せる。`--permission-mode dontAsk` に `--allowedTools` で道具を列挙する。
    - **選んだもの**：`dontAsk` と `--allowedTools "Read,Edit,Bash(npm test *)"`。
    - **理由**：やることが決まっているので、必要な道具を先に列挙できる。列挙にない呼び出しは拒まれ、確認待ちで止まる心配がない。作業の範囲が広がって列挙しきれなくなったら、`auto` とサンドボックスを組み合わせる。

## 止まる上限（ターンと費用） {#limits}

無人の実行は、止める人がいない。`-p` で使える上限は 2 つある。どちらも print モード（`-p`）専用である。

- `--max-turns`：エージェントのターン数を制限する。既定は制限なしである。
- `--max-budget-usd`：見積もりの費用がこの額に達したら止める。サブエージェントの費用も数える。見積もりはクライアント側の概算で、請求と食い違う。上限を超えて使うことがあるので、余裕を見て決める。

上限に達したときの終了コードと出力は、この辞典では確かめていない。上限を入れた実行では、止まった場合の出力を先に観察して、スクリプトの判定に入れる。

`json` の出力の `total_cost_usd` は、実行ごとの費用の見積もりである。`--continue` や `--resume` で続けると、会話全体の合計が出る。CI の時間切れのような、ジョブ側の制限も併用する。

費用がどこで増えるかは <!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> で確かめる。多数のファイルに同じ作業を流す場合は、まず数件で上限を試す（<!-- link:begin batch-and-p-loops -->多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）<!-- link:end -->）。

## 知らないフォルダで動かすとき {#untrusted-folders}

対話の Claude Code は、初めてのフォルダで信頼の確認を出す。`-p` は出さない。`--bare` を付けない `-p` は、知らないフォルダでも、そのフォルダの `.claude/settings.json` のフックを動かし、`.mcp.json` のサーバーに接続する。

だから、他人のリポジトリや、外から来た PR のチェックアウトで `claude -p` を動かすと、中のフックがそのまま動く。開く前に見るファイルは次にある。

- <!-- link:begin before-opening-unknown-repos#files-to-check -->[知らないリポジトリを開く前に › 開く前に見るファイル](../safety/before-opening-unknown-repos.md#files-to-check)<!-- link:end -->
- 非対話で確認が出ない点：<!-- link:begin before-opening-unknown-repos#headless -->[知らないリポジトリを開く前に › 非対話の実行では確認が出ない](../safety/before-opening-unknown-repos.md#headless)<!-- link:end -->

手段は 2 つある。

- 自動の読み込みを止める：`--bare` を付けると、フック・スキル・プラグイン・MCP・自動メモリ・CLAUDE.md の自動検出を止め、どのマシンでも同じ条件になる。止めるものの一覧は <!-- link:begin bare-mode#what-is-skipped -->--bare と再現性 › 読み込まないもの（準備中）<!-- link:end --> にある。`--bare` は API キーで認証し、サブスクリプションのログインを使わない（<!-- link:begin bare-mode#authentication -->--bare と再現性 › 認証が変わる（サブスクリプションで使うとき）（準備中）<!-- link:end -->）。
- 隔離する：使い捨ての環境と <!-- link:begin sandboxing#minimal -->[サンドボックスで封じ込める › 最小の使い方](../enforce/sandboxing.md#minimal)<!-- link:end --> で、動いても困らない範囲に閉じる（<!-- link:begin before-opening-unknown-repos#isolate -->[知らないリポジトリを開く前に › 隔離して動かす](../safety/before-opening-unknown-repos.md#isolate)<!-- link:end -->）。

外の人が書いた issue や PR を読ませる場合は、<!-- link:begin github-actions-with-claude#untrusted-input -->GitHub Actions と @claude › 外の人が書いた issue と PR（準備中）<!-- link:end --> も読む。鍵や秘密は、作業ディレクトリと会話に置かない（<!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end -->）。

## 課金の経路（API キーがあるとき） {#billing-path}

環境変数 `ANTHROPIC_API_KEY` があると、`-p` は確認なしにその鍵を使う。対話のセッションなら使うかを一度聞かれるが、`-p` は聞かない。サブスクリプションでログインしていても、その鍵の組織に API の従量の料金がかかる。プランの利用量は使われない（[Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)）。

逆に、鍵がなく、プランでログインした状態の `-p` や Agent SDK は、プランの利用上限から引かれる（[Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)）。思わぬ請求になる典型の原因は、シェルの設定ファイルに鍵を書いたことを忘れていることである。

無人で回す前に、経路を確かめる。

1. 動かすシェルで `ANTHROPIC_API_KEY` が設定されているかを見る。
2. 対話の Claude Code で `/status` を開き、今の認証を見る。
3. 経路が決まる順と確かめ方は <!-- link:begin check-billing-path#how-the-path-is-chosen -->課金の経路を確かめる（API キーとサブスクリプション） › 経路が決まる順（準備中）<!-- link:end --> と <!-- link:begin check-billing-path#check-current-path -->課金の経路を確かめる（API キーとサブスクリプション） › 今の経路を確かめる（準備中）<!-- link:end --> にある。

鍵のある `-p` の費用は、プランとは別の課金である。月の API credits の扱いは <!-- link:begin check-billing-path#monthly-api-credits -->課金の経路を確かめる（API キーとサブスクリプション） › プランに付く API credits（準備中）<!-- link:end --> にある。

## 雛形 {#templates}

許す道具・上限・出力形式を明示した例である。`dontAsk` と列挙で、確認待ちを作らずに範囲を絞る。成功の判定は、終了コードと要約に頼らず、自分でテストを流し直して差分を見る。

<!-- gen:begin snippet headless-basics/limited-run -->
<!-- textlint-disable -->

??? example "雛形：許可を絞った claude -p の実行例（許す道具・上限・出力形式）"

    ```bash
    #!/usr/bin/env bash
    # 許す道具・止まる上限・出力の形式を明示して claude -p を動かす例。
    # 値（--max-turns と --max-budget-usd）は例。自分の作業の大きさに合わせて決める。
    set -euo pipefail

    # 1. 許す道具を列挙し、列挙にない承認待ちは拒む（dontAsk）。上限と出力形式も渡す。
    json=$(claude -p "npm test を実行し、失敗しているテストの原因を直す。直したら npm test をもう一度実行し、結果を報告する。" \
      --permission-mode dontAsk \
      --allowedTools "Read,Edit,Bash(npm test *)" \
      --max-turns 20 \
      --max-budget-usd 2 \
      --output-format json)

    # 2. 要約を読む。ここで見るのは「Claude がどう言ったか」だけ。
    printf '%s\n' "$json" | jq -r '.result'

    # 3. 成功かどうかは終了コードと要約で決めず、自分でテストと差分を確かめる。
    npm test
    git diff --stat
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet headless-basics/limited-run -->

## 効かない場面・落とし穴 {#pitfalls}

- 編集やコマンドをせずに終わる：許す道具の列挙が足りないか、権限モードが確認待ちを拒んでいる。`stream-json` の `permission_denied` や `permission_denials` で、拒まれた呼び出しを見る。足りなければ列挙か allow ルールを足す。
- CI が成功と出たのに何もしていない：終了コードだけを見ている。出力の中身、記録、差分で確かめる。固定した古い版の CI は、起動の失敗を見逃すことがある。
- API の請求が来た：`ANTHROPIC_API_KEY` が環境にある。鍵を外すか、経路を確かめる。
- 他のマシンで結果が変わる：手元の設定やフック、CLAUDE.md が混ざっている。`--bare` で条件をそろえる（API キーが要る）。
- 子プロセスは許可のルールで縛れない：シェルの中で動く別のコマンドの中身までは、道具の許可で止められない。囲うならサンドボックスを使う（<!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end -->）。
- 入れ子の実行：クラウドや self-hosted の runner のセッションの中で `claude -p` を動かしたとき、セッション ID と記録を共有する不具合が、古い版にあった。いまは直っている。
- 理由を言わずに止まる：古い版の `-p` には、止まった理由を出力に言わないことがあった。止まったら、出力の最後と記録を読む。

## 比べる相手 {#compare}

- 決まった時刻・イベント・スクリプトのどれから動かすか、どこで動くか、どの課金になるかで選ぶ：<!-- link:begin choosing-automation -->自動化の選び方（定期タスク・非対話モード・SDK）（準備中）<!-- link:end -->。
- GitHub のイベントや `@claude` で動かす：<!-- link:begin github-actions-with-claude#modes -->GitHub Actions と @claude › 呼ばれて動く形と、イベントで動く形（準備中）<!-- link:end -->。
- 自分のプログラムに組み込み、承認のコールバックや型付きのメッセージが要る：<!-- link:begin agent-sdk-basics#same-and-different -->Agent SDK（Claude Code をライブラリとして使う） › Claude Code と同じもの・違うもの（準備中）<!-- link:end -->。層の比較は <!-- link:begin sdk-comparison#comparison -->[Client SDK・Agent SDK・Managed Agents・CLI の比較 › 層ごとの比較（自分のプロセスに組み込む・Anthropic にホストさせる・CLI で動かす）](../api/sdk-comparison.md#comparison)<!-- link:end --> にある。
- 多数のファイルに同じ作業を流す：<!-- link:begin batch-and-p-loops -->多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）<!-- link:end -->。

## 古くなった助言 {#outdated}

「無人で回すなら `--dangerously-skip-permissions` で確認を全部飛ばす」という助言は古い。いまは、ふだんは許す道具を絞った `-p` か `auto` モードにサンドボックスを重ね、確認をすべて外すモードは使い捨てのコンテナや VM の中だけにする。台帳の行は <!-- link:begin outdated-advice-ledger#yolo-skip-permissions -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#yolo-skip-permissions)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Run Claude Code programmatically](https://code.claude.com/docs/en/headless)：Anthropic・英語・確認日 2026-11-04
- [CLI reference](https://code.claude.com/docs/en/cli-reference)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)：Anthropic・英語・確認日 2026-11-04
- [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [任せ方の段階と、無人で走らせる前の五つの問い](five-questions-before-delegating.md)

**次に読む**

- 多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）
- 自動化の選び方（定期タスク・非対話モード・SDK）（準備中）
- --bare と再現性（準備中）
- GitHub Actions と @claude（準備中）

**関連**

- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 無人実行の結果を確かめる（準備中）
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [bypassPermissions と無人の実行はどこで動かすか](../safety/where-bypass-is-ok.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [知らないリポジトリを開く前に](../safety/before-opening-unknown-repos.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- 課金の経路を確かめる（API キーとサブスクリプション）（準備中）
- [上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)
- structured outputs（形式を保証する）（準備中）
- [Client SDK・Agent SDK・Managed Agents・CLI の比較](../api/sdk-comparison.md)
- Agent SDK（Claude Code をライブラリとして使う）（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
