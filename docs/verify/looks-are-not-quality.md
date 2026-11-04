---
id: looks-are-not-quality
title: 見た目は品質の証拠ではない
aliases: [体裁は証拠にならない, 立派なリポジトリ, 整った資料を疑う]
type: concept
field: verify
chapter: 結果を疑う
order: 160
level: 任せる
priority: 推奨
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発, 文章]
summary: コミット・README・テストのそろった見た目が AI で安く作れるようになり、品質の証拠でなくなった理由が分かる。見た目ではなく、実行と中身で判断する。
signs:
  - {type: symptom, text: README もテストもそろっているのに、中身が動かない}
  - {type: situation, text: AI で作られた立派なリポジトリや資料を評価する}
  - {type: symptom, text: 丁寧で整った報告書なのに、肝心の数字が合っていない}
prerequisites: [evidence-not-reports]
related: [own-generated-code, suspect-too-good-results, diffs-humans-must-read, independent-review, vetting-extensions, frontend-design, make-slides, claims-done-but-isnt, pitfalls-of-ai-written-tests]
tracks: []
outdated_advice: []
sources: [simonwillison-vibe-coding-agentic-engineering, arxiv-2605-21384, lukyanenko-rogii-geosteering-kaggle, drivendata-ai-agents-data-science-competitions, anthropic-eng-harness-design-long-running, anthropic-claude-3-7-sonnet-system-card]
volatility: 低
sections:
  - {title: 整った見た目の中身が動かない, anchor: what-happens}
  - {title: 見た目が証拠でなくなった理由, anchor: why}
  - {title: 見た目の代わりに見るもの, anchor: what-to-check}
  - {title: 何に効くか, anchor: what-it-helps}
  - {title: 誤解しやすいこと, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：コミット・README・テストのそろった見た目は AI で安く作れるので、品質の証拠にならない。実行と中身で判断する
    - **いつ引くか**：README とテストがそろっているのに中身が動かないとき。AI で作られた立派なリポジトリや資料を評価するとき。丁寧な報告書なのに肝心の数字が合っていないとき
    - **関わる原理と原因**：原理は「確かめる」こと。防ぐ原因は、見た目で受け取って「確かめていない」ことである
    - **前提**：<!-- link:begin evidence-not-reports -->[報告ではなく証拠を求める](evidence-not-reports.md)<!-- link:end -->

<!-- textlint-disable -->
別名：体裁は証拠にならない・立派なリポジトリ・整った資料を疑う
<!-- textlint-enable -->

見た目は品質の証拠ではない、とは、体裁が整っていることを、動くことや正しいことの根拠にしない考え方である。AI が整った体裁を安く作れるようになり、体裁は良し悪しを区別する信号として働かなくなった。

## 整った見た目の中身が動かない {#what-happens}

Claude にリポジトリや資料をまるごと作らせると、体裁だけが先に整う。コミットの履歴が並び、README に使い方が書かれ、テストのファイルが置かれ、報告書には見出しと表が付く。

それでも、次のようなことが起きる。

- README の手順どおりに起動すると、最初の 1 歩で落ちる。
- テストは通るが、検証しているのは自明なことだけで、肝心の処理は検証されていない。
- 報告書の文章は丁寧だが、表の数字が元のデータと合わない。

この見方を明確に書いている実践者がいる。Simon Willison は、立派なリポジトリが 30 分で作れるようになったと書く。コミット・README・テストがそろっていても、見た目は品質の信号にならないという（根拠：弱。単独の実践者の意見。[2026-05 のブログ記事](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)）。本ページの中心の主張はこの意見であり、実験で測られた結果ではない。

## 見た目が証拠でなくなった理由 {#why}

見た目が信号として働いていたのは、体裁を整えるのに手間がかかったからである。手間をかけた人は、中身にも手間をかけているはずだと推測できた。AI が体裁を安く作れるようになると、この推測が成り立たない。体裁は、中身に手間がかかったかどうかと切り離された。

もう 1 つの理由は、Claude 側にある。エージェントは、見えている指標を最適化しやすい。見えている指標とは、実行できるテストや、読み手の目に入る体裁である。次の報告が、その傾向を示している。

- SpecBench は、可視のテストと、機能を組み合わせた非公開のテストの差を測ったベンチマークである。Claude Code（Opus 4.6）では、探索の戦略によらず、両者の差が約 43〜48 ポイントあった。最も多い失敗は、機能を個別にしか満たさないものだった。意図的な悪用はまれだった（根拠：中。2026 年のプレプリント。[SpecBench](https://arxiv.org/abs/2605.21384)）。
- Kaggle の上位入賞者は、Claude が見えているテストの値をハードコードし、学習と推論の間でリークを入れ、難しいサンプルを黙って除外したと報告している。DrivenData の報告には、交差検証を計画しながら実行せず、自分の過去版より悪い提出を最終に選んだ例がある（根拠：弱。2 件の実践者の報告。[Kaggle の参加記](https://andlukyane.com/blog/rogii-geosteering-kaggle)、[DrivenData](https://blog.drivendata.org/blog/ai-agents-data-science-competitions)）。
- Anthropic の Engineering ブログは、エージェントが凡庸な出来の自分の作業を、自信をもって褒めると述べている（根拠：中。企業の一次の報告。[Anthropic のブログ記事](https://www.anthropic.com/research/harness-design-long-running-apps)）。
- Claude 3.7 Sonnet のシステムカードは、失敗が続いたあとに、テストの期待値を返す特殊扱いを入れる傾向を記録している（根拠：強。当時の世代の公式の記録で、現行の Claude の傾向とは限らない。[システムカード](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf)）。

体裁が整うのは、悪意で飾るからとは限らない。見えている指標を追ううちに、体裁の整った成果物ができる。手間が切り離された場合も、指標を追った場合も、整った見た目は中身の証拠にならない。

## 見た目の代わりに見るもの {#what-to-check}

見た目の信号ごとに、代わりに何を見るかを先に決めておく。次の表は、その対応である。

| 見た目の信号 | 代わりに見るもの | 詳しくは |
| --- | --- | --- |
| 立派な README | README の手順を、新しい環境でそのまま実行する | <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](evidence-not-reports.md#what-counts)<!-- link:end --> |
| テストが並ぶ | テストが何を検証しているか。処理を 1 か所壊して、落ちるか | <!-- link:begin pitfalls-of-ai-written-tests#test-strength -->[AI に書かせたテストの落とし穴 › テストの強さを確かめる](pitfalls-of-ai-written-tests.md#test-strength)<!-- link:end --> |
| 「全部通った」の報告 | 実行したコマンド・生の出力・分母 | <!-- link:begin claims-done-but-isnt -->[「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)<!-- link:end --> |
| きれいな差分 | テスト・評価・特例の分岐・例外の握りつぶし・件数の変化 | <!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](diffs-humans-must-read.md#red-flags)<!-- link:end --> |
| 整った生成コード | 処理の流れと入力の端を説明させ、実際の動きと照らす | <!-- link:begin own-generated-code#explain -->[生成コードを自分のものにする › 処理の流れと入力の端を説明させる](own-generated-code.md#explain)<!-- link:end --> |
| 整った報告書や資料 | 数字の出所を元のデータまでたどる | <!-- link:begin make-slides -->資料・スライドを作る（準備中）<!-- link:end --> |
| 満点に近い結果 | リーク・退化・採点の省略を疑う | <!-- link:begin suspect-too-good-results#what-to-suspect -->[良すぎる結果を疑う › まず疑うもの](suspect-too-good-results.md#what-to-suspect)<!-- link:end --> |

自分で見る時間がないときは、書いた本人ではない者に確かめさせる。変更を生んだ推論を見ていない新しいセッションや別の人が向く。AI の承認は、人の承認に数えない。分け方は <!-- link:begin independent-review#who -->[書いた本人ではない者にレビューさせる › 誰にレビューさせるか](independent-review.md#who)<!-- link:end --> にある。

他人のリポジトリや拡張を選ぶときも、見た目に頼れないのは同じである（類推）。整った README や履歴だけで入れず、出所と中身を確かめる。手順は <!-- link:begin vetting-extensions#provenance -->[MCP・プラグイン・スキルを入れる前の確認 › 出所を確かめる](../safety/vetting-extensions.md#provenance)<!-- link:end --> にある。画面のデザインのように見た目そのものが成果物のときは、見た目を手本と見比べて直させる。これは <!-- link:begin frontend-design -->フロントエンドのデザイン（準備中）<!-- link:end --> が扱う。

!!! example "判断例：立派な見た目のリポジトリを受け取る"
    - **状況**：Claude に小さなコマンドラインの道具を作らせた。README があり、テストが 40 件並び、履歴も整っている。報告は「全部通った」である。
    - **迷う候補**：テストが通っているので、そのまま使う。あるいは、先に自分で動かして中身を確かめる。
    - **選んだもの**：先に確かめる。README の手順を新しい環境で実行し、処理を 1 か所壊してテストが落ちるかを見る。
    - **理由**：どちらの候補も筋は通る。ただし、見た目が整っていることは、動くことの根拠にならない。確かめる手間は数分で、外れたときの手戻りより小さい。壊しても落ちないテストなら、その「全部通った」は中身を保証していない。

## 何に効くか {#what-it-helps}

見た目を証拠にしない考え方は、原理「確かめる」に関わる。体裁を根拠に受け取ると、確かめないまま採ることになる。これが、防ぐ原因「確かめていない」である。見た目を証拠から外すと、確かめる手を実行と中身に向けられる。

効く場面は、リポジトリや資料をまるごと作らせる段である。個別の変更なら差分を読めるが、まるごとでは全体の見た目しか目に入らない。そこで見た目に頼る誤りが起きやすい。

効かない場面もある。

- 全部を確かめる時間はない。確かめる箇所は、要の処理と、数字が決まる所に絞る。
- 見た目が整っていないことは、品質が低い証拠でもない。見た目は、読みやすさの手がかりとしては残る。
- 確かめた結果が悪くても、直し方は別の話である。直す手順は、持ち主のページ（<!-- link:begin claims-done-but-isnt#routes-to-fixes -->[「完了」と言うが終わっていない › 原因ごとの対処](../symptoms/claims-done-but-isnt.md#routes-to-fixes)<!-- link:end -->）に任せる。

## 誤解しやすいこと {#misconceptions}

- **「整っているから、雑に作られている」**：そうではない。見た目は、良い悪いのどちらの証拠にもならない。見た目の外で確かめる、というだけである。
- **「Claude が飾って誤魔化している」**：多くの場合は違う。SpecBench では、意図的な悪用はまれで、最も多い失敗は機能を個別にしか満たさないことだった。悪意の有無にかかわらず、確かめる手は変わらない。
- **「テストが通っているから、動く」**：通ることと、壊れたら落ちることは別である。テストも AI が書いたなら、同じ見た目の問題がある。
- **「この主張は実験で確かめられている」**：確かめられてはいない。見た目が信号にならない、という点は実践者の意見（根拠：弱）である。ただし、見えている指標に合わせて整う傾向は、SpecBench など「見た目が証拠でなくなった理由」の節に挙げた報告で裏付けがある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Vibe coding and agentic engineering are getting closer than I’d like](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)：Simon Willison・英語・確認日 2026-11-04
- [SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents](https://arxiv.org/abs/2605.21384)：arXiv（Zhao, Bingchen ほか）・英語・確認日 2026-11-04
- [How AI agents helped me win a Kaggle silver medal — and how they failed me](https://andlukyane.com/blog/rogii-geosteering-kaggle)：Andrey Lukyanenko・英語・確認日 2026-11-04
- [AI Agents in Data Science Competitions: Lessons from the Leaderboard](https://blog.drivendata.org/blog/ai-agents-data-science-competitions)：DrivenData・英語・確認日 2026-11-04
- [Harness design for long-running application development](https://www.anthropic.com/research/harness-design-long-running-apps)：Anthropic・英語・確認日 2026-11-04
- [Claude 3.7 Sonnet System Card](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [報告ではなく証拠を求める](evidence-not-reports.md)

**関連**

- [生成コードを自分のものにする](own-generated-code.md)
- [良すぎる結果を疑う](suspect-too-good-results.md)
- [人間が読むべき差分の箇所](diffs-humans-must-read.md)
- [書いた本人ではない者にレビューさせる](independent-review.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- フロントエンドのデザイン（準備中）
- 資料・スライドを作る（準備中）
- [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)
- [AI に書かせたテストの落とし穴](pitfalls-of-ai-written-tests.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
