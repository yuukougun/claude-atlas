---
id: record-decisions
title: 決定を文書に残す（ADR と週次アップデート）
nav_title: 決定を文書に残す
aliases: [ADR, Architecture Decision Record, 週次アップデート]
type: recipe
field: team
chapter: レビューと判断
order: 100
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [見せる, 握る]
prevents: [見えていない]
pitfalls: []
scenes: [チーム, 開発]
summary: 決めたことと理由を ADR に残し、週ごとに決めたこと・AI に任せたこと・見てほしい点を書面で共有できる。新しい人が文書だけで作業を始められるかで、書けているかを確かめる。
signs:
  - {type: symptom, text: なぜそう決めたかが、後から分からない}
  - {type: goal, text: AI に任せたことと決めたことを、チームに書面で伝えたい}
prerequisites: [handoff-documents]
related: [keep-failure-lessons, postmortems, experiment-log, disclosure-and-provenance, what-to-put-in-claude-md, agents-md, separate-roles, rolling-out-to-teams, compare-hypotheses-in-parallel]
sources: []
sections:
  - {anchor: guards, title: 先に整える守り}
  - {anchor: steps, title: 手順}
  - {anchor: template, title: 雛形：ADR・週次アップデート・CLAUDE.md の指す先}
  - {anchor: check, title: 確かめ方}
  - {anchor: when-it-fails, title: 失敗したとき}
volatility: 低
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：決めたことと理由を ADR に残し、週ごとに決めたこと・AI に任せたこと・見てほしい点を書面で共有できる。
    - **いつ引くか**：なぜそう決めたかが後から分からないとき。AI に任せたことと決めたことを、チームに書面で伝えたいとき。
    - **前提**：<!-- link:begin handoff-documents -->[handoff 文書と document-and-clear](../context/handoff-documents.md)<!-- link:end -->

<!-- textlint-disable -->
別名：ADR・Architecture Decision Record・週次アップデート
<!-- textlint-enable -->

決定を文書に残す方法は、決定ごとに 1 ファイルの ADR（Architecture Decision Record、決定の記録）と、週ごとの書面のアップデートの 2 つを回す進め方である。<!-- link:begin handoff-documents -->[handoff 文書と document-and-clear](../context/handoff-documents.md)<!-- link:end -->の考え方をチームに広げたもので、個人の作業の引き継ぎを、人と AI が混ざった複数人の作業へ移す。

## 先に整える守り {#guards}

AI に任せる幅が広がるほど、決定の経緯は会話の中に埋もれる。記録を始める前に、次の 4 つを決めておく。

- **置き場所を 1 つにする**：決定は `docs/decisions/` に 1 決定 1 ファイルで置く。週次のアップデートは `docs/updates/` に置く。チャットや会話の履歴だけの決定は、新しいセッションからも新しい担当者からも見えない。
- **決める人を人にする**：ADR の「決めた人」は人の名前か役割にする。Claude が案を出しても、採用を決めたのは誰かを書く。AI が同意したことは決定の根拠に数えない（<!-- link:begin separate-roles#against-sycophancy -->[役割を分ける（書く人・承認する人・疑う人） › 迎合と過信に備える（AI の同意を根拠に数えない）](separate-roles.md#against-sycophancy)<!-- link:end -->）。
- **任せた部分と確かめ方を対で書く**：「AI に任せたこと」を書くときは、確かめ方（テスト・差分のレビュー・実行結果）を同じ行に書く。確かめていないなら、そう書く。任せる幅を広げた週ほど、この対が欠けやすい。
- **CLAUDE.md には指す先だけを書く**：決定の本文は ADR に置き、CLAUDE.md には「ADR を読む」「食い違う変更は先に伝える」という指す先と基準だけを残す。何を CLAUDE.md に入れ、何を外すかは<!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](../extend/what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end -->で決める。例外を許さない禁止は、ADR ではなく deny ルールかフックなどの強制する仕組みに移し、ADR には理由だけを書く。

## 手順 {#steps}

次の順に進める。各段に、終わったと言える確かめを付けた。

1. **ADR の置き場所と雛形を用意する。**
    - `docs/decisions/` を作り、雛形を `0000-template.md` として置く（下の「雛形」の節）。
    - 確かめ：リポジトリを開いた人が、`docs/decisions/` を見つけて雛形を写せる。
2. **今ある重要な決定を、さかのぼって 3〜5 件だけ書く。**
    - 全部は書かない。「なぜこうなっているのか」を新しい人によく聞かれる決定から選ぶ。
    - 確かめ：その決定を知らない人が ADR を読んで、同じ質問を口頭でしなくて済む。
3. **決めるたびに、決めた直後に ADR を書く。**
    - Claude に下書きを書かせてよい。会話で出た案・却下した案・理由を渡し、雛形の欄を埋めさせる。ただし、「決めたこと」と「理由」は決めた人が読んで直す。AI の下書きをそのまま採用の記録にしない。
    - 確かめ：状態が「採用」になっている ADR には、決めた人の名前か役割が入っている。
4. **決定を変えるときは、古い ADR を消さずに置き換える。**
    - 古い ADR の状態を「置き換え済み」にして置き換え先を書き、新しい ADR に置き換える理由を書く。
    - 確かめ：置き換え済みの ADR から、現行の ADR にたどれる。
5. **週に 1 回、週次アップデートを書く。**
    - 「今週決めたこと」「AI に任せたこと」「まだ決めていないこと」「レビューしてほしい点」を書く。雛形は下の「雛形」の節にある。
    - レビューしてほしい点は、「何に照らして見てほしいか」と「何は除外してよいか」の 2 つを組にして書く。観点を絞らない依頼は、読む人が全体を見直す負担を負う。
    - 確かめ：読む人が、アップデートだけを読んでレビューの的を絞れる。
6. **CLAUDE.md に、ADR の置き場所を指す数行を足す。**
    - 雛形は下の「雛形」の節にある。作業の前に関係する ADR を読ませ、食い違う変更を求められたら先に伝えさせる。
    - 確かめ：新しいセッションで、ADR と食い違う変更を頼み、Claude が食い違いを挙げるかを見る。CLAUDE.md の指示はお願いなので、必ず挙げるとは限らない。挙げない決定が守る対象なら、強制する仕組みに移す。

## 雛形：ADR・週次アップデート・CLAUDE.md の指す先 {#template}

3 つの雛形を載せる。動作は確かめていない。自分のチームの欄に合わせて直して使う。

ADR の雛形である。1 決定 1 ファイルで、状態・決めた人・AI に任せた部分を最初に置く。

<!-- gen:begin snippet record-decisions/adr-template -->
<!-- textlint-disable -->

??? example "雛形：ADR の雛形（docs/decisions/ に置く 1 決定 1 ファイル）"

    ```markdown
    # ADR-0001: <決めたことを 1 文で>

    - 状態：提案 / 採用 / 置き換え済み（ADR-NNNN に）
    - 日付：YYYY-MM-DD
    - 決めた人：<人の名前か役割>
    - AI に任せた部分：<AI が出した案・調査・実装。なければ「なし」>

    ## 背景

    <何に困っていたか。決める前の状況と、制約>

    ## 決めたこと

    <選んだ案を、実行できる形で。範囲の外も 1 行で>

    ## 理由

    <他の案より、これを選んだ根拠。確かめたこと（測った値・読んだ文書）と、確かめていないこと>

    ## 検討して選ばなかった案

    - <案 A>：<選ばなかった理由>
    - <案 B>：<選ばなかった理由>

    ## 見直す条件

    <この決定を見直す合図。例：前提にした制約が変わったとき>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet record-decisions/adr-template -->

週次アップデートの雛形である。「レビューしてほしい点」の欄は、何に照らして見るかと、何を除外するかを組にする。

<!-- gen:begin snippet record-decisions/weekly-update -->
<!-- textlint-disable -->

??? example "雛形：週次アップデートの型（決めたこと・AI に任せたこと・レビューしてほしい点）"

    ```markdown
    # 週次アップデート（YYYY-MM-DD の週）

    ## 今週決めたこと

    - <決定を 1 行で>（ADR-NNNN）

    ## AI に任せたこと

    - <任せた作業>：<任せた範囲>。確かめ方は <テスト・レビュー・差分の確認など>。結果は <確かめた／まだ確かめていない>

    ## まだ決めていないこと

    - <論点>：<決める人>が <日付> までに決める

    ## レビューしてほしい点

    - <ファイルか決定>を、<何に照らして>見てほしい。<何は除外して>よい
      - 例：ADR-0007 を、既存の API の互換を保てているかに照らして見てほしい。性能の議論は除外してよい

    ## 来週に回すこと

    - <項目>
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet record-decisions/weekly-update -->

CLAUDE.md に足す、ADR の置き場所を指す数行である。決定の本文は書かない。

<!-- gen:begin snippet record-decisions/claude-md-pointer -->
<!-- textlint-disable -->

??? example "雛形：CLAUDE.md に置く「決定の記録」の指す先"

    ```markdown
    ## 決定の記録

    - 設計や運用を決めたときは `docs/decisions/` に ADR を 1 ファイル書く。雛形は `docs/decisions/0000-template.md`
    - 作業の前に、触る範囲に関わる ADR を読む。状態が「置き換え済み」のものは、置き換え先を読む
    - ADR にある決定と食い違う変更を求められたら、変更する前に食い違いを伝える。ADR は勝手に書き換えない
    - 週次の状況は `docs/updates/` に置く
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet record-decisions/claude-md-pointer -->

!!! example "判断例：Claude が出した案を ADR にどう書くか"
    - **状況**：キャッシュの方式を Claude と相談し、Claude が 2 案を比較して片方を勧めた。担当者は勧められた案を採ることにした。
    - **迷う候補**：ADR の理由欄に「Claude が推奨したため」と書く。または、比較で見えた条件と、担当者が確かめたことを理由に書く。
    - **選んだもの**：後者。「AI に任せた部分」に Claude が比較を出したことを書き、「理由」には担当者が確かめた条件を書く。
    - **理由**：AI が勧めたことは根拠にならず、数か月後に読んだ人が見直す手がかりにもならない。前者でも経緯としては正確だが、見直すときに何を確かめ直せばよいかが残らない。

## 確かめ方 {#check}

記録が書けているかは、新しい人の立場で確かめる。新メンバー役が、`CLAUDE.md` と ADR だけを読んで、1 つの作業をこなせるかを見る。（根拠：弱。複数の実務家の提案を元にした、この辞典の推奨）

- **人で確かめる**：入って間もない人に、リポジトリの文書だけを渡して、小さな作業を 1 つ頼む。口頭で補足を求められたら、その内容が ADR か CLAUDE.md に足りなかった点である。
- **Claude で確かめる**：履歴のない新しいセッションで、作業を頼む前に「`CLAUDE.md` と `docs/decisions/` の ADR だけを読んで、この作業で守る決定を挙げて」と頼む。挙がらない決定、または理由が違って挙がる決定は、書き方か置き場所が不足している。Claude の答えは確認の補助であり、足りているかの判定は人が行う。
- **見る観点**：決めたことと理由が、別々に読み取れる。選ばなかった案と見直す条件がある。置き換え済みの決定が現行と混ざらない。週次アップデートの「AI に任せたこと」に、確かめ方が対で書かれている。

この確かめは、CLAUDE.md が足りているかを測る基準にもなる。新メンバー役の迷った点が、CLAUDE.md の書き足し候補になる。

## 失敗したとき {#when-it-fails}

| 起きたこと | 原因の見当 | 行き先 |
| --- | --- | --- |
| ADR が増えるだけで、誰も読まない | 作業の入口（CLAUDE.md）から指されていない。または 1 件が長すぎる | 手順 6。CLAUDE.md の書き方は<!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)<!-- link:end --> |
| ADR を読んだ Claude が、古い決定に従う | 置き換え済みの状態が付いていない | 手順 4。状態と置き換え先を足す |
| 失敗や巻き戻しの経緯が残らない | ADR は採用した決定の記録で、捨てた試みを書く場所ではない | <!-- link:begin keep-failure-lessons -->[失敗の教訓は捨てずに書き残す](../context/keep-failure-lessons.md)<!-- link:end -->、失敗の原因を仕組みに戻すなら<!-- link:begin postmortems -->[失敗を仕組みに戻す（ポストモーテム）](../judgment/postmortems.md)<!-- link:end --> |
| 週次アップデートが作業の羅列になる | 「レビューしてほしい点」に観点と除外がない | 手順 5。「何に照らして」「何は除外して」を組にして書く |
| 実験の仮説や判定の記録が散らばる | 決定の記録と実験の台帳を分けていない | <!-- link:begin experiment-log -->[実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)<!-- link:end --> |
| 役割が分かれず、書いた人が承認も兼ねる | 決める人・確かめる人が同じ | <!-- link:begin separate-roles -->[役割を分ける（書く人・承認する人・疑う人）](separate-roles.md)<!-- link:end --> |

AI の利用を開示する場面や、事前に作った資料の出所の記録が必要なときは、決定の記録とは別に<!-- link:begin disclosure-and-provenance#provenance -->[AI 利用の開示と出所の記録 › 出所を記録する](../safety/disclosure-and-provenance.md#provenance)<!-- link:end -->を使う。チーム全体に記録の習慣を広げる段取りは<!-- link:begin rolling-out-to-teams -->チームに広める（/team-onboarding など）<!-- link:end -->、他のエージェントツールと指示を共有するなら<!-- link:begin agents-md -->[AGENTS.md とほかのツールとの共有](../extend/agents-md.md)<!-- link:end -->を見る。仮説ごとに並べて試す作業の記録は、<!-- link:begin compare-hypotheses-in-parallel#template -->[仮説ごとに並べて、同じ物差しで比べる › 雛形：比較の記録と手順](../delegate/compare-hypotheses-in-parallel.md#template)<!-- link:end -->に比較の記録の雛形がある。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [handoff 文書と document-and-clear](../context/handoff-documents.md)

**関連**

- [失敗の教訓は捨てずに書き残す](../context/keep-failure-lessons.md)
- [失敗を仕組みに戻す（ポストモーテム）](../judgment/postmortems.md)
- [実験台帳（仮説を先に書く・提案者・分母・検証器の版）](../eval/experiment-log.md)
- [AI 利用の開示と出所の記録](../safety/disclosure-and-provenance.md)
- [CLAUDE.md に書くこと・書かないこと](../extend/what-to-put-in-claude-md.md)
- [AGENTS.md とほかのツールとの共有](../extend/agents-md.md)
- [役割を分ける（書く人・承認する人・疑う人）](separate-roles.md)
- [仮説ごとに並べて、同じ物差しで比べる](../delegate/compare-hypotheses-in-parallel.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
