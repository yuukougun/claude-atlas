# 工程6b 担当 D4 の報告：第一波のページの一次資料（sources・domains）と、ページごとの sources の一覧

- 版：2026-11-04。指示は [brief-data.md](brief-data.md)（§4 の D4 の行）と [brief-build.md](brief-build.md) の §1〜§3・§5
- 下書き：[data/D4.yml](data/D4.yml)（最上位のキーは `domains`・`sources`）、[data/wave1-sources.yml](data/wave1-sources.yml)（第一波のページごとの sources の id）
- 前に同じ割り当てで動いた担当はファイルを書く前に止められたので、最初からやり直した

## 1. 作ったファイルと中身の要約

| ファイル | 中身 |
| --- | --- |
| `planning/batches/step6/data/D4.yml` | sources 368件（公式文書 67・公式ブログ 24・研究 74・実践者 174・報道 29）と domains 143件。D1・D2 の下書きにある URL とドメインは重ねていない |
| `planning/batches/step6/data/wave1-sources.yml` | 第一波の136ページ（`check_catalog.py` の数え方。wave: 1 が62、前提でたどるもの24、routes から50）の並びで、ページごとに使える sources の id。D4 の368件に加えて D1 の44件・D2 の54件の id を指す |
| `planning/batches/step6/data-D4.md` | この報告 |

- 出典の一覧ができたページ：**134／136**。残りの2ページ（knowledge-map・ai-and-sources）は、materials が設計書・決定・手本と、ドメインの確かめ方の記録（research/22・28 の「AI の利用を断る指定の確認」）だけで、ページの根拠にする一次資料の URL がない（ページの項目の note に書いた）
- 公式の出典（公式文書・CHANGELOG・リリースノート・公式ブログ）を1つ以上持つページは127。持たない7ページ（human-pitfalls・over-reliance・ai-ideas-are-everyones・wont-rethink-approach・selection-pressure・summary-overgeneralization・review-bottlenecks）は、materials が研究と実践者の記録だけを指す判断・評価のページである
- 1ページあたりの出典の数：中央値15、最大111（product-map。materials が 01 KQ1・02 §1・§3・§5 と広い範囲を指すハブのページ）。次いで outdated-advice-ledger 48・four-principles 47・how-to-use 37
- sources の並び：D4.yml は面ごとの見出し（Claude Code の文書 → Platform → ヘルプセンター → claude.com・Academy → anthropic.com → GitHub・npm → ほかの公式 → 研究 → 実践者 → 報道）の中で id の順。wave1-sources.yml は種類の順（公式文書 → CHANGELOG → リリースノート → 公式ブログ → 研究 → 実践者 → 報道）

## 2. 確かめたこと

- **第一波のページ**：`tools/check_catalog.py` の `first_wave()` を scratchpad のスクリプトから呼んで136ページの id と materials を出した（`--stats` の第一波136ページと一致）
- **materials のたどり方**：785項目の materials を、調査資料のファイルごとの書き方（00 の §N・分野NN・小見出し、01 の KQ・X-N・N-M、02 と 05 の §N-M、03 の Q と W1・C1 など、04 の Q と A〜K、10 の第N章・第N部・付録 A-N、11 の第N節・分野・3-2 #N・C-N・第4節 #N・第5節 A-N と p12#・p34#・p56#、22〜28 の #N・§N.N・F2-a・A-12・P9・§2.3 ア など）で節・表の行・項目の範囲に解いた。解けなかったのは2項目だけ（11 第1節 新分野案X の冒頭の段落、11 第3節 3-3 の末尾の段落。どちらも 11 に URL がない）
- **11（照合の一覧）の論点**：p12#・p34#・p56# は照合のノート（11a・11b・11c）の行の「章」と「主な出典」を読み、補完調査（10）のその章のリンクのうち名前の合うものを拾った（237件のうち、主な出典が「—」でないのに合わなかったのは20件で、多くは「下記の事例」「第18章」のように出典を名指ししないもの）。合わない3件は手で当てた（p34#1 → C コンパイラの記事、p56#102 → Simon Willison の要約、p56#123 → Prompting Claude Opus 5）
- **工程2の報告（22〜28）**：表の行と節の URL に加えて、行の「出典」の欄の名前・S 番号（25・28）・「使った項目」（23）・CHANGELOG の版の記述から、各報告の「使った一次資料」の一覧の URL を拾った。research/27 §3.3 の英語への回帰の記録は、本文が番号で挙げる GitHub の issue（#87647・#96326・#96601・#98633・#99704・#99800・#101940）を `https://github.com/anthropics/claude-code/issues/<番号>` で出典にした
- **説明つきの参照**：「00 §1（日本語特有の論点の段落）」「04 Q3（textlint と PostToolUse フックの連携）」「10 第3章 二つ目（迎合）」のように節より狭い場所を指す40か所は、当たる段落・表の行・項目に手で絞った（絞らないと 00 §1 だけで58件の URL が全部のページに入る）
- **注記と訂正の付いた主張**：調査資料の 【2026-11-03 注記】・【2026-11-03 訂正】 の引用（「…」）から当て先の文・表の行を探し、その主張の URL を除いた。引用で当て先が決まらなかった注記は、前後を読んで手で当てた（00 が4件、05 が1件、10 が13件）。01 の冒頭の注記（Best practices を出典にした 0-1・A-1・C-2〜C-5・F-1・H-1・J-1・K-1・N-2・P-3 と KQ3 の Inferences は改稿前の版の要約の可能性がある）は、その項目の Best practices の URL だけを除いた。注記・訂正の付いた主張にだけ出てくるために除いた URL は21件（§5）。除いた主張の確かめ直した出典は、materials が並べて挙げる research/22〜28 の項目から入る（例：Best practices は research/23 §3.1・research/25 §3.4 から入る）
- **一次資料が開けるか**：2026-11-04 に、使える URL をすべて curl で1回ずつ取得した（名乗る User-Agent は1つ。転送は1段ずつたどり、転送先が AI の利用を断るドメインならたどらない）。開けなかった18件は sources に入れていない（§5）。`url` はどれも転送先の URL（research/28 §3.8・design §6.8）
- **AI の利用を断る指定**：D1・D2 の domains にない162のホストを `uv run python tools/check_noai.py --robots --json` で1つの URL ずつ確かめ、出典に使う143のドメインを domains に書いた。noai・noimageai の指定（meta と X-Robots-Tag）があるドメインはなかった。atcoder.jp・info.atcoder.jp・codeforces.com は開いていない（その URL は sources に入れていない）。取得した本文の meta robots と X-Robots-Tag も URL ごとに見た（指定のある URL はなかった）
- **題名・言語・日付**：取得した本文の og:title・title・h1（anthropic.com の研究・ニュースと claude.com の記事は、長いほうの見出し。PDF は1ページ目の文と文書の情報）、html の lang、記事の日付の meta（article:published_time・citation_date・JSON-LD の datePublished と dateModified）から入れた。PDF とページの題名が汎用のもの（「Sakana AI」など）は、本文の見出しで手で直した
- **形の検査**：scratchpad のスクリプト（`/tmp/claude-1000/-home-yuuki-projects-kyopro2-claude-atlas/2ee2ba0e-8978-48f8-837d-c53e59939dbb/scratchpad/d4/scripts/validate.py`。`uv run python` で動かす）で、D4.yml をリポジトリの読み方（`tools/lib/yamlio`）で読み、`schema/sources.schema.json` に jsonschema 4.26（Draft7Validator・FormatChecker）と `tools/lib/schema.py` の Validator の両方で当てて、誤り0件。あわせて、id と URL の重なり（D4 の中と、D1・D2 との間）がないこと、出典のホストがすべて domains（D4・D1・D2。いちばん長く一致するもの）にあること、AI の利用を断るドメインの出典がないこと、wave1-sources.yml が第一波の136ページを同じ並びで持ち、指す id がすべて D4・D1・D2 にあること、D4 の出典がどれもどこかのページから指されることを確かめた
- **D1・D2 との重なり**：URL（転送先を正規化したもの）が D1・D2 の出典と同じ98件は新しく作らず、その id を一覧で指した（D1 44件・D2 54件）。例：cc-changelog・cc-docs-changelog・hc-release-notes・api-release-notes・cc-docs-memory・hc-usage-limits・hc-styles-to-skills（写しの URL）

## 3. 決めたこと

### 3.1 何を一次資料として sources に入れたか

- 調査資料が引く URL のうち、公式（Anthropic の文書・ヘルプセンター・Privacy Center・CHANGELOG・公式ブログ・研究）、研究（論文と研究機関の報告）、実践者の記事、報道を入れた。指示のとおり公式を先に確かめたが、時間の内に全部を確かめられたので、実践者と報道も入れた
- 写し・集約サイトを引いていたものは、開ける元の資料に置き換え、note に書いた：Algolia の DocSearch → `github.com/anthropics/courses`、gitlink のミラー → `github.com/anthropics/prompt-eng-interactive-tutorial`、beri.net → Anthropic Academy の Introduction to Model Context Protocol、jsDelivr の README → `github.com/luongnv89/claude-howto`、claudeissues.com（ホストが引けない）→ GitHub の元の issue（5件）、alphaxiv → arXiv
- arXiv の論文は版の付かない `https://arxiv.org/abs/<id>` を1件の出典にした（html・pdf・版の違う URL を一つにまとめた）。調査資料が版や形式を指していたものは note に「調査資料は … を引いた」と書いた
- 同じ文書の別の URL はまとめた：raw の CHANGELOG → D1 の cc-changelog、Claude 3.7 Sonnet の System Card の CDN の URL → assets.anthropic.com の URL、threadreaderapp の scrolly → thread
- 改稿前の Best practices の写し（Internet Archive、2026-10-26）は別の出典にせず、cc-docs-best-practices の `archive` に入れた（schema の archive の用途どおり）
- 入れなかったもの：X の投稿（本文はスクリプトで描く画面で読めない。x.com の1件）、MCP のサーバーの接続先の例（mcp.notion.com/mcp）、GitHub の issue の一覧のページ

### 3.2 属性の付け方

| 属性 | 決め方 |
| --- | --- |
| id | 担当の記号を付けず、内容から作った。D1・D2 の頭をそろえた：`cc-docs-<パス>`・`api-docs-<名前>`・`hc-<題の語>`（日本語版は `hc-ja-<番号>`）・`claude-blog-`・`claude-docs-`。ほかは `anthropic-eng-`（Engineering の記事）・`anthropic-research-`・`anthropic-news-`・`academy-`・`cc-issue-<番号>`・`arxiv-<番号>`、実践者はサイトと記事の語（`zenn-<書き手>-<記事の頭>`・`qiita-<書き手>-<記事の頭>`・`speakerdeck-<書き手>-<語>` など）。日本語の題で語が取れないものと、番号だけのパスのものは手で付けた |
| kind | Anthropic の文書・ヘルプセンター・Privacy Center・Academy・規約は公式文書、anthropic.com の news・Engineering・製品の発表と claude.com の blog・resources/articles・claude.dev Blog は公式ブログ、anthropic.com/research の研究の報告と論文・研究機関の報告は研究、ニュースのサイトとプレスリリースは報道、ほかは実践者。GitHub の anthropics/claude-code の issue は利用者の報告なので実践者にした。**Anthropic 以外の主催者・機関の一次の文書（ISUCON2026 のレギュレーション・文部科学省と奈良高専の指針・Model Context Protocol の文書・rustc-dev-guide）は公式文書にした**（§4 の2） |
| publisher | Anthropic のものは「Anthropic」（Academy・Privacy Center・claude.dev Blog・npm は括弧で添えた）。arXiv は「arXiv（筆頭著者 ほか）」、Zenn・Qiita・Speaker Deck は「サイト（書き手の名前）」、ほかはサイトか著者の名前。写しは「…（写し）」と書いた |
| lang | 英語・日本語のサイトは決め打ち、Speaker Deck とヘルプセンターはページの lang と題名の文字で決めた |
| published | 記事・論文・ブログの発行の日。ヘルプセンターの記事は JSON-LD の dateModified（D2 と同じ）。code.claude.com・platform.claude.com・claude.com/docs の文書には書いていない（D1 と同じ）。メタデータに日付がないものは書いていない |
| note | 置き換えの理由、Engineering の記事の転送、arXiv の版、失敗の例に使う資料（GitHub の issue・はてなブックマークのコメント）は書き手を名指ししないこと（decisions 2026-11-03「書き方の方針（第三者・根拠・コンテスト）」の1）、写しであること |

### 3.3 Anthropic の Engineering の記事

`https://www.anthropic.com/engineering/<名前>` は、2026-11-04 には `https://www.anthropic.com/research/<名前>` へ転送される。url は転送先にし、種類は公式ブログのまま、id は `anthropic-eng-<名前>`、note に元の URL を書いた（8件：building-c-compiler・claude-code-auto-mode・demystifying-evals-for-ai-agents・effective-context-engineering-for-ai-agents・effective-harnesses-for-long-running-agents・harness-design-long-running-apps・multi-agent-research-system・writing-tools-for-agents）。april-23-postmortem（品質のポストモーテム）も /research/ にあるが公式ブログにした

### 3.4 wave1-sources.yml の形

- `pages:` の下に、第一波の並びで `{id, sources, note}`（note は出典がないページだけ）。一覧は「materials がたどる節にある、使える出典」で、本文に全部を使うという意味ではない。値は執筆の時に一次資料で確かめる（ファイルの冒頭の注に書いた）
- 節を指す materials（「00 §3 分野18」など）は、その節のどの文の出典も入る。1つの節が多くのページに当たるので、ページの主題から遠い出典も混ざる（例：refused-or-blocked に、research/26 §3.3 が触れる Desktop と MCP の文書）

## 4. 提案

1. **robots.txt で AI のクローラを断るドメイン（メインか作者の判断）**：次の12ドメインは、noai・noimageai の指定はない（check_noai.py の判定は「指定なし」）が、robots.txt で ClaudeBot などの AI のクローラにサイト全体を禁じる。domains の note に書き、noai は false にした。H1 と同じ扱い（資料にしない）にするかを決めてほしい：anthropic.skilljar.com と anthropic-partners.skilljar.com（Anthropic Academy。Anthropic 自身の講座）・threadreaderapp.com・techcrunch.com・www.theregister.com・www.bleepingcomputer.com・chessprogramming.org・posfie.com・israynotarray.com・ringling.libguides.com・www.oreilly.com・zenn.dev（Bytespider だけ）。research/28 と D1 の github.com と同じく、指定の確認の記録として残した
2. **kind の語彙（site.yml の source_kinds）**：Anthropic 以外の主催者・機関の一次の文書（大会の規則・公的な指針・MCP の文書）を公式文書にした。「公式」をバッジで Anthropic の公式と読ませるなら、別の種類（例：「主催者の文書」）を足すか、実践者に寄せるかを決めてほしい。該当は isucon2026-regulation・mext-genai-university-overview・nara-kosen-genai-guidelines・mcp-docs-…・rustc-dev-guide-…
3. **Engineering の記事の URL**：ほかの担当（D3 を含む）とメインが data/ にまとめるとき、`/engineering/` の URL は `/research/` の転送先で同じ出典として扱う（§3.3）
4. **ページの sources の初期値**：骨格（6c）で front matter の sources は空のリストにする決まり（keys.yml）なので、wave1-sources.yml は執筆者への渡し物として使い、front matter には写さない。写すなら、ページの主題から遠い出典を目次の担当が外してから
5. **ヘルプセンターの日本語版**：Claude Code チートシート（hc-ja-14553413）と週間制限のプロモーション（hc-ja-15910845）の記事は日本語版の URL のまま入れた。後者は題が「2026年5月～8月」に変わっていた（調査資料の URL は「5月-7月」で、転送された）

## 5. 確かめていないこと・終わらなかったこと

- **開けなかった18件**（sources に入れていない。ページ数は materials で指すページの数）：
  - 403（この環境からの取得を断られた）：www.datacamp.com の2件（Claude Code in Action の日本語の講座ページ 2ページ・autoresearch の解説 6ページ）・openai.com/index/expanding-on-sycophancy（2）・news.stanford.edu の迎合の研究の記事（4）・www.issoh.co.jp/tech/details/18753（1）・www.phoronix.com の Fedora の記事（2）・aipicks.jp の CLAUDE.md の記事（2）
  - 429：www.morphllm.com の2件（使用量の上限 3・自動の圧縮 1）
  - 接続できない：blog.oimo.io（ホストが引けない。2）・recursive.cc（時間切れ。2）・joschu.net（接続が切れる。1。同じ文章の写しの pengsida.net の PDF は入れた）・pasqualepillitteri.it（1）
  - 404：zenn.dev/fleagne/articles/4eb2a7aef1acf9（1）
  - AI の利用を断るドメイン（開かない）：atcoder.jp の2件（生成 AI のテストのコンテスト 1・長期 AHC の2部門 2）
  - 本文を読めない：x.com の投稿 1件。文書でない：mcp.notion.com/mcp
  - Internet Archive に写しがあるかは調べきれなかった（2026-11-04 に availability API へ14件を問い合わせたところ、すべて 429 で返った。新しい写しは作っていない）。403 の7件は人が開けば読める見込みが高いので、写しか本文を確かめてから足すとよい
- **注記・訂正の付いた主張にだけ出てくるので除いた21件**：例として、ImpossibleBench の監査の LessWrong の記事、Fahad ほかの判断の反転の論文（alphaxiv 2607.10411）、Chiang ほか（IUI 2024）と Drosos ほかの研究、OfficeChai の AtCoder の記事の一つ、SWE-fficiency（arXiv 2511.06090）と KernelBench-Verified（2607.16241）、Awesome Agents の ultrathink の記事、DataCamp の使用量の記事、Simon Willison の cognitive debt、AtCoder の規則（info.atcoder.jp・atcoder.jp）。ほかのページが注記のない主張で同じ URL を引くときは入れた（例：arxiv-2601-20245）
- **注記の当て先は引用の文字で決めた**：当て先の文に URL がなく、次の文の URL が両方の根拠になっているとき（例：10 第8章の「42%から95%」の文と、次の文の Anthropic の evals の記事）は、次の文の URL を残した。手で当てた18件のほかに、取り違えがあるかもしれない
- **名前で拾った出典（research/22〜28）**：行と節の文に出てくる資料の名前を「使った一次資料」の一覧と照らした。1語の名前（errors・desktop など）は「の errors」の形に限ったが、近いページの文書が混ざっていることがある（§3.4）。逆に、名前の書き方が一覧と違うものは拾えていない
- **題名・日付は取得したページのメタデータのまま**：記事の本文の題と1件ずつ照らしてはいない（汎用の題名とサイト名の付いたものだけ手で直した）。og:title が記事の見出しより短いサイトがある。anthropic.com の研究・ニュースと claude.com の記事は、見出し（h1）が長いときは見出しを題名にした（例：anthropic-research-code-expertise は og:title が「How Claude Code is used in practice」、見出しが research/25 の S1 と同じ「Agentic coding and persistent returns to expertise」）。ほかのサイトは og:title のまま
- **出典の中身は読んでいない**：開けることと題名・日付だけを確かめた。調査資料の主張がその出典に本当にあるかは、執筆と検証で確かめる
- **AI の利用の指定は、ドメインごとに1つの URL で確かめた**（出典の URL ごとには、取得した本文の meta robots と X-Robots-Tag を見ただけ）。media.defcon.org は check_noai.py の取得が途中で切れたので、出典の取得で読めた本文とヘッダーに指定がないことを note に書いて noai を false にした
- **調査資料に URL がない参照**：11（照合の一覧）の行そのもの、research/21、design・requirements・decisions などの内部の文書は、URL を持たないので出典を拾っていない
- **使ったスクリプト**（再現の手がかり。scratchpad にある）：`/tmp/claude-1000/-home-yuuki-projects-kyopro2-claude-atlas/2ee2ba0e-8978-48f8-837d-c53e59939dbb/scratchpad/d4/scripts/` の `wave1.py`（第一波の materials）・`rindex.py`（調査資料の区画と注記）・`overrides.py`（説明つきの参照の絞り込み）・`collect.py`・`candidates.py`・`fetch.py`・`parse.py`・`build.py`・`emit.py`・`validate.py`
