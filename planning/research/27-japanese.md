# 工程2 R6：日本語で使う（公式の日本語訳・出力を揃える仕組み・英語への回帰）

- 版：2026-11-03 v1
- 担当：R6（[batches/step2/README.md](../batches/step2/README.md)）。共通の指示は [brief.md](../batches/step2/brief.md)
- 割り当て：初版の第一波に足した「日本語で使う」の核（decisions.md 2026-11-03「第一波に足すもの」）の材料。関わる調査資料は `04-community-japanese.md`（Q3・Q6・F）と `00-content-report.md` の分野15
- 確認日：すべて 2026-11-03。手元の Claude Code は 2.1.317（`claude --version`）。公式の文書は、その日に配信されていた版（CHANGELOG は 2.1.317・2026-11-03 まで）を読んだ
- 注意：GitHub の issue の報告者の数値は、どれも利用者が自分の記録を数えた自己申告である。この報告では個人のアカウント名を出さず、issue の番号で示す

---

## 1. 調べた範囲と方法

### 1.1 方法

- 公式の文書は、URL が分かるものを検索せずに直接取得した。code.claude.com と platform.claude.com は `.md` 版を `curl` で取得し、support.claude.com は HTML から本文を抜き出した。取得したものは作業用のフォルダに置き、`grep` と短い Python で数えた
- 公式の日本語訳の訳語は、code.claude.com/docs/ja の主なページ29本（用語集・sub-agents・hooks・hooks-guide・skills・plugins・permissions・permission-modes・sandboxing・context-window・model-config・output-styles・memory・settings・settings-reference・best-practices・features-overview・how-claude-code-works・costs・agent-teams・interactive-mode・commands・cli-reference・statusline・env-vars・plugins-reference・discover-plugins・checkpointing・auto-mode-config）の本文で、表記ごとの回数を数えた。コードの塊・インラインコード・リンク先の URL は数えていない
- 英語への回帰の記録は、`gh search issues --repo anthropics/claude-code` で題名と本文を検索し（英語の語で17回）、出てきた705件の題名から返答の言語に関わるものを選び、43件の本文とコメントを `gh issue view` で読んだ
- Web 検索は1回だけ使った（日本語圏でクラスメソッド以外の報告があるかの確認）
- `claude -p` などで Claude Code を動かす確認はしていない（brief §4）

### 1.2 使った一次資料

Claude Code の公式の文書（code.claude.com）

- 文書の索引：https://code.claude.com/docs/llms.txt ・日本語の索引：https://code.claude.com/docs/_llms/jp.txt ・全文：https://code.claude.com/docs/llms-full.txt
- 設定の一覧（`language`）：https://code.claude.com/docs/en/settings-reference#language （日本語版 https://code.claude.com/docs/ja/settings-reference ）
- 用語集：https://code.claude.com/docs/en/glossary ・https://code.claude.com/docs/ja/glossary
- output style：https://code.claude.com/docs/en/output-styles
- CLAUDE.md と自動メモリ：https://code.claude.com/docs/en/memory
- サブエージェント（起動時に読み込むもの）：https://code.claude.com/docs/en/sub-agents#what-loads-at-startup
- 圧縮の後に残るもの：https://code.claude.com/docs/en/context-window#what-survives-compaction
- hooks の仕様：https://code.claude.com/docs/en/hooks （UserPromptSubmit・MessageDisplay・Stop・PostToolUse・終了コード）・入門：https://code.claude.com/docs/en/hooks-guide
- Best practices：https://code.claude.com/docs/en/best-practices
- システムプロンプトの外で足される文脈：https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts
- system prompt のフラグ：https://code.claude.com/docs/en/cli-reference#system-prompt-flags
- クラウドのセッションに届く設定：https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup ・https://code.claude.com/docs/en/settings#settings-in-cloud-sessions
- 権限のルール（MultiEdit は legacy）：https://code.claude.com/docs/en/permissions
- CHANGELOG：https://code.claude.com/docs/en/changelog （GitHub の CHANGELOG.md から生成されたもの）

Claude Platform の文書（platform.claude.com）

- 多言語の対応：https://platform.claude.com/docs/en/build-with-claude/multilingual-support （日本語版 https://platform.claude.com/docs/ja/build-with-claude/multilingual-support ）
- 用語集（トークン）：https://platform.claude.com/docs/en/about-claude/glossary ・日本語版 https://platform.claude.com/docs/ja/about-claude/glossary
- Opus 5.5 の移行の手引き（トークナイザー）：https://platform.claude.com/docs/en/models/opus-5-5/migration-guide
- Opus 5.5 の頼み方の手引き・新機能・claude.ai の system prompt（言語の記述がないことの確認）：prompting-claude-opus-5-5、whats-new-opus-5-5、release-notes/system-prompts/claude-opus-5-5

Claude のヘルプセンター（support.claude.com）

- 好みの言語で使う：https://support.claude.com/en/articles/10769299 （日本語版 https://support.claude.com/ja/articles/10769299 ）
- 個人設定の機能：https://support.claude.com/en/articles/10185728 （日本語版あり）
- プロジェクトの作成と管理：https://support.claude.com/en/articles/9519177 （日本語版あり）
- 組織の指示：https://support.claude.com/en/articles/14546867 （日本語版あり）
- Claude Code チートシート：https://support.claude.com/en/articles/14553413 （日本語版あり）
- モデル・effort・思考の設定：https://support.claude.com/en/articles/8664678 （日本語版あり）
- シークレットチャット：https://support.claude.com/en/articles/12260368
- リリースノート：https://support.claude.com/en/articles/12138966
- 記事の一覧：https://support.claude.com/sitemap.xml

GitHub（anthropics の公開リポジトリ）

- issue（番号は §3.3 の表）：https://github.com/anthropics/claude-code/issues
- 公式の例とプラグインの一覧：https://github.com/anthropics/claude-code （examples・plugins）、https://github.com/anthropics/claude-plugins-official

二次・実践者の資料（一次資料を探す手がかり、または「その人が観察したこと」の一次資料として読んだ）

- クラスメソッド（DevelopersIO）の記事（2026-10-20）：https://dev.classmethod.jp/articles/claude-code-hooks-prevent-english-reply/
- Zenn の textlint の記事（2025-07-26 公開、07-28 更新）：https://zenn.dev/yuki_fujisawa/articles/a01e472dc190cf
- note の個人の記事（2026-09-29）：https://note.com/good_nerine619/n/n93163a04fb77

### 1.3 AI の利用を断る指定の確認（`python3 -I tools/check_noai.py`、2026-11-03）

| ドメイン | 結果 | 備考 |
| --- | --- | --- |
| code.claude.com | 指定なし | robots.txt にも AI 向けの指定なし |
| support.claude.com | 指定なし | meta robots は `all` |
| platform.claude.com | 指定なし | |
| github.com | 指定なし | robots.txt は AI 向けのクローラに検索や一部のパスを Disallow している。issue は `gh`（GitHub の API）で読んだ |
| dev.classmethod.jp | 指定なし | meta robots は `index, follow` |
| zenn.dev | 指定なし | |
| note.com | 指定なし | |
| www.issoh.co.jp | 指定なし | ただし HTTP 403 で本文を取得できない（返ってきたページの meta robots は `noindex, nofollow`）。読んでいない |

atcoder.jp と codeforces.com は開いていない。

---

## 2. 結果の一覧

「場所」は調査資料のファイルと節。結果は 正しい／誤り／一部誤り／確かめられない の4つで示す。

| # | 主張とその場所 | 結果 | 正しい内容（一次資料に基づく） | 出典（確認日 2026-11-03） | 教材への影響 |
| --- | --- | --- | --- | --- | --- |
| 1 | 公式の Claude Code の文書には日本語訳がある（00「調査の空白…」の末尾、06 §「公式ドキュメントは日本語訳されている」） | 正しい | 日本語版は英語版と同じ228ページがそろっている（英語の索引の重複を除いた228ページと、日本語の索引の228ページが一致）。変更履歴だけは訳されておらず、日本語版の URL は英語の CHANGELOG.md（GitHub）へ転送される。調べた29ページでは、ページ中の版番号（最大 2.1.314）が英語版と同じで、更新は追いついている。翻訳の方法（機械翻訳か）は、調べたページには書かれていない | llms.txt の「Indexes」、`_llms/jp.txt`、`/docs/ja/changelog` の転送先 | 用語集と prh の基準。§3.1 |
| 2 | `~/.claude/settings.json` に `"language": "japanese"` を書くか `/config` で設定する（04 Q3） | 正しい | `language` は公式の設定のキー。英語以外で返答させる指示として、値をそのまま Claude に渡す。どのファイルにも書ける。音声入力のページは、`/config` からも設定でき、言語名でも BCP 47 の符号（`ja`）でもよいとする。追加は v2.1.0（2026-01-07） | settings-reference#language、voice-dictation、CHANGELOG 2.1.0 | 分野15「日本語で返し続けさせる」 |
| 3 | 値はチェックされないので、綴りを誤ってもエラーにならない（04 Q3、SSD Nodes） | 正しい | 公式に「値を検証しない。誤った綴りは書いたまま Claude に届く」とある。同じ値が音声入力の言語と、自動で付くセッションの題名の言語も決める。未設定なら題名は会話の言語に合わせる | settings-reference#language | 同上。症状ページの確認欄 |
| 4 | `language` はコメントやコミットメッセージには効かない（04 Q3、00 分野15。出典は Issoh、v2.1.308） | 確かめられない | 公式の文書には、`language` がコミットメッセージ・コードのコメント・圧縮の要約・思考の要約に効くかどうかの記述がない（llms-full.txt 全文を検索）。Issoh の記事は HTTP 403 で読めなかった | settings-reference、llms-full.txt | 分野15「コミットメッセージ・コメントの言語」は「公式の記述なし」と書き、検証ノートにする |
| 5 | `language` を共有のプロジェクト設定に入れると、個人の設定を上書きしてしまう（04 Q3） | 正しい | 設定の優先順は 管理 > `--settings` > `.claude/settings.local.json` > `.claude/settings.json` > `~/.claude/settings.json`。値が1つのキーは上の層が下を上書きする。リポジトリの `.claude/settings.json` の `language` は各人の `~/.claude/settings.json` より優先される | glossary「Settings layers」、settings | 分野15。OSS では個人の設定に置く、という助言の根拠 |
| 6 | 効かないときは JSON の誤り、上位のスコープ、CLAUDE.md 内の英語の指示を確かめる（04 Q3、GiftX） | 一部確かめられない | スコープの優先順は公式（#5）。JSON の誤りと CLAUDE.md の英語の指示は、公式の文書に診断の手順としては書かれていない（妥当な推測） | settings | 症状ページの診断チェックリスト（安く確かめられる順） |
| 7 | Opus 5.5 は英語のツール出力やサブエージェントの報告を読んだ後に英語へ戻る（04 Q3、00 §1・分野15。出典はクラスメソッドの1件） | 正しい（裏付けが増えた） | 調査資料の出典は1社だけだが、一次の記録はそれより多い。Opus 5.5 の公開（2026-09-22）の翌日から、GitHub に同じ症状の issue が少なくとも16件（うち12件は Opus 5.5 と明記）あり、#96326 のコメントでは日本語のほかヘブライ語・イタリア語・韓国語・繁体字中国語・ドイツ語・ロシア語・ペルシア語の利用者が、自分の記録を数えた割合を報告している。Anthropic の担当者の返答は、読んだスレッドにはなく、CHANGELOG（2.1.317 まで）に直した記録もない。根拠の強さは「中」（§3.3） | §3.3 の issue、CHANGELOG | 分野15・症状辞典「英語で返ってくる」。根拠の強さ「中」と確認日を付けて書ける |
| 8 | CLAUDE.md やメモリでの指示は一時的にしか効かない（04 Q3） | 正しい | 公式は、CLAUDE.md と自動メモリを「強制される設定ではなく文脈」として扱い、厳密に守られる保証はないとする。CLAUDE.md はシステムプロンプトの後のユーザーメッセージ（system reminder）として届く。issue でも、訂正の直後は日本語に戻るが、またすぐ英語になる、という報告が多い | memory、glossary「System reminder」、#96326・#98633・#99704 | 背骨の「お願いと鍵」の実例 |
| 9 | japanese-reply は UserPromptSubmit・Stop・MessageDisplay と PreToolUse の3層で、MessageDisplay と PreToolUse で途中の英語の発話を差し戻す（04 F・Q3） | 正しい | 記事の設計と一致する。ただし公式には、MessageDisplay は表示だけを差し替える hook で、メッセージを止めることも、Claude が見る内容を変えることもできない（v2.1.152 で追加）。記事は MessageDisplay で英語の一言を見つけて印を残し、次の PreToolUse でツールの実行を止めて言い直させている。記事も「英語が一度画面に出るのは防げない」と書く | hooks#messagedisplay、CHANGELOG 2.1.152、クラスメソッドの記事 | 雛形の注記。「途中の一言は Stop では拾えない」 |
| 10 | クラスメソッドは UserPromptSubmit・Stop・MessageDisplay の hook で日本語を強制する解決策を作った（00 分野15） | 一部誤り | PreToolUse が抜けている。MessageDisplay だけでは差し戻せない（#9） | 同上 | 00 の文の直し（§4 P1） |
| 11 | v2.1.280 と Opus 5.5 で検証、翻訳の出力までブロックされる副作用がある（04 Q3） | 正しい | 記事は v2.1.280・Opus 5.5・2026年10月の確認と明記し、注意点に「英語で答えてほしいときも止まる」「判定は文字の比率」「MessageDisplay が途中から動かないように見えた（原因は未確認）」を挙げる | クラスメソッドの記事 | 第三者のプラグインは名前だけ（D13） |
| 12 | 日本語と英語でプロンプトの精度を比べた実測は見つからなかった。「測定はないが、言語より構造が効く」と書く（00 分野15。requirements §10.4 の「データが存在しないもの」にも「日本語と英語の指示の精度比較」） | 一部誤り | 公式の多言語の評価がある。MMLU を専門の翻訳者が14言語に訳した問題で、英語を100%とした日本語の成績は Claude Sonnet 4.5（廃止済み）96.8%、Claude Haiku 4.5 93.5%（extended thinking あり、zero-shot CoT）。ただし旧い世代のモデルの知識問題であり、指示の守り方やエージェントの作業を比べたものではない。「エージェントの作業で日本語と英語の指示を比べたデータはない」は正しい | multilingual-support | 分野15「日本語で指示して大丈夫か」の根拠を差し替える（§4 P3・P4） |
| 13 | 日本語のトークン：英語に対する固定の倍率はなく、言語ごとの換算率は非公表。Opus 4.7 以降の新しいトークナイザーでは同じ文章で約30%多い（04 Q3、SSD Nodes） | 正しい | 公式の用語集は「1トークンが表す文字数はモデルと言語による」「4.7 以降は同じ文章でおよそ30%多い」とし、言語ごとの数値は出していない。Opus 5.5 の移行の手引きは「1〜1.35倍、内容による」とする。正確な数は token counting で数えるよう案内している | platform glossary「Tokens」、Opus 5.5 migration guide | 分野15「日本語はトークンが多めになる」。数値は facts.yml へ |
| 14 | textlint を PostToolUse（`Write\|Edit\|MultiEdit`）の後に走らせ、エラーが残れば exit 2 で差し戻す（04 Q3、Zenn） | 正しい（補足あり） | 記事の内容と一致する（`decision: "block"` と exit 2、`textlint-rule-preset-japanese`・`prh`・`no-mix-dearu-desumasu` など）。ただし現行の公式の文書は MultiEdit を legacy として扱っている。また公式の文書と公式のリポジトリに textlint の例はない（§3.4） | Zenn の記事、permissions、llms-full.txt | 雛形は `Edit\|Write` にし、Bash で書いた場合の抜けを注記（§3.4） |
| 15 | claude.ai は表示の言語として日本語に対応し、表示の言語に関係なく書いた言語で返答する。音声の言語は別の設定（02 §1-16） | 正しい | 2026-10-23 更新の記事も同じ。言語の設定（プロフィールのアイコン → 言語）は画面の表示だけを変え、Claude は使った言語で会話する。音声の言語は 設定 > 機能 > 音声 > 話す言語（ない場合は 設定 > 一般 > 音声 > 言語）。返答の言語を固定する設定は claude.ai にはない（記事に記述がない） | support 10769299（en・ja） | 分野15・分野01（アプリ）。claude.ai では指示で頼むしかない |
| 16 | 個人設定の公式の使い分けは Instructions for Claude／project instructions／skills。personalization の記事に Styles の記載がない（02 §1-3） | 正しい | 2026-10-23 更新の記事でも同じ3つ。Help Center の記事一覧（sitemap、英語367件）に Styles の記事はない。シークレットチャットの記事には「custom styles」への言及が残る。Styles の現行の仕様は確かめられない（R5 の担当） | support 10185728・12260368、sitemap.xml | 分野15「表記ゆれと漢字の開き」で Styles を頼りにしない |
| 17 | personalization の記事は project instructions を有料プラン限定とし、Projects の記事の「Free も5個まで」と食い違う（02 §1-2 注意） | 正しい（食い違いは続いている） | 現行の personalization の記事の中に「Free も最大5個のプロジェクトを作れる」と「project instructions は有料プランのみ」の両方が並ぶ | support 10185728 | facts.yml に「食い違いあり」で置く |
| 18 | 日本語の思考のキーワード（「熟考」など）を判定していたのは逆コンパイルの解析で非公式。今も有効かは未確認（04 Q3） | 一部確かめた | CHANGELOG の 1.0.8（2025-06-02）に「英語以外の言語で thinking を起動できるようにした」とあり、当時は公式の機能だった。いまの扱い（キーワードが効くか）は確かめていない（R2 の範囲：effort と ultrathink） | CHANGELOG 1.0.8 | 古くなった助言の台帳の項目に一次資料を足せる |
| 19 | 日本語の環境に固有のトラブル（Windows・WSL・IME・文字コード）の体系的な資料はない（requirements §10.4、00 分野15「要調査」） | 一部誤り | 体系的な資料はないが、CHANGELOG に個別の修正の記録が多い。例：2.1.296（2026-10-09）から、UTF-8 でないファイル（Shift-JIS・Windows-1252・GBK）を Edit で編集すると非 ASCII の文字が置き換わる不具合を直し、そうした編集を拒むようにした。2.1.299（10-14）から Write も Shift-JIS などを黙って UTF-8 に変えずに拒む。IME の変換窓の位置（2.0.68 ほか）、全角の空白と数字の入力（2.1.21・2.1.31）、Windows の日本語の文字化け（2.1.97・2.1.126）など。Windows の Bash ツールが CP932 の出力を UTF-8 として読む問題は未解決の issue（#96271） | CHANGELOG、#96271 | 分野15「文字コード」「Windows・WSL・IME で困ったら」に版つきで使える |

件数：正しい 13（うち補足・裏付けの追加あり 3）、一部誤り 3、一部確かめられない・一部確かめた 2、確かめられない 1。

---

## 3. 新しく分かったこと

### 3.1 公式の日本語版と主な用語の訳語

**日本語版の有無**

| 公式の資料 | 日本語版 | 分かったこと |
| --- | --- | --- |
| Claude Code の文書（code.claude.com/docs/ja） | ある（228ページ、英語版と同じ） | 索引は `_llms/jp.txt`。変更履歴は英語の GitHub へ転送。調べた29ページの版番号は英語版と同じ。用語集は見出し語を英語のまま残し、本文で説明する。翻訳の方法の注記はない。直訳と見られる箇所がある（英語の「fleet」が「フロート」になっている、など） |
| Claude Platform の文書（platform.claude.com/docs/ja） | ある | 用語集の見出しは日本語（コンテキストウィンドウ、トークン、事前訓練など） |
| ヘルプセンター（support.claude.com/ja） | ある（英語367記事のうち365記事） | サイト名は「Anthropicヘルプセンター」。訳語が Claude Code の文書と違うものがある（プランモード、努力レベル）。チートシートの「筋肉記憶に値する語彙」のような直訳がある |
| claude.ai の画面 | ある（表示の言語に日本語） | 画面の項目名は Help Center の訳から推測できるが、画面そのものは見ていない（§5） |

**主な用語の訳語**

code.claude.com/docs/ja の数は、29ページの本文で数えた回数と割合（コードとリンク先を除く）。

| 英語 | Claude Code の日本語版（本文の多数派と割合） | ヘルプセンターの日本語版 | 教材の表記の案（提案） |
| --- | --- | --- | --- |
| subagent | サブエージェント（94%）。組み込みサブエージェント、カスタムサブエージェント | サブエージェント | サブエージェント |
| hooks | フック（93%）。ページ名は「hooks でアクションを自動化する」など英語も残る。hook event はフックイベント、matcher は英語のまま（マッチャーは少数） | フック | フック（イベント名と matcher は英語のまま） |
| skills | スキル（91%）。bundled skills はバンドルスキル | スキル | スキル |
| plugins | プラグイン（93%）。marketplace はマーケットプレイス | プラグイン | プラグイン |
| permissions | 権限（94%）。permission mode は権限モード、permission prompt は権限プロンプト。allow／ask／deny のルールは許可ルール・確認ルール・拒否ルール（「deny ルール」なども少数） | 権限 | 権限。ルールは「allow ルール」などキーの名前と並べる案と、訳す案がある（決める点） |
| sandbox | サンドボックス（98%） | （記事なし） | サンドボックス |
| auto mode | auto モード（80%）、オートモード（11%、auto-mode-config のページ）、auto mode（9%） | （記事なし） | auto モード |
| plan mode | plan モード（79%）、プランモード（11%）、plan mode（10%） | プランモード | 割れている。どちらかに決めて prh に入れる（決める点） |
| acceptEdits | acceptEdits モード | 編集を受け入れるモード | acceptEdits モード |
| compaction | 圧縮（96%）。コンテキスト圧縮、自動圧縮。「compaction」はほとんど使わない | （チートシートは「圧縮または削除」） | 圧縮（初出に compaction を添える） |
| context window | コンテキストウィンドウ（98%） | コンテキストウィンドウ | コンテキストウィンドウ |
| effort | effort（91%）。effort レベル。努力レベルは少数 | 努力レベル・努力（記事 8664678 の題名と本文） | effort（claude.ai の日本語の画面では「努力」と出る可能性を添える。画面は未確認） |
| output style | 出力スタイル（84%） | （記事なし） | 出力スタイル（初出に output style） |
| memory／auto memory | メモリ（89%）／自動メモリ（93%）。memory のページの題名は「Claude があなたのプロジェクトを記憶する方法」 | メモリ | メモリ・自動メモリ |
| CLAUDE.md | CLAUDE.md（「CLAUDE.md ファイル」とも） | CLAUDE.md | CLAUDE.md |
| agent teams／teammate | エージェントチーム（93%）／チームメイト（90%） | — | 同左 |
| extended thinking | 拡張思考（92%） | 拡張思考 | 拡張思考 |
| prompt caching | プロンプトキャッシング（99%） | — | プロンプトキャッシング |
| managed settings | 管理設定（95%） | — | 管理設定 |
| checkpoint | チェックポイント（96%） | — | チェックポイント |
| worktree | worktree（96%、英語のまま） | — | worktree |
| non-interactive mode | 非対話モード（87%） | — | 非対話モード |
| system prompt／system reminder | システムプロンプト／システムリマインダー | — | 同左 |
| classifier | 分類器（100%） | — | 分類器 |
| frontmatter | フロントマター（87%） | — | フロントマター |
| session／turn／transcript | セッション／ターン／トランスクリプト | セッション | 同左 |
| Instructions for Claude | — | Claudeの指示（設定の項目名は「指示」） | Claude への指示（画面の名前は確認してから） |
| Project instructions | — | プロジェクト指示 | プロジェクトの指示 |
| Organization instructions | — | 組織の指示 | 組織の指示 |
| Projects／Skills／Memory | — | プロジェクト／スキル／メモリ | 同左 |
| Incognito chats | — | シークレットチャット | シークレットチャット |
| Artifacts／Research／Connectors | — | アーティファクト／リサーチ／コネクタ | 同左 |
| Voice mode | — | 音声モード | 音声モード |

まとめると、公式の日本語の表記は、二つの点で教材の基準にそのまま使えない。一つは公式の中で割れていること（plan モードとプランモード、effort と努力レベル）、もう一つはページによって英語とカタカナが混ざることである。それでも本文の多数派ははっきりしているので、教材は多数派に揃え、割れている語だけを教材で決めて prh に入れるのがよい（§4 P11）。

### 3.2 日本語の出力を揃える公式の仕組みと、その効く範囲

**Claude Code**

| 仕組み | 公式の文書に書かれていること | 書かれていないこと |
| --- | --- | --- |
| `language` の設定（v2.1.0 から） | 英語以外で返答させる。値をそのまま「常にその言語で返答する」指示として渡す。値は検証しない。音声入力とセッションの題名の言語にも効く。`/config` でも設定できる | 指示がどこに入るか（システムプロンプトか）。サブエージェント・圧縮の要約・思考の要約・コミットメッセージ・コードのコメントに効くか。system reminder の一覧（agent-sdk/modifying-system-prompts）には載っていない |
| CLAUDE.md | 強制ではなく文脈。厳密に守られる保証はない。システムプロンプトの後のユーザーメッセージ（system reminder）として届く。プロジェクトの根の CLAUDE.md は圧縮の後にディスクから読み直される。fork でないサブエージェントにも届くが、組み込みの Explore と Plan、`omitClaudeMd` のサブエージェントには届かない | 言語の指示の守られやすさが、書く位置や書き方でどう変わるか |
| output style | 指示であり、必ず起きることは保証しない。毎回のリクエストで送られ、圧縮の後も効く。fork を除くサブエージェントには効かない（サブエージェントは自分のシステムプロンプトで動く）。組み込みは Proactive・Concise・Explanatory・Learning。カスタムの style は `keep-coding-instructions: true` でコーディングの指示を残せる。主の会話では system reminder として届く | Concise などの style の指示が英語で入ることが、返答の言語に影響するか（#96326 で利用者が仮説を出し、本人が弱めた） |
| `--append-system-prompt`（`-file`） | 既定のシステムプロンプトに書き足す。公式の例に `--append-system-prompt "Always reply in French"` がある。システムプロンプトは圧縮の後も効く | 設定ファイルのキーとしては書けない（起動のたびのフラグ）。API の文書の「応答言語はシステムプロンプトで指定するのが最も確実」を Claude Code に当てはめてよいかは書かれていない（推論） |
| UserPromptSubmit hook | 標準出力か `additionalContext` を、プロンプトごとに system reminder として足す。バックグラウンドのサブエージェントの報告や予定のタスクでも動く | 注入した言語の指示の効き目（#96326 では、毎ターン注入しても英語になったと報告） |
| Stop hook（SubagentStop も同じ形） | `last_assistant_message` でターンの最後の返事を受け取れる。`decision: "block"` と `reason`（または exit 2 の標準エラー）で終わらせずに続けさせる。続けさせるのは8回まで（`CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` で変える）。`stop_hook_active` で二重の差し戻しを避ける | 言語の判定のしかた（公式の例はない） |
| PreToolUse hook | exit 2 などでツールの呼び出しを止め、理由を Claude に返せる | — |
| PostToolUse hook | exit 2 にすると標準エラーが Claude に届く。`decision: "block"` の `reason` はツールの結果の横に足される。`updatedToolOutput` でツールの出力を差し替えられる（Claude が見るものだけが変わる）。matcher が `Edit\|Write` の PostToolUse は、Bash などでファイルが書き換わったときには動かない（どこから書き換えても拾うなら FileChanged） | 英語のツール出力に注記を足すと言語が保たれるか（推論。試した記録はない） |
| MessageDisplay hook（v2.1.152 から） | 画面に出る返事の文を、表示のときだけ差し替える。止めることも、記録や Claude が見る内容を変えることもできない。`claude -p` ではメッセージごとに1回 | — |
| prompt・agent 型の hook | 別のモデルが判断するので決定的ではない。本当に強制するなら command か http の hook を使う | — |
| サブエージェントの定義・委任の文 | サブエージェントは自分のシステムプロンプトで動く。必ず届けたい規則は委任の文に書き直す | — |
| 設定の層とクラウドのセッション | クラウドのセッションは、ユーザーの `~/.claude/settings.json`・`.claude/settings.local.json`・`~/.claude/CLAUDE.md` を読まない。リポジトリの `.claude/settings.json` は1つのリポジトリのセッションでは読む（プロジェクトのスレッドでは hooks などが効かない）。プラグインはクラウドで読み込まれない。個人の指示は setup script で `~/.claude/CLAUDE.md` を書けば届く（公式の例はコミットメッセージの好み） | — |

効く範囲の要点を三つにまとめる。

1. **強制できるのは「ターンの終わり」と「ツールの前後」だけである。** Stop で最後の返事を、PreToolUse で次のツールの前を止められる。ツールの合間の一言を、画面に出る前に止める仕組みはない（MessageDisplay は表示を変えるだけ）。英語の一言が一度画面に出ることは、公式の仕組みでは防げない
2. **お願いの層は、届く範囲が違う。** `language`・output style・CLAUDE.md はどれも指示である。output style は fork でないサブエージェントに届かず、CLAUDE.md は Explore と Plan に届かず、`language` は届くかどうかが書かれていない
3. **面によって届く設定が違う。** ユーザーの設定・CLAUDE.md・hooks・プラグインはクラウドのセッションに届かない。日本語の指示を確実に届けるには、リポジトリの CLAUDE.md と `.claude/settings.json` に入れるが、そうするとチーム全員に効く（#5）

**claude.ai**

| 仕組み | 公式に書かれていること | 書かれていないこと |
| --- | --- | --- |
| 表示の言語 | プロフィールのアイコン → 言語。画面の表示だけが変わる。Claude は使った言語で会話する。Web と Desktop の記述 | 返答の言語を固定する設定。モバイルの表示の言語の変え方 |
| 音声の言語 | 表示の言語とは別。設定 > 機能 > 音声 > 話す言語 | — |
| Claude への指示（Instructions for Claude） | アカウント全体の指示で、すべての会話に適用される。「一般的なコミュニケーションの指示」を書く例がある | 言語の指示の守られやすさ |
| プロジェクトの指示 | そのプロジェクトの中のチャットにだけ適用される。プランの条件は記事の中で食い違う（#17） | — |
| 組織の指示（Team・Enterprise） | オーナーが組織の全会話に効く指示を書く（3,000字まで、反映に最大1時間）。個人の指示と矛盾すれば組織の指示を優先する。公式の例に「Always respond in formal English」がある。優先はプロンプトの層の指示に頼るので、まれに挙動が変わる、と明記 | Claude Code にも効くか（「Claude の製品全体」とだけある） |
| スキル | 返答の口調や形式、自分の文章に基づく書き方を加える。個人設定の記事は、形式や届け方を変えたいときはスキルを使うとする | — |
| Styles | 現行の記事がない（#16） | 現行の仕様（R5） |
| メモリ | 02 §1-4（記事 11817273、2026-10-29 確認）によれば、コミュニケーションの好みなどを保存できる。今回は読み直していない | 言語の好みを保存したときの効き目 |

claude.ai には、hooks や検査のような、返答の言語や文体を機械的に確かめる仕組みの記述がない。公式の手段はどれも指示である。

**API（参考）**

Platform の多言語の文書は、Claude は会話から返答の言語を推測するが、本番では明示すべきで、最も確実な場所はシステムプロンプトだとする。入力と出力の言語を明示すると確実さが上がる、とも書く。英語に戻る現象そのものには触れていない。Opus 5.5 の頼み方の手引き・移行の手引き・新機能のページにも、言語の注意はない。

### 3.3 英語への回帰の一次の記録

**公式の文書**

- 英語に戻る現象そのものを書いた公式の文書は見つからなかった（code.claude.com の全文、Platform の多言語・Opus 5.5 の各ページ、Help Center）
- 関係する公式の記述は、上の表の「指示であって保証しない」（CLAUDE.md・output style・組織の指示）と、「例外を許さないものは hook にする」（Best practices）である
- CHANGELOG には、Claude Code の機能が `language` を無視して英語で書いた不具合を直した記録や、`language` に従うように改めた記録がある：セッションの題名（2.1.16、2.1.121、2.1.176）、`/settings` の言語の変更が Esc で戻る（2.1.136）、`language` を設定すると返答からアクセント記号などが落ちる（2.1.108）、You should know が `language` に関係なく英語でメモを書く（2.1.290、2026-10-05）。モデルの返事が英語に流れることを直した記録は、2.1.317 までにない

**GitHub の issue（anthropics/claude-code）**

見つけた件数は、返事（最後のまとめ・途中の一言）が英語に戻る・流れるもの29件（うち日本語10件）。このほかに、セッションの題名・コンパニオン・思考の要約などの機能が `language` を無視して英語で出す報告が十数件ある（数えていない）。検索は英語の語に頼ったので全数ではない。

Opus 5.5 の公開（2026-09-22）より前（13件）

| # | 起票 | 版 | モデル | 言語 | 面 | 状態 | 内容 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7970 | 2025-09-21 | 1.0.117 | 不明 | ロシア語 | CLI（macOS） | 閉 | 会話の圧縮の後に英語へ |
| 10432 | 2025-10-27 | 2.0.27 | 不明 | ロシア語 | CLI（macOS） | 閉（重複） | 圧縮の後、規則にあるのに英語へ |
| 11245 | 2025-11-08 | 2.0.28 | 不明 | 不明 | CLI（Windows） | 閉（重複） | 自動圧縮の後に英語へ |
| 11567 | 2025-11-13 | 2.0.37 | Sonnet（既定） | 不明 | VS Code（Windows） | 閉 | 圧縮の後に英語へ |
| 13524 | 2025-12-10 | 2.0.61 | 不明 | スペイン語 | — | 閉（重複） | 自動圧縮の後に英語へ |
| 21871 | 2026-01-30 | 不明 | 不明 | スペイン語 | Windows | 閉（重複） | スペイン語で話しても英語で返す |
| 25677 | 2026-02-14 | 2.1.38 | 不明 | 韓国語 | CLI（macOS） | 閉（重複） | 圧縮の後に英語へ |
| 26280 | 2026-02-17 | 2.1.44 | Opus 4.6 | 日本語 | CLI（macOS） | 閉 | `language` と CLAUDE.md を無視して英語 |
| 32107 | 2026-03-08 | 2.1.71（退行） | 不明 | 不明 | Windows | 閉 | plan モードの「文脈を消して自動承認」の後の実行中だけ英語 |
| 32181 | 2026-03-08 | 2.1.71 | Opus 4.6 | 日本語 | — | 閉 | コードの多い作業で徐々に英語へ |
| 59299 | 2026-05-15 | 2.1.141 | 不明 | スペイン語 | macOS | 閉 | 圧縮の後に英語へ |
| 78996 | 2026-07-19 | 2.1.215 | Opus 4.7・4.8・Sonnet 5 | 韓国語 | VS Code（Windows） | 閉 | 長いセッションで崩れる、または英語へ |
| 80850 | 2026-07-24 | 2.1.211 | Opus 4.8 | 日本語 | Desktop（Windows） | 閉 | ツール呼び出しの境目で英語が混ざる |

Opus 5.5 の公開の後（16件）

| # | 起票 | 版 | モデル | 言語 | 面 | 状態 | 内容 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 96326 | 2026-09-23 | コメントで 2.1.280〜2.1.309 | Opus 5.5 | 日本語（コメントで7言語） | CLI（Linux）ほか | 開（コメント18） | 英語のツール出力・サブエージェントの報告・コードレビューの出力を読んだ後に英語。訂正が続かない |
| 96601 | 2026-09-24 | 2.1.278 → 2.1.280・281 | Opus 5 → 5.5 | 繁体字中国語 | macOS | 開 | output style の言語の規則がツールの連続の後に破られる。0.4% → 4.2% |
| 98633 | 2026-10-01 | 2.1.282 | Opus 5.5 | 日本語 | VS Code（Windows） | 開 | CLAUDE.md・メモリ・会話での指示があっても英語 |
| 98848 | 2026-10-02 | 2.1.287 | 不明 | スペイン語 | macOS | 開 | 何度頼んでも英語 |
| 99494 | 2026-10-04 | 2.1.289 | 不明 | 韓国語 | macOS | 開 | 設定してあるのに英語に戻る |
| 99603 | 2026-10-05 | 不明 | Opus 5.5・Sonnet 5.5 | ドイツ語 | Desktop（Windows） | 開（#96326 の重複とされた） | 一度英語になると戻らない |
| 99641 | 2026-10-05 | 不明 | Opus 5.5 ほか | 日本語 | Desktop（Windows） | 開 | 表示が思考の言い換えに置き換わる問題も含む |
| 99704 | 2026-10-05 | 2.1.283・2.1.289 | Opus 5 → 5.5 | 韓国語 | macOS | 開 | 同じ CLI で Opus 5 は 0%、Opus 5.5 は 33% |
| 99800 | 2026-10-05 | 不明 | Opus 5.5 | 日本語 | Desktop（Windows） | 閉（完了、10-18。直した記録は示されていない） | 途中の一言が英語。コメントで「圧縮の要約が英語で書かれる」 |
| 101940 | 2026-10-14 | 不明 | Opus 5.5 | 日本語 | Desktop（Windows） | 開 | PreToolUse と Stop の hook でも止まりきらない。画面の読み上げの利用者に影響 |
| 103672 | 2026-10-20 | 2.1.304 | Opus 5.5 | 日本語 | macOS | 開 | skill の作業中の途中の報告が英語 |
| 104035 | 2026-10-21 | 2.1.306 | Opus 5.5 | 韓国語 | CLI（macOS） | 開 | CLAUDE.md・メモリ・訂正があっても英語 |
| 104137 | 2026-10-21 | 2.1.306 | Opus 5.5 | スペイン語 | VS Code（Windows） | 開 | ツールの合間の一言が、1セッションに十数回英語 |
| 105644 | 2026-10-28 | 2.1.312 | 不明 | 日本語 | macOS | 開 | 日本語の設定なのに途中から英語 |
| 106893 | 2026-11-03 | 不明 | Opus 5.5 | ヘブライ語 | Desktop（Windows） | 開 | 途中の一言と思考の要約が英語 |
| 106911 | 2026-11-03 | 2.1.317 | 不明 | ドイツ語 | macOS | 開（regression の印） | 英語のツール出力の後に英語へ |

閉じた状態の読み方：GitHub のこのリポジトリでは、反応の少ない issue を一定の期間で自動で閉じる（#87647 は「has repro の印のある6千件以上が2026年3月から自動で閉じられた」と報告している）。上の「閉」の多くは自動の close や重複の判定で、直ったことを意味しない。読んだスレッドに Anthropic の担当者の返答はなかった（読んだ43件の issue のコメント156件は、ボットを含めてすべて authorAssociation が NONE）。

**利用者が数えた割合（自己申告。方法は人ごとに違う）**

- Opus 5.5 で英語になった割合は、言語の規則があるときの集計で、テキストのまとまりが約4〜38%、ターンの最後の返事が約1.5〜32%と幅が広い（31件中14件＝45%という小さな集計もある）。同じ人の Opus 5 は0〜4%程度（#96326 のヘブライ語・韓国語・繁体字中国語、#96601 のイタリア語・繁体字中国語、#99704 の韓国語）
- 起きやすい場所：ツールの結果の直後の一言（繁体字中国語の集計で約27%、利用者のメッセージの直後は約5%。韓国語の集計で13.1%と5.6%）。ツールの呼び出しが多いターンほど多い。英語の skill を読み込んだ後に多い
- 文脈の長さや圧縮との関係は、集計した2人とも見つけていない。ただし #99800 のコメントは、20回圧縮したセッションの要約がすべて英語だったと報告している
- CLI の版（2.1.281）で悪化したという集計が2人、モデルについて回るという集計が別の1人。どちらとも決められない

**報告された対策の効き目（自己申告）**

- 毎ターン UserPromptSubmit で規則を注入しても止まらなかった（#96326、1人）
- Stop hook で最後の返事を判定し、英語なら書き直させた実運用で、差し戻した44回すべてで次の返事が目的の言語になった（ペルシア語、#96326、1人）。過去の記録に当てはめた再生実験も1件ある。ただしツールの合間の一言には届かず、英語の下書きは画面に出る
- PreToolUse と Stop の hook を入れても、注意の直後の一言がまた英語になることがあった（#101940、日本語）
- Concise から Default に戻すと減った、という観察は、同じ人が後で「確実な対策ではない」と弱めた（#96326）

**日本語圏の記録**

調査資料が引くのはクラスメソッドの記事（2026-10-20）1件である。ほかに note の個人の記事（2026-09-29）があるが、中身は #96326 と #96601 のまとめで、独立の観察ではない。日本語の一次の記録としては、GitHub の日本語の利用者の issue（上の10件）と、#96326 のコメントの日本語の利用者2人の集計（2.1.280 で0〜7%と4%、2.1.281 で45%と11%）がある。

**根拠の強さ（requirements §6.2 の基準）**

| 主張 | 強さ | 理由 |
| --- | --- | --- |
| Claude Code で、日本語などで頼んでも返事が英語に戻ることがある | 中 | 独立した利用者の報告が多く、言語も多い。公式の認知と統制された測定はない |
| Opus 5.5 で増えた（Opus 5 などより多い） | 中 | 複数の利用者が自分の記録を数えて一致。ただしモデルの切り替えと CLI の更新が同じ日に重なった例があり、条件はそろっていない |
| 英語のツール出力・サブエージェントの報告・英語の skill の後、とくにツールの合間の短い一言で起きやすい | 中 | 複数の集計とクラスメソッドの観察が一致 |
| CLI 2.1.281 で悪化した | 弱 | 2人の小さな集計。反対の観察もある |
| Concise の英語の注意書きが引き金になる | 弱 | 1人の仮説で、本人が弱めた |
| 圧縮の後に英語に戻る | 弱 | 2025-09〜2026-05 の旧い版の報告が中心で、重複として自動で閉じられたものが多い。現行の版の報告は1件（圧縮の要約が英語） |
| CLAUDE.md・メモリ・毎ターンの注入では止まらない | 中 | 複数の報告。公式も CLAUDE.md は強制ではないとする（その部分は強） |
| Stop hook で最後の返事を確かめて書き直させると減る | 弱 | 1件の実運用、1件の再生実験、クラスメソッドの動作確認。止まりきらないという報告（#101940）もある |
| ツールの合間の一言は Stop では拾えず、画面に出る前には止められない | 強 | 公式の仕様（Stop は最後の返事だけ、MessageDisplay は表示だけ） |
| 日本語の成績は英語より少し低い（旧い世代の知識問題で英語比 93.5〜96.8%） | 強（ただし類推） | 公式の評価。現行のモデルとエージェントの作業に当てはめるのは類推 |

### 3.4 文体・表記を仕組みで揃える方法：公式の例と記述の所在

- **textlint・Vale・markdownlint の公式の例はない。** code.claude.com の全文（llms-full.txt）を検索しても出てこない。anthropics/claude-code の `examples/hooks` は `bash_command_validator_example.py` だけで、公式のプラグインの一覧（claude-plugins-official）にも言語や文章の検査のものはない（出力スタイルの `explanatory-output-style`・`learning-output-style` や、hook を作る `hookify` はある）
- **形が同じ公式の例はある。**
  - hooks の入門「編集後にコードを自動フォーマットする」：PostToolUse・matcher `Edit|Write`・Prettier（https://code.claude.com/docs/en/hooks-guide ）
  - Best practices「Enforce steps with hooks」の整形の例と、型検査を Stop hook で強制する例（exit 2 で、標準エラーが Claude に返る）（https://code.claude.com/docs/en/best-practices ）
  - hooks の仕様「PostToolUse から Claude に警告を返すには exit 2 にする」、`decision: "block"` の `reason`（https://code.claude.com/docs/en/hooks ）
  - 文体の手引きは、参照用の skill として置く例が公式の文書にある（features-overview・skills の「API の style guide」）
- **雛形を作るときに、公式の文書から言えること**
  - matcher は `Edit|Write` にする（MultiEdit は legacy）
  - Bash のヒアドキュメントなどで書いたファイルには、PostToolUse（`Edit|Write`）は動かない。どこから書き換えても拾うなら FileChanged を使う
  - 決定的に強制するなら command か http の hook にし、hook が落ちたときも止めるなら `onFailure: "block"` を付ける。prompt・agent 型の hook は別のモデルの判断なので強制にならない
  - 強制する規則は少なく保つ（Best practices。decisions.md 2026-11-03「hooks と permissions」の注意と同じ方向）
  - クラウドのセッションでは、ユーザーの設定の hooks とプラグインは効かない。リポジトリの `.claude/settings.json` に入れたものは、1つのリポジトリのセッションで効く

### 3.5 そのほか

- Opus 5.5 の公開日は 2026-09-22、Sonnet 5.5 は 09-28（Help Center のリリースノート）
- Claude Code の `language` は、2025-06-02 の 1.0.8 で「英語以外の言語で thinking を起動」、2026-01-07 の 2.1.0 で設定のキーとして追加、と CHANGELOG でたどれる
- MessageDisplay は 2.1.152（2026-05-27）、Stop hook の8回の上限は 2.1.143（2026-05-15）に入った（CHANGELOG）

---

## 4. 提案

メインがまとめて反映する前提の案である。

**調査資料への直し**

- P1（00 分野15 の冒頭の段落）：「そこで UserPromptSubmit・Stop・MessageDisplay の hook で日本語を強制する解決策を作った」を、「そこで UserPromptSubmit・Stop・MessageDisplay・PreToolUse の hook で日本語を保つ仕組みを作った（MessageDisplay は表示を変えるだけで止められないため、次のツールの呼び出しを PreToolUse で止めて言い直させる）。同じ症状は GitHub の anthropics/claude-code に、Opus 5.5 の公開（2026-09-22）の後だけで少なくとも16件ある（うち12件は Opus 5.5 と明記。#96326 など。27-japanese.md §3.3）」に直す
- P2（00 分野15 と 04 Q3 の `language` の記述）：「言語設定の `language` は、コメントやコミットメッセージには効かない」を、「`language` がコメントやコミットメッセージに効くかは、公式の文書に書かれていない（Issoh の記事は 2026-11-03 に取得できず未確認）」に直す
- P3（00 分野15 の「日本語と英語でプロンプトの精度を比べた実測記事は見つからなかった。そのため…」）：次の文を足す。「公式の多言語の評価はある。人が訳した MMLU で、英語を100%とした日本語の成績は Sonnet 4.5 で96.8%、Haiku 4.5 で93.5%（extended thinking あり）。旧い世代の知識問題で、指示の守り方やエージェントの作業の比較ではない」
- P4（requirements §10.4「データが存在しないもの」）：「日本語と英語の指示の精度比較」を、「エージェントの作業での日本語と英語の指示の精度比較（公式の多言語の評価は、旧い世代のモデルの知識問題だけ）」に直す
- P5（requirements §10.4 の4つ目）：「日本語環境に固有のトラブル（Windows・WSL・IME・文字コード）の体系的な資料」に、「（CHANGELOG に個別の修正の記録はある。例：2.1.296・2.1.299 から Shift-JIS などの UTF-8 でないファイルの編集を拒む）」を足す
- P6（04 Q3「Opus 5.5 は英語の返答に戻りやすい」）：出典に GitHub の #96326・#99704・#96601 を足し、「1社の観察だけでなく、多数の利用者の報告がある（根拠の強さ：中。自己申告の集計で、公式の認知はない。2026-11-03 確認）」と注記する
- P7（04 F と Q3 の textlint）：「MultiEdit は現行の文書では legacy。雛形の matcher は `Edit|Write`。Bash で書いたファイルには動かないので、必要なら FileChanged」と注記する
- P8（02 §1-2 の「注意」）：「食い違いは、現行の personalization の記事（2026-10-23 更新）の中で両方が並ぶ形で続いている」と足す
- P9（02 §1-3 の Styles）：「personalization の記事（2026-10-23 更新）にも Styles はなく、Help Center の記事一覧に Styles の記事がない（2026-11-03）。シークレットチャットの記事に custom styles の言及が残る」と足す（R5 の結果と合わせる）
- P10（00 分野15 の表）：「日本語で返し続けさせる」の要点に「効く範囲（サブエージェント・圧縮・クラウドのセッション）と、ツールの合間の一言は止められないこと」を足す。「日本語で指示して大丈夫か」の根拠を「日」から「公D・日」にする

**decisions.md への提案（メインか作者が決める点）**

- P11 用語の表記の方針。案は三つ。(a) code.claude.com/docs/ja の本文の多数派に揃える、(b) 機能の名前はすべて英語のまま、(c) ページごとに選ぶ。推奨は (a) である。読者が公式の日本語版と行き来しやすく、prh で検査しやすい。公式の中で割れている語（plan モード／プランモード、effort／努力レベル、allow ルール／許可ルール）だけ教材で決め、もう一方を prh で指摘する。初出には英語を添える（例：圧縮（compaction））
- P12 英語への回帰の検証ノート（decisions.md の「大事な論点の数件だけ回数の上限を決めて繰り返し、傾向として書く」）の測り方の案。(1) 数える単位を「ツールの合間の一言」と「ターンの最後の返事」に分ける、(2) コードの塊・インラインコード・URL・パスを除き、30字以上のまとまりだけを数え、かなと漢字の割合で判定する（GitHub の集計と比べられる形）、(3) 英語のツール出力を読む作業（英語のログを読ませる）と読まない作業を同じ回数ずつ、(4) 条件は `language` だけ、CLAUDE.md だけ、両方＋Stop hook、の三つ、(5) モデルと版と日付を記録する。回数の上限はメインが決める
- P13 分野15 と症状辞典「英語で返ってくる」の書き方。診断の確認欄を、安く確かめられる順に並べる案：`language` を設定したか（どの層か）→ リポジトリの設定に別の値がないか → output style → モデル（Opus 5.5 か）→ 英語のツール出力・サブエージェントの直後か → クラウドのセッションか → Stop hook を足す。根拠の強さは §3.3 の表のとおりに付ける
- P14 facts.yml に置く値の候補：`language` の追加（2.1.0、2026-01-07）、MessageDisplay（2.1.152）、Stop の上限8回（2.1.143、環境変数）、Opus 5.5 の公開（2026-09-22）、多言語の評価の値（Sonnet 4.5・Haiku 4.5）、トークナイザーの倍率（約30%、1〜1.35倍）、組織の指示の上限（3,000字・最大1時間）、Shift-JIS などの編集を拒む版（2.1.296・2.1.299）

---

## 5. 確かめていないこと

- claude.ai の日本語の画面（「努力」「指示」などの項目名）は見ていない。Help Center の訳から推測しただけである。作者にまとめて頼む候補にする（decisions.md「作者が試せる面」）
- `language` の指示がどこに入るか、サブエージェント・圧縮の要約・思考の要約・コミットメッセージに効くかは、公式の文書に書かれていない。動かして確かめることはしていない（brief §4）。#96326 には「サブエージェントと fork は英語に流れなかった」という利用者の観察が1件あるだけである
- Styles の現行の仕様（R5 の担当）。モバイルのアプリの表示の言語の変え方
- Issoh の記事（HTTP 403）。GiftX・SSD Nodes・入江・仁頼など、04 が引くほかの日本語の記事は開いていない
- GitHub の検索は英語の語に頼った。日本語の語での検索は0件で、日本語だけで書かれた issue を取りこぼしている可能性がある。件数は「見つけた数」であり全数ではない。利用者の集計の方法は確かめていない
- claude.ai のチャット（Claude Code でない面）でも Opus 5.5 で英語に戻るかは、公開の報告の場所がなく、調べていない
- 日本語の思考のキーワードが今も効くか（R2 の範囲）
- 公式の日本語訳が機械翻訳か人の翻訳か（注記がない）。29ページより外のページの表記の割合
- 組織の指示が Claude Code に効くか（記事は「Claude の製品全体」とだけ書く）

---

## 6. 使った量の目安

- 道具の呼び出し：約90回（Bash が大半、Read・Write・ToolSearch が数回）
- Web の取得：`curl` で約105回（code.claude.com 約70：日本語版と英語版の29ページずつ、索引、全文、転送の確認など。support.claude.com 18。platform.claude.com 10。第三者の記事3。check_noai の取得 8 URL）
- GitHub：`gh search issues` 17回、`gh issue view` 43回、`gh api` 7回
- Web 検索：1回
- かかった時間：約1時間半
