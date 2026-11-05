---
id: postmortems
title: 失敗を仕組みに戻す（ポストモーテム）
aliases: [postmortem, 再発防止, ブレームレスな振り返り]
type: judgment
field: judgment
chapter: 振り返りと再発防止
order: 110
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [縛る, 握る]
prevents: [縛っていない]
pitfalls: []
scenes: [開発, チーム]
summary: AI と組んだ作業の失敗を、誰の誤りかではなくどの仕組みの隙間が許したかで書き、再発防止を CLAUDE.md・フック・レビューの観点のどこに入れるかを決められる。
signs:
  - {type: situation, text: AI に任せた作業で事故が起きたので、再発を防ぎたい}
  - {type: symptom, text: 注意したのに、同じ種類の失敗が別の作業でまた起きた}
prerequisites: [when-to-lock]
related: [retros-without-ai-verdicts, hook-recipes, what-to-put-in-claude-md, grow-review-checklists, keep-failure-lessons, recover-lost-work, record-decisions, deleted-something-important, instructions-ignored, request-lock-table, decide-when-to-quit]
tracks: [claude-md, hooks]
outdated_advice: []
sources: [google-sre-workbook-postmortem-culture, arxiv-2505-13995, collins-premortem]
volatility: 低
sections:
  - {title: 誰がではなく、どの隙間が, anchor: which-gap}
  - {title: 人と AI の操作の時間線, anchor: timeline}
  - {title: 再発防止をどこに入れるか, anchor: where-to-put-fixes}
  - {title: プレモーテムの扱い, anchor: premortem}
  - {title: 判断例, anchor: decision-examples}
  - {title: 人が握るもの, anchor: what-you-hold}
  - {title: 確かめ方, anchor: how-to-check}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：AI との作業の失敗を、誰の誤りでなくどの仕組みの隙間が許したかで書き、再発防止の置き場所を決められる。
    - **いつ引くか**：AI に任せた作業で事故が起きて再発を防ぎたいとき。注意したのに同じ種類の失敗が別の作業でまた起きたとき。
    - **前提**：<!-- link:begin when-to-lock -->[お願いを鍵に移す判断](../enforce/when-to-lock.md)<!-- link:end -->
    - **根拠の強さ**：「誰がでなく仕組みの隙間を問う」型は、定評ある実務の型である（根拠：中。AI との作業で効果を測った研究はなく、AI への当てはめは類推）。プレモーテムは、効果が実証された手法として扱わない。

<!-- textlint-disable -->
別名：postmortem・再発防止・ブレームレスな振り返り
<!-- textlint-enable -->

失敗を仕組みに戻すとは、事故の記録を、人や AI の反省で終わらせず、次に同じ隙間を通れなくする仕組みの変更にまで落とすことである。ポストモーテムは、その記録の書き方である。このページは、書き方と、再発防止を CLAUDE.md・フック・レビューの観点のどこに置くかの決め方を扱う。

## 誰がではなく、どの隙間が {#which-gap}

ポストモーテムは、事実に基づき、個人の判断を含まない文書にする。問うのは「誰が起こしたか」ではなく、「どの仕組みの隙間が許したか」である。Google の SRE の実務書がこの型を示している。アクション項目には単一のオーナーと、測れる完了状態を付け、別のメンバーが記録を確かめる（根拠：中。実務の型）。

AI と組んだ作業では、「誰が」の問いが 2 つの形で現れる。

- **AI のせいにする**：「Claude が勝手に消した」で終わる。AI に注意し直しても、同じ操作を止める仕組みは増えない。
- **自分のせいにする**：「私の頼み方が悪かった」で終わる。次は気をつける、が再発防止になる。人の注意は、疲れた日にも、別の担当者にも、同じようには働かない。

どちらも、仕組みの変更を残さない。隙間の側に置き直すと、問いはこう変わる。

- 起きたことを止める鍵（フック・権限ルール）はあったか。
- 頼んだお願い（CLAUDE.md や会話の指示）はあったか。あったのに破られたのか、そもそもなかったのか。
- 人のレビューの観点に、この種の見落としは入っていたか。

AI が絡む事故の隙間の多くは、お願いしかなく鍵がない形（原因の分類では「縛っていない」）に当たる、と読む。これは辞典の見立てで、件数を数えた研究に拠るものではない（推論・実践例なし）。お願いと鍵の違いは<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end -->が扱う。

振り返りの結論を AI に出させる運用は避ける。AI は自分の判断を肯定する側に寄りやすく、結論は人が出す。理由と進め方は<!-- link:begin retros-without-ai-verdicts#why-not-ai-verdicts -->振り返りで AI に評価させない（集計係にとどめる）<!-- link:end -->が扱う。

## 人と AI の操作の時間線 {#timeline}

ポストモーテムの中心は、人と AI の操作を時刻順に並べた時間線である。誰の操作か、その時点で何が見えていたか、結果はどうだったかを、評価の語なしで書く。「うっかり」「軽率」を入れると、隙間でなく人の話に戻る。

時間線の材料は、セッションの記録（トランスクリプト）から抜き出せる。記録には、秘密が平文で残ることがある。保存場所と読み方、残る期間は版によって変わるので、<!-- link:begin recover-lost-work#transcripts -->[セッション記録から失った作業を取り戻す › トランスクリプトの場所と読み方](../cli/recover-lost-work.md#transcripts)<!-- link:end -->を見る。そこに付いた確認日を読み、自分の版で通じるかを確かめる。伏せ字にしてから共有する。

AI に頼んでよいのは、記録からの事実の抽出と集計である。原因や評価は頼まない。

Before/After で比べる。同じ依頼で、頼む内容だけを変えている。

!!! example "Before：評価を頼む"
    - **依頼**：事故の記録を貼って「私の判断は正しかったですよね？ 原因を教えてください」と聞く。
    - **起きやすいこと**：肯定する物語が返りやすい。ELEPHANT という評価では、一般的な相談で、モデルが利用者を肯定する割合が人より 50 ポイント高かった（72% 対 22%。2025 年の研究。対象は当時の複数のモデル。根拠：中）。この結果を、現行の Claude の傾向にはしない。

!!! example "After：事実の表を頼む"
    - **依頼**：同じ記録を貼って「このログから事実だけを時系列の表にして」「この結論と矛盾するデータを列挙して」と頼む。
    - **足したもの**：評価と原因の判断を外し、表と反証の列挙だけにした。判断は人が下す。

雛形は次のとおりである。動作は確かめていない。

<!-- gen:begin snippet postmortems/timeline-prompt -->
<!-- textlint-disable -->

??? example "雛形：時間線の抽出の依頼（事実の表だけを頼み、原因の判断は頼まない）"

    ```markdown
    添付したセッションの記録（トランスクリプト）から、事故に関わる部分だけを時系列の表にしてください。

    - 列は、時刻・誰の操作か（人・AI・フック）・操作の内容・その直前に画面に出ていたこと・結果
    - 記録にあることだけを書く。原因の推測、評価、誰が悪いかの判断は入れない
    - 記録から読み取れない欄は「不明」と書く
    - 表のあとに、この表と矛盾する記録があれば、その箇所を列挙する

    根本原因の判断と、再発防止の置き場所は、私が決める。ここでは出さないでください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet postmortems/timeline-prompt -->

時間線を書いたら、記録の全体は次の項目の雛形に入れる。ポストモーテムの項目は、要約・影響・時間線・根本原因・うまくいったこと・アクション項目・再発防止の置き場所である。

<!-- gen:begin snippet postmortems/postmortem-entry -->
<!-- textlint-disable -->

??? example "雛形：ポストモーテムの項目（要約・影響・時間線・根本原因・うまくいったこと・アクション項目・再発防止の置き場所）"

    ```markdown
    ## PM-007 共有のステージング環境のデータを、AI が消した

    - 要約：Claude Code に頼んだリファクタリングの途中で、テスト用のデータ初期化スクリプトが、手元の DB ではなく共有のステージング DB に対して実行された
    - 影響：ステージング DB のデータが消え、チームの検証が止まった。復旧に半日かかった（例）
    - 検知：検証担当が、ステージングのデータが空なのに気づいた

    ### 人と AI の操作の時間線

    - 事実だけを書く。「うっかり」「軽率」のような評価の語を入れない
    - 各行に、誰の操作か（人・AI・フックなどの仕組み）、その時点で見えていたもの、結果を書く
    - 時刻（例）｜誰｜操作｜その時点で見えていたもの｜結果
    - 10:02｜人｜スクリプトの整理を依頼した｜接続先は環境変数で切り替わる前提だった｜-
    - 10:15｜AI｜テスト前に初期化スクリプトを実行した｜シェルの環境変数がステージングを指していた｜ステージングのデータが消えた

    ### 根本原因（誰がではなく、どの隙間が許したか）

    - 仕組みの隙間として書く。人の誤りや AI の誤りを原因にしない
    - 例：共有環境を指す接続先で、破壊的なスクリプトを実行できた。止める仕組みがなく、CLAUDE.md の「共有環境に触らない」というお願いだけがあった

    ### うまくいったこと

    - 例：バックアップがあり、半日で戻せた。検証担当がすぐ気づいた

    ### アクション項目（単一のオーナーと、測れる完了状態を付ける）

    - 項目：接続先が共有環境のときに、破壊的なスクリプトの実行を止める
      - オーナー：（1 人の名前）
      - 期日：（日付）
      - 完了状態：安全な環境で同じ操作を再現し、実行が止まることを確かめた記録がある

    ### 再発防止の置き場所（隙間ごとに 1 か所を選ぶ）

    - 鍵（フック・deny ルール）：共有環境を指すときの破壊的な実行を止める
    - CLAUDE.md：なぜ共有環境に触らないのか（理由）と、開発用の接続先の確かめ方
    - レビューの観点：スクリプトを足す PR で、接続先を切り替える仕組みを確かめる
    - 置き場所を選んだ理由：

    ### レビュー

    - 別のメンバーが、評価の語が入っていないことと、アクション項目の完了状態が測れることを確かめた：（日付と名前）
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet postmortems/postmortem-entry -->

## 再発防止をどこに入れるか {#where-to-put-fixes}

再発防止の置き場所は、CLAUDE.md・フック・レビューの観点の 3 つから、隙間の種類で選ぶ。1 つの事故に 3 つ全部を足さず、隙間ごとに 1 か所を選ぶ。

<!-- gen:begin compare 強制力 読み込みの時期 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 強制力 | 読み込みの時期 |
| --- | --- | --- |
| [CLAUDE.md](../extend/what-to-put-in-claude-md.md) | お願い | セッション開始 |
| [フック（hooks）](../enforce/hooks-basics.md) | 鍵 | イベントが起きたとき |

すべて共通：圧縮で残るか 残る。

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 圧縮で残るか -->

置き場所は、機能の表の CLAUDE.md とフックに、機能ではないレビューの観点を足した 3 つから選ぶ。向く隙間と入れるものは次のとおりである。

| 置き場所 | 向く隙間 | 入れるもの |
| --- | --- | --- |
| フック・deny ルール（鍵） | 例外を許さない操作を、機械的に判定できる | 止める操作の条件。例：共有環境を指すときの破壊的な実行 |
| CLAUDE.md（お願い） | 推測できない事情や理由が、AI に伝わっていなかった | コマンド・理由・落とし穴・確かめ方 |
| レビューの観点 | 機械では判定できない見落とし。判断を含む | 見落とした理由から抜き出した観点 |

選ぶ順は次のとおりである。

1. その操作を、パターンで機械的に判定できるか。できるなら鍵にする。注意を 2 回した、強調しても破られた、会話で言った禁止が圧縮で消えた、は鍵に移す合図である。合図は<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end -->と<!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<!-- link:end -->が扱う。フックの組み方は<!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](../enforce/hook-recipes.md#block-dangerous)<!-- link:end -->、用途ごとの鍵の選び方は<!-- link:begin request-lock-table#table -->[お願いと鍵の対応表 › 用途ごとの対応表](../enforce/request-lock-table.md#table)<!-- link:end -->が扱う。
2. 判定できないなら、CLAUDE.md に理由を書くか、レビューの観点にする。CLAUDE.md に残す行と外す行は<!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end -->と<!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](../extend/what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end -->が扱う。例外を許さない禁止を CLAUDE.md だけに置いて終わらせない。
3. 見落としを直した PR から観点を育てる進め方は、<!-- link:begin grow-review-checklists -->[レビューの観点を育てる](../team/grow-review-checklists.md)<!-- link:end -->が扱う。AI のレビュアーへの指示も、同じ観点で育てる。
4. 試して分かったことと、駄目だった理由は、同じ失敗の再提案を防ぐために書き残す。書き方は<!-- link:begin keep-failure-lessons#what-to-keep -->[失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか](../context/keep-failure-lessons.md#what-to-keep)<!-- link:end -->が扱う。

アクション項目には、オーナー 1 人と、測れる完了状態を付ける。完了状態は「フックを足した」ではなく、「安全な環境で同じ操作を再現し、止まることを確かめた記録がある」と書く。確かめ方は<!-- link:begin hook-recipes#verify -->[代表的なフックのレシピ › 常設する前に確かめる](../enforce/hook-recipes.md#verify)<!-- link:end -->が扱う。事故が消去や破壊に当たるときの初動と復旧は、<!-- link:begin deleted-something-important#recover -->[消してはいけないものを消された › まず戻す（復旧の手順）](../symptoms/deleted-something-important.md#recover)<!-- link:end -->が扱う。

## プレモーテムの扱い {#premortem}

プレモーテムとは、計画を始める前に「失敗したと仮定して、その原因を挙げる」検討である。ポストモーテムの逆向きで、隙間を事故の前に探す。このページでは、人同士の検討を補う手段として扱い、効果が実証された手法として紹介しない。

過信を減らす効果はあるとされるが、計画の成果まで改善するかは確かめられていない（根拠：弱。個人による原典の読み直し。未検証）。

AI に使うときは、順序を守る。

1. 人が先に、失敗の原因を自分で書き終える。
2. そのあとで、AI に「人が挙げていない失敗要因」を別枠で挙げさせる。
3. 挙がった要因は、下書きとして人が採否を決める。

先に AI の案を見ると、人の案が引きずられる。この順序は実務の勧めで、効果を測った研究はない（推論・実践例なし）。人が先に書く理由は<!-- link:begin retros-without-ai-verdicts#write-first -->振り返りで AI に評価させない（集計係にとどめる）<!-- link:end -->が扱う。

行う時期は、大きな方針を決めるときと、本番の前が例に挙がる。「本番の 1 か月前」は出典のない例で、決まりではない。自分の作業の大きさで決める。

## 判断例 {#decision-examples}

!!! example "判断例：共有環境のデータを消された"
    - **状況**：Claude Code に頼んだリファクタリングの途中で、テスト用の初期化スクリプトが、共有のステージング DB に対して実行された。データが消えた。CLAUDE.md には「共有環境には触らない」と書いてあった。復旧はできた。
    - **迷う候補**：CLAUDE.md の文を「絶対に」と強め、例を足す。または、接続先が共有環境を指すときの破壊的な実行を、フックで止める。
    - **選んだもの**：フックで止める。CLAUDE.md には、なぜ共有環境に触らないのかの理由と、開発用の接続先の確かめ方だけを残す。完了状態は、安全な環境で再現して止まったことの記録にする。
    - **理由**：書いてあったのに起きたので、隙間は「お願いしかなく、鍵がない」だった。文を強めても、同じ隙間が残る。接続先は機械で判定できるので、鍵にできる。強めた文は、会話の圧縮や長い作業で埋もれやすい。

!!! example "判断例：生成されたテストが実装をなぞるだけだった"
    - **状況**：AI が書いたテストは、実装の返す値をそのまま期待値にしていた。そのためバグを見逃した。先月も別の機能で、同じ種類の見落としがあった。
    - **迷う候補**：テストの形をフックで検査する。または、レビューの観点に「期待値が、仕様でなく実装から写されていないか」を足す。
    - **選んだもの**：レビューの観点に足す。AI のレビュアーへの指示にも同じ観点を入れる。観点を足す PR は、人が承認する。
    - **理由**：期待値が仕様から来たかは、機械では判定できない。フックで止めようとすると、形だけ整えたテストが通ってしまう。判断を含む見落としは、観点として育てるほうが合う。観点が効いたかは、同じ種類の見落としが再び通ったかで確かめる。

## 人が握るもの {#what-you-hold}

AI にポストモーテムの下書きや集計を任せても、次の 3 つは人が握る。

- **根本原因の結論**：どの隙間が許したかを決める。AI の草稿は、そのまま採らない。
- **置き場所の選択と、アクション項目の採否**：鍵・お願い・レビューの観点のどれにするか、誰が持つかを決める。
- **記録の承認**：別のメンバーが、評価の語が入っていないことと、完了状態が測れることを確かめる。

任せてよいのは、時間線の抽出、記録の整形、人が書いたあとの別枠の洗い出しである。

## 確かめ方 {#how-to-check}

ポストモーテムが仕組みに戻せたかは、記録を付けて測る。次を確かめる。

- 根本原因の欄が、人や AI の名指しでなく、仕組みの隙間として書かれているか。
- すべてのアクション項目に、オーナー 1 人と、測れる完了状態があるか。期日を過ぎた項目が残っていないか。
- 完了した項目は、安全な環境で同じ操作を再現して、止まる（または観点で拾える）ことが確かめられているか。
- 同じ種類の隙間で、再び事故が起きていないか。事故に隙間の種類を付けて数え、決まった間隔で見返す。件数が少ないうちは、傾向として読む。
- CLAUDE.md が、鍵にすべき禁止の置き場になっていないか。破られた規則は<!-- link:begin instructions-ignored#diagnosis -->[CLAUDE.md や指示が守られない › 原因を安く確かめる順](../symptoms/instructions-ignored.md#diagnosis)<!-- link:end -->で原因を切り分ける。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Postmortem Culture: Learning from Failure (The Site Reliability Workbook, Chapter 10)](https://sre.google/workbook/postmortem-culture/)：Google・英語・確認日 2026-11-05
- [ELEPHANT: Measuring and understanding social sycophancy in LLMs](https://arxiv.org/abs/2505.13995)：arXiv（Cheng, Myra ほか）・英語・確認日 2026-11-04
- [Pre-mortem](https://corporate.jcx.au/premortem)：Jason Collins・英語・確認日 2026-11-05

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いを鍵に移す判断](../enforce/when-to-lock.md)

**関連**

- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [レビューの観点を育てる](../team/grow-review-checklists.md)
- [失敗の教訓は捨てずに書き残す](../context/keep-failure-lessons.md)
- [セッション記録から失った作業を取り戻す](../cli/recover-lost-work.md)
- [決定を文書に残す（ADR と週次アップデート）](../team/record-decisions.md)
- [消してはいけないものを消された](../symptoms/deleted-something-important.md)
- [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- [お願いと鍵の対応表](../enforce/request-lock-table.md)
- [やめどきを先に決める（撤退基準を着手前に書き、実装者以外が判定する）](decide-when-to-quit.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
