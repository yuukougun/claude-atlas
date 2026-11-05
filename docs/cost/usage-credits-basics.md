---
id: usage-credits-basics
title: usage credits（上限を超えた分の従量課金）
nav_title: usage credits
aliases: [extra usage, 超過分の課金, 上限を超えて使う, 追加の使用量]
type: feature
field: cost
chapter: プランと支払い
order: 60
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [握る]
prevents: [合っていない]
pitfalls: []
summary: プランの上限を使い切っても、usage credits で従量課金に切り替えて作業を続けられる。思わぬ請求を防ぐため、月の上限額と通知を先に決めておく。
signs:
  - {type: goal, text: 上限に当たっても、作業を止めたくない}
  - {type: symptom, text: 上限を超えた分の請求が、思ったより多かった}
  - {type: situation, text: プランに付く API credits と usage credits の違いが分からない}
prerequisites: [how-usage-limits-work]
related: [check-billing-path#monthly-api-credits, choosing-a-plan, before-using-top-model, paying-in-yen, parallel-and-loop-costs, when-ai-is-unavailable]
tracks: [usage-credits]
outdated_advice: [workflow-keyword-extra-usage]
sources: [hc-usage-credits, hc-usage-limits, hc-api-credits, hc-release-notes]
volatility: 高
sections:
  - {title: 使いどころ, anchor: when-to-use}
  - {title: 切り替わる仕組み, anchor: how-it-works}
  - {title: 上限額と通知を決める, anchor: set-a-cap}
  - {title: API credits との違い, anchor: vs-api-credits}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 古くなった助言, anchor: outdated}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：プランの上限を使い切っても、従量課金に切り替えて作業を続けられる。月の上限額と通知を先に決めておく。
    - **いつ引くか**：上限に当たっても作業を止めたくないとき。上限を超えた分の請求が思ったより多かったとき。プランに付く API credits との違いが分からないとき。
    - **前提**：<!-- link:begin how-usage-limits-work -->[利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)<!-- link:end -->

<!-- textlint-disable -->
別名：extra usage・超過分の課金・上限を超えて使う・追加の使用量
<!-- textlint-enable -->

usage credits は、プランの利用上限を使い切った後も、前払いした分から API の標準の料金で払って使い続ける仕組みである。止まらない代わりに、請求が増える。このページは、切り替わる仕組みと、先に決める上限額と通知、プランに付く API credits との違いを扱う。

## 使いどころ {#when-to-use}

使いどころは、上限に当たる前に、締め切りのある作業を止めたくないときである。上限の種類と戻る時刻は <!-- link:begin how-usage-limits-work#limit-types -->[利用上限の仕組み（面をまたいで共有する枠） › 枠の種類と戻る時刻（プランごとの表）](how-usage-limits-work.md#limit-types)<!-- link:end --> にある。待てば戻る場面で、待つ代わりに払うかどうかを決めるのがこの機能である。

防ぐ原因は「合っていない」である。仕事の量とプランの枠が合わないとき、止まる以外の選び方を足せる。ただし払う額は、使った量にそのまま比例する。握るものは費用の上限である。上限額と通知を先に決めておけば、続ける判断を請求の前に手元へ置ける。

払う前に確かめることが 2 つある。

- 枠を待つか、プランを見直すか、払うか。プランの比べ方は <!-- link:begin choosing-a-plan -->[プランの選び方](choosing-a-plan.md)<!-- link:end --> にある。
- 本当に今日要る作業か。止まったときの備えは <!-- link:begin when-ai-is-unavailable -->[AI が使えないときの備え（障害・上限）](when-ai-is-unavailable.md)<!-- link:end --> にある。

## 切り替わる仕組み {#how-it-works}

有効にしてあると、上限を使い切ったときに作業が止まらず、従量課金に移る。移るのは、5 時間の枠や週の枠など、プランの枠のいずれかを使い切ったときである。料金は API の標準の料金である。Claude と Claude Code の両方に効く。

対象のプランは Pro・Max・Ultra である。Team と席の Enterprise は別の記事になっているので、組織のプランで使うときは、その記事を確かめる。対象の範囲は変わりやすい。現在の範囲は公式の記事で確かめる。

使った分は、前払いした残高から引かれる。残高が足りなくなったときに自動で補充する設定もある。補充の設定は、上限額とセットで見る必要がある（次の節）。

購入した分には失効の期限がある。日本などでの失効の期間は、<!-- fact:begin usage-credits-expiry-japan -->未確認<!-- fact:end -->である。期間と日付は変わりやすいので、まとめて買う前に、公式の記事で確かめる。失効の前には、メールで知らせが届く。

呼び名は変わった。以前は extra usage、コマンドは `/extra-usage` だった。今は <!-- name:begin extra-usage-to-usage-credits -->usage credits（/usage-credits）<!-- name:end --> である。旧名のコマンドも今は動く。公式の記事や古い手順書には旧名が残っているので、読み替えて読む。

## 上限額と通知を決める {#set-a-cap}

有効にする前に、決めることが 3 つある。月に払ってよい上限額、自動の補充を使うか、通知を受け取るか、である。決めずに有効にすると、並列やループで使う量が増えたとき、請求だけ先に膨らむ。

費用が膨らむ仕組みの説明は、<!-- link:begin parallel-and-loop-costs#multiplication -->[並列・ループ・workflows のコスト › 費用が膨らむ掛け算](parallel-and-loop-costs.md#multiplication)<!-- link:end --> を読む。

並列やループを始める前に決める事柄は、<!-- link:begin parallel-and-loop-costs#decide-before-starting -->[並列・ループ・workflows のコスト › 始める前に決める三つ](parallel-and-loop-costs.md#decide-before-starting)<!-- link:end --> で確かめる。

最小の手順は次のとおりである。面によって入り口が違う。

=== "アプリ"

    設定の Usage の画面で有効にする。そこで、前払いの額、月の上限額、自動の補充、通知を決める。モバイルのストアで契約している場合も、有効にできるのは web の設定だけである。画面の名前は変わりやすいので、迷ったら公式の記事を見る。

=== "Claude Code"

    設定は web の同じ画面で決める。Claude Code の側には `/usage-credits` のコマンドがある。切り替わった後の Claude Code は、usage credits を使って動く。WSL・Linux 以外の OS と IDE 拡張での見え方は未確認である。

!!! example "判断例：週の締め切りの前に枠を使い切りそうなとき"
    - **状況**：金曜の締め切りに向けて、水曜の夜に週の枠を使い切りそうになった。残りの作業は、あと半日ぶんある。
    - **迷う候補**：木曜の朝に枠が戻るのを待つ。usage credits を有効にして、そのまま続ける。
    - **選んだもの**：月の上限額を低めに決め、通知を付けてから有効にし、必要な作業だけ続ける。
    - **理由**：待つと締め切りに間に合わない。一方、上限なしで有効にすると、請求が読めなくなる。額の天井を先に置けば、続けるための費用を自分で決めて払える。

上限額の決め方に決まった正解はない。その月に、プランの枠で足りなかった分だけを払うと考え、先に額を決めておく。通知が来たら、続けるかどうかをそのたびに決め直す。

## API credits との違い {#vs-api-credits}

名前が似ているものに、Max・Ultra・Team のプランに付く月の API credits がある。どちらもお金の単位だが、別のもので、使える場面が違う。

| 比べる点 | usage credits | プランに付く API credits |
| --- | --- | --- |
| 何のためか | プランの上限を超えた分を、従量課金で続ける | API や Agent SDK の利用に使う |
| 使える場面 | Claude と Claude Code の対話 | 対話の Claude Code には使えない |
| 互いに使えるか | プランの API credits は使えない | usage credits の支払いには使えない |

プランに付く API credits は、対話の Claude Code の超過分には使えない。上限を超えた分を払いたいときは、usage credits が必要である。Claude Code が API キーとプランのどちらで課金されるかは、<!-- link:begin check-billing-path#monthly-api-credits -->[課金の経路を確かめる（API キーとサブスクリプション） › プランに付く API credits](check-billing-path.md#monthly-api-credits)<!-- link:end --> で確かめる。

## 効かない場面・落とし穴 {#pitfalls}

効かない場面と落とし穴は次のとおりである。

- **対象外のプラン**：Team と席の Enterprise は、別の記事の扱いになる。Pro・Max・Ultra の手順をそのまま当てはめない。
- **月の API credits では払えない**：プランに付く API credits が残っていても、対話の超過分には使えない。
- **モデルによっては最初から対象**：最上位のモデルは、プランによっては枠に含まれず、最初から usage credits で使う。使う前の確かめ方は <!-- link:begin before-using-top-model#which-limit -->[最上位のモデルを使う前に › どの枠から引かれるか（プランごとの表）](before-using-top-model.md#which-limit)<!-- link:end --> にある。
- **使うほど増える**：払う額は使った量に比例する。無人で回す仕事は、止める条件と費用の上限を先に決める。
- **失効**：買った分は、期限が来ると使えなくなる。まとめ買いの前に期間を確かめる。
- **円での支払い**：為替、消費税、請求書の扱いは <!-- link:begin paying-in-yen -->円での支払い・消費税・インボイス（準備中）<!-- link:end --> にある。

「請求が思ったより多かった」ときは、まず、上限額を決めずに有効にしていないか、並列やループが走っていないかを見る。

## 古くなった助言 {#outdated}

手順書や頼み方の型に extra usage・`/extra-usage` と書いてあれば、usage credits・`/usage-credits` に読み替える。旧名のコマンドも今は動く。ワークフローを起動する語の移り変わりも含めた台帳の行は、<!-- link:begin outdated-advice-ledger#workflow-keyword-extra-usage -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#workflow-keyword-extra-usage)<!-- link:end --> で読める。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)：Anthropic・英語・確認日 2026-11-04
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)：Anthropic・英語・確認日 2026-11-04
- [Monthly API credits for Max, Ultra, and Team plans](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)：Anthropic・英語・確認日 2026-11-04
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)

**関連**

- [課金の経路を確かめる（API キーとサブスクリプション） › プランに付く API credits](check-billing-path.md#monthly-api-credits)
- [プランの選び方](choosing-a-plan.md)
- [最上位のモデルを使う前に](before-using-top-model.md)
- 円での支払い・消費税・インボイス（準備中）
- [並列・ループ・workflows のコスト](parallel-and-loop-costs.md)
- [AI が使えないときの備え（障害・上限）](when-ai-is-unavailable.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
