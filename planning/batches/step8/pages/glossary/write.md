# glossary 執筆の報告（write）

## 書いたファイル
- `docs/start/glossary.md`（stubs/start/glossary.md を移して書いた。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（表記の正規形・モデルの性質の語・安全と拡張の語・評価の語・機能と利用の語・学びと表記の語を足した。既存の anchor は変えず）・`stage`・`updated`
- 雛形・図・sources.d は作っていない（この型は雛形なし）

## 必ず持つものの対応
- 冒頭の要点のほかに必ず持つものはない型。要点の囲みは冒頭に置いた。level なし。sources は任意で、付けていない

## メインに判断してほしいこと
- 目次の notes にある「どれも公式の日本語版の多数派を数えていない」語（fast mode・workflows・Web 検索・usage credits・アプリの Auto／Manual・Quick entry・status line・transcript の Claude Code 側・クラウドセッションの揺れ・code intelligence・agent view・背景セッション・dynamic workflows・定期タスク・旧 routines・チームメイト）は、決める作業をしていないので載せていない。決めるなら、公式の日本語版を数えてから表記の正規形に足す
- 用語集に足す語のうち、定義の根拠が「バックログの1行」だけで、持ち主のページの本文と突き合わせていないもの：red/green・凍結・OOF・認知負債・技能形成・表記の正本・漢字を開く・Topics・tool poisoning・rug pull・slopsquatting・ポストモーテム。持ち主のページ側の定義と食い違っていないか、検証の担当かメインが見てほしい

## 提案
```yaml
frontmatter:
  - {id: glossary, key: related, before: [term-index, how-to-use, four-principles, six-causes, request-vs-lock, roadmap, five-questions-before-delegating#autonomy-stages, how-memory-works, using-auto-memory, skills-in-the-app#migrated-styles, output-style-modes], after: [同左に加えて outdated-advice-ledger, over-reliance, why-hallucinations, knowledge-cutoff, measure-changes, test-the-verifier, what-auto-mode-stops], reason: "本文の link の目印が指すページ（related に無くても検査は通った）。page-links に出すかは任せる"}
```
- prh：本文の「表記の正規形」の表の語を prh の元にする。auto モード・フロントマターなどは用語集から作る既存の方針のまま
- sources：評価の語（task・trial・grader・transcript・outcome・pass@k・pass^k）の出典として Anthropic Engineering「Demystifying evals for AI agents」（https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents。check_noai.py は判定「noai の指定はない」）を data/sources に足し、このページの sources に付ける案

## 検査の結果
- 1回目：エラー 7・警告 3（前提の書き方・prh の front matter／permission mode／supporting files・助詞の重複）。すべて直した
- 2回目：エラー 0・警告 1（no-doubled-joshi の「が」）。その後、文を直したが、再検査はしていない（2回の決まり）。警告は残っている可能性がある

## 確かめていないこと
- 評価の語 7つの定義は、上の記事の本文で確かめた。それ以外の追加の語（能力の凸凹・ハルシネーション・非決定性・2つの knowledge cutoff・システムプロンプト・prompt injection・分類器・auto モード・利用上限など）は、バックログの1行と一般の理解で短く書いた。持ち主のページ・公式の一次資料とは突き合わせていない
- アプリの Topics・Pause・Reset の画面での名前と動き、アプリの effort の項目名は未確認
- 面ごとに似た名前の表は、features.yaml の note の1行（別の機能であること）に沿った。個々の機能の中身は持ち主のページを指すだけで、確かめていない
- 公式の日本語版の表記は、束の research/27 の写しによる。再数えはしていない
- link の目印が指す持ち主のページのうち、題名だけ確認したもの（using-projects・voice-and-mobile・loop-and-scheduling など）は、中身が目的に合うか見ていない

## 使用量
- 道具の呼び出し：約 14 回（Read 3・Bash 数回・Write 2・検査 2）。Web の取得：1 回（Anthropic Engineering の評価の記事）
