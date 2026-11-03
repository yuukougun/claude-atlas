# 工程2 R5：公式情報の空白（requirements §10.4・21 §2.3）

- 担当：R5（工程2「調査の補完」）
- 確認日：2026-11-03（この報告の事実はすべてこの日に確かめた。版に依存するものは、その場で版を書く）
- 手元の Claude Code：2.1.317（`claude --version`）。文書だけで確かめ、Claude Code やアプリを実際には動かしていない
- 共通の指示：[../batches/step2/brief.md](../batches/step2/brief.md)

---

## 1. 調べた範囲と方法

### 1.1 範囲

割り当ての12項目を調べた。

- requirements §10.4「公式情報で未取得のもの」の9項目：Styles、チャット共有、断られたときの公式の案内、IDE 拡張の固有の機能、Desktop のローカル MCP、Office アドイン、knowledge cutoff の Help Center の記事、`ANTHROPIC_API_KEY` と課金の経路、AskUserQuestion の質問数の上限
- 21 §2.3 の3項目：個人向けプランの年齢の条件、Max プランの API credits、個人プランの学習への利用と保持の期間

あわせて、調査資料（00・01・02・05・10・11）のうち、これらに関わる記述を一次資料と照らした。

### 1.2 方法

- 公式の文書を curl で取り、文字だけを抜き出して読んだ。code.claude.com・platform.claude.com・claude.com/docs は Markdown 版（`.md`）を、Help Center（support.claude.com）と Privacy Center（privacy.claude.com）は HTML を読んだ。小さなモデルが要約する WebFetch は、取り違えを避けるために使っていない
- 記事の場所が分からないものだけ Web 検索（5回）で探し、見つけた記事は直接読んだ。検索結果の要約そのものは根拠にしていない
- 取り下げられた公式の記事（Styles の移行の記事）は、Internet Archive の写し（2026-07-10 に保存されたもの）で本文を読んだ。公式のページそのものではないので、その旨を出典に書く
- Help Center の検索ページ（`https://support.claude.com/en/?q=…`）で、Styles と拒否に関わる記事の有無を確かめた

### 1.3 使った一次資料（すべて 2026-11-03 に取得）

Help Center（support.claude.com）

- [How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)・[Personalization and settings（分類の一覧）](https://support.claude.com/en/collections/18031818-personalization-and-settings)・[How to use Claude in your preferred language](https://support.claude.com/en/articles/10769299-how-to-use-claude-in-your-preferred-language)
- [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)・[How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)・[Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)・[What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- Styles are moving to skills（ID 10181068）：2026-11-03 は 404。本文は [Internet Archive の写し（2026-07-10 保存、記事の日付は 2026-06-01）](https://web.archive.org/web/20260710101210/https://support.claude.com/en/articles/10181068-styles-are-moving-to-skills) で読んだ
- [Share and unshare chats](https://support.claude.com/en/articles/10593882-share-and-unshare-chats)・[Public links for shared chats](https://support.claude.com/en/articles/16762437-public-links-for-shared-chats)・[Share a chat with specific people](https://support.claude.com/en/articles/16762496-share-a-chat-with-specific-people)・[Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- [Monthly API credits for Max, Ultra, and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)・[What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)・[What is the Ultra plan?](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan)
- [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)・[Manage API key environment variables in Claude Code](https://support.claude.com/en/articles/12304248-manage-api-key-environment-variables-in-claude-code)
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- Safeguards の分類：[Safeguards（一覧）](https://support.claude.com/en/collections/4078535-safeguards)・[Safeguards warnings and appeals](https://support.claude.com/en/articles/8241253-safeguards-warnings-and-appeals)・[Our Approach to User Safety](https://support.claude.com/en/articles/8106465-our-approach-to-user-safety)・[Exceptions to our Usage Policy](https://support.claude.com/en/articles/9528712-exceptions-to-our-usage-policy)・[Age assurance on Claude](https://support.claude.com/en/articles/15171100-age-assurance-on-claude)・[Cyber Verification Program](https://support.claude.com/en/articles/14604842-cyber-verification-program)
- [Why Claude switched models in your conversation with Opus 5 or Opus 5.5](https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5-or-opus-5-5)・[Why am I receiving an 'Output blocked by content filtering policy' error?](https://support.claude.com/en/articles/9205721-why-am-i-receiving-an-output-blocked-by-content-filtering-policy-error)

Privacy Center（privacy.claude.com）

- [Is my data used for model training?](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)・[How long do you store my data?](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)・[How do I change my model improvement privacy settings?](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings)

Claude Code の文書（code.claude.com/docs/en/…）

- [authentication](https://code.claude.com/docs/en/authentication)・[headless](https://code.claude.com/docs/en/headless)・[data-usage](https://code.claude.com/docs/en/data-usage)・[errors](https://code.claude.com/docs/en/errors)・[commands](https://code.claude.com/docs/en/commands)
- [vs-code](https://code.claude.com/docs/en/vs-code)・[jetbrains](https://code.claude.com/docs/en/jetbrains)・[desktop](https://code.claude.com/docs/en/desktop)・[mcp](https://code.claude.com/docs/en/mcp)
- [tools-reference](https://code.claude.com/docs/en/tools-reference)・[hooks](https://code.claude.com/docs/en/hooks)・[sub-agents](https://code.claude.com/docs/en/sub-agents)・[best-practices](https://code.claude.com/docs/en/best-practices)・[agent-sdk/user-input](https://code.claude.com/docs/en/agent-sdk/user-input)・[agent-sdk/overview](https://code.claude.com/docs/en/agent-sdk/overview)（settings-reference・interactive-mode・common-workflows は語の検索だけ）

Claude Platform の文書（platform.claude.com）

- [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)・[Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)・モデルごとのページ（[Opus 5](https://platform.claude.com/docs/en/models/opus-5/overview)・[Sonnet 5](https://platform.claude.com/docs/en/models/sonnet-5/overview)・[Opus 4.6](https://platform.claude.com/docs/en/models/opus-4-6/overview)）

claude.com

- [Plans & pricing](https://claude.com/pricing)
- Claude for M365：[overview](https://claude.com/docs/office-agents/overview)・[Excel](https://claude.com/docs/office-agents/excel)・[PowerPoint](https://claude.com/docs/office-agents/powerpoint)・[Word](https://claude.com/docs/office-agents/word)・[Outlook](https://claude.com/docs/office-agents/outlook)・[Work across M365 apps](https://claude.com/docs/office-agents/work-across-apps)（Help Center の Excel・PowerPoint・cross-app の記事は、ここへ転送される）

anthropic.com

- [Consumer Terms of Service](https://www.anthropic.com/legal/consumer-terms)（表示は Effective Oct 8, 2025）・[Usage Policy](https://www.anthropic.com/legal/aup)（表示は Effective Nov 12, 2026）・[Updates to our Consumer Terms and Privacy Policy](https://www.anthropic.com/news/updates-to-our-consumer-terms)（2025-08-28）・[Claude's Constitution](https://www.anthropic.com/constitution)

そのほか

- Model Context Protocol の文書：[Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers)（Claude Desktop の JSON 設定の場所を確かめるため。Help Center の local MCP の記事がこのサイトを案内している）

### 1.4 AI の利用を断る指定の確認

新しいドメインを読む前に `python3 -I tools/check_noai.py`（`--robots` 付きを含む）で確かめた。noai・noimageai の指定があるドメインはなかった。atcoder.jp と codeforces.com は開いていない。

| ドメイン | 確かめた URL | 結果 |
| --- | --- | --- |
| support.claude.com | `/en/` | 指定なし（meta robots="all"、robots.txt に AI 向けの指定なし） |
| code.claude.com | `/docs/en/overview` | 指定なし |
| platform.claude.com | `/docs/en/about-claude/models/overview` | 指定なし |
| www.anthropic.com | `/legal/consumer-terms`・`/constitution` | 指定なし（consumer-terms は meta robots="noindex, nofollow"。検索に出さない指定で、AI の利用を断る指定ではない） |
| claude.com | `/pricing`・`/docs/office-agents/overview` | 指定なし |
| privacy.claude.com | `/en/` | 指定なし（meta robots="all"） |
| modelcontextprotocol.io | `/docs/develop/connect-local-servers` | 指定なし |
| web.archive.org | Styles の記事の写しの URL | 指定なし（取得は写し1件だけ） |
| github.com | `/anthropics/mcpb`（`/modelcontextprotocol/mcpb` へ転送） | 指定なし（robots.txt に AI のクローラ向けの Disallow の一覧はある）。中身は資料にしていない |

---

## 2. 結果の一覧

結果の区分：正しい／誤り／一部誤り／確かめられない／空白を埋めた（調査資料が「未取得」としていた点）。出典の確認日はすべて 2026-11-03。

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 1 | 02 §1-3（80行）：personalization の記事に Styles はないが、Incognito の記事から Styles 自体は残っているように読める | 一部誤り | 2026-06-01 に「Styles are moving to skills」が告知された。custom styles は skills へ自動で移され、既定の Concise・Explanatory・Formal はなくなり、Learning は skill として残り、移行が終わると styles のメニューは消える。2026-11-03 はこの記事も Styles の記事も 404。Incognito の記事の「custom styles」は古い記述の残り | Internet Archive の写し（記事 10181068）、personalization の記事、Incognito の記事 | 「指示の置き場所」（00 分野表 291行）から Styles を外す。日本語の出力を揃える仕組み（R6）に Styles を挙げない |
| 2 | 02 §1 Gaps（356行）・00 §7（878行）・requirements §10.4：Styles の現行の仕様は未取得 | 空白を埋めた | §3.1 | 同上 | 同上 |
| 3 | 02 §1-3 の「Styles は残っている」の現状：今も UI に styles のメニューが出るか | 確かめられない | Help Center に記事がなく、移行が終わったかを書いた公式の文書も見つからない。作者のアカウントで見れば分かる | Help Center の検索（`?q=styles`） | 作者に確かめてもらう候補（§5） |
| 4 | 02 §1 Gaps（357行）：共有の現行の仕様は未調査。「Free/Pro/Max ではファイル成果物を含む会話の公開共有が無効」 | 正しい（空白も埋めた） | 公開共有の無効は今も同じで、Ultra も対象。共有の仕様は §3.2 | Create and edit files、共有の3記事 | アプリの「共有」のページを書ける |
| 5 | 00 §7（878行）・requirements §10.4：断られたときの頼み直し方は未取得 | 空白を埋めた | §3.3 | Help Center（モデルの切り替え・Safeguards）、Claude Code の errors、Platform の Refusals and fallback、Usage Policy、Constitution | 症状のページ「断られた・止められた」 |
| 6 | decisions.md「書き方の方針（安全・面・表現）」3：誤って断られた正当な依頼に、目的と文脈を足す方法だけを書く | 正しい（根拠あり。ただし公式の案内はほかの手段も含む） | Constitution は、確かめられない理由でも依頼の文脈と理由は解釈を変えうる、偽りの文脈なら責任の一部はその人に移る、と書く。公式の案内には、巻き戻し・新しい会話・推論の全文を求めない・誤判定の報告・検証の制度もある | Constitution、Claude Code の errors、Help Center | 方針の言い換えの提案（§4.3） |
| 7 | 02 §4（588・648行）：推論を本文に書かせる指示は `reasoning_extraction` として拒否されうる | 正しい | 今は拒否の分類（`stop_details.category`）の一つとして明記され、出力の前に止まっても課金される分類に入る（2026-09 時点） | Refusals and fallback、Claude Code の errors | 「推論を見せてほしいとき」（00 分野表 256行）に課金の注意を足せる |
| 8 | 00 分野表（330行）：IDE で使う＝差分表示、選択範囲の共有（詳細は未調査）。01（380行）：IDE 固有の機能は未確認 | 正しい（空白も埋めた） | §3.4 | vs-code、jetbrains | 「IDE で使う」のページを公式の文書の確認日つきで書ける |
| 9 | 02 §1 Gaps（358行）：Desktop のローカル MCP の手順は未取得 | 空白を埋めた | §3.5 | Help Center の local MCP の記事、Claude Code の desktop・mcp、MCP の文書 | Desktop・MCP のページ |
| 10 | 02 §1-13（248〜255行）：M365 のアドインは有料プラン、「Let Claude work across files」は Pro/Max 既定オン・Team/Enterprise 既定オフ、開いているファイルにしか作用しない、チャット履歴はブラウザ内 | 正しい | 今の文書も同じ。プランの表記は Pro・Max・Team・Enterprise（Ultra の記載はない） | claude.com/docs/office-agents | 一覧ページ（requirements §6.3 の「周辺製品は一覧だけ」） |
| 11 | 02 §1 Gaps（359行）：Excel・PowerPoint・Word・Outlook それぞれの機能は未確認 | 空白を埋めた | §3.6 | 同上 | 同上 |
| 12 | 02 §6（893行）・05 §2-6（263行）・§3-6（329行）：現行4モデルの reliable knowledge cutoff は 2026年6月 | 正しい | training data cutoff も 2026年6月。古いモデルでは二つが違う（Opus 4.6 は reliable が 2025年5月、training が 2025年8月） | Models overview、モデルごとのページ | 数値ファイルに二つを分けて持つ |
| 13 | 02 §6 Gaps（912行）：Help Center の knowledge cutoff の記事は未取得 | 空白を埋めた | 記事は「How up-to-date is Claude's training data?」。並ぶ日付は training data cutoff に当たる（§3.7） | Help Center 8114494 | 同上 |
| 14 | 01（258行）：`--bare` は `ANTHROPIC_API_KEY` が要り、サブスクリプションの OAuth を使わない | 正しい | bare mode は OAuth の認証情報も keychain も読まない。Anthropic の API には `ANTHROPIC_API_KEY` か `apiKeyHelper` を使う | headless、authentication | 作者の決定（API キーを使わない）のままでは `--bare` を使えない（§4.3） |
| 15 | requirements §10.4・21 §2.3：`ANTHROPIC_API_KEY` と課金の経路の関係は未確認 | 空白を埋めた | §3.8 | authentication、Help Center 12304248・11145838 | 料金・認証のページ、制作の環境の点検 |
| 16 | 10 付録A-1（379行）・11 第4節 #12（792行）：AskUserQuestion は1回の呼び出しで最大4問（出典は Zenn で未確認） | 正しい | Claude Code の hooks の文書は「1〜4問」、Agent SDK の文書は「1〜4問、各問に2〜4の選択肢」と書く（§3.9） | hooks、agent-sdk/user-input | 数値ファイルに入れてよい |
| 17 | 01（405行）：Best practices は「AskUserQuestion ツールで詳しくインタビューして→SPEC.md」 | 一部誤り（文言が古い） | 今の Best practices はツール名を出さず、「spec が書けるまでインタビューして SPEC.md に書いて」と頼むと Claude が選択式の質問を返す、と書く | best-practices | 雛形 A-6 などは「インタビューして」と書けば足りる |
| 18 | 21 §2.3：個人向けプランの年齢は18歳以上（担当の記憶） | 正しい | 利用規約 §2：18歳以上か、居住地で利用の同意に必要な最低の年齢の、高い方。Help Center は18歳未満の兆候があれば年齢の確認を求めるとする（§3.10） | Consumer Terms、Age assurance | 読者の前提（decisions「読者の前提」）に矛盾はない |
| 19 | 02 §2-1（373行）：Max は 5x が月 $100、20x が月 $200 | 誤り（2026-11-03 時点で古い） | Max 20x は Ultra に改名された（既存の契約者は自動で移り、価格は同じ）。Max は月 $100 で Pro の5倍（5時間と週）。Ultra は月 $200 で週に Pro の10倍、確認済みのアカウントは5時間の上限がない | Max・Ultra の記事、Plans & pricing | 料金・プランのページと数値ファイル。作者のプランの確認（§4.3） |
| 20 | 02 §2-1（374行）：Max の API credits は月次で 5x に $100、20x に $200 | 一部誤り（名称が古い） | Max に $100、Ultra に $200。Team は席ごとに Standard $20・Premium $100 を合算し、月 $500 まで。使い道は §3.11 | Monthly API credits の記事 | 同上 |
| 21 | 02 §2-1（387行）：Max/Team の月次 API credits は 2026-10-07 開始で、Console の組織を紐付けて受け取る | 正しい | Release notes の 2026-10-07 の項と一致。受け取りには7日以上の契約が要り、紐付けられる組織は1つ | Release notes、Monthly API credits の記事 | なし |
| 22 | 02 §2-1（375行）：Max での Fable は週上限の50%まで | 正しい | 料金のページは「週上限の半分まで」と書く。ただし Max・Ultra の記事は「Fable には別の週上限がある」と書く（02 §2-4 の「同じ週上限の内側」との関係は確かめていない） | Plans & pricing、Max・Ultra の記事 | R1（10-29 以降の変更）と照らす |
| 23 | 05 §4-7（466行）：学習を許可すると保持は5年、許可しなければ従来どおり30日 | 正しい（補足が要る） | 許可すると、設定の後の新しい会話と再開した会話を、匿名化した形で最大5年、学習のパイプラインに残す。「30日」は削除した会話がバックエンドから消えるまでの期間。違反と判定された会話は入出力が最大2年、分類のスコアが最大7年残る。フィードバックは5年（§3.12） | Privacy Center、2025-08-28 のお知らせ、Claude Code の data-usage | 安全とデータのページ、数値ファイル |
| 24 | 05 §4-7（468行）：設定の場所は claude.ai/settings/data-privacy-controls | 正しい | Privacy Center の手順では Settings > Privacy の「Help improve our AI models」 | data-usage、Privacy Center 12109829 | なし |
| 25 | 05 §4-6（462行）：`/feedback`・`/bug`・`/share` を使うと会話が送られ、5年保持 | 正しい | `/share` は `/bug` の別名で、公開リンクを作る機能ではない（v2.1.212 より前は `/feedback` の別名） | data-usage、commands | 「共有」と取り違えないよう注記 |
| 26 | 05 §4-7（470行）：incognito は履歴にもメモリにも残らない。Team・Enterprise では管理者がデータのエクスポートで見られる | 正しい | 加えて、学習には使わず、バックエンドには既定で30日残る（Enterprise は組織の保持の設定による）。新しい体験ではファイル作成とコード実行が使えない | Incognito の記事 | 安全とデータのページ |

件数：正しい15（うち2件は空白も埋めた）、誤り1、一部誤り3、確かめられない1、空白を埋めた6。

---

## 3. 新しく分かったこと

各項目は、教材に書くときに使える形にした。確認日はすべて 2026-11-03。

### 3.1 claude.ai の Styles（今もあるか・どこで設定するか・Instructions との関係）

- **移行の告知**（2026-06-01 付の記事「Styles are moving to skills」。Internet Archive の 2026-07-10 の写しで読んだ）
  - 自分で作った styles は、自動で skills に移される。移された skill は既定で無効なので、Customize > Skills で使うものを有効にする
  - 既定の styles のうち Concise・Explanatory・Formal は、移行の後は使えない。Learning は skill として残り、Customize > Skills の「+」> Browse skills から入れる
  - 移行が終わると styles のメニューは表示されなくなる。それまでは styles と skills が並ぶ
  - 移された style は、名前から作られる slash command `/{名前}-style` で呼ぶ。名前は小文字にし、空白をハイフンにし、記号・絵文字・アクセントを除く。長すぎれば切り詰め、同じ名前になれば番号を付ける
  - skills を使いたくなければ、同じ調子・形式の指示を Instructions に書けばよい、と記事は案内している
- **2026-11-03 の状態**：この記事は英・独・西・伊・日のどの版も 404 で、Help Center を「styles」で検索しても Styles の記事は出ない。個人設定の記事は、置き場所を Instructions for Claude（全会話）・project instructions（プロジェクトの中だけ）・skills（応答の調子と形式、繰り返す振る舞い）の三つとし、「応答の形式や届け方を変えたいなら skills」とする。Styles は出てこない
- **古い記述の残り**：Incognito の記事の FAQ と、Privacy Center の学習の記事に「custom styles」の語が残る。今も Styles があることの根拠にはならない
- **Instructions の場所**：Settings > Your Claude > Instructions（旧レイアウトは Account > Instructions for Claude）。全会話に効く。Cowork の Global instructions はここに統合された
- **教材への書き方（案）**：「Styles は 2026-06 に skills への移行が告知され、2026-11-03 時点で公式の記事は取り下げられている。調子と形式をいつも揃えたいなら Instructions、場面ごとに切り替えたいなら skill を使う（移された style は `/{名前}-style` で呼ぶ）」。UI にメニューがまだ出るかは未確認と添える
- Claude Code の output styles とは別の機能である。混同しないよう、用語集で分ける

### 3.2 チャット共有（claude.ai）

- **共有のしかたは2つある**
  - 特定の人への招待（メール）：既定の共有のしかた。全プラン（Free・Pro・Max・Ultra・Team・Enterprise）で、claude.ai の Web から使える。モバイルのアプリからは、まだ招待できない（共有された会話はどの端末でも開ける）。招待はそのメールアドレスでしか開けず、転送しても他の人には開かない。相手に Claude のアカウントがなければ、登録（Free でよい）へ案内される。開かれない招待は30日で切れる。1日に招待できる人数に上限がある
  - 公開リンク：Free・Pro・Max・Ultra だけ。リンクを知っていれば、アカウントがなくても誰でも見られる
  - Team・Enterprise：組織の中だけ。組織のドメインのメールに招待するか、「Anyone at [組織]」を選ぶ。公開リンクは作れない。管理者は共有を止め、共有を一覧して取り消し、監査ログで見られる
- **共有されるもの**：共有した時点の snapshot（それまでのメッセージと artifact）。共有の後のメッセージは入らない（招待なら「Update shared chat」、公開リンクなら共有をやめて共有し直すと更新される）。見るだけで、続きの会話・自分のアカウントへの複製・ファイルのダウンロードはできない。添付したファイルは入らない（組織の中の共有を除く）。MCP や connector から取った生のデータは出ず、Claude の最終的な応答だけが見える
- **取り消し**：Share のメニューで Public から Private に（招待なら「Turn off」）。Settings > Privacy の Shared chats（Manage）で一覧し、1件ずつ Unshare できる。止めるとリンクはすぐに開かなくなる。会話を消すと snapshot も消える
- **公開リンクの注意**：共有のページには noindex を付け、一覧やサイトマップを出さず、推測できない長い URL にしている。ただし、リンクを貼られた先、コピーやスクリーンショット、外部の保存（アーカイブ）は消せない。公式も「公開リンクは公開したものとして扱う」よう勧めている
- **制限**：コード実行とファイル作成で作ったファイルを含む会話は、Free・Pro・Max・Ultra では公開共有できない（安全のための措置として明記）
- **別物との区別**：Claude Code の `/share` は `/bug` の別名で、会話を Anthropic に送る（5年保持）。共有のリンクは作らない。Claude Code の `Artifact` ツールで公開した artifact は公開リンクで共有できる（Team・Enterprise は組織の中で、公開は Owner が許可したときだけ。tools-reference）

### 3.3 断られたとき（拒否・利用ポリシー）の公式の案内

**(a) 何が起きているか（面ごと）**

- **アプリ（claude.ai・Desktop・Mobile・Cowork・M365・Claude Code など）**：Opus 5・5.5（Sonnet 5.5、Fable 5・5.1 も別の記事がある）は、すべての依頼に分類器をかける。分類器は利用者が打った文だけでなく、モデルが読むもの（memory、connector の内容、web 検索の結果、ファイル）も見るので、打っていない内容が引き金になりうる。サイバー（exploit の生成など）・生物（dual-use）・最先端の LLM 開発（Opus 5.5 だけ）では、能力の低いモデルに切り替えて答え直す。推論の抜き出し（distillation）は切り替えずに止める。自動の切り替えは既定でオンで、Settings > Capabilities の「Switch models when a message is flagged」で切れる（Claude Code では Config > MODEL & OUTPUT）。切れば、止まったところで会話が止まり、直して送り直すか、手で低いモデルに送るかを選ぶ。公式は、分類器は正当な依頼も止めることがあり、減らす努力を続けていると書く
- **Claude Code**：表示は「<model> can't help with this. Start a new session to continue」（v2.1.219 以降の文）。判定は会話全体にかかるので、同じセッションで送り直しても、`--continue`・`--resume` で開き直しても、また止まる。サイバーの分類では別の表示（「<model>'s safeguards flagged this message」）になり、Cyber Verification Program へのリンクが付く。ただし自動のモデルの切り替えがあるモデル（Opus 5.5・Sonnet 5.5）では表示が違い（「… flagged this session」で始まる）、このリンクは付かない
- **API**：HTTP 200 の普通の応答で `stop_reason: "refusal"` が返る。`stop_details.category` は cyber・bio・frontier_llm・reasoning_extraction・general_harms（または null）。文書は、どの分類でも無害な仕事が引っかかりうると書く
- **「Output blocked by content filtering policy」**：既存の著作物をそのまま再現させないためのもので、内容の是非の判断ではない、と Help Center は説明する

**(b) 公式が勧めること（正当な依頼が止められたとき）**

1. 引き金になったやり取りより前に戻して、言い方か進め方を変える。Claude Code では Esc を2回か `/rewind`、どこが原因か分からなければ `/clear` で新しい会話にする（前の会話は `/resume` に残る）。`-p` では `--continue` を付けずに新しいセッションで言い直す。アプリでは、切り替えの後に元のモデルへ戻すと同じ判定がまたかかりうるので、前のメッセージを直してから送るとよい、と公式が書く
2. 推論の全文や決まった形（`<thinking>` の欄、JSON の reasoning の欄など）を求める指示を外す。CLAUDE.md・skill・subagent・output style・MCP のツールの説明に入っていることもあり、`claude --safe-mode` で設定を外して切り分けられる。理由を知りたいなら、短い説明・根拠・行ったことの要約を頼み、thinking の要約は `showThinkingSummaries`（Claude Code）や `display: "summarized"`（API）で読む
3. 誤った判定を報告する。アプリは「Send feedback」、Claude Code は `/feedback`（表示の Request ID を添えられる）、API はサポートに request ID を添える。警告が誤りだと思えば usersafety@anthropic.com へ、アカウントの停止には claude.ai/restricted の異議申し立て（停止されたアカウントでログインして使う）
4. 正当な専門の仕事なら、検証の制度に申し込む。サイバーは Cyber Verification Program（2026-10 に Opus 5.5・Sonnet 5.5・Mythos 5.1 向けの3段階になった。個人で申し込めるのは Defense の段階だけ）、生命科学は Life Sciences Verification Program（組織向け）
5. モデルを変える。Claude Code の errors は「判定はモデルごとに違うので、`--model` で変えると通ることがある」と書く。アプリは自動で切り替える。API は fallback（server-side は beta、SDK の middleware、手書きの再試行）で別のモデルに送り直す設計を勧める（「同じ依頼を別のモデルに送れば、たいてい答えが得られる」）

**(c) 目的と文脈を足すことの根拠**

- Claude の Constitution（Anthropic が公開。CC0）は、Claude は利用者の申告を確かめられないが、依頼の文脈と理由は Claude が手伝うかどうかに影響しうる、確かめられない理由でも無害な読みと悪意の読みの見込みを上げ下げする、と書く。偽りの文脈で助けを得たなら、結果の責任の少なくとも一部はその人に移る、とも書く。逆に、文脈によって手伝わなくなることもある（ナイフの削り方の例）
- したがって、「本当の目的と文脈を書き足す」は公式の考え方に沿う。偽りの文脈を作ることは、教材で勧められない

**(d) 書いてはいけない側の根拠**

- Usage Policy は、Anthropic の許可なく製品の機能・制限・ガードレールを意図して回避・妨害すること（jailbreak や prompt injection で有害な出力をさせることを含む）を禁じる。分類器を避けるための言い換え・分割は、これに当たりうる
- 違反と判断されると警告が出て、重なればアカウントの停止になりうる。繰り返す利用者には、感度を上げた safety filter を一時的にかけることがある（Our Approach to User Safety。公式は、これらの仕組みは誤りうると認めている）
- 課金：出力の前に止まった拒否でも、bio・frontier_llm・reasoning_extraction（アプリの記事では distillation）の分類は課金される。2026-09 時点で誤判定の少ない分類だから、という説明である。ほかの分類は課金されない。途中で止まれば、それまでの入力と出力は課金される

**教材への書き方（案）**：症状のページ「断られた・止められた」に、(1) 面ごとの表示の違い、(2) 会話全体（読み込んだ資料を含む）が判定されるので巻き戻すか新しい会話にする、(3) 本当の目的と文脈を足す（偽らない）、(4) 推論の全文を求めない、(5) 誤判定は報告する、(6) 専門の仕事は検証の制度、の順に書く。回避の言い換えは書かない。

### 3.4 IDE 拡張（VS Code・JetBrains）の固有の機能

**VS Code の拡張**（Cursor など VS Code の派生でも入る。Open VSX にもある）

- 前提：VS Code 1.94.0 以上。有料プラン（Pro・Max・Ultra・Team・Enterprise）か Console のアカウントで、API キーは要らない
- 拡張は自分用の CLI を同梱する。拡張の版＝同梱の Claude Code の版。拡張を入れても `claude` は PATH に入らないので、統合ターミナルで CLI を使うには別に CLI を入れる
- 固有の機能
  - 計画のレビュー：Plan モードでは、計画が Markdown の文書として開き、行ごとにコメントを付けて返せる（`/plan` は v2.1.280 以降）
  - 差分：Manual モードでは編集の前に左右の差分を出して許可を求める。変更ごとの Accept・Reject は v2.1.275 以降（100か所を超える差分は丸ごとで判断）。差分を手で直してから受け入れると、Claude にそのことが伝わる
  - 選択範囲と開いているファイル：選んだ範囲と開いているファイル名が自動でメッセージに入る。Option+K（Mac）/ Alt+K で `@file.ts#5-10` の形の参照を入れる。設定 `attachSelection`（v2.1.300 以降）・`attachOpenFile`（v2.1.271 以降）で止められる
  - 除外：チャットの欄では、`files.exclude`・`search.exclude` に当たるファイルと、git が無視するファイルの選択範囲は送らない（パスだけ）。ただし統合ターミナルの CLI には効かないので、秘密は `Read` の deny ルールで守る
  - checkpoints：メッセージから「会話を分岐」「コードだけ戻す」「両方」を選べる
  - 複数の会話をタブや窓で開ける。Customize のメニューから MCP・hooks・permissions・memory・CLAUDE.md・output styles・sandbox・Claude in Chrome を扱える（それぞれ版の条件がある）
  - コンテキストの使用量の表示、prompt cache の残り時間の時計、subagent の「agent map」
- CLI との違い：コマンドと skills は一部だけ、`!` の Bash の近道とタブ補完はない。会話の履歴は CLI と共通（`claude --resume` で続けられる）
- 組み込みの IDE 用 MCP サーバー（`ide`）：拡張が動いていると、CLI はこれにつながり、VS Code の差分表示を使い、選択範囲を読み、Jupyter のセルを実行する。`127.0.0.1` の 10000〜65535 の乱数のポートで、認証のトークンは `~/.claude/ide/<port>.lock`（権限 0600）に書かれる。モデルに見えるツールは `mcp__ide__getDiagnostics`（Problems の欄を読む）と `mcp__ide__executeCode`（毎回 VS Code の確認が出る）の二つ。チャットの欄の診断は `mcp__claude-vscode__getDiagnostics`（v2.1.285 以降）で、`Read` の deny では止まらないので、名前で deny する
- 設定：拡張の設定（VS Code 側）と `~/.claude/settings.json`（CLI と共通）の二つ。`initialPermissionMode` はユーザーの設定だけを読む。`allowDangerouslySkipPermissions` を入れると Bypass が選べるようになる（文書はネットにつながらない sandbox だけで使うよう書く）。v2.1.283 以降、最初の権限モードは Auto
- シェルに `ANTHROPIC_API_KEY` があっても、VS Code がシェルの環境を受け継いでいなければ使われない（端末から `code .` で起動すると受け継ぐ）

**JetBrains のプラグイン**（IntelliJ IDEA・PyCharm・Android Studio・WebStorm・PhpStorm・GoLand など）

- プラグインは「Claude Code [Beta]」の名前で、JetBrains Marketplace にある。CLI を同梱しないので、CLI を別に入れる（プラグインは IDE の統合ターミナルで `claude` を動かしてつながる）
- 機能：Cmd+Esc / Ctrl+Esc で開く。差分を IDE の差分表示で出す（`/config` の Diff tool：auto か terminal）。選択範囲と開いているタブを自動で渡す（`Read` の deny で止まる）。Cmd+Option+K / Alt+Ctrl+K でファイルの参照を入れる。IDE の検査の結果（lint・構文の誤り）を `getDiagnostics` で読む（編集の後に自動では読まない）
- 外のターミナルから使うときは `/ide` でつなぐ
- WSL2：「No available IDEs detected」になるのは、WSL2 の NAT か Windows のファイアウォールが原因であることが多い。WSL2 の範囲を許すファイアウォールの規則を足すか、mirrored networking（Windows 11 22H2 以降）にする。WSL の CLI は `wsl -d Ubuntu -- bash -lic "claude"` の形で指定する
- Remote Development では、プラグインを手元ではなく remote host に入れる
- 安全の注意：acceptEdits や auto mode では、IDE が自動で実行する設定ファイルを Claude が書き換えうる。これは Bash の承認を迂回する道になりうるので、文書は Manual モードを考えるよう書く

**教材への書き方（案）**：decisions（安全・面・表現 5）は IDE の拡張を「未確認」と書くとしているが、機能の概要は公式の文書（確認日・版つき）で書ける。動作は制作の環境で試していないと添える。

### 3.5 Desktop アプリのローカル MCP の設定

- **desktop extensions（.mcpb）**：ローカルの MCP サーバーを一つの包みにしたもの。ディレクトリ（Anthropic が審査したもの）から入れるには、Settings > Desktop app の Extensions の「Manage」（旧レイアウトは Settings > Extensions）から「Browse extensions」。自作の .mcpb は「Advanced settings」の Extension Developer にある「Install Extension…」から入れる
  - API キーなど sensitive と印を付けた設定は、OS の秘密の保管庫（macOS の Keychain、Windows の Credential Manager、Linux の keychain）で暗号化される
  - Node.js・Python・バイナリのサーバーに対応し、Desktop は Node.js を内蔵する
  - ディレクトリのものは既定で自動更新、私的に配った .mcpb は手で入れ替える
  - Team・Enterprise の Owner は、公開の extensions を許す・止める、許可の一覧、自作の extension の配布ができる。端末側の企業向けの方針（`isDesktopExtensionEnabled` など）はアプリ内の設定より優先される
- **JSON の設定（従来の方法）**：`claude_desktop_config.json` の `mcpServers` に command と args を書き、Desktop を完全に終了して起動し直す。ファイルの場所は macOS が `~/Library/Application Support/Claude/`、Windows が `%APPDATA%\Claude\`、Linux が `~/.config/Claude/`。MCP の文書は Settings > Developer の「Edit Config」から開くと書くが、Help Center はこの画面を旧レイアウトの名前として扱う（新しいレイアウトでの入口の名前は確かめていない）。サーバーは利用者の権限で動くので、渡すフォルダを絞るよう文書は書く
- **つながりの確認**：入力欄の「+」>「Connectors」で、つながった MCP サーバーとツールが見える。Extensions のページの Local MCP servers の欄（旧レイアウトは Settings > Developer）で状態とログを見る
- **Claude Code との関係**：Desktop の Code タブのローカルのセッションは、`claude_desktop_config.json` のサーバーも、`~/.claude.json` と `.mcp.json` のものと並べて読む（同じ名前なら Desktop の設定が勝つ）。単独の CLI は `claude_desktop_config.json` を読まない。`claude mcp add-from-claude-desktop` で `~/.claude.json` に写せる（macOS と WSL だけ。名前に英数字・ハイフン・下線以外を含むものは写せない）
- Linux の Desktop は beta（Ubuntu・Debian。Claude Code の文書の一覧）

### 3.6 Office アドイン（Claude for M365：Excel・PowerPoint・Word・Outlook）

- **提供**：Excel・PowerPoint・Word は Pro・Max・Team・Enterprise で一般提供、Outlook は beta（同じプラン）。ページに Ultra の記載はない。Microsoft AppSource の「Claude for Microsoft 365」から入れ、Claude のアカウントでサインインする。組織は M365 の管理センターから配れる。Bedrock・Vertex AI・Foundry・LLM gateway を通す配り方もある（このときは cross-app が使えない）
- **Excel**：セル単位の引用つきで数式やモデルを説明する、数式の関係を保って前提の値を変える、`#REF!` などの原因をたどる、テンプレートを埋める・モデルを作る、並べ替え・フィルター・ピボット・条件付き書式・入力規則。データテーブルとマクロ・VBA はできない。最終の成果物や監査に関わる計算を人の確認なしに使うことは勧めていない。Excel 2016・2019 の買い切り版と iPad では動かない
- **PowerPoint**：既存のテンプレートでスライドを作る、特定のスライドだけ直す、箇条書きを図やネイティブのグラフにする
- **Word**：節の引用つきで答える、書式を保って選んだ範囲を直す、変更履歴（tracked changes）として編集する、コメントのスレッドに沿って直して返信する、相手の修正（redline）を要約する、文書のスタイルでテンプレートを埋める
- **Outlook**：受信箱の仕分け、利用者の文体での返信の下書き（送らずに作成の欄に置く。送信の権限 `Mail.Send` を求めない）、スレッドの要約（メールごとの引用つき）、添付の .docx・.xlsx を開かずに読む、会議の時間を探して招待を下書きする。導入には管理者の Microsoft Graph の同意が要る。外部の差出人のメールには prompt injection の注意がある
- **アプリをまたぐ**：add-in ごと・端末ごとに「Let Claude work across files」をオンにする（Pro・Max は既定でオン、Team・Enterprise は既定でオフで、管理者は組織で止められる）。開いているファイル・メール・予定にしか作用せず、ファイルを作る・開く・閉じる・切り替えることはできない。有効な skills はアプリをまたいで効く
- **指示**：各アドインの Settings に Instructions がある。Excel の指示は Excel だけに効く
- **利用とデータ**：Claude のプランの利用上限に数える。使えるモデルは Office 向けに絞った一部。チャットの履歴はブラウザの IndexedDB に残り、端末の間で同期しない。会話（読んだ内容と添付を含む）は Anthropic に送られ、履歴を消しても Anthropic 側の写しは消えない。バックエンドでは30日以内に消す（例外は組織向けの保持の記事による）とされる。組織の独自の保持の設定は引き継がず、Enterprise の監査ログにも入らない（Compliance API には入る）
- **既知の不具合**：2026-09・10 の Windows の M365 の更新の後、履歴と skills が消えた利用者がいる、と全ページに注意がある

### 3.7 knowledge cutoff の Help Center の記事

- 記事は「How up-to-date is Claude's training data?」（Get started with Claude の分類）。モデルごとに「この時点までのデータで学習した」と並べる：Haiku 5.5・Sonnet 5.5・Opus 5.5・Fable 5.1 が 2026年6月、Opus 5 が 2026年5月、Sonnet 5・Fable 5・Opus 4.8・Opus 4.7 が 2026年1月、Sonnet 4.6・Opus 4.6 が 2025年8月、Haiku 4.5 が 2025年7月、Opus 3 が 2023年8月。詳しくは Models overview を見るよう案内している
- この日付は Platform の文書の **training data cutoff** に当たる。Platform はもう一つ **reliable knowledge cutoff**（知識がいちばん広く確かな時点）を載せ、古いモデルでは早いことがある（Opus 4.6：reliable が 2025年5月、training が 2025年8月。Opus 5・Sonnet 5 は二つが同じ）。現行の4モデルは二つとも 2026年6月。両方の詳細は Transparency Hub にある
- **教材への書き方（案）**：「どこまでの知識を当てにできるか」は reliable knowledge cutoff で書く。Help Center の一覧は training data cutoff なので、二つを数値ファイルに分けて持つ

### 3.8 `ANTHROPIC_API_KEY` と課金の経路（Claude Code）

- **優先の順番**（authentication の文書）：(1) クラウドの提供元（`CLAUDE_CODE_USE_BEDROCK` など）、(2) `ANTHROPIC_AUTH_TOKEN`、(3) `ANTHROPIC_API_KEY`、(4) `apiKeyHelper`、(5) `CLAUDE_CODE_OAUTH_TOKEN`（`claude setup-token` で作る1年の token。サブスクリプションで認証する）、(6) Anthropic の profile と federation、(7) `/login` のサブスクリプション（Pro・Max・Ultra・Team・Enterprise の既定）。社内の gateway にサインインしたセッションは、この順番の外で最も強い
- **環境変数を置くとどうなるか**
  - 対話のセッションでは、最初に一度だけ、その鍵を使うかを聞かれ、答えは記憶される。後から変えるには `/config` の「Use custom API key」（変数があるときだけ出る）
  - `-p`（非対話）では、変数があれば必ずその鍵を使う
  - 鍵を使うと、その鍵の Console の組織に API の従量の料金がかかる。サブスクリプションでログインしていても同じ（Help Center）。プランの利用量は使われない
  - 起動のときに鍵が見つかれば確認が出て、両方が有効ならログインの後に通知が出る。`/status` で今の認証を確かめられ、使っていない方に印が付く
- **面による違い**：`ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN`・`apiKeyHelper` は、CLI と CLI を包む面（VS Code の拡張、Agent SDK、GitHub Actions）に効く。Claude Desktop とクラウドのセッションはこれらを読まず OAuth を使う。クラウドのセッションは、環境に鍵を置いてもサブスクリプションの認証が使われる
- **`--bare`**：OAuth の認証情報も keychain も読まず、`CLAUDE_CODE_OAUTH_TOKEN` も読まない。Anthropic の API には `ANTHROPIC_API_KEY` か `apiKeyHelper` が要る
- **サブスクリプションで `-p` や Agent SDK を動かすと**、プランの利用上限から引かれ、API credits は使われない（Monthly API credits の FAQ）。なお、第三者の開発者が自分の製品で claude.ai のログインや利用枠を提供することは、許可がなければ認められていない（Agent SDK の概要）
- **組織の制限**：管理者が `forceLoginOrgUUID`・`forceLoginMethod` を設定すると、`ANTHROPIC_API_KEY` などの環境の認証情報のセッションは起動の時点で止められる
- **教材への書き方（案）**：サブスクリプションで使うなら `ANTHROPIC_API_KEY` を置かない。シェルの設定ファイルに書いて忘れる、が典型の落とし穴。`-p` は確認なしで鍵を使う。確かめるには `/status`

### 3.9 AskUserQuestion の1回の質問数

- Claude Code の hooks の文書（ツールの入力の節）：AskUserQuestion は「1〜4問の選択式の質問」をする
- Agent SDK の文書（Handle approvals and user input）：1回の呼び出しで1〜4問、各問に2〜4の選択肢。各問の `header` は12文字まで。`multiSelect` で複数選べる。利用者は「Other」で自由に書ける
- subagent からは使えない（Agent SDK の文書の制限。Claude Code の sub-agents の文書も、すべての subagent から外すツールに挙げる）
- `-p` では、承認を受け持つ仕組み（permission host）があるときだけ使われる（hooks の文書）
- 答えないと、既定では待ち続ける。`askUserQuestionTimeout`（60s・5m・10m）で、放っておくと選んだ分だけ送って先へ進むようにできる（tools-reference）
- 今の Best practices は、ツール名を出さずに「spec が書けるまでインタビューして SPEC.md に書いて」と頼む例を示し、Claude が選択式の質問を返すと書く。spec ができたら新しいセッションで作る

### 3.10 個人向けプランの年齢の条件

- 利用規約（Consumer Terms、表示は Effective Oct 8, 2025）§2「Account creation and access」：18歳以上か、居住地で利用の同意に必要な最低の年齢か、高い方。この規約は claude.ai・Claude Pro など個人向けのサービス（Free・Pro・Max・Ultra）に適用される。API キーと Console は商用の規約（Commercial Terms）の側
- Help Center「Age assurance on Claude」（2026-05-18）：個人向けの Claude は18歳以上だけが使える。登録のときに18歳以上であることを確かめる。18歳未満の兆候があればアカウントを止め、第三者の Yoti で年齢を確かめれば戻す（顔の写真で年齢を推定・身分証・Yoti のアプリ）。Anthropic が受け取るのは合否だけ、と書く
- Team・Enterprise・Education など商用の契約の側の年齢の条件は確かめていない

### 3.11 Max（と Ultra）の API credits

- **額**：Max $100/月、Ultra $200/月。Team は Standard $20・Premium $100 の席ごとの額を合算し、月 $500 まで。Free・Pro・Enterprise は対象外
- **受け取り**：claude.ai の Settings > Billing の API credits の欄で「Link organization」を選び、Console の組織を一つ紐付ける。契約から7日たつと受け取れる。紐付けた組織は自分では変えられず、一つの組織は一つのプランからしか受け取れない。Console にカードを登録する必要はない
- **使えるもの**：Claude Platform の全モデルで、Claude API（Messages・Message Batches）、Console の Playground、Claude Managed Agents、Claude Agent SDK
- **使えないもの**：対話の Claude Code（端末・IDE・desktop・web）、Claude・Claude Code・Cowork の extra usage（usage credits）、Bedrock・Vertex AI・Foundry の Claude
- **`claude -p` の扱い**：紐付けた組織の API キーで自分で動かすときは Agent SDK の利用として credits が使われる。プランでログインして動かすときはプランの上限から引かれる。GitHub Action・IDE 拡張・Desktop から起動したものは、`-p` でも Claude Code の利用として扱われ、credits の対象外
- **働き**：請求のたびに付与され、繰り越さない（期末に失効）。購入した credits より先に使われる。組織の全員の API キーが同じ残高から使う。プランの利用上限は変わらない。使い切って他に credits がなければ API は止まり、プランに請求されることはない
- 6月に告知された「Agent SDK の credits」とは別物で、そちらは提供されていない、と FAQ にある
- **教材と制作への影響**：検証に使うには API キーが要る。decisions（API キー）の決定のままでは、制作の検証に使えない

### 3.12 個人プランの学習への利用と保持の期間

- **対象**：Free・Pro・Max・Ultra の個人向けのアカウント（そのアカウントで使う Claude Code を含む）。Team・Enterprise・API・Gov・Education は商用の規約の側で、顧客が明示して提供しない限り学習に使わない
- **学習に使われる場合**：(1) 設定で改善への利用を許可したとき、(2) 会話が安全の審査の対象になったとき（利用ポリシーの検出と執行の改善に使う）、(3) Trusted Tester などに明示して参加したとき。使われるのは会話の全体（内容、custom styles、会話の好みの設定、Claude in Chrome のデータを含む）。connector や MCP サーバーから取った生の内容は含まない（会話に貼った分は含む）。incognito の会話は、許可していても使わない
- **設定**：Settings > Privacy の「Help improve our AI models」（`claude.ai/settings/data-privacy-controls`）。Web・Desktop・Mobile のどれでも変えられる。新しい利用者は登録のときに選ぶ（既定がオンかオフかは、公式の文書に書かれていない）。2025-08-28 の改定のとき、既存の利用者の期限は 2025-10-08 だった
- **保持の期間**（Privacy Center「How long do you store my data?」2026-07-01）
  - 会話を消すと、履歴からすぐ消え、バックエンドからは30日以内に消える
  - 改善への利用を許可すると、匿名化した形で最大5年、学習のパイプラインに残す。これは設定を有効にした後の新しい会話と再開した会話だけ
  - 設定を切ると、前の会話も新しい会話も、これからの学習には使わない。ただし、もう始まっている学習とでき上がったモデルからは取り除かれない。消した会話も、これからの学習には使わない
  - 利用ポリシーの違反と判定された会話は、入出力を最大2年、安全の分類のスコアを最大7年残す
  - 👍👎 などのフィードバックとバグの報告は5年（`/feedback`・`/bug`・`/share` も5年。Claude Code の data-usage）
  - 法令などで必要なときは、さらに残すことがある
- **書き方の違い**：Claude Code の data-usage と 2025-08-28 のお知らせは「許可すれば5年、しなければ30日」と短く書く。Privacy Center は「最大5年・匿名化・学習のパイプライン」と書く。教材は Privacy Center の書き方に合わせ、「30日」は消した会話がバックエンドから消えるまでの期間と書く
- Claude Code の手元の記録（`~/.claude/projects/` に平文で30日、`cleanupPeriodDays` で変更）は、これとは別の手元の保存である

### 3.13 そのほか見つかったこと

- **Ultra プランができた**：Max 20x は Ultra に改名された（既存の契約者は自動で移り、価格は同じ）。Ultra は月 $200（Web、月払いのみ）で週に Pro の10倍。5時間の上限は、自動で確認されたアカウントにはない（確認までは仮の上限がかかる。Settings > Usage に Current session の棒がなければ確認済み）。Max は月 $100 の1段で、5時間ごとと週ごとに Pro の5倍。Max と Ultra には Fable の別の週上限がある。Help Center の分類名も「Pro, Max, and Ultra plans」になった。いつ変わったかは Release notes に載っておらず、確かめていない（R1 の範囲と重なる）
- **Usage Policy の新しい版**：ページの表示は「Effective Nov 12, 2026」で、まだ発効していない版が出ている。変更点は読んでいない（R1 と照らす）
- **公式同士の食い違い**
  - 個人設定の記事は「project instructions は有料プランだけ」と書くが、同じ記事と Projects の記事は「Projects は Free でも使える（5個まで）」と書き、Projects の記事は project instructions の設定をプランで限っていない
  - Opus 5・5.5 のモデルの切り替えの記事（2026-09-24）は「Opus 5.5 は Cyber Verification Program でまだ使えない」と書くが、CVP の記事（2026-10 に更新）は Opus 5.5 を3段階の対象にしている。新しい CVP の記事が今の状態だと読める
  - 料金のページと Max の記事で、Fable の扱いの書き方が違う（「週上限の半分まで」と「別の週上限」）
  - M365 のページと Privacy Center の記事は、プランの一覧に Ultra を書いていない（Claude Code の data-usage と Help Center の多くの記事は Ultra を書く）。改名の後の更新が追いついていないと思われる
- **claude.ai の表示の言語**（Help Center「How to use Claude in your preferred language」）：表示の言語に日本語がある（Web・Desktop）。表示の言語を変えても、Claude は話しかけた言語で答える。音声モードの言語は別の設定（R6 の参考）

---

## 4. 提案

### 4.1 調査資料への直し

| # | ファイルと場所 | 直した文（案） |
| --- | --- | --- |
| 1 | 02 §1-3（80行） | 「- Styles：2026-06-01 に『Styles are moving to skills』が告知された。custom styles は skills に自動で移され（既定は無効。Customize > Skills で有効にする）、既定の Concise・Explanatory・Formal はなくなり、Learning は skill として残る。移行が終わると styles のメニューは消える。2026-11-03 時点で記事は取り下げられ（404）、個人設定の記事にも Styles はない（research/26 §3.1）— Internet Archive の写し（2026-07-10）」 |
| 2 | 02 §1 Gaps（356〜359行） | 各行の末尾に「→ research/26 §3.1・§3.2・§3.5・§3.6 で補った（2026-11-03）」 |
| 3 | 02 §2-1（373行） | 「- Max：月 $100（Web、月払いのみ）。5時間ごとと週ごとに Pro の5倍。旧 Max 20x は Ultra に改名された（月 $200、週に Pro の10倍、確認済みのアカウントは5時間の上限なし）。2026-11-03 確認 — What is the Max plan? / What is the Ultra plan?」 |
| 4 | 02 §2-1（374行） | 「- 月次の API credits：Max $100、Ultra $200、Team は席ごとに Standard $20・Premium $100（合算して月 $500 まで）。Claude API・Playground・Managed Agents・Agent SDK に使え、対話の Claude Code・extra usage・Bedrock などには使えない（research/26 §3.11）— Monthly API credits for Max, Ultra, and Team plans」 |
| 5 | 02 §6 Gaps（912行） | 「→ 記事は『How up-to-date is Claude's training data?』。日付は training data cutoff に当たる（research/26 §3.7）」 |
| 6 | 05 §4-7（466行） | 「許可すると保持期間は5年、許可しなければ従来通り30日」を「許可すると、設定の後の新しい会話と再開した会話を、匿名化した形で最大5年、学習のパイプラインに残す。『30日』は、消した会話がバックエンドから消えるまでの期間である。違反と判定された会話は入出力が最大2年、分類のスコアが最大7年残る。対象は Free・Pro・Max・Ultra（Claude Code を含む）— How long do you store my data?」に替える |
| 7 | 05 §4-6（462行） | 末尾に「`/share` は `/bug` の別名で、公開リンクを作る機能ではない — commands」を足す |
| 8 | 01（380行） | 末尾に「→ VS Code と JetBrains は research/26 §3.4 で補った」 |
| 9 | 01（405行） | 「大きな機能は『AskUserQuestion ツールで詳しくインタビューして→SPEC.md を書いて』」を「大きな機能は『spec が書けるまでインタビューして SPEC.md に書いて』と頼むと、Claude は選択式の質問（AskUserQuestion）で返す（2026-11-03 の文はツール名を出さない）」に替える |
| 10 | 00 分野表（291行） | 「指示の置き場所（Instructions・Project・Memory・Skills・Styles）」を「指示の置き場所（Instructions・Project・Memory・Skills。Styles は 2026-06 に skills へ移行）」に |
| 11 | 00 分野表（330行） | 「（詳細は未調査）」を「（research/26 §3.4）」に |
| 12 | 00 §7（878行） | 末尾に「八つのうち、What survives compaction 以外の七つは research/26 で補った（2026-11-03）」 |
| 13 | 10 付録A-1（379行）・11 第4節 #12（792行） | 「公式で確認：hooks の文書は1回に1〜4問、Agent SDK の文書は各問に2〜4の選択肢・header は12文字まで（2026-11-03、research/26 §3.9）」と注記 |

### 4.2 requirements への直し

- §10.4 の「公式情報で未取得のもの」の9項目に「research/26 で補った（2026-11-03）」と注記する。残る未確認（Styles のメニューが UI に出るか、Desktop の新しい設定画面での JSON の設定の入口）は §5 のとおり

### 4.3 decisions.md への反映（メインが判断し、必要なら作者に諮る）

1. **「書き方の方針（安全・面・表現）」3 の言い換えの案**：「誤って断られた正当な依頼には、公式が案内する手段だけを書く。本当の目的と文脈を足す（偽らない）、引き金になった内容を会話から外す（巻き戻し・新しい会話）、推論の全文を求める指示を外す、誤判定を報告する、専門の仕事は検証の制度（CVP・LSVP）を案内する。アプリの自動のモデル切り替えは仕組みとして説明する。分類器を避けるための言い換え・分割・偽の文脈など、利用ポリシーを回避する頼み方は書かない」。理由：公式の案内は文脈を足すこと以外も含み、それを書かないと読者が詰まる（分類器は会話全体と読み込んだ資料を見るので、文脈を足しても同じ会話では止まり続ける）。Claude Code の errors の「`--model` で変えると通ることがある」は公式の案内だが、回避と紛らわしいので、自動の切り替えの説明にとどめるのが安全と考える
2. **作者のプラン**：2026-11-03 時点で Max は月 $100 の1段になり、旧 Max 20x は Ultra になった。作者が旧 20x なら今は Ultra（確認済みなら5時間の上限がない）。ワークフローの規模（同時に16〜20体）と利用上限の見積もりに関わるので、Max か Ultra かを作者に確かめるとよい
3. **「書き方の方針（安全・面・表現）」5（IDE の拡張は「未確認」と書く）**：機能の概要は公式の文書で確かめられた（§3.4）。「公式の文書の確認日つきで概要を書き、動作は未確認と添える」に改めてよい
4. **API キー（使わない）との関係**：Max・Ultra の API credits は API キーでしか使えず、`--bare` も API キーか `apiKeyHelper` が要る。決定のままなら、どちらも制作の確認に使えない（R7 の「`claude -p` で読み込む設定を絞る方法」の検討の前提になる）。逆に、制作の環境に `ANTHROPIC_API_KEY` があると、`-p` は確認なしにそれを使って従量の課金になる。制作の前に `env | grep ANTHROPIC` と `/status` で確かめる手順を format-and-operations に足すとよい

### 4.4 数値ファイル（data/facts.yml）の候補

| 値 | 内容 | 条件 | 出典 |
| --- | --- | --- | --- |
| AskUserQuestion の質問数 | 1回に1〜4問、各問に2〜4の選択肢、header は12文字まで | Claude Code・Agent SDK。subagent では使えない | hooks、agent-sdk/user-input |
| knowledge cutoff | 現行4モデルは reliable・training とも 2026年6月。旧モデルは Help Center の一覧（training）とモデルのページ（reliable）を分けて持つ | モデルごと | Help Center 8114494、Models overview |
| 月次の API credits | Max $100、Ultra $200、Team 席ごと $20・$100（月 $500 まで） | API・Playground・Managed Agents・Agent SDK だけ | Monthly API credits の記事 |
| プラン | Max 月 $100（Pro の5倍、5時間と週）、Ultra 月 $200（週に Pro の10倍、確認済みは5時間の上限なし） | Web の価格、月払い | Max・Ultra の記事 |
| 学習を許可したときの保持 | 最大5年（匿名化、学習のパイプライン） | 個人向けプラン、設定の後の新しい・再開した会話 | Privacy Center |
| 消した会話 | 履歴からすぐ、バックエンドから30日以内 | 個人向けプラン | 同上 |
| 違反と判定された会話 | 入出力は最大2年、分類のスコアは最大7年 | 個人向けプラン | 同上 |
| フィードバック | 5年（👍👎、`/feedback`・`/bug`・`/share`） | 個人向け・Claude Code | Privacy Center、data-usage |
| incognito | 履歴・memory に残らず、学習に使わず、バックエンドに既定で30日 | 全プラン（Enterprise は保持の設定による） | Incognito の記事 |
| 共有の招待の期限 | 開かれない招待は30日で切れる | claude.ai の Web | Share a chat with specific people |
| 年齢 | 18歳以上（居住地の同意の年齢が高ければそれ） | 個人向けの規約 | Consumer Terms §2 |
| M365 の保持 | バックエンドで30日以内に消す（組織の記事の例外あり） | Claude for M365 | office-agents の各ページ |

---

## 5. 確かめていないこと

- **Styles のメニューが今も UI に出るか**：公式の文書では分からない。作者のアカウント（Web・Desktop・スマホ）で、入力欄やメニューに styles があるかを見ればすぐ分かる（作者に頼む候補）
- **Desktop の新しい設定画面での `claude_desktop_config.json` の入口**：MCP の文書は Settings > Developer の「Edit Config」と書き、Help Center はこれを旧レイアウトとして扱う。新しい画面での名前は確かめていない
- **Free で project instructions を使えるか**：Help Center の記事同士で食い違う（§3.13）
- **学習の設定の既定値**（新しい利用者の画面でオンかオフか）：公式の文書に書かれていない
- **年齢**：日本向けなど地域ごとの規約の版があるか、商用の契約（Team・Enterprise・Education）の側の年齢の条件は読んでいない
- **Usage Policy の 2026-11-12 版の変更点**：版の履歴は読んでいない（ページの履歴の一覧は取れなかった）
- **Ultra への改名の日付**と、Fable の週上限の扱い（02 §2-4 の「同じ週上限の内側」との関係）：Release notes に載っておらず、確かめていない（R1 と重なる）
- **M365 のアドインを Ultra で使えるか**：ページに Ultra の記載がない
- **Opus 5・5.5 以外のモデルの切り替えの記事**（Sonnet 5.5、Fable 5・5.1）は、存在を検索で見ただけで本文を読んでいない
- **Claude Code の `/share` の歴史**（いつ `/bug` の別名になったか）は commands の記述だけで、CHANGELOG は読んでいない
- **Google Workspace の add-on** は割り当ての外なので読んでいない
- **実際の動作**：IDE 拡張・Desktop の MCP・`ANTHROPIC_API_KEY` の確認の画面などは、指示（`claude -p` などで動かさない）に従い、一つも試していない

---

## 6. 使った量の目安

- 道具の呼び出し：約105回（Bash が大半。ファイルの読み書きを含む）
- Web 検索：5回（Styles の記事の所在で3回、チャット共有で1回、拒否の記事で1回）
- Web の取得：curl で約90件（文書の一覧の llms.txt 3件と Help Center の検索ページ6件を含む。うち404が11で、多くは Styles の記事の取り下げの確認）、Internet Archive の写し1回、noai の確認11 URL（9ドメイン）。WebFetch は0回
- かかった時間：約35分（2026-11-03 20:38〜21:10 ごろ）
