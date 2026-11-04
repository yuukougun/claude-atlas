---
id: progress-files
title: 進捗ファイルで、途中から再開できるようにする
nav_title: 進捗ファイル
aliases: [進捗ファイル（PLAN・TODO・KNOWLEDGE）, TODO.md, 作業ログ, 進捗の外部記憶]
type: recipe
field: context
chapter: 書き出す
order: 80
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている, 見えていない]
pitfalls: []
scenes: [開発, 文章, コンテスト]
summary: 計画・やること・決めたこと・分かったことをファイルに分けて持たせ、どのセッションからでも続きを始められるようにする。変えてよい欄を限ると、状態を壊されにくい。
signs:
  - {type: goal, text: 何日もかかる作業の状態を、会話の外に持ちたい}
  - {type: goal, text: 長い作業を明日も続けたい}
  - {type: symptom, text: 新しいセッションのたびに、前回どこまで進んだかを説明し直している}
prerequisites: [handoff-documents]
related: [keep-failure-lessons, progress-logs-for-long-jobs, long-running-agent-context, experiment-log, record-decisions, spec-first, resume-and-branch, promises-after-compaction, repeating-the-same-explanation]
tracks: []
outdated_advice: []
sources: [qiita-minorun365-114f53, anthropic-eng-effective-harnesses-long-running, anthropic-eng-effective-context-engineering-ai, cc-docs-memory, cc-docs-best-practices]
volatility: 低
sections:
  - {title: 先に整える守り, anchor: guards}
  - {title: ファイルの分け方, anchor: files}
  - {title: 開始と更新の回し方, anchor: cycle}
  - {title: 決めたことと、聞くべきことを分ける, anchor: decided-vs-open}
  - {title: 状態を壊されにくくする, anchor: protect-state}
  - {title: 再開できるかの確かめ方, anchor: check}
  - {title: うまくいかないとき, anchor: troubleshoot}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：計画・やること・決めたこと・分かったことをファイルに分けて持たせ、新しいセッションが読んで続きを始められる。
    - **いつ引くか**：何日もかかる作業の状態を会話の外に持ちたいとき。長い作業を明日も続けたいとき。新しいセッションのたびに、前回どこまで進んだかを説明し直しているとき。
    - **前提**：<!-- link:begin handoff-documents -->[handoff 文書と document-and-clear](handoff-documents.md)<!-- link:end -->

<!-- textlint-disable -->
別名：進捗ファイル（PLAN・TODO・KNOWLEDGE）・TODO.md・作業ログ・進捗の外部記憶
<!-- textlint-enable -->

進捗ファイルは、作業の状態を会話の外のファイルに分けて置き、新しいセッションがそれを読んで続きを始める方法である。一度きりの持ち越しは handoff 文書の役目で、こちらは何日も更新し続ける状態を扱う。手順は 4 段である。ファイルを分けて置く、読ませて始める、区切りで更新させる、新しい会話で再開できるかを確かめる。

## 先に整える守り {#guards}

進捗ファイルは、書かれた内容が正しく、次のセッションが読み直して初めて効く。ファイルを作る前に、3 つを整える。

- **完了と証拠**：やることを「済み」と書かせるなら、完了の条件と、証拠の形を先に決める。決め方は <!-- link:begin handoff-documents#guard -->[handoff 文書と document-and-clear › 先に決めておく完了と証拠](handoff-documents.md#guard)<!-- link:end --> にある。根拠のない「済み」は、次のセッションがそのまま前提にする。
- **読み直される入口**：「毎回このファイルを読んで」と会話で頼んだだけでは、圧縮や `/clear` の後に消えうる。入口の指示は、読み直される `CLAUDE.md` に置く。置き場所の選び方は <!-- link:begin promises-after-compaction#where-to-put -->[圧縮で消えない場所に約束を置く › 約束の種類ごとの置き場所](promises-after-compaction.md#where-to-put)<!-- link:end --> にある。
- **例外を許さない約束**：進捗ファイルに書いた決めごとはお願いであり、守られる保証がない。書き換えを許さないものは、上で指した置き場所の選び方に従って、deny ルールやフックに移す。

## ファイルの分け方 {#files}

進捗ファイルは、更新の頻度と、書き換えてよい人が違うものを別のファイルに分ける。複数の実務家が、`PLAN.md`・`SPEC.md`・`TODO.md`・`KNOWLEDGE.md` のように役割で分けた運用を書いている（根拠：中）。この辞典は、仕様を別の持ち主に任せて、次の 4 つに絞った形を勧める。

| ファイル | 持たせるもの | 書き換える人 |
| --- | --- | --- |
| `PLAN.md` | 目的、完了の条件、範囲外、変えてはならないもの | 人。Claude は変更を提案する |
| `TODO.md` | 次の一手を 1 つ、残りのやること、済みと根拠 | Claude が毎回更新する |
| `DECISIONS.md` | 決めたことと、聞くべきこと（未決） | 人が決め、Claude が記録する |
| `KNOWLEDGE.md` | 分かったことと、試して駄目だったこと | Claude が追記する |

仕様が大きいときは、`SPEC.md` を別に置いてよい。仕様に書く中身は <!-- link:begin spec-first#what-goes-in-the-spec -->[仕様を先に固める（spec・インタビュー・モック先行） › 仕様に書くこと](../recipes/spec-first.md#what-goes-in-the-spec)<!-- link:end --> にある。1 日で終わる作業は、4 つ揃えなくてよい。handoff 文書 1 枚で足りる。

最初から全部を埋めない。`PLAN.md` に目的と完了の条件を書き、`TODO.md` に最初の一手を書けば始められる。残りのファイルは、決めたことや分かったことが出てから作る。この運用で再開の成功率や品質が上がったかを測った記事は、見つからなかった。効果は自分の作業で確かめる。

雛形は次のとおりである。

<!-- gen:begin snippet progress-files/progress-layout -->
<!-- textlint-disable -->

??? example "雛形：進捗ファイルの雛形（計画・やること・決めたこと・分かったこと）"

    ```markdown
    === progress/PLAN.md（計画。変えるのは人。Claude は変更を提案するだけ） ===
    目的：
    完了の条件：<確かめるコマンドと、返ってくるべき結果>
    範囲外：
    変えてはならないもの：

    === progress/TODO.md（やること。毎回変わる） ===
    次の一手（1 つだけ）：
    - [ ] <最初にやること>

    残り：
    - [ ] <やること>：完了の確かめ方 <コマンド>

    済み：
    - [x] <やったこと>：根拠 <実行したコマンドと出力の要点>

    === progress/DECISIONS.md（決めたことと、聞くべきこと） ===
    決めたこと：
    - <内容>｜決めた人：<人か Claude の提案を人が承認>｜日付：｜理由：

    聞くべきこと（未決）：
    - <問い>｜聞く相手：｜暫定の仮定：｜答えが出るまで進めてよい範囲：

    === progress/KNOWLEDGE.md（分かったこと。追記だけ） ===
    - <日付>｜分かったこと：｜根拠：
    - <日付>｜試して駄目だったこと：｜理由：｜次に避けること：
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet progress-files/progress-layout -->

## 開始と更新の回し方 {#cycle}

進捗ファイルは、読ませる側と更新させる側の両方を決めておくと回る。各段に、終わりの確かめを付ける。

1. **入口を置く**：`CLAUDE.md` に、読む順番と、各ファイルの扱いを書く。確かめ：新しいセッションで何も頼まずに始めても、最初に読むファイルが決まっている。

    <!-- gen:begin snippet progress-files/claude-md-resume -->
    <!-- textlint-disable -->

    ??? example "雛形：CLAUDE.md の再開の入口と進捗ファイルの扱い"

        ```markdown
        ## 作業を再開するとき

        作業に着手する前に、次の順で読む。

        1. `progress/TODO.md`：次の一手と、残りのやること
        2. `progress/DECISIONS.md`：決めたことと、聞くべきこと（未決）
        3. `progress/KNOWLEDGE.md`：分かったことと、試して駄目だったこと
        4. `progress/PLAN.md`：目的と完了の条件（必要なときだけ）

        読み終えたら、次の一手と未決を自分の言葉で言い直し、確認を待つ。

        ## 進捗ファイルの扱い

        - `PLAN.md` と `DECISIONS.md` の「決めたこと」は書き換えない。変えたいときは、理由を添えて提案する。
        - `TODO.md` は、済みにした項目に根拠（実行したコマンドと出力の要点）を付ける。
        - `KNOWLEDGE.md` は追記だけにする。
        - 人が決めていないことは「聞くべきこと」に書き、「決めたこと」に移さない。
        ```

        動作を確かめていない雛形。

    <!-- textlint-enable -->
    <!-- gen:end snippet progress-files/claude-md-resume -->

2. **読ませて始める**：着手の前に、次の一手と未決を言い直させる。確かめ：言い直しが `TODO.md` の先頭と `DECISIONS.md` に一致する。ずれたら、作業を始める前に直す。言い直させる理由と手順は <!-- link:begin handoff-documents#resume -->[handoff 文書と document-and-clear › 新しい会話での再開の仕方](handoff-documents.md#resume)<!-- link:end --> と同じである。同じ会話に戻りたいだけなら、<!-- link:begin resume-and-branch#resume -->[セッションに名前を付けて再開・分岐する › 再開する](../cli/resume-and-branch.md#resume)<!-- link:end --> で足りる。
3. **区切りで更新させる**：作業のひと区切りごとに、次の依頼で反映させる。確かめ：`git diff` で、変わったのが `TODO.md` の項目と `KNOWLEDGE.md` の追記だけである。

    <!-- gen:begin snippet progress-files/update-progress -->
    <!-- textlint-disable -->

    ??? example "雛形：区切りで進捗ファイルを更新させる依頼"

        ```markdown
        ここまでの作業を、進捗ファイルに反映して。

        - `progress/TODO.md`：終わった項目を済みにして、根拠（実行したコマンドと出力の要点）を付ける。次の一手を 1 つだけ書く。
        - `progress/KNOWLEDGE.md`：新しく分かったことと、試して駄目だったこと（理由と、次に避けること）を追記する。既存の行は変えない。
        - `progress/DECISIONS.md`：私が決めたと言ったことだけを「決めたこと」に書く。私に確認が要ることは「聞くべきこと」に書き、暫定の仮定と、答えが出るまで進めてよい範囲を添える。
        - `progress/PLAN.md` は変えない。変えたい点があれば、書き換えずにここで提案する。

        反映したら、変えた項目を一覧で返して。実装の続きには進まない。
        ```

        動作を確かめていない雛形。

    <!-- textlint-enable -->
    <!-- gen:end snippet progress-files/update-progress -->

4. **終えるときに次の一手を残す**：その日の終わりも、手順 3 の更新の依頼と同じものを使う。確かめ：次の一手が 1 つだけ残り、明日の自分が読んで着手できる。

## 決めたことと、聞くべきことを分ける {#decided-vs-open}

`DECISIONS.md` には、決まったことと、人に聞かないと決まらないことを別の欄で書く。混ぜると、Claude の暫定の読みが「決めたこと」に紛れる。次のセッションは、それを前提として扱う。コンテストの課題の曖昧な点を、決定事項と運営に質問すべき事項に分けて記録する実践がある（根拠：弱）。

- **決めたこと**：内容、決めた人、日付、理由。人が承認したものだけを書く。
- **聞くべきこと**：問い、聞く相手、暫定の仮定、答えが出るまで進めてよい範囲。Claude が自分で「決めたこと」へ移さない。
- **棄却したこと**：選ばなかった案と理由は、`DECISIONS.md` ではなく `KNOWLEDGE.md` の「試して駄目だったこと」に書く。同じ案の再提案を防げる。何を残すかの基準は <!-- link:begin keep-failure-lessons#what-to-keep -->[失敗の教訓は捨てずに書き残す › 何を残し、何を捨てるか](keep-failure-lessons.md#what-to-keep)<!-- link:end --> にある。

聞くべきことは、答えが出たら「決めたこと」に移し、元の問いは消さずに印を付ける。移す作業は人が決めてから Claude に頼む。

!!! example "判断例：曖昧な規則の読みを、どちらに書くか"
    - **状況**：課題の規則に、提出形式を 2 通りに読める一文がある。主催者への質問はまだ出せていない。
    - **迷う候補**：Claude が妥当と考えた読みで進め、「決めたこと」に書く。または、読みを「聞くべきこと」に書き、質問の文面を作って、2 通りどちらにも耐える範囲で進める。
    - **選んだもの**：「聞くべきこと」に書き、暫定の仮定と進めてよい範囲を添える。
    - **理由**：暫定の読みを「決めたこと」に書くと、翌日のセッションはそれを確定として扱い、どこで仮定したかが残らない。未決の欄なら、回答が来た時点で影響する箇所を探せる。

## 状態を壊されにくくする {#protect-state}

進捗ファイルの危険は、Claude が良かれと思って状態を書き換えることである。書き換えてよい欄を限ると、壊されにくくなる。強い順に 3 段ある。

1. **欄を限る**：Anthropic の長時間エージェントの運用例では、機能の一覧を JSON で持ち、コーディングを行うエージェントには `passes` の欄の値だけを変えさせている。理由は、JSON のほうが Markdown よりモデルに不適切に書き換えられにくい、という経験である。この例は [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)（2025-11-26 公開）の時点のもので、モデルの世代で変わりうる（根拠：中・版依存）。同じ形は次のように書ける。

    <!-- gen:begin snippet progress-files/todo-state -->
    <!-- textlint-disable -->

    ??? example "雛形：状態を JSON で持ち、変えてよい欄を passes に限る例"

        ```json
        {
          "items": [
            {
              "id": "T1",
              "title": "入力の検証を足す",
              "done_when": "`npm test -- validate` が成功する",
              "passes": false
            },
            {
              "id": "T2",
              "title": "エラー表示を日本語にする",
              "done_when": "`npm test -- messages` が成功する",
              "passes": false
            }
          ]
        }
        ```

        動作を確かめていない雛形。

    <!-- textlint-enable -->
    <!-- gen:end snippet progress-files/todo-state -->

    「変えてよいのは `passes` だけ」という指示は、`CLAUDE.md` か依頼に書く。この指示はお願いなので、差分で守られたかを見る。
2. **書き方を限る**：`KNOWLEDGE.md` は追記だけ、`TODO.md` は項目の状態と根拠だけ、と決める。編集でなく追記にすると、過去の記録を書き換えられる範囲が減る。git に履歴を残せば、壊れても戻せる。
3. **仕組みで止める**：決めたことの書き換えを例外なく止めたいときは、`CLAUDE.md` の文では足りない。deny ルールやフックに移す。判断の基準は <!-- link:begin promises-after-compaction#effects -->[圧縮で消えない場所に約束を置く › 何に効くか（縛る・見せる）](promises-after-compaction.md#effects)<!-- link:end --> にある。

欄を限ると、人が書いた欄を Claude が整えようとして、人の意図を消す事故も防げる。

## 再開できるかの確かめ方 {#check}

進捗ファイルが書けているかは、前回の会話を見せずに再開させて確かめる。新しいセッションで再開の入口だけを渡し、次の 4 点を見る。

- **次の一手**：言い直した内容が、`TODO.md` の先頭と一致する。
- **未決の扱い**：「聞くべきこと」を、決まったこととして進めていない。
- **失敗の繰り返し**：`KNOWLEDGE.md` にある駄目だった案を、再提案していない。
- **最初の編集**：最初に触るのが、`TODO.md` の次の一手に書いたファイルである。

1 点でも外れたら、原因のファイルを探して直す。次の一手が違うなら、`TODO.md` が古い。未決を進めていたなら、`DECISIONS.md` の欄の区切りが曖昧だった。

## うまくいかないとき {#troubleshoot}

- **更新が実作業とずれる**：Claude が更新を忘れたか、根拠なしに「済み」にしている。区切りの依頼を決まった形にして、`git diff` で見る。
- **ファイルが膨らんで読むのが重い**：済みの項目と古い記録を別のファイルへ移し、入口が読むのは現在の分だけにする。移したものは削らず、日付を付けて残す。
- **毎回同じ説明をしている**：進捗の問題ではなく、背景や手順の置き場所の問題かもしれない。<!-- link:begin repeating-the-same-explanation#diagnosis -->[毎回同じ説明をしている › 原因を安く確かめる順](../symptoms/repeating-the-same-explanation.md#diagnosis)<!-- link:end --> で原因を切り分ける。
- **同じ失敗の案が出る**：書き残しが足りないか、多すぎて埋もれている。<!-- link:begin keep-failure-lessons#too-much -->[失敗の教訓は捨てずに書き残す › 書き残しすぎの副作用](keep-failure-lessons.md#too-much)<!-- link:end --> を見る。
- **圧縮の後に決めごとを忘れる**：入口が読み直される場所にない。<!-- link:begin promises-after-compaction#what-comes-back -->[圧縮で消えない場所に約束を置く › 読み直される場所と、要約に溶ける約束](promises-after-compaction.md#what-comes-back)<!-- link:end --> を見る。
- **無人の長時間ジョブの状況を追いたい**：人と Claude が対話で再開する状態ではなく、観察するための記録が要る。<!-- link:begin progress-logs-for-long-jobs -->長時間ジョブの進捗ログを設計する（準備中）<!-- link:end --> を見る。
- **実験の仮説と結果を残したい**：進捗ファイルとは別の台帳が向く。違いは <!-- link:begin experiment-log#not-progress-file -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版） › 進捗ファイルなどとの違い](../eval/experiment-log.md#not-progress-file)<!-- link:end --> にある。
- **API で長く動くエージェントを作っている**：状態をファイルに持たせる考え方は <!-- link:begin long-running-agent-context#external-state -->長時間エージェントのコンテキスト管理 › 状態をファイルに持たせる（準備中）<!-- link:end --> にある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [handoff 文書と document-and-clear](handoff-documents.md)

**次に読む**

- 長時間ジョブの進捗ログを設計する（準備中）

**関連**

- [失敗の教訓は捨てずに書き残す](keep-failure-lessons.md)
- 長時間エージェントのコンテキスト管理（準備中）
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- 決定を文書に残す（ADR と週次アップデート）（準備中）
- [仕様を先に固める（spec・インタビュー・モック先行）](../recipes/spec-first.md)
- [セッションに名前を付けて再開・分岐する](../cli/resume-and-branch.md)
- [圧縮で消えない場所に約束を置く](promises-after-compaction.md)
- [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Claude Codeですべての日常業務を爆速化しよう！](https://qiita.com/minorun365/items/114f53def8cb0db60f47)：Qiita（minorun365）・確認日 2026-11-04
- [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)：Anthropic・英語・確認日 2026-11-04
- [Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
