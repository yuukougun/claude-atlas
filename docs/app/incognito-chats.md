---
id: incognito-chats
title: シークレットチャット（記録を残さない会話）
aliases: [Incognito chats, Incognito]
type: feature
field: app
chapter: 指示と記憶
order: 50
level: 整える
priority: 推奨
surfaces: [app]
principle: [見せる]
prevents: [境界がない, 散らかっている]
summary: 履歴にもメモリにも残さずに相談でき、記憶に影響させずに試せる。それでも残るものと、使えない機能が分かる。
signs:
  - {type: goal, text: 記録を残さずに相談したい}
  - {type: goal, text: 記憶や履歴に影響させずに試したい}
prerequisites: [how-memory-works]
related: [where-your-data-goes, entrusted-data, files-and-code-execution, what-each-surface-cannot-do]
tracks: [incognito]
sources: [hc-incognito, hc-memory, hc-release-notes]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 最小の使い方, anchor: usage}
  - {title: 残らないもの・残るもの, anchor: retention}
  - {title: 使えない機能, anchor: limits}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：履歴とメモリを避けて相談でき、記憶に影響させずに試せる。
    - **いつ引くか**：記録を残さずに相談したいとき。記憶や履歴に影響させずに試したいとき。
    - **強制力**：記録を保存しないのはアプリの仕組みで、依頼で頼むお願いではない。ただし、バックエンドの保持と管理者への見え方は止められない。
    - **前提**：<!-- link:begin how-memory-works -->[アプリのメモリ（仕組み・範囲・消し方と止め方）](how-memory-works.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Incognito chats・Incognito
<!-- textlint-enable -->

シークレットチャットは、claude.ai のアプリで開く、記録を残さない一時的な会話である。履歴とメモリには保存されない。それでも「何も残らない」わけではない。残るものを知ったうえで使い分ける。

## 使いどころ {#when}

シークレットチャットが効くのは、会話の記録が後から記憶や履歴に混ざる問題である。メモリは、過去の会話から作られて次の会話に効く。ここに残したくない話題や、残したくない試行がある場面で使う。

- **記録を残さずに相談したい**：個人的な相談や、メモリに入ってほしくない話題を、履歴とメモリから外して話せる。これは、境界がない（話題どうしが混ざる）という原因を防ぐ。
- **記憶に影響させずに試したい**：試しの頼み方や使い捨ての質問で、履歴が散らかるのを防げる。さらに、始めた時点で既存のメモリを使わないので、いつもの記憶に引っ張られない素の応答も見られる。これは、散らかっているという原因を防ぐ。

どちらも、Claude が参照する記憶を会話の単位で絞る使い方である。メモリの仕組みと、止め方の全体は <!-- link:begin how-memory-works#turning-off -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 消し方と止め方（Pause・Reset・会話ごとのオフ・シークレットチャット）](how-memory-works.md#turning-off)<!-- link:end --> が持つ。

!!! example "判断例：転職の相談を、メモリに残したくない"
    - **状況**：転職を考えていることを相談したい。ただし、この話題を今後の会話の前提にされたくない。
    - **迷う候補**：メモリそのものを Pause する／この会話だけメモリをオフにする／シークレットチャットで話す。
    - **選んだもの**：プロジェクトの外の単発の相談なので、シークレットチャットで話す。
    - **理由**：メモリを止めると、他の会話の記憶も止まる。シークレットチャットなら、この 1 回だけを履歴とメモリから外せる。この会話を後で見返したいなら、残る通常のチャットのほうが合う。

## 最小の使い方 {#usage}

=== "アプリ"

    プロジェクトの外で新しいチャットを開くと、画面の右上にゴーストのアイコンが出る。これを押すと、シークレットチャットになる（2026-11-05 時点の Help Center の記述。画面の見た目は変わりうる）。

    1. 新しいチャットを、プロジェクトの外で開く。
    2. ゴーストのアイコンを押す。黒い枠と「Incognito chat」の表示が出る。
    3. 普通に話す。
    4. 終わったら右上の「x」で閉じる。閉じると、同じ会話は再び開けない。

    プロジェクトの中のチャットでは、シークレットチャットは使えない。代わりに、最初のメッセージの前に「+」メニューで Memory をオフにする方法がある。

シークレットチャットは、始めたあとで通常のチャットに変えることもできない。残したくなったら、必要な内容を自分でコピーして取っておく。

## 残らないもの・残るもの {#retention}

シークレットチャットで残らないものと、残るものを分けて覚える。

**残らない（または使われない）もの**

- チャット履歴。一覧に出ず、閉じると開き直せない。
- メモリ。この会話の内容は、今後のメモリの項目に入らない。
- 過去チャットの検索。他の会話から、この会話の内容は引かれない。違いは <!-- link:begin how-memory-works#chat-search -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 過去チャットの検索との違い](how-memory-works.md#chat-search)<!-- link:end --> にある。
- 学習。この会話は学習に使われない。
- 月次のふり返り（monthly recap）の対象。

**残るもの**

- バックエンドでの保持。履歴に出なくても、一定の期間は保持される。
- 組織での見え方。組織向けのプランでは、管理者が受け取るデータのエクスポートに含まれる。さらに上位のプランでは Compliance API の対象にもなる。
- プロフィールの情報。個人用の設定などは、シークレットチャットの中でも Claude が使える。

保持の期間は、次のとおりである。

- 既定の保持：<!-- fact:begin incognito-retention-period -->未確認<!-- fact:end -->

組織向けのプランでは、組織の保持の設定でこれより長くなることがある。期間は変わりやすいので、数字は上の目印の値を見る。学習に使われる条件と、プランごとの保持の全体は <!-- link:begin where-your-data-goes#retention -->[送ったデータの行方（学習・保持期間） › 残る期間](../safety/where-your-data-goes.md#retention)<!-- link:end --> が持つ。

つまりシークレットチャットは、ユーザー自身の画面とメモリから記録を外すもので、サービスの側の保持や、組織の管理者の見え方を消すものではない。預かったデータや規約付きのデータを渡してよいかは、シークレットチャットにしても変わらない。判断は <!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](../safety/entrusted-data.md#contracted-surfaces)<!-- link:end --> に従う。

## 使えない機能 {#limits}

シークレットチャットでは、通常のチャットで使える機能の一部が使えない。決まりは次の 3 つである。

- **ファイルの作成とコードの実行ができない**：新しい Claude の体験を使っていても、シークレットチャットは前の体験で開く。そのため、表計算や文書のファイルを作らせることも、コードを実行させることもできない。頼み方と環境の話は <!-- link:begin files-and-code-execution -->[ファイル作成とコード実行](files-and-code-execution.md)<!-- link:end --> にある。
- **プロジェクトの外でしか使えない**：プロジェクトの資料や指示を使う作業には向かない。
- **通常のチャットへ変換できず、閉じると開き直せない**：結果を残したいときは、閉じる前に自分で写す。

ファイルを作らせたい相談は、シークレットチャットでは進まない。その場合は、通常のチャットで、載せる内容を絞って頼む。面ごとに使えない機能の早見表は <!-- link:begin what-each-surface-cannot-do#table -->[面ごとにできないこと（早見表） › 早見表（面 × 機能）](../surfaces/what-each-surface-cannot-do.md#table)<!-- link:end --> で引ける。

## 比べる相手 {#compare}

記憶や記録を扱う手段は、残る範囲で選ぶ。

| 手段 | 向く場面 |
| --- | --- |
| シークレットチャット | プロジェクトの外の単発の相談や試行。履歴にもメモリにも残したくない |
| 会話ごとにメモリをオフ | プロジェクトの中のチャットで、その会話だけメモリに入れたくない |
| メモリの Pause | しばらくの間、すべての会話でメモリを増やしたくない |
| 記憶の見直し・消去 | すでに覚えられた内容を直したい、消したい |

表の手段の手順と違いは、メモリのページが持つ。目的別の入口は次のとおりである。

- 止め方：<!-- link:begin how-memory-works#turning-off -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 消し方と止め方（Pause・Reset・会話ごとのオフ・シークレットチャット）](how-memory-works.md#turning-off)<!-- link:end -->
- 見直し：<!-- link:begin how-memory-works#manage -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 覚えた内容を見る・直す（棚卸し）](how-memory-works.md#manage)<!-- link:end -->
- 会話を消しても残る点：<!-- link:begin how-memory-works#deleted-chats -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 会話を消しても残るもの](how-memory-works.md#deleted-chats)<!-- link:end -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [アプリのメモリ（仕組み・範囲・消し方と止め方）](how-memory-works.md)

**関連**

- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)
- [ファイル作成とコード実行](files-and-code-execution.md)
- [面ごとにできないこと（早見表）](../surfaces/what-each-surface-cannot-do.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)：Anthropic・英語・確認日 2026-11-04
- [Use Claude’s chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
