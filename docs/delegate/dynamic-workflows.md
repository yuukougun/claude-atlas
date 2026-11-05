---
id: dynamic-workflows
title: dynamic workflows（スクリプトで多数のサブエージェントを動かす）
nav_title: dynamic workflows
aliases: [ultracode, workflows, /workflows, ワークフロー, /deep-research]
type: feature
field: delegate
chapter: 並べる
order: 130
level: 回す
priority: 推奨
surfaces: [claude-code]
principle: [確かめる, 縛る]
prevents: [合っていない, 確かめていない]
pitfalls: []
scenes: [開発, 調べもの]
summary: Claude が書いたスクリプトで多数のサブエージェントを動かし、コードベース全体の監査や大量のファイルの移行を背景で進められる。費用が大きくなりやすいので、小さな範囲で試してから広げる。
signs:
  - {type: goal, text: コードベース全体の監査や大規模な移行を、一度に進めたい}
  - {type: symptom, text: ワークフローで動かしたら、思ったより利用枠を使った}
prerequisites: [choosing-parallel-modes, permission-rules]
related: [parallel-and-loop-costs, sandboxing, hooks-basics, independent-review, checking-unattended-runs, batch-and-p-loops, agent-teams, research-in-subagents, humans-set-the-parallel-limit, refactor-and-migrate, effort-levels]
tracks: [workflows, effort]
outdated_advice: [workflow-keyword-extra-usage]
sources: [cc-docs-workflows, cc-docs-agents, cc-docs-sub-agents, cc-docs-permissions, cc-docs-sandboxing, cc-docs-costs, cc-changelog]
volatility: 中
sections:
  - {title: 向く規模と、小さく試す, anchor: when-and-start-small}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 雛形, anchor: templates}
  - {title: 担当にも効く縛り、確かめていない縛り, anchor: guards-for-workers}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：Claude が書いたスクリプトで多数のサブエージェントを背景で動かし、コードベース全体の監査や大量のファイルの移行を進められる。
    - **いつ引くか**：コードベース全体の監査や大規模な移行を一度に進めたいとき。ワークフローで動かしたら、思ったより利用枠を使ったとき。
    - **前提**：<!-- link:begin choosing-parallel-modes -->[並列の方式の選び方](choosing-parallel-modes.md)<!-- link:end -->、<!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end -->
    - **止められるもの**：担当の道具の呼び出しには、権限ルールとサンドボックスが効く。ワークフロー自体の強制力は「<!-- gen:begin feature workflows/enforcement -->なし<!-- gen:end feature workflows/enforcement -->」で、規模の警告は助言にとどまり、実行を止めない。費用の上限は自分で決める。

<!-- textlint-disable -->
別名：ultracode・workflows・/workflows・ワークフロー・/deep-research
<!-- textlint-enable -->

dynamic workflows は、Claude が書いた JavaScript のスクリプトを実行環境が背景で動かし、スクリプトが多数のサブエージェントを呼ぶ機能である。このページでは、呼ばれるサブエージェントを「担当」と書く。途中の結果はスクリプトの変数に残り、会話には最終の結果だけが戻る。成熟度は <!-- gen:begin feature workflows/maturity -->GA<!-- gen:end feature workflows/maturity --> で、入った版は <!-- gen:begin feature workflows/since -->2.1.154（2026-05-28）<!-- gen:end feature workflows/since --> である（[Orchestrate subagents at scale with dynamic workflows](https://code.claude.com/docs/en/workflows)）。

## 向く規模と、小さく試す {#when-and-start-small}

向くのは、対象が多く、同じ手順を対象ごとに当てられ、結果を後から確かめられる作業である。コードベース全体の監査、数百ファイルの移行、出典を突き合わせる調べものが例になる。

サブエージェントやエージェントチームでは、次に何を動かすかを Claude が 1 ターンずつ決める。ワークフローでは、その計画をスクリプトが持つ。選び方の全体は <!-- link:begin choosing-parallel-modes#who-coordinates -->[並列の方式の選び方 › 誰が調整するか](choosing-parallel-modes.md#who-coordinates)<!-- link:end --> にある。計画がコードに移るので、独立した担当に互いの指摘を反証させる段や、複数の角度から案を出させる段を、毎回同じ形で組み込める。単発の 1 回で済ませるより、確かめた結果を得やすくなる。これが防ぐのは、確かめていない結果を受け取ることである。担当ごとに範囲が分かれるので、長い会話の途中で指示がずれる、という合っていない結果も減ると考えられる（推論・実践例なし）。

向かない作業もある。

- 対象が数件で済む作業。サブエージェントを数個動かすほうが軽い。
- 途中で人の判断を挟む作業。実行中のワークフローは、人の入力を受けない。段の間で承認が要るなら、段ごとに別のワークフローにする。
- 担当どうしが連絡し合う作業。これは <!-- link:begin agent-teams -->エージェントチーム（複数の Claude に分担させる）<!-- link:end --> の領分である。
- 同じファイルを触る作業。担当どうしの変更がぶつかる。担当ごとに隔離したコピーで作業させられるなら使える。

### 先に決める守り

ワークフローは任せる幅を大きく広げるので、動かす前に、守りを 3 つ決めておく。

1. 費用の上限と止める条件。決め方は <!-- link:begin parallel-and-loop-costs#decide-before-starting -->[並列・ループ・workflows のコスト › 始める前に決める三つ](../cost/parallel-and-loop-costs.md#decide-before-starting)<!-- link:end --> にある。
2. 結果を確かめる者。担当の自己申告や終了の表示だけで決めない。分け方は <!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end -->、無人の結果の確かめ方は <!-- link:begin checking-unattended-runs#beyond-exit-codes -->[無人実行の結果を確かめる › 終了コードと要約だけで決めない](../verify/checking-unattended-runs.md#beyond-exit-codes)<!-- link:end --> にある。
3. 結果を読む人の側の限度。担当を増やしても、確かめる人の手間は本数に応じて増える。理由は <!-- link:begin humans-set-the-parallel-limit#why-human-side -->[並列の上限は人間が決める › 上限が人の側にある理由](humans-set-the-parallel-limit.md#why-human-side)<!-- link:end --> にある。

### 小さく試す

大きな作業で使う前に、小さな範囲で 1 回走らせて、費用と結果の質を見る。公式も、大きなタスクの前に 1 ディレクトリや狭い問いで試すことを勧めている（[Dynamic workflows の Cost](https://code.claude.com/docs/en/workflows#cost)）。

1. 対象を 1 ディレクトリか、狭い問いに絞る。
2. 最初は、ファイルを変更せず読むだけの作業にする。
3. 走っている間に `/workflows` を開き、担当ごとのトークンの使用量を見る。そこから、いつでも止められる。止めても、終わった分の結果は多くの場合残る。
4. 使用量と結果の質（誤検出の多さなど）を見てから、範囲を広げるかを決める。

進捗の行に `Large workflow` の警告が出る場合がある。出る条件は、<!-- fact:begin workflow-large-warning -->担当が 25 を超えるか、トークンの見込みが 150 万を超えたとき。size guideline を自分で選ぶと、担当の数のしきい値はその段の数に替わる。ultracode が on の間は出ない。警告は助言で、止めない（2026-11-05 時点）<!-- fact:end -->である。担当の数の目安を段階で変える設定 `workflowSizeGuideline` もあり、段階の目安は<!-- fact:begin workflow-size-guideline -->unrestricted は目安なし、small は 5 未満、medium は 10 未満、large は 50 未満。既定は medium、Pro で v2.1.271 以降は small。助言で上限ではない（2026-11-05 時点）<!-- fact:end -->である。

上限になるのは、実行環境が持つ同時に動かせる担当の数と、1 回の実行で呼べる担当の総数である。同時に動かせる担当の数は、<!-- fact:begin workflow-concurrent-agents -->既定は 16。CPU が少ないと減る。環境変数 CLAUDE\_CODE\_WORKFLOW\_MAX\_CONCURRENT\_AGENTS で 1〜256（v2.1.269 以降）（2026-11-05 時点）<!-- fact:end -->。1 回の実行の上限は、<!-- fact:begin workflow-agent-caps -->担当は 1 回の実行で合計 1000。parallel() と pipeline() の 1 回の呼び出しは 4096 件まで（2026-11-05 時点）<!-- fact:end -->。

!!! example "判断例：全ルートの認証の監査を、どこから流すか"
    - **状況**：ルートハンドラーが多数あるリポジトリで、認証の確認の抜けを全部洗い出したい。
    - **迷う候補**：最初からリポジトリ全体をワークフローで流す。または、1 ディレクトリを読むだけで試してから広げる。
    - **選んだもの**：1 ディレクトリを読むだけで試し、`/workflows` で使用量と誤検出を見てから広げる。
    - **理由**：どちらも筋が通る。ただし全体で走らせると、担当 1 つあたりの使用量も、指摘の質も分からないまま、利用枠を大きく使う。先に小さく見れば、全体の見込みを持って判断できる。

## 最小の使い方 {#minimal}

=== "Claude Code"

    1 回の作業だけをワークフローにするには、依頼に `ultracode` を含めるか、「ワークフローで」と自分の言葉で頼む。起動のキーワードは <!-- name:begin workflow-to-ultracode -->ultracode（dynamic workflows を起動するキーワード）<!-- name:end --> で、`workflow` という語だけでは起動しない。キーワードは、作業の組み立て方を選ぶだけである。担当の道具の呼び出しは、ほかの呼び出しと同じ権限の確認とサンドボックスを受ける。

    セッション全体で使うには、`/effort ultracode` にする。以後、実質的な作業のたびに Claude がワークフローを組む。この設定は落とし穴が多いので、<!-- link:begin effort-levels#how-to-set -->[effort の段階と使い分け › 面ごとの変え方](../models/effort-levels.md#how-to-set)<!-- link:end --> と、このページの「効かない場面・落とし穴」を先に読む。戻すのは `/effort ultracode off` である。

    実行の前に、計画の段が出て、承認か中止を選ぶ。スクリプトの本文を見てから決めることもできる。確認の出方は権限モードで変わる。

    走り始めたら、`/workflows` で進捗を見る。進捗の画面から、実行の一時停止、担当ごとの停止、スクリプトの保存ができる。保存すると、`.claude/workflows/`（プロジェクト）か `~/.claude/workflows/`（自分のホーム）に置かれ、次回から `/<名前>` で同じ組み立てを再実行できる。

    同梱のワークフローとして `/deep-research <問い>` がある。複数の角度から Web を調べ、出典を突き合わせ、引用付きの報告を返す。WebSearch の道具が要る。アプリの Research とは別の機能である。

## 雛形 {#templates}

最初に流す依頼は、範囲・読むだけか・確かめ方・広げたときの見込み、の 4 つを書いておく。

<!-- gen:begin snippet dynamic-workflows/scoped-trial -->
<!-- textlint-disable -->

??? example "雛形：範囲を絞って試すワークフローの依頼"

    ```markdown
    ワークフローで、<対象のディレクトリ 1 つ> の中だけを調べてほしい。リポジトリ全体には広げない。

    調べること：<探す問題を 1 文で。例：認証の確認が抜けているルートハンドラー>
    ファイルは変更しない。読むだけにする。

    担当の数は少なめにする。強いモデルが要らない段（ファイルの一覧づくりなど）は、小さいモデルを使う。
    見つけた問題は、別の担当に反証させてから報告する。反証の担当が確かめきれなかったものは「未検証」として分けて出す。

    最後に、次の 3 つを報告する。
    1. 見つけた問題の一覧（場所と理由）
    2. 未検証のものの一覧
    3. 全体に広げるとしたら、担当の数と所要の見込みがどのくらい増えそうか
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.154。

<!-- textlint-enable -->
<!-- gen:end snippet dynamic-workflows/scoped-trial -->

変更を伴う移行は、隔離したコピーで作業させ、触らせないものと確かめるコマンドを先に書く。

<!-- gen:begin snippet dynamic-workflows/scoped-migration -->
<!-- textlint-disable -->

??? example "雛形：大量の移行を、1 ディレクトリで試す依頼"

    ```markdown
    ワークフローで、<移行の内容。例：JavaScript から TypeScript へ> の移行を、<対象のディレクトリ 1 つ> の中だけで試したい。

    - ファイルごとに別の担当が、そのファイルの隔離したコピーの中で変換する。担当どうしで同じファイルを触らせない。
    - 変換のたびに、<確かめるコマンド。例：型検査とそのディレクトリのテスト> を流し、通ったものだけを採用する。
    - 触ってよいのは、このディレクトリの中のソースだけにする。設定ファイル、テスト用の設定、<触らせないもの> は変更しない。
    - 通らなかったファイルは、直さずに一覧に残す。何度も直し直させない。

    最後に、採用したファイルの数、通らなかったファイルの一覧、変更の差分の見方を報告する。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.154。

<!-- textlint-enable -->
<!-- gen:end snippet dynamic-workflows/scoped-migration -->

移行の分け方と、挙動が保たれたことの確かめ方は <!-- link:begin refactor-and-migrate#bulk-changes -->[リファクタリングと大規模な移行 › 多数のファイルに同じ変更を流す](../recipes/refactor-and-migrate.md#bulk-changes)<!-- link:end --> と <!-- link:begin refactor-and-migrate#behavior-preserved -->[リファクタリングと大規模な移行 › 挙動が変わっていないことを確かめる](../recipes/refactor-and-migrate.md#behavior-preserved)<!-- link:end --> が扱う。

## 担当にも効く縛り、確かめていない縛り {#guards-for-workers}

ワークフローの担当は、サブエージェントの規則で動く。担当は利用者の権限ルールを使い、権限モードもサブエージェントの規則で決まる（[Dynamic workflows](https://code.claude.com/docs/en/workflows#approve-the-plan-before-it-runs)）。担当の道具の呼び出しには、ほかの呼び出しと同じ権限の確認とサンドボックスが掛かる。文書で効くと分かっているのは、この 2 つである。

- **権限ルール**：deny ルールは担当にも効く。評価の順番は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end --> にある。ただし、担当が起こす子プロセスには権限ルールが届かない（<!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end -->）。
- **サンドボックス**：コマンドの読み書きと通信を OS の層で囲う。囲える範囲と、読み取りが既定で広い点は <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> と <!-- link:begin sandboxing#default-reads -->[サンドボックスで封じ込める › 読み取りは既定で広い](../enforce/sandboxing.md#default-reads)<!-- link:end --> にある。

確かめていない縛りもある。設定のフックが、ワークフローの担当の中で走るかどうかは、文書に明記がない。フックはサブエージェントの中で走ると書かれているので、走ると読める。しかし、ワークフローの担当について書いた箇所は見つからない。この辞典は、フックだけに頼る縛りを、確かめるまで勧めない。フックの置き場所と効く範囲は <!-- link:begin hooks-basics#locations -->[フックの考え方とイベント › 置き場所と効く範囲（サブエージェントと信頼の確認）](../enforce/hooks-basics.md#locations)<!-- link:end --> にある。

自分の環境で確かめるには、無害な操作を止めるフックを置き、小さなワークフローの担当にその操作を試させる。止まったかどうかを、担当の記録と差分で見る。確かめた版と日付は手元に残す。

長い走りで確認が止まるのを避けたいときは、担当に要る道具を、あらかじめ allow ルールに足しておく。ただし、足すほど担当が動ける範囲は広がる。足すのは、読むだけの道具や対象のディレクトリに限り、触らせないものの deny ルールは残す。

!!! example "判断例：触らせたくないファイルを、どの仕組みで止めるか"
    - **状況**：テストの設定ファイルを、移行のワークフローの担当に変更させたくない。
    - **迷う候補**：変更を検知して止めるフックを置く。または、deny ルールとサンドボックスの書き込み範囲で止める。
    - **選んだもの**：deny ルールとサンドボックスの書き込み範囲で止め、フックは追加の確認にとどめる。
    - **理由**：担当にも効くと文書で分かるのは、権限ルールとサンドボックスである。フックが担当の中で走るかは確かめられていない。確かめられた縛りを本線にして、確かめていないものは補助に回す。

実行が終わったら、返ってきた要約だけで決めず、記録と差分で確かめる。やり方は <!-- link:begin checking-unattended-runs#records -->[無人実行の結果を確かめる › 記録と差分で確かめる](../verify/checking-unattended-runs.md#records)<!-- link:end --> にある。検証の担当が確かめられなかった主張は、報告に「未検証」として載る。反証された主張とは別物なので、読むときに分ける。

## 効かない場面・落とし穴 {#pitfalls}

- **`/effort ultracode` を付けたままにする**：実質的な作業のたびにワークフローが組まれ、1 つの依頼が複数のワークフローに分かれることもある。すると同じ作業でも、使うトークンと時間が増え、サブスクリプションでは上限に早く届く。しかも、この設定の間は `Large workflow` の警告が出ず、auto モードでも最初の起動の承認を聞かれない。思ったより利用枠を使った、という症状の最初の疑いどころである。日常の作業に戻るときは `/effort ultracode off` にする。
- **`-p` やスケジュールの依頼でキーワードを頼る**：`ultracode` のキーワードは、自分が打った依頼でだけ起動の合図になる。`-p` で渡した依頼や、スケジュールされた依頼には効かない。`-p` では、Workflow の起動も権限の評価を通るので、起動を許すには allow ルールなどが要る。
- **途中の承認を前提にする**：実行中は人の入力を受けない。段の間に人の確認を置きたいときは、段ごとに別のワークフローにする。
- **失敗した担当の後ろが走り直す**：再開すると、失敗した担当より後に始まった担当も走り直す。途中で失敗すると、終わっていた作業のトークンを、もう一度使うことがある。
- **上限に当たる**：使用上限に当たると、条件が合えば実行は上限が戻るまで待って続き、合わなければ担当が失敗する。どちらになるかの条件は、公式の文書で確かめる。長い走りの前に上限の残りを見ておく。
- **倍率の数字を見積もりに使う**：マルチエージェントは通常のチャットよりずっと多くのトークンを使う、という話に倍率が添えられていることがある。2025 年の Research 機能の値なら、Claude Code のワークフローには直接当てはまらない。見積もりは、小さく走らせた `/workflows` の使用量から立てる。費用の膨らみ方は <!-- link:begin parallel-and-loop-costs#multiplication -->[並列・ループ・workflows のコスト › 費用が膨らむ掛け算](../cost/parallel-and-loop-costs.md#multiplication)<!-- link:end --> にある。
- **担当のモデルを見落とす**：担当のモデルは、指定がなければ、そのセッションのモデルで動く。大きな走りの前に `/model` を確かめ、強いモデルが要らない段は小さいモデルでよい、と依頼で伝える。

## 比べる相手 {#compare}

- **<!-- link:begin choosing-parallel-modes#compare -->[並列の方式の選び方 › 方式の比較](choosing-parallel-modes.md#compare)<!-- link:end -->**：並列の方式の全体の比較。誰が調整するかで選ぶ。
- **<!-- link:begin batch-and-p-loops -->多数のファイルに同じ作業を流す（/batch と -p のループ）<!-- link:end -->**：多数のファイルに同じ作業を、自分が書いたループで流す。計画を自分が持ちたいとき、ワークフローではなくこちらを選ぶ。
- **<!-- link:begin agent-teams -->エージェントチーム（複数の Claude に分担させる）<!-- link:end -->**：担当どうしが連絡し合うとき。ワークフローの担当は互いに話さず、スクリプトがつなぐ。
- **<!-- link:begin goal-until-done -->[/goal（完了するまで続けさせる）](goal-until-done.md)<!-- link:end -->**：検証できる終わりの条件まで、順番に回し続けるとき。依存のある直列の作業は /goal、独立した並列の作業はワークフロー、という分け方が実務家の間にある（根拠：弱）。
- **<!-- link:begin research-in-subagents -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)<!-- link:end -->**：出力の多い調査を 1 つ任せるだけなら、サブエージェント 1 つで足りる。

## 古くなった助言 {#outdated}

起動の合図を `workflow` という語にしている手順書は、古い。今は <!-- name:begin workflow-to-ultracode -->ultracode（dynamic workflows を起動するキーワード）<!-- name:end --> と書くか、「ワークフローで」と自分の言葉で頼む。セッション全体なら `/effort ultracode` にする。超過分を払う仕組みの呼び名も替わった。手順書の `extra usage` と `/extra-usage` は、今は <!-- name:begin extra-usage-to-usage-credits -->usage credits（/usage-credits）<!-- name:end --> である。旧名のコマンドも動く。台帳の行は <!-- link:begin outdated-advice-ledger#workflow-keyword-extra-usage -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#workflow-keyword-extra-usage)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Orchestrate subagents at scale with dynamic workflows](https://code.claude.com/docs/en/workflows)：Anthropic・英語・確認日 2026-11-04
- [Run agents in parallel](https://code.claude.com/docs/en/agents)：Anthropic・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [並列の方式の選び方](choosing-parallel-modes.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)

**関連**

- [並列・ループ・workflows のコスト](../cost/parallel-and-loop-costs.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [フックの考え方とイベント](../enforce/hooks-basics.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [無人実行の結果を確かめる](../verify/checking-unattended-runs.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)
- [並列の上限は人間が決める](humans-set-the-parallel-limit.md)
- [リファクタリングと大規模な移行](../recipes/refactor-and-migrate.md)
- [effort の段階と使い分け](../models/effort-levels.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
