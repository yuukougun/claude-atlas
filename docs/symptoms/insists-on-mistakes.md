---
id: insists-on-mistakes
title: 誤りを認めずに言い張る
aliases: [間違いを認めない, 存在しないものをあると言い張る, 言い訳が続く]
type: symptom
field: symptoms
chapter: 返答と品質
order: 60
level: 整える
priority: 必須
surfaces: [claude-code, app]
principle: [確かめる]
prevents: [見えていない, 散らかっている, 確かめていない]
pitfalls: []
scenes: [開発]
summary: 誤りを指摘しても認めずに言い張るときに、言い争う代わりに実物（履歴・検索・実行結果）を見せて確かめ、会話を巻き戻すかを決める。
signs:
  - {type: symptom, text: 間違いを指摘しても認めずに言い張る}
  - {type: symptom, text: 存在しないバグや変更をあったことにして譲らない}
  - {type: symptom, text: 説明と実際の履歴が食い違っている}
wave: 1
prerequisites: [context-rot]
related: [why-hallucinations, unfaithful-reasoning, caves-when-pushed, going-in-circles, blames-the-tools, plausible-falsehoods, six-causes]
routes:
  - {cause: 見えていない, to: [choose-what-to-read, working-with-git]}
  - {cause: 散らかっている, to: [rewind-dont-correct, when-to-start-fresh]}
  - {cause: 確かめていない, to: [evidence-not-reports#facts-win]}
tracks: []
outdated_advice: []
sources: [lukyanenko-kaggle-antigravity-s6e7, cc-issue-46940]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 実物を見せる頼み方, anchor: show-evidence}
  - {title: 原因ごとの振り分け先, anchor: routes}
  - {title: 判断例, anchor: examples}
  - {title: 予防, anchor: prevent}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：誤りを指摘しても言い張るとき、言い返さずに実物を見せて原因を切り分け、巻き戻すかを決められる。
    - **いつ引くか**：間違いを指摘しても認めない、存在しないバグや変更をあったことにして譲らない、説明と実際の履歴が食い違うとき。
    - **前提**：<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end -->

<!-- textlint-disable -->
別名：間違いを認めない・存在しないものをあると言い張る・言い訳が続く
<!-- textlint-enable -->

誤りを認めずに言い張る症状は、指摘を受けても前の主張を変えない、または指摘のたびに別の理屈を足して結論を守る状態である。言い争っても、会話に主張が増えるだけで解決しない。決め手は、履歴・検索・実行結果といった実物を見せて、どちらの言い分が合うかを確かめることである。

## よくある形 {#forms}

読者が出会う形は 3 つある。

- **存在しないものをあると言い張る**：ない関数、ないバグ、していない変更を前提に説明を続け、指摘されても擁護する。
- **説明と履歴の食い違い**：「直した」と言うのに差分にない。「元からあった不具合だ」と言うのに履歴にない。
- **言い訳が続く**：指摘のたびに別の理由を挙げて、結論そのものは変えない。

実践者の報告に、この形の事例がある。他社のコーディング用エージェントが、学習の結果がおかしい理由として、テンプレートに「元からあった」誤記があると説明した。説明は症状に合っていて、もっともらしかった。書き手が実際の行を見せ、エージェントが履歴を検索して、その誤記が一度もなかったと確かめた後で、ようやく説明が引っ込んだ（根拠：弱、単独の経験談・他社のモデル・版依存）。この辞典は、これを特定のモデルの傾向としては扱わない。ここから取るのは、反論を重ねず、実物を見せて決着させるという実践である。

似た症状とは、次のように見分ける。

- 押すとすぐ同意して答えを変えるなら、逆向きの症状である。<!-- link:begin caves-when-pushed -->[すぐ同意して意見を変える（迎合）](caves-when-pushed.md)<!-- link:end -->で扱う。
- 同じ失敗を何度も繰り返すなら、<!-- link:begin going-in-circles -->[同じ失敗を繰り返す（堂々巡り）](going-in-circles.md)<!-- link:end -->で扱う。
- 存在しない出典や引用を挙げるなら、<!-- link:begin plausible-falsehoods -->[もっともらしい嘘・出典の誤り](plausible-falsehoods.md)<!-- link:end -->で扱う。
- 「環境や道具が壊れた」と言い出すなら、<!-- link:begin blames-the-tools -->[環境や道具が壊れたと言い出す](blames-the-tools.md)<!-- link:end -->で扱う。

## 原因を安く確かめる順 {#diagnosis}

最初に、自分の指摘が実物と合うかを確かめる。言い張る側が正しいこともあるので、`git log`・`grep`・テストの実行で、指摘の根拠を自分の目で見る。これは数十秒で済み、以降のどの原因の確認にも使う実物になる。

「なぜそう言ったのか」を Claude に問い詰める手は、勧めない。画面に出る説明は、内部の処理と一致するとは限らない。仕組みは<!-- link:begin unfaithful-reasoning -->[表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)<!-- link:end -->を見る。説明のもっともらしさではなく、実物で決める。

原因は、安く確かめられる順に 3 つ見る。

1. **見えていない**
    - 何を見るか：返答が、実際のファイル・行・コマンドの出力を根拠にしているか。記憶や推測で話していないか。
    - どう確かめるか：「その主張の根拠の行を引用して」と頼む。引用できない、または引用が実物と違うなら、見えていない。読ませるファイルは @ で直接指す。
    - 振り分け先：<!-- link:begin choose-what-to-read#point-or-search -->[@参照と、何を読ませるかの絞り込み › 直接指すか、探させるか](../context/choose-what-to-read.md#point-or-search)<!-- link:end -->、<!-- link:begin working-with-git#granularity -->[git との付き合い方 › どこで区切るか](../cli/working-with-git.md#granularity)<!-- link:end -->。
2. **散らかっている**
    - 何を見るか：誤った主張が会話に残り、後の返答がそれを前提に進んでいないか。指摘への返答が、前の返答の言い換えになっていないか。
    - どう確かめるか：新しい会話に同じ実物を渡して、同じ質問をする。新しい会話で正しく答えるなら、原因は会話に残った跡である。誤った主張が次の答えを引きずる理由は<!-- link:begin context-rot -->[context rot と紛らわしい情報](../basics/context-rot.md)<!-- link:end -->で扱う。
    - 振り分け先：<!-- link:begin rewind-dont-correct#why -->[違うと返すより、巻き戻す・編集する › なぜ訂正より巻き戻しか](../context/rewind-dont-correct.md#why)<!-- link:end -->、<!-- link:begin when-to-start-fresh#signals -->[新しい会話を始めるタイミング › 新しくする合図](../context/when-to-start-fresh.md#signals)<!-- link:end -->。
3. **確かめていない**
    - 何を見るか：説明に対応する、実行したコマンドとその生の出力があるか。「確認した」「全部通った」とだけ書かれていないか。
    - どう確かめるか：自分で `grep`・`git log`・テストを実行して、説明と照らす。食い違えば、実行・検索・git で見た事実を正とする。
    - 事例：利用者の報告に、失敗が残っているのに、分母を変えて「全部通過」と返した例がある（根拠：弱、単独の報告・版依存）。
    - 振り分け先：<!-- link:begin evidence-not-reports#facts-win -->[報告ではなく証拠を求める › 説明と事実が食い違ったら](../verify/evidence-not-reports.md#facts-win)<!-- link:end -->。

人の側の落とし穴も疑う。どこが違うかを示さずに「違う」とだけ返すと、Claude には見直す手がかりがない（推論・実践例なし）。押し返しを重ねて会話が長くなると、誤った主張が会話に残るので「散らかっている」が重なる。人の側の落とし穴の全体は<!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end -->を見る。

## 実物を見せる頼み方 {#show-evidence}

言い張りに出会ったら、次の形で実物を見せる。どの原因でも最初の手当てになる。実行結果は、先に自分で出して貼る。主張の言い換えではなく、出力の行の引用を答えさせる点が肝である。

<!-- gen:begin snippet insists-on-mistakes/show-evidence -->
<!-- textlint-disable -->

??? example "雛形：実物の出力を見せて、どちらが正しいかを答えさせる頼み方"

    ```markdown
    あなたが「<変更や不具合についての主張>」と説明した点は、実物と合わない。次の実行結果を見てほしい。

    - 実行したコマンド：`git log -S'<主張の中の文字列>' --oneline -- <ファイルのパス>`
    - 出力：<生の出力をそのまま貼る。出力が空なら「空」と書く>

    この出力とあなたの説明のどちらが正しいかを、出力の該当の行を引用して答えてほしい。説明が間違っていたなら、その説明を前提にした直しや結論を一覧にして、まだ使えるものと取り消すものに分けてほしい。
    ```

    動作を確かめていない雛形。

<!-- textlint-enable -->
<!-- gen:end snippet insists-on-mistakes/show-evidence -->

実物を見せても主張が変わらないとき、または認めた後も前の主張を前提にした答えが続くときは、訂正を重ねない。誤った主張が会話に残っている疑い（「散らかっている」）が強いので、巻き戻す。

## 原因ごとの振り分け先 {#routes}

対処の本体は、各分野のページが持つ。原因ごとに、次のページへ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 見えていない | [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)<br>[git との付き合い方](../cli/working-with-git.md) |
| 散らかっている | [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)<br>[新しい会話を始めるタイミング](../context/when-to-start-fresh.md) |
| 確かめていない | [報告ではなく証拠を求める › 説明と事実が食い違ったら](../verify/evidence-not-reports.md#facts-win) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：存在しない変更を原因だと言い張る"
    - **状況**：Claude Code に失敗したテストの原因を聞くと、「直前のコミットで設定の読み込みを変えたのが原因だ」と答えた。`git log -p` で見ると、そのコミットに設定の読み込みの変更はない。指摘しても「その変更の影響だ」と繰り返す。
    - **迷う候補**：`git log -p` の出力を貼って、その場で答えさせる。または、すぐ巻き戻して、出力を貼った新しい頼みから始める。
    - **選んだもの**：出力を貼って、出力の該当の行を引用して答えさせる。それでも主張が変わらなければ、その主張が出る前のメッセージまで巻き戻す。
    - **理由**：貼った出力は議論の余地がなく、認めれば会話を続けられて安い。変わらないなら誤った主張が会話に残って引きずるので、巻き戻して消す。問い詰めて理由を聞き出しても、その説明は内部の処理と一致するとは限らず、会話に主張が増えるだけである。

## 予防 {#prevent}

言い張りは、実物を見せる手間を前もって払っておくと起きにくい。仕組みに移せるものから並べる。

- 読ませたいファイルは @ で直接指す。出力が長いなら、要点の数行に絞って渡す。<!-- link:begin choose-what-to-read#trim-output -->[@参照と、何を読ませるかの絞り込み › 出力を絞る](../context/choose-what-to-read.md#trim-output)<!-- link:end -->を見る。
- 変更を小さく区切ってコミットし、履歴を食い違いの基準にする。<!-- link:begin working-with-git#one-change-one-eval -->[git との付き合い方 › 1変更1評価1コミット](../cli/working-with-git.md#one-change-one-eval)<!-- link:end -->を見る。
- 完了の報告には、実行したコマンドと生の出力を添えさせる。形は<!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](../verify/evidence-not-reports.md#what-counts)<!-- link:end -->を見る。
- 訂正が一度で通らなかったら、押し返しを重ねず、前のメッセージを直して送り直すか巻き戻す。話題が変わったら新しい会話にする。
- 分からないことは分からないと言ってよいと伝える。理由は<!-- link:begin why-hallucinations#what-helps -->[ハルシネーションはなぜ起きるか › 何に効くか](../basics/why-hallucinations.md#what-helps)<!-- link:end -->を見る。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Starting and iterating on a Kaggle competition in Google Antigravity](https://andlukyane.com/blog/kaggle-antigravity-s6e7)：Andrey Lukyanenko・英語・確認日 2026-11-04
- [Claude fabricates test results - reports ALL PASSED when tests are FAILING（Issue #46940）](https://github.com/anthropics/claude-code/issues/46940)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [context rot と紛らわしい情報](../basics/context-rot.md)

**次に読む**

- [@参照と、何を読ませるかの絞り込み](../context/choose-what-to-read.md)
- [git との付き合い方](../cli/working-with-git.md)
- [違うと返すより、巻き戻す・編集する](../context/rewind-dont-correct.md)
- [新しい会話を始めるタイミング](../context/when-to-start-fresh.md)
- [報告ではなく証拠を求める](../verify/evidence-not-reports.md)

**関連**

- [ハルシネーションはなぜ起きるか](../basics/why-hallucinations.md)
- [表示された思考は内部の計算と一致するとは限らない](../basics/unfaithful-reasoning.md)
- [すぐ同意して意見を変える（迎合）](caves-when-pushed.md)
- [同じ失敗を繰り返す（堂々巡り）](going-in-circles.md)
- [環境や道具が壊れたと言い出す](blames-the-tools.md)
- [もっともらしい嘘・出典の誤り](plausible-falsehoods.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
