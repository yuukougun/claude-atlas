# 工程3 C12：symptoms（症状辞典）の目次の報告

- 担当：C12（2026-11-04）
- 書いたもの：[planning/catalog/symptoms.yaml](../../catalog/symptoms.yaml)
- 指示：[brief-catalog.md](brief-catalog.md)。この担当に固有の指示（全ページに `wave: 1`、症状は1症状1ページで題名は読者の言葉、signs の symptom を2つ以上、prevents を1つ以上、prerequisites と related に原因ごとの対処のページ、00 §4 の73項目の振り分け、requirements §4.4 の5つの症状）に従った

## 1. 書いたファイルとページ数

symptoms：33ページ（registry の候補26をすべて採り、新しく7ページを足した）。型はすべて symptom。

| 内訳 | 数 |
| --- | --- |
| 優先度 | 必須 16・推奨 17・任意 0 |
| レベル | 使う 6・整える 16・任せる 9・仕組みにする 2・回す 0 |
| 章 | 返答と品質 6・事実と出典 5・会話と文脈 4・指示と仕組み 2・日本語の出力 2・完了と検証 3・長い作業と方針 4・安全と承認 4・上限と速さ 3 |

作り方の決めごと：

- **診断の順**：prevents は、そのページの診断で問う原因を、六つの原因を安く確かめられる順（見えていない → 散らかっている → 確かめていない → 縛っていない → 合っていない → 境界がない。requirements §3.2・design §2.2・§6.3）に並べた。人の側の落とし穴が関わる10ページに pitfalls を付けた（caves-when-pushed・going-in-circles・claims-done-but-isnt・misses-broken-evaluation・stuck-in-a-check-loop・wont-rethink-approach・parallel-fatigue・deleted-something-important・wrong-amount-of-approvals・seems-less-capable）
- **前提と関連**：prerequisites には、原因ごとの対処のうち中心になるページ（直接の前提、1〜3件）を置き、残りの対処のページを related に近い順に置いた。必須の前提は必須、前提は同じか下の段、の規則を満たさない対処の中心（four-specifics・keep-replies-in-japanese・when-to-add-what など）は related に回した（§6）
- **入ってくる道**：症状どうしを related で互いに結び、全ページが少なくとも1つの症状のページから指される。ほかの分野からも、新しい4ページ（parallel-fatigue・secrets-exposed・followed-injected-instructions・too-slow）を除く29ページが指されている（2026-11-04 の各分野のファイルで数えた）
- **sections**：全ページに `{title: 原因を安く確かめる順, anchor: diagnosis}` を置き、ほかのページが `id#diagnosis` で診断の節を指せるようにした。消された・秘密を出されたの2ページには、復旧と最初の手当ての節（recover・first-response）を診断より前に置いた。refused-or-blocked には面ごとの表示の節（by-surface）
- **書かないもの**：summary・signs・title に変わりやすい値（上限の時間の枠・プランの名前・PDF のページ数・既定の effort・締め切りの日付・研究の割合）を書いていない。訂正・注記の付いた主張（改稿前の Best practices の「埋まるほど性能が落ちる」「強調は1行だけ」、具体性の4要素を研究の結果とすること、迎合の説得率、11 3-2 #5 の skill の一覧など）を summary・signs の根拠にしていない。materials には関わる報告の番号を書いた。materials と notes に個人の名前を書いていない

## 2. merged・dropped と、新しく足したページ

merged・dropped：なし（registry の26候補をすべて pages に入れた）。

registry の notes が挙げた重なりは、症状のページ（読者の言葉と切り分け）と、なぜ・対処の本体のページに分けて両方を残した：forgot-after-compaction と basics の what-survives-compaction・context の promises-after-compaction（enforce の spoken-prohibitions-fade は enforce で when-to-lock にまとめられた）、seems-less-capable と models の suspected-degradation、summary-overstates-source と basics の summary-overgeneralization。

新しく足したページ（7。すべて推奨。notes に「新規：理由」を書いた）：

| id | 題名 | 理由 |
| --- | --- | --- |
| refused-or-blocked | 断られた・止められた | research/26 §3.3 が症状のページを提案し、decisions 2026-11-03 が書き方を決めている。safety が足した when-requests-are-refused（手段の本体）を前提にし、ここは面ごとの表示と切り分けに絞った |
| too-slow | 返事が遅い・時間がかかりすぎる | requirements §3.2 の原因⑤の典型的な症状「遅い」にページがない。00 §4 の「入れた拡張が多すぎて重い」の受け皿 |
| secrets-exposed | 秘密の情報を読まれた・外に出された | requirements §3.2 の原因⑥の典型的な症状「秘密の流出」にページがない |
| followed-injected-instructions | 読ませたページやファイルの指示に従ってしまった | requirements §3.2 の原因⑥の典型的な症状「悪意ある入力に従う」にページがない |
| unexpected-memories | 別の会話やプロジェクトの内容が混ざる | 00 §4 の2項目（記憶が混ざる・消した会話を覚えている）の受け皿。アプリの Memory と Claude Code の CLAUDE.md の階層・auto memory をまたいで切り分ける |
| inconsistent-japanese-style | 文体や表記が揃わない | 00 §4 の2項目（です・ますの混在・表記ゆれ。原因④）の受け皿で、日本語の核（第一波）の症状側の入口 |
| parallel-fatigue | 並列にしたら疲れた・レビューが追いつかない | 00 §4 の「並列にしたら疲れた」の受け皿。人の側の落とし穴（ア・エ）と judgment・eval の核をつなぐ |

registry の見当から変えたもの：misses-broken-evaluation の level を「仕組みにする」から「任せる」に下げた（評価器を渡して実験を任せた段階で出会う。前提の eval の verifier-defines-problem・check-the-metric と同じ段）。

requirements §4.4 の5つ（misses-broken-evaluation・stuck-in-a-check-loop・blames-the-tools・insists-on-mistakes・wont-rethink-approach）は、根拠の行（11 第1節 分野18）の強さと類推・版依存を materials に書き、他社のモデルの事例（insists-on-mistakes）や単独の事例（stuck-in-a-check-loop）を特定のモデルの傾向として書かないよう notes に書いた。

## 3. `wave: 1` を付けたページ

33ページすべて（symptoms は第一波の核の分野で、registry の wave_core と D10 による）。`tools/check_catalog.py --stats` の第一波は全体で122ページ（wave: 1 が59、前提でたどって届くもの63。2026-11-04、全分野のファイルがそろった時点）。

## 4. ほかの分野への提案（open_issues の要約）と new_features

open_issues（16項目。提案15と、決めきれなかった点1）の要点：

1. models：suspected-degradation と seems-less-capable の分担。merged にするなら seems-less-capable の前提から外す必要がある
2. japanese：replies-in-english と inconsistent-japanese-style の前提に align-japanese-output を置いた。keep-replies-in-japanese は任せるなので related
3. prompting：four-specifics（整える）は not-what-i-meant（使う）の related。4要素は研究の結果ではない（research/25 P9）
4. extend：when-to-add-what（任せる）は repeating-the-same-explanation（整える）の related
5. safety：依存（パッケージ）を入れる前の確かめ方の本体がない
6. safety：when-requests-are-refused の related に refused-or-blocked を。手段の本体は when-requests-are-refused、表示と切り分けは症状のページに
7. safety：protecting-secrets・lethal-trifecta から secrets-exposed へ、prompt-injection-in-practice・instructions-hidden-in-materials から followed-injected-instructions への道を
8. models・context：effort-levels・fast-mode-and-advisor・always-on-costs から too-slow への道を
9. start：six-causes と reverse-index から症状の全ページへの道を
10. delegate：goal-until-done・open-ended-loop-trap から stuck-in-a-check-loop、humans-set-the-parallel-limit から parallel-fatigue への道を
11. app：memory-faq（アプリの操作の本体）と unexpected-memories（面をまたぐ切り分け）の分担
12. basics：summary-overgeneralization の related に summary-overstates-source を
13. verify：検索の打ち切り（research/22 #18）と、起動に失敗しても 0 で終わった例（#24）を evidence-not-reports か verification-ladder に
14. cost・models：00 §4 の「Pro と Max」「Fable を使ってみたい」は、名前を使わない言い方に（§7 の表）

new_features（2）：

- `refusals`：拒否と分類器による停止（アプリの自動のモデルの切り替え、Claude Code の表示、API の stop_reason: refusal）。research/26 §3.3。refused-or-blocked が tracks で指す
- `language-setting`：Claude Code の language 設定。research/27 §3.2。replies-in-english が指す（settings の一部だが、英語への回帰の点検のために分けて追う案）

## 5. 検査の結果

`python3 tools/check_catalog.py --field symptoms`：エラー0、警告0（分野のファイル23・ページ361を読んだ時点）。

途中で、related に置いたほかの分野の候補のうち16件が、その分野のファイルで merged になっていた（old-and-new-names → glossary、claude-code-costs → what-uses-up-limits、spoken-prohibitions-fade → when-to-lock など）。まとめた先に差し替えるか、まとめた先がすでに前提か関連にあるものは外した。ほかの担当が新しく足したページのうち、when-requests-are-refused（safety）・align-japanese-output（japanese）を前提に、isolate-with-safe-mode（cli）・lock-side-effects（enforce）を related に入れた。

## 6. 確かめていないこと、迷った点

- **一次資料は見ていない**（Web を開かない指示）。症状の言葉と根拠は 00 §3・§4、05 §1・§2・§4、11 第1〜2節、research/22〜27 による
- **前提に置けなかった対処の中心**：使う・整えるの症状では、対処の中心が上の段にあり related に回ったものがある（not-what-i-meant の four-specifics、repeating-the-same-explanation の when-to-add-what・what-to-put-in-claude-md、replies-in-english の keep-replies-in-japanese、hits-limits-quickly の what-uses-up-limits・saving-priorities）。第一波は前提でたどれるページなので、これらが第一波に入らないことがある。第一波の公開のときに、症状のページから未公開のページへのリンクをどう見せるかは設計の判断が要る
- **instructions-ignored の level**：design §3.3 の例は「整える」だが、registry（00 の L3）に従い「任せる」にした。会話の中の指示が守られない場面は、not-what-i-meant と forgets-in-long-chats に振り分ける
- **00 §4 の症状の項目のうち、専用のページを作らず既存の症状のページの signs にしたもの**：「同じ質問で毎回答えが違う」（plausible-falsehoods。05 §2-7 がばらつきを確かめる合図として扱う）、「回答が長すぎる・短すぎる」「文章が AI っぽい」（not-what-i-meant。00 §4 で原因①）、「大量のログやテスト出力で会話が埋まる」（forgets-in-long-chats）、「作った skill が使われない」（instructions-ignored）、「古い記事のやり方が通じない」（doesnt-know-latest。読者の側の情報が古い場合として）。最後のものは本体が changes の台帳なので、changes のページの signs にも置くのがよい
- **新しいページの数**：7ページを足したので、symptoms は requirements §4.2 の目安（25）より8多い。どれも推奨にし、初版の必須の範囲は増やしていない。ただし全ページが wave: 1 なので第一波は増える（前提で safety・delegate・japanese の数ページが届く）。減らすなら、unexpected-memories（app の memory-faq と重なる）と parallel-fatigue（delegate・team の2ページと重なる）が候補
- **volatility**：hits-limits-quickly（プランと上限の構成が変わる）と refused-or-blocked（表示の文・分類・検証の制度が変わる）を高、summary-overstates-source（原理）を低、ほかを中にした
- **ほかの分野のファイルは並列に書かれていた**：検査は 2026-11-04 のある時点の全分野のファイルで行った。その後にほかの分野が id を merged・dropped にすると、このファイルの参照がエラーになりうる

## 7. 00 §4 の逆引き73項目の振り分け（ほかの分野の担当への引き継ぎ）

- 種類：symptom（困りごと）33項目は、このファイルの signs に入れた（文はそのままか、読者の言葉のまま少し補った）。goal（やりたいこと・問い）34項目と situation（置かれた状況）6項目の計40項目は、症状のページに置かず、向く先のページを挙げた
- 「向く先」は、その項目を signs に置くとよいほかの分野のページ（00 §4 の「引くページ」を、2026-11-04 の各分野のファイルの id に読み替えた）。symptom の項目も、向く先のページの signs に同じ困りごとを置くと、逆引きで症状のページと対処のページが並ぶ
- id の読み替え：sessions-as-branches → resume-and-branch、old-and-new-names → glossary（どちらも各分野で merged）。cli の for-non-engineers は dropped なので、72 は recipes だけを挙げた

| # | 項目（00 §4） | 種類 | このファイルで置いたページ | 向く先（ほかの分野のページ） |
| --- | --- | --- | --- | --- |
| 1 | 頼んだものと違うものが出てくる | symptom | not-what-i-meant | prompting/four-specifics |
| 2 | 毎回同じ背景を説明している | symptom | repeating-the-same-explanation | app/where-to-put-instructions・extend/when-to-add-what |
| 3 | 「いい感じに」と頼むと平凡になる | symptom | not-what-i-meant | prompting/brief-a-new-colleague・show-examples |
| 4 | 提案だけで止まり、実行してくれない | symptom | keeps-stopping | prompting/suggest-or-do |
| 5 | 頼んでいない機能やファイルが増える | symptom | does-more-than-asked | prompting/state-the-scope |
| 6 | もっともらしいが出典が怪しい | symptom | plausible-falsehoods | verify/checking-citations |
| 7 | 最近の出来事や新しい版について間違える | symptom | doesnt-know-latest | basics/knowledge-cutoff |
| 8 | 同じ質問で毎回答えが違う | symptom | plausible-falsehoods（「どれが正しいか分からない」まで補った） | basics/nondeterminism・verify/fact-checking |
| 9 | こちらの誤った指摘にもすぐ同意する | symptom | caves-when-pushed | basics/sycophancy・judgment/ask-without-sycophancy |
| 10 | 長い PDF の後半の図について答えられない | symptom | skipped-later-pages | app/how-attachments-are-read |
| 11 | 推論の過程を全部見せてほしい | goal | — | prompting/asking-for-reasoning・basics/unfaithful-reasoning |
| 12 | 回答が長すぎる・短すぎる | symptom | not-what-i-meant | prompting/output-shape・models/model-quirks |
| 13 | 文章が「AI っぽい」 | symptom | not-what-i-meant | japanese/less-ai-sounding-japanese・prompting/requesting-prose |
| 14 | 返事が英語になる | symptom | replies-in-english | japanese/keep-replies-in-japanese・align-japanese-output |
| 15 | です・ますとだ・であるが混ざる | symptom | inconsistent-japanese-style（新規） | japanese/consistent-politeness・textlint-hook |
| 16 | 「サーバー」と「サーバ」が混在する | symptom | inconsistent-japanese-style（新規） | japanese/consistent-notation |
| 17 | 会話が長くなると精度が落ちる | symptom | forgets-in-long-chats | basics/context-rot |
| 18 | 同じバグの修正を何度も失敗する | symptom | going-in-circles | context/rewind-dont-correct |
| 19 | どのタイミングで新しい会話にすべきか分からない | goal | — | context/when-to-start-fresh |
| 20 | 圧縮されたら前に決めたことを忘れた | symptom | forgot-after-compaction | basics/what-survives-compaction・context/promises-after-compaction |
| 21 | 長い作業を明日も続けたい | goal | — | context/handoff-documents・progress-files・cli/resume-and-branch |
| 22 | ちょっとした質問で本筋を汚したくない | goal | — | context/side-questions-btw |
| 23 | 何がコンテキストを占めているか知りたい | goal | — | context/inspect-context・always-on-costs |
| 24 | 大量のログやテスト出力で会話が埋まる | symptom | forgets-in-long-chats | context/research-in-subagents・enforce/hook-recipes |
| 25 | 別のプロジェクトの記憶が混ざる | symptom | unexpected-memories（新規） | app/how-memory-works・memory-faq |
| 26 | 会話を消したのに覚えている | symptom | unexpected-memories（新規） | app/memory-faq |
| 27 | 記録を残さずに相談したい | goal | — | app/incognito-chats・safety/where-your-data-goes |
| 28 | 1M コンテキストなら気にしなくてよいのか | goal（問い） | — | models/1m-context・basics/attention-budget |
| 29 | CLAUDE.md に書いたのに守られない | symptom | instructions-ignored | enforce/when-to-lock |
| 30 | CLAUDE.md が長くなってきた | situation | —（instructions-ignored には「書き足すほど守られなくなった」を置いた） | extend/claude-md-length・path-scoped-rules |
| 31 | CLAUDE.md に何を書けばよいか分からない | goal | — | extend/what-to-put-in-claude-md |
| 32 | 特定のディレクトリだけのルールを書きたい | goal | — | extend/path-scoped-rules |
| 33 | 同じ手順書を何度も貼っている | symptom | repeating-the-same-explanation | extend/how-skills-load・writing-skills |
| 34 | 作った skill が使われない | symptom | instructions-ignored | extend/skill-descriptions |
| 35 | デプロイ用の skill を勝手に動かされたくない | goal | — | extend/manual-only-skills |
| 36 | 毎回フォーマッタをかけさせたい | goal | — | enforce/hook-recipes |
| 37 | `.env` や migrations を絶対に触らせたくない | goal | — | enforce/permission-rules・block-with-exit-2・safety/protecting-secrets |
| 38 | テストが通るまで終わらせたくない | goal | — | enforce/stop-hooks・verify/verification-ladder・delegate/goal-until-done |
| 39 | skill と subagent のどちらにすべきか | goal（問い） | — | extend/skill-vs-subagent |
| 40 | MCP を入れるか CLI で済ませるか | goal（問い） | — | extend/mcp-or-cli |
| 41 | 他のエージェントツールと指示を共有したい | goal | — | extend/agents-md |
| 42 | 入れた拡張が多すぎて重い | symptom | too-slow（新規） | extend/pruning-extensions・context/always-on-costs |
| 43 | チームで同じ設定を使いたい | goal | — | team/share-team-settings・extend/plugins-and-marketplaces |
| 44 | 「全部通りました」と言うが信用できない | symptom | claims-done-but-isnt | verify/evidence-not-reports |
| 45 | テストのほうを書き換えて通された | symptom | rewrote-tests-to-pass | verify/protect-tests |
| 46 | 自分の目で全部レビューする時間がない | situation | — | verify/independent-review・diffs-humans-must-read |
| 47 | 見た目の崩れを確かめさせたい | goal | — | verify/visual-checks |
| 48 | CLAUDE.md を変えて良くなったか知りたい | goal | — | eval/measure-changes・felt-vs-measured |
| 49 | 調査結果の出典を確かめたい | goal | — | verify/checking-citations・app/using-research |
| 50 | 確認ボタンを読まずに押している | symptom | wrong-amount-of-approvals | safety/approval-fatigue |
| 51 | auto mode に任せて大丈夫か | goal（問い） | — | enforce/what-auto-mode-stops・sandboxing |
| 52 | 知らない人のリポジトリを開きたい | goal | — | safety/before-opening-unknown-repos |
| 53 | 便利そうな MCP や plugin を見つけた | situation | — | safety/vetting-extensions |
| 54 | Web ページやメールを読ませるのが不安 | situation | —（起きた後の症状は followed-injected-instructions（新規）で受ける） | safety/prompt-injection-in-practice・lethal-trifecta |
| 55 | ファイルを消された・消されそうで怖い | symptom | deleted-something-important | cli/checkpoints-and-rewind・safety/destructive-commands |
| 56 | 入力した内容が学習に使われるか知りたい | goal | — | safety/where-your-data-goes |
| 57 | 会社や学校で使ってよいか確かめたい | situation | — | safety/checking-ai-rules・team/ai-usage-guidelines |
| 58 | すぐ上限に当たる | symptom | hits-limits-quickly | cost/what-uses-up-limits |
| 59 | /clear すれば上限は戻るのか | goal（問い） | — | cost/how-usage-limits-work |
| 60 | Pro と Max のどちらにすべきか | goal | — | cost/choosing-a-plan（プランの名前は変わりやすいので「どのプランにすべきか迷う」の形に） |
| 61 | Fable を使ってみたい | goal | — | cost/before-using-fable・models/choosing-a-model（モデルの名前を使わず「いちばん高性能なモデルを使ってみたい」の形に） |
| 62 | 急に性能が落ちた気がする | symptom | seems-less-capable | models/suspected-degradation |
| 63 | effort を上げるべきか、モデルを替えるべきか | goal（問い） | — | models/choosing-a-model・effort-levels |
| 64 | 「think hard」は効くのか | goal（問い） | — | models/thinking-keywords・changes/outdated-advice-ledger |
| 65 | アプリと Claude Code のどちらでやるべきか | goal（問い） | — | surfaces/choosing-a-surface |
| 66 | 席を外している間も進めてほしい | goal | — | delegate/five-questions-before-delegating・goal-until-done・cloud-schedules |
| 67 | 毎朝決まった調査をさせたい | goal | — | delegate/loop-and-scheduling・app/tasks-and-schedules-in-the-app |
| 68 | 複数の作業を同時に進めたい | goal | — | delegate/choosing-parallel-modes・parallel-with-worktrees |
| 69 | 並列にしたら疲れた | symptom | parallel-fatigue（新規） | delegate/humans-set-the-parallel-limit・team/review-bottlenecks |
| 70 | スクリプトや CI から使いたい | goal | — | delegate/headless-basics・github-actions-with-claude |
| 71 | 自分のアプリに Claude を組み込みたい | goal | — | api/sdk-comparison |
| 72 | コードを書かない仕事に Claude Code を使いたい | situation | — | recipes/office-paperwork |
| 73 | 古い記事のやり方が通じない | symptom | doesnt-know-latest（読者の側の情報が古い場合として） | changes/outdated-advice-ledger・start/glossary |

数：symptom 33（このファイルの signs に入れた）、goal 34（うち問いの形 8）、situation 6。
