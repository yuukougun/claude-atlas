---
id: when-to-add-what
title: 拡張を足すタイミング
aliases: [足すタイミング表, Build your setup over time, いつスキルにするか, いつフックにするか]
type: concept
field: extend
chapter: 全体と使い分け
order: 10
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる, 縛る]
prevents: [見えていない, 縛っていない]
pitfalls: []
scenes: [開発]
summary: 同じ注意や手順の繰り返しから、どの拡張をいつ足すかが分かる。最初から作り込まず、繰り返しが見えてから仕組みに移すほうがよい理由も分かる。
signs:
  - {type: goal, text: 繰り返している注意や手順を、どの仕組みに移すか決めたい}
  - {type: goal, text: 設定や拡張を何から足せばよいか知りたい}
  - {type: situation, text: 便利な拡張の記事を見て、全部入れたくなっている}
prerequisites: [request-vs-lock]
related: [extensions-at-a-glance, claude-md-vs-rules-skills-styles, when-to-lock, repeating-the-same-explanation, always-on-costs, what-to-put-in-claude-md, how-skills-load, writing-subagents, connecting-mcp, code-intelligence-plugins, plugins-and-marketplaces, hooks-basics, output-style-modes, pruning-extensions]
tracks: [claude-md, output-styles, skills, subagents, mcp, hooks, plugins]
sources: [cc-docs-features-overview, cc-docs-features-overview-ja, cc-docs-context-window, claude-blog-steering-code-skills-hooks]
volatility: 中
sections:
  - {title: 何が起きるか, anchor: what-happens}
  - {title: 繰り返しの種類と移す先, anchor: triggers}
  - {title: 繰り返しを見つける, anchor: noticing}
  - {title: 繰り返しが見えてから足す理由, anchor: why}
  - {title: 足す前に見る強制力とコスト, anchor: costs}
  - {title: 判断例, anchor: examples}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：同じ注意や手順の繰り返しから、どの拡張をいつ足すかが分かる。最初から作り込まず、繰り返しが見えてから仕組みに移すほうがよい理由も分かる。
    - **いつ引くか**：繰り返している注意や手順を、どの仕組みに移すか決めたいとき。設定や拡張を何から足せばよいか知りたいとき。便利な拡張の記事を見て、全部入れたくなっているとき。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：足すタイミング表・Build your setup over time・いつスキルにするか・いつフックにするか
<!-- textlint-enable -->

拡張を足すタイミングは、同じことを Claude Code に繰り返し言った事実で決める。公式の文書も、拡張を一度に揃えず、繰り返しが見えるたびに 1 つずつ足す順で書いている。

## 何が起きるか {#what-happens}

拡張の紹介記事を読むと、CLAUDE.md・スキル・サブエージェント・フック・MCP・プラグインを、まとめて入れたくなる。入れた直後は整った環境に見える。しかし、自分が実際に繰り返していることと、入れたものが合っているとは限らない。

入れたものには、使わなくても払う費用がある。CLAUDE.md は全文が毎回のリクエストに乗り、スキルは説明が毎回入る。プラグインは、入れると中のスキルやエージェントの名前と説明が毎回入る。使わない拡張でも、常駐する分は Claude の焦点を散らし、費用を増やす。

逆に、何も足さないままだと、同じ注意を毎回言い直すことになる。言い直した内容は、会話が変わると Claude から見えなくなる。足す境目は、同じことの繰り返しが見えたかどうかである。

## 繰り返しの種類と移す先 {#triggers}

繰り返している内容の種類で、移す先がほぼ決まる。下の表は、公式の「Build your setup over time」の対応を、読者の言葉で並べ直したものである。

| 繰り返していること | 移す先 | 詳しく |
| --- | --- | --- |
| 同じ規約やコマンドを、何度も間違える | CLAUDE.md | <!-- link:begin what-to-put-in-claude-md -->[CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)<!-- link:end --> |
| 毎回「短く」「説明を多めに」と頼んでいる | 出力スタイル | <!-- link:begin output-style-modes -->[出力スタイルで応答の仕方を切り替える](../cli/output-style-modes.md)<!-- link:end --> |
| 同じ開始の依頼を、毎回打っている | 自分で呼び出せるスキル | <!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)<!-- link:end --> |
| 同じ手順書を、何度も貼っている | スキル | <!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)<!-- link:end --> |
| ブラウザのデータを、コピーして貼り続けている | MCP | <!-- link:begin connecting-mcp -->[MCP をつなぐ](connecting-mcp.md)<!-- link:end --> |
| 定義の探索のために、多数のファイルを読ませている | code intelligence プラグイン | <!-- link:begin code-intelligence-plugins -->[code intelligence プラグイン（LSP）](code-intelligence-plugins.md)<!-- link:end --> |
| 副作業の出力が、会話を埋めてしまう | サブエージェント | <!-- link:begin writing-subagents -->[サブエージェントの作り方と使いどころ](writing-subagents.md)<!-- link:end --> |
| 毎回、必ず起きてほしいことがある | フック | <!-- link:begin hooks-basics -->[フックの考え方とイベント](../enforce/hooks-basics.md)<!-- link:end --> |
| 2 つ目のリポジトリでも、同じ設定を使いたい | プラグイン | <!-- link:begin plugins-and-marketplaces -->[プラグインとマーケットプレイス](plugins-and-marketplaces.md)<!-- link:end --> |

公式の表は、規約を間違えた回数や手順書を貼った回数を添えて、足す目安を示している。回数は公式の表の値で、変わりうる。この表は種類だけを並べ、回数を載せない。大事なのは、何回かではなく、「同じことを、また言っている」と気づくことである。

表で迷うのは、同じ繰り返しが 2 つの行に当たるときである。たとえば、手順書を貼っていて、しかも毎回必ず実行してほしいなら、スキルとフックの両方に当たる。このときは、守られなくても取り返せる手順ならスキル、例外なく毎回起きなければならないことならフックを選ぶ。お願いと鍵の分け方は <!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end --> にある。置き場所を 4 つ並べて選ぶときは <!-- link:begin claude-md-vs-rules-skills-styles#how-to-choose -->[CLAUDE.md・rules・スキル・出力スタイルの違い › 指示の置き場所の選び方](claude-md-vs-rules-skills-styles.md#how-to-choose)<!-- link:end --> を引く。

## 繰り返しを見つける {#noticing}

繰り返しは、気づかないと数えられない。言い直すたびに、その内容を一行のメモに残すと、たまったメモが「足す根拠」になる。メモは、会話の外（自分のメモ帳やリポジトリの下書き）に置く。会話の中に置くと、圧縮や新しいセッションで見えなくなる。

メモがたまったら、Claude に仕分けさせると速い。下の依頼は、メモの各行を移し先の候補に分け、まだ何も作らせない。仕分けの結果を、そのまま信じず、自分で表と見比べる。

<!-- gen:begin snippet when-to-add-what/sort-repeats -->
<!-- textlint-disable -->

??? example "雛形：繰り返したメモを移し先に仕分けさせる依頼"

    ```markdown
    次のメモは、私が最近 Claude に言い直した注意や、貼り直した手順の記録である。

    <ここに、言い直した内容を 1 行ずつ貼る。いつ・どこで言ったかも、分かる範囲で添える>

    各行を、移し先の候補に仕分けてほしい。候補は次のとおり。

    - CLAUDE.md（毎回効かせる規約・コマンド・落とし穴）
    - 出力スタイル（応答の長さ・口調・形）
    - スキル（ときどき使う手順書）
    - サブエージェント（出力が多い調査・確認の作業）
    - フック（例外がなく、機械で判定できる、毎回必ず起きてほしいこと）
    - 移さない（まだ繰り返しが見えていない）

    行ごとに、移し先と理由を 1 行で書く。同じ種類の行は 1 つにまとめる。

    今は何も作らず、仕分けの表だけを出す。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet when-to-add-what/sort-repeats -->

毎回同じ背景を説明している状態から、置き場所を決める診断は <!-- link:begin repeating-the-same-explanation#diagnosis -->[毎回同じ説明をしている › 原因を安く確かめる順](../symptoms/repeating-the-same-explanation.md#diagnosis)<!-- link:end --> にある。

## 繰り返しが見えてから足す理由 {#why}

足すのを繰り返しが見えてからにする理由は 3 つある。

- **形が決まる**：何を繰り返しているかが見えると、移す先の種類も、書く中身も決まる。先に作ると、実際の繰り返しとずれた中身になりやすい。
- **常駐の費用を払わずに済む**：常駐するものは、使わなくても毎回の費用がかかる。常駐を小さく保つ理由は <!-- link:begin always-on-costs#resident-vs-on-demand -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 常駐するものと、使うときだけ読むもの](../context/always-on-costs.md#resident-vs-on-demand)<!-- link:end --> にある。
- **削る作業が減る**：足したものは、後で棚卸しして削る。最初から足さなければ、削る作業も要らない。削る基準は <!-- link:begin pruning-extensions#criteria -->[拡張の棚卸しと剪定 › 切る基準](pruning-extensions.md#criteria)<!-- link:end --> にある。

繰り返しを待ってから足す考え方には、立場に幅がある。

- **公式の立場**：公式の文書は、繰り返しをきっかけにして段階的に足す表を示している。
- **実践者の幅**：何も書かないところから始め、同じことを繰り返し言うようになってから足す、という助言がある（根拠：弱、実践者の助言）。一方で、日に何度もやる内側の作業は、早くからコマンドやスキルにする人もいる。また、作ったコマンドをほとんど使わなくなり、残ったのは 1 つだけだった、という報告もある（根拠：弱、単独の経験談）。
- **この辞典の推奨**：小さく始め、繰り返しが見えたものから足す。日に何度もやる作業は、見えるのが早いだけで、考え方は同じである。

## 足す前に見る強制力とコスト {#costs}

移す先を決める前に、その機能が何を保証し、どれだけ常駐するかを見る。下の表は、この辞典のデータから作ったものである。

<!-- gen:begin compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 強制力 | 読み込みの時期 | コンテキストのコスト | 圧縮で残るか |
| --- | --- | --- | --- | --- |
| [CLAUDE.md](what-to-put-in-claude-md.md) | お願い | セッション開始 | 常駐 | 残る |
| [出力スタイル（output styles）](../cli/output-style-modes.md) | お願い | セッション開始と切り替えたとき | 常駐 | 残る |
| [スキル（skills）](writing-skills.md) | お願い | セッション開始と使うとき | 使うまで小さい | 残る |
| [サブエージェント（subagents）](writing-subagents.md) | — | 起動したとき | 分離 | 未確認 |
| [MCP](connecting-mcp.md) | なし | セッション開始 | 使うまで小さい | 未確認 |
| [フック（hooks）](../enforce/hooks-basics.md) | 鍵 | イベントが起きたとき | ゼロ（出力を返さない限り） | 残る |
| [プラグイン（plugins）](plugins-and-marketplaces.md) | なし | セッション開始と使うとき | 使うまで小さい | 未確認 |

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->

表を読むときの注意は 2 つある。強制力が「お願い」の機能は、Claude が読んで判断するもので、守られる保証がない。強制力が「鍵」の機能だけが、Claude の判断に頼らず毎回実行される。もう 1 つは、コストの欄が「常駐」の機能は、足した分だけ毎回の費用が増えることである。値が「未確認」や空の欄は、公式の文書で確かめられていない（または、条件で変わる）ことを示す。

機能全体の比べ方は <!-- link:begin extensions-at-a-glance -->[拡張機能の全体図と使い分け早見表](extensions-at-a-glance.md)<!-- link:end --> にある。

## 判断例 {#examples}

!!! example "判断例：記事を読んで全部入れたくなったとき"
    - **状況**：拡張の紹介記事を読み、スキル・サブエージェント・フック・プラグインを一度に入れたくなっている。小さな個人のリポジトリで、実際に言い直しているのは、テストの実行コマンドだけである。
    - **迷う候補**：記事の構成をそのまま入れて整える。または、言い直している 1 点だけを CLAUDE.md に書いて様子を見る。
    - **選んだもの**：言い直している 1 点だけを CLAUDE.md に書く。
    - **理由**：言い直した内容に見合う仕組みだけがあればよい。ほかの拡張は、繰り返しが見えたときに足せる。入れた分の説明は、使わなくても常駐する。

!!! example "判断例：編集のたびにフォーマッタを頼んでいるとき"
    - **状況**：ファイルを編集させるたびに、「フォーマッタをかけて」と言い直している。
    - **迷う候補**：CLAUDE.md に「編集後にフォーマッタをかける」と書く。または、編集後に自動で走るフックにする。
    - **選んだもの**：フックにする。
    - **理由**：例外がなく、コマンドで機械的に実行できる。「毎回、必ず起きてほしい」ことは、公式の表でもフックの行に当たる。CLAUDE.md はお願いなので、書いても抜ける回がありうる。例外が多い、状況で判断が要る、という場合は CLAUDE.md に理由を書くほうが合う。分け方は <!-- link:begin when-to-lock#what-not-to-lock -->[お願いを鍵に移す判断 › 鍵にしない規則（判断を含むもの）](../enforce/when-to-lock.md#what-not-to-lock)<!-- link:end --> にある。

!!! example "判断例：大きな出力が会話を埋めるとき"
    - **状況**：テスト全体の実行や大きなログの調査をさせると、出力が会話を埋め、本題の作業が押される。
    - **迷う候補**：その作業の手順をスキルにする。または、サブエージェントに任せて、要約だけを返させる。
    - **選んだもの**：サブエージェントに任せる。
    - **理由**：困りごとは、手順を覚えさせることではなく、出力の量が本題の会話に入ることである。サブエージェントは別の文脈で動き、要約が戻る。ただし、余分なトークンはかかる。手順が長く、何度も繰り返すなら、スキルが合う場面もある。使いどころは <!-- link:begin writing-subagents#when-to-use -->[サブエージェントの作り方と使いどころ › 使いどころと、使わない場面](writing-subagents.md#when-to-use)<!-- link:end --> にある。

## 何に効くか {#effects}

このページの判断は、原理「見せる」と「縛る」の 2 つに関わる。

- **見せる（原因：見えていない）**：背景・規約・手順・外部のデータは、Claude に見えていなければ使われない。これを見える所に置くのが、CLAUDE.md・出力スタイル・スキル・MCP・code intelligence プラグインである。繰り返し言い直している内容は、Claude に見えていない内容のしるしである。
- **縛る（原因：縛っていない）**：頼んだだけの規則は、守られるかどうかが Claude の判断に残る。例外を許さないものは、フックや権限ルールに移して縛る。「毎回、必ず起きてほしい」が、その合図である。移す合図と移し先は <!-- link:begin when-to-lock#signals -->[お願いを鍵に移す判断 › 鍵に移す合図](../enforce/when-to-lock.md#signals)<!-- link:end --> と <!-- link:begin when-to-lock#where-to-move -->[お願いを鍵に移す判断 › 移し先の選び方](../enforce/when-to-lock.md#where-to-move)<!-- link:end --> にある。

公式ブログは、CLAUDE.md に「いつも Y をする」と書くならフックへ移すよう書く。「X を絶対にしない」は指示ではガードレールにならないので、フック・権限・管理設定へ移す。長い手順はスキルへ移す。後から直せる間違いは、繰り返しを見てから足せばよい。取り返しのつかない操作の禁止は、繰り返しを待たずに鍵を考える。

## 誤解 {#misconceptions}

- **誤解：拡張は多いほど Claude を使いこなせる**。足した分は、常駐する説明と管理の手間になる。使っていないものは外す。減らす順は <!-- link:begin always-on-costs#reduce -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 減らす順](../context/always-on-costs.md#reduce)<!-- link:end --> にある。
- **誤解：最初に CLAUDE.md を作り込めばよい**。推測できないコマンドや落とし穴だけを残す。構成の説明や、検査で確かめられる規約は外す。書く行と外す行は <!-- link:begin what-to-put-in-claude-md#what-to-leave-out -->[CLAUDE.md に書くこと・書かないこと › 書かないことと、移し先](what-to-put-in-claude-md.md#what-to-leave-out)<!-- link:end --> にある。
- **誤解：繰り返しが見えたら、まずプラグインにする**。プラグインは、スキルやフックなどを束ねて配る単位である。足す目安は、2 つ目のリポジトリや、ほかの人にも同じ設定が要るときである。入れる前の確認は <!-- link:begin plugins-and-marketplaces#before-install -->[プラグインとマーケットプレイス › 入れる前の確認](plugins-and-marketplaces.md#before-install)<!-- link:end --> にある。共有する拡張は、複数の人が使うものに絞る（根拠：中、実務の一致）。
- **誤解：回数さえ守れば、判断は要らない**。表の回数は目安である。同じ内容でも、守られなくても取り返せるか、例外なく毎回必要かで、移す先は変わる。
- **誤解：古い記事のカスタムコマンドは、別の拡張として足す**。カスタムコマンドは、今はスキルにまとめられている。記事の「コマンドにする」は、スキルにすると読み替える。
- **誤解：足したら終わり**。足した後は、使っているかを見て削る。移した後に削り、足すのは繰り返しが見えてからにする流れは <!-- link:begin repeating-the-same-explanation#prevention -->[毎回同じ説明をしている › 予防：移した後に削り、足すのは繰り返しが見えてから](../symptoms/repeating-the-same-explanation.md#prevention)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Claude Code を拡張する](https://code.claude.com/docs/ja/features-overview)：Anthropic・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents](https://claude.com/resources/articles/steering-claude-code-skills-hooks-rules-subagents-and-more)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**関連**

- [拡張機能の全体図と使い分け早見表](extensions-at-a-glance.md)
- [CLAUDE.md・rules・スキル・出力スタイルの違い](claude-md-vs-rules-skills-styles.md)
- [お願いを鍵に移す判断](../enforce/when-to-lock.md)
- [毎回同じ説明をしている](../symptoms/repeating-the-same-explanation.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [CLAUDE.md に書くこと・書かないこと](what-to-put-in-claude-md.md)
- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)
- [サブエージェントの作り方と使いどころ](writing-subagents.md)
- [MCP をつなぐ](connecting-mcp.md)
- [code intelligence プラグイン（LSP）](code-intelligence-plugins.md)
- [プラグインとマーケットプレイス](plugins-and-marketplaces.md)
- [フックの考え方とイベント](../enforce/hooks-basics.md)
- [出力スタイルで応答の仕方を切り替える](../cli/output-style-modes.md)
- [拡張の棚卸しと剪定](pruning-extensions.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
