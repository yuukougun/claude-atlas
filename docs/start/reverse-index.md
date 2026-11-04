---
id: reverse-index
title: 逆引き辞典（症状・やりたいこと・状況）
nav_title: 逆引き辞典
aliases: [逆引き, 困りごとから引く, 症状から引く, やりたいことから引く]
type: hub
field: start
chapter: 辞書として引く
order: 40
priority: 必須
summary: 困りごと・やりたいこと・置かれた状況の言葉から、引くページと疑う原因へ進める。表は各ページのサインから作り、どれから疑うかの注記を手で添える。
signs: []
wave: 1
prerequisites: []
related: [six-causes, how-to-use, term-index, outdated-advice-ledger]
volatility: 低
sections:
  - {title: 引き方, anchor: how-to-read}
  - {title: 困りごとから引く, anchor: by-symptom}
  - {title: やりたいことから引く, anchor: by-goal}
  - {title: 置かれた状況から引く, anchor: by-situation}
  - {title: 同じ言葉が複数のページに当たるとき, anchor: disambiguation}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：困りごと・やりたいこと・置かれた状況の言葉から、引くページへ進める。
    - **いつ引くか**：Claude の返答や動きに困ったとき、やりたいことの進め方を知りたいとき、チームや大会などの状況に合わせて準備するとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：逆引き・困りごとから引く・症状から引く・やりたいことから引く
<!-- textlint-enable -->

逆引き辞典は、読者の言葉から行き先のページを引く表である。機能名を知らなくても、困りごとの言い方で探せる。

## 引き方 {#how-to-read}

このページは、3 つの入口を持つ。困りごと、やりたいこと、置かれた状況である。自分の言葉に近いものを選び、その節の表から行き先のページへ進む。

- **困りごと**：Claude の返答や動きがおかしい。まず [困りごとから引く](#by-symptom) の表を見る。
- **やりたいこと**：やりたいことがはっきりしていて、進め方を知りたい。[やりたいことから引く](#by-goal) を見る。
- **置かれた状況**：チームで導入する、大会に向けて練習するなど、周りの条件が先に決まっている。[置かれた状況から引く](#by-situation) を見る。

表は各ページのフロントマターの `signs` から道具が作る。ページが増えると表も増える。手書きなのは、各節の導入と、最後の節の注記だけである。

困りごとの行から着く先は、まず症状のページである。症状のページは、原因を安く確かめられる順の診断と、対処のページへの振り分けを持つ。原因の全体像は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](six-causes.md#diagnosis)<!-- link:end --> にある。症状の言葉が思い浮かばないときは、<!-- link:begin how-to-use#lookup -->[この辞典の引き方 › 引き方（困りごと・やりたいこと・名前から）](how-to-use.md#lookup)<!-- link:end --> の道筋を先に読む。機能名や旧名が分かっているときは、<!-- link:begin term-index -->[用語索引と旧名の対応](term-index.md)<!-- link:end --> のほうが早い。

症状のページを集めた入口は <!-- link:begin field:symptoms -->[症状辞典](../symptoms/index.md)<!-- link:end --> である。

## 困りごとから引く {#by-symptom}

困りごとの節は、症状辞典の章ごとに分かれている。自分の困りごとに近い行を探し、行き先のページを開く。行き先が症状のページでなく対処のページの行は、症状のページが振り分ける内容のうち、その対処が直接の答えになる狭い場面である。

原因が分からないまま対処を試す前に、<!-- link:begin six-causes#claude-side -->[失敗の二つの軸と診断の入口 › Claude 側の六つの原因](six-causes.md#claude-side)<!-- link:end --> の 6 つの原因のどれに当たるかを疑うと、遠回りが減る。

<!-- gen:begin signs symptom -->
<!-- textlint-disable -->

### 返答と品質

- うまくいかないが、何が悪いのか見当がつかない → [失敗の二つの軸と診断の入口](six-causes.md)（アプリ・Claude Code・API、案内）
- AI に任せて失敗したが、原因が AI なのか自分の判断なのか分からない → [失敗の二つの軸と診断の入口](six-causes.md)（アプリ・Claude Code・API、案内）
- 自分には当たり前の前提が伝わっていない → [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)（アプリ・Claude Code・API、考え方）
- 書いた規則を、少し違う場面になると守らない → [理由を添える](../prompting/give-reasons.md)（アプリ・Claude Code・API、考え方）
- 指示の文字どおりにだけ従い、意図を汲まない → [理由を添える](../prompting/give-reasons.md)（アプリ・Claude Code・API、考え方）
- 直してと頼んだのに、見当違いの場所を直された → [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)（アプリ・Claude Code・API、考え方）
- 相談のつもりだったのに、ファイルを書き換えられた → [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)（アプリ・Claude Code・API、考え方）
- 話題を変えたのに、前の話に引きずられた答えが返る → [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)（アプリ・Claude Code、考え方）
- テストの件数が、報告のたびに変わっている → [報告ではなく証拠を求める](../verify/evidence-not-reports.md)（Claude Code・アプリ、考え方）
- うまくいった場合だけを並べた報告が返ってくる → [報告ではなく証拠を求める](../verify/evidence-not-reports.md)（Claude Code・アプリ、考え方）
- Claude に自分の作業を確認させると、いつも問題なしと言う → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)（Claude Code・アプリ、考え方）
- 拒否のルールに書いたのに、下のフォルダにある同じ名前のファイルは読まれた → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)（Claude Code、機能）
- auto モードに操作を止められて、作業が進まない → [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)（Claude Code・アプリ、機能）
- 自分の案を AI に見せると、たいてい褒められる → [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)（アプリ・Claude Code、判断）
- 頼んだものと違うものが出てくる → [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)（アプリ・Claude Code・API、症状）
- 「いい感じに」と頼むと平凡なものしか出ない → [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)（アプリ・Claude Code・API、症状）
- 回答が長すぎる・短すぎる → [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)（アプリ・Claude Code・API、症状）
- 文章が AI っぽい → [意図と違うものが出てくる](../symptoms/not-what-i-meant.md)（アプリ・Claude Code・API、症状）
- 頼んでいない機能やファイルが増える → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)（Claude Code・アプリ、症状）
- 小さな修正を頼んだのに周りまで書き換えられる → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)（Claude Code・アプリ、症状）
- 使わない抽象化や設定項目を勝手に足される → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)（Claude Code・アプリ、症状）
- 古いコードを消さずに新しい版を足していく → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)（Claude Code・アプリ、症状）
- 作業フォルダに一時ファイルを残していく → [頼んでいないことまでやる（過剰設計）](../symptoms/does-more-than-asked.md)（Claude Code・アプリ、症状）
- 提案だけで止まり、実行してくれない → [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)（Claude Code・アプリ、症状）
- 「続けますか」と毎回聞いてくる → [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)（Claude Code・アプリ、症状）
- 長い作業を途中でやめて報告してくる → [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)（Claude Code・アプリ、症状）
- 理由を言わずに止まっている → [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)（Claude Code・アプリ、症状）
- 正当な依頼なのに断られる → [断られた・止められた](../symptoms/refused-or-blocked.md)（アプリ・Claude Code・API、症状）
- 「新しい会話を始めて」と言われて続けられない → [断られた・止められた](../symptoms/refused-or-blocked.md)（アプリ・Claude Code・API、症状）
- 途中で別のモデルの返事に切り替わった → [断られた・止められた](../symptoms/refused-or-blocked.md)（アプリ・Claude Code・API、症状）
- 操作を止められたが、何に止められたのか分からない → [断られた・止められた](../symptoms/refused-or-blocked.md)（アプリ・Claude Code・API、症状）
- こちらの誤った指摘にもすぐ同意する → [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)（アプリ・Claude Code・API、症状）
- 「本当に？」と聞くと答えを変える → [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)（アプリ・Claude Code・API、症状）
- Claude も賛成したのに計画が失敗した → [すぐ同意して意見を変える（迎合）](../symptoms/caves-when-pushed.md)（アプリ・Claude Code・API、症状）
- 間違いを指摘しても認めずに言い張る → [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)（Claude Code・アプリ、症状）
- 存在しないバグや変更をあったことにして譲らない → [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)（Claude Code・アプリ、症状）
- 説明と実際の履歴が食い違っている → [誤りを認めずに言い張る](../symptoms/insists-on-mistakes.md)（Claude Code・アプリ、症状）

### 事実と出典

- 聞き覚えのある名前について、中身をでっち上げる → [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)（アプリ・Claude Code・API、考え方）
- 長い資料を渡すと、質問の肝心な所を外す → [長い資料は先、質問は最後](../prompting/long-context-first.md)（アプリ・Claude Code・API、考え方）
- Word の資料に入れた図を読んでくれない → [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)（アプリ・API、機能）
- もっともらしいが出典が怪しい → [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)（アプリ・Claude Code・API、症状）
- 存在しない論文や URL を挙げられる → [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)（アプリ・Claude Code・API、症状）
- 同じ質問をするたびに答えが変わり、どれが正しいか分からない → [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)（アプリ・Claude Code・API、症状）
- 確かめると数字や引用が原文と違っている → [もっともらしい嘘・出典の誤り](../symptoms/plausible-falsehoods.md)（アプリ・Claude Code・API、症状）
- 存在しない関数や引数を自信満々に使う → [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)（Claude Code・アプリ・API、症状）
- インストールできないパッケージ名を書かれる → [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)（Claude Code・アプリ・API、症状）
- 実行する環境で使えないライブラリを足される → [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)（Claude Code・アプリ・API、症状）
- 最近の出来事や新しい版について間違える → [最新の情報を知らない](../symptoms/doesnt-know-latest.md)（アプリ・Claude Code・API、症状）
- Claude Code の新しい機能について聞くと古い答えが返る → [最新の情報を知らない](../symptoms/doesnt-know-latest.md)（アプリ・Claude Code・API、症状）
- 古い書き方のコードや設定を出してくる → [最新の情報を知らない](../symptoms/doesnt-know-latest.md)（アプリ・Claude Code・API、症状）
- 古い記事のやり方が通じない → [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)（アプリ・Claude Code・API、症状）
- 前は効いた書き方や設定が効かなくなった → [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)（アプリ・Claude Code・API、症状）
- 記事に出てくるコマンドや機能の名前が、手元に見当たらない → [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)（アプリ・Claude Code・API、症状）
- 記事によって書いてあることが食い違う → [記事や前のやり方が通じない](../symptoms/old-advice-doesnt-work.md)（アプリ・Claude Code・API、症状）
- 長い PDF の後半の図について答えられない → [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)（アプリ・API、症状）
- 資料の途中から内容を取り違える → [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)（アプリ・API、症状）
- 添付したのに読んでいないような答えが返る → [添付した資料の後半を読んでいない](../symptoms/skipped-later-pages.md)（アプリ・API、症状）
- 要約すると「場合がある」が「必ず」になる → [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)（アプリ・Claude Code・API、症状）
- 論文の要約が原文の結論より強い → [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)（アプリ・Claude Code・API、症状）
- 条件や但し書きが要約から落ちる → [要約が原文より断定的になる](../symptoms/summary-overstates-source.md)（アプリ・Claude Code・API、症状）

### 会話と文脈

- 間違った方向に進み始めたのに、止め方が分からない → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)（Claude Code、機能）
- 巻き戻したのに、一部のファイルが元に戻らない → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)（Claude Code、機能）
- CLAUDE.md に「〜しない」と書いたのに破られる → [お願いを鍵に移す判断](../enforce/when-to-lock.md)（Claude Code・アプリ・API、考え方）
- 「push しないで」と言ったのに、しばらくすると push された → [お願いを鍵に移す判断](../enforce/when-to-lock.md)（Claude Code・アプリ・API、考え方）
- ここまで作ったので、今さら方針を変えられない → [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)（アプリ・Claude Code、判断）
- 直したと言われたのに、条件を変えると同じバグが出る → [バグを直す](../recipes/fix-a-bug.md)（Claude Code・アプリ、手順）
- 修正を頼むたびに、的外れな場所が書き換えられる → [バグを直す](../recipes/fix-a-bug.md)（Claude Code・アプリ、手順）
- 会話が長くなると精度が落ちる → [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)（アプリ・Claude Code・API、症状）
- 最初に伝えた前提を途中から忘れる → [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)（アプリ・Claude Code・API、症状）
- 大量のログやテスト出力で会話が埋まっていく → [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)（アプリ・Claude Code・API、症状）
- 同じバグの修正を何度も失敗する → [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)（Claude Code・アプリ、症状）
- 直してと言うたびに同じ間違いが戻ってくる → [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)（Claude Code・アプリ、症状）
- 訂正しても別の形で同じ誤りが出る → [同じ失敗を繰り返す（堂々巡り）](../symptoms/going-in-circles.md)（Claude Code・アプリ、症状）
- 圧縮されたら前に決めたことを忘れた → [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)（Claude Code・アプリ・API、症状）
- 会話で禁止したことを圧縮の後にやられた → [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)（Claude Code・アプリ・API、症状）
- 自動圧縮の後から作業の進め方が変わった → [圧縮の後に約束を忘れた](../symptoms/forgot-after-compaction.md)（Claude Code・アプリ・API、症状）
- 別のプロジェクトの記憶が混ざる → [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)（アプリ・Claude Code、症状）
- 会話を消したのに覚えている → [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)（アプリ・Claude Code、症状）
- 前の会話で話した内容を勝手に持ち出される → [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)（アプリ・Claude Code、症状）

### 指示と仕組み

- 設定した指示が、関係のない会話にまで効いてしまう → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)（アプリ、比較）
- CLAUDE.md に構成の説明を長く書いたのに、役に立っている気がしない → [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)（Claude Code、機能）
- MCP サーバーをつないだのに、ツールが出てこない・つながらない → [MCP をつなぐ](../extend/connecting-mcp.md)（Claude Code・アプリ、機能）
- 設定したフックが動いていないように見える → [フックの考え方とイベント](../enforce/hooks-basics.md)（Claude Code・API、機能）
- CLAUDE.md に書いたのに守られない → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)（Claude Code・アプリ、症状）
- 長い会話の途中から規則を無視し始める → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)（Claude Code・アプリ、症状）
- 作ったスキルが使われない → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)（Claude Code・アプリ、症状）
- CLAUDE.md を書き足すほど守られなくなった → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)（Claude Code・アプリ、症状）
- 決めたコマンド（uv・pnpm など）を使わず別の方法で実行する → [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)（Claude Code・アプリ、症状）
- 毎回同じ背景を説明している → [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)（アプリ・Claude Code、症状）
- 同じ手順書を何度も貼っている → [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)（アプリ・Claude Code、症状）
- 新しい会話のたびにプロジェクトの説明からやり直している → [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)（アプリ・Claude Code、症状）
- 同じ注意を何度も繰り返している → [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)（アプリ・Claude Code、症状）

### 日本語の出力

- 言語を日本語に設定しても、英語の返事が混ざる → [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)（Claude Code・アプリ・API、手順）
- 漢字が多くて硬い文章になる → [表記ゆれと漢字の開き](../japanese/consistent-notation.md)（アプリ・Claude Code、手順）
- 用語集を渡して頼んでも、表記の揺れが残る → [textlint をフックで回す](../japanese/textlint-hook.md)（Claude Code、手順）
- 返事が英語になる → [英語で返ってくる](../symptoms/replies-in-english.md)（Claude Code・アプリ・API、症状）
- 途中から英語に切り替わって戻らない → [英語で返ってくる](../symptoms/replies-in-english.md)（Claude Code・アプリ・API、症状）
- ツールの結果を読んだ後の一言だけ英語になる → [英語で返ってくる](../symptoms/replies-in-english.md)（Claude Code・アプリ・API、症状）
- です・ますとだ・であるが混ざる → [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)（アプリ・Claude Code・API、症状）
- 「サーバー」と「サーバ」が混在する → [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)（アプリ・Claude Code・API、症状）
- 指定した文体が長い文章の途中で崩れる → [文体や表記が揃わない](../symptoms/inconsistent-japanese-style.md)（アプリ・Claude Code・API、症状）

### 完了と検証

- 「確かめて」と書いても、確かめずに終わる → [検証の階段](../verify/verification-ladder.md)（Claude Code、考え方）
- テストに書いた条件だけが満たされ、書かなかった意図は抜けていた → [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)（Claude Code・API、考え方）
- 手元で試した入力と、本番の入力の傾向が違っていた → [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)（Claude Code・API、考え方）
- 採点のスクリプト自体にバグがあった → [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)（Claude Code、手順）
- どの方法を試しても点が出ず、何かがおかしい → [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)（Claude Code、手順）
- いちばん点の良かった版を選んだのに、新しい入力では平凡だった → [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)（Claude Code・API、考え方）
- フックで止めても、Claude が理由を分からずに同じ操作を繰り返す → [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)（Claude Code、機能）
- AI の案をそのまま採って、なぜそうしたか説明できない → [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)（アプリ・Claude Code、考え方）
- もっともらしい答えを、確かめずにそのまま使ってしまう → [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)（アプリ・Claude Code、判断）
- AI の出力がおかしいと感じても、自分の判断で上書きできない → [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)（アプリ・Claude Code、判断）
- 大会の AI のルールが前と変わっていて、どれが最新か分からない → [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)（考え方）
- 「全部通りました」と言うが信用できない → [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)（Claude Code・アプリ・API、症状）
- 完了と報告されたのに動かない → [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)（Claude Code・アプリ・API、症状）
- 計画したはずの確認を実際にはやっていない → [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)（Claude Code・アプリ・API、症状）
- 「ほかに該当する箇所はない」と言い切られたが残っていた → [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)（Claude Code・アプリ・API、症状）
- テストのほうを書き換えて通された → [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)（Claude Code、症状）
- 特定の入力だけ通るように分岐を足された → [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)（Claude Code、症状）
- 例外を握りつぶしたり型を緩めたりしてエラーを消された → [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)（Claude Code、症状）
- 評価のやり方の誤りを指摘してくれない → [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)（Claude Code・API、症状）
- 手元のスコアは上がるのに本番で通用しない → [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)（Claude Code・API、症状）
- おかしな評価のまま実験を続けている → [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)（Claude Code・API、症状）

### 長い作業と方針

- AI で速くなった気がするが、本当か分からない → [体感と実測](../eval/felt-vs-measured.md)（アプリ・Claude Code、判断）
- 前に効かなかった改善案を、気づかずにまた試していた → [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)（Claude Code、手順）
- 結果を見てから、効いた理由を後付けしている → [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)（Claude Code、手順）
- 拒否のルールを書いたのに、スクリプト経由で読まれた → [サンドボックスで封じ込める](../enforce/sandboxing.md)（Claude Code、機能）
- 条件に入れた「テストを変えない」が守られたか判定されない → [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)（Claude Code、機能）
- 並列の方法が多すぎて、どれを使えばいいか分からない → [並列の方式の選び方](../delegate/choosing-parallel-modes.md)（Claude Code、比較）
- AI に頼りきって、判断を誤った気がする → [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)（アプリ・Claude Code、判断）
- AI に出させた企画が、どこかで見たようなものばかりになる → [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)（アプリ・Claude Code、判断）
- AI と一緒だと分かった気になるが、AI なしでは解けない → [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)（アプリ・Claude Code、判断）
- マネージャーのところで PR が止まる → [レビューのボトルネックと疲労](../team/review-bottlenecks.md)（Claude Code、考え方）
- ベンチを回してスコアを見るだけの繰り返しになる → [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)（Claude Code、症状）
- 同じ修正と確認を利用上限まで繰り返す → [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)（Claude Code、症状）
- 何時間も回したのに途中から進んでいない → [同じ確認のループにはまる](../symptoms/stuck-in-a-check-loop.md)（Claude Code、症状）
- エラーを直し続けるだけで、やり方そのものを見直さない → [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)（Claude Code・アプリ、症状）
- 少し試しただけで「これ以上は無理です」と言われる → [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)（Claude Code・アプリ、症状）
- 会話が長くなると撤退を勧めてくる → [直し続けて方針を疑わない（またはすぐ撤退を勧める）](../symptoms/wont-rethink-approach.md)（Claude Code・アプリ、症状）
- 「環境が壊れている」と言って作業をやめる → [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)（Claude Code、症状）
- ツールが動かないと言うが、自分で実行すると動く → [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)（Claude Code、症状）
- 長く動かすうちに道具への不満が増えていく → [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)（Claude Code、症状）
- 並列にしたら疲れた → [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)（Claude Code、症状）
- レビュー待ちの変更がたまっていく → [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)（Claude Code、症状）
- 並べた分だけ速くなった気がしない → [並列にしたら疲れた・レビューが追いつかない](../symptoms/parallel-fatigue.md)（Claude Code、症状）

### 安全と承認

- ファイルを消された・消されそうで怖い → [消してはいけないものを消された](../symptoms/deleted-something-important.md)（Claude Code・アプリ、症状）
- git の履歴やブランチを巻き戻された → [消してはいけないものを消された](../symptoms/deleted-something-important.md)（Claude Code・アプリ、症状）
- データベースのデータを消された → [消してはいけないものを消された](../symptoms/deleted-something-important.md)（Claude Code・アプリ、症状）
- .env の中身を読まれて会話に出された → [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)（Claude Code・アプリ、症状）
- API キーを含むファイルをコミットされた → [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)（Claude Code・アプリ、症状）
- 秘密の値がログや出力に残っている → [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)（Claude Code・アプリ、症状）
- 会話に API キーを貼ってしまった → [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)（Claude Code・アプリ、症状）
- 読ませた Web ページに書かれた指示どおりに動いた → [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)（アプリ・Claude Code・API、症状）
- 頼んでいない送信や操作をしようとした → [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)（アプリ・Claude Code・API、症状）
- 資料を読ませたら答えが不自然な方向に誘導された → [読ませたページやファイルの指示に従ってしまった](../symptoms/followed-injected-instructions.md)（アプリ・Claude Code・API、症状）
- 確認ボタンを読まずに押している → [承認の確認が多すぎる・少なすぎる](../symptoms/wrong-amount-of-approvals.md)（Claude Code・アプリ、症状）
- 許可を求められる回数が多すぎて作業にならない → [承認の確認が多すぎる・少なすぎる](../symptoms/wrong-amount-of-approvals.md)（Claude Code・アプリ、症状）
- 確認なしで実行されて怖い → [承認の確認が多すぎる・少なすぎる](../symptoms/wrong-amount-of-approvals.md)（Claude Code・アプリ、症状）

### 上限と速さ

- 一度試して良かった変更が、次には効かなかった → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)（アプリ・Claude Code・API、手順）
- 平均は良くなったのに、一部のケースで悪くなっていた → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)（アプリ・Claude Code・API、手順）
- アプリをたくさん使った日は、Claude Code でも早く上限に当たる → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)（アプリ・Claude Code、考え方）
- 長いセッションを続けると、消費が急に増える → [上限を早く使う要因](../cost/what-uses-up-limits.md)（アプリ・Claude Code、考え方）
- すぐ上限に当たる → [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)（アプリ・Claude Code・API、症状）
- 数回のやりとりで使用量の残りが大きく減る → [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)（アプリ・Claude Code・API、症状）
- 「会話が長すぎる」と表示されて続けられない → [すぐ上限に当たる](../symptoms/hits-limits-quickly.md)（アプリ・Claude Code・API、症状）
- 返事が返ってくるまで時間がかかりすぎる → [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)（アプリ・Claude Code・API、症状）
- 簡単な質問なのに長く考え込む → [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)（アプリ・Claude Code・API、症状）
- 入れた拡張が多すぎて重い → [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)（アプリ・Claude Code・API、症状）
- 急に性能が落ちた気がする → [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)（アプリ・Claude Code・API、症状）
- 前は一度でできたことができなくなった → [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)（アプリ・Claude Code・API、症状）
- 更新の後から答えが雑になった気がする → [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)（アプリ・Claude Code・API、症状）

<!-- textlint-enable -->
<!-- gen:end signs symptom -->

## やりたいことから引く {#by-goal}

やりたいことの節は、場面か分野ごとに分かれている。「長い作業を任せたい」「毎回同じ手順を貼りたくない」のような言い方で探す。理由を知りたいときも、この節に行を置いてある。

行き先には、面（アプリ・Claude Code）や型（考え方・手順）の短い印が付く。同じ問いに答えるページが複数あるときは、1 行に束ねてある。自分の使っている面に合う印のページから開くとよい。

<!-- gen:begin signs goal -->
<!-- textlint-disable -->

### 入口と地図

- 書いてあることをどこまで信用してよいか知りたい → [この辞典の引き方](how-to-use.md)（案内）
- 自分の AI にこの辞典を読ませたい → [この辞典の引き方](how-to-use.md)（案内）
- 公式の文書や講座とこの辞典を、どう使い分ければよいか知りたい → [この辞典の引き方](how-to-use.md)（案内）
- 個別の小技ではなく、うまく使うための考え方の筋をつかみたい → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)（アプリ・Claude Code・API、案内）
- どこまで任せてよいかを決める基準がほしい → [四つの原理と比例則（見せる・確かめる・縛る・握る）](four-principles.md)（アプリ・Claude Code・API、案内）
- 症状から原因を順に切り分けたい → [失敗の二つの軸と診断の入口](six-causes.md)（アプリ・Claude Code・API、案内）
- 古い記事に出てくる機能の名前から、今の名前を知りたい → [用語索引と旧名の対応](term-index.md)（案内）
- 英語の機能名から日本語の説明を探したい → [用語索引と旧名の対応](term-index.md)（案内）
- この辞典の言葉が、公式の文書のどの言葉に当たるか知りたい → [用語集（独自の用語と公式の訳語）](glossary.md)（案内）
- アプリと Claude Code で名前が同じ機能が、同じものか知りたい → [用語集（独自の用語と公式の訳語）](glossary.md)（案内）
- Claude の製品と機能の全体像をつかみたい → [全体地図：Claude の面と層](product-map.md)（アプリ・Claude Code・API、案内）
- 次にどこまで任せられるようになればよいか知りたい → [ロードマップ（委任の段階別）](roadmap.md)（案内）
- 何から順に読めばよいか知りたい → [ロードマップ（委任の段階別）](roadmap.md)（案内）
- この辞典の文章を誰がどう書いて確かめているか知りたい → [出典と AI 利用の方針](ai-and-sources.md)（案内）
- この辞典の文章や雛形を自分の資料に使いたい → [出典と AI 利用の方針](ai-and-sources.md)（案内）

### 基礎：なぜそうなるか

- 上限や費用で言う「トークン」が何を数えているのか知りたい → [トークンとは](../basics/tokens.md)（アプリ・Claude Code・API、考え方）
- コンテキストが広くなったのなら、資料を全部入れてよいのか知りたい → [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)（アプリ・Claude Code・API、考え方）
- 資料を多く渡すほど、大事な点が拾われにくくなる理由を知りたい → [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)（アプリ・Claude Code・API、考え方）
- 長い会話ほど返事が遅く、上限の減りも早くなる理由を知りたい → [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)（アプリ・Claude Code・API、考え方）
- 長い会話で答えの質が落ちていく理由を知りたい → [context rot と紛らわしい情報](../basics/context-rot.md)（アプリ・Claude Code・API、考え方）
- 失敗した試みが会話に残ると、同じ誤りに戻りやすくなる理由を知りたい → [context rot と紛らわしい情報](../basics/context-rot.md)（アプリ・Claude Code・API、考え方）
- 長い資料の真ん中の情報は使われにくい、というのは本当か知りたい → [context rot と紛らわしい情報](../basics/context-rot.md)（アプリ・Claude Code・API、考え方）
- 圧縮のあとに何が残り、何が消えるのか知りたい → [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)（Claude Code・アプリ・API、考え方）
- 調べものを別の担当に任せると、何が得で何が損か知りたい → [サブエージェントは別室の部下](../basics/subagent-isolation.md)（Claude Code・API、考え方）
- エージェントが裏で何を繰り返して作業を進めているのか知りたい → [エージェントループと tool use](../basics/agent-loop.md)（Claude Code・アプリ・API、考え方）
- 動くか確かめないまま終わったことにする理由を知りたい → [エージェントループと tool use](../basics/agent-loop.md)（Claude Code・アプリ・API、考え方）
- 考える量を増やすと何が良くなり、何が悪くなるのか知りたい → [思考（thinking）と effort の仕組み](../basics/how-thinking-works.md)（アプリ・Claude Code・API、考え方）
- もっともらしい誤りを自信を持って言う理由を知りたい → [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)（アプリ・Claude Code・API、考え方）
- Claude が最近の出来事や今日の日付を知らない理由を知りたい → [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)（アプリ・Claude Code・API、考え方）
- 同じ頼み方でも答えが毎回変わる理由を知りたい → [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)（アプリ・Claude Code・API、考え方）
- 一回うまくいった頼み方を信じてよいか判断したい → [同じ質問でも答えが変わる（非決定性）](../basics/nondeterminism.md)（アプリ・Claude Code・API、考え方）
- AI の要約をそのまま根拠に使ってよいか判断したい → [要約は原文より強く言いがち（過度な一般化）](../basics/summary-overgeneralization.md)（アプリ・Claude Code・API、考え方）
- Claude が賛成しがちな理由を知りたい → [迎合（sycophancy）](../basics/sycophancy.md)（アプリ・Claude Code・API、考え方）
- 採点やテストの抜け道を突かれる理由を知りたい → [採点器を騙す（reward hacking）](../basics/reward-hacking.md)（Claude Code・API、考え方）
- 検証を書き換えられない形にすべき理由を知りたい → [採点器を騙す（reward hacking）](../basics/reward-hacking.md)（Claude Code・API、考え方）
- CLAUDE.md やプロジェクトの指示がどこに入り、どれだけ効くのか知りたい → [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)（Claude Code・アプリ・API、考え方）
- 「必ず」と書いた規則でも破られる理由を知りたい → [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)（Claude Code、考え方）
- どの規則を仕組みで強制すべきか見分けたい → [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)（Claude Code、考え方）
- 読ませた資料の中の指示に、なぜ従ってしまうのか知りたい → [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)（アプリ・Claude Code・API、考え方）

### モデル・effort・思考

- 返答をもっと深く考えさせたい → [effort の段階と使い分け](../models/effort-levels.md)（アプリ・Claude Code・API、機能）
- 簡単な作業では、深く考えさせずに速く済ませたい → [effort の段階と使い分け](../models/effort-levels.md)（アプリ・Claude Code・API、機能）
- 「劣化した」と感じたのが本当かを、測って確かめたい → [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)（Claude Code・アプリ・API、手順）
- 更新の前と後で、同じ課題の結果を比べたい → [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)（Claude Code・アプリ・API、手順）

### 頼み方

- 頼み方の基本を一つだけ押さえたい → [新人の同僚に頼むつもりで](../prompting/brief-a-new-colleague.md)（アプリ・Claude Code・API、考え方）
- 一回で意図どおりに動いてほしい → [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)（アプリ・Claude Code・API、考え方）
- 大事な方針の変更では、手を止めて相談してほしい → [提案してほしいのか、実行してほしいのか](../prompting/suggest-or-do.md)（アプリ・Claude Code・API、考え方）
- 小さな修正は、小さいまま終わらせたい → [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)（アプリ・Claude Code・API、考え方）
- 触ってよいファイルを限りたい → [範囲を伝える（やらないこと）](../prompting/state-the-scope.md)（アプリ・Claude Code・API、考え方）
- 複数の文書を読ませて比べたい → [長い資料は先、質問は最後](../prompting/long-context-first.md)（アプリ・Claude Code・API、考え方）
- 資料のどこを根拠にしたのか示してほしい → [長い資料は先、質問は最後](../prompting/long-context-first.md)（アプリ・Claude Code・API、考え方）
- 分からないときは、分からないと答えてほしい → [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)（アプリ・Claude Code・API、考え方）
- 根拠のない部分は、推測だと分かるように書いてほしい → [「分からない」と言ってよいと伝える](../prompting/allow-i-dont-know.md)（アプリ・Claude Code・API、考え方）

### 文脈を整える

- どのタイミングで新しい会話にすべきか知りたい → [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)（アプリ・Claude Code、考え方）
- 失敗したやり取りをなかったことにしてやり直したい → [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)（アプリ・Claude Code、考え方）
- 圧縮のあとも守らせたい約束を、どこに書けばよいか知りたい → [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)（Claude Code、考え方）
- 長いセッションで、最初に決めた約束を最後まで守らせたい → [圧縮で消えない場所に約束を置く](../context/promises-after-compaction.md)（Claude Code、考え方）
- 長い作業を明日も続けたい → [handoff 文書と document-and-clear](../context/handoff-documents.md)（Claude Code・アプリ、手順）
- 要約に任せず、次の会話に持ち越すものを自分で選びたい → [handoff 文書と document-and-clear](../context/handoff-documents.md)（Claude Code・アプリ、手順）
- 何がコンテキストを占めているか知りたい → [/context で中身を見る](../context/inspect-context.md)（Claude Code、機能）
- 拡張を足した後、起動直後にどれだけ場所を取っているか確かめたい → [/context で中身を見る](../context/inspect-context.md)（Claude Code、機能）
- MCP や skill をどこまで入れてよいか知りたい → [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)（Claude Code、考え方）
- 読ませるファイルを自分で指定したい → [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)（Claude Code・アプリ、考え方）

### アプリを使いこなす

- 返答の口調や形式をいつも揃えたい → [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)（アプリ、比較）
- 前の会話で話したことを覚えていてほしい → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)（アプリ、機能）
- 前の会話の内容を探して使わせたい → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)（アプリ、機能）
- 何を覚えられているかを確かめたい → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)（アプリ、機能）
- 間違って覚えられた内容を直したい → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)（アプリ、機能）
- しばらく記憶を使わせずに話したい → [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)（アプリ、機能）
- 大きな資料を漏れなく読ませたい → [添付ファイルはどこまで読まれるか](../app/how-attachments-are-read.md)（アプリ・API、機能）
- 最新の情報を踏まえて答えてほしい → [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)（アプリ、比較）
- 検索より、じっくり考えて答えてほしい → [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)（アプリ、比較）
- 調べものに、どこまで時間をかけさせるか決めたい → [web 検索・リサーチ・拡張思考の使い分け](../app/search-research-thinking.md)（アプリ、比較）

### Claude Code の基本操作

- Claude Code の入力欄でできることを最初に知りたい → [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)（Claude Code、機能）
- 確認を減らしたいが、どのモードにすればよいか分からない → [権限モードの選び方](../cli/permission-modes-overview.md)（Claude Code、機能）
- 既定の権限モードで、何が確認なしで実行されるのか知りたい → [権限モードの選び方](../cli/permission-modes-overview.md)（Claude Code、機能）
- 試しにやらせて、駄目なら元に戻したい → [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)（Claude Code、機能）
- コミットや PR の作成をどこまで任せてよいか決めたい → [git との付き合い方](../cli/working-with-git.md)（Claude Code、考え方）

### 文脈と指示を仕組みにする

- CLAUDE.md に何を書けばよいか知りたい → [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)（Claude Code、機能）
- ビルドやテストのコマンドと落とし穴を、毎回説明せずに伝えておきたい → [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)（Claude Code、機能）
- CLAUDE.md から何を削ればよいか知りたい → [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)（Claude Code、機能）
- 常に守らせたい規則と、ときどき使う手順の置き場所を分けたい → [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)（Claude Code、比較）
- 応答の口調や形式を変えたいが、どこに書けばよいか分からない → [CLAUDE.md・rules・スキル・出力スタイルの違い](../extend/claude-md-vs-rules-skills-styles.md)（Claude Code、比較）
- 繰り返す作業の手順を、名前で呼べるようにしたい → [スキルの作り方](../extend/writing-skills.md)（Claude Code・アプリ、機能）
- 自分用のスラッシュコマンドを作りたい → [スキルの作り方](../extend/writing-skills.md)（Claude Code・アプリ、機能）
- 作ったスキルが効いているかを、体感ではなく確かめたい → [スキルの作り方](../extend/writing-skills.md)（Claude Code・アプリ、機能）
- ブラウザからコピーして貼っているデータを、直接取りに行かせたい → [MCP をつなぐ](../extend/connecting-mcp.md)（Claude Code・アプリ、機能）
- 社内のツールや外部のサービスを、Claude から使いたい → [MCP をつなぐ](../extend/connecting-mcp.md)（Claude Code・アプリ、機能）

### 確かめる

- どこまでやったら終わりかを、はっきり伝えたい → [「完了」を定義して渡す](../verify/define-done.md)（アプリ・Claude Code・API、考え方）
- どのコマンドがどう返れば完了かを、依頼に書いて渡したい → [「完了」を定義して渡す](../verify/define-done.md)（アプリ・Claude Code・API、考え方）
- 席を外す前に、終わりの条件を決めて渡したい → [「完了」を定義して渡す](../verify/define-done.md)（アプリ・Claude Code・API、考え方）
- 見ていなかった作業が本当に済んだかを、短い時間で確かめたい → [報告ではなく証拠を求める](../verify/evidence-not-reports.md)（Claude Code・アプリ、考え方）
- テストが通るまで終わらせたくない → [検証の階段](../verify/verification-ladder.md)（Claude Code、考え方）・[/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)（Claude Code、機能）
- 任せる範囲に合わせて、確かめ方の強さを選びたい → [検証の階段](../verify/verification-ladder.md)（Claude Code、考え方）
- 答えの中の事実が正しいか確かめたい → [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)（アプリ・Claude Code・API、手順）
- 渡した資料に書いてあることだけで答えさせたい → [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)（アプリ・Claude Code・API、手順）
- 要約が原文に書いてあるとおりかを照らしたい → [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)（アプリ・Claude Code・API、手順）
- テストや採点のスクリプトを、Claude に書き換えさせたくない → [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)（Claude Code、考え方）
- テストを書き換えずに直すよう、依頼の段階で伝えたい → [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)（Claude Code、考え方）
- 書いた本人ではない目でレビューさせたい → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)（Claude Code・アプリ、考え方）
- AI が書いたコードに脆弱性がないか見させたい → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)（Claude Code・アプリ、考え方）

### 評価と実験

- Claude に長く改善を回させても、方向を誤らせたくない → [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)（Claude Code・API、考え方）
- 良くなった・悪くなったという自分の感じを、どこまで信じてよいか知りたい → [体感と実測](../eval/felt-vs-measured.md)（アプリ・Claude Code、判断）
- AI を使った効果を、感覚ではなく記録で確かめたい → [体感と実測](../eval/felt-vs-measured.md)（アプリ・Claude Code、判断）
- CLAUDE.md を変えて良くなったか知りたい → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)（アプリ・Claude Code・API、手順）
- プロンプトや手順書を直した効果を比べたい → [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)（アプリ・Claude Code・API、手順）
- Claude に回させる前に、評価の仕組みが信用できるか確かめたい → [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)（Claude Code・API、考え方）
- 評価の仕組みが正しく採点しているか確かめてから使いたい → [検証器そのものを確かめる（red/green・手で計算したケース）](../eval/test-the-verifier.md)（Claude Code、手順）
- どの変更がなぜ効いたかを、後から追えるようにしたい → [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)（Claude Code、手順）

### 仕組みで縛る

- 例外なく守らせたい規則がある → [お願いを鍵に移す判断](../enforce/when-to-lock.md)（Claude Code・アプリ・API、考え方）
- .env や migrations を絶対に触らせたくない → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)（Claude Code、機能）・[フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)（Claude Code、機能）
- よく使う安全なコマンドは、毎回確認させたくない → [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)（Claude Code、機能）
- auto モードに任せて大丈夫か → [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)（Claude Code・アプリ、機能）・[サンドボックスで封じ込める](../enforce/sandboxing.md)（Claude Code、機能）
- 確認なしで進めつつ、危ない操作だけは止めたい → [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)（Claude Code・アプリ、機能）
- 確認を減らしても、壊されたり外へ送られたりしないようにしたい → [サンドボックスで封じ込める](../enforce/sandboxing.md)（Claude Code、機能）
- Docker や devcontainer の中で Claude Code を動かすべきか決めたい → [サンドボックスで封じ込める](../enforce/sandboxing.md)（Claude Code、機能）
- ファイルを編集するたびに、必ず何かを実行したい → [フックの考え方とイベント](../enforce/hooks-basics.md)（Claude Code・API、機能）
- Claude に頼まずに、規則を毎回確実に守らせたい → [フックの考え方とイベント](../enforce/hooks-basics.md)（Claude Code・API、機能）
- 特定のコマンドを、理由を伝えて止めたい → [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)（Claude Code、機能）

### 安全とデータ

- 安全のために、最低限どこまで設定すればよいか知りたい → [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)（アプリ・Claude Code・API、比較）
- アプリと Claude Code で、既定の安全の設定がどう違うか知りたい → [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)（アプリ・Claude Code・API、比較）
- 入力した内容が学習に使われるか知りたい → [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)（アプリ・Claude Code・API、考え方）
- 記録を残さずに相談したい → [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)（アプリ・Claude Code・API、考え方）
- 消した会話が、提供元にいつまで残るか知りたい → [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)（アプリ・Claude Code・API、考え方）
- 外部の資料を、安全に読ませたい → [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)（アプリ・Claude Code・API、考え方）
- メールや Web を読ませつつ、社内のデータにもつなぎたい → [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)（アプリ・Claude Code・API、考え方）
- 入れた拡張が安全かを確かめたい → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)（Claude Code・アプリ、手順）
- Claude が足そうとしているパッケージが、本物か確かめたい → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)（Claude Code・アプリ、手順）
- .env や API キーを、絶対に読ませたくない → [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)（Claude Code・アプリ、手順）
- 本番のデータベースやリモートのブランチに触らせたくない → [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)（Claude Code・アプリ、考え方）
- 取り返しのつかない操作の前には、必ず止めてほしい → [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)（Claude Code・アプリ、考え方）

### 任せて並べる

- AI にどこまで任せてよいか、線を引きたい → [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)（アプリ・Claude Code、考え方）
- 席を外している間も進めてほしい → [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)（Claude Code・アプリ、考え方）・[/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)（Claude Code、機能）
- 長い作業を任せたい → [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)（Claude Code・アプリ、考え方）
- 条件を満たすまで、自分で作業を続けさせたい → [/goal（完了するまで続けさせる）](../delegate/goal-until-done.md)（Claude Code、機能）
- 何本まで並べてよいか決めたい → [並列の上限は人間が決める](../delegate/humans-set-the-parallel-limit.md)（Claude Code、考え方）
- 複数の作業を同時に進めたい → [並列の方式の選び方](../delegate/choosing-parallel-modes.md)（Claude Code、比較）

### 判断と理解を守る

- AI と組んだ作業の失敗を、自分の側から振り返りたい → [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)（アプリ・Claude Code、判断）
- Claude の賛成を、方針が正しい根拠にしてよいか知りたい → [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)（アプリ・Claude Code、判断）
- 頭打ちになった方針を、続けるかやめるか決めたい → [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)（アプリ・Claude Code、判断）
- Claude の「もう打ち手がない」を、やめる根拠にしてよいか判断したい → [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](../judgment/decide-when-to-quit.md)（アプリ・Claude Code、判断）
- AI を使いながら、ほかの人と違う案を出したい → [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)（アプリ・Claude Code、判断）
- コンテストの上位解法や解説を AI に要約させて学びたい → [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)（アプリ・Claude Code、判断）

### 費用と利用上限

- /clear すれば上限が戻るのか知りたい → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)（アプリ・Claude Code、考え方）
- 上限がいつ戻るのか知りたい → [利用上限の仕組み（面をまたいで共有する枠）](../cost/how-usage-limits-work.md)（アプリ・Claude Code、考え方）
- 何が使用量を食っているのか知りたい → [上限を早く使う要因](../cost/what-uses-up-limits.md)（アプリ・Claude Code、考え方）
- /usage の内訳から、何を減らせばよいかを読み取りたい → [上限を早く使う要因](../cost/what-uses-up-limits.md)（アプリ・Claude Code、考え方）
- 上限に当たらないように、使い方を節約したい → [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)（アプリ・Claude Code・API、考え方）

### 日本語で使う

- 日本語の出力を、いつも同じ文体と表記にしたい → [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)（アプリ・Claude Code・API、考え方）
- Claude Code の返事を、いつも日本語にしたい → [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)（Claude Code・アプリ・API、手順）
- 最後の返事が英語のときは、自動で日本語に直させたい → [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)（Claude Code・アプリ・API、手順）
- 文書を、です・ますか、だ・であるのどちらかに揃えたい → [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)（アプリ・Claude Code、手順）
- チームの文書を、いつも同じ文体で書かせたい → [です・ます／だ・であるを揃える](../japanese/consistent-politeness.md)（アプリ・Claude Code、手順）
- 社内の用語集どおりの表記で書かせたい → [表記ゆれと漢字の開き](../japanese/consistent-notation.md)（アプリ・Claude Code、手順）
- 文体や表記の決まりを、毎回自動で守らせたい → [textlint をフックで回す](../japanese/textlint-hook.md)（Claude Code、手順）

### 用途別レシピ

- エラーの原因を突き止めて直させたい → [バグを直す](../recipes/fix-a-bug.md)（Claude Code・アプリ、手順）

### 組織・チームで使う

- AI で増えた PR を、チームでレビューできる量に合わせて流したい → [レビューのボトルネックと疲労](../team/review-bottlenecks.md)（Claude Code、考え方）

### 古くなった助言と変更の記録

- 前は効いた書き方や設定を、今はどうすればよいか知りたい → [古くなった助言の台帳](../changes/outdated-advice-ledger.md)（アプリ・Claude Code・API、台帳）
- ネットで見た小技が今も使えるか確かめたい → [古くなった助言の台帳](../changes/outdated-advice-ledger.md)（アプリ・Claude Code・API、台帳）
- 「think hard」や「よく考えて」が効くのか知りたい → [古くなった助言の台帳](../changes/outdated-advice-ledger.md)（アプリ・Claude Code・API、台帳）

<!-- textlint-enable -->
<!-- gen:end signs goal -->

## 置かれた状況から引く {#by-situation}

置かれた状況の節は、自分では変えにくい周りの条件から引く。チームで導入する、AI を禁じる大会に向けて練習する、といった状況である。状況が決める制約は、困りごとが起きる前に知っておくと効く。

状況の行は、題材の入口のページや、状況ごとの準備のページへ進む。古い記事や設定を引き継いだ状況なら、<!-- link:begin outdated-advice-ledger#find-in-your-setup -->[古くなった助言の台帳 › 自分の設定や記事で見つける](../changes/outdated-advice-ledger.md#find-in-your-setup)<!-- link:end --> で、いま使っている助言が古くなっていないかを確かめられる。

<!-- gen:begin signs situation -->
<!-- textlint-disable -->

### 入口と地図

- この辞典を初めて開いた → [この辞典の引き方](how-to-use.md)（案内）
- 辞典の内容に誤りや古い情報を見つけた → [この辞典の引き方](how-to-use.md)（案内）
- 読んでいる記事がアプリ・Claude Code・API のどれの話か分からない → [全体地図：Claude の面と層](product-map.md)（アプリ・Claude Code・API、案内）
- 毎日使っているが、使いこなせている気がしない → [ロードマップ（委任の段階別）](roadmap.md)（案内）

### 基礎：なぜそうなるか

- Web ページやメールを読ませるのが不安 → [データと命令を区別できない（prompt injection の原理）](../basics/data-vs-instructions.md)（アプリ・Claude Code・API、考え方）・[プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)（アプリ・Claude Code・API、考え方）・[三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)（アプリ・Claude Code・API、考え方）

### モデル・effort・思考

- アプリと Claude Code と API で、同じモデルなのに振る舞いが違う気がする → [effort の段階と使い分け](../models/effort-levels.md)（アプリ・Claude Code・API、機能）
- 「性能が落とされた」という話を見かけ、自分の環境でも起きているか確かめたい → [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)（Claude Code・アプリ・API、手順）

### 文脈を整える

- 長い作業の途中で区切りがついた → [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)（アプリ・Claude Code、考え方）
- 期待と違う返事が来て、訂正を書こうとしている → [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)（アプリ・Claude Code、考え方）
- 一つの会話では終わらない作業を任せている → [handoff 文書と document-and-clear](../context/handoff-documents.md)（Claude Code・アプリ、手順）
- 大きなコードベースで作業している → [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)（Claude Code・アプリ、考え方）

### Claude Code の基本操作

- Claude の変更が大きくなり、どこで区切ればよいか分からない → [git との付き合い方](../cli/working-with-git.md)（Claude Code、考え方）

### 文脈と指示を仕組みにする

- CLAUDE.md が長くなってきた → [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)（Claude Code、機能）
- 昔の記事のとおり、コマンド用のフォルダに Markdown を置いている → [スキルの作り方](../extend/writing-skills.md)（Claude Code・アプリ、機能）
- チームで同じ外部ツールへの接続を使いたい → [MCP をつなぐ](../extend/connecting-mcp.md)（Claude Code・アプリ、機能）

### 確かめる

- 長い作業を任せて、途中は見ないつもりでいる → [検証の階段](../verify/verification-ladder.md)（Claude Code、考え方）
- 自分の目で全部レビューする時間がない → [書いた本人ではない者にレビューさせる](../verify/independent-review.md)（Claude Code・アプリ、考え方）

### 評価と実験

- スコアやテストを目標に、Claude に試行を繰り返させている → [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)（Claude Code・API、考え方）
- 何十通りも試させて、いちばん良かった版を採っている → [選択圧：良かった版を選び続ける罠](../eval/selection-pressure.md)（Claude Code・API、考え方）

### 仕組みで縛る

- スクリプトやテストを、確認なしで実行させたい → [サンドボックスで封じ込める](../enforce/sandboxing.md)（Claude Code、機能）

### 安全とデータ

- Claude に任せる範囲を広げようとしている → [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)（アプリ・Claude Code・API、比較）
- コネクタや MCP を増やして、何でもできる構成になっている → [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)（アプリ・Claude Code・API、考え方）
- 便利そうな MCP やプラグインを見つけた → [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)（Claude Code・アプリ、手順）
- 認証情報のあるマシンで、Claude Code に作業を任せる → [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)（Claude Code・アプリ、手順）

### 任せて並べる

- 評価の基準まで AI に作らせている → [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)（アプリ・Claude Code、考え方）
- 初めて Claude Code を無人で走らせる → [任せ方の段階と、無人で走らせる前の五つの問い](../delegate/five-questions-before-delegating.md)（Claude Code・アプリ、考え方）
- マシンや予算に余裕があるので、並べる本数を増やそうとしている → [並列の上限は人間が決める](../delegate/humans-set-the-parallel-limit.md)（Claude Code、考え方）

### 判断と理解を守る

- AI に任せる範囲が広がってきて、自分の判断に自信が持てない → [人の側の五つの落とし穴（総論）](../judgment/human-pitfalls.md)（アプリ・Claude Code、判断）
- 評価のしかたや方針の選び方まで AI に任せている → [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)（アプリ・Claude Code、判断）
- 複数の AI にレビューさせて、全部が問題なしと答えた → [同意は根拠に数えない（AI レビュアーの一致を含む）](../judgment/agreement-is-not-evidence.md)（アプリ・Claude Code、判断）
- 順位や採択を競う場で、AI の案をそのまま使おうとしている → [AI の案は「みんなの案」（均質化）](../judgment/ai-ideas-are-everyones.md)（アプリ・Claude Code、判断）
- 新しいライブラリや手法を、AI と一緒に覚えたい → [AI で新しい技術を学ぶ（生成させた後に理解を確かめる）](../judgment/learning-with-ai.md)（アプリ・Claude Code、判断）

### 費用と利用上限

- 節約のコツをいろいろ試したが、あまり変わらない → [節約の優先順位（手戻りを減らすのが先）](../cost/saving-priorities.md)（アプリ・Claude Code・API、考え方）

### 日本語で使う

- 日本語の指示を足しても揃わず、仕組みにすべきか迷っている → [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)（アプリ・Claude Code・API、考え方）
- チームで日本語の文書を Claude に書かせる → [日本語の出力を揃える：お願いで足りること、仕組みが要ること](../japanese/align-japanese-output.md)（アプリ・Claude Code・API、考え方）
- 日本語のドキュメントを Claude Code で大量に書かせている → [textlint をフックで回す](../japanese/textlint-hook.md)（Claude Code、手順）

### コンテストで使う

- 出る大会で、AI をどこまで使ってよいか確かめたい → [大会の規則の早見（禁止・部門分け・許可と開示）](../contest/competition-rules.md)（考え方）

<!-- textlint-enable -->
<!-- gen:end signs situation -->

## 同じ言葉が複数のページに当たるとき {#disambiguation}

同じ言葉の行に複数のページが並ぶことがある。選び方の目安は次の 3 つである。

- 困りごとの行では、症状のページを先に開く。症状のページで原因を絞ってから、振り分けられた対処のページへ進む。対処のページから入ると、別の原因を疑う機会を飛ばしやすい。
- 面の印が付いた行では、いま使っている面のページを開く。アプリと Claude Code は手段が違うことが多く、同じ問いでも手順は別になる。
- 型の印が付いた行では、考え方のページは「なぜそうなるか」を、手順のページは「どう進めるか」を答える。理由が分からないまま手順だけ試して外れたときは、考え方のページに戻る。

どれにも当たらないときは、<!-- link:begin term-index#how-to-read -->[用語索引と旧名の対応 › 引き方](term-index.md#how-to-read)<!-- link:end --> で名前から探し直す。それでも見つからない言葉は、この辞典がまだ扱っていない可能性がある。誤りや抜けの報告のしかたは <!-- link:begin how-to-use#report -->[この辞典の引き方 › 誤りや古い情報の報告](how-to-use.md#report)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [失敗の二つの軸と診断の入口](six-causes.md)
- [この辞典の引き方](how-to-use.md)
- [用語索引と旧名の対応](term-index.md)
- [古くなった助言の台帳](../changes/outdated-advice-ledger.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
