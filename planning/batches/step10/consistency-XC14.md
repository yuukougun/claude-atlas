# 工程10 整合の確認 XC14

対象：plugins-and-marketplaces・choosing-mcp-servers・code-intelligence-plugins・connecting-mcp・manual-only-skills・what-subagents-dont-inherit・pruning-extensions（docs/extend/）

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 軽い | what-subagents-dont-inherit「使うスキルは定義に書いて読ませる」と manual-only-skills「効かない場面」 | manual-only-skills は「`disable-model-invocation: true` はサブエージェントへの事前の読み込みも止める」と書く。what-subagents-dont-inherit の `skills` の節には、この例外の記述も manual-only-skills への導線もない。矛盾ではなく欠け。読者が手動専用のスキルを `skills` に挙げて読み込まれない恐れがある | 直さなかった。食い違いではなく追記の提案で、表現を決めるのはメインのため |

確認して合っていたもの：
- MCP のスコープの優先順（local、project、user、プラグイン、claude.ai）と、サンドボックスが MCP を囲わない説明は、connecting-mcp・choosing-mcp-servers・plugins-and-marketplaces で一致している。
- 強制力の語（MCP・プラグイン・code intelligence は「なし」、スキルは「お願い」、フックと道具の制限は「鍵」）は、data の値とどのページも合っている。
- コンテキストのコスト（MCP とプラグインは「使うまで小さい」）は、pruning-extensions と他のページで合っている。
- 手動専用スキルは「呼ぶまで何も載らない」という説明が、manual-only-skills と pruning-extensions で一致している。
- 持ち主のページへの link は、各ページとも正しい。

## メインに決めてほしいこと
- 軽い欠け1件：what-subagents-dont-inherit の `skills` の節に、「手動専用（`disable-model-invocation: true`）のスキルは事前の読み込みもできない」と一文足して manual-only-skills#limits へ link するか。足さなくても誤りにはならない。

## check_page.py の結果
直したページがないので流していない。

## 道具の呼び出し
Bash 6回、Write 1回（この報告）。
