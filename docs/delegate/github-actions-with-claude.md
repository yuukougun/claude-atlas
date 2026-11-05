---
id: github-actions-with-claude
title: GitHub Actions と @claude
aliases: [claude-code-action, /install-github-app]
type: feature
field: delegate
chapter: 定期と無人の実行
order: 210
level: 回す
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 確かめる]
prevents: [境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: GitHub Actions から Claude Code を動かし、issue や PR で @claude と呼んだり、イベントや定時で作業させたりできる。鍵は secrets に置き、権限を最小にし、マージの前に人がレビューする。
signs:
  - {type: goal, text: issue や PR で、@claude と呼んで作業させたい}
  - {type: goal, text: スクリプトや CI から Claude Code を使いたい}
  - {type: symptom, text: 古い記事の書き方で、Claude の GitHub Action が動かない}
prerequisites: [headless-basics, protecting-secrets]
related: [lethal-trifecta, prompt-injection-in-practice, where-bypass-is-ok, permission-rules, automated-pr-review, risk-tiered-approval, create-and-review-prs, checking-unattended-runs, check-billing-path, bare-mode, choosing-automation, what-to-put-in-claude-md]
tracks: [github-actions]
outdated_advice: [action-beta-direct-prompt]
sources: [cc-docs-github-actions, cc-docs-feature-availability, gh-claude-code-action-migration, gh-claude-code-action-v1]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 呼ばれて動く形と、イベントで動く形, anchor: modes}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 鍵と権限, anchor: secrets-and-permissions}
  - {title: 外の人が書いた issue と PR, anchor: untrusted-input}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：GitHub Actions から Claude Code を動かし、issue や PR での @claude の呼びかけ、イベント、定時で作業させられる。
    - **いつ引くか**：issue や PR で @claude と呼んで作業させたいとき。スクリプトや CI から Claude Code を使いたいとき。古い記事の書き方で、Claude の GitHub Action が動かないとき。
    - **強制力**：workflow の `permissions` と GitHub 側の設定、branch の保護は鍵である。CLAUDE.md のレビュー基準は、お願いにとどまる。
    - **いちばんの注意**：鍵は secrets に置き、権限を絞り、マージの前に人が差分を読む。外の人が書いた本文は、信頼できない入力として扱う。
    - **前提**：<!-- link:begin headless-basics -->[非対話モード（claude -p）の基本](headless-basics.md)<!-- link:end -->・<!-- link:begin protecting-secrets -->[秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)<!-- link:end -->

<!-- textlint-disable -->
別名：claude-code-action・/install-github-app
<!-- textlint-enable -->

GitHub Actions と @claude は、GitHub の workflow の中で Claude Code を動かす公式の仕組み（`anthropics/claude-code-action`）である。成熟度は <!-- gen:begin feature github-actions/maturity -->GA<!-- gen:end feature github-actions/maturity --> で、リポジトリに置く workflow のファイルで設定する。このページは、動かす形の選び方、鍵と権限の決め方、外の人が書いた本文の扱いを扱う。

## 使いどころ {#when}

人が画面の前にいない場所で、リポジトリに近い作業を Claude にさせたいときに使う。使い方は 4 つある。issue のコメントで @claude と呼んで実装を頼む。PR の質問に答えさせる。PR が開かれるたびに決まった手順で見させる。定時に報告を作らせる。

席を外す分だけ任せる幅が広がるので、守りを先に決める。このページが防ぐ原因は「境界がない」で、使う原理は「縛る」と「確かめる」である。

- 縛る：workflow の権限、渡す道具、ターン数の上限、ジョブの時間を決める。
- 確かめる：Claude が出した変更は、マージの前に人が読む。確かめ方は <!-- link:begin checking-unattended-runs#final-decision -->[無人実行の結果を確かめる › 最後の判断を人に置く](../verify/checking-unattended-runs.md#final-decision)<!-- link:end --> にある。

CI の中で `claude -p` を直接動かす書き方は <!-- link:begin headless-basics#minimal -->[非対話モード（claude -p）の基本 › 最小の使い方](headless-basics.md#minimal)<!-- link:end --> にある。この Action は、その上に GitHub のイベントと認証をつないだものである。

## 呼ばれて動く形と、イベントで動く形 {#modes}

Action は、workflow に `prompt` の入力があるかどうかで、動き方を自動で決める。`mode` の入力は要らない。

- 呼ばれて動く形（interactive mode）：`prompt` を書かない。issue や PR のコメント、PR のレビュー、新しく開いた issue の題名や本文にある `@claude` を待ち、その依頼に答える。進みと結果は、呼ばれた issue や PR のコメントに出る。
- イベントで動く形（automation mode）：`prompt` を書く。@claude の呼びかけを待たず、workflow の `on:` に書いたイベントや定時で動く。結果は既定で実行ログに出る。issue や PR に書かせたいときは、prompt で頼み、書き込める道具を渡す。

どちらの形でも、実行の前に 2 つの確認が走る。

- 書き込み権限：issue と PR のイベントでは、起こした人がリポジトリへの write 権限を持っていなければならない。持っていなければ、実行は失敗する。定時のように人が書かないイベントは、この確認を飛ばす。
- 人であること：ボットが起こした実行は、`allowed_bots` に載せない限り断られる。ボット同士の無限の呼び合いを防ぐ確認である。定時の実行は、cron を最後に書き換えた人の実行として数えられる。

`prompt` の入力には、文章のほかにスキルの呼び出し（`/skill-name`）も書ける。リポジトリの `.claude/skills/` にあるスキルを使うなら、Action の前に `actions/checkout` を置く。プラグインのスキルは `plugin_marketplaces` と `plugins` の入力で入れる。

形の選び方は、誰が始めるかで決める。

- 人が見て、その場で頼みたい：呼ばれて動く形。
- 決まった手順を、イベントや時刻のたびに回したい：イベントで動く形。

!!! example "判断例：PR が開かれるたびに見させるか、見てほしい PR だけ呼ぶか"
    - **状況**：チームのリポジトリで、PR の一次のレビューを Claude に手伝わせたい。PR の数は多く、人のレビューは必ず残す。
    - **迷う候補**：PR のイベントで動く形にして、全部の PR を見させる。呼ばれて動く形にして、レビューを頼みたい PR のコメントで @claude と呼ぶ。
    - **選んだもの**：まず呼ばれて動く形で始め、手順が固まってから、イベントで動く形に移す。
    - **理由**：呼ぶ形は、どの PR に費用と権限を使うかを人が選べる。手順と指摘の質が見えてから、全部の PR に広げても遅くない。PR ごとに自動で付けたいだけなら、workflow を自分で持たない <!-- link:begin automated-pr-review -->自動 PR レビュー（Code Review・/ultrareview）（準備中）<!-- link:end --> も選べる。

## 最小の使い方 {#minimal}

=== "Claude Code"

    手早く入れるなら、リポジトリで `claude` を開き、`/install-github-app` を実行する。GitHub App の導入、認証の secret の登録、workflow の PR の用意までを案内する。

    - リポジトリの admin 権限が要る。GitHub CLI（`gh`）を入れて、`gh auth login` を済ませておく。
    - 使えるのは github.com のリポジトリだけである。gitlab.com や bitbucket.org のリモートでは、案内を出して終わる。
    - 認証は API キーか、サブスクリプションの長期のトークンのどちらかを選ぶ。
    - 最後に workflow のファイルを含む PR が用意される。その PR をマージすると、@claude が使える。

    コマンドが失敗するときや、workflow を自分で管理したいときは、手で入れる。Claude GitHub App を入れ、secret を足し、公式の `examples/claude.yml` を `.github/workflows/` にコピーする。コピーする前に、書かれた `permissions` を自分の用途に合わせて見直す。下の「雛形」に最小の例を置いた。

    入れたら、issue か PR のコメントに `@claude` を含む依頼を書いて試す。試す場所は、使い捨てのリポジトリが望ましい。

## 鍵と権限 {#secrets-and-permissions}

無人の実行では、Claude に渡した鍵と権限が、そのまま被害の大きさの上限になる。鍵は漏らさないこと、権限は用途の分だけに絞ることが、このページの守りの中心である。

### 認証の鍵

認証の secret は 2 種類ある。どちらも、workflow に直接書かず、リポジトリの secrets から渡す。

- `ANTHROPIC_API_KEY`：Console の API キー。入力 `anthropic_api_key` に渡す。API の従量の課金になる。
- `CLAUDE_CODE_OAUTH_TOKEN`：`claude setup-token` で作るトークン。入力 `claude_code_oauth_token` に渡す。サブスクリプションの利用枠で動く。

組織で 1 つの secret を共有するなら、API キーにする。OAuth のトークンは、コマンドを実行した人のサブスクリプションに結び付くからである。長期の secret を置きたくないときは、workload identity federation（`anthropic_federation_rule_id` などの入力）で、workflow の OIDC トークンから認証できる。

課金の経路は、どちらの鍵を渡したかで変わる。GitHub Action から起動したものは、プランに付く API credits の対象外として扱われる。確かめ方は <!-- link:begin check-billing-path#monthly-api-credits -->[課金の経路を確かめる（API キーとサブスクリプション） › プランに付く API credits](../cost/check-billing-path.md#monthly-api-credits)<!-- link:end --> と <!-- link:begin check-billing-path#check-current-path -->[課金の経路を確かめる（API キーとサブスクリプション） › 今の経路を確かめる](../cost/check-billing-path.md#check-current-path)<!-- link:end --> にある。

鍵の扱いの基本は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> にある。コミットに鍵を入れない。ログに出さない。漏れたと分かったら、secret を消すだけでなく、鍵そのものを Console で失効させる。secret を消しても、鍵は有効なまま残るからである。

### 権限

権限は 3 つの層で決まる。

- workflow の `permissions`：その workflow に渡る `GITHUB_TOKEN` の権限。job ごとに、要るものだけを書く。
- GitHub App の権限：Action は既定で Claude GitHub App として認証する。公式の App は、他の機能と共用の権限のまとまりを一括で受け取る。一部だけを受け取ることはできない。Contents・Issues・Pull requests だけで足りる組織は、自前の GitHub App を作る選択肢がある。
- Claude に渡す道具：`claude_args` の `--allowedTools` や `settings` の allow ルール。イベントで動く形で文章の `prompt` を渡すと、渡した道具のほかは、シェルも GitHub の API も使えない。スキルを呼ぶ形では、スキルの `allowed-tools` が許す道具が使える。

道具の許し方の考え方は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end --> と <!-- link:begin headless-basics#permissions -->[非対話モード（claude -p）の基本 › 許可と権限モード](headless-basics.md#permissions)<!-- link:end --> にある。確認をすべて外すモードは、使い捨ての隔離した環境でだけ使う（<!-- link:begin where-bypass-is-ok#why-isolate -->[bypassPermissions と無人の実行はどこで動かすか › なぜ隔離した環境だけか](../safety/where-bypass-is-ok.md#why-isolate)<!-- link:end -->）。Actions の runner は使い捨てだが、リポジトリへ書き込める鍵を持つので、それだけで安全にはならない。

### 止まる上限

費用と時間は、次で抑える。

- `claude_args` の `--max-turns`：ターン数（Claude の往復の回数）の上限。
- ジョブの `timeout-minutes`：ジョブ側の時間の上限。
- `concurrency`：同じ対象での並列の実行を制限する。
- 依頼を具体的にし、issue のテンプレートで文脈を先に渡す。`CLAUDE.md` は毎回読まれるので、短く保つ。

上限の考え方は <!-- link:begin headless-basics#limits -->[非対話モード（claude -p）の基本 › 止まる上限（ターンと費用）](headless-basics.md#limits)<!-- link:end --> にある。

### マージの前に人が読む

Claude が push した変更や作った PR は、人が差分を読んでからマージする。AI が通したことを、人の承認に数えない（<!-- link:begin risk-tiered-approval#ai-approval-doesnt-count -->[リスク段階別の承認（AI の承認を人の承認に数えない） › AI の承認を数えない](../team/risk-tiered-approval.md#ai-approval-doesnt-count)<!-- link:end -->）。PR の作り方とレビューの受け方は <!-- link:begin create-and-review-prs#risks-before-submitting -->[PR を作り、レビューを受ける › 出す前にリスクを挙げさせる](../recipes/create-and-review-prs.md#risks-before-submitting)<!-- link:end --> にある。無人で動いた結果を、終了コードや要約だけで決めない確かめ方は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->[無人実行の結果を確かめる › 終了コードと要約だけで決めない](../verify/checking-unattended-runs.md#beyond-exit-codes)<!-- link:end --> にある。

リポジトリの `CLAUDE.md` にレビューの基準やプロジェクトの決まりを書くと、Claude はそれに従う。ただし、これはお願いである。例外を許さない禁止は、branch の保護や権限で強制する。何を書くかは <!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)<!-- link:end --> にある。

## 外の人が書いた issue と PR {#untrusted-input}

外の人が書ける issue と PR の本文は、信頼できない入力である。そこに仕込まれた指示に Claude が従うと、runner にある鍵と、リポジトリへの書き込みが、攻撃の道具になる。

Action には、この経路を狭める既定の確認がある。

- 起こした人が write 権限を持たなければ、実行は失敗する。外の人の issue や @claude のコメントでは、Claude は動かない。
- `allowed_non_write_users` で、write 権限のない人にも許せる。ただし、この入力を使うには、自分で用意した `github_token` も渡す必要がある。これは確認を外す設定なので、外の人の本文が Claude に届く経路を作る。
- 公開リポジトリでは、fork からの PR の実行に、GitHub が secrets を渡さない。fork の PR を、secrets を使うレビューの対象にはできない。

この確認を外す前に、3 つの能力が同じ実行に重なっていないかを見る。

- 信頼できない入力：外の人が書いた本文。
- 秘密や私的なデータ：secrets、非公開のコード。
- 外への送信や変更：push、コメント、道具を通した通信。

3 つが同時にそろうと、仕込まれた指示が被害につながる。考え方は <!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](../safety/lethal-trifecta.md#three-capabilities)<!-- link:end -->、指示が入ってくる経路は <!-- link:begin prompt-injection-in-practice#channels -->[プロンプトインジェクションの実際 › 指示が入ってくる経路](../safety/prompt-injection-in-practice.md#channels)<!-- link:end -->、防ぐ手立ては <!-- link:begin prompt-injection-in-practice#what-works -->[プロンプトインジェクションの実際 › 防ぐ手立ては権限と通信の側にある](../safety/prompt-injection-in-practice.md#what-works)<!-- link:end --> にある。防ぐのは、本文を疑う賢さではなく、持たせる権限と通信を減らすことである。

!!! example "判断例：外の人が出した issue を自動で仕分けさせるか"
    - **状況**：公開のリポジトリで、外の人が出す issue が増えた。ラベル付けと重複の確認を、Claude に手伝わせたい。
    - **迷う候補**：`allowed_non_write_users` を設定し、issue が開かれるたびにイベントで動く形で仕分けさせる。メンテナーが issue を読み、仕分けさせたいものにだけ @claude とコメントして呼ぶ。
    - **選んだもの**：メンテナーが呼ぶ形。渡す道具は、ラベルを付ける道具と読む道具に絞る。
    - **理由**：自動の形は、外の人の本文を人の目を通さず Claude に渡す。書き込み権限のある道具が付いていると、仕込まれた指示の被害が大きい。呼ぶ形は、人が本文を一度読み、write 権限の確認も既定のまま残る。それでも本文は信頼できない入力なので、道具の絞りは外さない。

3 つとも要る作業では、人の承認を挟む。承認の段の決め方は <!-- link:begin risk-tiered-approval -->[リスク段階別の承認（AI の承認を人の承認に数えない）](../team/risk-tiered-approval.md)<!-- link:end --> にある。

## 雛形 {#templates}

1 つめは、@claude と呼ばれたときだけ動く最小の workflow である。`prompt` を書かないので、呼ばれて動く形になる。鍵は secrets から渡し、ターン数とジョブの時間に上限を付けた。

<!-- gen:begin snippet github-actions-with-claude/minimal-workflow -->
<!-- textlint-disable -->

??? example "雛形：最小権限の workflow（@claude に応える）"

    ```yaml
    # .github/workflows/claude.yml
    # @claude と呼ばれたときだけ動く workflow の最小の例（呼ばれて動く形）。
    # 値（timeout-minutes と --max-turns）は例。自分の作業の大きさに合わせて決める。
    # permissions は、この workflow に渡る GITHUB_TOKEN の権限である。
    # action は既定で Claude GitHub App として認証するので、App 側の権限は別に決まる。
    name: Claude Code

    on:
      issue_comment:
        types: [created]
      pull_request_review_comment:
        types: [created]

    # 同じ issue や PR で、実行が重ならないようにする。
    concurrency:
      group: claude-${{ github.event.issue.number || github.event.pull_request.number }}
      cancel-in-progress: false

    jobs:
      claude:
        # @claude を含まないコメントでは、runner を起動しない。
        if: contains(github.event.comment.body, '@claude')
        runs-on: ubuntu-latest
        # ジョブ側の時間の上限。暴走を止める。
        timeout-minutes: 20
        permissions:
          contents: write        # Claude がファイルを変えて push するため
          pull-requests: write   # PR への返信と作成のため
          issues: write          # issue への返信のため
          id-token: write        # 既定の GitHub App の認証に要る
          actions: read          # PR の CI の結果を読むため
        steps:
          - uses: actions/checkout@v6
            with:
              fetch-depth: 1
          - uses: anthropics/claude-code-action@v1
            with:
              # 鍵は workflow に書かず、必ず repository の secrets から渡す。
              anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
              # prompt を書かないので、@claude の呼びかけに答える形になる。
              # ターン数の上限。ほかの CLI の設定も claude_args に書く。
              claude_args: --max-turns 10
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet github-actions-with-claude/minimal-workflow -->

2 つめは、定時に読むだけの報告を作らせる workflow である。`prompt` を書くので、イベントで動く形になる。渡す道具は、読むだけの 2 つに絞った。この例はリポジトリに何も書かない。書かせるときは、書き込める道具を足す前に、上の「外の人が書いた issue と PR」の節を読む。

<!-- gen:begin snippet github-actions-with-claude/scheduled-report -->
<!-- textlint-disable -->

??? example "雛形：定時に読むだけの報告をさせる workflow（prompt あり）"

    ```yaml
    # .github/workflows/daily-report.yml
    # prompt を渡して、定時に読むだけの作業をさせる例（イベントで動く形）。
    # 結果は既定で workflow の実行ログに出る。リポジトリには何も書かない。
    # 時刻（cron）と --max-turns は例。自分の作業に合わせて決める。
    name: Daily Report

    on:
      schedule:
        - cron: "0 9 * * *"

    jobs:
      report:
        runs-on: ubuntu-latest
        timeout-minutes: 15
        permissions:
          contents: read
          issues: read
          id-token: write
        steps:
          - uses: anthropics/claude-code-action@v1
            with:
              anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
              prompt: "Generate a summary of yesterday's commits and open issues"
              # prompt を渡した実行では、道具を列挙して渡さないと、
              # シェルも GitHub の API も使えない。読むだけの道具に絞る。
              claude_args: |
                --max-turns 8
                --allowedTools "mcp__github__list_commits,mcp__github__list_issues"
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet github-actions-with-claude/scheduled-report -->

## 効かない場面・落とし穴 {#pitfalls}

- 動かないときの確認：GitHub App が入っているか、workflow が有効か、secret が置かれているかを見る。コメントに `@claude` が単語として含まれるかも見る。`/claude` や `@claude-bot` では呼べない。呼んだ人の write 権限も確かめる。
- Claude の push した commit で CI が走らない：Action の入力 `github_token` に既定の `GITHUB_TOKEN` を渡していると、GitHub は、そのトークンで作られたコミットから別の workflow を起動しない。その入力の行を外すか、自前の GitHub App のトークンを渡す。
- 定時の実行：GitHub は、既定のブランチにある workflow だけを定時で動かす。公開のリポジトリでは、動きのない期間が続くと、定時の実行が止められる。
- 古い記事の書き方：`@beta` や `direct_prompt` を使う記事のとおりに書くと動かない。直し方は、下の「古くなった助言」の節にある。
- 課金の取り違え：`ANTHROPIC_API_KEY` を渡すと、API の従量の課金になる。サブスクリプションのつもりなら、OAuth のトークンを使う。無人で回す前に、経路を確かめる（<!-- link:begin check-billing-path#how-the-path-is-chosen -->[課金の経路を確かめる（API キーとサブスクリプション） › 経路が決まる順](../cost/check-billing-path.md#how-the-path-is-chosen)<!-- link:end -->）。
- 手元の設定が混ざる：Action はリポジトリをチェックアウトして動くので、リポジトリの `CLAUDE.md` や設定が読まれる。信頼できないブランチの設定が混ざるのを避けたいときは <!-- link:begin bare-mode#what-is-skipped -->[--bare と再現性 › 読み込まないもの](bare-mode.md#what-is-skipped)<!-- link:end --> を見る。この組み合わせは、この辞典では確かめていない。
- AI のレビューが通ったからといって、承認にはならない。指摘の採否と承認は、人が決める。

## 比べる相手 {#compare}

- 決まった時刻・イベント・スクリプトのどれから、どこで動かすかで選ぶ：<!-- link:begin choosing-automation -->[自動化の選び方（定期タスク・非対話モード・SDK）](choosing-automation.md)<!-- link:end -->。
- PR ごとの自動のレビューを、workflow を持たずに付ける：<!-- link:begin automated-pr-review -->自動 PR レビュー（Code Review・/ultrareview）（準備中）<!-- link:end -->。
- workflow を自分で持たず、`claude -p` をスクリプトや CI に直接書く：<!-- link:begin headless-basics -->[非対話モード（claude -p）の基本](headless-basics.md)<!-- link:end -->。
- 動かす環境を隔離する考え方：<!-- link:begin where-bypass-is-ok#decision -->[bypassPermissions と無人の実行はどこで動かすか › 無人の夜間実行をどこで動かすかの判断例](../safety/where-bypass-is-ok.md#decision)<!-- link:end -->。

## 古くなった助言 {#outdated}

「`anthropics/claude-code-action@beta` を使い、`direct_prompt` でプロンプトを渡す」という書き方は古い。いまは `@v1` を使い、プロンプトは `prompt` に、`max_turns` や `model` などの設定は `claude_args` に書く。`mode` の入力は外す。`custom_instructions` は、`claude_args` の `--append-system-prompt` になる。自分の workflow の古い書き方は、`.github/workflows/` で `@beta`・`direct_prompt`・`mode`・`max_turns` を探せば見つかる。台帳の行は <!-- link:begin outdated-advice-ledger#action-beta-direct-prompt -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#action-beta-direct-prompt)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)：Anthropic・英語・確認日 2026-11-04
- [Feature availability](https://code.claude.com/docs/en/feature-availability)：Anthropic・英語・確認日 2026-11-04
- [Migration Guide: v0.x to v1.0](https://github.com/anthropics/claude-code-action/blob/main/docs/migration-guide.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code GitHub Action v1.0](https://github.com/anthropics/claude-code-action/releases/tag/v1)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [非対話モード（claude -p）の基本](headless-basics.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)

**関連**

- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)
- [bypassPermissions と無人の実行はどこで動かすか](../safety/where-bypass-is-ok.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 自動 PR レビュー（Code Review・/ultrareview）（準備中）
- [リスク段階別の承認（AI の承認を人の承認に数えない）](../team/risk-tiered-approval.md)
- [PR を作り、レビューを受ける](../recipes/create-and-review-prs.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [課金の経路を確かめる（API キーとサブスクリプション）](../cost/check-billing-path.md)
- [--bare と再現性](bare-mode.md)
- [自動化の選び方（定期タスク・非対話モード・SDK）](choosing-automation.md)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
