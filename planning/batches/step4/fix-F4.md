# 工程4 目次の直し：F4（cli・extend・contest）の報告

- 担当：F4。書いたのは `planning/catalog/cli.yaml`・`extend.yaml`・`contest.yaml` と、この報告だけ
- 日付：2026-11-04
- 指示：[brief-fix.md](brief-fix.md)、[README.md](README.md) の2段目の表（主な行：a・d・e・h〔R1-17〕・l・m〔recover-lost-work〕・q〔completion-notifications〕・r・w〔settings-layers〕）
- 読んだもの：design-review.md（全部）、catalog/README.md、schema/site.yml、review-R1.md・review-R3.md（全部）、review-R2.md（§2）、review-R4.md（受け持ちの id で検索）、fix-aliases.md、受け持ちの3ファイル（全部）、symptoms.yaml の全ページの signs・前提・関連、ほかの分野の関わるページ（読むだけ）。材料は research/01 B-1・G-1・P-2、03 Q2 C6・Q4 T4、28 #25〜#35
- ページの数（cli 19・extend 24・contest 9）・id・priority・level・wave は変えていない。まとめたページと新しいページはない
- 変えたページの notes の末尾に「（2026-11-04 工程4：DR-19 <記号>）」を足した。3ファイルの末尾の `notes` にも、工程4の1行を足した

## 1. DR-19 の行ごとの扱い

| 記号 | 変えたページ | 中身 | しなかったときの理由 |
| --- | --- | --- | --- |
| a | cli 9・extend 9・contest 3 のページ（§2。b と r の分を含む） | 症状のページが振り分ける困りごとの言い換えを、その対処が直接の答えになる狭い場面の symptom か、goal の形に書き換えた。対処のページどうしの近い文（R1-06・R3-5）も書き分けた | — |
| b | ask-claude-code・command-cheatsheet・writing-subagents | 「記事のやり方が手元で動かない」型の一般的な sign を、Claude Code の答えの版・コマンドの旧名・サブエージェントの作成の画面の場面にした | 症状のページを足すのは F7 |
| c | — | — | symptoms（F7） |
| d | usage-context-statusline・how-skills-load・plugins-and-marketplaces・evaluators-by-format | 外す側の別名5つを外した。permission-modes-overview の permission modes だけ残した（§3） | — |
| e | claude-md-vs-rules-skills-styles・running-contest-experiments | 推移的な前提2本を related に移した（§4） | 付表B の辺は受け持ちの分野にない |
| f・g | — | — | team（F6）・api（F2） |
| h | connecting-mcp | R1-17：sign「MCP サーバーをつないだのに、ツールが出てこない・つながらない」と節 troubleshooting（状態を見る → 設定の層とスコープ → --safe-mode で自分の設定のせいか）を足した。summary に「つながらないときは切り分けられる」、別名に /mcp、related に settings-layers・isolate-with-safe-mode、materials に research/28 #26・#28・#30 を足した。--safe-mode は MCP も読まないので、ほかの設定との干渉の切り分けに使うと notes に書いた | R1-13〜16・18 は受け持ちにない。R1-13（決めたコマンドを使わない）は what-to-put-in-claude-md も候補だが、症状のページ（F7）が受けるので足していない |
| i | using-auto-memory | related の memory-faq（app が how-memory-works にまとめた）を外し、その位置に症状のページ unexpected-memories を置いた | — |
| j・k | — | 指す先（suspected-degradation・own-generated-code）は id が残るので、直す点はない | — |
| l | init-and-first-claude-md・claude-md-length・what-to-put-in-claude-md | 削り方の持ち主を claude-md-length にした。claude-md-length に節 init-draft（/init の叩き台を削る）を足し、summary に「/init の叩き台」を入れ、outdated_advice に architecture-in-claude-md、materials に 03 Q2 C6 を足し、related の init-and-first-claude-md#prune をページへの参照にした。init-and-first-claude-md は summary を /init の操作と流れに書き直し、節 run-init を足し、節 prune を「叩き台を削ってから使う（削り方は claude-md-length）」の1段落にし、related の先頭を claude-md-length#init-draft にした | prune の anchor は残した（題名だけ変えた） |
| m | recover-lost-work | 消された直後の初動は deleted-something-important#recover が持つと notes に書き、related の先頭にその節を置いた。summary の「消えた変更」を「途中のやり取り」にした | 初動だけの節はなかったので、外した節はない |
| n | — | 新しい id（split-models-by-role・agent-teams）を指している。古い id は0件 | — |
| o・p | — | lost-in-the-middle・ai-amplifies-organizations を指していない | — |
| q | completion-notifications・long-team-competitions | completion-notifications はまとめずに残した。独自の判断を notes に1行で書いた：任せている間の確認を、通知で割り込ませるか、確かめる時刻を自分で決めてまとめて見るかを、待ち時間の長さと割り込みの重さで選ぶ。hook-recipes#notify はフックの組み方だけなので重ならない。節がなかったので2節（when-to-notify・channels）を足し、related の先頭を hook-recipes#notify にした。long-team-competitions の related から curb-sycophancy-and-overtrust を外した（team が前提の separate-roles にまとめたので、まとめた先は related に足せない） | — |
| r | competition-rules | 節 why-rules-differ・silence-is-not-permission を外し、本文の冒頭で前提の checking-ai-rules（節 why-rules-differ・when-unclear）を指すと notes に書いた。summary から「割れる理由」を外し、1文目を「引ける」の形にした。図の案を、三類型の理由の図から、主な大会を三類型の上に置く図に替えた。sign「規約に AI のことが書かれていない大会に出る」は答えが checking-ai-rules に移ったので外した | — |
| s | — | connecting-mcp・plugins-and-marketplaces が org-managed-settings-and-mcp を指す。id は変わらず、MCP の許可の話なので直さない | — |
| t・u | — | — | 受け持ちにない |
| v | usage-context-statusline | 内訳の読み方は what-uses-up-limits#find-what-uses-it と inspect-context#reading が持ち、節 instruments は道具ごとに何が分かるかと、読み方のページへの案内だけにすると notes に書いた。related の先頭を inspect-context#reading にした | — |
| w | settings-layers | summary の1文目を「誰に効き、どれが勝つかが決まる」から「誰に効かせたいかで層に書き分け、効かないときは /status で読み込まれた層を確かめて直せる」にした。節 verify に置く効かない原因の典型（信頼の前の project の allow と env、project と local では効かない defaultMode の値、-p の壊れた設定。01 B-1・research/28 #31）を notes に書いた | — |
| x | — | — | symptoms（F7） |

関わる DR-17・DR-18・DR-02：

- DR-17（R3-22）：受け持ちで書き直すよう名指しされた summary は settings-layers だけ（w）。r で competition-rules、l で init-and-first-claude-md・claude-md-length、h で connecting-mcp、m で recover-lost-work の summary も直したので、1文目を「何ができるか」の形にした
- DR-17（R2-19・R2-21）：コンテストの決定は contest の notes が守っていた。作者の参加の記録を事例に使わないことと、大会の規則の版を作者に確かめてもらわないことを、contest のファイルの notes に1行で足した。第三者のツールの成熟度と確認日を choosing-mcp-servers・evaluators-by-format の notes に足した
- DR-18：command-cheatsheet の notes に「旧名・今の名前・変わった時期は数値ファイルの名称の表から引く」を足した
- DR-02：受け持ちの分野に症状のページはない

## 2. 言い換えの重なり（a）で直した sign

| ページ | 前 | 後 | 重なっていた相手 |
| --- | --- | --- | --- |
| ask-claude-code | situation「記事に書かれたやり方が、手元の版で動かない」 | symptom「Claude Code に教わった機能や設定が、手元の版にない」 | doesnt-know-latest「古い記事のやり方が通じない」と DR-19 b の新しい症状のページ |
| permission-modes-overview | situation「確認なしで進むのが既定になってから、何が勝手に実行されるのか不安」 | goal「既定の権限モードで、何が確認なしで実行されるのか知りたい」 | wrong-amount-of-approvals「確認なしで実行されて怖い」 |
| when-to-plan | symptom「実装が終わってから、前提の誤解に気づくことが多い」 | symptom「大きな変更を、実装が済んでから方針ごと作り直すことが多い」 | prompting/let-claude-ask「作らせてから、前提の食い違いに気づく」（近い文）、not-what-i-meant |
| recover-lost-work | symptom「圧縮や異常終了の後に、途中の内容が見当たらない」 | symptom「異常終了したセッションの、途中のやり取りが見つからない」 | forgot-after-compaction（圧縮の場面が紛れる） |
| recover-lost-work | goal「過去のセッションのやり取りを読み返したい」 | goal「過去のセッションや、圧縮の前のやり取りを読み返したい」 | 上の圧縮の場面をやりたいことに移した |
| usage-context-statusline | symptom「気づいたら上限に当たって、作業が止まっていた」 | symptom「上限に近づいていることに、止まるまで気づけない」 | hits-limits-quickly「すぐ上限に当たる」 |
| settings-layers | symptom「設定を書いたのに効いていない」 | symptom「settings.json に書いた設定が効いていない」 | instructions-ignored「CLAUDE.md に書いたのに守られない」 |
| cloud-sessions-and-teleport | goal「PC を閉じても作業を進めておいてほしい」 | goal「手元で計画した作業をクラウドに渡し、PC を閉じても進めさせたい」 | surfaces/where-it-runs「PC を閉じても作業を続けさせたい」ほか「席を外している間も」の8ページ（R1-06・R3-5）。受け皿は where-it-runs |
| control-from-phone | goal「外出先から、手元のセッションの承認や指示をしたい」 | goal「スマホから、手元で動いているセッションに指示や承認を返したい」 | where-it-runs「外出先から、手元の PC で動いている作業を見たい」 |
| command-cheatsheet | goal「コマンドの名前から、使い方のページを引きたい」と situation「古い記事に出てくるコマンドが、手元で動かない」 | goal「コマンドの名前や、古い記事で見た旧名から、使い方のページを引きたい」（1つにした） | doesnt-know-latest・新しい症状のページ。同じ日に start/term-index が持った「古い記事に出てくる機能の名前から、今の名前を知りたい」と近い文を並べないため |
| when-to-add-what | situation「同じ注意を何度も繰り返している」 | goal「繰り返している注意や手順を、どの仕組みに移すか決めたい」 | repeating-the-same-explanation（題名「毎回同じ説明をしている」）。enforce の when-to-lock との束ねはなくなった |
| what-to-put-in-claude-md | symptom「プロジェクト固有のコマンドや落とし穴を、毎回知らないまま作業される」 | goal「ビルドやテストのコマンドと落とし穴を、毎回説明せずに伝えておきたい」 | repeating-the-same-explanation「新しい会話のたびにプロジェクトの説明からやり直している」 |
| claude-md-length | symptom「強調を書き足しても、規則が守られない」 | （外した） | instructions-ignored「CLAUDE.md を書き足すほど守られなくなった」。「強調しても守られない」は prompting/emphasis-words・basics/request-vs-lock にもあった（R1-06） |
| using-auto-memory | symptom「教えた覚えのないことを覚えていて、どこに書かれたか分からない」 | （外し、「どこに」は下の goal に入れた） | unexpected-memories（DR-19 i で必須） |
| using-auto-memory | goal「Claude が書き溜めた記録を見て、直したい」 | goal「Claude Code が書き溜めた記録の場所を知り、見て直したい」 | — |
| using-auto-memory | symptom「間違った結論を覚えられ、その後の作業に混ざる」 | symptom「一度の誤った結論を覚えられ、後の作業でも前提にされる」 | unexpected-memories（「混ざる」が紛れる） |
| manual-only-skills | symptom「頼んでいないのに、副作用のある手順を実行された」 | symptom「デプロイのような手順を、頼んでいないのに始められた」 | does-more-than-asked |
| hook-vs-skill | symptom「手順として書いたのに、ときどき飛ばされる」 | symptom「スキルに書いた手順の、必ずやってほしい一歩を飛ばされる」 | instructions-ignored |
| writing-subagents | symptom「昔の記事の手順で作ろうとしたら、作成の画面が出てこない」 | symptom「昔の記事の手順でサブエージェントを作ろうとしたら、作成の画面が出てこない」 | DR-19 b の新しい症状のページ |
| what-subagents-dont-inherit | symptom「サブエージェントの報告だけ、英語で返ってくる」 | goal「サブエージェントにも、日本語で報告させたい」 | replies-in-english（原因もこのページだけとは限らない） |
| choosing-mcp-servers | situation「便利そうな MCP サーバーを見つけた」 | goal「見つけた MCP サーバーを、入れる価値があるか見極めたい」 | safety/vetting-extensions「便利そうな MCP やプラグインを見つけた」（近い文） |
| evaluators-by-format | symptom「手元のスコアは上がったのに、本番の順位が上がらない」 | symptom「手元の評価器のスコアが、公式の採点と合わない」 | misses-broken-evaluation（R1-07） |
| long-team-competitions | symptom「手元で強くなったボットが、ほかのチームに勝てない」 | symptom「旧版に勝ち越したボットを採ったのに、ほかのチームには負ける」 | misses-broken-evaluation と同じ型（R1-07）。summary も節 adoption に合わせて「旧版とほかのチームとの対戦で採否を決めて」にした |
| competition-rules | situation「規約に AI のことが書かれていない大会に出る」 | （外した） | 答えが checking-ai-rules#when-unclear に移った（r） |

- 足した sign：connecting-mcp の symptom「MCP サーバーをつないだのに、ツールが出てこない・つながらない」（h）
- 残したもの：逆引きで1行に束ねるために同じ文にそろえた goal（resume-and-branch「長い作業を明日も続けたい」〔handoff-documents・progress-files〕、plugins-and-marketplaces「チームで同じ設定を使いたい」〔share-team-settings〕。DR-15）と、catalog/README §4.5 の4の例と同じ「より狭い場面」の symptom（path-scoped-rules「圧縮の後、フォルダごとの規約が効かなくなった」など）
- 数え方：目で全部の sign を symptoms.yaml の105文と比べ、2字の重なりと difflib の比で上位を出して確かめた（作業用の道具は scratchpad に置いた）

## 3. 別名の重なり（d）

外した（fix-aliases.md の外す側）：

| ページ | 外した別名 | 主のページ | 外しても引ける理由 |
| --- | --- | --- | --- |
| usage-context-statusline | /context | inspect-context | 題名に /context がある |
| how-skills-load | Skills・Agent Skills | skills-in-the-app | skills-in-the-app の前提がこのページ |
| plugins-and-marketplaces | plugins | plugins-in-the-app | /plugin・plugin.json と題名で引ける。plugins-in-the-app の related の先頭がこのページ |
| evaluators-by-format | 評価環境 | build-test-harness | ローカルテスタ・ローカル評価が残る |

残した：permission-modes-overview の permission modes。表の主は app の permission-modes-in-the-app で、理由は「機能のページ」だが、どちらも feature で、分野の並びで決まっている。permission modes は Claude Code の機能（features.yaml の permission-modes）の公式の英語名で、アプリのページは別の機能（app-permission-modes）を扱う。アプリのページからこのページへの道は related の9番目だけで、題名は日本語なので、外すと英語名から Claude Code のページを引けなくなる。fix-aliases.md の例外（別の機能の公式の名前で、外すと引けなくなるもの）に当たると判断した（§6 の1）。

主として持つもの（相手が外す側）：checkpoints-and-rewind（Esc を2回）、usage-context-statusline（/cost・/stats）、settings-layers（settings.local.json）、cloud-sessions-and-teleport（claude.ai/code・Claude Code on the Web）、control-from-phone（Remote Control）、writing-subagents（subagent）、connecting-mcp（.mcp.json）。最後の検査の時点で、相手の側ではどれも外されていた。

足した別名：connecting-mcp に /mcp（h）。ほかのページと重ならない。最後の検査で、受け持ちの分野が関わる重なりは permission modes の1語だけ。

## 4. 外した前提（e）

| ページ | 外した前提 | 届く道 | 移した先 |
| --- | --- | --- | --- |
| claude-md-vs-rules-skills-styles | what-to-put-in-claude-md | path-scoped-rules → what-to-put-in-claude-md | related の2番目 |
| running-contest-experiments | selection-pressure | experiment-log → selection-pressure | related の先頭（比例則は前提の experiment-log で満たす） |

## 5. まとめたページ・新しいページ・priority と level・anchor

- まとめたページ：なし。q の completion-notifications は、独自の判断を notes に1行で書けたので残した（§1）
- 新しいページ：なし
- priority・level・wave：変えていない
- 足した anchor：init-and-first-claude-md#run-init、claude-md-length#init-draft、connecting-mcp#troubleshooting、completion-notifications#when-to-notify・#channels
- 外した anchor：competition-rules#why-rules-differ・#silence-is-not-permission。DR-19 r が「節を外して指す」と名指ししたためで、brief-fix §4 の「anchor を変えない」とぶつかる（§6 の2）。catalog と planning の文書で、この2つを指す参照は0件だった
- 題名を変えた節：init-and-first-claude-md#prune（「叩き台をどう削るか」→「叩き台を削ってから使う（削り方は claude-md-length）」）

## 6. メインへ

1. **permission modes の主**：cli の permission-modes-overview を主にする案（理由は §3）。替えるなら app の permission-modes-in-the-app（F2）から外す。替えないなら、こちらに残すのを fix-aliases.md の例外として扱ってほしい。同じ理屈で Skills・Agent Skills・plugins も Claude Code の側を主にできるが、どれも app のページから前提か related の先頭でこちらに着くので、表どおり外した
2. **competition-rules の anchor を2つ外した**：DR-19 r を brief-fix §4 より優先した。残すべきなら、checking-ai-rules を1行で指す節として、同じ anchor で戻す
3. **safety の checking-ai-rules（F6）への提案**：competition-rules から外した sign「規約に AI のことが書かれていない大会に出る」の答えは checking-ai-rules の節 when-unclear にあるので、そちらに置く案。三類型の理由の図（個人の考える力を測る大会は禁止へ、成果物を測る大会は許可と開示へ、両方を測る大会は部門分けへ）も、節 why-rules-differ の図の案として渡せる
4. **enforce の when-to-lock（F5）**：situation「同じ注意を何度も繰り返している」は when-to-add-what と同じ文で束ねていたが、こちらは repeating-the-same-explanation の言い換えと見て goal に替えた。最後の検査の時点で when-to-lock には残っている。when-to-lock の summary は「同じ注意を二回した」を鍵に移す合図とするので、残す理由もある。そろえるかを見てほしい
5. **symptoms（F7）が routes を作るときの候補**：(a) deleted-something-important の初動（節 recover）の後に、成果の所在を探すなら recover-lost-work。(b) DR-19 b の新しい症状のページから command-cheatsheet（コマンドの旧名）・ask-claude-code#check-version・writing-skills#from-commands・writing-subagents#define（/agents の画面の削除）。(c) R1-13 の「決めたコマンドを使わない」を対処の側でも受けるなら what-to-put-in-claude-md#what-to-write（と enforce の hook-recipes）。こちらには足していない。(d) MCP の不調を受ける症状のページはないので、振り分けるなら connecting-mcp#troubleshooting

## 7. 検査の結果

`python3 tools/check_catalog.py --field <field>` を、最後の直しの後に流した（読んだページは357。ほかの担当がまとめた分だけ減っている）。

| 分野 | エラー | 警告 | 残した警告の理由 |
| --- | --- | --- | --- |
| cli | 0 | 0 | — |
| extend | 0 | 1 | 比例則：agents-md。notes に理由がある（指示ファイルの読み方と共有で、自律・並列・無人・権限の緩和を含まない）。工程3から残しているもの |
| contest | 0 | 0 | — |

- 推移的な前提の警告：0（直す前は extend 1・contest 1）
- まとめたページを指す参照のエラー：受け持ちの分野では0件。app が memory-faq を、team が curb-sycophancy-and-overtrust をまとめたが、using-auto-memory・long-team-competitions からの参照は外した
- 途中で contest に「未処理の候補」の警告が1件出た（team が curb-sycophancy-and-overtrust を pages から外し、merged に書く前だった）。まとまった後に参照を外して消えた

## 8. 確かめていないこと

- 書き換えた sign が読者の言葉として自然か、逆引きでどう並ぶかは、逆引きを生成して確かめていない（試作の工程で確かめる）
- connecting-mcp の切り分けの順と、settings-layers の効かない原因の典型は、research/01 B-1・G-1 と research/28 #26・#28・#30・#31 から書いた。公式の文書は開いていない（Web を開かない指示）。どちらの notes にも、書く前に一次資料で確かめると書いた
- completion-notifications の「端末の通知の設定」の材料は 01 KQ3 Gaps（端末の設定）と 01 の注記（terminalSequence の記述）だけで、設定の名前と面ごとの違いは確かめていない。スマホへの通知は材料にないので、手段に入れていない
- ほかの担当が同時に書いているので、検査の結果は最後に流した時点のもの
- 用語索引を aliases から作るか、features.yaml の page から作るか（DR-15）は設計で決まっていない。別名を外した後に英語名で引けるかは、その作り方に左右される
- DR-17 の「見せ方を目次の notes に書く」（R2-13）は受け持ちの行にないので、足していない
