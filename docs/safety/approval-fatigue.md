---
id: approval-fatigue
title: 承認疲れ
aliases: [approval fatigue, 確認を読まずに押す, 承認のしすぎ]
type: judgment
field: safety
chapter: 既定と承認
order: 20
level: 整える
priority: 推奨
surfaces: [claude-code, app]
principle: [握る, 縛る]
prevents: [境界がない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: 確認が多いと中身を読まずに承認するようになり、確認が安全の仕組みとして働かなくなる理由が分かる。確認を auto モード・allow ルール・サンドボックスで減らし、残す確認を絞れる。
signs:
  - {type: goal, text: どの確認を残し、どれを減らすかを決めたい}
  - {type: goal, text: 確認を減らしても、残した確認は中身を読んで判断したい}
prerequisites: [permission-modes-overview]
related: [what-auto-mode-stops, permission-rules, sandboxing, wrong-amount-of-approvals, keeps-stopping, over-reliance, review-bottlenecks, permission-modes-in-the-app, default-safety-settings]
tracks: [auto-mode, permission-modes]
outdated_advice: [approve-everything-first]
sources: [anthropic-eng-code-auto-mode, claude-blog-auto-mode-default, cc-docs-permission-modes, cc-docs-auto-mode-config, cc-docs-permissions, cc-docs-sandboxing]
volatility: 中
sections:
  - {title: なぜ読まなくなるか, anchor: why}
  - {title: 確認を減らす順番, anchor: reduce-prompts}
  - {title: 残す確認を選ぶ, anchor: keep-prompts}
  - {title: 確かめ方, anchor: check}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：確認が多いと読まずに押す理由が分かり、確認を減らして、残す確認を絞れる。
    - **いつ引くか**：どの確認を残し、どれを減らすかを決めたいとき、確認を減らしても、残した確認は中身を読んで判断したいとき。
    - **前提**：<!-- link:begin permission-modes-overview -->[権限モードの選び方](../cli/permission-modes-overview.md)<!-- link:end -->

<!-- textlint-disable -->
別名：approval fatigue・確認を読まずに押す・承認のしすぎ
<!-- textlint-enable -->

承認疲れは、確認の出る回数が多すぎて、人が中身を読まずに承認を押すようになり、確認が安全の仕組みとして働かなくなることである。このページは、確認を減らす手と、読んで判断する確認を残す基準を扱う。確認の数を減らすことと、残した確認を読むことは、1 つの判断の両面である。

## なぜ読まなくなるか {#why}

確認が多い環境では、人は確認の大半を読まずに承認する。ここでいう確認は、Claude が操作を動かす前に、人へ承認を求める表示のことである。

Anthropic 自身の測定が、この傾向を示す。2026-03-25 の engineering の記事は、手動の承認の確認は実際には 93% が承認されると書く。2026-08-07 の Anthropic の blog は、Claude Code の権限の確認の 97% が承認されると書く。どちらも Anthropic の一次の報告で、測った期間と母集団の説明はない。値が違うのは、時期とデータが違うからである（根拠：中）。

同じ blog は、1,053 人の有償の被験者の対照実験を報告する。1 回の確認を明らかに危ないコマンドに差し替えたとき、人が止めたのは 13.6%（143 件）だった。人はセッションが長くなるほど止めなくなった（根拠：中。ベンダー自身の実験で、課題の細部は記事による）。同じ実験で auto モードが止めた割合は記事が示すが、自社の製品の評価なので、ここでは人の側の結果だけを読む。

なぜ読まなくなるのか。確認の大半は安全な操作で、押せば進むという経験が積もる。押す動作が習慣になり、危うい 1 件も同じ動作で通る。警告が多すぎると読まれなくなる、という隣の分野の知見の当てはめである（類推）。

確認が働かないと、境界がないという原因がそのまま表に出る。確認は「人が握る」止め手なのに、握る手が離れている。人の側の落とし穴としては、判断を預けすぎることの一形である。判断まで預けると、もっともらしい誤りを採る理由は <!-- link:begin over-reliance#why-we-hand-over -->[判断を預けすぎる（過度依存） › なぜ預けてしまうか](../judgment/over-reliance.md#why-we-hand-over)<!-- link:end --> にある。確認だけでなくレビューも、量が増えると人に積もって浅くなる。その仕組みは <!-- link:begin review-bottlenecks#where-it-clogs -->[レビューのボトルネックと疲労 › 詰まる場所はレビューと動作確認](../team/review-bottlenecks.md#where-it-clogs)<!-- link:end --> にある。

確認が多すぎるのか少なすぎるのかを、まず診断したいときは <!-- link:begin wrong-amount-of-approvals#diagnosis -->[承認の確認が多すぎる・少なすぎる › 原因を安く確かめる順](../symptoms/wrong-amount-of-approvals.md#diagnosis)<!-- link:end --> から入る。確認ばかりで進まないときは <!-- link:begin keeps-stopping#diagnosis -->[確認ばかりで進まない・途中で止まる › 原因を安く確かめる順](../symptoms/keeps-stopping.md#diagnosis)<!-- link:end --> で原因を切り分ける。

## 確認を減らす順番 {#reduce-prompts}

確認を減らすときは、読まなくてよい確認から外し、外す前に守りを置く。守りを置かずに確認だけを外すと、任せる幅だけが広がる。

- **1. 繰り返し出る確認を数える**：同じ形の確認が何度も出ていないかを見る。数え方は <!-- link:begin wrong-amount-of-approvals#diagnosis -->[承認の確認が多すぎる・少なすぎる › 原因を安く確かめる順](../symptoms/wrong-amount-of-approvals.md#diagnosis)<!-- link:end --> にある。
- **2. 毎回同じ安全な操作を、狭い allow ルールで通す**：`npm test` のように、形が決まっていて取り返せる操作だけを許可する。書き方は <!-- link:begin permission-rules#minimal -->[権限ルール（allow・ask・deny） › 最小の使い方](../enforce/permission-rules.md#minimal)<!-- link:end --> にある。任意のコマンドを通す広いルールは、減らす手にならない。守りまで外れるうえ、auto モードでは広い allow ルールが働かなくなる。
- **3. サンドボックスで囲む**：サンドボックスは、コマンドの読み書きと通信を OS の層で囲う。自動許可を有効にすると、囲いの中の Bash コマンドは、Manual でも確認なしに実行される（例外あり）。囲える範囲と囲えない範囲は <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> で確かめる。
- **4. auto モードで残りを減らす**：別の分類器のモデルが操作を事前に見て、範囲を超えるものを止める。強制力はモデルの判定で、確認を減らすが安全を保証しない。すり抜けは <!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end --> にある。

auto モードが日常の操作を止めるときは、分類器に信頼する場所を教える。信頼する場所の記述は、個人の `~/.claude/settings.json` に置く。プロジェクトの設定に置いても、分類器は読まない。`/auto-mode-setup` が下書きを作る。止められた操作は `/permissions` の <!-- name:begin recently-denied-to-blocked -->Recently blocked（/permissions のタブ）<!-- name:end --> で見直せる。見直し方は <!-- link:begin what-auto-mode-stops#when-blocked -->[auto モードは何を止め、何を止めないか › 止められたときの見直し方](../enforce/what-auto-mode-stops.md#when-blocked)<!-- link:end --> にある。

「最初はすべての確認が出るので、承認していく」という前提の助言は古い。何も設定していなければ、対話のセッションの既定は <!-- fact:begin permission-mode-default-interactive -->auto モード（Claude Code 2.1.283 以降の、ターミナルと VS Code の対話のセッション。どのプランと提供元でも）（2026-11-04 時点）<!-- fact:end --> である。版で変わってきたので、今の既定と版は <!-- link:begin permission-modes-overview#defaults -->[権限モードの選び方 › 既定のモードと版](../cli/permission-modes-overview.md#defaults)<!-- link:end --> で確かめる。台帳の行は <!-- link:begin outdated-advice-ledger#approve-everything-first -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#approve-everything-first)<!-- link:end --> にある。

面によって、減らす手の置き場所が違う。

=== "アプリ"

    - Auto と Manual を選べる。読める範囲と行動できる範囲を、同時に広げない。
    - 専用のフォルダと低いリスクの作業から始める。手順は <!-- link:begin permission-modes-in-the-app#start-small -->[アプリの権限モード（Auto と Manual）と安全 › 専用のフォルダと、低いリスクの作業から](../app/permission-modes-in-the-app.md#start-small)<!-- link:end --> にある。

=== "Claude Code"

    - この節の 1 から 4 の順に、ルール・サンドボックス・auto モードで減らす。
    - 権限モードごとに何が確認なしで進むかは <!-- link:begin permission-modes-overview#modes -->[権限モードの選び方 › モードごとに確認なしで進むもの](../cli/permission-modes-overview.md#modes)<!-- link:end --> にある。

本ページの Claude Code の動作は、WSL・Linux の CLI を基準にしている。ほかの OS と IDE 拡張の動作は未確認である。

## 残す確認を選ぶ {#keep-prompts}

確認を残すのは、人が握る判断である。何を残すかは、取り返せるか・外へ届くか・自分の判断が要るかで決める。

- **残す**：取り返しがつかない操作（push、外への送信、削除、本番への反映）。囲いの外へ届く操作。方針の分かれ目で、自分が選ばないと決まらないもの。
- **減らす**：取り返せて、囲いの中で、毎回同じ形の操作。

残す確認は、機能の名前で決めず、操作の形で決める。外へ出る操作は `ask` ルールで、確認に残せる。内容を絞った ask ルールは、auto モードでも必ず確認を出す。分類器が自動で承認することはない。決して実行させない操作は deny ルールにする。deny は分類器より先に効く。

会話で「確認なしに push しない」と言っておく方法は、確かな保証ではない。圧縮でその発言が消えると、分類器は読めなくなりうる。守りたい境界は、ルールに書く。

<!-- gen:begin snippet approval-fatigue/narrow-allow-and-ask -->
<!-- textlint-disable -->

??? example "雛形：毎回同じ安全なコマンドは allow ルールで通し、外へ出す操作は ask ルールで確認に残す設定"

    ```json
    {
      "permissions": {
        "allow": [
          "Bash(npm test)"
        ],
        "ask": [
          "Bash(git push *)",
          "Bash(gh pr create *)"
        ]
      }
    }
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。

<!-- textlint-enable -->
<!-- gen:end snippet approval-fatigue/narrow-allow-and-ask -->

雛形の ask ルールは、`git push` で始まるコマンドに当たる。`git -C <dir> push` のように別の形で書かれた push には当たらない。コマンド全体を見て止めたいときは、deny ルールか、フックで強制する。ルールの評価の順番は <!-- link:begin permission-rules#evaluation-order -->[権限ルール（allow・ask・deny） › 評価の順番（deny → ask → allow）](../enforce/permission-rules.md#evaluation-order)<!-- link:end -->、子プロセスに効かない場面は <!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end --> にある。

残した確認は、説明ではなくコマンドそのものを読む。説明は Claude かツールが書いたもので、中身と食い違いうる。

!!! example "判断例：確認の大半が npm test とファイル編集だったとき"
    - **状況**：Claude Code を auto モードで使っている。確認の大半は `npm test` とファイルの編集で、後半は中身を見ずに押している。push と依存の追加の確認も、同じ調子で押してしまった。
    - **迷う候補**：(a) 確認を全部残し、読む意識を高めて対応する。(b) 毎回同じ安全な操作を allow ルールとサンドボックスで外し、外へ出る操作だけを確認に残す。
    - **選んだもの**：(b)。`npm test` を狭い allow ルールで通し、`git push` と `gh pr create` を ask ルールで確認に残す。
    - **理由**：読む意識は長いセッションでは続かない。実験でも、人はセッションが長くなるほど止めなくなった。残す確認が少なければ、1 件ずつに目が行く。ただし ask ルールは別の形の push に当たらないので、push を確実に止めたいなら deny ルールかフックを足す。

確認を減らす前に決めておくことがある。減らした分の守りを、何に任せるのかである。ルールとサンドボックスは鍵で、auto モードはモデルの判定である。鍵に任せた確認は外してよく、モデルの判定に任せた確認は、すり抜けを前提に残す。段階ごとの既定の設定は <!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](default-safety-settings.md#by-stage)<!-- link:end --> が正本で、ここでは繰り返さない。

## 確かめ方 {#check}

確認を減らした後に、読んで判断できているかを記録で測る。感覚では、読んだつもりになりやすい。

- **数えて比べる**：減らす前後の 1 週間で、確認が出た回数と、中身を読んで押した回数を数える。母数が小さい自己申告なので、傾向として読む（根拠：弱）。
- **やめどきを先に決める**：残した確認を、読まずに続けて押したら、その種類を allow ルールか deny ルールに移す。基準の回数は自分で決める。
- **止められた操作を見直す**：auto モードが止めた操作が続くなら、ルールの不足か、分類器に教える場所の不足を疑う。足す前に、その操作が本当に通してよいかを読む。
- **設定が効いているかを見る**：分類器が実際に使う設定は、`claude auto-mode config` で読める。ルールを足した後に確かめる。

減らしすぎて怖い、または多すぎて進まないときは、症状のページへ戻る。確認が多すぎて読まずに押す、少なすぎて怖いときの調整先は <!-- link:begin wrong-amount-of-approvals#routes -->[承認の確認が多すぎる・少なすぎる › 原因ごとの振り分け先](../symptoms/wrong-amount-of-approvals.md#routes)<!-- link:end -->、確認ばかりで進まないときは <!-- link:begin keeps-stopping#routes -->[確認ばかりで進まない・途中で止まる › 原因ごとの振り分け先](../symptoms/keeps-stopping.md#routes)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [How we built Claude Code auto mode: a safer way to skip permissions](https://www.anthropic.com/research/claude-code-auto-mode)：Anthropic・英語・確認日 2026-11-04
- [Auto mode is now the default in Claude Code for Pro, Max, Ultra, and Team plans](https://claude.com/resources/articles/auto-mode-default-in-claude-code)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Configure auto mode](https://code.claude.com/docs/en/auto-mode-config)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [権限モードの選び方](../cli/permission-modes-overview.md)

**関連**

- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [承認の確認が多すぎる・少なすぎる](../symptoms/wrong-amount-of-approvals.md)
- [確認ばかりで進まない・途中で止まる](../symptoms/keeps-stopping.md)
- [判断を預けすぎる（過度依存）](../judgment/over-reliance.md)
- [レビューのボトルネックと疲労](../team/review-bottlenecks.md)
- [アプリの権限モード（Auto と Manual）と安全](../app/permission-modes-in-the-app.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](default-safety-settings.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
