# 工程6b 担当 E2 の報告：data を出典と照らす（台帳・names・sources・wave1-sources）

- 版：2026-11-04。指示は、メインからの依頼（工程6b の E2）と [brief-data.md](brief-data.md)。書いた担当の報告 [data-D3.md](data-D3.md)・[data-D4.md](data-D4.md) は手がかりにだけ使い、値はファイルと一次資料で確かめた
- 照らしたもの：data/outdated-advice.yml の37行、data/facts.yml の names の19件、data/sources.yml（domains 151・sources 534 から抜き出し）、planning/batches/step6/data/wave1-sources.yml（136ページから抜き出し）
- 書いたのはこのファイルだけ。data/ と下書きは直していない。git は使っていない。AI の利用を断るドメイン（.claude/settings.json の deny）は開いていない

## 1. 指摘の表

| 番号 | 重さ | 場所 | 問題 | 一次資料で見たこと | 直し方の案 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直す | data/outdated-advice.yml の hash-to-memorize の why_then（33行） | 文が「2.0.70 より前は、入力の先頭に」で切れている。下書き D3.yml の229行の値は引用符がなく「 # 」を含むので、YAML がそこから後ろを注釈として読んだ。schema の検査・textlint・check_pages.py はどれも通る。ほかの下書き（D1・D2・D4）に同じ形の行はなかった | CHANGELOG 2.0.70「Removed # shortcut for quick memory entry (tell Claude to edit your CLAUDE.md instead)」 | 値を引用符で囲み、D3 の文に戻す：`'2.0.70 より前は、入力の先頭に # を付けると、その行を CLAUDE.md に書き足す近道があった。'`。あわせて、data/ と sources.d/ で「引用符のない値の後ろに ' #' が続く行」を見つける検査を check_pages.py の data の検査に足すとよい（提案） |
| 2 | 直す | data/sources.yml の domains の media.defcon.org（309行）と sources の defcon33-claude-ctf-scoreboard（3626行）、wave1-sources.yml の6ページ | robots.txt が Anthropic のクローラにサイト全体を禁じているのに、noai: false のまま出典が残っている。domains の note のとおり check_noai.py はページの取得で接続を切られ、robots.txt を判定していない（D4 は meta と X-Robots-Tag だけを見た） | 2026-11-04 に https://media.defcon.org/robots.txt を直接読んだ：ai.robots.txt の一覧の User-agent の組（anthropic-ai・Claude-Web・ClaudeBot を含む）に「Disallow: /」。check_noai.py は今も「Remote end closed connection without response」で判定できない。check_noai.py の check() は、ページの取得に失敗すると robots.txt を見ずに返る | decisions 2026-11-04 の規則のとおりにする：domains を noai: true にして note に robots.txt の中身を書く、deny に2つの形で足す、出典を消し、wave1-sources.yml の four-principles・plausible-falsehoods・stuck-in-a-check-loop・blames-the-tools・allow-i-dont-know・five-questions-before-delegating から外す（同じ講演は別の一次資料を探す）。check_noai.py は、ページを取得できなくても robots.txt を判定する形に直すとよい（提案）。なお、この出典の lang: ja は字幕のファイル（.eng.txt）と合わない |
| 3 | 直したほうがよい | hash-to-memorize の how_to_find | 「今の入力の記号は、先頭の /（コマンドとスキル）と !（シェル）、ファイルを指す @ だけ」の「だけ」が文書と合わない | Interactive mode の Quick commands の表は、/・!・@ のほかに「:（絵文字の短縮名）」と「空の入力での ?（ショートカットの一覧）」を挙げる。# はない | 「今の入力の記号の表（Quick commands）に # はない」のように、# がないことだけを書く |
| 4 | 直したほうがよい | customize-tabs の now | 「サイドバーの名前は「Plugins」になり…」と、全員が変わったように書いている。2026-11-04 は展開の途中 | Help Center「Manage plugins, skills, and connectors from one Plugins page」：Free・Pro・Max・Ultra・Team は 10-29 から順に展開して 11-09 に一般提供、Enterprise は 11-30 から既定で有効。「Claude Cowork and chat are one Claude」は今も「Connect apps in Customize > Connectors」と書く | cowork-separate-app の行と同じく、展開中であることと、サイドバーに「Customize」が出るアカウントは前の画面のままであることを足す。11-09 と 11-30 の後に確かめ直す（D3 の提案5） |
| 5 | 直したほうがよい（状態の変更なので作者の承認が要る。design §9.4 の4） | 状態：prefill-for-json・budget-tokens・thinking-tags・mcp-sse-transport・cowork-separate-app（どれも撤回）と tell-it-to-use-subagents（条件付き） | 一次資料の書き方が、research/00 §5 の状態の定義（撤回＝使えないか使うべきでない、置換＝正式な仕組みに置き換わった、条件付き＝今も効くが前提が変わった）と合わない | prefill：Prompting best practices は structured outputs を形を守らせるための機能として勧め、4.6 より前のモデルは今も prefill を受け付けると書く。budget_tokens：2026-02-05 のリリースノート「Effort replaces budget_tokens for controlling thinking depth on new models」、Extended thinking は手動の思考しかないモデルでは今のままでよいと書く。thinking タグ：Prompting best practices が「Manual chain-of-thought (CoT) prompting as a fallback」（思考を切ったとき、答えを answer タグに書かせる）を今も挙げる。SSE：MCP の文書は非推奨と書くが、Claude Code は HTTP の後に SSE へ切り替えて今もつなぐ。cowork：展開中で、前の体験のアカウントが残る。subagent：Best practices の「What you can stop doing」が「Delegate to a subagent for a better answer」を、答えはよくならないとして挙げる | 案：prefill-for-json・budget-tokens・mcp-sse-transport を置換、thinking-tags を置換か条件付き、cowork-separate-app を条件付き、tell-it-to-use-subagents を撤回。D3 の提案3（5行）に tell-it-to-use-subagents を足して作者に回す |
| 6 | 直したほうがよい | wave1-sources.yml（抜き出した20ページ） | ページの主題から遠い出典が多く混ざるページがある。節の単位で拾うこと（D4 §3.4）と、名前で拾うことによる | 20ページのうち、主題に合う（遠いものが2件まで）10、遠いものが2〜3割混ざる6、目立って合わないか要の出典が欠ける4（does-more-than-asked・how-usage-limits-work・keeps-stopping・how-attachments-are-read）。目立つ例：does-more-than-asked（過剰設計）の22件のうち13件ほどが、迎合（SycEval・TRUTH DECAY・Challenging the Evaluator）、テストの生成、要約の一般化、競技プログラミングの生成、プログラムの修復の論文。how-usage-limits-work（利用上限）に Usage Policy（anthropic-legal-aup）・Exceptions to our Usage Policy・Cyber Verification Program・How to use Claude in your preferred language・Data usage が入る（research/26 §3.13 の節をまるごと拾ったもの。同じ組が rewind-dont-correct にも入る） | 執筆者に渡す前に、明らかに遠いもの（上の例）を外すか、ページごとに「節から拾った出典」の印を付けて主な出典と分ける。少なくとも how-usage-limits-work と rewind-dont-correct から利用規約と CVP の組を外す |
| 7 | 直したほうがよい（メインか作者の判断） | sources の reddit-snapshot-1qspcip・reddit-snapshot-1uk434i（reddit.sentinel-team.org。wave1 の claude-md-length・choosing-parallel-modes・humans-set-the-parallel-limit・what-to-put-in-claude-md が指す） | 元のサイトがクローラにサイト全体を禁じているのに、第三者の写しを出典にしている | reddit.com の robots.txt は「User-agent: *」に「Disallow: /」で、Public Content Policy を指す。check_noai.py は AI 向けのクローラの名前がないので「指定はない」と判定する。写しのサイトは meta robots が noindex | decisions 2026-11-04 は、Anthropic のクローラを名指しして禁じる形だけを決めている。「*」でサイト全体を禁じるドメインと、その写しを同じに扱うかを決めてほしい（H1 の理由の文は、写しを通して読むことも同じ扱いと書く）。同じに扱うなら2件を外す |
| 8 | 軽い | 名前の変更の行の why_then（code-on-the-web-remote・routines-name・slash-cost-and-stats・fork-to-branch・workflow-keyword-extra-usage・max-5x-or-20x）と、commands-directory・removed-commands の changed の note | 名前の変更の時期（版・日付）を、names に加えて行の文にも書いている。DR-18 の「二か所に持たない」に外れ、names を直したときに文が取り残される | 書き方の問題（時期の値そのものは names と一致していた） | 「改名の前は…」のように時期を書かない文にし、時期は names から道具が出す形に任せる |
| 9 | 軽い | names の routines-to-scheduled-tasks の note | 「CHANGELOG は 2.1.310（2026-10-23）まで routine と書き、2.1.316（10-31）から cloud scheduled task と書く」が CHANGELOG と合わない | CHANGELOG は 2.1.311 と 2.1.312（10-27）も routine と書き、2.1.314（10-30）から Scheduled tasks と書く（cloud scheduled task の語は 2.1.316 から） | 「2.1.312（10-27）まで routine と書き、2.1.314（10-30）から scheduled tasks と書く」に直す |
| 10 | 軽い | names の slack-to-claude-tag | 時期が 2026-08-03 だけで、Claude Tag が公開された日が分からない | Help Center のリリースノート 2026-06-23「Delegate work to Claude in Slack with Claude Tag」（Team と Enterprise）。「What is Claude Tag?」は、Claude in Slack が 08-03 に Claude Tag の体験に切り替わったと書く | note に 06-23 の公開を足し、sources に hc-release-notes を足す |
| 11 | 軽い | architecture-in-claude-md の why_then | 「リポジトリを自分で読んで全体をつかむことも、その 1 つだった」は公式の文にない推測で、前の文「公式は…とする」に続くので公式の主張に読める | 改稿前の写し（10-26）は、CLAUDE.md に書かないものに「Anything Claude can figure out by reading code」「File-by-file descriptions of the codebase」を、書くものに「Architectural decisions specific to your project」を挙げていた | 推測と分かる書き方にするか、根拠を足す。改稿前もファイルごとの説明は勧めていなかったことを書くと、助言の出どころが正確になる |
| 12 | 軽い | think-hard-keywords の changed | 2.1.68（2026-03-04）は ultrathink を「戻した」版で、think hard などの段階が終わった版ではない。今の生成の道具は changed の note を出さないので、読者には 2.1.68 で段階が終わったように見える | CHANGELOG 2.1.68「Re-introduced the "ultrathink" keyword to enable high effort for the next turn」。段階を外した行は CHANGELOG にない（D3 の報告 §5 と同じ） | approx を付けるか、now か why_then に「2.1.68 の時点では…」と書く。D3 の提案4（note を出す）でもよい |
| 13 | 軽い | interactive-tutorial の now | 「temperature を 0 にする呼び方は、今のモデルでは 400 エラーになる」は広すぎる | Migrating to API version 2026-10-21 と Model deprecations：版 2026-10-21 では既定の値でも 400、それより前の版では Claude 4.7 以降のモデルが既定以外の値で 400。Sonnet 4.6 は古い版なら受け付ける | 「Claude 4.7 以降のモデルか、API の版 2026-10-21 では」と条件を書く（lower-temperature の行と同じ書き方） |
| 14 | 軽い | 台帳の行の sources | 文の主張の出典が sources にない行がある | subagent-per-step の until 2026-10-27 は Best practices の改稿（写し）によるが、wb-cc-best-practices-2026-10-26・-10-27 がない（「Know what subagents cost」の節は 10-27 の写しから出てくる）。ralph-loops の --max-turns・--max-budget-usd は CLI reference にあるが、cc-docs-cli-reference がない | それぞれ sources に足す |
| 15 | 軽い | wave1-sources.yml の keeps-stopping・how-attachments-are-read・block-with-exit-2 | ページの節の要の出典が一覧にない（materials がその出典を含む節を指していないため） | keeps-stopping の「権限モード」「提案か実行かの伝え方」に当たる cc-docs-permission-modes と api-docs-prompting-best-practices は data にあるが一覧にない。how-attachments-are-read の「API で渡すとき（Files API・PDF・画像）」に当たる api-docs-files（D2）がない。block-with-exit-2 に cc-docs-hooks-guide がない（逆に cc-docs-costs は遠い） | 一覧に足す（materials の節にない出典でも、data にあって主題に当たるものは渡す） |
| 16 | 軽い | sources の属性（抜き出した50件と、写しの出典） | 題名・種類・写しの扱いに小さな食い違いがある | claude-blog-articles は記事の一覧のページ（題は「Articles」）で、題名「Claude blog」と合わず、出典としても弱い（where-your-data-goes・rereads-whole-history が指す）。github-openai-mle-bench はベンチマークの公開物で、種類は研究のほうが合う。Internet Archive の写し（wb-…・hc-styles-to-skills）の publisher は「Anthropic」で、D4 の写しの書き方（「…（写し）」）と違う。tao-mathematical-exploration-at-scale と schulman-opinionated-guide-ml-research は写しを出典にしているが、元のサイトが開ける（terrytao.wordpress.com、http://joschu.net/blog/opinionated-guide-ml-research.html。どちらも check_noai.py で指定なし。joschu.net は https では時間切れ、http では 200） | 題名と種類を直す。写しの publisher の書き方をそろえる。元が開けるものは元の URL にする（D4 §3.1 の決まり。joschu.net は domains に足す） |

## 2. 確かめたこと（指摘のないところ）

### 2.1 台帳の37行

- 照らした一次資料（すべて 2026-11-04 に取得）：GitHub の CHANGELOG（raw。2.1.318 まで436版）、公式の changelog のページ（版ごとの日付の表を作り、行と names に出てくる版の日付をすべて照らした）、code.claude.com の文書23ページ（.md）、Claude Platform の文書12ページ（.md）、Help Center の記事13件、claude.com の3ページ、GitHub（チュートリアルの README と第0章・第5章、claude-code-action の移行の手引きと v1 の公開の日時）、MCP の仕様 2025-03-26 の変更点、Internet Archive のすでにある写し8件（Best practices 10-26・10-27、クラウドセッション 07-03・07-06・09-10・09-17、routines 10-19・10-21）と、取り下げられた Styles の記事の写し（2026-07-10。元の URL は 404）
- 指摘の1〜5・8・11〜14 のほかは、今どうするか・変わった時期と版・かつてなぜ正しかったか・見つける方法が一次資料と合っていた。主なもの：
  - 版と日付：行と names に出てくる版（0.2.x を除く）の日付は、どれも公式の changelog のページと一致した。0.2.x の日付（2025-04-02 にそろう）を入った日に使っていないことも確かめた
  - 改稿の境：Best practices の「What you can stop doing」の表は 10-26 の写しになく 10-27 の写しにある。改稿前の写しには、守られない1行にだけ IMPORTANT を付ける勧め、窓がすぐ埋まるという前提、調べものはサブエージェントに任せる勧めがあった（important-caps・save-context-for-200k・subagents-to-save-context の why_then のとおり）
  - 公式同士の食い違いの記録：auto モードで始まる境を、文書は 2.1.283、CHANGELOG は 2.1.284（すべてのプランと提供元）と書く。approve-everything-first の note は両方を書いている（brief §3 の決まりのとおり）
  - 細部：/doctor がコードから分かる中身を削る案を出すこと、/agents が今は案内の文だけを出すこと、/pr-comments の削除が文書だけにあり CHANGELOG にないこと、自動の継続が3回で止まること、確認済みの Ultra の口座は Settings > Usage に Current session の棒が出ないこと（Ultra の記事にある）、auto mode on・manual mode on の表示、--allow-dangerously-skip-permissions のフラグ、temperature の扱い（版 2026-10-21）などは文書のとおりだった
- 状態の数（撤回16・置換14・条件付き7）、changed を持つ行30・name を持つ行7、行の id と並びが registry の ledger と同じことは、D3 の報告のとおりだった。題名の違いは表記（バッククォートを外す、用語集の語にする）だけだった

### 2.2 names の19件

- 今の名前・旧名・変わった時期を、19件すべて一次資料で照らした（CHANGELOG・公式の changelog のページ・文書・Help Center・リリースノート・ブログの編集の注・Internet Archive の写し）。指摘の9・10 のほかは合っていた。写しで絞った時期（cloud セッションの題 09-10〜09-17、--remote から --cloud 07-03〜07-06、routines の題 10-19〜10-21）は、写しの題名と本文で確かめた。CHANGELOG の区分の名前（2.1.281 まで Claude Code on the web、2.1.282 から Cloud sessions）も note のとおりだった
- DR-18：name を持つ台帳の7行は、どれも names の正しい id を指す（code-on-the-web-remote → web-to-cloud-sessions など）。行の note が挙げる names の id（default-to-manual-mode・vim-to-editor-mode・project-prefix-removed・workbench-to-playground・remote-to-cloud-flag・extra-usage-to-usage-credits）も、すべて names にある。names の feature はどれも features にあり、当て先の機能も名前の変更に合っていた（workbench-to-playground だけ当たる機能がない）
- 第三者：台帳と names の文に、個人や記事を否定的な文脈で名指しするところはなかった

### 2.3 sources と domains

- 抜き出した50件（公式文書14・公式ブログ5・リリースノート1・研究10・実践者13・報道7。台帳と names の出典は除いて無作為に）：50件すべて HTTP 200 で、どれも転送なしに data の url のまま開けた。題名は49件が title・og:title・h1 のどれかと合った（合わない1件は指摘16）。種類・言語・発行の日に大きな食い違いはなかった（指摘16 のほか）。台帳と names の出典も、ほぼすべてを開いて読んだ
- domains：出典のホストは、どれも domains に同じ名前で記録があり、確かめた日と結果がある。noai: true でない141ドメインの確かめた URL を、`uv run python tools/check_noai.py --json` で取り直した：noai・noimageai の指定はなかった。robots.txt で Anthropic のクローラにサイト全体を禁じるのは media.defcon.org だけ（道具が判定できず、robots.txt を直接読んで分かった。指摘2）。github.com（一部のパスと Bytespider）・zenn.dev（Bytespider）・ringling.libguides.com（Anthropic 以外の4つ）・pmc.ncbi.nlm.nih.gov（* に Disallow: / があるが /articles/ などを Allow）は、決定の範囲の外で使ってよい形だった。proceedings.iclr.cc は1回目が時間切れ、2回目で指定なしを確かめた
- noai: true の10ドメイン：その出典が sources に残っていないことを、scratchpad のスクリプトと `uv run python tools/check_pages.py`（[AI の利用の指定]・[断るドメインと deny] とも エラー 0。警告 8 件は data と関係のない stub の front matter）の両方で確かめた。10ドメインとも deny に2つの形である。D4 の下書きにあった Anthropic Academy・techcrunch などの出典は data にも wave1-sources.yml にもない

### 2.4 wave1-sources.yml

- 136ページ。指す id はすべて data/sources.yml にある。出典がないのは knowledge-map と ai-and-sources の2ページ（D4 の報告のとおり）
- 20ページを抜き出した（無作為の14と、分野を散らすために足した6：effort-levels・how-usage-limits-work・input-symbols・connecting-mcp・keep-replies-in-japanese・goal-until-done）。目次の materials と照らすと、混ざる出典は materials が指す節にあるもので、D4 のたどり方そのものは materials に沿っていた。合う・合わないの数と例は指摘6・15

## 3. 確かめていないこと

- Claude Code とアプリを動かしてはいない（/agents の出力・画面の表示・Plugins のページなどは、文書と CHANGELOG の記述による）
- D3 が §5 に挙げた未確認の点（think hard などの段階が外れた版、日本語の語が当たった段、Styles のメニューが今も出るか、Console の画面の prompt generator が消えたこと）は、一次資料に記述が見つからず、私も確かめられなかった
- 抜き出した50件の出典は、開けることと題名・種類・日付だけを見た。調査資料の主張がその出典にあるかは見ていない
- wave1-sources.yml の残りの116ページ、data/facts.yml の features、日本語版の文書と Help Center

### 範囲の外で気づいたこと（参考）

- data/facts.yml の features の note に、日本語の語の間に半角の空白が入った箇所が96ある（例：claude-md の「CHANGELOG の 最も古い版」、rules の「同じ扱いの指示 であることから」）。下書きで複数行に折った値が、つなぐときに空白になったものと見える。台帳と names と domains にはなかった（sources は題名の2件で、元の題名のとおり）

## 4. 使ったスクリプトと取得物（scratchpad）

- スクリプト：`/tmp/claude-1000/-home-yuuki-projects-kyopro2-claude-atlas/2ee2ba0e-8978-48f8-837d-c53e59939dbb/scratchpad/e2/scripts/`（compare.py：D3 の下書きと data の比較、srcstats.py：domains と sources の対応と noai、vdates.py：版と日付の表、cl.py：CHANGELOG の節と語の検索、h2t.py：HTML を文字に、sample.py・titles.py：50件の抜き出しと題名の照合、wave1.py・wave1show.py：wave1 の id と20ページの表示、noaisum.py：check_noai.py の結果のまとめ、ほか）
- 取得物：同じ scratchpad の `e2/dl/`（CHANGELOG と changelog のページ、文書・Help Center・写し・抜き出した出典の HTML）。check_noai.py の結果は `e2/noai-all.json`
