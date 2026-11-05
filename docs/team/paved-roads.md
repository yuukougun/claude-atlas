---
id: paved-roads
title: 禁止ではなく安全な道を作る
aliases: [paved road, 舗装された道, 野良の AI 利用, シャドー AI, AI は組織の強みも機能不全も増幅する, 増幅器としての AI, DORA]
type: concept
field: team
chapter: 導入と決まり
order: 20
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [縛る, 握る]
prevents: [境界がない, 縛っていない]
pitfalls: []
scenes: [チーム, 開発]
summary: AI の利用を禁じる代わりに、安全な既定と許す面を用意した、使ってよい道を作れる。AI は組織の土台の強さも弱さも増幅するので、テストとレビューを見直し、危険の小さい作業から広げる。
signs:
  - {type: situation, text: 会社が AI の利用を禁じていて、隠れて使う人がいる}
  - {type: goal, text: AI を禁止せずに、安全に使える状態を作りたい}
  - {type: situation, text: 組織全体に AI を広げる前に、何を整えるか考える}
  - {type: symptom, text: AI を入れて速くなったのに、障害や手戻りが増えた}
prerequisites: [default-safety-settings, request-vs-lock]
related: [ai-usage-guidelines, rolling-out-to-teams, review-bottlenecks, four-principles#proportional-rule, share-team-settings, org-managed-settings-and-mcp, managed-settings-enforcement, sandboxing, where-your-data-goes, entrusted-data, checking-ai-rules, approval-fatigue, risk-tiered-approval, measure-changes, felt-vs-measured]
sources: [dora-2025-report, infoq-dora-state-ai-dev, atmarkit-mercari-claude-code-rollout, codeknights-japan-cases-2026-summer]
volatility: 低
sections:
  - {title: 禁止すると何が起きるか, anchor: what-happens}
  - {title: 注意力に頼らない既定, anchor: defaults-over-attention}
  - {title: 危険の小さい作業から始める, anchor: start-low-risk}
  - {title: AI は土台の強さも弱さも増幅する（広げる前に見直すもの）, anchor: amplifier}
  - {title: どの原理・どの原因に関わるか, anchor: principles-and-causes}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：AI の利用を禁じる代わりに、安全な既定と許す面を用意した「使ってよい道」を作る考え方と、広げる前に整える土台が分かる。
    - **いつ引くか**：会社が AI を禁じていて隠れて使う人がいるとき。AI を禁止せずに安全に使える状態を作りたいとき。組織全体へ広げる前に、何を整えるか考えるとき。入れて速くなったのに障害や手戻りが増えたとき。
    - **前提**：<!-- link:begin default-safety-settings -->[安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)<!-- link:end -->、<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：paved road・舗装された道・野良の AI 利用・シャドー AI・AI は組織の強みも機能不全も増幅する・増幅器としての AI・DORA
<!-- textlint-enable -->

禁止ではなく安全な道を作るとは、AI の利用を一律には禁じず、既定の設定と許す面を組織が用意して、その上を通る使い方を標準にすることである。広げる順番は、危険の小さい作業から決める。AI は組織の土台の強みと弱みを両方とも大きくするので、広げる前にテストとレビューの足場を見直す。

## 禁止すると何が起きるか {#what-happens}

AI の利用を禁じても、使いたい人がいなくなるとは限らない。禁止の文が効くのは、守る人の手元だけである。守らない人は私物の端末や個人のアカウントで使い、これが野良の AI 利用（シャドー AI）になる。

禁止が生むものを、組織の側から見ると次のようになる。

| 方針 | 組織に見えるもの | 組織が決められるもの |
| --- | --- | --- |
| 禁止だけを置く | 守った人の利用だけ | ほとんどなし |
| 使ってよい道を作る | 許した面の利用と、その設定 | 面・データの扱い・設定の既定 |

隠れた利用は、データがどの面に送られ、どの記録が残るかを組織が知らない状態を作る。送ったデータの扱いは面とプランで違う（<!-- link:begin where-your-data-goes#consumer-vs-commercial -->[送ったデータの行方（学習・保持期間） › 個人のプランと商用のプラン](../safety/where-your-data-goes.md#consumer-vs-commercial)<!-- link:end -->）。見えない利用には、この違いに沿った管理も届かない。

これは禁止の文書自体の欠点でもある。書いた禁止はお願いにすぎず、守らせたい規則は設定で縛る（<!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end -->、<!-- link:begin ai-usage-guidelines#lock-the-prohibitions -->[社内ガイドラインに書くこと › 禁止は設定で縛る](ai-usage-guidelines.md#lock-the-prohibitions)<!-- link:end -->）。禁止を守らせたいなら、禁止の先にある安全な使い方を、使いやすい形で用意するほうが筋に合う（推論・実践例なし）。

日本の企業の導入では、全社展開と並べて野良の利用への対策を説明する報告がある。たとえばメルカリは、2026 年 8 月の @IT の報道で、全社展開とシャドー AI 対策を支える仕組みを明かしている（根拠：中）。

## 注意力に頼らない既定 {#defaults-over-attention}

注意力に頼らない既定とは、利用者が何も考えなくても安全な側に倒れる設定を、組織が先に配っておくことである。人は疲れ、確認が多いと中身を読まずに承認する（<!-- link:begin approval-fatigue#why -->[承認疲れ › なぜ読まなくなるか](../safety/approval-fatigue.md#why)<!-- link:end -->）。注意力で安全を保つ設計は、使う人が増えるほど崩れる。

既定を作るときの順番は次のとおりである。

1. 公式の既定を基準にする。面ごとの既定と、任せる段階ごとに足すものは、正本のページにある（<!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end -->）。このページでは書き直さない。
2. 例外を許さない規則は、お願いではなく鍵に移す。deny ルールやフックで、守らせたいことを毎回必ず効く形にする（<!-- link:begin request-vs-lock#two-layers -->[お願いと鍵（決定論的か、非決定論的か） › 二層で書く](../basics/request-vs-lock.md#two-layers)<!-- link:end -->）。
3. 利用者が外せない範囲を、組織の設定で決める。配る経路と優先の順番は、別のページで選ぶ（<!-- link:begin org-managed-settings-and-mcp#delivery -->組織に設定と MCP サーバーを配る<!-- link:end -->、<!-- link:begin managed-settings-enforcement#cannot-override -->管理設定と組織の強制<!-- link:end -->）。
4. チームでは、共有する設定と個人に残す設定を分ける（<!-- link:begin share-team-settings#shared-vs-personal -->[チームで設定を共有する › 共有するものと個人に残すもの](share-team-settings.md#shared-vs-personal)<!-- link:end -->）。
5. 任せる幅が広い作業には、封じ込めを足す。読み書きと通信を OS の層で囲える（<!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end -->）。

もう 1 つの柱が、許す面を決めることである。どの面に、どのデータを渡してよいかを先に決める。預かったデータや規約付きのデータは、契約で扱いが決まっている面だけで使う（<!-- link:begin entrusted-data#contracted-surfaces -->[預かったデータ・規約付きのデータを AI に渡してよいか › 契約のある面だけで使う](../safety/entrusted-data.md#contracted-surfaces)<!-- link:end -->）。学校・組織・大会の規則が先にある場合は、その規則の型を確かめてから決める（<!-- link:begin checking-ai-rules#checklist -->[学校・組織・コンテストの規則（類型と確認表） › 確認表](../safety/checking-ai-rules.md#checklist)<!-- link:end -->）。法令の解釈や社内規則の回避は、このページでは扱わない。

実例として、メルカリは 2026 年 5 月に Claude Code と Claude Cowork を全社に展開し、エンジニアと非エンジニアで別の設定を配布したと報じられている。非エンジニアは通常ローカルの管理者権限を持たず、必要なときに申請すると一時的に付き、自動で失効する（根拠：中。企業の説明を報じた記事で、自己申告にあたる）。利用者の注意力ではなく、配る設定の側で線を引いている例である。

決まりごとの文書は、既定の上に重ねる。文書に書くことは別のページにある（<!-- link:begin ai-usage-guidelines#what-to-write -->[社内ガイドラインに書くこと › 書くこと（データの区分・面とモード・レビューの責任）](ai-usage-guidelines.md#what-to-write)<!-- link:end -->）。

## 危険の小さい作業から始める {#start-low-risk}

危険の小さい作業から始めるとは、任せる範囲を、間違えたときの被害が小さく、戻しやすいものに絞って始めることである。任せる幅を広げるほど、確かめる仕組みと封じ込めを強める（比例則。<!-- link:begin four-principles#proportional-rule -->[四つの原理と比例則（見せる・確かめる・縛る・握る） › 比例則](../start/four-principles.md#proportional-rule)<!-- link:end -->）。守りが先で、範囲の拡大は後になる。

危険が小さい作業の目安は、次の条件を満たすものである。

- 読み取りが中心で、書き込みが少ない。
- 間違えても戻せる（バージョン管理の下にある、下書きで終わる）。
- 秘密や預かったデータを含まない。
- 本番の環境に直接触れない。

広げるときは、段を分けて、段ごとに承認の数を決める（<!-- link:begin risk-tiered-approval#three-tiers -->[リスク段階別の承認（AI の承認を人の承認に数えない） › 三つの段と承認の数](risk-tiered-approval.md#three-tiers)<!-- link:end -->）。段を上げる前に、その段の変更が効いたかを、同じ物差しで測る（<!-- link:begin measure-changes#small-eval -->[変更が効いたかを測る（小さな eval） › 小さな eval の手順](../eval/measure-changes.md#small-eval)<!-- link:end -->、<!-- link:begin felt-vs-measured#what-to-record -->[体感と実測 › 記録で測るもの](../eval/felt-vs-measured.md#what-to-record)<!-- link:end -->）。体感の「速くなった」だけで広げない。

日本語圏の実務の記事では、セキュリティ部門と協力しながら、低リスクの作業から始める進め方がよく勧められている（根拠：弱）。立ち上げの手引きの作り方は、導入のページにまとめてある（<!-- link:begin rolling-out-to-teams#onboarding-guide -->チームに広める（/team-onboarding など）<!-- link:end -->）。

!!! example "判断例：最初に任せる作業を選ぶ"
    - **状況**：チームに Claude Code を広げ始める。候補になる作業が 2 つある。
    - **迷う候補**：A は、既存のテストが揃ったモジュールの、テスト追加とリファクタリング。B は、本番の設定ファイルを変更する自動化。
    - **選んだもの**：A から始める。
    - **理由**：A は、変更をテストで確かめられ、バージョン管理で戻せる。B は、間違いが本番に直接出る。B も見合う守りが揃えば任せられるが、守りを作る前に任せる順番ではない。

## AI は土台の強さも弱さも増幅する（広げる前に見直すもの） {#amplifier}

AI は土台の強さと弱さの両方を増幅する、というのは、AI の導入が組織の既存の強みを大きくするのと同じ力で、既存の弱みまで大きくするという見方である。開発の成果を測る調査研究 DORA（Google Cloud）の 2025 年の報告は、AI の主な役割を、組織の強みと弱みを拡大する増幅器だと述べている。大きな見返りは、個々の道具よりも、組織の仕組み全体に目を向けた取り組みから出る、という趣旨である（根拠：中。大規模調査）。

同じ調査の報道では、AI の採用はスループットと正の関係を示した一方で、デリバリーの不安定さは増え続けた、と紹介されている（根拠：中）。この調査は相関を示すもので、AI が不安定さの原因だと言い切るものではない。このページも、因果は主張しない。

この見方は、広げる前の点検で使う。AI で変更が増えると、次の弱点から先に表へ出ると考えられる（推論・実践例なし）。

- **テストが薄い**：変更の正否を確かめる手段が足りず、障害になって初めて気づく。
- **レビューが詰まる**：変更は増えるのに、レビューと動作確認に回せる量は増えない。作業は人に積もる（<!-- link:begin review-bottlenecks#where-it-clogs -->[レビューのボトルネックと疲労 › 詰まる場所はレビューと動作確認](review-bottlenecks.md#where-it-clogs)<!-- link:end -->）。
- **戻す手段が弱い**：失敗を小さい範囲で止めて戻す仕組みがない。

流す量は、変更を出す速さではなく、レビューできる量に合わせる（<!-- link:begin review-bottlenecks#match-review-capacity -->[レビューのボトルネックと疲労 › 流す量をレビューに合わせる](review-bottlenecks.md#match-review-capacity)<!-- link:end -->）。導入の事例を読むときは、数値が自己申告で標本も限られることに気をつける（<!-- link:begin review-bottlenecks#reading-case-numbers -->[レビューのボトルネックと疲労 › 事例の数値の読み方（自己申告と標本の大きさ）](review-bottlenecks.md#reading-case-numbers)<!-- link:end -->）。導入事例の一覧には、速さの数値だけでなく、レビューの待ち時間の増加や疲労感の増加といった課題を公開した企業もある（根拠：弱。各社の自己申告）。

AI を入れて速くなったのに障害や手戻りが増えたとき、原因を AI の質へ求める前に、テストとレビューの余力を見る。これは、広げる前に見直すものと同じ一覧である。

## どの原理・どの原因に関わるか {#principles-and-causes}

このページが扱うのは、原理の「縛る」と「握る」、原因の「境界がない」と「縛っていない」である。4 つの原理の全体は別のページにある（<!-- link:begin four-principles#overview -->[四つの原理と比例則（見せる・確かめる・縛る・握る） › 4 つの原理の一覧](../start/four-principles.md#overview)<!-- link:end -->）。

- **縛る**：禁止の文を設定で縛ること。安全な既定と、利用者の手では外せない範囲は、これにあたる（<!-- link:begin four-principles#lock -->[四つの原理と比例則（見せる・確かめる・縛る・握る） › 縛る](../start/four-principles.md#lock)<!-- link:end -->）。防ぐ原因は「縛っていない」である。禁止がお願いの文のままだと、守らない人がいても止まらない。
- **握る**：広げる順番と承認の数を、人が決めること。危険の小さい作業から始め、段ごとに人の承認を置くことが、これにあたる（<!-- link:begin four-principles#hold -->[四つの原理と比例則（見せる・確かめる・縛る・握る） › 握る](../start/four-principles.md#hold)<!-- link:end -->）。
- **境界がない**：どこまで使ってよいかの線がない状態。許す面と、渡してよいデータの範囲を先に決めることで、線が引かれる。野良の利用は、この線の外で起きる。

## よくある誤解 {#misconceptions}

- **安全な道を作るのは、制限を緩めることだ**：違う。道を作る側は、既定と許す面を整え、deny ルールや管理設定のような縛りも残す。禁じる範囲を減らすのではなく、守らせる手段を文書から設定へ移す。
- **禁止の文書を書けば守られる**：文書はお願いである。例外を許さない規則は、設定で縛る（<!-- link:begin request-vs-lock#misconceptions -->[お願いと鍵（決定論的か、非決定論的か） › 誤解](../basics/request-vs-lock.md#misconceptions)<!-- link:end -->）。
- **導入すれば自然に速く安全になる**：AI は土台を増幅するので、土台が弱ければ弱さも大きくなる。DORA の調査は相関であり、AI が不安定さを生むとは言っていない。この調査から言えるのは、土台を見直さずに広げると問題になりうる、という注意までである。
- **ほかの会社の数値が自社の目標になる**：事例の数値は自己申告で、条件も違う。自社の物差しで測る（<!-- link:begin felt-vs-measured#why -->[体感と実測 › なぜ体感はずれるか](../eval/felt-vs-measured.md#why)<!-- link:end -->）。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)
- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**関連**

- [社内ガイドラインに書くこと](ai-usage-guidelines.md)
- [レビューのボトルネックと疲労](review-bottlenecks.md)
- [四つの原理と比例則（見せる・確かめる・縛る・握る） › 比例則](../start/four-principles.md#proportional-rule)
- [チームで設定を共有する](share-team-settings.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)
- [預かったデータ・規約付きのデータを AI に渡してよいか](../safety/entrusted-data.md)
- [学校・組織・コンテストの規則（類型と確認表）](../safety/checking-ai-rules.md)
- [承認疲れ](../safety/approval-fatigue.md)
- [リスク段階別の承認（AI の承認を人の承認に数えない）](risk-tiered-approval.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [体感と実測](../eval/felt-vs-measured.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [2025 DORA State of AI-assisted Software Development Report](https://dora.dev/research/2025/dora-report/)：DORA（Google Cloud）・英語・確認日 2026-11-05
- [DORA Report Finds AI Is an Amplifier in Software Development, But Trust Remains Low](https://www.infoq.com/news/2025/09/dora-state-of-ai-in-dev-2025/)：InfoQ・英語・確認日 2026-11-04
- [メルカリが明かす「Claude Code全社展開」「シャドーAI対策」を支える仕組み](https://atmarkit.itmedia.co.jp/ait/spv/2608/04/news002.html)：@IT（アイティメディア）・確認日 2026-11-04
- [Claudeの日本企業の導入事例まとめ【2026年夏】](https://www.codeknights.co.jp/contents/claude-japan-cases-2026summer)：CodeKnights・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
