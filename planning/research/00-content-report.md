# 三つの原理と症状索引で Claude 辞典を組み立てる

この教材の中心に書くべきなのは、機能の一覧ではない。「なぜうまくいかないか」と「次に何を足し、どう確かめるか」という判断である。Claude Code の公式ドキュメントはすでに日本語を含む11言語に訳されていて（各228ページ）、翻訳や機能ツアーでは付加価値が出にくい ([Claude Code docs llms.txt](https://code.claude.com/docs/llms.txt))。その公式自身が、うまくいかないセッションの原因を四つに分けている。「Claude に見えない情報」「検証手段の欠如」「例外を許さないルールをお願いで守らせている」「既定値の手間とコスト」である。さらに指示を「Claude が判断するもの」と「Claude Code が必ず実行するもの」に二分している ([Best practices](https://code.claude.com/docs/en/best-practices))。本報告はこれを「見せる・確かめる・縛る」の三原理と、研究と実践知で広げた六つの失敗原因に整理し直し、全ページ共通のメタデータにすることを提案する。そうすれば、kyopro-atlas 形式の逆引き・知識マップ・ロードマップを、症状と原因と委任の段階から自然に生成できる。構成案は**20分野・300ページ候補**で、そのうち初版に必須とするのは**151ページ**である。中でも逆引きの受け皿になる症状辞典と、古くなった助言の台帳を最優先にする。差別化の核は四つある。症状から引ける索引、検証と無人実行の信頼性、日本語の出力品質、確認日と版を持つ「古くなった助言」の台帳である。どれも既存の日本語書籍・講座・記事ではほぼ空白になっている。Claude Code は2026年1月から10月末までに約235版が出るほど変化が速い ([npm registry](https://registry.npmjs.org/@anthropic-ai/claude-code))。鮮度の管理を後付けにせず設計の一部にしなければ、公開から数か月で誤った助言を配る辞典になってしまう。

## 1. 2026年の重心は「機能を覚える」から「任せて確かめる」へ移った

### 公式は失敗を四つに分け、「お願い」と「鍵」を区別する

公式は Claude Code を「モデルを包むエージェントのハーネス」と定義している。Claude は「文脈を集める → 行動する → 結果を確かめる」のループで動き、ツールの結果が次の判断に戻る ([How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works))。この前提から、推奨のほぼすべてが三つの問いに行き着く。何を見せるか、どう確かめさせるか、どこまで仕組みで縛るか、である。

現行の Best practices は冒頭で、期待どおりに進まなかったセッションはほぼ四つのどれかに当たると述べる。リポジトリを読んでも得られない情報が足りない場合、作業を確かめる手段がない場合、絶対に起きてはならないことを prompt だけで保証しようとしている場合、結果は正しいが時間・トークン・承認の手間が見合わない場合である。そのうえで、prompt・CLAUDE.md・skill を「従う保証のない非決定論的な指示」、hook・deny rule・managed setting を「ハーネスが毎回必ず実行する決定論的な制御」として分けている ([Best practices](https://code.claude.com/docs/en/best-practices))。

同じページには「もうやめてよい古い助言」の表もある。挙がっているのは「コンテキストを最優先で節約する」「IMPORTANT や全大文字で強調する」「think hard と書く」「keep going と書く」「アーキテクチャを CLAUDE.md に書く」である。コンテキストについては、現行モデルの多くが 1M window を持ち compaction も自動なので「溢れる」ことはまれだ、と理由を述べている。ただし回答の質とコストのために、/clear は今も有効とされる ([Best practices](https://code.claude.com/docs/en/best-practices))。つまりコンテキストの扱いは、「溢れさせない技術」から「質とコストのために机を整える習慣」へ意味が変わった。

2026年6月の公式ブログも同じ立場をとる。CLAUDE.md・rules・skills・subagents・hooks・output styles を「いつ読み込まれるか・圧縮を生き延びるか・どれだけの権威を持つか」で比べ、「Never do X」は指示として書いてもガードレールにならないと明言した ([Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more))。

モデルとプロンプトの公式指針も同じ方向を向いている。Prompting best practices は自らを「living reference」と呼び、基本に五つを置く。Claude を「文脈を持たない優秀な新人」として扱うこと、理由を添えること、例を3〜5個示すこと、長い資料を先頭に置くこと（公式のテストで品質が**最大30%向上**）、否定形ではなく望む形で書くことである ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices))。最新世代に向けては注意点も三つ挙げている。「CRITICAL: You MUST」のような強い言い回しは過剰反応を招くので和らげること、**prefill は Claude 4.6 以降で**エラーになること、**`budget_tokens` は 4.7 以降で**エラーになることである（同上）。

モデル選択についての公式の立場は「迷ったら Opus 5.5 から始める」「モデルを替えるより effort を調整するほうが効くことが多い」である ([Choosing the right model](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model))。モデルごとの癖も文書になっている。Opus 5 は自分で検証するので「double-check して」と書くと過剰検証になる。Sonnet 5.5 は low・medium では確認のために止まりすぎ、high 以上では頼まれていないことまでやる ([Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5); [Prompting Claude Sonnet 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5))。教材が「良いプロンプトの型」を一つだけ示して済ませられない理由がここにある。

アプリ側の公式は、まず指示の置き場所を切り分けている。アカウント全体に効かせるなら Instructions for Claude、案件ごとなら project instructions、応答の形式や手順なら skills である ([Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features))。調べ方も使い分けを示す。1〜2回の検索で済む事実確認は web search、最新情報を要しない複雑な推論は thinking、5回以上の検索を重ねる調査は Research である ([When should I use web search, extended thinking, and research?](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research))。安全については二条件のモデルを示している。prompt injection は「信頼境界の外の情報を読める」と「被害につながる行動ができる」の両方がそろって成立するので、片方を外せばよい ([Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely))。

Claude Code の auto mode についても、公式は「承認の手間は減らすが安全を保証しない」と書く。`bypassPermissions` は隔離したコンテナか VM でだけ使うよう求めている ([Permission modes](https://code.claude.com/docs/en/permission-modes))。

公式の考え方をまとめると、次の四つになる。Claude には必要なものだけを見せる。完了は証拠で判定する。例外を許さないことは仕組みに任せる。任せる幅を広げるほど封じ込めを強める。

### 実践者は検証・計画・分割・書き戻しで一致し、量と自律度で割れる

英語圏で最も強い合意は、Claude が自分で実行できる検証手段を渡すことである。テスト、ビルドの終了コード、ブラウザ、スクリーンショット比較などがこれに当たる。Claude Code の作者 Boris Cherny はこれを「最も重要な tip」と呼び ([paddo.dev](https://paddo.dev/blog/how-boris-uses-claude-code))、Simon Willison や Armin Ronacher も同じ趣旨を述べている ([Simon Willison](https://simonwillison.net/2025/Sep/30/designing-agentic-loops); [Armin Ronacher](https://lucumr.pocoo.org/2025/12/22/a-year-of-vibes/))。

これに次の三つが続く。計画を先に固めること。完了を定義できる単位にタスクを切ること。ミスのたびに CLAUDE.md・スクリプト・hook へ再発防止策を書き戻すことで、Mitchell Hashimoto はこれを harness engineering と呼ぶ ([Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey))。Anthropic が約40万セッションを分析した研究も、熟練者との差は長さではなく具体性に出ると報告している。具体性とは「対象ファイル・シナリオ・完了の意味・倣うパターン」を書くことである。熟練者のセッションは、1回の依頼あたりの仕事量がむしろ大きい。ただしこの研究は二次要約でしか確認できていない ([Analytics Vidhya](https://www.analyticsvidhya.com/blog/2026/08/claude-code-best-practices-analysis/); [Creeta](https://news.creeta.com/en/claude-code-expertise-domain-over-coding-2026/))。

日本語圏の合意もほぼ同じ六点に収まる。コンテキストを最重要の資源として扱うこと、Plan を先に作ること、検証手段を与えること、CLAUDE.md を短くして守らせたいことは Hooks や permissions で強制すること、タスクを小さく切って要点をファイルに外出しすること、別のコンテキストでレビューすることである。クラスメソッドはこれを「同じ注意を2回したら、それは仕組みに落とすタイミング」と表現した ([DevelopersIO](https://dev.classmethod.jp/articles/lt-devio2026-tokyo-harness-engineering/))。

対立があるのは「どれだけ」と「どこまで任せるか」の点である。教材はこれを一つの正解に潰さず、公式の立場、実践者の幅、本辞典の推奨の三段で書くのがよい。

| 論点 | 一方の立場 | 他方の立場 | 教材での扱い |
|---|---|---|---|
| `/init` で CLAUDE.md を作るか | 叩き台に使う（[Boris](https://www.jitendrazaa.com/blog/others/tips/10-claude-code-tips-from-the-creator-boris-cherny-february/)、公式、みのるん） | 1行ずつ手で書く（[HumanLayer 系の要約](https://redreamality.com/garden/notes/library/writing-a-good-claude-md/)、[jyas-protein](https://qiita.com/jyas-protein/items/9cc733d2ed7f80bef7a1)） | 両論を併記する。使うなら削って手で直す |
| CLAUDE.md の長さ | 公式は200行未満（[memory](https://code.claude.com/docs/en/memory)） | 60行の実例（HumanLayer）から、合計500行で見直し（[hikariclaude01](https://qiita.com/hikariclaude01/items/e54c70c90c6aa84d0f66)）まで | 公式値を主とし、実践者の幅を並べて示す |
| 構成説明を CLAUDE.md に書くか | 書かない。Claude は自分で読む（[Best practices](https://code.claude.com/docs/en/best-practices)） | WHAT/WHY/HOW を書く（[Tembo](https://www.tembo.io/blog/how-to-write-a-great-claude-md)） | 推測できない「理由」と落とし穴だけを書く |
| 長い作業の続け方 | 焦点を指定して /compact | 書き出してから /clear（[dsebastien](https://www.dsebastien.net/claude-code-tips-and-best-practices/)） | 要約で失いたくない作業は書き出しを使う |
| 並列セッションの本数 | 5〜10本以上（[Boris](https://paddo.dev/blog/how-boris-uses-claude-code)） | 1本（[Mitchell](https://mitchellh.com/writing/my-ai-adoption-journey)）、上限3〜4本（[marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)） | 1〜3本から始める。上限を決めるのは人間のレビュー能力 |
| モデルの経済 | Opus で計画し Sonnet で実装（[ClaudeLog](https://claudelog.com/faqs/how-to-use-opus-5-in-claude-code/)） | 信頼できる変更1件あたりのコストで考え、常に最強を使う（[Karo Zieminski](https://karozieminski.substack.com/p/boris-cherny-claude-code-workflow)） | 両論に、2026年の価格変化を添える |
| git をどこまで任せるか | 人が握る（[DoltHub](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/)） | PR まで任せる（Boris、[ykdojo](https://awesomeclaude.ai/claude-code-tips)） | 慣れるまでは人が握り、慣れたら draft PR |
| 強調語 | IMPORTANT で遵守率が上がる（[seabat](https://qiita.com/seabat-dev/items/27cb2e1dbd1e9bc1e4b8)） | 過剰適用を招く（[Best practices](https://code.claude.com/docs/en/best-practices)） | 使うのは1行だけ。守られないなら仕組みに移す |
| レビュアーへの指示 | 正しさに関わる指摘だけ出させる（[Best practices](https://code.claude.com/docs/en/best-practices)） | 全部出させて、別のパスで絞る（[Opus 5 ガイド](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)） | モデルの世代で書き方が変わる例として載せる |
| 仕様をどう先に作るか | 文章の spec を先に書く（[cc-sdd](https://github.com/gotalab/cc-sdd)） | モックを先に作る（[kazuki_ogawa](https://qiita.com/kazuki_ogawa/items/f1a15a199d9f91fe6080)） | 作業の型の選択肢として並べる |
| 日本語か英語か | 日本語で問題ない（[入江](https://devtools.shingoirie.com/blog/claude-code-japanese-claude-md-guide/)） | プログラミングは英語が有利な場合もある（[仁頼](https://jinrai.co.jp/blog/claude-japanese/)） | 測定データがない。言語より構造を優先する |
| カスタムコマンドや hooks | 1日に2回やることは skill にする（Boris） | ほとんど使わなくなった（[Armin](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/)） | 足すきっかけと剪定をセットで教える |

日本語圏には固有の重心がある。最も読まれたのは二つで、公式ベストプラクティスを21枚に要約したスライド（64k views）と、非エンジニアの日常業務への応用記事（Qiita 2,374いいね）である。需要は「公式の忠実な体系化」と「コードを書かない使い方」に集中している ([みのるん Speaker Deck](https://speakerdeck.com/minorun365/claude-codebesutopurakuteisumatome); [みのるん Qiita](https://qiita.com/minorun365/items/114f53def8cb0db60f47))。一方で、「自称完全ガイド」や AI 生成風の有料記事には強い反発がある。「changelog を追っていればわかるが誇張のない良心的な記事」といった整理のほうが評価されている ([はてブ 417](https://b.hatena.ne.jp/entry/s/zenn.dev/417/articles/c15af4f4106a9f); [はてブ wataru86](https://b.hatena.ne.jp/entry/s/qiita.com/wataru86/items/b859f1578191a1e15808))。public に公開する教材にとって、誇張せず出典を示すことは信頼の条件そのものである。

日本語特有の論点は、「日本語で書くと精度が落ちるか」よりも出力の側にある。Opus 5.5 は英語のツール出力を読んだ後に英語へ戻ることがあり、hook で強制的に止める解決策が出ている ([DevelopersIO](https://dev.classmethod.jp/articles/claude-code-hooks-prevent-english-reply/))。textlint を PostToolUse hook で走らせて文体を揃える手法もある ([Zenn](https://zenn.dev/yuki_fujisawa/articles/a01e472dc190cf))。日本語推敲 skill を比べた記事は 342 いいねを集めた ([Qiita](https://qiita.com/inoyu-qiita/items/0ffe6e74ecaf3aaa8b14))。どれも「お願いでは揺れるものを仕組みで縛る」という背骨を、日本語に当てはめた例である。

### 既存教材は機能順の一本道で、症状・検証・鮮度が空白のまま

既存教材のほぼすべては、「導入 → CLAUDE.md → コンテキスト管理 → 計画 → MCP / サブエージェント / Hooks / Skills → GitHub / CI」という機能順の一本道で組まれている。日本語の Claude Code 専門書だけで、2025年12月から2026年9月までに少なくとも11冊が出た ([クリスタルメソッド](https://crystal-method.com/blog/claude-code-books/))。辞典的と評される齊藤本も機能別の章立てで、症状からは引けない。

この構成のせいで、空白が三つ残っている。一つ目は**症状から引く索引**で、先行例は2025年6月の Zenn 記事「逆引きコマンド事典」と、公式 Best practices 冒頭の症状対応くらいしかない ([Zenn](https://zenn.dev/ml_bear/articles/84e92429698177))。二つ目は**検証と無人実行の信頼性**で、これを独立した章として扱うのは公式の Claude Code in Action（Verify and Share）など少数にとどまる ([DataCamp](https://www.datacamp.com/ja/courses/claude-code-in-action))。三つ目は**陳腐化した Tips の撤回**で、明示的に撤回しているのは公式の「What you can stop doing」表くらいである。

陳腐化は公式教材にも起きている。公式コース Introduction to Subagents は `/agents` での作成を教えているが ([pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/371/anthropic-academy-free-courses-claude))、このウィザードは v2.1.198（2026-07-01）で削除された ([CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md))。公式のインタラクティブなプロンプト教材も Claude 3 世代向けのまま残っていて、食い違う点は Prompting best practices に従うよう注記されている ([Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview))。

日本語には、さらに四つの空白がある。claude.ai の Research と Artifacts を深く使う方法、日本語の文書品質を仕組みで担保する体系、効果の測り方、そして人間側の負荷である。人間側の負荷については、auto mode で承認の連打が減った代わりに「レビュー地獄」になったという報告がある ([DevelopersIO](https://dev.classmethod.jp/articles/devio2026-tokyo-claude-code-automode-unattended-environment/))。並列作業によって**42%が疲労感の増加**を訴えた企業事例もある ([CodeKnights](https://www.codeknights.co.jp/contents/claude-japan-cases-2026summer))。注釈付きのセッション記録を中心に据えた教材は、日英どちらでも見つからなかった。

### 2026年の変化は統合・自律の既定化・effort 中心の制御に集約される

| 領域 | 変化 | 時期 | 教材への影響 | 出典 |
|---|---|---|---|---|
| アプリ | Chat と Cowork が一つの会話に統合された。どの会話でもファイル作成・コード実行・タスク・skills・connectors が使える | 2026-09-16 | 「Cowork は別アプリ」「Web search はトグルで有効化」は古い | [統合の記事](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude) |
| アプリ | Memory がトピック単位の個別エントリになり、chat とクラウドの Cowork で共通化された | 2026-07-10、08-25 | 「日次要約」前提の説明は古い | [Release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| アプリ | Artifacts が Docs / Slides / Design / Dashboards / Motion のテンプレート型に作り直された | 2026-09-16 | それ以前の artifact は legacy 扱い | [Artifacts](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) |
| アプリ | Pro/Max の新規タスクはクラウドで実行され、「Only on your computer」は廃止された | 2026-10-06 | ローカル実行を前提にした安全の説明を見直す | [Cowork の面](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile) |
| Claude Code | auto mode が既定になった。有料プランは 08-14 から、ターミナルと VS Code の対話セッション全体は v2.1.283 から | 2026-08〜09 | 「最初は毎回承認を求められる」前提は古い。分類器の限界を教える | [Permission modes](https://code.claude.com/docs/en/permission-modes); [Business Today](https://www.businesstoday.in/technology/news/story/anthropic-is-making-claude-code-more-autonomous-auto-mode-coming-as-default-for-paid-users-548281-2026-08-10) |
| Claude Code | `-p` と SDK では、承認が必要な呼び出しを既定で拒否するようになった | v2.1.302（10-16） | 自動化の説明で必ず触れる | [Permission modes](https://code.claude.com/docs/en/permission-modes) |
| Claude Code | /goal、dynamic workflows（`ultracode`）、agent view、agent teams（実験的）が加わった | 2026-02〜06 | 自作ループや tmux での組織づくりは歴史として扱う | [Agents](https://code.claude.com/docs/en/agents); [goal](https://code.claude.com/docs/en/goal) |
| Claude Code | カスタムコマンドが skills に統合され、`/agents` ウィザードが削除された。AGENTS.md に対応し、Mods が加わった | 2026-01〜10 | 「作り方」記事の多くが古い | [Skills](https://code.claude.com/docs/en/skills); [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| Claude Code | Web 版が「クラウドセッション」として正式提供された | 2026-09-24 | 「Claude Code on the Web」の呼称は古い | [はてブ](https://b.hatena.ne.jp/entry/s/zenn.dev/goat_eat_any/articles/claude-code-cloud-sessions) |
| モデル | 主力が Fable 5.1 / Opus 5.5 / Sonnet 5.5 / Haiku 5.5 になった。いずれも context 1M、最大出力128K、reliable cutoff は2026年6月、thinking は adaptive | 2026-09〜10 | 「200k 前提」は古い。ただし 1M は「全部をよく読める」という意味ではない | [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) |
| モデル | effort が正規の制御手段になった。5.5世代は thinking を切れず、Claude Code の既定 effort は medium | 2026 | `think hard` 系は認識されない。`ultrathink` だけが有効 | [Model config](https://code.claude.com/docs/en/model-config) |
| プロンプト | prefill と `budget_tokens` が使えなくなった。Console の prompt generator / improver API は退役した | 2026-08-17 ほか | 旧技法を台帳にまとめる | [Platform release notes](https://platform.claude.com/docs/en/release-notes/overview) |
| 品質 | 既定 effort の引き下げ、thinking 履歴のバグ、冗長さの制限が重なり、約6週間品質が不安定になった。ポストモーテムが公開された | 2026-03〜04 | 「劣化したと感じたら、まずバージョンと effort を確かめる」 | [InfoQ](https://infoq.com/news/2026/05/anthropic-claude-code-postmortem) |
| 料金 | Fable は Pro では最初から従量課金、Max では週上限の50%まで。usage credits は日本では購入から6か月で失効する | 2026-09 | 料金は1ページに集約し、確認日を付ける | [Fable](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan); [credits](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans) |

表の各行に共通するのは、名前が短期間で揺れていることである。routines は cloud scheduled tasks に、extra usage は usage credits に、workflow というトリガー語は ultracode に変わった。`/simplify` は一度 `/code-review` に改名された後、別機能として再び載っている ([CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md))。npm の公開記録で数えると、2026年1月の v2.0.77 から10月末の v2.1.312 までに約235版が出ている ([npm registry](https://registry.npmjs.org/@anthropic-ai/claude-code))。

ここから設計上の結論が出る。静的な辞書の「仕様」部分は数か月で古くなる。変わりにくいのは「原理」の部分だけである。だから両者をページの中でもメタデータの上でも分けておく必要がある。

## 2. 背骨は「見せる・確かめる・縛る」と六つの「ない」

### 三つの原理と一つの比例則

調査全体を貫く考え方は、三つの動詞と一つの比例則にまとめられる。一つ目の原理「見せる」は、Claude には見せたもの・取りに行けたものしか分からず、見せすぎても劣化する、ということである。二つ目の「確かめる」は、Claude は「終わったように見えた」ところで止まるので、完了は自己申告ではなく証拠で決める、ということである。三つ目の「縛る」は、指示はお願いで仕組みは鍵なので、例外を許さないものは鍵に任せる、ということである。比例則は、任せる幅を広げるほど確かめる仕組みと封じ込めを強める、ということである。

| 原理 | 一文で | なぜ成り立つか（基礎分野で説明する） | 代表的な手段（アプリ / Claude Code / API） |
|---|---|---|---|
| 見せる | 必要なものを見せ、余計なものは片付ける | 毎ターン全履歴を読み直す。attention には限りがある。context rot。知識カットオフ | 具体的な依頼、Projects、新しいチャット / @参照、CLAUDE.md、/clear、handoff 文書、subagent での隔離 / system prompt、prompt caching、compaction |
| 確かめる | 完了は自己申告でなく証拠で決める | エージェントループ。ハルシネーション。reward hacking。非決定性 | 引用、Research の出典、best-of-N / テスト、/goal、Stop hook、独立レビュー / citations、eval |
| 縛る | 例外を許さないものは仕組みに任せる | CLAUDE.md は user message として届く。会話の約束は圧縮で消えうる。prompt injection | connector の承認設定、権限モード、ネットワーク設定 / hooks、permissions deny、sandbox、managed settings、ブランチ保護 / structured outputs、strict tool use |
| 比例則 | 任せる幅に比例して確かめ、封じ込める | 承認疲れ。分類器の見逃し。lethal trifecta | 低リスクから始める、専用フォルダ / 無人実行前の5つの問い、最小権限、`--max-budget-usd` / Rule of Two |

この背骨は既存の枠組みの言い換えであり、新しい学説ではない。見せるは公式の「Claude に見えない情報」と context engineering 論 ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)) に、確かめるは「検証手段」に、縛るは「決定論的な制御」に対応する。比例則は、Claude Code in Action の学習目標「監督の少なさに比例して無人実行の結果を検証する」に対応する ([Anthropic Partners Skilljar](https://anthropic-partners.skilljar.com/claude-code-in-action))。Anthropic の AI Fluency が掲げる 4D（Delegation・Description・Discernment・Diligence）とも重なる ([Ringling LibGuide](https://ringling.libguides.com/ai/framework))。ただし AI Fluency は CC BY-NC-ND なので、用語を引用することはできても、改変した派生フレームワークとして再配布することはできない。本教材は独自の三動詞を立て、4D は参考文献として扱うのが安全である。

### 六つの失敗原因は公式の四分類を研究と実践知で広げたもの

公式の四分類は Claude Code のセッションを念頭に置いている。そのため、チャットで長い会話が劣化すること、引用を幻覚すること、悪意ある入力に乗っ取られることは、そのままでは収まりにくい。そこで、コンテキストの劣化研究 ([Chroma](https://www.trychroma.com/research/context-rot)) とセキュリティ研究 ([Simon Willison: lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)) を加えて、六つの「ない」に広げることを提案する。

| 原因 | 公式の四分類との対応 | 典型的な症状 | 効く手の種類 |
|---|---|---|---|
| ① 見えていない（情報不足） | 「リポジトリから読めない情報が足りない」 | 意図と違うものが出る、古い情報で答える、存在しない API を使う | 頼み方、CLAUDE.md、資料、検索 |
| ② 散らかっている（情報過多・失敗の残骸） | 四分類の外（context rot 研究と実践知） | 長い会話で前提を忘れる、堂々巡り、圧縮後に約束を忘れる | /clear、巻き戻し、handoff 文書、subagent、常駐物の削減 |
| ③ 確かめていない | 「検証手段がない」 | 完了の偽装、テストの改ざん、引用の誤り | テスト、/goal、Stop hook、独立レビュー、引用 |
| ④ 縛っていない | 「例外を許さないルールを prompt だけで」 | CLAUDE.md の無視、英語への回帰、文体の揺れ、破壊的な操作 | hooks、deny、sandbox、textlint |
| ⑤ 合っていない | 「既定値の手間とコスト」を広げたもの | すぐ上限に当たる、止まりすぎ・やりすぎ、遅い、面の選び違い | モデル・effort・面・プランの選択、/usage |
| ⑥ 境界がない | 四分類の外（セキュリティ研究） | 秘密の流出、悪意あるリポジトリや MCP、Web 上の指示に従う | 権限モード、sandbox、Rule of Two、データ設定 |

診断の入口ページでは、この六つを安く確かめられる順に問う。見せたか、片付けたか、確かめさせたか、縛ったか、合っているか、境界はあるか、の順である。安い順に並べる理由は二つある。前半の三つは次のプロンプトを書き直すだけで直ることが多く、後半ほど設定や構成の変更が要るからである。

公式の Best practices には「最初の1分を見て、ずれたら即 Esc。訂正が2回失敗したら /clear して書き直す」という助言がある ([Best practices](https://code.claude.com/docs/en/best-practices))。これは①と②の境界で使う判断である。逆引きの各行と各症状ページにこの原因タグを付ければ、読者は個別の対処を覚えなくても、次に何を疑えばよいかが分かるようになる。

### 背骨が分野構成・メタデータ・レベルに効く五つの経路

**一つ目は、分野を「活動」で切ることである。** 活動とは、頼む・文脈を整える（見せる）、確かめる、仕組みにする・守る（縛る）、任せて並べる（比例則）、払う（合っている）である。面に固有のものだけを、面別の分野（アプリ、Claude Code の操作、API）に置く。横断ページでは MkDocs Material の content tabs を使い、「アプリ / Claude Code / API」ごとの手段を並べる。たとえば「上限に早く当たる」も「事実を確かめる」も、三つの面で手段が違うが原理は同じである。

**二つ目は、メタデータに原理を持たせることである。** 全ページに `principle`（見せる・確かめる・縛る）と `prevents`（①〜⑥）を付ける。機能ページにはさらに四つの属性を持たせる。お願いか鍵かを表す `enforcement`、常駐か使うときだけかを表す `context_cost`、いつ読み込まれるかを表す `load_timing`、圧縮を生き延びるかを表す `survives_compaction` である。これらは公式の比較表の列と同じなので ([Extend Claude Code](https://code.claude.com/docs/en/features-overview))、「拡張機能の使い分け早見表」や各種の X vs Y 比較表を front matter から自動生成できる。手書きの表と本文の食い違いも防げる。

**三つ目は、レベルを「委任の段階」で定義することである。** 比例則に従い、上の段のページには対応する「確かめる」「縛る」のページを prerequisites として持たせる。たとえば /goal のページは「検証の階段」と「auto mode は何を止め、何を止めないか」を前提にする。こうすると、生成されるロードマップは「機能を覚える順」ではなく「任せる幅を広げる順」になる。

**四つ目は、基礎分野が「なぜ」を一手に引き受けることである。** 各ページの「なぜ」欄は基礎ページへのリンクで済ませる。原理は変わりにくいので確認の頻度を下げられる。仕様ページと分けておくと、鮮度管理の負担がはっきり軽くなる。

**五つ目は、古い助言を原理で解釈することである。** 古くなった助言の多くは、原理を満たすための回避策が正式な仕組みに置き換わったものである。`think hard` は effort に、IMPORTANT の多用は hooks に、`--dangerously-skip-permissions` の常用は auto mode と sandbox に、自作の Ralph ループは /goal に、`.claude/commands/` は skills に置き換わった。台帳に「どの原理の回避策だったか」を書いておけば、読者は次に何かが撤回されても自分で気づける。

ページの標準テンプレートは kyopro-atlas の「要点」を生かす。冒頭の要点は「何ができるか（概念ページでは何が分かるか）・いつ引くか・前提」の三行にする。本文はその後に、なぜ（原理へのリンク）、最小の使い方、Before/After、比較、よくある失敗と診断、古い助言との関係、関連、の順で続ける。ページの型は概念・機能・症状・比較・レシピ・台帳の六つに分け、front matter は共通にすることを推奨する。

## 3. 20分野・300ページ候補は活動で切り、面はタブで表す

20分野のページ候補は合計300で、優先度の内訳は必須151、推奨110、任意39である。面（アプリ・Claude Code・API）ごとに章を分けると、「上限に当たる」「事実を確かめる」のように三つの面に共通する話が三か所に散らばる。そこで分野は活動（頼む・整える・確かめる・縛る・任せる・払う）で切り、面に固有の操作だけを面別の分野（06・07・13）に置く。

### レベル・優先度・根拠の凡例

レベルは「機能の難しさ」や「使い始めてからの期間」ではなく、委任の段階で定義することを提案する。既存のコミュニティガイドでは、レベルを利用期間（初日 / 1〜4週 / 1か月以上）で決めたり ([Ultimate Guide](https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/693d97d284ea342c8c8fb13894df0cee26d3a3d3/guide/learning-path/README.md))、機能のモジュールごとに5段階を付けたりしている ([claude-howto](https://cdn.jsdelivr.net/gh/luongnv89/claude-howto@main/README.md))。しかし本教材の読者は「多用しているが使いこなせていない」層である。必要なのは「次にどこまで任せられるか」を示す軸のほうだ。

| Lv | 名前 | この段階の読者 | 上がる条件（ロードマップの節目） |
|---|---|---|---|
| L1 | 使う | 対話で頼み、返答を読んで使う | 期待外れの原因を「見えていない／散らかっている」と言い分けられる |
| L2 | 整える | 頼み方・資料・会話の長さを整え、結果を確かめて直す | 完了の条件と確かめ方を、依頼に含めて渡せる |
| L3 | 任せる | 計画させてから任せ、長い作業を途中で舵取りする | 二回同じ注意をしたら、仕組みに移すと判断できる |
| L4 | 仕組みにする | CLAUDE.md、skills、hooks、permissions、MCP、plugins で常設化し、共有する | 無人で動かす前の5つの問いに答えられる |
| L5 | 回す | 並列・無人・定期・プログラムから動かす | ― |

読者層を考えると、L1 のページは少なく短くてよく、厚くすべきは L2〜L4 である。基礎（なぜ）のページには、そのページが初めて必要になる段階を level として付ける。優先度は三段階とする。「必須」は初版で書き、逆引きの受け皿になるページ、「推奨」は初版か次の版で書くページ、「任意」は需要や成熟度を見て書くページである。根拠欄の記号は、公D が公式ドキュメント・Help Center、公B が公式ブログ・engineering・研究、CL が CHANGELOG・リリースノート、英が英語圏の実践者、日が日本語圏の実践者、研が第三者の研究・セキュリティ報告、教が既存の教材・書籍、新が既存教材では手薄な独自整理を表す。

### 分野00 入口と地図（7ページ）

kyopro-atlas と同じく、索引・地図・ロードマップの大半は front matter から自動生成する。手書きするのは「使い方」と「背骨」と「診断の入口」だけでよい。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| この辞典の引き方 | L1 | 必須 | 要点欄・レベル・逆引き・確認日の読み方。公式ドキュメントとの役割分担 | 新 |
| 三つの原理（見せる・確かめる・縛る） | L1 | 必須 | 背骨。比例則。各原理を、アプリ・Claude Code・API それぞれの手段で示す | 公D・公B |
| 六つの失敗原因と診断の手順 | L1 | 必須 | ①〜⑥を安く確かめられる順に問う。症状ページへの振り分け | 公D・研 |
| 全体地図：Claude の面と層 | L1 | 必須 | アプリ（Cowork と統合済み）／Claude Code／API・SDK／周辺製品。モデル層と拡張層 | 公D |
| ロードマップ（委任の段階別） | L1 | 必須 | 自動生成。L1→L5 の節目と、各段の必読ページ | 新 |
| 逆引き辞典（症状・やりたいこと） | L1 | 必須 | 自動生成。signs から作る | 新 |
| 用語索引と旧名の対応 | L1 | 必須 | 自動生成。aliases から作る（routines→scheduled tasks など） | CL |

### 分野01 基礎：なぜそうなるか（19ページ）

この分野は変わりにくい部分を受け持つので、他の分野の「なぜ」欄がここへリンクする。Anthropic の context engineering 論は、コンテキストを「逓減する有限の資源」と位置づけている ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents))。ハルシネーションの説明には二つの研究を併用する。統計的に生じる理由を示した論文 ([Why Language Models Hallucinate](https://arxiv.org/html/2509.04664v1)) と、Claude の内部で「知っているつもり」の回路が誤って働くことを示した研究 ([Tracing thoughts](https://www.anthropic.com/research/tracing-thoughts-language-model)) である。どちらも比喩を付けて説明できる。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| トークンとは（日本語の場合） | L1 | 必須 | 語のかけら。日本語は英語より多めになる（倍率は tokenizer 次第）。Opus 4.7 以降で約30%増 | 公D・研 |
| コンテキストウィンドウと注意の予算 | L1 | 必須 | 広い机と、よく読めることは別。1M でも劣化する | 公B・研 |
| 毎ターン全履歴を読み直す | L1 | 必須 | 長い会話が重くなる理由。cache が効く理由 | 公D |
| context rot と紛らわしい情報 | L2 | 必須 | Chroma の18モデル実験。失敗した試行が紛らわしい情報として残る | 研 |
| 中ほどの情報は使われにくい（lost in the middle） | L2 | 推奨 | U字型の性能。ただし条件によって変わる | 研 |
| ハルシネーションはなぜ起きるか | L1 | 必須 | 白紙より山を張る受験生。知っているつもりの回路 | 研・公B |
| 知識カットオフと「今」を知らない問題 | L1 | 必須 | 現行モデルの信頼できる知識は2026年6月まで。日付と検索を渡す | 公D |
| 同じ質問でも答えが変わる（非決定性） | L2 | 必須 | 一回の結果で判断しない。ばらつきを不確かさの合図と見る | 公B・研 |
| 推論（thinking）と effort の仕組み | L2 | 必須 | adaptive thinking。表示されるのは要約。thinking も出力として課金される | 公D |
| 表示された推論は内部の計算と一致しない | L2 | 推奨 | 計算したと書くが痕跡がない。後付けの理屈 | 公B |
| エージェントループと tool use | L2 | 必須 | 読む→行動→確かめる。「確かめる」が欠けると、見た目で止まる | 公D・公B |
| system prompt・user message・CLAUDE.md の位置 | L3 | 必須 | CLAUDE.md は user message として届く。強制力はない | 公D |
| prompt caching（先頭が変わらないことの価値） | L3 | 推奨 | tools→system→messages の積み木。effort やモデルを替えると cache が切れる | 公D |
| compaction（要約圧縮）で何が残り、何が消えるか | L3 | 必須 | 議事録だけ残して録音を消す。CLAUDE.md は再注入される | 公D・公B |
| subagent は別室の部下 | L3 | 必須 | 文脈の隔離。賢くはならない。給料（トークン）はかかる | 公D |
| お願いと鍵（決定論的か、非決定論的か） | L2 | 必須 | 背骨の「縛る」の理論面。公式の5行表 | 公D |
| データと命令を区別できない（prompt injection の原理） | L2 | 必須 | バグではなく性質。完全な防御はない | 研・公D |
| 迎合（sycophancy） | L2 | 推奨 | RLHF に由来する性質。独立したレビュアーが効く | 公B |
| 採点器を騙す（reward hacking） | L3 | 推奨 | テストの改ざんの背景。改ざんできない検証が必要な理由 | 公B |

### 分野02 製品の地図と面の選び方（11ページ）

2026年9月16日以降、アプリは Chat と Cowork が一つの会話にまとまった。軽い質問から多段の作業まで、Claude がツールを選んで進める ([統合の記事](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude))。そのため「どのアプリを使うか」より、「どこで実行され、何に触れられるか」で選ぶ説明のほうが長持ちする。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| アプリ・Claude Code・API の選び方 | L1 | 必須 | 比較表。誰が手を動かすか、何に触れるか、どこで動くか | 公D・日 |
| 統合された Claude（チャットとタスク） | L1 | 必須 | 2026-09 の統合。Tasks。クラウドで動くかローカルで動くか | 公D |
| 実行場所の違い（クラウド／自分の PC／リモート操作） | L2 | 必須 | ローカルのファイルやブラウザ操作には Desktop が必要。クラウドのセッションは user 設定を読まない | 公D |
| Claude Code の面（ターミナル・IDE・Desktop・Web・モバイル） | L2 | 推奨 | 同じエージェントループ。面ごとの差 | 公D |
| Claude Code と Cowork の使い分け | L2 | 推奨 | 繰り返す作業になったら Code へ、という実践知 | 日 |
| Claude in Chrome とブラウザ操作 | L2 | 推奨 | 有料プラン、Chrome のみ。機微な作業には非推奨 | 公D |
| Office アドイン と Google Workspace | L2 | 任意 | 開いているファイルにだけ作用する。編集モード | 公D |
| Computer use（画面操作） | L3 | 任意 | 最後の手段。サンドボックスはない。アプリごとに許可する | 公D |
| Claude Design・Science・Duet・Tag | L2 | 任意 | 周辺製品の要点。research preview なので変わりやすい | 公D |
| Agent SDK と Managed Agents の位置づけ | L4 | 推奨 | Claude Code をライブラリとして使う SDK と、Anthropic がホストする Managed Agents | 公D |
| 面ごとにできないこと一覧 | L2 | 推奨 | Incognito では作れない、モバイルでは artifact が使えない、など | 公D |

### 分野03 モデル・effort・思考（13ページ）

公式の推奨は「迷ったら Opus 5.5 から始め、モデルを替える前に effort を調整する」で、Opus 5.5 で足りなければ Fable 5.1 に上げる ([Models overview](https://platform.claude.com/docs/en/about-claude/models/overview))。Fable の扱いはプランで大きく違う。Pro では最初から usage credits で使う。Max と premium seat では、週上限の50%までがプランに含まれる ([Claude Fable models on your plan](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan))。モデルを選ぶページでは、必ずプランとの関係を添える。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 現行モデルの一覧と位置づけ | L1 | 必須 | Fable・Opus・Sonnet・Haiku。共通仕様。確認日を明記 | 公D |
| モデルの選び方（三段階） | L1 | 必須 | 既定のまま → effort を上げる → Fable。プランとの関係 | 公D |
| effort の段階と使い分け | L2 | 必須 | low〜max。トークン予算ではなく振る舞いの合図。Claude Code では /effort | 公D |
| 「考えて」と書くことの現在（ultrathink） | L2 | 必須 | think hard は認識されない。ultrathink は1ターンだけ深く考えさせる | 公D・CL |
| Fable と Mythos | L2 | 推奨 | 同じモデルで、安全装置の強さが違う。透かしが入る。提供範囲 | 公D |
| 計画は Opus、実装は Sonnet（opusplan など） | L3 | 推奨 | 分業の是非。2026年に価格が変わった | 英・公D |
| fast mode と advisor | L3 | 任意 | 速度とコスト。重要な局面だけ別モデルに助言させる | 公D |
| モデル別の癖と、プロンプトの合わせ方 | L3 | 推奨 | Opus 5 は冗長、Sonnet 5.5 は止まりすぎるかやりすぎる、Fable は報告が少ない | 公D |
| 新しいモデルに替えたら見直すこと | L3 | 必須 | effort を持ち越さない。旧来の強調・検証指示を外す。/doctor prompt-audit | 公D |
| 1M コンテキストとの付き合い方 | L2 | 推奨 | 容量はあるが劣化する。自動圧縮の窓 | 公D・日 |
| 「劣化した」と感じたら（版と effort を確認する） | L2 | 必須 | 2026年3〜4月のポストモーテムを実例に | 公B・日 |
| 旧モデルの退役と既定モデルの変化 | L2 | 任意 | 退役の日付。既定が変わったときの気づき方 | 公D |
| Haiku を使いどころで使う | L3 | 任意 | 大量処理、subagent、分類 | 公D |

### 分野04 頼み方（プロンプト）（22ページ）

公式の基本原則（文脈のない新人として扱う、理由を添える、例を示す、XML で区切る、長い資料は先頭に置く）は、アプリにも Claude Code にもそのまま使える ([Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices))。Claude Code の Best practices には「Instead of / Try」の対比表がある。たとえば "fix the login bug" を「セッションのタイムアウト後にログインが失敗する、src/auth/ のトークン更新を見て、再現する失敗テストを書いてから直せ」に書き換える例である ([Best practices](https://code.claude.com/docs/en/best-practices))。この分野は全ページを Before/After で書く。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 新人の同僚に頼むつもりで | L1 | 必須 | 文脈のない同僚が混乱するなら、Claude も混乱する | 公D |
| 具体性の4点（対象・状況・完了・手本） | L2 | 必須 | 熟練者との差は長さではなく具体性 | 公D・英 |
| 理由を添える | L1 | 必須 | 読み上げエンジンの例。理由があると応用が利く | 公D |
| 例を見せる（3〜5個） | L2 | 必須 | 多様で典型的な例。自分の文章を見本にする | 公D・日 |
| XML タグで区切る | L2 | 推奨 | instructions、context、input。文書の入れ子 | 公D |
| 長い資料は先、質問は最後 | L2 | 必須 | 公式のテストで最大30%向上。先に引用させる | 公D |
| 否定形ではなく、望む形で書く | L2 | 必須 | 「markdown を使うな」より「段落で書け」。正の例を示す | 公D |
| 提案してほしいのか、実行してほしいのか | L2 | 必須 | 「suggest」と頼むと提案だけで終わる。動詞をはっきりさせる | 公D |
| 範囲を伝える（やらないこと） | L2 | 必須 | anti-goals。頼んだ範囲で。追加の機能を足させない | 公D・英 |
| 細かく指図せず、成果で頼む | L3 | 推奨 | Delegate, don't dictate。文脈は渡す | 公D・英 |
| 質問させる・インタビューさせる | L2 | 必須 | AskUserQuestion。spec を作らせてから新しいセッションへ | 公D・英・日 |
| 選択肢と推奨案を出させる | L2 | 推奨 | 不確かなときの定番 | 英 |
| 画像・スクリーンショット・音声で渡す | L2 | 必須 | 9割に画像を添える人もいる。音声入力（Aqua Voice など） | 英・日 |
| 強調語（IMPORTANT・必ず）の現在 | L2 | 必須 | 強調を重ねると過剰に適用される。1行だけにする。守られないなら仕組みへ | 公D |
| 出力の形と分量を指定する | L2 | 推奨 | 書式、冗長さ、要約の有無。プロンプト自体の書き方が出力に映る | 公D |
| 「分からない」と言ってよいと伝える | L1 | 必須 | ハルシネーション対策の第一手 | 公D |
| 頼み方は一回で決めない（会話で詰める） | L1 | 推奨 | 完璧なプロンプトは要らない。違うと返すより、元の依頼を編集する | 公D・英 |
| 「念のため確認して」は効くか | L3 | 推奨 | 検証の「手段」を渡すのは今も有効。言葉で検証を命じるのは、5世代では過剰になる | 公D |
| 文章を頼むとき（AI 臭さを避ける） | L2 | 推奨 | 具体例で嫌な点を伝える。過剰な装飾を外す | 英・日 |
| 推論を見せてほしいとき | L3 | 任意 | 推論を全文書かせる指示は拒否されうる。要約や短い根拠を頼む | 公D |
| Before/After プロンプト集 | L2 | 必須 | 30例程度。面別のタブで示す | 公D・新 |
| 用途別プロンプトの型 | L2 | 推奨 | 調査・要約・レビュー・計画・バグ報告などの雛形 | 教・新 |

### 分野05 文脈を整える（コンテキスト管理）（18ページ）

英語圏では「コンテキストは牛乳のように新鮮なうちに」という言い方が象徴的である ([ykdojo](https://awesomeclaude.ai/claude-code-tips))。公式には「訂正が2回失敗したら /clear」という具体的な線引きがある ([Best practices](https://code.claude.com/docs/en/best-practices))。ただしコンテキストの意味は変わった。かつては「溢れさせないための節約」だったが、今は「質とコストのための整頓」として教えるべきである。この分野のページは、アプリ（新しいチャット、プロンプトの編集、Projects）と Claude Code（/clear、/rewind、handoff）を同じ原理の下に並べる。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 机を整える：新鮮さ・巻き戻し・書き出し・委任 | L2 | 必須 | 四つの動作の総論 | 英・公D |
| 新しい会話を始めるタイミング | L1 | 必須 | 話題が変わったとき。訂正を2回しても直らないとき。チャットなら30〜50ターンが目安という声も | 公D・英 |
| 違うと返すより、巻き戻す・編集する | L2 | 必須 | /rewind、Esc Esc、アプリでの編集。失敗の残骸を残さない | 英・公D |
| /compact と自動圧縮 | L3 | 必須 | 焦点を指示する。Compact instructions。要約が失うもの | 公D |
| handoff 文書と document-and-clear | L3 | 必須 | 書き出してから /clear。/compact との使い分け | 英・日 |
| 進捗ファイル（PLAN・TODO・KNOWLEDGE） | L3 | 推奨 | みのるんの4ファイル。途中から再開できる | 日 |
| 失敗の教訓は捨てずに書き残す | L3 | 推奨 | 巻き戻すと教訓も消える問題（Armin の指摘）への補い | 英 |
| @参照と、何を読ませるかの絞り込み | L2 | 必須 | 直接読ませる。長いコマンド出力を絞る | 公D・英 |
| /context で中身を見る | L3 | 必須 | 何が場所を取っているか。起動直後の基準値 | 公D |
| 本筋を汚さずに聞く（/btw） | L3 | 推奨 | 履歴に残らない横道の質問 | 公D |
| 調査は subagent に任せて要約だけ受け取る | L3 | 必須 | 冗長な出力の隔離。渡し方 | 公D |
| 常駐するもののコスト（CLAUDE.md・MCP・skills） | L3 | 必須 | listing tax。使わないものを切る | 公D・英 |
| 長い資料を渡すとき | L2 | 必須 | 引用を先に抜かせる。分割する。Markdown にしてから渡す | 公D・英 |
| セッションに名前を付けて再開・分岐する | L3 | 推奨 | /rename、/resume、/branch。ブランチのように扱う | 公D |
| 休憩と cache 切れ | L3 | 任意 | 長い離席の後は全体を読み直す。離席前に畳む | 公D・日 |
| 圧縮のあとに残る約束、消える約束 | L3 | 必須 | 会話で伝えた制約は消えうる。deny に書く | 公D |
| アプリでの文脈管理（Projects・Memory・新しいチャット） | L2 | 必須 | アプリ版の整頓。自動の context 管理 | 公D |
| 1M 時代の圧縮設定 | L4 | 任意 | `CLAUDE_CODE_AUTO_COMPACT_WINDOW` など。実践者の値には幅がある | 日 |

### 分野06 アプリを使いこなす（claude.ai・Desktop・Mobile）（22ページ）

アプリの指示の置き場所について、公式の区分は明快である。全体に効かせるなら Instructions、案件ごとなら project instructions、形式や手順なら skills を使う ([personalization](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features))。それでも誤解が多い仕様がある。たとえば、会話を消してもその会話から作られた memory は残る ([memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context))。PDF は100ページまでなら図も読むが、101ページ以降は文字しか読まない ([Upload files](https://support.claude.com/en/articles/8241126-upload-files-to-claude))。Research と Artifacts を深く使う日本語の実践記事はほぼない。ここは差別化できる余地が大きい。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 指示の置き場所（Instructions・Project・Memory・Skills・Styles） | L2 | 必須 | 使い分けの表。効く範囲と、いつ読まれるか | 公D |
| Projects の使いどころ | L2 | 必須 | 資料を固定した繰り返し作業。1プロジェクト1目的。cache が効く | 公D・英・日 |
| Project の knowledge が多すぎるとき | L2 | 推奨 | 上限に近づくと RAG モードに切り替わる。少数精鋭で | 公D |
| Memory の仕組みと範囲 | L2 | 必須 | トピック単位。プロジェクトで分かれる。機微な話題 | 公D |
| Memory の困りごと FAQ | L2 | 必須 | 会話を消しても残る。Pause と Reset の違い。会話ごとにオフにする | 公D |
| 過去チャットの検索 | L2 | 推奨 | memory とは別の機能。オフにできる | 公D |
| Incognito（記録しない会話） | L2 | 推奨 | 30日は保持される。組織では見える。作れないものがある | 公D |
| web search・Research・thinking の使い分け | L2 | 必須 | 呼び出し回数と時間の目安 | 公D |
| Research を使いこなす | L2 | 推奨 | 起動しないときの頼み方。出典の確かめ方。connectors との併用 | 公D・新 |
| Artifacts（Docs・Slides・Design・Dashboards） | L2 | 必須 | テンプレート型。中から Claude を呼べる。共有したときの扱い | 公D |
| Artifacts を小さなアプリにする | L3 | 推奨 | データ保存、connectors、閲覧者の上限で動く | 公D |
| ファイル作成とコード実行 | L2 | 必須 | xlsx、pptx、docx、PDF。サンドボックス。ネットワークの設定 | 公D |
| 添付ファイルはどこまで読まれるか | L1 | 必須 | PDF は100ページまで図も読む。それ以外の文書は画像を読まない | 公D |
| Connectors（MCP）をアプリで使う | L2 | 必須 | ディレクトリ型とカスタム型。オンデマンド。信頼の判断 | 公D |
| アプリの Skills | L3 | 推奨 | ZIP でアップロード。description の書き方。組織での共有 | 公D |
| アプリの Plugins | L3 | 任意 | 役割ごとの束。marketplace。Claude Code と同期する | 公D |
| タスクと定期実行（旧 Cowork） | L3 | 必須 | 結果で頼む。クラウドで動く。取り消しにくい操作は定期にしない | 公D |
| 権限モード（Auto と Manual）と安全 | L3 | 必須 | 二条件モデル。専用フォルダ。低リスクから始める | 公D |
| 長い会話の自動 context 管理と長さの上限 | L2 | 推奨 | 要約されても履歴は残る。上限に当たったときの対処 | 公D |
| 音声・Quick entry・モバイル | L1 | 任意 | 音声モード、Option を2回、モバイルでのタスク監視 | 公D |
| チームで使う（共有 Project・組織の skills） | L3 | 任意 | 閲覧と編集の権限。配布 | 公D |
| アプリでの調べもの・文章作成のレシピ | L2 | 推奨 | 分野12への入口 | 新 |

### 分野07 Claude Code の基本操作（18ページ）

インストールや設定の基本は、読者層に合わせて薄くする。公式ドキュメントと日本語のチートシートへリンクし ([チートシート](https://support.claude.com/ja/articles/14553413-claude-code-チートシート))、本文は「知らないと損をする操作」と「判断」に絞る。既定の権限モードが auto に変わったので、権限の説明は版によって変わることを必ず書いておく ([Permission modes](https://code.claude.com/docs/en/permission-modes))。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 入力の4記号（/ ! @ と Esc） | L1 | 必須 | コマンド、シェル、参照、中断と割り込み。# メモリは削除された | 公D・CL |
| 知らないと損をする操作20 | L2 | 必須 | Esc Esc、Shift+Tab、Ctrl+G、Ctrl+B、Ctrl+O、画像の貼り付けなど | 公D・日 |
| 権限モードの全体像 | L2 | 必須 | manual・acceptEdits・plan・auto・dontAsk・bypass。既定は auto | 公D |
| plan mode の使いどころ | L2 | 必須 | 方針が不確か、複数ファイル、不慣れなとき。1文で説明できる差分なら飛ばしてよい | 公D・英 |
| checkpoint と rewind（git との違い） | L2 | 必須 | Bash での変更は戻らない。リスクのある試行に使う | 公D |
| セッションの再開・分岐・命名 | L2 | 推奨 | --continue、/resume、/branch、--from-pr | 公D |
| /usage・/context・status line | L2 | 必須 | 使用量と占有量を常に見えるようにする | 公D |
| 設定ファイルの階層（最小限） | L3 | 推奨 | user・project・local・managed。配列はマージされる。/status で確認 | 公D |
| /init と最初の CLAUDE.md | L2 | 推奨 | 叩き台をどう扱うか（分野08へ） | 公D・英 |
| git との付き合い方 | L2 | 必須 | 小さくコミットする。人が握るか任せるか。draft PR | 英・日 |
| IDE（VS Code・JetBrains）で使う | L2 | 任意 | 差分表示、選択範囲の共有（詳細は未調査） | 公D |
| クラウドセッションと teleport | L3 | 推奨 | 手元を閉じても続く。計画を push してから --cloud | 公D・日 |
| スマホから操作する（Remote Control） | L3 | 任意 | 実行もファイルも手元に残る | 公D |
| Claude Code 自身に聞く | L1 | 推奨 | 使い方を聞けば最新のドキュメントを調べる。/powerup、/insights | 公D |
| output style（説明多め・簡潔・学習用） | L3 | 推奨 | Explanatory と Learning。CLAUDE.md との違い | 公D |
| Claude Code を非エンジニアが使う | L2 | 推奨 | Desktop の Code タブ。作業用フォルダ。手動モード | 日 |
| 終わったら知らせてもらう | L3 | 任意 | Notification hook。通知が要るかどうかは好みが分かれる | 英・日 |
| 主要コマンド早見表 | L2 | 推奨 | 自動生成。旧名との対応も載せる | 公D・CL |

### 分野08 文脈と指示を仕組みにする（Claude Code の拡張）（26ページ）

この分野は、日本語でも英語でも「使い分けが分からない」という記事が最も乱立している領域である ([fujisho1216](https://qiita.com/fujisho1216/items/90b34ef9abd910deb6ac); [rcanand](https://rcanand.bearblog.dev/claude-code-just-got-confusing-plan-mode-vs-superpowers-vs-agent-teams-a-practical-guide/))。公式の「Build your setup over time」には、拡張を足すきっかけが回数付きで並んでいる。「同じ規約を2回間違えた → CLAUDE.md」「同じ手順書を3回貼った → skill」「副作業の出力が会話を埋める → subagent」「毎回必ず起きてほしい → hook」「2つ目のリポジトリにも同じ設定 → plugin」である ([Extend Claude Code](https://code.claude.com/docs/en/features-overview))。この表を、逆引きと各ページの signs の骨格にする。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 拡張機能の全体図と使い分け早見表 | L3 | 必須 | front matter から自動生成する比較表（強制力・コスト・読み込み時期・圧縮後に残るか） | 公D・公B |
| 足すタイミング表（トリガー → 機能） | L3 | 必須 | 回数で判断する。少ない状態から始める | 公D |
| CLAUDE.md に書くこと | L3 | 必須 | 推測できないコマンド、理由、落とし穴（地雷リスト）、検証手順 | 公D・英・日 |
| CLAUDE.md に書かないこと | L3 | 必須 | 構成の説明、lint で検査できる規約、コード片、たまにしか使わない手順 | 公D・英 |
| CLAUDE.md の長さと剪定 | L3 | 必須 | 200行未満。各行の削除テスト。/doctor prompt-audit | 公D・日 |
| CLAUDE.md の階層と読み込み順 | L3 | 推奨 | 連結される。遅延ロード。@import でコンテキストは減らない | 公D・日 |
| .claude/rules と paths で必要なときだけ読ませる | L3 | 必須 | ディレクトリ別の規約。条件付きの読み込み | 公D・日 |
| auto memory | L3 | 推奨 | MEMORY.md の先頭だけが読まれる。/memory で確認 | 公D |
| AGENTS.md と他ツールとの共有 | L3 | 推奨 | v2.1.277 から。@AGENTS.md で取り込む。/import | 公D・CL |
| Skills の考え方（手順を必要なときだけ読む） | L3 | 必須 | progressive disclosure。オープン標準 | 公D・英 |
| Skill の作り方 | L4 | 必須 | SKILL.md、frontmatter、500行未満、scripts、skill-creator | 公D・教 |
| Skill の description の書き方 | L4 | 必須 | 成否の9割を決める。いつ使うかを先頭に | 公D・日 |
| 副作用のある skill を勝手に動かさない | L4 | 推奨 | disable-model-invocation。直接起動 | 公D |
| カスタムコマンドは skills へ | L3 | 必須 | 統合された。旧記法 /project:name | 公D・日 |
| Subagent の作り方と使いどころ | L4 | 必須 | 工程ではなく文脈の独立性で分ける。tools を絞る。model: haiku | 公D・日 |
| Subagent に引き継がれないもの | L4 | 推奨 | 会話の履歴、skills、output style。委任のプロンプトに書き直す | 公D |
| MCP をつなぐ | L3 | 必須 | HTTP 推奨。スコープ。/mcp。読み取り専用の資格情報 | 公D |
| MCP か CLI か | L3 | 必須 | CLI のほうがコンテキストの効率がよい。MCP と skill の組み合わせ | 公D・英 |
| よく使われる MCP と選び方 | L3 | 推奨 | ブラウザ検証、Context7 など。入れすぎない | 英・日 |
| code intelligence plugin（LSP） | L4 | 推奨 | 型のある言語では入れるよう推奨されている | 公D |
| Plugins と marketplace | L4 | 推奨 | 配布の単位。常駐するコスト。導入前の確認 | 公D |
| Mods（深い挙動の変更） | L5 | 任意 | 2026-10 に追加。成熟していない | CL |
| 拡張の棚卸しと剪定 | L4 | 必須 | /skill-doctor、/usage、使っていないものを切る。40個を超えたら見直す | 公D・英 |
| Skill と Subagent の違い | L3 | 必須 | 比較ページ | 公D |
| Hook と Skill の違い | L3 | 必須 | 比較ページ（決定論か非決定論か） | 公D |
| CLAUDE.md・rules・skills・output style の違い | L3 | 必須 | 比較ページ（常駐と条件付き、知識と応答形式） | 公D・公B |

### 分野09 確かめる（検証と評価）（16ページ）

公式は検証の強さを段階で上げることを勧めている。依頼の中で頼む、/goal の条件にする、Stop hook で止める、別のエージェントに反証させる、の順である ([Best practices](https://code.claude.com/docs/en/best-practices))。この「検証の階段」を分野の中心に置く。Opus 5 のガイドは、言葉で「double-check して」と書くことを過剰検証として外すよう勧めている ([Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5))。そのため、「手段を渡す」ことと「言葉で命じる」ことを区別して書く必要がある。体感が当てにならないことの根拠として、METR の研究を使える。経験のある開発者が「20%速くなった」と感じていたのに、実測では19%遅くなっていた ([The Decoder](https://the-decoder.com/ai-coding-can-make-developers-slower-even-if-they-feel-faster/))。ただしこれは旧世代のツールでの結果であり、「AI は遅い」という結論には使わない。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 検証の階段 | L3 | 必須 | 依頼 → /goal → Stop hook → 独立したエージェント | 公D |
| 「完了」を定義して渡す | L2 | 必須 | 測れる終了状態。チェックリスト | 公D・英 |
| 報告ではなく証拠を求める | L2 | 必須 | 実行したコマンドと出力。テキストだけの完了報告は証明にならない | 公D |
| テストを先に書かせる | L3 | 推奨 | TDD。テストの変更は特に注意してレビューする | 英・日 |
| 画面で確かめる（ブラウザ・スクリーンショット・/verify） | L3 | 推奨 | Chrome、Playwright、アプリを起動して確認する | 公D・英 |
| 書いた本人ではない者にレビューさせる | L3 | 必須 | Writer/Reviewer。/code-review。新しいセッション | 公D・英・日 |
| レビュアーへの指示の書き方 | L4 | 推奨 | 正しさに関わる指摘だけ出させるか、全部出させて絞るか。モデルの世代で変わる | 公D |
| テストを守る（改ざんを防ぐ） | L4 | 推奨 | 保護 hook。一般解を求める | 公D・英 |
| 事実を確かめる（引用・照合・best-of-N） | L1 | 必須 | 主張ごとの引用。提供した資料の範囲で答えさせる | 公D |
| 引用や出典の確かめ方 | L2 | 必須 | タイトルや著者だけが微妙に違う誤り（Anthropic の訴訟の事例） | 研・公D |
| 人間が読むべき差分の箇所 | L3 | 推奨 | 要となる処理は厳しく、周辺は緩く。テストと設定の変更 | 英 |
| 変更が効いたかを測る（小さな eval） | L4 | 推奨 | 失敗したタスクを5〜20個選び、前後で3回ずつ走らせる。pass^k | 公B・新 |
| 体感と実測 | L3 | 推奨 | METR の研究。測る習慣 | 研 |
| /insights と /usage で振り返る | L3 | 推奨 | 摩擦の起きた点と内訳 | 公D |
| 生成コードを自分のものにする | L3 | 推奨 | 説明できないコードを出荷しない | 英・教 |
| 無人実行の結果を確かめる | L5 | 推奨 | 監督の少なさに比例して確かめる。最終決定は人とブランチ保護に | 公D・教 |

### 分野10 仕組みで縛る（hooks・権限・sandbox）（13ページ）

公式は「`.env` を編集しない」を CLAUDE.md や skill に書くことを「依頼であって保証ではない」と言い切り、PreToolUse hook でブロックすることを強制の手段として示している ([Extend Claude Code](https://code.claude.com/docs/en/features-overview))。hooks は既定で fail-open になっている。ポリシーに使う場合は `onFailure: "block"` を指定する必要がある ([Hooks](https://code.claude.com/docs/en/hooks))。sandbox は既定のままだと `~/.ssh` や `~/.aws/credentials` を読めてしまうので、`denyRead` を明示する ([Sandboxing](https://code.claude.com/docs/en/sandboxing))。この分野では、直感に反するこうした既定値を必ず書く。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| お願いを鍵に移す判断 | L3 | 必須 | 強調しても守られない行は hook にする合図。二回同じ注意をしたら仕組みにする | 公D・日 |
| Hooks の考え方とイベント | L4 | 必須 | ライフサイクルで必ず実行される。代表的なイベントだけを挙げる | 公D |
| exit 2 でブロックし、理由を返す | L4 | 必須 | stderr が Claude に渡る。JSON での判定 | 公D |
| 代表的な hook のレシピ | L4 | 必須 | フォーマッタ、危険操作の遮断、テスト出力の絞り込み、通知 | 公D・英・日 |
| Stop hook で「終わらせない」 | L4 | 推奨 | 検証が通るまでターンを終えさせない。連続ブロックには上限がある | 公D・英 |
| hook を安全に書く | L4 | 推奨 | fail-open。`onFailure`。`args`（exec 形式）。他人の hook はコードとして確認する | 公D |
| 権限ルール（allow・ask・deny） | L3 | 必須 | 評価は deny から。前方一致の落とし穴。/permissions | 公D |
| auto mode は何を止め、何を止めないか | L3 | 必須 | 分類器の既定ルール。見逃しはある。広すぎる allow は無効になる | 公D・公B |
| sandbox で封じ込める | L4 | 必須 | ファイルシステムとネットワークの境界。denyRead。Windows は WSL2 で | 公D |
| 消せない場所・触れない場所（protected paths） | L3 | 推奨 | `.git`、`.claude` など。どのモードでもブロックされる rm | 公D |
| managed settings と組織の強制 | L4 | 任意 | 優先順位の最上位。配布の手段 | 公D・日 |
| 会話で言った禁止事項は圧縮で消える | L3 | 推奨 | 「push しないで」を deny に書く理由 | 公D |
| お願いと鍵の対応表 | L3 | 必須 | 完了の判定、禁止、形式、文体など。用途ごとに二列で並べる | 公D・新 |

### 分野11 安全とデータ（14ページ）

prompt injection は「バグ」ではなく、LLM がデータと命令を区別できないという性質として教える。OpenAI・Anthropic・Google DeepMind の研究者を含む論文は、公開済みの12の防御に適応型の攻撃を行い、多くで成功率が90%を超えたと報告した ([Simon Willison newsletter](https://simonw.substack.com/p/new-prompt-injection-papers-agents))。だから対策は構成の側に置く。Meta の Agents Rule of Two は「信頼できない入力」「機微なデータ」「状態の変更・外部との通信」のうち、1セッションで満たしてよいのは二つまでとする ([Meta](https://ai.meta.com/blog/practical-ai-agent-security/))。Check Point は、clone したリポジトリの `.claude/settings.json` や `.mcp.json` だけで RCE や API キーの窃取が成立した脆弱性を公表した（修正済み） ([Check Point Research](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/))。この事例は「設定ファイルもコードとして扱う」ことの実例になる。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| prompt injection の実際 | L2 | 必須 | ファイル、Web、issue、tool の説明文に指示が仕込まれる。GitHub MCP の事例 | 研・公D |
| 三つを同時に持たせない（lethal trifecta と Rule of Two） | L3 | 必須 | 設計の原則。アプリの二条件モデルとの対応 | 研・公D |
| 知らないリポジトリを開く前に | L3 | 必須 | `.claude/`、`.mcp.json`、`.vscode/` を確認する。`-p` では trust の確認が出ない | 研・公D |
| MCP・plugins・skills を入れる前の確認 | L3 | 必須 | tool poisoning、rug pull。出所。ユーザー権限でコードが動く | 研・公D |
| 秘密情報（.env・API キー）を守る | L3 | 必須 | Read の deny、sandbox の denyRead。会話の記録は平文で残る | 公D |
| 消されたくないもの（破壊的コマンド） | L3 | 必須 | 実例（ホームの削除）。checkpoint の限界。確認の求め方 | 研・公D |
| bypassPermissions はどこで使ってよいか | L4 | 推奨 | 隔離したコンテナか VM のみ。root では起動しない | 公D |
| 承認疲れ | L2 | 推奨 | 93% が承認されている。読まずに押すようになる。auto mode と sandbox で減らす | 公B |
| 送ったデータの行方（学習・保持期間） | L1 | 必須 | 2025-08 の規約改定。オプトアウト。30日と5年。商用は対象外 | 公B・公D |
| /feedback・transcript 共有で送られるもの | L2 | 推奨 | 会話とコードが送られる。保持期間 | 公D |
| Chrome・computer use・ブラウザでの注意 | L2 | 推奨 | 機微な作業は非推奨。サンドボックスはない | 公D |
| 公開された artifact とファイルの扱い | L2 | 任意 | 知らない送り主からのファイルとして扱う | 公D |
| 学校・組織・コンテストの規則 | L1 | 推奨 | 規則は変わるので、最新の公式ページを確認する。条文は転載しない | 研・新 |
| 安全の早見表（面ごとの既定値） | L2 | 必須 | 権限、ネットワーク、データ、記録の既定値。確認日付き | 公D・新 |

### 分野12 任せて並べる（自律・並列・自動化）（17ページ）

並列や自律の機能は、作者たちの特殊な使い方から広まった。そのため反論も多い ([marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html); [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey))。2026年に組み込み機能が整い、2025年の自作の仕組みの多くは置き換えられた ([paddo.dev: Ralph](https://paddo.dev/blog/ralph-wiggum-autonomous-loops/))。公式は無人で走らせる前に五つの問いを置いている。完了の定義、自分で検証できるか、触ってよい範囲、何で止まるか、誰が承認するか、である ([Best practices](https://code.claude.com/docs/en/best-practices))。この分野の全ページはこの問いを前提にする。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 委任の段階と、任せる前の五つの問い | L4 | 必須 | 比例則。上限（`--max-turns`、`--max-budget-usd`） | 公D |
| /goal（完了するまで続けさせる） | L4 | 必須 | 測れる終了状態。evaluator は会話に出た証拠しか見ない。ターン上限 | 公D・英 |
| /loop と定期実行の三方式 | L4 | 推奨 | セッション内、Desktop、クラウド。7日で失効する | 公D |
| クラウドの定期タスク（旧 routines） | L5 | 推奨 | トリガーの種類。成功の定義を書く | 公D |
| headless（`claude -p`）の基本 | L5 | 必須 | 出力形式、`--json-schema`、承認は既定で拒否される | 公D |
| `--bare` と再現性 | L5 | 推奨 | 自動検出をスキップする。将来は既定になる予定 | 公D |
| GitHub Actions と @claude | L5 | 推奨 | `@v1`。CLAUDE.md にレビュー基準を書く。最小権限 | 公D |
| 自動 PR レビュー（Code Review・/ultrareview） | L4 | 任意 | 管理されたレビュー。費用と使いどころ | 公D |
| 並列の五方式の選び方 | L4 | 必須 | subagent、agent view、agent teams、projects、workflows。誰が調整するか | 公D |
| git worktree で並列にする | L4 | 必須 | `-w`。`.worktreeinclude`。依存のインストールは worktree ごとに要る | 公D・日 |
| agent view と背景セッション | L4 | 推奨 | 投入して監視する。research preview | 公D |
| agent teams（実験的） | L5 | 任意 | トークンは約7倍。書き込みが多いと衝突する | 公D・日 |
| dynamic workflows（ultracode） | L5 | 推奨 | 大規模な監査や移行。まず小さく試す。Large の警告 | 公D |
| fan-out（/batch と `-p` ループ） | L5 | 任意 | 2〜3ファイルで試してから全体へ | 公D |
| 並列の上限は人間が決める | L4 | 必須 | レビューのボトルネック、疲労、1〜3本から始める | 英・日 |
| 自作ループ（Ralph など）の現在 | L4 | 任意 | 考え方は残り、組み込み機能に置き換わった | 英 |
| 自動化の選び方（routine・headless・SDK） | L5 | 推奨 | 比較ページ | 教・公D |

### 分野13 API・SDK の概念（14ページ）

ここはコードの書き方を教える分野ではない。アプリや Claude Code の挙動を「仕組みから」理解するための概念を扱う。アプリの機能には API に対応物がある。project knowledge の cache は prompt caching に、自動の context 管理は compaction に、Memory は memory tool に、アプリの Skills は Agent Skills に対応する ([Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching); [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction))。この対応表は、パワーユーザーにとって最も価値の高いページになる。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| アプリの機能と API の概念の対応表 | L3 | 必須 | cache、compaction、memory、skills、定期実行 | 公D・新 |
| Messages API と会話の正体 | L3 | 推奨 | 状態を持たない。毎回全履歴を送る。system と messages | 公D |
| tool use のループ | L4 | 推奨 | client tools と server tools。tool_choice、strict | 公D |
| structured outputs（形式を保証する） | L4 | 推奨 | prefill の代わり。保証されない場合 | 公D |
| prompt caching の実務 | L4 | 推奨 | ブレークポイント、TTL、cache を壊す操作 | 公D |
| Batch API | L5 | 任意 | 50%引き。24時間以内に処理される | 公D |
| citations と根拠の返却 | L4 | 任意 | プロンプトで引用させるより確かである | 公D |
| ファイル・PDF・画像の扱い | L4 | 任意 | Files API。vision | 公D |
| 長時間エージェントの context 管理 | L5 | 推奨 | compaction、context editing、memory tool の組み合わせ | 公D |
| Agent SDK（Claude Code をライブラリとして使う） | L5 | 推奨 | 同じツールとループ。`.claude/` を読む。プランとの関係 | 公D |
| Managed Agents | L5 | 任意 | Agent、Environment、Session。料金の考え方 | 公D |
| Client SDK・Agent SDK・Managed Agents・CLI の比較 | L4 | 必須 | 比較ページ（自分でループを書くか、ホストさせるか） | 公D |
| エージェント用のツールを設計する原則 | L5 | 任意 | 少数に統合する、名前空間、高シグナルの出力、評価で改善する | 公B |
| プロンプトの評価（eval）入門 | L4 | 推奨 | 成功基準を先に決める。task・trial・grader。pass@k と pass^k | 公B・公D |

### 分野14 費用と利用上限（10ページ）

有料プランには二層の上限がある。5時間ごとの session limit と週ごとの weekly limit で、claude.ai・Claude Code・Desktop が同じ枠を使う ([How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work))。公式の節約策は多い。ただ、実践者の観察では一番効くのは手戻りを減らすことで、トークンの約半分が訂正に消えたという報告もある ([Matsuoka](https://hyperdev.matsuoka.com/p/the-tired-toddler-problem))。この分野では「小手先の節約」より前に「計画と検証」を置く。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 利用上限の仕組み（5時間・週・共有） | L1 | 必須 | 面をまたいで共有される。/clear では上限は戻らない | 公D |
| 上限を早く使う七つの要因 | L2 | 必須 | 長さ、添付、ツール、モデル、effort、artifact、多段の作業 | 公D |
| 節約の優先順位（手戻りを減らすのが先） | L2 | 必須 | 計画、検証、/clear、常駐物の削減、effort | 公D・英 |
| プランの選び方（確認日付き） | L1 | 推奨 | Free・Pro・Max・Team・Enterprise。数値はこの1ページに集約する | 公D |
| Fable を使う前に | L2 | 推奨 | Pro では従量課金、Max では週上限の50%まで。消費が速い | 公D |
| usage credits（超過分の従量課金） | L2 | 推奨 | 自動チャージと月の上限額。日本では6か月で失効する | 公D |
| Claude Code のコストを見る（/usage・status line） | L3 | 必須 | 内訳と推奨。cache の状態 | 公D |
| 並列・ループ・workflows のコスト | L4 | 必須 | 反復回数に比例する。agent teams は約7倍。同時実行数に上限を設ける | 公D・英 |
| API 料金の読み方 | L4 | 任意 | 入力と出力、cache、batch。日本語は token が多めになる | 公D |
| 円での支払い・消費税・インボイス | L1 | 任意 | 為替、2026-04 からの消費税、登録番号、クレジットカードのみ | 日 |

### 分野15 日本語で使う（12ページ）

日本語の論点は出力の品質に集中している。クラスメソッドは、Opus 5.5 が英語のツール出力やサブエージェントの報告を読んだ後に英語へ戻り、CLAUDE.md や memory の指示が一時的にしか効かないことを観察した。そこで UserPromptSubmit・Stop・MessageDisplay の hook で日本語を強制する解決策を作った ([DevelopersIO](https://dev.classmethod.jp/articles/claude-code-hooks-prevent-english-reply/))。言語設定の `language` は、コメントやコミットメッセージには効かない ([Issoh](https://www.issoh.co.jp/tech/details/18753/))。日本語と英語でプロンプトの精度を比べた実測記事は見つからなかった。そのため「日本語で大丈夫か」には「測定はないが、言語より構造が効く」と正直に書く。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 日本語で指示して大丈夫か | L1 | 必須 | 測定データはない。構造が大事。技術用語やパスは原文のまま | 日 |
| 日本語で返し続けさせる | L3 | 必須 | language 設定、CLAUDE.md、hooks。英語に戻る理由 | 日 |
| コミットメッセージ・コメントの言語 | L3 | 推奨 | language は効かない。OSS では個人の設定に置く | 日 |
| です・ます／だ・であるを揃える | L2 | 必須 | お願いでは揺れる。例示と lint | 日 |
| 表記ゆれと漢字の開き | L2 | 推奨 | 表記ルール、prh、Projects の指示 | 日 |
| 「AI臭さ」を減らす | L2 | 推奨 | 具体的な嫌な点、自分の文章を見本に、推敲 skill | 日・英 |
| textlint を hook で回す | L4 | 推奨 | PostToolUse。exit 2 で差し戻す。ルールの例 | 日 |
| 日本語推敲 skill の選び方 | L3 | 任意 | 文体を保つか、再構成するか。比較は1回の出力だけ | 日 |
| 日本語はトークンが多めになる | L2 | 推奨 | 倍率は tokenizer 次第。自分で数える | 研 |
| 文字コード（Shift_JIS の CSV など） | L2 | 推奨 | 集計が空欄になる例。UTF-8 にしてから渡す | 日 |
| Windows・WSL・IME で困ったら | L2 | 任意 | sandbox は WSL2 で。日本語環境のトラブル（要調査） | 公D・新 |
| 日本語の資料を読ませる・書かせる | L2 | 推奨 | 縦書きや PDF、敬語、社内用語集 | 新 |

### 分野16 用途別レシピ（14ページ）

公式の Common workflows は、どのレシピも「質問 → 提案 → 適用 → 検証」の四段で書かれている ([Common workflows](https://code.claude.com/docs/en/common-workflows))。日本語で最も読まれたのは、非エンジニアの日常業務への応用だった ([みのるん Qiita](https://qiita.com/minorun365/items/114f53def8cb0db60f47))。レシピは演習ではない。「推奨の頼み方」「確かめ方」「よくある失敗」を三点セットにした参照ページとして書き、面ごとのタブで並べる。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 知らないコードベースを読む | L2 | 必須 | 広く聞いてから絞る。用語集を作らせる。シニアに聞くように | 公D |
| バグを直す | L2 | 必須 | 再現手順と完了の定義。失敗するテストを先に書く。症状を抑えるだけにしない | 公D |
| リファクタリングと大規模な移行 | L3 | 推奨 | 挙動を保つ。小さく分ける。workflows | 公D |
| テストを足す | L3 | 推奨 | 既存のスタイルに合わせる。境界値 | 公D |
| PR を作り、レビューを受ける | L3 | 推奨 | リスクを挙げさせる。draft PR。`--from-pr` | 公D・英 |
| 仕様を先に固める（spec・インタビュー・モック先行） | L3 | 必須 | 作業の型を比べる。実装は新しいセッションで | 英・日 |
| ドキュメント・技術文書を書く | L2 | 推奨 | プロジェクトの標準に照らす。文体（分野15） | 公D・日 |
| データ分析（SQL を書かずに） | L3 | 推奨 | CLI 経由。生データで裏を取る | 英 |
| 調べものとレポート | L2 | 必須 | Research と Claude Code の使い分け。出典の確かめ方 | 公D・新 |
| 資料・スライドを作る | L2 | 推奨 | Artifacts の Slides、Marp。最後の2割は人が仕上げる | 公D・日 |
| 事務作業の半自動化（経費・報告） | L3 | 推奨 | 人→AI→人のサイクル。私的な情報の扱い。手順を育てる | 日 |
| ノート・PKM（Obsidian など） | L3 | 任意 | vault で動かす。バックアップを取る | 英 |
| フロントエンドのデザイン | L3 | 任意 | 何も言わないと汎用的な見た目になる。スクリーンショットで比べる | 公D |
| 雑務をまとめたモノレポ | L4 | 任意 | 業務ごとのディレクトリと README。文脈を蓄積する | 日 |

### 分野17 組織で使う（9ページ）

日本の導入事例には、情報システム部門の制約に合わせた構成が多い。MDM での配布、管理者権限のない端末、LiteLLM ゲートウェイ、Bedrock 経由などである ([@IT メルカリ](https://atmarkit.itmedia.co.jp/ait/spv/2608/04/news002.html); [DevelopersIO](https://dev.classmethod.jp/articles/claude-code-bedrock-governance-tips/))。一方で、マネージャー層でマージまでの時間が93.5%増えた例もある。導入時の人の負荷も、組織の論点として扱う ([CodeKnights](https://www.codeknights.co.jp/contents/claude-japan-cases-2026summer))。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| チームで設定を共有する | L4 | 推奨 | CLAUDE.md、`.claude/settings.json`、`.mcp.json`、plugins。個人用と共有用を分ける | 公D・日 |
| Team と Enterprise の違い（概念） | L4 | 任意 | SSO、監査、保持期間、使用量の課金方式 | 公D・日 |
| managed settings と MCP の組織管理 | L5 | 任意 | MDM、claude.ai の管理コンソール、managedMcpServers | 公D・日 |
| 監査ログと可視化（OpenTelemetry など） | L5 | 任意 | 何が記録され、何が記録されないか | 公D・日 |
| 禁止ではなく安全な道を作る | L4 | 推奨 | セキュリティ部門と協力する。低リスクから始める。研修 | 日 |
| 社内ガイドラインに書くこと | L4 | 推奨 | データ区分、許可する面とモード、レビューの責任 | 日・新 |
| レビューのボトルネックと疲労 | L4 | 必須 | 並列化の副作用。マネージャー層で詰まる | 日 |
| Bedrock・Vertex・Foundry 経由で使う | L5 | 任意 | 管理コンソールが使えない場合の統制 | 公D・日 |
| チームに広める（/team-onboarding など） | L4 | 任意 | 利用履歴から立ち上げガイドを作る | 公D |

### 分野18 症状辞典（20ページ）

症状ページは「症状の確認 → 六つの原因のどれか → 即効の対処 → 構造的な対処 → 関連する原理」の順に書く。逆引きで最も多く引かれる受け皿になる。英語圏の分析でも、熟練度の差が最も出るのは「うまくいかなくなった後の立て直し」の場面だった ([Creeta](https://news.creeta.com/en/claude-code-expertise-domain-over-coding-2026/))。

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 意図と違うものが出てくる | L1 | 必須 | ①。具体性の4点、手本、質問させる | 公D |
| 長い会話で前提を忘れる・雑になる | L1 | 必須 | ②。新しい会話、要約して引き継ぐ | 研・公D |
| 同じ失敗を繰り返す（堂々巡り） | L2 | 必須 | ②。2回で /clear、巻き戻す、書き直す | 公D |
| 「完了」と言うが終わっていない | L2 | 必須 | ③。証拠を求める、検証の階段 | 公D・研 |
| テストを書き換えて通した | L3 | 必須 | ③④。保護 hook、一般解を求める | 研・公D |
| CLAUDE.md や指示が守られない | L3 | 必須 | ②④。短くする、rules、hook へ | 公D・英・日 |
| 頼んでいないことまでやる（過剰設計） | L2 | 必須 | ①⑤。範囲を指定する、/simplify、effort | 公D・英 |
| 確認ばかりで進まない・途中で止まる | L2 | 推奨 | ⑤。Sonnet の low・medium の癖、最後までやらせる指示 | 公D |
| 存在しない関数やパッケージを使う | L2 | 必須 | ①③。読んでから答えさせる、LSP、パッケージを確かめる | 研・公D |
| もっともらしい嘘・出典の誤り | L1 | 必須 | ①③。引用、照合、分からないと言わせる | 公D・研 |
| すぐ同意して意見を変える（迎合） | L2 | 推奨 | ③。独立したレビュアー、反証を求める | 公B |
| 最新の情報を知らない | L1 | 必須 | ①。カットオフ、検索、日付 | 公D |
| 添付した資料の後半を読んでいない | L1 | 推奨 | ①②。100ページの壁、分割、ページ番号 | 公D |
| 圧縮の後に約束を忘れた | L3 | 必須 | ②④。CLAUDE.md、deny | 公D |
| 英語で返ってくる | L2 | 必須 | ④。分野15 | 日 |
| すぐ上限に当たる | L1 | 必須 | ⑤。七つの要因、手戻り | 公D |
| 急に賢くなくなった気がする | L2 | 必須 | ⑤。版、effort、モデル、コンテキスト量の順に確かめる | 公B・日 |
| 承認の確認が多すぎる・少なすぎる | L3 | 推奨 | ⑤⑥。モード、allowlist、sandbox | 公D |
| 消してはいけないものを消された | L3 | 必須 | ⑥④。復旧の手順、再発防止 | 研・公D |
| 毎回同じ説明をしている | L2 | 必須 | ①。足すタイミング表への入口 | 公D |

### 分野19 古くなった助言と変更の記録（5ページ）

| ページ候補 | Lv | 優先 | 扱う要点 | 根拠 |
|---|---|---|---|---|
| 古くなった助言台帳 | L1 | 必須 | 台帳形式（第5節）。どの原理を補う回避策だったかを書く | 公D・CL・日 |
| 旧名と新名の対応表 | L1 | 必須 | aliases から自動生成する | CL |
| 2026年の主な変更年表 | L1 | 推奨 | アプリ・Claude Code・モデル・API の四列 | CL・公D |
| いつの情報かを見分ける | L1 | 推奨 | 記事・書籍・動画の読み方。版と日付を確認する | 新 |
| 最新を自分で確かめる方法 | L2 | 推奨 | CHANGELOG、`/release-notes`、Claude に聞く、/doctor prompt-audit | 公D |

## 4. 逆引き73項目は読者の言葉で書き、六つの原因へ戻す

逆引きは各ページの front matter の `signs` から自動生成する。公式の「足すタイミング表」は回数のしきい値付きの対応表で ([Extend Claude Code](https://code.claude.com/docs/en/features-overview))、日本語の「〜したい」型の逆引き記事は一問一答形式だった ([Zenn](https://zenn.dev/ml_bear/articles/84e92429698177))。どちらも先例になる。見出しには読者の言葉を使う。「指示を無視される」「毎回同じことを説明している」「会話が長くなると精度が落ちる」などである。原因タグは読者が次に疑う方向を示す。①見えていない、②散らかっている、③確かめていない、④縛っていない、⑤合っていない、⑥境界がない、の六つで、目的別の行には目的の分類を付ける。以下は、生成される逆引きのうち手作業で検証した核となる項目の例である。

### 返答と品質の困りごと

| 症状・やりたいこと | 引くページ | 原因 |
|---|---|---|
| 頼んだものと違うものが出てくる | 意図と違うものが出てくる／具体性の4点 | ① |
| 毎回同じ背景を説明している | 指示の置き場所（アプリ）／足すタイミング表 | ① |
| 「いい感じに」と頼むと平凡になる | 新人の同僚に頼むつもりで／例を見せる | ① |
| 提案だけで止まり、実行してくれない | 提案してほしいのか、実行してほしいのか | ① |
| 頼んでいない機能やファイルが増える | 頼んでいないことまでやる／範囲を伝える | ①⑤ |
| もっともらしいが出典が怪しい | もっともらしい嘘・出典の誤り／引用や出典の確かめ方 | ③ |
| 最近の出来事や新しい版について間違える | 最新の情報を知らない／知識カットオフ | ① |
| 同じ質問で毎回答えが違う | 同じ質問でも答えが変わる／事実を確かめる | ③ |
| こちらの誤った指摘にもすぐ同意する | すぐ同意して意見を変える | ③ |
| 長い PDF の後半の図について答えられない | 添付した資料の後半を読んでいない | ①② |
| 推論の過程を全部見せてほしい | 推論を見せてほしいとき／表示された推論は内部と一致しない | ― |
| 回答が長すぎる・短すぎる | 出力の形と分量を指定する／モデル別の癖 | ⑤ |
| 文章が「AI っぽい」 | 「AI臭さ」を減らす／文章を頼むとき | ① |
| 返事が英語になる | 英語で返ってくる／日本語で返し続けさせる | ④ |
| です・ますとだ・であるが混ざる | です・ます／だ・であるを揃える／textlint を hook で回す | ④ |
| 「サーバー」と「サーバ」が混在する | 表記ゆれと漢字の開き | ④ |

### 会話と文脈の困りごと

| 症状・やりたいこと | 引くページ | 原因 |
|---|---|---|
| 会話が長くなると精度が落ちる | 長い会話で前提を忘れる／context rot | ② |
| 同じバグの修正を何度も失敗する | 同じ失敗を繰り返す／違うと返すより巻き戻す | ② |
| どのタイミングで新しい会話にすべきか分からない | 新しい会話を始めるタイミング | ② |
| 圧縮されたら前に決めたことを忘れた | 圧縮の後に約束を忘れた／compaction で何が残るか | ②④ |
| 長い作業を明日も続けたい | handoff 文書／進捗ファイル／セッションの命名と再開 | ② |
| ちょっとした質問で本筋を汚したくない | 本筋を汚さずに聞く（/btw） | ② |
| 何がコンテキストを占めているか知りたい | /context で中身を見る／常駐するもののコスト | ② |
| 大量のログやテスト出力で会話が埋まる | 調査は subagent に任せる／hook でテスト出力を絞る | ② |
| 別のプロジェクトの記憶が混ざる | Memory の仕組みと範囲／Memory の困りごと FAQ | ② |
| 会話を消したのに覚えている | Memory の困りごと FAQ | ⑥ |
| 記録を残さずに相談したい | Incognito／送ったデータの行方 | ⑥ |
| 1M コンテキストなら気にしなくてよいのか | 1M コンテキストとの付き合い方／注意の予算 | ② |

### 指示と仕組みの困りごと（主に Claude Code）

| 症状・やりたいこと | 引くページ | 原因 |
|---|---|---|
| CLAUDE.md に書いたのに守られない | CLAUDE.md や指示が守られない／お願いを鍵に移す判断 | ②④ |
| CLAUDE.md が長くなってきた | CLAUDE.md の長さと剪定／rules と paths | ② |
| CLAUDE.md に何を書けばよいか分からない | CLAUDE.md に書くこと／書かないこと | ① |
| 特定のディレクトリだけのルールを書きたい | .claude/rules と paths | ② |
| 同じ手順書を何度も貼っている | Skills の考え方／Skill の作り方 | ① |
| 作った skill が使われない | Skill の description の書き方 | ① |
| デプロイ用の skill を勝手に動かされたくない | 副作用のある skill を勝手に動かさない | ④ |
| 毎回フォーマッタをかけさせたい | 代表的な hook のレシピ | ④ |
| `.env` や migrations を絶対に触らせたくない | 権限ルール／exit 2 でブロック／秘密情報を守る | ④⑥ |
| テストが通るまで終わらせたくない | Stop hook で「終わらせない」／検証の階段 | ③④ |
| skill と subagent のどちらにすべきか | Skill と Subagent の違い | ― |
| MCP を入れるか CLI で済ませるか | MCP か CLI か | ⑤ |
| 他のエージェントツールと指示を共有したい | AGENTS.md と他ツールとの共有 | ― |
| 入れた拡張が多すぎて重い | 拡張の棚卸しと剪定／常駐するもののコスト | ②⑤ |
| チームで同じ設定を使いたい | チームで設定を共有する／Plugins | ― |

### 確かめ方の困りごと

| 症状・やりたいこと | 引くページ | 原因 |
|---|---|---|
| 「全部通りました」と言うが信用できない | 報告ではなく証拠を求める／「完了」と言うが終わっていない | ③ |
| テストのほうを書き換えて通された | テストを書き換えて通した／テストを守る | ③④ |
| 自分の目で全部レビューする時間がない | 書いた本人ではない者にレビューさせる／人間が読むべき差分の箇所 | ③ |
| 見た目の崩れを確かめさせたい | 画面で確かめる | ③ |
| CLAUDE.md を変えて良くなったか知りたい | 変更が効いたかを測る／体感と実測 | ③ |
| 調査結果の出典を確かめたい | 引用や出典の確かめ方／Research を使いこなす | ③ |

### 安全の困りごと

| 症状・やりたいこと | 引くページ | 原因 |
|---|---|---|
| 確認ボタンを読まずに押している | 承認疲れ／auto mode は何を止めるか | ⑥ |
| auto mode に任せて大丈夫か | auto mode は何を止め、何を止めないか／sandbox | ⑥ |
| 知らない人のリポジトリを開きたい | 知らないリポジトリを開く前に | ⑥ |
| 便利そうな MCP や plugin を見つけた | MCP・plugins・skills を入れる前の確認 | ⑥ |
| Web ページやメールを読ませるのが不安 | prompt injection の実際／三つを同時に持たせない | ⑥ |
| ファイルを消された・消されそうで怖い | 消してはいけないものを消された／checkpoint と rewind | ⑥ |
| 入力した内容が学習に使われるか知りたい | 送ったデータの行方 | ⑥ |
| 会社や学校で使ってよいか確かめたい | 学校・組織・コンテストの規則／社内ガイドラインに書くこと | ⑥ |

### 費用・選び方・任せ方

| 症状・やりたいこと | 引くページ | 原因 |
|---|---|---|
| すぐ上限に当たる | すぐ上限に当たる／上限を早く使う七つの要因 | ⑤ |
| /clear すれば上限は戻るのか | 利用上限の仕組み | ⑤ |
| Pro と Max のどちらにすべきか | プランの選び方 | ⑤ |
| Fable を使ってみたい | Fable を使う前に／モデルの選び方 | ⑤ |
| 急に性能が落ちた気がする | 急に賢くなくなった気がする | ⑤ |
| effort を上げるべきか、モデルを替えるべきか | モデルの選び方（三段階）／effort の段階 | ⑤ |
| 「think hard」は効くのか | 「考えて」と書くことの現在／古くなった助言台帳 | ⑤ |
| アプリと Claude Code のどちらでやるべきか | アプリ・Claude Code・API の選び方 | ⑤ |
| 席を外している間も進めてほしい | 委任の段階と五つの問い／/goal／クラウドの定期タスク | ― |
| 毎朝決まった調査をさせたい | /loop と定期実行の三方式／タスクと定期実行 | ― |
| 複数の作業を同時に進めたい | 並列の五方式の選び方／git worktree | ― |
| 並列にしたら疲れた | 並列の上限は人間が決める／レビューのボトルネックと疲労 | ⑤ |
| スクリプトや CI から使いたい | headless の基本／GitHub Actions | ― |
| 自分のアプリに Claude を組み込みたい | Client SDK・Agent SDK・Managed Agents・CLI の比較 | ― |
| コードを書かない仕事に Claude Code を使いたい | Claude Code を非エンジニアが使う／事務作業の半自動化 | ― |
| 古い記事のやり方が通じない | 古くなった助言台帳／旧名と新名の対応表 | ― |

## 5. 公式に任せる部分と、31項目の古くなった助言台帳

### 公式ドキュメントに任せ、辞典は判断に集中する

扱いを軽くするのは五つの領域である。**インストールと OS 別の設定**は、公式ドキュメントと日本語チートシートへのリンクで済ませる。**全コマンド・全設定キー・全33種の hook イベントの網羅**は、公式リファレンスが週ごとに更新されるので、早見表は自動生成の索引にとどめる ([Hooks](https://code.claude.com/docs/en/hooks); [Commands](https://code.claude.com/docs/en/commands))。**research preview や実験的な機能の操作手順**（Mods、agent teams、Duet、Claude Design など）は、成熟度バッジを付けた概念紹介にとどめる。**第三者のプラグインやツール**（Superpowers、cc-sdd、Serena、ccusage など）は「考え方の例」として名前を出すだけにし、推薦リストにはしない。**API のパラメータやコード例**は、概念と対応関係だけを書く。軽く扱う部分でも「なぜ」は省かない。たとえば「MCP を全部入れない」理由はコンテキストのコストであり、基礎ページへのリンク一本で示せる。

書かないものは三つの基準で決める。一つ目は**根拠の弱い数値**である。「◯倍速くなった」という自己申告の生産性、逆コンパイルから推測された日本語の思考キーワード（「熟考」で31,999トークン、など。[Gist](https://gist.github.com/oikon48/980b89462904aa1980c5d188b30d1f54)）、2025年末のコミュニティ推定である「最先端モデルが従える指示は150〜200個」などがこれに当たる。こうした数値は本文の主張には使わず、使う場合は「経験則」と明記する。企業事例の数値は、自己申告であることを添えて使う。二つ目は**安全装置を外す近道を勧めること**で、`--dangerously-skip-permissions` を普段使いすること、sandbox の外での再試行を常に許すこと、アカウントを共有することなどがこれに当たる。三つ目は**特定の個人の構成を標準として示すこと**で、Boris Cherny の並列5〜10本や Opus 常用は、反対意見と並べて紹介する。

これとは別に、**AI Fluency の 4D をそのまま章の構成に使う**ことも避ける。4D は CC BY-NC-ND なので、改変した派生フレームワークとして再配布せず、参照と引用にとどめる ([Ringling LibGuide](https://ringling.libguides.com/ai/framework))。

### 古くなった助言は台帳にして「どの原理の回避策だったか」を残す

教材の中に「古くなった助言」ページを独立して置くことを強く勧める。公式自身が「The old advice / Why it's gone」の表を持っている ([Best practices](https://code.claude.com/docs/en/best-practices))。日本語圏でも、2025年の記事の記法や前提が大量に流通したまま残っている ([adalocamp](https://zenn.dev/adalocamp/articles/claude-code-advanced-tips); [acntechjp](https://zenn.dev/acntechjp/articles/5bf01d6b530b8d))。

台帳の各行には、次の項目を持たせる。「古い助言」「今どうするか」「変わった時期と版」「どの原理を補う回避策だったか」「自分の設定や記事で見つける方法」「出典」「確認日」である。各ページの front matter の `outdated_advice` からこの台帳に逆リンクを張り、「この助言に関係するページ」を自動で一覧にする。

状態は三つに分ける。「撤回」は使えないか、使うべきでないもの。「置換」は正式な仕組みに置き換わったもの。「条件付き」は今も効くが前提が変わったもの、たとえば /clear や ultrathink である。

| 古い助言 | 今どうするか | 変化の時期 | 状態 | 出典 |
|---|---|---|---|---|
| `#` で始めると CLAUDE.md に記憶される | Claude に CLAUDE.md の編集を頼む | v2.0.70（2025-12-15） | 撤回 | [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| `.claude/commands/` にカスタムコマンドを作る、`/project:name` 記法 | skills で作る（既存のファイルは動く） | 2026-01 | 置換 | [Skills](https://code.claude.com/docs/en/skills) |
| `/agents` で subagent を作る | Claude に作らせるか、ファイルを直接書く | v2.1.198（2026-07-01） | 撤回 | [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| think → think hard → ultrathink の段階、日本語の「熟考」 | effort で調整する。ultrathink だけが1ターンの深い推論として有効 | 2026-01〜03 に変遷 | 置換 | [Model config](https://code.claude.com/docs/en/model-config); [Awesome Agents](https://awesomeagents.ai/news/claude-code-ultrathink-returns-medium-effort-default/) |
| IMPORTANT や YOU MUST で強調すれば守られる | 強調は1行だけにし、守られないなら hook・deny へ | 2026（公式の撤回表） | 撤回 | [Best practices](https://code.claude.com/docs/en/best-practices) |
| `--dangerously-skip-permissions` で YOLO 運用 | auto mode と sandbox。bypass は隔離環境だけ | 2026-08〜09 | 置換 | [Permission modes](https://code.claude.com/docs/en/permission-modes) |
| 最初は毎回承認を求められる | 対話セッションの既定は auto mode | v2.1.283（2026-09-25） | 撤回 | [Permission modes](https://code.claude.com/docs/en/permission-modes) |
| 200k を前提にコンテキストを最優先で節約する | 1M と自動圧縮。質とコストのために /clear する | 2026 | 条件付き | [Best practices](https://code.claude.com/docs/en/best-practices) |
| アーキテクチャやファイル構成を CLAUDE.md に書く | 推測できない理由と落とし穴だけを書く | 2026（公式の撤回表） | 撤回 | [Best practices](https://code.claude.com/docs/en/best-practices) |
| 「keep going」「don't be lazy」と書く | 完了条件と /goal を使う。過剰作業の原因になる | 2026（公式の撤回表） | 撤回 | [Best practices](https://code.claude.com/docs/en/best-practices) |
| 「最後に double-check して」と書き足す | 検証の手段を渡す。5世代のモデルは自分で検証する | Opus 5 世代 | 条件付き | [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) |
| 「subagent を使え」と書き足す | 大きく独立したタスクに限る。委任しすぎを抑える | Opus 5 世代 | 条件付き | [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) |
| 工程ごとに subagent を大量に作る | 文脈の独立性で分ける | 2026 | 撤回 | [DevelopersIO](https://dev.classmethod.jp/articles/claude-code-subagent-review/) |
| prefill で JSON の形を強制する | structured outputs を使う | Claude 4.6 以降は400エラー | 撤回 | [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| `budget_tokens` で思考量を指定する | adaptive thinking と effort | 4.7 以降は400エラー | 撤回 | [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| `<thinking>` タグに推論を書かせる | 要約された thinking を見るか、短い根拠を頼む | 最新世代 | 撤回 | [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) |
| Console の prompt generator / improver を使う | 退役した。best practices と eval で改善する | 2026-08-17 | 撤回 | [Platform release notes](https://platform.claude.com/docs/en/release-notes/overview) |
| 公式インタラクティブチュートリアルが最新の作法 | Claude 3 世代向け。食い違いは best practices に従う | ― | 条件付き | [Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) |
| Cowork は別アプリ、Web search はトグルで入れる | 一つの会話に統合され、検索は Claude が自分で判断する | 2026-09-16 | 撤回 | [統合の記事](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude) |
| Memory は会話の後に日次で要約される | 会話中にトピック単位で保存される | 2026-07-10 | 撤回 | [Release notes](https://support.claude.com/en/articles/12138966-release-notes) |
| Claude Code on the Web、`--remote` | クラウドセッション、`--cloud` | 2026-09 | 置換 | [Web](https://code.claude.com/docs/en/claude-code-on-the-web) |
| routines | cloud scheduled tasks（URL には旧名が残る） | 2026 | 置換 | [Routines](https://code.claude.com/docs/en/routines) |
| `/cost`、`/stats` | `/usage`（旧名は別名として動く） | 2026 | 置換 | [Commands](https://code.claude.com/docs/en/commands) |
| `/fork` で会話を分岐する | `/branch`。現在の `/fork` は別の機能 | v2.1.77（2026-03-16） | 置換 | [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| `/vim`、`/tag`、`/pr-comments`、ultraplan、TaskOutput ツール | 削除された（vim は /config の Editor mode へ） | 2026-04〜09 | 撤回 | [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| MCP の SSE transport | HTTP を使う | 2026 | 撤回 | [MCP](https://code.claude.com/docs/en/mcp) |
| GitHub Action `@beta`、`direct_prompt` | `@v1`、`prompt`、`claude_args` | 2026 | 置換 | [GitHub Actions](https://code.claude.com/docs/en/github-actions) |
| workflow というトリガー語、extra usage | `ultracode`、usage credits | v2.1.160、v2.1.144 | 置換 | [CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| Ralph プラグインや自作 bash ループで回し続ける | /goal、/loop、dynamic workflows | 2026-05〜06 | 置換 | [paddo.dev](https://paddo.dev/blog/ralph-wiggum-autonomous-loops/) |
| tmux で自作のエージェント組織を作る | agent view、agent teams（実験的） | 2026-02 | 置換 | [gihyo.jp](https://gihyo.jp/article/2026/02/get-started-claude-code-07) |
| Opus は高いので避ける | Opus 5.5 は $4/$20 で、多くのプランの既定 | 2026-09 | 条件付き | [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) |

この台帳には「かつてはなぜ正しかったか」も書いておく。それが公平であり、読者が次に何かが撤回されたときにも自分で判断できるようになるからである。たとえば `think hard` は、思考予算をキーワードでしか変えられなかった時代の回避策だった。IMPORTANT の多用は、指示に従う精度が低かった世代の回避策だった。こうした回避策は、正式な制御手段（effort、hooks、auto mode）が整うと役目を終える。この規則性を台帳の冒頭に書いておけば、台帳そのものが「変化への備え方」の教材になる。

## 6. 鮮度はメタデータと点検の流れで保ち、見せ方は「比べる・対にする・注釈する」で揃える

### 変わりやすさでページを分け、数値は一か所に集める

鮮度を保つうえで最初に決めるべきなのは、「何がいつ古くなるか」をページの属性として持たせることである。調査からは、古くなる速さが三層に分かれることが分かった。**原理の層**（基礎、背骨、頼み方の原則）は年単位で持つ。context rot の研究は2025年のものだが、2026年の公式文書でも前提として引かれている ([Chroma](https://trychroma.com/research/context-rot); [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents))。**機能の使い方の層**は月単位で変わる。**数値・既定値・名称の層**（料金、上限、既定のモデルと effort、research preview の機能名）は週単位で変わる。2026年に既定 effort が high から medium に下げられ、品質の不満が出て約1か月後に戻された経緯がその例である ([InfoQ](https://infoq.com/news/2026/05/anthropic-claude-code-postmortem))。

そこで front matter に `volatility`（低・中・高）と `verified`（確認日）を持たせ、点検の期限を自動で計算する。期限は、低なら365日、中なら90日、高なら30日を目安にする。期限を過ぎたページには、ビルド時に「この情報は確認から N 日経っている」という注意書きを自動で差し込む。

数値や既定値は本文に直接書かない。`data/facts.yml` のような一つのファイルにまとめ、項目ごとに出典と確認日を持たせる。本文からは mkdocs-macros などで参照する。こうすると、料金が改定されたときに一か所を直すだけで全ページに反映される。

| 項目 | 例 | 目的 |
|---|---|---|
| `verified` | 2026-10-29 | ページ全体の確認日 |
| `verified_with` | `claude_code: 2.1.312`、`models: [claude-opus-5-5]`、`app: 2026-09 新体験` | どの版で確かめたか。CHANGELOG と照らし合わせるための基準になる |
| `volatility` | 低 / 中 / 高 | 点検の周期と注意書きの基準 |
| `maturity` | GA / beta / research preview / experimental | 成熟度のバッジ。名称が揺れることへの警告 |
| `tracks` | `[/goal, permissions.defaultMode, effortLevel]` | そのページが依存するコマンド・設定キー・機能名。変更検知に使う |
| `aliases` | `[routines, Claude Code on the Web]` | 旧名からの検索と、用語索引の生成 |
| `outdated_advice` | `[think-hard, important-caps]` | 台帳への逆リンク |
| `sources` | `{type: 公D, url: ..., checked: 2026-10-29}` | 根拠の種類を表示し、リンク切れを検査する |

点検は Claude CLI の定期作業にすると回しやすい。週に一度、前回確認した版以降の CHANGELOG と、Help Center・プラットフォームのリリースノートの差分を読ませる。差分に出てくる語を各ページの `tracks` と `aliases` に照らして、影響を受けるページの一覧を出させる。影響があったページは出典を読み直し、人が承認してから `verified` を更新する。

注意すべき点は二つある。一つは、公式文書そのものが移転することである。Claude Code の文書は docs.anthropic.com から code.claude.com に移り、旧ブログの記事も文書へリダイレクトされている ([Best practices](https://code.claude.com/docs/en/best-practices))。だからリンク切れとリダイレクトの検査も同じ作業に入れる。もう一つは、公式の情報同士が食い違うことである。調査中にも二つ見つかった。Fable 5.1 の公開日は、ニュース一覧と Help Center で 09-15 と 09-01 に分かれていた ([Anthropic News](https://www.anthropic.com/news/models); [Release notes](https://support.claude.com/en/articles/12138966-release-notes))。Free プランで project instructions を使えるかについても、記事によって記述が違った ([Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects); [personalization](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features))。食い違いを見つけたら、facts.yml に「出典で食い違いあり」と書き、両方の出典を残す運用にしておく。

制作の手順にも鮮度の規則を組み込む。planning/catalog は、ページの一覧と front matter の唯一の正本にし、雛形はそこから生成する。Claude CLI で下書きするときは、出典のない数値を本文に入れない。下書きのたびに、会話を見ていない別のエージェントに、主張と出典の照合と、数値が facts.yml を経由しているかを確かめさせる。最終的な公開は人が承認する。これは本教材が教える「縛る」と「確かめる」を、教材の制作そのものに当てはめたものである。front matter の具体例を下に示す。

```yaml
---
title: CLAUDE.md や指示が守られない
type: symptom            # concept / feature / symptom / comparison / recipe / ledger
level: L3
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 見せる]
prevents: [散らかっている, 縛っていない]
summary:
  can: 守られない原因を切り分け、どれを仕組みに移すか判断できる
  when: CLAUDE.md や指示に書いたルールが破られたとき
  prereq: CLAUDE.md の位置づけ、お願いと鍵
prerequisites: [basics/claude-md-position, basics/request-vs-lock]
related: [extend/rules-paths, enforce/hooks-recipes, ledger/outdated#important-caps]
signs:
  - CLAUDE.md に書いたのに守られない
  - 「必ず」と書いても破られる
  - 長いセッションの途中から規約を無視し始める
aliases: [指示を無視される]
maturity: GA
volatility: 中
verified: 2026-10-29
verified_with: {claude_code: 2.1.312, models: [claude-opus-5-5]}
tracks: [CLAUDE.md, .claude/rules, /doctor prompt-audit]
outdated_advice: [important-caps]
sources:
  - {type: 公D, url: "https://code.claude.com/docs/en/memory", checked: 2026-10-29}
  - {type: 公D, url: "https://code.claude.com/docs/en/best-practices", checked: 2026-10-29}
---
```

機能ページでは、これに加えて `enforcement`・`context_cost`・`load_timing`・`survives_compaction` を持たせる。比較表はこれらの属性から自動で生成する。

### 演習の代わりに、比較・対比・注釈・判断例で分からせる

演習は作らない。その代わりに六つの見せ方を全ページで使い回す。どれも既存の教材で評価されているか、需要があると確認できたものである。

**一つ目は、Before/After の対比表である。** 公式は Best practices で「Instead of / Try」の表を使っている ([Best practices](https://code.claude.com/docs/en/best-practices))。本教材ではこれに三つの工夫を加える。各行に「何が足されたか」を具体性の4点で注記する。面ごとのタブ（アプリ / Claude Code / API）で同じ原理の書き換えを並べる。日本語の依頼文で書く。CLAUDE.md にも同じ形の対比を使える。たとえば200行の悪い例を60行に削る過程を、各行の削除テストの判定付きで示すと、「何を書かないか」が一目で分かる。

**二つ目は、属性から生成する比較表である。** 公式の Extend Claude Code は、機能を「何をするか・いつ使うか・読み込みの時期・コンテキストのコスト・決定論か」で比べ、ペアごとの比較タブも持っている ([Extend Claude Code](https://code.claude.com/docs/en/features-overview))。本教材ではこれらの列を front matter から生成する。生成するので、手で書いた表と本文が食い違わない。

**三つ目は、比喩付きの図である。** 調査で使えると判断した比喩は次のとおり。

| 概念 | 比喩 |
|---|---|
| コンテキストと注意の予算 | 書類が増えるほど目配りが薄くなる広い机 |
| 毎ターン全履歴を送ること | 毎回最初から読み直す受験者 |
| prompt caching | 付箋。上の段（tools・system）を変えると下の段が全部はがれる積み木 |
| compaction | 議事録だけ残して録音を消す |
| subagent | 調査を頼む別室の部下 |
| ハルシネーション | 白紙を避けて山を張る受験生（OpenAI 論文自身の比喩）([Why Language Models Hallucinate](https://arxiv.org/html/2509.04664v1)) |
| 決定論的と非決定論的 | お願いと鍵 |

ほかに、検証の階段、委任の段階のはしご、Rule of Two の三つ巴の図、指示の置き場所の地図（効く範囲 × 読み込みの時期）を用意する。公式にはコンテキストが埋まっていく様子を見せる対話型のシミュレーションがある ([Explore the context window](https://code.claude.com/docs/en/context-window.md))。本教材では静的な Mermaid か SVG にし、ダークモードにも対応させれば足りる。

**四つ目は、注釈付きのセッション記録である。** 日英どちらの教材にも中心に据えた例が見つからなかったので、差別化の余地が最も大きい。MkDocs Material のコード注釈機能を使い、実際の（または再構成した）やり取りに番号付きの注釈を付ける。最初に用意するとよいのは三本である。堂々巡りのセッションが2回目の訂正の後に /clear で立ち直る例、「全部通りました」という報告を証拠を求めて崩す例、CLAUDE.md に書いた規則が無視されて hook に移す例である。

**五つ目は、判断例である。** 公式ブログは厳密な決定木ではなく、「こういうことをしていたら」という型のシナリオで判断を示している ([Steering Claude Code](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more))。Claude Code in Action の演習名「Rewind, goal, or worktree?」「Which surface owns the rule?」も、判断そのものを問う形になっている ([DataCamp](https://www.datacamp.com/ja/courses/claude-code-in-action))。本教材では答えを伏せない「判断例」として書く。状況、迷う候補、選んだもの、理由を四行の表にする。こうすれば演習を要らないという要望を守りつつ、判断の感覚は伝えられる。

**六つ目は、症状ページの診断チェックリストである。** 六つの原因を安く確かめられる順に並べた確認欄を置き、各項目から対処のページへ飛べるようにする。

ページの冒頭にはバッジの列を置く。並べるのはレベル、原理、強制力（お願いか鍵か）、成熟度、変わりやすさ、確認日と版である。読者は本文を読む前に「どれだけ信用してよい情報か」を判断できる。用語集は、MkDocs Material の略語ツールチップで本文中の語に自動で付ける。機能名・コマンド・ファイル名は原文のまま表記し、公式日本語訳での言い方を括弧で併記する。

## 7. 未決の11論点と、調査の空白

### ユーザーの判断が必要な11の論点

| 論点 | 選択肢 | 本報告の推奨 |
|---|---|---|
| レベル体系 | 委任の段階 L1〜L5（本報告案）／機能の難易度／kyopro-atlas と同じ段階名 | 委任の段階。kyopro-atlas の level は「基礎・水・青・黄・発展」という名前の列挙なので、「使う・整える・任せる・仕組みにする・回す」のような名前で持たせると形式が揃う |
| 分野の切り方 | 活動別＋面別（本報告案）／面別だけ（アプリ編・Code 編・API 編） | 活動別を主にし、面はタブとタグで表す。面別だけにすると「上限」「事実確認」が三か所に分かれてしまう |
| 初版の範囲 | 必須だけ（151）／必須と推奨（261）／全部（300） | 必須だけで公開し、逆引きで多く引かれた項目から推奨を足す。さらに絞るなら、症状辞典・入口・台帳と、そこから prerequisites でたどれるページを第一波にする |
| 料金と数値 | facts.yml に集めて確認日を付けて載せる／公式へのリンクだけ | facts.yml。読者は円換算や上限の目安を求めている ([Zenken](https://ai.zenken.co.jp/post/claude-code-pricing/)) |
| 実在の人物・企業の事例と数値 | 名前と数値を出す／匿名化する／出さない | 出典付きで出し、自己申告の数値は「自己申告」と明記する |
| 第三者ツールの扱い | 推薦リストにする／例として名前を出すだけ | 例として名前を出すだけ。成熟度と確認日を付ける |
| 独自の用語 | 「お願いと鍵」「六つのない」を採用する／公式の用語（決定論的・非決定論的）だけを使う | 独自の用語を見出しにし、公式の用語を併記する |
| 周辺製品の深さ | Design・Science・Duet・Office アドイン・Chrome を個別ページにする／一覧ページだけ | 一覧ページだけにする。research preview が多い |
| コンテストや学校の規則 | 個別の規則を要約して載せる／確認先へのリンクだけ | リンクと「確認すべき点」だけを書く。AtCoder の規則は2026-10-14版に改定されたばかりである ([ISSOH](https://www.issoh.co.jp/column/details/3596/)) |
| 教材自体のライセンスと引用 | CC BY など／公式文書の引用の範囲 | 引用は短くし、出典を示す。AI Fluency は改変せず参照だけにする |
| 鮮度の点検を誰がするか | 作者が手で／Claude CLI の定期作業と人の承認／外部からの PR | 定期作業と人の承認。外部からの「古い」報告は issue のテンプレートで受ける |

### kyopro-atlas の形式との対応（確認済み）

手本の kyopro-atlas は、ページの front matter の規則を `schema/page.schema.json`（JSON Schema）に置き、`tools/` の独立スクリプト（`make_skeleton.py`・`gen_site.py`・`check_pages.py` など）が catalog → 骨格 → 索引・逆引き・知識マップの順に生成と検査をしている。必須のキーは `id`・`title`・`type`・`field`・`order`・`kind`・`prerequisites`・`summary`・`stage`・`updated` で、`type`・`field`・`level`・`kind` は列挙で固定されている。スクリプトの多くは AtCoder 固有（問題の台帳、difficulty、コード片のコンパイル）なので、新しいリポジトリでは流用せず作り直す前提になる。そのため、本報告のメタデータ案を足すこと自体に互換性の問題はない。対応は次のとおり。

| kyopro-atlas | 本教材での対応 |
|---|---|
| `summary`（1文）→ 冒頭の「要点」の囲み（何ができるか・いつ使うか・計算量・前提） | `summary` は1文のまま残し、要点の囲みは「何ができるか・いつ引くか・前提」に。計算量の代わりに「強制力（お願いか鍵か）」や「確認日と版」を出す |
| `signs: {type: phrase / constraint / shape, text}` → 逆引き辞典 | `signs: {type: symptom / goal / situation, text}`（症状・やりたいこと・状況）にすると、§4 の逆引きをそのまま生成できる |
| `level`（基礎・水・青・黄・発展）と、節ごとの `level` | 委任の段階の名前。節ごとの level も、ページより上の段の内容を示すのに使える |
| `frequency`（A/B/C、出題データから算出） | 直接の対応はない。`priority`（必須・推奨・任意）で置き換える |
| `stage`（stub → draft → reviewed → done）と `updated` | そのまま使い、`verified`・`verified_with`・`volatility` を足す |
| `related`（`id#anchor`）、`aliases`、`kind` の固定語彙 | そのまま使う。`kind` の語彙は `principle`・`prevents`・`surfaces` に分けて持たせる |
| `planning/checklists/fact.md` など執筆後の確認表 | 鮮度と出典の確認表（facts.yml 経由か、出典の確認日）を足す |
| `claude/project-instructions.md`（claude.ai で教材を引かせる指示） | 本教材でも同じ仕組みが使え、それ自体が「Projects の使い方」の実例ページになる |

### 調査の空白は一次情報・日本語環境の二つに集中している

公式情報のうち、本文を取得できていないものが八つある。Styles の現行の仕様、チャット共有の仕様、拒否や利用ポリシーへの向き合い方（断られたときの頼み直し方を含む）、IDE 拡張の固有機能、Desktop のローカル MCP の設定、Office アドインの個別機能、Claude Code の「What survives compaction」の完全な一覧 ([Explore the context window](https://code.claude.com/docs/en/context-window.md))、knowledge cutoff 専用の Help Center 記事である。教材を書く前に、これらを一次情報で補う必要がある。

資料の間で食い違う点もあった。ultrathink は、二次情報には「廃止された」という説明と「復活した」という説明が混在している。公式文書は「単一ターンの深い推論要求として現在も有効」としている ([Model config](https://code.claude.com/docs/en/model-config))。auto mode の承認率は、公式の engineering ブログでは93% ([auto mode](https://anthropic.com/engineering/claude-code-auto-mode))、二次報道では97% ([GIGAZINE](https://gigazine.net/gsc_news/en/20260810-claude-code-auto-mode/)) だった。auto mode の既定化の時期も、有料プランが 2026-08-14、対話セッション全体が v2.1.283（09-25）と、二段階で説明されている。本報告では公式の値を使ったが、教材ではどちらの段階を指すかを書き分ける必要がある。

実践知と研究のうち、確認が要るものもある。Anthropic の約40万セッションの研究は、一次ページを取得できず二次要約に頼った。HumanLayer の CLAUDE.md 論も原文は未取得である。データそのものが存在しないものもある。Opus 5.5 世代で過剰設計・迎合・テスト改ざんがどの程度残っているかの定量的なデータ、5.x 世代の tokenizer での日本語と英語のトークン比、日本語と英語の指示で精度を比べた実測は、どれも見つからなかった。

日本語の環境に固有のトラブル（Windows、WSL、IME、文字コード）、claude.ai の Research と Artifacts を深く使う事例、CLAUDE.md の変更の効果を測った記事も見つかっていない。分野15と分野06の該当ページは、作者が自分で確かめた結果を載せる「検証ノート」形式にするか、確認日を付けて控えめに書くことを推奨する。

最後に用語の問題がある。公式の Claude Code 文書には日本語訳がある ([Claude Code docs llms.txt](https://code.claude.com/docs/llms.txt))。その用語と本教材の用語索引を揃えるため、公式日本語訳での主要な訳語を一度洗い出しておく価値がある。

## 結論

この調査から分かったのは、Claude を使いこなす知識には変わりにくい核があるということである。核は小さく、「何を見せるか」「完了をどう確かめるか」「どこまで仕組みで縛るか」の三つに集約できる。2026年に起きた変化の多くは、この三つを満たすための回避策が、正式な仕組みに置き換わった結果だった。`think hard` は effort に、IMPORTANT の連打は hooks に、YOLO モードは auto mode と sandbox に、自作ループは /goal に置き換わった。したがって辞典の価値は、機能を網羅することではなく、変化を吸収できる構造にある。原理のページは長く持つものとして書く。古くなりやすい数値と名称は facts.yml とバッジに隔離する。撤回された助言は「どの原理の回避策だったか」と一緒に台帳に残す。こうすれば、次に何かが撤回されたときにも、読者は自分で意味を読み取れる。これは、更新できない書籍や、Tips を並べた記事にはできない差別化である。

もう一つの示唆は、学習の順序を「機能を覚える順」から「任せる幅を広げる順」に変えるべきだということである。上の段に進むほど、確かめる仕組みと封じ込めを前提として求める。そうすれば、2026年に表面化した新しい問題に教材として向き合える。それは、承認は減ったがレビューが詰まり、並列化で人が疲れるという、人間側のボトルネックである。この読者に本当に足りないのは新しい機能の知識ではない。症状から原因へ戻る診断の手順と、「どこまで任せてよいか」を自分で決める基準である。逆引きと症状辞典を初版の中心に置き、そこから原理へリンクでたどれるようにすることが、この教材を既存の書籍や記事と分ける最短の道になる。
