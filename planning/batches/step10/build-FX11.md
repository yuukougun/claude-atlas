# FX11 直しの報告

全ページ check_page.py 1回、エラー0（警告は既存の textlint のみ）。

| # | ページ | 直したこと |
| --- | --- | --- |
| 1 | enforce/protected-paths | 「鍵ではなく確認」を「毎回必ず効く仕組み（鍵）で、止める代わりに確認を求める」の向きに 2 か所直した。要点の強制力は data の値のまま |
| 2 | safety/approval-fatigue | 「既定は auto」の手書きを、fact `permission-mode-default-interactive` の目印に替え、permission-modes-overview#defaults への link は残した |
| 3 | cost/how-usage-limits-work・cost/choosing-a-plan | 別の週の上限の言い切りを「公式の文書の間で書き方が分かれている」に直し、before-using-top-model#which-limit を link で指した。what-uses-up-limits は言い切りがなく直さず |
| 4 | cost/when-ai-is-unavailable | 「別の経路を使う」に check-billing-path の link を足した |
| 5 | api/long-running-agent-context | compaction・context editing がキャッシュの先頭の一致を崩す 1 文を context editing の節の後に足し、prompt-caching-in-practice#invalidation を指した |
| 6 | delegate/cloud-schedules・delegate/loop-and-scheduling | 手書きの「クラウドの定期タスク」「定期タスク」（クラウド側の話）を「クラウドの予定のタスク」「予定のタスク」にそろえた（cloud-schedules 13行、loop-and-scheduling 3か所）。choosing-automation は既に予定のタスクで直さず |
| 7 | extend/what-subagents-dont-inherit | skills の節に、手動専用のスキルは `skills` に挙げても事前の読み込みができない旨の 1 文と manual-only-skills#limits の link を足した |

## メインに判断してほしいこと
- 食い違いが残る名前：cloud-schedules の title「クラウドの定期タスク」と aliases、loop-and-scheduling の aliases（定期タスク・予定のタスク）、他ページから link される題名、term-index・by-principle・roadmap の生成物。title を data の今の名前「クラウドの予定のタスク」に合わせるか決めてほしい。
- cli/cloud-sessions-and-teleport の表のセル「クラウドの定期タスク」は、割り当て外のため直していない。
- loop-and-scheduling の Desktop 側の「定期タスク」（別の機能）は、そのままにした。
- how-usage-limits-work・choosing-a-plan の表は fact-table の生成物で、「最上位のモデルの別の週の上限」の列は Max・Ultra を「あり」と出している。data 側の見直しが要る（本文は注記で補った）。
