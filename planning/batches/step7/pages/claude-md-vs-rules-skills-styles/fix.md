# 報告：直し（claude-md-vs-rules-skills-styles）

- 手引きの版：共通 2026-11-04 第1版・型（comparison）2026-11-04 第1版
- 対象：`verify-clarity.md` の指摘 23 件（直す 2・直したほうがよい 12・軽い 9）。すべて扱った。ページ側で直したのは 21 件で、#1 と #3 はページ側で和らげたうえで道具の変更を提案する（6）
- 書かなかった見出し（範囲を越えたこと・止められた操作）は、なしのため省いた

## 1. 書いたファイル

- `docs/extend/claude-md-vs-rules-skills-styles.md`。front matter で変えたキーは `sections`（5 節の title。anchor は変えていない）と `sources`（`cc-docs-permissions`・`cc-docs-debug-your-config` を足した）。`stage` は draft のまま、`updated` は同日の 2026-11-04 のまま
- `data/sources.d/claude-md-vs-rules-skills-styles.yml`：`cc-docs-debug-your-config` を足した
- 雛形（`snippets/claude-md-vs-rules-skills-styles/`）は変えていない

## 2. 直したこと

番号は `verify-clarity.md` の指摘の番号。

| 番号 | 扱い | 直したこと |
| --- | --- | --- |
| 1 | 一部 | 表の幅は、`gen:begin compare` が値のある属性を全部出す作りのため、ページ側では変えられない（`tools/gen/facts.py` の `b_compare`）。表の前に「選ぶときに見る列は 4 つ、ほかは参考」を足して和らげた。道具の変更は 6 |
| 2 | 直した | 「この表の機能は」を、4 つの名前を書いた文に替えた |
| 3 | 直した | 表の直後に「表の読み方」を足し、「—」「未確認」「残る」の意味を言った。rules の「未確認」の説明は rules の項から移し、項には参照の 1 文を残した。値の側（rules を「場合による」と出す）は 6 |
| 4 | 直した | 要点の「何ができるか」を「4 つはどれもお願い → 禁止は鍵（定義つき）へ → CLAUDE.md には理由と相談の基準だけ」の順にした。1 文目は答えのまま |
| 5 | 直した | 軸に A・B・C と名前を付け、問い 5 つの題に軸を書いた。導入は軸を数えるのをやめて選び方に一本化し、長い文を 2 文に分けた（導入は 3 文のまま） |
| 6 | 直した | 問い 6 を番号の列から外し、「1〜5 で種類を決めたあと、ユーザーレベルに替える」の段落にした。一覧に `~/.claude/skills/` を足した |
| 7 | 直した | クラウドの項を 2 つに分け、リポジトリに置くと全員に効くので個人の好みは置かず、setup script で `~/.claude/CLAUDE.md` を書く、とした。問い 6 と食い違わない |
| 8 | 直した | 文体の判断例の理由を、公式の比較（口調・長さ・形はセッション全体、コマンド 1 つで切り替え、CLAUDE.md はどのスタイルでも残る）に基づいて書き直した。CLAUDE.md に書いても指示として働くと認めたうえで、切り替えと、事実と口調が混ざることを理由にした |
| 9 | 直した | 問い 2 に `/output-style` と `/config` のメニューを足し、組み込みの種類と選び方は output-style-modes へ導線を付けた。名前・数・要る版は手で書いていない |
| 10 | 直した | スキル（`/skills`）と出力スタイル（`/output-style`）の確かめ方を足した。CLAUDE.md の「一覧にないとき」に置き場所の確認と `/memory` を足した。末尾に「読み込まれているのに守られないとき」の 1 文と、公式の Debug your configuration へのリンクを足した。`InstructionsLoaded` は `hooks` キーに書くことと、hooks-basics への導線を足した |
| 11 | 直した | 決まり 1 に「片方だけ直すと食い違う」を足した。決まり 2 は判断例 1 と鍵の項の繰り返しなので削り、決まりが 1 つになったので番号の列をやめた |
| 12 | 直した | リリースの判断例の理由に「この設定が止めるのは Claude が自分で呼ぶことだけ」「承認を必ず挟むなら ask ルール」を足した。雛形の前置きに「手順 4 の承認は頼みである」を足した。`cc-docs-permissions` を sources に足した |
| 13 | 直した | 要点と導入に「Claude Code」を入れた。要点の「いつ引くか」に、アプリの Styles は別の機能で末尾の節を見る、を足した |
| 14 | 直した | 各節の最初の文に、CLAUDE.md・rules・スキル・出力スタイルを名前で書いた。見出しの title を 5 つ変えた（anchor は変えていない） |
| 15 | 直した | 問い 1 の目印を「鍵の考え方は〔A〕、手段の選び方は〔B〕を見る」の形にした。問い 1 の鍵にも 1 句の定義を足した |
| 16 | 直した | 「`keep-coding-instructions: true` を付けないと、標準のソフトウェア開発の指示が外れる」と言い切った（出典 output-styles。束 6.3 とも一致） |
| 17 | 直した | `disable-model-invocation: true` の初出に「（Claude が自分では呼ばず、人が呼んだときだけ動く設定）」を足した |
| 18 | 直した | 管理設定（managed settings）は「組織が配り、利用者のファイルでは上書きできない設定」と書いた（表記は prh に従い管理設定）。`--append-system-prompt` は「その起動だけ足す。スクリプトや自動化に向く。自作の出力スタイルと違い標準の指示を外さない」と書いた |
| 19 | 一部 | 迷う候補の「スキルにする」を「rules にする」に替え、理由に「rules も同じお願いで強さは変わらない」を足した。deny ルールとフックの選び方は request-lock-table への導線にとどめ、選んだものは二択のまま残した（このページの論点は鍵かお願いかで、手段の選び方は持ち主のページが持つため） |
| 20 | 直した | 状況に「会話が圧縮されたあと」を入れ、選んだものに「どちらも圧縮の後はディスクから入れ直される」、理由に「違いは置き場所の整理だけ」を足した（根拠：data の rules の note） |
| 21 | 直した | 雛形の前置きに、4 つの雛形と判断例の対応を書いた。組み合わせ方の各項に置き場所のパスを添えた |
| 22 | 直した | rules × サブエージェントを公式の sub-agents の文書で確かめて足した。出力スタイル × クラウドは「確かめていない」と書いた。クラウドのセッションと setup script に 1 句の定義を足し、cloud-sessions-and-teleport と公式の Configure cloud environments への導線を足した。プロジェクトのスレッドでは届く範囲が狭いことも、cloud-environments で確かめて足した |
| 23 | 直した | 見出しを「混同されやすい別の機能」にした（anchor は変えていない） |

## 5. メインに判断してほしいこと

1. 雛形 `claude-md-root` の「`.env` は deny ルールで読めなくしてある」は、言い切りが強い可能性がある。公式の permissions の文書は、Read の deny ルールが、ファイルを名指さずに読む `grep -r` や、別のプログラム経由の読み取りには効かないと書く。事実の検証役が置かれないので、直さずに渡す。直すなら「deny ルールで止めてある」程度に弱める。
2. 見出しの title を 5 つ変えた（anchor は同じ）。ほかのページが title つきで指す所は、再生成で追随する。

## 6. 提案

- 道具（`tools/gen` の compare）。#1 と #3 の本体
  - 全行が同じ値の列（面・成熟度・確認日）を省く。9 列が 6 列になる
  - 列を指定できるようにする（例：`<!-- gen:begin compare cols=強制力,読み込みの時期,… -->`）か、縦横を入れ替える（機能を列にすると 5 列）
  - 値が null のときの言葉を属性ごとに変えられるようにし、rules の「圧縮で残るか」を「場合による」と出す。入ったら、本文の「表の読み方」の rules の文と、rules の項の最後の文を直す
- front matter（任意。write.md の提案に 2 件足した）

```yaml
frontmatter:
  - {id: claude-md-vs-rules-skills-styles, key: related, before: [output-style-modes#vs-claude-md, what-to-put-in-claude-md, where-to-put-instructions, extensions-at-a-glance, request-lock-table, using-auto-memory, hook-vs-skill, when-to-add-what, keep-replies-in-japanese], after: [output-style-modes#vs-claude-md, what-to-put-in-claude-md, where-to-put-instructions, extensions-at-a-glance, request-lock-table, using-auto-memory, hook-vs-skill, when-to-add-what, keep-replies-in-japanese, what-subagents-dont-inherit, skills-in-the-app#migrated-styles, hooks-basics, cloud-sessions-and-teleport], reason: "本文の「確かめ方」「届く範囲の違い」「混同されやすい別の機能」で指しているため（任意）"}
```

- 用語集：write.md の 3 語に加え、管理設定（managed settings）：組織が配り、利用者のファイルでは上書きできない設定（request-vs-lock と keep-replies-in-japanese も使う）
- 手引き：共通 §3 に「要点の「何ができるか」の 1 文目は 90 字ほどまで」と足す。textlint は要点の囲みを 1 つの段落として数え、1 文目には囲みの見出し行と行頭の記号も文字数に入るので、見かけは 100 字弱の文が 120 字の警告に当たる
- 数値の提案：なし（変わりやすい値は手で書いていない。組み込みの出力スタイルの名前・数と `/output-style` の要る版は output-style-modes に任せた）

## 7. 検査の結果

- `gen_site.py --page`：目印を埋め、`--check` で差なし
- `check_pages.py --page`：エラー 0・警告 0
- `check_templates.py --page`：エラー 0・警告 0
- `npx textlint`：最初は警告 3・エラー 2（文長 125、助詞「で」「に」の重なり、prh の Output style と managed settings）。直して 0。`npm run lint:text` でこのページの指摘は 0
- `render_pages.py`：流していない（メインが流す）

## 8. 確かめていないこと

- 足した事実は、公式の output-styles・memory・skills・sub-agents・cloud-environments の Markdown 版を今日取得して読み、debug-your-config・permissions・settings・cli-reference は scratchpad にあった同日の写しで読んで確かめた。事実の検証役は置かれないので、再確認はしていない
- rules が `/context` の「Memory files」に出るかは確かめていない。本文は、公式の debug の文書が「rules とスキルの説明が入っているかも `/context` で確かめられる」と書くとおりに書いた
- `/output-style` を引数なしで流したときの一覧と印は、公式の記述のとおりで、実機では試していない。古い版でのコマンドの動きは未確認
- 出力スタイルがクラウドのセッションで効くかは未確認（本文にも書いた）
- 雛形 4 本は実機で動かしていない（変更なし）。描画（幅 390px・ダーク）は見ていない

## 9. 使用量

- 道具の呼び出しは約 60 回（Read 7・Edit 15・Bash 約 36・Write 1）。Web の取得は 5 回（curl で公式の文書 5 本）。かかった時間は約 18 分
