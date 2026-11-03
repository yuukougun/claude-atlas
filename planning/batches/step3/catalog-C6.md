# 工程3 C6：extend（文脈と指示を仕組みにする）の目次の報告

- 担当：C6（2026-11-04）
- 書いたもの：[planning/catalog/extend.yaml](../../catalog/extend.yaml)
- 指示：[brief-catalog.md](brief-catalog.md)。形式と規則は catalog/README.md §3・§4、語彙は schema/site.yml

## 1. 書いたファイルとページ数

| 項目 | 数 |
| --- | --- |
| ページ | 24（registry の候補26のうち、採る24・まとめた2・採らない0。新しいページ0） |
| 優先度 | 必須 15・推奨 8・任意 1 |
| レベル | 任せる 15・仕組みにする 9（使う・整える・回すは0） |
| 型 | feature 16・comparison 5・concept 2・recipe 1 |
| 章 | 全体と使い分け 2・CLAUDE.md・rules・自動メモリ 7・スキル 5・サブエージェント 3・MCP 3・プラグイン 3・見直し 1 |

- 比較のページ（comparison）は、混同されやすい組だけ：extensions-at-a-glance（総覧）・claude-md-vs-rules-skills-styles・hook-vs-skill・skill-vs-subagent・mcp-or-cli。表は数値ファイルの機能の属性から生成する前提で書き、ページには属性を持たせていない（design §3.3）。表に並べる機能を道具に渡すため、comparison にも tracks を書いた
- 雛形は16ページに26個（skill 6・settings 6・prompt 5・claude-md 4・subagent 3・hook 1・other 1）。`safety: true` は3個（MCP の資格情報の2つと、副作用のあるスキルを Claude から呼べなくする1つ）
- 人の側の落とし穴（pitfalls）：claude-md-length・writing-skills・pruning-extensions に「体感を信じる」（00 §4 の「CLAUDE.md を変えて良くなったか知りたい」）、using-auto-memory に「預けすぎる」を付けた
- registry からの変更：
  - 題名：公式の日本語版の多数派の訳語（research/27 §3.1）に合わせ、スキル・サブエージェント・フック・プラグイン・マーケットプレイス・出力スタイル・自動メモリにした（英語名は aliases）。enforce・basics の担当も同じ案。ほかに when-to-add-what を「拡張を足すタイミング」、choosing-mcp-servers を「MCP サーバーの選び方」（D13 に合わせ、推薦の一覧でなく判断の基準のページにした）
  - level：mods だけ「回す」から「仕組みにする」に改めた（並列・無人・定期・プログラムからの実行とは関係せず、プラグインで環境を常設化する段階のため）。ほかは 00 §3 の L3・L4 のまま
  - 優先度と型：変えていない

## 2. まとめた候補・採らなかった候補・新しいページ

| 候補 | 扱い | 理由 |
| --- | --- | --- |
| what-to-leave-out-of-claude-md | what-to-put-in-claude-md へまとめた（節 `what-to-leave-out`） | 「この行を CLAUDE.md に置くか」という一つの判断の表と裏で、00 §4 の逆引きも一つの行から両方を指す。書かない行の多くは移し先（linter と hook・rules・skills・deny）を示すのが本体なので、残す行と並べたほうが一度で判断できる。題名を「CLAUDE.md に書くこと・書かないこと」にし、旧の題名は aliases に置いた |
| commands-became-skills | writing-skills へまとめた（節 `from-commands`） | カスタムコマンドは skills に統合された同じ機能の旧名。古い記法は台帳の commands-directory が持ち、残る中身（既存のファイルは動く・移ると何が増えるか）は作り方の一部。旧名は aliases に置いた |

- 採らなかった候補・新しいページ：なし。迷ったのは、モノレポで指示を分けるレシピ（claude-md-loading-order の節 `monorepo` と path-scoped-rules で足りる）と、拡張が効いたかを確かめるページ（eval の measure-changes が CLAUDE.md・skill の変更を対象にしている）で、どちらも作っていない

## 3. wave: 1

extend は第一波の核の分野ではないので、付けていない。

## 4. ほかの分野への提案（open_issues の要約）と new_features

open_issues は12項目。主なもの：

1. **まとめた id の指し直し（全分野・メイン）**：what-to-leave-out-of-claude-md・commands-became-skills を指していれば、まとめた先（`what-to-put-in-claude-md#what-to-leave-out`・`writing-skills#from-commands`）に直す。**最後の全体の検査の時点で、cli の init-and-first-claude-md の related がまとめた id を指している（エラー1件。cli の担当かメインが直す）**。enforce の when-to-lock の同じ参照は、途中で直っていた
2. **output style の置き場所（cli・工程4）**：機能のページは cli の output-style-modes（整える）に置かれた。design §4.2 の境界では extend にも読めるが、組み込みの切り替えの操作が中心なら cli でよい。両方の側から相互に指している
3. **台帳（changes）**：changes の担当の「コンテキストを守るために subagent を使う」を足す案に賛成した。足したら writing-subagents も outdated_advice で指す。basics の subagent-isolation・context の research-in-subagents・extend の writing-subagents の書き方は揃っている
4. **境界**：cli の init-and-first-claude-md（/init の操作と叩き台）と what-to-put-in-claude-md（何を残すか）、context の always-on-costs（なぜ）と extend の早見表・棚卸し、safety の vetting-extensions（入れる前の確認と MCP の脅威の型）、app の skills・connectors・plugins のページ（アプリに固有の操作だけを app に）
5. **symptoms**：instructions-ignored・repeating-the-same-explanation・replies-in-english・forgot-after-compaction から extend のどのページを指すかの案
6. **team**：CLAUDE.md をチームの合意文書として運用する話（11 第2節 p56#64）は claude-md-length の節 `team` に置いた
7. **表記（用語集）**：題名の訳語を research/27 §3.1 の案に合わせた。registry とほかの分野に英語の表記が残る
8. **決めきれなかった点**：choosing-mcp-servers を残すか、mcp-or-cli にまとめるか（工程4へ）

ほかの分野からの extend への提案は、すべて反映した：

- delegate：writing-subagents の related に choosing-parallel-modes
- enforce：hook-vs-skill から hooks-basics、writing-subagents・what-subagents-dont-inherit から `hook-recipes#subagent-only` と、disallowedTools に指定子を付けても Bash 全体が外れる注意
- team：plugins-and-marketplaces の related に share-team-settings・org-managed-settings-and-mcp、what-to-put-in-claude-md の related に ai-usage-guidelines
- app：connecting-mcp に Desktop の Code タブが claude_desktop_config.json を読むことと写し方、plugins-and-marketplaces・how-skills-load にアプリから Claude Code への同期と app のページへの関連
- cli：claude-md-vs-rules-skills-styles から `output-style-modes#vs-claude-md`、claude-md-length から `init-and-first-claude-md#prune`

ほかの分野がまとめた id も、まとめた先に指し直した（models の when-to-use-haiku → opusplan、cost の claude-code-costs → `what-uses-up-limits#find-what-uses-it`）。

**new_features（2つ）**

| id | 題名 | 理由 |
| --- | --- | --- |
| `mods` | Mods（プラグインの hooks module） | plugins の一部だが、成熟度と版の下限を別に持つ。mods が tracks で指す |
| `code-intelligence` | code intelligence プラグイン（LSP） | 公式の Extend Claude Code の表で独立の行を持ち、読み込みの時期とコンテキストのコストが plugins と違う。code-intelligence-plugins と extensions-at-a-glance が tracks で指す |

agent teams と output styles の機能のページは、delegate（agent-teams-experimental）と cli（output-style-modes）にあるので、extend では比較のページの tracks で指すだけにした。

## 5. 検査の結果

`python3 tools/check_catalog.py --field extend`（2026-11-04、分野のファイル20の時点。api・japanese・symptoms はまだない）：**エラー 0 件、警告 2 件**。

| 警告 | 残した理由 |
| --- | --- |
| agents-md：[比例則] | 指示をほかのツールと共有するページで、任せる幅を広げない。notes に「比例則：対象外」と理由を書いた |
| how-skills-load：[比例則] | 読み込みの仕組みの説明（concept）で、任せる幅を広げない。notes に同じく書いた |

- 任せる幅を広げる内容のページ（MCP・プラグイン・mod・スキル・サブエージェント）は、safety の vetting-extensions・lethal-trifecta、enforce の permission-rules・hooks-basics、verify の independent-review を related に置いた。前提にしなかったのは、相手がこちらを前提に置いたときの循環を避けるため（実際に safety の vetting-extensions は connecting-mcp を、app の skills-in-the-app は how-skills-load を前提に置いている）
- 前提は basics（request-vs-lock・where-instructions-sit・attention-budget・what-survives-compaction・subagent-isolation・agent-loop）、context の always-on-costs（相手が extend のページを前提にしていないと確かめてから、claude-md-length と pruning-extensions の前提にした）、自分の分野だけにした。レベルの逆転と「必須の前提は必須」は手元のスクリプトでも確かめた
- 全体の検査（`-q`）はエラー15件で、extend のまとめによるものは cli.yaml の1件だけ（§4 の1）

## 6. 確かめていないこと・迷った点

**確かめていないこと**

- 一次資料は開いていない（指示どおり）。機能の事実は 01・02 と工程2の報告（research/22・23・26〜28）による。01 の Best practices を出典にした項目（A-1 の含める／除外の表など）は改稿前の版の要約の可能性があり（01 冒頭の注記）、執筆の前に現行の版で確かめる必要がある（notes に書いた）
- まだファイルのない symptoms（7ページ）と japanese（3ページ）の id は registry で指した。相手がまとめたり落としたりすれば、参照のエラーになる
- 00 §3 の「40個を超えたら見直す」（pruning-extensions）の出どころと、「成否の9割を決める」（skill-descriptions）の根拠は確かめていない。どちらも題名・要約・サインに使っていない
- Agent Skills の標準の移管（research/22 §3.7）は、工程2で題と要約しか見ていない
- code intelligence と mods の公式の日本語の表記（題名は英語の機能名にプラグインを足した形）

**迷った点**

1. **2つのまとめ**：00 は別のページとして必須にしていた。ページの単位（design §4.1 の1・3）と逆引きの形から、まとめたほうが判断が一か所で済むと見た。工程4で分け直すなら、節の anchor をそのまま id にできる
2. **choosing-mcp-servers**：「よく使われる MCP」の一覧は D13 と衝突しやすい（research/21 §2.4）。判断の基準のページに題名を変えて残したが、mcp-or-cli にまとめる案もある
3. **output style の置き場所**：cli に置かれたまま、相互に指す形にした（§4 の2）
4. **前提の置き方**：循環を避けるため、ほかの分野のページは原則 related で指した。その結果、知識マップで extend の前提は basics と自分の分野に寄る
5. **pitfalls**：judgment のページではないページに付けたので、付けすぎかは工程4で見てほしい
