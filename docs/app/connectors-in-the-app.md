---
id: connectors-in-the-app
title: コネクタ（MCP）をアプリで使う
aliases: [Connectors, Custom connectors, Desktop extensions, .mcpb, claude_desktop_config.json, ローカル MCP サーバー]
type: feature
field: app
chapter: つなぐ・足す
order: 130
level: 整える
priority: 必須
surfaces: [app]
principle: [見せる, 縛る]
prevents: [見えていない, 境界がない]
scenes: [調べもの, チーム]
summary: メール・カレンダー・社内の資料や自分の MCP サーバーをアプリにつなぎ、会話から使える。多くつなぐときの読ませ方と、信頼してよいかの判断が分かる。
signs:
  - {type: goal, text: メールやカレンダー、社内の資料を踏まえて答えてほしい}
  - {type: goal, text: 自分の MCP サーバーをアプリから使いたい}
  - {type: situation, text: 外部のサービスとつなぐ便利な道具を見つけた}
prerequisites: []
related: [connecting-mcp, vetting-extensions, lethal-trifecta, prompt-injection-in-practice, always-on-costs, mcp-or-cli, using-research, plugins-in-the-app]
tracks: [connectors, mcp]
outdated_advice: [customize-tabs]
sources: [hc-connectors, claude-blog-integrations, hc-getting-started-local-mcp, mcp-docs-develop-connect-local-servers, cc-docs-desktop, hc-plugins-page, hc-release-notes, hc-cowork-and-chat]
volatility: 中
sections:
  - {title: コネクタの種類, anchor: types}
  - {title: 使うときだけ読ませる（On demand）, anchor: on-demand}
  - {title: Desktop のローカル MCP, anchor: desktop-local-mcp, level: 任せる}
  - {title: 信頼してよいか, anchor: trust}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：メールや社内の資料につなぐコネクタを会話から使い、多くつなぐときは On demand で読ませる量を絞れる。
    - **いつ引くか**：メールやカレンダー、社内の資料を踏まえて答えてほしいとき。自分の MCP サーバーをアプリから使いたいとき。外部のサービスとつなぐ便利な道具を見つけたとき。
    - **強制力**：コネクタは道具を足す機能で、Claude に何かを禁じる鍵ではない。止められるのは、道具ごとの許可（Always allow・Needs approval・Blocked）で締めた操作だけである。
    - **前提**：なし

<!-- textlint-disable -->
別名：Connectors・Custom connectors・Desktop extensions・.mcpb・claude_desktop_config.json・ローカル MCP サーバー
<!-- textlint-enable -->

コネクタ（MCP）をアプリで使うとは、claude.ai・Desktop・Mobile の会話から、メール・カレンダー・社内の資料などの外部のサービスを道具として呼べるようにすることである。つなぎ先を会話に見せる機能なので、答えの前提を整える段階で効く。防ぐ原因は 2 つある。会話に前提の資料が見えていないこと、そして何を読み書きしてよいかの境界がないことである。同時に、外のデータと外への操作を会話に持ち込むので、信頼の判断が付いて回る。MCP の仕組みと Claude Code 側の設定は <!-- link:begin connecting-mcp -->[MCP をつなぐ](../extend/connecting-mcp.md)<!-- link:end --> にある。ここには、アプリに固有の操作だけを書く。

## コネクタの種類 {#types}

コネクタの種類とは、つなぎ先がどこで動き、誰が用意したかの違いである。公式の文書は次の 4 つに分ける。

- **Directory connectors**：ディレクトリに並ぶ既製のコネクタ。メール・カレンダー・ファイル置き場・チャットなどのサービスを選んで入れる。
- **Custom connectors**：リモートの MCP サーバーを自分でつなぐもの。Anthropic のクラウドから接続し、手元の端末からは接続しない。
- **Desktop extensions**：Claude Desktop 用の包み。ローカルで動く MCP サーバーを 1 つにまとめたもので、`.mcpb` の形で配る。
- **Interactive connectors**：会話の中にライブの UI を描くもの。

違いが効くのは、どこで動くかである。Custom connectors はクラウドから接続するので、自分の PC の中だけで動くサーバーには届かない。ローカルのコネクタと MCP は Desktop 専用である。Web と Mobile は、リモートのコネクタを使う。

プランによる差もある。Team と Enterprise では、owner が組織でコネクタを有効にし、各人が自分のアカウントで認証する。個人のプランでは Custom connectors の数に上限がある。数や対象のプランは変わりやすいので、現在の値は公式の記事を見る。

### 最小の使い方

使い始めは 4 つの手順で足りる。

1. コネクタの管理画面で、Directory のコネクタを入れるか、リモートの MCP サーバーを Custom connector として足す。画面の名前は変わりつつある（後の「古くなった助言」の節）。
2. 足したサービスで認証する。Team と Enterprise なら、owner が最初に有効化する。
3. 会話の入力欄の「+」か「/」から Connectors を開き、そのチャットで使うものをオンにする。オンにするのはチャットごとである。
4. 依頼に、何を読ませるか、読むだけか書き込みもするかを書く。

依頼の例は次の雛形にある。書き込みの道具を使わせたくないときは、依頼で禁じるだけでなく、道具ごとの許可でも締める（「信頼してよいか」の節）。

<!-- gen:begin snippet connectors-in-the-app/connector-request -->
<!-- textlint-disable -->

??? example "雛形：コネクタを使う依頼（読み取りだけに絞る）"

    ```markdown
    Google カレンダーの今週の予定と、Gmail の未読のうち件名に「見積」を含むものを読んで、返信が要るものを一覧にしてほしい。

    - 使うのは読み取りだけにする。メールの送信、下書きの作成、予定の変更はしない
    - 一覧には、相手・期限・返信が要る理由を 1 行ずつ書く
    - 読めなかったものや、判断に迷ったものは、一覧の最後にまとめる
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet connectors-in-the-app/connector-request -->

## 使うときだけ読ませる（On demand） {#on-demand}

On demand とは、コネクタの道具をチャットの最初から全部抱えず、使うときに読み込ませる設定である。コネクタの設定にある Tool access には Auto と On demand があり、読み込み方を選べる。

多くつなぐと、道具の一覧と説明が文脈を使う。毎回のリクエストに乗るものの費用は、常駐するものと使うときだけ読むものの違いとして、<!-- link:begin always-on-costs#resident-vs-on-demand -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 常駐するものと、使うときだけ読むもの](../context/always-on-costs.md#resident-vs-on-demand)<!-- link:end --> にまとめてある。公式の記事は、有効にしたコネクタが多いとき（目安の数は公式の記事を見る）に On demand を勧めている。

On demand が効くのは、見えていないものを減らすためではなく、見せすぎて焦点がぼやけるのを防ぐためである。コネクタが多いほど、依頼に関係のない道具が文脈に混ざる。

判断の分かれ目は、そのチャットで使うコネクタの数と、どれを使うかを自分で言えるかである。

!!! example "判断例：コネクタを多くつないだ人の既定の選び方"
    - **状況**：メール・カレンダー・ファイル置き場・チャット・社内の wiki など、コネクタを多くつないでいる。多くの会話では、そのうち 1 つか 2 つしか使わない。
    - **迷う候補**：Tool access を Auto のままにして、Claude に必要な道具を選ばせる。または On demand にして、使うときだけ読み込ませる。
    - **選んだもの**：On demand にし、使ってほしいコネクタは依頼に名前で書く。
    - **理由**：Auto だと、使わない道具の説明も毎回文脈に乗る。依頼に名前を書けば、読み込みのきっかけが明確になる。ただし、名前を書く運用が読み込みを確実にするかは公式の記事に書かれていない（推論・実践例なし）。使い勝手が悪ければ Auto に戻す。

## Desktop のローカル MCP {#desktop-local-mcp}

Desktop のローカル MCP とは、自分の PC で動く MCP サーバーを Claude Desktop につなぐ仕組みである。リモートのコネクタと違い、サーバーは利用者の権限で動く。入れる前に、出所と中身の確かめ方を <!-- link:begin vetting-extensions#checklist -->[MCP・プラグイン・スキルを入れる前の確認 › 全体の確かめ方](../safety/vetting-extensions.md#checklist)<!-- link:end --> で見てから進める。

つなぎ方は 2 通りある。

- **Desktop extensions（.mcpb）**：ローカルの MCP サーバーを 1 つの包みにしたもの。Anthropic が審査したディレクトリから入れるほか、自作の `.mcpb` を開発者向けの設定から入れられる。Node.js・Python・バイナリのサーバーに対応する。API キーなど sensitive と印を付けた設定は、OS の秘密の保管庫で暗号化される。ディレクトリのものは既定で自動更新され、私的に配った `.mcpb` は手で入れ替える。
- **JSON の設定**：従来の方法。`claude_desktop_config.json` の `mcpServers` に command と args を書き、Desktop を完全に終了して起動し直す。ファイルの場所は OS ごとに違うので、公式の文書を見る。

JSON の設定の最小の例は次のとおりである。渡すフォルダは、作業用の 1 つに絞る。

<!-- gen:begin snippet connectors-in-the-app/desktop-config -->
<!-- textlint-disable -->

??? example "雛形：claude\_desktop\_config.json にローカル MCP サーバーを足す例"

    ```json
    {
      "mcpServers": {
        "filesystem": {
          "command": "npx",
          "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "/path/to/one-working-folder"
          ]
        }
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet connectors-in-the-app/desktop-config -->

設定画面の入口の名前は、公式の文書の間で揺れている。MCP の文書は Settings > Developer の「Edit Config」から開くと書くが、Help Center はこの画面を旧レイアウトの名前として扱う。新しいレイアウトでの入口の名前は確かめていない。迷ったときは、設定ファイルを直接開く。

つながったかどうかは、入力欄の「+」>「Connectors」で確かめる。つながった MCP サーバーとツールが見える。状態とログは、Extensions のページの Local MCP servers の欄で見る。旧レイアウトでは Settings > Developer にあった。

Team と Enterprise の owner は、公開の extensions の可否、許可の一覧、自作の extension の配布を決められる。端末側の企業向けの方針は、アプリ内の設定より優先される。

Desktop の Code タブが `claude_desktop_config.json` を読む話は、Claude Code 側の扱いと合わせて <!-- link:begin connecting-mcp#desktop -->[MCP をつなぐ › Desktop アプリの MCP との関係](../extend/connecting-mcp.md#desktop)<!-- link:end --> にまとめてある。

## 信頼してよいか {#trust}

コネクタを信頼してよいかとは、つなぎ先のサーバーを動かす組織と、そこから会話に入ってくるデータを、どこまで信じるかの判断である。

Custom connectors は Anthropic の検証を受けていない。公式の記事は、信頼できる組織のサーバーだけにつなぐよう案内している。Directory のコネクタを使うときも、そのコネクタが何を読み、何を書けるかは自分で確かめる。入れる前の確かめ方は <!-- link:begin vetting-extensions#provenance -->[MCP・プラグイン・スキルを入れる前の確認 › 出所を確かめる](../safety/vetting-extensions.md#provenance)<!-- link:end --> と <!-- link:begin vetting-extensions#changes-after-install -->[MCP・プラグイン・スキルを入れる前の確認 › 入れた後に変わる（rug pull）](../safety/vetting-extensions.md#changes-after-install)<!-- link:end --> にある。

メールや資料を読むコネクタは、会話に外のデータを入れる。そのデータに、仕込まれた指示が混ざる場合もある。仕組みは <!-- link:begin prompt-injection-in-practice#channels -->[プロンプトインジェクションの実際 › 指示が入ってくる経路](../safety/prompt-injection-in-practice.md#channels)<!-- link:end --> に書いてある。防ぐ手立ては、持たせる権限の側にあり、Claude の賢さには頼れない（<!-- link:begin prompt-injection-in-practice#what-works -->[プロンプトインジェクションの実際 › 防ぐ手立ては権限と通信の側にある](../safety/prompt-injection-in-practice.md#what-works)<!-- link:end -->）。

アプリで効く手段は、道具単位の許可である。道具ごとに Always allow・Needs approval・Blocked を選べる。Team と Enterprise では、owner が組織の側でこれを設定できる。読むだけの道具は Always allow、書き込みや送信の道具は Needs approval か Blocked、という分け方が基本になる。

能力を 3 つ同時に持たせる危険は、<!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](../safety/lethal-trifecta.md#three-capabilities)<!-- link:end --> にある。メールのコネクタは、これを 1 つで満たしやすい。受信箱には外の人の文が入り（信頼できない入力）、中身は私的なデータで、送信の道具があれば外へ出せる。

!!! example "判断例：メールのコネクタに送信の道具まで許すか"
    - **状況**：受信箱を読んで返信の案を作らせたい。コネクタには、読む道具と送信する道具の両方がある。
    - **迷う候補**：送信の道具も Always allow にして、返信まで任せる。または送信の道具を Needs approval か Blocked にして、案を作らせるまでにする。
    - **選んだもの**：送信の道具は Needs approval にし、案の確認は自分で行う。
    - **理由**：受信箱には外の人の文が入る。そこに仕込まれた指示が送信を呼べば、私的な内容が外へ出る。3 つの能力がそろう構成なので、送信の前に人の承認を挟む。3 つとも要る作業の考え方は <!-- link:begin lethal-trifecta#when-all-three -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つとも要るとき](../safety/lethal-trifecta.md#when-all-three)<!-- link:end --> にある。

## 効かない場面と落とし穴 {#limits}

効かない場面と落とし穴は、次のとおりである。

- **道具単位の許可は、ツールの中身までは見ない**。許した道具の引数に何が入るかは、許可では決まらない。
- **オンにするのは、チャットごと**。前のチャットでオンにしたつもりのコネクタが、新しいチャットでは使われない。
- **ローカルの MCP は Desktop だけ**。Web と Mobile では、ローカルのサーバーに依存した手順が動かない。
- **サーバーは利用者の権限で動く**。ローカルの MCP サーバーに広いフォルダを渡すと、Claude への指示では守れない。渡す範囲で縛る。
- **後から中身が変わる**。入れた時点で確かめても、更新されると道具の説明は変わりうる（<!-- link:begin vetting-extensions#changes-after-install -->[MCP・プラグイン・スキルを入れる前の確認 › 入れた後に変わる（rug pull）](../safety/vetting-extensions.md#changes-after-install)<!-- link:end -->）。
- **Mobile や段階展開中の機能は、見え方が違う**。同じプランでも、画面の名前や項目は揃わない場合もある。

## 比べる相手 {#compare}

比べる相手は、同じ目的を別の手段で満たすものである。

- **Claude Code の MCP**：設定の置き場所とスコープを自分で決める。アプリの画面操作ではなく、設定ファイルと CLI で扱う。仕組みは <!-- link:begin connecting-mcp -->[MCP をつなぐ](../extend/connecting-mcp.md)<!-- link:end --> にある。
- **CLI とスキルで済ませる**：成熟した CLI があれば、MCP をつながずに済むことがある。選び方は <!-- link:begin mcp-or-cli -->[MCP か CLI か](../extend/mcp-or-cli.md)<!-- link:end --> にある。
- **プラグイン**：スキル・コネクタ・サブエージェントなどの束。職種ごとの道具一式を入れたいときは <!-- link:begin plugins-in-the-app -->アプリでプラグインを使う（準備中）<!-- link:end --> を見る。
- **リサーチと組み合わせる**：コネクタをつなぐと、リサーチが社内の資料も調べに使える。頼み方と出典の確かめ方は <!-- link:begin using-research#with-connectors -->[リサーチを使いこなす › コネクタと組み合わせる](using-research.md#with-connectors)<!-- link:end --> にある。

## 古くなった助言 {#outdated}

古くなった助言は、コネクタの管理画面の名前に関するものである。「Customize」の「Skills」「Connectors」「Plugins」の各タブで管理する、という手順書が古くなりつつある。現在は <!-- name:begin customize-to-plugins -->「Plugins」（サイドバー・チャットのメニュー・設定の名前と、1 つの「Plugins」のページ）<!-- name:end --> に切り替わる途中で、変わった口座では 1 つの「Plugins」のページでコネクタも管理する。展開の途中なので、自分の口座がどちらの画面かは、サイドバーに「Customize」と「Plugins」のどちらが出るかで確かめる。台帳の行は <!-- link:begin outdated-advice-ledger#customize-tabs -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#customize-tabs)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)：Anthropic・英語・確認日 2026-11-04
- [Claude can now connect to your world](https://claude.com/resources/articles/integrations)：Anthropic・英語・確認日 2026-11-04
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)：Anthropic・英語・確認日 2026-11-04
- [Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers)：Model Context Protocol・英語・確認日 2026-11-04
- [Desktop application](https://code.claude.com/docs/en/desktop)：Anthropic・英語・確認日 2026-11-04
- [Manage plugins, skills, and connectors from one Plugins page](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- アプリでプラグインを使う（準備中）

**関連**

- [MCP をつなぐ](../extend/connecting-mcp.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [MCP か CLI か](../extend/mcp-or-cli.md)
- [リサーチを使いこなす](using-research.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
