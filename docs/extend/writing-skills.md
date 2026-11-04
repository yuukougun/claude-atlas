---
id: writing-skills
title: スキルの作り方
aliases: [SKILL.md, カスタムコマンド, カスタムスラッシュコマンド, .claude/commands, skill-creator, .claude/skills]
type: feature
field: extend
chapter: スキル
order: 110
level: 仕組みにする
priority: 必須
surfaces: [claude-code, app]
principle: [見せる]
prevents: [見えていない]
pitfalls: [体感を信じる]
scenes: [開発, 文章]
summary: 繰り返す手順をスキルにして、Claude にも自分にも呼べるようにできる。本文は短くし、詳しい資料と決まった処理は補助ファイルとスクリプトに分ける。
signs:
  - {type: goal, text: 繰り返す作業の手順を、名前で呼べるようにしたい}
  - {type: goal, text: 自分用のスラッシュコマンドを作りたい}
  - {type: situation, text: 昔の記事のとおり、コマンド用のフォルダに Markdown を置いている}
  - {type: goal, text: 作ったスキルが効いているかを、体感ではなく確かめたい}
prerequisites: [how-skills-load]
related: [skill-descriptions, manual-only-skills, hook-vs-skill, skill-vs-subagent, permission-rules, vetting-extensions, measure-changes, felt-vs-measured, move-judgment-into-scripts, plugins-and-marketplaces, skills-in-the-app, share-team-settings, less-ai-sounding-japanese#proofreading-skill, pruning-extensions, writing-subagents, claude-md-vs-rules-skills-styles, when-to-add-what]
tracks: [skills]
outdated_advice: [commands-directory]
sources: [cc-docs-skills, api-docs-skill-best-practices]
volatility: 中
sections:
  - {title: どんなときにスキルにするか, anchor: when-to-use}
  - {title: 最小のスキルを作る, anchor: minimal}
  - {title: カスタムコマンドから移る, anchor: from-commands}
  - {title: 補助ファイルとスクリプトに分ける, anchor: supporting-files}
  - {title: 効いているかを確かめる, anchor: evaluate}
  - {title: 効かない場面と落とし穴, anchor: limits}
stage: draft
updated: 2026-11-04
---

!!! abstract "要点"
    - **何ができるか**：繰り返す手順をスキルにして、Claude と自分の両方から呼べるようにできる。本文は短くし、詳しい資料は別のファイル（補助ファイル）に、決まった処理はスクリプトに分ける。
    - **いつ引くか**：繰り返す作業の手順を、名前で呼べるようにしたいとき。自分用のスラッシュコマンドを作りたいとき。昔の記事のとおり、コマンド用のフォルダ（`.claude/commands/`）に Markdown を置いているとき。カスタムコマンドはスキルにまとめられていて、既存のコマンドは今も動くので、急いで移さなくてよい。移す判断は、[カスタムコマンドから移る](#from-commands)の節にある。
    - **強制力**：<!-- gen:begin feature enforcement -->お願い<!-- gen:end feature enforcement -->。手順を渡す仕組みなので、何も止められない。使われないことも、途中で従わなくなることも防げない。毎回守らせたい規則は、フックに移す。
    - **前提**：<!-- link:begin how-skills-load -->[スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)<!-- link:end -->

<!-- textlint-disable -->
別名：SKILL.md・カスタムコマンド・カスタムスラッシュコマンド・.claude/commands・skill-creator・.claude/skills
<!-- textlint-enable -->

スキルの作り方は、繰り返す手順を `SKILL.md` に書き、`/名前` と Claude の判断のどちらでも呼べるようにする方法である。本文は短く保ち、詳しい資料とスクリプトは別のファイルに分ける。作った後は、体感で済ませず、スキルの有無を比べて確かめる。

## どんなときにスキルにするか {#when-to-use}

スキルが防ぐのは、必要な手順が Claude に見えていないことである。同じ手順書やチェックリストを会話へ何度も貼っているなら、その手順はスキルの候補である。自分用のスラッシュコマンドを作りたいときも、スキルにする。スキルは `/名前` で呼べる。公式の文書は、スキルを勧める場面として、同じ指示や手順を何度も貼るときと、CLAUDE.md の一部が事実ではなく手順へ育ったときを挙げている。

スキルのコンテキストのコストは、<!-- gen:begin feature context_cost -->使うまで小さい<!-- gen:end feature context_cost -->。本文は呼ばれたときだけ会話に入り、使わない会話で場所を取るのは名前と説明だけである。何回繰り返したらスキルにするかの目安は、「<!-- link:begin when-to-add-what -->[拡張を足すタイミング](when-to-add-what.md)<!-- link:end -->」にある。

似た手段との分け方は次のとおりである。

- **決まったときに動かしたい処理**はフックにする。スキルは Claude が読んで従う手順で、従わせる力はない。違いは「<!-- link:begin hook-vs-skill -->[フックとスキルの違い](hook-vs-skill.md)<!-- link:end -->」にまとめてある。
- **別の文脈で作業させ、要約だけを受け取りたいとき**はサブエージェントにする。違いは「<!-- link:begin skill-vs-subagent -->[スキルとサブエージェントの違い](skill-vs-subagent.md)<!-- link:end -->」にある。
- **常に成り立つ短い事実や規約**は、CLAUDE.md や rules に置く。分け方は「<!-- link:begin claude-md-vs-rules-skills-styles -->[CLAUDE.md・rules・スキル・出力スタイルの違い](claude-md-vs-rules-skills-styles.md)<!-- link:end -->」にある。

文章の手直しも、スキルにできる。<!-- link:begin less-ai-sounding-japanese#proofreading-skill -->日本語の「AI 臭さ」を減らす › 推敲をスキルにする（文体を保つか、構成から直すか）（準備中）<!-- link:end -->は、日本語の推敲をスキルにする例である。

## 最小のスキルを作る {#minimal}

最小のスキルは、フォルダ 1 つと `SKILL.md` 1 つである。`SKILL.md` は、先頭のフロントマターと、その後ろの本文でできている。フロントマターの `name` はスキルの名前で、`/名前` の名前にもなる。`description` は、Claude がそのスキルを読み込むかを決める手がかりである。本文には、呼ばれたときに従う手順を書く。

<!-- gen:begin snippet writing-skills/SKILL -->
<!-- textlint-disable -->

??? example "雛形：最小の SKILL.md（リリースノートの下書き）"

    ```markdown
    ---
    name: release-notes
    description: リリースの準備で「リリースノートを書いて」「変更点をまとめて」と頼まれたときに使う。直近のタグから今までのコミットを集めて、製品の利用者向けの下書きにする。
    ---

    直近のタグから今までの変更を集めて、リリースノートの下書きを作る。

    1. `git describe --tags --abbrev=0` で直近のタグを調べ、そのタグから HEAD までのコミットを `git log` で集める。
    2. コミットを「追加」「変更」「修正」に分け、1 項目を 1 行で書く。製品の利用者に関係しない変更は省く。
    3. 出力は Markdown の箇条書きだけにする。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet writing-skills/SKILL -->

この例の `description` は、いつ使うかを先頭に書いている。本文は 3 つの手順だけで、ほかのファイルは要らない。コミットの集計をスクリプトに任せる形は、[補助ファイルとスクリプトに分ける](#supporting-files)の節で示す。

置き場所と呼び方は、面で違う。

=== "アプリ"

    アプリでは、同じ形の `SKILL.md` を入れたスキルをアップロードして有効にする。手順は「<!-- link:begin skills-in-the-app#upload -->アプリでスキルを使う › 自作のスキルを入れる（準備中）<!-- link:end -->」に任せる。

    アップロードで使えるフロントマターのキーは、`name`・`description`・`license`・`compatibility`・`metadata`・`allowed-tools` だけである。ほかのキーを入れると、取り込みはエラーで止まる。`argument-hint` や `disable-model-invocation` のような Claude Code だけのキーを使ったスキルは、そのままではアップロードできない。コマンドの出力を本文に埋め込む記法など、Claude Code だけの本文の機能も、アプリでは動かない。

=== "Claude Code"

    1. フォルダを作る。個人用なら `~/.claude/skills/<名前>/`、リポジトリで共有するなら `.claude/skills/<名前>/` である。
    2. その中に `SKILL.md` を置く。スクリプトを使うなら `scripts/` に入れる。
    3. `/名前` で呼んで、本文のとおりに動くかを見る。Claude に任せるときは、`description` に合う依頼を投げる。

    編集した内容は、同じセッションの中で反映される。セッションを始めた後に、`~/.claude/skills/` か `.claude/skills/` のフォルダそのものを初めて作ったときだけ、`/reload-skills` を流す。リポジトリの `.claude/skills/` を commit すれば、チームで同じスキルを使える。共有の設定は「<!-- link:begin share-team-settings -->チームで設定を共有する（準備中）<!-- link:end -->」、複数のリポジトリに配る方法は「<!-- link:begin plugins-and-marketplaces -->プラグインとマーケットプレイス（準備中）<!-- link:end -->」にある。

Claude Code では、フロントマターのキーはすべて省けるが、`description` は書く。`name` を省くと、フォルダ名がスキルの名前になる。アプリや API に持ち出すスキルは、`name` と `description` の両方が要る。`name` は英小文字・数字・ハイフンだけにしておくと、持ち出しやすい。`name` と `description` には文字数の上限があり、値は [Skill authoring best practices の Skill structure の項](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#skill-structure)で確かめる。ほかのキーは、[公式の文書のフロントマターの一覧](https://code.claude.com/docs/en/skills#frontmatter-reference)で確かめる。

最初から自分で書かなくてもよい。うまくいった作業を終えた会話の中で、Claude にスキルの案を書かせる方法がある。[Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) も、作業を終えた後に、その会話で与えた文脈や好みをスキルにさせる流れを勧めている。頼み方の雛形を次に示す。作らせた本文には、Claude がもともと知っている説明が入りがちなので、削って短くする。

<!-- gen:begin snippet writing-skills/make-skill-prompt -->
<!-- textlint-disable -->

??? example "雛形：うまくいった会話からスキルを作らせるプロンプト"

    ```text
    この会話でうまくいった手順を、あとから何度も使えるスキルにしたいです。
    次の条件で、`.claude/skills/<名前>/SKILL.md` の案を作ってください。

    - 名前は、英小文字・数字・ハイフンだけにする。
    - この会話で私が直した点と、指定した条件を、手順に入れる。
    - `description` には、先頭に「いつ使うか」を書く。
    - 本文は短くする。Claude がもともと知っていることは書かない。
    - 長い資料は別のファイルに、毎回同じ結果にしたい処理はスクリプトに分ける。

    ファイルを作る前に、名前・`description`・ファイルの構成の案を見せて、私の返事を待ってください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet writing-skills/make-skill-prompt -->

公式の skill-creator プラグインを使うと、作ったスキルの有無を比べる確かめを、会話の中から自動で回せる。使い方は、[効いているかを確かめる](#evaluate)の節にある。

## カスタムコマンドから移る {#from-commands}

`.claude/commands/` に置いた Markdown のカスタムコマンドは、今もそのまま動く。コマンドとスキルはまとめられていて、`.claude/commands/deploy.md` と `.claude/skills/deploy/SKILL.md` は、どちらも `/deploy` になる。同じ名前のものが両方あるときは、スキルが優先される。そのため、急いで移す必要はない。

この節と、これ以降の節は、特に断らない限り、Claude Code の話である。アプリで使うスキルは、「<!-- link:begin skills-in-the-app -->アプリでスキルを使う（準備中）<!-- link:end -->」に任せる。

スキルに移すのは、スキルにしかない働きが要るものからにする。公式の文書は、スキルが足す働きとして次の 3 つを挙げている。

- 資料やスクリプトを置くフォルダ
- 呼ぶのが自分か Claude かを決めるフロントマター
- 関係する場面で Claude が読み込む働き

新しく作るものは、最初からスキルにする。

!!! example "判断例：2 つのコマンドを移すか"
    - **状況**：`.claude/commands/` に `commit-msg.md` と `release-notes.md` がある。前者は 5 行ほどで、自分だけが呼ぶ。後者は書式の説明が長く、コミットの集計を毎回 Claude に書かせている。
    - **迷う候補**：両方を移す／どちらも移さない／必要なほうだけ移す
    - **選んだもの**：`release-notes` だけをスキルに移す。`commit-msg` はそのまま置く。
    - **理由**：`release-notes` は、書式を補助ファイルに、集計をスクリプトに分けたい。この分け方はスキルのフォルダが前提である。`commit-msg` は 1 ファイルで足りていて、移しても得るものがない。

移る前の `release-notes` コマンドの例を、書式の説明を省いて次に示す。

<!-- gen:begin snippet writing-skills/legacy-command -->
<!-- textlint-disable -->

??? example "雛形：移る前：.claude/commands/ のコマンド（リリースノートの下書き）"

    ```markdown
    ---
    description: リリースノートの下書きを作る
    argument-hint: [起点のタグ]
    ---

    直近のタグ（`$ARGUMENTS` で指定されたときはそのタグ）から HEAD までのコミットを `git log` で集めて、
    リリースノートの下書きを作ってください。
    「追加」「変更」「修正」に分け、1 項目を 1 行で書いてください。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet writing-skills/legacy-command -->

移す手順は次のとおりである。

1. `.claude/skills/<名前>/` を作り、コマンドのファイルを `SKILL.md` として移す。
2. フロントマターの `description` を、いつ使うかを先頭に具体的に書いた文に書き直す。スキルでは、説明が Claude の読み込む手がかりになる。`name` は、Claude Code だけで使うなら省ける。アプリや API へ持ち出すなら足す。
3. デプロイや送信のように副作用のある手順なら、`disable-model-invocation: true` を足して、人だけが呼べるようにする。考え方は「<!-- link:begin manual-only-skills -->副作用のあるスキルを勝手に動かさない（準備中）<!-- link:end -->」にある。
4. 長い本文を、補助ファイルとスクリプトに分ける。分け方は、[補助ファイルとスクリプトに分ける](#supporting-files)の節で述べる。
5. 古いコマンドのファイルを消す。同名のスキルが優先されるが、どちらが動いているかが分かりにくくなる。

手順 1 と 2 だけを済ませたスキルは、移る前のファイルの本文をそのまま使い、フロントマターが次のように変わる。

- `description`：何をするかだけの一言（例：「リリースノートの下書きを作る」）を、いつ使うかから始まる文に変える。たとえば「リリースの準備で『リリースノートを書いて』と頼まれたときに使う」と書き始める。
- `name`：足さなくてもよい。足さないと、フォルダ名（ここでは `release-notes`）が呼ぶ名前になる。
- `argument-hint` と本文の `$ARGUMENTS`：そのまま使える。`/release-notes v1.2.0` のように、名前の後ろに続けて書いた引数が `$ARGUMENTS` に入る。

移した後は、`/` のメニューに出るかと、呼ぶ名前が変わっていないかを確かめる。サブフォルダに置いたコマンド（`.claude/commands/frontend/component.md` など）は、今も `/frontend:component` の形で呼ぶ。スキルの名前はフォルダ名か `name` で決まり、サブフォルダの区切りは入らない。呼び方が変わるので、たとえば `frontend-component` のように、名前を付け直す。

昔の記事にある `/project:` や `/user:` を付けた呼び方は、今は使わず、`/<名前>` で呼ぶ。この古くなった助言の扱いは、「<!-- link:begin outdated-advice-ledger#commands-directory -->[古くなった助言の台帳](../changes/outdated-advice-ledger.md#commands-directory)<!-- link:end -->」にまとめてある。

## 補助ファイルとスクリプトに分ける {#supporting-files}

`SKILL.md` の本文は、呼ばれると会話に入り、以後のやり取りでも残り続ける。本文の 1 行ごとが、以後のやり取りで毎回かかるコストになる。そこで、本文は手順の骨格と案内だけにして、詳しい内容は同じフォルダの別のファイルに分ける。公式の文書は、本文を短く保つ行数の目安を挙げている（値は、[公式の文書の補助ファイルの節](https://code.claude.com/docs/en/skills#add-supporting-files)で確かめる）。それを超えそうになったら分ける。

分けて置くものは 3 種類ある。この辞典では、本文とスクリプトを除く、資料のファイルを補助ファイルと呼ぶ。公式の文書の「supporting files」は、スクリプトも含む呼び名である。

- **本文（`SKILL.md`）**：手順の骨格と、補助ファイルを読む条件を書く。「書式を確かめるときは `format.md` を読む」のように、ファイルの中身と読む場面を添える。
- **補助ファイル**：長い仕様・書式の詳細・見本を置く。Claude が読むまでは、場所を取らない。
- **スクリプト（`scripts/`）**：決まった処理を置く。実行させると、会話に入るのは出力だけで、スクリプトの中身は入らない。

<!-- gen:begin snippet writing-skills/skill-folder-layout -->
<!-- textlint-disable -->

??? example "雛形：スキルのフォルダの構成（本文・補助ファイル・scripts）"

    ```text
    .claude/skills/release-notes/
    ├── SKILL.md                  # 本文。手順の骨格と、補助ファイルを読む条件だけ書く
    ├── format.md                 # 補助ファイル。書式の詳細。本文から案内し、必要なときだけ読ませる
    ├── examples.md               # 補助ファイル。出来上がりの見本
    └── scripts/
        └── collect-changes.sh    # 決まった処理。実行させ、中身は読ませない
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet writing-skills/skill-folder-layout -->

コミットの集計のように、結果を毎回同じにしたい処理は、スクリプトにする。最小の例の手順 1 を、スクリプトの実行に置き換えた `SKILL.md` は、次のとおりである。スクリプトの場所は `${CLAUDE_SKILL_DIR}` で書く。この変数は `SKILL.md` のあるフォルダに置き換わるので、どこから呼んでも同じ場所を指す。

<!-- gen:begin snippet writing-skills/SKILL-with-script -->
<!-- textlint-disable -->

??? example "雛形：スクリプトを呼ぶ SKILL.md（リリースノートの下書き）"

    ```markdown
    ---
    name: release-notes
    description: リリースの準備で「リリースノートを書いて」「変更点をまとめて」と頼まれたときに使う。直近のタグから今までのコミットを集めて、製品の利用者向けの下書きにする。
    ---

    直近のタグから今までの変更を集めて、リリースノートの下書きを作る。

    1. `bash ${CLAUDE_SKILL_DIR}/scripts/collect-changes.sh` を実行して、コミットの一覧を得る。起点のタグを指定されたときは、第 1 引数に渡す。
    2. 一覧を「追加」「変更」「修正」に分け、1 項目を 1 行で書く。製品の利用者に関係しない変更は省く。
    3. 出力は Markdown の箇条書きだけにする。
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet writing-skills/SKILL-with-script -->

起点のタグを指定するときは、`/release-notes v1.2.0` のように、スキルの名前の後ろに続けて書く。本文に引数の置き場所（`$ARGUMENTS`）がなくても、渡した引数は本文の末尾に `ARGUMENTS: v1.2.0` の形で付く。手順 1 の「第 1 引数に渡す」は、この値をスクリプトの第 1 引数にする指示である。呼ばれるスクリプトは、次のとおりである。

<!-- gen:begin snippet writing-skills/collect-changes -->
<!-- textlint-disable -->

??? example "雛形：スクリプト：collect-changes.sh（コミットの一覧を出す）"

    ```bash
    #!/usr/bin/env bash
    # 直近のタグから HEAD までのコミットを、1 行 1 件で標準出力に出す。
    # 使い方: collect-changes.sh [起点にするタグ]
    set -euo pipefail

    since="${1:-}"
    if [ -z "$since" ]; then
      since="$(git describe --tags --abbrev=0 2>/dev/null || true)"
    fi
    if [ -z "$since" ]; then
      echo "起点にするタグが見つからない。第 1 引数にタグ名を渡す。" >&2
      exit 1
    fi

    git log --no-merges --pretty='- %s (%h)' "${since}..HEAD"
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet writing-skills/collect-changes -->

この節の `${CLAUDE_SKILL_DIR}` は Claude Code の置き換えの記法で、アプリで同じ書き方が動くかは、確かめていない。

分け方と書き方の判断は 4 つある。

**何を補助ファイルに出すか**：毎回要る手順は本文に残し、特定の場面でだけ要る詳細を補助ファイルに出す。補助ファイルは、本文から直接案内するものに限る。補助ファイルからさらに別のファイルへ案内を重ねると、Claude が先頭だけを読んで止まることがある。長い補助ファイルは、冒頭に目次を置く（長さの目安は、[Platform の指針の該当の項](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#structure-longer-reference-files-with-a-table-of-contents)にある）。

**何をスクリプトにするか**：手順が 1 通りに決まり、結果が毎回同じであるべき処理は、スクリプトにする。状況で判断が変わる所は、文章で書く。公式の指針も、壊れやすい処理には具体的なスクリプトを、判断が要る処理には文章の指示を使い分けるよう書いている。スクリプトにすると結果が毎回同じになり、確かめやすくなる。考え方は「<!-- link:begin move-judgment-into-scripts -->判断を決定論的なスクリプトに移す（準備中）<!-- link:end -->」にある。

**実行させるのか、読ませるのか**：本文に、スクリプトを実行するのか、読んで参考にするのかを書く。ほとんどは実行させる。

**失敗したときの出し方**：スクリプトは、失敗したときに足りないものをメッセージに出して止まるようにする。原因の推測を Claude に任せない。雛形の `collect-changes.sh` は、起点のタグが決まらないとき、標準エラーに理由を出して終了コード 1 で止まる。

圧縮の後、スキルは<!-- gen:begin feature survives_compaction -->残る<!-- gen:end feature survives_compaction -->。ただし残るのは、呼んだスキルの本文の、1 つあたり<!-- fact:begin skill-reattach-tokens-each -->先頭から 5000 トークンまで（2026-11-04 時点）<!-- fact:end -->、全体で<!-- fact:begin skill-reattach-tokens-total -->合計 25000 トークンまで（2026-11-04 時点）<!-- fact:end -->で、古く呼んだものは落ちる。仕組みは「<!-- link:begin how-skills-load#after-compaction -->[スキルの考え方（手順を必要なときだけ読む） › 圧縮の後に戻るもの](how-skills-load.md#after-compaction)<!-- link:end -->」にある。そのため、大事な指示は本文の上に置く。圧縮の後にスキルが守られなくなったら、呼び直す。

スクリプトを動かすたびに確認を求められると、作業の流れが止まる。確認を省く前に、スクリプトの中身を自分で読む。リポジトリに入っている他人のスキルは、`allowed-tools` とスクリプトを読んでから使う。確認の手順は「<!-- link:begin vetting-extensions -->[MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)<!-- link:end -->」にある。

確認を省くには、フロントマターの `allowed-tools` に、省きたいコマンドを書く。許可するコマンドは、本文が指示するコマンドと同じ形で書く。本文と `allowed-tools` の両方で `${CLAUDE_SKILL_DIR}` を使うと、形がそろう。次の 1 行は、この節のスクリプトの例である。

<!-- gen:begin snippet writing-skills/allowed-tools -->
<!-- textlint-disable -->

??? example "雛形：確認を省く allowed-tools の行（SKILL.md のフロントマターに足す）"

    ```yaml
    allowed-tools: Bash(bash ${CLAUDE_SKILL_DIR}/scripts/collect-changes.sh *)
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet writing-skills/allowed-tools -->

省くのは、そのスキルを呼んだターンの間だけで、列挙した道具に限られる。使える道具を絞る設定ではないので、禁じたいものは権限ルールで禁じる。書き方は「<!-- link:begin permission-rules -->[権限ルール（allow・ask・deny）](../enforce/permission-rules.md)<!-- link:end -->」にある。

## 効いているかを確かめる {#evaluate}

スキルが呼ばれたことは、スキルが意図どおりに働いたことを示さない。[公式の文書の評価の節](https://code.claude.com/docs/en/skills#evaluate-and-iterate-on-a-skill)は、Claude が呼ぶべき依頼で呼んでいるかと、呼んだときの出力が期待に合っているかを、別々に測るよう書いている。作った直後の「うまく動いた気がする」では、どちらも確かめられていない。

確かめる材料は、スキルを書く前に集める。スキルなしで Claude に頼んで、うまくいかなかった依頼を数件控えておく。リリースノートなら、コミットの取りこぼしがあった依頼である。書く手順は、その失敗を直す最小のものにする。もう書いてしまった後なら、過去の会話から、うまくいかなかった依頼を選び直す。[Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#build-evaluations-first) も、スキルなしで失敗する場面を先に集めてから、指示を書くよう勧めている。

確かめ方は 3 段階である。

1. **呼ばれるかを見る**：使わせたい依頼を、自分が実際に言う言い方で、新しいセッションに投げる。使えるスキルを聞いて、名前が出るかも見る。呼ばれないときは、`/名前` で直接呼べるかを見て、説明を直す。直し方は「<!-- link:begin skill-descriptions -->[スキルの description の書き方](skill-descriptions.md)<!-- link:end -->」にある。
2. **出力が合うかを見る**：期待を、先に箇条書きで書いておく。`release-notes` なら、「追加・変更・修正に分かれている」「利用者に関係しない変更がない」「箇条書きだけで出る」である。呼ばれたときの出力が、この期待を満たすかを照らす。
3. **有無を比べる**：控えておいた依頼を数件選び、新しいセッションで、スキルを有効にした場合と切った場合を、それぞれ数回走らせて比べる。

新しいセッションにするのは、スキルを書いたときの会話が残っていると、手順の書き漏れが隠れるからである。

スキルの有無を切り替える手順は、Claude Code のものである。個人用かプロジェクトのスキルを切るには、設定の `skillOverrides` で `"off"` にする。`/skills` のメニューからも切り替えられ、その場合は `.claude/settings.local.json` に書かれる。手で書くときも、同じ `.claude/settings.local.json` に書く。実験のための切り替えを、チームで共有する `.claude/settings.json` に書くと、チームの全員でそのスキルが切れる。切ったスキルは Claude にも `/` のメニューにも出なくなるので、比べる実験の「無し」側に使える。

<!-- gen:begin snippet writing-skills/local-settings -->
<!-- textlint-disable -->

??? example "雛形：比べる実験でスキルを切る設定（.claude/settings.local.json の skillOverrides）"

    ```json
    {
      "skillOverrides": {
        "release-notes": "off"
      }
    }
    ```

    動作を確かめていない雛形。要る最低の版：Claude Code 2.0.20。

<!-- textlint-enable -->
<!-- gen:end snippet writing-skills/local-settings -->

プラグインで配るスキルには `skillOverrides` が効かない。その場合は、プラグインを入れた場合と入れない場合を自動で比べる `claude plugin eval` を使う。

この比べる作業は、会話の中から自動で回すこともできる。公式のマーケットプレイスの skill-creator プラグインは、`/plugin install skill-creator@claude-plugins-official` で入れる。テストの依頼と期待をスキルのフォルダの `evals/evals.json` に残し、依頼ごとに独立したサブエージェントで、スキルの有無を走らせて採点する。説明を直す材料として、呼ばせたい依頼と呼ばせたくない依頼を作り、呼ばれる割合を測る機能もある。依頼ごとにサブエージェントが走るので、依頼を増やすほど、トークンと時間がかかる。結果には、スキルの有無でトークンと時間がどれだけ違うかも出る。依頼は、控えておいた数件から始める。

!!! example "判断例：作ったスキルが効いたか"
    - **状況**：スキルを作る前、同じ依頼でコミットの取りこぼしがあったので、その依頼を数件控えておいた。`release-notes` を作り、2 回使ってみたら、どちらも良い下書きが出た。
    - **迷う候補**：このまま配る／もう数回試してみる／控えた依頼で有無を比べる
    - **選んだもの**：控えた依頼で、新しいセッションを使い、スキルを有効にした場合と切った場合を、それぞれ数回ずつ走らせて比べる。
    - **理由**：2 回の成功では、スキルのおかげか、たまたまかを分けられない。もう数回試しても、スキルなしでも同じ結果が出たかは分からない。スキルを書いた会話には手順の補足が残っているので、同じ会話で試すと、書き漏れも見えない。

どの方法でも、1 回の試行で判断しない。体感と実測がずれる理由は「<!-- link:begin felt-vs-measured -->[体感と実測](../eval/felt-vs-measured.md)<!-- link:end -->」、小さく比べる手順は「<!-- link:begin measure-changes -->[変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)<!-- link:end -->」にある。効き方は使うモデルでも変わるので、公式のベストプラクティスに従い、使うモデルのすべてで試す。アプリで使うスキルが使われないときの確かめ方は、「<!-- link:begin skills-in-the-app -->アプリでスキルを使う（準備中）<!-- link:end -->」にある。

## 効かない場面と落とし穴 {#limits}

スキルは手順を渡す仕組みで、従わせる仕組みではない。効かない場面と、見落としやすい点は次のとおりである。特に断らない限り、Claude Code の話である。

- **途中で従わなくなる**：本文は呼ばれたときに一度だけ会話に入り、ファイルは読み直されない。毎回守らせたい規則は、フックに移す。設定のフックは、そのイベントのたびに動く。スキルと一緒に持たせたいなら、フロントマターの `hooks` に書く。この `hooks` は、スキルを呼んだときから、セッションの終わりまで効く。
- **指針が一度きりの手順として読まれる**：作業全体に当てはめたい指針は、「テストを走らせる」ではなく「編集のたびにテストを走らせる」のように、作業全体に当てはまる形で書く。
- **呼ばれない、呼ばれすぎる**：説明が依頼の言葉に合っていないか、ほかのスキルと重なっている。呼ばれないときは、依頼で使う言葉を含む形に説明を直す。呼ばれすぎるときは、説明を具体的にするか、人だけが呼ぶ設定にする。説明の直し方は「<!-- link:begin skill-descriptions -->[スキルの description の書き方](skill-descriptions.md)<!-- link:end -->」にある。
- **副作用のある手順を勝手に動かす**：デプロイや送信のような手順は、`disable-model-invocation: true` を付けて、Claude が自分の判断では動かさないようにする。付け方は「<!-- link:begin manual-only-skills -->副作用のあるスキルを勝手に動かさない（準備中）<!-- link:end -->」にある。
- **一覧に載るコストが積もる**：入れたスキルの名前と説明は、使わなくても毎回のやり取りに載る。数が増えると、一覧の長さの上限を超えないよう説明が削られ、呼ばれにくくなる（上限の値は「<!-- link:begin how-skills-load#residual-cost -->[スキルの考え方（手順を必要なときだけ読む） › 入れすぎたときに残るコスト](how-skills-load.md#residual-cost)<!-- link:end -->」、変え方は[公式の文書の説明が切られる節](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short)にある）。`/skill-doctor` で費用と使われ方を見て、使っていないものを外す。外し方は「<!-- link:begin pruning-extensions -->[拡張の棚卸しと剪定](pruning-extensions.md)<!-- link:end -->」にある。
- **同じ名前のスキルが複数ある**：管理設定、個人用、プロジェクトの順に優先される。個人用とプロジェクトに同じ名前のスキルがあれば、個人用が動く。`.claude/commands/` のファイルと同じ名前なら、スキルが動く。詳しい表は、[公式の文書の同名の扱い](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name)にある。
- **組み込みのコマンドや同梱のスキルと同じ名前にしたとき**：その名前では、自作のスキルが動く。置き換わるのは名前だけで、元のコマンドの別名で呼ぶと、元のコマンドが動く。組み込みのコマンドについては、ローカルのターミナルのセッションでの挙動で、ほかの環境は確かめていない。
- **`verify` か `simplify` という名前**：この名前のスキルがあり、Claude が呼べる設定になっていると、Claude はコミットの直前にそれを実行する。文書とテストだけの変更は除く。名前だけでコミットのたびに動くので、意図して付ける。条件は、[公式の文書のコミット前の確認](https://code.claude.com/docs/en/skills#run-your-checks-before-each-commit)にある。
- **他人のスキルの中身**：リポジトリやプラグインから入るスキルは、スクリプトを持てる。入れる前に中身を読む。確認の手順は「<!-- link:begin vetting-extensions -->[MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)<!-- link:end -->」にある。

<!-- gen:begin references -->
<!-- textlint-disable -->

## 参考 {#references}

- [Extend Claude with skills](https://code.claude.com/docs/en/skills)：Anthropic・英語・確認日 2026-11-04
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)：Anthropic・英語・確認日 2026-11-04

<!-- textlint-enable -->
<!-- gen:end references -->

<!-- gen:begin page-links -->
<!-- textlint-disable -->

<div class="ca-page-links" markdown>

**前提**

- [スキルの考え方（手順を必要なときだけ読む）](how-skills-load.md)

**次に読む**

- [スキルの description の書き方](skill-descriptions.md)
- 副作用のあるスキルを勝手に動かさない（準備中）

**関連**

- [フックとスキルの違い](hook-vs-skill.md)
- [スキルとサブエージェントの違い](skill-vs-subagent.md)
- [権限ルール（allow・ask・deny）](../enforce/permission-rules.md)
- [MCP・プラグイン・スキルを入れる前の確認](../safety/vetting-extensions.md)
- [変更が効いたかを測る（小さな eval）](../eval/measure-changes.md)
- [体感と実測](../eval/felt-vs-measured.md)
- 判断を決定論的なスクリプトに移す（準備中）
- プラグインとマーケットプレイス（準備中）
- アプリでスキルを使う（準備中）
- チームで設定を共有する（準備中）
- 日本語の「AI 臭さ」を減らす › 推敲をスキルにする（文体を保つか、構成から直すか）（準備中）
- [拡張の棚卸しと剪定](pruning-extensions.md)
- [サブエージェントの作り方と使いどころ](writing-subagents.md)
- [CLAUDE.md・rules・スキル・出力スタイルの違い](claude-md-vs-rules-skills-styles.md)
- [拡張を足すタイミング](when-to-add-what.md)

</div>

<!-- textlint-enable -->
<!-- gen:end page-links -->
