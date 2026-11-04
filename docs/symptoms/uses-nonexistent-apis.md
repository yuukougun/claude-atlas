---
id: uses-nonexistent-apis
title: 存在しない関数やパッケージを使う
aliases: [存在しない API, 架空のパッケージ, package hallucination]
type: symptom
field: symptoms
chapter: 事実と出典
order: 80
level: 整える
priority: 必須
surfaces: [claude-code, app, api]
principle: [見せる, 確かめる]
prevents: [見えていない, 確かめていない, 境界がない]
pitfalls: []
scenes: [開発, コンテスト]
summary: 存在しない関数・引数・パッケージを使われる原因を、読ませた資料と知識の古さから切り分け、読んでから書かせる手と、導入前の確かめ方を決める。
signs:
  - {type: symptom, text: 存在しない関数や引数を自信満々に使う}
  - {type: symptom, text: インストールできないパッケージ名を書かれる}
  - {type: symptom, text: 実行する環境で使えないライブラリを足される}
wave: 1
prerequisites: [why-hallucinations, knowledge-cutoff]
related: [fact-checking, connecting-mcp, read-specs-yourself, doesnt-know-latest, plausible-falsehoods, six-causes]
routes:
  - {cause: 見えていない, to: [choose-what-to-read, code-intelligence-plugins]}
  - {cause: 確かめていない, to: [tests-first, evidence-not-reports]}
  - {cause: 境界がない, to: [vetting-extensions#dependencies]}
tracks: [plugins]
outdated_advice: []
sources:
  - arxiv-2406-10279
  - arxiv-2605-17062
  - arxiv-2507-15224
  - arxiv-2403-08937
  - zenn-lluminai-7bd42376
  - api-docs-prompting-best-practices
  - cc-docs-best-practices
  - cc-docs-costs
  - invicti-web-security-owasp-top-risks
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 原因ごとの対処へ, anchor: to-fixes}
  - {title: 判断例, anchor: example}
  - {title: 予防は依頼と仕組みに移す, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：存在しない関数・引数・パッケージが出る原因を、読ませたもの・版・確かめ・環境の境界の順に切り分け、振り分け先を決められる。
    - **いつ引くか**：存在しない関数や引数を自信満々に使われたとき、インストールできないパッケージ名を書かれたとき、実行する環境で使えないライブラリを足されたとき。
    - **前提**：<!-- link:begin why-hallucinations -->[ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)<!-- link:end -->、<!-- link:begin knowledge-cutoff -->[知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)<!-- link:end -->

<!-- textlint-disable -->
別名：存在しない API・架空のパッケージ・package hallucination
<!-- textlint-enable -->

存在しない関数やパッケージを使う症状は、Claude が実在しない名前を、実在するもののように書く現象である。名前と形が本物らしいので、読むだけでは見分けにくい。実行するかインストールして初めて分かる。

## よくある形 {#forms}

この症状は、次の 3 つの形で現れる。どれも「存在しない」と言えるが、原因と手が違う。

- **存在しない関数や引数**：名前も引数の並びも本物らしいが、実行すると `AttributeError` や型エラーになる。別の版にだけある関数、別のライブラリの関数、名前だけ似た関数が混ざる。
- **インストールできないパッケージ名**：`pip install` や `npm install` が「見つからない」で失敗する。実在しない名前は、後から誰かがその名前を登録する可能性があり、失敗したから無害とは限らない。
- **実行する環境で使えないライブラリ**：名前は実在するが、実行する環境が許さない。Kaggle の自動化を試した体験記では、エージェントがオフラインの制約に反して `pip install` を書き足し、存在しないデータセットを指定した（根拠：弱、単独の体験記）。

どれも、分からないときに「分からない」と言わず、それらしい名前で答案を埋める挙動の現れである。山を張る受験生が、知らない設問にそれらしい答えを書くのに近い。仕組みは <!-- link:begin why-hallucinations#guess-pays -->[ハルシネーションはなぜ起きるか › 分からなくても答えるほうが得になる訓練](../basics/why-hallucinations.md#guess-pays)<!-- link:end --> を見る。

規模の目安を挙げる。16 のモデルが書いた 576,000 件のコードで、存在しないパッケージ名を含む割合は、商用モデルで 5.2% 以上、オープンソースモデルで 21.7% だった（根拠：強）。Spracklen らの 2024 年公開の研究（USENIX Security 2025）の結果である。調べた世代は当時のモデルで、現行の Claude にそのまま当てはめない。

2026 年 4 月の追試は、Claude Sonnet 4.6・Haiku 4.5 を含む 5 モデルで、割合が 4.62% から 6.10% に狭まったと報告した。5 モデルが同じ名前を作った例は 127 件あった（根拠：弱、独立研究者 1 名の論文で査読状況は不明）。SIMD の命令を LLM に書かせた研究もある。失敗の約 41% は、存在しないか名前の違う intrinsic によるコンパイルエラーだった（根拠：中、SIMD に限る）。

## 原因を安く確かめる順 {#diagnosis}

原因を切り分ける節である。確かめる手間が小さい順に 4 つ並べた。上から見て、当てはまったところで止めてよい。

1. **読ませたか（見えていない）**
    - 何を見る：その関数やパッケージの定義・公式文書が、会話の中に入っているか。
    - どう確かめる：Claude に、その関数の定義を読んだ場所（ファイルと行、文書の節）を示させる。示せなければ、記憶で書いている。
    - 当てはまったら：読ませるファイルを指す（下の「原因ごとの対処へ」）。
2. **版が合っているか（知識の古さ）**
    - 何を見る：自分の環境のライブラリの版と、書かれた API が属する版。
    - どう確かめる：lockfile の版と、公式の変更履歴・リファレンスを見比べる。関数が別の版で消えたか、名前が変わったか、モデルの知識より新しい版でできたかを確かめる。
    - 当てはまったら：版と公式文書を渡して書かせる。背景は <!-- link:begin knowledge-cutoff#what-helps -->[知識カットオフと「今」を知らない問題 › 何に効くか](../basics/knowledge-cutoff.md#what-helps)<!-- link:end --> を、最新の情報を知らない症状として扱うなら <!-- link:begin doesnt-know-latest#diagnosis -->[最新の情報を知らない › 原因を安く確かめる順](doesnt-know-latest.md#diagnosis)<!-- link:end --> を見る。
3. **動かして確かめたか（確かめていない）**
    - 何を見る：書いた後に、実行・型の検査・テストを通したか。通した結果が報告に載っているか。
    - どう確かめる：「動くはず」という説明ではなく、実行したコマンドと出力を求める。型のある言語なら、編集のたびに型エラーが返る環境にしておくと、存在しない API を早く見つけられる（公式文書で確認済み）。
    - 当てはまったら：テストを先に書かせるか、報告ではなく証拠を求める（行き先は下の「原因ごとの対処へ」の表）。
4. **入れる前の境界があるか（境界がない）**
    - 何を見る：パッケージを足す操作が、確認なしに通っていないか。実行環境の制約（オフライン、使えるパッケージが決まっている、など）を Claude が知っているか。
    - どう確かめる：書かれたパッケージ名を、公式のパッケージ管理のページで検索して、実在・公開元・公開日を見る。環境の制約が、依頼や `CLAUDE.md` に書いてあるかを見る。
    - 当てはまったら：依存のパッケージを入れる前の確かめ方を扱うページを見る（行き先は下の「原因ごとの対処へ」の表）。

LLM が使う依存関係のリスクは、OWASP の LLM 向け Top 10（2025 年版）でも、サプライチェーンの項目として挙げられている。人の側にも落とし穴がある。Claude の答えを、実行や検索で確かめずに採用してしまうことである。診断の全体は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> と <!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end --> にある。

## 原因ごとの対処へ {#to-fixes}

診断で当てはまった原因ごとの、対処のページを次の表に示す。対処の本体は各ページにある。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)<br>code intelligence プラグイン（LSP）（準備中） |
| 確かめていない | テストを先に書かせる（準備中）<br>[報告ではなく証拠を求める](../verify/evidence-not-reports.md) |
| 境界がない | [MCP・プラグイン・スキルを入れる前の確認 › 依存のパッケージを入れる前に（存在しない名前・後から登録された名前）](../safety/vetting-extensions.md#dependencies) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#example}

!!! example "判断例：オフラインの提出環境向けのコードに、存在しない引数と知らないパッケージが混ざった"
    - **状況**：オフラインで実行する提出環境向けのコードを、Claude に書かせた。返ってきたコードには、ライブラリに存在しない引数と、見覚えのないパッケージの `pip install` が混ざっていた。
    - **迷う候補**：A は「存在するものだけを使って、書き直して」とまとめて頼む。B は 2 つの誤りを別の原因として切り分け、別の手で直す。
    - **選んだもの**：B。引数の誤りは、「読ませたか」と「動かして確かめたか」（診断の 1 と 3）で確かめて、定義を読ませてから書き直させ、実行した結果を求める。パッケージは、「入れる前の境界があるか」（診断の 4）に当たるので、環境の制約を依頼に書いたうえで、足す前に相談させる。
    - **理由**：A でも一度は直るが、「存在するもの」を Claude 自身が判断するので、同じ記憶頼みの判断を繰り返す。原因が違えば、効く手も違う。引数は読ませることで防ぎ、パッケージは環境の境界で防ぐ。

## 予防は依頼と仕組みに移す {#prevention}

毎回気をつけるより、依頼の形と環境に移すほうが続く。

- **読んでから書かせる**：使う関数の定義を読んだ場所を、書く前に挙げさせる。公式のプロンプトの手引きも、開いていないコードについて推測せず、答える前にファイルを読ませるよう勧めている。依頼の雛形を次に示す。

<!-- gen:begin snippet uses-nonexistent-apis/read-then-write -->
<!-- textlint-disable -->

??? example "雛形：読んでから書かせる依頼"

    ```markdown
    `<機能の説明>` を実装して。

    - 使うライブラリは `<ライブラリ名>`、版は `<lockfile に書かれた版>`。
    - 書く前に、使う関数と引数の定義を `<ソースのパス>` か、渡した公式文書から読んで、読んだ場所（ファイルと行）を一覧にして。
    - 定義が見つからなかったものは使わず、「見つからなかった」と書いて。名前を推測で補わないで。
    - 新しいパッケージが要るときは、入れる前に名前と理由を報告して。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.12。

<!-- textlint-enable -->
<!-- gen:end snippet uses-nonexistent-apis/read-then-write -->

- **動かした結果で受け取る**：型の検査とテストを通した出力を、完了の条件にする。型のある言語では <!-- link:begin code-intelligence-plugins -->code intelligence プラグイン（LSP）（準備中）<!-- link:end --> で、定義へのジャンプと編集後の型エラーの報告を使える。
- **新しい依存は入れる前に相談させる**：理由と相談の基準を `CLAUDE.md` に書く。その雛形を次に示す。例外を許さないなら、`CLAUDE.md` ではなく、設定やフックで強制する。

<!-- gen:begin snippet uses-nonexistent-apis/new-dependency-rule -->
<!-- textlint-disable -->

??? example "雛形：依存を足す前に相談させる CLAUDE.md の節"

    ```markdown
    ## 依存パッケージの追加

    - 新しいパッケージを足す前に、名前・用途・足す理由を報告して、私の返事を待つ。実在するかを、記憶ではなくパッケージ管理の公式のページで確かめた結果も添える。
    - 理由：パッケージの名前は、実在しないものや後から登録されたものを、それらしく書いてしまうことがある。
    - 実行環境の制約：`<オフライン、使えるパッケージの一覧など>`。この制約で足せないものは、足さずに代わりの案を相談する。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.12。

<!-- textlint-enable -->
<!-- gen:end snippet uses-nonexistent-apis/new-dependency-rule -->

- **実行環境の制約を先に伝える**：オフラインか、使えるパッケージは何かを、依頼か `CLAUDE.md` に書く。

これらが効かない場面もある。定義を読ませても、読んだ内容の取り違えは起きる。パッケージ名を公式のページで確かめても、実在する名前が意図に合うとは限らない。読んだ場所を示させるのは、確かめる手間を減らす手であり、確かめの代わりではない。重要な事実の照合は <!-- link:begin fact-checking -->[事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)<!-- link:end --> に任せる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs](https://arxiv.org/abs/2406.10279)：arXiv（Spracklen, Joseph ほか）・英語・確認日 2026-11-04
- [The Range Shrinks, the Threat Remains: Re-evaluating LLM Package Hallucinations on the 2026 Frontier-Model Cohort](https://arxiv.org/abs/2605.17062)：arXiv（Churilov, Aleksandr ほか）・英語・確認日 2026-11-04
- [SimdBench: Benchmarking Large Language Models for SIMD-Intrinsic Code Generation](https://arxiv.org/abs/2507.15224)：arXiv（He, Yibo ほか）・英語・確認日 2026-11-04
- [Bugs in Large Language Models Generated Code: An Empirical Study](https://arxiv.org/abs/2403.08937)：arXiv（Tambon, Florian ほか）・英語・確認日 2026-11-04
- [\[Claude Code\] Kaggle完全自動化で金メダルは獲れるのか？（前編：最強の推論パイプライン構築と見えない壁）](https://zenn.dev/lluminai_tech/articles/7bd423768740a0)：Zenn（lluminai\_tech）・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [OWASP Top 10 for LLMs 2025: Key Risks and Mitigation Strategies](https://www.invicti.com/blog/web-security/owasp-top-10-risks-llm-security-2025)：Invicti・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)
- [知識カットオフと「今」を知らない問題](../basics/knowledge-cutoff.md)

**次に読む**

- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- code intelligence プラグイン（LSP）（準備中）
- テストを先に書かせる（準備中）
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)

**関連**

- [事実を確かめる（引用・照合・best-of-N）](../verify/fact-checking.md)
- [MCP をつなぐ](../extend/connecting-mcp.md)
- 仕様を自分で読み、AI に誤読を指摘させる（準備中）
- [最新の情報を知らない](doesnt-know-latest.md)
- [もっともらしい嘘・出典の誤り](plausible-falsehoods.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
