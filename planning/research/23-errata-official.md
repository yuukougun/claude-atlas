# 工程2 R2：公式の機能についての既知の誤りの確認

- 担当：R2（requirements §10.1 の10件と、21 §2.2 の F2・F3・F6）
- 日付：2026-11-03
- 確認した環境：Claude Code 2.1.317（この WSL の `claude --version`）。npm の dist-tags は latest・next が 2.1.317、stable が 2.1.311（2026-11-03 取得）
- 書いたのはこのファイルだけ。調査資料・requirements・decisions への直しは §4 に提案として書いた

---

## 1. 調べた範囲と方法

### 1.1 確認日と方法

- 確認日：すべて 2026-11-03（JST 20:40〜21:20 ごろ）
- 公式文書は Markdown 版（`https://code.claude.com/docs/en/<ページ>.md`、`https://platform.claude.com/docs/en/<ページ>.md`）を curl で取得し、文字列で確かめた。要約の誤りを避けるため、WebFetch（小さなモデルが要約する道具）は使っていない
- Claude Code の文書の全文（`https://code.claude.com/docs/llms-full.txt`、約1,000万字・127,056行）で、旧い文が今も残っていないかを探した
- 版と日付：CHANGELOG（GitHub の raw）と、npm registry の `time`（版ごとの公開日時。UTC）を突き合わせた。数え方のスクリプトは標準ライブラリだけで書き、取得したファイルとは別のフォルダに置いた
- Best practices がいつ書き直されたかは、Wayback Machine の CDX（保存の一覧）と保存の本文で二分探索した
- Web 検索は1回だけ（auto mode の既定化の公式の告知を探すため）。ほかの URL は予測して直接読んだ
- 版の表記：「v2.1.xxx（日付）」の日付は npm の公開日（UTC）

### 1.2 使った一次資料

| 資料 | URL | 使った項目 |
| --- | --- | --- |
| Best practices（現行） | https://code.claude.com/docs/en/best-practices | 1・3・9・F6 |
| Best practices（改稿前の保存） | https://web.archive.org/web/20261026194435/https://code.claude.com/docs/en/best-practices ほか（2026-01-22・05-23・09-01・09-18・10-01・10-14・10-20・10-24・10-26・10-27・10-29・11-02 の保存） | 1・F6 |
| Output styles | https://code.claude.com/docs/en/output-styles | 2 |
| Hooks reference / Hooks guide | https://code.claude.com/docs/en/hooks ・ https://code.claude.com/docs/en/hooks-guide | 3 |
| Environment variables | https://code.claude.com/docs/en/env-vars | 3・9 |
| Configure permissions | https://code.claude.com/docs/en/permissions | 4・5 |
| Errors（設定の警告） | https://code.claude.com/docs/en/errors | 4 |
| Sandboxing | https://code.claude.com/docs/en/sandboxing | 5 |
| Explore the context window | https://code.claude.com/docs/en/context-window | 6 |
| Memory / How Claude Code works / Large codebases | https://code.claude.com/docs/en/memory ・ https://code.claude.com/docs/en/how-claude-code-works ・ https://code.claude.com/docs/en/large-codebases | 6・F6 |
| Manage costs / Agent teams | https://code.claude.com/docs/en/costs ・ https://code.claude.com/docs/en/agent-teams | 7 |
| Model configuration | https://code.claude.com/docs/en/model-config | 8・9・F3 |
| Permission modes | https://code.claude.com/docs/en/permission-modes | F2 |
| Claude Code の文書の全文 | https://code.claude.com/docs/llms-full.txt | 1・4・F6 |
| CHANGELOG | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md（取得は raw.githubusercontent.com） | 2・3・4・6・9・F2・F3 |
| npm registry | https://registry.npmjs.org/@anthropic-ai/claude-code | 10、版の日付すべて |
| Models overview | https://platform.claude.com/docs/en/about-claude/models/overview（→ /docs/en/models/overview） | 8・F3 |
| Effort | https://platform.claude.com/docs/en/build-with-claude/effort | 8・F3 |
| Prompting Claude Sonnet 5.5 / Opus 5.5 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5 ・ …/prompting-claude-opus-5-5 | 8 |
| Change the model, effort, and thinking settings（Help Center） | https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings | 8 |
| Introducing Claude Sonnet 5.5（2026-09-28） | https://www.anthropic.com/claude-sonnet-5-5 | 8 |
| Introducing Claude Fable 5.1 and Claude Mythos 5.1 | https://www.anthropic.com/claude-fable-and-mythos-5-1 | 8 |
| Introducing Claude Opus 5.5（2026-09-22）/ Haiku 5.5（2026-10-07） | https://www.anthropic.com/claude-opus-5-5 ・ https://www.anthropic.com/claude-haiku-5-5 | 8・F3 |
| An update on recent Claude Code quality reports（2026-04-23） | https://www.anthropic.com/research/april-23-postmortem | F3・8 |
| How we built Claude Code auto mode（2026-03-25） | https://www.anthropic.com/research/claude-code-auto-mode | F2 |
| Auto mode is now the default in Claude Code（2026-08-07、10-22 追記） | https://claude.com/blog/auto-mode-default-in-claude-code（→ https://claude.com/resources/articles/auto-mode-default-in-claude-code） | F2 |

### 1.3 AI の利用を断る指定の確認（`python3 -I tools/check_noai.py`、2026-11-03）

| ドメイン | 確かめた URL | 結果 |
| --- | --- | --- |
| code.claude.com | /docs/en/best-practices（`--robots` 付き） | 指定なし。robots.txt にも AI 向けの指定なし |
| platform.claude.com | /docs/en/about-claude/models/overview（`--robots` 付き） | 指定なし。robots.txt にも AI 向けの指定なし |
| www.anthropic.com（anthropic.com を含む） | /engineering/claude-code-auto-mode（308）、/research/claude-code-auto-mode、/claude-sonnet-5-5、/research/april-23-postmortem、/news | 指定なし |
| claude.com | /blog（308）、/resources/articles/auto-mode-default-in-claude-code | 指定なし（meta robots は max-image-preview:large だけ） |
| support.claude.com | /en/articles/8664678-… | 指定なし（meta robots="all"） |
| registry.npmjs.org | /@anthropic-ai/claude-code（`--robots` 付き） | 指定なし |
| github.com | /anthropics/claude-code/blob/main/CHANGELOG.md（`--robots` 付き） | 指定なし。robots.txt は GPTBot・ClaudeBot などに一部の道（/*/raw/ など）を Disallow しているが、CHANGELOG の道は対象外。取得は raw.githubusercontent.com で行った |
| raw.githubusercontent.com | /anthropics/claude-code/main/CHANGELOG.md | 指定なし |
| web.archive.org | / | 指定なし。archive.org の API は 429 で判定できなかったので使わず、web.archive.org の CDX と保存だけを使った |

atcoder.jp と codeforces.com は開いていない。二次情報（GIGAZINE・Oikon のスライドなど）は読んでいない。

---

## 2. 結果の一覧

結果は、表の「主張」（requirements §10.1 と 21 §2.2 の記述）が一次資料と合うかである。行番号は 2026-11-03 時点のファイルの行。

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典（確認日はすべて 2026-11-03） | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 1 | §10.1：01 の冒頭の要約の「コンテキストはすぐ埋まり、埋まるほど性能が落ちる」は古い。**場所**：01 KQ1 の Takeaway（16行）・0-3（32〜36行）・2-1「大前提」（399行）。同じ旧い前提が 10 第12章（215・217行）にある（11 第4節 #9・C-25 で指摘済み） | 正しい | 現行の Best practices は「コンテキストを最大の制約として積極的に管理する」を「What you can stop doing」の表に入れている。理由は、多くの現行モデルが 1M トークンの窓を持ち、圧縮も自動なので、溢れることはまれだから。関係のない作業の間の `/clear` は、焦点の合った文脈のほうが答えがよく安いので、今も勧めている。旧い文は Wayback の保存で 2026-10-26 19:44（UTC）まであり、10-27 08:15（UTC）の保存で消えている。01 は改稿前の版を引いていた（§3.1） | Best practices。Wayback 20261026194435・20261027081520 | 分野01・05、古くなった助言の台帳（第一波）の「200k を前提に…」の時期、症状辞典「長い会話で前提を忘れる」 |
| 2 | §10.1：output style の組み込みは4種（Proactive・Concise・Explanatory・Learning）。**場所**：00 分野07「output style（説明多め・簡潔・学習用）」（334行）が Explanatory と Learning だけ。01 I-1（237行）は正しい | 正しい | Default（スタイルを選ばない状態）のほかに組み込みが4種ある。Explanatory と Learning は v1.0.81（2025-08-14）から、Concise は v2.1.237（2026-08-19）から。Proactive の追加の版は CHANGELOG にない（v2.1.257 に修正の記述がある）。`/output-style <名前>` は v2.1.269（2026-09-11）以降（v2.1.73 で一度非推奨になり、戻った）。設定の `outputStyle` は大文字小文字を区別し、合わない値は Default になる。コマンドは区別しない。Proactive は権限モードを変えない | Output styles、CHANGELOG | 分野07、日本語で使う（output style で文体をそろえる。R6）、facts.yml（版と大文字小文字） |
| 3 | §10.1：Stop hook は、ツール呼び出しを挟まずに8回続けてブロックすると上書きされ、環境変数で変えられる。**場所**：00 分野10「Stop hook で『終わらせない』」（405行）は回数なし。05（48行）は8回と環境変数を書く。10 付録A-1（376行）は「連続8回」で、「ツール呼び出しを挟まずに」が抜けている | 正しい | Stop と SubagentStop の hook が、Claude のツール呼び出しを挟まずに8回続けてターンの終了を止めると、次のブロックは上書きされ、警告付きでターンが終わる。数えはツール呼び出しのたびに戻る。上限は `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`（既定8、0 で上限なし）で変える。v2.1.143（2026-05-15）から。`additionalContext` で続けさせる場合も同じ上限が効く。対策は、入力の `stop_hook_active` を見て早めに抜けること | Hooks（#stop-input）、Hooks guide、Environment variables、Best practices、CHANGELOG v2.1.143 | 分野10、検証の階段（評価と実験の核・第一波）、雛形 A-14 |
| 4 | §10.1：`Write(path)`・`NotebookEdit(path)`・`Glob(path)` のルールは受け付けられるが当たらず、パスで縛るときは Edit と Read で書く。**場所**：00 分野10「権限ルール」（407行）に記述がない。11 3-3 #3・11c（247行）が指摘 | 正しい | ファイルの権限は `Edit(path)` と `Read(path)` のルールだけで判定する。`Write`・`NotebookEdit`・`Glob`（と旧い `MultiEdit`）にパスを付けたルールは、受け付けられるがどの読み書きにも当たらない。書き込みは `Edit(...)`、Glob の代わりは `Read(...)` で書く。パスなしの道具名だけのルールは、その道具の使用すべてに当たる。v2.1.210（2026-07-14）から起動時に警告が出る（対話では deny・ask のルールだけ1行表示し、allow はデバッグログだけ。`-p` は stderr。`--allowedTools` の Glob は警告なし） | Configure permissions（#read-and-edit）、Errors（#is-not-matched-by-file-permission-checks）、CHANGELOG v2.1.210 | 分野10、制作の `.claude/settings.json`（decisions「hooks と permissions」）、R7 |
| 5 | §10.1：Read と Edit の deny は、組み込みのツールと認識できるシェルのコマンドにしか効かず、任意の子プロセスには効かない。**場所**：00 分野10・分野11「秘密情報を守る」（425行）に限界の記述がない。10 第17章（11 第4節 #11）、10 付録A-1（375行）、11 3-2 #9 | 正しい | Read・Edit の deny が効くのは、組み込みのファイルの道具、Claude Code が Bash の中で見分けるファイルのコマンド（cat・head・tail・sed・tee など）、リダイレクトの先である。名前を挙げずにファイルを読むコマンド（そのフォルダでの `grep -r パターン .` など）と、自分でファイルを開くスクリプト（Python・Node など）には効かない。すべてのプロセスを止めるには sandbox（OS の層。Bash・PowerShell・Monitor とその子プロセス）を使う。Read・Edit の deny は sandbox の設定にも合わさるが、sandbox の `denyRead` は Read の道具を止めない。hook・ローカルの MCP サーバーなどは sandbox の外で全権で動く。Read の deny は同じパスの Edit と Write（Write は v2.1.228 以降）も止めるが、NotebookEdit は止めない | Configure permissions、Sandboxing | 分野10・11、雛形 A-3・A-4（§10.3 の hold-out の保護）、decisions「危ない雛形を試す場所」、R7 |
| 6 | §10.1：圧縮の後に残るものの完全な一覧が公式の context-window のページにある。**場所**：00 §7（878行）が空白とし、分野01（186行）は「CLAUDE.md は再注入される」だけ。05（93・197行）は取得できず。10 付録A-1（378行）は一部。11 3-2 #5・11b 第2節 #5 が一覧を書く | 正しい（11 の要約の一部は誤り） | 一覧は「What survives compaction」の表にある（要約は §3.4）。11 3-2 #5 の「skill の一覧（description）は戻らない」は誤り。v2.1.304（2026-10-19）以降は、今の skills から作り直して入れ直す（10-27 の保存の時点で文書にこの行があった）。11 にない行として、バックグラウンドのコマンドと subagent は動き続けること、hook が前に足した文脈は会話と一緒に要約されることがある。auto memory の「先頭200行または25KB」は Memory のページの値（起動時に読む量）で、この表には書かれていない | Explore the context window（#what-survives-compaction）、Memory、CHANGELOG v2.1.304、Wayback 20261027152919 | 分野01「compaction で何が残り、何が消えるか」、分野05、症状「圧縮の後に約束を忘れた」、front matter の `survives_compaction`、21 §2.4 |
| 7 | §10.1：agent teams の「約7倍のトークン」は teammate が plan mode のときの値。**場所**：00 分野12「agent teams（実験的）」（453行）・分野14「並列・ループ・workflows のコスト」（494行）が条件なし。01 E（174行）・05（174行）・10 付録A-1（377行）・04（75・341行）は条件付きで正しい | 正しい | Manage costs は「teammate が plan mode で動くとき、通常のセッションの約7倍」と書く。理由は、teammate ごとに文脈を持ち、別の Claude として動くから。Agent teams のページは倍率を書かず、トークンは動いている teammate の数に応じて増えるとだけ書く。agent teams は実験的で、既定ではオフ（`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` で有効） | Manage costs（agent team の節）、Agent teams | 分野12・14、facts.yml |
| 8 | §10.1：Sonnet 5.5 の既定 effort が API の文書と Claude Code の文書で食い違う（公式同士の食い違いの3件目）。**場所**：02 3-1（461行、high）、01 L-2（297行、medium）、10 付録A-1（373行）・付録C（668行）、11 3-2 #1、21 §2.3 | 一部誤り（値は違うが、食い違いではなく面ごとの既定） | Sonnet 5.5 の既定は、Claude Platform（API）で high、Claude Code とアプリで medium。Sonnet 5.5 の発表（2026-09-28）がこの分け方を明記している。Models overview の「Default effort」は「Claude API での effort の既定」と注記されている。Claude Code は自分の既定をリクエストに入れて送り、送らない設定（`CLAUDE_CODE_EFFORT_LEVEL=auto` か `unset`）にすると API の既定が効く。ポストモーテム（2026-04-23）も、既定は製品の層で選んで API に送る値だと説明している。面で既定が違うのは Sonnet 5.5 だけではない（Fable 5.1、Opus 4.7。§3.2） | Introducing Claude Sonnet 5.5、Models overview、Effort、Model configuration（#send-no-effort-level）、ポストモーテム | 分野03、facts.yml（面ごとの値）、書き方の方針7、00 §6 |
| 9 | §10.1：「think hard」は「effort を上げるキーワードとしては効かず、普通の文として扱われる」が正確。ultrathink の現在の扱いも。**場所**：00 §1 の表（80行）・分野03（220行）・台帳（721行）、01 L-2（298行）・KQ2 Inferences（435行）・KQ4（519行）、05（26・340行）、10 付録A-1（373行）・付録B（630行）、03 Q5 P6（346〜348行）と Gaps（371行）、11 3-2 #14 | 正しい | Best practices：think hard・think harder・be thorough は、effort の設定の範囲で軽く後押しする普通の文で、effort を上げるキーワードではない。Model configuration：think・think hard・think more は普通の文として渡し、キーワードとして認識しない。ultrathink は、そのターンだけ深く考えるよう頼む言葉として認識され、セッションの effort の設定は変えない。v2.1.311（2026-10-26）以降の対話のターミナル（VS Code は v2.1.316 以降）では、Opus 5.5・Sonnet 5.5・Haiku 5.5・Fable 5.1 を Anthropic の API で使うとき、そのターンを xhigh で動かす（効くときは虹色に表示）。`CLAUDE_CODE_EFFORT_LEVEL` が xhigh より下のとき、組織の上限があるとき、Bedrock などでは上がらない。`CLAUDE_CODE_DISABLE_ULTRATHINK`（v2.1.316 以降）で止められる | Best practices（What you can stop doing）、Model configuration（#use-ultrathink-for-one-off-deep-reasoning）、CHANGELOG | 分野03「『考えて』と書くことの現在」、台帳、requirements §6.3 |
| 10 | §10.1：リリース数を、期間を明記した一つの数字にそろえる（「1年で約310回」と「1〜10月で約235版」）。**場所**：00 §1（85行）・01 KQ1 Inferences（377行）「v2.0.77 から v2.1.312 までに約235版」、10 冒頭（7行）・付録B（631行）「1年で約310回」、11 3-2 #10、11a（229行） | 一部誤り（そろえる方針は正しいが、「約235版」が誤り） | npm の公開記録では、v2.0.77（2026-01-06）から v2.1.312（2026-10-27）までに271版が公開された（同じ範囲の CHANGELOG の見出しは254）。235 はどの数え方とも合わない。2026年1〜10月は274版（v2.0.77〜v2.1.316）、2025-11-01〜2026-10-31 の12か月は315版（月に約26版）。2026年のどこで12か月を切っても313〜321版なので、「1年で約310回」は npm の記録とほぼ合う（§3.6） | npm registry、CHANGELOG | 台帳と鮮度の説明（分野00・19）、facts.yml |
| F2-a | 21 F2：auto mode の既定化は「有料プラン」と「対話セッション全体」の二段階か。**場所**：03 Q1 の前提（18行）・T6（294行）「8/14 から既定」、00 §1 の表（74行）・台帳（724行）・§7（880行）、05（6行）、01 C-1（96行）、10 付録A-1（375行）、11 3-2 #4 | 正しい（二段目の版に細部あり） | 一段目：公式の告知（2026-08-07）で、2026-08-14 から Pro・Max・Team の新しいセッションを auto mode で始めた（今の題名と一部の文は Ultra を含めて書き、ほかの文は Pro・Max・Team とだけ書く）。Enterprise・Claude API・クラウドの提供元は当面オプトインだった。文書では、この既定は機能フラグを取得するセッションで v2.1.228 以降（ネイティブの Windows は v2.1.233 以降）。二段目：文書は「v2.1.283 以降、ターミナルと VS Code の対話セッションは、どのプラン・提供元でも auto mode で始まる」とする。CHANGELOG では v2.1.283（09-25）が他社の基盤とテレメトリを切ったセッション、v2.1.284（09-28）が「すべてのプランと提供元」 | Auto mode is now the default in Claude Code、Permission modes、CHANGELOG | 台帳「最初は毎回承認を求められる」、分野10、decisions「安全の既定の勧め方」 |
| F2-b | 21 F2：`claude -p` の既定は Manual。**場所**：01 C-1（96行）、10 付録A-1（375行） | 正しい | `claude -p` と Agent SDK で権限モードを決めていないときは `default`（表示は Manual。v2.1.200 で表示名が変わった）。v2.1.302（2026-10-16）以降は、承認の要る呼び出しを、allow ルール・hook・`canUseTool`・`--permission-prompt-tool` で認めない限り拒否する。経緯として、v2.1.285（09-29）で他社の基盤とテレメトリを切った `-p` を auto で始めるようにし、v2.1.302 で `default` に戻した。`--permission-mode auto` を渡せば auto で動く | Permission modes、CHANGELOG | decisions「雛形の動作確認」（`claude -p` では権限モードと allow を明示する）、分野12 |
| F2-c | 21 F2：承認率・検出率の公式の値は93%で、97%・89% は二次情報（GIGAZINE）の値。**場所**：03 Q1 の前提（18行）・T6（294行）、00 §7（880行）・分野11「承認疲れ」（428行）、05（138・145行） | 一部誤り（97%・89% も公式の値） | 値の出所は二つの公式の記事で、時期とデータが違う。(1) 2026-03-25 の engineering の記事：手動の承認は実際には93%が承認される。分類器（本番の二段の流れ）は、社内の実トラフィック（n=10,000）で誤ってブロックするのが 0.4%、実際の行き過ぎた行動（n=52）の見逃しが 17%、合成の持ち出し（n=1,000）の見逃しが 5.7%。(2) 2026-08-07 の Claude の blog：Claude Code の権限の確認の97%が承認される。1,053人の有償の被験者の対照実験で、1回の確認を明らかに危ないコマンドに差し替えたとき、人が止めたのは13.6%（143件）、auto mode が止めたのは89%（937件）。03 の「86.4% を見逃した」は人の見逃しの割合（100−13.6）。03 の数値は (2) と一致するので、出典を (2) に差し替えればよい。どちらの承認率にも、測った期間と母集団の説明はない | How we built Claude Code auto mode、Auto mode is now the default in Claude Code | 分野11「承認疲れ」、分野10「auto mode は何を止め、何を止めないか」、facts.yml |
| F3 | 21 F3：03 Q5 P6（346行）の「全モデルの既定が high または xhigh になった」と、各モデルの既定 effort の公式の値 | 一部誤り（2026-04 の時点の記述で、現行と違う） | ポストモーテム（2026-04-23）は、3月4日に Claude Code の既定を high から medium に下げたのを4月7日に戻し、Opus 4.7 は xhigh、ほかのモデルは high にしたと書く（影響は Sonnet 4.6 と Opus 4.6）。CHANGELOG では、戻したのは v2.1.94（04-07。API キー・Bedrock/Vertex/Foundry・Team・Enterprise）と v2.1.117（04-21。Pro/Max の Opus 4.6・Sonnet 4.6）の二回。その後に出た Opus 5.5（09-22）・Sonnet 5.5（09-28）・Haiku 5.5（10-07）は、Claude Code の既定が medium なので、「全モデルが high か xhigh」は今は誤り。現行の値は §3.2 の表 | ポストモーテム、Model configuration、Effort、CHANGELOG | 分野03、台帳、facts.yml |
| F6 | 21 F6：01 の「埋まるほど性能が落ちる」は KQ1 の Takeaway・0-3・2-1 の3か所 | 正しい（ほかに3か所と、2-1 の全体） | 3か所に加えて、KQ2 の Takeaway の④（393行）と 2-1「セッション管理」（406行）の「コンテキストを積極管理」、2-1「環境設定」（404行）の「IMPORTANT は1行だけ」も改稿前の版の勧め。2-1 は全体が改稿前の版（〜2026-10-26）の要約で、kitchen sink・Writer/Reviewer・fan-out・trust-then-verify・AskUserQuestion でのインタビューなどの語は現行の版にない（§3.1）。直した文は §4.1 | Best practices（現行）、Wayback 20261026194435・20261027081520 | 01 を素材にするページすべて |

件数：15件。正しい 11件、一部誤り 4件（8・10・F2-c・F3）、誤り 0件、確かめられない 0件。ただし、確かめる途中で調査資料の側の誤りが見つかった（「約235版」、11 3-2 #5 の skill の一覧、03 の「全モデルが high か xhigh」、05 の `-p` の扱い、ほか §3.7）。

---

## 3. 新しく分かったこと

### 3.1 Best practices は 2026-10-26〜27 に大きく書き直された（調査資料は版が混ざっている）

Wayback の保存（CDX の一覧で、2026年の保存が digest の重複を除いて約160）を二分探索した。

- 2026-01-22・05-23・09-01・09-18・10-01・10-14・10-20・10-24 と、10-26 19:44（UTC）の保存には、旧い前提の文がある：「Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills.」（改稿前の Best practices）。続けて、窓が埋まると初めの指示を忘れたり誤りが増えたりするので、コンテキストは最も大事な管理の対象だ、と書いていた。「What you can stop doing」の表はなく、守られない1行にだけ IMPORTANT を付けるよう勧めていた
- 10-27 08:15（UTC）以降の保存（10-27・10-29・11-02）と 11-03 の現行の版には、旧い文がなく、「What you can stop doing」の表がある。表の行は7つ：コンテキストを最大の制約として管理する、IMPORTANT や全大文字で強調する、コンテキストを守るために subagent を使う、よい答えのために subagent に任せる、think hard などを書く、keep going などと書く、アーキテクチャを CLAUDE.md に書く
- 現行の版の冒頭は、多くの場合は Claude Code の既定（auto mode、subagent への委任、窓が埋まる前の自動の圧縮）で最初の平易な依頼が正しく動くとし、既定で足りないとき（見えない情報、確かめる手段、例外のない規則、既定の手間とコスト）を扱う構成になった
- 調査資料はどれも「2026-10-29 時点」とするが、読んだ版が違う。01 の KQ1・0-3・KQ2 の 2-1 と、10 第12章は改稿前の版を、00 §1・06・11b は現行の版を要約している。01 の 2-1 に並ぶ語（kitchen sink session、Writer/Reviewer、fan-out、trust-then-verify gap、infinite exploration、validateEmail の例、Ctrl+G、adversarial review、AskUserQuestion でのインタビュー、status line での常時監視）は現行の版にない
- 現行の文書の全文（llms-full.txt）に「fills up fast」「degrades as it fills」はない。近い記述は二つだけある。How Claude Code works は、自動で圧縮するが会話の初めの指示は失われうるので、続く規則は CLAUDE.md に置くと書く。Large codebases は、大きなコードベースで関係のない指示や読み込みが窓を埋めると、トークンを使い性能も落ちると書く

### 3.2 既定の effort（2026-11-03 時点の公式の値）

| モデル | Claude API | Claude Code | アプリ（claude.ai・Cowork など） |
| --- | --- | --- | --- |
| Fable 5.1 | high | high | medium（claude.ai と Cowork。Fable 5.1 の発表） |
| Opus 5.5 | medium | medium | 文書に面ごとの値はない（発表は「既定（medium）」とだけ書く） |
| Sonnet 5.5 | high | medium | medium（Sonnet 5.5 の発表：Claude Code とアプリは medium、Claude Platform は high） |
| Haiku 5.5 | medium | medium | 値を書いた文書は見つけていない |
| Fable 5・Opus 5・Opus 4.8・Opus 4.6・Sonnet 4.6 | high | high | — |
| Sonnet 5 | high | high（Effort のページに「Claude API と Claude Code で high」とある） | — |
| Opus 4.7 | high | xhigh | — |

- 出典：API は Models overview と Effort、Claude Code は Model configuration（effort の決まり方の5番目）、アプリは各モデルの発表。Help Center の記事は、メニューで各モデルの推奨の値に「Default」と表示するとだけ書き、値の一覧はない
- Claude Code での決まり方：環境変数 `CLAUDE_CODE_EFFORT_LEVEL`、セッションで選んだ値、`--effort`、設定（モデルごとの `modelSettings` か `effortLevel`）、モデルの既定、の順に最初に当たったもの。組織が既定のモデルの effort を決めていればそれが既定になる。ユーザー設定の一番上の `effortLevel` は Opus 5.5 とそれより後のモデルには効かない（モデルごとに保存するようになったため）
- 10-29 より後の変更：v2.1.317（2026-11-02）で、本体と違うモデルで動く subagent と teammate は、セッションの effort ではなく、そのモデルに保存した値か既定を使うようになった。Agent teams のページの「teammate はリーダーの effort を引き継ぐ」という記述と合わなくなっている可能性がある（R1 の範囲）

### 3.3 auto mode の既定化と公式の数値（F2）

時期：

| 日付と版 | 変更 | 出典 |
| --- | --- | --- |
| 2026-03-25 | engineering の記事で auto mode の仕組みと評価を公開 | How we built Claude Code auto mode |
| v2.1.200（07-03） | 権限モード `default` の表示名を Manual にした（`manual` も受け付ける） | CHANGELOG |
| 08-07 告知、08-14 開始 | Pro・Max・Team の新しいセッションを auto mode で始める。別の既定を決めていた人には一度だけ尋ね、固定した既定は変えない。Enterprise・Claude API・クラウドの提供元はオプトインのまま。文書では v2.1.228（08-11）以降、ネイティブの Windows は v2.1.233（08-14）以降で、機能フラグを取得するセッション | Auto mode is now the default…、Permission modes |
| v2.1.283（09-25） | 他社の基盤やテレメトリを切った対話セッションも auto で始める（文書はこの版を「どのプラン・提供元でも」の境とする） | CHANGELOG、Permission modes |
| v2.1.284（09-28） | ターミナルと VS Code の対話セッションを、すべてのプランと提供元で auto で始める | CHANGELOG |
| v2.1.285（09-29） | 他社の基盤やテレメトリを切った `-p` と Python の Agent SDK も auto で始める。HIPAA の構成の組織は Manual で始める | CHANGELOG、Permission modes |
| v2.1.302（10-16） | `-p` と Agent SDK は（他社の基盤・テレメトリなし・新しいインストールでも）`default` で始める。承認の要る呼び出しは、認める手段がなければ拒否 | CHANGELOG、Permission modes |
| 10-22 追記 | 「来週から、Claude のほとんどのアプリで Pro・Max・Team の新しいセッションを auto mode で始める。Enterprise の管理者には先にメールする」 | Auto mode is now the default…（追記） |

数値（どれも公式。教材では出典の日付とデータの種類を添える）：

| 値 | 意味 | 出典 |
| --- | --- | --- |
| 93% | 手動の承認の確認のうち、実際に承認される割合 | 2026-03-25 の記事 |
| 97%（却下は3%） | Claude Code の権限の確認のうち、承認される割合。計画の確認は39%が却下される | 2026-08-07 の記事 |
| 0.4% | 分類器（二段の流れ）が社内の実トラフィック（n=10,000）の無害な操作を止める割合 | 2026-03-25 の記事 |
| 17%（止める側は83%） | 実際のセッションから集めた行き過ぎた行動（n=52）を見逃す割合 | 2026-03-25 の記事 |
| 5.7% | 合成した持ち出しの試み（n=1,000）を見逃す割合 | 2026-03-25 の記事 |
| 89% と 13.6% | 1,053人の有償の被験者の実験で、1回の確認を明らかに危ないコマンドに差し替えたとき、auto mode が止めた割合（937件）と人が止めた割合（143件）。人はセッションが長くなるほど止めなくなった | 2026-08-07 の記事 |
| 12% → 7% | 第三者が作った攻撃のデータで、強化の前後の見逃しの割合（合成の敵対的なデータで、実トラフィックの値ではないと記事が断っている） | 2026-08-07 の記事 |

- 03 の「97%・86.4%・89%」は 2026-08-07 の記事の値と一致する。21 F2 の「GIGAZINE 経由の数字」は、出典の書き方の問題で、値の誤りではない
- 「検出率」は、データの作り方で 83% から 95% 近くまで違う。一つの値で「auto mode の検出率」と書かない
- 連続のブロック：3回続けて、または合計20回ブロックすると auto mode は止まって確認に戻る（しきい値は変えられない）。`--permission-prompt-tool` のない `-p` では、しきい値に達してもその操作を実行しないだけで、実行は止めない（Permission modes、2026-11-03）。2026-03-25 の記事は「-p ではプロセスを終える」と書いていたので、05（149行）の「headless（-p）ではプロセスが終了する」は今の文書と合わない。変わった版は CHANGELOG で見つけられなかった

### 3.4 圧縮の後に残るもの（項目6。Explore the context window の表の要約、2026-11-03）

圧縮では、会話の履歴を要約に置き換える。何が残るかは、どう読み込まれたかで決まる。

- **そのまま効く**：system prompt と output style
- **ディスクから入れ直す**：プロジェクト直下の CLAUDE.md と `paths:` のない rules、auto memory、plan mode で書いた計画
- **作り直して入れ直す**：skill の説明文（今の skills から作る。v2.1.304 以降）、git status（起動時に取っていたセッションだけ、新しく取り直す）
- **必要になったら読み直す**：`paths:` 付きの rules とサブフォルダの CLAUDE.md。引き金のファイルを読む・書くまでは戻らない。圧縮を越えて残したい規則は、`paths:` を外すか直下の CLAUDE.md に移す
- **一部を読み直す**：読んだか編集したファイルのうち、最近変更されたものから5つまで。5,000トークンを超えるファイルは中身なしのパスの参照（`Referenced file`）で戻る
- **上限付きで入れ直す**：呼び出した skill の本文。1つ5,000トークン、合計25,000トークンまでで、古いものから落とす。先頭を残して切るので、大事な指示は SKILL.md の上に置く
- **動き続ける**：バックグラウンドのコマンドと subagent。まだ動いているものを Claude に知らせ、重複して始めないようにする
- **要約に溶ける**：hook が前に足した文脈と、会話の中だけで伝えた指示
- **もう一度走る**：`compact` に合う SessionStart hook。出力を圧縮後の文脈に足す
- 補足：要約の依頼は、セッションの thinking の設定を引き継ぐ（v2.1.198 以降）。auto memory を起動時に読む量は MEMORY.md の先頭200行か25KB の早いほう（Memory のページ）。手前で打てる手は、焦点を付けた `/compact`、`/rewind` の部分的な要約、`/autocompact <トークン数>`、関係のない作業の間の `/clear`、大きな読み込みの subagent への委任

### 3.5 ultrathink の経緯（項目9・F3）

| 日付と版 | 変更 |
| --- | --- |
| v0.2.44（2025-03-15） | think・think harder・ultrathink で考える量を頼めるようになった |
| v2.1.68（2026-03-04） | Opus 4.6 の既定を Max と Team で medium にし、同時に ultrathink を「次のターンを high に」として戻した |
| v2.1.311（2026-10-26） | 対話のターミナルで、5.5世代と Fable 5.1 を Anthropic の API で使うとき、ultrathink のターンを xhigh で動かす。作業中に打つと、そのターンの残りを上げる |
| v2.1.316（2026-10-31） | VS Code でも xhigh にした。`CLAUDE_CODE_DISABLE_ULTRATHINK` を足した（環境変数の一覧のページにはまだ載っていない） |
| v2.1.317（2026-11-02） | VS Code でテレメトリを切ったときに効かなかったのを直した |

03 の「2026年1月16日に廃止」は CHANGELOG に記述がなく、確かめられなかった（03 の出典は二次情報）。03 Gaps（371行）の「Opus 5.5 世代で ultrathink が効くか確認できない」は、上の文書と CHANGELOG で埋まる。

### 3.6 リリース数の数え方（項目10）

npm registry（2026-11-03 取得。公開日時は UTC）で数えた。数は `time` にある版（公開の後に取り下げた版を含む）で、すべて x.y.z の形だった。

| 期間 | 公開された版 | 範囲 |
| --- | --- | --- |
| v2.0.77〜v2.1.312（調査資料と同じ範囲） | 271（CHANGELOG の見出しは254） | 2026-01-06〜10-27 |
| 2026年1〜10月 | 274 | v2.0.77〜v2.1.316 |
| 2025-11-01〜2026-10-31（12か月） | 315（月に約26） | v2.0.32〜v2.1.316 |
| 2025-10-29〜2026-10-28（調査の日までの1年） | 315 | v2.0.29〜v2.1.312 |
| 2026年に終わる12か月の窓（6月〜11月の各月初めで切る） | 313〜321 | — |
| 2025年（公開の初め 2025-02-24 から） | 285 | v0.2.6〜v2.0.76 |

- 版番号は連番ではない。2.1.0〜2.1.317 のうち44の番号が公開されていない。2.1.88（2026-03-30）は公開の後に取り下げられた（npm の `time` にあって `versions` にない）。だから「最後の番号−最初の番号」では数えられない。v2.1.312 の 312 から v2.0.77 の 77 を引くと 235 になるが、調査資料がこう数えたかは確かめていない
- CHANGELOG の見出しは、npm の版より少ない（見出しのない版がある）

### 3.7 そのほか、調べる中で見つけたこと

- **subagent とコンテキスト**：現行の Best practices は「コンテキストを守るために subagent を使う」も「もうやめてよい助言」に入れた。溢れることがまれになったからで、並列の作業、うるさい出力を本筋から離すこと、独立のレビューには今も向くが、どれも追加のトークンがかかる、とする。03 X6「サブエージェントでメインのコンテキストを守る」（221〜225行）は「有効」とするので、理由の書き方を直す必要がある
- **IMPORTANT の強調**：改稿前の版は「守られない1行にだけ IMPORTANT を付ける」と勧めていた。現行の版は、IMPORTANT を足しても直らない、ファイルが長すぎるか、例外のない規則なので hook にする、とする。00 台帳（722行）の「強調は1行だけにし」と 01 2-1（404行）の「IMPORTANT は1行だけ」は改稿前の勧め
- **台帳の「公式の撤回表」の時期**：撤回の表は 2026-10-27 ごろの改稿で入った。00 台帳で「2026（公式の撤回表）」とした行（IMPORTANT、アーキテクチャ、keep going）と、「200k を前提に…」（「2026」）は、時期を「2026-10-27 ごろ（Best practices の改稿）」にできる
- **プラン名**：文書と auto mode の告知の題名に「Ultra」というプランがある（Pro・Max・Ultra・Team）。02 にない可能性がある（R5・R1 の範囲。中身は調べていない）
- **アプリの auto mode**：auto mode の告知の 10-22 の追記に、Claude のほとんどのアプリでも Pro・Max・Team の新しいセッションを auto mode で始める、とある（R1 の範囲）

---

## 4. 提案

### 4.1 調査資料 01（F6 と項目1）

**(a) 01 KQ1 の Takeaway（16行）**

現：「…の4層の拡張を重ねた構造で、公式は「コンテキストウィンドウが最重要資源」という一点からほぼ全ての推奨を導いている。2026年に auto mode（v2.1.283 で既定化）、…」

案：「…の4層の拡張を重ねた構造である。公式の Best practices は、2026-10-26 ごろまで「コンテキストはすぐ埋まり、埋まるほど性能が落ちる」という一つの制約からほぼすべての推奨を導いていたが、2026-10-27 ごろの改稿で、コンテキストを最大の制約として管理するという助言を「もうやめてよい助言」に移した（多くの現行モデルは 1M トークンの窓を持ち、圧縮も自動なので、溢れることはまれ。関係のない作業の間の /clear は、答えの質とコストのために今も勧める。2026-11-03 確認）。2026年に auto mode（Pro・Max・Team は 2026-08-14 から、ターミナルと VS Code の対話セッション全体は v2.1.283 から既定）、…」

**(b) 01 0-3（32〜36行）**

- 見出し：「0-3. コンテキストウィンドウ（最重要資源）」→「0-3. コンテキストウィンドウ」
- 概要：「会話、読んだファイル、コマンドの出力、CLAUDE.md、auto memory、skill の説明文、システムの指示など、セッションで Claude が知ることはすべて context window に入る。上限に近づくと Claude Code が会話を自動で要約に置き換える（compaction）ので、窓が埋まってもセッションは終わらない。ただし、会話の中だけで伝えた指示は要約で失われうる — [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)・[Explore the context window](https://code.claude.com/docs/en/context-window)。現行の Best practices（2026-10-27 ごろ改稿）は「コンテキストを最大の制約として積極的に管理する」を「What you can stop doing」の表に入れている。多くの現行モデルが 1M トークンの窓を持ち、圧縮も自動なので、溢れることはまれだからである。一方で、焦点の合った文脈のほうが答えがよく安いので、関係のない作業の間の /clear は今も勧めている — [Best practices](https://code.claude.com/docs/en/best-practices)。大きなコードベースで関係のない指示や読み込みが窓を埋めると、トークンを使い、性能も落ちる — [Large codebases](https://code.claude.com/docs/en/large-codebases)。改稿前の版（〜2026-10-26）は、推奨のほとんどを「窓はすぐ埋まり、埋まるほど性能が落ちる」という一つの制約から導いていた（Wayback の保存で確認）」
- 「公式の推奨」：「`/context` で内訳を見る — [Explore the context window]。費用はまず `/usage` で見る — [Best practices]」（「status line で常時監視」は改稿前の版の勧めなので外す）
- 確認日：2026-11-03

**(c) 01 2-1（397〜410行）**

- 節の頭に注記を足す：「**注意（2026-11-03）**：この節は改稿前の Best practices（2026-10-26 ごろまで）を要約している。現行の版は 2026-10-27 ごろに書き直され、kitchen sink session・Writer/Reviewer・fan-out・trust-then-verify gap・AskUserQuestion でのインタビューなどの語は消えた。使う前に現行の版で確かめ直す」
- 「大前提」の行（399行）を差し替える：「**前提の変化**：改稿前の版は「コンテキストはすぐ埋まり、埋まるほど性能が落ちる」を大前提にしていた。現行の版は、Claude Code の既定（auto mode、subagent への委任、自動の圧縮）で多くの依頼は最初の平易な一文で足りるとし、既定で足りないとき（Claude に見えない情報、確かめる手段、例外のない規則、既定の手間とコスト）の手当てを扱う。コンテキストを最大の制約とする助言は「What you can stop doing」の表に移った — [Best practices]（2026-11-03 確認）」
- 「環境設定」の行（404行）の「IMPORTANT は1行だけ」の後に足す：「（改稿前の版の勧め。現行の版は、守られない行に IMPORTANT を足しても直らず、ファイルを短くするか hook にする、とする）」
- 「セッション管理」の行（406行）の「コンテキストを積極管理（…）」→「関係のない作業の間は /clear し、圧縮には焦点を付ける（…）。現行の版は /clear の理由を答えの質とコストに置く」

**(d) 01 KQ2 の Takeaway（393行）**

「④コンテキストを積極管理（/clear、subagent に調査させる、2回訂正して駄目ならやり直す）」→「④関係のない作業の間は /clear し、2回訂正して駄目なら /clear して頼み直す（コンテキストを『積極的に管理する』こと自体は、2026-10-27 ごろの改稿で古い助言の表に入った）」

**(e) 01 のほかの箇所**

- KQ1 の Inferences（377行）「約235リリース」→「npm に271版（v2.0.77〜v2.1.312、2026-01-06〜10-27。2026-11-03 に npm registry で数えた）」
- L-2（298行）「「think hard」等のフレーズは認識されない」→「「think」「think hard」などはキーワードとして認識されず、普通の文として渡る（effort は上がらない）。ultrathink は v2.1.311（2026-10-26）以降、対話のターミナルで 5.5世代と Fable 5.1 を Anthropic の API で使うとき、そのターンを xhigh で動かす（VS Code は v2.1.316 以降）」
- C-1（96行）の既定モード：「v2.1.283（2026-09-25）以降、ターミナルと VS Code の対話セッションの既定は auto mode」の前に「Pro・Max・Team は 2026-08-14 から（v2.1.228 以降で機能フラグを取得するセッション）」を足し、後ろに「CHANGELOG では v2.1.283 が他社の基盤とテレメトリなしのセッション、v2.1.284（09-28）がすべてのプランと提供元」を足す

### 4.2 調査資料 00

| 場所 | 現 | 案 |
| --- | --- | --- |
| §1（85行） | 「2026年1月の v2.0.77 から10月末の v2.1.312 までに約235版が出ている」 | 「2025-11-01〜2026-10-31 の12か月に315版（月に約26版）が出ている（npm registry の公開日時、2026-11-03 確認）」。範囲を変えたくなければ「v2.0.77〜v2.1.312（2026-01-06〜10-27）に271版」 |
| §1 の表（80行） | 「`think hard` 系は認識されない。`ultrathink` だけが有効」 | 「think hard などはキーワードとして扱われず、普通の文として渡る（effort の範囲で軽く後押しするだけ）。ultrathink は1ターンだけ深く考えるよう頼む言葉で、v2.1.311 以降の対話のターミナルでは 5.5世代と Fable 5.1 のそのターンを xhigh で動かす」 |
| 分野01（186行） | 「CLAUDE.md は再注入される」 | 「公式の表（Explore the context window）で、そのまま効くもの・入れ直すもの・必要になったら読み直すもの・要約に溶けるものを分けて書く（23 §3.4）」 |
| 分野07（334行） | 「Explanatory と Learning。CLAUDE.md との違い」 | 「組み込みは Default のほかに Proactive・Concise・Explanatory・Learning の4種（Concise は v2.1.237 以降、`/output-style` は v2.1.269 以降、`outputStyle` の値は大文字小文字を区別）。CLAUDE.md との違い」 |
| 分野10（405行） | 「連続ブロックには上限がある」 | 「ツール呼び出しを挟まずに8回続けて止めると、次のブロックは上書きされる（v2.1.143 以降。`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` で変え、0 で上限なし）。`stop_hook_active` で二重の継続を避ける」 |
| 分野10（407行） | 「評価は deny から。前方一致の落とし穴。/permissions」 | 末尾に「パスで縛るのは `Edit(path)` と `Read(path)` だけ。`Write`・`NotebookEdit`・`Glob` にパスを付けたルールは受け付けられるが当たらない（起動時に警告。v2.1.210 以降）」を足す |
| 分野11（425行） | 「Read の deny、sandbox の denyRead」 | 「Read の deny（組み込みの道具と、Claude Code が見分けるシェルのコマンドだけに効く）と sandbox の denyRead（子プロセスまで効くが Read の道具は止めない）を併用する」 |
| 分野11（428行） | 「93% が承認されている」 | 「手動の承認の確認の93%（2026-03 の記事）〜97%（2026-08 の記事）が承認されている」 |
| 分野12（453行）・分野14（494行） | 「トークンは約7倍」「agent teams は約7倍」 | 「teammate が plan mode のとき、通常のセッションの約7倍」 |
| §6（775行） | 公式同士の食い違いは2件 | 食い違いの2件はそのまま。足す文：「既定の effort は面ごとに違う（Sonnet 5.5 は Claude Platform で high、Claude Code とアプリで medium。Fable 5.1 は Claude Code と API で high、claude.ai と Cowork で medium。Opus 4.7 は API で high、Claude Code で xhigh）。これは食い違いではないので、facts.yml に面ごとの値として持つ」 |
| §7（878行） | 本文を取得できていないものに「What survives compaction の完全な一覧」 | この項目を外す（23 §3.4 で取得済み） |
| §7（880行） | 「auto mode の承認率は、公式の engineering ブログでは93%、二次報道では97%」 | 「auto mode の承認率は、2026-03-25 の engineering の記事では93%、2026-08-07 の Claude の blog では97% で、どちらも公式である（測った期間の説明はない）」 |
| 台帳（722行） | 「強調は1行だけにし、守られないなら hook・deny へ」「2026（公式の撤回表）」 | 「強調せず平易に1行で書く。守られないなら、ファイルを短くするか hook・deny へ」「2026-10-27 ごろ（Best practices の改稿で撤回の表に入った）」 |
| 台帳（721行） | 「2026-01〜03 に変遷」 | 「v2.1.68（2026-03-04）に ultrathink が復活、v2.1.311（10-26）からそのターンを xhigh に」 |
| 台帳（725行） | 「200k を前提に…」の時期「2026」 | 「2026-10-27 ごろ（Best practices の改稿）」 |
| 台帳（727行・726行） | keep going・アーキテクチャの行の「2026（公式の撤回表）」 | 「2026-10-27 ごろ（Best practices の改稿）」 |

### 4.3 調査資料 03・05・10・11

| ファイルと場所 | 案 |
| --- | --- |
| 03 Q1 の前提（18行）・T6（294行） | 出典を GIGAZINE から [Auto mode is now the default in Claude Code](https://claude.com/blog/auto-mode-default-in-claude-code)（2026-08-07）に差し替える。「89% を検出した」に「1,053人の有償の被験者の実験で、1回の確認を危ないコマンドに差し替えたとき。人は13.6%」を足す。「8月14日から Pro/Max/Team の既定」の後に「対話セッション全体は v2.1.283〜284（2026-09-25〜28）から」を足す |
| 03 Q5 P6（346行） | 「全モデルの既定が high または xhigh になった」→「（2026-04-23 のポストモーテムの時点で）Opus 4.7 は xhigh、ほかのモデルは high になった。その後の Opus 5.5・Sonnet 5.5・Haiku 5.5 は、Claude Code の既定が medium である（2026-11-03 確認）」。「現在も有効か」の ultrathink の文は、23 §3.5 の版で書き直す |
| 03 Gaps（371行） | 「Opus 5.5 における ultrathink の挙動は確認できなかった」→ 削るか、「確認した（23 §3.5）」とする |
| 03 X6（221〜225行） | 「現在も有効か：有効」に「ただし現行の Best practices は『コンテキストを守るために subagent を使う』を古い助言とした。うるさい出力を本筋から離す・並列・独立のレビューのために使い、どれもトークンがかかる」を足す |
| 05（145行） | 「93% を承認している」に「（2026-03-25 の記事。2026-08-07 の記事は97%）」を足す |
| 05（149行） | 「headless（-p）ではプロセスが終了する」→「2026-03-25 の記事では -p はプロセスを終えるとしていたが、現行の文書（2026-11-03）では、`--permission-prompt-tool` のない -p はしきい値に達してもその操作を実行しないだけで、実行は止めない」 |
| 05（197行） | 「What survives compaction は取得できず」→「取得した（23 §3.4）」 |
| 10 第12章（215・217行） | 根拠の文「Anthropic の現行のベストプラクティスは、ほぼすべての推奨を…から導いている」→「Anthropic の Best practices は 2026-10-26 ごろまで、ほぼすべての推奨を…から導いていた。現行の版はこれを古い助言とし、溢れることはまれだが、焦点の合った文脈のほうが答えがよく安いとする」（11 C-25 の扱いと同じ） |
| 10 冒頭（7行）・付録B（631行） | 「1年で約310回」→「直近の12か月（2025-11〜2026-10）で315版（npm registry、2026-11-03 確認）」 |
| 10 付録A-1（376行） | 「連続8回で上書き」→「ツール呼び出しを挟まずに8回続けると上書き」 |
| 11 3-2 #1 | 「公式同士の食い違いで…3件目として足し」→「面ごとの既定の違い（Sonnet 5.5 の発表が明記）。食い違いとしては数えず、facts.yml に面ごとに持つ」 |
| 11 3-2 #5 | 「skill の一覧（description）は戻らない」→「skill の説明文は v2.1.304 以降、今の skills から作り直して入れ直す。バックグラウンドのコマンドと subagent は動き続け、hook が足した文脈は会話と一緒に要約される」 |
| 11 3-2 #10・11a（229行） | 「MAIN の値を、期間を明示して使う」→「MAIN の『約235版』は npm の記録と合わない（271版）。npm で数え直した値を使う（23 §3.6）」 |

### 4.4 requirements §10.1

| 項目 | 案 |
| --- | --- |
| 1 | 「下調べノート `01` の KQ1 の要約・0-3・2-1（と KQ2 の要約の④）にある「コンテキストはすぐ埋まり、埋まるほど性能が落ちる」が中心という書き方は、改稿前の Best practices（〜2026-10-26）のもの。2026-10-27 ごろの改稿で「もうやめてよい助言」に入った（1M と自動圧縮。/clear は質とコストのため）。01 の 2-1 は全体が改稿前の版の要約で、調査資料の中で読んだ版が混ざっている」 |
| 6 | 末尾に「11 3-2 #5 の『skill の一覧は戻らない』は v2.1.304 以降は誤り（23 §3.4）」を足す |
| 8 | 「Sonnet 5.5 の既定 effort は、Claude Platform（API）で high、Claude Code とアプリで medium。面ごとの既定で、公式同士の食い違いではない（2026-09-28 の発表が明記）。Fable 5.1 と Opus 4.7 も面で既定が違う。facts.yml には面ごとに持つ」 |
| 9 | 末尾に「ultrathink は v2.1.311（2026-10-26）以降、対話のターミナルでそのターンを xhigh で動かす（23 §3.5）」を足す |
| 10 | 「Claude Code のリリース数は、npm の公開記録で期間を明記した一つの数字にそろえる。『1〜10月で約235版』は誤りで、v2.0.77〜v2.1.312 は271版、2026年1〜10月は274版、2025-11〜2026-10 の12か月は315版（2026-11-03 確認）」 |

### 4.5 decisions・設計への提案（メインの判断に）

- **雛形の動作確認**（decisions 2026-11-03）：`claude -p` の既定の権限モードは Manual（`default`）で、v2.1.302 以降は承認の要る呼び出しを拒否する。雛形を `claude -p` で確かめるときは、`--permission-mode` か `--allowedTools` を必ず明示し、その値を検証ノートに書く。auto mode で確かめる雛形は、連続3回・合計20回のブロックで `-p` では操作が実行されないまま続く点も記録する
- **hooks と permissions**（decisions 2026-11-03）：制作の `.claude/settings.json` でパスを縛るときは `Edit(...)`・`Read(...)` で書く（`Write(...)` は当たらない）。Read の deny は子プロセスに効かないので、秘密と評価資産は sandbox と併用する（R7 と重なる）
- **鮮度の仕組み**（設計）：公式文書は予告なく大きく書き直される（Best practices は 2026-10-27 ごろ）。調査と検証で公式のページを読んだら、確認日に加えて、読んだ版を見分ける手がかり（要点の一文や見出しの並び）を data/sources.yml に残すと、版の混在に気づける。Wayback の保存は過去の版を確かめるのに使えた
- **facts.yml の effort**（書き方の方針7）：既定の effort は「モデル × 面（API・Claude Code・アプリ）」の表で持つ。面ごとの違いは「食い違い」として並べず、食い違いの欄は本当に公式同士が合わないときだけに使う

---

## 5. 確かめていないこと

- Proactive の output style が入った版（CHANGELOG に追加の記述がない。v2.1.257 に修正の記述があるので、それより前からある）
- 93%・97% の承認率の、測った期間と母集団（どちらの記事にも書かれていない）
- `-p` で auto mode のしきい値に達したときの扱いが「プロセスを終える」から「実行を続ける」に変わった版（CHANGELOG で見つからない）
- Opus 5.5 と Haiku 5.5 の、アプリでの既定の effort（文書に値がない。アプリのメニューの「Default」の表示を見る必要がある。作者に頼むほどのことかは、メインの判断に任せる）
- 03 の「2026年1月16日に think 系のキーワードが廃止された」（CHANGELOG に記述がない。03 の出典は二次情報）
- 10 が引く Oikon のスライドの「1年で約310回」の、数えた期間（スライドを読んでいない。二次情報）
- 03 が出典にした GIGAZINE の記事（読んでいない。03 の数値は公式の記事と一致する）
- 調査資料の「約235」がどう数えられたか（312−77 と一致するが、推測で、確かめていない）
- Best practices の改稿の正確な時刻（保存は 10-26 19:44 と 10-27 08:15（UTC）の間までしか絞れない）と、版の公開（v2.1.312 は 10-27 18:36 UTC）との関係
- auto mode の告知で「来月」とした Enterprise・Claude API・クラウドの提供元での既定化が、いつ入ったか（v2.1.284 の「すべてのプランと提供元」で入ったと読めるが、別の告知は探していない）
- Permission modes の Desktop と Web のタブ（アプリでの権限モードの既定）は読んでいない
- 「Ultra」プランの中身（文書と告知に名前があることだけ確かめた）

---

## 6. 使った量の目安

- 道具の呼び出し：約110回（Bash 約85、Read 約10、Write 6、WebSearch 1、ToolSearch 1）
- Web の取得：curl で約60回（code.claude.com 19、platform.claude.com 7、support.claude.com 1、www.anthropic.com 8、claude.com 1、registry.npmjs.org 1、raw.githubusercontent.com 1、web.archive.org 約20）。WebFetch は0回
- AI の利用を断る指定の確認：`tools/check_noai.py` を4回（16の URL）
- Web 検索：1回（auto mode の既定化の公式の告知を探すため）
- 時間：約40分（2026-11-03 20:38〜21:20 ごろ、JST）
