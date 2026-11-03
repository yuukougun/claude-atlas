# 工程3 C5：分野の目次（app・api）の報告

- 担当：C5（2026-11-04）
- 書いたもの：[planning/catalog/app.yaml](../../catalog/app.yaml)（20ページ）、[planning/catalog/api.yaml](../../catalog/api.yaml)（11ページ）
- 検査：`python3 tools/check_catalog.py --field app` はエラー0・警告0。`--field api` はエラー0・警告2（比例則。§5）
- 書き終える前に、ほかの22分野のファイルが出そろったので、全体の検査を見て参照を合わせた（§4.3）

## 1. 書いたファイルとページ数

| 分野 | registry の候補 | pages | merged | dropped | 新規 |
| --- | --- | --- | --- | --- | --- |
| app | 22 | 20 | 2 | 0 | 0 |
| api | 14 | 11 | 3 | 0 | 0 |

| 分野 | 優先度 | レベル | 型 | volatility |
| --- | --- | --- | --- | --- |
| app | 必須 11・推奨 6・任意 3 | 使う 2・整える 12・任せる 4・仕組みにする 2 | feature 18・comparison 2 | 中 11・高 9 |
| api | 必須 2・推奨 6・任意 3 | 任せる 2・仕組みにする 6・回す 3 | concept 4・feature 5・comparison 2 | 中 8・高 2・低 1 |

- 章：app は「指示と記憶（6）・資料と長い会話（2）・調べる・作る（5）・つなぐ・足す（3）・任せる（2）・チームとモバイル（2）」、api は「アプリと API の対応（2）・API の主な機能（5）・エージェントを組む（4）」
- 優先度は 00 §3 のまま変えていない
- registry の見当から level を変えたもの：artifacts-as-apps と shared-projects-and-org-skills を任せるから仕組みにするへ（常設化と共有の段階）。designing-agent-tools を回すから仕組みにするへ（MCP サーバーや自作のツールを作るのは仕組みにする段階）
- 題名：アプリの機能名は、ヘルプセンターの日本語版の訳語（research/27 §3.1）に合わせた。プロジェクト・メモリ・シークレットチャット・アーティファクト・リサーチ・コネクタ・スキル・音声モード。英語の名前は aliases に置いた。API の題名は英語の名前のまま（Platform の日本語版の訳語は工程2で調べていない）で、prompt caching だけ Claude Code の日本語版の多数派の「プロンプトキャッシング」にした
- 「タスクと定期実行（旧 Cowork）」は「タスクと定期タスク（Cowork）」にした。ヘルプセンターが今も Claude Cowork の名前を使っている（research/22 §5）。「定期タスク」は delegate の題名とそろえた
- volatility の高は、2026年に作り直されたか、段階的に展開中のもの（メモリ・アーティファクト・スキル・プラグイン・タスク・権限モード・長い会話の上限、API の beta）

## 2. merged・dropped にした候補と、新しいページ

merged（5）：

| 候補 | まとめた先 | 理由 |
| --- | --- | --- |
| searching-past-chats（過去チャットの検索） | app の how-memory-works（節 chat-search） | メモリと取り違えやすい別の機能だが、単独では「メモリとの違い」のほかに判断がない |
| research-and-writing-in-the-app（アプリでの調べもの・文章作成のレシピ） | recipes の research-and-reports | 用途ごとの進め方は recipes が持ち（design §4.2）、面ごとに分けない（D9）。recipes の担当がアプリのタブを置いた |
| files-pdfs-and-images（ファイル・PDF・画像の扱い） | app の how-attachments-are-read（節 api） | アプリの添付と同じ話題で、面のタブにした（D9）。任意で、API の分野は概念と対応関係だけを書く |
| managed-agents-basics（Managed Agents） | api の sdk-comparison（節 managed-agents） | beta の機能。独自の判断は「ループと環境を Anthropic に預けるか」で、比較そのもの |
| prompt-evals-intro（プロンプトの評価入門） | eval の measure-changes | 評価の指標は eval の受け持ち（design §4.2、D4）。eval の担当も同じ案を出し、中身（成功の基準・task などの語・pass@k と pass^k・batch-api-basics への関連・台帳の console-prompt-generator）を取り込んだ |

dropped：なし。

新規：最終的にはなし。会話の共有のページ（sharing-chats。research/26 §3.2 で仕様が確かめられた）を足したが、取り下げた。safety の担当が shared-artifacts-and-files を「共有リンクと公開アーティファクトの扱い」に改め、優先度を推奨に上げて、共有の仕様（写し・見られる人・取り消し）を持ったため。app からは4ページがそれを関連で指す。

## 3. wave: 1

app・api は核の分野でないので付けていない。ただし、前提でたどって第一波に入る app のページが3つある（どれも必須で、前提の鎖は短い）。

- where-to-put-instructions ← symptoms の repeating-the-same-explanation（前提は basics の attention-budget だけ）
- how-attachments-are-read ← symptoms の skipped-later-pages（前提なし）
- how-memory-works ← symptoms の unexpected-memories（前提なし）

## 4. ほかの分野への提案と new_features

### 4.1 open_issues の要約

app.yaml：

1. safety：shared-artifacts-and-files に、共有の操作（特定の人への招待・公開リンク・共有した会話の更新・Team と Enterprise の組織の中だけの共有）も短く入れてほしい
2. surfaces と features：new_features の app-tasks を、choosing-a-surface と where-it-runs の tracks にも入れてほしい（surfaces の担当の提案のとおり）
3. changes とメイン：台帳に「Styles で応答の調子と形式を揃える」を足すかを決めてほしい（changes の担当も同じ提案をしている。台帳の id は registry にあるので、足すならメインが直す）
4. japanese：keep-replies-in-japanese のアプリのタブから where-to-put-instructions を指してほしい（claude.ai には返答の言語を固定する設定がない。research/27 #15）
5. start の glossary：アプリの訳語と、取り違えやすい語（アプリのメモリと Claude Code のメモリ・自動メモリ、アプリの Styles と Claude Code の output style）を用語集で決めてほしい
6. 決めきれなかった点：memory-faq を how-memory-works にまとめるか（§6）
7. 確かめていないこと（作者に頼むなら一度にまとめる）：§6 の一覧

api.yaml：

1. delegate：choosing-automation の related の managed-agents-basics を外してほしい（同じ related に sdk-comparison がある）。全体の検査で、app・api が原因のエラーはこの1件だけ残っている。あわせて batch-and-p-loops で、Claude Code の /batch と API の Message Batches API の取り違えに触れてほしい
2. 決めきれなかった点：API の題名の訳語。files-pdfs-and-images をアプリのページにまとめたので、API の読者が分野の一覧から見つけにくくなるおそれ（feature-to-api-mapping から how-attachments-are-read#api を指して補った）

### 4.2 new_features（9）

| id | 分野 | 中身 |
| --- | --- | --- |
| app-tasks | app | アプリのタスクと定期タスク（Cowork）。README §5 の scheduled-tasks は Claude Code の行 |
| app-permission-modes | app | アプリの権限モード（Auto・Manual）とプランごとの既定 |
| app-plugins | app | アプリのプラグイン。使えるプランと動く範囲が Claude Code と違う |
| file-uploads | app | アップロードの境目（図も読むページ数・大きさと数の上限） |
| app-context-management | app | 長い会話の自動のコンテキスト管理と長さの上限 |
| message-threads | api | message threads（beta、2026-11-02。research/22 #40） |
| api-compaction | api | API の compaction（beta） |
| context-editing | api | context editing（beta） |
| memory-tool | api | memory tool |

chat-sharing は safety の担当が new_features に入れたので、重ねていない。

### 4.3 ほかの担当の決定に合わせて直したこと

- 参照の直し：context の managing-context-in-the-app は tidy-the-desk#in-the-app に、surfaces の unified-claude は choosing-a-surface に替えた。claude-code-vs-cowork は外した（choosing-a-surface が前提にあり、同じページを関連に置けないため）
- 提案を取り込んだもの：team（rolling-out-to-teams・org-managed-settings-and-mcp）、safety（artifacts-overview から shared-artifacts-and-files）、delegate（tasks-and-schedules-in-the-app から loop-and-scheduling・cloud-schedules。sdk-comparison から choosing-automation）、surfaces（タスクの実行場所の節と where-it-runs）、basics（stateless-messages-api は rereads-whole-history を前提にし、API に固有の内容に絞る。tool-use-loop は agent-loop を前提にする）
- symptoms の unexpected-memories を、how-memory-works と memory-faq から関連で指した
- 取り込まれたのを確かめたもの：recipes（research-and-reports）、eval（measure-changes）、cost（reading-api-pricing・check-billing-path）、extend（アプリのタブ）、models（effort-levels のアプリの面）、verify（checking-citations から citations-basics）、surfaces（peripheral-products から artifacts-overview#claude-design）。台帳の lower-temperature・budget-tokens・thinking-tags は、ほかの分野のページに付いた

## 5. 検査の結果

- `--field app`：エラー0・警告0
- `--field api`：エラー0・警告2。どちらも [比例則] で、notes に理由を書いて残した
  - feature-to-api-mapping（任せる）：機能と概念の対応表で、任せる幅を広げる内容ではない
  - prompt-caching-in-practice（仕組みにする）：費用と待ち時間の整え方で、任せる幅を広げる内容ではない
- 全体（2026-11-04、23分野・361ページ）：エラー4・警告6。app・api が原因のエラーは delegate の1件（§4.1）。ほかの3件は japanese がまとめた候補への参照（basics・extend）で、app・api とは関係しない
- 道具が見ない点も手元で確かめた。aliases が題名の語と重ならないこと（1件を直した）、level があるページに level_evidence があること、summary・signs・題名に数字がないこと（summary は最長でも110字）、materials と notes に個人と第三者の名前がないこと（企業の記事の名前を1か所外した）

## 6. 確かめていないこと、迷った点

確かめていないこと：

- 一次資料は開いていない（Web を使わない指示）。アプリの事実は 02（2026-10-29）と、工程2の報告 research/22・23・26・27（2026-11-03）による
- 工程2でも確かめられていない点：Styles のメニューが今も画面に出るか、Free でプロジェクトの指示を使えるか（ヘルプセンターの記事の間で食い違う）、Desktop の新しい設定画面で claude_desktop_config.json を開く入口、アプリの権限モードの Desktop と Web の既定、日本語の画面の項目名、RAG mode で読み方がどう変わるか
- アプリの Auto と Claude Code の auto mode が同じ分類器かは確かめていない。本文で同じものと書かないよう notes に書いた
- アプリは制作の環境で試せない。検証ノートが要るときは、作者にまとめて頼む

迷った点：

1. memory-faq を how-memory-works にまとめるか。00 は両方を必須で別に立て、逆引き（00 §4）も両方を指す。symptoms の unexpected-memories ができて困りごとの入口はそちらにもあるが、symptoms・safety・extend の担当は memory-faq を「アプリの操作の本体」として指しているので残した
2. 会話の共有のページを app に置くか、safety に任せるか。safety の担当の決定を見て、safety に任せた
3. 題名の訳語の方針（アプリは日本語、API は英語）。用語集の決定で、まとめて見直してほしい
4. 添付のページ（使う段階・必須）に API のタブを足したこと。API の節は level を仕組みにするにした
5. Message Batches API と citations は、薄いが名前で引かれる機能なので、任意のまま残した。citations は verify の checking-citations が API の面から指している
6. 前提は、まとめられそうな候補や任意の候補を避け、循環しにくい上流の概念（basics・start）と必須のページに絞った。症状のページは、前提ではなく関連に置いた（症状の側がこちらを前提にするため）
