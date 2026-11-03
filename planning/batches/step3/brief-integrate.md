# 工程3：目次の統合の担当への共通の指示

- 版：2026-11-04 v1
- 担当ごとの受け持ちは [README.md](README.md) の3段目の表にある

## 1. 背景

claude-atlas は、Claude 全般を使いこなすための、辞書として引く日本語の教材である。読者は開発の経験がある人。リポジトリは `/home/yuuki/projects/kyopro2/claude-atlas`。今日は 2026-11-04。

23分野の目次（`planning/catalog/<field>.yaml`）は、12人の担当が並列に書いた。担当は、ほかの分野への提案を自分のファイルの `open_issues` に書いた（全165件）。また、症状辞典の担当が、逆引きの「やりたいこと（goal）」と「状況（situation）」の40項目を、ほかの分野のどのページに置くとよいかを表にした（`catalog-C12.md` §7）。

あなたは、受け持ちの分野のファイルに、これらの提案を反映する。分野ごとに持ち主を1人に決めてあるので、ほかの担当と同じファイルを書くことはない。

## 2. 最初に読むもの

1. `planning/catalog/README.md`（全部。形式と規則）
2. `planning/design.md` の §2〜§4 と §6.2（分野と型、レベル、キーの台帳、粒度と境界、用語）
3. `schema/site.yml`（語彙）
4. 自分の材料：`state/step3-integrate/<担当>-input.md`（A は受け持ちに関わる open_issues、B は逆引きの行。メインが広めに抜き出した。全体は `planning/batches/step3/open-issues.md`）
5. 受け持ちの分野のファイル（全部）と、それを書いた担当の報告（`planning/batches/step3/catalog-C*.md`。README の2段目の表で分かる）
6. 必要なら：`planning/catalog/registry.yaml`・`features.yaml`、`planning/research/27-japanese.md` §3.1（用語の表）、ほかの分野のファイル（読むだけ）、調査資料（00〜11・21〜28）

## 3. メインが決めたこと（統合の前提）

**M1 題名の表記**：公式の日本語版の本文の多数派に合わせる（design §6.2、research/27 §3.1・§4 P11 の (a)）。受け持ちの分野の `title` と `summary` をこの表で揃える。`signs` は読者の言葉なので変えなくてよい。題名を変えたら、元の英語の名前を `aliases` に入れる（題名と同じ語は入れない）。機能名・コマンド・ファイル名・設定のキーは原文のまま書く。

| 英語 | 書く表記 |
| --- | --- |
| subagent | サブエージェント |
| hook・hooks | フック（イベント名と matcher は英語のまま） |
| skill・skills | スキル |
| plugin・marketplace | プラグイン・マーケットプレイス |
| permissions・permission mode | 権限・権限モード |
| allow／ask／deny のルール | 許可ルール・確認ルール・拒否ルール（**仮**。aliases に「allow ルール」「deny ルール」など） |
| sandbox | サンドボックス |
| auto mode | auto モード |
| plan mode | plan モード（**仮**。aliases に「プランモード」） |
| compaction・auto-compact | 圧縮・自動圧縮 |
| context window | コンテキストウィンドウ |
| effort | effort（**仮**。aliases に「努力レベル」） |
| output style | 出力スタイル |
| memory・auto memory | メモリ・自動メモリ（アプリのものと分けるときは「アプリのメモリ」） |
| agent teams | エージェントチーム |
| extended thinking | 拡張思考 |
| prompt caching | プロンプトキャッシング |
| managed settings | 管理設定 |
| checkpoint | チェックポイント |
| worktree | worktree（英語のまま） |
| non-interactive mode | 非対話モード |
| system prompt・frontmatter | システムプロンプト・フロントマター |
| アプリの Projects・Memory・Incognito chats・Artifacts・Research・Connectors・Skills・Voice mode | プロジェクト・メモリ・シークレットチャット・アーティファクト・リサーチ・コネクタ・スキル・音声モード |
| Project instructions・Instructions for Claude | プロジェクトの指示・Claude への指示（画面の名前は確かめていない） |
| API の機能名（Messages API・tool use・structured outputs など） | 英語のまま（Platform の日本語版の訳語は調べていない）。プロンプトキャッシングだけ上の表のとおり |

「仮」の3つは、工程5でユーザーに確かめる。

**M2 逆引き**：材料の B の行の「項目」を、向く先の受け持ちのページの `signs` に足す。

- `type` は表の種類（「goal（問い）」は goal）。文は読者の言葉のまま。変わりやすい値とモデル・プランの名前は使わない（#60 は「どのプランにすべきか迷う」、#61 は「いちばん高性能なモデルを使ってみたい」の形）
- 同じ意味の sign がすでにあれば足さない。向く先が複数のときは、その項目に直接答えるページに足す（受け持ちの中で多くて3ページ）
- 症状（symptom）の33項目は、症状のページの signs にすでにある。対処のページに同じ文を重ねて置かない（逆引きで同じ文が二か所に出ると、症状のページの振り分けを飛ばす読み方になる）

**M3 台帳**：registry の `ledger` に `styles-for-tone`（Styles で応答の調子と形式を切り替える）と `subagents-to-save-context`（コンテキストを守るために subagent に調べさせる）を足した。関わるページの `outdated_advice` に入れてよい。

**M4 機能の id**：`planning/catalog/features.yaml` に、README §5 の表と担当の new_features をまとめた。`tracks` はここの id を使う。足りない機能は自分のファイルの `new_features` に足し、報告に書く。

**M5 断られたとき**：decisions 2026-11-03「断られたときの頼み直し」に従う。書くのは公式が案内する手段だけ（本当の目的と文脈を足す〔偽らない〕、巻き戻しや新しい会話で引き金になった内容を外す、誤判定を報告する、専門の仕事には検証の制度を案内する）。アプリの自動のモデル切り替えは仕組みとして説明する。「モデルを変える」を通すための手段として書かない。言い換え・分割・偽の文脈は書かない。

**M6 安全の既定の正本**：safety の `default-safety-settings#by-stage` を正本にする。start の `four-principles` と `roadmap` から related で指す。

**M7 用語集**：start の `terminology` の notes に、M1 の仮の決定と、用語集で決める点（plan モード／プランモード、effort／努力レベル、許可ルール／allow ルール、アプリのメモリと Claude Code のメモリ・自動メモリの区別、アプリの Styles と Claude Code の出力スタイルの区別、API の訳語は Platform の日本語版を確かめてから決めること、旧名は数値ファイルの名称の項目から生成すること）を書く。

**M8 動く図**：basics の `rereads-whole-history` の動く図を自作するか公式の対話の図にリンクするかは、執筆のときに公式の図と比べて決める。目次は変えない。

**M9 比例則の警告**（いまの6件）：basics の `why-prompt-caching`、extend の `agents-md`・`how-skills-load`、api の `feature-to-api-mapping`・`prompt-caching-in-practice`、team の `ideate-independently`。任せる幅を広げる内容なら、verify・eval・enforce・safety のページを related に足す。広げない内容なら notes に理由を書く（警告は残ってよい）。level がそもそも合っているかも見る。

**M10 wave**：`wave` は変えない（第一波はメインが決める）。

**M11 生成のページ**：本体を生成するページの印のキーは目次に足さない（土台作りで、生成の道具の設定に持つ）。notes の書き方はそのまま。

## 4. すること

1. 材料の A の各項目を読み、受け持ちの分野に関わる変更を、自分のファイルに反映する。「取り込み済み」とある項目は、本当に入っているかを確かめる
2. 材料の B の行を、M2 のとおり signs に足す
3. 受け持ちの分野の題名と要約を、M1 のとおり揃える
4. M9 の警告が受け持ちにあれば扱う
5. 検査する（§6）
6. 報告を書く（§7）

## 5. してよいこと・しないこと

- 書いてよいのは、受け持ちの分野のファイルと、自分の報告（`planning/batches/step3/integrate-<担当>.md`）だけ。registry・features・設計書・ほかの分野のファイルは変えない
- **ページの id と、sections の anchor を消さない・変えない**（ほかの担当が同時に指している）。anchor を足すのはよい
- ページの分野をまたぐ移動、ページの統合（id が消えるもの）、削除はしない。要ると思えば、報告の「メインへ」に書く
- 新しいページは、提案がはっきり求め、受け持ちの分野に置くのが境界の表（design §4.2）に合うときだけ足す。notes に「新規（2026-11-04 統合）：理由」と書く
- `priority`・`level` を変えるのは、提案が求め、規則（必須のページの前提は必須、前提に上の段を置かない）が保たれるときだけ。notes に理由を書く
- 変えたページの notes の末尾に「（2026-11-04 統合：<材料の番号>）」を足す
- 調査資料の訂正・注記の付いた主張（`【2026-11-03 訂正】`・`【2026-11-03 注記】`）を、summary・signs・題名の根拠にしない
- summary・signs・title に、変わりやすい値（数値・既定値・料金・モデルの世代・上限）を書かない
- 第三者を否定的な文脈で名指ししない（materials と notes にも、個人の名前を書かない）
- git の操作をしない。Web を開かない

## 6. 検査

受け持ちの分野ごとに `python3 tools/check_catalog.py --field <field>` を走らせ、エラーを0にする。ほかの担当も同時にほかのファイルを書いているので、ほかの分野のファイルが原因のエラーが出たら、少し置いてから走らせ直す（それでも残れば報告に書く）。警告は、理由を notes に書けば残してよい。

## 7. 報告の形（`planning/batches/step3/integrate-<担当>.md`）

1. 材料 A の各項目の扱い（表：番号｜扱い〔反映した・反映しない・メインへ・対象外・取り込み済みを確かめた〕｜変えたページと、反映しないときの理由）。全項目を書く
2. 材料 B の行の扱い（足したページと sign の文、足さなかった理由）
3. 題名を変えたページ（前 → 後）
4. 新しいページ、priority・level を変えたページと理由
5. メインへ（分野をまたぐ移動・統合、設計書や道具への提案など、判断の要るもの）
6. 検査の結果（エラー・警告の数と、残した警告の理由）
7. 確かめていないこと、迷った点

最後の返答（メインへの報告）は300字まで。
