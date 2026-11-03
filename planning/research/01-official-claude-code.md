# Claude Code 公式機能・公式推奨プラクティス棚卸し（2026年10月時点）

> **調査メタ情報**
> - 確認日: **2026-10-29**（全項目共通。個別項目にも記載）
> - 確認時点の最新版: **v2.1.312（2026-10-27 公開, npm `latest`/`next`）**、`stable` タグは v2.1.308 — [npm registry](https://registry.npmjs.org/@anthropic-ai/claude-code)
> - バージョン→日付の対応は npm registry の公開日時から算出（例: v2.1.30=2026-02-03, v2.1.90=2026-04-01, v2.1.198=2026-07-01, v2.1.257=2026-09-01, v2.1.287=2026-10-01）— [npm registry](https://registry.npmjs.org/@anthropic-ai/claude-code)
> - 一次情報: 公式ドキュメント `code.claude.com/docs/en/*`（docs.anthropic.com / docs.claude.com からは移行済み。旧URLは本調査環境から到達不可）、公式 CHANGELOG — [CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
> - **重要**: 旧エンジニアリングブログ記事「Claude Code: Best practices for agentic coding」の URL（anthropic.com/engineering/claude-code-best-practices）は現在 **公式ドキュメントの Best practices ページへ 302 リダイレクト**される。つまり同記事の内容は docs に吸収・継続更新されている — [リダイレクト元](https://www.anthropic.com/engineering/claude-code-best-practices) → [Best practices](https://code.claude.com/docs/en/best-practices)
> - 公式ドキュメントのサイト構成（教材の章立ての参考）: Getting started / Core concepts / Use Claude Code / Platforms and integrations（cloud, desktop, mobile, Chrome, computer use, VS Code, JetBrains, Slack）/ Code review and PRs / Agents and parallel work / MCP / Skills / Artifacts / Automation（hooks, channels, scheduled tasks, goal, headless, deep links）/ Plugins（Mods 含む）/ Troubleshooting — [docs map](https://code.claude.com/docs/en/claude_code_docs_map.md)

---

## Key Question 1: Claude Code の現行機能・概念の全体像（領域別インベントリ）

### Takeaway
2026年10月時点の Claude Code は「エージェントループ（コンテキスト収集→行動→検証）＋ツール」の上に、常時ロードされる文脈（CLAUDE.md / rules / output style）、必要時ロード（skills / MCP tool search）、隔離実行（subagents / workflows / worktrees / cloud）、決定的自動化（hooks / permissions / sandbox）の4層の拡張を重ねた構造で、公式は「コンテキストウィンドウが最重要資源」という一点からほぼ全ての推奨を導いている。2026年に auto mode（v2.1.283 で既定化）、dynamic workflows、agent view、/goal、cross-session messaging、AGENTS.md 対応、Mods などが追加され、旧来の `#` メモリショートカットや `/agents` ウィザードなどは削除済み。

### Cited Findings

#### 0. 基本概念（教材の土台）

**0-1. エージェントループとツール**
- **概要**: Claude はタスクを「gather context → take action → verify results」の3フェーズで回し、ツール使用の結果が次の判断に戻る。組み込みツールは File operations / Search / Execution / Web / Code intelligence の5カテゴリ（code intelligence は plugin 導入が必要）。Claude Code はモデルを包む "agentic harness" と定義 — [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- **なぜ重要か**: 「チャットボットではなく、読む・実行する・直す・検証するエージェント」という理解が、指示の出し方（検証手段を渡す等）の前提になる — [Best practices](https://code.claude.com/docs/en/best-practices)
- **公式の推奨**: 「Delegate, don't dictate」= 有能な同僚に任せるように文脈と方向性を与え、読むファイルやコマンドは Claude に任せる。会話的に反復してよい（完璧なプロンプトは不要）。`Esc` で中断、実行中に入力して Enter で割り込み（queued）可能 — [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- **確認日**: 2026-10-29

**0-2. 実行環境とインターフェース**
- **概要**: 実行環境は Local（自機）/ Cloud（Anthropic 管理 VM または組織の self-hosted 環境）/ Remote Control（自機で実行しブラウザ・スマホから操作）の3種。インターフェースは terminal、desktop app、IDE 拡張、claude.ai/code、Remote Control、Slack、CI/CD。どこでもエージェントループは同一 — [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- **確認日**: 2026-10-29

**0-3. コンテキストウィンドウ（最重要資源）**
- **概要**: 会話・読んだファイル・コマンド出力すべてが context window を消費し、満ちるほど性能が劣化する（初期指示を「忘れる」）。「Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills.」— [Best practices](https://code.claude.com/docs/en/best-practices)
- **補足**: Claude Code は自前のコンテキストも追加する（CLAUDE.md、output style の指示、読んだファイルの変更通知、コミット/PR の attribution 行など = system reminder）。attribution は `attribution` 設定、組み込み git 指示は `includeGitInstructions: false` で外せる — [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- **公式の推奨**: status line でコンテキスト使用量を常時監視、`/context` で内訳確認 — [Best practices](https://code.claude.com/docs/en/best-practices)
- **確認日**: 2026-10-29

**0-4. 拡張機能の使い分け（Extend Claude Code）**
- **概要（公式の比較表）**: CLAUDE.md=毎セッション常駐の規約 / Output style=応答の役割・トーン・形式 / Skill=再利用可能な知識・起動可能ワークフロー / Subagent=隔離コンテキストで要約を返す / Dynamic workflow=多数の subagent をスクリプトで回す / Cross-session messaging=自分の別セッションへメッセージ / Code intelligence=LSP による定義ジャンプ・型エラー / MCP=外部サービス接続 / Hook=ライフサイクルイベントで必ず実行 / Artifact=出力を非公開 Web ページとして公開 / Plugin=これらを束ねる配布単位 — [features-overview](https://code.claude.com/docs/en/features-overview)
- **公式の「段階的に足す」トリガー表**: 同じ規約・コマンドを2回間違えた→CLAUDE.md / 毎回「短く」「説明多めに」と言っている→output style / 同じ開始プロンプトを打っている→user-invocable skill / 同じ手順書を3回目に貼った→skill / ブラウザからデータをコピペし続けている→MCP / シンボル探索で多数ファイルを読む→code intelligence plugin / 副作業の出力が会話を埋める→subagent / 毎回必ず起きてほしい→hook / 2つ目のリポジトリに同じ設定→plugin — [features-overview](https://code.claude.com/docs/en/features-overview)
- **コンテキストコスト**: CLAUDE.md=全文が毎リクエスト / Output style=毎リクエスト（Default は0）/ Skills=説明文のみ常駐、本文は使用時 / MCP=ツール名のみ、スキーマは必要時（tool search 既定ON）/ Subagents=本体から隔離 / Hooks=出力を返さない限りゼロ — [features-overview](https://code.claude.com/docs/en/features-overview)
- **重ね合わせ規則**: CLAUDE.md は加算（全階層が同時に効く）、Skills/Subagents は名前で上書き（skills: managed > user > project、subagents: managed > CLI flag > project > user > plugin）、MCP は名前で上書き（local > project > user）、Hooks はマージ（全部発火）— [features-overview](https://code.claude.com/docs/en/features-overview)
- **公式ブログによる補強（2026-06-18 公開）**: 「Always do Y」を CLAUDE.md に書くなら hook へ、「Never do X」は指示ではガードレールにならないので hooks/permissions/managed settings へ、長い手順は skill へ、1ディレクトリだけのルールは `paths:` でスコープ、個人の好みはユーザーレベルへ — [Steering Claude Code (claude.com blog)](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)
- **確認日**: 2026-10-29

---

#### A. メモリと指示ファイル

**A-1. CLAUDE.md とメモリ階層**
- **概要**: 毎セッション開始時に読み込まれる Markdown の持続的指示。配置先は ① Managed policy（macOS `/Library/Application Support/ClaudeCode/CLAUDE.md`、Linux/WSL `/etc/claude-code/CLAUDE.md`、Windows `C:\Program Files\ClaudeCode\CLAUDE.md`）② Project（`./CLAUDE.md` または `./.claude/CLAUDE.md`、git で共有）③ User（`~/.claude/CLAUDE.md`）④ Local（`./CLAUDE.local.md`、個人用・.gitignore 推奨）— [memory](https://code.claude.com/docs/en/memory)
- **読み込み順**: 作業ディレクトリとその祖先の CLAUDE.md / CLAUDE.local.md を起動時に読み、**上書きではなく連結**。ルート側→作業ディレクトリ側の順に並び、同一ディレクトリ内では CLAUDE.local.md が後。サブディレクトリの CLAUDE.md は、そこのファイルを読む/編集した時点で遅延ロード。`--add-dir` 先の CLAUDE.md は既定では読まず、`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` で読む — [memory](https://code.claude.com/docs/en/memory)
- **@import**: `@path/to/import` で他ファイルを展開。相対パスはインポート元ファイル基準、再帰は**最大4ホップ**。ただし import は整理用でありコンテキストコストは減らない（一緒にロードされる）。プロジェクト外の import は初回承認ダイアログが出る — [memory](https://code.claude.com/docs/en/memory)
- **なぜ重要か**: コードから推測できない文脈（コマンド、規約、落とし穴）を毎回与える唯一の常駐手段。ただし「enforced configuration ではなく context」なので、絶対に守らせたいことは PreToolUse hook で — [memory](https://code.claude.com/docs/en/memory)
- **公式の推奨**: 1ファイル **200行未満**を目安。`/init` で雛形生成→育てる。各行に「これを消したら Claude は間違えるか?」と問い、No なら削る。含める: 推測できない Bash コマンド、既定と違うコードスタイル、テスト手順、ブランチ命名/PR 規約、プロジェクト固有の設計判断、環境の癖、非自明な落とし穴。除外: コードを読めば分かること、標準的言語規約、詳細な API ドキュメント（リンクにする）、頻繁に変わる情報、長い説明、ファイル単位の説明、「きれいなコードを書け」等の自明事項。守られない1行だけ「IMPORTANT」等で強調（多用すると効かない）。git に入れてチームで育てる。`/doctor` でコードから導出可能な内容の削減案を出せる — [Best practices](https://code.claude.com/docs/en/best-practices)
- **監査**: `/doctor prompt-audit`（`/checkup prompt-audit` も可）で CLAUDE.md・skills・agents・commands を「旧モデル向けの書き方」について監査 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [memory](https://code.claude.com/docs/en/memory)
- **大規模リポジトリ**: 他チームの CLAUDE.md を `claudeMdExcludes`（glob, 全設定層でマージ）で除外可能。managed CLAUDE.md は除外不可 — [memory](https://code.claude.com/docs/en/memory)
- **確認日**: 2026-10-29

**A-2. `.claude/rules/`（パス別ルール）**
- **概要**: CLAUDE.md を分割するためのルールファイル群。`paths` frontmatter を付けると該当ファイルを扱う時だけロードされ、コンテキストを節約。`~/.claude/rules/` でユーザー共通ルール。シンボリックリンクで共有可（初回承認あり）— [memory](https://code.claude.com/docs/en/memory), [features-overview](https://code.claude.com/docs/en/features-overview)
- **公式の推奨**: 言語別・ディレクトリ別ガイドラインは rules に、CLAUDE.md は全セッション必須事項だけに — [features-overview](https://code.claude.com/docs/en/features-overview)
- **確認日**: 2026-10-29

**A-3. Auto memory（自動メモリ）**
- **概要**: Claude 自身が訂正や好みから学習内容を書き溜める仕組み。リポジトリ単位（worktree 間で共有）、毎セッション `MEMORY.md` の**先頭200行または25KB**をロード。`/memory` で CLAUDE.md 編集・auto memory の有効/無効・エントリ閲覧 — [memory](https://code.claude.com/docs/en/memory), [commands](https://code.claude.com/docs/en/commands)
- **確認日**: 2026-10-29

**A-4. AGENTS.md 対応（2026年9月追加）**
- **概要**: v2.1.277（2026-09-18）以降、作業ディレクトリ以上に CLAUDE.md / CLAUDE.local.md が無ければ AGENTS.md を読む。`/config` の "Project instructions" で `claude-md-or-agents-md`（既定）/ `claude-md-and-agents-md` / `managed-only` 等を選択。CLAUDE.local.md を置くと AGENTS.md を読まなくなる点に注意。他ツールと共有するなら CLAUDE.md に `@AGENTS.md` を書く方式も可 — [memory](https://code.claude.com/docs/en/memory), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **確認日**: 2026-10-29

**A-5. 他ツールからの移行**
- **概要**: `/import codex|gemini|cursor` で OpenAI Codex / Gemini CLI / Cursor の指示ファイル・MCP 設定等を取り込み。`/init` も他ツールの設定を検出 — [commands](https://code.claude.com/docs/en/commands)
- **確認日**: 2026-10-29

---

#### B. 設定（settings.json 階層）

**B-1. settings ファイルと優先順位**
- **概要**: スコープは User `~/.claude/settings.json` / Shared project `.claude/settings.json`（コミットしてチーム共有）/ Project local `.claude/settings.local.json`（個人・git 外）/ Managed（`managed-settings.json`、MDM、claude.ai 管理コンソールからの server-managed settings）。優先順位は **Managed > コマンドライン（`--settings`）> Project local > Shared project > User** — [settings](https://code.claude.com/docs/en/settings)
- **配列はマージ**: `permissions.allow` 等のリストは上書きでなく結合（`fallbackModel`、`modelPicker`、`availableModels`、`modelSettings` は例外）— [settings](https://code.claude.com/docs/en/settings)
- **変更方法**: `/config`（または `/config key=value`、例 `/config thinking=false`）、ファイル直接編集（`"$schema": "https://json.schemastore.org/claude-code-settings.json"` で補完）、1セッション限定は `--settings`/フラグ/環境変数。多くの変更は再起動なしでホットリロード（`model`, `effortLevel` などは除く）。`/status` の `Setting sources` で読み込まれたファイルを確認、`claude doctor` で拒否されたエントリを確認 — [settings](https://code.claude.com/docs/en/settings)
- **落とし穴**: `permissions.defaultMode` の `auto` / `bypassPermissions` は project/local では無効（user か managed で設定）。project の `permissions.allow` や `env` は**ワークスペース信頼後**に有効、`deny`/`ask` は即時有効。クラウドセッションは user/local 設定を読まない — [settings](https://code.claude.com/docs/en/settings)
- **`~/.claude.json`**: アカウント情報、MCP 設定（local/user scope）、プロジェクト別の信頼状態などを Claude Code 自身が書く第5のファイル — [settings](https://code.claude.com/docs/en/settings)
- **確認日**: 2026-10-29

---

#### C. 権限・安全

**C-1. Permission modes（権限モード）**
- **概要**: `default`（UI 表示 "Manual"、CLI では `manual` も別名）=読み取りのみ自動 / `acceptEdits`=作業ディレクトリ内のファイル編集と mkdir/touch/mv/cp/sed/rm 等を自動 / `plan`=調査と計画のみ / `auto`=分類器(classifier)モデルがバックグラウンドで審査し危険なものだけブロック / `dontAsk`=事前許可以外はすべて拒否（CI 向け）/ `bypassPermissions`=すべて許可（隔離コンテナ/VM 専用）— [permission-modes](https://code.claude.com/docs/en/permission-modes)
- **切替**: `Shift+Tab` で `default → acceptEdits → plan`（有効なら `bypassPermissions`、最後に `auto`）。起動時 `--permission-mode`、既定は `permissions.defaultMode`。VS Code は `claudeCode.initialPermissionMode` — [permission-modes](https://code.claude.com/docs/en/permission-modes)
- **既定モード（2026年の大変更）**: **v2.1.283（2026-09-25）以降、ターミナルと VS Code の対話セッションの既定は auto mode**（それ以前は Pro/Max/Team のみ条件付き）。`claude -p` と Agent SDK の既定は Manual で、v2.1.302（2026-10-16）以降は承認が必要な呼び出しは allow ルール/hook/`canUseTool`/`--permission-prompt-tool` が無い限り拒否 — [permission-modes](https://code.claude.com/docs/en/permission-modes), [npm registry](https://registry.npmjs.org/@anthropic-ai/claude-code)
- **auto mode の詳細**: 分類器は既定で Sonnet 5（`CLAUDE_CODE_AUTO_MODE_MODEL` で変更）。既定でブロック: `curl | bash`、機密データの外部送信、本番デプロイ/マイグレーション、force push、`git reset --hard`、`terraform destroy`、未承認 PR のマージ、IAM 権限付与、`--dangerously-skip-permissions` でのエージェントループ起動等。既定で許可: 作業ディレクトリ内のファイル操作、lockfile 記載の依存インストール、読み取り専用 HTTP、非デプロイブランチへの push 等。auto に入ると `Bash(*)` 等の広すぎる allow ルールは一時的に無効化。連続3回または合計20回ブロックで一時停止し手動承認に戻る。会話で「push しないで」と言うと分類器が尊重するが、圧縮で失われ得るので確実にするなら deny ルール。`claude auto-mode defaults` で全ルール表示、`/auto-mode-setup` で環境記述を作成 — [permission-modes](https://code.claude.com/docs/en/permission-modes), [commands](https://code.claude.com/docs/en/commands)
- **公式の警告**: auto mode は「reduces permission prompts but does not guarantee safety」。`bypassPermissions` は「offers no protection against prompt injection or unintended actions」で、インターネット遮断のコンテナ/VM 等でのみ使用、root/sudo では起動拒否 — [permission-modes](https://code.claude.com/docs/en/permission-modes)
- **Protected paths / Critical paths**: `.git`, `.vscode`, `.claude`, `.bashrc`, `.mcp.json` 等への書き込みは allow ルールでも事前承認されない。ルート/ホーム/作業ディレクトリ等への `rm` はどのモードでもブロック — [permission-modes](https://code.claude.com/docs/en/permission-modes)
- **確認日**: 2026-10-29

**C-2. Plan mode**
- **概要**: 編集をブロックして読み取り・調査・計画提案のみ行うモード。`Shift+Tab`、`/plan [説明]`、`claude --permission-mode plan` で入る。計画完成時の選択肢「Yes, and use auto mode」「Yes, manually approve edits」「No, keep planning」。`Ctrl+G` で計画をエディタで直接編集。`showClearContextOnPlanAccept` で承認時に計画コンテキストをクリアする選択肢を追加 — [permission-modes](https://code.claude.com/docs/en/permission-modes)
- **公式の推奨**: 手法が不確か・複数ファイル変更・不慣れなコードのときに使う。「diff を1文で説明できるなら計画は飛ばせ」— [Best practices](https://code.claude.com/docs/en/best-practices)
- **確認日**: 2026-10-29

**C-3. Permission rules（allow / ask / deny）**
- **概要**: 評価順は **deny → ask → allow**、最初の一致が勝ち、具体性は順序を変えない。スコープを跨いでも deny が勝つ — [permissions](https://code.claude.com/docs/en/permissions)
- **構文例**: `Bash(npm run *)`（末尾 ` *` で前方一致。スペース無し `Bash(git diff*)` は `git diff-index` にも一致するので注意。`:*` 記法も同等）、`Read(./.env)`、`Edit(...)`、`WebFetch(domain:example.com)`（サブドメインは `*.example.com`）、MCP は `mcp__server__tool`、subagent は `Agent(Explore)`、skill は `Skill(deploy *)` — [permissions](https://code.claude.com/docs/en/permissions), [headless](https://code.claude.com/docs/en/headless), [skills](https://code.claude.com/docs/en/skills)
- **管理**: `/permissions` で閲覧・追加・削除、作業ディレクトリ管理、"Recently denied" 確認。「Yes, and don't ask again」は `.claude/settings.local.json` に allow として保存 — [settings](https://code.claude.com/docs/en/settings), [commands](https://code.claude.com/docs/en/commands)
- **公式の推奨**: 信頼できるツールを `/permissions` で事前許可、sandbox で自由度を上げる。トランスクリプトから読み取り専用コマンドの allowlist 案を作る skill `/fewer-permission-prompts`（CHANGELOG 上は `/less-permission-prompts` として追加）— [Best practices](https://code.claude.com/docs/en/best-practices), [commands](https://code.claude.com/docs/en/commands), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **確認日**: 2026-10-29

**C-4. Sandboxing（Bash サンドボックス）**
- **概要**: Claude が実行するシェルコマンド（Bash/PowerShell/Monitor と子プロセス）に OS レベルのファイルシステム/ネットワーク境界をかける。macOS は Seatbelt、Linux/WSL2 は bubblewrap + socat。ネイティブ Windows は非対応（WSL2 を使う）。ネットワークはローカルプロキシ経由で allowedDomains（初期は空）をチェック。Read/Edit/WebFetch 等の組み込みツール・MCP・hooks はサンドボックス外（permission rules で制御）— [sandboxing](https://code.claude.com/docs/en/sandboxing)
- **モード**: `/sandbox` で auto-allow（サンドボックス内コマンドは無確認実行）か regular permissions を選択。失敗時の非サンドボックス再試行（`dangerouslyDisableSandbox`）は `"allowUnsandboxedCommands": false` で無効化可。`excludedCommands`、資格情報のマスキング（`mask`/`injectHosts`）あり — [sandboxing](https://code.claude.com/docs/en/sandboxing)
- **公式の推奨**: プロンプト疲れを減らしつつ制御を保つ手段として、allowlist と並ぶ二本柱。分類器なしで Bash のプロンプトを減らしたいなら Manual + `/sandbox` auto-allow — [Best practices](https://code.claude.com/docs/en/best-practices), [permission-modes](https://code.claude.com/docs/en/permission-modes)
- **確認日**: 2026-10-29

**C-5. Checkpoints / Rewind**
- **概要**: ターンを開始する各プロンプトの前に Claude の編集対象ファイルをスナップショット。`Esc` 2回（入力欄が空のとき）または `/rewind`（別名 `/checkpoint`, `/undo`）でメニュー: Restore code and conversation / Restore conversation / Restore code / **Summarize from here** / **Summarize up to here**。セッションあたり直近100チェックポイント、約30日で削除（`cleanupPeriodDays`）。セッション再開後も rewind 可。`/clear` 前の会話にも戻れる — [checkpointing](https://code.claude.com/docs/en/checkpointing)
- **制限**: Bash 経由の変更（rm/mv/cp）、外部での変更、多くの subagent の編集は復元されない。git の代替ではない — [checkpointing](https://code.claude.com/docs/en/checkpointing)
- **公式の推奨**: 「リスクのあることを試させ、ダメなら巻き戻す」使い方を推奨 — [Best practices](https://code.claude.com/docs/en/best-practices)
- **確認日**: 2026-10-29

---

#### D. コマンドと Skills

**D-1. Slash commands（組み込みコマンド）**
- **概要**: メッセージ先頭の `/` のみ認識、引数は後続テキスト。最大6個の skill を連結可（`/skill-a /skill-b do XYZ`）。主なもの（2026-10 時点の公式表から抜粋）: `/add-dir`, `/advisor`, `/autocompact`, `/autofix-pr`, `/background`(`/bg`), `/batch`, `/branch`, `/btw`, `/cd`, `/clear`, `/code-review`(`/review`), `/compact`, `/config`, `/context`, `/copy`, `/debug`, `/deep-research`, `/desktop`, `/diff`, `/doctor`, `/effort`, `/export`, `/fast`, `/focus`, `/fork`, `/goal`, `/hooks`, `/ide`, `/import`, `/init`, `/insights`, `/install-github-app`, `/keybindings`, `/list-agents`, `/loop`, `/mcp`, `/memory`, `/model`, `/output-style`, `/permissions`, `/plan`, `/plugin`, `/powerup`, `/recap`, `/release-notes`, `/reload-plugins`, `/reload-skills`, `/remote-control`, `/rename`, `/resume`, `/rewind`, `/run`, `/sandbox`, `/schedule`, `/security-review`, `/simplify`, `/skill-doctor`, `/skills`, `/status`, `/statusline`, `/subtask`, `/tasks`, `/team-onboarding`, `/teleport`(`/tp`), `/terminal-setup`, `/theme`, `/tui`, `/ultrareview`, `/usage`（`/cost`,`/stats` は別名）, `/verify`, `/voice`, `/web-setup`, `/workflows` — [commands](https://code.claude.com/docs/en/commands)
- **教材向けの注目コマンド**: `/btw`（回答が会話履歴に入らないサイド質問）、`/cd`（プロンプトキャッシュを壊さず作業ディレクトリ移動, v2.1.169=2026-06-08 追加）、`/focus`、`/insights`（自分の使い方の HTML レポート）、`/powerup`（アニメーション付き対話レッスン）、`/team-onboarding`（利用履歴からチーム向け立ち上げガイド生成）— [commands](https://code.claude.com/docs/en/commands), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **確認日**: 2026-10-29

**D-2. Skills（SKILL.md、カスタムコマンドを統合）**
- **概要**: `SKILL.md` を含むディレクトリ。Claude が関連時に自動ロード、または `/skill-name` で直接起動。オープン標準 Agent Skills（agentskills.io）準拠＋Claude Code 拡張。**旧 `.claude/commands/` のカスタムコマンドは skills に統合済み**（既存ファイルは動作継続）— [skills](https://code.claude.com/docs/en/skills)
- **配置と優先**: Enterprise（managed）/ Personal `~/.claude/skills/<name>/SKILL.md` / Project `.claude/skills/` / Nested（monorepo サブディレクトリ）/ `--add-dir` / Plugin（`/plugin:skill` 名前空間）/ claude.ai 同期。同名は enterprise > personal > project。編集はライブリロード、新規トップレベルディレクトリは `/reload-skills` — [skills](https://code.claude.com/docs/en/skills)
- **frontmatter**: `name`, `description`（最重要。`when_to_use` と合わせ1,536文字で切り詰め）, `argument-hint`, `arguments`, `disable-model-invocation`（Claude の自動起動を禁止、副作用のある操作向け）, `user-invocable: false`（/メニューから隠し Claude 専用に）, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context: fork`（subagent で実行）, `agent`, `background`, `hooks`, `paths`, `shell` — [skills](https://code.claude.com/docs/en/skills)
- **置換と動的注入**: `$ARGUMENTS`, `$0`/`$1`…, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_SESSION_ID}`。`` !`command` `` で skill 読込前にコマンド出力を埋め込み（permission rules 適用、`disableSkillShellExecution` で無効化可）— [skills](https://code.claude.com/docs/en/skills)
- **Progressive disclosure**: SKILL.md は概要とナビゲーション（**500行未満**）、詳細は `reference.md` 等の補助ファイルに分け必要時に読ませ、`scripts/` は読まずに実行させる。起動後の SKILL.md は会話に残り続け、自動圧縮時は各 skill の先頭5,000トークン（合計25,000トークン枠）が再添付 — [skills](https://code.claude.com/docs/en/skills)
- **公式の作成推奨**: 説明文は具体的に・主用途を先頭に。本文は簡潔に（読み込み後は毎ターンのトークンコスト）。副作用ある操作は `disable-model-invocation: true`。skill 有り/無しを新規セッションで比較評価（`skill-creator` plugin、`claude plugin eval`）。`/skill-doctor` で未使用 skill の常駐コストを洗い出す。`skillOverrides`（`on`/`name-only`/`user-invocable-only`/`off`）で他人の skill を編集せず可視性調整 — [skills](https://code.claude.com/docs/en/skills)
- **バンドル skill**: `/doctor`, `/code-review`(`/review`), `/batch`, `/debug`, `/simplify`, `/loop`, `/verify`（手動専用、アプリを実際に起動して確認）, `/run`, `/run-skill-generator`, `/claude-api`, `/skill-doctor`, `/workflow-authoring` 他。`disableBundledSkills` で一括無効化。`verify` または `simplify` という名前の自作 skill があると、コミット前に Claude がそれを実行する（v2.1.286+）— [skills](https://code.claude.com/docs/en/skills)
- **互換性の注意**: claude.ai アップロード/Skills API は `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` 以外のキーでエラー — [skills](https://code.claude.com/docs/en/skills)
- **確認日**: 2026-10-29

---

#### E. Subagents と並列作業

**E-1. Subagents（サブエージェント）**
- **概要**: 独自の context window・システムプロンプト・ツール権限で動く専門アシスタント。冗長な出力（検索結果、ログ）を本会話から隔離し、要約だけ返す。使用量は本会話と同じ上限にカウント — [sub-agents](https://code.claude.com/docs/en/sub-agents)
- **組み込み subagent**: **Explore**（読み取り専用の高速コードベース探索、thoroughness: quick/medium/very thorough）、**Plan**（plan mode 中の調査）、**general-purpose**（探索と行動の両方）、**claude**（汎用、background sessions の既定）、**statusline-setup**、**claude-code-guide**（Claude Code の機能質問に回答, Haiku）。Explore と Plan は CLAUDE.md と git status を読まない — [sub-agents](https://code.claude.com/docs/en/sub-agents)
- **定義方法**: `.claude/agents/`（プロジェクト）/ `~/.claude/agents/`（ユーザー）の Markdown、`--agents` JSON（セッション限定）、plugin。優先: managed > `--agents` > project > user > plugin。**`/agents` ウィザードは v2.1.198（2026-07-01）で削除**、Claude に作らせるかファイルを直接編集 — [sub-agents](https://code.claude.com/docs/en/sub-agents), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **frontmatter**: 必須は `name`, `description`。他に `tools`, `disallowedTools`, `model`（sonnet/opus/haiku/fable/フルID/inherit）, `permissionMode`, `maxTurns`, `autoCompactWindow`, `skills`（最大32個を全文プリロード）, `mcpServers`, `hooks`, `memory`（user/project/local の永続メモリ）, `background`, `omitClaudeMd`, `effort`, `isolation: worktree`, `color`, `initialPrompt` — [sub-agents](https://code.claude.com/docs/en/sub-agents)
- **起動・並列**: 自然言語（「use the X subagent」）、`@"name (agent)"` で確実に起動、`claude --agent name` でメインスレッド化。description に「use proactively」で自動委任を促す。既定で同時実行20（`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`）、ネスト深さ3（`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`）。対話セッションで Claude が生成する subagent は既定でバックグラウンド。`Ctrl+B` で実行中タスクをバックグラウンド化。`SendMessage` で再開（Explore/Plan は再開不可）— [sub-agents](https://code.claude.com/docs/en/sub-agents)
- **Fork**: 親の会話全体を引き継ぐ subagent。`/subtask <task>` で開始。（`/fork` は現在「会話を新しいバックグラウンドセッションにコピー」の意味）— [agents](https://code.claude.com/docs/en/agents), [commands](https://code.claude.com/docs/en/commands)
- **何を引き継がないか**: 会話履歴、起動済み skill、output style、auto memory は渡らない。subagent 内で守らせたいルールは委任プロンプトで再記述 — [sub-agents](https://code.claude.com/docs/en/sub-agents)
- **公式の推奨**: 大量出力タスク（例「テストを走らせ失敗だけ報告」）に使う。反復的なやり取りや小さな編集は本会話で。description は短く詳細はシステムプロンプトへ。レビュー系は tools を絞る。安価なタスクは `model: haiku`。memory は `project` スコープを既定に — [sub-agents](https://code.claude.com/docs/en/sub-agents)
- **確認日**: 2026-10-29

**E-2. 並列実行の5方式（Run agents in parallel）**
- **概要**: ① Subagents（1セッション内の委任）② **Agent view**（`claude agents` で背景セッションを一画面で投入・監視、research preview）③ **Agent teams**（リード＋チームメイト、共有タスクリストと相互メッセージ、experimental で既定無効）④ **Projects**（claude.ai/code や desktop の継続的会話から Claude が並列 "threads" を起動、Pro/Max 向け public beta）⑤ **Dynamic workflows**（Claude が書く JS スクリプトが多数の subagent を実行・相互検証）。補助として Worktrees、Cross-session messaging、`/batch`（5〜30の worktree 隔離 subagent に分割）— [agents](https://code.claude.com/docs/en/agents)
- **選び方**: 誰が調整するか（Claude が1会話内で→subagents / 自分が渡して後で確認→agent view / Claude が計画・割当・監督→agent teams / スクリプトが計画を保持→workflows）、相互通信が要るか、同じファイルを触るか（触るなら worktree で隔離。agent teams は worktree 隔離しないのでファイル単位で分担）— [agents](https://code.claude.com/docs/en/agents)
- **確認**: 背景セッション→`claude agents`、セッション内の背景作業→`/tasks`、workflows→`/workflows` — [agents](https://code.claude.com/docs/en/agents)
- **確認日**: 2026-10-29

**E-3. Agent view / Background sessions（research preview）**
- **概要**: `claude agents` で全背景セッションを状態別（Working / Needs input / Idle / Completed / Failed / Stopped）に表示。下部入力で新セッション投入、シェルから `claude --bg "..."`。`Space` で覗いて返信、`Enter` でアタッチ、`←` でデタッチ（停止しない）。投入されたセッションは編集前に `.claude/worktrees/` の worktree に移る。`/background` で現会話を背景化、`/fork` でコピー — [agent-view](https://code.claude.com/docs/en/agent-view)
- **公式の推奨**: 見張る必要のない独立タスク複数（バグ修正・PR レビュー・調査）に。削除前にコミット/push。各セッションが個別にクォータを消費するので同時数を制限 — [agent-view](https://code.claude.com/docs/en/agent-view)
- **確認日**: 2026-10-29

**E-4. Agent teams（experimental）**
- **概要**: 複数 Claude Code インスタンスをリードが調整。research preview として v2.1.32（2026-02-05）に追加、`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` で有効化 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [costs](https://code.claude.com/docs/en/costs)
- **公式の推奨（コスト）**: plan mode のチームメイトは通常の約7倍のトークン。チームメイトは Sonnet、チームは小さく、spawn プロンプトは絞り、終わったら停止 — [costs](https://code.claude.com/docs/en/costs)
- **確認日**: 2026-10-29

**E-5. Dynamic workflows（2026年追加）**
- **概要**: Claude が書いた JavaScript スクリプト（`agent()`, `pipeline()`, `parallel()`, `phase()`）をランタイムがバックグラウンド実行し、中間結果はスクリプト変数に保持（本会話には最終結果のみ）。全有料プランで利用可（Pro は `/config` で有効化）。起動は プロンプトに **`ultracode`** キーワード、または「use a workflow」と依頼、または `/effort ultracode` で Claude に判断させる。バンドル workflow は `/deep-research`。`/workflows` で進捗確認・一時停止・保存（`.claude/workflows/` または `~/.claude/workflows/` に保存すると `/<name>` で再実行可）— [workflows](https://code.claude.com/docs/en/workflows)
- **制限**: 同時16エージェント（既定）、1実行1,000エージェント、規模ガイドライン既定 `medium`（10未満、Pro は `small`）。25エージェント超または150万トークン超で「Large workflow」警告 — [workflows](https://code.claude.com/docs/en/workflows)
- **公式の推奨**: 少数の subagent では手に負えない規模（全コードベース監査、500ファイル移行、相互検証付き調査）や結果の相互検証が欲しい時に。大規模実行の前に小さな範囲で試してコスト感を掴む — [workflows](https://code.claude.com/docs/en/workflows)
- **確認日**: 2026-10-29

**E-6. Git worktrees と並列セッション**
- **概要**: `claude --worktree <name>`（`-w`）で `.claude/worktrees/<name>/` に `worktree-<name>` ブランチを作り隔離セッション開始。`"#1234"` や PR/MR URL で PR から作成可。`.worktreeinclude`（.gitignore 構文）で `.env` 等の gitignore ファイルをコピー。`worktree.baseRef` は `fresh`（既定: リモート既定ブランチから）/`head`。終了時、変更なしなら自動削除、変更ありなら保持/削除を確認。subagent は `isolation: worktree`。非 git VCS は `WorktreeCreate`/`WorktreeRemove` hook — [worktrees](https://code.claude.com/docs/en/worktrees)
- **公式の推奨**: `.claude/worktrees/` を .gitignore に追加。worktree は新規チェックアウトなので依存インストール等の環境初期化が必要 — [worktrees](https://code.claude.com/docs/en/worktrees)
- **確認日**: 2026-10-29

**E-7. Cross-session messaging**
- **概要**: Claude が自分の他の Claude Code セッション（同一マシン・別マシン・クラウド）を一覧しメッセージを送る（`SendMessage`/`ListAgents`、`/list-agents`=`/peers`）。受信の可否は `crossSessionInbound`（accept/hold/refuse）— [agents](https://code.claude.com/docs/en/agents), [commands](https://code.claude.com/docs/en/commands), [costs](https://code.claude.com/docs/en/costs)
- **確認日**: 2026-10-29

---

#### F. Hooks（決定的自動化）

**F-1. Hooks**
- **概要**: ライフサイクルイベントで shell コマンド等を必ず実行する仕組み。CLAUDE.md が「助言」なのに対し hooks は「決定的」— [Best practices](https://code.claude.com/docs/en/best-practices)
- **イベント（33種）**: `SessionStart`, `Setup`, `UserPromptSubmit`, `UserPromptExpansion`, `PreToolUse`, `PermissionRequest`, `PermissionDenied`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Notification`, `MessageDisplay`, `SubagentStart`, `SubagentStop`, `TaskCreated`, `TaskCompleted`, `Stop`, `StopFailure`, `TeammateIdle`, `InstructionsLoaded`, `ConfigChange`, `CwdChanged`, `DirectoryAdded`, `FileChanged`, `WorktreeCreate`, `WorktreeRemove`, `PreCompact`, `PostCompact`, `PreModelSwitch`, `PostModelSwitch`, `Elicitation`, `ElicitationResult`, `SessionEnd` — [hooks](https://code.claude.com/docs/en/hooks)
- **ハンドラ種別**: `command`（stdin に JSON）/ `http`（POST）/ `mcp_tool` / `prompt`（単発 LLM 判定）/ `agent`（ツールを使える subagent で検証, experimental）— [hooks](https://code.claude.com/docs/en/hooks)
- **設定場所**: user / project / local settings、managed、plugin の `hooks/hooks.json`、skill frontmatter、subagent frontmatter。全て**マージ**される。`/hooks` で閲覧 — [hooks](https://code.claude.com/docs/en/hooks), [Best practices](https://code.claude.com/docs/en/best-practices)
- **matcher と終了コード**: matcher は完全一致・`|` 区切り・その他は JS 正規表現。MCP ツールは `mcp__server__.*`。`if` フィールドに permission rule 構文（例 `Bash(rm *)`）。exit 0=成功（JSON なら解釈）、**exit 2=ブロック（stderr が理由として Claude に渡る）**、その他=非ブロッキングエラー。JSON 出力で `permissionDecision`（allow/deny/ask/defer）、`updatedInput`、`additionalContext`、`decision: "block"` 等 — [hooks](https://code.claude.com/docs/en/hooks)
- **代表的用途（公式例）**: 編集後に eslint/formatter、migrations フォルダへの書き込みブロック、テスト出力をフィルタして失敗行だけ返す PreToolUse（トークン削減）、Stop hook で検証が通るまでターン終了を阻止、セッション終了時に Slack 通知 — [Best practices](https://code.claude.com/docs/en/best-practices), [costs](https://code.claude.com/docs/en/costs), [features-overview](https://code.claude.com/docs/en/features-overview)
- **公式の推奨/警告**: 「Claude にフックを書かせる」（例「Write a hook that runs eslint after every file edit」）。hooks はユーザー権限で任意コード実行するので plugin/リポジトリ由来は確認。既定は fail-open なのでポリシー用途は `onFailure: "block"`（v2.1.295+）。シェル展開事故防止に `args`（exec 形式）を推奨 — [Best practices](https://code.claude.com/docs/en/best-practices), [hooks](https://code.claude.com/docs/en/hooks)
- **確認日**: 2026-10-29

---

#### G. MCP

**G-1. MCP servers**
- **概要**: 外部サービス（Notion、Figma、DB、Sentry 等）をツールとして接続するプロトコル。transport は **HTTP（推奨）**、stdio（ローカルプロセス）、WebSocket、**SSE は非推奨**（v2.1.265+ は HTTP を先に試行）— [mcp](https://code.claude.com/docs/en/mcp)
- **追加**: `claude mcp add --transport http notion https://mcp.notion.com/mcp`、stdio は `claude mcp add --env KEY=... --transport stdio name -- npx -y pkg`、`claude mcp add-json`。管理は `claude mcp list/get/remove/login/logout`、セッション内 `/mcp`（OAuth 認証、`/mcp reconnect all`）— [mcp](https://code.claude.com/docs/en/mcp), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **スコープ**: local（既定・`~/.claude.json` のプロジェクト下）/ project（`.mcp.json` をコミット共有、初回承認あり）/ user（`~/.claude.json`）。同名時の優先: managed `managedMcpServers` > local > project > user > plugin > claude.ai connectors — [mcp](https://code.claude.com/docs/en/mcp)
- **コンテキスト**: tool search が既定 ON でツール定義は遅延ロード（名前とサーバー指示のみ常駐）。出力は10,000トークンで警告、既定上限25,000（`MAX_MCP_OUTPUT_TOKENS`）。`/context all` でツール毎のトークン確認 — [mcp](https://code.claude.com/docs/en/mcp), [features-overview](https://code.claude.com/docs/en/features-overview)
- **Resources / Prompts**: `@server:resource`（例 `@github:repos/owner/repo/issues`）で MCP リソースを参照。MCP prompts は `/mcp__server__prompt` 形式のコマンドとして使える — [common-workflows](https://code.claude.com/docs/en/common-workflows), [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)
- **公式の推奨/警告**: 信頼できるサーバーだけ接続（外部コンテンツ取得はプロンプトインジェクションの危険）、DB は読み取り専用資格情報。`gh`/`aws`/`gcloud` 等の CLI がある場合は MCP より CLI の方がコンテキスト効率が良い。使っていないサーバーは無効化。MCP（接続）＋ skill（使い方の知識）の組み合わせを推奨 — [mcp](https://code.claude.com/docs/en/mcp), [costs](https://code.claude.com/docs/en/costs), [features-overview](https://code.claude.com/docs/en/features-overview)
- **Channels**: `claude/channel` 機能を宣言したサーバーが CI 結果やアラートをセッションへ push（`--channels` で opt-in）— [mcp](https://code.claude.com/docs/en/mcp), [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)
- **確認日**: 2026-10-29

---

#### H. Plugins / Marketplaces / Mods

**H-1. Plugins と marketplaces**
- **概要**: skills、agents、hooks、MCP servers、hooks module（Mods）、LSP、output styles 等を1単位で導入する配布形式。manifest は `.claude-plugin/plugin.json`。plugin の skill は `/plugin-name:skill` で名前空間化。marketplace は `.claude-plugin/marketplace.json` を持つカタログ（ストアではない）。公式 marketplace `claude-plugins-official` は初回の対話起動時に自動追加。`/plugin` の Discover タブから導入、`claude plugin` CLI、開発時は `--plugin-dir` — [plugins overview](https://code.claude.com/docs/en/plugins/overview)
- **インストールスコープ**: user / project（`.claude/settings.json` 経由でチーム共有。各自のマシンで要インストール）/ local。クラウドセッションはローカル設定の plugin を読まない — [plugins overview](https://code.claude.com/docs/en/plugins/overview)
- **コストと安全**: 有効な plugin の skill/agent の名前と説明は毎ターン常駐し、使わないセッションでもトークンを消費。公式 marketplace では "Context cost" 推定を表示、Installed タブの "Not used recently" で無効化候補。plugin はユーザー権限でコードを実行するので導入前に確認。公式/コミュニティ名は `github.com/anthropics/` 由来のみ受け付け — [plugins overview](https://code.claude.com/docs/en/plugins/overview)
- **Code intelligence plugins**: LSP ツールは言語別 plugin を入れると有効化。定義ジャンプ・参照検索・編集後の型エラー自動報告でファイル読み込みを減らす（型付き言語では導入推奨）— [features-overview](https://code.claude.com/docs/en/features-overview), [costs](https://code.claude.com/docs/en/costs), [Best practices](https://code.claude.com/docs/en/best-practices)
- **Claude Mods（2026-10 追加）**: v2.1.287（2026-10-01）で「plugins may now modify deeper behavior」。hooks を JavaScript 関数で書き、ペイン描画やコマンド追加もできる hooks module を持つ plugin を mod と呼ぶ — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [plugins overview](https://code.claude.com/docs/en/plugins/overview)
- **確認日**: 2026-10-29

---

#### I. 表示・出力のカスタマイズ

**I-1. Output styles**
- **概要**: セッション全体の役割・トーン・応答形式を変える指示。組み込みは Default と **Proactive**（確認せず進める）/ **Concise**（結果先行、v2.1.237+）/ **Explanatory**（`★ Insight` ブロックで理由を説明）/ **Learning**（`TODO(human)` で一部をユーザーに書かせる）の4種。`/output-style <name>`（v2.1.269+）、`/config`、`outputStyle` 設定（大文字小文字区別）— [output-styles](https://code.claude.com/docs/en/output-styles)
- **カスタム**: `~/.claude/output-styles/` / `.claude/output-styles/` の Markdown。`keep-coding-instructions: true` で組み込みのソフトウェア開発指示を保持（省略時は外れる）— [output-styles](https://code.claude.com/docs/en/output-styles)
- **公式の推奨**: 「何を知るべきか」は CLAUDE.md、「どう答えるか」は output style、必ず起きるべきことは hook。大きな役割変更以外は組み込みスタイルから始める — [output-styles](https://code.claude.com/docs/en/output-styles), [Steering blog](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)
- **経緯**: 2025-11 に一度非推奨→コミュニティの声で非推奨撤回（v2.0.32）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **確認日**: 2026-10-29

**I-2. Status line**
- **概要**: 画面下部に任意のシェルスクリプト出力を表示。stdin で JSON（`model.display_name`, `workspace.current_dir`, `cost.total_cost_usd`, `context_window.used_percentage`, `rate_limits.five_hour.used_percentage`, `session_id` 等）を受け取る。`/statusline` で説明から自動設定（シェルプロンプトから自動生成も可）— [statusline](https://code.claude.com/docs/en/statusline)
- **公式の推奨**: コンテキスト使用量を常時追跡するために使う — [Best practices](https://code.claude.com/docs/en/best-practices)
- **確認日**: 2026-10-29

**I-3. TUI / テーマ / その他表示**
- **概要**: `/tui fullscreen` でちらつきの無い全画面レンダラ、`/theme`、`/color`（プロンプトバー色）、`/focus`（最後のプロンプトと要約だけ表示）、`Ctrl+O` でトランスクリプトビューア — [commands](https://code.claude.com/docs/en/commands), [interactive-mode](https://code.claude.com/docs/en/interactive-mode)
- **確認日**: 2026-10-29

---

#### J. 非対話モード・CI・SDK

**J-1. Headless / non-interactive（`claude -p`）**
- **概要**: `claude -p "prompt"` で非対話実行（Agent SDK の CLI 形態）。`--output-format text|json|stream-json`（json は `result`, `session_id`, `total_cost_usd` 等、stream-json は `--verbose` 併用、`--include-partial-messages` でトークン逐次）。`--json-schema` で `structured_output` に構造化出力。stdin パイプ可（上限10MB）。`--continue` / `--resume <id>` で継続。`--allowedTools`、`--permission-mode`、`--permission-prompts none`（無人実行で確認待ちを全拒否, v2.1.259+）、`--max-budget-usd`、`--append-system-prompt`、`--no-session-persistence` — [headless](https://code.claude.com/docs/en/headless), [Best practices](https://code.claude.com/docs/en/best-practices)
- **`--bare`**: hooks・skills・plugins・MCP・auto memory・CLAUDE.md の自動検出をスキップし、マシン差の無い再現性を得る。**スクリプト/SDK 呼び出しの推奨モードで、将来 `-p` の既定になる予定**。`ANTHROPIC_API_KEY` が必要（サブスクリプションの OAuth は使わない）— [headless](https://code.claude.com/docs/en/headless)
- **注意**: `--bare` 無しの `-p` は未信頼フォルダでも `.claude/settings.json` の hooks と `.mcp.json` のサーバーを実行する（信頼ダイアログが出ない）— [headless](https://code.claude.com/docs/en/headless)
- **`-p` で使えるコマンド**: ユーザー起動 skill（`/skill-name`）は展開される。`/model sonnet`、`/config key=value`、`/output-style` 等は引数形式で可。`/login` 等 TUI 専用は不可 — [headless](https://code.claude.com/docs/en/headless)
- **確認日**: 2026-10-29

**J-2. GitHub Actions / CI**
- **概要**: `anthropics/claude-code-action@v1`。`/install-github-app` で GitHub App・secret・workflow PR を自動準備（github.com のみ）。`prompt` 無し=interactive mode（`@claude` メンションに応答）、`prompt` 有り=automation mode（任意イベント・cron）。skill 起動（`/skill-name`）や plugin 導入（`plugin_marketplaces`, `plugins`）も可。CLI 引数は `claude_args`（`--max-turns`, `--model`, `--allowedTools`, `--mcp-config`）。認証は `ANTHROPIC_API_KEY`、`CLAUDE_CODE_OAUTH_TOKEN`（`claude setup-token`）、または workload identity federation。Bedrock/Vertex/Foundry 対応。GitLab CI/CD 版もあり — [github-actions](https://code.claude.com/docs/en/github-actions)
- **公式の推奨**: リポジトリ直下 CLAUDE.md にレビュー基準等を定義、鍵は必ず Secrets、最小権限、マージ前に人がレビュー、`--max-turns`・workflow timeout・concurrency でコスト制御、CLAUDE.md は毎回読まれるので簡潔に。`@beta` からは `@v1` へ移行（`mode` 削除、`direct_prompt`→`prompt`、CLI オプションは `claude_args` へ）— [github-actions](https://code.claude.com/docs/en/github-actions)
- **関連製品**: マネージドな自動 PR レビュー **Code Review**、クラウドでの多エージェントレビュー **`/ultrareview`**、`/security-review`、`/code-review`（`--comment` で PR にインラインコメント）— [github-actions](https://code.claude.com/docs/en/github-actions), [commands](https://code.claude.com/docs/en/commands)
- **確認日**: 2026-10-29

**J-3. Agent SDK**
- **概要**: Claude Code と同じツール・エージェントループ・コンテキスト管理を Python / TypeScript パッケージおよび CLI（`claude -p`）として提供。GitHub Action も SDK 上に構築 — [headless](https://code.claude.com/docs/en/headless), [github-actions](https://code.claude.com/docs/en/github-actions)
- **確認日**: 2026-10-29

---

#### K. コンテキスト管理

**K-1. `/clear`, `/compact`, 自動圧縮, `/context`, `/btw`**
- **概要**: `/clear`=空のコンテキストで新会話（名前を付けて `/resume` で戻れる）。`/compact [指示]`=要約して空きを作る。自動圧縮は上限接近時に古いツール出力を消し、必要なら会話を要約。`/autocompact` で圧縮ウィンドウ設定。`/context`=使用量をカラーグリッドで可視化。`/btw`=回答が履歴に入らないサイド質問。rewind の「Summarize from here / up to here」で部分圧縮 — [commands](https://code.claude.com/docs/en/commands), [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works), [Best practices](https://code.claude.com/docs/en/best-practices)
- **公式の推奨**: 無関係なタスクの間で頻繁に `/clear`。CLAUDE.md に「When compacting, always preserve the full list of modified files and any test commands」等の "Compact Instructions" を書く。永続ルールは会話でなく CLAUDE.md に。巨大ファイルで圧縮が繰り返す "thrashing" は自動停止しエラー表示 — [Best practices](https://code.claude.com/docs/en/best-practices), [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)
- **確認日**: 2026-10-29

**K-2. Prompt caching の意識**
- **概要**: モデル切替は別キャッシュなので切替後の初回は会話全体を非キャッシュで再読込。output style 切替もキャッシュに影響。`/usage` に `Prompt cache (main)` 行（ヒット率・ミス・warm/cold）。長い休憩後の初回はキャッシュ切れで全コンテキスト再処理 — [settings](https://code.claude.com/docs/en/settings), [costs](https://code.claude.com/docs/en/costs), [output-styles](https://code.claude.com/docs/en/output-styles)
- **確認日**: 2026-10-29

---

#### L. モデル・effort・thinking

**L-1. モデル選択**
- **概要（Anthropic API での現行エイリアス）**: `default`（Pro/Max/Team/Enterprise/API では **Opus 5.5**）、`best`（Fable、無ければ Opus）、`fable`=Fable 5.1、`opus`=Opus 5.5、`sonnet`=Sonnet 5.5、`haiku`=Haiku 5.5、`opus[1m]`/`sonnet[1m]`、`opusplan`（plan mode は Opus、実行は Sonnet）。優先: `/model` > `--model` > `ANTHROPIC_MODEL` > settings `model` > `ANTHROPIC_DEFAULT_MODEL`。`/model` の picker で `s` を押すと保存せず切替。`--fallback-model` で過負荷時の代替（最大3）— [model-config](https://code.claude.com/docs/en/model-config)
- **2026年のモデル追加（CHANGELOG）**: Fable 5.1 が既定 Fable に（v2.1.257, 2026-09-01）、Sonnet 5.5 が既定 Sonnet に（v2.1.284, 2026-09-28、1M context）、Haiku 5.5 が既定 Haiku に（v2.1.293, 2026-10-07、1M context）、Opus 5.5 が既定 Opus に（1M context） — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **公式の推奨**: Fable 5.1=最難関・長時間タスク（曖昧な根本原因調査、障害デバッグ、設計判断）で、手順でなく成果を記述し検証リマインダは省く。Opus=複雑な推論、Sonnet=日常のコーディング、Haiku=簡単なタスク — [model-config](https://code.claude.com/docs/en/model-config)
- **確認日**: 2026-10-29

**L-2. Effort と extended thinking**
- **概要**: effort は `low`/`medium`/`high`/`xhigh`/`max`。既定は多くのモデルで `high`、**Opus 5.5 / Sonnet 5.5 / Haiku 5.5 は `medium`**。`/effort`（スライダー、`/effort high`、`/effort auto`）、`--effort`、`CLAUDE_CODE_EFFORT_LEVEL`、`effortLevel` 設定、skill/subagent の `effort` frontmatter。**Ultracode** は effort レベルではなく workflow 自動化の別設定（`/effort ultracode`）— [model-config](https://code.claude.com/docs/en/model-config)
- **Thinking**: `Option+T`/`Alt+T` でセッション内切替、`alwaysThinkingEnabled`。Opus 5.5/Sonnet 5.5/Haiku 5.5/Fable は thinking を無効化できない。**`ultrathink` はそのターンだけ深い推論を要求するキーワードとして現在も有効。「think hard」等のフレーズは認識されない** — [model-config](https://code.claude.com/docs/en/model-config), [interactive-mode](https://code.claude.com/docs/en/interactive-mode)
- **公式の推奨（effort）**: low=すぐ確認する短いやり取り、medium=範囲の明確な日常作業、high=バグ修正など検証が重要な作業、xhigh=より深い推論、max=難問だが過剰思考や逓減もあるので試してから採用。Opus 5 → 5.5 移行時は以前のレベルを持ち越さず `medium` から — [model-config](https://code.claude.com/docs/en/model-config)
- **Fast mode / Advisor**: `/fast`（`Option+O`/`Alt+O`）で高速モード、`/advisor` で重要局面に第2モデルの助言を受ける — [commands](https://code.claude.com/docs/en/commands), [interactive-mode](https://code.claude.com/docs/en/interactive-mode)
- **確認日**: 2026-10-29

---

#### M. コスト・使用量

**M-1. `/usage` と分析**
- **概要**: `/usage`（`/cost`, `/stats` は別名）でセッションコスト（API 利用者向けの推定値）、プラン使用量バー、利用内訳（skills/subagents/plugins/MCP 毎の比率）、推奨事項（`f` で自動適用, v2.1.305+）、`/loop` 毎のトークン。`/insights` は直近セッションを分析して作業傾向・摩擦点・改善提案の HTML レポート — [costs](https://code.claude.com/docs/en/costs)
- **公式データ**: 企業導入の平均は**アクティブ日あたり約$13/開発者、月$150〜250/開発者**、90%のユーザーは日$30未満 — [costs](https://code.claude.com/docs/en/costs)
- **公式のトークン削減策**: タスク間で `/clear`（その前に `/rename`）、カスタム圧縮指示、Sonnet を基本に Opus は複雑な設計判断へ、subagent に `model: haiku`、MCP より CLI、未使用 MCP 無効化、code intelligence plugin、hooks で前処理（ログを grep して返す）、CLAUDE.md の専門手順を skills へ（200行未満）、effort を下げる、冗長な処理を subagent へ、具体的なプロンプト、plan mode・早期の軌道修正・検証目標・段階的テスト — [costs](https://code.claude.com/docs/en/costs)
- **長時間セッションで使用量が増える理由**: 長いコンテキストの再送、キャッシュミス、`/loop`、cross-session メッセージ、`/goal` チェックイン、subagents/workflows、agent teams、圧縮自体のコスト — [costs](https://code.claude.com/docs/en/costs)
- **組織向け**: Team/Enterprise は分析ダッシュボードと spend limit、Console はワークスペース上限と Analytics API、クラウドプロバイダは OpenTelemetry 等。チーム規模別 TPM/RPM 推奨表あり — [costs](https://code.claude.com/docs/en/costs)
- **確認日**: 2026-10-29

---

#### N. 入力・操作のコツ（Interactive mode）

**N-1. キーボードショートカットと入力プレフィックス**
- **概要**: `Esc`=中断（作業は保持）/ `Esc`+`Esc`=入力クリア or rewind / `Shift+Tab`=権限モード切替 / `Ctrl+C`=中断・入力クリア / `Ctrl+D`=終了 / `Ctrl+G`=外部エディタで編集 / `Ctrl+O`=トランスクリプト / `Ctrl+R`=履歴逆検索 / `Ctrl+V`（iTerm2 は `Cmd+V`、Windows/WSL は `Alt+V`）=画像貼り付け（`[Image #N]`）/ `Ctrl+B`=実行中タスクを背景化 / `Ctrl+T`=Claude の To-do 表示 / `Ctrl+S`=入力の退避・復元 / `Ctrl+Enter`=キュー中メッセージを即送信 / `Option+P`=モデル切替 / `Option+T`=thinking 切替 / `Option+O`=fast mode / `?`=ショートカット一覧 — [interactive-mode](https://code.claude.com/docs/en/interactive-mode)
- **プレフィックス**: `/`=コマンド・skill、`!`=シェルモード（直接実行し出力をセッションに追加）、`@`=ファイルパス補完・参照（ディレクトリは一覧のみ、該当ディレクトリの CLAUDE.md も読み込まれる、MCP リソースも `@server:resource`）。**`#` メモリショートカットは v2.0.70（2025-12-15）で削除済み**（Claude に CLAUDE.md を編集するよう頼む）— [interactive-mode](https://code.claude.com/docs/en/interactive-mode), [common-workflows](https://code.claude.com/docs/en/common-workflows), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **その他**: Vim モード（`/config` → Editor mode。`/vim` コマンドは v2.1.92 で削除）、`/terminal-setup` で Shift+Enter 改行、音声入力 `/voice`（既定 space の push-to-talk）、プロンプト候補表示、`/diff` で変更レビュー、使用上限リセット後に自動継続、PR ステータス表示 — [interactive-mode](https://code.claude.com/docs/en/interactive-mode), [commands](https://code.claude.com/docs/en/commands), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **`@` 参照の注意**: `@` 参照はツール呼び出しを伴わないため PreToolUse hook が走らない。読ませたくないパスは `Read` deny ルールで — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **確認日**: 2026-10-29

**N-2. セッションの再開・分岐**
- **概要**: 会話は `~/.claude/projects/` に JSONL で保存。`claude --continue`（直近）、`claude --resume`（一覧）、`/resume`、`--fork-session` / `/branch`（新 ID に分岐、旧 `/fork` は v2.1.77 で `/branch` に改名）、`/rename` で命名、`claude --from-pr 1234` で PR に紐づくセッション、`/export` で書き出し — [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works), [common-workflows](https://code.claude.com/docs/en/common-workflows), [commands](https://code.claude.com/docs/en/commands), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **公式の推奨**: セッションに `oauth-migration` のような名前を付け、ブランチのように扱う — [Best practices](https://code.claude.com/docs/en/best-practices)
- **確認日**: 2026-10-29

---

#### O. 長時間・自律実行と定期実行

**O-1. `/goal`（2026-05 追加）**
- **概要**: 完了条件を設定すると、各ターン後に別の小型高速モデル（evaluator）が条件達成を判定し、未達なら Claude が次ターンを自動開始。達成・不可能判定・要修正エラーで解除。`/goal`（状態表示）、`/goal clear`。`-p` でも動作。v2.1.139（2026-05-11）追加 — [goal](https://code.claude.com/docs/en/goal), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **公式の推奨**: evaluator はコマンドを実行せず会話に出た証拠だけで判定するので、「`npm test` が exit 0」のように Claude の出力で示せる単一の測定可能な終了状態＋確認方法＋制約を書く。上限は「or stop after 20 turns」のように条件に含める。無人化には auto mode と併用 — [goal](https://code.claude.com/docs/en/goal)
- **確認日**: 2026-10-29

**O-2. `/loop` と CLI 内スケジュール**
- **概要**: `/loop 5m <prompt>`（固定間隔）、`/loop <prompt>`（Claude が1分〜1時間で間隔を自己調整）、`/loop`（組み込みメンテナンスプロンプト or `.claude/loop.md`）。セッションスコープで、閉じると停止。定期タスクは**7日で失効**、1セッション最大50タスク、`CronCreate/CronList/CronDelete` ツール、自然言語で「3pm にリマインド」も可 — [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)
- **3方式比較**: Cloud scheduled tasks（旧 routines, マシン不要, 最小1時間）/ Desktop scheduled tasks（自機, 最小1分, ローカルファイル可）/ `/loop`（開いているセッション内）— [scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)
- **公式の推奨**: 定期タスクのプロンプトは自律実行で質問できないので、成功の定義と結果の扱いを明示する — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **確認日**: 2026-10-29

**O-3. Cloud scheduled tasks（旧名 Routines, research preview）**
- **概要**: プロンプト＋リポジトリ＋コネクタを保存し、Schedule / API（HTTP POST）/ GitHub イベントのトリガーでクラウド実行。Pro/Max/Team/Enterprise。claude.ai/code/routines または CLI の `/schedule`（`/schedule daily PR review at 9am`、`/schedule list/update/run`）— [routines](https://code.claude.com/docs/en/routines)
- **確認日**: 2026-10-29

---

#### P. サーフェス（Web / Desktop / Mobile / IDE / Remote）

**P-1. Claude Code in the cloud（claude.ai/code）**
- **概要**: Anthropic 管理 VM（または self-hosted 環境）でセッションを実行し、ラップトップを閉じても継続。ブラウザ、モバイルアプリの Code タブ、Desktop、`claude --cloud "task"`（`--remote` は非推奨エイリアス）から開始。クラウド環境でネットワークアクセス・環境変数・setup script を設定。`claude --teleport` / `/teleport` でクラウドセッションをローカル端末に取り込み（逆方向は CLI からは不可）。`claude -p "msg" --cloud <id>` で追い指示。PR の **Auto-fix**（CI 失敗とレビューコメントに自動対応、`/autofix-pr`）— [claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web)
- **公式の推奨**: 複雑なタスクはローカルの plan mode で計画→計画ファイルをコミット・push→`claude --cloud "Execute the migration plan in docs/migration-plan.md"`。独立タスクは複数の `--cloud` で並列 — [claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web)
- **注意**: 利用は Pro/Max/Team と Enterprise の premium seat 等。使用量は通常の上限を共有。クラウドセッションは user 設定・local 設定・ローカル plugin を読まない — [claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web), [settings](https://code.claude.com/docs/en/settings)
- **確認日**: 2026-10-29

**P-2. Remote Control**
- **概要**: 自機で動くローカルセッションを claude.ai/code や iOS/Android アプリから操作（実行・ファイルは自機に留まる）。`claude remote-control`（サーバーモード）、`claude --remote-control`/`--rc`（通常の対話セッション＋遠隔操作）、セッション内 `/remote-control`、`remoteControlAtStartup` で常時接続。QR コードでスマホ接続 — [remote-control](https://code.claude.com/docs/en/remote-control)
- **確認日**: 2026-10-29

**P-3. Desktop / Mobile / IDE / Slack / Chrome**
- **概要**: ドキュメントには desktop（macOS/Windows、Linux、WSL、Desktop scheduled tasks、iOS Simulator）、mobile、VS Code、JetBrains、Slack、Claude Tag、Claude in Chrome、computer use の各ページが存在 — [docs map](https://code.claude.com/docs/en/claude_code_docs_map.md)
- **補足**: Desktop は並列セッションを視覚的に管理（worktree オプションあり）、`/desktop` で現セッションを Desktop に移す。Claude in Chrome（v2.0.72 で Beta 追加）でブラウザ操作・スクショ比較による UI 検証 — [Best practices](https://code.claude.com/docs/en/best-practices), [commands](https://code.claude.com/docs/en/commands), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **確認日**: 2026-10-29

**P-4. Artifacts**
- **概要**: セッションの出力を非公開のインタラクティブ Web ページとして公開（例: 調査に合わせて更新されるインシデントタイムライン）。`/artifacts` で一覧 — [features-overview](https://code.claude.com/docs/en/features-overview), [commands](https://code.claude.com/docs/en/commands)
- **確認日**: 2026-10-29

### Inferences
- 教材の章立ては公式 docs の構造（Core concepts → Use → 拡張機能 → 並列 → 自動化 → プラットフォーム）と、公式の「段階的に足すトリガー表」に沿うと、利用者の「次に何を学ぶべきか」と一致しやすい。
- 「CLAUDE.md・skill・output style は *指示* であり強制力が無い／hooks・permissions・sandbox・managed settings が *強制*」という二分法が、公式全体で繰り返される最重要の概念区別。辞書の各項目に「強制力: あり/なし」の属性を付けると誤用を防げる。
- 2026年に追加された機能の多く（agent view、agent teams、cloud scheduled tasks、projects、workflows の一部）は research preview / experimental / public beta 表記であり、UI・名称が変わりやすい。辞書では「成熟度」欄を設け、確認日とバージョンを必ず併記するのが安全。
- 機能の追加頻度は非常に高く（2026年1月の v2.0.77 から10月末の v2.1.312 まで約235リリース。npm 公開日から算出）、静的な辞書は数か月で陳腐化する前提で更新運用を設計すべき。

### Gaps
- VS Code / JetBrains / Desktop / Mobile / Slack / Claude in Chrome / computer use の個別ページは本調査で本文未取得（docs map 上の存在のみ確認）。IDE 固有機能（diff 表示、選択範囲共有等）の詳細は未確認。
- Agent teams、Artifacts、Code Review（マネージド製品）、Channels、Fast mode、Advisor、Agent SDK overview の各専用ページは未取得で、他ページ・CHANGELOG からの二次的記述に留まる。
- MCP ページはツール出力が途中で切れ、`claude mcp serve`（Claude Code を MCP サーバーとして使う機能）、resources/prompts の詳細節、managed MCP の詳細は未確認。
- Hooks リファレンスはイベント別詳細スキーマの途中で切れている（イベント一覧・終了コード・JSON フィールドは取得済み）。
- Opus 5.5 / Opus 5 が既定化された正確なバージョン番号は CHANGELOG の行は確認したが版番号との対応は未特定。
- `/simplify` は v2.1.147（2026-05-21）で `/code-review` に改名されたと CHANGELOG にあるが、現行 commands ページには再び `/simplify`（4つのレビューエージェントでクリーンアップと修正を適用する skill）が `/code-review` とは別に掲載されている。再追加の時期は未確認。
- `/less-permission-prompts`（CHANGELOG 表記）と `/fewer-permission-prompts`（現行 commands ページ表記）の改名時期は未確認。

---

## Key Question 2: Anthropic 公式のベストプラクティス記事は何を推奨しているか

### Takeaway
公式推奨の中核は ①Claude が自分で実行できる検証手段（テスト・ビルド・スクリーンショット）を渡す ②Explore → Plan → Implement → Commit で調査と実装を分ける ③具体的なファイル・制約・既存パターンを指示する ④コンテキストを積極管理（/clear、subagent に調査させる、2回訂正して駄目ならやり直す）⑤非対話モード・並列セッション・Writer/Reviewer・fan-out でスケールする、の5点。2025年の engineering ブログ記事は現在 docs の Best practices に統合・更新されており、context engineering・tool 設計の記事が理論的裏付けを与えている。

### Cited Findings

#### 2-1. 「Best practices for Claude Code」（公式 docs, 旧 engineering ブログ記事の後継）
- **出典の状態**: 旧 URL anthropic.com/engineering/claude-code-best-practices は docs の Best practices に 302 リダイレクト（2026-10-29 確認）— [Best practices](https://code.claude.com/docs/en/best-practices)
- **大前提**: 「Claude's context window fills up fast, and performance degrades as it fills」— [Best practices](https://code.claude.com/docs/en/best-practices)
- **検証手段を渡す（最優先）**: 「Give Claude a check it can run: tests, a build, a screenshot to compare. It's the difference between a session you watch and one you walk away from.」例: 「validateEmail を書き、テストケース X/Y/Z、実装後にテストを実行」「スクショを貼り、結果のスクショと比較して差分を列挙し修正」「エラーを貼り、根本原因を直し、エラーを抑制しない」。ゲートの強さを段階的に上げる: 1プロンプト内で指示 → `/goal` 条件 → Stop hook（決定的）→ 検証用 subagent / workflow（別モデルに反証させる）。成功を主張させず証拠（テスト出力、実行コマンド、スクショ）を示させる。`/verify` で実アプリ確認 — [Best practices](https://code.claude.com/docs/en/best-practices)
- **Explore → Plan → Implement → Commit**: plan mode で `/src/auth を読んで理解して` → `Google OAuth を追加したい。変更ファイルとセッションフローは? 計画を作って`（`Ctrl+G` で計画を直接編集）→ plan mode を抜けて実装＋テスト → コミットと PR 作成。ただし diff を1文で説明できる小さな変更は直接やらせる — [Best practices](https://code.claude.com/docs/en/best-practices)
- **具体的に指示する**: タスクのスコープ（どのファイル・どのシナリオ・モック回避等）、情報源を指す（「git 履歴を見て API の経緯を要約」）、既存パターンを参照（「HotDogWidget.php を手本に」）、症状・場所・"直った"の定義を述べる（「失敗するテストを書いて再現してから直す」= TDD 的）。探索段階では曖昧な質問も有用 — [Best practices](https://code.claude.com/docs/en/best-practices)
- **リッチな入力**: `@` でファイル参照、画像の貼り付け/ドラッグ、URL（よく使うドメインは `/permissions` で許可）、`cat error.log | claude -p` でパイプ、Claude 自身に取りに行かせる — [Best practices](https://code.claude.com/docs/en/best-practices)
- **環境設定**: CLAUDE.md を `/init` で作り育てる（含める/除外表、各行の削除テスト、IMPORTANT は1行だけ）、`/permissions` と `/sandbox`、CLI ツール（`gh` 等。未知の CLI は `--help` で学ばせる）、MCP、hooks（「必ず毎回」用）、skills（`disable-model-invocation: true` で副作用ワークフロー）、custom subagents、plugins（型付き言語は code intelligence plugin）— [Best practices](https://code.claude.com/docs/en/best-practices)
- **コミュニケーション**: シニアエンジニアに聞くようにコードベースの質問をする（オンボーディングに有効）。大きな機能は「AskUserQuestion ツールで詳しくインタビューして→SPEC.md を書いて」→新セッションで実装。良い spec は自己完結（関与ファイル・インターフェース・スコープ外・E2E 検証手順）— [Best practices](https://code.claude.com/docs/en/best-practices)
- **セッション管理**: 早く頻繁に軌道修正（`Esc`、`Esc Esc`/`/rewind`、「Undo that」、`/clear`）。**同じ問題で2回以上訂正したら `/clear` して学びを反映した良いプロンプトでやり直す**。コンテキストを積極管理（`/clear`、`/compact <指示>`、部分要約、CLAUDE.md の圧縮指示、`/btw`）。調査は subagent に（「use subagents to investigate X」）。checkpoint でリスクある試行。`/rename` でセッションをブランチのように — [Best practices](https://code.claude.com/docs/en/best-practices)
- **自動化とスケール**: `claude -p` を CI・pre-commit・スクリプトに。並列セッション（worktrees、cross-session messaging、desktop、cloud、agent view、agent teams）。**Writer/Reviewer パターン**（別セッションの新鮮なコンテキストでレビュー、テストを書く Claude と実装する Claude を分ける）。**Fan-out**: `/batch` または `claude -p` ループ＋`--allowedTools`＋`--permission-mode dontAsk`、まず2〜3ファイルで試してから全体へ。auto mode で無人実行。**Adversarial review step**: 完了扱いの前に subagent に diff を新鮮な文脈でレビューさせる（`/code-review` や PLAN.md との照合）。ただし「指摘を探せ」と言われたレビュアーは健全な作業にも指摘を出すので、正しさ・要件に関わる指摘だけを必須にし過剰設計を避ける — [Best practices](https://code.claude.com/docs/en/best-practices)
- **よくある失敗パターン**: kitchen sink session（無関係タスク混在→`/clear`）、何度も訂正（→2回失敗で `/clear`）、肥大化した CLAUDE.md（→容赦なく削る or hook 化）、trust-then-verify gap（→検証できないなら出荷しない）、infinite exploration（→調査範囲を絞るか subagent）— [Best practices](https://code.claude.com/docs/en/best-practices)
- **直感を育てる**: ガイドは出発点。深い問題では文脈を溜める、探索的タスクでは計画を省く、など状況判断を — [Best practices](https://code.claude.com/docs/en/best-practices)
- **確認日**: 2026-10-29

#### 2-2. 「Effective context engineering for AI agents」（Anthropic Engineering, 2025-09-29 公開）
- 「context engineering」= プロンプトだけでなくコンテキストウィンドウ全体の構成を、毎ターン反復的にキュレーションすること。トークン数増加で想起が劣化する「context rot」→コンテキストは逓減的な有限資源で、「the smallest possible set of high-signal tokens」を目指す — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- システムプロンプトは「right altitude」（硬直した if-else と曖昧な指針の中間）。最小構成で始め、失敗を見て追加。ツールは自己完結・重複最小・トークン効率的な「minimal viable set」。例は多様で典型的な少数を — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Just-in-time retrieval（パスやクエリなど軽い参照を持ち必要時にツールで読む）、compaction（古いツール結果のクリアが低リスクな第一歩）、structured note-taking（NOTES.md や To-do）、sub-agent アーキテクチャ（各サブエージェントはクリーンな文脈で探索し1,000〜2,000トークン程度の要約を返す）— [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- Claude Code での具現化: CLAUDE.md を先に入れ glob/grep で必要時取得（ハイブリッド）、圧縮で設計判断・未解決バグ・実装詳細と直近アクセスの5ファイルを保持、To-do リストを構造化メモとして使用 — [Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **確認日**: 2026-10-29

#### 2-3. 「Writing effective tools for agents — with agents」（Anthropic Engineering, 2025-09-11 公開）
- API エンドポイントをそのまま包まず関連手順を統合（`list_contacts` より `search_contacts`）、「More tools don't always lead to better outcomes」。サービス別の名前空間（`asana_search`, `jira_search`）。高シグナルな情報だけ返し暗号的 ID より自然言語名。ページネーション・フィルタ・切り詰めと実行可能なエラーメッセージ。新人に説明するようにツール説明を書き、`user` でなく `user_id` のような明確な引数名。Claude Code で試作→現実的な多段タスクで評価（held-out テストセット）→Claude にトランスクリプトを分析させツールを改善 — [Anthropic Engineering](https://www.anthropic.com/engineering/writing-tools-for-agents)
- **確認日**: 2026-10-29

#### 2-4. 「Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents」（claude.com blog, 2026-06-18 公開）
- 各手段は「いつロードされるか・圧縮を生き延びるか・どれだけの権威を持つか」が違う。root CLAUDE.md=常に必要な事実（200行未満）、サブディレクトリ CLAUDE.md=その領域の規約、rules=具体的制約（`paths:` スコープで安価に）、skills=反復手順、subagents=ノイズの多い副作業、hooks=決定的に必要なこと、output styles=大きな役割変更のみ、`--append-system-prompt`=呼び出し単位の追加的嗜好（増えるほど遵守が弱まる）— [claude.com blog](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)
- **確認日**: 2026-10-29

#### 2-5. Extend Claude Code / How Claude Code works（docs）の推奨
- 「Put guardrails in hooks」:「never edit .env」を CLAUDE.md や skill に書くのは依頼であって保証ではない。PreToolUse hook でのブロックが強制 — [features-overview](https://code.claude.com/docs/en/features-overview)
- Skill の説明文が曖昧・重複すると誤ロードや未ロードが起きる。確実に使わせたいなら `/<name>` で起動 — [features-overview](https://code.claude.com/docs/en/features-overview)
- Claude Code 自身に使い方を聞ける（「how do I set up hooks?」）。`/init`, `/doctor`, `/powerup` — [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works), [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **確認日**: 2026-10-29

### Inferences
- 旧ブログ記事（2025年）にあった「Explore-plan-code-commit」「TDD」「visual iteration」「be specific」「course-correct early」「/clear」「subagents for investigation」「headless」「multi-Claude（Writer/Reviewer, worktrees, fan-out）」はすべて現行 docs に形を変えて残っており、加えて 2026 年版では「検証手段を渡す」が最上位に昇格し、`/goal`・Stop hook・adversarial review・auto mode・`/batch`・workflows といった新機能と結び付けられている。教材ではこの「検証の階段（プロンプト→/goal→Stop hook→別エージェント）」を中心概念に据える価値が高い。
- 旧記事で推奨されていた「think / think hard / ultrathink」の段階的キーワードは、現行では `ultrathink` のみ有効で「think hard」は認識されない（model-config 記載）。旧情報の転載に注意が必要。
- 旧記事の「safe YOLO mode（`--dangerously-skip-permissions` をコンテナで）」に相当する推奨は、現行では「auto mode（分類器）」「sandbox」「bypassPermissions は隔離環境のみ」に置き換わっている。

### Gaps
- 「Building effective agents」（anthropic.com/engineering）は本調査で未取得。
- 「Equipping agents for the real world with Agent Skills」は検索で存在（anthropic.com/engineering → claude.com/blog → anthropic.com/research へリダイレクト）を確認したがツール呼び出し上限のため本文未取得。公開日・内容は未検証。
- 「How Anthropic teams use Claude Code」は anthropic.com/news から claude.com/resources/articles へリダイレクトされるが、リダイレクト先が本環境の許可リスト外で未取得。
- 2026年の新しい engineering ブログ記事は「Steering Claude Code」（2026-06-18）以外に特定できなかった（検索結果は第三者記事が大半）。Code w/ Claude 2026（2026年5月頃）関連の公式発表は第三者経由の言及のみで一次情報未確認。

---

## Key Question 3: 公式ドキュメントが示す代表的ワークフロー

### Takeaway
公式 Common workflows は「広い質問→絞り込み」のコードベース理解、再現コマンド付きのバグ修正、小さく検証可能な単位でのリファクタ、既存スタイルに合わせたテスト追加、PR 作成と見直し、画像・@参照の活用、スケジュール実行、Claude 自身への機能質問、worktree 並列、plan mode、subagent 委任、パイプ利用をレシピとして提示している。

### Cited Findings
- **新しいコードベースの理解**: ルートで `claude` → 「give me an overview of this codebase」→「explain the main architecture patterns」「what are the key data models?」「how is authentication handled?」。広い質問から始めて絞る、規約やパターンを聞く、プロジェクト固有用語の用語集を作らせる — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **関連コードを探す**: 「find the files that handle user authentication」→「how do these work together?」→「trace the login process from front-end to database」。プロジェクトのドメイン用語を使う、code intelligence plugin で定義ジャンプ — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **バグ修正**: エラーを共有→修正案を複数出させる→適用。再現コマンドとスタックトレースを渡す、再現手順、間欠的か常時かを伝える — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **リファクタリング**: 非推奨 API 使用を探す→提案→「同じ挙動を保ったまま」適用→テスト実行。利点を説明させる、後方互換を要求、小さくテスト可能な単位で。大規模移行は公式ブログ「how Anthropic runs large-scale code migrations」を参照 — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **テスト**: 未カバー関数を特定→雛形→エッジケース追加→実行して失敗修正。Claude は既存テストのスタイル・フレームワーク・アサーションに合わせる。境界値・エラー条件を提案させる — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **PR 作成**: 「create a pr」または変更要約→PR 作成→説明の強化。提出前にレビューしリスクを挙げさせる。`gh pr create` で作成された PR はセッションに紐づき `claude --from-pr <番号>` で再開 — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **ドキュメント**: 未ドキュメント関数の特定→JSDoc 等の生成→例の追加→プロジェクト標準との照合 — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **ノート・非コードフォルダ**: Obsidian 等のノート保管庫や Markdown 集でも同様に検索・編集・再編成できる — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **画像**: ドラッグ＆ドロップ、`Ctrl+V`（Windows/WSL は `Alt+V`）、パス指定。エラー画面・UI デザイン・図の解析、モックから CSS/HTML 生成。`[Image #1]` を Cmd/Ctrl+クリックで開く — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **@参照**: `@src/utils/auth.js`（Read ツール上限25,000トークン以内で全文、256KB 超のテキストは含めない）、`@src/components`（一覧）、`@github:repos/owner/repo/issues`（MCP リソース）— [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **Extended thinking**: 現行では effort レベルと `ultrathink` キーワード、`Option+T` で制御（common-workflows 単独の節ではなく model-config に集約）— [model-config](https://code.claude.com/docs/en/model-config)
- **スケジュール実行**: Cloud scheduled tasks / Desktop scheduled tasks / GitHub Actions / `/loop` の使い分け表 — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **Claude に機能を聞く**: Claude は最新ドキュメントを調べて回答する（実行中バージョンに限られない）。実演は `/powerup` — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **その他レシピ**: `claude --continue`/`--resume`、`claude --worktree feature-auth` で並列、`claude --permission-mode plan`、「use a subagent to investigate ...」、`git log --oneline -20 | claude -p "summarize these recent commits"` — [common-workflows](https://code.claude.com/docs/en/common-workflows)
- **ビルドスクリプト組込例**: `package.json` に `"lint:claude": "git diff main | claude -p \"you are a typo linter...\""`（diff をパイプすれば Bash 権限不要）。コミット作成例は `--allowedTools "Bash(git diff *),Bash(git log *),Bash(git status *),Bash(git commit *)"` — [headless](https://code.claude.com/docs/en/headless)
- **確認日**: 2026-10-29

### Inferences
- 公式レシピはいずれも「質問→提案→適用→検証」の4段で書かれており、Best practices の Explore→Plan→Implement→Commit と同型。辞書の各ワークフロー項目は「推奨プロンプト例」と「Tips」を対にして載せる形式が公式と整合する。

### Gaps
- Common workflows ページ内に独立した「extended thinking」節・「通知（notifications）」節は現行版では確認できなかった（過去版にはあったと思われるが未検証）。通知設定は hooks の `Notification` イベントや `terminalSequence` に関する記述のみ確認。

---

## Key Question 4: 2026年の変更点・廃止/改名（古い情報を教えないために）

### Takeaway
2026年は v2.0.77（1月）から v2.1.312（10月末）まで急速に進化し、auto mode の既定化、dynamic workflows・agent view・agent teams・/goal・cross-session messaging・Projects・Mods・AGENTS.md 対応などが追加された。一方で `#` メモリショートカット、`/agents` ウィザード、ultraplan、`/vim`、`/tag`、`/pr-comments`、TaskOutput ツール、SSE transport（非推奨）、「think hard」系キーワードなど、旧来の記事で頻出の要素が削除・非推奨になっている。

### Cited Findings

#### 4-1. 2026年の主な追加（バージョン・日付は CHANGELOG と npm 公開日から）
- v2.1.32（2026-02-05）: Agent teams を research preview で追加（`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.63（2026-02-28）: `/simplify` と `/batch` バンドルコマンド追加 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- 2026-03: 音声入力の多言語化（v2.1.69）、`--bare` フラグ（v2.1.81）、`--channels` の権限リレー（v2.1.81）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.98（2026-04-09）: Monitor ツール（バックグラウンドスクリプトのイベントをストリーム）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.139（2026-05-11）: `/goal` 追加 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.144（2026-05-18）: `/resume` が `claude --bg` / agent view の背景セッションに対応 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- 2026-05〜06: dynamic workflows（v2.1.157 時点で設定項目あり）、v2.1.160（2026-06-01）でトリガー語を `workflow` → **`ultracode`** に改名 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.169（2026-06-08）: `/cd` 追加 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.248（2026-08-27）: cross-session messaging（`SendMessage`/`ListAgents`）を Bedrock/Vertex/Foundry 等にも拡大 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.257（2026-09-01）: Claude Fable 5.1 が既定 Fable モデルに — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.277（2026-09-18）: AGENTS.md 対応 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.283（2026-09-25）: **auto mode がターミナル/VS Code の既定権限モードに** — [permission-modes](https://code.claude.com/docs/en/permission-modes), [npm registry](https://registry.npmjs.org/@anthropic-ai/claude-code)
- v2.1.284（2026-09-28）: Sonnet 5.5 が既定 Sonnet に — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.287（2026-10-01）: Claude Mods — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.293（2026-10-07）: Haiku 5.5 が既定 Haiku に — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.299（2026-10-14）: `/usage` に max effort・workflows・常駐コンテキスト・大きなツール結果の警告 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- v2.1.302（2026-10-16）: `-p`/SDK で承認が必要な呼び出しを既定拒否 — [permission-modes](https://code.claude.com/docs/en/permission-modes)
- 時期不明だが現行 docs に存在する 2026 年系機能: `/btw`、`/doctor prompt-audit`、`/skill-doctor`、`/output-style`（v2.1.269+）、`/config key=value`、`/powerup`、`/team-onboarding`、`/insights`、`/ultrareview`、`/tui fullscreen`、Projects（public beta）、Artifacts、Cloud scheduled tasks（旧 routines）— [commands](https://code.claude.com/docs/en/commands), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [agents](https://code.claude.com/docs/en/agents)

#### 4-2. 廃止・削除・改名・非推奨（教材で教えてはいけない/注記すべきもの）
- **`#` メモリショートカット削除**（v2.0.70, 2025-12-15）:「tell Claude to edit your CLAUDE.md instead」— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **カスタム slash commands（`.claude/commands/`）は skills に統合**（既存ファイルは動作継続）— [skills](https://code.claude.com/docs/en/skills)
- **`/fork` → `/branch` に改名**（v2.1.77, 2026-03-16）。現行の `/fork` は「会話を新しいバックグラウンドセッションへコピー」という別機能、会話を引き継ぐ subagent は `/subtask` — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [commands](https://code.claude.com/docs/en/commands)
- **`TaskOutput` ツール**: v2.1.83 で非推奨→v2.1.277（2026-09-18）で削除。背景タスク出力は Read で読む — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **`/pr-comments` 削除**（v2.1.91）、**`/vim` 削除**（v2.1.92, 2026-04-04, `/config` → Editor mode へ）、**`/tag` 削除**（v2.1.92）— [commands](https://code.claude.com/docs/en/commands), [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **`/simplify` → `/code-review` 改名**（v2.1.147, 2026-05-21, 正しさのバグ報告に変更）。ただし現行 commands ページには別機能として `/simplify` が再掲（Gaps 参照）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [commands](https://code.claude.com/docs/en/commands)
- **「extra usage」→「usage credits」**、`/extra-usage` → `/usage-credits`（v2.1.144, 旧名も動作）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **dynamic workflow トリガー語 `workflow` → `ultracode`**（v2.1.160）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **`/agents` ウィザード削除**（v2.1.198, 2026-07-01）。`/agents` は案内メッセージのみ、`claude agents`（agent view）とは別物 — [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [agents](https://code.claude.com/docs/en/agents)
- **Task tool の `mode` パラメータ非推奨**（v2.1.212, 2026-07-16。subagent は親の権限モードを継承）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **ultraplan 機能削除**（v2.1.222, 2026-08-04、`/ultraplan` は plan mode を使うよう案内）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md), [commands](https://code.claude.com/docs/en/commands)
- **Routines → "cloud scheduled tasks"（formerly routines）に呼称変更**（URL や一部 UI には routines が残存）— [routines](https://code.claude.com/docs/en/routines)
- **`claude --remote` は `--cloud` の非推奨エイリアス** — [claude-code-on-the-web](https://code.claude.com/docs/en/claude-code-on-the-web)
- **MCP の SSE transport は非推奨**（HTTP を使う）— [mcp](https://code.claude.com/docs/en/mcp)
- **Thinking キーワード**: `ultrathink` のみ有効、「think hard」等は非認識。5.5 世代と Fable は thinking 常時 ON — [model-config](https://code.claude.com/docs/en/model-config)
- **`/cost`, `/stats` は `/usage` の別名に統合** — [commands](https://code.claude.com/docs/en/commands)
- **ドキュメントの所在変更**: Claude Code ドキュメントは code.claude.com/docs に移行、旧 engineering ブログのベストプラクティス記事も docs へリダイレクト — [Best practices](https://code.claude.com/docs/en/best-practices)
- **GitHub Action**: `@beta` → `@v1`（`mode`, `direct_prompt`, `max_turns` 等の入力は廃止/移動）— [github-actions](https://code.claude.com/docs/en/github-actions)
- **Fast mode の対象変更**: Opus 4.7 は fast mode 対象外になり、`CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` は削除（no-op）— [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- **確認日**: 2026-10-29

### Inferences
- 2025年の書籍・ブログ・動画で頻出の「`#` で記憶」「`/agents` で作成」「think/think hard/ultrathink の段階」「`--dangerously-skip-permissions` で YOLO」「`.claude/commands/` にカスタムコマンド」は、いずれも現行では削除・非推奨・別手段推奨になっている。辞書では「旧情報」欄を設けて明示的に訂正するのが有効。
- 既定権限モードが auto に変わった（v2.1.283）ことで、「最初は毎回承認を求められる」という前提の解説は2026年9月末以降の新規ユーザーには当てはまらない。権限周りの解説はバージョン依存であることを明記すべき。
- 名称（routines→scheduled tasks、extra usage→usage credits、workflow→ultracode、/simplify→/code-review→/simplify 再掲）が短期間で揺れているため、辞書の見出し語には旧名からの参照（エイリアス）を持たせると検索性が上がる。

### Gaps
- 2026年1〜4月の追加機能の網羅的リスト（全 Added 行は 700 行超あり）を本ノートでは主要なものに絞った。全量はローカルで抽出済みだが未整理（CHANGELOG を直接参照のこと）。
- Opus 5 / Opus 5.5 / Opus 4.8 の Claude Code での既定化時期（版番号）は未特定。
- `/simplify` の再追加時期、`/less-permission-prompts` → `/fewer-permission-prompts` の改名時期は未確認。
- 公式ブログ・ニュースでの 2026 年発表（例: Code w/ Claude 2026、Projects の発表）の一次情報は未取得。
