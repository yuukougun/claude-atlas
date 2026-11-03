# 既存の構造化学習教材(Claude / Claude Code / エージェント型AIコーディング)の構成・網羅範囲・ギャップ調査(2026年10月29日時点)

> 調査メモ: WebSearch はターン全体の上限に達したため、後半は取得済み URL の WebFetch だけで補った。Udemy の日本語講座、大澤本・掌田本・増山本・みのるん式の目次、判断フローチャート系ブログの中身は取れていない(各「Gaps」に記載)。github.com と anthropic.skilljar.com のトップは allowlist 外だったので、ミラーや個別ページで代用した。

---

## 1. Anthropic 公式の学習教材(Anthropic Academy/Skilljar、anthropics/courses、プロンプトチュートリアル、Claude Code ドキュメント)のシラバス

### Takeaway
公式教材は2つに分けられる。1つは「用途別トラック × 約21コース」のカタログ型 Academy。もう1つは、機能リファレンスに横断的な判断ページ(Extend Claude Code / Best practices / Explore the context window)を加えたドキュメント。Claude Code 系コースは「101(入門: 仕組み→日常ワークフロー→カスタマイズ)」と「in Action(中級: 長時間セッションの舵取り→設定→自動化→検証)」の2段構成に再編された。in Action の演習は「どれを使うか」を選ばせる判断型になっている。

### Cited Findings
**Academy 全体の構成**
- 2026年7月31日時点で Academy は21コース。トラックは Everyday Use(Claude 101 / Claude Code 101 / Claude Platform 101 / Introduction to Claude Cowork / Claude Code in Action)、Developer & Technical(Building with the Claude API / Intro to MCP / MCP Advanced Topics / Intro to Agent Skills / Intro to Subagents / Bedrock / Google Cloud)、AI Fluency(Framework & Foundations、Students / Educators / Teaching / Nonprofits / Small Businesses / Builders / pK-12 向け)、General AI Literacy(AI Capabilities and Limitations)の4つ。紹介記事には各コースのレベルも所要時間も書かれていない — [Tutorials Dojo (2026-07-31)](https://tutorialsdojo.com/?p=40340)

**Claude Code 101(入門)**
- 対象は「ソフトウェア開発を始めたばかりの開発者」と「AIコーディングエージェントを使ったことのない経験豊富なエンジニア」。前提はエディタとコマンドラインの基本操作、および Pro/Max/Enterprise アカウントか API キー — [Skilljar: Claude Code 101](https://anthropic.skilljar.com/claude-code-101/469795)
- カリキュラムの順序: What is Claude Code? → How Claude Code works → Your first prompt → Installing → Daily workflows → The explore → plan → code → commit workflow → Context management → Code review → Customizing Claude Code → CLAUDE.md → Subagents → Skills → MCP → Hooks → Quiz — [Skilljar: Claude Code 101](https://anthropic.skilljar.com/claude-code-101/469795)
- 学習目標には「agentic loop・context window・tools・permissions がどう連携するか説明できる」「/compact・/clear・/context でコンテキストを管理できる」「hooks でフォーマット・コマンドブロック・通知を書ける」などがある — [Skilljar: Claude Code 101](https://anthropic.skilljar.com/claude-code-101/469795)

**Claude Code in Action(中級、2026年版)**
- 対象は「単発プロンプトでは Claude Code を使っているが、より長く、監督の少ない、チーム規模のワークフローに進みたい開発者」。構成: 1. Steer the Work(Steering Long Sessions)、2. Configure Claude(A CLAUDE.md That Follows / Verification Skills / Permission Modes / Hooks)、3. Automate Repeat Work(Routines and Headless / GitHub Actions and Code Review)、4. Verify and Share(Trust It: Verifying Unsupervised Runs / Plugins)、5. Quiz — [Anthropic Partners Skilljar](https://anthropic-partners.skilljar.com/claude-code-in-action); [Skilljar](https://anthropic.skilljar.com/claude-code-in-action/303235)
- DataCamp 版は Intermediate、3時間、動画9本・演習31。前提コースは Claude Code 101。演習名は判断を問う形になっている: 「Scope it before you run it」「Rewind, goal, or worktree?」「Put the file on a diet」「The skill worth building first」「Which surface owns the rule?」「Match the mode to the job」「Make the rule unskippable」「Redact instead of block」「Routine, headless, or SDK?」「Gate the turn, don't take its word」「A cold second opinion」「Package what you built」 — [DataCamp: Claude Code in Action](https://www.datacamp.com/ja/courses/claude-code-in-action)
- 旧版(2026年3〜4月時点の紹介)は約1時間・15レッスン・クイズ1回で、セットアップ、ファイル読込/コマンド実行/編集、コンテキスト管理、GitHub 連携、MCP、ベストプラクティスを扱っていた — [pasqualepillitteri.it (2026-03-12, 04-26更新)](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude)。「旧 Skilljar URL は変更後のシラバスを指している」とも指摘されている — [Scrimba (2026-09-09再確認)](https://scrimba.com/articles/best-claude-code-tutorials-and-courses-in-2026/)
- Coursera 版のレビューは 4.3/5(81件)。称賛は「明快な図」「実例」「理論と実践のバランス」。不満は「セットアップの how-to を飛ばす」「古いバージョン前提(Next.js のバージョン固定や依存衝突)」「hooks は絶対パスでないと黙って失敗する」「AI 採点がキーワード一致を要求する」「深さが足りない」「初級と上級が混ざっている」。どの版に対するレビューかは不明 — [Coursera reviews](https://www.coursera.org/learn/claude-code-in-action/reviews)

**API・MCP・Skills・Subagents 系**
- Building with the Claude API は84レッスン・動画8.1時間・クイズ10回 — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude)。章立て: Introduction / Accessing Claude with the API(system prompts、temperature、streaming、structured data)/ Prompt evaluation(テストデータ生成、モデル採点、コード採点)/ Prompt engineering techniques(clear and direct、specific、XML tags、examples)/ Tool use(スキーマ、マルチターン、text edit tool、web search tool)/ RAG and Agentic Search(chunking、embeddings、BM25、multi-index)/ Features of Claude(extended thinking、画像、PDF、citations、prompt caching、code execution、Files API)/ MCP(tools・resources・prompts、inspector、client 実装)/ Anthropic apps(Claude Code と computer use)/ Agents and workflows(parallelization、chaining、routing、workflows vs agents)/ Final assessment — [Skilljar: Building with the Claude API](https://anthropic.skilljar.com/claude-with-the-anthropic-api/287753)
- Introduction to MCP は Stephen Grider 担当、約4時間、Beginner。4モジュール(Introduction / Hands-on with MCP servers / Connecting with MCP clients / Review and final assessment)。前提は Python と JSON/HTTP。MCP Advanced Topics は Intermediate — [beri.net(アグリゲータ)](https://www.beri.net/learning/anthropic-academy-intro-to-mcp)
- Introduction to Agent Skills は30分・6レッスン(Skill とは / 構造 / チーム共有 / 自動化パターン / 命名・テスト・保守)。Introduction to Subagents は4モジュールで、独立コンテキスト、入力と要約の流れ、`/agents` での作成、構造化出力・ブロッカー報告・ツール制限といった設計パターン、使うべき場面とアンチパターンを扱う — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude)
- Claude 101 は19項目: Meet Claude → first conversation → Getting better results → projects → artifacts → skills → Connecting your tools → Enterprise search → Research → use-cases by role → … — [Skilljar: Claude 101](https://anthropic.skilljar.com/claude-101/383401)

**AI Fluency 系(詳細は第5問)**
- Framework & Foundations の構成: Introduction(4D Framework)→ Deep Dive 1: What is Generative AI?(capabilities & limitations)→ Delegation(Project planning and Delegation)→ Description → Deep Dive 2: Effective prompting techniques → Discernment(The Description-Discernment loop)→ Diligence → Conclusion。Prof. Joseph Feller(UCC)と Prof. Rick Dakan(Ringling)との協働 — [Skilljar: AI Fluency F&F](https://anthropic.skilljar.com/ai-fluency-framework-foundations)。分量は1.1時間・14レッスン — [pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude)
- AI Fluency for Builders(CodePath と共同制作)には「Delegation & the builder's toolkit」「Discernment for code」「Discernment for user experience」「Stand behind what you build」などのレッスンがある — [Skilljar: AI Fluency for Builders](https://anthropic.skilljar.com/ai-fluency-for-builders)

**GitHub: anthropics/courses とプロンプトチュートリアル**
- 推奨順序は 1. Anthropic API fundamentals → 2. Prompt engineering interactive tutorial → 3. Real world prompting → 4. Prompt evaluations(9レッスン、promptfoo を使用)→ 5. Tool use(6レッスン)。費用を抑えるため、多くは Claude 3 Haiku を使う前提 — [anthropics/courses(Algolia DocSearch のミラー)](https://docsearch.algolia.com/mcp/docs/repo/anthropics/courses)
- プロンプトチュートリアルは Beginner(1 Basic Prompt Structure / 2 Being Clear and Direct / 3 Assigning Roles)、Intermediate(4 Separating Data from Instructions / 5 Formatting Output & Speaking for Claude / 6 Precognition / 7 Using Examples)、Advanced(8 Avoiding Hallucinations / 9 Building Complex Prompts — Chatbot / Legal / Financial / Coding)、付録(Chaining / Tool Use / Search & Retrieval)の構成。各章にレッスン・演習・「Example Playground」があり、解答キーは Google Sheets で提供 — [gitlink ミラー](https://www.gitlink.org.cn/mirrors/prompt-eng-interactive-tutorial)

**Claude Code ドキュメントの構造(2026年10月)**
- トップレベルは Getting started / Build with Claude Code / Plugins / Administration / Configuration / Reference / Agent SDK / What's New / Resources。Getting started には「How Claude Code works」「Extend Claude Code」「Explore the .claude directory」「Explore the context window」「How Claude Code uses prompt caching」「How Claude remembers your project」「Common workflows」「Prompt library」「Best practices」がある。Reference には Glossary がある。What's New は週次ダイジェスト(2026年の Week 13〜37)。日本語を含む11言語の翻訳があり、各228ページ — [Claude Code docs llms.txt](https://code.claude.com/docs/llms.txt)
- 「Extend Claude Code」ページは機能比較の装置が最も充実している。中身は、(1)「Match features to your goal」表(Feature / What it does / When to use it / Example)、(2)「Build your setup over time」表(Trigger → Add。例: 「Claude gets a convention or command wrong twice → CLAUDE.md に追加」「You paste the same playbook … for the third time → skill 化」「A side task floods your conversation → subagent」「You want something to happen every time without asking → hook」「A second repository needs the same setup → plugin」)、(3)「Compare similar features」タブ(Skill vs Subagent、CLAUDE.md vs Skill、CLAUDE.md vs Output style、CLAUDE.md vs Rules vs Skills、Subagent vs Dynamic workflow、MCP vs Skill、Hook vs Skill)、(4)レイヤーの優先順位、(5)組み合わせパターン表、(6)機能別のコンテキストコスト表、(7)コンテキスト読込の SVG 図(ライト/ダーク対応)。経験則として「CLAUDE.md は200行未満」と書かれている — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- 「Best practices」ページの章立ては Tell Claude what it can't see / Give Claude a check to run / Enforce the rules that can't have exceptions / Change a default / Steer the session / Let Claude run without you / What you can stop doing。冒頭に「セッションが期待通りにいかないときは、ほぼ次のどれか」という症状→節の対応がある。ほかに「Non-deterministic(Claude decides)vs Deterministic(Claude Code enforces)」の5行表、「Instead of / Try」形式の Before/After プロンプト表(例: "fix the login bug" → "users report login fails after the session times out. look at token refresh in src/auth/, write a failing test that reproduces it, then fix it")、「The old advice / Why it's gone」表(IMPORTANT や全大文字での強調、"think hard"、「コンテキスト保護のためのサブエージェント」、「アーキテクチャを CLAUDE.md に書く」などが不要になった理由)がある — [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)
- 「Explore the context window」は、1セッションの中でコンテキストが埋まっていく様子を見せる対話型シミュレーション。System prompt、Auto memory、環境情報、MCP tools(deferred)、Skill descriptions、~/.claude/CLAUDE.md、Project CLAUDE.md、プロンプト、ファイル読込、パス条件で読み込まれる rule、Hook: prettier、npm test 出力、独自コンテキストを持つサブエージェントの起動、/compact などのイベントがタイムラインに並ぶ。後続の節は What survives compaction / When your context fills up / Check your own session — [Explore the context window](https://code.claude.com/docs/en/context-window.md)
- 公式ブログ「Steering Claude Code」(2026-06-18、Michael Segner)は、CLAUDE.md / rules / skills / subagents / hooks / output styles / system prompt の追記、の7手段を「読み込みタイミング / コンパクション時の挙動 / コンテキストコスト / 使う場面」の表で比較している。判断は「こういうことをしていたら」型の5シナリオで示され、全体を「コンテキストコストと強制力(authority)のトレードオフ」として整理している。MCP は比較に含まれていない — [Claude blog](https://www.claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)
- Help Center の日本語版「Claude Code チートシート」(2026-08-07)は1ページで、用語集・コマンド・キーボードショートカットの3つの表からなる。新規ユーザー向け — [support.claude.com](https://support.claude.com/ja/articles/14553413-claude-code-チートシート)

### Inferences
- 公式教材は「機能ツアー」から「判断力」の育成へ重心を移している。in Action の演習名がそのまま「X か Y か」の問いになっている。辞書型リソースの各エントリに「いつ使うか / 何と迷うか」を持たせる設計と相性がよい。
- 公式ドキュメント自体に「Trigger → Add」表と症状→節の対応がすでにある。これは逆引き索引の原型と言える。ただし表は1枚・数行規模で、症状の網羅性は低い。
- 公式ドキュメントは日本語に翻訳済み(228ページ)なので、リファレンスの和訳だけでは付加価値が小さい。価値が出るのは、判断支援、症状からの逆引き、実例(Before/After)、陳腐化の管理である。
- 「What you can stop doing」表があるということは、過去の定番 Tips(ultrathink 系や全大文字での強調など)が公式に撤回されうるということ。エントリには「検証日 / 対象バージョン / 撤回済み」のメタデータが必要。

### Gaps
- anthropic.skilljar.com のカタログトップと github.com/anthropics/courses の本体は取得できず、ミラーと個別ページで代用した。Intro to MCP のレッスン単位のタイトル、MCP Advanced Topics・Claude Platform 101・Introduction to Claude Cowork・AI Capabilities and Limitations の詳細シラバスは未取得。
- 現行の Claude Code in Action の公式所要時間は Skilljar 版では非公開(DataCamp 版は3時間)。

---

## 2. サードパーティのコース(DeepLearning.AI、Coursera/Udemy、YouTube など)のシラバスとレベル

### Takeaway
サードパーティの主要コースは次の3系統に分かれる。(1) Anthropic の教育責任者が関わる DeepLearning.AI の短期コース(プロジェクト駆動、中級)。(2) Udemy や YouTube の「作って売る」「ノーコード」寄りの長尺講座。(3) Simon Willison のようなツール非依存のパターン集。いずれも線形のハンズオンが中心で、症状から引く構成や判断支援を前面に出したものは見当たらない。

### Cited Findings
- DeepLearning.AI「Claude Code: A Highly Agentic Coding Assistant」: 講師は Elie Schoppik(Anthropic 技術教育責任者)、Intermediate、約2時間、2026-08-17更新。構成: Introduction / What is Claude Code? / Course Notes / Setup & Codebase Understanding / Adding Features / Testing, Error Debugging and Code Refactoring / Adding Multiple Features Simultaneously / Exploring GitHub Integration & Hooks / Refactoring a Jupyter Notebook & Creating a Dashboard / Creating a Web App Based on a Figma Mockup / Conclusion / Quiz / Prompts & Summaries of Lessons。題材は RAG チャットボット、EC データの Notebook からのダッシュボード化、Figma からの Web アプリの3プロジェクト。MCP は Playwright と Figma を使う。前提は Python と Git — [DeepLearning.AI](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)
- DeepLearning.AI「Agent Skills with Anthropic」: Beginner、2時間19分、2026-07-17更新。レッスン: Why Use Skills I/II、Skills vs Tools, MCP, and Subagents、Exploring Pre-Built Skills、Creating Custom Skills、Skills with the Claude API / Claude Code / Claude Agent SDK。SKILL.md の形式と progressive disclosure も扱う — [DeepLearning.AI](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
- Educative「Claude Code: Workflows and Tools」: 4時間・15レッスン。Introduction(2)/ Fundamentals(6: Conversation-Driven Development、Context Management and Project Setup、Advanced Communication and Planning、Guiding the Conversation、Custom Commands and Skills、Sub-Agents)/ Hooks and Customization(3)/ Integrations(2: MCP、GitHub)/ Wrap Up(2)。ブラウザ内エディタと AI Tutor 付き — [Educative](https://www.educative.io/courses/claude-code)
- Scrimba のまとめ記事(2026-03-25公開、09-09再確認)が挙げているもの:
  - Coursera「Vibe Coding with Claude Code」(Scrimba 制作、2モジュール約3時間、Intermediate、4.5/28件)
  - 「CC for Everyone」(Carl Vellotti、Claude Code の中で学ぶ形式、4〜5時間、非技術者向け、要 Pro)
  - 「CC for PMs」(10〜12時間)
  - Frank Kane「Claude Code: Building Faster with AI」(6セクション40レッスン。テスト、セキュリティスキャン、CI、GitHub Actions、サブエージェント、MCP)
  - Matt Pocock の AI Hero コホート講座(795ドル、2026-03-30〜04-10、現在はウェイトリストのみ)

  記事が指摘する共通の欠落: 「古いコホートや古いセットアップ手順が推薦され続けている」「無料教材はテスト・セキュリティスキャン・CI・デプロイといったライフサイクル全体を飛ばしがち」「質の低いチュートリアルは簡単なアプリで止まるか、CLAUDE.md やコンテキスト管理を扱わない」 — [Scrimba](https://scrimba.com/articles/best-claude-code-tutorials-and-courses-in-2026/)。Scrimba 自身が Coursera 講座の制作元なので利益相反があり、記事内で開示されている。
- Udemy のおすすめ記事(2026-03-08、アフィリエイトリンク付き)に並ぶのは、Frank Kane 講座、「The Complete AI Coding Course (2026): Cursor, Claude Code」、「MCP: Build Agents with Claude, Cursor, Flowise, Python & n8n」、「The Complete Agentic AI Engineering Course (2026)」(69,333人。Claude は複数フレームワークの1つ)など。Claude Code 専用でないものが多い — [React Java Substack](https://reactjava.substack.com/p/i-tried-20-claude-code-courses-on)
- YouTube ロードマップ(2026-10-25検証)は無料動画20本を4段階に並べたもの: Start Here(Tech With Tim、freeCodeCamp 4:27:48 など)→ Core Skills(Nick Saraev 4時間「Build & Sell」、Nate Herk 10時間、Programming with Mosh など)→ Advanced & Deep Dives(Nick Saraev Advanced 3時間、IndyDevDan の Hooks)→ Stay Current。Anthropic 公式の短い動画(「How Claude Code Works」2:51)も含まれる — [Developer Educators](https://developereducators.com/roadmap/claude-code/)
- Simon Willison「Agentic Engineering Patterns」(2026-02-23開始、全16章): What is agentic engineering? / Writing code is cheap now / Hoard things you know how to do / AI should help us produce better code / Anti-patterns: things to avoid / How coding agents work / Using Git with coding agents / Subagents / Red/green TDD / First run the tests / Agentic manual testing / Linear walkthroughs / Interactive explanations / 実例2章 / Prompts I use。Claude Code と Codex の両方を対象にしたツール非依存の構成 — [simonwillison.net/guides](https://simonwillison.net/guides)

### Inferences
- 長尺の YouTube や Udemy 講座は「作って売る」「ノーコードでアプリ」の訴求が強い。本プロジェクトの想定読者(すでに多用しているが使いこなせていない層)向けの「判断・検証・失敗回避」を扱う教材は手薄。
- Willison のガイドは「パターン名 → 解説」の章立てで、アンチパターンを独立した章にしている。辞書エントリの命名(パターン名を見出し語にする)の参考になる。

### Gaps
- Udemy の日本語 Claude Code 講座のカリキュラムは、検索上限のため未調査。
- 「Foundations of AI Coding Agents with Claude Code」(Ascendient Learning)はタイトルしか確認できていない。
- DeepLearning.AI「MCP: Build Rich-Context AI Apps with Anthropic」は検索結果で名前を見ただけで、シラバスは未取得。

---

## 3. 書籍(英語・日本語、2025〜2026年)の目次

### Takeaway
日本語の Claude Code 本は2025年12月から2026年11月にかけて10冊以上出ている。ほとんどが「導入 → 小さなアプリ → CLAUDE.md・MCP・サブエージェント・Hooks・Skills → CI/チーム/企業導入」という線形構成をとる。辞典的な構成と評されるのは齊藤本(『完全解説!Claude Codeテクニック集』)だけで、それも機能別の章立てであり、症状から引く逆引きではない。英語圏では、Claude Code 専用本(Packt)とツール非依存の思想書(O'Reilly、IT Revolution)に分かれる。

### Cited Findings
**日本語書籍の全体像**
- クリスタルメソッドの一覧(2026-06-08公開、10-23更新)が、出版社の公式ページで書誌を確認できた11冊を発売順に並べている。平川(技評 2025-12-05)、西見ほか(技評 2025-12-26)、箕輪(インプレス NextPublishing 2026-02-20)、大澤(マイナビ 2026-05-19)、佐藤(技評 2026-06-08)、掌田(秀和システム新社 2026-06-16)、Oikon・前川(SB 2026-08-14)、齊藤(インプレス 2026-08-18、全15章528ページ、「辞典的な構成」)、増山(技評 2026-09-08)、御田「みのるん式」(技評 2026-09-24、事務仕事への活用や社内のセキュリティの壁の越え方)、羽田野(インプレス 2026-09-25)の11冊 — [クリスタルメソッド](https://crystal-method.com/blog/claude-code-books/)
- DotAI(2026-04-05)はレベル別の読書順として「平川 → 西見ほか → 箕輪」を推奨し、物語形式の『ストーリーで覚えるClaude Code開発ガイド』(Kindle のみ、2026-02-13、280ページ)は並行して読んでよいとしている。評価は、平川本「一部古くなっている情報もある」、西見本「入門者には分量が重い」、箕輪本「154ページと薄く入門者には難しい」。運営元による主観評価 — [DotAI TIMES](https://dot-ai.myuuu.co.jp/times/108)

**個別の目次**
- 『実践Claude Code入門 ―現場で活用するためのAIコーディングの思考法』(西見公宏・吉田真吾・大嶋勇樹、技術評論社、2025-12-26、304ページ)。第1部 ハンズオン(1 ソフトウェアエンジニアリングへの組み込み / 2 基礎 / 3 MCP / 4 スペック駆動開発 / 5 Claude Code Action)、第2部 動作原理と開発フローの体系化(6 仕組みの理解 / 7 意図通りに動かす / 8・9 スペック駆動開発フローの体系化(設計・実践))、付録 — [gihyo.jp](https://gihyo.jp/book/2026/978-4-297-15354-0)
- 『Claude CodeによるAI駆動開発入門』(平川知秀、技術評論社、2025-12-05、320ページ)。章タイトルに作る時間の目安が入っている: 2章「5分でアプリを作る」、3章「30分でAIチャットボット」(MCP、GitHub Actions)、4章「半日で社内システム」(コンテキストウィンドウの理解、ガードレール、タスク分割、並列処理とサブエージェント、カスタムスラッシュコマンドと Hooks)、5章 セキュリティと高度な使い方。付録はスラッシュコマンド一覧と索引 — [gihyo.jp](https://gihyo.jp/book/2025/978-4-297-15275-8)
- 『Claude Code実践入門[生成AI深掘りガイド]』(Oikon・前川蒼、SBクリエイティブ、2026-08-14)。1 AIコーディングの世界(補完から自律へ、Claude 製品群の全体像)/ 2 使ってみよう(プロンプトの書き方①具体的な指示と例 ②リッチコンテンツ、コンテキスト管理、動作モード、モデル選択とコスト、セッション管理)/ 3 制御する(設定ファイルの配置と適用範囲、CLAUDE.md とメモリ、settings.json、Hooks、サンドボックス、「まとめ:制御レイヤーの整理」)/ 4 拡張する(Skills、MCP、マルチエージェント、Plugins、「まとめ:4つの拡張機能を組み合わせる」)/ 5 現場で活用する(ヘッドレス、/loop と /goal、CI/CD、安定運用、コスト・ログ・トラブルシューティング、チーム運用、コスト可視化)/ 6 エンタープライズ(セキュリティ・コンプライアンス、ネットワーク、コスト、既存環境との統合、社内展開)/ 7 今後 — [丸善ジュンク堂](https://www.maruzenjunkudo.co.jp/products/9784815643119)
- 『完全解説!Claude Codeテクニック集 爆速開発のための完全ガイド』(齊藤貴義、技術の泉シリーズ、プレスリリース 2026-05-08、本文522ページ、B5カラー)。全15章: 1 アーキテクチャと基本原則 / 2 コンテキストウィンドウ管理 / 3 Skill / 4 サブエージェント / 5 Hooks / 6 Agent Teams / 7 Tasks / 8 MCP 完全解説 / 9 MCP 統合の実践 / 10 Plugins / 11 CI/CD とチーム開発 / 12 並列駆動開発 / 13 データ分析・ML / 14 インフラ自動化 / 15 パフォーマンス最適化とトラブルシューティング — [PR TIMES](https://prtimes.jp/main/html/rd/p/000007363.000005875.html)。発売日とページ数は資料によって異なる(クリスタルメソッドは 2026-08-18・528ページとし、「同名の NextPublishing 版も報じられている」と注記している)— [クリスタルメソッド](https://crystal-method.com/blog/claude-code-books/)
- 『Claude Code開発体系 拡張・制御・運用の手引き』(箕輪峻、インプレス NextPublishing、2026-02-20、154ページ)。1 基本 / 2 MCP で拡張 / 3 Context 管理とサブエージェント / 4 便利機能 / 5 動作を管理 / 6 カスタマイズを包括的に管理 — [koubo/PR TIMES](https://koubo.jp/press-release/prtimes/c5875_r7187)
- 『Claude Codeで学ぶ Agent Skills入門』(佐藤亮、技術評論社、2026-06-08、272ページ)。1 Agent Skills とは(他技術との違い)/ 2 オープン標準と動向 / 3 初体験 / 4〜6 Anthropic 公式スキルの章別カタログ(design 系、pdf・docx・pptx・xlsx、mcp-builder・webapp-testing など)/ 7 パートナーとサードパーティ(見極め方)/ 8 skill-creator での作成(テストと改善ループ、description の最適化)/ 9 配布・セキュリティ・組み込みスキル。付録は frontmatter リファレンス — [gihyo.jp](https://gihyo.jp/book/2026/978-4-297-15698-5)
- 『1週間でClaude Codeの基礎が学べる本』(羽田野太巳、インプレス、2026-09-25、360ページ)。1日目〜7日目の構成(知る・準備 → はじめてのアプリ → 自在に操る → 仕上げ → 外部連携と自動化 → 拡張と安全管理 → さらに広く)。Pro 以上のプランが前提 — [koubo/PR TIMES](https://koubo.jp/press-release/prtimes/c5875_r7683)
- 近刊(発売日 2026-11-27、本調査時点では未発売)。SBクリエイティブ、山田祥寛・高江賢・山田研二・山田奈美。第3章「CLAUDE.md から始める連携ファイルの育て方」に「CLAUDE.md だけの限界」「分割の判断基準」「paths 付き rules」「よくある失敗パターンと対処法(肥大化させない / 役割を混ぜない / 指示で済ませない / 個人と共有を分ける)」がある。第6章はチーム展開で、「導入前の12項目」チェックリストを含む。付録はコマンドリファレンス、シーン別プロンプトパターン集、プロジェクトタイプ別 CLAUDE.md テンプレート集、MCP サーバーカタログ — [丸善ジュンク堂](https://www.maruzenjunkudo.co.jp/products/9784815646813)。**書名に食い違いあり**: 取得したページ本文は『作りながら学べる Claude Codeの基本』、同じ URL の検索結果タイトルは『手を動かして学ぶ Claude Code入門』。書名は未確定として扱う。

**英語書籍**
- 『Agentic Coding with Claude Code』(Eden Marco、Packt、2026-03-27、376ページ)。Part 1 Foundations of Context Engineering(1 Context Engineering / 2 The Gist of Claude Code / 3 Essential Commands)、Part 2(4 MCP & Plugins / 5 GitHub / 6 Planning and Multi-agent / 7 Subagents / 8 Output Styles)、Part 3(9 Agent Skills / 10 Claude Code Desktop / 11 Deep Agents) — [Packt](https://www.packtpub.com/product/agentic-coding-with-claude-code/9781806022595)
- 『Beyond Vibe Coding』(Addy Osmani、O'Reilly、2025年8月、254ページ)。Part I Foundations(What Is Vibe Coding? / The Art of the Prompt)、Part II AI Coding in Practice(The 70% Problem / Beyond the 70% / Understanding Generated Code: Review, Refine, Own / Prototyping / Web Apps)、Part III Trust and Autonomy(Security, Maintainability, and Reliability / Ethics / Autonomous Background Coding Agents / Future) — [O'Reilly](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749)
- 『Vibe Coding: Building Production-Grade Software With GenAI, Chat, Agents, and Beyond』(Gene Kim & Steve Yegge、2025-10-21、384ページ)。4部構成で、レビューによれば Part 1 が FAAFO(Fast, Ambitious, Autonomous, Fun, Optionality)、Part 2 が「head chef(開発者)と sous chef(AI)」の比喩、Part 3 がツールと inner / middle / outer の開発ループ、Part 4 が組織変革。Goodreads の説明とレビューに基づく二次情報 — [Goodreads](https://www.goodreads.com/book/show/228438060-vibe-coding)

### Inferences
- 日本語書籍の章立ては「制御(CLAUDE.md・settings・Hooks・sandbox)」と「拡張(Skills・MCP・マルチエージェント・Plugins)」の二分法に収束しつつある(Oikon 本、箕輪本の副題「拡張・制御・運用」)。辞書サイトのカテゴリ設計で、この軸は日本の読者に馴染みやすい。
- 書籍は発売から数か月で陳腐化しやすい(平川本に「一部古くなっている」という声。in Action も改訂済み)。紙ではできない「継続更新される辞書」であること自体が差別化になる。
- 近刊の SB 本(書名未確定)の「よくある失敗パターン」「分割の判断基準」「12項目チェックリスト」は、本プロジェクトのエントリ形式(症状・判断シグナル)に近い。競合として発売後に確認すべき。

### Gaps
- 大澤本(マイナビ)、掌田本(秀和システム新社)、増山本(技評)、御田本(技評)、ストーリー本の詳細目次は、検索上限のため未取得。
- 英語の Claude Code 本(Leanpub の自費出版など)は未調査。Manning の該当書は確認できていない。

---

## 4. コミュニティによる構造化ガイド(ガイドリポジトリ、チートシート、ClaudeLog、awesome リスト、ベストプラクティス集)

### Takeaway
大規模なコミュニティガイドは「ペルソナ・レベル別の学習パス + 時間見積もり + クイズ + テンプレート集 + 図」というコース型に寄っている。ClaudeLog は「Mechanics(概念)/ FAQ(疑問形スラッグ230+)/ Add-ons」に分けたサイト型。awesome リストは「悩み別カテゴリ」の索引型。日本語では Zenn の「逆引きコマンド事典」が「〜したい」形式の一問一答をとっており、本プロジェクトの逆引き索引に最も近い先行例。

### Cited Findings
- **Claude Code Ultimate Guide**(Florian Bruniaux、v3.41.1、2026-07-29更新): ロール別の「Choose Your Path」(テックリード / CTO / PM / 開発者 / キャリアチェンジ組など)、7モジュールの学習パス(8〜11時間)、1ページのチートシート、473問のクイズ(Junior / Senior / Power User / PM の4プロファイル)、Mermaid 図48点(ASCII のフォールバック付き)、「agents vs skills vs commands」の判断フレームワーク、Golden Rules(コンテキスト使用率の閾値を含む5原則)、57枚のリキャップカード、AI 向けの機械可読ファイル(llms.txt / reference.yaml)、MCP サーバー、脅威データベース(CVE 対応28件、悪性スキル655件)。テンプレート数は箇所により268と275で不一致 — [README](https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/693d97d284ea342c8c8fb13894df0cee26d3a3d3/README.md)
- 同ガイドの学習パスは、モジュールごとに ⭐ の難易度(Beginner / Intermediate / Advanced)と演習・チェックポイントを持つ。学習者レベルは利用期間で定義されている(初日 / 1〜4週間 / 1か月以上)。各モジュールは `/lesson-quiz [topic]` で確認し、最後に `/self-assessment comprehensive` を行う — [learning-path README](https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/693d97d284ea342c8c8fb13894df0cee26d3a3d3/guide/learning-path/README.md)
- **claude-howto**(luongnv89、2026-10-26更新): 冒頭で既存教材の問題を3つ挙げている。「ドキュメントは機能を説明するが組み合わせ方を示さない」「学習順序が不明確」「例が基本的すぎる」。10モジュールにそれぞれレベル(Beginner / Beginner+ / Intermediate / Intermediate+ / Advanced)と時間を付けている(Slash Commands 30分 → Memory 45分 → Checkpoints → CLI → Skills → Hooks → MCP → Subagents 1.5時間 → Advanced → Plugins、合計11〜13時間)。ほかに「Find Your Level」、公式ドキュメントとの比較表、「What Can You Build」表(用途 → 組み合わせる機能)、do's and don'ts、トラブルシューティング、`/self-assessment`、EPUB — [claude-howto README](https://cdn.jsdelivr.net/gh/luongnv89/claude-howto@main/README.md)
- **awesome-claude-code**(hesreallyhim): カテゴリは Start Here / From Anthropic / Documentation, Knowledge & Learning / … / Security / Multi-Agent Orchestration / Skills / Memory & Context Persistence / Usage & Cost Monitoring / Observability など。各エントリには評価的なコメントが付き、一部には作成日・最終コミット・ライセンス・スター数のメタデータがある — [awesome-claude-code ミラー](https://gh.mise.run.place/hesreallyhim/awesome-claude-code)。スター数は約4.7万(記事執筆時点、年は不明)。記事の勧めは「自分の悩みに対応するカテゴリから入る」「全部入れない、Context bloat is real」 — [DEV Community](https://dev.to/tienbku/the-github-repository-every-claude-code-user-needs-to-bookmark-2b6f)
- **ClaudeLog**: セクションは Install / Tutorial / Configuration / Pricing & Limits / News & Changelog / Mechanics(`/mechanics/<slug>`。Foundation・Agents・Performance・Development に分類。例: Plan Mode、Ultrathink、Hooks、Rewind、「Context Window Depletion」)/ CLAUDE.md Vault / MCPs & Add-ons / Comparisons / FAQs(230ページ以上。「what-is-X-in-claude-code」のような疑問形スラッグで、フォルダなしのフラット構造)— [ClaudeLog llms.txt](https://claudelog.com/llms.txt)
- **チートシート類**:
  - aeulker/claude-code-cheat-sheet は HTML と Excel の形式で、都市を模した「記憶の宮殿」型の学習ガイドを含む。SuperClaude フレームワークへの依存が強い — [GitHub](https://github.com/aeulker/claude-code-cheat-sheet)
  - Shipyard のチートシート(2025-08-18)は、Getting started / Config / CLI commands + flags / Interactive session commands / Advanced features / Common workflows / Security + permissions / Session model の順。3列の表と `>` 付きのプロンプト例を使う — [DEV Community](https://dev.to/shipyard/claude-code-cli-cheatsheet-config-commands-prompts-best-practices-13li)
- **日本語の逆引き**: Zenn「Claude Code 逆引きコマンド事典」(ML_Bear、2025-06-23)は「『Claude Codeの〇〇で困った時どうする?』という逆引き一問一答形式」と自ら説明している。見出しは「〜したい」「〜どうやるの?」の形で、カテゴリは基本コマンド / 会話制御 / 設定 / メモリ・ルール管理 / 画像 / Git / Custom slash commands / MCP / 使い方のコツ — [Zenn](https://zenn.dev/ml_bear/articles/84e92429698177)
- 典型的な日本語の体験記事(MIXI、2025-02-27公開、06-02更新)は、セットアップ → 実践 → 注意点と進む線形の記録で、日付付きの追記で鮮度を保っている — [Zenn](https://zenn.dev/mixi/articles/daee52c49e739b)
- 「Skills vs Subagents vs Hooks vs MCP をどう使い分けるか」を主題にしたブログ記事は多数ある(例: davidloor「When to use skills, CLAUDE.md, subagents, hooks, MCP」、gautamkhorana「skills vs commands vs subagents vs hooks vs MCP」、claudedirectory「Which Claude Code Extension Should You Use?」、productpeak「The Four Claude Code Building Blocks」)。いずれも検索結果のタイトルで確認しただけで、本文は未確認 — [davidloor](https://davidloor.com/en/blog/when-to-use-skills-claudemd-subagents-hooks-mcp); [gautamkhorana](https://gautamkhorana.com/blog/claude-code-skills-vs-commands-vs-subagents-vs-hooks-vs-mcp/); [claudedirectory](https://claudedirectory.org/blog/claude-code-skills-vs-subagents-vs-mcp); [productpeak](https://productpeak.substack.com/p/the-four-claude-code-building-blocks)

### Inferences
- 「機能の使い分け」記事が乱立していること自体が、判断支援への需要が大きいことを示している。辞書の中核エントリとして「X vs Y」比較ページ群を用意する価値は高い。
- ClaudeLog の疑問形 FAQ スラッグと ML_Bear の「〜したい」見出しは、逆引き索引の見出し語のつけ方(症状・欲求の文で引く)の先行例になる。ただしどちらも、レベルや前提知識、関連ページといったメタデータは構造化されていない。
- コミュニティガイドは分量が大きく(2.4万行超、テンプレート275件など)、数値の不整合も見られる。網羅を競うより、エントリの粒度を揃え、検証日を明示する方が信頼性で差別化できる。

### Gaps
- everything-claude-code など他の大型リポジトリの構造は未確認。
- 日本語の Claude Code ガイドリポジトリ(GitHub や Zenn Books)の体系的な調査は、検索上限のため未実施。

---

## 5. 教育学的フレーミング(AI Fluency の4D、エージェントのメンタルモデル、AI支援開発の成熟度レベル): 本リソースの整理軸・レベル体系に使えるもの

### Takeaway
軸の候補は大きく2種類ある。1つは能力の軸で、AI Fluency(3モダリティ × 4D × 各3下位能力、CC BY-NC-ND)がこれにあたる。もう1つは自律度・成熟度の軸で、Yegge の8レベル、Eledath の8レベル、in Action の「監督の少なさに比例した検証」がこれにあたる。公式ドキュメントにはさらに、機能を選ぶための軸として「決定論的か非決定論的か」と「コンテキストコストと強制力」がある。辞書エントリのメタデータとしては、「4D のどれを鍛えるか」「どの自律段階で必要になるか」「決定論的か」の3つを組み合わせられる。

### Cited Findings
- **AI Fluency Framework v1.1**(Rick Dakan & Joseph Feller、2025、CC BY-NC-ND 4.0)は、AI Fluency を「AI と効果的に、効率的に、倫理的に、安全に働くこと」と定義する。人とAIの関わり方を3つのモダリティに分ける: Automation(人の直接指示でAIがタスクを実行)/ Augmentation(人とAIが反復的に共同で定義・実行する)/ Agency(人が、将来のタスクを独立に行うようAIを構成する)。4D はそれぞれ3つの下位能力を持つ:
  - Delegation: Goal and Task Awareness / Platform Awareness / Task Delegation
  - Description: Product / Process / Performance Description
  - Discernment: Product / Process / Performance Discernment
  - Diligence: Creation / Transparency / Deployment Diligence

  出典 — [Ringling College LibGuide](https://ringling.libguides.com/ai/framework)
- コースでは Description と Discernment を継続的なフィードバックループとして教える。Delegation の下位能力を「Problem Awareness / Platform Awareness / Task Delegation」と呼ぶ紹介もあり、v1.1 の「Goal and Task Awareness」と呼び方が違う — [The Neuron (2025-06-15)](https://www.theneuron.ai/explainer-articles/inside-anthropics-ai-fluency-masterclass-on-human-ai-collaboration)
- 4D は「decide → prompt → evaluate → own」の閉ループとしても説明される。2023〜2024年に開発された — [Envisioning](https://www.envisioning.com/vocab/4d-ai-fluency)
- **Steve Yegge の8レベル**(二次資料): 1 No AI → 2 IDE Agent, Permissions On → 3 IDE Agent, YOLO Mode → 4 Watching Agent, Not Diffs → 5 CLI-First, IDE Abandoned → 6 Several Agents in Parallel → 7 10+ Agents by Hand → 8 Custom Orchestrator。同じ記事の中で、レベル1の定義が「No AI」と「autocomplete」の2通りに書かれている。最大の断絶はレベル5(conductor から orchestrator への移行)とされる — [Augment Code (2026-04-20)](https://www.augmentcode.com/guides/steve-yegge-8-levels-ai-assisted-development)
- **Bassim Eledath の「8 Levels of Agentic Engineering」**(紹介記事による): 1 Tab Complete → 2 Agent IDE → 3 Context Engineering → 4 Compounding Engineering(計画・委任・評価・教訓をルール化するループ)→ 5 MCP and Skills → 6 Harness Engineering and Automated Feedback Loops → 7 Background Agents → 8 Autonomous Agent Teams — [Unblocked (2026-04-29)](https://getunblocked.com/blog/8-levels-of-agentic-engineering/)
- 『Vibe Coding』(Kim & Yegge)は FAAFO、head chef の比喩、inner / middle / outer の開発ループを使う(二次情報) — [Goodreads](https://www.goodreads.com/book/show/228438060-vibe-coding)。Osmani は「The 70% Problem」(AI で7割まではすぐ進むが残りが難しい)を章題にしている — [O'Reilly](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749)
- 公式 Claude Code ドキュメント自体のレベル観は「最初は CLAUDE.md から始め、他の拡張は具体的なトリガーが現れたら追加する」というトリガー駆動の段階化 — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)。Best practices は指示を「Non-deterministic(Claude が決める)/ Deterministic(Claude Code が強制する)」の2列で整理している — [Best practices](https://code.claude.com/docs/en/best-practices)。公式ブログは各手段を「コンテキストコストと強制力のトレードオフ」で位置づける — [Claude blog](https://www.claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)
- Claude Code in Action の学習目標には「監督の少なさに比例して無人実行の結果を検証する」とある — [Anthropic Partners Skilljar](https://anthropic-partners.skilljar.com/claude-code-in-action)
- **Claude 認定資格**(第三者サイト。非公開の受験者向け試験ガイド v1.0(2026年7月発効)に基づくと主張): Claude Certified Architect – Foundations(CCA-F)のドメイン配分は Agentic Architecture & Orchestration 27% / Claude Code Configuration & Workflows 20% / Prompt Engineering & Structured Output 20% / Tool Design & MCP Integration 18% / Context Management & Reliability 15%。ほかに Architect Professional、Developer Foundations、Associate Foundations(非技術職向け。Output Evaluation & Validation 21% など)があるとされる。3資格のコードはタグからの推測で未確認 — [claudearchitectcertification.com (2026-08-20)](https://claudearchitectcertification.com/blog/what-each-claude-certification-actually-tests-domain-by-domain.md)
- Ultimate Guide は学習者レベルを利用期間(初日 / 1〜4週 / 1か月以上)で定義している — [learning-path README](https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/693d97d284ea342c8c8fb13894df0cee26d3a3d3/guide/learning-path/README.md)。claude-howto は Beginner〜Advanced の5段階に「you can …」というスキル記述を付けている — [claude-howto](https://cdn.jsdelivr.net/gh/luongnv89/claude-howto@main/README.md)

### Inferences
- 本リソースの「レベル」は利用期間や機能の難しさではなく、委任の自律度で定義するのが想定読者(多用しているが使いこなせていない層)に合う。例えば次の段階が考えられる(Yegge・Eledath・in Action を参考にした提案で、出典のある定義ではない)。
  - L1 対話で一緒に書く
  - L2 計画させて任せる
  - L3 長時間セッションを舵取りする
  - L4 並列・ワークツリー
  - L5 無人・定期・CI
- 各エントリには「4D タグ」を付けられる。例: 「プロンプトの具体化」は Description、「差分の検証・テストゲート」は Discernment、「hooks や deny ルールでの強制」は Diligence/Deployment、「どこまで任せるか」は Delegation。AI Fluency は CC BY-NC-ND なので、用語を参照・引用するのはよいが、改変した派生フレームワークとして再配布する場合はライセンスの確認が必要。
- 機能選択系のエントリには「決定論的か非決定論的か」「常時読込かオンデマンドか」「コンテキストコスト」を共通の属性欄として持たせると、公式の比較軸と一致して検証しやすい。

### Gaps
- Yegge の一次資料(Medium のエッセイなど)は取得しておらず、8レベルは二次資料に依拠している。Eledath の原典も未取得。
- AI Fluency for Builders のレッスン本文で、エージェント型コーディングへの 4D の具体的な適用がどう説明されているかは未確認。
- 公式な「Claude Code 成熟度モデル」は見つからなかった。

---

## 6. 評価されている提示手法(判断フローチャート、Before/After プロンプト、注釈付きセッション記録、コンテキスト図、機能比較表など)

### Takeaway
実際に多く使われ、評価もされているのは次の6つ。(1) 機能比較表(読込タイミング・コスト・決定論性など共通の列を持つもの)、(2) トリガー→機能の対応表、(3)「Instead of / Try」の Before/After プロンプト、(4) 撤回された旧 Tips の表、(5) コンテキストウィンドウの図や対話型シミュレータ、(6)「X か Y か」を問う判断演習。厳密な分岐型フローチャートは、公式では使われていない(公式ブログもシナリオ型)。注釈付きセッション記録が評価されているという証拠は見つからなかった。

### Cited Findings
- 機能比較表: 公式の「Match features to your goal」(Feature / What it does / When to use it / Example)、「Context cost by feature」(When it loads / What loads / Context cost)、ペアごとの比較タブ(Hook vs Skill では Runs / Triggered by / Determinism / Context cost / Best for)。「Put guardrails in hooks. … is a request, not a guarantee」のような一行の原則も添えている — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- トリガー→機能表(「同じ誤りを2回したら CLAUDE.md」「同じ手順を3回貼ったら skill」など、回数の閾値付き) — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- Before/After: 「Instead of / Try」表 — [Best practices](https://code.claude.com/docs/en/best-practices)
- 陳腐化した助言の表: 「The old advice / Why it's gone」(全大文字での強調、think hard、「コンテキスト保護のためのサブエージェント」、「Tell Claude to keep going」など) — [Best practices](https://code.claude.com/docs/en/best-practices)
- 症状→節の対応(「セッションが期待通りにいかないときはほぼ次のどれか」) — [Best practices](https://code.claude.com/docs/en/best-practices)
- コンテキストの図: 対話型タイムラインのシミュレーション(コンパクション後に何が残るかの節を含む) — [Explore the context window](https://code.claude.com/docs/en/context-window.md)。読込タイミングの SVG 図(ダークモード版あり) — [Extend Claude Code](https://code.claude.com/docs/en/features-overview)
- 判断演習: in Action の「Rewind, goal, or worktree?」「Which surface owns the rule?」「Routine, headless, or SDK?」など — [DataCamp](https://www.datacamp.com/ja/courses/claude-code-in-action)
- 判断の提示形式: 公式ブログは形式的な決定木ではなく「if you find yourself doing this」型の5シナリオを使う — [Claude blog](https://www.claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more)
- 学習者の評価: in Action の Coursera レビューでは「明快な図」「実例」「現実的なクイズ」が称賛され、「古いバージョン」「セットアップ省略」「AI 採点のキーワード一致」が批判された — [Coursera reviews](https://www.coursera.org/learn/claude-code-in-action/reviews)
- 練習場: プロンプトチュートリアルの「Example Playground」と演習、解答キー — [gitlink ミラー](https://www.gitlink.org.cn/mirrors/prompt-eng-interactive-tutorial)。DeepLearning.AI は「Prompts & Summaries of Lessons」という読み物で、講座内で使ったプロンプトを再利用できる形で配布している — [DeepLearning.AI](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)。Willison は「Prompts I use」章を設けている — [simonwillison.net/guides](https://simonwillison.net/guides)
- 図とクイズ: Ultimate Guide の Mermaid 図48点(ASCII フォールバック付き)、473問クイズ、57枚のリキャップカード、Golden Rules — [README](https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/693d97d284ea342c8c8fb13894df0cee26d3a3d3/README.md)
- 時間とレベルの表示: claude-howto はモジュールごとにレベルと所要時間を示す — [claude-howto](https://cdn.jsdelivr.net/gh/luongnv89/claude-howto@main/README.md)。平川本は章タイトルに「5分 / 30分 / 半日」の成果物時間を入れる — [gihyo.jp](https://gihyo.jp/book/2025/978-4-297-15275-8)
- 章末のまとめ: Oikon 本の「まとめ:制御レイヤーの整理」「まとめ:4つの拡張機能を組み合わせる」 — [丸善ジュンク堂](https://www.maruzenjunkudo.co.jp/products/9784815643119)
- 失敗パターン、テンプレート集、チェックリスト: 近刊 SB 本(書名未確定)の「よくある失敗パターンと対処法」「シーン別プロンプトパターン集」「プロジェクトタイプ別 CLAUDE.md テンプレート集」「導入前の12項目」 — [丸善ジュンク堂](https://www.maruzenjunkudo.co.jp/products/9784815646813)
- 逆引きの見出し: ML_Bear の「〜したい」形式 — [Zenn](https://zenn.dev/ml_bear/articles/84e92429698177)。ClaudeLog の疑問形 FAQ スラッグ — [ClaudeLog](https://claudelog.com/llms.txt)
- 1枚もの: 公式の日本語チートシート(用語集・コマンド・ショートカットの3つの表) — [support.claude.com](https://support.claude.com/ja/articles/14553413-claude-code-チートシート)

### Inferences
- 本リソースのエントリテンプレートには、公式の比較列(読込タイミング / コンテキストコスト / 決定論性 / 使う場面 / 例)をそのまま属性として持たせ、そこに「Instead of / Try」と「旧 Tips の撤回」欄を加えるのが効果的と考えられる。
- 判断支援は、厳密なフローチャートより「トリガー(回数の閾値付き)→ 機能」と「こうしていたら → こちらへ」というシナリオ型の方が公式と整合しやすく、保守もしやすい。
- 「注釈付きセッション記録」は既存教材にほとんどない(下記 Gaps)ので、むしろ差別化の機会になる(推論)。

### Gaps
- 「注釈付きセッション記録」を中心に据えた教材や、それが評価されているという証拠は見つからなかった(Willison の「Linear walkthroughs」は、エージェントにコードの解説を書かせるパターンで、セッション記録の注釈とは別物)。
- 判断フローチャート系ブログ(Towards AI「Skills vs Subagents vs Hooks vs Workflows」など)は取得に失敗するか、検索上限のため本文を確認できていない。
- 提示手法の効果を測った定量的な研究(学習効果の比較など)は見つからなかった。

---

## 7. 統合: 教材比較表、(a) ほぼ全教材が扱うトピック、(b) ほとんど扱われないトピック(ギャップ)、(c) 採用すべき提示手法

### Takeaway
既存教材はほぼすべてが「導入 → CLAUDE.md → コンテキスト管理 → 計画 → MCP / サブエージェント / Hooks / Skills → GitHub/CI」という機能中心の線形構成をとる。不足しているのは次の5つ。(1) 症状・問題から引く索引、(2) 出力の検証(Discernment)と無人実行の信頼性、(3) 陳腐化した Tips の管理(検証日・撤回)、(4) 失敗パターンやアンチパターンの体系、(5) 日本の現場固有の事情(日本語での指示、社内セキュリティ規程)。

### Cited Findings
**教材比較表**(各セルの根拠は第1〜6問の該当箇所)

| 教材 | 発行/更新 | 形式 | レベル | 構成の特徴 | 強み | 弱み |
|---|---|---|---|---|---|---|
| Claude Code 101(Anthropic) | 2026時点 | 動画+クイズ | 入門 | 仕組み→explore-plan-code-commit→コンテキスト→CLAUDE.md→Subagents→Skills→MCP→Hooks | 公式、メンタルモデル(agentic loop / context / tools / permissions)を最初に置く | 所要時間・レベルの明示がない([Skilljar](https://anthropic.skilljar.com/claude-code-101/469795)) |
| Claude Code in Action(Anthropic、2026年版) | 2026改訂 | 動画9+演習31 | 中級 | Steer→Configure→Automate→Verify | 判断型の演習、検証を独立した章として扱う([DataCamp](https://www.datacamp.com/ja/courses/claude-code-in-action)) | 改訂で旧URL・旧レビューとずれている、AI採点への不満([Scrimba](https://scrimba.com/articles/best-claude-code-tutorials-and-courses-in-2026/); [Coursera](https://www.coursera.org/learn/claude-code-in-action/reviews)) |
| Building with the Claude API | 2026時点 | 84レッスン・8.1時間 | 中級(要 Python) | API→評価→プロンプト→Tool use→RAG→機能→MCP→Agents | 評価(evals)を早い段階で教える([Skilljar](https://anthropic.skilljar.com/claude-with-the-anthropic-api/287753)) | Claude Code の扱いは1章のみ |
| AI Fluency F&F / for Builders | 2025〜 | 1.1時間・14レッスン | 全レベル | 4D 順 | 能力の枠組み、Description-Discernment ループ([Skilljar](https://anthropic.skilljar.com/ai-fluency-framework-foundations)) | ツール操作は扱わない |
| Prompt Eng. Interactive Tutorial | 2024〜 | Notebook+Playground+解答 | 初〜上級 | 9章+付録 | 演習と Playground([gitlink](https://www.gitlink.org.cn/mirrors/prompt-eng-interactive-tutorial)) | API・単発プロンプト前提(Claude 3 Haiku)([courses](https://docsearch.algolia.com/mcp/docs/repo/anthropics/courses)) |
| Claude Code ドキュメント | 週次更新 | リファレンス+横断ページ | 全レベル | Getting started / Build / Config / Reference など | 比較表、トリガー表、Before/After、旧 Tips 撤回表、シミュレータ([features](https://code.claude.com/docs/en/features-overview); [best practices](https://code.claude.com/docs/en/best-practices)) | プロジェクト型の学習がない、分量が多い([Scrimba](https://scrimba.com/articles/best-claude-code-tutorials-and-courses-in-2026/)) |
| DeepLearning.AI Claude Code | 2026-08-17更新 | 動画+クイズ | 中級 | 3プロジェクト駆動 | 実プロジェクト、プロンプト集付き([DLAI](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)) | 機能の網羅性・判断支援は薄い(推論) |
| Educative Claude Code | — | テキスト+エディタ | — | 5モジュール | AI Tutor([Educative](https://www.educative.io/courses/claude-code)) | 詳細不明 |
| YouTube ロードマップ | 2026-10-25 | 動画20本 | 初〜上級 | 4段階 | 無料・長尺([Developer Educators](https://developereducators.com/roadmap/claude-code/)) | 「作って売る」寄り、内容がばらつく |
| Agentic Engineering Patterns(Willison) | 2026-02〜 | Web ガイド16章 | 中〜上級 | パターン名の章立て+アンチパターン章 | ツール非依存、テスト中心([Willison](https://simonwillison.net/guides)) | Claude Code の機能リファレンスはない |
| 実践Claude Code入門(技評) | 2025-12-26 | 書籍304ページ | 実務者 | 2部(ハンズオン/原理と体系化) | スペック駆動開発、動作原理([gihyo](https://gihyo.jp/book/2026/978-4-297-15354-0)) | 入門者には重い([DotAI](https://dot-ai.myuuu.co.jp/times/108)) |
| AI駆動開発入門(技評、平川) | 2025-12-05 | 書籍320ページ | 入門 | 成果物時間付きの章 | すぐ体験できる、付録のコマンド一覧と索引([gihyo](https://gihyo.jp/book/2025/978-4-297-15275-8)) | 一部情報が古い([DotAI](https://dot-ai.myuuu.co.jp/times/108)) |
| Claude Code実践入門(SB、Oikon・前川) | 2026-08-14 | 書籍・全7章 | 入門〜組織導入 | 使う→制御→拡張→現場→企業 | 制御と拡張の整理、コスト、エンタープライズ([丸善ジュンク堂](https://www.maruzenjunkudo.co.jp/products/9784815643119)) | 紙ゆえの陳腐化(推論) |
| テクニック集(齊藤) | 2026-05〜08 | 書籍522〜528ページ | 中級 | 機能別15章 | 辞典的([クリスタルメソッド](https://crystal-method.com/blog/claude-code-books/)) | 機能から引く構成で、症状からは引けない(推論) |
| Agent Skills入門(技評、佐藤) | 2026-06-08 | 書籍272ページ | 実務 | スキル特化・公式スキルのカタログ | skill-creator、配布、セキュリティ([gihyo](https://gihyo.jp/book/2026/978-4-297-15698-5)) | 対象範囲が狭い |
| 1週間で基礎(インプレス) | 2026-09-25 | 書籍360ページ | 非エンジニア入門 | 7日間 | ターミナル不要([koubo](https://koubo.jp/press-release/prtimes/c5875_r7683)) | Pro 前提 |
| Agentic Coding with Claude Code(Packt) | 2026-03-27 | 書籍376ページ | 開発者 | Context Engineering から始める | 概念の土台([Packt](https://www.packtpub.com/product/agentic-coding-with-claude-code/9781806022595)) | — |
| Beyond Vibe Coding(O'Reilly) | 2025-08 | 書籍254ページ | 開発者 | 70%問題→信頼と自律 | 生成コードのレビューと所有([O'Reilly](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749)) | ツール非依存 |
| Ultimate Guide(Bruniaux) | 2026-07-29 | GitHub/Web | 全レベル・ロール別 | 学習パス+クイズ+図+テンプレート | 図48点、クイズ473問、脅威DB([README](https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/693d97d284ea342c8c8fb13894df0cee26d3a3d3/README.md)) | 巨大、数値の不整合 |
| claude-howto | 2026-10-26 | GitHub | 5段階 | 10モジュール+時間 | レベル・時間・自己評価([claude-howto](https://cdn.jsdelivr.net/gh/luongnv89/claude-howto@main/README.md)) | 機能順(推論) |
| ClaudeLog | 継続 | Web | — | Mechanics / FAQ 230+ / Add-ons | 疑問形 FAQ([ClaudeLog](https://claudelog.com/llms.txt)) | メタデータが構造化されていない(推論) |
| 逆引きコマンド事典(Zenn) | 2025-06-23 | 記事 | — | 「〜したい」一問一答 | 逆引き形式([Zenn](https://zenn.dev/ml_bear/articles/84e92429698177)) | 1記事規模、更新が止まっている可能性(推論) |

**(a) ほぼ全教材が扱うトピック**(上の教材の目次を横断して確認)
- インストールと初期設定、プラン・料金(CC101、平川本、Oikon 本、1週間本、Shipyard)
- CLAUDE.md / メモリ(CC101、in Action、全日本語書籍、Ultimate Guide、claude-howto)
- コンテキスト管理(/clear、/compact、コンテキストウィンドウ)(CC101、旧 in Action、平川本4章、Oikon 本2章、齊藤本2章、箕輪本3章)
- 計画してから実装する流れ(Plan Mode / explore-plan-code-commit / スペック駆動)(CC101、in Action、西見本、Packt 6章)
- MCP(ほぼ全教材)
- サブエージェント / マルチエージェント(CC101、Intro to Subagents、平川本、Oikon 本、齊藤本、Packt)
- Hooks(CC101、in Action、DLAI、平川本、Oikon 本、齊藤本)
- Skills(2026年以降の教材すべて: CC101、in Action、DLAI Skills、佐藤本、Oikon 本、齊藤本、Packt 9章)
- GitHub Actions / CI / PR レビュー(in Action、DLAI、西見本5章、Oikon 本5章、齊藤本11章、Packt 5章)
- Plugins(2026年の教材: in Action、Oikon 本、齊藤本、Packt 4章)

**(b) ほとんど扱われないトピック(ギャップ)**
- **症状・問題から引く索引**: 先行例は Zenn の逆引き記事1本([Zenn](https://zenn.dev/ml_bear/articles/84e92429698177))と、公式 Best practices 冒頭の症状対応・トリガー表([Best practices](https://code.claude.com/docs/en/best-practices); [features](https://code.claude.com/docs/en/features-overview))程度。
- **出力の検証と無人実行の信頼性**: 正面から章を立てているのは in Action の「Verify and Share」、AI Fluency for Builders の「Discernment for code」、Willison のテスト系の章、Osmani の「Review, Refine, Own」に限られる([DataCamp](https://www.datacamp.com/ja/courses/claude-code-in-action); [Skilljar Builders](https://anthropic.skilljar.com/ai-fluency-for-builders); [Willison](https://simonwillison.net/guides); [O'Reilly](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749))。無料教材はテスト・セキュリティスキャン・CI・デプロイを飛ばしがちとの指摘もある([Scrimba](https://scrimba.com/articles/best-claude-code-tutorials-and-courses-in-2026/))。
- **陳腐化の管理(撤回された Tips、検証日)**: 明示しているのは公式の「What you can stop doing」表だけ([Best practices](https://code.claude.com/docs/en/best-practices))。書籍やコースの陳腐化はレビューで指摘されている([Coursera](https://www.coursera.org/learn/claude-code-in-action/reviews); [DotAI](https://dot-ai.myuuu.co.jp/times/108))。
- **失敗パターン / アンチパターンの体系**: 散発的にしかない(Intro to Subagents のアンチパターン、Willison のアンチパターン章、近刊 SB 本の「よくある失敗パターン」)([pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude); [Willison](https://simonwillison.net/guides); [丸善ジュンク堂](https://www.maruzenjunkudo.co.jp/products/9784815646813))。
- **非エンジニア業務での Claude Code 活用と、社内セキュリティ規程への対処**: みのるん式本、CC for Everyone、1週間本など少数([クリスタルメソッド](https://crystal-method.com/blog/claude-code-books/); [Scrimba](https://scrimba.com/articles/best-claude-code-tutorials-and-courses-in-2026/))。
- **エージェント時代のプロンプト**: 公式のプロンプト教材は API・単発チャット前提の旧世代(Claude 3 Haiku)([courses](https://docsearch.algolia.com/mcp/docs/repo/anthropics/courses))。エージェントへの指示の仕方は Best practices の数行と Oikon 本2章程度。

**(c) 採用すべき提示手法**(第6問の Cited Findings を参照)
- 共通の比較列を持つ「X vs Y」比較表(読込タイミング / コンテキストコスト / 決定論性 / 使う場面 / 例)
- 回数の閾値付きの「トリガー → 機能」表(逆引き索引の原型)
- 「Instead of / Try」の Before/After プロンプト
- 「旧 Tips / 撤回理由」表(検証日・対象バージョン付き)
- コンテキストウィンドウのタイムライン図(静的な図でもよい)と「コンパクション後に残るもの」
- 「X か Y か」型の判断クイズ(in Action の演習名の形式)
- レベルと所要時間の表示、章末の「まとめ: レイヤーの整理」
- 再利用できるプロンプト集とテンプレート集(DLAI の「Prompts & Summaries」、近刊 SB 本の付録)
- 疑問形・欲求形の見出し(「〜したい」「〜とは」)

### Inferences
- 本リソースの差別化ポイントは次の4つになる(推論)。(1) 症状から引く逆引き索引を一級市民として扱う。(2) すべてのエントリに検証日・対象バージョン・撤回フラグを持たせる。(3) レベルを自律度(委任の段階)で、能力タグを 4D で付ける。(4) 公式の比較軸(決定論性・コンテキストコスト・読込タイミング)を全機能エントリの共通属性にする。
- 公式ドキュメントは日本語訳されているが、判断表は数行規模にとどまる。これを日本語の現場の症状語彙(「指示を無視される」「毎回同じことを説明している」「会話が長くなると精度が落ちる」など)で大幅に拡張する余地がある(推論)。

### Gaps
- 日本語 Udemy 講座、未取得の日本語書籍4冊の目次、判断フローチャート系ブログの本文は、検索上限のため確認できていない。
- (a)(b) の判定は、取得できた目次レベルの情報に基づく。本文でどこまで深く扱っているかは検証していない。
