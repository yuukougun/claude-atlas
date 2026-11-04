# build-DM1：数値の提案を data にまとめる（工程8）

## 結果
- 足した facts：56 件（data/facts.yml の facts の末尾。確認済み 39・未確認 17。表の fact 4 件を含む）
- 強制力（enforcement）を足した機能：0 件（下の理由）
- facts-placement.md：66 行（表の行。fact の id 56 件すべてが少なくとも 1 行に出る）
- 検査：`check_pages.py` エラー 0（警告 4 は比例則 3・前提と関連の数 1 で、今回の変更と無関係）／`unittest test_lib*.py` 87 件 OK／facts.schema.json に対する jsonschema 検証 エラー 0
- 道具の呼び出し：約 35 回。Web 0 回。gen_site.py は流していない

## 判断（メインが見る点）
- 合流：同じ値の提案を 1 つの id にした（auto-continue-max-times・clear-after-failed-corrections・app-pdf-visual-pages／app-pdf-text-only-pages・model-knowledge-cutoffs・effort-default-by-model-surface・permission-mode-default-interactive／noninteractive・v2.1.317/v2.1.314 の検索と起動の修正 2 件）。default-safety-settings の claude-code-default-start-mode は、permission-mode-default-* の 2 件に分けて統合し、独立の id にしなかった
- backlog が「同じ id にまとめる」とした forgot-after-compaction の v2.1.317 は、直した不具合が別（圧縮の失敗と要約の取りこぼし）なので、別の id `compaction-bugfix-version` にした（提案の id compaction-bugfix-min-version は、版が「入った最低の版」ではなく「直った版」なので改名）。まとめるならメインが決める
- 検索の修正の版は id を `claude-code-search-truncation-fix-version` に統一（claims-done-but-isnt の `claude-code-search-truncation-fix` は廃止）
- status：提案が「確認済み」とするものだけ確認済み。「要確認」「CHANGELOG で原文を未確認」「一次資料を開いていない」と書くものは 未確認（subagent-own-model-effort-min-version は提案が確認済みだが note に原文未確認とあるので 未確認。default-safety-settings の 3 件〔app-default-permission-mode・sandbox-default-state・incognito-retention-period〕は write.md が「一次資料を開いて確かめていない」とあるので 未確認）
- model-knowledge-cutoffs は knowledge-cutoff（要確認）と doesnt-know-latest（確認済み 2026-11-04）の食い違いを、後者に合わせて 確認済みにした。「現行のモデル」の行はモデルごとの確認ではない（note に書いた）。不安なら 未確認に下げる
- `match`（目印の外の手書きを照らす型）は付けていない（「3 回」「30 日」「5 年」などは本文に別の意味で出て、誤警告が増えるため）
- どの facts も volatility を明示した（既定の「高」にしたのは effort の表・プラン別の表・メモリの既定などプランやモデルで変わるもの）

## 強制力（enforcement）を足さなかった理由と提案
対象の effort・mcp・checkpoints・auto-mode・app-memory・interactive-mode・goal（と context-window〔inspect-context が「なし」と手書き〕）には足さなかった。site.yml の語彙が「お願い」「鍵」の 2 値だけで、どの機能もページ本文の手書きが「鍵に数えない」「なし」「何も止めない」で、2 値のどちらにも当たらない。推測で決めない規則に従い、決められないものとして一覧にする。

| 機能 | ページの手書き | 足せない理由 |
| --- | --- | --- |
| effort | 何も止めない | 設定。お願いでも鍵でもない（ページの担当も同じ判断） |
| mcp | 何も止めない（止めるのは権限・管理設定の側） | 道具を足す仕組み |
| checkpoints | なし（戻す手段） | 止める仕組みではない |
| interactive-mode | 本文に手書きなし（`!` は許可を通らない、`Esc` は変更を戻さない） | 値の根拠が出典にない |
| context-window | なし（見せるだけ） | 止める仕組みではない |
| auto-mode | 鍵には数えない | data の note が「分類器の判断は決定論ではないので強制力は書かない」。お願い（Claude が読む指示）でもない |
| goal | 鍵には数えない | data の note は強制力を書かない。verification-ladder は「鍵」と書き、食い違う |
| app-memory | 止められるものは文で書いた | 出典（hc-memory）に強制か文脈かの記述が確認できない。personal-instructions と同じ「お願い」とみなすのは推測 |

提案（メインか SK が判断）：schema/keys.yml・site.yml の enforcements に「なし」（止める仕組みではない）を足せば、effort・checkpoints・context-window・mcp・interactive-mode は一括で決まる。auto-mode と goal は「モデルの判定」の値（例：判定）を足すか、手書きのままにする。app-memory は hc-memory を読んだ検証役が「お願い」と確かめれば足せる。

## 入れなかった提案
| 提案 | 理由 |
| --- | --- |
| where-to-put-instructions の app-instruction-scope-and-timing | 値が「本文の表のとおり」で 1 つに決まらない（backlog どおり） |
| what-auto-mode-stops の auto-mode-classifier-rates-2026-03-25（0.4%・17%・5.7%）と destructive-commands の auto-mode-overeager-miss-rate（17%・n=52） | 研究の固定の記録で、記事の日付とデータの種類を添えて手書きでよい（batch2-decisions 7・common §9・decisions 2026-11-05）。2 件を 1 つにする案も不要 |
| how-thinking-works の effort-default-by-model-surface（値が説明文） | effort-levels の表の fact に統合（入れ直した） |
| lethal-trifecta・prompt-injection-in-practice の v2.1.317（クラウドの予定のタスクのコネクタ警告・メールアドレス確認） | 提案の YAML がなく、出典の id も title も束にない。research/22 #27・#9 の写しで、sources に入れる CHANGELOG の確認がない。出典が決まれば足せる |
| align-japanese-output の確認日つき挙動に付ける Claude Code の版（「採るなら」） | 提案に値も出典もない |
| default-safety-settings の claude-code-default-start-mode（独立の id） | permission-mode-default-interactive／noninteractive に統合 |
| how-thinking-works の effort の「新しい版」2 件 | effort-levels の effort-model-settings-min-version・subagent-own-model-effort-min-version として入れた |

## 注意（検証役向け）
- 未確認 17 件の値は、提案のとおりに写しただけ。CHANGELOG・各公式文書での確認が要る（hook-* の 4 件・v2.1.314/317 の 4 件・default-safety の 3 件・mcp・auto-mode のブロック回数・fishtest・at-reference・tokenizer-token-range-opus-5-5・subagent-own-model-effort）
- 確認日は提案の日付のまま。表と合流した項目は、合流元の古いほうにした（clear-after-failed-corrections は 2026-11-03）
