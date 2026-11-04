---
id: parallel-with-worktrees
title: git worktree で並列にする
aliases: [claude -w, --worktree, .worktreeinclude, 並列開発]
type: feature
field: delegate
chapter: 並べる
order: 100
level: 仕組みにする
priority: 必須
surfaces: [claude-code]
principle: [縛る]
prevents: [散らかっている]
pitfalls: []
scenes: [開発]
summary: git worktree で作業ごとに別のチェックアウトを作り、複数のセッションが互いのファイルを上書きせずに並行して進められる。依存の導入や秘密のファイルの写し方は worktree ごとに決める。
signs:
  - {type: goal, text: 同じリポジトリで、複数のセッションを同時に動かしたい}
  - {type: symptom, text: 並列のセッションが、互いのファイルを書き換えてしまう}
prerequisites: [working-with-git]
related: [choosing-parallel-modes, humans-set-the-parallel-limit, compare-hypotheses-in-parallel, agent-view-and-background, batch-and-p-loops, protecting-secrets, sandboxing, checkpoints-and-rewind, resume-and-branch, writing-subagents]
tracks: [worktrees]
sources: [cc-docs-worktrees, cc-changelog, cc-docs-changelog]
volatility: 中
sections:
  - {title: 使いどころ, anchor: when}
  - {title: 最小の使い方, anchor: minimal}
  - {title: worktree ごとの準備（依存・秘密・データベース）, anchor: per-worktree-setup}
  - {title: 片付けと残すもの, anchor: cleanup}
  - {title: 効かない場面・落とし穴, anchor: pitfalls}
  - {title: 比べる相手, anchor: compare}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：作業ごとに別のチェックアウトを作り、複数のセッションが互いのファイルを上書きせずに並行して進められる。
    - **いつ引くか**：同じリポジトリで複数のセッションを同時に動かしたいとき、並列のセッションが互いのファイルを書き換えてしまうとき。
    - **強制力**：<!-- gen:begin feature enforcement -->なし<!-- gen:end feature enforcement -->。作業場所を分けるだけで、ほかのセッションの書き込みを禁じない。分かれるのはファイルの置き場所だけで、データベースやポートなど外の状態は分かれない。
    - **前提**：<!-- link:begin working-with-git -->[git との付き合い方](../cli/working-with-git.md)<!-- link:end -->

<!-- textlint-disable -->
別名：claude -w・--worktree・.worktreeinclude・並列開発
<!-- textlint-enable -->

git worktree は、1 つのリポジトリから、ブランチごとの作業ディレクトリを別々に作る git の機能である。Claude Code は `--worktree`（短縮形 `-w`）でこれを使い、セッションごとに隔離された作業場所を用意する。このページは、使いどころ、最小の使い方、worktree ごとに決める準備、片付け、効かない場面を扱う。

## 使いどころ {#when}

防ぐ原因は「散らかっている」である。同じ作業ディレクトリで複数のセッションを動かすと、同じファイルを同時に書き換え、互いの変更を上書きする。worktree は作業ディレクトリそのものを分けるので、セッション同士がファイルを取り合わない。原理は「縛る」で、並べる場所を物理的に分けて、ぶつかる余地を減らす。

使いどころは次の 3 つである。

- 別々の機能やバグ修正を、同時に進めたい。
- 調査や使い捨ての試作を、本流の作業場所から離して走らせたい。
- 仮説ごとに実装を分けて、あとで比べたい。比べ方は <!-- link:begin compare-hypotheses-in-parallel -->[仮説ごとに並べて、同じ物差しで比べる](compare-hypotheses-in-parallel.md)<!-- link:end --> にある。

本数を増やす前に、守りを先に置く。worktree は並列の入口にすぎず、並べた分だけ結果を確かめる人の手間が増えるからである。本数の決め方は <!-- link:begin humans-set-the-parallel-limit#guards-before-widening -->[並列の上限は人間が決める › 本数を増やす前に置く守り](humans-set-the-parallel-limit.md#guards-before-widening)<!-- link:end --> にある。秘密を写す設定は「worktree ごとの準備」の節で扱い、置き方の原則は <!-- link:begin protecting-secrets#keep-out -->[秘密情報（.env・API キー）を守る › 秘密を作業ディレクトリと会話に置かない](../safety/protecting-secrets.md#keep-out)<!-- link:end --> と <!-- link:begin sandboxing#when -->[サンドボックスで封じ込める › 使いどころ](../enforce/sandboxing.md#when)<!-- link:end --> が持つ。

機能の成熟度は <!-- gen:begin feature worktrees/maturity -->GA<!-- gen:end feature worktrees/maturity --> で、入った版は <!-- gen:begin feature worktrees/since -->2.1.49（2026-02-19）<!-- gen:end feature worktrees/since --> である（[Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees)）。

## 最小の使い方 {#minimal}

Claude Code を `-w` 付きで起動する。WSL・Linux の CLI を基準に書く。ほかの OS と IDE 拡張での動作は未確認である。

```bash
claude --worktree <名前>
```

起動すると、`.claude/worktrees/<名前>/` に作業ディレクトリが作られ、`worktree-<名前>` というブランチが切られて、そこでセッションが始まる。ターミナルを別に開いて名前を変えれば、同じリポジトリで 2 本目のセッションが並ぶ。分岐元は設定のキー `worktree.baseRef` で決まる。リモートの既定ブランチから切る `fresh` と、今の HEAD から切る `head` がある。新しい worktree には未コミットの変更が入らないので、引き継ぎたい作業は先にコミットし、分岐元の違いも確かめる。

`"#1234"` のような PR の番号や、PR・MR の URL を渡して、その PR を元に worktree を作ることもできる（[Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees)）。

`.claude/worktrees/` は、リポジトリの `.gitignore` に入れておく。公式もそう勧めている。

サブエージェントを worktree で動かしたいときは、サブエージェントの定義に `isolation: worktree` を書く。定義の書き方は <!-- link:begin writing-subagents#define -->[サブエージェントの作り方と使いどころ › 定義の書き方（ファイルを書くか、Claude に作らせる）](../extend/writing-subagents.md#define)<!-- link:end --> にある。git ではないバージョン管理を使うときは、`WorktreeCreate` と `WorktreeRemove` のフックで作成と削除の処理を自分で書く。

## worktree ごとの準備（依存・秘密・データベース） {#per-worktree-setup}

worktree は新しいチェックアウトなので、git が追跡しているファイルしか入っていない。動かすのに要る準備は、worktree ごとに決める。

- **依存**：`node_modules` や仮想環境などは入っていない。worktree ごとにインストールする。公式も、環境の初期化が要ると案内している。
- **秘密のファイル**：`.env` のような gitignore 済みのファイルは、既定では写らない。`.worktreeinclude` に書いたものだけが写される。
- **データベースとポート**：開発用のデータベースや待ち受けのポートを、全 worktree で同じ値にすると衝突する。worktree ごとに名前かポートを変える。単独の経験談だが、複数の worktree でこの衝突を踏む報告が出ている（根拠：弱）。
- **ディスク**：worktree の数だけ、作業ディレクトリと依存の分の容量を使う。

`.worktreeinclude` は、書いたファイルを新しい worktree に写す。**写す先が増えるほど秘密の置き場所も増える**ので、最低限だけを書く。次の雛形は、開発用の 2 ファイルだけを写し、書いてはいけないものをコメントで残す。

<!-- gen:begin snippet parallel-with-worktrees/worktreeinclude -->
<!-- textlint-disable -->

??? example "雛形：.worktreeinclude の例（秘密を写しすぎない）"

    ```text
    # .worktreeinclude（リポジトリの直下に置く。書き方は .gitignore と同じ）
    # 新しい worktree に写すのは、開発で動かすのに最低限要るファイルだけにする。
    # 写す対象は、gitignore されていて、この一覧に当たるファイル。
    .env.local
    config/local.dev.json

    # 次のようなものは書かない。
    # - 本番や共有の認証情報（.env.production・秘密鍵・クラウドの認証ファイル）
    # - 広すぎる指定（.env* や *.pem）：意図しない秘密まで写る
    # - 大きなデータ（worktree の数だけディスクを使う）
    ```

    動作を確かめていない雛形。安全のための雛形なので、守りとして頼る前に、止めたい操作が自分の環境で止まるかを確かめる。要る最低の版：Claude Code 2.1.49。

<!-- textlint-enable -->
<!-- gen:end snippet parallel-with-worktrees/worktreeinclude -->

!!! example "判断例：.env を worktree に写すか"
    - **状況**：3 本のセッションを worktree で並べる。アプリは `.env` の API キーがないと起動しない。
    - **迷う候補**：`.env` を丸ごと `.worktreeinclude` に書く。開発用のキーだけを入れた `.env.local` を別に用意して、それだけを書く。
    - **選んだもの**：開発用のキーだけの `.env.local` を作り、それだけを書く。
    - **理由**：`.env` に本番のキーが混ざっていると、3 つの worktree とそのセッションに本番のキーが広がる。開発用に絞れば、広がっても被害が小さい。置いたあとは、偽の値で写り方を確かめる。確かめ方は <!-- link:begin protecting-secrets#verify -->[秘密情報（.env・API キー）を守る › 偽の秘密で確かめる](../safety/protecting-secrets.md#verify)<!-- link:end --> にある。

秘密を Claude の目に触れさせない二重の守りは <!-- link:begin protecting-secrets#two-layers -->[秘密情報（.env・API キー）を守る › 権限ルールとサンドボックスの二重にする](../safety/protecting-secrets.md#two-layers)<!-- link:end --> にある。サンドボックスの読み取りは既定で広いので、worktree の外の秘密の場所は明示して塞ぐ。範囲は <!-- link:begin sandboxing#default-reads -->[サンドボックスで封じ込める › 読み取りは既定で広い](../enforce/sandboxing.md#default-reads)<!-- link:end --> で確かめる。

## 片付けと残すもの {#cleanup}

セッションを終えるときの扱いは、変更の有無で分かれる。変更がなければ、worktree は自動で削除される。変更があれば、残すか削除するかを聞かれる。

残す前に、次の 3 つを決めておく。

- **取り込むもの**：worktree の中の成果は、`worktree-<名前>` ブランチのコミットとして残る。本流に取り込むには、通常の git の手順（マージ・リベース・PR）を使う。誰がコミットして取り込むかは <!-- link:begin working-with-git#who-commits -->[git との付き合い方 › 誰がコミットするか](../cli/working-with-git.md#who-commits)<!-- link:end --> で決める。
- **捨てるもの**：コミットしていない変更は、worktree を削除すると失われる。捨てるつもりのものだけを削除させる。
- **古い worktree**：残した worktree は、`git worktree list` で一覧し、不要になったら `git worktree remove` で消す。放っておくと、依存の分の容量を使い続ける。

巻き戻しの機能と git も混ぜない。会話とコードを巻き戻す機能は、git の代わりにならない。違いは <!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](../cli/checkpoints-and-rewind.md#what-is-restored)<!-- link:end --> にある。セッションを再開するときは、同じ worktree で再開するのか別に作るのかを先に決める。再開と分岐の名前の付け方は <!-- link:begin resume-and-branch#naming -->[セッションに名前を付けて再開・分岐する › 名前の付け方](../cli/resume-and-branch.md#naming)<!-- link:end --> にある。

## 効かない場面・落とし穴 {#pitfalls}

- **外の状態は分かれない**：データベース・キャッシュ・外部のサービス・ポートは、worktree を分けても同じものを指す。ファイルの衝突は減るが、実行時の衝突は残る。
- **統合のぶつかりは残る**：2 つの worktree が同じファイルを変えれば、取り込むときにマージの衝突が起きる。同じファイルを触る作業は並べず、触る範囲を分けて割り当てる。判断の基準は <!-- link:begin choosing-parallel-modes#same-files -->[並列の方式の選び方 › 同じファイルを触るか](choosing-parallel-modes.md#same-files)<!-- link:end --> にある。
- **出入りの道具が止まる設定がある**：設定のキー `permissions.blockWritesOutsideWorkingDirectories` を true にすると、作業ディレクトリの外への書き込みを、どの権限モードでも拒む。この設定を入れると、会話の途中で worktree を出入りする EnterWorktree と ExitWorktree の道具は使えない。シェルのコマンドと MCP の道具は縛られないため、シェルの側はサンドボックスで塞ぐ（[CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)）。
- **無人の再開で保護が抜けた版がある**：`claude -p --resume` や `--continue` で入った worktree で、サンドボックスの保護が働かない不具合があった。直った版は CHANGELOG で確かめ、無人で走らせる前に自分の版を見る（[CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)）。無人の流し方は <!-- link:begin batch-and-p-loops -->多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）<!-- link:end --> にある。
- **本数が増えると確かめきれない**：worktree は何本でも作れるが、結果を確かめる人は増えない。本数の上限は人の側にある。理由は <!-- link:begin humans-set-the-parallel-limit#why-human-side -->[並列の上限は人間が決める › 上限が人の側にある理由](humans-set-the-parallel-limit.md#why-human-side)<!-- link:end --> にある。

## 比べる相手 {#compare}

worktree は、作業場所を分ける仕組みである。目的が違う仕組みと取り違えないようにする。

- **並列の方式全体**：誰が調整するか、同じファイルを触るかで選ぶ。worktree はその 1 つの手段である。比較は <!-- link:begin choosing-parallel-modes#compare -->[並列の方式の選び方 › 方式の比較](choosing-parallel-modes.md#compare)<!-- link:end --> にある。
- **agent view と背景セッション**：見張らなくてよい作業を投入し、状態を一覧する仕組みである。作業場所を分ける仕組みとは役割が違う。向く作業の判断は <!-- link:begin agent-view-and-background#what-fits -->[agent view と背景セッション › 向く作業と向かない作業](agent-view-and-background.md#what-fits)<!-- link:end --> にある。
- **/batch と `-p` のループ**：多数のファイルに同じ作業を流す仕組みである。worktree との併用の可否は、このページでは確かめていない。流し方は <!-- link:begin batch-and-p-loops -->多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）<!-- link:end --> にある。
- **セッションの分岐**：会話の分岐であり、ファイルの置き場所は変わらない。分岐した会話を別々のファイルで動かすなら、worktree が要る。会話の分岐は <!-- link:begin resume-and-branch#branch -->[セッションに名前を付けて再開・分岐する › 分岐して別案を試す](../cli/resume-and-branch.md#branch)<!-- link:end --> にある。
- **サブエージェント**：文脈を分ける仕組みであり、ファイルを分けるには `isolation: worktree` を足す。使いどころは <!-- link:begin writing-subagents#when-to-use -->[サブエージェントの作り方と使いどころ › 使いどころと、使わない場面](../extend/writing-subagents.md#when-to-use)<!-- link:end --> にある。

古くなった助言の台帳に、この機能の行はない（確認日 2026-11-05 時点）。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees)：Anthropic・英語・確認日 2026-11-04
- [Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)：Anthropic・英語・確認日 2026-11-04
- [Claude Code changelog](https://code.claude.com/docs/en/changelog)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [git との付き合い方](../cli/working-with-git.md)

**次に読む**

- [仮説ごとに並べて、同じ物差しで比べる](compare-hypotheses-in-parallel.md)
- 多数のファイルに同じ作業を流す（/batch と -p のループ）（準備中）

**関連**

- [並列の方式の選び方](choosing-parallel-modes.md)
- [並列の上限は人間が決める](humans-set-the-parallel-limit.md)
- [agent view と背景セッション](agent-view-and-background.md)
- [秘密情報（.env・API キー）を守る](../safety/protecting-secrets.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- [セッションに名前を付けて再開・分岐する](../cli/resume-and-branch.md)
- [サブエージェントの作り方と使いどころ](../extend/writing-subagents.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
