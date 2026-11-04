---
id: shared-artifacts-and-files
title: 共有リンクと公開アーティファクトの扱い
aliases: [会話の共有, 公開リンク, 公開された artifact, 共有の取り消し, 公開された artifact とファイルの扱い]
type: concept
field: safety
chapter: データの扱い
order: 60
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [握る]
prevents: [境界がない]
pitfalls: []
scenes: [文章, チーム, コンテスト]
summary: 会話やアーティファクトを招待や公開リンクで共有したとき、何が誰に見え、取り消して消えるものと消えないものが分かる。他人が公開したものは、知らない送り主から届いたファイルと同じに疑う。
signs:
  - {type: goal, text: 会話やアーティファクトを人に見せたい}
  - {type: symptom, text: 共有したリンクに、見せたくない内容が入っていた}
  - {type: situation, text: 他人が公開したアーティファクトを開こうとしている}
prerequisites: [artifacts-overview]
related: [where-your-data-goes, what-feedback-sends, entrusted-data, shared-projects-and-org-skills, files-and-code-execution, prompt-injection-in-practice, artifacts-as-apps, competition-day-operations]
tracks: [artifacts, chat-sharing]
sources: [hc-share-chats, hc-share-people, hc-share-public, hc-files, hc-connectors, hc-artifacts]
volatility: 中
sections:
  - {title: 共有のしかた（特定の人への招待・公開リンク・組織の中だけの共有）, anchor: how-to-share}
  - {title: 共有されるもの（その時点の写しと、更新のしかた）, anchor: snapshot}
  - {title: 見られる人と、プランによる違い, anchor: who-can-see}
  - {title: 取り消せるもの・取り消せないもの, anchor: revoke}
  - {title: 他人が公開したものを開くとき, anchor: opening-others}
  - {title: 何に効くか, anchor: what-it-prevents}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：共有した会話やアーティファクトが誰に何として見え、取り消して消えるものと消えないものを区別できる。
    - **いつ引くか**：会話やアーティファクトを人に見せたいとき。共有したリンクに見せたくない内容が入っていたとき。他人が公開したアーティファクトを開こうとしているとき。
    - **前提**：<!-- link:begin artifacts-overview -->[アーティファクト（会話の中で作る文書・スライド・デザイン）](../app/artifacts-overview.md)<!-- link:end -->

<!-- textlint-disable -->
別名：会話の共有・公開リンク・公開された artifact・共有の取り消し・公開された artifact とファイルの扱い
<!-- textlint-enable -->

共有リンクと公開アーティファクトの扱いは、見せる相手を選ぶ操作と、一度出したものが手元から離れる範囲を知ることの 2 つに分かれる。招待は相手を限れるが、公開リンクは知っている人なら誰でも開ける。リンクを止めても、すでに写された内容は消せない。他人が公開したものを開く側では、知らない送り主から届いたファイルと同じに疑う。

## 共有のしかた（特定の人への招待・公開リンク・組織の中だけの共有） {#how-to-share}

会話の共有のしかたは、特定の人への招待、公開リンク、組織の中だけの共有の 3 通りである。どれを使えるかはプランで決まる。

- **特定の人への招待**：相手のメールアドレスに招待を出す。既定の共有のしかたで、招待はそのメールアドレスでしか開けない。転送しても、ほかの人には開かない。相手に Claude のアカウントがなければ、登録へ案内される。
- **公開リンク**：リンクを知っていれば、アカウントがなくても誰でも見られる。
- **組織の中だけの共有**：組織向けのプランでは、組織のドメインのメールへの招待か、組織の全員への共有に限られる。公開リンクは作れない。管理者は共有を止め、共有を一覧して取り消し、監査ログで確かめられる。

=== "アプリ"

    会話の共有は、claude.ai の Web から行う。モバイルのアプリからは、まだ共有できない。共有された会話は、どの端末でも開ける。

    共有のメニューで、招待か公開かを選ぶ。組織の中での共有の権限の考え方は <!-- link:begin shared-projects-and-org-skills#shared-projects -->アプリをチームで使う（共有プロジェクト・組織のスキル） › プロジェクトの共有と権限（準備中）<!-- link:end --> と考え方がつながる。

=== "Claude Code"

    Claude Code には、会話を共有する機能がない。`/share` は共有のリンクを作らず、会話を Anthropic に送る。取り違えやすい点は <!-- link:begin what-feedback-sends#share-is-bug -->[/feedback・トランスクリプトの共有で送られるもの › /share は共有のリンクではない](what-feedback-sends.md#share-is-bug)<!-- link:end --> にある。

    Claude Code から公開できるのは、`Artifact` ツールで作ったアーティファクトである。公開リンクで共有できる。組織向けのプランでは、組織の中が既定で、公開は管理者が許可したときだけである。

共有の操作は画面の名前が変わりやすい。操作の細部は公式の文書で確かめる。この辞典は、何が見え、何が消せないかの側を扱う。

## 共有されるもの（その時点の写しと、更新のしかた） {#snapshot}

共有されるのは、共有した時点の写しである。それまでのメッセージとアーティファクトが入り、共有の後に足した発言は入らない。

- **見る側にできること**：見るだけである。続きの会話、自分のアカウントへの複製、ファイルのダウンロードはできない。
- **入らないもの**：添付したファイルは入らない。例外は組織の中だけの共有で、こちらは添付したファイルも入る。MCP や connector から取った生のデータも出ない。見えるのは Claude の最終的な応答だけである。
- **更新のしかた**：招待で共有した会話は、更新の操作で最新の発言を反映する。公開リンクは、共有をやめて共有し直す。

写しなので、共有した後に会話へ秘密を貼っても、すでに出したリンクには出ない。逆に、共有する前の発言は全部入る。共有する前に、会話の最初から読み返す。そこに貼った鍵・顧客の名前・社内の情報が、見せたい相手に見せてよいものかを確かめる。

## 見られる人と、プランによる違い {#who-can-see}

見られる人は、共有のしかたで決まる。プランによって、使えるしかたと制限が違う。

| 共有のしかた | 見られる人 | 向き |
| --- | --- | --- |
| 特定の人への招待 | 招待したメールアドレスの持ち主 | 見せたい相手が決まっているとき |
| 公開リンク | リンクを知っている全員 | 不特定の読者に読ませるとき |
| 組織の中だけの共有 | 組織の中の人 | チーム内の共有 |

- **招待**：全プランで使える。開かれない招待は一定の期間で切れる。1 日に招待できる人数にも上限がある。
- **公開リンク**：個人向けのプランだけである。組織向けのプランでは作れない。
- **ファイルを含む会話の公開**：コードの実行とファイル作成で作ったファイルを含む会話は、個人向けのプランでは公開リンクで共有できない。安全のための措置と明記されている。ファイルの扱いは <!-- link:begin files-and-code-execution#outputs -->[ファイル作成とコード実行 › 作ったファイルの受け取り方](../app/files-and-code-execution.md#outputs)<!-- link:end --> にある。

プランごとの可否、期間、上限の数は変わりやすい。契約しているプランで何が使えるかは、公式の共有の記事で確かめる。

!!! example "判断例：1 人にだけ見せたい会話"
    - **状況**：レビューを頼みたい同僚 1 人に、アーティファクトを作った会話を見せたい。
    - **迷う候補**：公開リンクを作ってチャットで送る。または、同僚のメールアドレスに招待を出す。
    - **選んだもの**：招待を出す。
    - **理由**：公開リンクは、リンクを貼られた先で誰でも開ける。相手が 1 人に決まっているなら、招待のほうが見られる人を限れる。招待は転送しても他人には開かない。ただし、相手の側で写される分は止められない。

## 取り消せるもの・取り消せないもの {#revoke}

共有の取り消しで止められるのは、リンクや招待の効力である。すでに相手の手元にある写しは止められない。

- **取り消せるもの**：共有のメニューで公開から非公開に戻すか、招待を止める。設定のプライバシーにある共有した会話の管理で、共有中の会話を一覧し、1 件ずつ共有をやめられる。止めるとリンクはすぐに開かなくなる。会話を消すと、写しも消える。
- **取り消せないもの**：すでに見た人の手元にある内容、コピー、スクリーンショット、外部の保存（アーカイブ）。リンクを貼られた先は、リンクを止めても自分では消せない。公開リンクのページは検索の対象から外す印を付け、一覧やサイトマップを出さず、推測できない長い URL にしている。ただし、これは見つかりにくくする工夫であり、見せてよいという保証ではない。

公式も、公開リンクは公開したものとして扱うよう勧めている。取り消す前に誰かが写したものは、取り消しの対象の外である。見せたくない内容が入っていたと気づいたときの順は次のとおりである。

1. 共有をやめる。リンクはすぐに開かなくなる。
2. 入っていた内容が鍵・パスワード・トークンなら、共有をやめただけでは足りない。発行元で無効にして、作り直す。
3. 顧客や第三者のデータなら、扱いを決めた約束の側の手順に従う。判断の枠組みは <!-- link:begin entrusted-data#whose-data -->[預かったデータ・規約付きのデータを AI に渡してよいか › 誰のデータで、何が決まっているか](entrusted-data.md#whose-data)<!-- link:end --> にある。

送った会話が学習に使われる条件や残る期間は、共有とは別の話である。<!-- link:begin where-your-data-goes#consumer-vs-commercial -->[送ったデータの行方（学習・保持期間） › 個人のプランと商用のプラン](where-your-data-goes.md#consumer-vs-commercial)<!-- link:end --> で確かめる。

競技の期間中は、共有に関する守りを先に固める。private のリポジトリを使い、共有リンクを無効にし、公開されるページへ出力しない。これは主催者の規則ではなく、実践者の一致による運用の目安である（類推）。規則そのものは <!-- link:begin checking-ai-rules -->[学校・組織・コンテストの規則（類型と確認表）](checking-ai-rules.md)<!-- link:end --> で確かめ、本番の流れは <!-- link:begin competition-day-operations -->本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態）（準備中）<!-- link:end --> にある。

## 他人が公開したものを開くとき {#opening-others}

他人が公開したアーティファクトやリンクは、知らない送り主から届いたファイルと同じに扱う。公開された場所にあることは、中身の安全の証拠にならない。

- **開く前**：誰が作ったか、どこで見つけたかを確かめる。出所の分からないものは、重要な作業をしている環境や、権限の大きいアカウントで開かない。
- **開いた後**：入力欄に秘密を入れない。接続や権限の許可を求められても、何を許可するのかを読んでから決める。アプリとして動くアーティファクトが誰の権限と枠で動くかは <!-- link:begin artifacts-as-apps#whose-account -->アーティファクトを小さなアプリにする › 共有したときに誰の権限と枠で動くか（準備中）<!-- link:end --> で確かめる。
- **Claude に読ませるとき**：他人が公開したページや文書の中に、Claude への指示が仕込まれていることがある。読ませた内容の中の指示は、データとして扱う。経路と防ぎ方は <!-- link:begin prompt-injection-in-practice#channels -->[プロンプトインジェクションの実際 › 指示が入ってくる経路](prompt-injection-in-practice.md#channels)<!-- link:end --> にある。
- **ダウンロードしたコードやファイル**：中身を読む前に実行しない。

!!! example "判断例：SNS で見つけた公開アーティファクト"
    - **状況**：便利そうな集計ツールのアーティファクトが SNS で公開されている。自分の業務のデータで試したい。
    - **迷う候補**：そのまま業務のデータを入れて試す。または、作り物のデータで試し、挙動を確かめてから決める。
    - **選んだもの**：作り物のデータで試す。
    - **理由**：公開された場所にあることは、安全の証拠にならない。送り主が不明のファイルと同じに、権限と入力するデータを絞って始める。

## 何に効くか {#what-it-prevents}

共有リンクと公開アーティファクトの扱いが防ぐ原因は「境界がない」である。共有のリンクは、会話の中身を手元から外へ出す境界の操作である。会話に何が入っているかを意識しないまま押すと、見せる相手と見せる内容の線が引かれないまま出ていく。

原理は「握る」である。誰に何を見せるか、いつ取り消すかの決定を、共有の既定や気軽さに任せず、人の側で握る。見せる内容は共有の前に読み、見せる相手は共有のしかたで選び、取り消せない部分は最初から出さない。他人が公開したものを開く側でも、開くか、何を入力するかの決定を、人が握る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Share and unshare chats](https://support.claude.com/en/articles/10593882-share-and-unshare-chats)：Anthropic・英語・確認日 2026-11-04
- [Share a chat with specific people](https://support.claude.com/en/articles/16762496-share-a-chat-with-specific-people)：Anthropic・英語・確認日 2026-11-04
- [Public links for shared chats](https://support.claude.com/en/articles/16762437-public-links-for-shared-chats)：Anthropic・英語・確認日 2026-11-04
- [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)：Anthropic・英語・確認日 2026-11-04
- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)：Anthropic・英語・確認日 2026-11-04
- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [アーティファクト（会話の中で作る文書・スライド・デザイン）](../app/artifacts-overview.md)

**関連**

- [送ったデータの行方（学習・保持期間）](where-your-data-goes.md)
- [/feedback・トランスクリプトの共有で送られるもの](what-feedback-sends.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](entrusted-data.md)
- アプリをチームで使う（共有プロジェクト・組織のスキル）（準備中）
- [ファイル作成とコード実行](../app/files-and-code-execution.md)
- [プロンプトインジェクションの実際](prompt-injection-in-practice.md)
- アーティファクトを小さなアプリにする（準備中）
- 本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態）（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
