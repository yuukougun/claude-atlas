---
id: browser-agent-cautions
title: ブラウザや画面の操作を任せるときの注意
aliases: [Claude in Chrome の注意, Computer use の注意, ブラウザ操作の安全, Chrome・computer use・ブラウザでの注意]
type: concept
field: safety
chapter: 悪意ある入力
order: 130
level: 整える
priority: 推奨
surfaces: [app, claude-code]
principle: [縛る]
prevents: [境界がない]
pitfalls: []
scenes: [開発, 調べもの]
summary: ブラウザや画面の操作を Claude に任せるとき、ログイン済みのサイトや開いているアプリまで届くことを踏まえて、任せる範囲を決められる。機微な情報に触れる作業には使わない。
signs:
  - {type: situation, text: Claude in Chrome で作業を任せようとしている}
  - {type: goal, text: 画面の操作を任せても大丈夫な作業を見分けたい}
prerequisites: [prompt-injection-in-practice]
related: [browser-control, lethal-trifecta, visual-checks, default-safety-settings]
tracks: [claude-in-chrome, computer-use]
sources: [cc-docs-chrome, hc-claude-in-chrome, hc-computer-use, hc-cowork-safety, claude-for-chrome-blog]
volatility: 高
sections:
  - {title: 届く範囲（ログイン済みのサイト・開いているアプリ）, anchor: reach}
  - {title: 起きること（読んだ画面の指示で動く）, anchor: what-happens}
  - {title: 何に効くか（縛るで境界のなさを補う）, anchor: what-it-prevents}
  - {title: 任せない作業, anchor: what-not-to-do}
  - {title: よくある誤解, anchor: misconceptions}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何が分かるか**：ブラウザや画面の操作を任せると、Claude の手がログイン済みのサイトや開いているアプリまで届くと分かり、任せる範囲を決められる。
    - **いつ引くか**：Claude in Chrome や computer use で作業を任せようとしていて、どこまで任せてよいか見分けたいとき。
    - **前提**：<!-- link:begin prompt-injection-in-practice -->[プロンプトインジェクションの実際](prompt-injection-in-practice.md)<!-- link:end -->

<!-- textlint-disable -->
別名：Claude in Chrome の注意・Computer use の注意・ブラウザ操作の安全・Chrome・computer use・ブラウザでの注意
<!-- textlint-enable -->

ブラウザや画面の操作を任せるときの注意とは、Claude に画面の操作を渡すと、会話の中だけで済んでいた失敗が、自分の名前で動くアカウントやアプリに及ぶという話である。使い方は <!-- link:begin browser-control -->[Claude in Chrome と computer use（ブラウザと画面の操作）](../surfaces/browser-control.md)<!-- link:end --> に任せ、このページは「どこまで任せるか」の判断だけを持つ。

## 届く範囲（ログイン済みのサイト・開いているアプリ） {#reach}

画面の操作を任せたとき、Claude が届く先は、自分がその画面で届く先とほぼ同じになる。会話だけのチャットでは、Claude が触れるのは貼った文章とファイルだった。画面の操作では、触れる先が画面の向こうへ広がる。

- Claude in Chrome：Chrome の拡張で、Claude が Web サイトを読み、クリックし、移動する。自分のブラウザで動くので、自分がログインしているサイトの画面は、Claude からも見えて操作できる（推論。公式の説明は操作の内容を述べ、ログインの扱いは述べていない）
- computer use：使えるコネクタや道具がないときに、Claude が画面を直接クリックし、入力する。届く先は、画面に開いているアプリである。公式は、Claude とアプリの間にサンドボックスはないと述べている

> Computer use has no sandbox between Claude and your applications
> （出典：Let Claude use your computer in Cowork）

使う順は、コネクタ、ブラウザ、画面の順である。届く範囲が狭い手段を先に選び、画面の操作は最後に回す。手段の選び方は <!-- link:begin browser-control#which-to-use -->[Claude in Chrome と computer use（ブラウザと画面の操作） › コネクタ・ブラウザ・画面の順に選ぶ](../surfaces/browser-control.md#which-to-use)<!-- link:end --> にある。

届く範囲を狭める手がかりは、公式の側にもある。computer use はアプリごとに許可を求める。投資・トレード・暗号資産のアプリは、既定でブロックされる。銀行・医療・行政のアプリは、オフにしておくよう公式が勧めている。既定の細部は版で変わるので、使う面の公式の説明で確かめる。

## 起きること（読んだ画面の指示で動く） {#what-happens}

画面の操作を任せると、Claude は開いたページやメールの中身を読んで次の行動を決める。その中身に仕込まれた指示にも、従ってしまうことがある。仕組みの全体は <!-- link:begin prompt-injection-in-practice#channels -->[プロンプトインジェクションの実際 › 指示が入ってくる経路](prompt-injection-in-practice.md#channels)<!-- link:end --> にあり、ここでは画面の操作ならではの点だけを書く。

- 読む先が広い：Web ページ、メール、チャットの画面のどれも、書き手が自分とは限らない
- 動ける先が広い：ログイン済みのサイトでは、送信・購入・削除のような取り消しにくい操作に手が届く

公式の Cowork の安全指針は、prompt injection が成り立つ条件を 2 つ挙げている。信頼境界の外の情報を読めることと、被害につながる行動ができることの両方がそろったときである。片方を外せば、攻撃は難しくなる。この 2 つに、秘密や私的なデータへの到達が加わった組を <!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](lethal-trifecta.md#three-capabilities)<!-- link:end --> が扱っている。ログイン済みのブラウザは、この 3 つがそろいやすい。

Anthropic は 2025-08 の research preview の時点で、Chrome 拡張の攻撃試験の結果を公開している。29 の攻撃シナリオ、123 件のテストで、緩和策がないときの攻撃の成功率は 23.6%、緩和策を入れた自律モードで 11.2% だった。ブラウザ特有の攻撃 4 種（ページに隠したフォームなど）の成功率は、35.7% から 0% に下がった（根拠：中）。対象は当時の初期版で、公開文書は対象のモデルを名指ししていない。現行版の数値は確かめていない。緩和策を入れても 0 にはならなかった、という読み方が実務に近い。

!!! example "判断例：どこまで画面の操作を任せるか"
    - **状況**：自作の Web アプリの画面崩れを確かめたい。同じ週に、経費精算サイトへのログインと入力も任せたくなった。
    - **迷う候補**：両方を同じブラウザで続けて任せる。確認だけを任せて、経費精算は自分で行う。
    - **選んだもの**：画面崩れの確認だけを任せ、経費精算は自分で行う。
    - **理由**：画面崩れの確認は、自分が作った画面を見るだけで、読む先が信頼できる。経費精算は、ログイン済みの口座に近い所で、送信という取り消しにくい操作がある。両方を同じブラウザで任せると、読む先と動ける先が混ざる。

## 何に効くか（縛るで境界のなさを補う） {#what-it-prevents}

このページの判断は、原理の「縛る」で、原因の「境界がない」を補うものである。ログイン済みのブラウザや開いているアプリには、Claude と自分の持ち物を分ける境界が、もともとない。だから、お願いや注意で済ませずに、届く先そのものを縛る。

- 作業用の Chrome のプロファイルや、別のユーザーを用意し、任せる作業に要るサイトだけにログインしておく（推論・実践例なし。公式の指針は専用の作業フォルダを勧めており、それを画面に当てはめた案）
- computer use のアプリごとの許可は、作業に要るアプリだけに出す
- 低リスクの作業から始める。バックアップを取る。送信や購入のような取り消しにくい操作を、定期実行の作業にしない

アプリごとの許可は computer use の公式の説明、低リスクから始める・バックアップ・定期実行の注意は Cowork の安全指針の項目である。ただし、縛りが効くのは届く先までで、読んだ内容に従うかどうかは縛れない。そこは <!-- link:begin prompt-injection-in-practice#what-works -->[プロンプトインジェクションの実際 › 防ぐ手立ては権限と通信の側にある](prompt-injection-in-practice.md#what-works)<!-- link:end --> のとおり、権限と通信の組み合わせで抑える。面ごとの既定と、段階ごとに足す設定は、<!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](default-safety-settings.md#by-stage)<!-- link:end --> を正とする。3 つとも要る作業は、人の承認を挟む（<!-- link:begin lethal-trifecta#when-all-three -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つとも要るとき](lethal-trifecta.md#when-all-three)<!-- link:end -->）。

## 任せない作業 {#what-not-to-do}

次の作業は、画面の操作を任せない。

- 機微な情報を扱う作業：公式は、Claude in Chrome が安全分類器で強化されていても、機微な情報の扱いに使うことを強く勧めないと述べている。公式のブログは、金融・法律・医療などの機微な情報が絡むサイトを避けるよう書いている。
- 銀行・医療・行政のアプリを開く作業：computer use では、これらのアプリをオフにしておくのが公式の勧めである。
- 送信・購入・削除のような、取り消しにくい操作：一度の操作で済み、巻き戻せない。
- 知らない送り主のメールやページを、続けて読ませる作業：読んだ中身が、指示を仕込まれる経路になる。

任せてよいかの目安は、読む先が自分の管理下にあるか、動いた結果を自分が確かめられるか、の 2 点である。自作の画面を見て確かめる作業は、この 2 点を満たしやすい。確かめ方は <!-- link:begin visual-checks#as-a-user -->[画面で確かめる（ブラウザ・スクリーンショット・/verify） › 人のユーザーとして確かめさせる](../verify/visual-checks.md#as-a-user)<!-- link:end --> にある。

任せない作業でも、Claude に手伝わせる道は残る。画面を渡さずに、必要な文章やファイルだけを貼って相談する。その作業用のコネクタがあれば、画面の操作より先にそれを使う。

## よくある誤解 {#misconceptions}

- 「安全分類器が入っているから、機微な作業も任せられる」：公式は、強化されていてもまだ危険があると述べている。分類器は届く範囲を狭めない。
- 「自分のパソコンの中だから、外には出ない」：画面の操作で動くのは、自分のログインで届く先すべてである。外へ送る操作も、画面からできる。
- 「見張っていれば防げる」：ページに隠した指示は、画面を眺めるだけでは見えないことがある。Anthropic の攻撃試験にも、ページに隠したフォームを使う攻撃が含まれていた。取り消しにくい操作は、任せる前に除くほうが確かである。
- 「Claude in Chrome と computer use は同じ注意で済む」：届く先が違う。前者はブラウザの中、後者は開いているアプリである。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Use Claude Code with Chrome](https://code.claude.com/docs/en/chrome)：Anthropic・英語・確認日 2026-11-04
- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)：Anthropic・英語・確認日 2026-11-04
- [Let Claude use your computer in Cowork](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)：Anthropic・英語・確認日 2026-11-04
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)：Anthropic・英語・確認日 2026-11-04
- [Piloting Claude for Chrome](https://claude.com/blog/claude-for-chrome)：Anthropic・英語・確認日 2026-11-05

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [プロンプトインジェクションの実際](prompt-injection-in-practice.md)

**関連**

- [Claude in Chrome と computer use（ブラウザと画面の操作）](../surfaces/browser-control.md)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](lethal-trifecta.md)
- [画面で確かめる（ブラウザ・スクリーンショット・/verify）](../verify/visual-checks.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](default-safety-settings.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
