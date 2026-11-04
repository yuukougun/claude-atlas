---
id: glossary
title: 用語集（独自の用語と公式の訳語）
nav_title: 用語集
aliases: [用語の定義, 訳語の対応, 表記の約束, 表記の正規形, 独自の用語]
type: guide
field: start
chapter: 辞書として引く
order: 60
priority: 必須
summary: この辞典の独自の用語（お願いと鍵・六つの「ない」など）の意味と公式の用語との対応、公式の日本語版に合わせた訳語と表記の正規形を引ける。
signs:
  - {type: goal, text: この辞典の言葉が、公式の文書のどの言葉に当たるか知りたい}
  - {type: goal, text: アプリと Claude Code で名前が同じ機能が、同じものか知りたい}
wave: 1
prerequisites: []
related: [term-index, how-to-use, four-principles, six-causes, request-vs-lock, roadmap, five-questions-before-delegating#autonomy-stages, how-memory-works, using-auto-memory, skills-in-the-app#migrated-styles, output-style-modes]
volatility: 中
sections:
  - {title: 訳語の決め方, anchor: translation-policy}
  - {title: 独自の用語と公式の用語, anchor: own-terms}
  - {title: 公式で表記が割れている語, anchor: split-terms}
  - {title: 表記の正規形, anchor: notation}
  - {title: 面ごとに似た名前の機能, anchor: same-names-across-surfaces}
  - {title: 用語の定義, anchor: definitions}
  - {title: モデルの性質の語, anchor: model-terms}
  - {title: 安全と拡張の語, anchor: safety-terms}
  - {title: 評価の語, anchor: eval-terms}
  - {title: 機能と利用の語, anchor: product-terms}
  - {title: 学びと表記の語, anchor: human-terms}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：この辞典の独自の用語と、公式の日本語版に合わせた訳語・表記を引ける。
    - **いつ引くか**：辞典の言葉が公式の文書のどの言葉に当たるか知りたいとき。アプリと Claude Code で名前が同じ機能は同じものかを知りたいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：用語の定義・訳語の対応・表記の約束・表記の正規形・独自の用語
<!-- textlint-enable -->

用語集は、この辞典が使う言葉の意味と、公式の用語との対応を 1 か所にまとめたページである。表記の揺れを検査する prh の元にもなる。語は表から引く。長い説明は、各語の持ち主のページに任せる。辞典独自の呼び名は「独自の用語と公式の用語」、訳語の迷いは「公式で表記が割れている語」と「表記の正規形」、アプリと Claude Code の取り違えは「面ごとに似た名前の機能」を見る。そのほかの語は「用語の定義」以降の表にある。

## 訳語の決め方 {#translation-policy}

訳語は、公式の日本語版の本文で多数派の表記に合わせる。読者が公式の文書とこの辞典を行き来しやすく、表記の検査もしやすいからである。

- 公式の日本語版は、Claude Code の文書・Platform の文書・ヘルプセンターのそれぞれにある。同じ語でも、文書ごとに訳が異なることもある。
- 本文の多数派がはっきりしている語は、多数派に揃える。表記の対応は「表記の正規形」にまとめた。
- 公式の中で割れている語だけ、この辞典で決める。決め方は「公式で表記が割れている語」に書いた。
- 機能名・コマンド・ファイル名・設定のキーは、原文のまま書く。
- 訳した語の初出には、英語を添えることがある。例は「圧縮（compaction）」である。
- API の機能名は、Platform の日本語版の訳語を確かめるまで英語のまま書く。例外はプロンプトキャッシングで、Claude Code の日本語版の多数派に合わせる。
- 独自の用語は、独自の言葉を見出しにし、公式の言葉を併記する。

## 独自の用語と公式の用語 {#own-terms}

この辞典が付けた呼び名と、辞典の読み方の語である。公式の文書にある別の言い方があるときは、右の欄に添える。

| 語 | 意味 | 公式の用語・備考 |
| --- | --- | --- |
| <span id="request-lock"></span>お願い・鍵 | お願いは、Claude が読んで判断する指示（プロンプト・CLAUDE.md・スキル）で、守られる保証がない。鍵は、Claude の判断によらずハーネスが実行する制御（フック・deny ルール・管理設定）で、効く範囲と条件の中では毎回必ず効く | お願い＝非決定論的な指示、鍵＝決定論的な制御。解説は <!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end --> |
| <span id="four-principles"></span>4 つの原理・比例則 | うまくいかない理由と次の一手を考える 4 つの原理（見せる・確かめる・縛る・握る）と、任せる幅を広げるほど確かめる仕組みと封じ込めを強める比例則 | 公式の Best practices の考え方を整理し直した。「握る」はこの辞典が足した。解説は <!-- link:begin four-principles -->[四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)<!-- link:end --> |
| <span id="six-nai"></span>6 つの「ない」 | うまくいかないときの、Claude 側の 6 つの原因の呼び名。安く確かめられる順に問う | 人の側の 5 つの落とし穴と対にする。解説は <!-- link:begin six-causes -->[失敗の二つの軸と診断の入口](six-causes.md)<!-- link:end --> |
| <span id="four-specifics"></span>具体性の 4 点 | 依頼に書く対象・状況・完了の形・倣う手本の 4 点。欠けている点が、次に書き足すものになる | 公式の Best practices の助言（ファイルの名指し・症状・直った状態の先出し・倣うパターンの指定）を、この辞典が 4 点にまとめた呼び名 |
| <span id="workaround"></span>回避策 | 原理を満たす正式な仕組みやモデルの力が足りない間に、言葉・手順・自作のスクリプトで補った手段。仕組みが入るか、モデルが言われなくてもできるようになると役目を終える | 古くなった助言の台帳で、行ごとに「どの原理の回避策だったか」を添える |
| <span id="ledger-states"></span>台帳の状態（撤回・置換・条件付き） | 撤回は、使えないか使わないほうがよい助言。置換は、同じ目的を別の正式な仕組みや新しい名前が担うもの。条件付きは、今も効くが前提が変わったもの | 本文の定義は <!-- link:begin outdated-advice-ledger -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md)<!-- link:end --> を正とする |
| <span id="level"></span>レベル（委任の段階） | ページが想定する読者の段階（使う・整える・任せる・仕組みにする・回す）。ページの段階とは別のもの | フロントマターの `level`。段階ごとの読み順は <!-- link:begin roadmap -->[ロードマップ（委任の段階別）](roadmap.md)<!-- link:end --> |
| <span id="autonomy-stage"></span>任せ方の段階 | 1 つの作業をどこまで任せるか（対話・計画の承認・停止条件つきの反復・隔離した無人実行）。読者の段階であるレベルとは別のもの | 解説は <!-- link:begin five-questions-before-delegating#autonomy-stages -->[任せ方の段階と、無人で走らせる前の五つの問い › 任せ方の段階](../delegate/five-questions-before-delegating.md#autonomy-stages)<!-- link:end --> |
| <span id="surface"></span>面 | Claude を使う入口の種類（アプリ・Claude Code・API）。同じ目的でも、面によって手段が違う | 公式では surfaces、またはプロダクト名で呼ぶ |
| <span id="evidence-mark"></span>根拠の印 | 研究や数値を根拠にする主張の後に付ける印（根拠：強・中・弱、類推、推論・実践例なし） | 読み方は <!-- link:begin how-to-use#evidence -->[この辞典の引き方 › 根拠の強さの書き分け](how-to-use.md#evidence)<!-- link:end --> |
| <span id="coming-soon"></span>題名（準備中） | まだ公開していないページを指す所に、リンクにせず出す表記。相手を公開すると、リンクに変わる | |
| <span id="page-stage"></span>ページの段階 | ページの書き進み具合（骨格・下書き・検証済み・完成）。レベルとは別のもの | フロントマターの `stage`。読み方は <!-- link:begin how-to-use#stage -->[この辞典の引き方 › 段階・下書きの帯・「準備中」の題名](how-to-use.md#stage)<!-- link:end --> |
| <span id="symptom-page"></span>症状のページ | 困りごと（例：指示が守られない）から引く型のページ。原因を安く確かめる順に並べ、直し方のページへ送る | 型 `symptom` |
| <span id="field"></span>分野 | ナビゲーションの大きな区分 | フロントマターの `field` |
| <span id="chapter"></span>章 | 分野の中の区切り。症状のページだけを章ごとに並べた分野が「症状辞典」である | フロントマターの `chapter` |

## 公式で表記が割れている語 {#split-terms}

公式の日本語版の中で表記が割れ、多数派を 1 つに決めにくい語である。この辞典は本文で英語のまま書き、日本語の訳は別名に置く。日本語の訳で検索した読者も、ページに着ける。

<!-- textlint-disable prh -->
| 本文の表記 | 公式の日本語版の表記 | 別名に置く訳 |
| --- | --- | --- |
| plan mode | Claude Code の文書は plan モードが多数派で、プランモードも混ざる。ヘルプセンターはプランモード | plan モード・プランモード |
| effort | Claude Code の文書は effort が多数派。ヘルプセンターは努力レベル・努力 | 努力レベル・努力 |
| allow ルール・ask ルール・deny ルール | Claude Code の文書は許可ルール・確認ルール・拒否ルールが多数派。「deny ルール」なども少数ある | 許可ルール・確認ルール・拒否ルール |
<!-- textlint-enable prh -->

アプリの画面の項目名が effort のままか「努力」かは、画面を見て確かめていない。

## 表記の正規形 {#notation}

本文で使う表記の正規形と、公式の英語との対応である。表記の揺れは prh が見つける。

<!-- textlint-disable prh -->
| 英語 | 本文の表記 | 備考 |
| --- | --- | --- |
| subagent | サブエージェント | 組み込みサブエージェント、カスタムサブエージェント |
| hooks | フック | イベント名と matcher は英語のまま |
| skills | スキル | |
| plugins・marketplace | プラグイン・マーケットプレイス | |
| permissions・permission mode | 権限・権限モード | |
| sandbox | サンドボックス | |
| auto mode | auto モード | オートモード・auto mode とは書かない |
| compaction・auto-compact | 圧縮・自動圧縮 | 初出に compaction を添える。API の機能名 compaction は英語のまま |
| context window | コンテキストウィンドウ | |
| output style | 出力スタイル | 初出に output style を添える |
| memory・auto memory | メモリ・自動メモリ | アプリのものと分けるときは「アプリのメモリ」 |
| agent teams・teammate | エージェントチーム・チームメイト | |
| extended thinking | 拡張思考 | |
| prompt caching | プロンプトキャッシング | API の機能名の中で、日本語にする唯一の例外 |
| managed settings | 管理設定 | |
| checkpoint | チェックポイント | |
| worktree | worktree | 英語のまま |
| non-interactive mode | 非対話モード | |
| classifier | 分類器 | |
| system prompt・frontmatter | システムプロンプト・フロントマター | |
| acceptEdits | acceptEdits モード | 設定の値は原文のまま |
<!-- textlint-enable prh -->

アプリの機能の名前は、次の日本語で書く。プロジェクト・メモリ・シークレットチャット・アーティファクト・リサーチ・コネクタ・スキル・音声モード。「Claude への指示」と「プロジェクトの指示」の画面の名前は、確かめていない。

## 面ごとに似た名前の機能 {#same-names-across-surfaces}

名前が似ていても、面が違うと別の機能のことが多い。次の組は、混同しないよう分けて書く。

| 名前 | Claude Code | アプリ・API |
| --- | --- | --- |
| メモリ | CLAUDE.md と、Claude が自分で書き溜める自動メモリ | アプリのメモリ。会話から覚え、見る・直す・消す・止める手段がある |
| 出力スタイル／Styles | 出力スタイル：セッション全体の役割・口調・応答の形を変える指示 | Styles：応答の調子と形式を選ぶ機能。スキルへの移行が告知されている |
| プロジェクト | Claude Code の Projects（並列の threads） | アプリのプロジェクト（資料と指示をまとめて置く場所） |
| 音声 | `/voice` の音声入力 | アプリの音声モード |
| タスク | scheduled tasks（定期実行） | アプリのタスクと定期タスク |
| スキル・プラグイン | Claude Code のスキルとプラグイン | アプリのスキルとプラグイン。入れる画面と手順が別 |
| 権限モード | 権限モード（auto モードを含む） | アプリの権限モード。設定の場所と既定が違う |
| バッチ | `/batch`（多数のファイルに同じ作業を流す） | Message Batches API（急がない大量の処理） |
| 圧縮 | Claude Code の圧縮（compaction） | API の compaction |

見る先は次のとおり。

- メモリ：<!-- link:begin how-memory-works -->[アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)<!-- link:end -->・<!-- link:begin using-auto-memory -->自動メモリ（準備中）<!-- link:end -->
- 出力スタイル／Styles：<!-- link:begin output-style-modes -->出力スタイルで応答の仕方を切り替える（準備中）<!-- link:end -->・<!-- link:begin skills-in-the-app#migrated-styles -->アプリでスキルを使う › 移された Styles（準備中）<!-- link:end -->
- プロジェクト：<!-- link:begin using-projects -->[プロジェクトの使いどころ](../app/using-projects.md)<!-- link:end -->
- 音声：<!-- link:begin voice-and-mobile -->音声モード・Quick entry・モバイル（準備中）<!-- link:end -->
- タスク：<!-- link:begin tasks-and-schedules-in-the-app -->[タスクと定期タスク（Cowork）](../app/tasks-and-schedules-in-the-app.md)<!-- link:end -->・<!-- link:begin loop-and-scheduling -->/loop と定期実行の方式（準備中）<!-- link:end -->
- スキル・プラグイン：<!-- link:begin skills-in-the-app -->アプリでスキルを使う（準備中）<!-- link:end -->・<!-- link:begin plugins-in-the-app -->アプリでプラグインを使う（準備中）<!-- link:end -->
- 権限モード：<!-- link:begin permission-modes-overview -->[権限モードの選び方](../cli/permission-modes-overview.md)<!-- link:end -->・<!-- link:begin permission-modes-in-the-app -->[アプリの権限モード（Auto と Manual）と安全](../app/permission-modes-in-the-app.md)<!-- link:end -->
- バッチ：<!-- link:begin batch-and-p-loops -->多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）<!-- link:end -->・<!-- link:begin batch-api-basics -->Message Batches API（急がない大量の処理）（準備中）<!-- link:end -->
- 圧縮：<!-- link:begin what-survives-compaction -->[圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)<!-- link:end -->

出力スタイルと Styles は、特に取り違えやすい。2 つは別の機能で、片方の手順をもう片方に当てはめない。

## 用語の定義 {#definitions}

本文で使う語のうち、独自でなく、意味を決めておくと迷う語である。

| 語 | 意味 | 備考 |
| --- | --- | --- |
| <span id="harness"></span>ハーネス | モデルのまわりでツールを動かし、モデルが見る文脈を管理する層。Claude Code 本体がこれにあたる | |
| <span id="output-style"></span>出力スタイル | Claude Code で、セッション全体の役割・口調・応答の形を変える指示 | claude.ai の Styles とは別の機能 |
| <span id="fork"></span>fork | 親の会話とシステムプロンプトを丸ごと引き継いで分かれるサブエージェント。出力スタイルが効く | |
| <span id="managed-settings"></span>管理設定 | 組織が配り、利用者のファイルでは上書きできない設定 | 表記は prh に従い「管理設定」 |
| <span id="compaction"></span>圧縮 | 長い会話を要約に置き換えること | API の機能名 compaction は英語のまま |
| <span id="resident"></span>常駐 | 読み込まれた後、会話の間コンテキストに居続けること | |
| <span id="bypass"></span>回り込み | 鍵で止められた操作の代わりに、止められていない別の手段で同じ結果を得ること | 縛りすぎの害の一つ |
| <span id="turn"></span>ターン | 依頼を送ってから最後の返事までの 1 区切り。途中でツールを何度も呼ぶ | |
| <span id="aside"></span>ツールの合間の一言 | Claude がツールを呼ぶ前後に書く短い文。最後の返事とは別で、Stop フックは見ない | |
| <span id="block-back"></span>差し戻し | フックが Claude に返事のやり直しを求め、ターンを終えさせないこと | `decision` を `block` にする形 |
| <span id="supporting-files"></span>補助ファイル | スキルのフォルダの中で `SKILL.md` 以外に置く資料やスクリプトのファイル。資料は Claude が読むまでコンテキストに入らない。スクリプトは、読ませずに実行だけさせる | 公式の英語の呼び名は、スクリプトも含む。この辞典の <!-- link:begin writing-skills -->[スキルの作り方](../extend/writing-skills.md)<!-- link:end --> は、資料とスクリプトを分けて書く |

## モデルの性質の語 {#model-terms}

Claude の出力の信頼性を考えるときの語である。

| 語 | 意味 | 備考 |
| --- | --- | --- |
| <span id="jagged-frontier"></span>能力の凸凹（jagged frontier） | 人には易しく見える課題でつまずき、難しく見える課題をこなすことがある。得意と不得意の境が一様でない性質 | 解説は <!-- link:begin over-reliance -->[判断を預けすぎる（過度依存）](../judgment/over-reliance.md)<!-- link:end --> |
| <span id="hallucination"></span>ハルシネーション | もっともらしいが事実でない内容を出すこと。分からない問いにも答えたほうが得な採点では、山を張る受験生のように推測で埋めやすい | 解説は <!-- link:begin why-hallucinations -->[ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)<!-- link:end --> |
| <span id="nondeterminism"></span>非決定性（nondeterminism） | 同じ依頼を出し直しても、答えが毎回同じとは限らない性質。1 回の成否だけで効き目を決めない理由になる | 評価では複数回の試行で見る。解説は <!-- link:begin measure-changes -->[変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)<!-- link:end --> |
| <span id="training-data-cutoff"></span>training data cutoff | 学習データに含まれる最後の時期 | 次の reliable knowledge cutoff とは別の概念 |
| <span id="reliable-knowledge-cutoff"></span>reliable knowledge cutoff | モデルが確かな知識を持つと見なせる時期。最近の出来事は学習データに薄いので、training data cutoff より前になりうる | 2 つの区別は <!-- link:begin knowledge-cutoff -->[知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)<!-- link:end -->。症状の側は <!-- link:begin doesnt-know-latest -->[最新の情報を知らない](../symptoms/doesnt-know-latest.md)<!-- link:end --> |
| <span id="postmortem"></span>ポストモーテム（事後報告） | 障害や品質低下のあとに、提供側が原因と対応を書いた報告 | モデルが劣化したと疑うときの確かめ方は <!-- link:begin suspected-degradation -->[劣化を疑ったら測って確かめる](../models/suspected-degradation.md)<!-- link:end --> |
| <span id="system-prompt"></span>システムプロンプト | 会話の前に渡される、役割や決まりを書いた指示。利用者が毎回書く依頼とは別 | 新しい同僚に頼む気持ちで書く、と考える。解説は <!-- link:begin brief-a-new-colleague -->[新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)<!-- link:end --> |

## 安全と拡張の語 {#safety-terms}

読ませた資料や入れた拡張から起きる問題の語である。攻撃の手順は書かず、何を指す語かだけを示す。

| 語 | 意味 | 備考 |
| --- | --- | --- |
| <span id="prompt-injection"></span>prompt injection | 読ませた資料に紛れた文が、Claude の行動を変えてしまうこと。資料の中の文は指示でなくデータとして扱う | 解説は <!-- link:begin data-vs-instructions -->[データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)<!-- link:end --> |
| <span id="tool-poisoning"></span>tool poisoning | ツールの説明文に、利用者から見えない指示が仕込まれていること | 入れる前の確かめ方は <!-- link:begin vetting-extensions -->[MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)<!-- link:end --> |
| <span id="rug-pull"></span>rug pull | 入れたときは無害だった拡張が、あとで中身を差し替えられること | 入れる前の確かめ方は tool poisoning の行と同じ |
| <span id="slopsquatting"></span>slopsquatting | AI が実在しないパッケージ名を作り出す傾向につけ込み、その名前のパッケージを先に公開しておくこと | 入れる前の確かめ方は tool poisoning の行と同じ |

## 評価の語 {#eval-terms}

変更の効き目を測るときの語である。定義は、Anthropic の評価の解説記事（Demystifying evals for AI agents）に合わせた。

| 語 | 意味 | 備考 |
| --- | --- | --- |
| <span id="eval-task"></span>task | 入力と成功の基準が決まった、1 つのテスト | 解説は <!-- link:begin measure-changes -->[変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)<!-- link:end --> |
| <span id="trial"></span>trial | task に対する 1 回の試行。出力がぶれるので、同じ task を複数回試す | |
| <span id="grader"></span>grader | エージェントの出来の一部を採点する仕組み。1 つの task に複数つけてよい | |
| <span id="transcript"></span>transcript | 1 回の試行の完全な記録。出力・ツール呼び出し・推論・途中の結果を含む | Claude Code のセッションの記録を指す語でもあるので、評価の話では「試行の記録」と添える |
| <span id="outcome"></span>outcome | 試行の終わりに環境が置かれていた最終状態。Claude の「できました」という報告とは別 | 完了は報告でなく証拠で決める、という考え方につながる |
| <span id="pass-at-k"></span>pass@k | k 回の試行のうち、少なくとも 1 回成功する見込み | |
| <span id="pass-hat-k"></span>pass^k | k 回の試行がすべて成功する見込み。毎回確実に動いてほしい用途に向く | pass@k と逆向きの指標 |
| <span id="verifier"></span>検証器 | 出力が正しいかを機械的に判定する仕組み（テスト・採点スクリプトなど） | 検証器自体を確かめる方法は <!-- link:begin test-the-verifier -->[検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)<!-- link:end --> |
| <span id="red-green"></span>red/green | 検証器が、壊れた入力で落ち（red）、正しい入力で通る（green）ことを確かめる手順 | 確かめ方は検証器の行を参照 |
| <span id="freeze"></span>凍結 | 作業の途中で検証器や採点の基準が変わらないよう、固定しておくこと | 確かめ方は検証器の行を参照 |
| <span id="oof"></span>OOF（学習に使わなかった分の予測） | 交差検証で、学習に使わなかった分に対して出した予測。学習に使った分で測ると、評価が甘くなる | 評価が壊れている症状は <!-- link:begin misses-broken-evaluation -->[手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)<!-- link:end --> |

## 機能と利用の語 {#product-terms}

機能の名前や、使い方の中で出る語である。

| 語 | 意味 | 備考 |
| --- | --- | --- |
| <span id="auto-mode"></span>auto モード | 権限の確認の多くを、分類器に任せて進める Claude Code の権限モード。止められる操作と止められない操作がある | 表記は「auto モード」。解説は <!-- link:begin what-auto-mode-stops -->[auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)<!-- link:end --> |
| <span id="classifier"></span>分類器（auto モードの） | auto モードで、操作を実行してよいかを判定するモデル | 止めるものと止めないものは auto モードの行を参照 |
| <span id="memory-topics"></span>Topics | アプリのメモリで、覚えた内容をまとめた項目。画面での訳は確かめていない | 見る・直す方法は <!-- link:begin how-memory-works#manage -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 覚えた内容を見る・直す（棚卸し）](../app/how-memory-works.md#manage)<!-- link:end --> |
| <span id="memory-pause-reset"></span>Pause・Reset | アプリのメモリを止める操作（Pause）と、覚えた内容を消す操作（Reset） | 解説は <!-- link:begin how-memory-works#turning-off -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 消し方と止め方（Pause・Reset・会話ごとのオフ・シークレットチャット）](../app/how-memory-works.md#turning-off)<!-- link:end --> |
| <span id="usage-limit"></span>利用上限 | 一定の期間内に使える量の上限。別名は利用制限・使用制限 | 数値と種類はプランで違う。解説は <!-- link:begin how-usage-limits-work -->[利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)<!-- link:end --> |

## 学びと表記の語 {#human-terms}

AI と付き合う人の側の語と、日本語の表記を揃えるための語である。

| 語 | 意味 | 備考 |
| --- | --- | --- |
| <span id="cognitive-debt"></span>認知負債 | AI に任せて自分で理解を組み立てなかった分が、あとで理解の不足として返ってくること | 解説は <!-- link:begin learning-with-ai -->[AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)<!-- link:end --> |
| <span id="skill-formation"></span>技能形成 | 自分で試し、つまずきながら、力が身につくこと。AI に先に答えを出させると、この過程が減りうる | 解説は認知負債の行を参照 |
| <span id="notation-source"></span>表記の正本 | 表記の揺れを直すときに、基準にする 1 つの文書 | この辞典では、このページが正本である。解説は <!-- link:begin consistent-notation -->[表記ゆれと漢字の開き](../japanese/consistent-notation.md)<!-- link:end --> |
| <span id="open-kanji"></span>漢字を開く | 漢字で書ける語を、かなで書くこと | 解説は表記の正本の行を参照 |

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [用語索引と旧名の対応](term-index.md)
- [この辞典の引き方](how-to-use.md)
- [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- [失敗の二つの軸と診断の入口](six-causes.md)
- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- [ロードマップ（委任の段階別）](roadmap.md)
- [任せ方の段階と、無人で走らせる前の五つの問い › 任せ方の段階](../delegate/five-questions-before-delegating.md#autonomy-stages)
- [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- 自動メモリ（準備中）
- アプリでスキルを使う › 移された Styles（準備中）
- 出力スタイルで応答の仕方を切り替える（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
