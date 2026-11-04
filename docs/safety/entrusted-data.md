---
id: entrusted-data
title: 預かったデータ・規約付きのデータを AI に渡してよいか
aliases: [機密のデータを AI に渡す, NDA のデータ, 顧客のデータ, コンペのデータの規約, 社外秘の資料]
type: concept
field: safety
chapter: データの扱い
order: 70
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [握る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, データ分析, チーム, コンテスト]
summary: 顧客のデータや、NDA・規約の付いたデータを、どの面なら渡してよいかを判断できる。預かったデータは、契約で扱いが決まっている面だけで使う。
signs:
  - {type: situation, text: 顧客から預かったデータを分析させたい}
  - {type: situation, text: コンペのデータを、クラウドで動くエージェントに読ませようとしている}
  - {type: goal, text: 社外秘の資料を AI に渡してよいか確かめたい}
prerequisites: [where-your-data-goes]
related: [checking-ai-rules, default-safety-settings#by-stage, protecting-secrets, where-it-runs, ai-usage-guidelines, via-cloud-providers, choosing-an-org-plan, data-analysis, office-paperwork, cloud-sessions-and-teleport]
sources: [cc-docs-data-usage, privacy-long-store-data, anthropic-news-updates-our-consumer-terms, cc-docs-security, cc-docs-claude-code-on-the-web, hc-cowork-and-chat]
volatility: 中
sections:
  - {title: 誰のデータで、何が決まっているか, anchor: whose-data}
  - {title: 契約のある面だけで使う, anchor: contracted-surfaces}
  - {title: クラウドで動く作業に気をつける, anchor: cloud-runs}
  - {title: 何に効くか, anchor: what-it-prevents}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：顧客のデータや NDA・規約付きのデータを、どの面なら渡してよいかを判断できる。預かったデータは、契約で扱いが決まっている面だけで使う。
    - **いつ引くか**：顧客から預かったデータを分析させたいとき、コンペのデータをクラウドで動くエージェントに読ませようとしているとき、社外秘の資料を AI に渡してよいか確かめたいときに引く。
    - **前提**：<!-- link:begin where-your-data-goes -->[送ったデータの行方（学習・保持期間）](where-your-data-goes.md)<!-- link:end -->

<!-- textlint-disable -->
別名：機密のデータを AI に渡す・NDA のデータ・顧客のデータ・コンペのデータの規約・社外秘の資料
<!-- textlint-enable -->

預かったデータを AI に渡してよいかは、Claude の設定ではなく、データの持ち主との約束で決まる。このページは、渡す前に確かめる 2 つの契約、契約のある面に絞る判断、クラウドの作業から外に出るものを説明する。法令の解釈や個別の契約条項の読み方は扱わない。

## 誰のデータで、何が決まっているか {#whose-data}

預かったデータとは、自分のものではなく、顧客・取引先・主催者・組織が持ち主のデータである。たとえば、顧客から受け取った売上の記録、NDA を結んだ相手の設計資料、コンペの主催者が配る学習用のデータがこれに当たる。

渡してよいかは、独立した 2 つの契約を別々に確かめて決める。

- **持ち主との約束**：NDA・業務委託の契約・データの利用規約・コンペの規約。外部のサービスに送ってよいか、AI のサービスに送ってよいか、保管や削除に条件があるかが書かれる。
- **提供元との契約**：自分や組織が Claude の提供元と結んでいる規約。送った内容を学習に使うか、どれだけ残すかを決める。

提供元との契約が商用の規約で、学習に使われない側にあっても、持ち主との約束が送ることを許すとは限らない。約束が「第三者への開示を禁じる」「自社の管理下の環境から出さない」と書いていれば、学習に使われなくても、送った時点で約束に反しうる。逆の場合もある。持ち主が AI の利用を明示して認めていても、個人向けの契約で学習に使う設定が有効なら、約束した扱いにならない。

確かめる順は次のとおりにする。

1. 持ち主との約束は、AI のサービスへの送信を許すのか、禁じるのか、書いていないのか。
2. 許すなら、提供元・プラン・面のどれを指定しているのか。
3. 自分の使う面は、その指定に合う契約の側にあるのか。
4. 作業が動く場所が、約束の範囲に収まるか（契約のある面の節とクラウドの節で確かめる）。

書いていない場合は、渡してよいという意味にならない。データの持ち主、または組織の法務・情報セキュリティの担当に聞いてから渡す。このページは具体的な契約の条項を扱わず、確かめる観点だけを示す。

コンペのデータは、このうち主催者の規約が決める。クラウドのエージェントにコンペのデータを送ることが、データの規約に抵触しうる（根拠：中・類推）。規約は大会ごと、年ごとに変わるので、参加する大会の最新の規約を読む。AI の利用そのものの規則は <!-- link:begin checking-ai-rules#checklist -->[学校・組織・コンテストの規則（類型と確認表） › 確認表](checking-ai-rules.md#checklist)<!-- link:end --> で確かめる。

## 契約のある面だけで使う {#contracted-surfaces}

預かったデータを使う面は、約束に合う契約が結ばれている面だけに絞る。契約の側は、個人向けと商用で分かれる。違いは <!-- link:begin where-your-data-goes#consumer-vs-commercial -->[送ったデータの行方（学習・保持期間） › 個人のプランと商用のプラン](where-your-data-goes.md#consumer-vs-commercial)<!-- link:end --> にある。個人向けは設定で許可すると学習に使われ、商用の規約は、顧客が明示して提供しない限り学習に使わない。

面ごとに、契約の側をどこで確かめるかが違う。

=== "アプリ"

    使っているアカウントが、個人向けか組織の契約かを確かめる。個人向けのアカウントで学習への利用を許可していると、預かったデータを貼った会話も対象になりうる。許可の設定は <!-- link:begin where-your-data-goes#training-setting -->[送ったデータの行方（学習・保持期間） › 学習への利用の設定](where-your-data-goes.md#training-setting)<!-- link:end --> で確かめる。

    アプリのタスクはクラウドで動く。動く場所が約束の範囲に収まるかは、「クラウドで動く作業に気をつける」の節で確かめる。

=== "Claude Code"

    ログインに使っているアカウントや認証の方式で、契約の側が決まる。個人のアカウントでログインしていれば個人向け、組織の契約や API の認証なら商用の側になる。クラウド事業者経由で使うときは、そのクラウドの契約と統制の中で動く。選び方は <!-- link:begin via-cloud-providers -->Bedrock・Vertex AI・Foundry 経由で使う（準備中）<!-- link:end --> にある。

    手元に残る記録は、提供元の契約とは別の保存である。預かったデータを読ませたセッションの記録は、手元に平文で残る。扱いは <!-- link:begin where-your-data-goes#local-transcripts -->[送ったデータの行方（学習・保持期間） › 手元に残る記録](where-your-data-goes.md#local-transcripts)<!-- link:end --> で確かめる。

=== "API"

    API は商用の規約の側にある。顧客が明示して提供しない限り学習に使われず、標準の保持期間がある。資格のある組織は、Zero Data Retention を個別に有効にできる。

    ただし、API を使うことは、持ち主との約束を満たすことではない。約束が提供元や地域を指定していないかを、先に確かめる。

組織で使うプランは <!-- link:begin choosing-an-org-plan -->組織で使うプランの選び方（準備中）<!-- link:end --> で比べる。プランごとの学習と保持の扱いは、公式の文書（参考の Data usage と Privacy Center）で今の記述を確かめる。

面を絞る決めは、個人の注意に任せず、組織の決まりに書いておくと守られやすい。書く項目は <!-- link:begin ai-usage-guidelines#what-to-write -->[社内ガイドラインに書くこと › 書くこと（データの区分・面とモード・レビューの責任）](../team/ai-usage-guidelines.md#what-to-write)<!-- link:end --> にある。書いた禁止はお願いにすぎないので、守らせたいものは設定で縛る。縛る段階は <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](default-safety-settings.md#by-stage)<!-- link:end --> を正本にする。

!!! example "判断例：顧客の売上データを分析させる"
    - **状況**：顧客から受け取った売上データを集計し、傾向を報告したい。契約書には「業務の目的以外に使わない」「第三者に開示しない」とある。AI の利用には触れていない。
    - **迷う候補**：手元で使い慣れた個人のアカウントの Claude Code で分析する。組織が契約している面で分析する。
    - **選んだもの**：先に契約の持ち主へ、AI のサービスに送ってよいか、どの面なら許されるかを聞く。許可が出るまでデータは渡さない。許可の範囲が組織の契約の面なら、その面で分析する。
    - **理由**：契約が AI の利用に触れていなくても、使ってよい意味にならない。個人のアカウントは、学習に使う設定が有効なら約束した扱いと食い違いうる。許可の範囲を先に決めれば、後から使い方を変えずに済む。

分析の進め方は <!-- link:begin data-analysis#check-raw-data -->データを分析する › 生データで裏を取る（準備中）<!-- link:end --> にある。事務作業に預かった情報が混ざるときの、渡す範囲の決め方は <!-- link:begin office-paperwork#private-data -->事務作業の半自動化（経費・報告） › 私的な情報を渡す範囲（準備中）<!-- link:end --> にある。

## クラウドで動く作業に気をつける {#cloud-runs}

クラウドで動く作業では、データが自分の PC の外に出る。預かったデータの約束が「自社の管理下の環境の外に出さない」と書いていれば、クラウドで動かすこと自体が約束に反しうる。

クラウドで動くものは次のとおりである。

- **アプリのタスク**：アプリのタスクはクラウドで動き、PC を閉じても続く。スケジュールした実行も、PC の電源が切れていても動く。
- **Claude Code のクラウドセッション**：Anthropic が管理する隔離された環境で動く。リポジトリの内容を送って作業させる。

リポジトリの中に預かったデータが入っていれば、クラウドに送る作業と一緒に、そのデータも環境へ送られる。コンペのデータをリポジトリに置いたまま、クラウドのエージェントに読ませる場面がこれに当たる。クラウドに送ってよい作業は <!-- link:begin cloud-sessions-and-teleport#what-to-send -->クラウドセッションと teleport › クラウドに送ってよい作業（準備中）<!-- link:end --> で確かめる。

作業の動く場所は、手元・クラウド・リモート操作の 3 つである。見分け方は <!-- link:begin where-it-runs#three-locations -->[実行場所の違い（クラウド・自分の PC・リモート操作） › 三つの実行場所](../surfaces/where-it-runs.md#three-locations)<!-- link:end --> にある。リモート操作は、実行を手元に残したまま別の端末から操作する。クラウドに出したくないデータは、手元で動かす形を選ぶ。

!!! example "判断例：コンペのデータをクラウドのエージェントに読ませる"
    - **状況**：オンラインのコンペで配られた学習用のデータを、クラウドで動くエージェントに読ませて、前処理を任せたい。規約は読んだが、クラウドへの送信には触れていない。
    - **迷う候補**：クラウドのエージェントに任せて、手元を空ける。手元で動かして、クラウドには送らない。
    - **選んだもの**：規約が外部のサービスへの送信を禁じているか分からない間は、手元で動かす。主催者に問い合わせて許可が確認できたら、クラウドに移す。
    - **理由**：クラウドへの送信が規約に抵触しうる（根拠：中・類推）。手元で動かせば、データが提供元の管理するクラウドの環境へ渡る経路は避けられる。ただし、手元で動かしても、読ませた内容はモデルに送られる。そのため、「誰のデータで、何が決まっているか」の節の 4 つの確認は手元でも省かない。

預かったデータの隣に、認証情報（`.env`・API キー）が置かれていることがある。認証情報を作業ディレクトリと会話から外す設定は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](protecting-secrets.md#keep-out)<!-- link:end --> にある。

## 何に効くか {#what-it-prevents}

この判断が防ぐ原因は「境界がない」である。預かったデータは、どの面にどこまで渡してよいかの線が、約束によってすでに引かれている。線を意識せずに便利な面を選ぶと、約束の外へデータが出る。

原理は「握る」である。何を渡し、どの面で動かすかの決定を、道具の既定や使い慣れた面に任せず、人の側で握っておく。公式の既定だけでは、預かったデータの約束は守れない。既定は Anthropic の側の想定であり、持ち主との約束は含まれないからである。段階ごとの既定の限界は <!-- link:begin default-safety-settings#limits -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 公式の既定の限界](default-safety-settings.md#limits)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- **商用の規約だから渡してよい**：商用の規約は、提供元の側の扱い（学習に使わない、標準の保持期間）を決める。持ち主との約束は別なので、約束が許す面かどうかを別に確かめる。
- **学習に使われなければ問題ない**：約束は、学習の有無に限らず、第三者への開示や環境の外への持ち出しを禁じることがある。送った時点で成立する。
- **オプトアウトすれば取り返せる**：個人向けで学習への利用を切っても、すでに学習に使われたデータは残る。送る前に決めるのであって、送った後に直せない。
- **契約に AI の文言がないので使ってよい**：文言がないことは、使ってよいことを意味しない。確かめ方は <!-- link:begin checking-ai-rules#when-unclear -->[学校・組織・コンテストの規則（類型と確認表） › 文言がないとき・分からないとき](checking-ai-rules.md#when-unclear)<!-- link:end --> にある。
- **データを削除すれば手元に何も残らない**：会話や作業の記録は、提供元の保存とは別に手元に残る。残る場所と期間は <!-- link:begin where-your-data-goes#local-transcripts -->[送ったデータの行方（学習・保持期間） › 手元に残る記録](where-your-data-goes.md#local-transcripts)<!-- link:end --> で確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Data usage](https://code.claude.com/docs/en/data-usage)：Anthropic・英語・確認日 2026-11-04
- [How long do you store my data?](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)：Anthropic（Privacy Center）・英語・確認日 2026-11-04
- [Updates to Consumer Terms and Privacy Policy](https://www.anthropic.com/news/updates-to-our-consumer-terms)：Anthropic・英語・確認日 2026-11-04
- [Security](https://code.claude.com/docs/en/security)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)：Anthropic・英語・確認日 2026-11-04
- [Claude Cowork and chat are one Claude](https://support.claude.com/en/articles/16761823-claude-cowork-and-chat-are-one-claude)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [送ったデータの行方（学習・保持期間）](where-your-data-goes.md)

**次に読む**

- 事務作業の半自動化（経費・報告）（準備中）

**関連**

- [学校・組織・コンテストの規則（類型と確認表）](checking-ai-rules.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](default-safety-settings.md#by-stage)
- [秘密情報（.env・API キー）を守る](protecting-secrets.md)
- [実行場所の違い（クラウド・自分の PC・リモート操作）](../surfaces/where-it-runs.md)
- [社内ガイドラインに書くこと](../team/ai-usage-guidelines.md)
- Bedrock・Vertex AI・Foundry 経由で使う（準備中）
- 組織で使うプランの選び方（準備中）
- データを分析する（準備中）
- クラウドセッションと teleport（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
