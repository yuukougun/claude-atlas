---
id: deleted-something-important
title: 消してはいけないものを消された
aliases: [ファイルを消された, rm -rf された, 履歴を消された]
type: symptom
field: symptoms
chapter: 安全と承認
order: 280
level: 任せる
priority: 必須
surfaces: [claude-code, app]
principle: [縛る, 握る]
prevents: [縛っていない, 境界がない]
pitfalls: [預けすぎる]
scenes: [開発]
summary: 消してはいけないファイルや履歴を消されたときに、戻せる手段を先に確かめて復旧し、何が止められなかったかを切り分けて再発を防ぐ。
signs:
  - {type: symptom, text: ファイルを消された・消されそうで怖い}
  - {type: symptom, text: git の履歴やブランチを巻き戻された}
  - {type: symptom, text: データベースのデータを消された}
wave: 1
prerequisites: [request-vs-lock]
related: [checkpoints-and-rewind, working-with-git, recover-lost-work, block-with-exit-2, hook-recipes, postmortems, notes-and-pkm, wrong-amount-of-approvals, secrets-exposed, six-causes]
routes:
  - {cause: 縛っていない, to: [destructive-commands, permission-rules, protected-paths]}
  - {cause: 境界がない, to: [sandboxing, where-bypass-is-ok]}
  - {cause: 預けすぎる, to: [default-safety-settings#by-stage, what-auto-mode-stops#limits]}
tracks: [checkpoints, permissions, permission-modes, sandbox, hooks]
outdated_advice: [yolo-skip-permissions]
sources: [cc-docs-checkpointing, cc-docs-permissions, cc-docs-sandboxing, cc-docs-permission-modes, cc-docs-hooks-guide, cc-docs-best-practices, api-docs-prompting-best-practices, anthropic-eng-code-auto-mode, cc-issue-10077, cc-issue-75859]
volatility: 中
sections:
  - {title: よくある形, anchor: forms}
  - {title: まず戻す（復旧の手順）, anchor: recover}
  - {title: 原因を安く確かめる順, anchor: diagnosis}
  - {title: 判断例, anchor: examples}
  - {title: 予防：戻せる状態と鍵を先に置く, anchor: prevention}
stage: draft
updated: 2026-11-05
---

!!! abstract "要点"
    - **何ができるか**：消されたものを戻せる手段（git・チェックポイント・バックアップ）を先に確かめ、止められなかった原因を切り分けて再発を防げる。
    - **いつ引くか**：ファイルを消された、または消されそうで怖いとき。git の履歴やブランチを巻き戻されたとき。データベースのデータを消されたとき。
    - **前提**：<!-- link:begin request-vs-lock -->[お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)<!-- link:end -->

<!-- textlint-disable -->
別名：ファイルを消された・rm -rf された・履歴を消された
<!-- textlint-enable -->

消してはいけないものを消された場合は、原因を探す前に、戻せる手段が残っているかを確かめる。戻せるかどうかは、何で消されたかで決まる。復旧のあとで、止める仕組みがお願いだけだったのか、鍵があっても外れたのかを切り分け、再発を防ぐ。

## よくある形 {#forms}

消された形ごとに、戻し方の入口が変わる。消された直後なら、先に[復旧の節](#recover)へ進む。

- **ファイルを消された・消されそうで怖い**：`rm -rf` のような削除で、作業ディレクトリの外まで消えることがある。GitHub の Issue には、ある Bash 呼び出しで `HOME` を一時ディレクトリに変え、別の Bash 呼び出しで `rm -rf "$HOME"` を実行した報告がある。Bash の呼び出しの間でシェルの環境変数は引き継がれないので、本物のホームに展開されて Documents などが消えた（根拠：弱。単独の経験談）。
- **git の履歴やブランチを巻き戻された**：`git reset --hard` や force push のような、戻しにくい操作である。公式のプロンプトの手引きは、指示がなければ、ファイルの削除や force push のような戻しにくい行動を取ることがあると書く（Opus 4.6 についての記述）。
- **データベースのデータを消された**：Anthropic の社内の記録には、指示を誤解して本番のデータベースに migration を試みた例がある。データベースの中身は、git でもチェックポイントでも戻らない。

## まず戻す（復旧の手順） {#recover}

消された直後は、原因を探すより先に、これ以上状態を変えないことと、戻せる手段の確認を優先する。

1. **止める**：Claude の作業を中断する。「元に戻して」と続けて頼まない。復旧のつもりのコマンドが、戻せる状態をさらに変えることがある（この辞典の推奨）。復旧が終わるまで、消えた場所に新しいものを書かせない。
2. **何が消えたかを分ける**：消えたものによって、戻す先が違う。
    - **git で追跡していたファイル**：`git status` で、削除や変更として出るかを見る。出れば `git restore <パス>` で、コミットした（または `git add` した）時点の内容に戻る。未コミットの編集は戻らない。
    - **git の履歴やブランチ**：`git reflog` で、巻き戻される前のコミットを探す。見つかれば、`git branch <新しい名前> <コミット>` で付け直すか、`git reset` で戻す。reflog は手元の clone の記録で、リモートの履歴は別である。未コミットの変更は reflog にも残らない。
    - **git の外のファイル**（未追跡・未コミット・作業ディレクトリの外）：git では戻らない。この後の段で述べるチェックポイント、バックアップ、エディタの履歴を探す。
    - **データベース**：git とチェックポイントのどちらも及ばない。データベース側のバックアップやスナップショットを確かめる。手順はデータベースごとに違い、このページでは扱わない。

次に、チェックポイントで戻せるかを見る。チェックポイントは Claude のファイル編集の道具が変えた分だけを記録するので、何で消されたかによって、効く場合と効かない場合がある。

=== "アプリ"

    - チェックポイントと `/rewind` は Claude Code の機能で、アプリでの復旧の手段は、この教材ではまだ確かめていない（未確認）。
    - git やバックアップから戻す手は、面によらず使える。

=== "Claude Code"

    - `/rewind` で、送ったプロンプトごとの時点に、コード・会話・その両方を戻せる。
    - 戻せるのは、Claude のファイル編集の道具で変えたファイルだけである。Bash で消したファイル、Bash だけが変えたファイル、Claude Code の外での変更、ほとんどのサブエージェントの編集は戻らない。
    - 戻せるものと戻せないものの詳細は、<!-- link:begin checkpoints-and-rewind#what-is-restored -->[チェックポイントと /rewind（git との違い） › 戻せるもの・戻せないもの](../cli/checkpoints-and-rewind.md#what-is-restored)<!-- link:end -->にある。チェックポイントは git の代わりにならない。

どこにも見つからないときは、失った作業をセッションの記録から探す。探す順と記録の場所は、<!-- link:begin recover-lost-work#order -->[セッション記録から失った作業を取り戻す › 探す順](../cli/recover-lost-work.md#order)<!-- link:end -->にある。

戻せたら、戻した内容が消える前と同じかを、差分で確かめる。そのうえで、次の節で原因を切り分ける。

## 原因を安く確かめる順 {#diagnosis}

復旧のめどが立ったら、なぜ止まらなかったのかを、確かめる手間が小さい順に見る。どれも、設定と記録を見るだけの確認である。

1. **縛っていない**：消した操作を止める鍵（権限ルールの deny、フック）が、置いてあったか。
    - 見るもの：設定ファイルの deny ルールとフック、そして CLAUDE.md の「消さない」という文である。CLAUDE.md の文は、Claude が読んで判断するお願いで、鍵ではない。違いは<!-- link:begin request-vs-lock#sorting -->[お願いと鍵（決定論的か、非決定論的か） › お願いと鍵の分け方](../basics/request-vs-lock.md#sorting)<!-- link:end -->にある。
    - 確かめ方：消された操作と同じ形の操作に、deny ルールが当たるかを見る。何も置いていなければ、縛っていなかった。
    - deny を置いていたのに消えたなら、パスの書き方が当たっていなかったか、スクリプト（Python・Node など）が消したかを疑う。Read・Edit の deny は、任意の子プロセスには効かない。見方は<!-- link:begin permission-rules#path-rules -->[権限ルール（allow・ask・deny） › パスの書き方と、何にも当たらないルール](../enforce/permission-rules.md#path-rules)<!-- link:end -->と<!-- link:begin permission-rules#child-processes -->[権限ルール（allow・ask・deny） › 子プロセスには効かない](../enforce/permission-rules.md#child-processes)<!-- link:end -->にある。
2. **境界がない**：Claude に触らせるつもりのない場所が消えていたか。
    - 見るもの：消えたパスが作業ディレクトリの内か外か。サンドボックスを有効にしていたか。確認をすべて外すモード（bypassPermissions）で動かしていたか。
    - 確かめ方：パスが作業ディレクトリの外なら、境界がなかった。サンドボックスは、シェルのコマンドとそこから起きたプロセスを OS の層で囲むが、Claude のファイルの道具・MCP サーバー・フックは囲まない。囲えるものは<!-- link:begin sandboxing#scope -->[サンドボックスで封じ込める › 囲えるもの・囲えないもの](../enforce/sandboxing.md#scope)<!-- link:end -->で確かめる。
    - 作業ディレクトリの外への書き込みを止める設定は、ファイルの道具の書き込みを止めるが、シェルのコマンドは止めない。隔離の代わりにならない。見方は<!-- link:begin protected-paths#outside-working-directory -->[消せない場所・触れない場所（protected paths） › 作業ディレクトリの外への読み書きを閉じる](../enforce/protected-paths.md#outside-working-directory)<!-- link:end -->にある。
    - bypassPermissions で動かしていたなら、隔離した使い捨ての環境の外で使っていないかを見る。理由は<!-- link:begin where-bypass-is-ok#why-isolate -->[bypassPermissions と無人の実行はどこで動かすか › なぜ隔離した環境だけか](../safety/where-bypass-is-ok.md#why-isolate)<!-- link:end -->にある。
3. **預けすぎる**（人の側の落とし穴）：確認を減らして任せる幅を広げたのに、見合う守りを足さなかった。
    - 見るもの：消した時点の権限モードと、そのとき足していた守り（deny ルール・サンドボックス・バックアップ）。
    - 確かめ方：auto モードで消されたなら、auto モードは確認を減らす仕組みで、安全を保証しない。すり抜けうる操作は<!-- link:begin what-auto-mode-stops#limits -->[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits)<!-- link:end -->にある。任せる段階ごとに足す設定は<!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end -->にある。

確かめる場所は、面によって違う。

=== "アプリ"

    - 権限やサンドボックスの確かめ方は、この教材ではまだ確かめていない（未確認）。
    - 消えた場所が、アプリに渡したフォルダの内か外かだけでも控えておく。

=== "Claude Code"

    - 設定ファイルの `permissions` と `hooks`、`/permissions` で見えるルールの一覧、消した時点の権限モードを見る。
    - サンドボックスの有無は設定で分かる。

原因が分かったら、次の表の先へ進む。

<!-- gen:begin routes -->
<!-- textlint-disable -->

| 原因 | 対処のページ（近い順） |
| --- | --- |
| 縛っていない | [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)<br>[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<br>[消せない場所・触れない場所（protected paths）](../enforce/protected-paths.md) |
| 境界がない | [サンドボックスで封じ込める](../enforce/sandboxing.md)<br>[bypassPermissions と無人の実行はどこで動かすか](../safety/where-bypass-is-ok.md) |
| 預けすぎる | [安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<br>[auto モードは何を止め、何を止めないか › すり抜けと限界](../enforce/what-auto-mode-stops.md#limits) |

<!-- textlint-enable -->
<!-- gen:end routes -->

## 判断例 {#examples}

!!! example "判断例：git reset --hard で数コミットが消えた"
    - **状況**：長い作業を任せている間に、Claude が `git reset --hard` を実行し、直近の数コミットが履歴から消えた。
    - **迷う候補**：`/rewind` でコードを戻す。`git reflog` で巻き戻される前のコミットを探す。
    - **選んだもの**：`git reflog` でコミットを探して付け直し、コミットしていなかった編集だけをチェックポイントで確かめる。
    - **理由**：履歴の巻き戻しは git の操作で、チェックポイントはファイル編集の道具が変えたファイルしか記録しない。コミットは reflog に残るが、未コミットの変更は残らない。2 つを分けて見ると、戻せない部分が早く分かる。

!!! example "判断例：作業ディレクトリの外のファイルが消えた"
    - **状況**：「不要なファイルを片付けて」と頼んだ後、作業ディレクトリの外のフォルダのファイルが消えた。git では管理していない。
    - **迷う候補**：まず設定を見直して原因を突き止める。まずバックアップから復旧する。
    - **選んだもの**：作業を止め、バックアップから復旧してから、原因を切り分ける。
    - **理由**：原因の切り分けは復旧の後でもできるが、復旧が遅れるほど、消えた場所への書き込みが進み、戻せるものが減りうる。復旧のあと、パスが作業ディレクトリの外なので「境界がない」と分かる。サンドボックスと、作業ディレクトリの外への書き込みを止める設定を足し、その設定がシェルのコマンドを止めないことも踏まえて決める。

## 予防：戻せる状態と鍵を先に置く {#prevention}

同じことを繰り返さないために、戻せる状態を先に作り、消されたくないものは鍵で守る。

- **戻せる状態を先に作る**：変更を小さく区切ってコミットしておくと、消されても戻せる。区切り方は<!-- link:begin working-with-git#granularity -->[git との付き合い方 › どこで区切るか](../cli/working-with-git.md#granularity)<!-- link:end -->にある。ノートの保管庫のような、コードでないフォルダに一括の書き換えを任せるときも、先に戻せる状態にする。<!-- link:begin notes-and-pkm -->ノート・PKM（Obsidian など）（準備中）<!-- link:end -->を参照する。
- **消されたくないものは鍵で守る**：例外を許さない禁止は、deny ルールかフックで止める。CLAUDE.md には、理由と相談の基準だけを書く。経路と、巻き戻しで戻らないものは<!-- link:begin destructive-commands#how-it-happens -->[消されたくないもの（破壊的コマンド） › 消える経路](../safety/destructive-commands.md#how-it-happens)<!-- link:end -->にある。止めた理由と代わりの手段を返すフックの書き方は、<!-- link:begin block-with-exit-2 -->[フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)<!-- link:end -->と<!-- link:begin hook-recipes#block-dangerous -->[代表的なフックのレシピ › 危ない操作を止める](../enforce/hook-recipes.md#block-dangerous)<!-- link:end -->にある。
- **境界を OS の層で足す**：サンドボックスでシェルのコマンドを囲む。確認をすべて外す運用は、隔離した使い捨ての環境だけにする。古くなった助言は<!-- link:begin outdated-advice-ledger#yolo-skip-permissions -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#yolo-skip-permissions)<!-- link:end -->にある。
- **任せる幅に守りを合わせる**：確認を減らすほど、守りを同じ流れの中で足す。段階ごとの設定は<!-- link:begin default-safety-settings#by-stage -->[安全の早見表（面ごとの既定と、段階ごとに足すもの） › 段階ごとに足すもの](../safety/default-safety-settings.md#by-stage)<!-- link:end -->にある。
- **失敗を仕組みに戻す**：誰の誤りかではなく、どの隙間が許したかで振り返る。方法は<!-- link:begin postmortems -->[失敗を仕組みに戻す（ポストモーテム）](../judgment/postmortems.md)<!-- link:end -->にある。

承認の確認の量が合っていないことが根にあるなら、<!-- link:begin wrong-amount-of-approvals -->[承認の確認が多すぎる・少なすぎる](wrong-amount-of-approvals.md)<!-- link:end -->を見る。秘密の情報が読まれた疑いがあるなら、<!-- link:begin secrets-exposed -->[秘密の情報を読まれた・外に出された](secrets-exposed.md)<!-- link:end -->を先に見る。症状全体の振り分けは<!-- link:begin six-causes -->[失敗の二つの軸と診断の入口](../start/six-causes.md)<!-- link:end -->から始める。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Checkpointing](https://code.claude.com/docs/en/checkpointing)：Anthropic・英語・確認日 2026-11-04
- [Configure permissions](https://code.claude.com/docs/en/permissions)：Anthropic・英語・確認日 2026-11-04
- [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing)：Anthropic・英語・確認日 2026-11-04
- [Choose a permission mode](https://code.claude.com/docs/en/permission-modes)：Anthropic・英語・確認日 2026-11-04
- [Automate actions with hooks](https://code.claude.com/docs/en/hooks-guide)：Anthropic・英語・確認日 2026-11-04
- [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)：Anthropic・英語・確認日 2026-11-04
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)：Anthropic・英語・確認日 2026-11-04
- [How we built Claude Code auto mode: a safer way to skip permissions](https://www.anthropic.com/research/claude-code-auto-mode)：Anthropic・英語・確認日 2026-11-04
- [\[BUG\] ## CRITICAL: Claude Code executed rm -rf deleting entire home directory（Issue #10077）](https://github.com/anthropics/claude-code/issues/10077)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04
- [Claude Code ran rm -rf against $HOME due to env var not persisting between Bash tool calls, deleting Downloads/Documents/Pictures/.config（Issue #75859）](https://github.com/anthropics/claude-code/issues/75859)：GitHub の anthropics/claude-code の issue（利用者の報告）・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [お願いと鍵（決定論的か、非決定論的か）](../basics/request-vs-lock.md)

**次に読む**

- [消されたくないもの（破壊的コマンド）](../safety/destructive-commands.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [消せない場所・触れない場所（protected paths）](../enforce/protected-paths.md)
- [サンドボックスで封じ込める](../enforce/sandboxing.md)
- [bypassPermissions と無人の実行はどこで動かすか](../safety/where-bypass-is-ok.md)
- [安全の早見表（面ごとの既定と、段階ごとに足すもの）](../safety/default-safety-settings.md)
- [auto モードは何を止め、何を止めないか](../enforce/what-auto-mode-stops.md)

**関連**

- [チェックポイントと /rewind（git との違い）](../cli/checkpoints-and-rewind.md)
- [git との付き合い方](../cli/working-with-git.md)
- [セッション記録から失った作業を取り戻す](../cli/recover-lost-work.md)
- [フックで止めて理由を返す（exit 2 と JSON）](../enforce/block-with-exit-2.md)
- [代表的なフックのレシピ](../enforce/hook-recipes.md)
- [失敗を仕組みに戻す（ポストモーテム）](../judgment/postmortems.md)
- ノート・PKM（Obsidian など）（準備中）
- [承認の確認が多すぎる・少なすぎる](wrong-amount-of-approvals.md)
- [秘密の情報を読まれた・外に出された](secrets-exposed.md)
- [失敗の二つの軸と診断の入口](../start/six-causes.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
