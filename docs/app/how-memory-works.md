---
id: how-memory-works
title: アプリのメモリ（仕組み・範囲・消し方と止め方）
nav_title: アプリのメモリ
aliases: [Memory, Claude のメモリ, 過去チャットの検索, Search and reference chats, chat search, Memory FAQ, メモリの Pause と Reset]
type: feature
field: app
chapter: 指示と記憶
order: 40
level: 整える
priority: 必須
surfaces: [app]
principle: [見せる, 確かめる]
prevents: [散らかっている, 境界がない]
summary: アプリのメモリが何を、いつ、どの範囲で覚えるかが分かり、見る・直す・消す・止める手段を選べる。会話を消してもメモリは残ることと、過去チャットの検索との違いも分かる。
signs:
  - {type: goal, text: 前の会話で話したことを覚えていてほしい}
  - {type: goal, text: 前の会話の内容を探して使わせたい}
  - {type: goal, text: 何を覚えられているかを確かめたい}
  - {type: goal, text: 間違って覚えられた内容を直したい}
  - {type: goal, text: しばらく記憶を使わせずに話したい}
prerequisites: []
related: [unexpected-memories, incognito-chats, where-to-put-instructions, using-projects, using-auto-memory, where-your-data-goes, tidy-the-desk#in-the-app, feature-to-api-mapping]
tracks: [app-memory, chat-search, incognito]
outdated_advice: [memory-daily-summary]
sources: [hc-memory, hc-incognito, hc-release-notes, lukyanenko-rogii-geosteering-kaggle]
volatility: 高
sections:
  - {title: 何が、いつ保存されるか, anchor: what-is-saved}
  - {title: アカウントのメモリとプロジェクトのメモリ, anchor: scope}
  - {title: 過去チャットの検索との違い, anchor: chat-search}
  - {title: 覚えた内容を見る・直す（棚卸し）, anchor: manage}
  - {title: 会話を消しても残るもの, anchor: deleted-chats}
  - {title: 消し方と止め方（Pause・Reset・会話ごとのオフ・シークレットチャット）, anchor: turning-off}
  - {title: 古くなった助言, anchor: outdated-advice}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：アプリのメモリが何を、いつ、どの範囲で覚えるかが分かり、見る・直す・消す・止める手段を選べる。
    - **止められるもの**：保存済みの項目は、見て、直して、消せる。使うこと自体も止められる。止められないのは、項目が会話とは別に残ることである。会話を消してもメモリの項目は消えない。
    - **いつ引くか**：前の会話で話したことを覚えていてほしいとき。何を覚えられているかを確かめて、間違いを直したいとき。しばらく記憶を使わせずに話したいとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：Memory・Claude のメモリ・過去チャットの検索・Search and reference chats・chat search・Memory FAQ・メモリの Pause と Reset
<!-- textlint-enable -->

アプリのメモリは、Claude が会話の中で覚えておくべき事柄を項目として保存し、後の会話で読む機能である。毎回の背景説明は減るが、中身が見えないと間違いが残り、範囲が曖昧だと別の話題が混ざる。このページは、メモリの中身を見せて確かめる手段と、範囲を分ける手段を引くためのものである。

## 何が、いつ保存されるか {#what-is-saved}

メモリは、会話の後にまとめて要約する方式ではない。話している間に、Claude がトピックごとの項目として保存し、読み、更新する。Claude が自分で保存するほか、「覚えて」と頼んでも保存される。

保存の対象になるカテゴリは、公式の説明では次の 4 つである。

- 役割とプロジェクト
- 仕事や生活に関わる人
- コミュニケーションや技術面の好み
- 進行中のプロジェクトの詳細

機微な話題は、既定では保存されない。健康・人種・宗教・政治・性自認などがこれに当たる。設定の `Include sensitive topics in memory` でオプトインでき、その場合は保存のたびに通知が出る。政府発行の ID 番号・犯罪歴・金融口座番号・在留資格は、設定に関係なく保存されない。

メモリが既定で有効かどうかは、プランで違う。既定は、<!-- fact:begin memory-default-by-plan -->Free・Pro・Max・Ultra は既定で有効。Team と Enterprise は owner が使えるかを決め、各メンバーは自分で有効にするまで無効（2026-11-04 時点）<!-- fact:end -->。組織向けのプランでは、管理者が使えるかを決め、各メンバーが自分で有効にするまでは無効である。ほかの AI からの取り込みと書き出しもあるが、experimental なので手順は扱わない。

覚えさせたい事柄は、「覚えて」と頼むと確実に残せる。ただし、Claude が「覚えた」と返したことは申告である。実際に保存された項目は、設定の Topics（保存された項目の一覧）で確かめる（原理は「見せる・確かめる」）。

<!-- gen:begin snippet how-memory-works/remember-request -->
<!-- textlint-disable -->

??? example "雛形：覚えてほしいことを頼み、訂正する"

    ```markdown
    次のことを、これからの会話でも使えるように覚えて。
    - <覚えさせる事柄を 1 つずつ書く。例：レビューのコメントは日本語で、結論から書く>

    覚えたら、保存した内容を 1 行ずつ言い直して。

    ---

    さっき覚えた「<間違った内容>」は違う。正しくは「<正しい内容>」。覚え直して。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet how-memory-works/remember-request -->

メニューの名前や既定値は、2026 年に二度大きく変わった。このページは公式の説明に沿って書いてあり、画面と違うときは公式の文書を優先する。

## アカウントのメモリとプロジェクトのメモリ {#scope}

メモリには、アカウント全体のものと、プロジェクトごとのものがある。会話の場所によって、読まれるメモリが違う。

| 会話の場所 | 読まれるメモリ |
| --- | --- |
| プロジェクトの外 | アカウントのメモリ |
| プロジェクトの中 | そのプロジェクトのメモリと、アカウントのメモリ。ほかのプロジェクトのメモリは読まれない |
| シークレットチャット | 履歴にもメモリにも残らない。プロジェクトの外でだけ開ける |

プロジェクトの外の会話が、プロジェクトのメモリを読むかどうかは、確かめていない。

プロジェクトの間を完全に分けたいときは、そのプロジェクトの設定で `Use account memory` をオフにする。これで、プロジェクトの間に境界がないことによる混ざりを防げる。プロジェクトをどう切るかは <!-- link:begin using-projects#scope -->[プロジェクトの使いどころ › プロジェクトを切る単位（1つに1つの目的）](using-projects.md#scope)<!-- link:end --> にある。

Cowork とは、Cowork がクラウドで動くときだけメモリを共有する。

メモリは、Claude が自分で書き溜める記録である。毎回守らせたい前提や形式は、メモリではなく指示に書く。置き場所の選び方は <!-- link:begin where-to-put-instructions#how-to-choose -->[アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル） › どこに置くかの選び方](where-to-put-instructions.md#how-to-choose)<!-- link:end --> にある。Claude Code の自動メモリは別の機能で、確かめ方は <!-- link:begin using-auto-memory#review -->[自動メモリ › 誤った記録の見直し](../extend/using-auto-memory.md#review)<!-- link:end --> にある。

別の会話やプロジェクトの内容が混ざる原因を切り分けたいときは、<!-- link:begin unexpected-memories#diagnosis -->[別の会話やプロジェクトの内容が混ざる › 原因を安く確かめる順](../symptoms/unexpected-memories.md#diagnosis)<!-- link:end --> から入る。

## 過去チャットの検索との違い {#chat-search}

過去チャットの検索は、メモリとは別の機能である。Claude が必要と判断したとき、過去の会話を検索して引く。会話の中では、道具の呼び出しとして表示される。

使えるプランと面は、<!-- fact:begin chat-search-plans -->Pro・Max・Ultra・Team・Enterprise（web・Desktop・Mobile）。customer-managed encryption keys を使う Enterprise では使えない（2026-11-04 時点）<!-- fact:end -->。検索の範囲は、プロジェクトの外の会話と、各プロジェクトの中の会話である。オフにするには、設定の `Search and reference chats` を切る。

| 比べる点 | メモリ | 過去チャットの検索 |
| --- | --- | --- |
| 持っているもの | Claude が抽出した項目 | 過去の会話そのもの |
| 読まれ方 | 新しい会話で使われる | 必要なときに、検索の呼び出しとして引かれる |
| 止め方 | Pause・会話ごとのオフ・項目の削除・Reset | `Search and reference chats` のトグル |

使い分けは、この辞典の推奨として次のとおりにする。

- 好みや前提のように、毎回効いてほしい事柄は、メモリに任せる。
- 特定の会話で決めた中身を探して使いたいときは、過去チャットの検索に任せる。

メモリを止めても検索は止まらず、検索を止めてもメモリは止まらない。片方だけを止めたつもりで、もう片方から古い内容が出てくることがある。

## 覚えた内容を見る・直す（棚卸し） {#manage}

メモリの中身は、`Settings > Your Claude` の `Your memory` で `Manage` を開くと、Topics として見られる。ここで項目を閲覧・編集・削除できる。

覚えた内容は、定期的に見直す。誤った結論が項目に入ると、後の会話がそれを前提に進み、気づきにくいからである。見直しの手順は次のとおりである。

1. Topics を開き、項目を上から読む。
2. 間違い・古くなったもの・今の作業と関係ないものを探す。
3. 間違いは編集で直し、不要なものは削除する。
4. 直したあと、新しい会話で関係する話題を振り、期待どおりに使われるかを確かめる。

棚卸しの根拠は、アプリではなく Claude Code の自動メモリでの経験談である。誤った結論が自動の記憶に書かれ、後の実験を汚し、手動で消すしかなかったという報告がある（類推・根拠：弱。単独の経験談で、アプリのメモリを調べたものではない）。アプリのメモリでも同じ型の失敗が起こりうるので、見直しの習慣は安い備えになる。

間違って覚えられた内容を直すのは、会話の中で「それは違う」と言うだけでは足りない。直すのは Topics で行い、直った項目を目で確かめる。

## 会話を消しても残るもの {#deleted-chats}

会話を削除しても、その会話から作られたメモリの項目は消えない。項目は会話とは別に保存されているからである。

消したはずの内容を Claude が覚えているときは、次の順で消す。

1. 会話を削除する。
2. Topics を開き、その会話から作られた項目を探して削除する。
3. 内容が広く残っていそうなら、Pause や Reset を検討する（手段の違いは、節「消し方と止め方」にある）。

会話を消したあとで過去チャットの検索に何が出るかは、確かめていない。送ったデータが保持される期間や学習への扱いは、メモリとは別の問いで、<!-- link:begin where-your-data-goes#retention -->[送ったデータの行方（学習・保持期間） › 残る期間](../safety/where-your-data-goes.md#retention)<!-- link:end --> で確かめる。

## 消し方と止め方（Pause・Reset・会話ごとのオフ・シークレットチャット） {#turning-off}

メモリを止める手段は、止める範囲と、取り消せるかどうかが違う。範囲の狭いものから選ぶ。

| 手段 | 止まるもの | 残るもの | 取り消せるか |
| --- | --- | --- | --- |
| 項目の削除 | その項目 | ほかの項目 | 戻せるかは確かめていない |
| 会話ごとのオフ | その会話でのメモリ | 既存の項目 | その会話の途中では戻せない |
| Pause | メモリの使用と追加の両方 | 既存の項目 | 項目は残る。再開の手順は確かめていない |
| Reset | すべて | なし。プロジェクトのメモリも消える | 取り消せない |
| シークレットチャット | その会話の履歴とメモリへの記録 | 保持される分がある | 会話ごとに決まる |

- 会話ごとのオフ：最初のメッセージを送る前に、`+` メニューの Memory をオフにする。後から切り替えられないと説明されているので、送ったあとには使えない。
- Pause：既存のメモリを残したまま、使用と追加の両方を止める。しばらく記憶を使わせずに話したいときの手段である。
- Reset：プロジェクトのメモリを含めて全削除する。取り消せないので、実行前に Topics を見て、残したい項目を控える。
- シークレットチャット：履歴とメモリに残らない。詳しい扱いは次の 2 か所にある。残らないもの・残るものは <!-- link:begin incognito-chats#retention -->[シークレットチャット（記録を残さない会話） › 残らないもの・残るもの](incognito-chats.md#retention)<!-- link:end -->、使えない機能は <!-- link:begin incognito-chats#limits -->[シークレットチャット（記録を残さない会話） › 使えない機能](incognito-chats.md#limits)<!-- link:end --> にある。

!!! example "判断例：今夜だけメモリを使わせたくない"
    - **状況**：個人的な相談を今夜だけしたい。普段のメモリは混ぜたくないが、会話は後で見返したい。
    - **迷う候補**：シークレットチャットで開く。会話ごとにメモリをオフにして開く。
    - **選んだもの**：会話ごとのオフ。
    - **理由**：シークレットチャットは履歴に残らないので、後で見返せない。会話ごとのオフなら、メモリを使わせず、履歴は残せる。履歴にも残したくない相談なら、シークレットチャットのほうを選ぶ。

どの手段でも、止めた結果は Topics と、実際の返答で確かめる。止めたつもりでも、別の仕組みである過去チャットの検索から内容が出ることがある。

## 古くなった助言 {#outdated-advice}

「メモリは会話の後に日次で要約される」「反映は翌日になる」「要約を待つ」という助言は、古い。今のメモリは、話している間に項目として保存される。項目は設定の Topics で見て、直して、消せる。台帳の行は <!-- link:begin outdated-advice-ledger#memory-daily-summary -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#memory-daily-summary)<!-- link:end --> にある。

自分の画面がどちらの体験かは、設定に Memory の項目があるか、`Generate memory from chats` があるかで見分ける。契約によっては、新しい体験が来ていない組織もある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use Claude’s chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)：Anthropic・英語・確認日 2026-11-04
- [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04
- [How AI agents helped me win a Kaggle silver medal — and how they failed me](https://andlukyane.com/blog/rogii-geosteering-kaggle)：Andrey Lukyanenko・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [シークレットチャット（記録を残さない会話）](incognito-chats.md)

**関連**

- [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)
- [アプリの指示の置き場所（Claude への指示・プロジェクト・メモリ・スキル）](where-to-put-instructions.md)
- [プロジェクトの使いどころ](using-projects.md)
- [自動メモリ](../extend/using-auto-memory.md)
- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- [机を整える：新鮮さ・巻き戻し・書き出し・委任 › アプリでの整え方](../context/tidy-the-desk.md#in-the-app)
- [アプリの機能と API の概念の対応表](../api/feature-to-api-mapping.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
