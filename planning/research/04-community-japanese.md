# 日本語の実践者コンテンツ調査：Claude / Claude Code の使いこなし（2025〜2026年10月時点）

> 調査メモの前提
> - 調査日：2026-10-29。対象：Zenn、Qiita、note、DevelopersIO（クラスメソッド）、企業テックブログ、Speaker Deck、はてなブックマーク、書籍・講座情報。
> - **人気指標の読み方**：はてブ（users数）は値がはっきりしているので、最も比較に使いやすい。Qiita はページ上に数字が2つあり、ラベルが取れなかったので「いいね／（ストックと推定）」と書いた。Speaker Deck は閲覧数（views）とスター数。Zenn は API とトピックページがこの環境では取得できず、**Zenn のいいね数はほぼ取れていない**（Gaps 参照）。
> - 各項目は「内容／根拠・なぜ効くか／人気・広まり／現在も有効か／出典」の順で書いた。
> - WebSearch の上限に達したため、後半は検索済みの URL を取得して調査した。X（旧Twitter）の投稿は、記事に引用されたものだけを扱っている。

---

## Q1. 人気の日本語記事・スライドのテーマ別カタログ（Claude Code の使いこなし／CLAUDE.md／サブエージェント／スラッシュコマンド／Skills／Hooks／MCP／並列開発／仕様駆動開発／非エンジニアの活用／ドキュメント作成）

### Takeaway
日本語圏で突出して読まれているのは、**(1) 公式ベストプラクティスを日本語で要約したもの（みのるんのスライド 64k views）、(2) 「入門〜中級」を一枚にまとめた総まとめ記事（K5K の Qiita 記事 973いいね、hokuto_tech の Zenn 記事 はてブ835）、(3) 非コーディング業務への応用（みのるんの「日常業務を爆速化」 2,374いいね）** の3系統。テーマ別に見ると、CLAUDE.md・Skills・機能の使い分けを整理する記事は数が多い。一方、Hooks や並列開発は 2025年の個人記事が中心で、人気指標も中くらいにとどまる。

### Cited Findings

#### A. 総合・使いこなし（最も人気）
- **みのるん（@minorun365, KDDIアジャイル開発センター）「Claude Codeですべての日常業務を爆速化しよう！」（Qiita, 2026-03-01／最終更新 2026-09-21）**
  - 内容：AI を「仕事を任せる同僚」として扱い、まず「半自動化」から始める。「プチ仕様駆動開発」として PLAN.md（音声入力で背景を全部吐き出す）、SPEC.md（壁打ちで仕様を固める）、TODO.md（コンテキストが切れても再開できる）、KNOWLEDGE.md（学びやハマりどころの蓄積）の4ファイルを使う。経費精算、稼働報告、Marp でのスライド作成、家計 CSV の処理、Todoist MCP の活用などの実例を挙げ、雑務は業務ごとのディレクトリと README を持つモノレポで管理する。
  - 根拠：情報が少ないと AI は意図しないものを生成するので、音声で大量に入力して整理・構造化を任せる、という考え方。
  - 人気：**2,374いいね／1,858（ストックと推定）**。今回見つけた日本語の Claude Code 記事の中で最大級。Qiita Conference 2026 版のスライドは 20k views・19 stars。
  - 現在：有効（2026年9月に更新済み）。書籍『みのるん式』に発展。
  - 出典：[Qiita](https://qiita.com/minorun365/items/114f53def8cb0db60f47)／[Speaker Deck（Qiita Conference 2026, 2026-05-28）](https://speakerdeck.com/minorun365/claude-codedesubetenori-chang-ye-wu-wobao-su-hua-siyou)
- **みのるん「Claude Codeベストプラクティスまとめ」（Speaker Deck, 2026-01-24）**
  - 内容：公式の best practices（code.claude.com）を日本語の21枚に要約したもの。中心原則は「コンテキストウィンドウ管理」で、7つの実践（検証手段を与える、Explore→Plan→Implement、具体的なコンテキスト、環境設定、効果的な対話、セッション管理、自動化）と、失敗パターンの表（キッチンシンク・セッション、修正の繰り返し、CLAUDE.md の肥大化、検証なしの信頼、際限のない探索）を載せている。
  - 根拠：公式ドキュメントの忠実な翻案。
  - 人気：**64k views・71 stars**。日本語スライドとして非常に多い。
  - 現在：有効（2026年1月時点の公式内容に準拠）。
  - 出典：[Speaker Deck](https://speakerdeck.com/minorun365/claude-codebesutopurakuteisumatome)
- **K5K「【入門記事】ClaudeCodeの中級者になりたい人は集合してください」（Qiita, 2026-03-13）**
  - 内容：設定・調査・Skills の作成まで Claude Code に任せる。AskUserQuestion で曖昧な依頼を明確にする。Plan Mode から始める。`/compact` は使用率50%前後で実行。CLAUDE.md は約200行以内で、育てていく。使わない MCP は外す。Skills の段階的開示。「最初は全部 CLAUDE.md に書き、使う頻度の低いものを後で Skills に移す」。
  - 人気：**973いいね／1,075（ラベル不明）**。
  - 現在：有効。
  - 出典：[Qiita](https://qiita.com/K5K/items/72cc4282819ace823524)
- **hokuto_tech「Claude Code を初めて使う人向けの実践ガイド」（Zenn, 2025年6月頃初出・2025-09-30 に追記）**
  - 内容：コマンド、音声入力、画像やスクリーンショットの活用、こまめな git add、メモリ、権限、ワークフロー、MCP。
  - 人気：**はてブ 835 users**（今回確認した Claude Code 関連エントリーで最多）。トップコメントは Aqua Voice での音声入力。
  - 現在：骨格は有効だが、2025年中頃の UI と機能が前提（下の「陳腐化」参照）。
  - 出典：[はてブ](https://b.hatena.ne.jp/entry/s/zenn.dev/hokuto_tech/articles/86d1edb33da61a)
- **stafes_blog（nano72mkn）「Claude Codeをはじめて触るエンジニアのためのざっくり入門」（Zenn, 2026-05-29）**
  - 内容：まず覚える8コマンド（`/help` `/clear` `/resume` `/init` `/review` `/remote-control` `/mcp` `/btw`）。Shift+Tab でのモード切替、`@` による参照、`!` でのシェル実行、Skills の自作、MCP で GitHub や Notion を1つつなぐこと。Skill や MCP は導入前に中身を確認する。
  - 人気：**はてブ 434 users**（2026年6月）。
  - 現在：有効（2026年の UI に対応）。
  - 出典：[記事](https://zenn.dev/stafes_blog/articles/nano72mkn-claude-code-intro)／[はてブ](https://b.hatena.ne.jp/entry/s/zenn.dev/stafes_blog/articles/nano72mkn-claude-code-intro)
- **wataru86「Claude Code を4ヶ月使ってわかった、おすすめコマンド・スキル 10 選」（Qiita, 2026年6〜7月）**
  - 内容：`/clear` `/resume` `/rewind` `/insights` `/update-config` など。コメントでは grill-me や remote-control も話題に。
  - 人気：**はてブ 384 users**。「claude code の changelog 追ってればわかることだけど、誇張なく良心的な記事」というコメントが付いた。
    > 【2026-11-03 訂正】括弧の中のコメントを原文の言い方に直した（元は「changelog を追っていればわかるが誇張のない良心的な記事」という言い換えで、「と評価された」としていた）。ページに表示された1件のコメントで、読者全体の評価として量で確かめたものではない。research/25 の P3。
  - 出典：[はてブ](https://b.hatena.ne.jp/entry/s/qiita.com/wataru86/items/b859f1578191a1e15808)
- **Oikon（@oikon48）のスライド群（Speaker Deck）**：「Claude Code はじめてガイド -1時間で学べるAI駆動開発の基本と実践-」43k views・55 stars、「Claude Codeの進化と各機能の活かし方」16k・23、「Claude Code 2026年 最新アップデート」14k・17、「Everything Claude Code を眺める」13k・15、「Claude Codeをどのようにキャッチアップしているか」12k・15、「Claude Codeとハーネスについて考えてみる」11k・21、「Claude Codeの体系的な理解と知識のフック」8.9k・10（views と stars の対応はページ表示からの推定）。
  - 根拠：Oikon は書籍『Claude Code実践入門』の共著者で、2025年に Claude Code の流行を整理した記事も書いている。日本で最も参照される解説者の一人と見られる。
  - 出典：[Speaker Deck 一覧](https://speakerdeck.com/oikon48)
- **Oikon「2025年6月にClaude Codeが突然話題になった理由をまとめる」（Zenn, 2025-06-07）**：Claude 4 の性能、Max プラン（2025-05-01）と Pro プラン（2025-06-05）での定額利用、IDE 統合、自律性の4要因を挙げる。**はてブ 325 users**。同じサイトの「Claude Codeアドベントカレンダー: 24 Tipsまとめ」が 233 users、「Claude Codeの全てのCHANGELOGを追ってきて」が 106 users。— [記事](https://zenn.dev/oikon/articles/adac12ea9e839b)／[はてブ](https://b.hatena.ne.jp/entry/s/zenn.dev/oikon/articles/adac12ea9e839b)
- **その他の2025年の人気エントリー（はてブ）**：tonkotsuboy「実務で使っているClaude Codeの活用事例集 - Claude Code Meetup」**293 users**（`/create-pr` カスタムコマンド、Puppeteer・Figma・o3-search の MCP、Hooks、Aqua Voice、Kiro 連携）[はてブ](https://b.hatena.ne.jp/entry/s/tonkotsuboy.github.io/20250717-findy-claudecode/)。carenet「やっぱりClaude Codeしか勝たんかもしれない」**265 users**（「リポジトリを育てる」という表現が支持された）[はてブ](https://b.hatena.ne.jp/entry/s/zenn.dev/carenet/articles/59f62014092a1b)。trysmr「1ヶ月ほぼ毎日Claude Codeを使ってわかった魅力と所感」**239 users**（定額なので失敗を恐れず試行錯誤できる）[はてブ](https://b.hatena.ne.jp/entry/s/zenn.dev/trysmr/articles/one-month-using-claude-code)。
- **2026年後半の人気エントリー**：goat_eat_any「Claude Code クラウドセッション、使ってみて！」**242 users**（2026-09。Claude Code on the Web は 2026-09-24 に正式リリースされ「クラウドセッション」に改称）[はてブ](https://b.hatena.ne.jp/entry/s/zenn.dev/goat_eat_any/articles/claude-code-cloud-sessions)。
- **Zenn チーム（和田祐介, クラスメソッド）「Claude Code でアプリ開発をオートパイロットにするためのTips集 Zennの場合」（2025-09-17）**：CLAUDE.md には実行コマンドを書く、CI/CD は「道路の舗装」、変更は10ファイル未満に小さく切る、`/review-pr` コマンドで事前レビュー、feature flag、rulesync で Cursor とルールを共有、tsumiki。サブエージェント・GitHub の @claude・Figma MCP は「不採用」だった。7k views・8 stars。— [Speaker Deck](https://speakerdeck.com/wadayusuke/claude-code-tips-in-zenn)

#### B. CLAUDE.md の書き方
- **hikariclaude01「CLAUDE.md 設計パターン集──プロジェクト規模別に使い分ける7つのテンプレート」（Qiita, 2026-07-20）**：個人スクリプトなら10〜20行、中規模なら40〜80行、モノレポはルートに共通方針だけを置く。禁止事項を明記し、「関数は30行以内」のように数値で書く。合計500行を超えたら見直す。月1回の棚卸し。**263いいね**。— [Qiita](https://qiita.com/hikariclaude01/items/e54c70c90c6aa84d0f66)
- **Serverworks「CLAUDE.md の書き方ガイド」（2026-05-11）**：約200行以内に収める。リンターで強制される規約は書かない。手順は Skills へ移す。**`@import` は起動時に展開されるのでコンテキストは減らない**。減らしたいなら `.claude/rules/` に分け、`paths` フロントマターで条件付きで読み込ませる。— [Serverworks](https://blog.serverworks.co.jp/claude-code-claudemd-guide)
- **「humanlayerのブログから学ぶ、良いCLAUDE.mdの書き方」（NCDC, Speaker Deck, 2026-01-19）**：WHY/WHAT/HOW を書く。300行未満にする（デフォルトのシステムプロンプトに約50の指示があるため）。段階的開示を使う。エージェントをリンター代わりにしない（Hooks を使う）。`/init` での自動生成は避ける。350 views と小規模だが、海外記事の翻案として典型的。— [Speaker Deck](https://speakerdeck.com/tsukamoto1783/humanlayernoblogkaradu-mijie-kuliang-iclaude-dot-mdnoshu-kifang-no)
- **jyas-protein「CLAUDE.mdの書き方と注意点」（Qiita, 2026-03-30）**：100行程度を推奨。「CLAUDE.md は実質 Session Start Hook である」という見方。AI が生成した CLAUDE.md は無いより精度が下がることがあるという研究を引いて `/init` を避ける。`.claude/rules/` は `@import` より確実に効く。6いいね。— [Qiita](https://qiita.com/jyas-protein/items/9cc733d2ed7f80bef7a1)
- **aipicks「CLAUDE.mdの書き方|7つのルール」（2026-08-13）**：コマンド、機械でチェックされない規約、アーキテクチャの「理由」、**地雷リスト（最も効果が高い）**、検証手順、触ってはいけないファイル、外部ツールを書く。まず100行以内。— [aipicks](https://aipicks.jp/mag/claude-md-guide-2026)
- 行数の目安は記事によって 100／200／300／500 と分かれ、`/init` についても**推奨（公式・みのるん・Serverworks）と非推奨（humanlayer 系・jyas-protein）で対立**している。— 上記各出典、[みのるんのスライド](https://speakerdeck.com/minorun365/claude-codebesutopurakuteisumatome)

#### C. 機能の使い分け（CLAUDE.md／サブエージェント／スラッシュコマンド／Skills／Hooks／MCP）
- **fujisho1216「役割が混在してきたので…改めてまとめてみた」（Qiita, 2026-01-13）**：CLAUDE.md は常時、サブエージェントは独立コンテキスト、スラッシュコマンドは手動、Skills は文脈に応じて自動で発動する。サブエージェントは親の Skills を継承しないので、`skills` フィールドに明示が必要。**90いいね**。— [Qiita](https://qiita.com/fujisho1216/items/90b34ef9abd910deb6ac)
- **frontline「Subagent・Skills・CLAUDE.md、どこに何を書くべきか整理してみた」（Zenn, 2026-03-13）**：全体の規則は CLAUDE.md、役割は Subagent、手順は Skill、機械的に強制したいものは Hook。レビュー役は Subagent に置き、基準は Skill に分ける。— [Zenn](https://zenn.dev/frontline/articles/860e18f65807e3)
- nak1104（Qiita, Advent Calendar 2025 の8日目）：「スラッシュコマンドは何をするか、Skills はどうやるか」。Web 版の Claude はローカルの Skills やローカル MCP を使えない。4いいね。— [Qiita](https://qiita.com/nak1104/items/a0274cd106ea7b6f1771)
- この「使い分け整理」記事は Zenn・Qiita で非常に多い（検索結果の上位に同種が5本以上）。読者が機能の境界に混乱していることがうかがえる。— [Zenn（linkedge）](https://zenn.dev/linkedge/articles/27c38cdd9bedc6)、[Qiita（fujisho1216）](https://qiita.com/fujisho1216/items/90b34ef9abd910deb6ac)

#### D. サブエージェント／Agent Teams
- **@IT「『Claude Codeでトークン浪費』の原因 Anthropicが明かす『サブエージェント』5つの使い所と止め所」（2026-06-04, 2026-04-07 の Anthropic ブログを紹介）**：使い所は、調査、独立タスク、新しい視点でのレビュー、コミット前検証、パイプライン。使わない方がよいのは、逐次依存、同一ファイル、小タスク、専門エージェントの作りすぎ、エージェント間の通信が必要な場合。— [@IT](https://atmarkit.itmedia.co.jp/ait/spv/2606/04/news055.html)
- **クラスメソッド「サブエージェントを増やしすぎていたら、Claude公式が挙げる失敗パターンに当てはまっていた話」（2026-10-26）**：工程ごとに12体まで増やしたら、受け渡しのルール作りに追われた。「工程ではなく、コンテキストが独立しているかで分ける」方針に変え、レビューは6体を2体に統合。承認ゲートは permissions の ask で強制する。— [DevelopersIO](https://dev.classmethod.jp/articles/claude-code-subagent-review/)
- **gihyo.jp 連載「これからはじめるClaude Code入門」第7回 Agent Teams（平川知秀, 2026-03-03）**：v2.1.32（2026-02-05, Opus 4.6 と同時）で実験的に追加。plan mode でトークン約7倍、`/rewind` と `/resume` が使えない、チームメイトには Sonnet/Haiku、Delegate Mode。— [gihyo.jp](https://gihyo.jp/article/2026/02/get-started-claude-code-07)
- **クラスメソッド「Agent Teams 機能を使って…専門家チームを作ってみた」（2026-02-09）**：`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`。Pro プランでもメンバーを増やすとすぐ上限に達する。承認要求が頻繁。— [DevelopersIO](https://dev.classmethod.jp/articles/claude-code-agent-teams-how-to-build/)
- 2025年の前史：tmux で「社長・部長・ワーカー」の組織を作る Claude-Code-Communication（ある個人の Zenn の記事、2025-06。関連する X 投稿は20万インプレッション超）。`--dangerously-skip-permissions` が前提。Agent Teams が公式化した今は**歴史的な位置づけ**。
  > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。

#### E. カスタムスラッシュコマンド → Skills
- **スラッシュコマンドは Skills に統合された**（YouMind による日本語解説, 2026-01-23。元は Thariq（@trq212）の X 投稿で、約560K views・1.8K いいね・2.0K ブックマーク）。`.claude/commands` は引き続き動くが、新規作成は Skill を推奨。`user-invocable` `disable-model-invocation` `context: fork` `agent:` などのフロントマター。— [YouMind](https://youmind.com/ja-JP/landing/x-viral-articles/claude-code-skills-merge)／[mrsekut Scrapbox](https://scrapbox.io/mrsekut-p/%E2%9D%8C%EF%B8%8F.claude%2Fcommands)
- **SIOS「Claude Code Skillsの使い方と汎用テンプレート公開」（2025-12-06）**：「成否は description の書き方で9割決まる」。SKILL.md は500行未満、決定的な処理はスクリプトにする、出所が信頼できる Skill だけ使う。— [SIOS Tech Lab](https://tech-lab.sios.jp/archives/50570)
- **エクスプラザ「Claude Skills (Agent Skills) 入門」（2025-10-21）**：name は64字・description は1024字以内、三人称で書く、参照は1階層まで、100行を超える参照ファイルには目次を付ける。— [Zenn](https://zenn.dev/explaza/articles/b3dde4451aa249)
- NCDC「Claude CodeにAgent Skillsを自作してもらった」（2025-10-18）：公式の `skill-creator` を有効化して頼むだけで作れる。公式 Skills を全部有効にするとコンテキストを浪費する。— [Zenn](https://zenn.dev/ncdc/articles/77b4150bc3148f)
- 2025年の custom commands 記事（例：2025-07 のある個人の記事の `/project:name` `/user:name` 記法）は**記法が古い**。
  > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。

#### F. Hooks
- 通知系の入門が多い：the_exile「Hooks機能で完了通知を受け取りましょう」（2025-07-01, Notification と Stop で macOS の osascript）。— [Zenn](https://zenn.dev/the_exile/articles/claude-code-hooks)
- Stop フックで lint／RuboCop を自動実行（timelab, 2025-08-04）。— [Zenn](https://zenn.dev/timelab/articles/a74b56607e60f9)
- **日本語返答を強制する Hooks プラグイン「japanese-reply」（クラスメソッド, 2026-10-20）**：UserPromptSubmit でリマインド、Stop で英語判定してブロック、MessageDisplay と PreToolUse で途中の英語発話を差し戻す。— [DevelopersIO](https://dev.classmethod.jp/articles/claude-code-hooks-prevent-english-reply/)（Q3 で詳述）
- 書籍・Zenn Book では Hooks に章を割く例が増えている。増山の Zenn Book では46章中10章（29〜38章）が Hooks。— [Zenn Book](https://zenn.dev/tmasuyama1114/books/claude_code_basic)

#### G. MCP
- 2025年は Serena MCP が人気だった（ある個人の Zenn の記事、2025-07。トークン60〜80%削減と主張しているが測定方法は示されていない）。
  > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。
- 2026年は「MCP の入れすぎ」への警告が主流。dai_chi はプロジェクトあたり約10サーバー・合計約80ツールまでを目安にする（2026-01-23）。翻訳記事でも、使わない MCP が起動時からトークンを消費すると注意している。— [Qiita](https://qiita.com/dai_chi/items/63b15050cc1280c45f86)／[ライフハッカー（MakeUseOf の翻訳, 2026-09-03）](https://www.lifehacker.jp/article/2609checked-claude-code-usage-found-four-hidden-token-drains-never-knew-about/)
- naopen（KDDI AD）：Advent Calendar の運営を Chrome DevTools MCP と Playwright MCP で自動化（Playwright はページ全体の取得で約19.2k トークンを消費）。26いいね。— [Qiita](https://qiita.com/naopen/items/31c4221906d60247aa87)

#### H. 並列開発（git worktree／tmux）
- adalocamp「【爆速テク】Claude Code並列処理で生産性1.5倍!Git worktree+カスタムコマンド完全攻略」（2025-07-14）：worktree ごとに `npm install` が必要、`.env` はコピーされない、開発 DB が衝突する、ディスクを食う、という落とし穴。生産性の数値は自己申告。— [Zenn](https://zenn.dev/adalocamp/articles/claude-code-advanced-tips)
- camoneart「Maestro」（2025-08-04）：worktree・tmux・GitHub 連携の CLI。— [Zenn](https://zenn.dev/camoneart/articles/ba1e905aa9d633)／aiya000「git-worktreeへの移行方法」（2025-07-27）— [Zenn](https://zenn.dev/aiya000/articles/cb55bcdc12b137)
- frontendflat（2025-08-31, 2026-02 更新）：ブランチごとに worktree を作り、`/design` `/revise` `/implement` `/review`（並列のサブエージェント）`/recap` のコマンドで流れを作る。プロンプトと成果物は Obsidian に蓄積する。— [Zenn](https://zenn.dev/frontendflat/articles/acc1095edc0d6d)
- 神戸大の学生の発表（2025-07-13, 1.5k views）：worktree での並列化と、Tailscale と Termius でスマホから SSH 操作。— [Speaker Deck](https://speakerdeck.com/yuuuuuuuuu54/claude-codefa-biao)

#### I. 仕様駆動開発（SDD／Kiro 系）
- **cc-sdd（gotalab）**：Kiro の Spec mode に着想を得た SDD ハーネス。**GitHub 3.7k stars**。v3.0 では Agent Skills として提供され、`/kiro-discovery` → requirements（EARS 記法）→ design → tasks → `kiro-impl`（TDD とレビュー）。`--lang ja` を含む14言語に対応。— [GitHub](https://github.com/gotalab/cc-sdd)
- kokushing の cc-sdd 体験記（2025-09-09）：時間とトークンを食う。ゼロから作るより、vibe coding で作ったものを本番品質に固める用途に向く。**導入すると CLAUDE.md が上書きされる**点に注意。— [Zenn](https://zenn.dev/kokushing/articles/7468d5f195e54c)
- **tsumiki（クラスメソッド, 2025年7月末）**：`/kairo-requirements` → design → tasks → implement（TDD）。Pro プランの上限で完走できなかった、設計書が長すぎる、という指摘あり。— [Zenn](https://zenn.dev/uniformnext/articles/tsumiki-claude-code)
- 吉田真吾「達人に学ぶAIコーディング」（2026-01-19）：product.md・requirements.md・design.md・tech.md・structure.md を永続ドキュメントとし、変更のたびにドキュメントを先に更新する。書籍『実践Claude Code入門』の第4章「達人に学ぶスペック駆動開発」と対応する。— [Speaker Deck](https://speakerdeck.com/yoshidashingo/ai-coding-learned-from-master)
- **kazuki_ogawa「文章で要件定義するのをやめた。AIでモックを先に作ったら、認識ズレが実装前に全部見つかった」（Qiita, 2026-10-05）**：高コストな判断だけを先に決め、1枚の HTML モックで認識ずれを洗い出し、要件書はモックの後に書く。最後に成功した手順を Skill 化する。**268いいね／195**。「文章の仕様より先にモックを作る」という SDD への反論・補完として注目された。— [Qiita](https://qiita.com/kazuki_ogawa/items/f1a15a199d9f91fe6080)

#### J. 非エンジニアの活用・業務利用
- みのるんの記事と書籍（上記A）が代表。ほかに Ubie（全職種に配布、営業が HTML 動画を作る、非エンジニアが PR を出す。notty, note, 2026-04-01）— [note](https://note.com/notty0123/n/n89846a4c1b5f)
- 非エンジニアのマーケターが173日使った例（X の @eggAIeguite の投稿、約140万インプレッション。月60万円規模の業務という数字は未検証）— [hashout](https://hashout.jp/ai/9166/)
- crystal-method「非エンジニア向け Claude Code」（2026-06-08, 2026-10-28 更新）：デスクトップアプリの Code タブを使い、権限は「手動」にする。初期状態が auto mode だった。Shift_JIS の CSV で集計が空欄になった。`/init` が英語の CLAUDE.md を生成した。作業用フォルダにはコピーだけを置く。— [crystal-method](https://crystal-method.com/blog/claude-code-non-engineer/)
- LayerX のマーケティング部（池田小百合, 2026-02-05）：Gemini の Gems で作っていた事例記事制作を Claude Code の Skill（examples/templates/SKILL.md）へ移行し、企画からタイトル案まで5段階のワークフローにした。630 views。— [Speaker Deck](https://speakerdeck.com/koyurin/claude-codedetukurushi-li-ji-shi-zhi-zuo-agent)
- Schoo「非エンジニアのためのClaude Code入門」（2026-09-07, 片岡駿人）。— [Schoo](https://schoo.jp/course/9269)

#### K. ドキュメント・記事作成
- izumin「Claude Codeで記事作成」（2025-07-26）：普段から文章生成に Claude Code を使っている。記事レビュー用のサブエージェントを作成。— [Zenn](https://zenn.dev/izumin_0401/articles/claude-codearticlecreation)
- 日本語推敲 Skill の比較（2026-10-01, **342いいね／288**）は Q3 で詳述。— [Qiita](https://qiita.com/inoyu-qiita/items/0ffe6e74ecaf3aaa8b14)
- Marp でのスライド作成は、みのるんの記事、書籍『みのるん式』5章、多数の SEO 系記事で扱われている。— [Qiita（みのるん）](https://qiita.com/minorun365/items/114f53def8cb0db60f47)

### Inferences
- 人気が集中するのは「公式情報の日本語での体系化」と「総まとめ／入門〜中級の地図」。辞書型の教材はこの需要に直接応える。ただし「完全ガイド」と名乗る記事の乱立には読者の反発もある（Q6）。
- **非エンジニアの業務利用（みのるん系）が最大のヒット**であり、「コードを書かない Claude Code」は日本で特に強いテーマと考えられる。
- 2025年の人気テーマ（tmux 組織、Serena、カスタムコマンド記法）は2026年に陳腐化が進んだ。2026年は「入れすぎ・分けすぎへの反省」（MCP やサブエージェントの削減）と「仕組みで強制する（Hooks／permissions／ハーネス）」に関心が移っている。

### Gaps
- Zenn の記事ごとのいいね数は、この環境では API とトピックページにアクセスできず取得できなかった。Zenn の「全期間」ランキング（https://zenn.dev/topics/claudecode）で確認するとよい。
- note の有料記事（チャエンなど）の販売数やスキ数は取得できなかった。
- 企業テックブログ（LayerX、メルカリ、サイバーエージェントの本体ブログ）の個別記事は、許可リストの制限で本文を取得できなかったものが多い。数値は二次まとめ（CodeKnights）経由（Q3）。
  > 【2026-11-03 注記】このうちメルカリのブログの記事（2025-10-28）は research/25 の P11 で確かめた。CodeKnights の数値のうち READYFOR と Rehab for JAPAN の2件は、元の記事を research/25 の P7 で確かめた。

---

## Q2. 繰り返し登場する具体的Tips（Plan mode を先に、日本語か英語か、CLAUDE.md を短く、作業ログ・進捗ファイル、/clear のタイミング、自動テストで検証、別セッションでレビュー など）

### Takeaway
日本語圏でほぼ合意されている Tips は、**「コンテキストは最重要資源」→「Plan を先に」「検証手段（テスト・スクリーンショット・CI）を与える」「CLAUDE.md は短く、守らせたいことは Hooks や permissions で強制」「タスクは小さく、セッションは短く、要点はファイルに外出し」「別のコンテキストでレビュー」** の6つ。数値の目安（CLAUDE.md の行数、compact する閾値）は記事ごとにばらつく。

### Cited Findings
- **Plan mode を先に**
  - 内容：Explore → Plan → Implement → Commit。手作業なら5分以上かかるタスクは計画を先に作らせる（nogataka）。Boris Cherny（Claude Code の開発者）もほぼ常に Plan mode から始めると Oikon に答えた。
  - 根拠：意図と実装のずれを先に潰すと手戻りとレビュー負荷が減る（Oikon の振り返り）。
  - 人気・現在：ほぼすべての入門記事と書籍に載っている。有効。
  - 出典：[みのるんのスライド](https://speakerdeck.com/minorun365/claude-codebesutopurakuteisumatome)／[nogataka（157いいね）](https://qiita.com/nogataka/items/392934f79e943e8b9228)／[Oikon 2025 振り返り](https://github.com/oikon48/zenn-contents/blob/main/articles/claude-code-2025.md)／[takezaki（2025-07）](https://speakerdeck.com/74k3z4k1/si-no-claude-code-noshi-ifang-toshi-shi-henoinpakuto)
- **検証手段を与える（テスト・スクショ・CI）＝最も効果が高い**
  - 内容：期待する入出力を示してテストを実行させる。UI はスクリーンショットで比較させる。Zenn チームは CI/CD を「道路の舗装」と呼ぶ。テストを人が直して意図を示す方が、口頭で説明するより効く（takezaki）。
  - 根拠：エージェントが自分で正誤を判定できると自律的にループを回せる。
  - 現在：有効。2026年には「ハーネスエンジニアリング」として理論化された。クラスメソッドの「同じ注意を2回したら、それは仕組みに落とすタイミング」（DevelopersIO 2026, 2026-10-24）。
  - 出典：[みのるんのスライド](https://speakerdeck.com/minorun365/claude-codebesutopurakuteisumatome)／[Zenn チーム](https://speakerdeck.com/wadayusuke/claude-code-tips-in-zenn)／[クラスメソッドのハーネス講演](https://dev.classmethod.jp/articles/lt-devio2026-tokyo-harness-engineering/)／[kobori：AI開発手法まとめ（2026-10-20）](https://qiita.com/kobori_slj/items/b9683ce90f4c26a6e7ae)
- **CLAUDE.md は短く、強制したいことは Hooks／permissions へ**
  - 内容：目安は 100行（jyas-protein, aipicks）、200行（Serverworks, K5K, seabat）、300行（humanlayer 系）、合計500行で見直し（hikariclaude01）。「削除したら Claude がミスするか？」と自問する。
  - 根拠：指示が多いほど遵守率が下がる。CLAUDE.md は「お願い」であって強制力がない。choplin（2025-06）は「常に日本語で」すら守られない例を報告している。
  - 現在：有効。2026年は `.claude/rules/` の `paths` による条件読み込みや Skills への移動が標準的な処方になった。
  - 出典：[Serverworks](https://blog.serverworks.co.jp/claude-code-claudemd-guide)／[seabat（IMPORTANT／YOU MUST で遵守率が上がるという主張も）](https://qiita.com/seabat-dev/items/27cb2e1dbd1e9bc1e4b8)／[choplin](https://zenn.dev/choplin/articles/2025-06-24-claude-code-1-reality-and-mindset)／[ai-orchestra（Hooks／permissions で強制）](https://www.ai-orchestra.ai/claude-code-training/columns/claude-code-security)／[dai_chi（SessionStart フックで環境を決定的に）](https://qiita.com/dai_chi/items/63b15050cc1280c45f86)
  - 対立点：一方で「禁止事項に忠実に従う傾向がある」（hikariclaude01）、「IMPORTANT で遵守率が上がる」（seabat）という主張もあり、どれだけ守られるかの評価は分かれている。いずれも測定データはない。
- **作業ログ・進捗ファイル・引き継ぎ**
  - 内容：PLAN/SPEC/TODO/KNOWLEDGE.md（みのるん）。`/session-save` で作業内容と次の一手を書き出してから `/clear`（クラスメソッド, 2026-10-14）。compact する前に「なぜそうしたか」を CLAUDE.md、コミット、設計書に移す（crystal-method）。中間成果物はファイルに保存して次のフェーズへ渡す（dai_chi）。雑務モノレポでは、ハマった点を README に追記する（みのるん）。
  - 根拠：compact の要約では細部が消える。ファイルにあればコンテキストが切れても再開できる。
  - 現在：有効。
  - 出典：[みのるん](https://qiita.com/minorun365/items/114f53def8cb0db60f47)／[クラスメソッド「セッションを長くしすぎないために入れた工夫3つ」](https://dev.classmethod.jp/articles/claude-code-keep-sessions-short/)／[crystal-method](https://crystal-method.com/blog/claude-code-compact-clear/)
- **/clear と /compact のタイミング**
  - 内容：無関係のタスクに移るときは `/clear`。同じ修正を2回以上したら `/clear` して具体的なプロンプトでやり直す（みのるん／公式）。compact の目安は使用率50%（K5K）、約150kトークン（dai_chi）、200k超で通知（クラスメソッド）。1M コンテキストのモデルでは自動 compact が遅いので `CLAUDE_CODE_AUTO_COMPACT_WINDOW=500000` を設定する（クラスメソッド）。キャッシュが切れる前、つまり長時間離席する前にもセッションを畳む。
  - 現在：有効。ただし「200k コンテキスト」を前提にした2025年の記事（2025-09 のある個人の記事など）は 1M コンテキストの時代とずれている。
  - 出典：[K5K](https://qiita.com/K5K/items/72cc4282819ace823524)／[クラスメソッド](https://dev.classmethod.jp/articles/claude-code-keep-sessions-short/)
  > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。
- **別セッション・別コンテキストでレビュー**
  - 内容：Writer/Reviewer パターン（みのるん、公式由来）。実装の文脈を持たない新しいセッションで「ブラックボックスレビュー」をすると、虚偽の完了報告が見つかる（choplin）。サブエージェントの「新しい視点」「コミット前検証」（Anthropic, @IT 経由）。Zenn チームの `/review-pr`。
  - 根拠：実装したセッションは自分の前提に引きずられる。Claude は未完成でも「完了」と報告することがある（choplin：TODO のまま、スキップしたテストで「通過」と報告）。
  - 現在：有効。
  - 出典：[choplin](https://zenn.dev/choplin/articles/2025-06-24-claude-code-1-reality-and-mindset)／[@IT](https://atmarkit.itmedia.co.jp/ait/spv/2606/04/news055.html)／[Zenn チーム](https://speakerdeck.com/wadayusuke/claude-code-tips-in-zenn)
- **タスクを小さく切る**：10ファイル未満、1機能10PR未満（Zenn チーム）。単一目的のステップに分ける（dai_chi）。長い要件書は分割のサイン（kazuki_ogawa）。— [Zenn チーム](https://speakerdeck.com/wadayusuke/claude-code-tips-in-zenn)／[kazuki_ogawa](https://qiita.com/kazuki_ogawa/items/f1a15a199d9f91fe6080)
- **音声入力**：Aqua Voice が繰り返し推奨されている（はてブ 835 の記事のトップコメント、みのるん、tonkotsuboy）。CLAUDE.md に「音声入力である」と書いておく工夫もある。書籍『みのるん式』4.2「音声入力で自己紹介し、仕事の文脈を渡す」。— [はてブ](https://b.hatena.ne.jp/entry/s/zenn.dev/hokuto_tech/articles/86d1edb33da61a)／[みのるん](https://qiita.com/minorun365/items/114f53def8cb0db60f47)
- **AI に指示を守らせる原則（2026年の総括）**：songchong（2026-10-18, 42いいね）。①毎回守らせたい指示は AGENTS.md に書き、CLAUDE.md には `@AGENTS.md` の1行だけを置く。②指示は資料の途中に書かず先頭か末尾に置く。③指示は少なく明確に。④指示ファイルの先頭を変えない（日時などを書くとプロンプトキャッシュが外れて料金が増える）。⑤長くなったら要点をまとめて新しい会話にする。⑥長い資料はファイルに、専門手順は SKILL にする。— [Qiita](https://qiita.com/songchong/items/351a939e2e1b673c2929)
- **コミット単位で戻せるように進める**：プロンプトごとにコミットして `git reset` で戻せるようにする。difit でコミットごとにレビューする（frontendflat）。— [Zenn](https://zenn.dev/frontendflat/articles/acc1095edc0d6d)
- **「Tips より方向性を学べ」**：Claude Code は変化が速く、v1.0.0（5/23）から v1.0.68（8/5）まで2か月半で68版。細かいカスタマイズや Tips はすぐ古くなる（Oikon, 2025-08-05）。— [Speaker Deck](https://speakerdeck.com/oikon48/claude-codekarawo-gaxue-bubekikoto)

### Inferences
- 「CLAUDE.md は強制力のないお願い → 仕組み（Hooks／permissions／テスト）で強制」という転換は、2025年の choplin から2026年のクラスメソッドまで一貫して深まった、日本語圏の中心的な学びと言える。辞書の項目として「お願いと強制の境界」を独立させる価値がある。
- 数値の目安（行数、compact の閾値）は根拠のない経験則が大半なので、教材では「公式の推奨値」と「実践者の幅」を分けて示すのが妥当。

### Gaps
- 「日本語で指示するか英語か」で精度が変わるかについて、日本語の比較実験記事は見つからなかった（Q3）。
  > 【2026-11-03 注記】公式の多言語の評価（旧い世代のモデルの知識問題）があることは research/27 の #12 で確かめた（Q3 の Gaps の注記を参照）。
- 進捗ファイル運用の効果（再開率や品質）を測定した記事は見つからなかった。

---

## Q3. 日本特有の関心事（日本語・文体・表記ゆれ・textlint／社内導入・セキュリティ・情報漏洩／料金（円換算・Max）／企業ガイドライン事例）

### Takeaway
日本特有の論点は大きく5つ。①**返答が英語に戻る問題**（2026年の Opus 5.5 で再燃し、Hooks で強制する解決策が登場）。②**日本語か英語か**（「日本語で問題ない」が多数派だが測定データはない）。③**文体・表記ゆれ・「AI臭さ」**（textlint と Hooks の連携、2026年10月に日本語推敲 Skill がバズ）。④**社内導入ガバナンス**（MDM による managed settings、LiteLLM ゲートウェイ、OTel での監査ログ、Team と Enterprise の選択）。⑤**ドル建て料金**（$1=158円で Max20x は約31,600円、2026-04-01 から消費税10%、インボイス登録番号あり）。

> 【2026-11-03 注記】⑤の「Max20x」は 2026-10-29 より後に変わった。2026-10-30 に旧 Max 20x は Ultra（月 $200）に改名され、Max は月 $100 の1段になった（research/22 の #32）。

### Cited Findings

#### 日本語での返答・日本語か英語か
- **返答言語の設定**：`~/.claude/settings.json` に `"language": "japanese"` を書くか `/config` で設定する。効かないときは JSON の誤り、上位スコープ、CLAUDE.md 内の英語指示を確認する（GiftX, 2026-09-03）。値はチェックされないので綴りを間違えてもエラーにならない（SSD Nodes, 2026-10-02）。— [GiftX](https://ai.giftx.co.jp/blog/claude-code-japanese/)／[SSD Nodes](https://www.ssdnodes.com/learn/lang/ja/claude-in-japanese-app-language-and-limits)
  > 【2026-11-03 注記】効かないときに確かめる3つのうち、上位のスコープ（設定の優先順）は公式の文書で確かめられたが、JSON の誤りと CLAUDE.md の中の英語の指示は、公式の文書に診断の手順として書かれておらず、一次資料で確かめられなかった（research/27 の #6）。
- **`language` はコメントやコミットメッセージには効かない**。これらは CLAUDE.md に「コミットメッセージは日本語で」と書く。`language` を共有のプロジェクト設定に入れると個人の設定を上書きしてしまう。OSS では日本語のルールを `CLAUDE.local.md` か `~/.claude/CLAUDE.md` に置く（Issoh, 2026-10-22, v2.1.308 で確認）。— [Issoh](https://www.issoh.co.jp/tech/details/18753/)
  > 【2026-11-03 注記】「`language` はコメントやコミットメッセージには効かない」は一次資料で確かめられなかった。公式の文書には、`language` がコミットメッセージ・コードのコメント・圧縮の要約・思考の要約に効くかの記述がなく、Issoh の記事は 2026-11-03 に HTTP 403 で読めなかった（research/27 の #4）。
- **Opus 5.5 は英語の返答に戻りやすい → Hooks で強制（クラスメソッド, 2026-10-20）**
  - 内容：英語のツール出力やサブエージェントの報告を読んだ後に英語へ戻る。CLAUDE.md やメモリでの指示は一時的にしか効かない。UserPromptSubmit・Stop・MessageDisplay と PreToolUse の3層で日本語を強制し、プラグイン `japanese-reply` として公開。
  - 根拠：「お願い」ではなく「決定的な制御」。
  - 現在：最新（v2.1.280 と Opus 5.5 で検証）。翻訳出力までブロックされる副作用がある。
  - 出典：[DevelopersIO](https://dev.classmethod.jp/articles/claude-code-hooks-prevent-english-reply/)
  - 前史：2025-06 の choplin が「常に日本語で」という CLAUDE.md の指示を無視される例を報告。— [Zenn](https://zenn.dev/choplin/articles/2025-06-24-claude-code-1-reality-and-mindset)
- **日本語で書いても精度は落ちない（経験則）**：入江慎吾は「日本語で書いても精度が落ちる実感がありません」と述べる。言語より構造（`##` 見出し、1行1ルール）が重要で、英語にするのは技術用語・コマンド・パスだけ（2026-04-07）。AI Orchestra も「英語で書いたほうが精度が上がる、ということは基本的にない」とするが、根拠はなく自社研修の宣伝を兼ねる（2026-07-22）。一方、仁頼は「プログラミング関連の質問は英語の方が精度が高い場合がある」とする（2026-03-26）。jyas-protein は「内部では英語で推論し、最終回答を日本語に訳させる」CLAUDE.md の例を紹介している。— [入江](https://devtools.shingoirie.com/blog/claude-code-japanese-claude-md-guide/)／[AI Orchestra](https://www.ai-orchestra.ai/claude-code-training/columns/claude-code-nihongo)／[仁頼](https://jinrai.co.jp/blog/claude-japanese/)／[jyas-protein](https://qiita.com/jyas-protein/items/9cc733d2ed7f80bef7a1)
- **日本語のトークン消費**：英語に対する固定の倍率はなく、Anthropic は言語ごとの換算率を公表していない（2026年10月時点）。Opus 4.7 以降の新しいトークナイザーでは、同じ文章で以前より約30%多くなる。測定には `/v1/messages/count_tokens` を使う（SSD Nodes）。Issoh も公式の比較データはないとし、言語を変えるより長いログを渡さない・セッションを分けるほうが効くとする。— [SSD Nodes](https://www.ssdnodes.com/learn/lang/ja/claude-in-japanese-app-language-and-limits)／[Issoh](https://www.issoh.co.jp/tech/details/18753/)
- **日本語の思考キーワード（陳腐化に注意）**：2025-07 の Oikon の Gist では、Claude Code が「熟考」「深く考えて」（31,999トークン）、「よく考えて」（10,000）、「考えて」（4,000）を ultrathink 系と同じく判定していた。逆コンパイルした解析で非公式。2026年には `/effort` 設定（Opus 5.5 の既定は medium、v2.1.280 以降）が主流で、キーワード方式が今も有効かは未確認。— [Gist](https://gist.github.com/oikon48/980b89462904aa1980c5d188b30d1f54)／[ai-revolution](https://ai-revolution.co.jp/media/claude-code-quality-postmortem/)
  > 【2026-11-03 注記】英語以外の言語で thinking を起動できるようにしたことが CHANGELOG の 1.0.8（2025-06-02）にあり、当時は公式の機能だったことは research/27 の #18 で確かめた。今もキーワードが効くかは確かめていない。

#### 文体（です・ます／だ・である）・表記ゆれ・textlint・「AI臭さ」
- **textlint と PostToolUse フックの連携（藤澤勇樹, Zenn, 2025-07-26）**
  - 内容：`Write|Edit|MultiEdit` の後に `textlint --fix` と `markdownlint-cli2 --fix` を実行する。エラーが残れば exit 2 で Claude に差し戻して直させる。ルールは `textlint-rule-preset-japanese`、`no-mix-dearu-desumasu`（本文はです・ます、箇条書きはである）、1文150字まで、読点の数、連続する漢字、助詞の重複、`prh` での技術用語の統一、全角と半角の混在など。
  - 根拠：文体の統一は LLM への「お願い」では揺れるので、決定的なリンターで強制する（Q2 の「仕組みで強制」と同じ考え方）。
  - 人気：いいね数は不明。同種の記事は少数。
  - 現在：有効（Hooks の仕様は基本的に同じ）。
  - 出典：[Zenn](https://zenn.dev/yuki_fujisawa/articles/a01e472dc190cf)
- クラスメソッドは社内ナレッジ（CCG）で以前から textlint を CI 必須にしている（2023-08）。AI 以前からの日本の技術文書文化が、AI 時代の Hooks 連携の土台になっている。— [DevelopersIO](https://dev.classmethod.jp/articles/ccg-writing-guide-textlint/)
- **日本語推敲 Skill がバズ（2026年10月）**：inoyu-qiita「新しい日本語推敲スキル『yomiyasu』がバズっていたので、Claudeで日本語推敲スキル3つを比べてみた」（2026-10-01, **342いいね／288**。2026年10月の Qiita claudecode タグで上位）。
  - yomiyasu（nanaism, @oga_aiichiro が X で紹介）：文の構造を書き換え、lint スクリプト付き。です・ます体を維持。
  - natural-japanese（coji）：設計→執筆→検査→収束のワークフロー。見出しや段落を大きく再編。
  - japanese-tech-writing（ある個人の gist）：比喩や太字を削除。**です・ますを指示したのに、である体に変えてしまった**。
    > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。
  - 結論：文体を維持したいなら yomiyasu、再構成なら natural-japanese、論理重視の技術文書なら japanese-tech-writing。ただし1回の出力だけでの比較。
  - 出典：[Qiita](https://qiita.com/inoyu-qiita/items/0ffe6e74ecaf3aaa8b14)
- **表記ゆれと漢字の開き**（仁頼, 2026-03-26／2026-10-05 更新）：「サーバー／サーバ」のゆれ。対策は表記ルールを明記するか、Projects のカスタム指示に登録すること。Claude は漢字の比率が高くなりがちなので、開くルールを指示する。Few-shot で自分の文章を見せる。です・ます調を明示しないと途中で揺れる。— [仁頼](https://jinrai.co.jp/blog/claude-japanese/)
- 書籍『みのるん式』10.2「AIテキストにありがちな『生成AI臭さ』を消す」が独立した節になっている。「AI臭さ」が日本語圏の関心事だとわかる。— [丸善ジュンク堂の目次](https://www.maruzenjunkudo.co.jp/products/9784297159399)
- 文字コード：Shift_JIS の CSV を集計したら空欄になった（非エンジニア向けの検証）。`/init` が英語の CLAUDE.md を生成した。— [crystal-method](https://crystal-method.com/blog/claude-code-non-engineer/)

#### 社内導入・セキュリティ・情報漏洩対策
- **メルカリ（@IT, 2026-08）**
  - 内容：2026年5月から Claude Code と Claude Cowork を全社展開。非エンジニア1,000人以上を対象に「AI Agent Day」を開催。Jamf（MDM）と Okta を同期し、エンジニアと非エンジニアで別の設定を配布する（Claude Enterprise 単体では全員に同じ設定しか配れない）。非エンジニアは通常ローカル管理者権限なしで、Slack コマンドで一時的な管理者権限を申請すると自動で失効する。すべての AI 利用を LiteLLM ゲートウェイ（GKE 上、短命の API キー）経由にして FinOps を可視化する。
  - 補足：メルカリが設定で `--dangerously-skip-permissions` を禁じているか、非エンジニアの作業時間が減ったか（減ったならどれだけか）は、メルカリの一次資料では確かめられない（@IT のインタビューの読める範囲には出てこない）。どちらも別のまとめ記事にだけある記述である。
    > 【2026-11-03 訂正】元の文は、まとめ記事を出典に、メルカリが `bypassPermissionsDisabled: true` で `--dangerously-skip-permissions` を禁じ、非エンジニア1人あたり月10〜15時間を減らしたと読めたので、断定を外した。この設定と時間はあるまとめ記事（2026-07）にだけあり、BinxAI も削減時間は公開情報から判断できないとしている。`bypassPermissionsDisabled` は公式の文書にも CHANGELOG にもない。bypass permissions を使えなくする公式の設定は、`permissions.disableBypassPermissionsMode` を `"disable"` にするもの（Claude Code の Permissions・Permission modes の文書、2.1.317、2026-11-03 確認）。research/25 の P6。
  - 出典：[@IT](https://atmarkit.itmedia.co.jp/ait/spv/2608/04/news002.html)／[BinxAI](https://binxai.co.jp/blog/mercari-claude-code-company-wide-rollout)
    > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。確かめられない記述の出どころとして挙げたまとめ記事の、書き手の名前と URL を外した。
- **5社まとめ（yukibjj）**：ZOZO は Atlassian MCP を `READ_ONLY_MODE: true` にして社内ガイドラインをチェック。GMO デザインワンはまず横展開し、運用設計は後から詰めた。Gemcook の教訓は「個人に選ばせた期間が標準化を遅らせた」。共通軸は「配布範囲」「自動実行をどこまで許すか」「コンテキスト配布の構造化（CLAUDE.md／MCP／Plugin／Skills）」。— [Zenn](https://zenn.dev/yukibjj/articles/claude-code-enterprise-rollout-5-companies-2026)
- **Ubie**：全職種に配布。生成AI利用ポリシーと Claude Code 固有のガイドラインを**ゲーミフィケーション型の研修**で教え、ガードレールで個人の注意力に頼らない設計にした。— [note](https://note.com/notty0123/n/n89846a4c1b5f)
- **日本企業の導入事例一覧（CodeKnights, 2026-07-31）**：日立（約29万人が対象）、富士通（約10万人）、NEC（国内初のグローバルパートナー、約3万人）、KDDI アジャイル開発センター（全職種）、サイバーエージェント（約2,000人が利用）、サイボウズ（2025年は全社プランを見送り、2026年から Team Plan を全社展開）、freee（リクエストの約80%が Claude Code）、マネーフォワード（API 実装が2日→5時間）、楽天（24営業日→5営業日）、LINEヤフーコミュニケーションズ（導入率92%）、DeNA（PR あたりのレビュー回数 7.2→2.7）、PLAID（月間PR 約150→約600）。課題を公開した例として、Rehab for JAPAN はマネージャー層のマージまでの時間が93.5%増、READYFOR は42%が疲労感の増加を報告。数値は各社の自己申告。— [CodeKnights](https://www.codeknights.co.jp/contents/claude-japan-cases-2026summer)
- **クラスメソッドのチーム運用（佐藤智樹, BuriKaigi 2026, 2026-01-09）**：STRIDE で脅威を整理。`.mcp.json` のキーは環境変数にする。DevContainer のファイアウォール、`.env` への読み取り拒否、deny ルール、main への直接 push 禁止。5.6k views。— [Speaker Deck](https://speakerdeck.com/tomoki10/team-claude-code-practices)
- **監査ログ**：Team プランで managed settings を配布し、Claude Code の OpenTelemetry ログを CloudWatch Logs に直接送る（2026-10-26）。プロンプト本文やコマンドは opt-in。claude.ai のチャットと Cowork は対象外。未管理の端末では回避できるので MDM の併用を推奨。— [DevelopersIO](https://dev.classmethod.jp/articles/claude-code-otel-cloudwatch-logs/)
- **Bedrock 経由の統制**：claude.ai の管理コンソールが使えないため、設定の配布方法を別に考える必要がある（2026-10-24 の登壇報告）。— [DevelopersIO](https://dev.classmethod.jp/articles/claude-code-bedrock-governance-tips/)
- **セキュリティガイド（StartLink, 2026-03-10／2026-10-11 更新）**：Team は5〜20人で SSO や監査ログが不要な場合、Enterprise は20人以上で SSO・SCIM・監査ログ API・ZDR・managed-settings の強制が必要な場合。推奨する deny 例は `rm -rf`、`git push --force`、`curl * | bash`、`env`／`printenv`。CVE-2026-21852 と CVE-2025-59536 に言及。— [StartLink](https://start-link.jp/hubspot-ai/ai/claude-code-practice/claude-code-enterprise-security)
- **AI Orchestra の5つのリスク**（社外送信、意図しない操作、秘密情報の漏洩、誤公開、野良利用）と、「CLAUDE.md はお願いにすぎない → permissions や Hooks で機械的に統制」（2026-07-03）。— [AI Orchestra](https://www.ai-orchestra.ai/claude-code-training/columns/claude-code-security)
- 書籍『みのるん式』第11章「企業における『セキュリティの壁』の乗り越え方」：禁止するのではなく安全に使える道を作る。セキュリティ部門と協力する。低リスクの半自動化から始める。外から仕込まれる罠と人間の慣れに備える。— [丸善ジュンク堂](https://www.maruzenjunkudo.co.jp/products/9784297159399)

#### 料金（円換算・Max）・利用制限
- **円換算（Zenken, 2026-10-15, $1=158円）**：Pro $20（約3,160円、年払いなら月約2,690円）、Max 5x $100（約15,800円）、Max 20x $200（約31,600円）、Team Standard $25/席、Team Premium $125/席、Enterprise は $20/席＋従量課金（20席以上・年払い）。Anthropic は適格請求書発行事業者（T7700150134388）。支払いはクレジットカードのみ。部署で個人アカウントを共有するのは非推奨。— [Zenken](https://ai.zenken.co.jp/post/claude-code-pricing/)
  > 【2026-11-03 注記】「Max 5x」「Max 20x」は 2026-10-29 より後に変わった。2026-10-30 に旧 Max 20x は Ultra（月 $200）に改名され、Max は月 $100 の1段になった（research/22 の #32）。
- 2026-04-01 から日本からの利用に消費税10%が加算。— [SSD Nodes](https://www.ssdnodes.com/learn/lang/ja/claude-in-japanese-app-language-and-limits)
- **利用制限の歴史**：週次上限を2025-08-28 から導入（「影響は5%未満」）。$200 プランで数万ドル分を使うユーザーがいた、アカウントの共有や転売があった、が理由。— [PC Watch](https://pc.watch.impress.co.jp/docs/news/2034998.html)／ユーザーの不満（上限に達するとロックアウトが長い、残量が見えない、実質値上げ）— [fleagne（Zenn）](https://zenn.dev/fleagne/articles/4eb2a7aef1acf9)。2026-05-13〜09-13 は週次上限を50%増やすプロモーション。— [Claude ヘルプセンター](https://support.claude.com/ja/articles/15910845-claude-code-2026年5月-7月-週間利用制限プロモーション)。5時間上限は2026年5月に約2倍になり、9月にもさらに引き上げ。— [Zenken](https://ai.zenken.co.jp/post/claude-code-pricing/)
- **2026年3〜4月の品質低下とポストモーテム**：既定の effort を high から medium に下げた、thinking 履歴のバグ（キャッシュミスで上限を早く消費）、冗長さを制限するシステムプロンプト、の3件。2026-04-23 に全ユーザーの利用上限をリセット。— [GIGAZINE](https://gigazine.net/news/20260424-anthropic-claude-code-quality)／ユーザー向けの教訓（`/effort` を確認、モデルを切り替えたら effort を設定し直す、stable チャネル、`/feedback`）— [ai-revolution](https://ai-revolution.co.jp/media/claude-code-quality-postmortem/)
- 月額への心理的抵抗：2025-02 の API 時代には「費用怖くて使えない」（npaka の記事へのはてブコメント）。定額化後も「月3万円」を払うかの議論があった（trysmr の記事へのコメント）。— [はてブ（npaka）](https://b.hatena.ne.jp/entry/s/note.com/npaka/n/n3d754c78f439)／[はてブ（trysmr）](https://b.hatena.ne.jp/entry/s/zenn.dev/trysmr/articles/one-month-using-claude-code)

### Inferences
- 日本語での利用の核心は、「日本語で書いて精度が落ちるか」よりも、**「日本語で返し続けさせる」「日本語の文体を揃える」「日本語の文書品質（AI臭さ）を上げる」** という出力品質の側にある。これらは Hooks・textlint・推敲 Skill といった「仕組み」で解く方向に進んでいる。辞書の重点項目にすべき。
- 社内導入では、海外の記事より「MDM での配布」「管理者権限なしの端末」「LiteLLM ゲートウェイ」「Bedrock／Vertex 経由」など、**日本の情報システム部門の制約に合わせた構成**が多く語られている。
- 料金は「ドル建て、為替、消費税、インボイス、クレカのみ」の組み合わせが日本特有で、経費処理の Q&A に需要がある。

### Gaps
- 日本語と英語のプロンプトで精度やトークン量を比べた実測記事は見つからなかった（SSD Nodes と Issoh も公式データはないと明言）。
  > 【2026-11-03 注記】精度についての「公式データはない」は一部誤り。公式の多言語の評価があり、MMLU を専門の翻訳者が14言語に訳した問題で、英語を100%とした日本語の成績は Claude Sonnet 4.5（廃止済み）が96.8%、Claude Haiku 4.5 が93.5%（extended thinking あり）である。ただし旧い世代のモデルの知識問題で、指示の守り方やエージェントの作業を比べたものではない（エージェントの作業で日本語と英語の指示を比べたデータがないのは正しい）。Takeaway ②の「測定データはない」も同じ。research/27 の #12。
- 「文体（です・ます）を守らせる」ことに特化して、CLAUDE.md・Skill・Hook の効果を比べた記事は見つからなかった。
- 公的機関や業界団体による Claude Code 固有の日本語ガイドラインは見つからなかった（企業ブログや個社の事例のみ）。
- teratail の Q&A は検索で1件も出てこなかった。日本語の Q&A は X・はてブのコメント・Zenn のコメントに分散していると推測される。

---

## Q4. claude.ai（Projects、Artifacts、Research、メモリ）の使い方は日本語でどう語られているか

### Takeaway
claude.ai のアプリ機能を扱う日本語記事は、**AI メディアやコンサル企業の SEO 記事（仁頼、マネーフォワード、GiftX、WEEL など）が中心**で、エンジニアコミュニティ（Zenn／Qiita／はてブ）で人気になった例はほとんど見つからなかった。話題の中心は Projects（業務ごとのカスタム指示とナレッジ）とメモリ（2026年8月にチャットと Cowork で統合）。Artifacts や Research の深い使い方を書いた記事は乏しい。

### Cited Findings
- **Projects（仁頼, 2026-04-03／2026-10-05 更新）**
  - 内容：カスタム指示（全チャットに適用）とナレッジ（ファイル）の2つで構成。最初は3〜5ファイルにし、古い版は削除。1プロジェクト1目的。指示には「いい感じに」ではなく数値や形式を書く。業務パターンとしてビジネスメール、議事録、SEO 記事、社内 FAQ、契約レビュー（最終判断は法務担当者）。
  - 根拠：目的を混ぜると指示とナレッジが衝突する。
  - 人気：不明（企業ブログ）。
  - 出典：[仁頼](https://jinrai.co.jp/blog/claude-projects-guide/)
- マネーフォワード「Projects 活用」（2026-03-04／04-28 更新）：社内 FAQ、論文の比較、契約の一次チェック、ハウススタイルに沿ったブログ、章ごとの長文執筆、議事録。Artifacts・Research・メモリは扱っていない。— [マネーフォワード クラウド](https://biz.moneyforward.com/ai/basic/4463/)
- **メモリ（GiftX, 2026-08-26）**：トピック単位で保存。チャット検索とメモリの使い分け。プロジェクト単位でメモリを分離。シークレットチャットはメモリに残らない。Pause と Reset の違い。会話を削除しても抽出済みのメモリは残ることがある。Free・Pro・Max は既定でオン、Team・Enterprise は既定でオフ。パスワードや未公開の機密は保存しない。— [GiftX](https://ai.giftx.co.jp/blog/claude-memory-guide/)
- **チャットと Cowork のメモリ統合（2026-08-26 発表）**：会話中にリアルタイムでトピックを保存。「覚えておいて」と明示すると確実。健康などのセンシティブ情報は opt-in。— [WEEL](https://weel.co.jp/?p=123538)
- Cowork はチャットに統合されたと報告されている（2026-09-16）。Code と Cowork の使い分けは「Cowork から始め、繰り返す作業になったら Code へ」。— [fyve](https://fyve.co.jp/claude-code/articles/claude-code-vs-cowork-guide)
- **カスタム指示の書き方（ギズモード・ジャパン, 2026-07-25, 日本語のオリジナル記事）**：短く全体方針だけを書く。得意分野と不得意分野で説明の深さを変えさせる。言語ルール。口調（関西弁やずんだもん風も可）。— [ギズモード](https://www.gizmodo.jp/article/how_to_write_claude_instruction/)
- Artifacts と Research への言及は、souzoh（2026-07-22）に「Artifacts でチェックリストや簡易計算ツール、Research で詳細なレポート」と1行ずつある程度。— [souzoh](https://media.souzoh-official.com/claude-tsukaikata)。claudekedai「Claude使いこなし術15選」（Zenn, 2026-03-15）も Projects と Artifacts を各1項目扱うだけ。— [Zenn](https://zenn.dev/claudekedai/articles/20260314-2026314claude1510)
- 「Gemini の Gems → Claude Code の Skills」への移行事例（LayerX のマーケティング部）。Gems の弱点（プロンプトが見つけにくい、文字数制限、履歴が不明瞭、共有しにくい）を Skills のファイル管理で解決した。claude.ai の Projects ではなく Claude Code を選んだ点が示唆的。— [Speaker Deck](https://speakerdeck.com/koyurin/claude-codedetukurushi-li-ji-shi-zhi-zuo-agent)
- 書籍『Claude Codeで学ぶ Agent Skills入門』1.4.2 は「Claude Projects」と Skills の違いを扱っている。— [技術評論社](https://gihyo.jp/book/2026/978-4-297-15698-5)

### Inferences
- 日本の上級ユーザー層の関心は claude.ai から Claude Code・Cowork・Skills に移っており、**claude.ai の機能（とくに Research と Artifacts）を深く使う日本語の実践知は空白に近い**。辞書で「Projects と Skills と Claude Code の使い分け」「メモリの範囲（チャット／Cowork／プロジェクト／Incognito）」を整理すれば差別化できる。
- 企業の SEO 記事は機能紹介が中心で、「なぜ効くか」や失敗例が少ない。

### Gaps
- Research 機能の日本語での使いこなし（日本語ソースの扱い、引用の質）を検証した実践記事は見つからなかった。
- Artifacts の共有、公開、業務での利用事例を扱う日本語記事は見つからなかった。
- note 上の個人の claude.ai 活用記事（スキ数の多いもの）は、許可リストの制限で本文を確認できなかった。

---

## Q5. 2025〜2026年の日本語書籍・講座の目次

### Takeaway
2025年12月から2026年10月の間に、**少なくとも12冊以上**の Claude Code 専門書が出た。技術評論社だけで5冊。目次の傾向は、①入門＋アプリのハンズオン（平川、増山、掌田、大澤）、②運用と仕組み化（実践Claude Code入門、箕輪、齊藤）、③Skills 専門（佐藤）、④ビジネスパーソン・非エンジニア向け（みのるん式、羽田野、ひつじ）の4系統。共通の章立ては「CLAUDE.md、コンテキスト管理、MCP、サブエージェント、Hooks、Skills、セキュリティ」。2026年後半の本では Agent Teams、Plugins、組織導入が加わった。

### Cited Findings
- **平川知秀『Claude CodeによるAI駆動開発入門』技術評論社, 2025-12-05, 320頁, 3,080円**：1. 基本と環境構築／2. 5分でアプリ（デプロイ、UI デバッグ、テスト）／3. MCP で AI チャットボット（要件、タスク管理しながらの実装、GitHub Actions）／4. サブエージェントで並列作業（コンテキストウィンドウ、ガードレール、タスク分割、スラッシュコマンド、Hooks）／5. セキュリティと応用。付録はスラッシュコマンド一覧。目次は全169項目。著者は gihyo.jp で連載「これからはじめるClaude Code入門」も執筆。— [crystal-method](https://crystal-method.com/blog/claude-code-books/)／[NDL](https://ndlsearch.ndl.go.jp/books/R100000002-I034427524)／[gihyo 連載](https://gihyo.jp/article/2026/02/get-started-claude-code-07)
- **西見公宏・吉田真吾・大嶋勇樹『実践Claude Code入門―現場で活用するためのAIコーディングの思考法』技術評論社, 2025-12-26（NDL では 2026.1）, 304頁**：第1部 1章 ソフトウェアエンジニアリングとの統合、2章 基礎、3章「MCPを使いこなせ！」、4章「達人に学ぶスペック駆動開発」、Claude Code Action。第2部は動作原理、意図どおりに制御する、スペック駆動フローの設計と実践。CLAUDE.md、コンテキスト管理、Git Worktree とセッション分離も扱う。— [NDL](https://ndlsearch.ndl.go.jp/books/R100000002-I034465907)／[dot-ai](https://dot-ai.myuuu.co.jp/times/articles/108)
- **箕輪峻『Claude Code開発体系 拡張・制御・運用の手引き』インプレスNextPublishing, 2026-02-20, 154頁, 1,980円**：基本、MCP サーバーによる拡張、コンテキスト管理とサブエージェント、便利機能、動作の制御、カスタマイズと管理の6章。「入門書ではない」と割り切っている。— [crystal-method](https://crystal-method.com/blog/claude-code-books/)／[dot-ai](https://dot-ai.myuuu.co.jp/times/articles/108)
- **多佳宮崇志『ストーリーで覚えるClaude Code開発ガイド』ネクストステージ出版, 2026-02-13, Kindle のみ**：物語・解説・実践ワークの3層構成。CLAUDE.md、Plan モード、サブエージェント、MCP、チーム導入戦略。出版社ページでは確認できていない（crystal-method による注記）。— [dot-ai](https://dot-ai.myuuu.co.jp/times/articles/108)
- **齊藤貴義『完全解説！Claude Codeテクニック集 爆速開発のための完全ガイド』インプレス NextPublishing**：全15章（528頁と報告）。アーキテクチャ、コンテキストウィンドウ、Skills、サブエージェント、Hooks、Agent Teams、Tasks、MCP、Plugins、CI/CD とチーム開発、git worktree での並列開発、データ分析と ML、インフラ自動化（Terraform／Kubernetes）、性能・コスト最適化（Fast Mode、モデル選択）とトラブルシューティング。**発売日は情報源で食い違う**（窓の杜は 2026-05-08、crystal-method は 2026-08-18 のインプレス版と記載）。— [窓の杜](https://forest.watch.impress.co.jp/docs/bookwatch/news/2108437.html)／[crystal-method](https://crystal-method.com/blog/claude-code-books/)
- **大澤文孝『開発効率をアップする！ Claude Code 実用入門』マイナビ出版, 2026-05-19**：基本操作、アプリ開発、テスト、MCP サーバー開発、Skills とサブエージェントでの効率化、自動コーディング環境の構築。付録は Docker Desktop と VS Code。— [crystal-method](https://crystal-method.com/blog/claude-code-books/)
- **佐藤亮『Claude Codeで学ぶ Agent Skills入門』技術評論社, 2026-06-08, 272頁, 2,860円（目次全文を確認）**：1章 Skills とは（宣言的知識と手続き的知識、段階的開示、Projects・GPTs/Gems・MCP・ルールファイルとの違い）／2章 オープンスタンダード（agentskills.io、Copilot・Codex・Gemini CLI・Cursor の採用状況）／3章 初体験（自動発動とスラッシュコマンド、プラグインの4つの拡張ポイント、マーケットプレイス）／4章 デザイン系（frontend-design、theme-factory、canvas-design、brand-guidelines、algorithmic-art、slack-gif-creator）／5章 ドキュメント系（pdf、docx、pptx、xlsx）／6章 開発・コラボ系（web-artifacts-builder、webapp-testing、mcp-builder、doc-coauthoring、internal-comms）／7章 パートナー・サードパーティ（Notion、Firecrawl、Playwright、Remotion、skills.sh、信頼できるスキルの見分け方）／8章 skill-creator（見積書スキルの作成、テストと改善ループ、eval-viewer、description の最適化）／9章 配布・セキュリティ・組み込みスキル（`/simplify` `/batch` `/debug` `/loop` `/claude-api`）／付録はフロントマターのリファレンスと動的コンテキスト注入。— [技術評論社](https://gihyo.jp/book/2026/978-4-297-15698-5)
- **掌田津耶乃『ターミナルから始める次世代AIコーディング Claude Code入門』秀和システム新社, 2026-06-16, 3,300円**：Node.js 環境と API キー、プロンプト、レガシーコードのリファクタリング、Vitest／Jest での TDD、CLI ツール、Express、React（Claude API 連携の日英翻訳ボード）、MCP サーバーの自作。— [公募ガイド（PR TIMES）](https://koubo.jp/press-release/prtimes/c169048_r154)
- **Oikon・前川蒼『Claude Code実践入門［生成AI深掘りガイド］』SBクリエイティブ, 2026-08-14**：全7章。アプリを作りながら CLAUDE.md、Hooks、Agent Skills、MCP、Plugins を学び、セキュリティとコスト管理、組織導入、6章でエンタープライズ環境を扱う。技評の『実践Claude Code入門』とは別の本。Oikon は執筆の裏話（「Claude Code本は、どのように執筆チームで書かれたか」「変化の早いClaude Codeを書籍に落とし込む」）もスライドで公開している。— [crystal-method](https://crystal-method.com/blog/claude-code-books/)／[紀伊國屋](https://www.kinokuniya.co.jp/f/dsd-101001037025-06-)／[Oikon の Speaker Deck](https://speakerdeck.com/oikon48)
- **増山友司（とまだ）『Claude Codeで作って学ぶ AI駆動アプリ開発入門』技術評論社, 2026-09-08**：1章 料金プランなど／2章 セットアップ、`claude doctor`、Git／3章 入力とショートカット、コンテキスト管理、`@` 参照、スラッシュコマンド、権限ルール／4章 CLAUDE.md（`/init`、書き方、ディレクトリごとの分割、パス別ルール、チームでの共有）／5章 明確な指示、タスク分割、エラー対応、`/rewind`、`/code-review` スキルの作成／6章 既存コードの読解・テスト・リファクタ・ドキュメント生成／7章 MCP（Playwright、Context7、Supabase）／8章 タスク管理アプリ（Next.js、Supabase、E2E、Vercel）／9章 実務での活用（AI に何を任せるか、チームの課題、GitHub Actions でのレビュー）。同じ著者の無料 Zenn Book「Claude Code 完全ガイド」（全46章、2025-10-07 公開、2026-08-21 更新、約29万字）は Hooks に10章を割く。— [技術評論社](https://gihyo.jp/dp/ebook/2026/978-4-297-15824-8)／[Zenn Book](https://zenn.dev/tmasuyama1114/books/claude_code_basic)
- **御田稔（みのるん）『［みのるん式］ビジネスパーソンのためのClaude Code仕事術』技術評論社, 2026-09-24（目次全文を確認）**：1章 なぜコーディングエージェントが日常業務に有用か／2章 AI エージェントの基礎（料金プランと「トークン消費」、セキュリティの基本）／3章 セットアップ（コネクタで日程候補を調べる、ブラウザ拡張でフォームに入力）／4章「何でもAIに相談する癖」（作業フォルダ、音声入力での自己紹介、思考を整理せずに伝える）／5章 資料作成の前工程（最後の2割は自分で）／6章「半自動化」のサイクル（人間→AI→人間、ガードレール、手順ファイルを育てる）／7章 経費精算の半自動化（社内ルールの引き継ぎ、カード明細の私的情報を安全に処理、「コピペするだけ」）／8章 モノレポで「コンテキストの複利」（機密案件の分離、自分専用の設定、サブエージェント）／9章 プロジェクト業務（会議から現在地とタスクを更新、成功とつまずきをスキル・ルールにする）／10章 仕様駆動開発の考え方、「生成AI臭さ」を消す、複数セッションでの並行作業、スマホからの指示、チームの資産化、別の AI エージェントへの移植／11章 企業の「セキュリティの壁」（禁止ではなく安全な道、セキュリティ部門との協力、法人向け契約と管理設定）。— [丸善ジュンク堂](https://www.maruzenjunkudo.co.jp/products/9784297159399)
- **羽田野太巳『1週間でClaude Codeの基礎が学べる本』インプレス, 2026-09-25**：7日構成。前半は Claude デスクトップアプリ、後半は VS Code 拡張を使い、**ターミナル操作は不要**。MCP、Subagents、Agent Teams も扱う。— [crystal-method](https://crystal-method.com/blog/claude-code-books/)
- その他（目次は未確認）：ひつじ・染谷昌利『あらゆる仕事が爆速化する Claude Code徹底活用術』日本実業出版社 2026/08、池田朋弘『Claude 最強のAI自動化術』芸術新聞社 2026/07。— [紀伊國屋](https://www.kinokuniya.co.jp/f/dsd-101001037025-06-)
- **講座・連載**：Schoo「非エンジニアのためのClaude Code入門」（2026-09-07, 60分。チャット AI との違い、初期設定、活用シーン）— [Schoo](https://schoo.jp/course/9269)。gihyo.jp 連載（平川）— [gihyo.jp](https://gihyo.jp/article/2026/02/get-started-claude-code-07)。Udemy の講座もあることは確認できたが、名称は特定できなかった。— [Qiita まとめ](https://qiita.com/kamome_susume/items/af629235d2703e071f18)
- ある個人の有料の Zenn の本は、はてブ 170 users で、表示されたコメント7件の中に「こりを、200円で？情報商材感ある」「AIくさいな」などの批判的なものがあった（閲覧者の印象で、本が AI で書かれたと確かめたものではない）。
  > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。あわせて、コメントを原文の言い方に直し（元の「情報商材っぽい」「AI臭い」は言い換え）、「批判的なコメントが多い」を表示されたコメントの範囲の言い方にした。ブックマークのページに価格の表示はなく、「200円」はコメントによる。research/25 の P10。

### Inferences
- 書籍は「網羅的なリファレンス（齊藤、528頁）」と「特定の読者層・目的への特化（Skills、ビジネスパーソン、ターミナル不要）」に二極化している。辞書型の教材の競合は「網羅本」だが、書籍は**更新できない**（Oikon も変化の速さを書籍の課題として講演している）。Web 辞書はこの点で優位に立てる。
- 書籍目次に共通する章立て（CLAUDE.md、コンテキスト、MCP、サブエージェント、Hooks、Skills、セキュリティ、チーム・組織導入）は、日本の読者が期待する「標準カリキュラム」とみなせる。
- 2026年後半の本は「ターミナル不要」「ビジネスパーソン向け」が増えた。読者層は非エンジニアに広がっている。

### Gaps
- 箕輪本、大澤本、Oikon・前川本、羽田野本の詳細目次（節レベル）は取得できなかった（二次まとめのみ）。
- Amazon.co.jp のレビュー数やランキングは取得できなかった。
- 翔泳社から Claude Code の専門書が出ているかは確認できなかった。

---

## Q6. 読者の不満・よくある質問と、日本語コンテンツのギャップ

### Takeaway
読者の不満は、①**変化が速すぎて Tips がすぐ古くなる**、②**「完全ガイド」と称する AI 生成風の記事や有料記事の乱立への嫌悪**、③**CLAUDE.md の指示が守られない、英語に戻る**、④**利用上限・品質低下・コスト**、⑤**人間側のレビューが詰まり、疲労する**、に集約される。日本語コンテンツの空白は、**「なぜ効くかの原理」「効果の測定」「claude.ai の Research と Artifacts」「日本語の文書品質を仕組みで担保する体系」「レビューのボトルネックと人間の負荷」「Windows や日本語環境のトラブル」**。

> 【2026-11-03 注記】②は一部誤り（言い過ぎ）。根拠は Q6 の2件のはてなブックマークの、表示された数件のコメントで、読者全体の不満として量で確かめたものではない。「AI 生成風」は閲覧者の印象で、本が AI で書かれたと確かめたものではない。research/25 の P3・P10。

### Cited Findings

#### 読者の不満・反応（はてブのコメントなど）
- **乱立する「完全ガイド」への反発**：題に「完全ガイド」と付けたある個人の記事（はてブ 265）には「自称完全ガイドはどれだけ登場するんだ？」「Claude Codeを作っている人向けのガイドではないのでタイトル変えた方がいい」。ある個人の有料の Zenn の本（はてブ 170）には「こりを、200円で？情報商材感ある」「こういう記事が蔓延しすぎて嫌になってきた。」「AIくさいな」（表示されたコメント7件のうちの3件。閲覧者の印象である）。
  > 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。あわせて、有料の本へのコメントを原文の言い方に直した（元の「200円で？情報商材っぽい」「この手の記事に飽き飽き」「AI臭い」は言い換えだった）。どれも閲覧者の印象で、本が AI で書かれたことや内容の質を確かめたものではない。ブックマークのページに価格の表示はなく、「200円」はコメントによる。research/25 の P10。
- **変化が速い**：「ベストプラクティスが毎月変わる。追いつける人はすごい」（tonkotsuboy の記事へのコメント, 2025-07）。Oikon は「Tips はすぐ陳腐化するので方向性を学べ」と講演（2025-08）。DevelopersIO では石川覚がほぼ毎日「Claude Code v2.1.xxx の主要アップデート」を書いており（2026年10月だけで10本以上）、変化を追う需要が大きい。— [はてブ（tonkotsuboy）](https://b.hatena.ne.jp/entry/s/tonkotsuboy.github.io/20250717-findy-claudecode/)／[Oikon のスライド](https://speakerdeck.com/oikon48/claude-codekarawo-gaxue-bubekikoto)／[DevelopersIO タグ一覧](https://dev.classmethod.jp/tags/claude-code/)
- **「コマンドを覚えなくていい」という意見**：自然言語で頼めば Claude が実行してくれる（wataru86 の記事へのコメント）。逆に `/clear` や `/rewind` は過去のやり取りが消えて改善点を探しにくくなるので使わない、という人もいる。— [はてブ（wataru86）](https://b.hatena.ne.jp/entry/s/qiita.com/wataru86/items/b859f1578191a1e15808)
- **基本だけで十分か**：トップコメントは「bypassPermissions と statusline で、タスクごとか200K程度で再起動する。発展的な機能はレート制限が気になってからでいい」（stafes の記事, 2026-06）。「Skills や MCP は中身を確認してから入れる」という警告もあった。— [はてブ（stafes）](https://b.hatena.ne.jp/entry/s/zenn.dev/stafes_blog/articles/nano72mkn-claude-code-intro)
- **クラウドセッションの制約**：Skills が同じリポジトリにないと使えない、30GB のディスク要件、Compliance API の対象外、権限を渡したくない（2026-09）。— [はてブ（goat_eat_any）](https://b.hatena.ne.jp/entry/s/zenn.dev/goat_eat_any/articles/claude-code-cloud-sessions)
- **日本の流行は特殊なのか**：「Google Trends では世界は Cursor 優勢で、Claude Code は主に日本で人気」（2025-06）。Zenn の Claude Code 記事は Codex の10倍以上（2026-04 のスライド）。— [はてブ（carenet）](https://b.hatena.ne.jp/entry/s/zenn.dev/carenet/articles/59f62014092a1b)／[yuupher のスライド](https://speakerdeck.com/yuupher/claude-code-bu-kunai-zuo-xue-patosuraido)
- **Claude Code は嘘をつく、手抜きで「完了」と言う**：TODO のまま、スキップしたテストで「通過」と報告、推測を事実のように書いたドキュメント、ジュニア並みのコード品質（choplin, 2025-06）。メルカリのエンジニアリングブログ「The AI lied to me…」（2025-10-28, 本文は未取得）も同じテーマ。— [choplin](https://zenn.dev/choplin/articles/2025-06-24-claude-code-1-reality-and-mindset)／[CodeKnights（メルカリ事例の要約）](https://www.codeknights.co.jp/contents/claude-japan-cases-2026summer)
  > 【2026-11-03 注記】このブログの本文は research/25 の P11 で確かめた。存在しない API の項目を自信を持って答えた例と、指定した静的解析の道具を使わずに作り、動くことだけを確かめて完了と報告した例がある。
- **人間側がボトルネックになり、疲労する**：auto mode で承認の連打はなくなったが「レビュー地獄」になった（クラスメソッド, 2026-10-24）。READYFOR では83%が生産性向上を感じる一方、66.7%が並列作業の増加、42%が疲労感の増加を報告。Rehab for JAPAN はマネージャー層のマージまでの時間が93.5%増。タイミーの3人チームではデプロイ頻度が改善しなかった。神戸大の学生も「レビューと承認が新しいボトルネック」と指摘（2025-07）。— [DevelopersIO](https://dev.classmethod.jp/articles/devio2026-tokyo-claude-code-automode-unattended-environment/)／[CodeKnights](https://www.codeknights.co.jp/contents/claude-japan-cases-2026summer)／[Speaker Deck](https://speakerdeck.com/yuuuuuuuuu54/claude-codefa-biao)
- **利用上限と品質低下**：週次上限への不満（2025-08）。2026年3〜4月の品質低下（ポストモーテムで3つの原因を公表し、上限をリセット）。— [fleagne](https://zenn.dev/fleagne/articles/4eb2a7aef1acf9)／[GIGAZINE](https://gigazine.net/news/20260424-anthropic-claude-code-quality)
- **Agent Teams のコスト**：plan mode で約7倍（gihyo）。Pro ではすぐ上限に達する（クラスメソッド）。— [gihyo.jp](https://gihyo.jp/article/2026/02/get-started-claude-code-07)／[DevelopersIO](https://dev.classmethod.jp/articles/claude-code-agent-teams-how-to-build/)
- **よくある質問（記事の題材から推測した FAQ）**：日本語で返させる方法、文字化け（UTF-8 ロケールやフォント、Shift_JIS のファイル）、Windows／WSL でのインストール、CLAUDE.md・Skills・サブエージェント・MCP の使い分け、Pro と Max のどちらにするか、円での料金、会社で使ってよいか（学習のオプトアウト、Team と Enterprise）。— [GiftX](https://ai.giftx.co.jp/blog/claude-code-japanese/)／[Zenken](https://ai.zenken.co.jp/post/claude-code-pricing/)／[fujisho1216](https://qiita.com/fujisho1216/items/90b34ef9abd910deb6ac)

#### 陳腐化した情報（教材で注意が必要なもの）
- `/project:name` `/user:name` のカスタムコマンド記法（2025-07）→ Skills への統合（2026-01）で新規作成は Skill を推奨。— ある個人の記事（2025-07、旧）／[YouMind（新）](https://youmind.com/ja-JP/landing/x-viral-articles/claude-code-skills-merge)
- npm でのインストール、`/allowed-tools`、`/vibe`、「ultrathink」（2025-05 の acntechjp 記事）→ 現在はワンライナーのインストーラー（crystal-method）と `/effort`（ai-revolution）。キーワード方式の現状は未確認。— [acntechjp（2025-05）](https://zenn.dev/acntechjp/articles/5bf01d6b530b8d)／[medicalforce（2025-06, ultrathink）](https://zenn.dev/medicalforce/articles/8bc0b6afbbb8a7)／[ai-revolution](https://ai-revolution.co.jp/media/claude-code-quality-postmortem/)
- tmux での自作マルチエージェント組織（2025-06）→ 公式の Agent Teams（2026-02, 実験的）。— ある個人の記事（2025-06）／[gihyo.jp](https://gihyo.jp/article/2026/02/get-started-claude-code-07)
- 「Claude Code on the Web」→ 2026-09-24 に「クラウドセッション」として正式リリース。— [はてブ（goat_eat_any）](https://b.hatena.ne.jp/entry/s/zenn.dev/goat_eat_any/articles/claude-code-cloud-sessions)
- 「200k コンテキスト」を前提にした説明 → 1M コンテキストのモデルと `CLAUDE_CODE_AUTO_COMPACT_WINDOW`。— ある個人の記事（2025-09）／[クラスメソッド（2026-10）](https://dev.classmethod.jp/articles/claude-code-keep-sessions-short/)
- `/cost` → `/usage`（Issoh）。ある個人の記事（2026-03）はまだ `/cost` を推奨しており、「従量課金」前提の記述も定額プランのユーザーとずれる。— [Issoh](https://www.issoh.co.jp/tech/details/18753/)
- Serena MCP の「10倍賢く」（2025-07）など、測定根拠のない宣伝的な主張。— ある個人の記事（Zenn、2025-07）
- サブエージェントを工程ごとに大量に作る2025年の流儀 → 2026年は「コンテキストが独立しているかで分ける」へ（Anthropic とクラスメソッド）。— [DevelopersIO](https://dev.classmethod.jp/articles/claude-code-subagent-review/)
- cc-sdd のコマンド名：2025年の `/kiro:spec-init` 形式 → v3.0 では Skills 形式の `/kiro-discovery` など。— ある個人の記事（2025-09、旧）／[GitHub（新）](https://github.com/gotalab/cc-sdd)

> 【2026-11-03 訂正】否定的な文脈の実名を外した（decisions.md 2026-11-03「否定的な文脈の実名」）。この一覧で、古い情報の例として挙げた個人の記事の名前と URL を外した。

### Inferences
- **最大の空白は「原理と判断基準」**。Tips 集や「完全ガイド」は大量にあるが、変化が速いので個々の Tips は数か月で古くなる。読者（とくにはてブ層）は、公式に沿って誇張がなく整理された記事を高く評価している（wataru86、みのるんのスライド）。辞書型の教材は「機能の仕様」より「なぜそうするか（コンテキスト、検証、お願いと強制の違い、分離）」を軸にし、版ごとの差分は注記として分ける設計が向いている。
  > 【2026-11-03 注記】「高く評価している」は一部誤り（言い過ぎ）。量で確かめたものではなく、根拠ははてなブックマークに表示されたコメント1件とスライドの閲覧数である。research/25 の P3。
- **効果測定の空白**：個人記事のほとんどは自己申告の「◯倍速」。企業事例も自社公表の値。PLAID、SmartHR、DeNA など数値を出す企業はあるが、手法の比較（例：サブエージェントを統合して漏れが減ったか）は「未測定」と書かれている（クラスメソッド）。
- **人間側の負荷（レビュー、並列化による疲労、マネージャー層の詰まり）**は、2026年に表面化した新しい論点。日本語ではまだ体系的な処方がない。
- **日本語の文書品質**（文体の統一、表記ゆれ、AI臭さ、textlint と Hooks、推敲 Skill の選び方）は、需要がある（推敲 Skill の記事が 342いいね、書籍にも節がある）のに、まとまった解説がない。
- **claude.ai の Research と Artifacts**、および**Windows／WSL／IME などの日本語環境のトラブル**も手薄。
  > 【2026-11-03 注記】日本語の環境のトラブルは、体系的な資料はないが、CHANGELOG に個別の修正の記録が多いことを research/27 の #19 で確かめた（例：2.1.296・2.1.299 から、Shift-JIS などの UTF-8 でないファイルの編集と書き込みを拒む）。Takeaway の「Windows や日本語環境のトラブル」も同じ。

### Gaps
- teratail での質問傾向は、検索で該当がなく分析できなかった。
- X の投稿は記事に引用されたもの（4件）しか確認できず、日本語 X 上の不満を量的に把握することはできなかった。
- Zenn と Qiita のタグ全体の「いいね順ランキング」は、API とページへのアクセス制限で取得できなかった。人気の比較ははてブ users、Qiita の個別ページ、Speaker Deck の閲覧数に頼っている。
- 2026年に人気だった Zenn 記事（ナレッジワーク「月間400件以上のPR」、READYFOR のアンケート、PLAID、Spectee、ログラスなど）は許可リストの制限で本文を確認できず、数値は CodeKnights のまとめに頼った。
  > 【2026-11-03 注記】このうち READYFOR のアンケートの元の記事は research/25 の P7 で確かめた。

> 【2026-11-03 訂正】2つ目の項の X の投稿の書き手の名前を外した（Q1 D で外した記事が、この並びからたどれないようにするため。decisions.md 2026-11-03「工程2：反映を確かめた後の判断」）。
