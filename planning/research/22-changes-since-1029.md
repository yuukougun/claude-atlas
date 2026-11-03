# 工程2 R1：2026-10-29 以降の変更

- 担当：R1（工程2「調査の補完」）
- 確認日：2026-11-03（この報告の事実はすべてこの日に確かめた。取得は 20:38〜21:10 JST ごろ）
- 手元の Claude Code：2.1.317（`claude --version`）。Claude Code を動かす確認はしていない（brief §4）
- 割り当て：[../batches/step2/README.md](../batches/step2/README.md) の R1

---

## 1. 調べた範囲と方法

### 範囲

1. Claude Code の CHANGELOG の v2.1.312 より後（2.1.314・2.1.316・2.1.317）。各版の日付
2. Help Center のリリースノートの 2026-10-29 以降の項目と、10-29 以降に更新された記事
3. Claude Platform のリリースノートの 2026-10-29 以降の項目と、関わる文書
4. Anthropic のニュース（anthropic.com/news、claude.com/blog）と料金のページ
5. コンテストの分野の 10-29 以降の出来事（ISUCON2026、IEEEXtreme 20.0）。atcoder.jp と codeforces.com は開いていない
6. 上の変更の、requirements §4.2 の分野・00 §5 の台帳（31項目）・requirements §10.1 への影響

### 方法

- CHANGELOG は raw を取得し、v2.1.312 より後の3版の全行（約270行）を読んだ。CHANGELOG には日付がないので、npm の公開記録の時刻（UTC）と、docs の changelog のページの日付で版の日付を確かめた
- 教材に効く変更は、docs の該当のページ（settings-reference・permissions・permission-modes・model-config・sub-agents・env-vars・hooks・context-window・costs・interactive-mode）で裏を取った。docs に載っていないものはそう書いた
- Help Center は、リリースノートに加えて、15のコレクションのページから記事ごとの最終更新の日時を抜き出し、10-29 以降に更新された139本の一覧を作った。10-30 17:08 UTC に一斉に更新されており、多くはプランの名前（Ultra）の置き換えと見た。中身が変わったと見られる13本を読み、ほかに2本を抜き取りで確かめた
- Platform はリリースノートの markdown と、message threads・fast mode・model deprecations の文書を読んだ
- ニュースは一覧のページの日付で、10-29 以降の項目の有無を確かめた
- コンテストは ISUCON の公式ブログを読み、ほかの大会は検索1回で探した。規則は所在（URL と日付）と節の名前だけを書き、条文は要約しない（decisions「書き方の方針（第三者・根拠・コンテスト）」の4）

### 使った一次資料

| 資料 | URL |
| --- | --- |
| Claude Code CHANGELOG | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md （取得は https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md ） |
| Claude Code の docs の changelog（版の日付） | https://code.claude.com/docs/en/changelog |
| npm の公開記録（版の時刻と dist-tags） | https://registry.npmjs.org/@anthropic-ai/claude-code |
| Claude Code の docs | https://code.claude.com/docs/en/ の settings-reference・permissions・permission-modes・model-config・sub-agents・env-vars・hooks・context-window・costs・interactive-mode・settings（それぞれ `.md` で取得） |
| Help Center のリリースノート | https://support.claude.com/en/articles/12138966-release-notes |
| Help Center の記事 | What is the Ultra plan?（17728952）、What is the Max plan?（11049741）、What is the Pro plan?（8325606）、How do usage and length limits work?（11647753）、Claude Fable models on your plan（15424964）、Monthly API credits for Max, Ultra, and Team plans（17154008）、What is a limit reset?（17007452）、Claude Haiku 4.5 was removed from the model selector（17444146）、Manage plugins, skills, and connectors from one Plugins page（17740565）、How large is the context window on paid Claude plans?（8606394）、Use Claude Code with your Pro, Max, or Ultra plan（11145838）、Use the Claude Agent SDK with your Claude plan（15036540）、Claude Code wrap-up allowance（17040437）、Paid plan billing FAQs（8325618）、抜き取り：Use Claude Cowork safely（13364135）、Claude Cowork and chat are one Claude（16761823）。URL はどれも https://support.claude.com/en/articles/<番号> |
| Help Center のコレクション | https://support.claude.com/en/collections/ の15本（記事の更新日の一覧を作るため） |
| 料金のページ | https://claude.com/pricing |
| Platform のリリースノート | https://platform.claude.com/docs/en/release-notes/overview |
| Platform の文書 | https://platform.claude.com/docs/en/build-with-claude/message-threads 、https://platform.claude.com/docs/en/build-with-claude/fast-mode 、https://platform.claude.com/docs/en/about-claude/model-deprecations |
| ニュース | https://www.anthropic.com/news 、https://claude.com/blog |
| ISUCON 公式ブログ | https://isucon.net/ と、まとめ（60124520）・レギュレーション（59966826）・参加規約（59967038）・事前準備（60111629）・結果（60126600）。URL は https://isucon.net/archives/<番号>.html |
| IEEEXtreme | https://ieeextreme.org/rules/ 、https://ieeextreme.org/ |
| GitHub API（ISUCON2026 の問題のリポジトリの有無） | https://api.github.com/repos/isucon/isucon2026 |

### AI の利用を断る指定の確認（`python3 -I tools/check_noai.py`、2026-11-03）

| ドメイン | 確かめた URL | 結果 |
| --- | --- | --- |
| github.com | CHANGELOG の blob の URL | noai・noimageai なし。robots.txt は ClaudeBot などに `/*/raw/` などを Disallow しているが、`/blob/` は対象外 |
| raw.githubusercontent.com | CHANGELOG の raw | なし（robots.txt なし） |
| api.github.com | isucon2026 のリポジトリ | なし（応答は 404） |
| registry.npmjs.org | claude-code | なし |
| code.claude.com | changelog | なし |
| support.claude.com | release notes | なし（meta robots="all"） |
| platform.claude.com | release notes | なし |
| www.anthropic.com | news | なし |
| claude.com | pricing・blog | なし（www.claude.com は claude.com へ転送） |
| isucon.net | トップ | なし |
| ieeextreme.org | rules | なし（meta robots="max-image-preview:large"） |
| x.com | — | 検索の結果に出ただけで開いていない（指定も確かめていない） |
| atcoder.jp・codeforces.com | — | 開いていない |

---

## 2. 結果の一覧

結果の列の語：「正しい／誤り／一部誤り／確かめられない」は調査資料の記述の当否。「古くなった」は 10-29 時点では正しかったが、その後の変更で直す必要があるもの。「空白」は 10-29 より前からあるのに調査資料にないもの。「新しい変更」は 10-29 以降の変更で、調査資料に対応する記述がないもの。「確認（項目なし）」は新しい項目がないことを確かめたもの。出典の確認日はすべて 2026-11-03。CHANGELOG は https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md を指す。

### 2.1 Claude Code の版と日付

| # | 主張とその場所 | 結果 | 正しい内容 | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 1 | 01 冒頭（5行目）「確認時点の最新版 v2.1.312（npm latest/next）、stable は v2.1.308」 | 古くなった | 11-03 時点で npm の latest と next は 2.1.317、stable は 2.1.311。v2.1.312 より後に出たのは、2.1.314（npm 2026-10-30 00:12 UTC。docs の changelog では October 30）、2.1.315（10-30 21:05 UTC。CHANGELOG にも docs にも項目がない）、2.1.316（10-31 00:42 UTC。October 31）、2.1.317（11-02 23:57 UTC。November 3）。2.1.313 は npm にない | https://registry.npmjs.org/@anthropic-ai/claude-code 、https://code.claude.com/docs/en/changelog 、CHANGELOG | 22 changes。鮮度の点検の skill（欠番と、項目のない版がある前提にする）。検証ノートの版の記録 |
| 2 | requirements §7・01 KQ1 の Inferences「2026年1月〜10月末に約235版（v2.0.77 → v2.1.312）」 | 誤り（数え方が合わない。R2 の担当と重なる） | npm の公開記録では、v2.0.77（2026-01-06）から v2.1.312（10-27）までに271版。CHANGELOG の見出しでは同じ範囲で254版。どちらの数え方でも235にならない。11-02 までなら npm で275版 | npm（上と同じ）、CHANGELOG | §10.1 の「リリース数を一つの数字に」。入口や台帳の冒頭で使う数（数値ファイルに置く） |
| 3 | 新しい変更（関わる場所：01 全体の「Requires v…」の書き方） | 新しい変更 | stable の通り道は、ふつう1週間ほど前の版で、大きな退行のある版を飛ばす（docs）。11-03 時点の stable は 2.1.311 なので、下の 2.1.314 以降の変更は stable の読者の手元にはまだない | https://code.claude.com/docs/en/settings-reference （autoUpdatesChannel）、npm の dist-tags | 07 cli。本文の版の下限の書き方。検証ノートに latest と stable のどちらで試したかを書く |

### 2.2 権限・sandbox・hooks・安全

| # | 主張とその場所 | 結果 | 正しい内容 | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 4 | 01 C-3・C-4、requirements §10.1（Read と Edit の deny は子プロセスに効かない） | 新しい変更 | v2.1.314 で `permissions.blockWritesOutsideWorkingDirectories` が入った。Write・Edit・NotebookEdit が、bypassPermissions を含むどの権限モードでも作業ディレクトリの外への書き込みを拒む。シェルのコマンド・MCP の道具・hooks が動かすプログラムは縛らず、docs は sandbox との併用を勧める。どの設定ファイルで true にしても効くので、リポジトリは自分で入れられるが、利用者の設定を外すことはできない。入れると EnterWorktree と ExitWorktree の道具が使えなくなる。読み取り側の `blockReadsOutsideWorkingDirectories` は以前からある | CHANGELOG v2.1.314、https://code.claude.com/docs/en/settings-reference 、https://code.claude.com/docs/en/permissions | 11 enforce・12 safety。§10.1 と同じ限界が公式に明記された。§10.3 の雛形 A-3・A-4 の補強。decisions「危ない雛形を試す場所」で、道具の側の一つの層に使える（シェルは sandbox で塞ぐ） |
| 5 | 01 F-1（hooks の matcher）・01 C-4（sandbox は Monitor にもかかる） | 新しい変更 | v2.1.314 で、Bash に当てた hooks が、Monitor の道具が起動するシェルコマンドにも走るようになった。止める・確認を求めることはできるが、許可や書き換えはできない。hook の `if` の `Monitor(tail *)` は `Bash(tail *)` と同じように当たる。それより前の版では、Bash の hook は Monitor のコマンドを素通しにしていた。11-03 時点で、hooks の docs に Monitor の扱いの記述は見当たらない | CHANGELOG v2.1.314、https://code.claude.com/docs/en/hooks | 11 enforce（縛る経路の抜けの実例。hook の雛形の版の下限）。R7 の「hooks はどこまで効くか」 |
| 6 | decisions「API キー」（`claude -p` に作者の設定を混ぜない）・21 §2.3 | 新しい変更 | v2.1.314 で、`--setting-sources` で外した設定ファイルが、auto mode の規則や保存した許可の同意などの一部の設定をまだ渡していた不具合を直した。v2.1.317 で、`--setting-sources` を使う実行で古い transcript が片付かない不具合も直した | CHANGELOG v2.1.314・v2.1.317 | 雛形の確認は 2.1.314 以上で行い、版を記録する。設定を絞る方法は R7 の担当 |
| 7 | 01 C-4（sandbox）・01 J-1（`--continue`／`--resume`） | 新しい変更 | v2.1.314 で、`claude -p --resume`／`--continue` で入った worktree に sandbox の保護がかからなかった不具合を直した。あわせて `sandbox.excludedCommands` の説明を直した（一つの呼び出しの中のコマンドがすべて一致したときだけ sandbox の外で動く） | CHANGELOG v2.1.314 | 11 enforce・13 delegate（無人の再開の版の下限） |
| 8 | 01 C-3「`/permissions` で … "Recently denied" 確認」 | 古くなった | v2.1.314 でこのタブの名前が Recently blocked になった（docs の permission-modes も Recently blocked）。あわせて、全文を読めない呼び出しは承認させないようにし、auto mode が止めたときの知らせに、コマンドの名前・再試行されること・/permissions で見直せることを出すようにした | CHANGELOG v2.1.307・v2.1.314、https://code.claude.com/docs/en/permission-modes | 07 cli・11 enforce。aliases に旧名を持たせる |
| 9 | 新しい変更 | 新しい変更 | v2.1.317 で、web やシェルの道具の呼び出しがアカウントのメールアドレスをネットワークへ送る前に、確認を求めるようになった | CHANGELOG v2.1.317 | 12 safety（流出の型の例と、その対策が入った版） |
| 10 | 01 E-4（agent teams）、00 §5 台帳の「最初は毎回承認を求められる」の行 | 新しい変更 | v2.1.317 で、tmux や iTerm2 の pane で動く agent team の teammate が、リードが manual のときでも auto mode で始まっていた不具合を直した | CHANGELOG v2.1.317 | 13 delegate・11 enforce（権限モードの受け継ぎを確かめる例と版の下限）。台帳の行の状態は変わらない |
| 11 | 01 C-1（auto mode） | 新しい変更 | auto mode の判定が返らないときの見え方を直した。v2.1.314：判定がないのに「止めた」と表示し /permissions に載せていた。v2.1.316：`claude -p` の出力が、止まった理由を言わないことがあった。クラウドのセッションと予定のタスクが失敗と記録されなかった。v2.1.317：subagent の呼び出しに判定がないとき、本体の画面に何も出なかったので、知らせを出すようにした | CHANGELOG v2.1.314・v2.1.316・v2.1.317 | 21 symptoms（理由を言わずに止まる）・13 delegate（無人の実行の失敗の見分け方） |
| 12 | 01 F-1「既定は fail-open。ポリシーの用途は `onFailure: "block"`（v2.1.295+）」 | 正しい（補足あり） | docs の記述（v2.1.295 以上）と合う。v2.1.317 で、Agent SDK の hook のコールバックにも `onFailure: "block"` が入った。v2.1.316 で、Windows の PowerShell の hook が、型キャスト・`param`・`using`・属性で始まるコマンドでは exit 2 でも止めなかった不具合を直した | https://code.claude.com/docs/en/hooks 、CHANGELOG v2.1.316・v2.1.317 | 11 enforce・15 api（hook が実際に止めるかを確かめる例） |
| 13 | 01 B（managed settings）・02 1-18 | 新しい変更 | v2.1.316 で、Team と Enterprise のログインで Anthropic の API から取った server-managed settings が、承認の確認なしに適用されるようになり、検証できない保存の写しは拒まれるようになった。managed の `autoMode.allow` に `"$defaults"` がないときの扱いも直した（組み込みの例外が戻ってくる不具合、予定のタスクの組み込み規則を消していた点） | CHANGELOG v2.1.316 | 19 team |
| 14 | 01 F-1 | 新しい変更 | v2.1.314 で、PreCompact の hook の出力を hook ごとに1万文字で切るようにした（大きいと圧縮が失敗するか繰り返していた）。docs では、hook の additionalContext などの文字列と標準出力の上限は1万文字で、超えるとファイルに書き、先頭2,000文字の抜粋とパスを Claude に渡す | CHANGELOG v2.1.314、https://code.claude.com/docs/en/hooks | 08 extend・05 context |

### 2.3 コンテキスト

| # | 主張とその場所 | 結果 | 正しい内容 | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 15 | 01 K-1（自動圧縮。放置したときの圧縮の記述がない）、00 §5 台帳「200k を前提にコンテキストを最優先で節約する」の行 | 空白（10-29 より前からある）＋新しい変更 | idle compaction は、端末では v2.1.299（2026-10-14）から既定で有効。会話が既定で 200,000 トークン以上（変えられる）で、1時間の prompt cache のとき、約1時間放置すると cache が切れる前に要約する（2.1.299 の CHANGELOG では約54分）。v2.1.314 で VS Code と Desktop の Code タブにも広がり、テレメトリーを切った契約者と、1時間の cache を有効にした Bedrock・Vertex・Foundry・LLM gateway でも動くようになった。`idleCompaction: false` か /config の行で止める | CHANGELOG v2.1.299・v2.1.302・v2.1.314、https://code.claude.com/docs/en/settings-reference （idleCompaction）、https://code.claude.com/docs/en/context-window 、https://code.claude.com/docs/en/costs | 05 context（/clear と /compact の判断）・16 cost（放置中にも使用量を使う）。台帳の「200k 前提」の行の「今どうするか」に足す |
| 16 | 01 K-1 | 新しい変更 | v2.1.317 で、Read の「前回読んでから変わっていない」という短い返事をやめ、変わっていないファイルを読み直しても中身を返すようにした | CHANGELOG v2.1.317 | 05 context・16 cost（読み直しの分だけ文脈を使う） |
| 17 | requirements §10.1「圧縮の後に残るものの完全な一覧は公式の context-window にある」 | 正しい（補足あり） | context-window のページに、圧縮の後に残るものの節がある。v2.1.317 で、大きな CLAUDE.md が前回の送信から変わったセッションで自動圧縮の後に "Prompt is too long" になる不具合と、圧縮が自分の要求を縮めたときに以前の要約を失う不具合を直した | https://code.claude.com/docs/en/context-window 、CHANGELOG v2.1.317 | 21 symptoms（圧縮の後に約束を忘れる・続けられない）・05 context |
| 18 | 00 §2 の原因①「見えていない」 | 新しい変更 | v2.1.317 で、Grep と Glob の検索が時間切れで途中までしか返さなかったのに、Claude がそれを全部の結果とみなしていた不具合を直した | CHANGELOG v2.1.317 | 01 basics・09 verify・21 symptoms（「ない」と言い切られたら検索の打ち切りを疑う例） |

### 2.4 モデルと effort

| # | 主張とその場所 | 結果 | 正しい内容 | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 19 | 01 L-2（Fast mode）・02 5-8（Opus 5.5 は 10-15 に research preview を終了） | 正しい（補足あり） | Platform（10-30）と Claude Code v2.1.316：Opus 4.8 の fast mode を 10-30 に非推奨とし、11-30 に削除する。削除の後は標準の速度に戻らずエラーになる。続けるには Opus 5.5 へ移る（Opus 5 の fast mode は research preview のまま）。fast mode の料金は、Opus 5.5 が入力 $8・出力 $40、Opus 5 と 4.8 が $10・$50（MTok あたり） | https://platform.claude.com/docs/en/release-notes/overview 、https://platform.claude.com/docs/en/build-with-claude/fast-mode 、CHANGELOG v2.1.316 | 03 models・16 cost・数値ファイル（11-30 に確かめ直す） |
| 20 | 00 §5 台帳の4行目（think → think hard → ultrathink）・01 L-2「ultrathink はそのターンだけ深い推論を要求するキーワード。think hard は認識されない」 | 正しい（補足あり） | docs（model-config）：ultrathink はそのターンに深い推論を頼むキーワードで、think hard などのほかの言い回しは普通の文として渡る。加えて、端末で打つとそのターンを xhigh に上げられる（v2.1.311 以上。Anthropic の API の Opus 5.5・Sonnet 5.5・Haiku 5.5・Fable 5.1 で。上げられるときは虹色で表示）。v2.1.316 で VS Code も同じ動きになり、`CLAUDE_CODE_DISABLE_ULTRATHINK` で切れるようになった。この環境変数は 11-03 時点で env-vars のページにない | https://code.claude.com/docs/en/model-config 、CHANGELOG v2.1.311・v2.1.316・v2.1.317、https://code.claude.com/docs/en/env-vars | 03 models・04 prompting・台帳4行目の「今どうするか」の文。§10.1 の think hard の言い方の直しとも合う |
| 21 | 01 E-1・L-2（subagent の `effort` frontmatter）、requirements §10.1（Sonnet 5.5 の既定 effort の食い違い） | 新しい変更 | v2.1.316 で `CLAUDE_CODE_SUBAGENT_EFFORT`（ほかに指定がないときに subagent が動く effort）を足した。v2.1.317 で、メインの会話と違うモデルで動く subagent と teammate は、セッションの effort を受け継がず、そのモデルに保存した effort か、そのモデルの既定で動くようになった。11-03 時点で、docs の sub-agents と env-vars にはこの2つの記述がない | CHANGELOG v2.1.316・v2.1.317、https://code.claude.com/docs/en/sub-agents | 03 models・13 delegate・16 cost（「subagent に `model: haiku`」の勧めは Haiku の既定の effort で動く）。§10.1 の食い違いが subagent にも効くようになる |
| 22 | 01 L-2・02 1-18 | 新しい変更 | v2.1.314 で、組織の管理者がモデルの effort に上限をかけているときに "Invalid effort level" で失敗し続けた不具合を直し、effort を下げて再試行し、使う段を知らせるようにした。v2.1.317 で、アプリが先に立ち上げたセッション（Desktop の Code タブの新しいセッションなど）で project の `effortLevel` が無視される不具合を直した | CHANGELOG v2.1.314・v2.1.317 | 19 team・03 models |
| 23 | 02 3-7（旧モデルの退役。アプリは 01-16 に Opus 4／4.1 を外した） | 新しい変更 | 10-29 に、アプリ（chat・Cowork・Design。Free・Pro・Max の各プラン。Desktop と Mobile を含む）のモデルの選択肢から Haiku 4.5 を外し、Haiku 5.5 に置き換えた（10-15 に告知）。Claude Code・Team と Enterprise・API には残る。Haiku 4.5 で始めた会話の続きは Haiku 5.5 が答える | https://support.claude.com/en/articles/17444146-claude-haiku-4-5-was-removed-from-the-model-selector （記事の更新 2026-10-29） | 03 models・06 app・数値ファイル |

### 2.5 無人の実行・並列・予定

| # | 主張とその場所 | 結果 | 正しい内容 | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 24 | 01 J-1（`claude -p`） | 新しい変更 | v2.1.314 で、起動に失敗しても何も出さず終了コード 0 で終わっていた不具合を直し、エラーを出して 1 で終わるようにした。v2.1.317 で、ディスクやクォータが一杯で transcript か `~/.claude.json` の書き込みを失ったときも、エラーを出して 1 で終わるようにした（text と json の出力。NFS では漏れうると書かれている） | CHANGELOG v2.1.314・v2.1.317 | 09 verify・13 delegate。終了コードだけで成功を決める CI は、2.1.314 より前では起動の失敗を見逃した（「確かめる」の実例と版の下限。10 eval の例にも使える） |
| 25 | 01 P-1・J-1 | 新しい変更 | v2.1.317 で、クラウドや self-hosted runner のセッションの中で動かした `claude -p` が、そのセッションの ID と transcript を共有していた不具合を直した（再起動で別の会話を再開しうる）。`CLAUDE_CODE_DISABLE_NESTED_SESSION_ID=1` で前の動きに戻せる | CHANGELOG v2.1.317 | 13 delegate（入れ子の実行） |
| 26 | 01 M-1・O-1、05 1-12（記述なし） | 空白（v2.1.234 からある）＋修正 | 「Continue automatically at usage limit」（設定は `autoContinueAtUsageLimit`。v2.1.234＝2026-08-17 から既定で有効）は、claude.ai の上限で止まった作業を、開いたままのセッションで待ち、リセットの後に自動で続ける。docs では、自動の継続は3回で止まる（/goal と、セッションの予定のタスクも同じ）。続けた作業でも許可の確認は出る。v2.1.314 で、待ちの間に作業が自分で再開した場合（/goal のチェックイン、背景や予定のタスク）に3回を超えて続けていた不具合を直した | https://code.claude.com/docs/en/interactive-mode 、https://code.claude.com/docs/en/settings-reference 、CHANGELOG v2.1.234・v2.1.314 | 13 delegate・16 cost。decisions「ワークフロー」の再開の決まり（format-and-operations F15） |
| 27 | 01 O-3（cloud scheduled tasks） | 新しい変更 | v2.1.317 で、/schedule で作った新しいクラウドの予定のタスクに、頼んでいない connector が付いたときに警告し、外し方を示すようにした | CHANGELOG v2.1.317 | 12 safety・13 delegate（予定のタスクの最小権限を確かめる） |
| 28 | 01 E-2〜E-5 | 新しい変更 | 並列の小さな変更。SendMessage が走行中の背景エージェントに早く届くようになった（実行中のコマンドを止めずに背景へ移す。v2.1.317）。プロンプトの入力を消すための Ctrl+C が背景エージェントを全部止めていた不具合を直した（v2.1.317）。背景とクラウドのセッションで切った Ultracode が次の起動で戻る不具合を直した（v2.1.314）。多くの subagent を使う headless のターンで、親が subagent の道具の結果をターンの終わりまで持たなくなった（v2.1.314） | CHANGELOG v2.1.314・v2.1.317 | 13 delegate（影響は小さい。版の下限に使う程度） |
| 29 | 01 D-2・H-1 | 新しい変更 | v2.1.317 で、claude.ai から同期した skills が、ディスクに書けないときに失われるか10分ごとに取り直されていた不具合を直した。組み込みの `plugin-authoring` skill が、作った mod が動いた後に一度だけ共有の手伝いを申し出るようになった | CHANGELOG v2.1.317 | 08 extend（影響は小さい） |
| 30 | requirements §7（点検の手順） | 新しい変更 | 11-03 時点で、CHANGELOG にある `CLAUDE_CODE_SUBAGENT_EFFORT`・`CLAUDE_CODE_DISABLE_ULTRATHINK`・`CLAUDE_CODE_DISABLE_NESTED_SESSION_ID` は env-vars のページになく、Monitor と hooks の関係は hooks のページにない。一方、`blockWritesOutsideWorkingDirectories`・Recently blocked・idle compaction の VS Code と Desktop への広がりは docs に入っている | https://code.claude.com/docs/en/env-vars 、https://code.claude.com/docs/en/hooks 、CHANGELOG | 鮮度の点検は CHANGELOG と docs の両方を見る。docs にないものは CHANGELOG の版で書く |

### 2.6 Help Center とプラン

| # | 主張とその場所 | 結果 | 正しい内容 | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 31 | requirements §7（点検の手順）・02 1-0（年表の出典がリリースノート） | 確認（項目なし） | Help Center のリリースノートの最新の項目は 10-21（Claude Duet）で、10-29 以降の日付の項目はない（ページの更新は 10-30 21:51 UTC）。下の Ultra・Haiku 4.5・Plugins の変更は、リリースノートではなく個別の記事にだけある | https://support.claude.com/en/articles/12138966-release-notes | 鮮度の点検は、リリースノートに加えて記事の更新日も見る |
| 32 | 02 2-1「Max：5x が月$100、20x が月$200。Pro に比べ session あたり5倍または20倍」・04 の円換算（Max 5x／Max 20x） | 古くなった | 10-30 に旧 Max 20x は Ultra に改名され、契約者は料金を変えずに自動で移った。Max は $100 の一つだけで、Pro の5倍を5時間ごとと週ごとに持つ。Ultra は $200（月払いだけ）で、週あたり Pro の10倍、確認済みの口座には5時間の上限がない。確認は口座と支払いの履歴などから自動で行い、まだのときは一時的な上限がかかる（Settings > Usage に Current session の棒がなければ確認済み）。電話番号の確認は別のもので、この上限を外さない | https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan （更新 10-30）、https://support.claude.com/en/articles/11049741-what-is-the-max-plan （更新 10-30）、https://claude.com/pricing | 16 cost・数値ファイルのプランの表。decisions「作者のプラン：Max」（旧 20x なら今は Ultra） |
| 33 | 02 2-2・00 分野14の本文「有料プランには5時間の session limit と週の limit の2層があり、claude.ai・Claude Code・Desktop で共有」・05 1-12 | 古くなった（一部） | 共有の部分は変わらない。2層の部分は、確認済みの Ultra の口座では週の上限だけになった。週の上限は全モデルにかかり、Max と Ultra には Fable の別の上限（週の上限の半分まで）がある。呼び方は、Help Center が five-hour limit、Claude Code が v2.1.312 から 5-hour limit（それまでは session limit） | https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work （更新 10-30）、CHANGELOG v2.1.312 | 16 cost・21 symptoms（上限の症状の文と aliases） |
| 34 | 02 2-4「Fable は Max と premium seat で週上限の50%まで（追加枠ではない）。Pro と standard seat は usage credits」 | 正しい（Ultra を足す） | Fable の記事（10-30 更新）でも同じ仕組みで、対象に Ultra が加わった。Claude Code で使うには、Fable 5 は v2.1.170 以上、Fable 5.1 は v2.1.255 以上 | https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan | 16 cost・数値ファイル |
| 35 | 02 2-1「Max の API credits：5x に$100、20x に$200」 | 古くなった（名前だけ） | 月の API credits は、Max $100、Ultra $200、Team は standard $20・premium $100 を席ごとに合わせて月 $500 まで。Free・Pro・Enterprise は対象外。プランに7日いてから受け取れる。リンクできる Console の組織は一つで、自分では変えられない | https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans | 16 cost・15 api。21 §2.3 の「Max の API credits」（R5 の担当） |
| 36 | 02 2-2・05 1-12（記述なし） | 確かめられない（導入の時期） | Wrap-Up Allowance：Claude Code が応答の途中で5時間の上限に達したとき、区切りまで少しだけ続ける（画面に「Usage limit reached · wrapping up」と出る）。Pro は週に一度まで、Max・未確認の Ultra・Team の premium seat は5時間の上限に当たるたび。使った分は週の上限に数える。v2.1.277 以上で、API キーや Bedrock・Vertex では効かない。段階的に展開中。記事に日付がなく、いつ入ったかは確かめられない | https://support.claude.com/en/articles/17040437 、https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan | 16 cost・13 delegate |
| 37 | requirements §10.4「`ANTHROPIC_API_KEY` と課金経路の関係」（R5 の担当） | 空白（答えの手がかり） | Help Center（10-30 更新）：環境変数 `ANTHROPIC_API_KEY` があると、Claude Code はプランではなくその API キーで認証し、API の料金になる。Agent SDK の記事：プランでログインしているときは、SDK と `claude -p` もプランの上限から引く。月の API credits は、リンクした Console の組織の API キーで SDK・`claude -p`・Managed Agents を動かすときに使える | https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan 、https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan | 16 cost（課金経路の確かめ方）。decisions「API キー」の方針の裏付け。R5 に渡す |
| 38 | 02 1-10「Customize > Skills からアップロード」「Customize > Plugins の Discover タブ」・02 1-0（02-24/25 の Customize） | 古くなった（展開中） | 10-29 から Free・Pro・Max・Ultra・Team に順に展開し、11-09 に一般提供、Enterprise は 11-30 から既定で有効。サイドバーなどの Customize は Plugins という名前になり、一つの Plugins のページが Skills・Connectors・Plugins のタブに代わる（skill と connector で絞り込める）。skill は「+」か「/」で使う。11-30 から、Skills を切った Team と Enterprise の組織では Desktop の plugins も止まる | https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page （更新 10-30） | 06 app（画面の名前）・19 team。台帳の新しい行の候補（§3.4） |

### 2.7 Claude Platform（API）とニュース

| # | 主張とその場所 | 結果 | 正しい内容 | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 39 | 01 M-1「Console はワークスペース上限と Analytics API」 | 新しい変更 | Platform 10-29：Usage and Cost Analytics API（beta、`analytics-usage-cost-2026-08-24`）を出した。`/v1/organizations/analytics/usage` と `/cost` で、Console と Enterprise の組織のトークンと費用を、モデル・workspace・API キー・利用者などで絞って集計できる。前の Usage and Cost API と、Enterprise Analytics API の usage・cost の報告は legacy になった（サポートは続く）。Claude Code v2.1.317 の Claude apps gateway の費用の報告も同じ `GET /v1/organizations/analytics/cost` | https://platform.claude.com/docs/en/release-notes/overview 、CHANGELOG v2.1.317 | 16 cost・19 team |
| 40 | requirements §6.6 の比喩「毎回読み直す受験者（全履歴の送信）」・02 5-1・5-2 | 新しい変更（比喩は保てる） | Platform 11-02：message threads（beta、`message-threads-2026-08-12`）。最初に会話全体を送り、その後は新しいメッセージと直前の応答の id だけを送る。API はモデルを呼ぶ前に会話を組み立て直すので、モデルが読む量は変わらず、料金と rate limit も変わらない。prompt caching は自分で指定する。スレッドは最後の要求から5分で切れ、最後に使ってから1時間以内に消える（メモリにだけ置く）。足すだけの形なので、圧縮するには要約から新しいスレッドを始める。ZDR と HIPAA の対象外 | https://platform.claude.com/docs/en/release-notes/overview 、https://platform.claude.com/docs/en/build-with-claude/message-threads 、https://claude.com/blog （11-02 の記事） | 15 api・01 basics（「毎回全体を読む」の説明は保ち、「送る」のは差分にできると添える）・12 safety（ZDR の対象外） |
| 41 | 02 3-7「Sonnet 4.5 は 2026-11-30 に退役予定」 | 正しい | model deprecations のページでも 11-30 に退役のまま。10-29 以降に、新しい非推奨・退役の告知はない（#19 の fast mode を除く） | https://platform.claude.com/docs/en/about-claude/model-deprecations | 03 models・数値ファイル（11-30 に確かめ直す） |
| 42 | 02 5章（記述なし） | 空白（10-21・10-28。10-29 より前） | Platform 10-21：API の版 `2026-10-21` を出した。この版では `temperature`・`top_p`・`top_k` を送ると 400 になる（前の版でも、Claude 4.7 以降のモデルに既定以外の値を送ると 400）。docs は、引数を外して指示で振る舞いを導くよう勧める。新しい SDK と ant CLI はこの版を既定で送り、ライセンスが MIT から Apache 2.0 になった。10-28：Messages API と Token Counting API の要求の大きさの上限を 32 MB から 128 MB に上げた | https://platform.claude.com/docs/en/release-notes/overview 、https://platform.claude.com/docs/en/about-claude/model-deprecations | 15 api・04 prompting。台帳の新しい行の候補（§3.4） |
| 43 | 02 3-2（リリース年表）・02 2-1（料金） | 確認（項目なし） | anthropic.com/news の一覧の最新は 10-28（AI for Science の拡大）。10-29〜11-03 に、モデル・料金・プラン・利用上限の発表の記事はない。Ultra の発表の記事も、anthropic.com/news と claude.com/blog の一覧には見当たらない（一次資料は Help Center と料金のページ）。claude.com/blog の 10-29 以降は、11-02 の message threads の記事だけ | https://www.anthropic.com/news 、https://claude.com/blog | 03・16。鮮度の点検で見る順（Help Center の記事 → 料金のページ → ニュース） |
| 44 | 02 2-1（旧 Max 20x の上限） | 確かめられない | 「旧 Max 20x の週の上限はもともと Pro の10倍で、20倍だったのは5時間の上限だけ。だから Ultra の週の上限は変わらない」という説明が X の投稿にあると、検索の要約が示した。投稿は開いておらず、投稿者も確かめていない。Help Center と料金のページは「料金は変わらない」とだけ書き、週の上限が前と同じかは書いていない。調査資料にも旧 20x の週の倍率はない | WebSearch の結果（2026-11-03）。一次資料なし | 16 cost（Ultra で使える量が減ったか同じかを、本文で断定しない） |

### 2.8 コンテストの分野

| # | 主張とその場所 | 結果 | 正しい内容 | 出典 | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 45 | 10 第1部（ISUCON13・14・2026 の規約は、AI によるコードの分析と生成を許可される行為として明記）・10 付録の「大会規約の版」と「ISUCON2026 当日マニュアルの AI 記述：未取得」・11 C-8・requirements §10.5 | 正しい（所在を確かめた。条文は要約しない） | ISUCON2026 は 2026-10-31（土）10:00〜18:00 に開かれた（まとめの記事は 10-31 15:36。856チーム、うち学生83、参加者1,596人）。レギュレーション（2026-07-28 12:43 公開）の「サーバー事項」と「禁止事項」の節に、AI の利用の項目がある。10 の記述はこの所在と合う。結果は 11-02 16:45 公開。問題の解説と講評・イベントレポートは 11-03 時点で準備中。当日マニュアルは見ていない（公開の場所が分からない）。問題のリポジトリ isucon/isucon2026 は、11-03 時点で GitHub の API が 404 を返す | まとめ https://isucon.net/archives/60124520.html 、レギュレーション https://isucon.net/archives/59966826.html 、参加規約（2026-07-28 12:39）https://isucon.net/archives/59967038.html 、結果 https://isucon.net/archives/60126600.html | 20 contest（数値ファイルの規則の版と確認日。講評が出たら確かめ直す） |
| 46 | 新しい変更 | 新しい変更 | IEEEXtreme 20.0 は 2026-10-31 に、UTC で24時間行われた。規則のページに「AI-Permitted and AI-Prohibited Tasks」という AI の利用の節がある（ページの時刻は 2026-10-30T22:38:35+00:00。更新日とは書かれていない）。11-03 時点で 20.0 の順位は載っていない | https://ieeextreme.org/rules/ 、https://ieeextreme.org/ （WebFetch で読んだ） | 20 contest（規則の類型の例の候補。使うなら設計で規則の原文を読む） |
| 47 | 新しい変更（17 japanese） | 確認（項目なし） | 3版の CHANGELOG に、日本語の出力や IME を名指しした変更はない。近いものは、VS Code の音声入力のショートカットが非ラテン文字の配列（ロシア語・ギリシャ語・ヘブライ語）で効かなかった不具合の修正（v2.1.314）と、見えない文字を含むプロンプトが2回目の Enter まで送られなかった不具合の修正（v2.1.316）だけ | CHANGELOG v2.1.314・v2.1.316 | 17 japanese（第一波の「日本語で使う」の核への影響はない） |

**件数**：正しい7（うち補足や追記が要るもの5：#12・#17・#19・#20・#34）、誤り1、古くなった6、空白4、確かめられない2、新しい変更24、確認（項目なし）3。計47。

---

## 3. 新しく分かったこと

### 3.1 版と日付（v2.1.312 より後）

| 版 | npm の公開（UTC） | docs の changelog の日付 | 主な中身 |
| --- | --- | --- | --- |
| 2.1.313 | （npm にない） | （なし） | 欠番 |
| 2.1.314 | 2026-10-30 00:12 | October 30, 2026 | `blockWritesOutsideWorkingDirectories`、Monitor と Bash の hook、`--setting-sources` の漏れの修正、`-p --resume` の worktree の sandbox の修正、Recently blocked、idle compaction の VS Code と Desktop への広がり、`claude -p` の終了コード、PreCompact の hook の出力の上限 |
| 2.1.315 | 2026-10-30 21:05 | （項目なし） | CHANGELOG にも docs にも項目がない |
| 2.1.316 | 2026-10-31 00:42 | October 31, 2026 | Opus 4.8 の fast mode の非推奨、`CLAUDE_CODE_DISABLE_ULTRATHINK`、`CLAUDE_CODE_SUBAGENT_EFFORT`、VS Code の ultrathink、server-managed settings |
| 2.1.317 | 2026-11-02 23:57 | November 3, 2026 | メールアドレスを送る前の確認、SDK の hook の `onFailure: "block"`、subagent の effort、Read の短い返事の廃止、Grep と Glob の打ち切り、teammate の auto mode の不具合、`/schedule` の connector の警告 |

npm の dist-tags（11-03）：latest と next が 2.1.317、stable が 2.1.311。docs の changelog の日付は npm の UTC の日付とずれることがある（2.1.317）。

### 3.2 教材に特に効く変更

1. **プラン**：旧 Max 20x が Ultra に改名された（10-30）。確認済みの Ultra の口座は5時間の上限がなく週の上限だけになり、「有料プランは5時間と週の2層」が条件付きになった（#32・#33）。リリースノートにもニュースにも載っておらず、Help Center の記事と料金のページだけにある（#31・#43）
2. **縛る**：書き込みを作業ディレクトリに閉じる公式の鍵（#4）が入り、Bash の hook が Monitor の道具を素通しにしていた抜けが塞がれた（#5）。どちらも「道具の側の鍵はシェルや子プロセスに効かないので sandbox と併用する」という §10.1 の論点の実例になる
3. **確かめる**：2.1.314 より前は、`claude -p` が起動に失敗しても終了コードが 0 だった（#24）。検索の打ち切りを全部と取り違える不具合もあった（#18）。どちらも「完了は証拠で決める」の例と、版の下限の書き方の例に使える
4. **effort**：ultrathink がそのターンを xhigh に上げるようになり（#20）、別のモデルの subagent はそのモデルの既定の effort で動くようになった（#21）
5. **文脈**：idle compaction（#15）は 10-29 より前からあるのに調査資料になかった。Read の読み直しが中身を返すようになった（#16）
6. **API**：message threads（#40）は送る量を減らすだけで、モデルが毎回全体を読むことと料金は変わらない。requirements §6.6 の比喩はそのまま使える
7. **鮮度の仕組み**：変更の在り処が分かれている（リリースノートに載らない Help Center の変更、docs に遅れて入る CHANGELOG の変更、CHANGELOG のない版と欠番、stable の遅れ）。§7 の点検の手順は、これを前提にする必要がある（#1・#3・#30・#31）

### 3.3 requirements §4.2 の分野への影響

| 分野 | 関わる行 |
| --- | --- |
| 00 start・01 basics | #2（入口の数）・#18・#40 |
| 02 surfaces | #3（stable）・#15・#20（VS Code と端末の差が縮んだ）・#38 |
| 03 models | #19・#20・#21・#22・#23・#41 |
| 04 prompting | #20・#42 |
| 05 context | #14・#15・#16・#17 |
| 06 app | #23・#38 |
| 07 cli | #1・#3・#8 |
| 08 extend | #5・#12・#14・#29 |
| 09 verify | #11・#18・#24 |
| 10 eval | #24（例として） |
| 11 enforce | #4・#5・#6・#7・#8・#10・#12 |
| 12 safety | #4・#9・#27・#40 |
| 13 delegate | #7・#10・#11・#21・#24・#25・#26・#27・#28・#36 |
| 14 judgment | なし |
| 15 api | #12・#19・#39・#40・#42 |
| 16 cost | #15・#16・#19・#21・#26・#32〜#37・#39・#44 |
| 17 japanese | #47（影響なし） |
| 18 recipes | なし |
| 19 team | #13・#22・#38・#39 |
| 20 contest | #45・#46 |
| 21 symptoms | #11・#17・#18・#33 |
| 22 changes | #1・#2、§3.4 の台帳の候補 |

第一波（D10 と「日本語で使う」の核）では、台帳（§3.4）、症状辞典（#11・#17・#18・#33）、評価と実験の核（#24 を例に使える）、入口（#2 の数と #32 のプラン）に関わる。判断と理解の核と、日本語で使うの核に関わる変更はない。

### 3.4 00 §5 の古くなった助言の台帳（31項目）への影響

**影響がある行（3行）**

| 行 | いまの「今どうするか」 | 足す内容 | 状態 |
| --- | --- | --- | --- |
| 4：think → think hard → ultrathink、日本語の「熟考」 | effort で調整する。ultrathink だけが1ターンの深い推論として有効 | ultrathink は端末（v2.1.311 以上）と VS Code（v2.1.316 以上）でそのターンを xhigh に上げる。`CLAUDE_CODE_DISABLE_ULTRATHINK`（v2.1.316）で切れる（#20） | 置換のまま |
| 6：`--dangerously-skip-permissions` で YOLO 運用 | auto mode と sandbox。bypass は隔離環境だけ | 補足：`permissions.blockWritesOutsideWorkingDirectories`（v2.1.314 以上）は bypass でも Write・Edit・NotebookEdit の作業ディレクトリの外への書き込みを止めるが、シェルは止めないので隔離の代わりにはならない（#4） | 置換のまま |
| 8：200k を前提にコンテキストを最優先で節約する | 1M と自動圧縮。質とコストのために /clear する | 長く放置した大きな会話は idle compaction で要約される（端末 v2.1.299 以上、VS Code と Desktop v2.1.314 以上。止められる）（#15） | 条件付きのまま |

**影響がない行（28行）**：10-29 以降の変更で状態が変わったものはない。7行目（最初は毎回承認）は #10 の不具合の修正があるが、行の内容は変わらない。

**足す候補**

| 古い助言 | 今どうするか | 変化の時期 | 状態 | 出典 | 優先度の見立て |
| --- | --- | --- | --- | --- | --- |
| Max は 5x と 20x から選ぶ | Max（Pro の5倍）か Ultra（旧 Max 20x。週に Pro の10倍、確認済みの口座は5時間の上限なし） | 2026-10-30 | 置換（改名） | [What is the Ultra plan?](https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan) | 高（プランの名前で引かれる。旧名の記事が多い） |
| 有料プランは5時間の上限に当たったら待つしかない | Ultra の確認済みの口座は週の上限だけ。ほかの有料プランは5時間と週の2層のまま。上限のときは usage credits か、Claude Code の自動の継続（3回まで）も選べる | 2026-10-30（自動の継続は v2.1.234） | 条件付き | [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)、[Interactive mode](https://code.claude.com/docs/en/interactive-mode) | 中 |
| Customize の Skills・Connectors・Plugins の各タブで管理する | 一つの Plugins のページで管理する（サイドバーの名前も Plugins） | 2026-10-29〜11-09（Enterprise は 11-30） | 置換 | [Manage plugins, skills, and connectors from one Plugins page](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page) | 中（画面の名前。11-09 の一般提供の後に確かめ直す） |
| temperature（や top_p・top_k）を下げて出力を安定させる | 引数を外し、指示で振る舞いを導く。Claude 4.7 以降のモデルは既定以外の値で 400、API の版 2026-10-21 では引数ごと削除 | 2026-10-21（4.7 以降の制限がいつ始まったかは未確認） | 撤回 | [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations) | 高（API の古い記事に多い。10-29 より前の変更だが調査資料にない） |

台帳ではなく数値ファイルと aliases で持つのがよいもの：Opus 4.8 の fast mode（11-30 に削除、#19）、アプリの Haiku 4.5（10-29 に削除、#23）、`/permissions` の Recently denied → Recently blocked（#8）、session limit → 5-hour limit（#33）。

### 3.5 requirements §10.1 の既知の誤りとの関わり

| §10.1 の項目 | 10-29 以降の変更 |
| --- | --- |
| 01 の「埋まるほど性能が落ちる」 | 関わる変更なし |
| output style の組み込みは4種 | 3版に変更なし |
| Stop hook は8回で上書き | 3版に変更なし |
| `Write(path)`・`NotebookEdit(path)`・`Glob(path)` は何にも当てはまらない | #4 の新しい鍵が、作業ディレクトリ単位の境界を Write・Edit・NotebookEdit にかける公式の手段になった。パス単位で縛るのは Edit と Read のまま |
| Read と Edit の deny は子プロセスに効かない。sandbox と併用 | #4 の docs も同じ限界を明記した。#5 の Monitor の件も、縛る経路の抜けの同じ型 |
| 圧縮の後に残るものの一覧 | #14・#17（圧縮の不具合の修正と、hook の出力の上限） |
| agent teams の約7倍 | 変更なし |
| Sonnet 5.5 の既定 effort の食い違い | #21 で、別のモデルの subagent はそのモデルの既定の effort で動くようになり、食い違いの影響が subagent にも及ぶ |
| think hard の言い方 | #20（11-03 の docs の言い方は §10.1 の直しと合う） |
| リリース数を一つの数字に | #2（npm で271版、CHANGELOG で254版） |

### 3.6 decisions.md に関わること

- **作者のプラン**（工程1の回答「Max」。5x か 20x かは聞いていない）：旧 Max 20x なら、10-30 から Ultra に自動で移っている（料金は同じ。確認済みの口座なら5時間の上限がない）。制作のワークフローの規模と、上限で止まったときの再開の決まり（F15）の見積もりに関わる（#32・#33）
- **雛形の動作確認**と**API キー**：`--setting-sources` の漏れが 2.1.314 で直ったので、設定を絞った `claude -p` の確認は 2.1.314 以上で行うのが安全（#6）。`ANTHROPIC_API_KEY` があると課金がプランから API に移ることが Help Center に明記されている（#37）。API キーを使わない方針の裏付けになる
- **危ない雛形を試す場所**：#4 の鍵を使えば、使い捨てのフォルダの外への Write・Edit を道具の側で止められる。シェルは sandbox（bubblewrap と socat）で塞ぐ
- **ワークフロー**：自動の継続（#26）は3回で止まる。無人で長く回すときの再開の決まりに入れる

### 3.7 10-29 より前の変更で、調査資料に見当たらないもの（手がかり）

- idle compaction（v2.1.299、10-14）（#15）と、自動の継続の設定（v2.1.234、08-17）（#26）
- API の版 2026-10-21 での `temperature`・`top_p`・`top_k` の削除、SDK のライセンスの変更、要求の大きさの上限の引き上げ（#42）
- anthropic.com/news の 10-22「Donating Agent Skills to the Agentic AI Foundation」（Agent Skills の標準を財団に移す）。一覧の題と要約を見ただけで本文は読んでいない。01 D-2 の「オープン標準 Agent Skills（agentskills.io）準拠」に関わる
- claude.com/blog の 10-22「Building agents: When to fold subagents into your main agent loop」（API でエージェントを作るとき、subagent を減らして文脈と道具を段階的に見せるほうがよい場合がある、という趣旨の要約）。題と要約だけを見た。台帳の12・13行目（subagent を使え／工程ごとに大量に作る）の根拠に使えるかもしれない
- claude.com/blog の 10-28「Smart reports, surveys, and pooled group budgets for Claude Enterprise」（題だけ。CLI v2.1.316 の gateway の pooled group budgets と関わる）

---

## 4. 提案

ファイルを変えるのはメインの判断に任せる。直した文は案である。

### 4.1 調査資料

| ファイル・場所 | 直し方 | 直した文（案） |
| --- | --- | --- |
| 01 冒頭（5行目） | 注記を足す | 「（2026-11-03 追記）latest と next は v2.1.317（npm 2026-11-02 23:57 UTC）、stable は v2.1.311。v2.1.312 より後の変更は research/22 にまとめた」 |
| 01 C-3「管理」 | 置き換える | 「"Recently denied" 確認」→「Recently blocked のタブで確認する（v2.1.314 で Recently denied から改名）」 |
| 01 C-3 の末尾 | 1項目を足す | 「**作業ディレクトリの外への書き込みを止める**：`permissions.blockWritesOutsideWorkingDirectories`（v2.1.314 以上）で、Write・Edit・NotebookEdit が、bypassPermissions を含むどの権限モードでも作業ディレクトリの外を拒む。シェル・MCP・hooks の動かすプログラムは縛らないので sandbox と併用する。読み取りは `blockReadsOutsideWorkingDirectories`」 |
| 01 F-1「matcher と終了コード」 | 追記する | 「v2.1.314 以上では、Bash に当てた hook は Monitor の起動するシェルコマンドにも走る（止める・確認を求めるだけで、許可と書き換えはできない）。それより前の版では素通しだった。PreCompact の hook の出力は hook ごとに1万文字で切られる（v2.1.314）。Agent SDK の hook のコールバックも `onFailure: "block"` を持てる（v2.1.317）」 |
| 01 K-1 | 1項目を足す | 「**idle compaction**：大きな会話（既定 200,000 トークン以上）を約1時間放置すると、1時間の prompt cache が切れる前に要約する。端末は v2.1.299、VS Code と Desktop の Code タブは v2.1.314 から。`idleCompaction: false` か /config で止める」 |
| 01 L-2「Thinking」 | 追記する | 「ultrathink は、端末では v2.1.311、VS Code では v2.1.316 から、そのターンを xhigh に上げる（Anthropic の API の 5.5 系と Fable 5.1）。`CLAUDE_CODE_DISABLE_ULTRATHINK`（v2.1.316）で切れる」 |
| 01 L-2「概要」（effort） | 追記する | 「v2.1.317 から、メインの会話と違うモデルで動く subagent と teammate は、そのモデルに保存した effort か、そのモデルの既定で動く。`CLAUDE_CODE_SUBAGENT_EFFORT`（v2.1.316）で、指定のない subagent の effort を決められる」 |
| 01 L-2「Fast mode / Advisor」 | 追記する | 「Opus 4.8 の fast mode は 2026-10-30 に非推奨、11-30 に削除（エラーになり、標準の速度に戻らない）」 |
| 01 J-1 | 追記する | 「v2.1.314 より前は、起動に失敗しても出力なしで終了コード 0 だった。v2.1.317 からは、transcript の書き込みを失ったときも 1 で終わる」 |
| 02 2-1 の Max の項 | 置き換える | 「Max：月$100（web の価格、月払いのみ）。Pro の5倍を5時間ごとと週ごとに持つ。Ultra（2026-10-30 に旧 Max 20x を改名。契約者は料金そのままで移った）：月$200（月払いのみ）。週あたり Pro の10倍で、確認済みの口座には5時間の上限がない — What is the Max plan?・What is the Ultra plan?（確認 2026-11-03）」。API credits の行は「Max に$100、Ultra に$200」 |
| 02 2-2 と §2 の Takeaway | 条件を足す | 「有料プランには5時間ごとの上限と週の上限がある（2026-10-30 以降、確認済みの Ultra の口座は週の上限だけ）」 |
| 02 2-4 | 対象を足す | 「Max と premium seat」→「Max・Ultra と premium seat」 |
| 02 1-10 | 注記を足す | 「Customize は、2026-10-29 から順に、一つの Plugins のページに変わる（11-09 に一般提供、Enterprise は 11-30）」 |
| 02 3-7「アプリ」 | 1行を足す | 「2026-10-29 に Haiku 4.5 を、アプリ（Free・Pro・Max）のモデルの選択肢から外した（Claude Code・Team と Enterprise・API には残る）」 |
| 02 5-8 | 項目を足す | message threads（#40）、Usage and Cost Analytics API（#39）、Opus 4.8 の fast mode の非推奨（#19）、API の版 2026-10-21 の `temperature`・`top_p`・`top_k`（#42）を、それぞれ1行で |
| 04 の円換算（240行目） | 注記を足す | 「Max 20x」に「（2026-10-30 から Ultra）」 |
| 00 §5 台帳 | 行を直す・足す | §3.4 の3行の「足す内容」と、「足す候補」の4行 |
| 10 付録の「大会規約の版」（383行目） | 追記する | 「ISUCON2026 は 2026-10-31 開催。レギュレーションは 2026-07-28 公開の版、結果は 11-02 公開（所在は research/22 #45）」 |
| 10 付録C「ISUCON2026当日マニュアルのAI記述」（665行目） | 状態を足す | 「11-03 時点でも未取得。問題の解説と講評は準備中」 |

### 4.2 requirements.md

| 場所 | 直した文（案） |
| --- | --- |
| §7 冒頭 | 「Claude Code は 2026年1月〜10月末に約235版が出た（npm の公開記録。v2.0.77 → v2.1.312）」→「Claude Code は 2026-01-06〜10-27 に npm で271版が出た（v2.0.77 → v2.1.312。CHANGELOG の見出しでは254版）」。R2 の結果と突き合わせてから直す |
| §7「点検の手順」 | 追記：「Help Center には、リリースノートに載らない変更がある（2026-10-30 の Ultra、10-29 の Haiku 4.5、Plugins のページ）。コレクションのページの記事ごとの更新日も見る。Claude Code は、docs が CHANGELOG より遅れること（環境変数など）、CHANGELOG のない版（2.1.315）と欠番（2.1.313）があること、stable が latest より1週間ほど遅れることを前提にする」 |
| §6.6 の比喩「毎回読み直す受験者（全履歴の送信）」 | 注記：「API の message threads（beta、2026-11-02）では送るのを差分にできるが、モデルは毎回全体を読み、料金も変わらない。比喩の『読み直す』は保てる」 |
| §10.5 | 追記：「2026-11-03 に research/22 で確かめた（Claude Code v2.1.314〜317、Help Center と Platform の 10-29 以降、ISUCON2026 と IEEEXtreme 20.0 の所在）」 |

### 4.3 decisions.md（メインが作者に聞くかを判断する）

- 「作者のプラン：Max」の補足に、5x か旧 20x か（旧 20x なら 2026-10-30 から Ultra）を足す。ワークフローの規模と上限の見積もりに関わるので、作者に確かめるかをメインが判断する
- 「雛形の動作確認」の補足に「Claude Code は v2.1.314 以上で行う（`--setting-sources` の漏れの修正）。latest と stable のどちらで確かめたかも書く」を足す

---

## 5. 確かめていないこと

- Help Center の、10-29 以降に更新された139本のうち、中身を読んだのは13本と抜き取りの2本だけ。多くはプランの名前の置き換えと見たが、全部は読んでいない。特に、11-02 の新しい記事「Run your endpoint detection and response (EDR) sensor in Claude Cowork on Claude Desktop」と「Set up and manage the new unified Claude experience for your Enterprise organization」、10-30 に更新された「Share and unshare chats」（R5 のチャット共有に関わる）・「Use Claude in Chrome safely」・「Claude in Chrome permissions guide」・「Use skills in Claude」・「Data retention practices for Covered Models」は中身を見ていない
- Ultra の週の上限が旧 Max 20x と同じか（#44）。一次資料に記述がない
- Wrap-Up Allowance がいつ入ったか（#36）。記事に日付がない
- CHANGELOG の [Cloud sessions]・[Claude Tag]・[Code Review]・Claude apps gateway・self-hosted runner・Windows・VS Code の細かい修正の多くは、教材への影響が小さいと見て表に入れていない（約270行のうち、表に入れたのは約60行分）
- v2.1.315 の中身（npm にあるが、CHANGELOG と docs に項目がない）
- v2.1.316 の `--restricted` のセッションの修正（Read の allow の規則で作業ディレクトリの外のファイルを上げていた）。`--restricted` が何かを確かめていない
- docs で裏を取ったのは主な変更（#4・#8・#14・#15・#20・#21・#26 など）だけで、ほかは CHANGELOG の文だけによる
- ISUCON2026 の当日マニュアル、参加規約の全文（AI の語で探しただけ）、講評（準備中）
- IEEEXtreme の規則のページは、curl では小さなページしか取れず、WebFetch（要約の道具を通す）で読んだ。節の名前とページの時刻は道具の返答による
- 10-29 以降のほかのコンテスト（AtCoder の AHC など）。atcoder.jp を開かないので確かめておらず、検索は1回だけ
- 日本語版の Help Center のリリースノート
- §3.7 の 10-29 より前の記事（Agent Skills の寄贈、subagent を減らす記事、Enterprise の pooled budgets）の本文
- X の投稿は開いていない
- Platform の pricing のページは読んでいない（リリースノートに 10-29 以降の料金の変更がないことで代えた）

---

## 6. 使った量の目安

- 道具の呼び出し：約95回（ほとんどが Bash。Read 約12回、Write 1回、Edit 3回、ToolSearch 1回）
- Web の取得：curl で約75件（Help Center 約37件〔うちコレクション15件〕、Claude Code の docs 約20件、Platform 4件、ニュース・ブログ・料金 3件、ISUCON 6件、GitHub の API 2件、npm 1件、CHANGELOG 1件、IEEEXtreme 1件）。AI の利用を断る指定の確認は12の URL（robots.txt を含む）。WebFetch 2回、WebSearch 2回
- かかった時間：約35分（20:37〜21:10 JST ごろ）
