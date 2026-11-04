# 報告：M1（数値の取り込み・検査・判断事項のまとめ）

1. 数値：5ページの facts-proposal.yml から 15 件を `data/facts.yml` に足した（doctor-prompt-audit-since は doctor-prompt-audit-min-version と同じ値 2.1.283 なので統合し、出典は cc-docs-memory・cc-changelog の2件）。`used_in` は schema にないので写していない。出典は全件が既存の sources にあり、足さなかったものはない。`gen_site.py` を流し、docs/contest/competition-rules.md の表と nav.yml が変わった。本文の fact の目印を置く作業は書き手の担当に残る（decisions-needed.md の 19）
2. 書き方の検査：`tools/textlint_targets.py` の `--run` が、link・gen・fact の目印の間に textlint-disable／enable を足した写しで検査し、出力のパスを元に戻す（行番号は変わらず、同じ行の目印より後の桁はずれる。`--fix` のときは元のページを直す）。試験 `tests/tools/test_textlint_targets.py` に 3 件を足した。実際の textlint で、目印の中は外れ、外は検査されることを確かめた。警告は 2 件から 0 件
3. 検査：`uv run python tools/check_all.py` は 13 段のうち 11 が通り、2 が落ちた（check_templates・tests-tools の test_cli）。原因は同じで、snippets/keep-replies-in-japanese/user-settings.json の `language` が `tools/checks/template_keys.yml` の許す一覧にない。範囲外（共有の道具の設定）なので直さず、decisions-needed.md の 18 に書いた（writing-skills の `skillOverrides` も同じ表）
4. 判断事項：`planning/batches/step7/decisions-needed.md`（48 行）
