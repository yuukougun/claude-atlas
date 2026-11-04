# 工程6b 担当 DF の報告：verify-E1・verify-E2 の指摘を data に反映した

- 版：2026-11-04。指示は、メインからの依頼（工程6b の data の直し）と [brief-build.md](brief-build.md)・[brief-data.md](brief-data.md)。指摘は [verify-E1.md](verify-E1.md)（features 117件）と [verify-E2.md](verify-E2.md)（台帳・names・sources・wave1-sources）
- 書いたもの：`data/facts.yml`・`data/sources.yml`・`data/outdated-advice.yml`、`planning/batches/step6/data/wave1-sources.yml`、`stubs/delegate/progress-logs-for-long-jobs.md` の front matter（`tracks: [monitor-tool]` の1行だけ）、この報告。git は使っていない。`.claude/settings.json` の deny にあるドメイン（media.defcon.org ほか）は開いていない
- 直し方：データの YAML は、読み込んで直して同じ形（PyYAML の `safe_dump`・`allow_unicode`・`width=1000`）で書き戻した。まとめたときと同じ形で、直す前の書き戻しはバイト単位で同じになることを確かめた。文字列に「 #」や「: 」が入る値は、書き出しの側が引用符で囲む（E2-1 の形を繰り返さない）

## 1. 結果

| | 指摘 | 直した | 直さなかった |
| --- | --- | --- | --- |
| E1 | 23件（直す 2・直したほうがよい 5・軽い 16） | 21件 | 2件（E1-21・E1-22。理由は表） |
| E2 | 16件（直す 2・直したほうがよい 5・軽い 9） | 15件 | 1件（E2-5。作者の承認が要る状態の変更。提案を §5.1 に書いた） |

- 「直す」2件ずつ（E1-1・E1-2、E2-1・E2-2）はすべて直した。「直したほうがよい」のうち、直さなかったのは E2-5 だけ
- `uv run python tools/check_all.py` は13段すべて通った（§6）

## 2. E1（features）の扱い

| 番号 | 直した中身 | 一次資料で確かめたこと | 直さなかったときの理由 |
| --- | --- | --- | --- |
| E1-1 monitor-tool | ページ progress-logs-for-long-jobs の front matter に `tracks: [monitor-tool]` を足した（目次は直していない）。monitor-tool の note の「どのページも tracks に持たない」を、tracks に持つ形に直した。照合の語 `experimental.monitors` を `plugin monitors` に替えた | CHANGELOG 2.1.98（2026-04-09）「Added Monitor tool for streaming events from background scripts」。「plugin monitors」は CHANGELOG 2.1.310・2.1.317 と Tools reference の Monitor tool の節にある。`experimental.monitors` の文字は取得した資料のどこにもない（2.1.129 は「`monitors` should now be declared under `"experimental"`」） | |
| E1-2 rules | survives_compaction を省いた（true だったのを外す）。note に、paths のない rules と paths のある rules で答えが違い、真偽で言い切れないので書かない、と足した。claude-md は true のまま（入れ子の CLAUDE.md の扱いは note に書いてある） | Explore the context window の What survives compaction の表：「Project-root CLAUDE.md and unscoped rules｜Re-injected from disk」「Rules with `paths:` frontmatter｜Claude Code reloads them on demand」。表の下の文「compaction summarizes them away with everything else. If a rule must persist…」 | 三つ目の値（「必要なときに読み直す」）は schema/keys.yml と tools/gen/config.yml の直しなので触っていない。決まるまでの暫定として省いた。省くと作る層では、主のページのバッジに出ず（出す側が値のない属性を飛ばす）、比較の表では値のある機能が一緒にあれば「未確認」と出る（§5.4） |
| E1-3 computer-use | 出典に cc-docs-desktop を足し、note に食い違い（Help Center は beta、Claude Code の文書は Desktop も CLI も research preview、API は stable）を両方の出典つきで書いた。maturity は beta のまま | hc-computer-use「Computer use is in beta for Pro, Max, and Ultra plans…Cowork and Claude Code in the Claude Desktop application」。cc-docs-desktop「Computer use is a research preview on macOS and Windows…」。cc-docs-computer-use「a research preview on macOS」。API の featureMetadata は Claude API: stable、Platform のリリースノート 2026-08-19 | id を面で分ける案は、目次（features.yaml と tracks）を変えるので触っていない。分けるなら API の行は API の分野のページが主になる。note にそう書いた |
| E1-4 ide-extensions | 照合の語に `VSCode`・`[VSCode]` を足した | CHANGELOG の「[VSCode]」で始まる行 455、「VSCode」を含む行 490 | |
| E1-5 cloud-providers | `Bedrock`・`Vertex`・`Foundry`・`Mantle`・`CLAUDE_CODE_USE_ANTHROPIC_AWS` を足した | CHANGELOG の行数は Bedrock 188・Vertex 133・Foundry 81・Mantle 21。`CLAUDE_CODE_USE_ANTHROPIC_AWS` は cc-docs-feature-availability にある | |
| E1-6 code-projects | 一般の語（Projects・project・threads・thread）を外し、文書に出る句（claude-projects・project conversation・project threads・cloud threads・Overview pane・claude.ai/code/projects）にした | Claude Code の Projects の文書（cc-docs-claude-projects）に6つとも出る（project threads は先頭が大文字）。CHANGELOG と Help Center のリリースノートにはこの機能の行がまだない（0件） | |
| E1-7 chat-search | `chat search`・`past chats`・`search past conversations` を足した | Help Center のリリースノート 2025-08-11「Ability to search past conversations」「prompt Claude to search over past chats」。「chat search」は5行に出る | |
| E1-8 claude-in-chrome | note の GA の根拠を、CHANGELOG 2.1.198（2026-07-01）の行に替えた（値は GA のまま） | CHANGELOG 2.0.72「Claude in Chrome (Beta)」、2.1.198「Claude in Chrome is now generally available」 | |
| E1-9 sessions | since に `claude_code: 0.2.93`・`date: 2025-04-30` と note を足し、note の「入った版は書かない」を消した | CHANGELOG 0.2.93「Resume conversations from where you left off…--continue…--resume」、変更履歴のページの日付 2025-04-30。/resume は 1.0.27 | |
| E1-10 ask-user-question | since に `2.0.21`・`2025-10-18` と note（道具の名前を書かない追加の行）を足した | CHANGELOG 2.0.21「Added an interactive question tool」「Claude will now ask you questions more often in plan mode」 | |
| E1-11 agent-sdk | since に `date: 2025-06-16` と note を足し、出典に cc-changelog・cc-docs-changelog を足した。改名の時期は names の code-sdk-to-agent-sdk を指す形にした（時期を二か所に持たない） | CHANGELOG 1.0.23（2025-06-16）「Released Python SDK」「Released TypeScript SDK」、2.0.0（2025-09-29）「The Claude Code SDK is now the Claude Agent SDK」、2.0.25「Removed legacy SDK entrypoint」。names には 2.0.0 の改名がすでにある | since に Claude Code の版（1.0.23）は入れなかった。SDK は別のパッケージで、雛形が要る Claude Code の版にならない（メインの判断とされていた点。note に理由を書いた） |
| E1-12 advisor・effort | since に API の公開日を入れた（advisor：2026-04-09、effort：2025-11-24）。note に、Claude Code の入った版は書かないこと（CHANGELOG に導入の行がない）を足した | Platform のリリースノート 2026-04-09「launched the advisor tool in beta」、2025-11-24「launched the effort parameter in beta for Claude Opus 4.5」。CHANGELOG の advisor の最初の行は 2.1.117（改善の行）、effort は 2.1.42（callout の行） | |
| E1-13 team-onboarding | since.date を `2026-04-10` にし、出典に cc-changelog・cc-docs-changelog を足した | CHANGELOG 2.1.101「Added `/team-onboarding` command…」、変更履歴のページの日付 2026-04-10 | |
| E1-14 wrap-up-allowance | since を外し、2.1.277 は Help Center が資格の条件に書く版で、入った版ではないと note に書いた | hc-wrap-up-allowance「You're using Claude Code version 2.1.277 or later」。CHANGELOG に Wrap-Up Allowance の行は0行 | |
| E1-15 app-skills・app-plugins | note に、Claude Code への同期に要る版の食い違い（Help Center は v2.1.273、CHANGELOG は 2.1.275 で追加）を両方の版と日付つきで書き、出典に cc-changelog・cc-docs-changelog を足した | hc-skills-use・hc-plugins「needs Claude Code v2.1.273 or later」。CHANGELOG 2.1.275（2026-09-17）「Added syncing of the skills and plugins enabled on your claude.ai account…」。2.1.273 の行は同期したスキルの修正とサインインでのプラグインへのアクセスの要求 | |
| E1-16 usage-credits・usage-limits | usage-credits に `/usage-credits`・`/extra-usage`、usage-limits に `usage limit` を足した。2.1.144 の改名は names の extra-usage-to-usage-credits にすでにある | CHANGELOG の行数は /usage-credits 12・/extra-usage 7・usage limit 26。2.1.144「Renamed "extra usage" to "usage credits"…」 | |
| E1-17 desktop-code | `Claude Desktop`・`Claude Code for Desktop`・`desktop app` を足した | CHANGELOG 2.0.51「Introducing Claude Code for Desktop」（足した語で拾える）、「Claude Desktop」を含む行 75 | |
| E1-18 voice-dictation（と voice） | voice-dictation に `voice mode`・`dictation`・`Voice STT` を足し、voice と語が重なることを両方の note に書いた（点検では面で振り分ける） | CHANGELOG の行数は voice mode 27・dictation 20・Voice STT 1（2.1.69） | |
| E1-19 表記のずれた語 | monitor-tool（E1-1 と同じ）。claude-md：`@path import` を `@-imports`・`CLAUDE.md imports` に。fast-mode：`speed: fast` を文書の形 `speed: "fast"` に。language-setting：`"language"` を外し、CHANGELOG の形 `` `language` setting `` を足した。citations：文書の JSON の形 `"citations": {"enabled": true}` に。interactive-mode：`! prefix` を `bash mode`・`shell mode` に。plan-mode：model-selection の語と重なる `opusplan` を外した | `@-imports`（CHANGELOG 2行）・`CLAUDE.md imports`（1行）。API の fast mode の文書は `speed: "fast"`。CHANGELOG の `` `language` setting `` は7行。API の citations の文書の例は `"citations": {"enabled": true}`。CHANGELOG の bash mode 11行・shell mode 7行（文書は「Shell mode with `!` prefix」）。opusplan は model-selection の語にある | |
| E1-20 一般の語 | plans：Free・Pro・Max・Team・Enterprise を外し、`Free plan`・`Pro plan`・`Max plan`・`Team plan`・`Enterprise plan`・`Ultra plan` を足した（Ultra は残す）。app-memory：`memory`・`Topics` を外し `Settings > Memory`・`Memory from chat history` を足した。connectors：`Interactive` を `interactive connectors` に。app-tasks：`Scheduled` を外し `Scheduled tasks in Cowork` を足した。app-permission-modes：`Blocked` を `Connector tool permission` に。personal-instructions：`Instructions` を外した。chat-sharing：`Share` を外した。code-execution：`sandbox` を `sandboxed environment` に。interactive-mode：`Esc` を `Esc Esc`・`double-Esc`・`Esc key`・`press Esc` に。scheduled-tasks：`routine` を外した（`routines` は残す） | 足した句は Help Center のリリースノートか記事・claude.com/pricing に出る（例：interactive connectors は Help Center のリリースノート（2026-03-25）が挙げる記事の題、`Connector tool permission: "Blocked"` は hc-cowork-start、`sandboxed environment` は hc-files、Free plan・Ultra plan は claude.com/pricing）。外した語の行数は CHANGELOG で Enterprise 90・Team 58・Max 51・memory 199・Interactive 98・Scheduled 68・Blocked 58・Share 33・sandbox 122・Esc 80・routine 49 | |
| E1-21 artifacts・api-credits・otel-telemetry・usage-analytics-api | 直していない | 主のページの surfaces が機能の surfaces を含まないことは、目次（features.yaml と各ページの surfaces）を見て確かめた | ページの surfaces を足すか主のページを替えるかは目次（planning/catalog/）の判断で、この担当の書ける範囲の外。data 側で機能の surfaces を主のページに合わせると、使える面を狭めて誤る |
| E1-22 advisor・fast-mode | 直していない（値は今のままでよいと E1 も書く） | 面ごとの成熟度の違いは、advisor・fast-mode の note に両方の表記が書いてある | バッジに note の要点を添えるか、面ごとの成熟度の形を持つかは、作る層の設計の判断（E1-3 と同じ。§5.4） |
| E1-23 volatility | 一つの決め方にそろえた。成熟度が GA の機能は中、そのほか（beta・research preview・experimental・成熟度なし）は既定の高。D2 の GA 36件のうち33件に `volatility: 中` を足した。fast-mode（面で research preview が残る）と、新しい体験の展開の途中にある app-skills・app-plugins・app-tasks は既定の高のまま | 決め方の根拠は requirements §6.1（機能の使い方は月単位）と design §9.2（中は90日・数値は既定の高） | |

## 3. E2（台帳・names・sources・wave1-sources）の扱い

| 番号 | 直した中身 | 一次資料で確かめたこと | 直さなかったときの理由 |
| --- | --- | --- | --- |
| E2-1 hash-to-memorize の why_then | 下書き D3.yml の原文「2.0.70 より前は、入力の先頭に # を付けると、その行を CLAUDE.md に書き足す近道があった。」に戻した（書き出しが引用符で囲む）。D1・D2・D3・D4・wave1-sources の下書き全部で、引用符のない値の後ろに「 #」が続く行を走査し、ほかに0件であることを確かめた | CHANGELOG 2.0.70（2025-12-15）「Removed # shortcut for quick memory entry」 | |
| E2-2 media.defcon.org | domains の行を `noai: true` にし、note に robots.txt の中身（照らす担当が読んだもの）と check_noai.py が判定できなかったことと、decisions 2026-11-04 の規則を書いた。出典 defcon33-claude-ctf-scoreboard を外し、wave1-sources.yml の6ページ（four-principles・plausible-falsehoods・stuck-in-a-check-loop・blames-the-tools・allow-i-dont-know・five-questions-before-delegating）から外した。facts・台帳・names にこの id はなかった | 開いていない（deny）。robots.txt の中身は E2 の報告による。`.claude/settings.json` の deny に2つの形が入っていることと、check_pages.py の「AI の利用の指定」「断るドメインと deny」がエラー0で通ることは確かめた | 「同じ講演は別の一次資料を探す」は、していない（§7） |
| E2-3 hash-to-memorize の how_to_find | 「今の入力の記号は…だけ」を、「今の入力の記号の表（Interactive mode の Quick commands）に # はない」に替えた | Interactive mode の Quick commands の表は、`/`・`!`・`@`のほかに`:`（絵文字の短縮名）と空の入力での`?`を挙げ、`#`はない | |
| E2-4 customize-tabs | now に、展開の途中であることと、サイドバーに「Customize」が出る口座はまだ前の画面のままであることを足した。how_to_find に、どちらの画面かの見分け方と、まだ「Customize > Connectors」と書く公式の記事があることを足した。出典に hc-cowork-and-chat を足した。日付は names の customize-to-plugins にあるので、行の文には書かなかった（DR-18） | hc-plugins-page「Free, Pro, Max, Ultra, and Team plans start rolling out on October 29…generally available November 9」「Enterprise…November 30」。hc-cowork-and-chat は「Connect apps in Customize > Connectors」と今も書く | |
| E2-5 状態の変更（prefill-for-json・budget-tokens・thinking-tags・mcp-sse-transport・cowork-separate-app・tell-it-to-use-subagents） | 直していない | 6行すべての一次資料の書き方を、今日開いて確かめた（§5.1） | 台帳の状態が変わる更新は作者が承認する（design §9.4 の4）。D3 の提案3（5行）に tell-it-to-use-subagents を足した6行を、案と根拠つきで §5.1 にまとめた。承認が出たら status の値を替えるだけでよい |
| E2-6 wave1-sources.yml の遠い出典 | 名指しの4ページ：does-more-than-asked は12件（迎合・テストの生成・要約の一般化・競プロの生成・プログラムの修復などの研究）を外して10件に。how-usage-limits-work は利用規約・例外・CVP・言語の記事・Data usage・Opus 4.6 の6件を外して23件に。rewind-dont-correct は規約・例外・CVP・Constitution・Our Approach to User Safety の5件を外して15件に。keeps-stopping と how-attachments-are-read は E2-15。あわせて、同じ「章のリンクを全部拾った」形のものを、拾った履歴（D4 の収集の記録）から探して外した：not-what-i-meant 8・four-specifics 8・going-in-circles 7・uses-nonexistent-apis 2・summary-overstates-source 6・summary-overgeneralization 2。wave1-sources.yml 全体で外した参照は75（E2-2・E2-7・E2-15・E2-16 の分を含む）、足したのは4 | 外した出典は、調査資料（11 の論点の行・research/26 §3.3 と §3.13）の「主な出典」の欄と章を照らして、論点が名指しする出典でないことを確かめた（例：論点 p34#74 の主な出典は Tambon et al. で、テストの生成の論文は同じ章の隣のリンク）。論点が名指しする出典（Tambon et al.・Wei et al.・Peters & Chin-Yee・Cai et al.・Huang et al.・Jin & Chen）は残した | 136ページすべては見ていない。拾った履歴で「章のリンクだけから拾った」ものを調べた範囲に限る。残りは §7 |
| E2-7 Reddit の第三者の写し | reddit-snapshot-1qspcip・reddit-snapshot-1uk434i を sources から外し、wave1-sources.yml の4ページ（claude-md-length・choosing-parallel-modes・humans-set-the-parallel-limit・what-to-put-in-claude-md）から外した。domains の reddit.sentinel-team.org の行は残し、note に外した理由を書いた（noai は false のまま。true にすると deny が要る） | check_noai.py で reddit.com の robots.txt を見た：AI 向けの指定はなく、`*` に `Disallow: /`。写しのサイトは robots.txt がなく、meta robots もない（E2 の「noindex」は見つからなかった） | 判断が要る点：決定は Anthropic のクローラを名指しで禁じる形だけを決めている。`*` でサイト全体を禁じるドメインの写しも同じに扱うかは、メインか作者の判断。保守側（外す）に倒した。戻すなら D4.yml の2件を sources に戻し、wave1-sources.yml の4ページに足す（§5.2） |
| E2-8 名前の変更の行の時期の重なり | name を指す6行（code-on-the-web-remote・routines-name・slash-cost-and-stats・fork-to-branch・workflow-keyword-extra-usage・max-5x-or-20x）の why_then を「以前は…」にし、時期を書かない文にした。code-on-the-web-remote と workflow-keyword-extra-usage の行 note の時期も names を指す形にした。commands-directory と removed-commands の changed の note から、names にある時期（1.0.25・/vim の 2.1.92）を外した。commands-directory の why_then の「1.0.25 より前」も同じに直した | 時期の値そのものは names と一致していることを、CHANGELOG（1.0.25・2.1.77・2.1.92・2.1.144・2.1.154・2.1.160）で確かめた | |
| E2-9 names の routines-to-scheduled-tasks | note を「2.1.312（2026-10-27）まで routine と書き、2.1.314（10-30）から Scheduled tasks（ページの名前）と書き、2.1.316（10-31）から cloud scheduled task と書く」に直した | CHANGELOG：2.1.312「Added an effort level to the model picker when you create or edit a routine」、2.1.314「Added an Include completed button to the Scheduled tasks page」、2.1.316「cloud scheduled tasks」 | |
| E2-10 names の slack-to-claude-tag | note に、Claude Tag の公開（Help Center のリリースノート 2026-06-23、Team と Enterprise）を足し、出典に hc-release-notes を足した | Help Center のリリースノート 2026-06-23「Delegate work to Claude in Slack with Claude Tag」。hc-claude-tag「switched over to the new Claude Tag experience on August 3, 2026」 | |
| E2-11 architecture-in-claude-md の why_then | 公式の文に推測を続けていた形をやめた。公式が書くこと（どれも当時はよい助言で、多くは回避策）、この行がどの回避策かは公式が書かないこと、ここでの推測は推測と分かる書き方、改稿の前の版（写し）の内容、の順にした | 現行の Best practices の「What you can stop doing」の表（「Claude reads the repo itself. Only write down what isn't in there.」）。sources にすでにある Internet Archive の写し 2026-10-26 の CLAUDE.md の表：Exclude に「Anything Claude can figure out by reading code」「File-by-file descriptions of the codebase」、Include に「Architectural decisions specific to your project」 | |
| E2-12 think-hard-keywords | why_then に「段階のキーワードがいつ外れたかは一次資料に版の記述がない。変わった時期に書いた 2.1.68 は ultrathink だけが戻った版である」を足した（台帳の生成の道具は changed の note を出さないので、出す欄に書いた） | CHANGELOG 2.1.68「Re-introduced the "ultrathink" keyword」。think hard などを外した行は0件 | |
| E2-13 interactive-tutorial の now | 「prefill や temperature を 0 にする呼び方は今のモデルでは 400 エラー」を、prefill は Claude 4.6 以降、temperature は Claude 4.7 以降のモデルか API の版 2026-10-21、と条件を書いた | Migrating to API version 2026-10-21「returns a 400 error, even at the parameter's default value」。Model deprecations「Earlier API versions return it when set to a non-default value on Claude 4.7 and later models」。Prompting best practices「Starting with Claude 4.6 models…prefilled responses…return a 400 error」 | |
| E2-14 台帳の行の出典 | subagent-per-step に wb-cc-best-practices-2026-10-26・-10-27 を、ralph-loops に cc-docs-cli-reference を足した | 「Know what subagents cost」の節は 2026-10-27 の写しにだけある。CLI reference に `--max-turns`・`--max-budget-usd` がある | |
| E2-15 wave1-sources.yml の要の出典 | keeps-stopping に cc-docs-permission-modes・api-docs-prompting-best-practices を足した。how-attachments-are-read に api-docs-files を足し、遠い4件（api-docs-compaction・api-docs-prompt-caching・hc-memory・hc-personalization）を外した。block-with-exit-2 に cc-docs-hooks-guide を足し、cc-docs-costs を外した | ページの sections（権限モード・提案か実行かの伝え方、API で渡すとき、フックの書き方）と、足した出典の中身 | |
| E2-16 sources の属性 | claude-blog-articles の題名を実際の「Articles」にして note に一覧のページであることを書き、2ページの一覧から外した。github-openai-mle-bench の種類を研究に。Internet Archive の写し10件の発行者を「Anthropic（写し）」に。tao-…と schulman-… は元の URL（terrytao.wordpress.com の記事、joschu.net の記事。後者は http）に替え、domains に terrytao.wordpress.com・joschu.net を足した | claude.com/resources/articles の og:title は「Articles」。2つの新しいドメインは check_noai.py で確かめた（どちらも noai・noimageai の指定なし）。記事を開き、題名が一致することを確かめた（Tao：2025-11-05 の投稿） | |

## 4. 指摘の番号のないもの（ついでに直したこと）

- **日本語の語の間の余分な空白**（E2「範囲の外で気づいたこと」）：features の note の、下書きで折った行をつないだときの空白を105か所なくした（日本語どうし、「。」「、」「・」の後、ASCII の後の「（」の前）。台帳・names・domains・sources にはなかった（sources の題名3件と URL の後の「 ）」は元の題名・書き方のまま）
- **下書きの担当名が残った参照**：features の note に「D1 の code-projects」のように担当名が残っていた5か所（scheduled-tasks・projects・voice・adaptive-thinking・connectors）を、項目の id に直した

## 5. 提案・作者の承認が要るもの・判断を残したもの

### 5.1 台帳の状態の見直し（E2-5。作者の承認に回す）

D3 の提案3の5行に、E2 の指摘の tell-it-to-use-subagents を足した6行。一次資料は 2026-11-04 に開いて確かめた。状態の定義は research/00 §5（撤回＝使えないか使うべきでない、置換＝正式な仕組みに置き換わった、条件付き＝今も効くが前提が変わった）

| 台帳の id | 今の状態 | 案 | 一次資料で見たこと |
| --- | --- | --- | --- |
| prefill-for-json | 撤回 | 置換 | Prompting best practices「Migrating away from prefilled responses」：4.6 以降は最後のターンの prefill が 400 エラー、「Earlier models continue to support prefills」。移行先は structured outputs（形を守らせる機能） |
| budget-tokens | 撤回 | 置換 | Extended thinking の文書「deprecated. Claude 4.7 and later models do not support it」「Manual mode remains useful when your workload requires predictable latency or precise control」。リリースノート 2026-02-05「Effort replaces budget_tokens…on new models」 |
| thinking-tags | 撤回 | 置換か条件付き | Prompting best practices「Manual chain-of-thought (CoT) prompting as a fallback」：思考を切ったときは今も、考えさせて答えを `<answer>` に書かせてよい。一方、Fable 5.1・Opus 5.5・Opus 5・Sonnet 5.5 では `<thinking>` に推論を書かせる頼み方は断られうる |
| mcp-sse-transport | 撤回 | 置換 | Claude Code の MCP の文書「The SSE transport is deprecated. Use HTTP servers instead」。ただし HTTP を先に試して SSE に切り替える（CHANGELOG 2.1.265）ので、SSE しか出さないサーバーにも今もつながる |
| cowork-separate-app | 撤回 | 条件付き | hc-cowork-and-chat「The new Claude experience is rolling out gradually…On Team plans (in beta) and Enterprise plans, it's available where Chat and Cowork unified is turned on」。前の体験のアカウントが残る |
| tell-it-to-use-subagents | 条件付き | 撤回 | Best practices の「What you can stop doing」の表「Delegate to a subagent for a better answer｜Handing the same task to a subagent doesn't make the answer any better. A fresh reviewer does help…」 |

- 承認が出たら、`data/outdated-advice.yml` の status を替えるだけでよい（now・why_then は、条件が書いてあるので足りている）
- 確かめ直す日：Plugins のページの一般提供（11-09）と Enterprise（11-30）の後に customize-tabs・cowork-separate-app（D3 の提案5）

### 5.2 メインか作者の判断を残したもの

- **Reddit の写し**（E2-7）：外した。戻すなら、D4.yml の2件を data/sources.yml に戻し、wave1-sources.yml の4ページに足す。決定を `*` でサイト全体を禁じるドメインにも広げるかは、決まっていない
- **DEF CON の講演の代わりの出典**：6ページから出典が1つ減った。同じ講演の話は、Anthropic の公式の研究の記事（anthropic-research-cyber-competitions。verifier-defines-problem と stuck-in-a-check-loop にすでにある）で足りるかを、執筆の時に見る（講演の個々の値が同じ記事にあるかは確かめていない）

### 5.3 目次・front matter（メインの作業）

- **E1-1 の目次側**：`planning/catalog/delegate.yaml` の progress-logs-for-long-jobs に `tracks: [monitor-tool]` を足すと、`uv run python tools/make_skeleton.py --check` の差（いまは「tracks: 目次（なし）・stub [monitor-tool]」の1件）がなくなる。足さないまま `make_skeleton.py --force` を流すと、stub の tracks が消える
- **E1-3 と E1-21**：computer-use を面で分けるか、artifacts・api-credits・otel-telemetry・usage-analytics-api の主のページの surfaces を足すか（目次の判断）

### 5.4 作る層・schema（メインの作業）

- **E1-2**：schema/keys.yml の survives_compaction に三つ目の値（例：「必要なときに読み直す」）を足し、tools/gen/config.yml の表示の言葉も足してから rules に当てる。足すまで rules は省いてある（比較の表では、値のある機能が一緒にあれば「未確認」と出る）
- **E1-3・E1-22**：面やモデルで成熟度が違う機能（computer-use・advisor・fast-mode）のバッジに note の要点を添えるか、面ごとの成熟度の形を持つか
- **E1-14**：バッジの「入った版」と、Help Center が資格の条件に書く「要る版」を区別する欄を持つか（wrap-up-allowance は since を外した）

### 5.5 検査・道具（メインの作業）

- **E2-1**：data/ と data/sources.d/ で、引用符のない値の後ろに「 #」が続く行（YAML が注釈と読んで文を切る形）を見つける検査を、check_pages.py の data の検査に足す。data の本文には注釈の行がないので、本文にある行頭以外の「 #」をすべて疑ってよい。schema の検査・textlint・check_pages はこの形を通す
- **E2-2**：tools/check_noai.py は、ページの取得で接続を切られると robots.txt を見ずに返る。取得に失敗しても robots.txt は判定する形にするとよい

## 6. check_all.py の結果

`uv run python tools/check_all.py`（直した後）：

```
通った  make_schema　通った  gen_site　通った  check_pages（エラー 0・警告 8）　通った  check_catalog
通った  check_templates　通った  check_svg　通った  textlint　通った  mkdocs
通った  tests-tools（481件）　通った  tests-site　通った  tests-hooks-python3　通った  tests-hooks　通った  tests-guides
通った 13・落ちた 0・飛ばした 0
```

- check_pages の警告8件は、data と関係のない stub の front matter（直す前と同じ8件）
- 別に、3つの data ファイルを schema/*.schema.json に jsonschema（Draft-07・FormatChecker）で当てて誤り0、features・names・台帳・wave1-sources が指す出典の id がすべて data/sources.yml にあること、外した3つの id がどこにも残っていないこと、出典のホストがすべて domains にあり noai のドメインの出典が0であること、wave1-sources.yml が136ページを同じ並びで持つこと（出典のないページは knowledge-map と ai-and-sources の2つのまま）を確かめた

## 7. 確かめていないこと

- **media.defcon.org の robots.txt**：開いていない。中身は E2 の報告による。check_noai.py は今も判定できない
- **wave1-sources.yml の残り**：外す作業は、名指しの5ページと、拾った履歴で「章のリンクを全部拾った」ものを調べた範囲（11の論点の章から拾った分）に限る。D4 の収集の記録で、論点が名指しする出典かどうかを、arXiv の番号と題名で照らした。名指しかどうかを自動では決められない出典（arXiv でないもの）は、ページの主題と題名を見て手で選んだ。研究の節をまるごと拾ったほかの形（00 の節、research/22〜28 の節）で、主題から遠い出典が残るページがありうる。E2 の抜き出し20ページの「2〜3割混ざる6ページ」は、ページの名前が報告になく、全部は特定できていない
- **E1-6 の新しい語**：Claude Code の Projects の機能は、CHANGELOG と Help Center のリリースノートにまだ行がないので、足した語が実際の変更の行を拾うかは確かめられていない（文書に出る形で持った）
- **照合の語の数え方**：行数は語の境界で大文字と小文字を区別せずに数えた（E1 と同じ仮の数え方）。点検の skill の照らし方（部分一致・句）が決まると、E1-19・E1-20 の語の選び方は変わりうる
- **features の note の細部**：E1 が照らしていない78件の note の利用条件・既定値は、今回も見ていない
- **画面・実機**：Claude Code とアプリを動かしていない（Plugins のページの出方、styles のメニューなど）
- **Internet Archive**：新しい写しは作っていない。sources にすでにある写し2件（Best practices 2026-10-26・10-27）を読んだだけ

## 8. 使ったスクリプトと取得物（scratchpad）

- スクリプト：`/tmp/claude-1000/-home-yuuki-projects-kyopro2-claude-atlas/2ee2ba0e-8978-48f8-837d-c53e59939dbb/scratchpad/fix-df/scripts/`（yio.py：読み書き、fix_facts.py・fix_advice.py・fix_sources.py・fix_wave1.py：直し、validate.py：事後の確認、cl.py：CHANGELOG の検索、prov.py：wave1 の拾った履歴の照らし合わせ、cmp.py：前後の比較）
- 取得物：同じ scratchpad の `fix-df/dl/`（CHANGELOG と変更履歴のページ、Claude Code・Platform の文書、Help Center の記事、Internet Archive の既存の写し）。直す前のファイルは `fix-df/orig/`
