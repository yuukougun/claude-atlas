---
id: choosing-parallel-modes
title: 並列の方式の選び方
aliases: [並列実行, Run agents in parallel, マルチエージェント]
type: comparison
field: delegate
chapter: 並べる
order: 90
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [見せる, 握る]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: 並列の方式を、誰が調整するか・同じファイルを触るか・互いに連絡が要るかで選べる。どの方式でも、結果を確かめる人の手間は本数に応じて増える。
signs:
  - {type: goal, text: 複数の作業を同時に進めたい}
  - {type: symptom, text: 並列の方法が多すぎて、どれを使えばいいか分からない}
prerequisites: [subagent-isolation]
related: [humans-set-the-parallel-limit, parallel-with-worktrees, agent-view-and-background, agent-teams, dynamic-workflows, batch-and-p-loops, compare-hypotheses-in-parallel, writing-subagents, skill-vs-subagent, research-in-subagents, independent-review, sandboxing, parallel-and-loop-costs, cloud-sessions-and-teleport]
tracks: [subagents, agent-view, agent-teams, workflows, worktrees, code-projects]
outdated_advice: [subagent-per-step, subagents-to-save-context]
sources: [cc-docs-agents, cc-docs-sub-agents, cc-docs-agent-view, cc-docs-agent-teams, cc-docs-workflows, cc-docs-worktrees, cc-docs-claude-projects, marmelab-code-tips-wish-id-had, dsebastien-code-tips-best-practices, mitchellh-writing-ai-adoption-journey, paddo-boris-uses-code, infoq-code-creator-workflow]
volatility: 中
sections:
  - {title: 方式の比較, anchor: compare}
  - {title: 誰が調整するか, anchor: who-coordinates}
  - {title: 同じファイルを触るか, anchor: same-files}
  - {title: 一部は捨てる前提で回す, anchor: expect-to-discard}
  - {title: 組み合わせ方, anchor: combine}
  - {title: 結果の確かめ方, anchor: how-to-check}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：調整する者が Claude ならサブエージェントかエージェントチーム、自分なら agent view、スクリプトなら workflows を選ぶ。同じファイルを触るなら worktree で分ける。
    - **いつ引くか**：複数の作業を同時に進めたいが、並列の方法が多すぎて、どれを使えばいいか分からないとき。
    - **前提**：<!-- link:begin subagent-isolation -->[サブエージェントは別室の部下](../basics/subagent-isolation.md)<!-- link:end -->
    - **共通の注意**：どの方式でも、結果を確かめる人の手間は本数に応じて増える。

<!-- textlint-disable -->
別名：並列実行・Run agents in parallel・マルチエージェント
<!-- textlint-enable -->

並列の方式の選び方は、Claude Code で複数の作業を同時に進める方式から、作業に合うものを選ぶための比較である。方式は増減しうるので、数や成熟度はこのページに書かず、表から読む。選ぶ軸は 3 つある。誰が調整するか、同じファイルを触るか、互いに連絡が要るかである。

並列は任せる幅を広げるので、方式を選ぶ前に、確かめる手段と費用の上限を決めておく。確かめる人の分け方は <!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end -->、費用は <!-- link:begin parallel-and-loop-costs#decide-before-starting -->並列・ループ・workflows のコスト › 始める前に決める三つ（準備中）<!-- link:end -->、同時に動かす本数の上限は <!-- link:begin humans-set-the-parallel-limit -->[並列の上限は人間が決める](humans-set-the-parallel-limit.md)<!-- link:end --> にある。

## 方式の比較 {#compare}

次の表は、並列の方式として扱う Claude Code の機能を並べたものである。属性は数値ファイルから道具が作る。

<!-- gen:begin compare 成熟度 入った版 -->
<!-- textlint-disable -->

| 機能 | 成熟度 | 入った版 |
| --- | --- | --- |
| サブエージェント（subagents）（準備中） | GA | 1.0.60（2025-07-24） |
| agent view（準備中） | research preview | 2.1.139（2026-05-11） |
| エージェントチーム（agent teams）（準備中） | experimental | 2.1.32（2026-02-05） |
| ワークフロー（workflows）（準備中） | GA | 2.1.154（2026-05-28） |
| worktree（準備中） | GA | 2.1.49（2026-02-19） |
| [Claude Code の Projects（並列の threads）](choosing-parallel-modes.md) | beta | — |

<!-- textlint-enable -->
<!-- gen:end compare 成熟度 入った版 -->

表の読み方は 3 つある。

- worktree は方式ではなく、作業ごとに作業場所を分ける仕組みである。同じファイルを触るときに、ほかの方式へ足す。
- Claude Code の Projects は、アプリの projects とは別の機能である。claude.ai/code か Desktop アプリの 1 つの会話から、Claude がタスクごとに並列のセッション（threads）を始める。使えるプランは変わるので、[公式の文書](https://code.claude.com/docs/en/claude-projects)で確かめる。
- 成熟度の欄が安定版でない方式は、画面やキーが変わりうる。操作の手順は各方式のページに任せ、このページでは選ぶ基準だけを扱う。

## 誰が調整するか {#who-coordinates}

誰が作業を割り当て、進み具合を見て、結果をまとめるのかで、並列の方式は分かれる。公式の文書も、この軸を最初の基準にしている（[Run agents in parallel](https://code.claude.com/docs/en/agents)）。

| 方式 | 調整する者 | 向く作業 | 詳しく |
| --- | --- | --- | --- |
| サブエージェント | Claude が、1 つの会話の中で | 並べられる独立の作業・出力が多い作業の切り離し・独立したレビュー | <!-- link:begin writing-subagents#when-to-use -->サブエージェントの作り方と使いどころ › 使いどころと、使わない場面（準備中）<!-- link:end --> |
| agent view | 自分が背景のセッションに投入し、後で確認する | 見張らなくてよい独立した作業 | <!-- link:begin agent-view-and-background#what-fits -->agent view と背景セッション › 向く作業と向かない作業（準備中）<!-- link:end --> |
| エージェントチーム | リードの Claude が計画・割り当て・監督をする | 互いに連絡しながら進める、小さく焦点を絞った作業 | <!-- link:begin agent-teams -->エージェントチーム（複数の Claude に分担させる）（準備中）<!-- link:end --> |
| workflows | Claude が書いたスクリプトが計画を持つ | コードベース全体の監査や、大量のファイルの移行 | <!-- link:begin dynamic-workflows#when-and-start-small -->dynamic workflows（スクリプトで多数のサブエージェントを動かす） › 向く規模と、小さく試す（準備中）<!-- link:end --> |
| Projects | Claude が、続いている会話の中で | 会話を軸に、タスクごとに threads を分けたい作業 | [Let Claude coordinate ongoing work with Projects](https://code.claude.com/docs/en/claude-projects) |
| /batch と claude -p のループ | 自分が出したコマンドかループ | 同じ作業を多数のファイルに流す | <!-- link:begin batch-and-p-loops#not-the-batch-api -->多数のファイルに同じ作業を流す（/batch と -p のループ） › API の Message Batches API とは別のもの（準備中）<!-- link:end --> |

互いに連絡が要るかは、この軸とほぼ重なる。サブエージェントは別の文脈で作業して、要約だけを返す。エージェントチームだけが、共有のタスクリストと相互のメッセージで、担当どうしが途中経過を渡し合える。途中経過を渡し合う必要がなければ、エージェントチームを選ぶ理由は薄い。チームメイトの数だけトークンを使うからである。背景のセッションに別のセッションから知らせたいだけなら、<!-- link:begin agent-view-and-background#cross-session-messaging -->agent view と背景セッション › ほかのセッションに知らせる（cross-session messaging）（準備中）<!-- link:end --> で足りる。

サブエージェントを選ぶ理由に、コンテキストの節約だけを置かない。工程ごとにサブエージェントを作る形は <!-- link:begin outdated-advice-ledger#subagent-per-step -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#subagent-per-step)<!-- link:end -->、コンテキストを守るためだけに調べさせる形は <!-- link:begin outdated-advice-ledger#subagents-to-save-context -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#subagents-to-save-context)<!-- link:end --> が扱う。今は、並べる作業・うるさい出力を本筋から離すこと・独立したレビューのために使い、どれもトークンが余分にかかる。

!!! example "判断例：調査 3 件を、手元の実装と並べたい"
    - **状況**：ある不具合の原因を、ログ・設定・依存の 3 方向から調べたい。その間に、手元では別の機能を実装し続ける。調べた結果は、あとで 1 か所にまとめて読めればよい。
    - **迷う候補**：サブエージェントに 3 方向を並べさせる。agent view で 3 つの背景セッションに投入する。
    - **選んだもの**：サブエージェントに 3 方向を並べさせる。
    - **理由**：3 件は互いに連絡が要らず、要約だけ戻れば足りる。ログのような出力の多い調べものは、別の文脈に切り離せる。agent view は、時間のかかる作業を手元から完全に離したいときに筋が通る。ただし今回は、結果を今の会話に戻して続きの判断に使いたいので、戻り方が決まっているサブエージェントが合う。

## 同じファイルを触るか {#same-files}

同じファイルを触る作業を同じ作業場所で並べると、互いの変更が上書きされる。公式の文書の基準は、触るなら worktree で隔離する、である。エージェントチームは worktree で隔離しないので、担当をファイル単位で分ける。

- 触るファイルが重なる作業：作業ごとに worktree を作り、別のセッションで進める。依存の導入・秘密のファイルの写し方・データベースは worktree ごとに決める。手順は <!-- link:begin parallel-with-worktrees#per-worktree-setup -->git worktree で並列にする › worktree ごとの準備（依存・秘密・データベース）（準備中）<!-- link:end --> にある。
- 触るファイルが重ならない作業：worktree は要らない。分けると、準備と片付けの手間だけが増える。
- エージェントチームで進める作業：チームメイトごとに担当のファイルを決め、同じファイルを 2 人に渡さない。
- 同じ作業を多数のファイルに流す作業：/batch は、worktree で隔離したサブエージェントに分けて進める。範囲の決め方は <!-- link:begin batch-and-p-loops -->多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）<!-- link:end --> にある。

worktree は、片付けも要る。残すものと消すものは <!-- link:begin parallel-with-worktrees#cleanup -->git worktree で並列にする › 片付けと残すもの（準備中）<!-- link:end --> で決める。

!!! example "判断例：同じモジュールを触る 2 つの実装案を比べたい"
    - **状況**：認証のモジュールを、案 A と案 B の 2 通りに直したい。どちらも同じファイルを大きく書き換える。
    - **迷う候補**：エージェントチームに 2 人のチームメイトを作らせ、案ごとに割り当てる。worktree を 2 つ作り、案ごとに別のセッションで進める。
    - **選んだもの**：worktree を 2 つ作り、案ごとに別のセッションで進める。
    - **理由**：エージェントチームは worktree で隔離せず、ファイル単位の分担を前提にする。2 案は同じファイルを書き換えるので、分担のしようがない。案どうしの連絡も要らない。同じ評価器で比べて勝った方だけを取り込む流れは <!-- link:begin compare-hypotheses-in-parallel -->仮説ごとに並べて、同じ物差しで比べる（準備中）<!-- link:end --> にある。

## 一部は捨てる前提で回す {#expect-to-discard}

並列で回す作業の一部は、途中で捨てる前提にしておくとよい。全部を採用する前提で並べると、確かめる人の手間が本数に比例して増え、捨てにくくなる。

実践者の幅は広い。

- Claude Code の開発者は、複数のセッションを並べ、1〜2 割ほどは想定外の展開で途中放棄する、と語ったと報じられている（根拠：弱。本人の自己申告を二次の報道が伝えたもので、一次の資料では確かめていない）。
- 並列化は文脈の切り替えで人を疲れさせ、処理量が増えても品質が落ちうる、という指摘がある（根拠：弱。実践者の経験談）。
- 同時に回す本数は 3〜4 本ほどが限度という声がある（経験則）。複数ではなく 1 本のエージェントに絞る実践者もいる（立場の表明）。

公式の文書が示すのは、方式を選ぶ基準であり、本数や捨てる割合の数字ではない。上の 1〜2 割も、公式の数字ではない。この辞典の推奨は、個人の構成を標準にせず、少ない本数から始めることである。そのうえで、作業を 2 つに分ける。

- 捨ててよい作業：調査・使い捨ての試作・仮説の比較。多めに並べてよい。どれを捨てるかの基準と、止める条件を先に決める。
- 捨てない作業：レビューの要る本流。少なく保ち、1 本ずつ確かめる。

本流と偵察で本数を分ける考え方は <!-- link:begin humans-set-the-parallel-limit#mainline-vs-scouting -->[並列の上限は人間が決める › 本流と偵察で本数を分ける](humans-set-the-parallel-limit.md#mainline-vs-scouting)<!-- link:end --> にある。費用が本数と回数の掛け算で膨らむ理由は <!-- link:begin parallel-and-loop-costs#multiplication -->並列・ループ・workflows のコスト › 費用が膨らむ掛け算（準備中）<!-- link:end --> にある。

## 組み合わせ方 {#combine}

方式は 1 つに決めなくてよい。作業の種類ごとに、次のように置き分ける。

| 置くもの | どこに置くか | 指す先 |
| --- | --- | --- |
| 割り当てと進行 | 調整する者（Claude・スクリプト・自分）の方式 | 前の節「誰が調整するか」 |
| 作業場所の分離 | worktree（触るファイルが重なるとき） | <!-- link:begin parallel-with-worktrees -->git worktree で並列にする（準備中）<!-- link:end --> |
| 出力の多い調査 | サブエージェント。本筋には結論と根拠の場所だけを戻す | <!-- link:begin research-in-subagents#how -->出力の多い調査はサブエージェントに任せて要約だけ受け取る › 頼み方と戻させる形（準備中）<!-- link:end --> |
| 結果の確認 | 書いた本人ではない者。AI の承認は人の承認に数えない | <!-- link:begin independent-review#ai-approval -->[書いた本人ではない者にレビューさせる › AI の承認を人の承認に数えない](../verify/independent-review.md#ai-approval)<!-- link:end --> |
| 動かす範囲の囲い | 見張らない方式ほど、OS の層で囲む | <!-- link:begin sandboxing#when -->[サンドボックスで封じ込める › 使いどころ](../enforce/sandboxing.md#when)<!-- link:end --> |
| 手元を閉じても続ける作業 | クラウドのセッション。計画と縛りはリポジトリに置いてから送る | <!-- link:begin cloud-sessions-and-teleport#what-to-send -->クラウドセッションと teleport › クラウドに送ってよい作業（準備中）<!-- link:end --> |

手順を今の会話で読ませたいだけなら、並列にせずスキルで足りる。違いは <!-- link:begin skill-vs-subagent -->スキルとサブエージェントの違い（準備中）<!-- link:end --> にある。

方式を決めきれないときは、作業の情報を渡して、選択肢と推奨案を Claude に出させる。次の雛形は、実行させずに案だけを出させる依頼である。

<!-- gen:begin snippet choosing-parallel-modes/ask-for-mode-choice -->
<!-- textlint-disable -->

??? example "雛形：並列の方式を選ばせる依頼"

    ```markdown
    次の作業を並列で進めたい。方式は決めていない。

    作業：<並べたい作業を 1 行ずつ>
    触るファイル：<作業ごとに、触るファイルやディレクトリ>
    連絡：<作業どうしで途中の結果を渡す必要があるか>
    確かめる人：<結果を読む人と、続けて読める件数>

    次の順で答えてほしい。まだ実行しない。

    1. 作業ごとに、誰が調整する方式（サブエージェント・agent view・エージェントチーム・workflows のうち、この環境で使えるもの）が合うかを、推奨案を 1 つ選んで理由を添える。
    2. 同じファイルを触る作業があれば、worktree で分けるか、ファイル単位で分担するかを提案する。
    3. 捨ててよい作業と、捨てずに確かめる作業を分ける。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.154。

<!-- textlint-enable -->
<!-- gen:end snippet choosing-parallel-modes/ask-for-mode-choice -->

Claude の推奨は、本文の基準と食い違うことがある。食い違ったら、触るファイルと連絡の要否を自分で見直してから決める。

## 結果の確かめ方 {#how-to-check}

方式ごとに、結果の戻り方が違う。戻り方に合わせて確かめる。

- 背景のセッション：`claude agents` で状態の一覧を開く。返事の要るセッションだけを見に行く。
- セッションの中の背景作業：`/tasks` で見る。
- workflows：`/workflows` で見る。
- サブエージェント：返るのは要約だけなので、要約をそのまま信じず、根拠の場所まで見る。

コマンドの名前と画面は、公式の文書で確かめる（[Run agents in parallel](https://code.claude.com/docs/en/agents)）。確かめる手間は、どの方式でも本数に応じて増える。確認が追いつかなくなった兆しは <!-- link:begin humans-set-the-parallel-limit#signs-of-fatigue -->[並列の上限は人間が決める › 疲れの兆し](humans-set-the-parallel-limit.md#signs-of-fatigue)<!-- link:end --> にある。兆しが出たら、新しい作業を足さず、本数を減らす。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Run agents in parallel](https://code.claude.com/docs/en/agents)：Anthropic・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Manage multiple agents with agent view](https://code.claude.com/docs/en/agent-view)：Anthropic・英語・確認日 2026-11-04
- [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams)：Anthropic・英語・確認日 2026-11-04
- [Orchestrate subagents at scale with dynamic workflows](https://code.claude.com/docs/en/workflows)：Anthropic・英語・確認日 2026-11-04
- [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees)：Anthropic・英語・確認日 2026-11-04
- [Let Claude coordinate ongoing work with Projects](https://code.claude.com/docs/en/claude-projects)：Anthropic・英語・確認日 2026-11-04
- [Claude Code Tips I Wish I’d Had From Day One](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)：marmelab・英語・確認日 2026-11-04
- [Claude Code Tips and Best Practices](https://www.dsebastien.net/claude-code-tips-and-best-practices/)：Sébastien Dubois・英語・確認日 2026-11-04
- [My AI Adoption Journey](https://mitchellh.com/writing/my-ai-adoption-journey)：Mitchell Hashimoto・英語・確認日 2026-11-04
- [How the Creator of Claude Code Uses Claude Code](https://paddo.dev/blog/how-boris-uses-claude-code)：paddo.dev・英語・確認日 2026-11-04
- [Inside the Development Workflow of Claude Code's Creator](https://www.infoq.com/news/2026/01/claude-code-creator-workflow/)：InfoQ・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [サブエージェントは別室の部下](../basics/subagent-isolation.md)

**次に読む**

- agent view と背景セッション（準備中）
- dynamic workflows（スクリプトで多数のサブエージェントを動かす）（準備中）
- エージェントチーム（複数の Claude に分担させる）（準備中）

**関連**

- [並列の上限は人間が決める](humans-set-the-parallel-limit.md)
- git worktree で並列にする（準備中）
- 多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）
- 仮説ごとに並べて、同じ物差しで比べる（準備中）
- サブエージェントの作り方と使いどころ（準備中）
- スキルとサブエージェントの違い（準備中）
- 出力の多い調査はサブエージェントに任せて要約だけ受け取る（準備中）
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- 並列・ループ・workflows のコスト（準備中）
- クラウドセッションと teleport（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
