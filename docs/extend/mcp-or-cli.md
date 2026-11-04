---
id: mcp-or-cli
title: MCP か CLI か
aliases: [MCP と CLI の使い分け, MCP より CLI]
type: comparison
field: extend
chapter: MCP
order: 190
level: 任せる
priority: 必須
surfaces: [claude-code]
principle: [見せる]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: 外部ツールを MCP でつなぐか、CLI とスキルで済ませるかを選べる。成熟した CLI があればコンテキストの効率がよく、CLI がないときや権限を狭く絞りたいときに MCP が生きる。
signs:
  - {type: goal, text: 外部ツールをつなぐか、コマンドで済ませるかを決めたい}
  - {type: symptom, text: つないだツールの定義や出力で、コンテキストが埋まる}
prerequisites: [connecting-mcp]
related: [move-judgment-into-scripts, how-skills-load, always-on-costs, choosing-mcp-servers, permission-rules, lethal-trifecta, writing-skills]
tracks: [mcp, skills]
sources: [cc-docs-mcp, cc-docs-costs, cc-docs-features-overview, cc-docs-how-claude-code-works, composio-content-best-mcp-servers-code, simonwillison-agentic-coding, simonwillison-every-code-feature, simonwillison-designing-agentic-loops]
sections:
  - {title: 比較の表, anchor: table}
  - {title: 公式の立場・実践者の幅・この辞典の推奨, anchor: stances}
  - {title: 選び方, anchor: how-to-choose}
  - {title: 組み合わせ方, anchor: combine}
  - {title: 確かめ方, anchor: verify}
volatility: 中
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：成熟した CLI があって手順が決まっているなら CLI とスキル、CLI がない・認証つきの生の文脈が要る・権限を狭く絞りたいなら MCP、と選べる。
    - **いつ引くか**：外部ツールをつなぐか、コマンドで済ませるかを決めたいとき。つないだツールの定義や出力で、コンテキストが埋まるとき。
    - **前提**：<!-- link:begin connecting-mcp -->[MCP をつなぐ](connecting-mcp.md)<!-- link:end -->

<!-- textlint-disable -->
別名：MCP と CLI の使い分け・MCP より CLI
<!-- textlint-enable -->

MCP か CLI かは、Claude Code から外部のサービスを使うとき、MCP サーバーとしてつなぐか、シェルで既存のコマンドを実行させるかを選ぶ話である。どちらも筋の通る場面がある。選び誤ると、使わない定義や長い出力でコンテキストが散らかる。CLI のない相手を、無理に回り道して扱うこともある。このページの話は Claude Code に限る。Desktop アプリの MCP との関係は <!-- link:begin connecting-mcp#desktop -->[MCP をつなぐ › Desktop アプリの MCP との関係](connecting-mcp.md#desktop)<!-- link:end --> を見る。

## 比較の表 {#table}

MCP の属性を、データから作った表で見る。CLI は Claude Code の機能ではなく、シェルで動く既存のコマンドなので、表の行にはない。CLI を使わせるときは、コマンドの使い方を教えるスキルの説明文だけが常駐し、コマンドそのものは実行するまで何も載らない。実行した出力は会話に載る。

<!-- gen:begin compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->
<!-- textlint-disable -->

| 機能 | 強制力 | 読み込みの時期 | 圧縮で残るか |
| --- | --- | --- | --- |
| [MCP](connecting-mcp.md) | なし | セッション開始 | 未確認 |
| [スキル（skills）](writing-skills.md) | お願い | セッション開始と使うとき | 残る |

すべて共通：コンテキストのコスト 使うまで小さい。

<!-- textlint-enable -->
<!-- gen:end compare 強制力 読み込みの時期 コンテキストのコスト 圧縮で残るか -->

表のコンテキストのコストは、ツールの定義が載る分の見積もりである。MCP の出力は、定義とは別に会話へ載る。出力が大きすぎると警告が出て、既定の上限もある。常駐するものと、使うときだけ読むものの違いは <!-- link:begin always-on-costs#resident-vs-on-demand -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 常駐するものと、使うときだけ読むもの](../context/always-on-costs.md#resident-vs-on-demand)<!-- link:end --> にある。

## 公式の立場・実践者の幅・この辞典の推奨 {#stances}

実践者の間で意見が割れる論点なので、3 つに分けて書く。

- **公式の立場**：公式の文書は、`gh`・`aws`・`gcloud` のような CLI がある相手には、MCP より CLI のほうがコンテキストの効率がよいと案内している。接続は MCP、使い方の知識はスキルという組み合わせを勧めている。MCP は信頼できるサーバーだけにつなぎ、データベースには読み取り専用の資格情報を使い、使っていないサーバーは無効にする。
- **実践者の幅**（根拠：弱。個人の経験談とベンダーの記事）：シェルが使えるなら、スクリプトやコマンドを使わせるという立場が目立つ。Simon Willison は MCP の大半を自作のシェルスクリプトに置き換えた。一方で、安全なリソースへの制御されたアクセスには MCP の役割があるとも述べている。Composio（ベンダー記事）の基準は、成熟した CLI がある決まった作業は CLI とスキル、CLI がない・認証つきのライブな文脈が要る・シェル全体より狭い権限にしたいときは MCP である。サーバーを足すごとにツールとスキーマが増えるので、判断を良くする以上にコンテキストを膨らませるなら切る、という見方も重なる。
- **この辞典の推奨**（根拠：中。公式の案内と複数の実務家の一致）：先に、CLI とスキルで済まないかを考える。足りないときだけ MCP を足す。足す理由は 3 つに限る。CLI がない。認証つきのライブな文脈が要る。シェル全体より狭い権限にしたい。MCP を足したら、定義と出力の費用を測り、使わないものは外す。

ツール定義の遅延読み込みが入った後でも、CLI との差がどれだけ残るかは、確かめていない。だから CLI を優先する理由を、コンテキストの効率だけに置かない。手順を文章に決められること、出力を絞れること、足す物を増やさないことも、理由に数える。

## 選び方 {#how-to-choose}

次の順に問うと、選べる。

1. その相手に、成熟した CLI があるか。ないなら MCP を考える。決まった処理だけなら、書かせたスクリプトで足りることもある（<!-- link:begin move-judgment-into-scripts#what-to-move -->判断を決定論的なスクリプトに移す › 移す作業の見分け方（準備中）<!-- link:end -->）。
2. 作業の手順は決まっているか。決まっているなら、スキルに書いて CLI を呼ばせる。
3. 権限を、シェル全体より狭くしたいか。MCP は、サーバーが出すツールだけを渡せる。CLI は権限ルールで絞れるが、子プロセスには効かない点がある（<!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end -->）。
4. 認証つきのライブな状態を扱うか。ログイン済みのブラウザや、操作のたびに結果が変わる画面なら、MCP が合う。
5. どちらを選んでも、信頼できない入力・秘密のデータ・外への送信が同じ構成に揃っていないか。揃うなら、方式の選び方より先に構成を見直す（<!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](../safety/lethal-trifecta.md#three-capabilities)<!-- link:end -->）。

!!! example "判断例：GitHub の PR と CI を読ませる"
    - **状況**：PR の会話、issue、CI の失敗したログを Claude Code に読ませたい。
    - **迷う候補**：GitHub の MCP サーバーをつなぐ。または `gh` をシェルで実行させる。
    - **選んだもの**：`gh` とスキル。`gh` の使い方を教えるスキルの雛形は、組み合わせ方の節にある。
    - **理由**：`gh` は成熟した CLI で、サブコマンドが決まっていて、`--json` と `--jq` で出力を絞れる。MCP を足さないので、ツールの定義も増えない。書き込みは、スキルに「頼まれたときだけ」と書いて止める。

!!! example "判断例：分析用のデータベースを読ませる"
    - **状況**：分析用のデータベースの集計を、Claude Code に頼みたい。
    - **迷う候補**：データベースの CLI をシェルで実行させる。またはデータベースの MCP サーバーをつなぐ。
    - **選んだもの**：読み取り専用の資格情報を使った MCP サーバー。
    - **理由**：サーバーが出すツールだけを渡せるので、シェル全体を開けずに済む。資格情報はデータベース側で SELECT だけを許す。更新を止めるのはデータベースの権限であり、MCP を選んだことそのものではない。資格情報の作り方は <!-- link:begin connecting-mcp#credentials -->[MCP をつなぐ › 資格情報と権限](connecting-mcp.md#credentials)<!-- link:end --> を見る。

!!! example "判断例：ログイン済みのブラウザを操作させる"
    - **状況**：ログインが要る管理画面を、Claude Code に操作させて確かめたい。
    - **迷う候補**：画面操作のスクリプトを書かせて実行する。またはブラウザを操作する MCP サーバーをつなぐ。
    - **選んだもの**：ブラウザを操作する MCP サーバー。画面の操作が決まったテストになったら、その部分だけスクリプトに移す。
    - **理由**：認証つきのライブな状態を見ながら、操作ごとの結果を返す道具が要る。最初から手順を決められないので、スキルと CLI だけでは足りない。

どの MCP サーバーを入れるかは <!-- link:begin choosing-mcp-servers -->MCP サーバーの選び方（準備中）<!-- link:end --> で判断する。

## 組み合わせ方 {#combine}

方式を選んだら、何をどちらに置くかを決める。広げる前に、守りを先に置く。

- 資格情報は読み取り専用から始める（<!-- link:begin connecting-mcp#credentials -->[MCP をつなぐ › 資格情報と権限](connecting-mcp.md#credentials)<!-- link:end -->）。シェルで使わせるコマンドも、先に権限ルールで範囲を決める（<!-- link:begin permission-rules#when -->[権限ルール（allow・ask・deny） › 使いどころ](../enforce/permission-rules.md#when)<!-- link:end -->）。
- 信頼できない入力・秘密・外への送信の 3 つが揃うなら、人の承認を挟む（<!-- link:begin lethal-trifecta#when-all-three -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つとも要るとき](../safety/lethal-trifecta.md#when-all-three)<!-- link:end -->）。

そのうえで、役割を分ける。

- **MCP に置くもの**：接続、認証、ライブな文脈、狭い権限の窓口。
- **スキルに置くもの**：使い方の知識。どのツールをどの順で呼ぶか、出力をどう絞るか、書き込みは頼まれたときだけにするか、を書く。MCP でつないだものにも、CLI にも使える（<!-- link:begin writing-skills#minimal -->[スキルの作り方 › 最小のスキルを作る](writing-skills.md#minimal)<!-- link:end -->）。
- **CLI とスクリプトに置くもの**：毎回同じ結果を返す処理。長い手順は、スキルの補助ファイルやスクリプトへ分ける（<!-- link:begin writing-skills#supporting-files -->[スキルの作り方 › 補助ファイルとスクリプトに分ける](writing-skills.md#supporting-files)<!-- link:end -->）。

次の雛形は、MCP の代わりに `gh` の使い方を教えるスキルの例である。

<!-- gen:begin snippet mcp-or-cli/gh-cli-skill -->
<!-- textlint-disable -->

??? example "雛形：.claude/skills/github-cli/SKILL.md（MCP の代わりに gh の使い方を教えるスキル）"

    ```markdown
    ---
    name: github-cli
    description: PR・issue・CI の状況を調べるとき、GitHub の MCP ではなく gh コマンドで読む。書き込み（マージ・クローズ・コメント）は、人が頼んだときだけ行う
    ---

    # gh で GitHub の状況を調べる

    GitHub の情報は、`gh` をシェルで実行して読む。出力は必要な分だけに絞る。

    1. PR の概要と会話は `gh pr view <番号> --comments` で読む。CI の状態は `gh pr checks <番号>` で読む。
    2. issue は `gh issue view <番号>` で読む。
    3. CI が落ちたときは、`gh run list --limit 5` で実行を探し、`gh run view <run-id> --log-failed` で失敗したジョブのログだけを読む。
    4. 出力が長いときは、`--json` で項目を選んで `--jq` で絞るか、`| head -n 80` で先頭だけを読む。全文を会話に貼らない。
    5. 使い方が分からないサブコマンドは、推測せずに `gh <サブコマンド> --help` で確かめる。
    6. PR のマージ、issue のクローズ、コメントの投稿は、人が頼んだときだけ行う。頼まれていないときは、実行するコマンドを示して止まる。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet mcp-or-cli/gh-cli-skill -->

常駐するものを小さく保つ順番は <!-- link:begin always-on-costs#reduce -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 減らす順](../context/always-on-costs.md#reduce)<!-- link:end --> にある。スキルが説明文だけを常駐させる仕組みは <!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)<!-- link:end --> にある。

## 確かめ方 {#verify}

選んだ後に、コンテキストが散らかっていないかを確かめる。

- **入れる前**：同じ作業を CLI で 1 回やらせる。手順と、出力の長さが見える。足りないと分かってから MCP を足す。
- **入れた後**：`/context all` で、ツールごとのトークンを見る。`/mcp` でつないだサーバーを確かめ、使っていないサーバーは無効にする。
- **出力が大きいとき**：MCP の出力には警告と既定の上限があり、環境変数 `MAX_MCP_OUTPUT_TOKENS` で変えられる。CLI の出力は、`--json` や `head` で先に絞る。
- **やめどき**：数回の作業で一度も呼ばれないサーバーは外す。入れてコンテキストが膨らんだのに、判断が良くならないなら切る。

ここに書いた操作は WSL・Linux の Claude Code を基準にしている。macOS と IDE 拡張での動作は未確認である。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)：Anthropic・英語・確認日 2026-11-04
- [Best MCP servers for Claude Code and Codex I'm using in 2026](https://composio.dev/content/best-mcp-servers-claude-code-codex)：Composio・英語・確認日 2026-11-04
- [Agentic Coding: The Future of Software Development with Agents](https://simonwillison.net/2025/Jun/29/agentic-coding/)：Simon Willison・英語・確認日 2026-11-04
- [How I Use Every Claude Code Feature](https://feeds.simonwillison.net/2025/Nov/2/how-i-use-every-claude-code-feature/)：Simon Willison・英語・確認日 2026-11-04
- [Designing agentic loops](https://simonwillison.net/2025/Sep/30/designing-agentic-loops/)：Simon Willison・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [MCP をつなぐ](connecting-mcp.md)

**関連**

- 判断を決定論的なスクリプトに移す（準備中）
- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- MCP サーバーの選び方（準備中）
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [スキルの作り方](writing-skills.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
