---
id: what-subagents-dont-inherit
title: サブエージェントに引き継がれないもの
aliases: [サブエージェントが規則を守らない, omitClaudeMd, 委任のプロンプト]
type: feature
field: extend
chapter: サブエージェント
order: 160
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発]
summary: サブエージェントに届かない会話・スキル・出力スタイルなどを知り、要る規則を確実に渡せる。委任の文と定義に書き直し、例外を許さない規則はフックで縛る。
signs:
  - {type: symptom, text: サブエージェントが、会話で決めた前提や規則を知らない}
  - {type: goal, text: サブエージェントにも、日本語で報告させたい}
prerequisites: [writing-subagents]
related: [subagent-isolation, hooks-basics, hook-recipes#subagent-only, keep-replies-in-japanese, replies-in-english, how-skills-load, what-to-put-in-claude-md, research-in-subagents]
tracks: [subagents]
sources: [cc-docs-sub-agents, cc-docs-features-overview, cc-docs-features-overview-ja, cc-docs-hooks]
volatility: 中
sections:
  - {title: 届くものと届かないもの, anchor: what-arrives}
  - {title: 規則を委任の文に書き直す, anchor: hand-over}
  - {title: 使うスキルは定義に書いて読ませる, anchor: skills-field}
  - {title: 例外を許さない規則はフックで縛る, anchor: enforce}
  - {title: 日本語で報告させる, anchor: language}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：サブエージェントに届かない会話・スキル・出力スタイルなどを知り、要る規則を委任の文と定義で確実に渡せる。
    - **いつ引くか**：会話で決めた前提や規則を担当が知らないとき、担当にも日本語で報告させたいとき。
    - **前提**：<!-- link:begin writing-subagents -->[サブエージェントの作り方と使いどころ](writing-subagents.md)<!-- link:end -->
    - **強制力**：委任の文と定義の本文に書いた規則はお願いで、守られる保証はない。例外を許さない規則は、フックか道具の制限（鍵）で縛る。成熟度は <!-- gen:begin feature maturity -->GA<!-- gen:end feature maturity -->、読み込みの時期は <!-- gen:begin feature load_timing -->起動したとき<!-- gen:end feature load_timing -->、コンテキストのコストは <!-- gen:begin feature context_cost -->分離<!-- gen:end feature context_cost --> である。

<!-- textlint-disable -->
別名：サブエージェントが規則を守らない・omitClaudeMd・委任のプロンプト
<!-- textlint-enable -->

サブエージェントに引き継がれないものは、親の会話では見えている情報のうち、担当の側には見えないものの一覧である。担当は別の文脈で動くので、会話で決めた規則が見えていないまま作業を始める。ここでは、何が届くか、見えていないものをどう渡し直すか、渡し直しで足りない規則をどう縛るかを扱う。

## 届くものと届かないもの {#what-arrives}

サブエージェント（fork でない担当）の文脈は、起動のときに作り直される。親の会話の履歴は持ち込まれない。次の表は、公式の文書（確認日 2026-11-04）で確かめた範囲である。

| 親にあるもの | 担当に届くか | 渡し方 |
| --- | --- | --- |
| 会話の履歴・会話で決めた約束 | 届かない | 委任の文に書く |
| 親が読み込んだスキル | 届かない | 定義の `skills` に書く |
| 出力スタイル（output style） | 届かない（fork を除く） | 委任の文か定義の本文に書く |
| 自動メモリ（auto memory） | 届かない | 委任の文に書く |
| CLAUDE.md と git status | 届く。組み込みの Explore と Plan、`omitClaudeMd` を付けた担当には届かない | 届かない担当には委任の文に書く |
| 設定（settings・プラグイン）に書いたフック | 担当の中でも走る | そのまま使える |

担当が動く土台は、自分のシステムプロンプト（定義の本文）、`skills` に挙げたスキル、CLAUDE.md と git status である。親から担当へ渡る道は、委任の文（Claude が担当に渡す依頼文）だけである。つまり、規則を確実に渡す場所は、委任の文と定義の 2 つに絞られる。例外は fork で、親の会話全体を引き継ぐ。

防ぐ原因は「見えていない」である。担当が規則を破ったように見えても、多くは、規則が見えていないだけである。担当が別の文脈で動く理由と費用は <!-- link:begin subagent-isolation#why -->[サブエージェントは別室の部下 › なぜ本筋が散らからないのか](../basics/subagent-isolation.md#why)<!-- link:end --> を見る。

## 規則を委任の文に書き直す {#hand-over}

会話で決めた規則は、担当が読める形に書き直して渡す。担当は「さっきの方針」や「前に決めたやり方」を知らないので、指す言葉を使わず、中身を書く。

=== "Claude Code"

    1. **渡したい規則を拾う**：この作業に効く約束だけを選ぶ。目的と完了の形・触ってよい範囲・守る規則・報告の言語と形の 4 つが目安である。会話の全文は貼らない。
    2. **委任の文に書き直す**：「例の件」のような指す言葉を避け、規則そのものを書く。頼み方は下の雛形にある。
    3. **毎回要る規則は定義に移す**：同じ規則を何度も書くなら、担当の定義の本文に置く。定義の本文は、担当のシステムプロンプトとして毎回届く。
    4. **返ってきた報告で確かめる**：規則どおりに動いたかを、報告の中身で見る。

書き直す前と後は次のとおりである。

- Before：「認証まわりを調べて」
- After：「認証まわりの呼び出し元を調べて。ファイルは編集しない。日本語で、結論・根拠の場所・未確認の点の順に報告して」

After で足したのは、範囲（編集しない）と、報告の言語と形である。足した規則は担当の側から見えるので、守られやすくなる。ただし、お願いなので保証はない。

<!-- gen:begin snippet what-subagents-dont-inherit/delegate-with-rules -->
<!-- textlint-disable -->

??? example "雛形：会話で決めた規則を、委任の文に書き直させるプロンプト"

    ```text
    <調査や作業の内容> を subagent に任せてください。依頼文には、この会話で決めた次の点を、あなたの言葉で省かずに書いてください。担当はこの会話を見られません。

    - 目的と完了の形：<何が分かれば終わりか>
    - 触ってよい範囲：<例：src/auth/ の読み取りだけ。ファイルは編集しない>
    - 守る規則：<例：外部への通信をしない。テストは tests/auth だけ走らせる>
    - 報告の言語と形：日本語で、結論・根拠の場所（ファイルと行）・未確認の点の順に書く

    担当の報告が戻ったら、上の規則が守られているかを確かめてから、結果を私に伝えてください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet what-subagents-dont-inherit/delegate-with-rules -->

自動で任せるとき、委任の文を書くのは Claude である。頼む側は、上の雛形のように、依頼文に含めてほしい項目を指定できる。調査を任せるときの頼み方と戻させる形は <!-- link:begin research-in-subagents#how -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 頼み方と戻させる形](../context/research-in-subagents.md#how)<!-- link:end --> にある。

## 使うスキルは定義に書いて読ませる {#skills-field}

親が読み込んだスキルは、担当には引き継がれない。担当にスキルを使わせるときは、担当の定義の `skills` の項目に、スキルの名前を挙げる。挙げたスキルは、担当が起動するときに全文が読み込まれる。

通常のスキルは、説明文だけが常駐し、本文は必要なときに読まれる（仕組みは <!-- link:begin how-skills-load#what-happens -->[スキルの考え方（手順を必要なときだけ読む） › 何が起きるか](how-skills-load.md#what-happens)<!-- link:end --> を見る）。定義の `skills` に挙げたスキルはそうならず、担当の文脈に最初から入る。長いスキルを何本も挙げると、担当の文脈を最初から使うので、その担当が使う分だけに絞る。

手動専用（`disable-model-invocation: true`）のスキルは、担当の定義の `skills` に挙げても、事前の読み込みができない。そのスキルが要る手順は、人が呼ぶか、委任の文に書き直す。理由と範囲は <!-- link:begin manual-only-skills#limits -->[副作用のあるスキルを勝手に動かさない › 効かない場面と落とし穴](manual-only-skills.md#limits)<!-- link:end --> にある。

<!-- gen:begin snippet what-subagents-dont-inherit/skills-in-definition -->
<!-- textlint-disable -->

??? example "雛形：使うスキルを先に読ませる定義（skills の項目）"

    ```markdown
    ---
    name: pr-reviewer
    description: 変更の差分を、チームのレビュー基準に沿って確かめるレビュアー。コードは編集しない。実装を終えた後やコミットの前に、書いた本人とは別の目で確かめたいときに使う。
    tools: Read, Grep, Glob
    skills:
      - review-checklist
    ---

    あなたは変更を読んで報告するだけのレビュアーである。ファイルを編集しない。

    - 確かめる基準は、読み込まれている review-checklist のスキルと、依頼文に書かれたものだけである
    - 報告は日本語で書く。コードや識別子は原文のままにする
    - 指摘ごとに、場所（ファイルと行）、問題、確かめ方を書く
    - 依頼文に書かれていない前提は推測せず、「未確認」として報告に挙げる
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.60。

<!-- textlint-enable -->
<!-- gen:end snippet what-subagents-dont-inherit/skills-in-definition -->

定義の書き方と、道具・モデルの絞り方は <!-- link:begin writing-subagents#define -->[サブエージェントの作り方と使いどころ › 定義の書き方（ファイルを書くか、Claude に作らせる）](writing-subagents.md#define)<!-- link:end --> にある。

## 例外を許さない規則はフックで縛る {#enforce}

委任の文と定義の本文に書いた規則は、お願いである。破られて困る規則は、お願いのままにせず、フックで止める。

設定（`settings.json`・管理の設定・プラグイン）に書いたフックは、サブエージェントの中でも走る。PreToolUse と PostToolUse は、メインと同じに発火する。つまり、1 つのフックで、メインと担当の両方を見られる。担当の定義のフロントマターに書いたフックは、その担当が動く間だけ走る。

担当にだけ禁じたいときは、フックの入力にある `agent_id` を見る。組み方は <!-- link:begin hook-recipes#subagent-only -->[代表的なフックのレシピ › 担当にだけ禁じる（agent\_id）](../enforce/hook-recipes.md#subagent-only)<!-- link:end -->、フックの置き場所と効く範囲は <!-- link:begin hooks-basics#locations -->[フックの考え方とイベント › 置き場所と効く範囲（サブエージェントと信頼の確認）](../enforce/hooks-basics.md#locations)<!-- link:end --> にある。道具の制限（定義の `tools` と `disallowedTools`）も鍵だが、止められるのは道具の単位までである。

!!! example "判断例：読み取り専用の調査で、設定ファイルを触らせない"
    - **状況**：親の会話で「設定ファイルは触らない」と決めた。調査を担当に任せるが、担当はこの約束を見ていない。
    - **迷う候補**：委任の文に「設定ファイルは触らない」と書く。設定ファイルへの書き込みをフックで止める。
    - **選んだもの**：委任の文には、規則と理由を書く。設定ファイルへの書き込みは、フックでも止める。
    - **理由**：委任の文は、担当に規則を見せるための手段である。破られた場合に備えて止めるのは、フックの役目である。見せることと、止めることを、別の手段に分ける。

## 日本語で報告させる {#language}

サブエージェントにも日本語で報告させたいときは、届く場所に書く。出力スタイルは fork でない担当に届かず、CLAUDE.md は Explore と Plan に届かない。`language` の設定が担当に効くかは、公式の文書（確認日 2026-11-04）に書かれていない。確実に届くのは、委任の文と定義の本文である。

1. 委任の文に、報告の言語と形を書く。雛形は「規則を委任の文に書き直す」の節にある。
2. 毎回日本語で返させる担当は、定義の本文に「報告は日本語で書く。コードや識別子は原文のままにする」を置く。
3. 戻った報告の言語を確かめたいなら、SubagentStop のフックで最後の返事を確かめる方法がある（組み方は <!-- link:begin keep-replies-in-japanese#stop-hook -->[日本語で返し続けさせる › Stop フックで最後の返事を確かめる](../japanese/keep-replies-in-japanese.md#stop-hook)<!-- link:end --> を見る）。

英語で返る原因は、届かない指示だけとは限らない。英語のツール出力や報告を読んだ後に、英語へ戻ることもある。切り分けは <!-- link:begin replies-in-english#diagnosis -->[英語で返ってくる › 原因を安く確かめる順](../symptoms/replies-in-english.md#diagnosis)<!-- link:end --> に任せ、届く範囲の全体は <!-- link:begin keep-replies-in-japanese#reach -->[日本語で返し続けさせる › 届かない所（サブエージェント・圧縮の要約・クラウドのセッション）](../japanese/keep-replies-in-japanese.md#reach)<!-- link:end --> を見る。

## 効かない場面・落とし穴 {#pitfalls}

- **Explore と Plan は CLAUDE.md を読まない**：組み込みの Explore と Plan は、CLAUDE.md と git status を持たない。CLAUDE.md に書いた規則は、この 2 つには届かないので、委任の文に書く。
- **`omitClaudeMd` を付けた担当にも届かない**：定義にこれを付けた担当は、CLAUDE.md を読まない。規則が届かないときは、定義に `omitClaudeMd` がないかを確かめる。
- **書いても守られる保証はない**：委任の文も定義の本文もお願いである。破られて困る規則は、フックに移す。CLAUDE.md の行を鍵へ移す考え方は <!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end --> にある。
- **定義の `disallowedTools` に指定子を付けても、Bash 全体が外れる**：特定のコマンドだけを止めるなら、フックを使う（<!-- link:begin writing-subagents#pitfalls -->[サブエージェントの作り方と使いどころ › 効かない場面・落とし穴](writing-subagents.md#pitfalls)<!-- link:end --> を見る）。
- **渡しすぎると別室の利点が消える**：会話の全文や長い経緯を貼ると、担当の文脈が埋まる。作業に効く規則だけを渡す。
- **自動の委任では、委任の文を Claude が書く**：書いてほしい規則が毎回の委任に入るとは限らない。毎回要るものは、定義の本文に置く。
- **規則が届いたかは、報告で見る**：報告の先頭に、守った規則を 1 行で書かせると、届いたかを読み取りやすい（推論・実践例なし）。

## 比べる相手 {#compare}

- **CLAUDE.md**：全体の規則を置く場所で、fork でない担当には届く。ただし、Explore と Plan、`omitClaudeMd` の担当には届かない。届く担当でも、お願いである（<!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)<!-- link:end --> を見る）。
- **fork**：親の会話を引き継ぐ担当である。見えていない問題は起きにくいが、別室の利点である文脈の分離も弱まる。
- **フック**：担当の中でも走る。規則を見せるのではなく、操作を止める手段である（<!-- link:begin hooks-basics -->[フックの考え方とイベント](../enforce/hooks-basics.md)<!-- link:end --> を見る）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Claude Code を拡張する](https://code.claude.com/docs/ja/features-overview)：Anthropic・確認日 2026-11-04
- [Hooks reference](https://code.claude.com/docs/en/hooks)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [サブエージェントの作り方と使いどころ](writing-subagents.md)

**関連**

- [サブエージェントは別室の部下](../basics/subagent-isolation.md)
- [フックの考え方とイベント](../enforce/hooks-basics.md)
- [代表的なフックのレシピ › 担当にだけ禁じる（agent\_id）](../enforce/hook-recipes.md#subagent-only)
- [日本語で返し続けさせる](../japanese/keep-replies-in-japanese.md)
- [英語で返ってくる](../symptoms/replies-in-english.md)
- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)
- [CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](../context/research-in-subagents.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
