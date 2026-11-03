# Claude公式機能・モデル・プロンプト指針・API概念の棚卸し（2026年10月時点）

> 調査担当範囲: claude.ai アプリ（web / desktop / mobile）機能、プラン・利用上限、モデルラインナップと選び方、Anthropic公式プロンプトガイダンス（モデル世代別を含む）、API / Agent SDK / Managed Agents の概念、限界とハルシネーション対策。
> 確認日: 全項目 2026-10-29（WebFetchで公式ページを取得した日）。Help Center記事の多くは発行日を出しておらず、「Updated this week」「Updated over 2 weeks ago」などの相対表記しかない。そのため各項目に「変わりやすさ」の注記を付けた。
> 出典は公式のみ: support.claude.com、platform.claude.com/docs、code.claude.com/docs、claude.com、anthropic.com、academy.claude.com。
> 制約: 調査の途中でWebSearchの上限（ターン共有の200回）に達したため、後半は既に見つかった公式URLの取得だけで進めた。未確認の項目は各 Gaps に書いた。

---

## 1. claude.ai アプリ機能（2026年に登場・変化したものを含む）

### Takeaway
2026年のアプリで一番大きな変化は、2026-09-16以降に「Chat」と「Cowork」が一つの会話に統合されたこと（ファイル作成、コード実行、タスク、スケジュール実行、Skills、Connectors をどの会話からでも使える）。もう一つは、Artifacts が Docs / Slides / Design / Dashboards / Motion という「テンプレート型」に作り直され、データ保存・Claude呼び出し・コネクタ連携を持つアプリ的な成果物になったこと。Memory は2026-07に「トピック単位の個別エントリ」方式へ変わった。教材は「機能名の暗記」ではなく、「Instructions / Project / Memory / Skills をどう使い分けるか」と「agentic な実行の安全な任せ方」を軸に組むのがよい。

### Cited Findings

#### 1-0. 2026年の主な変更年表（Help Center Release notes より）
- 2026-01-12 Cowork research preview（Max・macOS、隔離VMでローカル実行）。同日、HIPAA-ready Enterprise と、iOS/Android の健康・フィットネスデータ分析（Pro/Max、米国のみ）— [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-01-16 Cowork を Pro（macOS）へ拡大。Team Standard seat に Claude Code を同梱。Opus 4 / 4.1 をモデル選択から削除 — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-02-05 Claude for PowerPoint add-in 登場。Claude for Excel を Opus 4.6 へ更新（ピボットテーブル編集・条件付き書式）— [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-02-24/25 Cowork plugin marketplace と管理者向け制御。定期・オンデマンドの scheduled tasks。skills・plugins・connectors をまとめた「Customize」セクション — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-03-02 「チャット履歴からのMemory」が全ユーザー（Free含む）に開放 — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-03-11 Excel / PowerPoint add-in 間で会話コンテキストを共有。skills対応、LLM gateway経由のアクセスに対応 — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-03-12 チャット回答の中にインタラクティブなチャート・図・可視化を描画。2026-03-25 に mobile でも対応 — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-03-17 / 03-23 Cowork の持続エージェントスレッド（Desktop / mobile から管理）。Computer use の research preview（Pro/Max）と Dispatch の改善 — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-04-09 Cowork が macOS / Windows で GA — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-04-17 Claude Design（Anthropic Labs）登場 — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-06-12 ドラフトのその場編集（範囲を選び、横に変更内容を入力）— [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-06-23 Claude Tag（Slack で @Claude にタスクを任せる。Team/Enterprise）— [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-07-07 Cowork が web / mobile に拡大（Maxから先行。リモート実行はbeta）。同日、Microsoft 365 connector に書き込みツール（メール・カレンダー・OneDrive/SharePoint。Teamsは読み取りのみ）— [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-07-09 Monthly recap（beta、Settings > Reflect）と Time and focus（休憩リマインダー・quiet hours）— [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-07-10 Memory が「会話中にClaudeが更新するカテゴリ別の個別エントリ」へ移行し、日次サマリー方式を置き換えた — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-08-25 Memory が chat とクラウドの Cowork で共通化。トピックを編集でき、センシティブな話題を含めるかの設定も追加 — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-09-16 Cowork の機能をどの会話からも使えるようになった（Pro/Maxから展開）。同日、Claude Design / Slides / Docs をどの会話でも作れるようになり、artifacts が全プランで使えるようになった — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-09-25 plugin を Claude directory に提出するための Developer portal — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 2026-10-21 Claude Duet research preview（Pro/Max。能動的に動く別アプリ）— [Release notes](https://support.claude.com/en/articles/12138966-release-notes)

#### 1-1. 統合された Claude 体験（Chat と Cowork の一体化）
- 概要: Chat と Cowork が一つの会話にまとまり、どちらを使うか事前に選ぶ必要がなくなった。軽い質問にも、調査・レポート・表計算・プレゼン作成のような大きな作業にも Claude がツールを選んで対応し、成果物は編集可能なファイルとして返る — [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- 主な構成要素:
  - Tasks: 結果を伝えるとClaudeが手順を進める。複数のタスクを同時に走らせられる。
  - Cloud タスク: PCを閉じても続く。ローカルのファイルやアプリを使うタスクは Desktop を開いておく必要がある。
  - Desktop の出力は「Storage folder」に保存される。アクセスを許可したフォルダは「Trusted folders」に並ぶ。
  - Scheduled tasks はクラウドで動き、PCの電源が切れていても実行される。
  - mobile からタスクの監視・質問への回答・方向修正・開始ができる。
  - Recents には chat と task が一つのリストで並ぶ。
  — [同上](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- Research は `/deep-research` か「+」ボタン > Research で使う。Web search にトグルはなく、役に立つときにClaudeが自分で検索する — [同上](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- 権限モード: Pro/Max/Team の既定は **Auto**（各ステップで確認せずに進むが、事前に自動の安全チェックが走る）。Enterprise の既定は **Manual**（毎回確認）。設定は会話全体に効き、いつでも変更できる — [同上](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- 現時点の制約:
  - Add from GitHub が使えない。
  - 会話の途中からの分岐ができない。
  - Incognito は旧体験のままなので、ファイル作成やコード実行ができない。
  - 古い Cowork タスクは検索の対象外。
  - Dispatch は新規ユーザーには提供されない。
  — [同上](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- 展開状況: Pro/Max から先行（web / desktop / mobile）。Team は「Chat and Cowork unified」が有効な組織で beta。Enterprise も有効化された組織で利用できる。段階展開なので、同じプランでも見え方が違うことがある — [同上](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- 2026-10-06 以降、Pro/Max の新規タスクはクラウドで実行され、「Only on your computer」設定は廃止された（元に戻せない）— [Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
- surface ごとの差: ローカルファイル、ブラウザ操作、computer use は Desktop が開いていることが前提。ローカルの connectors / MCP は Desktop 専用。mobile は artifacts に非対応 — [同上](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
- 使いどころ/なぜ重要か: 多段の作業（調べる → 分析する → ファイルにまとめる）を一つの会話で任せられる。agentic なタスクは単純な質問よりかなり多く usage を使う — [同上](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- 確認日: 2026-10-29（記事は「Updated this week」。段階展開中なので変わりやすい）

#### 1-2. Projects（knowledge / instructions / project memory）
- 概要: 文脈を共有するチャットをまとめるワークスペース。全ユーザーが使え、Free は最大5個まで — [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- Project knowledge: アップロードした内容は、そのプロジェクト内のすべてのチャットで使われる。有料プランでは、knowledge が context window の上限に近づくと自動で RAG mode が有効になり、容量が広がる — [同上](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- Project instructions: プロジェクト内の全チャットに適用される — [同上](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- Project memory: プロジェクトごとに独立した memory を持つ。プロジェクト内では「そのプロジェクトの memory」と「プロジェクト外の account memory」を使い、他プロジェクトの memory は使わない。完全に分けたいときは「Use account memory」をオフにする — [同上](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- 共有（Team/Enterprise）: Can view（閲覧とチャットのみ）と Can edit（instructions・knowledge の編集も可）の2段階 — [同上](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- 公式の推奨: 繰り返し参照する主要な資料は最初に project にアップロードしておく。cache が効き、再利用時の usage 消費が少なくなる。ただし一定時間使わないと cache が切れ、全量カウントに戻る — [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- 確認日: 2026-10-29
- 注意: personalization の記事には「project instructions は有料プラン限定」とあり、Projects 記事の「Freeも5個まで作成可」と食い違っている（[Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)）。

#### 1-3. 個人設定: Instructions for Claude / Project instructions / Skills の使い分け
- Instructions for Claude（アカウント全体）: すべての会話に適用される。Settings > Your Claude（旧レイアウトでは Account）> Instructions。Cowork の Global instructions はここに統合された — [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)
- 公式の使い分け:
  - アカウント全体に効かせたい → Instructions for Claude
  - 特定プロジェクト向けの指示 → project instructions
  - 応答の形式や届け方 → skills
  — [同上](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)
- Styles: personalization 記事には Styles の記載がない。一方、Incognito 記事には「Incognito でもプロフィール情報（custom styles や preferences）は使われる」とあり、Styles 自体は残っているように読める — [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)
- 確認日: 2026-10-29

#### 1-4. Memory と過去チャット検索
- Chat search: 有料プランで使える（web / Desktop / mobile）。RAG を使った検索で、チャット上ではツール呼び出しとして表示される。「Search and reference chats」トグルでオフにできる — [Use Claude's chat search and memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Memory の現行方式: 会話後に要約するのではなく、話しながら個別のトピックとして保存していく。Claude が自分で保存するほか、「remember this」と頼んでも保存される。対象カテゴリは、役割とプロジェクト、仕事や生活に関わる人、コミュニケーションや技術面の好み、進行中プロジェクトの詳細 — [同上](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- 既定値: Free/Pro/Max は既定でオン。Team/Enterprise はオーナーが有効化したうえで、各メンバーが自分でオンにする — [同上](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Sensitive topics:
  - 健康・人種・宗教・政治・性自認などは既定で保存しない。「Include sensitive topics in memory」でオプトインでき、保存のたびに通知が出る。
  - 政府発行のID番号・犯罪歴・金融口座番号・在留資格は、設定に関係なく保存されない。
  — [同上](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- 管理: Settings > Your Claude >「Your memory」の Manage で、Topics を閲覧・編集・削除できる。
  - Pause: 既存の memory を残したまま、使用も追加も止める。
  - Reset: project memory を含めて全削除。取り消せない。
  - 単発のチャットだけ使わない: 最初のメッセージを送る前に「+」メニューで Memory をオフにする。
  — [同上](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- Memory の Import / Export: 他のAIアシスタントから取り込める。experimental 扱い — [同上](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- 注意点: 会話を削除しても、その会話から作られた memory エントリは消えない。Cowork はクラウド実行のときだけ memory を共有する — [同上](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- 使いどころ: 毎回同じ背景説明を繰り返さなくて済み、usage の節約にもなる（公式の節約Tipsにも挙がっている）— [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- 確認日: 2026-10-29（2026-07と08に大きな仕様変更があったので変わりやすい）

#### 1-5. Incognito chats
- 概要: 履歴にも memory にも保存されない一時的な会話。学習には使われず、monthly recap の対象外。全プランで使える — [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)
- 保持と組織での扱い: 既定で30日間は保持される。Team/Enterprise ではデータエクスポートに含まれ、Enterprise では Compliance API の対象にもなる — [同上](https://support.claude.com/en/articles/12260368-use-incognito-chats)
- 制約:
  - 新体験のユーザーでも旧体験で開くため、ファイル作成・コード実行ができない。
  - プロジェクトの外でしか使えない。
  - 通常チャットに変換できない。
  - 閉じると再び開けない。
  — [同上](https://support.claude.com/en/articles/12260368-use-incognito-chats)
- 確認日: 2026-10-29

#### 1-6. Artifacts（テンプレート型: Docs / Slides / Design / Dashboards / Motion）
- 概要: 「人に見せるために Claude が作るもの」すべて。会話の横に開いて、編集・再訪・共有ができる。分量があり（目安15行超）、単体で完結し、再利用されそうな内容のときに作られる — [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- テンプレート:
  - Docs: チームとリアルタイムで共同編集する文書。Word / PDF / Markdown / Google Docs にエクスポートできる。
  - Slides: PowerPoint / PDF / Google Slides に出力できる。
  - Design: ビジュアル、モックアップ、プロトタイプ、LP。.zip / PDF / PPTX / HTML に出力できる。
  - Dashboards（beta）: 各チャートにクエリと最終更新時刻が表示される。
  - Motion（beta、Team/Enterprise限定）: MP4 で出力できる。
  — [同上](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- Runtime capabilities:
  - Claude を直接呼び出せる。API キーは不要で、利用分は各ユーザー自身のプラン上限から引かれる。
  - 接続済みアプリ（Asana / Google Calendar / Slack など）を読み書きできる。共有された artifact でも、閲覧者が自分のアプリを接続する。
  - データ保存: personal（ユーザーごとに非公開）と shared（全員が見える）があり、1 artifact あたり20MBまで、テキストのみ。
  — [同上](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- 公開と共有: 作成直後は本人だけが見られる（private）。他人が公開した artifact は「知らない送り主からのファイル」と同じように扱うよう公式が注意している — [同上](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- 編集: Claude に頼む方法と、直接編集する方法がある。Docs や Markdown では範囲を選んで「Edit with Claude」を使う。過去のメッセージを編集すると別ブランチになり、元の成果物は残る — [同上](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- プラン別の可否:
  - artifact 作成と Docs / Slides / Design: 全プラン
  - Dashboards・アプリ接続・データ保存: Pro 以上
  - Motion: Team / Enterprise
  - Enterprise では Docs / Slides / Design が 2026-10-15 から既定でオン
  — [同上](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- 前提条件: Settings で「Cloud code execution and file creation」をオンにしておく必要がある。2026-09-16 より前の artifact は legacy 扱いで、引き続き動くが新規には作れない — [同上](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- 「sheets（スプレッドシート型テンプレート）」は記事に記載がない（表計算は file creation の .xlsx や Dashboards で扱う）— [同上](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- 確認日: 2026-10-29（2026-09-16に再設計。beta項目が多い）

#### 1-7. File creation / Code execution / ファイル分析
- 概要: .xlsx / .pptx / .docx / PDF を作成・編集でき、ダウンロードや Google Drive への保存ができる。アップロードとダウンロードはどちらも1ファイル30MBまで。30MBを超えるPDFも、context に載せずに実行環境の中で処理できる — [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- 実行環境: 隔離されたサンドボックスで Python などを実行する。データ分析、PNG の可視化、CSV/TSV の処理、機械学習モデルの構築ができる — [同上](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- ネットワーク:
  - Free/Pro/Max: 既定で egress オン。
  - Team: 既定で package manager のみ。
  - Enterprise: 既定で egress オフ。
  - 設定肢は off / package managers only / 指定ドメイン追加 / All domains（最もリスクが高い）。
  — [同上](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- 公式の注意:
  - 外部ファイルやWebに仕込まれた prompt injection によって、信頼できないコードが実行されたり、データが外部へ送られたりするおそれがある。
  - network access を切れば、データはサンドボックスの外に出ない。
  - ただし MCP 連携は egress 設定に関係なく外部と通信できる。
  — [同上](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- 長い会話の自動 context 管理（compaction）は code execution がオンのときに働く — [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- 確認日: 2026-10-29

#### 1-8. Web search / Research / 思考設定の使い分け
- Web search: 新体験ではトグルがなく、役に立つときに Claude が検索する（classic のチャットでは「+」> Web search）。回答には出典が付く。web search と web fetch はどちらも usage を消費し、長い記事を fetch すると大きく減る。Team/Enterprise ではオーナーがワークスペース単位で有効化する必要がある — [Enable and use web search](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)
- Research:
  - 前の検索結果をもとに次の検索を重ね、何を調べるかを自分で決めていく。
  - 情報源は web と、接続済みのツール（Gmail・Calendar・Google Docs など）。
  - Pro 以上で使える。
  - 選んでいるモデルに関係なく Claude Opus 5.5 で動く（必要に応じて Opus 4.8 にフォールバック）。
  - mobile では web のみを使い、ローカル MCP は使えない。
  — [Use research on Claude](https://support.claude.com/en/articles/11088861-use-research-on-claude)
- 公式の使い分け:
  - Web search: 1〜2回のツール呼び出しで答えられる単純な事実確認向け。
  - Extended thinking: 最新情報が不要な複雑な推論（数学、デバッグなど）向け。
  - Research: 5回以上のツール呼び出しを1〜3分かけて行う包括的な情報収集向け。
  - thinking と research を組み合わせると、計画を立ててから集めるので、より長く出典付きのレポートになる。
  — [When should I use web search, extended thinking, and research?](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research)
- 公式のコツ: Research が起動しないときは「Claude, please use the research tool to…」と明示する — [Use research on Claude](https://support.claude.com/en/articles/11088861-use-research-on-claude)
- 確認日: 2026-10-29

#### 1-9. モデル・effort・thinking のアプリ内設定
- モデルは送信ボタン横のメニューで切り替える（「More models」で追加表示）。変更は次の応答から反映される — [Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)
- Effort:
  - 段階は Low / Medium / High / Extra high（xhigh、Opus 4.7 以降）/ Max。
  - 対応モデル: Haiku 5.5, Sonnet 5.5, Opus 5.5, Fable 5.1, Opus 5, Sonnet 5, Fable 5, Opus 4.7, Opus 4.6, Sonnet 4.6。
  - 各モデルの推奨値には「Default」と表示される。
  — [同上](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)
- Thinking:
  - effort があるモデルでは「Thinking」、それ以外では「Extended」と表示される。
  - Haiku 5.5 / Sonnet 5.5 / Opus 5.5 / Fable 5.1 / Opus 5 ではアプリから thinking をオフにできない。
  - Opus 5.5 と Fable 5.1 は API でも全 effort で常時オン。
  — [同上](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)
- 公式の推奨:
  - 日常的な用途は既定値で十分。
  - 複雑な作業は effort を上げるか thinking をオンにする。
  - Opus 4.7 以降で複雑なコーディングや agentic な作業をするなら、まず xhigh を試す。
  - Max は最難関で正確さが重要な作業に限る。
  - 高 effort ほど時間も token も多く使う。
  — [同上](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)
- アプリでの effort 既定値:
  - Fable 5.1 は Claude Code で High、Cowork と Claude.ai で Medium。
  - Sonnet 5.5 は Claude Code とアプリで Medium。
  — [Introducing Claude Mythos and Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)、[Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)
- Enterprise 管理者は、ロールごとに使えるモデルや effort を制限でき、新規チャットの初期モデルと初期 effort も設定できる — [Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)
- 確認日: 2026-10-29

#### 1-10. Skills と Plugins（アプリ内）
- Skills:
  - 専門知識やワークフローを Claude に与える仕組み。
  - Excel / Word / PowerPoint / PDF 用の Anthropic 製 skills があり、関連する場面で自動的に使われる。
  - カスタム skill はフォルダ（skill.md を含む）を ZIP にして Customize > Skills からアップロードする。
  - 全プラン（Free含む）と Claude Code で使え、API でも code execution tool 経由で使える。
  - code execution が有効になっている必要がある。
  — [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- Skills の公式の推奨:
  - Claude は依頼内容と skill の description を見て使うかどうかを決めるので、「いつ使う skill か」が分かる description を書く。
  - 使われないときは、トグルがオンになっているか確認し、プロンプトで skill 名を挙げる。
  — [同上](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- Skills の組織での共有: Team/Enterprise では閲覧専用で共有でき、組織ライブラリに公開できる。オーナーは全員に配布（provision）できる — [同上](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- Plugins:
  - skills・connectors・sub-agents・commands をまとめたもの。hooks とローカル MCP は Cowork と Claude Code でだけ動く。
  - web の chat、Desktop、Cowork、Claude Code で使え、アカウントに保存されて Claude Code に同期される（v2.1.273 以上）。
  - Pro 以上で使える。
  — [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- Plugins の入手: Customize > Plugins の Discover タブから入れる。Knowledge Work marketplace が既定で入っており、Financial Services / Legal / Life Sciences の marketplace もある。GitHub などのリポジトリから marketplace を追加でき、「Plugin Create」で自作もできる — [同上](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- 確認日: 2026-10-29

#### 1-11. Connectors（MCP、Google Workspace、Microsoft 365 など）
- 種類:
  - Directory connectors: 既製の connector。
  - Custom connectors: リモート MCP。Anthropic のクラウドから接続し、ローカル端末からは接続しない。
  - Desktop extensions: Claude Desktop 用。
  - Interactive connectors: 会話の中にライブUIを描画する。
  — [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- 使い方とプラン差: custom connector は全プランで使えるが、Free は1個まで。チャットごとに「+」か「/」から Connectors をオンにする。10個以上有効なら Tool access を「On demand」にするよう推奨されている — [同上](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- Team/Enterprise の管理: オーナーがツール単位で Always allow / Needs approval / Blocked を設定できる — [同上](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- 安全上の注意: custom connector は Anthropic の検証を受けていない。信頼できる組織のサーバーだけに接続する — [同上](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- Team プランの connectors: Google Drive / Gmail / Google Calendar / GitHub / Microsoft 365 / Slack。Enterprise search は専用の検索プロジェクトで Slack / M365 / custom connectors を横断検索する — [What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)
- 確認日: 2026-10-29

#### 1-12. Claude in Chrome
- 概要: Claude が Web サイトを読み、クリックし、移動するブラウザ拡張。Chrome のサイドパネル、Cowork、Claude Code からタスクを始められる。有料プランのみ。Google Chrome 限定で、他の Chromium 系ブラウザや mobile は非対応 — [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- 機能:
  - 「/」で保存済みプロンプトを呼び出せる。
  - ワークフローを記録できる（classic サイドパネルのみ）。
  - タブを切り替えても動き続ける。
  - tab groups で複数タブを扱える。
  - 日・週・月・年単位の定期タスクを設定できる。
  — [同上](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- Claude Code との連携: Claude Code で作ったサイトをブラウザで検証でき、コンソールログ・ネットワーク・DOM を読める — [同上](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- 公式の注意: 安全分類器で強化されているが「still risky」。機微な情報の扱いに built-in browser や Claude in Chrome を使うことは強く非推奨 — [同上](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)、[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- 確認日: 2026-10-29

#### 1-13. Claude for Microsoft 365（Excel / PowerPoint / Word / Outlook）と Google Workspace add-on
- M365:
  - Excel / PowerPoint / Word / Outlook の add-in を連携させ、あるアプリから読んだ内容で別のアプリを変更できる（例: Excel のモデル → PowerPoint のスライド、Word のメモ）。
  - 有効な skills はアプリをまたいで適用される。
  - 有料プランで使える。
  - 「Let Claude work across files」は Pro/Max では既定でオン、Team/Enterprise では既定でオフ。
  — [Work across M365 apps](https://claude.com/docs/office-agents/work-across-apps)
- M365 の制約: 開いているファイル、開いているメールやイベントにしか作用しない。ファイルを開く・閉じる・切り替えることはできない。チャット履歴はブラウザ内に保存される — [同上](https://support.claude.com/en/articles/13892150-work-across-excel-and-powerpoint)
- Google Workspace add-on（beta）:
  - Docs / Sheets / Slides のサイドバーで動き、開いているファイルを読んでその場で編集する。
  - Sheets では数式の作成・修正、モデル構築、データ整形ができる。
  - 「Ask before edits」（既定）と「Accept all edits」の2モード。
  - 1回の操作は6分で止まる。
  - Pro 以上で使える。
  — [Use Claude in Google Docs, Sheets, and Slides](https://support.claude.com/en/articles/16951679-use-claude-in-google-docs-sheets-and-slides)
- Gmail / Calendar / Drive の connector は add-on とは別物で、claude.ai でのチャット中に参照するためのもの — [同上](https://support.claude.com/en/articles/16951679-use-claude-in-google-docs-sheets-and-slides)
- 確認日: 2026-10-29

#### 1-14. Claude in Slack（Claude Tag）
- 概要: Claude in Slack は 2026-08-03 に Claude Tag へ移行した。@Claude をタグ付けして、組織のツールやチャンネルの文脈を使って作業を任せる — [What is Claude Tag?](https://support.claude.com/en/articles/15594475-what-is-claude-tag)
- できること: 数日にわたって文脈を覚え、自分でフォローアップを予約し、完了報告などを能動的に投稿する。独自の組織IDで動く — [同上](https://support.claude.com/en/articles/15594475-what-is-claude-tag)
- プランと課金: Team/Enterprise で beta。チャンネルでの作業は組織に、DM とアシスタントパネルでの利用は個人アカウントに課金される — [同上](https://support.claude.com/en/articles/15594475-what-is-claude-tag)
- 確認日: 2026-10-29

#### 1-15. Desktop app（computer use、ローカルファイル、quick entry）
- Computer use（beta）:
  - 使える connector やツールがないときに、画面を直接クリック・入力・操作する。
  - macOS / Windows の Desktop（Cowork と Claude Code）で動き、Pro/Max 限定（Team/Enterprise は不可）。
  - 優先順位は connectors → built-in browser / Claude in Chrome → 画面操作。
  — [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
- Computer use の安全面:
  - アプリごとに許可を求める。投資・トレード・暗号資産のアプリは既定でブロックされる。
  - 「Computer use has no sandbox between Claude and your applications」。
  - 銀行・医療・行政系のアプリはオフにしておくよう推奨されている。
  — [同上](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)
- Cowork の安全指針:
  - prompt injection は「信頼境界の外の情報を読める」と「被害につながる行動ができる」の両方がそろって成立する。片方を外せば攻撃は難しくなる。
  - Claude 専用の作業フォルダを作る。
  - 低リスクのタスクから始める。
  - バックアップを取る。
  - 信頼できる MCP や plugin だけを使う。
  - 送信・購入など取り消しにくい操作を scheduled task にしない。
  - Claude がした行動の責任はユーザーにある。
  — [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
- Quick entry（macOS）:
  - Option を2回押すと、どのアプリからでも呼び出せる。
  - 範囲を選んだスクリーンショットや、ウィンドウの内容を添付できる。
  - Caps Lock で音声入力（既定はオフ）。
  - 全プランで使える。
  — [Use quick entry with Claude Desktop on Mac](https://support.claude.com/en/articles/12626668-use-quick-entry-with-claude-desktop-on-mac)
- 確認日: 2026-10-29

#### 1-16. Mobile / Voice / 言語
- Voice mode（beta）:
  - 全プランで使え、mobile・Desktop・web に対応（phone 向けに最適化）。
  - Hands-free（既定）と push-to-talk がある。
  - テキストと音声を途中で切り替えても文脈は保たれ、文字起こしは履歴に残る。
  - Gmail / Calendar / Docs / Slack の connector と web search を使える。
  - Fable は voice では使えない。
  — [Use voice mode](https://support.claude.com/en/articles/11101966-use-voice-mode)
- Mobile の機能: インタラクティブなチャートや図（2026-03-25）、Cowork タスクの監視と開始、健康データ分析（米国のみ）— [Release notes](https://support.claude.com/en/articles/12138966-release-notes)、[Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)
- 日本語: UI 言語として日本語に対応している。表示言語に関係なく、Claude は書かれた言語で返答する。音声の言語は別設定（Settings > Capabilities > Voice > Spoken language）— [How to use Claude in your preferred language](https://support.claude.com/en/articles/10769299-how-to-use-claude-in-your-preferred-language)
- 確認日: 2026-10-29

#### 1-17. 新しい周辺プロダクト（2026年）
- Claude Design（2026-04-17、Anthropic Labs、research preview）:
  - デザイン、プロトタイプ、スライド、ワンペーパーを作る。
  - コードベースやデザインファイルから design system を構築する。
  - PPTX / PDF / HTML / Canva に出力でき、Claude Code へ引き渡せる。
  - Pro 以上で使える。
  — [Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/claude-design-anthropic-labs)
- Claude Science（2026-06-30、beta）:
  - 研究者向けのワークベンチ（PubMed、Jupyter、R、HPC）。
  - 60以上の skills / connectors を備える。
  - 成果物はコードと環境付きで再現できる。
  - reviewer agent が引用と計算を検証する。
  — [Claude Science, an AI workbench for scientists](https://www.anthropic.com/news/claude-science-ai-workbench)
- Claude Duet（2026-10-21、research preview）:
  - 人にメッセージを送る感覚で使う、能動的なエージェントアプリ。自前のクラウドPCで動き続け、朝のブリーフィングを送る。
  - 送信・支払い・署名・削除の前には承認を求める。
  - 米国の Pro/Max に waitlist 経由で提供（iPhone / Android）。
  - モデルは選べず Opus 5.5 固定。
  - プランの usage を消費する。
  — [Get started with Claude Duet](https://support.claude.com/en/articles/17631495-get-started-with-claude-duet)
- 公式の学習コース: Claude Academy の「Claude 101」は13レッスン。Meet Claude / Getting better results / projects / artifacts / skills / connectors / Enterprise search / Research / use-cases by role を扱う — [Claude Academy: Claude 101](https://academy.claude.com/courses/claude-101/creating-with-artifacts)
- 確認日: 2026-10-29

#### 1-18. Team / Enterprise 向け機能（概念）
- Team:
  - SSO・ドメインキャプチャ・JIT・ロール権限・組織や個人単位の spend cap。
  - プロジェクト共有と Enterprise search。
  - Claude Code と Cowork を同梱。
  - 2〜150席。
  — [What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)
- Enterprise: 監査ログ、SCIM、カスタム保持期間、Compliance API、Analytics API、顧客管理の暗号鍵、US-only inference、HIPAA-ready 構成 — [What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)
- 2026年に追加された管理機能:
  - グループ単位の RBAC（04-09）
  - connector やツール単位のロール制御（05-28）
  - モデルや effort の制御（07-01、beta）
  - skill / plugin のセキュリティスキャン（08-06、beta）
  - Smart reports（09-10、beta）
  — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 確認日: 2026-10-29

### Inferences
- 中〜上級者向けの教材では、①「Instructions for Claude（全体）/ Project instructions（案件別）/ Memory（自動蓄積）/ Skills（手順の再利用）/ Plugins（役割ごとの束）」の使い分け表、②「web search / Research / thinking・effort」の使い分け、③ Agentic 実行の権限モード（Auto / Manual / Skip）と prompt injection の2条件モデル、の3つを中心に据えると効果的だと考えられる。いずれも公式が明確に定義しているのに、ユーザーが混同しやすい。
- 2026-09-16の統合以前に書かれた外部記事（「Cowork は別アプリ」「Web search はトグル」など）は古くなっている。教材では「2026-09以降の新体験」と「classic / 旧体験」をはっきり分けて書く必要がある。
- Memory は「削除した会話の memory は残る」「project memory は独立している」「sensitive は既定で保存しない」といった誤解されやすい仕様が多い。FAQ 形式の項目に向いている。

### Gaps
- Styles（preset / custom）の現行仕様は、取得した記事では確認できなかった（Incognito 記事に custom styles への言及があるだけ）。
- チャットの共有（share link / snapshot）の現行仕様は、検索上限に達したため調べられなかった。分かったのは「Free/Pro/Max ではファイル成果物を含む会話の公開共有が無効」という一点だけ（[Create and edit files](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)）。
- Desktop のローカル MCP（設定ファイル方式）の現行手順、mobile のウィジェットや Shortcuts の詳細は取得していない。
- Claude for Excel / PowerPoint / Word / Outlook それぞれの単体機能（Word・Outlook の提供開始日など）は、cross-app 記事以外では確認できなかった。

---

## 2. プランと利用上限（usage limits）

### Takeaway
有料プランには「5時間ごとにリセットされる session limit」と「週1回リセットされる weekly limit」の2層がある。claude.ai・Claude Code・Desktop で同じ上限を共有する。消費を早める要因は、メッセージ長、添付サイズ、会話の長さ、ツール（Research や web search）、モデル、effort、artifacts、多段タスク。Fable は Max と Team/Enterprise の premium seat で「週上限の50%まで」含まれ、Pro と standard seat では usage credits が必要。金額や倍率は変わりやすいので、教材では日付付きで書く。

### Cited Findings

#### 2-1. プラン一覧（2026-10-29 時点の公開価格）
- Free: $0。web / desktop / mobile でチャットでき、Memory あり、Projects は5個まで。Claude Code と Research はなし。モデルは Sonnet と Haiku（Opus と Fable は含まれない）— [Plans & pricing](https://claude.com/pricing)
- Pro: 年払いで月$17（$200前払い）、月払いで$20。Claude Code、Claude Science、Projects、Research、Memory、Dashboards（beta）。Opus を含む。Fable は usage credits で使う — [Plans & pricing](https://claude.com/pricing)
- Max: 5x が月$100、20x が月$200（web価格。mobile では異なる場合がある。月払いのみ）。Pro に比べ session あたり5倍または20倍の利用量。新モデルや新機能への優先アクセス。Claude Code を同梱 — [What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- Max の API credits: 月次で 5x に$100、20x に$200 — [Plans & pricing](https://claude.com/pricing)
- Max での Fable: 週上限の50%まで — [Plans & pricing](https://claude.com/pricing)
- Team:
  - Standard seat は年払い$20 / 月払い$25、Premium seat は年払い$100 / 月払い$125（米国価格）。
  - Standard は Pro の1.25倍、Premium は Pro の6.25倍（session あたり）。週上限もある。上限は個人ごとで、メンバー間で共有できない。
  - 2〜150席。
  — [What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)
- Team のその他: pooled API credits が最大$500/月。Premium seat で Fable を週上限の50%まで — [Plans & pricing](https://claude.com/pricing)
- Enterprise:
  - 現行は usage-based。席料は月$20/席の年払い（最低20席）に、API 料金での従量課金が加わる。
  - 「There are no per-seat usage limits and no included token allowance」。
  - 旧来の seat-based（Standard / Premium）は次回の契約更新時に移行する。
  — [What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)、[Plans & pricing](https://claude.com/pricing)
- Max/Team の月次 API credits は 2026-10-07 開始で、Console 組織を紐付けて受け取る — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- 確認日: 2026-10-29（価格は「変更されることがある」と明記されている）

#### 2-2. Usage limit の仕組み
- 有料プランには5時間ごとにリセットされる session limit と、週1回リセットされる weekly limit がある。claude.ai・Claude Code・Claude Desktop の利用は同じ上限にカウントされる。アップグレードすると新しい上限がすぐに適用される — [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- weekly limit のリセット時刻はアカウントごとに固定 — [What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)
- 2026-09-22（Opus 5.5 の発表時）に、Pro / Max / Team / seat-based Enterprise の5時間上限が引き上げられた。あわせて、保存して後で使える rate limit reset が付与された — [Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)
- 消費を早める要因:
  - メッセージの長さ、添付ファイルのサイズ、会話全体の長さ
  - ツール（Research、web search）
  - モデルの選択、effort の高さ
  - artifact の作成と利用
  - 多段タスク（コード実行、ファイル作成、ブラウジング）
  — [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- 補足: 「Higher effort uses more tokens」。tools と connectors は「token-intensive」。自動 context 管理が発動するほど長い会話も、より多く消費する — [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- Fable の消費: 通常の weekly limit から引かれ、他のモデルより速く減る（倍率は非公開）— [Claude Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
- 公式の節約Tips:
  - 始める前に計画し、関連する質問はまとめて送る。
  - 具体的に書く。
  - memory と chat search を活用する。
  - 送信前に見直す。
  - よく使う資料は project に置いて cache を効かせる。
  - Settings > Usage で進捗バーを確認する。
  - コードは環境の情報とコード全体を1通にまとめ、文章は全文を1通で渡す。
  — [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- 確認日: 2026-10-29

#### 2-3. Context window（アプリ内の長さ制限）と自動 context 管理
- 有料プランでは、最新モデルが最大1M token の context window に対応している。それ以外のモデルは500Kまたは200K。応答用の領域が確保されるので、実際に使える長さは少し短くなる — [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- 自動 context 管理（code execution 有効時）: 上限が近づくと古いメッセージを要約して会話を続ける。チャット履歴そのものは保存され、要約後も参照できる — [同上](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- 上限に当たったときの公式の対処: project を使う、project instructions を短くする、project のファイルを減らす、extended thinking をオフにする、effort を下げる、ツールを減らす — [同上](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- 確認日: 2026-10-29

#### 2-4. Usage credits（超過分の従量課金）と Fable の扱い
- Usage credits の仕組み:
  - session・weekly・Fable 週上限のいずれかを使い切っても、止まらずに従量課金へ移る。料金は標準の API 料金。
  - 自動チャージ、月の上限額、アラートを設定できる。
  - Claude Code と Research にも適用される。
  — [Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)
- **日本固有の注意**: 2026-09-10 以降、日本では credits が購入から6か月で失効する。失効の7日前にメールが届く — [同上](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)
- Fable 5 / 5.1 の扱い:
  - 全有料プランで使える。Free では使えない。
  - Max と premium seat はプランに含まれ、週上限の50%まで。50%は「追加枠」ではなく、同じ週上限の内側にある。
  - Pro と standard seat はプランの上限に含まれず、最初から usage credits で使う。
  - Fable 5 の無料プロモーションは 2026-07-19 に終了し、Fable 5.1 には適用されない（記事日付 2026-09-02）。
  — [Claude Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
- 確認日: 2026-10-29

### Inferences
- 中級者の「すぐ上限に当たる」という悩みの多くは、長い会話を続けること、大きな添付を繰り返すこと、高 effort や Fable を常用することが原因だと推測される。教材では「新しいチャットに切り替える目安」「project に置いて cache を効かせる」「effort は既定から始める」の3点をセットで教えるとよい。
- Pro と Max では Fable の扱いが根本から違う（Pro は最初から従量課金）。モデル選択の項でプランとの関係を必ず添えるべきだ。

### Gaps
- Free / Pro の具体的なメッセージ数や token 量は、公式に数値として公開されていない（倍率のみ）。
- Fable が Opus に比べて何倍消費するかは非公開。
- 公開されている「自動 context 管理」の閾値も確認できなかった。

---

## 3. モデルラインナップ（2026年10月時点）と選び方

### Takeaway
現行の主力は Claude Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 の4つ。どれも context window 1M、最大出力128K、reliable knowledge cutoff 2026年6月、adaptive thinking に対応する。最上位の新しい系列として Fable（一般向け）と Mythos（Fable と同じモデルで safeguard が緩く、検証済み組織に限定）が加わった。公式の推奨は「迷ったら Opus 5.5 から始め、モデルを替える前に effort を調整する」。

### Cited Findings

#### 3-1. 現行モデル表（API docs）

| | Fable 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---|---|---|
| API ID | `claude-fable-5-1` | `claude-opus-5-5` | `claude-sonnet-5-5` | `claude-haiku-5-5` |
| Context window / 最大出力 | 1M / 128K | 1M / 128K | 1M / 128K | 1M / 128K |
| Reliable knowledge cutoff | 2026年6月 | 2026年6月 | 2026年6月 | 2026年6月 |
| Thinking | Adaptive（常時オン） | Adaptive（常時オン） | Adaptive | Adaptive |
| 既定 effort | high | medium | high | medium |
| 速度 | 遅め | 中 | 速い | 最速 |
| 価格（入力 / 出力、$/MTok） | $10 / $50 | $4 / $20 | $2 / $10 | $0.10〜 / $0.50〜 |
| 得意分野 | 高度な推論と長時間の agentic 作業 | 長時間の agentic coding と knowledge work | 速度と知能のバランス | 大量処理・低遅延（分類・抽出・ルーティング） |

出典: [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)

- Haiku 5.5 の価格: prompt が100k token 以下なら入力$0.10 / 出力$0.50、100k を超えると$0.50 / $2.50 — [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- 1M context の料金: Claude 4.6 以降（Haiku 5.5 を除く）は1M 全域が標準料金 — [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Tokenizer: Claude 4.7 以降は、同じテキストでも旧モデルより約30%多くの token を使う — [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- 確認日: 2026-10-29

#### 3-2. 2026年のリリース年表

| 日付 | リリース |
|---|---|
| 02-05 | Opus 4.6 |
| 02-17 | Sonnet 4.6 |
| 04-16 | Opus 4.7 |
| 05-28 | Opus 4.8 |
| 06-09 | Fable 5 と Mythos 5 |
| 06-30 | Sonnet 5 |
| 07-24 | Opus 5 |
| 09-15 | Mythos と Fable 5.1 |
| 09-22 | Opus 5.5 |
| 09-28 | Sonnet 5.5 |
| 10-07 | Haiku 5.5 |

出典: [Anthropic News: Models](https://www.anthropic.com/news/models)

- **日付の食い違い**: Fable 5.1 / Mythos 5.1 の公開日は、News の一覧では 2026-09-15、Help Center の Release notes では 2026-09-01。Platform release notes でも Fable 5.1 の cache 料金が 09-01 付けになっている — [Anthropic News: Models](https://www.anthropic.com/news/models)、[Release notes](https://support.claude.com/en/articles/12138966-release-notes)、[Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- Fable 5 の一時停止:
  - 2026-06-12、米国政府が Fable 5 / Mythos 5 に輸出管理を適用した。国籍をリアルタイムで確認できなかったため、全ユーザーへの提供が停止された。
  - 06-30 に規制が解除され、07-01 に世界で再提供された。
  - 再提供にあわせて分類器が強化され、ブロックされた依頼は Opus 4.8 に回されるようになった。
  — [Redeploying Fable 5](https://www.anthropic.com/news/redeploying-fable-5)
- 確認日: 2026-10-29

#### 3-3. Fable と Mythos（新しい上位系列）
- 両者の関係: 「Claude Fable 5.1 and Claude Mythos 5.1 are the same model, but with different levels of safeguards」 — [Introducing Claude Mythos and Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- Fable 5.1: 一般提供。脆弱性を見つける用途には使えるが、exploit の開発には使えない — [同上](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- Mythos 5.1:
  - Cyber Verification Program（防御的なセキュリティ業務向け）と Life Sciences Verification Program 経由でのみ提供される。
  - 現在は米国の組織に限られる。
  - 研究用途の生物学能力は safeguard で制限されている。
  — [同上](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- 両モデル共通の措置: 出力に不可視の透かしが入る（EU AI Act 対応）。新規 API アカウントでは、過去の thinking を保ったまま前の文脈を編集することができない（蒸留攻撃対策）— [同上](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- アプリでの扱い: claude.ai の model picker で「Fable 5」「Fable 5.1」を選ぶ — [Claude Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
- 確認日: 2026-10-29

#### 3-4. 各モデルの位置づけ（発表ページより）
- Opus 5.5（2026-09-22）:
  - agentic coding、computer use、knowledge work でトップ。「It performs at the level of Claude Fable 5.1 on most work」。
  - Opus 5 より約40%安く動く。
  - 取り消しにくい行動を取りにくく、prompt injection への耐性も高い。
  — [Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5)
- Sonnet 5.5（2026-09-28）:
  - 「Where Opus 5.5 is built for complex work requiring careful judgment, Sonnet 5.5 is strongest at well-scoped everyday tasks」。
  - Sonnet 5 より30%以上速く、1タスクあたり最大30%安い。
  — [Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5)
- Haiku 5.5（2026-10-07）:
  - 要約、compaction、DB クエリ、分類、サブエージェントといった大量処理向け。
  - Haiku 系で初めて effort に対応した。
  - 複雑な agentic coding は Sonnet / Opus のほうが上。
  — [Introducing Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)
- 確認日: 2026-10-29

#### 3-5. 公式のモデル選択ガイド
- 基本方針: 「If you're unsure which model to use, start with Claude Opus 5.5 for most workloads」。Opus 5.5 を高い effort にしても評価が足りない場合に Fable 5.1 へ上げる — [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- 2つの始め方 — [Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model):
  - 効率優先: Haiku 5.5 から始め、性能が足りない部分だけ上位に替える。
  - 能力優先: Opus 5.5 から始め、effort を下げたり下位モデルに替えたりして最適化する。xhigh / max でも足りなければ Fable 5.1 へ。
- 選択マトリクス — [同上](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model):
  - Fable 5.1: 何時間も続く agent、多段の deep research、完成した文書・表・デッキまで仕上げる分析。
  - Opus 5.5: 何時間も自律で動くコーディング、大規模リファクタリング、vision 中心の作業、computer use。
  - Sonnet 5.5: 日常的なコーディング、データ分析、コンテンツ作成、agentic な tool use。
  - Haiku 5.5: リアルタイム処理、大量処理、サブエージェント。
- 「Tuning effort is often a better lever than switching models」 — [同上](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- 評価の重要性: 「Having a good evaluation set is the most important step in the process」 — [同上](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- 複数モデルの組み合わせ: executor が難しい判断を advisor にエスカレーションする形と、orchestrator が安価な worker に作業を割り振る形の2パターン — [同上](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)
- 確認日: 2026-10-29

#### 3-6. Adaptive thinking と Effort（概念）
- Thinking の挙動 — [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking):
  - Adaptive thinking では、Claude がいつ・どれだけ考えるかを自分で決める。
  - 既定で thinking オン（adaptive のみ）: Opus 5.5 / Opus 5 / Sonnet 5.5 / Sonnet 5 / Haiku 5.5 / Fable / Mythos。
  - 既定でオフ（adaptive をオプトイン）: Opus 4.6〜4.8 / Sonnet 4.6。
  - 旧来の `budget_tokens` 方式: Opus 4.5 / Sonnet 4.5 / Haiku 4.5。
- Thinking の表示と課金 — [Thinking](https://platform.claude.com/docs/en/build-with-claude/thinking):
  - thinking token は返却されなくても出力 token として課金される。
  - 表示される要約は生の思考過程ではない（「What you see is never the raw chain of thought」）。
- Effort の段階 — [Effort](https://platform.claude.com/docs/en/build-with-claude/effort):
  - low: 単純なタスク、サブエージェント、低遅延・低コスト向け。
  - medium: バランス型。
  - high: 複雑な推論や難しいコーディング。
  - xhigh: 30分を超える長時間の agentic 作業。
  - max: 制約なしの最大能力。
- Effort の性質 — [Effort](https://platform.claude.com/docs/en/build-with-claude/effort):
  - effort は「a behavioral signal, not a strict token budget」。
  - 低い effort ではツール呼び出しが減り、前置きなしで行動する。高い effort では計画を説明してから動き、詳しくまとめる。
- 確認日: 2026-10-29

#### 3-7. 旧モデルの退役（変わりやすい）
- アプリ: 2026-01-16 に Opus 4 / 4.1 をモデル選択から削除 — [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- API:
  - Sonnet 3.7 / Haiku 3.5 は 2026-02-19 に退役。
  - Haiku 3 は 04-20 に退役。
  - Sonnet 4 / Opus 4 は 06-15 に退役。
  - Opus 4.1 は 08-05 に退役。
  - Sonnet 4.5 は 2026-11-30 に退役予定（09-30 に告知）。
  — [Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- 確認日: 2026-10-29

### Inferences
- アプリユーザー向けの「モデル選び」は、①既定（多くは Opus 5.5 か Sonnet 5.5）を使う、②重い仕事は effort を上げる、③それでも足りなければ Fable（プランと課金に注意）、という3段階で説明するのがよい。これは公式の API 向けガイドを、アプリの文脈に合わせて言い換えたもの。
- 全モデルの knowledge cutoff が2026年6月で揃っている。そのため「2026年7月以降の出来事は web search が必要」という説明を一つにまとめられる（ただし次のモデルが出れば変わる）。

### Gaps
- claude.ai の各プランでの既定モデル（Free の既定が Sonnet 5.5 なのか Haiku 5.5 なのか）は公式記事で確認できなかった。
- training data cutoff（reliable ではない方）は Transparency Hub に載っているとされるが、未取得。
- Mythos 5（Fable 5 と同時期のもの）の現在の提供状態の詳細は未確認。

---

## 4. 公式のプロンプトエンジニアリング指針（モデル世代別を含む）

### Takeaway
公式は「Prompting best practices」を「living reference」と位置づけ、基本技法（明確さ、背景と目的、例示、XML タグ、役割、長文の配置、thinking、chaining）とモデル別の差分をここに集約している。最新世代で特に教えるべき変化は次の5つ。①prefill が廃止された（4.6以降は400エラー）。②`budget_tokens` から effort へ移行した。③推論を本文に書かせる指示は `reasoning_extraction` として拒否されることがある。④「CRITICAL / MUST」のような強い表現は過剰反応を招くので和らげる。⑤冗長さ・進捗報告・スコープ・過剰な検証はモデルごとに癖があり、明示的に指示する。Console の prompt generator / improver API は2026-08-17に退役し、インタラクティブチュートリアルは Claude 3 世代向けとして注記付きで残っている。

### Cited Findings

#### 4-0. ドキュメント構成と前提
- 前提として、①成功基準の定義、②それを経験的に測る方法、③改善したい初稿、の3つを用意する。足りなければ「Define success criteria and build evaluations」から始める — [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- 成功基準によっては、プロンプトよりモデル選択で解決するほうが早い（遅延やコストなど）— [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- 全技法は「Prompting best practices」に集約されている（「the living reference; start there」）— [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- 対象モデル: Fable 5.1 / Mythos 5.1 / Fable 5 / Mythos 5 / Opus 5.5 / Opus 5 / Opus 4.6〜4.8 / Sonnet 5.5 / Sonnet 5 / Sonnet 4.6 / Haiku 5.5 / Haiku 4.5。構成は「モデル別ガイダンス → 全モデル共通の技法 → 移行の注意」 — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-1. Be clear and direct（明確かつ直接的に）
- 概要: Claude を「a brilliant but new employee who lacks context」と考える — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 公式の推奨:
  - 文脈をあまり知らない同僚にプロンプトを見せ、その人が混乱するなら Claude も混乱する（key test）。
  - 期待以上の作業をしてほしいなら、推測に頼らず明示する。例: `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.`
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-2. Add context / motivation（理由を添える）
- 概要: 「なぜそうするのか」を伝えると、Claude はその意図を他の場面にも当てはめられる — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 公式の例: 「NEVER use ellipses」より「Your response will be read aloud by a text-to-speech engine, so never use ellipses since the text-to-speech engine will not know how to pronounce them.」のほうが効く — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-3. Multishot / few-shot examples（例示）
- 概要: 例を示すと精度と一貫性が上がる — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 公式の推奨:
  - 関連性があり、多様で、構造化された例を `<example>` / `<examples>` タグで囲む。
  - 3〜5個が最もよい結果になる。
  - 例が適切かどうかを Claude に評価させたり、追加の例を作らせたりしてもよい。
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-4. XML tags（構造化）
- 公式の推奨: `<instructions>` `<context>` `<input>` のように一貫した説明的なタグ名を使い、`<documents>` の中に `<document index="n">` を入れるように入れ子で階層を表す — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-5. System prompt / Role（役割付与）
- 公式の推奨: system prompt に1文の役割を書くだけでも効く（例: 「You are a helpful coding assistant specializing in Python.」）。自己認識のサンプルとして「The assistant is Claude, created by Anthropic. The current model is Claude Opus 5.5.」も示されている — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-6. Long context prompting（2万 token を超える長文）
- 公式の推奨:
  - 長い文書はプロンプトの**先頭**に置き、質問と指示を末尾に置く。テストでは品質が最大30%向上した（特に複数文書の場合）。
  - 文書は `<document>`、`<document_content>`、`<source>` で包む。
  - 回答の前に、関係する部分を引用させて根拠を固める。
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-7. Chain of thought / Thinking
- 公式の推奨:
  - 4.6以降は adaptive thinking を優先する。手書きの手順より「think thoroughly」のような一般的な指示のほうがよい。
  - thinking がオフのときだけ、手動の CoT（推論を書かせてから `<answer>` タグに答えを入れる）を使う。
  - 自己チェックには「Before you finish, verify your answer against [test criteria].」と書く。ただし Opus 5 は自分で検証するので、この指示は外す。
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 新しいモデルでの注意:
  - `<thinking>` タグに推論を書かせる指示は拒否されることがある。
  - Opus 4.5 は thinking オフのとき「think」という語に敏感なので、「consider」「evaluate」に言い換える。
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 移行: `thinking={"type":"enabled","budget_tokens":N}` から `thinking={"type":"adaptive"}` と `output_config={"effort":"high"}` の組み合わせへ。`budget_tokens` は4.7以降で400エラーになる — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 推論の読み方: 推論を本文に再現させる指示は `reasoning_extraction` で拒否されることがある。summarized thinking（`display: "summarized"`）で読むか、短い説明を求める — [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- 確認日: 2026-10-29

#### 4-8. Prefilling（廃止）
- 概要: Claude 4.6 と Mythos Preview 以降では、最後の assistant メッセージを prefill すると400エラーになる — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 移行先:
  - 形式の強制 → structured outputs
  - 前置きを省く → 直接指示する
  - 不要な拒否を避ける → user メッセージで明確に指示すれば足りる（「Claude is much better at appropriate refusals now」）
  - 続きを書かせる、文脈を補う → user ターンに入れる、ツールを使う、compaction を使う
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-9. Prompt chaining（プロンプトの連結）
- 概要: adaptive thinking とサブエージェントが多段の推論の多くを内部でこなすようになった。それでも中間出力を確かめたい場合には、明示的な chaining が有効 — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 代表的なパターン: 下書き → 基準に照らしたレビュー → 改善 — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-10. 出力形式と冗長さの制御
- 公式の推奨:
  - 「何をするか」を書き、「何をしないか」は書かない（「Do not use markdown」より「smoothly flowing prose paragraphs で書く」）。
  - XML の形式指示を使う。
  - プロンプト自体の書き方を、望む出力の書き方に合わせる（プロンプトから markdown を減らすと出力の markdown も減る）。
  - LaTeX が不要なら plain text を指定する。
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 冗長さの傾向:
  - 最新モデルは簡潔で、ツール使用後の要約を省くことがある。必要なら「After completing a task that involves tool use, provide a quick summary of the work you've done.」と書く。
  - Opus 5 は冗長なので、簡潔さを明示的に求める。
  - Fable 5.1 は進捗報告が少ないので、明示的に求める。
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-11. Tool use（行動するか提案にとどめるか、並列呼び出し）
- 行動と提案: 「Can you suggest…?」と聞くと提案だけで終わることがある。実行してほしいなら「Change this function…」のように明示する。system prompt で `<default_to_action>`（積極的に実行）か `<do_not_act_before_instructions>`（慎重に待つ）を指定する — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 強すぎる表現: Opus 4.5 / 4.6 は system prompt に強く反応する。「CRITICAL: You MUST use this tool」は「Use this tool when…」に和らげる — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 並列ツール呼び出し: 既定で並列に行う。さらに促すなら `<use_parallel_tool_calls>` ブロックを使い、抑えたいなら逐次実行を指示する — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-12. 考えすぎ・作り込みすぎ・テストへの迎合の抑制（agentic coding 向け）
- 考えすぎ・探索しすぎ: 「Default to using [tool]」より「Use [tool] when it would enhance your understanding」と書く。一つの方針を選んだらそれを貫かせる（「choose an approach and commit to it」）— [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 作り込みすぎ: 「The right amount of complexity is the minimum needed for the current task.」 — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- テストへの迎合: テストケースだけでなく、すべての有効な入力で正しく動く実装を求める。テストが誤っていたら回避せずに報告させる — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- コードに関するハルシネーション: `<investigate_before_answering>`（開いていないコードについて推測しない）を使う — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 自律と安全のバランス: `rm -rf`、`git push --force`、外部への投稿などは確認を取らせ、`--no-verify` のような安全チェックの回避を禁じる — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 長時間タスク:
  - 状態は JSON、進捗メモは自由記述、チェックポイントは git で管理する。
  - 最初のウィンドウ用には別のプロンプトを用意する。
  - 「compaction されるので早めに終わらせなくてよい」と伝える。
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- フロントエンドデザイン: 指示がないと汎用的な「AI slop」デザインに寄る。`<frontend_aesthetics>` ブロックで Inter / Roboto や紫グラデーションを避けるよう指定する — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-13. モデル別の差分（最新世代の要点）
- Opus 5.5 — [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
  - 既定 effort は medium。thinking は常時オンで、オフにできない。
  - medium で Opus 5 の high 相当かそれ以上。low でも多くのコーディング評価で近い性能を出す。
  - 思考を減らしたいなら、プロンプトで指示するより effort を下げるほうが確実。
  - 図表やスクリーンショットの読み取りが大幅に向上したので、旧モデル向けの補助を見直す。
  - 貼り付けた外部テキストはランダムIDの付いたタグで包み、その中の指示には従わないよう system prompt に書く（prompt injection 対策）。
- Opus 5 — [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
  - 既定で冗長なので「Keep responses focused, brief, and concise.」と書く。
  - 自分で検証するので「double-check」指示は外す。
  - スコープを守らせる: 「Deliver what was asked, at the scope intended.」
  - サブエージェントを抑える: 「Do not delegate work you can finish yourself in a handful of tool calls…」
- Sonnet 5.5 — [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
  - low / medium では確認のために止まりすぎ、high 以上では頼まれていないことまでやりがち。
  - 最後までやり切らせる: 「Keep working until everything the user asked for is done…」
  - 追加作業を抑える: 「Don't add features, tests, files, docs or refactors that weren't asked for.」
  - アイデアや計画を求めたときは、それを出したら止めて着手しないよう指示する。
  - 最小の thinking 設定として `between_tools` がある。
- Fable 5.1 — [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)
  - 自律実行の冒頭文を推奨している: 「You are operating autonomously. The user is not watching in real time…」
  - ターンを終える前に、最後の段落が計画や約束で終わっていないか確認させる。
  - low effort では検索を減らして記憶で答えがちになる。名前を知っていることと、その現状を知っていることは別。
  - 書式を控えめにする傾向があるので、古い反書式ルールは外す。
  - 密すぎる文章には「Please remove all mannered prose.」
- Haiku 5.5 — [Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)
  - 今日の日付を渡す: 「The current date is {{current_date}}.」
  - 「何でも検索」という一律の指示は過剰検索を招く。
  - low では早く止まりがちで、medium に上げると半減した。
  - system prompt を守り続けさせる: 「The rules in this system prompt hold for the whole conversation…」
- 共通の移行注意: thinking block は改変せずに返す。履歴は追記のみにする。system や tools を途中で変える代わりに、会話途中の system message を使う — [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 確認日: 2026-10-29

#### 4-14. 公式ツールと学習教材
- 公式チュートリアル — [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview):
  - GitHub のインタラクティブチュートリアル: Claude 3 世代向けに書かれたもので、食い違う点は Prompting best practices に従うよう注記されている（[github.com/anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)）。
  - Google Sheets 版の軽量チュートリアル。
- Prompt generator: Overview から metaprompt ノートブック（[Claude Cookbooks metaprompt.ipynb](https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/metaprompt.ipynb)）にリンクされている — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
- Console の prompt tools 退役（2026-07-17 告知）:
  - 旧 Workbench は 2026-08-17 に終了した。
  - 生成・改善・テンプレート化の experimental API（`/v1/experimental/generate_prompt`、`improve_prompt`、`templatize_prompt`）も同日に退役した。
  - 新しい Workbench（playground）では、保存済みプロンプト・変数・eval に対応していない。
  — [Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- 旧 docs の「prompt-generator」「prompt-improver」ページは、現在 Prompting best practices へ302リダイレクトされる（2026-10-29 に確認）— [prompt-improver（リダイレクト元）](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/prompt-improver)
- Claude 固有ではない一般的な指針として、ブログ記事「best practices for prompt engineering」もある — [Claude blog](https://claude.com/blog/best-practices-for-prompt-engineering)
- 確認日: 2026-10-29

### Inferences
- 公式ガイドは API と system prompt を前提に書かれているが、アプリユーザーにもそのまま使える原則が多い。たとえば「理由を添える」「例を3〜5個」「長文資料は先に置き、質問は最後」「禁止ではなく望む形で指示する」「提案ではなく実行を頼むなら動詞で明示する」「強い大文字の命令は逆効果になりうる」。教材では、API 固有の項目（prefill、budget_tokens、thinking block の扱い）と、アプリでも使える項目を分けて示すとよい。
- 「推論を本文に全部書いて」という依頼は、新しいモデルでは拒否されることがある。アプリユーザーには「thinking の要約を見る／短い根拠説明を頼む」へ置き換えるよう教えるのが安全。
- 古いチュートリアルや外部記事にある「prefill で JSON を強制する」「budget_tokens を指定する」「`<thinking>` タグに推論を書かせる」は、現行モデルでは非推奨か使えないので、「旧来の技法」として注意書きを付けるべきだ。

### Gaps
- GitHub のインタラクティブチュートリアル（anthropics/prompt-eng-interactive-tutorial）の章立てと最終更新日は、取得が許可されず確認できなかった。学習知識では「Basic Prompt Structure / Being Clear and Direct / Assigning Roles / Separating Data from Instructions / Formatting Output & Speaking for Claude / Precognition / Using Examples / Avoiding Hallucinations / Building Complex Prompts」と付録（Chaining、Tool Use、Search & Retrieval）だが、**未検証**。
- anthropics/courses リポジトリの現在の構成も未確認。
- Console の新 Workbench（playground）に prompt generator / improver の UI が残っているかどうかは確認できなかった（API は退役済み）。
- 旧来の単独ページ（Be clear and direct、Use XML tags など）は、best practices に統合されたように見える（overview がそう説明している）。ただし各旧URLのリダイレクト先を一つずつは確認していない。

---

## 5. API / SDK の概念（パワーユーザー向けに概念だけ）

### Takeaway
パワーユーザーが概念として押さえておきたいのは次のとおり。Messages API と tool use のループ。コストに効く prompt caching（読み取りは基本単価の0.1倍、最新モデルではさらに安い）と Batch（50%引き）。構造を保証する structured outputs。根拠を返す citations。長時間 agent 向けの context 管理（compaction、context editing、memory tool）。「Claude Code をライブラリとして使う」Agent SDK と、「Anthropic がホストする agent harness」の Managed Agents の違い。アプリの Project knowledge cache や自動 context 管理は、これら API 概念のアプリ版と捉えると分かりやすい。

### Cited Findings

#### 5-1. Messages API と Tool use
- Client tools: アプリ側で実行する。Claude が `stop_reason: "tool_use"` と `tool_use` ブロックを返し、アプリ側が `tool_result` を返す — [Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- Server tools: Anthropic 側で実行する（web_search / web_fetch / code_execution / tool_search）— [同上](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- 呼び出しの制御: `tool_choice` は既定で auto。必ず呼ばせたいならプロンプトではなく tool_choice で指定する。スキーマ通りの呼び出しを保証するなら `strict: true`。SDK の tool runner はツール実行の往復を肩代わりする — [同上](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- どのツールをいつ呼ぶかは、依頼内容とツールの description から Claude が判断する — [同上](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- オーバーヘッド: tools を指定すると隠れた system prompt が加わる（Opus 5.5 / Sonnet 5.5 で auto のとき286 token）— [同上](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- Opus 5.5 では強制 tool use（`tool_choice` の any / tool）が400エラーになる。auto / none と strict または structured outputs で代替する — [What's new in Claude Opus 5.5](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5)
- 確認日: 2026-10-29

#### 5-2. Prompt caching
- 仕組み: tools → system → messages の順にプレフィックスを再利用する。100%一致した場合だけヒットする。出力内容には影響しない。自動キャッシュ（トップレベルの `cache_control`）と、明示的なブレークポイント（最大4つ）がある — [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- TTL と料金: TTL は5分（使うたびに無料で延長）と1時間。書き込みは基本単価の1.25倍（5分）または2倍（1時間）、読み取りは0.1倍。Fable 5.1 では0.025倍、Opus 5.5 / Sonnet 5.5 では0.05倍 — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- 最小長: キャッシュできる最小の長さはモデルによって512〜4,096 token — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- キャッシュが無効になる操作:
  - tool 定義の変更 → すべて無効
  - system の変更 → system 以降が無効
  - thinking や effort の変更 → messages 以降（モデルによってはそれより前も）が無効
  — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- 公式の推奨: ブレークポイントは、リクエスト間で変わらない最後のブロックに置く — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- アプリ側の対応物: project knowledge は cache され、再利用時の消費が少ない — [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- 確認日: 2026-10-29

#### 5-3. Message Batches API
- 料金: すべて標準価格の50%。prompt caching の割引と重ねられる（ただし cache ヒットはベストエフォートで30〜98%）— [Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- 処理時間: 多くは1時間以内に終わる。24時間で期限切れになり、期限切れ分は課金されない — [同上](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- 上限: 1バッチは100,000リクエストまたは256MBまで — [同上](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- 用途: 大規模な評価、モデレーション、大量のコンテンツ生成 — [同上](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- 確認日: 2026-10-29

#### 5-4. Structured outputs
- 概要: JSON outputs（`output_config.format`。応答そのものの形式を決める）と strict tool use（`strict: true`。ツール呼び出しの形式を検証する）の2つ。constrained decoding によってスキーマ準拠を保証する — [Structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- 保証されない場合: 拒否、max_tokens での途切れ、enum の大文字小文字 — [同上](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- 制約: citations と併用できない（400エラー）。再帰スキーマや数値範囲などには非対応 — [同上](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)
- 推論タスクでの使い方: structured outputs を優先する。adaptive thinking と組み合わせるなら「Think the problem through before you answer.」を system prompt の最後に加える — [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
- 確認日: 2026-10-29

#### 5-5. Citations
- 概要: 各主張を支える原文の箇所を返す。対応形式は plain text（文単位で分割）、PDF（ページ番号）、custom content（ブロック単位）— [Citations](https://platform.claude.com/docs/en/build-with-claude/citations)
- プロンプトで引用させる方法に比べた利点: cited_text は出力 token に数えられない。指し示す位置が有効であることが保証される。最も関連する引用を選ぶ精度も高い — [同上](https://platform.claude.com/docs/en/build-with-claude/citations)
- 制約: 画像は引用できない。structured outputs と併用できない — [同上](https://platform.claude.com/docs/en/build-with-claude/citations)
- 確認日: 2026-10-29

#### 5-6. Files API / PDF / Vision
- Files API: PDF・画像・テキストを一度アップロードすれば、毎回送り直さずに再利用できる。2026-08-19 に beta を終了した — [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview)、[Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- PDF support（テキストと図の両方を分析）と Vision は GA — [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview)
- 確認日: 2026-10-29

#### 5-7. Context 管理（compaction / context editing / memory tool）
- Compaction（beta）:
  - 古いターンを、サーバー側で Claude が書いた要約に置き換える。会話が長くなるほど品質が落ちるので、作業中の context を小さく保つ目的もある。
  - 呼び出し側が任意のタイミングで実行する on-demand（`compact-2026-09-04`）と、指定した閾値で自動実行する方式がある。公式は on-demand を推奨している。
  — [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction)
- Context editing（beta）:
  - 古いツール結果（`clear_tool_uses_20250919`）や thinking block（`clear_thinking_20251015`）を、ルールに従ってサーバー側で消す。
  - 多くの用途ではサーバー側の compaction が主な手段で、context editing はより細かく制御したいときに使う。
  — [Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)
- Memory tool:
  - `/memories` ディレクトリのファイルを会話をまたいで残す。client-side で、保存先はアプリが決める。
  - 公式は「compaction で context を小さく保ち、memory で要約後も残すべき情報を保存する」組み合わせを推奨している。
  - path traversal 対策が必須。
  — [Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
- 確認日: 2026-10-29

#### 5-8. その他の最新 API 機能（名前と用途だけ）
- 機能一覧 — [Features overview](https://platform.claude.com/docs/en/build-with-claude/overview):
  - Advisor tool（beta）: 速い executor と賢い advisor を組み合わせる。
  - Tool search: ツールを必要になったときに検索して読み込む。
  - Programmatic tool calling: code execution のコンテナから自前のツールを呼ぶ。
  - MCP connector（beta）: Messages API から直接リモート MCP に接続する。
  - Agent Skills: progressive disclosure で context を節約する。
  - Server-side fallback（beta）: 拒否されたリクエストを別のモデルで再試行する。
  - Data residency: `inference_geo`。"us" を指定すると料金が1.1倍になる（[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)）。
- 会話の途中で設定を変える機能 — [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)、[Platform release notes](https://platform.claude.com/docs/en/release-notes/overview):
  - Mid-conversation system messages
  - per-message effort（beta。cache を維持できる）
  - Task budgets（beta）
- Fast mode: 出力が最大2.5倍速くなる。Opus 5.5 は 2026-10-15 に research preview を終了し、料金は入力$8 / 出力$40 — [Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)、[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- Web search: 1,000回あたり$10。Code execution は web search / web fetch と併用すれば無料 — [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- 確認日: 2026-10-29

#### 5-9. Agent SDK と Managed Agents、Client SDK の違い
- Agent SDK:
  - 「Claude Code as a library」。Claude Code と同じツール、agent loop、context 管理を Python / TypeScript から使える。
  - built-in tools、hooks、subagents、MCP、permissions、sessions、skills / commands / memory（`.claude/` から読み込む）、plugins に対応する。
  - Anthropic の事前承認がない限り、第三者が自社製品で claude.ai ログインやプランの rate limit を提供することは認められていない。
  — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- Agent SDK を自分のプランで使う方法についての Help Center 記事もある — [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)
- 使い分け表:
  - 自分のプロセスに agent を組み込む → Agent SDK
  - 対話的な開発 → Claude Code CLI
  - API を直接呼んでループを自分で書く → Client SDK
  - Anthropic にホストさせる → Managed Agents
  — [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- Managed Agents（beta、2026-04-08 開始）:
  - 構成要素は Agent（モデル・system prompt・tools・MCP・skills）、Environment（Anthropic のクラウドサンドボックスか自前ホスト）、Session、Events。
  - 長時間の非同期作業、状態を持つセッション、定期実行に向く。
  - ZDR と HIPAA BAA の対象外。
  - 料金はセッション1時間あたり$0.08（running 中のみ）。
  — [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview)、[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- 確認日: 2026-10-29

### Inferences
- 「claude.ai の project knowledge cache ↔ prompt caching」「自動 context 管理 ↔ compaction」「Memory ↔ memory tool」「Skills（アプリ）↔ Agent Skills（API）」「Cowork / scheduled tasks ↔ Managed Agents の scheduled deployments」のように、アプリと API の概念を対応させて見せると、「なぜ長い会話は重いのか」「なぜ資料は project に置くべきか」をアプリユーザーにも仕組みから説明できる。
- Opus 5.5 や Fable 5.1 では thinking block を改変せずに返す必要があり、履歴の編集も制限されている。アプリの「会話途中からの分岐ができない」という制約（統合体験の制限）と関係している可能性があるが、公式には明言されていない（推測）。

### Gaps
- Tool search、Programmatic tool calling、Advisor tool の詳細ページは取得していない（概要表のみ）。
- Agent SDK を Claude プランで使う場合の具体的な条件（Help Center 記事 15036540）は本文を取得していない。

---

## 6. 限界に関する公式ガイダンス（ハルシネーション、knowledge cutoff、検索を使う場面）

### Takeaway
公式のハルシネーション対策は7つ。「分からないと言ってよい」と許可する、直接引用で根拠を固める（2万 token 超の文書）、主張ごとに出典を付けさせ引用できない主張は撤回させる、thinking の要約を確認する、同じプロンプトを複数回実行して比べる（Best-of-N）、出力を入力に回して検証する、提供した資料だけを使うよう限定する。公式は「これらで大きく減るが、ゼロにはならない」と明言している。現行モデルの reliable knowledge cutoff は2026年6月なので、それ以降の情報や、変わりうる事実（料金、規約、最新状況）は検索で確かめるのが前提。

### Cited Findings
- ハルシネーション低減の基本策 — [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations):
  - ①「分からない」と言うことを明示的に許可する（「This technique can drastically reduce false information」）。
  - ②2万 token を超える文書では、先に一字一句の引用を抜き出させる。
  - ③各主張に引用を付けさせ、引用が見つからない主張は撤回させる。
- 応用策 — [同上](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations):
  - ④thinking を `display: "summarized"` で返させ、答えが怪しいときに推論を確認する。
  - ⑤Best-of-N: 同じプロンプトを複数回実行し、出力が食い違えばハルシネーションの兆候と見る。
  - ⑥出力を次のプロンプトに渡して検証させる。
  - ⑦提供した資料だけを使い、一般知識を使わないよう指示する。
- 限界: 「they don't eliminate them entirely. Always validate critical information, especially for high-stakes decisions」 — [同上](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- Knowledge cutoff: 現行4モデル（Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5）の reliable knowledge cutoff はすべて2026年6月 — [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)
- 検索を使う場面（アプリ）: 単純な事実確認は web search、最新情報が不要な複雑な推論は thinking、包括的な調査は Research — [When should I use web search, extended thinking, and research?](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research)
- 検索を使う場面（API とモデル別の指針）:
  - Fable 5.1 は low effort だと記憶で答えがちになる。名前を知っていても現状を知っているとは限らないので、検索させる。
  - Haiku 5.5 には現在の日付を渡す。
  - Sonnet 5.5 では「許可されていること、必要なこと、料金のように変わりうる詳細」を検索で確かめるよう指示する。
  — [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)、[Prompting Claude Haiku 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)、[Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)
- コードに関するハルシネーション: 開いていないファイルについて推測させない（`<investigate_before_answering>`）— [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 医療（服薬量）: 子どもの用量は記憶ではなく製品ラベルのみに基づく、という system prompt ブロックが公式に用意されている — [同上](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- 自己申告への注意: Opus 5.5 の無人実行では、テキストだけの `end_turn` は「報告」であって完了の証明ではない。チェックリストで確認する — [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)
- 自動化の限界: 承認や auto-mode の分類器を、モデルがすり抜けることがまだある — [Introducing Claude Mythos and Fable 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)
- Artifact の不具合: 「Try fixing with Claude」ボタンで直せることがあるが、成功は保証されない — [What are artifacts](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)
- 確認日: 2026-10-29

### Inferences
- アプリユーザー向けには、①「分からなければそう言って」と添える、②資料を渡したら「この資料の範囲だけで、引用付きで」と頼む、③重要な結論は新しいチャットで同じ質問をして比べる、④2026年6月以降の情報や料金・規約は検索させる、の4つが、公式の7策をすぐ実践できる形に言い換えたものになる。
- 「AI が完了したと言った ≠ 完了した」（Opus 5.5 ガイドの end_turn の注意）は、Cowork や agentic な使い方が広がる中で、中級者に特に伝えるべき点だと考えられる。

### Gaps
- Help Center にある「Claude の knowledge cutoff と、cutoff 以降の情報の扱い」専用記事は、検索上限のため取得できなかった（web search 記事にリンクがあることだけ確認）。
- 公式の「Increase output consistency」「Mitigate jailbreaks」「Reduce prompt leak」ページは名前を確認しただけで、本文は取得していない（[Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) のサイドバー）。
