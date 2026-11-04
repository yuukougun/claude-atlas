# 工程6b 担当 D1 の報告：features（Claude Code の機能）

- 版：2026-11-04。指示は [brief-data.md](brief-data.md)（D1 の行）と [brief-build.md](brief-build.md) §1〜§3・§5
- 下書き：[data/D1.yml](data/D1.yml)（最上位のキーは `features`・`domains`・`sources`）

## 1. 作ったファイルと中身の要約

| ファイル | 中身 |
| --- | --- |
| `planning/batches/step6/data/D1.yml` | features 65件（features.yaml の5つの群：文脈と指示 14・縛り 7・操作 23・任せ方 18・面 3。並びも features.yaml と同じ）、domains 5件、sources 70件 |
| `planning/batches/step6/data-D1.md` | この報告 |

- 65件すべて `status: 確認済み`（未確認 0件）。確かめられなかった属性は値を入れず、項目の note に理由を書いた（§5）
- 属性の入り方：surfaces 65件、maturity 65件（GA 59・research preview 3・experimental 2・beta 1）、enforcement 13件（鍵 7・お願い 6）、load_timing 12件・context_cost 14件、survives_compaction 9件（すべて true）、since 35件、match_terms 65件、volatility 59件（中）
- 主のページ（page）は65件すべて目次にあるページ。52件が型 feature、13件がほかの型（§3.3）
- sources は Claude Code の文書（英語 60・日本語 1）、GitHub の CHANGELOG と文書の変更履歴のページ（各1）、Claude Platform の文書 4、Help Center 3。id は内容から作った（頭に担当の記号を付けない）。URL はどれも転送のない最終の URL（curl -L で確かめた）

## 2. 確かめたこと

- **一次資料**：code.claude.com/docs/en の96ページ（`llms.txt` の索引から本文の markdown を取得。版ごとの日付のある変更履歴のページを含む）、同じパスの日本語版58ページ、GitHub の CHANGELOG.md（2.1.318 まで、436版）、Claude Platform の文書4ページ、Help Center 3記事を、2026-11-04 に読んだ。調査資料は、題名の表記を確かめるのに research/27 §3.1 の表を見たほかは使わず、値はすべてこれらから入れた
- **AI の利用の指定**：`uv run python tools/check_noai.py`（`--robots` つき）で、code.claude.com（英語版・日本語版）・github.com・raw.githubusercontent.com・platform.claude.com・support.claude.com を確かめ、どれも noai・noimageai の指定なし。github.com の robots.txt は AI 向けのクローラに一部のパスを禁じる（指定の確認として note に書いた）。claude.com も確かめた（指定なし）が、資料に使わなかったので domains に入れていない
- **schema**：scratchpad のスクリプト（`/tmp/claude-1000/-home-yuuki-projects-kyopro2-claude-atlas/2ee2ba0e-8978-48f8-837d-c53e59939dbb/scratchpad/d1-features/scripts/validate.py`。`uv run python` で動かす）で、下書きを `features` と `domains`・`sources` に分け、`schema/facts.schema.json`・`schema/sources.schema.json` に当てた。道具の検査器（`tools/lib/schema.py`。日付を文字列のまま読む `lib/yamlio`）と jsonschema 4.26（Draft7Validator と FormatChecker。date・partial-date・regex）の両方で誤り0件
- **参照**：features の id が features.yaml の受け持ちの65件と同じ並びで重なりがない、features の sources がすべて sources にある、sources の id と URL に重なりがない、sources の URL のドメインがすべて domains にある、page がすべて目次のページ、を確かめた。どの機能も指さない出典は0件
- **終わりの条件（この担当の分）**：第一波（`check_catalog.py` の数え方の136ページ）が tracks で指す id のうち D1 の受け持ちは42件で、すべて下書きにある。features の各項目に主のページがある
- **語彙**：load_timing と context_cost の値が、§3.1 の語彙の外にないことを確かめた（7種と7種をすべて使った）

## 3. 決めたこと

### 3.1 読み込みの時期とコンテキストのコストの語彙（メインが site.yml に足す）

公式の Extend Claude Code の「Context cost by feature」の表（日本語版の題は「Claude Code を拡張する」の「機能別のコンテキストコスト」。列は When it loads／ロード時期・What loads／ロード内容・Context cost／コンテキストコスト）の行の値を、教材の書き方（和語・だ・である）に直して語彙にした。表にない機能（rules・自動メモリ・プラグイン・ステータスライン・/btw）は、その機能のページの記述から当てはめ、足りない値だけを足した。

```yaml
load_timings: [セッション開始, セッション開始と切り替えたとき, セッション開始か、一致するファイルを扱うとき,
               セッション開始と使うとき, 編集の後と調べるとき, 起動したとき, イベントが起きたとき]   # 読み込みの時期
context_costs: [常駐, 常駐か、一致するファイルのときだけ, 使うまで小さい, 小さい, 分離,
                ゼロ（出力を返さない限り）, ゼロ]                                                 # コンテキストのコスト
```

| 語彙 | 公式の表記（英語／日本語版） | 当てた機能 |
| --- | --- | --- |
| セッション開始 | Session start／セッション開始 | CLAUDE.md・MCP・自動メモリ（自動メモリは memory のページの「Every session」） |
| セッション開始と切り替えたとき | Session start, and again when you switch styles／セッション開始、およびスタイルを切り替えるときに再度 | 出力スタイル |
| セッション開始か、一致するファイルを扱うとき | 表にない。比較のタブの「Every session, or when matching files are opened」／「すべてのセッション、または一致するファイルが開かれたとき」 | rules |
| セッション開始と使うとき | Session start + when used／セッション開始 + 使用時 | スキル・プラグイン（プラグインは Measure plugin cost の記述） |
| 編集の後と調べるとき | After file edits and on demand／ファイル編集後およびオンデマンド | code intelligence |
| 起動したとき | When spawned／スポーン時 | サブエージェント・エージェントチーム・dynamic workflows |
| イベントが起きたとき | On trigger／トリガー時 | フック |
| 常駐 | Every request／すべてのリクエスト（requirements §5 の例「常駐」） | CLAUDE.md・出力スタイル・自動メモリ |
| 常駐か、一致するファイルのときだけ | 表にない。memory のページ（paths のない rules は CLAUDE.md と同じ、paths のある rules は一致するファイルを扱うときだけ） | rules |
| 使うまで小さい | Low (descriptions every request)・Low until a tool is used／低い（毎リクエスト説明）・低い（ツール使用まで） | スキル・MCP・プラグイン |
| 小さい | Low; reduces file reads elsewhere／低い。ファイル読み取りを削減 | code intelligence |
| 分離 | Isolated from main session／メインセッションから分離 | サブエージェント・エージェントチーム・dynamic workflows |
| ゼロ（出力を返さない限り） | Zero, unless hook returns additional context／ゼロ（フックが追加コンテキストを返さない限り） | フック |
| ゼロ | 表にない。statusline のページ「does not consume API tokens」、/btw の「without adding to the conversation history」 | ステータスライン・/btw |

- 値は一つの機能に一つ。条件で変わる機能（rules）は、公式の比較のタブに合わせて「か」でつないだ値にした
- 文脈に入らない機能（権限・サンドボックス・設定・コマンドの多く）には書かない（当てはまらない。省いた属性は比較の表で空になる）。ステータスラインと /btw は、文脈に入らないこと自体が読者に要る情報なので context_cost だけを書いた
- メインが site.yml に足すときは、この順で足すと道具の並び（比較の表の列の値の順）になる

### 3.2 属性の決め方

| 属性 | 決め方 |
| --- | --- |
| maturity | 公式の文書が research preview・beta（public beta を含む）・experimental と書くものだけをそれにし、書いていないものを GA にした（公式は GA と明記しないため）。面やモデルで違うものは、Claude Code の文書の表記を値にし、違いを note に書いた（advisor：Claude Code は experimental・API は beta、fast mode：Opus 5.5 は提供済み・Opus 5 と 4.8 は research preview、IDE の拡張：JetBrains のプラグインに [Beta]） |
| enforcement | 公式が「指示で、強制しない」と書くもの（CLAUDE.md・rules・自動メモリ・スキル・出力スタイル・language の設定）をお願い、Claude Code・OS・決定論のコードが止めるもの（フック・権限・権限モード・plan mode・サンドボックス・管理設定・mods）を鍵にした。別のモデルが判断するもの（auto モードの分類器・/goal の判定・prompt と agent の型のフック）は鍵に数えない（目次の enforce.yaml の request-lock-table の notes と同じ立場）。指示と制限が混ざる機能（サブエージェント）と、規則の手段でない機能には書かない |
| survives_compaction | 公式の Explore the context window の「What survives compaction」の表にある機能だけ true を入れた（CLAUDE.md・rules・自動メモリ・スキル・出力スタイル・plan mode）。フック・権限・サンドボックスは、公式が「会話の外で動く／モデルではなく Claude Code が強制する」と書くことと、会話で言った境界は圧縮で消えうるので deny ルールを足すよう公式が勧めることから true にした（根拠は note）。表に行のない MCP・サブエージェントなどは書かない（null にすると「未確認」と出るため、当てはまるか分からないものは省いた） |
| surfaces | Claude Code の機能は claude-code。同じ名前と仕組みがほかの面にもあり、その面に別の項目がないものだけ面を足した（context-window・effort は app と api、fast mode・advisor は api、Claude in Chrome は app）。アプリの projects・コネクタ・API の compaction など別の id があるものは足さない |
| since | CHANGELOG の追加の行（「Added」「Released」「Introducing」など）がある版だけを入れ、date は文書の変更履歴のページの日付にした。0.2.x の版はどれも同じ日付（2025-04-02）なので date を書かず note にした（compaction・ultrathink）。改名で入った版（/code-review）と、面で版が違うもの（セッションの間のメッセージ）は note を添えた。追加の行が見つからない・CHANGELOG の最初より古いものは書かない（30件。§5） |
| match_terms | 公式の英語の名前・コマンド・フラグ・設定のキー・環境変数・フックのイベント・beta のヘッダーの名前。改名の前の名前（routines・/simplify・/ultrareview）も入れた（古い名前で書かれた変更の行を拾うため） |
| volatility | GA の機能を中（requirements §6.1 の「機能の使い方」の層）、research preview・beta・experimental と、モデルによって research preview が残る fast mode は省いた（既定の高） |
| title | features.yaml の仮の題名のまま。plan-mode だけ、工程5の決定（表記の割れる3語は英語のまま）に合わせて「plan mode」にした（features.yaml は「plan モード」） |

### 3.3 主のページ（page）

- 目次で機能を tracks に持つページのうち、その機能そのものを扱う型 feature のページを選んだ。複数あるときは、機能の全体を扱うページ（多くは第一波・必須）を選び、局面だけを扱うページ（長さ・読み込み順・止め方・通知など）を外した。例：claude-md は what-to-put-in-claude-md（claude-md-length・claude-md-loading-order・init-and-first-claude-md・agents-md は局面）、hooks は hooks-basics（DR-15 の例の completion-notifications ではない）、auto-mode は what-auto-mode-stops、managed-settings は managed-settings-enforcement、interactive-mode は input-symbols（この機能だけを tracks に持ち第一波。キーボードショートカットは must-know-operations）、scheduled-tasks は cloud-schedules（/loop は loop の主）
- 型 feature でないページを主にした13件と理由：

| 機能 | 主のページ（型） | 理由 |
| --- | --- | --- |
| plugin-eval | measure-changes（recipe） | tracks に持つ唯一のページ |
| clear | when-to-start-fresh（concept） | feature の型のページがない。別名「/clear のタイミング」を持つ |
| context-window | attention-budget（concept） | 別名 context window を持ち、用語そのものを説明する（inspect-context は /context の見方） |
| model-selection | choosing-a-model（concept） | feature の型のページがない。別名「モデル選択」を持つ |
| ask-user-question | let-claude-ask（concept） | 唯一のページで、別名 AskUserQuestion を持つ |
| voice-dictation | images-and-voice（concept） | 唯一のページで、別名 /voice を持つ |
| language-setting | keep-replies-in-japanese（recipe） | 別名「language 設定」と節「言語の設定」を持つ |
| code-review | independent-review（concept） | 別名 /code-review を持つ |
| security-review | independent-review（concept） | 唯一のページで、別名 /security-review と節「セキュリティのレビューを頼む」を持つ |
| code-projects | choosing-parallel-modes（comparison） | tracks に持つ唯一のページ |
| auto-continue | how-usage-limits-work（concept） | 第一波・必須で、節「上限に当たったとき」を持つ（when-ai-is-unavailable も tracks に持つ） |
| desktop-code | claude-code-surfaces（comparison） | 別名「Desktop の Code タブ」を持つ（where-it-runs は実行場所の概念） |
| monitor-tool | progress-logs-for-long-jobs（recipe） | どのページも tracks に持たない。材料に「Monitor の道具」を挙げる唯一のページ（§4 の2） |

## 4. 提案

1. **site.yml**：§3.1 の `load_timings` と `context_costs` を足し、`make_schema.py` で schema を作り直す（いまは空でない文字列かだけを見ている）
2. **目次・front matter**：monitor-tool を `progress-logs-for-long-jobs`（delegate）の tracks に足す（別名に Monitor を足すかは目次の判断）。足さないなら、主のページを別に決める
3. **圧縮で残るかの値**：CLAUDE.md（入れ子の CLAUDE.md）と rules（paths のある rules）は「要約に消え、必要なときに読み直す」部分があり、true／false では言い切れない。いまは true にして note に条件を書いたが、バッジは note を出さないので、主のページの path-scoped-rules のバッジが「残る」になる。keys.yml の survives_compaction に三つ目の値（例：「必要なときに読み直す」）を足すか、作る層が note を添えて出すかを決めてほしい
4. **用語集・prh（題名の表記）**：公式の日本語版の本文（取得した58ページ。コードとリンク先を除いて数えた目安）で、features.yaml の仮の題名と多数派が違う語がある。用語集で決めるときの材料にしてほしい：agent view → エージェントビュー（132対36）、予定のタスク（scheduled tasks）→ スケジュールタスク（144対16）、ワークフロー（workflows）→ 公式は「動的ワークフロー」（dynamic workflows）、音声入力（/voice）→ 音声ディクテーション（29対13。ページ名も）、クラウドのセッション → クラウドセッション（288対0）、対話モードの操作 → インタラクティブモード（ページ名。非対話モードは非対話モードのまま）、fast mode は「高速モード」87・「fast mode」79 で割れている（ページ名は「高速モードでレスポンスを高速化」）。管理設定は本文が多数派（397対25。ページ名だけ「マネージド設定」）
5. **名称と旧名（D3 の範囲。メインから渡してほしい）**：一次資料で見つけた名前の変更。scheduled tasks の旧名 routines（/schedule の別名 /routines が残る。routines.md）、/ultrareview は今の呼び方が /code-review ultra で /ultrareview は別名（ultrareview.md）、/simplify は 2.1.147 で /code-review に改名され、2.1.154 で /simplify が片付けだけのレビューとして別に戻った（CHANGELOG）、dynamic workflows の起動の語が 2.1.160 で workflow から ultracode に替わった、/agents は 2.1.198 から作り方の案内を出すだけになった（commands の /agents の行）、Manual モードの設定の値は default（permission-modes）、/ultraplan は削除された（commands）
6. **features.yaml の note**：security-review の「挙動・使える面・版は土台作りで確かめる」と plugin-eval の「成熟度・版の下限・使える面は土台作りで確かめる」は、この下書きで確かめた（data に移したら note を外せる）。code-projects・code-review などの「別の機能」の注は data の note にも残した
7. **D2 との重なり**：effort・fast mode・advisor・context-window は app や api の面も入れた（D2 の adaptive-thinking・app-context-management とは別の id）。11:05 の時点の D2.yml（読むだけ）と URL が重なる出典は3件で、cc-docs-commands・cc-docs-model-config は id も同じ、Help Center の context window の記事は D2 の id（hc-context-window）に合わせた。Help Center と Platform の出典の id は D2 の付け方（hc-・api-docs-）にそろえた。features の id の重なりはない。D2 は load_timing・context_cost をまだ使っていない（§3.1 の語彙と食い違う値はない）

## 5. 確かめていないこと

- **入った版（since）を書いていない30件**：CHANGELOG の最初の版（0.2.21）より古いか、追加の行が見つからなかったもの。claude-md・mcp・permissions・permission-modes・auto-mode（権限の auto モードの行は 2.1.86 から）・managed-settings・settings・plan-mode・clear・context-window・model-selection・effort（effort の行は 2.1.42 から）・insights・ask-user-question・interactive-mode・sessions・btw・voice-dictation・advisor（2.1.117 から）・feedback・verify-skill・security-review・scheduled-tasks・cloud-sessions（2.0.24 に teleport の行）・remote-control・headless・github-actions・code-projects・managed-code-review・ide-extensions。雛形の最低の版が要る機能は、試作で文書の「Requires Claude Code vX or later」の記述から足す
- **成熟度の GA は推測を含む**：公式が成熟度を書かない機能を GA とした（§3.2）。特に Claude in Chrome は 2.0.72 で (Beta) として入り、今の Claude Code の文書と Help Center の Get started には表記がない。mods は 2.1.287 で入ったばかりで既定で有効だが、表記がない
- **公式の呼び方の食い違い**：エージェントチームは今の文書が experimental、2.1.32 の CHANGELOG が research preview と書く（時期の違いと見て、今の文書の値にした。両方の出典を項目に入れた）
- **アプリと API の側**：effort・context-window・fast mode・advisor・Claude in Chrome のアプリと API の面は、Help Center 3記事と Platform の文書4ページの存在と状態だけを確かめた。中身の値（既定の effort、窓の大きさなど）は facts の範囲で、入れていない
- **写し（Internet Archive）**：既存の写しを探していない（archive は空）
- **日本語版**：語彙の表記には日本語版の Extend Claude Code を使い、ほかの日本語のページは題名と語の数えだけに使った（値は英語版から入れた）
- **CLAUDE_CODE_SAFE_MODE・MCP_TIMEOUT などの照合語**：CHANGELOG の行から取った語で、今の文書の表で一つずつは照らしていない（照合語なので、古い語でも害は小さい）
