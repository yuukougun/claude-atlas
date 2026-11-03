# 工程4 設計の見直し：R1 読者の立場

- 担当：R1（観点は読者の立場。brief-review.md §4）
- 日付：2026-11-04
- 対象：planning/design.md（第1版）、planning/catalog/（第1版、23分野・361ページ）

## 1. 見た範囲と方法

### 読んだもの

- 全部読んだ：brief-review.md、step4/README.md、requirements.md、decisions.md、design.md、catalog/README.md、schema/site.yml
- 道具で抜き出して読んだ：catalog の23ファイルの全361ページの title・aliases・signs・summary・prerequisites・related・sections（start と symptoms は全ページを通して読んだ。ほかの分野は課題に関わるページの項目と、一部の notes）
- 材料：research/00 §4（逆引き73項目）と §3 の分野13・14・17、research/03 の Q6〜Q9、research/04 の Q2〜Q6
- `python3 tools/check_catalog.py --stats`（エラー0、警告4、第一波125）

### 数えた方法

作業用の一時の道具（リポジトリの外に置いた）で数えた。

- 第一波：wave: 1 のページから prerequisites をたどって閉じた集合（check_catalog.py の first_wave と同じ定義で、同じ125ページになった）
- 前提の深さ：prerequisites の最長の段数。祖先：たどって届くページの数
- signs の重なり：記号を除いた文の完全一致、文字の2-gram の Jaccard（0.33以上と0.5以上）、語（記事・本番・スコア・上限・完了・守られ・英語・席を外 など）で抜いて目で確かめた。言い換えは拾い漏れがあるので、重なりの数は下限である
- 逆引き73項目：00 §4 の表から抜き、同じ文か、2-gram が最も近い sign の行き先を見た（4項目は手で行き先を決めた）
- 課題：読者が打ちそうな語で、題名・別名・signs・summary を部分一致で引いた

### 課題と引いた結果（34件。00 §4 から15件、自分でつくったもの19件）

段階は委任の段階、面は app（アプリ）・CC（Claude Code）・API。「前提」は直接の前提の数／最長の段数。「波」は第一波に入るか（W）。

| # | 出どころ | 場面・段階・面 | 読者の言葉 | 着くページ（入口） | summary で足りるか | 前提 | 結果 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 00 §4 | 開発・整える・CC | 同じバグの修正を何度も失敗する | going-in-circles（同じ文の sign）W | 足りる | 3／4 | 着く。第一波では振り分け先12件のうち5件が未公開 |
| 2 | 00 §4 | 調べもの・使う・app | 長い PDF の後半の図について答えられない | skipped-later-pages（同じ文）W | 足りる | 1／1 | 着く。第一波では振り分け先7件のうち5件が未公開 |
| 3 | 00 §4 | 文章・整える・app | です・ますとだ・であるが混ざる | inconsistent-japanese-style（同じ文）W | 足りる | 3／3 | 着く |
| 4 | 00 §4 | 開発・任せる・CC | 長い作業を明日も続けたい | handoff-documents・progress-files・resume-and-branch（3ページに同じ文） | 3つとも見分けられる | 1／4〜5 | 迷う（同じ行が3つ） |
| 5 | 00 §4 | 開発・任せる・CC | .env や migrations を絶対に触らせたくない | permission-rules・block-with-exit-2（2ページに同じ文）W | 足りる | 1／2 | 迷うが、どちらも答えになる |
| 6 | 00 §4 | 開発・任せる・CC | テストが通るまで終わらせたくない | verification-ladder（W）・stop-hooks（2ページに同じ文）、goal-until-done にも同じ意味の sign | 足りる | 2／3、goal は 2／7 | 迷う（3ページ） |
| 7 | 00 §4 | 開発・任せる・CC | CLAUDE.md を変えて良くなったか知りたい | measure-changes（同じ文）W | 足りる | 3／3 | 着く |
| 8 | 00 §4 | 開発・任せる・CC | 知らない人のリポジトリを開きたい | before-opening-unknown-repos（同じ文） | 足りる | 2／3 | 着く。必須だが第一波の外 |
| 9 | 00 §4 | 開発・使う・全 | /clear すれば上限は戻るのか | how-usage-limits-work（近い文）W | summary が答えている（戻らない） | 0／0 | 着く |
| 10 | 00 §4 | 開発・回す・CC と app | 席を外している間も進めてほしい | 同じ文が3ページ（tasks-and-schedules-in-the-app・five-questions-before-delegating・goal-until-done）、言い換えが5ページ | 見分けにくい | goal は 2／7 | 迷う（8ページ。受け皿なし） |
| 11 | 00 §4 | 開発・仕組みにする・API | 自分のアプリに Claude を組み込みたい | sdk-comparison（同じ文） | 足りる | 2／1 | 着く。第一波の外 |
| 12 | 00 §4 | チームと学習・使う・全 | 会社や学校で使ってよいか確かめたい | checking-ai-rules（同じ文） | 足りる | 0／0 | 着く。必須だが第一波の外 |
| 13 | 00 §4 | 開発・整える・CC | 古い記事のやり方が通じない | doesnt-know-latest（同じ文）W、ほか6ページに同じ型 | 足りない（Claude の知識の締め切りの話で、読者の資料の古さに答えない） | 1／1 | 迷う |
| 14 | 00 §4 | 開発・使う・全 | すぐ上限に当たる | hits-limits-quickly W | 足りる | 2／2 | 着くが、第一波では本体の what-uses-up-limits・saving-priorities（ともに必須）が未公開 |
| 15 | 00 §4 | 開発・任せる・CC | CLAUDE.md に書いたのに守られない | instructions-ignored W | 足りる | 3／4 | 着くが、第一波では振り分け先18件のうち12件が未公開 |
| 16 | 自（03 F6） | 開発・整える・CC | uv を使わず pip で入れてしまう（決めたコマンドを使わない） | 「uv」「pip」で0件。「コマンド」で what-to-put-in-claude-md の「プロジェクト固有のコマンドや落とし穴を…」 | 一部 | 2／1 | 着きにくい |
| 17 | 自（03 F4） | 開発・整える・CC | 古い関数を消さずに新しい版を横に足していく | 「死んだ」「消さず」で0件。does-more-than-asked に近い | 一部 | 1／3 | 着きにくい |
| 18 | 自（03 F5） | 開発・任せる・CC | 作業フォルダに一時スクリプトやテスト用 DB が残る | 「一時」「散らか」「残骸」で当たらない | — | — | 着けない |
| 19 | 自 | 開発・任せる・CC | つないだ MCP のツールが出てこない | connecting-mcp（「MCP」の別名） | 足りない（不調の切り分けがない） | 1／1 | 着くが用が足りない |
| 20 | 自 | 開発・仕組みにする・CC | 書いたフックが動かない | hooks-basics（「設定したフックが動いていないように見える」）W | 足りる | 2／4 | 着く |
| 21 | 自 | 開発・任せる・CC | settings.json に書いた設定が効かない | settings-layers（「設定を書いたのに効いていない」） | 足りる | 0／0 | 着く |
| 22 | 自 | チーム・回す・CC | PR に自動で AI のレビューを付けたい | automated-pr-review（任意）、github-actions-with-claude | 足りる | gha は 2／8（祖先14） | 着くが前提の鎖が長く、初版に入らないことがある |
| 23 | 自 | 開発・仕組みにする・API | API が 429 や 529 を返す | 「429」「レート」「rate」「overloaded」で0件 | — | — | 着けない |
| 24 | 自 | 開発・仕組みにする・API | JSON で返すよう頼んでも形が崩れる | structured-outputs-basics（同じ意味の sign） | 足りる | 1／1 | 着く |
| 25 | 自 | データ分析・整える・CC と app | CSV を集計させたら日本語の列が文字化け | character-encodings | 足りる | 0／0 | 着く |
| 26 | 自 | 開発とチーム・任せる・全 | AI が書いたコードを製品や OSS に入れてよいか | 「ライセンス」で ai-and-sources（この辞典自身のライセンス）だけ | 合わない | — | 違うページに着く |
| 27 | 自 | 開発・回す・CC | devcontainer や Docker の中で無人で走らせたい | 「Docker」「devcontainer」「コンテナ」で0件（where-bypass-is-ok に雛形はある） | — | 2／4 | 着きにくい |
| 28 | 自 | 学習・整える・全 | 新しい技術を Claude で覚えたいが身につかない | learning-with-ai（別名「AI で学ぶと身につかない」）W | 足りる | 1／3 | 着く |
| 29 | 自 | コンテスト・任せる・CC | AHC のローカルテスタを AI に作らせたい | evaluators-by-format | 足りる | 1／6 | 着く（第一波の外は決定どおり） |
| 30 | 自（design §1.2 の例） | チーム・仕組みにする・CC | チームに Claude Code を導入したい | rolling-out-to-teams（任意）だけ | 足りる | 2／4 | 初版（必須）では着けない |
| 31 | 自 | データ分析とコンテスト・任せる・CC | 手元のスコアは上がったのに本番で悪い | 6ページに同じ型 | 症状のページの題名が Claude の側の言い方 | 3／6 | 迷う |
| 32 | 00 §4 と自 | 開発・整える・CC | ツールの結果を読んだ後の一言だけ英語になる | replies-in-english と keep-replies-in-japanese の両方に同じ困りごと W | 足りる | 2／3 | 迷う（2行） |
| 33 | 自 | 開発・整える・app と CC | 設計や技術の選び方を壁打ちしたい | 「設計」「相談」「壁打ち」で当たらない。近いのは ask-for-options | 一部 | 1／3 | 着きにくい |
| 34 | 自 | 開発・任せる・CC | AI が書いたコードに脆弱性がないか見させたい | 「セキュリティ」「脆弱」で当たらない（/security-review は automated-pr-review の別名だけ） | — | — | 着きにくい |

まとめ：34件のうち、迷わず着くのは12件（うち3件は第一波の外）、着くが迷う・前提が長い・第一波で先が切れるのが12件、着きにくい・着けない・違うページに着く・用が足りない・初版では着けないのが10件。signs は読者の言葉でよく書けていて（907件のうち、この辞典の独自の用語を含むのは1件）、着けない原因は、言葉の不足よりも、第一波の切れ目・同じ困りごとの重なり・入口の欠けにある。

## 2. 指摘の一覧

| 番号 | 重さ | 場所 | 問題 | 根拠 | 直し方の案 |
| --- | --- | --- | --- | --- | --- |
| R1-01 | 重大 | design §2.3・§8.5・§8.6、catalog/README §4.6、symptoms の全ページ | 第一波で公開する症状のページから、振り分け先の過半に道がない。第一波は wave: 1 と前提でたどれる125ページで、stub はビルドから外し、公開するページから stub へのリンクは検査で止める（§8.5）。症状のページ33本が指す対処のページ（前提と関連の合計378件。症状と start を除く）のうち213件（56%）が第一波の外である。例：hits-limits-quickly の本体の what-uses-up-limits・saving-priorities（ともに必須）、instructions-ignored の claude-md-length・what-to-put-in-claude-md・path-scoped-rules・hook-recipes、repeating-the-same-explanation は10件のうち8件が外。第一波のページ全体でも related 1330件のうち648件（49%）が外で、外のページで多く指されるのは hook-recipes（15）・independent-review（12）・default-safety-settings（10。安全の既定の正本）・tidy-the-desk（10）。全体地図の product-map は12件のうち9件が外。逆引き73項目のうち28項目（行き先に必須のページを含むものは18項目）は、第一波では行き先に着けない。公開するページは「振り分けが本体」なのに、第一波では振り分けられず、後の波で33本を書き直すことになる | D10・decisions「初版の範囲」（第一波を書いて公開する）、decisions「公開する段階」（stub は公開しない）、design §1.3 の1（3回のクリック以内）・§4.1 の2。設計書に、公開したページから未公開のページへの道の扱いはない（「準備中」「未公開」で0件。§13 E で準備中の印での公開は採らなかった）。数え方は §1 | 土台作りの道具（§8.4〜§8.6）を作る前に、次のどちらかを決める。(1) 第一波を「核と、その前提と、症状のページの主な振り分け先（とその前提）」と定義し直す。症状のページが related に持つ必須のページを足すと180ページ（+55）、各症状のページの近い3件を足すと192ページ（+67）になる。(2) 第一波を今のままにし、公開するページから未公開のページを指すときは、道具が題名を「準備中」の平文で出し、そのページを公開したら自動でリンクにする決まりを §8.5 に足す（本文のリンクも同じ形で書かせる）。(1) は D10 の文言を変えるのでユーザーの判断（§3） |
| R1-02 | 中 | symptoms.yaml の冒頭の注記と、症状のページの prerequisites | 症状のページの前提（68件）に、対処の本体が少なくとも23件入っている（型が feature 11・recipe 7・judgment 4・comparison 1 のもの。concept の45件にも対処のページがある）。担当は冒頭の注記で「prerequisites には、原因ごとの対処のうち中心になるページを」と書いている。例：replies-in-english の前提が keep-replies-in-japanese、inconsistent-japanese-style の前提が consistent-politeness と consistent-notation、secrets-exposed の前提が protecting-secrets、stuck-in-a-check-loop の前提が goal-until-done（/goal を使っていない人にも起きる症状なのに、段階が「仕組みにする」に上がり、前提の鎖が8段・祖先18ページになる）。冒頭の要点の「前提」は読者に「先に読むもの」として見えるので、答えを先に読めと言うことになり、振り分けが逆になる | catalog/README §4.4 の1（前提は「これを知らないと読めない」もの）、design §4.1 の2・§6.4（要点に「前提」）・§3.1 の規則3（前提より下の段にしない） | 症状のページの主な行き先は、前提と別に持つ（例：任意のキー `routes`、または related の先頭の数件を主な行き先と決める）。前提は診断に要る概念のページだけにする。R1-01 の(1)を取るなら、第一波を routes まで広げれば、第一波の中身を保ったまま前提の意味を戻せる |
| R1-03 | 中 | design §7（逆引き辞典）、start.yaml の reverse-index | 逆引き辞典の、節の中の分け方・並び・1行に出すもの・同じ文の束ね方が決まっていない。signs は907件（困りごと386・やりたいこと383・状況138）で、00 §4 の73項目の約12倍ある。節は型の三つだけなので、困りごとの節に386行が入る（第一波でも195行）。MkDocs の検索は見出しの節の単位で当たるので、1節に数百行あると、検索からその行に着けない（確かめていない）。3回のクリックの成功の条件は工程10でしか試さない | design §1.2・§1.3 の1、requirements §1 の核1（症状から引く索引）、00 §4（6つの章立てと原因の列を手本にしている。reverse-index の materials） | (1) 困りごとの節は症状辞典の9章で分け、対処のページの困りごとは振り分け先の症状のページの章に入れる（分野から章への対応表を作る層に持つか、sign に任意の group を足す）。(2) やりたいことの節は場面か面で分ける。(3) 同じ文は1行に束ね、行き先に面や型の短い印を付ける（R1-06）。(4) 試作（工程7）で逆引きを生成し、この報告の課題で引いて確かめる（工程10まで待たない） |
| R1-04 | 中 | catalog/README §4.5 の4、design §8.6（逆引きの重複の警告）、症状のページと対処のページの signs | 症状のページが振り分ける困りごとを、対処のページにも言い換えで重ねている。規則は README §4.5 の4 にあるが、§8.6 の検査は同じ文しか見ないので、言い換えはすり抜ける（今の同じ文の重複13組には症状のページが一つも入っていないので、検査は通る）。拾えただけで12本の症状のページに当たる：replies-in-english と keep-replies-in-japanese（「ツールの結果の後の一言だけ英語」「途中から英語」、別名「英語に戻る」も両方）、seems-less-capable と suspected-degradation（「更新の後から…気がする」、別名「性能が落ちた」）・felt-vs-measured（「前より賢くなくなった気がする」）、hits-limits-quickly と what-uses-up-limits（「少し使っただけなのに上限に当たる」）、claims-done-but-isnt と define-done、caves-when-pushed と agreement-is-not-evidence（「Claude も賛成したのに…」）、wont-rethink-approach と share-targets-and-bounds（「これ以上は無理／難しい」）、unexpected-memories と memory-faq（題名が症状の文そのもの）、wrong-amount-of-approvals と approval-fatigue、forgets-in-long-chats と promises-after-compaction、parallel-fatigue と review-bottlenecks（「レビューが追いつかない」）、ほかに R1-05・R1-07 の束 | README §4.5 の4（「同じ文も、言い換えも」重ねない。「逆引きで同じ困りごとが二か所に出ると、振り分けを飛ばす読み方になる」）。数え方は §1（下限の数） | 対処のページの重なった sign を、その対処に固有の狭い場面か goal に書き換える（例：keep-replies-in-japanese は「language を設定しても英語に戻る」）。§8.6 の検査を、2-gram の重なりなどで言い換えも警告する形にする（警告どまり。最後は人が見る） |
| R1-05 | 中 | symptoms/doesnt-know-latest、changes の3ページ、cli/ask-claude-code・command-cheatsheet、start/term-index | 「古い記事のやり方が通じない」が、一般的な言い方だけで7ページに散り、受け皿が答えていない。統合で doesnt-know-latest を入口に決めた（changes.yaml の notes の M2）が、その題名と summary は Claude の知識の締め切りの話（「最近の出来事や新しい版について間違える原因を知識の締め切りから切り分け」）で、読者の読んだ記事・本・自分の設定が古い場合に答えない。同じ型の sign：checking-for-updates「記事の手順どおりにしても手元では動かない」、ask-claude-code「記事に書かれたやり方が、手元の版で動かない」、command-cheatsheet「古い記事に出てくるコマンドが、手元で動かない」、outdated-advice-ledger「前は効いた書き方や設定が効かなくなった」、term-index「古い記事に出てくる機能の名前が…見当たらない」、dating-information「記事によって書いてあることが食い違う」 | requirements §1 の核4（古くなった助言の台帳）、research/04 Q6 の読者の不満の1つ目（変化が速く Tips がすぐ古くなる）、README §4.5 の4。数え方：signs を「記事」「古い」「前は」「手元」で抜いた | (a) 読者の側の古さを受ける症状のページを立てる（例「記事や前のやり方が通じない」。台帳・旧名の対応・自分で確かめる方法へ振り分ける）か、(b) doesnt-know-latest の題名と summary を「Claude が古い／読んだ資料が古い」の二つの枝にする。どちらでも、ほかの6ページの一般的な sign は、コマンド名・機能名・GitHub Action など狭い場面か goal に書き換える |
| R1-06 | 中 | 対処のページどうしの同じ文の sign（13組・28件）と、受け皿のない束 | 同じ文の sign が2〜3ページにある。「長い作業を明日も続けたい」（handoff-documents・progress-files・resume-and-branch）、「席を外している間も進めてほしい」（tasks-and-schedules-in-the-app・five-questions-before-delegating・goal-until-done。言い換えを含めると where-it-runs・cloud-sessions-and-teleport・cloud-schedules・control-from-phone・completion-notifications まで8ページ）、「テストが通るまで終わらせたくない」（verification-ladder・stop-hooks。goal-until-done にも同じ意味の goal）、「チームで同じ設定を使いたい」（plugins-and-marketplaces・share-team-settings）、「auto モードに任せて大丈夫か」（what-auto-mode-stops・sandboxing）など。言い換えでは「夜間や CI で、人が見ていない間に Claude を動かす」が checking-unattended-runs と where-bypass-is-ok に、「強調しても守られない」が emphasis-words・claude-md-length・request-vs-lock にある。逆引きでは同じ行が並び、読者は題名だけで選ぶことになる | 00 §4 は1行に行き先を「／」で並べていた（1行で複数の行き先）。design §8.6 の重複の警告は症状のページの sign だけが対象。数え方：記号を除いた文の完全一致 | (1) 逆引きの生成で同じ文を1行に束ね、行き先に面や型の短い印（アプリ／Claude Code、考え方／手順）を付ける。(2) 「席を外している間も」は比較のページ（where-it-runs か choosing-automation）を受け皿にし、ほかのページは面や方式に固有の goal にする。(3) 「強調しても守られない」は一つのページに寄せる |
| R1-07 | 中 | eval・delegate・contest の5ページと symptoms/misses-broken-evaluation | 「手元のスコアは良いのに本番で悪い」が6ページに同じ型で並ぶ（misses-broken-evaluation・check-the-metric・selection-pressure・verifier-three-conditions・open-ended-loop-trap・evaluators-by-format）。受け皿の症状のページの題名「評価のおかしさに自分からは気づかない」は Claude の側の言い方で、評価がおかしいと知らない読者は題名から選べない | design §4.1 の2（症状の題名は読者の言葉）、README §4.5 の4。数え方：signs を「本番」「スコア」で抜いた | 症状のページの題名を読者の言葉にし（例「手元の評価は良いのに本番で通用しない」）、今の題名は aliases に移す。ほかの5ページの sign は、選び続けた・指標がずれた・隠しテストで落ちた・長く回した、など原因に固有の場面に書き換える |
| R1-08 | 中 | start/term-index（用語索引）、全ページの aliases | 別名1356件のうち48件が2ページ以上に重なり、名前で引く読者が最もよく打つ語がその中にある：skills・plugins・subagent・compaction・自動圧縮・prompt caching・thinking・extended thinking・research・permission modes・managed settings・sycophancy・prompt injection・/context・/cost など。用語索引で同じ語が2〜3ページを指し、どちらが主か分からない。「承認疲れ」は wrong-amount-of-approvals の別名で、approval-fatigue の題名でもある | design §1.2「名前で引く」・§7（用語索引は title と aliases から生成）、catalog/README §4.5 の2。数え方：aliases を小文字にして、2ページ以上に出るものを数えた | 用語ごとに主のページを一つ決める（features.yaml の機能の id に主のページを持たせるか、用語集に持つ）。索引では主のページを先に出し、ほかのページを「アプリ」「仕組み」などの印付きで並べる。ほかのページの題名と同じ別名は外す |
| R1-09 | 中 | design §7・§8.2（docs/ の構成）、start.yaml、ナビゲーションの並び | サイトのトップ（docs/index.md）の中身と作り方が、横断のページの表にも構成の図にも目次にもない。読者が最初に着くページで、三つの入口（困りごと・やりたいこと・名前）・検索・症状辞典への道・非公式の明記（D20 の「サイトの冒頭」）を置く場所である。あわせて、ナビゲーションでは症状辞典が23分野の22番目で、横の一覧から症状を探す読者には遠い | requirements §1（非公式をサイトの冒頭とフッターに明記）、D20、design §1.2・§2.1。数え方：design.md と catalog を「トップ」「ホーム」「docs/index」で探して0件 | トップを横断のページの表（§7）に足し、how-to-use と兼ねるか別に置くか、手書きか生成かを決める。ナビゲーションでは、start の直後に症状辞典と台帳を置くか、トップから直接指す（requirements §4.1 の並びの理由は活動の分野の順の話で、辞典の部分の位置は縛っていない） |
| R1-10 | 中 | delegate を中心とする前提の鎖（five-questions-before-delegating → what-not-to-delegate → verifier-defines-problem → verification-ladder → evidence-not-reports → define-done → agent-loop） | 前提の深さが6段以上のページが47本あり、43本がこの鎖を通る。「CI から Claude Code を使いたい」で着く github-actions-with-claude は8段・祖先14ページ、headless-basics は7段・11ページ、compare-hypotheses-in-parallel は9段・22ページ。知識マップを祖先の表示で開くと十数ページが出て、具体的な用で来た読者には「これだけ先に読め」に見える。鎖の多くは判断のページどうしで、「知らないと読めない」関係ではない | catalog/README §4.4 の1（直接の前提だけ）、design §6.1 の3（1ページで完結させる）、§3.1 の4（比例則は前提か関連のどちらかで満たせる）。数え方は §1 | 鎖の途中の判断どうしの前提（five-questions → what-not-to-delegate、what-not-to-delegate → verifier-defines-problem など）を related に移す。比例則は、各ページが確かめる・縛るのページを一つ直接持つ形で満たす。目安として、回すのページでも祖先は8ページ程度までにする |
| R1-11 | 中 | team（16ページ中必須1本）、design §1.2 の例 | 設計書が「状況から引く」の例に挙げる「チームで導入する」の行き先が rolling-out-to-teams（任意）だけで、初版（必須）では着けない。初版の team は review-bottlenecks の1本になる | design §1.2、requirements §1（組織での運用まで含む）、D10（初版は必須）。00 §3 分野17 でも必須は1本。数え方：signs を「導入」「チームで」「社内」で抜き、優先度を見た | 「チームで導入する」を受ける必須のページを一つ決める（share-team-settings か ai-usage-guidelines を必須にして sign を移す）。または design §1.2 の例を、初版で引けるものに替える |
| R1-12 | 中 | api（11ページ）、cost/when-ai-is-unavailable | API で組む開発者がまず当たる、レート制限と混雑（429・529）・再試行の考え方の入口がない。「429」「レート」「rate」「overloaded」で0件、「エラー」でも after-switching-models の1件だけ。when-ai-is-unavailable はサブスクリプションの上限と障害の話で、出力が max_tokens で途切れる話は structured-outputs-basics の中だけにある | requirements §1（API と SDK の概念）、00 §3 分野13（書き方でなく仕組みを扱う）。調査資料に API のエラーとしての扱いはない（rate limit の語は research/02・05 に3か所あるが、プランの上限とキャッシュの話）。数え方：題名・別名・signs・summary を語で引いた | when-ai-is-unavailable に API の節（上限の段階・混雑と再試行の考え方。数値は facts.yml）と sign「API が 429 や 529 を返す」を足すか、api に「API の上限とエラー」を1本（推奨で）足す。コード例は公式へ。足す前に一次資料で確かめる |
| R1-13 | 軽 | symptoms/does-more-than-asked・instructions-ignored、extend/what-to-put-in-claude-md、enforce/hook-recipes | 英語圏で多い失敗の型のうち三つに、読者の言葉の入口がない：古い関数を消さずに新しい版を横に足す（F4、広まり ◎）、作業フォルダに一時スクリプトやテスト用の DB を残す（F5）、決めた道具を使わない（uv でなく pip など。F6、○）。「uv」「pip」「死んだ」「一時」「散らか」で0件 | research/03 Q8 の F4〜F6 | does-more-than-asked に「古いコードを消さずに新しい版を足していく」「作業フォルダに一時ファイルを残していく」、instructions-ignored か what-to-put-in-claude-md に「決めたコマンド（uv・pnpm など）を使わず別の方法で実行する」を足す。hook-recipes に「決めたコマンドへ誘導する」の節を足す |
| R1-14 | 軽 | safety/where-bypass-is-ok・enforce/sandboxing | where-bypass-is-ok は「使い捨てのコンテナで無人の実行を動かす手順の例」の雛形を持つのに、「Docker」「devcontainer」「コンテナ」が、どのページの題名・別名・sign にもない | design §1.2「名前で引く」、research/04 Q3（DevContainer のファイアウォールを使う運用） | 別名に devcontainer・Docker・コンテナを足し、sign「コンテナの中で Claude Code を無人で動かしたい」を足す |
| R1-15 | 軽 | verify/independent-review・instructing-reviewers、delegate/automated-pr-review | 「AI が書いたコードに脆弱性がないか見させたい」の入口がない。/security-review は automated-pr-review（任意）の別名にだけあり、「セキュリティ」「脆弱」では when-requests-are-refused と paved-roads にしか当たらない | research/01（/security-review は公式の関連の機能に挙がる） | independent-review か instructing-reviewers に sign を足す（独立のページは要らない） |
| R1-16 | 軽 | safety/disclosure-and-provenance・checking-ai-rules、start/ai-and-sources | 「AI が書いたコードを製品や OSS に入れてよいか（権利・ライセンス）」で引くと、この辞典自身のライセンス（ai-and-sources）にだけ着く。法令の解釈は書かない決定だが、境界を示す入口もない | design §6.11（法令の解釈は書かない）、decisions「書き方の方針（安全・面・表現）」7（法的な助言ではない） | disclosure-and-provenance か checking-ai-rules に sign を足し、本文には「解釈はしない。確かめる先（利用規約・組織の規則）」だけを書く |
| R1-17 | 軽 | extend/connecting-mcp | 「つないだ MCP のツールが出てこない・つながらない」の sign がなく、summary にも不調の切り分けがない（isolate-with-safe-mode に着けば切り分けはできる） | research/03 Q4（MCP の利用は広い）、design §1.2 | connecting-mcp に sign と、切り分けの順（状態を見る → 設定の層 → --safe-mode）の節を足す。操作の詳細は公式へ |
| R1-18 | 軽 | prompting/ask-for-options・judgment/ask-without-sycophancy | 開発者がよく頼む「設計や技術の選び方を壁打ちしたい」の sign がない（「設計」「相談」「壁打ち」で当たらない）。中身は ask-for-options・ask-without-sycophancy・think-before-asking にある | design §1.2「やりたいことから引く」 | ask-for-options か ask-without-sycophancy に sign を足す |

ほかの観点と重なりうる指摘：R1-01 と R1-11 は優先度と第一波（R3）、R1-01 の stub の扱いは技術（R4）、R1-02・R1-10 は前提の質（R3）、R1-09 の D20 は要件の照合（R2）と重なりうる。R1 では読者が着けるかの面から書いた。

## 3. ユーザーに判断してもらうべき点

### 第一波の範囲（R1-01）

D10 と decisions「初版の範囲」は、第一波を「核と、そこから前提でたどれるページ」とし、decisions「公開する段階」は stub を公開しない。この二つを合わせると、第一波で公開する症状辞典から、対処のページの56%に道がない。次のどれかを選んでもらう。

| 案 | 中身 | 良い点 | 悪い点 |
| --- | --- | --- | --- |
| A | 第一波を「核と、前提と、症状のページの主な振り分け先でたどれるページ」に広げる（D10 を改める） | 公開したときに症状から対処まで着ける | 第一波が約180〜192ページになり（今の125から+55〜67）、必須174の大半と重なる。公開が遅れる |
| B | 第一波は今のまま。公開するページから未公開のページを指すときは、題名を「準備中」の平文で出し、公開したら道具が自動でリンクにする（stub は公開しないまま） | 決定を変えずに済み、後の波で書き直さない | 第一波の症状のページの半分ほどの行き先が「準備中」になる |
| C | 第一波は今のまま。症状のページの本文は第一波の中だけを指し、後の波で書き直す | 今の設計のまま進める | 第一波の症状辞典の用が足りず、33本を後で書き直す |

R1 の推奨は A か B。A を取るなら、R1-02 の主な行き先のキーとあわせて決める。

## 4. 直さなくてよいと判断した論点

- signs は読者の言葉で書けている。907件のうち、この辞典の独自の用語を含むのは1件（「落とし穴」）だけだった
- 00 §4 の73項目のうち55項目は同じ文の sign があり、残りも近い文がある。プラン名とモデル名は signs から外して aliases に置いた（「Fable を使う前に」など）。変わりやすい値を signs に入れない規則（design §5.3）に合い、名前でも引ける
- 機能名だけの題名（agent view・teleport・--bare・opusplan など）も、signs が読者の困りごとで書かれていて、機能名を知らなくても引ける
- 比喩や独自の用語の題名（机を整える・お願いと鍵・別室の部下）は、別名と signs で公式の語や困りごとから引ける（D14 のとおり）
- ほかのページにまとめた registry の候補31件は、まとめ先の別名・節・signs から名前で引ける（道具で見つからなかった9件を目で確かめた）
- 研究や機能の紹介に寄って見えるページ（ai-amplifies-organizations・harness-over-model・ai-in-contests-today・mods・voice-and-mobile など）も、読者の言葉の sign と判断の一文を持つ。多くは任意か推奨で、ai-in-contests-today は requirements §4.3 にある。削る理由は弱い
- 長い題名は89本のうち75本に nav_title がある。別名は1ページ2〜9個で、冒頭の別名の行が長すぎることはない
- 場面と面は散っている（場面がないページは57本。学習21・データ分析41ページ）。場面ごとに引く入口が空になる場面はない
- 症状のページの summary は、何を切り分けて何を決めるかを1文目で言えている。how-usage-limits-work のように summary だけで答えになるページもある

## 5. 確かめていないこと

- catalog のうち start と symptoms 以外の分野は、title・aliases・signs・summary・prerequisites・related・sections を道具で抜いて読んだ。materials・templates・visual と大半の notes は読んでいない。本文はまだないので、欠けとした論点が後で節として書かれる可能性はある
- 重なりの数（R1-04・R1-06・R1-07・R1-08）は、完全一致・2-gram の重なり・語での抜き出しで拾ったもので、言い換えの拾い漏れがある（下限の数）
- R1-01 の「stub へのリンクは止まる」は design §8.5・§8.6 の文から判断した。gen_site.py と check_pages.py はまだなく、related の一覧から stub を道具が自動で外すかどうかは設計書に書かれていない
- MkDocs（Material）の検索が、逆引きのページのような数百行の節をどう当てるか（R1-03）は試していない
- 課題のうち自分でつくったものは、03・04 を出どころに書いたもの以外（API の 429・529、設計の壁打ち、生成コードの権利、脆弱性のレビュー、devcontainer）は、読者が困る頻度を材料で確かめていない。Web は開いていないので、Claude Code・API の機能や挙動（/security-review、MCP の状態の見方、レート制限の仕組みなど）も一次資料で確かめていない
- 3回のクリックの数え方は、ページの描画や実際のリンクで試していない。第一波と初版の数は目次の第1版のもので、ほかの担当の指摘で変わりうる
- research/01・02・05・06・10・11 は、語を探すほかは読んでいない
