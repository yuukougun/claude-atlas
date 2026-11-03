# 工程3 I7：symptoms・recipes の目次の統合の報告

- 担当：I7（2026-11-04）
- 指示：[brief-integrate.md](brief-integrate.md)。材料：`state/step3-integrate/I7-input.md`（A の open_issues 55件、B の逆引きの行 1行）
- 書いたもの：[planning/catalog/symptoms.yaml](../../catalog/symptoms.yaml)・[recipes.yaml](../../catalog/recipes.yaml)
- 変えたページ：symptoms 20ページ（not-what-i-meant・does-more-than-asked・keeps-stopping・refused-or-blocked・uses-nonexistent-apis・forgets-in-long-chats・going-in-circles・forgot-after-compaction・instructions-ignored・repeating-the-same-explanation・replies-in-english・inconsistent-japanese-style・claims-done-but-isnt・rewrote-tests-to-pass・misses-broken-evaluation・stuck-in-a-check-loop・wont-rethink-approach・blames-the-tools・deleted-something-important・wrong-amount-of-approvals）、recipes 5ページ（explore-a-codebase・fix-a-bug・spec-first・data-analysis・office-paperwork）。どれも notes の末尾に「（2026-11-04 統合：番号）」を付けた
- 変えていないもの：ページの数（symptoms 33・recipes 21）、ページの id と sections の anchor、title、priority、level、wave（M10）、merged・dropped。open_issues は、番号（symptoms#n・recipes#n）がずれないよう2段目の文のまま残した

## 1. 材料 A の扱い

「取り込み済み」は、2026-11-04 の作業の終わりの時点のファイルで確かめた。ほかの分野への提案（対象外）も、相手のファイルの状態を書いた。

| 番号 | 扱い | 変えたページと、反映しないときの理由 |
| --- | --- | --- |
| start#2 | 取り込み済みを確かめた | symptoms の33ページすべてが related に six-causes を持つ（six-causes は guide で level がない）。変更なし |
| start#8 | 対象外 | M10（wave は変えない）。symptoms の全ページの wave: 1 はそのまま |
| basics#2 | 取り込み済みを確かめた | forgot-after-compaction は what-survives-compaction と promises-after-compaction を前提に持つ。残るものの一覧を繰り返さない点は notes の既存の記述どおり。when-to-lock#spoken-rules-fade への related は enforce#2 で入れた |
| basics#5 | 一部を確かめ、一部は反映しない | caves-when-pushed は sycophancy を前提に持つ（取り込み済み）。rewrote-tests-to-pass には reward-hacking を前提として足さず related のままにした：前提の verifier-three-conditions が reward-hacking を前提にしていて推移的に届く（catalog/README §4.4 の1。contest の担当と同じ扱い）。理由を notes に書いた |
| basics#6 | 一部を確かめ、一部は反映しない | instructions-ignored は where-instructions-sit と request-vs-lock を前提に持つ（取り込み済み）。forgets-in-long-chats には context-rot を前提として足さなかった：前提の when-to-start-fresh が context-rot を前提にしていて推移的に届く。related の先頭のまま。level_evidence（「整える」と書いていた）と notes を直した |
| surfaces#4 | 取り込み済みを確かめた | make-slides・office-paperwork は peripheral-products#office-add-ins を related に持つ |
| models#4 | 取り込み済みを確かめた | seems-less-capable → suspected-degradation（前提）、keeps-stopping → effort-levels（前提）・model-quirks、does-more-than-asked → effort-levels・model-quirks |
| prompting#1 | 反映した | refused-or-blocked は when-requests-are-refused を前提に持つ（related より強い。前提と関連に重ねない）。M5 に合わせて summary・related（choosing-a-model を外した）・tracks（model-selection を外した）・materials・notes を直した（補足を参照）。自動の切り替えの設定は新しい id を足さず、既存の refusals で追う（メインへ 3） |
| prompting#7 | 取り込み済みを確かめた | spec-first は let-claude-ask を前提に、write-docs は requesting-prose を related に持つ |
| context#1 | 取り込み済みを確かめた | symptoms・recipes に、まとめた候補（managing-context-in-the-app・compaction-settings・breaks-and-cache-expiry・sessions-as-branches）への参照はない（検査の参照のエラー 0） |
| context#2 | 反映した | forgets-in-long-chats の related に rewind-dont-correct を、going-in-circles の related に handoff-documents を足した（どちらも段が上なので related）。forgot-after-compaction の related の compact-and-auto-compact を compact-and-auto-compact#idle-compaction にした。ほかの組（when-to-start-fresh・promises-after-compaction など）は入っていた |
| app#6 | 対象外 | app の判断（工程4）。unexpected-memories は how-memory-works を前提に、memory-faq を related に持つ。まとめるなら、まとめた先に直す |
| cli#1 | 取り込み済みを確かめた | office-paperwork の signs（00 §4 のサイン）・節 work-folder・前提 default-safety-settings。サインの種類は B の 72 で直した |
| cli#2 | 取り込み済みを確かめた | instructions-ignored・seems-less-capable・replies-in-english・blames-the-tools は isolate-with-safe-mode を、wrong-amount-of-approvals は permission-modes-overview を、deleted-something-important は checkpoints-and-rewind・recover-lost-work を指す |
| extend#9 | 反映した | instructions-ignored の related に hook-vs-skill を足した（上限の20件に収めるため block-with-exit-2 を外した。hooks-basics と hook-recipes から届く）。forgot-after-compaction の related に path-scoped-rules#after-compaction を足した。ほかの組は入っていた |
| verify#2 | 取り込み済みを確かめた | claims-done-but-isnt（define-done・evidence-not-reports）、plausible-falsehoods（fact-checking。checking-citations は related）、summary-overstates-source（checking-citations）、rewrote-tests-to-pass の related の protect-tests |
| verify#3 | 取り込み済みを確かめた | verify.yaml の側：fact-checking → read-specs-yourself、visual-checks・looks-are-not-quality → frontend-design・make-slides、suspect-too-good-results → audit-ml-pipelines。recipes の側の変更はない |
| eval#2 | 反映した | misses-broken-evaluation の related の measure-changes を measure-changes#by-stratum にした。seems-less-capable はページがあり、felt-vs-measured を related に持つ（取り込み済み） |
| eval#4 | 取り込み済みを確かめた | test-the-verifier の related に add-tests、verifier-three-conditions は任せるのまま |
| enforce#2 | 反映した | forgot-after-compaction の related の when-to-lock を when-to-lock#spoken-rules-fade にした。spoken-prohibitions-fade への参照はない |
| enforce#7 | 反映した | stuck-in-a-check-loop の related に stop-hooks#avoid-loops を、keeps-stopping の related に what-auto-mode-stops#when-blocked を足した。instructions-ignored（when-to-lock は前提）・forgot-after-compaction（when-to-lock#spoken-rules-fade）・keeps-stopping の lock-side-effects・wrong-amount-of-approvals の what-auto-mode-stops と lock-side-effects は入っていた |
| enforce#9 | 対象外 | 情報。symptoms・recipes は sandboxing を related だけで指していて、段の逆転は起きない（確かめた） |
| safety#1 | 取り込み済みを確かめた | 症状のページ refused-or-blocked があり、when-requests-are-refused を前提に持つ。safety は when-requests-are-refused を対処の本体として残した |
| safety#8 | 取り込み済みを確かめた | explore-a-codebase → before-opening-unknown-repos、data-analysis → entrusted-data |
| delegate#5 | 反映した | wont-rethink-approach の related に open-ended-loop-trap と goal-until-done を足した（どちらも仕組みにするなので related）。stuck-in-a-check-loop（両方とも前提）・keeps-stopping と claims-done-but-isnt（goal-until-done）は入っていた |
| delegate#7 | 取り込み済みを確かめた | spec-first → goal-until-done、refactor-and-migrate → goal-until-done・batch-and-p-loops・dynamic-workflows・parallel-with-worktrees |
| judgment#3 | 反映した | going-in-circles の related に decide-when-to-quit を足した（任せるなので前提にしない）。caves-when-pushed（agreement-is-not-evidence・ask-without-sycophancy は前提）・wont-rethink-approach（decide-when-to-quit は前提）は入っていた |
| cost#3 | 取り込み済みを確かめた | hits-limits-quickly は how-usage-limits-work（前提）・what-uses-up-limits・saving-priorities を指す |
| japanese#2 | 反映した | replies-in-english の前提を keep-replies-in-japanese と can-i-prompt-in-japanese にした（keep-replies-in-japanese は整える・必須になったので逆転しない）。keep-replies-in-japanese が前提にする align-japanese-output は、直接の前提に重ねず related の先頭に移した（catalog/README §4.4 の1）。診断の順（research/27 P13）は notes の既存の記述どおり |
| recipes#1 | 取り込み済みを確かめた | delegate の goal-until-done の notes に、spec-first と refactor-and-migrate も同じ雛形を取り込むとある。spec-first の notes にも共有を書いた |
| recipes#2 | 取り込み済みを確かめた | eval の側：test-the-verifier → add-tests、verifier-three-conditions は任せるのまま |
| recipes#3 | 取り込み済みを確かめた | verify の側（verify#3 と同じ） |
| recipes#4 | 反映した | spec-first（A-6）と data-analysis（A-8）の templates の名前と notes に、prompting の let-claude-ask・prompt-patterns と同じ雛形を snippets の1か所から取り込むと書いた（prompting の notes にも同じ記述がある） |
| recipes#5 | 取り込み済みを確かめた | enforce の側：move-judgment-into-scripts → bisect-regressions、freeze-eval-assets → build-test-harness |
| recipes#6 | 取り込み済みを確かめた | safety の側：entrusted-data → office-paperwork、where-your-data-goes → data-analysis・office-paperwork |
| recipes#7 | 反映した | claims-done-but-isnt・rewrote-tests-to-pass の related に fix-a-bug#no-symptom-patches、not-what-i-meant・does-more-than-asked に spec-first、deleted-something-important に notes-and-pkm を足し、going-in-circles の fix-a-bug を fix-a-bug#when-stuck にした。safety が vetting-extensions に節 dependencies を足したので、explore-a-codebase・fix-a-bug の related に vetting-extensions#dependencies を足し、uses-nonexistent-apis の vetting-extensions をこの節にした |
| recipes#8 | 取り込み済みを確かめた | team の側：grow-review-checklists → create-and-review-prs#pr-description |
| recipes#9 | 取り込み済みを確かめた | japanese の側：documents-in-japanese → write-docs・research-and-reports、character-encodings → office-paperwork |
| recipes#10 | 反映しない | 工程4の批判的な読みに残す（audit-ml-pipelines を data-analysis の節にするのはページの統合で、この工程ではしない。brief §5） |
| team#3 | 取り込み済みを確かめた | create-and-review-prs は risk-tiered-approval・grow-review-checklists・review-bottlenecks・separate-roles などを指す |
| contest#2 | 取り込み済みを確かめた | build-observation-tools の related に insight-patterns はなく、think-before-asking を前提に持つ |
| symptoms#1 | 取り込み済みを確かめた | models は suspected-degradation を残し、related に seems-less-capable を置いた |
| symptoms#2 | 反映した | japanese#2 と同じ（replies-in-english の前提に keep-replies-in-japanese） |
| symptoms#3 | 対象外 | prompting への提案。four-specifics は整えるのままなので、not-what-i-meant（使う）の related のまま。prompting の notes は4点を研究の結果としないと書いている |
| symptoms#4 | 対象外 | extend への提案。when-to-add-what は任せるのままなので、repeating-the-same-explanation（整える）の related のまま |
| symptoms#5 | 反映した | safety が vetting-extensions#dependencies を足した。uses-nonexistent-apis の related をその節にし、notes を直した |
| symptoms#6 | 取り込み済みを確かめた | safety の側：when-requests-are-refused の related に refused-or-blocked があり、notes に分担（表示の文と切り分けは症状のページ、手段と仕組みの本体は safety）がある。この分担に合わせて refused-or-blocked の notes を直し、related の asking-for-reasoning を asking-for-reasoning#refusal にした |
| symptoms#7 | 取り込み済みを確かめた | safety の側：protecting-secrets・lethal-trifecta → secrets-exposed、prompt-injection-in-practice・instructions-hidden-in-materials → followed-injected-instructions |
| symptoms#8 | 取り込み済みを確かめた | effort-levels・fast-mode-and-advisor・always-on-costs → too-slow |
| symptoms#9 | 対象外 | start への提案（I1）。作業の終わりの時点で、six-causes の related は症状のページ33のうち10を指し、reverse-index（生成のページ）は related に持たない。症状のページの側からは33ページすべてが six-causes を指す |
| symptoms#10 | 取り込み済みを確かめた | goal-until-done・open-ended-loop-trap → stuck-in-a-check-loop、humans-set-the-parallel-limit → parallel-fatigue |
| symptoms#11 | 取り込み済みを確かめた | app の memory-faq の notes に分担（操作の本体は memory-faq、切り分けは unexpected-memories）がある |
| symptoms#12 | 取り込み済みを確かめた | summary-overgeneralization → summary-overstates-source |
| symptoms#13 | 取り込み済みを確かめた | verify の evidence-not-reports に節 tool-output ができた。claims-done-but-isnt と blames-the-tools はこのページを前提にしているので related に節を重ねず、notes に「診断の節から tool-output へ案内する」と書いた |
| symptoms#16 | メインへ | 第一波と、related に回った対処のページ（メインへ 2） |

## 2. 材料 B の行の扱い

| # | 項目 | 扱い |
| --- | --- | --- |
| 72 | コードを書かない仕事に Claude Code を使いたい（situation） | recipes/office-paperwork に同じ意味の sign（goal「コードを書かない仕事にも Claude Code を使いたい」。2段目に cli#1 で入った）があったので足さず、M2 のとおり種類を situation に、文を表の文（「にも」→「に」）にそろえた |

- 症状の33項目は、症状のページの signs にある（M2）。recipes の signs に、症状のページと同じ文はない（文字の近さで照らした）
- メインがあとで決める「文が違っても同じ困りごとを言う sign」の候補（recipes の側。変えていない）：spec-first「作らせ終えてから、思っていたものと違うと気づく」と not-what-i-meant「頼んだものと違うものが出てくる」、frontend-design「作らせた画面が、どれも同じような見た目になる」と not-what-i-meant「「いい感じに」と頼むと平凡なものしか出ない」、research-and-reports「レポートの出典を開くと、書かれていないことが書いてある」と plausible-falsehoods「確かめると数字や引用が原文と違っている」、write-docs「文書ごとに文体や用語がばらばらになる」と inconsistent-japanese-style。近さが弱いもの：fix-a-bug「直したと言われたのに、条件を変えると同じバグが出る」と claims-done-but-isnt・going-in-circles、data-analysis「自分の仮説に合う分析ばかり返ってくる」と caves-when-pushed

## 3. 題名を変えたページ（前 → 後）

なし。両分野の題名に M1 の表の語はなかった（CLAUDE.md・PR・git bisect はファイル名・コマンド）。M1 の表で summary を直したもの：

| ページ | 前 | 後 |
| --- | --- | --- |
| repeating-the-same-explanation | （指示・Project・CLAUDE.md・skill） | （指示・プロジェクト・CLAUDE.md・スキル） |
| wrong-amount-of-approvals | 権限モード・許可のルール・sandbox | 権限モード・権限ルール・サンドボックス（enforce の permission-rules・sandboxing の題名と同じ） |

## 4. 新しいページ、priority・level を変えたページ

なし。

## 5. メインへ（3件）

1. **前提の推移的な重なり（catalog/README §4.4 の1「推移的に届くものは書かない」）**：検査の道具はこれを見ないので、2段目からの重なりが残っている。symptoms 15ページ・18件（caves-when-pushed の sycophancy・agreement-is-not-evidence〔ask-without-sycophancy から届く〕、plausible-falsehoods の why-hallucinations、forgets-in-long-chats の rereads-whole-history、going-in-circles の context-rot、forgot-after-compaction の what-survives-compaction、instructions-ignored の request-vs-lock・where-instructions-sit〔when-to-lock から〕、inconsistent-japanese-style の align-japanese-output、claims-done-but-isnt の define-done、misses-broken-evaluation の verifier-defines-problem、blames-the-tools の agent-loop、deleted-something-important の checkpoints-and-rewind・permission-rules〔destructive-commands から〕、secrets-exposed の permission-rules、followed-injected-instructions の data-vs-instructions、wrong-amount-of-approvals の permission-modes-overview、seems-less-capable の effort-levels）、recipes 5件（fix-a-bug の define-done、refactor-and-migrate の verification-ladder、performance-tuning の evidence-not-reports、office-paperwork の where-your-data-goes、notes-and-pkm の checkpoints-and-rewind）。ほかの分野にもある（delegate 5・enforce 2・app・contest・extend・japanese・safety 各1）。この統合では新しい重なりを作らないようにした（basics#5・basics#6 の提案を前提に足さず、replies-in-english では align-japanese-output を related に移した）が、既存のものは、提案（basics#2・basics#5・basics#6・verify#2・judgment#3・cli#2）で前提に置かれたものが多く、外すと instructions-ignored の related が上限を超えるので変えていない。決めてほしいこと：(a) check_catalog.py に警告を足し、工程4で外す、(b) 症状のページは「原因ごとの対処の中心」を前提に並べてよいと README に例外として書く、のどちらか
2. **第一波と、related に回った対処のページ（symptoms#16）**：M10 で wave は変えていない。第一波は125ページで、統合の前と同じ。症状のページから related で指す対処の中心のうち、段か優先度の規則で前提に置けず、第一波に入らないもの：extend の when-to-add-what・what-to-put-in-claude-md（repeating-the-same-explanation・instructions-ignored）、cost の what-uses-up-limits・saving-priorities（hits-limits-quickly）、verify の protect-tests（rewrote-tests-to-pass）、recipes の fix-a-bug・spec-first（節への振り分け）。第一波の公開のときに、症状のページから未公開のページへのリンクをどう見せるかを決める必要がある
3. **features.yaml の refusals**：prompting#1 は、アプリの自動のモデルの切り替えの設定を追うなら機能の id を足すよう勧める。新しい id は足さず、既存の refusals で追うことにした（refused-or-blocked の tracks は checkpoints・refusals）。features.yaml の refusals の題名か note に「アプリの自動のモデルの切り替えの設定（Settings の Switch models when a message is flagged と、Claude Code の Config）を含む」と書いてほしい（symptoms.yaml の new_features の refusals はその書き方。features.yaml だけを読むと切り替えの設定が入るか分からない）

## 6. 検査の結果

- `python3 tools/check_catalog.py --field symptoms`：エラー 0・警告 0
- `python3 tools/check_catalog.py --field recipes`：エラー 0・警告 0
- 全体（`-q`、作業の終わりの時点）：エラー 0・警告 4（比例則 4。どれもほかの分野）。残した警告はない。M9 の比例則の警告は受け持ちにない
- 自分のスクリプトで確かめたこと：前提は4つまで・related は20件まで（instructions-ignored がちょうど20）、summary は120字以内、新しい前提の推移的な重なりがないこと（§5 の1の既存のものだけ）、`id#anchor` の anchor があること、第一波の数（125）が変わっていないこと、signs にモデル・プランの名前と変わりやすい値がないこと

## 7. 確かめていないこと、迷った点

- 一次資料は見ていない（Web を開かない指示）。根拠は材料・catalog の各ファイル・調査資料（research/23・26・27 など）による
- **B の 72 の種類**：文は「〜したい」で、README §4.5 の4の定義では goal に近いが、M2（種類は表の種類）に従って situation にした
- **forgot-after-compaction の compact-and-auto-compact#idle-compaction**：同じページを related に2回置けないので、ページ全体ではなく context#2 の提案の節にした。自動圧縮の節（auto-compact）のほうが近い読者もいる
- **instructions-ignored の block-with-exit-2 を外した**：hook-vs-skill を足すと related が21件になるので、hooks-basics と hook-recipes から届く block-with-exit-2 を外した
- **refused-or-blocked**：M5 に合わせ、related から choosing-a-model を、tracks から model-selection を外した。current-models は、切り替わった先のモデルの位置づけを読むために残した。prevents の「合っていない」は、面ごとの表示の違いを問うので残した。節 by-surface は、safety の notes の分担に合わせて「表示の文の違い」を書く節とした（safety の by-surface は仕組みを書く）
- **forgets-in-long-chats の summary の「委任」**：台帳の subagents-to-save-context（M3）に当たらないよう、notes に「出力の多い調査を本筋から離すために勧め、コンテキストの節約を理由にしない」と書いた。summary は変えていない（根拠の 05 §1-11 は、冗長な出力を subagent に任せる現行の勧め）
- **M3**：outdated_advice に、forgets-in-long-chats へ subagents-to-save-context を、repeating-the-same-explanation と inconsistent-japanese-style へ styles-for-tone を足した（research/26 #1 が、指示の置き場所と日本語の出力を揃える仕組みから Styles を外すとする）。not-what-i-meant（長さ・調子）にも関わりうるが、根拠の記述がないので足していない
- **open_issues と new_features**：symptoms.yaml の open_issues には、統合で古くなった文（keep-replies-in-japanese を related に置いた、など）があるが、番号がずれないよう残した。new_features の refusals・language-setting は features.yaml に入ったが、symptoms.yaml にも残した（検査に影響はない）
- **工程4に残した判断**：recipes#10（audit-ml-pipelines を data-analysis の節にするか）、app#6（memory-faq と how-memory-works をまとめるか。まとめれば unexpected-memories の参照を直す）
- **並列の作業**：ほかの担当が同時にファイルを書いていたので、§1 の相手の分野の状態は作業の終わりの時点のもの。途中で safety（vetting-extensions#dependencies・when-requests-are-refused の分担）と verify（evidence-not-reports#tool-output）の変更を見て、こちらの参照を合わせた

## 補足：メインの決定と、ほかの担当からの依頼による変更

- **M5**（refused-or-blocked）：summary を「会話の中の引き金・依頼の文脈・モデルのどれが効いているかを切り分け」から「面ごとの表示から何が起きたかを読み、会話の中の引き金と依頼の文脈のどちらが効いているかを切り分けて」にした。notes の手段の一覧から「モデルを変える」を外し、decisions 2026-11-03 の4つ（本当の目的と文脈を足す〔偽らない〕、巻き戻しや新しい会話で引き金を外す、誤判定を報告する、検証の制度）にした。自動の切り替えは、表示から切り替えが起きたと読む手がかり（仕組みの本体は safety）として書く。materials の「モデルを変える」には、research/26 §4.3 の1 のとおり手段として書かないと添えた
- **M10**：wave は変えていない
- **I3 からの依頼（メイン経由）**：forgets-in-long-chats の related に context の choose-what-to-read#trim-output を足した。I3 が M2 で choose-what-to-read から外したサイン「大量のログやテスト出力で会話が埋まる」は、この症状のページにあり、出力を要点に絞る節はその対処に直接当たる（整えるなので related）。あわせて同じサインの対処の hook-recipes を、テストの出力を絞る節 hook-recipes#filter-test-output にし、notes に安い順の振り分け（出力を絞る → 調査を任せる → hook で絞る）を書いた
