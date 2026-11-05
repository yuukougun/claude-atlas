---
id: isolate-with-safe-mode
title: 設定を外して切り分ける（--safe-mode）
aliases: [--safe-mode, 拡張なしで起動する, 自分の設定のせいか確かめる, Debug your configuration]
type: feature
field: cli
chapter: 見る・切り分ける
order: 110
level: 任せる
priority: 推奨
surfaces: [claude-code]
principle: [確かめる]
prevents: [散らかっている, 合っていない]
pitfalls: []
scenes: [開発]
summary: CLAUDE.md・スキル・フック・MCP などを読まずに起動し、同じ依頼で挙動を比べて不調の原因を切り分ける。認証と管理の設定は効いたままで、自分の deny ルールは外れる。
signs:
  - {type: goal, text: おかしな挙動が、自分の設定や拡張のせいか確かめたい}
  - {type: situation, text: 拡張を入れてから急に挙動が変わった}
prerequisites: [settings-layers]
related: [seems-less-capable, instructions-ignored, replies-in-english, blames-the-tools, suspected-degradation, pruning-extensions, felt-vs-measured, usage-context-statusline]
tracks: [safe-mode]
outdated_advice: []
sources: [cc-docs-cli-reference, cc-docs-debug-your-config, cc-docs-errors, cc-changelog]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 外れるもの・残るもの, anchor: what-is-disabled}
  - {title: 最小の使い方, anchor: usage}
  - {title: 比べ方, anchor: compare}
  - {title: 雛形, anchor: templates}
  - {title: 効かない場面・落とし穴, anchor: limits}
  - {title: ほかの切り分けとの違い, anchor: alternatives}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：CLAUDE.md・スキル・プラグイン・フック・MCP などを読まずに起動し、同じ依頼で挙動を比べて、不調が自分の設定から来るかを切り分けられる。
    - **いつ引くか**：おかしな挙動が、自分の設定や拡張のせいか確かめたいとき。拡張を入れてから急に挙動が変わったとき。
    - **止められるもの**：読み込みを止めるだけである。認証・モデルの選択・組み込みの道具・権限は通常どおり働き、管理の方針も効く。安全の設定を外す道具ではない。
    - **前提**：<!-- link:begin settings-layers -->[設定ファイルの階層と優先順位](settings-layers.md)<!-- link:end -->

<!-- textlint-disable -->
別名：--safe-mode・拡張なしで起動する・自分の設定のせいか確かめる・Debug your configuration
<!-- textlint-enable -->

`--safe-mode` は、自分で入れた設定と拡張を読まずに Claude Code を起動するオプションである。このページは、不調の原因が自分の設定にあるのかを、このオプションで切り分ける手順と、その限界を扱う。入った版と成熟度は、ページ上部のバッジで確かめる。

## 使いどころ {#when}

CLAUDE.md・スキル・フック・MCP を足していくと、挙動の変化が設定のせいなのか、モデルや版のせいなのかを見分けにくくなる。設定が散らかっているか、今の使い方に合っていないと、指示が守られない、遅い、英語で返るといった形で表に出る。`--safe-mode` は、その設定をまとめて外した状態を作り、原因の候補を「設定の中」と「設定の外」に二分する。

引く場面は 2 つある。

- 拡張を入れた直後に、急に挙動が変わった。
- 指示が守られない、賢くなくなった気がする、といった症状の診断で、設定を疑う段に来た。

症状ごとの診断の順番は、それぞれのページが持つ。このページは、設定を外して比べる操作の側を持つ。

- 指示が守られない：<!-- link:begin instructions-ignored#diagnosis -->[CLAUDE.md や指示が守られない › 原因を安く確かめる順](../symptoms/instructions-ignored.md#diagnosis)<!-- link:end -->
- 急に賢くなくなった気がする：<!-- link:begin seems-less-capable#diagnosis -->[急に賢くなくなった気がする › 原因を安く確かめる順](../symptoms/seems-less-capable.md#diagnosis)<!-- link:end -->
- 英語で返ってくる：<!-- link:begin replies-in-english#diagnosis -->[英語で返ってくる › 原因を安く確かめる順](../symptoms/replies-in-english.md#diagnosis)<!-- link:end -->
- 環境や道具が壊れたと言い出す：<!-- link:begin blames-the-tools#diagnosis -->[環境や道具が壊れたと言い出す › 原因を安く確かめる順](../symptoms/blames-the-tools.md#diagnosis)<!-- link:end -->

依頼が断られたときにも使える。推論の全文を決まった形で出させる指示のような、断られる引き金になる文が、CLAUDE.md・スキル・出力スタイル・MCP の道具の説明に入っていることがある。公式も、そうした指示を探して外すときに `--safe-mode` で設定を外して切り分けられると案内している。目的は、設定に入った引き金を見つけて外すことであり、判定を避けることではない。

## 外れるもの・残るもの {#what-is-disabled}

`--safe-mode` で止まるのは、自分で足した設定と拡張である。残るのは、Claude Code が動くのに要るものと、組織が決めた方針である。

| 区分 | 内容 |
| --- | --- |
| 外れる | CLAUDE.md、スキル、プラグイン、フック、MCP サーバー、自作のコマンドとエージェント、出力スタイル、キー割り当て、ステータスライン、LSP、自動メモリ |
| 残る | 認証、モデルの選択、組み込みの道具、権限 |
| 管理の方針 | 管理のフックと設定の方針は効く。管理が配ったプラグイン・スキル・CLAUDE.md・MCP サーバーは外れる |

自分で入れた mod も止まる。組み込みの mod は止まらない。

認証が通常どおり使えるので、サブスクリプションのログインのまま起動できる。この点が、API キーの扱いを変える `--bare` との違いである。

権限が残るとは、操作ごとの確認という仕組みが残る意味である。`--safe-mode` は「設定を白紙にして何でもできる状態」を作らない。ただし、自分の設定ファイルに書いた `allow`・`deny` ルールとフックは外れる。プロジェクトで禁止していた操作が、この起動では自分のルールの守りなしになる。管理の設定に書かれたルールは効く。権限の層の読み方は <!-- link:begin settings-layers#layers -->[設定ファイルの階層と優先順位 › 層と優先順位](settings-layers.md#layers)<!-- link:end --> にある。

## 最小の使い方 {#usage}

起動は、普段の `claude` に `--safe-mode` を付けるだけである。不調が出たプロジェクトのフォルダで実行する。

```bash
claude --safe-mode
```

起動したら、不調が出たときと同じ依頼を出す。外れているかは `/context` で確かめられる。自分の CLAUDE.md やスキルが一覧に出ていなければ、外れている。

結果の読み方は 2 通りである。

- 不調が消えた：外れた設定のどれかが原因の候補になる。次に、どれが原因かを 1 つずつ絞る。
- 不調が残った：原因は自分の設定の外にある。モデル・版・依頼の書き方・会話の長さを疑う。

消えたときの絞り込みは、外れたものを分けて確かめる。読み込まれているかを見るコマンドは、公式が次のように案内している。

| 疑うもの | 見るコマンド |
| --- | --- |
| CLAUDE.md・全体の占有 | `/context`、`/memory` |
| スキル | `/skills` |
| フック | `/hooks` |
| MCP サーバー | `/mcp` |
| 設定ファイルの壊れ・使っていない拡張 | `/doctor` |
| 効いている層・管理の設定 | `/status` |

1 つずつ戻して再現するのは、手間がかかる。常駐しているものが多いほど、戻す回数も増える。使っていない拡張を外す棚卸しは <!-- link:begin pruning-extensions#measure -->[拡張の棚卸しと剪定 › 測る](../extend/pruning-extensions.md#measure)<!-- link:end --> が持つ。

## 比べ方 {#compare}

`--safe-mode` の結果だけを見て、直ったと決めるのは危ない。返答は毎回少し違い、会話の長さや依頼の言い方でも変わる。設定のせいかを確かめるには、条件を揃えて 2 つの起動を比べる。

1. 比べる依頼を 1 つ決め、文面を書き写して、毎回そのまま貼る。
2. 通常の起動と `--safe-mode` の起動で、どちらも新しい会話から始める。
3. 同じフォルダで、同じ版のまま流す。版は先に控える。
4. 返答がばらつくなら、各側で 2〜3 回ずつ流す。
5. 通常の起動では `/context` も保存する。何が常駐していたかの記録になる。

手順の写しは、雛形の節に置く。

!!! example "判断例：拡張を入れてから返答が変わった"
    - **状況**：フックとスキルを足した翌日から、コミットメッセージが指定の書式にならなくなった。
    - **迷う候補**：モデルの調子が落ちたとみて、しばらく様子を見る。または、足した拡張を疑って外して比べる。
    - **選んだもの**：同じ依頼を通常の起動と `--safe-mode` で 3 回ずつ流して比べる。
    - **理由**：どちらの見立ても筋が通るが、切り分けの費用が低いのは比べるほうである。`--safe-mode` で 3 回とも書式が守られ、通常の起動では守られなければ、外れた設定の中に原因がある。両方で崩れるなら、設定の外を疑う。

体感だけで「直った」「悪化した」と決めない考え方は <!-- link:begin felt-vs-measured#evidence -->[体感と実測 › 何が起きるか（研究と根拠の強さ）](../eval/felt-vs-measured.md#evidence)<!-- link:end --> にある。版と effort を記録して同じ課題で繰り返し比べる手順は <!-- link:begin suspected-degradation#measure -->[劣化を疑ったら測って確かめる › 版と effort を記録して、同じ課題で比べる](../models/suspected-degradation.md#measure)<!-- link:end --> にある。

## 雛形 {#templates}

比べる手順の写しと、`--safe-mode` でも不調が残るときに使う、空の設定フォルダで起動するスクリプトを置く。どちらも自分の環境で動作を確かめてから使う。

<!-- gen:begin snippet isolate-with-safe-mode/compare-steps -->
<!-- textlint-disable -->

??? example "雛形：同じ依頼を通常の起動と --safe-mode で比べる手順"

    ```markdown
    ## --safe-mode と通常の起動で同じ依頼を比べる手順

    準備
    - 不調が出たプロジェクトのフォルダで作業する（フォルダを替えない）
    - 比べる依頼を 1 つ決めて、文面をメモに書き写す（毎回この文面をそのまま貼る）
    - `claude --version` の出力を控える

    通常の起動
    1. `claude` で新しい会話を始める
    2. メモの依頼を貼って、返答を保存する
    3. `/context` の出力も保存する（CLAUDE.md・スキル・MCP が何を占めているかの記録になる）

    --safe-mode の起動
    4. いったん終了して、`claude --safe-mode` で新しい会話を始める
    5. 同じ文面の依頼を貼って、返答を保存する

    読み取り
    - 2 と 5 を見比べる。返答にばらつきがあるなら、各側で 2〜3 回ずつ流す
    - 不調が safe mode で消えた：外れた設定のどれかが原因の候補になる
    - 不調が safe mode でも残った：自分の設定の外（モデル・版・依頼の書き方・会話の長さ）を疑う
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.169。

<!-- textlint-enable -->
<!-- gen:end snippet isolate-with-safe-mode/compare-steps -->

<!-- gen:begin snippet isolate-with-safe-mode/clean-config -->
<!-- textlint-disable -->

??? example "雛形：空の設定フォルダで起動するスクリプト"

    ```bash
    #!/usr/bin/env bash
    # 自分の設定を何も持たない状態で Claude Code を起動する（--safe-mode でも不調が残るときの次の手）
    # 実行前に、動いている Claude Code のセッションを閉じる

    mkdir -p ~/claude-clean/empty
    cd ~/claude-clean/empty || exit 1

    # 新しい設定フォルダを使い、プロジェクトの設定（.claude/settings.json・CLAUDE.md・.mcp.json）を読まない
    # 初回の設定画面とログインがもう一度出る。それが新しい設定フォルダが効いている印
    CLAUDE_CONFIG_DIR=~/claude-clean/config claude --setting-sources user
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.1.169。

<!-- textlint-enable -->
<!-- gen:end snippet isolate-with-safe-mode/clean-config -->

## 効かない場面・落とし穴 {#limits}

`--safe-mode` が答えられるのは、「自分の設定と拡張を外すと変わるか」だけである。次の点で読み違えやすい。

- **雛形そのものの確認には使えない**：プロジェクトのフックも止まるので、フックや設定の雛形が動くかは、この起動では確かめられない。
- **設定の外の原因は分からない**：不調が残ったとき、分かるのは「自分の設定のせいではなさそうだ」までである。モデル・版・依頼のどれかは、別に切り分ける。
- **管理の方針は外れない**：組織が配った設定のせいなら、不調は残る。`/status` で管理の設定が効いているかを見る。
- **守りも外れる**：自分の `deny` ルールやフックも止まる。安全の設定を外す近道として使わない。外した状態で危険な操作をさせない。
- **シェルの環境変数は別**：環境変数が `--safe-mode` で無視されるかは、公式の文書で確かめていない。外れたと決めつけず、環境変数は別に確かめる。
- **古い版では使えない**：入った版より前の Claude Code にはこのオプションがない。手元の版は `claude --version` で確かめる。
- **WSL・Linux の CLI を基準にした記述である**：ほかの OS と IDE 拡張での動作は未確認である。

## ほかの切り分けとの違い {#alternatives}

`--safe-mode` で原因が分からないとき、またはもっと細かく分けたいときに使う手段がある。公式の「Debug your configuration」は、まず `--safe-mode`、それで足りなければ空の設定フォルダでの起動を勧めている。

| 手段 | 外れるもの | 使いどころ |
| --- | --- | --- |
| `--safe-mode` | 自分の設定と拡張をまとめて | 最初の二分 |
| `--setting-sources` | 読む源（`user`・`project`・`local`）を選んで | どの層が原因かを層で絞る |
| 新しい `CLAUDE_CONFIG_DIR` | 設定フォルダごと（`~/.claude` と認証情報の入れ物も別になる） | 自分の設定ファイルそのものが壊れている疑い |

`--setting-sources` だけでは、管理の設定、`~/.claude.json`、自動メモリ、claude.ai の MCP コネクタは外れない。古い版には、外した源の設定が一部漏れる不具合があった。直った版は、更新履歴で確かめる。

新しい `CLAUDE_CONFIG_DIR` を使うと、初回の設定とログインをやり直す。この手順は雛形の `clean-config` にまとめた。その結果の読み方は次のとおりである。

- 不調が消えた：原因は自分のユーザーまたはプロジェクトの設定にある。`~/.claude.json` と `~/.claude` の中身を、新しいフォルダへ 1 つずつ戻して、再現するものを探す。
- 不調が残った：原因は自分の設定の外にある。`/status` で管理の設定を確かめ、シェルの環境変数を見る。

設定ファイルが壊れていると、対話のときはエラーのダイアログが出る。`-p` では、壊れたファイルや値が黙って飛ばされる。何を落としたかは `claude doctor` で見る。

層の優先順位の読み方は <!-- link:begin settings-layers#verify -->[設定ファイルの階層と優先順位 › 効いているかを確かめる](settings-layers.md#verify)<!-- link:end -->、状態を測る道具は <!-- link:begin usage-context-statusline#instruments -->[/usage・/context・ステータスラインで状態を見る › 三つの道具で見えるもの](usage-context-statusline.md#instruments)<!-- link:end --> にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [CLI reference](https://code.claude.com/docs/en/cli-reference)：Anthropic・英語・確認日 2026-11-04
- [Debug your configuration](https://code.claude.com/docs/en/debug-your-config)：Anthropic・英語・確認日 2026-11-04
- [Error reference](https://code.claude.com/docs/en/errors)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [設定ファイルの階層と優先順位](settings-layers.md)

**関連**

- [急に賢くなくなった気がする](../symptoms/seems-less-capable.md)
- [CLAUDE.md や指示が守られない](../symptoms/instructions-ignored.md)
- [英語で返ってくる](../symptoms/replies-in-english.md)
- [環境や道具が壊れたと言い出す](../symptoms/blames-the-tools.md)
- [劣化を疑ったら測って確かめる](../models/suspected-degradation.md)
- [拡張の棚卸しと剪定](../extend/pruning-extensions.md)
- [体感と実測](../eval/felt-vs-measured.md)
- [/usage・/context・ステータスラインで状態を見る](usage-context-statusline.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
