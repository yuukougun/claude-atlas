# 工程2 R7：制作の道具とサイトの技術の確認

- 担当：R7（工程2「調査の補完」。共通の指示は [../batches/step2/brief.md](../batches/step2/brief.md)）
- 確認日：2026-11-03（この報告のすべての事実。版に依存するものは行ごとに版を書く）
- 手元の Claude Code：2.1.317（`claude --version`）。npm の `latest` も 2.1.317（2026-11-02 公開）、`stable` は 2.1.311
- 方法：公式文書を Markdown（`<ページの URL>.md`）で取得して読み、版と日付を CHANGELOG・npm・PyPI・GitHub の Releases で確かめた。Claude Code は `--version` と `--help` のほかは動かしていない（brief §4）。Web 検索は使っていない

---

## 1. 調べた範囲と方法

### 1.1 範囲

割り当ての1〜6（hooks と permissions、作者の設定を混ぜない起動、sandbox、設定の仕様と schema、Zensical と Material、主な出典のドメインの AI の利用の指定）。関わる案は format-and-operations の F7・F9・F11・F12・F15・F19、調査資料は 01 の B・C・E・F・J の節、05 §4-5、requirements §10.1・§10.3、decisions の「危ない雛形を試す場所」「API キー」「サイトを作る道具」である。

### 1.2 使った一次資料

表の「出典」の欄の S 番号は、この一覧を指す。確認日はすべて 2026-11-03。

| S | 資料 | URL |
| --- | --- | --- |
| S1 | Hooks reference | https://code.claude.com/docs/en/hooks |
| S2 | Configure permissions | https://code.claude.com/docs/en/permissions |
| S3 | Create custom subagents | https://code.claude.com/docs/en/sub-agents |
| S4 | Dynamic workflows | https://code.claude.com/docs/en/workflows |
| S5 | Run Claude Code programmatically（headless） | https://code.claude.com/docs/en/headless |
| S6 | CLI reference | https://code.claude.com/docs/en/cli-reference |
| S7 | Settings | https://code.claude.com/docs/en/settings |
| S8 | Settings reference | https://code.claude.com/docs/en/settings-reference |
| S9 | Configure the sandboxed Bash tool | https://code.claude.com/docs/en/sandboxing |
| S10 | Extend Claude with skills | https://code.claude.com/docs/en/skills |
| S11 | Environment variables | https://code.claude.com/docs/en/env-vars |
| S12 | How Claude remembers your project（memory） | https://code.claude.com/docs/en/memory |
| S13 | Explore the .claude directory | https://code.claude.com/docs/en/claude-directory |
| S14 | Debug your configuration | https://code.claude.com/docs/en/debug-your-config |
| S15 | Authentication | https://code.claude.com/docs/en/authentication |
| S16 | Tools reference | https://code.claude.com/docs/en/tools-reference |
| S17 | Permission modes | https://code.claude.com/docs/en/permission-modes |
| S18 | Agent SDK：Claude Code features（settingSources） | https://code.claude.com/docs/en/agent-sdk/claude-code-features |
| S19 | Plugin commands reference（plugin validate） | https://code.claude.com/docs/en/plugins/cli-reference |
| S20 | Claude Code の CHANGELOG（raw.githubusercontent.com で取得） | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md |
| S21 | npm の公開記録（版の日付） | https://registry.npmjs.org/@anthropic-ai/claude-code |
| S22 | `claude --help`（手元の 2.1.317） | — |
| S23 | SchemaStore の Claude Code の設定のスキーマ（301 で www.schemastore.org へ） | https://json.schemastore.org/claude-code-settings.json |
| S24 | 同スキーマのコミットの履歴（api.github.com で取得） | https://github.com/SchemaStore/schemastore （`src/schemas/json/claude-code-settings.json`） |
| S25 | Agent Skills の仕様 | https://agentskills.io/specification |
| S26 | Zensical「What changes on November 5, 2026」 | https://zensical.org/upcoming-changes/ |
| S27 | Zensical：MkDocs の互換・移行 | https://zensical.org/docs/compatibility/mkdocs/ 、 https://zensical.org/docs/compatibility/mkdocs/migration/ |
| S28 | Zensical：MkDocs plugins | https://zensical.org/docs/compatibility/mkdocs/plugins/ |
| S29 | Zensical：Python Markdown Extensions | https://zensical.org/docs/compatibility/markdown/python-markdown-extensions/ |
| S30 | Zensical：Customization | https://zensical.org/docs/customization/ |
| S31 | Zensical：Search | https://zensical.org/docs/setup/search/ |
| S32 | Zensical：Validation | https://zensical.org/docs/setup/validation/ |
| S33 | Zensical：Roadmap | https://zensical.org/roadmap/ |
| S34 | Zensical の Releases（v0.0.72〜0.0.74） | https://github.com/zensical/zensical/releases |
| S35 | Material for MkDocs の Releases（9.7.2〜9.8.0） | https://github.com/squidfunk/mkdocs-material/releases |
| S36 | Material の blog「What MkDocs 2.0 means for your documentation projects」（2026-02-18、最終更新 2026-10-02。Material のチームの記事） | https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/ |
| S37 | PyPI の JSON（zensical・mkdocs-material・mkdocs） | https://pypi.org/pypi/zensical/json ほか |
| S38 | 手元の環境の確認（`/etc/os-release`・`command -v`・`sysctl`。読むだけ） | — |

### 1.3 AI の利用を断る指定（`python3 -I tools/check_noai.py --robots`）

リポジトリの根で実行した。各ドメインの代表のページは、調査資料で最も多く引かれた出典か、この報告で読んだ公式のページである。

| ドメイン | 確かめたページ | 取得 | X-Robots-Tag | meta robots | robots.txt の AI 向けの指定 | 判定 |
| --- | --- | --- | --- | --- | --- | --- |
| code.claude.com | /docs/en/hooks | 200 | なし | なし | なし（`*` に /cdn-cgi/・/_next/ の Disallow） | 指定なし |
| docs.claude.com | /en/docs/build-with-claude/prompt-engineering/prompt-improver | 302 で platform.claude.com の同名へ、さらに 308 で claude-prompting-best-practices へ | なし | なし | なし（`*` に /api/） | 指定なし |
| platform.claude.com | /docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | 200 | なし | なし | なし（`*` に /api/） | 指定なし |
| support.claude.com | /en/articles/12138966-release-notes | 200 | なし | `all` | なし | 指定なし |
| claude.com | /blog/steering-claude-code-skills-hooks-rules-subagents-and-more → 308 → /resources/articles/（同名） | 200（転送先） | なし | `max-image-preview:large` | なし（`*` は Allow: /） | 指定なし |
| www.anthropic.com | /engineering/effective-context-engineering-for-ai-agents → 308 → /research/（同名） | 200（転送先） | なし | なし | なし（`*` は Allow: /） | 指定なし |
| github.com | /anthropics/claude-code | 200 | なし | なし | GPTBot・OAI-SearchBot・ClaudeBot・anthropic-ai・PerplexityBot を一つの群にし、Crawl-delay 1 と、`*` とほぼ同じ Disallow（`/*/raw/`・`/*/tree/`・`/*/blame/`・`/*/*/commits/` など）。Bytespider は全面 Disallow | 指定なし |
| raw.githubusercontent.com | /anthropics/claude-code/main/CHANGELOG.md | 200 | なし | なし（Markdown） | robots.txt がない（404） | 指定なし |
| zenn.dev | /ml_bear/articles/84e92429698177 | 200 | なし | なし | Bytespider だけ全面 Disallow | 指定なし |
| qiita.com | /minorun365/items/114f53def8cb0db60f47 | 200 | なし | `max-image-preview:large` | なし（`*` に `/policies/td-optout$` の Disallow があるが、そのページは 404） | 指定なし |
| note.com | /notty0123/n/n89846a4c1b5f | 200 | なし | `max-image-preview:large` | なし | 指定なし |
| speakerdeck.com | /minorun365/claude-codebesutopurakuteisumatome | 200 | なし | `max-image-preview:large` | なし | 指定なし |
| dev.classmethod.jp | /articles/claude-code-hooks-prevent-english-reply/ | 200 | なし | `index, follow, max-image-preview:large` | なし | 指定なし |
| gihyo.jp | /article/2026/02/get-started-claude-code-07 | 200 | なし | なし | なし | 指定なし |
| arxiv.org | /abs/2307.03172v3 | 200 | なし | なし | なし（`*` に /abs・/pdf・/html などの Allow） | 指定なし |
| zensical.org | / | 200 | なし | なし | robots.txt がない（404） | 指定なし |
| squidfunk.github.io | /mkdocs-material/ | 200 | なし | なし | robots.txt がない（404） | 指定なし |

- この報告で読んだ追加のドメイン（json.schemastore.org・www.schemastore.org・api.github.com・agentskills.io・registry.npmjs.org・pypi.org）も、同じ道具で noai・noimageai の指定がないことを確かめた
- 参考：どのドメインにも TDM の拒否（`tdm-reservation` のヘッダーと meta）はなく、`/.well-known/tdmrep.json` もない（404。gihyo.jp は 403、zensical.org は 302 の転送）
- **道具の不具合**：この環境の `python3` は 3.10.12 で、urllib が 308 の転送をたどるのは 3.11 からである。そのため claude.com と www.anthropic.com では、最初の実行で転送前の 308 の応答を見て「指定はない」と出た。転送先の URL を直接渡して確かめ直した（§4 の提案 12）

---

## 2. 結果の一覧

結果の数：**正しい 58**（既存の主張を確かめたもの 30、新しく確かめた事実 28）・**誤り 1**・**一部誤り 3**・**確かめられない 1**（計63件）。「正しい（補足）」は主張は正しいが、教材や設計に要る条件が欠けていたもの、「正しい（新規）」は割り当ての問いに一次資料で答えたものである。

### 2.1 hooks と permissions

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 1 | F19 の前提：hooks の入力で、呼び出しがサブエージェントの中かを見分けられる | 正しい | 共通の入力に `agent_id` と `agent_type` がある。`agent_id` はサブエージェントか in-process の teammate の中で発火したときだけ付く。`agent_type` はサブエージェントの中か、`--agent` で起動したセッションで付く（サブエージェントの型が優先）。`--agent` なしのメインの会話にはどちらもない。v2.1.69（2026-03-04）で追加 | S1 #common-input-fields、S20（2.1.69）、S21 | 「メイン以外に生成と commit をさせない」は `agent_id` の有無で判定する。`agent_type` は `--agent` でメインにも付くので使わない |
| 2 | F19・F15：設定の hooks はサブエージェントにも効く | 正しい | settings・管理の設定・plugin の hooks はサブエージェントの中でも走り、PreToolUse・PostToolUse がメインと同じに発火する。サブエージェントの front matter の hooks は、その担当が動く間だけ走る（Stop は SubagentStop に変わる） | S1 #hook-locations・#hooks-in-skills-and-agents、S3 #define-hooks-for-subagents | `.claude/settings.json` の一つの hook で、メインと担当の両方を見られる |
| 3 | F15：ワークフローの担当にも permissions と sandbox が効く | 正しい | 担当のツールの呼び出しは、セッションのほかの呼び出しと同じ権限の確認と sandbox を受ける。担当は利用者の permission rules を使い、モードはサブエージェントの規則で決まる。`-p` では Workflow の起動も権限の評価を通り、`Workflow` か `Workflow(<名前>)` の allow などが要る | S4 #ask-for-a-workflow-in-your-prompt・#approve-the-plan-before-it-runs | ワークフローでも deny の規則はそのまま効く |
| 4 | F15・F19：ワークフローの担当にも設定の hooks が走り、`agent_id` が付く | 確かめられない | 文書は `agent()` がサブエージェントを1つ生むと書き、hooks はサブエージェントの中で走ると書くので、走ると読める。しかし、ワークフローの担当で hooks が走ることと、そのときの `agent_type` の値は、hooks・workflows・sub-agents・tools-reference のどれにも明記がない。CHANGELOG には mod の `agent.spawn` がワークフローの担当を扱う（2.1.292）とあるだけ | S1、S3、S4、S20 | 頼る前に、制作の環境で無害な操作（`git commit --dry-run` を止める hook など）で確かめる（F12） |
| 5 | 01 F-1：matcher は完全一致・`\|` 区切り・ほかは JS 正規表現 | 正しい（補足） | 文字・数字・`_`・`-`・空白・`,`・`\|` だけなら完全一致（`\|` か `,` で並べる。`,` は v2.1.191＝2026-06-24 から）。ほかの文字を含むと前後を固定しない正規表現になり、`Edit.*` は NotebookEdit にも当たる（`^Edit$` で固定する）。大文字小文字を区別する。matcher を配列で書くと無効で、PreToolUse・PermissionRequest の下なら同じファイルのほかの hooks も読まれない | S1 #matcher-patterns、S14 #check-common-causes | 部分一致で止めすぎない（F19 の決まり3）。matcher は完全一致か `^…$` で書く |
| 6 | 01 F-1：`if` に permission rule の構文を書ける | 正しい（補足） | ツールのイベントだけで評価し、規則は一つしか書けない（`&&`・`\|\|` はない）。Bash の判定は best-effort で、コマンドを読み切れないときは規則にかかわらず hook を走らせる。文書は、確実な許可・拒否には hook ではなく permissions を使うよう勧める | S1 #common-fields・#how-if-patterns-match-bash-commands | `if` は hook を呼ぶ回数を減らすために使い、判定はスクリプトの中でも行う |
| 7 | 01 C-3・F19：WebFetch をドメインで拒む | 正しい（補足） | `WebFetch(domain:atcoder.jp)` は atcoder.jp だけに当たる。サブドメインには `WebFetch(domain:*.atcoder.jp)` を別に足す（任意の深さに当たり、親は含まない）。ワイルドカードは v2.1.172（2026-06-10）から。大文字小文字を区別せず、末尾の `.` を除いて比べる。素の `WebFetch` の deny はツールごと消し、`WebFetch(domain:*)` の deny はツールを残して各取得を拒む | S2 #webfetch・#allow-or-deny-every-fetch | noai のサイトは4行（各ドメインとその `*.`）で拒める。強制に hook は要らない |
| 8 | F19：転送（リダイレクト）で拒むドメインに抜けないか | 正しい（新規） | WebFetch は別のホストへの転送をたどらず、元の URL と転送先を結果として返す。Claude は転送先を2回目の WebFetch で取りに行くので、その呼び出しに deny と hook が効く | S16 #webfetch-tool-behavior | 短縮 URL などからの転送でも、ドメインの deny で足りる |
| 9 | F19：WebFetch の規則で、AI で開かないサイトへの取得を全部止められる | 一部誤り | 規則は WebFetch のツールだけに効く。Bash の `curl` などは対象外で、Bash の deny も `/usr/bin/curl` や `sh -c '…'` を止めない（文書の表）。sandbox を有効にすると `WebFetch(domain:…)` の規則が sandbox のネットワークの一覧に入り、Bash にも効く（sandbox が従うのは先頭の `*.` と `*` だけ）。WebSearch と MCP のツールは別の名前で、この規則の外 | S2 #what-a-bash-rule-doesnt-match・#webfetch、S9 #permission-rules・#network-isolation | 規則の説明（README・CLAUDE.md）に「止めるのは WebFetch。curl などは sandbox を入れたときに止まる」と書く |
| 10 | requirements §10.1・01 C-3：Read と Edit はパスで拒む | 正しい（補足） | gitignore の形式。`//path` は絶対、`~/path` はホーム、`/path` は設定の置き場所が基点（`.claude/settings.json` なら主な作業ディレクトリ、`~/.claude/settings.json` なら `~/.claude`、`--settings` のファイルならそのフォルダ）、`path`・`./path` は現在のディレクトリ。`/Users/x` は絶対パスにならない。deny と ask の `secrets/**` は任意の深さに当たり、allow では現在のディレクトリの直下だけに当たる | S2 #how-path-patterns-match | 生成物の手書きを止めるなら `Edit(/生成先/**)`。ユーザーの設定に書く規則は `//` か `~/` で書く |
| 11 | requirements §10.1：`Write(path)`・`NotebookEdit(path)`・`Glob(path)` は何にも当たらない | 正しい（補足） | 受け付けるが何にも当たらない（古い `MultiEdit(path)` も同じ）。Read の deny は同じパスの Edit と Write（新しく作ることも）も止める（Write は v2.1.228＝2026-08-11 から）。NotebookEdit は対象外なので、変えさせないパスには Edit の deny を足す | S2 #what-read-and-edit-rules-cover・#writepath-notebookeditpath-and-globpath-rules-never-match | 雛形は Edit と Read だけで書く |
| 12 | requirements §10.1：Read・Edit の deny は任意の子プロセスに効かない | 正しい | 組み込みのファイルのツールと、Claude Code が認識するシェルのコマンド（`cat`・`head`・`tail`・`sed`・`tee`）とリダイレクトの先には効く。`grep -r` のように名前を出さずに読むものや、Python・Node のスクリプトが自分で開くファイルには効かない | S2（Read and Edit の警告の枠） | 生成スクリプトは子プロセスなので、Edit の deny を置いても生成は止まらない（意図どおり） |
| 13 | 01 C-3：評価は deny → ask → allow で、最初の一致が勝つ | 正しい | 具体性で順は変わらない。どのスコープの deny もほかのスコープの allow に勝つ。PreToolUse の hook が `allow` を返しても deny と ask の規則は評価される。exit 2 で止める hook は allow の規則より先に効く | S2 #manage-permissions・#precedence-among-rules-hooks-and-mods・#settings-precedence | hook の allow で deny を外すことはできない（安全側に倒れる） |
| 14 | F19（問いの前提）：サブエージェントの定義の `disallowedTools: Bash(git commit *)` で、担当にだけ commit を禁じられる | 誤り | `disallowedTools` の項目に `Bash(git push *)` のような指定子を付けても、Bash のツール全体が外れる。特定のコマンドだけを止めるには `permissions.deny` の Bash の規則を使うよう文書は勧め、その規則はメインとサブエージェントの両方に効く。`tools`・`disallowedTools` が扱うのはツールの単位（MCP はサーバーの単位も可） | S3 #restrict-which-tools-a-subagent-can-use | 「担当にだけ」禁じるには hook（`agent_id`）しかない。deny はメインの commit も止める |
| 15 | F19：止めた理由と代わりの手段を Claude に返す方法 | 正しい（補足） | (a) exit 2：stderr が理由になり、Claude には「PreToolUse:Bash hook error: [コマンド]: …」の形で届く。(b) exit 0 で JSON：`hookSpecificOutput` に `permissionDecision: "deny"` と `permissionDecisionReason` を入れる（deny の理由は Claude に見える）。`additionalContext` で状況を足せる（一つの値は1万字まで）。PreToolUse の最上位の `decision`・`reason` は非推奨。複数の hook の判定が違うと deny > defer > ask > allow。exit 2 と JSON を混ぜると exit 2 の止めが勝つ。`systemMessage` は利用者向けで Claude 向けではない | S1 #exit-code-2・#json-output・#pretooluse-decision-control | F19 の決まり2は (b) で書き、理由と代わり（「報告に提案として書く」など）を `permissionDecisionReason` に入れる |
| 16 | F19 の決まり2：理由の文の書き方 | 正しい（新規） | 文書は `additionalContext` について、命令ではなく事実の形で書くよう勧め、システムの命令のような書き方は prompt injection の防御を働かせ、文脈として扱われずに利用者へ示されることがあると注意している | S1 #add-context-for-claude | 止めたときの文は「このリポジトリでは commit はメインが行う。変更は報告のファイルに書く」のような事実の形にする（`permissionDecisionReason` に同じ注意を当てるのは推論） |
| 17 | 01 F-1・requirements §10.3（A-4）：既定は fail-open | 正しい（補足） | 起動できない、0 と 2 以外で終わる（exit 1 も含む）、タイムアウト、JSON が壊れている、のどれも「止めない誤り」で、操作は進む。`"onFailure": "block"`（command と http の hook。v2.1.295＝2026-10-08 から）を付けると、失敗を exit 2 と同じに扱う。Stop・SubagentStop・TaskCompleted・TeammateIdle と非同期の hook には効かない。command の hook の既定のタイムアウトは 600 秒。スクリプトが中で失敗しても 0 で終われば、`onFailure` があっても通る | S1 #block-the-action-when-a-hook-fails・#timeouts・#common-fields、S20（2.1.295） | 縛る hook の `onFailure` は規則ごとに決めて書く（F19 の決まり5）。jq などの有無はスクリプトが確かめ、欠けたら 2 で終わる（A-4 の直し） |
| 18 | F19 の決まり4：止めた記録をどのイベントで取るか | 正しい（新規） | `PermissionDenied` は auto mode の判定で拒んだときだけ発火し、deny の規則・hook・手動の拒否では発火しない。`PostToolUseFailure` も権限で拒んだ呼び出しでは発火しない。PreToolUse は権限の判定の前に走るので、deny の規則で止まる呼び出しも見える。`-p` の `stream-json` では拒否が `permission_denied` の行と、結果の `permission_denials` に出る | S1 #permissiondenied・#posttoolusefailure、S2 #extend-permissions-with-hooks、S5 #turn-off-permission-prompts-in-unattended-runs | 記録は PreToolUse の hook で取り、追跡外のファイル（`state/`）に書く |
| 19 | F19 の決まり5・F18：読者がリポジトリを開いたときに縛りが効く条件 | 正しい（新規） | 対話のセッションでは、フォルダの信頼のダイアログを受け入れるまで、どの設定ファイルの hooks も走らない（自分の `~/.claude/settings.json` も含む）。`-p` と SDK はダイアログを出さず、信頼したものとして `.claude/settings.json` の hooks を走らせる。`.claude/settings.json` の `permissions.allow` と `additionalDirectories` は信頼の後でだけ使われ、deny と ask は信頼と関係なく効く | S1 #workspace-trust、S2 #project-allow-rules-and-workspace-trust・#what-runs-before-you-trust-a-folder | README に「信頼すると次の hooks が走る」「deny は信頼の前から効く」と書く |
| 20 | F19：担当が縛りの設定を書き換えて外せるか | 正しい（新規） | `.claude/` は保護されたパスで、書き込みは Manual と acceptEdits では確認が出る、auto mode では分類器が判断する、dontAsk では拒否、bypassPermissions では許可。allow の規則（`Edit(.claude/**)` など）では事前に許せない | S17 #protected-paths | hook のスクリプトも `.claude/hooks/` に置けば同じ保護がかかる。F15 の `.claude/workflows/` への保存もこの保護を受ける |
| 21 | F15・L11：担当が報告を渡す前の確認を hook でできるか | 正しい（新規・参考） | auto mode のサブエージェントは `SubagentHandback` のツールで報告を渡し、PreToolUse でこれを deny すると、担当に最大3回やり直しを求める（その後は報告なしで終わる）。報告の本文は `tool_input.message` で読める。このツールは auto mode のときに用意される（v2.1.271＝2026-09-14 から） | S1 #pretooluse-ask-decisions-in-auto-mode・#subagentstop、S16、S21 | 「報告をファイルに書いてから終える」を機械で確かめる余地がある。モードに依存し、試していない |
| 22 | 01 F-1：イベントは33種、ハンドラは5種 | 正しい | 33のイベント（PreModelSwitch・PostModelSwitch を含む）と、command・http・mcp_tool・prompt・agent（実験的）の5種。一つのイベントで当たった hooks は並列に走る | S1 #hook-events・#hook-handler-fields | なし |
| 23 | 01 F-1：exec 形式（`args`）を勧める | 正しい（補足） | `args` があると `command` を実行ファイルとしてシェルなしで起動し、各要素をそのまま一つの引数にする。`${CLAUDE_PROJECT_DIR}` などの置き換えを使う hook では `args` を付けるよう文書は勧め、シェルの形では二重引用符で囲む | S1 #exec-form-and-shell-form・#reference-scripts-by-path | 雛形の hook は exec 形式で書く |

### 2.2 雛形の確認で作者の設定を混ぜない方法（F12）

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 24 | 01 J（`--bare`）・21 §1 #7・decisions「API キー」 | 正しい（補足） | `--bare` は hooks・skills・commands・サブエージェント・plugins・MCP・auto memory・CLAUDE.md の自動の読み込みを省く。Anthropic の認証は `ANTHROPIC_API_KEY` か `--settings` の `apiKeyHelper` だけで、OAuth（サブスクリプションのログイン）と keychain を読まない。v2.1.81（2026-03-20）で追加、将来 `-p` の既定にする予定。v2.1.286 から system reminder を送らず、背景のタスクも止めるので、ふつうの `-p` と挙動が違う。プロジェクトの settings の `env` と一部の helper はなお効く | S5 #start-faster-with-bare-mode、S6、S22、S2 #what-runs-before-you-trust-a-folder | API キーを使わない決定のもとでは `--bare` は使えない。`-p` の既定が変わると雛形の確認の前提が変わる（鮮度の点検の対象） |
| 25 | F12：`--setting-sources` で読む設定の源を絞れる | 正しい（新規） | `user`・`project`・`local` から選ぶ。user は `~/.claude/` の settings.json・CLAUDE.md・rules・skills・commands・agents。project は `.claude/settings.json` と hooks、作業ディレクトリとその上の CLAUDE.md と rules、プロジェクトの skills・commands・agents。local は `settings.local.json` と CLAUDE.local.md。認証の制約はない。user を外すと claude.ai の skill の同期もしない。v2.1.314（2026-10-30）で、外した源から一部（auto mode の規則・保存した同意）が漏れる不具合が直った | S18 #control-filesystem-settings-with-settingsources、S6、S10、S20（2.1.314） | 2.1.314 より前の版の結果は、漏れの影響を受けうる |
| 26 | F12：`--setting-sources` で絞れないもの | 正しい（新規） | 管理の設定、`~/.claude.json`（`CLAUDE_CONFIG_DIR` で移す）、auto memory（`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` か `autoMemoryEnabled: false`）、claude.ai の MCP コネクタ（`--strict-mcp-config`・`disableClaudeAiConnectors`・`ENABLE_CLAUDEAI_MCP_SERVERS=false`。`claude setup-token` のトークンでは読まれない）、ユーザーの settings の `sandbox.credentials` の deny と mask | S18 #what-settingsources-does-not-control | §3.4 の手順でこれらを一つずつ塞ぐ |
| 27 | F12：`CLAUDE_CONFIG_DIR` で設定の置き場所を変えられる | 正しい（新規） | `~/.claude` の代わりのフォルダにできる。設定・履歴・plugins に加え、`.claude.json` と認証情報の `.credentials.json` もその下になる。新しいフォルダでは初回の設定とログインをやり直す（サブスクリプションの /login で足りる）。公式の「Debug your configuration」は、新しいフォルダと `--setting-sources user` で起動して原因を切り分ける手順を示す。プロジェクトと local の settings の `env` に書いても無視される | S11、S13、S15 #credential-management、S14 | 雛形の確認の専用の置き場所にできる（API キーは要らない） |
| 28 | F12：`--safe-mode` | 正しい（新規） | CLAUDE.md・skills・plugins・hooks・MCP・自作の commands と agents・output styles・workflows・auto memory などを読まずに起動する。認証・モデル・組み込みのツール・permissions は通常どおり（OAuth も使える）。管理の設定は効く。v2.1.169（2026-06-08） | S6、S11、S20（2.1.169） | プロジェクトの hooks も止まるので、雛形そのものの確認には使えない。「雛形がないとき」の対照の実行に使える |
| 29 | F12：`--restricted` | 正しい（新規） | コマンドを実行するツールと WebFetch を外し（`--tools` で名指しすれば使える）、管理の設定と `--settings` だけを読み、ファイルのツールを作業ディレクトリに閉じ、bypassPermissions を拒む。評価の道具が共有のマシンで動かす用途。v2.1.248（2026-08-27） | S6、S22、S20（2.1.248） | 挙動が変わりすぎるので、雛形の確認には向かない |
| 30 | 05 §4-5・01 J：`-p` は信頼のダイアログを出さない | 正しい（補足） | `-p`（と stdout が端末でないとき）はダイアログを飛ばす。設定ファイルの hooks・`env`・helper と、プロジェクトの skill の hooks と `allowed-tools` は使われ、`.mcp.json` のサーバーは承認なしにつなぐ。一方、`.claude/settings.json` の `permissions.allow` と `additionalDirectories` は使われず（stderr に警告）、プロジェクトのサブエージェントの front matter の hooks も走らない。手で信頼するには `.claude.json` の `projects["<パス>"].hasTrustDialogAccepted` を true にする | S22、S2 #what-runs-before-you-trust-a-folder、S1 #hooks-in-skills-and-agents | 雛形の allow の規則とサブエージェントの hooks は、そのままの `-p` では確かめられない。専用の置き場所の `.claude.json` で使い捨てのフォルダを信頼させる |
| 31 | F12：`-p` で設定ファイルが壊れていたとき | 正しい（新規） | 対話ではエラーのダイアログが出るが、`-p` は壊れたファイルや値を黙って飛ばして続ける。何を落としたかは `claude doctor` で見る | S7 #fix-a-broken-settings-file、S22 | 雛形の確認では「期待の設定が読まれたか」を別に確かめる（静的な検査と `claude doctor`） |
| 32 | F12：`-p` の既定の権限 | 正しい（新規） | v2.1.302（2026-10-16）以降、モードを決めない `-p` は Manual で始まり、承認の要る呼び出しは、allow の規則・PermissionRequest の hook・`--permission-prompt-tool` がない限り拒否される | S5 #auto-approve-tools、S21 | 「この操作が止められる」の期待は、雛形がなくても満たされうる。対照の実行と比べる |
| 33 | decisions「API キー」・F12：環境の API キー | 正しい（新規。R5 と重なる） | `-p` では `ANTHROPIC_API_KEY` があれば必ず使う（対話では一度確かめる）。認証の優先は、クラウドの事業者 > `ANTHROPIC_AUTH_TOKEN` > `ANTHROPIC_API_KEY` > `apiKeyHelper` > `CLAUDE_CODE_OAUTH_TOKEN` > … > `/login` | S15 #authentication-precedence | 雛形の確認の前に `ANTHROPIC_API_KEY` などを外す（意図しない API の課金を防ぐ） |
| 34 | F12：使い捨てのフォルダの置き場所 | 正しい（新規） | CLAUDE.md と CLAUDE.local.md は、作業ディレクトリとその上のすべてのフォルダから読む（project の源） | S12 #how-claudemd-files-load、S18 | 使い捨てのフォルダをリポジトリの中に作ると claude-atlas の CLAUDE.md が混ざる。CLAUDE.md を持たないフォルダの下に作る |
| 35 | F12：ログインの代わりの長期のトークン | 正しい（新規） | `claude setup-token` はサブスクリプションで1年の OAuth トークンを出し、どこにも保存しない。`CLAUDE_CODE_OAUTH_TOKEN` に置くと、そのトークンはモデルの要求だけができ、claude.ai のコネクタは読まれない | S15 #generate-a-long-lived-token、S18 | 専用の置き場所で /login する代わりに使える（どちらも API キーは要らない） |

### 2.3 sandbox

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 36 | 05 §4-5・01 C-4・decisions「危ない雛形を試す場所」：Linux と WSL2 は bubblewrap と socat を使う | 正しい | bubblewrap がファイルの隔離、socat がプロキシへの中継を担う。Ubuntu・Debian は `sudo apt-get install bubblewrap socat`。ripgrep は Claude Code に同梱。seccomp のフィルタは任意で、Unix ソケットを塞ぐ（`npm install -g @anthropic-ai/sandbox-runtime`）。依存は起動時に確かめるので、入れた後は再起動して `/sandbox` の Dependencies のタブで欠けを見る | S9 #set-up-linux-and-wsl2 | decisions の前提は一次資料で確かめられた |
| 37 | 05・01：ネイティブの Windows では使えず WSL2 が要る | 正しい（補足） | sandbox は macOS・Linux・WSL2 で動く。WSL1 は使えない（「Sandboxing requires WSL2」と出る）。ネイティブの Windows ではコマンドを sandbox なしで動かす。WSL2 では Windows の実行ファイル（`cmd.exe` や `/mnt/c/` の下）の起動が Unix ソケットを通り、止めるには seccomp のフィルタが要る | S9 冒頭・#set-up-linux-and-wsl2 | 「WSL・Linux を基準にする」決定と合う。WSL2 から Windows 側のプログラムが動く点は注記に値する |
| 38 | decisions「危ない雛形を試す場所」：作者が bubblewrap と socat を入れれば足りるか | 正しい（新規） | Ubuntu 24.04 以降は既定の AppArmor が bubblewrap の user namespace を止めることがあり、`sysctl kernel.apparmor_restrict_unprivileged_userns` が 1 なら bwrap 用のプロファイルを足す（0 かキーがなければ不要）。この環境は Ubuntu 22.04.5 LTS（WSL2、カーネル 6.18.54.1）で、そのキーがない。bwrap と socat は入っていない。管理の設定（`/etc/claude-code`）もない | S9（Ubuntu 24.04 の項）、S38 | `sudo apt install bubblewrap socat` だけで足りる見込み（入れた後の確認はしていない） |
| 39 | 05 §4-5：sandbox は既定でオフ | 正しい | `/sandbox` か `sandbox.enabled: true` で有効にする。`/sandbox` で選んだモードは `.claude/settings.local.json` に保存される | S9 #what-the-sandbox-restricts・#get-started、S8 #sandbox-enabled | なし |
| 40 | 05 §4-5：sandbox が起動できないとき | 正しい（補足） | 依存が欠けているか対応しない環境では、既定で sandbox なしでコマンドを動かす（fail-open）。`sandbox.failIfUnavailable: true` で起動時に終了する。起動後に初期化に失敗したら、各コマンドを「Sandbox is required」で拒む | S9（Get started の警告の枠）、S8 #sandbox-failifunavailable | sandbox に頼る雛形と制作の設定には `failIfUnavailable` を付ける |
| 41 | 05 §4-5・01 C-4：主な設定のキー | 正しい（補足） | `enabled`・`failIfUnavailable`・`autoAllowBashIfSandboxed`（既定 true。sandbox の中のコマンドを確認なしで動かす）・`excludedCommands`・`allowUnsandboxedCommands`（false で `dangerouslyDisableSandbox` の再試行を止める）・`filesystem.allowWrite`/`denyWrite`/`denyRead`/`allowRead`・`network.allowedDomains`（初めは空）/`deniedDomains`/`strictAllowlist`（リポジトリの設定では効かない）・`credentials`（deny と mask。組み込みの一覧はない）。配列はスコープをまたいで合わさる。sandbox のパスは `/tmp/x` が絶対・`~/` がホームで、permissions の `//`・`/` と書き方が違う | S8 #sandbox ほか、S9 #configure-sandboxing・#network-isolation | 雛形では2つのパスの書き方の違いを注記する |
| 42 | 05 §4-5：既定で `~/.ssh` なども読める | 正しい | 読み取りは既定でマシンのほぼ全体。秘密は `denyRead` か `credentials` で列挙する | S9 #what-the-sandbox-restricts | なし |
| 43 | 01 C-4：sandbox の外で動くもの | 正しい | 組み込みのファイルと Web のツール（`denyRead` は Read を止めず、`allowedDomains` は WebFetch を縛らない）、hooks、MCP、LSP、status line、`apiKeyHelper` は外。自分で `!` に打つコマンドも多くのセッションで外 | S9 #what-runs-outside-the-sandbox | hook のスクリプトは sandbox で守られない（F19 の決まり5の「壊す操作をしない」が要る） |
| 44 | F12：`--setting-sources` と sandbox | 正しい（新規） | 外した源の `sandbox.filesystem`・Edit の規則・Read の deny は sandbox の構成に入らない（v2.1.246＝2026-08-25 から） | S9 #configure-sandboxing、S20 | 雛形の確認で源を絞ると sandbox の境界も変わる |

### 2.4 設定の仕様と schema

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 45 | 01 B（`$schema` で補完） | 正しい（補足） | 公式の文書は `https://json.schemastore.org/claude-code-settings.json` を Claude Code の設定の「公開された JSON schema」として挙げ、新しい CLI に遅れることがあり、新しいキーで警告が出ても設定が誤りとは限らないと書く。URL は今 www.schemastore.org へ 301 で転送される。Anthropic のドメインに置かれたスキーマは文書に見当たらない | S7（設定の例の直後の段落）、S23 | 「公式の文書が案内する、SchemaStore の共同のスキーマ」と書く |
| 46 | F12・F11 #8：settings の schema で CI の静的な検査をする | 一部誤り | 取得したスキーマ（draft-07）は、最後の大きな同期が「v2.1.220 に合わせる」（2026-07-27）で、その後は小さな直し（最後は 2026-10-19）だけ。hooks のイベントは31で `PreModelSwitch`・`PostModelSwitch` がなく、hooks のオブジェクトが `additionalProperties: false` なのでこの2つは誤りになる。command の hook も `additionalProperties: false` で `onFailure` がなく、`"onFailure": "block"` を書いた正しい設定が落ちる。最上位は `additionalProperties: true` で、最上位のキーの綴りの誤りは通る。permission の規則の形は、列挙したツール名と `mcp__` だけを通す | S23、S24 | そのままでは F19 の hooks（`onFailure` を使う）が検査で落ちる。自前のスキーマか上書きを持つ（§4 の提案 3） |
| 47 | 01 E-1：サブエージェントの front matter の必須は name と description | 正しい（補足） | 必須は2つ。知らない項目は報告なしに無視する（v2.1.296＝2026-10-09 から debug log に最大5件の名前を出す）。name は256字まで、`:` を含めず、`-` で始めない。name がないと文書として扱い、description がないと飛ばす（どちらもセッションには出ない）。01 が挙げた項目名と「skills は最初の32個まで」は現行の表と合う。`experimental.cacheTtl` も足された | S3 #frontmatter-reference・#subagent-files-claude-code-skips・#preload-skills-into-subagents | 綴りの誤りは黙って効かないので、静的な検査で拾う |
| 48 | 01 D-2：skill の front matter | 正しい（補足） | Claude Code ではすべて任意で、description を勧める（ないと本文の最初の行を使う）。知らない項目は黙って無視し、YAML が壊れていても項目なしで読む。開きの `---` が1行目でないと front matter として読まない。Agent Skills の仕様では name（1〜64字、小文字の英数字とハイフン、親のフォルダ名と一致）と description（1〜1024字）が必須。claude.ai へのアップロードと Skills API は、6つの項目（name・description・license・compatibility・metadata・allowed-tools）以外があると誤りにする | S10 #frontmatter-reference・#using-skill-frontmatter-outside-claude-code、S25 | 教材の雛形はどちらの道でも通るよう、name と description を必ず書く |
| 49 | F11 #8・F12：skill と subagent の front matter を CI で検査できるか | 正しい（新規） | 公式の検査器は `claude plugin validate <パス> [--strict] [--json]`。`.claude` を渡すと中の skills・agents・commands を検査し（v2.1.233＝2026-08-14 から）、`--strict` で知らない項目も誤りにする。終了コードは 0（通過）・1（失敗）・2（検査器の失敗）。settings.json は対象に書かれていない。`claude doctor` は信頼の確認なしに今のフォルダの設定を読み、拒んだ項目を示す。どちらも CI に Claude Code の CLI を入れる必要があり、ログインが要るかは文書にない。Agent Skills には `skills-ref validate` がある | S19 #plugin-validate、S14、S22、S25 | CI では自前の検査を主にし、`claude plugin validate --strict` は制作の環境の確認に加える案 |

### 2.5 サイトの道具（F9）

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 50 | F9：Zensical の 11-05 の予告（「中身は未確認」） | 正しい（新規） | (1) Zensical 0.1.0 で 0.0.x の alpha を抜け、頼れる版の系列を始める（1.0 までは 0.x で、公開の API は変わりうるが、互換を設計の制約とし、変えるときは移行の道を示すとする）。(2) Studio（closed source の執筆のアプリ。Free・Pro・Team）と Spark Community（個人向けの有料の会員）を始める。(3) Material の重要な保守を6か月延ばし 2027-05-05 までとする。(4) OSS は MIT のまま無料で、移行を強いず既存のプロジェクトは動き続けるとする | S26 | サイトの作り方への直接の影響は小さい。0.1.0 の後に F9 の評価をする案のままでよい |
| 51 | F9（決定）：Material の保守は 2027-05-05 に終わる | 正しい | 9.8.0 の Release の本文と Zensical の予告がともに 2027-05-05 とする。もとは 2026-11-05 の予定で（9.7.7 の本文）、延長は 2026-09-16 に告知された（S36 の更新の記録） | S35、S26、S36 | なし |
| 52 | F9：Material の最新は 9.8.0（2026-10-24。主にセキュリティの修正、Python 3.11 以上） | 正しい | 依存の下限を上げて既知の脆弱性を避ける版で、Python 3.8〜3.10 を外した。依存に `mkdocs>=1.6,<2` を持つ | S35、S37 | uv で 3.11 以上を固定する案は正しい。この環境の `python3` は 3.10.12 で、そのままではビルドできない |
| 53 | F9：Zensical の最新は 0.0.74（2026-10-30）で alpha | 正しい | PyPI の分類は「Development Status :: 3 - Alpha」、MIT、Python 3.11 以上。依存に pymdown-extensions（11.0 以上）と jinja2 を持つ | S37、S34 | なし |
| 54 | F9：Material からの移行の互換（テンプレートの上書き・独自の CSS と JS） | 正しい（新規） | `mkdocs.yml` をそのまま読み、同じプロジェクトを `mkdocs build` と `zensical build` で作れる。未対応の設定は `hooks`（MkDocs の Python の hooks）。テンプレートは MiniJinja で描き、任意の Python の関数を呼べない。Material 9.6.18（2025-08-22）以降を元にした上書きはおおむねそのまま動く。追加の CSS と JS は classic の変種でそのまま動き、JS の初期化は `document$` を購読する。`custom_dir` はそのまま使う | S27、S30、S37 | 決定の「MkDocs の hooks を使わない」と合う。`overrides/` は 9.8 系のテンプレートを元に作り、Python の関数を呼ばない |
| 55 | F9：プラグイン | 正しい（新規） | 任意の MkDocs のプラグインは動かさず、主なものを自前で作り直している（search・tags・blog・offline・privacy・social・redirects・macros・llmstxt・minify など）。一覧にないプラグインの設定は黙って無視し、対応するプラグインの知らない設定は誤りにする。自作のプラグインは動かせず、別の Module API を準備中（まず Spark の会員に早期提供） | S28、S33 | 「自作プラグインを使わない」決定と合う。macros は Zensical でも動く（0.0.40 から）が、F5 の理由で使わない案のままでよい |
| 56 | F9：pymdownx の拡張 | 正しい（新規） | Python Markdown Extensions を依存に持ち、原則すべて動くとし、Arithmatex・Caption・Caret/Mark/Tilde・Details・Emoji・Highlight・InlineHilite・Keys・SmartSymbols・Snippets・SuperFences・Tabbed・Tasklist を「そのまま動く」と挙げる。Arithmatex の generic 以外の設定は対応の外 | S29 | 使う拡張をこの一覧に寄せると、両方で動く見込みが高い |
| 57 | F9・日本語のサイト：検索 | 正しい（新規。要注意） | Zensical は新しく書いた検索を持ち、Lunr を使わない。言語は `theme.language` から取り、search の `lang`・`pipeline`・`jieba_dict` などは無視する。検索の画面は今は英語だけ（多言語の検索には影響しないとする）。日本語の語の区切り方は書かれていない | S31、S28 | 日本語の検索の質を、試験ビルドで確かめる項目にする（Material の側は `lang: ja` を使う） |
| 58 | F11 #3：`--strict` のリンクの検査 | 正しい（新規） | Zensical は内部のリンクと anchor をビルドのときに検証し、`zensical build --strict` か設定の `strict: true` で、問題があれば終了コード 1 で止める | S32 | F11 #3 を両方のビルドで回せる |
| 59 | F9：Zensical の CLI の違い | 正しい（新規） | `gh-deploy` と `get-deps` がない。`--theme`・`--use-directory-urls`・`--site-dir` もなく、設定で書く | S27 | GitHub Pages への公開は `mkdocs gh-deploy` に頼らず、GitHub Actions などで行う |
| 60 | F9：MkDocs 2.0 と Material の関係 | 正しい（新規） | MkDocs の安定版は 1.6.1（2024-08-30）で、2.0 は開発版（2.0.dev1〜dev6、2026-08-29〜09-15）だけが PyPI にある。Material は 9.7.2（2026-02-18）から build で「MkDocs 2.0 と互換でない」旨の警告を出し（`NO_MKDOCS_2_WARNING=1` で消える）、9.7.5（2026-03-10）から MkDocs を 2 未満に制限した。Material のチームは、2.0 はプラグインの仕組みを持たず、テーマの仕組みと設定の形式（TOML）が変わるので Material は動かないと述べる（当事者の見解。MkDocs 側の一次資料は読んでいない） | S35、S36、S37 | Material 9.8 の固定で MkDocs 1.6 系に固定される。`mkdocs` を直接の依存に書くなら `<2` を付ける |

### 2.6 AI の利用の指定と出典の URL

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 61 | F7・requirements §2：主な出典のドメインに noai・noimageai の指定があるか | 正しい（どれにもない） | 割り当ての17のドメインと、読んだ追加の6つの代表のページに、X-Robots-Tag と meta の noai・noimageai はない。TDM の拒否の指定もない。robots.txt で AI のクローラに特別の指定があるのは github.com と zenn.dev だけ（§1.3） | §1.3 の実行の記録 | 資料にしてよい。ただし代表の1ページで確かめただけ |
| 62 | F7・requirements §7（リンク）：出典の URL の転送 | 正しい（新規） | `claude.com/blog/…` は `claude.com/resources/articles/…` へ、`www.anthropic.com/engineering/…` は `www.anthropic.com/research/…` へ 308 で転送される（3件で確かめた）。docs.claude.com の prompt-improver は platform.claude.com の同名へ転送され、さらに claude-prompting-best-practices へ転送される。調査資料には claude.com/blog が5種16か所、anthropic.com/engineering が9種45か所ある | 取得の記録（2026-11-03） | `data/sources.yml` には転送先の URL を持つ。リンクの検査でリダイレクトを報告する（§7 の方針どおり） |
| 63 | tools/check_noai.py：転送をたどって判定する（docstring） | 一部誤り（道具の不具合） | この環境の `python3` は 3.10.12 で、urllib が 308 をたどるのは 3.11 から。308 で転送するページでは、転送前の応答の本文を見て「指定はない」と出す | 実行の記録、S38 | 道具を直す（§4 の提案 12）。直すまでは「HTTP 308」と出たら転送先で確かめ直す |

---

## 3. 新しく分かったこと

### 3.1 F19 の候補の規則と、縛る仕組みの対応

文書の上では、候補の規則ごとに使える仕組みが違う（#7・#10・#14・#15・#17）。

| 候補の規則 | 強制の仕組み | 理由と代わりを返すには | メインと担当を分けるか | 注意 |
| --- | --- | --- | --- | --- |
| AI の利用を断るサイトへの WebFetch を拒む | `permissions.deny` に `WebFetch(domain:atcoder.jp)`・`WebFetch(domain:*.atcoder.jp)`・`WebFetch(domain:codeforces.com)`・`WebFetch(domain:*.codeforces.com)` | deny の規則に理由の文を足す設定は、文書に見当たらない。理由を返したいなら、同じ判定の PreToolUse の hook を足し、`permissionDecisionReason` で返す | 分けない（読者にも、信頼の前から効く） | curl などは sandbox を入れたときだけ止まる。WebSearch・MCP のツールは外 |
| 生成物を手で書き換えさせない | `permissions.deny` に `Edit(/生成先/**)` | 同上 | 分けない | 生成スクリプトは子プロセスなので止まらない（意図どおり）。シェルの `sed`・`tee`・リダイレクトは止まる |
| メイン以外に生成と commit をさせない | PreToolUse の hook（matcher は `Bash`）。`agent_id` があり、コマンドが `git commit`・`git push`・生成のスクリプトに当たれば deny | `permissionDecisionReason` に「commit と生成はメインが行う。変更は報告のファイルに書く」 | `agent_id` の有無で分ける | deny の規則も `disallowedTools` も使えない。照合は文字列なので、`git -C . commit` などの別の書き方はスクリプトで拾う。ワークフローの担当で効くかは未確認（#4） |
| 変わりやすい値の手書きを止める | PreToolUse の hook（Edit・Write の `new_string`・`content` を調べる） | 同上 | 必要なら `agent_id` | 判断を含みやすく、止めすぎの恐れが大きい（F19 の決まり1）。目印の間（`fact:begin`〜`fact:end`）への手書きだけを止める、など機械で判定できる形に絞る |

役割の分け方の案（推論。試していない）：強制は依存のない deny の規則に任せ、hook は理由の文と記録だけを受け持つ規則では `onFailure` を付けない（hook が壊れても deny が止める）。hook だけが強制を担う規則（担当の commit）には `onFailure: "block"` を付け、スクリプトは依存（`python3` など）の有無を自分で確かめる。読者の環境で依存が欠けると、当たった呼び出しがすべて止まるので、matcher と `if` を狭くする（F19 の決まり3・5）。

### 3.2 止めたときの返し方

- exit 2 より、exit 0 と JSON（`permissionDecision: "deny"` と `permissionDecisionReason`）のほうが、理由と代わりを構造立てて返せる。exit 2 では stderr がそのまま理由になる（#15）
- 文書は、hook が Claude に渡す文を事実の形で書くよう勧め、システムの命令のような形は prompt injection の防御を働かせると注意している（#16）。F19 の決まり2「止められた側が回避策を探さない」には、命令口調より「このリポジトリの規則と、代わりの手段」を事実として書くほうが合う
- 止めた記録は、PermissionDenied ではなく PreToolUse の hook で取る（#18）

### 3.3 読者の環境での振る舞い（F19 の決まり5）

- 対話のセッションでは、読者が信頼のダイアログを受け入れるまで hooks は走らない。`.claude/settings.json` の deny は信頼の前から効く（#19）
- `-p` で読者がこのリポジトリを使うと、信頼の確認なしに hooks が走る。hooks は sandbox の外で、利用者の権限で動く（#43）
- 担当が `.claude/` を書き換えて縛りを外すことは、bypassPermissions でない限り確認か分類器の審査を通る（#20）

### 3.4 雛形の確認で作者の設定を切り離す手順（F12。文書から組んだ案で、動かしていない）

API キーを使わずに、作者の `~/.claude` を混ぜない形は、文書の上では次の組み合わせになる（#24〜#35）。

1. **専用の置き場所**：リポジトリの外のフォルダを `CLAUDE_CONFIG_DIR` にする。そこで一度だけ `/login` する（サブスクリプション）か、`claude setup-token` のトークンを `CLAUDE_CODE_OAUTH_TOKEN` に置く。これで `~/.claude` の settings・CLAUDE.md・rules・skills・agents・plugins・auto memory・`.claude.json` が入れ替わる
2. **使い捨てのフォルダ**：CLAUDE.md を持たないフォルダの下（`/tmp` の下など）に作り、雛形の `.claude/` を写す。雛形の `permissions.allow` やサブエージェントの hooks を確かめるときは、専用の置き場所の `.claude.json` に `projects["<フォルダ>"].hasTrustDialogAccepted: true` を書く
3. **環境変数**：`ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN` を外す。`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`、`ENABLE_CLAUDEAI_MCP_SERVERS=false` を置く。版を揃えたいなら `DISABLE_AUTOUPDATER=1`。作者のシェルのほかの `CLAUDE_*`・`ANTHROPIC_*` の変数も外す
4. **起動**：`claude -p --setting-sources project,local --strict-mcp-config --output-format json …`（`stream-json` なら拒否が `permission_denied` の行で出る）。モデルは `--model` で固定する
5. **対照**：同じ操作を `--safe-mode` でも流し、雛形がないときの結果と比べる（`-p` は承認の要る呼び出しを既定で拒むので、「止められた」だけでは雛形の効き目と言えない。#32）
6. **記録**：`claude --version`・OS・日付と、`claude doctor` の出力（落とした設定がないか。#31）

### 3.5 静的な検査（F11 #8・F12）

- settings.json：公式の文書が案内するスキーマは SchemaStore のもので、2026-11-03 時点で v2.1.220 相当であり、`onFailure` と新しい2つのイベントを誤りにする（#45・#46）。最上位のキーの綴りの誤りは通す
- サブエージェントと skill：Claude Code は知らない項目を黙って無視するので、綴りの誤りは効かないまま気づけない（#47・#48）。公式の検査器 `claude plugin validate .claude --strict` は知らない項目も誤りにできる（#49）
- そのため、土台作りでは自前の検査（使うキーの許可の一覧、必須の項目、確かめた版）を主にするのがよい

### 3.6 sandbox を入れるとき（decisions「危ない雛形を試す場所」）

- この環境（Ubuntu 22.04.5、WSL2）では `sudo apt install bubblewrap socat` で足りる見込みである。AppArmor の追加の設定は Ubuntu 24.04 以降の話で、この環境にはそのキーがない（#38）
- seccomp のフィルタは任意で、入れると Unix ソケットを塞ぐ。WSL2 では Windows の実行ファイルの起動もこのソケットを通る（#36・#37）
- 依存が欠けると既定で sandbox なしで動くので、sandbox を前提にする雛形には `failIfUnavailable: true` を付ける（#40）

### 3.7 Zensical と Material（F9）

- 11-05 の予告の中身は、0.1.0 の版の系列の開始、商用の Studio と Spark の開始、Material の保守の延長（2027-05-05）である（#50・#51）
- 互換の主な条件：MkDocs の `hooks` は未対応、テンプレートは MiniJinja（Python の関数を呼べない）、classic の変種で見た目と追加の CSS・JS を保つ、プラグインは自前の作り直しのものだけが動く（#54・#55）
- 日本語のサイトに固有の不安は検索である。Zensical の検索は Lunr を使わない新しいもので、画面は英語だけ、日本語の区切り方は文書にない（#57）
- Zensical には `gh-deploy` がないので、公開の手順は GitHub Actions で組む（#59）
- MkDocs 2.0 は開発版の段階で、Material は MkDocs を 2 未満に固定している（#60）

### 3.8 出典の URL の転送（F7・requirements §7）

claude.com の blog と anthropic.com の engineering の記事が、別の道に転送されている（#62）。転送は効いているのでリンクは切れていないが、`data/sources.yml` には転送先を持たせ、リンクの検査で転送を報告するのがよい。

---

## 4. 提案

1. **format-and-operations.md F9 の「2026-11-03 に確かめた事実」**：「11-05 に変更の予告がある（中身は未確認）。kyopro-atlas の記録の「0.1.0 は 2026-11-05 の予定」は 10-21 時点の情報である」を、次に直す。
   「11-05 に、Zensical 0.1.0 で 0.0.x の alpha を抜けて頼れる版の系列を始め（1.0 までは 0.x）、closed source の執筆のアプリ Studio と個人向けの会員 Spark Community を始め、Material の重要な保守を 2027-05-05 まで延ばす、と予告している（zensical.org/upcoming-changes/、2026-11-03 確認）。Material 9.8.0 は依存を `mkdocs>=1.6,<2` に制限している」
2. **F9 の案に足す文**：「Zensical の試験ビルドでは、日本語の検索（Lunr を使わない新しい検索で、日本語の扱いが文書にない）、classic の変種での見た目、`overrides/` のテンプレート（MiniJinja で、Python の関数を呼べない）を確かめる。公開は `mkdocs gh-deploy` に頼らない（Zensical にない）」
3. **F11 #8 と F12 の「静的な検査」**：次の文を足す。「settings の schema は、公式の文書が案内する SchemaStore のもの（2026-11-03 時点で v2.1.220 相当。`onFailure` と PreModelSwitch・PostModelSwitch を誤りにする）をそのまま使わず、使うキーを足した自前の写しを `schema/` に置き、確かめた Claude Code の版を書く。skill と subagent の front matter は自前の検査で必須の項目（subagent は name・description、教材の skill の雛形は name・description）と項目名の綴りを確かめる。制作の環境では `claude plugin validate .claude --strict` も流す」
4. **F12 に足す文**：「実際に動かす確認は、リポジトリの外の専用の `CLAUDE_CONFIG_DIR`（サブスクリプションでログイン、または `claude setup-token` のトークン）と、CLAUDE.md を持たない使い捨てのフォルダで、`claude -p --setting-sources project,local --strict-mcp-config` で行う。`ANTHROPIC_API_KEY` を外し、`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`・`ENABLE_CLAUDEAI_MCP_SERVERS=false` を置く。`-p` は信頼していないフォルダの `permissions.allow` とサブエージェントの hooks を使わないので、専用の `.claude.json` で使い捨てのフォルダを信頼させる。`-p` は承認の要る呼び出しを既定で拒むので、`--safe-mode` の対照と比べる。`--bare` は API キーが要るので使わない」
5. **F19 に足す文**（決まりの具体）：「(a) AI の利用を断るサイトの WebFetch と生成物の手書きは `permissions.deny` で強制する（`WebFetch(domain:…)` は各ドメインと `*.` 付きの2行ずつ、`Edit(/生成先/**)`）。(b) メイン以外の生成と commit は、`agent_id` の有無で判定する PreToolUse の hook で止める（deny の規則と `disallowedTools` では担当だけを止められない）。(c) 止めるときは exit 0 の JSON で `permissionDecision: "deny"` と `permissionDecisionReason` を返し、理由と代わりの手段を事実の形で書く。(d) 強制を deny の規則が担うものでは、hook は理由と記録だけを受け持ち `onFailure` を付けない。hook だけが強制を担うものには `onFailure: "block"` を付け、依存の有無をスクリプトで確かめる。(e) 止めた記録は PreToolUse の hook で `state/` に書く（PermissionDenied は auto mode の判定でしか発火しない）。(f) ワークフローの担当で hooks と `agent_id` が効くかは、土台作りで確かめてから頼る」
6. **01 E-1 の frontmatter の項（154行目付近）に足す文**：「`disallowedTools` の項目に `Bash(git push *)` のような指定子を付けても Bash 全体が外れる。特定のコマンドは `permissions.deny` の Bash の規則で止める（メインとサブエージェントの両方に効く）— [sub-agents](https://code.claude.com/docs/en/sub-agents)（2026-11-03 確認）」
7. **01 F-1 の matcher の項（201行目付近）に足す文**：「`,` 区切りは v2.1.191 から。matcher は大文字小文字を区別し、配列で書くと無効。`if` の Bash の判定は best-effort で、確実な拒否には permissions を使う。hooks の入力の `agent_id` はサブエージェントの中でだけ付く（v2.1.69 から）」
8. **01 J の `--bare` と「注意」の項（258〜259行目）に足す文**：「`--bare` の認証は `ANTHROPIC_API_KEY` か `--settings` の `apiKeyHelper` だけで、サブスクリプションのログインは読まない。`-p` の未信頼のフォルダでは、`.claude/settings.json` の `permissions.allow` とサブエージェントの front matter の hooks は使われない（deny・ask と設定ファイルの hooks は使われる）」
9. **01 B の設定の項（84行目）に足す文**：「`$schema` のスキーマは SchemaStore のもので、CLI の新しい版に遅れる（2026-11-03 時点で v2.1.220 相当。`onFailure` がない）」
10. **05 §4-5 の Sandbox の「仕組み」（448行目付近）に足す文**：「WSL1 では使えない。Ubuntu 24.04 以降は AppArmor の設定が要ることがある。seccomp のフィルタは任意。依存が欠けると既定で sandbox なしで動く（`failIfUnavailable: true` で起動を止める）— [Sandboxing](https://code.claude.com/docs/en/sandboxing)（2026-11-03 確認）」
11. **decisions.md「危ない雛形を試す場所」の補足**：「Claude Code の sandbox が Linux・WSL2 で bubblewrap と socat を使うことは、公式の sandboxing の文書で確かめた（2026-11-03、工程2 R7）。この環境（Ubuntu 22.04.5）では AppArmor の追加の設定は要らない見込み」
12. **tools/check_noai.py**：Python 3.10 でも 308 の転送をたどるよう、転送の処理で 308 を 307 と同じに扱う（`redirect_request` で 308 を受け、`http_error_308` を定義する）。または、Python 3.11 以上で実行すると docstring に書く。直すまでは、出力が「HTTP 308」なら転送先の URL で確かめ直す
13. **requirements §7 の「リンク」**：「公式文書は移転が多い（docs.anthropic.com → code.claude.com など）」の例に、「claude.com/blog → claude.com/resources/articles、anthropic.com/engineering → anthropic.com/research（2026-11-03 に転送を確認）」を足す。F7 に「sources.yml には転送先の URL を持つ」を足す

---

## 5. 確かめていないこと

1. **Claude Code を動かす確認は一切していない**（brief §4）。とくに次は文書だけでは決まらない：ワークフローの担当で設定の hooks が走るかと、そのときの `agent_id`・`agent_type`（#4）。fork のサブエージェント（`subagent_type: "fork"`）に `agent_id` が付くか。hook の deny が `permission_denials` に出るか。`--settings` で渡したファイルの `permissions.allow` が、未信頼のフォルダの `-p` で使われるか（文書の表は `.claude/settings.json` だけを挙げる）。`claude plugin validate` と `claude doctor` がログインなしで動くか。§3.4 の手順の全体と、`CLAUDE_CONFIG_DIR` と `setup-token` のトークンの組み合わせ
2. hooks-guide・devcontainer・sandbox-environments・security・settings-example のページは取得したが、読み込んでいない（hooks の reference などで足りた）
3. SchemaStore のスキーマの欠けは、`onFailure`・2つのイベント・いくつかの sandbox のキーだけを見た。今の文書のキーとの全数の突き合わせはしていない
4. Zensical：日本語の検索の質、classic の変種での実際の見た目、Material 9.8 のテンプレートが MiniJinja で動くか（文書は 9.6.18 以降はおおむね動くとする）、0.1.0 の実際の中身（11-05 の後に出る）
5. MkDocs 2.0 については Material のチームの記事（当事者の見解）だけを読み、MkDocs 側の発表や roadmap は読んでいない
6. AI の利用の指定は、各ドメインの代表の1ページで確かめただけである。記事ごとに著者が指定を変えられるサイトで、記事ごとの差がありうるかは確かめていない
7. Agent Skills の `skills-ref validate` が Claude Code の拡張の項目を誤りにするかは読んでいない
8. WebSearch・MCP のツール・Claude in Chrome を、AI で開かないサイトに向けない方法は調べていない（WebSearch の入力の `blocked_domains` を PreToolUse の `updatedInput` で足す余地はある。推論）
9. claude.com/blog などの転送がいつ始まったかは分からない

---

## 6. 使った量の目安

- 道具の呼び出し：約130回（Bash が大半。ファイルの書き込みはこの報告の1回）
- Web の取得：約160回（curl と `check_noai.py`。内訳は code.claude.com の文書25、zensical.org 約20、noai の確認と robots.txt・tdmrep.json 約60、GitHub の API・npm・PyPI・SchemaStore など約15、転送の確認約10）。WebFetch の道具は使っていない。Web 検索は0回
- 時間：約35分（2026-11-03 20:38 頃〜21:12 頃）
