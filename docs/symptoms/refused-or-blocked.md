---
id: refused-or-blocked
title: 断られた・止められた
aliases: [利用ポリシーで止められた, 拒否された, 分類器に止められた, refusal]
type: symptom
field: symptoms
chapter: 返答と品質
order: 40
level: 使う
priority: 必須
surfaces: [app, claude-code, api]
principle: [見せる]
prevents: [見えていない, 散らかっている, 合っていない]
pitfalls: []
scenes: [開発, 調べもの]
summary: 正当な依頼が断られた・止められたときに、利用ポリシーの判定か、auto モード・フック・権限ルールの停止かを先に見分け、引き金と依頼の文脈のどちらが効いたかを切り分けて進め直す。
signs:
  - {type: symptom, text: 正当な依頼なのに断られる}
  - {type: symptom, text: 「新しい会話を始めて」と言われて続けられない}
  - {type: symptom, text: 途中で別のモデルの返事に切り替わった}
  - {type: symptom, text: 操作を止められたが、何に止められたのか分からない}
wave: 1
prerequisites: []
related: [checkpoints-and-rewind, what-feedback-sends, isolate-with-safe-mode, current-models, block-with-exit-2, keeps-stopping, followed-injected-instructions, wrong-amount-of-approvals, six-causes]
routes:
  - {cause: 見えていない, to: [when-requests-are-refused#official-steps, give-reasons]}
  - {cause: 散らかっている, to: [rewind-dont-correct, when-to-start-fresh, asking-for-reasoning#refusal]}
  - {cause: 合っていない, to: [what-auto-mode-stops#when-blocked, lock-side-effects, permission-rules]}
tracks: [checkpoints, refusals, auto-mode]
outdated_advice: []
sources: [hc-switched-models, hc-output-blocked, api-docs-refusals, cc-docs-errors, cc-docs-permission-modes]
volatility: 高
sections:
  - {title: よくある形, anchor: forms}
  - {title: 何に止められたかを見分ける（利用ポリシーか、auto モード・フック・権限ルールか）, anchor: what-stopped}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 面ごとの表示（本体は when-requests-are-refused の節 by-surface）, anchor: by-surface}
  - {title: 判断例, anchor: examples}
  - {title: 予防, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：断られた・止められた原因を、利用ポリシーの判定と、auto モード・フック・権限ルールの停止に分け、進め直す手を選べる。
    - **いつ引くか**：正当な依頼が断られた。「新しい会話を始めて」と言われて続けられない。途中で別のモデルの返事になった。操作を止められたが、何に止められたか分からない。
    - **前提**：なし

<!-- textlint-disable -->
別名：利用ポリシーで止められた・拒否された・分類器に止められた・refusal
<!-- textlint-enable -->

Claude が依頼を断る、または操作が止められると、読者は「何が」止めたのかが分からないまま同じ依頼を繰り返しやすい。このページは、止めたものを先に見分け、安く確かめられる順に原因を切り分ける。対処の手順の本体は、振り分け先のページが持つ。

## よくある形 {#forms}

読者の言葉で書くと、次のような形で現れる。

- 開発や調べものの正当な依頼なのに、「手伝えない」と断られる。
- 「新しい会話を始めて」と案内され、同じ会話で送り直しても続けられない。
- 返答の途中から、別のモデルが答えたような文面に変わる。
- ツールの操作が止められたが、利用ポリシーなのか自分の設定なのか分からない。

最後の形は、断られたのではなく操作が止められた場合を含む。Claude が自分から確認を求めて進まない症状は、<!-- link:begin keeps-stopping -->[確認ばかりで進まない・途中で止まる](keeps-stopping.md)<!-- link:end --> が受け持つ。

## 何に止められたかを見分ける（利用ポリシーか、auto モード・フック・権限ルールか） {#what-stopped}

止めたものは大きく 2 つに分かれ、進め直す手が違う。最初にどちらかを決める。

- **利用ポリシーの判定**：Claude の返答が断りの文面になる、会話が止まる、別のモデルの返事に切り替わる。API では、拒否はエラーではなく、`stop_reason` が `refusal` の通常の応答として返る。判定は打った文だけでなく、Claude が読んだ内容にもかかる。
- **操作の停止**：ツールの呼び出し（コマンドの実行・ファイルの編集など）が拒否される。止めたのは auto モードの分類器、フック、権限ルールのどれかで、会話の内容ではなく操作そのものが見られている。

見分ける手がかりは 3 つある。

1. 止まったのが返答の文面か、ツールの操作か。返答の文面なら利用ポリシーの側、操作なら停止の側を先に疑う。
2. 操作の停止なら、止めた記録を見る。auto モードが止めた操作は、<!-- name:begin recently-denied-to-blocked -->Recently blocked（/permissions のタブ）<!-- name:end --> で見直せる。自分で書いたフックが止めたなら、返された理由の文面が自分の書いたものと一致する。
3. 自分の設定が絡むか迷うなら、<!-- link:begin isolate-with-safe-mode -->[設定を外して切り分ける（--safe-mode）](../cli/isolate-with-safe-mode.md)<!-- link:end --> で設定を読まずに起動し、同じ依頼を送って比べる。権限と管理の設定は効いたままなので、権限ルールの停止はこの方法では消えない。

利用ポリシーの判定なら、次の節の 1 と 2 から確かめる。操作の停止なら、3 から確かめる。どちらか決められないときは、1 から順に確かめる。

## 原因を安く確かめる順 {#diagnosis}

Claude 側の原因を、確かめる手間が小さい順に並べる。全体の見取り図は <!-- link:begin six-causes#claude-side -->[失敗の二つの軸と診断の入口 › Claude 側の六つの原因](../start/six-causes.md#claude-side)<!-- link:end --> にある。

1. **見えていない**（利用ポリシーの判定。依頼の目的や文脈が伝わっていない）
    - 何を見るか：依頼の文だけを切り出して読み、目的や立場を知らない人にどう見えるか。
    - どう確かめるか：本当の目的と文脈を足して、引き金より前から言い直す。文脈は事実だけを書く。偽の文脈は足さない。足した後も同じ会話で止まり続けるなら、次の原因に進む。手段は <!-- link:begin when-requests-are-refused#official-steps -->[正当な依頼が断られたとき › 公式が案内する手段](../safety/when-requests-are-refused.md#official-steps)<!-- link:end --> と <!-- link:begin give-reasons -->[理由を添える](../prompting/give-reasons.md)<!-- link:end --> にある。
2. **散らかっている**（利用ポリシーの判定。引き金が会話の中に残っている）
    - 何を見るか：判定は会話全体にかかる。引き金は、前のやり取り、読み込んだファイルや Web ページ、メモリ、推論の全文を求める指示のどれにもありうる。Claude Code で「新しい会話を始めて」と案内されたときは、同じ会話で送り直しても、`--continue` や `--resume` で開き直しても、また止まる。
    - どう確かめるか：引き金の前に巻き戻して送り直す（<!-- link:begin checkpoints-and-rewind -->[チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)<!-- link:end -->）。どこが引き金か分からなければ新しい会話にする（<!-- link:begin when-to-start-fresh -->[新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<!-- link:end -->）。推論の全文を求める指示が CLAUDE.md やスキルなどに入っていないかも見る。
3. **合っていない**（操作の停止。縛りや権限の設定が作業に合っていない）
    - 何を見るか：止められたのが操作か。止めたのは auto モードの分類器か、フックか、権限ルールか。
    - どう確かめるか：止めた記録と理由を見て、その規則が本当に止めたかったものか判断する。見直しの手順は <!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<!-- link:end --> にある。
4. **上の 3 つのどれでもない**：返答の質や、確認を求めて止まる症状なら、このページの外にある。<!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> から別の症状のページへ進む。

人の側の落とし穴として 1 つだけ挙げる。断られた依頼を、言い換えたり小分けにしたりして通そうとしてはいけない。判定の仕組みと、そうしない理由は <!-- link:begin when-requests-are-refused#why-not-evade -->[正当な依頼が断られたとき › 分類器を避ける頼み方をしない理由（利用ポリシー）](../safety/when-requests-are-refused.md#why-not-evade)<!-- link:end --> にある。このページが勧める手段は、公式が案内するものに限る。目的と文脈を足す。巻き戻す。新しい会話にする。誤判定を報告する。この 4 つである。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [正当な依頼が断られたとき › 公式が案内する手段](../safety/when-requests-are-refused.md#official-steps)<br>[理由を添える](../prompting/give-reasons.md) |
| 散らかっている | [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)<br>[新しい会話を始めるタイミング](../context/when-to-start-fresh.md)<br>[推論を見せてほしいとき › 全文を求める指示が断られる理由](../prompting/asking-for-reasoning.md#refusal) |
| 合っていない | [auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<br>[縛りすぎの害と見直し（止めすぎ・回り込み）](../enforce/lock-side-effects.md)<br>[権限ルール（allow・ask・deny）](../enforce/permission-rules.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 面ごとの表示（本体は when-requests-are-refused の節 by-surface） {#by-surface}

断られたときの表示の文は面ごとに違い、変わりやすい。本体は <!-- link:begin when-requests-are-refused#by-surface -->[正当な依頼が断られたとき › 面ごとの表示と仕組み（分類器が見るもの・自動のモデルの切り替え）](../safety/when-requests-are-refused.md#by-surface)<!-- link:end --> が 1 か所で持つので、ここには書かない。

途中で別のモデルの返事になったときは、自動のモデルの切り替えが起きた手がかりとして読む。切り替えた先のモデルの位置づけは <!-- link:begin current-models -->[現行モデルの一覧と位置づけ](../models/current-models.md)<!-- link:end --> で読める。「モデルを変えれば通る」という手段としては扱わない。

## 判断例 {#examples}

!!! example "判断例：長い会話の途中で、正当な調査の依頼が断られた"
    - **状況**：自社サービスの脆弱性対応の調査をしていて、読み込ませたログの内容を含む依頼が断られた。同じ会話で送り直しても断られる。
    - **迷う候補**：目的と立場を同じ会話で書き足して送り直す。引き金より前に巻き戻して、目的と立場を最初に書いて言い直す。
    - **選んだもの**：巻き戻して、目的と立場を最初に書いて言い直す。
    - **理由**：判定は会話全体にかかるので、引き金が残ったまま文脈を足しても止まり続けることがある。巻き戻せば、引き金と文脈の足し方を同時に直せる。

!!! example "判断例：コマンドが止められたが、理由が出ていない"
    - **状況**：Claude Code でコマンドが止められた。断りの文面はなく、何が止めたか分からない。
    - **迷う候補**：依頼を言い換えて、別のコマンドで同じことをさせる。止めた記録と、自分のフックと権限ルールを見る。
    - **選んだもの**：止めた記録と、自分のフックと権限ルールを見る。
    - **理由**：操作の停止は会話の内容ではなく規則で決まる。規則が作業に合っていないなら、直すのは規則であり、回り込む手段を探すことではない。

## 予防 {#prevention}

断られる・止められる頻度は、仕組みに移すと下げられる。

- 依頼の最初に目的と立場を書く習慣にする。依頼に理由を添える書き方は <!-- link:begin give-reasons -->[理由を添える](../prompting/give-reasons.md)<!-- link:end --> にある。
- 話題が変わったら新しい会話にして、関係のない読み込みを持ち越さない。
- 自分で書くフックは、止めるときに理由と代わりの手段を返す。書き方は <!-- link:begin block-with-exit-2 -->[フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)<!-- link:end --> にある。自分の規則が何を止めたかが、次から分かる。
- 止めた記録を見直す。止めすぎの見直しは <!-- link:begin lock-side-effects#review-blocks -->[縛りすぎの害と見直し（止めすぎ・回り込み） › 止めた記録の見直し](../enforce/lock-side-effects.md#review-blocks)<!-- link:end --> にある。
- 誤判定だと思ったら報告する。報告で送られるものは <!-- link:begin what-feedback-sends -->[/feedback・トランスクリプトの共有で送られるもの](../safety/what-feedback-sends.md)<!-- link:end --> で先に確かめる。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Why Claude switched models in your conversation with Opus 5 or Opus 5.5](https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5-or-opus-5-5)：Anthropic・英語・確認日 2026-11-04
- [Why am I receiving an 'Output blocked by content filtering policy' error?](https://support.claude.com/en/articles/9205721-why-am-i-receiving-an-output-blocked-by-content-filtering-policy-error)：Anthropic・英語・確認日 2026-11-04
- [Refusals and fallback](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)：Anthropic・英語・確認日 2026-11-04
- [Error reference](https://code.claude.com/docs/en/errors)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- なし

**次に読む**

- [正当な依頼が断られたとき](../safety/when-requests-are-refused.md)
- [理由を添える](../prompting/give-reasons.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [推論を見せてほしいとき](../prompting/asking-for-reasoning.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [縛りすぎの害と見直し（止めすぎ・回り込み）](../enforce/lock-side-effects.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)

**関連**

- [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- [/feedback・トランスクリプトの共有で送られるもの](../safety/what-feedback-sends.md)
- [設定を外して切り分ける（--safe-mode）](../cli/isolate-with-safe-mode.md)
- [現行モデルの一覧と位置づけ](../models/current-models.md)
- [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- [確認ばかりで進まない・途中で止まる](keeps-stopping.md)
- [読ませたページやファイルの指示に従ってしまった](followed-injected-instructions.md)
- [承認の確認が多すぎる・少なすぎる](wrong-amount-of-approvals.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
