---
id: glossary
title: 用語集（独自の用語と公式の訳語）
nav_title: 用語集
aliases: [用語の定義, 訳語の対応, 表記の約束, 表記の正規形, 独自の用語]
type: guide
field: start
chapter: 辞書として引く
order: 60
priority: 必須
summary: この辞典の独自の用語（お願いと鍵・六つの「ない」など）の意味と公式の用語との対応、公式の日本語版に合わせた訳語と表記の正規形を引ける。
signs:
  - {type: goal, text: この辞典の言葉が、公式の文書のどの言葉に当たるか知りたい}
  - {type: goal, text: アプリと Claude Code で名前が同じ機能が、同じものか知りたい}
wave: 1
prerequisites: []
related: [term-index, how-to-use, four-principles, six-causes, request-vs-lock, roadmap, five-questions-before-delegating#autonomy-stages, how-memory-works, using-auto-memory, skills-in-the-app#migrated-styles, output-style-modes]
volatility: 中
sections:
  - {title: 訳語の決め方, anchor: translation-policy}
  - {title: 独自の用語と公式の用語, anchor: own-terms}
  - {title: 公式で表記が割れている語, anchor: split-terms}
  - {title: 面ごとに似た名前の機能, anchor: same-names-across-surfaces}
  - {title: 用語の定義, anchor: definitions}
stage: stub
updated: 2026-11-04
---

## 訳語の決め方 {#translation-policy}

## 独自の用語と公式の用語 {#own-terms}

この辞典が付けた呼び名と、辞典の読み方の語である。公式の文書にある別の言い方があるときは、右の欄に添える。

| 語 | 意味 | 公式の用語・備考 |
| --- | --- | --- |
| <span id="request-lock"></span>お願い・鍵 | お願いは、Claude が読んで判断する指示（プロンプト・CLAUDE.md・スキル）で、守られる保証がない。鍵は、Claude の判断によらずハーネスが実行する制御（フック・deny ルール・管理設定）で、効く範囲と条件の中では毎回必ず効く | お願い＝非決定論的な指示、鍵＝決定論的な制御。解説は request-vs-lock |
| <span id="four-specifics"></span>具体性の 4 点 | 依頼に書く対象・状況・完了の形・倣う手本の 4 点。欠けている点が、次に書き足すものになる | 公式の Best practices の助言（ファイルの名指し・症状・直った状態の先出し・倣うパターンの指定）を、この辞典が 4 点にまとめた呼び名 |
| <span id="workaround"></span>回避策 | 原理を満たす正式な仕組みやモデルの力が足りない間に、言葉・手順・自作のスクリプトで補った手段。仕組みが入るか、モデルが言われなくてもできるようになると役目を終える | 古くなった助言の台帳で、行ごとに「どの原理の回避策だったか」を添える |
| <span id="ledger-states"></span>台帳の状態（撤回・置換・条件付き） | 撤回は、使えないか使わないほうがよい助言。置換は、同じ目的を別の正式な仕組みや新しい名前が担うもの。条件付きは、今も効くが前提が変わったもの | 本文の定義は古くなった助言の台帳のページを正とする |
| <span id="surface"></span>面 | Claude を使う入口の種類（アプリ・Claude Code・API）。同じ目的でも、面によって手段が違う | 公式では surfaces、またはプロダクト名で呼ぶ |
| <span id="evidence-mark"></span>根拠の印 | 研究や数値を根拠にする主張の後に付ける印（根拠：強・中・弱、類推、推論・実践例なし） | 読み方は how-to-use の「根拠の強さの書き分け」 |
| <span id="coming-soon"></span>題名（準備中） | まだ公開していないページを指す所に、リンクにせず出す表記。相手を公開すると、リンクに変わる | |
| <span id="page-stage"></span>ページの段階 | ページの書き進み具合（骨格・下書き・検証済み・完成）。レベルとは別のもの | front matter の `stage` |
| <span id="level"></span>レベル | ページが想定する読者の委任の段階（使う・整える・任せる・仕組みにする・回す）。ページの段階とは別のもの | front matter の `level` |
| <span id="symptom-page"></span>症状のページ | 困りごと（例：指示が守られない）から引く型のページ。原因を安く確かめる順に並べ、直し方のページへ送る | 型 `symptom` |
| <span id="field"></span>分野 | ナビゲーションの大きな区分 | front matter の `field` |
| <span id="chapter"></span>章 | 分野の中の区切り。症状のページだけを章ごとに並べた分野が「症状辞典」である | front matter の `chapter` |

## 公式で表記が割れている語 {#split-terms}

## 面ごとに似た名前の機能 {#same-names-across-surfaces}

| 名前 | Claude Code | アプリ（claude.ai） |
| --- | --- | --- |
| 出力スタイル／Styles | 出力スタイル：セッション全体の役割・口調・応答の形を変える指示 | Styles：応答の調子と形式を選ぶ機能。2026-06-01 にスキルへの移行が告知された |

この2つは別の機能である。

## 用語の定義 {#definitions}

本文で使う語のうち、独自でなく、意味を決めておくと迷う語である。

| 語 | 意味 | 備考 |
| --- | --- | --- |
| <span id="harness"></span>ハーネス | モデルのまわりでツールを動かし、モデルが見る文脈を管理する層。Claude Code 本体がこれにあたる | |
| <span id="output-style"></span>出力スタイル | Claude Code で、セッション全体の役割・口調・応答の形を変える指示 | claude.ai の Styles とは別の機能 |
| <span id="fork"></span>fork | 親の会話とシステムプロンプトを丸ごと引き継いで分かれるサブエージェント。出力スタイルが効く | |
| <span id="managed-settings"></span>管理設定 | 組織が配り、利用者のファイルでは上書きできない設定 | 表記は prh に従い「管理設定」 |
| <span id="compaction"></span>圧縮 | 長い会話を要約に置き換えること | API の機能名 compaction は英語のまま |
| <span id="resident"></span>常駐 | 読み込まれた後、会話の間コンテキストに居続けること | |
| <span id="bypass"></span>回り込み | 鍵で止められた操作の代わりに、止められていない別の手段で同じ結果を得ること | 縛りすぎの害の一つ |
| <span id="turn"></span>ターン | 依頼を送ってから最後の返事までの 1 区切り。途中でツールを何度も呼ぶ | |
| <span id="aside"></span>ツールの合間の一言 | Claude がツールを呼ぶ前後に書く短い文。最後の返事とは別で、Stop フックは見ない | |
| <span id="block-back"></span>差し戻し | フックが Claude に返事のやり直しを求め、ターンを終えさせないこと | `decision` を `block` にする形 |
| <span id="supporting-files"></span>補助ファイル | スキルのフォルダの中で `SKILL.md` 以外に置く資料やスクリプトのファイル。資料は Claude が読むまでコンテキストに入らない。スクリプトは、読ませずに実行だけさせる | 公式の supporting files はスクリプトも含む。この辞典の writing-skills は、資料とスクリプトを分けて書く |

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- 用語索引と旧名の対応（準備中）
- この辞典の引き方（準備中）
- 四つの原理と比例則（見せる・確かめる・縛る・握る）（準備中）
- 失敗の二つの軸と診断の入口（準備中）
- お願いと鍵（決定論的か、非決定論的か）（準備中）
- ロードマップ（委任の段階別）（準備中）
- 任せ方の段階と、無人で走らせる前の五つの問い › 任せ方の段階（準備中）
- アプリのメモリ（仕組み・範囲・消し方と止め方）（準備中）
- 自動メモリ（準備中）
- アプリでスキルを使う › 移された Styles（準備中）
- 出力スタイルで応答の仕方を切り替える（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
