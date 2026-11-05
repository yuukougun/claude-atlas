---
id: change-timeline-2026
title: 2026 年の主な変更の年表
nav_title: 2026 年の変更の年表
aliases: [変更の記録, 年表, 2026 年の変化, リリースの歴史, 改名の時期]
type: ledger
field: changes
chapter: 台帳と年表
order: 20
priority: 推奨
surfaces: [app, claude-code, api]
summary: 2026 年のアプリ・Claude Code・モデル・API の主な変更を、日付と版付きで時系列に引ける。統合・自律の既定化・effort 中心の制御という流れも分かる。
signs:
  - {type: goal, text: いつ何が変わったかを時系列で知りたい}
  - {type: situation, text: しばらく使っていない間の変化に追いつきたい}
prerequisites: []
related: [outdated-advice-ledger, term-index, checking-for-updates, dating-information, default-safety-settings]
sources: []
volatility: 高
sections:
  - {title: この年の変化の流れ, anchor: trends}
  - {title: 年表, anchor: timeline}
  - {title: 年表の読み方, anchor: how-to-read}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：2026 年のアプリ・Claude Code・モデル・API の主な変更を、日付と版付きで時系列に引ける。
    - **いつ引くか**：いつ何が変わったかを時系列で知りたいとき、しばらく使っていない間の変化に追いつきたいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：変更の記録・年表・2026 年の変化・リリースの歴史・改名の時期
<!-- textlint-enable -->

2026 年の主な変更の年表は、この年にアプリ・Claude Code・モデル・API で起きた変更を、日付と版を添えて時系列に並べたページである。行は道具が数値ファイルの日付と版から作るので、手で書き足さない。先に流れを 3 つ読み、次に表で個別の変更を引く。

## この年の変化の流れ {#trends}

この年の変更は、統合・自律の既定化・effort 中心の制御という 3 つの流れにまとめて読める。個々の変更を覚える前に、どの流れの一部なのかを押さえると、記事や本の助言が今も通じるかを判断しやすい。

- **統合**：別々だった入口や機能が、1 つの仕組みにまとまった。アプリでは、Chat と Cowork が 1 つの会話になり、「Cowork は別アプリ」という前提が崩れた（<!-- link:begin outdated-advice-ledger#cowork-separate-app -->[古くなった助言の台帳](outdated-advice-ledger.md#cowork-separate-app)<!-- link:end -->）。Claude Code では、カスタムコマンドの置き場がスキルに寄った（<!-- link:begin outdated-advice-ledger#commands-directory -->[古くなった助言の台帳](outdated-advice-ledger.md#commands-directory)<!-- link:end -->）。「作り方」を説明した古い記事は、この統合で多くが外れた。
- **自律の既定化**：許可を毎回尋ねる運用から、権限の自動判定（auto mode）を最初から使う運用へ移った。既定になる範囲は、プラン、対話のターミナルと VS Code、`-p` と SDK の順に、段階を踏んで広がった。「最初は毎回承認を求められる」という前提は古くなった（<!-- link:begin outdated-advice-ledger#approve-everything-first -->[古くなった助言の台帳](outdated-advice-ledger.md#approve-everything-first)<!-- link:end -->）。任せる幅が広がるほど、守りを先に確かめる必要がある。自動判定は分類器による判定で、誤ることがある。既定がどこまで効くかは <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end --> で確かめる。`-p` と SDK では、承認が要る呼び出しを認める手段がなければ拒否されるようになった。自動化の手順を書くときは、この挙動を前提にする。
- **effort 中心の制御**：考える量を、キーワードや思考の予算の指定ではなく、effort で決める流れになった。think や think hard は、考える量を変えるキーワードとしては扱われず、普通の文として渡る（<!-- link:begin outdated-advice-ledger#think-hard-keywords -->[古くなった助言の台帳](outdated-advice-ledger.md#think-hard-keywords)<!-- link:end -->）。ultrathink は、そのターンだけ深く考えるよう頼む言葉として残り、効く範囲が段階的に広がった。API でも、思考の量は `budget_tokens` ではなく effort で決める方向に置き換わった（<!-- link:begin outdated-advice-ledger#budget-tokens -->[古くなった助言の台帳](outdated-advice-ledger.md#budget-tokens)<!-- link:end -->）。

3 つの流れの下には、台帳に共通する規則がある。利用者が手作りしていた回避策（自作のループ、tmux での組織づくりなど）は、同じ働きの正式な仕組みが入ると歴史になる。この規則は <!-- link:begin dating-information#workarounds -->[いつの情報かを見分ける › 回避策は正式な仕組みに置き換わる](dating-information.md#workarounds)<!-- link:end --> にまとまっている。年表で「入った」と読める変更は、どれかの回避策を置き換えた可能性がある。

## 年表 {#timeline}

次の一覧は、日付の古い順に、名前の変更と、古くなった助言の変わった時期を並べたものである。行の形は 2 つある。「旧名 → 今の名前」の行は改名や置き換えで、「助言 → 今どうするか」の行は台帳の行へのリンクが付く。日付が「A〜B」の行は、変更が A から B にかけて段階的に進んだことを表す。版が付く行は Claude Code の変更で、付かない行はアプリや API などの変更である。

<!-- gen:begin timeline -->
<!-- textlint-disable -->

- 2025-03-26：[MCP を SSE transport でつなぐ](outdated-advice-ledger.md#mcp-sse-transport) → リモートの MCP サーバーは HTTP（Streamable HTTP）でつなぐ（claude mcp add --transport http）。2.1.265 以上は、SSE しか出していないサーバーにも HTTP を先に試してから SSE に切り替える。SSE を直接指定するのは、古い版のときか、HTTP を受け付けないサーバーのときだけ。
- 2025-06-02・Claude Code 1.0.7：/allowed-tools → /permissions（[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)）
- 2025-06-16・Claude Code 1.0.25：/project:&lt;名前&gt;・/user:&lt;名前&gt; → /&lt;名前&gt;（サブディレクトリのファイルは /&lt;フォルダ&gt;:&lt;名前&gt;）（[スキルの作り方](../extend/writing-skills.md)）
- 2025-08-26：[GitHub Action を @beta と direct\_prompt で書く](outdated-advice-ledger.md#action-beta-direct-prompt) → anthropics/claude-code-action@v1 を使い、direct\_prompt は prompt に、max\_turns や model などの CLI の設定は claude\_args に移す。mode の入力は外す（自動で判定する）。custom\_instructions は claude\_args の --append-system-prompt になる。
- 2025-09-29・Claude Code 2.0.0：Claude Code SDK・claude-code-sdk（Python のパッケージ） → Claude Agent SDK（[Agent SDK（Claude Code をライブラリとして使う）](../api/agent-sdk-basics.md)）
- 2025-12-15・Claude Code 2.0.70：[「#」で始めると CLAUDE.md に記憶される](outdated-advice-ledger.md#hash-to-memorize) → CLAUDE.md に足したいことは、Claude に CLAUDE.md の編集を頼むか、/memory でファイルを開いて自分で書く。セッションの中で学んだことは、自動メモリが書き残す。
- 2026-01-09・Claude Code 2.1.3：[.claude/commands/ にカスタムコマンドを作る、/project:name 記法](outdated-advice-ledger.md#commands-directory) → 新しく作るものはスキル（.claude/skills/&lt;名前&gt;/SKILL.md）にする。.claude/commands/ のファイルも今も同じように動き、同じ名前のスキルがあればスキルが優先される。名前に project: や user: は付けず /&lt;名前&gt; で呼ぶ（サブディレクトリのファイルは /&lt;フォルダ&gt;:&lt;名前&gt;）。
- 2026-02-05：[budget\_tokens で思考量を指定する](outdated-advice-ledger.md#budget-tokens) → thinking の type を adaptive にし、深さは effort で決める。Claude 4.7 以降のモデルは、budget\_tokens を使う要求を 400 エラーで断る。Opus 4.6 と Sonnet 4.6 では非推奨。手動の思考しか持たないモデル（Opus 4.5・Haiku 4.5 など）は今のままでよい。
- 2026-02-05〜2026-04-20：[公式インタラクティブチュートリアルが最新の作法](outdated-advice-ledger.md#interactive-tutorial) → 基本の考え方の練習には使えるが、Claude 3 のモデル向けに書かれているので、食い違うところは Prompting best practices に従う（公式の文書もそう書く）。第 5 章の prefill（Speaking for Claude）は、Claude 4.6 以降のモデルで 400 エラーになる。temperature を 0 にする呼び方は、Claude 4.7 以降のモデルで、または API の版 2026-10-21 で、400 エラーになる。
- 2026-02-05：[prefill で JSON の形を強制する](outdated-advice-ledger.md#prefill-for-json) → structured outputs（JSON の出力か strict tool use）で形を保証する。まず形を指示に書き、検査して再試行する手もある。分類なら、ラベルを enum にした道具か structured outputs を使う。Claude 4.6 以降のモデルは、最後の assistant のターンを先に書いた要求を 400 エラーで断る。
- 2026-02-05〜2026-05-11・Claude Code 2.1.32：[tmux で自作のエージェント組織を作る](outdated-advice-ledger.md#tmux-agent-orgs) → 背景のセッションをまとめて見るなら agent view（claude agents。research preview）を使う。リードがチームメイトに仕事を振って調整するなら、エージェントチーム（experimental。CLAUDE\_CODE\_EXPERIMENTAL\_AGENT\_TEAMS を 1 にして有効にする）を使う。どちらも使う量が増えるので、まずサブエージェントやセッションの間のメッセージで足りないかを確かめる。
- 2026-03-04・Claude Code 2.1.68：[think → think hard → ultrathink の段階、日本語の「熟考」](outdated-advice-ledger.md#think-hard-keywords) → think・think hard・think harder・「熟考」・「よく考えて」と書いても、effort は上がらない。これらはキーワードとして扱われず、effort の範囲で少し後押しするふつうの文として渡る。考える深さは effort（/effort・--effort・設定）で決める。ultrathink だけは、そのターンだけ深く考えるよう頼む言葉として認識され、セッションの effort は変えない。Claude Code が Anthropic の API で Opus 5.5・Sonnet 5.5・Haiku 5.5・Fable 5.1 を使うときは、ultrathink のターンを xhigh で動かす。この動きは、対話のターミナル（2.1.311 以上）と VS Code（2.1.316 以上）で働く。CLAUDE\_CODE\_DISABLE\_ULTRATHINK（2.1.316 以上）で切れる。
- 2026-03-17・Claude Code 2.1.77：/fork → /branch（今の /fork は、会話を新しい背景のセッションに写す別の機能）（[セッションに名前を付けて再開・分岐する](../cli/resume-and-branch.md)）
- 2026-03-17・Claude Code 2.1.77：[/fork で会話を分岐する](outdated-advice-ledger.md#fork-to-branch) → 会話を分けて別の方向を試すのは /branch。今の /fork は、会話を新しい背景のセッションに写し、元の会話を続ける別の機能（2.1.212 から）。
- 2026-04-02〜2026-09-18：[/vim・/tag・/pr-comments・ultraplan・TaskOutput ツールを使う](outdated-advice-ledger.md#removed-commands) → どれも消えた。/pr-comments（2.1.91）の代わりは、PR のコメントを Claude に直接頼んで読ませること。/vim（2.1.92）の代わりは、/config の Editor mode で Vim の操作を切り替えること。/tag（2.1.92）の代わりの案内は文書にない。ultraplan（2.1.222）の代わりは plan mode。TaskOutput ツール（2.1.83 から非推奨、2.1.277 で削除）の代わりは、Claude が Read でその出力のファイルを読むこと。
- 2026-04-04・Claude Code 2.1.92：/vim → /config の Editor mode（Vim と Normal の切り替え）（[入力の記号（/ ! @）と Esc](../cli/input-symbols.md)）
- 2026-04-23・Claude Code 2.1.118：/cost・/stats → /usage（[/usage・/context・ステータスラインで状態を見る](../cli/usage-context-statusline.md)）
- 2026-04-23・Claude Code 2.1.118：[/cost・/stats で使用量を見る](outdated-advice-ledger.md#slash-cost-and-stats) → /usage で見る。/cost と /stats は今も打てる別名で、/usage の該当のタブを開く。
- 2026-05-11〜2026-05-28・Claude Code 2.1.139：[プラグインや自作の bash ループで回し続ける](outdated-advice-ledger.md#ralph-loops) → 完了の条件を決めて続けさせるなら /goal、決まった間隔でくり返すなら /loop、大きな作業を多くのエージェントに分けるなら dynamic workflows を使う。無人で回すときは、止まる条件と使う量の上限を先に決める。
- 2026-05-19・Claude Code 2.1.144：extra usage・/extra-usage → usage credits（/usage-credits）（[usage credits（上限を超えた分の従量課金）](../cost/usage-credits-basics.md)）
- 2026-06-01：[スタイル（Styles）で応答の調子と形式を切り替える](outdated-advice-ledger.md#styles-for-tone) → いつも同じ調子にするなら、全会話に効く Claude への指示（設定の Instructions）に書く。場面ごとに切り替えるならスキルにする。自分で作ったスタイルは移行でスキルになり、名前から作られるスラッシュコマンド（/&lt;名前&gt;-style）で呼ぶ。既定の Learning はスキルとして残った。
- 2026-06-02・Claude Code 2.1.160：workflow（起動のキーワード） → ultracode（dynamic workflows を起動するキーワード）（[dynamic workflows（スクリプトで多数のサブエージェントを動かす）](../delegate/dynamic-workflows.md)）
- 2026-06-02・Claude Code 2.1.160：[「workflow」と書いて workflows を起動し、超過分は extra usage で払う](outdated-advice-ledger.md#workflow-keyword-extra-usage) → dynamic workflows を 1 つの作業で使うなら、プロンプトに ultracode と書くか、「ワークフローで」と自分の言葉で頼む（workflow という語だけでは起動しない）。セッション全体なら /effort ultracode にする。上限を超えた分は usage credits（/usage-credits）で払う。
- 2026-06-09：[&lt;thinking&gt; タグに推論を書かせる](outdated-advice-ledger.md#thinking-tags) → 推論を見たいときは、応答の本文に書かせず、thinking のブロックを読む（display を summarized にして要約を受け取る）。根拠が要るなら、短い説明を頼む。Fable 5・Opus 5・Sonnet 5.5・Opus 5.5・Fable 5.1 では、内部の推論を本文に書かせる頼み方は reasoning\_extraction として断られることがある。
- 2026-07-01・Claude Code 2.1.198：[/agents でサブエージェントを作る](outdated-advice-ledger.md#agents-command) → Claude にサブエージェントを作らせるか直させる（どこに置き、何をさせ、どの道具を許すかを頼む）。または .claude/agents/ か ~/.claude/agents/ の Markdown を直接書く。今の /agents は、このやり方を知らせる文を出すだけになった。
- 2026-07-03・Claude Code 2.1.200：default モード（表示の名前） → Manual（権限モード。設定の値は default のまま）（[権限モードの選び方](../cli/permission-modes-overview.md)）
- 2026-07-03〜2026-07-06：--remote → --cloud（[クラウドセッションと teleport](../cli/cloud-sessions-and-teleport.md)）
- 2026-07-10：[メモリは会話の後に日次で要約される](outdated-advice-ledger.md#memory-daily-summary) → 今のメモリは、話している間に Claude がトピックごとの項目として保存し、読み、更新する（「覚えて」と頼んで保存させることもできる）。覚えたことは設定の Topics で見て、直し、消せる。
- 2026-07-24：[「最後に double-check して」と書き足す](outdated-advice-ledger.md#add-double-check) → 確かめる手段（テスト・型の検査・照らす基準）を渡す。Opus 5 は自分の作業を言われなくても確かめるので、「見直して」「double-check して」や、確かめ役のサブエージェントを使わせる指示は消す（確かめすぎでトークンと時間が増える）。Opus 5.5 の公式の手引きは、Opus 5 の頼み方を出発点として使えるとするので、同じ扱いから始め、自分の作業で比べる。ほかのモデルでは、終わる前に基準と照らして確かめるよう頼むのは今も効く。
- 2026-07-24〜2026-10-27：[工程ごとにサブエージェントを大量に作る](outdated-advice-ledger.md#subagent-per-step) → サブエージェントは、文脈を分ける意味のある作業に使う：本筋に残したくない長い出力（すべてのテストの実行や広い検索）、並べられる独立の作業、書く過程を見ていないレビュー、道具を絞った役。小さな作業は本体で済ませる。新しいサブエージェントは文脈を集め直すので、かえって遅くなることもある。
- 2026-07-24〜2026-10-27：[「subagent を使え」と書き足す](outdated-advice-ledger.md#tell-it-to-use-subagents) → 書き足さない。サブエージェントに任せるのは、大きく、本当に独立していて並べられる作業だけにする。同じ作業をサブエージェントに渡しても答えはよくならない（よくなるのは、書く過程を見ていない別のレビューを頼むとき）。Claude Code では CLAUDE\_CODE\_MAX\_SUBAGENT\_SPAWN\_DEPTH と CLAUDE\_CODE\_MAX\_CONCURRENT\_SUBAGENTS で数を縛れる。
- 2026-08-03：Claude in Slack → Claude Tag（周辺製品の一覧（準備中））
- 2026-08-06・Claude Code 2.1.223：/review → /code-review（[書いた本人ではない者にレビューさせる](../verify/independent-review.md)）
- 2026-08-14〜2026-09-28・Claude Code 2.1.283：[最初は毎回承認を求められる](outdated-advice-ledger.md#approve-everything-first) → 何も設定していなければ、ターミナルと VS Code の対話のセッションは auto モードで始まる（2.1.283 以上）。毎回確かめたいなら、permissions.defaultMode を default（表示は Manual）にするか、--permission-mode manual で起動する。claude -p と Agent SDK は、決めていなければ Manual で動く。
- 2026-08-14〜2026-09-28：[--dangerously-skip-permissions で YOLO 運用](outdated-advice-ledger.md#yolo-skip-permissions) → ふだんの対話は auto モード（今の既定）にし、サンドボックスを重ねる。bypassPermissions（--dangerously-skip-permissions と同じ）は、使い捨てのコンテナや VM の中だけで使う。permissions.blockWritesOutsideWorkingDirectories（2.1.314 以上）は、bypass でも Write・Edit・NotebookEdit が作業ディレクトリの外に書くのを止める。ただしシェルのコマンドは止めないので、隔離の代わりにはならない。
- 2026-08-17：[Console の prompt generator / improver を使う](outdated-advice-ledger.md#console-prompt-generator) → 公式の Prompting best practices を出発点にし、成功の基準と評価（eval）を決めて、変えた効果を測りながら直す。下書きを機械に作らせたいなら、公式の文書は Claude Cookbook の metaprompt のノートブックを案内している。
- 2026-08-18：Workbench → playground（Claude Console）
- 2026-09-10〜2026-09-17：Claude Code on the web → クラウドセッション（cloud sessions）（[クラウドセッションと teleport](../cli/cloud-sessions-and-teleport.md)）
- 2026-09-10〜2026-09-17：[Claude Code on the Web と --remote を使う](outdated-advice-ledger.md#code-on-the-web-remote) → 機能の名前はクラウドセッション（cloud sessions）。ターミナルからは、claude --cloud に頼む内容を付けて始める（--remote は非推奨の別名として今も動く）。ブラウザの claude.ai/code は、今も Claude Code on the web とも呼ばれる。
- 2026-09-16：[Cowork は別アプリ、Web search はトグルで入れる](outdated-advice-ledger.md#cowork-separate-app) → 新しい Claude の体験では、チャットと Cowork は 1 つの会話にまとまり、モードを選ばずに頼む。Web 検索のトグルはなく、Claude が要るときに自分で検索する。リサーチは /deep-research か「+」から選ぶ。体験は順に展開中で、入力欄に「Chat」と「Cowork」の選択が残るアカウントは、まだ前のやり方のまま。
- 2026-09-22・Claude Code 2.1.280：[Opus は高いので避ける](outdated-advice-ledger.md#avoid-opus-as-expensive) → 一律に避けず、自分の作業で比べて選ぶ。Opus 5.5 は Opus 5 より安く、Claude Code の Pro・Max・Ultra・Team・Enterprise と API で既定のモデル（2.1.280 以上）。プランでは、選ぶモデルで上限の減り方が変わるので、/usage で確かめる。
- 2026-10-20 ごろ：routines → クラウドの予定のタスク（cloud scheduled tasks）（[クラウドの定期タスク](../delegate/cloud-schedules.md)）
- 2026-10-20 ごろ：[routines で定期実行を作る](outdated-advice-ledger.md#routines-name) → 今の名前はクラウドの予定のタスク（cloud scheduled tasks）。claude.ai/code/routines か Desktop の Code タブ（Local と Cloud の選択が出たら Cloud）、CLI の /schedule で作る。一部の画面・URL・/routines の別名・API には旧名が残るが、同じ機能を指す。
- 2026-10-21：[temperature（や top\_p・top\_k）を下げて出力を安定させる](outdated-advice-ledger.md#lower-temperature) → 引数を送らず、指示で振る舞いを導く。API の版 2026-10-21 では、この 3 つを送ると、既定の値でも 400 エラーになる。それより前の API の版でも、Claude 4.7 以降のモデルは、既定以外の値で 400 エラーになる。既定以外の値を受け付けるモデル（Sonnet 4.6 など）を古い API の版で呼ぶときだけ、今も効く。API の版を上げると効き目がなくなり、代わりの設定はない。
- 2026-10-27・Claude Code 2.1.312：session limit → 5-hour limit（5 時間の上限）（[利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)）
- 2026-10-27 ごろ：[アーキテクチャやファイル構成を CLAUDE.md に書く](outdated-advice-ledger.md#architecture-in-claude-md) → Claude はリポジトリを自分で読むので、構成やファイルの並びは書かない。書くのは、リポジトリを読んでも分からないこと（推測できない理由・決まり・落とし穴）だけにする。
- 2026-10-27 ごろ：[IMPORTANT や YOU MUST で強調すれば守られる](outdated-advice-ledger.md#important-caps) → 強調せず、ふつうの言葉で書く。それでも守られないなら、ファイルが長すぎて埋もれていないかを見て短くするか、例外を許さない規則ならフックか deny ルールにする。強調を重ねると、Claude が規則を当てはめすぎる原因にもなる。
- 2026-10-27 ごろ：[「keep going」「don't be lazy」と書く](outdated-advice-ledger.md#keep-going-dont-be-lazy) → こうした一言は消す。今のモデルは合意した作業を言われなくても続け、この手の文はやりすぎの原因になりやすい。代わりに、通すべきテストのような確かめる手段を渡す。途中で止まったら continue と言い、誰も見ていない実行は /goal か Stop フックで続けさせる。
- 2026-10-27 ごろ：[200k を前提にコンテキストを最優先で節約する](outdated-advice-ledger.md#save-context-for-200k) → 今の多くのモデルは 1M トークンのコンテキストウィンドウを持ち、圧縮も自動なので、溢れることはまれになった。関係のない作業に移るときの /clear は、答えの質とコストのために今も勧められる。大きな会話（既定で 200K トークン以上）を 1 時間ほど放置すると、プロンプトキャッシュが切れる前に要約される（idle compaction）。ターミナルは 2.1.299、VS Code と Desktop の Code タブは 2.1.314 から働き、idleCompaction を false にするか /config で止められる。
- 2026-10-27 ごろ：[コンテキストを守るためにサブエージェントに調べさせる](outdated-advice-ledger.md#subagents-to-save-context) → 溢れることはまれになったので、守るためだけには使わない。サブエージェントが今も向くのは、並べる作業、うるさい出力を本筋から離すこと、独立したレビュー。どれもトークンが余分にかかる。
- 2026-10-29〜2026-11-30：「Customize」・「Customize」の「Skills」「Connectors」「Plugins」のタブ → 「Plugins」（サイドバー・チャットのメニュー・設定の名前と、1 つの「Plugins」のページ）（アプリでプラグインを使う（準備中））
- 2026-10-29〜2026-11-30：[Customize の「Skills」「Connectors」「Plugins」の各タブで管理する](outdated-advice-ledger.md#customize-tabs) → サイドバーの名前は「Plugins」に変わる途中で、変わった口座では 1 つの「Plugins」のページでプラグイン・スキル・コネクタを管理する（スキルとコネクタだけに絞り込める）。展開の途中なので、サイドバーに「Customize」が出る口座は、まだ前の画面（Skills・Connectors・Plugins の各タブ）のままである。スキルはチャットの「+」か「/」で使う。Team と Enterprise で「Skills」を切っている組織は、2026-11-30 から Desktop のプラグインも止まる。
- 2026-10-30：Max 20x → Ultra（[プランの選び方](../cost/choosing-a-plan.md)）
- 2026-10-30・Claude Code 2.1.314：Recently denied・Recent → Recently blocked（/permissions のタブ）（[auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)）
- 2026-10-30：[Max は 5x と 20x から選ぶ](outdated-advice-ledger.md#max-5x-or-20x) → 個人の上位のプランは Max と Ultra（旧 Max 20x）の 2 つ。Max は 5 時間ごとと週ごとの上限を持ち、Ultra は確認済みの口座なら 5 時間の上限がなく週の上限だけ。倍率と料金はプランのページで確かめる。
- 2026-10-30：[有料プランは 5 時間の上限に当たったら待つしかない](outdated-advice-ledger.md#wait-out-5-hour-limit) → 確認済みの Ultra の口座には 5 時間の上限がなく、週の上限だけ。ほかの有料プランは 5 時間と週の 2 段のまま。上限に当たったら、待つほかに、usage credits を有効にして続けるか、プランを上げる手がある。Claude Code（2.1.234 以上）は、開いたままのセッションで待ち、上限が戻ると自動で作業を続ける（続けるのは 3 回まで）。

<!-- textlint-enable -->
<!-- gen:end timeline -->

## 年表の読み方 {#how-to-read}

年表は時系列で変更を引く表で、「その助言を今どうするか」は書かない。変更に気づいたら、次の順に使い分ける。

- **助言を今どうするかを知りたい**：<!-- link:begin outdated-advice-ledger#ledger -->[古くなった助言の台帳 › 台帳](outdated-advice-ledger.md#ledger)<!-- link:end --> で、同じ変更の行を引く。台帳は状態（撤回・置換・条件付き）と、どの原理の回避策だったかを並べている。読み方は <!-- link:begin outdated-advice-ledger#how-to-read -->[古くなった助言の台帳 › 台帳の読み方（状態と、どの原理の回避策だったか）](outdated-advice-ledger.md#how-to-read)<!-- link:end --> にある。
- **旧名を今の名前に直したい**：<!-- link:begin term-index#old-names -->[用語索引と旧名の対応 › 旧名から引く](../start/term-index.md#old-names)<!-- link:end --> を引く。改名が起きた時期はこの年表に、旧名と今の名前の対応は用語索引に置く。
- **日付と版の癖を知りたい**：同じ変更でも、日付が情報源でずれることがある。たとえば、npm の公開日（UTC）と、docs の changelog の日付は一致しないことがある。版番号は連番ではなく、公開されなかった番号や、公開の後に取り下げられた版がある。「最後の番号から最初の番号を引いた数」は、リリースの数ではない。確かめ方は <!-- link:begin dating-information#check-date-and-version -->[いつの情報かを見分ける › 日付と版の確かめ方](dating-information.md#check-date-and-version)<!-- link:end --> にある。
- **この年の後の変更を知りたい**：この表は 2026 年の記録で、表に載っていない最近の変更は、自分で確かめる。手順は <!-- link:begin checking-for-updates -->[最新を自分で確かめる方法](checking-for-updates.md)<!-- link:end --> にある。
- **自分の設定や指示に古い書き方が残っているか調べたい**：<!-- link:begin outdated-advice-ledger#find-in-your-setup -->[古くなった助言の台帳 › 自分の設定や記事で見つける](outdated-advice-ledger.md#find-in-your-setup)<!-- link:end --> で点検する。

リリースノートに載らない変更（Help Center の記事や料金のページだけに書かれた変更）や、docs に遅れて入る変更がある。そのため、年表に行がないことは、変更がなかった証拠にならない。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [古くなった助言の台帳](outdated-advice-ledger.md)
- [用語索引と旧名の対応](../start/term-index.md)
- [最新を自分で確かめる方法](checking-for-updates.md)
- [いつの情報かを見分ける](dating-information.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
