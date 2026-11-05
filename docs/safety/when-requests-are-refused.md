---
id: when-requests-are-refused
title: 正当な依頼が断られたとき
aliases: [断られた, モデルが切り替わった, 断られたときの頼み直し]
type: concept
field: safety
chapter: 規則と開示
order: 180
level: 使う
priority: 推奨
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない]
pitfalls: []
scenes: [開発, 調べもの]
summary: 正当な依頼が止められたときに、公式が案内する手段（巻き戻しや新しい会話で引き金を外す・本当の目的と文脈を足す・誤判定を報告する・検証の制度）から選べる。面ごとの表示と、分類器が会話全体を見る仕組み・自動のモデルの切り替えも分かる。
signs:
  - {type: goal, text: 誤って断られた依頼を、どう頼み直せばよいか知りたい}
  - {type: goal, text: 返事のモデルが途中で切り替わった理由を知りたい}
  - {type: situation, text: セキュリティや生命科学の正当な仕事に Claude を使っている}
prerequisites: []
related: [refused-or-blocked, give-reasons, checkpoints-and-rewind, when-to-start-fresh, rewind-dont-correct, asking-for-reasoning#refusal, isolate-with-safe-mode, what-feedback-sends, checking-ai-rules, where-your-data-goes, what-auto-mode-stops#when-blocked]
tracks: [refusals]
sources: [hc-switched-models, hc-output-blocked, api-docs-refusals, cc-docs-model-config, cc-docs-errors, hc-cyber-verification-program, anthropic-legal-aup, anthropic-constitution]
volatility: 高
sections:
  - {title: 面ごとの表示と仕組み（分類器が見るもの・自動のモデルの切り替え）, anchor: by-surface}
  - {title: 公式が案内する手段, anchor: official-steps}
  - {title: 手段が何に効くか（見せる・見えていない）, anchor: effect}
  - {title: 分類器を避ける頼み方をしない理由（利用ポリシー）, anchor: why-not-evade}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：正当な依頼が止められたときに、公式が案内する手段（引き金を外す・目的を足す・報告する・検証の制度）から選べる。
    - **いつ引くか**：誤って断られた依頼をどう頼み直すか知りたいとき、返事のモデルが途中で切り替わった理由を知りたいとき、セキュリティや生命科学の正当な仕事に Claude を使っているとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：断られた・モデルが切り替わった・断られたときの頼み直し
<!-- textlint-enable -->

正当な依頼が断られたときは、分類器が会話全体を見て判定していることを知ったうえで、公式が案内する手段から選ぶ。この記事は、止められる仕組みと、頼み直しの手段と、その手段が効く理由を扱う。止められたものが利用ポリシーの判定か auto モードやフックの停止かを見分ける手順は <!-- link:begin refused-or-blocked#what-stopped -->[断られた・止められた › 何に止められたかを見分ける（利用ポリシーか、auto モード・フック・権限ルールか）](../symptoms/refused-or-blocked.md#what-stopped)<!-- link:end --> にある。

## 面ごとの表示と仕組み（分類器が見るもの・自動のモデルの切り替え） {#by-surface}

正当な依頼が止められるのは、分類器が会話全体を見て、問題がありそうだという印（この記事では「旗」と呼ぶ）を立てるからである。公式の記事によると、対象のモデルではすべての依頼に分類器がかかる。分類器が見るのは、利用者が打った文だけではない。モデルが読むもの（メモリ・コネクタの内容・Web 検索の結果・ファイル）も見る。会話は広い机の上に並んだ全部であり、分類器はその机を端から見る。だから、打っていない内容が引き金になりうる。

旗が立つ分野には、サイバー（攻撃用コードの生成など）と生物（両用の知識）がある。ほかにも分野があり、対象のモデルと分野は変わるので、公式の記事で確かめる。旗が立つと、能力の低いモデルで答え直すか、そこで止まる。推論の抜き出しは切り替えずに止まる。公式は、分類器が正当な依頼も止めることがあり、減らす努力を続けていると書く。

表示と設定は面で違う。

=== "アプリ"
    - **切り替え**：旗が立つと、能力の低いモデルで答え直す。返事のモデルが途中で変わったときは、この仕組みが働いている。
    - **設定**：自動の切り替えは、Settings > Capabilities の Switch models when a message is flagged で切れる（2026-11-04 時点、公式の記事による）。切ると、止まったところで会話が止まり、その先は利用者が選ぶ。
    - **戻し方**：切り替えの後で元のモデルへ戻すと、同じ判定がまたかかりうる。公式は、前のメッセージを直してから送るよう書く。

=== "Claude Code"
    - **表示**：新しい会話を始めるよう促す文が出る。判定は会話全体にかかるので、同じセッションで送り直しても、`--continue` や `--resume` で開き直しても、また止まる。
    - **サイバーの分類**：別の表示になり、検証の制度へのリンクが付く。自動の切り替えがあるモデルでは表示の文が違い、このリンクは付かない。分類ごとの切り替えが要る版は、<!-- fact:begin refusals-cc-per-category-switch-min-version -->未確認<!-- fact:end -->である。
    - **既定**：自動の切り替えの既定は、（<!-- fact:begin refusals-auto-switch-default -->未確認<!-- fact:end -->）である。
    - **設定**：自動の切り替えは、`/config` の Switch models when a message is flagged（設定のキーは `switchModelsOnFlag`）で切れる（2026-11-04 時点）。
    - **文の確かめ方**：表示の文は版で変わる。手元の文は [Error reference](https://code.claude.com/docs/en/errors) で突き合わせる。

=== "API"
    - **拒否の形**：拒否はエラーではなく、HTTP 200 の普通の応答である。`stop_reason` が `refusal` になり、`stop_details.category` が分野を示す。分野の値は、（<!-- fact:begin refusals-api-categories -->未確認<!-- fact:end -->）である。
    - **引っかかり**：どの分類でも、無害な仕事が引っかかりうると文書は書く。
    - **自動の切り替え**：リクエストに `fallbacks` を設定して使う。詳しくは [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback) にある。
    - **課金**：拒否の課金の扱いは分野で違い、何度か変わった。現在の扱いは、（<!-- fact:begin refusals-billing-by-category -->未確認<!-- fact:end -->）である。同じ文書で確かめる。

別の仕組みに、「Output blocked by content filtering policy」のエラーがある。これは既存の著作物をそのまま再現させないためのもので、内容の是非の判断ではない。公式の説明は [Why am I receiving an 'Output blocked by content filtering policy' error?](https://support.claude.com/en/articles/9205721-why-am-i-receiving-an-output-blocked-by-content-filtering-policy-error) にある。モデルの切り替えの設定は [Model configuration](https://code.claude.com/docs/en/model-config) に、切り替えの理由は [Why Claude switched models in your conversation with Opus 5 or Opus 5.5](https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5-or-opus-5-5) にある。

## 公式が案内する手段 {#official-steps}

正当な依頼が止められたときに公式が案内する手段は、引き金を会話から外す・推論の全文を求める指示を外す・本当の目的と文脈を足す・誤判定を報告する・検証の制度に申し込む、の 5 つである。選び方は原因の見立てによる。引き金になった内容が会話に残っていそうなら 1、設定や CLAUDE.md に推論を求める指示がありそうなら 2、依頼の目的が伝わっていないなら 3、誤判定だと思うなら 4、継続する専門の仕事なら 5 を使う。1 と 3 と 4 は重ねてよい。

1. **引き金になったやり取りより前に戻す。** Claude Code では Esc を 2 回押すか `/rewind` を使う。どこが原因か分からなければ `/clear` で新しい会話にする（前の会話は `/resume` に残る）。`-p` では `--continue` を付けずに新しいセッションで言い直す。アプリでは前のメッセージを直して送る。判定が会話全体にかかるので、止まった内容を会話に残さないことが効く。手順は <!-- link:begin checkpoints-and-rewind#how-to -->[チェックポイントと /rewind（git との違い） › 最小の使い方](../cli/checkpoints-and-rewind.md#how-to)<!-- link:end --> と <!-- link:begin rewind-dont-correct#how -->[違うと返すより、巻き戻す・編集する › 面ごとの戻し方](../context/rewind-dont-correct.md#how)<!-- link:end --> に、新しくする合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。
2. **推論の全文や決まった形を求める指示を外す。** `<thinking>` の欄や JSON の reasoning の欄を求める指示は、止まる原因になる。CLAUDE.md・スキル・サブエージェント・出力スタイル・MCP のツールの説明に入っていることもあり、`claude --safe-mode` で設定を外すと切り分けられる。理由を知りたいときは、短い説明か根拠の要約を頼む。経緯は <!-- link:begin asking-for-reasoning#refusal -->[推論を見せてほしいとき › 全文を求める指示が断られる理由](../prompting/asking-for-reasoning.md#refusal)<!-- link:end --> に、切り分けは <!-- link:begin isolate-with-safe-mode#compare -->[設定を外して切り分ける（--safe-mode） › 比べ方](../cli/isolate-with-safe-mode.md#compare)<!-- link:end --> にある。
3. **本当の目的と文脈を足す。** 誰が、どの範囲で、何のために頼んでいるかを、事実のとおりに書く。同じ会話では止まり続けることがあるので、1 の戻した先か新しい会話の最初に書く。理由を添えると意図が伝わる仕組みは <!-- link:begin give-reasons#what-changes -->[理由を添える › 理由を添えると何が変わるか](../prompting/give-reasons.md#what-changes)<!-- link:end --> にある。偽の文脈は手段に入らない。入らない理由は、このページの節「分類器を避ける頼み方をしない理由（利用ポリシー）」に書いた。
4. **誤判定を報告する。** アプリは Send feedback から、Claude Code は `/feedback` から報告する（表示の Request ID を添えられる）。API ではサポートに request ID を添える。アカウントの停止には異議申し立ての窓口がある。報告では会話が送られるので、送る前に <!-- link:begin what-feedback-sends#what-is-sent -->[/feedback・トランスクリプトの共有で送られるもの › 送られるものと残る期間](what-feedback-sends.md#what-is-sent)<!-- link:end --> で中身を確かめる。
5. **正当な専門の仕事なら、検証の制度に申し込む。** サイバーは Cyber Verification Program がある。段階と個人で申し込める範囲は、（<!-- fact:begin refusals-cvp-tiers -->未確認<!-- fact:end -->）である。範囲は変わるので [Cyber Verification Program](https://support.claude.com/en/articles/14604842-cyber-verification-program) で確かめる。生命科学には Life Sciences Verification Program があり、組織向けと案内されている。

頼み直しの文は、同じ依頼で並べると差が分かる。

- **Before**：この Web アプリの脆弱性を突くコードを書いて。
- **After**：自社の検証環境にある Web アプリ（本番とは分離）の脆弱性診断をしている。診断の依頼書の範囲内で、見つかった入力検証の不備が修正後に直ったかを確かめるテストを書きたい。

After で足したのは、誰の環境か・どの範囲か・何のためか、の 3 つである。どれも事実のものだけを書く。足しても、同じ会話では止まり続けることがある。

!!! example "判断例：自社アプリの診断で止められた"
    - **状況**：Claude Code で自社 Web アプリの脆弱性診断を手伝わせている。ある依頼でサイバーの分類に止められ、目的を足して同じセッションで送り直したが、また止まった。
    - **迷う候補**：同じセッションで文面を整えて送り続ける。巻き戻して、または新しい会話にして、最初に目的と範囲を書く。
    - **選んだもの**：新しい会話にして、診断の目的と範囲を最初に書く。誤判定だと思うなら `/feedback` でも報告する。
    - **理由**：判定は会話全体にかかり、止まった内容が会話に残る限り、同じ会話では止まり続けるからである。診断が継続する仕事なら、検証の制度も候補になる。

## 手段が何に効くか（見せる・見えていない） {#effect}

5 つの手段は、原理「見せる」で、原因「見えていない」を埋める。見えていないものは 2 方向にある。

- **分類器から見えていないもの**：依頼の本当の目的と文脈。目的を足す手段が、これを見せる。
- **利用者から見えていないもの**：メモリ・コネクタ・検索の結果・ファイルのうち、引き金になった内容。巻き戻しと新しい会話が、これを机から外す。推論の全文を求める指示は、設定の中に隠れて見えていないことがある。

見えていないものは、見せるか外すかで扱う。報告と検証の制度は、会話の中では埋められない分を、判定する側に伝える手段である。

## 分類器を避ける頼み方をしない理由（利用ポリシー） {#why-not-evade}

分類器を避けるための頼み方は、手段に入れない。[Usage Policy](https://www.anthropic.com/legal/aup) は、製品に設けられた機能・制限・ガードレールを意図して回避したり妨げたりすることを禁じる。違反すれば、警告のほか、アクセスの制限や停止がありうる。

偽の文脈も同じ側にある。[Claude’s Constitution](https://www.anthropic.com/constitution) は、確かめられない理由でも文脈と理由は解釈を変えうるとし、偽りの文脈なら責任の一部は本人に移ると書く。正当な依頼なら、事実のとおりの目的を足し、止まるなら誤判定として報告する。規則の確かめ方は <!-- link:begin checking-ai-rules#checklist -->[学校・組織・コンテストの規則（類型と確認表） › 確認表](checking-ai-rules.md#checklist)<!-- link:end --> にある。

## よくある誤解 {#misconceptions}

- **止められたのは利用ポリシーの違反だ**：そうとは限らない。ポリシーは、止められたこと自体は違反を意味しないと書く。
- **文脈を足せば、同じ会話でも通る**：通らないことがある。分類器は会話全体と読み込んだ資料を見るので、止まった内容が残る限り止まり続ける。
- **モデルが途中で変わったのは不具合だ**：旗が立ったときの仕組みである。自動の切り替えは設定で切れる。
- **Output blocked は内容が悪いという判定だ**：違う。既存の著作物の再現を防ぐ仕組みである。

auto モードの分類器に操作を止められた場合の見直し方は、<!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Why Claude switched models in your conversation with Opus 5 or Opus 5.5](https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5-or-opus-5-5)：Anthropic・英語・確認日 2026-11-04
- [Why am I receiving an 'Output blocked by content filtering policy' error?](https://support.claude.com/en/articles/9205721-why-am-i-receiving-an-output-blocked-by-content-filtering-policy-error)：Anthropic・英語・確認日 2026-11-04
- [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)：Anthropic・英語・確認日 2026-11-04
- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [Error reference](https://code.claude.com/docs/en/errors)：Anthropic・英語・確認日 2026-11-04
- [Cyber Verification Program](https://support.claude.com/en/articles/14604842-cyber-verification-program)：Anthropic・英語・確認日 2026-11-04
- [Usage Policy](https://www.anthropic.com/legal/aup)：Anthropic・英語・確認日 2026-11-04
- [Claude’s Constitution](https://www.anthropic.com/constitution)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**関連**

- [断られた・止められた](../symptoms/refused-or-blocked.md)
- [理由を添える](../prompting/give-reasons.md)
- [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- [推論を見せてほしいとき › 全文を求める指示が断られる理由](../prompting/asking-for-reasoning.md#refusal)
- [設定を外して切り分ける（--safe-mode）](../cli/isolate-with-safe-mode.md)
- [/feedback・トランスクリプトの共有で送られるもの](what-feedback-sends.md)
- [学校・組織・コンテストの規則（類型と確認表）](checking-ai-rules.md)
- [送ったデータの行方（学習・保持期間）](where-your-data-goes.md)
- [auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
