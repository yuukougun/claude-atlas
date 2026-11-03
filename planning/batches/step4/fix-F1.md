# 工程4 目次の直し：F1（start・changes・basics・judgment）

- 担当：F1。日付：2026-11-04
- 指示：[brief-fix.md](brief-fix.md)。受け持ちの主な行は [README.md](README.md) の2段目の表（a・b〔changes の一般的な sign〕・d・e・k〔judgment 側〕・p〔lost-in-the-middle〕・DR-17〔how-to-use・ai-and-sources の notes〕）
- 書いたファイル：`planning/catalog/start.yaml`・`changes.yaml`・`basics.yaml`・`judgment.yaml` と、この報告だけ。git と Web は使っていない
- 変えたページの notes の末尾に「（2026-11-04 工程4：…）」を足し、4ファイルの冒頭の注記に1行足した。id と既存の anchor は変えていない（context-rot に anchor `lost-in-the-middle` を足した）

## 1. DR-19 の行ごとの扱い

| 記号 | 変えたページ | 中身 | しなかったときの理由 |
| --- | --- | --- | --- |
| a | basics 11（attention-budget・rereads-whole-history・context-rot・what-survives-compaction・agent-loop・unfaithful-reasoning・why-hallucinations・knowledge-cutoff・reward-hacking・request-vs-lock・data-vs-instructions）、judgment 4（agreement-is-not-evidence・decide-when-to-quit・postmortems・learning-with-ai） | 症状のページが振り分ける困りごとの言い換えを、goal か狭い場面に書き換えた（§2） | — |
| b | changes 3（outdated-advice-ledger・dating-information・checking-for-updates）、start の term-index、basics の knowledge-cutoff（notes） | 古い記事の一般的な sign を、そのページが答える goal にした。notes の「doesnt-know-latest に置く」（M2）を、症状辞典に足す「記事や前のやり方が通じない」に改めた | 新しい症状のページは symptoms の担当（F7）が足すので、id を知らず related には入れていない（§6） |
| d | basics 4（how-thinking-works・what-survives-compaction・subagent-isolation・why-prompt-caching）、judgment の how-much-understanding-to-keep | 外す側の別名を外した（§3） | — |
| e | judgment の how-much-understanding-to-keep | 推移的な前提の警告は受け持ちの4分野で前も後も0件。R1-10 の「判断どうしの前提を関連に」に当たる1辺を関連に移した（§4） | 付表B の辺は受け持ちにない |
| h | start の ai-and-sources | R1-16：別名「ライセンス」を「この辞典のライセンス」にした（生成コードの権利で引いた読者が、この辞典のライセンスに着かないように） | R1-18 は prompting の担当が ask-for-options に sign「設計や技術の選び方を壁打ちしたい」を足したのを確かめたので、ask-without-sycophancy には足していない（同じ困りごとを2か所に置かない） |
| k | judgment の how-much-understanding-to-keep・learning-with-ai | 理解の線引き（中核と周辺・説明できないものは採らない）を how-much-understanding-to-keep に置くと notes に書いた。verify の担当が own-generated-code の困りごとの sign（「マージしたコードを、自分で説明できない」「障害が起きたとき…直せない」）を外して手順の goal にしたので、learning-with-ai の「AI に書かせたコードを、自分では説明できない」を how-much-understanding-to-keep に移し、1か所にした | — |
| n | — | 受け持ちのファイルの参照が新しい id（large-context-window）になっていることを確かめた | メインが道具で済ませていた |
| o | — | 受け持ちの title・summary・signs に変わりやすい値がないことを確かめた（数字は change-timeline-2026 の年だけ。年ごとのページの設計で、R3 も直さなくてよいとした） | 該当なし |
| p | basics の lost-in-the-middle → context-rot。start の four-principles（関連） | lost-in-the-middle をまとめた（§5）。team の担当が ai-amplifies-organizations を paved-roads の節 amplifier にまとめたので、four-principles の関連を `paved-roads#amplifier` に替え、notes に書いた | ai-amplifies-organizations のまとめは team の担当 |
| q | basics の sycophancy、judgment の human-pitfalls・agreement-is-not-evidence・ask-without-sycophancy（関連） | team の担当が curb-sycophancy-and-overtrust を separate-roles の節 against-sycophancy にまとめたので、4ページの関連を `separate-roles#against-sycophancy` に替え、agreement-is-not-evidence の notes の文も直した | 受け持ちにまとめる候補はない |
| x | — | — | 症状のページは symptoms の担当。前提を basics の概念にすると段の逆転が出うる（§6） |
| c・f・g・i・j・l・m・r・s・t・u・v・w | — | 受け持ちのページに直すところはなかった。i の memory-faq・q の does-double-check-work を指す参照も受け持ちのファイルにない | 該当なし |

関わる DR の反映（DR-19 以外）：

| DR | 変えたページ | 中身 |
| --- | --- | --- |
| DR-17 | how-to-use | 節 official-docs の題名に公式の教材を足し、notes に公式の教材（Academy・公式の文書）の案内（評価や推薦をしない、講座の名前と数は変わるので入口へのリンク、AI Fluency は構成に使わない）、守れない約束を書かない（report は窓口と書いてほしいことだけ、freshness は期限までに必ず点検するとは書かない）、report・freshness の節も作者の承認に入れることを書いた。sign「公式の文書や講座とこの辞典を、どう使い分ければよいか知りたい」を足し、summary の2文目に「公式の文書や教材との使い分け」を足した |
| DR-17・DR-10・DR-14・DR-06 | ai-and-sources | notes の「完成」の意味を「設計で決める」から DR-10 の決定（draft〔下書き・未検証〕→ reviewed → done。作者がすべてを確かめた意味ではない）に改めた。節 unofficial を全ページの冒頭とフッターの非公式の文・© 2026 yuukougun・ライセンスの表示とそろえる、節 citations に訳して載せない・転載しない・出典に残すを書く（節の題名にも足した）、contact と disclaimers で返事や直す時期を約束しない、作者への頼みは工程7の終わりの1回（how-to-use の2節と冒頭・フッターの文と一緒に）、と書いた |
| DR-17（R2-29） | rereads-whole-history | visual を dynamic から static にした。公式の対話型の図へのリンクを主にし、自作は公式にない点（毎ターン全部を読み直す・窓に近づくと圧縮）だけの静止図。動く図にするのは試作で公式が足りないと分かったときだけ |
| DR-01・DR-10・DR-11・DR-14 | how-to-use | 節 stage の題名に「準備中」の題名を足し、notes に段階の移り方・「題名（準備中）」の読み方・期限の日の計算（DR-11）・サイトのトップとの分担（トップは三つの入口と検索だけ、節 lookup から症状辞典を直接指す）を書いた。visual の見取り図に冒頭とフッターの非公式の文と「題名（準備中）」を足した |
| DR-02 | six-causes・knowledge-map | 節 to-symptoms の表と知識マップは routes も読む、と notes に書いた。knowledge-map の summary の2文目を「図は各ページの前提と段階、症状のページの振り分け先から作る」にした |
| DR-15 | reverse-index・term-index | 逆引きの節の分け方と同じ文の束ね方、用語索引の主のページの出し方を notes に書いた |
| DR-18 | outdated-advice-ledger・change-timeline-2026・term-index | 名前と画面の変更の事実は数値ファイルの名称の表を正にし、台帳の改名の行（6行）は消さずに時期をそこから引く、と notes に書いた。change-timeline-2026 の「台帳ではなく」は、二重に持たない意味に読むと注記した |

start の open_issues の2件（生成のページの型、ai-and-sources の承認の時期）に、DR-17・DR-06 で決まったと注記した。judgment の open_issues の C9 への依頼に、要らなくなったと注記した。

## 2. 言い換えの重なり（a・b）で直した sign

（　）は重なっていた症状のページ。

| ページ | 前 | 後 |
| --- | --- | --- |
| attention-budget | symptom「資料をたくさん渡したのに、大事な点を拾ってくれない」（skipped-later-pages・forgets-in-long-chats） | goal「資料を多く渡すほど、大事な点が拾われにくくなる理由を知りたい」 |
| rereads-whole-history | symptom「会話が長くなると返事が遅くなり、上限の減りも早くなる」と goal「長い会話がなぜ重くなるのか知りたい」（hits-limits-quickly・too-slow） | goal「長い会話ほど返事が遅く、上限の減りも早くなる理由を知りたい」（1つにまとめた） |
| context-rot | symptom「失敗したやり方を何度も蒸し返してくる」（going-in-circles） | goal「失敗した試みが会話に残ると、同じ誤りに戻りやすくなる理由を知りたい」 |
| context-rot（旧 lost-in-the-middle） | symptom「長い資料の真ん中あたりの内容を見落とされる」（skipped-later-pages） | goal「長い資料の真ん中の情報は使われにくい、というのは本当か知りたい」 |
| what-survives-compaction | goal「圧縮のあとも守らせたい約束を、どこに書けばよいか知りたい」（context の promises-after-compaction の goal とほぼ同じ文） | goal「圧縮のあとに何が残り、何が消えるのか知りたい」（DR-15 の書き分け） |
| agent-loop | symptom「動くか確かめないまま、終わったことにする」（claims-done-but-isnt） | goal「動くか確かめないまま終わったことにする理由を知りたい」 |
| unfaithful-reasoning | symptom「説明された理由と、実際の結果が食い違う」（insists-on-mistakes。R3 付表A の16） | symptom「表示された思考の筋道と、最後の答えが合っていない」 |
| unfaithful-reasoning | goal「推論の過程を全部見せてほしい」 | goal「なぜその答えになったのか、過程を全部見せてほしい」（prompting の asking-for-reasoning と同じ文。DR-15 の束ね） |
| why-hallucinations | symptom「もっともらしいが事実と違うことを、自信を持って言う」（plausible-falsehoods） | goal「もっともらしい誤りを自信を持って言う理由を知りたい」 |
| knowledge-cutoff | symptom「古い版の書き方を、今の方法として勧めてくる」（doesnt-know-latest。R3 付表A の13） | 外した（goal の1つが残る） |
| reward-hacking | symptom「テストや採点の抜け道を突いて通そうとする」（rewrote-tests-to-pass） | goal「採点やテストの抜け道を突かれる理由を知りたい」 |
| request-vs-lock | symptom「「必ず」と書いても破られる」（instructions-ignored。R1-06 の束で prompting の emphasis-words とも重なる） | goal「「必ず」と書いた規則でも破られる理由を知りたい」（困りごとは emphasis-words に寄せる） |
| data-vs-instructions | symptom「読ませた資料の中の指示に従ってしまった」（followed-injected-instructions） | goal「読ませた資料の中の指示に、なぜ従ってしまうのか知りたい」 |
| agreement-is-not-evidence | symptom「Claude も賛成したのに、方針が間違っていた」（caves-when-pushed。R1-04・付表A の2） | goal「Claude の賛成を、方針が正しい根拠にしてよいか知りたい」 |
| decide-when-to-quit | symptom「微修正を続けているのに、いっこうに良くならない」（wont-rethink-approach・going-in-circles・stuck-in-a-check-loop） | goal「頭打ちになった方針を、続けるかやめるか決めたい」 |
| decide-when-to-quit | situation「Claude に「もう打ち手がない」と言われて、やめるか迷っている」（wont-rethink-approach） | goal「Claude の「もう打ち手がない」を、やめる根拠にしてよいか判断したい」 |
| postmortems | symptom「同じ種類の失敗を、注意しても何度も繰り返す」（going-in-circles の題名） | symptom「注意したのに、同じ種類の失敗が別の作業でまた起きた」 |
| learning-with-ai | symptom「AI に書かせたコードを、自分では説明できない」（verify の own-generated-code と同じ困りごと。k） | how-much-understanding-to-keep へ移した |
| outdated-advice-ledger | symptom「前は効いた書き方や設定が効かなくなった」（b） | goal「前は効いた書き方や設定を、今はどうすればよいか知りたい」 |
| outdated-advice-ledger | goal「「think hard」は効くのか」 | goal「「think hard」や「よく考えて」が効くのか知りたい」（models の thinking-keywords と同じ文。DR-15 の束ね） |
| dating-information | symptom「記事によって書いてあることが食い違う」（b） | goal「記事どうしで書いてあることが食い違うとき、どちらが新しい情報か見分けたい」 |
| checking-for-updates | symptom「記事の手順どおりにしても手元では動かない」（b） | goal「記事の手順が手元の版でも通じるか、自分で確かめたい」 |
| term-index | symptom「古い記事に出てくる機能の名前が、今の画面や文書に見当たらない」（b） | goal「古い記事に出てくる機能の名前から、今の名前を知りたい」 |

狭い場面として残したもの：why-hallucinations「聞き覚えのある名前について、中身をでっち上げる」（知っているつもりの誤作動が直接の答え）、checking-for-updates「公式の文書にある機能やコマンドが、手元では見つからない」（文書が手元の版より新しい場合）、agreement-is-not-evidence「自分の案を AI に見せると、たいてい褒められる」・「複数の AI にレビューさせて、全部が問題なしと答えた」、ask-without-sycophancy「「この方針で良いよね？」と聞くと、いつも同意される」、decide-when-to-quit「ここまで作ったので、今さら方針を変えられない」（人の側の固執で、症状のページにない）。

## 3. 別名の重なり（d）

外した別名（主のページは fix-aliases.md のとおり。主のページに今もその別名があることを確かめた）：

| ページ | 外した別名 | 主のページ |
| --- | --- | --- |
| how-thinking-works | 拡張思考 | effort-levels（models） |
| what-survives-compaction | 自動圧縮 | compact-and-auto-compact（context） |
| subagent-isolation | subagent | writing-subagents（extend） |
| why-prompt-caching | prompt caching | prompt-caching-in-practice（api） |
| how-much-understanding-to-keep | 認知負債 | own-generated-code（verify） |

- 外す側で残した別名はない（ほかの機能の公式の名前に当たるものがなかった）。
- 認知負債は、k で線引きが how-much-understanding-to-keep に来るので主を替えることも考えたが、材料（11 の p56#40「理解が追いつかないままコードが増える」）が「生成コードを自分のものにする」に置かれていて、verify の担当もそのまま残しているので、fix-aliases.md の主に従った。
- 受け持ちが主のページの別名（ステートレス・compaction・ツールの呼び出し・thinking・extended thinking・過度な一般化・要約の言い過ぎ・sycophancy・reward hacking・prompt injection・間接プロンプトインジェクション・自動化バイアス）はそのまま残した。
- d とは別に、lost-in-the-middle の別名（lost in the middle・位置の効果・U 字型の性能）と旧題名（中ほどの情報は使われにくい）を context-rot の aliases に移した（p）。

## 4. 外した前提（e）

- 推移的な前提の警告：受け持ちの4分野で、直しの前も後も0件。
- how-much-understanding-to-keep の前提から what-not-to-delegate を外し、related の先頭に移した。任せないものの一覧を読まなくても線引きは読める判断どうしの辺で（catalog/README §4.4 の1、R1-10）、own-generated-code がこのページを前提にすると鎖がさらに伸びるため。直しの前は6段・祖先11ページだった。delegate の担当が付表B の4本目（what-not-to-delegate → verifier-defines-problem）を関連に移したので、前提に残しても4段・祖先5ページになる。移した主な理由は、鎖の長さよりも「知らないと読めない」前提でないこと。移した後は4段・祖先4ページで、own-generated-code は5段・祖先5ページ。

## 5. まとめたページ・新しいページ・priority と level

- まとめた：basics の lost-in-the-middle（推奨・整える）を context-rot の節 `lost-in-the-middle`（level 整える）にした（merged に記録）。理由は R3-16（研究の紹介が本体で独自の判断がない。prompting の long-context-first も前提にしていなかった）。related を context-rot に移し（long-context-first・handing-long-documents・skipped-later-pages）、materials（00 §3 分野01・05 §3-4。研究者の個人の名前は書かなかった）も移した。context-rot は必須で第一波に入りうるので、節の分だけ第一波の中身が増える。
- 新しいページ：なし。
- priority と level を変えたページ：なし。

## 6. メインへ

1. **同じ語の日英で主が分かれる**：「extended thinking」は how-thinking-works（basics）、「拡張思考」は effort-levels（models）が主になっている（fix-aliases.md の見当の規則の結果）。用語索引で同じ機能の名前が別の主を持つので、どちらかにそろえるかを決めてほしい（effort-levels は「thinking のオンとオフ」も別名に持つ機能のページ）。
2. **b の新しい症状のページ**：「記事や前のやり方が通じない」は symptoms の担当が足す。受け持ちの notes（outdated-advice-ledger・dating-information・checking-for-updates・term-index・knowledge-cutoff）は題名で指している。その routes の行き先の案は outdated-advice-ledger・term-index#old-names・checking-for-updates・dating-information。id が決まったら、changes の4ページの related に足すかを決めてほしい（入ってくる道は routes でできるので、足さなくても検査は通る）。
3. **lost-in-the-middle を指す参照**：2026-11-04 の最後の検査で、ほかの分野のファイルに2件残る（symptoms の skipped-later-pages・forgets-in-long-chats の related）。app・context・prompting の担当は `context-rot#lost-in-the-middle` に直した。同じ形で直せる。
4. **k の sign の置き場所**：own-generated-code が困りごとの sign を外したので、「AI に書かせたコードを、自分では説明できない」を how-much-understanding-to-keep に置いた。own-generated-code に戻すなら、how-much-understanding-to-keep から外す。
5. **束ねるためにそろえた文**：outdated-advice-ledger の goal を models の thinking-keywords と、unfaithful-reasoning の goal を prompting の asking-for-reasoning と同じ文にした。相手の sign が変わったら、そろえ直しが要る。cli の command-cheatsheet の goal「古い記事に出てくるコマンドの、今の名前を知りたい」と term-index の goal「古い記事に出てくる機能の名前から、今の名前を知りたい」は近い。機能とコマンドで書き分けたままにしたが、1行に束ねるなら文をそろえる。
6. **x の段の逆転**：症状のページの前提を basics の概念にすると、出会う段で付け直した level より basics の前提が上の段になる組が出うる（例：rewrote-tests-to-pass を整えるにすると、前提の候補の reward-hacking は任せる）。受け持ちの level は変えていない。symptoms の担当から依頼があれば、DR-19 x として basics の level を見直す。
7. **見せ方（DR-17・R2-13）**：notes に「見せ方」を全ページ書くことは受け持ちの行になかったので、書いていない。受け持ちで見せ方がすでに決まっているのは ask-without-sycophancy（迎合の自己実験の検証ノート、11 第5節 A-7 の Before/After）と retros-without-ai-verdicts（Before/After の雛形）。メインが作る一覧の材料にできる。
8. **「要約の言い過ぎ」の主**：fix-aliases.md の更新（困りごとの言い方は症状のページを主にする）に照らすと、summary-overgeneralization（basics）が主の「要約の言い過ぎ」は困りごとの言い方とも読める。同じ原則にするなら、症状の summary-overstates-source を主にする案がある。今の表のとおり、受け持ちでは残した（外すと、symptoms の担当が表に従って外したときに引けなくなるため）。「過度な一般化」は用語なので basics のままでよい。

## 7. 検査の結果

`python3 tools/check_catalog.py --field <field>`（2026-11-04、最後に流した結果。ほかの担当が同時に書いているので、ページ数は流すたびに変わった）：

| 分野 | エラー | 警告 |
| --- | --- | --- |
| start | 0 | 0 |
| changes | 0 | 0 |
| basics | 0 | 0 |
| judgment | 0 | 0 |

- まとめたページ（lost-in-the-middle）を指す、ほかの分野のファイルの参照のエラー：2件（symptoms.yaml の skipped-later-pages・forgets-in-long-chats）。メインが後で直す
- 推移的な前提の警告：0件。残した警告：なし
- 全分野（`python3 tools/check_catalog.py`）では、最後に流したときエラー5件で、どれも symptoms.yaml の、まとめたページを指す参照（上の2件のほか、memory-faq・does-double-check-work・curb-sycophancy-and-overtrust）だった
- 途中で、team の担当がまとめる最中の「未処理の候補」の警告が受け持ちの5ページに出たが、まとめ先が決まったので参照を替えて消した

## 8. 確かめていないこと

- 新しい症状のページ（b）と、症状のページの routes（x）は、まだ symptoms の担当が書いていない。受け持ちの sign の書き換えは今の symptoms.yaml の signs と related で判断した。routes ができたら、振り分け先と言い換えの重なりを確かめ直す余地がある
- 言い換えは、2字の重なり・difflib の比と、症状のページの signs と related を目で照らして拾った。言葉の違う言い換えは見落としがありうる
- notes に書いた design の節（第2版の §3.3・§8.3・§8.5・§9.2・§10.2）は、D1 が書いている途中で、番号と中身を確かめきっていない
- 公式の教材（Academy）の講座の名前と数、「拡張思考」が公式の日本語版の訳語であることは、調査資料（research/06 §1・research/27 §3.1）によるもので、Web では確かめていない
- 「完成」の意味と、冒頭とフッターの非公式の文の言い方は、作者の承認の前の案である
