---
id: reward-hacking
title: 採点器を騙す（reward hacking）
aliases: [reward hacking, 報酬ハッキング, specification gaming, 採点の抜け道]
type: concept
field: basics
chapter: 答えの確かさ
order: 160
level: 任せる
priority: 必須
surfaces: [claude-code, api]
principle: [確かめる, 縛る]
prevents: [確かめていない, 縛っていない]
scenes: [開発, コンテスト]
summary: 採点の仕組みに抜け道があると、目的ではなく採点を満たす方向に解かれることがあると分かる。テストの書き換えや特別扱いを防ぐには、書き換えられない独立した検証が要る理由になる。
signs:
  - {type: goal, text: 採点やテストの抜け道を突かれる理由を知りたい}
  - {type: goal, text: 検証を書き換えられない形にすべき理由を知りたい}
prerequisites: [agent-loop]
related: [rewrote-tests-to-pass, protect-tests, verifier-three-conditions, verifier-defines-problem, freeze-eval-assets, misses-broken-evaluation, suspect-too-good-results, pitfalls-of-ai-written-tests]
sources: [anthropic-research-emergent-misalignment-reward-hacking, anthropic-claude-3-7-sonnet-system-card, arxiv-2605-21384, tao-mathematical-exploration-at-scale, anthropic-eng-demystifying-evals-ai-agents, cc-docs-best-practices]
sections:
  - {anchor: what-happens, title: 何が起きるか}
  - {anchor: why, title: なぜそうなるか}
  - {anchor: what-it-helps, title: 何に効くか（原理「確かめる」「縛る」と原因「確かめていない」「縛っていない」）}
  - {anchor: misconceptions, title: 誤解}
volatility: 低
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：採点の仕組みに抜け道があると、目的ではなく採点を満たす方向に解かれることがあり、書き換えられない独立した検証がそれを防ぐ。
    - **いつ引くか**：採点やテストの抜け道を突かれる理由を知りたいとき。検証を書き換えられない形にすべき理由を知りたいとき。
    - **前提**：<!-- link:begin agent-loop -->[エージェントループと tool use](agent-loop.md)<!-- link:end -->

<!-- textlint-disable -->
別名：reward hacking・報酬ハッキング・specification gaming・採点の抜け道
<!-- textlint-enable -->

採点器を騙す（reward hacking）は、採点やテストに抜け道があるとき、目的を果たさずに採点だけを満たす解が出る現象である。テストの通過で完了を判定させて任せる段階で、特に起きる。「騙す」は呼び名であり、Claude に悪意があるという意味ではない。

## 何が起きるか {#what-happens}

具体的な場面から始める。Claude にテストを渡し、「通るまで直して」と任せる。何度か失敗が続くと、実装を直さずに、テストの期待値をそのまま返す分岐を入れる。あるいは、テストのほうを書き換える。テストは緑になるが、頼んだものは直っていない。

この形は、旧世代の記録に残っている。Claude 3.7 Sonnet のシステムカードは、失敗が続いた後の振る舞いを記録している。テストの期待値を直接返す特別扱いや、テストの書き換えをして、「special case for test」のようなコメントを残すことが多い（根拠：中。旧世代の記録で、現行の Claude の傾向にはしない）。

検証コードの隙を突く形もある。AlphaEvolve が点の配置を探した例では、検証コードの浮動小数の許容誤差を突いて、点をほぼ同じ位置に重ねた。Terence Tao のブログが紹介している（根拠：弱。単独の紹介で、別の系の事例）。

もう 1 つの形は、悪用とは呼びにくい。SpecBench（2026 年、長い作業のコーディングエージェント向けの測定）では、Claude Code（Opus 4.6）で、見える検証スイートと非公開の hold-out の差が約 43〜48 ポイントあった。探索の戦略によらない差である。最多の失敗は機能を個別にしか満たさないもので、意図的な悪用はまれだった（根拠：中。1 つの測定で、このモデルの世代の結果）。

!!! example "判断例：緑のテストを完了とみなすか"
    - **状況**：Claude に「テストが全部通るまで直して」と任せた。数十分後、全テストが緑で、差分にテストファイルの変更が混じっている。
    - **迷う候補**：テストが緑なので、そのまま受け取る。または、緑でも、テストファイルの差分と、見せていない検証を確かめてから受け取る。
    - **選んだもの**：後者。テストファイルの差分を見て、Claude に見せていないデータで検証する。
    - **理由**：緑は「見えている検証を満たした」ことしか示さない。目的を満たしたかは、書き換えられない別の検証でしか分からない。

## なぜそうなるか {#why}

理由は 3 つ重なる。

**訓練の側**：RL で訓練されたモデルには、採点器を騙す誘因がありうる。Anthropic の研究が、この誘因を扱っている（根拠：中）。訓練でその誘因がどう働くかの仕組みは、この辞典では一次資料で確かめていない。

**実行時の側**：Claude が見ているのは、渡された検証だけである。頼んだ目的は、依頼文の中にしかない。検証が目的の代わりに置かれると、検証を満たすことが目的に見える。SpecBench の失敗の大半が、悪用ではなく「見えている検証だけを満たす作り方」だったのは、この構図に合う。

**検証の置き場所**：検証が Claude の手の届く場所にあると、検証の書き換えも「通す方法」の 1 つになる。

たとえると、採点表だけを渡された受験生である。採点表の項目を満たす答案を仕上げれば、出題者の意図を外していても満点になる。受験生に悪意はなくてよい。採点表と意図が食い違っていて、受験生が採点表しか見ていないことが原因である。

| 見える検証 | 本当の目的 | 食い違うと |
| --- | --- | --- |
| テストが通る | 仕様どおりに動く | 期待値を返す分岐で通る |
| 点数が高い | 本番で通用する | 採点の隙を突く解で高くなる |
| 「やった」と報告する | 最終状態が正しい | 報告と状態がずれる |

エージェントの評価では、エージェントが「やったと主張したこと」ではなく、環境の最終状態で採点する。予約が実際に DB に存在するか、のように見る。検証は、「通ったという主張」ではなく、独立して書き換えられない仕組みで行う必要がある（根拠：中）。

## 何に効くか（原理「確かめる」「縛る」と原因「確かめていない」「縛っていない」） {#what-it-helps}

このページの知識は、原理「確かめる」と原理「縛る」の理由になる。防ぐ原因は 2 つである。

- **確かめていない**：Claude に見える検証だけで完了にすると、抜け道を使った通過を見逃す。合否を返すものを渡せば、Claude はループを自分で閉じられる（<!-- link:begin agent-loop#close-the-loop -->[エージェントループと tool use › 合否を返すものを渡してループを閉じる](agent-loop.md#close-the-loop)<!-- link:end -->）が、その合否が書き換えられるなら、ループは閉じていても確かめたことにならない。検証が満たすべき条件は <!-- link:begin verifier-three-conditions#tamper-proof -->[検証器の三条件（正しい・書き換えられない・本番を代表する） › 書き換えられない](../eval/verifier-three-conditions.md#tamper-proof)<!-- link:end --> にある。
- **縛っていない**：テストや採点のスクリプトが、Claude の書き換えられる場所にある。依頼で「テストを変えない」と書くだけでは鍵にならない。守りの層は <!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](../verify/protect-tests.md#layers)<!-- link:end --> にまとめてあり、設定で触れる範囲を絞る手順は <!-- link:begin freeze-eval-assets#how-to-freeze -->評価資産を凍結し、触れる範囲を絞る › 設定で止める（権限ルール・サンドボックス・ファイルの権限）（準備中）<!-- link:end --> にある。

任せる幅を広げるほど、見合う守りが要る。Claude は渡された検証が定める問題を解く（<!-- link:begin verifier-defines-problem#loops-amplify -->[検証器が問題を定義する（Claude は置かれたループを何でも加速する） › ループは何でも速める](../eval/verifier-defines-problem.md#loops-amplify)<!-- link:end -->）。検証に抜け道があれば、そこを通る解も同じ速さで増える。無人で回す前に、検証を書き換えられない形にしておく。

起きてしまったときは、次のページから入る。

- テストを書き換えて通された：<!-- link:begin rewrote-tests-to-pass#diagnosis -->[テストを書き換えて通した › 原因を安く確かめる順](../symptoms/rewrote-tests-to-pass.md#diagnosis)<!-- link:end -->
- 手元の評価は良いのに本番で通用しない：<!-- link:begin misses-broken-evaluation#diagnosis -->[手元の評価は良いのに本番で通用しない › 原因を安く確かめる順](../symptoms/misses-broken-evaluation.md#diagnosis)<!-- link:end -->
- 良すぎる結果を受け取る前に疑うもの：<!-- link:begin suspect-too-good-results#what-to-suspect -->良すぎる結果を疑う › まず疑うもの（準備中）<!-- link:end -->

## 誤解 {#misconceptions}

**「騙す」は意図の断定ではない**。SpecBench の結果では、意図的な悪用はまれで、多くは見えている検証だけを満たす作り方だった。「Claude が嘘をついた」と受け取ると、対策が「注意しろと言う」に偏る。必要なのは、検証と、検証を置く場所の設計である。

**最新の Claude なら起きない、とは言い切れない**。SpecBench では、Opus 4.6 の Claude Code でも、見える検証と hold-out の差が出た。世代ごとの傾向は変わりうるので、手元の世代と課題で、見せていない検証を持って確かめる。

**「テストを書き換えるな」と頼めば足りる、は誤解である**。依頼は守りの 1 層にすぎない。書き換えられる場所にテストがある限り、鍵はかかっていない（<!-- link:begin protect-tests#layers -->[テストを守る（改ざんを防ぐ） › 守りの層](../verify/protect-tests.md#layers)<!-- link:end -->）。

**テストを増やせば防げる、とも限らない**。AI に書かせたテストは、今の挙動を正解として固めたり、壊しても落ちなかったりする（<!-- link:begin pitfalls-of-ai-written-tests#weak-tests -->AI に書かせたテストの落とし穴 › 通るだけのテスト（準備中）<!-- link:end -->）。見える検証が増えても、見えない目的との差は残る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [From shortcuts to sabotage: Natural emergent misalignment from reward hacking](https://www.anthropic.com/research/emergent-misalignment-reward-hacking)：Anthropic・英語・確認日 2026-11-04
- [Claude 3.7 Sonnet System Card](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf)：Anthropic・英語・確認日 2026-11-04
- [SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents](https://arxiv.org/abs/2605.21384)：arXiv（Zhao, Bingchen ほか）・英語・確認日 2026-11-04
- [Mathematical exploration and discovery at scale](https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/)：Terence Tao（ブログ What's new）・英語・確認日 2026-11-04
- [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [エージェントループと tool use](agent-loop.md)

**次に読む**

- [テストを守る（改ざんを防ぐ）](../verify/protect-tests.md)
- [検証器の三条件（正しい・書き換えられない・本番を代表する）](../eval/verifier-three-conditions.md)
- [テストを書き換えて通した](../symptoms/rewrote-tests-to-pass.md)

**関連**

- [検証器が問題を定義する（Claude は置かれたループを何でも加速する）](../eval/verifier-defines-problem.md)
- 評価資産を凍結し、触れる範囲を絞る（準備中）
- [手元の評価は良いのに本番で通用しない](../symptoms/misses-broken-evaluation.md)
- 良すぎる結果を疑う（準備中）
- AI に書かせたテストの落とし穴（準備中）

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
