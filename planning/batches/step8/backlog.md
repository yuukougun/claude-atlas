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
