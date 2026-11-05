---
id: choose-what-to-read
title: '@参照と、何を読ませるかの絞り込み'
aliases: ['@ でファイルを指定する', 読ませるファイルを絞る, 長いコマンド出力を絞る]
type: concept
field: context
chapter: 見る・絞る
order: 120
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発, データ分析]
summary: 読むべきファイルを @ で直接指し、テストやログの長い出力は要点の数行に絞ってから会話に入れる。探させる手間と、関係のない読み込みが答えをぼかすことの両方を減らせる。
signs:
  - {type: goal, text: 読ませるファイルを自分で指定したい}
  - {type: situation, text: 大きなコードベースで作業している}
prerequisites: [context-rot]
related: [input-symbols, handing-long-documents, research-in-subagents, inspect-context, hook-recipes, explore-a-codebase, code-intelligence-plugins, four-specifics, mcp-or-cli, protecting-secrets]
tracks: [context-window]
outdated_advice: []
sources: [cc-docs-common-workflows, cc-docs-large-codebases, cc-docs-interactive-mode, cc-docs-context-window, anthropic-eng-building-c-compiler]
volatility: 中
sections:
  - {title: 直接指すか、探させるか, anchor: point-or-search}
  - {title: 出力を絞る, anchor: trim-output}
  - {title: 何に効くか, anchor: effects}
  - {title: '@ 参照の注意', anchor: caveats}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：読ませたいファイルは @ で直接指し、長い出力は数行に絞って渡す理由と、その使い分け。
    - **いつ引くか**：読ませるファイルを自分で指定したいとき。大きなコードベースで、関係のない読み込みが増えてきたとき。
    - **前提**：<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end -->

<!-- textlint-disable -->
別名：@ でファイルを指定する・読ませるファイルを絞る・長いコマンド出力を絞る
<!-- textlint-enable -->

@参照と、何を読ませるかの絞り込みは、広い机に置く資料を、依頼する側が選ぶ技法である。読むべきファイルは @ で名指しし、テストやログの長い出力は要点だけを会話に入れる。Claude に探させる手間と、関係のない読み込みが答えをぼかすことの、両方を減らせる。

## 直接指すか、探させるか {#point-or-search}

読むファイルが分かっているなら、探させずに @ で直接指す。Claude Code では、`@src/auth/login.ts` のようにパスを書くと、そのファイルの内容が依頼と一緒に読み込まれる（根拠は公式の Common workflows。出典は末尾の参考）。ディレクトリを指したときは、中身ではなく一覧が入る。

Before と After を並べる。同じ不具合の依頼である。

```text
Before：ログインのバグを直して。

After：@src/auth/login.ts の login 関数で、空のパスワードが通ってしまう。
再現は @tests/auth/login.test.ts の「空のパスワード」のテスト。
直すのは login.ts だけにして、直したらそのテストを実行して。
```

After で足したのは 3 点である。直す対象のファイル、症状と再現の入口、終わりの確かめ方。対象・状況・完了を書く考え方は、<!-- link:begin four-specifics#target -->[具体性の 4 点（対象・状況・完了・手本） › 対象：どのファイル・どの画面か](../prompting/four-specifics.md#target)<!-- link:end --> にある。@ で指すのは、そのうちの「対象」を確実に渡す手段にあたる。

記号の打ち方と補完は <!-- link:begin input-symbols#at -->[入力の記号（/ ! @）と Esc › @ ファイルを直接指す](../cli/input-symbols.md#at)<!-- link:end --> にある。ここでは、指すか探させるかの選び方を扱う。

=== "アプリ"

    @ の記法は Claude Code の入力欄のものである。アプリでは、読ませたい資料だけを添付するか、必要な箇所だけを貼ることで、同じ「選んで渡す」を行う。添付の扱いの細部は、この辞典では未確認である。

=== "Claude Code"

    パスを @ で指す。補完でパスを選べる。MCP のリソースも `@server:resource` の形で指せる。

!!! example "判断例：バグの原因のファイルが分かっているか"
    - **状況**：ログイン処理で、空のパスワードが通る不具合を直したい。
    - **迷う候補**：原因のファイルを @ で指す。または、症状だけを伝えて、Claude に関連するコードを探させる。
    - **選んだもの**：原因が `login.ts` にあると分かっているので、@ で指す。分からないときは、探させる。
    - **理由**：分かっている対象は、直接渡したほうが探索の手間が省ける。分からない対象を無理に指すと、本当の原因のファイルが読まれずに、的外れな修正になる。探させる場合の進め方は <!-- link:begin explore-a-codebase#broad-to-narrow -->[知らないコードベースを読む › 広い質問から絞る](../recipes/explore-a-codebase.md#broad-to-narrow)<!-- link:end --> にある。

型のある言語では、言語サーバーに尋ねて定義へ飛ばせるので、総当たりで読む量が減る。その設定は <!-- link:begin code-intelligence-plugins -->[code intelligence プラグイン（LSP）](../extend/code-intelligence-plugins.md)<!-- link:end --> で扱う。

## 出力を絞る {#trim-output}

テストやビルドの長い出力は、要点の数行に絞ってから会話に入れる。読み込んだファイルやコマンドの出力は会話に残り、以後のターンでも読み直される。毎回、全履歴を読み直す受験者に、使わない長い出力まで持たせ続けることになる。

絞るのは、会話に入る前でなければ意味がない。Claude がコマンドを実行した時点で、出力の全文は会話に入っている。後から「要約して」と頼んでも、入った分は戻らない。そこで、実行の仕方を指定する。全文はファイルに書き出し、会話には件数と一覧だけを返させる。

<!-- gen:begin snippet choose-what-to-read/trim-test-output -->
<!-- textlint-disable -->

??? example "雛形：長いコマンド出力を絞って受け取る依頼"

    ```markdown
    <テストの実行コマンド> を実行して、失敗したテストを教えて。

    出力をそのまま会話に流さない。次の形で実行する。

    1. 出力の全文を `test.log` に書き出す（例：`<テストの実行コマンド> > test.log 2>&1`）。
    2. `test.log` から、失敗したテストの名前と、各テストの最初のエラー 1 行だけを取り出す。取り出しは `grep` などで行い、20 行までにする。
    3. 報告は、失敗の件数と、2 の一覧にする。

    原因の調べに全文が要るときは、`test.log` の該当箇所だけを読む。全文を読む前に、こちらに確認する。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet choose-what-to-read/trim-test-output -->

評価器やテストの出力を数行（件数、最悪の例、不一致の数など）に絞り、詳細はファイルに書く運用は、複数の実務家の報告で一致している（根拠：中）。Anthropic の C コンパイラの事例も、出力を数行に絞り、後から `grep` で引けるようにしている。

全文を捨てるわけではない。全文はファイルに残るので、原因の調べに要るときだけ、該当の箇所を読ませる。絞りすぎて原因の手がかりが消えたときは、絞る範囲を広げて、もう一度実行させる。

絞り込みを毎回の頼み方に頼らず、仕組みにする方法もある。テストの出力を絞るフックは <!-- link:begin hook-recipes#filter-test-output -->[代表的なフックのレシピ › テストの出力を絞る](../enforce/hook-recipes.md#filter-test-output)<!-- link:end --> にある。調査そのものが大量の出力を出すときは、絞るより、別の文脈で読ませる手がある。その線引きは <!-- link:begin research-in-subagents#when -->[出力の多い調査はサブエージェントに任せて要約だけ受け取る › 任せてよい調査、本筋で読むべきもの](research-in-subagents.md#when)<!-- link:end --> にある。

## 何に効くか {#effects}

この技法は、原理「見せる」に当たる。Claude に見せるものを、依頼する側が選ぶ。見せる量が少なければよいわけではなく、答えに要るものが見えていて、要らないものが混ざっていない状態をつくる。

防ぐ原因は 2 つある。

- **見えていない**：読むべきファイルが Claude の目に入っていない。@ で直接指すと、探索が外れても対象が確実に机に載る。
- **散らかっている**：関係のない読み込みや長い出力が机を埋めている。公式の Large codebases は、大きなコードベースで、関係のない指示や読み込みが窓を埋めると、トークンを使うだけでなく性能も落ちると述べている。絞った出力と選んだファイルは、この散らかりを減らす。

入力が長く、紛らわしい情報が混ざるほど答えの質が下がる仕組みは、<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end --> にある。中身が実際に何で埋まっているかは、<!-- link:begin inspect-context#reading -->[/context で中身を見る › 内訳の読み方](inspect-context.md#reading)<!-- link:end --> の内訳で見分けられる。

## @ 参照の注意 {#caveats}

@ 参照は便利だが、4 つの落とし穴がある。

- **指したファイルが全部読まれるとは限らない**：全文が入るのは、Read ツールの上限に収まる大きさのファイルまでである。上限を超えるファイルは、全文が入らない。上限は、<!-- fact:begin at-reference-read-limit -->25,000 トークン以内なら全文（256KB 超のテキストは含めない）（2026-11-06 時点）<!-- fact:end -->。値は版で変わりうる。大きなファイルは、読ませる範囲を行や関数で指定して頼む。
- **指しすぎは散らかりになる**：多くのファイルを念のために指すと、関係のない内容が机を埋める。指すのは、答えに要るファイルに絞る。
- **指さなかったファイルは、探されない保証がない**：指したファイルの外に原因があるときは、Claude が自分で探す。「このファイルだけで直して」と縛ったときは、ほかのファイルが要る場面で止めて確認させる。そのための文面は、この節の末尾の雛形の 2 段落目にある。
- **読ませたくないファイルは、@ では守れない**：@ 参照はツールの呼び出しを伴わないので、PreToolUse フックが走らない。フックで止めているつもりのパスも、@ で指されると読み込まれうる。読ませたくないパスは、`Read` の deny ルールで守る。設定は <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> にある。

読ませるファイルを指す依頼の雛形を、次に示す。山かっこの欄を埋めて使う。

<!-- gen:begin snippet choose-what-to-read/point-with-at -->
<!-- textlint-disable -->

??? example "雛形：読ませるファイルを @ で指す依頼"

    ```markdown
    @<直すファイル> の <関数名または処理名> で、<症状> が起きている。再現は @<テストファイル> の <テスト名> で確かめられる。

    直す対象は <直すファイル> だけにする。ほかのファイルを読む必要が出たら、読む前にファイル名と理由を挙げて、こちらの返事を待つ。

    直した後は、<テストの実行コマンド> を実行して、そのテストが通ることを確かめる。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet choose-what-to-read/point-with-at -->

長い資料を渡すときの分け方と変換は <!-- link:begin handing-long-documents#split-and-convert -->[長い資料を渡すとき › 分ける・形を直す](handing-long-documents.md#split-and-convert)<!-- link:end --> にある。MCP でつなぐか CLI で済ませるかによっても、会話に入る量は変わる。選び方は <!-- link:begin mcp-or-cli -->[MCP か CLI か](../extend/mcp-or-cli.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Common workflows](https://code.claude.com/docs/en/common-workflows)：Anthropic・英語・確認日 2026-11-04
- [Set up Claude Code in a monorepo or large codebase](https://code.claude.com/docs/en/large-codebases)：Anthropic・英語・確認日 2026-11-04
- [Interactive mode](https://code.claude.com/docs/en/interactive-mode)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/research/building-c-compiler)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [context rot と紛らわしい情報](../basics/context-rot.md)

**次に読む**

- [知らないコードベースを読む](../recipes/explore-a-codebase.md)

**関連**

- [入力の記号（/ ! @）と Esc](../cli/input-symbols.md)
- [長い資料を渡すとき](handing-long-documents.md)
- [出力の多い調査はサブエージェントに任せて要約だけ受け取る](research-in-subagents.md)
- [/context で中身を見る](inspect-context.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [code intelligence プラグイン（LSP）](../extend/code-intelligence-plugins.md)
- [具体性の 4 点（対象・状況・完了・手本）](../prompting/four-specifics.md)
- [MCP か CLI か](../extend/mcp-or-cli.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
