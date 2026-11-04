---
id: saving-priorities
title: 節約の優先順位（手戻りを減らすのが先）
nav_title: 節約の優先順位
aliases: [節約のコツ, トークンを節約する, 使用量を減らす]
type: concept
field: cost
chapter: 上限と節約
order: 30
level: 整える
priority: 必須
surfaces: [app, claude-code, api]
principle: [確かめる, 見せる]
prevents: [合っていない, 散らかっている]
pitfalls: []
summary: 小手先の節約より、計画と確かめで手戻りを減らすほうが効く理由が分かる。次に関係のない文脈を片付けて常駐するものを減らし、effort やモデルを下げるのは最後にする。
signs:
  - {type: goal, text: 上限に当たらないように、使い方を節約したい}
  - {type: situation, text: 節約のコツをいろいろ試したが、あまり変わらない}
prerequisites: [what-uses-up-limits]
related: [define-done, when-to-plan, when-to-start-fresh, always-on-costs, pruning-extensions, hook-recipes, verification-ladder, effort-levels, split-models-by-role]
tracks: []
outdated_advice: []
sources: [hc-usage-limit-best-practices, cc-docs-costs, cc-docs-model-config, api-docs-effort, hyperdev-tired-toddler-problem]
volatility: 中
sections:
  - {title: 優先順位, anchor: order}
  - {title: 手戻りが高くつく理由, anchor: why-rework}
  - {title: 手戻りを減らす, anchor: reduce-rework}
  - {title: 文脈と常駐物を片付ける, anchor: clean-up}
  - {title: effort とモデルは最後に触る, anchor: last}
  - {title: 面ごとの節約の手段, anchor: by-surface}
  - {title: 何に効くか, anchor: effect}
  - {title: 誤解しやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：節約は、計画と確かめで手戻りを減らすのが一番手で、次が文脈と常駐物の片付け、effort とモデルを下げるのは最後だと分かる。
    - **いつ引くか**：節約のコツを試したのに使用量があまり減らないときや、上限に当たらないよう、どこから手を付けるか決めたいとき。
    - **前提**：<!-- link:begin what-uses-up-limits -->[上限を早く使う要因](what-uses-up-limits.md)<!-- link:end -->

<!-- textlint-disable -->
別名：節約のコツ・トークンを節約する・使用量を減らす
<!-- textlint-enable -->

節約の優先順位は、使用量を減らす手段を、手を付ける順に並べた考え方である。ここでの手戻りは、Claude の答えが外れて、訂正や作り直しの往復が増えることをいう。小さな工夫を足す前に、この往復そのものを減らす。

## 優先順位 {#order}

節約の手段は、手を付ける順に並べると 5 つになる。上のものほど先に手を付ける。順位の根拠は、下の 3 段の整理にある。

| 順 | 手段 | この位置に置く理由 |
| --- | --- | --- |
| 1 | 計画と確かめで手戻りを減らす | 往復の数そのものが減る。直しの往復ごとに、それまでの履歴の送り直しが加わるため |
| 2 | 関係のない文脈を片付ける | 話題が変わった後の履歴は、毎回送られるのに答えの役に立たない |
| 3 | 常駐するものを減らす | 毎回のリクエストに乗るので、使わない回の分も積もる |
| 4 | 出力を絞る | テスト出力やログの全文は文脈に残り、後の往復で送られ続ける |
| 5 | effort とモデルを下げる | 1 回の単価は下がるが、答えが外れて手戻りが増えれば、かえって高くつく |

この順位は、立場が 3 段に分かれる。

- **公式の立場**：節約の手段を多く挙げている。計画する・具体的に頼む・無関係な作業の間で `/clear` する・常駐物を減らす・effort を下げる・モデルを使い分ける、などである。
- **実践者の幅**：一番効くのは手戻りを減らすことだという報告がある。ある実践者の自己申告では、トークンの約半分が訂正に消えた（根拠：弱・自己申告。経験則として読む）。
- **この辞典の推奨**：上の順に手を付ける。手戻りを減らす手段は品質も上げ、effort を下げる手段は品質を下げうるため、順位は後者が最後になる。この順位そのものを測った研究は、束の材料には見当たらない。

## 手戻りが高くつく理由 {#why-rework}

手戻りが高くつくのは、Claude が毎回のリクエストで会話の全履歴を読み直すからである。毎回読み直す受験者に、訂正のたびに問題用紙が 1 枚ずつ足されると考えると近い。

たとえば「ログインの不具合を直して」と頼んだところ、Claude が別の箇所を直したとする。「そこではない」と返すと、次のリクエストには、最初の依頼・見当違いの作業・訂正のすべてが乗る。もう 1 度外れれば、さらに積み上がる。1 往復の費用は小さく見えても、往復が増えるほど 1 回ごとの送り直しが重くなる。

公式の文書は、長いセッションで使用量が増える理由として、毎リクエストの履歴の再送、休止後のキャッシュミス、圧縮そのものの費用などを挙げている。詳しい仕組みは <!-- link:begin what-uses-up-limits#long-sessions -->[上限を早く使う要因 › 長いセッションで増える理由](what-uses-up-limits.md#long-sessions)<!-- link:end --> にある。

外れた作業の結果が履歴に残ると、費用だけでなく焦点も散らかる。外れた方針の説明が文脈に残り、次の答えを引きずるためである。散らかった後の立て直しは <!-- link:begin when-to-start-fresh#why -->[新しい会話を始めるタイミング › なぜ新しくすると答えがよくなるか](../context/when-to-start-fresh.md#why)<!-- link:end --> にある。

## 手戻りを減らす {#reduce-rework}

手戻りを減らすには、実装に入る前と終わった後の両方で、誤解を安く見つける。公式の文書も、plan mode・早期の軌道修正・検証の目標を、費用の削減策に挙げている。

- **計画を読んで直してから実装に入る**：誤解は計画の段階で見つけるほど安く直せる。計画の読み方は <!-- link:begin when-to-plan#review -->[plan mode の使いどころ › 計画の読み方と直し方](../cli/when-to-plan.md#review)<!-- link:end --> にある。
- **完了を測れる形で渡す**：終わりとなるコマンドの返りを先に決める。入れるものは <!-- link:begin define-done#what-to-include -->[「完了」を定義して渡す › 完了の定義に入れるもの](../verify/define-done.md#what-to-include)<!-- link:end --> にある。
- **確かめる手段を渡す**：「念のため確認して」と書き足すより、テストやコマンドなど確かめる手段を渡す。段の選び方は <!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](../verify/verification-ladder.md#choose-step)<!-- link:end --> にある。
- **外れたら早く止めて直す**：外れた方向のまま進めさせると、履歴に外れた作業が積み上がる。数ターン進めてから直すより、気づいた時点で直す。

小さな作業では、計画を省いてよい。省く目安は <!-- link:begin when-to-plan#when -->[plan mode の使いどころ › 計画が効く作業、省いてよい作業](../cli/when-to-plan.md#when)<!-- link:end --> にある。

!!! example "判断例：上限が近い週の、機能追加の依頼"
    - **状況**：週の上限が近い。範囲が曖昧な機能追加を、これから頼む。
    - **迷う候補**：effort を下げてすぐ実装させる。または、先に plan mode で計画を出させ、読んで直してから実装に入る。
    - **選んだもの**：先に計画を出させ、完了の条件を決めてから実装に入る。
    - **理由**：範囲が曖昧なまま実装すると、外れた作業の訂正が何往復も続きやすい。計画の読み直し 1 回のほうが、訂正の往復より安い。範囲が明確な小さな作業なら、すぐ実装させて effort を下げる選択も筋が通る。

## 文脈と常駐物を片付ける {#clean-up}

手戻りを減らした後に効くのは、答えの役に立たないのに毎回送られるものを片付けることである。対象は 3 つある。

- **関係のない文脈**：無関係な作業の間で `/clear` する。新しい会話に移す合図は <!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end --> にある。
- **常駐するもの**：`CLAUDE.md` の全文・スキルの説明・MCP のツールの一覧は、毎回のリクエストに乗る。使わない接続は外し、必要なときだけ読ませる形に移す。減らす順は <!-- link:begin always-on-costs#reduce -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 減らす順](../context/always-on-costs.md#reduce)<!-- link:end --> にある。入れた拡張の見直しは、先に常駐の費用を測ってから切る（<!-- link:begin pruning-extensions#measure -->[拡張の棚卸しと剪定 › 測る](../extend/pruning-extensions.md#measure)<!-- link:end -->）。
- **出力**：テスト出力は失敗の行だけに絞る。フックで絞る形は <!-- link:begin hook-recipes#filter-test-output -->[代表的なフックのレシピ › テストの出力を絞る](../enforce/hook-recipes.md#filter-test-output)<!-- link:end --> にある。

## effort とモデルは最後に触る {#last}

effort やモデルを下げるのは、ほかの手段を試した後にする。下げる前は、既定の段で何が起きているかを測る。

下げる手段を最後に置く理由は、答えの質が下がると手戻りが増えうる点にある。公式の文書は、最高の段は考えすぎることもあると注意している。つまり、上げ下げのどちらも、既定から始めて自分の作業で確かめる対象である。API 側の文書も、旧モデルの設定を流用せず、自分の評価で段を振って確かめるよう勧めている。

下げてよい仕事もある。軽い仕事のモデルを軽くする判断は、<!-- link:begin split-models-by-role#lighter-models -->[計画・実装・サブエージェントでモデルを分ける › 軽いモデルの使いどころ](../models/split-models-by-role.md#lighter-models)<!-- link:end --> にある。段ごとの振る舞いは <!-- link:begin effort-levels#levels -->[effort の段階と使い分け › 段ごとの振る舞い](../models/effort-levels.md#levels)<!-- link:end --> にある。下げた後に訂正の往復が増えたら、元の段に戻す。

## 面ごとの節約の手段 {#by-surface}

面ごとに、使える節約の手段が違う。以下は、2026 年 10 月に公式の文書で確かめた範囲である。

=== "アプリ"

    - **始める前に計画する**：関連する質問は 1 通にまとめて送る。
    - **具体的に書く**：曖昧な依頼は、訂正の往復を生む。
    - **よく使う資料は project に置く**：同じ資料を毎回貼り直さずに済む。
    - **進み具合を見る**：Settings の Usage で、使用量の進捗バーを確認する。見る場所は <!-- link:begin what-uses-up-limits#find-what-uses-it -->[上限を早く使う要因 › /usage の内訳の読み方（自分の場合を確かめる）](what-uses-up-limits.md#find-what-uses-it)<!-- link:end --> にもある。

=== "Claude Code"

    - **内訳を見る**：`/usage` で、セッションの費用・プラン使用量・内訳・推奨を確認する。
    - **状況を常に見せる**：status line に、コンテキストの使用率と利用枠の使用率を表示しておくと、枠切れで作業が止まる前に気づける。
    - **作業の間で片付ける**：無関係な作業の間に `/clear` する。その前に `/rename` で名前を付けておくと、後で戻れる。`/clear` 自体に費用はかからない。
    - **常駐物と出力を絞る**：使わない MCP を無効にし、テスト出力は失敗の行だけにする。
    - **確認の範囲**：WSL と Linux の CLI を基準にした。ほかの OS と IDE 拡張の動作は未確認である。

=== "API"

    - **effort は評価で決める**：旧モデルの設定を流用せず、自分の評価で段を振って確かめる。
    - **送る内容を自分で決める**：履歴を持つのは呼び出す側なので、関係のない履歴を送らないのも、手戻りで増えた履歴を整理するのも自分の仕事である。
    - **確認の範囲**：API 料金の読み方は、この辞典の別のページで扱う。ここでは手段の優先順位だけを書き、料金の数値は確かめていない。

## 何に効くか {#effect}

この順位が効くのは、原理の「確かめる」「見せる」と、Claude 側の原因の「合っていない」「散らかっている」に当たる部分である。

- **確かめる（原理）**：計画を読む・完了を測る・確かめる手段を渡す、はどれも、合っていない出力を早い段で見つける。早いほど直しの往復が少なく、履歴に積み上がる量も少ない。
- **見せる（原理）**：`/usage` や status line や Settings の Usage は、何が使っているかを見せる。見えれば、自分の場合に効く手段を選べる。
- **合っていない（原因）**：外れた答えは、訂正の往復を生み、使用量を増やす。節約の一番手が手戻りの削減なのは、この原因に当たるからである。
- **散らかっている（原因）**：関係のない履歴と使わない常駐物は、費用を増やすだけでなく焦点も散らす。片付けると、費用と答えの質の両方に効く。常駐を小さく保つ理由は <!-- link:begin always-on-costs#why-small -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › なぜ常駐を小さく保つのか](../context/always-on-costs.md#why-small)<!-- link:end --> にある。

## 誤解しやすいこと {#misconceptions}

節約の話には、順位を取り違えやすい誤解がある。

- **「節約のコツは、全部やるほど効く」**：手戻りが多いままなら、ほかの手段の効きは小さい。順位の高い手段から試す。
- **「effort を下げれば確実に安くなる」**：1 回の単価は下がっても、答えが外れて往復が増えれば逆になりうる。下げた後は、訂正の往復が増えていないかを見る。
- **「`/clear` で上限が戻る」**：戻らない。`/clear` は文脈を空にするだけで、使った分の枠は戻らない。戻らないものは <!-- link:begin when-to-start-fresh#what-does-not-reset -->[新しい会話を始めるタイミング › 新しくしても戻らないもの（上限・記憶）](../context/when-to-start-fresh.md#what-does-not-reset)<!-- link:end --> にある。
- **「常駐物は削るほどよい」**：必要な指示まで外すと、指示が届かず手戻りが増える。移すときの落とし穴は <!-- link:begin always-on-costs#misconceptions -->[常駐するもののコスト（CLAUDE.md・MCP・スキル） › 誤解と、移すときの落とし穴](../context/always-on-costs.md#misconceptions)<!-- link:end --> にある。
- **「計画はいつも要る」**：小さな作業では、計画の読み直しのほうが高くつく。
- **「手戻りで半分が消える、は一般の数字」**：個人の自己申告であり、一般の割合として使わない。自分の場合は、`/usage` の内訳で確かめる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [上限を早く使う要因](what-uses-up-limits.md)

**関連**

- [「完了」を定義して渡す](../verify/define-done.md)
- [plan mode の使いどころ](../cli/when-to-plan.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [常駐するもののコスト（CLAUDE.md・MCP・スキル）](../context/always-on-costs.md)
- [拡張の棚卸しと剪定](../extend/pruning-extensions.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [検証の階段](../verify/verification-ladder.md)
- [effort の段階と使い分け](../models/effort-levels.md)
- [計画・実装・サブエージェントでモデルを分ける](../models/split-models-by-role.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)：Anthropic・英語・確認日 2026-11-04
- [Manage costs effectively](https://code.claude.com/docs/en/costs)：Anthropic・英語・確認日 2026-11-04
- [Model configuration](https://code.claude.com/docs/en/model-config)：Anthropic・英語・確認日 2026-11-04
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)：Anthropic・英語・確認日 2026-11-04
- [The Tired Toddler Problem](https://hyperdev.matsuoka.com/p/the-tired-toddler-problem)：Matsuoka（HyperDev）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
