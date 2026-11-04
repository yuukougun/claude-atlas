---
id: repeating-the-same-explanation
title: 毎回同じ説明をしている
aliases: [同じ説明の繰り返し, 毎回背景を説明する, 同じ手順書を貼っている]
type: symptom
field: symptoms
chapter: 指示と仕組み
order: 180
level: 整える
priority: 必須
surfaces: [app, claude-code]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
pitfalls: []
scenes: [開発, 文章, チーム]
summary: 毎回同じ背景・手順・注意を説明している状態から、どれを置き場所（指示・プロジェクト・CLAUDE.md・スキル）に移し、どの注意を仕組みで縛るかを決める。
signs:
  - {type: symptom, text: 毎回同じ背景を説明している}
  - {type: symptom, text: 同じ手順書を何度も貼っている}
  - {type: symptom, text: 新しい会話のたびにプロジェクトの説明からやり直している}
  - {type: symptom, text: 同じ注意を何度も繰り返している}
wave: 1
prerequisites: [where-instructions-sit]
related: [using-projects, init-and-first-claude-md, how-skills-load, writing-skills, skills-in-the-app, how-memory-works, path-scoped-rules, share-team-settings, progress-files, instructions-ignored, unexpected-memories, not-what-i-meant, six-causes]
routes:
  - {cause: 見えていない, to: [where-to-put-instructions, when-to-add-what, what-to-put-in-claude-md]}
  - {cause: 縛っていない, to: [when-to-lock#signals]}
tracks: [claude-md, skills, projects, project-instructions, personal-instructions, app-memory]
outdated_advice: [hash-to-memorize, commands-directory, styles-for-tone]
sources: [cc-docs-features-overview, hc-personalization, hc-projects-what]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処, anchor: causes}
  - {title: 判断例, anchor: examples}
  - {title: 予防：移した後に削り、足すのは繰り返しが見えてから, anchor: prevention}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：毎回の説明を背景・手順・注意に分け、置き場所に移すか、仕組みで縛るかを決められる。
    - **いつ引くか**：毎回同じ背景を説明している、同じ手順書を何度も貼っている、新しい会話のたびにプロジェクトの説明からやり直している、同じ注意を何度も繰り返しているとき。
    - **前提**：<!-- link:begin where-instructions-sit -->[システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)<!-- link:end -->

<!-- textlint-disable -->
別名：同じ説明の繰り返し・毎回背景を説明する・同じ手順書を貼っている
<!-- textlint-enable -->

毎回同じ説明をしているのは、説明が Claude の見える場所にない状態である。置いてあるのに同じ注意を繰り返しているなら、守らせる仕組みがない状態である。このページは、繰り返している説明を 1 つずつ分けて、移し先を決めるための振り分けである。

## よくある形 {#forms}

繰り返している説明は、次のどれかの形で現れる。

- 新しい会話を始めるたびに、プロジェクトの目的・構成・用語・読み手を説明し直す。
- 決まった手順書や書式（レビューの観点、記事の体裁、リリースの段取り）を、そのまま貼る。
- 「これはしないで」「必ずこうして」を、毎回の依頼に添える。
- 会話ごとに、文体や出力の形式を指定し直す。

中身は 3 種類に分けられる。変わらない事実の**背景**、決まった段取りの**手順**、してはいけないことや守ってほしい規則の**注意**である。移し先は種類で変わる。

## 原因を安く確かめる順 {#diagnosis}

繰り返している説明を 1 つ選び、上から順に確かめる。上ほど安い。

1. **すでにどこかに書いてあるか（見る：書いた場所と、会話を始めた場所）。** Claude への指示、プロジェクトの指示、CLAUDE.md、スキルに、同じ内容がすでにないかを見る。あるなら、その会話で読まれる位置かを確かめる。プロジェクトの指示はそのプロジェクトの中の会話に使われるので、プロジェクトの外で会話を始めていないかを見る。書いてあり、読まれる位置にあっても破られるなら、このページではなく <!-- link:begin instructions-ignored#diagnosis -->[CLAUDE.md や指示が守られない › 原因を安く確かめる順](instructions-ignored.md#diagnosis)<!-- link:end --> へ進む。別の会話の内容が混ざるなら <!-- link:begin unexpected-memories#diagnosis -->[別の会話やプロジェクトの内容が混ざる › 原因を安く確かめる順](unexpected-memories.md#diagnosis)<!-- link:end --> へ進む。
2. **書いていない背景か（原因：見えていない）。** 変わらない事実を毎回説明しているなら、置き場所に移す。移した後の確かめ方は、背景を貼らずに新しい会話で頼み、Claude がその前提で答えるかを見ることである。前提の抜けた答えなら、まだ Claude に見えていない。移し先は面で変わる。置き場所の比較は <!-- link:begin where-to-put-instructions#comparison -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › 置き場所ごとの効く範囲と読まれる時期](../app/where-to-put-instructions.md#comparison)<!-- link:end --> にある。

    === "アプリ"
        - 全部の会話に効かせたい好みや前提は、Claude への指示に書く。
        - 案件ごとの背景と資料は、プロジェクトの指示とナレッジに置く。切り方は <!-- link:begin using-projects#scope -->プロジェクトの使いどころ › プロジェクトを切る単位（1つに1つの目的）（準備中）<!-- link:end --> にある。
        - アプリのメモリは Claude が覚える仕組みで、範囲と消し方は <!-- link:begin how-memory-works#scope -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › アカウントのメモリとプロジェクトのメモリ](../app/how-memory-works.md#scope)<!-- link:end --> で確かめる。

    === "Claude Code"
        - 毎回読ませたい前提は、CLAUDE.md に書く。CLAUDE.md は強制ではなく文脈として扱われる（<!-- link:begin where-instructions-sit#why -->[システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置 › なぜ強制ではなく文脈になるか](../basics/where-instructions-sit.md#why)<!-- link:end -->）。何を残すかは <!-- link:begin what-to-put-in-claude-md#what-to-write -->[CLAUDE.md に書くこと・書かないこと › 書くこと](../extend/what-to-put-in-claude-md.md#what-to-write)<!-- link:end --> で決める。
        - 特定のフォルダだけの規約は、触れたときだけ読ませる。<!-- link:begin path-scoped-rules -->.claude/rules と paths で必要なときだけ読ませる（準備中）<!-- link:end --> を見る。
        - 叩き台から始めるなら <!-- link:begin init-and-first-claude-md#run-init -->/init と最初の CLAUDE.md › /init で叩き台を作る（準備中）<!-- link:end --> を見る。

3. **決まった手順か（原因：見えていない）。** 貼っている文書が毎回ほぼ同じで、使うのが特定の作業のときだけなら、スキルにする。スキルは説明文だけが常駐し、本文は必要なときだけ読まれるので、長い手順を常駐の指示へ積まずに済む。作業の種類を問わず常に要る前提なら、手順ではなく背景として、上の「書いていない背景か」の項へ戻る。見分け方と作り方は <!-- link:begin writing-skills#when-to-use -->[スキルの作り方 › どんなときにスキルにするか](../extend/writing-skills.md#when-to-use)<!-- link:end --> と <!-- link:begin skills-in-the-app -->アプリでスキルを使う（準備中）<!-- link:end --> にある。確かめ方は、スキルを呼んだときの動きが、貼っていた手順書のときと同じかを見ることである。
4. **同じ注意の繰り返しか（原因：縛っていない）。** 次のどれかなら、置き場所ではなく鍵の問題である。同じ禁止を何度も添えている。強調しても破られた。会話で言った禁止が途中で効かなくなった。例外を許さない禁止は、権限ルールやフックに移す。判断を含む規則は鍵にしない。合図と移し先は <!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end --> と <!-- link:begin when-to-lock#where-to-move -->[お願いを鍵に移す判断 › 移し先の選び方](../enforce/when-to-lock.md#where-to-move)<!-- link:end --> にある。確かめ方は、言い方を変えれば守られるのか、守られても会話が進むと消えるのかを見ることである。後者は <!-- link:begin when-to-lock#spoken-rules-fade -->[お願いを鍵に移す判断 › 会話で言った禁止は圧縮で消える](../enforce/when-to-lock.md#spoken-rules-fade)<!-- link:end --> にある。

毎回変わる部分は、移さない。その回の目的・対象・出来上がりの条件は頼む内容であり、置き場所に固定すると別の依頼で邪魔になる。頼んだものと違うものが出るなら <!-- link:begin not-what-i-meant#diagnosis -->[意図と違うものが出てくる › 原因を安く確かめる順](not-what-i-meant.md#diagnosis)<!-- link:end --> へ進む。ここまでで決まらないときは <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> で 6 つの原因の全体から確かめ直す。

## 原因ごとの対処 {#causes}

原因ごとの対処の本体は、振り分け先のページにある。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)<br>拡張を足すタイミング（準備中）<br>[CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md) |
| 縛っていない | [お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：案件ごとの背景を毎回貼っている（アプリ）"
    - **状況**：複数の案件で、読み手・用語・書式の説明を、新しい会話のたびに貼っている。案件ごとに内容が違う。
    - **迷う候補**：全部の会話に効く Claude への指示に書く。案件ごとにプロジェクトを作り、その指示と資料に置く。
    - **選んだもの**：案件ごとのプロジェクトにする。
    - **理由**：案件の内容は案件ごとで違い、全部の会話に効く指示へ入れると別の案件に混ざる。プロジェクトなら 1 つの目的に 1 つの置き場所が対応する（<!-- link:begin using-projects#knowledge -->プロジェクトの使いどころ › ナレッジを置くと何が変わるか（準備中）<!-- link:end -->）。全案件に共通する好みだけを、Claude への指示に残す。

!!! example "判断例：リリース手順と本番に触るなという注意を毎回添えている（Claude Code）"
    - **状況**：リリースのたびに手順書を貼り、本番の環境には触らないでほしいと添えている。
    - **迷う候補**：両方を CLAUDE.md に書く。手順はスキルにし、禁止は仕組みで止める。
    - **選んだもの**：手順はスキルに、禁止は権限ルールかフックに移す。CLAUDE.md には禁止の理由と、迷ったときに相談する基準だけを書く。
    - **理由**：手順は特定の作業でだけ要るので、必要なときにだけ読まれるスキルが合う。禁止は例外を許さないので、CLAUDE.md への頼みでは足りない。CLAUDE.md への頼みは文脈として扱われ、破られることがある（<!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](../enforce/when-to-lock.md#what-not-to-lock)<!-- link:end -->）。

## 予防：移した後に削り、足すのは繰り返しが見えてから {#prevention}

- 最初から作り込まない。同じ説明や注意を繰り返したと気づいた時点で、1 つずつ移す。回数を目安にした足し方は <!-- link:begin when-to-add-what -->拡張を足すタイミング（準備中）<!-- link:end --> にある。
- 移したら、貼っていた元の文面は使わない。二重に残すと、食い違ったときにどちらが効くのかが分からなくなる。
- CLAUDE.md に移したら、叩き台のまま使わず削る。削り方は <!-- link:begin init-and-first-claude-md#prune -->/init と最初の CLAUDE.md › 叩き台を削ってから使う（削り方は claude-md-length）（準備中）<!-- link:end --> にある。
- チームで同じ前提を使うなら、リポジトリに入れて共有する。個人の好みと秘密は共有のファイルに入れない（<!-- link:begin share-team-settings#shared-vs-personal -->チームで設定を共有する › 共有するものと個人に残すもの（準備中）<!-- link:end -->）。
- 前回の作業の続きを毎回説明しているなら、背景ではなく途中の状態の問題である。<!-- link:begin progress-files#files -->進捗ファイルで、途中から再開できるようにする › ファイルの分け方（準備中）<!-- link:end --> のように、ファイルに持たせる。
- 繰り返しを洗い出すところから Claude に手伝わせるなら、次の依頼を使う。

<!-- gen:begin snippet repeating-the-same-explanation/inventory-request -->
<!-- textlint-disable -->

??? example "雛形：繰り返している説明を、置き場所へ振り分けさせる依頼"

    ```markdown
    私が何度も説明し直している内容を、置き場所に振り分けたい。下に、最近の会話で貼った説明や添えた注意をそのまま貼る。

    <ここに、繰り返し貼っている背景・手順書・注意を貼る>

    次の順で答えてほしい。

    1. 貼った内容を「背景（変わらない事実）」「手順（決まった段取りや書式）」「注意（してはいけないこと、守ってほしい規則）」に分ける。
    2. 毎回変わる部分（その回の目的や対象）は、移さずに頼みの側へ残す。どれがそうかも書く。
    3. 背景と手順と注意のそれぞれについて、移し先の案を 1 つ出す。注意のうち、例外を許さない禁止は、お願いではなく仕組みで止める案にする。
    4. ファイルはまだ作らず、案だけを出す。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet repeating-the-same-explanation/inventory-request -->

## 古くなった助言 {#outdated}

置き場所に移す手順の記事には、今は変わっているものがある。

- <!-- link:begin outdated-advice-ledger#hash-to-memorize -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#hash-to-memorize)<!-- link:end -->：今は、Claude に CLAUDE.md の編集を頼むか、`/memory` でファイルを開いて自分で書く。
- <!-- link:begin outdated-advice-ledger#commands-directory -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#commands-directory)<!-- link:end -->：新しく作る繰り返しの手順は、スキルにする。既存のコマンドのファイルは今も動く。
- <!-- link:begin outdated-advice-ledger#styles-for-tone -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#styles-for-tone)<!-- link:end -->：いつも同じ調子にするなら Claude への指示に、場面ごとに切り替えるならスキルにする。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)：Anthropic・英語・確認日 2026-11-04
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [システムプロンプト・ユーザーメッセージ・CLAUDE.md の位置](../basics/where-instructions-sit.md)

**次に読む**

- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](../app/where-to-put-instructions.md)
- 拡張を足すタイミング（準備中）
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)

**関連**

- プロジェクトの使いどころ（準備中）
- /init と最初の CLAUDE.md（準備中）
- スキルの考え方（手順を必要なときだけ読む）（準備中）
- [スキルの作り方](../extend/writing-skills.md)
- アプリでスキルを使う（準備中）
- [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- .claude/rules と paths で必要なときだけ読ませる（準備中）
- チームで設定を共有する（準備中）
- 進捗ファイルで、途中から再開できるようにする（準備中）
- [CLAUDE.md や指示が守られない](instructions-ignored.md)
- [別の会話やプロジェクトの内容が混ざる](unexpected-memories.md)
- [意図と違うものが出てくる](not-what-i-meant.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
