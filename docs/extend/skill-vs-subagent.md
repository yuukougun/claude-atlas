---
id: skill-vs-subagent
title: スキルとサブエージェントの違い
aliases: [skill と subagent の使い分け, 'context: fork']
type: comparison
field: extend
chapter: サブエージェント
order: 170
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
scenes: [開発]
summary: 手順を今の会話で読ませるか、別の文脈の担当に任せるかを選べる。スキルは知識と手順を足し、サブエージェントは作業を本筋から隔てて要約だけを返す。
signs:
  - {type: goal, text: skill と subagent のどちらにすべきか}
  - {type: goal, text: 手順を自分の会話で使うか、別の担当に任せるかを決めたい}
prerequisites: [how-skills-load, subagent-isolation]
related: [writing-skills, writing-subagents, extensions-at-a-glance, research-in-subagents, choosing-parallel-modes, what-subagents-dont-inherit, independent-review]
tracks: [skills, subagents]
sources: [cc-docs-skills, cc-docs-sub-agents, cc-docs-features-overview, cc-docs-best-practices]
sections:
  - {title: 比較の表, anchor: table}
  - {title: 選び方, anchor: how-to-choose}
  - {title: 組み合わせ方と確かめ方, anchor: combine}
volatility: 中
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：手順を今の会話で使うならスキル、出力の多い作業を本筋から隔てて要約だけ受け取るならサブエージェントに置き分けられる。
    - **いつ引くか**：スキルとサブエージェントのどちらにすべきか迷ったとき。手順を自分の会話で使うか、別の担当に任せるかを決めたいとき。
    - **前提**：<!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)<!-- link:end -->、<!-- link:begin subagent-isolation -->[サブエージェントは別室の部下](../basics/subagent-isolation.md)<!-- link:end -->

<!-- textlint-disable -->
別名：skill と subagent の使い分け・context: fork
<!-- textlint-enable -->

スキルとサブエージェントの違いは、手順を今の会話の中で読ませるか、別の文脈の担当に任せるかである。スキルは知識と手順を会話に足す。サブエージェントは作業を本筋から隔てて、要約だけを返す。どちらも「繰り返す手順を仕組みにする」ために使うので混同されやすいが、動く場所と、本筋に残るものが違う。

## 比較の表 {#table}

2 つの機能を、データから作った属性で並べる。

<!-- gen:begin compare 読み込みの時期 コンテキストのコスト 入った版 -->
<!-- textlint-disable -->

| 機能 | 読み込みの時期 | コンテキストのコスト | 入った版 |
| --- | --- | --- | --- |
| [スキル（skills）](writing-skills.md) | セッション開始と使うとき | 使うまで小さい | 2.0.20（2025-10-16） |
| [サブエージェント（subagents）](writing-subagents.md) | 起動したとき | 分離 | 1.0.60（2025-07-24） |

<!-- textlint-enable -->
<!-- gen:end compare 読み込みの時期 コンテキストのコスト 入った版 -->

属性の表に出ない違いは次のとおりである。

- **動く場所**：スキルは今の会話の中で動く。サブエージェントは自分の文脈を新しく作って動く。
- **履歴が見えるか**：スキルは会話の履歴をそのまま見られる。サブエージェントには会話の履歴が渡らない。渡らないものの全体は<!-- link:begin what-subagents-dont-inherit -->[サブエージェントに引き継がれないもの](what-subagents-dont-inherit.md)<!-- link:end -->にある。
- **本筋に残るもの**：スキルは手順の本文と、実行の途中の出力が本筋に残る。サブエージェントは要約だけが戻る。
- **費用の出方**：スキルは読み込まれた本文が、そのあと会話に残り続ける。サブエージェントは自分の request を送るので、同じ使用量の枠を消費する。本筋がすでに持っていた文脈を集め直すこともある。詳しくは<!-- link:begin subagent-isolation#cost -->[サブエージェントは別室の部下 › 賢くはならず、費用がかかる](../basics/subagent-isolation.md#cost)<!-- link:end -->を見る。
- **圧縮の後**：スキルは、呼んだスキルの本文が上限つきで入れ直される。入れ直しの仕組みは<!-- link:begin how-skills-load#after-compaction -->[スキルの考え方（手順を必要なときだけ読む） › 圧縮の後に戻るもの](how-skills-load.md#after-compaction)<!-- link:end -->にある。サブエージェントの記録は、本筋の会話の圧縮の影響を受けない。

## 選び方 {#how-to-choose}

選ぶ基準は、手順の途中を本筋で見たいか、本筋から隔てたいかである。途中の出力を見て判断したい、会話の履歴を使いたい、小さな編集を繰り返したい、のどれかならスキルを選ぶ。出力が多くて本筋を埋める、本筋から独立して進められる、書いた本人ではない者に確かめさせたい、のどれかならサブエージェントを選ぶ。後者は<!-- link:begin subagent-isolation#what-it-helps -->[サブエージェントは別室の部下 › 何に効くか（原理「見せる」と原因「散らかっている」）](../basics/subagent-isolation.md#what-it-helps)<!-- link:end -->で扱う、サブエージェントが向く場面である。

!!! example "判断例：リリース手順"
    - **状況**：リリースのたびに、同じ手順書を会話に貼っている。バージョンを上げ、タグを付け、公開前の出力を人が確かめてから公開する。
    - **迷う候補**：スキルにする。または、リリース専用のサブエージェントに任せる。
    - **選んだもの**：スキル。
    - **理由**：公開前の出力を人が見て承認する手順なので、途中が本筋で見えなければならない。どのバージョンを上げるかという会話の履歴も使う。サブエージェントに任せると、承認の材料が要約になってしまう。作り方は<!-- link:begin writing-skills#when-to-use -->[スキルの作り方 › どんなときにスキルにするか](writing-skills.md#when-to-use)<!-- link:end -->を見る。

!!! example "判断例：長いテスト出力の調査"
    - **状況**：テストを流すと出力が数千行になり、失敗したものを知りたいだけなのに会話がそれで埋まる。
    - **迷う候補**：スキルとして手順を書いて本筋で流す。または、別の文脈の担当に流させて失敗だけを返させる。
    - **選んだもの**：別の文脈の担当に任せる。手順はスキルに書き、フロントマターの `context: fork` で、スキルの本文を担当への依頼として渡す（書き方は次の節にある）。
    - **理由**：欲しいのは出力の全体ではなく、失敗の一覧と原因の候補である。出力の多い調査を隔てる考え方は<!-- link:begin research-in-subagents#when -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 任せてよい調査、本筋で読むべきもの](../context/research-in-subagents.md#when)<!-- link:end -->にある。隔てても失敗の確認は要る。返ってきた要約を、そのまま正しいとは扱わない。

隔てることが効かない場面もある。サブエージェントに渡しても、答えがよくなるわけではない。反復するやり取りや小さな編集は、本筋で行うほうが速い。サブエージェントの向く場面は<!-- link:begin writing-subagents#when-to-use -->[サブエージェントの作り方と使いどころ › 使いどころと、使わない場面](writing-subagents.md#when-to-use)<!-- link:end -->に整理してある。例外を許さない規則を守らせたいなら、フックを選ぶ。スキルもサブエージェントも、お願いの層である。置き場所の全体は<!-- link:begin extensions-at-a-glance -->[拡張機能の全体図と使い分け早見表](extensions-at-a-glance.md)<!-- link:end -->で比べられる。

## 組み合わせ方と確かめ方 {#combine}

2 つは対立するものではなく、組み合わせられる。組み合わせ方は 2 通りで、依頼を書く場所がスキルか委任のメッセージかで分かれる。以下は、2026-11-05 に確かめた公式の文書の挙動である。

**スキルを、サブエージェントとして動かす**。スキルのフロントマターに `context: fork` と `agent` を書く。新しいサブエージェントが起動し、スキルの本文を、その担当への依頼として受け取る。`agent` で、組み込みの Explore・Plan・general-purpose か、自作のサブエージェントを選ぶ。省くと general-purpose になる。結果は要約として本筋に戻る。

<!-- gen:begin snippet skill-vs-subagent/test-triage -->
<!-- textlint-disable -->

??? example "雛形：.claude/skills/test-triage/SKILL.md（サブエージェントとして動くスキル）"

    ```markdown
    ---
    name: test-triage
    description: テストを走らせ、失敗したものだけを原因の候補つきで報告する。テストの出力が長く、本筋の会話を埋めたくないときに使う
    context: fork
    agent: general-purpose
    ---

    # テストの失敗の洗い出し

    次の手順を、この指示だけを頼りに実行する。呼び出した会話の履歴は見えない。

    1. プロジェクトの README や設定ファイルから、テストを実行するコマンドを見つけて実行する。引数は `$ARGUMENTS` で渡される。空なら全体を対象にする
    2. 失敗したテストだけを拾う。通ったテストの出力は報告に含めない
    3. 失敗ごとに、テストの名前、ファイルと行、エラーの要点、原因の候補を 1〜3 行で書く
    4. 最後に、失敗の件数と、1 件を再現するコマンドを書く
    5. 修正はしない。読み取りと実行だけをする
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet skill-vs-subagent/test-triage -->

この形には 3 つの注意がある。

- 名前に反して、今の会話の複製ではない。担当には会話の履歴が見えないので、スキルの本文だけで依頼が成り立つように書く。会話ごと引き継ぐ別の機能（fork したサブエージェント）とは別物である。
- 実行すべき作業がある手順にだけ使う。「この API の規約に従う」のような指針だけを書くと、担当は指針を受け取っても取りかかる作業がなく、意味のある出力を返さない。
- Explore と Plan は CLAUDE.md を読まない。必要な前提は本文に書く。既定ではバックグラウンドで動き、結果は終わったときに届く。待たせたいときは `background: false` を書く。

**サブエージェントに、スキルを読み込ませる**。サブエージェントの定義に `skills` を書くと、起動時にそのスキルの本文が入る。通常のセッションが説明だけを先に読むのと違い、全文が最初から入る。担当に引き継がれないスキルを渡す方法でもある。作業の依頼は、委任のメッセージで渡す。

<!-- gen:begin snippet skill-vs-subagent/release-reviewer -->
<!-- textlint-disable -->

??? example "雛形：.claude/agents/release-reviewer.md（スキルを読み込んで動く読み取り専用のサブエージェント）"

    ```markdown
    ---
    name: release-reviewer
    description: リリース前に、指定されたファイルをチェックリストに沿って読み取り専用でレビューする。変更を書いた会話とは別に確認したいときに使う
    tools: Read, Grep, Glob
    skills:
      - review-checklist
    ---

    あなたはリリース前のレビュー担当である。

    委任のメッセージで指定されたファイルを、起動時に読み込まれた review-checklist の項目に沿って読む。

    - 項目ごとに、問題なし・問題あり・判断できない、のどれかを書く
    - 問題ありには、根拠になるファイルと行を付ける
    - ファイルは変更しない
    - 最初の 1 行に、問題ありの件数を書く
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet skill-vs-subagent/release-reviewer -->

2 つの形の違いは、依頼をどちらに書くかである。`context: fork` では依頼がスキルの本文で、実行役を `agent` で選ぶ。`skills` では依頼が委任のメッセージで、参照資料がスキルである。同じ基準を何度も使うレビューのように、基準を知識として切り出し、レビュー役を隔てたいときは後者が合う。レビュー役を隔てる理由は<!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](../verify/independent-review.md#who)<!-- link:end -->にある。道具を `Read, Grep, Glob` に絞れば、編集できないことを仕組みで保てる。定義の書き方は<!-- link:begin writing-subagents#tools-and-model -->[サブエージェントの作り方と使いどころ › 道具・モデル・effort を絞る](writing-subagents.md#tools-and-model)<!-- link:end -->を見る。

!!! example "判断例：レビューの基準と役割"
    - **状況**：リリース前のレビューに、同じ 10 項目ほどの基準を使う。基準は他の作業でも参照したい。
    - **迷う候補**：基準と役割を、1 つのサブエージェントの定義に書く。または、基準はスキルに書き、役割はサブエージェントに書く。
    - **選んだもの**：基準をスキルに、役割をサブエージェントに分け、サブエージェントに `skills` で基準を読み込ませる。
    - **理由**：基準はレビュー以外の作業でも使うので、スキルにすれば本筋でも呼べる。役割を隔てると、変更を書いた会話の推論を知らない者が確かめられる。

確かめ方は、同じ依頼を新しいセッションで 2 通り試して比べることである。

1. 隔てた場合と、隔てない場合で、`/context` で本筋の文脈の使用量を見る。隔てても本筋の使用量が減らないなら、隔てる意味がない。
2. 返ってきた要約に、根拠の場所（ファイルと行）が含まれているかを見る。ない要約は、確認のやり直しを生む。
3. 要約の主張を 1 つ選び、根拠の場所を自分で開いて確かめる。

効果の比べ方の考え方は<!-- link:begin writing-skills#evaluate -->[スキルの作り方 › 効いているかを確かめる](writing-skills.md#evaluate)<!-- link:end -->にもある。担当を増やすほど、結果を確かめる手間は増える。並列に動かす方式の選び方は<!-- link:begin choosing-parallel-modes -->[並列の方式の選び方](../delegate/choosing-parallel-modes.md)<!-- link:end -->にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)
- [サブエージェントは別室の部下](../basics/subagent-isolation.md)

**関連**

- [スキルの作り方](writing-skills.md)
- [サブエージェントの作り方と使いどころ](writing-subagents.md)
- [拡張機能の全体図と使い分け早見表](extensions-at-a-glance.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)
- [並列の方式の選び方](../delegate/choosing-parallel-modes.md)
- [サブエージェントに引き継がれないもの](what-subagents-dont-inherit.md)
- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
