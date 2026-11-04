# 工程6b 担当 D3 の報告：古くなった助言の台帳（advice）と、名称と旧名（names）

- 版：2026-11-04。指示は [brief-data.md](brief-data.md)（§4 の D3 の行）と [brief-build.md](brief-build.md) の §1〜§3・§5
- 下書き：[data/D3.yml](data/D3.yml)（最上位のキーは `features`〔空〕・`facts`〔空〕・`names`・`advice`・`domains`・`sources`）
- 前に同じ割り当てで動いた担当はファイルを書く前に止められたので、最初からやり直した（その担当の途中の材料は使っていない）

## 1. 作ったファイルと中身の要約

| ファイル | 中身 |
| --- | --- |
| `planning/batches/step6/data/D3.yml` | advice 37行（registry の ledger と同じ id・同じ並び）、names 19件、domains 9件、sources 62件 |
| `planning/batches/step6/data-D3.md` | この報告 |

- **台帳の行**：37行すべて、今どうするか・変わった時期と版（または name）・状態・原理・かつてなぜ正しかったか・見つける方法・出典・確認日を一次資料で確かめて書いた。**確認済み 37・未確認 0**。ただし行の中の細部で確かめられなかった点は、その行の note か changed の note に書いた（§5）
- 状態：撤回 16・置換 14・条件付き 7（00 §5 と目次の notes・research/22 §3.4 の案のまま。§3.3）
- 時期：changed を持つ行 30、name で names を指す行 7（DR-18 の6行と workflow-keyword-extra-usage）
- **names**：19件、すべて `status: 確認済み`。台帳の行が指すもの7件と、用語索引と年表のためのもの12件（§3.6）。18件は D1・D2 の features の id を `feature` で指す（Workbench の改名だけ、当たる機能がない）
- **sources**：62件。D1・D2 と同じ URL の 40件は同じ id にそろえ、新しい 22件は D1・D2 の付け方（`cc-docs-`・`api-docs-`・`hc-`・`claude-blog-`）に `gh-`・`mcp-spec-`・`wb-`（Internet Archive の写し）を足した

## 2. 確かめたこと

- **一次資料**（すべて 2026-11-04 に取得して読んだ。調査資料は手がかりにしただけで、入れた値はすべてこれらによる）
  - Claude Code：GitHub の CHANGELOG（raw。2.1.318 まで 436版）、版の日付のための公式の changelog のページ、code.claude.com の文書 37ページ（`.md`。best-practices・skills・sub-agents・commands・model-config・permission-modes・memory・interactive-mode・mcp・github-actions・routines・scheduled-tasks・claude-code-on-the-web・cli-reference・settings-reference・env-vars・workflows・agent-teams・agent-view・goal・tools-reference・agent-sdk/migration-guide ほか）
  - Claude Platform：17ページ（リリースノート・Prompting best practices・Prompting Claude Opus 5／5.5・Prompt engineering overview・Extended thinking・Thinking・Effort・Structured outputs・Model deprecations・Migrating to API version 2026-10-21・Pricing ほか）
  - Help Center：13記事（リリースノート・Cowork と chat の統合・メモリ・Ultra・Max・利用上限・Plugins のページ・usage credits・Web 検索・Claude Tag・個人設定ほか）。Styles の記事は 404 を確かめ、Internet Archive の既存の写しで読んだ
  - claude.com：auto モードの既定化の記事（2026-08-07）、リサーチの記事（編集の注で Ultra への改名の日）、料金のページ
  - GitHub：公式のプロンプトのチュートリアル（README・第0章・第5章）、claude-code-action の移行の手引きと v1 の公開の日時（GitHub の API）
  - MCP の仕様の版 2025-03-26 の変更点
  - Internet Archive：CDX の一覧（3回）と、すでにある写し（Best practices 2・クラウドセッションの文書 23・routines の文書 7・Styles の記事 1）。新しい写しは作っていない。途中で接続を断られたので、間隔をあけて取り直した
- **改稿と改名の時期**：写しで次の境を確かめた（時刻は UTC）

  | 変更 | 前の写し | 後の写し |
  | --- | --- | --- |
  | Best practices に「What you can stop doing」の表が入る（4行の時期） | 2026-10-26 19:44 | 2026-10-27 08:15 |
  | `--remote` から `--cloud`（`--remote` は非推奨の別名） | 2026-07-03 14:52 | 2026-07-06 15:57 |
  | 文書の題 Use Claude Code on the web → in the cloud | 2026-09-10 21:53 | 2026-09-17 23:49 |
  | 文書の題 Automate work with routines → scheduled tasks | 2026-10-19 23:32 | 2026-10-21 01:57 |

- **AI の利用の指定**：`uv run python tools/check_noai.py`（`--robots` つきを含む）で code.claude.com・github.com・raw.githubusercontent.com・api.github.com・platform.claude.com・support.claude.com・claude.com・web.archive.org・modelcontextprotocol.io を確かめ、どれも noai・noimageai の指定なし。github.com の robots.txt は AI のクローラに一部のパスを禁じる（domains の note）。結果を `domains` に書いた
- **schema と参照**：scratchpad のスクリプト（`/tmp/claude-1000/-home-yuuki-projects-kyopro2-claude-atlas/2ee2ba0e-8978-48f8-837d-c53e59939dbb/scratchpad/d3/scripts/validate.py`。`uv run python` で動かす）で、下書きをまとめた後の3つの形に分け、`tools/lib/schema.py` の検査器と jsonschema（Draft-07・FormatChecker）の両方で当てて、誤り 0件。あわせて、advice の id と並びが registry の ledger と同じ、advice の name がすべて names にある、names の feature がすべて D1・D2 の features にある、すべての出典が使われ id と URL に重なりがない、出典のドメインがすべて domains にある、D1・D2 と同じ URL の出典が同じ id、を確かめた
- **第一波**：`check_catalog.py` の数え方の第一波（136ページ）が outdated_advice で指す台帳の id は 31で、すべて下書きにある（台帳の37行は、どれもいずれかのページから指されている）
- **書き方の検査**：台帳と用語索引に生成される文（title・now・why_then・how_to_find、names の current・old）を、生成の道具と同じ md_text で Markdown にして textlint（リポジトリの .textlintrc.json と prh.yml）にかけ、エラー 0件（警告 13件。助詞の重なりと文の長さ）。note の文もエラー 0件。スクリプトは同じ scratchpad の `scripts/to_md.py`

## 3. 決めたこと

1. **文の形**：生成の道具（tools/gen/ledger.py・terms.py）は平文の欄の記法の字（バッククォートなど）を外すので、コマンド・フラグ・キーもバッククォートで囲まない平文にした。台帳の文はそのまま書き方の検査にかかるので、用語集の表記（サブエージェント・スキル・フック・auto モード・deny ルールなど）で書き、英語の画面の名前（Skills・Plugins）は「」で囲んだ（prh の誤検出を避ける）。だ・である調、半角と全角の間に空白
2. **title**：registry の題名を基本にし、平文にして用語集の表記に直した（例：「工程ごとに subagent を…」→「工程ごとにサブエージェントを…」、Memory → メモリ、Customize のタブの名前を「」で囲む）。id と意味は変えていない
3. **状態**：00 §5 の状態を変えずに入れた（足した6行は research/22 §3.4 と目次の notes の案）。状態が変わる更新は作者の承認が要る（design §9.4 の4）ので、別の状態が合いそうな行は §4 の提案にした
4. **時期**：日付は公式の changelog のページの日付（D1 と同じ。npm の UTC の時刻と1日ずれることがある）。段階的な変更は `until` で幅を持たせ、写しでしか絞れない改稿は `approx: true`（ごろ）にした。`version` は文書が境とする版。根拠と細部は changed の note に書いた（今の生成の道具は note を出さない。§4 の4）
5. **原理（どの原理の回避策だったか）**：research/00 §2 の五つ目の経路に従い、回避策の行はその回避策が補っていた原理にした（強調・確認を飛ばす・最初の承認・prefill → 縛る、CLAUDE.md・コマンド・サブエージェント・窓の節約 → 見せる、keep going・double-check・自作のループ・thinking タグ → 確かめる）。名前の変更の行は、その機能の主のページの原理にした。思考の量（think hard・budget_tokens）は、目次の effort-levels のページに合わせて確かめる、プランと上限の行（Max・5時間の上限・workflow と超過分・自作のエージェント組織）は、費用と並べ方の判断を人が持つので握る、avoid-opus-as-expensive は作業で比べて選ぶので確かめる にした（四つの原理に「合わせる」がないための当てはめ。§4 の2）
6. **names の範囲**：台帳の行が指す7件に、一次資料で日付まで確かめられた改名12件（`--remote`→`--cloud`、extra usage→usage credits、session limit→5-hour limit、Recently denied→Recently blocked、default→Manual の表示、/review→/code-review、Claude Code SDK→Claude Agent SDK、Claude in Slack→Claude Tag、Workbench→playground、/allowed-tools→/permissions、/vim→/config の Editor mode、/project: の前置き）を足した。日付を確かめられなかった候補は入れず §5 に挙げた。Styles からスキルへの移行は改名ではなく機能の移行なので names に入れず、台帳の行 styles-for-tone に changed で持った（同じ時期を二か所に持たない）
7. **名前の変更が2つある行**：code-on-the-web-remote（機能の名前とフラグ）と workflow-keyword-extra-usage（起動の語と超過分の呼び名）は、schema の name が1つなので、主の方（web-to-cloud-sessions・workflow-to-ultracode）を指し、もう一方を note に書いた（§4 の1）
8. **出典**：同じ一次資料は D1・D2 と同じ URL と id にした。Internet Archive の写しは時期の証拠なので、元のページの `archive` ではなく別の出典にした（url は写しの URL。題名に写しの日時を書いた）。Best practices（`cc-docs-best-practices`）は第一波のページも引くので、D4 と URL が重なりうる（メインが URL で1つにする）
9. **第三者**：00 §5 が一部の行（工程ごとのサブエージェント・自作のループ・tmux の組織・思考のキーワード）の出典にしていた第三者の記事は使わず、公式の文書と CHANGELOG で書き直した。助言を広めた個人や記事は名指ししていない（design §6.12）
10. **変わりやすい値**：今の料金・倍率の数は書かず（料金は facts に置く。avoid-opus-as-expensive の note）、昔の値（Opus 4・4.1 は Sonnet 4 の5倍）と、変わった時期と版だけを書いた

## 4. 提案

1. **schema（keys.yml の outdated-advice）**：advice の `name` を id のリストでも持てるようにし、生成の道具が名前の変更の幅（いちばん早い日〜遅い日）を出す。今は code-on-the-web-remote と workflow-keyword-extra-usage の時期が片方の改名の日だけになる
2. **原理の語彙**：effort・モデル・プラン・上限の行は四つの原理のどれにもぴったりは当たらない（「合っていない」の原因に当たる）。台帳の導入で「名前の変更の行は機能の原理を、合わせる種類の行は近い原理を当てた」と断るか、名前の変更の行は principle を任意にするかを決めてほしい（目次の choosing-a-plan・how-usage-limits-work も principle が空）
3. **状態を見直す候補（作者の承認に回す）**：cowork-separate-app（新しい体験は展開中で、前の体験のアカウントにはトグルが残る。条件付きも合う）、thinking-tags と prefill-for-json と budget-tokens（古いモデルでは今も効く。条件付きか置換も合う）、mcp-sse-transport（SSE は非推奨だが、2.1.265 以上は HTTP の後に SSE へ切り替えて今もつながる）。00 §5 の状態のまま入れてある
4. **生成の道具（tools/gen/ledger.py）**：changed の note を出していない。段階のある変更（auto モードの既定化：2026-08-14 に Pro・Max・Team、2.1.283〜2.1.284 で全体）は note がないと読み違えるので、時期の後ろに小さく出すとよい
5. **確かめ直す日**：Plugins のページ（11-09 に一般提供、Enterprise は 11-30）と、新しい Claude の体験の展開（Cowork と chat の統合）は展開の途中。customize-to-plugins と cowork-separate-app は、11-09 と 11-30 の後に確かめ直す
6. **features（D2 の提案2 と同じ）**：Claude in Slack の id は旧名のまま。names の slack-to-claude-tag で旧名を引けるので、id は変えなくても用語索引は困らない

## 5. 確かめていないこと

- **台帳の行の細部**
  - think hard などの段階がいつキーワードでなくなったか：CHANGELOG は 2.1.68 の「ultrathink を再び入れた」だけで、外した版はない。日本語の語（「熟考」など）がどの段に当たったかも一次資料で確かめていない（1.0.8 の「英語以外の言語で思考を起動できる」までは確かめた）
  - /pr-comments の削除の版（2.1.91）は公式の文書の記述だけで、CHANGELOG に行がない。/tag の代わりの機能は文書にない
  - Claude 4.7 以降のモデルが既定以外の temperature を断るようになった時期（Model deprecations は決まりだけを書く）
  - Console の画面の prompt generator と improver が消えたこと：2026-07-17 の告知（旧 Workbench と、生成・改善・テンプレート化の実験的な API の退役）から読み取った。画面は見ていない
  - 画面に Styles のメニューが今も出るか（移行が終わったか）
  - Opus 5.5 にも「double-check を消す」が当たるか：Opus 5.5 の手引きは、Opus 5 の型を出発点にしてよいとだけ書く
- **names**
  - extra usage → usage credits の Help Center での改名の日（日付は Claude Code の 2.1.144）
  - Max 5x を Max に改名したかどうか（公式は Max 20x → Ultra だけを書く。今の Max は1つの段）
  - Recent → Recently denied に変わった版
  - 写しで絞った時期（§2 の表）は、写しの間のいつ変わったかまでは分からない。日付は UTC で、日本時間では1日ずれることがある
  - 入れなかった候補（日付を確かめられない、または誤解を招く）：Integrations → コネクタ、Vertex AI → Google Cloud's Agent Platform、Cowork の権限モードの名前（Ask before acting → Manually approve など）、Analysis tool → Code execution and file creation、Instructions for Claude → Instructions（新しい設定の画面）、/ultrareview → /code-review ultra（導入の版が CHANGELOG にない）、/simplify → /code-review（2.1.147。2.1.154 で /simplify が片付けのレビューとして戻ったので、旧名として出すと誤解を招く）、MCP の scope の改名（0.2.49。0.2.x の日付が公式の changelog のページで当てにならない）
- **そのほか**
  - npm の公開の時刻は使っていない（版の日付は公式の changelog のページ）
  - Claude Code を動かして確かめていない（今 # で始めたときの動き、/agents の出力など。文書と CHANGELOG の記述による）
  - 日本語版の文書と Help Center は読んでいない（訳語は用語集と prh.yml に合わせた）
  - claude-code-action の v1 の公開の日時は GitHub の API で読んだ（リリースのページは noai の確かめだけ）
