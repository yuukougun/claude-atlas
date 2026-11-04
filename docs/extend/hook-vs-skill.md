---
id: hook-vs-skill
title: フックとスキルの違い
aliases: [hook と skill の使い分け, hooks と skills]
type: comparison
field: extend
chapter: スキル
order: 140
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [縛る, 見せる]
prevents: [縛っていない]
pitfalls: []
scenes: [開発]
summary: 決まった手順をスキルにするか、フックで必ず走らせるかを選べる。スキルは Claude が判断して使うお願いで、フックは決まったときに必ず動く鍵である。
signs:
  - {type: symptom, text: スキルに書いた手順の、必ずやってほしい一歩を飛ばされる}
  - {type: goal, text: 手順として読ませるか、自動で必ず走らせるかを決めたい}
prerequisites: [request-vs-lock, how-skills-load]
related: [hooks-basics, when-to-lock, request-lock-table, hook-recipes, writing-skills, manual-only-skills, extensions-at-a-glance, textlint-hook, less-ai-sounding-japanese#lint-vs-judgment]
tracks: [hooks, skills]
sources: [cc-docs-hooks-guide, cc-docs-features-overview, cc-docs-skills, cc-docs-context-window, claude-blog-steering-code-skills-hooks]
sections:
  - {title: 比較の表, anchor: table}
  - {title: フックとスキルの選び方, anchor: how-to-choose}
  - {title: 組み合わせ方, anchor: combine}
  - {title: 移したあとの確かめ方, anchor: verify}
volatility: 中
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：手順の中身を読んで判断しながら進めてほしいならスキル、きっかけが決まっていて例外なく毎回走らせたい一歩ならフックに、置き分けられる。スキルは Claude が読んで従うお願いで、フックは Claude の判断を通さずに動く鍵である。
    - **いつ引くか**：スキルに書いた手順の、必ずやってほしい一歩を飛ばされるとき。手順として読ませるか、自動で必ず走らせるかを決めたいとき。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->、<!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)<!-- link:end -->

<!-- textlint-disable -->
別名：hook と skill の使い分け・hooks と skills
<!-- textlint-enable -->

フックとスキルの違いは、手順を実行するかどうかを誰が決めるかにある。スキルでは Claude が決め、フックでは設定が決める。必ずやってほしい一歩をスキルの手順にだけ書くと、縛っていないのと同じになる。

## 比較の表 {#table}

フックとスキルを、属性ごとに比べる表である。置き場所を選ぶときに見る列は、強制力・読み込みの時期・コンテキストのコスト・圧縮で残るかである。2 つの機能で同じ値の列は、表から省いて表の下にまとめてある。

<!-- gen:begin compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 強制力 | 読み込みの時期 | コンテキストのコスト |
| --- | --- | --- | --- |
| [フック（hooks）](../enforce/hooks-basics.md) | 鍵 | イベントが起きたとき | ゼロ（出力を返さない限り） |
| [スキル（skills）](writing-skills.md) | お願い | セッション開始と使うとき | 使うまで小さい |

すべて共通：圧縮で残るか 残る。

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->

表の値だけでは分からない点を補う。まずスキルである。名前と説明は毎回の会話に入り、Claude はその説明を読んで、今の依頼にスキルを使うかを判断する。説明が曖昧だったり、ほかのスキルと重なったりすると、使うべき場面で呼ばれなかったり、違う場面で呼ばれたりする。確実に呼ばせたいときは、人が `/<名前>` で呼ぶ。呼ばれたあとも、本文は Claude が読んで従う指示であり、手順の一歩が飛ばされる可能性は残る。外れ方は 2 段階ある。呼ばれない回と、呼ばれても飛ばされる回である。公式の文書は、スキルの指示はお願いであり保証ではないと述べている。

次にフックである。フックは会話の外にある設定で、ファイルを書いた直後・道具を使う前・ターンの終わりのような決まったきっかけに、コマンドを走らせる。Claude が手順を思い出すかどうかに左右されない。一方、コマンドのフックは判断をしない。「この変更は危ないか」のような読んで決めることは、フックでは書けない。Claude とは別のモデルに判断させる型のフックもあるが、判断の結果が毎回同じになる保証はないので、この辞典では鍵に数えない。型の違いは<!-- link:begin hooks-basics#deterministic -->[フックの考え方とイベント › 決定的なフックと、モデルが判断するフック](../enforce/hooks-basics.md#deterministic)<!-- link:end -->を見る。

最後に、圧縮の扱いである。表では両方とも圧縮の後に残るとあるが、残り方は違う。フックは会話の外にあるので、圧縮の影響を受けない。スキルは、名前と説明が入れ直され、すでに呼んだスキルの本文は上限つきで入れ直されて、古いものから外れる。長い作業の途中で手順が薄れる場合は、<!-- link:begin how-skills-load#after-compaction -->[スキルの考え方（手順を必要なときだけ読む） › 圧縮の後に戻るもの](how-skills-load.md#after-compaction)<!-- link:end -->を見る。

フックにも弱点がある。フックはユーザーの権限で任意のコマンドを実行するので、プラグインやリポジトリから来たフックは中身を確かめてから有効にする。既定では、フックのコマンドが自分で落ちても作業は止まらず、守りが黙って外れうる。守りの用途では、落ちたときに止まる設定があるかを確かめる。効かない場面は<!-- link:begin hooks-basics#limits -->[フックの考え方とイベント › 効かない場面と落とし穴](../enforce/hooks-basics.md#limits)<!-- link:end -->を見る。ここで扱った範囲は、Claude Code のコマンドライン（WSL・Linux）を基準にしている。ほかの OS と IDE 拡張での動作は未確認である。

## フックとスキルの選び方 {#how-to-choose}

ある一歩をフックとスキルのどちらに置くかは、3 つの問いで決まる。次の順に当てはめる。

1. **きっかけが決まっているか**：「ファイルを書いた直後」「あるコマンドを使う前」「ターンの終わり」のように、イベントで言えるならフックの候補になる。「このあたりでやる」としか言えないなら、スキルに置く。
2. **例外がなく、機械で判定できるか**：常に同じ結果になる処理で、やるかやらないかの判断が要らないなら、フックに置く。読んで判断することが混ざるなら、スキルに置く。
3. **中身は処理か、手順や知識か**：1 つのコマンドで済む処理はフックに向く。順序・理由・場合分けを含む長い手順は、スキルに向く。

フックに移すのは、手順のうち、1 と 2 を満たす一歩だけである。手順全体を移すのではない。例外を許さない禁止を鍵に移す判断の全体は<!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end -->を見る。

!!! example "判断例：編集のあとの整形"
    - **状況**：ソースを編集したあとに、必ず prettier を流してほしい。今は、スキルの手順の 1 つとして書いてあるが、整形されていない編集が混ざる。
    - **迷う候補**：スキルの手順に書き続ける。説明を書き直して、スキルが呼ばれやすくする。編集の直後にフックを動かす。
    - **選んだもの**：フックに置く。
    - **理由**：きっかけ（編集の直後）が決まっていて、例外がなく、1 つのコマンドで済むので、3 つの問いにすべて当てはまる。スキルのままでは、呼ばれない回と飛ばされる回の 2 段階で外れる。説明を直しても、後者は減らない。ただし、整形から外すファイルの判断は、ツールの設定（`.prettierignore`）に寄せる。フックに判断は書けない。

同じ「編集のあとに整形する」を、スキルとフックで書いた対比を示す。スキルの手順には、整形から外すファイルの判断を含めてある。フックは、ファイルが書かれるたびに同じ処理を走らせる。

<!-- gen:begin snippet hook-vs-skill/format-skill -->
<!-- textlint-disable -->

??? example "雛形：.claude/skills/format-after-edit/SKILL.md（整形の手順を書いたスキル）"

    ```markdown
    ---
    name: format-after-edit
    description: ソースファイルを編集するときに使う。編集のあとに prettier で整形する手順を書いている
    ---

    # 編集のあとの整形

    1. ソースファイルを編集したら、そのファイルに `npx prettier --write <ファイル>` を流す
    2. `.prettierignore` に載っているファイルと、生成物（`generated/` の下）には流さない
    3. 整形で差分が増えたときは、増えた差分も含めて、変更の内容を確かめる
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet hook-vs-skill/format-skill -->

<!-- gen:begin snippet hook-vs-skill/format-hook -->
<!-- textlint-disable -->

??? example "雛形：.claude/settings.json（編集のたびに必ず整形するフック）"

    ```json
    {
      "hooks": {
        "PostToolUse": [
          {
            "matcher": "Edit|Write",
            "hooks": [
              {
                "type": "command",
                "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write --ignore-unknown"
              }
            ]
          }
        ]
      }
    }
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 1.0.38。

<!-- textlint-enable -->
<!-- gen:end snippet hook-vs-skill/format-hook -->

!!! example "判断例：リリースの手順"
    - **状況**：バージョンを上げ、変更履歴を書き、タグを付けて公開する手順がある。公開は main の上でしかしてはいけない。
    - **迷う候補**：手順の全体をスキルに書く。全体をフックにする。手順はスキルに、公開の条件だけを鍵に分ける。
    - **選んだもの**：手順はスキルに書き、「main 以外では公開しない」だけを、道具を使う前に動くフック（PreToolUse）か deny ルールで止める。
    - **理由**：変更履歴の文面や、どこまで確認してから公開するかは、読んで判断する部分なので、スキルに向く。ブランチの条件は機械で判定でき、例外がないので、鍵に向く。公開のように副作用のある手順は、Claude が自分で呼ばないようにもできる。その設定と、それでも鍵が要る場面は<!-- link:begin manual-only-skills -->副作用のあるスキルを勝手に動かさない（準備中）<!-- link:end -->を見る。

!!! example "判断例：日本語の文体を揃える"
    - **状況**：Claude に日本語の文章を書かせている。表記の揺れと、読みにくい言い回しの両方を減らしたい。
    - **迷う候補**：全部を textlint のフックで直させる。全部を推敲のスキルに任せる。機械で見つかるものはフック、判断が要るものはスキルに分ける。
    - **選んだもの**：分ける。
    - **理由**：表記の揺れのように、機械で見つけられる違反は、書いた直後に走るフックで確実に拾える。読みにくさの型や、文章の構成の直しは、読んで判断することが多いので、スキルに任せる。分け方の詳細は<!-- link:begin textlint-hook#rules -->[textlint をフックで回す › どのルールを機械に任せるか](../japanese/textlint-hook.md#rules)<!-- link:end -->と<!-- link:begin less-ai-sounding-japanese#lint-vs-judgment -->日本語の「AI 臭さ」を減らす › lint に任せる所と、判断の要る所（準備中）<!-- link:end -->を見る。

!!! example "判断例：テストを流す一歩が飛ばされる"
    - **状況**：スキルの最後の一歩に「テストを流して、通ってから終わる」と書いてある。ときどき、テストを流さずに終わりを宣言される。
    - **迷う候補**：手順の文を強調する。スキルの説明を直す。ターンの終わりに動くフック（Stop）で、テストが通るまで終わらせない。Stop は Claude が応答を終えようとしたときに動くイベントである。
    - **選んだもの**：テストが失敗しているときだけ終わりを止める Stop のフックを置く。
    - **理由**：強調はお願いのままで、飛ばされる可能性は残る。「終わるとき」は、フックのイベントで言えるきっかけであり、テストの成否は機械で判定できる。ただし、常に止めるフックは Claude を終わらせなくなるので、失敗しているときに限る。止めたときの理由は Claude に渡るので、直す手がかりを書く。イベントの選び方は<!-- link:begin hooks-basics#events -->[フックの考え方とイベント › 代表的なイベント](../enforce/hooks-basics.md#events)<!-- link:end -->を見る。

## 組み合わせ方 {#combine}

フックとスキルは択一ではない。1 つの作業の中で、役割を分けて同時に使う。

- **スキル**：手順の全体・順序・理由・場合分けを置く。読んで判断する一歩はここに残す。
- **フック**：飛ばされると困る一歩のうち、きっかけが決まっていて機械で判定できるものを置く。
- **deny ルール**：道具の使用を例外なく断る禁止を置く。フックとの選び方は<!-- link:begin request-lock-table#table -->[お願いと鍵の対応表 › 用途ごとの対応表](../enforce/request-lock-table.md#table)<!-- link:end -->を見る。

分け方の決まりは、同じ一歩を二か所に書かないことである。フックに移した一歩は、スキルの手順から外し、「整形はフックが走らせる」のように一言だけ残す。二か所に書くと、片方だけを直したときに食い違う。

フックが止めたときの理由は、Claude に渡される。理由の文を、スキルの手順で使う言葉に揃えておくと、止められたあとに何をすればよいかが伝わる。

スキルのフロントマター（ファイルの先頭の設定欄）にも、フックを書ける。ある手順だけのチェックを、スキルと一緒に配りたいなら、この書き方が使える。有効になる範囲の細部は、<!-- link:begin hooks-basics#locations -->[フックの考え方とイベント › 置き場所と効く範囲（サブエージェントと信頼の確認）](../enforce/hooks-basics.md#locations)<!-- link:end -->と公式の文書で確かめる。

どちらに置くか迷うときは、まずスキルに書いてよい。同じ注意を繰り返すようになってから、その一歩だけをフックに移すほうが、無駄なフックを増やさない。

## 移したあとの確かめ方 {#verify}

一歩をフックに移したあとは、実際に走ったかを確かめる。確かめ方は次のとおりである。

1. 新しいセッションを開き、`/hooks` でフックが一覧に出ているかを見る。
2. きっかけになる操作を Claude にさせて、移した一歩が毎回走ったかを見る。1 回で判断せず、スキルのときに飛ばされた依頼を、同じ形で数回流す。
3. 走らないときは、matcher（どの道具に反応するかの指定）と、Bash で書いたファイルのような拾えない書き込みを疑う。診断は<!-- link:begin hooks-basics#not-running -->[フックの考え方とイベント › 動いていないように見えるとき](../enforce/hooks-basics.md#not-running)<!-- link:end -->にある。

スキルのほうは、同じ依頼を数回流して、呼ばれた回数と、手順のどの一歩が抜けたかを記録する。効いているかの確かめ方は<!-- link:begin writing-skills#evaluate -->[スキルの作り方 › 効いているかを確かめる](writing-skills.md#evaluate)<!-- link:end -->を見る。移す前と移した後で、抜けた回数を比べると、移した効果が分かる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)
- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)

**関連**

- [フックの考え方とイベント](../enforce/hooks-basics.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [お願いと鍵の対応表](../enforce/request-lock-table.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [スキルの作り方](writing-skills.md)
- 副作用のあるスキルを勝手に動かさない（準備中）
- [拡張機能の全体図と使い分け早見表](extensions-at-a-glance.md)
- [textlint をフックで回す](../japanese/textlint-hook.md)
- 日本語の「AI 臭さ」を減らす › lint に任せる所と、判断の要る所（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
