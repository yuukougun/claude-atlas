---
id: where-your-data-goes
title: 送ったデータの行方（学習・保持期間）
aliases: [学習に使われるか, データの保持期間, Help improve our AI models, オプトアウト]
type: concept
field: safety
chapter: データの扱い
order: 40
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [握る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, 文章, チーム]
summary: 送った会話やコードが学習に使われる条件と残る期間を、個人のプランと商用のプランに分けて確かめられる。手元に残る記録は、これとは別に考える。
signs:
  - {type: goal, text: 入力した内容が学習に使われるか知りたい}
  - {type: goal, text: 記録を残さずに相談したい}
  - {type: goal, text: 消した会話が、提供元にいつまで残るか知りたい}
prerequisites: []
related: [incognito-chats, what-feedback-sends, entrusted-data, shared-artifacts-and-files, default-safety-settings, how-memory-works, unexpected-memories, when-requests-are-refused, choosing-an-org-plan, data-analysis, office-paperwork, check-billing-path]
tracks: [incognito, app-memory]
sources: [cc-docs-data-usage, privacy-long-store-data, anthropic-news-updates-our-consumer-terms, hc-incognito, hc-memory, api-docs-message-threads]
volatility: 中
sections:
  - {title: 個人のプランと商用のプラン, anchor: consumer-vs-commercial}
  - {title: 学習への利用の設定, anchor: training-setting}
  - {title: 残る期間, anchor: retention}
  - {title: 手元に残る記録, anchor: local-transcripts}
  - {title: 何に効くか, anchor: what-it-prevents}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：送った会話やコードが学習に使われる条件と提供元に残る期間を、個人のプランと商用のプランに分けて確かめられる。
    - **いつ引くか**：入力した内容が学習に使われるか知りたいとき、消した会話の残る期間を知りたいとき、記録を残さず相談したいときに引く。
    - **前提**：なし

<!-- textlint-disable -->
別名：学習に使われるか・データの保持期間・Help improve our AI models・オプトアウト
<!-- textlint-enable -->

送ったデータの行方は、アカウントが個人向けか商用かで決まる規約と、会話を消したあとにも残る保管で決まる。このページは、学習に使われる条件、提供元に残る期間、手元に残る記録の 3 つを分けて説明する。具体的な日数や年数は変わりうるので、このページの末尾の参考にある Privacy Center の記事で、今の値を確かめる。

## 個人のプランと商用のプラン {#consumer-vs-commercial}

送った内容の扱いは、個人向けのアカウントか商用の契約かで規約が分かれる。個人向けは、無料と有料の個人のアカウントで、そのアカウントで使う Claude Code も含む。商用は、組織向けのプラン・API・政府向け・教育向けで、顧客が明示して提供しない限り、送った内容を学習に使わない。

| 区分 | 学習への利用 | 残る期間の基本 |
| --- | --- | --- |
| 個人向け | 設定で許可したときと、安全の審査の対象になったときに使う | 消した会話は一定の期間で消える。許可すると、学習側にはさらに長く残る |
| 商用 | 顧客が明示して提供しない限り使わない | 標準の保持期間。資格のある組織は Zero Data Retention を個別に有効にできる |

どちらの側に当たるかは、面ごとに確かめ方が違う。

=== "アプリ"

    ログインしているアカウントの契約で決まる。自分で契約した個人のアカウントなら個人向け、組織が契約した席に入っているなら商用の側になる。学校が配るアカウントの扱いは未確認なので、学校のアカウントで使うときは、学校の案内か公式の文書で確かめる。

=== "Claude Code"

    認証の経路で決まる。個人のサブスクリプションでログインしているなら個人向けの規約が当たり、組織のプランなら商用、API キーなら API の側になると読めるが、公式で直接は確かめていない。今どの経路で動いているかは <!-- link:begin check-billing-path#check-current-path -->[課金の経路を確かめる（API キーとサブスクリプション） › 今の経路を確かめる](../cost/check-billing-path.md#check-current-path)<!-- link:end --> で確かめる。

=== "API"

    API は商用の規約の側で、標準では学習に使われない。ただし、API の message threads（beta）はゼロデータ保持（Zero Data Retention）の対象外である。ゼロデータ保持を前提に設計しているときは、message threads を使わない。

!!! example "判断例：個人のアカウントで顧客のコードを相談したい"
    - **状況**：自分で契約した個人のアカウントで、顧客から預かったコードの不具合を相談したい。
    - **迷う候補**：学習への利用をオフにして、そのまま個人のアカウントで続ける。契約のある面（組織のプランか API）に移す。
    - **選んだもの**：契約のある面に移す。
    - **理由**：オフにしても、標準の保持期間と、安全の審査での利用は残る。そもそも預かったデータを個人のアカウントに渡してよいかは顧客との契約が決める。判断の基準は <!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](entrusted-data.md#contracted-surfaces)<!-- link:end --> にある。

組織で使うプランの選び方は <!-- link:begin choosing-an-org-plan -->組織で使うプランの選び方（準備中）<!-- link:end --> を見る。

## 学習への利用の設定 {#training-setting}

個人向けのアカウントでは、会話が学習に使われる場面が 3 つある。設定で改善への利用を許可したとき、会話が安全の審査の対象になったとき（利用ポリシーの検出と執行の改善に使う）、Trusted Tester などに明示して参加したときである。

使われるのは会話の全体で、内容・custom styles・会話の好みの設定・Claude in Chrome のデータを含む。connector や MCP サーバーから取った生の内容は含まないが、会話に貼った分は含む。シークレットチャットの会話は、許可していても学習に使わない（<!-- link:begin incognito-chats#retention -->[シークレットチャット（記録を残さない会話） › 残らないもの・残るもの](../app/incognito-chats.md#retention)<!-- link:end --> を見る）。

設定の場所は、Settings > Privacy の「Help improve our AI models」である。`claude.ai/settings/data-privacy-controls` から開け、Web・Desktop・Mobile のどれからでも変えられる。新しく使い始める人は登録のときに選ぶ。既定がオンかオフかは、公式の文書に書かれていないので、自分の画面で確かめる。

設定を切ったあとの扱いは次のとおりである。

- 前の会話と新しい会話は、これからの学習に使わない。
- もう始まっている学習と、できあがったモデルからは取り除かれない。
- 消した会話も、これからの学習には使わない。

2025 年 8 月の規約改定で、個人向けのアカウントは許可するかどうかを選ぶ形になった。選ぶ期限は既存の利用者に設けられたが、設定はいつでも変えられる。

商用の側には、この設定がない。顧客が Development Partner Program などで明示して提供しない限り、学習に使われないからである。

## 残る期間 {#retention}

提供元に残る期間は、データの種類ごとに層が分かれる。消した会話が消えるまでの期間と、学習側に残る期間は別のものとして読む。

| 対象 | 残り方 |
| --- | --- |
| 消した会話 | 履歴からはすぐ消える。バックエンドからは<!-- fact:begin deleted-chat-backend-days -->30 日（2026-11-05 時点）<!-- fact:end -->のうちに消える |
| 許可した学習の対象 | 匿名化した形で、学習のパイプラインに<!-- fact:begin training-opt-in-retention-years -->最長 5 年（2026-11-05 時点）<!-- fact:end -->残る。設定を有効にしたあとの新しい会話と再開した会話だけが対象 |
| 利用ポリシーの違反と判定された会話 | 入出力と安全の分類のスコアが<!-- fact:begin violation-retention -->最長で入出力 2 年・分類スコア 7 年（2026-11-05 時点）<!-- fact:end -->残る |
| フィードバックと報告 | <!-- fact:begin feedback-retention-years -->5 年（2026-11-05 時点）<!-- fact:end -->残る。`/feedback`・`/bug`・`/share` もここに入る |
| 法令などで必要なとき | さらに残すことがある |

具体的な日数と年数は変わりうるので、参考にある Privacy Center の記事で確かめる。

標準の期間は、消した会話がバックエンドから消えるまでの期間である。Claude Code の文書と 2025 年の規約改定のお知らせは「許可すれば長く、しなければ標準の期間」と短く書くが、Privacy Center は「最大・匿名化・学習のパイプライン」と区別して書く。この辞典は Privacy Center の書き方に合わせる。

- シークレットチャットは、履歴とメモリに残らず、学習に使われないが、バックエンドには標準の期間残る。企業向けの契約では組織の保持の設定に従う。詳しくは <!-- link:begin incognito-chats#retention -->[シークレットチャット（記録を残さない会話） › 残らないもの・残るもの](../app/incognito-chats.md#retention)<!-- link:end --> を見る。
- 違反と判定された会話が長く残る点は、<!-- link:begin when-requests-are-refused#by-surface -->[正当な依頼が断られたとき › 面ごとの表示と仕組み（分類器が見るもの・自動のモデルの切り替え）](when-requests-are-refused.md#by-surface)<!-- link:end --> と合わせて読む。
- `/feedback` などで会話とコードを送ったときに何が送られるかは <!-- link:begin what-feedback-sends#what-is-sent -->[/feedback・トランスクリプトの共有で送られるもの › 送られるものと残る期間](what-feedback-sends.md#what-is-sent)<!-- link:end --> にある。
- 商用の側は、標準の保持期間が基本になる。Zero Data Retention は資格のある Enterprise の組織で個別に有効にされるもので、既定ではない。
- Team と Enterprise では、管理者がデータエクスポートでシークレットチャットの会話を見られることがあり、保持ポリシーの対象にもなる。

## 手元に残る記録 {#local-transcripts}

手元に残る記録は、提供元の保管とは別のものである。Claude Code は、セッションの記録を手元の `~/.claude/projects/` に平文で保存し、<!-- fact:begin local-transcript-cleanup-days -->既定で 30 日（2026-11-05 時点）<!-- fact:end -->残す。期間は設定の `cleanupPeriodDays` で変えられる。会話に貼った秘密情報もそこに残る。この説明は WSL・Linux の CLI を基準にしていて、ほかの OS と IDE 拡張の動作は未確認である。

手元の記録を消しても、提供元に送った分は消えない。逆に、アプリで会話を消しても、手元の Claude Code の記録は消えない。両方を消したいときは、それぞれの場所で別に消す。

アプリのメモリも別の保管である。会話を消してもメモリに残る内容があり、見る・直す・消すは <!-- link:begin how-memory-works#deleted-chats -->[アプリのメモリ（仕組み・範囲・消し方と止め方） › 会話を消しても残るもの](../app/how-memory-works.md#deleted-chats)<!-- link:end --> にある。消したはずの内容を覚えているときの切り分けは <!-- link:begin unexpected-memories#diagnosis -->[別の会話やプロジェクトの内容が混ざる › 原因を安く確かめる順](../symptoms/unexpected-memories.md#diagnosis)<!-- link:end --> を見る。

手元の保管と通信の既定は、面ごとに <!-- link:begin default-safety-settings#defaults-by-surface -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 面ごとの既定（生成の表）](default-safety-settings.md#defaults-by-surface)<!-- link:end --> に並んでいる。テレメトリと報告の機能を止める方法は <!-- link:begin what-feedback-sends#telemetry -->[/feedback・トランスクリプトの共有で送られるもの › テレメトリと報告の機能を止める](what-feedback-sends.md#telemetry)<!-- link:end --> を見る。

## 何に効くか {#what-it-prevents}

このページは、原理「握る」と原因「境界がない」に関わる。送るデータの範囲と置き場所を、自分で握ってから渡すという考え方である。

- 境界がない：どの面の、どのアカウントの規約が当たるかを知らないまま渡すと、渡してよい範囲の線が引けない。個人向けと商用の表で、渡す前にどちらの側かを確かめる。
- 握る：学習の設定、消し方、手元の記録の期間は、いずれも自分で変えられる。変えられるものを先に決めておけば、渡した後で悩まずに済む。
- 預かったデータなど、渡してよいかが契約で決まるものは、先に誰のデータかを決める。<!-- link:begin entrusted-data#whose-data -->[預かったデータ・規約付きのデータを AI に渡してよいか › 誰のデータで、何が決まっているか](entrusted-data.md#whose-data)<!-- link:end --> が、その判断を扱う。

共有リンクや公開アーティファクトの見え方は別の話で、<!-- link:begin shared-artifacts-and-files#who-can-see -->[共有リンクと公開アーティファクトの扱い › 見られる人と、プランによる違い](shared-artifacts-and-files.md#who-can-see)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- 設定を切れば、過去に学習に使われた分も取り戻せる：取り戻せない。もう始まっている学習とできあがったモデルからは取り除かれない。切ると、これからの学習で使われなくなる。
- 会話を消せば、すべて消える：履歴からは消えるが、バックエンドには標準の期間残る。メモリと手元の記録は別に残る。
- 学習に使われないなら、何も残らない：学習への利用と保持は別である。シークレットチャットも、学習に使わないだけで、標準の期間は保持される。
- 商用なら、何も残らない：商用でも標準の保持期間はある。残らない設計にするには、資格のある組織が Zero Data Retention を個別に有効にする。
- `/share` は共有のリンクを作る：リンクを作る機能ではない。`/bug` の別名で、会話を報告として送る。くわしくは <!-- link:begin what-feedback-sends#share-is-bug -->[/feedback・トランスクリプトの共有で送られるもの › /share は共有のリンクではない](what-feedback-sends.md#share-is-bug)<!-- link:end --> にある。

業務で使うときの流れの中で私的な情報を渡す範囲を決める例は <!-- link:begin office-paperwork#private-data -->[事務作業の半自動化（経費・報告） › 私的な情報を渡す範囲](../recipes/office-paperwork.md#private-data)<!-- link:end --> にある。データ分析で生データを渡す前の考え方は <!-- link:begin data-analysis#check-raw-data -->[データを分析する › 生データで裏を取る](../recipes/data-analysis.md#check-raw-data)<!-- link:end --> を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Data usage](https://code.claude.com/docs/en/data-usage)：Anthropic・英語・確認日 2026-11-04
- [How long do you store my data?](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)：Anthropic（Privacy Center）・英語・確認日 2026-11-04
- [Updates to Consumer Terms and Privacy Policy](https://www.anthropic.com/news/updates-to-our-consumer-terms)：Anthropic・英語・確認日 2026-11-04
- [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)：Anthropic・英語・確認日 2026-11-04
- [Use Claude’s chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)：Anthropic・英語・確認日 2026-11-04
- [Message threads](https://platform.claude.com/docs/en/build-with-claude/message-threads)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](default-safety-settings.md)
- [/feedback・トランスクリプトの共有で送られるもの](what-feedback-sends.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](entrusted-data.md)
- [社内ガイドラインに書くこと](../team/ai-usage-guidelines.md)
- [秘密の情報を読まれた・外に出された](../symptoms/secrets-exposed.md)
- 組織で使うプランの選び方（準備中）

**関連**

- [シークレットチャット（記録を残さない会話）](../app/incognito-chats.md)
- [共有リンクと公開アーティファクトの扱い](shared-artifacts-and-files.md)
- [アプリのメモリ（仕組み・範囲・消し方と止め方）](../app/how-memory-works.md)
- [別の会話やプロジェクトの内容が混ざる](../symptoms/unexpected-memories.md)
- [正当な依頼が断られたとき](when-requests-are-refused.md)
- [データを分析する](../recipes/data-analysis.md)
- [事務作業の半自動化（経費・報告）](../recipes/office-paperwork.md)
- [課金の経路を確かめる（API キーとサブスクリプション）](../cost/check-billing-path.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
