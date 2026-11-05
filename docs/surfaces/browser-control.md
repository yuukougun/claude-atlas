---
id: browser-control
title: Claude in Chrome と computer use（ブラウザと画面の操作）
nav_title: Claude in Chrome と computer use
aliases: [Chrome 拡張, ブラウザ操作, 画面操作, コンピュータの操作]
type: feature
field: surfaces
chapter: ブラウザと周辺製品
order: 50
level: 任せる
priority: 推奨
surfaces: [app, claude-code]
principle: [確かめる, 縛る]
prevents: [確かめていない, 境界がない]
pitfalls: []
scenes: [開発, 調べもの]
summary: Claude in Chrome でブラウザを、computer use で手元のアプリの画面を操作させ、作った画面の確かめや手作業の代行に使える。コネクタ（MCP）があればそちらを先に使い、機微な作業は任せない。
signs:
  - {type: goal, text: 作った Web の画面を、Claude に実際のブラウザで確かめさせたい}
  - {type: goal, text: ブラウザでのフォーム入力のような手作業を代わりにやってほしい}
  - {type: situation, text: API も connector もないアプリを Claude に操作させたい}
prerequisites: [where-it-runs]
related: [browser-agent-cautions, visual-checks, lethal-trifecta, prompt-injection-in-practice, connectors-in-the-app, permission-modes-in-the-app, office-paperwork]
tracks: [claude-in-chrome, computer-use]
outdated_advice: []
sources: [cc-docs-chrome, hc-claude-in-chrome, hc-computer-use, cc-docs-computer-use, api-docs-computer-use, cc-docs-desktop, cc-docs-feature-availability]
volatility: 高
sections:
  - {title: コネクタ・ブラウザ・画面の順に選ぶ, anchor: which-to-use}
  - {title: Claude in Chrome, anchor: claude-in-chrome}
  - {title: computer use は最後の手段, anchor: computer-use}
  - {title: 任せない作業, anchor: what-not-to-hand-over}
  - {title: 効かない場面と落とし穴, anchor: limits}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：ブラウザは Claude in Chrome、手元のアプリの画面は computer use で操作させ、画面の確かめや手作業の代行に使える。
    - **いつ引くか**：作った Web の画面を実際のブラウザで確かめさせたいとき。フォーム入力のような手作業を任せたいとき。API やコネクタがないアプリを操作させたいとき。
    - **前提**：<!-- link:begin where-it-runs -->[実行場所の違い（クラウド・自分の PC・リモート操作）](where-it-runs.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Chrome 拡張・ブラウザ操作・画面操作・コンピュータの操作
<!-- textlint-enable -->

Claude in Chrome と computer use は、Claude に画面の操作を任せる 2 つの機能である。前者は Chrome のブラウザの中を、後者は手元のアプリの画面全体を操作する。どちらも、ログイン済みのサイトや開いているアプリまで届くため、任せる範囲を先に決めてから使う。

## コネクタ・ブラウザ・画面の順に選ぶ {#which-to-use}

操作を任せる手段には優先順がある。公式の案内では、先に試すのがコネクタ（Claude Code では MCP）、次がブラウザの操作（Claude in Chrome）、最後が画面の操作（computer use）である。コネクタのほうが速く確実だからだ。この順は、届く範囲の広さの順でもある。コネクタは対象のサービスだけに届き、ブラウザの操作はログイン済みのサイトに届き、画面の操作は開いているアプリすべてに届く。

任せる幅が広がる手段なので、使う前に守りを確かめておく。ログイン済みのサイトとアプリに何が届くかの整理は <!-- link:begin browser-agent-cautions#reach -->[ブラウザや画面の操作を任せるときの注意 › 届く範囲（ログイン済みのサイト・開いているアプリ）](../safety/browser-agent-cautions.md#reach)<!-- link:end --> にある。読む情報・秘密・外への送信を同時に持たせない考え方は <!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](../safety/lethal-trifecta.md#three-capabilities)<!-- link:end --> にある。

| 手段 | 向く作業 | 届く範囲 |
| --- | --- | --- |
| コネクタ（MCP） | メール・カレンダー・社内の資料など、つなぎ先のサービスの操作 | つないだサービスだけ |
| Claude in Chrome | Web の画面の確かめ、ブラウザでの入力や情報の取り出し | ブラウザで開けるページ（ログイン済みのサイトを含む） |
| computer use | コネクタもブラウザの道具もないアプリの操作 | 画面に出ているアプリ全般 |

コネクタの使い方と信頼の判断は <!-- link:begin connectors-in-the-app#trust -->[コネクタ（MCP）をアプリで使う › 信頼してよいか](../app/connectors-in-the-app.md#trust)<!-- link:end --> にある。2 つの機能の成熟度と入った版は、次の表を見る。

<!-- gen:begin compare -->
<!-- textlint-disable -->

| 機能 | 面 | 成熟度 | 入った版 |
| --- | --- | --- | --- |
| [Claude in Chrome](browser-control.md) | アプリ・Claude Code | GA | 2.0.72（2025-12-17） |
| [computer use](browser-control.md) | アプリ・Claude Code・API | beta | 2024-10-22 |

すべて共通：確認日 2026-11-04。

<!-- textlint-enable -->
<!-- gen:end compare -->

!!! example "判断例：コネクタのない社内の勤怠システムに入力させる"
    - **状況**：勤怠の入力は社内の Web システムで行う。API やコネクタはない。
    - **迷う候補**：Claude in Chrome にブラウザで入力させる。computer use に画面ごと操作させる。
    - **選んだもの**：Claude in Chrome。
    - **理由**：画面がブラウザの中にあるので、優先順が上の手段で足りる。操作がブラウザのタブに収まり、ほかのアプリに触れない。

## Claude in Chrome {#claude-in-chrome}

Claude in Chrome は、Claude がブラウザのページを読み、クリックし、移動できるようにする Chrome の拡張である。Chrome のサイドパネル、Cowork、Claude Code から使える。Claude はタブを新しく開いて作業し、ブラウザのログイン状態を共有するため、自分がログイン済みのサイトにも入れる。ログイン画面や CAPTCHA が出たときは、止まって人に操作を求める。

使いどころは 2 つある。

1 つ目は、作った画面の確かめである。Claude Code で作った画面を実際のブラウザで開き、フォームの動きとコンソールのエラーと DOM の状態を見せる。単体テストだけで完了とみなす「確かめていない」状態を防げる。確かめ方の本体は <!-- link:begin visual-checks#as-a-user -->[画面で確かめる（ブラウザ・スクリーンショット・/verify） › 人のユーザーとして確かめさせる](../verify/visual-checks.md#as-a-user)<!-- link:end --> と <!-- link:begin visual-checks#screenshots -->[画面で確かめる（ブラウザ・スクリーンショット・/verify） › スクリーンショットで比べる](../verify/visual-checks.md#screenshots)<!-- link:end --> にある。

2 つ目は、手作業の代行である。ログイン済みのサイトでのフォーム入力、情報の取り出し、複数のサイトをまたぐ作業を任せられる。

縛りの置き場所は拡張の側にある。どのサイトを閲覧・クリック・入力してよいかの許可は、拡張の設定から引き継がれる。Claude Code では、ブラウザの操作の前に許可を求める画面が出る。「このサイトの操作を、このセッションで全部許可する」も選べるが、広げる前に、そのサイトにログイン済みの情報が何かを考える。

=== "アプリ"
    Chrome のサイドパネルか、Cowork から始める。サイドパネルでは、保存したプロンプトの呼び出し、定期タスク、複数タブの扱いなども使える。対応するプランと Chrome の対応範囲は、公式の案内（確認日 2026-11-05）で確かめる。面に固有の手順は、公式の Help Center の入門の記事にある。

=== "Claude Code"
    ターミナルから `claude --chrome` で起動すると、ブラウザの操作が使える。接続の状態の確認、権限の管理、再接続、使うブラウザの選択は、`/chrome` で行う。毎回フラグを付けない設定もあるが、ブラウザの道具の説明が常に読み込まれるため、コンテキストの使用量が増える。必要なときだけ接続するほうが軽い。

    Claude Code から使う要件は、次のとおりである（<!-- fact:begin chrome-extension-requirements -->拡張 1.0.36 以降。Chrome・Edge と、検出される Chromium 系。直接の Anthropic のプラン（Pro・Max・Ultra・Team・Enterprise）。/login での認証が要る（API キーと setup-token では無効）。WSL は非対応。第三者のプロバイダー経由は不可（2026-11-05 時点）<!-- fact:end -->）。API キーや長期のトークンで認証しているセッションでは、この連携は有効にならない。`/login` でのログインが要る。ほかの OS と IDE 拡張の動作は未確認である。

Claude Code から画面を確かめさせる依頼と、フォーム入力を送信の手前で止める依頼の雛形を載せる。どちらも、試験用の画面と偽のデータで試す。

<!-- gen:begin snippet browser-control/verify-local-app -->
<!-- textlint-disable -->

??? example "雛形：ローカルの画面を確かめさせる依頼"

    ```markdown
    手元の開発サーバー（`http://localhost:3000`）で、ログインフォームの入力の確かめをしてほしい。コードは書き換えず、ブラウザで見て報告するだけにする。開くのはこのアドレスのタブだけにして、ほかのサイトのタブは開かない。

    次の 3 つを順に試す。

    1. 何も入力せずに送信し、エラーの表示を確かめる
    2. メールアドレスに `abc` だけを入れて送信し、エラーの表示を確かめる
    3. 試験用の `test@example.com` と、画面に書いてある試験用のパスワードで送信し、移動先の画面を確かめる

    各段階でスクリーンショットを撮り、コンソールにエラーが出たかを見る。コンソールは全文を貼らず、エラーの行だけを拾う。

    結果は表で返す。列は「試したこと」「画面に見えたもの」「コンソールのエラー」「期待と合っているか」とする。見えたものと、そこからの推測は分けて書く。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.72。

<!-- textlint-enable -->
<!-- gen:end snippet browser-control/verify-local-app -->

<!-- gen:begin snippet browser-control/fill-form-dry-run -->
<!-- textlint-disable -->

??? example "雛形：送信の手前で止めるフォーム入力の依頼"

    ```markdown
    ブラウザで、次の問い合わせフォームを埋めてほしい。ただし、送信ボタンは押さない。

    - 開くページ：`http://localhost:3000/contact`（試験用のページ）
    - 名前：試験 太郎
    - メール：`test@example.com`
    - 本文：これは入力の試験です。

    入力し終えたら、そこで止めて、画面に見えている入力欄と値を一覧にして返す。ログインや CAPTCHA の画面が出たら、操作せずに知らせる。入力欄が見つからない、または名前や値が想定と違うときは、推測で埋めずに止めて報告する。送信するかどうかは、一覧を見てからこちらで決める。
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.0.72。

<!-- textlint-enable -->
<!-- gen:end snippet browser-control/fill-form-dry-run -->

## computer use は最後の手段 {#computer-use}

computer use は、使えるコネクタもブラウザの道具もないときに、Claude が画面を直接クリックし、入力し、アプリを開けるようにする機能である。Claude in Chrome がブラウザの中に限られるのに対し、こちらは画面に出ているアプリ全般を操作する。手段として一番広く届くので、優先順では最後に置く。

縛りは弱い。公式の Help Center は、Claude とアプリの間にサンドボックスがないと明記している。許可はアプリごとに求められ、投資・取引・暗号資産のアプリは既定でブロックされる。それでも、画面に出ている個人情報や機密は Claude に見える。また、あるアプリでの操作が別のアプリに及ぶ。たとえば、リンクを開くと Chrome が起動する。

公式は、金融・医療・法務など個人の記録を扱うアプリには使わないよう案内している。使うなら、機微なファイルを先に閉じ、信頼できるアプリから始め、具体的な依頼で進め、作業を見守る。操作はいつでも止められる。デスクトップを起きたままにしておく必要がある。

成熟度の表記は、面と出典で違う。Cowork と Desktop の Help Center は beta と書き、Claude Code の文書は research preview と書く。この辞典の成熟度の表（先頭の節）は、Cowork と Desktop の Help Center の表記に合わせている。研究中の機能なので、操作の手順は書かず、対象のプラン・OS・面は公式で確かめる。

=== "アプリ"
    Cowork と Desktop で使える。設定の「Enable computer use」の切り替えで有効にする。対象のプランと OS は（<!-- fact:begin computer-use-requirements -->未確認<!-- fact:end -->）。

=== "Claude Code"
    Desktop の Code タブと、CLI から使える。CLI は Desktop と対象の OS が違い、使える条件が限られる。公式の文書（確認日 2026-11-05）で確かめる。

API でも computer use の道具が公開されている。API からの使い方は、この辞典では API の分野で扱う。

## 任せない作業 {#what-not-to-hand-over}

ブラウザと画面の操作で任せない作業は、取り消しにくいもの、機微な情報に触れるもの、権限が広すぎるものの 3 つである。範囲の整理の本体は <!-- link:begin browser-agent-cautions#what-not-to-do -->[ブラウザや画面の操作を任せるときの注意 › 任せない作業](../safety/browser-agent-cautions.md#what-not-to-do)<!-- link:end --> にあり、ここでは判断の入口だけを示す。

- 銀行・医療・行政・投資など、機微な情報を扱うサイトとアプリの操作。公式は、機微な情報の扱いに Claude in Chrome などを使うことを強く勧めていない（確認日 2026-10-29）
- 送信・購入・支払いのような、取り消しにくい操作。定期実行のタスクにもしない
- 認証情報や秘密を入力させる作業
- 信頼できないページを読ませながら、ログイン済みのサイトで書き込みや送信をさせる作業。ページに仕込まれた指示に従うおそれがある。防ぎ方は <!-- link:begin prompt-injection-in-practice#what-works -->[プロンプトインジェクションの実際 › 防ぐ手立ては権限と通信の側にある](../safety/prompt-injection-in-practice.md#what-works)<!-- link:end --> にある

入力までを任せ、確定は人が行う、という分け方が基本である。

!!! example "判断例：経費精算のフォームを埋めさせる"
    - **状況**：経費精算の Web フォームに、領収書の内容を 20 件入力する。ログイン済みのブラウザで行う。
    - **迷う候補**：送信まで任せて手間を最小にする。入力までを任せ、送信は人が押す。
    - **選んだもの**：入力までを任せ、入力欄と値の一覧を見て、送信は人が押す。
    - **理由**：送信は取り消しにくい。入力の誤りは、一覧を見れば送信の前に直せる。依頼の形は、Claude in Chrome の節にある雛形「送信の手前で止めるフォーム入力の依頼」を使う。

人 → AI → 人の流れで事務作業を半自動にする考え方は <!-- link:begin office-paperwork#human-ai-human -->[事務作業の半自動化（経費・報告） › 人 → AI → 人の流れにする](../recipes/office-paperwork.md#human-ai-human)<!-- link:end --> にある。私的な情報を渡す範囲を先に決める手順は <!-- link:begin office-paperwork#private-data -->[事務作業の半自動化（経費・報告） › 私的な情報を渡す範囲](../recipes/office-paperwork.md#private-data)<!-- link:end --> にある。確認なしで進める範囲を決める権限モードは <!-- link:begin permission-modes-in-the-app#two-conditions -->[アプリの権限モード（Auto と Manual）と安全 › 読める範囲と行動できる範囲を同時に広げない](../app/permission-modes-in-the-app.md#two-conditions)<!-- link:end --> にある。

## 効かない場面と落とし穴 {#limits}

動かない・止まる原因は、多くが接続の側にある。Claude Code の連携で出やすいものを挙げる。

- **ダイアログで止まる**：ページの alert・confirm・prompt が出ていると、ブラウザの操作が止まる。ダイアログを手で閉じてから、続けるよう頼む
- **接続が切れる**：長いセッションで、拡張が眠って接続が切れる。`/chrome` で再接続する
- **「Browser extension is not connected」**：拡張が、Claude Code と別のアカウントや組織でログインしている。同じアカウントと組織に揃える。`/status` で組織が分かる
- **アップロードが断られる**：読む権限のないファイル、複数のハードリンクを持つファイル、認証情報の置き場の名前のファイル（`.env`・`.ssh` 配下など）は添付されない
- **記録に写り込む**：GIF の記録は、画面に見えているアカウントの情報を写す。社外に出す前に見直す
- **リポジトリからは有効にならない**：チェックアウトしたリポジトリの設定は、ブラウザの連携を勝手に有効にしない。手元で `claude --chrome` か `/chrome` を使う

読んだページに仕込まれた指示に Claude が従う危険は、機能の側では消せない。減らす手立ては、持たせる権限と通信の組み合わせの側にある。

古くなった助言の台帳に、この機能の行は今のところない。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use Claude Code with Chrome](https://code.claude.com/docs/en/chrome)：Anthropic・英語・確認日 2026-11-04
- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)：Anthropic・英語・確認日 2026-11-04
- [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)：Anthropic・英語・確認日 2026-11-04
- [Let Claude use your computer from the CLI](https://code.claude.com/docs/en/computer-use)：Anthropic・英語・確認日 2026-11-04
- [Computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)：Anthropic・英語・確認日 2026-11-04
- [Desktop application](https://code.claude.com/docs/en/desktop)：Anthropic・英語・確認日 2026-11-04
- [Feature availability](https://code.claude.com/docs/en/feature-availability)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [実行場所の違い（クラウド・自分の PC・リモート操作）](where-it-runs.md)

**関連**

- [ブラウザや画面の操作を任せるときの注意](../safety/browser-agent-cautions.md)
- [画面で確かめる（ブラウザ・スクリーンショット・/verify）](../verify/visual-checks.md)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)
- [プロンプトインジェクションの実際](../safety/prompt-injection-in-practice.md)
- [コネクタ（MCP）をアプリで使う](../app/connectors-in-the-app.md)
- [アプリの権限モード（Auto と Manual）と安全](../app/permission-modes-in-the-app.md)
- [事務作業の半自動化（経費・報告）](../recipes/office-paperwork.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
