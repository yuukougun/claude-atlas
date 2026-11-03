# 工程3 I6：目次の統合（safety・delegate・team）の報告

- 担当：I6（2026-11-04）
- 共通の指示：[brief-integrate.md](brief-integrate.md)。材料：`state/step3-integrate/I6-input.md`（A：open_issues 48件、B：逆引きの行 13）
- 書いたもの：[planning/catalog/safety.yaml](../../catalog/safety.yaml)・[delegate.yaml](../../catalog/delegate.yaml)・[team.yaml](../../catalog/team.yaml)
- 変えたページは31（safety 14・delegate 13・team 4）。各ページの notes の末尾に「（2026-11-04 統合：<番号>）」を付けた
- ページの id と sections の anchor は消していない・変えていない。足した anchor は3つ：shared-artifacts-and-files#how-to-share・vetting-extensions#dependencies・batch-and-p-loops#not-the-batch-api
- prerequisites・priority・level・wave は変えていない（第一波の数と必須の前提は変わらない）
- 受け持ちのファイルの open_issues の欄は、2段目の提案の記録として残した（反映の状態は §1）

## 1. 材料 A の扱い

ほかの分野の状態は、ほかの担当が同時に書いているので、02:28 ごろに読んだ値である。

| 番号 | 扱い | 変えたページ・反映しない理由 |
| --- | --- | --- |
| surfaces#4 | 取り込み済みを確かめた | browser-agent-cautions の related に browser-control がある |
| prompting#1 | 反映した | when-requests-are-refused を M5 にそろえた（中身は下の「M5 の変更」）。自動の切り替えの設定は、機能の id を新しく立てず、features の既存の refusals（symptoms の提案）を tracks に入れた（メインへ 2）。refused-or-blocked の related と notes は symptoms の担当の側で、M5 にそろっている |
| context#8 | 反映した | progress-logs-for-long-jobs の notes の境界の言い方を、context の担当とそろえた（progress-files は対話で再開するための状態、こちらは無人の長時間ジョブを観察して判断するための記録）。progress-files は前提のまま残した（状態をファイルに書く考え方の土台） |
| app#1 | 反映した | shared-artifacts-and-files：節 how-to-share（特定の人への招待・公開リンク・組織の中だけの共有）を足し、節 snapshot の題を「その時点の写しと、更新のしかた」にした。summary を共有する側の操作も含む形にした。related に shared-projects-and-org-skills・files-and-code-execution を足した |
| app#6 | 対象外 | memory-faq を how-memory-works にまとめるかは、app と工程4の判断。where-your-data-goes は両方を related で指しているので、まとめたら直す（メインへ 6） |
| cli#1 | 反映しない | 「作業用のフォルダ」は recipes の office-paperwork（節 work-folder）がすでに持つ。「手動のモードで始める」を安全の既定に足すと、公式の既定（auto モード）を基準にする決定と食い違う。理由は default-safety-settings の notes に書いた（メインへ 3） |
| cli#7 | 取り込み済みを確かめた（一部反映） | delegate のページは4つの操作のページをすでに指している（下の注1）。逆引き #66 を置いた goal-until-done にも completion-notifications を足した |
| cli#8 | 取り込み済みを確かめた（一部反映） | default-safety-settings と approval-fatigue は permission-modes-overview を前提にしている。where-bypass-is-ok の related にも、モードの一覧の入口として足した |
| extend#7 | 反映した | vetting-extensions：related と tracks に mods を足した。extend の各ページから指される本体であることと、mod の確認を重くすることを notes に書いた。前提は connecting-mcp のまま（ほかの extend のページは level が上なので前提にしない） |
| extend#10 | 反映した | share-team-settings の related に claude-md-length#team |
| verify#1 | 反映した | vetting-extensions の related に looks-are-not-quality |
| eval#1 | 対象外 | メインが eval の2ページに wave: 1 を付けた。open-ended-loop-trap の前提（selection-pressure）は変えていない（symptoms の stuck-in-a-check-loop から第一波に届く道） |
| eval#4 | 取り込み済みを確かめた | open-ended-loop-trap が selection-pressure を、compare-hypotheses-in-parallel が experiment-log を前提にしている |
| enforce#4 | 取り込み済みを確かめた（notes を足した） | managed-settings-enforcement は org-managed-settings-and-mcp#delivery を指していて、境界が合う。where-bypass-is-ok と org-managed-settings-and-mcp の notes に、設定名 permissions.disableBypassPermissionsMode を書いた（古い名前を使わない）。受け持ちのファイルに古い名前はない |
| enforce#9 | 対象外（確かめた） | sandboxing（任せる）を前提にする protecting-secrets（任せる）・where-bypass-is-ok（仕組みにする）に、段の逆転はない。delegate では related にだけ置いている |
| safety#1 | 取り込み済みを確かめた | symptoms が refused-or-blocked を足し、when-requests-are-refused を前提にした。when-requests-are-refused は merged にせず、対処の本体として残した |
| safety#2 | 取り込み済みを確かめた | competition-rules が checking-ai-rules を前提にしている。practice-vs-contest-day へは competition-rules を通して届く（contest#1） |
| safety#3 | 反映した | github-actions-with-claude・cloud-schedules の related に where-bypass-is-ok を、goal-until-done の related に sandboxing を足した。headless-basics・five-questions-before-delegating・parallel-with-worktrees は元から持つ |
| safety#4 | 対象外（確かめた） | app の側。permission-modes-in-the-app・incognito-chats・artifacts-overview から safety のページへの related は入っている |
| safety#5 | 対象外（確かめた） | surfaces の browser-control が browser-agent-cautions を指している |
| safety#6 | 対象外（確かめた） | basics の data-vs-instructions が prompt-injection-in-practice を指している |
| safety#7 | 取り込み済みを確かめた | ai-usage-guidelines は checking-ai-rules を前提に、entrusted-data を related に持つ |
| safety#8 | 対象外（確かめた） | recipes の explore-a-codebase → before-opening-unknown-repos、data-analysis → entrusted-data は入っている |
| safety#9 | 取り込み済みを確かめた | protecting-secrets と cost の check-billing-path は、互いを related に持つ |
| safety#10 | 反映した | M6：default-safety-settings の notes に、節 by-stage を正本にすること（anchor は変えない）を書いた。段階ごとの既定に触れる4ページ（where-bypass-is-ok・protecting-secrets・entrusted-data・five-questions-before-delegating）は、related を default-safety-settings#by-stage にし、notes に「既定を繰り返さずに指す」と書いた。start の four-principles・roadmap からの related は start の担当が入れた。点検の目印はメインへ 4 |
| delegate#1 | 対象外（確かめた） | changes の outdated-advice-ledger は homemade-loops を外し、goal-until-done を指している（節でなくページを指す形） |
| delegate#2 | 対象外（確かめた） | start の terminology が、読者の段階と作業ごとの任せ方の段階を分けると notes に書いた。five-questions-before-delegating#autonomy-stages を指している（anchor は変えていない） |
| delegate#3 | 対象外 | cli の側。permission-modes-overview の related に agent-teams-experimental は入ったが、headless-basics はまだない |
| delegate#4 | 対象外（確かめた） | api の sdk-comparison が choosing-automation を指している |
| delegate#5 | 対象外（確かめた） | symptoms の4ページ（stuck-in-a-check-loop・wont-rethink-approach・keeps-stopping・claims-done-but-isnt）が goal-until-done を指している。前の2つは open-ended-loop-trap も指している |
| delegate#7 | 取り込み済みを確かめた | 挙げたページが delegate のページを指していることを、参照をたどって確かめた |
| judgment#2 | 対象外（確かめた） | what-not-to-delegate の level は任せるのまま（変えていない） |
| api#1 | 反映した | choosing-automation の related に managed-agents-basics がもうないことを確かめた。batch-and-p-loops に節 not-the-batch-api（API の Message Batches API とは別のもの）を足し、related に batch-api-basics を足した |
| cost#3 | 取り込み済みを確かめた | cost のページが受け持ちのページを指している（下の注2）。指している anchor はある |
| japanese#7 | 反映した | disclosure-and-provenance の related に less-ai-sounding-japanese を足した。「AI 臭さ」は読みやすさの品質で、AI の利用を隠す話ではないことを notes に書いた（方針 B4） |
| recipes#1 | 反映した | goal-until-done の notes に、停止条件の雛形を snippets の1か所に置くと書いた（recipes の spec-first・refactor-and-migrate も同じものを取り込む）。related は spec-first#goal-with-stop-conditions・refactor-and-migrate#goal-stop-conditions にした。git status の出力を会話に示させる直しは元からある |
| recipes#6 | 取り込み済みを確かめた | entrusted-data に office-paperwork、where-your-data-goes に data-analysis・office-paperwork がある |
| recipes#7 | 反映した（safety の分） | 依存のパッケージを入れる前の確かめ方を、vetting-extensions の節 dependencies にした（symptoms#5）。振り分け先の直しは symptoms の側。explore-a-codebase・fix-a-bug は、もう vetting-extensions#dependencies を指している |
| recipes#8 | 反映した | grow-review-checklists の related に create-and-review-prs#pr-description |
| team#1 | 取り込み済みを確かめた | 「チームで使う意味」を足さない決定は、team.yaml の open_issues と curb-sycophancy-and-overtrust の notes にある。変えていない |
| team#2 | 対象外（確かめた） | cost の choosing-a-plan が enterprise-vs-team-plans を指している |
| team#3 | 取り込み済みを確かめた | 挙げたページが team のページを指していることを確かめた |
| contest#1 | 取り込み済みを確かめた | competition-rules が checking-ai-rules を前提にしている。checking-ai-rules は雛形 A-2 を確認表として持つ |
| contest#2 | 取り込み済みを確かめた | is-the-task-ai-suited は format-cheatsheet#why-formats-differ を指し、format-cheatsheet は is-the-task-ai-suited を前提にしている。ideate-independently は、まとめた候補を指していない |
| symptoms#5 | 反映した | vetting-extensions に、節 dependencies（存在しない名前・後から登録された名前）・サイン・aliases（依存のパッケージの確認・slopsquatting）・材料を足した。材料は 05 1-7 で、研究の割合は使わない。summary に依存のパッケージを入れ、related に uses-nonexistent-apis を足した |
| symptoms#6 | 反映した | when-requests-are-refused：related の先頭に refused-or-blocked を置いた。分担（表示と切り分けは refused-or-blocked、手段の本体と仕組みはここ）にそって、節 by-surface の題を「面ごとの仕組み」にした。symptoms と同じ意味の症状のサイン2つは、やりたいこと・状況のサインに替えた。推論の全文を求めたときの課金の注意は asking-for-reasoning#refusal に任せた |
| symptoms#7 | 反映した | secrets-exposed を protecting-secrets・lethal-trifecta の related に、followed-injected-instructions を prompt-injection-in-practice・instructions-hidden-in-materials の related に足した。prompt-injection-in-practice の、followed-injected-instructions と同じ意味の症状のサインは外した |
| symptoms#10 | 反映した | humans-set-the-parallel-limit の related の先頭に parallel-fatigue を置いた。goal-until-done と open-ended-loop-trap は、元から stuck-in-a-check-loop を持つ。goal-until-done の材料に p56#80（ターンの上限の実例）を足した。提案は「11 第2節 分野12」としていたが、11 でこの行があるのは第1節の分野18 なので、そう書いた |

注1（cli#7 の4つの操作のページと、それを指す delegate のページ）：

- cloud-sessions-and-teleport：choosing-parallel-modes・agent-view-and-background・cloud-schedules
- control-from-phone：agent-view-and-background
- completion-notifications：progress-logs-for-long-jobs・agent-view-and-background・loop-and-scheduling
- resume-and-branch：parallel-with-worktrees

注2（cost#3 で確かめた参照）：

- check-billing-path → headless-basics#billing-path・bare-mode#authentication・protecting-secrets
- parallel-and-loop-costs → agent-teams-experimental
- choosing-a-plan → enterprise-vs-team-plans

**M5 の変更（when-requests-are-refused）**

- summary の手段：公式が案内する4つにした（巻き戻しや新しい会話で引き金を外す・本当の目的と文脈を足す・誤判定を報告する・検証の制度）
- summary の仕組み：分類器が会話全体を見ることと、自動のモデルの切り替えを足した。「言い換えや分割で回避しない理由も分かる」の文は外した
- 「モデルを変える」：通すための手段としては書かないと、notes に書いた（research/26 §4.3）
- 節 why-not-evade：題を「分類器を避ける頼み方をしない理由（利用ポリシー）」にした。書くのは、利用ポリシーが禁じることと、警告や停止になりうることだけにした（anchor は残した）
- related に isolate-with-safe-mode・what-feedback-sends・asking-for-reasoning#refusal を足した
- tracks に refusals を、材料に research/26 §4.3 を足した

**そのほかのメインの決定**

- M9（ideate-independently）：最初の案出しから AI を外す、任せる幅を絞る手順である。守りのページは足さず、警告を残した。level も見直したが、仕組みにするのままにした（理由は notes）
- M3：choosing-parallel-modes の outdated_advice に subagents-to-save-context を足した。styles-for-tone に関わるページは、受け持ちにない
- M4：when-requests-are-refused の tracks に refusals を、vetting-extensions の tracks に mods を足した。どちらも features.yaml にあるので、new_features は足していない
- M10・M11：wave は変えていない。受け持ちに生成のページはない

## 2. 材料 B の行の扱い

| # | 項目（種類） | 扱い |
| --- | --- | --- |
| 27 | 記録を残さずに相談したい（goal） | where-your-data-goes にすでにある |
| 37 | .env や migrations を絶対に触らせたくない（goal） | 足さない。protecting-secrets に、同じ意味の「.env や API キーを、絶対に読ませたくない」がある。migrations の側は enforce の permission-rules・block-with-exit-2 が受ける。このサインのバッククォートは外した（平文） |
| 38 | テストが通るまで終わらせたくない（goal） | 足さない。goal-until-done に、同じ意味の「テストが通るまで止まらずに続けてほしい」がある |
| 43 | チームで同じ設定を使いたい（goal） | share-team-settings にすでにある |
| 52 | 知らない人のリポジトリを開きたい（goal） | before-opening-unknown-repos にあったが、type が situation だったので goal にした |
| 53 | 便利そうな MCP や plugin を見つけた（situation） | vetting-extensions に、同じ意味の「便利そうな MCP やプラグインを見つけた」がある |
| 54 | Web ページやメールを読ませるのが不安（situation） | prompt-injection-in-practice にすでにある。構成で防ぐ側として、lethal-trifecta に足した |
| 56 | 入力した内容が学習に使われるか知りたい（goal） | where-your-data-goes にすでにある |
| 57 | 会社や学校で使ってよいか確かめたい（situation） | checking-ai-rules にすでにある。ai-usage-guidelines には足さない。規則を書く側のページで、使ってよいかを確かめる問いに直接答えるのは checking-ai-rules だから |
| 66 | 席を外している間も進めてほしい（goal） | five-questions-before-delegating にすでにある。goal-until-done に足した（summary が「席を外している間も作業を進められる」）。cloud-schedules には足さない。決まった時刻に走らせる方式で、その言い方「PC を閉じていても、決まった時刻に作業を走らせたい」がある |
| 67 | 毎朝決まった調査をさせたい（goal） | loop-and-scheduling にすでにある |
| 68 | 複数の作業を同時に進めたい（goal） | choosing-parallel-modes にすでにある。parallel-with-worktrees には足さない。同じ意図の狭い言い方「同じリポジトリで、複数のセッションを同時に動かしたい」がある。方式を選ぶ問いに直接答えるのは choosing-parallel-modes である |
| 70 | スクリプトや CI から使いたい（goal） | 足さない。headless-basics に「スクリプトや CI から Claude Code を使いたい」が、github-actions-with-claude に「CI の中で Claude Code を動かしたい」がある |

**M2 の3つ目を、既存のサインにも当てた**

M2 の3つ目は「症状の文を対処のページに重ねない」である。受け持ちの既存のサインに、症状のページと同じ文・同じ意味のものが6つあったので、外すか替えた。どれも、その症状のページがこのページを前提にしているので、逆引きから症状のページを通って届く。

00 §4 の症状の項目と同じ文（3つ）：

- approval-fatigue「確認のボタンを、読まずに押している」（wrong-amount-of-approvals と同じ）：外し、goal「どの確認を残し、どれを減らすかを決めたい」を置いた
- destructive-commands「ファイルを消された・消されそうで怖い」（deleted-something-important と同じ）：外し、goal「取り返しのつかない操作の前には、必ず止めてほしい」を置いた
- humans-set-the-parallel-limit「並列にしたら疲れた」（parallel-fatigue と同じ）：外した

新しい症状のページと同じ意味（3つ）：

- when-requests-are-refused の2つ（refused-or-blocked と同じ意味）
  - 外したサイン：「正当な依頼なのに断られた」「途中で別のモデルに切り替わって、答えが変わった」
  - 置いたサイン：goal「誤って断られた依頼を、どう頼み直せばよいか知りたい」、goal「返事のモデルが途中で切り替わった理由を知りたい」、situation「セキュリティや生命科学の正当な仕事に Claude を使っている」
- prompt-injection-in-practice「読ませた資料の中の指示どおりに Claude が動いた」（followed-injected-instructions と同じ意味）：外した

## 3. 題名を変えたページ

| ページ | 前 → 後 | aliases など |
| --- | --- | --- |
| delegate/dynamic-workflows | dynamic workflows（スクリプトで多数の subagent を動かす）→ dynamic workflows（スクリプトで多数のサブエージェントを動かす） | — |
| delegate/agent-teams-experimental | agent teams（複数の Claude に分担させる）→ エージェントチーム（複数の Claude に分担させる） | nav_title も変えた。aliases の「エージェントチーム」を外し、「agent teams」を入れた |
| delegate/choosing-automation | 自動化の選び方（定期タスク・headless・SDK）→ 自動化の選び方（定期タスク・非対話モード・SDK） | — |
| delegate/headless-basics | headless（claude -p）の基本 → 非対話モード（claude -p）の基本 | aliases の「非対話モード」を外し、「headless」「ヘッドレス」を入れた |
| team/org-managed-settings-and-mcp | 組織に設定と MCP サーバーを配る（managed settings）→ 組織に設定と MCP サーバーを配る（管理設定） | aliases に「managed settings」を入れた |

summary の表記だけを変えたページ（M1）：

- dynamic-workflows：subagent → サブエージェント
- agent-teams-experimental：teammate → チームメイト（research/27 §3.1 の多数派）
- bare-mode：hooks → フック
- share-team-settings：plugins → プラグイン

safety の題名と要約は、2段目でそろっていた。signs は読者の言葉のままにした。

節の題を変えたもの（anchor は同じ）：when-requests-are-refused の by-surface・why-not-evade、shared-artifacts-and-files の snapshot。

## 4. 新しいページ、priority・level を変えたページ

なし。ideate-independently の level は M9 で見直したが、仕組みにするのままにした（理由は notes）。

## 5. メインへ

1. **M2 を既存のサインにも当てたこと**：§2 の6つを外すか替えた。ほかの分野の対処のページにも、症状のページと同じ文のサインが残っていれば、同じ扱いにそろえるかを決めてほしい（受け持ちの外は見ていない）
2. **自動のモデルの切り替えの設定の追い方**：features の refusals で追う形にした（symptoms の refused-or-blocked も同じ）。facts.yml で refusals の属性として持つか、別の id（prompting#1 の例は switch-models-when-flagged）に分けるかを決めてほしい
3. **cli#1 の「手動のモードで始める」**：安全の既定には足していない。足すなら安全の既定の変更なので、作者の承認（design §9.4）が要る
4. **by-stage の点検の目印**：safety#10 の後半の提案。default-safety-settings#by-stage が作者の承認の対象（design §9.4）だと分かる目印を、数値ファイルと点検の skill のどちらで持つかを決めてほしい
5. **research/27 §3.1 の表にない語**：公式の日本語版の表記を確かめていない。用語集（M7）で決めるときに見てほしい
   - 確かめていない語：agent view・背景セッション（background sessions）・dynamic workflows・定期タスク（scheduled tasks）・旧 routines
   - チームメイト：research/27 の多数派に合わせたが、M1 の表にはない
6. **工程4（app#6）**：memory-faq が how-memory-works にまとめられたら、where-your-data-goes の related を直す

## 6. 検査の結果

`python3 tools/check_catalog.py --field <field>` の結果（最後の実行は 02:30。分野のファイル 23・ページ 361）：

- safety：エラー 0・警告 0
- delegate：エラー 0・警告 0
- team：エラー 0・警告 1
  - 比例則：ideate-independently（M9）。任せる幅を絞る手順なので、守りのページを足さず、notes に理由を書いて残した
- 全体（`python3 tools/check_catalog.py`）：エラー 0・警告 4。どれも比例則で、受け持ちの外の3つは extend の agents-md、api の feature-to-api-mapping・prompt-caching-in-practice

## 7. 確かめていないこと、迷った点

**確かめていないこと**

- 一次資料と Web は見ていない。事実は research/25・26・27 と、05・11 の記述による
- 05 1-7 の研究の割合と、11 p56#80 の事例の数値は、summary と signs に使っていない。05 1-7 の 2026 年の追試は、独立の研究者1名の論文で、査読の状況は分からない
- ほかの分野の状態（§1 の「確かめた」）は 02:28 ごろの値である。その後にほかの担当が変えていれば、ずれうる

**迷った点**

- **M2 を既存のサインに当てた範囲**：同じ文と、同じ意味のものに限った。似ているが向きの違うものは残した
  - open-ended-loop-trap「長く回したのに、手元のスコアだけ上がって本番では良くならない」と misses-broken-evaluation：長く回すループの話に絞っている
  - where-your-data-goes「会話を消したのに、まだどこかに残っていないか不安」と unexpected-memories：保持の話と、メモリの話で違う
- **vetting-extensions の題名**：変えなかった。依存のパッケージは、節・summary・aliases・サインで引ける。題名を広げるかは、工程4で見てよい
- **when-requests-are-refused の節 why-not-evade**：anchor を消せないので残し、書く範囲を、利用ポリシーが禁じることと結果に絞った。research/26 §3.3 の教材の案には、この節がない
- **progress-logs-for-long-jobs の前提**：progress-files を前提のまま残した。context#8 は「互いに related」と書いている
- **B の行を足さなかったページ**：B #66 の cloud-schedules、#68 の parallel-with-worktrees、#57 の ai-usage-guidelines には足さなかった。M2 の「その項目に直接答えるページに足す」を、こう読んだ
