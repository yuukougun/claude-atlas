---
id: visual-checks
title: 画面で確かめる（ブラウザ・スクリーンショット・/verify）
nav_title: 画面で確かめる
aliases: [スクリーンショットで確かめる, ブラウザで動作確認, E2E で確かめる]
type: feature
field: verify
chapter: 完了を確かめる
order: 40
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [確かめていない]
pitfalls: []
scenes: [開発]
summary: 画面を持つ成果物を、ブラウザの操作やスクリーンショットの比較で、人が使うのと同じように確かめさせられる。単体テストや応答の確認だけで完了とみなすのを防ぐ。
signs:
  - {type: goal, text: 見た目の崩れを確かめさせたい}
  - {type: symptom, text: テストは通るのに、画面を開くと動かない}
  - {type: goal, text: モックと出来上がりの画面の違いを挙げさせたい}
prerequisites: [evidence-not-reports]
related: [browser-control, images-and-voice, verification-ladder, browser-agent-cautions, looks-are-not-quality, frontend-design, make-slides, claims-done-but-isnt]
tracks: [claude-in-chrome, verify-skill]
outdated_advice: []
sources: [cc-docs-skills, cc-docs-commands, cc-docs-chrome, hc-claude-in-chrome, cc-docs-best-practices, anthropic-eng-effective-harnesses-long-running, cc-changelog]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 人のユーザーとして確かめさせる, anchor: as-a-user}
  - {title: スクリーンショットで比べる, anchor: screenshots}
  - {title: 依頼の雛形, anchor: templates}
  - {title: 効かない場面と落とし穴, anchor: limits}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：画面を持つ成果物を、ブラウザの操作やスクリーンショットの比較で、人が使うのと同じように確かめさせられる。
    - **いつ引くか**：見た目の崩れを確かめさせたいとき。テストは通るのに、画面を開くと動かないとき。モックと出来上がりの画面の違いを挙げさせたいとき。
    - **強制力**：<!-- gen:begin feature verify-skill/enforcement -->—<!-- gen:end feature verify-skill/enforcement -->（値は数値ファイルの登録待ち）。確かめる手段を渡すだけで、確かめずに完了と言うことは止められない。止めたいときは、完了の条件にスクリーンショットを入れ、証拠として受け取る。
    - **前提**：<!-- link:begin evidence-not-reports -->[報告ではなく証拠を求める](evidence-not-reports.md)<!-- link:end -->

<!-- textlint-disable -->
別名：スクリーンショットで確かめる・ブラウザで動作確認・E2E で確かめる
<!-- textlint-enable -->

画面で確かめるとは、画面を持つ成果物を起動して開き、操作して見た目を撮り、人が使うのと同じ順に確かめさせることである。単体テストや応答の確認では見つからない「動かない」「崩れている」を拾うために使う。Claude Code では、ブラウザを操作する連携か、バンドルのスキル `/verify` が手段になる。

## 使いどころ {#when}

画面で確かめさせる目的は、「確かめていない」という原因を防ぐことである。コードが正しく見えて、テストも通るのに、画面を開くと動かない。この食い違いは、テストが画面の外側だけを見ているときに起きる。

Anthropic の長時間エージェントの運用例では、Claude は単体テストや `curl` を開発サーバーに打つだけで、機能が端から端まで動くかを確かめないまま完了と判断しがちだった。そこで、ブラウザの自動操作を使い、人のユーザーとして確かめるよう明示した。すると性能が大きく改善し、コードを見ただけでは分からない不具合が見つかった（根拠：中。[Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) の時点のもので、モデルの世代で変わりうる）。

使うのは、次のような場面である。

- 画面を持つものの実装を任せ、仕上がりを確かめさせる段。任せる幅が広いほど、人が途中で画面を見る機会が減るので、確かめる手段を先に渡す。
- 「完了」と言われたが、画面を開くと動かないとき。原因の切り分けは <!-- link:begin claims-done-but-isnt#diagnosis -->[「完了」と言うが終わっていない › 原因を安く確かめる順](../symptoms/claims-done-but-isnt.md#diagnosis)<!-- link:end --> で行う。
- モックや手本の画面と、出来上がりの違いを挙げさせたいとき。

どの確かめ方を、どの段で任せるかは <!-- link:begin verification-ladder#choose-step -->[検証の階段 › 任せる幅に合わせて段を選ぶ](verification-ladder.md#choose-step)<!-- link:end --> で選ぶ。「画面でも確かめて」と書き足すより、操作する手段と、証拠の形を渡すほうが効く。

## 人のユーザーとして確かめさせる {#as-a-user}

人のユーザーとして確かめさせるとは、画面を開き、クリックや入力を実際に行い、起きたことを見て報告させることである。確かめ方の手段は、2 つある。

=== "Claude Code"

    - **ブラウザを操作する連携**：Claude in Chrome（成熟度 <!-- gen:begin feature claude-in-chrome/maturity -->GA<!-- gen:end feature claude-in-chrome/maturity -->）で、Chrome を操作させる。選び方と任せない作業は <!-- link:begin browser-control#which-to-use -->[Claude in Chrome と computer use（ブラウザと画面の操作） › コネクタ・ブラウザ・画面の順に選ぶ](../surfaces/browser-control.md#which-to-use)<!-- link:end --> にある。プロジェクトに入れたブラウザ自動操作の道具（Playwright など）を使う方法もある。第三者の道具の例として名前を出すだけで、推薦ではない。
    - **`/verify`**：バンドルのスキルで、アプリを作って動かし、結果を見て変更を確かめる。テストや型の検査に頼らない。成熟度は <!-- gen:begin feature verify-skill/maturity -->GA<!-- gen:end feature verify-skill/maturity --> である。自分で呼んだときだけ動く。手順を `.claude/skills/verify/SKILL.md` に記録できる。

`/verify` は手動専用なので、依頼の中で「人のユーザーとして画面で確かめて」と書き、操作の手順と返してほしい証拠を指定するほうが、確かめ方が揃う。なお、自作のスキルを `verify` という名前で置くと、コミットの前に Claude がそれを実行する。この動きが入った版は <!-- fact:begin skill-verify-simplify-commit-min-version -->Claude Code 2.1.286 以降（2026-11-04 時点）<!-- fact:end --> である。自分で書いた手順を、コミットのたびに走らせたいなら使える。

依頼には、次の 4 つを入れる。

1. 起動の方法と、起動できたことの確かめ方
2. 行う操作の一覧（正常に進む操作と、エラーになるはずの操作の両方）
3. 操作ごとに返す証拠（スクリーンショットのファイル名と、画面の表示・遷移・コンソールのエラー）
4. 操作できなかったものを「確かめていない」と書かせること

証拠の形は、報告ではなく実行した操作と見えた画面である。この考え方は <!-- link:begin evidence-not-reports#what-counts -->[報告ではなく証拠を求める › 証拠の形（コマンド・生の出力・分母）](evidence-not-reports.md#what-counts)<!-- link:end --> と同じで、ここではそれを画面に当てはめている。

!!! example "判断例：テストが通った画面の変更"
    - **状況**：入力フォームの検証を直した。単体テストは全部通ったと報告が来た。
    - **迷う候補**：テストが通っているので、そのまま受け入れる。または、画面でも確かめさせてから受け入れる。
    - **選んだもの**：画面で確かめさせる。正常な入力、必須の項目を空にした入力、長すぎる入力の 3 つを操作させ、操作ごとのスクリーンショットを返させる。
    - **理由**：単体テストは検証の関数だけを見ていて、エラーの表示が画面に出るかは見ていない。画面の操作は 3 回で済み、確かめるのに安い。

## スクリーンショットで比べる {#screenshots}

スクリーンショットで比べるとは、画面を撮った画像を、モックや前の版と見比べさせて、違いを挙げさせることである。見た目の崩れ、配置や色のずれ、部品の欠けは、文字の出力では見えない。画像として読ませると見つかる。画像を渡す側の注意は <!-- link:begin images-and-voice#images -->[画像・スクリーンショット・音声で渡す › 画像で渡すと速いもの](../prompting/images-and-voice.md#images)<!-- link:end --> にある。

比べ方は、2 つある。

- **モックと出来上がりを比べる**：モックの画像と、同じ状態で撮った出来上がりの画像を並べ、違いを一覧にさせる。直す前の一覧と、直した後の一覧を分けて返させる。デザインの手本を渡して作らせる流れは <!-- link:begin frontend-design -->フロントエンドのデザイン（準備中）<!-- link:end --> にある。
- **直す前と直した後を比べる**：変更の前後で同じ手順のスクリーンショットを撮り、意図していない違いがないかを見させる。

比べる条件は揃える。画面の幅、表示するデータ、ログインの状態が違うと、違いの一覧に本物の崩れと条件の差が混ざる。幅は 2 通りほど決めて、撮る状態を依頼に書く。

違いの一覧は、場所・モックの見た目・出来上がりの見た目・直す必要があるかの判断、の 4 つの欄で返させると、直す・直さないを人が決めやすい。画面の資料やスライドの見た目を確かめる場合の流れは <!-- link:begin make-slides -->資料・スライドを作る（準備中）<!-- link:end --> にある。

## 依頼の雛形 {#templates}

画面で確かめさせる依頼の雛形を 2 つ置く。どちらも動作は確かめていない。使うときは新しいセッションで試す。

<!-- gen:begin snippet visual-checks/as-a-user -->
<!-- textlint-disable -->

??? example "雛形：画面で確かめさせる依頼（人のユーザーとして操作する）"

    ```markdown
    [機能名または画面] を実装したので、人のユーザーとして画面で確かめて。単体テストと curl の結果だけで完了としない。

    1. [開発サーバーの起動コマンド] で起動する。起動できたか、ログとポートで確かめる。
    2. ブラウザで [開始の URL] を開き、次の操作を実際に行う。
       - [操作 1：例 ログインして一覧を開く]
       - [操作 2：例 新規作成して保存し、一覧に出るか見る]
       - [操作 3：例 必須の項目を空にして保存し、エラーの表示を見る]
    3. 操作ごとに、画面の見た目（スクリーンショットのファイル名）と、起きたこと（表示・遷移・コンソールのエラー）を書く。
    4. 動かなかった操作は、直さずに先に一覧にする。直したときは、同じ操作をもう一度行って確かめ直す。

    最後に、行った操作の一覧、スクリーンショットのファイル名、動かなかったものを返す。操作できなかったものは「確かめていない」と書く。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.72。

<!-- textlint-enable -->
<!-- gen:end snippet visual-checks/as-a-user -->

<!-- gen:begin snippet visual-checks/compare-with-mock -->
<!-- textlint-disable -->

??? example "雛形：モックと出来上がりの違いを挙げさせる依頼"

    ```markdown
    [画面名] の出来上がりを、モック（[モックの画像のパス]）と見比べて。

    1. [開発サーバーの起動コマンド] で起動し、[URL] を開いて、モックと同じ状態の画面のスクリーンショットを撮る。幅は [幅 1] と [幅 2] の 2 通り。
    2. モックと出来上がりを、次の観点で見比べる。
       - 配置と余白
       - 文字の大きさと折り返し
       - 色
       - 部品の有無と状態（ホバー・無効・エラー）
    3. 違いを一覧にする。1 行に、場所・モックの見た目・出来上がりの見た目・直す必要があるかの判断を書く。
    4. 直す必要があるものだけを直し、同じ手順でスクリーンショットを撮り直して、一覧の行を更新する。

    直す前の一覧と、直した後の一覧を分けて返す。見比べられなかった観点は「確かめていない」と書く。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.72。

<!-- textlint-enable -->
<!-- gen:end snippet visual-checks/compare-with-mock -->

## 効かない場面と落とし穴 {#limits}

画面で確かめさせても、防げないことがある。

- **確かめる側が見落とす**：画像を読むのもモデルの判定で、見落としは残る。公式の運用例でも、Claude の視覚とブラウザ操作の限界のため、すべての不具合は拾えなかった。ブラウザ標準のアラートのダイアログは操作の道具から見えず、その表示を使う機能は不具合が多く残った（根拠：中。同じ運用例の時点のもの）。
- **見た目が良いことは品質の証拠にならない**：スクリーンショットが整っていても、中の処理が正しいとは限らない。<!-- link:begin looks-are-not-quality -->[見た目は品質の証拠ではない](looks-are-not-quality.md)<!-- link:end --> の考え方で、画面の確認は、単体テストやレビューの代わりではなく、足す確認として使う。
- **確かめる条件が本番と違う**：開発用のデータ、ログイン済みの状態、広い画面だけで撮ると、本番の崩れを見逃す。
- **Web の内容が入力になる**：ブラウザを操作させると、開いたページの文が Claude への入力になる。ログイン済みのサイトや開いているアプリまで届くので、任せる範囲は <!-- link:begin browser-agent-cautions#reach -->[ブラウザや画面の操作を任せるときの注意 › 届く範囲（ログイン済みのサイト・開いているアプリ）](../safety/browser-agent-cautions.md#reach)<!-- link:end --> で決める。機微な作業は任せない。確かめる対象は、自分で起動した開発環境にとどめる。
- **手動専用の機能は自動では動かない**：`/verify` は、自分で呼んだときだけ動く。毎回の完了で必ず動かしたいなら、完了の条件に入れるか、仕組みに移す。段の選び方は <!-- link:begin verification-ladder#four-steps -->[検証の階段 › 四つの段](verification-ladder.md#four-steps)<!-- link:end --> にある。
- **版で変わる**：`/verify` の動きは版で変わるので、使う版で確かめる。Windows と macOS、IDE の拡張での動きは未確認である。

## 比べる相手 {#compare}

- <!-- link:begin verification-ladder -->[検証の階段](verification-ladder.md)<!-- link:end -->：画面で確かめさせるのは、この階段の「確かめる手段を渡す」段の一つである。完了の確かめ全体のどこに置くかを決める。
- <!-- link:begin evidence-not-reports -->[報告ではなく証拠を求める](evidence-not-reports.md)<!-- link:end -->：何を証拠として受け取るかの原則。画面の確認では、証拠はスクリーンショットと操作の記録になる。
- <!-- link:begin browser-control -->[Claude in Chrome と computer use（ブラウザと画面の操作）](../surfaces/browser-control.md)<!-- link:end -->：ブラウザや画面の操作そのものの選び方。このページは、その道具を確かめに使う場面を扱う。
- <!-- link:begin claims-done-but-isnt -->[「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)<!-- link:end -->：「完了」と言うが終わっていない症状から入る入口。画面で確かめさせる前に、原因の切り分けに使う。

古くなった助言の台帳に、このページに関わる行はない。

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [報告ではなく証拠を求める](evidence-not-reports.md)

**次に読む**

- フロントエンドのデザイン（準備中）

**関連**

- [Claude in Chrome と computer use（ブラウザと画面の操作）](../surfaces/browser-control.md)
- [画像・スクリーンショット・音声で渡す](../prompting/images-and-voice.md)
- [検証の階段](verification-ladder.md)
- [ブラウザや画面の操作を任せるときの注意](../safety/browser-agent-cautions.md)
- [見た目は品質の証拠ではない](looks-are-not-quality.md)
- 資料・スライドを作る（準備中）
- [「完了」と言うが終わっていない](../symptoms/claims-done-but-isnt.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Commands](https://code.claude.com/docs/en/commands)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Code with Chrome](https://code.claude.com/docs/en/chrome)：Anthropic・英語・確認日 2026-11-04
- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->
