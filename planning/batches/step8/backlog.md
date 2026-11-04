# 工程8：後でまとめて扱うもの

[rules.md](rules.md) の「後でまとめて扱うもの」。バッチの終わりに足していく。

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
