---
id: handoff-documents
title: handoff 文書と document-and-clear
aliases: [引き継ぎ文書, HANDOFF.md, 書き出してから /clear, document and clear]
type: recipe
field: context
chapter: 書き出す
order: 70
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発, 文章, 調べもの]
summary: 目的と完了の条件・今の状態と根拠・試して駄目だったこと・次の一手を文書に書かせてから会話を新しくし、その文書から再開する。要約の損失を避けたい長い作業に向く。
signs:
  - {type: goal, text: 長い作業を明日も続けたい}
  - {type: goal, text: 要約に任せず、次の会話に持ち越すものを自分で選びたい}
  - {type: situation, text: 一つの会話では終わらない作業を任せている}
prerequisites: [when-to-start-fresh]
related: [compact-and-auto-compact#compact-or-clear, progress-files, keep-failure-lessons, promises-after-compaction, resume-and-branch, define-done, evidence-not-reports, long-running-agent-context, progress-logs-for-long-jobs, tidy-the-desk]
tracks: [clear]
outdated_advice: []
sources: [cc-docs-best-practices, cc-docs-commands, cc-docs-context-window, dsebastien-code-tips-best-practices, classmethod-code-keep-sessions-short, crystal-method-compact-clear, arxiv-2607-07744]
volatility: 低
sections:
  - {title: 先に決めておく完了と証拠, anchor: guard}
  - {title: 書かせる四項目, anchor: four-items}
  - {title: 置き場所（圧縮で消えない所）, anchor: where}
  - {title: 新しい会話での再開の仕方, anchor: resume}
  - {title: 引き継ぎがうまくいったかの確かめ方, anchor: check}
  - {title: 引き継いだのにうまくいかないとき, anchor: troubleshoot}
  - {title: /compact との使い分け, anchor: vs-compact}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：Claude に 4 項目の文書を書かせてから会話を新しくし、その文書から長い作業を再開できる。
    - **いつ引くか**：長い作業を明日も続けたいとき。要約に任せず、次の会話に持ち越すものを自分で選びたいとき。
    - **前提**：<!-- link:begin when-to-start-fresh -->[新しい会話を始めるタイミング](when-to-start-fresh.md)<!-- link:end -->

<!-- textlint-disable -->
別名：引き継ぎ文書・HANDOFF.md・書き出してから /clear・document and clear
<!-- textlint-enable -->

handoff 文書と document-and-clear は、会話を捨てる前に続きに要るものをファイルに書き出させ、新しい会話で読ませる進め方である。要約では Claude が残すものを決める。この方法では、残すものを自分で決められる。手順は 5 段である。書かせる、読んで直す、置く、区切る、再開して言い直させる。

## 先に決めておく完了と証拠 {#guard}

引き継ぎ文書を書かせる前に、この作業の完了と、完了の証拠の形を決めておく。文書の中身の半分は、この 2 つで決まるからである。

- **完了**：どのコマンドがどう返れば終わりか、変えてはならないものは何か。決め方は <!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end --> にある。これが決まっていないと、文書の「目的と完了の条件」が曖昧になり、新しい会話が途中で終わったと思い込む。
- **証拠**：現状を「通っている」と書かせるなら、実行したコマンドと出力を付けさせる。受け取り方は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](../verify/evidence-not-reports.md#what-counts)<!-- link:end --> にある。根拠のない「通った」は、次の会話にそのまま持ち越される。

文書に書いた決めごとは、圧縮や /clear の後に守られるとは限らない。例外を許さないものは、<!-- link:begin promises-after-compaction#where-to-put -->[圧縮で消えない場所に約束を置く › 約束の種類ごとの置き場所](promises-after-compaction.md#where-to-put)<!-- link:end --> に従って、読み直される場所や deny ルールに置く。

## 書かせる四項目 {#four-items}

引き継ぎ文書は、次の 4 項目で書かせる。実務家の間で同じ形が繰り返し勧められている（根拠：中）。

1. **目的と完了の条件**：何を達成すれば終わりか。終わりを確かめるコマンドと、返すべき結果。
2. **現状と根拠**：何が通り、何が落ちているか。それぞれに、根拠のコマンドと出力の要点を付ける。確かめたことと推測を分ける。
3. **試して駄目だったこと**：試した方法、駄目だった理由、分かったこと。同じ案の再提案を防ぐ。何を残すかは <!-- link:begin keep-failure-lessons#what-to-keep -->失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか（準備中）<!-- link:end --> にある。
4. **次の一手**：最初にやることを 1 つ。その後の見通し。人に聞くべきこと。聞くべきことの分け方は <!-- link:begin progress-files#decided-vs-open -->進捗ファイルで、途中から再開できるようにする › 決めたことと、聞くべきことを分ける（準備中）<!-- link:end --> にある。

依頼は次のように出す。項目を指定しないと、経過の要約が中心になり、完了の条件と試して駄目だったことが抜けやすい。

<!-- gen:begin snippet handoff-documents/handoff-request -->
<!-- textlint-disable -->

??? example "雛形：handoff 文書を書かせる依頼（4 項目）"

    ```markdown
    ここまでの作業を、`HANDOFF.md` に書き出して。新しい会話の Claude が、この文書だけで続きを始められるようにする。次の 4 項目で書く。

    1. 目的と完了の条件：何を達成すれば終わりか。終わりを確かめるコマンドと、そのコマンドが返すべき結果。変えてはならないもの。
    2. 現状と根拠：いま何が通り、何が落ちているか。それぞれの根拠として、実行したコマンドと、その出力の要点。確かめたことと、推測を分けて書く。
    3. 試して駄目だったこと：試した方法、駄目だった理由、分かったこと。同じ案をもう一度出さないための記録。
    4. 次の一手：最初にやることを 1 つ。その後の見通し。人に聞くべきこと。

    書き終えたら止まる。実装の続きはしない。1 画面に収まる長さにする。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet handoff-documents/handoff-request -->

何度も使うなら、スキルにしておく。次の例は、人が `/handoff` と入力したときだけ動く。書いた後の `/clear` は人が打つ。

<!-- gen:begin snippet handoff-documents/skill-handoff -->
<!-- textlint-disable -->

??? example "雛形：.claude/skills/handoff/SKILL.md（人が呼んだときだけ動くスキル）"

    ```markdown
    ---
    name: handoff
    description: 作業を区切るとき、次の会話に持ち越す HANDOFF.md を書く。人が /handoff と入力したときだけ使う
    disable-model-invocation: true
    ---

    # handoff 文書を書く

    作業を一度区切るために、`HANDOFF.md` を書く。書いたら止まり、実装の続きはしない。

    1. `git status` と `git log -5 --oneline` を見て、変更の現状をつかむ。
    2. 完了の条件のコマンドを実行し、結果を確かめる。実行していない結果を、通ったとは書かない。
    3. 次の 4 項目で `HANDOFF.md` を書く。既にあれば上書きする。
       - 目的と完了の条件（終わりを確かめるコマンドと、返すべき結果、変えてはならないもの）
       - 現状と根拠（通ること・落ちること。それぞれ実行したコマンドと出力の要点。確かめたことと推測を分ける）
       - 試して駄目だったこと（方法・理由・分かったこと）
       - 次の一手（最初にやること 1 つ、その後の見通し、人に聞くべきこと）
    4. 最後に、書いた場所と、次の会話の最初に打つ文を伝える。`/clear` は人が打つ。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet handoff-documents/skill-handoff -->

確かめ：`HANDOFF.md` ができ、4 項目が並び、現状の記述ごとに実行したコマンドが付いている。

**書かせたら、そのまま使わずに自分で読む**。この読む手間が、要約に任せる場合との違いである。手間をかける代わりに、取りこぼしを自分で防げる。現状の記述が実際と違っていれば、この場で直させる。長すぎる文書は、新しい会話の文脈を最初から埋めてしまう。1 画面に収まる長さにする。書きすぎの副作用は <!-- link:begin keep-failure-lessons#too-much -->失敗の教訓は捨てずに書き残す › 書き残しすぎの副作用（準備中）<!-- link:end --> を見る。

確かめ：自分が読んで、完了の条件のコマンドを実際に流し、文書の記述と結果が合っている。

## 置き場所（圧縮で消えない所） {#where}

文書は、会話の外のファイルに置く。会話の中に書いただけの文書は、圧縮で要約に溶けうるし、`/clear` で消える。ファイルならどちらの後でも読み直せる。

- 作業のフォルダの直下に `HANDOFF.md` として置く。作業が複数あるなら、`HANDOFF-parser.md` のように名前で分ける。
- CLAUDE.md には書かない。CLAUDE.md は毎回読み込まれるので、期限のある引き継ぎを入れると、終わった後も場所を取り続ける。常に守らせる決めごとだけを CLAUDE.md に置く。
- 複数のファイルに分けて持ちたくなったら、<!-- link:begin progress-files#files -->進捗ファイルで、途中から再開できるようにする › ファイルの分け方（準備中）<!-- link:end --> の分け方に移る。引き継ぎ文書は 1 回の区切りのための 1 枚で、進捗ファイルは何度も更新して使い続けるものである。

=== "アプリ"

    アプリでは、書かせた文書の全文を、自分で保存しておく。次の会話は新しいチャットで始め、最初のメッセージに貼るか添付する。Projects など、アプリの保存の仕組みで文書を持ち越せるかは、この辞典では未確認である。

=== "Claude Code"

    Claude Code では、作業のフォルダに `HANDOFF.md` を書かせる。`/clear` は空の文脈で新しい会話を始めるもので、前の会話は `/resume` で戻れる。ただし、戻った会話は元の長さのままなので、頼りにするのは文書のほうにする。

確かめ：新しい会話を開く前に、ファイルがフォルダにあり、自分で保存してある。

## 新しい会話での再開の仕方 {#resume}

文書を書かせて確かめたら、会話を新しくして、文書から再開する。Claude Code では `/clear` を使い、アプリでは新しいチャットを開く。新しくする判断の目安は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](when-to-start-fresh.md#signals)<!-- link:end --> にある。

新しい会話の最初に出す依頼は、文書を読んだ後、手を動かす前に、言い直させる形にする。

<!-- gen:begin snippet handoff-documents/resume-request -->
<!-- textlint-disable -->

??? example "雛形：新しい会話の最初に出す再開の依頼"

    ```markdown
    `HANDOFF.md` を読んで、作業を引き継いでほしい。まだ手を動かさず、次の 3 つを自分の言葉で答える。

    - 目的と、終わりを確かめるコマンド
    - 現状の根拠になっているコマンドを実行した結果が、文書の記述と合っているか
    - 最初にやる 1 つのことと、試して駄目だったことのうち繰り返してはならないもの

    食い違いがあれば、文書より、実行して見えた事実を正とする。私が確認するまで、次の一手には進まない。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet handoff-documents/resume-request -->

言い直させるのは、読み違いを作業の前に見つけるためである。Claude が目的や次の一手を取り違えていても、答えを読めば分かる。取り違えたまま作業に入ると、直すのは作業の後になる。

確かめ：Claude の言い直しが、文書の 4 項目と合っている。根拠のコマンドを流した結果も、文書と合っている。

前の会話に戻って別の案を試したいときは、再開ではなく分岐である。やり方は <!-- link:begin resume-and-branch#branch -->セッションに名前を付けて再開・分岐する › 分岐して別案を試す（準備中）<!-- link:end --> にある。

## 引き継ぎがうまくいったかの確かめ方 {#check}

引き継ぎ全体の確かめは、新しい会話が、前の会話の続きとして動いているかで見る。次の 3 点を見る。

- **同じ失敗を繰り返していない**：「試して駄目だったこと」に書いた案を、再び提案していない。
- **完了の判定が文書どおり**：完了を、文書にあるコマンドと結果で判定している。説明と事実が食い違えば、<!-- link:begin evidence-not-reports#facts-win -->[報告ではなく証拠を求める › 説明と事実が食い違ったら](../verify/evidence-not-reports.md#facts-win)<!-- link:end --> のとおり、実行して見えた事実を正とする。
- **次の一手から始まっている**：既に済んだ作業をやり直さず、文書の「次の一手」から進んでいる。

3 つのどれかが外れたら、新しい会話の問題より先に、文書の問題を疑う。文書に書いていないことは、新しい会話は知らないからである。

!!! example "判断例：文書を書かせた後の確かめ方"
    - **状況**：パーサーの修正を 2 日続けた会話で、HANDOFF.md を書かせた。現状の項目に「テストは全部通る」とある。
    - **迷う候補**：書かれた内容を信じて `/clear` する。先に完了のコマンドを自分で流してから `/clear` する。
    - **選んだもの**：先に流す。実行すると 2 件が落ちていた。
    - **理由**：文書は Claude が書いた報告で、事実ではない。`/clear` の後は、誤った現状が確かめられないまま次の会話の出発点になる。落ちている 2 件を現状に書き直させてから区切った。

## 引き継いだのにうまくいかないとき {#troubleshoot}

引き継いだ後に起きやすい失敗と、直す場所を並べる。

- **同じ案をまた提案される**：「試して駄目だったこと」が薄い。方法と理由を足して書き直させる。書き残す範囲は <!-- link:begin keep-failure-lessons#what-to-keep -->失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか（準備中）<!-- link:end --> にある。
- **前に決めた約束が守られない**：約束が文書にしかなく、読み直される場所にない。置き場所の移し方は、読み直される場所を整理した <!-- link:begin promises-after-compaction#what-comes-back -->[圧縮で消えない場所に約束を置く › 読み直される場所と、要約に溶ける約束](promises-after-compaction.md#what-comes-back)<!-- link:end --> にある。
- **終わっていないのに終わったと言う**：完了の条件が測れる形で書かれていない。<!-- link:begin define-done#why-it-stops -->[「完了」を定義して渡す › 終わったように見えた所で止まる](../verify/define-done.md#why-it-stops)<!-- link:end --> を見て、完了の条件を書き直す。
- **文書が古い**：書いた後に作業を続けて、文書と実際がずれた。続きの作業をした日は、区切る前に書き直させる。
- **長時間のジョブの状況が見えない**：1 回の引き継ぎでは足りない。<!-- link:begin progress-logs-for-long-jobs -->長時間ジョブの進捗ログを設計する（準備中）<!-- link:end --> のように、進捗を定期的に書き出す仕組みを足す。

## /compact との使い分け {#vs-compact}

長い作業の続け方には、2 つの立場がある。割れる論点なので、三段で示す。

- **公式の立場**：無関係な作業に移るときは `/clear` を使うよう勧めている。`/compact` には、残したい焦点を指示できる。指示の仕方は <!-- link:begin compact-and-auto-compact#focused-compact -->[/compact と自動圧縮 › /compact に焦点を指示する](compact-and-auto-compact.md#focused-compact)<!-- link:end --> にある。
- **実践者の幅**：焦点を指定して `/compact` に頼る人と、文書に書き出してから `/clear` する人に分かれる。書き出す側は、圧縮では細部（ファイルパス、エラーメッセージ、行番号）が変わりうるので、何を残すかを自分で決めたいと言う（根拠：弱。実務家の経験談）。
- **この辞典の推奨**：要約で失いたくない作業は、書き出して `/clear` する。短い作業や、同じ話題をそのまま続けるだけなら、焦点を指示した `/compact` で足りる。

引き継ぎ文書を新しいセッションに渡すと、性能最適化のベンチマークで追加の改善が出たという報告がある（根拠：弱。PERFOPT-Bench、2026 年、8 系列のパイロット）。著者自身が、予算が交絡した探索的な結果だと認めている。この辞典は、効果の大きさの根拠にしない。

!!! example "判断例：/compact か、書き出して /clear か"
    - **状況**：リファクタリングを 3 日続けている。途中で試して戻した方法が複数あり、テストの落ち方も毎日変わる。
    - **迷う候補**：焦点を指示して `/compact` する。HANDOFF.md に書き出して `/clear` する。
    - **選んだもの**：書き出して `/clear` する。
    - **理由**：試して駄目だった方法と、どのコマンドで確かめたかは、要約で薄まると取り返しにくい。文書に書けば、残るものを自分で選べる。逆に、同じ修正を続けているだけの数十分なら、焦点を指示した `/compact` で足りる。

両者の関係は <!-- link:begin compact-and-auto-compact#compact-or-clear -->[/compact と自動圧縮 › 圧縮か、書き出して /clear か](compact-and-auto-compact.md#compact-or-clear)<!-- link:end --> にも書いてある。API で長く動くエージェントを組む場合は、<!-- link:begin long-running-agent-context -->長時間エージェントのコンテキスト管理（準備中）<!-- link:end --> の手段を使う。4 つの動作の全体は <!-- link:begin tidy-the-desk -->[机を整える：新鮮さ・巻き戻し・書き出し・委任](tidy-the-desk.md)<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [新しい会話を始めるタイミング](when-to-start-fresh.md)

**次に読む**

- 進捗ファイルで、途中から再開できるようにする（準備中）
- 決定を文書に残す（ADR と週次アップデート）（準備中）

**関連**

- [/compact と自動圧縮 › 圧縮か、書き出して /clear か](compact-and-auto-compact.md#compact-or-clear)
- 失敗の教訓は捨てずに書き残す（準備中）
- [圧縮で消えない場所に約束を置く](promises-after-compaction.md)
- セッションに名前を付けて再開・分岐する（準備中）
- [「完了」を定義して渡す](../verify/define-done.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- 長時間エージェントのコンテキスト管理（準備中）
- 長時間ジョブの進捗ログを設計する（準備中）
- [机を整える：新鮮さ・巻き戻し・書き出し・委任](tidy-the-desk.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Claude Code Tips and Best Practices](https://www.dsebastien.net/claude-code-tips-and-best-practices/)：Sébastien Dubois・英語・確認日 2026-11-04
- [Claude Code のセッションを長くしすぎないために入れた工夫3つ](https://dev.classmethod.jp/articles/claude-code-keep-sessions-short/)：クラスメソッド（DevelopersIO）・確認日 2026-11-04
- [Claude Codeの/clearとは？使い方と使うタイミングをcompactとの違いも解説](https://crystal-method.com/blog/claude-code-compact-clear/)：crystal-method・確認日 2026-11-04
- [PERFOPT-Bench: Evaluating Coding Agents on Software Performance Optimization](https://arxiv.org/abs/2607.07744)：arXiv（Cui, Yingyun ほか）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
