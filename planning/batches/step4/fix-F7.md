# 工程4 目次の直し：F7（symptoms・recipes）の報告

- 担当：F7。日付：2026-11-04
- 指示：[brief-fix.md](brief-fix.md)、[README.md](README.md) の2段目の表（主な行：x〔routes〕・b・c・d・e・h〔R1-13〕・i・j・m・q〔add-tests〕・t）と、メインの追加の指示（routes の作り方・まとめたページを指す参照・b〜t の中身）
- 読んだもの：brief-fix.md・README.md、design-review.md（DR-02・DR-03・DR-19・§3・§6。作業中に更新された U2 の注記と §6 の13も）、catalog/README.md（T3 の routes の規則と検査）、fix-T3.md（§6 の比例則の直しを含む）、fix-aliases.md、fix-F1〜F6.md の「メインへ」（全部）と関わる §1・§2、review-R1.md の R1-02・R1-04〜R1-08・R1-10・R1-13、review-R3.md の R3-1・R3-2・R3-5・R3-8・R3-9・R3-12・R3-17・R3-20・付表A・付表B・§4、schema/site.yml、design.md §3.1・§3.3・§4.1・§6.3、requirements §3.2・§3.3、受け持ちの2ファイル（全部）と、振り分け先の候補のページ（約240。ほかの分野のファイルは読むだけ）。材料は 00 §3 分野16・§4、research/03 Q8 F4〜F6、research/04 Q6、research/22 §3.4、research/23 §3.7・F2、research/27 §3.3
- 書いたファイル：`planning/catalog/symptoms.yaml`・`planning/catalog/recipes.yaml` と、この報告だけ。git の操作と Web は使っていない。作業用の写しと集計の道具は scratchpad の F7/ に置いた
- ページの id と既存の anchor は変えていない。anchor を1つ足した（refused-or-blocked の what-stopped）。wave は変えていない（新しいページに wave: 1）。変えたページの notes の末尾に「（2026-11-04 工程4：DR-19 …）」を足し、symptoms.yaml の冒頭の注記と recipes.yaml の末尾の notes に工程4の1行を足した

## 1. DR-19 の行ごとの扱い

| 記号 | 変えたページ | 中身 | しなかったときの理由 |
| --- | --- | --- | --- |
| x | symptoms の全34ページ | routes を作った（原因 89・振り分け先 208。§1.1）。prerequisites を診断を読むのに要る概念（basics 中心）だけにした（68本 → 31本。外した54本・足した17本。§4）。level を出会う段階で6ページ付け直した（§5）。related は routes にない近いページだけにした。routes の先を related と前提から外した | — |
| b | old-advice-doesnt-work（新しいページ）・doesnt-know-latest | 「記事や前のやり方が通じない」を必須・wave: 1 で足した（§5）。routes は fix-F1 の2と fix-F4 の5(b) の案から作った。doesnt-know-latest は Claude の知識の締め切りの話に絞り、sign「古い記事のやり方が通じない」を新しいページへ移し、related の outdated-advice-ledger・term-index・checking-for-updates を外して old-advice-doesnt-work を置いた | — |
| c | misses-broken-evaluation | 題名を「手元の評価は良いのに本番で通用しない」にし、前の題名「評価のおかしさに自分からは気づかない」を aliases の先頭に移した。summary も題名に合わせた（「Claude は評価の誤りを自分からは直さない」は2文目に残した） | — |
| d | symptoms 5・recipes 1 | 外す側の別名6つを外した（§3） | — |
| e | symptoms（x の中で）・recipes 5 | 推移的な前提の警告を symptoms 18 → 0、recipes 5 → 0 にした（§4） | — |
| h（R1-13） | does-more-than-asked・instructions-ignored | does-more-than-asked に sign「古いコードを消さずに新しい版を足していく」「作業フォルダに一時ファイルを残していく」と別名「死んだコードを残す」「作業フォルダが散らかる」を、instructions-ignored に sign「決めたコマンド（uv・pnpm など）を使わず別の方法で実行する」と別名「決めたコマンドを使わない」を足した（research/03 Q8 の F4〜F6）。instructions-ignored の縛っていないの routes に hook-recipes#redirect-commands（F5 が足した節）を置いた | — |
| i | unexpected-memories | 優先度を推奨 → 必須にした。前提を basics の where-instructions-sit（必須・整える）にし、必須の前提は必須を保った。related の memory-faq（how-memory-works にまとめた）を外し、how-memory-works は routes に置いた | — |
| j | seems-less-capable | 安く確かめる順（版・effort・モデル・会話の量）をこのページだけが持つと notes に書き、前提の suspected-degradation を routes（合っていない → #official-sources、体感を信じる → #measure）に移した。前提は basics の nondeterminism | — |
| m | deleted-something-important・secrets-exposed・refused-or-blocked（と recipes の notes-and-pkm の notes） | 消された直後・漏れた直後の初動は症状のページが持つ（design §4.1 の2の例外）と notes に書いた。secrets-exposed に F6 から移した sign「会話に API キーを貼ってしまった」を足し、節 first-response に、貼った鍵も無効化から始めることと、手元の記録に平文で残ることを持たせると書いた。deleted-something-important の related に recover-lost-work（戻した後に失った作業を探す。fix-F4 の5(a)）を残した。refused-or-blocked の節 by-surface は題名を「面ごとの表示（本体は when-requests-are-refused の節 by-surface）」にし、1行で指すと notes に書いた | 対処のページの側の節（protecting-secrets の if-leaked・recover-lost-work の初動）は、F6・F4 がすでに外して症状のページを指していたので、受け持ちで直すものはなかった |
| q | recipes の add-tests | 独自の判断を notes に1行で書けなかったので、verify の pitfalls-of-ai-written-tests にまとめた（merged に into と理由。§5）。受け持ちのファイルの参照（property-based-tests の前提、refactor-and-migrate・build-test-harness の related）は、まとめた先に替えた | curb-sycophancy-and-overtrust・does-double-check-work は相手の分野でまとめ済み。それを指す symptoms の参照は直した（下の「参照」） |
| t | refused-or-blocked | 診断の最初に「何に止められたか（利用ポリシーか、auto モード・フック・権限ルールか）」を見分ける節 what-stopped を足した。利用ポリシーの枝は見えていない・散らかっている、止められた枝は合っていない（requirements §3.2 の⑤「止まりすぎ」）として routes に振り分けた（合っていない → what-auto-mode-stops#when-blocked・lock-side-effects・permission-rules）。別名は「利用ポリシーで止められた」を先頭にした。sign「操作を止められたが、何に止められたのか分からない」を足した。summary を、まず見分けることを入れた文にした | — |
| 参照 | caves-when-pushed・skipped-later-pages・forgets-in-long-chats・unexpected-memories・claims-done-but-isnt | まとめたページを指す5件を直した：curb-sycophancy-and-overtrust → caves-when-pushed の routes の separate-roles#against-sycophancy、lost-in-the-middle（2件）→ 外した（context-rot を前提に置いたので、前提と related の重なりを避けた。節 lost-in-the-middle は context-rot の中）、memory-faq → 外した（how-memory-works は routes）、does-double-check-work → 外した（verification-ladder は routes） | recipes にはまとめたページを指す参照はなかった |
| a | recipes 4（spec-first・read-specs-yourself・audit-ml-pipelines・write-docs） | 症状のページが振り分ける困りごとの言い換えだった sign を、goal か、その対処が直接答える狭い場面にした（§2） | symptoms の signs は振り分ける側。重なっていた対処の側は F1〜F6 が直していた（付表A の16組と R1-05・R1-07 の束を照らした） |
| p | skipped-later-pages・forgets-in-long-chats | 上の「参照」のとおり | — |
| f・g・k・l・n・o・r・s・u・v・w | — | 受け持ちのページに直すところはなかった。n の新しい id（large-context-window・split-models-by-role・agent-teams）は、受け持ちのファイルがすでに使っている | 該当なし |

### 1.1 x の結果（ページごとの routes・level・前提）

- routes の数：34ページで原因 89（1原因1件以上。prevents・pitfalls のどの原因にも routes がある）、振り分け先 208（1原因に1〜3件）
- 第一波（`--stats`）：**none 88・first 136・all 206**。first の内訳は wave: 1 が 62、前提でたどって届くもの 24、routes から 50、named から 0（default-safety-settings は deleted-something-important と wrong-amount-of-approvals の routes から入る）。工程4の前は 127（wave: 1 の61＋前提64＋named 2。症状のページの前提に対処を置いていたので前提で届いていた）
- **必須の先がない原因：0**。ただし、原因の先頭の先が推奨で、第一波には2つ目以降の必須の先が入る原因が13ある（§6 の4）

| ページ | level（前 → 後） | routes の原因 | 振り分け先 | 外した前提 | いまの前提 |
| --- | --- | --- | --- | --- | --- |
| not-what-i-meant | 使う | 3（見えていない・散らかっている・合っていない） | 7 | 1 | なし |
| does-more-than-asked | 整える | 3（見えていない・確かめていない・合っていない） | 7 | 1 | なし |
| keeps-stopping | 整える | 2（見えていない・合っていない） | 5 | 2 | agent-loop |
| refused-or-blocked | 整える → 使う | 3（見えていない・散らかっている・合っていない） | 8 | 2 | なし |
| caves-when-pushed | 整える | 2（確かめていない・同意を根拠にする） | 4 | 2 | sycophancy |
| insists-on-mistakes | 整える | 3（見えていない・散らかっている・確かめていない） | 5 | 2 | context-rot |
| plausible-falsehoods | 使う | 2（見えていない・確かめていない） | 4 | 2 | why-hallucinations |
| uses-nonexistent-apis | 整える | 3（見えていない・確かめていない・境界がない） | 5 | 1 | why-hallucinations・knowledge-cutoff |
| doesnt-know-latest | 使う | 1（見えていない） | 2 | 0 | knowledge-cutoff |
| old-advice-doesnt-work | （新）使う | 2（確かめていない・合っていない） | 6 | 0 | なし |
| skipped-later-pages | 使う | 2（見えていない・散らかっている） | 4 | 1 | context-rot |
| summary-overstates-source | 整える | 2（見えていない・確かめていない） | 4 | 1 | summary-overgeneralization |
| forgets-in-long-chats | 使う | 2（見えていない・散らかっている） | 5 | 2 | context-rot |
| going-in-circles | 整える | 4（見えていない・散らかっている・確かめていない・やめられない） | 8 | 2 | context-rot |
| forgot-after-compaction | 任せる | 2（散らかっている・縛っていない） | 6 | 1 | what-survives-compaction |
| unexpected-memories | 整える | 2（散らかっている・境界がない） | 6 | 1 | where-instructions-sit |
| instructions-ignored | 任せる → 整える | 3（見えていない・散らかっている・縛っていない） | 9 | 1 | request-vs-lock・where-instructions-sit |
| repeating-the-same-explanation | 整える | 2（見えていない・縛っていない） | 4 | 1 | where-instructions-sit |
| replies-in-english | 整える | 4（見えていない・散らかっている・縛っていない・合っていない） | 10 | 2 | request-vs-lock |
| inconsistent-japanese-style | 整える | 3（見えていない・散らかっている・縛っていない） | 7 | 3 | request-vs-lock |
| claims-done-but-isnt | 整える | 3（見えていない・確かめていない・預けすぎる） | 6 | 2 | agent-loop |
| rewrote-tests-to-pass | 任せる | 2（確かめていない・縛っていない） | 6 | 2 | reward-hacking |
| misses-broken-evaluation | 任せる | 2（確かめていない・預けすぎる） | 4 | 2 | verifier-defines-problem |
| stuck-in-a-check-loop | 仕組みにする → 任せる | 4（見えていない・散らかっている・合っていない・預けすぎる） | 11 | 2 | agent-loop |
| wont-rethink-approach | 任せる | 4（散らかっている・確かめていない・やめられない・預けすぎる） | 8 | 2 | なし |
| blames-the-tools | 任せる | 3（見えていない・散らかっている・確かめていない） | 6 | 2 | agent-loop・context-rot |
| parallel-fatigue | 仕組みにする | 4（確かめていない・合っていない・預けすぎる・体感を信じる） | 7 | 1 | なし |
| deleted-something-important | 任せる | 3（縛っていない・境界がない・預けすぎる） | 7 | 3 | request-vs-lock |
| secrets-exposed | 任せる → 使う | 2（縛っていない・境界がない） | 4 | 2 | where-your-data-goes |
| followed-injected-instructions | 整える | 2（縛っていない・境界がない） | 5 | 1 | data-vs-instructions |
| wrong-amount-of-approvals | 任せる → 整える | 3（合っていない・境界がない・預けすぎる） | 7 | 3 | なし |
| hits-limits-quickly | 使う | 2（散らかっている・合っていない） | 6 | 0 | how-usage-limits-work・rereads-whole-history |
| too-slow | 整える → 使う | 2（散らかっている・合っていない） | 6 | 2 | rereads-whole-history |
| seems-less-capable | 整える | 3（散らかっている・合っていない・体感を信じる） | 9 | 2 | nondeterminism |

付け直した level の根拠（level_evidence に書いた）：refused-or-blocked（整える → 使う。対話で頼む段階から断られる）、instructions-ignored（任せる → 整える。CLAUDE.md を書き始めて出会う。design §3.3 の例と同じ）、stuck-in-a-check-loop（仕組みにする → 任せる。/goal を使わなくても長い作業で出会う。R1-02）、secrets-exposed（任せる → 使う。会話に鍵を貼る形は対話の段から）、wrong-amount-of-approvals（任せる → 整える。Claude Code やアプリに作業させる段で、確認の多さと少なさの両方に出会う。auto モードを既定にする面がある。research/23 F2）、too-slow（整える → 使う。対話で使うだけで出会う）。どれも下げる向きで、前提に上の段のページを置いていない。basics の level を変える必要はなかった（fix-F1 の6の依頼はしない）。

routes を作るときに決めたこと：

1. **前提**：「これを知らないと診断が読めない」basics の概念（why-hallucinations・knowledge-cutoff・context-rot・rereads-whole-history・agent-loop・sycophancy・reward-hacking・request-vs-lock・where-instructions-sit・data-vs-instructions・nondeterminism・summary-overgeneralization・what-survives-compaction）を基本にした。basics の外の概念は、診断の中心の概念が basics にない3つだけ（cost の how-usage-limits-work、eval の verifier-defines-problem、safety の where-your-data-goes。どれも型は concept で必須）。読むのに要る概念がない7ページは前提を空にした（not-what-i-meant・does-more-than-asked・refused-or-blocked・old-advice-doesnt-work・wont-rethink-approach・parallel-fatigue・wrong-amount-of-approvals。prompting の brief-a-new-colleague は頼み方の対処なので前提にしなかった）。six-causes は、全ページの related の末尾のまま（前提にすると全症状が1つの guide に掛かり、知識マップが平らになるため）
2. **routes の先の順**：summary と診断の順で中心の対処を先に置き、近さが同じなら必須を先にした。推奨の対処が中心なら推奨を先に置いた（13原因。§6 の4）
3. **同じページを二つ以上の原因で指す**ときは、原因ごとに違う節（またはページ全体と節）を指した（replies-in-english の keep-replies-in-japanese は4原因で4つの節、seems-less-capable の suspected-degradation は2つの節、going-in-circles の fix-a-bug は2つの節など）
4. **R3 §4 が受け皿なしとした2枝**（wont-rethink-approach の散らかっている、blames-the-tools の見えていない）に先を置いた（新しい会話と引き継ぎ／サンドボックスの範囲と --safe-mode）
5. **repeating-the-same-explanation に縛っていないを足した**：extend の when-to-add-what と enforce の when-to-lock が、症状の言い換えとして situation「同じ注意を何度も繰り返している」を外したので、その sign をこのページで受け、鍵に移す合図（when-to-lock#signals）へ振り分けた（fix-F4 §2・fix-F5 の7）。principle に縛るを足し、summary を「どの注意を仕組みで縛るか」まで書いた
6. **replies-in-english の散らかっている**は、英語に戻りやすい場面を知って直後を確かめること（keep-replies-in-japanese#when）だけにした。英語のツール出力を減らす手（choose-what-to-read#trim-output）が効くと確かめた資料がないため（research/27 §3.3）

## 2. 言い換えの重なり（a）で直した sign（前 → 後）

| ページ | 前 | 後 | 重なっていた症状のページ |
| --- | --- | --- | --- |
| recipes/spec-first | symptom「作らせ終えてから、思っていたものと違うと気づく」 | goal「作り始める前に、画面の見た目と動きをモックで合意したい」（節 mock-first） | not-what-i-meant「頼んだものと違うものが出てくる」（fix-F3 の5） |
| recipes/read-specs-yourself | symptom「AI の要約だけ読んで進めたら、大事な条件を落としていた」 | symptom「AI に要約させた仕様で実装したら、仕様の条件を取り違えていた」 | summary-overstates-source「条件や但し書きが要約から落ちる」 |
| recipes/audit-ml-pipelines | symptom「検証の成績が良すぎて、本番でも同じ成績が出るか不安」 | symptom「機械学習の検証の成績が良すぎて、データの漏れがないか不安」 | misses-broken-evaluation（新しい題名「手元の評価は良いのに本番で通用しない」） |
| recipes/write-docs | symptom「文書ごとに文体や用語がばらばらになる」 | goal「プロジェクトの文書の文体と用語を、既存の文書にそろえたい」 | inconsistent-japanese-style「文体や表記が揃わない」 |

残したもの：performance-tuning「桁違いに速くなったと報告されたが、本当か怪しい」は verify の suspect-too-good-results と同じ文で、逆引きで1行に束ねる文（DR-15。fix-F5 の5）。fix-a-bug・explore-a-codebase・data-analysis・research-and-reports・frontend-design・make-slides・create-and-review-prs・refactor-and-migrate・shrink-failing-inputs・bisect-regressions の symptom は、そのレシピが直接答える狭い場面（バグの修正・コードの説明・分析の数字・レポートの出典・画面・スライド・PR・大きな変更・大きな入力・退行）なので残した。

症状のページの signs の変化（足した・移した）：does-more-than-asked に2つ（h）、instructions-ignored に1つ（h）、refused-or-blocked に1つ（t）、repeating-the-same-explanation に1つ（x の5）、secrets-exposed に1つ（m。safety から移した）、old-advice-doesnt-work に4つ（b。うち「古い記事のやり方が通じない」は doesnt-know-latest から移し、ほかの3つは F1・F4 が goal に書き換えた一般的な言い方を、症状の文として受けた）。どれも、ほかのページの sign と同じ文はない（逆引きの重複の警告0件）。

## 3. 別名の重なり（d）

外した別名（fix-aliases.md の表で受け持ちのページが外す側のもの）：

| ページ | 外した別名 | 主のページ |
| --- | --- | --- |
| summary-overstates-source | 過度な一般化 | basics の summary-overgeneralization |
| caves-when-pushed | sycophancy | basics の sycophancy |
| rewrote-tests-to-pass | reward hacking | basics の reward-hacking |
| wrong-amount-of-approvals | 承認疲れ | safety の approval-fatigue |
| deleted-something-important | 破壊的な操作 | safety の destructive-commands |
| recipes/office-paperwork | 経費精算（このページの意味の言い方「経費の一覧づくり」に替えた。fix-F2 の6） | cost の paying-in-yen |

残した別名（受け持ちのページが主）：要約の言い過ぎ（summary-overstates-source）、性能が落ちた（seems-less-capable）、提案だけで止まる（keeps-stopping）、拒否された・分類器に止められた（refused-or-blocked）、英語に戻る（replies-in-english）、評価環境（recipes の build-test-harness）。外す別名で「そのページが扱う別の機能の公式の名前」に当たるものはなかった。

足した別名：does-more-than-asked「死んだコードを残す」「作業フォルダが散らかる」、instructions-ignored「決めたコマンドを使わない」（h）、misses-broken-evaluation「評価のおかしさに自分からは気づかない」（c。前の題名）、old-advice-doesnt-work の4つ（b）。refused-or-blocked は並びだけ変えた（t）。最後の検査の時点で、受け持ちのページの別名と同じ語がほかのページにあるのは2語だけで、どちらも外す側が F3 のファイルにある（§6 の2）。

## 4. 外した前提（e と x）

design-review の U2（比例則の読み）で要件の読みを選んだときに戻せるよう、外した辺をすべて残す。【守り】は verify・eval・enforce・safety のページ（23本）。症状のページでは、守りのページは前提から外しても routes に残っている（rewrote-tests-to-pass の2本だけ related）。行き先が routes のものは「原因：先」を書いた。

推移的な前提の警告（e）は、症状のページの18件を x で前提を概念だけにして消した。推移的に届いていた前提のうち、診断を読むのに要る概念（caves-when-pushed の sycophancy、plausible-falsehoods の why-hallucinations、going-in-circles の context-rot、forgot-after-compaction の what-survives-compaction、instructions-ignored の request-vs-lock・where-instructions-sit、misses-broken-evaluation の verifier-defines-problem、blames-the-tools の agent-loop、followed-injected-instructions の data-vs-instructions）の9件は前提に残し、そこへ届く道になっていた対処のページを routes に移した。ほかの9件（caves-when-pushed の agreement-is-not-evidence、forgets-in-long-chats の rereads-whole-history、inconsistent-japanese-style の align-japanese-output、claims-done-but-isnt の define-done、deleted-something-important の checkpoints-and-rewind・permission-rules、secrets-exposed の permission-rules、wrong-amount-of-approvals の permission-modes-overview、seems-less-capable の effort-levels）は、推移的な前提そのものを外した（routes か related へ）。recipes の5件は、推移的な前提そのものを related の先頭に移した（下の表の recipes の5行。add-tests の行を除く）。

| ページ | 外した前提（分野） | 行き先 |
| --- | --- | --- |
| symptoms/not-what-i-meant | brief-a-new-colleague（prompting） | related（brief-a-new-colleague） |
| symptoms/does-more-than-asked | state-the-scope（prompting） | routes（見えていない：state-the-scope） |
| symptoms/keeps-stopping | suggest-or-do（prompting） | routes（見えていない：suggest-or-do） |
| symptoms/keeps-stopping | effort-levels（models） | routes（合っていない：effort-levels） |
| symptoms/refused-or-blocked | when-requests-are-refused（safety）【守り】 | routes（見えていない：when-requests-are-refused#official-steps） |
| symptoms/refused-or-blocked | rewind-dont-correct（context） | routes（散らかっている：rewind-dont-correct） |
| symptoms/caves-when-pushed | ask-without-sycophancy（judgment） | routes（確かめていない：ask-without-sycophancy） |
| symptoms/caves-when-pushed | agreement-is-not-evidence（judgment） | routes（同意を根拠にする：agreement-is-not-evidence） |
| symptoms/insists-on-mistakes | evidence-not-reports（verify）【守り】 | routes（確かめていない：evidence-not-reports#facts-win） |
| symptoms/insists-on-mistakes | rewind-dont-correct（context） | routes（散らかっている：rewind-dont-correct） |
| symptoms/plausible-falsehoods | fact-checking（verify）【守り】 | routes（確かめていない：fact-checking） |
| symptoms/plausible-falsehoods | allow-i-dont-know（prompting） | routes（見えていない：allow-i-dont-know） |
| symptoms/uses-nonexistent-apis | choose-what-to-read（context） | routes（見えていない：choose-what-to-read） |
| symptoms/skipped-later-pages | how-attachments-are-read（app） | routes（見えていない：how-attachments-are-read） |
| symptoms/summary-overstates-source | checking-citations（verify）【守り】 | routes（確かめていない：checking-citations） |
| symptoms/forgets-in-long-chats | rereads-whole-history（basics） | related（rereads-whole-history） |
| symptoms/forgets-in-long-chats | when-to-start-fresh（context） | routes（散らかっている：when-to-start-fresh） |
| symptoms/going-in-circles | rewind-dont-correct（context） | routes（散らかっている：rewind-dont-correct） |
| symptoms/going-in-circles | when-to-start-fresh（context） | routes（散らかっている：when-to-start-fresh） |
| symptoms/forgot-after-compaction | promises-after-compaction（context） | routes（散らかっている：promises-after-compaction） |
| symptoms/unexpected-memories | how-memory-works（app） | routes（散らかっている：how-memory-works#manage、境界がない：how-memory-works） |
| symptoms/instructions-ignored | when-to-lock（enforce）【守り】 | routes（縛っていない：when-to-lock） |
| symptoms/repeating-the-same-explanation | where-to-put-instructions（app） | routes（見えていない：where-to-put-instructions） |
| symptoms/replies-in-english | keep-replies-in-japanese（japanese） | routes（見えていない：keep-replies-in-japanese#language-setting、散らかっている：keep-replies-in-japanese#when、縛っていない：keep-replies-in-japanese#stop-hook、合っていない：keep-replies-in-japanese#app-and-api） |
| symptoms/replies-in-english | can-i-prompt-in-japanese（japanese） | related（can-i-prompt-in-japanese） |
| symptoms/inconsistent-japanese-style | align-japanese-output（japanese） | routes（縛っていない：align-japanese-output#lock-layer） |
| symptoms/inconsistent-japanese-style | consistent-politeness（japanese） | routes（見えていない：consistent-politeness、散らかっている：consistent-politeness#example） |
| symptoms/inconsistent-japanese-style | consistent-notation（japanese） | routes（見えていない：consistent-notation） |
| symptoms/claims-done-but-isnt | define-done（verify）【守り】 | routes（見えていない：define-done） |
| symptoms/claims-done-but-isnt | evidence-not-reports（verify）【守り】 | routes（確かめていない：evidence-not-reports） |
| symptoms/rewrote-tests-to-pass | verifier-three-conditions（eval）【守り】 | related（verifier-three-conditions#tamper-proof） |
| symptoms/rewrote-tests-to-pass | when-to-lock（enforce）【守り】 | related（when-to-lock） |
| symptoms/misses-broken-evaluation | check-the-metric（eval）【守り】 | routes（確かめていない：check-the-metric） |
| symptoms/misses-broken-evaluation | verifier-three-conditions（eval）【守り】 | routes（確かめていない：verifier-three-conditions） |
| symptoms/stuck-in-a-check-loop | goal-until-done（delegate） | routes（合っていない：goal-until-done#writing-conditions） |
| symptoms/stuck-in-a-check-loop | open-ended-loop-trap（delegate） | routes（合っていない：open-ended-loop-trap） |
| symptoms/wont-rethink-approach | decide-when-to-quit（judgment） | routes（確かめていない：decide-when-to-quit#ai-advice-on-quitting、やめられない：decide-when-to-quit） |
| symptoms/wont-rethink-approach | share-targets-and-bounds（prompting） | routes（確かめていない：share-targets-and-bounds） |
| symptoms/blames-the-tools | handoff-documents（context） | routes（散らかっている：handoff-documents） |
| symptoms/blames-the-tools | evidence-not-reports（verify）【守り】 | routes（確かめていない：evidence-not-reports#tool-output） |
| symptoms/parallel-fatigue | humans-set-the-parallel-limit（delegate） | routes（預けすぎる：humans-set-the-parallel-limit） |
| symptoms/deleted-something-important | checkpoints-and-rewind（cli） | related（checkpoints-and-rewind） |
| symptoms/deleted-something-important | destructive-commands（safety）【守り】 | routes（縛っていない：destructive-commands） |
| symptoms/deleted-something-important | permission-rules（enforce）【守り】 | routes（縛っていない：permission-rules） |
| symptoms/secrets-exposed | protecting-secrets（safety）【守り】 | routes（縛っていない：protecting-secrets） |
| symptoms/secrets-exposed | permission-rules（enforce）【守り】 | routes（縛っていない：permission-rules） |
| symptoms/followed-injected-instructions | prompt-injection-in-practice（safety）【守り】 | routes（境界がない：prompt-injection-in-practice） |
| symptoms/wrong-amount-of-approvals | permission-modes-overview（cli） | routes（合っていない：permission-modes-overview） |
| symptoms/wrong-amount-of-approvals | what-auto-mode-stops（enforce）【守り】 | routes（境界がない：what-auto-mode-stops） |
| symptoms/wrong-amount-of-approvals | approval-fatigue（safety）【守り】 | routes（預けすぎる：approval-fatigue） |
| symptoms/too-slow | effort-levels（models） | routes（合っていない：effort-levels） |
| symptoms/too-slow | choosing-a-model（models） | routes（合っていない：choosing-a-model） |
| symptoms/seems-less-capable | suspected-degradation（models） | routes（合っていない：suspected-degradation#official-sources、体感を信じる：suspected-degradation#measure） |
| symptoms/seems-less-capable | effort-levels（models） | routes（合っていない：effort-levels） |
| recipes/fix-a-bug | define-done（verify）【守り】 | related（define-done） |
| recipes/refactor-and-migrate | verification-ladder（verify）【守り】 | related（verification-ladder） |
| recipes/performance-tuning | evidence-not-reports（verify）【守り】 | related（evidence-not-reports） |
| recipes/property-based-tests | add-tests（recipes。まとめた） | まとめた先の pitfalls-of-ai-written-tests を前提にした |
| recipes/office-paperwork | where-your-data-goes（safety）【守り】 | related（where-your-data-goes） |
| recipes/notes-and-pkm | checkpoints-and-rewind（cli） | related（checkpoints-and-rewind） |

## 5. まとめたページ・新しいページ・priority と level を変えたページ

- **まとめた**：recipes の add-tests → verify の pitfalls-of-ai-written-tests（recipes.yaml の merged）。要点の「足したテストは、わざと壊したコードで落ちることで受け取る」は pitfalls-of-ai-written-tests の節 test-strength（と eval の test-the-verifier の節 broken-copy）と同じで、「既存のテストの書き方と境界値に合わせて足させる」（00 §3 分野16・01 KQ3）は依頼の書き方で判断ではない。テストを足す作業の落とし穴（今の挙動を正解として固める・壊しても落ちない）の本体もまとめ先にあり、独自の判断を1行で書けなかった（R3-17）。test-the-verifier ではなく pitfalls-of-ai-written-tests にしたのは、test-the-verifier が採点や評価の仕組みを確かめるページで、テストを足す読者の困りごと（AI に書かせたテストの弱さ）に近いのは pitfalls-of-ai-written-tests だから
- **新しいページ**：symptoms の old-advice-doesnt-work「記事や前のやり方が通じない」（必須・使う・wave: 1。notes に「新規（2026-11-04 工程4）」）。章は事実と出典（doesnt-know-latest の次）。原因は読者の側の情報の古さで、六つの原因では確かめていない（記事の日付と版を確かめていない → dating-information#check-date-and-version・checking-for-updates・outdated-advice-ledger#find-in-your-setup）と合っていない（記事のやり方が今の版・面・モデルに合っていない → outdated-advice-ledger・term-index#old-names・command-cheatsheet）にした（00 §4 のこの行は原因が「―」）。related にコマンドの旧名と削除の場面（ask-claude-code#check-version・writing-skills#from-commands・writing-subagents#define）と、頼み方の古い勧め（thinking-keywords・emphasis-words）、doesnt-know-latest・seems-less-capable を置いた。outdated_advice に名前と画面の変更・削除の行を6つ置いた（fork-to-branch・removed-commands・commands-directory・agents-command・routines-name・code-on-the-web-remote）
- **priority**：unexpected-memories を推奨 → 必須（DR-19 i）。新しいページを含め、必須は全体で 174 → 176
- **level**：§1.1 の6ページ（どれも下げる向き）
- **型・題名**：misses-broken-evaluation の題名（c）。型を変えたページはない

## 6. メインへ

1. **add-tests をまとめた後の受け入れ**（q。F5 のファイル）：(a) 参照のエラー3件を道具で直してほしい。3件とも add-tests を外せばよい：verify の tests-first と eval の test-the-verifier は、まとめた先の pitfalls-of-ai-written-tests をすでに同じ related に持ち（置き換えると重複になる）、verify の pitfalls-of-ai-written-tests は自分自身になる。(b) まとめ先に移すもの：節（案「テストのないコードに足させる」。手順：既存のテストの書き方と境界値に合わせて足させ、わざと壊したコードで落ちることを出力つきで見せさせる）、題名「テストを足す」と別名（テストを書かせる・テストの追加・カバレッジを上げる・単体テスト）、goal の sign「テストのない古いコードにテストを足したい」、雛形「既存のテストに合わせて足させ、わざと壊したコードで落ちることを出力つきで見せさせる依頼の型」（prompt）、材料（00 §3 分野16・01 KQ3・10 付録A-13）。symptom の sign「AI が書いたテストは全部通るが、何も確かめていない気がする」は、まとめ先の「テストは全部通るのに、バグが残っている」と同じ困りごとなので移さない。(c) まとめ先は推奨・任せるのまま（add-tests も推奨・任せるだった）
2. **残った別名の重なり（F3 のファイル）**：fix-aliases.md の更新（困りごとの言い方は症状のページを主にする）で主になった2語が、外す側に残っている。「英語に戻る」は japanese の keep-replies-in-japanese に、「提案だけで止まる」は prompting の suggest-or-do にある。F3 は「替えるならこちらから外す」と書いている（fix-F3 の2）。受け持ちの症状のページには残した
3. **old-advice-doesnt-work**：(a) routes の確かめていないの先頭の二つ（changes の dating-information・checking-for-updates）は推奨なので、第一波では準備中になる（三つ目の outdated-advice-ledger#find-in-your-setup が必須で入る）。DR-19 b が必須とした症状の中心の先なので、必須に上げるかを changes の担当とメインで決めてほしい。(b) changes の4ページ・start の term-index・cli の command-cheatsheet の related にこのページを足すか（fix-F1 の2。入ってくる道は doesnt-know-latest の related と、六つの原因の表〔生成〕でできている）。(c) registry にない（notes に新規の印。registry への取り込みはメイン）。(d) 原因を確かめていない・合っていないにした読み（読者の側の古さを六つの原因に当てた）を確かめてほしい
4. **先頭が推奨の原因（13）**：not-what-i-meant 合っていない（model-quirks → 第一波は effort-levels）、does-more-than-asked 確かめていない（diffs-humans-must-read → working-with-git）、refused-or-blocked 見えていない（when-requests-are-refused → give-reasons）、caves-when-pushed 確かめていない（ask-without-sycophancy → independent-review）、uses-nonexistent-apis 確かめていない（tests-first → evidence-not-reports）、old-advice-doesnt-work 確かめていない（dating-information → outdated-advice-ledger#find-in-your-setup）、going-in-circles 見えていない（keep-failure-lessons → handoff-documents）、replies-in-english 合っていない（model-quirks → keep-replies-in-japanese#app-and-api）、inconsistent-japanese-style 散らかっている（output-shape#mirror → consistent-politeness#example）、rewrote-tests-to-pass 縛っていない（freeze-eval-assets → permission-rules）、stuck-in-a-check-loop 見えていない（share-targets-and-bounds → experiment-log）、parallel-fatigue 確かめていない（diffs-humans-must-read → review-bottlenecks）、wrong-amount-of-approvals 預けすぎる（approval-fatigue → default-safety-settings#by-stage）。第一波で中心の先そのものを入れたいなら、その先の priority を上げる判断が要る（U1 の材料。受け持ちの外なので変えていない）。推奨の症状のページ（16）の routes も first で第一波に入る（DR-03 の推奨の案のとおり）
5. **第一波の数と中身**（U1 の材料）：first 136（routes から50）。routes から入るのは prompting 7・context 7・safety 6・delegate 5・app 4・cli 4・basics 2・cost 2・models 2・enforce 3・extend 3・verify 3・recipes 1（fix-a-bug）・team 1（review-bottlenecks）。delegate の5（what-not-to-delegate・goal-until-done・choosing-parallel-modes・humans-set-the-parallel-limit と、goal-until-done の前提の five-questions-before-delegating）は、任せる以上の症状のページの routes の先とその前提
6. **合っていないの読み**：refused-or-blocked の「auto モード・フック・権限ルールに止められた」と stuck-in-a-check-loop の「ループの組み方が課題に合っていない」を、requirements §3.2 の⑤（止まりすぎ・やりすぎ）として合っていないに当てた。⑤の括弧（モデル・effort・面・プラン）に権限モードと縛りの設定も含めて読んでよいかを確かめてほしい
7. **検査の道具**：症状の全34ページが routes を持ったので、「症状の routes」（routes がない）の検査を、設計書 §3.3 のキーの台帳（routes は symptom で必須）のとおりエラーに上げられる（T3 の §4 の3。design-review §6 の12）
8. **level を下げた6ページ**で、ロードマップの使う・整えるの列に症状のページが増える（症状のページの使うは 6 → 10。下げた3と新しいページ1。整えるは 16 のまま、任せるは 9 → 7、仕組みにするは 2 → 1）。症状のページの level は「出会う段階」なので、ロードマップでの見せ方（対処より前に出る）は生成の層で確かめてほしい
9. **MCP の不調**（fix-F4 の5(d)）：受ける症状のページはない。足すかはメインが決める（受け持ちでは足していない。新しいページは b だけという指示のため）

## 7. 検査の結果

```text
$ python3 tools/check_catalog.py --field symptoms
symptoms に関わる指摘：エラー 0 件、警告 0 件（分野のファイル 23・ページ 357 を読んだ）
$ python3 tools/check_catalog.py --field recipes
recipes に関わる指摘：エラー 0 件、警告 0 件（分野のファイル 23・ページ 357 を読んだ）
$ python3 tools/check_catalog.py --stats -q（抜き書き）
第一波: 136 ページ（wave: 1 が 62、前提でたどって届くもの 24、routes から 50、named から 0）
  routes の数え方ごとの第一波（site.yml の first_wave の routes。いまは first）: none 88・first 136・all 206
  必須の先がない cause（first ではそこから入れない）: 0
必須: 176 ページ
エラー 3 件（参照 3）、警告 3 件（比例則 3）
```

- 前の数：symptoms はエラー5（まとめたページを指す参照）・警告75（推移的な前提18・症状の前提24・症状の routes 33）、recipes はエラー0・警告5（推移的な前提5）。どちらも0件にした
- 全体のエラー3件は、add-tests をまとめたことで verify（tests-first・pitfalls-of-ai-written-tests）と eval（test-the-verifier）の related に残った参照（§6 の1）。指示のとおりメインが後で直す種類
- 全体の警告3件は比例則（extend の agents-md、api の feature-to-api-mapping・prompt-caching-in-practice）で、受け持ちの外
- 別名の重なりは道具が見ないので、自分で小文字にして空白を除いて比べた（§3）。逆引きの重複・症状の前提・routes の重なりと原因・入ってくる道・比例則（routes を数える版）は、受け持ちの2分野で0件
- 試験（tests/tools）は、道具を変えていないので流していない

## 8. 確かめていないこと

1. **routes の中身の判断**：本文がまだないので、振り分け先が中心の対処か・近い順かは、各ページの summary・signs・sections・notes から判断した。道具は中身を見ない（fix-T3 §4 の5）。別の担当の照合（V2）で見てほしい
2. **節を指した routes の先**（例：hook-recipes#redirect-commands・keep-replies-in-japanese の4つの節・fix-a-bug の節）が、執筆の後もその中身を持つか
3. **新しいページの別名と signs**（4つずつ）が、ほかのページの近い文（checking-for-updates「公式の文書にある機能やコマンドが、手元では見つからない」、writing-subagents「昔の記事の手順でサブエージェントを作ろうとしたら、作成の画面が出てこない」など）と逆引きでどう並ぶか。どちらも狭い場面として持ち主が残したもので、同じ文ではない
4. 言い換えの重なりは、付表A・R1-04〜R1-07 の束と、受け持ちのページの sign を目で照らしただけで、全ページを似た度合いで比べてはいない
5. research/03 Q8 の F4〜F6 の元の記事は読んでいない（調査資料の要約による）。auto モードを既定にする面がある点は research/23 F2 の記述による
6. Python 3.12 では流していない（3.10.12）
