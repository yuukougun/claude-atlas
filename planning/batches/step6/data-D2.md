# 工程6b 担当 D2 の報告（features：アプリ・API・SDK・面をまたぐもの・プランと上限・組織と提供の経路）

- 版：2026-11-04。指示は [brief-data.md](brief-data.md)（§4 の D2 の行）と [brief-build.md](brief-build.md) の §1〜§3・§5
- 下書き：[data/D2.yml](data/D2.yml)（features 52・sources 105・domains 5。names・facts・advice は空）

## 1. 作ったファイルと中身の要約

| ファイル | 中身 |
| --- | --- |
| `planning/batches/step6/data/D2.yml` | features.yaml の5つの区分の52項目（アプリ 23・API・SDK 19・面をまたぐもの 1・プランと上限 5・組織と提供の経路 4）。各項目に題名・主のページ（page）・面・成熟度・強制力（当てはまるものだけ）・入った時期と版・照らす英語の語（match_terms）・出典・確認日・状態・注。出典 105件（ヘルプセンター 44〔うち styles の記事は写しの URL〕・Claude Platform の文書とリリースノート 35・claude.com の料金と文書と公式ブログ 13・Claude Code の文書 12・Claude Apps の旧いリリースノートの写し 1）と、使ったドメイン 5件 |
| `planning/batches/step6/data-D2.md` | この報告 |

- 状態：確認済み 51・未確認 1（styles。§5）
- 成熟度：GA 36・beta 9・書かない 7（styles・refusals・plans・usage-limits・usage-credits・api-credits・wrap-up-allowance）
- 入った時期（since）：39項目に書いた。書けなかった13項目は §5
- 強制力：お願い 4（project-instructions・personal-instructions・styles・app-skills）、鍵 2（structured-outputs・app-permission-modes）
- 第一波のページが tracks で指す D2 の機能は22（projects・project-instructions・app-memory・chat-search・incognito・styles・personal-instructions・file-creation・web-search・research・connectors・app-skills・file-uploads・files-api・adaptive-thinking・citations・token-counting・refusals・plans・usage-limits・usage-credits・wrap-up-allowance）。52項目を全部入れたので、第一波の分は欠けていない

## 2. 確かめたこと

- **一次資料**：2026-11-04 に全部をその場で開いて読んだ（curl で取得し本文を読んだ。ヘルプセンターは記事の JSON-LD の dateModified を published にした）。Claude Platform の文書は Markdown 版（`.md`）の front matter の `featureMetadata`（status・supportedPlatforms・betaHeader）を成熟度と使えるプラットフォームの根拠にした。日付は Help Center のリリースノート（2025-08〜）、Platform のリリースノート（2024-05〜）、Claude Apps の旧いリリースノートの写し（2024-05〜2025-05）、claude.com の公式ブログで確かめた
- **AI の利用の指定**：`uv run python tools/check_noai.py` で support.claude.com・platform.claude.com・claude.com・code.claude.com・web.archive.org を確かめ、どれも noai・noimageai の指定がない（support.claude.com は meta robots が all）。結果を `domains` に書いた。docs.anthropic.com・www.anthropic.com も指定がない（どちらも転送されるだけで、出典の URL には使っていない）
- **写し**：Internet Archive は、すでにある写しを2件読んだだけ（新しい写しは作っていない）。styles の記事（2026-07-10 の写し。元の記事は 404）と、Claude Apps の旧いリリースノート（2025-06-28 の写し。元の URL は今 Help Center のリリースノートへ転送される）
- **形の検査**：scratchpad のスクリプトで、リポジトリの読み方（`tools/lib/yamlio`。日付を文字列で読む）で下書きを読み、まとめた後の形（facts・features・names → `schema/facts.schema.json`、domains・sources → `schema/sources.schema.json`、advice → `schema/outdated-advice.schema.json`）に、jsonschema（Draft-07・FormatChecker）と `tools/lib/schema.py` の Validator（date・partial-date も見る）の両方で当てて、誤り 0件。あわせて、features の sources の id がすべてあること・使わない出典がないこと・出典の id と URL に重なりがないこと・出典のドメインが domains にあること・52項目が features.yaml の受け持ちと一致すること・主のページが目次にあり、その tracks に機能の id があること・load_timing と context_cost を書いていないことを確かめた
- **第一波**：`tools/check_catalog.py` の first_wave（136ページ）で、第一波のページが tracks で指す D2 の機能を数えた（§1 の22）

## 3. 決めたこと

### 3.1 成熟度と強制力の付け方

- Platform の文書は featureMetadata.status の `stable` を GA、`beta` を beta にした（site.yml の maturities の語彙はこのままで足りる。公式の語は Platform が stable・beta・research preview、ヘルプセンターと claude.com が generally available・beta・research preview・experimental）
- ヘルプセンターと claude.com の文書は本文の表記に従った。beta などの表記がなく、プランで提供と書かれているものは GA とした（明示の「generally available」があるのは Cowork・Excel・PowerPoint・Word のアドインだけ）
- 面で表記が違う computer-use は、主のページ（browser-control）が扱う Cowork と Desktop の表記の beta にし、注に面ごとの表記を書いた（§4 の提案1）
- プランと上限の項目、拒否（refusals）、撤去の途中の styles は語彙に当てはまらないので成熟度を書かない
- 強制力は D14（お願い＝非決定論的な指示、鍵＝決定論的な制御）で、公式の文書が根拠になるものだけに書いた。指示として読まれるもの（Claude への指示・プロジェクトの指示・Styles・スキル）をお願い、制約つきのデコードで形を保証する structured outputs と、動作の前に許可を求める仕組みのアプリの権限モードを鍵にした（Auto の審査は Claude の判断で、Skip は確かめないことを注に書いた）

### 3.2 主のページ（page）

型が feature のページが主になったのは29項目。残りの23項目は、その機能を tracks に持つ feature のページがないか、機能そのものを扱うのが別の型のページなので、次のように決めた。

| 機能 | 主のページ（型） | 理由 |
| --- | --- | --- |
| personal-instructions | where-to-put-instructions（comparison） | tracks に持つ feature のページがない。アプリの指示の置き場所を扱う本体 |
| web-search | search-research-thinking（comparison） | アプリの分野で web 検索そのものを扱うのはここだけ（ほかは概念・レシピ・症状） |
| office-add-ins・claude-in-slack | peripheral-products（hub） | 周辺製品は一覧のページだけにする（D15） |
| chat-sharing | shared-artifacts-and-files（concept） | tracks に持つのはここだけ。目次の注で、共有の操作もここが持つ |
| messages-api・message-threads | stateless-messages-api（concept） | Messages API の形そのものを扱う。sdk-comparison と reading-api-pricing は別の話題 |
| tool-use・server-tools | tool-use-loop（concept） | tool use のループと client tools・server tools を扱う。feature-to-api-mapping は対応表 |
| adaptive-thinking | how-thinking-works（concept） | 思考の仕組みのページ。effort-levels（feature）は effort の段階のページ |
| mcp-connector | feature-to-api-mapping（comparison） | tracks に持つのはここだけ |
| managed-agents | sdk-comparison（comparison） | managed-agents-basics をまとめた先（節 managed-agents） |
| token-counting | tokens（concept） | トークンと数え方のページ |
| api-compaction・context-editing・memory-tool | long-running-agent-context（concept） | API でこの3つを扱う本体 |
| api-rate-limits | rate-limits-and-errors（concept） | tracks に持つのはここだけ |
| refusals | when-requests-are-refused（concept） | 目次の注で、仕組み・面ごとの表示・手段はここが一か所で持ち、症状のページ refused-or-blocked は切り分けだけ |
| plans | choosing-a-plan（comparison） | プランそのものを比べる。how-usage-limits-work は上限のページ |
| usage-limits・wrap-up-allowance | how-usage-limits-work（concept） | 上限の仕組みのページ（wrap-up-allowance は tracks に持つのがここだけ） |
| api-credits | check-billing-path（concept） | tracks に持つのはここだけ |
| team-onboarding | rolling-out-to-teams（recipe） | tracks に持つのはここだけ |

feature のページのうち、分けて書いておく判断：project-instructions は using-projects（プロジェクトのページ。指示だけのページがない）、styles は skills-in-the-app（Styles はスキルへ移り、節 migrated-styles がある）、files-api は how-attachments-are-read（API の files-pdfs-and-images をまとめ、API のタブを持つ）、computer-use は browser-control（surfaces の分野）。

### 3.3 題名・面・出典の書き方

- 題名は features.yaml の仮の題名を、prh.yml と目次の表記（Claude への指示・プロジェクトの指示・シークレットチャット・音声モード・コネクタ・メモリ・リサーチ）に合わせ、公式の英語の名前を括弧に添えた。改名を確かめたものは今の名前にした：claude-in-slack は「Claude Tag（旧 Claude in Slack）」、office-add-ins は「Claude for Microsoft 365 のアドイン」、styles は「スタイル（Styles。スキルへ移行）」。id は目次が tracks で指しているので変えていない（§4 の提案2）
- 面は site.yml の surfaces の順（app・claude-code・api）。Microsoft 365 のアドインと Claude Tag は、アプリの外（M365・Slack）で動くが、claude.ai のプランの製品なので app にし、注に書いた。アプリの機能でも Claude Code で使えると公式が書くもの（artifacts）は claude-code を足した。スキルとプラグインの Claude Code への同期は注に書き、面には足していない
- 出典の id は担当の記号を付けず、ヘルプセンターは `hc-`、Platform の文書は `api-docs-`、Platform のリリースノートは `api-release-notes`、claude.com の文書は `claude-docs-`、公式ブログは `claude-blog-`、Claude Code の文書は `cc-docs-`（brief の例 cc-docs-hooks に合わせた）。URL は転送先（記事の番号つきの今の slug）にした
- 元の URL が今は内容を返さない2件（styles の記事は 404、Claude Apps の旧いリリースノートは別の文書へ転送）は、url に写しの URL を書き、元の URL を note に書いた（転送先の URL にすると別の文書と同じ URL になり、まとめるときに重なるため）

### 3.4 読み込みの時期とコンテキストのコスト（書かなかった）

D1 が語彙を決めるので、値は書いていない。アプリと API の機能のうち、公式の文書に読み込みの時期や文脈の量の記述があるものは次のとおり（D1 の語彙が決まった後、メインが当てる候補）。

| 機能 | 公式の記述（出典） |
| --- | --- |
| projects・project-instructions | プロジェクトの知識は、プロジェクトの会話を始めると常に読まれる（What are skills? の Skills vs. projects）。ナレッジが文脈の上限に近づくと RAG で関わる部分だけを読む（How large is the context window…・How can I create and manage projects?） |
| personal-instructions | 全部の会話に使われる（Understanding Claude's personalization features・What are skills? の Skills vs. custom instructions） |
| app-skills | 名前と説明は常に（1件およそ100トークン）、本体は使うときに（5千トークン未満）、付属のファイルは要るときに（Platform の Agent Skills の表）。ヘルプセンターも関わるときだけ読むと書く |
| app-memory | Claude が会話の中で読み、更新する（リリースノート 2026-07-10）。いつ・どれだけ読むかは書かれていない |
| chat-search | 頼まれたときに道具の呼び出し（RAG）で読む（Use Claude's chat search and memory…） |
| connectors | 道具とコネクタは多くのトークンを使う。10件以上なら Tool access を On demand にすると文脈に余裕ができる（Use connectors…・How do usage and length limits work?） |
| memory-tool | 作業を始める前にメモリのディレクトリを見る（Memory tool） |

当てはまらないもの（値を書かないのが正しいもの）：アプリの chat-sharing・incognito・file-creation・code-execution・web-search・research・voice・app-tasks・app-permission-modes・app-plugins・file-uploads・app-context-management・artifacts・office-add-ins・claude-in-slack・styles、API の全部（memory-tool を除く。messages-api・prompt-caching・structured-outputs・tool-use・batch-api・files-api・adaptive-thinking・citations・server-tools・computer-use・mcp-connector・agent-sdk・managed-agents・token-counting・message-threads・api-compaction・context-editing・api-rate-limits）、refusals、プランと上限の5つ、組織の4つ。圧縮で残るか（survives_compaction）も、アプリと API の機能には公式の記述がないので書いていない（アプリの自動のコンテキスト管理は「全履歴は残り参照できる」とだけ書く）。

### 3.5 食い違い（公式同士が同じ点で違う。両方の出典を sources に残し、注に「食い違い」と書いた）

1. **project-instructions**：個人設定の記事の使い分けの節は「paid plans only」、同じ記事とプロジェクトの記事は Free でもプロジェクトを5件まで作れると書き、指示の設定に制限を書かない
2. **artifacts**：Docs・Slides・Design を、アーティファクトの記事と料金のページは beta と書かず、Cowork とチャットの統合の記事は beta、リリースノート（2026-09-16）は Enterprise で beta と書く
3. **app-skills**：Help Center（2026-10-30 更新）と料金のページは Free でも使え、Help Center は Customize > Skills で管理・組織で配る・共有と公開・Claude Code へ同期と書く。Platform の Agent Skills の文書は claude.ai の custom skills を Settings > Features から上げ、Pro 以上、各人だけ、面をまたいで同期しないと書く。また Help Center は API のスキルを beta と書くが、Platform では 2026-08-19 に beta を外れた
4. **office-add-ins**：M365 の文書は対象を Pro・Max・Team・Enterprise と書き、料金のページは Ultra も含める
5. **file-uploads**：アップロードの記事は会話へのアップロードを1ファイル 500MB まで、ファイルの作成の記事はアップロードとダウンロードを1ファイル 30MB までと書く（facts に置くときにも両方の出典が要る）
6. **plans**：Team の記事は「200k context window」と書き、コンテキストウィンドウの記事は有料のプランの新しいモデルで 1M まで（モデルで違う）と書く

表記の差・古い記述の残り（食い違いには数えない。注に書いた）：app-context-management（「有料のプランで」を書く記事と書かない記事）、chat-sharing（既定の共有のしかたの書き方）、incognito（FAQ に custom styles の語）、usage-credits（API credits の記事に旧名 Extra usage）、computer-use（Help Center の記事は beta、2026-03-23 のリリースノートと Claude Code の CLI の文書は research preview。面と時期が違う）。

## 4. 提案

1. **computer-use を面で分けるか**（メインの判断）：API の computer use tool（computer_toolset_20260801 は stable）と、Cowork・Claude Code の computer use（beta・research preview。Pro・Max・Ultra だけ）は、成熟度・プラン・設定が違う。compaction と api-compaction のように id を分けると、バッジが面ごとに正しくなる。分けるなら、API の行は api の分野のページ、今の行は browser-control が主
2. **claude-in-slack の id**：今の名前は Claude Tag で、前の Claude in Slack は 2026-08-03 に切り替わった。id を claude-tag に改めるなら目次（peripheral-products の tracks）も直す。改めないなら今のまま（名前の変更は names で持つ）
3. **D3 の names の候補**（確かめた事実と出典。時期を確かめられたものは日付つき）
   - Claude in Slack → Claude Tag（2026-08-03 に切り替え。hc-claude-tag）
   - Max 20x → Ultra（2026-10-30。hc-ultra-plan、claude-blog-research の編集の注）
   - Styles → スキル（2026-06-01 に告知。hc-styles-to-skills の写し）
   - Integrations → コネクタ（2025-05-01 の記事は Integrations。今の Help Center は connectors。改名の日は確かめていない）
   - Claude Code SDK → Claude Agent SDK（cc-docs-agent-sdk-migration。日付は文書にない）
   - Vertex AI → Google Cloud's Agent Platform（Claude Code の文書の「formerly Vertex AI」。Platform の文書は Claude Models on Google Cloud。日付は確かめていない）
   - Cowork の権限モード：Ask before acting → Manually approve、Act without asking → Skip all approvals（hc-cowork-start。日付は確かめていない）
   - Extra usage → usage credits（2025-08-20 のリリースノートは Extra usage。今は usage credits）
   - Customize → Plugins（2026-10-29 から順に。Free〜Team は 2026-11-09 に generally available、Enterprise は 2026-11-30。hc-plugins-page）
   - Analysis tool → Code execution and file creation（写しの 2024-10-24 は Analysis tool。改名の日は確かめていない）。設定の名前は新しい画面で Create and edit files
   - Workbench → playground（2026-08-18。api-release-notes）
   - 設定の画面：Instructions for Claude → Instructions、Settings > Memory → Settings > Your Claude（新しい設定の画面。hc-personalization・hc-memory）。Cowork の Global instructions は Claude への指示にまとまった
4. **facts の候補**（6b の受け持ちにないが、見つけたので書く）：アップロードの上限（§3.5 の5）、Team の文脈の大きさ（§3.5 の6）、Wrap-Up Allowance の頻度、usage credits の失効（日本などは 2026-09-10 以降の購入から6か月）、月の API credits の額（Max $100・Ultra $200・Team は席ごとで上限 $500）、プランの料金と倍率、message threads の寿命（最後の要求から5分、1時間以内に消す）、rate limits の段（Start・Build・Scale）
5. **主のページが第一波にない機能**：第一波のページが tracks で指す22のうち12（projects・project-instructions・incognito・styles・file-creation・research・connectors・app-skills・citations・refusals・plans・usage-credits）は、主のページが第一波にない（第一波の公開の間、用語索引で主のページが stub のままになる）。用語索引が公開中のページへ落とすか、主を第一波のページにするかはメインの判断
6. **features の volatility**：既定の高（30日）のままにした。長く変わっていない API の機能（messages-api・tool-use・prompt-caching・batch-api・token-counting・citations）は中（90日）にすると点検の量が減る。決めるのはメイン
7. **用語集（start の glossary）への材料**：Help Center の日本語版の題名の訳語は、シークレットチャット・音声モード・コネクタ・スキル・アーティファクト・プロジェクト・メモリと目次の表記に合う。合わないのは、ウェブ検索（目次は web 検索・Web 検索）、調査機能（目次はリサーチ）、使用クレジット（usage credits）、月間 API クレジット、ラップアップ許容量（Wrap-Up Allowance）、使用量と長さの制限（利用上限）。決めていない（本文は読まず、題名だけを見た）

## 5. 確かめていないこと

- **styles（未確認）**：移行の告知は写しで確かめたが、今の画面に styles のメニューが残るか（移行が終わったか）は一次資料で確かめられない。記事は 404、シークレットチャットの記事に custom styles の語が残る。画面で確かめるには作者か画面を見られる道具が要る
- **入った時期が分からないもの**（since を書いていない13項目）：project-instructions・voice・app-permission-modes・file-uploads・chat-sharing・messages-api（Platform のリリースノートの始まりより前）・agent-sdk（改名の日も）・api-rate-limits・refusals・plans・usage-limits・otel-telemetry・cloud-providers。wrap-up-allowance は資格の条件の版（2.1.277）だけで、導入の日付は記事にない。usage-credits の個人のプランへの公開の時期も
- **Claude Code の CHANGELOG** は開いていない（版は Help Center と Claude Code の文書の記述から：wrap-up-allowance 2.1.277、team-onboarding 2.1.101、スキルとプラグインの同期 2.1.273、拒否の分類ごとの切り替え 2.1.219）。CHANGELOG の版と合うかは D1 か点検で照らす
- 食い違い（§3.5）のどちらが今の正しい姿か。とくに app-skills（Free で使えるか・組織で配れるか・Claude Code へ同期するか）と project-instructions（Free で使えるか）。展開の途中（新しい Claude の体験・Plugins のページ）で記事の書き方がそろっていない可能性がある
- ヘルプセンターの記事は展開の状態で中身が変わる（新しい Claude の体験・新しい設定の画面・新しいメモリの体験）。2026-11-04 に読んだ版で書いた
- Google Workspace の Claude（Docs・Sheets・Slides）、Claude Duet・Claude Science・Claude Security は features.yaml にないので調べていない。peripheral-products が扱うなら、id を足すかはメインの判断
- 日本語版のヘルプセンターは題名だけを見た（本文の訳語は数えていない）
