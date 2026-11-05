---
id: code-intelligence-plugins
title: code intelligence プラグイン（LSP）
aliases: [LSP, 言語サーバー, コードインテリジェンス]
type: feature
field: extend
chapter: プラグイン
order: 220
level: 仕組みにする
priority: 推奨
surfaces: [claude-code]
principle: [見せる]
prevents: [見えていない, 散らかっている]
pitfalls: []
scenes: [開発]
summary: 型のある言語で、定義へのジャンプや型エラーの報告を Claude に使わせられる。ファイルを総当たりで読む代わりに言語サーバーに尋ねるので、探索で読む量が減る。
signs:
  - {type: symptom, text: 関数の定義を探すたびに、多くのファイルを読ませている}
  - {type: goal, text: 編集の後の型エラーに、Claude 自身に気づかせたい}
prerequisites: [plugins-and-marketplaces]
related: [choose-what-to-read, explore-a-codebase, using-ides, vetting-extensions, when-to-add-what]
tracks: [code-intelligence, plugins]
sources: [cc-docs-code-intelligence, cc-docs-features-overview, cc-docs-plugins-overview, cc-docs-changelog]
sections:
  - {title: 使いどころ, anchor: use}
  - {title: 最小の使い方, anchor: minimal}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
volatility: 中
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：型のある言語で、言語サーバーに尋ねて、定義へのジャンプと編集後の型エラーの報告を Claude に使わせられる。
    - **いつ引くか**：関数の定義を探すたびに多くのファイルを読ませているとき。編集の後の型エラーに、Claude 自身に気づかせたいとき。
    - **強制力**：<!-- gen:begin feature code-intelligence/enforcement -->なし<!-- gen:end feature code-intelligence/enforcement -->。Claude に何かを禁じる機能ではない。診断は編集の後に自動で返り、シンボルの検索は読み取り専用の道具である。Claude の動きを止める働きはない。
    - **前提**：<!-- link:begin plugins-and-marketplaces -->[プラグインとマーケットプレイス](plugins-and-marketplaces.md)<!-- link:end -->

<!-- textlint-disable -->
別名：LSP・言語サーバー・コードインテリジェンス
<!-- textlint-enable -->

code intelligence プラグインは、言語ごとの言語サーバーに Claude Code をつなぎ、エディタが持つ「定義へのジャンプ」と「型エラーの表示」を Claude にも使わせるプラグインである。言語サーバーは、Language Server Protocol（LSP）で話す、コードの意味を解析する別のプログラムである。

## 使いどころ {#use}

code intelligence プラグインは、コードを読んで探すより、言語サーバーが解析した結果を尋ねるほうが速い場面で効く。効き方は 2 つある。

- **編集の後の診断**：Claude がファイルを編集するたびに、言語サーバーが見つけた型エラー・足りない import・構文エラーが Claude に返る。ビルドを走らせなくても、自分の編集が持ち込んだ誤りに気づける
- **シンボルでの検索**：Claude が `LSP` という読み取り専用の道具を使い、定義や参照を文字列の検索ではなく、解析した結果から引く。ファイルを総当たりで読む量が減る

この辞典の言葉では、防ぐ原因は 2 つである。1 つ目は「見えていない」。編集の直後に型エラーが Claude に見えないと、Claude は誤りを抱えたまま作業を進める。2 つ目は「散らかっている」。定義を探すために無関係なファイルを大量に読むと、会話に不要な内容が積もり、本当に要る情報がぼやける。原理としては、Claude に見える形で情報を出す「見せる」にあたる。

公式の文書は、使うきっかけとして「シンボルの探索のために多くのファイルを読んでいる」ことを挙げる。型のある言語のリポジトリで使うことが勧められている。同じ「繰り返しが見えてから足す」考え方は <!-- link:begin when-to-add-what#triggers -->[拡張を足すタイミング › 繰り返しの種類と移す先](when-to-add-what.md#triggers)<!-- link:end --> にまとまっている。

!!! example "判断例：入れるか、入れないか"
    - **状況**：TypeScript のリポジトリで、関数の定義を探すたびに Claude が十数個のファイルを読み、編集の後の型エラーはビルドを走らせるまで分からない。
    - **迷う候補**：言語のプラグインと言語サーバーを入れる。入れずに、読ませたいファイルを `@` で直接指して済ませる。
    - **選んだもの**：プラグインを入れる。
    - **理由**：探すファイルが毎回変わるので、`@` で先に指せない。定義の探索と編集後の診断は、毎回の作業で起きる繰り返しである。逆に、触るファイルが数個と分かっている小さな作業なら、`@` で指すほうが手間がない。

読むファイルを自分で指せるときは <!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](../context/choose-what-to-read.md#point-or-search)<!-- link:end --> の方法が先に立つ。知らないコードを読むときの進め方は <!-- link:begin explore-a-codebase#broad-to-narrow -->[知らないコードベースを読む › 広い質問から絞る](../recipes/explore-a-codebase.md#broad-to-narrow)<!-- link:end --> にある。

## 最小の使い方 {#minimal}

使い始める前に、入れるものが 2 つあることを押さえる。言語サーバーの実行ファイルと、それをつなぐプラグインである。プラグインには言語サーバーが含まれないので、実行ファイルは自分で入れる。どちらも自分の権限で動くので、入れる前の確認は <!-- link:begin plugins-and-marketplaces#before-install -->[プラグインとマーケットプレイス › 入れる前の確認](plugins-and-marketplaces.md#before-install)<!-- link:end --> と <!-- link:begin vetting-extensions#provenance -->[MCP・プラグイン・スキルを入れる前の確認 › 出所を確かめる](../safety/vetting-extensions.md#provenance)<!-- link:end --> に従う。

=== "Claude Code"

    1. 使う言語に対応する言語サーバーの実行ファイルを入れ、`claude` を起動するシェルの PATH にあることを確かめる。言語とプラグインと実行ファイルの対応表は[公式の文書](https://code.claude.com/docs/en/plugins/code-intelligence)にある。
    2. Claude Code の中で、公式のマーケットプレイスからプラグインを入れる。例は TypeScript の場合である。

    ```
    /plugin install typescript-lsp@claude-plugins-official
    ```

    3. 入れた直後に、有効になったか `/reload-plugins` が要るかを示すメッセージが出る。出たとおりにする。
    4. 動いているかを確かめる。言語サーバーは、そのプラグインが扱う拡張子のファイルを Claude が最初に編集したときに起動する。

動作の確かめ方は、編集の後の表示である。型エラーをわざと入れる編集をさせ、その下に新しい診断の件数を示す 1 行が出れば、言語サーバーは動いている。診断の中身は Ctrl+O で開ける。1 行も出ないときは、`/plugin` を開いて Errors の欄を見る。`Executable not found in $PATH` と出ていれば、実行ファイルが入っていないか、PATH にない。

なお、言語サーバーの実行ファイルが PATH にあるのにプラグインを入れていないと、編集の後に LSP のプラグインを勧める確認が出る。その場で入れるか断るかを選べ、断る選択肢には今回だけのものと、出さなくするものがある。出さなくした後に戻す方法は公式の文書にある。

VS Code 拡張とデスクトップアプリでの入れ方は、ターミナルと手順が違う（公式は別の手順を案内する）。この辞典の制作の環境では、WSL の CLI 以外の動作を試していないため、未確認である。

## 雛形 {#templates}

どちらも依頼の本文に使う。1 つ目は、言語サーバーが動いているかを確かめる依頼である。壊れても困らないファイルで試す。2 つ目は、定義と参照をシンボルとして探させる依頼で、プラグインの入った環境で効果が出る。

<!-- gen:begin snippet code-intelligence-plugins/check-diagnostics -->
<!-- textlint-disable -->

??? example "雛形：言語サーバーが動いているかを確かめる依頼"

    ```text
    言語サーバーが動いているかを確かめたい。次の手順で進めてください。

    1. <対象のファイル> に、型エラーを 1 つだけわざと入れる（例：数値を受ける引数に文字列を渡す）
    2. 編集の後に Claude Code が報告した診断の内容を、そのまま書き写す
    3. 入れた型エラーを直し、直した後に診断が消えたことを確かめる

    この確認のために変えてよいのは <対象のファイル> だけ。確認が終わったら、ファイルが最初の内容に戻っていることを示す。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.74。

<!-- textlint-enable -->
<!-- gen:end snippet code-intelligence-plugins/check-diagnostics -->

<!-- gen:begin snippet code-intelligence-plugins/find-by-symbol -->
<!-- textlint-disable -->

??? example "雛形：シンボルで定義と参照を探させる依頼"

    ```text
    <関数名またはクラス名> の定義と、それを呼んでいる場所を調べてください。

    - 文字列の検索ではなく、シンボルとして定義と参照をたどる
    - 見つけた場所は、ファイル名と行で示す
    - 関係のないファイルは開かない。開いたファイルがあれば、その理由を 1 行で書く

    調べるだけで、ファイルは変えない。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.74。

<!-- textlint-enable -->
<!-- gen:end snippet code-intelligence-plugins/find-by-symbol -->

## 効かない場面と落とし穴 {#limits}

code intelligence プラグインが効かない、または期待と違う動きになる場面を並べる。

- **実行ファイルがない**：プラグインを入れても、言語サーバーの実行ファイルがなければ何も起きない。診断が 1 行も出ないときに、まず疑う原因である。`/plugin` の Errors の欄で確かめる
- **ターミナルのセッションだけで動く**：公式の文書によると、クラウドのセッションでは言語サーバーが起動せず、診断もシンボルの検索も使えない。クラウドで使う場面は、このプラグインに頼らず、読ませるファイルを絞るほうが確実である
- **診断が最初の編集まで出ない**：言語サーバーは、そのプラグインが扱う拡張子のファイルを最初に編集したときに起動する。編集の前に「診断がない」と読むのは早計である
- **誤検出がある**：モノレポでは、import が解決できないという診断が、実際には正しいのに出ることがある。診断を鵜呑みにせず、ビルドやテストの結果と突き合わせる。Claude が誤検出の診断に引きずられて、正しいコードを直そうとしていないかを見る
- **メモリを使う**：言語サーバーがプロジェクトを索引する間は、メモリの使用が増えることがある。重いと感じたら、公式のトラブルシューティングを見る
- **言語が対応表にない**：公式の対応表にない言語は、自分で `.lsp.json` を持つプラグインを書いて、`--plugin-dir` で読み込む。作り方は公式の文書にあり、ここでは扱わない
- **診断はビルドの代わりにならない**：診断が空でも、テストが通ることは保証されない。完了の確かめは、テストやビルドの実行で行う

公式は、シンボルの検索が広いファイルの読み込みを置き換えるので、全体として使うコンテキストは減りうると書く。ただし、減るかどうかは環境による。誤検出の診断が多い環境では、その対応で読む量が増えうるので、自分の環境で見てから判断する。

IDE の拡張が持つ診断の道具は、このプラグインとは別の仕組みである。IDE 側でできることと違いは <!-- link:begin using-ides#what-you-get -->IDE（VS Code・JetBrains）で使う › IDE で得られるもの（準備中）<!-- link:end --> にある。

## 比べる相手 {#compare}

code intelligence プラグインを、ほかの手段と比べる。

| 手段 | 向く場面 |
| --- | --- |
| code intelligence プラグイン | 型のある言語で、定義の探索と編集後の型エラーの確認が繰り返し起きる |
| `@` で直接指す | 読むファイルが分かっている。<!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](../context/choose-what-to-read.md#point-or-search)<!-- link:end --> |
| 文字列の検索とテスト・ビルドの実行 | 型のない言語、または言語サーバーが使えない環境 |
| IDE の拡張の診断 | IDE を使っていて、IDE 側の検査の結果を読ませたい。<!-- link:begin using-ides#vs-cli -->IDE（VS Code・JetBrains）で使う › CLI との違い（準備中）<!-- link:end --> |

このプラグインはプラグインの一種なので、読み込みの時期やコストは次の表のとおりである。

<!-- gen:begin compare 成熟度 読み込みの時期 コンテキストのコスト 入った版 -->
<!-- textlint-disable -->

| 機能 | 読み込みの時期 | コンテキストのコスト | 入った版 |
| --- | --- | --- | --- |
| [code intelligence プラグイン（LSP）](code-intelligence-plugins.md) | 編集の後と調べるとき | 小さい | 2.0.74（2025-12-19） |
| [プラグイン（plugins）](plugins-and-marketplaces.md) | セッション開始と使うとき | 使うまで小さい | 2.0.12（2025-10-09） |

すべて共通：成熟度 GA。

<!-- textlint-enable -->
<!-- gen:end compare 成熟度 読み込みの時期 コンテキストのコスト 入った版 -->

プラグインをチームで配る方法は <!-- link:begin plugins-and-marketplaces#team-marketplace -->[プラグインとマーケットプレイス › チームのマーケットプレイスを作る](plugins-and-marketplaces.md#team-marketplace)<!-- link:end --> にある。足す順序の考え方は <!-- link:begin when-to-add-what#why -->[拡張を足すタイミング › 繰り返しが見えてから足す理由](when-to-add-what.md#why)<!-- link:end --> を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Code intelligence plugins](https://code.claude.com/docs/en/plugins/code-intelligence)：Anthropic・英語・確認日 2026-11-04
- [Extend Claude Code](https://code.claude.com/docs/en/features-overview)：Anthropic・英語・確認日 2026-11-04
- [Plugins overview](https://code.claude.com/docs/en/plugins/overview)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [プラグインとマーケットプレイス](plugins-and-marketplaces.md)

**関連**

- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- [知らないコードベースを読む](../recipes/explore-a-codebase.md)
- IDE（VS Code・JetBrains）で使う（準備中）
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [拡張を足すタイミング](when-to-add-what.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
