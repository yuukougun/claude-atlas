# 報告：直し（writing-skills）

- 手引きの版：共通 2026-11-04 第1版・型（feature）2026-11-04 第1版
- 対象：`verify-clarity.md` の指摘 17 件（直したほうがよい 9・軽い 8）。直した 16・暫定で直した 1（3）・見送り 0

## 1. 書いたファイル

- `docs/extend/writing-skills.md`（front matter は変えていない。`stage` は draft、`updated` は 2026-11-04 のまま）
- `snippets/writing-skills/`：`SKILL.md`・`SKILL.expect.yaml`（スクリプトなしの最小の例に差し替え）、`SKILL-with-script.md`・`.expect.yaml`（もとの `SKILL.md`。新規）、`allowed-tools.yaml`・`.expect.yaml`（新規）、`skill-override-off.expect.yaml`（題に書き先を入れた）
- `planning/batches/step7/pages/writing-skills/facts-proposal.yml`（各 note の「本文の足し先」を、直した後の文に合わせた。10 件のまま）
- `planning/batches/step7/pages/writing-skills/fix.md`

## 2. 直したこと

- 1：直した。要点の「いつ引くか」に、コマンドはスキルにまとめられ既存のものは今も動くこと、急いで移さなくてよいこと、判断は節 from-commands にあることを足した。
- 2：直した（案 a）。節 minimal の例をスクリプトなしにし、スクリプトを呼ぶ版とスクリプトは節 supporting-files へ移した。引数の渡し方もそこに書いた。
- 3：暫定で直した。数字は書かず、各所に公式の文書の該当の節へのリンクを付けた（name・description の上限、行数、目次の長さ、圧縮後の量、一覧の上限）。メインの判断待ち（5）。
- 4：直した。節 evaluate に「確かめる材料は書く前に集める」段落を置き、書いた後なら過去の会話から選ぶと書いた。手順 3 と判断例はその依頼を使う形にした。
- 5：直した。手で書く先を `.claude/settings.local.json` と書き、共有の `.claude/settings.json` に書くと全員で切れると添えた。雛形の題にも書き先を入れた。
- 6：直した。段落を「中身を読む → 省く方法」の順にし、1 行の雛形 `allowed-tools.yaml` を足した。許可するコマンドは本文のコマンドと同じ形で書く、と行動の形にした。
- 7：直した。3 項目に分けた（同名の優先順位／組み込み・同梱と同名／`verify`・`simplify`）。「元のコマンドの別名」「ローカルのターミナルのセッション」と基準を書き、順序の言い換えは 1 回にした。
- 8：直した。「移る前」の雛形を手順の前に出し、手順の後に、移った後に変わる点（`description`・`name`・引数）を箇条書きで示した。雛形は足さない案を選んだ。
- 9：直した。節 from-commands の冒頭に「これ以降は特に断らない限り Claude Code の話」と書き、アプリは skills-in-the-app に任せた。supporting-files・evaluate・limits にも面を書いた。
- 10：直した。「失敗したときの出し方」を 4 つ目の項目に分け、`collect-changes.sh` の止まる部分を例にした。
- 11：直した。`name` は Claude Code だけなら省ける、アプリや API へ持ち出すなら足す、にそろえた。「読み込む手がかり」は `description` だけにした。
- 12：直した。要点で「別のファイル（補助ファイル）」と言い換え、定義に「スクリプトを除く。公式の supporting files はスクリプトも含む」を足した。用語集の追加は write.md §6 のまま。
- 13：直した。状況に「作る前に取りこぼしがあり、依頼を数件控えた」を足し、候補を実際に迷う 3 つ（配る／もう数回試す／有無を比べる）に直した。
- 14：直した。手順 2 に、期待を先に箇条書きで書いて出力を照らす、と書き、`release-notes` の期待を 3 つ例にした。
- 15：直した。節 minimal の末尾に skill-creator の案内を足し、節 evaluate に、依頼ごとにサブエージェントが走りトークンと時間がかかることを足した。
- 16：直した。フロントマターの `hooks` はスキルを呼んだときからセッションの終わりまで効く、設定のフックはイベントのたびに動く、と使い分けを書いた。
- 17：直した。サブフォルダのコマンドは今も `/<フォルダ>:<名前>` で呼ぶ（現在形）と書き、スキルでは区切りが入らないので `frontend-component` のように付け直す、と例を添えた。

## 5. メインに判断してほしいこと

- **数値の書き方**（write.md §5 と同じ件）：指摘 3 は暫定でリンクにした。`facts-proposal.yml` の 10 件を数値ファイルに採用するなら、note の場所に目印を足し、そのときリンクは外す。採用しないなら、リンクのままでよいか
- **雛形の「要る最低の版」**：新しい 2 つ（`SKILL-with-script`・`allowed-tools`）にも tracks の版が出る。`${CLAUDE_SKILL_DIR}` と `allowed-tools` の `Bash(…)` の書き方が入った版は確かめていない（write.md §5 と同じ件）

## 6. 提案

- 用語集（補助ファイル）：write.md §6 の案に「公式の文書の supporting files はスクリプトも含む」を併記してほしい（本文の定義はそうしてある）
- front matter・数値：新しい提案なし（数値は `facts-proposal.yml` の note を更新しただけ）

## 7. 検査の結果

- `gen_site.py --page writing-skills`：注意なし（2 回目は書いた 0 ファイル）
- `check_pages.py --page writing-skills`：エラー 0・警告 0
- `check_templates.py --page writing-skills`：エラー 0・警告 0
- `npx textlint docs/extend/writing-skills.md`：エラー 0・警告 0（途中で助詞の重なり・読点の数・同じ接続詞の警告が出て、文を直した。囲みの中の箇条書きは行をまたいで 1 文に数えられるので、行を変えても読点が足し算になる）
- `npm run lint:text`：自分のページの指摘は 0（全体の 2 件は他のページ）
- `render_pages.py`・`check_svg.py`：流していない（メインが流す。図はない）

## 8. 確かめていないこと

- 事実は、公式の文書（skills・Platform の best-practices・hooks・permissions）を 2026-11-04 に取得して照らした。照らした主張：`skillOverrides` の書き先、`allowed-tools` の形と末尾の ` *`、`hooks` の効く期間、同名の優先順位、サブフォルダのコマンドの呼び方、skill-creator の動き。リンクの節の anchor も見出しと照らした
- 雛形はどれも実機で動かしていない。新しい `allowed-tools` の 1 行が実際に確認を省くかは、公式の文書の例に倣って書いたが、実行していない
- 共有の `.claude/settings.json` に書くと全員で切れる、は推論である（公式の文書は「user・project・local の設定で名前に当たる」と書く）。実機では確かめていない
- `name` にコロンを書けるかは確かめていない（本文は付け直す例だけを書いた）
- アプリでの `${CLAUDE_SKILL_DIR}` とスクリプトの動作（本文に「確かめていない」と書いた）、公式の日本語版、Windows・macOS・IDE の拡張、描画

## 9. 使用量

- 道具の呼び出し：約 60 回（Read 約 15・Bash 約 40・Write 2）。Web の取得：4 回（curl で skills・best-practices・hooks・permissions の Markdown。WebFetch は 0 回）。かかった時間：約 18 分
