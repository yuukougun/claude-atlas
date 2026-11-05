---
id: when-ai-is-unavailable
title: AI が使えないときの備え（障害・上限）
nav_title: AI が使えないときの備え
aliases: [障害のとき, サービスの停止, 上限で止まったとき, 代わりの手段]
type: concept
field: cost
chapter: 任せて回すとき
order: 110
level: 任せる
priority: 推奨
surfaces: [app, claude-code, api]
principle: [握る]
prevents: []
pitfalls: [預けすぎる]
scenes: [開発, チーム, コンテスト]
summary: 障害や上限で AI が止まっても仕事を続けられるように、AI なしで最低限を進められる状態と、止まったときの切り替え先を先に決めておける。
signs:
  - {type: situation, text: 締め切りの直前に AI が使えなくなったら困る}
  - {type: symptom, text: 障害や上限で止まり、作業が進められなくなった}
prerequisites: [how-usage-limits-work]
related: [over-reliance, how-much-understanding-to-keep, own-generated-code, what-not-to-delegate, handoff-documents, progress-files, usage-credits-basics, rate-limits-and-errors, competition-day-operations]
tracks: [usage-limits, auto-continue]
outdated_advice: []
sources: [hc-usage-limits, hc-claude-code-plan, hc-wrap-up-allowance, cc-docs-interactive-mode, cc-docs-settings-reference]
volatility: 中
sections:
  - {title: 止まり方の種類（障害・上限・規則）, anchor: kinds}
  - {title: AI なしで最低限を進められる状態, anchor: minimum-without-ai}
  - {title: 止まったときの切り替え先, anchor: fallbacks}
  - {title: どの原理・どの原因に関わるか, anchor: cause}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：AI が止まる 3 つの形（障害・上限・規則）と、止まっても最低限を進められる状態の作り方、止まったときの切り替え先の決め方が分かる。
    - **いつ引くか**：締め切りの直前に AI が使えなくなったら困るとき。障害や上限で止まり、作業が進められなくなったとき。
    - **前提**：<!-- link:begin how-usage-limits-work -->[利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)<!-- link:end -->

<!-- textlint-disable -->
別名：障害のとき・サービスの停止・上限で止まったとき・代わりの手段
<!-- textlint-enable -->

AI が使えない状態は、仕事の流れの中でいつか起きるものとして扱う。このページは、止まる前に「AI なしで最低限を進められる状態」と「止まった理由ごとの切り替え先」を決めておく考え方を扱う。止まった後の復旧の手順ではなく、止まる前の備えの話である。

## 止まり方の種類（障害・上限・規則） {#kinds}

AI が止まる理由は、障害・上限・規則の 3 つに分けられる。理由によって、いつ戻るかと、先に決めておけることが違う。

| 種類 | 誰の都合か | 戻る見込み | まず見るもの |
| --- | --- | --- | --- |
| 障害 | サービスの側 | 利用者には決められず、見通しも立たないことがある | 公式の稼働状況の情報 |
| 上限 | 自分の使用量（面をまたいで共有する枠） | 枠の種類ごとに戻る時刻がある | 残りを見る場所 |
| 規則 | 大会や職場の決まり | 変わらない。事前に分かる | 規約・部門・社内の方針 |

- 障害は、始まる時刻と終わる時刻を利用者が決められない。備えは、戻る時刻を当てにしない形にする。
- 上限は、戻る時刻が分かる。枠の種類と戻り方は <!-- link:begin how-usage-limits-work#limit-types -->[利用上限の仕組み（面をまたいで共有する枠） › 枠の種類と戻る時刻（プランごとの表）](how-usage-limits-work.md#limit-types)<!-- link:end -->、残りを見る場所は <!-- link:begin how-usage-limits-work#where-to-check -->[利用上限の仕組み（面をまたいで共有する枠） › 残りを見る場所](how-usage-limits-work.md#where-to-check)<!-- link:end --> にある。アプリ・Claude Code・Desktop は同じ枠を分け合うので、<!-- link:begin how-usage-limits-work#shared-limit -->[利用上限の仕組み（面をまたいで共有する枠） › 面をまたいで一つの枠](how-usage-limits-work.md#shared-limit)<!-- link:end --> のとおり、面を変えても逃げ道にならない。
- 規則は、使えないことが事前に分かる。AI の利用を禁じる大会や、使える範囲を決めた職場がこれに当たる。大会の運用は <!-- link:begin competition-day-operations#fallback -->[本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態） › AI が止まっても続けられる備え](../contest/competition-day-operations.md#fallback)<!-- link:end --> が持つ。
- API で組んだ仕組みが混雑や上限で止まるときのエラーの見分け方と再試行は、<!-- link:begin rate-limits-and-errors#kinds -->[rate limits とエラー（混雑と再試行） › エラーの見分け方（自分の上限・全体の混雑・要求の誤り）](../api/rate-limits-and-errors.md#kinds)<!-- link:end --> が持つ。このページはそこを繰り返さない。

止まったのが障害か上限かが分からないときは、自分の残りの使用量を先に見る。使用量に余裕があるのに止まっているなら、障害を疑う。

## AI なしで最低限を進められる状態 {#minimum-without-ai}

AI なしで最低限を進められる状態とは、AI が止まっても「これだけは出す」という線まで、人の手で届く状態をいう。線を先に決めておくと、止まった時点で迷う時間が減る。

この状態は、次の 4 つで作る。

- **最低限の完了を決める**：提出物やリリースのうち、これだけは出すというものと、その確かめ方を先に書く。決めるのは人である。完了の定義は AI に任せない。持ち主は <!-- link:begin what-not-to-delegate#what-humans-hold -->[任せないもの（評価・採否・撤退・中核の理解） › どの段階でも人が握るもの](../delegate/what-not-to-delegate.md#what-humans-hold)<!-- link:end --> である。
- **確かめ方を手元に置く**：テストや動作確認の手順を、AI を通さずに実行できる形にしておく。確かめ方が AI の側にしかないと、止まった時点で採否を決められない。
- **途中の状態をファイルに残す**：計画・決めたこと・分かったことを、作業の最中から進捗ファイルに書かせる。上限や障害は予告なく来るので、止まる直前にまとめて書かせる前提にしない。分け方と回し方は <!-- link:begin progress-files#cycle -->[進捗ファイルで、途中から再開できるようにする › 開始と更新の回し方](../context/progress-files.md#cycle)<!-- link:end -->、会話をまたぐ引き継ぎは <!-- link:begin handoff-documents#resume -->[handoff 文書と document-and-clear › 新しい会話での再開の仕方](../context/handoff-documents.md#resume)<!-- link:end --> を使う。
- **中核の理解を手元に残す**：自分のコードの中核を説明できないと、AI が止まったときに直せない。線引きは <!-- link:begin how-much-understanding-to-keep#core-and-periphery -->[どこまで理解を手放してよいか（中核と周辺） › 中核と周辺を分ける](../judgment/how-much-understanding-to-keep.md#core-and-periphery)<!-- link:end -->、採る前の確かめ方は <!-- link:begin own-generated-code#gate -->[生成コードを自分のものにする › 自分の言葉で言い直してから採る](../verify/own-generated-code.md#gate)<!-- link:end --> を使う。

この考え方の根拠は強くない。大会中に AI の上限や障害に当たった参加記は、調べた範囲で見つからなかった。AI なしで最低限の提出を作れる状態は、AI の利用を禁じる大会への準備と同じ形になる、という推論にとどまる（推論・実践例なし）。個々の手は、それぞれ別のページが扱っている。

AI を使わない時間をわざと残すことも、この状態を保つ手になる。理由と進め方は <!-- link:begin how-much-understanding-to-keep#ai-free-time -->[どこまで理解を手放してよいか（中核と周辺） › AI を使わない時間を残す](../judgment/how-much-understanding-to-keep.md#ai-free-time)<!-- link:end --> にある。

## 止まったときの切り替え先 {#fallbacks}

切り替え先は、止まった理由ごとに先に決めておく。選択肢は 4 つある。待つ、追加の枠で続ける、別の経路を使う、AI なしで進める、である。

- **待つ**：上限は戻る時刻まで、障害は復旧まで待つ。待つ間に AI なしでできる作業があれば、その作業へ移る。
- **追加の枠で続ける**：プランの上限を使い切っても、usage credits で従量課金に切り替えて続けられる。思わぬ請求を防ぐため、上限額と通知を先に決めておく。仕組みは <!-- link:begin usage-credits-basics#how-it-works -->[usage credits（上限を超えた分の従量課金） › 切り替わる仕組み](usage-credits-basics.md#how-it-works)<!-- link:end -->、上限額は <!-- link:begin usage-credits-basics#set-a-cap -->[usage credits（上限を超えた分の従量課金） › 上限額と通知を決める](usage-credits-basics.md#set-a-cap)<!-- link:end --> にある。
- **別の経路を使う**：API は、プランの枠とは別の経路である。違いは <!-- link:begin usage-credits-basics#vs-api-credits -->[usage credits（上限を超えた分の従量課金） › API credits との違い](usage-credits-basics.md#vs-api-credits)<!-- link:end --> にある。
- **AI なしで進める**：先に決めた最低限の完了の線（手順書の「最低限の完了」）まで、人の手で進める。作り方は上の節にある。

面ごとの違いは、次のとおりである。

=== "アプリ"

    - 上限で止まったら、戻る時刻を見る。戻る時刻が締め切りより前なら、待つ選択肢がある。
    - 会話を片付けても、使った分は戻らない。誤解は <!-- link:begin how-usage-limits-work#misconceptions -->[利用上限の仕組み（面をまたいで共有する枠） › よくある誤解](how-usage-limits-work.md#misconceptions)<!-- link:end --> にある。
    - 上限に当たったときの動きは <!-- link:begin how-usage-limits-work#when-you-hit-the-limit -->[利用上限の仕組み（面をまたいで共有する枠） › 上限に当たったとき](how-usage-limits-work.md#when-you-hit-the-limit)<!-- link:end --> が持つ。

=== "Claude Code"

    - claude.ai の利用上限で止まった作業を、開いたままのセッションで待ち、上限が戻った後に自動で続ける設定がある。続ける回数は <!-- fact:begin auto-continue-max-times -->3 回まで（2026-11-05 時点）<!-- fact:end --> である。続けた作業でも、許可の確認は出る。
    - 自動の継続は、放っておいてよい仕組みではない。任せる幅が広がるので、止まる前に完了の条件と進捗ファイルを整えておく。整え方は <!-- link:begin progress-files#guards -->[進捗ファイルで、途中から再開できるようにする › 先に整える守り](../context/progress-files.md#guards)<!-- link:end --> にある。
    - 応答の途中で上限に達したとき、区切りまで少しだけ続ける仕組み（Wrap-Up Allowance）もある。使える条件はプランと版で違うので、<!-- link:begin how-usage-limits-work#when-you-hit-the-limit -->[利用上限の仕組み（面をまたいで共有する枠） › 上限に当たったとき](how-usage-limits-work.md#when-you-hit-the-limit)<!-- link:end --> で確かめる。
    - API キーでの利用や、背景のセッション、`-p` では自動の継続が使えない。そのときは、手で再開できるように進捗ファイルを頼る。
    - WSL・Linux の CLI を基準に書いた。ほかの OS と IDE 拡張の動作は未確認である。

=== "API"

    - API で組んだ仕組みは、プランの上限の仕組みの外にある。止まるときは、混雑や上限のエラーとして返る。見分け方と再試行は <!-- link:begin rate-limits-and-errors#retry -->[rate limits とエラー（混雑と再試行） › 再試行の考え方（間隔を広げ、回数に上限を設ける）](../api/rate-limits-and-errors.md#retry)<!-- link:end --> が持つ。
    - 再試行しても通らない時間が続くことを前提に、仕組みの側で「AI なしの手順に落とす」経路を作っておく。たとえば、処理を溜めておいて人が見る、定型の返答に切り替える、などである（推論・実践例なし）。
    - エラーにならずに止まる応答（長さの上限や拒否）は、<!-- link:begin rate-limits-and-errors#non-error-stops -->[rate limits とエラー（混雑と再試行） › エラーにならずに止まる応答（長さの上限・拒否）](../api/rate-limits-and-errors.md#non-error-stops)<!-- link:end --> で扱う。

切り替え先を決めた後は、手順書にまとめて、止まる前に読める場所へ置く。雛形は、止まった理由ごとの切り替え先と、最低限の完了の条件と、切り替えを決める人を書く欄を持つ。

<!-- gen:begin snippet when-ai-is-unavailable/no-ai-runbook -->
<!-- textlint-disable -->

??? example "雛形：AI が止まったときの手順書の雛形"

    ```markdown
    AI が使えないときの手順書（プロジェクトの `docs/no-ai-runbook.md` などに置く）

    最低限の完了（AI なしでも出すもの）
    - 出すもの：<提出物・リリース・報告のうち、これだけは出す、というもの>
    - 満たす条件：<人が確かめられる形で書く。例：指定のテストが通る、手順どおりに動く>
    - 切り捨てるもの：<最低限に入れない改善・整理・追加の機能>

    AI なしで進める作業
    - 今すぐ手元でできる作業：<例：テストの追加、設定の確認、文書の下書き>
    - 手元で確かめる方法：<テストのコマンド、動作確認の手順>
    - 手元にある資料：<ライブラリの資料、過去の実装、メモの置き場所>

    止まった理由ごとの切り替え先
    - 障害：公式の稼働状況を見る。見通しが締め切りに間に合わないなら、AI なしの作業へ移る。
    - 上限：戻る時刻を見る。締め切りより前に戻るなら待つ。後なら、<usage credits で続ける／AI なしで進める> のどちらかを選ぶ。
    - 規則で使えない：規則の範囲を確かめ、使える道具と使えない道具を分ける。
    - 切り替えを決める人：<名前または役割>
    - 連絡する相手：<名前または役割>

    再開するとき
    - 状態の置き場所：<進捗ファイルのパス>
    - AI の出力を採る前に確かめるもの：<テスト、差分の目視、説明できるか>
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.234。

<!-- textlint-enable -->
<!-- gen:end snippet when-ai-is-unavailable/no-ai-runbook -->

!!! example "判断例：締め切り前に上限へ当たったとき"
    - **状況**：締め切りの前日の午後に、利用上限へ当たった。戻る時刻は締め切りの後になる。残りの作業は、実装の仕上げとテストの追加である。
    - **迷う候補**：usage credits に切り替えて AI で続ける。または、AI なしで最低限の完了まで進める。
    - **選んだもの**：手順書の「最低限の完了」まで AI なしで進め、残りの仕上げにだけ、上限額を決めたうえで usage credits を使う。
    - **理由**：テストが手元で実行できるので、最低限の完了は人の手で確かめられる。追加の枠は、請求の上限額を先に決めておけば、仕上げに限って使える。両方を先に決めてあったから、迷う時間が短くなった。

## どの原理・どの原因に関わるか {#cause}

このページが関わる原理は「握る」で、人の側の落とし穴は「預けすぎる」である。どちらも、備えの形を決める。

- **握る**：完了の定義、採否、切り替えの判断は、AI が止まっても人の手元に残る。握っていれば、何を出せば完了かを、止まった後でも決められる。範囲は <!-- link:begin what-not-to-delegate#what-it-prevents -->[任せないもの（評価・採否・撤退・中核の理解） › 握ることが防ぐもの](../delegate/what-not-to-delegate.md#what-it-prevents)<!-- link:end --> が持つ。
- **預けすぎる**：判断や理解まで AI に預けていると、止まったときに何も進められない。止まる事態は、預けすぎの度合いを測る機会になる。理由と手元に残す判断は <!-- link:begin over-reliance#what-to-keep -->[判断を預けすぎる（過度依存） › 手元に残す判断](../judgment/over-reliance.md#what-to-keep)<!-- link:end --> が持つ。

このページが防ぐのは、AI の誤りではなく、AI が使えないことによる停止である。特定の原因を直すページではないので、`prevents` は空にしてある。

## よくある誤解 {#misconceptions}

- **「待てば戻るから、備えは要らない」**：戻る時刻が締め切りより後なら、待つだけでは間に合わない。障害は、戻る時刻そのものが分からない。
- **「会話を片付ければ上限が戻る」**：使った分は戻らない。<!-- link:begin how-usage-limits-work#misconceptions -->[利用上限の仕組み（面をまたいで共有する枠） › よくある誤解](how-usage-limits-work.md#misconceptions)<!-- link:end --> にある。
- **「別の面に移れば続けられる」**：アプリ・Claude Code・Desktop は同じ枠を分け合う。上限が理由なら、面を変えても止まったままである。
- **「自動の継続があるから、放っておいてよい」**：続ける回数に上限があり、続けた作業でも許可の確認は出る。開いたセッションで待つ必要もある。
- **「AI が止まったら、人は何もできない」**：これは、預けすぎた結果の状態である。最低限の線を決め、手元に確かめ方を置いておけば、止まっても進められる。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [利用上限の仕組み（面をまたいで共有する枠）](how-usage-limits-work.md)

**関連**

- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- [どこまで理解を手放してよいか（中核と周辺）](../judgment/how-much-understanding-to-keep.md)
- [生成コードを自分のものにする](../verify/own-generated-code.md)
- [任せないもの（評価・採否・撤退・中核の理解）](../delegate/what-not-to-delegate.md)
- [handoff 文書と document-and-clear](../context/handoff-documents.md)
- [進捗ファイルで、途中から再開できるようにする](../context/progress-files.md)
- [usage credits（上限を超えた分の従量課金）](usage-credits-basics.md)
- [rate limits とエラー（混雑と再試行）](../api/rate-limits-and-errors.md)
- [本番の運用（開始直後に評価器・終盤は凍結・AI なしでも提出できる状態）](../contest/competition-day-operations.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code with your Pro, Max, or Ultra plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)：Anthropic・英語・確認日 2026-11-04
- [Claude Code Wrap-Up Allowance](https://support.claude.com/en/articles/17040437-claude-code-wrap-up-allowance)：Anthropic・英語・確認日 2026-11-04
- [Interactive mode](https://code.claude.com/docs/en/interactive-mode)：Anthropic・英語・確認日 2026-11-04
- [All settings](https://code.claude.com/docs/en/settings-reference)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
