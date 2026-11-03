# 工程4：設計の見直し R3（目次の質）

- 担当：R3（観点：目次の質。粒度・境界・レベル・優先度と第一波・前提と関連・文・症状辞典・台帳）
- 日付：2026-11-04
- 指示：[brief-review.md](brief-review.md) §4 の R3

## 1. 見た範囲と方法

**読んだもの**

- 全部：`planning/requirements.md`、`planning/decisions.md`、`planning/design.md`、`planning/catalog/README.md`、`schema/site.yml`、`planning/batches/step3/README.md`・`brief-catalog.md`・`brief-integrate.md`
- 道具で全件を読んだもの：`planning/catalog/` の23分野のファイル（361ページの全キー）、`registry.yaml`（pages・ledger・notes）
- 抜き出して読んだもの：`features.yaml`（成熟度の記述の有無）、`catalog-C12.md`・`integrate-I7.md`・`tool-T2.md`（前提・第一波・逆引きの重複の判断）、`research/20`（前提の扱い）、`research/22` §3.4（台帳の足す候補）、`research/23` §3.7（やめてよい助言）
- `python3 tools/check_catalog.py --stats` と、T2 の後の `python3 tools/check_catalog.py`（エラー0、警告39：推移的な前提35・比例則4）

**数えた方法**（すべて Python で目次の YAML を読んで数えた。道具のコードは使っていない）

- 第一波：`wave: 1` の61ページから prerequisites をたどった閉包。症状のページを核から外したとき・症状のページの前提を basics の概念だけにしたとき・原因ごとに振り分け先を1つ足したときの閉包も作って比べた
- 症状のページ：33ページの level と前提の段、level_evidence の文、prevents（原因）ごとに、その原因を prevents に持つ対処のページが前提か関連にあるか、それが第一波にあるか
- 関連：第一波のページの related のうち第一波の外を指すもの、被リンク（前提と関連）の数
- signs：症状のページの105文とほかのページの802文の全組を、2字の重なり（Jaccard）と difflib の比で並べ、上位を目で見て言い換えを選んだ。症状のページ以外どうしの同じ文と近い文も数えた
- 前提：推移的に届く前提、鎖の深さ（最長の前提の段数）と祖先の数、辺を関連に移したときの深さ
- 優先度と段階：registry の見当との差、必須の閉包
- 文：題名・summary・signs・id の数字・名称・成熟度の語、平文の欄の記法、summary の1文目の形（正規表現）

道具の担当の数と照らした：推移的な前提35件は自分の数え方でも35件、症状のページの関連437件のうち第一波の外213件も一致した。「似た組9組」は、自分の数え方では16組になった（R3-5）。

## 2. 指摘の一覧

| 番号 | 重さ | 場所 | 問題 | 根拠 | 直し方の案 |
| --- | --- | --- | --- | --- | --- |
| R3-1 | 重大 | `symptoms.yaml` の33ページの prerequisites（ファイル冒頭の注記「prerequisites には、原因ごとの対処のうち中心になるページを」）、catalog/README §4.4 の1、design §3.1 の2・3 | 症状のページの前提を「原因ごとの対処の中心」の意味で使っている。前提（これを知らないと読めない）と振り分け先（読んだ後に行く先）が1つのキーに混ざり、(a) 症状のページの段階が「出会う段階」でなく対処のページの段で決まる、(b) どの対処を「中心」にするかが段と優先度の規則で決まる、(c) 生成する知識マップとロードマップで、対処が症状より前に描かれる、(d) 第一波の48ページはこの前提だけで入る | 33ページすべてで level が前提の最も高い段と同じ。10ページの level_evidence が「〜と同じ段」「そろえた」と書き、5ページが「上の段の対処は related に置いた」と書く（not-what-i-meant の four-specifics、repeating-the-same-explanation の when-to-add-what・what-to-put-in-claude-md、hits-limits-quickly の what-uses-up-limits など）。refused-or-blocked（整える）は自分の対処の when-requests-are-refused（使う）より上の段。instructions-ignored は前提の when-to-lock のため任せる（design §3.3 の例は整える）。design §3.1 の2は「symptom は出会いやすい段階」、§1.2 は症状のページが「対処のページへの振り分け」を持つとする。推移的な前提35件のうち18件も症状のページで、原因は同じ | 骨格の前（front matter の形を決める工程6より前）に、振り分け先を別のキーにする。例：`routes: [{cause: 見えていない, to: [four-specifics, let-claude-ask]}, ...]`。routes には段と優先度の規則を当てない（上の段の対処も中心に置ける）。症状のページの prerequisites は、診断を読むのに要る basics の概念だけにし、level は出会う段階で付け直す。診断の節のリンク・知識マップ・ロードマップは routes を読んで生成する。I7 の案 (b)（README に例外として書く）は (a)〜(c) が残るので採らない。第一波の数え方は R3-2 |
| R3-2 | 重大 | design §2.3（第一波は前提でたどれるページ）・§8.5（公開するページから stub へのリンクを止める）・§9.4、`check_catalog.py` の第一波の数 | 第一波が前提だけで閉じていて、リンクでは閉じていない。第一波のページの関連の半分が、第一波の公開の時点で stub のページを指す。未公開の先をどう見せるか（隠す・文字だけにする）の規則が設計にない。安全の既定の正本 `default-safety-settings#by-stage`（必須）も第一波の外にある | 第一波125ページの related 1330件のうち648件（189ページ）が第一波の外。症状のページでは437件のうち213件（128ページ）。§8.5 は stub へのリンクを --strict と check_pages.py で止めるので、このままでは第一波を公開できない。default-safety-settings は第一波の10ページ（four-principles・roadmap・deleted-something-important・wrong-amount-of-approvals・permission-modes-overview など）から指され、decisions「安全の既定の勧め方」と design §9.4 が正本とするのに第一波に入らない（safety の必須11のうち8が第一波の外）。R3-1 のとおり前提を本来の意味に戻すだけだと、第一波は83ページになり、症状×原因の74の枝のうち39で対処のページが第一波にない（いまは10） | (1) 第一波を「核＋前提の閉包＋症状のページの routes（原因ごとに1つ）の閉包＋名指しの正本（default-safety-settings など）」で数える。いまの related の順で原因ごとの最初の対処を取り、症状のページの前提を basics の概念だけにすると約137ページで、対処のない2枝を除く全部の枝が埋まる（I7-2 の158は、いまの前提を残したまま症状ごとに1ページ足した数）。(2) 生成の層に「未公開のページへの前提・関連は、リンクにせず題名だけを出す」規則を足して §8.5 に書く。診断の節も routes から生成すれば同じ規則で扱える。(3) 第一波の範囲はユーザーに確かめる（§3 の1） |
| R3-3 | 中 | `symptoms.yaml` の推奨17ページの `wave: 1`、catalog/README §4.6 の2 | 推奨の症状のページ17に wave: 1 が付き、その前提から推奨8ページ（ask-for-outcomes・share-targets-and-bounds・summary-overgeneralization・check-the-metric・approval-fatigue・when-requests-are-refused・open-ended-loop-trap・ask-without-sycophancy）も第一波に入る。第一波に推奨が25ページ入り、必須の74ページはその後になる | D10「初版は必須のページで公開する」と decisions「初版の範囲」の順（第一波 → 残りの必須 → 推奨）。全部が wave: 1 なので、症状のページの優先度は意味を持たない。README §4.6 の2（核は「総論と、ほかのページの多くが前提にするページ」）にも合わない（症状のページはどれも前提にされない） | (a) 症状のページを全部必須にする（いまの前提のままだと必須は174から199）か、(b) 第一波の核を必須の症状16に絞り、推奨の17は推奨の順で足す（第一波は84）。どちらかをユーザーに確かめる（§3 の2）。README §4.6 の2の文も、決めた形に直す |
| R3-4 | 中 | design §2.3・§10.7 | 第一波と初版の大きさに目標も上限もなく、前提の書き方から出た数（125・174）がそのまま範囲になる。必須は上がる向きにだけ動いている | 第一波125（全体の35%）、必須174（48%）。kyopro-atlas の1ページ35〜45万トークンを掛けると、第一波だけで4,375万〜5,625万、初版で6,090万〜7,830万トークン（§10.7 はこれより重くなる見込みとし、工程2の全体は約680万）。必須は registry の見当の164から174になった：推奨→必須が13、任意→推奨が3、下がった例は0（必須の前提は必須の規則で上がる） | 工程7の試作で1ページの実測を出したら、第一波の上限（ページ数かトークン）と、超えたときに外す順（例：推奨の症状 → 推奨の対処 → …）を決めて design §2.3 に書く。R3-2 の数え方を道具に入れ、内訳（核・前提・routes・正本）を出す |
| R3-5 | 中 | 対処のページの signs（下の付表A）、catalog/README §4.5 の4、`check_catalog.py` の「逆引きの重複」 | 症状のページの困りごとの言い換えが、対処のページの symptom・situation の sign にある。逆引きで同じ困りごとが二か所に並び、振り分けを飛ばす読み方になる。T2 の警告は空白と記号を除いて同じ文だけを見るので、0件と出る | README §4.5 の4は「同じ文も、言い換えも」重ねないとする。12の症状のページについて、少なくとも16の組（付表A）。数え方は §1。メインの「似た組9組」より多い。ほかに、症状のページ以外どうしで、同じ文にそろえていない近い文が並ぶもの（「PC を閉じても…」が where-it-runs・cloud-sessions-and-teleport・cloud-schedules の3文）は、逆引きで似た行が3つ並ぶ | 付表A の対処の側を、goal の形か、その対処が直接の答えになる狭い場面の困りごとに直す。わざと1項目にまとめる goal は同じ文にそろえ、まとめないものは場面を書き分ける。道具には、似た度合いの上位を一覧で出すだけの形（警告にしない）を足す |
| R3-6 | 中 | `delegate.yaml`（humans-set-the-parallel-limit・parallel-with-worktrees・choosing-parallel-modes・what-not-to-delegate）と推移的な前提35件 | 前提の鎖が最大9段、祖先が最大22ページ（compare-hypotheses-in-parallel）。深さ7以上の25ページはすべて verifier-defines-problem を、18ページは five-questions-before-delegating を通る。比例則の守り（確かめる・縛るのページ）を前提で持たせた辺が鎖を伸ばしている | 比例則（design §3.1 の4）は「前提か関連」でよい。並列の本数の判断（humans-set-the-parallel-limit）は、無人で走らせる前の五つの問いを知らなくても読める。worktree の操作や並列の方式の選び方も、上限の判断を知らなくても読める。付表B の4本を関連に移すと、最も深い鎖は9→8段、深さ7以上のページは25→9になる（試算）。推移的な前提35件は「推移的に届くものは書かない」（README §4.4 の1）に反する | 付表B の4本を related に移す（4本目は前提として要るかをメインが見る）。推移的な前提35件のうち、症状のページの18件は R3-1 の直しで消える。残りの17件は related に移す |
| R3-7 | 中 | `team.yaml` の16ページの level と level_evidence | チームの16ページがすべて「仕組みにする」で、根拠はどれも「〜を仕組みにする段階」「〜を決める段階」という定義の言い直しになっている。design §3.1 の1（そのページが最初に要る段階）で付けていない | 個人のプラン選び choosing-a-plan は使う、組織のプラン選び enterprise-vs-team-plans は仕組みにする。規則の確かめ checking-ai-rules は使う、社内ガイドライン ai-usage-guidelines（前提は使う・使う・整える）は仕組みにする。ロードマップでは、AI を使い始めたチームが最初に要る決まりのページが、全部4段目に並ぶ | ページごとに「その決まりがチームに最初に要る段階」で付け直す（例：ai-usage-guidelines・enterprise-vs-team-plans は使うか整える）。または、組織のページは委任の段階を持たない扱いを design §3.1 に足し、ロードマップには載せず team の入口から引く |
| R3-8 | 中 | `app.yaml` の memory-faq・how-memory-works、`symptoms.yaml` の unexpected-memories | memory-faq（必須）は題名も節も症状そのもの（消したのに覚えている・話が混ざる）で、unexpected-memories（推奨）と同じ困りごとに答える。止め方（Pause・Reset・会話ごとのオフ・シークレットチャット）は how-memory-works の節「見る・直す・止める」とも重なる。工程3で工程4に送られた点（step3 README の I6-6） | design §4.1 の2（症状は1症状1ページ、対処の本体は各分野）。症状の入口が推奨で、対処の側が症状の題名を持つので、題名や用語索引から引くと振り分けを飛ばす | memory-faq を how-memory-works にまとめ（「消し方と止め方」「覚えた内容の棚卸し」の節）、症状の入口は unexpected-memories だけにする。unexpected-memories の優先度は、まとめた先に合わせて必須にする |
| R3-9 | 中 | `symptoms.yaml` の seems-less-capable、`models.yaml` の suspected-degradation | 2つの必須のページが、同じ「版・effort・モデル・会話（文脈）の量を安い順に確かめる」診断を持つ。sign も言い換え（付表A の1） | suspected-degradation の summary と節「安く確かめる順」、seems-less-capable の summary。suspected-degradation の notes は「対処の本体」とするが、中身は診断である。registry の notes も重なりの組に挙げていた | 安く確かめる順は seems-less-capable だけに置く。suspected-degradation は「製品の側の変更だった例」と「測って比べる」（版と effort の確かめ方の手順）に絞り、題名も対処の形（例：劣化を測って確かめる）にする |
| R3-10 | 中 | `verify.yaml` の own-generated-code、`judgment.yaml` の how-much-understanding-to-keep・learning-with-ai | own-generated-code と how-much-understanding-to-keep が同じ線引き（中核は説明できるまで確かめ、説明できないものは採らない）を持つ。sign も言い換え（「障害が起きたとき、AI が書いた部分を自分で直せない」と「障害が起きたら、自分でデバッグしなければならない部分がある」、「マージしたコードを、自分で説明できない」と learning-with-ai の「AI に書かせたコードを、自分では説明できない」） | design §4.2 は「人の側の判断（過度依存・迎合・撤退・均質化・理解）」を judgment に置く。own-generated-code の節「中核の変更のゲート」と how-much-understanding-to-keep の節「説明できないものは採らない」 | 線引きは how-much-understanding-to-keep に置く。own-generated-code は「説明させて確かめる手順」（verify の確かめ方）に絞り、how-much-understanding-to-keep を前提にする。signs は1か所にする |
| R3-11 | 中 | `cli.yaml` の init-and-first-claude-md、`extend.yaml` の what-to-put-in-claude-md・claude-md-length | /init のページの節「叩き台をどう削るか」が、extend の2ページと同じ判断（推測できる説明を削り、推測できない約束と落とし穴を残す）を持つ。CLAUDE.md の書き方が3ページに散る | design §4.2「CLAUDE.md・rules・skills…（文脈と指示の置き場所）は extend、cli・enforce からリンク」。claude-md-length の related が `init-and-first-claude-md#prune` を指していて、削り方の本体が cli にある形になっている | 削り方は claude-md-length に置き、init-and-first-claude-md は /init の操作と「叩き台から始める」流れだけにして claude-md-length を指す。または what-to-put-in-claude-md の節（/init から始める）にまとめる |
| R3-12 | 中 | `symptoms.yaml` の deleted-something-important#recover・secrets-exposed#first-response・refused-or-blocked#by-surface | 症状のページが対処の本体の一部を持ち、対処のページと重なる。復旧の手順は cli の recover-lost-work に、鍵の無効化は safety の protecting-secrets の節「貼ってしまったとき」に、面ごとの表示は safety の when-requests-are-refused の節「面ごとの仕組み」にもある | design §4.1 の2（対処の本体は各分野のページ）。面ごとの表示の文は変わりやすく、二か所に持つと点検で食い違う | 消された直後・漏れた直後の初動は症状のページが持つ、という例外を design §4.1 の2に書き、対処のページの同じ節は外して症状のページを指す（一か所にする）。面ごとの表示は when-requests-are-refused に寄せ、症状のページは切り分けだけにする |
| R3-13 | 中 | `registry.yaml` の ledger、`changes.yaml` の change-timeline-2026 の notes、design §9.1 | 台帳と名称の表（data/facts.yml）の分担が決まっていない。改名や画面の変更の行が台帳にあり、名称の表と同じ事実（旧名・今の名前・変わった時期）を二か所に持つ。台帳の列（どの原理の回避策だったか・かつてなぜ正しかったか）も、改名の行には当たらない | 台帳37行のうち routines-name・slash-cost-and-stats・fork-to-branch・code-on-the-web-remote・customize-tabs・max-5x-or-20x は名前か画面の変更。change-timeline-2026 の notes は「プランの改名（旧 Max 20x から Ultra）は台帳ではなく数値ファイルの名称の項目に持つ」と書くが、台帳には max-5x-or-20x があり choosing-a-plan が指している（research/22 §3.4 は足す候補に挙げていた） | 名前と画面の変更は名称の表を正にし、台帳の行は「今どうするか」が変わったものに限る。改名に伴って勧めも変わる行は、名称の id を指して時期を名称の表から引く。土台作りの前に design §9.1 に書く |
| R3-14 | 軽 | `models.yaml` の 1m-context・opusplan、`delegate.yaml` の agent-teams-experimental | id に変わりやすい値（窓の大きさ・成熟度・モデルの系統名を含む別名）が入っている | design §5.3（id は骨格の後は変えない）、§6.1 の5（名称・成熟度は数値ファイル）。agent-teams-experimental の notes は「題名から成熟度を外した」とするが、id に残っている | 骨格の前に、wide-context-window・agent-teams・models-by-role のような id にする |
| R3-15 | 軽 | `delegate.yaml` の cloud-schedules、`team.yaml` の enterprise-vs-team-plans、`models.yaml` の thinking-keywords | 題名に旧名「（旧 routines）」とプラン名「Team と Enterprise」、summary に ultrathink の使い方（「1ターンだけなら ultrathink を使う」）がある | design §5.3・§6.1 の5。プランの名前は 2026-10-30 に変わった例がある（decisions 工程2）。ultrathink の効く版と面は数値ファイルの項目（design §9.1 の models#2） | 旧名は aliases へ。プラン名の題名は「組織で使うプランの選び方」などにし、名前は aliases と生成の表に置く。summary は「1ターンだけ深く考えさせる手段もある」の形にする |
| R3-16 | 軽 | `basics.yaml` の lost-in-the-middle、`team.yaml` の ai-amplifies-organizations | 研究の結果の紹介が本体で、独自の判断がない | design §4.1 の5。lost-in-the-middle の notes は「2023 年のモデルの結果で、2025 年の実験では位置の差が目立たなかった」とし、prompting の long-context-first も前提にしない。節はない。ai-amplifies-organizations の notes は review-bottlenecks・paved-roads と重なるとする。節はない | lost-in-the-middle は context-rot の節に、ai-amplifies-organizations は paved-roads か review-bottlenecks の節にする（merged に入れる） |
| R3-17 | 軽 | `cli.yaml` の completion-notifications、`recipes.yaml` の add-tests、`team.yaml` の curb-sycophancy-and-overtrust、`prompting.yaml` の does-double-check-work | 要点がほかのページの節と同じで、1節で足りる | completion-notifications は hook-recipes の節「終わったら知らせる」と同じ。add-tests（節なし）の要点「わざと壊したコードで落ちるか」は pitfalls-of-ai-written-tests の節「テストの強さを確かめる」と test-the-verifier と同じ。curb-sycophancy-and-overtrust（節なし）の「AI のレビュー済みを根拠に数えない」は independent-review・risk-tiered-approval・agreement-is-not-evidence・automated-pr-review・create-and-review-prs の5ページにもある。does-double-check-work の答え（確かめる手段を渡す）は evidence-not-reports と同じ | 試作の前に、各ページの独自の判断を notes に1行で書けるかを確かめ、書けないものは節にまとめる。「AI の承認を人の承認に数えない」は risk-tiered-approval を持ち主にし、ほかは1行で指す |
| R3-18 | 軽 | `contest.yaml` の competition-rules、`safety.yaml` の checking-ai-rules | competition-rules の節「規則が割れる理由」「文言がないことは許可ではない」が、checking-ai-rules の「なぜ規則が割れるか（三つの型）」「文言がないとき・分からないとき」と同じ | design §4.2（一般の類型と確認表は safety、contest は早見で safety の確認表を前提にする） | competition-rules から2つの節を外し、前提の checking-ai-rules を指す。summary の「割れる理由」も外す |
| R3-19 | 軽 | `enforce.yaml` の managed-settings-enforcement、`team.yaml` の org-managed-settings-and-mcp | どちらの summary も「利用者（個人）の設定より優先して効かせる」で、題名の「管理設定」も同じ。どちらも任意 | design §4.2（managed settings の使い方は enforce）。registry の notes も重なりの組に挙げていた | team の側は「配る経路とグループの分け方・MCP の許可」に絞り、題名から「（管理設定）」を外す。または enforce にまとめる |
| R3-20 | 軽 | `symptoms.yaml` の refused-or-blocked | aliases の「分類器に止められた」は、auto モードの分類器に操作を止められた場合とも読めるが、このページは what-auto-mode-stops#when-blocked と lock-side-effects を指さない（keeps-stopping だけが指す）。逆引きで「止められた」と引いた人が、利用ポリシーのページに着く | keeps-stopping の notes（auto モードの分類器に止められたときの見直しは what-auto-mode-stops#when-blocked） | related に what-auto-mode-stops#when-blocked と lock-side-effects を足し、診断の最初に「何に止められたか（利用ポリシー・auto モード・フック・権限ルール）」を置く。aliases は「利用ポリシーで止められた」に寄せる |
| R3-21 | 軽 | `prompting.yaml`（concept 21）・`context.yaml`（concept 10）、design §2.2・§6.3・§10.1 の工程7 | 頼み方の技法（例を見せる・XML タグで区切る など）も concept で、design §2.2 の concept（なぜそうなるか）と §6.3 の流れ（なぜそうなるか〔比喩付きの図〕）に合わない。工程7の試作は型ごとに1ページなので、basics の concept を試作しても、技法のページの書き方は確かめられない | 技法のページの summary の多くが「〜すると〜が減る」の形（R3-22） | 試作に prompting の concept を1ページ足す。または §2.2 の concept の定義に「技法（どう頼むと何が変わり、なぜか）」を足し、§6.3 に目安の流れを足す |
| R3-22 | 軽 | 48ページの summary（prompting 19・cli 10・context 6・japanese 6・recipes 6・start 1） | 1文目が「何ができるか・何が分かるか」の形でなく、助言そのもの（「〜すると〜が減る」）か命令（「〜を渡す」）。多くはそれで用が足りるが、suggest-or-do（「動きは変わる」だけ）・asking-for-reasoning（注意だけ）・before-after-prompts（「示す」でページの説明）・settings-layers（「どれが勝つかが決まる」）は、読者が何をすればよいかが分からない | design §5.3（1文目は何ができるか）。数え方：1文目の末尾が「できる・分かる・選べる」などの形かを正規表現で見た（見落としがありうる） | §5.3 を「何ができるか、または答えそのもの」に広げ、上の4ページは書き直す |
| R3-23 | 軽 | design §2.2 の最後の項、`start.yaml`（reverse-index・term-index・roadmap・knowledge-map）、`changes.yaml`・`cli.yaml` の ledger のページ | §2.2 は生成のページ（逆引き・用語索引・知識マップ・ロードマップの列・台帳の表）は型を持たないとするが、目次ではこれらに hub・ledger の型がある | registry の notes「型は仮に hub にした」。design §2.2 の表の ledger は「データから生成する表」 | §2.2 を「本体を生成するページも hub・ledger の型を持ち、生成の部分は目印で作る」に直す |
| R3-24 | 軽 | `prompting.yaml` の refine-in-conversation、`context.yaml` の rewind-dont-correct | refine-in-conversation の節「訂正を重ねるより依頼を直す」が、rewind-dont-correct の本体（訂正を重ねるより、前のメッセージを直して送り直すか巻き戻す）と同じ。sign も近い（「訂正を重ねるほど返事がこじれていく」と「「そうじゃない」と何度返しても方向が直らない」） | design §4.1 の1（独自の「なぜ」か判断を持つ単位） | refine-in-conversation の節は1行にして rewind-dont-correct を指し、sign は片方に置く |
| R3-25 | 軽 | cli の usage-context-statusline、context の inspect-context、cost の what-uses-up-limits、eval の insights-and-usage-review | /usage の内訳の読み方が3ページ（cli・cost・eval）、/context の内訳の読み方が2ページ（cli・context）にある。画面の項目は変わりやすい | 各ページの節（「三つの道具で見えるもの」「内訳の読み方」「自分の場合を確かめる（/usage の内訳など）」「/usage の内訳から削るものを選ぶ」） | 内訳の読み方の持ち主を1つに決め（/usage は what-uses-up-limits、/context は inspect-context）、ほかのページは目的の判断だけにして指す |

### 付表A：症状のページの sign と、対処のページの sign の言い換え（R3-5）

左が症状のページ、右が対処のページ。

1. seems-less-capable「更新の後から答えが雑になった気がする」— suspected-degradation（situation）「更新の後から、結果が変わった気がする」
2. caves-when-pushed「Claude も賛成したのに計画が失敗した」— agreement-is-not-evidence「Claude も賛成したのに、方針が間違っていた」
3. misses-broken-evaluation「手元のスコアは上がるのに本番で通用しない」— check-the-metric「手元のスコアは良いのに、本当の目的では悪い」
4. 同上 — verifier-three-conditions「手元の評価では勝つのに、本番では効かない」
5. 同上 — open-ended-loop-trap「長く回したのに、手元のスコアだけ上がって本番では良くならない」
6. wont-rethink-approach「少し試しただけで「これ以上は無理です」と言われる」— share-targets-and-bounds「少し改善しただけで「これ以上は難しい」と言う」
7. 同上 — measure-the-upper-bound「「これ以上は改善できません」と言われた」
8. replies-in-english の3文 — keep-replies-in-japanese の「日本語で話しているのに、途中から返事が英語になる」「日本語の設定や指示をしても、英語に戻る」「ツールを使った直後の一言だけ英語で出る」
9. repeating-the-same-explanation「同じ手順書を何度も貼っている」— skills-in-the-app「同じ手順の説明を会話のたびに貼っている」
10. hits-limits-quickly「すぐ上限に当たる」— what-uses-up-limits「少し使っただけなのに上限に当たる」
11. hits-limits-quickly「「会話が長すぎる」と表示されて続けられない」— long-chat-limits「会話が長くなり、それ以上続けられなくなった」
12. plausible-falsehoods「存在しない論文や URL を挙げられる」— allow-i-dont-know「存在しない文献や数字を、それらしく出してくる」
13. doesnt-know-latest「古い書き方のコードや設定を出してくる」— knowledge-cutoff「古い版の書き方を、今の方法として勧めてくる」
14. does-more-than-asked「小さな修正を頼んだのに周りまで書き換えられる」— state-the-scope「小さな修正のつもりが、大きな書き換えになった」
15. forgets-in-long-chats「最初に伝えた前提を途中から忘れる」— promises-after-compaction「最初に伝えた禁止事項を、途中から守らなくなった」（圧縮の場面と書いていないので、圧縮でない人もこのページに着く）
16. insists-on-mistakes「説明と実際の履歴が食い違っている」— unfaithful-reasoning「説明された理由と、実際の結果が食い違う」（境目）

目で見て迷ったもの（数に入れていない）：plausible-falsehoods「確かめると数字や引用が原文と違っている」と checking-citations・research-and-reports の出典の不一致の sign、summary-overstates-source と fact-checking「要約に、原文にない言い切りが混ざっている」、instructions-ignored と when-to-lock「CLAUDE.md に「〜しない」と書いたのに破られる」（README §4.5 の4の例の「より狭い場面」に当たる）。

### 付表B：関連に移す候補の前提の辺（R3-6）

1. humans-set-the-parallel-limit の前提 five-questions-before-delegating（並列の本数の判断に、無人の実行の五つの問いは要らない）
2. parallel-with-worktrees の前提 humans-set-the-parallel-limit（worktree の操作の前提ではなく守り）
3. choosing-parallel-modes の前提 humans-set-the-parallel-limit（同上）
4. what-not-to-delegate の前提 verifier-defines-problem（「機械的に確かめられるか」の軸は前提の説明なしでも読めるかを、メインが見る）

1〜3だけで深さ7以上のページは25→17、4まで移すと25→9。さらに define-done の前提 agent-loop を外すと最長7段・1ページになるが、これは「なぜ完了を定義するか」の本当の前提なので残してよい。

## 3. ユーザーに判断してもらうべき点

1. **第一波の範囲（D10 の「核から前提でたどれるページ」）**：いまの125ページは、症状のページが対処のページを前提に置いたこと（R3-1）で成り立っている。前提を本来の意味に戻すと83ページで、症状×原因の74の枝のうち39で対処が未公開になる。案は「症状のページの振り分け先（原因ごとに1つ）と、名指しの正本（安全の既定など）も第一波に入れる」で、約137ページになる（R3-2）。症状のページの関連をすべて入れると265ページ。あわせて、第一波の公開のときに未公開のページへのリンクを題名だけで見せる（リンクにしない）ことを確かめる
2. **推奨の症状のページを第一波に入れるか（D10 の「初版は必須」との関係）**：(a) 症状のページを全部必須にする（必須は約199）、(b) 第一波の核を必須の症状16に絞り、推奨の17は推奨の順で足す（第一波は約84。R3-2 の振り分け先を足すと増える）、(c) 核の分野（eval・judgment・japanese）に結びつく推奨の症状（misses-broken-evaluation・caves-when-pushed・inconsistent-japanese-style など）だけ必須にする。R3-3

## 4. 直さなくてよいと判断した論点

- **入ってくる道**：start の外で、前提と関連で指されるのが1ページ以下のページはない
- **症状の振り分けの網**：症状×原因の74の枝のうち72に、その原因を受け持つ対処のページがある（抜けは wont-rethink-approach の「散らかっている」と blames-the-tools の「見えていない」だけ。執筆で足りる）
- **症状のページの signs**：105文とも読者の言葉で、機能名を答えとして書いていない。症状のページどうしで同じ困りごとはない
- **関連の並び**：抜き取りの11ページ（hooks-basics・permission-rules・define-done・when-to-lock・tokens など）は近い順になっている
- **台帳の逆リンク**：37行すべてが1ページ以上の outdated_advice から指される。存在しない id もない
- **比例則の警告4件**（agents-md・feature-to-api-mapping・prompt-caching-in-practice・ideate-independently）：どれも notes に「任せる幅を広げない」理由がある。第一波の中でも、任せる幅を広げるページの守りは1件（stuck-in-a-check-loop）を除いて第一波にある
- **大きすぎるページ**：hub・guide を除くと、節が6以上は7ページ（evaluators-by-format 8、measure-changes 7、keep-replies-in-japanese 7、prompt-patterns・test-the-verifier・decide-when-to-quit・competition-day-operations 6）で、どれも1つの問いに答えている
- **「使う」の数**：35ページ（約10%）で少ない
- **change-timeline-2026 の id の年**：年ごとのページにする設計（notes）なので直さない
- **症状のページ以外どうしの同じ文13組**：統合の担当が逆引きで1項目に並べるためにそろえたもの（tool-T2 §1.4）。逆引きの節「同じ言葉が複数のページに当たるとき」の手書きの注記は要る
- **題名の表記**：M1 の表どおり。「文脈」と「コンテキスト」の混在は用語集で決める範囲
- **handoff-documents と progress-files**：一度きりの引き継ぎと、続く作業の状態で分けられている
- **半角と全角の間の空白**：題名と summary で3件（「4点」「1ターン」「1回」）だけで、textlint で拾える

## 5. 確かめていないこと

- 本文がないので、ページの実際の長さ・節の厚さは見ていない。薄い・大きいの判断は sections・summary・notes からの見立て
- 言い換えの組は、2字の重なりと difflib の比で上位を出し、目で選んだ。比の低い言い換え（言葉の違う同じ困りごと）は見落としがありうる
- 関連が近い順かは11ページの抜き取りだけ。level_evidence は症状・team・extend・「使う」のページを全部読み、ほかの分野は抜き取り
- 費用の見込み（R3-4）は kyopro-atlas の1ページ35〜45万トークンを掛けただけで、検証と直しの回数は入れていない
- R3-2 の約137ページは、いまの related の順で原因ごとに最初の対処を取った試算。振り分け先を選び直せば変わる
- research preview・experimental の判定は notes の記述に頼った（features.yaml に成熟度の値はない）
- 公式の日本語版の訳語（「背景セッション」など）は確かめていない（Web を開かない）
- `planning/batches/step3/open-issues.md` は全部は読んでいない。catalog-C1〜C11・integrate-I1〜I6 の報告も読んでいない（C12・I7・T2 は前提と第一波の判断の箇所を読んだ）
- ほかの見直しの担当（R1・R2・R4）の報告は見ていない。R1 の欠けの指摘、R2 の D10 の解釈、R4 の使用量の見込みと重なる点がありうる
