---
id: roadmap
title: ロードマップ（委任の段階別）
aliases: [学ぶ順, 何から読むか, 委任の段階, レベル, 使う・整える・任せる・仕組みにする・回す]
type: hub
field: start
chapter: 地図と道順
order: 80
priority: 必須
summary: 使う・整える・任せる・仕組みにする・回すの段階ごとに、次の段へ上がる条件と読むページの順が分かる。どの段階でも人が握るものを冒頭に示す。
signs:
  - {type: goal, text: 次にどこまで任せられるようになればよいか知りたい}
  - {type: goal, text: 何から順に読めばよいか知りたい}
  - {type: situation, text: 毎日使っているが、使いこなせている気がしない}
wave: 1
prerequisites: []
related: [four-principles, five-questions-before-delegating, what-not-to-delegate, default-safety-settings#by-stage, how-much-understanding-to-keep, human-pitfalls, verification-ladder, when-to-lock, knowledge-map, how-to-use#levels, glossary#definitions]
volatility: 低
sections:
  - {title: どの段階でも人が握るもの, anchor: always-hold}
  - {title: 五つの段階と上がる条件, anchor: levels}
  - {title: 段階ごとのページの列, anchor: reading-order}
  - {title: 段階は仮説である, anchor: hypothesis}
stage: draft
updated: 2026-11-05
sources: [simonwillison-ai-adoption-journey, arxiv-2607-05068, github-florianbruniaux-claude-code-ultimate-guide, github-luongnv89-claude-howto]
---

!!! abstract "要点"
    - **何ができるか**：次にどこまで任せてよいかを、5 つの段階と上がる条件で確かめ、読むページの順を引ける。
    - **いつ引くか**：次にどこまで任せられるようになればよいか知りたいとき。何から順に読めばよいか迷うとき。毎日使っているのに使いこなせている気がしないとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：学ぶ順・何から読むか・委任の段階・レベル・使う・整える・任せる・仕組みにする・回す
<!-- textlint-enable -->

ロードマップは、任せる幅の広がりを 5 つの段階に分け、段ごとに上がる条件と読むページの順を示す案内である。機能の難しさや使った期間ではなく、どこまで任せられるかで段を分ける。

## どの段階でも人が握るもの {#always-hold}

どの段階に進んでも、評価の定義・採否・撤退の判断・中核の理解の 4 つは人が握る。任せる幅が広がっても、この 4 つは Claude に渡さない。

- **評価の定義**：何をもって良い結果とするか。基準を Claude に決めさせると、出力が基準に合っているかを人が確かめられなくなる。
- **採否**：出てきた案を採るかどうか。案の出どころより、誰がどの評価で採ったかを記録に残す。
- **撤退**：続けるか、やめるか、巻き戻すか。
- **中核の理解**：自分が説明できなければならない部分。周辺は任せきりにしてよいが、中核は説明できるまで確かめる。

任せてよいものとの分け方は、出力を機械的に確かめられるかどうかである。詳しい線引きは <!-- link:begin what-not-to-delegate#what-humans-hold -->[任せないもの（評価・採否・撤退・中核の理解） › どの段階でも人が握るもの](../delegate/what-not-to-delegate.md#what-humans-hold)<!-- link:end --> にある。中核と周辺の分け方は <!-- link:begin how-much-understanding-to-keep#core-and-periphery -->どこまで理解を手放してよいか（中核と周辺） › 中核と周辺を分ける（準備中）<!-- link:end --> を引く。

段階が上がるほど、人が握るものを手放したくなる誘惑は強まる。人の側の崩れ方は <!-- link:begin human-pitfalls#five-pitfalls -->[人の側の五つの落とし穴（総論） › 五つの落とし穴の一覧](../judgment/human-pitfalls.md#five-pitfalls)<!-- link:end --> にまとまっている。段階ごとに足す安全の設定は、ここでは繰り返さず <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end --> を正本とする。

## 五つの段階と上がる条件 {#levels}

委任の段階は、使う・整える・任せる・仕組みにする・回すの 5 つである。各段の読者と、次の段へ上がる条件は次の表のとおりである。

| 段階 | この段階の読者 | 次の段へ上がる条件 | この段で強める確かめと縛り |
| --- | --- | --- | --- |
| 使う | 対話で頼み、返答を読んで使う | 期待外れの原因を「見えていない」か「散らかっている」かに言い分けられる | 返答を自分で読む |
| 整える | 頼み方・資料・会話の長さを整え、結果を確かめて直す | 完了の条件と確かめ方を、依頼に含めて渡せる | 依頼に確かめ方を書く（<!-- link:begin verification-ladder#four-steps -->[検証の階段 › 四つの段](../verify/verification-ladder.md#four-steps)<!-- link:end -->） |
| 任せる | 計画させてから任せ、長い作業を途中で舵取りする | 同じ注意を 2 回したら、仕組みに移すと判断できる | 判定役に見張らせる（<!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](../verify/verification-ladder.md#choose-step)<!-- link:end -->） |
| 仕組みにする | `CLAUDE.md`・スキル・フック・権限・MCP・プラグインで常設化し、共有する | 無人で動かす前の 5 つの問いに答えられ、検証器を自分で確かめられる | 頼んだ規則を鍵へ移す（<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end -->） |
| 回す | 並列・無人・定期・プログラムから動かす | （上限なし） | 段ごとに確かめと封じ込めを強める（<!-- link:begin five-questions-before-delegating#proportional-guards -->[任せ方の段階と、無人で走らせる前の五つの問い › 段ごとに強める確かめ方と封じ込め](../delegate/five-questions-before-delegating.md#proportional-guards)<!-- link:end -->） |

この段階は、読者が今どこまで任せているかを表す。作業ごとに決める「任せ方の段階」とは別のものである。作業ごとの段階は <!-- link:begin five-questions-before-delegating#autonomy-stages -->[任せ方の段階と、無人で走らせる前の五つの問い › 任せ方の段階](../delegate/five-questions-before-delegating.md#autonomy-stages)<!-- link:end --> が持つ。2 つの語の区別は <!-- link:begin glossary#definitions -->[用語集（独自の用語と公式の訳語） › 用語の定義](glossary.md#definitions)<!-- link:end --> に置いてある。

上がる条件は、段に入った直後ではなく、その段で身につけたことの確認である。条件を満たす前に上の段へ進むと、確かめる手段のないまま任せる幅だけが広がる。任せる幅を広げるほど確かめと封じ込めを強める考え方は、<!-- link:begin four-principles#proportional-rule -->[四つの原理と比例則（見せる・確かめる・縛る・握る） › 比例則](four-principles.md#proportional-rule)<!-- link:end --> にまとまっている。

自分の段の見当がつかないときは、困りごとから引くほうが早い。困りごとから引く道は <!-- link:begin how-to-use#lookup -->[この辞典の引き方 › 引き方（困りごと・やりたいこと・名前から）](how-to-use.md#lookup)<!-- link:end --> に、レベルの読み方は <!-- link:begin how-to-use#levels -->[この辞典の引き方 › レベル（委任の段階）](how-to-use.md#levels)<!-- link:end --> にある。

段階のはしごを 1 枚で見たいときは、ページの前提関係を図にした <!-- link:begin knowledge-map -->[知識マップ](knowledge-map.md)<!-- link:end --> を使う。

## 段階ごとのページの列 {#reading-order}

段階ごとのページの列は、各ページの level と前提から道具が作る。同じ段の中では、任せる幅を広げる内容のページより手前に、対応する守りのページが並ぶ。上から順に読めば、任せる幅を広げる順になる。

<!-- gen:begin roadmap -->
<!-- textlint-disable -->

### 使う {#reading-order-1}

1. [トークンとは](../basics/tokens.md)（基礎：なぜそうなるか）：Claude が文章を読み書きする単位であるトークンと、コンテキスト・費用・利用上限がトークンで決まることが分かる。
2. [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)（基礎：なぜそうなるか）：コンテキストウィンドウに入ることと中身をよく使えることは別で、関係のない情報が増えるほど大事な情報への注意が薄くなることが分かる。
3. [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)（基礎：なぜそうなるか）：Claude は毎回、会話の最初からすべてを読み直して返事をするので、長い会話ほど遅く重く、上限も早く使うことが分かる。
4. [context rot と紛らわしい情報](../basics/context-rot.md)（基礎：なぜそうなるか）：入力が長くなるほど、また似ているが違う情報が混ざるほど、答えの質が下がりやすいことが分かる。
5. [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)（基礎：なぜそうなるか）：分からないときも答えを作ってしまうのは、推測が得になる訓練と、知っているつもりの誤作動が重なるからだと分かる。
6. [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)（基礎：なぜそうなるか）：モデルの知識はある時点で止まり、今日の日付も知らないので、最近の出来事や新しい版について誤ることが分かる。
7. [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)（頼み方）：Claude は会話の外の事情を知らないものとして頼むと、依頼に何を書き足せばよいかが分かる。
8. [理由を添える](../prompting/give-reasons.md)（頼み方）：規則や依頼に理由を添えると、Claude は書いていない場面にも意図を当てはめられる。
9. [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)（頼み方）：分からなければ分からないと答えてよい、根拠のない所は推測と書け、と添えると、もっともらしい作り話が減る。
10. [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)（文脈を整える）：話題が変わったときや訂正を重ねても直らないときに、続けるか新しい会話にするかの分かれ目が分かる。
11. [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)（アプリを使いこなす）：添付した PDF や文書のどこまでが図も含めて読まれるかが分かり、大きな資料の分け方と、読まれたかの確かめ方を選べる。
12. [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)（Claude Code の基本操作）：/ でコマンドとスキルを呼び、! で自分でシェルを実行して結果を会話に入れ、@ でファイルを直接指し、Esc で作業を止めて方向を直す。
13. [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)（確かめる）：答えの中の事実を、根拠の引用・資料との照合・同じ質問の繰り返しで確かめられる。
14. [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)（安全とデータ）：送った会話やコードが学習に使われる条件と残る期間を、個人のプランと商用のプランに分けて確かめられる。
15. [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)（費用と利用上限）：アプリ・Claude Code・Desktop が同じ利用枠を分け合うことと、枠の種類と戻り方が分かる。
16. [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)（コンテストで使う）：主な大会の AI の規則を、類型（禁止・部門分け・許可と開示）・版・確認日・一次資料の所在で引ける。
17. [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)（症状辞典）：頼んだものと違う・平凡なものが出る原因を、伝えた情報の不足から順に切り分け、具体性・手本・質問させるのどれを足すかを決める。
18. [断られた・止められた](../symptoms/refused-or-blocked.md)（症状辞典）：正当な依頼が断られた・止められたときに、利用ポリシーの判定か、auto モード・フック・権限ルールの停止かを先に見分け、引き金と依頼の文脈のどちらが効いたかを切り分けて進め直す。
19. [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)（症状辞典）：もっともらしい嘘や存在しない出典を、見せた資料と確かめ方の不足から切り分け、引用・照合・「分からない」と言わせる手を選ぶ。
20. [最新の情報を知らない](../symptoms/doesnt-know-latest.md)（症状辞典）：最近の出来事や新しい版について間違える原因を知識の締め切りから切り分け、検索・公式の資料・日付の確かめ方のどれを使うかを決める。
21. [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)（症状辞典）：記事や本、前に覚えたやり方が通じないときに、その情報の日付と版を確かめ、撤回された助言か名前が変わっただけかを切り分けて、今のやり方に置き換えられる。
22. [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)（症状辞典）：添付した長い資料の後半や図が答えに使われない原因を、読み込みの範囲と注意の偏りから切り分け、分け方と、ページ番号付きの引用での確かめ方を決める。
23. [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)（症状辞典）：長い会話で前提を忘れ、答えが雑になる原因を、会話に溜まった無関係な情報から切り分け、新しい会話・引き継ぎ・委任のどれで片付けるかを決める。
24. [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)（症状辞典）：秘密（.env・API キー）を読まれた・会話や履歴に出たときに、まず鍵を無効にし、どの境界が欠けていたかを切り分けて、読ませない縛りを決める。
25. [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)（症状辞典）：利用上限に早く当たる原因を、会話の長さ・常駐するもの・モデルと effort・手戻りに分けて切り分け、節約より先に直すものを決める。
26. [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)（症状辞典）：返事が遅い・時間がかかりすぎる原因を、effort とモデル、文脈の重さ、面の違いに分けて切り分け、速さと質のどちらを優先するかを決める。

### 整える {#reading-order-2}

1. [エージェントループと tool use](../basics/agent-loop.md)（基礎：なぜそうなるか）：Claude は道具を使って文脈を集め、行動し、結果を確かめる輪を回し、確かめる手段がないと終わったように見えたところで止まることが分かる。
2. [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)（基礎：なぜそうなるか）：Claude が答える前にどれだけ考えるかを effort でどう変えられるかと、考えた分も出力として費用と上限に数えられることが分かる。
3. [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)（基礎：なぜそうなるか）：同じ頼み方でも答えが毎回少し変わるので、一回の結果で良し悪しを決められないことが分かる。
4. [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)（基礎：なぜそうなるか）：AI の要約は、原文の条件や限定を落として主張の範囲を広げがちだと分かる。
5. [迎合（sycophancy）](../basics/sycophancy.md)（基礎：なぜそうなるか）：利用者の考えに合う応答が好まれる形で訓練されるので、Claude も同意しやすく、押されると意見を変えやすいことが分かる。
6. [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)（基礎：なぜそうなるか）：システムプロンプト・会話の発言・CLAUDE.md やプロジェクトの指示が、それぞれコンテキストのどこに入り、どれだけ続いて効くかが分かる。
7. [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)（基礎：なぜそうなるか）：プロンプト・CLAUDE.md・スキルのような指示は Claude が読んで判断するお願いで、フック・deny ルール・管理設定は効く範囲と条件の中で毎回必ず効く鍵だと分かる。
8. [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)（基礎：なぜそうなるか）：読ませた Web ページやファイルの中の文も頼んだ指示と同じ文脈に並ぶので、Claude はデータと命令を確実には分けられないことが分かる。
9. [effort の段階と使い分け](../models/effort-levels.md)（モデル・effort・思考）：effort で、考える深さとツールの使い方・待ち時間・使用量の釣り合いを変えられる。
10. [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)（頼み方）：依頼に対象・状況・完了の形・倣う手本の 4 点を書くと、Claude が推測で埋める所が減り、意図とのずれが減る。
11. [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)（頼み方）：提案だけか、実行までか、懸念があれば止まって相談するのかを動詞で書き分けると、勝手に書き換えられることも提案で止まることも減る。
12. [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)（頼み方）：依頼に、やること・やらないこと・触ってよい範囲を書くと、頼んでいない機能や変更が増えにくくなる。
13. [長い資料は先、質問は最後](../prompting/long-context-first.md)（頼み方）：長い資料は依頼の先頭に置き、質問と指示を最後に書くと答えの質が上がる。
14. [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)（文脈を整える）：期待と違う返答には、訂正を重ねるより、前のメッセージを直して送り直すか巻き戻すほうがよい理由が分かる。
15. [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)（文脈を整える）：読むべきファイルを @ で直接指し、テストやログの長い出力は要点の数行に絞ってから会話に入れる。
16. [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)（アプリを使いこなす）：Claude への指示・プロジェクトの指示・メモリ・スキルを、効く範囲と読まれる時期で比べ、繰り返す前提や形式の指定をどこに置くかを決められる。
17. [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)（アプリを使いこなす）：アプリのメモリが何を、いつ、どの範囲で覚えるかが分かり、見る・直す・消す・止める手段を選べる。
18. [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)（アプリを使いこなす）：web 検索・リサーチ・拡張思考を、最新の情報が要るか、どれだけ広く調べるかで使い分けられる。
19. [権限モードの選び方](../cli/permission-modes-overview.md)（Claude Code の基本操作）：権限モードごとに何が確認なしで進むかを知り、作業の危うさと見ていられる度合いに合わせて選ぶ。
20. [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)（Claude Code の基本操作）：プロンプトごとの時点に、コード・会話・その両方を戻し、途中から要約もできる。
21. [git との付き合い方](../cli/working-with-git.md)（Claude Code の基本操作）：変更を小さく区切ってコミットし、コミットと push を人が握るか任せるかを段階で決める。
22. [「完了」を定義して渡す](../verify/define-done.md)（確かめる）：どのコマンドがどう返れば終わりか・変えてはならないもの・止まって報告する条件を決め、「完了」を測れる形で Claude に渡せる。
23. [報告ではなく証拠を求める](../verify/evidence-not-reports.md)（確かめる）：完了の報告を、実行したコマンドと生の出力と分母のそろった証拠で受け取れる。
24. [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)（安全とデータ）：アプリ・Claude Code・API の、権限・通信・データ・記録の既定を並べて比べられる。
25. [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)（安全とデータ）：読ませた Web ページ・ファイル・issue・道具の説明に仕込まれた指示に、Claude が従ってしまう経路と型が分かる。
26. [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)（判断と理解を守る）：AI と組むと人の判断が崩れる五つの型（預けすぎる・同意を根拠にする・やめられない・体感を信じる・みんなの案になる）と、意志に頼らず決まりと道具で防ぐ考え方が分かる。
27. [体感と実測](../eval/felt-vs-measured.md)（評価と実験）：速くなった・良くなった・劣化したという体感が、実測とずれる理由が分かる。
28. [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)（モデル・effort・思考）：劣化を疑ったとき、版と effort を記録して同じ課題を何度か流して比べ、体感でなく結果で確かめられる。
29. [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)（判断と理解を守る）：判断まで AI に預けると、もっともらしい誤りをそのまま採ってしまう理由と、どの判断を手元に残し、確かめる手間をどう下げるかが分かる。
30. [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)（判断と理解を守る）：Claude の賛成や、複数の AI レビュアーの一致が正しさの証拠にならない理由と、代わりに何を証拠として数えるかが分かる。
31. [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)（判断と理解を守る）：AI の案を起点にすると発想が似通う理由と、差が要る場面では AI の案を「ほかの人も得ている案」として扱い、上積みを自分で考える判断が分かる。
32. [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)（判断と理解を守る）：AI に書かせても速さの得は確かめられず、理解が残りにくいことと、生成の後に理解を確かめる、エラーは自分で直す、といった理解が残る使い方が分かる。
33. [上限を早く使う要因](../cost/what-uses-up-limits.md)（費用と利用上限）：長い会話の送り直し・大きな添付・ツール・effort・並列の作業など、利用枠を早く減らす原因と、自分の場合に何が使っているかの確かめ方が分かる。
34. [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)（費用と利用上限）：小手先の節約より、計画と確かめで手戻りを減らすほうが効く理由が分かる。
35. [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)（日本語で使う）：返答の言語・文体・表記を揃える手段を、届く範囲と強制力で選び分けられる。
36. [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)（日本語で使う）：英語のツール出力やサブエージェントの報告を読んだ後に英語へ戻る返答を、設定・指示・フックの組み合わせで減らす。
37. [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)（日本語で使う）：文体を一行で指定し、手本の文章を見せ、毎回読まれる場所に置くと揺れが減る。
38. [表記ゆれと漢字の開き](../japanese/consistent-notation.md)（日本語で使う）：用語の表記と漢字を開く語を一覧にして渡し、機械で見つけられる揺れは辞書つきの lint で直させる。
39. [バグを直す](../recipes/fix-a-bug.md)（用途別レシピ）：バグは、再現の手順と「直った」の定義を渡し、失敗するテストで再現させてから直させる。
40. [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)（症状辞典）：頼んでいない機能・ファイル・抽象化が増える原因を、範囲の伝え方と effort・モデルの選び方に分けて切り分け、範囲の指定と差分の確かめ方を決める。
41. [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)（症状辞典）：確認ばかりで進まない・途中で止まる原因を、提案か実行かの伝え方、権限モード、モデルと effort の癖に分けて切り分け、最後まで進めさせる手を選ぶ。
42. [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)（症状辞典）：こちらが押すとすぐ同意して答えを変える原因を切り分け、好みを伏せた聞き方と、同意を根拠に数えない確かめ方を選ぶ。
43. [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)（症状辞典）：誤りを指摘しても認めずに言い張るときに、言い争う代わりに実物（履歴・検索・実行結果）を見せて確かめ、会話を巻き戻すかを決める。
44. [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)（症状辞典）：存在しない関数・引数・パッケージを使われる原因を、読ませた資料と知識の古さから切り分け、読んでから書かせる手と、導入前の確かめ方を決める。
45. [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)（症状辞典）：要約が原文より断定的になったときに、落ちた条件や但し書きを原文と照らして見つけ、要約を信じてよい範囲を決める。
46. [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)（症状辞典）：同じ失敗を何度も繰り返す原因を、会話に残った失敗の跡から切り分け、訂正を重ねるか、巻き戻すか、学んだことを書いて新しく始めるかを決める。
47. [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)（症状辞典）：別の会話やプロジェクトの内容が混ざる・消したはずの内容を覚えている原因を、どの記憶の仕組みかから切り分け、範囲の分け方と消し方を決める。
48. [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)（症状辞典）：CLAUDE.md や指示に書いた規則が破られる原因を切り分け、書き方を直すか、どれを仕組みに移すかを決める。
49. [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)（症状辞典）：毎回同じ背景・手順・注意を説明している状態から、どれを置き場所（指示・プロジェクト・CLAUDE.md・スキル）に移し、どの注意を仕組みで縛るかを決める。
50. [英語で返ってくる](../symptoms/replies-in-english.md)（症状辞典）：日本語で頼んでいるのに英語で返る原因を、設定・読み込んだ英語の出力・モデル・面の順に切り分け、指示で足りるか仕組みで止めるかを決める。
51. [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)（症状辞典）：です・ますの混在や表記ゆれの原因を、指定の不足・資料の影響・縛りの有無に分けて切り分け、例示で足りるか lint で縛るかを決める。
52. [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)（症状辞典）：「完了」「全部通った」という報告が事実と違う原因を切り分け、完了の定義と証拠を渡す・別の者に確かめさせる、のどこから足すかを決める。
53. [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)（症状辞典）：読ませた Web ページやファイルに書かれた指示に従ってしまったときに、何を読ませ何を許していたかを切り分け、読ませ方と許す操作の組み合わせを決め直す。
54. [承認の確認が多すぎる・少なすぎる](../symptoms/wrong-amount-of-approvals.md)（症状辞典）：承認の確認が多すぎて読まずに押す、または少なすぎて怖いときに、権限モード・権限ルール・サンドボックスのどれを調整するかを、任せる段階に合わせて決める。
55. [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)（症状辞典）：急に賢くなくなった気がするときに、版・effort・モデル・会話の量の順に確かめ、体感ではなく同じ課題で比べて判断する。

### 任せる {#reading-order-3}

1. [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)（基礎：なぜそうなるか）：圧縮で会話が要約に置き換わるとき、そのまま効くもの・入れ直されるもの・必要になったら読み直されるもの・要約に溶けて消えるものの違いが分かる。
2. [サブエージェントは別室の部下](../basics/subagent-isolation.md)（基礎：なぜそうなるか）：サブエージェントは別のコンテキストで作業して要約だけを返すので本筋を散らかさずに済むが、賢くはならずトークンは余分にかかることが分かる。
3. [handoff 文書と document-and-clear](../context/handoff-documents.md)（文脈を整える）：目的と完了の条件・今の状態と根拠・試して駄目だったこと・次の一手を文書に書かせてから会話を新しくし、その文書から再開する。
4. [/context で中身を見る](../context/inspect-context.md)（文脈を整える）：/context の内訳から、会話・読み込んだファイル・常駐するもののどれが場所を取っているかを見分け、片付け方を選ぶ。
5. [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)（文脈と指示を仕組みにする）：常に効かせる規則・フォルダごとの規約・場面ごとの手順・応答の形を、どこに置くかを選べる。
6. [検証の階段](../verify/verification-ladder.md)（確かめる）：完了の確かめを、依頼に書く・判定役に見張らせる・フックで終了を止める・書いていない者に確かめさせる、の段から任せる幅に応じて選べる。
7. [書いた本人ではない者にレビューさせる](../verify/independent-review.md)（確かめる）：変更を生んだ推論を見ていない者（新しいセッション・サブエージェント・別の人）にレビューさせる理由と分け方が分かる。
8. [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)（評価と実験）：Claude は渡された検証器（テスト・採点・ベンチマーク）が定める問題を解き、置かれたループを何でも速めることが分かる。
9. [採点器を騙す（reward hacking）](../basics/reward-hacking.md)（基礎：なぜそうなるか）：採点の仕組みに抜け道があると、目的ではなく採点を満たす方向に解かれることがあると分かる。
10. [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)（確かめる）：Claude がテストや採点を書き換えて通すのを、依頼・差分のレビュー・ファイルの鍵・見せないデータの層で防げる。
11. [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)（評価と実験）：CLAUDE.md・プロンプト・スキルの変更が効いたかを、失敗したタスクを前後で何度か走らせて比べる小さな eval で確かめられる。
12. [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)（評価と実験）：検証器が満たすべき三つの条件（正しい・書き換えられない・本番を代表する）で、評価の仕組みを使う前に点検できる。
13. [お願いを鍵に移す判断](../enforce/when-to-lock.md)（仕組みで縛る）：頼んだ規則のうち、どれを権限ルールやフックに移すかを判断できる。
14. [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)（仕組みで縛る）：許可・確認・拒否のルールで、Claude が使える道具とファイルを決められる。
15. [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)（文脈を整える）：圧縮のあとも守らせたい決めごとを、圧縮の後に読み直される CLAUDE.md や計画のファイルに書き、例外を許さないものはdeny ルールやフックに移す。
16. [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)（文脈と指示を仕組みにする）：CLAUDE.md に残す行と外す行を見分け、外す行の移し先を決められる。
17. [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)（仕組みで縛る）：auto モードの分類器が既定で止める操作と、すり抜けうる操作を知り、権限ルールやサンドボックスで補うものを決められる。
18. [サンドボックスで封じ込める](../enforce/sandboxing.md)（仕組みで縛る）：サンドボックスで、Claude が動かすコマンドの読み書きと通信を OS の層で囲える。
19. [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)（安全とデータ）：信頼できない入力・秘密や私的なデータ・外への送信や変更の三つを一つの構成に同時に持たせないことで、仕込まれた指示が被害につながる経路を断てる。
20. [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)（安全とデータ）：.env や API キー、認証情報を Claude に読ませない設定を、権限ルールとサンドボックスの二重にして作れる。
21. [MCP をつなぐ](../extend/connecting-mcp.md)（文脈と指示を仕組みにする）：外部のサービスやツールを MCP でつなぎ、共有の範囲と資格情報を決め、つながらないときは切り分けられる。
22. [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)（安全とデータ）：MCP サーバー・プラグイン・スキルや依存のパッケージを入れる前に、出所・持つ権限・中身（道具の説明やスクリプト）を確かめられる。
23. [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)（文脈を整える）：CLAUDE.md の全文・スキルの説明・MCP のツールの一覧など、毎回のリクエストに乗るものの費用が分かり、必要なときだけ読ませる形に移せる。
24. [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)（文脈と指示を仕組みにする）：CLAUDE.md や /init の叩き台を、行ごとに残すか削るかを判断して短く保てる。
25. [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)（安全とデータ）：取り返しのつかない削除や書き換えが起きる経路と、巻き戻しで戻らないものが分かり、消されたくないものを権限ルール・サンドボックス・バックアップで守れる。
26. [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)（任せて並べる）：評価の定義・採否・撤退・中核の理解など、どの段階でも人が握るものと、任せてよいものの分け方が分かる。
27. [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)（判断と理解を守る）：費やした分だけ方針を捨てにくくなる傾向に対し、やめる基準を着手前に書き、作った本人以外が判定して守る方法が分かる。
28. [レビューのボトルネックと疲労](../team/review-bottlenecks.md)（組織・チームで使う）：AI で変更が増えると、レビューと動作確認が人に積もって詰まり、疲れも溜まりやすい理由が分かる。
29. [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)（症状辞典）：圧縮の後に、会話で決めた約束や禁止を忘れる原因を切り分け、圧縮で残る場所に移すか、仕組みで縛るかを決める。
30. [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)（症状辞典）：テストの書き換えや特例の分岐で通されたときに、何が書き換えられる状態だったかを切り分け、テストの保護と一般解の求め方を決める。
31. [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)（症状辞典）：手元の評価は良いのに本番で通用しないときに、評価の仕組みが正しいか・書き換えられないか・本番を代表するかを切り分ける。
32. [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)（症状辞典）：実行と確認を繰り返すだけで進まないループを見分け、新しい仮説や情報を入れるか、止める条件を決めるか、新しい会話に移すかを選ぶ。
33. [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)（症状辞典）：エラーを直し続けて方針を疑わない、または早々に撤退を勧めるときに、続けるかやめるかを AI の勧めでなく、先に決めた基準と測った上界で決める。
34. [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)（症状辞典）：「環境や道具が壊れた」と言い出したときに、本当に壊れたのか、長い作業の劣化の兆しなのかを自分で確かめて切り分け、続けるか新しく始めるかを決める。
35. [消してはいけないものを消された](../symptoms/deleted-something-important.md)（症状辞典）：消してはいけないファイルや履歴を消されたときに、戻せる手段を先に確かめて復旧し、何が止められなかったかを切り分けて再発を防ぐ。

### 仕組みにする {#reading-order-4}

1. [スキルの作り方](../extend/writing-skills.md)（文脈と指示を仕組みにする）：繰り返す手順をスキルにして、Claude にも自分にも呼べるようにできる。
2. [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)（評価と実験）：検証器を使う前に、何もしない解が負け、強い解が勝ち、手で計算した値と一致し、わざと壊した検証器では落ちることを確かめてから凍結できる。
3. [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)（評価と実験）：Claude が正直でも、良かった版を選び続けるだけで評価の穴に合わせ込んでしまう罠が分かる。
4. [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)（評価と実験）：実験ごとに、実行前に書く仮説・提案者・分母・検証器の版・採否と判定者を台帳に残せる。
5. [フックの考え方とイベント](../enforce/hooks-basics.md)（仕組みで縛る）：フックで、決まったきっかけに必ずスクリプトを走らせ、規則を確実に守らせる仕組みが分かる。
6. [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)（仕組みで縛る）：PreToolUse のフックで操作を止め、理由と代わりの手段を Claude に返せる。
7. [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)（任せて並べる）：作業をどこまで任せるか（対話・計画の承認・停止条件つきの反復・隔離した無人実行）の段階と、無人で走らせる前に答える五つの問いが分かる。
8. [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)（任せて並べる）：完了の条件を満たすまで Claude にターンを続けさせ、席を外している間も作業を進められる。
9. [並列の上限は人間が決める](../delegate/humans-set-the-parallel-limit.md)（任せて並べる）：並列の本数を決めるのはマシンや予算ではなく、結果をレビューする人の帯域だと分かる。
10. [並列の方式の選び方](../delegate/choosing-parallel-modes.md)（任せて並べる）：並列の方式を、誰が調整するか・同じファイルを触るか・互いに連絡が要るかで選べる。
11. [textlint をフックで回す](../japanese/textlint-hook.md)（日本語で使う）：ファイルを書いた直後に textlint を走らせ、残った違反を Claude に返して直させる。

### 回す {#reading-order-5}

1. [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)（症状辞典）：並列で任せたら疲れた・レビューが追いつかないときに、並べる数・確かめ方・体感のずれのどれが原因かを切り分け、並列の上限と人が読む範囲を決め直す。

<!-- textlint-enable -->
<!-- gen:end roadmap -->

「回す」の段には、今は読むページの列がない。上の段のページを読み終えた人が、<!-- link:begin five-questions-before-delegating#five-questions -->[任せ方の段階と、無人で走らせる前の五つの問い › 無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md#five-questions)<!-- link:end --> に答えられるかを確かめてから進む。

この列はカリキュラムではない。「使う」のページは少なく短く、「整える」から「仕組みにする」までを厚くしてある。すでに知っている段は飛ばしてよい。

## 段階は仮説である {#hypothesis}

5 つの段階と上がる条件は、この辞典の仮説である。段階的に任せる範囲を広げる進め方を直接検証した査読研究は、確かめた範囲では見当たらない。

見当たらないことが、段階が誤りだということではない。隣り合う分野の結果と実践者の報告は、この考え方に沿っている。

- ある実践者は、導入の初期に同じ作業を自分とエージェントの両方で行って結果を比べ、確実にこなせる仕事から任せていった（根拠：弱）。
- 入門のプログラミング科目（CS1）の受講生 917 人を対象にした研究では、ほぼ正しい AI の解に現実的なバグを入れると、学生はコードを直接読んで直す傾向が増えた（根拠：中・類推）。AI の出力を読んで確かめる力が、任せる前提になりうることを示す。
- 既存の学習案内は、使った期間や機能のまとまりで段を分けている。この辞典は、次にどこまで任せられるかを軸にした。

AI を使わない地力と、AI を使いこなす力を並走させる点も、段の節目に添える程度の補助線である（根拠：弱）。任せるほど確かめる力が衰えうる問題は <!-- link:begin how-much-understanding-to-keep#supervision-paradox -->どこまで理解を手放してよいか（中核と周辺） › 確かめる力が衰える（監督のパラドックス）（準備中）<!-- link:end --> で扱う。

仮説なので、自分の記録で確かめて使う。条件を満たしたつもりで上の段へ進んだあとに、確かめの漏れが見つかったら、1 段下の段階に戻してよい。段を戻す合図は <!-- link:begin five-questions-before-delegating#back-to-dialogue -->[任せ方の段階と、無人で走らせる前の五つの問い › 対話に戻す合図](../delegate/five-questions-before-delegating.md#back-to-dialogue)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Mitchell Hashimoto: My AI Adoption Journey](https://simonwillison.net/2026/Feb/5/ai-adoption-journey/)：Simon Willison・英語・確認日 2026-11-04
- [When AI Is Wrong on Purpose: How Students Respond to Buggy GenAI Code](https://arxiv.org/abs/2607.05068)：arXiv（Pădurean, Victor-Alexandru ほか）・英語・確認日 2026-11-04
- [claude-code-ultimate-guide: guide/learning-path/README.md](https://raw.githubusercontent.com/FlorianBruniaux/claude-code-ultimate-guide/693d97d284ea342c8c8fb13894df0cee26d3a3d3/guide/learning-path/README.md)：GitHub（FlorianBruniaux）・英語・確認日 2026-11-04
- [luongnv89/claude-howto: A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.](https://github.com/luongnv89/claude-howto)：GitHub（luongnv89）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)
- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)
- どこまで理解を手放してよいか（中核と周辺）（準備中）
- [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)
- [検証の階段](../verify/verification-ladder.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [知識マップ](knowledge-map.md)
- [この辞典の引き方 › レベル（委任の段階）](how-to-use.md#levels)
- [用語集（独自の用語と公式の訳語） › 用語の定義](glossary.md#definitions)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
