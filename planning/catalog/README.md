# 目次（catalog）の作り方

全ページの一覧を置く。上位の規則は設計書（[../design.md](../design.md)）の §2〜§5。語彙は [../../schema/site.yml](../../schema/site.yml)。この文書はその詳細である。

catalog は骨格（工程6c）で各ページの front matter の元になる。骨格の後は front matter が正になり、catalog は凍結して執筆の指示（materials・templates・visual）としてだけ使う。

- 版：2026-11-04 第1版（同日、統合の後に §4.5 の4に重なりの規則を足した。工程4で、症状のページの routes〔§3・§4.4 の6〕と第一波の数え方〔§4.6 の3〕を足し、§4.6 の2を設計書 §5.3 に合わせ、§6 に検査を足した）

## 1. ファイル

| ファイル | 中身 | 書く担当 |
| --- | --- | --- |
| `registry.yaml` | 全候補の id・分野・題名・優先度・レベルの見当・出どころの一覧と、古くなった助言の台帳の項目の id の一覧 | 一覧の担当（最初に作る） |
| `<field>.yaml` | 分野ごとの全ページの詳細（§3） | 分野の担当（並列） |
| `features.yaml` | `tracks` で指す機能の id の一覧（§5）。土台作りで data/facts.yml の features に移す | メイン（担当の提案を反映） |

## 2. registry.yaml の形式

```yaml
pages:
  - id: instructions-ignored        # 英小文字・数字・ハイフン。一意
    field: symptoms
    title: CLAUDE.md や指示が守られない
    type: symptom                   # 見当でよい（分野の担当が決め直す）
    priority: 必須                  # 00 の表の値。新しい候補は見当を書き、分野の担当が決める
    level: 整える                   # 00 の L1〜L5 を、使う・整える・任せる・仕組みにする・回す に読み替えた見当
    origin: "00 §3 分野18"          # 出どころ（00 §3 の分野、11 第1節の行の番号、requirements §4.3 など）
    wave_core: true                 # 第一波の核の候補か（核の分野の総論や、多くのページが前提にするもの）
ledger:                             # 古くなった助言の台帳の項目（00 §5 の31項目と research/22 の候補）
  - {id: important-caps, title: "IMPORTANT や YOU MUST で強調すれば守られる", origin: "00 §5"}
```

- id は、題名の英訳か、公式の英語の機能名から作る（例：`hooks-basics`・`instructions-ignored`・`verifier-defines-problem`）。分野の名前を頭に付けない
- requirements §4.2 の各分野の候補数（目安）と合わない大きなずれがあれば、registry の末尾の `notes` に書く

## 3. <field>.yaml の形式

```yaml
field: symptoms
chapters: [指示と仕組み, 会話と文脈, 確かめ方, 安全, 費用と選び方]   # 分野の中の章（ナビゲーションの小見出し）。並び順
pages:                              # 並び順が、ナビゲーションの順になる
  - id: instructions-ignored
    chapter: 指示と仕組み
    title: CLAUDE.md や指示が守られない
    nav_title: null                 # 題名が長いときだけ
    aliases: [指示を無視される, CLAUDE.md が効かない]
    type: symptom
    level: 整える
    level_evidence: "CLAUDE.md を書き始めた段階で最初に出会う"
    priority: 必須
    wave: 1                         # 第一波の核なら 1。核でなければ書かない
    surfaces: [claude-code, app]
    principle: [縛る, 見せる]
    prevents: [散らかっている, 縛っていない]
    pitfalls: []
    scenes: [開発]
    summary: "CLAUDE.md や指示に書いた規則が破られる原因を切り分け、どれを仕組みに移すかを決める。"
    signs:
      - {type: symptom, text: "CLAUDE.md に書いたのに守られない"}
      - {type: symptom, text: "長い会話の途中から規則を無視し始める"}
    prerequisites: [request-vs-lock]  # 症状のページは、診断を読むのに要る概念のページだけ（§4.4 の6）
    routes:                         # 症状のページだけ。原因ごとの振り分け先（§4.4 の6）
      - {cause: 散らかっている, to: [what-to-put-in-claude-md, claude-md-length]}
      - {cause: 縛っていない, to: [when-to-lock, hooks-basics#events]}
    related: [permissions-deny]     # 症状のページは、routes にない近いページだけ
    tracks: [claude-md, hooks, permissions]
    outdated_advice: [important-caps]
    volatility: 中
    sections:                       # 主な節（任意）。level を省くとページと同じ
      - {title: "原因を安く確かめる順", anchor: diagnosis}
    templates:                      # 載せる予定の雛形（任意）
      - {name: "規則を hook に移す例", kind: hook, safety: false}
    visual: {kind: static, text: "お願いと鍵の二層の図"}   # 図の案（任意。kind は static・mermaid・dynamic）
    materials: ["00 §3 分野18", "00 §4 指示と仕組みの困りごと", "research/23 #1", "11 第1節 #12"]
    notes: null
merged:                             # registry の候補を、ほかのページへまとめたもの
  - {id: some-candidate, into: instructions-ignored, reason: "…"}
dropped:                            # 採らなかった候補
  - {id: other-candidate, reason: "…"}
open_issues:                        # ほかの分野への提案、決めきれなかった点
  - "提案：extend に …"
```

## 4. 規則

### 4.1 受け持ちと受け渡し

1. **registry の自分の分野の候補をすべて処理する**：`pages`（採る）、`merged`（ほかのページへまとめた）、`dropped`（採らない）のどこかに入れる
2. **新しいページ**は自分の分野にだけ足してよい。registry にない id は、`notes` に「新規：理由」と書く
3. **ほかの分野**のページは registry の id で指す。ほかの分野へのページの追加・移動の依頼は `open_issues` に「提案：〜」と書く（直接書かない）
4. 書いてよいのは、自分の担当のファイルだけ。git の操作をしない
5. 新しい Web の調査はしない（材料は調査資料と工程2の報告）

### 4.2 ページの単位（設計書 §4.1）

1. 1ページ＝名前・症状・やりたいことで引かれ、独自の「なぜ」か判断を持つ1つの単位。変種は節に、面ごとの違いはタブにする（面ごとにページを分けない）
2. 症状は1症状1ページ。題名は読者の言葉。振り分けが本体で、対処の本体はほかの分野のページ
3. 機能は1機能1ページ（密接な系統はまとめて節に）。全オプションの網羅はしない
4. 比較は混同されやすい組だけ
5. 研究や事例の紹介だけのページは作らない
6. コンテストの分野は固有の論点だけ。一般化できる論点はほかの分野に置き、`scenes` にコンテストを付ける
7. research preview・experimental は概念だけ。周辺製品は一覧のページだけ。本体に入って読者がふつうに触れる機能は使い方まで

分野の境界は設計書 §4.2 の表に従う。

### 4.3 レベル（設計書 §3.1）

1. そのページが最初に要る段階にする。根拠を `level_evidence` に書く
2. `ledger`・`guide`・`hub` は level を書かない
3. 前提に、自分より上の段のページを置かない
4. 比例則：任せる・仕組みにする・回すのページのうち、任せる幅を広げる内容（自律・並列・無人・権限の緩和）のものは、`verify`・`eval`・`enforce`・`safety` のページを前提か関連に持つ
5. 「使う」のページは少なく短くする

### 4.4 前提と関連

1. `prerequisites` は直接の前提だけ（「これを知らないと読めない」もの。4つまで）。推移的に届くものは書かない
2. 前提に循環を作らない。前提と related に同じページを置かない
3. 必須のページの前提は、必須のページにする（第一波と初版を前提でたどって閉じるため）
4. 入ってくる道（どのページの prerequisites・related にも出てこない）のないページを作らない。ただし start の入口のページは除く
5. related は近いものから順に書く（20件まで）。節を指すときは `id#anchor`（相手の sections にある anchor）
6. **症状のページの前提と振り分け先（`routes`）**（design-review DR-02）
   - 症状のページの `prerequisites` は、診断を読むのに要る概念のページ（ふつう basics と start。型が concept・guide・hub のもの）だけにする。level は、その症状に出会う段階にする（§4.3 の1）
   - 原因ごとの対処は `routes` に書く：`routes: [{cause: <prevents か pitfalls の値>, to: [<id か id#anchor>, …]}]`。原因ごとに中心の対処を1〜3件、近い順に書く。routes を持てるのは symptom の型のページだけ。cause には、そのページの prevents・pitfalls の原因を使い、どの原因にも routes を書く（対処のページがない原因は notes に書く）
   - routes には段階と優先度の規則（§4.3 の3、この節の3）を当てない（上の段の対処も、推奨の対処も置ける）。比例則（§4.3 の4）の前提・関連にも数えない。routes の先は、入ってくる道（4）に数える
   - 症状のページの related は、routes にない近いページだけにする（routes に置いたページを、前提・関連に重ねて置かない）
   - 知識マップ・症状の原因別の表（設計書 §8.3）・第一波の数え方（§4.6 の3）・診断の節の目印は routes を読む

### 4.5 文章

1. **title**：読者が引く言葉。症状は読者の言葉、機能は公式の名前。公式の日本語版の訳語に合わせる（設計書 §6.2）。半角英数字と全角文字の間に空白を入れる
2. **aliases**：公式の英語名・旧名・公式の日本語訳・よくある言い換え。題名と同じ語は入れない
3. **summary**：1文目は何ができるか（concept は何が分かるか）。2文・120字以内。だ・である調。「このページ」「ここでは」「扱う」「紹介する」「まとめる」を使わない。**変わりやすい値（数値・既定値・料金・モデルの世代・上限）を書かない**
4. **signs**：読者の言葉で書く。`symptom` は困りごと（「完了と言うのに終わっていない」）、`goal` はやりたいこと（「長い作業を任せたい」）、`situation` は置かれた状況（「チームで導入する」「AI を禁じる大会に向けて練習する」）。機能名を答えとして書かない。症状のページは symptom を2つ以上
   - 症状のページが振り分ける困りごとを、対処のページの signs に重ねて置かない（同じ文も、言い換えも）。対処のページに置く symptom は、その対処が直接の答えになる、より狭い場面の困りごと（例：「CLAUDE.md に書いた禁止が破られる」）にする。ふつうはやりたいこと（goal）の形にする（2026-11-04。逆引きで同じ困りごとが二か所に出ると、振り分けを飛ばす読み方になる）
5. **工程2の訂正を守る**：調査資料の、訂正・注記の付いた主張（`【2026-11-03 訂正】`・`【2026-11-03 注記】`。research/22〜28）を、summary・signs・題名の根拠にしない。materials には、関わる報告の番号も書く

### 4.6 優先度と第一波

1. `priority` は 00 §3 の表を基本にする。新しいページは担当が決め、理由を `notes` に書く
2. `wave: 1` は核の分野の総論と、その分野のほかのページの多くが前提にするページに付ける。入口（start）と症状辞典（symptoms）は全ページに付ける（設計書 §5.3。核の分野は site.yml の first_wave_core_fields：start・symptoms・changes・eval・judgment・japanese。核でない分野には付けない）
3. **第一波の数え方**（design-review DR-02・DR-03。範囲は工程5でユーザーに確かめる。いまの値は仮）：第一波は閉包である。核（`wave: 1` のページ）と、核の症状のページの `routes` の先と、名指しの正本を種にし、そこから `prerequisites` でたどれるページをすべて入れる（routes の先の前提と、正本の前提も含む）。数え方は site.yml の `first_wave` に書く
   - `routes`：routes の先をどこまで種に入れるか。`none`（入れない）・`first`（各 cause の to のうち、最初の必須の先。必須の先がない cause からは入れず、その先は第一波では「準備中」になる）・`all`（優先度を問わず全部）
   - `named`：名指しで入れる正本のページの id
   - `tools/check_catalog.py --stats` が、第一波の数と内訳（wave: 1・前提でたどって届くもの・routes から・named から）、routes を none・first・all にしたときの数、必須の先がない cause の数を出す。内訳は、この順に足したときに新しく増えるページの数（routes から＝routes の先と、その前提でたどって新しく届くページ）

### 4.7 そのほかの項目

- `surfaces`：そのページが扱う面。面ごとに手段が違うならタブを使うので、複数を書く
- `principle`：主に関わる原理（1〜2個）
- `prevents`：そのページが防ぐ・診断する Claude 側の原因。symptom は1つ以上
- `pitfalls`：judgment と、人の側の落とし穴に関わるページ
- `scenes`：例を取る場面（任意）
- `tracks`：feature は必須。§5 の id を使う
- `outdated_advice`：registry の `ledger` の id
- `volatility`：低（原理）・中（機能の使い方）・高（数値・名称・research preview・大会の規則）。requirements §6.1 の層に合わせる
- `templates`：載せる予定の雛形。`kind` は settings・hook・skill・subagent・claude-md・prompt・other。安全とデータの雛形は `safety: true`（動作確認を通るまで載せない）
- `visual`：図の案。動く図（dynamic）は、動かすことで分かりやすくなるものだけ（全体で数個）
- `materials`：執筆の材料になる調査資料の節（例：`00 §3 分野08`・`01 F-1`・`11 第1節 #45`・`research/23 #3`）

## 5. 機能の id（`tracks`）

`tracks` には、次の id を使う。ない機能は、ファイルの末尾の `new_features` に `{id, title, note}` で足す（メインが features.yaml にまとめる）。

| 面 | id |
| --- | --- |
| Claude Code の文脈と指示 | `claude-md`・`rules`・`auto-memory`・`skills`・`subagents`・`agent-teams`・`output-styles`・`mcp`・`plugins`・`marketplaces`・`statusline` |
| Claude Code の縛り | `hooks`・`permissions`・`permission-modes`・`auto-mode`・`sandbox`・`managed-settings`・`settings` |
| Claude Code の操作 | `plan-mode`・`checkpoints`・`compaction`・`clear`・`context-window`・`model-selection`・`effort`・`ultrathink`・`fast-mode`・`usage`・`insights`・`ask-user-question` |
| Claude Code の任せ方 | `goal`・`loop`・`scheduled-tasks`・`workflows`・`worktrees`・`agent-view`・`cloud-sessions`・`remote-control`・`headless`・`github-actions`・`cross-session-messaging` |
| Claude Code の面 | `ide-extensions`・`desktop-code`・`claude-in-chrome` |
| アプリ | `projects`・`project-instructions`・`app-memory`・`chat-search`・`incognito`・`styles`・`personal-instructions`・`artifacts`・`file-creation`・`code-execution`・`web-search`・`research`・`connectors`・`app-skills`・`office-add-ins`・`claude-in-slack`・`voice` |
| API・SDK | `messages-api`・`prompt-caching`・`structured-outputs`・`tool-use`・`batch-api`・`files-api`・`adaptive-thinking`・`citations`・`server-tools`・`computer-use`・`mcp-connector`・`agent-sdk`・`managed-agents`・`token-counting` |
| プランと上限 | `plans`・`usage-limits`・`usage-credits` |

## 6. 検査

`python3 tools/check_catalog.py` で検査する（工程3で作る）。見るもの：YAML の形、必須の項目、語彙（schema/site.yml）、id の一意と書式、registry との対応（registry の候補が pages・merged・dropped のどこかにあるか）、前提・関連・routes の解決（`id#anchor` の anchor を含む）、循環、レベルの逆転、必須の前提は必須、推移的な前提、比例則、入ってくる道、summary の長さと使わない語、signs の種類、逆引きの重複（症状のページの signs と同じ文）、症状のページの routes と前提（§4.4 の6）、tracks の id、outdated_advice の id、wave の付け方（§4.6 の2）、分野ごとの数（優先度・レベル・型）、第一波の数と内訳（§4.6 の3）。

routes の検査（工程4で足した）：

| 重さ | 見るもの |
| --- | --- |
| エラー | symptom でないページの routes、cause が語彙（site.yml の prevents・pitfalls）にない、to が空、to の参照が解決しない（`id#anchor` の anchor も）、cause・to がない、形の誤り |
| 警告 | 症状のページに routes がない、同じページで cause が重なる・1つの cause の to に同じ id が2回ある、1つの cause の to が4件以上、routes の先が同じページの prerequisites か related にもある、routes の cause がそのページの prevents・pitfalls にない・prevents・pitfalls の原因に routes がない、症状のページの前提の型が concept・guide・hub でない、routes の先が registry の候補のまま（未処理の候補） |
