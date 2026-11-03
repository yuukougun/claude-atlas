# 工程4 目次の直し：F2（surfaces・models・cost・api・app）

- 担当：F2。日付：2026-11-04
- 指示：[brief-fix.md](brief-fix.md)。受け持ちの主な行は [README.md](README.md) の2段目の表（a・d・e・g・i・j・o・v）
- 書いたもの：`planning/catalog/surfaces.yaml`・`models.yaml`・`cost.yaml`・`api.yaml`・`app.yaml` と、この報告。git と Web は使っていない
- 変えたページの notes の末尾に「（2026-11-04 工程4：DR-19 <記号>）」（DR-18 のものは「DR-18」）を足した。ページの id と既存の anchor は変えていない（suspected-degradation の節 check-order は DR-19 j のとおり外した。指していたページはない）

## 1. DR-19 の行ごとの扱い

| 記号 | 変えたページ | 中身 | しなかったときの理由 |
| --- | --- | --- | --- |
| a | surfaces：choosing-a-surface・where-it-runs／models：effort-levels・suspected-degradation／cost：what-uses-up-limits／api：citations-basics・long-running-agent-context／app：using-projects・how-memory-works・long-chat-limits・skills-in-the-app・permission-modes-in-the-app・voice-and-mobile | 症状のページが振り分ける困りごとの言い換えを、goal か、そのページが直接の答えになる狭い場面にした。症状でないページどうしの近い文は、同じ問いなら同じ文にそろえ（DR-15 の束）、違う問いなら場面を書き分けた（§2） | — |
| b | なし | 受け持ちの「古い記事・前のやり方」の型の sign は、どれもすでに狭い場面（Cowork が別のアプリという説明、考えさせるキーワード、節約の古いコツ、計画と実装の分業のコツ、プランの名前の変更、文体の設定）だった | 一般的な sign がない |
| d | surfaces：where-it-runs・claude-code-surfaces／models：suspected-degradation／cost：what-uses-up-limits／api：stateless-messages-api・tool-use-loop／app：where-to-put-instructions・search-research-thinking | fix-aliases.md の「外す側」の別名を外した。表の外でも、ほかのページの題名か別名とほぼ同じ語を外した（§3） | — |
| e | app：tasks-and-schedules-in-the-app | 推移的な前提 choosing-a-surface を外し、節 choosing-a-surface#app-tasks-or-claude-code を related の先頭に置いた（§4） | 付表B は delegate（F6）の受け持ち |
| g | api：rate-limits-and-errors（新規）。関連を足した：cost の how-usage-limits-work・when-ai-is-unavailable、api の batch-api-basics | API の rate limits と混雑のエラー・再試行の入口（推奨・仕組みにする）。章「上限とエラー」を足した。new_features に api-rate-limits（§5） | — |
| i | app：how-memory-works（memory-faq をまとめた）・incognito-chats | memory-faq を merged にし、節 deleted-chats・turning-off を how-memory-works に同じ anchor で足した（§5） | unexpected-memories を必須にするのは symptoms（F7） |
| j | models：suspected-degradation | 安く確かめる順の節を外し、測って確かめる手順と製品の側の変更の確かめ方と例に絞った。題名「劣化を疑ったら測って確かめる」、型を concept から recipe に、summary・signs・aliases・節を直した | 安く確かめる順を seems-less-capable の本体にするのは F7 |
| n | models：split-models-by-role の merged の理由（when-to-use-haiku） | 旧 id（opusplan）を指す文を直した（id はメインが改めた） | — |
| o | models：thinking-keywords（summary・sign）・split-models-by-role（題名） | thinking-keywords の summary を「その依頼だけ深く考えさせる手段もある」の形にし、sign の「この1回の」を外した。split-models-by-role の題名から「（opusplan など）」（モデルの系統の名前を含むエイリアスの名前）を外し、opusplan を aliases の先頭に置いた | cloud-schedules・enterprise-vs-team-plans は F6 |
| p | app：too-much-project-knowledge・how-attachments-are-read | basics（F1）が lost-in-the-middle を context-rot にまとめたので、前者は related から外し（context-rot が同じリストにある）、後者は context-rot#lost-in-the-middle に替えた | — |
| q | models：model-quirks・after-switching-models | prompting（F3）が does-double-check-work を verification-ladder にまとめたので、related を verification-ladder#verbal-checks に替えた | — |
| v | cost：what-uses-up-limits | 節 find-what-uses-it を「/usage の内訳の読み方（自分の場合を確かめる）」にし、/usage の内訳の読み方の持ち主にした（notes に cli・eval との分担） | /context の内訳は context の inspect-context（F3） |
| c・f・h・k・l・m・r・s・t・u・w・x | なし | — | 受け持ちのページが出てこない（h の R1-12 は g で扱った） |
| DR-18 | cost：choosing-a-plan | 改名の事実（旧名・今の名前・時期）は数値ファイルの名称の表を正にし、節 plan-table・台帳 max-5x-or-20x・change-timeline-2026・term-index はそこから引く、と notes に書いた | — |

## 2. 言い換えの重なり（a）で直した sign

症状のページの困りごとの言い換え（左が前、右が後。括弧は重なっていた症状のページ）：

| ページ | 前 | 後 |
| --- | --- | --- |
| models/effort-levels | symptom「簡単な作業なのに返答が遅く、使用量も多い」 | goal「簡単な作業では、深く考えさせずに速く済ませたい」（too-slow） |
| models/suspected-degradation | situation「更新の後から、結果が変わった気がする」 | goal「更新の前と後で、同じ課題の結果を比べたい」（seems-less-capable。R3 付表A の1） |
| 同上 | goal「性能が落ちたのが製品の変更か自分の設定かを切り分けたい」 | goal「「劣化した」と感じたのが本当かを、測って確かめたい」（切り分けは seems-less-capable。j） |
| 同上（足した） | — | situation「「性能が落とされた」という話を見かけ、自分の環境でも起きているか確かめたい」 |
| cost/what-uses-up-limits | symptom「少し使っただけなのに上限に当たる」 | goal「/usage の内訳から、何を減らせばよいかを読み取りたい」（hits-limits-quickly。付表A の10。v） |
| api/citations-basics | symptom「引用させても、資料にない文が混ざる」 | symptom「API で資料を渡して引用させても、資料にない文が引用に混ざる」（plausible-falsehoods。付表A で R3 が迷ったもの） |
| api/long-running-agent-context | symptom「長く動かしたエージェントが、前に決めたことを忘れる」 | symptom「API で組んだエージェントを長く動かすと、前に決めたことを忘れる」（forgot-after-compaction・forgets-in-long-chats） |
| app/using-projects | symptom「会話を変えるたびに資料を貼り直している」 | goal「同じ資料を、会話のたびに添付し直さずに使いたい」（repeating-the-same-explanation）。あわせて「同じ資料を使う作業を何度も繰り返す」の型を goal から situation にした |
| app/how-memory-works（memory-faq から） | symptom「間違った思い込みを覚えられてしまった」 | goal「間違って覚えられた内容を直したい」（困りごとの入口を unexpected-memories だけにする。R3-8） |
| app/long-chat-limits | symptom「会話が長くなり、それ以上続けられなくなった」 | goal「アプリの長い会話で、自動の要約が働くと何が残るか知りたい」（hits-limits-quickly。付表A の11） |
| app/skills-in-the-app | symptom「同じ手順の説明を会話のたびに貼っている」 | goal「長い手順を、必要なときだけ読ませたい」（repeating-the-same-explanation。付表A の9。extend の how-skills-load と同じ文） |
| app/permission-modes-in-the-app | symptom「確認なしにどこまで進めてよいか分からない」 | goal「アプリに任せる範囲を、低いリスクの作業から広げたい」（wrong-amount-of-approvals） |

症状でないページどうしの近い文（R1-06・R3-5。DR-15）：

| ページ | 前 | 後 | 扱い |
| --- | --- | --- | --- |
| surfaces/where-it-runs | goal「PC を閉じても作業を続けさせたい」 | goal「PC を閉じても作業を進めておいてほしい」 | 一般の問いの受け皿（R1-06 の(2)）。cli の cloud-sessions-and-teleport と delegate の cloud-schedules は、同じ工程で手段に固有の文に書き分けられた |
| 同上 | goal「外出先から、手元の PC で動いている作業を見たい」 | goal「外出先から触る作業を、手元とクラウドのどちらで動かすか決めたい」 | cli の control-from-phone・app の voice-and-mobile と書き分け |
| surfaces/choosing-a-surface | goal「コードを書かない仕事にも Claude Code を使うべきか知りたい」 | goal「コードを書かない仕事は、アプリと Claude Code のどちらが向くか知りたい」 | recipes の office-paperwork の situation と書き分け |
| app/long-chat-limits | situation「一つの会話で長い作業を続けている」 | situation「claude.ai で一つの長い会話を使い続けている」 | context の tidy-the-desk と同じ文にそろえた（束） |
| app/permission-modes-in-the-app | goal「取り消しにくい操作の前だけ止まってほしい」 | goal「確認なしで進めつつ、危ない操作だけは止めたい」 | enforce の what-auto-mode-stops と同じ文にそろえた（束。Claude Code とアプリの印） |
| app/voice-and-mobile | goal「スマホから作業の進み具合を見たい」 | goal「スマホのアプリから、任せたタスクの進み具合を見たい」 | cli の control-from-phone・where-it-runs と書き分け |

見て残したもの（その対処が直接の答えになる狭い場面）：how-usage-limits-work「アプリをたくさん使った日は、Claude Code でも早く上限に当たる」、before-using-top-model「上位のモデルを少し使っただけで、残りの枠が大きく減った」、what-uses-up-limits「長いセッションを続けると、消費が急に増える」、parallel-and-loop-costs「夜通しループを回したら、上限や請求が一気に増えた」、model-quirks「モデルを替えたら、確認ばかりで止まるようになった」、how-attachments-are-read「Word の資料に入れた図を読んでくれない」、too-much-project-knowledge「資料を足すほど、答えが資料を踏まえなくなった気がする」、skills-in-the-app「以前使っていた文体の設定が見当たらない」。

数え方：受け持ちのページの signs と症状のページの全 sign（と、症状でないほかのページの sign）の全組を、2字の重なり（Jaccard）と difflib の比で並べ、上位と、症状のページの題名・sign を通して目で照らした。

## 3. 別名の重なり（d）

fix-aliases.md の表で外したもの：

| ページ | 外した別名 | 主のページ |
| --- | --- | --- |
| api/stateless-messages-api | ステートレス | basics の rereads-whole-history（英語の stateless は API の形の語として残した） |
| api/tool-use-loop | ツールの呼び出し | basics の agent-loop |
| app/search-research-thinking | Thinking・extended thinking | basics の how-thinking-works（アプリの思考の切り替えは models の effort-levels#thinking-toggle を related に指し直して引ける） |
| 同上 | Research | app の using-research |
| app/where-to-put-instructions | 組織の指示 | app の shared-projects-and-org-skills（related を #org-instructions に指し直した） |
| cost/what-uses-up-limits | /cost | cli の usage-context-statusline |
| surfaces/claude-code-surfaces | claude.ai/code・Claude Code on the Web | cli の cloud-sessions-and-teleport |
| surfaces/where-it-runs | Remote Control | cli の control-from-phone |

表の外で外したもの（判断）：

- models/suspected-degradation の「性能が落ちた」：表では suspected-degradation が主（分野の並びで最初の見当）だが、症状の言葉で、R1-04 が seems-less-capable との言い換えの束に挙げていた。j で測って確かめるページに絞ったので外し、主を seems-less-capable にするようメインへ書いた（§6 の1）。「賢くなくなった」も seems-less-capable の題名の語なので外した。「nerf」は、製品の側で弱められたという話を確かめる語として残した
- surfaces/where-it-runs の「クラウドセッション」：cli の cloud-sessions-and-teleport の題名の語
- surfaces/claude-code-surfaces の「VS Code 拡張」「JetBrains」：cli の using-ides の題名と別名（VS Code の拡張・JetBrains のプラグイン）と「の」の有無だけの違い。使い方の本体のページを主にした
- app/how-memory-works：memory-faq の別名のうち、症状の言い方の「メモリの困りごと」は移さなかった（Memory FAQ・メモリの Pause と Reset は移した）

残した別名：外す側で「外すと引けなくなる」例外に当てたものはない。claude-code-surfaces の「Desktop の Code タブ」は、Desktop の使い方を持つページがほかにないので残した。表で受け持ちのページが主のもの（Skills・Agent Skills・Plugins・permission modes・Scheduled tasks・音声入力・voice mode・Research・/deep-research・組織の指示・prompt caching・経費精算・拡張思考）は残した。

足した別名：opusplan（split-models-by-role。題名から移した）、Claude Code をどこで使うか（claude-code-surfaces）、劣化の確かめ方（suspected-degradation）、新しいページの別名（レート制限・API のエラー・429・529・overloaded・再試行・リトライ）。

## 4. 外した前提（e）

| ページ | 外した前提 | 理由 | 移した先 |
| --- | --- | --- | --- |
| app/tasks-and-schedules-in-the-app | choosing-a-surface | 前提の permission-modes-in-the-app から届く（推移的な前提の警告） | related の先頭に choosing-a-surface#app-tasks-or-claude-code（アプリのタスクか Claude Code かの使い分けの節） |

受け持ちの5分野の推移的な前提の警告は、これで0件（前は app の1件だけ）。

## 5. まとめたページ・新しいページ・型と題名を変えたページ

- **まとめた**：app の memory-faq → how-memory-works（merged に `{id, into, reason}`）。how-memory-works の題名を「アプリのメモリ（仕組み・範囲・消し方と止め方）」（nav_title「アプリのメモリ」）にし、節に deleted-chats（会話を消しても残るもの）と turning-off（消し方と止め方）を memory-faq と同じ anchor で足し、manage を「覚えた内容を見る・直す（棚卸し）」にした。memory-faq の節の行き先は、deleted-chats・turning-off が同じ anchor、mixed-projects が how-memory-works#scope、review が how-memory-works#manage（merged の reason に書いた）。principle に確かめる、tracks に incognito を足した。priority（必須）と level（整える）は両ページで同じなので変えていない
- **新しいページ**：api の rate-limits-and-errors「rate limits とエラー（混雑と再試行）」。concept・仕組みにする・推奨（DR-19 g）・面は api と claude-code（Claude Code で同じ状態コードを見た読者も着くため）・volatility 高。章「上限とエラー」を足した。節は、エラーの見分け方（自分の上限・全体の混雑・要求の誤り）、上限の種類と今の値の確かめ方、再試行の考え方、上限に当たりにくい送り方、エラーにならずに止まる応答（長さの上限・拒否。振り分けだけ）、Claude Code で同じエラーを見たとき。比例則の守りは verify の checking-unattended-runs と safety の when-requests-are-refused（related）。notes に「新規（2026-11-04 工程4）：…」と、書く前に一次資料で確かめる項目を書いた。new_features に api-rate-limits を足した。入ってくる道は cost の how-usage-limits-work・when-ai-is-unavailable と api の batch-api-basics の related
- **型を変えた**：models の suspected-degradation を concept から recipe に（中身が測って確かめる手順になった。確かめるページの felt-vs-measured を前提に持つ）
- **題名を変えた**：suspected-degradation（「「劣化した」と感じたら（版と effort を確かめる）」→「劣化を疑ったら測って確かめる」）、split-models-by-role（「（opusplan など）」を外した）、how-memory-works（上のとおり）
- **priority と level を変えたページ**：ない

## 6. メインへ

1. **「性能が落ちた」の主のページを seems-less-capable に替えてほしい**（fix-aliases.md の見当は suspected-degradation）。suspected-degradation からは外したので、symptoms の担当（F7）が表のとおり seems-less-capable から外すと、どのページにも残らない。F7 への指示を直してほしい。あわせて、j の symptoms 側：seems-less-capable の診断の節が安く確かめる順の本体になる。routes にするときの行き先は suspected-degradation#measure（測って比べる）と #official-sources（製品の側の変更を確かめる先）
2. **memory-faq を指すほかの分野の参照**は、いまは symptoms の unexpected-memories の related の1件（検査のエラー1件）。unexpected-memories は how-memory-works を前提に持つので、how-memory-works に置き換えず外す（置き換えると前提と関連の重複になる）。extend の using-auto-memory と safety の where-your-data-goes は、すでに外されていた。unexpected-memories を必須にするのは F7（DR-19 i）
3. **新しいページ rate-limits-and-errors** は registry にない（notes に新規の印）。registry と features.yaml（new_features の api-rate-limits）への取り込みはメインが決める。調査資料にこの話題がないので、data の初版（DR-09）で一次資料（Platform の Rate limits・Errors、SDK の再試行の既定、Claude Code の errors のページ）を確かめる項目に入れてほしい
4. **/deep-research** は二つの別の機能の公式の名前（アプリで Research を起動するコマンドと、Claude Code の dynamic workflows に付いてくる workflow。research/02 §1-1・research/01 E-5）。主は using-research のままにした。delegate の dynamic-workflows も残している（fix-aliases の例外に当たる）。用語索引では面の印を付けて二つを並べるとよい
5. **同じ文にそろえた sign**（DR-15 の束）：long-chat-limits と context の tidy-the-desk「claude.ai で一つの長い会話を使い続けている」、skills-in-the-app と extend の how-skills-load「長い手順を、必要なときだけ読ませたい」、permission-modes-in-the-app と enforce の what-auto-mode-stops「確認なしで進めつつ、危ない操作だけは止めたい」。検査の時点では相手も同じ文。相手が後で文を変えると束が切れる（近い文が2行に戻るだけ）。ほかの担当が受け持ちのページの文にそろえたもの：changes の outdated-advice-ledger（thinking-keywords の goal）、delegate の headless-basics（check-billing-path の symptom）
6. **別名の主の見当で考え直す余地があるもの**（変えていない）：Skills・Agent Skills（主 skills-in-the-app。面をまたぐ仕組みの名前で、考え方の本体は extend の how-skills-load〔必須〕。extend はすでに外した）、Plugins（主 plugins-in-the-app。考え方の本体は extend の plugins-and-marketplaces）、permission modes（主 permission-modes-in-the-app。Claude Code の公式の文書の名前でもあり、cli の permission-modes-overview にも今は残っている）、経費精算（主 paying-in-yen〔Claude の料金を経費にする〕。recipes の office-paperwork〔経費の事務を Claude にさせる〕とは意味が違う。office-paperwork から外すなら、そちらは「経費の一覧づくり」などの言い換えで引ける）
7. app の where-to-put-instructions の nav_title「指示の置き場所」が、extend の claude-md-vs-rules-skills-styles の別名と同じ（fix-aliases の表の外。nav_title は用語索引に出ない見込みなので変えていない）
8. DR-17 の「目次の notes に見せ方を書く」は、受け持ちの行にないので書いていない。一覧を作るときの材料：suspected-degradation の節 measure（版と effort を記録して同じ課題を比べる）と thinking-keywords（「よく考えて」と書いても effort が上がらないこと）は、制作の環境の Claude Code で検証ノートにできる

## 7. 検査の結果

`python3 tools/check_catalog.py --field <field>`（最後に流した時点。ほかの担当の書きかけで全体のページ数は 357）：

| 分野 | エラー | 警告 |
| --- | --- | --- |
| surfaces | 0 | 0 |
| models | 0 | 0 |
| cost | 0 | 0 |
| api | 0 | 2（比例則） |
| app | 0 | 0 |

- 推移的な前提の警告：0件
- 残した警告：api の feature-to-api-mapping と prompt-caching-in-practice の比例則。どちらも notes に「任せる幅を広げる内容ではない（対応関係の表・費用と待ち時間の整え方）」と理由があり、工程3の統合（M9）で見直して残したもの
- まとめた memory-faq を指す、ほかの分野の参照のエラー：1件（symptoms の unexpected-memories）
- 参考：全分野の検査はエラー11件・警告26件。受け持ちに関わるのは上の1件だけで、ほかはほかの担当のまとめ（lost-in-the-middle・does-double-check-work・curb-sycophancy-and-overtrust・ai-amplifies-organizations）の後の参照

## 8. 確かめていないこと

- rate-limits-and-errors の中身（429・529 の意味、上限の種類と段階、応答のヘッダー、SDK の自動の再試行、Claude Code の表示）は調査資料になく、一次資料で確かめていない（Web を開かない）。sign と aliases の 429・529 は R1 の課題の読者の言葉による。summary と節の題名には値を書いていない
- suspected-degradation の節 if-product-side（stable の通り道で退行を避ける・/feedback で報告する）は、二次情報（04 Q3）と research/22 #3 による
- how-memory-works の節 deleted-chats・turning-off は 02 §1-4 による。2026年に二度変わった機能で、今の画面の名前（Pause・Reset など）は確かめていない
- アプリの Auto モードが「危ない操作だけ止める」動きをするかは確かめていない（permission-modes-in-the-app の sign は読者のやりたいことで、答えは本文が書く）
- 言い換えの重なりは機械の比と目で拾ったもので、比の低い言い換えは見落としがありうる
- 同じ文にそろえた相手の sign と、ほかの分野の参照の状態は、最後に検査した時点のもの。ほかの担当が同時に直しているので変わりうる
