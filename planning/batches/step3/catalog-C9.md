# 工程3 C9：分野の目次（delegate・team）の報告

- 担当：C9（2026-11-04）
- 共通の指示：[brief-catalog.md](brief-catalog.md)。形式と規則は [catalog/README.md](../../catalog/README.md)

## 1. 書いたファイルとページ数

| ファイル | ページ | 優先度 | レベル | 型 | registry の候補 |
| --- | --- | --- | --- | --- | --- |
| [planning/catalog/delegate.yaml](../../catalog/delegate.yaml) | 22 | 必須 7・推奨 12・任意 3 | 任せる 3・仕組みにする 11・回す 8 | concept 6・feature 12・comparison 2・recipe 2 | 23（採る 22・まとめた 1） |
| [planning/catalog/team.yaml](../../catalog/team.yaml) | 16 | 必須 1・推奨 8・任意 7 | 仕組みにする 16 | concept 6・feature 3・comparison 1・recipe 6 | 16（採る 16） |

章：

- delegate：任せる前の判断（5）・続けさせる（2）・並べる（8）・定期と無人の実行（7）
- team：導入と決まり（5）・レビューと判断（7）・管理と契約（4）

### 1.1 比例則（design §3.1 の4）

delegate の22ページは、どれも verify・eval・enforce・safety のページを前提か関連に持つ。任せる幅を広げるページの多くは、守りのページを前提に置いた（requirements §3.3 では、上の段のページは確かめる・縛るのページを前提に持つ）：

- five-questions-before-delegating（verification-ladder・permission-rules）、goal-until-done（evidence-not-reports）
- loop-and-scheduling・agent-view-and-background・agent-teams-experimental（what-auto-mode-stops）
- headless-basics・dynamic-workflows（permission-rules）、cloud-schedules（lethal-trifecta）、github-actions-with-claude（protecting-secrets）
- automated-pr-review（independent-review）、compare-hypotheses-in-parallel（experiment-log）
- open-ended-loop-trap・what-not-to-delegate・is-the-task-ai-suited（verifier-defines-problem など）

ほかのページは前提をたどると守りのページに届き、related にも直接持つ。

### 1.2 requirements §6.3（自律ループで戦略を改善させる手順は書かない）

- goal-until-done：反復は、仕様の決まった実装の作業に限り、停止条件を付ける（notes と節 spec-tasks-only）
- open-ended-loop-trap：なぜ勧めないかと、閉じた反復との違いだけを書き、組み方は書かない
- compare-hypotheses-in-parallel：仮説・物差し・採否は人が決め、AI に探索を回させる手順にしない

### 1.3 工程2で確かめた事実の反映

- /goal の判定役は会話しか読まない（requirements §10.3）：goal-until-done の summary・signs・節 evaluator-reads-conversation。雛形 A-14 は、git status の出力を会話に出させる形に直してから載せる
- hooks がワークフローの担当で走るかは文書にない（research/28 #4）：dynamic-workflows の notes。確かめるまで、hooks だけに頼る縛りは書かない。permissions と sandbox は担当にも効くと文書にある（research/28 #3）ので、そちらを勧める
- Max と Ultra（research/22 #32〜#35・research/26 §3.11）：本文はプランに中立に書き、差は数値ファイルへ送る。choosing-automation・enterprise-vs-team-plans・goal-until-done（上限で止まったとき）の材料に入れた
- research/22 §3.3 が delegate に挙げる変更（#7・#10・#11・#21・#24〜#28・#36）と team に挙げる変更（#13・#22・#38・#39）は、どれかのページの materials に入れた

## 2. まとめた候補・採らなかった候補・新しいページ

### 2.1 merged

| 候補 | まとめた先 | 理由 |
| --- | --- | --- |
| homemade-loops（自作ループ（Ralph など）の現在） | goal-until-done の節 from-homemade-loops | 残る考え方（状態をファイルに書く・機械的に完了を判定する・反復に上限を置く）は /goal の節で足りる。置き換えの経緯は台帳の ralph-loops が持つ。独自の判断が薄い。Ralph は aliases に置き、毎回新しい文脈から回す -p のループは batch-and-p-loops に書く |

dropped はない。新しいページも足していない（registry の39候補で、requirements §4.4 の delegate の6つと team の6つを含めて足りた）。

### 2.2 「チームで使う意味」（registry の notes で team の担当に残された判断）

足さない。理由：

- 根拠の行は11の p56#52 の1件だけで、【2026-11-03 注記】が付いている（P&G の実験の人数が 791 人と、要旨の 776 人で食い違う）
- research/24 B-43 によると、行の中心の「上位10%の解が約3倍」は要旨になく、確かめられていない
- catalog/README §4.5 の5により、summary と signs の根拠にできない。残るのは研究の紹介だけのページになる（design §4.1 の5）
- チームで AI を使う意味の判断は、curb-sycophancy-and-overtrust（人どうしの批評）・ideate-independently（独立した案出し）・separate-roles（役割）が持つ。研究は、論文の本文で人数と数値を確かめてから、これらのページの根拠の候補にする

この決定は team.yaml の open_issues の1件目にも書いた。

### 2.3 registry から変えたもの

**題名**

- five-questions-before-delegating：「委任の段階と、任せる前の五つの問い」から「任せ方の段階と、無人で走らせる前の五つの問い」へ。start の roadmap が使う「委任の段階」（読者の段階）と、作業ごとの任せ方の段階を取り違えないため
- 変わりやすい数と成熟度を外した
  - choosing-parallel-modes：「並列の五方式の選び方」から「並列の方式の選び方」へ
  - loop-and-scheduling：「三方式」から「方式」へ
  - agent-teams-experimental：「（実験的）」から「（複数の Claude に分担させる）」へ
  - dynamic-workflows：括弧の「ultracode」（改名の経緯がある起動の語）を機能の説明に替え、ultracode は aliases に置いた
- open-ended-loop-trap：「開いた改善ループの罠」から、読者が引く言い方の「AI に改善を回させ続ける罠（開いたループ）」へ。nav_title に元の題名を残した
- 平文にした：headless-basics・bare-mode・batch-and-p-loops の題名と要約から、バッククォートを外した
- team
  - enterprise-vs-team-plans：「（概念）」を外した
  - org-managed-settings-and-mcp：「組織に設定と MCP サーバーを配る（managed settings）」にした（enforce の managed-settings-enforcement と区別するため）
  - via-cloud-providers：Vertex を Vertex AI にした

**level**

- team の org-managed-settings-and-mcp・audit-logs-and-telemetry・via-cloud-providers を、registry の見当の「回す」から「仕組みにする」に改めた。組織に配って常設化するのは「仕組みにする」で、「回す」（並列・無人・定期・プログラム）ではない
- team は16ページ全部が「仕組みにする」になった
- delegate の level・priority・type は registry の見当のまま

**優先度**

新しい候補（delegate 6・team 7）は C0 の見当のまま決め、理由を各ページの notes に書いた。根拠が推論や類推のもの（is-the-task-ai-suited・ideate-independently など）は必須にしない。

## 3. wave: 1

付けていない（delegate と team は第一波の核の分野ではない）。

## 4. ほかの分野への提案と new_features

### 4.1 open_issues（最後に確かめた時点で、まだ入っていないもの）

- changes（C1）：outdated-advice-ledger の related にある homemade-loops を、goal-until-done#from-homemade-loops に替える。今は changes.yaml に参照のエラーが出ている
- start（C1）：terminology の節 definitions で、「委任の段階」（読者）と「任せ方の段階」（作業）を分ける
- cli（C4）：permission-modes-overview の related に headless-basics と agent-teams-experimental を足す
- api（C5）：sdk-comparison の related に choosing-automation を足す（自分の作業の自動化と、製品への組み込みの境目）
- symptoms（C12）：stuck-in-a-check-loop・wont-rethink-approach・keeps-stopping・claims-done-but-isnt から、goal-until-done・open-ended-loop-trap を related で指す
- cost（C2）：choosing-a-plan の related に enterprise-vs-team-plans を足す

**執筆の前に確かめること**：無人で走らせる前の五つの問いと、/batch・-p のループの書き方が、2026-10-27 ごろに書き直された今の Best practices にあるか（research/23 §3.1）。

**ほかの担当がすでに取り込んでいたもの**（2026-11-04 に確かめた。各 open_issues の最後の項に一覧）：

- start・judgment・safety・enforce・extend・recipes・contest・verify・eval・cli・app・cost・context の多くのページが、delegate と team のページを指していた
- enforce の managed-settings-enforcement は org-managed-settings-and-mcp#delivery を指していて、境界の分け方が合っている。enforce が持つのは設定のキーと強制の仕組み、team が持つのは配る経路・グループごとの設定・MCP の許可である
- contest の formats-and-ai-fit は format-cheatsheet にまとめられ、そこから is-the-task-ai-suited が指されている

### 4.2 new_features（12）

- delegate（8）：code-projects（Claude Code の Projects）・batch-command（/batch）・bare-mode・safe-mode・auto-continue（上限での自動の継続）・monitor-tool・managed-code-review（Code Review）・ultrareview
- team（4）：team-onboarding・otel-telemetry・usage-analytics-api・cloud-providers

## 5. 検査の結果

`python3 tools/check_catalog.py --field delegate` と `--field team`（最後の実行で分野のファイル20・ページ305）：

- delegate：エラー 0・警告 0
- team：エラー 0・警告 1
  - 比例則：ideate-independently。案出しの手順で、任せる幅を広げる内容ではない。守りの分野のページへの自然な関連もないので、notes に理由を書いて残した

道具は、分野のファイルがまだない分野への参照を確かめない。そこで別のスクリプトで、registry の値を使って確かめた。見たのは、id があるか・まとめられた候補を指していないか・レベルの逆転・必須の前提が必須か・台帳の id である。問題は0件だった。

途中で、ほかの担当がまとめた3つの候補を指していたので、まとめ先に替えた：

- formats-and-ai-fit → format-cheatsheet#why-formats-differ
- insight-patterns → 外した（think-before-asking はすでに related にある）
- claude-code-costs → what-uses-up-limits#find-what-uses-it
- あわせて、eval でまとめられた stratified-and-worst-case への参照を外した（measure-changes はすでに related にある）

## 6. 確かめていないこと・迷った点

### 6.1 確かめていないこと

- 一次資料は見ていない（指示どおり Web を使わない）。機能の名前・成熟度・既定は、research/01（2026-10-29 の確認）と工程2の報告による。特に次は執筆の前に確かめが要る
  - Claude Code の Projects（public beta）と Code Review（研究プレビュー）の今の状態
  - /goal の条件の上限と判定のモデル
  - 定期タスクの失効の日数
- 11 第1〜2節の行は、11 の要約で読んだ。作業ノート（11a〜11c）は一部しか読んでいない。補完調査（10）の本文と付録A の雛形（A-3・A-14）は、直接は読んでいない
- 前提にしたほかの分野のページの level・priority は、20の分野のファイルと registry の値で確かめた。この後にほかの担当が変えると、逆転や必須の前提の警告が出うる
- 機能の id の提案（new_features）は、ほかの担当の提案と重なるかを見ていない

### 6.2 迷った点

- **並列のページの level**：「回す」の定義には並列が入っている。ただし、並列を始める前の判断（humans-set-the-parallel-limit）と最初の手段（choosing-parallel-modes・parallel-with-worktrees・agent-view-and-background）は、00 と registry のとおり「仕組みにする」にした。大規模・無人・プログラムからの実行を「回す」にした
- **review-bottlenecks（team）と humans-set-the-parallel-limit（delegate）の境目**：一人の並列の本数は delegate、チームのレビューの流れは team に分けた。どちらも「並列にしたら疲れた」で引かれる（00 §4）。疲労の数値は小さな標本の自己申告なので、条件を添えるよう notes に書いた（research/25 P7）
- **choosing-automation（delegate）と sdk-comparison（api）の境目**：自分の作業を自動で回す比較は delegate、製品に組み込む比較は api にした
- **what-not-to-delegate の型**：握るものの判断なので judgment の型も考えたが、registry のとおり concept にした（判断例は本文に置ける）
- **automated-pr-review の置き場所**：team のレビューのページと近いが、registry のとおり delegate に置き、team の risk-tiered-approval・review-bottlenecks と related で結んだ
- **五つの問いの出典**：00 §3 分野12 と 05 §1-2 は公式の Best practices とする。Best practices が書き直されたので、今の版にあるかを執筆の前に確かめる（open_issues に書いた）
- **ほかの担当との調整**：ほかの担当が並行して書いているので、提案のうち取り込み済みのものは open_issues から外した。外したものは「取り込み済み」の項に残した
