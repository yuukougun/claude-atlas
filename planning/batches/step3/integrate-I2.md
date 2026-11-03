# 工程3 I2：目次の統合（surfaces・models・cost・api・app）の報告

- 担当：I2（2026-11-04）
- 書いたもの：[planning/catalog/surfaces.yaml](../../catalog/surfaces.yaml)・[models.yaml](../../catalog/models.yaml)・[cost.yaml](../../catalog/cost.yaml)・[api.yaml](../../catalog/api.yaml)・[app.yaml](../../catalog/app.yaml)
- 読んだもの：brief-integrate.md、catalog/README.md、design.md §2〜§4・§6、schema/site.yml、state/step3-integrate/I2-input.md、受け持ちの5ファイルと catalog-C2.md・catalog-C5.md、catalog-C12.md §7、registry.yaml の ledger、features.yaml、research/27 §3.1・§4、research/23 §3.1・§3.7、research/26 §3.1・§3.3、research/22 #40、00 §3 分野13、ほかの分野のファイル（読むだけ）
- 変えたページ：25（surfaces 3・models 7・cost 4・api 4・app 7）。どれも notes の末尾に「（2026-11-04 統合：<番号>）」を足した。ページの id と anchor は変えていない。新しいページ・merged・dropped・priority・level の変更はない

## 1. 材料 A の各項目の扱い

扱いの数：反映した 15・取り込み済みを確かめた 18・対象外 5・反映しない 2（計40）。取り込み済みの主張は、挙がった参照を全分野のファイルから引いて1件ずつ確かめた。

| 番号 | 扱い | 変えたページと、反映しないときの理由 |
| --- | --- | --- |
| basics#3 | 反映した | api/stateless-messages-api。前提の rereads-whole-history は取り込み済みだったが、要約と goal の sign が rereads-whole-history と同じ問い（なぜ長い会話が重く高いか）のままだった。要約を API の形（基本の形は状態を持たず呼び出し側が全体を渡す・message threads で減るのは送る量だけ）に、sign を「API で会話を続けるには、毎回何を送ればよいか知りたい」に絞った |
| basics#4 | 取り込み済みを確かめた | api/tool-use-loop の前提に agent-loop がある |
| basics#6 | 反映した | app/where-to-put-instructions の前提に where-instructions-sit（整える・必須）を足した。attention-budget は推移で届かないので残した |
| surfaces#1 | 反映した | surfaces/choosing-a-surface・where-it-runs の tracks に app-tasks（features.yaml にある） |
| surfaces#2 | 取り込み済みを確かめた | api/sdk-comparison は choosing-a-surface を前提に持ち（関連より強い）、節 comparison に三つの位置づけがあり、aliases に旧題がある |
| surfaces#3 | 対象外 | 数値ファイルの面の属性の表はメインの扱い。分野の側は choosing-a-surface・claude-code-surfaces・what-each-surface-cannot-do の notes に「表は数値ファイルから生成する」とすでにある |
| surfaces#4 | 取り込み済みを確かめた | 挙がった13の参照をすべて確かめた |
| models#1 | 対象外 | changes の台帳の側の依頼。models の側は、effort-levels の outdated_advice に budget-tokens、choosing-a-model（と opusplan）に avoid-opus-as-expensive がある |
| models#3 | 反映しない | harness-over-model は models に置いたまま（モデルを替える判断の直前に読まれる。比例則の守りも持つ） |
| models#4 | 取り込み済みを確かめた | 挙がった21の参照をすべて確かめた |
| prompting#4 | 反映した | models/model-quirks の related に does-double-check-work・emphasis-words を足した。after-switching-models の outdated_advice に add-double-check を足し、notes に見直しの2項目（強い言い方を和らげる・確認を命じる一文を外す）を書いた |
| prompting#8 | 対象外 | eval の measure-changes の例の話。api の側は merged（prompt-evals-intro → measure-changes）の記録がある |
| prompting#10 | 取り込み済みを確かめた | lower-temperature は basics の nondeterminism と models の after-switching-models（節 api-parameters）に付いている。api には付ける先がない（サンプリングの引数のページを置いていない） |
| context#7 | 取り込み済みを確かめた | where-to-put-instructions・using-projects・how-memory-works・long-chat-limits が tidy-the-desk#in-the-app を、long-chat-limits が when-to-start-fresh を指す。code execution の条件は long-chat-limits の materials にある |
| context#9 | 反映した | cost/how-usage-limits-work。答えは sign と要約にあった（取り込み済み）。戻り道として related に when-to-start-fresh を足した |
| app#1 | 対象外 | safety の shared-artifacts-and-files への依頼。app の4ページ（artifacts-overview・artifacts-as-apps・files-and-code-execution・shared-projects-and-org-skills）が指しているのを確かめた |
| app#2 | 反映した | surfaces#1 と同じ |
| app#3 | 反映した | M3 の styles-for-tone を app/where-to-put-instructions と skills-in-the-app の outdated_advice に入れた |
| app#4 | 対象外 | japanese の側の依頼。where-to-put-instructions と keep-replies-in-japanese が互いに指しているのを確かめた |
| app#6 | 反映しない | memory-faq を how-memory-works にまとめない（id が消える統合はしない）。symptoms#11 の分担で役を分けた |
| cli#1 | 取り込み済みを確かめた | choosing-a-surface に sign「コードを書かない仕事にも Claude Code を使うべきか知りたい」と 00 分野07 の材料がある。作業用のフォルダと手動のモードで始める点は、アプリでは permission-modes-in-the-app の節 start-small が持つ（office-paperwork と default-safety-settings は I7・I6 の側） |
| cli#3 | 取り込み済みを確かめた | cost の merged と節 find-what-uses-it、cli の usage-context-statusline と context の inspect-context からの参照がある |
| extend#8 | 反映した | app/skills-in-the-app・connectors-in-the-app・plugins-in-the-app。仕組みは extend のページを前提か related で指していた（取り込み済み）。notes に「app に書くのはアプリに固有の操作だけ」の境界を書いた。customize-tabs は3ページに付いている |
| eval#3 | 反映した | models/suspected-degradation の前提に felt-vs-measured、after-switching-models の前提に measure-changes（どちらも related から移した。段と優先度が合い、後者は recipe が確かめるページを前提に持つ規則〔design §2.2〕にも合う） |
| eval#4 | 取り込み済みを確かめた | api の merged と、measure-changes の related の batch-api-basics |
| safety#4 | 取り込み済みを確かめた | permission-modes-in-the-app → what-auto-mode-stops（関連）・lethal-trifecta（前提）、incognito-chats → where-your-data-goes、artifacts-overview → shared-artifacts-and-files |
| safety#5 | 取り込み済みを確かめた | browser-control の related の先頭に browser-agent-cautions |
| safety#9 | 取り込み済みを確かめた | check-billing-path と protecting-secrets が互いに related |
| delegate#4 | 取り込み済みを確かめた | sdk-comparison の related に choosing-automation |
| delegate#7 | 取り込み済みを確かめた | tasks-and-schedules-in-the-app、parallel-and-loop-costs（agent-teams-experimental を含む）、check-billing-path が delegate のページを指す |
| api#1 | 反映した | 依頼の本体は delegate の側（choosing-automation から managed-agents-basics は外れていた）。api の側として、batch-api-basics の related に batch-and-p-loops を足した（/batch と取り違えた読者の移り先） |
| api#3 | 取り込み済みを確かめた | feature-to-api-mapping → how-attachments-are-read#api、citations-basics → how-attachments-are-read。分野の一覧から見つけにくい点は §5 の4 |
| cost#3 | 取り込み済みを確かめた | 挙がった参照をすべて確かめた |
| japanese#5 | 反映した | Styles の移行の書き方を台帳の styles-for-tone に一本化し、where-to-put-instructions・skills-in-the-app の notes に書いた。japanese のページの前提にするかは I3 の側 |
| team#2 | 取り込み済みを確かめた | choosing-a-plan の related に enterprise-vs-team-plans |
| team#3 | 取り込み済みを確かめた | shared-projects-and-org-skills が team の4ページを指す |
| symptoms#1 | 反映した | まとめない。models/suspected-degradation から症状の sign「同じ頼み方なのに、前より雑な返事が増えた」を外し（症状の文は seems-less-capable に任せる）、notes に分担を書いた |
| symptoms#8 | 反映した | models/effort-levels・fast-mode-and-advisor の related に too-slow |
| symptoms#11 | 反映した | app/memory-faq・how-memory-works から unexpected-memories と同じ症状の文を外し（§2）、memory-faq の notes に分担（アプリのメモリの操作の本体）を書いた |
| symptoms#15 | 反映した | B #60・#61（§2） |

メインの決定の扱い：

- **M1**：§3。アプリの題名は C5 がすでにヘルプセンターの訳語にしていた。API の題名は英語のまま（プロンプトキャッシングだけ日本語）で合っていた
- **M3**：styles-for-tone を app の where-to-put-instructions・skills-in-the-app に、subagents-to-save-context を models の 1m-context（節 what-to-stop。Best practices の「やめてよいこと」の一行）と cost の parallel-and-loop-costs（追加のトークンの掛け算）に入れた。opusplan はコンテキストを守る話でないので入れなかった
- **M5**：symptoms の refused-or-blocked が current-models を指しているので、current-models の notes に執筆の注意（自動のモデルの切り替えは仕組みとして書き、通す手段として書かない）を書いた。app は safety の when-requests-are-refused に任せたまま
- **M9**：§6

## 2. 材料 B の行の扱い

| # | 項目 | 向く先 | 扱い |
| --- | --- | --- | --- |
| 27 | 記録を残さずに相談したい | app/incognito-chats | 足さなかった：同じ文がある |
| 28 | 1M コンテキストなら気にしなくてよいのか | models/1m-context | 足さなかった：同じ意味の「コンテキストが広いモデルなら、会話の長さを気にしなくてよいのか知りたい」がある（数値を外した形） |
| 49 | 調査結果の出典を確かめたい | app/using-research | 足さなかった：同じ文がある |
| 59 | /clear すれば上限は戻るのか | cost/how-usage-limits-work | 足さなかった：「/clear すれば上限が戻るのか知りたい」がある |
| 60 | Pro と Max のどちらにすべきか | cost/choosing-a-plan | **足した**：goal「どのプランにすべきか迷う」（今ある「今のプランから上げるべきか迷う」は上げるかの問いで、選ぶ問いとは別と見た） |
| 61 | Fable を使ってみたい | cost/before-using-fable・models/choosing-a-model | before-using-fable：同じ意味の「最上位のモデルを試してみたい」を、M2 の形「いちばん高性能なモデルを使ってみたい」に**言い換えた**。choosing-a-model：同じ意味の「一番賢いモデルを常に使うべきか知りたい」があるので足さなかった |
| 63 | effort を上げるべきか、モデルを替えるべきか | models/choosing-a-model・effort-levels | 足さなかった：choosing-a-model に同じ文がある。直接答えるのは choosing-a-model の節 effort-first なので、effort-levels にも足さなかった |
| 64 | 「think hard」は効くのか | models/thinking-keywords | 足さなかった：「「think hard」や「よく考えて」が効くのか知りたい」がある |
| 65 | アプリと Claude Code のどちらでやるべきか | surfaces/choosing-a-surface | 足さなかった：「この作業をアプリと Claude Code のどちらでやるべきか決めたい」がある |
| 67 | 毎朝決まった調査をさせたい | app/tasks-and-schedules-in-the-app | 足さなかった：同じ文がある |
| 71 | 自分のアプリに Claude を組み込みたい | api/sdk-comparison | 足さなかった：同じ文がある |

M2 の3つ目（症状の文を対処のページに重ねない）を、すでにある sign にも当てて、次の7文を外した。どれも、症状のページがそのページを前提か関連にして振り分けている。

| ページ | 外した sign | 同じ文を持つ症状のページ |
| --- | --- | --- |
| app/where-to-put-instructions | 毎回同じ背景を説明している（00 §4 #2） | repeating-the-same-explanation |
| app/how-memory-works | 別のプロジェクトの記憶が混ざる（#25） | unexpected-memories |
| app/memory-faq | 会話を消したのに覚えている（#26）・別のプロジェクトの記憶が混ざる（#25） | unexpected-memories |
| app/how-attachments-are-read | 長い PDF の後半の図について答えられない（#10） | skipped-later-pages |
| models/model-quirks | 返答が長すぎる・短すぎる（#12。「回答」との表記の違いだけ） | not-what-i-meant |
| models/suspected-degradation | 同じ頼み方なのに、前より雑な返事が増えた（33項目ではないが、symptoms#1 の分担で症状の文は seems-less-capable に任せた） | seems-less-capable |

外した後も、どのページにも sign が2つ以上残る。

## 3. 題名を変えたページ（M1）

| ページ | 前 | 後 |
| --- | --- | --- |
| app/where-to-put-instructions | アプリの指示の置き場所（指示・プロジェクト・メモリ・スキル） | アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） |

- aliases から題名と同じ語になった「Claude への指示」を外し、「全会話の指示」を足した（Instructions for Claude はもとからある）。雛形の名前も揃えた

題名のほかに M1 で揃えた要約と節の題名：

| ページ | 変えたこと |
| --- | --- |
| app/where-to-put-instructions | 要約の「全会話の指示」→「Claude への指示」（あわせて文末を「決められる」に） |
| surfaces/browser-control | 要約の「connector」→「コネクタ（MCP）」（Claude Code では MCP が当たるので添えた）。節 which-to-use の題名も「コネクタ」に |
| api/feature-to-api-mapping | 要約の「cache」→「キャッシュ」 |
| api/prompt-caching-in-practice | 要約と節 prefix・invalidation の題名の「cache」→「キャッシュ」（題名のプロンプトキャッシングに合わせた） |

ほかの題名と要約は M1 の表と合っていた（サブエージェント・コンテキストウィンドウ・拡張思考・effort・アプリの訳語など）。API の機能名（Messages API・tool use・structured outputs・citations・Message Batches API・compaction〔API〕など）は英語のままにした。

## 4. 新しいページ、priority・level を変えたページ

- 新しいページ：なし
- priority・level の変更：なし。M9 で feature-to-api-mapping と prompt-caching-in-practice の level を見直したが、変えなかった（§6）
- 前提を変えたページ（参考）：where-to-put-instructions（+ where-instructions-sit）、suspected-degradation（+ felt-vs-measured）、after-switching-models（+ measure-changes）。どれも段と優先度の規則を保ち、第一波の数（125）は変わらない（足した前提を除いて数え直して確かめた）

## 5. メインへ

1. **M2 の3つ目の当て方（言い換え）**：同じ文、「返答／回答」のような表記の違いだけのもの、symptoms#1 が分担を決めた1文は外した（§2）。文は違うが33項目と同じ意味の次の2文は残した：app/skills-in-the-app「同じ手順の説明を会話のたびに貼っている」（#33 の言い換え）、cost/what-uses-up-limits「少し使っただけなのに上限に当たる」（#58 の言い換え）。言い換えも外すなら、全分野で同じ基準にしてほしい（ほかの担当も同じ文の重なりを外し始めていて、2026-11-04 の時点で全分野に残る同じ文は basics の sycophancy の1件）
2. **題名のモデルの系統名**：cost/before-using-fable「Fable を使う前に」。M2 で signs からモデルの名前を外したのに合わせ、題名を「最上位のモデルを使う前に」にして Fable を aliases に置くか（id は変えない）。題名の規則が挙げるのは「モデルの世代」で、系統の名前ではないので、変えていない。C2 も迷った点に挙げている
3. **M1 の表にない語の表記**（受け持ちの題名に出るもの）：fast mode（auto モード・plan モードに倣えば「fast モード」）、workflows（features.yaml は「ワークフロー（workflows）」）、web 検索（features.yaml は「Web 検索」）、usage credits、アプリの Auto と Manual、Quick entry。用語集（M7）で決めてほしい。今は元のままにした
4. **（提案・急がない）API の読者の入口**：API の手段の一部が api の分野の外にある（app の how-attachments-are-read#api、models の effort-levels の API の面、cost の reading-api-pricing・check-billing-path、basics の why-prompt-caching・tokens）。分野の入口（生成）に、surfaces に api を持つほかの分野のページを「ほかの分野の API の節」として並べる案（api#3）。今は feature-to-api-mapping の related が受け皿

## 6. 検査の結果

`python3 tools/check_catalog.py --field <分野>`（最後に流したとき。分野のファイル 23・ページ 361）：

| 分野 | エラー | 警告 |
| --- | --- | --- |
| surfaces | 0 | 0 |
| models | 0 | 0 |
| cost | 0 | 0 |
| api | 0 | 2（比例則） |
| app | 0 | 0 |

- 全体：エラー 0・警告 4（比例則 4。うち2件が api）
- 残した警告（M9。理由は各ページの notes）：
  - feature-to-api-mapping（任せる）：level は 00 の L3 のまま。長い作業を任せてキャッシュや自動の要約に出会い、理由を知りたくなる段階で初めて要り、プログラムを書かずに読める。対応関係の表で、自律・並列・無人・権限の緩和を広げない
  - prompt-caching-in-practice（仕組みにする）：level はそのまま。API で同じ前置きを繰り返し送る仕組みを作る段階で初めて要る。費用と待ち時間の整え方で、任せる幅を広げない
- 道具が見ない点も確かめた：aliases が題名の語と重ならないこと、変えた要約が120字以内で変わりやすい値を含まないこと、足した sign に数値とプラン・モデルの名前がないこと

## 7. 確かめていないこと、迷った点

- 一次資料は開いていない（Web を使わない）。「Claude への指示」は M1 のとおりにし、画面の名前は確かめていない
- stateless-messages-api の要約は、message threads（beta）では API が会話を一時的に持つ（research/22 #40）ので、「会話を覚えない」と言い切らず「基本の形は状態を持たない」と書いた
- #61：choosing-a-model の「一番賢いモデルを常に使うべきか知りたい」を同じ意味と見て足さなかった。「一番」と「いちばん」の表記は揃えていない（文体の規則を決めるときに直せる）
- memory-faq の題名（消したのに覚えている・話が混ざる）は、読者の言葉の題名として残した。題名は逆引きの signs ではないので、M2 の重なりにはしなかった
- effort-levels の「簡単な作業なのに返答が遅く、使用量も多い」は too-slow の「簡単な質問なのに長く考え込む」と近いが、too-slow の文は 00 §4 の33項目ではないので残した
- 受け持ちのファイルの open_issues は消していない（open-issues.md の番号の元なので）。扱いの記録はこの報告の §1
- before-using-fable の題名（§5 の2）と、M1 の表にない語（§5 の3）は、用語集の決定に合わせて工程4で直せる
