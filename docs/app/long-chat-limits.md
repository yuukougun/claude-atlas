---
id: long-chat-limits
title: 長い会話の自動のコンテキスト管理と長さの上限
nav_title: 長い会話と長さの上限
aliases: [自動 context 管理, automatic context management, length limit, 会話の長さの制限]
type: feature
field: app
chapter: 資料と長い会話
order: 70
level: 整える
priority: 推奨
surfaces: [app]
principle: [見せる]
prevents: [散らかっている]
scenes: [文章, 調べもの]
summary: アプリの長い会話で、上限が近づくと何が自動で要約され何が残るかが分かり、長さの上限に当たったときの対処を選べる。
signs:
  - {type: situation, text: claude.ai で一つの長い会話を使い続けている}
  - {type: goal, text: アプリの長い会話で、自動の要約が働くと何が残るか知りたい}
prerequisites: [rereads-whole-history]
related: [tidy-the-desk#in-the-app, when-to-start-fresh, forgets-in-long-chats, what-survives-compaction, compact-and-auto-compact, files-and-code-execution, what-uses-up-limits, handoff-documents, feature-to-api-mapping]
tracks: [app-context-management, context-window]
sources: [hc-context-window, hc-usage-limits, hc-release-notes]
volatility: 高
sections:
  - {title: 上限が近づくと何が起きるか, anchor: auto-management}
  - {title: 要約のあとに残るもの, anchor: what-remains}
  - {title: 何に効くか, anchor: effects}
  - {title: 長さの上限に当たったとき, anchor: at-the-limit}
  - {title: 効かない場面と落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：アプリで会話が上限に近づくと古い発言が自動で要約され、履歴は残ると分かる。
    - **いつ引くか**：claude.ai で 1 つの長い会話を使い続けていて、自動の要約で何が残るか、長さの上限に当たったらどうするかを知りたいとき。
    - **前提**：<!-- link:begin rereads-whole-history -->[毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)<!-- link:end -->

<!-- textlint-disable -->
別名：自動 context 管理・automatic context management・length limit・会話の長さの制限
<!-- textlint-enable -->

長い会話の自動のコンテキスト管理は、claude.ai などのアプリで、会話が長くなりすぎる前に Claude が古い発言を要約して続ける仕組みである。要約が働く条件、要約のあとに残るもの、長さの上限に当たったときの公式の対処を、このページで引ける。

## 上限が近づくと何が起きるか {#auto-management}

アプリの会話は、Claude が一度に読める量（コンテキストウィンドウ）に収まる必要がある。会話がその上限に近づくと、自動のコンテキスト管理が古い発言を要約し、要約を足がかりに会話を続ける。利用者が操作しなくても、会話は止まらずに先へ進む。

動く条件は、公式の記事に次のとおり書かれている。

- **働く条件**：コードの実行が有効なときに働く。コードの実行がオフの会話でも同じように働くとは、確かめられていない。
- **履歴の扱い**：要約したあとも、チャット履歴そのものは保存される。要約後も Claude が参照できる。
- **働き始める時点**：上限に近づくと働く。閾値は公開されていない。
- **窓の大きさ**：モデルとプランで違う。応答用の領域が確保されるので、実際に使える長さは窓の大きさより少し短い。

コードの実行の設定は、<!-- link:begin files-and-code-execution#when -->[ファイル作成とコード実行 › 使いどころ](files-and-code-execution.md#when)<!-- link:end --> で扱う。窓の大きさの数値は本文に書かず、数値ファイルに置く（この節は数値なしで読める）。

!!! note "Claude Code や API の圧縮とは別の仕組み"
    - **同じ名前でも別物**：Claude Code の圧縮（compaction）と API の圧縮は、このページの自動の管理とは別の機能である。
    - **混ぜない**：Claude Code の圧縮で何が残るかは <!-- link:begin what-survives-compaction -->[圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)<!-- link:end --> にあるが、アプリの要約にそのまま当てはまるとは限らない。

## 要約のあとに残るもの {#what-remains}

要約のあとに残るものは、2 つに分けて考える。

- **履歴として残るもの**：チャット履歴そのものは保存される。要約で履歴が消えるわけではないので、あとから会話を読み返せる。
- **Claude が続きで使う材料**：古い発言は要約に置き換わる。要約でどの細部が落ちるかは、公開されていない。細部が落ちうると見て、残したいものは会話の外に置く。

要約で細部が落ちたかを確かめるには、会話の初めに出した条件を Claude に言い直させる。言い直しが食い違ったら、その条件を新しく書き足す（推論・実践例なし）。

残したい規則や条件の置き場所は、<!-- link:begin handoff-documents#where -->[handoff 文書と document-and-clear › 置き場所（圧縮で消えない所）](../context/handoff-documents.md#where)<!-- link:end --> にまとめてある。会話をまたいで残したいものは、ファイルや文書に書き出す。

## 何に効くか {#effects}

このページの機能が効くのは、原理「見せる」の側である。会話が長くなっても、Claude が読める範囲に必要な情報を収め続ける。

一方で、防ぐ原因「散らかっている」に対しては、この機能だけでは足りない。要約は会話を短くするが、今の作業に要る情報へ焦点を絞る仕組みではない。無関係な情報が溜まり、前提を忘れたり答えが雑になったりする症状は、<!-- link:begin forgets-in-long-chats -->[長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)<!-- link:end --> で原因を切り分ける。

自動の要約は、溢れを避ける安全弁として働く。答えの質と費用のために会話を整える判断は、利用者の側で行う。整え方は <!-- link:begin tidy-the-desk#in-the-app -->[机を整える：新鮮さ・巻き戻し・書き出し・委任 › アプリでの整え方](../context/tidy-the-desk.md#in-the-app)<!-- link:end --> に、新しい会話に移る合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。

なお、要約が働くほど長い会話は、利用上限も多く使う。長い会話が枠を早く減らす理由は <!-- link:begin what-uses-up-limits#long-sessions -->[上限を早く使う要因 › 長いセッションで増える理由](../cost/what-uses-up-limits.md#long-sessions)<!-- link:end --> にある。毎回、全履歴を読み直す仕組みが背景にあるので、前提の <!-- link:begin rereads-whole-history -->[毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)<!-- link:end --> もあわせて読む。

## 長さの上限に当たったとき {#at-the-limit}

自動の要約が間に合っても、長さの上限に当たることがある。たとえば、とても大きい最初の発言を送ったときである。長さの上限は、1 つの会話に収められる量の上限である。時間の枠ごとに戻る利用上限とは別のものなので、切り分けて考える。

長さの上限に当たったときの公式の対処は、次のとおりである。

1. **プロジェクトを使う**：資料や指示をプロジェクトに置いて作業する。
2. **プロジェクトの指示を短くする**：指示が長いと、会話に使える分が減る。
3. **プロジェクトのファイルを減らす**：作業に要るものだけを残す。
4. **拡張思考をオフにする**：考える分の消費を減らす。
5. **effort を下げる**：高い effort はトークンを多く使う。
6. **ツールを減らす**：ツールとコネクタは消費が大きい。

上の対処は、利用上限を早く減らす要因の一覧と重なる。自分の場合に何が効いているかを確かめるには、<!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](../cost/what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> を使う。

対処を試しても続けるのが難しいときは、会話を新しくするか、作業の状態を文書に書き出して移る。続けるか新しくするかの分かれ目は <!-- link:begin when-to-start-fresh -->[新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<!-- link:end --> に、文書に書かせる項目は <!-- link:begin handoff-documents#four-items -->[handoff 文書と document-and-clear › 書かせる四項目](../context/handoff-documents.md#four-items)<!-- link:end --> にある。新しくしても、利用上限と記憶の設定は戻らない（<!-- link:begin when-to-start-fresh#what-does-not-reset -->[新しい会話を始めるタイミング › 新しくしても戻らないもの（上限・記憶）](../context/when-to-start-fresh.md#what-does-not-reset)<!-- link:end -->）。

!!! example "判断例：長い調べものの会話が重くなった"
    - **状況**：資料を貼りながら、1 つの会話で長い調べものを続けている。返答が遅くなり、序盤で決めた条件が反映されなくなってきた。
    - **迷う候補**：自動の要約に任せて同じ会話を続ける／条件と途中結果を書き出して新しい会話に移る。
    - **選んだもの**：条件と途中結果を文書に書き出し、新しい会話でその文書を読み込ませて再開する。
    - **理由**：要約で細部が落ちうる。序盤の条件が反映されないのは、細部落ちか、無関係な情報の溜まりのどちらかだと考えられる。どちらであっても、文書に条件を固定すれば再開が確実になる。

## 効かない場面と落とし穴 {#pitfalls}

- **コードの実行がオフのとき**：自動の管理はコードの実行が有効なときに働く。オフの会話では自動の要約が働かないとみて、長さの上限に当たる前に自分で会話を整える。オフのときの挙動は確かめられていない。
- **履歴が残ることと、続きで使えることは別**：履歴は保存されて参照できる。ただ、要約のあとの続きで Claude がどこまで細部を使えるかは、別の話である。
- **プランによる違い**：窓の大きさはプランとモデルで違う。公式の 2 つの記事は、有料のプランに限るかの書き方が違う。自分のプランで働くかは、画面と公式の記事で確かめる。
- **要約が働くほど利用枠を使う**：長い会話は上限に当たる前に、利用上限を多く使う。
- **要約の閾値は当てにしない**：どの時点で働くかは公開されていない。ここから逆算して会話の長さを決めない。

アプリの自動の管理は、Claude Code の `/compact` や自動圧縮とは別である。手動で焦点を指示して要約する操作は <!-- link:begin compact-and-auto-compact#focused-compact -->[/compact と自動圧縮 › /compact に焦点を指示する](../context/compact-and-auto-compact.md#focused-compact)<!-- link:end --> にある（Claude Code の機能）。

## 比べる相手 {#compare}

- **API の対応する概念**：アプリの自動の要約が API のどの概念に当たるかは、<!-- link:begin feature-to-api-mapping#table -->[アプリの機能と API の概念の対応表 › 対応表](../api/feature-to-api-mapping.md#table)<!-- link:end --> の対応表で引ける。
- **Claude Code の圧縮**：別の機能である。何が残るかは <!-- link:begin what-survives-compaction -->[圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)<!-- link:end --> に、操作は <!-- link:begin compact-and-auto-compact -->[/compact と自動圧縮](../context/compact-and-auto-compact.md)<!-- link:end --> にある。
- **新しい会話・書き出し**：自動の要約に任せず、利用者が整える方法である。<!-- link:begin handoff-documents -->[handoff 文書と document-and-clear](../context/handoff-documents.md)<!-- link:end --> が、要約の損失を避けたい長い作業に向く。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [毎ターン全履歴を読み直す](../basics/rereads-whole-history.md)

**関連**

- [机を整える：新鮮さ・巻き戻し・書き出し・委任 › アプリでの整え方](../context/tidy-the-desk.md#in-the-app)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [長い会話で前提を忘れる・雑になる](../symptoms/forgets-in-long-chats.md)
- [圧縮（compaction）で何が残り、何が消えるか](../basics/what-survives-compaction.md)
- [/compact と自動圧縮](../context/compact-and-auto-compact.md)
- [ファイル作成とコード実行](files-and-code-execution.md)
- [上限を早く使う要因](../cost/what-uses-up-limits.md)
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- [アプリの機能と API の概念の対応表](../api/feature-to-api-mapping.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)：Anthropic・英語・確認日 2026-11-04
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
