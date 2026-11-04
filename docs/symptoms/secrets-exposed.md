---
id: secrets-exposed
title: 秘密の情報を読まれた・外に出された
nav_title: 秘密を読まれた・出された
aliases: [.env を読まれた, API キーの流出, 秘密をコミットされた]
type: symptom
field: symptoms
chapter: 安全と承認
order: 290
level: 使う
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 握る]
prevents: [縛っていない, 境界がない]
pitfalls: []
scenes: [開発, チーム]
summary: 秘密（.env・API キー）を読まれた・会話や履歴に出たときに、まず鍵を無効にし、どの境界が欠けていたかを切り分けて、読ませない縛りを決める。
signs:
  - {type: symptom, text: .env の中身を読まれて会話に出された}
  - {type: symptom, text: API キーを含むファイルをコミットされた}
  - {type: symptom, text: 秘密の値がログや出力に残っている}
  - {type: symptom, text: 会話に API キーを貼ってしまった}
wave: 1
prerequisites: [where-your-data-goes]
related: [what-feedback-sends, shared-artifacts-and-files, block-with-exit-2, hook-recipes, what-auto-mode-stops, vetting-extensions, before-opening-unknown-repos, postmortems, followed-injected-instructions, deleted-something-important, six-causes]
routes:
  - {cause: 縛っていない, to: [protecting-secrets, permission-rules]}
  - {cause: 境界がない, to: [sandboxing, lethal-trifecta]}
tracks: [permissions, sandbox, hooks]
outdated_advice: []
sources: [cc-docs-best-practices, cc-docs-data-usage, cc-docs-permissions, cc-docs-sandboxing, cc-docs-security]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: まず鍵を無効にする, anchor: first-response}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: example}
  - {title: 予防（仕組みに移す）, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：秘密が読まれた・出たら、先にキーを無効にし、縛りの欠けを安く切り分けて、直す先を決められる。
    - **いつ引くか**：`.env` の中身を会話に出された、キーを含むファイルをコミットされた、ログや出力に値が残った、会話に API キーを貼ってしまったとき。
    - **前提**：<!-- link:begin where-your-data-goes -->[送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)<!-- link:end -->

<!-- textlint-disable -->
別名：.env を読まれた・API キーの流出・秘密をコミットされた
<!-- textlint-enable -->

このページは、API キーや `.env` の値などの秘密が、Claude に読まれたり、会話や履歴に出たりしたときの入口である。調べる前にやることと、どの縛りが欠けていたかを切り分ける順を持つ。直し方の本体は、振り分け先のページに任せる。

## よくある形 {#forms}

秘密が出る形は 4 つある。どの形かで、写しが残る場所と、見る所が変わる。

- **読まれた**：Claude が `.env` などを読み、中身が会話に出た。値は会話の一部として送られ、手元の記録にも残る。
- **コミットされた**：キーを含むファイルが履歴に入った。push していれば、手元だけの話ではない。
- **出力に残った**：コマンドの出力やログファイルに、値がそのまま出た。
- **自分で貼った**：会話に API キーを貼った。Claude の縛りが破れたのではなく、秘密の置き方の問題である。

## まず鍵を無効にする {#first-response}

秘密が会話・履歴・出力のどれかに出たら、原因を調べる前に、発行元でキーを無効にする。ここでの鍵は、API キーやトークンなどの認証情報のことである。値が出た時点で、写しがどこに残ったかを全部は追えない。だから、読まれたかどうかではなく、出たかどうかで決める。自分で貼ったキーも同じ扱いにする。

1. 発行元の管理画面で、キーを失効させ、新しいキーを発行する。
2. 発行元の利用ログで、身に覚えのない使われ方がないかを見る。
3. 写しが残る場所を洗う。会話は手元の記録に平文で残る。詳しくは <!-- link:begin where-your-data-goes#local-transcripts -->[送ったデータの行方（学習・保持期間） › 手元に残る記録](../safety/where-your-data-goes.md#local-transcripts)<!-- link:end --> を見る。
4. コミットされたなら、履歴から消す書き換えは、キーを無効にした後の掃除として行う。書き換えはキーの無効化の代わりにならない。GitHub の文書も、まずキーを無効にするか交換するよう書き、履歴を書き換えて強制 push しただけでは、機密を含むコミットがほかの所から見えることがあると警告している（2026-11-05 に確認）。
5. `/feedback` やトランスクリプトの共有で会話を送っていたら、送った中身と残る期間を <!-- link:begin what-feedback-sends#what-is-sent -->/feedback・トランスクリプトの共有で送られるもの › 送られるものと残る期間（準備中）<!-- link:end --> で確かめる。会話を共有リンクにしていたら、<!-- link:begin shared-artifacts-and-files#revoke -->共有リンクと公開アーティファクトの扱い › 取り消せるもの・取り消せないもの（準備中）<!-- link:end --> で取り消せるかを確かめる。
6. 新しいキーは、置き場所と縛りを決めてから使う。前と同じ状態に置けば、同じことが繰り返される。次の節で、欠けていた縛りを探す。

## 原因を安く確かめる順 {#diagnosis}

キーを無効にしたら、なぜ出たかを確かめる。Claude 側の 6 つの原因のうち、秘密の流出に関わるのは「縛っていない」と「境界がない」である。確かめる順は <!-- link:begin six-causes#diagnosis -->[失敗の二つの軸と診断の入口 › 安く確かめられる順の診断](../start/six-causes.md#diagnosis)<!-- link:end --> と同じく、手間の小さいものからにする。

1. **出どころを見る**：会話の記録で、値が最初に出た場面を探す。自分が貼ったなら、Claude 側の欠けではないので、置き方を <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> で直す。ファイルの読み取りなら次へ進む。値がファイルでなく、環境変数や実行結果から出ていないかも見る。ファイルの deny では塞がらない経路だからである。
2. **縛っていない（読ませない規則があったか）**：CLAUDE.md の「`.env` を読まない」という行だけだったか、権限ルールの deny があったかを見る。設定ファイルと `/permissions` で確かめられる。公式は、この種の行は「ほぼ毎回」守られるが、足りないなら deny などの仕組みに移すよう勧める。deny があるのに読まれたなら、パスが当たっているかを <!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end --> で確かめる。コミットの形なら、`git add` を許す規則と、秘密のファイルを除く `.gitignore` の有無も見る（一般の実務の観点で、公式の文書の記述ではない）。
3. **境界がない（権限ルールの外の経路があったか）**：deny が効くのは、組み込みのファイルの道具と、Claude Code が見分けられるファイルのコマンドである。`grep -r` と、自分でファイルを開くスクリプトには効かない。値を出した道具やコマンドを特定し、<!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end --> と照らす。次に、サンドボックスを有効にしていたか、秘密の場所を読み取り拒否に入れていたかを見る。読み取りの範囲は既定で広いので、明示して塞ぐ。詳しくは <!-- link:begin sandboxing#default-reads -->[サンドボックスで封じ込める › 読み取りは既定で広い](../enforce/sandboxing.md#default-reads)<!-- link:end --> を見る。ただし、サンドボックスが囲うのはコマンドの側で、Claude のファイルの道具は囲わない。囲える範囲は <!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end --> を見る。
4. **境界がない（入力の側）**：読ませたのが自分の頼みでなく、読んだページ・ファイル・リポジトリに書かれた指示ではなかったかを見る。値が出る直前に、頼んでいない読み取りや外への送信がなかったかを記録で確かめる。該当すれば <!-- link:begin followed-injected-instructions#diagnosis -->[読ませたページやファイルの指示に従ってしまった › 原因を安く確かめる順](followed-injected-instructions.md#diagnosis)<!-- link:end --> へ進む。信頼できない入力・秘密・外への送信が 1 つの構成に揃っていたら、<!-- link:begin lethal-trifecta#three-capabilities -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つの能力](../safety/lethal-trifecta.md#three-capabilities)<!-- link:end --> の形である。
5. **人の側**：確認の画面を読まずに許可していなかったか。auto モードに任せていたなら、止めないものがあるので、<!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end --> を見る。人の側の落とし穴は <!-- link:begin six-causes#human-side -->[失敗の二つの軸と診断の入口 › 人の側の五つの落とし穴](../start/six-causes.md#human-side)<!-- link:end --> にある。

秘密を読んだり書いたりする操作では、原因が 1 つとは限らない。deny はあったが、サンドボックスがなかった、という重なりが多い。見つけた欠けは、次の表の先で直す。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 縛っていない | [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)<br>[権限ルール（allow・ask・deny）](../enforce/permission-rules.md) |
| 境界がない | [サンドボックスで封じ込める](../enforce/sandboxing.md)<br>[三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#example}

!!! example "判断例：deny があるのに、実行結果にキーが出た"
    - **状況**：プロジェクトの `.env` に deny ルールを入れていた。それでも、Claude がテスト用のスクリプトを動かした出力に、API キーの値が出た。
    - **迷う候補**：deny のパスの書き方を直す。あるいは、サンドボックスで読み取りを塞ぐ。
    - **選んだもの**：先に発行元でキーを無効にした。その後、サンドボックスの読み取り拒否に `.env` を足し、deny のパスも見直した。
    - **理由**：スクリプトが自分でファイルを開くと、deny は効かない。パスを直しても、この経路は残る。OS の層で塞げば、その子プロセスも止まる。足した後は、偽の値を入れたファイルで、スクリプトからの読み取りが止まることを確かめた。

## 予防（仕組みに移す） {#prevention}

「読まないで」と頼む文は、お願いであって、仕組みによる強制ではない。例外を許さないものは、会話の外で効く仕組みに移す。面によって手段が違う。

=== "アプリ"

    - 秘密を会話や添付に置かない。置き方は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> で決める。
    - 権限ルールとサンドボックスは Claude Code の仕組みである。アプリでの同等の設定は未確認である。

=== "Claude Code"

    - 読ませない設定を、権限ルールとサンドボックスの 2 つにする。作り方は <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> にある。
    - 特定の操作を止めて理由を返すなら、<!-- link:begin block-with-exit-2 -->[フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)<!-- link:end --> を使う。型は <!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](../enforce/hook-recipes.md#block-dangerous)<!-- link:end --> にある。
    - 3 つ（信頼できない入力・秘密・外への送信）が要る作業は、<!-- link:begin lethal-trifecta#when-all-three -->[三つを同時に持たせない（lethal trifecta と Rule of Two） › 三つとも要るとき](../safety/lethal-trifecta.md#when-all-three)<!-- link:end --> で人の承認を挟む。

任せる幅を広げる前に、この縛りを先に置く。出たものを仕組みの隙間として記録し、再発防止をどこに入れるかは <!-- link:begin postmortems#where-to-put-fixes -->失敗を仕組みに戻す（ポストモーテム） › 再発防止をどこに入れるか（準備中）<!-- link:end --> で決める。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Data usage](https://code.claude.com/docs/en/data-usage)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Security](https://code.claude.com/docs/en/security)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [送ったデータの行方（学習・保持期間）](../safety/where-your-data-goes.md)

**次に読む**

- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [三つを同時に持たせない（lethal trifecta と Rule of Two）](../safety/lethal-trifecta.md)

**関連**

- /feedback・トランスクリプトの共有で送られるもの（準備中）
- 共有リンクと公開アーティファクトの扱い（準備中）
- [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [知らないリポジトリを開く前に](../safety/before-opening-unknown-repos.md)
- 失敗を仕組みに戻す（ポストモーテム）（準備中）
- [読ませたページやファイルの指示に従ってしまった](followed-injected-instructions.md)
- [消してはいけないものを消された](deleted-something-important.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
