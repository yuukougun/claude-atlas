# 工程4 目次の直し：F6（safety・delegate・team）

- 担当：F6
- 日付：2026-11-04
- 受け持ち：`planning/catalog/safety.yaml`・`delegate.yaml`・`team.yaml`
- 指示：[brief-fix.md](brief-fix.md)、design-review の DR-19（と、関わる DR-02・DR-18）、[fix-aliases.md](fix-aliases.md)（途中で更新された版も読み直した）
- 途中でメインから受けた F4 の提案（checking-ai-rules へのサインと図）も扱った（§1 の r）

## 1. DR-19 の行ごとの扱い

| 記号 | 変えたページ | 中身 | しなかったときの理由 |
| --- | --- | --- | --- |
| a | safety：approval-fatigue・where-your-data-goes・instructions-hidden-in-materials・protecting-secrets・when-requests-are-refused・where-bypass-is-ok／delegate：open-ended-loop-trap・humans-set-the-parallel-limit・goal-until-done・headless-basics・github-actions-with-claude・cloud-schedules・automated-pr-review／team：review-bottlenecks・rolling-out-to-teams | 症状のページの困りごとの言い換えを外すか、やりたいこと・狭い場面に書き換えた。R1-06 の束は同じ文にそろえるか、場面を書き分けた（§2） | 同じ文の束5つ（§2 の終わり）は、00 §4 の項目をわざと1行にまとめたものなので変えない（DR-15） |
| d | prompt-injection-in-practice・vetting-extensions・share-team-settings・org-managed-settings-and-mcp・loop-and-scheduling・review-bottlenecks（curb-sycophancy-and-overtrust はまとめたので消えた） | fix-aliases の「外す側」の別名を外した（§3） | dynamic-workflows の /deep-research は、別の機能の公式の名前なので残した（§3） |
| e | protecting-secrets・what-not-to-delegate・humans-set-the-parallel-limit・parallel-with-worktrees・choosing-parallel-modes・open-ended-loop-trap・goal-until-done・headless-basics | 推移的な前提6件の警告を消し、R3 の付表B の4本を related に移した（§4）。付表B の4本目は、前提として要らないと判断して移した | five-questions-before-delegating と dynamic-workflows の警告は、付表B の辺を移したことで消えたので、そのページの前提は変えていない |
| f | team の14ページすべて（level 9 ページを付け直し、5 ページは level をそのままに level_evidence を書き直した）。ai-usage-guidelines を必須に上げた | 「定義の言い直し」だった level_evidence を、チームでそのページが最初に要る場面に書き直した。「チームで導入する」の受け皿を ai-usage-guidelines（必須）にした（§5） | — |
| h | where-bypass-is-ok（R1-14）・checking-ai-rules（R1-16） | R1-14：別名 devcontainer・Docker・コンテナと、サイン「コンテナの中で Claude Code を無人で動かしたい」を足した。R1-16：サイン「AI が書いたコードを、製品や OSS に入れてよいか確かめたい」、別名「生成物のライセンス」、節 rights-and-licenses（解釈は書かず、確かめる先だけ）を足した | R1-16 を disclosure-and-provenance でなく checking-ai-rules に置いた：「確かめる先」を持つ必須のページだから。disclosure-and-provenance は checking-ai-rules を前提にしているので、related では指せない |
| m | protecting-secrets・when-requests-are-refused | protecting-secrets から節「貼ってしまったとき」（if-leaked）とサイン「会話に API キーを貼ってしまった」を外し、related の先頭で secrets-exposed#first-response を指した。when-requests-are-refused の節 by-surface を「面ごとの表示と仕組み」にし、表示の文の持ち主をここにした | if-leaked を指すページはなかった。症状のページの側の直し（サインの移し先と by-surface の短縮）は F7 の受け持ちなので、open_issues とメインへ（§6）に書いた |
| o | cloud-schedules・enterprise-vs-team-plans | 題名を「クラウドの定期タスク」と「組織で使うプランの選び方」にし、旧名とプラン名は aliases に置いた（旧題「Team と Enterprise の違い」も aliases に）。旧名の事実は数値ファイルの名称の表を正にし、台帳の routines-name は残す（DR-18） | — |
| p | ai-amplifies-organizations → paved-roads | 節 amplifier にまとめ、旧題と別名、サイン2つを paved-roads に移した（§5） | review-bottlenecks でなく paved-roads にした：判断が比例則の組織版（広げる前に土台を強め、危険の小さい作業から広げる）で、安全な道を作るこのページと同じ向きだから |
| q | curb-sycophancy-and-overtrust → separate-roles | 独自の判断を1行で書けなかったので、節 against-sycophancy にまとめた（§5） | — |
| r（F4 の提案） | checking-ai-rules | competition-rules から外れたサイン「規約に AI のことが書かれていない大会に出る」を、大会に限らない状況のサイン「大会や学校、会社の規則に、AI のことが書かれていない」にして置いた（答えは節 when-unclear）。三つの型の理由（11 第1節 p12#23。根拠は強、訂正・注記なし）を、節 why-rules-differ の図の案（visual）にした | 図は大会の例を根拠にし、授業と仕事への当てはめは類推と書く旨を visual に添えた |
| s | org-managed-settings-and-mcp | 題名から「（管理設定）」を外して「組織に設定と MCP サーバーを配る」にし、nav_title を外した。summary を「配る経路・グループごとの設定・許す MCP サーバー」に絞り、優先して効く説明を外した。サイン「部署ごとに違う設定を配りたい」を足し、materials の bypass を止める設定（enforce の持ち分）を外した | — |
| i（関わり） | where-your-data-goes | related の memory-faq（F2 が how-memory-works にまとめた）を unexpected-memories に替え、notes を直した | — |
| DR-02（関わり） | approval-fatigue・prompt-injection-in-practice・protecting-secrets・when-requests-are-refused・humans-set-the-parallel-limit | notes の「症状のページがこのページを前提にする」を外した（routes に移るため） | routes そのものは F7 の受け持ち |

## 2. 言い換えの重なり（a）で直した sign（前 → 後）

症状のページの困りごとと重なっていたもの：

| ページ | 前 | 後 | 重なっていた症状のページ |
| --- | --- | --- | --- |
| approval-fatigue | symptom「確認が多すぎて、席を外すと作業が止まっている」 | goal「確認を減らしても、残した確認は中身を読んで判断したい」 | wrong-amount-of-approvals（R1-04） |
| where-your-data-goes | symptom「会話を消したのに、まだどこかに残っていないか不安」 | goal「消した会話が、提供元にいつまで残るか知りたい」 | unexpected-memories |
| instructions-hidden-in-materials | symptom「資料を読ませたら、頼んでいない指示に従った答えが返ってきた」 | symptom「課題の資料や問題文を読ませたら、頼んでいない指示に従った答えが返ってきた」（狭い場面） | followed-injected-instructions |
| protecting-secrets | symptom「会話に API キーを貼ってしまった」 | 外した（初動は secrets-exposed へ。m） | secrets-exposed |
| when-requests-are-refused | symptom「同じセッションで言い直しても、止められ続ける」 | 外した | refused-or-blocked |
| open-ended-loop-trap | symptom「長く回したのに、手元のスコアだけ上がって本番では良くならない」 | situation「方針や手法の改善まで、AI に自動で回させている」 | misses-broken-evaluation（R3 の付表A の5・R1-07） |
| open-ended-loop-trap | symptom「回し続けても、途中から結果が伸びない」 | goal「AI に回させる反復を、どこまでに限るか決めたい」 | stuck-in-a-check-loop |
| humans-set-the-parallel-limit | symptom「並べたセッションの結果を確かめきれない」 | situation「マシンや予算に余裕があるので、並べる本数を増やそうとしている」 | parallel-fatigue |
| review-bottlenecks | symptom「AI で PR が増えて、レビューが追いつかない」 | goal「AI で増えた PR を、チームでレビューできる量に合わせて流したい」 | parallel-fatigue（R1-04） |
| review-bottlenecks | symptom「AI の作業を見守るだけで疲れる」 | 外した（狭い場面の「マネージャーのところで PR が止まる」は残した） | parallel-fatigue |
| automated-pr-review | situation「人のレビューが追いつかず、AI のレビューで済ませたくなっている」 | situation「人のレビューの代わりに、AI のレビューで済ませたくなっている」 | parallel-fatigue |

対処のページどうしの近い文（R1-06・R3-5）：

| ページ | 前 | 後 | 扱い |
| --- | --- | --- | --- |
| where-bypass-is-ok | situation「夜間や CI で、人が見ていない間に Claude を動かす」 | 「夜間や CI で、人が見ていない間に Claude を動かしている」 | verify の checking-unattended-runs と同じ文にそろえた（どこで動かすか／どう確かめるかの二つの答えを1行に束ねる） |
| goal-until-done | goal「テストが通るまで止まらずに続けてほしい」 | 「テストが通るまで終わらせたくない」 | verification-ladder・stop-hooks と同じ文（00 §4 の項目）にそろえた |
| headless-basics | symptom「サブスクリプションのつもりが、スクリプトの実行に API の料金がかかった」 | 「サブスクリプションで使っているつもりが、API の請求が来た」 | cost の check-billing-path と同じ文にそろえた |
| github-actions-with-claude | goal「CI の中で Claude Code を動かしたい」 | 「スクリプトや CI から Claude Code を使いたい」 | headless-basics と同じ文にそろえた（00 §4 はこの項目の行き先を両方に並べていた） |
| cloud-schedules | goal「PC を閉じていても、決まった時刻に作業を走らせたい」 | 「決まった時刻の作業を、手元の PC なしで走らせたい」 | where-it-runs・cloud-sessions-and-teleport の「PC を閉じても…」と場面を書き分けた（R3-5） |
| rolling-out-to-teams | situation「チームに Claude Code を導入する」 | 「チームで Claude を導入する」 | 必須にした ai-usage-guidelines と同じ文にそろえた（f） |

変えなかった同じ文の束（00 §4 の項目をわざと1行にまとめたもの）：「席を外している間も進めてほしい」（five-questions-before-delegating・goal-until-done・app の tasks-and-schedules-in-the-app）、「毎朝決まった調査をさせたい」（loop-and-scheduling・tasks-and-schedules-in-the-app）、「記録を残さずに相談したい」（where-your-data-goes・incognito-chats）、「チームで同じ設定を使いたい」（share-team-settings・plugins-and-marketplaces）、「Web ページやメールを読ませるのが不安」（prompt-injection-in-practice・lethal-trifecta）。

まとめや h で足した sign：where-bypass-is-ok「コンテナの中で Claude Code を無人で動かしたい」、checking-ai-rules「AI が書いたコードを、製品や OSS に入れてよいか確かめたい」「大会や学校、会社の規則に、AI のことが書かれていない」、ai-usage-guidelines「チームで Claude を導入する」、paved-roads「組織全体に AI を広げる前に、何を整えるか考える」「AI を入れて速くなったのに、障害や手戻りが増えた」（ai-amplifies-organizations から）、separate-roles「チームの議論で「AI も賛成した」が決め手になっている」（curb から。チームの場面に絞った）、risk-tiered-approval「AI のレビューが通った PR を、人がよく見ずに承認している」（curb から）、org-managed-settings-and-mcp「部署ごとに違う設定を配りたい」。

## 3. 別名の重なり（d）

外した別名：

| ページ | 外した別名 | 主のページ |
| --- | --- | --- |
| prompt-injection-in-practice | prompt injection・間接プロンプトインジェクション | basics の data-vs-instructions（このページは題名の「プロンプトインジェクション」で引ける） |
| vetting-extensions | tool poisoning | prompt-injection-in-practice |
| share-team-settings | settings.local.json・.mcp.json | cli の settings-layers・extend の connecting-mcp |
| org-managed-settings-and-mcp | managed settings・managed-settings.json・server-managed settings | enforce の managed-settings-enforcement（管理コンソールから配る経路は節 delivery にあり、enforce から #delivery で指される） |
| loop-and-scheduling | scheduled tasks → Desktop scheduled tasks に替えた | app の tasks-and-schedules-in-the-app。Claude Code の側は公式の名前の Desktop scheduled tasks（research/01 O-2）で引けるようにした |
| curb-sycophancy-and-overtrust | 自動化バイアス | judgment の over-reliance（ページをまとめたので引き継がなかった） |
| review-bottlenecks | レビューが追いつかない（表にはない） | 症状のページ parallel-fatigue の題名の困りごとと重なるため外し、review bottleneck を足した |

残した別名：dynamic-workflows の /deep-research。app の using-research（アプリの Research）と同じ文字列だが、Claude Code では同梱のワークフローの名前（research/01 E-5）で、別の機能である。外すと Claude Code の側を名前で引けない（fix-aliases の例外）。

このページを主にした別名（相手の側が外す）：approval-fatigue の「承認疲れ」、prompt-injection-in-practice の「tool poisoning」、destructive-commands の「破壊的な操作」、when-requests-are-refused の「拒否された」「分類器に止められた」。後の二つは §6 を見てほしい。

足した別名：where-bypass-is-ok（devcontainer・Docker・コンテナ）、checking-ai-rules（生成物のライセンス）、paved-roads（AI は組織の強みも機能不全も増幅する・増幅器としての AI・DORA）、separate-roles（チームで迎合と過信を防ぐ）、risk-tiered-approval（AI のお墨付き）、enterprise-vs-team-plans（Team と Enterprise の違い）、org-managed-settings-and-mcp（設定の配布）。どれもほかのページの別名・題名と重ならないことを確かめた。

## 4. 外した前提（e）

| ページ | 外した前提 | 理由 | 移した先 |
| --- | --- | --- | --- |
| safety/protecting-secrets | permission-rules | sandboxing から推移的に届く | related の2番目 |
| delegate/what-not-to-delegate | verifier-defines-problem | 付表B の4。分ける軸（機械的に確かめられるか）は節 verifiable-axis で前提なしに読め、検証器が問題を定義することは理由の深掘りに当たる | related の先頭（比例則の守りも兼ねる） |
| delegate/humans-set-the-parallel-limit | five-questions-before-delegating | 付表B の1 | related（前提はなくなった。守りは independent-review などの related で持つ） |
| delegate/parallel-with-worktrees | humans-set-the-parallel-limit | 付表B の2 | related |
| delegate/choosing-parallel-modes | humans-set-the-parallel-limit | 付表B の3（dynamic-workflows の警告もこれで消えた） | related の先頭 |
| delegate/open-ended-loop-trap | verifier-defines-problem | selection-pressure から推移的に届く | related の先頭 |
| delegate/goal-until-done | evidence-not-reports | five-questions-before-delegating → verification-ladder から推移的に届く | related の先頭 |
| delegate/headless-basics | permission-rules | five-questions-before-delegating から推移的に届く | related の先頭 |
| team/review-bottlenecks | humans-set-the-parallel-limit | 推移的な前提ではないが、f のため（一人の並列の本数の判断を知らなくても、チームのレビューの詰まりは読める。R1-10 の判断どうしの前提） | related の先頭 |

結果（いまの目次全体。ほかの担当の直しを含む）：前提の深さの最大は 9 → 8、深さ7以上のページは 25 → 9（R3 の試算と同じ）。受け持ちで最も深いのは compare-hypotheses-in-parallel の 9段・祖先22 → 7段・祖先17。残る鎖は verification-ladder → evidence-not-reports → define-done → agent-loop を通り、R3 が本当の前提とした部分なので変えていない。第一波は 125 のまま（外した前提はどれも、ほかの道で第一波に残る）。

## 5. まとめたページ・新しいページ・priority と level

**まとめたページ**（team.yaml の merged）：

- ai-amplifies-organizations → paved-roads（節 amplifier）：研究の紹介が本体で独自の判断がなかった（R3-16）。判断は比例則の組織版で、paved-roads と同じ向き。paved-roads の summary に「土台の強さも弱さも増幅するので、テストとレビューを見直し」を入れた。調査は相関で因果は書かない
- curb-sycophancy-and-overtrust → separate-roles（節 against-sycophancy）：独自の判断を1行で書けなかった（R3-17）。原則は agreement-is-not-evidence、AI の承認を数えないことは risk-tiered-approval（持ち主にした）、独立の案出しは ideate-independently が持ち、残る「疑う役と人どうしの批評で迎合に備える」は separate-roles の疑う人の役割そのものだった。separate-roles の surfaces に app を、pitfalls に預けすぎるを足した

**新しいページ**：なし。**新しい節**：checking-ai-rules#rights-and-licenses、paved-roads#amplifier、separate-roles#against-sycophancy。**外した節**：protecting-secrets#if-leaked（m。参照なし）。

**priority**：ai-usage-guidelines を推奨 → 必須（f・R1-11）。design §1.2 の「チームで導入する」の初版の受け皿。前提（checking-ai-rules・where-your-data-goes・request-vs-lock）はどれも必須。章「導入と決まり」の先頭に移した。team の必須は 1 → 2（review-bottlenecks と ai-usage-guidelines）。

**level**（team。R3-7。チームでそのページが最初に要る場面で付け、前提より下にはしない）：

| ページ | 前 → 後 | 最初に要る場面 |
| --- | --- | --- |
| enterprise-vs-team-plans | 仕組みにする → 使う | 使い始める前の契約 |
| ai-usage-guidelines | 仕組みにする → 整える | チームで使い始めて決まりを整えるとき（前提の request-vs-lock が整える） |
| paved-roads | 仕組みにする → 整える | 禁じるか安全な道を用意するかを最初に決めるとき |
| ideate-independently | 仕組みにする → 整える | チームの案出しに AI を使い始めたとき（比例則の警告も正当に消えた） |
| review-bottlenecks | 仕組みにする → 任せる | AI が書いた PR が増えて詰まり始めるとき |
| risk-tiered-approval | 仕組みにする → 任せる | AI の変更とレビューが承認の流れに入るとき |
| separate-roles | 仕組みにする → 任せる | 実装を任せ、評価・撤退を誰が決めるかを分けるとき |
| record-decisions | 仕組みにする → 任せる | 決めたことと AI に任せたことを書面に残すとき |
| via-cloud-providers | 仕組みにする → 任せる | クラウドの契約の中で使い始めるとき（前提の check-billing-path が任せる） |
| share-team-settings・rolling-out-to-teams・grow-review-checklists・org-managed-settings-and-mcp・audit-logs-and-telemetry | 仕組みにするのまま | 設定を配る・広める・常設の指示を育てる・記録を見る場面で、前提も仕組みにする。level_evidence を書き直した |

team の内訳は、使う 1・整える 3・任せる 5・仕組みにする 5（14ページ）。任せるのページはどれも verify・safety・enforce のページを前提か related に持つ（比例則の警告なし）。

## 6. メインへ

1. **まとめたページを指すほかの分野の参照**：いまエラーは1件だけ（symptoms の caves-when-pushed の related の curb-sycophancy-and-overtrust）。start の four-principles、basics の sycophancy、judgment の3ページは、持ち主がすでに paved-roads#amplifier・separate-roles#against-sycophancy に直していた。この二つの anchor は、もう他の分野から指されている
2. **F7（symptoms）へ**：(1) secrets-exposed の signs に「会話に API キーを貼ってしまった」を足し、節 first-response で、貼った鍵も無効化から始めることと、手元の記録に平文で残ることを持ってほしい。(2) refused-or-blocked の節 by-surface は外すか1行にして when-requests-are-refused#by-surface を指してほしい（safety.yaml の open_issues にも書いた）
3. **fix-aliases の更新との食い違い**：更新後の規則「困りごとの言い方は症状のページを主にする」に照らすと、「拒否された」「分類器に止められた」は refused-or-blocked（t で auto モードやフックの場合にも振り分ける）を主にするほうが合う。ただ表は when-requests-are-refused を主のままにしているので、両方から消えないよう表のとおり残した。「分類器に止められた」で着いた auto モードの読者のために related に what-auto-mode-stops#when-blocked を足した。主を替えるなら、when-requests-are-refused から外すよう知らせてほしい
4. **同じ文にそろえたサインは、相手のページの文が変わると束がほどける**：checking-unattended-runs（F5）、verification-ladder・stop-hooks（F5）、check-billing-path（F2）、tasks-and-schedules-in-the-app（F2）。直しの後に照らしてほしい
5. **F5 へ**：(1) R1-14 の別名 devcontainer・Docker・コンテナは where-bypass-is-ok に置いたので、sandboxing に同じ別名を足すと新しい重なりになる。(2) R3-17 で「AI の承認を人の承認に数えない」の持ち主を risk-tiered-approval にした。verify の independent-review の節 ai-approval は1行にしてここを指すとよい
6. **F4 へ**：extend の choosing-mcp-servers の「便利そうな MCP サーバーを見つけた」は、vetting-extensions の「便利そうな MCP やプラグインを見つけた」（00 §4 の項目そのもの）の言い換え。同じ文にするか場面を書き分けるとよい
7. **判断を確かめてほしい点**：(1) review-bottlenecks の前提から humans-set-the-parallel-limit を外した（推移的な前提ではなく、f で任せるにするため）。(2) 付表B の4本目（what-not-to-delegate → verifier-defines-problem）は前提として要らないと判断して移した。(3) team の level を下げたので、ロードマップの使う〜任せるの列に team のページが並ぶ。R3-7 の別案（組織のページは level を持たない）を採るなら設計の変更になる
8. **変えていないが気づいた点**：enterprise-vs-team-plans の id にもプラン名が入る（id は変えていない。DR-19 n のような改名はメインの判断）。DR-07 の「この環境で試せない雛形」が受け持ちに4つある（where-bypass-is-ok の使い捨てのコンテナ、org-managed-settings-and-mcp の管理設定、github-actions-with-claude、bare-mode の --bare）。templates は変えていない
9. DR-17 の「見せ方」は、メインが題材の一覧を作るので、notes には足していない

## 7. 検査の結果

- `python3 tools/check_catalog.py --field safety`・`--field delegate`・`--field team`：どれもエラー 0 件、警告 0 件（推移的な前提の警告 6 件と、比例則の警告 1 件〔ideate-independently〕が消えた）
- 全体（`python3 tools/check_catalog.py`、ほかの担当の途中の直しを含む）：エラー 5 件（参照 5。うち受け持ちのまとめに関わるのは §6 の1の1件）、警告 26 件（受け持ちの分野には0件）
- summary はどれも120字以内・2文。受け持ちのサインと、症状のページの同じ文の重なりは0（逆引きの重複の警告なし）

## 8. 確かめていないこと

- 一次資料（Web）では確かめていない。Desktop scheduled tasks の名前、Claude Code の /deep-research が同梱のワークフローであることは research/01 によった。R1-16 の「確かめる先」（利用規約・組織の規則・入れる先のプロジェクトの規則）は、事実を書かず、確かめる先を示すだけにした
- 言い換えは2字の重なりと difflib の比で上位を見て、目で選んだ。比の低い言い換えは見落としがありうる
- ほかの担当が同時に直しているので、全体の数（エラー・第一波・必須）は検査した時点のもの。束にした相手の文が後で変わったかは追っていない
- 逆引きと用語索引は生成していないので、束ねた行が1行に出ることは確かめていない
