# 工程4 V2：目次の直しを、design-review の DR-19 ほかに照らして確かめた報告

- 担当：V2（[README.md](README.md) の3段目。共通の指示は [brief-verify.md](brief-verify.md)）
- 日付：2026-11-04
- 書いたファイル：この報告だけ。ほかのファイルは読むだけにした。git の操作と Web は使っていない。`../kyopro-atlas` は読んでいない
- 道具は `python3 -B` で流した。一時の道具（scratchpad。リポジトリの外）からは、check_catalog.py の読む層（load_catalog・first_wave・target_priority）を読むだけで呼んだ。tools/__pycache__ の日時が変わっていないことを確かめた

## 1. 見た範囲と方法

**読んだもの**：brief-verify.md・step4 の README、design-review.md（全部）、fix-aliases.md・brief-fix.md、fix-F1〜F7.md・fix-T3.md・verify-V1.md（全部）、catalog/README.md・schema/site.yml（全部）、design.md の §2.3・§3・§4.1・§5・§6.10・§7 の表・§8.4・§8.5・§9.5・§10.1・§10.3・§10.4・§10.8・§12・§13 P〜R・変更履歴、review-R1.md の R1-04〜R1-18、review-R3.md の R3-5〜R3-9・R3-25・付表A・付表B・§3・§4、requirements §3.2 の原因の表。目次は道具の読む層で全357ページを読み、症状のページ34、まとめ先・新しいページ・改名したページ・言い換えの相手のページは YAML の原文でも読んだ。fix-D1.md は読んでいない（設計書は V1 の受け持ち）

**方法**

- DR-19 の a〜x を1行ずつ、担当の報告の「変えたページ」と、今の目次のファイルの値で照らした（報告の記述をそのまま受け取らない）
- 別名：aliases を小文字にして空白を除き、(1) 2ページ以上にある語、(2) ほかのページの title・nav_title と同じ語、(3) 自分の title と同じ語、(4) 同じページの中の重複を数えた。fix-aliases.md の表の49行を1行ずつ、主のページにあって外す側にないかを確かめた。括弧と記号も除いた緩い比べ方でも流した
- 言い換え：R3 の付表A の16組の両側の signs を並べた。症状のページの signs 114文と、ほかのページの signs 801文の全組を、2字の重なり（Jaccard）と difflib の比で並べ、上位（symptom・situation の160組、goal の50組）を目で見た。対処のページどうしの同じ文の束（24組）と近い文も並べた。DR-19 b の一般的な sign は「記事・古い・前は・以前・通じない・手元の版・昔の」で引いた
- routes：症状のページ30ページを、振り分け先の題名・summary・節・prevents と並べて読み、cause と prevents・pitfalls、to が中心の対処で近い順か、前提の型と中身、level と level_evidence、related との重なりを見た（残る4ページ〔insists-on-mistakes・summary-overstates-source・forgot-after-compaction・inconsistent-japanese-style〕は、先の id と優先度だけ見た）
- まとめた6ページ：merged の reason と担当の報告の「移すもの」を、まとめ先の節・別名・signs・雛形・材料で照らした
- 改名：旧 id（1m-context・opusplan・agent-teams-experimental・enterprise-vs-team-plans・before-using-fable・before-using-opus）を planning/catalog・design.md・design-review.md・requirements・decisions・progress・schema・tools で引いた。用語集と用語索引の入れ替えは、glossary・term-index とその節の anchor の組み合わせで引いた
- V1 の指摘：24件を、設計書・catalog/README・site.yml・design-review の該当の箇所で照らした。設計書の表の列の数は行ごとに数えた
- notes の古い記述：症状のページの id の近くにある「前提」、主を替えた9語の別名、まとめたページの id で引いた

### 1.1 道具で数えた結果（工程5の材料）

`python3 -B tools/check_catalog.py --stats`：**エラー0件、警告3件**（比例則：extend の agents-md、api の feature-to-api-mapping・prompt-caching-in-practice。3件とも notes に「任せる幅を広げる内容ではない」理由がある）。357ページ（必須176・推奨145・任意36）。

| routes の数え方 | 第一波 | 必須 | 推奨 | 任意 |
| --- | --- | --- | --- | --- |
| none | 88 | 71 | 17 | 0 |
| first（いまの site.yml） | 136 | 119 | 17 | 0 |
| all | 206 | 146 | 58 | 2 |

- first の内訳：wave: 1 が62、前提でたどって届くもの24、routes から50、named から0（default-safety-settings は routes から先に入る）。必須の先がない cause は0
- routes から入る50ページの分野：prompting 7・context 7・safety 6・delegate 5・app 4・cli 4・enforce 3・verify 3・extend 3・models 2・cost 2・basics 2・recipes 1・team 1
- **第一波に入る推奨のページ：17**。症状のページ16（keeps-stopping・refused-or-blocked・caves-when-pushed・insists-on-mistakes・skipped-later-pages・summary-overstates-source・inconsistent-japanese-style・misses-broken-evaluation・stuck-in-a-check-loop・wont-rethink-approach・blames-the-tools・parallel-fatigue・secrets-exposed・followed-injected-instructions・wrong-amount-of-approvals・too-slow）と、summary-overstates-source の前提の basics の summary-overgeneralization（前提を持たない）。design §2.3 の推奨の案のとおり必須に上げると、必須は 176 → 193
- 原因の先頭の先が推奨で、第一波には2つ目以降の必須の先が入る原因：13（F7 の §6 の4 の一覧と一致）。うち症状のページが必須のもの7：not-what-i-meant の合っていない（先頭 model-quirks）、does-more-than-asked の確かめていない（diffs-humans-must-read）、uses-nonexistent-apis の確かめていない（tests-first）、old-advice-doesnt-work の確かめていない（dating-information・checking-for-updates）、going-in-circles の見えていない（keep-failure-lessons）、replies-in-english の合っていない（model-quirks）、rewrote-tests-to-pass の縛っていない（freeze-eval-assets）
- 使用量の概算（design §12 の19 の1ページ35〜45万トークンを当て直した見当）：第一波136ページで約4,760万〜6,120万、必須176で約6,160万〜7,920万、193に上げると約6,760万〜8,690万
- 症状のページ：34（必須18・推奨16。level は使う10・整える16・任せる7・仕組みにする1）。routes の原因89・振り分け先208（先の優先度は必須156・推奨50・任意2）。前提31本（空は7ページ。basics と start の外は cost の how-usage-limits-work・eval の verifier-defines-problem・safety の where-your-data-goes の3本で、どれも concept）
- 前提の鎖：最長8段（long-team-competitions、祖先20）、深さ7以上8ページ、6以上31ページ。症状のページは最長5段
- 別名：2ページ以上にある語は2（/deep-research：using-research・dynamic-workflows、音声入力：voice-and-mobile・images-and-voice。どちらも担当が「別の機能の公式の名前」の例外として残した）。ほかのページの題名と同じ別名0、ほかのページの nav_title と同じ別名1・同じページの中の重複1（指摘11）、自分の題名と同じ別名0

## 2. 指摘の一覧

| 番号 | 重さ | 場所 | 問題 | 根拠 | 直し方の案 |
| --- | --- | --- | --- | --- | --- |
| 1 | 直す | design §3.2 の表（144〜145行）、§3.3 のキーの台帳（194〜216行） | V1 の指摘5の直し（変更履歴の最後の行「wave を骨格で front matter に写す（§3.3）」）で、`wave` の行が §3.3 のキーの台帳でなく、§3.2 の分類の軸の表（4列）に入った。144行は6セル（キーの台帳の5列の形の前に、軸の名「前提と関連」が残っている）、145行は3セル（軸の名が抜けた `prerequisites`・`related` の行）で、表が崩れている（描画では wave の行の後ろ2セルが落ち、前提と関連の行が1列ずれる）。§3.3 のキーの台帳には wave の行がなく、§5.1（280行）の「骨格で front matter にも写す。§3.3」の参照先がない。page.schema.json はキーの台帳から作る（§3.3 の末尾）ので、このままでは骨格で写した wave がスキーマにない | V1 の指摘5、design の変更履歴の最後の行、§5.1・§3.3 | 145行を「\| 前提と関連 \| `prerequisites`・`related` \| ページの id（related は `id#anchor` も可） \| 知識マップ・次に読む・ロードマップの順 \|」に戻して144行を消し、§3.3 のキーの台帳に「\| `wave` \| 第一波の核のページだけ \| 目次（骨格で写す） \| 第一波の一覧（道具が routes と前提でたどって出す）・公開の区切り \| 1。核の分野の総論と多く前提にされるページ、入口と症状辞典の全ページ（§5.3） \|」を置く |
| 2 | 直したほうがよい | symptoms.yaml の misses-broken-evaluation（760行。routes 780行・related 783行） | R1-07 の束（手元のスコアは良いのに本番で悪い）の受け皿なのに、束のページのうち eval の selection-pressure（良かった版を選び続ける。必須）と delegate の open-ended-loop-trap（長く回し続ける。R3 付表A の5）を、routes にも related にも持たない。どちらの sign も DR-19 a・c で「原因に固有の場面」に書き換えられ、この症状のページから振り分けられる形になったが、症状のページからは前提の verifier-defines-problem の related か stuck-in-a-check-loop を経てしか着かない（ほかの束のページは、check-the-metric・verifier-three-conditions が routes、evaluators-by-format・lockbox-and-holdout が related にある） | DR-19 a・c（R1-07 の案：選び続けた・指標がずれた・隠しテストで落ちた・長く回した、など原因に固有の場面に書き換える）、DR-02（原因ごとに中心の対処） | related の先頭に selection-pressure と open-ended-loop-trap を足し、notes に「選び続けた・長く回した」の枝を書く（確かめていないの to は3件あるので、routes に入れるなら check-the-metric と比べて決める） |
| 3 | 直したほうがよい | notes：japanese の keep-replies-in-japanese（114行）、verify の own-generated-code（489行）、safety の when-requests-are-refused（640行）、basics の how-thinking-works（266行）、judgment の how-much-understanding-to-keep（324行）、cli の permission-modes-overview（134行） | メインが fix-aliases.md の主を9語替えた後も、担当が書いた notes が今の別名と逆のことを言う。keep-replies-in-japanese「英語に戻るは fix-aliases でこのページが主なので残した」（今は別名にない）、own-generated-code「認知負債は fix-aliases.md の表でこのページが主」（ない）、when-requests-are-refused「拒否された・分類器に止められたはこのページを主にした」（ない）、how-thinking-works「拡張思考は…外した」と how-much-understanding-to-keep「認知負債は…外した」（どちらも今はある。メインの注記「重なった別名の主を替えた。fix-aliases.md」はあるが、何をどこへ移したかを書いていない）、permission-modes-overview「fix-aliases.md では app の permission-modes-in-the-app が主」（今の表はこのページが主）。骨格の後も notes は執筆の指示として読まれる | fix-aliases.md の冒頭の3行目と表、DR-19 d、design §5.2 の5 | 6ページの該当の文を今の状態に書き換えるか、文の後に「（2026-11-04 メイン：主を〜に替え、この別名は〜へ移した／ここへ移した）」と添える |
| 4 | 軽い | design §5.3（295行） | aliases の規則が「ほかのページの題名と同じ語は入れない」だけで、「自分の題名と同じ語」がない。catalog/README §4.5 の2 は V1 の指摘11を受けて両方を書いた | V1 の指摘11 | §5.3 を「自分の題名とも、ほかのページの題名とも同じ語は入れない」にする |
| 5 | 軽い | design §8.5（526行） | §8.4 に未公開のページの定義を1か所で置き「この節と §8.5・check_pages.py は、この定義を使う」としたが、§8.5 のページ下部の項は「stub は「題名（準備中）」の平文」のまま | V1 の指摘6、design §8.4 | 「未公開のページ（§8.4）は「題名（準備中）」の平文」にする |
| 6 | 軽い | catalog/README の冒頭（5行）と版の行（7行） | 冒頭の「catalog は凍結して執筆の指示（materials・templates・visual）としてだけ使う」が、design §5.2 の5（V1 の指摘24の直しで「notes の見せ方」を足した）と §5.1（wave を骨格で front matter に写す）に合っていない。版の行に、V1 の指摘を受けた直し（§3 の例、§4.2 の2、§4.3 の4、§4.5 の2〜4、§5 の主のページ）がない | V1 の指摘12・24、catalog/README 冒頭（この文書は設計書の詳細） | 冒頭の括弧を「materials・templates・visual・notes の見せ方」にし、wave は骨格で front matter に写すと足す。版の行に V1 の指摘による直しを足す |
| 7 | 軽い | notes：app の where-to-put-instructions（41行）・how-attachments-are-read（187行）、verify の evidence-not-reports（76行）・fact-checking（215行）・protect-tests（351行）・verification-ladder（110行）、eval の felt-vs-measured（80行） | DR-02 で症状のページの対処を前提・関連から routes に移したのに、対処のページの notes が「症状のページがこのページを前提（protect-tests は related）にして振り分ける」と書いたまま（5ページ。今はどれも routes）。felt-vs-measured は「seems-less-capable の前提に置ける」とするが、judgment の型なので症状の前提に置けない（今は routes）。verification-ladder には「prompting の does-double-check-work と台帳 add-double-check を分け合う」が、まとめた後も残る。同じ型の notes を、F6 は safety と delegate の5ページで同じ工程に直している | DR-02、DR-19 q、catalog/README §4.4 の6 | 「前提に」を「routes に」と読める文に直す（例：「症状の X が routes でこのページへ振り分ける」）。verification-ladder の古い1文を消す |
| 8 | 軽い | team.yaml の choosing-an-org-plan の notes（312行）、design-review の DR-19 n・o | notes に「id にもプラン名が入るが、id は変えない」と、その後に「（2026-11-04 メイン：id を choosing-an-org-plan から改めた…）」があり、向きが逆で前の文とも食い違う。この改名は DR-19 n（3つ）にも §6 にもなく、DR-19 o は旧 id の enterprise-vs-team-plans で名指ししている（担当の報告 fix-F6 も旧 id で書く） | DR-19 n・o（メインの改名は DR-19 n に記録した）、design §5.3（id は骨格の後は変えない） | notes を「id を enterprise-vs-team-plans から choosing-an-org-plan に改めた」にして前の文を消す。DR-19 n か §6 に4つ目の改名として足す |
| 9 | 軽い | symptoms.yaml の doesnt-know-latest（routes 311行）、too-slow（routes 1120行） | doesnt-know-latest の見えていないの先は search-research-thinking（アプリの比較のページ）と ask-claude-code（推奨）だけで、summary が挙げる「公式の資料」を渡す手（context の choose-what-to-read。必須で第一波にある）は related にある。第一波の診断の節では、Claude Code で古い書き方を出された読者への先が出ない（uses-nonexistent-apis は同じ原因の先頭に choose-what-to-read を置く）。too-slow の散らかっているは always-on-costs・pruning-extensions（拡張の重さ）を先に、when-to-start-fresh（長い会話）を3番目に置くが、level を使うに下げた根拠（level_evidence：対話で長い会話の重さとして最初に出会う。拡張で重くなる形は整える段から）と順が合わない | DR-02（原因ごとに中心の対処を近い順に） | doesnt-know-latest の見えていないに choose-what-to-read を足す（2番目）。too-slow は when-to-start-fresh を先頭にするか、順の理由を notes に書く |
| 10 | 軽い | symptoms.yaml の parallel-fatigue の level_evidence（902行） | 「並列の方式を選ぶ delegate の choosing-parallel-modes が仕組みにするの段」と、対処のページの段を根拠にしている（R3-1 で直した型）。題名の「レビューが追いつかない」は、team の review-bottlenecks が工程4で任せる（AI が書いた PR が増えて詰まり始めるとき）にした。並列にした段で出会うなら、design §3.1 の表では並列は回すの読者になる | DR-02・DR-19 x（level は出会う段階）、design §3.1 | 出会う段階で level_evidence を書き直し、段を決め直す（任せるで出会うなら下げる） |
| 11 | 軽い | 別名：fix-aliases.md の表、basics の how-thinking-works（245行）、delegate の automated-pr-review（628行）、enforce の hooks-basics（315行）、extend の claude-md-vs-rules-skills-styles（248行） | (a) 例外として残した2語（/deep-research・音声入力）が、fix-aliases.md の表では外す側のまま残り、扱い（面の印を付けて並べる）は担当の報告（fix-F2 §6 の4・fix-F3 §6 の3）にあるだけ。(b) 機能の主のページが分かれうる語：how-thinking-works の別名 effort（機能 effort のページは題名に effort を含む models の effort-levels）、/security-review は automated-pr-review（任意）の別名にだけあり、機能 security-review の節は verify の independent-review（必須）にある。(c) hooks-basics の別名に hooks と Hooks（小文字にすると同じ）、claude-md-vs-rules-skills-styles の別名「指示の置き場所」が app の where-to-put-instructions の nav_title と同じ | DR-15（用語索引は機能ごとの主のページを先に出す。主は 6b で決める）、DR-19 d、catalog/README §4.5 の2 | (a)(b) を fix-aliases.md の表か features.yaml の note に書き、6b で features の page を決めるときの材料にする。(c) は片方を外す |
| 12 | 軽い | basics の data-vs-instructions（530行）、safety の prompt-injection-in-practice（273行）・lethal-trifecta（342行） | goal「Web ページやメールを読ませて大丈夫か知りたい」が、わざと束ねた situation「Web ページやメールを読ませるのが不安」（00 §4 の項目）と同じ問いなのに、文がそろっていない。逆引きで近い行が2つ並ぶ | DR-15（まとめる goal は同じ文にそろえ、まとめないものは場面を書き分ける）、catalog/README §4.5 の4 | data-vs-instructions の文を束に合わせるか、もう1つの goal（なぜ従ってしまうのか）だけにする |
| 13 | 軽い | tools/check_catalog.py の「症状の routes」、catalog/README §6 の表 | design-review §6 の12 は「検査は、症状の担当が routes を書き終えるまで警告にする」とした。症状のページ34すべてが routes を持ったので条件は満ちたが、まだ警告のまま（いまは0件なので影響はない） | design-review §6 の12、design §3.3（routes は symptom で必須） | 検査をエラーに上げ、README §6 の表を直す（道具の担当かメインが行う） |
| 14 | 軽い | design §12 の1・19（777行〜） | 工程5で示す要約の元の数が、直しの前の数（第一波125・推奨25、必須174、使用量の概算は125ページの場合）のまま。V1 の指摘14の3つ目（kyopro-atlas の AtCoder の規則の書き方の件）も §12 にない | DR-03・DR-13、design §12 の見出し（工程5で示す要約の元） | 工程5の前に §1.1 の数（第一波136・推奨17、必須176、上げると193）で書き直す。kyopro-atlas の件は §12 に足すか、工程5の一覧に足すと決める |

件数：直す1・直したほうがよい2・軽い11（計14）。

## 3. 決定どおりと確かめたもの

- **DR-19 a**：付表A の16組は、どれも対処の側が goal か、その対処が直接の答えになる狭い場面になった（両側の今の signs で確かめた）。R1-04 の束（12本の症状のページ）、R1-07 の5ページの sign も直った。全組の比べで、新しい言い換えの重なりは見つからなかった（上位は README §4.5 の4 の「より狭い場面」〔例：when-to-lock の「CLAUDE.md に「〜しない」と書いたのに破られる」〕か goal の形）。同じ文の重なり（逆引きの重複）は0件
- **b**：old-advice-doesnt-work（必須・使う・wave: 1・章は事実と出典・診断の節あり）を足し、台帳・用語索引の旧名・版の確かめ方へ振り分けた。doesnt-know-latest は知識の締め切りに絞った。一般的な sign は新しいページにだけあり、ほかは狭い場面（Cowork・GitHub Action・サブエージェントの作成の画面など）か goal
- **c**：題名を読者の言葉にし、前の題名を aliases の先頭に移した
- **d**：fix-aliases.md の49行のうち47行は表どおり（主のページにあり、外す側にない）。残る2語は例外（指摘11）。主を替えた9語も今の目次で表どおり
- **e**：推移的な前提の警告0件。付表B の4本はどれも前提から外れ、related にある。最長9段→8段
- **f**：team の14ページの level と level_evidence を付け直し（使う1・整える3・任せる5・仕組みにする5）、「チームで導入する」を必須の ai-usage-guidelines で受ける（team の必須は2）
- **g**：api の rate-limits-and-errors（推奨・仕組みにする・章「上限とエラー」・tracks に api-rate-limits。features.yaml にも入った）。入ってくる道は cost の how-usage-limits-work・when-ai-is-unavailable と api の batch-api-basics の related。題名・summary・signs に値はない（429・529 は sign と aliases だけ）
- **h**：R1-13（does-more-than-asked の2文と別名、instructions-ignored の sign、hook-recipes#redirect-commands と雛形）、R1-14（where-bypass-is-ok の別名3つと sign。sandboxing は節 containers だけ）、R1-15（independent-review の goal と節 security-review、features.yaml の security-review）、R1-16（checking-ai-rules の sign・別名・節 rights-and-licenses、ai-and-sources の別名「この辞典のライセンス」）、R1-17（connecting-mcp の sign・節 troubleshooting・別名 /mcp）、R1-18（ask-for-options の goal と別名）
- **i**：memory-faq を how-memory-works にまとめ（節 deleted-chats・turning-off を同じ anchor で、別名 Memory FAQ・メモリの Pause と Reset、goal の sign、tracks の incognito）、unexpected-memories を必須にした（前提の where-instructions-sit も必須）
- **j・k・l**：安く確かめる順は seems-less-capable の summary と notes に、suspected-degradation は測る手順と製品の側の確かめ方（recipe、題名「劣化を疑ったら測って確かめる」、節 check-order なし）。理解の線引きは how-much-understanding-to-keep、own-generated-code は説明させて確かめる手順（recipe）。削り方は claude-md-length（節 init-draft）、init-and-first-claude-md は /init の操作と流れ（節 prune は1段落で指す）
- **m**：初動は deleted-something-important#recover と secrets-exposed#first-response（sign「会話に API キーを貼ってしまった」を移した）が持ち、protecting-secrets の節 if-leaked は外れた。refused-or-blocked の節 by-surface は1行で when-requests-are-refused#by-surface を指す
- **n と改名**：旧 id（6つ）の参照は目次・設計書・design-review・要件・決定・progress・site.yml・道具で0件（design-review の DR-19 n・o の記録の文だけ）。choosing-an-org-plan・before-using-top-model は registry とすべての参照が新しい id。用語集 glossary（節 definitions・split-terms など）と用語索引 term-index（節 old-names）の取り違えは0件
- **o・s・t・u・v・w**：cloud-schedules・choosing-an-org-plan の題名と thinking-keywords の summary から変わりやすい値が外れた。org-managed-settings-and-mcp は配る経路・グループ・MCP の許可に絞った。refused-or-blocked は節 what-stopped と別名の並び。refine-in-conversation の sign は rewind-dont-correct の側だけ。/usage は what-uses-up-limits#find-what-uses-it、/context は inspect-context#reading が持ち主で、cli・eval のページはそこを指す。summary の4ページは1文目が「何ができるか」か「答え」
- **p・q**：lost-in-the-middle → context-rot#lost-in-the-middle（別名4つ・goal・材料・related を移した）、ai-amplifies-organizations → paved-roads#amplifier（旧題・別名・sign 2つ）、curb-sycophancy-and-overtrust → separate-roles#against-sycophancy（承認の場面の sign と別名は risk-tiered-approval）、does-double-check-work → verification-ladder#verbal-checks（題名と別名）、add-tests → pitfalls-of-ai-written-tests（節 add-to-untested・別名5つ・goal・雛形・材料）。まとめたページを指す参照は0件。completion-notifications は notes に独自の判断を1行で書いて残した
- **r**：competition-rules から checking-ai-rules と重なる節を外して前提で指した（anchor 2つを外した。brief-fix §4 より DR-19 r を優先。参照は0件）。sign と図の案は checking-ai-rules へ
- **x と DR-02**：34ページすべてに routes（原因89・先208）。cause と prevents・pitfalls は全ページで一致し、1原因の先は3件まで。前提はすべて concept（31本、空7）。level は6ページを下げ、前提に上の段はない。routes の先と前提・関連の重なりは0件。見た30ページの routes は、cause がそのページの原因に合い、先頭は summary と診断の順で中心の対処になっている（例外は指摘2・9）。refused-or-blocked と keeps-stopping の合っていないに権限モードや縛りを置く読みは、要件 §3.2 の⑤（止まりすぎ）と2ページでそろっている
- **DR-15・DR-17・DR-18（目次の notes）**：reverse-index・term-index の notes に節の分け方と主のページの出し方。how-to-use・ai-and-sources の notes（公式の教材の案内、守れない約束を書かない、「完成」の意味、承認の時期）。rereads-whole-history の図を、公式の図へのリンクを主にした静止図にした。名称の表を正にし台帳の行を残す notes が outdated-advice-ledger・change-timeline-2026・term-index・choosing-a-plan・command-cheatsheet・cloud-schedules にある
- **V1 の指摘**：直す3件は直った（§12 の1 と §13 P が「最初の必須の振り分け先」、§12 の21 の終わりの条件、DR-15 の6b の決定と §10.1 の6b の終わりの条件と catalog/README §5）。変更履歴の最後の行の直し（§2.3 の推奨のページを上げること、§8.4 の未公開のページ、§2.3・§10.1 の公開の区切り、§8.5 の最小の文、§10.8 の途中で聞くこと、§3.1 と design-review §6 の13 の比例則）は、wave の置き場所（指摘1）を除いて直った。ほかに V1 の指摘10・13・15〜23 も直っていた（11・6・12・24 の残りは指摘4〜6）

## 4. 決定の中の食い違い

1. **目次の notes の「見せ方」の時期**：DR-17 と design §6.10 は「どのページで何を使うかは、目次の notes に見せ方として書く」とし、§5.2 の5 は catalog を骨格（6c）で凍結して「notes の見せ方」を執筆の指示に使うとする。一方、題材の一覧は §10.1 の7 で試作の始め（6c の後）に作る。誰がいつ notes に書くかが決まっていない。工程4では、F5 が8ページに書き（ほかに basics の unfaithful-reasoning）、F1〜F4・F6・F7 は受け持ちの行にないとして書いていない（DR-17 の反映先にも目次は入っていない）。6c の前にメインが一覧を作って notes に写すか、§6.10 を「試作の始めの一覧に書く」に改めるかを決めるとよい
2. **DR-19 m と DR-03（U1）**：漏れた直後の初動は症状のページ secrets-exposed（推奨）が持ち、必須の safety の protecting-secrets から節 if-leaked を外した。推奨の案（第一波に入る推奨のページを必須に上げる）なら初版に入るが、U1 で (c)「核を必須の症状に絞る」を選ぶか上げないと、初版（必須）に API キーが漏れた直後の初動がなくなる。工程5で U1 を示すときに添えるとよい（deleted-something-important は必須なので当たらない）
3. **DR-19 b と DR-02・§6 の1**：DR-19 b は新しい症状のページを必須にし「版の確かめ方へ振り分ける」とするが、版の確かめ方の2ページ（changes の dating-information・checking-for-updates）は推奨のまま。routes に優先度の規則を当てない決定（DR-02）と「第一波には最初の必須の先」（§6 の1）により、第一波と初版では、この枝の先頭2つが「準備中」になる（F7 は台帳の節 find-in-your-setup を3つ目に足して埋めた）。F7 が上げるかを尋ねている（fix-F7 §6 の3(a)）が、決定の記録はまだない

## 5. 確かめていないこと

- routes の中身は30ページを振り分け先の summary・節と照らしたが、本文がないので「中心の対処か」は目次の記述からの見立て。残る4ページは先の id と優先度だけ見た
- 言い換えは、2字の重なりと difflib の比の上位と、付表A・R1-04〜R1-07 の束を目で見たもの。比の低い言い換え（言葉の違う同じ困りごと）は見落としがありうる
- notes の古い記述は、症状のページの id と「前提」の近さ、主を替えた9語、まとめたページの id で引いただけで、357ページの notes を全部は読んでいない
- まとめたページの元の中身は、git を使わないので見ていない。merged の reason と担当の報告の「移すもの」と照らした
- 設計書は §1 に挙げた節だけを読んだ。V1 の指摘のうち、本文の書き換えの言い回しの良し悪しは見ていない
- 道具の試験（tests/tools）は流していない。数は道具の読む層を呼んで数え直し、F7 の報告（原因89・先208・第一波136・必須176）と一致した
- rate-limits-and-errors の中身（状態コードの意味・再試行の既定）と、各ページの材料の一次資料は確かめていない（Web を開かない）
- 逆引き・用語索引・知識マップはまだ生成されないので、束ねた文が1行に出ること、例外の別名が印付きで並ぶことは確かめていない
