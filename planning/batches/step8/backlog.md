# 工程8：後でまとめて扱うもの

[rules.md](rules.md) の「後でまとめて扱うもの」。バッチの終わりに足していく。

## 推奨R3（TR-R3）

### 強制力（enforcement）の値の案（お願い・鍵・モデルの判定・なし。decisions 2026-11-05「強制力の語彙」の線引き）

- agent-sdk（agent-sdk-basics）：なし（機能全体では決まらない。権限・フックの側が決める）
- github-actions（github-actions-with-claude）：鍵とお願いの混在。起動を担うだけなら「なし」、権限（permissions・許可ツール）は鍵、依頼文はお願い。1 つに決めるなら「なし」を推す
- btw（side-questions-btw）：なし（write.md の proposal のとおり。確認済み、cc-docs-interactive-mode）
- scheduled-tasks（cloud-schedules）：なし（起動を担うだけ。止めるのは権限の側）。依頼文はお願い、保護ルール・環境は鍵の混在
- bare-mode：鍵（起動時に読み込みを止める。道具の許可は絞らない点は note に）。足したら要点を目印に置き換える

### 用語集に足す語

- settingSources（agent-sdk-basics）・path traversal（保存先のパスが許す範囲の外へ出る攻撃。long-running-agent-context）・stateless（状態を持たない）・ZDR（ゼロデータ保持）・HIPAA 対応・評価器（点や正しさを提出の前に自分で測る道具。ローカルテスタと同族）・アブレーション・Project instructions（画面の名前。prh は「プロジェクトの指示」を要求。例外か用語集か）
- 伴走（人が途中を見ながら一歩ずつ方向を直して進める協業の形）・委託（完了条件を渡して任せ、戻ってきた結果を後で確かめる協業の形）。「丸投げ」は別に定義
- 見せる／見えていない（ask-claude-code）・tool_use／tool_result／tool runner・Monitor（道具）・「ゲートウェイ」の説明（rate-limits-and-errors）

### 道具・data の形

- command-cheatsheet：`command-table` の目印を新設（features にコマンド・一言・page・anchor を持たせる）。暫定は手書きの表。`/skills`・`/hooks`・`/mcp`・`/plugin` の一言は公式の表で未確認。旧名 `/review`・`/allowed-tools` の台帳の行
- choosing-automation：軸の表（動く場所・触れられるもの・課金の経路）を data の属性にできるか。claude-code-surfaces も同じ（属性：動く場所・読む設定）
- 自己リンクになる compare 表：claude-code-surfaces（Desktop アプリの Claude Code）・tool-use-loop・refactor-and-migrate（recipe に compare を置く是非。成熟度が全行共通で表から外れる）
- cloud-schedules の `#compare`、format-cheatsheet の規則の列：`fact-cell` のようなセル単位の目印
- github-actions-with-claude：雛形を載せる方針の確認（カード §10 と目次の食い違い）。`permissions` を read に絞った効果は未確認
- 台帳（outdated-advice）：AGENTS.md の回避策（CLAUDE.md に「読め」と書く・SessionStart フック）の行。`/review`・`/allowed-tools` の行
- dora.dev を sources.yml のドメイン一覧へ（paved-roads。生成で確認）
- choosing-a-plan：Team 行のセルの文言を「未確認」に直す（data の `usage-limit-types-by-plan`）。料金の facts（`plan-prices-individual`）を入れたら、#plan-table の fact-table の直後に目印を足す。Team の席ごとの上限を facts に足すか
- 数値の提案の取り込み（facts-proposal.yml・write.md の proposals）：message-threads-lifetime、scheduled-tasks 系 6 件（hourly-cap は要確認）、bare-mode 系 3 件（leak-fix-version は要確認）、edit/write-refuses-non-utf8-since、agents-md 系 3 件、prompt-caching 4 件、ai-in-contests-today 4 件、reasoning-extraction 2 件、rate-limits 2 件、artifacts-as-apps 2 件、progress-logs（Monitor の見張りの期限 3 件・hook-monitor-min-version を確認済みに）、tool-use-loop（tool_choice の既定・強制が使えないモデル）、refactor-and-migrate（/goal 構文の fact）、recover-lost-work（key-transcript-and-background を確認済みに。sessions の note に「圧縮の前のやり取りの残り方は未確認」）。取り込み後に各ページへ目印を置く
- 同期：agent-sdk-basics の settingSources の既定（省くと user・project・local をすべて読む）を提案の fact に。headless-basics#permissions の権限モードの記述が数値・版なしか、持ち主の側で確認

### 出典・確認が要る事実

- sources の足し先：pairing-and-delegating（実務家の整理の元の投稿。check_noai のうえで）・record-decisions（ADR の公式の説明）・grow-review-checklists（企業ブログの URL）・build-observation-tools（threadreaderapp・speakerdeck は未確認、noai の恐れ）・progress-logs-for-long-jobs（ログが大きすぎた例）・postmortems（collins-premortem の「30% は理由の数」を原典で。SRE Workbook は 1 回確認済み）・is-the-task-ai-suited（仮想の場面の差し替えは任意）・competition-day-operations（ISUCON13 初参加、DEF CON 33）・ai-in-contests-today（AWTF 2025・ICPC 2025・IOI 2025・MLE-bench 等は出典なし。AWTF 2026 Heuristic は二次の報道）・running-contest-experiments（recursive.cc の Halite III 事例は check_noai が timed out。再確認して通れば事例と出典を足す）・share-targets-and-bounds（Anthropic の記事 2026-01-21 を確認済み。材料表の「未確認」の印を外すか）
- disclosure-and-provenance：文部科学省の通知の本文は未確認（版は書いていない）
- stateless-messages-api：ZDR と HIPAA の対象外（research/22 #40）を公式の文書で再確認
- running-contest-experiments：式 (1.96 × s / d)² は筆者が導いたもの。別の担当が確かめる
- competition-day-operations：review の指摘 2 の文は、出典を足すか削る
- prompt-patterns：snippets/prompt-patterns/analysis-request.md が書けていない（Write が止められた）。メインが作って gen_site --page prompt-patterns で埋める。案は build-TR-R3.md に載せた
- make-slides：周辺製品とフロントエンドのデザインのページの公開後に「準備中」表示が変わる

## 数値の提案（第一波の終わりに data へ入れ、目印を置く）

| ページ | 提案 | 置く所（used_in） |
| --- | --- | --- |
| tokens | facts-proposal.yml の3件（倍率・約30%・3.5文字。3件目は要確認） | write.md のとおり |
| evidence-not-reports・claims-done-but-isnt | 直った版2件（検索の時間切れ v2.1.317・起動の失敗の終了コード v2.1.314。同じ値なので1つの id にまとめる） | evidence-not-reports#tool-output・claims-done-but-isnt#forms |
| hooks-basics | 4件（イベントの数・ハンドラの種類・Monitor の版・agent_id の版） | write.md のとおり |
| what-survives-compaction | facts-proposal.yml の4件 | reloaded のファイルの項・kept のフックの項 |
| knowledge-cutoff | model-knowledge-cutoffs（モデルごとの reliable／training の cutoff の表） | knowledge-cutoff#why（fact-table） |
| how-thinking-works・effort-levels | effort の既定の段の「モデル × 面」の表（effort-default-by-model-surface）と、版の fact 2件 | effort-levels#defaults-by-surface（表の直前に fact-table を置き段落を直す）・modelSettings／別モデルのサブエージェントの「新しい版」 |
| long-context-first | 公式の「最大30%向上」（facts-proposal.yml） | write.md のとおり |
| when-to-start-fresh | clear-after-failed-corrections | when-to-start-fresh#signals（「回数の目安は公式を見る」を目印に差し替え） |
| how-memory-works | プランごとの既定・過去チャットの検索の対象プラン（2件） | write.md のとおり |
| how-attachments-are-read | app-pdf-visual-pages・app-pdf-text-only-pages・app-upload-file-size-count（3件目は食い違いあり） | #pdf-and-others・#pitfalls |
| search-research-thinking | 呼び出しの回数と時間の目安（2件） | #comparison の「どれだけ広く調べるか」 |
| permission-modes-overview | 既定の開始モード2件（対話は auto・-p は Manual） | #defaults |
| checkpoints-and-rewind | checkpoint-retention-count（100）・checkpoint-retention-days（約30日） | #what-is-restored |
| connecting-mcp | MCP の出力の警告と上限（要確認。調査資料 01 G-1） | write.md のとおり |
| selection-pressure | fishtest-retry-cap（おおよそ4〜5回） | selection-pressure#retry-cap（本文の手書きを目印に差し替え） |
| what-auto-mode-stops | 連続3回／合計20回の上限（1件目）。誤検知率・見逃し率の fact 化（2件目。採るなら本文の手書きを替える） | write.md のとおり |
| sandboxing | default-reads・fail-if-unavailable の既定 | write.md のとおり |
| default-safety-settings | facts-default-safety-settings.yml の4件（起動モード・アプリの Auto／Manual・サンドボックス・incognito の保持）。一次資料は未確認 | #defaults-by-surface |
| where-your-data-goes | 保持期間5件（deleted-chat-backend-days・training-opt-in-retention-years・violation-retention・feedback-retention-years・local-transcript-cleanup-days） | #retention・#local-transcripts・#misconceptions |

where-to-put-instructions の `app-instruction-scope-and-timing`（値が「本文の表のとおり」）は、1つの値でないので入れない。アプリの機能に「読み込みの時期」の属性を足す案は、data の形の件として下に置く。

## 用語集に足す語（glossary を書くバッチで渡す）

- 能力の凸凹（jagged frontier）：over-reliance が本文で説明した。持ち主の分野は basics か delegate
- ハルシネーション：why-hallucinations が導入で定義した
- システムプロンプト：brief-a-new-colleague。prh は「system prompt」を誤りにする
- 非決定性（nondeterminism）：同じ依頼を出し直すと答えが変わる性質
- prompt injection：読ませた資料に紛れた文が Claude の行動を変えること（data-vs-instructions）
- reliable knowledge cutoff・training data cutoff（knowledge-cutoff が表で短く定義）
- ポストモーテム（事後報告）：suspected-degradation。用語集にあるか確認
- Topics（メモリの項目）・Pause・Reset：how-memory-works
- task・trial・grader・transcript・outcome・pass@k・pass^k：measure-changes
- 検証器・red/green・凍結：test-the-verifier。あるか確認
- 分類器（auto モードの）：what-auto-mode-stops
- auto モード：prh が auto mode を直す（promises-after-compaction）

## 道具・data の形

- six-causes の原因から症状のページを引く表：生成の目印 `causes` がある（hosts）。束に、そのページが持つ生成の目印が載っていなかった（PK3 で直す）
- 束の調査資料の抜き出しが、別の話題の節を写した（why-hallucinations の 6.2）。PK3 で見る
- アプリの機能に「読み込みの時期」の属性を足すと、where-to-put-instructions の手書きの表を compare に替えられる（data の features）
- compare の表で「未確認」「準備中」「自己リンク」が出る件：what-survives-compaction（compaction 自身の行）・where-instructions-sit（アプリ2機能の読み込みの時期・圧縮で残るかが null）・search-research-thinking（web 検索の行が自ページを指す）・how-attachments-are-read（機能名が自ページへのリンク）
- 強制力（enforcement）の属性が data にない：effort・mcp・checkpoints・auto-mode・app-memory・interactive-mode。要点の「強制力」を手書きにしたページがある（checkpoints・what-auto-mode-stops）。型の手引きの要求との扱いを決める
- 目次の sections に反映：where-your-data-goes に追加した2節（what-it-prevents・misconceptions）。default-safety-settings の節題「面ごとの既定（生成の表）」から「（生成の表）」を外す（anchor は変えない）
- 目次の checkpoints-and-rewind の「Bash での変更は戻らない」を「Bash だけが変えたファイルは戻らない」に直す（公式は、先に編集の道具で触ったファイルへの Bash の変更は戻ると書く）
- allow-i-dont-know の pitfalls（言葉の許可だけを頼りにする・やりすぎて答えられることまで断らせる）を front matter に足す案。値の形は schema 次第
- 雛形の safety: true の注記がレビュー依頼の雛形に合わない（independent-review）。features を外すと tracks の最新版が出る（verification-ladder）。safety・features の付け方の見直し
- term-index：漢字の群を頭文字の読みで分ける、または語頭の字ごとに区切る生成の改善。生成の中身は表ではなく見出し付きの箇条（束・カードは「表」と書く）
- knowledge-map：図のページ選択と2つの表示（分野・祖先と子孫）の JS の実装を確かめ、本文に合わせる。図が出ない環境向けの一文
- 型の目安の「比喩付きの図」を置かなかったページ（always-on-costs・protect-tests ほか）：比喩の一覧に reward-hacking の「採点表だけを渡された受験生」を足すか

- reverse-index：各ページの signs が公開ページに増えた後で、生成の表と節の導入の文が合うかをメインが見る
- sycophancy：Science の公刊版（Cheng ほか 2026-03-26）は doi.org が AI の利用を断るので資料にしない。本文は査読前の版（arxiv-2510-01395）の値（50%・N=1604）に合わせた（BF1）。science.org の論文のページを check_noai.py で確かめて使えるなら、公刊版の値に戻せる
- felt-vs-measured：Bastani（PNAS 2025）の出典を PNAS 本体（doi 10.1073/pnas.2422633122）に差し替えるか追加する案。pnas.org は取得が403で、数値（48%・17%）を TR2 は確かめられなかったので本文から数字を外した。書誌ページ（RePEc）のみが出典
- allow-i-dont-know：「偽の flag を大量に提出した」報告（調査11 p34#205）は出典が束にないため本文から削った。元の出典が見つかれば戻せる

## バッチ3の終わり（TR3）で足したもの

### 数値の提案（第一波の終わりに data へ入れ、目印を置く）

| ページ | 提案 | 置く所（used_in） |
| --- | --- | --- |
| destructive-commands | auto-mode-overeager-miss-rate（17%・n=52）。what-auto-mode-stops の手書きの値と同じ出典なので、1つにまとめる | destructive-commands#misconceptions |
| goal-until-done | 5件（goal-condition-max-chars・goal-idle-checkins-max・goal-auto-retry-max・goal-checkin-minutes・auto-continue-max） | write.md のとおり |
| textlint-hook | hook-on-failure-block-min-version（2.1.295） | textlint-hook#failure-and-few |
| doesnt-know-latest | current-models-reliable-knowledge-cutoff・current-models-training-data-cutoff。knowledge-cutoff の model-knowledge-cutoffs と1つにまとめる | doesnt-know-latest#diagnosis |
| skipped-later-pages | pdf-visual-page-limit・pdf-text-only-page-limit（how-attachments-are-read の app-pdf-* とまとめる） | skipped-later-pages#diagnosis |
| going-in-circles | best-practices-clear-after-failed-corrections（when-to-start-fresh と同じ id） | going-in-circles#choose |
| forgot-after-compaction・lethal-trifecta | 直った版 v2.1.317（evidence-not-reports の「直った版」と同じ id にまとめる）。lethal-trifecta は「クラウドの予定のタスクに頼んでいないコネクタが付いたときの警告」が入った版 | forgot-after-compaction#diagnosis・lethal-trifecta（tasks-and-schedules-in-the-app 側の扱いも検討） |
| how-usage-limits-work | facts-proposal.yml の usage-limit-types-by-plan・auto-continue-max-times・wrap-up-allowance-frequency・wrap-up-allowance-min-version。採るなら #limit-types に fact-table の組、#when-you-hit-the-limit に目印。採らないなら節題から「（プランごとの表）」を外す | write.md のとおり |
| keeps-stopping | auto-mode-no-verdict-display-fixed | keeps-stopping#diagnosis |
| align-japanese-output | （採るなら）確認日つきの挙動に付ける Claude Code の版 | #app ほか |

### 用語集に足す語

- tool poisoning・rug pull・slopsquatting（vetting-extensions が本文で短く定義）
- 表記の正本・漢字を開く（consistent-notation が本文で短く定義）
- OOF（学習に使わなかった分の予測）：misses-broken-evaluation
- 認知負債・技能形成：learning-with-ai。語になっているか確認
- 利用上限（別名：利用制限・使用制限）：how-usage-limits-work。項があるか確認
- reliable knowledge cutoff・training data cutoff の区別が knowledge-cutoff 側にあるか確認（doesnt-know-latest）

### 道具・data の形

- 雛形の「要る最低の版」の注記が、面を問わない依頼・prompt 種にも出る。`features: [mcp]`・`features: [auto-mode]` で消している回避をやめ、features を空にできる指定か、prompt 種では出さない既定にするか決める（vetting-extensions・forgets-in-long-chats・followed-injected-instructions・seems-less-capable）
- 強制力（enforcement）の属性：goal-until-done の要点の「強制力」の手書き（protect-tests・what-auto-mode-stops と同じ件）
- choosing-parallel-modes の表の Projects 行が自ページを指す。data の page を変えるか決める
- 目次の sections の同期：vetting-extensions（guards・checklist・after-install の3節を足した7節）・what-uses-up-limits（effects・misconceptions を足した5節）・plausible-falsehoods（forms・to-fixes・examples・prevent の4節）・stuck-in-a-check-loop と plausible-falsehoods の routes の節の分割・learning-with-ai の節題（「速さの得は確かめられず、理解は残りにくい」。anchor は同じ）
- fix-a-bug の「症状への表」は手書き。routes に入れるなら front matter の提案が要る
- 症状のページの診断の並びは schema/site.yml の prevents の並び（見えていない→散らかっている→確かめていない→縛っていない→合っていない→境界がない）で確かめた。バッチ3の症状のページはこれと矛盾しない（確認済み。何もしない）
- knowledge-map の JS の突き合わせは TR3 が済ませ、本文を3通りの見方に直した（済）

### 調べる担当に回すもの

- アプリ面の手段：protecting-secrets・destructive-commands・secrets-exposed・forgot-after-compaction・inconsistent-japanese-style・seems-less-capable・skipped-later-pages の「未確認」、API タブの「履歴は呼び出す側が持つ」の出典（saving-priorities）、hits-limits-quickly のアプリ・API の記述
- Claude Code の手段：vetting-extensions の「全部の一覧を作る」の具体（/mcp など）、plausible-falsehoods の Claude Code タブ、unexpected-memories の設定画面の項目名
- 事実の検証役：keeps-stopping 手順1の不具合の修正（CHANGELOG）・too-slow 診断6（サブエージェントの effort。CHANGELOG のみ）・consistent-notation の prh specs の挙動・repeating-the-same-explanation の雛形 control・protecting-secrets の sandbox.credentials.envVars・goal-until-done の --max-turns/--max-budget-usd・misses-broken-evaluation #forms の2件の原文（ANDPAD・Pebblous の研究）
- 持ち主のページとの突き合わせ（第一波の後）：rewrote-tests-to-pass（Edit の deny と子プロセスの書き込み）・refused-or-blocked（面ごとの停止の表示は when-requests-are-refused 側）・plausible-falsehoods の判断例2（fact-checking#best-of-n）・old-advice-doesnt-work（台帳の行ごとの節。ledger の節が指せるようになったら差し替え）・unexpected-memories（プロジェクト内でアカウント全体のメモリも併用される件は how-memory-works#scope で確定）・doesnt-know-latest の「確かな知識の日付」と学習データの日付の区別

### 出典の差し替え・調査資料の見直し

- ai-ideas-are-everyones：原論文（science.org）は check_noai が断るので出典にできない。10.7% は書かないまま
- stuck-in-a-check-loop：ISUCON13 の記事は「対処として知識や検索を与えた」と書かない。調査資料 11 の行の表現を見直す
- going-in-circles：研究段落を消したので sources は1件。研究の根拠は context-rot 側に置く
- learning-with-ai：競技の上位解法の読み方は kyopro-atlas を指す決めだが、URL・ページ名が束にない。決まったら summaries-of-solutions の末尾に1文

## バッチ4の終わり（TR4）で足したもの

### 数値の提案（各ページの facts-proposal.yml・write.md の proposals。第一波の終わりに入れ、used_in に目印）

| ページ | 提案 | 目印を置く所 |
| --- | --- | --- |
| choosing-a-surface | surface-attributes（3面を features に足し tracks に入れる。compare の表が3面を並べられる） | #compare-surfaces |
| current-models | current-models-lineup・haiku-4-5-removed-from-app-selector・sonnet-4-5-retirement・mythos-availability。入れたら #lineup の表の後に fact-table current-models-lineup、手書きの確認日 2026-10-29 を出典の行に替える | #lineup・#fable-and-mythos |
| thinking-keywords | ultrathink の版・引き上げる先・対象モデル | #ultrathink |
| after-switching-models | facts-proposal.yml の4件（/doctor prompt-audit の最低の版ほか）。退役の日付・既定の値・API の版 | #retirements-and-default-changes・#api-parameters |
| show-examples | few-shot-recommended-count（3〜5 個。一次資料の再確認は未） | #how-many |
| let-claude-ask | ask-user-question-limits・ask-user-question-timeout（Agent SDK 文書の id が sources にない） | #how・#limits |
| compact-and-auto-compact | idle compaction の大きさ・放置の時間・端末の版・IDE の版・autoCompactWindow の範囲 | 各 used_in の節 |
| using-projects | projects-free-limit（5。急がない） | #pitfalls |
| files-and-code-execution | facts-proposal.yml の3件（ネットワークの既定・30MB の上限・共有の制限） | fact-table |
| artifacts-overview | facts-proposal.yml の5件（成熟度・プラン・上限・2026-09-16 の日付）。書き出し先の形式の表（#templates）も移すか決める | #templates |
| connectors-in-the-app | custom-connector-free-limit・connectors-on-demand-recommend-threshold | #types・#on-demand |
| permission-modes-in-the-app | app-permission-mode-defaults（Ultra の扱いが束の data と調査資料 02 で食い違う。要確認） | #modes |
| usage-context-statusline | statusline-json-context-used-percentage・statusline-json-five-hour-used-percentage（未確認）。「5-hour limit」の呼び方を fact にするか | #statusline |
| when-to-add-what | add-trigger-claude-md-mistake-count（2回）・add-trigger-skill-paste-count（3回目）。公式の表の原文で再確認が要る | #triggers |
| must-know-operations | キー割り当て4件（Shift+Tab・Ctrl+G・Ctrl+O・Ctrl+B・画像の貼り付け）。入れたら手書きのバッククォートを目印に替え、実機で確かめる | 本文の該当箇所 |

### 用語集に足す語

- 強調語（IMPORTANT・YOU MUST・全部が大文字・「絶対に」「必ず」）：emphasis-words が本文で短く定義
- legacy artifacts：artifacts-overview が本文で短く定義
- 定期タスク（Scheduled tasks）・信頼境界（trusted boundary）：tasks-and-schedules-in-the-app
- ステータスライン（正）／status line（別名）：usage-context-statusline
- bypass permissions の平文表記：when-to-plan は `bypassPermissions` と書いた（prh が弾く）。平文の扱いを決める
- プラグイン（plugin の訳）：where-it-runs（prh が plugin を弾く）

### 道具・data の形

強制力の値の案（お願い・鍵・モデルの判定・なし。decisions 2026-11-05「強制力の語彙」。線引き：読んで従うよう頼むだけ＝お願い、止める仕組みがない＝なし）：

- ultrathink（thinking-keywords）：お願い（プロンプトに指示を足すだけで何も止めない）
- compaction（compact-and-auto-compact）：なし（止める仕組みではない）
- code-execution・ファイル作成（files-and-code-execution）：機能ごとに決める。ネットワーク設定の側は鍵、依頼の文はお願い。2機能を「鍵」とするか、ネットワークの設定を別の行に分けるか
- artifacts（artifacts-overview）：なし（止める仕組みではない）
- connectors（connectors-in-the-app）：鍵ではない。止められるのはツールごとの許可で締めた操作だけ。値を1つ選ぶなら「お願い」（許可の設定は別の機能の鍵）
- app-tasks（tasks-and-schedules-in-the-app）：1値に丸めにくい。権限モードとフォルダ許可は鍵、依頼はお願い。案は「鍵」（主の仕組みが許可）か、行を分ける
- subagents・plugins・code-intelligence・mcp の圧縮の扱い（extensions-at-a-glance の表で「未確認」「—」）：mcp はなし。subagents・plugins・code-intelligence は出典で決める。「1語で言えない」の値の表現を data に持てるかも検討

そのほか：

- choosing-a-surface：catalog の tracks に claude-code・api 側の機能の id を足す（compare の表が3面を並べられる。今は3軸の表を手書き）
- usage-context-statusline：compare 表の context-window の行が「— / —」（コストと since が data にない）。data に値を足すか、表から外す
- thinking-keywords：find-old-keywords の雛形に「要る最低の版」が出る（grep には不要）。features を外す案（上の「雛形の注記」の件と一緒に）
- thinking-keywords：台帳の行 think-hard-keywords への link `outdated-advice-ledger#think-hard-keywords` が持つ anchor にあるか、一覧で確かめる。emphasis-words の `#keep-going-dont-be-lazy`・`#important-caps` も同じ（公開側の解決を生成後に確かめる）
- let-claude-ask：雛形 `snippets/let-claude-ask/` と spec-first の担当の雛形の重複（置き場所は batch4-decisions）
- images-and-voice：音声入力の言語は language の設定。keep-replies-in-japanese の language-setting の節を指す link が束にない（related は足した。本文の link は節が指せるようになってから）
- current-models：自動の切り替え（分類器が止めた依頼を別のモデルで答え直す）から when-requests-are-refused への link を足してよいか（指せる節に追加するか）
- choosing-a-model・after-switching-models・emphasis-words：モデル名（Opus 5 など）を names の目印で出すか。names に項目を足す提案
- 台帳（outdated-advice-ledger）の行 id の節を、公開側で指せるようにする（ledger の sections に行 id の anchor を持たせる）

### 調べる担当に回すもの

- 事実の検証役：using-projects の「1プロジェクト1目的」の裏付け（企業の解説記事1件、根拠：弱）・when-to-plan の「diff を一文で説明できるなら省く」は経験則の明記のまま・connector-request 雛形の control（未検証）
- アプリ面の手段：show-examples（Projects の資料に置く面ごとの置き方）・images-and-voice（アプリの画像添付の手順）・compact-and-auto-compact（アプリの手で圧縮する操作）・tidy-the-desk（アプリの「任せる」）・handing-long-documents（Claude Code と API の PDF の読み込みの上限）
- images-and-voice：Windows・WSL の貼り付けのキーを公式から確かめて足すか
- 確かめ済み（TR4）：say-what-you-want の「フックが止めるときに返す文（exit 2 の stderr）は Claude に届く」は、公式 Hooks の文書（Exit code 2）で確認済み。本文はそのままでよい

## バッチ5の終わり（TR5）で足したもの

### 数値の提案（各ページの facts-proposal.yml・write.md の proposals。第一波の終わりに入れ、used_in に目印）

- path-scoped-rules：必要なときに読み込まれるファイルの文字数の上限（used_in: path-scoped-rules#limits。本文は数字なしで読める）
- how-skills-load：`skill-description-rebuild-min-version`（圧縮の後に説明文が作り直される挙動が入った版。足し先：how-skills-load#after-compaction の「説明文」の項目）
- mcp-or-cli：`mcp-output-warning-tokens`（10,000）・`mcp-output-default-limit-tokens`（25,000）。どちらも一次未確認（used_in: mcp-or-cli#table・#verify）
- pruning-extensions：facts-proposal.yml の 2 件（measure の「/plugin の Installed タブ」の項目。2 件目は任意）。目次の備考「40 個を超えたら見直す」の置き場所も（used_in: pruning-extensions#criteria）
- hook-recipes：agent_id が入力に付く最低の版（v2.1.69。deny-subagent-commit の min_version_fact に使う）
- parallel-with-worktrees：`worktree-base-ref-default`・`worktree-sandbox-resume-fix-version`・`worktree-block-writes-setting-version`（2.1.314。いずれも要確認）
- headless-basics：3 件（`#permissions` の既定の変遷と `--permission-prompts none` の版、`#output-and-exit-codes` の「直った版」）
- sdk-comparison：`managed-agents-session-hour-price`（#managed-agents の「費用の面では」）
- parallel-and-loop-costs：複数エージェントの倍率「約7倍」（条件つき。Manage costs の原文は未確認）。「約 15 倍」（2025 年の Research 機能）を目印にするなら提案を足す
- can-i-prompt-in-japanese：`multilingual-global-mmlu-japanese`（Global-MMLU の日本語の値。モデルごとの fact-table で持つ。置き場所 #evaluation。確かめ済み 2026-11-05）

### 用語集に足す語（glossary を書くバッチで渡す）

- description（スキルの説明文）：「スキルの SKILL.md のフロントマターにあり、Claude がそのスキルを読み込むかを決める手がかりになる文。名前とともに毎回の会話に載る」（skill-descriptions の提案。writing-skills・writing-subagents でも使う）
- Agent／Environment／Session／Events（Managed Agents の構成要素。sdk-comparison が本文で短く定義）
- データの区分（ai-usage-guidelines が本文で短く定義。強い提案ではない）

### 道具・data の形

- skill-vs-subagent：subagents に `survives_compaction`（記録は圧縮の影響を受けない）を入れると、表に「圧縮で残るか」の列を足せる。「強制力」の列も、subagents の強制力が空のため外している
- mcp-or-cli：CLI を data の機能に足すか（足さないと比較の表を作れない）。tracks に `skills` を足す案は batch5-decisions に上げた
- parallel-with-worktrees：features の worktrees に `enforcement: なし`（作業場所を分けるだけで、書き込みを禁じる鍵でもお願いでもない）。値の選び方はメイン
- headless-basics：headless に強制力の属性がない（permission-modes の値を指した）。属性の持たせ方
- feature-to-api-mapping：compare 表の MCP connector の行が自己リンクになる（data の `mcp-connector` の page がこのページ）。道具側で自己リンクを避けるか
- hook-recipes：`cc-docs-subagents` 相当の出典 id（disallowedTools は指定子を付けても Bash 全体が外れる、の根拠。data/sources.d/hook-recipes.yml への追加が要る）
- writing-subagents ほか：台帳の行 id の anchor が check_page で通ることは確認済み（アクションなし）

### 出典の差し替え

- checking-citations：Anthropic の訴訟の事例の出典が techcrunch.com（noai）。noai でない別の一次（裁判所の記録など）が見つかれば、事例を足す
- how-skills-load・path-scoped-rules：`@import` でコンテキストが減る、の説明は実践者の記事（Serverworks）による。公式の文書で確かめられたら（根拠：弱）の印を外す

### 調べる担当に回すもの

- hook-recipes：filter-test-output が `updatedInput` と `permissionDecision: allow` を一緒に返す。allow が必須か（公式の文書の全文で）
- writing-safe-hooks：`${CLAUDE_PROJECT_DIR}` を `args` の要素に書いたとき、置き換えが効くか（動作確認）
- request-lock-table：Stop フックで返答の言語を確かめる行が、keep-replies-in-japanese の扱いと揃うか
- explore-a-codebase：`#guards-first` の plan mode の一言（編集を止めたまま調べさせる）の正確さ
- before-opening-unknown-repos：起動後に動いているフックと MCP を見る画面やコマンドの名前（手順 4）を公式で確かめて足すか。`.vscode/` の動作
- entrusted-data：Claude Code の認証方式と契約の側の対応を、公式の文書で照合する（review の指摘 6）。ZDR の説明（sdk-comparison の指摘 1）も同じ
- parallel-with-worktrees：`.worktreeinclude` の雛形（safety: true）が safety の確認を通ったか
- parallel-and-loop-costs：`--max-turns`・`--max-budget-usd` が「確かに止める」仕組みか（原文で）
- research-and-reports：Claude Code の面の web 検索・取得の動作（未確認と書いた）
- ai-usage-guidelines：「止まって相談する」の一行がモデルの癖に依存する旨の確認日

### 本文の足し先（値が入ったあと）

- 台帳（outdated-advice-ledger）に path-scoped-rules の行（「CLAUDE.md は再注入される」の言い切り）を足すか。足せば #outdated は台帳を指せる
- hook-vs-skill：「ほかの OS と IDE 拡張は未確認」の位置は #table の末尾のまま（レビューも許容）

## 推奨R1（TR-R1、2026-11-05）

### 数値の提案（第一波の終わりに data へ）

| ページ | 提案 | 置く所 |
| --- | --- | --- |
| output-style-modes | output-style-concise-min-version（2.1.237）・output-style-command-min-version（2.1.269）・output-style-setting-case-sensitive（区別する）。write.md の proposals のとおり | #built-in・#switch |
| protected-paths | block-writes-outside-min-version（v2.1.314）。facts-proposal.yml | #outside-working-directory（タブの版の文を目印に替える。「提案済み」の文は採用後に消す） |
| split-models-by-role | opusplan の割り当て（plan は上位の系統、実行は日常の系統）。facts-proposal.yml | 承認後に本文の系統名を目印へ |
| model-quirks | モデルの系統名（Opus・Sonnet・Fable・Haiku）の fact-table 化または names への追加。facts-proposal.yml | #official-guidance の表 |
| using-auto-memory | ローカルのセッションでの既定の状態。facts-proposal.yml | #usage |
| why-prompt-caching | prompt-cache-default-ttl・prompt-cache-read-multiplier（write.md の proposals） | #what-happens・#why |
| long-chat-limits | 窓の大きさ。facts-proposal.yml | auto-management の fact の目印 |
| using-research | research-model（値は hc-research で確かめてから） | #when-to-use |
| cloud-sessions-and-teleport | 入れ子の `claude -p` の不具合が直った版（CHANGELOG v2.1.317） | #limits |
| large-context-window | 窓の大きさ・長い入力の単価・トークナイザーの差の fact の id | #費用の節（今は current-models への link） |
| lockbox-and-holdout | 「月 1 回程度」の確認の頻度を数値にするか（根拠：弱のまま数字なしでも可） | — |

### 強制力（enforcement）の値の案（お願い・鍵・モデルの判定・なし。decisions 2026-11-05「強制力の語彙」の線引き）

- research：お願い（調べる機能。条件は依頼に書くお願い）。using-research の要点は手書きの「お願い」
- settings：鍵（管理の層は鍵、個人の層はお願いが混ざる。主を鍵と見るか確認）
- cloud-sessions：なし（実行の場所であり、止める力を持たない）
- sessions（resume-and-branch）：なし（操作で、お願い・鍵のどちらでもない）
- subagents（what-subagents-dont-inherit）：なし（継承の仕様。tools・permissionMode の指定は鍵として別の機能で扱う）
- plugins：なし（束ねて配るだけ。write.md の feature_patch のとおり。足したら要点に `feature plugins/enforcement` を入れる）
- auto-management（long-chat-limits）：なし
- init（init-and-first-claude-md）：お願い（CLAUDE.md を作る機能）

### 用語集に足す語

- 縛る（規則を鍵に移すこと）・握る・回り込み・止めすぎ（lock-side-effects が本文で定義）
- critical paths（重要な場所への rm/rmdir の保護）・protected paths（protected-paths）
- 層（scope。settings-layers が「層」で統一）
- 上位の系統・日常の系統・軽い系統（split-models-by-role。current-models の表と言い方を揃える）
- ロックボックス・hold-out（lockbox-and-holdout）
- teleport（cloud-sessions-and-teleport）
- マーケットプレイス（plugins-and-marketplaces。ストアではなくカタログ）
- lint・推敲（less-ai-sounding-japanese。あるか未確認）

### 道具・data の形

- compare の表の「—」「未確認」：share-team-settings（settings・mcp の強制力 null）。上の enforcement の値が入れば解ける
- 「提案済み」の文が採用後に古くなる：protected-paths（上の版の fact を入れたら目印に替える）
- 出典（sources）の足し先：open-ended-loop-trap（頭打ちの実験・DrivenData・ISUCON の一次資料）・read-specs-yourself（arXiv 2種・競技者の記事＋ check_noai）・documents-in-japanese（support.claude.com の Upload files to Claude）・init-and-first-claude-md（redreamality・Tembo。実践者の幅）・ask-without-sycophancy（Truth Decay arxiv-2503-11656・Jin & Chen arxiv-2603-00539 の一次資料）
- diffs-humans-must-read：p56#61（AI 生成 PR の指摘が約 1.7 倍。販売元の分析）は出典を立てるなら利害を併記
- using-research：要点の「前提」の link が生成後に search-research-thinking の題名で出るかを確かめる。research-call-guide の目印の間の日付「（2026-10-29 時点）」が生成で消えるか
- 動作確認：freeze-eval-assets の雛形の `./eval` 形のパス（settings-reference の節を未確認）。外れたら `/` 始まりの絶対パスに
- 確認が要る事実（束の外）：stop-hooks の Stop フックと `/goal` の併用・resume-and-branch の「分岐が分けるのは会話でファイルではない」・approval-fatigue のサンドボックスの自動許可の記述・output-style-modes の Proactive・Concise の挙動・own-generated-code の Rust ガイドの規約
- 目次の備考・調査資料 11 の要約の直し：DrivenData の記事はモデルとハーネスを切り分けていない（harness-over-model は記事に合わせた）
- 注釈付きのセッション記録（目次の見せ方 DR-17）：lock-side-effects・stop-hooks・checking-unattended-runs で未作成。state/blocks.log などの材料をメインが渡すとき

## 推奨R2（TR-R2、2026-11-05）

### 数値の提案（第一波の終わりに data へ。各ページの write.md の proposals のとおり）

| ページ | 提案 | 置く所 |
| --- | --- | --- |
| safe-mode | safe-mode-enforcement（なし） | isolate-with-safe-mode#what-is-disabled |
| shared-artifacts-and-files | chat-sharing-plans・chat-sharing-invite-expiry（要確認）・chat-sharing-file-limit。features chat-sharing の since は未確認 | #who-can-see |
| claude-md-loading-order | claude-md-import-max-hops・claude-md-on-demand-size-limit（要確認） | #import・#limits |
| check-billing-path | api-credits-eligible-plans-and-amounts・api-key-env-p-mode-uses-key-without-confirmation・auth-precedence-order（本文の確認日の手書きを目印に替える） | #monthly-api-credits・#api-key-in-env・#how-the-path-is-chosen |
| what-feedback-sends | feedback-transcript-share-retention-months（6） | #what-is-sent |
| agent-view-and-background | agent-view-worktree-delete（任意。features の note でもよい） | #pitfalls |
| incognito-chats | incognito-retention-period を確認済みにする | — |
| before-using-top-model | top-model-by-plan・top-model-weekly-share・top-model-claude-code-min-version。正本の見直し：facts usage-limits の note と usage-limit-types-by-plan の最上位のモデルの別の週の上限の列（公式同士の食い違い。Fable の記事は別の週の上限なし）。how-usage-limits-work#limit-types の最後の箇条も | #which-limit 他 |
| browser-control | chrome-extension-requirements・computer-use-requirements（公式同士の食い違いのため両方の出典） | #claude-in-chrome・#computer-use |
| loop-and-scheduling | loop-recurring-expiry-days・loop-max-tasks-per-session・loop-min-interval・loop-self-paced-interval-range・desktop-scheduled-task-min-interval・cloud-scheduled-task-min-interval | #loop・#where-to-run |
| usage-credits-basics | usage-credits-expiry-japan | #how-it-works |
| dynamic-workflows | workflow-concurrent-agents・workflow-agent-caps・workflow-large-warning・workflow-size-guideline（facts-proposal.yml） | 各節 |
| checking-for-updates | stable の遅れの日数（facts-proposal.yml） | — |
| when-requests-are-refused | facts-proposal.yml のとおり（既定の有効・版・表示の文・分類の名前・課金・対象のモデル・検証の制度の段階） | write.md の used_in |
| instructing-reviewers | モデル別の傾向の数値ファイルがあれば目印で書き足す | — |

### 強制力（enforcement）の値の案（お願い・鍵・モデルの判定・なし。decisions 2026-11-05「強制力の語彙」の線引き）

- safe-mode：なし（読み込みを止めるだけ。write.md の proposal のとおり）
- insights・usage（insights-and-usage-review）：なし（見るだけ）
- feedback（what-feedback-sends）：なし（強制の仕組みではない）
- agent-view・cross-session-messaging（agent-view-and-background）：なし（見る・送る機能）
- projects（too-much-project-knowledge）：なし（ナレッジは使える状態にするだけ）
- incognito：なし（保持と管理者への見え方は止められないが、止める機能ではない。鍵に見える読み取りは Help Center 由来で未確認）
- browser-control の Chrome 拡張のサイト許可：鍵に近い／computer use のアプリごとの許可：鍵（要確認）
- usage-credits：なし（課金の仕組み）
- code-intelligence：なし（write.md の feature_patch のとおり。足したら冒頭を `feature code-intelligence/enforcement` の目印に）
- verify-skill（visual-checks）：お願い（cc-docs-skills で確かめてから。足したら括弧を外す）
- workflows（dynamic-workflows）：なし（何も強制しない）

### 用語集に足す語

- 写し（snapshot：共有した時点の内容の複製）・RAG（mode）・較正（calibrate）・判定役／採点役・ミューテーションスコア・変異・カバレッジ
- ローカルテスタ・ベンチマーカー・CV・referee（対戦の審判）・愚直解・本解・月次のふり返り（monthly recap。あれば合わせる）

### 道具・data の形

- 出典（sources）の足し先：evaluators-by-format（ISUCON14・Battlecode・CV 実験。check_noai のうえで）・ask-for-options（公式の裏付け）・when-requests-are-refused（Life Sciences Verification Program の記事）・instructing-reviewers（api-docs-prompting-opus-5 は束の写しのまま未取得）・check-the-metric（OpenAI の sycophancy の記事は 403 で未取得。題名と日付は仮、Kaggle ブログの 0.967/0.874 は未確認、CVPR の published は仮）・when-ai-is-unavailable（status 系の出典・2026-08-16 の障害の日付）
- browser-agent-cautions：束の材料 6.3 の The Register（noai）を claude-for-chrome-blog に差し替えた。反映時に同じ URL の重複がないか確認
- 調査資料の見直し：p34#61・p34#63（59.6〜68.1%・PBT-Bench 約 31%）は arXiv の要旨で確認できず、誤読の疑い。catalog/verify.yaml の notes に追記
- data の形：what-each-surface-cannot-do（アプリの面ごとの制約を持つ属性がなく、表が「アプリ」1 行になる）
- tracks の chat-sharing / features の since 未確認
- 確認が要る事実（束の外）：manual-only-skills の ask ルール `Bash(./scripts/deploy.sh *)` の書式（permission-rules と突き合わせ）・loop-and-scheduling の Desktop の説明（新しいセッション・手元のファイル）・unfaithful-reasoning の平方根の例と表のモデル（tracing-thoughts と突き合わせ）・looks-are-not-quality の Anthropic ブログ URL（/research/ と /engineering/）・check-billing-path の ANTHROPIC_AUTH_TOKEN と apiKeyHelper の課金先・move-judgment-into-scripts の 1 件の研究・harness 系の「調査資料が拾った研究」の名・年
- data-analysis：A-8 の雛形 `snippets/data-analysis/observe-and-hypothesize` が正本。prompt-patterns の担当に同じ id を gen の目印で取り込むよう伝える
- 雛形：when-ai-is-unavailable の expect.yaml（features を空にして「要る最低の版」の表示を消すか）
- 図：claude-md-loading-order の木は文字の code ブロック（static の図が要るなら別の担当）。pitfalls・unfaithful-reasoning・looks-are-not-quality・move-judgment-into-scripts・build-test-harness は図なし（表や雛形で代えた）
