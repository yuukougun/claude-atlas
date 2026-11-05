---
id: parallel-fatigue
title: 並列にしたら疲れた・レビューが追いつかない
nav_title: 並列にしたら疲れた
aliases: [並列疲れ, レビュー待ちがたまる, 並列にしても速くならない]
type: symptom
field: symptoms
chapter: 長い作業と方針
order: 270
level: 回す
priority: 必須
surfaces: [claude-code]
principle: [握る, 確かめる]
prevents: [確かめていない, 合っていない]
pitfalls: [預けすぎる, 体感を信じる]
scenes: [開発, チーム]
summary: 並列で任せたら疲れた・レビューが追いつかないときに、並べる数・確かめ方・体感のずれのどれが原因かを切り分け、並列の上限と人が読む範囲を決め直す。
signs:
  - {type: symptom, text: 並列にしたら疲れた}
  - {type: symptom, text: レビュー待ちの変更がたまっていく}
  - {type: symptom, text: 並べた分だけ速くなった気がしない}
wave: 1
prerequisites: []
related: [independent-review, over-reliance, parallel-with-worktrees, completion-notifications, parallel-and-loop-costs, wrong-amount-of-approvals, hits-limits-quickly, six-causes]
routes:
  - {cause: 確かめていない, to: [diffs-humans-must-read, review-bottlenecks, risk-tiered-approval]}
  - {cause: 合っていない, to: [choosing-parallel-modes, agent-view-and-background#what-fits]}
  - {cause: 預けすぎる, to: [humans-set-the-parallel-limit]}
  - {cause: 体感を信じる, to: [felt-vs-measured]}
tracks: [worktrees, agent-view]
outdated_advice: [tmux-agent-orgs]
sources: []
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: example}
  - {title: 予防は仕組みに移す, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：並列で疲れたとき、確かめ方・向き不向き・預け方・体感のどれが原因かを切り分け、並列の上限と人が読む範囲を決め直す先が分かる。
    - **いつ引くか**：複数のセッションを並べて疲れたとき。レビュー待ちがたまるとき。並べても速くなった実感がないとき。
    - **前提**：なし

<!-- textlint-disable -->
別名：並列疲れ・レビュー待ちがたまる・並列にしても速くならない
<!-- textlint-enable -->

並列にしたら疲れた・レビューが追いつかないとは、Claude Code のセッションを複数並べたあと、人がレビューと動作確認に追われて詰まる症状である。疲れの正体は、並べた本数そのものより、人が確かめる量の増加にあることが多い。このページは、原因を安く確かめる順に並べて、対処を持つページへ振り分ける。

## よくある形 {#forms}

読者の言葉で書くと、この症状は次の 3 つの形で現れる。どれも、セッションを増やした直後から始まる。

- **疲れた**：画面を行き来して状況を追い、どれがどこまで進んだかを頭に置いておくだけで消耗する。
- **レビュー待ちがたまる**：出てくる変更の速さに、読んで動かして確かめる人の速さが追いつかない。待ちの数が日ごとに増える。
- **速くなった気がしない**：並べたのに、完成して手元に残る量が増えた実感を持てない。手戻りや捨てた作業が増えている。

詰まる場所がレビューと動作確認に偏る理由は、<!-- link:begin review-bottlenecks#where-it-clogs -->[レビューのボトルネックと疲労 › 詰まる場所はレビューと動作確認](../team/review-bottlenecks.md#where-it-clogs)<!-- link:end -->が持つ。変更が増えるほど、疲れもそこに溜まる。

承認の確認そのものが多すぎる・少なすぎるときは、並列とは別の症状として<!-- link:begin wrong-amount-of-approvals#diagnosis -->[承認の確認が多すぎる・少なすぎる › 原因を安く確かめる順](wrong-amount-of-approvals.md#diagnosis)<!-- link:end -->を引く。利用上限に当たるのが困りごとの中心なら、<!-- link:begin hits-limits-quickly#diagnosis -->[すぐ上限に当たる › 原因を安く確かめる順](hits-limits-quickly.md#diagnosis)<!-- link:end -->を引く。

## 原因を安く確かめる順 {#diagnosis}

原因は、手間のかからない確かめ方から順に潰す。確かめている間は、新しいセッションを足さない。1 から 4 を上から確かめ、当たった項目の振り分け先へ進む。複数に当たることも多い。6 つの原因全体の順は<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end -->にある。

1. **確かめていない**（Claude 側の原因）
    - 何を見るか：最近マージした変更のうち、差分の要点とテスト結果を見ずに通したものはないか。
    - どう確かめるか：直近のマージから数件を選び、人が読んだ箇所を言えるかを試す。言えないなら、読む場所が決まっていない。
    - 当たったとき：人が必ず読む箇所を絞る。見分け方は<!-- link:begin diffs-humans-must-read#red-flags -->[人間が読むべき差分の箇所 › 赤信号の一覧](../verify/diffs-humans-must-read.md#red-flags)<!-- link:end -->にある。AI が出した承認は、人の承認に数えない。
2. **合っていない**（Claude 側の原因）
    - 何を見るか：並べた作業が、並列に向く形か。同じファイルを触る作業、互いの結果を待つ作業、同じ文脈を共有してほしい作業が混ざっていないか。
    - どう確かめるか：衝突、やり直し、捨てた作業が出た作業を挙げ、共通点を探す。共通点が「同じ場所を触る」「順番に依存する」なら、並べ方が作業に合っていない。
    - 当たったとき：方式を選び直す。誰が調整するか・同じファイルを触るかで決める基準は<!-- link:begin choosing-parallel-modes#who-coordinates -->[並列の方式の選び方 › 誰が調整するか](../delegate/choosing-parallel-modes.md#who-coordinates)<!-- link:end -->にある。
3. **預けすぎる**（人の側の落とし穴）
    - 何を見るか：人のレビューを要する本流は、同時に何本走っているか。
    - どう確かめるか：走っている作業を、マージするつもりの本流と、調査や使い捨ての試作のような偵察に分けて数える。本流が人の手に余る数なら、疲れの兆しとして<!-- link:begin humans-set-the-parallel-limit#signs-of-fatigue -->[並列の上限は人間が決める › 疲れの兆し](../delegate/humans-set-the-parallel-limit.md#signs-of-fatigue)<!-- link:end -->に当たるかを見る。
    - 当たったとき：本数を決めるのは機械や予算ではなく、レビューする人の帯域である。判断まで預けていないかは<!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](../judgment/over-reliance.md#what-to-keep)<!-- link:end -->で見直す。
4. **体感を信じる**（人の側の落とし穴）
    - 何を見るか：「疲れた」「速くならない」の判断が、感覚だけに基づいていないか。逆に「速くなった」と感じていても、実測では変わらないことがある。
    - どう確かめるか：並列にする前後で、同じ物差しの記録を取って比べる。たとえば、1 件が着手から人が受け入れるまでの時間と、やり直しの回数を並べる。
    - 当たったとき：体感がずれる理由と記録の取り方は<!-- link:begin felt-vs-measured#what-to-record -->[体感と実測 › 記録で測るもの](../eval/felt-vs-measured.md#what-to-record)<!-- link:end -->にある。

診断の結果と振り分け先は、次の表にまとまる。対処の本体は、行き先のページが持つ。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 確かめていない | [人間が読むべき差分の箇所](../verify/diffs-humans-must-read.md)<br>[レビューのボトルネックと疲労](../team/review-bottlenecks.md)<br>[リスク段階別の承認（AI の承認を人の承認に数えない）](../team/risk-tiered-approval.md) |
| 合っていない | [並列の方式の選び方](../delegate/choosing-parallel-modes.md)<br>[agent view と背景セッション › 向く作業と向かない作業](../delegate/agent-view-and-background.md#what-fits) |
| 預けすぎる | [並列の上限は人間が決める](../delegate/humans-set-the-parallel-limit.md) |
| 体感を信じる | [体感と実測](../eval/felt-vs-measured.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#example}

!!! example "判断例：レビュー待ちがたまったとき、本数を減らすか、レビューを増やすか"
    - **状況**：worktree を分けて複数のセッションを並べたところ、レビュー待ちが日ごとに増え、マージが止まった。
    - **迷う候補**：並べる本数を減らす。または、別のセッションにレビューさせて、人が読む量を減らしながら本数を保つ。
    - **選んだもの**：先に待っている変更を、本流と偵察に分けて数える。偵察は捨てる前提に戻して待ちから外し、本流だけを人が読める本数まで絞る。残った本流に、独立したレビューを足す。
    - **理由**：どちらの案も筋は通るが、待ちの中身を数えるまで効く案が決まらない。待ちの多くが偵察なら、減らすべきは読む量ではなく待たせる作業である。独立したレビューは見落としを減らすが、人の確認の代わりにはならない。人が読む場所は、危ない場所に限って残す。

## 予防は仕組みに移す {#prevention}

並べ方の約束は、疲れてから守るのでなく、始める前に決める。

- **本数と範囲を先に決める**：本流の本数、偵察の本数、人が必ず読む場所を、並列を始める前に決める。決め方は<!-- link:begin humans-set-the-parallel-limit#mainline-vs-scouting -->[並列の上限は人間が決める › 本流と偵察で本数を分ける](../delegate/humans-set-the-parallel-limit.md#mainline-vs-scouting)<!-- link:end -->にある。費用も同じ時点で決める。始める前に決める項目は<!-- link:begin parallel-and-loop-costs#decide-before-starting -->[並列・ループ・workflows のコスト › 始める前に決める三つ](../cost/parallel-and-loop-costs.md#decide-before-starting)<!-- link:end -->にある。
- **作業ごとに環境を分ける**：セッションが互いのファイルを上書きしないよう、作業ごとに別のチェックアウトを作る。準備と片付けは<!-- link:begin parallel-with-worktrees#per-worktree-setup -->[git worktree で並列にする › worktree ごとの準備（依存・秘密・データベース）](../delegate/parallel-with-worktrees.md#per-worktree-setup)<!-- link:end -->で決める。
- **承認の段を決める**：変更の段ごとに、人の承認の数を決める。段の分け方は<!-- link:begin risk-tiered-approval#three-tiers -->[リスク段階別の承認（AI の承認を人の承認に数えない） › 三つの段と承認の数](../team/risk-tiered-approval.md#three-tiers)<!-- link:end -->にある。
- **画面に張りつかない**：終わりや承認待ちを通知させ、確認する時刻を自分で決める。選び方は<!-- link:begin completion-notifications#when-to-notify -->終わったら知らせてもらう<!-- link:end -->にある。
- **並列の前後を記録する**：1 件あたりの完了までの時間とやり直しの回数を取り続け、本数を変えるたびに比べる。

tmux で自作の組織を作って並べる古いやり方も、レビューの量は減らさない。今の置き換え先は<!-- link:begin outdated-advice-ledger#tmux-agent-orgs -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#tmux-agent-orgs)<!-- link:end -->にある。背景のセッションをまとめて見る手段は<!-- link:begin agent-view-and-background#what-fits -->[agent view と背景セッション › 向く作業と向かない作業](../delegate/agent-view-and-background.md#what-fits)<!-- link:end -->で、状況を確認する手間は減らせる。ただし、人が読む量は増減しない。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [人間が読むべき差分の箇所](../verify/diffs-humans-must-read.md)
- [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- [リスク段階別の承認（AI の承認を人の承認に数えない）](../team/risk-tiered-approval.md)
- [並列の方式の選び方](../delegate/choosing-parallel-modes.md)
- [agent view と背景セッション](../delegate/agent-view-and-background.md)
- [並列の上限は人間が決める](../delegate/humans-set-the-parallel-limit.md)
- [体感と実測](../eval/felt-vs-measured.md)

**関連**

- [書いた本人ではない者にレビューさせる](../verify/independent-review.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- [git worktree で並列にする](../delegate/parallel-with-worktrees.md)
- [並列・ループ・workflows のコスト](../cost/parallel-and-loop-costs.md)
- [承認の確認が多すぎる・少なすぎる](wrong-amount-of-approvals.md)
- [すぐ上限に当たる](hits-limits-quickly.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
