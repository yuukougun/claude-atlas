# 工程6b 担当 E3 の報告：data の直し（担当 DF）とメインの直しを確かめる

- 版：2026-11-04。確かめたもの：commit 83ad700 の差分（data/facts.yml・data/sources.yml・data/outdated-advice.yml・planning/batches/step6/data/wave1-sources.yml・tools/check_noai.py・.claude/settings.json・.github/workflows/links.yml・planning/catalog/delegate.yaml・stubs/delegate/progress-logs-for-long-jobs.md・planning/decisions.md）。指摘の元は [verify-E1.md](verify-E1.md)・[verify-E2.md](verify-E2.md)、直しの報告は [fix-DF.md](fix-DF.md)（正しいと受け取らず、ファイルと一次資料で確かめた）
- 書いたのはこのファイルだけ。git は読むだけ（show・log・status）。.claude/settings.json の deny にあるドメイン（media.defcon.org・reddit.com・reddit.sentinel-team.org ほか）は開いていない。新しく使ったドメイン（terrytao.wordpress.com・joschu.net・dl.acm.org・journals.aom.org・x.com）は、開く前に `uv run python tools/check_noai.py` で確かめた（dl.acm.org・journals.aom.org・x.com は check_noai.py の取得だけ）
- 結論：指摘11件（直す 0・直したほうがよい 2・軽い 9）。E1・E2 の「直す」4件と「直したほうがよい」10件は、作者の承認に回した E2-5 を除いて data で直っており、直した値は一次資料と合っていた。schema・出典の id・YAML の文字列に新しい誤りはなく、`check_all.py` は13段すべて通った。大きい点は、メインの補足（robots.txt の * の読み）が x.com にも当たり、2026-11-03 のユーザーの選択（主催者の公式 X で規則の版を確かめる）と食い違うこと（指摘1）と、check_noai.py が「全体を禁じて ads.txt などだけを開ける」形を黙って通すこと（指摘2）

## 1. 指摘の表

| 番号 | 重さ | 場所 | 問題 | 根拠 | 直し方の案 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | planning/decisions.md 2026-11-04「工程6b」の補足と、2026-11-03「工程2（調査の補完）の結果への回答」の「大会の規則の版」・design §6.13（418行）・guides/common.md §16（318行） | 補足の「* でサイト全体を禁じ、Anthropic のクローラに自分の組がないときも当たる」は x.com にも当たる。ユーザーの選択は「主催者の公式 X など、AI の利用を断るドメインの外の一次資料で確かめた版だけを数値ファイルに入れる」で、X を断るドメインの外として扱う。補足（メインの読み）と道具がこれと逆の判定になり、手引きのとおりに X を確かめた書き手は check_noai.py に止められる | `uv run python tools/check_noai.py https://x.com/atcoder`（2026-11-04）：robots.txt の * は「Disallow: /」「Disallow: /i/u」、AI 向けの組は Google-Extended だけ。判定は「noai あり: robots.txt で *（Anthropic のクローラも含む） にサイト全体を禁じる（資料にしない）」。research/24 の表は x.com/atcoder の投稿3件を規則の版の一次資料に挙げ、contest.yaml 328行は規則の項目を data に置く案を持つ。x.com は data の domains・deny・links.yml のどれにもない（data に x.com の出典はまだない） | 方針に関わるので、x.com に当てるかを作者に確かめる。当てるなら、x.com と twitter.com を domains（noai: true）・deny・links.yml に足し、2026-11-03 の行・design §6.13・common.md §16 を、X は使えない（版は「未確認」とリンクだけ）形に直す。当てないなら、補足の * の読みを狭めるか X を例外として書き、check_noai.py にも同じ形を入れる |
| 2 | 直したほうがよい | tools/check_noai.py の check() の whole_site（209〜212行） | ルート以外のパスの Allow が1つでもあれば「全体の禁止でない」とするので、「Disallow: /」で全体を閉じ、ads.txt・sitemap・robots.txt だけを開けるサイトを、何も言わずに通す。補足の例（PMC の /articles/）は本文を開けるもので、この形とは違う。書き手は新しいドメインをこの道具で確かめる（common.md 231行）ので、見落としがそのまま資料になる | 取得を差し替えて作り物の robots.txt で check() を動かした（取得はしていない）：「User-agent: * / Allow: /ads.txt / Allow: /app-ads.txt / Disallow: /」、「Disallow: / / Allow: /sitemap.xml」、「Disallow: / / Allow: /robots.txt」はどれも noai=False（判定「指定はない」）。最初の形は実際にあり、D4 の check_noai の記録（2026-11-04）で theregister.com の * の組がこの形（このサイトは名指しの組でも Anthropic のクローラを禁じるので、今は当たる） | 「開ける」に数える Allow から、本文でないファイル（/ads.txt・/app-ads.txt・/robots.txt・/sitemap…・/favicon.ico・/.well-known/）を除く。あるいは、Disallow: / と Allow が同じ組にあるときは「人が見て決める」と出して判定を保留する（黙って通さない）。PMC の形が当たらないままであることを試験で確かめる |
| 3 | 軽い | tools/check_noai.py 215行（* の組を当てる条件） | 「not any(a in agents for a in ANTHROPIC_AGENTS)」なので、5つのクローラのどれか1つに自分の組があると * を見ない。robots.txt では組をクローラごとに選び、自分の組のないクローラには * が当たる（RFC 9309 §2.2.1）。本体の判定は「5つのどれか1つでも全体を禁じれば当たる」なので、釣り合わない。補足の「Anthropic のクローラに自分の組がないとき」は、どちらの意味にも読める | 作り物の robots.txt で：「ClaudeBot: Disallow: /private/ ／ *: Disallow: /」「ClaudeBot: Allow: / ／ *: Disallow: /」「Claude-User: Allow: / ／ *: Disallow: /」はどれも noai=False（残りの4つのクローラは * で全体を禁じられる）。記録のある結果（E2 の141ドメイン、メインの142ドメインの根、D4 の記録）では、どちらの読みでも判定は変わらない | クローラごとに当てる（自分の組のないクローラに * を当て、1つでも全体を禁じられれば当たる）か、「5つのどれにも組がないとき」と決めるかを決め、補足の文と道具をそろえる |
| 4 | 軽い | tools/check_noai.py の whole_site と robots_txt、tests/ | 「Allow: /」を「開ける」に数えないので、「Disallow: /」と「Allow: /」が同じ組にあると全体の禁止と判定する（RFC 9309 §2.2.2 では同じ長さなら Allow が勝ち、全体を許す）。逆に「Disallow: /*」は全体の禁止に数えない（文字の一致を「Disallow: /」だけで見る。直す前からの形）。robots.txt の判定の試験がない | 「ClaudeBot: Disallow: / ／ Allow: /」は noai=True、「*: Disallow: /*」は noai=False。tests/ で check_noai.py を扱うのは test_check_pages.py の KNOWN_NOAI の字句と test_hooks.py の止めないことの確かめだけ | 「Allow: /」「Allow: /*」は全体を開けるものとして扱い、「Disallow: /*」も全体の禁止に数える。reddit・PMC・ai.robots.txt・x.com・ads.txt の形を tests/tools の試験にする |
| 5 | 軽い | tools/check_noai.py の check()（178〜187行） | ページの取得に失敗すると robots.txt を見ずに noai: null で返る（E2-2 の提案。fix-DF §5.5 でメインの作業として残っている）。media.defcon.org はこの形で判定できなかった | 取得の失敗を作って動かすと、robots.txt が ClaudeBot に Disallow: / でも `{'error': 'Remote end closed connection without response', 'noai': None}`。media.defcon.org は deny に入ったので、今は既知の noai で返る | 取得に失敗しても robots.txt を取りに行き、当たれば noai: true と出す（取得の失敗は別に出す） |
| 6 | 軽い | tools/checks/data_checks.py の「AI の利用の指定」（218行〜） | 補足は「当たるサイトの写し（第三者の写しのサイトや Internet Archive）を通して読むことも同じ扱い」とするが、検査は出典の url のホストだけを domains に引く。web.archive.org の URL の中の元の URL と、archive の欄は見ないので、断るサイトの写しの出典を足しても止まらない | いまの data の Internet Archive の写し10件の元は support.claude.com・docs.anthropic.com・code.claude.com で、当たるものはない。論文の写し2件（advait.org・gwern.net）の元の dl.acm.org・journals.aom.org も、check_noai.py で Anthropic のクローラへの指定はなかった | web.archive.org/web/<時刻>/<元の URL> の形の url と archive の欄は、元の URL のホストでも domains を引き、noai: true なら同じエラーにする（提案） |
| 7 | 軽い | data/facts.yml の rules（survives_compaction を外した暫定）と tools/gen/facts.py の比較の表 | 主のページのバッジには出なくなった（値のない属性は出さない）が、比較の表（b_compare）は、同じ表に値のある機能があると rules の欄を config.yml の null の言葉「未確認」にする。公式の表は rules を2行で答えているので、「未確認」は事実と合わない。rules を tracks に持つ第一波のページに、what-survives-compaction・promises-after-compaction・instructions-ignored がある | tools/gen/config.yml 36行 `survives_compaction: {"true": 残る, "false": 残らない, "null": 未確認}`。facts.py の feature_value は None をこの言葉にする。what-survives-compaction の tracks は compaction・claude-md・rules・auto-memory・skills（claude-md・auto-memory・skills は true） | fix-DF §5.4 の三つ目の値（例「必要なときに読み直す」）を、上の第一波のページを書く前に keys.yml と gen/config.yml に足して rules に当てる。間に合わなければ、これらのページの比較の表に rules を入れない |
| 8 | 軽い | data/facts.yml の sessions・ask-user-question・effort・advisor・wrap-up-allowance の sources | 直しで足した since（と note）の根拠の出典が、項目の sources にない。E1-13 で team-onboarding に足したのと同じ形 | sessions（since 0.2.93・2025-04-30）と ask-user-question（2.0.21・2025-10-18）は CHANGELOG と変更履歴のページによるが、cc-changelog・cc-docs-changelog がない。effort（2025-11-24）・advisor（2026-04-09）の since の note は「Platform のリリースノート」と書くが、api-release-notes がない。wrap-up-allowance の note の「CHANGELOG に Wrap-Up Allowance の行はない」も cc-changelog がない。値はどれも一次資料と合っていた（§3） | それぞれの sources に足す |
| 9 | 軽い | data/facts.yml の agent-sdk の since の note | 「SDK は Claude Code とは別のパッケージなので、Claude Code の版は書かない」は、1.0.23 の TypeScript の SDK に合わない | CHANGELOG 1.0.23「Released TypeScript SDK: import @anthropic-ai/claude-code to get started」。Migrate to Claude Agent SDK（cc-docs-agent-sdk-migration。この項目の sources にある）の表は、旧い TS/JS のパッケージ名を `@anthropic-ai/claude-code`、新しいものを `@anthropic-ai/claude-agent-sdk` と書く。別のパッケージだったのは Python の claude-code-sdk と、今の Agent SDK | 「今の Agent SDK は Claude Code と別のパッケージ（@anthropic-ai/claude-agent-sdk・claude-agent-sdk）で、雛形が要る Claude Code の版にならないので書かない（1.0.23 の TypeScript の SDK は @anthropic-ai/claude-code に入っていた）」のように直す |
| 10 | 軽い | planning/batches/step6/data/wave1-sources.yml の summary-overstates-source | 遠い出典を外したときに、ページの materials が指す出典 qiita-kmat67916008-d7586a（Kaggle画像コンペでやっていること④）も外れた（8件→2件）。fix-DF の決め方（論点が名指しする出典は残す）に合わない | materials の p12#152 は research/11 の35行「【競】K_mat は、上位解法の前提が性能を縛ることもあるので…AI の要約はこの条件を落としやすい」で、主な出典がこの記事。もう1つの materials「10 第7章（要約より原文を読む）」も、research/10 の第7章でこの記事を根拠にする。同じ p12#152 を持つ summary-overgeneralization には残っている | summary-overstates-source に qiita-kmat67916008-d7586a を戻す |
| 11 | 軽い | 記録の細部（decisions.md・data/sources.yml の domains・data/facts.yml） | (a) decisions 2026-11-04 の「当たるのは10ドメイン（…media.defcon.org を足して11）」が、data の noai: true の13（reddit.com と reddit.sentinel-team.org を含む）とずれる。(b) reddit.sentinel-team.org の note に、決める前の「作者の判断で戻してよい」が残り、続く文（補足で同じに扱う）と並ぶ。(c) reddit.com だけ url（確かめた URL）がない（schema では任意。ほかの153件は持つ）。(d) claude-in-slack の note に、下書きの報告を指す「（…。報告に提案）」が残る（fix-DF §4 で直した担当名の参照と同じ種類） | data/sources.yml 387〜395行、data/facts.yml の claude-in-slack の note の末尾 | (a) 数を13にし、reddit.com（* の形）と reddit.sentinel-team.org（写し）を挙げる。(b) 「作者の判断で戻してよい」を消す。(c) 確かめた URL（robots.txt）を足す。(d) 「報告に提案」を消す |

## 2. E1・E2 の「直す」「直したほうがよい」の確かめ

| 指摘 | 重さ | 結果 | 確かめたこと |
| --- | --- | --- | --- |
| E1-1 monitor-tool | 直す | 直っている | 目次 delegate.yaml と stub の front matter の両方に `tracks: [monitor-tool]`。`uv run python tools/make_skeleton.py --check` は「目次と stubs/ の front matter は同じ（357）」。note と照合の語（`plugin monitors`。Tools reference と CHANGELOG 2.1.310・2.1.317 にある）も直った |
| E1-2 rules | 直す | 直っている（暫定） | survives_compaction のキーがなくなり、主のページ path-scoped-rules のバッジに出ない（pages_out.py の feature_badges は、キーのある属性だけを出す）。note は公式の表（「Project-root CLAUDE.md and unscoped rules｜Re-injected from disk」「Rules with `paths:` frontmatter｜Claude Code reloads them on demand」）と合う。比較の表での出方は指摘7 |
| E1-3 computer-use | 直したほうがよい | 直っている | sources に cc-docs-desktop を足し、note に両方の出典つきで食い違いを書いた。cc-docs-desktop「Computer use is a research preview on macOS and Windows that requires a Pro, Max, or Ultra plan」、cc-docs-computer-use「a research preview on macOS」、hc-computer-use「Computer use is in beta for Pro, Max, and Ultra plans」、Platform のリリースノート 2026-08-19「out of beta on the Claude API as the `computer_toolset_20260801` toolset」。値は beta のまま、id を面で分けるかは目次の判断として残る |
| E1-4 ide-extensions | 直したほうがよい | 直っている | `VSCode`・`[VSCode]` を足した。CHANGELOG（2.1.318 まで436版）で 490行・455行に当たる |
| E1-5 cloud-providers | 直したほうがよい | 直っている | Bedrock 188・Vertex 133・Foundry 81・Mantle 21 行。`CLAUDE_CODE_USE_ANTHROPIC_AWS` は Feature availability にある |
| E1-6 code-projects | 直したほうがよい | 直っている | 一般の語がなくなった。足した6つの句は、どれも Projects の文書（cc-docs-claude-projects）にある（project threads は先頭が大文字）。CHANGELOG とリリースノートにはまだ0行 |
| E1-7 chat-search | 直したほうがよい | 直っている | Help Center のリリースノート 2025-08-11「Ability to search past conversations」「search over past chats」を、足した語で拾える |
| E2-1 hash-to-memorize の why_then | 直す | 直っている | D3.yml 229行の文に戻り、引用符で囲まれた。4つの下書きと data・wave1-sources で、引用符の外の「 #」は D3.yml 229行（直した元）だけ |
| E2-2 media.defcon.org | 直す | data は直っている。2点は残り | domains は noai: true と note、deny に2つの形、links.yml の除外。出典 defcon33-claude-ctf-scoreboard は data と wave1-sources.yml から消え、残るのは下書き D4.yml だけ（ほかの断るドメインの下書きの出典と同じ扱い）。残り：同じ講演の別の一次資料は探していない（fix-DF §5.2。執筆の時に見る。代わりになりうる anthropic-research-cyber-competitions は6ページのうち stuck-in-a-check-loop にしかない）、check_noai.py の取得の失敗（指摘5） |
| E2-3 hash-to-memorize の how_to_find | 直したほうがよい | 直っている | Interactive mode の Quick commands の表は `/`・`!`・`@`・`:`・空の入力での `?` で、`#` はない |
| E2-4 customize-tabs | 直したほうがよい | 直っている | hc-plugins-page「Free, Pro, Max, Ultra, and Team plans｜Rolling out gradually starting October 29, generally available November 9」「Enterprise｜On by default starting November 30」。hc-cowork-and-chat「Connect apps in Customize > Connectors」。サイドバーの表示で見分けることは、記事の「Customize becomes Plugins」と「one Plugins page replaces the separate … tabs」が同じ変更であることからの読み |
| E2-5 状態の見直し6行 | 直したほうがよい | 作者の承認待ち（直していないのは決まりどおり） | data の status は変わっていない。案と根拠は fix-DF §5.1 にあり、commit の記録は「試作の終わりの頼みに入れる」 |
| E2-6 wave1 の遠い出典 | 直したほうがよい | おおむね直っている | 名指しの3ページ（does-more-than-asked 22→10・how-usage-limits-work 29→23・rewind-dont-correct 20→15）から、迎合・テスト生成などの研究と、利用規約・CVP の組が外れた。章のリンクを全部拾った形の6ページも、論点が名指しする出典（Tambon et al.・Wei et al.・Peters & Chin-Yee・SimdBench・APR の幻覚の研究など）は残っていた。外しすぎ1件は指摘10。136ページの並び、出典のないページ（knowledge-map・ai-and-sources）は前と同じ |
| E2-7 Reddit の写し | 直したほうがよい | メインが外す側に決めてそろえた | 出典2件が data と wave1-sources.yml から消え、reddit.com（新しく足した）と reddit.sentinel-team.org を noai: true にし、deny と links.yml に足した。補足の読みの影響は指摘1・3・11 |

## 3. そのほか確かめたこと（指摘のないところ）

### 3.1 値を直したもの（E1・E2 の「軽い」）と一次資料

すべて 2026-11-04 に取得して照らした（CHANGELOG は raw.githubusercontent.com の本文、日付は Claude Code の変更履歴のページ）。

- **since の版と日付**：0.2.93＝2025-04-30（「Resume conversations … "claude --continue" and "claude --resume"」。/resume は 1.0.27＝2025-06-18）、2.0.21＝2025-10-18（「Added an interactive question tool」）、1.0.23＝2025-06-16（「Released TypeScript SDK」「Released Python SDK」）、2.0.0＝2025-09-29（「The Claude Code SDK is now the Claude Agent SDK」）、2.1.101＝2026-04-10（`/team-onboarding` の追加）。Platform のリリースノート：2026-04-09「We've launched the advisor tool in beta」、2025-11-24「launched the effort parameter in beta for Claude Opus 4.5」
- **claude-in-chrome**：2.0.72（2025-12-17）「Added Claude in Chrome (Beta)」、2.1.198（2026-07-01）「Claude in Chrome is now generally available」
- **wrap-up-allowance**：hc-wrap-up-allowance「You're using Claude Code version 2.1.277 or later」。CHANGELOG に Wrap-Up Allowance の行はない
- **app-skills・app-plugins**：hc-skills-use・hc-plugins「v2.1.273 or later」。CHANGELOG 2.1.275（2026-09-17）「Added syncing of the skills and plugins enabled on your claude.ai account…」、2.1.273（09-15）は同期したスキルの修正とサインインでのプラグインへのアクセスの変更
- **照合の語**：足した語は、CHANGELOG（/usage-credits 12・/extra-usage 7・usage limit 26・voice mode 27・dictation 20・Voice STT 1・Claude Desktop 75・desktop app 31・@-imports 2・CLAUDE.md imports 1・`language` setting 7・bash mode 11・shell mode 7 行）か文書（`speed: "fast"`＝Fast mode、`"citations": {"enabled": true}`＝Citations、Shell mode with `!` prefix＝Interactive mode）、Help Center（Settings > Memory・Memory from chat history・interactive connectors・Scheduled tasks in Cowork など）に出る形だった
- **volatility（E1-23）**：GA の91件が中、例外の4件（fast-mode・app-skills・app-plugins・app-tasks）と GA でない22件は既定（高）。fix-DF の決め方のとおり
- **names**：routines-to-scheduled-tasks は CHANGELOG 2.1.312（10-27）が routine の最後、2.1.314（10-30）に「Scheduled tasks page」、2.1.316（10-31）に「cloud scheduled tasks」。slack-to-claude-tag は Help Center のリリースノート 2026-06-23「Delegate work to Claude in Slack with Claude Tag」（Team and Enterprise）と hc-claude-tag「switched over to the new Claude Tag experience on August 3, 2026」。文中で names や機能の id を指す参照（20か所）は、どれも data にある
- **台帳**：名前の変更の7行は、why_then と note から改名の時期が消え（DR-18）、時期は tools/gen/ledger.py が names から引く。architecture-in-claude-md は、今の Best practices の「Every one of these was good advice when it was written. Most were workarounds…」と表の行「Describe your architecture and file layout in `CLAUDE.md`｜Claude reads the repo itself…」、写し 2026-10-26 の表（Exclude に「Anything Claude can figure out by reading code」「File-by-file descriptions of the codebase」、Include に「Architectural decisions specific to your project」）と合う。think-hard-keywords の足した文は CHANGELOG（2.1.68「Re-introduced the "ultrathink" keyword」、think hard などを外した行はない）と合う。interactive-tutorial は Prompting best practices「Starting with Claude 4.6 models … prefilled responses … return a 400 error」と Model deprecations「Removed in API version `2026-10-21`｜Returns a 400 error. Earlier API versions return it when set to a non-default value on Claude 4.7 and later models」と合い、どちらも行の sources にある。subagent-per-step の「Know what subagents cost」は写し 10-27 にだけあり、ralph-loops の `--max-turns`・`--max-budget-usd` は CLI reference にある
- **出典の属性（E2-16）**：claude.com/resources/articles の og:title は「Articles」。tao-mathematical-exploration-at-scale の新しい URL は 200 で、題は「Mathematical exploration and discovery at scale」、ページの日付は 5 November 2025（published: 2025-11-05）。schulman-opinionated-guide-ml-research の http の URL は 200 で、題は「An Opinionated Guide to ML Research」。2つの新しいドメインは check_noai.py で指定なし。写し10件の publisher「Anthropic（写し）」、github-openai-mle-bench の種類「研究」
- **日本語の語の間の空白**：features の note で消えた空白106か所は、日本語どうし、「。」「、」「・」の後、ASCII の語の後の「（」の前だけで、ASCII の語どうしがつながったところはない

### 3.2 新しい誤りの見張り

- 外した出典の id（defcon33-claude-ctf-scoreboard・reddit-snapshot-1qspcip・reddit-snapshot-1uk434i）は、data・wave1-sources.yml・stubs・docs のどこにもなく、下書き D4.yml にだけ残る。claude-blog-articles はどのページからも指されなくなった（出典は残る）
- 3つの data のファイルは schema/*.schema.json（Draft-07・FormatChecker）に誤り0。features・names・facts・台帳・wave1-sources が指す出典の id は、すべて data/sources.yml にある
- YAML の文字列：引用符の外の「 #」は data と wave1-sources にない。読み込んだ文字列で助詞などで切れたものもない（「…退役した日まで」の1件は文の終わり）
- noai: true のドメインの出典は0。Internet Archive の写しの元にも断るドメインはない（指摘6）
- data の noai: true の13ドメインは、どれも deny に2つの形（`WebFetch(domain:<d>)`・`WebFetch(domain:*.<d>)`）があり、links.yml の除外の正規表現が、根・www・大文字の URL に当たる。deny にあって data にないのは atcoder.jp・codeforces.com（KNOWN_NOAI と同じ扱い）だけ。除外は notreddit.com・defcon.org・sentinel-team.org のような近い別のドメインには当たらない。.claude/hooks/pre_tool_use.py は deny から一覧を読む（二か所に持たない）

### 3.3 check_noai.py の判定（取得を差し替えて作り物の robots.txt で動かした）

| robots.txt の形 | 判定 | 補足との関係 |
| --- | --- | --- |
| * に Disallow: /、Anthropic の組なし（reddit の形） | 当たる | 補足どおり |
| * に Disallow: / と Allow: /$・/articles/ など（PMC の形） | 当たらない | 補足どおり |
| ClaudeBot を含む組に Disallow: /（ai.robots.txt の形） | 当たる | 決定どおり |
| Googlebot だけ許し、* に Disallow: /（x.com の形） | 当たる | 補足どおり（指摘1） |
| * に Disallow: / と Allow: /$（根のページだけ） | 当たる | 補足どおり |
| * に Disallow: / と Allow: /ads.txt・/sitemap.xml・/robots.txt | 当たらない | 指摘2 |
| ClaudeBot か Claude-User だけ自分の組で許すか一部だけ禁じ、* に Disallow: / | 当たらない | 指摘3 |
| ClaudeBot に Disallow: / と Allow: / | 当たる | 指摘4 |
| * に Disallow: /* | 当たらない | 指摘4 |
| ページの取得に失敗 | 判定しない（null） | 指摘5 |

- 記録のある結果に今の判定を当て直した（取得はしていない）：E2 の141ドメイン（scratchpad/e2/noai-all.json）、メインの142ドメインの根（scratchpad/noai.json）、D4 の記録（scratchpad/d4/noai/）。前から断るとした10ドメインは今の判定でも当たり、pmc.ncbi.nlm.nih.gov は当たらない。前と判定が変わるのは x.com だけ（data にはない）

### 3.4 `uv run python tools/check_all.py`

```
通った  make_schema　通った  gen_site　通った  check_pages（エラー 0・警告 8）　通った  check_catalog
通った  check_templates　通った  check_svg　通った  textlint　通った  mkdocs
通った  tests-tools（481件）　通った  tests-site（66件）　通った  tests-hooks-python3（52件）　通った  tests-hooks（52件）　通った  tests-guides（14件）
通った 13・落ちた 0・飛ばした 0
```

- check_pages の警告8件は、data と関係のない stub の front matter（比例則3・平文の欄5）。「AI の利用の指定」「断るドメインと deny」に警告もエラーもない

## 4. 確かめていないこと

- media.defcon.org・reddit.com・reddit.sentinel-team.org の robots.txt とページ（deny のため開いていない）。domains の note の中身は E2 と fix-DF の記述による
- wave1-sources.yml の、直しで変わらなかったページ（136のうち、変わった24ページのほか）。E2 の「2〜3割混ざる6ページ」は名前が分からず、特定していない
- features の note のうち、直しで変わらなかったところ（E1 が抜き出さなかった78件の細部を含む）
- 画面と実機（Plugins のページの出方、Desktop の computer use の表示など）
- 比較の表の「未確認」（指摘7）は、作る層のコードと設定から読んだもので、ページを生成して見てはいない（第一波のページはまだ stub）

## 5. 使ったスクリプトと取得物（scratchpad）

- スクリプト：`/tmp/claude-1000/-home-yuuki-projects-kyopro2-claude-atlas/2ee2ba0e-8978-48f8-837d-c53e59939dbb/scratchpad/e3/scripts/`（cmp_facts.py：facts の前後の項目ごとの差、cmp_wave1.py：wave1 のページごとの外した id と足した id、robots_cases.py：作り物の robots.txt で check() を動かす、robots_variants.py：記録のある結果に今の判定と別の読みを当てる、cl.py：CHANGELOG の版・日付・語の数、rn.py：Platform のリリースノートの行と日付、h2t.py：HTML を文字に、yaml_cut.py・hash_scan.py：YAML の切れの見張り、space_diff.py：消えた空白の前後）
- 取得物：同じ scratchpad の `e3/dl/`（CHANGELOG と変更履歴のページ、Claude Code・Platform の文書、Help Center の記事、Best practices の写し2件、Tao と Schulman の記事）。直す前の data は `e3/old/`、check_all.py の出力は `e3/check_all.out`
