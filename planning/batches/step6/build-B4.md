# 工程6a 1段目 B4（縛り）の報告

- 担当：B4（共通の指示は [brief-build.md](brief-build.md)、受け持ちは [README.md](README.md) の表）
- 日付：2026-11-04。手元の Claude Code は 2.1.317、python3 は 3.10.12、uv の Python は 3.12.15
- 制作の印 `state/production` は作っていない。git と gh は使っていない

## 1. 作ったファイルと中身の要約

| ファイル | 中身 |
| --- | --- |
| `CLAUDE.md` | 何の教材か、再開するとき（state/now.md → progress.md → 設計書）、守ること（design §10.5 の5つと、kyopro-atlas は読むだけ）、道具（uv run・check_all.py）、並列の規則、仕組みで止めていること（H1〜H3 の一覧と、止められたら回り込まずに報告に書くこと） |
| `.claude/settings.json` | deny ルール7行（H1：`WebFetch(domain:atcoder.jp)`・`*.atcoder.jp`・`codeforces.com`・`*.codeforces.com`、H2：`Edit(/docs/llms.txt)`・`Edit(/docs/lists/**)`・`Edit(/docs/*/index.md)`）と、フック2つ（PreToolUse：matcher `Bash|Edit|Write|NotebookEdit|WebFetch`、SessionStart：matcher なし）。allow・ask・Bash の deny は置いていない |
| `.claude/hooks/pre_tool_use.py` | H1（WebFetch の理由と記録、Bash の取得の道具の URL の照らし）・H2（生成物のパスへの Edit・Write・NotebookEdit と、Bash のリダイレクト・tee・sed -i の理由と記録）・H3（印があるときの担当の git・gh の書き込みを止める）。標準のライブラリだけ |
| `.claude/hooks/session_start.py` | H4（印があり API キーなどの変数があるときに、名前だけを知らせる。止めない） |
| `.claude/README.md` | 入っているもの、規則の表と細部、読者の環境で動くもの・動かないもの、依存が欠けたとき・フックが壊れたとき、止めた記録の形と見直し、効いているかの確かめ方、規則を変えるとき |
| `tests/hooks/test_hooks.py` | フックの試験（47件。サブテストを含めて200を超える入力）。一時フォルダに .claude/ を写し、入力の JSON を与えて出力と終了コードを見る |

止めたときの返し方：exit 0 と JSON（`permissionDecision: "deny"` と `permissionDecisionReason`）。理由は事実の形で書き、規則の番号、代わりの手段、「この止め方が作業に合わないときは、別の手段で回り込まず、そのことを報告に書く（メインなら作者に相談する）」を必ず添える。止めないときは何も出さない。

## 2. 確かめたこと

- **試験**：`python3 -m unittest discover -s tests/hooks`（3.10.12）・`/usr/bin/python3.12 -m unittest …`・`uv run --frozen python -m unittest discover -s tests/hooks`（3.12.15）で 47件すべて通った。3.8 は手元にないので、`ast.parse(feature_version=(3, 8))` で文法だけを確かめた
- **試験が誤りを捕まえるか**：フックの判定を10か所わざと壊して流し、9か所で試験が落ちた（残り1つは同じ意味になる変更）。確かめた後に元に戻し、一致を `cmp` で確かめた
- **試験の中身**：settings.json の形（ドメインごとに2行あるか、Bash・Read の deny がないか、Edit の deny が根からの相対か、生成物の例に当たり手書きの例に当たらないか、command の文字列をそのまま bash で動かせるか）、H1〜H4 の止める例と止めない例、メインの commit の形（`git commit -m "$(cat <<'EOF' … EOF)"`。本文の `'`・`(`・`> docs/llms.txt` を含む）、記録（印があるときだけ・`state/` を作らない・秘密らしい値を伏せる）、壊れた入力・壊れた設定・閉じない引用、フックの中の誤り（印があり担当の git・gh のときだけ止める側）、理由の長さ（2000字・20行以内）、標準のライブラリだけか
- **いまの作業を止めないか**（メインの頼み）：入れた後の本物のフックに、メインと B1〜B5 がいまするような呼び出し19通りを与え、すべて止めなかった（メインの commit と push、`gh repo view`、`uv sync --locked && uv run mkdocs build --strict`、`npm ci`、担当の `uv run python -m unittest`・`python3 tools/check_catalog.py`・PyPI への curl・`git status`、`docs/index.md`・`nav.yml`・`mkdocs.yml`・`overrides/`・`schema/page.schema.json`・`data/`・`planning/guides/`・`tools/` への書き込み、npm と PyPI への WebFetch）。`state/` には何も書かれなかった
- **deny ルールの影響**：WebFetch の deny は atcoder.jp・codeforces.com とそのサブドメインだけで、PyPI・npm・公式の文書は止めない。Edit の deny の3つのパスは、いまどれも存在しない（`docs/index.md` は `docs/*/index.md` に当たらない）。生成の道具は子のプロセスなので止まらない。Bash の deny はないので、git の commit と push・uv run・npm・python3 の道具は止まらない。H3・H4 は印がないので働かない
- **重さ**：フック1回が約16ミリ秒（Python の起動だけで約9ミリ秒）
- **入力の形**：research/28 #1 のとおり。加えて、手元の 2.1.317 の実行ファイルに含まれる型の定義（文字列を grep で読んだ。Web は使っていない）で、共通の入力（session_id・transcript_path・cwd・permission_mode・`agent_id`・`agent_type` など）と、`agent_id` の説明（サブエージェントの中の呼び出しにだけ付き、`--agent` のメインにも付かない。メインと見分けるにはこれを使う）、PreToolUse の入力（tool_name・tool_input・tool_use_id）、道具の入力の名前（Edit・Write の file_path、NotebookEdit の notebook_path、WebFetch の url）、出力の hookSpecificOutput の項目、command のフックの項目（command・args・if・shell・timeout〔秒〕・onFailure〔continue か block〕）、permissionDecisionReason の上限（2000）を確かめた
- **`.claude/` への書き込み**：この担当（auto モードのメインから起動）は、`.claude/hooks/`・`.claude/settings.json`・`.claude/README.md` に確認なしで書けた（分類器が通したと見られる。モードは確かめていない）。ワークフローのスクリプトの置き場所を決める材料になる
- **書き方**：B3 の textlint（prh を含む）を CLAUDE.md と .claude/README.md に、--fix なしで当てた。誤りは0件、警告は列挙の行の文の長さの4件だけ。用語は B3 の prh に合わせた（フック・サンドボックス・auto モード・deny ルール）

## 3. 決めたこと

1. **一覧は1か所**：AI の利用を断るドメインと生成物のパスは、settings.json の deny ルールだけに持ち、フックはそこから読む（ドメインを足すときに直すのは settings.json だけ）。そのため、`Edit(/…)` の deny ルールは生成物にだけ使う（README に書いた）
2. **H2 の範囲**：いまは `docs/llms.txt`・`docs/lists/**`・`docs/*/index.md` だけ。`nav.yml` は B1 が手で書く仮の間は入れない（入れると B1 が止まる）。Bash は、Claude Code の deny ルールが見分けると文書にある形（リダイレクト・tee・sed -i）だけを照らし、deny ルールより広く止めないようにした
3. **H3 で許す git**：design の「読むだけの git（status・diff・log・show）」を、書き込む形のない読むだけのもの（blame・ls-files・rev-parse・grep など。一覧は .claude/README.md）まで広げた。4つに絞ると、`git rev-parse HEAD` や `git ls-files` のような無害な確かめまで止まり、ユーザーの注意（柔軟な対応を奪わない）に反するため。書き込む形のある stash・branch・config・remote・tag と、別名は許していない。`--output` は止める。gh は view・list などの読むだけと、`gh api` の GET だけを許す
4. **照らし方**：文字列の部分一致では照らさない。小さなシェルの字句の分け方（引用・エスケープ・注釈・演算子・リダイレクト・ヒアドキュメント・`$( )`・`` ` ` ``・`<( )`）を自前で書き、前に付けるコマンド（sudo・env・timeout・xargs など）と `bash -c`・`eval` をたどる。`$( )` の中のヒアドキュメントの本文も飛ばす（メインの commit の形で、本文の `'` のために後ろの `git push` を見落とす誤りを見つけて直した）
5. **壊れたときの倒し方（決まり5の「規則ごと」）**：フックの中の誤りは止めない側に倒す（H1 の WebFetch と H2 は deny ルールが強制するため）。ただし、印があり、担当の Bash に git か gh が出てくるときだけは止める側に倒す（H3 はフックだけが強制するため）。python3 がないときは Claude Code の既定（誤りを示して進む）に任せ、`onFailure: "block"` は付けない（付けると python3 のない読者の環境で Bash がすべて止まる。2.1.295 より古い版はこのキーを知らない）
6. **command の形**：`python3 "$CLAUDE_PROJECT_DIR/.claude/hooks/…"` のシェルの形にした。文書は exec の形（`args`）を勧めるが（research/28 #23）、`args` が入った版を確かめられず、古い版では `args` を知らずに python3 だけが起動するため。`if` も使わない（判定はスクリプトの中で行う）。timeout は10秒
7. **記録**：`state/blocks.log` は印があるときだけ書き、`state/` がなければ何も作らない（読者の環境に書かない）。1行は「日時・規則・誰（main か agent:<agent_type>:<agent_id>）・道具・対象」のタブ区切り。対象は160字で切り、`sk-ant-…`・`Bearer …`・`token=…` などは伏せる
8. **確かめるための印**：`state/hook-trace` があるときだけ、PreToolUse のフックが呼ばれるたびに `state/hook-trace.log` へ1行（日時・イベント・道具・agent_id・agent_type・止めたか）を書く。3段目の「ワークフローの担当でもフックが走り agent_id が付くか」を、無害な `git commit --dry-run` で確かめるため（手順は .claude/README.md）。既定では書かない
9. **H4 が見る変数**：`ANTHROPIC_…_API_KEY`・`ANTHROPIC_…_AUTH_TOKEN` の形（手元の版にある ANTHROPIC_FOUNDRY_API_KEY なども含む）と、`CLAUDE_CODE_USE_BEDROCK`・`VERTEX`・`FOUNDRY`。値は読まない。systemMessage（利用者）と additionalContext（Claude）の両方に出す
10. **試験の置き場所**：`tests/hooks/test_hooks.py`。`HOOK_PYTHON`（フックを動かす Python）と `HOOKS_TEST_SETTINGS`（入れる前の settings.json の案を試す）で変えられる。試験は本物の state/ に触れない
11. **CLAUDE.md**：design §10.5 の中身に、「手本の ../kyopro-atlas は読むだけ」の1行と、仕組みで止めていることの節（理由と相談の基準。要件 §6.7 の二層）を足した。`check_all.py` は未作成なので「できるまでは、変えたものの試験と検査を個別に流す」と添えた

## 4. 提案

1. **B1（CI）**：必須の検査に `python3 -m unittest discover -s tests/hooks` を足す（ランナーの標準の python3 で。読者の環境に近い）。uv の 3.12 でも流すなら `uv run python -m unittest discover -s tests/hooks`
2. **B1（README.md）**：決まり5の「README にどんなフックと deny ルールが入っているかを書く」のため、`.claude/README.md` を指す1行を足す（例：「このリポジトリには制作用の deny ルールとフックが入っている。中身と読者の環境での動きは .claude/README.md」）。最小の文の決まりに当たるかはメインが判断する
3. **2段目（check_all.py）**：フックの試験を組に入れる。design §8.6 の「sources で断るドメインがすべて deny にあるか」の検査は、`.claude/settings.json` の deny ルールの `WebFetch(domain:…)` を読んで照らす（ドメインの正本を settings.json にする）
4. **メイン（tools/check_noai.py）**：`KNOWN_NOAI` にドメインの一覧の2つ目がある。settings.json の deny ルールから読むか、検査で両者の一致を確かめる
5. **メイン（H2 の範囲を広げる時期）**：`gen_site.py` が nav.yml を生成するようになったら `Edit(/nav.yml)` を足す。`schema/page.schema.json` を生成物としてコミットするなら同じ。overrides/ の生成したデータも置き場所が決まったら足す。足したら試験の例（SettingsTest）も直す
6. **設計書 §10.5 の H3 の文**：実装に合わせて「読むだけの git（status・diff・log・show など、書き込む形のないもの）」にする（3 の決めたことを採るなら）
7. **3段目**：(a) `state/production` と `state/hook-trace` を置き、ワークフローの担当に `git commit --dry-run` を頼んで、止まることと hook-trace.log の agent_id を確かめる。fork の担当も同じに確かめる。(b) worktree で担当を動かす段になったら、H3（印は worktree にない）と commit の役割を決め直す。(c) 動いているメインのセッションにいまの settings.json が効いているかを、hook-trace で確かめる
8. **CLAUDE.md**：`check_all.py` ができたら、「できるまでは…」の文を外す

## 5. 確かめていないこと

1. **Claude Code を起動して確かめていない**（指示のとおり）。フックが実際に呼ばれ、deny が理由付きで返ることは、入力を与えたスクリプトの試験でしか確かめていない
2. **ワークフローの担当と fork の担当でフックが走るか、そのとき agent_id が付くか**（research/28 #4。文書にない）。走らなければ H3 は効かない（代わりは HEAD の比較）
3. **動いているセッション（メインと B1〜B5）に、書いた settings.json が効いているか**。止めない呼び出しではフックは何も出さないので、記録からは分からなかった。実行ファイルには、cloud のセッションが設定の変更を無視する処理があり、セッションの種類で違いうる
4. Claude Code の deny ルールの照らし方：`Edit(/docs/*/index.md)` の `*` が1段だけに当たること、Edit の deny が Write・NotebookEdit と Bash のリダイレクト・tee・sed -i に効くことは、文書（research/28 #10〜#12）によるもので、動かしていない
5. permissionDecisionReason の行数の上限（20行と読んだ）は、実行ファイルの値の並びからの推測。文字数の上限（2000）は同じ表にある
6. SessionStart の systemMessage が、この環境の画面に出るか
7. Python 3.8 での実行（文法だけを確かめた）と、Windows（パスの区切り・PowerShell・Microsoft Store の python3）での動き
8. `$schema` の SchemaStore のスキーマで settings.json を検査していない（取得していない。使っているキーは古くからあるものだけ）
9. 担当がスクリプトの中から動かす git（`python3 -c "subprocess…"` など）・`find -exec git`・変数に入れた URL やコマンドは照らさない。字句の分け方は bash の近似で、`let x=1<<2` のような珍しい形では後ろの行を見落としうる

## 範囲を越えたこと・止められた操作・使用量

- 範囲を越えたこと：なし。書いたのは割り当ての6ファイルと、この報告だけ（ほかに試験のための一時フォルダと scratchpad）。読んだだけのもの：Claude Code の実行ファイルの文字列（入力の形の確かめ）、このセッションの記録のファイル（フックが走った跡の検索）、B3 の textlint（--fix なし。設定の写しは scratchpad）、B1 の uv の環境（`uv run --frozen`）
- 止められた操作：なし
- 使用量：道具の呼び出し 約60回。Web の取得 0回
