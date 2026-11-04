# 工程7：残りの判断事項の決め（メイン、2026-11-05）

[decisions-needed.md](decisions-needed.md) の48件のうち、AP（[build-AP.md](build-AP.md)）が当てなかったものを、メインが決めた。番号は decisions-needed.md の番号。担当の記号：TA＝道具（ページの部品）、TB＝台帳と data、PF1・PF2＝ページと目次の直し（TA・TB の後）、M＝メイン、作者＝作者への頼み（progress.md）。

## 道具（TA）

| 番号 | 決め |
| --- | --- |
| 18 | `tools/checks/template_keys.yml` の `settings.top` に `skillOverrides` を足す（出典は cc-docs-skills の「Override skill visibility from settings」）。雛形の名前の改め（settings.local.json の形）は PF1 |
| 22 | compare の表：(1) 目印で列を指定できる（最優先。指定がなければ今の列）(2) 全行が同じ値の列は、表から省き、表の下に「すべて共通：…」の1行で出す (3) 値が null のとき、「未確認」（確かめていない）と「条件による」（条件で値が変わる）を出し分ける。data の書き方は最小の変更で schema/keys.yml に足す |
| 26 | check_pages の「link の目印」は、`outdated-advice-ledger#<台帳の行の id>` を、行の id が data/outdated-advice.yml にあれば通す（台帳の行の anchor は行の id。TB は変えない） |
| 28 | fact-table：セルの `sources` を行ごとの出典として出す（表の下の1段落にまとめない）。check_pages は、`gen:begin fact-table <id>` の未登録の id を `fact` と同じに止める |
| 31(b) | 主催者の公式 X の投稿を出典にできるよう、schema/site.yml の source_kinds に投稿の種類を足す（名前は既存の語彙に合わせる）。書き方の文は M が common §11 に書く |
| 34 | (a) expect.yaml に `open: true` を足すと、雛形の枠を開いた状態（`???+`）で出す。既定は今のまま閉じる (b) link の目印の出力の形は今の「ページの題 › 節の題」のままにする（直さない）(c) expect.yaml に、要る最低の版を facts の id で指す項目を足す（features の since より優先）(d) expect.yaml の形は、TA が足した項目を含めて card §10 に1つの形で書く |
| 41(a) | `text`・`markdown` のコードブロック（頼み方の例文など）だけ、サイトで折り返す（overrides/assets/css/ca.css）。プログラムのコードは今のまま横に送る |
| 43(a) | link の目印で分野の入口を指せるようにする（形は TA が決め、card §3 に書く。表示は分野の名前） |
| 45 | routes の表は、行き先を1つずつセルの中で改行して並べる（表の形は残す） |

## 台帳と data（TB）

| 番号 | 決め |
| --- | --- |
| 23 | T1〜T5 を入れる（案の全文は pages/outdated-advice-ledger/fix.md の 6）。行の anchor は行の id のまま |
| 24 | D2〜D7 の文面を写す。names の current（routines-to-scheduled-tasks）の変更は、data/sources.yml の一次資料で今の名前を確かめられたときだけ変え、できなければ報告に書く。5行の原理の付け直しは、台帳の読み方の節と食い違わないものだけ当て、迷うものは報告に書く |
| 25 | 行 ralph-loops の題は仕組みの名前で付ける。「Ralph」は検索のための中立の呼び名として本文に1回だけ書く |
| 32 | data/facts.yml に `subagent-handback-min-version`（出典 Hooks reference の SubagentStop input、確認日 2026-11-05）を足す。本文の目印は PF1 |
| 42(c) | 公式の学習サイトの名前を data/facts.yml の names に足す（今の名前 Claude Academy・旧名 Anthropic Academy・改名の時期は不明）。出典の academy.claude.com は check_noai.py で確かめてから sources に足す |

## ページと目次（PF1・PF2。TA・TB の後）

| 番号 | 決め |
| --- | --- |
| 5 | 三段の呼び名を「この辞典の推奨」にする（ページは PF1。design §6.6・common §8・card は M） |
| 7 | how-to-use の volatility を 中 に（目次とページ） |
| 12 | four-specifics の title と summary を「4 点」に、目次の節の題も「境界の入力」に合わせる |
| 16 | 目次の agreement-is-not-evidence の節 hard-to-notice の題を、本文の見出しに合わせる（PF2） |
| 18 | writing-skills の雛形 `skill-override-off.json` を settings.local.json の形に改める |
| 22 | claude-md-vs-rules-skills-styles・instructions-ignored の compare の目印で列を絞り、rules の「圧縮で残るか」の文を、新しい出し分けに合わせて直す |
| 26・27 | 原理のページ（four-principles）と台帳の行へのリンクを link の目印に戻す（four-specifics・request-vs-lock・outdated-advice-ledger・writing-skills） |
| 32 | keep-replies-in-japanese の「新しい版」を、facts の目印に替える |
| 33 | keep-replies-in-japanese の節 #measure の題を「検証の方法」に変える（anchor は変えない）。結果は載せない |
| 34(a) | keep-replies-in-japanese の雛形を `open: true` にする |
| 35 | 目次の cloud-sessions-and-teleport の notes に「keep-replies-in-japanese のクラウドの節にある Projects の説明を、このページに寄せる」を足す |
| 36 | 雛形 `claude-md-root` の「`.env` は deny ルールで読めなくしてある」を、「`.env` を読む操作は deny ルールで断ってある（別のプログラムを通した読み取りまでは止まらない）」の向きに弱める |
| 39 | 目次の model-based-grading の notes に「agreement-is-not-evidence の §3 末と §4 の例外の文と、位置づけを合わせる」を足す |
| 42(c) | how-to-use の学習サイトの名前を names の目印に替える |
| 43 | (a) 症状辞典の入口へのリンクを、分野の入口を指す link の目印にする (b) 雛形は残す (c) 目次の how-to-use の sections に `{title: 信用してよいかの見方, anchor: trust}` を badges の次に足し、official-docs の題を「公式の文書・公式の教材との役割分担」にする (d)「どの段階でも」を「どのレベルでも」にそろえる |
| 44 | request-vs-lock の surfaces を `[claude-code]` に絞る（目次とページ）。目次の notes に「アプリと API の鍵を調べて足したら surfaces を戻す」を足す |
| 46 | 目次の templates に、instructions-ignored の `claude-md-command-rule`、request-vs-lock の `lock-settings`・`request-claude-md` を足す。目次の claude-md-loading-order の notes に「AGENTS.md は、CLAUDE.md が作業ディレクトリかその上にあると読まれない」を足す |
| 検査 | 試作の14ページ（tools/gen/config.yml の held_back）の check_page.py をエラー0・警告0にする |

## メイン（M）・作者

| 番号 | 決め |
| --- | --- |
| 1〜4 | 作者の承認（工程7の終わりにまとめて頼む） |
| 5 | design §6.6・common §8・card を「この辞典の推奨」に直す |
| 21 | 研究の結果（割合・件数・対象のモデルの名）は、その研究の時点の固定の記録で、変わりやすい値に当たらない。研究の名・年・対象を添えれば本文に書いてよい、と common §9 と card に書く。今のモデルの名・既定値・上限は、今までどおり目印で書く |
| 29 | 表に「禁止」の行を足さない（「大会の規則の版」の決めを厳しく読んだまま） |
| 30 | (a) 備考の、類型の根拠の1文は残す (b) 図を表から作る案は、第一波の後に検討する（design の後回しの一覧に足す）(c) Codeforces の規則の URL は、作者が足すかを作者への頼みに入れる（codeforces.com は資料にしない。読者のためのリンクだけ） |
| 31(b) | common §11 に、主催者の公式 X の投稿を出典にする書き方を書く（投稿の本文だけを読む、投稿の中のリンクはたどらない、domains は x.com） |
| 37 | (a) rules を2機能に分けない (b) 6節のまま (c) 日付は sources.yml の note のほう (d) 本文は公式の memory の文書に従ったままにする（事実の検証は置かない） |
| 38 | Science の公刊版は、第一波でこのページを直す機会に足す（今は直さない） |
| 40 | (a)〜(c) このまま。(d) 用語集ができたら初出のリンクを付ける |
| 41(b) | 段落のまま |
| 42(a)(b) | (a) design §6.4 を、overrides/main.html のバッジの列に合わせる (b) 違いを書いたまま |
| 45 | 持ち主のページへ細部を移すのは、そのページを書く波で |
| 48 | 書式の早見は card.md（v3）で済んだ。束の欄を足す案は見送る |
| 17 | 「公式の文書」を正規形にする（requirements と catalog の「公式ドキュメント」はそのまま。用語集の本文を書く波で表に整える）。「条件つき→条件付き」の prh の規則は、block-with-exit-2 の表が直った後に M が足す |
