# .claude/：制作の縛り（deny ルールとフック）

claude-atlas の制作で、破ると害が大きく、機械で判定できる規則だけを止める設定である（planning/design.md §10.5、design-review.md の DR-08）。判断を含む規則（何が小さな直しか、など）は縛らず、CLAUDE.md と担当への指示に任せる。書いたときに確かめた Claude Code は 2.1.317（2026-11-04）。

## 入っているもの

| ファイル | 中身 |
| --- | --- |
| `settings.json` | deny ルール（`permissions.deny`。H1・H2 の強制）と、フックの登録（`hooks` の PreToolUse と SessionStart） |
| `hooks/pre_tool_use.py` | PreToolUse のフック。H1・H2 の理由と記録、H1 の Bash の照らし、H3 |
| `hooks/session_start.py` | SessionStart のフック。H4 の知らせ |
| `README.md` | この文書 |

試験は `tests/hooks/test_hooks.py` にある。フックのスクリプトに入力の JSON を与えて、出力と終了コードを確かめる（Claude Code は起動しない）。`python3 -m unittest discover -s tests/hooks` と `uv run python -m unittest discover -s tests/hooks` の両方で流す。

## 規則

| # | 規則 | 止めるもの | 働くとき | 止めたときに返すこと |
| --- | --- | --- | --- | --- |
| H1 | AI の利用を断るサイト（atcoder.jp・codeforces.com とそのサブドメイン）を開かない | WebFetch は deny ルール（`WebFetch(domain:…)` と `WebFetch(domain:*.…)`）。Bash はフックが、取得の道具の URL の引数のホストだけを照らす | いつも | そのサイトは AI の利用を断っている。別の一次資料を探し、なければ報告に書く |
| H2 | 生成物を手で書き換えない（`docs/llms.txt`・`docs/lists/` の下・`docs/<分野>/index.md`） | deny ルール（`Edit(/…)`）。フックは同じパスに理由を返す | いつも | 元のデータを直し、`gen_site.py` で作り直す（担当は `gen_site.py --page <id>`、ほかはメインに頼む） |
| H3 | 担当（サブエージェント）の git と gh は読むだけ | フックだけ（入力に `agent_id` がある呼び出し。メインは止めない） | 制作の印 `state/production` があるとき | commit・push・巻き戻しはメインが行う。変更は報告に書いて終える |
| H4 | API キーで課金されないようにする | 止めない（止める確かめは `tools/check_templates.py` の中の必須の確かめ） | 印があり、API キーなどの変数があるとき | 従量の課金になる。実機の確認の前に変数を外す |

どの理由の文にも「この止め方が作業に合わないときは、別の手段で回り込まず、そのことを報告に書く（メインなら作者に相談する）」を添える（design §10.5 の決まり 2）。理由は命令でなく事実の形で書く（research/28 #16）。

### H1 の細部

- ドメインの一覧は `settings.json` の deny ルールの `WebFetch(domain:…)` だけに持つ。フックはそこから読む（二か所に持たない）
- Bash で照らすのは、取得の道具（curl・wget・wget2・http・https・httpie・xh・xhs・curlie・aria2c・lynx・w3m・links・elinks）の引数の URL だけである。`atcoder.jp/…` のように scheme のない形も見る
- ドメインの文字列では照らさない。`grep atcoder.jp`・`echo`・`python3 tools/check_noai.py <URL>`（AI の利用を断るドメインを自分で取得しない道具）は止まらない
- コマンドは字句に分けてから照らす。`sudo`・`env`・`timeout`・`xargs` などを前に付けた形と、`bash -c '…'`・`eval`・`$( )` の中もたどる。ヒアドキュメントの本文と注釈は照らさない
- 止めないもの：WebSearch、MCP の道具（Claude in Chrome など）、自分で取得するスクリプト（Python の urllib など）、変数に入れた URL、写し（Internet Archive など。理由の文で「同じ扱い」と伝えるだけ）
- サンドボックスを有効にすると、`WebFetch(domain:…)` の規則が Bash のネットワークにも効く（research/28 #9）。制作では有効にしていない

### H2 の細部

- パスの一覧は `settings.json` の deny ルールの `Edit(/…)` だけに持つ。リポジトリの根からの相対で、`*` は 1 段、`**` は深さを問わない
- フックはその一覧を読み、Edit・Write・NotebookEdit のパスと、Bash の書き込みの形（リダイレクト・`tee`・`sed -i` の書き先）を照らす。Bash の形は、Claude Code が deny ルールで見分ける形に合わせた（research/28 #12）
- 生成の道具は子のプロセスなので止まらない（意図どおり）。読むこと（Read・`cat`・`grep`）も止めない
- 手書きのページの中の生成部分（`<!-- gen:begin … -->` などの目印の間）はパスで守れないので、CI の `gen_site.py --check` が見つける
- `nav.yml` は土台作りの間は手書きの仮なので、まだ deny ルールに入れていない。`gen_site.py` が生成するようになったら `Edit(/nav.yml)` を足す。`schema/page.schema.json`（生成してコミットするなら）と、overrides/ の生成したデータ（置き場所が決まったら）も同じ
- `Edit(/…)` の deny ルールは生成物にだけ使う（フックがすべての `Edit(/…)` に H2 の理由を返すため）

### H3 の細部

- 担当かどうかは、入力の `agent_id` の有無で見分ける。`agent_id` はサブエージェントの中の呼び出しにだけ付く。`agent_type` は `--agent` で起動したメインにも付くので使わない（research/28 #1。2.1.317 の入力の型の説明も同じ）
- 許す git：status・diff・log・show と、書き込む形のない読むだけのもの（blame・annotate・ls-files・ls-tree・rev-parse・rev-list・grep・cat-file・shortlog・describe・merge-base・show-ref・for-each-ref・name-rev・cherry・count-objects・check-ignore・check-attr・whatchanged・diff-tree・diff-files・diff-index・range-diff・var・help・version）
- `--output` でファイルに書く形は止める。`-C`・`-c`・`--git-dir` などの前置きのオプションは飛ばして照らすので、`git -C . commit` も止まる
- 別名（`git ci` など）・`stash list`・`branch`・`config`・`remote`・`tag` は、書き込む形があるので一覧に入れていない
- 許す gh：`pr`（view・list・diff・checks・status）・`issue`（view・list・status）・`repo`（view・list）・`run`（view・list・watch）・`workflow`・`release`・`gist`（view・list）・`label list`・`auth status`・`search`・`status`・`help`・`version`
- `gh api` は GET だけを許す。`-X` で GET 以外を指定した形と、`-f`・`-F`・`--input` を付けて GET を指定しない形は止める
- 止めないもの：スクリプトの中から動かす git（`python3 -c "subprocess.run(['git', …])"` など）、`find -exec git …`、変数に入れたコマンド
- 担当の作業ツリー（worktree）には印がないので、そこでは働かない（worktree で並列に直す段で扱いを決める）
- フックがワークフローの担当でも走るかは、文書に書かれていない（research/28 #4）。効かなかったときの代わりは、バッチの始めと終わりの HEAD を state/ に記録して比べること（design §10.5。メインの手順）

### H4 の細部

- 見る変数：`ANTHROPIC_…_API_KEY`・`ANTHROPIC_…_AUTH_TOKEN` の形（`ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN` を含む）で値が空でないものと、`CLAUDE_CODE_USE_BEDROCK`・`CLAUDE_CODE_USE_VERTEX`・`CLAUDE_CODE_USE_FOUNDRY` が 0・false でないもの
- 値は読まず、名前だけを利用者（systemMessage）と Claude（additionalContext）に出す

## 読者の環境で動くもの・動かないもの

- deny ルール（H1・H2）は、フォルダの信頼の前から効く（research/28 #19）
- フックは、対話のセッションでは信頼のダイアログを受け入れた後に走る。`claude -p` と SDK は確認なしに走る
- 制作の印がない環境（読者がリポジトリを開いたとき）では、H3・H4 は何もしないで終わる。H1・H2 のフックは deny ルールと同じ範囲に理由を返すだけで、記録も書かない
- フックはネットワークを使わず、ファイルを壊さない。書くのは、印があるときの `state/` の記録だけで、`state/` がなければ何も作らない
- フックは標準のライブラリの `python3` で動く。3.8 以上を目安にし、3.8 は文法だけを確かめた（試験は 3.10 と 3.12 で流した）。1 回あたり十数ミリ秒かかる
- PreToolUse のフックは、Bash・Edit・Write・NotebookEdit・WebFetch の呼び出しのたびに走る（matcher は完全一致の名前の並び）。SessionStart のフックは、起動・再開・/clear・圧縮のたびに走る
- フックはサンドボックスの外で、利用者の権限で動く（research/28 #43）
- 外したいときは、`.claude/settings.json` の deny ルールと `hooks` を消す（ほかのスコープの allow ルールでは deny ルールを外せない）

## 依存が欠けたとき・フックが壊れたとき

| 状況 | どうなるか |
| --- | --- |
| `python3` がない・起動できない・10 秒で終わらない | フックの誤りとして表示され、操作は進む（Claude Code の既定。`onFailure` は付けていない）。H1 の WebFetch と H2 は deny ルールが止め続け、H1 の Bash と H3 は止まらない |
| フックのスクリプトの中の誤り | 何も出さずに通す。ただし、印があり、担当の Bash に git か gh が出てくるときだけは止める（H3 はこのフックだけが止めるので、止める側に倒す） |
| `settings.json` が壊れている | 対話では Claude Code が設定の誤りを示す（`-p` は黙って飛ばす。research/28 #31）。フックは H1・H2 の照らしをしない（H3 は settings.json を読まない） |
| 入力の JSON が壊れている | 何もしないで通す |

`onFailure: "block"` を付けない理由：付けると、python3 のない読者の環境で、当たった呼び出し（Bash など）がすべて止まる。古い Claude Code はこのキーを知らない（2.1.295 から）。制作の環境には python3 がある。フックの command は、古い版でも動くシェルの形（`python3 "$CLAUDE_PROJECT_DIR/…"`）で書いた。

## 止めた記録と見直し

`state/blocks.log`（追跡しない）に、止めた操作を 1 行ずつ書く（印があるときだけ）。

```text
日時<TAB>規則（H1〜H3）<TAB>誰（main か agent:<agent_type>:<agent_id>）<TAB>道具<TAB>対象（ホスト・パス・コマンド）
```

対象は 160 字で切り、秘密らしい値（`sk-ant-…`・`Bearer …`・`token=…` など）は伏せる。メインはバッチの終わりに、担当の報告の「止められた操作」と照らして見直す。不適切な対処を招いた規則は外すか直し、その例を制作の記録（planning/production-log.md）に書く（決まり 4）。

## 制作の印と、効いているかの確かめ方

- `state/production`（追跡しない）：H3・H4 と記録を有効にする。メインが確かめてから作り、消せば止まる
- `state/hook-trace`（追跡しない）：あると、PreToolUse のフックが呼ばれるたびに、`state/hook-trace.log` へ 1 行（日時・イベント・道具・agent_id・agent_type・止めたか）を書く。コマンドの中身は書かない
- 確かめ方の例：`state/production` と `state/hook-trace` を置き、ワークフローの担当に `git commit --dry-run`（何も変えない）を頼む。止められることと、hook-trace.log に agent_id が出ることを見る。確かめたら `state/hook-trace` を消す
- 動いているセッションで settings.json の変更がすぐ効くかは、セッションの種類で違いうる（確かめていない）。新しいセッションは、信頼の後に読む

## 規則を変えるとき

- `.claude/` は保護されたパスで、書き込みには確認か、auto モードの分類器の審査が要る（research/28 #20）
- AI の利用を断るドメインを足す：deny ルールに `WebFetch(domain:<ドメイン>)` と `WebFetch(domain:*.<ドメイン>)` の 2 行を足す（試験が両方あるかを確かめる）。フックは deny ルールから読むので直さなくてよい。sources で断るドメインがすべて deny ルールにあるかは、検査の層が確かめる（design §8.6）
- 生成物のパスを足す：deny ルールに `Edit(/<パス>)` を足し、試験の生成物と手書きのパスの例（`SettingsTest`）を直す
- 新しい縛りは、機械で判定でき害の大きい規則だけにし、先に design §10.5 の表を直す。変えたら試験を流す
- `settings.json` の `$schema` は、公式の文書が案内する SchemaStore のスキーマである（新しいキーに遅れる。research/28 #46）。いまの設定は古くからあるキーだけを使う
