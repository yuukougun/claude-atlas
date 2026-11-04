# review.md：verification-ladder（分かりやすさの検証と直し）

| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直す | #four-steps・#choose-step・図 | 「新しい サブエージェント」と語の前後に不要な空白があり読みにくい | 空白を外した（本文 2 か所と SVG） |
| 2 | 直したほうがよい | #what-it-prevents | 「段 1」「段 2」「段 3」が節単独で読むと何の段か分からない（U3） | 各段の中身を一言添えた（3 か所） |
| 3 | 軽い | snippets/give-a-check.expect.yaml | `features: [goal]` だが依頼の雛形は /goal を使わず、最低の版の表示が合わない | 直さず（snippets は担当外の判断）。メインに判断を依頼 |
| 4 | U6 | 全体 | write.md の対応は本文と合う。principle・prevents は #what-it-prevents で名指し、pitfalls は空。level あり、要点の最初は「何が分かるか」。技法の構成（Before/After→何が変わるか→効かない場面→誤解）に沿う | 直しなし |
| 5 | 軽い | 冒頭・U1〜U5・U8 | 冒頭は用を足し、判断例は 4 行で迷う候補も筋が通る。Before/After に注記あり。薄い節なし | 直しなし |

## 検査の結果
- `check_page.py verification-ladder`（直した後）：エラー 0・警告 0

## メインに判断してほしいこと
- 指摘 3：雛形の `features` を外すか別の値にするか（外すと tracks の最新版が出る）。雛形が最低の版を要しないなら、版の表示を出さない方法の提案が要る

## 使用量
- 道具の呼び出し：約 7 回、Web の取得：0 回
