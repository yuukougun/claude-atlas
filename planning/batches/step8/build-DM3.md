# build-DM3：バッチ4・5の数値と強制力を data にまとめる（工程8）

## 結果
- 足した facts：32 件（data/facts.yml の facts の末尾。確認済み 9・未確認 23。表の fact 2 件を含む）
- 強制力を入れた機能：4 件（ultrathink＝お願い、compaction・artifacts・worktrees＝なし）
- 目印を置いた数（ページごと。fact の目印／fact-table／feature の目印）：current-models 2／0／0、thinking-keywords 5／0／1、after-switching-models 1／0／0、let-claude-ask 2／0／0、compact-and-auto-compact 6／0／1、files-and-code-execution 2／1／0、artifacts-overview 1／0／1（要点に強制力の行を新設）、path-scoped-rules 0／1／0、how-skills-load 1／0／0、pruning-extensions 1／0／0、headless-basics 2／0／0、sdk-comparison 1／0／0、parallel-with-worktrees 0／0／1（手書きを替えた）。must-know-operations・parallel-and-loop-costs は置いていない（下の理由）
- mcp-or-cli：tracks を `[mcp, skills]` にした。比較の表が MCP とスキルの 2 行になった
- 検査：`check_page.py` は変えた全ページでエラー 0（1 ページ最大 2 回。parallel-with-worktrees だけ 2 回）／`check_pages.py` エラー 0（警告 4 は比例則 3・前提と関連の数 1 で既存）／`facts.schema.json` に対する jsonschema 検証 エラー 0。gen_site.py の全体は流していない
- 道具の呼び出し：約 55 回。Web 0 回

## 判断
- status：担当の write.md が「一次資料を開いた」と書くものだけ 確認済み（auto-compact-window-range・file-creation-size-limit・code-execution-network-egress-defaults・shared-chat-with-created-files-restriction・plugin-not-used-recently-threshold・plugin-context-cost-highlight-threshold・headless-permission-prompts-min-version）。ほかは、提案が「確認済み」でも「束の写し・原文を開いていない」とあれば 未確認。「要確認」「食い違いあり」も 未確認
- 例外の 確認済み 2 件（data の既存の 確認済み の項目と一致するため）：ultrathink-raise-min-version-terminal（features の ultrathink の note が「2.1.311 以降」）、artifacts-rebuilt-date（features の artifacts の note が「2026-09-16 から今の形」）。不安なら 未確認 に下げる
- 合流：sonnet-4-5-retirement と sonnet-4-5-api-retirement-date → `sonnet-4-5-retirement-date`。headless-default-permission-mode → 既存の permission-mode-default-noninteractive（同じ値）。doctor-prompt-audit-min-version・path-scoped-rules の文字数の上限（claude-md-on-demand-char-limit）は data に既にあり、足していない。headless-startup-failure-exit-code-fixed-version は前半（2.1.314）が既存の claude-code-p-startup-failure-exit-code-fix-version と同じなので、後半（2.1.317・書き込みの失敗）だけ `claude-code-p-write-failure-exit-code-fix-version` に分けた
- 表にした fact：code-execution-network-egress-defaults（プラン × 既定）、artifacts-template-availability（テンプレート × 使えるプラン。未確認）
- 目印の置き方：未確認の項目は、括弧・「は、〜である」の形に置いて、出力の「未確認」が文として読めるようにした（確認済みになれば値の文に替わる）。値が出ても読める文にしてある
- 強制力の線引き：decisions 2026-11-05 のとおり、読んで従うよう頼むだけ＝お願い（ultrathink）、止める仕組みがない＝なし（compaction・artifacts・worktrees）。parallel-with-worktrees の手書き「鍵ではない」は目印に替えた。ほかのページの手書きの強制力は触っていない
- 強制力の目印を `feature ultrathink/enforcement` と機能の id つきにした（thinking-keywords の tracks は ultrathink・effort の 2 つで、先頭に依存しないため）

## 入れなかった提案と理由
| 提案 | 理由 |
| --- | --- |
| current-models-lineup（4 系統の表） | 提案の cells が「research/02 §3-1 の表をそのまま移す」の指示だけで、値がない（research は repo にない） |
| haiku-4-5-removed-from-app-selector | 出典の id が data にない（current-models は記事名の文字列、after-switching-models は空）。値は 2026-10-29（research/22 #23）。出典が決まれば足せる |
| artifacts-template-maturity | 公式同士が食い違い、値が 1 つに決まらない（features の artifacts の note に食い違いを記録済み） |
| pruning-extensions の「40 個を超えたら見直す」 | 提案に値も出典もない |
| parallel-and-loop-costs の「約 15 倍」（2025 年の Research 機能） | 提案に fact がない（本文は研究の固定の記録として手書きのまま） |
| バッチ5の mcp-or-cli の mcp-output-warning-tokens／default-limit-tokens | 既存の mcp-output-token-limits（未確認）と重なる。今回の対象ページ外 |
| バッチ4・5の残り（choosing-a-surface・show-examples・using-projects・connectors-in-the-app・permission-modes-in-the-app・usage-context-statusline・when-to-add-what・hook-recipes・parallel-with-worktrees の 3 件・can-i-prompt-in-japanese） | 指示の 14 ページの外。次の担当へ |

## 強制力を入れなかった機能
| 機能 | 理由 |
| --- | --- |
| file-creation・code-execution | ネットワークの設定（出口を止める。鍵に近い）と、機能そのもの（何も止めない＝なし）で値が分かれる。分けるか、鍵かなしかは作者の判断 |
| connectors | 道具を足す機能（mcp と同じ「なし」）と、ツールごとの許可で締める（許可の機能の鍵）が混ざる。backlog の案は「お願い」だが、お願い（読んで従う指示）ではない |
| app-tasks・subagents・plugins・code-intelligence | 出典で決まらない／値が混ざる（backlog どおり）。足していない |

## 目印を置かなかった所（未確認で文にならない）
- must-know-operations：キー 4 件（Shift+Tab ほか）は本文にバッククォートで書いたキーの名前で、「未確認」には替えられない。確認済みにしてから目印に替える
- parallel-and-loop-costs：倍率は本文が数字なしの文。目印の位置（#multiplication・#reading-examples・#misconceptions）は、確認済みにしてから足す
- after-switching-models：sonnet-4-5-retirement-date・api-version-removing-sampling-params（本文は台帳と公式への link で足りている）
- artifacts-overview：artifacts-template-availability・artifacts-required-setting（本文は公式の記事への誘導。未確認の語に替えると読めない）。storage-limit は artifacts-as-apps 側
- headless-basics：claude-code-p-write-failure-exit-code-fix-version と既存の起動の失敗の版（「入った版は更新履歴で確かめる」のまま）
- pruning-extensions：plugin-context-cost-highlight-threshold（任意）
- thinking-keywords の 2 件は未確認のまま置いた（引き上げる先・VS Code の版・無効化の版）

## 注意（検証役向け）
- 未確認 23 件の値は、提案のとおりに写した。確認日は提案の日付のまま（合流は古いほう）
- headless-basics #permissions の permission-mode-default-noninteractive の出力が長く、文長の警告が 1 件出る（DM2a の報告と同じ）
- ask-user-question-limits の選択肢の数・header の字数は Agent SDK の文書（sources に id がない）が根拠。sources に足してから確かめる
- 生成物は、check_page の `gen_site.py --page` で、変えたページと、compare の表が変わる what-survives-compaction・research-and-reports・choosing-parallel-modes だけ更新した
- 語彙の説明の文（schema/keys.yml・feature.md ほか）は触っていない
