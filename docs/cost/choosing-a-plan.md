---
id: choosing-a-plan
title: プランの選び方
aliases: [料金プラン, プランの比較, 個人向けプラン, サブスクリプション]
type: comparison
field: cost
chapter: プランと支払い
order: 40
level: 使う
priority: 推奨
surfaces: [app, claude-code]
principle: []
prevents: [合っていない]
pitfalls: []
summary: 個人向けのプランを、使う面・Claude Code の量・上位のモデルの扱い・上限の形で比べて選べる。料金と倍率は確認日つきの表で確かめる。
signs:
  - {type: goal, text: どのプランにすべきか迷う}
  - {type: goal, text: 今のプランから上げるべきか迷う}
  - {type: situation, text: プランの名前が変わり、どれが前のどれに当たるか分からない}
  - {type: goal, text: Claude Code をよく使うので、合うプランを知りたい}
prerequisites: [how-usage-limits-work]
related: [before-using-top-model, usage-credits-basics, paying-in-yen, check-billing-path, choosing-a-model, choosing-an-org-plan, saving-priorities, term-index, change-timeline-2026]
tracks: [plans, usage-limits]
outdated_advice: [max-5x-or-20x]
sources: [claude-pricing, hc-pro-plan, hc-max-plan, hc-ultra-plan, hc-claude-code-plan, hc-usage-limits, hc-usage-credits]
volatility: 高
sections:
  - {title: 比べる観点, anchor: what-to-compare}
  - {title: プランの表（確認日つき）, anchor: plan-table}
  - {title: 判断例, anchor: examples}
  - {title: 組み合わせ方, anchor: combining}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：アプリ中心で上限に当たらないなら今の段、Claude Code を長く回して上限に当たるなら上の段、という基準で個人向けのプランを選べる。
    - **いつ引くか**：どのプランにすべきか迷うとき。今のプランから上げるべきか迷うとき。プランの名前が変わり、どれが前のどれに当たるか分からないとき。Claude Code をよく使うので、合うプランを知りたいとき。
    - **前提**：<!-- link:begin how-usage-limits-work -->[利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)<!-- link:end -->

<!-- textlint-disable -->
別名：料金プラン・プランの比較・個人向けプラン・サブスクリプション
<!-- textlint-enable -->

プランの選び方は、個人向けの有料プランのどの段にするかを決める話である。このページは段を選ぶ基準を書き、料金と倍率は確認日つきの表に任せる。組織で使うプランは別の話で、<!-- link:begin choosing-an-org-plan -->組織で使うプランの選び方<!-- link:end --> が扱う。

## 比べる観点 {#what-to-compare}

個人向けのプランを比べる観点は 4 つある。どれも、自分がどう使うかから決まる。

- **使う面**：アプリ・Claude Code・Desktop の使用は、同じ利用枠に数えられる。Claude Code だけを使う人も、アプリだけを使う人も、見る枠は同じである。枠の仕組みは <!-- link:begin how-usage-limits-work#shared-limit -->[利用上限の仕組み（面をまたいで共有する枠） › 面をまたいで一つの枠](how-usage-limits-work.md#shared-limit)<!-- link:end --> にある。
- **Claude Code の量**：Claude Code は Pro・Max・Ultra のプランで使える（[Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)）。長い作業を回す人ほど枠が早く減るので、いちばん効く観点になる。いま枠をどれだけ使っているかは <!-- link:begin how-usage-limits-work#where-to-check -->[利用上限の仕組み（面をまたいで共有する枠） › 残りを見る場所](how-usage-limits-work.md#where-to-check)<!-- link:end --> で見る。
- **上位のモデルの扱い**：最上位のモデルは、プランによって、枠に含まれるか usage credits から引かれるかが違う。使う予定があるなら、先に <!-- link:begin before-using-top-model#which-limit -->[最上位のモデルを使う前に › どの枠から引かれるか（プランごとの表）](before-using-top-model.md#which-limit)<!-- link:end --> で引かれ方を確かめる。
- **上限の形**：5 時間の上限と週の上限のどちらを持つかは、プランで違う。短い時間に集中して使う人には 5 時間の上限が効き、毎日少しずつ使う人には週の上限が効く。持ち方と倍率は、次の節の表で見る。

月額は、4 つの観点で候補を絞った後に見る。円での支払いと消費税は <!-- link:begin paying-in-yen#currency-and-tax -->円での支払い・消費税・インボイス<!-- link:end --> が扱う。

## プランの表（確認日つき） {#plan-table}

個人向けのプランを、上限の形と倍率で比べる表を置く。表は数値ファイルから道具が作る。倍率は Pro を基準にした比で、Pro の量そのものは表にない。

<!-- gen:begin fact-table usage-limit-types-by-plan -->
<!-- textlint-disable -->

| プラン | 5 時間の上限 | 週の上限 | 最上位のモデルの別の週の上限 |
| --- | --- | --- | --- |
| Pro | あり | あり（基準） | —（確かめていない） |
| Max | あり（Pro の 5 倍） | Pro の 5 倍 | あり |
| Ultra | 確認済みの口座にはない（確認前は一時的な上限） | Pro の 10 倍 | あり |
| Team | —（束の材料に席ごとの値がない） | — | — |
| Enterprise（使用量に基づく） | なし | なし | — |

確認日 2026-11-04。出典：[What is the Ultra plan?](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan)、[What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)、[What is the Pro plan?](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)、[What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)、[What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)、[Plans & pricing](https://claude.com/pricing)。

<!-- textlint-enable -->
<!-- gen:end fact-table usage-limit-types-by-plan -->

個人向けの月額と払い方は、次の表のとおりである。

<!-- gen:begin fact-table plan-prices-individual -->
<!-- textlint-disable -->

未確認

<!-- textlint-enable -->
<!-- gen:end fact-table plan-prices-individual -->

表の読み方は次のとおりである。

- **5 時間の上限が自分の口座にあるか**：アプリの Settings > Usage に Current session の棒がなければ、5 時間の上限がない口座である。<!-- name:begin max-20x-to-ultra -->Ultra<!-- name:end --> の確認は口座と支払いの履歴などから自動で行われ、済むまでは一時的な上限がかかる。電話番号の確認は別のもので、この上限を外さない（[What is the Ultra plan?](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan)）。
- **「—」の欄**：この辞典がまだ確かめていない値で、「ない」という意味ではない。
- **Team と Enterprise の行**：組織のプランの行は、個人の選択には使わない。組織のプランは <!-- link:begin choosing-an-org-plan -->組織で使うプランの選び方<!-- link:end --> で比べる。
- **月額**：上の個人向けの月額の表で見る。月額と、年払いが選べるかは、プランで違う。[Plans & pricing](https://claude.com/pricing) でも確かめる。Max の記事は、モバイルで買う価格が Web と異なる場合があると書く（[What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)）。
- **最上位のモデル**：枠への含まれ方は <!-- link:begin before-using-top-model#which-limit -->[最上位のモデルを使う前に › どの枠から引かれるか（プランごとの表）](before-using-top-model.md#which-limit)<!-- link:end --> の表で見る。
- **プランに付く API credits**：付くプランと使い道は <!-- link:begin check-billing-path#monthly-api-credits -->[課金の経路を確かめる（API キーとサブスクリプション） › プランに付く API credits](check-billing-path.md#monthly-api-credits)<!-- link:end --> で確かめる。

プランの名前は変わったことがある。古い記事や社内の規程にある Max 5x・Max 20x の語は古い。Max 20x と呼んだ段は、今は <!-- name:begin max-20x-to-ultra -->Ultra<!-- name:end --> で、契約は料金そのままで移った。今の Max は 1 つの段で、Max 5x を改名したとは公式は書いていない。台帳の行は <!-- link:begin outdated-advice-ledger#max-5x-or-20x -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#max-5x-or-20x)<!-- link:end --> にある。旧名から今の名前を引くには <!-- link:begin term-index#old-names -->[用語索引と旧名の対応 › 旧名から引く](../start/term-index.md#old-names)<!-- link:end -->、変わった時期は <!-- link:begin change-timeline-2026#timeline -->[2026 年の主な変更の年表 › 年表](../changes/change-timeline-2026.md#timeline)<!-- link:end --> で確かめる。

旧 Max 20x と <!-- name:begin max-20x-to-ultra -->Ultra<!-- name:end --> で使える量が同じかは、一次資料で確かめられていない。Help Center と料金のページは料金が変わらないことを書くが、週の上限が前と同じかは書いていない。同じだという説明がネットにあっても、確かめるまでは、社内に量が同じだと説明しない。

## 判断例 {#examples}

!!! example "判断例：週に何度も 5 時間の上限に当たる"
    - **状況**：Pro で Claude Code を毎日使っている。ここ数週間、週に何度も 5 時間の上限に当たり、昼前に作業が止まる。
    - **迷う候補**：上の段に上げる。上げずに、超えた分を usage credits で払う。
    - **選んだもの**：上の段に上げる。
    - **理由**：当たる頻度が高いのは、枠の大きさが使い方に合っていないということである。超過分の支払いが毎週続くので、続く支払いと上の段の月額を、料金のページで見比べる。上の段は、Pro からなら Max が最初の候補である。Max でも当たるなら Ultra を考える。倍率と上限の形は、プランの表で見る。月に 1 回か 2 回しか当たらないなら、usage credits で足りる。先に Settings > Usage で、何回当たったかを数える。

!!! example "判断例：社内の規程に Max 20x と書いてある"
    - **状況**：社内の導入手順に「Max 20x を契約する」と書いてある。新しく契約したいが、今のプランの一覧に Max 20x がない。
    - **迷う候補**：今の Max を契約する。<!-- name:begin max-20x-to-ultra -->Ultra<!-- name:end --> を契約する。
    - **選んだもの**：<!-- name:begin max-20x-to-ultra -->Ultra<!-- name:end --> を候補にし、規程が想定した量を確かめてから契約する。
    - **理由**：Max 20x と呼んだ段が、今の <!-- name:begin max-20x-to-ultra -->Ultra<!-- name:end --> である。ただ、使える量が前と同じかは一次資料にない。規程の目的を確かめ、数日使って足りるかを見る。規程は今の名前に書き直す。

!!! example "判断例：アプリが中心で、最上位のモデルを少し試したい"
    - **状況**：Pro でアプリを使っていて、Claude Code はときどきしか使わない。最上位のモデルを試したくて、上の段に上げるか迷っている。
    - **迷う候補**：上の段に上げる。今の段のまま試す。
    - **選んだもの**：今の段のまま、先に引かれ方を確かめて試す。
    - **理由**：最上位のモデルが枠に含まれるかはプランで違い、含まれなくても usage credits で試せる。試すためだけに上げるのは、続けて使うと分かってからでよい。引かれ方は <!-- link:begin before-using-top-model#which-limit -->[最上位のモデルを使う前に › どの枠から引かれるか（プランごとの表）](before-using-top-model.md#which-limit)<!-- link:end --> で確かめる。数日試しても枠が足りないなら、そのときに上げる。

## 組み合わせ方 {#combining}

プランは、ほかの支払いと組み合わせて使う。何をどこに置くかを先に決めておく。

- **ふだんの量はプランの枠に置く**：プランの表で、自分の使い方に合う段を選ぶ。
- **超えた分は usage credits が受け持つ**：有効にすると、プランの上限を使い切った後も従量課金で続けられる。思わぬ請求を防ぐため、月の上限額と通知を先に決める。決め方は <!-- link:begin usage-credits-basics#set-a-cap -->[usage credits（上限を超えた分の従量課金） › 上限額と通知を決める](usage-credits-basics.md#set-a-cap)<!-- link:end --> を見る。
- **プランに付く API credits は API キー経由の用途に置く**：使える先は API キー経由の用途だけである。対話の Claude Code と usage credits は対象外である。詳しくは <!-- link:begin check-billing-path#monthly-api-credits -->[課金の経路を確かめる（API キーとサブスクリプション） › プランに付く API credits](check-billing-path.md#monthly-api-credits)<!-- link:end --> を見る。
- **Claude Code の課金の経路を確かめる**：環境変数・起動の仕方・面で、プランから引かれるか従量課金になるかが変わる。無人で回す前に <!-- link:begin check-billing-path#check-current-path -->[課金の経路を確かめる（API キーとサブスクリプション） › 今の経路を確かめる](check-billing-path.md#check-current-path)<!-- link:end --> で確かめる。
- **上げる前にモデルの選び方を済ませる**：上位のモデルに替えるほど枠は早く減る。プランを上げる前に、<!-- link:begin choosing-a-model#three-steps -->[モデルの選び方（三段階） › 三段階：既定 → effort → 上位のモデル](../models/choosing-a-model.md#three-steps)<!-- link:end --> の順を済ませているかを見る。プランとの関係は <!-- link:begin choosing-a-model#plans -->[モデルの選び方（三段階） › プランとの関係](../models/choosing-a-model.md#plans)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Plans & pricing](https://claude.com/pricing)：Anthropic・英語・確認日 2026-11-04
- [What is the Pro plan?](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)：Anthropic・英語・確認日 2026-11-04
- [What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)：Anthropic・英語・確認日 2026-11-04
- [What is the Ultra plan?](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)：Anthropic・英語・確認日 2026-11-04
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)：Anthropic・英語・確認日 2026-11-04
- [Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)

**関連**

- [最上位のモデルを使う前に](before-using-top-model.md)
- [usage credits（上限を超えた分の従量課金）](usage-credits-basics.md)
- [課金の経路を確かめる（API キーとサブスクリプション）](check-billing-path.md)
- [モデルの選び方（三段階）](../models/choosing-a-model.md)
- [節約の優先順位（手戻りを減らすのが先）](saving-priorities.md)
- [用語索引と旧名の対応](../start/term-index.md)
- [2026 年の主な変更の年表](../changes/change-timeline-2026.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
