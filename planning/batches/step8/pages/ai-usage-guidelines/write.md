# write.md：ai-usage-guidelines（執筆）

## 書いたファイル
- `docs/team/ai-usage-guidelines.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources を [cc-docs-permissions] に。sections に check-first・how-to-check・when-it-fails の 3 節を足した。既存の 3 つの anchor は変えていない）
- `snippets/ai-usage-guidelines/team-rules.md`・`.expect.yaml`（kind: claude-md、目次の templates の案）
- `snippets/ai-usage-guidelines/deny-prohibitions.json`・`.expect.yaml`（kind: settings。禁止は A-4 の deny と組にする、という notes のために足した）
- data/sources.d は作っていない（cc-docs-permissions は data/sources.yml にある既存の id）

## 必ず持つものの対応
- 手順：`#what-to-write`（データの区分→面とモード→レビューの責任の 3 段。各段に「確かめ」）、`#lock-the-prohibitions`（禁止を鍵に移す 4 段）
- 確かめる・縛るページへの道：front matter の prerequisites（checking-ai-rules・where-your-data-goes・request-vs-lock）と related（permission-rules・managed-settings-enforcement・protecting-secrets ほか）。本文では `#check-first`・`#lock-the-prohibitions`・`#how-to-check` で link
- level：front matter の「整える」（変更なし）
- 構成の目安：要点 → `#check-first`（先に整える守り）→ `#what-to-write`・`#three-categories`・`#lock-the-prohibitions`（手順）→ `#how-to-check`（確かめ方）→ `#when-it-fails`（失敗したとき）

## メインに判断してほしいこと
- 「止まって相談する」の一行は、モデルの既定の癖に依存する旨の注記（11 第5節 A-3）。本文では「お願いで、観察として扱う」と expect に書くに留め、モデル名と確認日は書いていない。確認日を付けるなら、検証担当か作者の確認が要る
- 目次の notes にある「`data/holdout/` を禁止に挙げているのに A-4 で守っていない」は、claude-atlas 自身の雛形の話で、この辞典のページの雛形には関係しないと読んだ。雛形では .env・secrets/ を例にした

## 提案
- 用語集：「データの区分」を本文で短く定義した。必要なら用語集への追加を検討（強い提案ではない）
- front matter の提案：なし

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 4（no-doubled-joshi。リンクの題が入って「に」が重なった）。文を直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- 雛形（CLAUDE.md の 3 区分、deny の設定）は実機で試していない。deny の `Bash(git push --force *)` の書き方は、権限ルールのページ（permission-rules）の書き方と突き合わせていない
- Fedora の「AI はレビューの補助で、唯一または最終の判定者にはならない」規約（材料 2）は、出典を開いていないので名指しせず、一般の決まりとして書いた
- 日本企業の事例（材料 5）は、自己申告の数値が多く、本文に使っていない
- アプリ・API のタブの記述は束の材料と一般の説明に基づく。プラン別の扱いは where-your-data-goes に任せた
- 3 区分の A〜D の分け方は、この辞典の例であり、公式の分類ではない（根拠の印は付けていない）

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
