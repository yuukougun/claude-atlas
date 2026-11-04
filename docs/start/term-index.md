---
id: term-index
title: 用語索引と旧名の対応
aliases: [用語索引, 索引, 旧名, 旧名と新名の対応表, 英語名から引く, 公式の訳語から引く, 名前から引く]
type: hub
field: start
chapter: 辞書として引く
order: 50
priority: 必須
summary: 機能名・旧名・英語名・公式の日本語訳から、その語のページを引ける。全ページの題名と別名から作り、旧名には今の名前を添える。
signs:
  - {type: goal, text: 古い記事に出てくる機能の名前から、今の名前を知りたい}
  - {type: goal, text: 英語の機能名から日本語の説明を探したい}
wave: 1
prerequisites: []
related: [glossary, reverse-index, outdated-advice-ledger, change-timeline-2026, how-to-use]
volatility: 低
sections:
  - {title: 引き方, anchor: how-to-read}
  - {title: 五十音順, anchor: kana}
  - {title: 英字の名前, anchor: latin}
  - {title: 旧名から引く, anchor: old-names}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：機能名・旧名・英語名・公式の日本語訳のどれからでも、その語を扱うページへ着ける。
    - **いつ引くか**：古い記事の機能名が今の画面や文書に見当たらないとき。英語の機能名から日本語の説明を探したいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：用語索引・索引・旧名・旧名と新名の対応表・英語名から引く・公式の訳語から引く・名前から引く
<!-- textlint-enable -->

用語索引は、機能や設定の名前から、その語を扱うページを引く一覧である。全ページの題名と別名から道具が作るので、手で足した行はない。名前が変わった機能には、今の名前を添えて並べる。

## 引き方 {#how-to-read}

引く一覧は、手元の名前の種類によって 3 つに分かれる。

- 日本語の名前で探すとき：「五十音順」の一覧を引く。
- 英語の機能名や設定のキーで探すとき：「英字の名前」の一覧を引く。`/permissions` のように `/` で始まるコマンド名は、「五十音順」の最後にある「漢字・記号で始まる語」の群に載る。
- 古い記事や動画で見た名前が、今の画面や文書に見当たらないとき：「旧名から引く」の一覧を引き、今の名前とそのページへ進む。

一覧には次の決まりがある。

- 語を載せるのは、下書き以上の段階にあるページだけである。行き先が「準備中」と出る行は、旧名の一覧にある。旧名の一覧は、今の名前の行き先がまだ公開前でも、旧名と今の名前の対応を先に示すためである。
- 同じ語が複数のページの別名にあるときは、その機能を主に扱うページを先に出し、ほかのページは短い印を付けて並べる。
- 旧名の行には、今の名前を添える。旧名と今の名前の対応は、この辞典の数値ファイルにある名称の項目を正とし、ページの別名と照らして作る。
- 名前が変わった時期と版は、この一覧に重ねて書かない。時期と版は <!-- link:begin change-timeline-2026#timeline -->2026 年の主な変更の年表 › 年表（準備中）<!-- link:end --> と <!-- link:begin outdated-advice-ledger#ledger -->[古くなった助言の台帳 › 台帳](../changes/outdated-advice-ledger.md#ledger)<!-- link:end --> に置いてあり、改名を 3 か所で持たないようにしている。

この索引が引くのは名前だけである。語の意味と表記の決め方は <!-- link:begin glossary -->[用語集（独自の用語と公式の訳語）](glossary.md)<!-- link:end --> に、困りごとやしたいことの言葉から引く道は <!-- link:begin reverse-index#how-to-read -->[逆引き辞典（症状・やりたいこと・状況） › 引き方](reverse-index.md#how-to-read)<!-- link:end --> にある。公式の日本語版で訳語が割れている語の扱いは <!-- link:begin glossary#split-terms -->[用語集（独自の用語と公式の訳語） › 公式で表記が割れている語](glossary.md#split-terms)<!-- link:end --> を見る。

## 五十音順 {#kana}

日本語の題名と別名を、読みの五十音順に並べた一覧である。漢字で始まる語は、読みではなく最初の字の順で、最後の群にまとまる。探す語が見つからないときは、その語の漢字の群を見る。

<!-- gen:begin terms kana -->
<!-- textlint-disable -->

### あ行 {#terms-a}

- アイデアの均質化 → [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)
- アプリと Claude Code と API の関係 → [全体地図：Claude の面と層](product-map.md)
- アプリのメモリ → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- イエスマンになる → [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)
- いつ /clear するか → [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- エージェントループ → [エージェントループと tool use](../basics/agent-loop.md)
- [エージェントループと tool use](../basics/agent-loop.md)
- エラーを直させる → [バグを直す](../recipes/fix-a-bug.md)
- オートモード → [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- オプトアウト → [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- お願いから鍵へ → [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- お願いと鍵 → [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- お願いと鍵（日本語の場合） → [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)
- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)

### か行 {#terms-ka}

- カスタムコマンド → [スキルの作り方](../extend/writing-skills.md)
- カスタムスラッシュコマンド → [スキルの作り方](../extend/writing-skills.md)
- カスタム指示 → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- この辞典のライセンス → [出典と AI 利用の方針](ai-and-sources.md)
- この辞典の作り方 → [出典と AI 利用の方針](ai-and-sources.md)
- [この辞典の引き方](how-to-use.md)
- コミットを任せるか → [git との付き合い方](../cli/working-with-git.md)
- コンテキストウィンドウ → [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)
- [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)
- コンテキストの内訳 → [/context で中身を見る](../context/inspect-context.md)
- コンテキストの劣化 → [context rot と紛らわしい情報](../basics/context-rot.md)
- コンテストの AI ルール → [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)

### さ行 {#terms-sa}

- [サブエージェントは別室の部下](../basics/subagent-isolation.md)
- サンクコスト → [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- サンドボックス → [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)
- システムリマインダー → [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)
- スキル（skills） → [スキルの作り方](../extend/writing-skills.md)
- [スキルの作り方](../extend/writing-skills.md)
- スキルの確認 → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)
- すぐ同意して意見を変える → [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)
- [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)
- すぐ同意する → [迎合（sycophancy）](../basics/sycophancy.md)
- すぐ諦めを勧める → [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- スコアだけ上がる → [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- スコープの膨張 → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- スコープを絞る → [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)
- ステートレス → [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)
- スラッシュコマンド → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)

### た行 {#terms-ta}

- チェックポイント → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- ツールが壊れたと言う → [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)
- ツールの呼び出し → [エージェントループと tool use](../basics/agent-loop.md)
- テストの改ざん → [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)
- テストの改ざんを防ぐ → [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- テストを書き換えさせない → [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)
- [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)
- です・ますが混ざる → [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)
- データと命令を区別できない → [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)
- [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)
- データの保持期間 → [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- でっち上げ → [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)
- デバッグ → [バグを直す](../recipes/fix-a-bug.md)
- [トークンとは](../basics/tokens.md)
- トークンの数え方 → [トークンとは](../basics/tokens.md)
- トークンを節約する → [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)
- トークンを食う → [上限を早く使う要因](../cost/what-uses-up-limits.md)
- トークン数 → [トークンとは](../basics/tokens.md)

### な行 {#terms-na}

- なぜを書く → [理由を添える](../prompting/give-reasons.md)

### は行 {#terms-ha}

- ハードコードで通す → [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)
- ハルシネーション → [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)
- [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)
- ハルシネーションを減らす頼み方 → [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)
- ハルシネーション対策 → [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [バグを直す](../recipes/fix-a-bug.md)
- バグ修正 → [バグを直す](../recipes/fix-a-bug.md)
- バッジの読み方 → [この辞典の引き方](how-to-use.md)
- ばらつき → [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- ファイルのアップロード → [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- ファイルのアップロード（アプリ） → [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- ファイルを消された → [消してはいけないものを消された](../symptoms/deleted-something-important.md)
- ファクトチェック → [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- フック（hooks） → [フックの考え方とイベント](../enforce/hooks-basics.md)
- フックイベント → [フックの考え方とイベント](../enforce/hooks-basics.md)
- フックで拒否する → [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- フックで止めて理由を返す → [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- [フックの考え方とイベント](../enforce/hooks-basics.md)
- プラグインの確認 → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- プロジェクトの指示 → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- プロンプトインジェクション → [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)
- [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)
- プロンプトの評価（eval）入門 → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- プロンプトを編集して送り直す → [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- ベンチを回すだけになる → [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)

### ま行 {#terms-ma}

- マルチエージェント → [並列の方式の選び方](../delegate/choosing-parallel-modes.md)
- メモリ（アプリ。memory） → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- メモリの Pause と Reset → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- メモリの混乱 → [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)
- メモリファイル → [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- もうやめてよい助言 → [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- もっともらしい嘘 → [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)
- [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)

### や行 {#terms-ya}

- やめどきを先に決める → [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- やらないことを書く → [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)
- やりたいことから引く → [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)

### ら行 {#terms-ra}

- リークに気づかない → [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- ルールを破られる → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- レビューの帯域 → [並列の上限は人間が決める](../delegate/humans-set-the-parallel-limit.md)
- レビュー待ちがたまる → [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)
- レビュー疲れ → [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- レベル → [ロードマップ（委任の段階別）](roadmap.md)
- [ロードマップ（委任の段階別）](roadmap.md)

### 漢字・記号で始まる語（最初の字の順。読みの順ではない） {#terms-other}

- ! でシェルを実行する → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- .claude/commands → [スキルの作り方](../extend/writing-skills.md)
- .claude/skills → [スキルの作り方](../extend/writing-skills.md)
- .env を読ませない → [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- .env を読まれた → [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)
- .mcp.json → [MCP をつなぐ](../extend/connecting-mcp.md)
- /checkpoint → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- /clear → [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- /clear のタイミング → [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- /code-review → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- /compact の後に忘れる → [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)
- /context → [/context で中身を見る](../context/inspect-context.md)
- [/context で中身を見る](../context/inspect-context.md)
- /doctor prompt-audit → [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- /effort → [effort の段階と使い分け](../models/effort-levels.md)
- /goal → [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- /mcp → [MCP をつなぐ](../extend/connecting-mcp.md)
- /permissions → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- /sandbox → [サンドボックスで封じ込める](../enforce/sandboxing.md)
- /security-review → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- /undo → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- /usage の内訳 → [上限を早く使う要因](../cost/what-uses-up-limits.md)
- @ でファイルを参照する → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- @ でファイルを指定する → [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- 「サーバー」と「サーバ」 → [表記ゆれと漢字の開き](../japanese/consistent-notation.md)
- [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)
- [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- [「完了」を定義して渡す](../verify/define-done.md)
- 「念のため確認して」は効くか → [検証の階段](../verify/verification-ladder.md)
- 三つを同時に持たせない → [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)
- 下書きの帯 → [この辞典の引き方](how-to-use.md)
- 不具合の修正 → [バグを直す](../recipes/fix-a-bug.md)
- 並列にしたら疲れた → [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)
- [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)
- 並列にしても速くならない → [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)
- [並列の上限は人間が決める](../delegate/humans-set-the-parallel-limit.md)
- [並列の方式の選び方](../delegate/choosing-parallel-modes.md)
- 並列の本数 → [並列の上限は人間が決める](../delegate/humans-set-the-parallel-limit.md)
- 並列実行 → [並列の方式の選び方](../delegate/choosing-parallel-modes.md)
- 並列疲れ → [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)
- 中ほどの情報は使われにくい → [context rot と紛らわしい情報](../basics/context-rot.md)
- 事実を確かめる → [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- 人が握るもの → [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)
- 人の側の失敗 → [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)
- 人の側の落とし穴 → [失敗の二つの軸と診断の入口](six-causes.md)
- 今日の日付を知らない → [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)
- 仕込まれた指示 → [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)
- 任せてはいけないこと → [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)
- 任せ方の段階と五つの問い → [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)
- 会話が長いと精度が落ちる → [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)
- 会話で言ったことが圧縮で消える → [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)
- 会話で言った禁止事項は圧縮で消える → [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- 会話をリセットする → [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- 会話全体の再送 → [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)
- 位置の効果 → [context rot と紛らわしい情報](../basics/context-rot.md)
- [体感と実測](../eval/felt-vs-measured.md)
- 体感を信じる → [体感と実測](../eval/felt-vs-measured.md)
- 何から読むか → [ロードマップ（委任の段階別）](roadmap.md)
- 何がコンテキストを占めているか → [/context で中身を見る](../context/inspect-context.md)
- 余計な変更 → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- 作業フォルダが散らかる → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- 使い方 → [この辞典の引き方](how-to-use.md)
- 使う・整える・任せる・仕組みにする・回す → [ロードマップ（委任の段階別）](roadmap.md)
- 使えなくなった小技 → [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- 使用制限 → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- 使用量がすぐなくなる → [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)
- 使用量が多い → [上限を早く使う要因](../cost/what-uses-up-limits.md)
- 使用量を減らす → [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)
- 依存のパッケージの確認 → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- 依存関係の地図 → [知識マップ](knowledge-map.md)
- 偽の完了 → [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- 先に引用を抜かせる → [長い資料は先、質問は最後](../prompting/long-context-first.md)
- 免責 → [出典と AI 利用の方針](ai-and-sources.md)
- 入力の4記号 → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- 全会話の指示 → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- 全体図 → [全体地図：Claude の面と層](product-map.md)
- [全体地図：Claude の面と層](product-map.md)
- 全部通ったと言うのに動かない → [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- 公式の訳語から引く → [用語索引と旧名の対応](term-index.md)
- 六つの「ない」 → [失敗の二つの軸と診断の入口](six-causes.md)
- 六つの失敗原因 → [失敗の二つの軸と診断の入口](six-causes.md)
- [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)
- 具体的なプロンプト → [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)
- 再現性 → [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- [出典と AI 利用の方針](ai-and-sources.md)
- 分類器に止められた → [断られた・止められた](../symptoms/refused-or-blocked.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- 別のコンテキストで調べさせる → [サブエージェントは別室の部下](../basics/subagent-isolation.md)
- 別の会話の内容が混ざる → [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)
- [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)
- 別室の部下 → [サブエージェントは別室の部下](../basics/subagent-isolation.md)
- 利用ポリシーで止められた → [断られた・止められた](../symptoms/refused-or-blocked.md)
- 利用上限（usage limits） → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- 利用上限での自動の継続（autoContinueAtUsageLimit） → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- 利用上限に早く当たる → [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)
- 利用上限の仕組み → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- 利用制限 → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- 前は効いたのに効かなくなった → [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)
- 前よりバカになった → [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)
- 前後で比べる → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- 前提の地図 → [知識マップ](knowledge-map.md)
- 前提を忘れる → [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)
- 前提関係のグラフ → [知識マップ](knowledge-map.md)
- 割り込んで指示する → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- 劣化した → [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)
- 劣化の確かめ方 → [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)
- [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)
- 努力レベル → [effort の段階と使い分け](../models/effort-levels.md)
- 動詞をはっきりさせる → [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)
- 勝手に送信しようとした → [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)
- 勝者の呪い → [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)
- 原因の切り分け → [失敗の二つの軸と診断の入口](six-causes.md)
- 取り返しのつかない操作 → [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- 古い Tips → [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)
- 古い助言 → [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- 古い情報で答える → [最新の情報を知らない](../symptoms/doesnt-know-latest.md)
- 古い記事が通じない → [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- 同じ修正の失敗 → [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)
- 同じ失敗を繰り返す → [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)
- [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)
- 同じ手順書を貼っている → [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)
- 同じ説明の繰り返し → [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- 同じ質問でも答えが変わる → [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- 同意は根拠に数えない → [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- 名前から引く → [用語索引と旧名の対応](term-index.md)
- 品質の低下 → [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)
- 嘘の引用 → [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)
- 四つの原理と比例則 → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- 困りごとから引く → [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)
- 図を読んでいない → [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)
- [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- 圧縮で残るもの・消えるもの → [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)
- 圧縮のあとに残る約束、消える約束 → [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)
- [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)
- 圧縮の後も守らせたい → [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)
- 地雷リスト → [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- 堂々巡り → [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- 報酬ハッキング → [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- 変更の効果の測り方 → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- 大会の生成 AI の利用規則 → [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)
- 大会の規則の早見 → [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)
- [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)
- [失敗の二つの軸と診断の入口](six-causes.md)
- 失敗の残骸 → [context rot と紛らわしい情報](../basics/context-rot.md)
- 失敗の残骸を残さない → [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- 好みに合わせる → [迎合（sycophancy）](../basics/sycophancy.md)
- 委任の段階 → [ロードマップ（委任の段階別）](roadmap.md)
- 存在しない API → [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)
- 存在しないものをあると言い張る → [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)
- 存在しない出典 → [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)
- [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)
- 学ぶ順 → [ロードマップ（委任の段階別）](roadmap.md)
- 学習に使われるか → [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- 学習データの期限 → [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)
- 安全の既定 → [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)
- 安全の早見表 → [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)
- 安全の設定の早見表 → [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)
- 完了と言うが終わっていない → [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- 完了の報告が信用できない → [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- 完了の定義 → [「完了」を定義して渡す](../verify/define-done.md)
- 完了条件 → [「完了」を定義して渡す](../verify/define-done.md)
- 完了条件で続けさせる → [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- 実測で確かめる → [体感と実測](../eval/felt-vs-measured.md)
- 実行と確認の繰り返し → [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)
- 実行結果で確かめる → [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- 実験のログ → [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- 実験の記録 → [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- 実験ノート → [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- 実験台帳 → [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- 対話モードの操作（入力の記号・キーボードショートカット） → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- 対象のファイルと症状を書く → [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)
- 小さくコミットする → [git との付き合い方](../cli/working-with-git.md)
- 小さな eval → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- 履歴を消された → [消してはいけないものを消された](../symptoms/deleted-something-important.md)
- 巻き戻し → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- 常駐するもののコスト（CLAUDE.md・MCP・skills） → [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- 常駐するコンテキスト → [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- 平凡な答えしか出ない → [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)
- 幻覚 → [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)
- 広い机 → [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)
- 引き継ぎ文書 → [handoff 文書と document-and-clear](../context/handoff-documents.md)
- 待ち時間が長い → [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)
- 思ったものと違う → [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)
- [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- 思考と effort の仕組み → [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)
- 性能が落ちた → [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)
- [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- [承認の確認が多すぎる・少なすぎる](../symptoms/wrong-amount-of-approvals.md)
- 技能形成 → [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- 押されると折れる → [迎合（sycophancy）](../basics/sycophancy.md)
- 押すと折れる → [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)
- 拒否された → [断られた・止められた](../symptoms/refused-or-blocked.md)
- 拒否ルール → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 拡張思考 → [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- 指示と強制 → [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- 指示の置き場所 → [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)
- 指示の置き場所（アプリ） → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- 指示はどこに入るか → [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)
- 指示を仕組みに移す → [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- 指示を無視される → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- 採点の抜け道 → [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- 採点スクリプトの検証 → [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- 推測で埋めさせない → [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)
- 推論の量 → [effort の段階と使い分け](../models/effort-levels.md)
- [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)
- 提案だけで止まる → [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- 握る → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- 損切りの判断 → [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- 撤回された助言 → [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- 撤退の判断 → [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)
- 敬体と常体を揃える → [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)
- 文体の揺れ → [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)
- 文体の統一 → [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)
- [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)
- 文末が揺れる → [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)
- 文章の lint → [textlint をフックで回す](../japanese/textlint-hook.md)
- 文脈のない新人として扱う → [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)
- 文脈の隔離 → [サブエージェントは別室の部下](../basics/subagent-isolation.md)
- 文脈を集める・行動する・確かめる → [エージェントループと tool use](../basics/agent-loop.md)
- [断られた・止められた](../symptoms/refused-or-blocked.md)
- 新しいセッションでレビュー → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- 新しいチャットにする → [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- 新しい版を知らない → [最新の情報を知らない](../symptoms/doesnt-know-latest.md)
- [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)
- 方針を疑わない・すぐ撤退を勧める → [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- 方針を見直さない → [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- 日本語で返してくれない → [英語で返ってくる](../symptoms/replies-in-english.md)
- [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)
- 日本語の出力を揃える仕組み → [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)
- 日本語の出力品質 → [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)
- 日本語の文章を機械で検査する → [textlint をフックで回す](../japanese/textlint-hook.md)
- 旧名 → [用語索引と旧名の対応](term-index.md)
- 旧名と新名の対応表 → [用語索引と旧名の対応](term-index.md)
- 明確かつ直接的に → [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)
- 書いた後に検査して差し戻す → [textlint をフックで回す](../japanese/textlint-hook.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- 書き出してから /clear → [handoff 文書と document-and-clear](../context/handoff-documents.md)
- 最低限の安全の設定 → [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)
- 最初の成果物は検証器 → [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- 最小権限 → [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [最新の情報を知らない](../symptoms/doesnt-know-latest.md)
- 期待外れの答え → [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)
- 本番を代表するテスト → [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- 条件が落ちる要約 → [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)
- 架空のパッケージ → [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)
- 検証の強さ → [検証の階段](../verify/verification-ladder.md)
- [検証の階段](../verify/verification-ladder.md)
- 検証器が問題を定義する → [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- 検証器そのものを確かめる → [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- 検証器のテスト → [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- 検証器の三条件 → [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- 検証器の質 → [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- 権限（permissions） → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 権限の分類器 → [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- 権限モード → [権限モードの選び方](../cli/permission-modes-overview.md)
- 権限モードの全体像 → [権限モードの選び方](../cli/permission-modes-overview.md)
- [権限モードの選び方](../cli/permission-modes-overview.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 死んだコードを残す → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)
- [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- 毎回確認してくる → [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- 毎回答えが違う → [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- 毎回背景を説明する → [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- 比例則 → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- 決めたコマンドを使わない → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- 決定論的な制御 → [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- 決定論的な制御に移す → [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- 注意の予算 → [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)
- [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- 消した会話を覚えている → [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)
- [消してはいけないものを消された](../symptoms/deleted-something-important.md)
- 添付が全部読まれていない → [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)
- [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)
- [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- 漢字をひらく → [表記ゆれと漢字の開き](../japanese/consistent-notation.md)
- 無人実行の前の確認 → [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)
- 無限検証ループ → [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)
- 特例の分岐で通す → [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)
- 独立したレビュー → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- 独自の用語 → [用語集（独自の用語と公式の訳語）](glossary.md)
- [理由を添える](../prompting/give-reasons.md)
- 環境のせいにする → [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)
- [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)
- 生の出力を出させる → [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- 生産性の錯覚 → [体感と実測](../eval/felt-vs-measured.md)
- 用語の定義 → [用語集（独自の用語と公式の訳語）](glossary.md)
- 用語索引 → [用語索引と旧名の対応](term-index.md)
- [用語索引と旧名の対応](term-index.md)
- 用語集 → [用語集（独自の用語と公式の訳語）](glossary.md)
- [用語集（独自の用語と公式の訳語）](glossary.md)
- 用語集を渡す → [表記ゆれと漢字の開き](../japanese/consistent-notation.md)
- 症状から引く → [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)
- 発想が似通う → [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)
- 直してもまた壊れる → [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)
- [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- 知識カットオフ → [最新の情報を知らない](../symptoms/doesnt-know-latest.md)
- [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)
- [知識マップ](knowledge-map.md)
- 破壊的な操作 → [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- 確かめる → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- 確かめ方の段階 → [検証の階段](../verify/verification-ladder.md)
- 確認なしで実行される → [承認の確認が多すぎる・少なすぎる](../symptoms/wrong-amount-of-approvals.md)
- [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- 確認ルール → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 確認日の読み方 → [この辞典の引き方](how-to-use.md)
- [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)
- 秘密の読み取りの禁止 → [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- 秘密をコミットされた → [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)
- 秘密を読まれた・出された → [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- 答えが毎回違う → [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)
- 節約のコツ → [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)
- 節約の優先順位 → [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)
- [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)
- [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)
- 索引 → [用語索引と旧名の対応](term-index.md)
- 終わりの条件を渡す → [「完了」を定義して渡す](../verify/define-done.md)
- 縛る → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- 考える量 → [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- 考え込みすぎる → [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)
- 背景と目的を伝える → [理由を添える](../prompting/give-reasons.md)
- 背骨の考え方 → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- 自作ループ（Ralph など） → [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- 自動化バイアス → [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- 自動圧縮で指示が消えた → [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)
- 自己申告ではなく証拠 → [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- 自律度の段階 → [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)
- [英語で返ってくる](../symptoms/replies-in-english.md)
- 英語に戻る → [英語で返ってくる](../symptoms/replies-in-english.md)
- 英語への回帰 → [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- 英語名から引く → [用語索引と旧名の対応](term-index.md)
- 表記の正規形 → [用語集（独自の用語と公式の訳語）](glossary.md)
- 表記の約束 → [用語集（独自の用語と公式の訳語）](glossary.md)
- 表記の統一 → [表記ゆれと漢字の開き](../japanese/consistent-notation.md)
- 表記ゆれ → [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)
- [表記ゆれと漢字の開き](../japanese/consistent-notation.md)
- 裏取り → [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- 製品の全体像 → [全体地図：Claude の面と層](product-map.md)
- [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)
- 要約の言い過ぎ → [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)
- 要約は原文より強く言いがち → [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)
- [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)
- 要約圧縮 → [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- 見せる → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)
- 言い訳が続く → [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)
- 訂正の往復をやめる → [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- 記事の手順が動かない → [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)
- [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)
- 記憶が混ざる → [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)
- 許可を何度も求められる → [承認の確認が多すぎる・少なすぎる](../symptoms/wrong-amount-of-approvals.md)
- 許可ルール → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- 訳語の対応 → [用語集（独自の用語と公式の訳語）](glossary.md)
- 診断の手順 → [失敗の二つの軸と診断の入口](six-causes.md)
- 評価のおかしさに自分からは気づかない → [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- 評価の誤りを放置する → [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- 評価への過適合 → [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)
- 評価を握る → [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- 評価器が問題を定義する → [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- 評価器の red/green → [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)
- 評価器の要件 → [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- 評価資産を守る → [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- 認証情報を守る → [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)
- 読ませたものの指示に従った → [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)
- [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)
- 読ませた文書の指示に従う → [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)
- 読ませるファイルを絞る → [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- 読み直す受験者 → [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)
- 調子が悪い → [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)
- 議事録だけ残す → [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- 資料の中の指示に従う → [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)
- 資料を先頭に置く → [長い資料は先、質問は最後](../prompting/long-context-first.md)
- 起動時に読み込まれるもの → [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- 起動直後の基準値 → [/context で中身を見る](../context/inspect-context.md)
- 辞典の使い方 → [この辞典の引き方](how-to-use.md)
- 迎合 → [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)
- [迎合（sycophancy）](../basics/sycophancy.md)
- 迎合の受け取り方 → [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- 返事が英語になる → [英語で返ってくる](../symptoms/replies-in-english.md)
- 返事が遅い → [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)
- [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)
- 返答の言語と文体を固定する → [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)
- 返答の言語を固定する → [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- 逆引き → [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)
- 逆引き辞典 → [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)
- [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)
- 途中で止まる → [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- 連絡先 → [出典と AI 利用の方針](ai-and-sources.md)
- 遅い → [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)
- 過剰設計 → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- 過去の会話の検索（search past chats） → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- 過去チャットの検索 → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- 過度な一般化 → [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)
- 道具への不満が増える → [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- 選んだ版の上振れ → [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)
- [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)
- 重い → [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)
- 長いコマンド出力を絞る → [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- 長い会話が重い理由 → [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)
- [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)
- 長い会話の劣化 → [context rot と紛らわしい情報](../basics/context-rot.md)
- [長い資料は先、質問は最後](../prompting/long-context-first.md)
- 間接プロンプトインジェクション → [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)
- 間違いを認めない → [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)
- 限界ですと言われる → [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)
- 非公式の教材 → [出典と AI 利用の方針](ai-and-sources.md)
- 非決定性 → [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)
- 非決定論的な指示 → [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- 面の地図 → [全体地図：Claude の面と層](product-map.md)
- 頼んだ範囲で → [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)
- 頼んでいないことまでやる → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)

<!-- textlint-enable -->
<!-- gen:end terms kana -->

## 英字の名前 {#latin}

英語の機能名・コマンド名・設定のキーなど、英字で始まる名前をアルファベット順に並べた一覧である。公式の日本語版が英語の名前をそのまま残している語も、ここで引ける。

<!-- gen:begin terms latin -->
<!-- textlint-disable -->

[A](#terms-latin-a)・[B](#terms-latin-b)・[C](#terms-latin-c)・[D](#terms-latin-d)・[E](#terms-latin-e)・[F](#terms-latin-f)・[G](#terms-latin-g)・[H](#terms-latin-h)・[I](#terms-latin-i)・[K](#terms-latin-k)・[L](#terms-latin-l)・[M](#terms-latin-m)・[N](#terms-latin-n)・[O](#terms-latin-o)・[P](#terms-latin-p)・[R](#terms-latin-r)・[S](#terms-latin-s)・[T](#terms-latin-t)・[U](#terms-latin-u)・[V](#terms-latin-v)・[W](#terms-latin-w)

### A {#terms-latin-a}

- adaptive thinking → [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- Add context → [理由を添える](../prompting/give-reasons.md)
- agentic loop → [エージェントループと tool use](../basics/agent-loop.md)
- Agents Rule of Two → [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- AI が書いた教材 → [出典と AI 利用の方針](ai-and-sources.md)
- AI で学ぶと身につかない → [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- AI で新しい技術を学ぶ → [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- AI に頼って判断を誤る仕組み → [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)
- AI に頼りすぎる → [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)
- AI の賛成を信じる → [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)
- AI を使った学習 → [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)
- allow ルール → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- anti-goals → [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)
- API キーの流出 → [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)
- API キーの漏洩 → [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- ask ルール → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- attention budget → [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)
- auto mode → [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- auto モード → [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)、[権限モードの選び方](../cli/permission-modes-overview.md)（機能）
- auto モードの分類器 → [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)

### B {#terms-latin-b}

- Be clear and direct → [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)
- brilliant but new employee → [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)
- bubblewrap → [サンドボックスで封じ込める](../enforce/sandboxing.md)

### C {#terms-latin-c}

- chat search → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- checkpoint → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- Claude Code の Projects（並列の threads） → [並列の方式の選び方](../delegate/choosing-parallel-modes.md)
- Claude Code のコストを見る → [上限を早く使う要因](../cost/what-uses-up-limits.md)
- claude mcp add → [MCP をつなぐ](../extend/connecting-mcp.md)
- claude plugin eval（スキルとプラグインの評価） → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- Claude のメモリ → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- Claude への指示（Instructions for Claude） → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- Claude 側の原因 → [失敗の二つの軸と診断の入口](six-causes.md)
- CLAUDE.md → [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- CLAUDE.md が効かない → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- CLAUDE.md が長い → [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- CLAUDE.md に書かないこと → [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- CLAUDE.md の位置づけ → [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)
- CLAUDE.md の書き方 → [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- CLAUDE.md の育て方 → [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- CLAUDE.md の行数 → [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)
- compaction → [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- compaction の後に忘れる → [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)
- context rot → [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)
- [context rot と紛らわしい情報](../basics/context-rot.md)
- context window → [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)

### D {#terms-latin-d}

- default\_to\_action → [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)
- Definition of Done → [「完了」を定義して渡す](../verify/define-done.md)
- deny ルール → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- denyRead → [サンドボックスで封じ込める](../enforce/sandboxing.md)
- deterministic → [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- distractor → [context rot と紛らわしい情報](../basics/context-rot.md)
- document and clear → [handoff 文書と document-and-clear](../context/handoff-documents.md)
- double-check して → [検証の階段](../verify/verification-ladder.md)
- draft PR → [git との付き合い方](../cli/working-with-git.md)

### E {#terms-latin-e}

- effort → [effort の段階と使い分け](../models/effort-levels.md)
- [effort の段階と使い分け](../models/effort-levels.md)
- Esc で止める → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- Esc を2回 → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- exit 2 でブロックする → [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- extended thinking → [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)

### F {#terms-latin-f}

- Files API → [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- five-hour limit → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- force push → [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)

### G {#terms-latin-g}

- git reset --hard → [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- [git との付き合い方](../cli/working-with-git.md)
- git を Claude に任せる → [git との付き合い方](../cli/working-with-git.md)
- Give Claude a check to run → [検証の階段](../verify/verification-ladder.md)
- going in circles → [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)

### H {#terms-latin-h}

- hallucination → [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- HANDOFF.md → [handoff 文書と document-and-clear](../context/handoff-documents.md)
- Help improve our AI models → [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- homogenization → [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)
- hook events → [フックの考え方とイベント](../enforce/hooks-basics.md)
- hooks → [フックの考え方とイベント](../enforce/hooks-basics.md)

### I {#terms-latin-i}

- I don't know を許す → [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)
- Instructions for Claude → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)

### K {#terms-latin-k}

- knowledge cutoff → [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)

### L {#terms-latin-l}

- language の設定（返答の言語） → [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- language 設定 → [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- lethal trifecta → [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- listing tax → [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- Long context prompting → [長い資料は先、質問は最後](../prompting/long-context-first.md)
- lost in the middle → [context rot と紛らわしい情報](../basics/context-rot.md)

### M {#terms-latin-m}

- Manual・acceptEdits・plan・auto・dontAsk・bypassPermissions → [権限モードの選び方](../cli/permission-modes-overview.md)
- MCP → [MCP をつなぐ](../extend/connecting-mcp.md)
- [MCP をつなぐ](../extend/connecting-mcp.md)
- MCP を入れすぎると重い → [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- MCP サーバー → [MCP をつなぐ](../extend/connecting-mcp.md)
- MCP サーバーの安全 → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- MCP・plugins・skills を入れる前の確認 → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- Memory → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- Memory FAQ → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- Model Context Protocol → [MCP をつなぐ](../extend/connecting-mcp.md)

### N {#terms-latin-n}

- nerf → [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)

### O {#terms-latin-o}

- output style と CLAUDE.md の違い → [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)
- over-engineering → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)
- over-reliance → [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- overgeneralization → [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)

### P {#terms-latin-p}

- package hallucination → [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)
- pass^k → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- PDF support → [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- PDF の後半を読まない → [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)
- permission modes → [権限モードの選び方](../cli/permission-modes-overview.md)
- permission rules → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- permissionDecision → [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- permissions → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- PreToolUse でブロックする → [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- prh → [表記ゆれと漢字の開き](../japanese/consistent-notation.md)
- Project instructions → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- prompt injection → [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)
- prompt injection にかかった → [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)

### R {#terms-latin-r}

- Ralph のループ → [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)
- refusal → [断られた・止められた](../symptoms/refused-or-blocked.md)
- review bottleneck → [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- reward hacking → [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- reward hacking への備え → [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- rewind → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- rm -rf → [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- rm -rf された → [消してはいけないものを消された](../symptoms/deleted-something-important.md)
- rug pull → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- Rule of Two → [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- rules と CLAUDE.md の違い → [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)
- Run agents in parallel → [並列の方式の選び方](../delegate/choosing-parallel-modes.md)

### S {#terms-latin-s}

- sandbox → [サンドボックスで封じ込める](../enforce/sandboxing.md)
- Sandboxing → [サンドボックスで封じ込める](../enforce/sandboxing.md)
- Search and reference chats → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- session limit → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- Shift+Tab でモードを切り替える → [権限モードの選び方](../cli/permission-modes-overview.md)
- skill が使われない → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- skill-creator → [スキルの作り方](../extend/writing-skills.md)
- SKILL.md → [スキルの作り方](../extend/writing-skills.md)
- slopsquatting → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- specification gaming → [採点器を騙す（reward hacking）](../basics/reward-hacking.md)
- Styles → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- sycophancy → [迎合（sycophancy）](../basics/sycophancy.md)
- system prompt → [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)
- system reminder → [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)

### T {#terms-latin-t}

- textlint → [textlint をフックで回す](../japanese/textlint-hook.md)
- textlint の hook → [textlint をフックで回す](../japanese/textlint-hook.md)
- [textlint をフックで回す](../japanese/textlint-hook.md)
- thinking → [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)
- thinking のオンとオフ → [effort の段階と使い分け](../models/effort-levels.md)
- token → [トークンとは](../basics/tokens.md)
- token counting → [トークンとは](../basics/tokens.md)
- tool poisoning → [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)

### U {#terms-latin-u}

- U 字型の性能 → [context rot と紛らわしい情報](../basics/context-rot.md)
- Upload files → [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)
- usage limit → [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)
- usage limits → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- user message → [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)

### V {#terms-latin-v}

- vision → [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)

### W {#terms-latin-w}

- web search → [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- Web 検索（web search。アプリ） → [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)
- weekly limit → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- What survives compaction → [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- What you can stop doing → [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- Wrap-Up Allowance → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- Write a specific prompt → [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)
- Writer/Reviewer パターン → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)

<!-- textlint-enable -->
<!-- gen:end terms latin -->

## 旧名から引く {#old-names}

古い記事や動画に出てくる名前から、今の名前と、その機能を扱うページを引く一覧である。名前は短い期間で変わることがあり、古い記事の手順がそのままでは通じない原因になる。

<!-- gen:begin terms old -->
<!-- textlint-disable -->

- --remote → --cloud（2026-07-03〜2026-07-06）：クラウドセッションと teleport（準備中）
- /allowed-tools → /permissions（2025-06-02・Claude Code 1.0.7）：[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- /cost → /usage（2026-04-23・Claude Code 2.1.118）：/usage・/context・ステータスラインで状態を見る（準備中）
- /extra-usage → usage credits（/usage-credits）（2026-05-19・Claude Code 2.1.144）：usage credits（上限を超えた分の従量課金）（準備中）
- /fork → /branch（今の /fork は、会話を新しい背景のセッションに写す別の機能）（2026-03-17・Claude Code 2.1.77）：セッションに名前を付けて再開・分岐する（準備中）
- /project:&lt;名前&gt; → /&lt;名前&gt;（サブディレクトリのファイルは /&lt;フォルダ&gt;:&lt;名前&gt;）（2025-06-16・Claude Code 1.0.25）：[スキルの作り方](../extend/writing-skills.md)
- /review → /code-review（2026-08-06・Claude Code 2.1.223）：[書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- /stats → /usage（2026-04-23・Claude Code 2.1.118）：/usage・/context・ステータスラインで状態を見る（準備中）
- /user:&lt;名前&gt; → /&lt;名前&gt;（サブディレクトリのファイルは /&lt;フォルダ&gt;:&lt;名前&gt;）（2025-06-16・Claude Code 1.0.25）：[スキルの作り方](../extend/writing-skills.md)
- /vim → /config の Editor mode（Vim と Normal の切り替え）（2026-04-04・Claude Code 2.1.92）：[入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- Anthropic Academy → Claude Academy（不明）
- Claude Code on the web → クラウドセッション（cloud sessions）（2026-09-10〜2026-09-17）：クラウドセッションと teleport（準備中）
- Claude Code SDK → Claude Agent SDK（2025-09-29・Claude Code 2.0.0）：Agent SDK（Claude Code をライブラリとして使う）（準備中）
- Claude in Slack → Claude Tag（2026-08-03）：周辺製品の一覧（準備中）
- claude-code-sdk（Python のパッケージ） → Claude Agent SDK（2025-09-29・Claude Code 2.0.0）：Agent SDK（Claude Code をライブラリとして使う）（準備中）
- default モード（表示の名前） → Manual（権限モード。設定の値は default のまま）（2026-07-03・Claude Code 2.1.200）：[権限モードの選び方](../cli/permission-modes-overview.md)
- extra usage → usage credits（/usage-credits）（2026-05-19・Claude Code 2.1.144）：usage credits（上限を超えた分の従量課金）（準備中）
- Max 20x → Ultra（2026-10-30）：プランの選び方（準備中）
- Recent → Recently blocked（/permissions のタブ）（2026-10-30・Claude Code 2.1.314）：[auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- Recently denied → Recently blocked（/permissions のタブ）（2026-10-30・Claude Code 2.1.314）：[auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- routines → クラウドの予定のタスク（cloud scheduled tasks）（2026-10-20 ごろ）：クラウドの定期タスク（準備中）
- session limit → 5-hour limit（5 時間の上限）（2026-10-27・Claude Code 2.1.312）：[利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)
- Workbench → playground（Claude Console）（2026-08-18）
- workflow（起動のキーワード） → ultracode（dynamic workflows を起動するキーワード）（2026-06-02・Claude Code 2.1.160）：dynamic workflows（スクリプトで多数のサブエージェントを動かす）（準備中）
- 「Customize」 → 「Plugins」（サイドバー・チャットのメニュー・設定の名前と、1 つの「Plugins」のページ）（2026-10-29〜2026-11-30）：アプリでプラグインを使う（準備中）
- 「Customize」の「Skills」「Connectors」「Plugins」のタブ → 「Plugins」（サイドバー・チャットのメニュー・設定の名前と、1 つの「Plugins」のページ）（2026-10-29〜2026-11-30）：アプリでプラグインを使う（準備中）

<!-- textlint-enable -->
<!-- gen:end terms old -->

旧名の行を見つけたら、次の順に確かめる。

1. 行き先のページで、今の名前での使い方を読む。名前が変わっても、機能が同じとは限らない。
2. 古い記事の助言そのものが変わっていないかを <!-- link:begin outdated-advice-ledger#find-in-your-setup -->[古くなった助言の台帳 › 自分の設定や記事で見つける](../changes/outdated-advice-ledger.md#find-in-your-setup)<!-- link:end --> で確かめる。
3. いつ、どの版で変わったかは <!-- link:begin change-timeline-2026#timeline -->2026 年の主な変更の年表 › 年表（準備中）<!-- link:end --> で確かめる。

旧名が一覧に見つからないときは、旧名ではなく、症状や目的の言葉で <!-- link:begin reverse-index#by-symptom -->[逆引き辞典（症状・やりたいこと・状況） › 困りごとから引く](reverse-index.md#by-symptom)<!-- link:end --> を引く。名前が一度変わった後に別の機能として再び現れる語もあるので、同じ名前でも記事の日付を確かめる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [用語集（独自の用語と公式の訳語）](glossary.md)
- [逆引き辞典（症状・やりたいこと・状況）](reverse-index.md)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)
- 2026 年の主な変更の年表（準備中）
- [この辞典の引き方](how-to-use.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
