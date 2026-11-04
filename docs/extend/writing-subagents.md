---
id: writing-subagents
title: サブエージェントの作り方と使いどころ
aliases: [subagent, カスタムサブエージェント, .claude/agents, /agents]
type: feature
field: extend
chapter: サブエージェント
order: 150
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [見せる, 確かめる]
prevents: [散らかっている, 確かめていない]
pitfalls: []
scenes: [開発]
summary: 調査・レビュー・出力の多い作業を、別の文脈で動く担当として定義できる。工程ではなく文脈の独立で分け、道具とモデルを絞り、余分なトークンがかかることを踏まえて使う。
signs:
  - {type: goal, text: 調査やレビューを、本筋の会話とは別の担当に任せたい}
  - {type: goal, text: 決まった役割の担当を、毎回同じ設定で呼びたい}
  - {type: symptom, text: 工程ごとに担当を作ったら、受け渡しの調整に追われている}
  - {type: symptom, text: 昔の記事の手順でサブエージェントを作ろうとしたら、作成の画面が出てこない}
prerequisites: [subagent-isolation]
related: [what-subagents-dont-inherit, skill-vs-subagent, research-in-subagents, independent-review, instructing-reviewers, permission-rules, hook-recipes#subagent-only, hooks-basics, choosing-parallel-modes, agent-teams, what-not-to-delegate, parallel-and-loop-costs, split-models-by-role, effort-levels#subagents-and-org-limits, skill-descriptions, agreement-is-not-evidence#reviewer-agreement]
tracks: [subagents]
outdated_advice: [agents-command, subagent-per-step, tell-it-to-use-subagents, subagents-to-save-context]
sources: [cc-docs-sub-agents, cc-docs-best-practices, cc-docs-commands, cc-docs-hooks, cc-changelog, api-docs-prompting-opus-5]
volatility: 中
sections:
  - {title: 定義の書き方（ファイルを書くか、Claude に作らせる）, anchor: define}
  - {title: 使いどころと、使わない場面, anchor: when-to-use}
  - {title: 道具・モデル・effort を絞る, anchor: tools-and-model}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：調査・レビュー・出力の多い作業を、道具とモデルを絞った別の文脈の担当として定義し、毎回同じ設定で呼べる。
    - **いつ引くか**：調査やレビューを本筋の会話から任せたいとき、担当を作ったら受け渡しの調整に追われているとき、昔の記事の手順で作成の画面が出ないとき。
    - **前提**：<!-- link:begin subagent-isolation -->[サブエージェントは別室の部下](../basics/subagent-isolation.md)<!-- link:end -->
    - **強制力**：定義の指示（description と本文）はお願いで、道具の制限（`tools`・`disallowedTools`）は鍵である。鍵が止められるのは道具の単位までで、特定のコマンドだけは止められない。成熟度は <!-- gen:begin feature maturity -->GA<!-- gen:end feature maturity -->、読み込みの時期は <!-- gen:begin feature load_timing -->起動したとき<!-- gen:end feature load_timing -->、コンテキストのコストは <!-- gen:begin feature context_cost -->分離<!-- gen:end feature context_cost --> である。

<!-- textlint-disable -->
別名：subagent・カスタムサブエージェント・.claude/agents・/agents
<!-- textlint-enable -->

サブエージェントの作り方と使いどころは、別の文脈で動く担当を定義し、どの作業を任せるかを決める話である。担当は自分のシステムプロンプトと道具の制限を持ち、作業の結果を要約にして本筋へ返す。ここでは、定義の書き方、使う場面と使わない場面、道具とモデルの絞り方を扱う。

## 定義の書き方（ファイルを書くか、Claude に作らせる） {#define}

サブエージェントの定義は、Markdown のファイルである。作る方法は 2 つあり、どちらも同じ形のファイルができる。

=== "Claude Code"

    1. **Claude に作らせる**：役割・置き場所・使う道具・モデルを伝えて、定義を書かせる。頼み方は下の雛形にある。作られたファイルは、必ず自分で読む。
    2. **ファイルを直接書く**：プロジェクトなら `.claude/agents/<名前>.md`、自分の全プロジェクトなら `~/.claude/agents/<名前>.md` に置く。
    3. **一時的に使う**：セッションの間だけなら、`--agents` に JSON を渡す方法もある。プラグインに入れて配ることもできる。

    以前あった `/agents` の作成画面（ウィザード）は、もうない。今の `/agents` は、上の 2 つのやり方を知らせる文を出すだけである。

同じ名前の定義が複数あるときは、管理設定、`--agents`、プロジェクト、ユーザー、プラグインの順で、前のものが使われる。

フロントマターで最初に覚えるのは次のキーである。全部のキーは公式の [Create custom subagents](https://code.claude.com/docs/en/sub-agents) にある。

| キー | 役割 |
| --- | --- |
| `name`・`description` | 必須。`description` は、いつ呼ぶかを先頭に具体的に書く。短くし、詳しい手順は本文へ置く |
| `tools`・`disallowedTools` | 使える道具を並べるか、外す道具を並べる（下の「道具・モデル・effort を絞る」） |
| `model`・`effort` | 担当が動くモデルと effort（同じく下の節） |
| `skills` | 起動したときに、指定したスキルの全文をその担当へ読み込ませる |
| `hooks` | その担当が動く間だけ走るフック |
| `memory` | 担当が持つ永続のメモリ。公式は `project` の範囲を既定に勧めている |
| `isolation` | `worktree` を指定すると、担当が独立した作業ツリーで動く |

本文は、その担当のシステムプロンプトになる。担当は起動したときに、この本文、指定したスキル、CLAUDE.md、git status で新しい文脈を作る。組み込みの調査用の Explore と、plan mode 用の Plan は、CLAUDE.md と git status を持たない。本筋の会話で話した内容は渡らないので、担当に守らせたい規則は、定義か呼ぶときの依頼に書き直す（<!-- link:begin what-subagents-dont-inherit -->サブエージェントに引き継がれないもの（準備中）<!-- link:end --> を見る）。

担当を呼ぶ方法は 3 つある。依頼に「X のサブエージェントを使って」と書く、`@"X (agent)"` と書いて確実に呼ぶ、`claude --agent X` で本体をその担当として起動する、である。Claude に自動で呼ばせたいなら、description に、いつ使うかをはっきり書く。description の書き方はスキルと共通する点が多い（<!-- link:begin skill-descriptions -->[スキルの description の書き方](skill-descriptions.md)<!-- link:end --> を見る）。

役割を伝えて、定義を書かせるプロンプトの雛形を示す。

<!-- gen:begin snippet writing-subagents/ask-claude-to-define -->
<!-- textlint-disable -->

??? example "雛形：役割を伝えて、サブエージェントの定義を書かせるプロンプト"

    ```markdown
    次の役割のサブエージェントを、このプロジェクト用に作ってください。

    - 役割：<何を任せるか。例：変更の差分を読み、バグの疑いだけを報告する>
    - 置き場所：.claude/agents/（このリポジトリで共有する）。自分の全プロジェクトで使うなら ~/.claude/agents/
    - 使う道具：<例：Read・Grep・Glob だけ。編集とコマンドの実行は許さない>
    - モデルと effort：<指定がなければ、本体と同じにする>
    - description：先頭に「どんなときに呼ぶか」を具体的に書く。自動で呼ばせたいときは、その旨も書く
    - 本文（システムプロンプト）：手順と、報告の形を書く。長い手順は本文に置き、description は短くする

    作ったら、ファイルの場所と、どんなときに呼ばれるかを教えてください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet writing-subagents/ask-claude-to-define -->

## 使いどころと、使わない場面 {#when-to-use}

サブエージェントを使うのは、文脈を分ける意味のある作業に限る。分ける軸は、工程ではなく、文脈が独立しているかどうかである。向くのは次の 4 つで、どれもトークンが余分にかかる。

- **出力が多くて、本筋に残したくない作業**：すべてのテストの実行や、広い検索。長い出力は担当の側に残り、本筋には要約だけが戻る。防ぐ原因は「散らかっている」である（仕組みは <!-- link:begin subagent-isolation#what-it-helps -->[サブエージェントは別室の部下 › 何に効くか（原理「見せる」と原因「散らかっている」）](../basics/subagent-isolation.md#what-it-helps)<!-- link:end --> を見る）。
- **書いた過程を見ていない者のレビュー**：変更を生んだ推論を見ていない担当が確かめる。防ぐ原因は「確かめていない」である（<!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end --> と <!-- link:begin instructing-reviewers#exhaustive-then-filter -->レビュアーへの指示の書き方 › 網羅と選別を分ける（準備中）<!-- link:end --> を見る）。
- **並べられる独立した作業**：互いの結果に依存しない調査を同時に進める。並べる前に、同時に動かす数・止める条件・費用の上限を決める（<!-- link:begin parallel-and-loop-costs#decide-before-starting -->[並列・ループ・workflows のコスト › 始める前に決める三つ](../cost/parallel-and-loop-costs.md#decide-before-starting)<!-- link:end --> を見る）。数は環境変数の `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` と `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` で縛れる。
- **道具を絞った役**：編集できないレビュアーのように、できることを減らした担当。

調査を任せる頼み方と戻させる形は <!-- link:begin research-in-subagents#how -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 頼み方と戻させる形](../context/research-in-subagents.md#how)<!-- link:end --> にある。読み取りだけの探索なら、組み込みの Explore がすでにあるので、自作の前にそれで足りるかを確かめる。

次の場面では使わない。

- **前の結果に次が依存する作業**：順番に進めるほうが、受け渡しがない分だけ速い。
- **同じファイルを触る作業**：担当どうしが衝突する。分け方は <!-- link:begin choosing-parallel-modes#same-files -->[並列の方式の選び方 › 同じファイルを触るか](../delegate/choosing-parallel-modes.md#same-files)<!-- link:end --> を見る。
- **小さな作業**：担当は文脈を集め直すので、かえって遅くなることがある。
- **担当どうしの連絡が要る作業**：サブエージェントは結果を本筋へ返すだけである。互いに連絡させたいなら <!-- link:begin agent-teams -->エージェントチーム（複数の Claude に分担させる）（準備中）<!-- link:end --> を検討する。
- **役の作りすぎ**：専門の担当を増やすほど、呼び分けと受け渡しの調整が増える。

担当に渡しても、同じ作業の答えはよくならない。よくなるのは、書く過程を見ていない者に別のレビューを頼むときである。コンテキストの窓を守るためだけにも使わない。窓が溢れることはまれになったので、使う理由は、出力の切り離し・並列・独立したレビューのどれかに置く。評価や採否のように、そもそも任せない仕事は <!-- link:begin what-not-to-delegate#verifiable-axis -->[任せないもの（評価・採否・撤退・中核の理解） › 分ける軸：機械的に確かめられるか](../delegate/what-not-to-delegate.md#verifiable-axis)<!-- link:end --> で分ける。

!!! example "判断例：工程ごとに担当を作るか"
    - **状況**：実装・テスト・レビュー・文書の 4 工程があり、工程ごとに担当を作ろうか迷っている。
    - **迷う候補**：工程ごとに 4 つの担当を作る。文脈が独立している作業だけを担当にする。
    - **選んだもの**：テストの実行（出力が長い）と、独立したレビュー（書いた過程を見せない）の 2 つだけを担当にし、実装と文書は本筋で進める。
    - **理由**：実装と文書は直前までの会話に強く依存するので、分けると文脈の渡し直しで手間が増える。切り離して得をするのは、出力が長い作業と、過程を見ていない目が要る作業である。

## 道具・モデル・effort を絞る {#tools-and-model}

担当の定義で絞れるのは、道具・モデル・effort の 3 つである。絞る目的は、できることを減らして事故を減らし、軽い作業の費用を抑えることである。

**道具**：`tools` に使える道具を並べる（許可の側）。`disallowedTools` には外す道具を並べる（禁止の側）。レビュー系は、`tools: Read, Grep, Glob` だけにする。編集の道具がないので、ハーネスが編集できないことを保証する。この形は、下の 1 つ目の雛形にある。道具の単位は、MCP ならサーバーごとにも指定できる。

**モデル**：`model` を省くと、本体のモデルを継承する。軽い作業の担当には軽いモデルを指定できる。分ける価値があるかは、仕事の重さの差と費用で決める（<!-- link:begin split-models-by-role#when-to-split -->計画・実装・サブエージェントでモデルを分ける › 分ける価値があるとき（準備中）<!-- link:end --> を見る）。

**effort**：担当の `effort` で、考える深さを担当ごとに変えられる。環境変数 `CLAUDE_CODE_SUBAGENT_EFFORT` は、ほかに指定がないときに担当が動く effort になる。本体と違うモデルで動く担当は、セッションの effort を受け継がず、そのモデルに保存された effort か、そのモデルの既定で動く。軽いモデルを指定した担当は、そのモデルの既定の effort で動くということである。この挙動は更新履歴で確かめたもので、公式の担当の文書には記述がない。詳しくは <!-- link:begin effort-levels#subagents-and-org-limits -->[effort の段階と使い分け › サブエージェントと組織の上限](../models/effort-levels.md#subagents-and-org-limits)<!-- link:end --> を見る。

雛形を 2 つ示す。1 つ目は、編集できないレビュアーである。

<!-- gen:begin snippet writing-subagents/reviewer -->
<!-- textlint-disable -->

??? example "雛形：編集できないレビュアー（道具を Read・Grep・Glob に絞る）"

    ```markdown
    ---
    name: reviewer
    description: 変更の差分を読み、バグの疑いと根拠を報告するレビュアー。コードは編集しない。実装を終えた後やコミットの前に、書いた本人とは別の目で確かめたいときに使う。
    tools: Read, Grep, Glob
    ---

    あなたは変更を読んで報告するだけのレビュアーである。ファイルを編集しない。

    - 渡された差分と、確かめる基準だけを根拠にする。実装の経緯や意図の説明は求めない
    - まず、疑いを漏れなく挙げる。確からしさが低いものも、ここでは捨てない。選別は呼んだ側が行う
    - 指摘ごとに、場所（ファイルと行）、問題、確かめ方（読む箇所か、実行してほしいコマンド）を書く
    - 直し方の提案や、書き換えたコードは出さない
    - 疑いが 1 件もないときは、何を確かめたかを書いて、0 件と報告する
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet writing-subagents/reviewer -->

2 つ目は、テストを走らせて失敗だけを報告する担当である。出力が長い作業を、本筋から離す例になる。

<!-- gen:begin snippet writing-subagents/test-runner -->
<!-- textlint-disable -->

??? example "雛形：テストを走らせて失敗だけを報告する担当"

    ```markdown
    ---
    name: test-runner
    description: テストスイート全体を走らせ、失敗したものだけを報告する。出力が長くなるテストの実行を、本筋の会話から離したいときに使う。
    tools: Bash, Read, Grep, Glob
    model: haiku
    ---

    あなたはテストを走らせて、失敗だけを報告する担当である。ファイルを編集しない。

    - 実行するコマンドは、依頼に書かれたものを使う。書かれていなければ、リポジトリの README かビルドの設定から探して、使ったコマンドを報告に書く
    - 報告には、実行したコマンド、終了コード、全体の件数と失敗の件数（分母）を書く
    - 失敗したテストごとに、テスト名と、最初のエラーの行、関係しそうなファイルの場所を書く
    - 成功したテストの出力と、ログ全文は戻さない
    - 失敗の原因の推測は、根拠の行とともに 1 行だけ書く。直さない
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet writing-subagents/test-runner -->

!!! example "判断例：担当にだけ git commit を禁じる"
    - **状況**：テスト担当に、git commit をさせたくない。本体の会話では commit できるままにしたい。
    - **迷う候補**：担当の定義の `disallowedTools` に `Bash(git commit *)` と書く。権限ルールの deny に書く。フックで、入力の `agent_id` を見て止める。
    - **選んだもの**：フックで `agent_id` を見る。
    - **理由**：`disallowedTools` に指定子を付けても、Bash の道具全体が外れてしまう。deny は特定のコマンドを止められるが、メインの会話も止める。呼び出しが担当の中かどうかを見分けられるのは、フックの入力の `agent_id` だけである。

フックの組み方は <!-- link:begin hook-recipes#subagent-only -->[代表的なフックのレシピ › 担当にだけ禁じる（agent\_id）](../enforce/hook-recipes.md#subagent-only)<!-- link:end -->、権限ルールの書き方は <!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end --> にある。設定に書いたフックは担当の中でも走るので、1 つのフックでメインと担当の両方を見られる。

## 効かない場面・落とし穴 {#pitfalls}

- **指定子を付けても Bash 全体が外れる**：`disallowedTools` はツールの単位で効く。特定のコマンドを止めるなら、権限ルールか、入力の `agent_id` を見るフックを使う。権限ルールの deny はメインの会話も止めるので、担当にだけ禁じるならフックになる。
- **Bash を許した担当は、読み取り専用ではない**：編集の道具を外しても、Bash を足せば、シェルから書き込める。読むだけの役は、`Read`・`Grep`・`Glob` に絞る。
- **description が曖昧だと呼ばれない**：Claude は description を見て呼ぶかを決める。いつ使うかを先頭に具体的に書き、ほかの担当と重ならないようにする。
- **要点だけが戻る**：本筋に戻るのは要約である。結論だけでなく、根拠の場所も戻させ、重要な点は本筋で確かめる（<!-- link:begin research-in-subagents#cost -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 費用と使いすぎ](../context/research-in-subagents.md#cost)<!-- link:end --> を見る）。
- **レビュアーの一致は証拠ではない**：担当を増やして賛成が揃っても、正しさの証拠にはならない（<!-- link:begin agreement-is-not-evidence#reviewer-agreement -->[同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](../judgment/agreement-is-not-evidence.md#reviewer-agreement)<!-- link:end --> を見る）。レビュアーに見せるのは成果物と基準で、書いた側の見立ては添えない。
- **費用の見積もりを忘れる**：担当の使用量は、本体と同じ上限に数えられる。担当の種類ごとの使用量は `/usage` で見られるので、使っていない定義や、元が取れていない担当は減らす。
- **担当の記録は圧縮の影響を受けない**：本筋の会話が圧縮されても、担当の記録は影響を受けない。ただし本筋に戻るのは要約だけなので、担当の記録を本筋の文脈の代わりにはできない。

## 比べる相手 {#compare}

- **スキル**：手順を今の会話で読ませるのがスキル、別の文脈の担当に任せるのがサブエージェントである（<!-- link:begin skill-vs-subagent -->[スキルとサブエージェントの違い](skill-vs-subagent.md)<!-- link:end --> を見る）。
- **エージェントチーム**：担当どうしが連絡し合うなら、リードとチームメイトの形を使う。方式の選び方は <!-- link:begin choosing-parallel-modes#compare -->[並列の方式の選び方 › 方式の比較](../delegate/choosing-parallel-modes.md#compare)<!-- link:end --> にある。
- **フック**：例外を許さない規則は、定義に書かず、フックで縛る。フックの考え方は <!-- link:begin hooks-basics -->[フックの考え方とイベント](../enforce/hooks-basics.md)<!-- link:end --> にある。

## 古くなった助言 {#outdated}

- `/agents` の画面で作る：今は Claude に作らせるか、ファイルを直接書く（<!-- link:begin outdated-advice-ledger#agents-command -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#agents-command)<!-- link:end -->）。
- 工程ごとに担当を大量に作る：文脈の独立で分ける（<!-- link:begin outdated-advice-ledger#subagent-per-step -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#subagent-per-step)<!-- link:end -->）。
- 「subagent を使え」と書き足す：書き足さず、大きく独立した作業だけを任せる（<!-- link:begin outdated-advice-ledger#tell-it-to-use-subagents -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#tell-it-to-use-subagents)<!-- link:end -->）。
- コンテキストを守るために調べさせる：守るためだけには使わない（<!-- link:begin outdated-advice-ledger#subagents-to-save-context -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#subagents-to-save-context)<!-- link:end -->）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [サブエージェントは別室の部下](../basics/subagent-isolation.md)

**次に読む**

- サブエージェントに引き継がれないもの（準備中）

**関連**

- [スキルとサブエージェントの違い](skill-vs-subagent.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- レビュアーへの指示の書き方（準備中）
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [代表的なフックのレシピ › 担当にだけ禁じる（agent\_id）](../enforce/hook-recipes.md#subagent-only)
- [フックの考え方とイベント](../enforce/hooks-basics.md)
- [並列の方式の選び方](../delegate/choosing-parallel-modes.md)
- エージェントチーム（複数の Claude に分担させる）（準備中）
- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [並列・ループ・workflows のコスト](../cost/parallel-and-loop-costs.md)
- 計画・実装・サブエージェントでモデルを分ける（準備中）
- [effort の段階と使い分け › サブエージェントと組織の上限](../models/effort-levels.md#subagents-and-org-limits)
- [スキルの description の書き方](skill-descriptions.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む） › AI レビュアーの一致](../judgment/agreement-is-not-evidence.md#reviewer-agreement)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
