---
id: choosing-mcp-servers
title: MCP サーバーの選び方
aliases: [よく使われる MCP, MCP の入れすぎ]
type: feature
field: extend
chapter: MCP
order: 200
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない, 境界がない]
pitfalls: []
scenes: [開発, 調べもの]
summary: どの MCP サーバーを入れるかを、足りない能力・提供元・権限・コンテキストのコストで判断できる。よく使われる種類を例に、入れすぎない基準を持つ。
signs:
  - {type: goal, text: 見つけた MCP サーバーを、入れる価値があるか見極めたい}
  - {type: goal, text: どの外部ツールをつなぐと効果があるか知りたい}
prerequisites: [connecting-mcp]
related: [mcp-or-cli, vetting-extensions, uses-nonexistent-apis, visual-checks, browser-control, lethal-trifecta, pruning-extensions, always-on-costs]
tracks: [mcp]
sources: [cc-docs-mcp, cc-docs-security, cc-docs-sandboxing, cc-docs-features-overview, composio-content-best-mcp-servers-code, marmelab-code-tips-wish-id-had]
volatility: 高
sections:
  - {title: 4 つの問いで見極める, anchor: questions}
  - {title: 足りない能力があるか, anchor: gap}
  - {title: よく使われる種類の例, anchor: examples}
  - {title: 提供元を見る, anchor: provider}
  - {title: 権限を絞る, anchor: permissions}
  - {title: コンテキストのコストを見る, anchor: cost}
  - {title: 判断例, anchor: example}
  - {title: 入れすぎない進め方, anchor: keep-small}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：見つけた MCP サーバーを、足りない能力・提供元・権限・コンテキストのコストの 4 つの問いで見極め、入れる価値があるものだけを入れられる。
    - **いつ引くか**：見つけた MCP サーバーを、入れる価値があるか見極めたいとき。どの外部ツールをつなぐと効果があるか知りたいとき。
    - **強制力**：<!-- gen:begin feature enforcement -->なし<!-- gen:end feature enforcement -->。サーバーを選ぶ基準の話で、何も止めない。入れたサーバーは利用者の権限で動くので、止めるのは資格情報の権限と権限ルールの側である。成熟度は <!-- gen:begin feature maturity -->GA<!-- gen:end feature maturity -->、読み込みの時期は <!-- gen:begin feature load_timing -->セッション開始<!-- gen:end feature load_timing --> である。
    - **前提**：<!-- link:begin connecting-mcp -->[MCP をつなぐ](connecting-mcp.md)<!-- link:end -->

<!-- textlint-disable -->
別名：よく使われる MCP・MCP の入れすぎ
<!-- textlint-enable -->

MCP サーバーの選び方とは、足せる MCP サーバーの中から、入れるものと入れないものを決める基準のことである。MCP のつなぎ方そのものは別のページに任せ、このページは「つなぐ前に何を見るか」だけを扱う。見つけたサーバーはどれも便利そうに見えるので、基準がないと入れすぎる。

## 4 つの問いで見極める {#questions}

入れるかどうかは、次の 4 つの問いに順に答えて決める。1 つでも答えられなければ、まだ入れない。

1. **足りない能力**：Claude にいま見えていないものは何か。それはサーバーなしで補えないか。[足りない能力があるか](#gap)の節で扱う。
2. **提供元**：誰が作り、誰が保守しているか。[提供元を見る](#provider)の節で扱う。
3. **権限**：どの資格情報で動き、何を読み、何を書き、どこへ送れるか。[権限を絞る](#permissions)の節で扱う。
4. **コンテキストのコスト**：入れたぶんだけ、毎回の文脈に何が増えるか。[コンテキストのコストを見る](#cost)の節で扱う。

この順にするのは、前の問いほど安く確かめられ、後の問いほど入れた後の負担が重いからである。1 問目は紙の上で答えられるが、4 問目は入れて使ってみないと実感できない。

入れるサーバーは、Claude に外のものを見せる（原理「見せる」）ために足す。ただし、足すほど Claude が触れる範囲は利用者の権限のまま広がり、境界がなくなっていく。つなぎ方と、その前に決めること（共有の範囲・資格情報）は「<!-- link:begin connecting-mcp#use -->[MCP をつなぐ › 何を任せて、何を先に決めるか](connecting-mcp.md#use)<!-- link:end -->」にある。入れる前の出所と中身の確かめは、安全の側のページが持つ。この節では、確かめる前に「入れる価値があるか」を絞る。

## 足りない能力があるか {#gap}

最初に、Claude にいま見えていないものを 1 文で言えるかを確かめる。「便利そうだから」は理由にならない。言えるのは、たとえば次のような場合である。

- ブラウザの画面やチケットの内容を、毎回コピーして貼っている。手作業で補っている部分が、そのまま足りない能力である。
- 古い、または存在しない関数や引数を使われる。ライブラリの文書が Claude に見えていないことが原因なら、文書を読ませる手が候補になる。原因の切り分けは「<!-- link:begin uses-nonexistent-apis#diagnosis -->[存在しない関数やパッケージを使う › 原因を安く確かめる順](../symptoms/uses-nonexistent-apis.md#diagnosis)<!-- link:end -->」にある。
- 画面を持つ成果物を、人が使うのと同じように確かめさせたい。使いどころは「<!-- link:begin visual-checks#when -->[画面で確かめる（ブラウザ・スクリーンショット・/verify） › 使いどころ](../verify/visual-checks.md#when)<!-- link:end -->」にある。

言えたら、次に、サーバーなしで済まないかを確かめる。成熟した CLI があれば、CLI とスキルのほうがコンテキストの効率がよい。CLI がないときや、権限を狭く絞りたいときに MCP が生きる。選び方は「<!-- link:begin mcp-or-cli#how-to-choose -->[MCP か CLI か › 選び方](mcp-or-cli.md#how-to-choose)<!-- link:end -->」にある。ブラウザや画面の操作には専用の手段があり、順番は「<!-- link:begin browser-control#which-to-use -->[Claude in Chrome と computer use（ブラウザと画面の操作） › コネクタ・ブラウザ・画面の順に選ぶ](../surfaces/browser-control.md#which-to-use)<!-- link:end -->」にある。

## よく使われる種類の例 {#examples}

よく挙がる MCP サーバーを、埋める能力ごとに並べる。名前は、種類をつかむための例である。推薦ではなく、評価もしない。

| 埋める能力 | 例の名前 |
| --- | --- |
| ブラウザの操作と画面の確かめ | Playwright MCP、Chrome DevTools MCP |
| バージョンに合ったライブラリの文書 | Context7 |
| 課題管理・文書・チャット | Linear、Jira、Notion、Slack、Google Workspace |
| エラー監視 | Sentry |
| デザイン | Figma |
| データベース・クラウド | PostgreSQL・SQLite・MySQL、Supabase、Neon、Vercel、Cloudflare |

この一覧は、2026-06-29 の実践者の記事（[Best MCP servers for Claude Code and Codex I'm using in 2026](https://composio.dev/content/best-mcp-servers-claude-code-codex)）などに挙がっていた名前を写したものである（根拠：弱。記事の一覧で、効果の測定ではない）。各サーバーの成熟度は未確認である。この表の日付は記事の日付であり、この辞典が各サーバーの存在や保守を確かめた日ではない。サーバーの名前は変わりやすいので、入れる前に、最新の提供元のページで確かめる。

人気のあるサーバーは、有力な候補にはなる。ただし、自分の環境で足りない能力を埋めるかは別の問いで、人気はその答えにならない。

## 提供元を見る {#provider}

Anthropic は、コネクタを Anthropic Directory に載せる前に掲載基準で審査する。一方で、MCP サーバーそのものの監査や管理は、どのサーバーについても行っていない。公式は、自分で書いたサーバーか、信頼できる提供元のサーバーを使うよう勧めている（[Claude Code Security](https://code.claude.com/docs/en/security)）。

見極めでは、まず次の 2 つを確かめる。

- 提供元と保守の様子が分かるか。分からないサーバーは、能力が魅力的でも後回しにする。
- 入れた後の自分の環境に、何が読み込まれるかを把握できるか。`.mcp.json` を見ただけでは、セッションが読み込むサーバーの全体は分からない。ほかのスコープの設定、claude.ai のコネクタ、プラグインも、サーバーを足しうる。

出所と中身を読んで確かめる手順は、このページでは繰り返さない。「<!-- link:begin vetting-extensions#provenance -->[MCP・プラグイン・スキルを入れる前の確認 › 出所を確かめる](../safety/vetting-extensions.md#provenance)<!-- link:end -->」と「<!-- link:begin vetting-extensions#read-contents -->[MCP・プラグイン・スキルを入れる前の確認 › 中身を読む（道具の説明・フック・スクリプト）](../safety/vetting-extensions.md#read-contents)<!-- link:end -->」にある。承認した後に定義が差し替わる場合は「<!-- link:begin vetting-extensions#changes-after-install -->[MCP・プラグイン・スキルを入れる前の確認 › 入れた後に変わる（rug pull）](../safety/vetting-extensions.md#changes-after-install)<!-- link:end -->」にある。

## 権限を絞る {#permissions}

入れたサーバーは、利用者の権限で動く。読んだ内容は Claude の入力になり、書き込みや外への送信ができる道具も、同じ権限で使える。サーバーを選ぶときは、能力の大きさより先に、必要な権限の小ささを見る。

- **資格情報は読み取り専用から始める**。書き込みの必要が出たら、そのとき広げる。詳しくは「<!-- link:begin connecting-mcp#credentials -->[MCP をつなぐ › 資格情報と権限](connecting-mcp.md#credentials)<!-- link:end -->」にある。
- **サンドボックスを守りと数えない**。サンドボックスが囲うのは、Bash などのシェルコマンドだけで、MCP サーバーには及ばない（[Sandboxing](https://code.claude.com/docs/en/sandboxing)）。
- **3 つを同時に持たせない**。信頼できない入力を読む道具、秘密や私的なデータを読む道具、外へ送る道具が 1 つの構成にそろうと、仕込まれた指示が被害につながる。候補のサーバーを足すと 3 つがそろわないかを確かめる。考え方は「<!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](../safety/lethal-trifecta.md#three-capabilities)<!-- link:end -->」にある。3 つとも要る作業には、人の承認を挟む。

守りを先に整えてから、サーバーを足す。順序を逆にして、入れた後に権限を絞ろうとすると、すでに読まれた内容は戻せない。

## コンテキストのコストを見る {#cost}

サーバーを入れると、コンテキストにも負担が乗る。MCP のコンテキストのコストの分類は「<!-- gen:begin feature context_cost -->使うまで小さい<!-- gen:end feature context_cost -->」である。セッションの開始時に入るのは道具の名前とサーバーの指示だけで、JSON のスキーマは使うときまで遅らされる。ツール検索は既定で有効だが、Microsoft Foundry の Azure の配置などでは使えない（[Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)）。

それでも、サーバーを足すほど、名前の一覧は長くなる。ツール検索でどこまで消費が減るかは、確かめられていない。判断の目安は、実践者の見解（根拠：弱）にある次の 1 文である。判断を良くする以上にコンテキストを膨らませるなら、そのサーバーは切る（[Composio](https://composio.dev/content/best-mcp-servers-claude-code-codex)）。道具は、多すぎるより、よく選んだ少数のほうがよいという指摘もある（[marmelab](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)）。

「何個まで」という数の目安と、「トークンを何割減らせる」という効果の数字は、この辞典の基準にしない。前者は環境で変わる。後者は自己申告で、測り方が示されないものが多い。基準にするのは、自分の環境で測った費用である。常駐するものの費用の見方は「<!-- link:begin always-on-costs#resident-vs-on-demand -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 常駐するものと、使うときだけ読むもの](../context/always-on-costs.md#resident-vs-on-demand)<!-- link:end -->」に、測り方は「<!-- link:begin pruning-extensions#measure -->[拡張の棚卸しと剪定 › 測る](pruning-extensions.md#measure)<!-- link:end -->」にある。

## 判断例 {#example}

!!! example "判断例：画面の確認用のサーバーを見つけた"
    - **状況**：開発中の画面を Claude に確かめさせたい。ブラウザを操作できる MCP サーバーの記事を見つけた。
    - **迷う候補**：その場でサーバーを入れる。または、いまある手段で足りるかを先に試す。
    - **選んだもの**：先に、いまある手段で足りるかを試す。足りない点を 1 文で言えたら、4 つの問いに答えて入れる。
    - **理由**：画面の確かめは、すでにある手段で済む場合がある。足りない点が言えないうちに入れると、能力の重なるサーバーが増えるだけになる。
      手段の選び方は「<!-- link:begin visual-checks#as-a-user -->[画面で確かめる（ブラウザ・スクリーンショット・/verify） › 人のユーザーとして確かめさせる](../verify/visual-checks.md#as-a-user)<!-- link:end -->」と「<!-- link:begin browser-control#which-to-use -->[Claude in Chrome と computer use（ブラウザと画面の操作） › コネクタ・ブラウザ・画面の順に選ぶ](../surfaces/browser-control.md#which-to-use)<!-- link:end -->」にある。

## 入れすぎない進め方 {#keep-small}

入れすぎを防ぐには、入れるときに外す条件も決めておく。

1. **1 つずつ入れる**。複数をまとめて入れると、どれが役に立ち、どれが負担かが分からない。
2. **入れる前に、補う能力と外す条件を 1 文ずつ書く**。下の依頼の雛形で、Claude に表の形で埋めさせられる。
3. **つながりを確かめる**。つなぎ方と確かめ方は「<!-- link:begin connecting-mcp#minimal -->[MCP をつなぐ › 最小のつなぎ方](connecting-mcp.md#minimal)<!-- link:end -->」にある。
4. **使わなかったものを外す**。外す基準と手順は「<!-- link:begin pruning-extensions#criteria -->[拡張の棚卸しと剪定 › 切る基準](pruning-extensions.md#criteria)<!-- link:end -->」と「<!-- link:begin pruning-extensions#cut -->[拡張の棚卸しと剪定 › 切る手順](pruning-extensions.md#cut)<!-- link:end -->」にある。
5. **共有の設定に入れるのは、複数の人が使うものだけにする**。共有の範囲の決め方は「<!-- link:begin connecting-mcp#scopes -->[MCP をつなぐ › スコープと共有](connecting-mcp.md#scopes)<!-- link:end -->」にある。

<!-- gen:begin snippet choosing-mcp-servers/vet-candidate -->
<!-- textlint-disable -->

??? example "雛形：入れる前に見極めさせる依頼"

    ```markdown
    見つけた MCP サーバーを、入れる前に見極めたい。サーバーは入れず、設定ファイルも書き換えない。読んで答えるだけにしてほしい。

    【サーバーの README を貼る】

    【このサーバーで任せたい作業を 1 文で書く】

    次の 5 項目を表で答えてほしい。README に書かれていない項目は推測で埋めず、「不明」と書いて、何を見れば分かるかを添える。

    1. 補う能力：この作業で、いま Claude に見えていないものは何か。サーバーを入れずに済む手（CLI、すでに入れた道具、貼り付け）はあるか。
    2. 提供元：誰が作り、誰が保守しているか。README だけで確かめられないことは何か。
    3. 権限：動かすときに要る資格情報と、読み取り専用で足りるか。書き込みや外への送信ができる道具はあるか。
    4. コンテキストのコスト：道具はいくつか。使わないときも名前の一覧が増える分に見合うか。
    5. 外す条件：どうなったら外すか。

    最後に、「入れる」「入れない」「先に確かめる」のどれかを一言で勧め、その理由を 2 文までで書く。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet choosing-mcp-servers/vet-candidate -->

この依頼は、README だけを読ませる。README にないことを Claude は推測で埋めやすいので、雛形は「不明」と書かせる。表の答えを鵜呑みにせず、提供元と権限は自分で確かめる。

## 効かない場面と落とし穴 {#limits}

- **人気は価値ではない**。よく挙がるサーバーでも、自分の作業の不足を埋めるとは限らない。
- **4 つの問いは、入れる前の判断である**。入れた後にサーバーの中身が変わることもあるので、入れた後も確かめ続ける。変わる経路は「<!-- link:begin vetting-extensions#changes-after-install -->[MCP・プラグイン・スキルを入れる前の確認 › 入れた後に変わる（rug pull）](../safety/vetting-extensions.md#changes-after-install)<!-- link:end -->」にある。
- **効果の数字は当てにしない**。トークンの削減などの数字は、自己申告で測り方が分からないものを基準にしない。
- **一覧は古くなる**。[よく使われる種類の例](#examples)の名前は変わりやすい。名前ではなく、埋める能力で考える。
- **このページは Claude Code の CLI（WSL・Linux）が基準である**。ほかの OS や IDE 拡張での動きは未確認である。

## 比べる相手 {#compare}

- サーバーを入れるか、CLI で済ませるか：「<!-- link:begin mcp-or-cli#how-to-choose -->[MCP か CLI か › 選び方](mcp-or-cli.md#how-to-choose)<!-- link:end -->」
- 入れる前の出所と中身の確かめ：「<!-- link:begin vetting-extensions#checklist -->[MCP・プラグイン・スキルを入れる前の確認 › 全体の確かめ方](../safety/vetting-extensions.md#checklist)<!-- link:end -->」
- 入れたものの棚卸し：「<!-- link:begin pruning-extensions -->[拡張の棚卸しと剪定](pruning-extensions.md)<!-- link:end -->」
- つなぎ方と共有の範囲：「<!-- link:begin connecting-mcp -->[MCP をつなぐ](connecting-mcp.md)<!-- link:end -->」

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [MCP をつなぐ](connecting-mcp.md)

**関連**

- [MCP か CLI か](mcp-or-cli.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [存在しない関数やパッケージを使う](../symptoms/uses-nonexistent-apis.md)
- [画面で確かめる（ブラウザ・スクリーンショット・/verify）](../verify/visual-checks.md)
- [Claude in Chrome と computer use（ブラウザと画面の操作）](../surfaces/browser-control.md)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [拡張の棚卸しと剪定](pruning-extensions.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)：Anthropic・英語・確認日 2026-11-04
- [Security](https://code.claude.com/docs/en/security)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Best MCP servers for Claude Code and Codex I'm using in 2026](https://composio.dev/content/best-mcp-servers-claude-code-codex)：Composio・英語・確認日 2026-11-04
- [Claude Code Tips I Wish I’d Had From Day One](https://marmelab.com/blog/2026/04/24/claude-code-tips-i-wish-id-had-from-day-one.html)：marmelab・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
