# バッチ4：メインが決めること

先例（rules.md）に当たらないものだけ。推す案を先に書く。

| ページ｜件｜案 |
| --- |
| let-claude-ask｜A-6 の雛形を `snippets/let-claude-ask/` に置いた。spec-first の担当が同じものを別に置くと重複する。共有の置き場所は｜`snippets/let-claude-ask/` を正本にし、spec-first と取り込みは同じ雛形を指す（spec-first の担当に、置かずに指せと伝える） |
| artifacts-overview｜#templates の表の「書き出し先」（Word・PDF・Google Docs など。確認日 2026-10-29 つきの手書き）は変わりやすい値に当たるか｜残す（形式の名前で、成熟度・プラン・上限ではない。確認日つき）。当たるとするなら列を外し、数値の提案へ移す |
| permission-modes-in-the-app｜「コネクタの許可は届く先を絞る」は束に直接の記述がない｜（推論・実践例なし）の印を付けて残した（TR4 で直した）。承認を要する公開の約束ではない |
| choosing-a-model｜原因「合っていない」の定義が site.yml と合うか（site.yml には原因の名前だけで定義の文がない）｜ページの定義（選んだモデルや effort が作業の重さに合っていない）のまま。定義の正本を design・型の手引きに置くかは作者の判断 |
| choosing-a-surface／where-it-runs／handing-long-documents／when-to-add-what｜図が無い（表で代えた）｜先例どおり図は作らない |
| usage-context-statusline｜compare 表の context-window の行が「— / —」｜推す案：表から行を外し、文で書く（data にコストと since を足すのは backlog）。足すなら data の提案を先に採る |
| when-to-plan｜「diff を一文で説明できるなら計画を省いてよい」は経験則の明記つき｜残す（この辞典の経験則と明記済み。公開の約束ではない） |
| say-what-you-want｜「禁じた語が文脈に載る」は推論と明記｜残す。フックの stderr が Claude に届く件は公式で確認済み（TR4） |
| extensions-at-a-glance｜表に「未確認」「—」が多い。「4つの層」は辞典の要約と明記｜残す。「1語で言えない」の値は backlog（data の形） |

## メインの決め（2026-11-05）

- let-claude-ask の雛形を正本にする（spec-first は重ねて置いていなかった。TR5 が確かめた）
- usage-context-statusline の compare の「— / —」の行は、data に値が入るまでそのまま（backlog）
- ほかの7行は、TR4 の推す案のとおり（残す）
