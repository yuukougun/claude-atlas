# 工程3 C4：分野 context・cli の目次

- 担当：C4（context「文脈を整える」・cli「Claude Code の基本操作」）
- 日付：2026-11-04
- 共通の指示：[brief-catalog.md](brief-catalog.md)（v1）
- 書いたファイル：`planning/catalog/context.yaml`・`planning/catalog/cli.yaml`・この報告。ほかのファイルは変えていない。git の操作も Web も使っていない

## 1. 書いたファイルとページ数

| 分野 | ページ | 優先度 | レベル | 型 | registry の候補 |
| --- | --- | --- | --- | --- | --- |
| context | 15 | 必須 11・推奨 4 | 使う 1・整える 6・任せる 8 | concept 10・feature 3・recipe 2 | 19（採る 15・まとめた 4） |
| cli | 19 | 必須 7・推奨 9・任意 3 | 使う 2・整える 10・任せる 6・なし 1（ledger） | feature 15・concept 2・recipe 1・ledger 1 | 19（採る 18・採らない 1）＋新規 1 |

章：

- context：総論／新しくする・巻き戻す／圧縮／書き出す／見る・絞る／脇道を分ける
- cli：入力と基本の操作／権限モードと計画／巻き戻しとセッション／見る・切り分ける／設定と最初の準備／ほかの面と離席／早見表

工程2の前提の反映（指示の「この担当に固有のこと」）：

- **総論と /clear・/compact の要約**：tidy-the-desk（総論）・when-to-start-fresh（/clear の判断）・compact-and-auto-compact（/compact と自動圧縮）の要約は、どれも「溢れを防ぐ節約ではなく、答えの質と費用のための整頓」として書いた。根拠は現行の Best practices（2026-10-27 ごろの改稿の後。research/23 #1・§3.1、00 §1）と、訂正が2回失敗したら /clear するという現行の勧め（research/25 §3.4）
- **注記の付いた主張を根拠にしない**：01 の「埋まるほど性能が落ちる」（KQ1・0-3・2-1）、「status line で常に監視する」（I-2）、「調査は subagent に」（2-1）、03 X6 の「メインのコンテキストを守る」という理由、11 3-2 #5 の「skill の一覧は圧縮の後に戻らない」は、要約・サイン・題名に使っていない。圧縮の後の skill の一覧は v2.1.304 以降は戻る（research/23 #6）と notes に書いた
- **research-in-subagents** は、現行の Best practices が「コンテキストを守るために subagent を使う」をもうやめてよい助言に入れたので、題名を「出力の多い調査は subagent に任せて要約だけ受け取る」にし、理由を「うるさい出力を本筋から離す・独立の調査」にした（トークンが余分にかかることも要約に入れた）
- **idle compaction**（research/22 #15。放置した大きな会話を cache が切れる前に要約する）を compact-and-auto-compact の節にし、registry の breaks-and-cache-expiry をそこにまとめた
- **境界**：/clear と /compact は、判断と操作を context のページに置き、cli の must-know-operations と command-cheatsheet から指した（registry に cli の /clear・/compact の候補がなく、操作だけのページは薄くなるため。設計書 §4.2 への提案は §4）。/goal・並列・worktree・無人実行は delegate のページを related で指した
- **セッション記録から失った作業を取り戻す**（requirements §4.2）：cli の recover-lost-work として採った

## 2. まとめた・採らなかった候補と、新しいページ

まとめた（merged）：

| 候補 | まとめた先 | 理由 |
| --- | --- | --- |
| managing-context-in-the-app（必須） | tidy-the-desk（節 in-the-app） | 面ごとにページを分けない（D9・design §4.1）。アプリの新しいチャット・編集・Projects・Memory は、総論の四つの動作のタブと節に置く。アプリに固有の仕組みは app の long-chat-limits と where-to-put-instructions |
| compaction-settings（任意） | compact-and-auto-compact（節 settings、level 仕組みにする） | 圧縮の機能の変種（design §4.1 の1） |
| breaks-and-cache-expiry（任意） | compact-and-auto-compact（節 idle-compaction） | 公式の idle compaction が対応するようになった（research/22 #15、05 1-6） |
| sessions-as-branches（推奨） | cli の resume-and-branch | 操作と「ブランチのように扱う」判断が同じ単位。design §4.2 で基本操作は cli。registry の notes の重なりの組 |

採らなかった（dropped）：

- **for-non-engineers**：decisions 2026-11-03「読者の前提」（非エンジニア向けの説明は省く）と食い違う。コードを書かない仕事は recipes、Desktop の Code タブは surfaces が持てる。サインの受け皿は §4 で提案した

新しく足したページ：

- **isolate-with-safe-mode**「設定を外して切り分ける（--safe-mode）」（cli、推奨、任せる）：CLAUDE.md・skills・plugins・hooks・MCP などを読まずに起動し、不調が自分の設定から来るかを比べる。権限と管理の設定は効いたまま（research/28 #28、v2.1.169）。症状のページ（instructions-ignored・seems-less-capable・replies-in-english など）の診断から引かれる操作で、起動の仕方なので cli に置いた

registry から変えたもの（理由は各ページの notes）：

- 題名：promises-after-compaction「圧縮で消えない場所に約束を置く」（判断が分かる形に）、progress-files（特定の実践者の4つのファイルの名前を題名から外した）、research-in-subagents（上記）、input-symbols・must-know-operations（数を外した）、checkpoints-and-rewind・when-to-plan・output-style-modes（公式の日本語版の多数派：チェックポイント・plan モード・出力スタイル）、usage-context-statusline・settings-layers・resume-and-branch。旧題は aliases に残した
- level：side-questions-btw と output-style-modes を任せる → 整える（どちらも任せる幅を広げる機能ではなく、会話や応答を整える段階で要る）
- type：ask-claude-code を feature → concept
- priority：recover-lost-work を任意 → 推奨（困ったときに引かれ、公式の機能だけで書ける。根拠の経験談は1件なので必須にはしない）

## 3. wave: 1

付けていない（context と cli は第一波の核の分野ではない）。核のページの前提に入れば、道具が第一波に数える。ほかの分野から前提として指されているのは、permission-modes-overview（safety・enforce から）、checkpoints-and-rewind（safety・recipes から）、always-on-costs（extend から）、choose-what-to-read・working-with-git・when-to-plan（recipes から）、settings-layers（team・enforce から）、handoff-documents（team から）、progress-files（delegate から）。必須のページから指されるものはどれも必須にしてある

## 4. ほかの分野への提案（open_issues の要約）と new_features

すぐに直してほしいもの：

- **symptoms**（書きかけ）：forgets-in-long-chats と unexpected-memories の related の managing-context-in-the-app を tidy-the-desk#in-the-app に、forgot-after-compaction の related の compaction-settings を compact-and-auto-compact#settings に直す（最後の検査で参照のエラー3件。原因は私のまとめ）
- **全分野**：まとめた id（上の4つ）と採らなかった for-non-engineers を指すページがあれば、まとめた先に直す
- app は、managing-context-in-the-app を指していた4ページを、すでに tidy-the-desk#in-the-app に指し直した（app の open_issues の依頼は tidy-the-desk の related で満たした）

提案：

- **symptoms**：forgets-in-long-chats・going-in-circles の対処先に when-to-start-fresh・rewind-dont-correct・handoff-documents、forgot-after-compaction に promises-after-compaction と compact-and-auto-compact#idle-compaction。instructions-ignored・seems-less-capable・replies-in-english・blames-the-tools の診断に isolate-with-safe-mode。forgets-in-long-chats（使う）の前提にできるのは when-to-start-fresh（使う）だけ
- **basics**：what-survives-compaction は research/23 §3.4 で書き、11 3-2 #5 を使わない。requirements §2 の動く図「コンテキストの埋まり方」は公式の Explore the context window が対話で見せている（21 §2.4）ので、自作するか（basics の attention-budget）リンクで済ませるか（context の inspect-context から）を決める（未決）
- **changes**：台帳に「コンテキストを守るために subagent に調査させる」を足す（現行の Best practices の What you can stop doing の表。既存の tell-it-to-use-subagents とは出どころと理由が違う）。save-context-for-200k の「今どうするか」に idle compaction を足す（research/22 §3.4）。checking-for-updates に stable の通り道の遅れ（research/22 #3）を書く
- **recipes か surfaces**：00 §4 のサイン「コードを書かない仕事に Claude Code を使いたい」の受け皿（office-paperwork か claude-code-vs-cowork）。00 分野07 の「作業用のフォルダと手動のモードで始める」は office-paperwork か safety の default-safety-settings へ
- **enforce・safety**：permission-modes-overview（整える）は、緩める判断の本体（what-auto-mode-stops・where-bypass-is-ok・sandboxing）を前提にせず related で指している
- **delegate**：progress-files（対話で再開するための状態）と progress-logs-for-long-jobs（無人のジョブの記録）の境界。cloud-sessions-and-teleport ほかは並列・無人の使い方を delegate に任せた
- **start（glossary）**：plan モード（Claude Code の日本語版の79%）とプランモード（Help Center）の表記を決める（research/27 §3.1）
- **設計書 §4.2**：「基本操作（起動・権限モード・/clear・/compact・rewind・plan mode）→ cli」の行に、/clear と /compact は判断と操作を context に置き cli から指す、と書き足す

確認だけのもの：ほかの分野が先にまとめた4つ（enforce の spoken-prohibitions-fade → when-to-lock、cost の claude-code-costs → what-uses-up-limits、extend の what-to-leave-out-of-claude-md → what-to-put-in-claude-md、changes の old-and-new-names → glossary、api の files-pdfs-and-images → how-attachments-are-read）は、まとめた先（節があれば id#anchor）に指し直した

new_features（tracks で使う、README §5 にない機能）：

| id | 中身 | 使うページ |
| --- | --- | --- |
| `btw` | /btw（会話の履歴に残らない横道の質問） | side-questions-btw |
| `interactive-mode` | 対話モードの操作（入力の記号・キーボードショートカット） | input-symbols・must-know-operations |
| `sessions` | セッションの保存・再開・分岐・命名と transcript | resume-and-branch・recover-lost-work |
| `safe-mode` | --safe-mode（自分の設定と拡張を読まずに起動） | isolate-with-safe-mode |

## 5. 検査の結果

`python3 tools/check_catalog.py --field context` と `--field cli`（2026-11-04 の最後の検査。分野のファイル23・ページ348を読んだ時点）：

- context：エラー 0、警告 2（どちらも未処理の候補）
- cli：エラー 0、警告 6（すべて未処理の候補）

残した警告は、symptoms の候補（wont-rethink-approach・wrong-amount-of-approvals・deleted-something-important・hits-limits-quickly・seems-less-capable・blames-the-tools）を related で指しているもので、symptoms.yaml が書きかけのために出ている。その分野の担当が採れば消える。まとめられたら、まとめた先に直す必要がある

途中で出て直したもの：ほかの分野がまとめた id への参照のエラー（上の5つ）、比例則の警告1件（compact-and-auto-compact。when-to-lock#spoken-rules-fade を指して解消）

全体の検査では、私のまとめが原因のエラーが symptoms.yaml に3件ある（§4 の最初の項目）。app.yaml の4件は app の担当が直した

## 6. 確かめていないこと・迷った点

- **managing-context-in-the-app をまとめるか**：D9 に従ってまとめたが、app と symptoms の担当はこの id を指していた（app は判断の本体として4ページから。app はその後 tidy-the-desk#in-the-app に指し直した）。中身（いつ新しい会話にするか・何を持ち越すか）は when-to-start-fresh と tidy-the-desk#in-the-app と app の where-to-put-instructions で足りると判断した。メインが別のページとして残すほうがよいと考えるなら、tidy-the-desk の節を切り出せばよい
- **inspect-context と always-on-costs と cli の usage-context-statusline の三つ**：重なりが大きく、二つにまとめる案も考えた。always-on-costs はほかの分野の18か所から、inspect-context は6か所から指されていたので、まとめずに、道具の一覧（cli）・内訳の読み方（inspect-context）・常駐を小さく保つ理由（always-on-costs）に分けた
- **plan モードの使いどころ**：「diff を一文で説明できる変更なら計画を省いてよい」は現行の Best practices で見つかっていない（11 第4節 #13）。要約は「方針や範囲に迷いがある作業で使う」という一般の形にし、執筆で現行の文書を確かめるよう notes に書いた。「方針が不確か・複数ファイル・不慣れなコード」という公式の挙げ方が現行の版にも残るかも確かめていない（01 2-1 は改稿の前の版の要約）
- **CLAUDE.md に書く圧縮の方針（Compact instructions）**：Manage costs の文書にある（05 1-6）が、改稿の前の Best practices の要約（01 2-1）にも出るので、執筆で現行の文書を確かめる
- **キーボードショートカット**：Ctrl+G は改稿の前の Best practices の例に出る（01 2-1 の注記）。操作そのものは Interactive mode の文書にある（01 N-1）が、現行で確かめていない。キーの割り当ては数値ファイルに置き、WSL・Linux の CLI を基準にする
- **level の見当**：他分野の level は検査の時点の値で前提の逆転を確かめた。basics が context-rot を「使う」にしたので、when-to-start-fresh（使う）の前提に入れた。ほかの担当が level を上げると逆転の警告が出うる
- **for-non-engineers**：採らなかったが、00 §1 は日本語圏の需要が「コードを書かない使い方」に集まると書く。読者を開発の経験がある人に絞った決定（decisions 2026-11-03）のもとでも、開発者がコードでない仕事に使う話は recipes が受けると考えた
- **IDE の拡張**：動作は試していない（公式の文書と確認日で書く。research/26 §3.4）
