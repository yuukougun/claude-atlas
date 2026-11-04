---
id: large-context-window
title: 広いコンテキストウィンドウとの付き合い方
aliases: [1M コンテキスト, 1M context, '[1m] のモデル', 長いコンテキスト]
type: concept
field: models
chapter: effort・思考・コンテキスト
order: 60
level: 整える
priority: 推奨
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [散らかっている]
pitfalls: []
summary: 窓が広くなり溢れる心配は減ったが、関係のない文脈が答えの質と費用を下げる点は変わらないことが分かる。やめてよい節約と、続ける片付けを分けられる。
signs:
  - {type: goal, text: コンテキストが広いモデルなら、会話の長さを気にしなくてよいのか知りたい}
  - {type: situation, text: コンテキストを節約する古いコツが、今も要るのか分からない}
prerequisites: [attention-budget]
related: [when-to-start-fresh, compact-and-auto-compact, context-rot, always-on-costs, what-uses-up-limits, current-models]
tracks: [context-window, compaction]
outdated_advice: [save-context-for-200k, subagents-to-save-context]
sources: [cc-docs-best-practices, cc-docs-context-window, api-docs-context-windows]
volatility: 高
sections:
  - {title: やめてよいこと, anchor: what-to-stop}
  - {title: 続けること, anchor: what-to-keep}
  - {title: 長い文脈の費用, anchor: cost-of-long-context}
  - {title: 何に効くか, anchor: effects}
  - {title: 誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：窓が広くなって減ったのは溢れる心配で、関係のない文脈が質と費用を下げる点は変わらない。
    - **いつ引くか**：コンテキストが広いモデルなら会話の長さを気にしなくてよいのか知りたいとき。節約する古いコツが今も要るのか分からないとき。
    - **前提**：<!-- link:begin attention-budget -->[コンテキストウィンドウと注意の予算](../basics/attention-budget.md)<!-- link:end -->

<!-- textlint-disable -->
別名：1M コンテキスト・1M context・[1m] のモデル・長いコンテキスト
<!-- textlint-enable -->

広いコンテキストウィンドウとは、1 回の会話に載せられる量が大きいモデルの窓のことである。溢れることはまれになったが、会話に何でも残してよいことにはならない。このページは、窓が小さかったころの節約のうち、やめてよいものと続けるものを分ける。

## やめてよいこと {#what-to-stop}

窓が小さかったころの節約は、溢れを避けるために身についた。長い作業の途中で、次のような決まりを今も守っていないか見直したい。

- 窓の溢れを恐れて、ファイルの読み込みを控える。
- 数ターンごとに、会話を自分で要約させる。
- 調べものは、窓を守るためだけにサブエージェントへ出す。

公式の Best practices は、改稿でコンテキストを最大の制約として積極的に管理することを「やめてよいこと」の表に入れた。理由は、多くの現行モデルが広い窓を持ち、圧縮も自動で、溢れることがまれだからである。窓の大きさはモデルと面で違うので、自分が使うモデルの値は <!-- link:begin current-models#lineup -->[現行モデルの一覧と位置づけ › 系統ごとの位置づけ（表）](current-models.md#lineup)<!-- link:end --> と公式の文書で確かめる。この変更の時期と今どうするかは、台帳の <!-- link:begin outdated-advice-ledger#save-context-for-200k -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#save-context-for-200k)<!-- link:end --> にある。

サブエージェントは、窓を守るためだけには使わなくなった。今も向くのは、作業を並べるとき、うるさい出力を本筋から離すとき、独立したレビューをさせるときである。どれも追加のトークンがかかる。台帳の <!-- link:begin outdated-advice-ledger#subagents-to-save-context -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#subagents-to-save-context)<!-- link:end --> を見る。

溢れへの備えは、面ごとに違う。

=== "アプリ"

    code execution が有効なとき、上限が近づくと古いメッセージを要約して会話を続ける。チャット履歴そのものは保存され、要約後も参照できる。

=== "Claude Code"

    窓が埋まる前に自動で圧縮される。圧縮で何が残るかは仕組みごとに違い、詳しくは <!-- link:begin compact-and-auto-compact#auto-compact -->[/compact と自動圧縮 › 自動圧縮で起きること](../context/compact-and-auto-compact.md#auto-compact)<!-- link:end --> にある。Claude Code の動作は WSL・Linux の CLI を基準に書いており、ほかの OS や IDE 拡張の動作は未確認である。

=== "API"

    窓の大きさはモデルで決まる。会話をどう続けるかは呼び出す側の設計で、API の圧縮の機能は別に用意されている。公式の Context windows の文書で確かめる。

!!! example "判断例：CLAUDE.md の窓の節約ルールを残すか"
    - **状況**：数か月前に書いた CLAUDE.md に、「ファイルは必要な部分だけ読む」「毎回、作業の後に要約する」とある。今のモデルは窓が広い。
    - **迷う候補**：全部消す。窓の節約が目的の行だけ消し、質や費用のために効く行は残す。
    - **選んだもの**：窓の節約が目的の行だけ消す。
    - **理由**：溢れを避ける目的の決まりは、溢れがまれになった今は手間だけが残る。一方、関係のない読み込みを減らす決まりは、答えの質と費用のために今も効く（理由は「続けること」の節にある）。行ごとに、何を防ぐ決まりかを見る。

## 続けること {#what-to-keep}

続けるのは、関係のない文脈を会話に残さない片付けである。窓が広いと溢れないが、広い机にものを積むほど、大事な一枚が見つけにくくなる点は変わらない。

- **話題が変わったら新しい会話にする**：関係のない作業の間の `/clear` は、今も勧められている。理由は溢れの回避ではない。焦点の合った文脈のほうが、答えがよく安いからである。合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。
- **残したい作業は書き出してから消す**：新しくする前に書き出すものの一覧は、<!-- link:begin when-to-start-fresh#before-clearing -->[新しい会話を始めるタイミング › 新しくする前に残すもの](../context/when-to-start-fresh.md#before-clearing)<!-- link:end --> にある。
- **圧縮は焦点を指示して使う**：`/compact` に残したい焦点を渡す。手順は <!-- link:begin compact-and-auto-compact#focused-compact -->[/compact と自動圧縮 › /compact に焦点を指示する](../context/compact-and-auto-compact.md#focused-compact)<!-- link:end --> にある。
- **席を外す前に知っておく**：大きな会話を長く放置すると、プロンプトキャッシュが切れる前に要約される（idle compaction）。詳しくは <!-- link:begin compact-and-auto-compact#idle-compaction -->[/compact と自動圧縮 › 席を外すとき（idle compaction と cache 切れ）](../context/compact-and-auto-compact.md#idle-compaction)<!-- link:end --> を見る。
- **常駐するものを小さく保つ**：CLAUDE.md やツールの一覧は毎回乗る。減らし方は <!-- link:begin always-on-costs#reduce -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 減らす順](../context/always-on-costs.md#reduce)<!-- link:end --> にある。

!!! example "判断例：別件の依頼を同じ会話で続けるか"
    - **状況**：認証のバグを調べた長い会話の続きに、まったく別の帳票出力の修正を頼みたい。窓にはまだ十分な空きがある。
    - **迷う候補**：空きがあるので同じ会話で続ける。調べた結果を書き出して、新しい会話で始める。
    - **選んだもの**：認証の調査で残したい結論を書き出して、新しい会話で始める。
    - **理由**：空きがあっても、認証の調査の読み込みは帳票の修正には関係がなく、答えの質を下げ、毎回の送り直しの費用を増やす。溢れるかどうかではなく、関係があるかどうかで判断する。

## 長い文脈の費用 {#cost-of-long-context}

長い会話の費用は、窓が広くなっても消えない。会話の履歴は、1 回ごとの依頼で全体が送り直される。毎回、全履歴を読み直す受験者のようなものである。会話が長いほど、1 回あたりに処理する量が増える。

- **使用量**：長いセッションで使用量が増える仕組みと、自分の場合の確かめ方は <!-- link:begin what-uses-up-limits#long-sessions -->[上限を早く使う要因 › 長いセッションで増える理由](../cost/what-uses-up-limits.md#long-sessions)<!-- link:end --> にある。
- **料金の仕組み**：窓の大きさ、長い入力の単価、同じ文章がトークンで何個になるかは、モデルで違う。選ぶ前に <!-- link:begin current-models#lineup -->[現行モデルの一覧と位置づけ › 系統ごとの位置づけ（表）](current-models.md#lineup)<!-- link:end --> と公式の料金のページで確かめる。値はここに書かない。
- **キャッシュ**：席を外した後の最初の依頼は、キャッシュが切れていると送り直しの費用がかさむ。idle compaction はこの場面を和らげる仕組みでもある。

窓が広いことは、費用を気にしなくてよいことを意味しない。会話を新しくする、常駐を小さくする、焦点を絞って圧縮するのは、どれも費用を下げる手段でもある。

## 何に効くか {#effects}

このページの内容は、原理の「見せる」と、原因の「散らかっている」に関わる。

- **見せる**：必要な情報を、必要なときに、見える形で渡す。窓が広くても、見せたいものが関係のない情報に埋もれると、見えているのと同じにならない。片付けることは、見せることの一部である。理由は <!-- link:begin attention-budget#effects -->[コンテキストウィンドウと注意の予算 › 何に効くか：見せることと、散らかっていること](../basics/attention-budget.md#effects)<!-- link:end --> にある。
- **散らかっている**：関係のない読み込み、失敗した試みの残り、古い議論が会話に残る状態を指す。入力が長くなるほど、また似ているが違う情報が混ざるほど、答えの質が下がりやすい。詳しくは <!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end --> を見る。窓が広くなったことで、溢れによる失敗は減ったが、散らかりによる失敗は残る。

## 誤解 {#misconceptions}

- **「窓が広いから、会話はいくら長くてもよい」**：溢れないことと、中身をよく使えることは別である。関係のない情報が増えるほど、大事な情報への注意は薄くなる。<!-- link:begin attention-budget#misconceptions -->[コンテキストウィンドウと注意の予算 › 誤解](../basics/attention-budget.md#misconceptions)<!-- link:end --> を見る。
- **「節約のコツはすべて古くなった」**：窓を守るためだけの節約が古くなった。質と費用のための片付けは古くなっていない。
- **「`/clear` すれば上限も戻る」**：新しい会話にしても、利用枠は戻らない。<!-- link:begin when-to-start-fresh#what-does-not-reset -->[新しい会話を始めるタイミング › 新しくしても戻らないもの（上限・記憶）](../context/when-to-start-fresh.md#what-does-not-reset)<!-- link:end --> を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Explore the context window](https://code.claude.com/docs/en/context-window)：Anthropic・英語・確認日 2026-11-04
- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [コンテキストウィンドウと注意の予算](../basics/attention-budget.md)

**関連**

- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [/compact と自動圧縮](../context/compact-and-auto-compact.md)
- [context rot と紛らわしい情報](../basics/context-rot.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)
- [現行モデルの一覧と位置づけ](current-models.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
