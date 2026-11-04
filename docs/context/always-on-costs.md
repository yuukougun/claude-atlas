---
id: always-on-costs
title: 常駐するもののコスト（CLAUDE.md・MCP・スキル）
aliases: [常駐するもののコスト（CLAUDE.md・MCP・skills）, listing tax, 常駐するコンテキスト, 起動時に読み込まれるもの, MCP を入れすぎると重い]
type: concept
field: context
chapter: 見る・絞る
order: 110
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: CLAUDE.md の全文・スキルの説明・MCP のツールの一覧など、毎回のリクエストに乗るものの費用が分かり、必要なときだけ読ませる形に移せる。溢れの心配より、焦点と費用のために常駐を小さく保つ。
signs:
  - {type: goal, text: MCP や skill をどこまで入れてよいか知りたい}
prerequisites: [rereads-whole-history]
related: [inspect-context, pruning-extensions, too-slow, extensions-at-a-glance, claude-md-length, path-scoped-rules, how-skills-load, connecting-mcp, mcp-or-cli, vetting-extensions, why-prompt-caching, what-uses-up-limits, choose-what-to-read]
tracks: [claude-md, skills, mcp, context-window]
outdated_advice: []
sources: [cc-docs-features-overview, cc-docs-context-window, cc-docs-memory, cc-docs-skills, cc-docs-mcp, cc-docs-large-codebases, cc-docs-how-claude-code-works, cc-docs-best-practices]
volatility: 中
sections:
  - {title: 常駐するものと、使うときだけ読むもの, anchor: resident-vs-on-demand}
  - {title: なぜ常駐を小さく保つのか, anchor: why-small}
  - {title: 何に効くか（原理と原因）, anchor: effect}
  - {title: 減らす順, anchor: reduce}
  - {title: 誤解と、移すときの落とし穴, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：毎回のリクエストに乗るもの（CLAUDE.md の全文・スキルの説明・MCP のツールの一覧）の費用が分かり、必要なときだけ読ませる形に移せる。
    - **いつ引くか**：MCP やスキルをどこまで入れてよいか知りたいとき。
    - **結論**：常駐を小さく保つ理由は、窓が溢れるからではなく、毎回送られる量の費用と、関係のない指示が焦点をぼかすことにある。
    - **前提**：<!-- link:begin rereads-whole-history -->[毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)<!-- link:end -->

<!-- textlint-disable -->
別名：常駐するもののコスト（CLAUDE.md・MCP・skills）・listing tax・常駐するコンテキスト・起動時に読み込まれるもの・MCP を入れすぎると重い
<!-- textlint-enable -->

常駐するもののコストとは、Claude Code がセッションの開始から毎回のリクエストに載せ続けるものが、使われなくても場所と費用を取ることをいう。このページは、何が常駐して何が使うときだけ読まれるかを分け、常駐を小さく保つ理由と、減らす順を示す。

## 常駐するものと、使うときだけ読むもの {#resident-vs-on-demand}

常駐するものは、セッションの開始から毎回のリクエストに乗り続ける。使うときだけ読むものは、呼ばれたときや関係するファイルに触れたときに、初めて入る。Claude は毎回、会話の最初から読み直して返事をするので、一度常駐に入れたものは、その後のターンのすべてで読み直される。

主な拡張の入り方は次のとおりである（Claude Code の話で、アプリのコネクタと API の MCP connector は別の仕組みなので、ここでは扱わない）。

- **CLAUDE.md**：読み込みの時期は <!-- gen:begin feature claude-md/load_timing -->セッション開始<!-- gen:end feature claude-md/load_timing -->、コストの分類は「<!-- gen:begin feature claude-md/context_cost -->常駐<!-- gen:end feature claude-md/context_cost -->」である。作業ディレクトリから上の階層の分は、全文が毎リクエストに乗る。サブディレクトリの CLAUDE.md は、Claude がそのディレクトリのファイルを読み書きしたときに入るので、使うときだけ読む側に近い。
- **スキル**：読み込みの時期は <!-- gen:begin feature skills/load_timing -->セッション開始と使うとき<!-- gen:end feature skills/load_timing -->、コストの分類は「<!-- gen:begin feature skills/context_cost -->使うまで小さい<!-- gen:end feature skills/context_cost -->」である。名前と説明がセッション開始から毎回入り、本体は呼ばれたときに入る。`disable-model-invocation: true` のスキルは、呼ぶまで何も入らない。
- **MCP**：読み込みの時期は <!-- gen:begin feature mcp/load_timing -->セッション開始<!-- gen:end feature mcp/load_timing -->、コストの分類は「<!-- gen:begin feature mcp/context_cost -->使うまで小さい<!-- gen:end feature mcp/context_cost -->」である。開始時に入るのはツールの名前とサーバーの指示だけで、JSON のスキーマは使うときまで遅らせる（ツール検索が既定で有効）。サーバーの指示が長ければ、それは常駐の分として残る。

ほかの拡張も、入り方で費用が分かれる。出力スタイルは毎リクエストに乗り、サブエージェントは本体のコンテキストから隔離され、フックは出力を返さない限りコンテキストを使わない。この分類は公式の Extend Claude Code に基づき、2026-10-29 に確かめた。全拡張を並べた比較は <!-- link:begin extensions-at-a-glance -->[拡張機能の全体図と使い分け早見表](../extend/extensions-at-a-glance.md)<!-- link:end --> にある。

ツール検索が使えない配置（公式は Microsoft Foundry の Azure の配置などを挙げる）は、MCP の入り方がここに書いたとおりにならない可能性がある。その場合の挙動は確かめていない。

## なぜ常駐を小さく保つのか {#why-small}

常駐を小さく保つ理由は 2 つあり、どちらも「窓が溢れるから」ではない。

1. **費用**：常駐するものは毎リクエストに乗るので、使わない日にも、毎ターンの入力の量に数えられる。会話の先頭が変わらなければ読み直しは安く済む（<!-- link:begin why-prompt-caching -->[プロンプトキャッシング（先頭が変わらないことの価値）](../basics/why-prompt-caching.md)<!-- link:end -->）が、安くなることと、窓や利用枠を占めないことは別である。利用枠を使う要因は <!-- link:begin what-uses-up-limits#causes -->[上限を早く使う要因 › 枠を早く減らす原因](../cost/what-uses-up-limits.md#causes)<!-- link:end --> にまとまっている。
2. **焦点**：公式の Large codebases は、大きなコードベースで関係のない指示や読み込みが窓を埋めると、トークンを使い性能も落ちると書く。今の作業と関係のない指示やツールの説明が並ぶと、Claude はそれも読んだうえで答えるので、本来効かせたい指示の比重が下がる。

「溢れさせないための節約」という見方は、古くなりつつある。2026-11-03 に確かめた現行の Best practices は、「コンテキストの窓が主な制約なので積極的に管理せよ」という助言を、やめてよいことの表に挙げる。窓が埋まる前の自動の圧縮が既定で働くので、整頓の目的は質と費用に移った。

## 何に効くか（原理と原因） {#effect}

常駐を小さくすることは、原理「見せる」（Claude に何を見せるかが答えを決める）を、毎回の土台の部分で実践することにあたる。毎回見える部分に置くのは、どの作業でも見せたいものだけにし、残りは必要な作業のときだけ見せる。

防ぐ原因は 2 つある。

- **散らかっている**：使っていない MCP のツールの一覧や、昔の作業の手順が常駐に残り、今の作業に要る情報を押しのける。常駐から外すと、今の作業に関係するものだけが机に残る（広い机＝コンテキストの比喩）。
- **合っていない**：別のプロジェクトの規約や、直し終えた不具合の注意が CLAUDE.md に残ると、今の作業に合わない指示として効く。使うときだけ読む形に移せば、合う作業のときだけ効く。

## 減らす順 {#reduce}

常駐を減らす順は、失うものが少なく戻しやすいものから進める、というのがこの辞典の推奨である。公式が順番を定めているわけではない。

1. **測る**：起動直後の /context の値を控え、何が常駐の分を占めているかを見る。読み方と基準値は <!-- link:begin inspect-context#baseline -->[/context で中身を見る › 起動直後の基準値](inspect-context.md#baseline)<!-- link:end -->、棚卸し全体の測り方は <!-- link:begin pruning-extensions#measure -->[拡張の棚卸しと剪定 › 測る](../extend/pruning-extensions.md#measure)<!-- link:end --> にある。
2. **使っていないものを外す**：使っていない MCP サーバーとスキルを外す。入れ直すのは簡単で、失うものがほぼない。外すかの基準は <!-- link:begin pruning-extensions#criteria -->[拡張の棚卸しと剪定 › 切る基準](../extend/pruning-extensions.md#criteria)<!-- link:end -->、つなぎ方は <!-- link:begin connecting-mcp -->[MCP をつなぐ](../extend/connecting-mcp.md)<!-- link:end --> にある。
3. **MCP を CLI で置き換えられるか見る**：成熟した CLI があれば、CLI とスキルのほうがコンテキストの効率がよいとする実務家の声が多い（根拠：中）。選び方は <!-- link:begin mcp-or-cli -->[MCP か CLI か](../extend/mcp-or-cli.md)<!-- link:end --> にある。
4. **長い手順をスキルへ移す**：特定の作業でしか使わない長い手順は、説明だけを常駐させ、本体を呼ばれたときに読ませる。仕組みは <!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)<!-- link:end --> にある。
5. **特定のフォルダ向けの規約を絞る**：そのフォルダのファイルに触れたときだけ読ませる。やり方は <!-- link:begin path-scoped-rules -->[.claude/rules と paths で必要なときだけ読ませる](../extend/path-scoped-rules.md)<!-- link:end --> にある。
6. **CLAUDE.md の行を削る**：「消したら誤りが出るか」で残す行を選ぶ。問いは <!-- link:begin claude-md-length#deletion-test -->[CLAUDE.md の長さと剪定 › 削るときの問い](../extend/claude-md-length.md#deletion-test)<!-- link:end -->、/init の叩き台なら <!-- link:begin claude-md-length#init-draft -->[CLAUDE.md の長さと剪定 › /init の叩き台を削る](../extend/claude-md-length.md#init-draft)<!-- link:end --> を使う。
7. **機械的に守らせたいことはフックか設定へ**：例外を許さない禁止は、CLAUDE.md に長く書かず、権限の設定かフックで強制し、CLAUDE.md には理由と相談の基準だけを残す。

外したら、同じ依頼で結果が変わらないかを確かめる。変わったなら、外したものは常駐に戻す。

!!! example "判断例：MCP をどこまで入れるか"
    - **状況**：ブラウザの操作・データベース・チケット管理の MCP サーバーを一通りつないだところ、起動直後の常駐の分が大きくなり、返事も重く感じる。
    - **迷う候補**：すべて残して、使うときのために備える。あるいは、日常の作業で使うものだけ残して、ほかは外す。
    - **選んだもの**：日常の作業で毎週使うものだけ残し、使う頻度の低いものは外して、必要な作業の直前につなぎ直す。
    - **理由**：外したものは、つなぎ直せば使えるので失うものが少ない。残すと、使わない日にも毎リクエストの費用と、焦点をぼかす影響を払い続ける。外してよいかは、まず /context で占める分を見て決める。

## 誤解と、移すときの落とし穴 {#misconceptions}

- **「常駐は悪で、ゼロにするのがよい」ではない**。毎回効かせたい規約や、守りの前提は常駐に置くものである。公式の How Claude Code works は、自動の圧縮で会話の初めの指示が失われうるので、続けて守らせる規則は CLAUDE.md に置くよう勧める。減らす対象は「毎回は要らないもの」である。
- **「スキルや MCP は入れても無料」ではない**。スキルは説明だけ、MCP はツールの名前とサーバーの指示だけでも、数が増えれば常駐の分は増える。入れすぎたときに残るコストは <!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)<!-- link:end --> にもある。
- **「使うときだけ読む形に移せば、いつでも効く」ではない**。フォルダ向けの規約やスキルの本体は、会話が圧縮された後、戻る時期が常駐のものと違う。<!-- link:begin path-scoped-rules#after-compaction -->[.claude/rules と paths で必要なときだけ読ませる › 圧縮の後に戻る時期](../extend/path-scoped-rules.md#after-compaction)<!-- link:end --> と <!-- link:begin how-skills-load#after-compaction -->[スキルの考え方（手順を必要なときだけ読む） › 圧縮の後に戻るもの](../extend/how-skills-load.md#after-compaction)<!-- link:end --> で確かめる。必ず効かせたい規約を移してしまわない。
- **「CLAUDE.md の強調で守らせる」は常駐を増やすだけ**。強調しても守られない行は、ファイルを短くするか、強制できる仕組みに移す。
- **入れる前の確認は別に要る**。MCP やスキルは、利用者の権限で動く。常駐の費用の話と別に、出所と中身の確認が要るので、<!-- link:begin vetting-extensions -->[MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)<!-- link:end --> で確かめてから入れる。

返事が遅く感じる症状から入る場合は、<!-- link:begin too-slow#diagnosis -->[返事が遅い・時間がかかりすぎる › 原因を安く確かめる順](../symptoms/too-slow.md#diagnosis)<!-- link:end --> で、常駐以外の原因（effort・モデル・会話の長さ）も安く確かめられる。長い出力や読み込みを絞る話は <!-- link:begin choose-what-to-read -->[@参照と、何を読ませるかの絞り込み](choose-what-to-read.md)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [How Claude remembers your project](https://code.claude.com/docs/en/memory)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)：Anthropic・英語・確認日 2026-11-04
- [Set up Claude Code in a monorepo or large codebase](https://code.claude.com/docs/en/large-codebases)：Anthropic・英語・確認日 2026-11-04
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)

**次に読む**

- [CLAUDE.md の長さと剪定](../extend/claude-md-length.md)
- [拡張の棚卸しと剪定](../extend/pruning-extensions.md)

**関連**

- [/context で中身を見る](inspect-context.md)
- [返事が遅い・時間がかかりすぎる](../symptoms/too-slow.md)
- [拡張機能の全体図と使い分け早見表](../extend/extensions-at-a-glance.md)
- [.claude/rules と paths で必要なときだけ読ませる](../extend/path-scoped-rules.md)
- [スキルの考え方（手順を必要なときだけ読む）](../extend/how-skills-load.md)
- [MCP をつなぐ](../extend/connecting-mcp.md)
- [MCP か CLI か](../extend/mcp-or-cli.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [プロンプトキャッシング（先頭が変わらないことの価値）](../basics/why-prompt-caching.md)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)
- [@参照と、何を読ませるかの絞り込み](choose-what-to-read.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
